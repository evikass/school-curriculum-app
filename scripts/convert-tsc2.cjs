#!/usr/bin/env node
// Convert ALL TS data files to JSON using tsc (TypeScript compiler)
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const BASE = "/home/z/my-project/school-curriculum-app";
const SRC = path.join(BASE, "src/data/grades");
const OUT = path.join(BASE, "public/data/grades");
const TMP = "/tmp/tc";

if (fs.existsSync(TMP)) fs.rmSync(TMP, { recursive: true });
fs.mkdirSync(TMP, { recursive: true });

// Shared stubs
const TYPES_TS = `
export interface MatchPair { left: string; right: string; }
export interface LessonTask { type: string; question: string; options?: string[]; correctAnswer?: any; hint?: string; image?: string; pairs?: MatchPair[]; }
export interface GameLesson { title: string; subject: string; icon: string; color: string; tasks: LessonTask[]; reward?: any; }
export interface LessonItem { title: string; description: string; tasks: string[]; image?: string; content?: string; examples?: string[]; keyPoints?: string[]; facts?: string[]; }
export interface LessonTopic { topic: string; lessons: LessonItem[]; }
export interface TopicSection { title: string; description: string; icon?: string; color?: string; topics?: LessonTopic[]; [key: string]: any; }
export interface SubjectData { title: string; icon: string; color: string; topics: string[]; detailedTopics: TopicSection[]; [key: string]: any; }
export interface Subject { title: string; icon: string; color: string; topics: string[]; detailedTopics: TopicSection[]; [key: string]: any; }
export interface GradeCurriculum { grade: number; title: string; subjects: Subject[]; }
export const gradeNames: Record<number, string> = {};
export const XP_REWARDS: Record<string, number> = {};
export function calculateLevel(xp: number): number { return 1; }
export function levelProgress(xp: number): number { return 0; }
export function getRank(level: number): string { return ""; }
export function xpForNextLevel(level: number): number { return 100; }
`;

const CONSTANTS_TS = `
export const XP_REWARDS: Record<string, number> = {};
export function calculateLevel(xp: number): number { return 1; }
export function levelProgress(xp: number): number { return 0; }
export function getRank(level: number): string { return ""; }
export function xpForNextLevel(level: number): number { return 100; }
`;

fs.writeFileSync(path.join(TMP, "types.ts"), TYPES_TS);
fs.writeFileSync(path.join(TMP, "constants.ts"), CONSTANTS_TS);

const grades = fs.readdirSync(SRC).filter(g => fs.statSync(path.join(SRC, g)).isDirectory()).sort((a, b) => parseInt(a) - parseInt(b));

let ok = 0, fail = 0;

for (const grade of grades) {
  const gd = path.join(SRC, grade);
  const subjects = fs.readdirSync(gd).filter(s => fs.statSync(path.join(gd, s)).isDirectory());

  for (const subject of subjects) {
    const tsPath = path.join(gd, subject, "index.ts");
    if (!fs.existsSync(tsPath)) continue;

    const outPath = path.join(OUT, grade, subject + ".json");
    process.stdout.write(grade + "/" + subject + " ");

    try {
      // Create temp dir for this conversion
      const td = path.join(TMP, grade + "_" + subject);
      fs.mkdirSync(td, { recursive: true });

      // Copy and fix imports
      let content = fs.readFileSync(tsPath, "utf-8");
      content = content.replace(/from\s*["']@\/data\/types["']/g, 'from "' + path.join(TMP, "types.ts") + '"');
      content = content.replace(/from\s*["']@\/data\/constants["']/g, 'from "' + path.join(TMP, "constants.ts") + '"');
      fs.writeFileSync(path.join(td, "data.ts"), content);

      // Create entry file
      const entryContent = `export { lessons, games } from "./data";\n`;
      fs.writeFileSync(path.join(td, "entry.ts"), entryContent);

      // Compile
      const outDir = path.join(td, "out");
      fs.mkdirSync(outDir, { recursive: true });

      execSync(
        `npx tsc ${path.join(td, "entry.ts")} --outDir ${outDir} --module commonjs --target ES2020 --skipLibCheck --esModuleInterop --strict false --noEmitOnError false 2>/dev/null`,
        { timeout: 60000 }
      );

      // Require the compiled JS
      const indexPath = path.join(outDir, "data.js");
      if (!fs.existsSync(indexPath)) {
        console.log("X");
        fail++;
        continue;
      }

      const data = require(indexPath);
      const result = {};
      if (data.lessons) result.lessons = data.lessons;
      if (data.games) result.games = data.games;

      if (Object.keys(result).length === 0) {
        console.log("-");
        continue;
      }

      fs.mkdirSync(path.dirname(outPath), { recursive: true });
      fs.writeFileSync(outPath, JSON.stringify(result, null, 1), "utf-8");
      ok++;
    } catch (e) {
      fail++;
    }

    // Clean this temp dir
    const td = path.join(TMP, grade + "_" + subject);
    if (fs.existsSync(td)) fs.rmSync(td, { recursive: true });
  }
  console.log("");
}

console.log("Done: " + ok + " ok, " + fail + " failed");

// Manifest
const manifest = {};
for (const grade of grades) {
  const gd = path.join(SRC, grade);
  manifest[grade] = fs.readdirSync(gd).filter(s => fs.statSync(path.join(gd, s)).isDirectory());
}
fs.mkdirSync(path.join(BASE, "public/data"), { recursive: true });
fs.writeFileSync(path.join(BASE, "public/data/manifest.json"), JSON.stringify(manifest, null, 2));
console.log("Manifest written");

fs.rmSync(TMP, { recursive: true });
