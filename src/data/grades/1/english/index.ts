import { SubjectData, GameLesson } from '@/data/types'

const createLesson = (title: string, description: string, tasks: string[], image?: string) => ({
  title, description, tasks,
  ...(image && { image })
})

export const lessons: SubjectData = {
  title: "Иностранный язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: ["Приветствие", "Представление", "Цвета", "Числа 1-10", "Семья", "Животные"],
  detailedTopics: [
    {
      topic: "Знакомство",
      lessons: [
        createLesson("Урок 1: Hello!", "Приветствия на английском.", [
          "Научиться Hello! Hi!",
          "Ответить на приветствие",
          "Познакомиться",
          "Разыграть диалог"
        ], "/images/lessons/grade1/english/lesson1-hello.svg"),
        createLesson("Урок 2: What is your name?", "Умение представиться.", [
          "Спросить имя",
          "Ответить: My name is...",
          "Разыграть диалог",
          "Написать имя"
        ], "/images/lessons/grade1/english/lesson2-name.svg"),
        createLesson("Урок 3: Goodbye!", "Прощание.", [
          "Научиться Goodbye!",
          "Ответить",
          "Выучить песенку",
          "Разыграть диалог"
        ], "/images/lessons/grade1/english/lesson3-goodbye.svg")
      ]
    },
    {
      topic: "Цвета и числа",
      lessons: [
        createLesson("Урок 4: Colours", "Название цветов.", [
          "Выучить: red, blue, green, yellow",
          "Показать предметы",
          "Назвать цвет",
          "Раскрасить картинку"
        ], "/images/lessons/grade1/english/lesson4-colours.svg"),
        createLesson("Урок 5: Numbers 1-5", "Счёт от 1 до 5.", [
          "Выучить: one, two, three...",
          "Посчитать предметы",
          "Показать пальцы",
          "Написать словами"
        ], "/images/lessons/grade1/english/lesson5-numbers-1-5.svg"),
        createLesson("Урок 6: Numbers 6-10", "Счёт от 6 до 10.", [
          "Выучить: six, seven...",
          "Посчитать до 10",
          "Назвать число",
          "Решить примеры"
        ], "/images/lessons/grade1/english/lesson6-numbers-6-10.svg")
      ]
    }
  ]
}

export const games: GameLesson[] = [
  {
    title: "Hello! Привет!",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Как сказать «Привет» по-английски?",
        options: ["Goodbye", "Hello", "Thanks"],
        correctAnswer: "Hello",
        hint: "Это самое популярное приветствие"
      },
      {
        type: 'match',
        question: "Соедини: Hello - это...",
        options: ["Hello"],
        correctAnswer: ["Привет"],
        hint: "Hello = Привет"
      },
      {
        type: 'quiz',
        question: "Как ещё можно поздороваться?",
        options: ["Hi", "Bye", "No"],
        correctAnswer: "Hi",
        hint: "Это короткое приветствие"
      },
      {
        type: 'find',
        question: "Выбери приветствия:",
        options: ["Hello", "Hi", "Goodbye", "Bye", "Thanks"],
        correctAnswer: ["Hello", "Hi"],
        hint: "Приветствия = Greetings"
      }
    ],
    reward: { stars: 3, message: "Great! Отлично! Ты знаешь приветствия! 👋" }
  },
  {
    title: "Цвета по-английски",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Red - это какой цвет?",
        options: ["Синий", "Красный", "Зелёный"],
        correctAnswer: "Красный",
        hint: "Red = Красный"
      },
      {
        type: 'quiz',
        question: "Как будет «синий» по-английски?",
        options: ["Red", "Blue", "Green"],
        correctAnswer: "Blue",
        hint: "Blue = Синий"
      },
      {
        type: 'find',
        question: "Выбери названия цветов:",
        options: ["Red", "Cat", "Blue", "Dog", "Green", "Yellow"],
        correctAnswer: ["Red", "Blue", "Green", "Yellow"],
        hint: "Colours = Цвета"
      },
      {
        type: 'quiz',
        question: "Какого цвета трава?",
        options: ["Red", "Blue", "Green"],
        correctAnswer: "Green",
        hint: "Трава зелёная"
      }
    ],
    reward: { stars: 3, message: "Wonderful! Ты знаешь цвета! 🎨" }
  },
  {
    title: "Числа 1-5",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "One - это какое число?",
        options: ["Один", "Два", "Три"],
        correctAnswer: "Один",
        hint: "One = 1"
      },
      {
        type: 'quiz',
        question: "Как будет «три» по-английски?",
        options: ["One", "Two", "Three"],
        correctAnswer: "Three",
        hint: "Three = 3"
      },
      {
        type: 'order',
        question: "Расставь по порядку: Three, One, Two",
        correctAnswer: "One, Two, Three",
        hint: "От 1 до 3"
      },
      {
        type: 'quiz',
        question: "Five - это?",
        options: ["4", "5", "6"],
        correctAnswer: "5",
        hint: "Five = 5"
      }
    ],
    reward: { stars: 3, message: "Excellent! Ты знаешь числа! 🔢" }
  },
  {
    title: "Животные",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Cat - это?",
        options: ["Собака", "Кошка", "Птица"],
        correctAnswer: "Кошка",
        hint: "Cat = Кошка"
      },
      {
        type: 'quiz',
        question: "Как будет «собака» по-английски?",
        options: ["Cat", "Dog", "Bird"],
        correctAnswer: "Dog",
        hint: "Dog = Собака"
      },
      {
        type: 'find',
        question: "Выбери названия животных:",
        options: ["Cat", "Red", "Dog", "Blue", "Bird", "Fish"],
        correctAnswer: ["Cat", "Dog", "Bird", "Fish"],
        hint: "Animals = Животные"
      },
      {
        type: 'quiz',
        question: "Fish - это?",
        options: ["Птица", "Рыба", "Кошка"],
        correctAnswer: "Рыба",
        hint: "Fish живёт в воде"
      }
    ],
    reward: { stars: 3, message: "Great job! Ты знаешь животных! 🐱" }
  }
]
