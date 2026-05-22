// Экспорт игр для 6 класса
import { GameLesson } from '../types'

export const sixthGradeGames: GameLesson[] = [
  {
    title: "Отрицательные числа",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "-5 + 3 = ?", options: ["-2", "-8", "2", "Не знаю", "Другой вариант"], correctAnswer: "-2", hint: "От большего по модулю отнимаем меньшее" },
      { type: 'quiz', question: "-7 - 3 = ?", options: ["-4", "-10", "4", "Не знаю", "Другой вариант"], correctAnswer: "-10", hint: "Два минуса = складываем модули, знак минус" },
      { type: 'quiz', question: "-4 × 5 = ...", options: ["20", "30", "-20", "10", "80"], correctAnswer: "-20", hint: "Минус на плюс = минус" },
      { type: 'quiz', question: "-6 × (-2) = ?", options: ["-12", "12", "-8", "Не знаю", "Другой вариант"], correctAnswer: "12", hint: "Минус на минус = плюс" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты работаешь с отрицательными числами! 🔢" }
  },
  {
    title: "Координаты на плоскости",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Точка A(3, 2). Какая координата x?", options: ["3", "2", "5", "Первый", "Второй"], correctAnswer: "3", hint: "Первая координата - это x (абсцисса)" },
      { type: 'quiz', question: "Где находится точка (-2, 3)?", options: ["I четверть", "II четверть", "III четверть", "Не знаю", "Другой вариант"], correctAnswer: "II четверть", hint: "x отрицательный, y положительный" },
      { type: 'quiz', question: "Точка (0, 5) лежит на оси ...", options: ["наречие", "существительное", "y", "прилагательное", "глагол"], correctAnswer: "y", hint: "x=0, значит на оси y" },
      { type: 'quiz', question: "Сколько координат у точки на плоскости?", options: ["1", "2", "3", "4", "5"], correctAnswer: "2", hint: "x и y - две координаты" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Супер! Ты понимаешь координаты! 📐" }
  },
  {
    title: "Пропорции",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "3/6 = 1/2. Верно ли равенство?", options: ["Да", "Нет", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Да", hint: "3/6 = 1/2 (сократили на 3)" },
      { type: 'quiz', question: "x/4 = 3/12, x = ...", options: ["0", "4", "1", "2", "3"], correctAnswer: "1", hint: "x = 4 × 3 / 12 = 1" },
      { type: 'quiz', question: "Основное свойство пропорции:", options: ["a/b = c/d", "a×d = b×c", "a+c = b+d", "Не знаю", "Другой вариант"], correctAnswer: "a×d = b×c", hint: "Произведение крайних = произведению средних" },
      { type: 'quiz', question: "5/x = 10/4, x = ...", options: ["2", "3", "0", "1", "4"], correctAnswer: "2", hint: "x = 5 × 4 / 10 = 2" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты решаешь пропорции! ⚖️" }
  },
  {
    title: "Длина окружности и площадь круга",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Формула длины окружности?", options: ["C = πr", "C = 2πr", "C = πr²", "Не знаю", "Другой вариант"], correctAnswer: "C = 2πr", hint: "C = 2πr или C = πd" },
      { type: 'quiz', question: "Формула площади круга?", options: ["S = πr", "S = 2πr", "S = πr²", "Не знаю", "Другой вариант"], correctAnswer: "S = πr²", hint: "Площадь круга = π × радиус²" },
      { type: 'quiz', question: "Если r = 3, то C = 2π × 3 = ...π", options: ["5", "8", "6", "4", "7"], correctAnswer: "6", hint: "C = 2πr = 2π × 3 = 6π" },
      { type: 'quiz', question: "Чему примерно равно π?", options: ["3", "3.14", "3.5", "Не знаю", "Другой вариант"], correctAnswer: "3.14", hint: "π ≈ 3.14" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Умница! Ты знаешь геометрию круга! ⭕" }
  },
  {
    title: "Имя числительное",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "\"Пять\" - это числительное...", options: ["Количественное", "Порядковое", "Собирательное", "Не знаю", "Другой вариант"], correctAnswer: "Количественное", hint: "Количественные отвечают на \"сколько?\"" },
      { type: 'quiz', question: "\"Пятый\" - это числительное...", options: ["Количественное", "Порядковое", "Дробное", "Не знаю", "Другой вариант"], correctAnswer: "Порядковое", hint: "Порядковые отвечают на \"который?\"" },
      { type: 'quiz', question: "Укажи числительные:", options: ["Пять", "Пятёрка", "Пятивратный", "Не знаю", "Другой вариант"], correctAnswer: "Пять", hint: "Числительное - часть речи, обозначающая число" },
      { type: 'quiz', question: "\"Двое\" - это числительное...", options: ["Количественное", "Порядковое", "Собирательное", "Не знаю", "Другой вариант"], correctAnswer: "Собирательное", hint: "Собирательные: двое, трое, четверо..." },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь числительные! 🔢" }
  },
  {
    title: "Местоимение",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "\"Я, ты, он, она\" - это местоимения...", options: ["Личные", "Притяжательные", "Вопросительные", "Не знаю", "Другой вариант"], correctAnswer: "Личные", hint: "Личные местоимения указывают на лица" },
      { type: 'quiz', question: "Укажи личные местоимения:", options: ["Я", "Мой", "Кто", "Не знаю", "Другой вариант"], correctAnswer: "Я", hint: "Личные: я, ты, он, она, оно, мы, вы, они" },
      { type: 'quiz', question: "\"Мой, твой, наш\" - это местоимения...", options: ["Личные", "Притяжательные", "Указательные", "Не знаю", "Другой вариант"], correctAnswer: "Притяжательные", hint: "Притяжательные указывают на принадлежность" },
      { type: 'quiz', question: "\"Кто, что, какой\" - это местоимения...", options: ["Личные", "Вопросительные", "Относительные", "Пушкин", "Лермонтов"], correctAnswer: "Вопросительные", hint: "Вопросительные используются в вопросах" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь местоимения! ✍️" }
  },
  {
    title: "Н и НН в прилагательных",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Сколько Н в слове \"кожаный\"?", options: ["Н", "НН", "1", "2", "3"], correctAnswer: "Н", hint: "-ан-, -ян-, -ин- пишется одна Н" },
      { type: 'quiz', question: "Сколько Н в слове \"деревянный\"?", options: ["Н", "НН", "1", "2", "3"], correctAnswer: "НН", hint: "-енн-, -онн- пишется НН" },
      { type: 'quiz', question: "Укажи слова с НН:", options: ["Традиционный", "Серебряный", "Кожаный", "Не знаю", "Другой вариант"], correctAnswer: "Традиционный", hint: "-онн-, -енн- = НН" },
      { type: 'quiz', question: "Стекля...ый (Н/НН)", options: ["нн\'", "нь", "н", "нн", "ннн"], correctAnswer: "нн", hint: "Стеклянный - исключение!" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь правописание Н и НН! 📚" }
  },
  {
    title: "Литературные жанры",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Рассказ - это жанр...", options: ["Эпоса", "Лирики", "Драмы", "Не знаю", "Другой вариант"], correctAnswer: "Эпоса", hint: "Эпос - повествовательные жанры" },
      { type: 'quiz', question: "Стихотворение - это жанр...", options: ["Эпоса", "Лирики", "Драмы", "Не знаю", "Другой вариант"], correctAnswer: "Лирики", hint: "Лирика выражает чувства и переживания" },
      { type: 'quiz', question: "Укажи эпические жанры:", options: ["Роман", "Стихотворение", "Пьеса", "Не знаю", "Другой вариант"], correctAnswer: "Роман", hint: "Эпос рассказывает о событиях" },
      { type: 'quiz', question: "Пьеса - это жанр...", options: ["Эпоса", "Лирики", "Драмы", "Не знаю", "Другой вариант"], correctAnswer: "Драмы", hint: "Драма предназначена для постановки" },
      { type: 'quiz', question: "Что такое сказка?", options: ["Научная статья", "Стихотворение", "Выдуманная история", "Учебник", "Энциклопедия"], correctAnswer: "Выдуманная история", hint: "Сказка - вымышленный рассказ" },
    ],
    reward: { stars: 3, message: "Прекрасно! Ты знаешь литературные роды! 📖" }
  },
  {
    title: "Изобразительные средства",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "\"Золотые руки\" - это...", options: ["Эпитет", "Метафора", "Сравнение", "Не знаю", "Другой вариант"], correctAnswer: "Метафора", hint: "Метафора - скрытое сравнение" },
      { type: 'quiz', question: "\"Как лев, он был смел\" - это...", options: ["Эпитет", "Метафора", "Сравнение", "Не знаю", "Другой вариант"], correctAnswer: "Сравнение", hint: "Сравнение с союзами как, словно, будто" },
      { type: 'quiz', question: "Укажи эпитеты:", options: ["Золотая осень", "Быстро бежит", "Птицы летят", "Не знаю", "Другой вариант"], correctAnswer: "Золотая осень", hint: "Эпитет - образное определение" },
      { type: 'quiz', question: "\"Шёпот листьев\" - это...", options: ["Эпитет", "Олицетворение", "Метафора", "Не знаю", "Другой вариант"], correctAnswer: "Олицетворение", hint: "Олицетворение - наделение неживого свойствами живого" },
      { type: 'quiz', question: "Что такое сказка?", options: ["Научная статья", "Стихотворение", "Выдуманная история", "Учебник", "Энциклопедия"], correctAnswer: "Выдуманная история", hint: "Сказка - вымышленный рассказ" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь художественные средства! ✨" }
  },
  {
    title: "Древняя Русь",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "В каком году призвали Рюрика?", options: ["862", "882", "988", "Не знаю", "Другой вариант"], correctAnswer: "862", hint: "862 год - призвание варягов" },
      { type: 'quiz', question: "Кто объединил Киев и Новгород?", options: ["Рюрик", "Олег", "Игорь", "Пушкин", "Лермонтов"], correctAnswer: "Олег", hint: "Олег Вещий объединил в 882 году" },
      { type: 'quiz', question: "Укажи киевских князей:", options: ["Олег", "Рюрик", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Олег", hint: "Рюрик правил в Новгороде" },
      { type: 'quiz', question: "В каком году крестили Русь?", options: ["862", "988", "1036", "Не знаю", "Другой вариант"], correctAnswer: "988", hint: "Крещение Руси - 988 год" },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Здорово! Ты знаешь историю Руси! 🏰" }
  },
  {
    title: "Феодальная раздробленность",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Что такое феодальная раздробленность?", options: ["Объединение земель", "Разделение на независимые княжества", "Война с врагами", "Не знаю", "Другой вариант"], correctAnswer: "Разделение на независимые княжества", hint: "Каждое княжество управлялось самостоятельно" },
      { type: 'quiz', question: "Кто разгромил Русь в 1237-1240 годах?", options: ["Хазары", "Монголо-татары", "Викинги", "Пушкин", "Лермонтов"], correctAnswer: "Монголо-татары", hint: "Батыево нашествие" },
      { type: 'quiz', question: "Укажи княжества периода раздробленности:", options: ["Киевское", "Римская империя", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Киевское", hint: "Русские княжества XII-XIII веков" },
      { type: 'quiz', question: "Кто был князем Владимиро-Суздальской земли?", options: ["Андрей Боголюбский", "Александр Невский", "Дмитрий Донской", "Пушкин", "Лермонтов"], correctAnswer: "Андрей Боголюбский", hint: "Андрей Боголюбский построил Успенский собор" },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь историю! 📜" }
  },
  {
    title: "Фотосинтез",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Где происходит фотосинтез?", options: ["В корнях", "В листьях", "В цветках", "Не знаю", "Другой вариант"], correctAnswer: "В листьях", hint: "Листья содержат хлорофилл" },
      { type: 'quiz', question: "Что нужно для фотосинтеза?", options: ["Кислород и вода", "Углекислый газ и вода", "Азот и вода", "Не знаю", "Другой вариант"], correctAnswer: "Углекислый газ и вода", hint: "CO₂ + H₂O → глюкоза + O₂" },
      { type: 'quiz', question: "Что образуется при фотосинтезе?", options: ["Кислород", "Углекислый газ", "Азот", "Не знаю", "Другой вариант"], correctAnswer: "Кислород", hint: "Продукты фотосинтеза" },
      { type: 'quiz', question: "Какой пигмент участвует в фотосинтезе?", options: ["Гемоглобин", "Хлорофилл", "Меланин", "Первый", "Второй"], correctAnswer: "Хлорофилл", hint: "Хлорофилл даёт зелёный цвет" },
      { type: 'quiz', question: "Какое животное млекопитающее?", options: ["Лягушка 🐸", "Рыба 🐟", "Кошка 🐱", "Змея 🐍", "Ящерица 🦎"], correctAnswer: "Кошка 🐱", hint: "Млекопитающие кормят детёнышей молоком" },
    ],
    reward: { stars: 3, message: "Превосходно! Ты понимаешь фотосинтез! 🌱" }
  },
  {
    title: "Систематика организмов",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какая систематическая категория самая крупная?", options: ["Вид", "Род", "Царство", "Первый", "Второй"], correctAnswer: "Царство", hint: "Царство > Тип > Класс > Отряд > Семейство > Род > Вид" },
      { type: 'quiz', question: "Какая категория самая мелкая?", options: ["Вид", "Род", "Семейство", "Первый", "Второй"], correctAnswer: "Вид", hint: "Вид - основная единица классификации" },
      { type: 'quiz', question: "Укажи правильный порядок (от крупного к мелкому):", options: ["Царство-Тип-Класс", "Класс-Тип-Царство", "Вид-Род-Семейство", "Царство-Вид-Класс", "Не знаю"], correctAnswer: "Царство-Тип-Класс", hint: "От крупного к мелкому" },
      { type: 'quiz', question: "К какому царству относится человек?", options: ["Растения", "Грибы", "Животные", "Не знаю", "Другой вариант"], correctAnswer: "Животные", hint: "Человек - животное" },
      { type: 'quiz', question: "Какое животное млекопитающее?", options: ["Лягушка 🐸", "Рыба 🐟", "Кошка 🐱", "Змея 🐍", "Ящерица 🦎"], correctAnswer: "Кошка 🐱", hint: "Млекопитающие кормят детёнышей молоком" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь систематику! 🔬" }
  },
  {
    title: "Гидросфера",
    subject: "География",
    icon: "Map",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Сколько процентов Земли покрыто водой?", options: ["50%", "71%", "90%", "1", "2"], correctAnswer: "71%", hint: "71% поверхности Земли - вода" },
      { type: 'quiz', question: "Какой океан самый большой?", options: ["Атлантический", "Тихий", "Индийский", "Первый", "Второй"], correctAnswer: "Тихий", hint: "Тихий океан занимает 1/3 поверхности Земли" },
      { type: 'quiz', question: "Укажи части Мирового океана:", options: ["Море", "Озеро", "Река", "Не знаю", "Другой вариант"], correctAnswer: "Море", hint: "Мировой океан = океаны + моря + заливы" },
      { type: 'quiz', question: "Как называется круговорот воды в природе?", options: ["Испарение", "Влагооборот", "Круговорот воды", "Не знаю", "Другой вариант"], correctAnswer: "Круговорот воды", hint: "Испарение → осадки → сток → испарение" },
      { type: 'quiz', question: "Какая самая большая страна в мире?", options: ["США", "Китай", "Россия", "Канада", "Бразилия"], correctAnswer: "Россия", hint: "Россия - самая большая страна по площади" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь гидросферу! 🌊" }
  },
  {
    title: "Атмосфера",
    subject: "География",
    icon: "Map",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Какой газ преобладает в атмосфере?", options: ["Кислород", "Азот", "Углекислый газ", "Первый", "Второй"], correctAnswer: "Азот", hint: "Азот - 78%, кислород - 21%" },
      { type: 'quiz', question: "Какой слой атмосферы ближе к Земле?", options: ["Стратосфера", "Тропосфера", "Мезосфера", "Первый", "Второй"], correctAnswer: "Тропосфера", hint: "Тропосфера - до 10-18 км" },
      { type: 'quiz', question: "Укажи атмосферные явления:", options: ["Дождь", "Цунами", "Прилив", "Не знаю", "Другой вариант"], correctAnswer: "Дождь", hint: "Атмосферные явления - в воздухе" },
      { type: 'quiz', question: "Что измеряет барометр?", options: ["Температуру", "Атмосферное давление", "Влажность", "Не знаю", "Другой вариант"], correctAnswer: "Атмосферное давление", hint: "Барометр = атмосферное давление" },
      { type: 'quiz', question: "Какая самая большая страна в мире?", options: ["США", "Китай", "Россия", "Канада", "Бразилия"], correctAnswer: "Россия", hint: "Россия - самая большая страна по площади" },
    ],
    reward: { stars: 3, message: "Замечательно! Ты знаешь атмосферу! ☁️" }
  },
  {
    title: "Past Perfect",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "When I came, she ___ already left.", options: ["has", "had", "was", "Не знаю", "Другой вариант"], correctAnswer: "had", hint: "Past Perfect: had + V3" },
      { type: 'quiz', question: "I had ... (finish) my work before he came. (finished)", options: ["существительное", "глагол", "прилагательное", "finished", "наречие"], correctAnswer: "finished", hint: "had + V3 (правильный глагол + -ed)" },
      { type: 'quiz', question: "Past Perfect используется для...", options: ["Действия в прошлом до другого действия", "Действия сейчас", "Будущего действия", "Не знаю", "Другой вариант"], correctAnswer: "Действия в прошлом до другого действия", hint: "\"Предпрошедшее\" время" },
      { type: 'quiz', question: "Укажи маркеры Past Perfect:", options: ["By the time", "Yesterday", "Last week", "Не знаю", "Другой вариант"], correctAnswer: "By the time", hint: "By the time, before, after, already" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Great! Ты знаешь Past Perfect! ⏮️" }
  },
  {
    title: "Conditionals",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "If it rains, I ___ at home.", options: ["stay", "will stay", "stayed", "Не знаю", "Другой вариант"], correctAnswer: "will stay", hint: "First Conditional: If + Present, will + V" },
      { type: 'quiz', question: "If I had money, I ___ a car.", options: ["buy", "would buy", "will buy", "Не знаю", "Другой вариант"], correctAnswer: "would buy", hint: "Second Conditional: If + Past, would + V" },
      { type: 'quiz', question: "If I ... you, I would study harder. (were)", options: ["прилагательное", "существительное", "наречие", "were", "глагол"], correctAnswer: "were", hint: "Second Conditional с were для всех лиц" },
      { type: 'quiz', question: "Zero Conditional описывает...", options: ["Нереальное условие", "Факты и законы природы", "Будущее", "Не знаю", "Другой вариант"], correctAnswer: "Факты и законы природы", hint: "If you heat water to 100°C, it boils." },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Excellent! Ты понимаешь условные предложения! 🔄" }
  },
  {
    title: "Сложение и вычитание дробей",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "1/2 + 1/4 = .../4", options: ["2", "4", "5", "3", "1"], correctAnswer: "3", hint: "Приведи к общему знаменателю: 2/4 + 1/4 = 3/4" },
      { type: 'quiz', question: "3/4 - 1/4 = .../4", options: ["1", "0", "2", "4", "3"], correctAnswer: "2", hint: "3/4 - 1/4 = 2/4 = 1/2" },
      { type: 'quiz', question: "1/2 + 1/3 = ?", options: ["2/5", "5/6", "1/6", "Не знаю", "Другой вариант"], correctAnswer: "5/6", hint: "Общий знаменатель 6: 3/6 + 2/6" },
      { type: 'quiz', question: "5/6 - 1/3 = ?", options: ["4/3", "1/2", "3/6", "Не знаю", "Другой вариант"], correctAnswer: "1/2", hint: "5/6 - 2/6 = 3/6 = 1/2" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты умеешь складывать дроби! 📊" }
  },
  {
    title: "Умножение и деление дробей",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "1/2 × 1/3 = .../6", options: ["4", "3", "1", "0", "2"], correctAnswer: "1", hint: "1×1 / 2×3 = 1/6" },
      { type: 'quiz', question: "2/3 × 3/4 = ?", options: ["6/7", "1/2", "5/7", "Не знаю", "Другой вариант"], correctAnswer: "1/2", hint: "2×3 / 3×4 = 6/12 = 1/2" },
      { type: 'quiz', question: "1/2 ÷ 1/4 = ...", options: ["3", "2", "4", "0", "1"], correctAnswer: "2", hint: "1/2 × 4/1 = 4/2 = 2" },
      { type: 'quiz', question: "3/4 ÷ 1/2 = ?", options: ["3/8", "1 1/2", "2/3", "Не знаю", "Другой вариант"], correctAnswer: "1 1/2", hint: "3/4 × 2/1 = 6/4 = 1 1/2" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Супер! Ты умеешь умножать и делить дроби! ✖️➗" }
  },
  {
    title: "Уравнения с дробями",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "x + 1/2 = 1, x = .../2", options: ["4", "0", "1", "2", "3"], correctAnswer: "1", hint: "x = 1 - 1/2 = 1/2" },
      { type: 'quiz', question: "x - 1/4 = 1/2, x = .../4", options: ["1", "5", "2", "4", "3"], correctAnswer: "3", hint: "x = 1/2 + 1/4 = 2/4 + 1/4 = 3/4" },
      { type: 'quiz', question: "2x = 1/2, x = ?", options: ["1", "1/4", "1/2", "Не знаю", "Другой вариант"], correctAnswer: "1/4", hint: "x = 1/2 ÷ 2 = 1/4" },
      { type: 'quiz', question: "x/3 = 2/3, x = ...", options: ["3", "4", "2", "1", "0"], correctAnswer: "2", hint: "x = 3 × 2/3 = 2" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты решаешь уравнения с дробями! 📐" }
  },
  {
    title: "Глагол: времена и формы",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Глаголы изменяются по:", options: ["Падежам", "Временам", "Склонениям", "Не знаю", "Другой вариант"], correctAnswer: "Временам", hint: "Прошедшее, настоящее, будущее" },
      { type: 'quiz', question: "Укажи глаголы прошедшего времени:", options: ["Читал", "Читает", "Будет читать", "Пишет", "Не знаю"], correctAnswer: "Читал", hint: "Прошедшее время - суффикс -л-" },
      { type: 'quiz', question: "Глаголы совершенного вида отвечают на вопрос:", options: ["Что делать?", "Что сделать?", "Оба вопроса", "Не знаю", "Другой вариант"], correctAnswer: "Что сделать?", hint: "Совершенный вид = действие завершено" },
      { type: 'quiz', question: "Глагол \"читать\" - ... вида (несовершенный/совершенный)", options: ["существительное", "несовершенного", "глагол", "прилагательное", "наречие"], correctAnswer: "несовершенного", hint: "Несовершенный вид = что делать?" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь глагол! 📝" }
  },
  {
    title: "Спряжения глаголов",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Глаголы I спряжения в 3 лице мн.ч. имеют окончание:", options: ["-ут/-ют", "-ат/-ят", "-ить", "Не знаю", "Другой вариант"], correctAnswer: "-ут/-ют", hint: "I спряжение: -ут/-ют" },
      { type: 'quiz', question: "Глагол \"говорить\" - какого спряжения?", options: ["I спряжение", "II спряжение", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "II спряжение", hint: "ГоворИТЬ - II спряжение" },
      { type: 'quiz', question: "Укажи глаголы II спряжения:", options: ["Смотреть", "Делать", "Читать", "Не знаю", "Другой вариант"], correctAnswer: "Смотреть", hint: "II спряжение: -ить + исключения" },
      { type: 'quiz', question: "Они пиш...т (I спр.)", options: ["прилагательное", "наречие", "существительное", "глагол", "ут"], correctAnswer: "ут", hint: "Писать - I спряжение" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь спряжения! ✍️" }
  },
  {
    title: "Басни И.А. Крылова",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Кто автор басни \"Стрекоза и Муравей\"?", options: ["Пушкин", "Крылов", "Лермонтов", "Гоголь", "Толстой"], correctAnswer: "Крылов", hint: "Иван Андреевич Крылов" },
      { type: 'quiz', question: "Укажи басни Крылова:", options: ["Ворона и Лисица", "Колобок", "Репка", "Не знаю", "Другой вариант"], correctAnswer: "Ворона и Лисица", hint: "Басни И.А. Крылова" },
      { type: 'quiz', question: "Мораль басни - это:", options: ["Вступление", "Нравоучительный вывод", "Описание героев", "Не знаю", "Другой вариант"], correctAnswer: "Нравоучительный вывод", hint: "Мораль учит чему-то" },
      { type: 'quiz', question: "\"Ты всё пела? Это дело: Так поди же, ...!\"", options: ["прилагательное", "существительное", "наречие", "попляши", "глагол"], correctAnswer: "попляши", hint: "Из басни \"Стрекоза и Муравей\"" },
      { type: 'quiz', question: "Что такое сказка?", options: ["Научная статья", "Стихотворение", "Выдуманная история", "Учебник", "Энциклопедия"], correctAnswer: "Выдуманная история", hint: "Сказка - вымышленный рассказ" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь басни! 📚" }
  },
  {
    title: "Монголо-татарское иго",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Когда Батый напал на Русь?", options: ["1223", "1237", "1240", "Не знаю", "Другой вариант"], correctAnswer: "1237", hint: "Зимой 1237-1238 годов" },
      { type: 'quiz', question: "Кто разбил шведов на Неве?", options: ["Дмитрий Донской", "Александр Невский", "Иван Калита", "Пушкин", "Лермонтов"], correctAnswer: "Александр Невский", hint: "1240 год - Невская битва" },
      { type: 'quiz', question: "Укажи последствия ига:", options: ["Упадок культуры", "Развитие торговли", "Усиление княжеств", "Не знаю", "Другой вариант"], correctAnswer: "Упадок культуры", hint: "Отрицательные последствия ига" },
      { type: 'quiz', question: "Когда закончилось иго?", options: ["1380", "1480", "1500", "Не знаю", "Другой вариант"], correctAnswer: "1480", hint: "Стояние на Угре" },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь историю! 🏰" }
  },
  {
    title: "Куликовская битва",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "В каком году была Куликовская битва?", options: ["1380", "1480", "1240", "Не знаю", "Другой вариант"], correctAnswer: "1380", hint: "8 сентября 1380 года" },
      { type: 'quiz', question: "Кто возглавил русское войско?", options: ["Александр Невский", "Дмитрий Донской", "Иван III", "Пушкин", "Лермонтов"], correctAnswer: "Дмитрий Донской", hint: "Дмитрий Иванович Донской" },
      { type: 'quiz', question: "Укажи участников битвы:", options: ["Дмитрий Донской", "Александр Невский", "Батый", "Не знаю", "Другой вариант"], correctAnswer: "Дмитрий Донской", hint: "Исторические личности 1380 года" },
      { type: 'quiz', question: "Битва проходила на ... поле", options: ["наречие", "глагол", "прилагательное", "Куликовом", "существительное"], correctAnswer: "Куликовом", hint: "Куликовская битва" },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь историю! ⚔️" }
  },
  {
    title: "Органы цветковых растений",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какой орган растения отвечает за размножение?", options: ["Корень", "Лист", "Цветок", "Первый", "Второй"], correctAnswer: "Цветок", hint: "Цветок - орган семенного размножения" },
      { type: 'quiz', question: "Укажи вегетативные органы:", options: ["Корень", "Цветок", "Плод", "Не знаю", "Другой вариант"], correctAnswer: "Корень", hint: "Вегетативные органы обеспечивают рост" },
      { type: 'quiz', question: "Плод образуется из:", options: ["Лепестков", "Завязи цветка", "Тычинок", "Не знаю", "Другой вариант"], correctAnswer: "Завязи цветка", hint: "Из завязи после опыления" },
      { type: 'quiz', question: "Семена находятся в ...", options: ["существительное", "прилагательное", "плоде", "глагол", "наречие"], correctAnswer: "плоде", hint: "Плод защищает семена" },
      { type: 'quiz', question: "Какое животное млекопитающее?", options: ["Лягушка 🐸", "Рыба 🐟", "Кошка 🐱", "Змея 🐍", "Ящерица 🦎"], correctAnswer: "Кошка 🐱", hint: "Млекопитающие кормят детёнышей молоком" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь растения! 🌸" }
  },
  {
    title: "Present Continuous",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I ___ reading now.", options: ["is", "am", "are", "Не знаю", "Другой вариант"], correctAnswer: "am", hint: "I am + V-ing" },
      { type: 'quiz', question: "She ... (play) tennis now. (is playing)", options: ["наречие", "прилагательное", "is playing", "глагол", "существительное"], correctAnswer: "is playing", hint: "She is + V-ing" },
      { type: 'quiz', question: "They ___ sleeping.", options: ["is", "am", "are", "Не знаю", "Другой вариант"], correctAnswer: "are", hint: "They are + V-ing" },
      { type: 'quiz', question: "Укажи маркеры Present Continuous:", options: ["Now", "Yesterday", "Tomorrow", "Always", "Не знаю"], correctAnswer: "Now", hint: "Now, at the moment, look, listen" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Great! Ты знаешь Present Continuous! ⏳" }
  },
  {
    title: "Материки и океаны",
    subject: "География",
    icon: "Map",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Сколько материков на Земле?", options: ["5", "6", "7", "1", "2"], correctAnswer: "6", hint: "Евразия, Африка, Сев.Америка, Юж.Америка, Австралия, Антарктида" },
      { type: 'quiz', question: "Укажи океаны:", options: ["Тихий", "Байкал", "Средиземное море", "Не знаю", "Другой вариант"], correctAnswer: "Тихий", hint: "Океаны - крупнейшие водоёмы" },
      { type: 'quiz', question: "Какой материк самый большой?", options: ["Африка", "Евразия", "Северная Америка", "Первый", "Второй"], correctAnswer: "Евразия", hint: "Евразия - самый большой материк" },
      { type: 'quiz', question: "Самый холодный материк - ...", options: ["существительное", "Антарктида", "глагол", "наречие", "прилагательное"], correctAnswer: "Антарктида", hint: "Антарктида - материк льдов" },
      { type: 'quiz', question: "Какая самая большая страна в мире?", options: ["США", "Китай", "Россия", "Канада", "Бразилия"], correctAnswer: "Россия", hint: "Россия - самая большая страна по площади" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь географию! 🌍" }
  }
]
