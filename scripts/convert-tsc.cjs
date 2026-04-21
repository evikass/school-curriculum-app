#!/usr/bin/env node
// Convert TS data files to JSON using tsc + vm
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const vm = require('vm');

const BASE = "/home/z/my-project/school-curriculum-app";
const SRC = path.join(BASE, "src/data/grades");
const OUT = path.join(BASE, "public/data/grades");
const TMP = "/tmp/tsc-convert";

if (fs.existsSync(TMP)) fs.rmSync(TMP, { recursive: true });
fs.mkdirSync(TMP, { recursive: true });

const grades = fs.readdirSync(SRC).filter(g => fs.statSync(path.join(SRC, g)).isDirectory()).sort((a, b) => parseInt(a) - parseInt(b));

let ok = 0, fail = 0;
const fails = [];

for (const grade of grades) {
  const gd = path.join(SRC, grade);
  const subjects = fs.readdirSync(gd).filter(s => fs.statSync(path.join(gd, s)).isDirectory());

  for (const subject of subjects) {
    const tsPath = path.join(gd, subject, "index.ts");
    if (!fs.existsSync(tsPath)) continue;

    const outPath = path.join(OUT, grade, subject + ".json");
    process.stdout.write(grade + "/" + subject + "... ");

    try {
      // Copy file to temp, replacing import
      let content = fs.readFileSync(tsPath, "utf-8");
      content = content.replace(/from\s*["']@\/data\/types["']/g, 'from "./types"');
      content = content.replace(/from\s*["']@\/data\/constants["']/g, 'from "./constants"');

      const tmpDir = path.join(TMP, grade + "_" + subject);
      fs.mkdirSync(tmpDir, { recursive: true });
      fs.writeFileSync(path.join(tmpDir, "index.ts"), content);

      // Create stub types
      fs.writeFileSync(path.join(tmpDir, "types.ts"), `
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
export function getRank(level: number): string { return ""; }
export function xpForNextLevel(level: number): number { return 100; }
`);

      fs.writeFileSync(path.join(tmpDir, "constants.ts"), `
export const XP_REWARDS: Record<string, number> = {};
export function calculateLevel(xp: number): number { return 1; }
export function levelProgress(xp: number): number { return 0; }
export function getRank(level: number): string { return ""; }
export function xpForNextLevel(level: number): number { return 100; }
`);

      // Create entry that captures exports
      const entryContent = `
import { lessons, games } from "./index";
const __result = { lessons, games };
process.stdout.write("__JSON__" + JSON.stringify(__result) + "__ENDJSON__");
`;
      fs.writeFileSync(path.join(tmpDir, "entry.ts"), entryContent);

      // Compile with tsc
      const outDir = path.join(tmpDir, "out");
      fs.mkdirSync(outDir, { recursive: true });

      try {
        execSync(
          `npx tsc ${path.join(tmpDir, "entry.ts")} --outDir ${outDir} --module esnext --target ES2020 --moduleResolution bundler --skipLibCheck --esModuleInterop --strict false --noEmitOnError false 2>&1`,
          { timeout: 30000, cwd: tmpDir, encoding: "utf-8" }
        );
      } catch (e) {
        // tsc might print errors but still produce output with --noEmitOnError false
        // Check if output file exists
      }

      // Check if JS output exists
      const jsPath = path.join(outDir, "entry.js");
      if (!fs.existsSync(jsPath)) {
        // Try alternative approach: use tsx (which uses esbuild internally but with better TS support)
        // Actually, let's try a different tsc config
        try {
          execSync(
            `npx tsc ${path.join(tmpDir, "entry.ts")} --outDir ${outDir} --module commonjs --target ES2020 --skipLibCheck --esModuleInterop --strict false --noEmitOnError false --allowImportingTsExtensions --noEmit false --declaration false 2>&1`,
            { timeout: 30000, cwd: tmpDir, encoding: "utf-8" }
          );
        } catch(e2) {}

        // Check for entry.js or entry/index.js
        const altJsPath = path.join(outDir, "entry.js");
        if (fs.existsSync(altJsPath)) {
          // Use CommonJS require
          const jsContent = fs.readFileSync(altJsPath, "utf-8");
          // Add JSON output at the end
          const modified = jsContent + '\nconst __result = { lessons: typeof lessons !== "undefined" ? lessons : undefined, games: typeof games !== "undefined" ? games : undefined }; process.stdout.write("__JSON__" + JSON.stringify(__result) + "__ENDJSON__");\n';
          fs.writeFileSync(path.join(outDir, "run.js"), modified);

          const output = execSync(`node ${path.join(outDir, "run.js")}`, { encoding: "utf-8", timeout: 10000, maxBuffer: 50*1024*1024 });
          const match = output.match(/__JSON__([\s\S]*?)__ENDJSON__/);
          if (match) {
            const data = JSON.parse(match[1]);
            const result = {};
            if (data.lessons) result.lessons = data.lessons;
            if (data.games) result.games = data.games;
            if (Object.keys(result).length > 0) {
              fs.mkdirSync(path.dirname(outPath), { recursive: true });
              fs.writeFileSync(outPath, JSON.stringify(result, null, 1), "utf-8");
              const size = fs.statSync(outPath).size;
              console.log("OK (" + (size/1024).toFixed(0) + "KB)");
              ok++;
              continue;
            }
          }
        }

        console.log("FAILED (no JS output)");
        fail++;
        fails.push(grade + "/" + subject);
        continue;
      }

      // Run the ESM output
      const output = execSync(`node ${jsPath}`, { encoding: "utf-8", timeout: 10000, maxBuffer: 50*1024*1024 });
      const match = output.match(/__JSON__([\s\S]*?)__ENDJSON__/);
      if (!match) {
        console.log("FAILED (no JSON)");
        fail++;
        fails.push(grade + "/" + subject);
        continue;
      }

      const data = JSON.parse(match[1]);
      const result = {};
      if (data.lessons) result.lessons = data.lessons;
      if (data.games) result.games = data.games;

      if (Object.keys(result).length === 0) {
        console.log("SKIP");
        continue;
      }

      fs.mkdirSync(path.dirname(outPath), { recursive: true });
      fs.writeFileSync(outPath, JSON.stringify(result, null, 1), "utf-8");
      const size = fs.statSync(outPath).size;
      console.log("OK (" + (size/1024).toFixed(0) + "KB)");
      ok++;
    } catch (e) {
      const msg = (e.message || String(e)).split("\n")[0].substring(0, 80);
      console.log("FAILED: " + msg);
      fail++;
      fails.push(grade + "/" + subject);
    }
  }
}

console.log("\nDone: " + ok + " ok, " + fail + " failed");
if (fails.length > 0) {
  console.log("Failed (" + fails.length + "): " + fails.slice(0, 20).join(", "));
}

// Manifest
const manifest = {};
for (const grade of grades) {
  const gd = path.join(SRC, grade);
  manifest[grade] = fs.readdirSync(gd).filter(s => fs.statSync(path.join(gd, s)).isDirectory());
}
fs.mkdirSync(path.join(BASE, "public/data"), { recursive: true });
fs.writeFileSync(path.join(BASE, "public/data/manifest.json"), JSON.stringify(manifest, null, 2));
console.log("Manifest written");

// Cleanup
fs.rmSync(TMP, { recursive: true });
