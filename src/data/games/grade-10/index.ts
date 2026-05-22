// Экспорт игр для 10 класса
import { GameLesson } from '../types'

export const tenthGradeGames: GameLesson[] = [
  {
    title: "Тригонометрия",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "sin²x + cos²x = ...", options: ["1", "4", "2", "3", "0"], correctAnswer: "1", hint: "Основное тригонометрическое тождество" },
      { type: 'quiz', question: "sin 30° = ?", options: ["0", "0.5", "1", "Не знаю", "Другой вариант"], correctAnswer: "0.5", hint: "sin 30° = 1/2" },
      { type: 'quiz', question: "cos 60° = ?", options: ["0", "0.5", "1", "Не знаю", "Другой вариант"], correctAnswer: "0.5", hint: "cos 60° = 1/2" },
      { type: 'quiz', question: "tg x = sin x / ...", options: ["глагол", "существительное", "наречие", "cos x", "прилагательное"], correctAnswer: "cos x", hint: "Тангенс = синус / косинус" },
      { type: 'quiz', question: "Чему равно 2 + 2?", options: ["3", "4", "5", "6", "8"], correctAnswer: "4", hint: "2 + 2 = 4" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тригонометрию! 📐" }
  },
  {
    title: "Производная",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Производная функции показывает:", options: ["Площадь под графиком", "Скорость изменения функции", "Максимум функции", "Не знаю", "Другой вариант"], correctAnswer: "Скорость изменения функции", hint: "f\'(x) - скорость изменения" },
      { type: 'quiz', question: "(x²)\' = ...x", options: ["2", "1", "0", "3", "4"], correctAnswer: "2", hint: "(xⁿ)\' = n·xⁿ⁻¹" },
      { type: 'quiz', question: "(3x + 5)\' = ?", options: ["3", "5", "3x", "Не знаю", "Другой вариант"], correctAnswer: "3", hint: "(ax + b)\' = a" },
      { type: 'quiz', question: "(x³)\' = ...x²", options: ["4", "5", "2", "1", "3"], correctAnswer: "3", hint: "(x³)\' = 3x²" },
      { type: 'quiz', question: "Чему равно 2 + 2?", options: ["3", "4", "5", "6", "8"], correctAnswer: "4", hint: "2 + 2 = 4" },
    ],
    reward: { stars: 3, message: "Супер! Ты понимаешь производные! 🔢" }
  },
  {
    title: "Показательные уравнения",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "2ˣ = 8. Чему равен x?", options: ["2", "3", "4", "Не знаю", "Другой вариант"], correctAnswer: "3", hint: "8 = 2³, значит x = 3" },
      { type: 'quiz', question: "3ˣ = 9, x = ...", options: ["3", "1", "4", "2", "0"], correctAnswer: "2", hint: "9 = 3²" },
      { type: 'quiz', question: "aˣ · aʸ = ?", options: ["aˣʸ", "aˣ⁺ʸ", "aˣ⁻ʸ", "Не знаю", "Другой вариант"], correctAnswer: "aˣ⁺ʸ", hint: "При умножении показатели складываются" },
      { type: 'quiz', question: "(aˣ)ʸ = ?", options: ["aˣʸ", "aˣ⁺ʸ", "aˣ⁻ʸ", "Не знаю", "Другой вариант"], correctAnswer: "aˣʸ", hint: "При возведении в степень - перемножаются" },
      { type: 'quiz', question: "Чему равно 2 + 2?", options: ["3", "4", "5", "6", "8"], correctAnswer: "4", hint: "2 + 2 = 4" },
    ],
    reward: { stars: 3, message: "Отлично! Ты решаешь показательные уравнения! 📊" }
  },
  {
    title: "Стереометрия",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Объём куба с ребром a:", options: ["a²", "a³", "6a²", "Не знаю", "Другой вариант"], correctAnswer: "a³", hint: "V = a³" },
      { type: 'quiz', question: "Объём параллелепипеда V = a·b·c. Если a=2, b=3, c=4, то V = ...", options: ["22", "19", "26", "14", "24"], correctAnswer: "24", hint: "2 × 3 × 4 = 24" },
      { type: 'quiz', question: "Площадь поверхности куба:", options: ["a³", "6a²", "a²", "Не знаю", "Другой вариант"], correctAnswer: "6a²", hint: "6 граней, каждая a²" },
      { type: 'quiz', question: "Объём шара:", options: ["πr²", "(4/3)πr³", "4πr²", "Не знаю", "Другой вариант"], correctAnswer: "(4/3)πr³", hint: "V = 4/3 π r³" },
      { type: 'quiz', question: "Сколько сторон у квадрата?", options: ["3", "4", "5", "6", "2"], correctAnswer: "4", hint: "Квадрат имеет 4 стороны" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь стереометрию! 📦" }
  },
  {
    title: "Многогранники",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Сколько граней у тетраэдра?", options: ["3", "4", "6", "1", "2"], correctAnswer: "4", hint: "Тетраэдр = 4 грани" },
      { type: 'quiz', question: "Сколько граней у куба?", options: ["4", "6", "8", "1", "2"], correctAnswer: "6", hint: "Куб = 6 граней" },
      { type: 'quiz', question: "Укажи правильные многогранники:", options: ["Тетраэдр", "Пирамида", "Цилиндр", "Не знаю", "Другой вариант"], correctAnswer: "Тетраэдр", hint: "Правильные многогранники имеют равные грани" },
      { type: 'quiz', question: "Призма - это многогранник с:", options: ["Треугольным основанием", "Двумя равными основаниями", "Одной вершиной", "Не знаю", "Другой вариант"], correctAnswer: "Двумя равными основаниями", hint: "Призма = два параллельных основания" },
      { type: 'quiz', question: "Сколько сторон у квадрата?", options: ["3", "4", "5", "6", "2"], correctAnswer: "4", hint: "Квадрат имеет 4 стороны" },
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь многогранники! 🔷" }
  },
  {
    title: "Стили речи",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Научный стиль используется в:", options: ["Художественных произведениях", "Научных статьях", "Разговорах", "Не знаю", "Другой вариант"], correctAnswer: "Научных статьях", hint: "Научный стиль - точность, логичность" },
      { type: 'quiz', question: "Укажи стили речи:", options: ["Научный", "Книжный", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Научный", hint: "Функциональные стили русского языка" },
      { type: 'quiz', question: "Официально-деловой стиль характеризуется:", options: ["Образностью", "Стандартизацией", "Эмоциональностью", "Не знаю", "Другой вариант"], correctAnswer: "Стандартизацией", hint: "Деловой стиль - документы, стандарты" },
      { type: 'quiz', question: "Художественный стиль использует:", options: ["Терминологию", "Образность и эмоции", "Штампы", "Не знаю", "Другой вариант"], correctAnswer: "Образность и эмоции", hint: "Художественный стиль - литература" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь стили речи! 📝" }
  },
  {
    title: "Чехов",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "А.П. Чехов родился в:", options: ["1860", "1850", "1870", "Не знаю", "Другой вариант"], correctAnswer: "1860", hint: "1860 год, Таганрог" },
      { type: 'quiz', question: "Укажи произведения Чехова:", options: ["Вишнёвый сад", "На дне", "Ревизор", "Не знаю", "Другой вариант"], correctAnswer: "Вишнёвый сад", hint: "Чехов - мастер рассказа и драматургии" },
      { type: 'quiz', question: "\"Вишнёвый сад\" - это:", options: ["Роман", "Пьеса", "Рассказ", "Не знаю", "Другой вариант"], correctAnswer: "Пьеса", hint: "Пьеса о смене эпох" },
      { type: 'quiz', question: "Чехов - профессия:", options: ["Учитель", "Врач", "Юрист", "Не знаю", "Другой вариант"], correctAnswer: "Врач", hint: "Чехов был врачом и писателем" },
      { type: 'quiz', question: "Что такое сказка?", options: ["Научная статья", "Стихотворение", "Выдуманная история", "Учебник", "Энциклопедия"], correctAnswer: "Выдуманная история", hint: "Сказка - вымышленный рассказ" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь Чехова! 📖" }
  },
  {
    title: "Бунин и Куприн",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "И.А. Бунин - лауреат Нобелевской премии по литературе:", options: ["Да", "Нет", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Да", hint: "Первый русский нобелевский лауреат по литературе" },
      { type: 'quiz', question: "Укажи произведения Бунина:", options: ["Тёмные аллеи", "Гранатовый браслет", "Поединок", "Не знаю", "Другой вариант"], correctAnswer: "Тёмные аллеи", hint: "Бунин - мастер лирической прозы" },
      { type: 'quiz', question: "\"Гранатовый браслет\" - автор:", options: ["Бунин", "Куприн", "Чехов", "Пушкин", "Лермонтов"], correctAnswer: "Куприн", hint: "Куприн - автор повести о любви" },
      { type: 'quiz', question: "\"Поединок\" - произведение о:", options: ["Любви", "Армейской жизни", "Революции", "Не знаю", "Другой вариант"], correctAnswer: "Армейской жизни", hint: "Куприн описал армейские будни" },
      { type: 'quiz', question: "Что такое сказка?", options: ["Научная статья", "Стихотворение", "Выдуманная история", "Учебник", "Энциклопедия"], correctAnswer: "Выдуманная история", hint: "Сказка - вымышленный рассказ" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь русскую литературу! 📚" }
  },
  {
    title: "Вторая мировая война",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Когда началась Вторая мировая война?", options: ["1939", "1941", "1945", "Не знаю", "Другой вариант"], correctAnswer: "1939", hint: "1 сентября 1939 - нападение на Польшу" },
      { type: 'quiz', question: "Когда началась Великая Отечественная война?", options: ["22 июня 1941", "1 сентября 1939", "9 мая 1945", "Не знаю", "Другой вариант"], correctAnswer: "22 июня 1941", hint: "Нападение Германии на СССР" },
      { type: 'quiz', question: "Укажи битвы Великой Отечественной:", options: ["Сталинградская", "Бородинская", "Невская", "Не знаю", "Другой вариант"], correctAnswer: "Сталинградская", hint: "Крупнейшие сражения 1941-1945" },
      { type: 'quiz', question: "Когда закончилась Великая Отечественная война?", options: ["8 мая 1945", "9 мая 1945", "2 сентября 1945", "Не знаю", "Другой вариант"], correctAnswer: "9 мая 1945", hint: "День Победы - 9 мая" },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь историю! ⚔️" }
  },
  {
    title: "Механика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Второй закон Ньютона:", options: ["F = ma", "F = mv", "F = m/a", "Не знаю", "Другой вариант"], correctAnswer: "F = ma", hint: "Сила = масса × ускорение" },
      { type: 'quiz', question: "Если m = 2 кг, a = 3 м/с², то F = ... Н", options: ["7", "6", "5", "8", "4"], correctAnswer: "6", hint: "F = 2 × 3 = 6" },
      { type: 'quiz', question: "Закон всемирного тяготения:", options: ["F = Gm₁m₂/r²", "F = Gm₁m₂/r", "F = Gm₁+m₂/r", "Не знаю", "Другой вариант"], correctAnswer: "F = Gm₁m₂/r²", hint: "Сила обратно пропорциональна квадрату расстояния" },
      { type: 'quiz', question: "Импульс тела:", options: ["p = m/v", "p = mv", "p = F·t", "Не знаю", "Другой вариант"], correctAnswer: "p = mv", hint: "Импульс = масса × скорость" },
      { type: 'quiz', question: "Что измеряется в метрах?", options: ["Время", "Масса", "Длина", "Температура", "Скорость"], correctAnswer: "Длина", hint: "Метр - единица длины" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь механику! ⚛️" }
  },
  {
    title: "Органическая химия",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: "Формула метана:", options: ["CH₄", "C₂H₄", "C₂H₆", "Не знаю", "Другой вариант"], correctAnswer: "CH₄", hint: "Метан - простейший алкан" },
      { type: 'quiz', question: "Алканы имеют общую формулу:", options: ["CₙH₂ₙ₊₂", "CₙH₂ₙ", "CₙH₂ₙ₋₂", "Не знаю", "Другой вариант"], correctAnswer: "CₙH₂ₙ₊₂", hint: "Алканы - предельные углеводороды" },
      { type: 'quiz', question: "Укажи алканы:", options: ["Метан", "Этен", "Этин", "Не знаю", "Другой вариант"], correctAnswer: "Метан", hint: "Алканы - только одинарные связи" },
      { type: 'quiz', question: "Этанол - это:", options: ["Уксус", "Спирт", "Сахар", "Не знаю", "Другой вариант"], correctAnswer: "Спирт", hint: "C₂H₅OH - этиловый спирт" },
      { type: 'quiz', question: "Из чего состоит молекула воды?", options: ["H₂O", "CO₂", "NaCl", "O₂", "H₂"], correctAnswer: "H₂O", hint: "Вода = H₂O" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь органическую химию! 🧪" }
  },
  {
    title: "Эволюция",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Автор теории эволюции:", options: ["Менделеев", "Дарвин", "Павлов", "Пушкин", "Лермонтов"], correctAnswer: "Дарвин", hint: "Чарльз Дарвин - автор теории эволюции" },
      { type: 'quiz', question: "Естественный отбор - это:", options: ["Выбор человека", "Выживание приспособленных", "Случайные изменения", "Не знаю", "Другой вариант"], correctAnswer: "Выживание приспособленных", hint: "Приспособленные особи выживают" },
      { type: 'quiz', question: "Укажи доказательства эволюции:", options: ["Палеонтологические", "Географические", "Физические", "Не знаю", "Другой вариант"], correctAnswer: "Палеонтологические", hint: "Основные доказательства эволюции" },
      { type: 'quiz', question: "Рудименты - это:", options: ["Новые органы", "Органы, утратившие функцию", "Атавизмы", "Не знаю", "Другой вариант"], correctAnswer: "Органы, утратившие функцию", hint: "Например, копчик у человека" },
      { type: 'quiz', question: "Какое животное млекопитающее?", options: ["Лягушка 🐸", "Рыба 🐟", "Кошка 🐱", "Змея 🐍", "Ящерица 🦎"], correctAnswer: "Кошка 🐱", hint: "Млекопитающие кормят детёнышей молоком" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь эволюцию! 🧬" }
  },
  {
    title: "Modal Verbs",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "\"You ___ smoke here\" (запрет):", options: ["can", "mustn\'t", "should", "Не знаю", "Другой вариант"], correctAnswer: "mustn\'t", hint: "Mustn\'t = строгий запрет" },
      { type: 'quiz', question: "\"She ___ be at home\" (вероятность):", options: ["must", "can", "should", "Не знаю", "Другой вариант"], correctAnswer: "must", hint: "Must = большая вероятность" },
      { type: 'quiz', question: "You ... take an umbrella. It\'s raining. (should/must)", options: ["прилагательное", "наречие", "существительное", "глагол", "should"], correctAnswer: "should", hint: "Should = совет" },
      { type: 'quiz', question: "\"I __ swim when I was 5\" (прошлое):", options: ["can", "could", "may", "Не знаю", "Другой вариант"], correctAnswer: "could", hint: "Could = мог в прошлом" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Great! Ты знаешь модальные глаголы! 🇬🇧" }
  },
  {
    title: "Исследование функций",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Точки экстремума - это:", options: ["Точки пересечения с осями", "Точки максимума и минимума", "Точки перегиба", "Не знаю", "Другой вариант"], correctAnswer: "Точки максимума и минимума", hint: "Экстремум = максимум или минимум" },
      { type: 'quiz', question: "Если f\'(x) > 0, то функция:", options: ["Возрастает", "Убывает", "Постоянна", "Не знаю", "Другой вариант"], correctAnswer: "Возрастает", hint: "Положительная производная = рост" },
      { type: 'quiz', question: "Если f\'(x) = 0 в точке, то это ... точка", options: ["наречие", "критическая", "существительное", "прилагательное", "глагол"], correctAnswer: "критическая", hint: "Критическая точка = производная равна 0" },
      { type: 'quiz', question: "Вторая производная показывает:", options: ["Скорость роста", "Выпуклость функции", "Экстремум", "Не знаю", "Другой вариант"], correctAnswer: "Выпуклость функции", hint: "f\'\'(x) > 0 = выпуклость вниз" },
      { type: 'quiz', question: "Чему равно 2 + 2?", options: ["3", "4", "5", "6", "8"], correctAnswer: "4", hint: "2 + 2 = 4" },
    ],
    reward: { stars: 3, message: "Отлично! Ты умеешь исследовать функции! 📊" }
  },
  {
    title: "Векторы в пространстве",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Вектор имеет:", options: ["Только длину", "Длину и направление", "Только направление", "Пушкин", "Лермонтов"], correctAnswer: "Длину и направление", hint: "Вектор - направленный отрезок" },
      { type: 'quiz', question: "Длина вектора a(3, 4, 0) = ...", options: ["4", "7", "5", "6", "3"], correctAnswer: "5", hint: "|a| = √(9 + 16 + 0) = 5" },
      { type: 'quiz', question: "Коллинеарные векторы:", options: ["Перпендикулярны", "Лежат на параллельных прямых", "Равны", "Пушкин", "Лермонтов"], correctAnswer: "Лежат на параллельных прямых", hint: "Коллинеарные = параллельные" },
      { type: 'quiz', question: "a(1,2,3), b(2,4,6). Векторы коллинеарны, k = ...", options: ["1", "4", "0", "3", "2"], correctAnswer: "2", hint: "b = 2a" },
      { type: 'quiz', question: "Сколько сторон у квадрата?", options: ["3", "4", "5", "6", "2"], correctAnswer: "4", hint: "Квадрат имеет 4 стороны" },
    ],
    reward: { stars: 3, message: "Супер! Ты работаешь с векторами! 📏" }
  },
  {
    title: "Молекулярная физика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Идеальный газ - это:", options: ["Реальный газ", "Модель газа без взаимодействия молекул", "Жидкость", "Не знаю", "Другой вариант"], correctAnswer: "Модель газа без взаимодействия молекул", hint: "Модель идеального газа" },
      { type: 'quiz', question: "Уравнение Менделеева-Клапейрона: PV = ...RT (ν - количество вещества)", options: ["глагол", "ν", "прилагательное", "существительное", "наречие"], correctAnswer: "ν", hint: "PV = νRT" },
      { type: 'quiz', question: "При постоянном объёме давление газа:", options: ["Не меняется", "Прямо пропорционально температуре", "Обратно пропорционально температуре", "Не знаю", "Другой вариант"], correctAnswer: "Прямо пропорционально температуре", hint: "Закон Шарля: P/T = const" },
      { type: 'quiz', question: "При T = 0 К тепловое движение ...", options: ["прекращается", "прилагательное", "наречие", "глагол", "существительное"], correctAnswer: "прекращается", hint: "Абсолютный ноль" },
      { type: 'quiz', question: "Что измеряется в метрах?", options: ["Время", "Масса", "Длина", "Температура", "Скорость"], correctAnswer: "Длина", hint: "Метр - единица длины" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь молекулярную физику! ⚛️" }
  },
  {
    title: "Электромагнетизм",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Магнитное поле создаётся:", options: ["Покоющимися зарядами", "Движущимися зарядами", "Только магнитами", "Не знаю", "Другой вариант"], correctAnswer: "Движущимися зарядами", hint: "Ток создаёт магнитное поле" },
      { type: 'quiz', question: "Сила Лоренца действует на:", options: ["Покоющийся заряд", "Движущийся заряд", "Любой заряд", "Не знаю", "Другой вариант"], correctAnswer: "Движущийся заряд", hint: "F = qvB sin α" },
      { type: 'quiz', question: "Укажи применения электромагнетизма:", options: ["Электродвигатель", "Термометр", "Линейка", "Не знаю", "Другой вариант"], correctAnswer: "Электродвигатель", hint: "Применения электромагнитной индукции" },
      { type: 'quiz', question: "Правило ... руки определяет направление силы (левой)", options: ["глагол", "левой", "наречие", "существительное", "прилагательное"], correctAnswer: "левой", hint: "Правило левой руки для силы Ампера" },
      { type: 'quiz', question: "Что измеряется в метрах?", options: ["Время", "Масса", "Длина", "Температура", "Скорость"], correctAnswer: "Длина", hint: "Метр - единица длины" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь электромагнетизм! ⚡" }
  },
  {
    title: "Гидролиз солей",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: "Гидролиз - это:", options: ["Разложение водой", "Разложение кислотой", "Окисление", "Не знаю", "Другой вариант"], correctAnswer: "Разложение водой", hint: "Гидролиз = взаимодействие с водой" },
      { type: 'quiz', question: "Соль сильной кислоты и слабого основания даёт среду:", options: ["Нейтральную", "Кислую", "Щелочную", "Не знаю", "Другой вариант"], correctAnswer: "Кислую", hint: "Например, NH₄Cl" },
      { type: 'quiz', question: "Укажи соли, подвергающиеся гидролизу:", options: ["CH₃COONa", "NaCl", "K₂SO₄", "Не знаю", "Другой вариант"], correctAnswer: "CH₃COONa", hint: "Соли слабых кислот или слабых оснований" },
      { type: 'quiz', question: "Среда раствора Na₂CO₃:", options: ["Нейтральная", "Кислая", "Щелочная", "Не знаю", "Другой вариант"], correctAnswer: "Щелочная", hint: "Соль слабой кислоты (угольной)" },
      { type: 'quiz', question: "Из чего состоит молекула воды?", options: ["H₂O", "CO₂", "NaCl", "O₂", "H₂"], correctAnswer: "H₂O", hint: "Вода = H₂O" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь гидролиз! 🧪" }
  },
  {
    title: "Генетика",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Ген - это:", options: ["Белок", "Участок ДНК", "Клетка", "Не знаю", "Другой вариант"], correctAnswer: "Участок ДНК", hint: "Ген кодирует признак" },
      { type: 'quiz', question: "Гомозигота имеет:", options: ["Разные аллели", "Одинаковые аллели", "Только доминантный признак", "Не знаю", "Другой вариант"], correctAnswer: "Одинаковые аллели", hint: "AA или aa" },
      { type: 'quiz', question: "Укажи законы Менделя:", options: ["Единообразия", "Сцепления", "Доминирования", "Не знаю", "Другой вариант"], correctAnswer: "Единообразия", hint: "Три закона Менделя" },
      { type: 'quiz', question: "При скрещивании Aa × Aa расщепление по фенотипу ...:1 (доминантный:рецессивный)", options: ["3", "2", "4", "1", "5"], correctAnswer: "3", hint: "3:1 по фенотипу" },
      { type: 'quiz', question: "Какое животное млекопитающее?", options: ["Лягушка 🐸", "Рыба 🐟", "Кошка 🐱", "Змея 🐍", "Ящерица 🦎"], correctAnswer: "Кошка 🐱", hint: "Млекопитающие кормят детёнышей молоком" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь генетику! 🧬" }
  },
  {
    title: "Революция 1917 года",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Февральская революция произошла в:", options: ["1914", "1917", "1918", "Не знаю", "Другой вариант"], correctAnswer: "1917", hint: "Февраль 1917 года" },
      { type: 'quiz', question: "Результат Февральской революции:", options: ["Приход большевиков", "Отречение Николая II", "Начало войны", "Не знаю", "Другой вариант"], correctAnswer: "Отречение Николая II", hint: "Конец монархии в России" },
      { type: 'quiz', question: "Укажи события 1917 года:", options: ["Февральская революция", "Гражданская война", "Первая мировая", "Не знаю", "Другой вариант"], correctAnswer: "Февральская революция", hint: "Ключевые события 1917 года" },
      { type: 'quiz', question: "Октябрьская революция привела к:", options: ["Конституционной монархии", "Установлению советской власти", "Демократии", "Не знаю", "Другой вариант"], correctAnswer: "Установлению советской власти", hint: "Большевики взяли власть" },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь историю! ⚔️" }
  },
  {
    title: "Conditionals",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Zero Conditional описывает:", options: ["Будущее", "Законы природы", "Нереальное", "Не знаю", "Другой вариант"], correctAnswer: "Законы природы", hint: "If + Present, Present" },
      { type: 'quiz', question: "First Conditional: If it rains, I __ (stay) home.", options: ["will stay", "would stay", "stay", "Не знаю", "Другой вариант"], correctAnswer: "will stay", hint: "First = реальное будущее" },
      { type: 'quiz', question: "If I ... (be) you, I would study more. (were)", options: ["наречие", "существительное", "глагол", "were", "прилагательное"], correctAnswer: "were", hint: "Second Conditional = нереальное настоящее" },
      { type: 'quiz', question: "Укажи типы условных предложений:", options: ["Zero Conditional", "Past Conditional", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Zero Conditional", hint: "Четыре основных типа" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Great! Ты знаешь условные предложения! 🇬🇧" }
  },
  {
    title: "Сочинение ЕГЭ",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Проблема в сочинении - это:", options: ["Тема текста", "Вопрос, над которым размышляет автор", "Главная мысль", "Не знаю", "Другой вариант"], correctAnswer: "Вопрос, над которым размышляет автор", hint: "Проблема = вопрос" },
      { type: 'quiz', question: "Позиция автора - это:", options: ["Тема текста", "Отношение автора к проблеме", "Вывод", "Пушкин", "Лермонтов"], correctAnswer: "Отношение автора к проблеме", hint: "Что думает автор" },
      { type: 'quiz', question: "Укажи структуру сочинения:", options: ["Вступление", "Не знаю", "Другой вариант", "Ни один из этих", "Все перечисленные"], correctAnswer: "Вступление", hint: "Структура сочинения ЕГЭ" },
      { type: 'quiz', question: "К2 в критериях - это ...", options: ["глагол", "существительное", "комментарий", "наречие", "прилагательное"], correctAnswer: "комментарий", hint: "Комментарий к проблеме" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты готов к сочинению! 📝" }
  },
  {
    title: "Тригонометрические формулы",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "sin 45° = .../√2 (число)", options: ["3", "4", "2", "0", "1"], correctAnswer: "1", hint: "sin 45° = 1/√2 = √2/2" },
      { type: 'quiz', question: "cos 90° = ?", options: ["0", "1", "-1", "Не знаю", "Другой вариант"], correctAnswer: "0", hint: "Косинус 90° = 0" },
      { type: 'quiz', question: "sin 2x = ?", options: ["2 sin x cos x", "sin²x + cos²x", "2 sin²x", "Не знаю", "Другой вариант"], correctAnswer: "2 sin x cos x", hint: "Формула синуса двойного угла" },
      { type: 'quiz', question: "cos 2x = cos²x - ...²x", options: ["существительное", "глагол", "прилагательное", "sin", "наречие"], correctAnswer: "sin", hint: "cos 2x = cos²x - sin²x" },
      { type: 'quiz', question: "Чему равно 2 + 2?", options: ["3", "4", "5", "6", "8"], correctAnswer: "4", hint: "2 + 2 = 4" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тригонометрию! 📐" }
  },
  {
    title: "Тела вращения",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Цилиндр получается вращением:", options: ["Треугольника", "Прямоугольника", "Круга", "Не знаю", "Другой вариант"], correctAnswer: "Прямоугольника", hint: "Вращение прямоугольника вокруг стороны" },
      { type: 'quiz', question: "Объём цилиндра V = πr²h. Если r=2, h=5, то V = ...π", options: ["19", "20", "18", "22", "21"], correctAnswer: "20", hint: "V = π · 4 · 5 = 20π" },
      { type: 'quiz', question: "Конус получается вращением:", options: ["Прямоугольника", "Треугольника", "Круга", "Не знаю", "Другой вариант"], correctAnswer: "Треугольника", hint: "Вращение прямоугольного треугольника" },
      { type: 'quiz', question: "Объём конуса:", options: ["πr²h", "(1/3)πr²h", "(4/3)πr³", "Не знаю", "Другой вариант"], correctAnswer: "(1/3)πr²h", hint: "V = 1/3 · πr² · h" },
      { type: 'quiz', question: "Сколько сторон у квадрата?", options: ["3", "4", "5", "6", "2"], correctAnswer: "4", hint: "Квадрат имеет 4 стороны" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тела вращения! ⭕" }
  },
  {
    title: "Законы сохранения",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Закон сохранения энергии:", options: ["E = const", "E всегда растёт", "E всегда убывает", "Не знаю", "Другой вариант"], correctAnswer: "E = const", hint: "Энергия не исчезает, а переходит" },
      { type: 'quiz', question: "Кинетическая энергия:", options: ["mgh", "mv²/2", "kx²/2", "Не знаю", "Другой вариант"], correctAnswer: "mv²/2", hint: "Eк = mv²/2" },
      { type: 'quiz', question: "Потенциальная энергия: Eп = mgh. Если m=2, g=10, h=5, то Eп = ... Дж", options: ["90", "100", "98", "102", "95"], correctAnswer: "100", hint: "Eп = 2 × 10 × 5 = 100" },
      { type: 'quiz', question: "Закон сохранения импульса:", options: ["p₁ = p₂", "p₁ + p₂ = const", "p всегда 0", "Не знаю", "Другой вариант"], correctAnswer: "p₁ + p₂ = const", hint: "Импульс системы сохраняется" },
      { type: 'quiz', question: "Что измеряется в метрах?", options: ["Время", "Масса", "Длина", "Температура", "Скорость"], correctAnswer: "Длина", hint: "Метр - единица длины" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь законы сохранения! ⚛️" }
  },
  {
    title: "Алкины и алкены",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: "Алкены имеют общую формулу:", options: ["CₙH₂ₙ₊₂", "CₙH₂ₙ", "CₙH₂ₙ₋₂", "Не знаю", "Другой вариант"], correctAnswer: "CₙH₂ₙ", hint: "Алкены содержат двойную связь" },
      { type: 'quiz', question: "Этен (этилен) - это:", options: ["C₂H₄", "C₂H₆", "C₂H₂", "Не знаю", "Другой вариант"], correctAnswer: "C₂H₄", hint: "Этен = C₂H₄ с двойной связью" },
      { type: 'quiz', question: "Укажи алкины:", options: ["Этин", "Этен", "Пропан", "Не знаю", "Другой вариант"], correctAnswer: "Этин", hint: "Алкины содержат тройную связь" },
      { type: 'quiz', question: "Этин (ацетилен) имеет формулу: C...H₂", options: ["4", "0", "1", "2", "3"], correctAnswer: "2", hint: "C₂H₂ - ацетилен" },
      { type: 'quiz', question: "Из чего состоит молекула воды?", options: ["H₂O", "CO₂", "NaCl", "O₂", "H₂"], correctAnswer: "H₂O", hint: "Вода = H₂O" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь углеводороды! 🧪" }
  },
  {
    title: "Экосистемы",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Продуценты - это:", options: ["Хищники", "Производители органики", "Разлагатели", "Не знаю", "Другой вариант"], correctAnswer: "Производители органики", hint: "Продуценты = растения" },
      { type: 'quiz', question: "Укажи функциональные группы:", options: ["Продуценты", "Минералы", "Вода", "Не знаю", "Другой вариант"], correctAnswer: "Продуценты", hint: "Три функциональные группы" },
      { type: 'quiz', question: "Пищевая цепь начинается с:", options: ["Хищников", "Растений", "Разлагателей", "Не знаю", "Другой вариант"], correctAnswer: "Растений", hint: "Растения - продуценты" },
      { type: 'quiz', question: "Правило ...%: на следующий уровень переходит ~10% энергии", options: ["9", "11", "10", "8", "12"], correctAnswer: "10", hint: "Правило 10%" },
      { type: 'quiz', question: "Какое животное млекопитающее?", options: ["Лягушка 🐸", "Рыба 🐟", "Кошка 🐱", "Змея 🐍", "Ящерица 🦎"], correctAnswer: "Кошка 🐱", hint: "Млекопитающие кормят детёнышей молоком" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь экосистемы! 🌿" }
  },
  {
    title: "Холодная война",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "\"Холодная война\" началась после:", options: ["Первой мировой", "Второй мировой", "Революции 1917", "Не знаю", "Другой вариант"], correctAnswer: "Второй мировой", hint: "Противостояние СССР и США" },
      { type: 'quiz', question: "Карибский кризис:", options: ["1960", "1962", "1965", "Не знаю", "Другой вариант"], correctAnswer: "1962", hint: "1962 год - ядерный кризис" },
      { type: 'quiz', question: "Укажи события \"холодной войны\":", options: ["Карибский кризис", "Вторая мировая", "Первая мировая", "Не знаю", "Другой вариант"], correctAnswer: "Карибский кризис", hint: "Глобальное противостояние" },
      { type: 'quiz', question: "\"Железный занавес\" - это:", options: ["Реальная стена", "Политический барьер", "Военный союз", "Не знаю", "Другой вариант"], correctAnswer: "Политический барьер", hint: "Разделение Востока и Запада" },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь историю! ⚔️" }
  },
  {
    title: "Passive Voice",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "The book ___ (write) by Pushkin.", options: ["wrote", "was written", "written", "Не знаю", "Другой вариант"], correctAnswer: "was written", hint: "Past Simple Passive: was/were + V3" },
      { type: 'quiz', question: "English ... (speak) worldwide. (is spoken)", options: ["прилагательное", "глагол", "is spoken", "наречие", "существительное"], correctAnswer: "is spoken", hint: "Present Simple Passive: am/is/are + V3" },
      { type: 'quiz', question: "The house ___ (build) next year.", options: ["will build", "will be built", "built", "Не знаю", "Другой вариант"], correctAnswer: "will be built", hint: "Future Simple Passive: will be + V3" },
      { type: 'quiz', question: "Укажи признаки пассивного залога:", options: ["be + V3", "have + V3", "will do", "Не знаю", "Другой вариант"], correctAnswer: "be + V3", hint: "Пассив = быть + причастие" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Great! Ты знаешь пассивный залог! 🇬🇧" }
  }
]
