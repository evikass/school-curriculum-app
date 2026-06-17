import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const DELAY = 500;
const MAX_RETRIES = 2;
const TEMP = 0.7;
const MAX_TOKENS = 4000;

const SYSTEM_PROMPT = "Ты эксперт по начальному образованию России. Отвечай ТОЛЬКО валидным JSON без markdown обёрток. Описание урока должно быть РАЗВЁРНУТЫМ — минимум 800 символов.";

function makeUserPrompt(subject, title, retry) {
  const emphasis = retry > 0 ? ` ВАЖНО: описание ОБЯЗАТЕЛЬНО минимум 800 символов! Пиши максимально подробно!` : '';
  return `Создай ПОДРОБНЫЙ контент урока для 2 класса (8 лет). Предмет: ${subject}. Урок: ${title}. Описание должно быть НЕ МЕНЕЕ 800 символов, с заголовками ## и **жирным текстом**. ВЕРНИ ТОЛЬКО JSON: {"description":"...минимум 800 символов...","keyPoints":["...5 пунктов..."],"examples":["...5 примеров..."],"facts":["...3 факта..."],"tests":{"quiz":[{"question":"...","options":["...","...","...","..."],"correct":0},...5 вопросов],"find":[{"text":"...","answer":"..."},...5 заданий],"match":[{"term":"...","definition":"..."},...5 пар]}}` + emphasis;
}

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

function extractJSON(text) {
  try { return JSON.parse(text); } catch(e) {}
  const m = text.match(/```(?:json)?\s*([\s\S]*?)```/);
  if (m) { try { return JSON.parse(m[1].trim()); } catch(e2) {} }
  const b = text.match(/\{[\s\S]*\}/);
  if (b) { try { return JSON.parse(b[0]); } catch(e3) {} }
  throw new Error('Cannot parse JSON: ' + text.substring(0, 150));
}

async function generateContent(zai, subject, title) {
  for (let retry = 0; retry <= MAX_RETRIES; retry++) {
    try {
      console.log(`  LLM: ${title}${retry > 0 ? ` (retry ${retry})` : ''}`);
      const resp = await zai.chat.completions.create({
        messages: [
          { role: 'system', content: SYSTEM_PROMPT },
          { role: 'user', content: makeUserPrompt(subject, title, retry) }
        ],
        temperature: TEMP,
        max_tokens: MAX_TOKENS
      });
      const raw = resp.choices?.[0]?.message?.content || '';
      if (!raw) throw new Error('Empty LLM response');
      const content = extractJSON(raw);
      
      // Validate description length
      if (!content.description || content.description.length < 800) {
        if (retry < MAX_RETRIES) {
          console.log(`  ⚠ Desc too short (${content.description?.length || 0}), retrying...`);
          await sleep(DELAY);
          continue;
        }
        console.log(`  ⚠ Desc still short after retries: ${content.description?.length || 0}`);
      }
      return content;
    } catch(e) {
      if (retry >= MAX_RETRIES) throw e;
      console.log(`  ⚠ Error: ${e.message}, retrying...`);
      await sleep(DELAY);
    }
  }
}

async function processSubject(subjectName, filePath) {
  console.log(`\n=== ${subjectName} ===\n`);
  const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  const zai = await ZAI.create();
  let ok = 0, fail = 0;
  const fails = [];

  for (const topic of data.lessons.detailedTopics) {
    for (const lesson of topic.lessons) {
      try {
        const c = await generateContent(zai, subjectName, lesson.title);
        lesson.description = c.description || lesson.description;
        lesson.keyPoints = c.keyPoints || [];
        lesson.examples = c.examples || [];
        lesson.facts = c.facts || [];
        lesson.tests = c.tests || { quiz: [], find: [], match: [] };
        ok++;
        console.log(`  ✅ ${lesson.title} (${lesson.description.length}ch)\n`);
      } catch(e) {
        fail++;
        fails.push({ lesson: lesson.title, error: e.message });
        console.log(`  ❌ ${lesson.title}: ${e.message}\n`);
      }
      await sleep(DELAY);
    }
  }

  fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf-8');
  console.log(`💾 Saved ${subjectName}: ${ok} ok, ${fail} fail`);
  return { subjectName, ok, fail, fails };
}

// Process a single subject passed as argument
const subject = process.argv[2];
const dir = '/home/z/school-curriculum-app/public/data/grades/2';

if (subject === 'russian') {
  processSubject('Русский язык', `${dir}/russian.json`)
    .then(r => console.log(`\nDONE: ${r.ok}/${r.ok + r.fail}`))
    .catch(e => { console.error('Fatal:', e); process.exit(1); });
} else if (subject === 'literature') {
  processSubject('Литературное чтение', `${dir}/literature.json`)
    .then(r => console.log(`\nDONE: ${r.ok}/${r.ok + r.fail}`))
    .catch(e => { console.error('Fatal:', e); process.exit(1); });
} else {
  console.error('Usage: node generate.mjs russian|literature');
  process.exit(1);
}
