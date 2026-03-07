import { SubjectData, GameLesson } from '@/data/types'

const createLesson = (title: string, description: string, tasks: string[]) => ({
  title, description, tasks
})

export const lessons: SubjectData = {
  title: "Развитие речи",
  icon: "MessageCircle",
  color: "text-teal-400",
  topics: ["Составление рассказов", "Артикуляция", "Стихи и скороговорки", "Словарный запас"],
  detailedTopics: [
    {
      topic: "Артикуляционная гимнастика",
      lessons: [
        createLesson("Урок 1: Упражнения для языка", "Развитие подвижности языка.", [
          "Упражнение \"Лопаточка\"",
          "Упражнение \"Иголочка\"",
          "Упражнение \"Чашечка\"",
          "Упражнение \"Грибок\""
        ]),
        createLesson("Урок 2: Упражнения для губ", "Развитие подвижности губ.", [
          "Упражнение \"Улыбка\"",
          "Упражнение \"Трубочка\"",
          "Упражнение \"Хоботок\"",
          "Чередование упражнений"
        ])
      ]
    }
  ]
}

export const games: GameLesson[] = [
  {
    title: "Скороговорки 🗣️",
    subject: "Развитие речи",
    icon: "MessageCircle",
    color: "text-teal-400",
    tasks: [
      {
        type: 'quiz',
        question: "Какой звук повторяется: \"Шесть мышат шуршат\"?",
        options: ["С", "Ш", "М"],
        correctAnswer: "Ш",
        hint: "Найди повторяющийся звук"
      },
      {
        type: 'order',
        question: "Собери скороговорку:",
        options: ["мыла", "Мама", "Милу"],
        correctAnswer: "Мама мыла Милу",
        hint: "Начни с подлежащего"
      },
      {
        type: 'quiz',
        question: "Что делает улитка на вилке?",
        options: ["Ползёт", "Сидит", "Спит"],
        correctAnswer: "Сидит",
        hint: "Вспомни скороговорку"
      },
      {
        type: 'match',
        question: "Соедини начало и конец скороговорки:",
        options: ["Карл у Клары украл", "От топота копыт", "Шла Саша"],
        correctAnswer: ["кораллы", "пыль по полю", "по шоссе"],
        hint: "Вспомни известные скороговорки"
      }
    ],
    reward: { stars: 3, message: "Отлично! Ты отлично говоришь скороговорки! 🗣️" }
  },
  {
    title: "Составь рассказ 📖",
    subject: "Развитие речи",
    icon: "MessageCircle",
    color: "text-teal-400",
    tasks: [
      {
        type: 'order',
        question: "Расставь события по порядку:",
        options: ["утром", "днём", "вечером", "ночью"],
        correctAnswer: "утром, днём, вечером, ночью",
        hint: "Время идёт от утра к ночи"
      },
      {
        type: 'quiz',
        question: "С чего начинается рассказ?",
        options: ["Завязка", "Конец", "Середина"],
        correctAnswer: "Завязка",
        hint: "Рассказ начинается с начала!"
      },
      {
        type: 'match',
        question: "Соедини части сказки:",
        options: ["Жили-были", "Однажды", "И жили они"],
        correctAnswer: ["дед да баба", "случилось чудо", "долго и счастливо"],
        hint: "Вспомни структуру сказки"
      },
      {
        type: 'find',
        question: "Что должно быть в рассказе?",
        options: ["Начало", "Картинка", "Середина", "Конец", "Обложка"],
        correctAnswer: ["Начало", "Середина", "Конец"],
        hint: "Три части рассказа"
      }
    ],
    reward: { stars: 3, message: "Супер! Ты умеешь составлять рассказы! 📖" }
  },
  {
    title: "Слова и звуки 🔊",
    subject: "Развитие речи",
    icon: "MessageCircle",
    color: "text-teal-400",
    tasks: [
      {
        type: 'quiz',
        question: "Какой первый звук в слове \"Арбуз\"?",
        options: ["А", "О", "У"],
        correctAnswer: "А",
        hint: "Произнеси слово медленно"
      },
      {
        type: 'find',
        question: "Выбери слова со звуком \"С\":",
        options: ["Сок", "Дом", "Сон", "Кот", "Стол"],
        correctAnswer: ["Сок", "Сон", "Стол"],
        hint: "Послушай звуки в словах"
      },
      {
        type: 'match',
        question: "Соедини слово с первым звуком:",
        options: ["Дом", "Рак", "Кот", "Мак"],
        correctAnswer: ["Д", "Р", "К", "М"],
        hint: "Назови первый звук"
      },
      {
        type: 'quiz',
        question: "Сколько звуков в слове \"КОТ\"?",
        options: ["2", "3", "4"],
        correctAnswer: "3",
        hint: "К-О-Т"
      }
    ],
    reward: { stars: 3, message: "Молодец! Ты хорошо слышишь звуки! 🔊" }
  },
  {
    title: "Рифмы 🎭",
    subject: "Развитие речи",
    icon: "MessageCircle",
    color: "text-teal-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что рифмуется со словом КОТ?",
        options: ["ДОМ", "КРОТ", "СОК"],
        correctAnswer: "КРОТ",
        hint: "Окончание должно звучать похоже"
      },
      {
        type: 'find',
        question: "Найди рифмы к слову МАМА:",
        options: ["ПАПА", "РАМА", "ЛАМА", "ВАТА", "ДАМА"],
        correctAnswer: ["РАМА", "ЛАМА", "ДАМА"],
        hint: "Они заканчиваются на -ама"
      },
      {
        type: 'match',
        question: "Соедини рифмующиеся слова:",
        options: ["МЫШКА", "КОШКА", "МИШКА", "ЛОЖКА"],
        correctAnswer: ["МИШКА", "ЛОЖКА", "МЫШКА", "КОШКА"],
        hint: "Найди пары с похожим окончанием"
      },
      {
        type: 'quiz',
        question: "Какое слово не рифмуется?",
        options: ["ДОМ - ГНОМ", "КОТ - КРОТ", "ШАР - СТОЛ"],
        correctAnswer: "ШАР - СТОЛ",
        hint: "Найди пару без рифмы"
      }
    ],
    reward: { stars: 3, message: "Отлично! Ты умеешь рифмовать! 🎭" }
  },
  {
    title: "Слова-действия 🏃",
    subject: "Развитие речи",
    icon: "MessageCircle",
    color: "text-teal-400",
    tasks: [
      {
        type: 'find',
        question: "Найди слова-действия:",
        options: ["БЕЖАТЬ", "КРАСИВЫЙ", "ПРЫГАТЬ", "ДОМ", "СПАТЬ"],
        correctAnswer: ["БЕЖАТЬ", "ПРЫГАТЬ", "СПАТЬ"],
        hint: "Они отвечают на вопрос 'что делать?'"
      },
      {
        type: 'match',
        question: "Соедини животное с действием:",
        options: ["Собака", "Кошка", "Птица", "Рыба"],
        correctAnswer: ["лает", "мяукает", "летает", "плавает"],
        hint: "Что они делают?"
      },
      {
        type: 'quiz',
        question: "Что делает учитель?",
        options: ["Летает", "Учит", "Плавает"],
        correctAnswer: "Учит",
        hint: "Учитель - он учит"
      },
      {
        type: 'find',
        question: "Что можно делать ногами?",
        options: ["Ходить", "Бегать", "Писать", "Прыгать", "Читать"],
        correctAnswer: ["Ходить", "Бегать", "Прыгать"],
        hint: "Подумай о действиях ног"
      }
    ],
    reward: { stars: 3, message: "Молодец! Ты знаешь слова-действия! 🏃" }
  },
  {
    title: "Слова-признаки 🌈",
    subject: "Развитие речи",
    icon: "MessageCircle",
    color: "text-teal-400",
    tasks: [
      {
        type: 'find',
        question: "Найди слова-признаки:",
        options: ["БОЛЬШОЙ", "БЕЖАТЬ", "КРАСНЫЙ", "ДОМ", "МЯГКИЙ"],
        correctAnswer: ["БОЛЬШОЙ", "КРАСНЫЙ", "МЯГКИЙ"],
        hint: "Они отвечают на вопрос 'какой?'"
      },
      {
        type: 'match',
        question: "Соедини предмет с признаком:",
        options: ["Лимон", "Снег", "Небо", "Трава"],
        correctAnswer: ["жёлтый", "белый", "голубой", "зелёная"],
        hint: "Какого они цвета?"
      },
      {
        type: 'quiz',
        question: "Какое солнышко?",
        options: ["Грустное", "Тёмное", "Яркое"],
        correctAnswer: "Яркое",
        hint: "Солнце светит ярко!"
      },
      {
        type: 'find',
        question: "Каким может быть дом?",
        options: ["Большой", "Бежать", "Красивый", "Прыгать", "Тёплый"],
        correctAnswer: ["Большой", "Красивый", "Тёплый"],
        hint: "Дом какой?"
      }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь слова-признаки! 🌈" }
  }
]
