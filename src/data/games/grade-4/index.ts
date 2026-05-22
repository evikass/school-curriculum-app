// Экспорт игр для 4 класса
import { GameLesson } from '../types'

export const fourthGradeGames: GameLesson[] = [
  {
    title: "Многозначные числа",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Сколько сотен в числе 3521?", options: ["3", "5", "52", "1", "2"], correctAnswer: "5", hint: "3 тысячи, 5 сотен, 2 десятка, 1 единица" },
      { type: 'quiz', question: "Какое число больше: 4050 или 4500?", options: ["4050", "4500", "Они равны", "1", "2"], correctAnswer: "4500", hint: "Сравни разряды слева направо" },
      { type: 'quiz', question: "5432 + 1234 = ...", options: ["6664", "6668", "6666", "6656", "6661"], correctAnswer: "6666", hint: "Сложи поразрядно" },
      { type: 'quiz', question: "Округли 347 до сотен:", options: ["300", "340", "350", "Не знаю", "Другой вариант"], correctAnswer: "300", hint: "47 < 50, значит округляем вниз" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты работаешь с большими числами! 🔢" }
  },
  {
    title: "Действия с числами",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "25 × 4 = ?", options: ["80", "100", "125", "Не знаю", "Другой вариант"], correctAnswer: "100", hint: "25 × 4 = 100" },
      { type: 'quiz', question: "144 ÷ 12 = ?", options: ["10", "11", "12", "Не знаю", "Другой вариант"], correctAnswer: "12", hint: "12 × 12 = 144" },
      { type: 'quiz', question: "1000 - 367 = ...", options: ["635", "623", "633", "628", "631"], correctAnswer: "633", hint: "Вычти поразрядно" },
      { type: 'quiz', question: "Укажи верные равенства:", options: ["15×4=60", "100÷25=5", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "15×4=60", hint: "Проверь каждое" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Супер! Ты отлично считаешь! ✖️➗" }
  },
  {
    title: "Задачи на скорость",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Скорость 60 км/ч, время 2 ч. Какое расстояние?", options: ["30 км", "62 км", "120 км", "Первый", "Второй"], correctAnswer: "120 км", hint: "S = v × t" },
      { type: 'quiz', question: "Расстояние 180 км, время 3 ч. Найди скорость.", options: ["60 км/ч", "90 км/ч", "540 км/ч", "Не знаю", "Другой вариант"], correctAnswer: "60 км/ч", hint: "v = S ÷ t" },
      { type: 'quiz', question: "Скорость 50 км/ч, время 4 ч. Расстояние = ... км", options: ["202", "198", "200", "195", "190"], correctAnswer: "200", hint: "S = 50 × 4" },
      { type: 'quiz', question: "Формула расстояния?", options: ["S = v × t", "v = S × t", "t = S × v", "Не знаю", "Другой вариант"], correctAnswer: "S = v × t", hint: "Расстояние = скорость × время" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты решаешь задачи на движение! 🚗" }
  },
  {
    title: "Дроби и действия",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "1/2 + 1/4 = ?", options: ["1/6", "2/6", "3/4", "Не знаю", "Другой вариант"], correctAnswer: "3/4", hint: "Приведи к общему знаменателю: 2/4 + 1/4" },
      { type: 'quiz', question: "3/4 - 1/4 = ?", options: ["2/4", "2/0", "1/2", "Не знаю", "Другой вариант"], correctAnswer: "2/4", hint: "3/4 - 1/4 = 2/4 = 1/2" },
      { type: 'quiz', question: "Укажи равные дроби:", options: ["1/2 = 2/4", "2/3 = 4/9", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "1/2 = 2/4", hint: "Умножь числитель и знаменатель на одно число" },
      { type: 'quiz', question: "2/5 от 100 = ...", options: ["38", "40", "30", "35", "42"], correctAnswer: "40", hint: "100 ÷ 5 × 2 = 40" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Умница! Ты понимаешь дроби! 📊" }
  },
  {
    title: "Спряжения глаголов",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Глагол \"писать\" - какого спряжения?", options: ["I спряжение", "II спряжение", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "I спряжение", hint: "ПишЕШЬ - окончание -ЕШЬ (I спр.)" },
      { type: 'quiz', question: "Глагол \"говорить\" - какого спряжения?", options: ["I спряжение", "II спряжение", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "II спряжение", hint: "ГоворИШЬ - окончание -ИШЬ (II спр.)" },
      { type: 'quiz', question: "Укажи глаголы II спряжения:", options: ["Смотреть", "Делать", "Читать", "Не знаю", "Другой вариант"], correctAnswer: "Смотреть", hint: "II спряжение - окончания -ИТЬ, исключения" },
      { type: 'quiz', question: "Они пиш...т (I спр.)", options: ["ут", "глагол", "прилагательное", "наречие", "существительное"], correctAnswer: "ут", hint: "I спряжение, 3 лицо мн.ч. - -УТ/-ЮТ" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь спряжения! 📝" }
  },
  {
    title: "Непроизносимые согласные",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Вставь букву: Сер...це (сердечный)", options: ["существительное", "прилагательное", "д", "наречие", "глагол"], correctAnswer: "д", hint: "Проверочное слово - сердечный" },
      { type: 'quiz', question: "Как проверить непроизносимую согласную?", options: ["Подобрать проверочное слово", "Посмотреть в словаре", "Написать без неё", "Не знаю", "Другой вариант"], correctAnswer: "Подобрать проверочное слово", hint: "Нужно, чтобы согласная слышалась чётко" },
      { type: 'quiz', question: "Укажи слова с непроизносимой согласной:", options: ["Солнце (солнечный)", "Чудесный", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Солнце (солнечный)", hint: "Проверь, произносится ли согласная" },
      { type: 'quiz', question: "Чес...ный (честен) - честный", options: ["существительное", "наречие", "т", "прилагательное", "глагол"], correctAnswer: "т", hint: "Честен - проверочное слово" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Супер! Ты проверяешь согласные! ✅" }
  },
  {
    title: "Однородные члены",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Какой знак ставится между однородными членами без союза?", options: ["Запятая", "Тире", "Двоеточие", "Первый", "Второй"], correctAnswer: "Запятая", hint: "Однородные члены без союза разделяются запятыми" },
      { type: 'quiz', question: "Какой союз не требует запятой?", options: ["А", "И", "Но", "Первый", "Второй"], correctAnswer: "И", hint: "Перед И однородные члены не разделяются запятой" },
      { type: 'quiz', question: "Найди предложения с однородными членами:", options: ["Кошка ест и спит.", "Кошка спит.", "Дети играют.", "Не знаю", "Другой вариант"], correctAnswer: "Кошка ест и спит.", hint: "Однородные члены отвечают на один вопрос" },
      { type: 'quiz', question: "\"В саду растут яблони, груши ___ сливы.\" Какой знак?", options: ["Запятая", "Без знака", "Точка с запятой", "Первый", "Второй"], correctAnswer: "Без знака", hint: "Перед И запятая не ставится" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь синтаксис! 📚" }
  },
  {
    title: "Былины",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Кто главный герой былины об Илье Муромце?", options: ["Добрыня Никитич", "Илья Муромец", "Алёша Попович", "Пушкин", "Лермонтов"], correctAnswer: "Илья Муромец", hint: "Былина так и называется" },
      { type: 'quiz', question: "Сколько лет лежал Илья Муромец?", options: ["10 лет", "33 года", "50 лет", "1", "2"], correctAnswer: "33 года", hint: "\"Тридцать три года лежал Илья...\"" },
      { type: 'quiz', question: "Укажи русских богатырей:", options: ["Илья Муромец", "Змей Горыныч", "Баба Яга", "Не знаю", "Другой вариант"], correctAnswer: "Илья Муромец", hint: "Три главных богатыря" },
      { type: 'quiz', question: "Что такое былина?", options: ["Сказка", "Русская эпическая песня", "Стихотворение", "Не знаю", "Другой вариант"], correctAnswer: "Русская эпическая песня", hint: "Былина рассказывает о подвигах богатырей" },
      { type: 'quiz', question: "Что такое сказка?", options: ["Научная статья", "Стихотворение", "Выдуманная история", "Учебник", "Энциклопедия"], correctAnswer: "Выдуманная история", hint: "Сказка - вымышленный рассказ" },
    ],
    reward: { stars: 3, message: "Прекрасно! Ты знаешь былины! ⚔️" }
  },
  {
    title: "Поэзия XIX века",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Кто написал \"Бородино\"?", options: ["Пушкин", "Лермонтов", "Тютчев", "Гоголь", "Толстой"], correctAnswer: "Лермонтов", hint: "Михаил Юрьевич Лермонтов" },
      { type: 'quiz', question: "Кого называют \"солнцем русской поэзии\"?", options: ["Лермонтова", "Пушкина", "Есенина", "Не знаю", "Другой вариант"], correctAnswer: "Пушкина", hint: "Александр Сергеевич Пушкин" },
      { type: 'quiz', question: "Укажи поэтов XIX века:", options: ["Пушкин", "Есенин", "Маяковский", "Не знаю", "Другой вариант"], correctAnswer: "Пушкин", hint: "XIX век - золотой век русской поэзии" },
      { type: 'quiz', question: "Кто написал \"Парус\"?", options: ["Пушкин", "Лермонтов", "Тютчев", "Гоголь", "Толстой"], correctAnswer: "Лермонтов", hint: "\"Белеет парус одинокой...\"" },
      { type: 'quiz', question: "Что такое сказка?", options: ["Научная статья", "Стихотворение", "Выдуманная история", "Учебник", "Энциклопедия"], correctAnswer: "Выдуманная история", hint: "Сказка - вымышленный рассказ" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь поэзию! 📖" }
  },
  {
    title: "История Древней Руси",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Кто крестил Русь?", options: ["Иван Грозный", "Князь Владимир", "Пётр I", "Пушкин", "Лермонтов"], correctAnswer: "Князь Владимир", hint: "Владимир Святославич в 988 году" },
      { type: 'quiz', question: "В каком году была крещена Русь?", options: ["862", "988", "1147", "Не знаю", "Другой вариант"], correctAnswer: "988", hint: "Крещение Руси - 988 год" },
      { type: 'quiz', question: "Укажи города Древней Руси:", options: ["Киев", "Москва", "Санкт-Петербург", "Не знаю", "Другой вариант"], correctAnswer: "Киев", hint: "Москва и СПб основаны позже" },
      { type: 'quiz', question: "Кто призван на княжение в Новгород?", options: ["Олег", "Рюрик", "Владимир", "Пушкин", "Лермонтов"], correctAnswer: "Рюрик", hint: "862 год - призвание варягов" },
      { type: 'quiz', question: "Что относится к живой природе?", options: ["Камень 🪨", "Дерево 🌳", "Вода 💧", "Солнце ☀️", "Гора ⛰️"], correctAnswer: "Дерево 🌳", hint: "Дерево - живое" },
    ],
    reward: { stars: 3, message: "Здорово! Ты знаешь историю! 🏰" }
  },
  {
    title: "Организм человека",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какой орган перекачивает кровь?", options: ["Лёгкие", "Сердце", "Печень", "Первый", "Второй"], correctAnswer: "Сердце", hint: "Сердце - главный орган кровеносной системы" },
      { type: 'quiz', question: "Где происходит газообмен?", options: ["В сердце", "В лёгких", "В желудке", "Не знаю", "Другой вариант"], correctAnswer: "В лёгких", hint: "Лёгкие - орган дыхания" },
      { type: 'quiz', question: "Укажи органы пищеварения:", options: ["Желудок", "Сердце", "Лёгкие", "Не знаю", "Другой вариант"], correctAnswer: "Желудок", hint: "Пищеварительная система перерабатывает пищу" },
      { type: 'quiz', question: "Сколько костей в теле взрослого человека?", options: ["156", "206", "306", "1", "2"], correctAnswer: "206", hint: "В скелете взрослого 206 костей" },
      { type: 'quiz', question: "Что относится к живой природе?", options: ["Камень 🪨", "Дерево 🌳", "Вода 💧", "Солнце ☀️", "Гора ⛰️"], correctAnswer: "Дерево 🌳", hint: "Дерево - живое" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь анатомию! 🫀" }
  },
  {
    title: "Past Simple",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I ___ to the park yesterday.", options: ["go", "went", "going", "Не знаю", "Другой вариант"], correctAnswer: "went", hint: "Past Simple - прошедшее время" },
      { type: 'quiz', question: "She ... (play) football last week. (played)", options: ["наречие", "глагол", "существительное", "played", "прилагательное"], correctAnswer: "played", hint: "Правильный глагол + -ed" },
      { type: 'quiz', question: "Did you watch TV? - No, I ___.", options: ["didn\'t", "don\'t", "doesn\'t", "Не знаю", "Другой вариант"], correctAnswer: "didn\'t", hint: "Отрицание в Past Simple - didn\'t" },
      { type: 'quiz', question: "Укажи формы Past Simple:", options: ["went", "goes", "see", "Не знаю", "Другой вариант"], correctAnswer: "went", hint: "Past Simple - прошедшее время" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Great! Ты знаешь Past Simple! ⏮️" }
  },
  {
    title: "Degrees of comparison",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "big - bigger - ___", options: ["biggest", "more big", "bigger", "Не знаю", "Другой вариант"], correctAnswer: "biggest", hint: "Превосходная степень: the biggest" },
      { type: 'quiz', question: "good - better - ___", options: ["goodest", "best", "more good", "Не знаю", "Другой вариант"], correctAnswer: "best", hint: "good - better - the best (исключение)" },
      { type: 'quiz', question: "beautiful - more beautiful - ... beautiful", options: ["глагол", "прилагательное", "наречие", "most", "существительное"], correctAnswer: "most", hint: "Длинные слова: more/most" },
      { type: 'quiz', question: "Укажи правильные сравнения:", options: ["tall-taller-tallest", "good-gooder-goodest", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "tall-taller-tallest", hint: "good - better - best (исключение)" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Excellent! Степени сравнения! 📈" }
  },
  {
    title: "Умножение и деление",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "25 × 4 = ...", options: ["90", "98", "100", "102", "95"], correctAnswer: "100", hint: "25 × 4 = 100" },
      { type: 'quiz', question: "144 ÷ 12 = ...", options: ["14", "13", "11", "10", "12"], correctAnswer: "12", hint: "12 × 12 = 144" },
      { type: 'quiz', question: "15 × 6 = ?", options: ["80", "90", "100", "Не знаю", "Другой вариант"], correctAnswer: "90", hint: "15 × 6 = 90" },
      { type: 'quiz', question: "96 ÷ 8 = ?", options: ["10", "11", "12", "Не знаю", "Другой вариант"], correctAnswer: "12", hint: "8 × 12 = 96" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты умеешь умножать и делить! ✖️➗" }
  },
  {
    title: "Единицы измерения",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Сколько метров в 1 километре?", options: ["100", "1000", "10000", "1", "2"], correctAnswer: "1000", hint: "1 км = 1000 м" },
      { type: 'quiz', question: "1 час = ... минут", options: ["62", "58", "50", "60", "55"], correctAnswer: "60", hint: "В часе 60 минут" },
      { type: 'quiz', question: "Сколько граммов в 1 килограмме?", options: ["100", "1000", "10000", "1", "2"], correctAnswer: "1000", hint: "1 кг = 1000 г" },
      { type: 'quiz', question: "2 кг 500 г = ... г", options: ["2500", "2495", "2490", "2502", "2498"], correctAnswer: "2500", hint: "2000 + 500 = 2500" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь единицы измерения! 📏" }
  },
  {
    title: "Порядок действий",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Какое действие выполняется первым: 2 + 3 × 4?", options: ["Сложение", "Умножение", "Оба вместе", "Первый", "Второй"], correctAnswer: "Умножение", hint: "Сначала умножение и деление" },
      { type: 'quiz', question: "3 + 2 × 5 = ...", options: ["15", "11", "14", "13", "12"], correctAnswer: "13", hint: "Сначала 2 × 5 = 10, потом 3 + 10 = 13" },
      { type: 'quiz', question: "(4 + 3) × 2 = ?", options: ["10", "11", "14", "Не знаю", "Другой вариант"], correctAnswer: "14", hint: "Сначала скобки: 7 × 2 = 14" },
      { type: 'quiz', question: "10 - 2 × 3 = ...", options: ["6", "2", "5", "4", "3"], correctAnswer: "4", hint: "Сначала 2 × 3 = 6, потом 10 - 6 = 4" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь порядок действий! 🔢" }
  },
  {
    title: "Имя прилагательное",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Имя прилагательное обозначает:", options: ["Предмет", "Признак предмета", "Действие", "Не знаю", "Другой вариант"], correctAnswer: "Признак предмета", hint: "Прилагательное отвечает на \"какой? какая? какое?\"" },
      { type: 'quiz', question: "Укажи имена прилагательные:", options: ["Красивый", "Красота", "Бежать", "Не знаю", "Другой вариант"], correctAnswer: "Красивый", hint: "Прилагательные описывают предметы" },
      { type: 'quiz', question: "Прилагательное изменяется по:", options: ["Падежам", "Лицам", "Времени", "Не знаю", "Другой вариант"], correctAnswer: "Падежам", hint: "Прилагательные изменяются по падежам, числам и родам" },
      { type: 'quiz', question: "Прилагательное \"большой\" в женском роде: ...", options: ["большая", "глагол", "наречие", "прилагательное", "существительное"], correctAnswer: "большая", hint: "Большой дом, большая книга" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь прилагательные! ✍️" }
  },
  {
    title: "Глагол",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Глагол обозначает:", options: ["Предмет", "Признак", "Действие", "Не знаю", "Другой вариант"], correctAnswer: "Действие", hint: "Глагол отвечает на \"что делать? что сделать?\"" },
      { type: 'quiz', question: "Укажи глаголы:", options: ["Бежать", "Бег", "Красивый", "Письмо", "Не знаю"], correctAnswer: "Бежать", hint: "Глаголы обозначают действия" },
      { type: 'quiz', question: "Глаголы изменяются по:", options: ["Падежам", "Временам", "Родам", "Не знаю", "Другой вариант"], correctAnswer: "Временам", hint: "Прошедшее, настоящее, будущее время" },
      { type: 'quiz', question: "Глагол \"читать\" в прошедшем времени: ...", options: ["наречие", "прилагательное", "читал", "существительное", "глагол"], correctAnswer: "читал", hint: "Читать → читал" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь глаголы! 📝" }
  },
  {
    title: "Правописание приставок",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Приставки на -з/-с: какой согласный пишется перед к?", options: ["-з", "-с", "Любой", "Первый", "Второй"], correctAnswer: "-с", hint: "Перед к, п, т пишется -с (без-, бес-)" },
      { type: 'quiz', question: "Бе...шумный (з/с)", options: ["с", "ц", "з", "ш", "ж"], correctAnswer: "с", hint: "Бесшумный - перед ш пишется с" },
      { type: 'quiz', question: "Укажи слова с приставкой на -з:", options: ["Беззвездный", "Бесконечный", "Бесшумный", "Не знаю", "Другой вариант"], correctAnswer: "Беззвездный", hint: "-з перед звонкими, -с перед глухими" },
      { type: 'quiz', question: "В слове \"расписать\" пишется:", options: ["з", "с", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "с", hint: "Расписать - перед п пишется с" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь приставки! 📖" }
  },
  {
    title: "Сказки зарубежных писателей",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Кто написал \"Русалочка\"?", options: ["Андерсен", "Братья Гримм", "Перро", "Пушкин", "Лермонтов"], correctAnswer: "Андерсен", hint: "Ганс Христиан Андерсен" },
      { type: 'quiz', question: "Кто автор \"Золушки\"?", options: ["Андерсен", "Братья Гримм", "Перро", "Пушкин", "Лермонтов"], correctAnswer: "Перро", hint: "Шарль Перро - французский сказочник" },
      { type: 'quiz', question: "Укажи сказки Андерсена:", options: ["Русалочка", "Золушка", "Белоснежка", "Не знаю", "Другой вариант"], correctAnswer: "Русалочка", hint: "Андерсен - датский сказочник" },
      { type: 'quiz', question: "\"Бременские музыканты\" - авторы:", options: ["Андерсен", "Братья Гримм", "Перро", "Пушкин", "Лермонтов"], correctAnswer: "Братья Гримм", hint: "Немецкие сказочники" },
      { type: 'quiz', question: "Что такое сказка?", options: ["Научная статья", "Стихотворение", "Выдуманная история", "Учебник", "Энциклопедия"], correctAnswer: "Выдуманная история", hint: "Сказка - вымышленный рассказ" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь зарубежные сказки! 📚" }
  },
  {
    title: "Природа России",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какое животное - символ России?", options: ["Тигр", "Медведь", "Лиса", "Первый", "Второй"], correctAnswer: "Медведь", hint: "Бурый медведь - символ России" },
      { type: 'quiz', question: "Укажи растения России:", options: ["Берёза", "Кактус", "Пальма", "Не знаю", "Другой вариант"], correctAnswer: "Берёза", hint: "Типичные растения России" },
      { type: 'quiz', question: "Самое глубокое озеро в мире:", options: ["Каспийское", "Байкал", "Ладожское", "Не знаю", "Другой вариант"], correctAnswer: "Байкал", hint: "Байкал - глубочайшее озеро" },
      { type: 'quiz', question: "Столица России - ...", options: ["наречие", "существительное", "прилагательное", "Москва", "глагол"], correctAnswer: "Москва", hint: "Москва - столица нашей страны" },
      { type: 'quiz', question: "Что относится к живой природе?", options: ["Камень 🪨", "Дерево 🌳", "Вода 💧", "Солнце ☀️", "Гора ⛰️"], correctAnswer: "Дерево 🌳", hint: "Дерево - живое" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь Россию! 🇷🇺" }
  },
  {
    title: "Охрана природы",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Что такое Красная книга?", options: ["Книга о природе", "Список редких животных", "Учебник", "Не знаю", "Другой вариант"], correctAnswer: "Список редких животных", hint: "Красная книга содержит редкие и исчезающие виды" },
      { type: 'quiz', question: "Укажи, что загрязняет природу:", options: ["Заводы", "Леса", "Парки", "Не знаю", "Другой вариант"], correctAnswer: "Заводы", hint: "Источники загрязнения" },
      { type: 'quiz', question: "Почему нельзя сжигать листья?", options: ["Не красиво", "Опасный дым", "Холодно", "Не знаю", "Другой вариант"], correctAnswer: "Опасный дым", hint: "При горении выделяются вредные вещества" },
      { type: 'quiz', question: "Сколько лет разлагается пластик?", options: ["10 лет", "100 лет", "Более 100 лет", "1", "2"], correctAnswer: "Более 100 лет", hint: "Пластик разлагается очень долго" },
      { type: 'quiz', question: "Что относится к живой природе?", options: ["Камень 🪨", "Дерево 🌳", "Вода 💧", "Солнце ☀️", "Гора ⛰️"], correctAnswer: "Дерево 🌳", hint: "Дерево - живое" },
    ],
    reward: { stars: 3, message: "Молодец! Ты бережёшь природу! 🌿" }
  },
  {
    title: "Future Simple",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I ___ visit London next summer.", options: ["will", "am", "did", "Не знаю", "Другой вариант"], correctAnswer: "will", hint: "Future Simple: will + глагол" },
      { type: 'quiz', question: "She ... come tomorrow. (will)", options: ["прилагательное", "наречие", "глагол", "существительное", "will"], correctAnswer: "will", hint: "Will для всех лиц" },
      { type: 'quiz', question: "Tomorrow I ___ to school.", options: ["go", "will go", "went", "Не знаю", "Другой вариант"], correctAnswer: "will go", hint: "Tomorrow = будущее время" },
      { type: 'quiz', question: "Укажи маркеры Future Simple:", options: ["Tomorrow", "Yesterday", "Last year", "Не знаю", "Другой вариант"], correctAnswer: "Tomorrow", hint: "Маркеры будущего времени" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Great! Ты знаешь будущее время! ⏭️" }
  },
  {
    title: "Профессии",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-indigo-400",
    tasks: [
      { type: 'quiz', question: "Кто лечит животных?", options: ["Врач", "Ветеринар", "Учитель", "Пушкин", "Лермонтов"], correctAnswer: "Ветеринар", hint: "Ветеринар - врач для животных" },
      { type: 'quiz', question: "Укажи профессии:", options: ["Врач", "Стол", "Книга", "Не знаю", "Другой вариант"], correctAnswer: "Врач", hint: "Профессии - это работа" },
      { type: 'quiz', question: "Кто строит дома?", options: ["Врач", "Строитель", "Повар", "Пушкин", "Лермонтов"], correctAnswer: "Строитель", hint: "Строитель создаёт здания" },
      { type: 'quiz', question: "Кто преподаёт в школе?", options: ["Врач", "Строитель", "Учитель", "Пушкин", "Лермонтов"], correctAnswer: "Учитель", hint: "Учитель обучает детей" },
      { type: 'quiz', question: "Что относится к живой природе?", options: ["Камень 🪨", "Дерево 🌳", "Вода 💧", "Солнце ☀️", "Гора ⛰️"], correctAnswer: "Дерево 🌳", hint: "Дерево - живое" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь профессии! 👨‍⚕️" }
  },
  {
    title: "Площадь и периметр",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Формула периметра квадрата:", options: ["P = 4a", "P = a²", "P = 2a", "Не знаю", "Другой вариант"], correctAnswer: "P = 4a", hint: "У квадрата 4 равные стороны" },
      { type: 'quiz', question: "Периметр квадрата со стороной 5 см = ... см", options: ["18", "21", "19", "20", "22"], correctAnswer: "20", hint: "P = 4 × 5 = 20" },
      { type: 'quiz', question: "Формула площади прямоугольника:", options: ["S = a + b", "S = a × b", "S = 2(a + b)", "Не знаю", "Другой вариант"], correctAnswer: "S = a × b", hint: "Площадь = длина × ширина" },
      { type: 'quiz', question: "Площадь прямоугольника 6 × 4 = ... см²", options: ["22", "14", "19", "24", "26"], correctAnswer: "24", hint: "S = 6 × 4 = 24" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь площадь и периметр! 📐" }
  },
  {
    title: "Уравнения",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "x + 15 = 30, x = ...", options: ["17", "16", "14", "13", "15"], correctAnswer: "15", hint: "x = 30 - 15" },
      { type: 'quiz', question: "x - 8 = 12, x = ...", options: ["20", "18", "22", "19", "21"], correctAnswer: "20", hint: "x = 12 + 8" },
      { type: 'quiz', question: "x × 4 = 24, x = ...", options: ["4", "7", "8", "6", "5"], correctAnswer: "6", hint: "x = 24 ÷ 4" },
      { type: 'quiz', question: "x ÷ 3 = 9, x = ...", options: ["17", "27", "25", "22", "29"], correctAnswer: "27", hint: "x = 9 × 3" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Супер! Ты решаешь уравнения! ✖️" }
  },
  {
    title: "Склонения существительных",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "К какому склонению относятся слова на -а, -я (мама, дядя)?", options: ["1 склонение", "2 склонение", "3 склонение", "Не знаю", "Другой вариант"], correctAnswer: "1 склонение", hint: "1 склонение - ж.р. и м.р. на -а, -я" },
      { type: 'quiz', question: "К какому склонению относится слово \"стол\"?", options: ["1 склонение", "2 склонение", "3 склонение", "Не знаю", "Другой вариант"], correctAnswer: "2 склонение", hint: "2 склонение - м.р. без окончания, ср.р. на -о, -е" },
      { type: 'quiz', question: "Укажи слова 3 склонения:", options: ["Мышь", "Стол", "Мама", "Не знаю", "Другой вариант"], correctAnswer: "Мышь", hint: "3 склонение - ж.р. на -ь" },
      { type: 'quiz', question: "Слово \"окно\" - ... склонение (число)", options: ["1", "3", "0", "4", "2"], correctAnswer: "2", hint: "Окно - ср.р. на -о, 2 склонение" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь склонения! 📚" }
  },
  {
    title: "Части речи",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Существительное обозначает:", options: ["Действие", "Предмет", "Признак", "Не знаю", "Другой вариант"], correctAnswer: "Предмет", hint: "Существительное - это предмет" },
      { type: 'quiz', question: "Укажи существительные:", options: ["Дом", "Бежать", "Красивый", "Писать", "Не знаю"], correctAnswer: "Дом", hint: "Существительные - это предметы" },
      { type: 'quiz', question: "Наречие отвечает на вопрос:", options: ["Кто? Что?", "Какой?", "Как? Где? Когда?", "Не знаю", "Другой вариант"], correctAnswer: "Как? Где? Когда?", hint: "Наречие - обстоятельство" },
      { type: 'quiz', question: "\"Быстро\" - это ... (часть речи)", options: ["глагол", "прилагательное", "числительное", "существительное", "наречие"], correctAnswer: "наречие", hint: "Как? Быстро - это наречие" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь части речи! ✍️" }
  },
  {
    title: "Басни Крылова",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Кто автор басни \"Ворона и Лисица\"?", options: ["Пушкин", "Крылов", "Лермонтов", "Гоголь", "Толстой"], correctAnswer: "Крылов", hint: "Иван Андреевич Крылов" },
      { type: 'quiz', question: "Укажи басни Крылова:", options: ["Стрекоза и Муравей", "Репка", "Колобок", "Не знаю", "Другой вариант"], correctAnswer: "Стрекоза и Муравей", hint: "Крылов - великий баснописец" },
      { type: 'quiz', question: "Что такое мораль басни?", options: ["Вступление", "Нравоучительный вывод", "Описание", "Не знаю", "Другой вариант"], correctAnswer: "Нравоучительный вывод", hint: "Мораль учит чему-то важному" },
      { type: 'quiz', question: "\"Ты всё пела? Это дело: Так поди же, ...!\" (попляши)", options: ["наречие", "попляши", "прилагательное", "глагол", "существительное"], correctAnswer: "попляши", hint: "Из басни \"Стрекоза и Муравей\"" },
      { type: 'quiz', question: "Что такое сказка?", options: ["Научная статья", "Стихотворение", "Выдуманная история", "Учебник", "Энциклопедия"], correctAnswer: "Выдуманная история", hint: "Сказка - вымышленный рассказ" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь басни! 📖" }
  },
  {
    title: "Планеты Солнечной системы",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-purple-400",
    tasks: [
      { type: 'quiz', question: "Какая планета ближе всех к Солнцу?", options: ["Венера", "Меркурий", "Земля", "Первый", "Второй"], correctAnswer: "Меркурий", hint: "Меркурий - самая близкая к Солнцу" },
      { type: 'quiz', question: "Сколько планет в Солнечной системе?", options: ["7", "8", "9", "1", "2"], correctAnswer: "8", hint: "Меркурий, Венера, Земля, Марс, Юпитер, Сатурн, Уран, Нептун" },
      { type: 'quiz', question: "Укажи планеты:", options: ["Земля", "Луна", "Солнце", "Не знаю", "Другой вариант"], correctAnswer: "Земля", hint: "Луна - спутник, Солнце - звезда" },
      { type: 'quiz', question: "Какая планета самая большая?", options: ["Земля", "Юпитер", "Сатурн", "Первый", "Второй"], correctAnswer: "Юпитер", hint: "Юпитер - крупнейшая планета" },
      { type: 'quiz', question: "Что относится к живой природе?", options: ["Камень 🪨", "Дерево 🌳", "Вода 💧", "Солнце ☀️", "Гора ⛰️"], correctAnswer: "Дерево 🌳", hint: "Дерево - живое" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь космос! 🚀" }
  },
  {
    title: "Can / Could",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I ___ swim. (умею)", options: ["can", "could", "am", "Не знаю", "Другой вариант"], correctAnswer: "can", hint: "Can = могу/умею (настоящее)" },
      { type: 'quiz', question: "___ you help me? (можешь)", options: ["Can", "Are", "Is", "Не знаю", "Другой вариант"], correctAnswer: "Can", hint: "Can используется для просьбы" },
      { type: 'quiz', question: "She ... speak English. (can)", options: ["глагол", "прилагательное", "can", "наречие", "существительное"], correctAnswer: "can", hint: "Can для всех лиц" },
      { type: 'quiz', question: "Укажи предложения с can/could:", options: ["I can swim", "I am swim", "She can dances", "Не знаю", "Другой вариант"], correctAnswer: "I can swim", hint: "Can/Could + глагол без to" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Great! Ты знаешь модальные глаголы! 🇬🇧" }
  },
  {
    title: "Геометрические фигуры",
    subject: "Математика",
    icon: "Calculator",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Сколько углов у треугольника?", options: ["2", "3", "4", "1", "5"], correctAnswer: "3", hint: "Тре-угольник = три угла" },
      { type: 'quiz', question: "У прямоугольника:", options: ["Все стороны равны", "Противоположные стороны равны", "Нет углов", "Не знаю", "Другой вариант"], correctAnswer: "Противоположные стороны равны", hint: "У прямоугольника 4 прямых угла" },
      { type: 'quiz', question: "Укажи фигуры с 4 углами:", options: ["Квадрат", "Треугольник", "Круг", "Не знаю", "Другой вариант"], correctAnswer: "Квадрат", hint: "Четырёхугольники" },
      { type: 'quiz', question: "У квадрата ... угла", options: ["3", "2", "4", "6", "5"], correctAnswer: "4", hint: "У квадрата 4 прямых угла" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь геометрические фигуры! 🔷" }
  }
]
