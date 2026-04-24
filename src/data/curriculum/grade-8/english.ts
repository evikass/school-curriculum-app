import { Subject } from '../../types'

export const grade8English: Subject = {
  "title": "Иностранный язык",
  "icon": "Languages",
  "color": "text-pink-400",
  "topics": [
    "Passive Voice",
    "Conditionals"
  ],
  "detailedTopics": [
    {
      "topic": "Passive Voice",
      "lessons": [
        {
          "title": "Урок 1: Passive Voice — пассивный залог",
          "description": "Образование и употребление пассивного залога",
          "tasks": [
            "Образовать пассив от глагола write",
            "Перевести: Книга была написана Пушкиным",
            "Определить время в пассивном залоге",
            "Перестроить активное предложение в пассивное"
          ],
          "theory": "Пассивный залог (Passive Voice) используется, когда действие совершается над подлежащим. Формула: be + V3 (причастие прошедшего времени). Времена: Present Simple Passive — am/is/are + V3; Past Simple Passive — was/were + V3; Future Simple Passive — will be + V3. Пассивный залог часто используется, когда исполнитель действия неизвестен или неважен.",
          "content": "## Passive Voice — пассивный залог\n\n### Формула\n**be + V3** (причастие прошедшего времени)\n\n### Времена\n| Время | Формула | Пример |\n|-------|---------|--------|\n| Present Simple | am/is/are + V3 | English is spoken worldwide |\n| Past Simple | was/were + V3 | The book was written in 1860 |\n| Future Simple | will be + V3 | The test will be done tomorrow |\n\n### Когда использовать\n1. Исполнитель неизвестен: The window was broken\n2. Исполнитель неважен: The letter was sent\n3. Действие важнее исполнителя",
          "keyPoints": [
            "Пассив: be + V3",
            "Present: am/is/are + V3",
            "Past: was/were + V3",
            "Future: will be + V3"
          ],
          "examples": [
            "Active: Pushkin wrote the poem → Passive: The poem was written by Pushkin",
            "The homework is done every day",
            "The bridge was built in 1990"
          ],
          "facts": [
            "Пассивный залог чаще используется в английском, чем в русском",
            "В научных текстах пассив используется очень часто",
            "By + исполнитель указывает, кто совершил действие"
          ],
          "image": "/school-curriculum-app/images/lessons/grade-8/english/passive-voice.svg"
        }
      ]
    },
    {
      "topic": "Conditionals",
      "lessons": [
        {
          "title": "Урок 2: Conditionals — условные предложения",
          "description": "Типы условных предложений в английском языке",
          "tasks": [
            "Образовать условное предложение 1 типа",
            "Образовать условное предложение 2 типа",
            "Отличить реальное условие от нереального",
            "Перевести: Если бы я был богат, я бы путешествовал"
          ],
          "theory": "Условные предложения (Conditionals) выражают условие и его результат. Тип 0: If + Present Simple, Present Simple (общие истины). Тип 1: If + Present Simple, Future Simple (реальное условие). Тип 2: If + Past Simple, would + V1 (нереальное условие в настоящем). Тип 3: If + Past Perfect, would have + V3 (нереальное условие в прошлом).",
          "content": "## Conditionals — условные предложения\n\n### Тип 0 (Общие истины)\nIf you heat water to 100°C, it boils.\n\n### Тип 1 (Реальное условие)\nIf + Present Simple → will + V1\nIf it rains, I will stay at home.\n\n### Тип 2 (Нереальное настоящее)\nIf + Past Simple → would + V1\nIf I were rich, I would travel. (Если бы я был богат...)\n\n### Тип 3 (Нереальное прошлое)\nIf + Past Perfect → would have + V3\nIf I had studied, I would have passed. (Если бы я учился...)",
          "keyPoints": [
            "Тип 1: реальное условие (if + Present, will)",
            "Тип 2: нереальное настоящее (if + Past, would)",
            "Тип 3: нереальное прошлое (if + Past Perfect, would have)",
            "If I were — вместо was в типе 2"
          ],
          "examples": [
            "If it rains, I'll stay home (Тип 1)",
            "If I were you, I'd agree (Тип 2)",
            "If I had known, I'd have come (Тип 3)"
          ],
          "facts": [
            "В типе 2 используется were для всех лиц",
            "Conditionals — одна из самых сложных тем английского",
            "Смешанные условные тоже существуют"
          ],
          "image": "/school-curriculum-app/images/lessons/grade-8/english/conditionals.svg"
        }
      ]
    }
  ]
}
