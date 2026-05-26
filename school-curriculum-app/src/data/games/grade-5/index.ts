// Экспорт игр для 5 класса
import { GameLesson } from '../types'

export const fifthGradeGames: GameLesson[] = [
  {
    title: "Части речи",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Имя существительное обозначает:", options: ["Место", "Признак", "Действие", "Количество", "Предмет"], correctAnswer: "Предмет", hint: "Существительное = предмет" },
      { type: 'quiz', question: "Глагол обозначает:", options: ["Количество", "Предмет", "Место", "Признак", "Действие"], correctAnswer: "Действие", hint: "Глагол = действие" },
      { type: 'quiz', question: "Имя прилагательное обозначает:", options: ["Количество", "Место", "Предмет", "Признак предмета", "Действие"], correctAnswer: "Признак предмета", hint: "Прилагательное = признак" },
      { type: 'quiz', question: "На какой вопрос отвечает существительное?", options: ["Сколько?", "Какой?", "Где?", "Кто? Что?", "Что делать?"], correctAnswer: "Кто? Что?", hint: "Существительное — кто? что?" },
      { type: 'quiz', question: "На какой вопрос отвечает глагол?", options: ["Что делать?", "Где?", "Какой?", "Сколько?", "Кто? Что?"], correctAnswer: "Что делать?", hint: "Глагол — что делать?" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Части речи»! 🎉" }
  },
  {
    title: "Падежи",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Сколько падежей в русском языке?", options: ["5", "7", "6", "8", "4"], correctAnswer: "6", hint: "И, Р, Д, В, Т, П" },
      { type: 'quiz', question: "Именительный падеж отвечает на вопрос:", options: ["Кого? Чего?", "Кого? Что?", "Кем? Чем?", "Кому? Чему?", "Кто? Что?"], correctAnswer: "Кто? Что?", hint: "И.п. — кто? что?" },
      { type: 'quiz', question: "Родительный падеж отвечает на вопрос:", options: ["Кого? Что?", "Кому? Чему?", "Кем? Чем?", "Кого? Чего?", "Кто? Что?"], correctAnswer: "Кого? Чего?", hint: "Р.п. — кого? чего?" },
      { type: 'quiz', question: "Дательный падеж отвечает на вопрос:", options: ["Кому? Чему?", "Кто? Что?", "Кого? Чего?", "Кого? Что?", "Кем? Чем?"], correctAnswer: "Кому? Чему?", hint: "Д.п. — кому? чему?" },
      { type: 'quiz', question: "Предложный падеж отвечает на вопрос:", options: ["Кто? Что?", "Кому? Чему?", "Кем? Чем?", "О ком? О чём?", "Кого? Чего?"], correctAnswer: "О ком? О чём?", hint: "П.п. — о ком? о чём?" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Падежи»! 🎉" }
  },
  {
    title: "Корень слова",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Корень — это:", options: ["Суффикс", "Окончание", "Общая часть родственных слов", "Основа", "Приставка"], correctAnswer: "Общая часть родственных слов", hint: "В корне — общий смысл" },
      { type: 'quiz', question: "Какое слово однокоренное слову «лес»?", options: ["Лисица", "Линейка", "Лестница", "Лесник", "Лесть"], correctAnswer: "Лесник", hint: "Лес — лесник — лесной" },
      { type: 'quiz', question: "Корень в слове «подосиновик»:", options: ["осин", "овик", "под", "подос", "осовик"], correctAnswer: "осин", hint: "Под-осин-овик" },
      { type: 'quiz', question: "Какое слово НЕ однокоренное «вода»?", options: ["Водитель", "Наводнение", "Водный", "Подводник", "Водяной"], correctAnswer: "Водитель", hint: "Водитель — от «водить»" },
      { type: 'quiz', question: "Однокоренные слова имеют общий:", options: ["Суффикс", "Окончание", "Корень", "Ударение", "Приставку"], correctAnswer: "Корень", hint: "Корень — общая часть" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Корень слова»! 🎉" }
  },
  {
    title: "Басни",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Мораль басни — это:", options: ["Вступление", "Завязка", "Описание героев", "Развязка", "Нравоучительный вывод"], correctAnswer: "Нравоучительный вывод", hint: "Главный урок басни" },
      { type: 'quiz', question: "Автор «Ворона и Лисица»:", options: ["Гоголь", "Крылов", "Пушкин", "Лермонтов", "Толстой"], correctAnswer: "Крылов", hint: "И.А. Крылов" },
      { type: 'quiz', question: "Аллегория в басне — это:", options: ["Метафора", "Прямое описание", "Гипербола", "Сравнение", "Иносказание"], correctAnswer: "Иносказание", hint: "Животные = люди" },
      { type: 'quiz', question: "Басня — это:", options: ["Краткий рассказ с моралью", "Роман", "Очерк", "Пьеса", "Стихотворение"], correctAnswer: "Краткий рассказ с моралью", hint: "Краткость + мораль" },
      { type: 'quiz', question: "Крылов написал:", options: ["«Стрекоза и Муравей»", "«Мёртвые души»", "«Отцы и дети»", "«Война и мир»", "«Руслан и Людмила»"], correctAnswer: "«Стрекоза и Муравей»", hint: "Крылов — баснописец" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Басни»! 🎉" }
  },
  {
    title: "Сказки Пушкина",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Сколько лет ждал старик золотую рыбку?", options: ["40 лет", "33 года", "20 лет", "35 лет", "30 лет и 3 года"], correctAnswer: "30 лет и 3 года", hint: "«Жил старик со своею старухой...»" },
      { type: 'quiz', question: "Кто превратился в лебедя?", options: ["Боярышня", "Царица", "Повариха", "Царевна", "Ткачиха"], correctAnswer: "Царевна", hint: "Царевна-лебедь" },
      { type: 'quiz', question: "«Сказка о рыбаке и рыбке» — автор:", options: ["Толстой", "Ершов", "Пушкин", "Лермонтов", "Гоголь"], correctAnswer: "Пушкин", hint: "А.С. Пушкин" },
      { type: 'quiz', question: "Кто тянул репку первым?", options: ["Бабка", "Внучка", "Дедка", "Жучка", "Мышка"], correctAnswer: "Дедка", hint: "«Посадил дед репку...»" },
      { type: 'quiz', question: "Золотая рыбка исполнила:", options: ["0 желаний", "10 желаний", "5 желаний", "1 желание", "3 желания (старухи)"], correctAnswer: "3 желания (старухи)", hint: "Но старуха прогневала" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Сказки Пушкина»! 🎉" }
  },
  {
    title: "Умножение",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "7 × 8 = ?", options: ["48", "56", "42", "63", "54"], correctAnswer: "56", hint: "Таблица умножения" },
      { type: 'quiz', question: "6 × 7 = ?", options: ["42", "35", "48", "36", "49"], correctAnswer: "42", hint: "Таблица умножения" },
      { type: 'quiz', question: "9 × 9 = ?", options: ["63", "81", "72", "99", "90"], correctAnswer: "81", hint: "Таблица умножения" },
      { type: 'quiz', question: "5 × 8 = ?", options: ["40", "48", "45", "35", "32"], correctAnswer: "40", hint: "Таблица умножения" },
      { type: 'quiz', question: "4 × 6 = ?", options: ["24", "20", "30", "28", "18"], correctAnswer: "24", hint: "Таблица умножения" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Умножение»! 🎉" }
  },
  {
    title: "Деление",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "72 ÷ 9 = ?", options: ["10", "9", "6", "8", "7"], correctAnswer: "8", hint: "9 × 8 = 72" },
      { type: 'quiz', question: "56 ÷ 8 = ?", options: ["6", "7", "8", "5", "9"], correctAnswer: "7", hint: "8 × 7 = 56" },
      { type: 'quiz', question: "45 ÷ 5 = ?", options: ["9", "8", "7", "11", "10"], correctAnswer: "9", hint: "5 × 9 = 45" },
      { type: 'quiz', question: "64 ÷ 8 = ?", options: ["8", "10", "6", "9", "7"], correctAnswer: "8", hint: "8 × 8 = 64" },
      { type: 'quiz', question: "36 ÷ 6 = ?", options: ["8", "7", "4", "6", "5"], correctAnswer: "6", hint: "6 × 6 = 36" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Деление»! 🎉" }
  },
  {
    title: "Дроби",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "1/2 от 100 = ?", options: ["50", "20", "75", "25", "10"], correctAnswer: "50", hint: "Половина от 100" },
      { type: 'quiz', question: "1/4 от 200 = ?", options: ["40", "25", "100", "75", "50"], correctAnswer: "50", hint: "Четверть от 200" },
      { type: 'quiz', question: "Сократи дробь: 6/8", options: ["3/5", "4/6", "2/3", "1/2", "3/4"], correctAnswer: "3/4", hint: "Раздели на 2" },
      { type: 'quiz', question: "2/5 + 1/5 = ?", options: ["3/10", "3/5", "4/5", "2/5", "1/5"], correctAnswer: "3/5", hint: "Сложи числители" },
      { type: 'quiz', question: "Какая дробь больше: 2/3 или 1/2?", options: ["Нельзя сравнить", "Они равны", "1/3", "1/2", "2/3"], correctAnswer: "2/3", hint: "2/3 = 4/6, 1/2 = 3/6" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Дроби»! 🎉" }
  },
  {
    title: "Площадь и периметр",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Периметр квадрата со стороной 5:", options: ["30", "25", "10", "20", "15"], correctAnswer: "20", hint: "P = 4 × 5 = 20" },
      { type: 'quiz', question: "Площадь прямоугольника 3 × 4:", options: ["24", "12", "14", "7", "10"], correctAnswer: "12", hint: "S = 3 × 4 = 12" },
      { type: 'quiz', question: "Периметр прямоугольника 2 × 3:", options: ["12", "8", "5", "6", "10"], correctAnswer: "10", hint: "P = 2(2 + 3) = 10" },
      { type: 'quiz', question: "Площадь квадрата со стороной 6:", options: ["24", "36", "12", "30", "42"], correctAnswer: "36", hint: "S = 6² = 36" },
      { type: 'quiz', question: "Периметр квадрата со стороной 4:", options: ["24", "16", "20", "12", "8"], correctAnswer: "16", hint: "P = 4 × 4 = 16" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Площадь и периметр»! 🎉" }
  },
  {
    title: "Древний мир",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Главная река Египта:", options: ["Нил", "Евфрат", "Тигр", "Дунай", "Волга"], correctAnswer: "Нил", hint: "Нил — река жизни Египта" },
      { type: 'quiz', question: "Пирамиды строили для:", options: ["Храмов", "Зерна", "Фараонов (гробницы)", "Музеев", "Жилья"], correctAnswer: "Фараонов (гробницы)", hint: "Гробницы фараонов" },
      { type: 'quiz', question: "Правитель Египта:", options: ["Царь", "Император", "Президент", "Фараон", "Султан"], correctAnswer: "Фараон", hint: "Фараон — правитель Египта" },
      { type: 'quiz', question: "Греческий город-государство:", options: ["Колония", "Республика", "Полис", "Империя", "Царство"], correctAnswer: "Полис", hint: "Полис = город-государство" },
      { type: 'quiz', question: "Автор «Илиады» и «Одиссеи»:", options: ["Гомер", "Пифагор", "Аристотель", "Платон", "Сократ"], correctAnswer: "Гомер", hint: "Гомер — великий поэт" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Древний мир»! 🎉" }
  },
  {
    title: "Древняя Русь",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Кто основал династию Рюриковичей?", options: ["Святослав", "Олег", "Владимир", "Иван Калита", "Рюрик"], correctAnswer: "Рюрик", hint: "862 год — призвание варягов" },
      { type: 'quiz', question: "Крещение Руси:", options: ["945", "988", "1380", "1147", "862"], correctAnswer: "988", hint: "Князь Владимир" },
      { type: 'quiz', question: "Кто объединил Киев и Новгород?", options: ["Ярослав", "Олег", "Владимир", "Рюрик", "Игорь"], correctAnswer: "Олег", hint: "Вещий Олег, 882 год" },
      { type: 'quiz', question: "Куликовская битва:", options: ["1613", "1380", "1480", "1147", "988"], correctAnswer: "1380", hint: "Дмитрий Донской" },
      { type: 'quiz', question: "Первый письменный свод законов:", options: ["Судебник", "Конституция", "Устав", "Договор", "Русская Правда"], correctAnswer: "Русская Правда", hint: "Ярослав Мудрый" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Древняя Русь»! 🎉" }
  },
  {
    title: "Клетка",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какая часть хранит ДНК?", options: ["Лизосома", "Ядро", "Цитоплазма", "Рибосома", "Мембрана"], correctAnswer: "Ядро", hint: "Ядро — хранилище наследственности" },
      { type: 'quiz', question: "Цитоплазма — это:", options: ["Внутренняя среда клетки", "Оболочка", "Стенка", "Ядро", "Вакуоль"], correctAnswer: "Внутренняя среда клетки", hint: "Заполняет клетку" },
      { type: 'quiz', question: "«Энергетическая станция» клетки:", options: ["Митохондрия", "Хлоропласт", "Рибосома", "Ядро", "Мембрана"], correctAnswer: "Митохондрия", hint: "Митохондрии = АТФ" },
      { type: 'quiz', question: "Фотосинтез происходит в:", options: ["Митохондриях", "Лизосомах", "Хлоропластах", "Рибосомах", "Ядре"], correctAnswer: "Хлоропластах", hint: "Хлорофилл в хлоропластах" },
      { type: 'quiz', question: "Белки синтезируются на:", options: ["Рибосомах", "Ядре", "Хлоропластах", "Мембране", "Митохондриях"], correctAnswer: "Рибосомах", hint: "Рибосомы — фабрики белка" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Клетка»! 🎉" }
  },
  {
    title: "Царства живой природы",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Сколько царств живой природы?", options: ["5", "4", "2", "3", "6"], correctAnswer: "4", hint: "Бактерии, грибы, растения, животные" },
      { type: 'quiz', question: "Какое царство фотосинтезирует?", options: ["Растения", "Бактерии", "Грибы", "Вирусы", "Животные"], correctAnswer: "Растения", hint: "Хлорофилл в растениях" },
      { type: 'quiz', question: "Грибы — это:", options: ["Животные", "Отдельное царство", "Вирусы", "Растения", "Бактерии"], correctAnswer: "Отдельное царство", hint: "Не растения и не животные" },
      { type: 'quiz', question: "Самое древнее царство:", options: ["Вирусы", "Бактерии", "Животные", "Грибы", "Растения"], correctAnswer: "Бактерии", hint: "Появились первыми" },
      { type: 'quiz', question: "Вирусы — это:", options: ["Царство", "Растения", "Неклеточная форма", "Грибы", "Бактерии"], correctAnswer: "Неклеточная форма", hint: "Не имеют клетки" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Царства живой природы»! 🎉" }
  },
  {
    title: "План и карта",
    subject: "География",
    icon: "Map",
    color: "text-teal-400",
    tasks: [
      { type: 'quiz', question: "Что показывает масштаб?", options: ["Высоту", "Направление", "Расстояние", "Площадь", "Степень уменьшения"], correctAnswer: "Степень уменьшения", hint: "Во сколько раз уменьшено" },
      { type: 'quiz', question: "Стороны горизонта:", options: ["Верх, низ", "Лево, право", "Север, юг, восток, запад", "Близко, далеко", "Тут, там"], correctAnswer: "Север, юг, восток, запад", hint: "4 основных направления" },
      { type: 'quiz', question: "Масштаб 1:1000 означает:", options: ["1 см = 1 м", "1 см = 10 м", "1 см = 1000 см", "1 см = 1 км", "1 см = 100 м"], correctAnswer: "1 см = 1000 см", hint: "В 1000 раз больше" },
      { type: 'quiz', question: "Горизонталь на карте показывает:", options: ["Рельеф", "Давление", "Температуру", "Ветер", "Осадки"], correctAnswer: "Рельеф", hint: "Одинаковая высота" },
      { type: 'quiz', question: "Азимут измеряется в:", options: ["Километрах", "Метрах", "Секундах", "Градусах", "Минутах"], correctAnswer: "Градусах", hint: "От 0° до 360°" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «План и карта»! 🎉" }
  },
  {
    title: "Мировой океан",
    subject: "География",
    icon: "Map",
    color: "text-teal-400",
    tasks: [
      { type: 'quiz', question: "Сколько океанов на Земле?", options: ["3", "4", "5", "6", "7"], correctAnswer: "5", hint: "Тихий, Атлантический, Индийский, Сев. Ледовитый, Южный" },
      { type: 'quiz', question: "Самый большой океан:", options: ["Атлантический", "Северный Ледовитый", "Тихий", "Индийский", "Южный"], correctAnswer: "Тихий", hint: "Тихий — самый большой" },
      { type: 'quiz', question: "Самый тёплый океан:", options: ["Индийский", "Тихий", "Южный", "Северный Ледовитый", "Атлантический"], correctAnswer: "Индийский", hint: "Индийский — самый тёплый" },
      { type: 'quiz', question: "Солёность океанской воды:", options: ["0‰", "10‰", "100‰", "35‰", "50‰"], correctAnswer: "35‰", hint: "В среднем 35 промилле" },
      { type: 'quiz', question: "Море — это часть:", options: ["Океана", "Залива", "Пролива", "Реки", "Озера"], correctAnswer: "Океана", hint: "Море принадлежит океану" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Мировой океан»! 🎉" }
  },
  {
    title: "Present Simple",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I ___ a student.", options: ["was", "is", "am", "are", "be"], correctAnswer: "am", hint: "I am — единственное число" },
      { type: 'quiz', question: "She ___ to school every day.", options: ["went", "going", "gone", "go", "goes"], correctAnswer: "goes", hint: "She + V-s/es" },
      { type: 'quiz', question: "They ___ English.", options: ["spoken", "speaks", "speaking", "spoke", "speak"], correctAnswer: "speak", hint: "They + V (без s)" },
      { type: 'quiz', question: "He ___ like pizza.", options: ["don't", "doesn't", "aren't", "isn't", "wasn't"], correctAnswer: "doesn't", hint: "He + doesn't" },
      { type: 'quiz', question: "___ you like ice cream?", options: ["Are", "Is", "Was", "Do", "Does"], correctAnswer: "Do", hint: "You + Do" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Present Simple»! 🎉" }
  },
  {
    title: "Past Simple",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Yesterday I ___ to school.", options: ["go", "going", "went", "gone", "goed"], correctAnswer: "went", hint: "Go — went (неправильный)" },
      { type: 'quiz', question: "She ___ (play) football yesterday.", options: ["play", "played", "plays", "playing", "plaied"], correctAnswer: "played", hint: "Правильный + -ed" },
      { type: 'quiz', question: "I ___ (see) him yesterday.", options: ["seen", "seed", "see", "seeing", "saw"], correctAnswer: "saw", hint: "See — saw — seen" },
      { type: 'quiz', question: "___ you watch TV yesterday?", options: ["Do", "Does", "Did", "Were", "Are"], correctAnswer: "Did", hint: "Did для прошедшего" },
      { type: 'quiz', question: "He ___ (come) home late.", options: ["coming", "comed", "came", "comes", "come"], correctAnswer: "came", hint: "Come — came — come" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Past Simple»! 🎉" }
  },
  {
    title: "Технология",
    subject: "Технология",
    icon: "Ruler",
    color: "text-yellow-400",
    tasks: [
      { type: 'quiz', question: "Бумага — материал из:", options: ["Древесины", "Пластика", "Стекла", "Металла", "Резины"], correctAnswer: "Древесины", hint: "Целлюлоза из дерева" },
      { type: 'quiz', question: "Ножницы — инструмент для:", options: ["Резания", "Клея", "Рисования", "Лепки", "Шитья"], correctAnswer: "Резания", hint: "Режут бумагу" },
      { type: 'quiz', question: "Клей нужен для:", options: ["Измерения", "Рисования", "Резания", "Соединения деталей", "Лепки"], correctAnswer: "Соединения деталей", hint: "Склеиваем части" },
      { type: 'quiz', question: "Какой инструмент измеряет длину?", options: ["Молоток", "Ножницы", "Кисть", "Карандаш", "Линейка"], correctAnswer: "Линейка", hint: "В сантиметрах" },
      { type: 'quiz', question: "Оригами — это:", options: ["Рисование", "Шитьё", "Лепка", "Вязание", "Искусство складывания бумаги"], correctAnswer: "Искусство складывания бумаги", hint: "Японское искусство" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Технология»! 🎉" }
  },
  {
    title: "Цвета",
    subject: "ИЗО",
    icon: "Palette",
    color: "text-rose-400",
    tasks: [
      { type: 'quiz', question: "Какого цвета солнце? ☀️", options: ["Зелёное", "Синее", "Фиолетовое", "Красное", "Жёлтое"], correctAnswer: "Жёлтое", hint: "Солнце яркое и тёплое" },
      { type: 'quiz', question: "Смешай жёлтый и синий:", options: ["Красный", "Фиолетовый", "Зелёный", "Коричневый", "Оранжевый"], correctAnswer: "Зелёный", hint: "Жёлтый + синий = зелёный" },
      { type: 'quiz', question: "Какого цвета трава? 🌿", options: ["Жёлтая", "Синяя", "Белая", "Зелёная", "Красная"], correctAnswer: "Зелёная", hint: "Трава зелёная" },
      { type: 'quiz', question: "Красный + жёлтый =", options: ["Фиолетовый", "Оранжевый", "Коричневый", "Зелёный", "Синий"], correctAnswer: "Оранжевый", hint: "Тёплый цвет" },
      { type: 'quiz', question: "Красный + синий =", options: ["Зелёный", "Фиолетовый", "Оранжевый", "Коричневый", "Жёлтый"], correctAnswer: "Фиолетовый", hint: "Холодный цвет" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Цвета»! 🎉" }
  },
  {
    title: "Музыкальные инструменты",
    subject: "Музыка",
    icon: "Music",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Какой инструмент бьют палочками?", options: ["Барабан 🥁", "Пианино 🎹", "Флейта 🎶", "Гитара 🎸", "Скрипка 🎻"], correctAnswer: "Барабан 🥁", hint: "Бум-бум-бум!" },
      { type: 'quiz', question: "Сколько нот в музыке?", options: ["6", "7", "5", "12", "8"], correctAnswer: "7", hint: "До, ре, ми, фа, соль, ля, си" },
      { type: 'quiz', question: "Чёрно-белый инструмент:", options: ["Пианино 🎹", "Барабан 🥁", "Гитара 🎸", "Труба 🎺", "Скрипка 🎻"], correctAnswer: "Пианино 🎹", hint: "Клавиши чёрные и белые" },
      { type: 'quiz', question: "У какого инструмента струны?", options: ["Барабан 🥁", "Бубен", "Гитара 🎸", "Труба 🎺", "Флейта 🎶"], correctAnswer: "Гитара 🎸", hint: "Дзинь-дзинь!" },
      { type: 'quiz', question: "Дирижёр руководит:", options: ["Кинотеатром", "Хором", "Оркестром", "Цирком", "Театром"], correctAnswer: "Оркестром", hint: "Дирижёр — руководитель" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Музыкальные инструменты»! 🎉" }
  },
  {
    title: "Спорт",
    subject: "Физкультура",
    icon: "Dumbbell",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Футбол играют:", options: ["Ногами и мячом ⚽", "Клюшкой", "Без мяча", "Руками", "Ракеткой"], correctAnswer: "Ногами и мячом ⚽", hint: "Футбол — ногами!" },
      { type: 'quiz', question: "Сколько игроков в команде по футболу?", options: ["11", "6", "5", "9", "7"], correctAnswer: "11", hint: "11 на поле" },
      { type: 'quiz', question: "Что полезно для здоровья?", options: ["Не спать", "Сидеть весь день", "Мало двигаться", "Зарядка", "Есть конфеты"], correctAnswer: "Зарядка", hint: "Движение — жизнь!" },
      { type: 'quiz', question: "Баскетбол играют:", options: ["Без мяча", "Ногами", "Руками и мячом 🏀", "Ракеткой", "Клюшкой"], correctAnswer: "Руками и мячом 🏀", hint: "Забрасываем в кольцо" },
      { type: 'quiz', question: "Сколько раз в неделю нужно заниматься спортом?", options: ["1", "2", "0", "7", "3-4"], correctAnswer: "3-4", hint: "Регулярность важна" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Спорт»! 🎉" }
  },
  {
    title: "Безопасность",
    subject: "ОБЖ",
    icon: "Shield",
    color: "text-slate-400",
    tasks: [
      { type: 'quiz', question: "При пожаре нужно звонить:", options: ["101", "102", "112", "104", "103"], correctAnswer: "101", hint: "Пожарная служба" },
      { type: 'quiz', question: "Скорая помощь:", options: ["102", "112", "103", "101", "104"], correctAnswer: "103", hint: "Медицинская помощь" },
      { type: 'quiz', question: "Полиция:", options: ["101", "104", "102", "103", "112"], correctAnswer: "102", hint: "Полицейская служба" },
      { type: 'quiz', question: "Единый номер экстренной помощи:", options: ["103", "102", "112", "101", "104"], correctAnswer: "112", hint: "Единый номер" },
      { type: 'quiz', question: "При пожаре НЕЛЬЗЯ:", options: ["Дышать через влажную ткань", "Прятаться", "Эвакуироваться", "Звонить 101", "Идти к выходу"], correctAnswer: "Прятаться", hint: "Нельзя прятаться!" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Безопасность»! 🎉" }
  },
]
