#!/usr/bin/env node
// Convert ALL TS data files to JSON using esbuild
const {execSync} = require('child_process');
const fs = require('fs');
const path = require('path');

const BASE = "/home/z/my-project/school-curriculum-app";
const TEMP = "/tmp/edata";
const PUBLIC_DATA = path.join(BASE, "public/data/grades");
const SRC_DATA = path.join(BASE, "src/data/grades");

if (fs.existsSync(TEMP)) fs.rmSync(TEMP, { recursive: true });
fs.mkdirSync(TEMP, { recursive: true });

// Stubs
fs.writeFileSync(path.join(TEMP, "types.ts"), "export const SubjectData={};export const GameLesson={};export const Subject={};export const LessonTask={};export const MatchPair={};export const TopicSection={};export const LessonTopic={};export const LessonItem={};");
fs.writeFileSync(path.join(TEMP, "constants.ts"), "export const XP_REWARDS={};export function calculateLevel(){return 1}export function levelProgress(){return 0}export function getRank(){return ''}export function xpForNextLevel(){return 100}");

const typesAbs = path.join(TEMP, "types.ts");
const constsAbs = path.join(TEMP, "constants.ts");

const grades = fs.readdirSync(SRC_DATA).filter(g => fs.statSync(path.join(SRC_DATA, g)).isDirectory()).sort((a, b) => parseInt(a) - parseInt(b));

// Create ALL fixed source files and entries first
const tasks = [];
for (const grade of grades) {
  const gradeDir = path.join(SRC_DATA, grade);
  const subjects = fs.readdirSync(gradeDir).filter(s => fs.statSync(path.join(gradeDir, s)).isDirectory());
  for (const subject of subjects) {
    const tsPath = path.join(gradeDir, subject, "index.ts");
    if (!fs.existsSync(tsPath)) continue;
    tasks.push({grade, subject, tsPath});
  }
}

console.log("Found " + tasks.length + " files to convert");

let success = 0;
let failed = 0;

// Process in batches of 10
for (let batch = 0; batch < tasks.length; batch += 10) {
  const batchTasks = tasks.slice(batch, batch + 10);
  
  for (const task of batchTasks) {
    const outputPath = path.join(PUBLIC_DATA, task.grade, task.subject + ".json");
    process.stdout.write(task.grade + "/" + task.subject + " ");
    
    try {
      let content = fs.readFileSync(task.tsPath, "utf-8");
      content = content.replace(/from\s*["']@\/data\/types["']/g, 'from "' + typesAbs + '"');
      content = content.replace(/from\s*["']@\/data\/constants["']/g, 'from "' + constsAbs + '"');
      
      const fixedPath = path.join(TEMP, "f_" + task.grade + "_" + task.subject + ".ts");
      fs.writeFileSync(fixedPath, content);
      
      const entryPath = path.join(TEMP, "e_" + task.grade + "_" + task.subject + ".mjs");
      fs.writeFileSync(entryPath, 'import {lessons,games} from "' + fixedPath + '";console.log(JSON.stringify({lessons,games}));');
      
      const bundlePath = path.join(TEMP, "b_" + task.grade + "_" + task.subject + ".mjs");
      execSync("npx esbuild " + entryPath + " --bundle --outfile=" + bundlePath + " --format=esm --platform=node --log-level=error", {timeout: 30000, cwd: BASE});
      
      const output = execSync("node " + bundlePath, {encoding: "utf-8", timeout: 10000, maxBuffer: 50*1024*1024});
      const data = JSON.parse(output);
      
      const resultData = {};
      if (data.lessons) resultData.lessons = data.lessons;
      if (data.games) resultData.games = data.games;
      
      if (Object.keys(resultData).length > 0) {
        fs.mkdirSync(path.dirname(outputPath), { recursive: true });
        fs.writeFileSync(outputPath, JSON.stringify(resultData, null, 1), "utf-8");
        success++;
      }
    } catch (e) {
      failed++;
    }
  }
  console.log(" [" + (batch + batchTasks.length) + "/" + tasks.length + " OK:" + success + " FAIL:" + failed + "]");
}

console.log("\nDone: " + success + " converted, " + failed + " failed");

// Manifest
const manifest = {};
for (const grade of grades) {
  const gradeDir = path.join(SRC_DATA, grade);
  manifest[grade] = fs.readdirSync(gradeDir).filter(s => fs.statSync(path.join(gradeDir, s)).isDirectory());
}
fs.mkdirSync(path.join(BASE, "public/data"), { recursive: true });
fs.writeFileSync(path.join(BASE, "public/data/manifest.json"), JSON.stringify(manifest, null, 2));
console.log("Manifest written");

// Cleanup
fs.rmSync(TEMP, { recursive: true });
