import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
import path from 'path';

const DATA_DIR = './src/data/grades';

// Subjects needing tests: { grade, subjectDir, subjectTitle, missingCount }
const TARGETS = [
  // Grade 10 - biggest gaps (no games export at all)
  { grade: 10, dir: 'coding', title: 'Программирование', missing: 32 },
  { grade: 10, dir: 'economy', title: 'Экономика', missing: 32 },
  { grade: 10, dir: 'lab', title: null, missing: 1 },
  { grade: 10, dir: 'philosophy', title: null, missing: 1 },
  // Grade 9
  { grade: 9, dir: 'algebra', title: null, missing: 15 },
  { grade: 9, dir: 'informatics', title: null, missing: 2 },
  // Grade 11
  { grade: 11, dir: 'algebra', title: null, missing: 13 },
  // Grade 5
  { grade: 5, dir: 'biology', title: null, missing: 12 },
  { grade: 5, dir: 'music', title: null, missing: 12 },
  { grade: 5, dir: 'pe', title: null, missing: 12 },
  { grade: 5, dir: 'crafts', title: null, missing: 11 },
  { grade: 5, dir: 'digital', title: null, missing: 10 },
  { grade: 5, dir: 'finance', title: null, missing: 10 },
  { grade: 5, dir: 'informatics', title: null, missing: 8 },
  { grade: 5, dir: 'robotics', title: null, missing: 10 },
  // Grade 6
  { grade: 6, dir: 'chemistry', title: null, missing: 10 },
  { grade: 6, dir: 'crafts', title: null, missing: 10 },
  { grade: 6, dir: 'ecology', title: null, missing: 9 },
  { grade: 6, dir: 'informatics', title: null, missing: 9 },
  { grade: 6, dir: 'physics', title: null, missing: 9 },
  { grade: 6, dir: 'robotics', title: null, missing: 9 },
  { grade: 6, dir: 'social', title: null, missing: 9 },
  { grade: 6, dir: 'math', title: null, missing: 4 },
  // Grade 3
  { grade: 3, dir: 'art', title: null, missing: 7 },
  { grade: 3, dir: 'informatics', title: null, missing: 8 },
  { grade: 3, dir: 'pe', title: null, missing: 8 },
  { grade: 3, dir: 'safety', title: null, missing: 7 },
  { grade: 3, dir: 'music', title: null, missing: 4 },
  { grade: 3, dir: 'tech', title: null, missing: 4 },
  // Grade 8
  { grade: 8, dir: 'coding', title: null, missing: 6 },
  { grade: 8, dir: 'russian', title: null, missing: 3 },
  // Grade 2
  { grade: 2, dir: 'english', title: null, missing: 3 },
  { grade: 2, dir: 'projects', title: null, missing: 5 },
];

