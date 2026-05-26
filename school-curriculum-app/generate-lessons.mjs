import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
import path from 'path';

const GRADE = parseInt(process.argv[2] || '5');
const START = parseInt(process.argv[3] || '1');
const COUNT = parseInt(process.argv[4] || '10');

const FILE_PATH = path.join(process.cwd(), 'public/data/grades', String(GRADE), 'biology.json');

// Full Пасечник В.В. curriculum for Grade 5 Biology (Введение в биологию) — 24 параграфа
const PASECHNIK_CURRICULUM = [
  // Глава 1: Биология — наука о живой природе (§1-5)
  { topic: "Биология — наука о живой природе", lessons: [
    { num: 1, title: "Биология — наука о живой природе", desc: "Биология как наука о живой природе. Предмет биологии, её связь с другими науками. Разделы биологии: ботаника, зоология, микробиология, генетика, экология, физиология. Значение биологии для понимания окружающего мира и практической деятельности человека." },
    { num: 2, title: "Методы исследования в биологии", desc: "Научные методы познания: наблюдение, эксперимент, измерение, сравнение, моделирование. Правила проведения наблюдений и экспериментов. Лабораторное оборудование. Гипотеза как научное предположение." },
    { num: 3, title: "Разнообразие живой природы. Царства живых организмов. Отличительные признаки живого", desc: "Основные свойства живых организмов: обмен веществ, рост, развитие, размножение, раздражимость, наследственность, изменчивость, саморегуляция. Царства живой природы: Бактерии, Грибы, Растения, Животные. Отличие живых организмов от неживых тел." },
    { num: 4, title: "Среды обитания организмов", desc: "Наземно-воздушная, водная, почвенная среды обитания. Организм как среда обитания. Приспособленность организмов к среде обитания. Влияние среды на организмы." },
    { num: 5, title: "Экологические факторы и их влияние на живые организмы", desc: "Факторы неживой природы (абиотические), факторы живой природы (биотические), антропогенные факторы. Влияние света, температуры, влажности на организмы. Взаимодействие факторов. Приспособления организмов к действию экологических факторов." },
  ]},
  // Глава 2: Клетка — основа строения и жизнедеятельности организмов (§6-10)
  { topic: "Клетка — основа строения и жизнедеятельности организмов", lessons: [
    { num: 6, title: "Устройство увеличительных приборов", desc: "Устройство лупы и микроскопа. Правила работы с микроскопом. Приготовление микропрепарата. История создания микроскопа: Р. Гук, А. Левенгук. Значение увеличительных приборов для изучения клеточного строения." },
    { num: 7, title: "Строение клетки", desc: "Клетка как единица строения живого организма. Основные части клетки: оболочка (клеточная стенка), цитоплазма, ядро. Особенности строения растительной и животной клеток. Вакуоли, пластиды (хлоропласты, хромопласты, лейкопласты), клеточная стенка. Хромосомы." },
    { num: 8, title: "Химический состав клетки", desc: "Неорганические вещества клетки: вода и минеральные соли. Органические вещества: белки, жиры, углеводы, нуклеиновые кислоты (ДНК, РНК). Роль воды в клетке. Значение органических веществ для жизнедеятельности клетки." },
    { num: 9, title: "Жизнедеятельность клетки, её деление и рост", desc: "Обмен веществ и превращение энергии в клетке. Дыхание клетки. Питание клетки. Рост и развитие клетки. Деление клетки — основа роста и размножения организмов. Этапы деления клетки." },
    { num: 10, title: "Ткани", desc: "Понятие о ткани. Типы тканей растений: покровная, основная (фотосинтезирующая, запасающая), проводящая, механическая, образовательная. Типы тканей животных: эпителиальная, соединительная, мышечная, нервная. Строение и функции тканей." },
  ]},
  // Глава 3: Бактерии. Грибы. Растения (§11-24)
  { topic: "Бактерии", lessons: [
    { num: 11, title: "Строение и жизнедеятельность бактерий", desc: "Строение бактериальной клетки: клеточная стенка, цитоплазма, кольцевая ДНК, жгутики, капсула. Формы бактерий: кокки, бациллы, вибрионы, спириллы. Питание и дыхание бактерий. Спорообразование. Размножение бактерий." },
    { num: 12, title: "Роль бактерий в природе и жизни человека", desc: "Бактерии-разрушители (редуценты), бактерии-паразиты, бактерии-симбионты. Бактерии в пищевой промышленности (молочнокислые бактерии). Болезнетворные бактерии и меры профилактики бактериальных заболеваний. Антибиотики. Клубеньковые бактерии." },
  ]},
  { topic: "Грибы", lessons: [
    { num: 13, title: "Общая характеристика грибов", desc: "Признаки грибов: гетеротрофное питание, наличие хитина в клеточной стенке, запасной гликоген, неограниченный рост. Строение шляпочного гриба: грибница (мицелий) и плодовое тело. Питание грибов: сапротрофы и паразиты. Размножение грибов спорами." },
    { num: 14, title: "Шляпочные грибы", desc: "Строение шляпочного гриба: шляпка и ножка. Трубчатые грибы (белый гриб, подберёзовик, подосиновик, маслёнок). Пластинчатые грибы (сыроежка, опёнок, рыжик, шампиньон). Съедобные и ядовитые грибы (бледная поганка, мухомор). Правила сбора грибов." },
    { num: 15, title: "Плесневые грибы и дрожжи", desc: "Плесневые грибы: мукор (белая плесень) и пеницилл (зелёная плесень). Строение мукора и пеницилла. Пеницилл — источник антибиотика пенициллина. Дрожжи — одноклеточные грибы. Брожение. Использование дрожжей в хлебопечении и пивоварении." },
    { num: 16, title: "Грибы-паразиты", desc: "Грибы-паразиты растений: трутовик, головня, спорынья. Вред, причиняемый грибами-паразитами сельскому хозяйству. Меры борьбы с грибами-паразитами. Грибы-паразиты животных и человека (лишай, стригущий лишай). Значение изучения грибов-паразитов." },
  ]},
  { topic: "Растения", lessons: [
    { num: 17, title: "Разнообразие, распространение, значение растений", desc: "Признаки царства Растения: автотрофное питание (фотосинтез), клеточная стенка из целлюлозы, пластиды, вакуоли. Ботаника — наука о растениях. Жизненные формы растений: деревья, кустарники, травы. Роль растений в природе и жизни человека. Охрана растений." },
    { num: 18, title: "Водоросли", desc: "Общая характеристика водорослей: отсутствие тканей и органов. Одноклеточные водоросли (хлорелла, хламидомонада). Многоклеточные водоросли (улотрикс, спирогира, ламинария). Бурые, красные и зелёные водоросли. Строение, размножение и значение водорослей в природе и жизни человека." },
    { num: 19, title: "Лишайники", desc: "Лишайник — симбиоз гриба и водоросли (или цианобактерии). Строение лишайника: грибница и клетки водоросли. Типы лишайников: накипные, листоватые, кустистые. Роль лишайников в природе: пионеры растительности, индикаторы чистоты воздуха. Значение лишайников." },
    { num: 20, title: "Мхи", desc: "Общая характеристика мхов: отсутствие корней, наличие стебля и листьев. Строение мха кукушкин лён: стебель, листья, ризоиды. Сфагнум — торфяной мох. Размножение мхов (спорами). Жизненный цикл мхов. Значение мхов в природе и образовании торфа." },
    { num: 21, title: "Плауны. Хвощи. Папоротники", desc: "Высшие споровые растения. Строение папоротника: корневище, листья (вайи), спорангии. Хвощи — строение и местообитание. Плауны — строение и местообитание. Происхождение каменного угля из древовидных папоротников. Значение высших споровых растений." },
    { num: 22, title: "Голосеменные", desc: "Общая характеристика голосеменных: семенное размножение, отсутствие плодов, наличие шишек. Строение хвои и шишек сосны, ели. Разнообразие голосеменных: лиственница, можжевельник, секвойя. Значение голосеменных в природе и хозяйстве. Охрана хвойных лесов." },
    { num: 23, title: "Покрытосеменные, или Цветковые", desc: "Общая характеристика покрытосеменных: наличие цветка и плода. Класс Двудольные: особенности строения семени (две семядоли), стержневая корневая система, сетчатое жилкование листьев. Класс Однодольные: одна семядоля, мочковатая корневая система, параллельное жилкование. Многообразие и значение цветковых растений." },
    { num: 24, title: "Происхождение растений. Основные этапы развития растительного мира", desc: "Историческое развитие растительного мира от древнейших водорослей до покрытосеменных. Выход растений на сушу. Появление мхов, папоротников, голосеменных, покрытосеменных. Эволюция растений — постепенное усложнение организации. Роль растений в формировании биосферы." },
  ]},
];

