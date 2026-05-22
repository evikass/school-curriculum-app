// Экспорт игр для 1 класса
import { GameLesson } from '../types'

export const firstGradeGames: GameLesson[] = [
  {
    title: "Алфавит: первые буквы",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Какая буква первая в алфавите?", options: ["А", "Б", "В", "Первый", "Второй"], correctAnswer: "А", hint: "Алфавит начинается с А" },
      { type: 'quiz', question: "Какая буква следует за А?", options: ["В", "Б", "Г", "Первый", "Второй"], correctAnswer: "Б", hint: "А, Б, ..." },
      { type: 'quiz', question: "Укажи гласные буквы:", options: ["А", "Б", "М", "Не знаю", "Другой вариант"], correctAnswer: "А", hint: "Гласные - их можно петь" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "33", "35", "1", "2"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь алфавит! 🔤" }
  },
  {
    title: "Буква А",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Какой звук обозначает буква А?", options: ["Гласный 🔴", "Согласный 🔵", "Первый", "Второй", "Третий"], correctAnswer: "Гласный 🔴", hint: "Этот звук поётся свободно!" },
      { type: 'quiz', question: "Укажи слова с буквой А:", options: ["МАМА 👩", "СЫН 👦", "ДОМ 🏠", "Не знаю", "Другой вариант"], correctAnswer: "МАМА 👩", hint: "Ищи букву А в словах" },
      { type: 'quiz', question: "С какой буквы начинается слово АРБУЗ?", options: ["О", "А", "У", "Первый", "Второй"], correctAnswer: "А", hint: "Произнеси слово: [А]рбуз" },
      { type: 'quiz', question: "Сколько звуков [а] в слове БАНАН?", options: ["1", "2", "3", "4", "5"], correctAnswer: "2", hint: "БА-НАН - послушай внимательно!" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь букву А! 🌟" }
  },
  {
    title: "ЖИ-ШИ пиши с И",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Как правильно: МАШ__НА?", options: ["МАШЫНА", "МАШИНА", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "МАШИНА", hint: "ЖИ-ШИ пиши с И!" },
      { type: 'quiz', question: "Как правильно написать?", options: ["ШЫНА 🛞", "ШИНА 🛞", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "ШИНА 🛞", hint: "ШИ всегда пишется с буквой И" },
      { type: 'quiz', question: "Укажи слова с ЖИ и ШИ:", options: ["ЖИРАФ 🦒", "МАМА 👩", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "ЖИРАФ 🦒", hint: "Ищи сочетания ЖИ и ШИ" },
      { type: 'quiz', question: "Вставь букву: ЛЫЖ...", options: ["наречие", "существительное", "глагол", "прилагательное", "И"], correctAnswer: "И", hint: "ЖИ - пиши с И!" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь правило! 🏆" }
  },
  {
    title: "Ча-ща пиши с А",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Как правильно: ТУЧ__?", options: ["ТУЧА ☁️", "ТУЧЯ ☁️", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "ТУЧА ☁️", hint: "ЧА-ЩА пиши с А!" },
      { type: 'quiz', question: "Укажи слова с ЧА и ЩА:", options: ["ЧАЩА 🌲", "МАМА 👩", "ЩУКА 🐟", "Не знаю", "Другой вариант"], correctAnswer: "ЧАЩА 🌲", hint: "Ищи ЧА и ЩА" },
      { type: 'quiz', question: "В слове РОЩА какая орфограмма?", options: ["ЖИ-ШИ", "ЧА-ЩА", "Первый", "Второй", "Третий"], correctAnswer: "ЧА-ЩА", hint: "РОЩА - это ЩА" },
      { type: 'quiz', question: "Вставь букву: ЗАДАЧ...", options: ["прилагательное", "существительное", "глагол", "А", "наречие"], correctAnswer: "А", hint: "ЧА - пиши с А!" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Замечательно! Ты знаешь правило ЧА-ЩА! 📝" }
  },
  {
    title: "Большая буква",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "С какой буквы начинаются имена?", options: ["С маленькой", "С большой", "Первый", "Второй", "Третий"], correctAnswer: "С большой", hint: "Имена пишутся с большой буквы!" },
      { type: 'quiz', question: "Укажи правильно написанные имена:", options: ["Маша", "маша", "ПЕТЯ", "аня", "Не знаю"], correctAnswer: "Маша", hint: "Имена начинаются с большой буквы" },
      { type: 'quiz', question: "Как написать название города?", options: ["москва", "Москва", "МОСКВА", "Не знаю", "Другой вариант"], correctAnswer: "Москва", hint: "Названия городов - с большой буквы" },
      { type: 'quiz', question: "Что пишется с большой буквы?", options: ["Стол", "Москва", "Бежит", "Не знаю", "Другой вариант"], correctAnswer: "Москва", hint: "Название города!" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Умница! Ты знаешь про большую букву! 📖" }
  },
  {
    title: "Числа 1-5",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Сколько звёзд? ⭐⭐⭐", options: ["2", "3", "4", "1", "5"], correctAnswer: "3", hint: "Посчитай: раз, два, три!" },
      { type: 'quiz', question: "Сколько яблок? 🍎🍎🍎🍎🍎", options: ["4", "5", "6", "1", "2"], correctAnswer: "5", hint: "Посчитай все яблоки!" },
      { type: 'quiz', question: "Расставь по порядку: 3, 1, 5, 2", options: ["1, 2, 3, 5", "2, 5, 1, 3", "1, 3, 5, 2", "1, 5, 2, 3", "2, 3, 1, 5"], correctAnswer: "1, 2, 3, 5", hint: "От меньшего к большему" },
      { type: 'quiz', question: "Какое число больше: 2 или 4?", options: ["2", "4", "Одинаково", "1", "3"], correctAnswer: "4", hint: "4 идёт позже при счёте" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Умница! Ты знаешь числа! 🔢" }
  },
  {
    title: "Сложение до 10",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "2 + 3 = ?", options: ["4", "5", "6", "Не знаю", "Другой вариант"], correctAnswer: "5", hint: "Два плюс три..." },
      { type: 'quiz', question: "4 + 2 = ?", options: ["5", "6", "7", "Не знаю", "Другой вариант"], correctAnswer: "6", hint: "Четыре и два вместе" },
      { type: 'quiz', question: "3 + ... = 7", options: ["3", "2", "6", "4", "5"], correctAnswer: "4", hint: "Сколько добавить до семи?" },
      { type: 'quiz', question: "5 + 5 = ?", options: ["9", "10", "11", "Не знаю", "Другой вариант"], correctAnswer: "10", hint: "Это все пальцы на руках!" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Супер! Ты умеешь складывать! ➕" }
  },
  {
    title: "Вычитание",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "5 - 2 = ?", options: ["2", "3", "4", "Не знаю", "Другой вариант"], correctAnswer: "3", hint: "Пять минус два..." },
      { type: 'quiz', question: "7 - 3 = ?", options: ["3", "4", "5", "Не знаю", "Другой вариант"], correctAnswer: "4", hint: "Семь убери три" },
      { type: 'quiz', question: "10 - ... = 6", options: ["2", "6", "5", "3", "4"], correctAnswer: "4", hint: "Что отнять от 10, чтобы получить 6?" },
      { type: 'quiz', question: "8 - 0 = ?", options: ["0", "8", "7", "Не знаю", "Другой вариант"], correctAnswer: "8", hint: "Если ничего не отнять..." },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты умеешь вычитать! ➖" }
  },
  {
    title: "Геометрические фигуры",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Сколько углов у треугольника?", options: ["2", "3", "4", "1", "5"], correctAnswer: "3", hint: "Треугольник = три угла" },
      { type: 'quiz', question: "Какая фигура круглой формы?", options: ["Квадрат ⬜", "Круг ⭕", "Треугольник 🔺", "Первый", "Второй"], correctAnswer: "Круг ⭕", hint: "Круглая как мяч!" },
      { type: 'quiz', question: "Укажи фигуры с 4 углами:", options: ["Квадрат ⬜", "Треугольник 🔺", "Круг ⭕", "Не знаю", "Другой вариант"], correctAnswer: "Квадрат ⬜", hint: "4 угла = четырёхугольник" },
      { type: 'quiz', question: "Что похоже на квадрат?", options: ["Мяч ⚽", "Окно 🪟", "Колесо 🛞", "Не знаю", "Другой вариант"], correctAnswer: "Окно 🪟", hint: "У окна 4 равные стороны" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Здорово! Ты знаешь фигуры! 🔷" }
  },
  {
    title: "Сказки",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Кто съел Колобка?", options: ["Волк 🐺", "Лиса 🦊", "Медведь 🐻", "Пушкин", "Лермонтов"], correctAnswer: "Лиса 🦊", hint: "Хитрая рыжая плутовка" },
      { type: 'quiz', question: "Из чего сделан Буратино?", options: ["Из железа", "Из дерева", "Из пластилина", "Не знаю", "Другой вариант"], correctAnswer: "Из дерева", hint: "Папа Карло вырезал его" },
      { type: 'quiz', question: "Кто помогал Красной Шапочке?", options: ["Охотники 🔫", "Волк 🐺", "Бабушка 👵", "Пушкин", "Лермонтов"], correctAnswer: "Охотники 🔫", hint: "Они спасли бабушку" },
      { type: 'quiz', question: "Кто тянул репку первым?", options: ["Бабка", "Дедка", "Внучка", "Пушкин", "Лермонтов"], correctAnswer: "Дедка", hint: "Посадил дед репку..." },
      { type: 'quiz', question: "Что такое сказка?", options: ["Научная статья", "Стихотворение", "Выдуманная история", "Учебник", "Энциклопедия"], correctAnswer: "Выдуманная история", hint: "Сказка - вымышленный рассказ" },
    ],
    reward: { stars: 3, message: "Прекрасно! Ты знаешь сказки! 📚" }
  },
  {
    title: "Времена года",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какое время года после зимы?", options: ["Лето ☀️", "Весна 🌸", "Осень 🍂", "Первый", "Второй"], correctAnswer: "Весна 🌸", hint: "Когда тает снег?" },
      { type: 'quiz', question: "Что бывает осенью?", options: ["Листопад 🍂", "Снег ❄️", "Цветы 🌷", "Не знаю", "Другой вариант"], correctAnswer: "Листопад 🍂", hint: "Осенью прохладно" },
      { type: 'quiz', question: "Когда можно купаться в речке?", options: ["Зимой ❄️", "Летом ☀️", "Осенью 🍂", "Не знаю", "Другой вариант"], correctAnswer: "Летом ☀️", hint: "Когда тепло и солнечно" },
      { type: 'quiz', question: "Сколько времён года?", options: ["3", "4", "5", "1", "2"], correctAnswer: "4", hint: "Зима, весна, лето, осень" },
      { type: 'quiz', question: "Что относится к живой природе?", options: ["Камень 🪨", "Дерево 🌳", "Вода 💧", "Солнце ☀️", "Гора ⛰️"], correctAnswer: "Дерево 🌳", hint: "Дерево - живое" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь времена года! 🌸" }
  },
  {
    title: "Животные",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какое животное говорит \"Му\"?", options: ["Кошка 🐱", "Корова 🐄", "Собака 🐕", "Первый", "Второй"], correctAnswer: "Корова 🐄", hint: "Большое животное на ферме" },
      { type: 'quiz', question: "Укажи домашних животных:", options: ["Кошка 🐱", "Лиса 🦊", "Волк 🐺", "Не знаю", "Другой вариант"], correctAnswer: "Кошка 🐱", hint: "Они живут с людьми" },
      { type: 'quiz', question: "Кто умеет летать?", options: ["Рыба 🐟", "Птица 🐦", "Змея 🐍", "Пушкин", "Лермонтов"], correctAnswer: "Птица 🐦", hint: "У кого есть крылья?" },
      { type: 'quiz', question: "Где живёт белка?", options: ["В норе 🕳️", "В дупле 🌳", "В воде 🌊", "Не знаю", "Другой вариант"], correctAnswer: "В дупле 🌳", hint: "Белка живёт на дереве" },
      { type: 'quiz', question: "Что относится к живой природе?", options: ["Камень 🪨", "Дерево 🌳", "Вода 💧", "Солнце ☀️", "Гора ⛰️"], correctAnswer: "Дерево 🌳", hint: "Дерево - живое" },
    ],
    reward: { stars: 3, message: "Молодец! Ты знаешь животных! 🐾" }
  },
  {
    title: "Hello! Привет!",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Как сказать \"Привет\" по-английски?", options: ["Goodbye 👋", "Hello 👋", "Thanks 🙏", "Не знаю", "Другой вариант"], correctAnswer: "Hello 👋", hint: "Самое популярное приветствие" },
      { type: 'quiz', question: "Что значит Hi?", options: ["Пока", "Привет", "Спасибо", "Не знаю", "Другой вариант"], correctAnswer: "Привет", hint: "Hi = Привет" },
      { type: 'quiz', question: "Укажи приветствия:", options: ["Hello", "Goodbye", "Bye", "Thanks", "Не знаю"], correctAnswer: "Hello", hint: "Приветствия по-английски" },
      { type: 'quiz', question: "Как сказать \"Пока\"?", options: ["Hello", "Bye", "Hi", "Не знаю", "Другой вариант"], correctAnswer: "Bye", hint: "Bye = Пока" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Great! Отлично! 👋" }
  },
  {
    title: "Цвета по-английски",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Red - это...", options: ["Синий", "Красный", "Зелёный", "Не знаю", "Другой вариант"], correctAnswer: "Красный", hint: "Red = красный цвет" },
      { type: 'quiz', question: "Как будет \"жёлтый\"?", options: ["Yellow", "Green", "Blue", "Не знаю", "Другой вариант"], correctAnswer: "Yellow", hint: "Yellow = цвет солнца" },
      { type: 'quiz', question: "Укажи цвета радуги:", options: ["Red", "Cat", "Dog", "Не знаю", "Другой вариант"], correctAnswer: "Red", hint: "Цвета = Colors" },
      { type: 'quiz', question: "Какого цвета трава?", options: ["Red", "Blue", "Green", "Не знаю", "Другой вариант"], correctAnswer: "Green", hint: "Green = зелёный" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Wonderful! Замечательно! 🎨" }
  },
  {
    title: "Счёт до 20",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Какое число идёт после 15?", options: ["14", "16", "17", "1", "2"], correctAnswer: "16", hint: "Посчитай: 14, 15, ..." },
      { type: 'quiz', question: "Какое число между 12 и 14?", options: ["12", "14", "11", "13", "15"], correctAnswer: "13", hint: "12, ?, 14" },
      { type: 'quiz', question: "Сколько десятков в числе 17?", options: ["1", "7", "17", "2", "3"], correctAnswer: "1", hint: "17 = 1 десяток и 7 единиц" },
      { type: 'quiz', question: "Какое число больше: 19 или 15?", options: ["19", "15", "Одинаково", "1", "2"], correctAnswer: "19", hint: "19 идёт позже при счёте" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Умница! Ты считаешь до 20! 🔢" }
  },
  {
    title: "Состав числа",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "5 - это 2 + ...", options: ["2", "4", "1", "3", "5"], correctAnswer: "3", hint: "2 + 3 = 5" },
      { type: 'quiz', question: "7 - это 4 + ...", options: ["4", "1", "2", "3", "5"], correctAnswer: "3", hint: "4 + 3 = 7" },
      { type: 'quiz', question: "Из каких чисел состоит 6?", options: ["3 и 3", "2 и 2", "5 и 2", "1", "2"], correctAnswer: "3 и 3", hint: "3 + 3 = 6" },
      { type: 'quiz', question: "10 - это 6 + ...", options: ["5", "3", "2", "4", "6"], correctAnswer: "4", hint: "6 + 4 = 10" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь состав чисел! 🧮" }
  },
  {
    title: "Чу-щу пиши с У",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Как правильно: Щ__КА?", options: ["ЩУКА 🐟", "ЩАКА", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "ЩУКА 🐟", hint: "ЧУ-ЩУ пиши с У!" },
      { type: 'quiz', question: "Укажи слова с ЧУ и ЩУ:", options: ["ЧУДО ✨", "МАМА 👩", "РОЩА 🌳", "Не знаю", "Другой вариант"], correctAnswer: "ЧУДО ✨", hint: "ЧУ-ЩУ с буквой У" },
      { type: 'quiz', question: "Вставь букву: Ч...ДО", options: ["наречие", "прилагательное", "глагол", "У", "существительное"], correctAnswer: "У", hint: "ЧУ - пиши с У!" },
      { type: 'quiz', question: "В слове ЧУМАКА какая орфограмма?", options: ["ЖИ-ШИ", "ЧУ-ЩУ", "Первый", "Второй", "Третий"], correctAnswer: "ЧУ-ЩУ", hint: "ЧУ - пишется с У" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь правило ЧУ-ЩУ! ✍️" }
  },
  {
    title: "Слова-действия",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Что делает птица? 🐦", options: ["Летит", "Плавает", "Бегает", "Не знаю", "Другой вариант"], correctAnswer: "Летит", hint: "Птицы летают!" },
      { type: 'quiz', question: "Укажи слова-действия:", options: ["Бежит 🏃", "Красивый", "Стол", "Не знаю", "Другой вариант"], correctAnswer: "Бежит 🏃", hint: "Слова-действия отвечают на \"что делает?\"" },
      { type: 'quiz', question: "На какой вопрос отвечает слово \"рисует\"?", options: ["Что?", "Что делает?", "Какой?", "Первый", "Второй"], correctAnswer: "Что делает?", hint: "Рисует - это действие" },
      { type: 'quiz', question: "Что делает рыба? 🐟", options: ["Летит", "Плавает", "Бегает", "Не знаю", "Другой вариант"], correctAnswer: "Плавает", hint: "Рыбы плавают в воде" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь слова-действия! 📝" }
  },
  {
    title: "Дни недели и месяцы",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какой день идёт после среды?", options: ["Вторник", "Четверг", "Пятница", "Первый", "Второй"], correctAnswer: "Четверг", hint: "Понедельник, вторник, среда, ..." },
      { type: 'quiz', question: "Укажи зимние месяцы:", options: ["Декабрь", "Июнь", "Июль", "Не знаю", "Другой вариант"], correctAnswer: "Декабрь", hint: "Зимние месяцы - холодные" },
      { type: 'quiz', question: "Сколько месяцев в году?", options: ["10", "11", "12", "1", "2"], correctAnswer: "12", hint: "В году 12 месяцев" },
      { type: 'quiz', question: "В каком месяце начинается учебный год?", options: ["Август", "Сентябрь", "Октябрь", "Не знаю", "Другой вариант"], correctAnswer: "Сентябрь", hint: "1 сентября - День знаний" },
      { type: 'quiz', question: "Что относится к живой природе?", options: ["Камень 🪨", "Дерево 🌳", "Вода 💧", "Солнце ☀️", "Гора ⛰️"], correctAnswer: "Дерево 🌳", hint: "Дерево - живое" },
    ],
    reward: { stars: 3, message: "Умница! Ты знаешь календарь! 📅" }
  },
  {
    title: "Животные и их детёныши",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Кто детёныш у кошки?", options: ["Щенок", "Котёнок", "Медвежонок", "Пушкин", "Лермонтов"], correctAnswer: "Котёнок", hint: "Кошка - котёнок" },
      { type: 'quiz', question: "Укажи правильные пары:", options: ["Собака - щенок", "Кошка - щенок", "Не знаю", "Другой вариант", "Ни один из этих"], correctAnswer: "Собака - щенок", hint: "У каждого животного свой детёныш" },
      { type: 'quiz', question: "Кто детёныш у курицы?", options: ["Утёнок", "Цыплёнок", "Гусёнок", "Пушкин", "Лермонтов"], correctAnswer: "Цыплёнок", hint: "Курица - цыплёнок" },
      { type: 'quiz', question: "Кто детёныш у медведя?", options: ["Медвежонок", "Зайчонок", "Лисёнок", "Пушкин", "Лермонтов"], correctAnswer: "Медвежонок", hint: "Медведь - медвежонок" },
      { type: 'quiz', question: "Что относится к живой природе?", options: ["Камень 🪨", "Дерево 🌳", "Вода 💧", "Солнце ☀️", "Гора ⛰️"], correctAnswer: "Дерево 🌳", hint: "Дерево - живое" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь детёнышей! 🐾" }
  },
  {
    title: "Числа на английском",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "One - это...", options: ["Один", "Два", "Три", "Не знаю", "Другой вариант"], correctAnswer: "Один", hint: "One = 1" },
      { type: 'quiz', question: "Как будет \"три\"?", options: ["Two", "Three", "Four", "Не знаю", "Другой вариант"], correctAnswer: "Three", hint: "Three = 3" },
      { type: 'quiz', question: "Two + Two = ... (Four)", options: ["существительное", "прилагательное", "наречие", "глагол", "Four"], correctAnswer: "Four", hint: "2 + 2 = 4" },
      { type: 'quiz', question: "Укажи числа от 1 до 3:", options: ["One", "Four", "Five", "Не знаю", "Другой вариант"], correctAnswer: "One", hint: "1, 2, 3" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Great! Ты знаешь числа! 🔢" }
  },
  {
    title: "Сравнение чисел",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Что больше: 7 или 5?", options: ["7", "5", "Одинаково", "Не знаю", "Другой вариант"], correctAnswer: "7", hint: "7 идёт позже при счёте" },
      { type: 'quiz', question: "Что меньше: 3 или 6?", options: ["3", "6", "Одинаково", "Не знаю", "Другой вариант"], correctAnswer: "3", hint: "3 идёт раньше при счёте" },
      { type: 'quiz', question: "Поставь знак: 4 ... 4 (равно)", options: ["=", "прилагательное", "существительное", "глагол", "наречие"], correctAnswer: "=", hint: "Числа одинаковые" },
      { type: 'quiz', question: "Сколько яблок больше? 🍎🍎🍎 vs 🍎🍎", options: ["Первых больше на 1", "Вторых больше", "Одинаково", "1", "2"], correctAnswer: "Первых больше на 1", hint: "3 > 2" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Отлично! Ты умеешь сравнивать! ⚖️" }
  },
  {
    title: "Задачи в картинках",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Было 3 яблока 🍎🍎🍎, съели 1. Сколько осталось?", options: ["1", "2", "4", "3", "5"], correctAnswer: "2", hint: "3 - 1 = 2" },
      { type: 'quiz', question: "Было 2 птички 🐦🐦, прилетели ещё 2. Сколько стало?", options: ["2", "4", "3", "1", "5"], correctAnswer: "4", hint: "2 + 2 = 4" },
      { type: 'quiz', question: "5 конфет 🍬🍬🍬🍬🍬, 2 съели. Осталось ...", options: ["2", "1", "3", "5", "4"], correctAnswer: "3", hint: "5 - 2 = 3" },
      { type: 'quiz', question: "У Маши 2 куклы 🎎🎎, у Даши 3. Сколько всего?", options: ["4", "5", "6", "1", "2"], correctAnswer: "5", hint: "2 + 3 = 5" },
      { type: 'quiz', question: "Чему равно 0 + 0?", options: ["1", "0", "2", "10", "-1"], correctAnswer: "0", hint: "Ноль плюс ноль равно ноль" },
    ],
    reward: { stars: 3, message: "Умница! Ты решаешь задачи! 📊" }
  },
  {
    title: "Слоги",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Сколько слогов в слове МА-МА?", options: ["1", "2", "3", "4", "5"], correctAnswer: "2", hint: "Хлопни два раза: МА-МА" },
      { type: 'quiz', question: "Сколько слогов в слове ШАР?", options: ["1", "2", "3", "4", "5"], correctAnswer: "1", hint: "Хлопни один раз" },
      { type: 'quiz', question: "Укажи слова из 2 слогов:", options: ["Вода 💧", "Дом 🏠", "Кот 🐱", "Сад 🌳", "Не знаю"], correctAnswer: "Вода 💧", hint: "Посчитай хлопки" },
      { type: 'quiz', question: "Какое слово самое длинное?", options: ["Кот", "Машина", "Дом", "Первый", "Второй"], correctAnswer: "Машина", hint: "Посчитай слоги" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь слоги! 📝" }
  },
  {
    title: "Слова-признаки",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Какой мяч? ⚽", options: ["Круглый", "Бежит", "Мяч", "Первый", "Второй"], correctAnswer: "Круглый", hint: "Признак предмета" },
      { type: 'quiz', question: "Укажи слова-признаки:", options: ["Большой", "Стол", "Дом", "Не знаю", "Другой вариант"], correctAnswer: "Большой", hint: "Слова-признаки описывают предметы" },
      { type: 'quiz', question: "На какой вопрос отвечает слово \"красивый\"?", options: ["Что?", "Какой?", "Что делает?", "Первый", "Второй"], correctAnswer: "Какой?", hint: "Какой? - это признак" },
      { type: 'quiz', question: "Какое небо? ☁️", options: ["Синее", "Бежит", "Небо", "Первый", "Второй"], correctAnswer: "Синее", hint: "Признак неба" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "31", "33", "35", "29"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь слова-признаки! ✍️" }
  },
  {
    title: "Семья",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Мама и папа - это...", options: ["Дети", "Родители", "Бабушка", "Не знаю", "Другой вариант"], correctAnswer: "Родители", hint: "Родители - это мама и папа" },
      { type: 'quiz', question: "Укажи членов семьи:", options: ["Мама 👩", "Учитель", "Друг", "Не знаю", "Другой вариант"], correctAnswer: "Мама 👩", hint: "Семья - самые близкие люди" },
      { type: 'quiz', question: "Брат мамы - это...", options: ["Дядя", "Дедушка", "Папа", "Не знаю", "Другой вариант"], correctAnswer: "Дядя", hint: "Брат мамы или папы" },
      { type: 'quiz', question: "Дочь мамы - это...", options: ["Тётя", "Сестра", "Бабушка", "Не знаю", "Другой вариант"], correctAnswer: "Сестра", hint: "Дочь моих родителей" },
      { type: 'quiz', question: "Что относится к живой природе?", options: ["Камень 🪨", "Дерево 🌳", "Вода 💧", "Солнце ☀️", "Гора ⛰️"], correctAnswer: "Дерево 🌳", hint: "Дерево - живое" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь семью! 👨‍👩‍👧‍👦" }
  },
  {
    title: "Транспорт",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-indigo-400",
    tasks: [
      { type: 'quiz', question: "Что летает в небе?", options: ["Машина 🚗", "Самолёт ✈️", "Корабль 🚢", "Не знаю", "Другой вариант"], correctAnswer: "Самолёт ✈️", hint: "У самолёта есть крылья" },
      { type: 'quiz', question: "Укажи транспорт:", options: ["Машина 🚗", "Стол 🪑", "Дерево 🌳", "Не знаю", "Другой вариант"], correctAnswer: "Машина 🚗", hint: "Транспорт - это то, на чём ездят" },
      { type: 'quiz', question: "Корабль плавает...", options: ["В небе", "На дороге", "По воде 🌊", "Не знаю", "Другой вариант"], correctAnswer: "По воде 🌊", hint: "Корабли плавают по морям и рекам" },
      { type: 'quiz', question: "Сколько колёс у велосипеда?", options: ["2", "3", "4", "1", "5"], correctAnswer: "2", hint: "Велосипед = два колеса" },
      { type: 'quiz', question: "Что относится к живой природе?", options: ["Камень 🪨", "Дерево 🌳", "Вода 💧", "Солнце ☀️", "Гора ⛰️"], correctAnswer: "Дерево 🌳", hint: "Дерево - живое" },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь транспорт! 🚗" }
  },
  {
    title: "Семья по-английски",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Mother - это...", options: ["Папа", "Мама", "Сестра", "Не знаю", "Другой вариант"], correctAnswer: "Мама", hint: "Mother = мама" },
      { type: 'quiz', question: "Как будет \"папа\"?", options: ["Mother", "Father", "Sister", "Не знаю", "Другой вариант"], correctAnswer: "Father", hint: "Father = папа" },
      { type: 'quiz', question: "Укажи слова о семье:", options: ["Mother 👩", "Cat 🐱", "Dog 🐕", "Не знаю", "Другой вариант"], correctAnswer: "Mother 👩", hint: "Family = семья" },
      { type: 'quiz', question: "Brother = ... (брат)", options: ["наречие", "брат", "глагол", "существительное", "прилагательное"], correctAnswer: "брат", hint: "Brother - это брат" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Great! Ты знаешь семью! 👨‍👩‍👧‍👦" }
  },
  {
    title: "Животные по-английски",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Cat - это...", options: ["Собака", "Кошка", "Птица", "Не знаю", "Другой вариант"], correctAnswer: "Кошка", hint: "Cat = кошка 🐱" },
      { type: 'quiz', question: "Как будет \"собака\"?", options: ["Cat", "Dog", "Bird", "Не знаю", "Другой вариант"], correctAnswer: "Dog", hint: "Dog = собака 🐕" },
      { type: 'quiz', question: "Fish = ... (рыба)", options: ["существительное", "рыба", "прилагательное", "наречие", "глагол"], correctAnswer: "рыба", hint: "Fish плавает в воде" },
      { type: 'quiz', question: "Укажи названия животных:", options: ["Cat 🐱", "Red", "Big", "Не знаю", "Другой вариант"], correctAnswer: "Cat 🐱", hint: "Animals = животные" },
      { type: 'quiz', question: "Как сказать \"спасибо\" по-английски?", options: ["Hello", "Thanks", "Goodbye", "Sorry", "Please"], correctAnswer: "Thanks", hint: "Thanks = спасибо" },
    ],
    reward: { stars: 3, message: "Wonderful! Ты знаешь животных! 🐾" }
  }
]
