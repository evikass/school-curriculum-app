import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
import path from 'path';

const args = process.argv.slice(2);
const grade = parseInt(args[0]);
const dir = args[1];
const count = parseInt(args[2]);

if (!grade || !dir || !count) {
  console.log('Usage: node gen-one.mjs <grade> <dir> <count>');
  process.exit(1);
}

const filePath = path.join('./src/data/grades', String(grade), dir, 'index.ts');

function extractInfo(content) {
  let subjectTitle = null, icon = 'BookOpen', color = 'text-blue-400';
  const tm = content.match(/title:\s*['"](.+?)['"]/);
  if (tm) subjectTitle = tm[1];
  const im = content.match(/icon:\s*['"](.+?)['"]/);
  if (im) icon = im[1];
  const cm = content.match(/color:\s*['"](.+?)['"]/);
  if (cm) color = cm[1];
  
  const lessons = [];
  const lr = /(?:title:\s*['"]|createLesson\(\s*['"])(Урок \d+[^'"]*)['"]/g;
  let m;
  while ((m = lr.exec(content)) !== null) lessons.push(m[1].trim());
  
  const descs = {};
  const dr = /createLesson\(\s*['"]([^'"]+)['"]\s*,\s*`([\s\S]*?)`\s*,\s*\[/g;
  while ((m = dr.exec(content)) !== null) descs[m[1]] = m[2].substring(0, 150);
  const dr2 = /title:\s*['"]([^'"]+)['"][\s\S]*?description:\s*`([\s\S]*?)`/g;
  while ((m = dr2.exec(content)) !== null) { if (!descs[m[1]]) descs[m[1]] = m[2].substring(0, 150); }
  
  const games = [];
  const gs = content.indexOf('export const games');
  if (gs !== -1) {
    const gc = content.substring(gs);
    const gr = /title:\s*['"](.+?)['"]/g;
    while ((m = gr.exec(gc)) !== null) games.push(m[1].trim());
  }
  
  return { subjectTitle, icon, color, lessons, descs, games, hasGames: gs !== -1 };
}

function formatTest(t, subj, icon, color) {
  const tasks = t.tasks.map(task => {
    const ca = JSON.stringify(task.correctAnswer);
    return `      { type: '${task.type}', question: ${JSON.stringify(task.question)}, options: ${JSON.stringify(task.options)}, correctAnswer: ${ca}, hint: ${JSON.stringify(task.hint)} }`;
  }).join(',\n');
  return `  {
    title: ${JSON.stringify(t.testTitle)},
    subject: ${JSON.stringify(subj)},
    icon: ${JSON.stringify(icon)},
    color: ${JSON.stringify(color)},
    tasks: [\n${tasks}\n    ],
    reward: { stars: 3, message: ${JSON.stringify('Отлично! Ты справился! 🎉')} }
  }`;
}

async function main() {
  const content = fs.readFileSync(filePath, 'utf-8');
  const info = extractInfo(content);
  
  if (!info.subjectTitle) { console.log('ERROR: No subject title found'); process.exit(1); }
  console.log(`Subject: ${info.subjectTitle}, Lessons: ${info.lessons.length}, Games: ${info.games.length}`);
  
  const covered = new Set();
  for (const g of info.games) {
    for (const l of info.lessons) {
      const lWords = l.toLowerCase().replace(/урок\s*\d+\s*[:\-]?\s*/, '').trim().split(' ').slice(0, 3);
      const gWords = g.toLowerCase().split(' ').slice(0, 3);
      if (lWords.some(w => w.length > 2 && gWords.some(gw => gw.includes(w) || w.includes(gw)))) {
        covered.add(l);
      }
    }
  }
  
  let needTests = info.lessons.filter(l => !covered.has(l));
  if (needTests.length < count) needTests = info.lessons.slice(info.games.length);
  // Only take 1 at a time to avoid truncation
  needTests = needTests.slice(0, 1);
  
  if (needTests.length === 0) { console.log('No lessons need tests'); process.exit(0); }
  console.log(`Generating ${needTests.length} tests...`);
  
  let lessonText = '';
  for (const lt of needTests) {
    // Only use first sentence of description
    let desc = (info.descs[lt] || '').split('.')[0];
    if (desc.length > 100) desc = desc.substring(0, 100);
    lessonText += `\n- ${lt}: ${desc}`;
  }
  
  const zai = await ZAI.create();
  
  // Generate 1 test at a time per call
  const lessonTitles = needTests.map(l => `- ${l}`).join('\n');
  
  const prompt = `Предмет: ${info.subjectTitle}, ${grade} класс.
Уроки needing tests:
${lessonTitles}

Создай 1 тест. Формат СТРОГО JSON. Вопросы КОРОТКИЕ (без кода, без многострочных строк). Варианты ответов КОРОТКИЕ (1-3 слова каждый). Подсказки КОРОТКИЕ (до 5 слов).

[{"testTitle":"Тема 📚","tasks":[{"type":"quiz","question":"Краткий вопрос?","options":["Ответ1","Ответ2","Ответ3","Ответ4","Ответ5"],"correctAnswer":"Ответ1","hint":"Краткая подсказка"},{"type":"quiz","question":"Вопрос2?","options":["A","B","C","D","E"],"correctAnswer":"A","hint":"Подсказка"},{"type":"quiz","question":"Вопрос3?","options":["X","Y","Z","W","V"],"correctAnswer":"Y","hint":"Подсказка"},{"type":"find","question":"Выбери верные:","options":["П1","Н2","П3","Н4","П5","Н6"],"correctAnswer":["П1","П3","П5"],"hint":"Подсказка"},{"type":"quiz","question":"Вопрос5?","options":["F","G","H","I","J"],"correctAnswer":"F","hint":"Подсказка"}]}]

ПРАВИЛА: 1 тест, 5 задач, quiz=5 вариантов, find=6 вариантов (3 верных). Без кода. Без многострочного текста. Строго JSON.`;

  // Rate limit: wait between API calls
  const wait = (ms) => new Promise(r => setTimeout(r, ms));
  await wait(3000);
  console.log('Calling AI...');
  
  let comp;
  for (let retry = 0; retry < 5; retry++) {
    try {
      comp = await zai.chat.completions.create({
        messages: [
          { role: 'system', content: 'Генератор тестов. Выводи ТОЛЬКО валидный JSON массив. Никакого markdown.' },
          { role: 'user', content: prompt }
        ],
        temperature: 0.7,
      });
      break;
    } catch(e) {
      if ((e.message?.includes('429') || e.message?.includes('Too many')) && retry < 4) {
        console.log(`Rate limited, waiting ${(retry+1)*8}s...`);
        await wait((retry+1) * 8000);
        continue;
      }
      throw e;
    }
  }
  
  let resp = comp.choices[0]?.message?.content || '';
  resp = resp.replace(/```json\n?/g, '').replace(/```\n?/g, '').trim();
  const jm = resp.match(/\[[\s\S]*\]/);
  if (jm) resp = jm[0];
  // Fix common JSON issues
  resp = resp.replace(/,\s*([}\]])/g, '$1');
  resp = resp.replace(/[\u201C\u201D\u00AB\u00BB\u201E\u201F]/g, '"');
  // Fix missing quote before [ in options like "options":["...
  resp = resp.replace(/"(\w+)"(\[)/g, '"$1": $2');
  // Fix "options":value -> "options": [value]
  
  let tests;
  try {
    tests = JSON.parse(resp);
  } catch(e) {
    // More aggressive fixing
    console.log('JSON parse error, trying aggressive fix...');
    // Replace any smart/double-encoded quotes
    let fixed = resp.replace(/\\"/g, '"');
    // Try parsing with each complete object
    try {
      // Find complete test objects
      const objRegex = /\{"testTitle"[^}]*"tasks"\s*:\s*\[[\s\S]*?\]\s*\}/g;
      const matches = [...fixed.matchAll(objRegex)];
      if (matches.length > 0) {
        tests = matches.map(m => {
          try { return JSON.parse(m[0]); } catch(e3) { return null; }
        }).filter(Boolean);
      }
    } catch(e2) {}
    
    if (!tests || tests.length === 0) {
      // Last resort: extract what we can
      try {
        const fixed2 = resp.substring(0, beforeLast) + ']}';
        const opens = (fixed2.match(/\[/g) || []).length;
        const closes = (fixed2.match(/\]/g) || []).length;
        if (closes < opens) fixed2 += ']';
        tests = JSON.parse(fixed2);
      } catch(e3) {
        console.log('RAW (first 1000):', resp.substring(0, 1000));
        console.log('Error:', e.message);
        process.exit(1);
      }
    }
  }
  console.log(`Generated ${tests.length} tests`);
  
  const testsCode = tests.map(t => formatTest(t, info.subjectTitle, info.icon, info.color)).join(',\n');
  
  let newContent = content;
  
  if (!info.hasGames) {
    if (!content.includes('GameLesson')) {
      newContent = content.replace(/import\s*\{([^}]+)\}\s*from/, (match, imp) => {
        return `import { ${imp}, GameLesson } from`;
      });
    }
    newContent = newContent + `\n\nexport const games: GameLesson[] = [\n${testsCode}\n]\n`;
  } else {
    const gsIdx = newContent.indexOf('export const games');
    let bc = 0, as = -1, ae = -1;
    for (let i = gsIdx; i < newContent.length; i++) {
      if (newContent[i] === '[') { if (as === -1) as = i; bc++; }
      else if (newContent[i] === ']') { bc--; if (bc === 0) { ae = i; break; } }
    }
    if (ae === -1) { console.log('ERROR: No games array end'); process.exit(1); }
    const arrContent = newContent.substring(as + 1, ae).trim();
    if (arrContent === '' || arrContent === '[]') {
      newContent = newContent.substring(0, gsIdx) + `export const games: GameLesson[] = [\n${testsCode}\n]` + newContent.substring(ae + 1);
    } else {
      newContent = newContent.substring(0, ae) + ',\n' + testsCode + newContent.substring(ae);
    }
  }
  
  fs.writeFileSync(filePath, newContent);
  console.log('Done! File written.');
}

main().catch(e => { console.error(e); process.exit(1); });
