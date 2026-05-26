// Экспорт игр для подготовительного класса
import { GameLesson } from '../types'

export const prepClassGames: GameLesson[] = [
  {
    title: "Буквы и звуки",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Какая буква первая в алфавите?", options: ["Г", "В", "Д", "А", "Б"], correctAnswer: "А", hint: "Алфавит начинается с А" },
      { type: 'quiz', question: "Сколько гласных букв в русском алфавите?", options: ["12", "5", "6", "8", "10"], correctAnswer: "10", hint: "А, О, У, И, Ы, Э, Е, Ё, Ю, Я" },
      { type: 'quiz', question: "Буква М — это...", options: ["Гласная 🔴", "Согласная 🔵", "Знак", "Цифра", "Буква"], correctAnswer: "Согласная 🔵", hint: "М — согласный звук" },
      { type: 'quiz', question: "Сколько звуков в слове КОТ?", options: ["2", "4", "5", "1", "3"], correctAnswer: "3", hint: "К-О-Т — три звука" },
      { type: 'quiz', question: "С какого звука начинается слово ШАР?", options: ["К", "Ш", "Р", "А", "О"], correctAnswer: "Ш", hint: "Ш-ар" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Буквы и звуки»! 🎉" }
  },
  {
    title: "Слоги",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Сколько слогов в слове МА-МА?", options: ["4", "5", "1", "3", "2"], correctAnswer: "2", hint: "МА-МА — два слога" },
      { type: 'quiz', question: "Сколько слогов в слове ДОМ?", options: ["1", "2", "4", "0", "3"], correctAnswer: "1", hint: "Дом — один слог" },
      { type: 'quiz', question: "Сколько слогов в слове МА-ШИ-НА?", options: ["2", "3", "1", "5", "4"], correctAnswer: "3", hint: "МА-ШИ-НА — три слога" },
      { type: 'quiz', question: "Какое слово самое длинное?", options: ["Машина", "Сад", "Дом", "Шар", "Кот"], correctAnswer: "Машина", hint: "Машина — 3 слога" },
      { type: 'quiz', question: "Какое слово состоит из 1 слога?", options: ["Машина", "Вода", "Кот", "Собака", "Рука"], correctAnswer: "Кот", hint: "Кот — 1 слог" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Слоги»! 🎉" }
  },
  {
    title: "ЖИ-ШИ пиши с И",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Как правильно: МАШ__НА?", options: ["МАШИНА", "МАШЭНА", "МАШЕНА", "МАШЫНА", "МАШОНА"], correctAnswer: "МАШИНА", hint: "ЖИ-ШИ пиши с И!" },
      { type: 'quiz', question: "Как правильно написать?", options: ["ШИНА 🛞", "ШЭНА 🛞", "ШЫНА 🛞", "ШЕНА 🛞", "ШОНА 🛞"], correctAnswer: "ШИНА 🛞", hint: "ШИ всегда с И" },
      { type: 'quiz', question: "Вставь букву: Ж__РАФ 🦒", options: ["Э", "О", "И", "Е", "Ы"], correctAnswer: "И", hint: "ЖИ пиши с И!" },
      { type: 'quiz', question: "Вставь букву: ЛЫЖ__", options: ["И", "О", "Э", "Е", "Ы"], correctAnswer: "И", hint: "ЖИ пиши с И!" },
      { type: 'quiz', question: "Какое слово написано правильно?", options: ["ЖЕЗНЬ", "ЖОЗНЬ", "ЖЭЗНЬ", "ЖЫЗНЬ", "ЖИЗНЬ ✨"], correctAnswer: "ЖИЗНЬ ✨", hint: "ЖИ пиши с И!" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «ЖИ-ШИ пиши с И»! 🎉" }
  },
  {
    title: "ЧА-ЩА пиши с А",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Как правильно: ТУЧ__?", options: ["ТУЧЕ ☁️", "ТУЧА ☁️", "ТУЧО ☁️", "ТУЧИ ☁️", "ТУЧЯ ☁️"], correctAnswer: "ТУЧА ☁️", hint: "ЧА-ЩА пиши с А!" },
      { type: 'quiz', question: "Вставь букву: ЗАДАЧ__", options: ["Я", "О", "А", "Е", "И"], correctAnswer: "А", hint: "ЧА пиши с А!" },
      { type: 'quiz', question: "Какое слово написано правильно?", options: ["ЧАЩА 🌲", "ЧЕЩА", "ЧОЩА", "ЧЯЩА", "ЧИЩА"], correctAnswer: "ЧАЩА 🌲", hint: "ЧА-ЩА пиши с А!" },
      { type: 'quiz', question: "Вставь букву: РОЩ__", options: ["О", "А", "Я", "И", "Е"], correctAnswer: "А", hint: "ЩА пиши с А!" },
      { type: 'quiz', question: "Как правильно: ДАЧ__?", options: ["ДАЧА 🏡", "ДАЧО", "ДАЧЕ", "ДАЧЯ", "ДАЧИ"], correctAnswer: "ДАЧА 🏡", hint: "ЧА пиши с А!" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «ЧА-ЩА пиши с А»! 🎉" }
  },
  {
    title: "Большая буква",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "С какой буквы начинаются имена?", options: ["С запятой", "С маленькой", "С цифры", "С большой", "С точки"], correctAnswer: "С большой", hint: "Имена пишутся с большой буквы!" },
      { type: 'quiz', question: "Как написать название города?", options: ["москва", "МосКва", "мОсква", "Москва", "МОСКВА"], correctAnswer: "Москва", hint: "Города — с большой буквы" },
      { type: 'quiz', question: "Что пишется с большой буквы?", options: ["красивый", "дом", "стол", "бежать", "Александр"], correctAnswer: "Александр", hint: "Имена с большой буквы!" },
      { type: 'quiz', question: "Какое слово — имя?", options: ["книга", "стол", "красный", "Маша", "бежать"], correctAnswer: "Маша", hint: "Имена пишутся с большой буквы" },
      { type: 'quiz', question: "Название реки пишется:", options: ["С большой буквы", "Как угодно", "Прописными", "Не важно", "С маленькой"], correctAnswer: "С большой буквы", hint: "Названия рек — с большой буквы" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Большая буква»! 🎉" }
  },
  {
    title: "Счёт до 5",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Сколько яблок? 🍎🍎🍎", options: ["4", "1", "5", "3", "2"], correctAnswer: "3", hint: "Посчитай: раз, два, три!" },
      { type: 'quiz', question: "Сколько шариков? 🎈🎈", options: ["2", "4", "1", "3", "5"], correctAnswer: "2", hint: "Один, два!" },
      { type: 'quiz', question: "Какое число идёт после 4?", options: ["7", "6", "3", "5", "2"], correctAnswer: "5", hint: "1, 2, 3, 4, ..." },
      { type: 'quiz', question: "Сколько звёзд? ⭐⭐⭐⭐", options: ["2", "3", "4", "5", "6"], correctAnswer: "4", hint: "Посчитай: раз, два, три, четыре!" },
      { type: 'quiz', question: "Сколько котят? 🐱🐱🐱🐱🐱", options: ["2", "3", "4", "5", "6"], correctAnswer: "5", hint: "Посчитай всех котят!" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Счёт до 5»! 🎉" }
  },
  {
    title: "Счёт до 10",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Сколько пальцев на двух руках?", options: ["8", "10", "5", "9", "11"], correctAnswer: "10", hint: "5 на одной и 5 на другой" },
      { type: 'quiz', question: "Какое число идёт после 7?", options: ["8", "10", "6", "9", "7"], correctAnswer: "8", hint: "1, 2, 3, 4, 5, 6, 7, ..." },
      { type: 'quiz', question: "Какое число перед 5?", options: ["6", "4", "7", "3", "2"], correctAnswer: "4", hint: "Посчитай назад: 5, ..." },
      { type: 'quiz', question: "Какое число между 4 и 6?", options: ["5", "6", "4", "7", "3"], correctAnswer: "5", hint: "4, ?, 6" },
      { type: 'quiz', question: "Какое число идёт после 9?", options: ["11", "8", "7", "12", "10"], correctAnswer: "10", hint: "1, 2, 3, 4, 5, 6, 7, 8, 9, ..." }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Счёт до 10»! 🎉" }
  },
  {
    title: "Сложение до 10",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "2 + 3 = ?", options: ["5", "4", "7", "3", "6"], correctAnswer: "5", hint: "Два плюс три..." },
      { type: 'quiz', question: "4 + 2 = ?", options: ["7", "8", "4", "5", "6"], correctAnswer: "6", hint: "Четыре и два вместе" },
      { type: 'quiz', question: "5 + 5 = ?", options: ["10", "12", "9", "8", "11"], correctAnswer: "10", hint: "Это все пальцы на руках!" },
      { type: 'quiz', question: "1 + 1 = ?", options: ["3", "2", "0", "1", "4"], correctAnswer: "2", hint: "Один плюс один..." },
      { type: 'quiz', question: "3 + 4 = ?", options: ["5", "6", "7", "9", "8"], correctAnswer: "7", hint: "Три плюс четыре..." }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Сложение до 10»! 🎉" }
  },
  {
    title: "Вычитание",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "5 - 2 = ?", options: ["4", "5", "1", "3", "2"], correctAnswer: "3", hint: "Пять минус два..." },
      { type: 'quiz', question: "7 - 3 = ?", options: ["6", "5", "2", "3", "4"], correctAnswer: "4", hint: "Семь убери три" },
      { type: 'quiz', question: "8 - 0 = ?", options: ["9", "8", "6", "7", "0"], correctAnswer: "8", hint: "Если ничего не отнять..." },
      { type: 'quiz', question: "10 - 5 = ?", options: ["7", "6", "4", "5", "3"], correctAnswer: "5", hint: "Десять минус пять..." },
      { type: 'quiz', question: "6 - 6 = ?", options: ["6", "12", "2", "1", "0"], correctAnswer: "0", hint: "Отнять само себя = 0" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Вычитание»! 🎉" }
  },
  {
    title: "Сравнение",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Что больше: 3 или 5?", options: ["5", "2", "6", "3", "Одинаково"], correctAnswer: "5", hint: "5 идёт позже при счёте" },
      { type: 'quiz', question: "Что меньше: 2 или 4?", options: ["Одинаково", "2", "3", "1", "4"], correctAnswer: "2", hint: "2 идёт раньше при счёте" },
      { type: 'quiz', question: "3 и 3 — это...", options: ["Одинаково", "3 меньше", "2 больше", "4 больше", "3 больше"], correctAnswer: "Одинаково", hint: "Числа равны" },
      { type: 'quiz', question: "Что больше: 7 или 5?", options: ["6", "Одинаково", "5", "7", "8"], correctAnswer: "7", hint: "7 идёт позже" },
      { type: 'quiz', question: "Что меньше: 1 или 3?", options: ["3", "1", "0", "2", "Одинаково"], correctAnswer: "1", hint: "1 идёт раньше" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Сравнение»! 🎉" }
  },
  {
    title: "Звуки речи",
    subject: "Развитие речи",
    icon: "MessageCircle",
    color: "text-teal-400",
    tasks: [
      { type: 'quiz', question: "С какого звука начинается слово МАМА?", options: ["А", "И", "М", "У", "О"], correctAnswer: "М", hint: "[М]ама" },
      { type: 'quiz', question: "Сколько звуков в слове ДОМ?", options: ["3", "1", "4", "5", "2"], correctAnswer: "3", hint: "Д-О-М" },
      { type: 'quiz', question: "Какой звук последний в слове КОТ?", options: ["О", "А", "Т", "К", "И"], correctAnswer: "Т", hint: "Ко-[Т]" },
      { type: 'quiz', question: "Буква А — это:", options: ["Согласная 🔵", "Знак", "Гласная 🔴", "Мягкий знак", "Цифра"], correctAnswer: "Гласная 🔴", hint: "А поётся свободно" },
      { type: 'quiz', question: "Сколько звуков в слове ШАР?", options: ["3", "5", "4", "1", "2"], correctAnswer: "3", hint: "Ш-А-Р" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Звуки речи»! 🎉" }
  },
  {
    title: "Животные",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какое животное говорит «Му»?", options: ["Лиса 🦊", "Птица 🐦", "Собака 🐕", "Корова 🐄", "Кошка 🐱"], correctAnswer: "Корова 🐄", hint: "Большое животное на ферме" },
      { type: 'quiz', question: "Кто умеет летать?", options: ["Собака 🐕", "Птица 🐦", "Рыба 🐟", "Змея 🐍", "Кот 🐱"], correctAnswer: "Птица 🐦", hint: "У кого есть крылья?" },
      { type: 'quiz', question: "Где живёт рыба?", options: ["На дереве 🌳", "В гнезде 🪺", "В норе 🕳️", "В доме 🏠", "В воде 🌊"], correctAnswer: "В воде 🌊", hint: "Рыба плавает" },
      { type: 'quiz', question: "Корова — какое животное?", options: ["Пустынное", "Дикое", "Домашнее", "Морское", "Лесное"], correctAnswer: "Домашнее", hint: "Живёт с людьми на ферме" },
      { type: 'quiz', question: "Кто живёт в дупле?", options: ["Волк 🐺", "Рыба 🐟", "Муравей 🐜", "Заяц 🐰", "Белка 🐿️"], correctAnswer: "Белка 🐿️", hint: "На дереве" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Животные»! 🎉" }
  },
  {
    title: "Времена года",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какое время года самое тёплое?", options: ["Зима ❄️", "Все одинаково", "Весна 🌸", "Лето ☀️", "Осень 🍂"], correctAnswer: "Лето ☀️", hint: "Можно купаться!" },
      { type: 'quiz', question: "Когда падает снег?", options: ["Летом ☀️", "Весной 🌸", "Всегда", "Зимой ❄️", "Осенью 🍂"], correctAnswer: "Зимой ❄️", hint: "Холодно, можно кататься на санках" },
      { type: 'quiz', question: "Сколько времён года?", options: ["2", "6", "3", "4", "5"], correctAnswer: "4", hint: "Зима, весна, лето, осень" },
      { type: 'quiz', question: "Что бывает весной?", options: ["Листопад 🍂", "Цветы 🌷", "Жара 🔥", "Снег ❄️", "Мороз 🥶"], correctAnswer: "Цветы 🌷", hint: "Весной всё расцветает" },
      { type: 'quiz', question: "После весны наступает:", options: ["Весна 🌸", "Осень 🍂", "Зима ❄️", "Лето ☀️", "Снова весна"], correctAnswer: "Лето ☀️", hint: "Весна, потом лето" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Времена года»! 🎉" }
  },
  {
    title: "Растения",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Что нужно растению для роста?", options: ["Мороженое 🍦", "Только камни 🪨", "Конфеты 🍬", "Вода и свет 💧☀️", "Мяч ⚽"], correctAnswer: "Вода и свет 💧☀️", hint: "Растения пьют и любят солнышко" },
      { type: 'quiz', question: "Какого цвета листья летом?", options: ["Жёлтого", "Белого", "Зелёного", "Красного", "Синего"], correctAnswer: "Зелёного", hint: "Вспомни деревья летом" },
      { type: 'quiz', question: "Что вырастает из семечка?", options: ["Растение 🌱", "Облако ☁️", "Камень 🪨", "Машина 🚗", "Звезда ⭐"], correctAnswer: "Растение 🌱", hint: "Семя — начало растения" },
      { type: 'quiz', question: "Где растут овощи?", options: ["В огороде 🥕", "В космосе 🚀", "В море 🌊", "На луне 🌙", "В холодильнике 🧊"], correctAnswer: "В огороде 🥕", hint: "На грядках" },
      { type: 'quiz', question: "Корень растения:", options: ["Привлекает насекомых", "Делает фотосинтез", "Всасывает воду", "Растёт вверх", "Производит семена"], correctAnswer: "Всасывает воду", hint: "Из почвы" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Растения»! 🎉" }
  },
  {
    title: "Цвета",
    subject: "ИЗО",
    icon: "Palette",
    color: "text-rose-400",
    tasks: [
      { type: 'quiz', question: "Какого цвета солнце? ☀️", options: ["Зелёное", "Красное", "Жёлтое", "Синее", "Фиолетовое"], correctAnswer: "Жёлтое", hint: "Солнце яркое и тёплое" },
      { type: 'quiz', question: "Смешай жёлтый и синий:", options: ["Оранжевый", "Зелёный", "Коричневый", "Фиолетовый", "Красный"], correctAnswer: "Зелёный", hint: "Жёлтый + синий = зелёный" },
      { type: 'quiz', question: "Какого цвета трава? 🌿", options: ["Белая", "Красная", "Зелёная", "Синяя", "Жёлтая"], correctAnswer: "Зелёная", hint: "Трава зелёная" },
      { type: 'quiz', question: "Красный + жёлтый =", options: ["Зелёный", "Фиолетовый", "Оранжевый", "Коричневый", "Синий"], correctAnswer: "Оранжевый", hint: "Тёплый цвет" },
      { type: 'quiz', question: "Красный + синий =", options: ["Оранжевый", "Коричневый", "Жёлтый", "Фиолетовый", "Зелёный"], correctAnswer: "Фиолетовый", hint: "Холодный цвет" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Цвета»! 🎉" }
  },
  {
    title: "Музыкальные инструменты",
    subject: "Музыка",
    icon: "Music",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Какой инструмент бьют палочками?", options: ["Флейта 🎶", "Скрипка 🎻", "Пианино 🎹", "Гитара 🎸", "Барабан 🥁"], correctAnswer: "Барабан 🥁", hint: "Бум-бум-бум!" },
      { type: 'quiz', question: "Сколько нот в музыке?", options: ["6", "8", "12", "5", "7"], correctAnswer: "7", hint: "До, ре, ми, фа, соль, ля, си" },
      { type: 'quiz', question: "Чёрно-белый инструмент:", options: ["Пианино 🎹", "Скрипка 🎻", "Барабан 🥁", "Труба 🎺", "Гитара 🎸"], correctAnswer: "Пианино 🎹", hint: "Клавиши чёрные и белые" },
      { type: 'quiz', question: "У какого инструмента струны?", options: ["Труба 🎺", "Гитара 🎸", "Флейта 🎶", "Барабан 🥁", "Бубен"], correctAnswer: "Гитара 🎸", hint: "Дзинь-дзинь!" },
      { type: 'quiz', question: "Дирижёр руководит:", options: ["Кинотеатром", "Театром", "Хором", "Цирком", "Оркестром"], correctAnswer: "Оркестром", hint: "Дирижёр — руководитель" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Музыкальные инструменты»! 🎉" }
  },
  {
    title: "Спорт",
    subject: "Физкультура",
    icon: "Dumbbell",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Футбол играют:", options: ["Клюшкой", "Ракеткой", "Без мяча", "Ногами и мячом ⚽", "Руками"], correctAnswer: "Ногами и мячом ⚽", hint: "Футбол — ногами!" },
      { type: 'quiz', question: "Сколько игроков в команде по футболу?", options: ["6", "7", "11", "9", "5"], correctAnswer: "11", hint: "11 на поле" },
      { type: 'quiz', question: "Что полезно для здоровья?", options: ["Зарядка", "Мало двигаться", "Есть конфеты", "Сидеть весь день", "Не спать"], correctAnswer: "Зарядка", hint: "Движение — жизнь!" },
      { type: 'quiz', question: "Баскетбол играют:", options: ["Без мяча", "Ракеткой", "Клюшкой", "Ногами", "Руками и мячом 🏀"], correctAnswer: "Руками и мячом 🏀", hint: "Забрасываем в кольцо" },
      { type: 'quiz', question: "Сколько раз в неделю нужно заниматься спортом?", options: ["1", "3-4", "0", "7", "2"], correctAnswer: "3-4", hint: "Регулярность важна" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Спорт»! 🎉" }
  },
  {
    title: "Лепка",
    subject: "Лепка",
    icon: "Circle",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Из чего лепят фигурки?", options: ["Камень", "Металл", "Дерево", "Бумага", "Пластилин"], correctAnswer: "Пластилин", hint: "Мягкий и цветной" },
      { type: 'quiz', question: "Что нужно для лепки?", options: ["Пила", "Гвозди", "Молоток", "Руки и пластилин", "Ножницы"], correctAnswer: "Руки и пластилин", hint: "Лепим руками" },
      { type: 'quiz', question: "Какую форму легче всего слепить?", options: ["Пирамиду", "Шар", "Квадрат", "Треугольник", "Куб"], correctAnswer: "Шар", hint: "Круглая форма — самая простая" },
      { type: 'quiz', question: "Пластилин бывает:", options: ["Только чёрный", "Разных цветов", "Прозрачный", "Только серый", "Только белый"], correctAnswer: "Разных цветов", hint: "Много цветов" },
      { type: 'quiz', question: "Перед лепкой нужно:", options: ["Охладить", "Сжечь", "Разбить", "Порезать", "Размять пластилин"], correctAnswer: "Размять пластилин", hint: "Размягчить руками" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Лепка»! 🎉" }
  },
]
