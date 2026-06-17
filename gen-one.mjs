import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const FILE_PATH = '/home/z/school-curriculum-app/public/data/grades/2/projects.json';

const delay = (ms) => new Promise(r => setTimeout(r, ms));

async function main() {
  const lessonNum = parseInt(process.argv[2]);
  if (!lessonNum || lessonNum < 1 || lessonNum > 12) {
    console.error('Usage: node gen-one.mjs <1-12>');
    process.exit(1);
  }

  const data = JSON.parse(fs.readFileSync(FILE_PATH, 'utf-8'));
  const zai = await ZAI.create();

  // Find the lesson
  const lessonEntries = [];
  for (let t = 0; t < data.lessons.detailedTopics.length; t++) {
    const topic = data.lessons.detailedTopics[t];
    for (let l = 0; l < topic.lessons.length; l++) {
      lessonEntries.push({ topicIdx: t, lessonIdx: l, lesson: topic.lessons[l] });
    }
  }

  const { lesson } = lessonEntries[lessonNum - 1];
  const title = lesson.title;
  console.log(`Lesson ${lessonNum}: ${title}`);

  const userPrompt = `Для урока 2 класса. Предмет: Проектная деятельность. Урок: ${title}. Создай: keyPoints: 5 ключевых пунктов, examples: 5 примеров, facts: 3 интересных факта, tests: {quiz:[5 {question,options[4],correct}], find:[5 {text,answer}], match:[5 {term,definition}]}. ВЕРНИ JSON: {"keyPoints":[...],"examples":[...],"facts":[...],"tests":{"quiz":[...],"find":[...],"match":[...]}}`;

  // Retry with increasing wait
  for (let attempt = 0; attempt < 10; attempt++) {
    try {
      console.log(`  Attempt ${attempt + 1}...`);
      const response = await zai.chat.completions.create({
        messages: [
          { role: 'system', content: 'Ты эксперт по проектной деятельности для начальной школы. Только валидный JSON.' },
          { role: 'user', content: userPrompt }
        ],
        max_tokens: 2500,
        temperature: 0.7,
        thinking: { type: 'disabled' }
      });

      const raw = response.choices?.[0]?.message?.content || '';
      let jsonStr = raw.trim();
      const codeMatch = jsonStr.match(/```(?:json)?\s*([\s\S]*?)```/);
      if (codeMatch) jsonStr = codeMatch[1].trim();
      const objMatch = jsonStr.match(/\{[\s\S]*\}/);
      if (objMatch) jsonStr = objMatch[0];

      const g = JSON.parse(jsonStr);

      // Apply keyPoints for lessons 2-12
      if (lessonNum >= 2 && g.keyPoints?.length >= 5) {
        lesson.keyPoints = g.keyPoints.slice(0, 5);
        console.log(`  ✓ keyPoints: ${lesson.keyPoints.length}`);
      }
      // Apply examples for lessons 2-12
      if (lessonNum >= 2 && g.examples?.length >= 5) {
        lesson.examples = g.examples.slice(0, 5);
        console.log(`  ✓ examples: ${lesson.examples.length}`);
      }
      // Apply facts for all
      if (g.facts?.length >= 3) {
        lesson.facts = g.facts.slice(0, 3);
        console.log(`  ✓ facts: ${lesson.facts.length}`);
      }
      // Apply tests for all
      if (g.tests?.quiz?.length >= 5) {
        lesson.tests = {
          quiz: g.tests.quiz.slice(0, 5).map(q => ({
            question: q.question,
            options: q.options?.slice(0, 4) || ['', '', '', ''],
            correct: typeof q.correct === 'number' ? q.correct : 0
          })),
          find: (g.tests.find || []).slice(0, 5).map(f => ({ text: f.text, answer: f.answer })),
          match: (g.tests.match || []).slice(0, 5).map(m => ({ term: m.term, definition: m.definition }))
        };
        console.log(`  ✓ tests: quiz=${lesson.tests.quiz.length}, find=${lesson.tests.find.length}, match=${lesson.tests.match.length}`);
      }

      fs.writeFileSync(FILE_PATH, JSON.stringify(data, null, 2), 'utf-8');
      console.log('SUCCESS');
      process.exit(0);

    } catch (err) {
      const isRateLimit = err.message?.includes('429');
      const waitMs = isRateLimit ? (attempt + 1) * 20000 : 5000;
      console.log(`  Error: ${err.message.substring(0, 80)}`);
      if (attempt < 9) {
        console.log(`  Waiting ${waitMs / 1000}s...`);
        await delay(waitMs);
      } else {
        console.error('FAILED after 10 attempts');
        process.exit(1);
      }
    }
  }
}

main().catch(err => { console.error('Fatal:', err); process.exit(1); });
