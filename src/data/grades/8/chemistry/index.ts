import { SubjectData, GameLesson } from '@/data/types'

export const lessons: SubjectData = {
  title: "Химия",
  icon: "FlaskConical",
  color: "text-emerald-400",
  topics: ["Атомы", "Молекулы", "Химические реакции", "Классы веществ"],
  detailedTopics: [
    {
      topic: "Основы химии",
      lessons: [
        { title: "Атомы и элементы", description: "Строение атома.", tasks: ["Протоны", "Нейтроны", "Электроны", "Ядро"] },
        { title: "Периодическая таблица", description: "Менделеев.", tasks: ["Периоды", "Группы", "Металлы", "Неметаллы"] },
        { title: "Химические формулы", description: "Запись веществ.", tasks: ["Индекс", "Коэффициент", "Относительная масса", "Расчёты"] }
      ]
    },
    {
      topic: "Реакции",
      lessons: [
        { title: "Типы реакций", description: "Классификация.", tasks: ["Соединение", "Разложение", "Замещение", "Обмен"] },
        { title: "Уравнения реакций", description: "Расстановка коэффициентов.", tasks: ["Закон сохранения", "Баланс", "Подбор", "Проверка"] }
      ]
    }
  ]
}

export const games: GameLesson[] = [
  {
    title: "Строение атома",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      {
        type: 'match',
        question: "Соедини частицу с зарядом:",
        options: ["протон", "нейтрон", "электрон", "ядро"],
        correctAnswer: ["+1", "0", "-1", "положительный"],
        hint: "Заряды частиц"
      },
      {
        type: 'find',
        question: "Какая частица имеет отрицательный заряд?",
        options: ["протон", "нейтрон", "электрон", "ядро"],
        correctAnswer: "электрон",
        hint: "Электрон заряжен отрицательно"
      },
      {
        type: 'find',
        question: "Где находится большая часть массы атома?",
        options: ["электроны", "ядро", "оболочка", "вакуум"],
        correctAnswer: "ядро",
        hint: "Ядро содержит протоны и нейтроны"
      },
      {
        type: 'match',
        question: "Соедини частицу с расположением:",
        options: ["протоны", "электроны", "нейтроны", "атом"],
        correctAnswer: ["в ядре", "на орбиталях", "в ядре", "нейтрален"],
        hint: "Строение"
      }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь атом! ⚛️" }
  },
  {
    title: "Периодическая таблица",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      {
        type: 'match',
        question: "Соедини элемент с символом:",
        options: ["водород", "кислород", "углерод", "азот"],
        correctAnswer: ["H", "O", "C", "N"],
        hint: "Химические символы"
      },
      {
        type: 'match',
        question: "Соедини элемент с группой:",
        options: ["натрий", "хлор", "железо", "кремний"],
        correctAnswer: ["металл", "неметалл", "металл", "неметалл"],
        hint: "Металлы и неметаллы"
      },
      {
        type: 'find',
        question: "Сколько электронов у атома с зарядом ядра +6?",
        options: ["3", "6", "12", "0"],
        correctAnswer: "6",
        hint: "Число электронов = числу протонов"
      },
      {
        type: 'find',
        question: "Кто создал периодическую таблицу?",
        options: ["Ньютон", "Менделеев", "Эйнштейн", "Бор"],
        correctAnswer: "Менделеев",
        hint: "Д.И. Менделеев"
      }
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь таблицу! 📊" }
  },
  {
    title: "Химические формулы",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      {
        type: 'match',
        question: "Соедини формулу с названием:",
        options: ["H₂O", "CO₂", "NaCl", "H₂SO₄"],
        correctAnswer: ["вода", "углекислый газ", "поваренная соль", "серная кислота"],
        hint: "Химические формулы"
      },
      {
        type: 'find',
        question: "Что означает индекс 2 в формуле H₂O?",
        options: ["2 молекулы", "2 атома водорода", "2 грамма", "2 литра"],
        correctAnswer: "2 атома водорода",
        hint: "Индекс показывает число атомов"
      },
      {
        type: 'find',
        question: "Формула молекулы кислорода:",
        options: ["O", "O₂", "O₃", "H₂O"],
        correctAnswer: "O₂",
        hint: "Кислород — двухатомная молекула"
      }
    ],
    reward: { stars: 3, message: "Отлично! Ты читаешь формулы! 🔬" }
  },
  {
    title: "Валентность",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      {
        type: 'match',
        question: "Соедини элемент с валентностью:",
        options: ["водород", "кислород", "азот", "углерод"],
        correctAnswer: ["I", "II", "III", "IV"],
        hint: "Постоянная валентность"
      },
      {
        type: 'find',
        question: "Валентность кислорода:",
        options: ["I", "II", "III", "IV"],
        correctAnswer: "II",
        hint: "Кислород всегда II-валентен"
      },
      {
        type: 'find',
        question: "Формула воды H₂O. Какова валентность кислорода?",
        options: ["I", "II", "III", "IV"],
        correctAnswer: "II",
        hint: "2 атома водорода (I) соединены с 1 атомом кислорода"
      }
    ],
    reward: { stars: 3, message: "Супер! Ты понимаешь валентность! ⚗️" }
  },
  {
    title: "Типы химических реакций",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      {
        type: 'match',
        question: "Соедини тип реакции со схемой:",
        options: ["соединение", "разложение", "замещение", "обмен"],
        correctAnswer: ["A + B = AB", "AB = A + B", "A + BC = AC + B", "AB + CD = AD + CB"],
        hint: "Типы реакций"
      },
      {
        type: 'find',
        question: "Какой тип реакции: 2H₂ + O₂ = 2H₂O?",
        options: ["соединение", "разложение", "замещение", "обмен"],
        correctAnswer: "соединение",
        hint: "Два вещества образуют одно"
      },
      {
        type: 'find',
        question: "Какой тип реакции: 2H₂O = 2H₂ + O₂?",
        options: ["соединение", "разложение", "замещение", "обмен"],
        correctAnswer: "разложение",
        hint: "Одно вещество распадается"
      },
      {
        type: 'find',
        question: "Какой тип реакции: Zn + 2HCl = ZnCl₂ + H₂?",
        options: ["соединение", "разложение", "замещение", "обмен"],
        correctAnswer: "замещение",
        hint: "Цинк вытесняет водород"
      }
    ],
    reward: { stars: 3, message: "Отлично! Ты различаешь реакции! 🧪" }
  },
  {
    title: "Классы неорганических веществ",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      {
        type: 'match',
        question: "Соедини класс с примером:",
        options: ["оксид", "кислота", "основание", "соль"],
        correctAnswer: ["CaO", "HCl", "NaOH", "NaCl"],
        hint: "Классы веществ"
      },
      {
        type: 'find',
        question: "Какое вещество — кислота?",
        options: ["NaOH", "H₂SO₄", "NaCl", "CaO"],
        correctAnswer: "H₂SO₄",
        hint: "Кислоты начинаются с H"
      },
      {
        type: 'find',
        question: "Какое вещество — оксид?",
        options: ["HCl", "NaOH", "CO₂", "NaCl"],
        correctAnswer: "CO₂",
        hint: "Оксид — элемент + кислород"
      },
      {
        type: 'find',
        question: "Какое вещество — основание?",
        options: ["HCl", "NaOH", "CO₂", "NaCl"],
        correctAnswer: "NaOH",
        hint: "Основание = металл + OH"
      }
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь классы веществ! 🎯" }
  }
]
