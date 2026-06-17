// Экспорт игр для 1 класса
import { GameLesson } from '../types'

export const firstGradeGames: GameLesson[] = [
  {
    title: "Буквы и звуки",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Какая буква первая в алфавите?", options: ["А", "Д", "В", "Г", "Б"], correctAnswer: "А", hint: "Алфавит начинается с А" },
      { type: 'quiz', question: "Сколько гласных букв в русском алфавите?", options: ["12", "8", "6", "5", "10"], correctAnswer: "10", hint: "А, О, У, И, Ы, Э, Е, Ё, Ю, Я" },
      { type: 'quiz', question: "Буква М — это...", options: ["Гласная 🔴", "Цифра", "Согласная 🔵", "Буква", "Знак"], correctAnswer: "Согласная 🔵", hint: "М — согласный звук" },
      { type: 'quiz', question: "Сколько звуков в слове КОТ?", options: ["5", "2", "1", "3", "4"], correctAnswer: "3", hint: "К-О-Т — три звука" },
      { type: 'quiz', question: "С какого звука начинается слово ШАР?", options: ["О", "К", "А", "Р", "Ш"], correctAnswer: "Ш", hint: "Ш-ар" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Буквы и звуки»! 🎉" }
  },
  {
    title: "Слоги",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Сколько слогов в слове МА-МА?", options: ["1", "5", "3", "4", "2"], correctAnswer: "2", hint: "МА-МА — два слога" },
      { type: 'quiz', question: "Сколько слогов в слове ДОМ?", options: ["0", "2", "3", "1", "4"], correctAnswer: "1", hint: "Дом — один слог" },
      { type: 'quiz', question: "Сколько слогов в слове МА-ШИ-НА?", options: ["2", "3", "4", "1", "5"], correctAnswer: "3", hint: "МА-ШИ-НА — три слога" },
      { type: 'quiz', question: "Какое слово самое длинное?", options: ["Кот", "Шар", "Дом", "Сад", "Машина"], correctAnswer: "Машина", hint: "Машина — 3 слога" },
      { type: 'quiz', question: "Какое слово состоит из 1 слога?", options: ["Машина", "Собака", "Рука", "Кот", "Вода"], correctAnswer: "Кот", hint: "Кот — 1 слог" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Слоги»! 🎉" }
  },
  {
    title: "ЖИ-ШИ пиши с И",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Как правильно: МАШ__НА?", options: ["МАШИНА", "МАШОНА", "МАШЫНА", "МАШЭНА", "МАШЕНА"], correctAnswer: "МАШИНА", hint: "ЖИ-ШИ пиши с И!" },
      { type: 'quiz', question: "Как правильно написать?", options: ["ШЕНА 🛞", "ШИНА 🛞", "ШОНА 🛞", "ШЭНА 🛞", "ШЫНА 🛞"], correctAnswer: "ШИНА 🛞", hint: "ШИ всегда с И" },
      { type: 'quiz', question: "Вставь букву: Ж__РАФ 🦒", options: ["Ы", "Е", "О", "И", "Э"], correctAnswer: "И", hint: "ЖИ пиши с И!" },
      { type: 'quiz', question: "Вставь букву: ЛЫЖ__", options: ["Э", "Е", "И", "Ы", "О"], correctAnswer: "И", hint: "ЖИ пиши с И!" },
      { type: 'quiz', question: "Какое слово написано правильно?", options: ["ЖЫЗНЬ", "ЖИЗНЬ ✨", "ЖОЗНЬ", "ЖЭЗНЬ", "ЖЕЗНЬ"], correctAnswer: "ЖИЗНЬ ✨", hint: "ЖИ пиши с И!" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «ЖИ-ШИ пиши с И»! 🎉" }
  },
  {
    title: "ЧА-ЩА пиши с А",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Как правильно: ТУЧ__?", options: ["ТУЧЯ ☁️", "ТУЧО ☁️", "ТУЧИ ☁️", "ТУЧА ☁️", "ТУЧЕ ☁️"], correctAnswer: "ТУЧА ☁️", hint: "ЧА-ЩА пиши с А!" },
      { type: 'quiz', question: "Вставь букву: ЗАДАЧ__", options: ["О", "А", "Я", "И", "Е"], correctAnswer: "А", hint: "ЧА пиши с А!" },
      { type: 'quiz', question: "Какое слово написано правильно?", options: ["ЧИЩА", "ЧОЩА", "ЧАЩА 🌲", "ЧЕЩА", "ЧЯЩА"], correctAnswer: "ЧАЩА 🌲", hint: "ЧА-ЩА пиши с А!" },
      { type: 'quiz', question: "Вставь букву: РОЩ__", options: ["Е", "Я", "А", "О", "И"], correctAnswer: "А", hint: "ЩА пиши с А!" },
      { type: 'quiz', question: "Как правильно: ДАЧ__?", options: ["ДАЧА 🏡", "ДАЧИ", "ДАЧЕ", "ДАЧО", "ДАЧЯ"], correctAnswer: "ДАЧА 🏡", hint: "ЧА пиши с А!" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «ЧА-ЩА пиши с А»! 🎉" }
  },
  {
    title: "Большая буква",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "С какой буквы начинаются имена?", options: ["С большой", "С маленькой", "С цифры", "С точки", "С запятой"], correctAnswer: "С большой", hint: "Имена пишутся с большой буквы!" },
      { type: 'quiz', question: "Как написать название города?", options: ["МосКва", "мОсква", "Москва", "москва", "МОСКВА"], correctAnswer: "Москва", hint: "Города — с большой буквы" },
      { type: 'quiz', question: "Что пишется с большой буквы?", options: ["стол", "бежать", "красивый", "дом", "Александр"], correctAnswer: "Александр", hint: "Имена с большой буквы!" },
      { type: 'quiz', question: "Какое слово — имя?", options: ["красный", "Маша", "книга", "бежать", "стол"], correctAnswer: "Маша", hint: "Имена пишутся с большой буквы" },
      { type: 'quiz', question: "Название реки пишется:", options: ["С большой буквы", "С маленькой", "Прописными", "Как угодно", "Не важно"], correctAnswer: "С большой буквы", hint: "Названия рек — с большой буквы" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Большая буква»! 🎉" }
  },
  {
    title: "Басни",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Мораль басни — это:", options: ["Вступление", "Нравоучительный вывод", "Развязка", "Описание героев", "Завязка"], correctAnswer: "Нравоучительный вывод", hint: "Главный урок басни" },
      { type: 'quiz', question: "Автор «Ворона и Лисица»:", options: ["Толстой", "Пушкин", "Гоголь", "Лермонтов", "Крылов"], correctAnswer: "Крылов", hint: "И.А. Крылов" },
      { type: 'quiz', question: "Аллегория в басне — это:", options: ["Гипербола", "Метафора", "Прямое описание", "Сравнение", "Иносказание"], correctAnswer: "Иносказание", hint: "Животные = люди" },
      { type: 'quiz', question: "Басня — это:", options: ["Очерк", "Роман", "Стихотворение", "Краткий рассказ с моралью", "Пьеса"], correctAnswer: "Краткий рассказ с моралью", hint: "Краткость + мораль" },
      { type: 'quiz', question: "Крылов написал:", options: ["«Война и мир»", "«Стрекоза и Муравей»", "«Мёртвые души»", "«Руслан и Людмила»", "«Отцы и дети»"], correctAnswer: "«Стрекоза и Муравей»", hint: "Крылов — баснописец" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Басни»! 🎉" }
  },
  {
    title: "Сказки Пушкина",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Сколько лет ждал старик золотую рыбку?", options: ["40 лет", "20 лет", "30 лет и 3 года", "33 года", "35 лет"], correctAnswer: "30 лет и 3 года", hint: "«Жил старик со своею старухой...»" },
      { type: 'quiz', question: "Кто превратился в лебедя?", options: ["Повариха", "Боярышня", "Ткачиха", "Царевна", "Царица"], correctAnswer: "Царевна", hint: "Царевна-лебедь" },
      { type: 'quiz', question: "«Сказка о рыбаке и рыбке» — автор:", options: ["Гоголь", "Лермонтов", "Ершов", "Пушкин", "Толстой"], correctAnswer: "Пушкин", hint: "А.С. Пушкин" },
      { type: 'quiz', question: "Кто тянул репку первым?", options: ["Жучка", "Мышка", "Дедка", "Бабка", "Внучка"], correctAnswer: "Дедка", hint: "«Посадил дед репку...»" },
      { type: 'quiz', question: "Золотая рыбка исполнила:", options: ["5 желаний", "1 желание", "10 желаний", "3 желания (старухи)", "0 желаний"], correctAnswer: "3 желания (старухи)", hint: "Но старуха прогневала" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Сказки Пушкина»! 🎉" }
  },
  {
    title: "Счёт до 5",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Сколько яблок? 🍎🍎🍎", options: ["4", "1", "5", "2", "3"], correctAnswer: "3", hint: "Посчитай: раз, два, три!" },
      { type: 'quiz', question: "Сколько шариков? 🎈🎈", options: ["2", "3", "4", "1", "5"], correctAnswer: "2", hint: "Один, два!" },
      { type: 'quiz', question: "Какое число идёт после 4?", options: ["5", "2", "6", "7", "3"], correctAnswer: "5", hint: "1, 2, 3, 4, ..." },
      { type: 'quiz', question: "Сколько звёзд? ⭐⭐⭐⭐", options: ["4", "6", "3", "5", "2"], correctAnswer: "4", hint: "Посчитай: раз, два, три, четыре!" },
      { type: 'quiz', question: "Сколько котят? 🐱🐱🐱🐱🐱", options: ["6", "4", "2", "3", "5"], correctAnswer: "5", hint: "Посчитай всех котят!" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Счёт до 5»! 🎉" }
  },
  {
    title: "Счёт до 10",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Сколько пальцев на двух руках?", options: ["5", "9", "11", "10", "8"], correctAnswer: "10", hint: "5 на одной и 5 на другой" },
      { type: 'quiz', question: "Какое число идёт после 7?", options: ["7", "9", "8", "6", "10"], correctAnswer: "8", hint: "1, 2, 3, 4, 5, 6, 7, ..." },
      { type: 'quiz', question: "Какое число перед 5?", options: ["2", "6", "7", "3", "4"], correctAnswer: "4", hint: "Посчитай назад: 5, ..." },
      { type: 'quiz', question: "Какое число между 4 и 6?", options: ["3", "4", "6", "5", "7"], correctAnswer: "5", hint: "4, ?, 6" },
      { type: 'quiz', question: "Какое число идёт после 9?", options: ["8", "12", "10", "7", "11"], correctAnswer: "10", hint: "1, 2, 3, 4, 5, 6, 7, 8, 9, ..." }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Счёт до 10»! 🎉" }
  },
  {
    title: "Сложение до 10",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "2 + 3 = ?", options: ["6", "4", "5", "3", "7"], correctAnswer: "5", hint: "Два плюс три..." },
      { type: 'quiz', question: "4 + 2 = ?", options: ["8", "7", "6", "5", "4"], correctAnswer: "6", hint: "Четыре и два вместе" },
      { type: 'quiz', question: "5 + 5 = ?", options: ["10", "12", "9", "11", "8"], correctAnswer: "10", hint: "Это все пальцы на руках!" },
      { type: 'quiz', question: "1 + 1 = ?", options: ["1", "4", "3", "2", "0"], correctAnswer: "2", hint: "Один плюс один..." },
      { type: 'quiz', question: "3 + 4 = ?", options: ["9", "6", "8", "5", "7"], correctAnswer: "7", hint: "Три плюс четыре..." }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Сложение до 10»! 🎉" }
  },
  {
    title: "Вычитание",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "5 - 2 = ?", options: ["1", "4", "5", "2", "3"], correctAnswer: "3", hint: "Пять минус два..." },
      { type: 'quiz', question: "7 - 3 = ?", options: ["5", "3", "4", "2", "6"], correctAnswer: "4", hint: "Семь убери три" },
      { type: 'quiz', question: "8 - 0 = ?", options: ["9", "8", "6", "7", "0"], correctAnswer: "8", hint: "Если ничего не отнять..." },
      { type: 'quiz', question: "10 - 5 = ?", options: ["4", "7", "6", "3", "5"], correctAnswer: "5", hint: "Десять минус пять..." },
      { type: 'quiz', question: "6 - 6 = ?", options: ["1", "6", "2", "12", "0"], correctAnswer: "0", hint: "Отнять само себя = 0" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Вычитание»! 🎉" }
  },
  {
    title: "Сравнение",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Что больше: 3 или 5?", options: ["5", "Одинаково", "6", "2", "3"], correctAnswer: "5", hint: "5 идёт позже при счёте" },
      { type: 'quiz', question: "Что меньше: 2 или 4?", options: ["3", "Одинаково", "2", "1", "4"], correctAnswer: "2", hint: "2 идёт раньше при счёте" },
      { type: 'quiz', question: "3 и 3 — это...", options: ["4 больше", "3 меньше", "3 больше", "Одинаково", "2 больше"], correctAnswer: "Одинаково", hint: "Числа равны" },
      { type: 'quiz', question: "Что больше: 7 или 5?", options: ["7", "8", "5", "Одинаково", "6"], correctAnswer: "7", hint: "7 идёт позже" },
      { type: 'quiz', question: "Что меньше: 1 или 3?", options: ["Одинаково", "1", "2", "0", "3"], correctAnswer: "1", hint: "1 идёт раньше" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Сравнение»! 🎉" }
  },
  {
    title: "Животные",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какое животное говорит «Му»?", options: ["Лиса 🦊", "Кошка 🐱", "Собака 🐕", "Птица 🐦", "Корова 🐄"], correctAnswer: "Корова 🐄", hint: "Большое животное на ферме" },
      { type: 'quiz', question: "Кто умеет летать?", options: ["Кот 🐱", "Рыба 🐟", "Змея 🐍", "Собака 🐕", "Птица 🐦"], correctAnswer: "Птица 🐦", hint: "У кого есть крылья?" },
      { type: 'quiz', question: "Где живёт рыба?", options: ["На дереве 🌳", "В норе 🕳️", "В воде 🌊", "В гнезде 🪺", "В доме 🏠"], correctAnswer: "В воде 🌊", hint: "Рыба плавает" },
      { type: 'quiz', question: "Корова — какое животное?", options: ["Пустынное", "Лесное", "Морское", "Домашнее", "Дикое"], correctAnswer: "Домашнее", hint: "Живёт с людьми на ферме" },
      { type: 'quiz', question: "Кто живёт в дупле?", options: ["Муравей 🐜", "Рыба 🐟", "Белка 🐿️", "Заяц 🐰", "Волк 🐺"], correctAnswer: "Белка 🐿️", hint: "На дереве" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Животные»! 🎉" }
  },
  {
    title: "Времена года",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какое время года самое тёплое?", options: ["Зима ❄️", "Осень 🍂", "Весна 🌸", "Лето ☀️", "Все одинаково"], correctAnswer: "Лето ☀️", hint: "Можно купаться!" },
      { type: 'quiz', question: "Когда падает снег?", options: ["Всегда", "Зимой ❄️", "Летом ☀️", "Весной 🌸", "Осенью 🍂"], correctAnswer: "Зимой ❄️", hint: "Холодно, можно кататься на санках" },
      { type: 'quiz', question: "Сколько времён года?", options: ["4", "6", "5", "2", "3"], correctAnswer: "4", hint: "Зима, весна, лето, осень" },
      { type: 'quiz', question: "Что бывает весной?", options: ["Цветы 🌷", "Листопад 🍂", "Мороз 🥶", "Жара 🔥", "Снег ❄️"], correctAnswer: "Цветы 🌷", hint: "Весной всё расцветает" },
      { type: 'quiz', question: "После весны наступает:", options: ["Осень 🍂", "Весна 🌸", "Зима ❄️", "Снова весна", "Лето ☀️"], correctAnswer: "Лето ☀️", hint: "Весна, потом лето" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Времена года»! 🎉" }
  },
  {
    title: "Растения",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Что нужно растению для роста?", options: ["Мяч ⚽", "Только камни 🪨", "Мороженое 🍦", "Конфеты 🍬", "Вода и свет 💧☀️"], correctAnswer: "Вода и свет 💧☀️", hint: "Растения пьют и любят солнышко" },
      { type: 'quiz', question: "Какого цвета листья летом?", options: ["Белого", "Жёлтого", "Зелёного", "Синего", "Красного"], correctAnswer: "Зелёного", hint: "Вспомни деревья летом" },
      { type: 'quiz', question: "Что вырастает из семечка?", options: ["Звезда ⭐", "Камень 🪨", "Растение 🌱", "Машина 🚗", "Облако ☁️"], correctAnswer: "Растение 🌱", hint: "Семя — начало растения" },
      { type: 'quiz', question: "Где растут овощи?", options: ["В море 🌊", "В огороде 🥕", "На луне 🌙", "В космосе 🚀", "В холодильнике 🧊"], correctAnswer: "В огороде 🥕", hint: "На грядках" },
      { type: 'quiz', question: "Корень растения:", options: ["Делает фотосинтез", "Всасывает воду", "Производит семена", "Привлекает насекомых", "Растёт вверх"], correctAnswer: "Всасывает воду", hint: "Из почвы" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Растения»! 🎉" }
  },
  {
    title: "Приветствие",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Как сказать «Привет» по-английски?", options: ["Please", "Sorry", "Hello 👋", "Thanks 🙏", "Goodbye 👋"], correctAnswer: "Hello 👋", hint: "Самое популярное приветствие" },
      { type: 'quiz', question: "Что значит Hi?", options: ["Привет", "Спасибо", "Извините", "Пока", "Пожалуйста"], correctAnswer: "Привет", hint: "Hi = Привет" },
      { type: 'quiz', question: "Как сказать «Пока»?", options: ["Bye", "Thanks", "Hi", "Hello", "Sorry"], correctAnswer: "Bye", hint: "Bye = Пока" },
      { type: 'quiz', question: "Goodbye — это:", options: ["До свидания", "Извините", "Пожалуйста", "Спасибо", "Здравствуйте"], correctAnswer: "До свидания", hint: "Goodbye = прощание" },
      { type: 'quiz', question: "Как ответить на «How are you?»", options: ["Hello", "Goodbye", "Sorry", "I am fine", "Thank you"], correctAnswer: "I am fine", hint: "I am fine = Я в порядке" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Приветствие»! 🎉" }
  },
  {
    title: "Цвета",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Red — это:", options: ["Белый", "Синий", "Жёлтый", "Красный", "Зелёный"], correctAnswer: "Красный", hint: "Red = красный" },
      { type: 'quiz', question: "Как будет «жёлтый»?", options: ["Red", "White", "Yellow", "Blue", "Green"], correctAnswer: "Yellow", hint: "Yellow = цвет солнца" },
      { type: 'quiz', question: "Зелёный по-английски:", options: ["Red", "Green", "Blue", "Yellow", "Black"], correctAnswer: "Green", hint: "Green = зелёный" },
      { type: 'quiz', question: "Blue — это:", options: ["Красный", "Жёлтый", "Зелёный", "Чёрный", "Синий"], correctAnswer: "Синий", hint: "Blue = синий" },
      { type: 'quiz', question: "Какой цвет — White?", options: ["Красный", "Синий", "Чёрный", "Белый", "Зелёный"], correctAnswer: "Белый", hint: "White = белый" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Цвета»! 🎉" }
  },
  {
    title: "Числа",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "One — это:", options: ["Три", "Пять", "Один", "Два", "Четыре"], correctAnswer: "Один", hint: "One = 1" },
      { type: 'quiz', question: "Как будет «три»?", options: ["One", "Five", "Two", "Three", "Four"], correctAnswer: "Three", hint: "Three = 3" },
      { type: 'quiz', question: "Five — это:", options: ["Шесть", "Четыре", "Два", "Пять", "Три"], correctAnswer: "Пять", hint: "Five = 5" },
      { type: 'quiz', question: "Two — это:", options: ["Четыре", "Три", "Два", "Один", "Пять"], correctAnswer: "Два", hint: "Two = 2" },
      { type: 'quiz', question: "Как будет «десять»?", options: ["Six", "Nine", "Ten", "Seven", "Eight"], correctAnswer: "Ten", hint: "Ten = 10" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Числа»! 🎉" }
  },
  {
    title: "Технология",
    subject: "Технология",
    icon: "Ruler",
    color: "text-yellow-400",
    tasks: [
      { type: 'quiz', question: "Бумага — материал из:", options: ["Пластика", "Древесины", "Резины", "Стекла", "Металла"], correctAnswer: "Древесины", hint: "Целлюлоза из дерева" },
      { type: 'quiz', question: "Ножницы — инструмент для:", options: ["Лепки", "Резания", "Шитья", "Клея", "Рисования"], correctAnswer: "Резания", hint: "Режут бумагу" },
      { type: 'quiz', question: "Клей нужен для:", options: ["Рисования", "Измерения", "Резания", "Соединения деталей", "Лепки"], correctAnswer: "Соединения деталей", hint: "Склеиваем части" },
      { type: 'quiz', question: "Какой инструмент измеряет длину?", options: ["Линейка", "Кисть", "Молоток", "Карандаш", "Ножницы"], correctAnswer: "Линейка", hint: "В сантиметрах" },
      { type: 'quiz', question: "Оригами — это:", options: ["Вязание", "Рисование", "Искусство складывания бумаги", "Шитьё", "Лепка"], correctAnswer: "Искусство складывания бумаги", hint: "Японское искусство" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Технология»! 🎉" }
  },
  {
    title: "Цвета",
    subject: "ИЗО",
    icon: "Palette",
    color: "text-rose-400",
    tasks: [
      { type: 'quiz', question: "Какого цвета солнце? ☀️", options: ["Фиолетовое", "Жёлтое", "Синее", "Зелёное", "Красное"], correctAnswer: "Жёлтое", hint: "Солнце яркое и тёплое" },
      { type: 'quiz', question: "Смешай жёлтый и синий:", options: ["Зелёный", "Оранжевый", "Красный", "Коричневый", "Фиолетовый"], correctAnswer: "Зелёный", hint: "Жёлтый + синий = зелёный" },
      { type: 'quiz', question: "Какого цвета трава? 🌿", options: ["Красная", "Жёлтая", "Зелёная", "Синяя", "Белая"], correctAnswer: "Зелёная", hint: "Трава зелёная" },
      { type: 'quiz', question: "Красный + жёлтый =", options: ["Оранжевый", "Синий", "Коричневый", "Зелёный", "Фиолетовый"], correctAnswer: "Оранжевый", hint: "Тёплый цвет" },
      { type: 'quiz', question: "Красный + синий =", options: ["Жёлтый", "Зелёный", "Оранжевый", "Коричневый", "Фиолетовый"], correctAnswer: "Фиолетовый", hint: "Холодный цвет" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Цвета»! 🎉" }
  },
  {
    title: "Музыкальные инструменты",
    subject: "Музыка",
    icon: "Music",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Какой инструмент бьют палочками?", options: ["Пианино 🎹", "Барабан 🥁", "Скрипка 🎻", "Гитара 🎸", "Флейта 🎶"], correctAnswer: "Барабан 🥁", hint: "Бум-бум-бум!" },
      { type: 'quiz', question: "Сколько нот в музыке?", options: ["6", "7", "12", "5", "8"], correctAnswer: "7", hint: "До, ре, ми, фа, соль, ля, си" },
      { type: 'quiz', question: "Чёрно-белый инструмент:", options: ["Барабан 🥁", "Гитара 🎸", "Труба 🎺", "Пианино 🎹", "Скрипка 🎻"], correctAnswer: "Пианино 🎹", hint: "Клавиши чёрные и белые" },
      { type: 'quiz', question: "У какого инструмента струны?", options: ["Бубен", "Барабан 🥁", "Гитара 🎸", "Труба 🎺", "Флейта 🎶"], correctAnswer: "Гитара 🎸", hint: "Дзинь-дзинь!" },
      { type: 'quiz', question: "Дирижёр руководит:", options: ["Хором", "Оркестром", "Кинотеатром", "Театром", "Цирком"], correctAnswer: "Оркестром", hint: "Дирижёр — руководитель" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Музыкальные инструменты»! 🎉" }
  },
  {
    title: "Спорт",
    subject: "Физкультура",
    icon: "Dumbbell",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Футбол играют:", options: ["Ногами и мячом ⚽", "Руками", "Клюшкой", "Без мяча", "Ракеткой"], correctAnswer: "Ногами и мячом ⚽", hint: "Футбол — ногами!" },
      { type: 'quiz', question: "Сколько игроков в команде по футболу?", options: ["11", "5", "6", "9", "7"], correctAnswer: "11", hint: "11 на поле" },
      { type: 'quiz', question: "Что полезно для здоровья?", options: ["Есть конфеты", "Не спать", "Зарядка", "Сидеть весь день", "Мало двигаться"], correctAnswer: "Зарядка", hint: "Движение — жизнь!" },
      { type: 'quiz', question: "Баскетбол играют:", options: ["Руками и мячом 🏀", "Без мяча", "Ракеткой", "Ногами", "Клюшкой"], correctAnswer: "Руками и мячом 🏀", hint: "Забрасываем в кольцо" },
      { type: 'quiz', question: "Сколько раз в неделю нужно заниматься спортом?", options: ["2", "7", "1", "3-4", "0"], correctAnswer: "3-4", hint: "Регулярность важна" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Спорт»! 🎉" }
  },
]
