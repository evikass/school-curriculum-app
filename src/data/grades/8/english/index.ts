import { SubjectData, GameLesson } from '@/data/types'

export const lessons: SubjectData = {
  title: "Английский язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: [
    "Грамматика",
    "Лексика",
    "Говорение",
    "Чтение"
  ],
  detailedTopics: [
    {
      topic: "Грамматика",
      lessons: [
        {
          title: "Present Perfect",
          description: `**Present Perfect** — настоящее совершённое время.\n\n**Образование:**\nhave/has + V3 (3-я форма глагола)\n\n**Употребление:**\n- Действие已完成 (completed) в прошлом, результат в настоящем\n\n**Маркеры:**\n- ever, never, already, yet, just\n- recently, lately\n- for, since\n\n**Примеры:**\n- I have visited Paris.\n- She has never seen this film.\n- They have lived here for 5 years.`,
          tasks: ["Как образуется Present Perfect?", "Когда используется?", "Маркеры времени?"]
        },
        {
          title: "Past Simple vs Present Perfect",
          description: `**Past Simple:**\n- Действие в прошлом\n- Конкретное время\n- yesterday, last week, in 2010\n\n**Present Perfect:**\n- Результат в настоящем\n- Не важно когда\n- ever, never, just, yet\n\n**Сравнение:**\n- I visited Paris last year. (Past Simple)\n- I have visited Paris. (Present Perfect)\n\n**Правило:**\nЕсли есть точное время → Past Simple\nЕсли важен результат → Present Perfect`,
          tasks: ["Отличие Past Simple от Present Perfect?", "Когда используем yesterday?", "Когда используем ever?"]
        }
      ]
    },
    {
      topic: "Лексика",
      lessons: [
        {
          title: "Тема: Путешествия",
          description: `**Лексика по теме «Travel»:**\n\n**Существительные:**\n- journey — путешествие\n- trip — поездка\n- flight — рейс\n- destination — место назначения\n- luggage — багаж\n\n**Глаголы:**\n- to travel — путешествовать\n- to book — бронировать\n- to pack — упаковывать\n- to arrive — прибывать\n- to depart — отправляться\n\n**Выражения:**\n- go sightseeing — осматривать достопримечательности\n- go on a trip — отправиться в поездку`,
          tasks: ["Переведите: journey", "Как сказать: бронировать?", "Что такое luggage?"]
        }
      ]
    }
  ]
}

export const games: GameLesson[] = [
  {
    title: "Present Perfect",
    subject: "Английский язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Present Perfect образуется с:", options: ["have/has + V", "have/has + V3", "had + V3", "will + V"], correctAnswer: "have/has + V3", hint: "3-я форма глагола" },
      { type: 'quiz', question: "Маркер Present Perfect:", options: ["yesterday", "last week", "ever", "in 2010"], correctAnswer: "ever", hint: "Связано с настоящим" },
      { type: 'fill', question: "I have __ to Paris. (be)", correctAnswer: "been", hint: "3-я форма be" },
      { type: 'quiz', question: "С маркером yesterday используем:", options: ["Present Perfect", "Past Simple", "Present Simple", "Future Simple"], correctAnswer: "Past Simple", hint: "Точное время в прошлом" }
    ],
    reward: { stars: 3, message: "Great! You know Present Perfect! 🎓" }
  }
]
