import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
import path from 'path';

const DATA_DIR = '/home/z/school-curriculum-app/public/data/grades/2';
const SUBJECT_FILE = process.argv[2];

const SUBJECT_NAMES = {
  tech: 'Технология',
  projects: 'Проектная деятельность',
  world: 'Окружающий мир',
};

const SYSTEM_PROMPT = "Ты эксперт по начальному образованию России. Отвечай ТОЛЬКО валидным JSON без markdown обёрток. Описание урока должно быть РАЗВЁРНУТЫМ — минимум 800 символов.";

function buildUserPrompt(subjectName, lessonTitle) {
  return `Создай ПОДРОБНЫЙ контент урока для 2 класса (8 лет). Предмет: ${subjectName}. Урок: ${lessonTitle}. Описание должно быть НЕ МЕНЕЕ 800 символов, с заголовками ## и **жирным текстом**. ВЕРНИ ТОЛЬКО JSON: {"description":"...минимум 800 символов...","keyPoints":["...5 пунктов..."],"examples":["...5 примеров..."],"facts":["...3 факта..."],"tests":{"quiz":[{"question":"...","options":["...","...","...","..."],"correct":0},...5 вопросов],"find":[{"text":"...","answer":"..."},...5 заданий],"match":[{"term":"...","definition":"..."},...5 пар]}}`;
}

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function extractJSON(text) {
  let cleaned = text.replace(/^```(?:json)?\s*/i, '').replace(/\s*```\s*$/i, '');
  try {
    return JSON.parse(cleaned);
  } catch (e) {
    const objMatch = cleaned.match(/\{[\s\S]*\}/);
    if (objMatch) {
      try { return JSON.parse(objMatch[0]); } catch (e2) {}
    }
    throw new Error(`Failed to parse JSON: ${text.substring(0, 200)}`);
  }
}

function validateContent(c) {
  if (!c.description || c.description.length < 800) return false;
  if (!c.keyPoints || c.keyPoints.length < 5) return false;
  if (!c.examples || c.examples.length < 5) return false;
  if (!c.facts || c.facts.length < 3) return false;
  if (!c.tests?.quiz || c.tests.quiz.length < 5) return false;
  if (!c.tests?.find || c.tests.find.length < 5) return false;
  if (!c.tests?.match || c.tests.match.length < 5) return false;
  return true;
}

async function generateContent(zai, subjectName, title, retries = 2) {
  for (let i = 0; i <= retries; i++) {
    try {
      const extra = i > 0 ? '\n\nВАЖНО: Описание ОБЯЗАТЕЛЬНО минимум 800 символов! Пиши развёрнуто!' : '';
      const resp = await zai.chat.completions.create({
        model: 'default',
        messages: [
          { role: 'system', content: SYSTEM_PROMPT },
          { role: 'user', content: buildUserPrompt(subjectName, title) + extra },
        ],
        temperature: 0.7,
        max_tokens: 3000,
      });

      const content = extractJSON(resp.choices[0].message.content);
      if (!validateContent(content) && i < retries) {
        console.log(`    Retry ${i+1}: desc=${content.description?.length}`);
        await delay(500);
        continue;
      }
      return content;
    } catch (err) {
      console.log(`    Error attempt ${i+1}: ${err.message.substring(0, 80)}`);
      if (i < retries) { await delay(500); continue; }
      return null;
    }
  }
  return null;
}

async function main() {
  const subjectName = SUBJECT_NAMES[SUBJECT_FILE];
  if (!subjectName) { console.error('Usage: node script.mjs <tech|projects|world>'); process.exit(1); }

  const filePath = path.join(DATA_DIR, SUBJECT_FILE + '.json');
  const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  const zai = await ZAI.create();

  let ok = 0, fail = 0, total = 0;

  for (const topic of data.lessons.detailedTopics) {
    for (const lesson of topic.lessons) {
      total++;
      console.log(`[${total}] ${lesson.title}`);
      const c = await generateContent(zai, subjectName, lesson.title);
      if (c) {
        lesson.description = c.description;
        lesson.keyPoints = c.keyPoints;
        lesson.examples = c.examples;
        lesson.facts = c.facts;
        lesson.tests = c.tests;
        ok++;
        console.log(`  ✅ desc=${c.description.length}`);
      } else {
        fail++;
        console.log(`  ❌ FAILED`);
      }
      await delay(500);
    }
  }

  fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf-8');
  console.log(`\n💾 ${SUBJECT_FILE}.json saved: ${ok}/${total} OK, ${fail} FAIL`);
}

main().catch(e => { console.error(e); process.exit(1); });
