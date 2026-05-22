// Экспорт игр для 5 класса
import { GameLesson } from '../types'

export const fifthGradeGames: GameLesson[] = [
  {
    title: "Обыкновенные дроби",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Сократи дробь: 6/8", options: ["3/4", "2/3", "1/2", "Не знаю", "Другой вариант"], correctAnswer: "3/4", hint: "Раздели числитель и знаменатель на 2" },
      { type: 'quiz', question: "Приведи к общему знаменателю: 1/2 и 1/3", options: ["3/6 и 2/6", "2/6 и 3/6", "1/6 и 1/6", "Не знаю", "Другой вариант"], correctAnswer: "3/6 и 2/6", hint: "Общий знаменатель = 6" },
      { type: 'quiz', question: "2/5 + 1/5 = .../5", options: ["1", "3", "5", "4", "2"], correctAnswer: "3", hint: "Сложи числители" },
      { type: 'quiz', question: "Какая дробь больше: 2/3 или 3/4?", options: ["2/3", "3/4", "Они равны", "Первый", "Второй"], correctAnswer: "3/4", hint: "Приведи к общему знаменателю: 8/12 vs 9/12" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь дроби! 📊" }
  },
  {
    title: "Десятичные дроби",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "0,5 + 0,3 = ?", options: ["0,53", "0,8", "0,35", "Не знаю", "Другой вариант"], correctAnswer: "0,8", hint: "Сложи как обычные числа" },
      { type: 'quiz', question: "0,25 × 4 = ?", options: ["0,100", "1", "1,00", "Не знаю", "Другой вариант"], correctAnswer: "1", hint: "25 × 4 = 100, значит 0,25 × 4 = 1" },
      { type: 'quiz', question: "1,5 - 0,7 = ...", options: ["2", "0,8", "1", "3", "40"], correctAnswer: "0,8", hint: "15 - 7 = 8" },
      { type: 'quiz', question: "Укажи равные дроби:", options: ["0,5 = 1/2", "0,3 = 1/3", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "0,5 = 1/2", hint: "0,3 ≈ 1/3, но не равно" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Супер! Ты работаешь с десятичными дробями! 🔢" }
  },
  {
    title: "Проценты",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "50% от 100 = ?", options: ["25", "50", "75", "Не знаю", "Другой вариант"], correctAnswer: "50", hint: "50% = 1/2 от числа" },
      { type: 'quiz', question: "25% от 200 = ?", options: ["25", "50", "100", "Не знаю", "Другой вариант"], correctAnswer: "50", hint: "25% = 1/4 от числа" },
      { type: 'quiz', question: "10% от 500 = ...", options: ["45", "40", "48", "50", "52"], correctAnswer: "50", hint: "10% = 1/10 от числа" },
      { type: 'quiz', question: "Сколько процентов составляет 1/4?", options: ["10%", "25%", "50%", "1", "2"], correctAnswer: "25%", hint: "1/4 = 25/100 = 25%" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь проценты! 💯" }
  },
  {
    title: "Уравнения",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "x + 5 = 12, x = ...", options: ["5", "7", "6", "9", "8"], correctAnswer: "7", hint: "x = 12 - 5" },
      { type: 'quiz', question: "x - 8 = 15, x = ...", options: ["13", "18", "21", "25", "23"], correctAnswer: "23", hint: "x = 15 + 8" },
      { type: 'quiz', question: "3x = 18, x = ...", options: ["5", "8", "7", "6", "4"], correctAnswer: "6", hint: "x = 18 ÷ 3" },
      { type: 'quiz', question: "Решить: 2x + 4 = 14", options: ["x = 5", "x = 7", "x = 10", "Не знаю", "Другой вариант"], correctAnswer: "x = 5", hint: "2x = 10, x = 5" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Умница! Ты решаешь уравнения! 📐" }
  },
  {
    title: "Причастия",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Причастие - это...", options: ["Глагол", "Прилагательное", "Особая форма глагола", "Не знаю", "Другой вариант"], correctAnswer: "Особая форма глагола", hint: "Причастие обозначает признак по действию" },
      { type: 'quiz', question: "Укажи причастия:", options: ["Читающий", "Читать", "Интересный", "Не знаю", "Другой вариант"], correctAnswer: "Читающий", hint: "Причастия отвечают на вопрос \"какой?\" и имеют признаки глагола" },
      { type: 'quiz', question: "Какой признак причастия от глагола?", options: ["Время", "Вид", "Род", "Первый", "Второй"], correctAnswer: "Время", hint: "Причастия бывают настоящего и прошедшего времени" },
      { type: 'quiz', question: "Действие, которое совершает сам предмет - ... причастие", options: ["действительное", "прилагательное", "существительное", "глагол", "наречие"], correctAnswer: "действительное", hint: "Действительные причастия" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь причастия! 📚" }
  },
  {
    title: "Деепричастия",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Деепричастие обозначает...", options: ["Признак предмета", "Добавочное действие", "Основное действие", "Не знаю", "Другой вариант"], correctAnswer: "Добавочное действие", hint: "Деепричастие отвечает на вопросы \"что делая? что сделав?\"" },
      { type: 'quiz', question: "Укажи деепричастия:", options: ["Читая", "Читать", "Читающий", "Не знаю", "Другой вариант"], correctAnswer: "Читая", hint: "Деепричастия оканчиваются на -а, -я, -в, -вши" },
      { type: 'quiz', question: "Деепричастие неизменяемо по...", options: ["Роду и числу", "По всем признакам", "По падежам", "Не знаю", "Другой вариант"], correctAnswer: "По всем признакам", hint: "Деепричастие - неизменяемая форма" },
      { type: 'quiz', question: "Как выделяется деепричастный оборот?", options: ["Запятыми", "Тире", "Не выделяется", "Не знаю", "Другой вариант"], correctAnswer: "Запятыми", hint: "Деепричастный оборот обособляется" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Супер! Ты понимаешь деепричастия! ✍️" }
  },
  {
    title: "Синтаксис сложного предложения",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Сложносочинённое предложение - это...", options: ["С союзом И, А, НО", "С союзами ЧТО, КОГДА", "Без союзов", "Не знаю", "Другой вариант"], correctAnswer: "С союзом И, А, НО", hint: "Союзы сочинения: и, а, но, или" },
      { type: 'quiz', question: "Сложноподчинённое предложение - это...", options: ["С союзом И, А, НО", "С союзами ЧТО, КОГДА", "Без союзов", "Не знаю", "Другой вариант"], correctAnswer: "С союзами ЧТО, КОГДА", hint: "Союзы подчинения: что, когда, если, потому что" },
      { type: 'quiz', question: "Укажи сложноподчинённые предложения:", options: ["Я пошёл домой, когда закончил работу.", "Светило солнце, и пели птицы.", "Дождь шёл, но мы гуляли.", "Не знаю", "Другой вариант"], correctAnswer: "Я пошёл домой, когда закончил работу.", hint: "Сложноподчинённые с союзами когда, что" },
      { type: 'quiz', question: "Сколько грамматических основ в сложном предложении?", options: ["Одна", "Две или больше", "Три", "1", "2"], correctAnswer: "Две или больше", hint: "Сложное = 2+ простых предложений" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь синтаксис! 📖" }
  },
  {
    title: "Басни и их особенности",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Что такое мораль басни?", options: ["Вступление", "Нравоучительный вывод", "Описание героев", "Не знаю", "Другой вариант"], correctAnswer: "Нравоучительный вывод", hint: "Мораль - это главный урок басни" },
      { type: 'quiz', question: "Кто автор басни \"Ворона и Лисица\"?", options: ["Крылов", "Пушкин", "Лермонтов", "Гоголь", "Толстой"], correctAnswer: "Крылов", hint: "Иван Андреевич Крылов" },
      { type: 'quiz', question: "Укажи особенности басни:", options: ["Аллегория", "Сказочные герои", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Аллегория", hint: "Басня - краткий рассказ с моралью" },
      { type: 'quiz', question: "Что такое аллегория в басне?", options: ["Иносказание", "Прямое описание", "Сравнение", "Не знаю", "Другой вариант"], correctAnswer: "Иносказание", hint: "Аллегория = иносказание, животные = люди" },
      { type: 'quiz', question: "Что такое сказка?", options: ["Научная статья", "Стихотворение", "Выдуманная история", "Учебник", "Энциклопедия"], correctAnswer: "Выдуманная история", hint: "Сказка - вымышленный рассказ" },
    ],
    reward: { stars: 3, message: "Прекрасно! Ты понимаешь жанр басни! 📚" }
  },
  {
    title: "Сказки Пушкина",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Сколько лет ждал старик золотую рыбку?", options: ["30 лет и 3 года", "33 года", "35 лет", "1", "2"], correctAnswer: "30 лет и 3 года", hint: "\"Жил старик со своею старухой у самого синего моря...\"" },
      { type: 'quiz', question: "Кто превратился в лебедя в сказке о царе Салтане?", options: ["Царевна", "Царица", "Ткачиха", "Пушкин", "Лермонтов"], correctAnswer: "Царевна", hint: "Царевна-лебедь" },
      { type: 'quiz', question: "Укажи сказки Пушкина:", options: ["Сказка о рыбаке и рыбке", "Конёк-горбунок", "Теремок", "Не знаю", "Другой вариант"], correctAnswer: "Сказка о рыбаке и рыбке", hint: "Александр Сергеевич Пушкин" },
      { type: 'quiz', question: "\"Сказка о ... и о работнике его Балде\"", options: ["наречие", "глагол", "прилагательное", "попе", "существительное"], correctAnswer: "попе", hint: "Поп нанял Балду" },
      { type: 'quiz', question: "Что такое сказка?", options: ["Научная статья", "Стихотворение", "Выдуманная история", "Учебник", "Энциклопедия"], correctAnswer: "Выдуманная история", hint: "Сказка - вымышленный рассказ" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь сказки Пушкина! ✨" }
  },
  {
    title: "Древний Египет",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Какая река была главной в Египте?", options: ["Евфрат", "Нил", "Тигр", "Первый", "Второй"], correctAnswer: "Нил", hint: "Нил - главная река Египта" },
      { type: 'quiz', question: "Для чего строили пирамиды?", options: ["Для жилья", "Для фараонов (гробницы)", "Для храмов", "Не знаю", "Другой вариант"], correctAnswer: "Для фараонов (гробницы)", hint: "Пирамиды - гробницы фараонов" },
      { type: 'quiz', question: "Укажи достижения египтян:", options: ["Иероглифы", "Колесо", "Бумага", "Не знаю", "Другой вариант"], correctAnswer: "Иероглифы", hint: "Египтяне изобрели иероглифы и папирус" },
      { type: 'quiz', question: "Кто был правителем Египта?", options: ["Царь", "Фараон", "Император", "Пушкин", "Лермонтов"], correctAnswer: "Фараон", hint: "Фараон - правитель Древнего Египта" },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Здорово! Ты знаешь Древний Египет! 🏛️" }
  },
  {
    title: "Древняя Греция",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Как называлось греческое государство-город?", options: ["Полис", "Империя", "Царство", "Не знаю", "Другой вариант"], correctAnswer: "Полис", hint: "Полис - город-государство в Греции" },
      { type: 'quiz', question: "Где проходили Олимпийские игры?", options: ["В Афинах", "В Олимпии", "В Спарте", "Не знаю", "Другой вариант"], correctAnswer: "В Олимпии", hint: "Олимпия - место первых Олимпийских игр" },
      { type: 'quiz', question: "Укажи греческих богов:", options: ["Зевс", "Юпитер", "Тор", "Не знаю", "Другой вариант"], correctAnswer: "Зевс", hint: "Зевс, Афина, Посейдон - греческие боги" },
      { type: 'quiz', question: "Кто написал \"Илиаду\" и \"Одиссею\"?", options: ["Сократ", "Гомер", "Платон", "Пушкин", "Лермонтов"], correctAnswer: "Гомер", hint: "Гомер - автор \"Илиады\" и \"Одиссеи\"" },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь Древнюю Грецию! 🏺" }
  },
  {
    title: "Клетка",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какая часть клетки хранит наследственную информацию?", options: ["Ядро", "Цитоплазма", "Мембрана", "Первый", "Второй"], correctAnswer: "Ядро", hint: "Ядро содержит ДНК" },
      { type: 'quiz', question: "Что такое цитоплазма?", options: ["Оболочка клетки", "Внутренняя среда клетки", "Ядро", "Не знаю", "Другой вариант"], correctAnswer: "Внутренняя среда клетки", hint: "Цитоплазма заполняет клетку" },
      { type: 'quiz', question: "Укажи части клетки:", options: ["Ядро", "Сердце", "Лёгкие", "Не знаю", "Другой вариант"], correctAnswer: "Ядро", hint: "Органоиды клетки" },
      { type: 'quiz', question: "Какой органоид называют \"энергетической станцией\"?", options: ["Ядро", "Митохондрия", "Рибосома", "Первый", "Второй"], correctAnswer: "Митохондрия", hint: "Митохондрии вырабатывают энергию" },
      { type: 'quiz', question: "Какое животное млекопитающее?", options: ["Лягушка 🐸", "Рыба 🐟", "Кошка 🐱", "Змея 🐍", "Ящерица 🦎"], correctAnswer: "Кошка 🐱", hint: "Млекопитающие кормят детёнышей молоком" },
    ],
    reward: { stars: 3, message: "Замечательно! Ты знаешь строение клетки! 🔬" }
  },
  {
    title: "Царства живой природы",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Укажи царства живой природы:", options: ["Бактерии", "Камни", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Бактерии", hint: "4 царства: бактерии, грибы, растения, животные" },
      { type: 'quiz', question: "Какое царство делает фотосинтез?", options: ["Бактерии", "Растения", "Животные", "Первый", "Второй"], correctAnswer: "Растения", hint: "Растения содержат хлорофилл" },
      { type: 'quiz', question: "Грибы - это...", options: ["Растения", "Животные", "Отдельное царство", "Не знаю", "Другой вариант"], correctAnswer: "Отдельное царство", hint: "Грибы - отдельное царство живой природы" },
      { type: 'quiz', question: "Какое царство самое древнее?", options: ["Бактерии", "Грибы", "Растения", "Первый", "Второй"], correctAnswer: "Бактерии", hint: "Бактерии появились первыми на Земле" },
      { type: 'quiz', question: "Какое животное млекопитающее?", options: ["Лягушка 🐸", "Рыба 🐟", "Кошка 🐱", "Змея 🐍", "Ящерица 🦎"], correctAnswer: "Кошка 🐱", hint: "Млекопитающие кормят детёнышей молоком" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь классификацию! 🌿" }
  },
  {
    title: "План и карта",
    subject: "География",
    icon: "Map",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Что показывает масштаб?", options: ["Расстояние", "Во сколько раз уменьшено", "Направление", "Не знаю", "Другой вариант"], correctAnswer: "Во сколько раз уменьшено", hint: "Масштаб показывает степень уменьшения" },
      { type: 'quiz', question: "Как называется линия на карте, соединяющая точки с одинаковой высотой?", options: ["Меридиан", "Изобара", "Горизонталь", "Не знаю", "Другой вариант"], correctAnswer: "Горизонталь", hint: "Горизонтали показывают рельеф" },
      { type: 'quiz', question: "Укажи стороны горизонта:", options: ["Север", "Верх", "Лево", "Не знаю", "Другой вариант"], correctAnswer: "Север", hint: "Север, юг, восток, запад" },
      { type: 'quiz', question: "Масштаб 1:1000 означает 1 см на карте = ... см на местности", options: ["990", "1000", "995", "998", "1002"], correctAnswer: "1000", hint: "В 1000 раз больше" },
      { type: 'quiz', question: "Какая самая большая страна в мире?", options: ["США", "Китай", "Россия", "Канада", "Бразилия"], correctAnswer: "Россия", hint: "Россия - самая большая страна по площади" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь карты! 🗺️" }
  },
  {
    title: "Present Perfect",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I have ___ this book.", options: ["read", "readed", "reading", "Не знаю", "Другой вариант"], correctAnswer: "read", hint: "Present Perfect: have + V3 (3-я форма)" },
      { type: 'quiz', question: "She has ... (visit) London. (visited)", options: ["существительное", "visited", "глагол", "наречие", "прилагательное"], correctAnswer: "visited", hint: "has + V3 (правильный глагол + -ed)" },
      { type: 'quiz', question: "Present Perfect используется для...", options: ["Действий в прошлом", "Действий с результатом в настоящем", "Будущих действий", "Не знаю", "Другой вариант"], correctAnswer: "Действий с результатом в настоящем", hint: "Результат важен сейчас" },
      { type: 'quiz', question: "Укажи маркеры Present Perfect:", options: ["Just", "Yesterday", "Last week", "Не знаю", "Другой вариант"], correctAnswer: "Just", hint: "Just, already, ever, never, yet" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Great! Ты знаешь Present Perfect! ✨" }
  },
  {
    title: "Modal Verbs",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I ___ swim. (могу)", options: ["can", "must", "should", "Не знаю", "Другой вариант"], correctAnswer: "can", hint: "Can = мочь, уметь" },
      { type: 'quiz', question: "You ___ do your homework. (должен)", options: ["can", "must", "may", "Не знаю", "Другой вариант"], correctAnswer: "must", hint: "Must = должен (обязанность)" },
      { type: 'quiz', question: "You ___ see a doctor. (следовало бы)", options: ["can", "must", "should", "Не знаю", "Другой вариант"], correctAnswer: "should", hint: "Should = следует, совет" },
      { type: 'quiz', question: "... I come in? (Можно?) - May", options: ["May", "существительное", "глагол", "прилагательное", "наречие"], correctAnswer: "May", hint: "May = можно (просьба разрешения)" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Excellent! Модальные глаголы! 🇬🇧" }
  },
  {
    title: "Деление и умножение",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "12 ÷ 4 = ...", options: ["5", "4", "2", "1", "3"], correctAnswer: "3", hint: "Сколько раз 4 помещается в 12?" },
      { type: 'quiz', question: "7 × 8 = ...", options: ["54", "56", "58", "51", "46"], correctAnswer: "56", hint: "Таблица умножения" },
      { type: 'quiz', question: "72 ÷ 9 = ?", options: ["7", "8", "9", "Не знаю", "Другой вариант"], correctAnswer: "8", hint: "9 × 8 = 72" },
      { type: 'quiz', question: "45 ÷ ... = 9", options: ["6", "4", "3", "7", "5"], correctAnswer: "5", hint: "Какое число умножить на 9 = 45?" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты владеешь умножением и делением! ✖️➗" }
  },
  {
    title: "Площадь и периметр",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Периметр квадрата со стороной 5:", options: ["10", "20", "25", "Не знаю", "Другой вариант"], correctAnswer: "20", hint: "P = 4 × a = 4 × 5" },
      { type: 'quiz', question: "Площадь прямоугольника 3 × 4 = ...", options: ["13", "11", "12", "10", "14"], correctAnswer: "12", hint: "S = a × b" },
      { type: 'quiz', question: "Периметр прямоугольника 2 × 3:", options: ["5", "6", "10", "Не знаю", "Другой вариант"], correctAnswer: "10", hint: "P = 2(a + b) = 2(2 + 3)" },
      { type: 'quiz', question: "Площадь квадрата со стороной 6 = ...", options: ["34", "31", "38", "36", "26"], correctAnswer: "36", hint: "S = a² = 6²" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Супер! Ты умеешь находить площадь и периметр! 📐" }
  },
  {
    title: "Имя существительное",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Имя существительное обозначает:", options: ["Действие", "Предмет", "Признак", "Не знаю", "Другой вариант"], correctAnswer: "Предмет", hint: "Существительное = предмет" },
      { type: 'quiz', question: "Укажи имена существительные:", options: ["Бег", "Бежать", "Красивый", "Не знаю", "Другой вариант"], correctAnswer: "Бег", hint: "Существительные отвечают на \"кто?\" \"что?\"" },
      { type: 'quiz', question: "Сколько падежей в русском языке?", options: ["5", "6", "7", "1", "2"], correctAnswer: "6", hint: "И, Р, Д, В, Т, П" },
      { type: 'quiz', question: "Какой падеж отвечает на вопрос \"кого? чего?\"?", options: ["Именительный", "Родительный", "Дательный", "Первый", "Второй"], correctAnswer: "Родительный", hint: "Родительный падеж - нет кого? чего?" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь имя существительное! 📚" }
  },
  {
    title: "Корень слова",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Корень - это:", options: ["Изменяемая часть", "Общая часть родственных слов", "Окончание", "Не знаю", "Другой вариант"], correctAnswer: "Общая часть родственных слов", hint: "В корне заключён общий смысл" },
      { type: 'quiz', question: "Укажи однокоренные слова к слову \"лес\":", options: ["Лесник", "Лестница", "Лесть", "Не знаю", "Другой вариант"], correctAnswer: "Лесник", hint: "Однокоренные слова имеют общий корень" },
      { type: 'quiz', question: "В слове \"подосиновик\" корень ...", options: ["существительное", "осин", "глагол", "наречие", "прилагательное"], correctAnswer: "осин", hint: "Под-осин-овик" },
      { type: 'quiz', question: "Что такое чередование звуков?", options: ["Замена одной буквы другой", "Замена одного звука другим", "Удвоение согласных", "Не знаю", "Другой вариант"], correctAnswer: "Замена одного звука другим", hint: "Например: бег - бежишь (г//ж)" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Супер! Ты понимаешь состав слова! ✍️" }
  },
  {
    title: "Древняя Русь",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Кто основал династию русских князей?", options: ["Иван Калита", "Рюрик", "Дмитрий Донской", "Пушкин", "Лермонтов"], correctAnswer: "Рюрик", hint: "862 год - призвание варягов" },
      { type: 'quiz', question: "Когда произошло крещение Руси?", options: ["862", "988", "1147", "Не знаю", "Другой вариант"], correctAnswer: "988", hint: "Князь Владимир крестил Русь" },
      { type: 'quiz', question: "Укажи первых русских князей:", options: ["Рюрик", "Иван Грозный", "Пётр I", "Не знаю", "Другой вариант"], correctAnswer: "Рюрик", hint: "Первые князья Древней Руси" },
      { type: 'quiz', question: "Кто объединил Киев и Новгород?", options: ["Рюрик", "Олег", "Владимир", "Пушкин", "Лермонтов"], correctAnswer: "Олег", hint: "Вещий Олег, 882 год" },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь историю Древней Руси! 🏰" }
  },
  {
    title: "Животные и среды обитания",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Укажи животных суши:", options: ["Медведь", "Акула", "Дельфин", "Не знаю", "Другой вариант"], correctAnswer: "Медведь", hint: "Животные, живущие на земле" },
      { type: 'quiz', question: "К какому царству относятся грибы?", options: ["Растения", "Животные", "Отдельное царство", "Не знаю", "Другой вариант"], correctAnswer: "Отдельное царство", hint: "Грибы - это не растения и не животные" },
      { type: 'quiz', question: "Что нужно для фотосинтеза?", options: ["Только вода", "Свет, вода, углекислый газ", "Только свет", "Не знаю", "Другой вариант"], correctAnswer: "Свет, вода, углекислый газ", hint: "Растения создают пищу с помощью света" },
      { type: 'quiz', question: "Укажи животных водоёмов:", options: ["Рыба", "Волк", "Сокол", "Не знаю", "Другой вариант"], correctAnswer: "Рыба", hint: "Животные, связанные с водой" },
      { type: 'quiz', question: "Какое животное млекопитающее?", options: ["Лягушка 🐸", "Рыба 🐟", "Кошка 🐱", "Змея 🐍", "Ящерица 🦎"], correctAnswer: "Кошка 🐱", hint: "Млекопитающие кормят детёнышей молоком" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь среды обитания! 🌿" }
  },
  {
    title: "Природные зоны",
    subject: "География",
    icon: "Map",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Укажи природные зоны России:", options: ["Тундра", "Джунгли", "Саванна", "Не знаю", "Другой вариант"], correctAnswer: "Тундра", hint: "Природные зоны нашей страны" },
      { type: 'quiz', question: "Какая зона находится севернее тайги?", options: ["Степь", "Тундра", "Пустыня", "Первый", "Второй"], correctAnswer: "Тундра", hint: "Тундра - самая северная зона с растениями" },
      { type: 'quiz', question: "Тайга - это...", options: ["Лес из лиственных деревьев", "Лес из хвойных деревьев", "Безлесная зона", "Не знаю", "Другой вариант"], correctAnswer: "Лес из хвойных деревьев", hint: "Ель, сосна, кедр - деревья тайги" },
      { type: 'quiz', question: "Самая холодная природная зона - арктическая ...", options: ["пустыня", "наречие", "глагол", "существительное", "прилагательное"], correctAnswer: "пустыня", hint: "Лёд и снег" },
      { type: 'quiz', question: "Какая самая большая страна в мире?", options: ["США", "Китай", "Россия", "Канада", "Бразилия"], correctAnswer: "Россия", hint: "Россия - самая большая страна по площади" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь природные зоны! 🗺️" }
  },
  {
    title: "Past Simple",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Yesterday I ___ to school. (go)", options: ["go", "went", "goed", "Не знаю", "Другой вариант"], correctAnswer: "went", hint: "Past Simple - прошедшее время" },
      { type: 'quiz', question: "She ... (play) football yesterday. (played)", options: ["глагол", "прилагательное", "played", "наречие", "существительное"], correctAnswer: "played", hint: "Правильный глагол + -ed" },
      { type: 'quiz', question: "Укажи неправильные глаголы:", options: ["Go", "Play", "Watch", "Не знаю", "Другой вариант"], correctAnswer: "Go", hint: "Неправильные глаголы не добавляют -ed" },
      { type: 'quiz', question: "I ___ (see) him yesterday.", options: ["seed", "saw", "seen", "Не знаю", "Другой вариант"], correctAnswer: "saw", hint: "See - saw - seen" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Great! Ты знаешь прошедшее время! 🇬🇧" }
  },
  {
    title: "Действия с десятичными дробями",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "0,6 + 0,4 = ...", options: ["0", "3", "4", "2", "1"], correctAnswer: "1", hint: "6 + 4 = 10, значит 0,6 + 0,4 = 1" },
      { type: 'quiz', question: "2,5 - 1,3 = ?", options: ["1,2", "1,5", "2,2", "Не знаю", "Другой вариант"], correctAnswer: "1,2", hint: "25 - 13 = 12" },
      { type: 'quiz', question: "0,2 × 5 = ...", options: ["2", "3", "0", "4", "1"], correctAnswer: "1", hint: "2 × 5 = 10, значит 0,2 × 5 = 1,0 = 1" },
      { type: 'quiz', question: "1,5 ÷ 0,5 = ?", options: ["3", "0,3", "30", "Не знаю", "Другой вариант"], correctAnswer: "3", hint: "15 ÷ 5 = 3" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты работаешь с десятичными дробями! 🔢" }
  },
  {
    title: "Задачи на проценты",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "В классе 20 учеников, 25% - отличники. Сколько отличников?", options: ["4", "5", "6", "1", "2"], correctAnswer: "5", hint: "25% = 1/4, 20 ÷ 4 = 5" },
      { type: 'quiz', question: "Цена 100 рублей, скидка 10%. Цена со скидкой = ... руб.", options: ["80", "88", "92", "85", "90"], correctAnswer: "90", hint: "100 - 10 = 90" },
      { type: 'quiz', question: "20% от 50 = ?", options: ["5", "10", "15", "Не знаю", "Другой вариант"], correctAnswer: "10", hint: "20% = 1/5, 50 ÷ 5 = 10" },
      { type: 'quiz', question: "Если 30% = 15, то 100% = ...", options: ["48", "52", "40", "50", "45"], correctAnswer: "50", hint: "15 ÷ 0,3 = 50" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Супер! Ты решаешь задачи на проценты! 💯" }
  },
  {
    title: "Правописание приставок",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "В приставках на -з/-с перед звонкими пишется:", options: ["-з", "-с", "Зависит от корня", "Не знаю", "Другой вариант"], correctAnswer: "-з", hint: "Перед звонкими - з, перед глухими - с" },
      { type: 'quiz', question: "Бе...шумный (перед ш - глухой)", options: ["существительное", "прилагательное", "наречие", "глагол", "с"], correctAnswer: "с", hint: "Ш - глухой звук, пишем с" },
      { type: 'quiz', question: "Укажи слова с приставкой на -з:", options: ["Беззвёздный", "Бесконечный", "Бесшумный", "Не знаю", "Другой вариант"], correctAnswer: "Беззвёздный", hint: "Перед звонкими пишется з" },
      { type: 'quiz', question: "Приставка пре- означает:", options: ["Очень", "Пере-", "Оба значения", "Не знаю", "Другой вариант"], correctAnswer: "Оба значения", hint: "Прекрасный = очень красивый, преградить = перегородить" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь приставки! ✍️" }
  },
  {
    title: "Имя прилагательное",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Имя прилагательное обозначает:", options: ["Предмет", "Признак предмета", "Действие", "Не знаю", "Другой вариант"], correctAnswer: "Признак предмета", hint: "Прилагательное отвечает на \"какой?\"" },
      { type: 'quiz', question: "Укажи имена прилагательные:", options: ["Красивый", "Красота", "Бежать", "Не знаю", "Другой вариант"], correctAnswer: "Красивый", hint: "Прилагательные описывают предметы" },
      { type: 'quiz', question: "Прилагательные изменяются по:", options: ["Временам", "Родам, числам, падежам", "Лицам", "Не знаю", "Другой вариант"], correctAnswer: "Родам, числам, падежам", hint: "Прилагательные согласуются с существительными" },
      { type: 'quiz', question: "Красивый (м.р.) → Красивая (ж.р.) → Красив... (ср.р.)", options: ["глагол", "наречие", "ое", "прилагательное", "существительное"], correctAnswer: "ое", hint: "Красивое (средний род)" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь прилагательные! 📝" }
  },
  {
    title: "Древний Рим",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Столица Римской империи:", options: ["Афины", "Рим", "Александрия", "Не знаю", "Другой вариант"], correctAnswer: "Рим", hint: "Рим - столица Римской империи" },
      { type: 'quiz', question: "Укажи римских богов:", options: ["Юпитер", "Зевс", "Посейдон", "Не знаю", "Другой вариант"], correctAnswer: "Юпитер", hint: "Римские боги: Юпитер, Марс, Венера" },
      { type: 'quiz', question: "Гладиаторы - это:", options: ["Боги", "Бойцы на арене", "Политики", "Не знаю", "Другой вариант"], correctAnswer: "Бойцы на арене", hint: "Гладиаторы сражались в Колизее" },
      { type: 'quiz', question: "Рим был основан в ... г. до н.э. (753)", options: ["755", "748", "743", "751", "753"], correctAnswer: "753", hint: "753 год до н.э." },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь Древний Рим! 🏛️" }
  },
  {
    title: "Средние века",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Феодализм - это:", options: ["Рабовладение", "Система земельных отношений", "Демократия", "Не знаю", "Другой вариант"], correctAnswer: "Система земельных отношений", hint: "Феодалы владели землёй" },
      { type: 'quiz', question: "Укажи сословия Средневековья:", options: ["Духовенство", "Рабочие", "Буржуазия", "Не знаю", "Другой вариант"], correctAnswer: "Духовенство", hint: "Три сословия: духовенство, рыцари, крестьяне" },
      { type: 'quiz', question: "Рыцарь - это:", options: ["Крестьянин", "Воин-феодал", "Священник", "Не знаю", "Другой вариант"], correctAnswer: "Воин-феодал", hint: "Рыцари были воинами" },
      { type: 'quiz', question: "Замок - это ... феодала", options: ["прилагательное", "крепость", "существительное", "наречие", "глагол"], correctAnswer: "крепость", hint: "Замки защищали феодалов" },
      { type: 'quiz', question: "В каком веке мы живём?", options: ["XX", "XXI", "XIX", "XXII", "XVIII"], correctAnswer: "XXI", hint: "Сейчас XXI век" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь Средние века! ⚔️" }
  },
  {
    title: "Строение растений",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какой орган растения всасывает воду?", options: ["Лист", "Корень", "Стебель", "Первый", "Второй"], correctAnswer: "Корень", hint: "Корень всасывает воду из почвы" },
      { type: 'quiz', question: "Укажи части растения:", options: ["Корень", "Не знаю", "Другой вариант", "Ни один из этих", "Все перечисленные"], correctAnswer: "Корень", hint: "Основные органы растения" },
      { type: 'quiz', question: "Фотосинтез происходит в:", options: ["Корне", "Листьях", "Стебле", "Не знаю", "Другой вариант"], correctAnswer: "Листьях", hint: "В листьях есть хлорофилл" },
      { type: 'quiz', question: "Корень закрепляет растение в ...", options: ["глагол", "наречие", "прилагательное", "существительное", "почве"], correctAnswer: "почве", hint: "Корень держит растение" },
      { type: 'quiz', question: "Какое животное млекопитающее?", options: ["Лягушка 🐸", "Рыба 🐟", "Кошка 🐱", "Змея 🐍", "Ящерица 🦎"], correctAnswer: "Кошка 🐱", hint: "Млекопитающие кормят детёнышей молоком" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь растения! 🌱" }
  },
  {
    title: "Мировой океан",
    subject: "География",
    icon: "Map",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Сколько океанов на Земле?", options: ["3", "4", "5", "1", "2"], correctAnswer: "5", hint: "Тихий, Атлантический, Индийский, Северный Ледовитый, Южный" },
      { type: 'quiz', question: "Укажи части океана:", options: ["Море", "Озеро", "Река", "Не знаю", "Другой вариант"], correctAnswer: "Море", hint: "Части Мирового океана" },
      { type: 'quiz', question: "Самый тёплый океан:", options: ["Тихий", "Индийский", "Атлантический", "Не знаю", "Другой вариант"], correctAnswer: "Индийский", hint: "Индийский океан самый тёплый" },
      { type: 'quiz', question: "Солёность океанской воды = ...‰ (промилле)", options: ["30", "37", "25", "35", "33"], correctAnswer: "35", hint: "В среднем 35‰" },
      { type: 'quiz', question: "Какая самая большая страна в мире?", options: ["США", "Китай", "Россия", "Канада", "Бразилия"], correctAnswer: "Россия", hint: "Россия - самая большая страна по площади" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь океаны! 🌊" }
  },
  {
    title: "Present Continuous",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I ___ reading now.", options: ["is", "am", "are", "Не знаю", "Другой вариант"], correctAnswer: "am", hint: "I am + V-ing" },
      { type: 'quiz', question: "She ... (play) tennis now. (is playing)", options: ["глагол", "существительное", "is playing", "наречие", "прилагательное"], correctAnswer: "is playing", hint: "She is + V-ing" },
      { type: 'quiz', question: "They ___ sleeping.", options: ["is", "am", "are", "Не знаю", "Другой вариант"], correctAnswer: "are", hint: "They are + V-ing" },
      { type: 'quiz', question: "Укажи маркеры Present Continuous:", options: ["Now", "Yesterday", "Last week", "Не знаю", "Другой вариант"], correctAnswer: "Now", hint: "Маркеры: now, at the moment, look, listen" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Great! Ты знаешь Present Continuous! ⏳" }
  }
]
