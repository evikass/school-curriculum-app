// Экспорт игр для 10 класса
import { GameLesson } from '../types'

export const tenthGradeGames: GameLesson[] = [
  {
    title: "Нормы языка",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Орфоэпические нормы — это:", options: ["Правила произношения", "Правила пунктуации", "Правила написания", "Правила лексики", "Правила образования слов"], correctAnswer: "Правила произношения", hint: "Орфоэпия = произношение" },
      { type: 'quiz', question: "Грамматические нормы регулируют:", options: ["Пунктуацию", "Лексику", "Произношение", "Написание", "Образование форм слов"], correctAnswer: "Образование форм слов", hint: "Склонение, спряжение" },
      { type: 'quiz', question: "Лексические нормы — это:", options: ["Правила грамматики", "Правила написания", "Правила произношения", "Правила пунктуации", "Правила употребления слов"], correctAnswer: "Правила употребления слов", hint: "Правильное использование слов" },
      { type: 'quiz', question: "Орфографические нормы — это:", options: ["Правила написания", "Правила произношения", "Правила лексики", "Правила пунктуации", "Правила образования слов"], correctAnswer: "Правила написания", hint: "Орфография = написание" },
      { type: 'quiz', question: "Пунктуационные нормы — это:", options: ["Правила грамматики", "Правила написания", "Правила расстановки знаков", "Правила произношения", "Правила лексики"], correctAnswer: "Правила расстановки знаков", hint: "Пунктуация = знаки препинания" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Нормы языка»! 🎉" }
  },
  {
    title: "Изобразительные средства",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "«Золотые руки» — это:", options: ["Сравнение", "Олицетворение", "Гипербола", "Эпитет", "Метафора"], correctAnswer: "Метафора", hint: "Скрытое сравнение" },
      { type: 'quiz', question: "«Как лев, он был смел» — это:", options: ["Сравнение", "Метафора", "Эпитет", "Олицетворение", "Гипербола"], correctAnswer: "Сравнение", hint: "Сравнение с «как»" },
      { type: 'quiz', question: "«Шёпот листьев» — это:", options: ["Эпитет", "Олицетворение", "Гипербола", "Сравнение", "Метафора"], correctAnswer: "Олицетворение", hint: "Наделение неживого свойствами живого" },
      { type: 'quiz', question: "«Море слёз» — это:", options: ["Эпитет", "Гипербола", "Олицетворение", "Сравнение", "Метафора"], correctAnswer: "Гипербола", hint: "Преувеличение" },
      { type: 'quiz', question: "«Золотая осень» — это:", options: ["Метафора", "Сравнение", "Эпитет", "Гипербола", "Олицетворение"], correctAnswer: "Эпитет", hint: "Образное определение" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Изобразительные средства»! 🎉" }
  },
  {
    title: "Серебряный век",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Серебряный век — период:", options: ["XIX века", "XVIII века", "Конца XIX — начала XX века", "XXI века", "XX века"], correctAnswer: "Конца XIX — начала XX века", hint: "1890-1917 годы" },
      { type: 'quiz', question: "Поэт Серебряного века:", options: ["Крылов", "Некрасов", "Пушкин", "Блок", "Лермонтов"], correctAnswer: "Блок", hint: "Александр Блок" },
      { type: 'quiz', question: "Символизм — направление:", options: ["Модернистское", "Реалистическое", "Сентиментальное", "Классическое", "Романтическое"], correctAnswer: "Модернистское", hint: "Течение модернизма" },
      { type: 'quiz', question: "Акмеизм противопоставлялся:", options: ["Футуризму", "Классицизму", "Романтизму", "Символизму", "Реализму"], correctAnswer: "Символизму", hint: "Акмеисты отказались от символизма" },
      { type: 'quiz', question: "Есенин — поэт:", options: ["Советского периода", "Серебряного века", "Золотого века", "Древней Руси", "Постмодернизма"], correctAnswer: "Серебряного века", hint: "С.А. Есенин" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Серебряный век»! 🎉" }
  },
  {
    title: "Логарифмы",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "log₂8 = ?", options: ["4", "1", "2", "8", "3"], correctAnswer: "3", hint: "2³ = 8" },
      { type: 'quiz', question: "logₐa = ?", options: ["0", "2", "1", "10", "a"], correctAnswer: "1", hint: "a¹ = a" },
      { type: 'quiz', question: "logₐ1 = ?", options: ["a", "0", "1", "10", "-1"], correctAnswer: "0", hint: "a⁰ = 1" },
      { type: 'quiz', question: "log₂16 = ?", options: ["5", "3", "2", "8", "4"], correctAnswer: "4", hint: "2⁴ = 16" },
      { type: 'quiz', question: "log₁₀100 = ?", options: ["4", "3", "1", "10", "2"], correctAnswer: "2", hint: "10² = 100" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Логарифмы»! 🎉" }
  },
  {
    title: "Интеграл",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "∫x²dx = ?", options: ["x²/2 + C", "x + C", "x³ + C", "2x + C", "x³/3 + C"], correctAnswer: "x³/3 + C", hint: "∫xⁿdx = xⁿ⁺¹/(n+1)" },
      { type: 'quiz', question: "∫cos(x)dx = ?", options: ["cos(x) + C", "-cos(x) + C", "-sin(x) + C", "tg(x) + C", "sin(x) + C"], correctAnswer: "sin(x) + C", hint: "Производная синуса = косинус" },
      { type: 'quiz', question: "Формула Ньютона-Лейбница:", options: ["F(a) + F(b)", "F(a) - F(b)", "F(b) × F(a)", "F(b) - F(a)", "F(b)/F(a)"], correctAnswer: "F(b) - F(a)", hint: "Определённый интеграл через первообразную" },
      { type: 'quiz', question: "∫1dx = ?", options: ["x + C", "C", "0 + C", "1 + C", "x² + C"], correctAnswer: "x + C", hint: "Интеграл константы" },
      { type: 'quiz', question: "∫sin(x)dx = ?", options: ["cos(x) + C", "-sin(x) + C", "-cos(x) + C", "tg(x) + C", "sin(x) + C"], correctAnswer: "-cos(x) + C", hint: "Производная косинуса = -синус" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Интеграл»! 🎉" }
  },
  {
    title: "Тела вращения",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Объём цилиндра V = ?", options: ["πr²h", "2πrh", "4πr³", "πr³", "(1/3)πr²h"], correctAnswer: "πr²h", hint: "V = πr²h" },
      { type: 'quiz', question: "Объём конуса V = ?", options: ["πr²h", "πr³", "(1/3)πr²h", "2πr²h", "(1/2)πr²h"], correctAnswer: "(1/3)πr²h", hint: "V = 1/3 × πr²h" },
      { type: 'quiz', question: "Объём шара V = ?", options: ["(1/3)πr³", "2πr³", "4πr²", "(4/3)πr³", "πr³"], correctAnswer: "(4/3)πr³", hint: "V = 4/3 × πr³" },
      { type: 'quiz', question: "Цилиндр — вращение:", options: ["Треугольника", "Прямоугольника", "Трапеции", "Полукруга", "Круга"], correctAnswer: "Прямоугольника", hint: "Вокруг стороны" },
      { type: 'quiz', question: "Конус — вращение:", options: ["Круга", "Полукруга", "Трапеции", "Прямоугольника", "Треугольника"], correctAnswer: "Треугольника", hint: "Прямоугольного треугольника" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Тела вращения»! 🎉" }
  },
  {
    title: "Атомная физика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Кто открыл радиоактивность?", options: ["Кюри", "Бор", "Резерфорд", "Беккерель", "Эйнштейн"], correctAnswer: "Беккерель", hint: "Анри Беккерель, 1896" },
      { type: 'quiz', question: "Альфа-излучение — это:", options: ["Электромагнитные волны", "Поток нейтронов", "Поток протонов", "Поток ядер гелия", "Поток электронов"], correctAnswer: "Поток ядер гелия", hint: "α = ₂⁴He" },
      { type: 'quiz', question: "E = mc² — формула:", options: ["Эйнштейна", "Резерфорда", "Планка", "Ньютона", "Бора"], correctAnswer: "Эйнштейна", hint: "Эквивалентность массы и энергии" },
      { type: 'quiz', question: "Бета-излучение — это:", options: ["Поток ядер гелия", "Электромагнитные волны", "Поток протонов", "Поток нейтронов", "Поток электронов"], correctAnswer: "Поток электронов", hint: "β = электрон" },
      { type: 'quiz', question: "Ядро состоит из:", options: ["Протонов и электронов", "Протонов и нейтронов", "Нейтронов и электронов", "Только нейтронов", "Только протонов"], correctAnswer: "Протонов и нейтронов", hint: "Нуклоны = p + n" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Атомная физика»! 🎉" }
  },
  {
    title: "Химическая кинетика",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: "Скорость реакции измеряется в:", options: ["г/см³", "Дж/К", "м/с", "моль/(л·с)", "кг/м³"], correctAnswer: "моль/(л·с)", hint: "Изменение концентрации" },
      { type: 'quiz', question: "При повышении температуры скорость:", options: ["Увеличивается", "Уменьшается", "Не меняется", "Случайно", "Сначала растёт, потом падает"], correctAnswer: "Увеличивается", hint: "Правило Вант-Гоффа" },
      { type: 'quiz', question: "Катализатор:", options: ["Не влияет", "Ускоряет, не расходуясь", "Замедляет", "Расходуется", "Увеличивает выход"], correctAnswer: "Ускоряет, не расходуясь", hint: "Катализатор — помощник" },
      { type: 'quiz', question: "Фактор скорости:", options: ["Форма сосуда", "Запах", "Масса сосуда", "Температура", "Цвет вещества"], correctAnswer: "Температура", hint: "Температура влияет на скорость" },
      { type: 'quiz', question: "Обратимая реакция:", options: ["Только назад", "Идёт в обоих направлениях", "Только вперёд", "Не идёт", "Идёт случайно"], correctAnswer: "Идёт в обоих направлениях", hint: "⇌ обратимая" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Химическая кинетика»! 🎉" }
  },
  {
    title: "Вторая мировая война",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Когда началась Великая Отечественная война?", options: ["1941", "1943", "1939", "1942", "1940"], correctAnswer: "1941", hint: "22 июня 1941" },
      { type: 'quiz', question: "Битва под Москвой:", options: ["1943", "1945", "1941-1942", "1942-1943", "1944"], correctAnswer: "1941-1942", hint: "Первая победа над вермахтом" },
      { type: 'quiz', question: "Сталинградская битва:", options: ["1942-1943", "1941", "1944", "1943-1944", "1945"], correctAnswer: "1942-1943", hint: "Перелом в войне" },
      { type: 'quiz', question: "День Победы:", options: ["2 сентября 1945", "8 мая 1945", "9 мая 1945", "1 мая 1945", "7 ноября 1945"], correctAnswer: "9 мая 1945", hint: "9 мая — праздник" },
      { type: 'quiz', question: "Сколько длилась Великая Отечественная?", options: ["1418 дней", "1000 дней", "2000 дней", "800 дней", "365 дней"], correctAnswer: "1418 дней", hint: "Почти 4 года" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Вторая мировая война»! 🎉" }
  },
  {
    title: "Холодная война",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Холодная война началась после:", options: ["Второй мировой", "Крымской войны", "Революции 1917", "Наполеоновских войн", "Первой мировой"], correctAnswer: "Второй мировой", hint: "Противостояние СССР и США" },
      { type: 'quiz', question: "Фултонская речь Черчилля:", options: ["1950", "1945", "1948", "1947", "1946"], correctAnswer: "1946", hint: "Начало холодной войны" },
      { type: 'quiz', question: "Карибский кризис:", options: ["1962", "1960", "1965", "1955", "1970"], correctAnswer: "1962", hint: "Ядерный кризис" },
      { type: 'quiz', question: "Берлинская стена пала в:", options: ["1985", "1990", "1987", "1989", "1991"], correctAnswer: "1989", hint: "Символ окончания холодной войны" },
      { type: 'quiz', question: "Распад СССР:", options: ["1989", "1990", "1985", "1993", "1991"], correctAnswer: "1991", hint: "Декабрь 1991" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Холодная война»! 🎉" }
  },
  {
    title: "Право",
    subject: "Обществознание",
    icon: "Scale",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Конституция — это:", options: ["Указ президента", "Приказ", "Постановление", "Обычный закон", "Основной закон государства"], correctAnswer: "Основной закон государства", hint: "Высшая юридическая сила" },
      { type: 'quiz', question: "Правоспособность возникает с:", options: ["14 лет", "18 лет", "Рождения", "21 года", "16 лет"], correctAnswer: "Рождения", hint: "Способность иметь права" },
      { type: 'quiz', question: "Дееспособность в полном объёме с:", options: ["21 года", "18 лет", "25 лет", "14 лет", "16 лет"], correctAnswer: "18 лет", hint: "Совершеннолетие" },
      { type: 'quiz', question: "Право на жизнь — это:", options: ["Юридическое", "Социальное", "Естественное право", "Экономическое", "Политическое"], correctAnswer: "Естественное право", hint: "Принадлежит от рождения" },
      { type: 'quiz', question: "Высшая ценность по Конституции:", options: ["Закон", "Государство", "Человек и его права", "Собственность", "Порядок"], correctAnswer: "Человек и его права", hint: "Права человека — высшая ценность" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Право»! 🎉" }
  },
  {
    title: "Экономика",
    subject: "Обществознание",
    icon: "Scale",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Инфляция — это:", options: ["Увеличение производства", "Стабильность", "Снижение цен", "Рост зарплат", "Повышение общего уровня цен"], correctAnswer: "Повышение общего уровня цен", hint: "Обесценивание денег" },
      { type: 'quiz', question: "Спрос и предложение определяют:", options: ["Налоги", "Только спрос", "Зарплату", "Рыночную цену", "Только предложение"], correctAnswer: "Рыночную цену", hint: "Закон спроса и предложения" },
      { type: 'quiz', question: "Факторы производства:", options: ["Только капитал", "Только деньги", "Труд, земля, капитал, предпринимательство", "Только земля", "Только труд"], correctAnswer: "Труд, земля, капитал, предпринимательство", hint: "4 фактора" },
      { type: 'quiz', question: "Безработица — это:", options: ["Длинный отпуск", "Отсутствие работы у трудоспособных", "Малая зарплата", "Наличие работы", "Переутомление"], correctAnswer: "Отсутствие работы у трудоспособных", hint: "Экономическая проблема" },
      { type: 'quiz', question: "Налог — это:", options: ["Добровольный взнос", "Инвестиция", "Обязательный платёж государству", "Подарок", "Штраф"], correctAnswer: "Обязательный платёж государству", hint: "Обязательный платёж" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Экономика»! 🎉" }
  },
  {
    title: "Экология",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Экология изучает:", options: ["Атомы", "Взаимоотношения организмов", "Молекулы", "Звёзды", "Клетки"], correctAnswer: "Взаимоотношения организмов", hint: "Связи в природе" },
      { type: 'quiz', question: "Пищевая цепь начинается с:", options: ["Симбионтов", "Разлагателей", "Хищников", "Производителей", "Паразитов"], correctAnswer: "Производителей", hint: "Растения — производители" },
      { type: 'quiz', question: "Биосфера — это:", options: ["Атмосфера", "Литосфера", "Часть Земли с жизнью", "Гидросфера", "Магнитосфера"], correctAnswer: "Часть Земли с жизнью", hint: "По Вернадскому" },
      { type: 'quiz', question: "Автор учения о биосфере:", options: ["Ломоносов", "Дарвин", "Вернадский", "Менделеев", "Павлов"], correctAnswer: "Вернадский", hint: "В.И. Вернадский" },
      { type: 'quiz', question: "Красная книга содержит:", options: ["Ископаемые", "Опасные виды", "Редкие и исчезающие виды", "Все виды", "Домашние виды"], correctAnswer: "Редкие и исчезающие виды", hint: "Охрана природы" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Экология»! 🎉" }
  },
  {
    title: "География России",
    subject: "География",
    icon: "Map",
    color: "text-teal-400",
    tasks: [
      { type: 'quiz', question: "Самая длинная река России:", options: ["Енисей", "Волга", "Амур", "Обь (с Иртышом)", "Лена"], correctAnswer: "Обь (с Иртышом)", hint: "Обь + Иртыш = 5410 км" },
      { type: 'quiz', question: "Самое глубокое озеро:", options: ["Телецкое", "Ладожское", "Байкал", "Каспийское", "Онежское"], correctAnswer: "Байкал", hint: "1642 м глубина" },
      { type: 'quiz', question: "Россия граничит с:", options: ["14", "12", "18 странами", "10", "20"], correctAnswer: "18 странами", hint: "Самое большое число границ" },
      { type: 'quiz', question: "Самая высокая гора России:", options: ["Эльбрус", "Белуха", "Мунку-Сардык", "Казбек", "Народная"], correctAnswer: "Эльбрус", hint: "5642 м" },
      { type: 'quiz', question: "Площадь России:", options: ["10 млн", "15 млн", "20 млн", "12 млн", "17.1 млн км²"], correctAnswer: "17.1 млн км²", hint: "Крупнейшая страна" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «География России»! 🎉" }
  },
  {
    title: "Reported Speech",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "«I am happy» → He said he __ happy.", options: ["was", "has been", "is", "were", "will be"], correctAnswer: "was", hint: "Present → Past" },
      { type: 'quiz', question: "«I will come» → She said she __ come.", options: ["should", "would", "can", "could", "will"], correctAnswer: "would", hint: "Will → would" },
      { type: 'quiz', question: "«I can swim» → He said he __ swim.", options: ["must", "should", "can", "will", "could"], correctAnswer: "could", hint: "Can → could" },
      { type: 'quiz', question: "«Don't go!» → She told me:", options: ["to not go", "not go", "not to go", "don't go", "no go"], correctAnswer: "not to go", hint: "Повелительное → инфинитив с not" },
      { type: 'quiz', question: "«I saw him» → She said she __ seen him.", options: ["did", "was", "has", "had", "have"], correctAnswer: "had", hint: "Past → Past Perfect" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Reported Speech»! 🎉" }
  },
  {
    title: "Conditionals",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "If I __ (study), I will pass.", options: ["studying", "studied", "study", "will study", "studies"], correctAnswer: "study", hint: "First: If + Present, will + V" },
      { type: 'quiz', question: "If I __ (be) rich, I would travel.", options: ["was", "were", "am", "be", "will be"], correctAnswer: "were", hint: "Second: If + Past, would + V" },
      { type: 'quiz', question: "If I __ (know), I would have helped.", options: ["would know", "had known", "have known", "knew", "know"], correctAnswer: "had known", hint: "Third: If + Past Perfect, would have + V3" },
      { type: 'quiz', question: "Zero conditional: If you heat water, it ___.", options: ["will boil", "would boil", "boiled", "boil", "boils"], correctAnswer: "boils", hint: "Zero: If + Present, Present" },
      { type: 'quiz', question: "Mixed: If I __ (study) yesterday, I would pass now.", options: ["have studied", "would study", "study", "studied", "had studied"], correctAnswer: "had studied", hint: "Past Perf + would + V" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Conditionals»! 🎉" }
  },
  {
    title: "Основы информатики",
    subject: "Информатика",
    icon: "Monitor",
    color: "text-sky-400",
    tasks: [
      { type: 'quiz', question: "1 байт = ?", options: ["16 бит", "4 бита", "10 бит", "8 бит", "2 бита"], correctAnswer: "8 бит", hint: "1 байт = 8 бит" },
      { type: 'quiz', question: "Двоичная система использует цифры:", options: ["0-7", "0-F", "0-2", "0-9", "0 и 1"], correctAnswer: "0 и 1", hint: "Бинарная система" },
      { type: 'quiz', question: "Алгоритм — это:", options: ["Уравнение", "Таблица", "Рисунок", "Порядок действий", "Формула"], correctAnswer: "Порядок действий", hint: "Чёткая последовательность" },
      { type: 'quiz', question: "Переменная — это:", options: ["Цикл", "Массив", "Условие", "Функция", "Именованное хранилище данных"], correctAnswer: "Именованное хранилище данных", hint: "Хранит значение" },
      { type: 'quiz', question: "HTTP — это:", options: ["Протокол передачи данных", "Операционная система", "База данных", "Язык программирования", "Графический редактор"], correctAnswer: "Протокол передачи данных", hint: "Для веб-страниц" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Основы информатики»! 🎉" }
  },
  {
    title: "Спорт",
    subject: "Физкультура",
    icon: "Dumbbell",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Футбол играют:", options: ["Ногами и мячом ⚽", "Руками", "Ракеткой", "Без мяча", "Клюшкой"], correctAnswer: "Ногами и мячом ⚽", hint: "Футбол — ногами!" },
      { type: 'quiz', question: "Сколько игроков в команде по футболу?", options: ["6", "5", "11", "7", "9"], correctAnswer: "11", hint: "11 на поле" },
      { type: 'quiz', question: "Что полезно для здоровья?", options: ["Сидеть весь день", "Не спать", "Есть конфеты", "Мало двигаться", "Зарядка"], correctAnswer: "Зарядка", hint: "Движение — жизнь!" },
      { type: 'quiz', question: "Баскетбол играют:", options: ["Ногами", "Клюшкой", "Ракеткой", "Руками и мячом 🏀", "Без мяча"], correctAnswer: "Руками и мячом 🏀", hint: "Забрасываем в кольцо" },
      { type: 'quiz', question: "Сколько раз в неделю нужно заниматься спортом?", options: ["0", "2", "1", "3-4", "7"], correctAnswer: "3-4", hint: "Регулярность важна" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Спорт»! 🎉" }
  },
  {
    title: "Безопасность",
    subject: "ОБЖ",
    icon: "Shield",
    color: "text-slate-400",
    tasks: [
      { type: 'quiz', question: "При пожаре нужно звонить:", options: ["104", "103", "102", "101", "112"], correctAnswer: "101", hint: "Пожарная служба" },
      { type: 'quiz', question: "Скорая помощь:", options: ["101", "103", "102", "112", "104"], correctAnswer: "103", hint: "Медицинская помощь" },
      { type: 'quiz', question: "Полиция:", options: ["112", "102", "103", "101", "104"], correctAnswer: "102", hint: "Полицейская служба" },
      { type: 'quiz', question: "Единый номер экстренной помощи:", options: ["112", "104", "102", "103", "101"], correctAnswer: "112", hint: "Единый номер" },
      { type: 'quiz', question: "При пожаре НЕЛЬЗЯ:", options: ["Прятаться", "Идти к выходу", "Дышать через влажную ткань", "Эвакуироваться", "Звонить 101"], correctAnswer: "Прятаться", hint: "Нельзя прятаться!" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Безопасность»! 🎉" }
  },
]
