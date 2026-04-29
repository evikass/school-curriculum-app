import fs from 'fs';
import path from 'path';

const GRADES_DIR = '/home/z/my-project/school-curriculum-app/src/data/grades';

const FILLER_WORDS = [
  'Никто не знает', 'Не знаю', 'Не указано', 'Нет ответа',
  'Неверно', 'Не подходит', 'Другой ответ', 'другой ответ',
  'Другой', 'другой', 'Это секрет', 'Все знают',
  'Затрудняюсь', 'Без понятия', 'Не определить', 'Невозможно',
  'Неясно', 'Не понятно', 'Не могу сказать', 'Нет верного',
  'нет верного', 'Все выше', 'все выше', 'Ничего', 'ничего',
  'Не имеет значения', 'Не важно', 'Не определено',
];

function isFiller(text) {
  text = text.trim();
  if (text === '-') return true;
  for (const fw of FILLER_WORDS) {
    if (fw.toLowerCase() === text.toLowerCase()) return true;
    if (text.toLowerCase().startsWith(fw.toLowerCase())) {
      const rest = text.slice(fw.length).trim();
      if (rest === '' || /^\d+$/.test(rest)) return true;
    }
  }
  return false;
}

function extractString(content, key) {
  const searchKey = key + ':';
  const idx = content.indexOf(searchKey);
  if (idx === -1) return null;
  const afterKey = content.slice(idx + searchKey.length).trimStart();
  // Support both double and single quotes
  const quoteChar = afterKey[0];
  if (quoteChar !== '"' && quoteChar !== "'") return null;
  let end = 1;
  while (end < afterKey.length) {
    if (afterKey[end] === '\\' && end + 1 < afterKey.length) { end += 2; continue; }
    if (afterKey[end] === quoteChar) break;
    end++;
  }
  return afterKey.slice(1, end).replace(/\\"/g, '"').replace(/\\'/g, "'");
}

