import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const FILE_PATH = '/home/z/school-curriculum-app/public/data/grades/2/projects.json';
const LOG_PATH = '/home/z/school-curriculum-app/gen-log.txt';

const delay = (ms) => new Promise(r => setTimeout(r, ms));

function log(msg) {
  const ts = new Date().toISOString();
  const line = `[${ts}] ${msg}\n`;
  fs.appendFileSync(LOG_PATH, line);
  console.log(line.trim());
}

async function main() {
  // Clear log
  fs.writeFileSync(LOG_PATH, '');
  log('Starting generation script');

  const data = JSON.parse(fs.readFileSync(FILE_PATH, 'utf-8'));
  const zai = await ZAI.create();
  log('SDK initialized');

  const lessonEntries = [];
  for (let t = 0; t < data.lessons.detailedTopics.length; t++) {
    const topic = data.lessons.detailedTopics[t];
    for (let l = 0; l < topic.lessons.length; l++) {
      lessonEntries.push({ topicIdx: t, lessonIdx: l, lesson: topic.lessons[l] });
    }
  }

  let fixed = 0;

  for (let i = 0; i < lessonEntries.length; i++) {
    const { lesson } = lessonEntries[i];
    const num = i + 1;
    const title = lesson.title;
    log(`Processing lesson ${num}/12: ${title}`);

    const userPrompt = `Для урока 2 класса. Предмет: Проектная деятельность. Урок: ${title}. Создай: keyPoints: 5 ключевых пунктов, examples: 5 примеров, facts: 3 интересных факта, tests: {quiz:[5 {question,options[4],correct}], find:[5 {text,answer}], match:[5 {term,definition}]}. ВЕРНИ JSON: {"keyPoints":[...],"examples":[...],"facts":[...],"tests":{"quiz":[...],"find":[...],"match":[...]}}`;

    let success = false;
    for (let attempt = 0; attempt < 15; attempt++) {
      try {
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

        if (num >= 2 && g.keyPoints?.length >= 5) {
          lesson.keyPoints = g.keyPoints.slice(0, 5);
          log(`  ✓ keyPoints: ${lesson.keyPoints.length}`);
        }
        if (num >= 2 && g.examples?.length >= 5) {
          lesson.examples = g.examples.slice(0, 5);
          log(`  ✓ examples: ${lesson.examples.length}`);
        }
        if (g.facts?.length >= 3) {
          lesson.facts = g.facts.slice(0, 3);
          log(`  ✓ facts: ${lesson.facts.length}`);
        }
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
          log(`  ✓ tests: quiz=${lesson.tests.quiz.length}, find=${lesson.tests.find.length}, match=${lesson.tests.match.length}`);
        }

        // Save after each successful lesson
        fs.writeFileSync(FILE_PATH, JSON.stringify(data, null, 2), 'utf-8');
        log(`  Lesson ${num} saved`);
        fixed++;
        success = true;
        break;

      } catch (err) {
        const is429 = err.message?.includes('429');
        const waitMs = is429 ? Math.min((attempt + 1) * 15000, 120000) : 5000;
        log(`  Attempt ${attempt + 1} failed: ${err.message?.substring(0, 80)}`);
        log(`  Waiting ${waitMs / 1000}s...`);
        await delay(waitMs);
      }
    }

    if (!success) {
      log(`  FAILED lesson ${num} after 15 attempts`);
    }

    // Delay between lessons
    if (i < lessonEntries.length - 1) {
      log(`  Waiting 3s before next lesson...`);
      await delay(3000);
    }
  }

  log(`\n=== COMPLETE: ${fixed}/12 lessons fixed ===`);
}

main().catch(err => { log(`Fatal: ${err.message}`); process.exit(1); });
