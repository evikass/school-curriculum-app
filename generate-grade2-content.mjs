import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
import path from 'path';

const DELAY = 500;
const MAX_RETRIES = 3;
const TEMP = 0.7;
const MAX_TOKENS = 3000;

const SYSTEM_PROMPT = "Ты эксперт по начальному образованию России. Отвечай ТОЛЬКО валидным JSON без markdown обёрток. Описание урока должно быть РАЗВЁРНУТЫМ — минимум 800 символов.";

function makeUserPrompt(subject, title) {
  return `Создай ПОДРОБНЫЙ контент урока для 2 класса (8 лет). Предмет: ${subject}. Урок: ${title}. Описание должно быть НЕ МЕНЕЕ 800 символов, с заголовками ## и **жирным текстом**. ВЕРНИ ТОЛЬКО JSON: {"description":"...минимум 800 символов...","keyPoints":["...5 пунктов..."],"examples":["...5 примеров..."],"facts":["...3 факта..."],"tests":{"quiz":[{"question":"...","options":["...","...","...","..."],"correct":0},...5 вопросов],"find":[{"text":"...","answer":"..."},...5 заданий],"match":[{"term":"...","definition":"..."},...5 пар]}}`;
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function extractJSON(text) {
  // Try direct parse
  try {
    return JSON.parse(text);
  } catch (e) {}

  // Try to strip markdown code blocks
  const jsonMatch = text.match(/```(?:json)?\s*([\s\S]*?)```/);
  if (jsonMatch) {
    try {
      return JSON.parse(jsonMatch[1].trim());
    } catch (e2) {}
  }

  // Try to find a JSON object
  const braceMatch = text.match(/\{[\s\S]*\}/);
  if (braceMatch) {
    try {
      return JSON.parse(braceMatch[0]);
    } catch (e3) {}
  }

  throw new Error(`Could not parse JSON from LLM response (first 200 chars): ${text.substring(0, 200)}`);
}

function validateContent(content) {
  const errors = [];
  if (!content.description || content.description.length < 800) {
    errors.push(`Description too short: ${content.description?.length || 0} chars (need ≥800)`);
  }
  if (!content.keyPoints || content.keyPoints.length < 5) {
    errors.push(`keyPoints: got ${content.keyPoints?.length || 0}, need 5`);
  }
  if (!content.examples || content.examples.length < 5) {
    errors.push(`examples: got ${content.examples?.length || 0}, need 5`);
  }
  if (!content.facts || content.facts.length < 3) {
    errors.push(`facts: got ${content.facts?.length || 0}, need 3`);
  }
  if (!content.tests?.quiz || content.tests.quiz.length < 5) {
    errors.push(`tests.quiz: got ${content.tests?.quiz?.length || 0}, need 5`);
  }
  if (!content.tests?.find || content.tests.find.length < 5) {
    errors.push(`tests.find: got ${content.tests?.find?.length || 0}, need 5`);
  }
  if (!content.tests?.match || content.tests.match.length < 5) {
    errors.push(`tests.match: got ${content.tests?.match?.length || 0}, need 5`);
  }
  return errors;
}

async function generateLessonContent(zai, subject, title, retryCount = 0) {
  const emphasis = retryCount > 0
    ? ` ВАЖНО: описание ОБЯЗАТЕЛЬНО минимум 800 символов! Пиши подробно, развёрнуто, с примерами и объяснениями! Предыдущая попытка была слишком короткой!`
    : '';

  const userPrompt = makeUserPrompt(subject, title) + emphasis;

  console.log(`  Calling LLM for: ${title}${retryCount > 0 ? ` (retry ${retryCount})` : ''}`);

  const response = await zai.chat.completions.create({
    messages: [
      { role: 'system', content: SYSTEM_PROMPT },
      { role: 'user', content: userPrompt }
    ],
    temperature: TEMP,
    max_tokens: MAX_TOKENS
  });

  const rawText = response.choices?.[0]?.message?.content || '';
  if (!rawText) {
    throw new Error('Empty response from LLM');
  }

  const content = extractJSON(rawText);
  const errors = validateContent(content);

  if (errors.length > 0 && retryCount < MAX_RETRIES) {
    console.log(`  ⚠ Validation: ${errors.join('; ')}. Retrying...`);
    await sleep(DELAY);
    return generateLessonContent(zai, subject, title, retryCount + 1);
  }

  if (errors.length > 0) {
    console.log(`  ⚠ Validation issues after ${MAX_RETRIES} retries: ${errors.join('; ')}`);
  }

  return content;
}

async function processSubject(subjectName, filePath) {
  console.log(`\n========== Processing: ${subjectName} ==========\n`);

  const rawData = fs.readFileSync(filePath, 'utf-8');
  const data = JSON.parse(rawData);

  let successCount = 0;
  let failCount = 0;
  const failures = [];

  const zai = await ZAI.create();
  console.log('ZAI client initialized.\n');

  for (const topicGroup of data.lessons.detailedTopics) {
    console.log(`Topic: ${topicGroup.topic}`);

    for (const lesson of topicGroup.lessons) {
      try {
        const content = await generateLessonContent(zai, subjectName, lesson.title);

        // Update lesson in place
        lesson.description = content.description || lesson.description;
        lesson.keyPoints = content.keyPoints || [];
        lesson.examples = content.examples || [];
        lesson.facts = content.facts || [];
        lesson.tests = content.tests || { quiz: [], find: [], match: [] };

        successCount++;
        console.log(`  ✅ ${lesson.title} — desc: ${lesson.description.length} chars, keyPoints: ${lesson.keyPoints.length}, examples: ${lesson.examples.length}, facts: ${lesson.facts.length}, quiz: ${lesson.tests.quiz?.length || 0}, find: ${lesson.tests.find?.length || 0}, match: ${lesson.tests.match?.length || 0}\n`);
      } catch (err) {
        failCount++;
        failures.push({ lesson: lesson.title, error: err.message });
        console.log(`  ❌ ${lesson.title} — Error: ${err.message}\n`);
      }

      await sleep(DELAY);
    }
  }

  // Save file after all lessons processed
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf-8');
  console.log(`\n💾 ${subjectName} saved to ${filePath}`);
  console.log(`   ${successCount} succeeded, ${failCount} failed.`);

  if (failures.length > 0) {
    console.log(`   Failures:`);
    failures.forEach(f => console.log(`     - ${f.lesson}: ${f.error}`));
  }

  return { subjectName, successCount, failCount, failures };
}

async function main() {
  const grade2Dir = '/home/z/school-curriculum-app/public/data/grades/2';

  const subjects = [
    { name: 'Русский язык', file: path.join(grade2Dir, 'russian.json') },
    { name: 'Литературное чтение', file: path.join(grade2Dir, 'literature.json') },
  ];

  const results = [];

  for (const subject of subjects) {
    const result = await processSubject(subject.name, subject.file);
    results.push(result);
  }

  console.log('\n\n==============================');
  console.log('       FINAL REPORT');
  console.log('==============================\n');

  let totalSuccess = 0;
  let totalFail = 0;

  for (const r of results) {
    totalSuccess += r.successCount;
    totalFail += r.failCount;
    console.log(`${r.subjectName}: ${r.successCount} ✅ | ${r.failCount} ❌`);
    if (r.failures.length > 0) {
      r.failures.forEach(f => console.log(`  ❌ ${f.lesson}: ${f.error}`));
    }
  }

  console.log(`\nTOTAL: ${totalSuccess} succeeded, ${totalFail} failed out of ${totalSuccess + totalFail} lessons.`);
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
