// Экспорт игр для 11 класса
import { GameLesson } from '../types'

export const eleventhGradeGames: GameLesson[] = [
  {
    title: "Нормы языка",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Орфоэпические нормы — это:", options: ["Правила пунктуации", "Правила образования слов", "Правила лексики", "Правила написания", "Правила произношения"], correctAnswer: "Правила произношения", hint: "Орфоэпия = произношение" },
      { type: 'quiz', question: "Грамматические нормы регулируют:", options: ["Произношение", "Лексику", "Написание", "Пунктуацию", "Образование форм слов"], correctAnswer: "Образование форм слов", hint: "Склонение, спряжение" },
      { type: 'quiz', question: "Лексические нормы — это:", options: ["Правила употребления слов", "Правила пунктуации", "Правила грамматики", "Правила произношения", "Правила написания"], correctAnswer: "Правила употребления слов", hint: "Правильное использование слов" },
      { type: 'quiz', question: "Орфографические нормы — это:", options: ["Правила лексики", "Правила написания", "Правила образования слов", "Правила пунктуации", "Правила произношения"], correctAnswer: "Правила написания", hint: "Орфография = написание" },
      { type: 'quiz', question: "Пунктуационные нормы — это:", options: ["Правила написания", "Правила лексики", "Правила расстановки знаков", "Правила грамматики", "Правила произношения"], correctAnswer: "Правила расстановки знаков", hint: "Пунктуация = знаки препинания" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Нормы языка»! 🎉" }
  },
  {
    title: "Изобразительные средства",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "«Золотые руки» — это:", options: ["Гипербола", "Сравнение", "Олицетворение", "Метафора", "Эпитет"], correctAnswer: "Метафора", hint: "Скрытое сравнение" },
      { type: 'quiz', question: "«Как лев, он был смел» — это:", options: ["Метафора", "Сравнение", "Эпитет", "Олицетворение", "Гипербола"], correctAnswer: "Сравнение", hint: "Сравнение с «как»" },
      { type: 'quiz', question: "«Шёпот листьев» — это:", options: ["Гипербола", "Сравнение", "Метафора", "Олицетворение", "Эпитет"], correctAnswer: "Олицетворение", hint: "Наделение неживого свойствами живого" },
      { type: 'quiz', question: "«Море слёз» — это:", options: ["Гипербола", "Эпитет", "Олицетворение", "Сравнение", "Метафора"], correctAnswer: "Гипербола", hint: "Преувеличение" },
      { type: 'quiz', question: "«Золотая осень» — это:", options: ["Сравнение", "Олицетворение", "Эпитет", "Гипербола", "Метафора"], correctAnswer: "Эпитет", hint: "Образное определение" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Изобразительные средства»! 🎉" }
  },
  {
    title: "Серебряный век",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Серебряный век — период:", options: ["XX века", "XIX века", "XVIII века", "Конца XIX — начала XX века", "XXI века"], correctAnswer: "Конца XIX — начала XX века", hint: "1890-1917 годы" },
      { type: 'quiz', question: "Поэт Серебряного века:", options: ["Блок", "Лермонтов", "Пушкин", "Крылов", "Некрасов"], correctAnswer: "Блок", hint: "Александр Блок" },
      { type: 'quiz', question: "Символизм — направление:", options: ["Модернистское", "Романтическое", "Классическое", "Реалистическое", "Сентиментальное"], correctAnswer: "Модернистское", hint: "Течение модернизма" },
      { type: 'quiz', question: "Акмеизм противопоставлялся:", options: ["Реализму", "Футуризму", "Символизму", "Романтизму", "Классицизму"], correctAnswer: "Символизму", hint: "Акмеисты отказались от символизма" },
      { type: 'quiz', question: "Есенин — поэт:", options: ["Постмодернизма", "Древней Руси", "Серебряного века", "Золотого века", "Советского периода"], correctAnswer: "Серебряного века", hint: "С.А. Есенин" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Серебряный век»! 🎉" }
  },
  {
    title: "Логарифмы",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "log₂8 = ?", options: ["8", "2", "3", "1", "4"], correctAnswer: "3", hint: "2³ = 8" },
      { type: 'quiz', question: "logₐa = ?", options: ["1", "a", "0", "10", "2"], correctAnswer: "1", hint: "a¹ = a" },
      { type: 'quiz', question: "logₐ1 = ?", options: ["1", "0", "-1", "10", "a"], correctAnswer: "0", hint: "a⁰ = 1" },
      { type: 'quiz', question: "log₂16 = ?", options: ["3", "8", "5", "4", "2"], correctAnswer: "4", hint: "2⁴ = 16" },
      { type: 'quiz', question: "log₁₀100 = ?", options: ["3", "2", "10", "1", "4"], correctAnswer: "2", hint: "10² = 100" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Логарифмы»! 🎉" }
  },
  {
    title: "Интеграл",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "∫x²dx = ?", options: ["x²/2 + C", "2x + C", "x³ + C", "x + C", "x³/3 + C"], correctAnswer: "x³/3 + C", hint: "∫xⁿdx = xⁿ⁺¹/(n+1)" },
      { type: 'quiz', question: "∫cos(x)dx = ?", options: ["-sin(x) + C", "sin(x) + C", "cos(x) + C", "tg(x) + C", "-cos(x) + C"], correctAnswer: "sin(x) + C", hint: "Производная синуса = косинус" },
      { type: 'quiz', question: "Формула Ньютона-Лейбница:", options: ["F(b)/F(a)", "F(a) - F(b)", "F(b) × F(a)", "F(a) + F(b)", "F(b) - F(a)"], correctAnswer: "F(b) - F(a)", hint: "Определённый интеграл через первообразную" },
      { type: 'quiz', question: "∫1dx = ?", options: ["C", "x + C", "x² + C", "0 + C", "1 + C"], correctAnswer: "x + C", hint: "Интеграл константы" },
      { type: 'quiz', question: "∫sin(x)dx = ?", options: ["-sin(x) + C", "cos(x) + C", "-cos(x) + C", "sin(x) + C", "tg(x) + C"], correctAnswer: "-cos(x) + C", hint: "Производная косинуса = -синус" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Интеграл»! 🎉" }
  },
  {
    title: "Тела вращения",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Объём цилиндра V = ?", options: ["(1/3)πr²h", "πr³", "2πrh", "πr²h", "4πr³"], correctAnswer: "πr²h", hint: "V = πr²h" },
      { type: 'quiz', question: "Объём конуса V = ?", options: ["πr²h", "2πr²h", "(1/2)πr²h", "(1/3)πr²h", "πr³"], correctAnswer: "(1/3)πr²h", hint: "V = 1/3 × πr²h" },
      { type: 'quiz', question: "Объём шара V = ?", options: ["(1/3)πr³", "(4/3)πr³", "2πr³", "πr³", "4πr²"], correctAnswer: "(4/3)πr³", hint: "V = 4/3 × πr³" },
      { type: 'quiz', question: "Цилиндр — вращение:", options: ["Полукруга", "Круга", "Прямоугольника", "Треугольника", "Трапеции"], correctAnswer: "Прямоугольника", hint: "Вокруг стороны" },
      { type: 'quiz', question: "Конус — вращение:", options: ["Прямоугольника", "Полукруга", "Треугольника", "Круга", "Трапеции"], correctAnswer: "Треугольника", hint: "Прямоугольного треугольника" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Тела вращения»! 🎉" }
  },
  {
    title: "Атомная физика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Кто открыл радиоактивность?", options: ["Кюри", "Бор", "Беккерель", "Резерфорд", "Эйнштейн"], correctAnswer: "Беккерель", hint: "Анри Беккерель, 1896" },
      { type: 'quiz', question: "Альфа-излучение — это:", options: ["Поток нейтронов", "Поток протонов", "Поток ядер гелия", "Поток электронов", "Электромагнитные волны"], correctAnswer: "Поток ядер гелия", hint: "α = ₂⁴He" },
      { type: 'quiz', question: "E = mc² — формула:", options: ["Эйнштейна", "Бора", "Ньютона", "Планка", "Резерфорда"], correctAnswer: "Эйнштейна", hint: "Эквивалентность массы и энергии" },
      { type: 'quiz', question: "Бета-излучение — это:", options: ["Электромагнитные волны", "Поток ядер гелия", "Поток протонов", "Поток электронов", "Поток нейтронов"], correctAnswer: "Поток электронов", hint: "β = электрон" },
      { type: 'quiz', question: "Ядро состоит из:", options: ["Только нейтронов", "Протонов и электронов", "Только протонов", "Нейтронов и электронов", "Протонов и нейтронов"], correctAnswer: "Протонов и нейтронов", hint: "Нуклоны = p + n" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Атомная физика»! 🎉" }
  },
  {
    title: "Химическая кинетика",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: "Скорость реакции измеряется в:", options: ["моль/(л·с)", "м/с", "кг/м³", "г/см³", "Дж/К"], correctAnswer: "моль/(л·с)", hint: "Изменение концентрации" },
      { type: 'quiz', question: "При повышении температуры скорость:", options: ["Случайно", "Уменьшается", "Сначала растёт, потом падает", "Увеличивается", "Не меняется"], correctAnswer: "Увеличивается", hint: "Правило Вант-Гоффа" },
      { type: 'quiz', question: "Катализатор:", options: ["Ускоряет, не расходуясь", "Увеличивает выход", "Замедляет", "Расходуется", "Не влияет"], correctAnswer: "Ускоряет, не расходуясь", hint: "Катализатор — помощник" },
      { type: 'quiz', question: "Фактор скорости:", options: ["Температура", "Форма сосуда", "Цвет вещества", "Масса сосуда", "Запах"], correctAnswer: "Температура", hint: "Температура влияет на скорость" },
      { type: 'quiz', question: "Обратимая реакция:", options: ["Только вперёд", "Не идёт", "Только назад", "Идёт в обоих направлениях", "Идёт случайно"], correctAnswer: "Идёт в обоих направлениях", hint: "⇌ обратимая" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Химическая кинетика»! 🎉" }
  },
  {
    title: "Вторая мировая война",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Когда началась Великая Отечественная война?", options: ["1943", "1940", "1941", "1939", "1942"], correctAnswer: "1941", hint: "22 июня 1941" },
      { type: 'quiz', question: "Битва под Москвой:", options: ["1942-1943", "1944", "1941-1942", "1943", "1945"], correctAnswer: "1941-1942", hint: "Первая победа над вермахтом" },
      { type: 'quiz', question: "Сталинградская битва:", options: ["1943-1944", "1942-1943", "1944", "1945", "1941"], correctAnswer: "1942-1943", hint: "Перелом в войне" },
      { type: 'quiz', question: "День Победы:", options: ["8 мая 1945", "9 мая 1945", "7 ноября 1945", "2 сентября 1945", "1 мая 1945"], correctAnswer: "9 мая 1945", hint: "9 мая — праздник" },
      { type: 'quiz', question: "Сколько длилась Великая Отечественная?", options: ["800 дней", "1418 дней", "1000 дней", "365 дней", "2000 дней"], correctAnswer: "1418 дней", hint: "Почти 4 года" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Вторая мировая война»! 🎉" }
  },
  {
    title: "Холодная война",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Холодная война началась после:", options: ["Второй мировой", "Крымской войны", "Революции 1917", "Первой мировой", "Наполеоновских войн"], correctAnswer: "Второй мировой", hint: "Противостояние СССР и США" },
      { type: 'quiz', question: "Фултонская речь Черчилля:", options: ["1948", "1947", "1950", "1945", "1946"], correctAnswer: "1946", hint: "Начало холодной войны" },
      { type: 'quiz', question: "Карибский кризис:", options: ["1955", "1965", "1962", "1960", "1970"], correctAnswer: "1962", hint: "Ядерный кризис" },
      { type: 'quiz', question: "Берлинская стена пала в:", options: ["1991", "1987", "1989", "1985", "1990"], correctAnswer: "1989", hint: "Символ окончания холодной войны" },
      { type: 'quiz', question: "Распад СССР:", options: ["1991", "1993", "1985", "1989", "1990"], correctAnswer: "1991", hint: "Декабрь 1991" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Холодная война»! 🎉" }
  },
  {
    title: "Право",
    subject: "Обществознание",
    icon: "Scale",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Конституция — это:", options: ["Постановление", "Обычный закон", "Указ президента", "Основной закон государства", "Приказ"], correctAnswer: "Основной закон государства", hint: "Высшая юридическая сила" },
      { type: 'quiz', question: "Правоспособность возникает с:", options: ["21 года", "16 лет", "18 лет", "14 лет", "Рождения"], correctAnswer: "Рождения", hint: "Способность иметь права" },
      { type: 'quiz', question: "Дееспособность в полном объёме с:", options: ["16 лет", "25 лет", "18 лет", "14 лет", "21 года"], correctAnswer: "18 лет", hint: "Совершеннолетие" },
      { type: 'quiz', question: "Право на жизнь — это:", options: ["Экономическое", "Естественное право", "Политическое", "Юридическое", "Социальное"], correctAnswer: "Естественное право", hint: "Принадлежит от рождения" },
      { type: 'quiz', question: "Высшая ценность по Конституции:", options: ["Собственность", "Государство", "Человек и его права", "Закон", "Порядок"], correctAnswer: "Человек и его права", hint: "Права человека — высшая ценность" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Право»! 🎉" }
  },
  {
    title: "Экономика",
    subject: "Обществознание",
    icon: "Scale",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Инфляция — это:", options: ["Стабильность", "Снижение цен", "Увеличение производства", "Повышение общего уровня цен", "Рост зарплат"], correctAnswer: "Повышение общего уровня цен", hint: "Обесценивание денег" },
      { type: 'quiz', question: "Спрос и предложение определяют:", options: ["Налоги", "Только предложение", "Рыночную цену", "Только спрос", "Зарплату"], correctAnswer: "Рыночную цену", hint: "Закон спроса и предложения" },
      { type: 'quiz', question: "Факторы производства:", options: ["Только деньги", "Только капитал", "Труд, земля, капитал, предпринимательство", "Только земля", "Только труд"], correctAnswer: "Труд, земля, капитал, предпринимательство", hint: "4 фактора" },
      { type: 'quiz', question: "Безработица — это:", options: ["Переутомление", "Отсутствие работы у трудоспособных", "Малая зарплата", "Длинный отпуск", "Наличие работы"], correctAnswer: "Отсутствие работы у трудоспособных", hint: "Экономическая проблема" },
      { type: 'quiz', question: "Налог — это:", options: ["Штраф", "Добровольный взнос", "Подарок", "Обязательный платёж государству", "Инвестиция"], correctAnswer: "Обязательный платёж государству", hint: "Обязательный платёж" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Экономика»! 🎉" }
  },
  {
    title: "Экология",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Экология изучает:", options: ["Атомы", "Звёзды", "Молекулы", "Взаимоотношения организмов", "Клетки"], correctAnswer: "Взаимоотношения организмов", hint: "Связи в природе" },
      { type: 'quiz', question: "Пищевая цепь начинается с:", options: ["Разлагателей", "Производителей", "Хищников", "Паразитов", "Симбионтов"], correctAnswer: "Производителей", hint: "Растения — производители" },
      { type: 'quiz', question: "Биосфера — это:", options: ["Гидросфера", "Атмосфера", "Часть Земли с жизнью", "Литосфера", "Магнитосфера"], correctAnswer: "Часть Земли с жизнью", hint: "По Вернадскому" },
      { type: 'quiz', question: "Автор учения о биосфере:", options: ["Дарвин", "Вернадский", "Павлов", "Менделеев", "Ломоносов"], correctAnswer: "Вернадский", hint: "В.И. Вернадский" },
      { type: 'quiz', question: "Красная книга содержит:", options: ["Редкие и исчезающие виды", "Опасные виды", "Ископаемые", "Все виды", "Домашние виды"], correctAnswer: "Редкие и исчезающие виды", hint: "Охрана природы" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Экология»! 🎉" }
  },
  {
    title: "География России",
    subject: "География",
    icon: "Map",
    color: "text-teal-400",
    tasks: [
      { type: 'quiz', question: "Самая длинная река России:", options: ["Енисей", "Лена", "Амур", "Обь (с Иртышом)", "Волга"], correctAnswer: "Обь (с Иртышом)", hint: "Обь + Иртыш = 5410 км" },
      { type: 'quiz', question: "Самое глубокое озеро:", options: ["Онежское", "Телецкое", "Байкал", "Ладожское", "Каспийское"], correctAnswer: "Байкал", hint: "1642 м глубина" },
      { type: 'quiz', question: "Россия граничит с:", options: ["10", "14", "12", "18 странами", "20"], correctAnswer: "18 странами", hint: "Самое большое число границ" },
      { type: 'quiz', question: "Самая высокая гора России:", options: ["Эльбрус", "Народная", "Белуха", "Казбек", "Мунку-Сардык"], correctAnswer: "Эльбрус", hint: "5642 м" },
      { type: 'quiz', question: "Площадь России:", options: ["10 млн", "20 млн", "17.1 млн км²", "12 млн", "15 млн"], correctAnswer: "17.1 млн км²", hint: "Крупнейшая страна" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «География России»! 🎉" }
  },
  {
    title: "Reported Speech",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "«I am happy» → He said he __ happy.", options: ["was", "were", "is", "will be", "has been"], correctAnswer: "was", hint: "Present → Past" },
      { type: 'quiz', question: "«I will come» → She said she __ come.", options: ["would", "will", "could", "can", "should"], correctAnswer: "would", hint: "Will → would" },
      { type: 'quiz', question: "«I can swim» → He said he __ swim.", options: ["could", "will", "should", "can", "must"], correctAnswer: "could", hint: "Can → could" },
      { type: 'quiz', question: "«Don't go!» → She told me:", options: ["not to go", "no go", "not go", "to not go", "don't go"], correctAnswer: "not to go", hint: "Повелительное → инфинитив с not" },
      { type: 'quiz', question: "«I saw him» → She said she __ seen him.", options: ["had", "has", "have", "did", "was"], correctAnswer: "had", hint: "Past → Past Perfect" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Reported Speech»! 🎉" }
  },
  {
    title: "Conditionals",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "If I __ (study), I will pass.", options: ["studies", "study", "will study", "studied", "studying"], correctAnswer: "study", hint: "First: If + Present, will + V" },
      { type: 'quiz', question: "If I __ (be) rich, I would travel.", options: ["will be", "were", "was", "be", "am"], correctAnswer: "were", hint: "Second: If + Past, would + V" },
      { type: 'quiz', question: "If I __ (know), I would have helped.", options: ["would know", "have known", "know", "knew", "had known"], correctAnswer: "had known", hint: "Third: If + Past Perfect, would have + V3" },
      { type: 'quiz', question: "Zero conditional: If you heat water, it ___.", options: ["would boil", "boil", "will boil", "boils", "boiled"], correctAnswer: "boils", hint: "Zero: If + Present, Present" },
      { type: 'quiz', question: "Mixed: If I __ (study) yesterday, I would pass now.", options: ["study", "studied", "have studied", "would study", "had studied"], correctAnswer: "had studied", hint: "Past Perf + would + V" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Conditionals»! 🎉" }
  },
  {
    title: "Основы информатики",
    subject: "Информатика",
    icon: "Monitor",
    color: "text-sky-400",
    tasks: [
      { type: 'quiz', question: "1 байт = ?", options: ["4 бита", "16 бит", "8 бит", "2 бита", "10 бит"], correctAnswer: "8 бит", hint: "1 байт = 8 бит" },
      { type: 'quiz', question: "Двоичная система использует цифры:", options: ["0-2", "0 и 1", "0-F", "0-9", "0-7"], correctAnswer: "0 и 1", hint: "Бинарная система" },
      { type: 'quiz', question: "Алгоритм — это:", options: ["Рисунок", "Уравнение", "Формула", "Порядок действий", "Таблица"], correctAnswer: "Порядок действий", hint: "Чёткая последовательность" },
      { type: 'quiz', question: "Переменная — это:", options: ["Функция", "Именованное хранилище данных", "Массив", "Цикл", "Условие"], correctAnswer: "Именованное хранилище данных", hint: "Хранит значение" },
      { type: 'quiz', question: "HTTP — это:", options: ["Операционная система", "Протокол передачи данных", "Графический редактор", "База данных", "Язык программирования"], correctAnswer: "Протокол передачи данных", hint: "Для веб-страниц" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Основы информатики»! 🎉" }
  },
  {
    title: "Спорт",
    subject: "Физкультура",
    icon: "Dumbbell",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Футбол играют:", options: ["Без мяча", "Клюшкой", "Ногами и мячом ⚽", "Ракеткой", "Руками"], correctAnswer: "Ногами и мячом ⚽", hint: "Футбол — ногами!" },
      { type: 'quiz', question: "Сколько игроков в команде по футболу?", options: ["9", "11", "7", "5", "6"], correctAnswer: "11", hint: "11 на поле" },
      { type: 'quiz', question: "Что полезно для здоровья?", options: ["Сидеть весь день", "Не спать", "Мало двигаться", "Есть конфеты", "Зарядка"], correctAnswer: "Зарядка", hint: "Движение — жизнь!" },
      { type: 'quiz', question: "Баскетбол играют:", options: ["Клюшкой", "Ракеткой", "Без мяча", "Руками и мячом 🏀", "Ногами"], correctAnswer: "Руками и мячом 🏀", hint: "Забрасываем в кольцо" },
      { type: 'quiz', question: "Сколько раз в неделю нужно заниматься спортом?", options: ["2", "3-4", "1", "0", "7"], correctAnswer: "3-4", hint: "Регулярность важна" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Спорт»! 🎉" }
  },
  {
    title: "Безопасность",
    subject: "ОБЖ",
    icon: "Shield",
    color: "text-slate-400",
    tasks: [
      { type: 'quiz', question: "При пожаре нужно звонить:", options: ["102", "104", "103", "101", "112"], correctAnswer: "101", hint: "Пожарная служба" },
      { type: 'quiz', question: "Скорая помощь:", options: ["112", "101", "104", "102", "103"], correctAnswer: "103", hint: "Медицинская помощь" },
      { type: 'quiz', question: "Полиция:", options: ["101", "104", "102", "112", "103"], correctAnswer: "102", hint: "Полицейская служба" },
      { type: 'quiz', question: "Единый номер экстренной помощи:", options: ["101", "112", "102", "104", "103"], correctAnswer: "112", hint: "Единый номер" },
      { type: 'quiz', question: "При пожаре НЕЛЬЗЯ:", options: ["Идти к выходу", "Прятаться", "Дышать через влажную ткань", "Звонить 101", "Эвакуироваться"], correctAnswer: "Прятаться", hint: "Нельзя прятаться!" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Безопасность»! 🎉" }
  },
]
