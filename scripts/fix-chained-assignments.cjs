#!/usr/bin/env node
// Fix chained assignment pattern in games exports:
// export const games: GameLesson[] = [...] = [...] = [...]
// Should be: export const games = [...]  (keep only the LAST array)
const fs = require('fs');
const path = require('path');

const SRC_DATA_DIR = path.resolve(__dirname, '..', 'src/data/grades');
const grades = fs.readdirSync(SRC_DATA_DIR).filter(g => {
  return fs.statSync(path.join(SRC_DATA_DIR, g)).isDirectory();
});

let fixed = 0;
let skipped = 0;

for (const grade of grades) {
  const gradeDir = path.join(SRC_DATA_DIR, grade);
  const subjects = fs.readdirSync(gradeDir).filter(s => {
    return fs.statSync(path.join(gradeDir, s)).isDirectory();
  });

  for (const subject of subjects) {
    const tsPath = path.join(gradeDir, subject, 'index.ts');
    if (!fs.existsSync(tsPath)) continue;

    const content = fs.readFileSync(tsPath, 'utf-8');

    // Check if this file has the chained assignment pattern
    // Pattern: a line that starts with "] = [" (after the first games array closes)
    if (!/^\]\s*=\s*\[/gm.test(content)) {
      skipped++;
      continue;
    }

    // Strategy: Find the games export, then find all ] = [ line positions
    // Keep only the last array by replacing:
    //   export const games: GameLesson[] = [first_array_content] = [second...] = [ 
    // with:
    //   export const games = [
    // and keep everything from the last [ onwards
    
    const lines = content.split('\n');
    
    // Find the games export line
    let gamesLineIdx = -1;
    for (let i = 0; i < lines.length; i++) {
      if (/^export\s+const\s+games/.test(lines[i].trim())) {
        gamesLineIdx = i;
        break;
      }
    }
    
    if (gamesLineIdx === -1) {
      console.log(`  ${grade}/${subject}: No games export found, skipping`);
      continue;
    }
    
    // Find all lines that start with "] = [" after the games line
    const chainLineIndices = [];
    for (let i = gamesLineIdx + 1; i < lines.length; i++) {
      if (/^\]\s*=\s*\[/.test(lines[i].trim())) {
        chainLineIndices.push(i);
      }
    }
    
    if (chainLineIndices.length === 0) {
      skipped++;
      continue;
    }
    
    // The last chain line is where the final array starts
    // We want to keep: everything before gamesLineIdx + the games export + the last array + closing
    const lastChainIdx = chainLineIndices[chainLineIndices.length - 1];
    
    // Build new content:
    // 1. Everything before gamesLineIdx
    // 2. "export const games = [" (new games line)
    // 3. Everything from lastChainIdx+1 to end (the final array content and closing bracket)
    
    const before = lines.slice(0, gamesLineIdx).join('\n');
    const after = lines.slice(lastChainIdx + 1).join('\n');
    
    const newContent = before + '\nexport const games = [\n' + after + '\n';
    
    fs.writeFileSync(tsPath, newContent, 'utf-8');
    fixed++;
    console.log(`  Fixed ${grade}/${subject} (${chainLineIndices.length} chains removed)`);
  }
}

console.log(`\nDone: ${fixed} fixed, ${skipped} skipped (no chains)`);
