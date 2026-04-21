#!/usr/bin/env node
const {execSync} = require("child_process");
const fs = require("fs");
const path = require("path");

const BASE = "/home/z/my-project/school-curriculum-app";
const TEMP = "/tmp/esbuild-convert";
const PUBLIC_DATA = path.join(BASE, "public/data/grades");
const SRC_DATA = path.join(BASE, "src/data/grades");

// Setup temp
if (fs.existsSync(TEMP)) fs.rmSync(TEMP, { recursive: true });
fs.mkdirSync(TEMP, { recursive: true });

// Create types stub
fs.writeFileSync(path.join(TEMP, "types.ts"), `
export const SubjectData = class {};
export const GameLesson = class {};
export const Subject = class {};
export const LessonTask = class {};
export const MatchPair = class {};
export const TopicSection = class {};
export const LessonTopic = class {};
export const LessonItem = class {};
`);

// Create constants stub
fs.writeFileSync(path.join(TEMP, "constants.ts"), `
export const XP_REWARDS = {};
export function calculateLevel(xp) { return 1; }
export function levelProgress(xp) { return 0; }
export function getRank(level) { return ""; }
export function xpForNextLevel(level) { return 100; }
`);

const typesPath = path.join(TEMP, "types.ts");
const constantsPath = path.join(TEMP, "constants.ts");

// Find all grade/subject directories
const grades = fs.readdirSync(SRC_DATA).filter(g => {
  return fs.statSync(path.join(SRC_DATA, g)).isDirectory();
}).sort((a, b) => parseInt(a) - parseInt(b));

let success = 0;
let failed = 0;
const failedList = [];

for (const grade of grades) {
  const gradeDir = path.join(SRC_DATA, grade);
  const subjects = fs.readdirSync(gradeDir).filter(s => {
    return fs.statSync(path.join(gradeDir, s)).isDirectory();
  });

  for (const subject of subjects) {
    const tsPath = path.join(gradeDir, subject, "index.ts");
    if (!fs.existsSync(tsPath)) continue;

    const outputPath = path.join(PUBLIC_DATA, grade, subject + ".json");
    process.stdout.write("Converting grade " + grade + "/" + subject + "... ");

    try {
      // Fix imports in the source
      let content = fs.readFileSync(tsPath, "utf-8");
      content = content.replace(/from\s*["']@\/data\/types["']/g, 'from "' + typesPath + '"');
      content = content.replace(/from\s*["']@\/data\/constants["']/g, 'from "' + constantsPath + '"');

      const fixedPath = path.join(TEMP, "fixed_" + grade + "_" + subject + ".ts");
      fs.writeFileSync(fixedPath, content);

      // Create entry point
      const entryPath = path.join(TEMP, "entry_" + grade + "_" + subject + ".mjs");
      const entryContent = 'import { lessons, games } from "' + fixedPath + '";\nconsole.log(JSON.stringify({lessons, games}));\n';
      fs.writeFileSync(entryPath, entryContent);

      // Bundle with esbuild
      const bundlePath = path.join(TEMP, "bundle_" + grade + "_" + subject + ".mjs");
      execSync(
        "npx esbuild " + entryPath + " --bundle --outfile=" + bundlePath + " --format=esm --platform=node --log-level=error",
        { timeout: 30000, cwd: BASE }
      );

      // Run the bundle
      const output = execSync("node " + bundlePath, {
        encoding: "utf-8",
        timeout: 10000,
        maxBuffer: 50 * 1024 * 1024
      });

      const data = JSON.parse(output);
      const resultData = {};
      if (data.lessons) resultData.lessons = data.lessons;
      if (data.games) resultData.games = data.games;

      if (Object.keys(resultData).length === 0) {
        console.log("SKIP (no exports)");
        continue;
      }

      fs.mkdirSync(path.dirname(outputPath), { recursive: true });
      fs.writeFileSync(outputPath, JSON.stringify(resultData, null, 1), "utf-8");

      const size = fs.statSync(outputPath).size;
      console.log("OK (" + (size / 1024).toFixed(0) + " KB)");
      success++;
    } catch (e) {
      const msg = (e.message || String(e)).split("\n")[0].substring(0, 100);
      console.log("FAILED: " + msg);
      failed++;
      failedList.push(grade + "/" + subject);
    }
  }
}

console.log("\nDone: " + success + " converted, " + failed + " failed");
if (failedList.length > 0) {
  console.log("Failed: " + failedList.length + " files");
  if (failedList.length <= 30) console.log(failedList.join(", "));
}

// Create manifest
const manifest = {};
for (const grade of grades) {
  const gradeDir = path.join(SRC_DATA, grade);
  const subjects = fs.readdirSync(gradeDir).filter(s => {
    return fs.statSync(path.join(gradeDir, s)).isDirectory();
  });
  manifest[grade] = subjects;
}
const manifestPath = path.join(BASE, "public/data/manifest.json");
fs.mkdirSync(path.dirname(manifestPath), { recursive: true });
fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2), "utf-8");
console.log("Manifest written");

// Cleanup
fs.rmSync(TEMP, { recursive: true });
