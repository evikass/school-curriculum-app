import { SubjectData, GameLesson } from '@/data/types'

export const lessons: SubjectData = {
  title: "Иностранный язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: [
    "Путешествия и туризм",
    "Профессии и карьера",
    "Экология и окружающая среда",
    "Средства массовой информации",
    "Научно-технический прогресс"
  ],
  detailedTopics: [
    {
      topic: "Путешествия и туризм",
      lessons: [
        {
          title: "Виды путешествий",
          description: `Изучение лексики по теме путешествия: авиаперелёты, железнодорожные поездки, круизы, автотуризм.

**Travel vocabulary:** flight (полёт), journey (путешествие), destination (место назначения), accommodation (размещение), itinerary (маршрут), sightseeing (осмотр достопримечательностей).

**Present Perfect для описания опыта путешествий:**
- I have visited Paris. (Я посетил Париж.)
- She has never been to London. (Она никогда не была в Лондоне.)
- Have you ever travelled by train? (Вы когда-нибудь путешествовали на поезде?)`,
          tasks: [
            "Как перевести слово destination?",
            "Когда используется Present Perfect для описания путешествий?",
            "Образуйте Past Participle от глагола be",
            "Составьте предложение: Я никогда не был в Японии"
          ]
        },
        {
          title: "В аэропорту",
          description: `Лексика для ориентирования в аэропорту: регистрация, паспортный контроль, таможня, посадка.

**Airport vocabulary:** check-in (регистрация), boarding pass (посадочный талон), departure lounge (зал вылета), gate (выход на посадку), customs (таможня), baggage claim (получение багажа).

**Useful phrases:**
- Where is the check-in counter? (Где стойка регистрации?)
- I'd like a window seat. (Я хотел бы место у окна.)
- My flight has been delayed. (Мой рейс задержан.)
- I've lost my luggage. (Я потерял багаж.)`,
          tasks: [
            "Как сказать «посадочный талон» на английском?",
            "Где получают багаж после прилёта?",
            "Переведите: I'd like an aisle seat",
            "Что означает фраза «boarding pass»?"
          ]
        },
        {
          title: "В гостинице",
          description: `Бронирование номера, регистрация заезда и выезда, решение проблем в отеле.

**Hotel vocabulary:** reservation (бронирование), check-in/out (заезд/выезд), room service (обслуживание номеров), amenities (удобства), deposit (залог), complimentary (бесплатный).

**Making a reservation:**
- I'd like to book a room for two nights. (Я хотел бы забронировать номер на две ночи.)
- Do you have any vacancies? (У вас есть свободные номера?)
- What's the rate per night? (Какая цена за ночь?)
- Is breakfast included? (Завтрак включён?)`,
          tasks: [
            "Что означает слово complimentary?",
            "Как забронировать номер на английском?",
            "Переведите: amenities",
            "Как спросить, включён ли завтрак?"
          ]
        }
      ]
    },
    {
      topic: "Профессии и карьера",
      lessons: [
        {
          title: "Мир профессий",
          description: `Изучение названий профессий, описание обязанностей и требований. Модальные глаголы для описания профессиональных требований.

**Professions:** doctor (врач), engineer (инженер), lawyer (юрист), accountant (бухгалтер), software developer (разработчик ПО), journalist (журналист), architect (архитектор).

**Modal verbs for job requirements:**
- You must have a medical degree to become a doctor. (Вы должны иметь медицинскую степень.)
- You should be good at math for engineering. (Вам следует быть хорошим в математике.)
- You need to be creative as a designer. (Вам нужно быть креативным.)`,
          tasks: [
            "Как будет «архитектор» на английском?",
            "Какой модальный глагол выражает обязательность?",
            "Переведите: software developer",
            "Опишите требования к профессии врача"
          ]
        },
        {
          title: "Поиск работы",
          description: `Написание резюме, сопроводительного письма, подготовка к собеседованию.

**Job search vocabulary:** CV/resume (резюме), cover letter (сопроводительное письмо), interview (собеседование), vacancy (вакансия), applicant (соискатель), salary (зарплата), benefits (льготы).

**Interview phrases:**
- Tell me about yourself. (Расскажите о себе.)
- Why do you want this job? (Почему вы хотите эту работу?)
- What are your strengths and weaknesses? (Какие ваши сильные и слабые стороны?)
- When can you start? (Когда вы можете начать?)`,
          tasks: [
            "Чем отличается CV от cover letter?",
            "Как ответить на вопрос о сильных сторонах?",
            "Переведите: vacancy",
            "Какие вопросы задают на собеседовании?"
          ]
        },
        {
          title: "Деловое общение",
          description: `Деловая переписка, телефонные разговоры, презентации. Профессиональный этикет.

**Business vocabulary:** meeting (встреча), deadline (крайний срок), proposal (предложение), negotiation (переговоры), contract (контракт), partnership (партнёрство).

**Email phrases:**
- I am writing to inquire about... (Я пишу, чтобы узнать о...)
- Please find attached... (Пожалуйста, найдите во вложении...)
- I look forward to hearing from you. (Жду вашего ответа.)
- Thank you for your consideration. (Спасибо за рассмотрение.)`,
          tasks: [
            "Что такое deadline?",
            "Как начать деловое письмо?",
            "Переведите: negotiation",
            "Как вежливо закончить деловое письмо?"
          ]
        }
      ]
    },
    {
      topic: "Экология и окружающая среда",
      lessons: [
        {
          title: "Экологические проблемы",
          description: `Изучение лексики по теме экологии: загрязнение, изменение климата, исчезновение видов.

**Environmental problems:** pollution (загрязнение), climate change (изменение климата), global warming (глобальное потепление), deforestation (вырубка лесов), endangered species (исчезающие виды).

**Causes and effects:**
- Pollution causes health problems. (Загрязнение вызывает проблемы со здоровьем.)
- Deforestation leads to habitat loss. (Вырубка лесов ведёт к потере среды обитания.)
- Carbon emissions contribute to global warming. (Выбросы углерода способствуют глобальному потеплению.)`,
          tasks: [
            "Что означает endangered species?",
            "Какие причины глобального потепления?",
            "Переведите: deforestation",
            "Опишите последствия загрязнения"
          ]
        },
        {
          title: "Защита окружающей среды",
          description: `Способы защиты природы: переработка, энергосбережение, устойчивое развитие.

**Environmental protection:** recycling (переработка), renewable energy (возобновляемая энергия), sustainable development (устойчивое развитие), conservation (сохранение), eco-friendly (экологичный).

**Actions:**
- We should reduce, reuse, and recycle. (Мы должны сокращать, повторно использовать и перерабатывать.)
- We can use public transport instead of driving. (Мы можем использовать общественный транспорт.)
- We need to protect natural habitats. (Нам нужно защищать естественную среду.)`,
          tasks: [
            "Что означает eco-friendly?",
            "Назовите три принципа защиты среды (3 R's)",
            "Переведите: renewable energy",
            "Как можно снизить углеродный след?"
          ]
        }
      ]
    },
    {
      topic: "Средства массовой информации",
      lessons: [
        {
          title: "Типы СМИ",
          description: `Изучение типов средств массовой информации: печать, радио, телевидение, интернет-медиа.

**Media types:** newspaper (газета), magazine (журнал), television (телевидение), radio (радио), online news (онлайн-новости), social media (социальные сети).

**Media vocabulary:** journalist (журналист), editor (редактор), headline (заголовок), article (статья), broadcast (трансляция), coverage (освещение).`,
          tasks: [
            "Чем отличается newspaper от magazine?",
            "Что такое headline?",
            "Переведите: broadcast",
            "Назовите типы СМИ"
          ]
        },
        {
          title: "Социальные сети",
          description: `Влияние социальных сетей на общество, преимущества и недостатки. Безопасность в интернете.

**Social media vocabulary:** platform (платформа), follower (подписчик), post (публикация), like (лайк), share (поделиться), comment (комментарий), viral (вирусный/популярный).

**Advantages:** staying connected, sharing information, building communities.
**Disadvantages:** fake news, cyberbullying, addiction, privacy concerns.`,
          tasks: [
            "Что означает viral content?",
            "Какие опасности социальных сетей?",
            "Переведите: cyberbullying",
            "Как защитить личную информацию в сети?"
          ]
        }
      ]
    },
    {
      topic: "Научно-технический прогресс",
      lessons: [
        {
          title: "Технологии будущего",
          description: `Изучение лексики по теме технологий: искусственный интеллект, роботы, виртуальная реальность.

**Technology vocabulary:** artificial intelligence (искусственный интеллект), robotics (робототехника), virtual reality (виртуальная реальность), automation (автоматизация), innovation (инновация).

**Future technologies:** self-driving cars (автопилотируемые автомобили), smart homes (умные дома), medical robots (медицинские роботы), space exploration (освоение космоса).`,
          tasks: [
            "Как расшифровывается AI?",
            "Что такое virtual reality?",
            "Переведите: automation",
            "Опишите технологии будущего"
          ]
        },
        {
          title: "Цифровая грамотность",
          description: `Безопасное использование технологий, защита личных данных, критическое мышление в цифровую эпоху.

**Digital literacy vocabulary:** cybersecurity (кибербезопасность), password (пароль), encryption (шифрование), phishing (фишинг), malware (вредоносное ПО), backup (резервная копия).

**Online safety tips:**
- Use strong passwords. (Используйте надёжные пароли.)
- Don't share personal information. (Не делитесь личной информацией.)
- Be careful with email attachments. (Будьте осторожны с вложениями.)
- Update your software regularly. (Регулярно обновляйте ПО.)`,
          tasks: [
            "Что такое phishing?",
            "Как создать надёжный пароль?",
            "Переведите: backup",
            "Какие правила цифровой безопасности?"
          ]
        }
      ]
    }
  ]
}

