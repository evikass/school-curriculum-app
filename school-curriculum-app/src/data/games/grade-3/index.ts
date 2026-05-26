// Экспорт игр для 3 класса
import { GameLesson } from '../types'

export const thirdGradeGames: GameLesson[] = [
  {
    title: "Части речи",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Имя существительное обозначает:", options: ["Действие", "Признак", "Предмет", "Количество", "Место"], correctAnswer: "Предмет", hint: "Существительное = предмет" },
      { type: 'quiz', question: "Глагол обозначает:", options: ["Предмет", "Признак", "Место", "Количество", "Действие"], correctAnswer: "Действие", hint: "Глагол = действие" },
      { type: 'quiz', question: "Имя прилагательное обозначает:", options: ["Признак предмета", "Действие", "Место", "Предмет", "Количество"], correctAnswer: "Признак предмета", hint: "Прилагательное = признак" },
      { type: 'quiz', question: "На какой вопрос отвечает существительное?", options: ["Какой?", "Кто? Что?", "Что делать?", "Где?", "Сколько?"], correctAnswer: "Кто? Что?", hint: "Существительное — кто? что?" },
      { type: 'quiz', question: "На какой вопрос отвечает глагол?", options: ["Какой?", "Что делать?", "Где?", "Кто? Что?", "Сколько?"], correctAnswer: "Что делать?", hint: "Глагол — что делать?" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Части речи»! 🎉" }
  },
  {
    title: "Падежи",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Сколько падежей в русском языке?", options: ["5", "7", "6", "4", "8"], correctAnswer: "6", hint: "И, Р, Д, В, Т, П" },
      { type: 'quiz', question: "Именительный падеж отвечает на вопрос:", options: ["Кто? Что?", "Кого? Чего?", "Кем? Чем?", "Кому? Чему?", "Кого? Что?"], correctAnswer: "Кто? Что?", hint: "И.п. — кто? что?" },
      { type: 'quiz', question: "Родительный падеж отвечает на вопрос:", options: ["Кем? Чем?", "Кто? Что?", "Кого? Что?", "Кому? Чему?", "Кого? Чего?"], correctAnswer: "Кого? Чего?", hint: "Р.п. — кого? чего?" },
      { type: 'quiz', question: "Дательный падеж отвечает на вопрос:", options: ["Кого? Чего?", "Кто? Что?", "Кому? Чему?", "Кого? Что?", "Кем? Чем?"], correctAnswer: "Кому? Чему?", hint: "Д.п. — кому? чему?" },
      { type: 'quiz', question: "Предложный падеж отвечает на вопрос:", options: ["О ком? О чём?", "Кого? Чего?", "Кто? Что?", "Кому? Чему?", "Кем? Чем?"], correctAnswer: "О ком? О чём?", hint: "П.п. — о ком? о чём?" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Падежи»! 🎉" }
  },
  {
    title: "Корень слова",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Корень — это:", options: ["Общая часть родственных слов", "Приставка", "Окончание", "Суффикс", "Основа"], correctAnswer: "Общая часть родственных слов", hint: "В корне — общий смысл" },
      { type: 'quiz', question: "Какое слово однокоренное слову «лес»?", options: ["Лесник", "Лисица", "Лесть", "Линейка", "Лестница"], correctAnswer: "Лесник", hint: "Лес — лесник — лесной" },
      { type: 'quiz', question: "Корень в слове «подосиновик»:", options: ["овик", "подос", "осин", "осовик", "под"], correctAnswer: "осин", hint: "Под-осин-овик" },
      { type: 'quiz', question: "Какое слово НЕ однокоренное «вода»?", options: ["Водный", "Водитель", "Водяной", "Наводнение", "Подводник"], correctAnswer: "Водитель", hint: "Водитель — от «водить»" },
      { type: 'quiz', question: "Однокоренные слова имеют общий:", options: ["Приставку", "Окончание", "Ударение", "Корень", "Суффикс"], correctAnswer: "Корень", hint: "Корень — общая часть" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Корень слова»! 🎉" }
  },
  {
    title: "Басни",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Мораль басни — это:", options: ["Описание героев", "Вступление", "Завязка", "Развязка", "Нравоучительный вывод"], correctAnswer: "Нравоучительный вывод", hint: "Главный урок басни" },
      { type: 'quiz', question: "Автор «Ворона и Лисица»:", options: ["Лермонтов", "Толстой", "Гоголь", "Пушкин", "Крылов"], correctAnswer: "Крылов", hint: "И.А. Крылов" },
      { type: 'quiz', question: "Аллегория в басне — это:", options: ["Метафора", "Сравнение", "Прямое описание", "Гипербола", "Иносказание"], correctAnswer: "Иносказание", hint: "Животные = люди" },
      { type: 'quiz', question: "Басня — это:", options: ["Роман", "Краткий рассказ с моралью", "Стихотворение", "Пьеса", "Очерк"], correctAnswer: "Краткий рассказ с моралью", hint: "Краткость + мораль" },
      { type: 'quiz', question: "Крылов написал:", options: ["«Стрекоза и Муравей»", "«Отцы и дети»", "«Руслан и Людмила»", "«Война и мир»", "«Мёртвые души»"], correctAnswer: "«Стрекоза и Муравей»", hint: "Крылов — баснописец" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Басни»! 🎉" }
  },
  {
    title: "Сказки Пушкина",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Сколько лет ждал старик золотую рыбку?", options: ["33 года", "20 лет", "35 лет", "30 лет и 3 года", "40 лет"], correctAnswer: "30 лет и 3 года", hint: "«Жил старик со своею старухой...»" },
      { type: 'quiz', question: "Кто превратился в лебедя?", options: ["Боярышня", "Повариха", "Царевна", "Ткачиха", "Царица"], correctAnswer: "Царевна", hint: "Царевна-лебедь" },
      { type: 'quiz', question: "«Сказка о рыбаке и рыбке» — автор:", options: ["Лермонтов", "Ершов", "Гоголь", "Пушкин", "Толстой"], correctAnswer: "Пушкин", hint: "А.С. Пушкин" },
      { type: 'quiz', question: "Кто тянул репку первым?", options: ["Дедка", "Мышка", "Внучка", "Бабка", "Жучка"], correctAnswer: "Дедка", hint: "«Посадил дед репку...»" },
      { type: 'quiz', question: "Золотая рыбка исполнила:", options: ["5 желаний", "10 желаний", "1 желание", "0 желаний", "3 желания (старухи)"], correctAnswer: "3 желания (старухи)", hint: "Но старуха прогневала" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Сказки Пушкина»! 🎉" }
  },
  {
    title: "Умножение",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "7 × 8 = ?", options: ["56", "63", "48", "42", "54"], correctAnswer: "56", hint: "Таблица умножения" },
      { type: 'quiz', question: "6 × 7 = ?", options: ["42", "35", "48", "49", "36"], correctAnswer: "42", hint: "Таблица умножения" },
      { type: 'quiz', question: "9 × 9 = ?", options: ["63", "90", "81", "72", "99"], correctAnswer: "81", hint: "Таблица умножения" },
      { type: 'quiz', question: "5 × 8 = ?", options: ["35", "32", "45", "48", "40"], correctAnswer: "40", hint: "Таблица умножения" },
      { type: 'quiz', question: "4 × 6 = ?", options: ["28", "30", "24", "20", "18"], correctAnswer: "24", hint: "Таблица умножения" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Умножение»! 🎉" }
  },
  {
    title: "Деление",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "72 ÷ 9 = ?", options: ["10", "8", "7", "6", "9"], correctAnswer: "8", hint: "9 × 8 = 72" },
      { type: 'quiz', question: "56 ÷ 8 = ?", options: ["6", "7", "5", "8", "9"], correctAnswer: "7", hint: "8 × 7 = 56" },
      { type: 'quiz', question: "45 ÷ 5 = ?", options: ["11", "10", "8", "7", "9"], correctAnswer: "9", hint: "5 × 9 = 45" },
      { type: 'quiz', question: "64 ÷ 8 = ?", options: ["8", "10", "7", "9", "6"], correctAnswer: "8", hint: "8 × 8 = 64" },
      { type: 'quiz', question: "36 ÷ 6 = ?", options: ["7", "6", "8", "4", "5"], correctAnswer: "6", hint: "6 × 6 = 36" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Деление»! 🎉" }
  },
  {
    title: "Дроби",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "1/2 от 100 = ?", options: ["50", "20", "75", "10", "25"], correctAnswer: "50", hint: "Половина от 100" },
      { type: 'quiz', question: "1/4 от 200 = ?", options: ["50", "25", "100", "75", "40"], correctAnswer: "50", hint: "Четверть от 200" },
      { type: 'quiz', question: "Сократи дробь: 6/8", options: ["1/2", "4/6", "2/3", "3/5", "3/4"], correctAnswer: "3/4", hint: "Раздели на 2" },
      { type: 'quiz', question: "2/5 + 1/5 = ?", options: ["4/5", "1/5", "2/5", "3/5", "3/10"], correctAnswer: "3/5", hint: "Сложи числители" },
      { type: 'quiz', question: "Какая дробь больше: 2/3 или 1/2?", options: ["2/3", "Нельзя сравнить", "1/3", "1/2", "Они равны"], correctAnswer: "2/3", hint: "2/3 = 4/6, 1/2 = 3/6" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Дроби»! 🎉" }
  },
  {
    title: "Площадь и периметр",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Периметр квадрата со стороной 5:", options: ["20", "15", "25", "30", "10"], correctAnswer: "20", hint: "P = 4 × 5 = 20" },
      { type: 'quiz', question: "Площадь прямоугольника 3 × 4:", options: ["24", "10", "14", "12", "7"], correctAnswer: "12", hint: "S = 3 × 4 = 12" },
      { type: 'quiz', question: "Периметр прямоугольника 2 × 3:", options: ["12", "5", "10", "8", "6"], correctAnswer: "10", hint: "P = 2(2 + 3) = 10" },
      { type: 'quiz', question: "Площадь квадрата со стороной 6:", options: ["30", "24", "42", "36", "12"], correctAnswer: "36", hint: "S = 6² = 36" },
      { type: 'quiz', question: "Периметр квадрата со стороной 4:", options: ["24", "12", "16", "8", "20"], correctAnswer: "16", hint: "P = 4 × 4 = 16" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Площадь и периметр»! 🎉" }
  },
  {
    title: "Животные",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какое животное говорит «Му»?", options: ["Корова 🐄", "Кошка 🐱", "Лиса 🦊", "Собака 🐕", "Птица 🐦"], correctAnswer: "Корова 🐄", hint: "Большое животное на ферме" },
      { type: 'quiz', question: "Кто умеет летать?", options: ["Птица 🐦", "Кот 🐱", "Собака 🐕", "Змея 🐍", "Рыба 🐟"], correctAnswer: "Птица 🐦", hint: "У кого есть крылья?" },
      { type: 'quiz', question: "Где живёт рыба?", options: ["В доме 🏠", "На дереве 🌳", "В гнезде 🪺", "В воде 🌊", "В норе 🕳️"], correctAnswer: "В воде 🌊", hint: "Рыба плавает" },
      { type: 'quiz', question: "Корова — какое животное?", options: ["Домашнее", "Лесное", "Морское", "Пустынное", "Дикое"], correctAnswer: "Домашнее", hint: "Живёт с людьми на ферме" },
      { type: 'quiz', question: "Кто живёт в дупле?", options: ["Заяц 🐰", "Волк 🐺", "Белка 🐿️", "Рыба 🐟", "Муравей 🐜"], correctAnswer: "Белка 🐿️", hint: "На дереве" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Животные»! 🎉" }
  },
  {
    title: "Времена года",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какое время года самое тёплое?", options: ["Зима ❄️", "Все одинаково", "Осень 🍂", "Весна 🌸", "Лето ☀️"], correctAnswer: "Лето ☀️", hint: "Можно купаться!" },
      { type: 'quiz', question: "Когда падает снег?", options: ["Зимой ❄️", "Летом ☀️", "Всегда", "Весной 🌸", "Осенью 🍂"], correctAnswer: "Зимой ❄️", hint: "Холодно, можно кататься на санках" },
      { type: 'quiz', question: "Сколько времён года?", options: ["4", "2", "3", "5", "6"], correctAnswer: "4", hint: "Зима, весна, лето, осень" },
      { type: 'quiz', question: "Что бывает весной?", options: ["Жара 🔥", "Мороз 🥶", "Листопад 🍂", "Снег ❄️", "Цветы 🌷"], correctAnswer: "Цветы 🌷", hint: "Весной всё расцветает" },
      { type: 'quiz', question: "После весны наступает:", options: ["Зима ❄️", "Лето ☀️", "Весна 🌸", "Осень 🍂", "Снова весна"], correctAnswer: "Лето ☀️", hint: "Весна, потом лето" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Времена года»! 🎉" }
  },
  {
    title: "Растения",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Что нужно растению для роста?", options: ["Мяч ⚽", "Конфеты 🍬", "Мороженое 🍦", "Только камни 🪨", "Вода и свет 💧☀️"], correctAnswer: "Вода и свет 💧☀️", hint: "Растения пьют и любят солнышко" },
      { type: 'quiz', question: "Какого цвета листья летом?", options: ["Красного", "Синего", "Белого", "Зелёного", "Жёлтого"], correctAnswer: "Зелёного", hint: "Вспомни деревья летом" },
      { type: 'quiz', question: "Что вырастает из семечка?", options: ["Звезда ⭐", "Машина 🚗", "Камень 🪨", "Облако ☁️", "Растение 🌱"], correctAnswer: "Растение 🌱", hint: "Семя — начало растения" },
      { type: 'quiz', question: "Где растут овощи?", options: ["На луне 🌙", "В холодильнике 🧊", "В космосе 🚀", "В море 🌊", "В огороде 🥕"], correctAnswer: "В огороде 🥕", hint: "На грядках" },
      { type: 'quiz', question: "Корень растения:", options: ["Всасывает воду", "Привлекает насекомых", "Делает фотосинтез", "Растёт вверх", "Производит семена"], correctAnswer: "Всасывает воду", hint: "Из почвы" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Растения»! 🎉" }
  },
  {
    title: "Present Simple",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I ___ a student.", options: ["are", "am", "be", "is", "was"], correctAnswer: "am", hint: "I am — единственное число" },
      { type: 'quiz', question: "She ___ to school every day.", options: ["going", "goes", "go", "went", "gone"], correctAnswer: "goes", hint: "She + V-s/es" },
      { type: 'quiz', question: "They ___ English.", options: ["speak", "spoken", "spoke", "speaks", "speaking"], correctAnswer: "speak", hint: "They + V (без s)" },
      { type: 'quiz', question: "He ___ like pizza.", options: ["aren't", "wasn't", "doesn't", "isn't", "don't"], correctAnswer: "doesn't", hint: "He + doesn't" },
      { type: 'quiz', question: "___ you like ice cream?", options: ["Are", "Does", "Do", "Is", "Was"], correctAnswer: "Do", hint: "You + Do" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Present Simple»! 🎉" }
  },
  {
    title: "Past Simple",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Yesterday I ___ to school.", options: ["gone", "going", "went", "go", "goed"], correctAnswer: "went", hint: "Go — went (неправильный)" },
      { type: 'quiz', question: "She ___ (play) football yesterday.", options: ["playing", "plaied", "plays", "play", "played"], correctAnswer: "played", hint: "Правильный + -ed" },
      { type: 'quiz', question: "I ___ (see) him yesterday.", options: ["seed", "see", "seeing", "seen", "saw"], correctAnswer: "saw", hint: "See — saw — seen" },
      { type: 'quiz', question: "___ you watch TV yesterday?", options: ["Are", "Does", "Did", "Do", "Were"], correctAnswer: "Did", hint: "Did для прошедшего" },
      { type: 'quiz', question: "He ___ (come) home late.", options: ["come", "coming", "came", "comed", "comes"], correctAnswer: "came", hint: "Come — came — come" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Past Simple»! 🎉" }
  },
  {
    title: "Технология",
    subject: "Технология",
    icon: "Ruler",
    color: "text-yellow-400",
    tasks: [
      { type: 'quiz', question: "Бумага — материал из:", options: ["Металла", "Стекла", "Резины", "Древесины", "Пластика"], correctAnswer: "Древесины", hint: "Целлюлоза из дерева" },
      { type: 'quiz', question: "Ножницы — инструмент для:", options: ["Шитья", "Лепки", "Резания", "Рисования", "Клея"], correctAnswer: "Резания", hint: "Режут бумагу" },
      { type: 'quiz', question: "Клей нужен для:", options: ["Рисования", "Лепки", "Измерения", "Резания", "Соединения деталей"], correctAnswer: "Соединения деталей", hint: "Склеиваем части" },
      { type: 'quiz', question: "Какой инструмент измеряет длину?", options: ["Молоток", "Карандаш", "Линейка", "Кисть", "Ножницы"], correctAnswer: "Линейка", hint: "В сантиметрах" },
      { type: 'quiz', question: "Оригами — это:", options: ["Шитьё", "Лепка", "Вязание", "Искусство складывания бумаги", "Рисование"], correctAnswer: "Искусство складывания бумаги", hint: "Японское искусство" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Технология»! 🎉" }
  },
  {
    title: "Цвета",
    subject: "ИЗО",
    icon: "Palette",
    color: "text-rose-400",
    tasks: [
      { type: 'quiz', question: "Какого цвета солнце? ☀️", options: ["Синее", "Красное", "Зелёное", "Жёлтое", "Фиолетовое"], correctAnswer: "Жёлтое", hint: "Солнце яркое и тёплое" },
      { type: 'quiz', question: "Смешай жёлтый и синий:", options: ["Фиолетовый", "Зелёный", "Оранжевый", "Коричневый", "Красный"], correctAnswer: "Зелёный", hint: "Жёлтый + синий = зелёный" },
      { type: 'quiz', question: "Какого цвета трава? 🌿", options: ["Белая", "Зелёная", "Синяя", "Красная", "Жёлтая"], correctAnswer: "Зелёная", hint: "Трава зелёная" },
      { type: 'quiz', question: "Красный + жёлтый =", options: ["Синий", "Оранжевый", "Зелёный", "Фиолетовый", "Коричневый"], correctAnswer: "Оранжевый", hint: "Тёплый цвет" },
      { type: 'quiz', question: "Красный + синий =", options: ["Коричневый", "Оранжевый", "Зелёный", "Жёлтый", "Фиолетовый"], correctAnswer: "Фиолетовый", hint: "Холодный цвет" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Цвета»! 🎉" }
  },
  {
    title: "Музыкальные инструменты",
    subject: "Музыка",
    icon: "Music",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Какой инструмент бьют палочками?", options: ["Гитара 🎸", "Скрипка 🎻", "Флейта 🎶", "Пианино 🎹", "Барабан 🥁"], correctAnswer: "Барабан 🥁", hint: "Бум-бум-бум!" },
      { type: 'quiz', question: "Сколько нот в музыке?", options: ["6", "8", "5", "12", "7"], correctAnswer: "7", hint: "До, ре, ми, фа, соль, ля, си" },
      { type: 'quiz', question: "Чёрно-белый инструмент:", options: ["Гитара 🎸", "Труба 🎺", "Скрипка 🎻", "Барабан 🥁", "Пианино 🎹"], correctAnswer: "Пианино 🎹", hint: "Клавиши чёрные и белые" },
      { type: 'quiz', question: "У какого инструмента струны?", options: ["Гитара 🎸", "Бубен", "Барабан 🥁", "Флейта 🎶", "Труба 🎺"], correctAnswer: "Гитара 🎸", hint: "Дзинь-дзинь!" },
      { type: 'quiz', question: "Дирижёр руководит:", options: ["Хором", "Кинотеатром", "Театром", "Цирком", "Оркестром"], correctAnswer: "Оркестром", hint: "Дирижёр — руководитель" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Музыкальные инструменты»! 🎉" }
  },
  {
    title: "Спорт",
    subject: "Физкультура",
    icon: "Dumbbell",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Футбол играют:", options: ["Ракеткой", "Руками", "Ногами и мячом ⚽", "Без мяча", "Клюшкой"], correctAnswer: "Ногами и мячом ⚽", hint: "Футбол — ногами!" },
      { type: 'quiz', question: "Сколько игроков в команде по футболу?", options: ["11", "6", "5", "9", "7"], correctAnswer: "11", hint: "11 на поле" },
      { type: 'quiz', question: "Что полезно для здоровья?", options: ["Мало двигаться", "Не спать", "Сидеть весь день", "Есть конфеты", "Зарядка"], correctAnswer: "Зарядка", hint: "Движение — жизнь!" },
      { type: 'quiz', question: "Баскетбол играют:", options: ["Клюшкой", "Ногами", "Руками и мячом 🏀", "Без мяча", "Ракеткой"], correctAnswer: "Руками и мячом 🏀", hint: "Забрасываем в кольцо" },
      { type: 'quiz', question: "Сколько раз в неделю нужно заниматься спортом?", options: ["1", "7", "0", "2", "3-4"], correctAnswer: "3-4", hint: "Регулярность важна" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Спорт»! 🎉" }
  },
]
