// Экспорт игр для 2 класса
import { GameLesson } from '../types'

export const secondGradeGames: GameLesson[] = [
  {
    title: "Буквы и звуки",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Какая буква первая в алфавите?", options: ["А", "Д", "В", "Г", "Б"], correctAnswer: "А", hint: "Алфавит начинается с А" },
      { type: 'quiz', question: "Сколько гласных букв в русском алфавите?", options: ["6", "10", "5", "12", "8"], correctAnswer: "10", hint: "А, О, У, И, Ы, Э, Е, Ё, Ю, Я" },
      { type: 'quiz', question: "Буква М — это...", options: ["Гласная 🔴", "Согласная 🔵", "Знак", "Цифра", "Буква"], correctAnswer: "Согласная 🔵", hint: "М — согласный звук" },
      { type: 'quiz', question: "Сколько звуков в слове КОТ?", options: ["5", "2", "1", "4", "3"], correctAnswer: "3", hint: "К-О-Т — три звука" },
      { type: 'quiz', question: "С какого звука начинается слово ШАР?", options: ["О", "К", "Р", "А", "Ш"], correctAnswer: "Ш", hint: "Ш-ар" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Буквы и звуки»! 🎉" }
  },
  {
    title: "Слоги",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Сколько слогов в слове МА-МА?", options: ["4", "3", "2", "5", "1"], correctAnswer: "2", hint: "МА-МА — два слога" },
      { type: 'quiz', question: "Сколько слогов в слове ДОМ?", options: ["3", "0", "4", "2", "1"], correctAnswer: "1", hint: "Дом — один слог" },
      { type: 'quiz', question: "Сколько слогов в слове МА-ШИ-НА?", options: ["2", "3", "1", "5", "4"], correctAnswer: "3", hint: "МА-ШИ-НА — три слога" },
      { type: 'quiz', question: "Какое слово самое длинное?", options: ["Дом", "Машина", "Кот", "Сад", "Шар"], correctAnswer: "Машина", hint: "Машина — 3 слога" },
      { type: 'quiz', question: "Какое слово состоит из 1 слога?", options: ["Вода", "Собака", "Рука", "Кот", "Машина"], correctAnswer: "Кот", hint: "Кот — 1 слог" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Слоги»! 🎉" }
  },
  {
    title: "ЖИ-ШИ пиши с И",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Как правильно: МАШ__НА?", options: ["МАШИНА", "МАШЕНА", "МАШЭНА", "МАШОНА", "МАШЫНА"], correctAnswer: "МАШИНА", hint: "ЖИ-ШИ пиши с И!" },
      { type: 'quiz', question: "Как правильно написать?", options: ["ШЭНА 🛞", "ШЕНА 🛞", "ШОНА 🛞", "ШЫНА 🛞", "ШИНА 🛞"], correctAnswer: "ШИНА 🛞", hint: "ШИ всегда с И" },
      { type: 'quiz', question: "Вставь букву: Ж__РАФ 🦒", options: ["И", "О", "Э", "Е", "Ы"], correctAnswer: "И", hint: "ЖИ пиши с И!" },
      { type: 'quiz', question: "Вставь букву: ЛЫЖ__", options: ["И", "Ы", "Э", "О", "Е"], correctAnswer: "И", hint: "ЖИ пиши с И!" },
      { type: 'quiz', question: "Какое слово написано правильно?", options: ["ЖИЗНЬ ✨", "ЖЭЗНЬ", "ЖОЗНЬ", "ЖЕЗНЬ", "ЖЫЗНЬ"], correctAnswer: "ЖИЗНЬ ✨", hint: "ЖИ пиши с И!" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «ЖИ-ШИ пиши с И»! 🎉" }
  },
  {
    title: "ЧА-ЩА пиши с А",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Как правильно: ТУЧ__?", options: ["ТУЧА ☁️", "ТУЧО ☁️", "ТУЧИ ☁️", "ТУЧЕ ☁️", "ТУЧЯ ☁️"], correctAnswer: "ТУЧА ☁️", hint: "ЧА-ЩА пиши с А!" },
      { type: 'quiz', question: "Вставь букву: ЗАДАЧ__", options: ["И", "А", "О", "Е", "Я"], correctAnswer: "А", hint: "ЧА пиши с А!" },
      { type: 'quiz', question: "Какое слово написано правильно?", options: ["ЧАЩА 🌲", "ЧОЩА", "ЧИЩА", "ЧЯЩА", "ЧЕЩА"], correctAnswer: "ЧАЩА 🌲", hint: "ЧА-ЩА пиши с А!" },
      { type: 'quiz', question: "Вставь букву: РОЩ__", options: ["Я", "О", "И", "А", "Е"], correctAnswer: "А", hint: "ЩА пиши с А!" },
      { type: 'quiz', question: "Как правильно: ДАЧ__?", options: ["ДАЧО", "ДАЧА 🏡", "ДАЧЕ", "ДАЧИ", "ДАЧЯ"], correctAnswer: "ДАЧА 🏡", hint: "ЧА пиши с А!" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «ЧА-ЩА пиши с А»! 🎉" }
  },
  {
    title: "Большая буква",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "С какой буквы начинаются имена?", options: ["С точки", "С цифры", "С запятой", "С большой", "С маленькой"], correctAnswer: "С большой", hint: "Имена пишутся с большой буквы!" },
      { type: 'quiz', question: "Как написать название города?", options: ["МосКва", "Москва", "москва", "мОсква", "МОСКВА"], correctAnswer: "Москва", hint: "Города — с большой буквы" },
      { type: 'quiz', question: "Что пишется с большой буквы?", options: ["бежать", "Александр", "дом", "красивый", "стол"], correctAnswer: "Александр", hint: "Имена с большой буквы!" },
      { type: 'quiz', question: "Какое слово — имя?", options: ["книга", "Маша", "стол", "бежать", "красный"], correctAnswer: "Маша", hint: "Имена пишутся с большой буквы" },
      { type: 'quiz', question: "Название реки пишется:", options: ["С большой буквы", "Не важно", "С маленькой", "Как угодно", "Прописными"], correctAnswer: "С большой буквы", hint: "Названия рек — с большой буквы" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Большая буква»! 🎉" }
  },
  {
    title: "Басни",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Мораль басни — это:", options: ["Описание героев", "Нравоучительный вывод", "Развязка", "Вступление", "Завязка"], correctAnswer: "Нравоучительный вывод", hint: "Главный урок басни" },
      { type: 'quiz', question: "Автор «Ворона и Лисица»:", options: ["Толстой", "Крылов", "Пушкин", "Гоголь", "Лермонтов"], correctAnswer: "Крылов", hint: "И.А. Крылов" },
      { type: 'quiz', question: "Аллегория в басне — это:", options: ["Иносказание", "Прямое описание", "Метафора", "Сравнение", "Гипербола"], correctAnswer: "Иносказание", hint: "Животные = люди" },
      { type: 'quiz', question: "Басня — это:", options: ["Очерк", "Стихотворение", "Краткий рассказ с моралью", "Пьеса", "Роман"], correctAnswer: "Краткий рассказ с моралью", hint: "Краткость + мораль" },
      { type: 'quiz', question: "Крылов написал:", options: ["«Мёртвые души»", "«Руслан и Людмила»", "«Отцы и дети»", "«Стрекоза и Муравей»", "«Война и мир»"], correctAnswer: "«Стрекоза и Муравей»", hint: "Крылов — баснописец" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Басни»! 🎉" }
  },
  {
    title: "Сказки Пушкина",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Сколько лет ждал старик золотую рыбку?", options: ["40 лет", "35 лет", "30 лет и 3 года", "20 лет", "33 года"], correctAnswer: "30 лет и 3 года", hint: "«Жил старик со своею старухой...»" },
      { type: 'quiz', question: "Кто превратился в лебедя?", options: ["Боярышня", "Царевна", "Царица", "Повариха", "Ткачиха"], correctAnswer: "Царевна", hint: "Царевна-лебедь" },
      { type: 'quiz', question: "«Сказка о рыбаке и рыбке» — автор:", options: ["Пушкин", "Ершов", "Лермонтов", "Гоголь", "Толстой"], correctAnswer: "Пушкин", hint: "А.С. Пушкин" },
      { type: 'quiz', question: "Кто тянул репку первым?", options: ["Мышка", "Дедка", "Бабка", "Жучка", "Внучка"], correctAnswer: "Дедка", hint: "«Посадил дед репку...»" },
      { type: 'quiz', question: "Золотая рыбка исполнила:", options: ["1 желание", "0 желаний", "5 желаний", "3 желания (старухи)", "10 желаний"], correctAnswer: "3 желания (старухи)", hint: "Но старуха прогневала" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Сказки Пушкина»! 🎉" }
  },
  {
    title: "Счёт до 5",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Сколько яблок? 🍎🍎🍎", options: ["1", "3", "5", "2", "4"], correctAnswer: "3", hint: "Посчитай: раз, два, три!" },
      { type: 'quiz', question: "Сколько шариков? 🎈🎈", options: ["1", "3", "4", "5", "2"], correctAnswer: "2", hint: "Один, два!" },
      { type: 'quiz', question: "Какое число идёт после 4?", options: ["2", "6", "7", "3", "5"], correctAnswer: "5", hint: "1, 2, 3, 4, ..." },
      { type: 'quiz', question: "Сколько звёзд? ⭐⭐⭐⭐", options: ["3", "6", "5", "4", "2"], correctAnswer: "4", hint: "Посчитай: раз, два, три, четыре!" },
      { type: 'quiz', question: "Сколько котят? 🐱🐱🐱🐱🐱", options: ["2", "5", "3", "4", "6"], correctAnswer: "5", hint: "Посчитай всех котят!" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Счёт до 5»! 🎉" }
  },
  {
    title: "Счёт до 10",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Сколько пальцев на двух руках?", options: ["8", "5", "9", "10", "11"], correctAnswer: "10", hint: "5 на одной и 5 на другой" },
      { type: 'quiz', question: "Какое число идёт после 7?", options: ["7", "9", "6", "10", "8"], correctAnswer: "8", hint: "1, 2, 3, 4, 5, 6, 7, ..." },
      { type: 'quiz', question: "Какое число перед 5?", options: ["7", "6", "4", "3", "2"], correctAnswer: "4", hint: "Посчитай назад: 5, ..." },
      { type: 'quiz', question: "Какое число между 4 и 6?", options: ["3", "6", "4", "7", "5"], correctAnswer: "5", hint: "4, ?, 6" },
      { type: 'quiz', question: "Какое число идёт после 9?", options: ["7", "11", "8", "10", "12"], correctAnswer: "10", hint: "1, 2, 3, 4, 5, 6, 7, 8, 9, ..." }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Счёт до 10»! 🎉" }
  },
  {
    title: "Сложение до 10",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "2 + 3 = ?", options: ["3", "4", "7", "5", "6"], correctAnswer: "5", hint: "Два плюс три..." },
      { type: 'quiz', question: "4 + 2 = ?", options: ["7", "8", "5", "4", "6"], correctAnswer: "6", hint: "Четыре и два вместе" },
      { type: 'quiz', question: "5 + 5 = ?", options: ["10", "9", "12", "11", "8"], correctAnswer: "10", hint: "Это все пальцы на руках!" },
      { type: 'quiz', question: "1 + 1 = ?", options: ["3", "4", "2", "0", "1"], correctAnswer: "2", hint: "Один плюс один..." },
      { type: 'quiz', question: "3 + 4 = ?", options: ["7", "8", "6", "5", "9"], correctAnswer: "7", hint: "Три плюс четыре..." }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Сложение до 10»! 🎉" }
  },
  {
    title: "Вычитание",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "5 - 2 = ?", options: ["1", "3", "2", "4", "5"], correctAnswer: "3", hint: "Пять минус два..." },
      { type: 'quiz', question: "7 - 3 = ?", options: ["2", "6", "3", "5", "4"], correctAnswer: "4", hint: "Семь убери три" },
      { type: 'quiz', question: "8 - 0 = ?", options: ["7", "8", "0", "6", "9"], correctAnswer: "8", hint: "Если ничего не отнять..." },
      { type: 'quiz', question: "10 - 5 = ?", options: ["7", "4", "5", "6", "3"], correctAnswer: "5", hint: "Десять минус пять..." },
      { type: 'quiz', question: "6 - 6 = ?", options: ["0", "2", "12", "6", "1"], correctAnswer: "0", hint: "Отнять само себя = 0" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Вычитание»! 🎉" }
  },
  {
    title: "Сравнение",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Что больше: 3 или 5?", options: ["3", "5", "2", "6", "Одинаково"], correctAnswer: "5", hint: "5 идёт позже при счёте" },
      { type: 'quiz', question: "Что меньше: 2 или 4?", options: ["1", "Одинаково", "2", "4", "3"], correctAnswer: "2", hint: "2 идёт раньше при счёте" },
      { type: 'quiz', question: "3 и 3 — это...", options: ["3 больше", "Одинаково", "3 меньше", "4 больше", "2 больше"], correctAnswer: "Одинаково", hint: "Числа равны" },
      { type: 'quiz', question: "Что больше: 7 или 5?", options: ["Одинаково", "7", "5", "8", "6"], correctAnswer: "7", hint: "7 идёт позже" },
      { type: 'quiz', question: "Что меньше: 1 или 3?", options: ["2", "3", "0", "Одинаково", "1"], correctAnswer: "1", hint: "1 идёт раньше" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Сравнение»! 🎉" }
  },
  {
    title: "Животные",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какое животное говорит «Му»?", options: ["Корова 🐄", "Птица 🐦", "Лиса 🦊", "Собака 🐕", "Кошка 🐱"], correctAnswer: "Корова 🐄", hint: "Большое животное на ферме" },
      { type: 'quiz', question: "Кто умеет летать?", options: ["Птица 🐦", "Собака 🐕", "Рыба 🐟", "Змея 🐍", "Кот 🐱"], correctAnswer: "Птица 🐦", hint: "У кого есть крылья?" },
      { type: 'quiz', question: "Где живёт рыба?", options: ["В воде 🌊", "В доме 🏠", "В гнезде 🪺", "На дереве 🌳", "В норе 🕳️"], correctAnswer: "В воде 🌊", hint: "Рыба плавает" },
      { type: 'quiz', question: "Корова — какое животное?", options: ["Лесное", "Пустынное", "Домашнее", "Дикое", "Морское"], correctAnswer: "Домашнее", hint: "Живёт с людьми на ферме" },
      { type: 'quiz', question: "Кто живёт в дупле?", options: ["Волк 🐺", "Заяц 🐰", "Муравей 🐜", "Белка 🐿️", "Рыба 🐟"], correctAnswer: "Белка 🐿️", hint: "На дереве" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Животные»! 🎉" }
  },
  {
    title: "Времена года",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какое время года самое тёплое?", options: ["Лето ☀️", "Осень 🍂", "Весна 🌸", "Все одинаково", "Зима ❄️"], correctAnswer: "Лето ☀️", hint: "Можно купаться!" },
      { type: 'quiz', question: "Когда падает снег?", options: ["Летом ☀️", "Осенью 🍂", "Зимой ❄️", "Всегда", "Весной 🌸"], correctAnswer: "Зимой ❄️", hint: "Холодно, можно кататься на санках" },
      { type: 'quiz', question: "Сколько времён года?", options: ["6", "4", "5", "2", "3"], correctAnswer: "4", hint: "Зима, весна, лето, осень" },
      { type: 'quiz', question: "Что бывает весной?", options: ["Снег ❄️", "Листопад 🍂", "Мороз 🥶", "Цветы 🌷", "Жара 🔥"], correctAnswer: "Цветы 🌷", hint: "Весной всё расцветает" },
      { type: 'quiz', question: "После весны наступает:", options: ["Снова весна", "Зима ❄️", "Весна 🌸", "Лето ☀️", "Осень 🍂"], correctAnswer: "Лето ☀️", hint: "Весна, потом лето" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Времена года»! 🎉" }
  },
  {
    title: "Растения",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Что нужно растению для роста?", options: ["Мяч ⚽", "Мороженое 🍦", "Вода и свет 💧☀️", "Только камни 🪨", "Конфеты 🍬"], correctAnswer: "Вода и свет 💧☀️", hint: "Растения пьют и любят солнышко" },
      { type: 'quiz', question: "Какого цвета листья летом?", options: ["Зелёного", "Жёлтого", "Красного", "Синего", "Белого"], correctAnswer: "Зелёного", hint: "Вспомни деревья летом" },
      { type: 'quiz', question: "Что вырастает из семечка?", options: ["Камень 🪨", "Машина 🚗", "Растение 🌱", "Облако ☁️", "Звезда ⭐"], correctAnswer: "Растение 🌱", hint: "Семя — начало растения" },
      { type: 'quiz', question: "Где растут овощи?", options: ["В море 🌊", "В холодильнике 🧊", "В огороде 🥕", "На луне 🌙", "В космосе 🚀"], correctAnswer: "В огороде 🥕", hint: "На грядках" },
      { type: 'quiz', question: "Корень растения:", options: ["Делает фотосинтез", "Привлекает насекомых", "Всасывает воду", "Растёт вверх", "Производит семена"], correctAnswer: "Всасывает воду", hint: "Из почвы" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Растения»! 🎉" }
  },
  {
    title: "Приветствие",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Как сказать «Привет» по-английски?", options: ["Hello 👋", "Sorry", "Thanks 🙏", "Please", "Goodbye 👋"], correctAnswer: "Hello 👋", hint: "Самое популярное приветствие" },
      { type: 'quiz', question: "Что значит Hi?", options: ["Спасибо", "Извините", "Пожалуйста", "Пока", "Привет"], correctAnswer: "Привет", hint: "Hi = Привет" },
      { type: 'quiz', question: "Как сказать «Пока»?", options: ["Bye", "Thanks", "Hi", "Hello", "Sorry"], correctAnswer: "Bye", hint: "Bye = Пока" },
      { type: 'quiz', question: "Goodbye — это:", options: ["До свидания", "Спасибо", "Здравствуйте", "Извините", "Пожалуйста"], correctAnswer: "До свидания", hint: "Goodbye = прощание" },
      { type: 'quiz', question: "Как ответить на «How are you?»", options: ["Goodbye", "Sorry", "Hello", "I am fine", "Thank you"], correctAnswer: "I am fine", hint: "I am fine = Я в порядке" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Приветствие»! 🎉" }
  },
  {
    title: "Цвета",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Red — это:", options: ["Зелёный", "Красный", "Жёлтый", "Белый", "Синий"], correctAnswer: "Красный", hint: "Red = красный" },
      { type: 'quiz', question: "Как будет «жёлтый»?", options: ["Red", "Blue", "Yellow", "White", "Green"], correctAnswer: "Yellow", hint: "Yellow = цвет солнца" },
      { type: 'quiz', question: "Зелёный по-английски:", options: ["Yellow", "Blue", "Black", "Green", "Red"], correctAnswer: "Green", hint: "Green = зелёный" },
      { type: 'quiz', question: "Blue — это:", options: ["Зелёный", "Синий", "Красный", "Жёлтый", "Чёрный"], correctAnswer: "Синий", hint: "Blue = синий" },
      { type: 'quiz', question: "Какой цвет — White?", options: ["Белый", "Зелёный", "Синий", "Красный", "Чёрный"], correctAnswer: "Белый", hint: "White = белый" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Цвета»! 🎉" }
  },
  {
    title: "Числа",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "One — это:", options: ["Два", "Пять", "Три", "Один", "Четыре"], correctAnswer: "Один", hint: "One = 1" },
      { type: 'quiz', question: "Как будет «три»?", options: ["One", "Three", "Five", "Two", "Four"], correctAnswer: "Three", hint: "Three = 3" },
      { type: 'quiz', question: "Five — это:", options: ["Шесть", "Пять", "Четыре", "Три", "Два"], correctAnswer: "Пять", hint: "Five = 5" },
      { type: 'quiz', question: "Two — это:", options: ["Четыре", "Пять", "Два", "Один", "Три"], correctAnswer: "Два", hint: "Two = 2" },
      { type: 'quiz', question: "Как будет «десять»?", options: ["Ten", "Six", "Seven", "Nine", "Eight"], correctAnswer: "Ten", hint: "Ten = 10" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Числа»! 🎉" }
  },
  {
    title: "Технология",
    subject: "Технология",
    icon: "Ruler",
    color: "text-yellow-400",
    tasks: [
      { type: 'quiz', question: "Бумага — материал из:", options: ["Резины", "Металла", "Пластика", "Древесины", "Стекла"], correctAnswer: "Древесины", hint: "Целлюлоза из дерева" },
      { type: 'quiz', question: "Ножницы — инструмент для:", options: ["Резания", "Клея", "Шитья", "Рисования", "Лепки"], correctAnswer: "Резания", hint: "Режут бумагу" },
      { type: 'quiz', question: "Клей нужен для:", options: ["Резания", "Измерения", "Рисования", "Соединения деталей", "Лепки"], correctAnswer: "Соединения деталей", hint: "Склеиваем части" },
      { type: 'quiz', question: "Какой инструмент измеряет длину?", options: ["Линейка", "Ножницы", "Молоток", "Кисть", "Карандаш"], correctAnswer: "Линейка", hint: "В сантиметрах" },
      { type: 'quiz', question: "Оригами — это:", options: ["Лепка", "Рисование", "Вязание", "Шитьё", "Искусство складывания бумаги"], correctAnswer: "Искусство складывания бумаги", hint: "Японское искусство" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Технология»! 🎉" }
  },
  {
    title: "Цвета",
    subject: "ИЗО",
    icon: "Palette",
    color: "text-rose-400",
    tasks: [
      { type: 'quiz', question: "Какого цвета солнце? ☀️", options: ["Фиолетовое", "Синее", "Красное", "Жёлтое", "Зелёное"], correctAnswer: "Жёлтое", hint: "Солнце яркое и тёплое" },
      { type: 'quiz', question: "Смешай жёлтый и синий:", options: ["Фиолетовый", "Зелёный", "Оранжевый", "Красный", "Коричневый"], correctAnswer: "Зелёный", hint: "Жёлтый + синий = зелёный" },
      { type: 'quiz', question: "Какого цвета трава? 🌿", options: ["Зелёная", "Красная", "Синяя", "Жёлтая", "Белая"], correctAnswer: "Зелёная", hint: "Трава зелёная" },
      { type: 'quiz', question: "Красный + жёлтый =", options: ["Коричневый", "Фиолетовый", "Зелёный", "Синий", "Оранжевый"], correctAnswer: "Оранжевый", hint: "Тёплый цвет" },
      { type: 'quiz', question: "Красный + синий =", options: ["Зелёный", "Фиолетовый", "Жёлтый", "Коричневый", "Оранжевый"], correctAnswer: "Фиолетовый", hint: "Холодный цвет" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Цвета»! 🎉" }
  },
  {
    title: "Музыкальные инструменты",
    subject: "Музыка",
    icon: "Music",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Какой инструмент бьют палочками?", options: ["Барабан 🥁", "Пианино 🎹", "Гитара 🎸", "Флейта 🎶", "Скрипка 🎻"], correctAnswer: "Барабан 🥁", hint: "Бум-бум-бум!" },
      { type: 'quiz', question: "Сколько нот в музыке?", options: ["5", "7", "12", "8", "6"], correctAnswer: "7", hint: "До, ре, ми, фа, соль, ля, си" },
      { type: 'quiz', question: "Чёрно-белый инструмент:", options: ["Гитара 🎸", "Труба 🎺", "Барабан 🥁", "Пианино 🎹", "Скрипка 🎻"], correctAnswer: "Пианино 🎹", hint: "Клавиши чёрные и белые" },
      { type: 'quiz', question: "У какого инструмента струны?", options: ["Бубен", "Труба 🎺", "Барабан 🥁", "Гитара 🎸", "Флейта 🎶"], correctAnswer: "Гитара 🎸", hint: "Дзинь-дзинь!" },
      { type: 'quiz', question: "Дирижёр руководит:", options: ["Театром", "Оркестром", "Хором", "Кинотеатром", "Цирком"], correctAnswer: "Оркестром", hint: "Дирижёр — руководитель" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Музыкальные инструменты»! 🎉" }
  },
  {
    title: "Спорт",
    subject: "Физкультура",
    icon: "Dumbbell",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Футбол играют:", options: ["Ногами и мячом ⚽", "Без мяча", "Клюшкой", "Ракеткой", "Руками"], correctAnswer: "Ногами и мячом ⚽", hint: "Футбол — ногами!" },
      { type: 'quiz', question: "Сколько игроков в команде по футболу?", options: ["7", "5", "6", "11", "9"], correctAnswer: "11", hint: "11 на поле" },
      { type: 'quiz', question: "Что полезно для здоровья?", options: ["Зарядка", "Есть конфеты", "Не спать", "Сидеть весь день", "Мало двигаться"], correctAnswer: "Зарядка", hint: "Движение — жизнь!" },
      { type: 'quiz', question: "Баскетбол играют:", options: ["Ногами", "Ракеткой", "Без мяча", "Руками и мячом 🏀", "Клюшкой"], correctAnswer: "Руками и мячом 🏀", hint: "Забрасываем в кольцо" },
      { type: 'quiz', question: "Сколько раз в неделю нужно заниматься спортом?", options: ["2", "3-4", "0", "7", "1"], correctAnswer: "3-4", hint: "Регулярность важна" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Спорт»! 🎉" }
  },
]
