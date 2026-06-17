// Экспорт игр для 6 класса
import { GameLesson } from '../types'

export const sixthGradeGames: GameLesson[] = [
  // ========== МАТЕМАТИКА ==========
  {
    title: "Отрицательные числа",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "-5 + 3 = ?", options: ["-2", "-8", "2", "-5", "8"], correctAnswer: "-2", hint: "От большего по модулю отнимаем меньшее" },
      { type: 'quiz', question: "-7 - 3 = ?", options: ["-4", "-10", "4", "-3", "10"], correctAnswer: "-10", hint: "Два минуса = складываем модули, знак минус" },
      { type: 'quiz', question: "-4 × 5 = ?", options: ["-20", "20", "-9", "9", "-1"], correctAnswer: "-20", hint: "Минус на плюс = минус" },
      { type: 'quiz', question: "-6 × (-2) = ?", options: ["-12", "12", "-8", "8", "-4"], correctAnswer: "12", hint: "Минус на минус = плюс" },
      { type: 'quiz', question: "-12 ÷ 4 = ?", options: ["-3", "3", "-8", "8", "-4"], correctAnswer: "-3", hint: "Минус делим на плюс = минус" }
    ],
    reward: { stars: 3, message: "Отлично! Ты работаешь с отрицательными числами! 🔢" }
  },
  {
    title: "Координаты на плоскости",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Точка A(3, 2). Какая координата x?", options: ["3", "2", "5", "1", "6"], correctAnswer: "3", hint: "Первая координата - это x (абсцисса)" },
      { type: 'quiz', question: "Где находится точка (-2, 3)?", options: ["I четверть", "II четверть", "III четверть", "IV четверть", "На оси"], correctAnswer: "II четверть", hint: "x отрицательный, y положительный" },
      { type: 'quiz', question: "Точка (0, 5) лежит на оси:", options: ["x", "y", "Обеих осях", "Начале координат", "Ни на какой"], correctAnswer: "y", hint: "x=0, значит на оси y" },
      { type: 'quiz', question: "Сколько координат у точки на плоскости?", options: ["1", "2", "3", "4", "5"], correctAnswer: "2", hint: "x и y - две координаты" },
      { type: 'quiz', question: "Где находится точка (4, -3)?", options: ["I четверть", "II четверть", "III четверть", "IV четверть", "На оси"], correctAnswer: "IV четверть", hint: "x положительный, y отрицательный — IV четверть" }
    ],
    reward: { stars: 3, message: "Супер! Ты понимаешь координаты! 📐" }
  },
  {
    title: "Пропорции",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "3/6 = 1/2. Верно ли равенство?", options: ["Да", "Нет", "Частично", "Нельзя сравнить", "Иногда"], correctAnswer: "Да", hint: "3/6 = 1/2 (сократили на 3)" },
      { type: 'quiz', question: "x/4 = 3/12, x = ?", options: ["1", "2", "3", "4", "0"], correctAnswer: "1", hint: "x = 4 × 3 / 12 = 1" },
      { type: 'quiz', question: "Основное свойство пропорции:", options: ["a/b = c/d", "a×d = b×c", "a+c = b+d", "a-b = c-d", "a×b = c×d"], correctAnswer: "a×d = b×c", hint: "Произведение крайних = произведению средних" },
      { type: 'quiz', question: "5/x = 10/4, x = ?", options: ["2", "1", "3", "4", "5"], correctAnswer: "2", hint: "x = 5 × 4 / 10 = 2" },
      { type: 'quiz', question: "8/4 = 6/x, x = ?", options: ["2", "3", "4", "5", "6"], correctAnswer: "3", hint: "x = 4 × 6 / 8 = 3" }
    ],
    reward: { stars: 3, message: "Отлично! Ты решаешь пропорции! ⚖️" }
  },
  {
    title: "Длина окружности и площадь круга",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Формула длины окружности?", options: ["C = πr", "C = 2πr", "C = πr²", "C = 2πr²", "C = π/r"], correctAnswer: "C = 2πr", hint: "C = 2πr или C = πd" },
      { type: 'quiz', question: "Формула площади круга?", options: ["S = πr", "S = 2πr", "S = πr²", "S = 2πr²", "S = π/r"], correctAnswer: "S = πr²", hint: "Площадь круга = π × радиус²" },
      { type: 'quiz', question: "Если r = 3, то C = 2π × 3 = ?", options: ["6π", "9π", "3π", "12π", "18π"], correctAnswer: "6π", hint: "C = 2πr = 2π × 3 = 6π" },
      { type: 'quiz', question: "Чему примерно равно π?", options: ["3", "3.14", "3.5", "2.14", "4.14"], correctAnswer: "3.14", hint: "π ≈ 3.14" },
      { type: 'quiz', question: "Если r = 5, то S = π × 25 = ?", options: ["5π", "10π", "25π", "50π", "15π"], correctAnswer: "25π", hint: "S = πr² = π × 5² = 25π" }
    ],
    reward: { stars: 3, message: "Умница! Ты знаешь геометрию круга! ⭕" }
  },

  // ========== РУССКИЙ ЯЗЫК ==========
  {
    title: "Имя числительное",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "«Пять» - это числительное...", options: ["Количественное", "Порядковое", "Собирательное", "Дробное", "Целое"], correctAnswer: "Количественное", hint: "Количественные отвечают на «сколько?»" },
      { type: 'quiz', question: "«Пятый» - это числительное...", options: ["Количественное", "Порядковое", "Дробное", "Собирательное", "Целое"], correctAnswer: "Порядковое", hint: "Порядковые отвечают на «который?»" },
      { type: 'find', question: "Выбери числительные:", options: ["Пять", "Пятёрка", "Пятеро", "Пятый", "Пятивратный"], correctAnswer: ["Пять", "Пятеро", "Пятый"], hint: "Числительное - часть речи, обозначающая число" },
      { type: 'quiz', question: "«Двое» - это числительное...", options: ["Количественное", "Порядковое", "Собирательное", "Дробное", "Целое"], correctAnswer: "Собирательное", hint: "Собирательные: двое, трое, четверо..." },
      { type: 'quiz', question: "«Одна целая и одна вторая» - это числительное...", options: ["Количественное", "Порядковое", "Собирательное", "Дробное", "Простое"], correctAnswer: "Дробное", hint: "Дробные числительные обозначают дробные числа" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь числительные! 🔢" }
  },
  {
    title: "Местоимение",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "«Я, ты, он, она» - это местоимения...", options: ["Личные", "Притяжательные", "Вопросительные", "Указательные", "Неопределённые"], correctAnswer: "Личные", hint: "Личные местоимения указывают на лица" },
      { type: 'find', question: "Выбери личные местоимения:", options: ["Я", "Мой", "Ты", "Кто", "Он"], correctAnswer: ["Я", "Ты", "Он"], hint: "Личные: я, ты, он, она, оно, мы, вы, они" },
      { type: 'quiz', question: "«Мой, твой, наш» - это местоимения...", options: ["Личные", "Притяжательные", "Указательные", "Вопросительные", "Неопределённые"], correctAnswer: "Притяжательные", hint: "Притяжательные указывают на принадлежность" },
      { type: 'quiz', question: "«Кто, что, какой» - это местоимения...", options: ["Личные", "Вопросительные", "Относительные", "Указательные", "Притяжательные"], correctAnswer: "Вопросительные", hint: "Вопросительные используются в вопросах" },
      { type: 'quiz', question: "«Этот, тот, такой» - это местоимения...", options: ["Личные", "Притяжательные", "Указательные", "Вопросительные", "Неопределённые"], correctAnswer: "Указательные", hint: "Указательные местоимения указывают на предметы" }
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь местоимения! ✍️" }
  },
  {
    title: "Н и НН в прилагательных",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Сколько Н в слове «кожаный»?", options: ["Н", "НН", "ННН", "Без Н", "Мягкий знак"], correctAnswer: "Н", hint: "-ан-, -ян-, -ин- пишется одна Н" },
      { type: 'quiz', question: "Сколько Н в слове «деревянный»?", options: ["Н", "НН", "ННН", "Без Н", "Мягкий знак"], correctAnswer: "НН", hint: "-енн-, -онн- пишется НН" },
      { type: 'find', question: "Выбери слова с НН:", options: ["Серебряный", "Традиционный", "Лимонный", "Кожаный", "Соломенный"], correctAnswer: ["Традиционный", "Лимонный", "Соломенный"], hint: "-онн-, -енн- = НН" },
      { type: 'quiz', question: "Сколько Н в слове «стеклянный»?", options: ["Н", "НН", "ННН", "Без Н", "Мягкий знак"], correctAnswer: "НН", hint: "Стеклянный - исключение!" },
      { type: 'quiz', question: "Сколько Н в слове «песчаный»?", options: ["Н", "НН", "ННН", "Без Н", "Мягкий знак"], correctAnswer: "Н", hint: "-ан- пишется с одной Н" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь правописание Н и НН! 📚" }
  },

  // ========== ЛИТЕРАТУРА ==========
  {
    title: "Литературные жанры",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Рассказ - это жанр...", options: ["Эпоса", "Лирики", "Драмы", "Сатиры", "Юмора"], correctAnswer: "Эпоса", hint: "Эпос - повествовательные жанры" },
      { type: 'quiz', question: "Стихотворение - это жанр...", options: ["Эпоса", "Лирики", "Драмы", "Сатиры", "Юмора"], correctAnswer: "Лирики", hint: "Лирика выражает чувства и переживания" },
      { type: 'find', question: "Выбери эпические жанры:", options: ["Роман", "Стихотворение", "Рассказ", "Пьеса", "Повесть"], correctAnswer: ["Роман", "Рассказ", "Повесть"], hint: "Эпос рассказывает о событиях" },
      { type: 'quiz', question: "Пьеса - это жанр...", options: ["Эпоса", "Лирики", "Драмы", "Сатиры", "Юмора"], correctAnswer: "Драмы", hint: "Драма предназначена для постановки" },
      { type: 'quiz', question: "Ода - это жанр...", options: ["Эпоса", "Лирики", "Драмы", "Сатиры", "Юмора"], correctAnswer: "Лирики", hint: "Ода — торжественное стихотворение, восхваляющее кого-то" }
    ],
    reward: { stars: 3, message: "Прекрасно! Ты знаешь литературные роды! 📖" }
  },
  {
    title: "Изобразительные средства",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "«Золотые руки» - это...", options: ["Эпитет", "Метафора", "Сравнение", "Олицетворение", "Гипербола"], correctAnswer: "Метафора", hint: "Метафора - скрытое сравнение" },
      { type: 'quiz', question: "«Как лев, он был смел» - это...", options: ["Эпитет", "Метафора", "Сравнение", "Олицетворение", "Гипербола"], correctAnswer: "Сравнение", hint: "Сравнение с союзами как, словно, будто" },
      { type: 'find', question: "Выбери эпитеты:", options: ["Золотая осень", "Быстро бежит", "Сладкий сон", "Крикливый сосед", "Птицы летят"], correctAnswer: ["Золотая осень", "Сладкий сон", "Крикливый сосед"], hint: "Эпитет - образное определение" },
      { type: 'quiz', question: "«Шёпот листьев» - это...", options: ["Эпитет", "Олицетворение", "Метафора", "Сравнение", "Гипербола"], correctAnswer: "Олицетворение", hint: "Олицетворение - наделение неживого свойствами живого" },
      { type: 'quiz', question: "«Океан слёз» - это...", options: ["Эпитет", "Олицетворение", "Метафора", "Сравнение", "Гипербола"], correctAnswer: "Гипербола", hint: "Гипербола - преувеличение" }
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь художественные средства! ✨" }
  },

  // ========== ИСТОРИЯ ==========
  {
    title: "Древняя Русь",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "В каком году призвали Рюрика?", options: ["862", "882", "988", "945", "1036"], correctAnswer: "862", hint: "862 год - призвание варягов" },
      { type: 'quiz', question: "Кто объединил Киев и Новгород?", options: ["Рюрик", "Олег", "Игорь", "Святослав", "Владимир"], correctAnswer: "Олег", hint: "Олег Вещий объединил в 882 году" },
      { type: 'find', question: "Выбери киевских князей:", options: ["Рюрик", "Олег", "Игорь", "Святослав", "Владимир"], correctAnswer: ["Олег", "Игорь", "Святослав", "Владимир"], hint: "Рюрик правил в Новгороде" },
      { type: 'quiz', question: "В каком году крестили Русь?", options: ["862", "988", "1036", "945", "882"], correctAnswer: "988", hint: "Крещение Руси - 988 год" },
      { type: 'quiz', question: "Какой князь крестил Русь?", options: ["Олег", "Игорь", "Святослав", "Ярослав Мудрый", "Владимир"], correctAnswer: "Владимир", hint: "Владимир Великий (Красное Солнышко)" }
    ],
    reward: { stars: 3, message: "Здорово! Ты знаешь историю Руси! 🏰" }
  },
  {
    title: "Феодальная раздробленность",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Что такое феодальная раздробленность?", options: ["Объединение земель", "Разделение на независимые княжества", "Война с врагами", "Создание государства", "Крещение Руси"], correctAnswer: "Разделение на независимые княжества", hint: "Каждое княжество управлялось самостоятельно" },
      { type: 'quiz', question: "Кто разгромил Русь в 1237-1240 годах?", options: ["Хазары", "Монголо-татары", "Викинги", "Поляки", "Шведы"], correctAnswer: "Монголо-татары", hint: "Батыево нашествие" },
      { type: 'find', question: "Выбери княжества периода раздробленности:", options: ["Киевское", "Владимиро-Суздальское", "Новгородская земля", "Римская империя", "Московское"], correctAnswer: ["Киевское", "Владимиро-Суздальское", "Новгородская земля", "Московское"], hint: "Русские княжества XII-XIII веков" },
      { type: 'quiz', question: "Кто был князем Владимиро-Суздальской земли?", options: ["Андрей Боголюбский", "Александр Невский", "Дмитрий Донской", "Иван Калита", "Рюрик"], correctAnswer: "Андрей Боголюбский", hint: "Андрей Боголюбский построил Успенский собор" },
      { type: 'quiz', question: "В каком веке началась раздробленность Руси?", options: ["X", "XI", "XII", "XIII", "IX"], correctAnswer: "XII", hint: "После смерти Мстислава Великого в 1132 году" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь историю! 📜" }
  },

  // ========== БИОЛОГИЯ ==========
  {
    title: "Фотосинтез",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Где происходит фотосинтез?", options: ["В корнях", "В листьях", "В цветках", "В стебле", "В семенах"], correctAnswer: "В листьях", hint: "Листья содержат хлорофилл" },
      { type: 'quiz', question: "Что нужно для фотосинтеза?", options: ["Кислород и вода", "Углекислый газ и вода", "Азот и вода", "Водород и вода", "Углерод и вода"], correctAnswer: "Углекислый газ и вода", hint: "CO₂ + H₂O → глюкоза + O₂" },
      { type: 'find', question: "Что образуется при фотосинтезе?", options: ["Кислород", "Углекислый газ", "Глюкоза", "Азот", "Вода"], correctAnswer: ["Кислород", "Глюкоза"], hint: "Продукты фотосинтеза" },
      { type: 'quiz', question: "Какой пигмент участвует в фотосинтезе?", options: ["Гемоглобин", "Хлорофилл", "Меланин", "Каротин", "Ксантофилл"], correctAnswer: "Хлорофилл", hint: "Хлорофилл даёт зелёный цвет" },
      { type: 'quiz', question: "Какой свет нужен для фотосинтеза?", options: ["Солнечный", "Ультрафиолетовый", "Инфракрасный", "Рентгеновский", "Любой"], correctAnswer: "Солнечный", hint: "Солнечный свет - главный источник энергии для фотосинтеза" }
    ],
    reward: { stars: 3, message: "Превосходно! Ты понимаешь фотосинтез! 🌱" }
  },
  {
    title: "Систематика организмов",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какая систематическая категория самая крупная?", options: ["Вид", "Род", "Царство", "Семейство", "Класс"], correctAnswer: "Царство", hint: "Царство > Тип > Класс > Отряд > Семейство > Род > Вид" },
      { type: 'quiz', question: "Какая категория самая мелкая?", options: ["Вид", "Род", "Семейство", "Класс", "Тип"], correctAnswer: "Вид", hint: "Вид - основная единица классификации" },
      { type: 'find', question: "Выбери правильный порядок (от крупного к мелкому):", options: ["Царство-Тип-Класс", "Класс-Тип-Царство", "Вид-Род-Семейство", "Царство-Вид-Класс", "Тип-Вид-Род"], correctAnswer: ["Царство-Тип-Класс"], hint: "От крупного к мелкому" },
      { type: 'quiz', question: "К какому царству относится человек?", options: ["Растения", "Грибы", "Животные", "Бактерии", "Простейшие"], correctAnswer: "Животные", hint: "Человек - животное" },
      { type: 'quiz', question: "К какому типу относится человек?", options: ["Хордовые", "Моллюски", "Членистоногие", "Кишечнополостные", "Кольчатые черви"], correctAnswer: "Хордовые", hint: "Хордовые имеют внутренний скелет — хорду" }
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь систематику! 🔬" }
  },

  // ========== ГЕОГРАФИЯ ==========
  {
    title: "Гидросфера",
    subject: "География",
    icon: "Map",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Сколько процентов Земли покрыто водой?", options: ["50%", "71%", "90%", "30%", "60%"], correctAnswer: "71%", hint: "71% поверхности Земли - вода" },
      { type: 'quiz', question: "Какой океан самый большой?", options: ["Атлантический", "Тихий", "Индийский", "Северный Ледовитый", "Южный"], correctAnswer: "Тихий", hint: "Тихий океан занимает 1/3 поверхности Земли" },
      { type: 'find', question: "Выбери части Мирового океана:", options: ["Озеро", "Море", "Река", "Залив", "Океан"], correctAnswer: ["Море", "Залив", "Океан"], hint: "Мировой океан = океаны + моря + заливы" },
      { type: 'quiz', question: "Как называется круговорот воды в природе?", options: ["Испарение", "Влагооборот", "Круговорот воды", "Осадки", "Сток"], correctAnswer: "Круговорот воды", hint: "Испарение → осадки → сток → испарение" },
      { type: 'quiz', question: "Какая река самая длинная в мире?", options: ["Амазонка", "Нил", "Волга", "Миссисипи", "Янцзы"], correctAnswer: "Нил", hint: "Нил протекает в Африке и имеет длину около 6670 км" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь гидросферу! 🌊" }
  },
  {
    title: "Атмосфера",
    subject: "География",
    icon: "Map",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Какой газ преобладает в атмосфере?", options: ["Кислород", "Азот", "Углекислый газ", "Водород", "Аргон"], correctAnswer: "Азот", hint: "Азот - 78%, кислород - 21%" },
      { type: 'quiz', question: "Какой слой атмосферы ближе к Земле?", options: ["Стратосфера", "Тропосфера", "Мезосфера", "Термосфера", "Экзосфера"], correctAnswer: "Тропосфера", hint: "Тропосфера - до 10-18 км" },
      { type: 'find', question: "Выбери атмосферные явления:", options: ["Дождь", "Ветер", "Цунами", "Облака", "Прилив"], correctAnswer: ["Дождь", "Ветер", "Облака"], hint: "Атмосферные явления - в воздухе" },
      { type: 'quiz', question: "Что измеряет барометр?", options: ["Температуру", "Атмосферное давление", "Влажность", "Скорость ветра", "Осадки"], correctAnswer: "Атмосферное давление", hint: "Барометр = атмосферное давление" },
      { type: 'quiz', question: "В каком слое атмосферы находится озоновый слой?", options: ["Тропосфера", "Стратосфера", "Мезосфера", "Термосфера", "Экзосфера"], correctAnswer: "Стратосфера", hint: "Озоновый слой защищает от ультрафиолета" }
    ],
    reward: { stars: 3, message: "Замечательно! Ты знаешь атмосферу! ☁️" }
  },

  // ========== АНГЛИЙСКИЙ ==========
  {
    title: "Past Perfect",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "When I came, she ___ already left.", options: ["has", "had", "was", "were", "have"], correctAnswer: "had", hint: "Past Perfect: had + V3" },
      { type: 'quiz', question: "I had ___ my work before he came.", options: ["finish", "finished", "finishing", "finishes", "to finish"], correctAnswer: "finished", hint: "had + V3 (правильный глагол + -ed)" },
      { type: 'quiz', question: "Past Perfect используется для...", options: ["Действия в прошлом до другого действия", "Действия сейчас", "Будущего действия", "Регулярного действия", "Действия в процессе"], correctAnswer: "Действия в прошлом до другого действия", hint: "«Предпрошедшее» время" },
      { type: 'find', question: "Выбери маркеры Past Perfect:", options: ["Yesterday", "By the time", "Last week", "Before", "Already (в прошлом)"], correctAnswer: ["By the time", "Before", "Already (в прошлом)"], hint: "By the time, before, after, already" },
      { type: 'quiz', question: "She had ___ the book before the film.", options: ["read", "reads", "reading", "to read", "readed"], correctAnswer: "read", hint: "had + V3: read — неправильный глагол, форма V3 = read" }
    ],
    reward: { stars: 3, message: "Great! Ты знаешь Past Perfect! ⏮️" }
  },
  {
    title: "Conditionals",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "If it rains, I ___ at home.", options: ["stay", "will stay", "stayed", "staying", "stays"], correctAnswer: "will stay", hint: "First Conditional: If + Present, will + V" },
      { type: 'quiz', question: "If I had money, I ___ a car.", options: ["buy", "would buy", "will buy", "bought", "buying"], correctAnswer: "would buy", hint: "Second Conditional: If + Past, would + V" },
      { type: 'quiz', question: "If I ___ you, I would study harder.", options: ["am", "were", "be", "was", "is"], correctAnswer: "were", hint: "Second Conditional с were для всех лиц" },
      { type: 'quiz', question: "Zero Conditional описывает...", options: ["Нереальное условие", "Факты и законы природы", "Будущее", "Прошлое", "Желания"], correctAnswer: "Факты и законы природы", hint: "If you heat water to 100°C, it boils." },
      { type: 'quiz', question: "If I had studied more, I ___ the exam.", options: ["will pass", "would pass", "pass", "passed", "passes"], correctAnswer: "would pass", hint: "Third Conditional: If + Past Perfect, would + have + V3" }
    ],
    reward: { stars: 3, message: "Excellent! Ты понимаешь условные предложения! 🔄" }
  },

  // ========== НОВЫЕ ИГРЫ ==========
  {
    title: "Сложение и вычитание дробей",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "1/2 + 1/4 = ?", options: ["3/4", "2/4", "1/6", "2/6", "1/4"], correctAnswer: "3/4", hint: "Приведи к общему знаменателю: 2/4 + 1/4 = 3/4" },
      { type: 'quiz', question: "3/4 - 1/4 = ?", options: ["2/4", "1/4", "3/4", "4/4", "1/2"], correctAnswer: "2/4", hint: "3/4 - 1/4 = 2/4 = 1/2" },
      { type: 'quiz', question: "1/2 + 1/3 = ?", options: ["2/5", "5/6", "1/6", "4/6", "2/6"], correctAnswer: "5/6", hint: "Общий знаменатель 6: 3/6 + 2/6" },
      { type: 'quiz', question: "5/6 - 1/3 = ?", options: ["4/3", "1/2", "3/6", "2/6", "4/6"], correctAnswer: "1/2", hint: "5/6 - 2/6 = 3/6 = 1/2" },
      { type: 'quiz', question: "2/5 + 1/10 = ?", options: ["3/10", "1/2", "5/10", "3/5", "2/10"], correctAnswer: "1/2", hint: "Общий знаменатель 10: 4/10 + 1/10 = 5/10 = 1/2" }
    ],
    reward: { stars: 3, message: "Отлично! Ты умеешь складывать дроби! 📊" }
  },
  {
    title: "Умножение и деление дробей",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "1/2 × 1/3 = ?", options: ["1/6", "2/6", "1/5", "2/5", "1/2"], correctAnswer: "1/6", hint: "1×1 / 2×3 = 1/6" },
      { type: 'quiz', question: "2/3 × 3/4 = ?", options: ["6/7", "1/2", "5/7", "6/12", "3/7"], correctAnswer: "1/2", hint: "2×3 / 3×4 = 6/12 = 1/2" },
      { type: 'quiz', question: "1/2 ÷ 1/4 = ?", options: ["2", "1/2", "1/8", "4", "1/4"], correctAnswer: "2", hint: "1/2 × 4/1 = 4/2 = 2" },
      { type: 'quiz', question: "3/4 ÷ 1/2 = ?", options: ["3/8", "1 1/2", "2/3", "6/4", "3/2"], correctAnswer: "1 1/2", hint: "3/4 × 2/1 = 6/4 = 1 1/2" },
      { type: 'quiz', question: "3/5 × 5/6 = ?", options: ["15/30", "1/2", "8/11", "2/5", "3/6"], correctAnswer: "1/2", hint: "3×5 / 5×6 = 15/30 = 1/2" }
    ],
    reward: { stars: 3, message: "Супер! Ты умеешь умножать и делить дроби! ✖️➗" }
  },
  {
    title: "Уравнения с дробями",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "x + 1/2 = 1, x = ?", options: ["1/2", "1/4", "3/4", "1", "2/2"], correctAnswer: "1/2", hint: "x = 1 - 1/2 = 1/2" },
      { type: 'quiz', question: "x - 1/4 = 1/2, x = ?", options: ["3/4", "1/4", "1/2", "2/4", "1"], correctAnswer: "3/4", hint: "x = 1/2 + 1/4 = 2/4 + 1/4 = 3/4" },
      { type: 'quiz', question: "2x = 1/2, x = ?", options: ["1", "1/4", "1/2", "2", "1/8"], correctAnswer: "1/4", hint: "x = 1/2 ÷ 2 = 1/4" },
      { type: 'quiz', question: "x/3 = 2/3, x = ?", options: ["2", "1", "3", "6", "2/9"], correctAnswer: "2", hint: "x = 3 × 2/3 = 2" },
      { type: 'quiz', question: "x + 3/5 = 1, x = ?", options: ["3/5", "2/5", "4/5", "1/5", "1"], correctAnswer: "2/5", hint: "x = 1 - 3/5 = 5/5 - 3/5 = 2/5" }
    ],
    reward: { stars: 3, message: "Отлично! Ты решаешь уравнения с дробями! 📐" }
  },
  {
    title: "Глагол: времена и формы",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Глаголы изменяются по:", options: ["Падежам", "Временам", "Склонениям", "Родам", "Числам"], correctAnswer: "Временам", hint: "Прошедшее, настоящее, будущее" },
      { type: 'find', question: "Выбери глаголы прошедшего времени:", options: ["Читал", "Читает", "Будет читать", "Писал", "Пишет"], correctAnswer: ["Читал", "Писал"], hint: "Прошедшее время - суффикс -л-" },
      { type: 'quiz', question: "Глаголы совершенного вида отвечают на вопрос:", options: ["Что делать?", "Что сделать?", "Оба вопроса", "Какой?", "Чей?"], correctAnswer: "Что сделать?", hint: "Совершенный вид = действие завершено" },
      { type: 'quiz', question: "Глагол «читать» - какого вида?", options: ["Совершенного", "Несовершенного", "Оба вида", "Ни одного", "Переходного"], correctAnswer: "Несовершенного", hint: "Несовершенный вид = что делать?" },
      { type: 'quiz', question: "Глагол «прочитать» - какого вида?", options: ["Совершенного", "Несовершенного", "Оба вида", "Ни одного", "Переходного"], correctAnswer: "Совершенного", hint: "Что сделать? — совершенный вид" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь глагол! 📝" }
  },
  {
    title: "Спряжения глаголов",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Глаголы I спряжения в 3 лице мн.ч. имеют окончание:", options: ["-ут/-ют", "-ат/-ят", "-ить", "-еть", "-ать"], correctAnswer: "-ут/-ют", hint: "I спряжение: -ут/-ют" },
      { type: 'quiz', question: "Глагол «говорить» - какого спряжения?", options: ["I спряжение", "II спряжение", "Оба", "Ни одного", "Разноспрягаемый"], correctAnswer: "II спряжение", hint: "ГоворИТЬ - II спряжение" },
      { type: 'find', question: "Выбери глаголы II спряжения:", options: ["Делать", "Смотреть", "Видеть", "Читать", "Любить"], correctAnswer: ["Смотреть", "Видеть", "Любить"], hint: "II спряжение: -ить + исключения" },
      { type: 'quiz', question: "Они пиш__т (I спр.). Какое окончание?", options: ["-ут", "-ат", "-ят", "-ит", "-ет"], correctAnswer: "-ут", hint: "Писать - I спряжение" },
      { type: 'quiz', question: "Глагол «брить» - это:", options: ["I спряжение", "II спряжение", "Разноспрягаемый", "Оба спряжения", "Ни одного"], correctAnswer: "I спряжение", hint: "«Брить» — исключение: -ить, но I спряжение" }
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь спряжения! ✍️" }
  },
  {
    title: "Басни И.А. Крылова",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Кто автор басни «Стрекоза и Муравей»?", options: ["Пушкин", "Крылов", "Лермонтов", "Тургенев", "Толстой"], correctAnswer: "Крылов", hint: "Иван Андреевич Крылов" },
      { type: 'find', question: "Выбери басни Крылова:", options: ["Ворона и Лисица", "Колобок", "Квартет", "Лебедь, Щука и Рак", "Репка"], correctAnswer: ["Ворона и Лисица", "Квартет", "Лебедь, Щука и Рак"], hint: "Басни И.А. Крылова" },
      { type: 'quiz', question: "Мораль басни - это:", options: ["Вступление", "Нравоучительный вывод", "Описание героев", "Завязка", "Развязка"], correctAnswer: "Нравоучительный вывод", hint: "Мораль учит чему-то" },
      { type: 'quiz', question: "«Ты всё пела? Это дело: Так поди же, ...!»", options: ["попляши", "попой", "отдохни", "поспи", "поработай"], correctAnswer: "попляши", hint: "Из басни «Стрекоза и Муравей»" },
      { type: 'quiz', question: "Кто такие герои басни «Квартет»?", options: ["Муравей и стрекоза", "Лев и мышь", "Мартышка, Осёл, Козёл и Мишка", "Ворона и Лисица", "Щука и Рак"], correctAnswer: "Мартышка, Осёл, Козёл и Мишка", hint: "Проказница Мартышка, Осёл, Козёл да косолапый Мишка" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь басни! 📚" }
  },
  {
    title: "Монголо-татарское иго",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Когда Батый напал на Русь?", options: ["1223", "1237", "1240", "1220", "1242"], correctAnswer: "1237", hint: "Зимой 1237-1238 годов" },
      { type: 'quiz', question: "Кто разбил шведов на Неве?", options: ["Дмитрий Донской", "Александр Невский", "Иван Калита", "Рюрик", "Олег"], correctAnswer: "Александр Невский", hint: "1240 год - Невская битва" },
      { type: 'find', question: "Выбери последствия ига:", options: ["Упадок культуры", "Развитие торговли", "Разрушение городов", "Усиление княжеств", "Уплата дани"], correctAnswer: ["Упадок культуры", "Разрушение городов", "Уплата дани"], hint: "Отрицательные последствия ига" },
      { type: 'quiz', question: "Когда закончилось иго?", options: ["1380", "1480", "1500", "1240", "1450"], correctAnswer: "1480", hint: "Стояние на Угре" },
      { type: 'quiz', question: "Кто стоял на реке Угре в 1480 году?", options: ["Дмитрий Донской", "Александр Невский", "Иван III", "Иван Калита", "Ярослав Мудрый"], correctAnswer: "Иван III", hint: "Иван III Васильевич и хан Ахмат" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь историю! 🏰" }
  },
  {
    title: "Куликовская битва",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "В каком году была Куликовская битва?", options: ["1380", "1480", "1240", "1223", "1360"], correctAnswer: "1380", hint: "8 сентября 1380 года" },
      { type: 'quiz', question: "Кто возглавил русское войско?", options: ["Александр Невский", "Дмитрий Донской", "Иван III", "Рюрик", "Олег"], correctAnswer: "Дмитрий Донской", hint: "Дмитрий Иванович Донской" },
      { type: 'find', question: "Выбери участников битвы:", options: ["Дмитрий Донской", "Мамай", "Александр Невский", "Батый", "Сергий Радонежский"], correctAnswer: ["Дмитрий Донской", "Мамай", "Сергий Радонежский"], hint: "Исторические личности 1380 года" },
      { type: 'quiz', question: "Битва проходила на ... поле", options: ["Куликовом", "Бородинском", "Полтавском", "Булыгином", "Пронским"], correctAnswer: "Куликовом", hint: "Куликовская битва" },
      { type: 'quiz', question: "Какой монах благословил войско на битву?", options: ["Пересвет", "Сергий Радонежский", "Ослябя", "Нестор", "Иларион"], correctAnswer: "Сергий Радонежский", hint: "Сергий Радонежский послал двух монахов-богатырей" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь историю! ⚔️" }
  },
  {
    title: "Органы цветковых растений",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какой орган растения отвечает за размножение?", options: ["Корень", "Лист", "Цветок", "Стебель", "Плод"], correctAnswer: "Цветок", hint: "Цветок - орган семенного размножения" },
      { type: 'find', question: "Выбери вегетативные органы:", options: ["Корень", "Цветок", "Стебель", "Лист", "Плод"], correctAnswer: ["Корень", "Стебель", "Лист"], hint: "Вегетативные органы обеспечивают рост" },
      { type: 'quiz', question: "Плод образуется из:", options: ["Лепестков", "Завязи цветка", "Тычинок", "Пестика", "Семян"], correctAnswer: "Завязи цветка", hint: "Из завязи после опыления" },
      { type: 'quiz', question: "Где находятся семена?", options: ["В листе", "В стебле", "В плоде", "В корне", "В цветке"], correctAnswer: "В плоде", hint: "Плод защищает семена" },
      { type: 'quiz', question: "Какая часть цветка привлекает насекомых?", options: ["Пестик", "Тычинка", "Венчик лепестков", "Чашелистики", "Завязь"], correctAnswer: "Венчик лепестков", hint: "Яркие лепестки привлекают опылителей" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь растения! 🌸" }
  },
  {
    title: "Present Continuous",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I ___ reading now.", options: ["is", "am", "are", "be", "was"], correctAnswer: "am", hint: "I am + V-ing" },
      { type: 'quiz', question: "She ___ tennis now.", options: ["is playing", "playing", "are playing", "am playing", "plays"], correctAnswer: "is playing", hint: "She is + V-ing" },
      { type: 'quiz', question: "They ___ sleeping.", options: ["is", "am", "are", "be", "was"], correctAnswer: "are", hint: "They are + V-ing" },
      { type: 'find', question: "Выбери маркеры Present Continuous:", options: ["Now", "Yesterday", "At the moment", "Tomorrow", "Always"], correctAnswer: ["Now", "At the moment"], hint: "Now, at the moment, look, listen" },
      { type: 'quiz', question: "He ___ TV right now.", options: ["is watching", "watch", "watches", "watched", "are watching"], correctAnswer: "is watching", hint: "He is + V-ing" }
    ],
    reward: { stars: 3, message: "Great! Ты знаешь Present Continuous! ⏳" }
  },
  {
    title: "Материки и океаны",
    subject: "География",
    icon: "Map",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Сколько материков на Земле?", options: ["5", "6", "7", "4", "8"], correctAnswer: "6", hint: "Евразия, Африка, Сев.Америка, Юж.Америка, Австралия, Антарктида" },
      { type: 'find', question: "Выбери океаны:", options: ["Тихий", "Атлантический", "Байкал", "Индийский", "Средиземное море"], correctAnswer: ["Тихий", "Атлантический", "Индийский"], hint: "Океаны - крупнейшие водоёмы" },
      { type: 'quiz', question: "Какой материк самый большой?", options: ["Африка", "Евразия", "Северная Америка", "Южная Америка", "Антарктида"], correctAnswer: "Евразия", hint: "Евразия - самый большой материк" },
      { type: 'quiz', question: "Самый холодный материк:", options: ["Евразия", "Африка", "Антарктида", "Австралия", "Северная Америка"], correctAnswer: "Антарктида", hint: "Антарктида - материк льдов" },
      { type: 'quiz', question: "Какой материк самый маленький?", options: ["Евразия", "Африка", "Антарктида", "Австралия", "Южная Америка"], correctAnswer: "Австралия", hint: "Австралия — самый маленький материк" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь географию! 🌍" }
  }
]
