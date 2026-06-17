import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs/promises';

const DATA_DIR = '/home/z/school-curriculum-app/public/data/grades/2';
const SUBJECT = process.argv[2]; // 'math' or 'english'
const START = parseInt(process.argv[3]) || 0; // lesson index to start from
const COUNT = parseInt(process.argv[4]) || 4; // how many lessons to process

const SUBJECT_NAMES = { math: 'Математика', english: 'Иностранный язык (English)' };

const SYSTEM_PROMPT = "Ты эксперт по начальному образованию России. Отвечай ТОЛЬКО валидным JSON без markdown обёрток. Описание урока должно быть РАЗВЁРНУТЫМ — минимум 800 символов.";

function buildPrompt(subject, title) {
  return `Создай ПОДРОБНЫЙ контент урока для 2 класса (8 лет). Предмет: ${subject}. Урок: ${title}. Описание должно быть НЕ МЕНЕЕ 800 символов, с заголовками ## и **жирным текстом**. ВЕРНИ ТОЛЬКО JSON: {"description":"...минимум 800 символов...","keyPoints":["...5 пунктов..."],"examples":["...5 примеров..."],"facts":["...3 факта..."],"tests":{"quiz":[{"question":"...","options":["...","...","...","..."],"correct":0},...5 вопросов],"find":[{"text":"...","answer":"..."},...5 заданий],"match":[{"term":"...","definition":"..."},...5 пар]}}`;
}

function delay(ms) { return new Promise(r => setTimeout(r, ms)); }

function extractJSON(text) {
  let cleaned = text.trim();
  if (cleaned.startsWith('```')) {
    cleaned = cleaned.replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/i, '');
  }
  return cleaned;
}

async function generateLessonContent(zai, subject, title, retries = 2) {
  for (let attempt = 0; attempt <= retries; attempt++) {
    try {
      if (attempt > 0) console.log(`  Retry attempt ${attempt} for: ${title}`);
      const response = await zai.chat.completions.create({
        messages: [
          { role: 'system', content: SYSTEM_PROMPT },
          { role: 'user', content: buildPrompt(subject, title) }
        ],
        temperature: 0.7,
        max_tokens: 3000
      });
      const rawContent = response.choices?.[0]?.message?.content || '';
      const jsonStr = extractJSON(rawContent);
      const parsed = JSON.parse(jsonStr);

      if (!parsed.description || parsed.description.length < 800) {
        console.log(`  ⚠ Description too short (${parsed.description?.length || 0} chars), retrying...`);
        continue;
      }
      if (!parsed.keyPoints || parsed.keyPoints.length < 5) { console.log('  ⚠ keyPoints insufficient'); continue; }
      if (!parsed.examples || parsed.examples.length < 5) { console.log('  ⚠ examples insufficient'); continue; }
      if (!parsed.facts || parsed.facts.length < 3) { console.log('  ⚠ facts insufficient'); continue; }
      if (!parsed.tests?.quiz || parsed.tests.quiz.length < 5) { console.log('  ⚠ quiz insufficient'); continue; }
      if (!parsed.tests?.find || parsed.tests.find.length < 5) { console.log('  ⚠ find insufficient'); continue; }
      if (!parsed.tests?.match || parsed.tests.match.length < 5) { console.log('  ⚠ match insufficient'); continue; }

      return parsed;
    } catch (e) {
      console.log(`  ❌ Error on attempt ${attempt}: ${e.message.substring(0, 100)}`);
      if (attempt === retries) return null;
    }
  }
  return null;
}

async function main() {
  const subjectName = SUBJECT_NAMES[SUBJECT];
  const filePath = `${DATA_DIR}/${SUBJECT}.json`;
  const raw = await fs.readFile(filePath, 'utf-8');
  const data = JSON.parse(raw);

  const allLessons = [];
  for (const topic of data.lessons.detailedTopics) {
    for (const lesson of topic.lessons) {
      allLessons.push(lesson);
    }
  }

  const lessonsToProcess = allLessons.slice(START, START + COUNT);
  console.log(`Processing ${subjectName}: lessons ${START+1}-${START+lessonsToProcess.length} of ${allLessons.length}`);

  const zai = await ZAI.create();
  let success = 0, failed = 0;

  for (let i = 0; i < lessonsToProcess.length; i++) {
    const lesson = lessonsToProcess[i];
    console.log(`[${START + i + 1}/${allLessons.length}] ${lesson.title}`);
    const content = await generateLessonContent(zai, subjectName, lesson.title);
    if (content) {
      lesson.description = content.description;
      lesson.keyPoints = content.keyPoints;
      lesson.examples = content.examples;
      lesson.facts = content.facts;
      lesson.tests = content.tests;
      success++;
      console.log(`  ✅ Success (desc: ${content.description.length} chars)`);
    } else {
      failed++;
      console.log(`  ❌ FAILED`);
    }
    if (i < lessonsToProcess.length - 1) await delay(500);
  }

  await fs.writeFile(filePath, JSON.stringify(data, null, 2), 'utf-8');
  console.log(`\n💾 Saved: ${success} success, ${failed} failed`);
}

main().catch(e => { console.error('Fatal:', e.message); process.exit(1); });
