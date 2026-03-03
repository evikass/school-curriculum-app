import { SubjectData, GameLesson } from '@/data/types'

export const lessons: SubjectData = {
  title: "Информатика",
  icon: "Code",
  color: "text-green-400",
  topics: [
    "Системы счисления",
    "Алгоритмы",
    "Программирование",
    "Подготовка к ЕГЭ"
  ],
  detailedTopics: [
    {
      topic: "Системы счисления",
      lessons: [
        {
          title: "Позиционные системы счисления",
          description: `**Система счисления** — способ записи чисел.\n\n**Позиционные системы:**\n- Значение цифры зависит от позиции\n\n**Двоичная система:**\n- Основание 2\n- Цифры: 0, 1\n\n**Перевод из десятичной:**\n- Делить на основание\n- Записывать остатки\n\n**Пример: 13₁₀ = 1101₂**\n13 ÷ 2 = 6 (ост. 1)\n6 ÷ 2 = 3 (ост. 0)\n3 ÷ 2 = 1 (ост. 1)\n1 ÷ 2 = 0 (ост. 1)\n\n**Шестнадцатеричная:**\n- Основание 16\n- Цифры: 0-9, A-F`,
          tasks: ["Переведите 10 в двоичную", "Что такое основание?", "Цифры шестнадцатеричной системы?"]
        }
      ]
    }
  ]
}

export const games: GameLesson[] = [
  {
    title: "Системы счисления",
    subject: "Информатика",
    icon: "Code",
    color: "text-green-400",
    tasks: [
      { type: 'fill', question: "13₁₀ = __₂", correctAnswer: "1101", hint: "1101 в двоичной" },
      { type: 'quiz', question: "Основание двоичной системы:", options: ["8", "10", "2", "16"], correctAnswer: "2", hint: "Два символа" },
      { type: 'quiz', question: "В шестнадцатеричной системе:", options: ["8 цифр", "10 цифр", "16 цифр", "2 цифры"], correctAnswer: "16 цифр", hint: "0-9 и A-F" },
      { type: 'fill', question: "10₁₀ = __₂", correctAnswer: "1010", hint: "Двоичное 10" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь системы счисления! 💻" }
  }
]