async function generateLesson(zai, lessonInfo, grade) {
  const prompt = `Ты — опытный преподаватель биологии в российской школе. Создай ПОЛНЫЙ подробный урок биологии для ${grade} класса по учебнику Пасечника В.В. «Биология. Введение в биологию. 5 класс».

УРОК: ${lessonInfo.title}
ОПИСАНИЕ: ${lessonInfo.desc}

ТРЕБОВАНИЯ:
1. Content — ПОДРОБНЫЙ текст урока (минимум 2500 символов), написанный в Markdown, с заголовками ##, жирным шрифтом **, списками. Должен быть подробным и развёрнутым, как в учебнике.
2. Description — краткое описание урока (1-2 предложения)
3. Tasks — 4-5 учебных заданий по теме урока
4. Examples — 3 конкретных примера с пояснениями
5. Facts — 3-4 интересных факта
6. KeyPoints — 3-4 ключевых положения
7. Theory — то же содержимое что и Content (полный текст урока)

Ответь ТОЛЬКО валидным JSON, без markdown:
{
  "title": "Урок ${lessonInfo.num}: ${lessonInfo.title}",
  "description": "...",
  "tasks": ["...", "...", "...", "..."],
  "examples": ["...", "...", "..."],
  "facts": ["...", "...", "..."],
  "keyPoints": ["...", "...", "..."],
  "content": "## Заголовок\n\nПодробный текст урока...",
  "theory": "## Заголовок\n\nПодробный текст урока..."
}`;

  try {
    const completion = await zai.chat.completions.create({
      messages: [
        { role: 'system', content: 'Ты — опытный преподаватель биологии, автор подробных учебных материалов. Отвечай ТОЛЬКО валидным JSON без markdown-обёрток. Content и Theory должны содержать минимум 2500 символов.' },
        { role: 'user', content: prompt }
      ],
      temperature: 0.7,
      max_tokens: 4000,
    });

    let responseText = completion.choices[0]?.message?.content || '';
    responseText = responseText.replace(/```json\n?/g, '').replace(/```\n?/g, '').trim();

    const lesson = JSON.parse(responseText);

    // Validate minimum content
    if (!lesson.content || lesson.content.length < 1500) {
      console.error(`  Lesson ${lessonInfo.num}: content too short (${lesson.content?.length || 0} chars). Retrying...`);
      return null;
    }
    if (!lesson.theory || lesson.theory.length < 1500) {
      lesson.theory = lesson.content;
    }

    // Add image path
    lesson.image = `/school-curriculum-app/images/lessons/grade${grade}/biology/lesson${lessonInfo.num}.svg`;

    // Ensure title format
    lesson.title = `Урок ${lessonInfo.num}: ${lessonInfo.title}`;

    return lesson;
  } catch (error) {
    console.error(`  Lesson ${lessonInfo.num}: Error: ${error.message}`);
    return null;
  }
}

