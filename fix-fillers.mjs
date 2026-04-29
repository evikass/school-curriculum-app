import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
import path from 'path';

const GRADES_DIR = '/home/z/my-project/school-curriculum-app/src/data/grades';

const FILLER_WORDS = [
  'Никто не знает', 'Не знаю', 'Не указано', 'Нет ответа',
  'Неверно', 'Не подходит', 'Другой ответ', 'другой ответ',
  'Другой', 'другой', 'Это секрет', 'Все знают',
  'Затрудняюсь', 'Без понятия', 'Не определить', 'Невозможно',
  'Неясно', 'Не понятно', 'Не могу сказать', 'Нет верного',
  'нет верного', 'Все выше', 'все выше', 'Ничего', 'ничего',
  'Не имеет значения', 'Не важно', 'Не определено',
];

function isFiller(text) {
  text = text.trim();
  if (text === '-') return true;
  for (const fw of FILLER_WORDS) {
    if (fw.toLowerCase() === text.toLowerCase()) return true;
    if (text.toLowerCase().startsWith(fw.toLowerCase())) {
      const rest = text.slice(fw.length).trim();
      if (rest === '' || /^\d+$/.test(rest)) return true;
    }
  }
  return false;
}

function extractString(content, key) {
  // Extract a string value after key: "value"
  const searchKey = key + ':';
  const idx = content.indexOf(searchKey);
  if (idx === -1) return null;
  const afterKey = content.slice(idx + searchKey.length).trimStart();
  if (!afterKey.startsWith('"')) return null;
  // Find the closing quote (handle escaped quotes)
  let end = 1;
  while (end < afterKey.length) {
    if (afterKey[end] === '\\' && end + 1 < afterKey.length) {
      end += 2;
      continue;
    }
    if (afterKey[end] === '"') break;
    end++;
  }
  return afterKey.slice(1, end).replace(/\\"/g, '"');
}

function extractOptions(content, startPos) {
  // Find options: [ and parse the array
  const idx = content.indexOf('options:', startPos);
  if (idx === -1) return null;
  const afterOptions = content.slice(idx + 8).trimStart(); // 'options:' is 8 chars
  if (!afterOptions.startsWith('[')) return null;
  
  // Find matching ]
  let depth = 0;
  let i = 0;
  for (; i < afterOptions.length; i++) {
    if (afterOptions[i] === '[') depth++;
    if (afterOptions[i] === ']') { depth--; if (depth === 0) break; }
  }
  const arrStr = afterOptions.slice(0, i + 1);
  
  // Parse quoted strings from the array
  const options = [];
  const optPattern = /"((?:[^"\\]|\\.)*)"/g;
  let m;
  while ((m = optPattern.exec(arrStr)) !== null) {
    options.push(m[1].replace(/\\"/g, '"'));
  }
  return { options, endPos: idx + 8 + i + 1, arrStr };
}

function parseQuizzes(content) {
  const quizzes = [];
  const pattern = /type:\s*'quiz'/g;
  let match;
  
  while ((match = pattern.exec(content)) !== null) {
    const quizStart = match.index;
    
    // Find the opening { before type:
    let braceStart = content.lastIndexOf('{', quizStart);
    if (braceStart === -1 || content.slice(braceStart, quizStart).includes('}')) continue;
    
    // Extract question
    const question = extractString(content.slice(braceStart), 'question');
    if (!question) continue;
    
    // Extract options
    const optResult = extractOptions(content, braceStart);
    if (!optResult) continue;
    
    // Extract correctAnswer
    const correctAnswer = extractString(content.slice(braceStart), 'correctAnswer');
    if (!correctAnswer) continue;
    
    // Find the closing }
    let depth = 0;
    let braceEnd = braceStart;
    for (let i = braceStart; i < content.length; i++) {
      if (content[i] === '{') depth++;
      if (content[i] === '}') { depth--; if (depth === 0) { braceEnd = i + 1; break; } }
    }
    
    const fullMatch = content.slice(braceStart, braceEnd);
    const fillerIdx = [];
    for (let i = 0; i < optResult.options.length; i++) {
      if (isFiller(optResult.options[i])) fillerIdx.push(i);
    }
    
    if (fillerIdx.length > 0) {
      quizzes.push({
        start: braceStart,
        end: braceEnd,
        fullMatch,
        question,
        options: optResult.options,
        correct: correctAnswer,
        fillerIdx,
      });
    }
  }
  return quizzes;
}

function escapeRegex(str) {
  return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function generateReplacements(zai, question, options, correct, fillerIdx, grade, subject, retries = 3) {
  const fillerLabels = fillerIdx.map(i => `option[${i}]="${options[i]}"`).join(', ');
  
  const prompt = `Замени бессмысленные варианты ответа в учебном тесте на осмысленные.
Класс: ${grade}, Предмет: ${subject}
Вопрос: "${question}"
Все варианты: ${JSON.stringify(options)}
Правильный ответ: "${correct}"
Заменить: ${fillerLabels}

Сгенерируй ${fillerIdx.length} правдоподобных, но НЕВЕРНЫХ дистрактора.
Ответь ТОЛЬКО в формате:
option[N]=Текст варианта`;

  for (let attempt = 0; attempt < retries; attempt++) {
    try {
      const completion = await zai.chat.completions.create({
        messages: [
          { role: 'system', content: 'Ты помощник для учебных тестов. Отвечай ТОЛЬКО запрошенными данными в точном формате.' },
          { role: 'user', content: prompt }
        ],
        temperature: 0.7,
        max_tokens: 500,
      });
      
      const result = completion.choices[0]?.message?.content?.trim() || '';
      const replacements = {};
      
      for (const line of result.split('\n')) {
        const m = line.trim().match(/^option\[(\d+)\]\s*=\s*(.+)/);
        if (m) {
          const oi = parseInt(m[1]);
          let text = m[2].trim().replace(/^["']|["']$/g, '').trim();
          if (fillerIdx.includes(oi)) {
            const isDup = options.some((opt, i) => i !== oi && text.toLowerCase().trim() === opt.toLowerCase().trim());
            if (!isDup && text.toLowerCase().trim() !== correct.toLowerCase().trim()) {
              replacements[oi] = text;
            }
          }
        }
      }
      return replacements;
    } catch (err) {
      if (err.message?.includes('429')) {
        const wait = 10 * Math.pow(2, attempt);
        console.log(`    Rate limited, waiting ${wait}s...`);
        await sleep(wait * 1000);
      } else {
        console.error(`    API Error: ${err.message?.slice(0, 100)}`);
        await sleep(2000);
      }
    }
  }
  return {};
}

async function fixFile(zai, filepath, grade, subject) {
  let content = fs.readFileSync(filepath, 'utf-8');
  let quizzes = parseQuizzes(content);
  
  if (quizzes.length === 0) return 0;
  
  console.log(`    Found ${quizzes.length} quizzes with fillers`);
  const totalFillers = quizzes.reduce((s, q) => s + q.fillerIdx.length, 0);
  console.log(`    Total filler options: ${totalFillers}`);
  
  let replacementsMade = 0;
  
  for (const q of quizzes) {
    const replacements = await generateReplacements(zai, q.question, q.options, q.correct, q.fillerIdx, grade, subject);
    
    if (Object.keys(replacements).length > 0) {
      const newOptions = [...q.options];
      for (const [idx, text] of Object.entries(replacements)) {
        newOptions[parseInt(idx)] = text;
        replacementsMade++;
        console.log(`    Replaced: "${q.options[parseInt(idx)]}" -> "${text}"`);
      }
      
      // Build new options string
      const newOptsStr = newOptions.map(o => `"${o}"`).join(', ');
      
      // Find the options array in the fullMatch and replace it
      const optsSectionMatch = q.fullMatch.match(/options:\s*\[(?:[^\[\]]|\[(?:[^\[\]])*\])*\]/s);
      if (optsSectionMatch) {
        const newOptsSection = `options: [${newOptsStr}]`;
        const newFullMatch = q.fullMatch.replace(optsSectionMatch[0], newOptsSection);
        content = content.slice(0, q.start) + newFullMatch + content.slice(q.end);
      }
    } else {
      console.log(`    No replacements for: ${q.question.slice(0, 50)}...`);
    }
    
    await sleep(3000); // Rate limiting - 3s between requests
  }
  
  if (replacementsMade > 0) {
    fs.writeFileSync(filepath, content, 'utf-8');
  }
  
  return replacementsMade;
}

async function main() {
  const grades = process.argv.length > 2 
    ? process.argv.slice(2).map(Number) 
    : [6, 7];
  
  const zai = await ZAI.create();
  let total = 0;
  
  for (const grade of grades) {
    const gradeDir = path.join(GRADES_DIR, String(grade));
    if (!fs.existsSync(gradeDir)) continue;
    
    console.log(`\n${'='.repeat(60)}`);
    console.log(`Grade ${grade}`);
    console.log('='.repeat(60));
    
    const subjects = fs.readdirSync(gradeDir).sort();
    for (const subject of subjects) {
      const fp = path.join(gradeDir, subject, 'index.ts');
      if (!fs.existsSync(fp)) continue;
      
      console.log(`\n  ${subject}:`);
      const count = await fixFile(zai, fp, grade, subject);
      total += count;
      console.log(`  -> ${count} replacements`);
    }
  }
  
  console.log(`\nTOTAL: ${total}`);
}

main().catch(console.error);
