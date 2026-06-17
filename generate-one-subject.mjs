import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
import path from 'path';

const DATA_DIR = '/home/z/school-curriculum-app/public/data/grades/2';
const SUBJECT_FILE = process.argv[2]; // e.g. 'tech', 'projects', 'world'
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
  // Strip markdown code blocks
  let cleaned = text.replace(/^```(?:json)?\s*/i, '').replace(/\s*```\s*$/i, '');
  try {
    return JSON.parse(cleaned);
  } catch (e) {
    // Try to find JSON object in text
    const objMatch = cleaned.match(/\{[\s\S]*\}/);
    if (objMatch) {
      try {
        return JSON.parse(objMatch[0]);
      } catch (e3) {}
    }
    throw new Error(`Failed to parse JSON from LLM response: ${text.substring(0, 300)}`);
  }
}

function validateContent(content) {
  const issues = [];
  if (!content.description || content.description.length < 800) {
    issues.push(`description length=${content.description?.length || 0} (need 800)`);
  }
  if (!content.keyPoints || content.keyPoints.length < 5) issues.push('keyPoints < 5');
  if (!content.examples || content.examples.length < 5) issues.push('examples < 5');
  if (!content.facts || content.facts.length < 3) issues.push('facts < 3');
  if (!content.tests?.quiz || content.tests.quiz.length < 5) issues.push('quiz < 5');
  if (!content.tests?.find || content.tests.find.length < 5) issues.push('find < 5');
  if (!content.tests?.match || content.tests.match.length < 5) issues.push('match < 5');
  return issues;
}

async function generateLessonContent(zai, subjectName, lessonTitle, maxRetries = 2) {
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      const emphasis = attempt > 0
        ? '\n\nВАЖНО: Описание ОБЯЗАТЕЛЬНО не менее 800 символов! Напиши максимально подробно и развёрнуто! Предыдущая попытка была слишком короткой!'
        : '';
      const userPrompt = buildUserPrompt(subjectName, lessonTitle) + emphasis;

      const response = await zai.chat.completions.create({
        model: 'default',
        messages: [
          { role: 'system', content: SYSTEM_PROMPT },
          { role: 'user', content: userPrompt },
        ],
        temperature: 0.7,
        max_tokens: 3000,
      });

      const text = response.choices[0].message.content;
      const content = extractJSON(text);

      const issues = validateContent(content);
      if (issues.length > 0) {
        console.log(`  ⚠ Validation issues (attempt ${attempt + 1}): ${issues.join('; ')}`);
        if (attempt < maxRetries) {
          await delay(500);
          continue;
        }
      }

      return content;
    } catch (err) {
      console.log(`  ⚠ Error on attempt ${attempt + 1}: ${err.message}`);
      if (attempt < maxRetries) {
        await delay(500);
        continue;
      }
      return null;
    }
  }
  return null;
}

async function main() {
  const subjectName = SUBJECT_NAMES[SUBJECT_FILE];
  if (!subjectName) {
    console.error(`Unknown subject: ${SUBJECT_FILE}. Use tech, projects, or world.`);
    process.exit(1);
  }

  const filePath = path.join(DATA_DIR, SUBJECT_FILE + '.json');
  console.log(`🚀 Processing: ${subjectName} (${SUBJECT_FILE}.json)\n`);

  const zai = await ZAI.create();
  console.log('✅ ZAI SDK initialized\n');

  const rawData = fs.readFileSync(filePath, 'utf-8');
  const data = JSON.parse(rawData);

  const topics = data.lessons.detailedTopics;
  let successCount = 0;
  let failCount = 0;
  let totalLessons = 0;

  for (const topic of topics) {
    console.log(`\n📂 Topic: ${topic.topic}`);
    
    for (const lesson of topic.lessons) {
      totalLessons++;
      console.log(`\n📝 [${totalLessons}] ${lesson.title}`);

      const content = await generateLessonContent(zai, subjectName, lesson.title);

      if (content) {
        lesson.description = content.description;
        lesson.keyPoints = content.keyPoints;
        lesson.examples = content.examples;
        lesson.facts = content.facts;
        lesson.tests = content.tests;
        successCount++;
        console.log(`  ✅ Done! desc=${content.description.length} chars`);
      } else {
        failCount++;
        console.log(`  ❌ Failed`);
      }

      await delay(500);
    }
  }

  // Save file
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf-8');
  console.log(`\n💾 Saved ${SUBJECT_FILE}.json: ${successCount}/${totalLessons} OK, ${failCount} FAIL`);
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