function extractOptions(content, startPos) {
  const idx = content.indexOf('options:', startPos);
  if (idx === -1) return null;
  const afterOptions = content.slice(idx + 8).trimStart();
  if (!afterOptions.startsWith('[')) return null;
  let depth = 0, i = 0;
  for (; i < afterOptions.length; i++) {
    if (afterOptions[i] === '[') depth++;
    if (afterOptions[i] === ']') { depth--; if (depth === 0) break; }
  }
  const arrStr = afterOptions.slice(0, i + 1);
  const options = [];
  const optPattern = /"((?:[^"\\]|\\.)*)"/g;
  let m;
  while ((m = optPattern.exec(arrStr)) !== null) {
    options.push(m[1].replace(/\\"/g, '"'));
  }
  return { options, arrStr };
}

function parseQuizzes(content) {
  const quizzes = [];
  const pattern = /type:\s*'quiz'/g;
  let match;
  while ((match = pattern.exec(content)) !== null) {
    const quizStart = match.index;
    let braceStart = content.lastIndexOf('{', quizStart);
    if (braceStart === -1 || content.slice(braceStart, quizStart).includes('}')) continue;
    
    const question = extractString(content.slice(braceStart), 'question');
    if (!question) continue;
    
    const optResult = extractOptions(content, braceStart);
    if (!optResult) continue;
    
    const correctAnswer = extractString(content.slice(braceStart), 'correctAnswer');
    if (!correctAnswer) continue;
    
    let depth = 0, braceEnd = braceStart;
    for (let i = braceStart; i < content.length; i++) {
      if (content[i] === '{') depth++;
      if (content[i] === '}') { depth--; if (depth === 0) { braceEnd = i + 1; break; } }
    }
    
    const fullMatch = content.slice(braceStart, braceEnd);
    const fillerIdx = [];
    for (let i = 0; i < optResult.options.length; i++) {
      if (isFiller(optResult.options[i])) fillerIdx.push(i);
    }
    
    if (fillerIdx.length > 0) {
      quizzes.push({
        start: braceStart,
        end: braceEnd,
        fullMatch,
        question,
        options: optResult.options,
        arrStr: optResult.arrStr,
        correct: correctAnswer,
        fillerIdx,
      });
    }
  }
  return quizzes;
}

// Subject-specific distractor pools for generating replacements
const SUBJECT_DISTRACTORS = {
  math: {
    numbers: ['12', '15', '18', '20', '24', '28', '30', '36', '42', '48', '54', '60', '72', '84', '100', '120'],
    fractions: ['1/2', '1/3', '2/3', '1/4', '3/4', '1/5', '2/5', '3/5', '1/6', '5/6', '1/8', '3/8'],
    operations: ['Умножение', 'Деление', 'Сложение', 'Вычитание', 'Возведение в степень'],
    terms: ['Числитель', 'Знаменатель', 'Делимое', 'Делитель', 'Частное', 'Произведение', 'Сумма', 'Разность'],
    properties: ['Переместительное', 'Сочетательное', 'Распределительное', 'Коммутативное'],
  },
  russian: {
    parts: ['Существительное', 'Прилагательное', 'Глагол', 'Наречие', 'Местоимение', 'Союз', 'Предлог', 'Частица', 'Междометие', 'Причастие', 'Деепричастие', 'Числительное'],
    cases: ['Именительный', 'Родительный', 'Дательный', 'Винительный', 'Творительный', 'Предложный'],
    genders: ['Мужской', 'Женский', 'Средний'],
    numbers: ['Единственное', 'Множественное'],
    tenses: ['Прошедшее', 'Настоящее', 'Будущее'],
    types: ['Простое', 'Сложное', 'Сложноподчинённое', 'Сложносочинённое', 'Бессоюзное'],
  },
  literature: {
    genres: ['Роман', 'Повесть', 'Рассказ', 'Сказка', 'Поэма', 'Басня', 'Ода', 'Элегия', 'Баллада', 'Комедия', 'Трагедия', 'Драма'],
    elements: ['Завязка', 'Кульминация', 'Развязка', 'Экспозиция', 'Пролог', 'Эпилог'],
    characters: ['Герой', 'Антагонист', 'Лирический герой', 'Рассказчик', 'Повествователь'],
    terms: ['Метафора', 'Эпитет', 'Сравнение', 'Олицетворение', 'Гипербола', 'Аллегория', 'Ирония', 'Антитеза'],
  },
  history: {
    periods: ['Древний мир', 'Средние века', 'Новое время', 'Новейшее время', 'Первобытный мир'],
    events: ['Куликовская битва', 'Бородинское сражение', 'Великая Отечественная война', 'Отечественная война 1812 года'],
    terms: ['Монархия', 'Республика', 'Демократия', 'Империя', 'Феодализм', 'Крепостное право', 'Реформа'],
    figures: ['Пётр I', 'Екатерина II', 'Александр Невский', 'Дмитрий Донской', 'Иван Грозный'],
  },
  geography: {
    objects: ['Река', 'Озеро', 'Гора', 'Равнина', 'Море', 'Океан', 'Пролив', 'Залив', 'Полуостров', 'Остров', 'Материк', 'Вулкан'],
    continents: ['Евразия', 'Африка', 'Северная Америка', 'Южная Америка', 'Австралия', 'Антарктида'],
    oceans: ['Тихий', 'Атлантический', 'Индийский', 'Северный Ледовитый'],
    climate: ['Тропический', 'Субтропический', 'Умеренный', 'Субарктический', 'Арктический', 'Экваториальный'],
    terms: ['Широта', 'Долгота', 'Меридиан', 'Параллель', 'Экватор', 'Масштаб', 'Абсолютная высота'],
  },
  biology: {
    kingdoms: ['Бактерии', 'Грибы', 'Растения', 'Животные', 'Протисты'],
    organs: ['Корень', 'Стебель', 'Лист', 'Цветок', 'Плод', 'Семя'],
    systems: ['Пищеварительная', 'Дыхательная', 'Кровеносная', 'Нервная', 'Выделительная', 'Половая'],
    terms: ['Фотосинтез', 'Дыхание', 'Питание', 'Размножение', 'Рост', 'Развитие', 'Эволюция'],
    types: ['Прокариоты', 'Эукариоты', 'Автотрофы', 'Гетеротрофы'],
  },
  physics: {
    quantities: ['Масса', 'Сила', 'Скорость', 'Ускорение', 'Плотность', 'Давление', 'Работа', 'Мощность', 'Энергия'],
    units: ['Ньютон', 'Паскаль', 'Джоуль', 'Ватт', 'Килограмм', 'Метр', 'Секунда'],
    laws: ['Закон Гука', 'Закон Ома', 'Закон Ньютона', 'Закон Паскаля', 'Закон Архимеда'],
    phenomena: ['Диффузия', 'Инерция', 'Трение', 'Деформация', 'Нагревание', 'Охлаждение'],
  },
  chemistry: {
    elements: ['Водород', 'Кислород', 'Азот', 'Углерод', 'Железо', 'Медь', 'Сера', 'Фосфор', 'Кальций', 'Натрий'],
    types: ['Оксид', 'Кислота', 'Основание', 'Соль', 'Металл', 'Неметалл'],
    reactions: ['Соединение', 'Разложение', 'Замещение', 'Обмен'],
    terms: ['Атом', 'Молекула', 'Валентность', 'Степень окисления', 'Молярная масса'],
  },
  english: {
    tenses: ['Present Simple', 'Past Simple', 'Future Simple', 'Present Continuous', 'Past Continuous'],
    parts: ['Noun', 'Verb', 'Adjective', 'Adverb', 'Pronoun', 'Preposition', 'Conjunction'],
    topics: ['Weather', 'Food', 'Travel', 'School', 'Sport', 'Music', 'Family', 'Hobby'],
    grammar: ['Article', 'Modal verb', 'Phrasal verb', 'Gerund', 'Infinitive', 'Participle'],
  },
  informatics: {
    terms: ['Алгоритм', 'Программа', 'Файл', 'Папка', 'Система', 'Сеть', 'Браузер', 'Сервер'],
    types: ['Целый', 'Вещественный', 'Строковый', 'Логический', 'Символьный'],
    structures: ['Массив', 'Список', 'Строка', 'Стек', 'Очередь', 'Дерево'],
    concepts: ['Ветвление', 'Цикл', 'Условие', 'Функция', 'Переменная', 'Константа'],
  },
  coding: {
    languages: ['Python', 'JavaScript', 'Java', 'C++', 'Scratch', 'HTML', 'CSS'],
    concepts: ['Переменная', 'Функция', 'Цикл', 'Условие', 'Массив', 'Класс', 'Объект'],
    terms: ['Синтаксис', 'Алгоритм', 'Отладка', 'Компиляция', 'Интерпретация', 'Итерация'],
  },
  ecology: {
    terms: ['Экосистема', 'Биосфера', 'Популяция', 'Сообщество', 'Среда обитания', 'Пищевая цепь'],
    problems: ['Загрязнение', 'Вырубка лесов', 'Парниковый эффект', 'Кислотные дожди', 'Опустынивание'],
    concepts: ['Биоразнообразие', 'Устойчивое развитие', 'Ресурсосбережение', 'Переработка', 'Охрана природы'],
  },
  social: {
    terms: ['Общество', 'Государство', 'Закон', 'Право', 'Конституция', 'Гражданин', 'Демократия'],
    concepts: ['Социальная норма', 'Мораль', 'Этика', 'Справедливость', 'Равенство', 'Свобода'],
  },
  art: {
    types: ['Живопись', 'Графика', 'Скульптура', 'Архитектура', 'Декоративно-прикладное', 'Фотоискусство'],
    styles: ['Реализм', 'Импрессионизм', 'Кубизм', 'Сюрреализм', 'Авангард', 'Классицизм'],
    elements: ['Цвет', 'Линия', 'Форма', 'Композиция', 'Ритм', 'Пропорция', 'Контраст'],
    terms: ['Натюрморт', 'Пейзаж', 'Портрет', 'Сюжет', 'Колорит', 'Фактура'],
  },
  music: {
    genres: ['Классика', 'Джаз', 'Рок', 'Поп', 'Фолк', 'Блюз', 'Этническая'],
    elements: ['Мелодия', 'Ритм', 'Гармония', 'Темп', 'Динамика', 'Тональность', 'Лад'],
    instruments: ['Фортепиано', 'Скрипка', 'Гитара', 'Флейта', 'Барабан', 'Труба'],
    terms: ['Хор', 'Оркестр', 'Симфония', 'Опера', 'Балет', 'Ария', 'Кантата'],
  },
  pe: {
    sports: ['Футбол', 'Баскетбол', 'Волейбол', 'Теннис', 'Плавание', 'Лёгкая атлетика', 'Гимнастика'],
    terms: ['Разминка', 'Тренировка', 'Снаряд', 'Эстафета', 'Соревнование', 'Рекорд'],
    concepts: ['Выносливость', 'Сила', 'Ловкость', 'Гибкость', 'Быстрота', 'Координация'],
  },
  safety: {
    hazards: ['Пожар', 'Наводнение', 'Землетрясение', 'Ураган', 'Техногенная авария'],
    terms: ['Эвакуация', 'Укрытие', 'Аптечка', 'Противогаз', 'Респиратор', 'Огнетушитель'],
    concepts: ['Предупреждение', 'Защита', 'Спасение', 'Первая помощь', 'Травма', 'Ожог'],
  },
  tech: {
    materials: ['Дерево', 'Металл', 'Пластик', 'Стекло', 'Керамика', 'Ткань'],
    tools: ['Молоток', 'Пила', 'Отвёртка', 'Плоскогубцы', 'Ножовка', 'Напильник'],
    terms: ['Чертёж', 'Эскиз', 'Разметка', 'Шаблон', 'Деталь', 'Узел', 'Механизм'],
  },
  crafts: {
    types: ['Вязание', 'Вышивание', 'Лепка', 'Аппликация', 'Оригами', 'Плетение'],
    materials: ['Пряжа', 'Ткань', 'Бумага', 'Картон', 'Пластилин', 'Бисер'],
    terms: ['Узор', 'Орнамент', 'Композиция', 'Цветовая гамма', 'Декор', 'Стилизация'],
  },
  robotics: {
    components: ['Датчик', 'Мотор', 'Контроллер', 'Сервопривод', 'Шасси', 'Аккумулятор'],
    concepts: ['Программирование', 'Автоматизация', 'Алгоритм', 'Цикл', 'Условие', 'Переменная'],
    types: ['Манипулятор', 'Дрон', 'Робот-пылесос', 'Промышленный робот', 'Гуманоидный робот'],
  },
  algebra: {
    expressions: ['Многочлен', 'Одночлен', 'Уравнение', 'Неравенство', 'Функция', 'Тождество'],
    terms: ['Коэффициент', 'Степень', 'Корень', 'Дискриминант', 'Аргумент', 'Область определения'],
    operations: ['Раскрытие скобок', 'Приведение подобных', 'Разложение на множители', 'Сокращение'],
  },
  geometry: {
    shapes: ['Треугольник', 'Прямоугольник', 'Квадрат', 'Круг', 'Ромб', 'Трапеция', 'Параллелограмм'],
    elements: ['Сторона', 'Угол', 'Вершина', 'Диагональ', 'Высота', 'Медиана', 'Биссектриса'],
    terms: ['Периметр', 'Площадь', 'Объём', 'Радиус', 'Диаметр', 'Хорда', 'Дуга'],
    types: ['Остроугольный', 'Прямоугольный', 'Тупоугольный', 'Равнобедренный', 'Равносторонний'],
  },
};

// Generic distractors for subjects not in the list
const GENERIC_DISTRACTORS = [
  'Вариант А', 'Вариант Б', 'Вариант В', 'Вариант Г',
  'Первый вариант', 'Второй вариант', 'Третий вариант',
];

function generateDistractor(question, existingOptions, correctAnswer, grade, subject) {
  // Try to use subject-specific distractors
  const subjectKey = subject.toLowerCase();
  const pool = SUBJECT_DISTRACTORS[subjectKey];
  
  if (pool) {
    // Collect all distractors from all categories in the pool
    const allDistractors = [];
    for (const category of Object.values(pool)) {
      allDistractors.push(...category);
    }
    
    // Shuffle and try to find a non-duplicate
    const shuffled = allDistractors.sort(() => Math.random() - 0.5);
    
    // Try to find one that's contextually relevant
    const questionLower = question.toLowerCase();
    
    // First try: find relevant category based on question content
    for (const [catName, catItems] of Object.entries(pool)) {
      // Check if any item from this category is already in options
      const hasCategoryItem = existingOptions.some(opt => 
        catItems.some(item => opt.toLowerCase().includes(item.toLowerCase()))
      );
      
      if (hasCategoryItem) {
        // This category is relevant - use items from it
        const relevant = catItems.filter(item => 
          !existingOptions.some(opt => opt.toLowerCase().trim() === item.toLowerCase().trim()) &&
          item.toLowerCase().trim() !== correctAnswer.toLowerCase().trim()
        );
        if (relevant.length > 0) {
          return relevant[Math.floor(Math.random() * relevant.length)];
        }
      }
    }
    
    // Second try: use any non-duplicate from the pool
    for (const d of shuffled) {
      if (!existingOptions.some(opt => opt.toLowerCase().trim() === d.toLowerCase().trim()) &&
          d.toLowerCase().trim() !== correctAnswer.toLowerCase().trim()) {
        return d;
      }
    }
  }
  
  // Fallback: generate number-based distractors if the answer seems numeric
  const numMatch = correctAnswer.match(/^[-]?\d+[\.,]?\d*$/);
  if (numMatch) {
    const num = parseFloat(correctAnswer.replace(',', '.'));
    const offsets = [-2, -1, 1, 2, -3, 3, 5, -5, 10, -10, 0.5, -0.5];
    for (const off of offsets.sort(() => Math.random() - 0.5)) {
      const newNum = num + off;
      const newStr = Number.isInteger(num) ? String(Math.round(newNum)) : newNum.toFixed(2);
      if (newStr !== correctAnswer && !existingOptions.some(opt => opt.trim() === newStr)) {
        return newStr;
      }
    }
  }
  
  // Fallback: generate subject-prefixed distractor
  const subjectNames = {
    math: 'математики', russian: 'русского языка', literature: 'литературы',
    history: 'истории', geography: 'географии', biology: 'биологии',
    physics: 'физики', chemistry: 'химии', english: 'английского языка',
    informatics: 'информатики', coding: 'программирования', ecology: 'экологии',
    social: 'обществознания', art: 'искусства', music: 'музыки',
    pe: 'физкультуры', safety: 'ОБЖ', tech: 'технологии',
    crafts: 'труда', robotics: 'робототехники', algebra: 'алгебры', geometry: 'геометрии',
  };
  const subjName = subjectNames[subjectKey] || subject;
  const prefixes = ['Основы', 'Элементы', 'Принципы', 'Правило', 'Закон', 'Свойство'];
  const prefix = prefixes[Math.floor(Math.random() * prefixes.length)];
  return `${prefix} ${subjName}`;
}

function fixFile(filepath, grade, subject) {
  let content = fs.readFileSync(filepath, 'utf-8');
  let quizzes = parseQuizzes(content);
  
  if (quizzes.length === 0) return 0;
  
  console.log(`    Found ${quizzes.length} quizzes with fillers`);
  const totalFillers = quizzes.reduce((s, q) => s + q.fillerIdx.length, 0);
  console.log(`    Total filler options: ${totalFillers}`);
  
  let replacementsMade = 0;
  
  for (const q of quizzes) {
    const newOptions = [...q.options];
    let changed = false;
    
    for (const idx of q.fillerIdx) {
      const replacement = generateDistractor(q.question, newOptions, q.correct, grade, subject);
      if (replacement) {
        newOptions[idx] = replacement;
        replacementsMade++;
        console.log(`    "${q.options[idx]}" -> "${replacement}"`);
        changed = true;
      } else {
        console.log(`    FAILED: "${q.options[idx]}"`);
      }
    }
    
    if (changed) {
      // Build new options string
      const newOptsStr = newOptions.map(o => `"${o}"`).join(', ');
      
      // Find the options array in the fullMatch and replace it
      const optsSectionMatch = q.fullMatch.match(/options:\s*\[(?:[^\[\]]|\[(?:[^\[\]])*\])*\]/s);
      if (optsSectionMatch) {
        const newOptsSection = `options: [${newOptsStr}]`;
        const newFullMatch = q.fullMatch.replace(optsSectionMatch[0], newOptsSection);
        content = content.slice(0, q.start) + newFullMatch + content.slice(q.end);
      }
    }
  }
  
  if (replacementsMade > 0) {
    fs.writeFileSync(filepath, content, 'utf-8');
  }
  
  return replacementsMade;
}

function main() {
  const grades = process.argv.length > 2 
    ? process.argv.slice(2).map(Number) 
    : [6, 7];
  
  let total = 0;
  
  for (const grade of grades) {
    const gradeDir = path.join(GRADES_DIR, String(grade));
    if (!fs.existsSync(gradeDir)) continue;
    
    console.log(`\n${'='.repeat(60)}`);
    console.log(`Grade ${grade}`);
    console.log('='.repeat(60));
    
    const subjects = fs.readdirSync(gradeDir).sort();
    for (const subject of subjects) {
      const fp = path.join(gradeDir, subject, 'index.ts');
      if (!fs.existsSync(fp)) continue;
      
      console.log(`\n  ${subject}:`);
      const count = fixFile(fp, grade, subject);
      total += count;
      console.log(`  -> ${count} replacements`);
    }
  }
  
  console.log(`\nTOTAL: ${total}`);
}

main();
