// Proper audit: count lessons accurately and tests accurately
import fs from 'fs';
import path from 'path';

function analyzeFile(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  
  // Get subject title (first title field)
  const titleMatch = content.match(/title:\s*['"](.+?)['"]/);
  const subjectTitle = titleMatch ? titleMatch[1] : null;
  
  // Count lessons: find detailedTopics section, count titles with indent > topic level
  const dtStart = content.indexOf('detailedTopics');
  const gamesStart = content.indexOf('export const games');
  let lessonCount = 0;
  
  if (dtStart >= 0) {
    const dtEnd = gamesStart >= 0 ? gamesStart : content.length;
    const dtSection = content.substring(dtStart, dtEnd);
    
    // Count title entries that are actual lessons (have tasks or description nearby)
    // Pattern: lines with title: '...' that are followed by description or tasks
    const lessonRegex = /title:\s*['"]([^'"]+)['"]\s*,\s*\n\s*(?:description|tasks|content|theory)/g;
    const matches = [...dtSection.matchAll(lessonRegex)];
    lessonCount = matches.length;
    
    // Fallback: if no matches, count by createLesson
    if (lessonCount === 0) {
      const createMatches = [...dtSection.matchAll(/createLesson\(/g)];
      lessonCount = createMatches.length;
    }
    
    // Another fallback: count titles with sufficient indent
    if (lessonCount === 0) {
      const lines = dtSection.split('\n');
      for (const line of lines) {
        const indent = line.length - line.trimStart().length;
        if (line.includes('title:') && indent >= 8 && !line.includes('topic:')) {
          lessonCount++;
        }
      }
    }
  }
  
  // Count games: count tasks: [ occurrences in games section
  let gameCount = 0;
  if (gamesStart >= 0) {
    const gamesSection = content.substring(gamesStart);
    gameCount = (gamesSection.match(/tasks:\s*\[/g) || []).length;
  }
  
  // Get unique game titles (to detect duplicates)
  const gameTitles = [];
  if (gamesStart >= 0) {
    const gamesSection = content.substring(gamesStart);
    const titleRegex = /title:\s*['"]([^'"]+)['"]/g;
    let m;
    while ((m = titleRegex.exec(gamesSection)) !== null) {
      gameTitles.push(m[1]);
    }
  }
  const uniqueGameTitles = new Set(gameTitles);
  const duplicateCount = gameTitles.length - uniqueGameTitles.size;
  
  return { subjectTitle, lessonCount, gameCount, uniqueGameCount: uniqueGameTitles.size, duplicateCount, gameTitles: [...uniqueGameTitles] };
}

// Also count legacy games per grade/subject
function countLegacyGames(gradeDir) {
  const legacyDir = path.join('./src/data/games', `grade-${gradeDir}`);
  const legacyFile = path.join(legacyDir, 'index.ts');
  if (!fs.existsSync(legacyFile)) return {};
  
  const content = fs.readFileSync(legacyFile, 'utf-8');
  const subjectCount = {};
  const regex = /subject:\s*['"]([^'"]+)['"]/g;
  let m;
  while ((m = regex.exec(content)) !== null) {
    subjectCount[m[1]] = (subjectCount[m[1]] || 0) + 1;
  }
  return subjectCount;
}

console.log('=== COMPREHENSIVE AUDIT ===\n');

let totalOk = 0, totalMissing = 0, totalDuplicates = 0;
const missingList = [];

for (let grade = 0; grade <= 11; grade++) {
  const gradeDir = path.join('./src/data/grades', String(grade));
  if (!fs.existsSync(gradeDir)) continue;
  
  const subjects = fs.readdirSync(gradeDir).filter(s => fs.existsSync(path.join(gradeDir, s, 'index.ts')));
  const legacyGames = countLegacyGames(grade);
  
  for (const subj of subjects) {
    const filePath = path.join(gradeDir, subj, 'index.ts');
    const info = analyzeFile(filePath);
    
    if (!info.subjectTitle) continue;
    
    const legacy = legacyGames[info.subjectTitle] || 0;
    const totalTests = info.uniqueGameCount + legacy;
    const missing = info.lessonCount - totalTests;
    
    if (info.duplicateCount > 0) {
      totalDuplicates += info.duplicateCount;
    }
    
    if (missing > 0) {
      totalMissing += missing;
      missingList.push({ grade, subj, title: info.subjectTitle, lessons: info.lessonCount, tests: totalTests, missing, duplicates: info.duplicateCount });
    } else {
      totalOk++;
    }
  }
}

missingList.sort((a, b) => b.missing - a.missing);

console.log(`OK (enough tests): ${totalOk} subjects`);
console.log(`MISSING tests: ${missingList.length} subjects (${totalMissing} tests needed)`);
console.log(`DUPLICATES found: ${totalDuplicates} test entries`);
console.log();

if (missingList.length > 0) {
  console.log('=== Subjects needing tests ===');
  for (const m of missingList) {
    const dupStr = m.duplicates > 0 ? ` [${m.duplicates} duplicates!]` : '';
    console.log(`  G${m.grade} ${m.title}: ${m.lessons}L / ${m.tests}T = -${m.missing}${dupStr}`);
  }
}
