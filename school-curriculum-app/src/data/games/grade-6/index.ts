// Экспорт игр для 6 класса
import { GameLesson } from '../types'

export const sixthGradeGames: GameLesson[] = [
  {
    title: "Части речи",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Имя существительное обозначает:", options: ["Количество", "Признак", "Действие", "Место", "Предмет"], correctAnswer: "Предмет", hint: "Существительное = предмет" },
      { type: 'quiz', question: "Глагол обозначает:", options: ["Предмет", "Место", "Признак", "Действие", "Количество"], correctAnswer: "Действие", hint: "Глагол = действие" },
      { type: 'quiz', question: "Имя прилагательное обозначает:", options: ["Место", "Предмет", "Количество", "Действие", "Признак предмета"], correctAnswer: "Признак предмета", hint: "Прилагательное = признак" },
      { type: 'quiz', question: "На какой вопрос отвечает существительное?", options: ["Кто? Что?", "Какой?", "Где?", "Что делать?", "Сколько?"], correctAnswer: "Кто? Что?", hint: "Существительное — кто? что?" },
      { type: 'quiz', question: "На какой вопрос отвечает глагол?", options: ["Кто? Что?", "Где?", "Сколько?", "Что делать?", "Какой?"], correctAnswer: "Что делать?", hint: "Глагол — что делать?" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Части речи»! 🎉" }
  },
  {
    title: "Падежи",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Сколько падежей в русском языке?", options: ["5", "4", "7", "6", "8"], correctAnswer: "6", hint: "И, Р, Д, В, Т, П" },
      { type: 'quiz', question: "Именительный падеж отвечает на вопрос:", options: ["Кого? Что?", "Кому? Чему?", "Кем? Чем?", "Кто? Что?", "Кого? Чего?"], correctAnswer: "Кто? Что?", hint: "И.п. — кто? что?" },
      { type: 'quiz', question: "Родительный падеж отвечает на вопрос:", options: ["Кем? Чем?", "Кого? Что?", "Кого? Чего?", "Кому? Чему?", "Кто? Что?"], correctAnswer: "Кого? Чего?", hint: "Р.п. — кого? чего?" },
      { type: 'quiz', question: "Дательный падеж отвечает на вопрос:", options: ["Кого? Что?", "Кем? Чем?", "Кто? Что?", "Кому? Чему?", "Кого? Чего?"], correctAnswer: "Кому? Чему?", hint: "Д.п. — кому? чему?" },
      { type: 'quiz', question: "Предложный падеж отвечает на вопрос:", options: ["Кого? Чего?", "Кто? Что?", "О ком? О чём?", "Кем? Чем?", "Кому? Чему?"], correctAnswer: "О ком? О чём?", hint: "П.п. — о ком? о чём?" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Падежи»! 🎉" }
  },
  {
    title: "Корень слова",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Корень — это:", options: ["Основа", "Суффикс", "Общая часть родственных слов", "Окончание", "Приставка"], correctAnswer: "Общая часть родственных слов", hint: "В корне — общий смысл" },
      { type: 'quiz', question: "Какое слово однокоренное слову «лес»?", options: ["Лесник", "Линейка", "Лесть", "Лисица", "Лестница"], correctAnswer: "Лесник", hint: "Лес — лесник — лесной" },
      { type: 'quiz', question: "Корень в слове «подосиновик»:", options: ["осовик", "подос", "овик", "осин", "под"], correctAnswer: "осин", hint: "Под-осин-овик" },
      { type: 'quiz', question: "Какое слово НЕ однокоренное «вода»?", options: ["Наводнение", "Подводник", "Водитель", "Водяной", "Водный"], correctAnswer: "Водитель", hint: "Водитель — от «водить»" },
      { type: 'quiz', question: "Однокоренные слова имеют общий:", options: ["Ударение", "Окончание", "Корень", "Приставку", "Суффикс"], correctAnswer: "Корень", hint: "Корень — общая часть" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Корень слова»! 🎉" }
  },
  {
    title: "Басни",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Мораль басни — это:", options: ["Описание героев", "Развязка", "Завязка", "Вступление", "Нравоучительный вывод"], correctAnswer: "Нравоучительный вывод", hint: "Главный урок басни" },
      { type: 'quiz', question: "Автор «Ворона и Лисица»:", options: ["Толстой", "Гоголь", "Крылов", "Пушкин", "Лермонтов"], correctAnswer: "Крылов", hint: "И.А. Крылов" },
      { type: 'quiz', question: "Аллегория в басне — это:", options: ["Иносказание", "Сравнение", "Метафора", "Прямое описание", "Гипербола"], correctAnswer: "Иносказание", hint: "Животные = люди" },
      { type: 'quiz', question: "Басня — это:", options: ["Роман", "Краткий рассказ с моралью", "Пьеса", "Очерк", "Стихотворение"], correctAnswer: "Краткий рассказ с моралью", hint: "Краткость + мораль" },
      { type: 'quiz', question: "Крылов написал:", options: ["«Руслан и Людмила»", "«Стрекоза и Муравей»", "«Война и мир»", "«Отцы и дети»", "«Мёртвые души»"], correctAnswer: "«Стрекоза и Муравей»", hint: "Крылов — баснописец" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Басни»! 🎉" }
  },
  {
    title: "Сказки Пушкина",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Сколько лет ждал старик золотую рыбку?", options: ["20 лет", "35 лет", "33 года", "40 лет", "30 лет и 3 года"], correctAnswer: "30 лет и 3 года", hint: "«Жил старик со своею старухой...»" },
      { type: 'quiz', question: "Кто превратился в лебедя?", options: ["Царевна", "Боярышня", "Ткачиха", "Повариха", "Царица"], correctAnswer: "Царевна", hint: "Царевна-лебедь" },
      { type: 'quiz', question: "«Сказка о рыбаке и рыбке» — автор:", options: ["Толстой", "Ершов", "Лермонтов", "Гоголь", "Пушкин"], correctAnswer: "Пушкин", hint: "А.С. Пушкин" },
      { type: 'quiz', question: "Кто тянул репку первым?", options: ["Внучка", "Дедка", "Жучка", "Мышка", "Бабка"], correctAnswer: "Дедка", hint: "«Посадил дед репку...»" },
      { type: 'quiz', question: "Золотая рыбка исполнила:", options: ["3 желания (старухи)", "0 желаний", "1 желание", "5 желаний", "10 желаний"], correctAnswer: "3 желания (старухи)", hint: "Но старуха прогневала" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Сказки Пушкина»! 🎉" }
  },
  {
    title: "Умножение",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "7 × 8 = ?", options: ["63", "54", "56", "48", "42"], correctAnswer: "56", hint: "Таблица умножения" },
      { type: 'quiz', question: "6 × 7 = ?", options: ["42", "36", "48", "35", "49"], correctAnswer: "42", hint: "Таблица умножения" },
      { type: 'quiz', question: "9 × 9 = ?", options: ["72", "90", "63", "99", "81"], correctAnswer: "81", hint: "Таблица умножения" },
      { type: 'quiz', question: "5 × 8 = ?", options: ["45", "48", "40", "35", "32"], correctAnswer: "40", hint: "Таблица умножения" },
      { type: 'quiz', question: "4 × 6 = ?", options: ["20", "28", "24", "18", "30"], correctAnswer: "24", hint: "Таблица умножения" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Умножение»! 🎉" }
  },
  {
    title: "Деление",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "72 ÷ 9 = ?", options: ["9", "7", "8", "6", "10"], correctAnswer: "8", hint: "9 × 8 = 72" },
      { type: 'quiz', question: "56 ÷ 8 = ?", options: ["8", "6", "5", "9", "7"], correctAnswer: "7", hint: "8 × 7 = 56" },
      { type: 'quiz', question: "45 ÷ 5 = ?", options: ["11", "8", "10", "9", "7"], correctAnswer: "9", hint: "5 × 9 = 45" },
      { type: 'quiz', question: "64 ÷ 8 = ?", options: ["6", "10", "7", "8", "9"], correctAnswer: "8", hint: "8 × 8 = 64" },
      { type: 'quiz', question: "36 ÷ 6 = ?", options: ["4", "8", "7", "5", "6"], correctAnswer: "6", hint: "6 × 6 = 36" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Деление»! 🎉" }
  },
  {
    title: "Дроби",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "1/2 от 100 = ?", options: ["75", "20", "25", "10", "50"], correctAnswer: "50", hint: "Половина от 100" },
      { type: 'quiz', question: "1/4 от 200 = ?", options: ["75", "25", "100", "50", "40"], correctAnswer: "50", hint: "Четверть от 200" },
      { type: 'quiz', question: "Сократи дробь: 6/8", options: ["3/5", "4/6", "2/3", "1/2", "3/4"], correctAnswer: "3/4", hint: "Раздели на 2" },
      { type: 'quiz', question: "2/5 + 1/5 = ?", options: ["3/5", "2/5", "3/10", "4/5", "1/5"], correctAnswer: "3/5", hint: "Сложи числители" },
      { type: 'quiz', question: "Какая дробь больше: 2/3 или 1/2?", options: ["Они равны", "2/3", "1/2", "1/3", "Нельзя сравнить"], correctAnswer: "2/3", hint: "2/3 = 4/6, 1/2 = 3/6" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Дроби»! 🎉" }
  },
  {
    title: "Площадь и периметр",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Периметр квадрата со стороной 5:", options: ["20", "15", "25", "10", "30"], correctAnswer: "20", hint: "P = 4 × 5 = 20" },
      { type: 'quiz', question: "Площадь прямоугольника 3 × 4:", options: ["24", "10", "14", "7", "12"], correctAnswer: "12", hint: "S = 3 × 4 = 12" },
      { type: 'quiz', question: "Периметр прямоугольника 2 × 3:", options: ["8", "10", "6", "5", "12"], correctAnswer: "10", hint: "P = 2(2 + 3) = 10" },
      { type: 'quiz', question: "Площадь квадрата со стороной 6:", options: ["30", "24", "12", "42", "36"], correctAnswer: "36", hint: "S = 6² = 36" },
      { type: 'quiz', question: "Периметр квадрата со стороной 4:", options: ["16", "8", "12", "20", "24"], correctAnswer: "16", hint: "P = 4 × 4 = 16" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Площадь и периметр»! 🎉" }
  },
  {
    title: "Древний мир",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Главная река Египта:", options: ["Нил", "Тигр", "Волга", "Дунай", "Евфрат"], correctAnswer: "Нил", hint: "Нил — река жизни Египта" },
      { type: 'quiz', question: "Пирамиды строили для:", options: ["Музеев", "Зерна", "Фараонов (гробницы)", "Храмов", "Жилья"], correctAnswer: "Фараонов (гробницы)", hint: "Гробницы фараонов" },
      { type: 'quiz', question: "Правитель Египта:", options: ["Царь", "Султан", "Император", "Президент", "Фараон"], correctAnswer: "Фараон", hint: "Фараон — правитель Египта" },
      { type: 'quiz', question: "Греческий город-государство:", options: ["Республика", "Царство", "Полис", "Колония", "Империя"], correctAnswer: "Полис", hint: "Полис = город-государство" },
      { type: 'quiz', question: "Автор «Илиады» и «Одиссеи»:", options: ["Платон", "Аристотель", "Сократ", "Гомер", "Пифагор"], correctAnswer: "Гомер", hint: "Гомер — великий поэт" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Древний мир»! 🎉" }
  },
  {
    title: "Древняя Русь",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Кто основал династию Рюриковичей?", options: ["Святослав", "Иван Калита", "Владимир", "Рюрик", "Олег"], correctAnswer: "Рюрик", hint: "862 год — призвание варягов" },
      { type: 'quiz', question: "Крещение Руси:", options: ["1380", "1147", "988", "945", "862"], correctAnswer: "988", hint: "Князь Владимир" },
      { type: 'quiz', question: "Кто объединил Киев и Новгород?", options: ["Ярослав", "Рюрик", "Олег", "Владимир", "Игорь"], correctAnswer: "Олег", hint: "Вещий Олег, 882 год" },
      { type: 'quiz', question: "Куликовская битва:", options: ["1480", "988", "1380", "1147", "1613"], correctAnswer: "1380", hint: "Дмитрий Донской" },
      { type: 'quiz', question: "Первый письменный свод законов:", options: ["Русская Правда", "Судебник", "Устав", "Договор", "Конституция"], correctAnswer: "Русская Правда", hint: "Ярослав Мудрый" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Древняя Русь»! 🎉" }
  },
  {
    title: "Клетка",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какая часть хранит ДНК?", options: ["Мембрана", "Рибосома", "Лизосома", "Ядро", "Цитоплазма"], correctAnswer: "Ядро", hint: "Ядро — хранилище наследственности" },
      { type: 'quiz', question: "Цитоплазма — это:", options: ["Ядро", "Оболочка", "Внутренняя среда клетки", "Стенка", "Вакуоль"], correctAnswer: "Внутренняя среда клетки", hint: "Заполняет клетку" },
      { type: 'quiz', question: "«Энергетическая станция» клетки:", options: ["Митохондрия", "Ядро", "Хлоропласт", "Рибосома", "Мембрана"], correctAnswer: "Митохондрия", hint: "Митохондрии = АТФ" },
      { type: 'quiz', question: "Фотосинтез происходит в:", options: ["Хлоропластах", "Ядре", "Лизосомах", "Митохондриях", "Рибосомах"], correctAnswer: "Хлоропластах", hint: "Хлорофилл в хлоропластах" },
      { type: 'quiz', question: "Белки синтезируются на:", options: ["Хлоропластах", "Ядре", "Рибосомах", "Мембране", "Митохондриях"], correctAnswer: "Рибосомах", hint: "Рибосомы — фабрики белка" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Клетка»! 🎉" }
  },
  {
    title: "Царства живой природы",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Сколько царств живой природы?", options: ["2", "4", "6", "3", "5"], correctAnswer: "4", hint: "Бактерии, грибы, растения, животные" },
      { type: 'quiz', question: "Какое царство фотосинтезирует?", options: ["Животные", "Растения", "Бактерии", "Грибы", "Вирусы"], correctAnswer: "Растения", hint: "Хлорофилл в растениях" },
      { type: 'quiz', question: "Грибы — это:", options: ["Животные", "Отдельное царство", "Вирусы", "Растения", "Бактерии"], correctAnswer: "Отдельное царство", hint: "Не растения и не животные" },
      { type: 'quiz', question: "Самое древнее царство:", options: ["Животные", "Вирусы", "Грибы", "Бактерии", "Растения"], correctAnswer: "Бактерии", hint: "Появились первыми" },
      { type: 'quiz', question: "Вирусы — это:", options: ["Бактерии", "Грибы", "Растения", "Царство", "Неклеточная форма"], correctAnswer: "Неклеточная форма", hint: "Не имеют клетки" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Царства живой природы»! 🎉" }
  },
  {
    title: "План и карта",
    subject: "География",
    icon: "Map",
    color: "text-teal-400",
    tasks: [
      { type: 'quiz', question: "Что показывает масштаб?", options: ["Расстояние", "Направление", "Площадь", "Степень уменьшения", "Высоту"], correctAnswer: "Степень уменьшения", hint: "Во сколько раз уменьшено" },
      { type: 'quiz', question: "Стороны горизонта:", options: ["Лево, право", "Север, юг, восток, запад", "Близко, далеко", "Верх, низ", "Тут, там"], correctAnswer: "Север, юг, восток, запад", hint: "4 основных направления" },
      { type: 'quiz', question: "Масштаб 1:1000 означает:", options: ["1 см = 1 м", "1 см = 10 м", "1 см = 1000 см", "1 см = 1 км", "1 см = 100 м"], correctAnswer: "1 см = 1000 см", hint: "В 1000 раз больше" },
      { type: 'quiz', question: "Горизонталь на карте показывает:", options: ["Осадки", "Ветер", "Давление", "Рельеф", "Температуру"], correctAnswer: "Рельеф", hint: "Одинаковая высота" },
      { type: 'quiz', question: "Азимут измеряется в:", options: ["Километрах", "Градусах", "Минутах", "Секундах", "Метрах"], correctAnswer: "Градусах", hint: "От 0° до 360°" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «План и карта»! 🎉" }
  },
  {
    title: "Мировой океан",
    subject: "География",
    icon: "Map",
    color: "text-teal-400",
    tasks: [
      { type: 'quiz', question: "Сколько океанов на Земле?", options: ["5", "6", "3", "4", "7"], correctAnswer: "5", hint: "Тихий, Атлантический, Индийский, Сев. Ледовитый, Южный" },
      { type: 'quiz', question: "Самый большой океан:", options: ["Тихий", "Южный", "Атлантический", "Индийский", "Северный Ледовитый"], correctAnswer: "Тихий", hint: "Тихий — самый большой" },
      { type: 'quiz', question: "Самый тёплый океан:", options: ["Южный", "Индийский", "Тихий", "Северный Ледовитый", "Атлантический"], correctAnswer: "Индийский", hint: "Индийский — самый тёплый" },
      { type: 'quiz', question: "Солёность океанской воды:", options: ["0‰", "10‰", "35‰", "50‰", "100‰"], correctAnswer: "35‰", hint: "В среднем 35 промилле" },
      { type: 'quiz', question: "Море — это часть:", options: ["Озера", "Залива", "Океана", "Пролива", "Реки"], correctAnswer: "Океана", hint: "Море принадлежит океану" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Мировой океан»! 🎉" }
  },
  {
    title: "Present Simple",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I ___ a student.", options: ["be", "are", "was", "am", "is"], correctAnswer: "am", hint: "I am — единственное число" },
      { type: 'quiz', question: "She ___ to school every day.", options: ["went", "gone", "goes", "go", "going"], correctAnswer: "goes", hint: "She + V-s/es" },
      { type: 'quiz', question: "They ___ English.", options: ["spoken", "speak", "speaking", "spoke", "speaks"], correctAnswer: "speak", hint: "They + V (без s)" },
      { type: 'quiz', question: "He ___ like pizza.", options: ["doesn't", "wasn't", "don't", "isn't", "aren't"], correctAnswer: "doesn't", hint: "He + doesn't" },
      { type: 'quiz', question: "___ you like ice cream?", options: ["Is", "Does", "Do", "Was", "Are"], correctAnswer: "Do", hint: "You + Do" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Present Simple»! 🎉" }
  },
  {
    title: "Past Simple",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Yesterday I ___ to school.", options: ["went", "going", "goed", "gone", "go"], correctAnswer: "went", hint: "Go — went (неправильный)" },
      { type: 'quiz', question: "She ___ (play) football yesterday.", options: ["plaied", "playing", "plays", "played", "play"], correctAnswer: "played", hint: "Правильный + -ed" },
      { type: 'quiz', question: "I ___ (see) him yesterday.", options: ["seen", "seed", "see", "seeing", "saw"], correctAnswer: "saw", hint: "See — saw — seen" },
      { type: 'quiz', question: "___ you watch TV yesterday?", options: ["Are", "Does", "Did", "Were", "Do"], correctAnswer: "Did", hint: "Did для прошедшего" },
      { type: 'quiz', question: "He ___ (come) home late.", options: ["comes", "coming", "come", "comed", "came"], correctAnswer: "came", hint: "Come — came — come" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Past Simple»! 🎉" }
  },
  {
    title: "Технология",
    subject: "Технология",
    icon: "Ruler",
    color: "text-yellow-400",
    tasks: [
      { type: 'quiz', question: "Бумага — материал из:", options: ["Стекла", "Пластика", "Резины", "Древесины", "Металла"], correctAnswer: "Древесины", hint: "Целлюлоза из дерева" },
      { type: 'quiz', question: "Ножницы — инструмент для:", options: ["Рисования", "Клея", "Шитья", "Резания", "Лепки"], correctAnswer: "Резания", hint: "Режут бумагу" },
      { type: 'quiz', question: "Клей нужен для:", options: ["Лепки", "Резания", "Рисования", "Измерения", "Соединения деталей"], correctAnswer: "Соединения деталей", hint: "Склеиваем части" },
      { type: 'quiz', question: "Какой инструмент измеряет длину?", options: ["Карандаш", "Ножницы", "Линейка", "Кисть", "Молоток"], correctAnswer: "Линейка", hint: "В сантиметрах" },
      { type: 'quiz', question: "Оригами — это:", options: ["Шитьё", "Рисование", "Вязание", "Искусство складывания бумаги", "Лепка"], correctAnswer: "Искусство складывания бумаги", hint: "Японское искусство" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Технология»! 🎉" }
  },
  {
    title: "Цвета",
    subject: "ИЗО",
    icon: "Palette",
    color: "text-rose-400",
    tasks: [
      { type: 'quiz', question: "Какого цвета солнце? ☀️", options: ["Жёлтое", "Красное", "Зелёное", "Фиолетовое", "Синее"], correctAnswer: "Жёлтое", hint: "Солнце яркое и тёплое" },
      { type: 'quiz', question: "Смешай жёлтый и синий:", options: ["Красный", "Зелёный", "Оранжевый", "Коричневый", "Фиолетовый"], correctAnswer: "Зелёный", hint: "Жёлтый + синий = зелёный" },
      { type: 'quiz', question: "Какого цвета трава? 🌿", options: ["Белая", "Зелёная", "Красная", "Жёлтая", "Синяя"], correctAnswer: "Зелёная", hint: "Трава зелёная" },
      { type: 'quiz', question: "Красный + жёлтый =", options: ["Коричневый", "Оранжевый", "Синий", "Фиолетовый", "Зелёный"], correctAnswer: "Оранжевый", hint: "Тёплый цвет" },
      { type: 'quiz', question: "Красный + синий =", options: ["Жёлтый", "Оранжевый", "Зелёный", "Коричневый", "Фиолетовый"], correctAnswer: "Фиолетовый", hint: "Холодный цвет" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Цвета»! 🎉" }
  },
  {
    title: "Музыкальные инструменты",
    subject: "Музыка",
    icon: "Music",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Какой инструмент бьют палочками?", options: ["Скрипка 🎻", "Флейта 🎶", "Барабан 🥁", "Гитара 🎸", "Пианино 🎹"], correctAnswer: "Барабан 🥁", hint: "Бум-бум-бум!" },
      { type: 'quiz', question: "Сколько нот в музыке?", options: ["8", "6", "12", "7", "5"], correctAnswer: "7", hint: "До, ре, ми, фа, соль, ля, си" },
      { type: 'quiz', question: "Чёрно-белый инструмент:", options: ["Барабан 🥁", "Скрипка 🎻", "Гитара 🎸", "Пианино 🎹", "Труба 🎺"], correctAnswer: "Пианино 🎹", hint: "Клавиши чёрные и белые" },
      { type: 'quiz', question: "У какого инструмента струны?", options: ["Гитара 🎸", "Труба 🎺", "Флейта 🎶", "Бубен", "Барабан 🥁"], correctAnswer: "Гитара 🎸", hint: "Дзинь-дзинь!" },
      { type: 'quiz', question: "Дирижёр руководит:", options: ["Цирком", "Хором", "Кинотеатром", "Оркестром", "Театром"], correctAnswer: "Оркестром", hint: "Дирижёр — руководитель" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Музыкальные инструменты»! 🎉" }
  },
  {
    title: "Спорт",
    subject: "Физкультура",
    icon: "Dumbbell",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Футбол играют:", options: ["Ракеткой", "Руками", "Клюшкой", "Ногами и мячом ⚽", "Без мяча"], correctAnswer: "Ногами и мячом ⚽", hint: "Футбол — ногами!" },
      { type: 'quiz', question: "Сколько игроков в команде по футболу?", options: ["9", "6", "7", "5", "11"], correctAnswer: "11", hint: "11 на поле" },
      { type: 'quiz', question: "Что полезно для здоровья?", options: ["Есть конфеты", "Мало двигаться", "Сидеть весь день", "Зарядка", "Не спать"], correctAnswer: "Зарядка", hint: "Движение — жизнь!" },
      { type: 'quiz', question: "Баскетбол играют:", options: ["Руками и мячом 🏀", "Клюшкой", "Ракеткой", "Ногами", "Без мяча"], correctAnswer: "Руками и мячом 🏀", hint: "Забрасываем в кольцо" },
      { type: 'quiz', question: "Сколько раз в неделю нужно заниматься спортом?", options: ["0", "3-4", "1", "7", "2"], correctAnswer: "3-4", hint: "Регулярность важна" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Спорт»! 🎉" }
  },
  {
    title: "Безопасность",
    subject: "ОБЖ",
    icon: "Shield",
    color: "text-slate-400",
    tasks: [
      { type: 'quiz', question: "При пожаре нужно звонить:", options: ["102", "104", "112", "103", "101"], correctAnswer: "101", hint: "Пожарная служба" },
      { type: 'quiz', question: "Скорая помощь:", options: ["102", "112", "103", "101", "104"], correctAnswer: "103", hint: "Медицинская помощь" },
      { type: 'quiz', question: "Полиция:", options: ["103", "102", "101", "104", "112"], correctAnswer: "102", hint: "Полицейская служба" },
      { type: 'quiz', question: "Единый номер экстренной помощи:", options: ["104", "112", "101", "103", "102"], correctAnswer: "112", hint: "Единый номер" },
      { type: 'quiz', question: "При пожаре НЕЛЬЗЯ:", options: ["Идти к выходу", "Прятаться", "Звонить 101", "Дышать через влажную ткань", "Эвакуироваться"], correctAnswer: "Прятаться", hint: "Нельзя прятаться!" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Безопасность»! 🎉" }
  },
]
