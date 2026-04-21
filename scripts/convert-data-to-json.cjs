#!/usr/bin/env node
// Convert TS data files to JSON using esbuild for reliable TypeScript transpilation
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const BASE_DIR = path.resolve(__dirname, '..');
const SRC_DATA_DIR = path.join(BASE_DIR, 'src/data/grades');
const PUBLIC_DATA_DIR = path.join(BASE_DIR, 'public/data/grades');
const TEMP_DIR = path.join(BASE_DIR, '.tmp-data');

// Clean temp dir
if (fs.existsSync(TEMP_DIR)) fs.rmSync(TEMP_DIR, { recursive: true });
fs.mkdirSync(TEMP_DIR, { recursive: true });

// Create stub types module for esbuild
const typesStubContent = `
export interface MatchPair { left: string; right: string; }
export interface LessonTask { type: string; question: string; options?: string[]; correctAnswer?: any; hint?: string; image?: string; pairs?: MatchPair[]; }
export interface GameLesson { title: string; subject: string; icon: string; color: string; tasks: LessonTask[]; reward?: any; }
export interface LessonItem { title: string; description: string; tasks: string[]; image?: string; content?: string; examples?: string[]; keyPoints?: string[]; facts?: string[]; }
export interface LessonTopic { topic: string; lessons: LessonItem[]; }
export interface TopicSection { title: string; description: string; icon?: string; color?: string; topics?: LessonTopic[]; }
export interface SubjectData { title: string; icon: string; color: string; topics: string[]; detailedTopics: TopicSection[]; }
export interface Subject { title: string; icon: string; color: string; topics: string[]; detailedTopics: TopicSection[]; }
export interface GradeCurriculum { grade: number; title: string; subjects: Subject[]; }
export const gradeNames: Record<number, string> = {};
export const XP_REWARDS: Record<string, number> = {};
export function calculateLevel(xp: number): number { return 1; }
export function levelProgress(xp: number): number { return 0; }
export function getRank(level: number): string { return ''; }
export function xpForNextLevel(level: number): number { return 100; }
`;
fs.writeFileSync(path.join(TEMP_DIR, 'types.ts'), typesStubContent);

const constantsStubContent = `
export const XP_REWARDS: Record<string, number> = {};
export function calculateLevel(xp: number): number { return 1; }
export function levelProgress(xp: number): number { return 0; }
export function getRank(level: number): string { return ''; }
export function xpForNextLevel(level: number): number { return 100; }
`;
fs.writeFileSync(path.join(TEMP_DIR, 'constants.ts'), constantsStubContent);

// Create tsconfig for esbuild
const tsconfig = {
  compilerOptions: {
    target: 'ES2020',
    module: 'ESNext',
    moduleResolution: 'bundler',
    strict: false,
    skipLibCheck: true,
    esModuleInterop: true,
    paths: {
      '@/data/*': [path.join(TEMP_DIR, '/*')]
    },
    baseUrl: '.'
  }
};
fs.writeFileSync(path.join(TEMP_DIR, 'tsconfig.json'), JSON.stringify(tsconfig, null, 2));

const grades = fs.readdirSync(SRC_DATA_DIR).filter(g => {
  return fs.statSync(path.join(SRC_DATA_DIR, g)).isDirectory();
}).sort((a, b) => parseInt(a) - parseInt(b));

let success = 0;
let failed = 0;
const failedList = [];

