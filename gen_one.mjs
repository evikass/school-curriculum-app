import fs from 'fs';

const ZAI_SDK = (await import('z-ai-web-dev-sdk')).default;

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

// Find which lesson to process based on command line arg
const lessonNum = parseInt(process.argv[2] || '1');
const idx = lessonNum - 1;
if (idx < 0 || idx >= lessons.length) {
  console.log(`Invalid lesson number. Use 1-${lessons.length}`);
  process.exit(1);
}

const { topicIdx, lessonIdx, lesson } = lessons[idx];
const title = lesson.title;
const kpCount = (lesson.keyPoints || []).length;
const exCount = (lesson.examples || []).length;
const factsCount = (lesson.facts || []).length;
const hasTests = lesson.tests && lesson.tests.quiz && lesson.tests.find && lesson.tests.match;

console.log(`Processing: ${title}`);
console.log(`keyPoints: ${kpCount}, examples: ${exCount}, facts: ${factsCount}, tests: ${hasTests ? 'YES' : 'NO'}`);

const needsKp = kpCount < 4;
const needsEx = exCount < 4;
const needsFacts = factsCount < 3;
const needsTests = !hasTests;

if (!needsKp && !needsEx && !needsFacts && !needsTests) {
  console.log('SKIP - all good');
  process.exit(0);
}

const prompt = `Для урока 2 класса Предмет: Литературное чтение. Урок: ${title}. Создай: 1) facts: 3 интересных факта, 2) tests: {quiz:[5 {question,options[4],correct}], find:[5 {text,answer}], match:[5 {term,definition}]}. Также если keyPoints меньше 4, создай 5 ключевых пунктов. Если examples меньше 4, создай 5 примеров. ВЕРНИ JSON: {"keyPoints":[...],"examples":[...],"facts":[...],"tests":{"quiz":[...],"find":[...],"match":[...]}}`;

// Very aggressive retry with exponential backoff
async function callLLM(messages) {
  const zai = await ZAI_SDK.create();
  for (let attempt = 0; attempt < 10; attempt++) {
    try {
      const response = await zai.chat.completions.create({
        messages,
        max_tokens: 2000,
        temperature: 0.7
      });
      return response;
    } catch (err) {
      if (err.message && (err.message.includes('429') || err.message.includes('rate'))) {
        const waitMs = (attempt + 1) * 15000 + Math.random() * 5000; // 15s, 30s, 45s, ... + jitter
        console.log(`Rate limited, waiting ${Math.round(waitMs/1000)}s (attempt ${attempt+1}/10)...`);
        await new Promise(r => setTimeout(r, waitMs));
      } else {
        throw err;
      }
    }
  }
  throw new Error('Max retries exceeded');
}

const response = await callLLM([
  { role: 'system', content: 'Ты эксперт по начальному образованию. Только валидный JSON.' },
  { role: 'user', content: prompt }
]);

let content = response.choices?.[0]?.message?.content || '';
if (typeof content !== 'string') content = JSON.stringify(content);

// Extract JSON
const firstBrace = content.indexOf('{');
let jsonStr = content;
if (firstBrace >= 0) {
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
  console.log(`ERROR parsing JSON: ${e.message}`);
  console.log(`JSON start: ${jsonStr.substring(0, 300)}`);
  process.exit(1);
}

// Apply generated content
if (needsFacts && generated.facts) {
  data.lessons.detailedTopics[topicIdx].lessons[lessonIdx].facts = generated.facts;
  console.log(`+ facts: ${generated.facts.length}`);
}
if (needsTests && generated.tests) {
  data.lessons.detailedTopics[topicIdx].lessons[lessonIdx].tests = generated.tests;
  console.log(`+ tests: quiz=${(generated.tests.quiz||[]).length}, find=${(generated.tests.find||[]).length}, match=${(generated.tests.match||[]).length}`);
}
if (needsKp && generated.keyPoints) {
  data.lessons.detailedTopics[topicIdx].lessons[lessonIdx].keyPoints = generated.keyPoints;
  console.log(`+ keyPoints: ${generated.keyPoints.length}`);
}
if (needsEx && generated.examples) {
  data.lessons.detailedTopics[topicIdx].lessons[lessonIdx].examples = generated.examples;
  console.log(`+ examples: ${generated.examples.length}`);
}

fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf-8');
console.log('SAVED successfully');
