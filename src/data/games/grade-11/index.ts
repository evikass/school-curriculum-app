// Экспорт игр для 11 класса
import { GameLesson } from '../types'

export const eleventhGradeGames: GameLesson[] = [
  {
    title: "Интеграл",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Интеграл - это:", options: ["Производная", "Первобразная", "Скорость", "Не знаю", "Другой вариант"], correctAnswer: "Первообразная", hint: "Интегрирование - операция, обратная дифференцированию" },
      { type: 'quiz', question: "∫x²dx = x³/... + C", options: ["3", "4", "2", "5", "1"], correctAnswer: "3", hint: "∫xⁿdx = xⁿ⁺¹/(n+1)" },
      { type: 'quiz', question: "∫cos(x)dx = ?", options: ["sin(x) + C", "-sin(x) + C", "cos(x) + C", "Не знаю", "Другой вариант"], correctAnswer: "sin(x) + C", hint: "Производная синуса - косинус" },
      { type: 'quiz', question: "Формула Ньютона-Лейбница:", options: ["∫ᵃᵇf(x)dx = F(b) - F(a)", "∫ᵃᵇf(x)dx = F(a) - F(b)", "∫ᵃᵇf(x)dx = F(a) + F(b)", "Не знаю", "Другой вариант"], correctAnswer: "∫ᵃᵇf(x)dx = F(b) - F(a)", hint: "Определённый интеграл через первообразную" },
      { type: 'quiz', question: "Чему равно 2 + 2?", options: ["3", "4", "5", "6", "8"], correctAnswer: "4", hint: "2 + 2 = 4" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь интегралы! 📐" }
  },
  {
    title: "Логарифмы",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "log₂8 = ... (2 в какой степени = 8?)", options: ["4", "1", "2", "3", "5"], correctAnswer: "3", hint: "2³ = 8" },
      { type: 'quiz', question: "logₐa = ?", options: ["0", "1", "a", "Не знаю", "Другой вариант"], correctAnswer: "1", hint: "a¹ = a" },
      { type: 'quiz', question: "logₐ1 = ?", options: ["0", "1", "a", "Не знаю", "Другой вариант"], correctAnswer: "0", hint: "a⁰ = 1" },
      { type: 'quiz', question: "logₐ(xy) = ?", options: ["logₐx + logₐy", "logₐx · logₐy", "logₐx - logₐy", "Не знаю", "Другой вариант"], correctAnswer: "logₐx + logₐy", hint: "Логарифм произведения = сумма логарифмов" },
      { type: 'quiz', question: "Чему равно 2 + 2?", options: ["3", "4", "5", "6", "8"], correctAnswer: "4", hint: "2 + 2 = 4" },
    ],
    reward: { stars: 3, message: "Супер! Ты работаешь с логарифмами! 🔢" }
  },
  {
    title: "Комплексные числа",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "i² = ?", options: ["-1", "1", "0", "Не знаю", "Другой вариант"], correctAnswer: "-1", hint: "i = √(-1), i² = -1" },
      { type: 'quiz', question: "(3 + 2i) + (1 + 4i) = ... + 6i", options: ["4", "6", "2", "5", "3"], correctAnswer: "4", hint: "Складываем действительные части: 3 + 1" },
      { type: 'quiz', question: "Мнимая единица i = ?", options: ["√1", "√(-1)", "√0", "Не знаю", "Другой вариант"], correctAnswer: "√(-1)", hint: "i = √(-1)" },
      { type: 'quiz', question: "Комплексное число a + bi содержит:", options: ["Только действительную часть", "Только мнимую часть", "Обе части", "1", "2"], correctAnswer: "Обе части", hint: "a - действительная, bi - мнимая часть" },
      { type: 'quiz', question: "Чему равно 2 + 2?", options: ["3", "4", "5", "6", "8"], correctAnswer: "4", hint: "2 + 2 = 4" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь комплексные числа! 📊" }
  },
  {
    title: "Тела вращения",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Цилиндр получается вращением:", options: ["Треугольника", "Прямоугольника", "Круга", "Не знаю", "Другой вариант"], correctAnswer: "Прямоугольника", hint: "Вращение прямоугольника вокруг стороны" },
      { type: 'quiz', question: "Объём цилиндра V = πr²h. Если r=2, h=5, то V = ...π", options: ["20", "21", "18", "22", "19"], correctAnswer: "20", hint: "V = π · 4 · 5 = 20π" },
      { type: 'quiz', question: "Конус получается вращением:", options: ["Прямоугольника", "Треугольника", "Круга", "Не знаю", "Другой вариант"], correctAnswer: "Треугольника", hint: "Вращение прямоугольного треугольника" },
      { type: 'quiz', question: "Объём конуса:", options: ["πr²h", "(1/3)πr²h", "(4/3)πr³", "Не знаю", "Другой вариант"], correctAnswer: "(1/3)πr²h", hint: "V = 1/3 · πr² · h" },
      { type: 'quiz', question: "Сколько сторон у квадрата?", options: ["3", "4", "5", "6", "2"], correctAnswer: "4", hint: "Квадрат имеет 4 стороны" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тела вращения! ⭕" }
  },
  {
    title: "Координаты и векторы в пространстве",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Расстояние между точками A(0,0,0) и B(3,4,0) = ...", options: ["3", "4", "5", "7", "6"], correctAnswer: "5", hint: "√(3² + 4² + 0²) = 5" },
      { type: 'quiz', question: "Скалярное произведение векторов a·b = ?", options: ["|a| × |b|", "|a| × |b| × cos α", "|a| + |b|", "Пушкин", "Лермонтов"], correctAnswer: "|a| × |b| × cos α", hint: "Через модули и косинус угла" },
      { type: 'quiz', question: "Вектор a(1,2,3), вектор b(2,1,1). a·b = ...", options: ["5", "9", "6", "7", "8"], correctAnswer: "7", hint: "1·2 + 2·1 + 3·1 = 7" },
      { type: 'quiz', question: "Если скалярное произведение = 0, то векторы:", options: ["Коллинеарны", "Перпендикулярны", "Равны", "Пушкин", "Лермонтов"], correctAnswer: "Перпендикулярны", hint: "a·b = 0 → cos 90° = 0" },
      { type: 'quiz', question: "Сколько сторон у квадрата?", options: ["3", "4", "5", "6", "2"], correctAnswer: "4", hint: "Квадрат имеет 4 стороны" },
    ],
    reward: { stars: 3, message: "Супер! Ты работаешь в пространстве! 📏" }
  },
  {
    title: "Нормы языка",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Орфоэпические нормы - это:", options: ["Правила написания", "Правила произношения", "Правила образования слов", "Не знаю", "Другой вариант"], correctAnswer: "Правила произношения", hint: "Орфоэпия = произношение" },
      { type: 'quiz', question: "Грамматические нормы регулируют:", options: ["Произношение", "Образование форм слов", "Написание", "Не знаю", "Другой вариант"], correctAnswer: "Образование форм слов", hint: "Склонение, спряжение" },
      { type: 'quiz', question: "Укажи языковые нормы:", options: ["Орфоэпические", "Математические", "Физические", "Не знаю", "Другой вариант"], correctAnswer: "Орфоэпические", hint: "Основные нормы литературного языка" },
      { type: 'quiz', question: "Лексические нормы - это:", options: ["Правила произношения", "Правила употребления слов", "Правила написания", "Не знаю", "Другой вариант"], correctAnswer: "Правила употребления слов", hint: "Правильное использование слов" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь нормы языка! 📝" }
  },
  {
    title: "Серебряный век",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Серебряный век - это период:", options: ["XIX века", "Конца XIX - начала XX века", "XX века", "Не знаю", "Другой вариант"], correctAnswer: "Конца XIX - начала XX века", hint: "1890-1917 годы" },
      { type: 'quiz', question: "Укажи поэтов Серебряного века:", options: ["Блок", "Пушкин", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Блок", hint: "Поэты рубежа XIX-XX веков" },
      { type: 'quiz', question: "Символизм - это направление:", options: ["Реалистическое", "Модернистское", "Классическое", "Не знаю", "Другой вариант"], correctAnswer: "Модернистское", hint: "Символизм - течение модернизма" },
      { type: 'quiz', question: "Акмеизм противопоставлялся:", options: ["Реализму", "Символизму", "Классицизму", "Не знаю", "Другой вариант"], correctAnswer: "Символизму", hint: "Акмеисты отказались от символизма" },
      { type: 'quiz', question: "Что такое сказка?", options: ["Научная статья", "Стихотворение", "Выдуманная история", "Учебник", "Энциклопедия"], correctAnswer: "Выдуманная история", hint: "Сказка - вымышленный рассказ" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь Серебряный век! 📖" }
  },
  {
    title: "Литература XX века",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "М.А. Булгаков написал:", options: ["Тихий Дон", "Мастер и Маргарита", "Доктор Живаго", "Пушкин", "Лермонтов"], correctAnswer: "Мастер и Маргарита", hint: "Роман о любви и творчестве" },
      { type: 'quiz', question: "Укажи писателей XX века:", options: ["Шолохов", "Толстой", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Шолохов", hint: "Русская литература XX века" },
      { type: 'quiz', question: "\"Тихий Дон\" - автор:", options: ["Булгаков", "Шолохов", "Пастернак", "Пушкин", "Лермонтов"], correctAnswer: "Шолохов", hint: "Шолохов - нобелевский лауреат" },
      { type: 'quiz', question: "\"Доктор Живаго\" - автор:", options: ["Булгаков", "Шолохов", "Пастернак", "Пушкин", "Лермонтов"], correctAnswer: "Пастернак", hint: "Пастернак - нобелевский лауреат" },
      { type: 'quiz', question: "Что такое сказка?", options: ["Научная статья", "Стихотворение", "Выдуманная история", "Учебник", "Энциклопедия"], correctAnswer: "Выдуманная история", hint: "Сказка - вымышленный рассказ" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь литературу XX века! 📚" }
  },
  {
    title: "Холодная война",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "\"Холодная война\" началась после:", options: ["Первой мировой", "Второй мировой", "Революции 1917", "Не знаю", "Другой вариант"], correctAnswer: "Второй мировой", hint: "Противостояние СССР и США" },
      { type: 'quiz', question: "Фултонская речь Черчилля:", options: ["1945", "1946", "1947", "Не знаю", "Другой вариант"], correctAnswer: "1946", hint: "1946 год - начало \"холодной войны\"" },
      { type: 'quiz', question: "Укажи события \"холодной войны\":", options: ["Карибский кризис", "Вторая мировая", "Первая мировая", "Не знаю", "Другой вариант"], correctAnswer: "Карибский кризис", hint: "Глобальное противостояние" },
      { type: 'quiz', question: "Карибский кризис:", options: ["1960", "1962", "1965", "Не знаю", "Другой вариант"], correctAnswer: "1962", hint: "1962 год - ядерный кризис" },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь историю! ⚔️" }
  },
  {
    title: "Распад СССР",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Когда был распад СССР?", options: ["1989", "1991", "1993", "Не знаю", "Другой вариант"], correctAnswer: "1991", hint: "Декабрь 1991 года" },
      { type: 'quiz', question: "Первый президент России:", options: ["Горбачёв", "Ельцин", "Путин", "Не знаю", "Другой вариант"], correctAnswer: "Ельцин", hint: "Б.Н. Ельцин - первый президент РФ" },
      { type: 'quiz', question: "Укажи события перестройки:", options: ["Гласность", "Коллективизация", "Индустриализация", "Не знаю", "Другой вариант"], correctAnswer: "Гласность", hint: "Политика Горбачёва" },
      { type: 'quiz', question: "Последний лидер СССР:", options: ["Ельцин", "Горбачёв", "Андропов", "Не знаю", "Другой вариант"], correctAnswer: "Горбачёв", hint: "М.С. Горбачёв - последний генсек" },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь новейшую историю! 🏛️" }
  },
  {
    title: "Атомная физика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Кто открыл радиоактивность?", options: ["Резерфорд", "Беккерель", "Кюри", "Пушкин", "Лермонтов"], correctAnswer: "Беккерель", hint: "Анри Беккерель, 1896" },
      { type: 'quiz', question: "Альфа-излучение - это:", options: ["Поток электронов", "Поток ядер гелия", "Электромагнитные волны", "Не знаю", "Другой вариант"], correctAnswer: "Поток ядер гелия", hint: "α = ₂⁴He" },
      { type: 'quiz', question: "Укажи виды радиоактивного распада:", options: ["Альфа-распад", "Дельта-распад", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Альфа-распад", hint: "Три основных вида" },
      { type: 'quiz', question: "Формула Эйнштейна E = ?", options: ["mc", "mc²", "m²c", "Не знаю", "Другой вариант"], correctAnswer: "mc²", hint: "E = mc² - энергия и масса эквивалентны" },
      { type: 'quiz', question: "Что измеряется в метрах?", options: ["Время", "Масса", "Длина", "Температура", "Скорость"], correctAnswer: "Длина", hint: "Метр - единица длины" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь атомную физику! ⚛️" }
  },
  {
    title: "Квантовая физика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Квант - это:", options: ["Волна", "Порция энергии", "Частица", "Не знаю", "Другой вариант"], correctAnswer: "Порция энергии", hint: "E = hν - энергия кванта" },
      { type: 'quiz', question: "Постоянная Планка обозначается:", options: ["c", "h", "ν", "Не знаю", "Другой вариант"], correctAnswer: "h", hint: "h ≈ 6.63 × 10⁻³⁴ Дж·с" },
      { type: 'quiz', question: "E = hν, где ν - это ... (частота)", options: ["частота", "глагол", "прилагательное", "существительное", "наречие"], correctAnswer: "частота", hint: "Греческая буква ню" },
      { type: 'quiz', question: "Фотоэффект открыл:", options: ["Эйнштейн", "Столетов", "Планк", "Не знаю", "Другой вариант"], correctAnswer: "Столетов", hint: "А.Г. Столетов изучал фотоэффект" },
      { type: 'quiz', question: "Что измеряется в метрах?", options: ["Время", "Масса", "Длина", "Температура", "Скорость"], correctAnswer: "Длина", hint: "Метр - единица длины" },
    ],
    reward: { stars: 3, message: "Супер! Ты понимаешь квантовую физику! 🔬" }
  },
  {
    title: "Химическая кинетика",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: "Скорость химической реакции измеряется в:", options: ["моль/л·с", "г/см³", "м/с", "Не знаю", "Другой вариант"], correctAnswer: "моль/л·с", hint: "Изменение концентрации в единицу времени" },
      { type: 'quiz', question: "При повышении температуры скорость реакции:", options: ["Уменьшается", "Увеличивается", "Не меняется", "Не знаю", "Другой вариант"], correctAnswer: "Увеличивается", hint: "Правило Вант-Гоффа" },
      { type: 'quiz', question: "Укажи факторы, влияющие на скорость:", options: ["Температура", "Объём", "Пушкин", "Лермонтов", "Гоголь"], correctAnswer: "Температура", hint: "Факторы скорости реакции" },
      { type: 'quiz', question: "Катализатор:", options: ["Расходуется в реакции", "Не расходуется", "Замедляет реакцию", "Не знаю", "Другой вариант"], correctAnswer: "Не расходуется", hint: "Катализатор ускоряет, но не расходуется" },
      { type: 'quiz', question: "Из чего состоит молекула воды?", options: ["H₂O", "CO₂", "NaCl", "O₂", "H₂"], correctAnswer: "H₂O", hint: "Вода = H₂O" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь кинетику! 🧪" }
  },
  {
    title: "Экология",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Экология изучает:", options: ["Клетки", "Взаимоотношения организмов", "Молекулы", "Не знаю", "Другой вариант"], correctAnswer: "Взаимоотношения организмов", hint: "Экология - наука о связях в природе" },
      { type: 'quiz', question: "Укажи уровни организации жизни:", options: ["Клеточный", "Молекулярный", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Клеточный", hint: "Уровни организации живого" },
      { type: 'quiz', question: "Пищевая цепь начинается с:", options: ["Хищников", "Производителей", "Разлагателей", "Не знаю", "Другой вариант"], correctAnswer: "Производителей", hint: "Растения - производители" },
      { type: 'quiz', question: "Биосфера - это:", options: ["Часть Земли с жизнью", "Атмосфера", "Гидросфера", "Не знаю", "Другой вариант"], correctAnswer: "Часть Земли с жизнью", hint: "По Вернадскому - оболочка Земли с жизнью" },
      { type: 'quiz', question: "Какое животное млекопитающее?", options: ["Лягушка 🐸", "Рыба 🐟", "Кошка 🐱", "Змея 🐍", "Ящерица 🦎"], correctAnswer: "Кошка 🐱", hint: "Млекопитающие кормят детёнышей молоком" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь экологию! 🌿" }
  },
  {
    title: "Academic English",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Essay structure includes:", options: ["Introduction, Body, Conclusion", "Only Body", "Introduction only", "Не знаю", "Другой вариант"], correctAnswer: "Introduction, Body, Conclusion", hint: "Три части эссе" },
      { type: 'quiz', question: "Укажи linking words:", options: ["However", "Beautiful", "Quickly", "Не знаю", "Другой вариант"], correctAnswer: "However", hint: "Слова-связки для эссе" },
      { type: 'quiz', question: "\"In conclusion\" используется:", options: ["В начале", "В конце", "В середине", "Не знаю", "Другой вариант"], correctAnswer: "В конце", hint: "In conclusion = в заключение" },
      { type: 'quiz', question: "On the one hand... on the ... hand...", options: ["существительное", "other", "прилагательное", "наречие", "глагол"], correctAnswer: "other", hint: "С одной стороны... с другой стороны" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Excellent! Ты готов к академическому английскому! 🇬🇧" }
  },
  {
    title: "Phrasal Verbs",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "\"Give up\" means:", options: ["Start", "Stop trying", "Continue", "Не знаю", "Другой вариант"], correctAnswer: "Stop trying", hint: "Give up = бросить, отказаться" },
      { type: 'quiz', question: "\"Look after\" means:", options: ["Search", "Take care of", "Watch", "Не знаю", "Другой вариант"], correctAnswer: "Take care of", hint: "Look after = присматривать" },
      { type: 'quiz', question: "Укажи фразовые глаголы:", options: ["Look up", "Beautiful house", "Very quickly", "Не знаю", "Другой вариант"], correctAnswer: "Look up", hint: "Фразовые глаголы = глагол + предлог" },
      { type: 'quiz', question: "Turn ... the light, please. (off/on)", options: ["off", "наречие", "существительное", "глагол", "прилагательное"], correctAnswer: "off", hint: "Turn off = выключить" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Great! Ты знаешь фразовые глаголы! 🔄" }
  },
  {
    title: "Определённый интеграл",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "∫₀² x dx = ... (по формуле Ньютона-Лейбница)", options: ["2", "0", "4", "3", "1"], correctAnswer: "2", hint: "x²/2 от 0 до 2 = 4/2 - 0 = 2" },
      { type: 'quiz', question: "Площадь под графиком f(x) от a до b:", options: ["f(b) - f(a)", "∫ₐᵇ f(x)dx", "f\'(x)", "Не знаю", "Другой вариант"], correctAnswer: "∫ₐᵇ f(x)dx", hint: "Определённый интеграл = площадь" },
      { type: 'quiz', question: "∫₀¹ 2x dx = ...", options: ["1", "3", "2", "0", "4"], correctAnswer: "1", hint: "x² от 0 до 1 = 1 - 0 = 1" },
      { type: 'quiz', question: "Интеграл от константы C:", options: ["Cx + C", "C", "Cx", "Не знаю", "Другой вариант"], correctAnswer: "Cx + C", hint: "∫C dx = Cx + C₁" },
      { type: 'quiz', question: "Чему равно 2 + 2?", options: ["3", "4", "5", "6", "8"], correctAnswer: "4", hint: "2 + 2 = 4" },
    ],
    reward: { stars: 3, message: "Отлично! Ты работаешь с интегралами! 📐" }
  },
  {
    title: "Дифференциальные уравнения",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Дифференциальное уравнение содержит:", options: ["Только функцию", "Функцию и её производные", "Только производные", "Не знаю", "Другой вариант"], correctAnswer: "Функцию и её производные", hint: "Уравнение с производными" },
      { type: 'quiz', question: "Решение y\' = kx:", options: ["y = kx", "y = kx²/2 + C", "y = k", "Не знаю", "Другой вариант"], correctAnswer: "y = kx²/2 + C", hint: "Интегрируем обе части" },
      { type: 'quiz', question: "y\' = 5, тогда y = 5x + ...", options: ["C", "прилагательное", "существительное", "глагол", "наречие"], correctAnswer: "C", hint: "Произвольная постоянная" },
      { type: 'quiz', question: "Порядок дифференциального уравнения определяется:", options: ["Старшей степенью", "Старшей производной", "Количеством переменных", "Не знаю", "Другой вариант"], correctAnswer: "Старшей производной", hint: "Порядок = наивысший порядок производной" },
      { type: 'quiz', question: "Чему равно 2 + 2?", options: ["3", "4", "5", "6", "8"], correctAnswer: "4", hint: "2 + 2 = 4" },
    ],
    reward: { stars: 3, message: "Супер! Ты понимаешь дифференциальные уравнения! 🔢" }
  },
  {
    title: "Оптика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Закон преломления света:", options: ["sin α = sin β", "sin α / sin β = n", "α = β", "Не знаю", "Другой вариант"], correctAnswer: "sin α / sin β = n", hint: "Закон Снеллиуса" },
      { type: 'quiz', question: "Угол падения ... углу отражения", options: ["наречие", "существительное", "прилагательное", "равен", "глагол"], correctAnswer: "равен", hint: "Закон отражения" },
      { type: 'quiz', question: "Показатель преломления стекла:", options: ["≈ 1", "≈ 1.5", "≈ 2", "Не знаю", "Другой вариант"], correctAnswer: "≈ 1.5", hint: "Стекло преломляет свет" },
      { type: 'quiz', question: "Укажи оптические явления:", options: ["Преломление", "Испарение", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Преломление", hint: "Явления, связанные со светом" },
      { type: 'quiz', question: "Что измеряется в метрах?", options: ["Время", "Масса", "Длина", "Температура", "Скорость"], correctAnswer: "Длина", hint: "Метр - единица длины" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь оптику! 💡" }
  },
  {
    title: "Ядерная физика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Ядро состоит из:", options: ["Протонов и электронов", "Протонов и нейтронов", "Только протонов", "Не знаю", "Другой вариант"], correctAnswer: "Протонов и нейтронов", hint: "Нуклоны = протоны + нейтроны" },
      { type: 'quiz', question: "Массовое число A = Z + N, где Z - протоны, N - ...", options: ["глагол", "существительное", "прилагательное", "нейтроны", "наречие"], correctAnswer: "нейтроны", hint: "N = количество нейтронов" },
      { type: 'quiz', question: "Альфа-распад:", options: ["Вылет электрона", "Вылет ядра гелия", "Вылет нейтрона", "Не знаю", "Другой вариант"], correctAnswer: "Вылет ядра гелия", hint: "₂⁴He" },
      { type: 'quiz', question: "Бета-распад:", options: ["Вылет электрона", "Вылет ядра гелия", "Вылет протона", "Не знаю", "Другой вариант"], correctAnswer: "Вылет электрона", hint: "Превращение нейтрона в протон" },
      { type: 'quiz', question: "Что измеряется в метрах?", options: ["Время", "Масса", "Длина", "Температура", "Скорость"], correctAnswer: "Длина", hint: "Метр - единица длины" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь ядерную физику! ⚛️" }
  },
  {
    title: "Общая химия",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: "Окислительно-восстановительные реакции:", options: ["Без изменения степеней", "С изменением степеней окисления", "Только с кислородом", "Не знаю", "Другой вариант"], correctAnswer: "С изменением степеней окисления", hint: "ОВР = передача электронов" },
      { type: 'quiz', question: "Укажи окислители:", options: ["O₂", "H₂", "Na", "Не знаю", "Другой вариант"], correctAnswer: "O₂", hint: "Окислители принимают электроны" },
      { type: 'quiz', question: "В реакции Zn + 2HCl → ZnCl₂ + H₂ окислитель - ...", options: ["существительное", "прилагательное", "глагол", "HCl", "наречие"], correctAnswer: "HCl", hint: "Водород принимает электроны" },
      { type: 'quiz', question: "Электролиз - это:", options: ["Разложение током", "Нагревание", "Окисление", "Не знаю", "Другой вариант"], correctAnswer: "Разложение током", hint: "Незапланированное разложение вещества током" },
      { type: 'quiz', question: "Из чего состоит молекула воды?", options: ["H₂O", "CO₂", "NaCl", "O₂", "H₂"], correctAnswer: "H₂O", hint: "Вода = H₂O" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь химию! 🧪" }
  },
  {
    title: "Биосфера и экология",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Автор учения о биосфере:", options: ["Дарвин", "Вернадский", "Менделеев", "Пушкин", "Лермонтов"], correctAnswer: "Вернадский", hint: "В.И. Вернадский" },
      { type: 'quiz', question: "Укажи функции биосферы:", options: ["Газовая", "Механическая", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Газовая", hint: "Функции живого вещества" },
      { type: 'quiz', question: "Красная книга содержит:", options: ["Все виды", "Редкие и исчезающие виды", "Опасные виды", "Не знаю", "Другой вариант"], correctAnswer: "Редкие и исчезающие виды", hint: "Охрана природы" },
      { type: 'quiz', question: "Биосфера - оболочка Земли, заселённая ... организмами", options: ["наречие", "существительное", "прилагательное", "глагол", "живыми"], correctAnswer: "живыми", hint: "Сфера жизни" },
      { type: 'quiz', question: "Какое животное млекопитающее?", options: ["Лягушка 🐸", "Рыба 🐟", "Кошка 🐱", "Змея 🐍", "Ящерица 🦎"], correctAnswer: "Кошка 🐱", hint: "Млекопитающие кормят детёнышей молоком" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь экологию! 🌍" }
  },
  {
    title: "Россия в 90-е годы",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Конституция 1993 года принята:", options: ["12 декабря", "12 июня", "7 ноября", "Не знаю", "Другой вариант"], correctAnswer: "12 декабря", hint: "День Конституции" },
      { type: 'quiz', question: "Укажи события 90-х:", options: ["Приватизация", "Крым 2014", "Олимпиада 2014", "Не знаю", "Другой вариант"], correctAnswer: "Приватизация", hint: "Россия в переходный период" },
      { type: 'quiz', question: "Приватизация в России началась в:", options: ["1990", "1992", "1995", "Не знаю", "Другой вариант"], correctAnswer: "1992", hint: "Ваучерная приватизация" },
      { type: 'quiz', question: "Дефолт в России произошёл в:", options: ["1995", "1998", "2000", "Не знаю", "Другой вариант"], correctAnswer: "1998", hint: "17 августа 1998" },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь новейшую историю! 🏛️" }
  },
  {
    title: "Reported Speech",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "\"I am happy\" → He said he __ happy.", options: ["is", "was", "will be", "Не знаю", "Другой вариант"], correctAnswer: "was", hint: "Смещение времён: Present → Past" },
      { type: 'quiz', question: "\"I will come\" → She said she ... come.", options: ["прилагательное", "наречие", "глагол", "would", "существительное"], correctAnswer: "would", hint: "Will → would" },
      { type: 'quiz', question: "\"I can swim\" → He said he __ swim.", options: ["can", "could", "will", "Не знаю", "Другой вариант"], correctAnswer: "could", hint: "Can → could" },
      { type: 'quiz', question: "Укажи изменения в косвенной речи:", options: ["Here → There", "Tomorrow → Yesterday", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Here → There", hint: "Смещение местоимений и наречий" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Excellent! Ты знаешь косвенную речь! 🇬🇧" }
  },
  {
    title: "Тригонометрические уравнения",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "sin x = 0, x = ?", options: ["πn", "π/2 + πn", "2πn", "Не знаю", "Другой вариант"], correctAnswer: "πn", hint: "sin x = 0 при x = πn" },
      { type: 'quiz', question: "cos x = 1, x = ...n", options: ["4", "3", "1", "2π", "0"], correctAnswer: "2π", hint: "cos x = 1 при x = 2πn" },
      { type: 'quiz', question: "tg x = 0, x = ?", options: ["πn", "π/2 + πn", "2πn", "Не знаю", "Другой вариант"], correctAnswer: "πn", hint: "tg x = 0 при x = πn" },
      { type: 'quiz', question: "sin x = 1/2, x = ?", options: ["π/6 + 2πn", "π/3 + 2πn", "π/4 + 2πn", "Не знаю", "Другой вариант"], correctAnswer: "π/6 + 2πn", hint: "sin 30° = 1/2" },
      { type: 'quiz', question: "Чему равно 2 + 2?", options: ["3", "4", "5", "6", "8"], correctAnswer: "4", hint: "2 + 2 = 4" },
    ],
    reward: { stars: 3, message: "Отлично! Ты решаешь тригонометрические уравнения! 📐" }
  },
  {
    title: "Комбинации тел",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Шар вписан в куб. Диаметр шара равен:", options: ["Стороне куба", "Диагонали куба", "Половине стороны", "Не знаю", "Другой вариант"], correctAnswer: "Стороне куба", hint: "Шар касается всех граней" },
      { type: 'quiz', question: "Конус вписан в цилиндр. Их высоты:", options: ["Разные", "Одинаковые", "Зависит от размера", "Не знаю", "Другой вариант"], correctAnswer: "Одинаковые", hint: "Конус касается оснований цилиндра" },
      { type: 'quiz', question: "Если радиус шара = 3, то объём = ...π (4/3πr³)", options: ["36", "31", "34", "38", "26"], correctAnswer: "36", hint: "V = 4/3 × π × 27 = 36π" },
      { type: 'quiz', question: "Сфера вписана в куб со стороной a. Радиус сферы:", options: ["a", "a/2", "a√2", "Не знаю", "Другой вариант"], correctAnswer: "a/2", hint: "Диаметр = a" },
      { type: 'quiz', question: "Сколько сторон у квадрата?", options: ["3", "4", "5", "6", "2"], correctAnswer: "4", hint: "Квадрат имеет 4 стороны" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь комбинации тел! 📦" }
  },
  {
    title: "Изобразительные средства",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "\"Золотые руки\" - это:", options: ["Эпитет", "Метафора", "Сравнение", "Не знаю", "Другой вариант"], correctAnswer: "Метафора", hint: "Скрытое сравнение" },
      { type: 'quiz', question: "\"Как лев, он был смел\" - это:", options: ["Метафора", "Эпитет", "Сравнение", "Не знаю", "Другой вариант"], correctAnswer: "Сравнение", hint: "Сравнение с союзом \"как\"" },
      { type: 'quiz', question: "Укажи эпитеты:", options: ["Золотая осень", "Шёпот листьев", "Бежит быстро", "Не знаю", "Другой вариант"], correctAnswer: "Золотая осень", hint: "Образные определения" },
      { type: 'quiz', question: "\"Шёпот листьев\" - это:", options: ["Метафора", "Олицетворение", "Эпитет", "Не знаю", "Другой вариант"], correctAnswer: "Олицетворение", hint: "Наделение предметов свойствами живых" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь изобразительные средства! ✨" }
  },
  {
    title: "Постмодернизм",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Постмодернизм характеризуется:", options: ["Чётким сюжетом", "Игрой с текстом", "Простотой", "Не знаю", "Другой вариант"], correctAnswer: "Игрой с текстом", hint: "Интертекстуальность, ирония" },
      { type: 'quiz', question: "Укажи черты постмодернизма:", options: ["Интертекстуальность", "Реализм", "Чёткий сюжет", "Не знаю", "Другой вариант"], correctAnswer: "Интертекстуальность", hint: "Особенности постмодернизма" },
      { type: 'quiz', question: "Постмодернизм возник:", options: ["В XIX веке", "Во второй половине XX века", "В XXI веке", "Не знаю", "Другой вариант"], correctAnswer: "Во второй половине XX века", hint: "1960-е годы" },
      { type: 'quiz', question: "\"Школа для дураков\" - автор:", options: ["Пелевин", "Соколов", "Сорокин", "Пушкин", "Лермонтов"], correctAnswer: "Соколов", hint: "Саша Соколов - постмодернист" },
      { type: 'quiz', question: "Что такое сказка?", options: ["Научная статья", "Стихотворение", "Выдуманная история", "Учебник", "Энциклопедия"], correctAnswer: "Выдуманная история", hint: "Сказка - вымышленный рассказ" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь постмодернизм! 📖" }
  },
  {
    title: "Современная Россия",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Крым вошёл в состав России:", options: ["2010", "2014", "2018", "Не знаю", "Другой вариант"], correctAnswer: "2014", hint: "Март 2014 года" },
      { type: 'quiz', question: "Укажи события современной России:", options: ["Олимпиада Сочи 2014", "Конституция 1993", "Перестройка", "Не знаю", "Другой вариант"], correctAnswer: "Олимпиада Сочи 2014", hint: "События после 2000 года" },
      { type: 'quiz', question: "Олимпиада в Сочи прошла в:", options: ["2010", "2014", "2018", "Не знаю", "Другой вариант"], correctAnswer: "2014", hint: "Зимняя олимпиада" },
      { type: 'quiz', question: "Конституция РФ принята в ... году", options: ["1988", "1995", "1993", "1983", "1991"], correctAnswer: "1993", hint: "12 декабря 1993" },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь современную историю! 🇷🇺" }
  },
  {
    title: "Термодинамика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Первый закон термодинамики:", options: ["Q = A", "Q = ΔU + A", "ΔU = Q", "Не знаю", "Другой вариант"], correctAnswer: "Q = ΔU + A", hint: "Количество теплоты = изменение внутренней энергии + работа" },
      { type: 'quiz', question: "Адиабатный процесс:", options: ["При постоянной температуре", "Без теплообмена", "При постоянном давлении", "Не знаю", "Другой вариант"], correctAnswer: "Без теплообмена", hint: "Q = 0" },
      { type: 'quiz', question: "Укажи изопроцессы:", options: ["Изотермический", "Изотопный", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Изотермический", hint: "Процессы при постоянном параметре" },
      { type: 'quiz', question: "КПД = (Q₁ - Q₂) / ...", options: ["существительное", "прилагательное", "глагол", "Q₁", "наречие"], correctAnswer: "Q₁", hint: "КПД = полезная работа / затраченная энергия" },
      { type: 'quiz', question: "Что измеряется в метрах?", options: ["Время", "Масса", "Длина", "Температура", "Скорость"], correctAnswer: "Длина", hint: "Метр - единица длины" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь термодинамику! ⚛️" }
  },
  {
    title: "Генетика человека",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Человек имеет хромосом:", options: ["23", "46", "48", "Не знаю", "Другой вариант"], correctAnswer: "46", hint: "23 пары хромосом" },
      { type: 'quiz', question: "Пол человека определяется:", options: ["X-хромосомой", "Y-хромосомой", "Обеими", "Не знаю", "Другой вариант"], correctAnswer: "Y-хромосомой", hint: "XY = мужчина, XX = женщина" },
      { type: 'quiz', question: "Укажи наследственные заболевания:", options: ["Гемофилия", "Грипп", "Простуда", "Не знаю", "Другой вариант"], correctAnswer: "Гемофилия", hint: "Генетические нарушения" },
      { type: 'quiz', question: "Гемофилия - ...-сцепленное заболевание", options: ["наречие", "прилагательное", "существительное", "глагол", "X"], correctAnswer: "X", hint: "Ген в X-хромосоме" },
      { type: 'quiz', question: "Какое животное млекопитающее?", options: ["Лягушка 🐸", "Рыба 🐟", "Кошка 🐱", "Змея 🐍", "Ящерица 🦎"], correctAnswer: "Кошка 🐱", hint: "Млекопитающие кормят детёнышей молоком" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь генетику! 🧬" }
  },
  {
    title: "Mixed Conditionals",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "If I __ (study) harder yesterday, I would pass now.", options: ["studied", "had studied", "study", "Не знаю", "Другой вариант"], correctAnswer: "had studied", hint: "Mixed: Past Perfect + would + V" },
      { type: 'quiz', question: "If she __ (be) rich, she would have bought it.", options: ["is", "were", "had been", "Не знаю", "Другой вариант"], correctAnswer: "were", hint: "Mixed: Second + Third" },
      { type: 'quiz', question: "If I knew her, I ... (say) hello yesterday. (would have said)", options: ["существительное", "прилагательное", "наречие", "глагол", "would have said"], correctAnswer: "would have said", hint: "Present unreal + Past unreal" },
      { type: 'quiz', question: "Укажи типы conditionals:", options: ["Zero", "Не знаю", "Другой вариант", "Ни один из этих", "Все перечисленные"], correctAnswer: "Zero", hint: "Пять типов условных предложений" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Excellent! Ты знаешь смешанные условия! 🇬🇧" }
  },
  {
    title: "Право",
    subject: "Обществознание",
    icon: "Scale",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Конституция - это:", options: ["Обычный закон", "Основной закон государства", "Указ президента", "Не знаю", "Другой вариант"], correctAnswer: "Основной закон государства", hint: "Конституция имеет высшую юридическую силу" },
      { type: 'quiz', question: "Правоспособность возникает с:", options: ["Рождения", "14 лет", "18 лет", "Не знаю", "Другой вариант"], correctAnswer: "Рождения", hint: "Способность иметь права" },
      { type: 'quiz', question: "Укажи права человека:", options: ["Право на жизнь", "Право нарушать закон", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Право на жизнь", hint: "Естественные права человека" },
      { type: 'quiz', question: "Дееспособность в полном объёме наступает с:", options: ["14 лет", "16 лет", "18 лет", "Не знаю", "Другой вариант"], correctAnswer: "18 лет", hint: "Совершеннолетие = полная дееспособность" },
      { type: 'quiz', question: "Что такое закон?", options: ["Совет", "Правило, обязательное для всех", "Пожелание", "Просьба", "Рекомендация"], correctAnswer: "Правило, обязательное для всех", hint: "Закон обязателен для исполнения" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь основы права! ⚖️" }
  },
  {
    title: "Экономика",
    subject: "Обществознание",
    icon: "Scale",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Инфляция - это:", options: ["Снижение цен", "Повышение общего уровня цен", "Стабильность цен", "Не знаю", "Другой вариант"], correctAnswer: "Повышение общего уровня цен", hint: "Обесценивание денег" },
      { type: 'quiz', question: "Спрос и предложение определяют:", options: ["Только предложение", "Рыночную цену", "Только спрос", "Не знаю", "Другой вариант"], correctAnswer: "Рыночную цену", hint: "Закон спроса и предложения" },
      { type: 'quiz', question: "Укажи факторы производства:", options: ["Труд", "Деньги", "Пушкин", "Лермонтов", "Гоголь"], correctAnswer: "Труд", hint: "Ресурсы для производства" },
      { type: 'quiz', question: "Безработица - это отсутствие ... у трудоспособного населения", options: ["существительное", "наречие", "работы", "глагол", "прилагательное"], correctAnswer: "работы", hint: "Трудоспособные люди без работы" },
      { type: 'quiz', question: "Что такое закон?", options: ["Совет", "Правило, обязательное для всех", "Пожелание", "Просьба", "Рекомендация"], correctAnswer: "Правило, обязательное для всех", hint: "Закон обязателен для исполнения" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь экономику! 💰" }
  },
  {
    title: "География России",
    subject: "География",
    icon: "Map",
    color: "text-teal-400",
    tasks: [
      { type: 'quiz', question: "Самая длинная река России:", options: ["Волга", "Обь", "Лена", "Не знаю", "Другой вариант"], correctAnswer: "Обь", hint: "Обь с Иртышом - самая длинная" },
      { type: 'quiz', question: "Самое глубокое озеро мира в России:", options: ["Ладожское", "Байкал", "Каспийское", "Не знаю", "Другой вариант"], correctAnswer: "Байкал", hint: "Байкал - глубочайшее озеро" },
      { type: 'quiz', question: "Укажи субъекты РФ:", options: ["Московская область", "Киев", "Минск", "Не знаю", "Другой вариант"], correctAnswer: "Московская область", hint: "Субъекты Российской Федерации" },
      { type: 'quiz', question: "Россия граничит с ... странами (число)", options: ["17", "18", "19", "20", "16"], correctAnswer: "18", hint: "Самое большое число границ" },
      { type: 'quiz', question: "Какая самая большая страна в мире?", options: ["США", "Китай", "Россия", "Канада", "Бразилия"], correctAnswer: "Россия", hint: "Россия - самая большая страна по площади" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь географию России! 🗺️" }
  },
  {
    title: "География мира",
    subject: "География",
    icon: "Map",
    color: "text-teal-400",
    tasks: [
      { type: 'quiz', question: "Самая большая страна мира по площади:", options: ["Китай", "США", "Россия", "Не знаю", "Другой вариант"], correctAnswer: "Россия", hint: "17 млн км²" },
      { type: 'quiz', question: "Самая населённая страна мира:", options: ["Индия", "Китай", "США", "Не знаю", "Другой вариант"], correctAnswer: "Индия", hint: "Индия превзошла Китай в 2023" },
      { type: 'quiz', question: "Укажи континенты:", options: ["Евразия", "Атлантида", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Евразия", hint: "Шесть континентов" },
      { type: 'quiz', question: "Самый большой океан - ... океан", options: ["наречие", "существительное", "Тихий", "прилагательное", "глагол"], correctAnswer: "Тихий", hint: "Тихий океан - самый большой" },
      { type: 'quiz', question: "Какая самая большая страна в мире?", options: ["США", "Китай", "Россия", "Канада", "Бразилия"], correctAnswer: "Россия", hint: "Россия - самая большая страна по площади" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь географию мира! 🌍" }
  },
  {
    title: "Программирование",
    subject: "Информатика",
    icon: "Monitor",
    color: "text-sky-400",
    tasks: [
      { type: 'quiz', question: "Переменная в программировании - это:", options: ["Постоянное значение", "Именованная область памяти", "Команда", "Не знаю", "Другой вариант"], correctAnswer: "Именованная область памяти", hint: "Хранит данные" },
      { type: 'quiz', question: "Цикл for используется для:", options: ["Однократного выполнения", "Многократного выполнения", "Остановки программы", "Не знаю", "Другой вариант"], correctAnswer: "Многократного выполнения", hint: "Повторение кода" },
      { type: 'quiz', question: "Укажи типы данных:", options: ["Integer", "Table", "Chair", "Не знаю", "Другой вариант"], correctAnswer: "Integer", hint: "Основные типы данных" },
      { type: 'quiz', question: "if-else - это ... конструкция", options: ["глагол", "условная", "существительное", "наречие", "прилагательное"], correctAnswer: "условная", hint: "Условный оператор" },
      { type: 'quiz', question: "Что такое компьютер?", options: ["Музыкальный инструмент", "Вычислительная машина", "Книга", "Животное", "Растение"], correctAnswer: "Вычислительная машина", hint: "Компьютер вычисляет и обрабатывает данные" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь программирование! 💻" }
  },
  {
    title: "Алгоритмы и структуры данных",
    subject: "Информатика",
    icon: "Monitor",
    color: "text-sky-400",
    tasks: [
      { type: 'quiz', question: "Массив - это:", options: ["Одна переменная", "Упорядоченный набор элементов", "Функция", "Не знаю", "Другой вариант"], correctAnswer: "Упорядоченный набор элементов", hint: "Коллекция данных" },
      { type: 'quiz', question: "Сложность алгоритма O(n) означает:", options: ["Константное время", "Линейное время", "Квадратичное время", "Не знаю", "Другой вариант"], correctAnswer: "Линейное время", hint: "Время растёт линейно" },
      { type: 'quiz', question: "Укажи алгоритмы сортировки:", options: ["Пузырьковая", "Умножения", "Деления", "Не знаю", "Другой вариант"], correctAnswer: "Пузырьковая", hint: "Алгоритмы упорядочивания" },
      { type: 'quiz', question: "Бинарный поиск работает за O(log ...)", options: ["прилагательное", "существительное", "наречие", "глагол", "n"], correctAnswer: "n", hint: "Логарифмическая сложность" },
      { type: 'quiz', question: "Что такое компьютер?", options: ["Музыкальный инструмент", "Вычислительная машина", "Книга", "Животное", "Растение"], correctAnswer: "Вычислительная машина", hint: "Компьютер вычисляет и обрабатывает данные" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь алгоритмы! 🔢" }
  },
  {
    title: "Электродинамика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Закон Ома для участка цепи:", options: ["I = U/R", "I = UR", "I = R/U", "Не знаю", "Другой вариант"], correctAnswer: "I = U/R", hint: "Ток = напряжение / сопротивление" },
      { type: 'quiz', question: "Сила тока измеряется в ...", options: ["прилагательное", "существительное", "наречие", "амперах", "глагол"], correctAnswer: "амперах", hint: "Единица силы тока" },
      { type: 'quiz', question: "При последовательном соединении сопротивления:", options: ["Складываются", "Вычитаются", "Перемножаются", "Не знаю", "Другой вариант"], correctAnswer: "Складываются", hint: "R = R₁ + R₂ + ..." },
      { type: 'quiz', question: "Укажи электрические величины:", options: ["Напряжение", "Масса", "Скорость", "Не знаю", "Другой вариант"], correctAnswer: "Напряжение", hint: "Электрические характеристики" },
      { type: 'quiz', question: "Что измеряется в метрах?", options: ["Время", "Масса", "Длина", "Температура", "Скорость"], correctAnswer: "Длина", hint: "Метр - единица длины" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь электродинамику! ⚡" }
  },
  {
    title: "Магнитное поле",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Магнитное поле создаётся:", options: ["Покоющимися зарядами", "Движущимися зарядами", "Только магнитами", "Не знаю", "Другой вариант"], correctAnswer: "Движущимися зарядами", hint: "Электрический ток создаёт магнитное поле" },
      { type: 'quiz', question: "Сила Лоренца действует на:", options: ["Покоющийся заряд", "Движущийся заряд", "Любой заряд", "Не знаю", "Другой вариант"], correctAnswer: "Движущийся заряд", hint: "F = qvB" },
      { type: 'quiz', question: "Правило ... руки определяет направление магнитного поля", options: ["наречие", "буравчика", "глагол", "прилагательное", "существительное"], correctAnswer: "буравчика", hint: "Правило буравчика или правой руки" },
      { type: 'quiz', question: "Магнитный поток измеряется в:", options: ["Тесла", "Вебер", "Ампер", "Не знаю", "Другой вариант"], correctAnswer: "Вебер", hint: "Ф = BS" },
      { type: 'quiz', question: "Что измеряется в метрах?", options: ["Время", "Масса", "Длина", "Температура", "Скорость"], correctAnswer: "Длина", hint: "Метр - единица длины" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь магнитное поле! 🧲" }
  },
  {
    title: "Органическая химия",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: "Алканы имеют общую формулу:", options: ["CₙH₂ₙ", "CₙH₂ₙ₊₂", "CₙH₂ₙ₋₂", "Не знаю", "Другой вариант"], correctAnswer: "CₙH₂ₙ₊₂", hint: "Предельные углеводороды" },
      { type: 'quiz', question: "Этанол - это:", options: ["Кислота", "Спирт", "Альдегид", "Не знаю", "Другой вариант"], correctAnswer: "Спирт", hint: "C₂H₅OH - этиловый спирт" },
      { type: 'quiz', question: "Укажи функциональные группы:", options: ["-OH", "-H₂O", "-O₂", "Не знаю", "Другой вариант"], correctAnswer: "-OH", hint: "Группы атомов, определяющие свойства" },
      { type: 'quiz', question: "Гомологический ряд - это серия веществ с разницей CH...", options: ["4", "3", "0", "1", "2"], correctAnswer: "2", hint: "Гомологи отличаются на CH₂" },
      { type: 'quiz', question: "Из чего состоит молекула воды?", options: ["H₂O", "CO₂", "NaCl", "O₂", "H₂"], correctAnswer: "H₂O", hint: "Вода = H₂O" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь органическую химию! 🧪" }
  },
  {
    title: "Углеводороды",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: "Алкены содержат:", options: ["Одинарную связь", "Двойную связь", "Тройную связь", "Не знаю", "Другой вариант"], correctAnswer: "Двойную связь", hint: "C=C - двойная связь" },
      { type: 'quiz', question: "Бензол имеет структуру:", options: ["Линейную", "Циклическую", "Разветвлённую", "Не знаю", "Другой вариант"], correctAnswer: "Циклическую", hint: "C₆H₆ - ароматическое кольцо" },
      { type: 'quiz', question: "Укажи типы реакций в органике:", options: ["Замещения", "Гниения", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Замещения", hint: "Основные типы органических реакций" },
      { type: 'quiz', question: "Метан - это CH...", options: ["4", "3", "6", "5", "2"], correctAnswer: "4", hint: "CH₄ - простейший алкан" },
      { type: 'quiz', question: "Из чего состоит молекула воды?", options: ["H₂O", "CO₂", "NaCl", "O₂", "H₂"], correctAnswer: "H₂O", hint: "Вода = H₂O" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь углеводороды! ⚗️" }
  }
]
