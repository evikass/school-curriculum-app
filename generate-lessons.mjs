import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs/promises';
import path from 'path';

const DATA_DIR = '/home/z/school-curriculum-app/public/data/grades/2';

const SYSTEM_PROMPT = "Ты эксперт по начальному образованию России. Отвечай ТОЛЬКО валидным JSON без markdown обёрток. Описание урока должно быть РАЗВЁРНУТЫМ — минимум 800 символов.";

function buildPrompt(subject, title) {
  return `Создай ПОДРОБНЫЙ контент урока для 2 класса (8 лет). Предмет: ${subject}. Урок: ${title}. Описание должно быть НЕ МЕНЕЕ 800 символов, с заголовками ## и **жирным текстом**. ВЕРНИ ТОЛЬКО JSON: {"description":"...минимум 800 символов...","keyPoints":["...5 пунктов..."],"examples":["...5 примеров..."],"facts":["...3 факта..."],"tests":{"quiz":[{"question":"...","options":["...","...","...","..."],"correct":0},...5 вопросов],"find":[{"text":"...","answer":"..."},...5 заданий],"match":[{"term":"...","definition":"..."},...5 пар]}}`;
}

function delay(ms) {
  return new Promise(r => setTimeout(r, ms));
}

function extractJSON(text) {
  // Try to extract JSON from the response, handling markdown wrappers
  let cleaned = text.trim();
  // Remove ```json ... ``` wrapper if present
  if (cleaned.startsWith('```')) {
    cleaned = cleaned.replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/i, '');
  }
  return cleaned;
}

async function generateLessonContent(zai, subject, title, retries = 2) {
  for (let attempt = 0; attempt <= retries; attempt++) {
    try {
      const prompt = buildPrompt(subject, title);
      if (attempt > 0) {
        // On retry, emphasize length more
        console.log(`  Retry attempt ${attempt} for: ${title}`);
      }

      const response = await zai.chat.completions.create({
        messages: [
          { role: 'system', content: SYSTEM_PROMPT },
          { role: 'user', content: prompt }
        ],
        temperature: 0.7,
        max_tokens: 3000
      });

      const rawContent = response.choices?.[0]?.message?.content || '';
      const jsonStr = extractJSON(rawContent);
      const parsed = JSON.parse(jsonStr);

      // Validate structure
      if (!parsed.description || parsed.description.length < 800) {
        console.log(`  ⚠ Description too short (${parsed.description?.length || 0} chars), retrying...`);
        continue;
      }

      if (!parsed.keyPoints || parsed.keyPoints.length < 5) {
        console.log(`  ⚠ keyPoints has ${parsed.keyPoints?.length || 0} items, retrying...`);
        continue;
      }

      if (!parsed.examples || parsed.examples.length < 5) {
        console.log(`  ⚠ examples has ${parsed.examples?.length || 0} items, retrying...`);
        continue;
      }

      if (!parsed.facts || parsed.facts.length < 3) {
        console.log(`  ⚠ facts has ${parsed.facts?.length || 0} items, retrying...`);
        continue;
      }

      if (!parsed.tests?.quiz || parsed.tests.quiz.length < 5) {
        console.log(`  ⚠ quiz has ${parsed.tests?.quiz?.length || 0} items, retrying...`);
        continue;
      }

      if (!parsed.tests?.find || parsed.tests.find.length < 5) {
        console.log(`  ⚠ find has ${parsed.tests?.find?.length || 0} items, retrying...`);
        continue;
      }

      if (!parsed.tests?.match || parsed.tests.match.length < 5) {
        console.log(`  ⚠ match has ${parsed.tests?.match?.length || 0} items, retrying...`);
        continue;
      }

      return parsed;
    } catch (e) {
      console.log(`  ❌ Error on attempt ${attempt}: ${e.message}`);
      if (attempt === retries) {
        return null;
      }
    }
  }
  return null;
}

async function processSubject(filename, subjectName) {
  const filePath = path.join(DATA_DIR, filename);
  const raw = await fs.readFile(filePath, 'utf-8');
  const data = JSON.parse(raw);

  const zai = await ZAI.create();

  // Collect all lessons
  const allLessons = [];
  for (const topic of data.lessons.detailedTopics) {
    for (const lesson of topic.lessons) {
      allLessons.push(lesson);
    }
  }

  console.log(`\n📚 Processing ${subjectName}: ${allLessons.length} lessons\n`);

  let success = 0;
  let failed = 0;

  for (let i = 0; i < allLessons.length; i++) {
    const lesson = allLessons[i];
    console.log(`[${i + 1}/${allLessons.length}] ${lesson.title}`);

    const content = await generateLessonContent(zai, subjectName, lesson.title);

    if (content) {
      // Update lesson in place
      lesson.description = content.description;
      lesson.keyPoints = content.keyPoints;
      lesson.examples = content.examples;
      lesson.facts = content.facts;
      lesson.tests = content.tests;
      success++;
      console.log(`  ✅ Success (description: ${content.description.length} chars)`);
    } else {
      failed++;
      console.log(`  ❌ FAILED after retries`);
    }

    // Delay between API calls
    if (i < allLessons.length - 1) {
      await delay(500);
    }
  }

  // Save file after processing all lessons
  await fs.writeFile(filePath, JSON.stringify(data, null, 2), 'utf-8');
  console.log(`\n💾 Saved ${filename}: ${success} success, ${failed} failed\n`);

  return { success, failed };
}

async function main() {
  console.log('🚀 Starting lesson content generation...\n');

  const mathResult = await processSubject('math.json', 'Математика');
  const englishResult = await processSubject('english.json', 'Иностранный язык (English)');

  console.log('\n========== FINAL REPORT ==========');
  console.log(`📐 Math:    ${mathResult.success}/${mathResult.success + mathResult.failed} lessons updated (${mathResult.failed} failures)`);
  console.log(`🔤 English: ${englishResult.success}/${englishResult.success + englishResult.failed} lessons updated (${englishResult.failed} failures)`);
  console.log(`📊 Total:   ${mathResult.success + englishResult.success}/${mathResult.success + mathResult.success + mathResult.failed + englishResult.failed} lessons updated`);
  console.log('==================================\n');
}

main().catch(e => {
  console.error('Fatal error:', e);
  process.exit(1);
});
