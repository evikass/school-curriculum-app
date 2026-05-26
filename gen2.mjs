import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
import path from 'path';

const DIR = '/home/z/school-curriculum-app/public/data/grades/2';
const SUBJECT = process.argv[2];
const NAMES = { art: 'Изобразительное искусство', music: 'Музыка', pe: 'Физическая культура' };
const name = NAMES[SUBJECT];
if (!name) { console.error('Usage: node gen2.mjs <art|music|pe>'); process.exit(1); }

const SYS = "Ты эксперт по начальному образованию России. Отвечай ТОЛЬКО валидным JSON без markdown обёрток. Описание урока должно быть РАЗВЁРНУТЫМ — минимум 800 символов.";

function mkPrompt(subj, title) {
  return `Создай ПОДРОБНЫЙ контент урока для 2 класса (8 лет). Предмет: ${subj}. Урок: ${title}. Описание должно быть НЕ МЕНЕЕ 800 символов, с заголовками ## и **жирным текстом**. ВЕРНИ ТОЛЬКО JSON: {"description":"...минимум 800 символов...","keyPoints":["...5 пунктов..."],"examples":["...5 примеров..."],"facts":["...3 факта..."],"tests":{"quiz":[{"question":"...","options":["...","...","...","..."],"correct":0},...5 вопросов],"find":[{"text":"...","answer":"..."},...5 заданий],"match":[{"term":"...","definition":"..."},...5 пар]}}`;
}

function parse(txt) {
  let c = txt.replace(/^```(?:json)?\s*/i,'').replace(/\s*```\s*$/i,'');
  try { return JSON.parse(c); } catch(e) {
    const m = c.match(/\{[\s\S]*\}/);
    if (m) try { return JSON.parse(m[0]); } catch(e2) {}
    throw new Error('Cannot parse JSON');
  }
}

function ok(c) {
  return c.description?.length >= 800 && c.keyPoints?.length >= 5 && c.examples?.length >= 5 && c.facts?.length >= 3 && c.tests?.quiz?.length >= 5 && c.tests?.find?.length >= 5 && c.tests?.match?.length >= 5;
}

const sleep = ms => new Promise(r => setTimeout(r, ms));

async function main() {
  const zai = await ZAI.create();
  console.log(`${name}: starting`);
  const filePath = path.join(DIR, SUBJECT + '.json');
  const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  let done = 0, failed = 0, n = 0;

  for (const topic of data.lessons.detailedTopics) {
    for (const lesson of topic.lessons) {
      n++;
      console.log(`[${n}] ${lesson.title}`);
      
      let content = null;
      for (let attempt = 0; attempt < 3; attempt++) {
        try {
          const extra = attempt > 0 ? ' ОПИСАНИЕ ОБЯЗАТЕЛЬНО МИНИМУМ 800 СИМВОЛОВ!' : '';
          const resp = await zai.chat.completions.create({
            messages: [
              { role: 'system', content: SYS },
              { role: 'user', content: mkPrompt(name, lesson.title) + extra },
            ],
            temperature: 0.7,
            max_tokens: 3000,
          });
          content = parse(resp.choices[0].message.content);
          if (!ok(content)) { console.log(`  retry ${attempt+1}: desc=${content.description?.length}`); await sleep(300); if (attempt < 2) continue; }
          break;
        } catch(e) { console.log(`  err ${attempt+1}: ${e.message?.substring(0,80)}`); await sleep(300); content = null; }
      }

      if (content && ok(content)) {
        lesson.description = content.description;
        lesson.keyPoints = content.keyPoints;
        lesson.examples = content.examples;
        lesson.facts = content.facts;
        lesson.tests = content.tests;
        done++;
        console.log(`  ✅ desc=${content.description.length}`);
      } else { failed++; console.log(`  ❌`); }
      
      // Save after each lesson
      fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf-8');
      await sleep(500);
    }
  }

  console.log(`\n${SUBJECT}: ${done}/${n} OK, ${failed} FAIL`);
}

main().catch(e => { console.error(e); process.exit(1); });
