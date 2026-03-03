import { SubjectData, GameLesson } from '@/data/types'

export const lessons: SubjectData = {
  title: "Иностранный язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: ["Дом", "Еда", "Животные", "Погода"]
}

export const games: GameLesson[] = [
  {
    title: "My Family - Моя семья",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Mother - это?", options: ["Папа", "Мама", "Брат"], correctAnswer: "Мама", hint: "Mother = мама" },
      { type: 'quiz', question: "Как будет «папа» по-английски?", options: ["Mother", "Father", "Brother"], correctAnswer: "Father", hint: "Father = папа" },
      { type: 'find', question: "Выбери слова о семье:", options: ["Mother", "Cat", "Father", "Dog", "Sister", "Brother"], correctAnswer: ["Mother", "Father", "Sister", "Brother"], hint: "Family = семья" },
      { type: 'quiz', question: "Sister - это?", options: ["Брат", "Сестра", "Мама"], correctAnswer: "Сестра", hint: "Sister = сестра" }
    ],
    reward: { stars: 3, message: "Great! Ты знаешь семью по-английски! 👨‍👩‍👧‍👦" }
  },
  {
    title: "Food - Еда",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Apple - это?", options: ["Груша", "Яблоко", "Апельсин"], correctAnswer: "Яблоко", hint: "Apple = яблоко" },
      { type: 'quiz', question: "Как будет «хлеб» по-английски?", options: ["Bread", "Water", "Milk"], correctAnswer: "Bread", hint: "Bread = хлеб" },
      { type: 'find', question: "Выбери названия еды:", options: ["Apple", "Cat", "Bread", "Dog", "Milk", "Water"], correctAnswer: ["Apple", "Bread", "Milk", "Water"], hint: "Food = еда" },
      { type: 'quiz', question: "Milk - это?", options: ["Вода", "Сок", "Молоко"], correctAnswer: "Молоко", hint: "Milk = молоко" }
    ],
    reward: { stars: 3, message: "Excellent! Ты знаешь еду по-английски! 🍎" }
  }
]
