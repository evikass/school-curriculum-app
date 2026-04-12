// Экспорт игр для 2 класса
import { GameLesson } from '../types'

export const secondGradeGames: GameLesson[] = [
  // ========== РУССКИЙ ЯЗЫК ==========
  {
    title: "Части речи",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Что такое имя существительное?", options: ["Предмет", "Действие", "Признак", "Число", "Место"], correctAnswer: "Предмет", hint: "Существительное отвечает на вопрос КТО? ЧТО?" },
      { type: 'find', question: "Выбери имена существительные:", options: ["Бежать", "Стол 🪑", "Красивый", "Книга 📖", "Петь"], correctAnswer: ["Стол 🪑", "Книга 📖"], hint: "Существительное = предмет" },
      { type: 'quiz', question: "На какой вопрос отвечает глагол?", options: ["Какой?", "Что делать?", "Кто?", "Сколько?", "Где?"], correctAnswer: "Что делать?", hint: "Глагол = действие" },
      { type: 'find', question: "Выбери глаголы:", options: ["Бежать 🏃", "Стол 🪑", "Петь 🎤", "Красивый", "Рисовать 🎨"], correctAnswer: ["Бежать 🏃", "Петь 🎤", "Рисовать 🎨"], hint: "Глагол обозначает действие" },
      { type: 'quiz', question: "На какой вопрос отвечает имя прилагательное?", options: ["Кто?", "Что делать?", "Какой?", "Где?", "Когда?"], correctAnswer: "Какой?", hint: "Прилагательное = признак предмета" }
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь части речи! 📝" }
  },
  {
    title: "Корень слова",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Что такое корень слова?", options: ["Окончание", "Главная часть слова", "Приставка", "Суффикс", "Окончание"], correctAnswer: "Главная часть слова", hint: "В корне заключён главный смысл" },
      { type: 'find', question: "Найди однокоренные слова к слову ЛЕС:", options: ["Лесник 🌲", "Лиса 🦊", "Лесной 🌳", "Лист 🍃", "Перелесок"], correctAnswer: ["Лесник 🌲", "Лесной 🌳", "Перелесок"], hint: "Однокоренные слова имеют общий корень" },
      { type: 'quiz', question: "Какой корень в слове ВОДНЫЙ?", options: ["ВОД", "ВОДН", "НЫЙ", "НЫ", "ВО"], correctAnswer: "ВОД", hint: "Найди общую часть с похожими словами" },
      { type: 'quiz', question: "Какое слово лишнее?", options: ["Гора ⛰️", "Горный", "Гореть 🔥", "Пригорок", "Горка"], correctAnswer: "Гореть 🔥", hint: "Проверь значение корня" },
      { type: 'find', question: "Найди однокоренные слова к слову СНЕГ:", options: ["Снег 🌨️", "Снежный", "Снегирь 🐦", "Снежок", "Снеговик ⛄"], correctAnswer: ["Снег 🌨️", "Снежный", "Снегирь 🐦", "Снежок", "Снеговик ⛄"], hint: "Все эти слова содержат корень -СНЕГ-" }
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь корень слова! 🌱" }
  },
  {
    title: "Правописание приставок",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Приставка - это...", options: ["Конец слова", "Часть перед корнем", "Корень", "Суффикс", "Окончание"], correctAnswer: "Часть перед корнем", hint: "Приставка стоит ПЕРЕД корнем" },
      { type: 'find', question: "Найди слова с приставкой ПРИ-:", options: ["Приехал 🚗", "Пример", "Прыгнул", "Пришёл 🚶", "Праздник"], correctAnswer: ["Приехал 🚗", "Пример", "Пришёл 🚶"], hint: "ПРИ- = приближение, присоединение" },
      { type: 'quiz', question: "Сколько приставок в слове ПЕРЕПРИШЁЛ?", options: ["1", "2", "3", "0", "4"], correctAnswer: "2", hint: "ПЕРЕ- и ПРИ- - две приставки" },
      { type: 'fill', question: "Вставь приставку: __ехал (приблизился)", correctAnswer: "При", hint: "Приближение = ПРИ-" },
      { type: 'find', question: "Найди слова с приставкой ЗА-:", options: ["Забежал 🏃", "Записал ✏️", "Замок 🔒", "Захотел", "Завтра"], correctAnswer: ["Забежал 🏃", "Записал ✏️", "Захотел"], hint: "ЗА- = начало действия" }
    ],
    reward: { stars: 3, message: "Умница! Ты знаешь приставки! 📖" }
  },

  // ========== МАТЕМАТИКА ==========
  {
    title: "Сложение до 20",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "8 + 7 = ?", options: ["13", "14", "15", "16", "17"], correctAnswer: "15", hint: "8 + 7 = 15" },
      { type: 'quiz', question: "9 + 6 = ?", options: ["14", "15", "16", "13", "17"], correctAnswer: "15", hint: "9 + 6 = 15" },
      { type: 'fill', question: "12 + __ = 18", correctAnswer: "6", hint: "Сколько добавить?" },
      { type: 'quiz', question: "15 + 5 = ?", options: ["19", "20", "21", "18", "22"], correctAnswer: "20", hint: "15 + 5 = 20" },
      { type: 'quiz', question: "7 + 8 = ?", options: ["14", "15", "16", "13", "17"], correctAnswer: "15", hint: "7 + 8 = 15" }
    ],
    reward: { stars: 3, message: "Отлично! Ты умеешь складывать до 20! ➕" }
  },
  {
    title: "Вычитание до 20",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "18 - 9 = ?", options: ["8", "9", "10", "7", "11"], correctAnswer: "9", hint: "18 - 9 = 9" },
      { type: 'quiz', question: "15 - 7 = ?", options: ["7", "8", "9", "6", "10"], correctAnswer: "8", hint: "15 - 7 = 8" },
      { type: 'fill', question: "20 - __ = 14", correctAnswer: "6", hint: "Сколько отнять?" },
      { type: 'quiz', question: "16 - 8 = ?", options: ["7", "8", "9", "6", "10"], correctAnswer: "8", hint: "16 - 8 = 8" },
      { type: 'quiz', question: "14 - 6 = ?", options: ["7", "8", "9", "6", "10"], correctAnswer: "8", hint: "14 - 6 = 8" }
    ],
    reward: { stars: 3, message: "Супер! Ты умеешь вычитать! ➖" }
  },
  {
    title: "Умножение",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "2 × 3 = ?", options: ["5", "6", "7", "4", "8"], correctAnswer: "6", hint: "2 + 2 + 2 = 6" },
      { type: 'quiz', question: "3 × 4 = ?", options: ["10", "11", "12", "9", "13"], correctAnswer: "12", hint: "3 + 3 + 3 + 3 = 12" },
      { type: 'quiz', question: "5 × 2 = ?", options: ["7", "10", "12", "8", "9"], correctAnswer: "10", hint: "5 + 5 = 10" },
      { type: 'fill', question: "4 × __ = 8", correctAnswer: "2", hint: "Какое число умножить?" },
      { type: 'quiz', question: "2 × 5 = ?", options: ["7", "10", "12", "8", "9"], correctAnswer: "10", hint: "2 + 2 + 2 + 2 + 2 = 10" }
    ],
    reward: { stars: 3, message: "Здорово! Ты изучаешь умножение! ✖️" }
  },
  {
    title: "Деление",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "6 ÷ 2 = ?", options: ["2", "3", "4", "1", "5"], correctAnswer: "3", hint: "6 разделить на 2 части" },
      { type: 'quiz', question: "10 ÷ 5 = ?", options: ["1", "2", "5", "3", "4"], correctAnswer: "2", hint: "10 разделить на 5" },
      { type: 'quiz', question: "8 ÷ 4 = ?", options: ["2", "3", "4", "1", "5"], correctAnswer: "2", hint: "8 разделить на 4" },
      { type: 'fill', question: "12 ÷ __ = 3", correctAnswer: "4", hint: "На сколько разделить 12?" },
      { type: 'quiz', question: "9 ÷ 3 = ?", options: ["2", "3", "4", "1", "5"], correctAnswer: "3", hint: "9 разделить на 3" }
    ],
    reward: { stars: 3, message: "Замечательно! Ты изучаешь деление! ➗" }
  },

  // ========== ЛИТЕРАТУРА ==========
  {
    title: "Русские писатели",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Кто написал «Мойдодыр»?", options: ["Пушкин", "Чуковский", "Барто", "Маршак", "Михалков"], correctAnswer: "Чуковский", hint: "Корней Чуковский" },
      { type: 'quiz', question: "Кто написал «Муха-Цокотуха»?", options: ["Маршак", "Чуковский", "Михалков", "Пушкин", "Барто"], correctAnswer: "Чуковский", hint: "Тот же автор, что и Мойдодыр" },
      { type: 'find', question: "Выбери произведения Пушкина:", options: ["Сказка о рыбаке и рыбке", "Мойдодыр", "Сказка о царе Салтане", "Колобок", "У Лукоморья дуб зелёный"], correctAnswer: ["Сказка о рыбаке и рыбке", "Сказка о царе Салтане", "У Лукоморья дуб зелёный"], hint: "Александр Сергеевич Пушкин" },
      { type: 'quiz', question: "Кто автор стихов про игрушки?", options: ["Барто", "Маршак", "Чуковский", "Пушкин", "Михалков"], correctAnswer: "Барто", hint: "Агния Барто писала про игрушки" },
      { type: 'quiz', question: "Кто написал «Дядя Стёпа»?", options: ["Маршак", "Чуковский", "Михалков", "Пушкин", "Барто"], correctAnswer: "Михалков", hint: "Сергей Михалков написал про Дядю Стёпу" }
    ],
    reward: { stars: 3, message: "Прекрасно! Ты знаешь писателей! 📚" }
  },

  // ========== ОКРУЖАЮЩИЙ МИР ==========
  {
    title: "Планета Земля",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какая планета наша?", options: ["Марс 🔴", "Земля 🌍", "Луна 🌙", "Венера", "Юпитер"], correctAnswer: "Земля 🌍", hint: "Мы живём на планете Земля" },
      { type: 'quiz', question: "Что такое Солнце?", options: ["Планета", "Звезда ⭐", "Спутник", "Комета", "Астероид"], correctAnswer: "Звезда ⭐", hint: "Солнце - это звезда!" },
      { type: 'find', question: "Выбери планеты:", options: ["Земля 🌍", "Солнце ☀️", "Марс 🔴", "Луна 🌙", "Венера"], correctAnswer: ["Земля 🌍", "Марс 🔴", "Венера"], hint: "Планеты вращаются вокруг Солнца" },
      { type: 'quiz', question: "Луна - это...", options: ["Планета", "Спутник Земли", "Звезда", "Комета", "Астероид"], correctAnswer: "Спутник Земли", hint: "Луна вращается вокруг Земли" },
      { type: 'quiz', question: "Сколько планет в Солнечной системе?", options: ["6", "7", "8", "9", "10"], correctAnswer: "8", hint: "8 планет: Меркурий, Венера, Земля, Марс, Юпитер, Сатурн, Уран, Нептун" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь космос! 🚀" }
  },
  {
    title: "Природа России",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какое животное символ России?", options: ["Медведь 🐻", "Тигр 🐯", "Лиса 🦊", "Волк 🐺", "Орёл 🦅"], correctAnswer: "Медведь 🐻", hint: "Большой бурый медведь" },
      { type: 'find', question: "Что растёт в лесу?", options: ["Берёза 🌳", "Ель 🌲", "Кактус 🌵", "Пальма 🌴", "Сосна"], correctAnswer: ["Берёза 🌳", "Ель 🌲", "Сосна"], hint: "Русский лес" },
      { type: 'quiz', question: "Какое озеро самое глубокое?", options: ["Каспийское", "Байкал", "Ладожское", "Онежское", "Ильмень"], correctAnswer: "Байкал", hint: "Байкал - самое глубокое в мире" },
      { type: 'quiz', question: "Столица России?", options: ["Петербург", "Москва", "Казань", "Новосибирск", "Екатеринбург"], correctAnswer: "Москва", hint: "Москва - столица России" },
      { type: 'quiz', question: "Какая река самая длинная в России?", options: ["Волга", "Дон", "Обь", "Енисей", "Лена"], correctAnswer: "Волга", hint: "Волга - самая длинная река Европы" }
    ],
    reward: { stars: 3, message: "Молодец! Ты знаешь Россию! 🇷🇺" }
  },

  // ========== АНГЛИЙСКИЙ ==========
  {
    title: "Животные по-английски",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Cat - это...", options: ["Собака 🐕", "Кошка 🐱", "Птица 🐦", "Рыба 🐟", "Лошадь 🐴"], correctAnswer: "Кошка 🐱", hint: "Cat = кошка" },
      { type: 'quiz', question: "Как будет «собака»?", options: ["Cat", "Dog", "Bird", "Fish", "Horse"], correctAnswer: "Dog", hint: "Dog = собака" },
      { type: 'find', question: "Выбери названия животных:", options: ["Cat 🐱", "Red", "Dog 🐕", "Big", "Bird 🐦"], correctAnswer: ["Cat 🐱", "Dog 🐕", "Bird 🐦"], hint: "Animals = животные" },
      { type: 'quiz', question: "Что такое Fish?", options: ["Птица 🐦", "Рыба 🐟", "Животное 🐾", "Кошка 🐱", "Собака 🐕"], correctAnswer: "Рыба 🐟", hint: "Fish = рыба" },
      { type: 'quiz', question: "Что такое Bear?", options: ["Лиса 🦊", "Волк 🐺", "Медведь 🐻", "Заяц 🐰", "Ёж 🦔"], correctAnswer: "Медведь 🐻", hint: "Bear = медведь" }
    ],
    reward: { stars: 3, message: "Wonderful! Замечательно! 🐾" }
  },
  {
    title: "Семья по-английски",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Mother - это...", options: ["Папа", "Мама", "Бабушка", "Сестра", "Тётя"], correctAnswer: "Мама", hint: "Mother = мама" },
      { type: 'quiz', question: "Как будет «папа»?", options: ["Mother", "Father", "Sister", "Brother", "Grandma"], correctAnswer: "Father", hint: "Father = папа" },
      { type: 'find', question: "Выбери слова о семье:", options: ["Mother 👩", "Cat 🐱", "Father 👨", "Dog 🐕", "Sister 👧"], correctAnswer: ["Mother 👩", "Father 👨", "Sister 👧"], hint: "Family = семья" },
      { type: 'quiz', question: "Brother - это...", options: ["Сестра", "Брат", "Дедушка", "Бабушка", "Дядя"], correctAnswer: "Брат", hint: "Brother = брат" },
      { type: 'quiz', question: "Grandmother - это...", options: ["Мама", "Бабушка", "Тётя", "Сестра", "Дочь"], correctAnswer: "Бабушка", hint: "Grandmother = бабушка" }
    ],
    reward: { stars: 3, message: "Great! Отлично! 👨‍👩‍👧‍👦" }
  },

  // ========== НОВЫЕ ИГРЫ ==========
  {
    title: "Умножение на 2 и 3",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'fill', question: "2 × 6 = __", correctAnswer: "12", hint: "2 + 2 + 2 + 2 + 2 + 2 = 12" },
      { type: 'fill', question: "3 × 4 = __", correctAnswer: "12", hint: "3 + 3 + 3 + 3 = 12" },
      { type: 'quiz', question: "2 × 8 = ?", options: ["14", "16", "18", "12", "20"], correctAnswer: "16", hint: "2 × 8 = 16" },
      { type: 'quiz', question: "3 × 7 = ?", options: ["18", "21", "24", "20", "22"], correctAnswer: "21", hint: "3 × 7 = 21" },
      { type: 'fill', question: "3 × 9 = __", correctAnswer: "27", hint: "3 × 9 = 27" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь таблицу умножения! ✖️" }
  },
  {
    title: "Деление на 2 и 3",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'fill', question: "12 ÷ 2 = __", correctAnswer: "6", hint: "Какое число × 2 = 12?" },
      { type: 'fill', question: "15 ÷ 3 = __", correctAnswer: "5", hint: "Какое число × 3 = 15?" },
      { type: 'quiz', question: "18 ÷ 2 = ?", options: ["7", "8", "9", "6", "10"], correctAnswer: "9", hint: "9 × 2 = 18" },
      { type: 'quiz', question: "21 ÷ 3 = ?", options: ["6", "7", "8", "5", "9"], correctAnswer: "7", hint: "7 × 3 = 21" },
      { type: 'fill', question: "24 ÷ 3 = __", correctAnswer: "8", hint: "Какое число × 3 = 24?" }
    ],
    reward: { stars: 3, message: "Супер! Ты умеешь делить! ➗" }
  },
  {
    title: "Правописание ЖИ-ШИ",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'fill', question: "Маш__на (И/Ы)", correctAnswer: "И", hint: "ЖИ-ШИ пиши с И!" },
      { type: 'fill', question: "Ш__на (И/Ы)", correctAnswer: "И", hint: "ШИ пиши с И!" },
      { type: 'find', question: "Выбери слова с ЖИ-ШИ:", options: ["Жираф", "Шина", "Машина", "Жизнь", "Шар"], correctAnswer: ["Жираф", "Шина", "Машина", "Жизнь"], hint: "ЖИ-ШИ пишутся с И" },
      { type: 'quiz', question: "В слове «лыжи» пишется:", options: ["И", "Ы", "Е", "Ю", "А"], correctAnswer: "И", hint: "ЖИ пиши с И" },
      { type: 'fill', question: "Ш__шки (И/Ы)", correctAnswer: "И", hint: "ШИ пиши с И!" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь правило ЖИ-ШИ! ✍️" }
  },
  {
    title: "Правописание ЧА-ЩА",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'fill', question: "Туч__ (А/Я)", correctAnswer: "А", hint: "ЧА-ЩА пиши с А!" },
      { type: 'fill', question: "Рощ__ (А/Я)", correctAnswer: "А", hint: "ЩА пиши с А!" },
      { type: 'find', question: "Выбери слова с ЧА-ЩА:", options: ["Чаща", "Чаша", "Роща", "Туча", "Чай"], correctAnswer: ["Чаща", "Чаша", "Роща", "Туча"], hint: "ЧА-ЩА пишутся с А" },
      { type: 'quiz', question: "В слове «дача» пишется:", options: ["А", "Я", "Е", "О", "У"], correctAnswer: "А", hint: "ЧА пиши с А" },
      { type: 'fill', question: "Ч__сики (А/Я)", correctAnswer: "А", hint: "ЧА пиши с А!" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь правило ЧА-ЩА! ✍️" }
  },
  {
    title: "Правописание ЧУ-ЩУ",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'fill', question: "Щ__ка (У/Ю)", correctAnswer: "У", hint: "ЧУ-ЩУ пиши с У!" },
      { type: 'fill', question: "Ч__до (У/Ю)", correctAnswer: "У", hint: "ЧУ пиши с У!" },
      { type: 'find', question: "Выбери слова с ЧУ-ЩУ:", options: ["Щука", "Чудо", "Чугун", "Щупальце", "Чудак"], correctAnswer: ["Щука", "Чудо", "Чугун", "Щупальце", "Чудак"], hint: "ЧУ-ЩУ пишутся с У" },
      { type: 'quiz', question: "В слове «чулок» пишется:", options: ["У", "Ю", "О", "Е", "А"], correctAnswer: "У", hint: "ЧУ пиши с У" },
      { type: 'fill', question: "Щ__ки (У/Ю)", correctAnswer: "У", hint: "ЩУ пиши с У!" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь правило ЧУ-ЩУ! ✍️" }
  },
  {
    title: "Правописание ЧК-ЧН",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "В слове «ночка» мягкий знак:", options: ["Нужен", "Не нужен", "Не знаю", "Иногда", "Обязательно"], correctAnswer: "Не нужен", hint: "ЧК-ЧН пишутся без мягкого знака!" },
      { type: 'quiz', question: "В слове «ночной» мягкий знак:", options: ["Нужен", "Не нужен", "Не знаю", "Иногда", "Обязательно"], correctAnswer: "Не нужен", hint: "ЧК-ЧН пишутся без мягкого знака!" },
      { type: 'find', question: "Выбери слова без мягкого знака:", options: ["Ночка", "Ночной", "Точка", "Тучка", "Ручка"], correctAnswer: ["Ночка", "Ночной", "Точка", "Тучка", "Ручка"], hint: "ЧК-ЧН без Ь" },
      { type: 'fill', question: "В слове «дочка» мягкий знак __", correctAnswer: "не нужен", hint: "ЧК без Ь" },
      { type: 'fill', question: "В слове «срочный» мягкий знак __", correctAnswer: "не нужен", hint: "ЧН без Ь" }
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь правило ЧК-ЧН! ✍️" }
  },
  {
    title: "Слова-предметы",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "На какой вопрос отвечает слово «стол»?", options: ["Что делает?", "Какой?", "Что?", "Где?", "Когда?"], correctAnswer: "Что?", hint: "Стол - это предмет" },
      { type: 'find', question: "Выбери слова-предметы:", options: ["Книга", "Бежать", "Красивый", "Стол", "Прыгать"], correctAnswer: ["Книга", "Стол"], hint: "Слова-предметы отвечают на «кто? что?»" },
      { type: 'quiz', question: "Слово «мама» - это:", options: ["Предмет", "Действие", "Признак", "Число", "Место"], correctAnswer: "Предмет", hint: "Мама - это кто?" },
      { type: 'quiz', question: "На какой вопрос отвечает слово «кот»?", options: ["Что делает?", "Кто?", "Какой?", "Где?", "Сколько?"], correctAnswer: "Кто?", hint: "Кот - это кто?" },
      { type: 'find', question: "Выбери слова, которые НЕ являются предметами:", options: ["Кот 🐱", "Бежать", "Красивый", "Яблоко 🍎", "Петь"], correctAnswer: ["Бежать", "Красивый", "Петь"], hint: "Предметы отвечают на «кто? что?»" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь слова-предметы! 📝" }
  },
  {
    title: "Слова-признаки",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "На какой вопрос отвечает слово «красивый»?", options: ["Что делает?", "Какой?", "Что?", "Где?", "Когда?"], correctAnswer: "Какой?", hint: "Красивый - это признак" },
      { type: 'find', question: "Выбери слова-признаки:", options: ["Большой", "Бежать", "Красный", "Стол", "Быстрый"], correctAnswer: ["Большой", "Красный", "Быстрый"], hint: "Слова-признаки отвечают на «какой? какая? какое?»" },
      { type: 'quiz', question: "Слово «зелёный» - это:", options: ["Предмет", "Действие", "Признак", "Число", "Место"], correctAnswer: "Признак", hint: "Зелёный - это какой?" },
      { type: 'quiz', question: "На какой вопрос отвечает слово «умный»?", options: ["Что делает?", "Кто?", "Какой?", "Где?", "Сколько?"], correctAnswer: "Какой?", hint: "Умный - это какой?" },
      { type: 'find', question: "Выбери слова-признаки:", options: ["Добрый", "Книга", "Яркий", "Бежать", "Сладкий"], correctAnswer: ["Добрый", "Яркий", "Сладкий"], hint: "Признаки описывают предметы" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь слова-признаки! 📝" }
  },
  {
    title: "Овощи и фрукты",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'find', question: "Выбери овощи:", options: ["Морковь 🥕", "Яблоко 🍎", "Огурец 🥒", "Груша 🍐", "Помидор 🍅"], correctAnswer: ["Морковь 🥕", "Огурец 🥒", "Помидор 🍅"], hint: "Овощи растут в огороде" },
      { type: 'find', question: "Выбери фрукты:", options: ["Яблоко 🍎", "Морковь 🥕", "Банан 🍌", "Огурец 🥒", "Груша 🍐"], correctAnswer: ["Яблоко 🍎", "Банан 🍌", "Груша 🍐"], hint: "Фрукты растут на деревьях" },
      { type: 'quiz', question: "Где растут овощи?", options: ["На деревьях", "В огороде", "В лесу", "В реке", "В небе"], correctAnswer: "В огороде", hint: "Огород - место для овощей" },
      { type: 'quiz', question: "Что полезнее: фрукт или конфета?", options: ["Фрукт", "Конфета", "Одинаково", "Мороженое", "Торт"], correctAnswer: "Фрукт", hint: "Фрукты содержат витамины" },
      { type: 'find', question: "Выбери ягоды:", options: ["Клубника 🍓", "Морковь 🥕", "Малина", "Банан 🍌", "Черника"], correctAnswer: ["Клубника 🍓", "Малина", "Черника"], hint: "Ягоды - мелкие плоды" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь овощи и фрукты! 🥗" }
  },
  {
    title: "Еда по-английски",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Apple - это...", options: ["Апельсин", "Яблоко 🍎", "Банан", "Груша", "Виноград"], correctAnswer: "Яблоко 🍎", hint: "Apple = яблоко" },
      { type: 'quiz', question: "Как будет «хлеб»?", options: ["Bread", "Water", "Milk", "Cheese", "Meat"], correctAnswer: "Bread", hint: "Bread = хлеб" },
      { type: 'find', question: "Выбери названия еды:", options: ["Apple 🍎", "Cat 🐱", "Bread 🍞", "Dog 🐕", "Milk 🥛"], correctAnswer: ["Apple 🍎", "Bread 🍞", "Milk 🥛"], hint: "Food = еда" },
      { type: 'fill', question: "Water = __ (вода)", correctAnswer: "вода", hint: "Water = вода" },
      { type: 'quiz', question: "Что такое Cheese?", options: ["Хлеб", "Сыр 🧀", "Молоко", "Мясо", "Рыба"], correctAnswer: "Сыр 🧀", hint: "Cheese = сыр" }
    ],
    reward: { stars: 3, message: "Great! Отлично! 🍎" }
  },

  // ========== НОВЫЕ ИГРЫ v3.41 ==========
  {
    title: "Таблица умножения на 4 и 5",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'fill', question: "4 × 4 = __", correctAnswer: "16", hint: "4 × 4 = 16" },
      { type: 'fill', question: "5 × 5 = __", correctAnswer: "25", hint: "5 × 5 = 25" },
      { type: 'quiz', question: "4 × 6 = ?", options: ["20", "24", "28", "22", "26"], correctAnswer: "24", hint: "4 × 6 = 24" },
      { type: 'quiz', question: "5 × 7 = ?", options: ["30", "35", "40", "32", "38"], correctAnswer: "35", hint: "5 × 7 = 35" },
      { type: 'fill', question: "4 × 9 = __", correctAnswer: "36", hint: "4 × 9 = 36" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь таблицу умножения! ✖️" }
  },
  {
    title: "Периметр и площадь",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Периметр квадрата со стороной 3:", options: ["6", "9", "12", "15", "18"], correctAnswer: "12", hint: "P = 4 × 3 = 12" },
      { type: 'fill', question: "Периметр прямоугольника 2 и 4 = __", correctAnswer: "12", hint: "P = 2 × (2 + 4) = 12" },
      { type: 'quiz', question: "Площадь квадрата со стороной 4:", options: ["8", "12", "16", "20", "24"], correctAnswer: "16", hint: "S = 4 × 4 = 16" },
      { type: 'fill', question: "Площадь прямоугольника 3 × 5 = __", correctAnswer: "15", hint: "S = 3 × 5 = 15" },
      { type: 'quiz', question: "Периметр квадрата со стороной 5:", options: ["15", "20", "25", "10", "30"], correctAnswer: "20", hint: "P = 4 × 5 = 20" }
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь периметр и площадь! 📐" }
  },
  {
    title: "Имя прилагательное",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Имя прилагательное обозначает:", options: ["Предмет", "Признак предмета", "Действие", "Число", "Место"], correctAnswer: "Признак предмета", hint: "Прилагательное отвечает на «какой?»" },
      { type: 'find', question: "Выбери прилагательные:", options: ["Красивый", "Красота", "Большой", "Дом", "Быстрый"], correctAnswer: ["Красивый", "Большой", "Быстрый"], hint: "Прилагательные описывают предметы" },
      { type: 'quiz', question: "На какой вопрос отвечает прилагательное?", options: ["Что?", "Какой?", "Что делает?", "Где?", "Когда?"], correctAnswer: "Какой?", hint: "Какой? - это признак" },
      { type: 'fill', question: "Зелёный (какой?) - это __", correctAnswer: "прилагательное", hint: "Прилагательное = признак" },
      { type: 'find', question: "Выбери прилагательные:", options: ["Весёлый", "Играть", "Маленький", "Книга", "Тёплый"], correctAnswer: ["Весёлый", "Маленький", "Тёплый"], hint: "Прилагательные описывают предметы" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь прилагательные! ✍️" }
  },
  {
    title: "Части тела",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Чем мы видим?", options: ["Ушами", "Глазами", "Носом", "Ртом", "Кожей"], correctAnswer: "Глазами", hint: "Глаза - орган зрения" },
      { type: 'find', question: "Выбери органы чувств:", options: ["Глаза", "Уши", "Рука", "Нос", "Язык"], correctAnswer: ["Глаза", "Уши", "Нос", "Язык"], hint: "Пять органов чувств" },
      { type: 'quiz', question: "Чем мы слышим?", options: ["Глазами", "Ушами", "Ртом", "Носом", "Кожей"], correctAnswer: "Ушами", hint: "Уши - орган слуха" },
      { type: 'fill', question: "Нос - орган __", correctAnswer: "обоняния", hint: "Обоняние = чувство запаха" },
      { type: 'quiz', question: "Чем мы чувствуем вкус?", options: ["Глазами", "Ушами", "Языком", "Носом", "Кожей"], correctAnswer: "Языком", hint: "Язык - орган вкуса" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь органы чувств! 👃" }
  },
  {
    title: "Present Simple",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I ___ to school every day.", options: ["go", "goes", "going", "went", "gone"], correctAnswer: "go", hint: "I go = я хожу" },
      { type: 'quiz', question: "She ___ to school.", options: ["go", "goes", "going", "went", "gone"], correctAnswer: "goes", hint: "She goes = она ходит" },
      { type: 'fill', question: "They __ (play) football. (play)", correctAnswer: "play", hint: "They play = они играют" },
      { type: 'find', question: "Выбери маркеры Present Simple:", options: ["Every day", "Yesterday", "Usually", "Last week", "Always"], correctAnswer: ["Every day", "Usually", "Always"], hint: "Present Simple = регулярно" },
      { type: 'fill', question: "He __ (like) apples. (likes)", correctAnswer: "likes", hint: "He likes = ему нравится" }
    ],
    reward: { stars: 3, message: "Great! Ты знаешь Present Simple! 🇬🇧" }
  },
  {
    title: "Дни недели и месяцы",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Monday - это...", options: ["Вторник", "Понедельник", "Среда", "Четверг", "Пятница"], correctAnswer: "Понедельник", hint: "Monday = понедельник" },
      { type: 'quiz', question: "Как будет «пятница»?", options: ["Friday", "Monday", "Sunday", "Tuesday", "Saturday"], correctAnswer: "Friday", hint: "Friday = пятница" },
      { type: 'fill', question: "Sunday = __ (воскресенье)", correctAnswer: "воскресенье", hint: "Sunday = воскресенье" },
      { type: 'find', question: "Выбери дни недели:", options: ["Monday", "January", "Friday", "December", "Sunday"], correctAnswer: ["Monday", "Friday", "Sunday"], hint: "Days of the week" },
      { type: 'quiz', question: "January - это...", options: ["День недели", "Январь", "Время года", "Праздник", "Цвет"], correctAnswer: "Январь", hint: "January = январь" }
    ],
    reward: { stars: 3, message: "Wonderful! Ты знаешь дни недели! 📅" }
  }
]