export const games: GameLesson[] = [
  {
    title: "Виды путешествий",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Present Perfect для описания опыта путешествий:?",
        options: ["Специальный метод вычисления", "Это понятие из другого раздела", "Понятие, обратное данному", "Вспомогательный термин", "I have visited Paris. (Я посетил Париж.)"],
        correctAnswer: "I have visited Paris. (Я посетил Париж.)",
        hint: "Вспомни определение из урока про Present Perfect для описания опыта путешествий:"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Travel vocabulary:»",
        options: ["Связанный термин", "Дополнительный элемент", "Другой термин", "Вспомогательное понятие", "Travel vocabulary:"],
        correctAnswer: "Travel vocabulary:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: Изучение лексики по теме путешествия: авиаперелёты, железнодорожные поездки, круизы, автотуризм.",
        options: ["Частично верно", "Да, верно", "Нет, неверно", "Зависит от контекста", "Только в некоторых случаях"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: чения), accommodation (размещение), itinerary (маршрут), sightseeing (осмотр достопримечательностей).",
        options: ["Частично верно", "Да, верно", "Нет, неверно", "Только в некоторых случаях", "Зависит от контекста"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: Present Perfect для описания опыта путешествий: - I have visited Paris.",
        options: ["Да, верно", "Нет, неверно", "Зависит от контекста", "Частично верно", "Только в некоторых случаях"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "В аэропорту",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Useful phrases:?",
        options: ["Вспомогательный термин", "Понятие, обратное данному", "Where is the check-in counter? (Где стойка регистрации?)", "Это понятие из другого раздела", "Специальный метод вычисления"],
        correctAnswer: "Where is the check-in counter? (Где стойка регистрации?)",
        hint: "Вспомни определение из урока про Useful phrases:"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Airport vocabulary:»",
        options: ["Airport vocabulary:", "Вспомогательное понятие", "Дополнительный элемент", "Связанный термин", "Другой термин"],
        correctAnswer: "Airport vocabulary:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Useful phrases:»",
        options: ["Связанный термин", "Дополнительный элемент", "Другой термин", "Вспомогательное понятие", "Useful phrases:"],
        correctAnswer: "Useful phrases:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: Лексика для ориентирования в аэропорту: регистрация, паспортный контроль, таможня, посадка.",
        options: ["Зависит от контекста", "Только в некоторых случаях", "Нет, неверно", "Частично верно", "Да, верно"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: re lounge (зал вылета), gate (выход на посадку), customs (таможня), baggage claim (получение багажа).",
        options: ["Да, верно", "Частично верно", "Только в некоторых случаях", "Нет, неверно", "Зависит от контекста"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "В гостинице",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Making a reservation:?",
        options: ["Это понятие из другого раздела", "Специальный метод вычисления", "Понятие, обратное данному", "Вспомогательный термин", "I'd like to book a room for two nights. (Я хотел бы забронировать номер на две н..."],
        correctAnswer: "I'd like to book a room for two nights. (Я хотел бы забронировать номер на две н...",
        hint: "Вспомни определение из урока про Making a reservation:"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Hotel vocabulary:»",
        options: ["Другой термин", "Hotel vocabulary:", "Дополнительный элемент", "Связанный термин", "Вспомогательное понятие"],
        correctAnswer: "Hotel vocabulary:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Making a reservation:»",
        options: ["Связанный термин", "Making a reservation:", "Вспомогательное понятие", "Дополнительный элемент", "Другой термин"],
        correctAnswer: "Making a reservation:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: Бронирование номера, регистрация заезда и выезда, решение проблем в отеле.",
        options: ["Нет, неверно", "Зависит от контекста", "Только в некоторых случаях", "Да, верно", "Частично верно"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: om service (обслуживание номеров), amenities (удобства), deposit (залог), complimentary (бесплатный).",
        options: ["Частично верно", "Нет, неверно", "Только в некоторых случаях", "Зависит от контекста", "Да, верно"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Мир профессий",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Modal verbs for job requirements:?",
        options: ["You must have a medical degree to become a doctor. (Вы должны иметь медицинскую ...", "Понятие, обратное данному", "Специальный метод вычисления", "Это понятие из другого раздела", "Вспомогательный термин"],
        correctAnswer: "You must have a medical degree to become a doctor. (Вы должны иметь медицинскую ...",
        hint: "Вспомни определение из урока про Modal verbs for job requirements:"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Professions:»",
        options: ["Связанный термин", "Другой термин", "Вспомогательное понятие", "Professions:", "Дополнительный элемент"],
        correctAnswer: "Professions:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: Изучение названий профессий, описание обязанностей и требований.",
        options: ["Да, верно", "Только в некоторых случаях", "Зависит от контекста", "Нет, неверно", "Частично верно"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: Модальные глаголы для описания профессиональных требований.",
        options: ["Зависит от контекста", "Нет, неверно", "Да, верно", "Только в некоторых случаях", "Частично верно"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: ant (бухгалтер), software developer (разработчик ПО), journalist (журналист), architect (архитектор).",
        options: ["Частично верно", "Только в некоторых случаях", "Зависит от контекста", "Да, верно", "Нет, неверно"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Поиск работы",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Interview phrases:?",
        options: ["Специальный метод вычисления", "Вспомогательный термин", "Это понятие из другого раздела", "Понятие, обратное данному", "Tell me about yourself. (Расскажите о себе.)"],
        correctAnswer: "Tell me about yourself. (Расскажите о себе.)",
        hint: "Вспомни определение из урока про Interview phrases:"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Job search vocabulary:»",
        options: ["Вспомогательное понятие", "Связанный термин", "Дополнительный элемент", "Job search vocabulary:", "Другой термин"],
        correctAnswer: "Job search vocabulary:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Interview phrases:»",
        options: ["Вспомогательное понятие", "Другой термин", "Interview phrases:", "Связанный термин", "Дополнительный элемент"],
        correctAnswer: "Interview phrases:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: Написание резюме, сопроводительного письма, подготовка к собеседованию.",
        options: ["Частично верно", "Только в некоторых случаях", "Нет, неверно", "Да, верно", "Зависит от контекста"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: ew (собеседование), vacancy (вакансия), applicant (соискатель), salary (зарплата), benefits (льготы).",
        options: ["Да, верно", "Зависит от контекста", "Частично верно", "Только в некоторых случаях", "Нет, неверно"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Деловое общение",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Email phrases:?",
        options: ["I am writing to inquire about... (Я пишу, чтобы узнать о...)", "Вспомогательный термин", "Специальный метод вычисления", "Понятие, обратное данному", "Это понятие из другого раздела"],
        correctAnswer: "I am writing to inquire about... (Я пишу, чтобы узнать о...)",
        hint: "Вспомни определение из урока про Email phrases:"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Business vocabulary:»",
        options: ["Вспомогательное понятие", "Другой термин", "Дополнительный элемент", "Business vocabulary:", "Связанный термин"],
        correctAnswer: "Business vocabulary:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Email phrases:»",
        options: ["Другой термин", "Дополнительный элемент", "Вспомогательное понятие", "Email phrases:", "Связанный термин"],
        correctAnswer: "Email phrases:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: Деловая переписка, телефонные разговоры, презентации.",
        options: ["Да, верно", "Зависит от контекста", "Нет, неверно", "Частично верно", "Только в некоторых случаях"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: Профессиональный этикет.",
        options: ["Нет, неверно", "Только в некоторых случаях", "Частично верно", "Да, верно", "Зависит от контекста"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Экологические проблемы",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Causes and effects:?",
        options: ["Это понятие из другого раздела", "Специальный метод вычисления", "Понятие, обратное данному", "Pollution causes health problems. (Загрязнение вызывает проблемы со здоровьем.)", "Вспомогательный термин"],
        correctAnswer: "Pollution causes health problems. (Загрязнение вызывает проблемы со здоровьем.)",
        hint: "Вспомни определение из урока про Causes and effects:"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Environmental problems:»",
        options: ["Вспомогательное понятие", "Другой термин", "Связанный термин", "Environmental problems:", "Дополнительный элемент"],
        correctAnswer: "Environmental problems:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Causes and effects:»",
        options: ["Causes and effects:", "Дополнительный элемент", "Связанный термин", "Другой термин", "Вспомогательное понятие"],
        correctAnswer: "Causes and effects:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: Изучение лексики по теме экологии: загрязнение, изменение климата, исчезновение видов.",
        options: ["Да, верно", "Частично верно", "Нет, неверно", "Только в некоторых случаях", "Зависит от контекста"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: warming (глобальное потепление), deforestation (вырубка лесов), endangered species (исчезающие виды).",
        options: ["Частично верно", "Зависит от контекста", "Да, верно", "Нет, неверно", "Только в некоторых случаях"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Защита окружающей среды",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Actions:?",
        options: ["We should reduce, reuse, and recycle. (Мы должны сокращать, повторно использоват...", "Понятие, обратное данному", "Специальный метод вычисления", "Вспомогательный термин", "Это понятие из другого раздела"],
        correctAnswer: "We should reduce, reuse, and recycle. (Мы должны сокращать, повторно использоват...",
        hint: "Вспомни определение из урока про Actions:"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Environmental protection:»",
        options: ["Environmental protection:", "Связанный термин", "Вспомогательное понятие", "Другой термин", "Дополнительный элемент"],
        correctAnswer: "Environmental protection:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Actions:»",
        options: ["Другой термин", "Связанный термин", "Дополнительный элемент", "Actions:", "Вспомогательное понятие"],
        correctAnswer: "Actions:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: Способы защиты природы: переработка, энергосбережение, устойчивое развитие.",
        options: ["Только в некоторых случаях", "Зависит от контекста", "Частично верно", "Нет, неверно", "Да, верно"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: sustainable development (устойчивое развитие), conservation (сохранение), eco-friendly (экологичный).",
        options: ["Частично верно", "Зависит от контекста", "Только в некоторых случаях", "Да, верно", "Нет, неверно"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Типы СМИ",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Media types:»",
        options: ["Media types:", "Вспомогательное понятие", "Другой термин", "Связанный термин", "Дополнительный элемент"],
        correctAnswer: "Media types:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Media vocabulary:»",
        options: ["Media vocabulary:", "Вспомогательное понятие", "Связанный термин", "Дополнительный элемент", "Другой термин"],
        correctAnswer: "Media vocabulary:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: Изучение типов средств массовой информации: печать, радио, телевидение, интернет-медиа.",
        options: ["Да, верно", "Зависит от контекста", "Частично верно", "Только в некоторых случаях", "Нет, неверно"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: elevision (телевидение), radio (радио), online news (онлайн-новости), social media (социальные сети).",
        options: ["Нет, неверно", "Только в некоторых случаях", "Зависит от контекста", "Частично верно", "Да, верно"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: tor (редактор), headline (заголовок), article (статья), broadcast (трансляция), coverage (освещение).",
        options: ["Нет, неверно", "Да, верно", "Частично верно", "Только в некоторых случаях", "Зависит от контекста"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Социальные сети",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Social media vocabulary:»",
        options: ["Другой термин", "Вспомогательное понятие", "Social media vocabulary:", "Связанный термин", "Дополнительный элемент"],
        correctAnswer: "Social media vocabulary:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Advantages:»",
        options: ["Вспомогательное понятие", "Advantages:", "Дополнительный элемент", "Другой термин", "Связанный термин"],
        correctAnswer: "Advantages:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Disadvantages:»",
        options: ["Disadvantages:", "Связанный термин", "Дополнительный элемент", "Вспомогательное понятие", "Другой термин"],
        correctAnswer: "Disadvantages:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: Влияние социальных сетей на общество, преимущества и недостатки.",
        options: ["Да, верно", "Частично верно", "Нет, неверно", "Зависит от контекста", "Только в некоторых случаях"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: Безопасность в интернете.",
        options: ["Частично верно", "Да, верно", "Только в некоторых случаях", "Нет, неверно", "Зависит от контекста"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Технологии будущего",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Technology vocabulary:»",
        options: ["Дополнительный элемент", "Technology vocabulary:", "Другой термин", "Вспомогательное понятие", "Связанный термин"],
        correctAnswer: "Technology vocabulary:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Future technologies:»",
        options: ["Другой термин", "Связанный термин", "Future technologies:", "Дополнительный элемент", "Вспомогательное понятие"],
        correctAnswer: "Future technologies:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: Изучение лексики по теме технологий: искусственный интеллект, роботы, виртуальная реальность.",
        options: ["Частично верно", "Да, верно", "Нет, неверно", "Зависит от контекста", "Только в некоторых случаях"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: хника), virtual reality (виртуальная реальность), automation (автоматизация), innovation (инновация).",
        options: ["Да, верно", "Нет, неверно", "Частично верно", "Только в некоторых случаях", "Зависит от контекста"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: smart homes (умные дома), medical robots (медицинские роботы), space exploration (освоение космоса).",
        options: ["Зависит от контекста", "Только в некоторых случаях", "Частично верно", "Да, верно", "Нет, неверно"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Цифровая грамотность",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Online safety tips:?",
        options: ["Вспомогательный термин", "Понятие, обратное данному", "Специальный метод вычисления", "Это понятие из другого раздела", "Use strong passwords. (Используйте надёжные пароли.)"],
        correctAnswer: "Use strong passwords. (Используйте надёжные пароли.)",
        hint: "Вспомни определение из урока про Online safety tips:"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Digital literacy vocabulary:»",
        options: ["Вспомогательное понятие", "Связанный термин", "Digital literacy vocabulary:", "Дополнительный элемент", "Другой термин"],
        correctAnswer: "Digital literacy vocabulary:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Online safety tips:»",
        options: ["Связанный термин", "Дополнительный элемент", "Другой термин", "Online safety tips:", "Вспомогательное понятие"],
        correctAnswer: "Online safety tips:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: Безопасное использование технологий, защита личных данных, критическое мышление в цифровую эпоху.",
        options: ["Нет, неверно", "Зависит от контекста", "Частично верно", "Только в некоторых случаях", "Да, верно"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: оль), encryption (шифрование), phishing (фишинг), malware (вредоносное ПО), backup (резервная копия).",
        options: ["Да, верно", "Зависит от контекста", "Нет, неверно", "Только в некоторых случаях", "Частично верно"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  }
]
