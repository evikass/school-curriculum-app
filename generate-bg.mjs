import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const FILE_PATH = '/home/z/school-curriculum-app/public/data/grades/2/projects.json';
const PROGRESS_PATH = '/home/z/school-curriculum-app/progress.json';
const delay = (ms) => new Promise(r => setTimeout(r, ms));

async function callLLM(zai, messages, maxRetries = 30) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await zai.chat.completions.create({
        messages,
        max_tokens: 2500,
        temperature: 0.7,
        thinking: { type: 'disabled' }
      });
    } catch (err) {
      if (err.message?.includes('429')) {
        const waitMs = 30000 + i * 5000; // 30s, 35s, 40s, 45s...
        process.stdout.write(`[429 wait ${waitMs/1000}s]`);
        await delay(waitMs);
      } else {
        throw err;
      }
    }
  }
  throw new Error('Max retries exceeded');
}

async function main() {
  const data = JSON.parse(fs.readFileSync(FILE_PATH, 'utf-8'));
  const zai = await ZAI.create();
  
  let progress = { completed: [] };
  try { progress = JSON.parse(fs.readFileSync(PROGRESS_PATH, 'utf-8')); } catch {}

  const lessonEntries = [];
  for (let t = 0; t < data.lessons.detailedTopics.length; t++) {
    for (let l = 0; l < data.lessons.detailedTopics[t].lessons.length; l++) {
      lessonEntries.push({ topicIdx: t, lessonIdx: l, lesson: data.lessons.detailedTopics[t].lessons[l], num: lessonEntries.length + 1 });
    }
  }

  console.log(`Total lessons: ${lessonEntries.length}, already done: ${progress.completed.length}`);

  for (const entry of lessonEntries) {
    if (progress.completed.includes(entry.num)) {
      console.log(`Skip lesson ${entry.num} (done)`);
      continue;
    }
    
    const { lesson, num } = entry;
    const title = lesson.title;
    console.log(`\nLesson ${num}/12: ${title}`);

    const userPrompt = `Для урока 2 класса. Предмет: Проектная деятельность. Урок: ${title}. Создай: keyPoints: 5 ключевых пунктов, examples: 5 примеров, facts: 3 интересных факта, tests: {quiz:[5 {question,options[4],correct}], find:[5 {text,answer}], match:[5 {term,definition}]}. ВЕРНИ JSON: {"keyPoints":[...],"examples":[...],"facts":[...],"tests":{"quiz":[...],"find":[...],"match":[...]}}`;

    try {
      const response = await callLLM(zai, [
        { role: 'system', content: 'Ты эксперт по проектной деятельности для начальной школы. Только валидный JSON.' },
        { role: 'user', content: userPrompt }
      ]);

      const raw = response.choices?.[0]?.message?.content || '';
      let jsonStr = raw.trim();
      const codeMatch = jsonStr.match(/```(?:json)?\s*([\s\S]*?)```/);
      if (codeMatch) jsonStr = codeMatch[1].trim();
      const objMatch = jsonStr.match(/\{[\s\S]*\}/);
      if (objMatch) jsonStr = objMatch[0];
      const g = JSON.parse(jsonStr);

      if (num >= 2 && g.keyPoints?.length >= 5) {
        lesson.keyPoints = g.keyPoints.slice(0, 5);
        console.log(`  + keyPoints: ${lesson.keyPoints.length}`);
      }
      if (num >= 2 && g.examples?.length >= 5) {
        lesson.examples = g.examples.slice(0, 5);
        console.log(`  + examples: ${lesson.examples.length}`);
      }
      if (g.facts?.length >= 3) {
        lesson.facts = g.facts.slice(0, 3);
        console.log(`  + facts: ${lesson.facts.length}`);
      }
      if (g.tests?.quiz?.length >= 5) {
        lesson.tests = {
          quiz: g.tests.quiz.slice(0, 5).map(q => ({ question: q.question, options: q.options?.slice(0, 4) || ['','','',''], correct: typeof q.correct === 'number' ? q.correct : 0 })),
          find: (g.tests.find || []).slice(0, 5).map(f => ({ text: f.text, answer: f.answer })),
          match: (g.tests.match || []).slice(0, 5).map(m => ({ term: m.term, definition: m.definition }))
        };
        console.log(`  + tests: quiz=${lesson.tests.quiz.length} find=${lesson.tests.find.length} match=${lesson.tests.match.length}`);
      }

      fs.writeFileSync(FILE_PATH, JSON.stringify(data, null, 2), 'utf-8');
      progress.completed.push(num);
      fs.writeFileSync(PROGRESS_PATH, JSON.stringify(progress, null, 2), 'utf-8');
      console.log(`  Saved!`);

      await delay(500); // 500ms between calls as requested
      
    } catch (err) {
      console.error(`  FAILED: ${err.message?.substring(0, 100)}`);
    }
  }

  console.log(`\n=== DONE: ${progress.completed.length}/12 ===`);
}

main().catch(err => { console.error('Fatal:', err.message); process.exit(1); });