for (const grade of grades) {
  const gradeDir = path.join(SRC_DATA_DIR, grade);
  const subjects = fs.readdirSync(gradeDir).filter(s => {
    return fs.statSync(path.join(gradeDir, s)).isDirectory();
  });

  for (const subject of subjects) {
    const tsPath = path.join(gradeDir, subject, 'index.ts');
    if (!fs.existsSync(tsPath)) continue;

    const outputPath = path.join(PUBLIC_DATA_DIR, grade, `${subject}.json`);
    process.stdout.write(`Converting grade ${grade}/${subject}... `);

    try {
      // Create a temporary entry file that re-exports and captures data
      const entryContent = `
import * as data from '${tsPath}';
const result = { lessons: data.lessons, games: data.games };
process.stdout.write('__JSON_START__' + JSON.stringify(result) + '__JSON_END__');
`;
      const entryPath = path.join(TEMP_DIR, `entry_${grade}_${subject}.mjs`);
      fs.writeFileSync(entryPath, entryContent);

      // Bundle with esbuild
      const bundlePath = path.join(TEMP_DIR, `bundle_${grade}_${subject}.mjs`);
      try {
        execSync(
          `npx esbuild ${entryPath} --bundle --outfile=${bundlePath} --format=esm ` +
          `--platform=node --target=node20 --external:@/data/types --external:@/data/constants ` +
          `--alias:@/data/types=${path.join(TEMP_DIR, 'types.ts')} ` +
          `--alias:@/data/constants=${path.join(TEMP_DIR, 'constants.ts')} ` +
          `--tsconfig=${path.join(TEMP_DIR, 'tsconfig.json')} ` +
          `--log-level=error`,
          { encoding: 'utf-8', timeout: 30000, cwd: BASE_DIR }
        );
      } catch (e) {
        // Try simpler approach without aliases
        // Just replace imports in the source file
        let content = fs.readFileSync(tsPath, 'utf-8');
        content = content.replace(/from\s*['"]@\/data\/types['"]/g, `from '${path.join(TEMP_DIR, 'types.ts')}'`);
        content = content.replace(/from\s*['"]@\/data\/constants['"]/g, `from '${path.join(TEMP_DIR, 'constants.ts')}'`);
        
        const fixedPath = path.join(TEMP_DIR, `fixed_${grade}_${subject}.ts`);
        fs.writeFileSync(fixedPath, content);
        
        const entry2 = `
import * as data from '${fixedPath}';
const result = { lessons: data.lessons, games: data.games };
process.stdout.write('__JSON_START__' + JSON.stringify(result) + '__JSON_END__');
`;
        fs.writeFileSync(entryPath, entry2);
        
        execSync(
          `npx esbuild ${entryPath} --bundle --outfile=${bundlePath} --format=esm ` +
          `--platform=node --target=node20 ` +
          `--tsconfig-raw='${JSON.stringify({compilerOptions: {strict: false, skipLibCheck: true, target: 'ES2020'}})}' ` +
          `--log-level=error`,
          { encoding: 'utf-8', timeout: 30000, cwd: BASE_DIR }
        );
      }

      // Execute the bundle
      const output = execSync(`node ${bundlePath}`, { encoding: 'utf-8', timeout: 10000 });
      const jsonMatch = output.match(/__JSON_START__([\s\S]*?)__JSON_END__/);
      if (!jsonMatch) {
        console.log('FAILED: No JSON output');
        failed++;
        failedList.push(`${grade}/${subject}`);
        continue;
      }

      const data = JSON.parse(jsonMatch[1]);
      const resultData = {};
      if (data.lessons) resultData.lessons = data.lessons;
      if (data.games) resultData.games = data.games;

      if (Object.keys(resultData).length === 0) {
        console.log('SKIP (no exports)');
        continue;
      }

      fs.mkdirSync(path.dirname(outputPath), { recursive: true });
      fs.writeFileSync(outputPath, JSON.stringify(resultData, null, 1), 'utf-8');

      const size = fs.statSync(outputPath).size;
      console.log(`OK (${(size / 1024).toFixed(0)} KB)`);
      success++;
    } catch (e) {
      const msg = e.message?.split('\n')[0]?.substring(0, 100) || String(e).substring(0, 100);
      console.log(`FAILED: ${msg}`);
      failed++;
      failedList.push(`${grade}/${subject}`);
    }
  }
}

console.log(`\nDone: ${success} converted, ${failed} failed`);
if (failedList.length > 0 && failedList.length <= 30) {
  console.log('Failed:', failedList.join(', '));
} else if (failedList.length > 30) {
  console.log(`Failed: ${failedList.length} files`);
}

// Create manifest
const manifest = {};
for (const grade of grades) {
  const gradeDir = path.join(SRC_DATA_DIR, grade);
  const subjects = fs.readdirSync(gradeDir).filter(s => {
    return fs.statSync(path.join(gradeDir, s)).isDirectory();
  });
  manifest[grade] = subjects;
}
const manifestPath = path.join(BASE_DIR, 'public/data/manifest.json');
fs.mkdirSync(path.dirname(manifestPath), { recursive: true });
fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2), 'utf-8');
console.log('Manifest written');

// Cleanup
fs.rmSync(TEMP_DIR, { recursive: true });
