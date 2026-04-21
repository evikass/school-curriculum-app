#!/usr/bin/env node
// Convert TypeScript data files to JSON for runtime loading
// Usage: npx tsx scripts/convert-data-to-json.mjs

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const BASE_DIR = path.resolve(__dirname, '..');
const SRC_DATA_DIR = path.join(BASE_DIR, 'src', 'data', 'grades');
const PUBLIC_DATA_DIR = path.join(BASE_DIR, 'public', 'data', 'grades');

// Find all grade/subject directories
const grades = fs.readdirSync(SRC_DATA_DIR).filter(g => {
  const p = path.join(SRC_DATA_DIR, g);
  return fs.statSync(p).isDirectory();
}).sort((a, b) => parseInt(a) - parseInt(b));

let success = 0;
let failed = 0;

for (const grade of grades) {
  const gradeDir = path.join(SRC_DATA_DIR, grade);
  const subjects = fs.readdirSync(gradeDir).filter(s => {
    const p = path.join(gradeDir, s);
    return fs.statSync(p).isDirectory();
  });

  for (const subject of subjects) {
    const tsPath = path.join(gradeDir, subject, 'index.ts');
    if (!fs.existsSync(tsPath)) {
      console.log(`  SKIP: grade ${grade}/${subject} - no index.ts`);
      continue;
    }

    const outputPath = path.join(PUBLIC_DATA_DIR, grade, `${subject}.json`);
    process.stdout.write(`Converting grade ${grade}/${subject}... `);

    try {
      // Dynamic import of the TS file via tsx
      const modulePath = path.join(SRC_DATA_DIR, grade, subject, 'index.ts');
      const data = await import(modulePath);

      const result = {};
      if (data.lessons) result.lessons = data.lessons;
      if (data.games) result.games = data.games;

      if (Object.keys(result).length === 0) {
        console.log('SKIP (no exports)');
        continue;
      }

      fs.mkdirSync(path.dirname(outputPath), { recursive: true });
      fs.writeFileSync(outputPath, JSON.stringify(result, null, 1), 'utf-8');

      const size = fs.statSync(outputPath).size;
      console.log(`OK (${(size / 1024).toFixed(0)} KB)`);
      success++;
    } catch (e) {
      console.log(`FAILED: ${e.message}`);
      failed++;
    }
  }
}

console.log(`\nDone: ${success} converted, ${failed} failed`);

// Also create a manifest file listing all available grade/subject data
const manifest = {};
for (const grade of grades) {
  const gradeDir = path.join(SRC_DATA_DIR, grade);
  const subjects = fs.readdirSync(gradeDir).filter(s => {
    const p = path.join(gradeDir, s);
    return fs.statSync(p).isDirectory();
  });
  manifest[grade] = subjects;
}

const manifestPath = path.join(BASE_DIR, 'public', 'data', 'manifest.json');
fs.mkdirSync(path.dirname(manifestPath), { recursive: true });
fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2), 'utf-8');
console.log(`Manifest written to ${manifestPath}`);
