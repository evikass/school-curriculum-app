import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const FILE = '/home/z/school-curriculum-app/public/data/grades/2/projects.json';
const PROG = '/home/z/school-curriculum-app/progress.json';

async function main() {
  const lessonNum = parseInt(process.argv[2]);
  if (!lessonNum) { console.error('Need lesson number 1-12'); process.exit(1); }

  const data = JSON.parse(fs.readFileSync(FILE, 'utf-8'));
  
  // Find lesson
  let lesson, idx = 0;
  for (let t = 0; t < data.lessons.detailedTopics.length; t++) {
    for (let l = 0; l < data.lessons.detailedTopics[t].lessons.length; l++) {
      idx++;
      if (idx === lessonNum) {
        lesson = data.lessons.detailedTopics[t].lessons[l];
        break;
      }
    }
    if (lesson) break;
  }

  const title = lesson.title;
  console.log(`Lesson ${lessonNum}: ${title}`);

  const zai = await ZAI.create();
  const prompt = `Для урока 2 класса. Предмет: Проектная деятельность. Урок: ${title}. Создай: keyPoints: 5 ключевых пунктов, examples: 5 примеров, facts: 3 интересных факта, tests: {quiz:[5 {question,options[4],correct}], find:[5 {text,answer}], match:[5 {term,definition}]}. ВЕРНИ JSON: {"keyPoints":[...],"examples":[...],"facts":[...],"tests":{"quiz":[...],"find":[...],"match":[...]}}`;

  const response = await zai.chat.completions.create({
    messages: [
      { role: 'system', content: 'Ты эксперт по проектной деятельности для начальной школы. Только валидный JSON.' },
      { role: 'user', content: prompt }
    ],
    max_tokens: 2500,
    temperature: 0.7,
    thinking: { type: 'disabled' }
  });

  const raw = response.choices?.[0]?.message?.content || '';
  let s = raw.trim();
  const cm = s.match(/```(?:json)?\s*([\s\S]*?)```/);
  if (cm) s = cm[1].trim();
  const om = s.match(/\{[\s\S]*\}/);
  if (om) s = om[0];
  const g = JSON.parse(s);

  if (lessonNum >= 2 && g.keyPoints?.length >= 5) { lesson.keyPoints = g.keyPoints.slice(0,5); console.log('keyPoints:', lesson.keyPoints.length); }
  if (lessonNum >= 2 && g.examples?.length >= 5) { lesson.examples = g.examples.slice(0,5); console.log('examples:', lesson.examples.length); }
  if (g.facts?.length >= 3) { lesson.facts = g.facts.slice(0,3); console.log('facts:', lesson.facts.length); }
  if (g.tests?.quiz?.length >= 5) {
    lesson.tests = {
      quiz: g.tests.quiz.slice(0,5).map(q => ({question:q.question,options:q.options?.slice(0,4)||['','','',''],correct:typeof q.correct==='number'?q.correct:0})),
      find: (g.tests.find||[]).slice(0,5).map(f => ({text:f.text,answer:f.answer})),
      match: (g.tests.match||[]).slice(0,5).map(m => ({term:m.term,definition:m.definition}))
    };
    console.log('tests: quiz='+lesson.tests.quiz.length+' find='+lesson.tests.find.length+' match='+lesson.tests.match.length);
  }

  fs.writeFileSync(FILE, JSON.stringify(data, null, 2), 'utf-8');
  
  // Update progress
  let prog = {completed:[]};
  try { prog = JSON.parse(fs.readFileSync(PROG,'utf-8')); } catch {}
  prog.completed.push(lessonNum);
  fs.writeFileSync(PROG, JSON.stringify(prog), 'utf-8');
  
  console.log('OK');
}

main().catch(e => { console.error('ERR:', e.message?.substring(0,100)); process.exit(1); });
