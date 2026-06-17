import fs from 'fs';

const ZAI_SDK = (await import('z-ai-web-dev-sdk')).default;
const zai = await ZAI_SDK.create();

const filePath = '/home/z/school-curriculum-app/public/data/grades/2/literature.json';
const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));

// Collect all lessons with their paths
const lessons = [];
for (let t = 0; t < data.lessons.detailedTopics.length; t++) {
  const topic = data.lessons.detailedTopics[t];
  for (let l = 0; l < topic.lessons.length; l++) {
    const lesson = topic.lessons[l];
    lessons.push({ topicIdx: t, lessonIdx: l, lesson });
  }
}

console.log(`Found ${lessons.length} lessons total\n`);

// Retry helper with aggressive exponential backoff
async function callLLMWithRetry(messages, maxRetries = 8) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      const response = await zai.chat.completions.create({
        messages,
        max_tokens: 2000,
        temperature: 0.7
      });
      return response;
    } catch (err) {
      const is429 = err.message && err.message.includes('429');
      if (is429) {
        const waitMs = Math.pow(2, attempt) * 5000 + Math.random() * 3000; // 5s, 10s, 20s, 40s, 80s, 160s, 320s, 640s + jitter
        console.log(`    Rate limited, waiting ${Math.round(waitMs/1000)}s before retry ${attempt+1}/${maxRetries}...`);
        await new Promise(r => setTimeout(r, waitMs));
      } else {
        throw err;
      }
    }
  }
  throw new Error('Max retries exceeded');
}

let fixedCount = 0;

for (let i = 0; i < lessons.length; i++) {
  const { topicIdx, lessonIdx, lesson } = lessons[i];
  const title = lesson.title;
  const kpCount = (lesson.keyPoints || []).length;
  const exCount = (lesson.examples || []).length;
  const factsCount = (lesson.facts || []).length;
  const hasTests = lesson.tests && lesson.tests.quiz && lesson.tests.find && lesson.tests.match;

  console.log(`[${i+1}/10] ${title}`);
  console.log(`  keyPoints: ${kpCount}, examples: ${exCount}, facts: ${factsCount}, tests: ${hasTests ? 'YES' : 'NO'}`);

  const needsKp = kpCount < 4;
  const needsEx = exCount < 4;
  const needsFacts = factsCount < 3;
  const needsTests = !hasTests;

  if (!needsKp && !needsEx && !needsFacts && !needsTests) {
    console.log('  -> SKIP (all good)\n');
    continue;
  }

  const prompt = `Для урока 2 класса Предмет: Литературное чтение. Урок: ${title}. Создай: 1) facts: 3 интересных факта, 2) tests: {quiz:[5 {question,options[4],correct}], find:[5 {text,answer}], match:[5 {term,definition}]}. Также если keyPoints меньше 4, создай 5 ключевых пунктов. Если examples меньше 4, создай 5 примеров. ВЕРНИ JSON: {"keyPoints":[...],"examples":[...],"facts":[...],"tests":{"quiz":[...],"find":[...],"match":[...]}}`;

  try {
    const response = await callLLMWithRetry([
      { role: 'system', content: 'Ты эксперт по начальному образованию. Только валидный JSON.' },
      { role: 'user', content: prompt }
    ]);

    let content = response.choices?.[0]?.message?.content || response.content || '';
    if (typeof content !== 'string') content = JSON.stringify(content);

    // Extract JSON from response - find the outermost balanced braces
    let jsonStr = content;
    const firstBrace = content.indexOf('{');
    if (firstBrace >= 0) {
      // Find the matching closing brace
      let depth = 0;
      let endIdx = -1;
      for (let c = firstBrace; c < content.length; c++) {
        if (content[c] === '{') depth++;
        if (content[c] === '}') depth--;
        if (depth === 0) { endIdx = c; break; }
      }
      if (endIdx > 0) jsonStr = content.substring(firstBrace, endIdx + 1);
    }

    let generated;
    try {
      generated = JSON.parse(jsonStr);
    } catch (e) {
      console.log(`  -> ERROR parsing JSON: ${e.message}`);
      console.log(`  JSON start: ${jsonStr.substring(0, 200)}\n`);
      continue;
    }

    // Apply generated content
    if (needsFacts && generated.facts) {
      data.lessons.detailedTopics[topicIdx].lessons[lessonIdx].facts = generated.facts;
      console.log(`  + facts: ${generated.facts.length}`);
    }
    if (needsTests && generated.tests) {
      data.lessons.detailedTopics[topicIdx].lessons[lessonIdx].tests = generated.tests;
      console.log(`  + tests: quiz=${(generated.tests.quiz||[]).length}, find=${(generated.tests.find||[]).length}, match=${(generated.tests.match||[]).length}`);
    }
    if (needsKp && generated.keyPoints) {
      data.lessons.detailedTopics[topicIdx].lessons[lessonIdx].keyPoints = generated.keyPoints;
      console.log(`  + keyPoints: ${generated.keyPoints.length}`);
    }
    if (needsEx && generated.examples) {
      data.lessons.detailedTopics[topicIdx].lessons[lessonIdx].examples = generated.examples;
      console.log(`  + examples: ${generated.examples.length}`);
    }

    fixedCount++;
    console.log('  -> FIXED\n');
  } catch (err) {
    console.log(`  -> ERROR: ${err.message}\n`);
  }

  // 5 second delay between lessons
  if (i < lessons.length - 1) {
    console.log('  Waiting 5s before next lesson...');
    await new Promise(r => setTimeout(r, 5000));
  }
}

// Save the updated file
fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf-8');
console.log(`\n=== DONE ===`);
console.log(`Lessons fixed: ${fixedCount} out of ${lessons.length}`);
