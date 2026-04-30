import { SubjectData, GameLesson } from '@/data/types'

const createLesson = (title: string, description: string, tasks: string[], image?: string) => ({
  title, description, tasks, image, image
})

export const lessons: SubjectData = {
  title: "Проектная деятельность",
  icon: "Lightbulb",
  color: "text-violet-400",
  topics: ["Тематические коллажи", "Исследования", "Презентации", "Творческие проекты"],
  detailedTopics: [
    {
      topic: "Тематические коллажи",
      lessons: [
        createLesson("Урок 1: Моя семья", "Создание коллажа о семье.", [
          "Собрать фотографии",
          "Подобрать материалы",
          "Составить композицию",
          "Оформить коллаж"
        ],
        "/school-curriculum-app/images/lessons/grade2/projects/lesson1.svg",
        createLesson("Урок 2: Мой питомец", "Проект о домашнем животном.", [
          "Нарисовать питомца",
          "Написать рассказ",
          "Подобрать фотографии",
          "Создать плакат"
        ],
        "/school-curriculum-app/images/lessons/grade2/projects/lesson2.svg",
        createLesson("Урок 3: Времена года", "Коллаж о природе.", [
          "Выбрать сезон",
          "Найти иллюстрации",
          "Составить описание",
          "Оформить работу"
        ],
        "/school-curriculum-app/images/lessons/grade2/projects/lesson3.svg",
        createLesson("Урок 4: Мой город", "Проект о родном городе.", [
          "Нарисовать достопримечательности",
          "Написать о городе",
          "Добавить фотографии",
          "Презентовать проект"
        ],
        "/school-curriculum-app/images/lessons/grade2/projects/lesson4.svg"
      ]
      keyPoints: ['Основные понятия темы «Проектная деятельность»', 'Ключевые правила и определения', 'Применение знаний на практике'],
      examples: ['Пример по теме «Проектная деятельность»', 'Практическое задание: Проектная деятельность'],
    },
    {
      topic: "Исследовательские проекты",
      lessons: [
        createLesson("Урок 5: Исследование растений", "Наблюдение за растениями.", [
          "Выбрать растение",
          "Вести дневник наблюдений",
          "Сделать зарисовки",
          "Подготовить отчёт"
        ],
        "/school-curriculum-app/images/lessons/grade2/projects/lesson5.svg",
        createLesson("Урок 6: Погода и природа", "Наблюдение за погодой.", [
          "Записывать температуру",
          "Отмечать осадки",
          "Рисовать облачность",
          "Делать выводы"
        ],
        "/school-curriculum-app/images/lessons/grade2/projects/lesson6.svg",
        createLesson("Урок 7: Мир животных", "Исследование животных.", [
          "Выбрать животное",
          "Изучить повадки",
          "Собрать информацию",
          "Создать презентацию"
        ],
        "/school-curriculum-app/images/lessons/grade2/projects/lesson7.svg",
        createLesson("Урок 8: Экологический проект", "Забота о природе.", [
          "Определить проблему",
          "Предложить решение",
          "Выполнить действия",
          "Рассказать о результатах"
        ],
        "/school-curriculum-app/images/lessons/grade2/projects/lesson8.svg"
      ]
    },
    {
      topic: "Презентация проектов",
      lessons: [
        createLesson("Урок 9: Подготовка к защите", "Как рассказать о проекте.", [
          "Составить план рассказа",
          "Выучить основные тезисы",
          "Подготовить наглядность",
          "Потренироваться выступать"
        ],
        "/school-curriculum-app/images/lessons/grade2/projects/lesson9.svg",
        createLesson("Урок 10: Наглядные материалы", "Создание плакатов.", [
          "Выбрать содержание",
          "Распределить материал",
          "Оформить плакат",
          "Добавить иллюстрации"
        ],
        "/school-curriculum-app/images/lessons/grade2/projects/lesson10.svg",
        createLesson("Урок 11: Выступление", "Защита проекта.", [
          "Вступительное слово",
          "Основная часть",
          "Демонстрация работы",
          "Ответы на вопросы"
        ],
        "/school-curriculum-app/images/lessons/grade2/projects/lesson11.svg",
        createLesson("Урок 12: Анализ проекта", "Подведение итогов.", [
          "Что получилось хорошо",
          "Что можно улучшить",
          "Чему научились",
          "Планы на будущее"
        ],
        "/school-curriculum-app/images/lessons/grade2/projects/lesson12.svg"
      ]
    }
  ]
}

export const games = [
  {
    title: "Планирование проекта",
        image: 'data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%20400%20300%22%3E%0A%3Crect%20width%3D%22400%22%20height%3D%22300%22%20fill%3D%22%234338ca%22/%3E%0A%3Crect%20x%3D%2220%22%20y%3D%2220%22%20width%3D%22360%22%20height%3D%2260%22%20rx%3D%2210%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.15%29%22/%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%2258%22%20text-anchor%3D%22middle%22%20fill%3D%22white%22%20font-size%3D%2220%22%20font-weight%3D%22bold%22%20font-family%3D%22sans-serif%22%3E%D0%9F%D0%BB%D0%B0%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0%3C/text%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%22190%22%20text-anchor%3D%22middle%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.7%29%22%20font-size%3D%2256%22%20font-family%3D%22sans-serif%22%3E%F0%9F%93%8B%3C/text%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%22265%22%20text-anchor%3D%22middle%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.5%29%22%20font-size%3D%2214%22%20font-family%3D%22sans-serif%22%3E2%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%20%C2%B7%20%D0%9F%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D1%8B%3C/text%3E%0A%3C/svg%3E',
    subject: "Проектная деятельность",
    icon: "Lightbulb",
    color: "text-violet-400",
    tasks: [
      {
        type: 'quiz',
        question: "С чего начинается любой проект?",
        options: ["С идеи", "С конца", "С середины", "Никто не знает", "Не знаю"],
        correctAnswer: "С идеи",
        hint: "Сначала нужно придумать!"
        keyPoints: ['Основные понятия темы «Планирование проекта»', 'Ключевые правила и определения', 'Применение знаний на практике'],
        examples: ['Пример по теме «Планирование проекта»', 'Практическое задание: Планирование проекта'],
      },
      {
        type: 'quiz',
        question: "Какой этап проекта должен быть первым?",
        options: ["Защита", "Подготовка", "Исследование", "Презентация", "Не знаю"],
        correctAnswer: "Исследование",
        hint: "Сначала изучи тему!"
      },
      {
        type: 'find',
        question: "Что нужно для проекта?",
        options: ["Идея", "План", "Материалы", "Все ответы верны", "Время"],
        correctAnswer: ["Все ответы верны"],
        hint: "Для проекта нужно многое!"
      },
      {
        type: 'quiz',
        question: "Что значит защитить проект?",
        options: ["Выступить и рассказать", "Написать текст", "Нарисовать рисунок", "Спрятать проект", "Не знаю"],
        correctAnswer: "Выступить и рассказать",
        hint: "Как называется выступление?"
      }
    ],
    reward: { stars: 3, message: "Отлично! Ты понимаешь, как делать проекты! 💡" }
  },
  {
    title: "Творческий проект",
        image: 'data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%20400%20300%22%3E%0A%3Crect%20width%3D%22400%22%20height%3D%22300%22%20fill%3D%22%234338ca%22/%3E%0A%3Crect%20x%3D%2220%22%20y%3D%2220%22%20width%3D%22360%22%20height%3D%2260%22%20rx%3D%2210%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.15%29%22/%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%2258%22%20text-anchor%3D%22middle%22%20fill%3D%22white%22%20font-size%3D%2220%22%20font-weight%3D%22bold%22%20font-family%3D%22sans-serif%22%3E%D0%A2%D0%B2%D0%BE%D1%80%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%3C/text%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%22190%22%20text-anchor%3D%22middle%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.7%29%22%20font-size%3D%2256%22%20font-family%3D%22sans-serif%22%3E%F0%9F%93%8B%3C/text%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%22265%22%20text-anchor%3D%22middle%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.5%29%22%20font-size%3D%2214%22%20font-family%3D%22sans-serif%22%3E2%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%20%C2%B7%20%D0%9F%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D1%8B%3C/text%3E%0A%3C/svg%3E',
    subject: "Проектная деятельность",
    icon: "Lightbulb",
    color: "text-violet-400",
    tasks: [
      {
        type: 'quiz',
        question: "Какой проект можно сделать о семье?",
        options: ["Коллаж", "Урок", "Контрольная", "Никто не знает", "Не знаю"],
        correctAnswer: "Коллаж",
        hint: "Что можно показать фотографиями?"
        keyPoints: ['Основные понятия темы «Творческий проект»', 'Ключевые правила и определения', 'Применение знаний на практике'],
        examples: ['Пример по теме «Творческий проект»', 'Практическое задание: Творческий проект'],
      },
      {
        type: 'quiz',
        question: "Что такое презентация проекта?",
        options: ["Рассказ о работе", "Проверка", "Перемена", "Никто не знает", "Не знаю"],
        correctAnswer: "Рассказ о работе",
        hint: "Нужно показать свою работу"
      },
      {
        type: 'find',
        question: "Выбери темы для проекта:",
        options: ["Мой город", "1+1=2", "Мой питомец", "Буква А", "Моя семья"],
        correctAnswer: ["Мой город", "Мой питомец"],
        hint: "Тема должна быть интересной и развёрнутой"
      },
      {
        type: 'quiz',
        question: "Кто может помочь с проектом?",
        options: ["Родители", "Учитель", "Никто", "Все могут помочь", "Не знаю"],
        correctAnswer: "Все могут помочь",
        hint: "Помощь важна!"
      }
    ],
    reward: { stars: 3, message: "Супер! Ты готов к творческим проектам! 🎨" }
  },
  {
    title: "Выбор темы проекта 💡",
        image: 'data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%20400%20300%22%3E%0A%3Crect%20width%3D%22400%22%20height%3D%22300%22%20fill%3D%22%234338ca%22/%3E%0A%3Crect%20x%3D%2220%22%20y%3D%2220%22%20width%3D%22360%22%20height%3D%2260%22%20rx%3D%2210%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.15%29%22/%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%2258%22%20text-anchor%3D%22middle%22%20fill%3D%22white%22%20font-size%3D%2220%22%20font-weight%3D%22bold%22%20font-family%3D%22sans-serif%22%3E%D0%92%D1%8B%D0%B1%D0%BE%D1%80%20%D1%82%D0%B5%D0%BC%D1%8B%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0%20%F0%9F%92%A1%3C/text%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%22190%22%20text-anchor%3D%22middle%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.7%29%22%20font-size%3D%2256%22%20font-family%3D%22sans-serif%22%3E%F0%9F%93%8B%3C/text%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%22265%22%20text-anchor%3D%22middle%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.5%29%22%20font-size%3D%2214%22%20font-family%3D%22sans-serif%22%3E2%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%20%C2%B7%20%D0%9F%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D1%8B%3C/text%3E%0A%3C/svg%3E',
    subject: "Проектная деятельность",
    icon: "Lightbulb",
    color: "text-yellow-400",
    tasks: [
      {
        type: 'quiz',
        question: "С чего начинается любой проект?",
        options: ["С защиты", "С идеи", "С поиска материалов", "Никто не знает", "Не знаю"],
        correctAnswer: "С идеи",
        hint: "Идея — начало проекта"
        keyPoints: ['Основные понятия темы «Выбор темы проекта 💡»', 'Ключевые правила и определения', 'Применение знаний на практике'],
        examples: ['Пример по теме «Выбор темы проекта 💡»', 'Практическое задание: Выбор темы проекта 💡'],
      },
      {
        type: 'find',
        question: "Где можно найти идею для проекта?",
        options: ["В книгах", "В интернете", "В природе", "В магазине", "У друзей"],
        correctAnswer: ["В книгах", "В интернете", "В природе", "У друзей"],
        hint: "Идеи повсюду"
      },
      {
        type: 'quiz',
        question: "Какой должна быть тема проекта?",
        options: ["Сложной", "Интересной", "Неизвестной", "Никто не знает", "Не знаю"],
        correctAnswer: "Интересной",
        hint: "Проект должен быть интересен"
      },
      {
        type: 'find',
        question: "Что помогает выбрать тему?",
        options: ["Интерес", "Возможности", "Польза", "Сложность", "Время"],
        correctAnswer: ["Интерес", "Возможности", "Польза"],
        hint: "Важные критерии"
      }
    ],
    reward: { stars: 3, message: "Отлично! Ты умеешь выбирать темы! 💡" }
  },
  {
    title: "Сбор информации 🔍",
        image: 'data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%20400%20300%22%3E%0A%3Crect%20width%3D%22400%22%20height%3D%22300%22%20fill%3D%22%234338ca%22/%3E%0A%3Crect%20x%3D%2220%22%20y%3D%2220%22%20width%3D%22360%22%20height%3D%2260%22%20rx%3D%2210%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.15%29%22/%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%2258%22%20text-anchor%3D%22middle%22%20fill%3D%22white%22%20font-size%3D%2220%22%20font-weight%3D%22bold%22%20font-family%3D%22sans-serif%22%3E%D0%A1%D0%B1%D0%BE%D1%80%20%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%B8%20%F0%9F%94%8D%3C/text%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%22190%22%20text-anchor%3D%22middle%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.7%29%22%20font-size%3D%2256%22%20font-family%3D%22sans-serif%22%3E%F0%9F%93%8B%3C/text%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%22265%22%20text-anchor%3D%22middle%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.5%29%22%20font-size%3D%2214%22%20font-family%3D%22sans-serif%22%3E2%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%20%C2%B7%20%D0%9F%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D1%8B%3C/text%3E%0A%3C/svg%3E',
    subject: "Проектная деятельность",
    icon: "Lightbulb",
    color: "text-yellow-400",
    tasks: [
      {
        type: 'quiz',
        question: "Где можно найти информацию для проекта?",
        options: ["В книгах", "В интернете", "Только у учителя", "Никто не знает", "Не знаю"],
        correctAnswer: "В книгах",
        hint: "Много источников"
        keyPoints: ['Основные понятия темы «Сбор информации 🔍»', 'Ключевые правила и определения', 'Применение знаний на практике'],
        examples: ['Пример по теме «Сбор информации 🔍»', 'Практическое задание: Сбор информации 🔍'],
      },
      {
        type: 'find',
        question: "Найди источники информации:",
        options: ["Книги", "Интернет", "Интервью", "Фантазия", "Энциклопедии"],
        correctAnswer: ["Книги", "Интернет", "Интервью", "Энциклопедии"],
        hint: "Где берём информацию"
      },
      {
        type: 'quiz',
        question: "Что нужно делать с найденной информацией?",
        options: ["Запомнить", "Записать", "Забыть", "Никто не знает", "Не знаю"],
        correctAnswer: "Записать",
        hint: "Записи важны"
      },
      {
        type: 'find',
        question: "Как можно записать информацию?",
        options: ["Текст", "Рисунок", "Таблица", "Схема", "На память"],
        correctAnswer: ["Текст", "Рисунок", "Таблица", "Схема"],
        hint: "Разные способы записи"
      }
    ],
    reward: { stars: 3, message: "Супер! Ты умеешь искать информацию! 🔍" }
  },
  {
    title: "Создание продукта 🛠️",
        image: 'data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%20400%20300%22%3E%0A%3Crect%20width%3D%22400%22%20height%3D%22300%22%20fill%3D%22%234338ca%22/%3E%0A%3Crect%20x%3D%2220%22%20y%3D%2220%22%20width%3D%22360%22%20height%3D%2260%22%20rx%3D%2210%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.15%29%22/%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%2258%22%20text-anchor%3D%22middle%22%20fill%3D%22white%22%20font-size%3D%2220%22%20font-weight%3D%22bold%22%20font-family%3D%22sans-serif%22%3E%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%20%F0%9F%9B%A0%EF%B8%8F%3C/text%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%22190%22%20text-anchor%3D%22middle%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.7%29%22%20font-size%3D%2256%22%20font-family%3D%22sans-serif%22%3E%F0%9F%93%8B%3C/text%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%22265%22%20text-anchor%3D%22middle%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.5%29%22%20font-size%3D%2214%22%20font-family%3D%22sans-serif%22%3E2%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%20%C2%B7%20%D0%9F%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D1%8B%3C/text%3E%0A%3C/svg%3E',
    subject: "Проектная деятельность",
    icon: "Lightbulb",
    color: "text-yellow-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое продукт проекта?",
        options: ["Идея", "Готовый результат", "План", "Никто не знает", "Не знаю"],
        correctAnswer: "Готовый результат",
        hint: "То, что получилось"
        keyPoints: ['Основные понятия темы «Создание продукта 🛠️»', 'Ключевые правила и определения', 'Применение знаний на практике'],
        examples: ['Пример по теме «Создание продукта 🛠️»', 'Практическое задание: Создание продукта 🛠️'],
      },
      {
        type: 'find',
        question: "Каким может быть продукт проекта?",
        options: ["Поделка", "Презентация", "Книга", "Видео", "Текст"],
        correctAnswer: ["Поделка", "Презентация", "Книга", "Видео"],
        hint: "Разные продукты"
      },
      {
        type: 'quiz',
        question: "Что важно при создании продукта?",
        options: ["Скорость", "Качество", "Красота", "Никто не знает", "Не знаю"],
        correctAnswer: "Качество",
        hint: "Делай хорошо"
      },
      {
        type: 'find',
        question: "Что нужно для создания продукта?",
        options: ["Материалы", "Инструменты", "Время", "Деньги", "Терпение"],
        correctAnswer: ["Материалы", "Инструменты", "Время", "Терпение"],
        hint: "Всё для работы"
      }
    ],
    reward: { stars: 3, message: "Отлично! Ты умеешь создавать! 🛠️" }
  },
  {
    title: "Защита проекта 🎤",
        image: 'data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%20400%20300%22%3E%0A%3Crect%20width%3D%22400%22%20height%3D%22300%22%20fill%3D%22%234338ca%22/%3E%0A%3Crect%20x%3D%2220%22%20y%3D%2220%22%20width%3D%22360%22%20height%3D%2260%22%20rx%3D%2210%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.15%29%22/%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%2258%22%20text-anchor%3D%22middle%22%20fill%3D%22white%22%20font-size%3D%2220%22%20font-weight%3D%22bold%22%20font-family%3D%22sans-serif%22%3E%D0%97%D0%B0%D1%89%D0%B8%D1%82%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0%20%F0%9F%8E%A4%3C/text%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%22190%22%20text-anchor%3D%22middle%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.7%29%22%20font-size%3D%2256%22%20font-family%3D%22sans-serif%22%3E%F0%9F%93%8B%3C/text%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%22265%22%20text-anchor%3D%22middle%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.5%29%22%20font-size%3D%2214%22%20font-family%3D%22sans-serif%22%3E2%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%20%C2%B7%20%D0%9F%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D1%8B%3C/text%3E%0A%3C/svg%3E',
    subject: "Проектная деятельность",
    icon: "Lightbulb",
    color: "text-yellow-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое защита проекта?",
        options: ["Спрятать проект", "Рассказать о проекте", "Сделать проект", "Никто не знает", "Не знаю"],
        correctAnswer: "Рассказать о проекте",
        hint: "Презентация работы"
        keyPoints: ['Основные понятия темы «Защита проекта 🎤»', 'Ключевые правила и определения', 'Применение знаний на практике'],
        examples: ['Пример по теме «Защита проекта 🎤»', 'Практическое задание: Защита проекта 🎤'],
      },
      {
        type: 'find',
        question: "Что нужно для защиты проекта?",
        options: ["Презентация", "Доклад", "Продукт", "Костюм", "Ответы на вопросы"],
        correctAnswer: ["Презентация", "Доклад", "Продукт", "Ответы на вопросы"],
        hint: "Готовься к защите"
      },
      {
        type: 'quiz',
        question: "Как говорить на защите?",
        options: ["Быстро", "Чётко и понятно", "Тихо", "Никто не знает", "Не знаю"],
        correctAnswer: "Чётко и понятно",
        hint: "Тебя должны понять"
      },
      {
        type: 'find',
        question: "Какие вопросы могут задать?",
        options: ["Зачем делал?", "Как делал?", "Что получилось?", "Сколько лет?", "Где живёшь?"],
        correctAnswer: ["Зачем делал?", "Как делал?", "Что получилось?"],
        hint: "О самом проекте"
      }
    ],
    reward: { stars: 3, message: "Круто! Ты готов к защите! 🎤" }
  },
  {
    title: "Работа в команде 👥",
        image: 'data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%20400%20300%22%3E%0A%3Crect%20width%3D%22400%22%20height%3D%22300%22%20fill%3D%22%234338ca%22/%3E%0A%3Crect%20x%3D%2220%22%20y%3D%2220%22%20width%3D%22360%22%20height%3D%2260%22%20rx%3D%2210%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.15%29%22/%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%2258%22%20text-anchor%3D%22middle%22%20fill%3D%22white%22%20font-size%3D%2220%22%20font-weight%3D%22bold%22%20font-family%3D%22sans-serif%22%3E%D0%A0%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%D0%B2%20%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B5%20%F0%9F%91%A5%3C/text%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%22190%22%20text-anchor%3D%22middle%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.7%29%22%20font-size%3D%2256%22%20font-family%3D%22sans-serif%22%3E%F0%9F%93%8B%3C/text%3E%0A%3Ctext%20x%3D%22200%22%20y%3D%22265%22%20text-anchor%3D%22middle%22%20fill%3D%22rgba%28255%2C255%2C255%2C0.5%29%22%20font-size%3D%2214%22%20font-family%3D%22sans-serif%22%3E2%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%20%C2%B7%20%D0%9F%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D1%8B%3C/text%3E%0A%3C/svg%3E',
    subject: "Проектная деятельность",
    icon: "Lightbulb",
    color: "text-yellow-400",
    tasks: [
      {
        type: 'quiz',
        question: "Зачем работать в команде?",
        options: ["Быстрее", "Интереснее", "Легче", "Никто не знает", "Не знаю"],
        correctAnswer: "Быстрее",
        hint: "Вместе — лучше"
        keyPoints: ['Основные понятия темы «Работа в команде 👥»', 'Ключевые правила и определения', 'Применение знаний на практике'],
        examples: ['Пример по теме «Работа в команде 👥»', 'Практическое задание: Работа в команде 👥'],
      },
      {
        type: 'find',
        question: "Какие роли есть в команде?",
        options: ["Лидер", "Исследователь", "Творец", "Зритель", "Оформитель"],
        correctAnswer: ["Лидер", "Исследователь", "Творец", "Оформитель"],
        hint: "У каждого своя роль"
      },
      {
        type: 'quiz',
        question: "Как решать споры в команде?",
        options: ["Драться", "Договариваться", "Обижаться", "Никто не знает", "Не знаю"],
        correctAnswer: "Договариваться",
        hint: "Дружба важна"
      },
      {
        type: 'find',
        question: "Что важно в командной работе?",
        options: ["Слушать других", "Помогать", "Критиковать", "Делиться идеями", "Поддерживать"],
        correctAnswer: ["Слушать других", "Помогать", "Делиться идеями", "Поддерживать"],
        hint: "Команда — одна семья"
      }
    ],
    reward: { stars: 3, message: "Супер! Ты умеешь работать в команде! 👥" }
  }
]

