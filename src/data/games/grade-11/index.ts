// Экспорт игр для 11 класса
import { GameLesson } from '../types'

export const eleventhGradeGames: GameLesson[] = [
  // ========== АЛГЕБРА ==========
  {
    title: "Интеграл",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Интеграл - это:", options: ["Производная", "Первообразная", "Скорость", "Лимит", "Матрица"], correctAnswer: "Первообразная", hint: "Интегрирование - операция, обратная дифференцированию" },
      { type: 'fill', question: "∫x²dx = x³/__ + C", correctAnswer: "3", hint: "∫xⁿdx = xⁿ⁺¹/(n+1)" },
      { type: 'quiz', question: "∫cos(x)dx = ?", options: ["sin(x) + C", "-sin(x) + C", "cos(x) + C", "tg(x) + C", "-cos(x) + C"], correctAnswer: "sin(x) + C", hint: "Производная синуса - косинус" },
      { type: 'quiz', question: "Формула Ньютона-Лейбница:", options: ["∫ᵃᵇf(x)dx = F(b) - F(a)", "∫ᵃᵇf(x)dx = F(a) - F(b)", "∫ᵃᵇf(x)dx = F(a) + F(b)", "∫ᵃᵇf(x)dx = F(b) + F(a)", "∫ᵃᵇf(x)dx = F(a) × F(b)"], correctAnswer: "∫ᵃᵇf(x)dx = F(b) - F(a)", hint: "Определённый интеграл через первообразную" },
      { type: 'fill', question: "∫sin(x)dx = -__ + C", correctAnswer: "cos(x)", hint: "Производная косинуса = -sin(x)" }
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь интегралы! 📐" }
  },
  {
    title: "Логарифмы",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'fill', question: "log₂8 = __ (2 в какой степени = 8?)", correctAnswer: "3", hint: "2³ = 8" },
      { type: 'quiz', question: "logₐa = ?", options: ["0", "1", "a", "1/a", "a²"], correctAnswer: "1", hint: "a¹ = a" },
      { type: 'quiz', question: "logₐ1 = ?", options: ["0", "1", "a", "-1", "∞"], correctAnswer: "0", hint: "a⁰ = 1" },
      { type: 'quiz', question: "logₐ(xy) = ?", options: ["logₐx + logₐy", "logₐx · logₐy", "logₐx - logₐy", "logₐx / logₐy", "(logₐx)ᵧ"], correctAnswer: "logₐx + logₐy", hint: "Логарифм произведения = сумма логарифмов" },
      { type: 'quiz', question: "logₐ(x/y) = ?", options: ["logₐx + logₐy", "logₐx - logₐy", "logₐx · logₐy", "logₐy - logₐx", "logₐ(x·y)"], correctAnswer: "logₐx - logₐy", hint: "Логарифм частного = разность логарифмов" }
    ],
    reward: { stars: 3, message: "Супер! Ты работаешь с логарифмами! 🔢" }
  },
  {
    title: "Комплексные числа",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "i² = ?", options: ["-1", "1", "0", "i", "-i"], correctAnswer: "-1", hint: "i = √(-1), i² = -1" },
      { type: 'fill', question: "(3 + 2i) + (1 + 4i) = __ + 6i", correctAnswer: "4", hint: "Складываем действительные части: 3 + 1" },
      { type: 'quiz', question: "Мнимая единица i = ?", options: ["√1", "√(-1)", "√0", "√2", "-√1"], correctAnswer: "√(-1)", hint: "i = √(-1)" },
      { type: 'quiz', question: "Комплексное число a + bi содержит:", options: ["Только действительную часть", "Только мнимую часть", "Обе части", "Ни одной", "Только ноль"], correctAnswer: "Обе части", hint: "a - действительная, bi - мнимая часть" },
      { type: 'fill', question: "Модуль комплексного числа |3 + 4i| = __", correctAnswer: "5", hint: "|a + bi| = √(a² + b²) = √(9 + 16) = 5" }
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь комплексные числа! 📊" }
  },

  // ========== ГЕОМЕТРИЯ ==========
  {
    title: "Тела вращения",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Цилиндр получается вращением:", options: ["Треугольника", "Прямоугольника", "Круга", "Квадрата", "Ромба"], correctAnswer: "Прямоугольника", hint: "Вращение прямоугольника вокруг стороны" },
      { type: 'fill', question: "Объём цилиндра V = πr²h. Если r=2, h=5, то V = __π", correctAnswer: "20", hint: "V = π · 4 · 5 = 20π" },
      { type: 'quiz', question: "Конус получается вращением:", options: ["Прямоугольника", "Треугольника", "Круга", "Квадрата", "Трапеции"], correctAnswer: "Треугольника", hint: "Вращение прямоугольного треугольника" },
      { type: 'quiz', question: "Объём конуса:", options: ["πr²h", "(1/3)πr²h", "(4/3)πr³", "2πr²h", "(1/2)πr²h"], correctAnswer: "(1/3)πr²h", hint: "V = 1/3 · πr² · h" },
      { type: 'fill', question: "Площадь поверхности шара S = 4πr². Если r=3, то S = __π", correctAnswer: "36", hint: "S = 4π · 9 = 36π" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тела вращения! ⭕" }
  },
  {
    title: "Координаты и векторы в пространстве",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'fill', question: "Расстояние между точками A(0,0,0) и B(3,4,0) = __", correctAnswer: "5", hint: "√(3² + 4² + 0²) = 5" },
      { type: 'quiz', question: "Скалярное произведение векторов a·b = ?", options: ["|a| × |b|", "|a| × |b| × cos α", "|a| + |b|", "|a| - |b|", "|a| / |b|"], correctAnswer: "|a| × |b| × cos α", hint: "Через модули и косинус угла" },
      { type: 'fill', question: "Вектор a(1,2,3), вектор b(2,1,1). a·b = __", correctAnswer: "7", hint: "1·2 + 2·1 + 3·1 = 7" },
      { type: 'quiz', question: "Если скалярное произведение = 0, то векторы:", options: ["Коллинеарны", "Перпендикулярны", "Равны", "Противоположны", "Совпадают"], correctAnswer: "Перпендикулярны", hint: "a·b = 0 → cos 90° = 0" },
      { type: 'fill', question: "Вектор a(1,0,0), модуль |a| = __", correctAnswer: "1", hint: "|a| = √(1² + 0² + 0²) = 1" }
    ],
    reward: { stars: 3, message: "Супер! Ты работаешь в пространстве! 📏" }
  },

  // ========== РУССКИЙ ЯЗЫК ==========
  {
    title: "Нормы языка",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Орфоэпические нормы - это:", options: ["Правила написания", "Правила произношения", "Правила образования слов", "Правила пунктуации", "Правила лексики"], correctAnswer: "Правила произношения", hint: "Орфоэпия = произношение" },
      { type: 'quiz', question: "Грамматические нормы регулируют:", options: ["Произношение", "Образование форм слов", "Написание", "Ударение", "Перевод"], correctAnswer: "Образование форм слов", hint: "Склонение, спряжение" },
      { type: 'find', question: "Выбери языковые нормы:", options: ["Орфоэпические", "Лексические", "Грамматические", "Математические", "Физические"], correctAnswer: ["Орфоэпические", "Лексические", "Грамматические"], hint: "Основные нормы литературного языка" },
      { type: 'quiz', question: "Лексические нормы - это:", options: ["Правила произношения", "Правила употребления слов", "Правила написания", "Правила ударения", "Правила перевода"], correctAnswer: "Правила употребления слов", hint: "Правильное использование слов" },
      { type: 'quiz', question: "Орфографические нормы регулируют:", options: ["Произношение", "Написание слов", "Образование форм", "Употребление слов", "Пунктуацию"], correctAnswer: "Написание слов", hint: "Орфография = правила написания" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь нормы языка! 📝" }
  },

  // ========== ЛИТЕРАТУРА ==========
  {
    title: "Серебряный век",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Серебряный век - это период:", options: ["XIX века", "Конца XIX - начала XX века", "XX века", "XVIII века", "Начала XXI века"], correctAnswer: "Конца XIX - начала XX века", hint: "1890-1917 годы" },
      { type: 'find', question: "Выбери поэтов Серебряного века:", options: ["Блок", "Есенин", "Маяковский", "Пушкин", "Ахматова"], correctAnswer: ["Блок", "Есенин", "Маяковский", "Ахматова"], hint: "Поэты рубежа XIX-XX веков" },
      { type: 'quiz', question: "Символизм - это направление:", options: ["Реалистическое", "Модернистское", "Классическое", "Романтическое", "Сентиментальное"], correctAnswer: "Модернистское", hint: "Символизм - течение модернизма" },
      { type: 'quiz', question: "Акмеизм противопоставлялся:", options: ["Реализму", "Символизму", "Классицизму", "Романтизму", "Натурализму"], correctAnswer: "Символизму", hint: "Акмеисты отказались от символизма" },
      { type: 'quiz', question: "Александр Блок - представитель:", options: ["Реализма", "Символизма", "Акмеизма", "Футуризма", "Классицизма"], correctAnswer: "Символизма", hint: "Блок - ведущий символист" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь Серебряный век! 📖" }
  },
  {
    title: "Литература XX века",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "М.А. Булгаков написал:", options: ["Тихий Дон", "Мастер и Маргарита", "Доктор Живаго", "Война и мир", "Отцы и дети"], correctAnswer: "Мастер и Маргарита", hint: "Роман о любви и творчестве" },
      { type: 'find', question: "Выбери писателей XX века:", options: ["Шолохов", "Пастернак", "Булгаков", "Толстой", "Солженицын"], correctAnswer: ["Шолохов", "Пастернак", "Булгаков", "Солженицын"], hint: "Русская литература XX века" },
      { type: 'quiz', question: "«Тихий Дон» - автор:", options: ["Булгаков", "Шолохов", "Пастернак", "Толстой", "Горький"], correctAnswer: "Шолохов", hint: "Шолохов - нобелевский лауреат" },
      { type: 'quiz', question: "«Доктор Живаго» - автор:", options: ["Булгаков", "Шолохов", "Пастернак", "Есенин", "Маяковский"], correctAnswer: "Пастернак", hint: "Пастернак - нобелевский лауреат" },
      { type: 'quiz', question: "«Один день Ивана Денисовича» - автор:", options: ["Булгаков", "Шолохов", "Пастернак", "Солженицын", "Горький"], correctAnswer: "Солженицын", hint: "А.И. Солженицын" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь литературу XX века! 📚" }
  },

  // ========== ИСТОРИЯ ==========
  {
    title: "Холодная война",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "«Холодная война» началась после:", options: ["Первой мировой", "Второй мировой", "Революции 1917", "Крымской войны", "Наполеоновских войн"], correctAnswer: "Второй мировой", hint: "Противостояние СССР и США" },
      { type: 'quiz', question: "Фултонская речь Черчилля:", options: ["1945", "1946", "1947", "1948", "1950"], correctAnswer: "1946", hint: "1946 год - начало «холодной войны»" },
      { type: 'find', question: "Выбери события «холодной войны»:", options: ["Карибский кризис", "Берлинская стена", "Вторая мировая", "Война во Вьетнаме", "Первая мировая"], correctAnswer: ["Карибский кризис", "Берлинская стена", "Война во Вьетнаме"], hint: "Глобальное противостояние" },
      { type: 'quiz', question: "Карибский кризис:", options: ["1960", "1962", "1965", "1970", "1958"], correctAnswer: "1962", hint: "1962 год - ядерный кризис" },
      { type: 'quiz', question: "НАТО создана в:", options: ["1945", "1949", "1955", "1960", "1947"], correctAnswer: "1949", hint: "Североатлантический альянс" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь историю! ⚔️" }
  },
  {
    title: "Распад СССР",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Когда был распад СССР?", options: ["1989", "1991", "1993", "1990", "1995"], correctAnswer: "1991", hint: "Декабрь 1991 года" },
      { type: 'quiz', question: "Первый президент России:", options: ["Горбачёв", "Ельцин", "Путин", "Кравчук", "Назарбаев"], correctAnswer: "Ельцин", hint: "Б.Н. Ельцин - первый президент РФ" },
      { type: 'find', question: "Выбери события перестройки:", options: ["Гласность", "Ускорение", "Коллективизация", "Демократизация", "Индустриализация"], correctAnswer: ["Гласность", "Ускорение", "Демократизация"], hint: "Политика Горбачёва" },
      { type: 'quiz', question: "Последний лидер СССР:", options: ["Ельцин", "Горбачёв", "Андропов", "Брежнев", "Хрущёв"], correctAnswer: "Горбачёв", hint: "М.С. Горбачёв - последний генсек" },
      { type: 'fill', question: "Беловежское соглашение о распаде СССР подписано в __ году", correctAnswer: "1991", hint: "8 декабря 1991 года" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь новейшую историю! 🏛️" }
  },

  // ========== ФИЗИКА ==========
  {
    title: "Атомная физика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Кто открыл радиоактивность?", options: ["Резерфорд", "Беккерель", "Кюри", "Томсон", "Бор"], correctAnswer: "Беккерель", hint: "Анри Беккерель, 1896" },
      { type: 'quiz', question: "Альфа-излучение - это:", options: ["Поток электронов", "Поток ядер гелия", "Электромагнитные волны", "Поток протонов", "Поток нейтронов"], correctAnswer: "Поток ядер гелия", hint: "α = ₂⁴He" },
      { type: 'find', question: "Выбери виды радиоактивного распада:", options: ["Альфа-распад", "Бета-распад", "Гамма-излучение", "Дельта-распад", "Сигма-распад"], correctAnswer: ["Альфа-распад", "Бета-распад", "Гамма-излучение"], hint: "Три основных вида" },
      { type: 'quiz', question: "Формула Эйнштейна E = ?", options: ["mc", "mc²", "m²c", "m/c²", "2mc"], correctAnswer: "mc²", hint: "E = mc² - энергия и масса эквивалентны" },
      { type: 'quiz', question: "Планетарная модель атома предложена:", options: ["Резерфордом", "Бором", "Томсоном", "Эйнштейном", "Планком"], correctAnswer: "Резерфордом", hint: "Опыт Резерфорда по рассеянию альфа-частиц" }
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь атомную физику! ⚛️" }
  },
  {
    title: "Квантовая физика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Квант - это:", options: ["Волна", "Порция энергии", "Частица", "Поле", "Сила"], correctAnswer: "Порция энергии", hint: "E = hν - энергия кванта" },
      { type: 'quiz', question: "Постоянная Планка обозначается:", options: ["c", "h", "ν", "λ", "f"], correctAnswer: "h", hint: "h ≈ 6.63 × 10⁻³⁴ Дж·с" },
      { type: 'fill', question: "E = hν, где ν - это __ (частота)", correctAnswer: "частота", hint: "Греческая буква ню" },
      { type: 'quiz', question: "Фотоэффект открыл:", options: ["Эйнштейн", "Столетов", "Планк", "Бор", "Резерфорд"], correctAnswer: "Столетов", hint: "А.Г. Столетов изучал фотоэффект" },
      { type: 'quiz', question: "Корпускулярно-волновой дуализм означает:", options: ["Частица = волна", "Свет - и частица, и волна", "Только волна", "Только частица", "Ничего из этого"], correctAnswer: "Свет - и частица, и волна", hint: "Свет проявляет обе природы" }
    ],
    reward: { stars: 3, message: "Супер! Ты понимаешь квантовую физику! 🔬" }
  },

  // ========== ХИМИЯ ==========
  {
    title: "Химическая кинетика",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: "Скорость химической реакции измеряется в:", options: ["моль/л·с", "г/см³", "м/с", "Дж", "Па"], correctAnswer: "моль/л·с", hint: "Изменение концентрации в единицу времени" },
      { type: 'quiz', question: "При повышении температуры скорость реакции:", options: ["Уменьшается", "Увеличивается", "Не меняется", "Обнуляется", "Инвертируется"], correctAnswer: "Увеличивается", hint: "Правило Вант-Гоффа" },
      { type: 'find', question: "Выбери факторы, влияющие на скорость:", options: ["Температура", "Концентрация", "Катализатор", "Давление", "Объём"], correctAnswer: ["Температура", "Концентрация", "Катализатор", "Давление"], hint: "Факторы скорости реакции" },
      { type: 'quiz', question: "Катализатор:", options: ["Расходуется в реакции", "Не расходуется", "Замедляет реакцию", "Изменяет продукты", "Является продуктом"], correctAnswer: "Не расходуется", hint: "Катализатор ускоряет, но не расходуется" },
      { type: 'fill', question: "Закон действующих масс: скорость пропорциональна __ реагентов", correctAnswer: "концентрации", hint: "v = k · [A] · [B]" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь кинетику! 🧪" }
  },

  // ========== БИОЛОГИЯ ==========
  {
    title: "Экология",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Экология изучает:", options: ["Клетки", "Взаимоотношения организмов", "Молекулы", "Атомы", "Звёзды"], correctAnswer: "Взаимоотношения организмов", hint: "Экология - наука о связях в природе" },
      { type: 'find', question: "Выбери уровни организации жизни:", options: ["Клеточный", "Организменный", "Популяционный", "Молекулярный", "Биосферный"], correctAnswer: ["Клеточный", "Организменный", "Популяционный", "Биосферный"], hint: "Уровни организации живого" },
      { type: 'quiz', question: "Пищевая цепь начинается с:", options: ["Хищников", "Производителей", "Разлагателей", "Паразитов", "Симбионтов"], correctAnswer: "Производителей", hint: "Растения - производители" },
      { type: 'quiz', question: "Биосфера - это:", options: ["Часть Земли с жизнью", "Атмосфера", "Гидросфера", "Литосфера", "Тропосфера"], correctAnswer: "Часть Земли с жизнью", hint: "По Вернадскому - оболочка Земли с жизнью" },
      { type: 'fill', question: "Правило экологической пирамиды: на каждом уровне __ в 10 раз", correctAnswer: "энергии", hint: "Переход энергии между уровнями" }
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь экологию! 🌿" }
  },

  // ========== АНГЛИЙСКИЙ ==========
  {
    title: "Academic English",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Essay structure includes:", options: ["Introduction, Body, Conclusion", "Only Body", "Introduction only", "Only Conclusion", "Title and Author"], correctAnswer: "Introduction, Body, Conclusion", hint: "Три части эссе" },
      { type: 'find', question: "Выбери linking words:", options: ["However", "Therefore", "Moreover", "Beautiful", "Quickly"], correctAnswer: ["However", "Therefore", "Moreover"], hint: "Слова-связки для эссе" },
      { type: 'quiz', question: "«In conclusion» используется:", options: ["В начале", "В конце", "В середине", "В заголовке", "В примечании"], correctAnswer: "В конце", hint: "In conclusion = в заключение" },
      { type: 'fill', question: "On the one hand... on the __ hand...", correctAnswer: "other", hint: "С одной стороны... с другой стороны" },
      { type: 'quiz', question: "«Furthermore» means:", options: ["Однако", "Кроме того", "Поэтому", "Наконец", "В результате"], correctAnswer: "Кроме того", hint: "Furthermore = additionally" }
    ],
    reward: { stars: 3, message: "Excellent! Ты готов к академическому английскому! 🇬🇧" }
  },
  {
    title: "Phrasal Verbs",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "«Give up» means:", options: ["Start", "Stop trying", "Continue", "Begin", "Finish"], correctAnswer: "Stop trying", hint: "Give up = бросить, отказаться" },
      { type: 'quiz', question: "«Look after» means:", options: ["Search", "Take care of", "Watch", "Find", "Ignore"], correctAnswer: "Take care of", hint: "Look after = присматривать" },
      { type: 'find', question: "Выбери фразовые глаголы:", options: ["Look up", "Go on", "Turn off", "Beautiful house", "Very quickly"], correctAnswer: ["Look up", "Go on", "Turn off"], hint: "Фразовые глаголы = глагол + предлог" },
      { type: 'fill', question: "Turn __ the light, please. (off/on)", correctAnswer: "off", hint: "Turn off = выключить" },
      { type: 'quiz', question: "«Take off» means:", options: ["Надеть", "Снять", "Положить", "Взять", "Убрать"], correctAnswer: "Снять", hint: "Take off = снять (одежду)" }
    ],
    reward: { stars: 3, message: "Great! Ты знаешь фразовые глаголы! 🔄" }
  },

  // ========== НОВЫЕ ИГРЫ ==========
  {
    title: "Определённый интеграл",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'fill', question: "∫₀² x dx = __ (по формуле Ньютона-Лейбница)", correctAnswer: "2", hint: "x²/2 от 0 до 2 = 4/2 - 0 = 2" },
      { type: 'quiz', question: "Площадь под графиком f(x) от a до b:", options: ["f(b) - f(a)", "∫ₐᵇ f(x)dx", "f'(x)", "f(a) + f(b)", "f(b) / f(a)"], correctAnswer: "∫ₐᵇ f(x)dx", hint: "Определённый интеграл = площадь" },
      { type: 'fill', question: "∫₀¹ 2x dx = __", correctAnswer: "1", hint: "x² от 0 до 1 = 1 - 0 = 1" },
      { type: 'quiz', question: "Интеграл от константы C:", options: ["Cx + C", "C", "Cx", "Cx² + C", "C/x + C"], correctAnswer: "Cx + C", hint: "∫C dx = Cx + C₁" },
      { type: 'fill', question: "∫₀³ x² dx = __ (x³/3 от 0 до 3)", correctAnswer: "9", hint: "27/3 - 0 = 9" }
    ],
    reward: { stars: 3, message: "Отлично! Ты работаешь с интегралами! 📐" }
  },
  {
    title: "Дифференциальные уравнения",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Дифференциальное уравнение содержит:", options: ["Только функцию", "Функцию и её производные", "Только производные", "Только константы", "Только интегралы"], correctAnswer: "Функцию и её производные", hint: "Уравнение с производными" },
      { type: 'quiz', question: "Решение y' = kx:", options: ["y = kx", "y = kx²/2 + C", "y = k", "y = kx + C", "y = k/x"], correctAnswer: "y = kx²/2 + C", hint: "Интегрируем обе части" },
      { type: 'fill', question: "y' = 5, тогда y = 5x + __", correctAnswer: "C", hint: "Произвольная постоянная" },
      { type: 'quiz', question: "Порядок дифференциального уравнения определяется:", options: ["Старшей степенью", "Старшей производной", "Количеством переменных", "Количеством констант", "Количеством корней"], correctAnswer: "Старшей производной", hint: "Порядок = наивысший порядок производной" },
      { type: 'quiz', question: "Дифференциальное уравнение первого порядка содержит:", options: ["Только y''", "y' (первую производную)", "y'''", "Интегралы", "Логарифмы"], correctAnswer: "y' (первую производную)", hint: "Наивысшая производная - первого порядка" }
    ],
    reward: { stars: 3, message: "Супер! Ты понимаешь дифференциальные уравнения! 🔢" }
  },
  {
    title: "Оптика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Закон преломления света:", options: ["sin α = sin β", "sin α / sin β = n", "α = β", "cos α = cos β", "tg α = tg β"], correctAnswer: "sin α / sin β = n", hint: "Закон Снеллиуса" },
      { type: 'fill', question: "Угол падения __ углу отражения", correctAnswer: "равен", hint: "Закон отражения" },
      { type: 'quiz', question: "Показатель преломления стекла:", options: ["≈ 1", "≈ 1.5", "≈ 2", "≈ 0.5", "≈ 3"], correctAnswer: "≈ 1.5", hint: "Стекло преломляет свет" },
      { type: 'find', question: "Выбери оптические явления:", options: ["Преломление", "Отражение", "Дифракция", "Испарение", "Интерференция"], correctAnswer: ["Преломление", "Отражение", "Дифракция", "Интерференция"], hint: "Явления, связанные со светом" },
      { type: 'fill', question: "Полное внутреннее отражение происходит при переходе из оптически более __ среды", correctAnswer: "плотной", hint: "Из среды с большим n в среду с меньшим n" }
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь оптику! 💡" }
  },
  {
    title: "Ядерная физика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Ядро состоит из:", options: ["Протонов и электронов", "Протонов и нейтронов", "Только протонов", "Только нейтронов", "Протонов, нейтронов и электронов"], correctAnswer: "Протонов и нейтронов", hint: "Нуклоны = протоны + нейтроны" },
      { type: 'fill', question: "Массовое число A = Z + N, где Z - протоны, N - __", correctAnswer: "нейтроны", hint: "N = количество нейтронов" },
      { type: 'quiz', question: "Альфа-распад:", options: ["Вылет электрона", "Вылет ядра гелия", "Вылет нейтрона", "Вылет протона", "Вылет позитрона"], correctAnswer: "Вылет ядра гелия", hint: "₂⁴He" },
      { type: 'quiz', question: "Бета-распад:", options: ["Вылет электрона", "Вылет ядра гелия", "Вылет протона", "Вылет нейтрона", "Вылет альфа-частицы"], correctAnswer: "Вылет электрона", hint: "Превращение нейтрона в протон" },
      { type: 'fill', question: "При альфа-распаде массовое число уменьшается на __", correctAnswer: "4", hint: "Альфа-частица ₂⁴He имеет массу 4" }
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь ядерную физику! ⚛️" }
  },
  {
    title: "Общая химия",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: "Окислительно-восстановительные реакции:", options: ["Без изменения степеней", "С изменением степеней окисления", "Только с кислородом", "Только с водородом", "Только при нагревании"], correctAnswer: "С изменением степеней окисления", hint: "ОВР = передача электронов" },
      { type: 'find', question: "Выбери окислители:", options: ["O₂", "H₂", "KMnO₄", "Na", "Cl₂"], correctAnswer: ["O₂", "KMnO₄", "Cl₂"], hint: "Окислители принимают электроны" },
      { type: 'fill', question: "В реакции Zn + 2HCl → ZnCl₂ + H₂ окислитель - __", correctAnswer: "HCl", hint: "Водород принимает электроны" },
      { type: 'quiz', question: "Электролиз - это:", options: ["Разложение током", "Нагревание", "Окисление", "Восстановление", "Фильтрование"], correctAnswer: "Разложение током", hint: "Незапланированное разложение вещества током" },
      { type: 'quiz', question: "Восстановитель - это вещество, которое:", options: ["Принимает электроны", "Отдаёт электроны", "Не участвует в реакции", "Является катализатором", "Растворяется"], correctAnswer: "Отдаёт электроны", hint: "Восстановитель окисляется" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь химию! 🧪" }
  },
  {
    title: "Биосфера и экология",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Автор учения о биосфере:", options: ["Дарвин", "Вернадский", "Менделеев", "Линней", "Ламарк"], correctAnswer: "Вернадский", hint: "В.И. Вернадский" },
      { type: 'find', question: "Выбери функции биосферы:", options: ["Газовая", "Концентрационная", "Окислительная", "Механическая", "Биохимическая"], correctAnswer: ["Газовая", "Концентрационная", "Окислительная", "Биохимическая"], hint: "Функции живого вещества" },
      { type: 'quiz', question: "Красная книга содержит:", options: ["Все виды", "Редкие и исчезающие виды", "Опасные виды", "Исследованные виды", "Вымершие виды"], correctAnswer: "Редкие и исчезающие виды", hint: "Охрана природы" },
      { type: 'fill', question: "Биосфера - оболочка Земли, заселённая __ организмами", correctAnswer: "живыми", hint: "Сфера жизни" },
      { type: 'quiz', question: "Ноосфера - это:", options: ["Сфера разума", "Сфера воды", "Сфера воздуха", "Сфера камня", "Сфера огня"], correctAnswer: "Сфера разума", hint: "Понятие Вернадского - сфера, преобразованная разумом" }
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь экологию! 🌍" }
  },
  {
    title: "Россия в 90-е годы",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Конституция 1993 года принята:", options: ["12 декабря", "12 июня", "7 ноября", "1 января", "9 мая"], correctAnswer: "12 декабря", hint: "День Конституции" },
      { type: 'find', question: "Выбери события 90-х:", options: ["Приватизация", "Дефолт 1998", "Крым 2014", "Чеченские войны", "Олимпиада 2014"], correctAnswer: ["Приватизация", "Дефолт 1998", "Чеченские войны"], hint: "Россия в переходный период" },
      { type: 'quiz', question: "Приватизация в России началась в:", options: ["1990", "1992", "1995", "1993", "1991"], correctAnswer: "1992", hint: "Ваучерная приватизация" },
      { type: 'quiz', question: "Дефолт в России произошёл в:", options: ["1995", "1998", "2000", "1996", "1997"], correctAnswer: "1998", hint: "17 августа 1998" },
      { type: 'fill', question: "Ваучер - это приватизационный __", correctAnswer: "чек", hint: "Ваучерная приватизация - каждый гражданин получил чек" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь новейшую историю! 🏛️" }
  },
  {
    title: "Reported Speech",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "«I am happy» → He said he __ happy.", options: ["is", "was", "will be", "has been", "had been"], correctAnswer: "was", hint: "Смещение времён: Present → Past" },
      { type: 'fill', question: "«I will come» → She said she __ come.", correctAnswer: "would", hint: "Will → would" },
      { type: 'quiz', question: "«I can swim» → He said he __ swim.", options: ["can", "could", "will", "would", "may"], correctAnswer: "could", hint: "Can → could" },
      { type: 'find', question: "Выбери изменения в косвенной речи:", options: ["Here → There", "Now → Then", "Today → That day", "Tomorrow → Yesterday", "Yesterday → The day before"], correctAnswer: ["Here → There", "Now → Then", "Today → That day", "Yesterday → The day before"], hint: "Смещение местоимений и наречий" },
      { type: 'fill', question: "«I went there» → He said he __ gone there.", correctAnswer: "had", hint: "Past Simple → Past Perfect" }
    ],
    reward: { stars: 3, message: "Excellent! Ты знаешь косвенную речь! 🇬🇧" }
  },

  // ========== НОВЫЕ ИГРЫ v3.42 ==========
  {
    title: "Тригонометрические уравнения",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "sin x = 0, x = ?", options: ["πn", "π/2 + πn", "2πn", "π/4 + πn", "π/3 + πn"], correctAnswer: "πn", hint: "sin x = 0 при x = πn" },
      { type: 'fill', question: "cos x = 1, x = __n", correctAnswer: "2π", hint: "cos x = 1 при x = 2πn" },
      { type: 'quiz', question: "tg x = 0, x = ?", options: ["πn", "π/2 + πn", "2πn", "π/4 + πn", "π/6 + πn"], correctAnswer: "πn", hint: "tg x = 0 при x = πn" },
      { type: 'quiz', question: "sin x = 1/2, x = ?", options: ["π/6 + 2πn", "π/3 + 2πn", "π/4 + 2πn", "π/2 + 2πn", "0 + 2πn"], correctAnswer: "π/6 + 2πn", hint: "sin 30° = 1/2" },
      { type: 'fill', question: "cos x = 0, x = π/2 + __n", correctAnswer: "π", hint: "cos x = 0 при x = π/2 + πn" }
    ],
    reward: { stars: 3, message: "Отлично! Ты решаешь тригонометрические уравнения! 📐" }
  },
  {
    title: "Комбинации тел",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Шар вписан в куб. Диаметр шара равен:", options: ["Стороне куба", "Диагонали куба", "Половине стороны", "Двойной стороне", "Диагонали грани"], correctAnswer: "Стороне куба", hint: "Шар касается всех граней" },
      { type: 'quiz', question: "Конус вписан в цилиндр. Их высоты:", options: ["Разные", "Одинаковые", "Зависит от размера", "Высота конуса больше", "Высота цилиндра больше"], correctAnswer: "Одинаковые", hint: "Конус касается оснований цилиндра" },
      { type: 'fill', question: "Если радиус шара = 3, то объём = __π (4/3πr³)", correctAnswer: "36", hint: "V = 4/3 × π × 27 = 36π" },
      { type: 'quiz', question: "Сфера вписана в куб со стороной a. Радиус сферы:", options: ["a", "a/2", "a√2", "a/3", "2a"], correctAnswer: "a/2", hint: "Диаметр = a" },
      { type: 'fill', question: "Объём шара с радиусом R = (4/3)πR³. При R=1, V = __π/3", correctAnswer: "4", hint: "V = 4π/3" }
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь комбинации тел! 📦" }
  },
  {
    title: "Изобразительные средства",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "«Золотые руки» - это:", options: ["Эпитет", "Метафора", "Сравнение", "Метонимия", "Гипербола"], correctAnswer: "Метафора", hint: "Скрытое сравнение" },
      { type: 'quiz', question: "«Как лев, он был смел» - это:", options: ["Метафора", "Эпитет", "Сравнение", "Олицетворение", "Ирония"], correctAnswer: "Сравнение", hint: "Сравнение с союзом «как»" },
      { type: 'find', question: "Выбери эпитеты:", options: ["Золотая осень", "Сладкий сон", "Шёпот листьев", "Крикливый сосед", "Бежит быстро"], correctAnswer: ["Золотая осень", "Сладкий сон", "Крикливый сосед"], hint: "Образные определения" },
      { type: 'quiz', question: "«Шёпот листьев» - это:", options: ["Метафора", "Олицетворение", "Эпитет", "Сравнение", "Гипербола"], correctAnswer: "Олицетворение", hint: "Наделение предметов свойствами живых" },
      { type: 'quiz', question: "Гипербола - это:", options: ["Преувеличение", "Преуменьшение", "Скрытое сравнение", "Образное определение", "Звукоподражание"], correctAnswer: "Преувеличение", hint: "Художественное преувеличение" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь изобразительные средства! ✨" }
  },
  {
    title: "Постмодернизм",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Постмодернизм характеризуется:", options: ["Чётким сюжетом", "Игрой с текстом", "Простотой", "Реалистичностью", "Историчностью"], correctAnswer: "Игрой с текстом", hint: "Интертекстуальность, ирония" },
      { type: 'find', question: "Выбери черты постмодернизма:", options: ["Интертекстуальность", "Ирония", "Цитатность", "Реализм", "Чёткий сюжет"], correctAnswer: ["Интертекстуальность", "Ирония", "Цитатность"], hint: "Особенности постмодернизма" },
      { type: 'quiz', question: "Постмодернизм возник:", options: ["В XIX веке", "Во второй половине XX века", "В XXI веке", "В XVIII веке", "В XVII веке"], correctAnswer: "Во второй половине XX века", hint: "1960-е годы" },
      { type: 'quiz', question: "«Школа для дураков» - автор:", options: ["Пелевин", "Соколов", "Сорокин", "Акунин", "Пелевин"], correctAnswer: "Соколов", hint: "Саша Соколов - постмодернист" },
      { type: 'quiz', question: "Виктор Пелевин - представитель:", options: ["Реализма", "Постмодернизма", "Классицизма", "Романтизма", "Сентиментализма"], correctAnswer: "Постмодернизма", hint: "Пелевин - известный русский постмодернист" }
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь постмодернизм! 📖" }
  },
  {
    title: "Современная Россия",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Крым вошёл в состав России:", options: ["2010", "2014", "2018", "2012", "2016"], correctAnswer: "2014", hint: "Март 2014 года" },
      { type: 'find', question: "Выбери события современной России:", options: ["Олимпиада Сочи 2014", "Крым 2014", "Конституция 1993", "Перестройка", "Вступление в ВТО 2012"], correctAnswer: ["Олимпиада Сочи 2014", "Крым 2014", "Вступление в ВТО 2012"], hint: "События после 2000 года" },
      { type: 'quiz', question: "Олимпиада в Сочи прошла в:", options: ["2010", "2014", "2018", "2012", "2016"], correctAnswer: "2014", hint: "Зимняя олимпиада" },
      { type: 'fill', question: "Конституция РФ принята в __ году", correctAnswer: "1993", hint: "12 декабря 1993" },
      { type: 'quiz', question: "День России отмечается:", options: ["12 июня", "12 декабря", "7 ноября", "9 мая", "4 ноября"], correctAnswer: "12 июня", hint: "День принятия декларации о суверенитете" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь современную историю! 🇷🇺" }
  },
  {
    title: "Термодинамика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Первый закон термодинамики:", options: ["Q = A", "Q = ΔU + A", "ΔU = Q", "Q = ΔU - A", "A = ΔU + Q"], correctAnswer: "Q = ΔU + A", hint: "Количество теплоты = изменение внутренней энергии + работа" },
      { type: 'quiz', question: "Адиабатный процесс:", options: ["При постоянной температуре", "Без теплообмена", "При постоянном давлении", "При постоянном объёме", "При постоянной влажности"], correctAnswer: "Без теплообмена", hint: "Q = 0" },
      { type: 'find', question: "Выбери изопроцессы:", options: ["Изотермический", "Изобарный", "Изохорный", "Адиабатный", "Изотопный"], correctAnswer: ["Изотермический", "Изобарный", "Изохорный", "Адиабатный"], hint: "Процессы при постоянном параметре" },
      { type: 'fill', question: "КПД = (Q₁ - Q₂) / __", correctAnswer: "Q₁", hint: "КПД = полезная работа / затраченная энергия" },
      { type: 'quiz', question: "Изотермический процесс - при постоянной:", options: ["Давлении", "Объёме", "Температуре", "Энтропии", "Энергии"], correctAnswer: "Температуре", hint: "T = const" }
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь термодинамику! ⚛️" }
  },
  {
    title: "Генетика человека",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Человек имеет хромосом:", options: ["23", "46", "48", "44", "50"], correctAnswer: "46", hint: "23 пары хромосом" },
      { type: 'quiz', question: "Пол человека определяется:", options: ["X-хромосомой", "Y-хромосомой", "Обеими", "Аутосомами", "Митохондриями"], correctAnswer: "Y-хромосомой", hint: "XY = мужчина, XX = женщина" },
      { type: 'find', question: "Выбери наследственные заболевания:", options: ["Гемофилия", "Дальтонизм", "Грипп", "Синдром Дауна", "Простуда"], correctAnswer: ["Гемофилия", "Дальтонизм", "Синдром Дауна"], hint: "Генетические нарушения" },
      { type: 'fill', question: "Гемофилия - __-сцепленное заболевание", correctAnswer: "X", hint: "Ген в X-хромосоме" },
      { type: 'quiz', question: "Генотип - это:", options: ["Внешний вид", "Совокупность генов", "Окружающая среда", "Фенотип", "Мутация"], correctAnswer: "Совокупность генов", hint: "Генетическая конституция организма" }
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь генетику! 🧬" }
  },
  {
    title: "Mixed Conditionals",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "If I __ (study) harder yesterday, I would pass now.", options: ["studied", "had studied", "study", "have studied", "would study"], correctAnswer: "had studied", hint: "Mixed: Past Perfect + would + V" },
      { type: 'quiz', question: "If she __ (be) rich, she would have bought it.", options: ["is", "were", "had been", "has been", "would be"], correctAnswer: "were", hint: "Mixed: Second + Third" },
      { type: 'fill', question: "If I knew her, I __ (say) hello yesterday. (would have said)", correctAnswer: "would have said", hint: "Present unreal + Past unreal" },
      { type: 'find', question: "Выбери типы conditionals:", options: ["Zero", "First", "Second", "Third", "Mixed"], correctAnswer: ["Zero", "First", "Second", "Third", "Mixed"], hint: "Пять типов условных предложений" },
      { type: 'quiz', question: "Third Conditional structure:", options: ["If + Past Simple, would + V", "If + Past Perfect, would have + V3", "If + Present Simple, will + V", "If + Present Perfect, will + V", "If + Future, will + V"], correctAnswer: "If + Past Perfect, would have + V3", hint: "Третий тип - прошлое нереальное" }
    ],
    reward: { stars: 3, message: "Excellent! Ты знаешь смешанные условия! 🇬🇧" }
  },

  // ========== ОБЩЕСТВОЗНАНИЕ ==========
  {
    title: "Право",
    subject: "Обществознание",
    icon: "Scale",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Конституция - это:", options: ["Обычный закон", "Основной закон государства", "Указ президента", "Постановление", "Приказ"], correctAnswer: "Основной закон государства", hint: "Конституция имеет высшую юридическую силу" },
      { type: 'quiz', question: "Правоспособность возникает с:", options: ["Рождения", "14 лет", "18 лет", "16 лет", "21 года"], correctAnswer: "Рождения", hint: "Способность иметь права" },
      { type: 'find', question: "Выбери права человека:", options: ["Право на жизнь", "Право на труд", "Право нарушать закон", "Право на образование", "Право на свободу"], correctAnswer: ["Право на жизнь", "Право на труд", "Право на образование", "Право на свободу"], hint: "Естественные права человека" },
      { type: 'quiz', question: "Дееспособность в полном объёме наступает с:", options: ["14 лет", "16 лет", "18 лет", "21 года", "25 лет"], correctAnswer: "18 лет", hint: "Совершеннолетие = полная дееспособность" },
      { type: 'quiz', question: "Гражданство - это:", options: ["Место жительства", "Правовая связь лица с государством", "Национальность", "Резидентство", "Паспорт"], correctAnswer: "Правовая связь лица с государством", hint: "Стабильная правовая связь" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь основы права! ⚖️" }
  },
  {
    title: "Экономика",
    subject: "Обществознание",
    icon: "Scale",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Инфляция - это:", options: ["Снижение цен", "Повышение общего уровня цен", "Стабильность цен", "Рост производства", "Падение курса"], correctAnswer: "Повышение общего уровня цен", hint: "Обесценивание денег" },
      { type: 'quiz', question: "Спрос и предложение определяют:", options: ["Только предложение", "Рыночную цену", "Только спрос", "Государственную цену", "Себестоимость"], correctAnswer: "Рыночную цену", hint: "Закон спроса и предложения" },
      { type: 'find', question: "Выбери факторы производства:", options: ["Труд", "Капитал", "Земля", "Деньги", "Предпринимательство"], correctAnswer: ["Труд", "Капитал", "Земля", "Предпринимательство"], hint: "Ресурсы для производства" },
      { type: 'fill', question: "Безработица - это отсутствие __ у трудоспособного населения", correctAnswer: "работы", hint: "Трудоспособные люди без работы" },
      { type: 'quiz', question: "Монополия - это:", options: ["Много конкурентов", "Один продавец на рынке", "Два продавца", "Отсутствие рынка", "Свободный рынок"], correctAnswer: "Один продавец на рынке", hint: "Единственный производитель товара" }
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь экономику! 💰" }
  },

  // ========== ГЕОГРАФИЯ ==========
  {
    title: "География России",
    subject: "География",
    icon: "Map",
    color: "text-teal-400",
    tasks: [
      { type: 'quiz', question: "Самая длинная река России:", options: ["Волга", "Обь", "Лена", "Енисей", "Амур"], correctAnswer: "Обь", hint: "Обь с Иртышом - самая длинная" },
      { type: 'quiz', question: "Самое глубокое озеро мира в России:", options: ["Ладожское", "Байкал", "Каспийское", "Онежское", "Таймыр"], correctAnswer: "Байкал", hint: "Байкал - глубочайшее озеро" },
      { type: 'find', question: "Выбери субъекты РФ:", options: ["Московская область", "Крым", "Киев", "Санкт-Петербург", "Минск"], correctAnswer: ["Московская область", "Крым", "Санкт-Петербург"], hint: "Субъекты Российской Федерации" },
      { type: 'fill', question: "Россия граничит с __ странами (число)", correctAnswer: "18", hint: "Самое большое число границ" },
      { type: 'quiz', question: "Столица России:", options: ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань"], correctAnswer: "Москва", hint: "Столица Российской Федерации" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь географию России! 🗺️" }
  },
  {
    title: "География мира",
    subject: "География",
    icon: "Map",
    color: "text-teal-400",
    tasks: [
      { type: 'quiz', question: "Самая большая страна мира по площади:", options: ["Китай", "США", "Россия", "Канада", "Бразилия"], correctAnswer: "Россия", hint: "17 млн км²" },
      { type: 'quiz', question: "Самая населённая страна мира:", options: ["Индия", "Китай", "США", "Индонезия", "Бразилия"], correctAnswer: "Индия", hint: "Индия превзошла Китай в 2023" },
      { type: 'find', question: "Выбери континенты:", options: ["Евразия", "Африка", "Атлантида", "Австралия", "Антарктида"], correctAnswer: ["Евразия", "Африка", "Австралия", "Антарктида"], hint: "Шесть континентов" },
      { type: 'fill', question: "Самый большой океан - __ океан", correctAnswer: "Тихий", hint: "Тихий океан - самый большой" },
      { type: 'quiz', question: "Самая высокая гора мира:", options: ["Эльбрус", "Эверест", "Килиманджаро", "Монблан", "Казбек"], correctAnswer: "Эверест", hint: "8848 м - Джомолунгма" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь географию мира! 🌍" }
  },

  // ========== ИНФОРМАТИКА ==========
  {
    title: "Программирование",
    subject: "Информатика",
    icon: "Monitor",
    color: "text-sky-400",
    tasks: [
      { type: 'quiz', question: "Переменная в программировании - это:", options: ["Постоянное значение", "Именованная область памяти", "Команда", "Оператор", "Функция"], correctAnswer: "Именованная область памяти", hint: "Хранит данные" },
      { type: 'quiz', question: "Цикл for используется для:", options: ["Однократного выполнения", "Многократного выполнения", "Остановки программы", "Ввода данных", "Вывода данных"], correctAnswer: "Многократного выполнения", hint: "Повторение кода" },
      { type: 'find', question: "Выбери типы данных:", options: ["Integer", "String", "Boolean", "Table", "Chair"], correctAnswer: ["Integer", "String", "Boolean"], hint: "Основные типы данных" },
      { type: 'fill', question: "if-else - это __ конструкция", correctAnswer: "условная", hint: "Условный оператор" },
      { type: 'quiz', question: "Массив - это:", options: ["Одна переменная", "Набор элементов", "Функция", "Оператор", "Цикл"], correctAnswer: "Набор элементов", hint: "Структура данных для хранения набора значений" }
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь программирование! 💻" }
  },
  {
    title: "Алгоритмы и структуры данных",
    subject: "Информатика",
    icon: "Monitor",
    color: "text-sky-400",
    tasks: [
      { type: 'quiz', question: "Массив - это:", options: ["Одна переменная", "Упорядоченный набор элементов", "Функция", "Цикл", "Условие"], correctAnswer: "Упорядоченный набор элементов", hint: "Коллекция данных" },
      { type: 'quiz', question: "Сложность алгоритма O(n) означает:", options: ["Константное время", "Линейное время", "Квадратичное время", "Логарифмическое время", "Экспоненциальное время"], correctAnswer: "Линейное время", hint: "Время растёт линейно" },
      { type: 'find', question: "Выбери алгоритмы сортировки:", options: ["Пузырьковая", "Быстрая", "Слиянием", "Умножения", "Деления"], correctAnswer: ["Пузырьковая", "Быстрая", "Слиянием"], hint: "Алгоритмы упорядочивания" },
      { type: 'fill', question: "Бинарный поиск работает за O(log __)", correctAnswer: "n", hint: "Логарифмическая сложность" },
      { type: 'quiz', question: "Стек работает по принципу:", options: ["FIFO", "LIFO", "Случайно", "По приоритету", "По кругу"], correctAnswer: "LIFO", hint: "Last In, First Out - последним пришёл, первым ушёл" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь алгоритмы! 🔢" }
  },

  // ========== ФИЗИКА: ЭЛЕКТРОДИНАМИКА ==========
  {
    title: "Электродинамика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Закон Ома для участка цепи:", options: ["I = U/R", "I = UR", "I = R/U", "I = U + R", "I = U × R"], correctAnswer: "I = U/R", hint: "Ток = напряжение / сопротивление" },
      { type: 'fill', question: "Сила тока измеряется в __", correctAnswer: "амперах", hint: "Единица силы тока" },
      { type: 'quiz', question: "При последовательном соединении сопротивления:", options: ["Складываются", "Вычитаются", "Перемножаются", "Делятся", "Не меняются"], correctAnswer: "Складываются", hint: "R = R₁ + R₂ + ..." },
      { type: 'find', question: "Выбери электрические величины:", options: ["Напряжение", "Сила тока", "Сопротивление", "Масса", "Скорость"], correctAnswer: ["Напряжение", "Сила тока", "Сопротивление"], hint: "Электрические характеристики" },
      { type: 'fill', question: "Напряжение измеряется в __", correctAnswer: "вольтах", hint: "Единица напряжения" }
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь электродинамику! ⚡" }
  },
  {
    title: "Магнитное поле",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Магнитное поле создаётся:", options: ["Покоющимися зарядами", "Движущимися зарядами", "Только магнитами", "Только током", "Только зарядами"], correctAnswer: "Движущимися зарядами", hint: "Электрический ток создаёт магнитное поле" },
      { type: 'quiz', question: "Сила Лоренца действует на:", options: ["Покоющийся заряд", "Движущийся заряд", "Любой заряд", "Нейтральные частицы", "Только магниты"], correctAnswer: "Движущийся заряд", hint: "F = qvB" },
      { type: 'fill', question: "Правило __ руки определяет направление магнитного поля", correctAnswer: "буравчика", hint: "Правило буравчика или правой руки" },
      { type: 'quiz', question: "Магнитный поток измеряется в:", options: ["Тесла", "Вебер", "Ампер", "Вольт", "Генри"], correctAnswer: "Вебер", hint: "Ф = BS" },
      { type: 'fill', question: "Магнитная индукция измеряется в __", correctAnswer: "тесла", hint: "Единица магнитной индукции" }
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь магнитное поле! 🧲" }
  },

  // ========== ХИМИЯ: ОРГАНИКА ==========
  {
    title: "Органическая химия",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: "Алканы имеют общую формулу:", options: ["CₙH₂ₙ", "CₙH₂ₙ₊₂", "CₙH₂ₙ₋₂", "CₙHₙ", "CHₙ"], correctAnswer: "CₙH₂ₙ₊₂", hint: "Предельные углеводороды" },
      { type: 'quiz', question: "Этанол - это:", options: ["Кислота", "Спирт", "Альдегид", "Кетон", "Эфир"], correctAnswer: "Спирт", hint: "C₂H₅OH - этиловый спирт" },
      { type: 'find', question: "Выбери функциональные группы:", options: ["-OH", "-COOH", "-NH₂", "-H₂O", "-O₂"], correctAnswer: ["-OH", "-COOH", "-NH₂"], hint: "Группы атомов, определяющие свойства" },
      { type: 'fill', question: "Гомологический ряд - это серия веществ с разницей CH__", correctAnswer: "2", hint: "Гомологи отличаются на CH₂" },
      { type: 'quiz', question: "Изомерия - это:", options: ["Одинаковое строение", "Одинаковая формула, разное строение", "Разная формула", "Отсутствие связи", "Свободные радикалы"], correctAnswer: "Одинаковая формула, разное строение", hint: "Вещества с одинаковой формулой, но разным строением" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь органическую химию! 🧪" }
  },
  {
    title: "Углеводороды",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: "Алкены содержат:", options: ["Одинарную связь", "Двойную связь", "Тройную связь", "Без связей", "Ионную связь"], correctAnswer: "Двойную связь", hint: "C=C - двойная связь" },
      { type: 'quiz', question: "Бензол имеет структуру:", options: ["Линейную", "Циклическую", "Разветвлённую", "Цепную", "Сферическую"], correctAnswer: "Циклическую", hint: "C₆H₆ - ароматическое кольцо" },
      { type: 'find', question: "Выбери типы реакций в органике:", options: ["Замещения", "Присоединения", "Гниения", "Отщепления", "Горения"], correctAnswer: ["Замещения", "Присоединения", "Отщепления", "Горения"], hint: "Основные типы органических реакций" },
      { type: 'fill', question: "Метан - это CH__", correctAnswer: "4", hint: "CH₄ - простейший алкан" },
      { type: 'quiz', question: "Алкины содержат:", options: ["Одинарную связь", "Двойную связь", "Тройную связь", "Без связей", "Две двойные связи"], correctAnswer: "Тройную связь", hint: "C≡C - тройная связь" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь углеводороды! ⚗️" }
  }
]