async function main() {
  console.log(`\n=== Generating Grade ${GRADE} Biology lessons (Пасечник В.В.), Lessons ${START}-${START + COUNT - 1} ===\n`);

  const zai = await ZAI.create();

  // Collect all lessons from curriculum
  const allLessons = [];
  for (const section of PASECHNIK_CURRICULUM) {
    for (const lesson of section.lessons) {
      allLessons.push({ ...lesson, topic: section.topic });
    }
  }

  console.log(`Total curriculum lessons: ${allLessons.length}`);

  // Generate lessons for the specified range
  const generatedLessons = [];
  const startIdx = START - 1;
  const endIdx = Math.min(startIdx + COUNT, allLessons.length);

  for (let i = startIdx; i < endIdx; i++) {
    const lessonInfo = allLessons[i];
    console.log(`Generating Lesson ${lessonInfo.num}: ${lessonInfo.title}...`);

    let lesson = null;
    let retries = 0;
    while (!lesson && retries < 5) {
      lesson = await generateLesson(zai, lessonInfo, GRADE);
      if (!lesson) {
        retries++;
        const waitTime = retries * 10000;
        console.log(`  Retry ${retries}... (waiting ${waitTime/1000}s)`);
        await new Promise(resolve => setTimeout(resolve, waitTime));
      }
    }

    if (lesson) {
      generatedLessons.push({ topic: lessonInfo.topic, lesson });
      console.log(`  ✓ Generated (${lesson.content.length} chars)`);
    } else {
      console.error(`  ✗ FAILED after 3 retries`);
    }

    await new Promise(resolve => setTimeout(resolve, 5000));
  }

  console.log(`\nGenerated ${generatedLessons.length} lessons`);

  // Now update the biology.json
  if (START === 1) {
    // Starting fresh - create new structure
    // Group lessons by topic
    const topicMap = new Map();
    for (const { topic, lesson } of generatedLessons) {
      if (!topicMap.has(topic)) topicMap.set(topic, []);
      topicMap.get(topic).push(lesson);
    }

    const detailedTopics = [];
    for (const [topic, lessons] of topicMap) {
      detailedTopics.push({ topic, lessons });
    }

    // If this is the first batch, read existing file for structure, then replace lessons
    let data;
    try {
      data = JSON.parse(fs.readFileSync(FILE_PATH, 'utf-8'));
    } catch {
      data = {};
    }

    data.lessons = {
      title: 'Биология',
      icon: 'Leaf',
      color: 'text-green-400',
      topics: [...new Set(generatedLessons.map(g => g.topic))],
      detailedTopics: detailedTopics
    };
    // Keep existing games if any
    if (!data.games) data.games = [];

    fs.writeFileSync(FILE_PATH, JSON.stringify(data, null, 2), 'utf-8');
    console.log(`\n✓ Created new structure with ${generatedLessons.length} lessons`);
  } else {
    // Append to existing structure
    const data = JSON.parse(fs.readFileSync(FILE_PATH, 'utf-8'));

    // Add lessons to appropriate topics
    for (const { topic, lesson } of generatedLessons) {
      let topicObj = data.lessons.detailedTopics.find(t => t.topic === topic);
      if (!topicObj) {
        topicObj = { topic, lessons: [] };
        data.lessons.detailedTopics.push(topicObj);
        data.lessons.topics.push(topic);
      }
      topicObj.lessons.push(lesson);
    }

    fs.writeFileSync(FILE_PATH, JSON.stringify(data, null, 2), 'utf-8');
    console.log(`\n✓ Updated with ${generatedLessons.length} additional lessons`);
  }
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
