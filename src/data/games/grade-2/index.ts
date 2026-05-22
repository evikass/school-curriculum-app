// Экспорт игр для 2 класса
import { GameLesson } from '../types'

export const secondGradeGames: GameLesson[] = [
  {
    title: "Части речи",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Что такое имя существительное?", options: ["Предмет", "Действие", "Признак", "Не знаю", "Другой вариант"], correctAnswer: "Предмет", hint: "Существительное отвечает на вопрос КТО? ЧТО?" },
      { type: 'quiz', question: "Укажи имена существительные:", options: ["Стол 🪑", "Бежать", "Красивый", "Петь", "Не знаю"], correctAnswer: "Стол 🪑", hint: "Существительное = предмет" },
      { type: 'quiz', question: "На какой вопрос отвечает глагол?", options: ["Какой?", "Что делать?", "Кто?", "Первый", "Второй"], correctAnswer: "Что делать?", hint: "Глагол = действие" },
      { type: 'quiz', question: "Укажи глаголы:", options: ["Бежать 🏃", "Стол 🪑", "Красивый", "Не знаю", "Другой вариант"], correctAnswer: "Бежать 🏃", hint: "Глагол обозначает действие" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь части речи! 📝" }
  },
  {
    title: "Корень слова",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Что такое корень слова?", options: ["Окончание", "Главная часть слова", "Приставка", "Не знаю", "Другой вариант"], correctAnswer: "Главная часть слова", hint: "В корне заключён главный смысл" },
      { type: 'quiz', question: "Найди однокоренные слова к слову ЛЕС:", options: ["Лесник 🌲", "Лиса 🦊", "Лист 🍃", "Не знаю", "Другой вариант"], correctAnswer: "Лесник 🌲", hint: "Однокоренные слова имеют общий корень" },
      { type: 'quiz', question: "Какой корень в слове ВОДНЫЙ?", options: ["ВОД", "ВОДН", "НЫЙ", "Первый", "Второй"], correctAnswer: "ВОД", hint: "Найди общую часть с похожими словами" },
      { type: 'quiz', question: "Какое слово лишнее?", options: ["Гора ⛰️", "Горный", "Гореть 🔥", "Пригорок", "Первый"], correctAnswer: "Гореть 🔥", hint: "Проверь значение корня" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь корень слова! 🌱" }
  },
  {
    title: "Правописание приставок",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Приставка - это...", options: ["Конец слова", "Часть перед корнем", "Корень", "Не знаю", "Другой вариант"], correctAnswer: "Часть перед корнем", hint: "Приставка стоит ПЕРЕД корнем" },
      { type: 'quiz', question: "Найди слова с приставкой ПРИ-:", options: ["Приехал 🚗", "Прыгнул", "Праздник", "Не знаю", "Другой вариант"], correctAnswer: "Приехал 🚗", hint: "ПРИ- = приближение, присоединение" },
      { type: 'quiz', question: "Сколько приставок в слове ПЕРЕПРИШЁЛ?", options: ["1", "2", "3", "4", "5"], correctAnswer: "2", hint: "ПЕРЕ- и ПРИ- - две приставки" },
      { type: 'quiz', question: "Вставь приставку: ...ехал (приблизился)", options: ["пере", "пре", "При", "под", "про"], correctAnswer: "При", hint: "Приближение = ПРИ-" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Умница! Ты знаешь приставки! 📖" }
  },
  {
    title: "Сложение до 20",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "8 + 7 = ?", options: ["13", "14", "15", "Не знаю", "Другой вариант"], correctAnswer: "15", hint: "8 + 7 = 15" },
      { type: 'quiz', question: "9 + 6 = ?", options: ["14", "15", "16", "Не знаю", "Другой вариант"], correctAnswer: "15", hint: "9 + 6 = 15" },
      { type: 'quiz', question: "12 + ... = 18", options: ["7", "8", "6", "5", "4"], correctAnswer: "6", hint: "Сколько добавить?" },
      { type: 'quiz', question: "15 + 5 = ?", options: ["19", "20", "21", "Не знаю", "Другой вариант"], correctAnswer: "20", hint: "15 + 5 = 20" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты умеешь складывать до 20! ➕" }
  },
  {
    title: "Вычитание до 20",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "18 - 9 = ?", options: ["8", "9", "10", "Не знаю", "Другой вариант"], correctAnswer: "9", hint: "18 - 9 = 9" },
      { type: 'quiz', question: "15 - 7 = ?", options: ["7", "8", "9", "Не знаю", "Другой вариант"], correctAnswer: "8", hint: "15 - 7 = 8" },
      { type: 'quiz', question: "20 - ... = 14", options: ["6", "4", "8", "5", "7"], correctAnswer: "6", hint: "Сколько отнять?" },
      { type: 'quiz', question: "16 - 8 = ?", options: ["7", "8", "9", "Не знаю", "Другой вариант"], correctAnswer: "8", hint: "16 - 8 = 8" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Супер! Ты умеешь вычитать! ➖" }
  },
  {
    title: "Умножение",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "2 × 3 = ?", options: ["5", "6", "7", "Не знаю", "Другой вариант"], correctAnswer: "6", hint: "2 + 2 + 2 = 6" },
      { type: 'quiz', question: "3 × 4 = ?", options: ["10", "11", "12", "Не знаю", "Другой вариант"], correctAnswer: "12", hint: "3 + 3 + 3 + 3 = 12" },
      { type: 'quiz', question: "5 × 2 = ?", options: ["7", "10", "12", "Не знаю", "Другой вариант"], correctAnswer: "10", hint: "5 + 5 = 10" },
      { type: 'quiz', question: "4 × ... = 8", options: ["0", "2", "3", "1", "4"], correctAnswer: "2", hint: "Какое число умножить?" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Здорово! Ты изучаешь умножение! ✖️" }
  },
  {
    title: "Деление",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "6 ÷ 2 = ?", options: ["2", "3", "4", "Не знаю", "Другой вариант"], correctAnswer: "3", hint: "6 разделить на 2 части" },
      { type: 'quiz', question: "10 ÷ 5 = ?", options: ["1", "2", "5", "Не знаю", "Другой вариант"], correctAnswer: "2", hint: "10 разделить на 5" },
      { type: 'quiz', question: "8 ÷ 4 = ?", options: ["2", "3", "4", "Не знаю", "Другой вариант"], correctAnswer: "2", hint: "8 разделить на 4" },
      { type: 'quiz', question: "12 ÷ ... = 3", options: ["2", "6", "5", "4", "3"], correctAnswer: "4", hint: "На сколько разделить 12?" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Замечательно! Ты изучаешь деление! ➗" }
  },
  {
    title: "Русские писатели",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Кто написал \"Мойдодыр\"?", options: ["Пушкин", "Чуковский", "Барто", "Лермонтов", "Гоголь"], correctAnswer: "Чуковский", hint: "Корней Чуковский" },
      { type: 'quiz', question: "Кто написал \"Муха-Цокотуха\"?", options: ["Маршак", "Чуковский", "Михалков", "Пушкин", "Лермонтов"], correctAnswer: "Чуковский", hint: "Тот же автор, что и Мойдодыр" },
      { type: 'quiz', question: "Укажи произведения Пушкина:", options: ["Сказка о рыбаке и рыбке", "Мойдодыр", "Колобок", "Не знаю", "Другой вариант"], correctAnswer: "Сказка о рыбаке и рыбке", hint: "Александр Сергеевич Пушкин" },
      { type: 'quiz', question: "Кто автор стихов про игрушки?", options: ["Барто", "Маршак", "Чуковский", "Пушкин", "Лермонтов"], correctAnswer: "Барто", hint: "Агния Барто писала про игрушки" },
      { type: 'quiz', question: "Что такое сказка?", options: ["Научная статья", "Стихотворение", "Выдуманная история", "Учебник", "Энциклопедия"], correctAnswer: "Выдуманная история", hint: "Сказка - вымышленный рассказ" },
    ],
    reward: { stars: 3, message: "Прекрасно! Ты знаешь писателей! 📚" }
  },
  {
    title: "Планета Земля",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какая планета наша?", options: ["Марс 🔴", "Земля 🌍", "Луна 🌙", "Первый", "Второй"], correctAnswer: "Земля 🌍", hint: "Мы живём на планете Земля" },
      { type: 'quiz', question: "Что такое Солнце?", options: ["Планета", "Звезда ⭐", "Спутник", "Не знаю", "Другой вариант"], correctAnswer: "Звезда ⭐", hint: "Солнце - это звезда!" },
      { type: 'quiz', question: "Укажи планеты:", options: ["Земля 🌍", "Солнце ☀️", "Луна 🌙", "Не знаю", "Другой вариант"], correctAnswer: "Земля 🌍", hint: "Планеты вращаются вокруг Солнца" },
      { type: 'quiz', question: "Луна - это...", options: ["Планета", "Спутник Земли", "Звезда", "Не знаю", "Другой вариант"], correctAnswer: "Спутник Земли", hint: "Луна вращается вокруг Земли" },
      { type: 'quiz', question: "Что относится к живой природе?", options: ["Камень 🪨", "Дерево 🌳", "Вода 💧", "Солнце ☀️", "Гора ⛰️"], correctAnswer: "Дерево 🌳", hint: "Дерево - живое" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь космос! 🚀" }
  },
  {
    title: "Природа России",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какое животное символ России?", options: ["Медведь 🐻", "Тигр 🐯", "Лиса 🦊", "Первый", "Второй"], correctAnswer: "Медведь 🐻", hint: "Большой бурый медведь" },
      { type: 'quiz', question: "Что растёт в лесу?", options: ["Берёза 🌳", "Кактус 🌵", "Пальма 🌴", "Не знаю", "Другой вариант"], correctAnswer: "Берёза 🌳", hint: "Русский лес" },
      { type: 'quiz', question: "Какое озеро самое глубокое?", options: ["Каспийское", "Байкал", "Ладожское", "Первый", "Второй"], correctAnswer: "Байкал", hint: "Байкал - самое глубокое в мире" },
      { type: 'quiz', question: "Столица России?", options: ["Петербург", "Москва", "Казань", "Не знаю", "Другой вариант"], correctAnswer: "Москва", hint: "Москва - столица России" },
      { type: 'quiz', question: "Что относится к живой природе?", options: ["Камень 🪨", "Дерево 🌳", "Вода 💧", "Солнце ☀️", "Гора ⛰️"], correctAnswer: "Дерево 🌳", hint: "Дерево - живое" },
    ],
    reward: { stars: 3, message: "Молодец! Ты знаешь Россию! 🇷🇺" }
  },
  {
    title: "Животные по-английски",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Cat - это...", options: ["Собака 🐕", "Кошка 🐱", "Птица 🐦", "Не знаю", "Другой вариант"], correctAnswer: "Кошка 🐱", hint: "Cat = кошка" },
      { type: 'quiz', question: "Как будет \"собака\"?", options: ["Cat", "Dog", "Bird", "Не знаю", "Другой вариант"], correctAnswer: "Dog", hint: "Dog = собака" },
      { type: 'quiz', question: "Укажи названия животных:", options: ["Cat 🐱", "Red", "Big", "Не знаю", "Другой вариант"], correctAnswer: "Cat 🐱", hint: "Animals = животные" },
      { type: 'quiz', question: "Что такое Fish?", options: ["Птица 🐦", "Рыба 🐟", "Животное 🐾", "Не знаю", "Другой вариант"], correctAnswer: "Рыба 🐟", hint: "Fish = рыба" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Wonderful! Замечательно! 🐾" }
  },
  {
    title: "Семья по-английски",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Mother - это...", options: ["Папа", "Мама", "Бабушка", "Не знаю", "Другой вариант"], correctAnswer: "Мама", hint: "Mother = мама" },
      { type: 'quiz', question: "Как будет \"папа\"?", options: ["Mother", "Father", "Sister", "Не знаю", "Другой вариант"], correctAnswer: "Father", hint: "Father = папа" },
      { type: 'quiz', question: "Укажи слова о семье:", options: ["Mother 👩", "Cat 🐱", "Dog 🐕", "Не знаю", "Другой вариант"], correctAnswer: "Mother 👩", hint: "Family = семья" },
      { type: 'quiz', question: "Brother - это...", options: ["Сестра", "Брат", "Дедушка", "Не знаю", "Другой вариант"], correctAnswer: "Брат", hint: "Brother = брат" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Great! Отлично! 👨‍👩‍👧‍👦" }
  },
  {
    title: "Умножение на 2 и 3",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "2 × 6 = ...", options: ["13", "12", "11", "14", "10"], correctAnswer: "12", hint: "2 + 2 + 2 + 2 + 2 + 2 = 12" },
      { type: 'quiz', question: "3 × 4 = ...", options: ["13", "11", "14", "10", "12"], correctAnswer: "12", hint: "3 + 3 + 3 + 3 = 12" },
      { type: 'quiz', question: "2 × 8 = ?", options: ["14", "16", "18", "Не знаю", "Другой вариант"], correctAnswer: "16", hint: "2 × 8 = 16" },
      { type: 'quiz', question: "3 × 7 = ?", options: ["18", "21", "24", "Не знаю", "Другой вариант"], correctAnswer: "21", hint: "3 × 7 = 21" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь таблицу умножения! ✖️" }
  },
  {
    title: "Деление на 2 и 3",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "12 ÷ 2 = ...", options: ["4", "7", "5", "8", "6"], correctAnswer: "6", hint: "Какое число × 2 = 12?" },
      { type: 'quiz', question: "15 ÷ 3 = ...", options: ["6", "4", "3", "7", "5"], correctAnswer: "5", hint: "Какое число × 3 = 15?" },
      { type: 'quiz', question: "18 ÷ 2 = ?", options: ["7", "8", "9", "Не знаю", "Другой вариант"], correctAnswer: "9", hint: "9 × 2 = 18" },
      { type: 'quiz', question: "21 ÷ 3 = ?", options: ["6", "7", "8", "Не знаю", "Другой вариант"], correctAnswer: "7", hint: "7 × 3 = 21" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Супер! Ты умеешь делить! ➗" }
  },
  {
    title: "Правописание ЖИ-ШИ",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Маш...на (И/Ы)", options: ["И", "Ы", "О", "А", "Е"], correctAnswer: "И", hint: "ЖИ-ШИ пиши с И!" },
      { type: 'quiz', question: "Ш...на (И/Ы)", options: ["И", "Ы", "О", "А", "Е"], correctAnswer: "И", hint: "ШИ пиши с И!" },
      { type: 'quiz', question: "Укажи слова с ЖИ-ШИ:", options: ["Жираф", "Шар", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Жираф", hint: "ЖИ-ШИ пишутся с И" },
      { type: 'quiz', question: "В слове \"лыжи\" пишется:", options: ["И", "Ы", "Е", "Не знаю", "Другой вариант"], correctAnswer: "И", hint: "ЖИ пиши с И" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь правило ЖИ-ШИ! ✍️" }
  },
  {
    title: "Правописание ЧА-ЩА",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Туч... (А/Я)", options: ["А", "наречие", "прилагательное", "глагол", "существительное"], correctAnswer: "А", hint: "ЧА-ЩА пиши с А!" },
      { type: 'quiz', question: "Рощ... (А/Я)", options: ["глагол", "прилагательное", "наречие", "А", "существительное"], correctAnswer: "А", hint: "ЩА пиши с А!" },
      { type: 'quiz', question: "Укажи слова с ЧА-ЩА:", options: ["Чаща", "Чай", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Чаща", hint: "ЧА-ЩА пишутся с А" },
      { type: 'quiz', question: "В слове \"дача\" пишется:", options: ["А", "Я", "Е", "Не знаю", "Другой вариант"], correctAnswer: "А", hint: "ЧА пиши с А" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь правило ЧА-ЩА! ✍️" }
  },
  {
    title: "Правописание ЧУ-ЩУ",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Щ...ка (У/Ю)", options: ["наречие", "прилагательное", "существительное", "У", "глагол"], correctAnswer: "У", hint: "ЧУ-ЩУ пиши с У!" },
      { type: 'quiz', question: "Ч...до (У/Ю)", options: ["У", "существительное", "глагол", "наречие", "прилагательное"], correctAnswer: "У", hint: "ЧУ пиши с У!" },
      { type: 'quiz', question: "Укажи слова с ЧУ-ЩУ:", options: ["Щука", "Не знаю", "Другой вариант", "Ни один из этих", "Все перечисленные"], correctAnswer: "Щука", hint: "ЧУ-ЩУ пишутся с У" },
      { type: 'quiz', question: "В слове \"чулок\" пишется:", options: ["У", "Ю", "О", "Не знаю", "Другой вариант"], correctAnswer: "У", hint: "ЧУ пиши с У" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь правило ЧУ-ЩУ! ✍️" }
  },
  {
    title: "Правописание ЧК-ЧН",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "В слове \"ночка\" мягкий знак:", options: ["Нужен", "Не нужен", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Не нужен", hint: "ЧК-ЧН пишутся без мягкого знака!" },
      { type: 'quiz', question: "В слове \"ночной\" мягкий знак:", options: ["Нужен", "Не нужен", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Не нужен", hint: "ЧК-ЧН пишутся без мягкого знака!" },
      { type: 'quiz', question: "Укажи слова без мягкого знака:", options: ["Ночка", "Не знаю", "Другой вариант", "Ни один из этих", "Все перечисленные"], correctAnswer: "Ночка", hint: "ЧК-ЧН без Ь" },
      { type: 'quiz', question: "В слове \"дочка\" мягкий знак ...", options: ["существительное", "не нужен", "прилагательное", "наречие", "глагол"], correctAnswer: "не нужен", hint: "ЧК без Ь" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь правило ЧК-ЧН! ✍️" }
  },
  {
    title: "Слова-предметы",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "На какой вопрос отвечает слово \"стол\"?", options: ["Что делает?", "Какой?", "Что?", "Первый", "Второй"], correctAnswer: "Что?", hint: "Стол - это предмет" },
      { type: 'quiz', question: "Укажи слова-предметы:", options: ["Книга", "Бежать", "Красивый", "Прыгать", "Не знаю"], correctAnswer: "Книга", hint: "Слова-предметы отвечают на \"кто? что?\"" },
      { type: 'quiz', question: "Слово \"мама\" - это:", options: ["Предмет", "Действие", "Признак", "Не знаю", "Другой вариант"], correctAnswer: "Предмет", hint: "Мама - это кто?" },
      { type: 'quiz', question: "На какой вопрос отвечает слово \"кот\"?", options: ["Что делает?", "Кто?", "Какой?", "Первый", "Второй"], correctAnswer: "Кто?", hint: "Кот - это кто?" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь слова-предметы! 📝" }
  },
  {
    title: "Слова-признаки",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "На какой вопрос отвечает слово \"красивый\"?", options: ["Что делает?", "Какой?", "Что?", "Первый", "Второй"], correctAnswer: "Какой?", hint: "Красивый - это признак" },
      { type: 'quiz', question: "Укажи слова-признаки:", options: ["Большой", "Бежать", "Стол", "Не знаю", "Другой вариант"], correctAnswer: "Большой", hint: "Слова-признаки отвечают на \"какой? какая? какое?\"" },
      { type: 'quiz', question: "Слово \"зелёный\" - это:", options: ["Предмет", "Действие", "Признак", "Не знаю", "Другой вариант"], correctAnswer: "Признак", hint: "Зелёный - это какой?" },
      { type: 'quiz', question: "На какой вопрос отвечает слово \"умный\"?", options: ["Что делает?", "Кто?", "Какой?", "Первый", "Второй"], correctAnswer: "Какой?", hint: "Умный - это какой?" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь слова-признаки! 📝" }
  },
  {
    title: "Овощи и фрукты",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Укажи овощи:", options: ["Морковь 🥕", "Яблоко 🍎", "Груша 🍐", "Не знаю", "Другой вариант"], correctAnswer: "Морковь 🥕", hint: "Овощи растут в огороде" },
      { type: 'quiz', question: "Укажи фрукты:", options: ["Яблоко 🍎", "Морковь 🥕", "Огурец 🥒", "Не знаю", "Другой вариант"], correctAnswer: "Яблоко 🍎", hint: "Фрукты растут на деревьях" },
      { type: 'quiz', question: "Где растут овощи?", options: ["На деревьях", "В огороде", "В лесу", "Не знаю", "Другой вариант"], correctAnswer: "В огороде", hint: "Огород - место для овощей" },
      { type: 'quiz', question: "Что полезнее: фрукт или конфета?", options: ["Фрукт", "Конфета", "Одинаково", "Не знаю", "Другой вариант"], correctAnswer: "Фрукт", hint: "Фрукты содержат витамины" },
      { type: 'quiz', question: "Что относится к живой природе?", options: ["Камень 🪨", "Дерево 🌳", "Вода 💧", "Солнце ☀️", "Гора ⛰️"], correctAnswer: "Дерево 🌳", hint: "Дерево - живое" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь овощи и фрукты! 🥗" }
  },
  {
    title: "Еда по-английски",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Apple - это...", options: ["Апельсин", "Яблоко 🍎", "Банан", "Не знаю", "Другой вариант"], correctAnswer: "Яблоко 🍎", hint: "Apple = яблоко" },
      { type: 'quiz', question: "Как будет \"хлеб\"?", options: ["Bread", "Water", "Milk", "Не знаю", "Другой вариант"], correctAnswer: "Bread", hint: "Bread = хлеб" },
      { type: 'quiz', question: "Укажи названия еды:", options: ["Apple 🍎", "Cat 🐱", "Dog 🐕", "Не знаю", "Другой вариант"], correctAnswer: "Apple 🍎", hint: "Food = еда" },
      { type: 'quiz', question: "Water = ... (вода)", options: ["глагол", "вода", "существительное", "прилагательное", "наречие"], correctAnswer: "вода", hint: "Water = вода" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Great! Отлично! 🍎" }
  },
  {
    title: "Таблица умножения на 4 и 5",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "4 × 4 = ...", options: ["17", "14", "18", "16", "15"], correctAnswer: "16", hint: "4 × 4 = 16" },
      { type: 'quiz', question: "5 × 5 = ...", options: ["27", "15", "25", "23", "20"], correctAnswer: "25", hint: "5 × 5 = 25" },
      { type: 'quiz', question: "4 × 6 = ?", options: ["20", "24", "28", "Не знаю", "Другой вариант"], correctAnswer: "24", hint: "4 × 6 = 24" },
      { type: 'quiz', question: "5 × 7 = ?", options: ["30", "35", "40", "Не знаю", "Другой вариант"], correctAnswer: "35", hint: "5 × 7 = 35" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь таблицу умножения! ✖️" }
  },
  {
    title: "Периметр и площадь",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Периметр квадрата со стороной 3:", options: ["6", "9", "12", "Не знаю", "Другой вариант"], correctAnswer: "12", hint: "P = 4 × 3 = 12" },
      { type: 'quiz', question: "Периметр прямоугольника 2 и 4 = ...", options: ["10", "12", "13", "14", "11"], correctAnswer: "12", hint: "P = 2 × (2 + 4) = 12" },
      { type: 'quiz', question: "Площадь квадрата со стороной 4:", options: ["8", "12", "16", "Не знаю", "Другой вариант"], correctAnswer: "16", hint: "S = 4 × 4 = 16" },
      { type: 'quiz', question: "Площадь прямоугольника 3 × 5 = ...", options: ["16", "15", "17", "14", "13"], correctAnswer: "15", hint: "S = 3 × 5 = 15" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь периметр и площадь! 📐" }
  },
  {
    title: "Имя прилагательное",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Имя прилагательное обозначает:", options: ["Предмет", "Признак предмета", "Действие", "Не знаю", "Другой вариант"], correctAnswer: "Признак предмета", hint: "Прилагательное отвечает на \"какой?\"" },
      { type: 'quiz', question: "Укажи прилагательные:", options: ["Красивый", "Красота", "Дом", "Не знаю", "Другой вариант"], correctAnswer: "Красивый", hint: "Прилагательные описывают предметы" },
      { type: 'quiz', question: "На какой вопрос отвечает прилагательное?", options: ["Что?", "Какой?", "Что делает?", "Первый", "Второй"], correctAnswer: "Какой?", hint: "Какой? - это признак" },
      { type: 'quiz', question: "Зелёный (какой?) - это ...", options: ["существительное", "глагол", "прилагательное", "числительное", "наречие"], correctAnswer: "прилагательное", hint: "Прилагательное = признак" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь прилагательные! ✍️" }
  },
  {
    title: "Части тела",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Чем мы видим?", options: ["Ушами", "Глазами", "Носом", "Не знаю", "Другой вариант"], correctAnswer: "Глазами", hint: "Глаза - орган зрения" },
      { type: 'quiz', question: "Укажи органы чувств:", options: ["Глаза", "Рука", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Глаза", hint: "Пять органов чувств" },
      { type: 'quiz', question: "Чем мы слышим?", options: ["Глазами", "Ушами", "Ртом", "Не знаю", "Другой вариант"], correctAnswer: "Ушами", hint: "Уши - орган слуха" },
      { type: 'quiz', question: "Нос - орган ...", options: ["существительное", "обоняния", "прилагательное", "глагол", "наречие"], correctAnswer: "обоняния", hint: "Обоняние = чувство запаха" },
      { type: 'quiz', question: "Что относится к живой природе?", options: ["Камень 🪨", "Дерево 🌳", "Вода 💧", "Солнце ☀️", "Гора ⛰️"], correctAnswer: "Дерево 🌳", hint: "Дерево - живое" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь органы чувств! 👃" }
  },
  {
    title: "Present Simple",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I ___ to school every day.", options: ["go", "goes", "going", "Не знаю", "Другой вариант"], correctAnswer: "go", hint: "I go = я хожу" },
      { type: 'quiz', question: "She ___ to school.", options: ["go", "goes", "going", "Не знаю", "Другой вариант"], correctAnswer: "goes", hint: "She goes = она ходит" },
      { type: 'quiz', question: "They ... (play) football. (play)", options: ["существительное", "play", "глагол", "наречие", "прилагательное"], correctAnswer: "play", hint: "They play = они играют" },
      { type: 'quiz', question: "Укажи маркеры Present Simple:", options: ["Every day", "Yesterday", "Last week", "Не знаю", "Другой вариант"], correctAnswer: "Every day", hint: "Present Simple = регулярно" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Great! Ты знаешь Present Simple! 🇬🇧" }
  },
  {
    title: "Дни недели и месяцы",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Monday - это...", options: ["Вторник", "Понедельник", "Среда", "Не знаю", "Другой вариант"], correctAnswer: "Понедельник", hint: "Monday = понедельник" },
      { type: 'quiz', question: "Как будет \"пятница\"?", options: ["Friday", "Monday", "Sunday", "Не знаю", "Другой вариант"], correctAnswer: "Friday", hint: "Friday = пятница" },
      { type: 'quiz', question: "Sunday = ... (воскресенье)", options: ["прилагательное", "глагол", "воскресенье", "наречие", "существительное"], correctAnswer: "воскресенье", hint: "Sunday = воскресенье" },
      { type: 'quiz', question: "Укажи дни недели:", options: ["Monday", "January", "December", "Не знаю", "Другой вариант"], correctAnswer: "Monday", hint: "Days of the week" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Wonderful! Ты знаешь дни недели! 📅" }
  }
]
