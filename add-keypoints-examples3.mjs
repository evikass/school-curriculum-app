import fs from 'fs';
import path from 'path';

const GRADE10_DIR = '/home/z/my-project/school-curriculum-app/src/data/grades/10';

// Content data - same as before, imported from separate data file
import {contentData} from './add-keypoints-data.mjs';

function escapeRegex(str) {
  return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function formatArray(items, indent) {
  const lines = items.map((item, i) => {
    const comma = i < items.length - 1 ? ',' : '';
    const escaped = item.replace(/'/g, "\\'");
    return `${indent}'${escaped}'${comma}`;
  });
  return '[\n' + lines.join('\n') + '\n' + indent.slice(0, -2) + ']';
}

/**
 * Find the end of a createLesson call by tracking string contexts
 * Returns the index of the closing ')' of createLesson
 */
function findCreateLessonEnd(content, startPos) {
  let i = startPos;
  let templateDepth = 0; // backtick strings
  
  while (i < content.length) {
    const ch = content[i];
    
    if (ch === '`') {
      if (templateDepth === 0) {
        templateDepth = 1;
        // Check for template expression ${
        i++;
        while (i < content.length && templateDepth > 0) {
          if (content[i] === '\\') { i += 2; continue; }
          if (content[i] === '`') { templateDepth = 0; i++; break; }
          if (content[i] === '$' && content[i+1] === '{') {
            // Template expression - track nested braces
            let braceDepth = 1;
            i += 2;
            while (i < content.length && braceDepth > 0) {
              if (content[i] === '\\') { i += 2; continue; }
              if (content[i] === '{') braceDepth++;
              if (content[i] === '}') braceDepth--;
              if (braceDepth > 0) {
                // Track strings inside template expression
                if (content[i] === '"') { 
                  i++;
                  while (i < content.length && content[i] !== '"') { if (content[i] === '\\') i++; i++; }
                }
                if (content[i] === "'") { 
                  i++;
                  while (i < content.length && content[i] !== "'") { if (content[i] === '\\') i++; i++; }
                }
              }
              i++;
            }
            continue;
          }
          i++;
        }
        continue;
      }
    }
    
    if (templateDepth > 0) { i++; continue; }
    
    // Outside of template strings - track regular strings
    if (ch === '"') {
      i++;
      while (i < content.length && content[i] !== '"') { if (content[i] === '\\') i++; i++; }
      i++; continue;
    }
    if (ch === "'") {
      i++;
      while (i < content.length && content[i] !== "'") { if (content[i] === '\\') i++; i++; }
      i++; continue;
    }
    
    // Track parentheses
    if (ch === '(') { i++; continue; }
    if (ch === ')') { return i; }
    
    i++;
  }
  return -1;
}

function processFile(filePath, subjectName, data) {
  console.log(`Processing ${subjectName}...`);
  let content = fs.readFileSync(filePath, 'utf-8');
  
  // Step 1: Update helper
  const oldHelper = /const createLesson = \(title: string, description: string, tasks: string\[\]\) => \(\{\s*title, description, tasks\s*\}\)/;
  if (oldHelper.test(content)) {
    content = content.replace(
      oldHelper,
      `const createLesson = (title: string, description: string, tasks: string[], examples?: string[], keyPoints?: string[]) => ({ title, description, tasks, examples, keyPoints })`
    );
    console.log(`  Updated createLesson helper`);
  }
  
  // Step 2: For each lesson, find and add data
  // Process lessons in reverse order to avoid offset issues
  const lessonEntries = Object.entries(data.lessons);
  let modified = 0;
  const results = [];
  
  for (const [lessonTitle, lessonData] of lessonEntries) {
    const escapedTitle = escapeRegex(lessonTitle);
    const startPattern = new RegExp(`createLesson\\("([^"]*${escapedTitle}[^"]*)"`);
    const startMatch = content.match(startPattern);
    
    if (!startMatch) {
      console.log(`  WARNING: Could not find lesson "${lessonTitle}"`);
      continue;
    }
    
    const startPos = content.indexOf(startMatch[0]);
    
    // Find the end of createLesson using string-aware parsing
    const endPos = findCreateLessonEnd(content, startPos);
    
    if (endPos === -1) {
      console.log(`  WARNING: Could not find end of lesson "${lessonTitle}"`);
      continue;
    }
    
    // Get the full createLesson call content
    const callContent = content.substring(startPos, endPos + 1);
    
    // Check if this lesson already has examples/keyPoints
    if (callContent.includes('examples:') || callContent.includes('keyPoints:')) {
      console.log(`  SKIP: "${lessonTitle}" already has examples/keyPoints`);
      continue;
    }
    
    // Find the last ]),  pattern - the tasks array close + createLesson close
    // Look backwards from endPos for ]\n
    let tasksCloseIdx = -1;
    for (let j = endPos - 1; j >= startPos; j--) {
      if (content[j] === ']') {
        tasksCloseIdx = j;
        break;
      }
    }
    
    if (tasksCloseIdx === -1) {
      console.log(`  WARNING: Could not find tasks end for "${lessonTitle}"`);
      continue;
    }
    
    // Determine indentation from context
    const lineStart = content.lastIndexOf('\n', tasksCloseIdx) + 1;
    const lineBefore = content.substring(lineStart, tasksCloseIdx);
    const baseIndent = lineBefore.match(/^(\s*)/)[1];
    const itemIndent = baseIndent + '          ';
    
    const examplesStr = formatArray(lessonData.examples, itemIndent);
    const keyPointsStr = formatArray(lessonData.keyPoints, itemIndent);
    
    results.push({
      startPos: tasksCloseIdx,
      endPos: endPos + 1,
      lessonTitle,
      examplesStr,
      keyPointsStr
    });
    modified++;
  }
  
  // Apply modifications in reverse order (from end of file to start)
  results.sort((a, b) => b.endPos - a.endPos);
  
  for (const r of results) {
    const oldText = content.substring(r.startPos, r.endPos);
    const newText = `],\n        ${r.examplesStr},\n        ${r.keyPointsStr}\n      )`;
    content = content.substring(0, r.startPos) + newText + content.substring(r.endPos);
  }
  
  fs.writeFileSync(filePath, content, 'utf-8');
  console.log(`  Modified ${modified} lessons`);
  return modified;
}

// Main
console.log('=== Grade 10: Adding keyPoints and examples ===\n');
let totalModified = 0;

for (const [subjectName, data] of Object.entries(contentData)) {
  const filePath = path.join(GRADE10_DIR, subjectName, 'index.ts');
  if (fs.existsSync(filePath)) {
    totalModified += processFile(filePath, subjectName, data);
  } else {
    console.log(`  File not found: ${filePath}`);
  }
}

console.log(`\n=== Done! Total lessons modified: ${totalModified} ===`);
