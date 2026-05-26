const fs = require('fs');

// We'll use dynamic import for the SDK
async function main() {
  const ZAI = (await import('z-ai-web-dev-sdk')).default;
  const zai = await ZAI.create();

  const DIR = '/home/z/school-curriculum-app/public/data/grades/2';

  async function generateLessonContent(subject, lessonTitle, lessonIndex, totalLessons) {
    const prompt = `Ты — создатель образовательного контента для российских школьников 2 класса (8 лет). 

Предмет: ${subject}
Урок: ${lessonTitle} (урок ${lessonIndex} из ${totalLessons})

Создай ПОЛНЫЙ контент урока в формате JSON. Требования:
- description: подробное описание урока на русском языке, НЕ МЕНЕЕ 800 символов, с заголовками ## и **жирным текстом** для ключевых понятий. Пиши подробно, с примерами и объяснениями для 8-летних детей.
- keyPoints: массив из 5 ключевых пунктов (строки)
- examples: массив из 5 примеров (строки)
- facts: массив из 3 интересных фактов (строки)
- tests: объект с тремя типами тестов:
  - quiz: массив из 5 вопросов, каждый с полями question (строка), options (массив 4 строк), correct (индекс правильного 0-3)
  - find: массив из 5 заданий, каждый с полями text (строка) и answer (строка)
  - match: массив из 5 пар, каждый с полями term (строка) и definition (строка)

Верни ТОЛЬКО валидный JSON без markdown.`;

    try {
      const completion = await zai.chat.completions.create({
        messages: [
          { role: 'system', content: 'Ты — эксперт по созданию образовательного контента для начальной школы. Отвечай ТОЛЬКО валидным JSON без markdown обёрток.' },
          { role: 'user', content: prompt }
        ],
        temperature: 0.7,
        max_tokens: 3000
      });
      
      let content = completion.choices[0]?.message?.content || '';
      content = content.replace(/^```json?\s*/i, '').replace(/\s*```\s*$/i, '');
      return JSON.parse(content);
    } catch (e) {
      console.error('  ERROR:', e.message?.substring(0, 80));
      return null;
    }
  }

  const subjects = {
    math: 'Математика',
    russian: 'Русский язык',
    literature: 'Литературное чтение',
    english: 'Английский язык',
    art: 'Изобразительное искусство',
    music: 'Музыка',
    pe: 'Физическая культура',
    tech: 'Технология',
    projects: 'Проектная деятельность',
    world: 'Окружающий мир',
  };

  let totalSuccess = 0;
  let totalFail = 0;

  for (const [key, title] of Object.entries(subjects)) {
    const filePath = DIR + '/' + key + '.json';
    const existingData = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    const lessons = existingData.lessons?.detailedTopics?.flatMap(t => t.lessons || []) || [];
    
    console.log(`\n=== ${title} (${lessons.length} lessons) ===`);
    
    for (let i = 0; i < lessons.length; i++) {
      const lesson = lessons[i];
      const num = i + 1;
      process.stdout.write(`  L${num}: ${lesson.title.substring(0, 45)}... `);
      
      const content = await generateLessonContent(title, lesson.title, num, lessons.length);
      
      if (content) {
        lesson.description = content.description;
        lesson.keyPoints = content.keyPoints;
        lesson.examples = content.examples;
        lesson.facts = content.facts;
        lesson.tests = content.tests;
        totalSuccess++;
        process.stdout.write('OK ✓\n');
      } else {
        totalFail++;
        process.stdout.write('FAIL ✗\n');
      }
      
      await new Promise(r => setTimeout(r, 300));
    }
    
    fs.writeFileSync(filePath, JSON.stringify(existingData, null, 2));
    console.log(`  Saved ${key}.json`);
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
