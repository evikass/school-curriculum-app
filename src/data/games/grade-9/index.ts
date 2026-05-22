// Экспорт игр для 9 класса
import { GameLesson } from '../types'

export const ninthGradeGames: GameLesson[] = [
  {
    title: "Неравенства",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "При делении неравенства на отрицательное число знак:", options: ["Не меняется", "Меняется на противоположный", "Становится равенством", "1", "2"], correctAnswer: "Меняется на противоположный", hint: "Важно: при делении на минус знак меняется!" },
      { type: 'quiz', question: "Решить: 2x > 6", options: ["x > 3", "x < 3", "x > 4", "Не знаю", "Другой вариант"], correctAnswer: "x > 3", hint: "x > 6/2 = 3" },
      { type: 'quiz', question: "-x > 5, значит x < ...", options: ["95", "5", "45", "15", "-5"], correctAnswer: "-5", hint: "При делении на -1 знак меняется" },
      { type: 'quiz', question: "Решить систему: x > 2 и x < 5", options: ["(2; 5)", "x > 5", "x < 2", "Не знаю", "Другой вариант"], correctAnswer: "(2; 5)", hint: "Пересечение интервалов" },
      { type: 'quiz', question: "Чему равно 2 + 2?", options: ["3", "4", "5", "6", "8"], correctAnswer: "4", hint: "2 + 2 = 4" },
    ],
    reward: { stars: 3, message: "Отлично! Ты решаешь неравенства! 📐" }
  },
  {
    title: "Прогрессии",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Арифметическая прогрессия: aₙ = a₁ + (n-1)d. Чему равен 5-й член: 2, 5, 8...?", options: ["11", "14", "17", "Не знаю", "Другой вариант"], correctAnswer: "14", hint: "a₅ = 2 + 4×3 = 14" },
      { type: 'quiz', question: "Сумма первых n членов арифм. прогрессии: Sₙ = n(a₁+aₙ)/2. S₅ = ... (для 2, 5, 8, 11, 14)", options: ["38", "42", "40", "35", "30"], correctAnswer: "40", hint: "S₅ = 5(2+14)/2 = 40" },
      { type: 'quiz', question: "Геометрическая прогрессия: bₙ = b₁ × qⁿ⁻¹. Чему равен 4-й член: 2, 6, 18...?", options: ["36", "54", "72", "Не знаю", "Другой вариант"], correctAnswer: "54", hint: "q = 3, b₄ = 2 × 3³ = 54" },
      { type: 'quiz', question: "Знаменатель геометрической прогрессии 3, 6, 12...:", options: ["2", "3", "4", "Не знаю", "Другой вариант"], correctAnswer: "2", hint: "q = b₂/b₁ = 6/3 = 2" },
      { type: 'quiz', question: "Чему равно 2 + 2?", options: ["3", "4", "5", "6", "8"], correctAnswer: "4", hint: "2 + 2 = 4" },
    ],
    reward: { stars: 3, message: "Супер! Ты понимаешь прогрессии! 🔢" }
  },
  {
    title: "Функции",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Что такое область определения функции?", options: ["Все значения y", "Все значения x", "График функции", "Не знаю", "Другой вариант"], correctAnswer: "Все значения x", hint: "D(f) - допустимые значения x" },
      { type: 'quiz', question: "График y = x² называется:", options: ["Прямая", "Парабола", "Гипербола", "Не знаю", "Другой вариант"], correctAnswer: "Парабола", hint: "Парабола - график квадратичной функции" },
      { type: 'quiz', question: "График y = k/x называется:", options: ["Прямая", "Парабола", "Гипербола", "Не знаю", "Другой вариант"], correctAnswer: "Гипербола", hint: "Обратная пропорциональность" },
      { type: 'quiz', question: "Вершина параболы y = (x-2)² + 3:", options: ["(0; 0)", "(2; 3)", "(-2; 3)", "Не знаю", "Другой вариант"], correctAnswer: "(2; 3)", hint: "y = (x-a)² + b → вершина (a; b)" },
      { type: 'quiz', question: "Чему равно 2 + 2?", options: ["3", "4", "5", "6", "8"], correctAnswer: "4", hint: "2 + 2 = 4" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь функции! 📊" }
  },
  {
    title: "Векторы",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Вектор имеет:", options: ["Только направление", "Только длину", "Направление и длину", "Пушкин", "Лермонтов"], correctAnswer: "Направление и длину", hint: "Вектор - направленный отрезок" },
      { type: 'quiz', question: "Сумма векторов a + b - это:", options: ["Вектор", "Число", "Точка", "Пушкин", "Лермонтов"], correctAnswer: "Вектор", hint: "Сумма векторов - вектор" },
      { type: 'quiz', question: "Длина вектора с координатами (3; 4) = ...", options: ["6", "7", "3", "5", "4"], correctAnswer: "5", hint: "|a| = √(3² + 4²) = 5" },
      { type: 'quiz', question: "Коллинеарные векторы:", options: ["Перпендикулярны", "Лежат на параллельных прямых", "Равны", "Пушкин", "Лермонтов"], correctAnswer: "Лежат на параллельных прямых", hint: "Коллинеарные = сонаправленные или противоположные" },
      { type: 'quiz', question: "Сколько сторон у квадрата?", options: ["3", "4", "5", "6", "2"], correctAnswer: "4", hint: "Квадрат имеет 4 стороны" },
    ],
    reward: { stars: 3, message: "Отлично! Ты работаешь с векторами! 📏" }
  },
  {
    title: "Окружность и круг",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Вписанный угол равен:", options: ["Дуге", "Половине дуги", "Центральному углу", "Не знаю", "Другой вариант"], correctAnswer: "Половине дуги", hint: "Вписанный угол = ½ дуги" },
      { type: 'quiz', question: "Центральный угол равен:", options: ["Дуге", "Половине дуги", "Вписанному углу", "Не знаю", "Другой вариант"], correctAnswer: "Дуге", hint: "Центральный угол = дуга" },
      { type: 'quiz', question: "Длина окружности C = 2πr. Если r = 5, то C = ...π", options: ["10", "12", "8", "11", "9"], correctAnswer: "10", hint: "C = 2π × 5 = 10π" },
      { type: 'quiz', question: "Угол, опирающийся на диаметр:", options: ["Острый", "Тупой", "Прямой", "Не знаю", "Другой вариант"], correctAnswer: "Прямой", hint: "Вписанный угол на диаметр = 90°" },
      { type: 'quiz', question: "Сколько сторон у квадрата?", options: ["3", "4", "5", "6", "2"], correctAnswer: "4", hint: "Квадрат имеет 4 стороны" },
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь окружность! ⭕" }
  },
  {
    title: "Сложное предложение",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Сложносочинённое предложение связывается:", options: ["Инфинитивом", "Сочинительными союзами", "Подчинительными союзами", "Не знаю", "Другой вариант"], correctAnswer: "Сочинительными союзами", hint: "ССП: и, а, но, или" },
      { type: 'quiz', question: "Сложноподчинённое предложение связывается:", options: ["Инфинитивом", "Сочинительными союзами", "Подчинительными союзами", "Не знаю", "Другой вариант"], correctAnswer: "Подчинительными союзами", hint: "СПП: что, чтобы, если, когда" },
      { type: 'quiz', question: "Укажи подчинительные союзы:", options: ["Что", "И", "Но", "А", "Не знаю"], correctAnswer: "Что", hint: "Подчинительные: что, чтобы, если, когда, потому что" },
      { type: 'quiz', question: "Бессоюзное предложение связывается:", options: ["Союзами", "Интонацией", "Предлогами", "Не знаю", "Другой вариант"], correctAnswer: "Интонацией", hint: "БСП: части связаны по смыслу" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь сложные предложения! 📝" }
  },
  {
    title: "Достоевский",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Ф.М. Достоевский родился в:", options: ["1819", "1821", "1825", "Не знаю", "Другой вариант"], correctAnswer: "1821", hint: "1821 год, Москва" },
      { type: 'quiz', question: "Укажи произведения Достоевского:", options: ["Преступление и наказание", "Война и мир", "Отцы и дети", "Не знаю", "Другой вариант"], correctAnswer: "Преступление и наказание", hint: "Достоевский - великий психолог" },
      { type: 'quiz', question: "Родион Раскольников - герой произведения:", options: ["Идиот", "Преступление и наказание", "Бесы", "Не знаю", "Другой вариант"], correctAnswer: "Преступление и наказание", hint: "Раскольников - главный герой романа" },
      { type: 'quiz', question: "Теория Раскольникова о:", options: ["Любви", "Тварях дрожащих и Право имеющих", "Боге", "Не знаю", "Другой вариант"], correctAnswer: "Тварях дрожащих и Право имеющих", hint: "Люди делятся на два типа" },
      { type: 'quiz', question: "Что такое сказка?", options: ["Научная статья", "Стихотворение", "Выдуманная история", "Учебник", "Энциклопедия"], correctAnswer: "Выдуманная история", hint: "Сказка - вымышленный рассказ" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь Достоевского! 📚" }
  },
  {
    title: "Толстой",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Л.Н. Толстой родился в:", options: ["1828", "1820", "1835", "Не знаю", "Другой вариант"], correctAnswer: "1828", hint: "1828 год, Ясная Поляна" },
      { type: 'quiz', question: "Укажи произведения Толстого:", options: ["Война и мир", "Преступление и наказание", "Отцы и дети", "Не знаю", "Другой вариант"], correctAnswer: "Война и мир", hint: "Толстой - великий русский писатель" },
      { type: 'quiz', question: "\"Война и мир\" - это:", options: ["Роман", "Роман-эпопея", "Повесть", "Не знаю", "Другой вариант"], correctAnswer: "Роман-эпопея", hint: "Масштабное произведение о войне 1812 года" },
      { type: 'quiz', question: "Пьер Безухов - герой:", options: ["Анны Карениной", "Войны и мира", "Воскресения", "Не знаю", "Другой вариант"], correctAnswer: "Войны и мира", hint: "Пьер - один из главных героев" },
      { type: 'quiz', question: "Что такое сказка?", options: ["Научная статья", "Стихотворение", "Выдуманная история", "Учебник", "Энциклопедия"], correctAnswer: "Выдуманная история", hint: "Сказка - вымышленный рассказ" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь Толстого! 📖" }
  },
  {
    title: "Первая мировая война",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Когда началась Первая мировая война?", options: ["1914", "1917", "1939", "Не знаю", "Другой вариант"], correctAnswer: "1914", hint: "28 июля 1914 года" },
      { type: 'quiz', question: "Повод к войне:", options: ["Убийство эрцгерцога Франца Фердинанда", "Нападение Германии на Польшу", "Революция в России", "Не знаю", "Другой вариант"], correctAnswer: "Убийство эрцгерцога Франца Фердинанда", hint: "Сараевское убийство" },
      { type: 'quiz', question: "Укажи страны Антанты:", options: ["Россия", "Германия", "Австро-Венгрия", "Не знаю", "Другой вариант"], correctAnswer: "Россия", hint: "Антанта = Россия, Франция, Англия" },
      { type: 'quiz', question: "Когда Россия вышла из войны?", options: ["1915", "1917", "1918", "Не знаю", "Другой вариант"], correctAnswer: "1917", hint: "После Октябрьской революции" },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь историю! ⚔️" }
  },
  {
    title: "Революция 1917 года",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Когда произошла Февральская революция?", options: ["Февраль 1917", "Март 1917", "Октябрь 1917", "Не знаю", "Другой вариант"], correctAnswer: "Февраль 1917", hint: "По старому стилю - февраль" },
      { type: 'quiz', question: "Последний российский император:", options: ["Александр III", "Николай II", "Александр II", "Не знаю", "Другой вариант"], correctAnswer: "Николай II", hint: "Николай II отрёкся в 1917 году" },
      { type: 'quiz', question: "Укажи события 1917 года:", options: ["Февральская революция", "Кровавое воскресенье", "Русско-японская война", "Не знаю", "Другой вариант"], correctAnswer: "Февральская революция", hint: "1917 год - год двух революций" },
      { type: 'quiz', question: "Кто возглавил Октябрьскую революцию?", options: ["Керенский", "Ленин", "Николай II", "Пушкин", "Лермонтов"], correctAnswer: "Ленин", hint: "Большевики под руководством Ленина" },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь историю России! 🏛️" }
  },
  {
    title: "Оптика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Угол падения равен:", options: ["Углу отражения", "Половине угла отражения", "Двойному углу отражения", "Не знаю", "Другой вариант"], correctAnswer: "Углу отражения", hint: "Закон отражения света" },
      { type: 'quiz', question: "При переходе света в более плотную среду:", options: ["Увеличивается скорость", "Уменьшается скорость", "Скорость не меняется", "Не знаю", "Другой вариант"], correctAnswer: "Уменьшается скорость", hint: "Показатель преломления больше" },
      { type: 'quiz', question: "Фокусное расстояние линзы F = 20 см. Оптическая сила D = ... дптр", options: ["6", "5", "4", "7", "3"], correctAnswer: "5", hint: "D = 1/F = 1/0.2 = 5 дптр" },
      { type: 'quiz', question: "Линза, которая собирает лучи:", options: ["Рассеивающая", "Собирающая", "Плоская", "Не знаю", "Другой вариант"], correctAnswer: "Собирающая", hint: "Выпуклая линза - собирающая" },
      { type: 'quiz', question: "Что измеряется в метрах?", options: ["Время", "Масса", "Длина", "Температура", "Скорость"], correctAnswer: "Длина", hint: "Метр - единица длины" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь оптику! 💡" }
  },
  {
    title: "Химические реакции",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: "Реакция соединения:", options: ["A + B → AB", "AB → A + B", "AB + C → AC + B", "Не знаю", "Другой вариант"], correctAnswer: "A + B → AB", hint: "Из нескольких веществ - одно" },
      { type: 'quiz', question: "Реакция разложения:", options: ["A + B → AB", "AB → A + B", "AB + C → AC + B", "Не знаю", "Другой вариант"], correctAnswer: "AB → A + B", hint: "Из одного вещества - несколько" },
      { type: 'quiz', question: "Укажи типы химических реакций:", options: ["Соединения", "Образования", "Разрушения", "Не знаю", "Другой вариант"], correctAnswer: "Соединения", hint: "Основные типы реакций" },
      { type: 'quiz', question: "Катализатор:", options: ["Ускоряет реакцию", "Замедляет реакцию", "Не влияет на реакцию", "Не знаю", "Другой вариант"], correctAnswer: "Ускоряет реакцию", hint: "Катализатор ускоряет, но не расходуется" },
      { type: 'quiz', question: "Из чего состоит молекула воды?", options: ["H₂O", "CO₂", "NaCl", "O₂", "H₂"], correctAnswer: "H₂O", hint: "Вода = H₂O" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь химию! 🧪" }
  },
  {
    title: "Генетика",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Ген - это:", options: ["Клетка", "Участок ДНК", "Белок", "Не знаю", "Другой вариант"], correctAnswer: "Участок ДНК", hint: "Ген кодирует признак" },
      { type: 'quiz', question: "Гомозигота - это:", options: ["AA", "Aa", "aa или AA", "Не знаю", "Другой вариант"], correctAnswer: "aa или AA", hint: "Гомозигота - одинаковые аллели" },
      { type: 'quiz', question: "Укажи термины генетики:", options: ["Генотип", "Хлорофилл", "Митохондрия", "Не знаю", "Другой вариант"], correctAnswer: "Генотип", hint: "Основные термины генетики" },
      { type: 'quiz', question: "При скрещивании Aa × Aa (гетерозиготы), расщепление по фенотипу:", options: ["1:1", "1:2:1", "3:1", "Не знаю", "Другой вариант"], correctAnswer: "3:1", hint: "Второй закон Менделя" },
      { type: 'quiz', question: "Какое животное млекопитающее?", options: ["Лягушка 🐸", "Рыба 🐟", "Кошка 🐱", "Змея 🐍", "Ящерица 🦎"], correctAnswer: "Кошка 🐱", hint: "Млекопитающие кормят детёнышей молоком" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь генетику! 🧬" }
  },
  {
    title: "Reported Speech",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Прямая: \"I am happy\" → Косвенная:", options: ["He said he is happy", "He said he was happy", "He said he will be happy", "Не знаю", "Другой вариант"], correctAnswer: "He said he was happy", hint: "Present → Past при согласовании" },
      { type: 'quiz', question: "\"I will come\" → He said:", options: ["he will come", "he would come", "he came", "Не знаю", "Другой вариант"], correctAnswer: "he would come", hint: "Future → Future in the Past" },
      { type: 'quiz', question: "\"I saw him\" → She said she ... seen him. (had/has)", options: ["глагол", "had", "существительное", "наречие", "прилагательное"], correctAnswer: "had", hint: "Past → Past Perfect" },
      { type: 'quiz', question: "\"Don\'t go!\" → She told me:", options: ["don\'t go", "not to go", "to not go", "Не знаю", "Другой вариант"], correctAnswer: "not to go", hint: "Повелительное → инфинитив с not" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Great! Ты знаешь косвенную речь! 🇬🇧" }
  },
  {
    title: "Степени сравнения прилагательных",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "good - better - ___", options: ["goodest", "best", "more good", "Не знаю", "Другой вариант"], correctAnswer: "best", hint: "good - better - best (исключение)" },
      { type: 'quiz', question: "bad - worse - ...", options: ["глагол", "worst", "наречие", "прилагательное", "существительное"], correctAnswer: "worst", hint: "bad - worse - worst" },
      { type: 'quiz', question: "important - more important - ___", options: ["most important", "importanter", "more important", "Не знаю", "Другой вариант"], correctAnswer: "most important", hint: "Длинные слова: more/most" },
      { type: 'quiz', question: "Укажи правильные формы:", options: ["tall-taller-tallest", "good-gooder-goodest", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "tall-taller-tallest", hint: "Исключения: good, bad, far" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Excellent! Степени сравнения! 📈" }
  },
  {
    title: "Корни и степени",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "√81 = ...", options: ["8", "10", "11", "9", "7"], correctAnswer: "9", hint: "9 × 9 = 81" },
      { type: 'quiz', question: "³√27 = ...", options: ["4", "1", "3", "2", "5"], correctAnswer: "3", hint: "3 × 3 × 3 = 27" },
      { type: 'quiz', question: "2³ = ?", options: ["6", "8", "9", "Не знаю", "Другой вариант"], correctAnswer: "8", hint: "2 × 2 × 2 = 8" },
      { type: 'quiz', question: "5⁰ = ?", options: ["0", "1", "5", "Не знаю", "Другой вариант"], correctAnswer: "1", hint: "Любое число в нулевой степени = 1" },
      { type: 'quiz', question: "Чему равно 2 + 2?", options: ["3", "4", "5", "6", "8"], correctAnswer: "4", hint: "2 + 2 = 4" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь корни и степени! 🔢" }
  },
  {
    title: "Системы уравнений",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Сколько решений может иметь система линейных уравнений?", options: ["Только одно", "0, 1 или бесконечно много", "Только два", "1", "2"], correctAnswer: "0, 1 или бесконечно много", hint: "Система может иметь 0, 1 или ∞ решений" },
      { type: 'quiz', question: "x + y = 5, x - y = 1. Сложив, получим: 2x = ...", options: ["7", "5", "8", "6", "4"], correctAnswer: "6", hint: "y исчезает, 2x = 6" },
      { type: 'quiz', question: "Метод подстановки:", options: ["Сложить уравнения", "Выразить одну переменную через другую", "Умножить уравнения", "Не знаю", "Другой вариант"], correctAnswer: "Выразить одну переменную через другую", hint: "Подстановка в другое уравнение" },
      { type: 'quiz', question: "Если x + y = 5 и x = 2, то y = ...", options: ["1", "2", "5", "3", "4"], correctAnswer: "3", hint: "2 + y = 5, y = 3" },
      { type: 'quiz', question: "Чему равно 2 + 2?", options: ["3", "4", "5", "6", "8"], correctAnswer: "4", hint: "2 + 2 = 4" },
    ],
    reward: { stars: 3, message: "Отлично! Ты решаешь системы! 📐" }
  },
  {
    title: "Свойства функций",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Область определения - это:", options: ["Все значения y", "Все допустимые значения x", "График функции", "Не знаю", "Другой вариант"], correctAnswer: "Все допустимые значения x", hint: "D(f) - допустимые x" },
      { type: 'quiz', question: "Функция возрастает, если:", options: ["y уменьшается", "y увеличивается при росте x", "y постоянна", "Не знаю", "Другой вариант"], correctAnswer: "y увеличивается при росте x", hint: "Возрастание = рост" },
      { type: 'quiz', question: "Укажи чётные функции:", options: ["y = x²", "y = x³", "y = √x", "Не знаю", "Другой вариант"], correctAnswer: "y = x²", hint: "f(-x) = f(x) для чётных" },
      { type: 'quiz', question: "Нули функции - это:", options: ["Максимумы", "Точки пересечения с осью x", "Минимумы", "Не знаю", "Другой вариант"], correctAnswer: "Точки пересечения с осью x", hint: "f(x) = 0" },
      { type: 'quiz', question: "Чему равно 2 + 2?", options: ["3", "4", "5", "6", "8"], correctAnswer: "4", hint: "2 + 2 = 4" },
    ],
    reward: { stars: 3, message: "Супер! Ты понимаешь функции! 📊" }
  },
  {
    title: "Подобие треугольников",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Подобные треугольники имеют:", options: ["Равные стороны", "Равные углы и пропорциональные стороны", "Равные площади", "Не знаю", "Другой вариант"], correctAnswer: "Равные углы и пропорциональные стороны", hint: "Подобие = одинаковость формы" },
      { type: 'quiz', question: "Первый признак подобия:", options: ["По трём сторонам", "По двум углам", "По стороне и углу", "Не знаю", "Другой вариант"], correctAnswer: "По двум углам", hint: "Два угла одного = два угла другого" },
      { type: 'quiz', question: "Если коэффициент подобия k = 3, то площадь больше в ... раз", options: ["11", "8", "9", "10", "7"], correctAnswer: "9", hint: "Площади относятся как k²" },
      { type: 'quiz', question: "Отношение периметров подобных треугольников:", options: ["k²", "k", "k³", "Не знаю", "Другой вариант"], correctAnswer: "k", hint: "Периметры относятся как k" },
      { type: 'quiz', question: "Сколько сторон у квадрата?", options: ["3", "4", "5", "6", "2"], correctAnswer: "4", hint: "Квадрат имеет 4 стороны" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь подобие! 📐" }
  },
  {
    title: "Окружность",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Вписанный угол равен:", options: ["Дуге", "Половине дуги", "Центральному углу", "Не знаю", "Другой вариант"], correctAnswer: "Половине дуги", hint: "Вписанный = ½ центрального" },
      { type: 'quiz', question: "Угол, опирающийся на диаметр:", options: ["Острый", "Тупой", "Прямой", "Не знаю", "Другой вариант"], correctAnswer: "Прямой", hint: "Всегда 90°" },
      { type: 'quiz', question: "Длина окружности C = 2πr. Если r = 7, то C = ...π", options: ["16", "15", "12", "13", "14"], correctAnswer: "14", hint: "C = 2π × 7 = 14π" },
      { type: 'quiz', question: "Укажи элементы окружности:", options: ["Радиус", "Высота", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Радиус", hint: "Элементы окружности" },
      { type: 'quiz', question: "Сколько сторон у квадрата?", options: ["3", "4", "5", "6", "2"], correctAnswer: "4", hint: "Квадрат имеет 4 стороны" },
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь окружность! ⭕" }
  },
  {
    title: "Синтаксис сложного предложения",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Сложносочинённое предложение связывается:", options: ["Подчинительными союзами", "Сочинительными союзами", "Интонацией", "Не знаю", "Другой вариант"], correctAnswer: "Сочинительными союзами", hint: "И, а, но, или" },
      { type: 'quiz', question: "Укажи сочинительные союзы:", options: ["И", "Что", "Если", "Не знаю", "Другой вариант"], correctAnswer: "И", hint: "Сочинительные: и, а, но, или" },
      { type: 'quiz', question: "Сложноподчинённое предложение имеет:", options: ["Равные части", "Главное и придаточное", "Только главное", "Не знаю", "Другой вариант"], correctAnswer: "Главное и придаточное", hint: "Подчинение частей" },
      { type: 'quiz', question: "Бессоюзное предложение связывается ...", options: ["существительное", "наречие", "интонацией", "глагол", "прилагательное"], correctAnswer: "интонацией", hint: "Без союзов" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь синтаксис! 📝" }
  },
  {
    title: "Русская литература XIX века",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "\"Герой нашего времени\" - автор:", options: ["Пушкин", "Лермонтов", "Гоголь", "Толстой", "Достоевский"], correctAnswer: "Лермонтов", hint: "Михаил Юрьевич Лермонтов" },
      { type: 'quiz', question: "Укажи произведения Пушкина:", options: ["Евгений Онегин", "Мцыри", "Ревизор", "Не знаю", "Другой вариант"], correctAnswer: "Евгений Онегин", hint: "А.С. Пушкин" },
      { type: 'quiz', question: "\"Мёртвые души\" - автор:", options: ["Пушкин", "Гоголь", "Тургенев", "Лермонтов", "Толстой"], correctAnswer: "Гоголь", hint: "Н.В. Гоголь" },
      { type: 'quiz', question: "\"Отцы и ...\" - роман Тургенева", options: ["существительное", "дети", "наречие", "прилагательное", "глагол"], correctAnswer: "дети", hint: "И.С. Тургенев" },
      { type: 'quiz', question: "Что такое сказка?", options: ["Научная статья", "Стихотворение", "Выдуманная история", "Учебник", "Энциклопедия"], correctAnswer: "Выдуманная история", hint: "Сказка - вымышленный рассказ" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь литературу! 📚" }
  },
  {
    title: "Гражданская война",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Гражданская война в России:", options: ["1914-1918", "1917-1922", "1920-1925", "Не знаю", "Другой вариант"], correctAnswer: "1917-1922", hint: "После революции 1917 года" },
      { type: 'quiz', question: "Укажи стороны Гражданской войны:", options: ["Красные", "Синие", "Коричневые", "Не знаю", "Другой вариант"], correctAnswer: "Красные", hint: "Основные силы" },
      { type: 'quiz', question: "Кто возглавлял Красную армию?", options: ["Колчак", "Троцкий", "Деникин", "Пушкин", "Лермонтов"], correctAnswer: "Троцкий", hint: "Л.Д. Троцкий" },
      { type: 'quiz', question: "Комуч - это:", options: ["Комитет учительства", "Комитет членов Учредительного собрания", "Коммунальный комитет", "Не знаю", "Другой вариант"], correctAnswer: "Комитет членов Учредительного собрания", hint: "Самара, 1918" },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь историю! ⚔️" }
  },
  {
    title: "СССР в 1920-30-е годы",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "НЭП - это:", options: ["Национализация", "Новая экономическая политика", "Народное образование", "Не знаю", "Другой вариант"], correctAnswer: "Новая экономическая политика", hint: "1921-1928 годы" },
      { type: 'quiz', question: "Коллективизация - это:", options: ["Создание колхозов", "Индустриализация", "Национализация", "Не знаю", "Другой вариант"], correctAnswer: "Создание колхозов", hint: "Объединение крестьянских хозяйств" },
      { type: 'quiz', question: "Укажи итоги индустриализации:", options: ["Строительство заводов", "Раскулачивание", "Коллективизация", "Не знаю", "Другой вариант"], correctAnswer: "Строительство заводов", hint: "Результаты индустриализации" },
      { type: 'quiz', question: "\"Год великого перелома\" - ... год", options: ["1931", "1924", "1929", "1927", "1919"], correctAnswer: "1929", hint: "Начало форсированной индустриализации" },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь историю СССР! 🏛️" }
  },
  {
    title: "Кислоты и основания",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: "Формула серной кислоты:", options: ["HCl", "H₂SO₄", "HNO₃", "Не знаю", "Другой вариант"], correctAnswer: "H₂SO₄", hint: "Серная кислота" },
      { type: 'quiz', question: "pH нейтральной среды:", options: ["0", "7", "14", "Не знаю", "Другой вариант"], correctAnswer: "7", hint: "Нейтральная среда = pH 7" },
      { type: 'quiz', question: "Укажи кислоты:", options: ["HCl", "NaOH", "KOH", "Не знаю", "Другой вариант"], correctAnswer: "HCl", hint: "Кислоты содержат H⁺" },
      { type: 'quiz', question: "Кислота + основание = ... + вода", options: ["соль", "существительное", "прилагательное", "наречие", "глагол"], correctAnswer: "соль", hint: "Реакция нейтрализации" },
      { type: 'quiz', question: "Из чего состоит молекула воды?", options: ["H₂O", "CO₂", "NaCl", "O₂", "H₂"], correctAnswer: "H₂O", hint: "Вода = H₂O" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь химию! 🧪" }
  },
  {
    title: "Законы Менделя",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Первый закон Менделя:", options: ["Расщепление", "Единообразие гибридов", "Независимое наследование", "Не знаю", "Другой вариант"], correctAnswer: "Единообразие гибридов", hint: "AA × aa → Aa (все одинаковые)" },
      { type: 'quiz', question: "При скрещивании Aa × Aa расщепление по фенотипу:", options: ["1:1", "1:2:1", "3:1", "Не знаю", "Другой вариант"], correctAnswer: "3:1", hint: "Второй закон Менделя" },
      { type: 'quiz', question: "Укажи термины генетики:", options: ["Ген", "Атом", "Молекула", "Не знаю", "Другой вариант"], correctAnswer: "Ген", hint: "Основные термины" },
      { type: 'quiz', question: "Гетерозигота - это ...", options: ["прилагательное", "глагол", "наречие", "Aa", "существительное"], correctAnswer: "Aa", hint: "Разные аллели" },
      { type: 'quiz', question: "Какое животное млекопитающее?", options: ["Лягушка 🐸", "Рыба 🐟", "Кошка 🐱", "Змея 🐍", "Ящерица 🦎"], correctAnswer: "Кошка 🐱", hint: "Млекопитающие кормят детёнышей молоком" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь генетику! 🧬" }
  }
]