function extractLessonInfo(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  
  // Extract subject title
  let subjectTitle = null;
  let icon = 'BookOpen';
  let color = 'text-blue-400';
  
  const titleMatch = content.match(/title:\s*['"](.+?)['"]/);
  if (titleMatch) subjectTitle = titleMatch[1];
  
  const iconMatch = content.match(/icon:\s*['"](.+?)['"]/);
  if (iconMatch) icon = iconMatch[1];
  
  const colorMatch = content.match(/color:\s*['"](.+?)['"]/);
  if (colorMatch) color = colorMatch[1];
  
  // Extract lesson titles
  const lessonTitles = [];
  const lessonRegex = /(?:title:\s*|createLesson\(\s*['"])(Урок \d+[:\s].+?)[.'"`]/g;
  let match;
  while ((match = lessonRegex.exec(content)) !== null) {
    lessonTitles.push(match[1].trim());
  }
  
  // Extract existing game titles
  const existingGames = [];
  const gameRegex = /title:\s*['"](.+?)['"]/g;
  const gamesSection = content.indexOf('export const games');
  if (gamesSection !== -1) {
    const gamesContent = content.substring(gamesSection);
    let gMatch;
    while ((gMatch = gameRegex.exec(gamesContent)) !== null) {
      existingGames.push(gMatch[1].trim());
    }
  }
  
  // Extract existing games array for reference
  let hasGamesExport = content.includes('export const games');
  
  return { subjectTitle, icon, color, lessonTitles, existingGames, hasGamesExport, content };
}

async function generateTestsForSubject(zai, grade, dir, subjectTitle, icon, color, lessonTitles, existingGameTitles, missingCount, allLessonDescriptions) {
  // Determine which lessons need tests
  const lessonsNeedingTests = lessonTitles.filter(lt => {
    // Check if any existing game covers this lesson (by topic match)
    return !existingGameTitles.some(egt => {
      const ltLower = lt.toLowerCase();
      const egtLower = egt.toLowerCase();
      return ltLower.includes(egtLower.split(' ')[0]) || egtLower.includes(ltLower.split(' ')[0]);
    });
  });
  
  if (lessonsNeedingTests.length === 0) {
    // Fallback: generate tests for the last N lessons
    const startIdx = Math.max(0, lessonTitles.length - missingCount);
    for (let i = startIdx; i < lessonTitles.length; i++) {
      lessonsNeedingTests.push(lessonTitles[i]);
    }
  }
  
  // Take only the missingCount needed
  const lessonsToGenerate = lessonsNeedingTests.slice(0, missingCount);
  
  if (lessonsToGenerate.length === 0) return null;
  
  // Build descriptions text for AI
  let descriptionsText = '';
  for (const title of lessonsToGenerate) {
    const desc = allLessonDescriptions[title] || '';
    descriptionsText += `\n--- ${title} ---\n${desc.substring(0, 500)}\n`;
  }
  
  const prompt = `Ты — генератор тестов для школьного приложения. Сгенерируй ${lessonsToGenerate.length} тестов по предмету "${subjectTitle}" для ${grade} класса.

Для КАЖДОГО урока создай тест с 5 вопросами. Вопросы должны быть по теме урока на основе описания.

УРОКИ:
${descriptionsText}

ФОРМАТ ВЫВОДА - ТОЛЬКО JSON массив, без markdown, без комментариев:
[
  {
    "lessonTitle": "Точный заголовок урока",
    "testTitle": "Заголовок теста (с эмодзи)",
    "tasks": [
      {"type": "quiz", "question": "Вопрос?", "options": ["В1", "В2", "В3", "В4", "В5"], "correctAnswer": "В1", "hint": "Подсказка"},
      {"type": "quiz", "question": "Вопрос 2?", "options": ["П", "Н1", "Н2", "Н3", "Н4"], "correctAnswer": "П", "hint": "Подсказка"},
      {"type": "quiz", "question": "Вопрос 3?", "options": ["A", "B", "C", "D", "E"], "correctAnswer": "A", "hint": "Подсказка"},
      {"type": "find", "question": "Выбери правильные:", "options": ["П1", "Н1", "П2", "П3", "Н2", "Н3"], "correctAnswer": ["П1", "П2", "П3"], "hint": "Подсказка"},
      {"type": "quiz", "question": "Вопрос 5?", "options": ["X", "Y", "Z", "W", "V"], "correctAnswer": "Y", "hint": "Подсказка"}
    ]
  }
]

ПРАВИЛА:
1. Каждый тест = 5 вопросов
2. Каждый quiz вопрос = РОВНО 5 вариантов ответа
3. correctAnswer для quiz = строка из options (ТОЧНОЕ совпадение)
4. correctAnswer для find = массив строк из options
5. Все на русском языке
6. find тип: 5-6 options, 3 правильных ответа
7. Вопросы по СОДЕРЖАНИЮ урока (возраст ${grade} класс)
8. Варианты "Не знаю" и "Ни один из вариантов" НЕ использовать
9. Выведи ТОЛЬКО JSON, ничего больше`;

  try {
    const completion = await zai.chat.completions.create({
      messages: [
        { role: 'system', content: 'Ты генерируешь тесты для школьного приложения. Выводишь ТОЛЬКО валидный JSON.' },
        { role: 'user', content: prompt }
      ],
      temperature: 0.7,
    });
    
    const responseText = completion.choices[0]?.message?.content || '';
    // Extract JSON from response
    let jsonStr = responseText;
    const jsonMatch = responseText.match(/\[[\s\S]*\]/);
    if (jsonMatch) jsonStr = jsonMatch[0];
    
    return JSON.parse(jsonStr);
  } catch (e) {
    console.error(`AI error for ${grade}/${dir}:`, e.message);
    return null;
  }
}

function formatTestAsTS(test, subjectTitle, icon, color) {
  const tasksStr = test.tasks.map(t => {
    if (t.type === 'find') {
      return `      { type: 'find', question: ${JSON.stringify(t.question)}, options: ${JSON.stringify(t.options)}, correctAnswer: ${JSON.stringify(t.correctAnswer)}, hint: ${JSON.stringify(t.hint)} }`;
    }
    return `      { type: '${t.type}', question: ${JSON.stringify(t.question)}, options: ${JSON.stringify(t.options)}, correctAnswer: ${JSON.stringify(t.correctAnswer)}, hint: ${JSON.stringify(t.hint)} }`;
  }).join(',\n');
  
  return `  {
    title: ${JSON.stringify(test.testTitle)},
    subject: ${JSON.stringify(subjectTitle)},
    icon: ${JSON.stringify(icon)},
    color: ${JSON.stringify(color)},
    tasks: [
${tasksStr}
    ],
    reward: { stars: 3, message: ${JSON.stringify(`Отлично! Ты справился! 🎉`)} }
  }`;
}

function extractAllLessonDescriptions(content) {
  const descriptions = {};
  // Match createLesson calls
  const regex = /createLesson\(\s*['"]([^'"]+)['"]\s*,\s*`([\s\S]*?)`\s*,\s*\[/g;
  let match;
  while ((match = regex.exec(content)) !== null) {
    descriptions[match[1]] = match[2];
  }
  // Also match object-style lessons
  const regex2 = /title:\s*['"]([^'"]+)['"][\s\S]*?description:\s*`([\s\S]*?)`/g;
  while ((match = regex2.exec(content)) !== null) {
    if (!descriptions[match[1]]) {
      descriptions[match[1]] = match[2];
    }
  }
  return descriptions;
}

async function processSubject(zai, target) {
  const filePath = path.join(DATA_DIR, String(target.grade), target.dir, 'index.ts');
  
  if (!fs.existsSync(filePath)) {
    console.log(`SKIP: ${filePath} not found`);
    return false;
  }
  
  console.log(`Processing: Grade ${target.grade}/${target.dir} (need ${target.missing} tests)`);
  
  const info = extractLessonInfo(filePath);
  const actualTitle = target.title || info.subjectTitle;
  
  if (!actualTitle) {
    console.log(`SKIP: Could not determine subject title for ${target.grade}/${target.dir}`);
    return false;
  }
  
  const allDescriptions = extractAllLessonDescriptions(info.content);
  
  // If no games export exists, we need all tests
  if (!info.hasGamesExport) {
    const tests = await generateTestsForSubject(
      zai, target.grade, target.dir, actualTitle, info.icon, info.color,
      info.lessonTitles, [], target.missing, allDescriptions
    );
    
    if (!tests || tests.length === 0) {
      console.log(`FAIL: Could not generate tests for ${target.grade}/${target.dir}`);
      return false;
    }
    
    // Append games export to file
    const testsCode = tests.map(t => formatTestAsTS(t, actualTitle, info.icon, info.color)).join(',\n');
    const gamesExport = `\n\nexport const games: GameLesson[] = [\n${testsCode}\n]\n`;
    
    // Make sure GameLesson is imported
    let content = info.content;
    if (!content.includes('GameLesson')) {
      content = content.replace(/import\s*\{([^}]+)\}\s*from/, (match, imports) => {
        if (!imports.includes('GameLesson')) {
          return `import { ${imports}, GameLesson } from`;
        }
        return match;
      });
    }
    
    fs.writeFileSync(filePath, content + gamesExport);
    console.log(`OK: Added ${tests.length} tests to ${target.grade}/${target.dir}`);
    return true;
  }
  
  // If games export exists, add more tests
  const tests = await generateTestsForSubject(
    zai, target.grade, target.dir, actualTitle, info.icon, info.color,
    info.lessonTitles, info.existingGames, target.missing, allDescriptions
  );
  
  if (!tests || tests.length === 0) {
    console.log(`FAIL: Could not generate tests for ${target.grade}/${target.dir}`);
    return false;
  }
  
  // Insert new tests before the closing ]
  const testsCode = tests.map(t => formatTestAsTS(t, actualTitle, info.icon, info.color)).join(',\n');
  
  let content = info.content;
  // Find the last ] of the games array
  const gamesStart = content.indexOf('export const games');
  if (gamesStart === -1) {
    console.log(`FAIL: No games export found in ${target.grade}/${target.dir}`);
    return false;
  }
  
  // Find the closing bracket of the games array
  let bracketCount = 0;
  let arrayStart = -1;
  let arrayEnd = -1;
  for (let i = gamesStart; i < content.length; i++) {
    if (content[i] === '[') {
      if (arrayStart === -1) arrayStart = i;
      bracketCount++;
    } else if (content[i] === ']') {
      bracketCount--;
      if (bracketCount === 0) {
        arrayEnd = i;
        break;
      }
    }
  }
  
  if (arrayEnd === -1) {
    console.log(`FAIL: Could not find games array end in ${target.grade}/${target.dir}`);
    return false;
  }
  
  // Check if array is empty
  const arrayContent = content.substring(arrayStart + 1, arrayEnd).trim();
  if (arrayContent === '' || arrayContent === '[]') {
    // Array is empty or broken - replace
    const newGames = `export const games: GameLesson[] = [\n${testsCode}\n]`;
    content = content.substring(0, gamesStart) + newGames + content.substring(arrayEnd + 1);
  } else {
    // Insert before the closing ]
    const insertPos = arrayEnd;
    content = content.substring(0, insertPos) + ',\n' + testsCode + content.substring(insertPos);
  }
  
  fs.writeFileSync(filePath, content);
  console.log(`OK: Added ${tests.length} tests to ${target.grade}/${target.dir}`);
  return true;
}

async function main() {
  console.log('Initializing AI...');
  const zai = await ZAI.create();
  
  let successCount = 0;
  let failCount = 0;
  
  for (const target of TARGETS) {
    try {
      const success = await processSubject(zai, target);
      if (success) successCount++;
      else failCount++;
    } catch (e) {
      console.error(`ERROR processing ${target.grade}/${target.dir}:`, e.message);
      failCount++;
    }
    // Small delay between subjects
    await new Promise(r => setTimeout(r, 1000));
  }
  
  console.log(`\nDone! Success: ${successCount}, Failed: ${failCount}`);
}

main().catch(console.error);
