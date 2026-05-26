// Экспорт игр для 4 класса
import { GameLesson } from '../types'

export const fourthGradeGames: GameLesson[] = [
  {
    title: "Части речи",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Имя существительное обозначает:", options: ["Место", "Действие", "Признак", "Предмет", "Количество"], correctAnswer: "Предмет", hint: "Существительное = предмет" },
      { type: 'quiz', question: "Глагол обозначает:", options: ["Количество", "Место", "Признак", "Действие", "Предмет"], correctAnswer: "Действие", hint: "Глагол = действие" },
      { type: 'quiz', question: "Имя прилагательное обозначает:", options: ["Место", "Предмет", "Действие", "Количество", "Признак предмета"], correctAnswer: "Признак предмета", hint: "Прилагательное = признак" },
      { type: 'quiz', question: "На какой вопрос отвечает существительное?", options: ["Где?", "Что делать?", "Сколько?", "Какой?", "Кто? Что?"], correctAnswer: "Кто? Что?", hint: "Существительное — кто? что?" },
      { type: 'quiz', question: "На какой вопрос отвечает глагол?", options: ["Кто? Что?", "Сколько?", "Где?", "Что делать?", "Какой?"], correctAnswer: "Что делать?", hint: "Глагол — что делать?" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Части речи»! 🎉" }
  },
  {
    title: "Падежи",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Сколько падежей в русском языке?", options: ["8", "5", "6", "7", "4"], correctAnswer: "6", hint: "И, Р, Д, В, Т, П" },
      { type: 'quiz', question: "Именительный падеж отвечает на вопрос:", options: ["Кого? Что?", "Кого? Чего?", "Кто? Что?", "Кем? Чем?", "Кому? Чему?"], correctAnswer: "Кто? Что?", hint: "И.п. — кто? что?" },
      { type: 'quiz', question: "Родительный падеж отвечает на вопрос:", options: ["Кому? Чему?", "Кого? Чего?", "Кого? Что?", "Кто? Что?", "Кем? Чем?"], correctAnswer: "Кого? Чего?", hint: "Р.п. — кого? чего?" },
      { type: 'quiz', question: "Дательный падеж отвечает на вопрос:", options: ["Кто? Что?", "Кого? Что?", "Кому? Чему?", "Кого? Чего?", "Кем? Чем?"], correctAnswer: "Кому? Чему?", hint: "Д.п. — кому? чему?" },
      { type: 'quiz', question: "Предложный падеж отвечает на вопрос:", options: ["О ком? О чём?", "Кому? Чему?", "Кто? Что?", "Кем? Чем?", "Кого? Чего?"], correctAnswer: "О ком? О чём?", hint: "П.п. — о ком? о чём?" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Падежи»! 🎉" }
  },
  {
    title: "Корень слова",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Корень — это:", options: ["Приставка", "Суффикс", "Основа", "Окончание", "Общая часть родственных слов"], correctAnswer: "Общая часть родственных слов", hint: "В корне — общий смысл" },
      { type: 'quiz', question: "Какое слово однокоренное слову «лес»?", options: ["Лисица", "Линейка", "Лесть", "Лестница", "Лесник"], correctAnswer: "Лесник", hint: "Лес — лесник — лесной" },
      { type: 'quiz', question: "Корень в слове «подосиновик»:", options: ["подос", "овик", "осовик", "под", "осин"], correctAnswer: "осин", hint: "Под-осин-овик" },
      { type: 'quiz', question: "Какое слово НЕ однокоренное «вода»?", options: ["Наводнение", "Водяной", "Водитель", "Водный", "Подводник"], correctAnswer: "Водитель", hint: "Водитель — от «водить»" },
      { type: 'quiz', question: "Однокоренные слова имеют общий:", options: ["Окончание", "Корень", "Суффикс", "Ударение", "Приставку"], correctAnswer: "Корень", hint: "Корень — общая часть" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Корень слова»! 🎉" }
  },
  {
    title: "Басни",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Мораль басни — это:", options: ["Развязка", "Описание героев", "Завязка", "Вступление", "Нравоучительный вывод"], correctAnswer: "Нравоучительный вывод", hint: "Главный урок басни" },
      { type: 'quiz', question: "Автор «Ворона и Лисица»:", options: ["Толстой", "Гоголь", "Пушкин", "Лермонтов", "Крылов"], correctAnswer: "Крылов", hint: "И.А. Крылов" },
      { type: 'quiz', question: "Аллегория в басне — это:", options: ["Иносказание", "Сравнение", "Прямое описание", "Метафора", "Гипербола"], correctAnswer: "Иносказание", hint: "Животные = люди" },
      { type: 'quiz', question: "Басня — это:", options: ["Пьеса", "Стихотворение", "Очерк", "Краткий рассказ с моралью", "Роман"], correctAnswer: "Краткий рассказ с моралью", hint: "Краткость + мораль" },
      { type: 'quiz', question: "Крылов написал:", options: ["«Отцы и дети»", "«Руслан и Людмила»", "«Война и мир»", "«Мёртвые души»", "«Стрекоза и Муравей»"], correctAnswer: "«Стрекоза и Муравей»", hint: "Крылов — баснописец" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Басни»! 🎉" }
  },
  {
    title: "Сказки Пушкина",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Сколько лет ждал старик золотую рыбку?", options: ["33 года", "20 лет", "30 лет и 3 года", "35 лет", "40 лет"], correctAnswer: "30 лет и 3 года", hint: "«Жил старик со своею старухой...»" },
      { type: 'quiz', question: "Кто превратился в лебедя?", options: ["Царица", "Ткачиха", "Боярышня", "Царевна", "Повариха"], correctAnswer: "Царевна", hint: "Царевна-лебедь" },
      { type: 'quiz', question: "«Сказка о рыбаке и рыбке» — автор:", options: ["Ершов", "Толстой", "Пушкин", "Лермонтов", "Гоголь"], correctAnswer: "Пушкин", hint: "А.С. Пушкин" },
      { type: 'quiz', question: "Кто тянул репку первым?", options: ["Бабка", "Жучка", "Дедка", "Мышка", "Внучка"], correctAnswer: "Дедка", hint: "«Посадил дед репку...»" },
      { type: 'quiz', question: "Золотая рыбка исполнила:", options: ["1 желание", "5 желаний", "3 желания (старухи)", "0 желаний", "10 желаний"], correctAnswer: "3 желания (старухи)", hint: "Но старуха прогневала" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Сказки Пушкина»! 🎉" }
  },
  {
    title: "Умножение",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "7 × 8 = ?", options: ["56", "42", "54", "48", "63"], correctAnswer: "56", hint: "Таблица умножения" },
      { type: 'quiz', question: "6 × 7 = ?", options: ["36", "49", "48", "35", "42"], correctAnswer: "42", hint: "Таблица умножения" },
      { type: 'quiz', question: "9 × 9 = ?", options: ["90", "99", "72", "81", "63"], correctAnswer: "81", hint: "Таблица умножения" },
      { type: 'quiz', question: "5 × 8 = ?", options: ["40", "35", "32", "48", "45"], correctAnswer: "40", hint: "Таблица умножения" },
      { type: 'quiz', question: "4 × 6 = ?", options: ["30", "20", "24", "28", "18"], correctAnswer: "24", hint: "Таблица умножения" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Умножение»! 🎉" }
  },
  {
    title: "Деление",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "72 ÷ 9 = ?", options: ["6", "7", "10", "9", "8"], correctAnswer: "8", hint: "9 × 8 = 72" },
      { type: 'quiz', question: "56 ÷ 8 = ?", options: ["5", "9", "6", "7", "8"], correctAnswer: "7", hint: "8 × 7 = 56" },
      { type: 'quiz', question: "45 ÷ 5 = ?", options: ["9", "11", "10", "7", "8"], correctAnswer: "9", hint: "5 × 9 = 45" },
      { type: 'quiz', question: "64 ÷ 8 = ?", options: ["6", "9", "7", "8", "10"], correctAnswer: "8", hint: "8 × 8 = 64" },
      { type: 'quiz', question: "36 ÷ 6 = ?", options: ["8", "6", "4", "5", "7"], correctAnswer: "6", hint: "6 × 6 = 36" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Деление»! 🎉" }
  },
  {
    title: "Дроби",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "1/2 от 100 = ?", options: ["25", "10", "75", "20", "50"], correctAnswer: "50", hint: "Половина от 100" },
      { type: 'quiz', question: "1/4 от 200 = ?", options: ["25", "50", "100", "40", "75"], correctAnswer: "50", hint: "Четверть от 200" },
      { type: 'quiz', question: "Сократи дробь: 6/8", options: ["1/2", "4/6", "3/5", "3/4", "2/3"], correctAnswer: "3/4", hint: "Раздели на 2" },
      { type: 'quiz', question: "2/5 + 1/5 = ?", options: ["4/5", "3/5", "2/5", "3/10", "1/5"], correctAnswer: "3/5", hint: "Сложи числители" },
      { type: 'quiz', question: "Какая дробь больше: 2/3 или 1/2?", options: ["1/3", "Нельзя сравнить", "Они равны", "1/2", "2/3"], correctAnswer: "2/3", hint: "2/3 = 4/6, 1/2 = 3/6" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Дроби»! 🎉" }
  },
  {
    title: "Площадь и периметр",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Периметр квадрата со стороной 5:", options: ["20", "10", "25", "30", "15"], correctAnswer: "20", hint: "P = 4 × 5 = 20" },
      { type: 'quiz', question: "Площадь прямоугольника 3 × 4:", options: ["24", "12", "10", "7", "14"], correctAnswer: "12", hint: "S = 3 × 4 = 12" },
      { type: 'quiz', question: "Периметр прямоугольника 2 × 3:", options: ["10", "5", "6", "12", "8"], correctAnswer: "10", hint: "P = 2(2 + 3) = 10" },
      { type: 'quiz', question: "Площадь квадрата со стороной 6:", options: ["42", "30", "12", "36", "24"], correctAnswer: "36", hint: "S = 6² = 36" },
      { type: 'quiz', question: "Периметр квадрата со стороной 4:", options: ["24", "16", "8", "20", "12"], correctAnswer: "16", hint: "P = 4 × 4 = 16" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Площадь и периметр»! 🎉" }
  },
  {
    title: "Животные",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какое животное говорит «Му»?", options: ["Лиса 🦊", "Птица 🐦", "Кошка 🐱", "Собака 🐕", "Корова 🐄"], correctAnswer: "Корова 🐄", hint: "Большое животное на ферме" },
      { type: 'quiz', question: "Кто умеет летать?", options: ["Змея 🐍", "Собака 🐕", "Рыба 🐟", "Кот 🐱", "Птица 🐦"], correctAnswer: "Птица 🐦", hint: "У кого есть крылья?" },
      { type: 'quiz', question: "Где живёт рыба?", options: ["В воде 🌊", "В норе 🕳️", "В доме 🏠", "В гнезде 🪺", "На дереве 🌳"], correctAnswer: "В воде 🌊", hint: "Рыба плавает" },
      { type: 'quiz', question: "Корова — какое животное?", options: ["Морское", "Лесное", "Домашнее", "Дикое", "Пустынное"], correctAnswer: "Домашнее", hint: "Живёт с людьми на ферме" },
      { type: 'quiz', question: "Кто живёт в дупле?", options: ["Волк 🐺", "Муравей 🐜", "Заяц 🐰", "Рыба 🐟", "Белка 🐿️"], correctAnswer: "Белка 🐿️", hint: "На дереве" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Животные»! 🎉" }
  },
  {
    title: "Времена года",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какое время года самое тёплое?", options: ["Осень 🍂", "Весна 🌸", "Лето ☀️", "Зима ❄️", "Все одинаково"], correctAnswer: "Лето ☀️", hint: "Можно купаться!" },
      { type: 'quiz', question: "Когда падает снег?", options: ["Летом ☀️", "Зимой ❄️", "Весной 🌸", "Всегда", "Осенью 🍂"], correctAnswer: "Зимой ❄️", hint: "Холодно, можно кататься на санках" },
      { type: 'quiz', question: "Сколько времён года?", options: ["4", "5", "2", "6", "3"], correctAnswer: "4", hint: "Зима, весна, лето, осень" },
      { type: 'quiz', question: "Что бывает весной?", options: ["Снег ❄️", "Цветы 🌷", "Мороз 🥶", "Жара 🔥", "Листопад 🍂"], correctAnswer: "Цветы 🌷", hint: "Весной всё расцветает" },
      { type: 'quiz', question: "После весны наступает:", options: ["Снова весна", "Весна 🌸", "Зима ❄️", "Лето ☀️", "Осень 🍂"], correctAnswer: "Лето ☀️", hint: "Весна, потом лето" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Времена года»! 🎉" }
  },
  {
    title: "Растения",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Что нужно растению для роста?", options: ["Вода и свет 💧☀️", "Мороженое 🍦", "Конфеты 🍬", "Только камни 🪨", "Мяч ⚽"], correctAnswer: "Вода и свет 💧☀️", hint: "Растения пьют и любят солнышко" },
      { type: 'quiz', question: "Какого цвета листья летом?", options: ["Синего", "Зелёного", "Жёлтого", "Красного", "Белого"], correctAnswer: "Зелёного", hint: "Вспомни деревья летом" },
      { type: 'quiz', question: "Что вырастает из семечка?", options: ["Растение 🌱", "Облако ☁️", "Звезда ⭐", "Камень 🪨", "Машина 🚗"], correctAnswer: "Растение 🌱", hint: "Семя — начало растения" },
      { type: 'quiz', question: "Где растут овощи?", options: ["В холодильнике 🧊", "В огороде 🥕", "В космосе 🚀", "В море 🌊", "На луне 🌙"], correctAnswer: "В огороде 🥕", hint: "На грядках" },
      { type: 'quiz', question: "Корень растения:", options: ["Всасывает воду", "Делает фотосинтез", "Растёт вверх", "Производит семена", "Привлекает насекомых"], correctAnswer: "Всасывает воду", hint: "Из почвы" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Растения»! 🎉" }
  },
  {
    title: "Present Simple",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I ___ a student.", options: ["be", "was", "are", "am", "is"], correctAnswer: "am", hint: "I am — единственное число" },
      { type: 'quiz', question: "She ___ to school every day.", options: ["gone", "go", "goes", "going", "went"], correctAnswer: "goes", hint: "She + V-s/es" },
      { type: 'quiz', question: "They ___ English.", options: ["spoken", "spoke", "speak", "speaks", "speaking"], correctAnswer: "speak", hint: "They + V (без s)" },
      { type: 'quiz', question: "He ___ like pizza.", options: ["wasn't", "isn't", "doesn't", "don't", "aren't"], correctAnswer: "doesn't", hint: "He + doesn't" },
      { type: 'quiz', question: "___ you like ice cream?", options: ["Is", "Are", "Was", "Do", "Does"], correctAnswer: "Do", hint: "You + Do" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Present Simple»! 🎉" }
  },
  {
    title: "Past Simple",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Yesterday I ___ to school.", options: ["going", "go", "goed", "went", "gone"], correctAnswer: "went", hint: "Go — went (неправильный)" },
      { type: 'quiz', question: "She ___ (play) football yesterday.", options: ["played", "playing", "plays", "play", "plaied"], correctAnswer: "played", hint: "Правильный + -ed" },
      { type: 'quiz', question: "I ___ (see) him yesterday.", options: ["see", "seen", "saw", "seeing", "seed"], correctAnswer: "saw", hint: "See — saw — seen" },
      { type: 'quiz', question: "___ you watch TV yesterday?", options: ["Were", "Does", "Do", "Did", "Are"], correctAnswer: "Did", hint: "Did для прошедшего" },
      { type: 'quiz', question: "He ___ (come) home late.", options: ["came", "comes", "come", "coming", "comed"], correctAnswer: "came", hint: "Come — came — come" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Past Simple»! 🎉" }
  },
  {
    title: "ОРКСЭ",
    subject: "ОРКСЭ",
    icon: "HeartHandshake",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Мораль — это:", options: ["Обычаи", "Правила доброго поведения", "Традиции", "Законы государства", "Ритуалы"], correctAnswer: "Правила доброго поведения", hint: "Нравственные правила" },
      { type: 'quiz', question: "Золотое правило морали:", options: ["Слушай старших", "Не помогай никому", "Поступай с другими так, как хочешь себе", "Делай что хочешь", "Думай только о себе"], correctAnswer: "Поступай с другими так, как хочешь себе", hint: "Относись к другим..." },
      { type: 'quiz', question: "Добро — это:", options: ["То, что приносит пользу", "То, что трудно", "То, что вредит", "То, что скучно", "То, что дорого"], correctAnswer: "То, что приносит пользу", hint: "Благо и польза" },
      { type: 'quiz', question: "Совесть — это:", options: ["Закон", "Правило", "Внутренний судья", "Традиция", "Обычай"], correctAnswer: "Внутренний судья", hint: "Голос внутри нас" },
      { type: 'quiz', question: "Семья — это:", options: ["Соседи", "Близкие люди", "Коллеги", "Незнакомцы", "Одноклассники"], correctAnswer: "Близкие люди", hint: "Самые близкие" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «ОРКСЭ»! 🎉" }
  },
  {
    title: "Технология",
    subject: "Технология",
    icon: "Ruler",
    color: "text-yellow-400",
    tasks: [
      { type: 'quiz', question: "Бумага — материал из:", options: ["Пластика", "Древесины", "Резины", "Металла", "Стекла"], correctAnswer: "Древесины", hint: "Целлюлоза из дерева" },
      { type: 'quiz', question: "Ножницы — инструмент для:", options: ["Рисования", "Лепки", "Клея", "Резания", "Шитья"], correctAnswer: "Резания", hint: "Режут бумагу" },
      { type: 'quiz', question: "Клей нужен для:", options: ["Лепки", "Соединения деталей", "Измерения", "Рисования", "Резания"], correctAnswer: "Соединения деталей", hint: "Склеиваем части" },
      { type: 'quiz', question: "Какой инструмент измеряет длину?", options: ["Кисть", "Ножницы", "Молоток", "Линейка", "Карандаш"], correctAnswer: "Линейка", hint: "В сантиметрах" },
      { type: 'quiz', question: "Оригами — это:", options: ["Шитьё", "Вязание", "Лепка", "Искусство складывания бумаги", "Рисование"], correctAnswer: "Искусство складывания бумаги", hint: "Японское искусство" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Технология»! 🎉" }
  },
  {
    title: "Цвета",
    subject: "ИЗО",
    icon: "Palette",
    color: "text-rose-400",
    tasks: [
      { type: 'quiz', question: "Какого цвета солнце? ☀️", options: ["Фиолетовое", "Синее", "Жёлтое", "Зелёное", "Красное"], correctAnswer: "Жёлтое", hint: "Солнце яркое и тёплое" },
      { type: 'quiz', question: "Смешай жёлтый и синий:", options: ["Оранжевый", "Красный", "Коричневый", "Фиолетовый", "Зелёный"], correctAnswer: "Зелёный", hint: "Жёлтый + синий = зелёный" },
      { type: 'quiz', question: "Какого цвета трава? 🌿", options: ["Жёлтая", "Красная", "Белая", "Зелёная", "Синяя"], correctAnswer: "Зелёная", hint: "Трава зелёная" },
      { type: 'quiz', question: "Красный + жёлтый =", options: ["Фиолетовый", "Синий", "Оранжевый", "Коричневый", "Зелёный"], correctAnswer: "Оранжевый", hint: "Тёплый цвет" },
      { type: 'quiz', question: "Красный + синий =", options: ["Фиолетовый", "Коричневый", "Оранжевый", "Зелёный", "Жёлтый"], correctAnswer: "Фиолетовый", hint: "Холодный цвет" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Цвета»! 🎉" }
  },
  {
    title: "Музыкальные инструменты",
    subject: "Музыка",
    icon: "Music",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Какой инструмент бьют палочками?", options: ["Скрипка 🎻", "Флейта 🎶", "Гитара 🎸", "Барабан 🥁", "Пианино 🎹"], correctAnswer: "Барабан 🥁", hint: "Бум-бум-бум!" },
      { type: 'quiz', question: "Сколько нот в музыке?", options: ["12", "8", "7", "5", "6"], correctAnswer: "7", hint: "До, ре, ми, фа, соль, ля, си" },
      { type: 'quiz', question: "Чёрно-белый инструмент:", options: ["Скрипка 🎻", "Барабан 🥁", "Гитара 🎸", "Труба 🎺", "Пианино 🎹"], correctAnswer: "Пианино 🎹", hint: "Клавиши чёрные и белые" },
      { type: 'quiz', question: "У какого инструмента струны?", options: ["Флейта 🎶", "Барабан 🥁", "Труба 🎺", "Бубен", "Гитара 🎸"], correctAnswer: "Гитара 🎸", hint: "Дзинь-дзинь!" },
      { type: 'quiz', question: "Дирижёр руководит:", options: ["Хором", "Театром", "Оркестром", "Кинотеатром", "Цирком"], correctAnswer: "Оркестром", hint: "Дирижёр — руководитель" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Музыкальные инструменты»! 🎉" }
  },
  {
    title: "Спорт",
    subject: "Физкультура",
    icon: "Dumbbell",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Футбол играют:", options: ["Руками", "Без мяча", "Ракеткой", "Ногами и мячом ⚽", "Клюшкой"], correctAnswer: "Ногами и мячом ⚽", hint: "Футбол — ногами!" },
      { type: 'quiz', question: "Сколько игроков в команде по футболу?", options: ["9", "11", "6", "7", "5"], correctAnswer: "11", hint: "11 на поле" },
      { type: 'quiz', question: "Что полезно для здоровья?", options: ["Не спать", "Сидеть весь день", "Зарядка", "Есть конфеты", "Мало двигаться"], correctAnswer: "Зарядка", hint: "Движение — жизнь!" },
      { type: 'quiz', question: "Баскетбол играют:", options: ["Клюшкой", "Без мяча", "Ракеткой", "Руками и мячом 🏀", "Ногами"], correctAnswer: "Руками и мячом 🏀", hint: "Забрасываем в кольцо" },
      { type: 'quiz', question: "Сколько раз в неделю нужно заниматься спортом?", options: ["0", "7", "1", "2", "3-4"], correctAnswer: "3-4", hint: "Регулярность важна" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Спорт»! 🎉" }
  },
]
