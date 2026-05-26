import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const DIR = '/home/z/school-curriculum-app/public/data/grades/2';

async function generateLessonContent(zai, subject, lessonTitle, lessonIndex, totalLessons) {
  const prompt = `Ты — создатель образовательного контента для российских школьников 2 класса (8 лет). 

Предмет: ${subject}
Урок: ${lessonTitle} (урок ${lessonIndex} из ${totalLessons})

Создай ПОЛНЫЙ контент урока в формате JSON. Требования:
- description: подробное описание урока на русском языке, НЕ МЕНЕЕ 800 символов, с заголовками в формате ## и **жирным текстом** для ключевых понятий. Пиши подробно, с примерами и объяснениями.
- keyPoints: массив из 5 ключевых пунктов (строки)
- examples: массив из 5 примеров (строки)
- facts: массив из 3 интересных фактов (строки)
- tests: объект с тремя типами тестов:
  - quiz: массив из 5 вопросов, каждый с полями question (строка), options (массив 4 строк), correct (индекс правильного ответа 0-3)
  - find: массив из 5 заданий "найди ответ", каждый с полями text (строка) и answer (строка)
  - match: массив из 5 пар для сопоставления, каждый с полями term (строка) и definition (строка)

Верни ТОЛЬКО валидный JSON без markdown обёрток. Формат:
{
  "description": "...",
  "keyPoints": ["...","...","...","...","..."],
  "examples": ["...","...","...","...","..."],
  "facts": ["...","...","..."],
  "tests": {
    "quiz": [{"question":"...","options":["...","...","...","..."],"correct":0}, ...],
    "find": [{"text":"...","answer":"..."}, ...],
    "match": [{"term":"...","definition":"..."}, ...]
  }
}`;

  try {
    const completion = await zai.chat.completions.create({
      messages: [
        { role: 'system', content: 'Ты — эксперт по созданию образовательного контента для начальной школы. Отвечай ТОЛЬКО валидным JSON.' },
        { role: 'user', content: prompt }
      ],
      temperature: 0.7,
      max_tokens: 3000
    });
    
    let content = completion.choices[0]?.message?.content || '';
    // Clean markdown wrapping if present
    content = content.replace(/^```json?\s*/i, '').replace(/\s*```\s*$/i, '');
    return JSON.parse(content);
  } catch (e) {
    console.error('  ERROR generating content:', e.message?.substring(0, 100));
    return null;
  }
}

async function rebuildSubject(zai, subjectKey, subjectData) {
  const filePath = DIR + '/' + subjectKey + '.json';
  const existingData = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  const lessons = existingData.lessons?.detailedTopics?.flatMap(t => t.lessons || []) || [];
  
  console.log(`\n=== ${subjectData.title} (${lessons.length} lessons) ===`);
  
  let success = 0;
  let fail = 0;
  
  for (let i = 0; i < lessons.length; i++) {
    const lesson = lessons[i];
    const num = i + 1;
    process.stdout.write(`  L${num}: ${lesson.title.substring(0, 50)}... `);
    
    const content = await generateLessonContent(zai, subjectData.title, lesson.title, num, lessons.length);
    
    if (content) {
      lesson.description = content.description;
      lesson.keyPoints = content.keyPoints;
      lesson.examples = content.examples;
      lesson.facts = content.facts;
      lesson.tests = content.tests;
      success++;
      process.stdout.write('OK ✓\n');
    } else {
      fail++;
      process.stdout.write('FAIL ✗\n');
    }
    
    // Small delay to avoid rate limiting
    await new Promise(r => setTimeout(r, 500));
  }
  
  // Save updated data
  fs.writeFileSync(filePath, JSON.stringify(existingData, null, 2));
  console.log(`  Result: ${success} OK, ${fail} FAIL`);
  return { success, fail };
}

async function main() {
  const zai = await ZAI.create();
  
  const subjects = {
    math: { title: 'Математика' },
    russian: { title: 'Русский язык' },
    literature: { title: 'Литературное чтение' },
    english: { title: 'Английский язык' },
    art: { title: 'Изобразительное искусство' },
    music: { title: 'Музыка' },
    pe: { title: 'Физическая культура' },
    tech: { title: 'Технология' },
    projects: { title: 'Проектная деятельность' },
    world: { title: 'Окружающий мир' },
  };
  
  let totalSuccess = 0;
  let totalFail = 0;
  
  for (const [key, data] of Object.entries(subjects)) {
    const result = await rebuildSubject(zai, key, data);
    totalSuccess += result.success;
    totalFail += result.fail;
  }
  
  console.log(`\n=== TOTAL: ${totalSuccess} OK, ${totalFail} FAIL ===`);
  
  // Rebuild _bundle.json
  const bundle = {};
  const files = fs.readdirSync(DIR).filter(f => f.endsWith('.json') && f !== '_bundle.json');
  files.forEach(f => {
    bundle[f.replace('.json', '')] = JSON.parse(fs.readFileSync(DIR + '/' + f, 'utf8'));
  });
  fs.writeFileSync(DIR + '/_bundle.json', JSON.stringify(bundle));
  console.log('_bundle.json rebuilt');
}

main().catch(console.error);
