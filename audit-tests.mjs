import fs from 'fs';
import path from 'path';

const gradesDir = './src/data/grades';

function countLessons(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  // Count lesson entries - look for "title:" inside lessons arrays
  const lessonMatches = content.match(/title:\s*["']Урок \d+/g);
  return lessonMatches ? lessonMatches.length : 0;
}

function countGames(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  // Count game entries in the games array
  const gamesMatches = content.match(/title:\s*["'][^"']+["'],?\s*\n\s*subject:/g);
  return gamesMatches ? gamesMatches.length : 0;
}

function getLessonTitles(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  const matches = [...content.matchAll(/title:\s*["']([^"']+)["']/g)];
  // Filter only lesson titles (Урок pattern or similar)
  return matches.map(m => m[1]).filter(t => t.match(/^Урок\s*\d/));
}

function getGameTitles(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  // Find the games array and extract titles
  const gamesSection = content.indexOf('export const games');
  if (gamesSection === -1) return [];
  
  const gamesContent = content.substring(gamesSection);
  const matches = [...gamesContent.matchAll(/title:\s*["']([^"']+)["']/g)];
  // Only get titles within the games array (before the closing ])
  const titles = [];
  let depth = 0;
  let inGames = false;
  
  for (const match of matches) {
    const idx = gamesContent.indexOf(match[0]);
    if (!inGames) {
      // Find opening bracket
      const bracketIdx = gamesContent.indexOf('[', gamesContent.indexOf('games'));
      if (idx > bracketIdx) inGames = true;
    }
    if (inGames) {
      titles.push(match[1]);
      // Check if this is the last title (rough heuristic)
      if (titles.length > 50) break; // safety
    }
  }
  return titles;
}

const grades = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
const subjectMap = {
  'russian': 'Русский язык', 'literature': 'Литература', 'math': 'Математика',
  'world': 'Окр. мир', 'english': 'Английский', 'reading': 'Чтение',
  'tech': 'Технология', 'art': 'ИЗО', 'music': 'Музыка', 'pe': 'Физкультура',
  'craft': 'Лепка', 'crafts': 'Ремесло', 'projects': 'Проекты',
  'informatics': 'Информатика', 'robotics': 'Робототехника',
  'geography': 'География', 'history': 'История', 'biology': 'Биология',
  'physics': 'Физика', 'chemistry': 'Химия', 'nature': 'Природоведение',
  'safety': 'ОБЖ', 'social': 'Обществознание', 'coding': 'Программирование',
  'ecology': 'Экология', 'digital': 'Цифровая грамотность', 'finance': 'Финансы',
  'religion': 'ОДНКНР', 'ethics': 'Этика', 'algebra': 'Алгебра',
  'geometry': 'Геометрия', 'law': 'Право', 'economy': 'Экономика',
  'astronomy': 'Астрономия', 'ege': 'ЕГЭ', 'lab': 'Лаборатории',
  'philosophy': 'Философия', 'business': 'Бизнес', 'career': 'Карьера',
  'oge': 'ОГЭ', 'psychology': 'Психология'
};

let totalMissing = 0;
const missingReport = [];

for (const grade of grades) {
  const gradeDir = path.join(gradesDir, String(grade));
  if (!fs.existsSync(gradeDir)) continue;
  
  const subjects = fs.readdirSync(gradeDir).filter(f => 
    fs.statSync(path.join(gradeDir, f)).isDirectory()
  );
  
  for (const subject of subjects) {
    const idxFile = path.join(gradeDir, subject, 'index.ts');
    if (!fs.existsSync(idxFile)) continue;
    
    const lessonCount = countLessons(idxFile);
    const gameCount = countGames(idxFile);
    
    if (lessonCount === 0) continue; // No lessons = skip
    
    if (gameCount < lessonCount) {
      const missing = lessonCount - gameCount;
      totalMissing += missing;
      const subjectName = subjectMap[subject] || subject;
      missingReport.push(`  Класс ${grade} - ${subjectName} (${subject}): уроков ${lessonCount}, тестов ${gameCount}, НЕ ХВАТАЕТ ${missing}`);
    }
  }
}

console.log(`\n=== АУДИТ ТЕСТОВ ===`);
console.log(`Всего не хватает тестов: ${totalMissing}\n`);
console.log(`Где не хватает:\n`);
for (const line of missingReport) {
  console.log(line);
}
