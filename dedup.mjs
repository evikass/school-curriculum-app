// Dedup by parsing test objects properly
import fs from 'fs';
import path from 'path';

for (let grade = 0; grade <= 11; grade++) {
  const gradeDir = path.join('./src/data/grades', String(grade));
  if (!fs.existsSync(gradeDir)) continue;
  
  for (const subj of fs.readdirSync(gradeDir)) {
    const fp = path.join(gradeDir, subj, 'index.ts');
    if (!fs.existsSync(fp)) continue;
    
    let content = fs.readFileSync(fp, 'utf-8');
    const gs = content.indexOf('export const games');
    if (gs === -1) continue;
    
    // Find = [ after export const games
    const afterGames = content.substring(gs);
    const eqBracket = afterGames.indexOf('= [');
    if (eqBracket === -1) continue;
    const aStart = gs + eqBracket + 2;
    
    // Find matching ]
    let bc = 0, aEnd = -1;
    for (let i = aStart; i < content.length; i++) {
      if (content[i] === '[') bc++;
      else if (content[i] === ']') { bc--; if (bc === 0) { aEnd = i; break; } }
    }
    if (aEnd === -1) continue;
    
    const arrStr = content.substring(aStart + 1, aEnd);
    
    // Find each top-level { } object (test)
    // Need to handle nested { } in tasks
    const objects = [];
    let depth = 0, objStart = -1;
    for (let i = 0; i < arrStr.length; i++) {
      const ch = arrStr[i];
      if (ch === '{') {
        if (depth === 0) objStart = i;
        depth++;
      } else if (ch === '}') {
        depth--;
        if (depth === 0 && objStart >= 0) {
          objects.push(arrStr.substring(objStart, i + 1));
          objStart = -1;
        }
      }
    }
    
    if (objects.length === 0) continue;
    
    // Find unique titles and remove duplicates
    const seen = new Set();
    const unique = [];
    let dups = 0;
    
    for (const obj of objects) {
      // Extract title - handle both single and double quotes
      const tm = obj.match(/title:\s*(["'])((?:(?!\1).)*)\1/);
      const title = tm ? tm[2] : '';
      
      if (title && seen.has(title)) {
        dups++;
        continue;
      }
      if (title) seen.add(title);
      unique.push(obj);
    }
    
    if (dups === 0) continue;
    
    // Rebuild the file with unique tests
    const newArr = '[\n' + unique.join(',\n') + '\n]';
    content = content.substring(0, aStart) + newArr + content.substring(aEnd + 1);
    fs.writeFileSync(fp, content);
    console.log(`G${grade}/${subj}: ${objects.length} -> ${unique.length} (-${dups})`);
  }
}
console.log('Dedup complete!');
