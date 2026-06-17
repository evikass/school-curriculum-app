import fs from 'fs';
import ZAI from 'z-ai-web-dev-sdk';

const FILE_PATH = '/home/z/school-curriculum-app/public/data/grades/2/pe.json';
const PROGRESS_PATH = '/tmp/pe_progress.json';

async function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function generateContent(zai, lessonTitle) {
  const prompt = `Для урока 2 класса. Предмет: Физическая культура. Урок: ${lessonTitle}. Создай: facts: 3 интересных факта о спорте и физкультуре, tests: {quiz:[5 вопросов {question,options[4],correct}], find:[5 {text,answer}], match:[5 {term,definition}]}. ВЕРНИ JSON: {"facts":[...],"tests":{"quiz":[...],"find":[...],"match":[...]}}`;

  const systemPrompt = "Ты эксперт по физической культуре для начальной школы. Только валидный JSON.";

  let retries = 0;
  while (retries < 30) {
    try {
      const response = await zai.chat.completions.create({
        messages: [
          { role: "system", content: systemPrompt },
          { role: "user", content: prompt }
        ],
        max_tokens: 2000,
        temperature: 0.7
      });

      const raw = response.choices?.[0]?.message?.content || '';
      
      let jsonStr = raw;
      const jsonMatch = raw.match(/```(?:json)?\s*([\s\S]*?)```/);
      if (jsonMatch) jsonStr = jsonMatch[1];
      
      const objMatch = jsonStr.match(/\{[\s\S]*\}/);
      if (objMatch) jsonStr = objMatch[0];
      
      try {
        return JSON.parse(jsonStr);
      } catch (e) {
        fs.appendFileSync('/tmp/pe_errors.log', `[${new Date().toISOString()}] Parse error for "${lessonTitle}": ${e.message}\nRaw: ${raw.substring(0, 200)}\n\n`);
        return null;
      }
    } catch (err) {
      if (err.message && err.message.includes('429')) {
        const waitSec = 30 + retries * 5;
        fs.appendFileSync('/tmp/pe_progress.log', `[${new Date().toISOString()}] Rate limited for "${lessonTitle}", waiting ${waitSec}s (attempt ${retries+1})...\n`);
        await delay(waitSec * 1000);
        retries++;
      } else {
        fs.appendFileSync('/tmp/pe_errors.log', `[${new Date().toISOString()}] API error for "${lessonTitle}": ${err.message.substring(0, 100)}\n`);
        return null;
      }
    }
  }
  return null;
}

async function main() {
  fs.writeFileSync('/tmp/pe_progress.log', `[${new Date().toISOString()}] Starting PE content generation\n`);
  
  const zai = await ZAI.create();
  const data = JSON.parse(fs.readFileSync(FILE_PATH, 'utf-8'));
  
  let processed = new Set();
  try {
    const p = JSON.parse(fs.readFileSync(PROGRESS_PATH, 'utf-8'));
    processed = new Set(p.processed || []);
  } catch {}
  
  // Collect all lessons with their references
  const lessonRefs = [];
  for (const topic of data.lessons.detailedTopics) {
    for (const lesson of topic.lessons) {
      lessonRefs.push({ topic: topic.topic, lesson });
    }
  }
  
  fs.appendFileSync('/tmp/pe_progress.log', `Found ${lessonRefs.length} lessons, ${processed.size} already done\n`);
  
  let fixedCount = 0;
  
  for (let i = 0; i < lessonRefs.length; i++) {
    const { lesson } = lessonRefs[i];
    
    if (processed.has(lesson.title)) {
      fs.appendFileSync('/tmp/pe_progress.log', `[${i+1}] SKIP ${lesson.title}\n`);
      continue;
    }
    
    if (lesson.facts?.length > 0 && lesson.tests?.quiz?.length > 0 && lesson.tests?.find?.length > 0 && lesson.tests?.match?.length > 0) {
      processed.add(lesson.title);
      fs.writeFileSync(PROGRESS_PATH, JSON.stringify({ processed: [...processed] }));
      fs.appendFileSync('/tmp/pe_progress.log', `[${i+1}] SKIP (has data) ${lesson.title}\n`);
      continue;
    }
    
    fs.appendFileSync('/tmp/pe_progress.log', `[${new Date().toISOString()}] [${i+1}/${lessonRefs.length}] Processing: ${lesson.title}\n`);
    
    const content = await generateContent(zai, lesson.title);
    
    if (content) {
      if (content.facts && Array.isArray(content.facts)) {
        lesson.facts = content.facts;
      }
      if (content.tests) {
        lesson.tests = content.tests;
      }
      fixedCount++;
      fs.appendFileSync('/tmp/pe_progress.log', `[${i+1}] DONE ${lesson.title}: facts=${content.facts?.length}, quiz=${content.tests?.quiz?.length}, find=${content.tests?.find?.length}, match=${content.tests?.match?.length}\n`);
    } else {
      fs.appendFileSync('/tmp/pe_progress.log', `[${i+1}] FAILED ${lesson.title}\n`);
    }
    
    processed.add(lesson.title);
    fs.writeFileSync(PROGRESS_PATH, JSON.stringify({ processed: [...processed] }));
    
    // Save intermediate result
    fs.writeFileSync(FILE_PATH, JSON.stringify(data, null, 2), 'utf-8');
    fs.appendFileSync('/tmp/pe_progress.log', `[${i+1}] File saved\n`);
    
    // Wait between calls
    await delay(3000);
  }
  
  fs.writeFileSync(FILE_PATH, JSON.stringify(data, null, 2), 'utf-8');
  fs.appendFileSync('/tmp/pe_progress.log', `\n[${new Date().toISOString()}] COMPLETE! Fixed ${fixedCount}/${lessonRefs.length} lessons.\n`);
}

main().catch(err => {
  fs.appendFileSync('/tmp/pe_errors.log', `[${new Date().toISOString()}] FATAL: ${err.message}\n`);
  process.exit(1);
});
