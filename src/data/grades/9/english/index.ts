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
    icon: "Plane",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What is 'destination'?", options: ["Place to go", "Type of food", "Transport", "Currency"], correctAnswer: "Place to go", hint: "Where you're heading" },
      { type: 'fill', question: "I have ___ visited Paris. (никогда не)", correctAnswer: "never", hint: "Negative experience" },
      { type: 'quiz', question: "Present Perfect is used for:", options: ["Life experience", "Past actions", "Future plans", "Daily routine"], correctAnswer: "Life experience", hint: "At any time" },
      { type: 'fill', question: "Sightseeing means seeing ___. (достопримечательности)", correctAnswer: "sights", hint: "Tourist attractions" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь лексику путешествий!" }
  },
  {
    title: "В аэропорту",
    subject: "Иностранный язык",
    icon: "Plane",
    color: "text-pink-400",
    tasks: [
      { type: 'fill', question: "___ pass is your ticket to board. (посадочный)", correctAnswer: "Boarding", hint: "Required for flight" },
      { type: 'quiz', question: "Where do you pick up luggage?", options: ["Baggage claim", "Check-in", "Gate", "Customs"], correctAnswer: "Baggage claim", hint: "After arrival" },
      { type: 'fill', question: "My flight was ___ for two hours. (задержан)", correctAnswer: "delayed", hint: "Not on time" },
      { type: 'quiz', question: "'Gate' at airport means:", options: ["Exit to plane", "Entrance to building", "Parking area", "Ticket office"], correctAnswer: "Exit to plane", hint: "Boarding area" }
    ],
    reward: { stars: 3, message: "Ты готов к путешествию на самолёте!" }
  },
  {
    title: "В гостинице",
    subject: "Иностранный язык",
    icon: "Hotel",
    color: "text-pink-400",
    tasks: [
      { type: 'fill', question: "I'd like to ___ a room for two nights. (забронировать)", correctAnswer: "book", hint: "Make a reservation" },
      { type: 'quiz', question: "What does 'complimentary' mean?", options: ["Free", "Expensive", "Reserved", "Unavailable"], correctAnswer: "Free", hint: "Included at no cost" },
      { type: 'fill', question: "Is breakfast ___? (включено)", correctAnswer: "included", hint: "Part of the deal" },
      { type: 'quiz', question: "'Check-out' means:", options: ["Leaving the hotel", "Arriving at hotel", "Paying extra", "Ordering food"], correctAnswer: "Leaving the hotel", hint: "End of stay" }
    ],
    reward: { stars: 3, message: "Ты можешь заселиться в отеле!" }
  },
  {
    title: "Мир профессий",
    subject: "Иностранный язык",
    icon: "Briefcase",
    color: "text-pink-400",
    tasks: [
      { type: 'fill', question: "A ___ treats patients in a hospital. (врач)", correctAnswer: "doctor", hint: "Medical professional" },
      { type: 'quiz', question: "Who designs buildings?", options: ["Architect", "Doctor", "Teacher", "Driver"], correctAnswer: "Architect", hint: "Construction plans" },
      { type: 'fill', question: "I work as a software ___ at Google. (разработчик)", correctAnswer: "developer", hint: "Creates programs" },
      { type: 'quiz', question: "'Must' expresses:", options: ["Obligation", "Suggestion", "Permission", "Ability"], correctAnswer: "Obligation", hint: "Necessity" }
    ],
    reward: { stars: 3, message: "Ты хорошо знаешь названия профессий!" }
  },
  {
    title: "Поиск работы",
    subject: "Иностранный язык",
    icon: "FileText",
    color: "text-pink-400",
    tasks: [
      { type: 'fill', question: "A ___ is a document about your experience. (резюме)", correctAnswer: "CV", hint: "Or resume" },
      { type: 'quiz', question: "What is an 'interview'?", options: ["Job meeting", "Written test", "Email exchange", "Phone call only"], correctAnswer: "Job meeting", hint: "Face to face discussion" },
      { type: 'fill', question: "Please find my CV ___ to this email. (приложенным)", correctAnswer: "attached", hint: "Included in email" },
      { type: 'quiz', question: "'Strengths' means:", options: ["Strong points", "Weaknesses", "Hobbies", "Skills only"], correctAnswer: "Strong points", hint: "Positive qualities" }
    ],
    reward: { stars: 3, message: "Ты готов к поиску работы!" }
  },
  {
    title: "Деловое общение",
    subject: "Иностранный язык",
    icon: "Mail",
    color: "text-pink-400",
    tasks: [
      { type: 'fill', question: "A ___ is the final date for a task. (крайний срок)", correctAnswer: "deadline", hint: "Time limit" },
      { type: 'quiz', question: "How to start a business email?", options: ["I am writing to...", "Hey there!", "What's up?", "Hi buddy"], correctAnswer: "I am writing to...", hint: "Formal opening" },
      { type: 'fill', question: "I look forward to ___ from you. (получить ответ)", correctAnswer: "hearing", hint: "Waiting for reply" },
      { type: 'quiz', question: "'Negotiation' means:", options: ["Discussion for agreement", "Argument", "Contract signing", "Meeting only"], correctAnswer: "Discussion for agreement", hint: "Reaching a deal" }
    ],
    reward: { stars: 3, message: "Ты готов к деловому общению!" }
  },
  {
    title: "Экологические проблемы",
    subject: "Иностранный язык",
    icon: "Leaf",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What causes global warming?", options: ["Greenhouse gases", "Recycling", "Wind energy", "Solar panels"], correctAnswer: "Greenhouse gases", hint: "Carbon dioxide, methane" },
      { type: 'fill', question: "___ species are animals at risk of extinction. (исчезающие)", correctAnswer: "Endangered", hint: "In danger" },
      { type: 'quiz', question: "'Deforestation' means:", options: ["Cutting down forests", "Planting trees", "Forest protection", "Forest fire"], correctAnswer: "Cutting down forests", hint: "Removing trees" },
      { type: 'fill', question: "Pollution causes health ___. (проблемы)", correctAnswer: "problems", hint: "Negative effects" }
    ],
    reward: { stars: 3, message: "Ты понимаешь экологические проблемы!" }
  },
  {
    title: "Защита окружающей среды",
    subject: "Иностранный язык",
    icon: "Recycle",
    color: "text-pink-400",
    tasks: [
      { type: 'fill', question: "We need to ___ plastic waste. (перерабатывать)", correctAnswer: "recycle", hint: "Process for reuse" },
      { type: 'quiz', question: "What are the 3 R's?", options: ["Reduce, Reuse, Recycle", "Read, Write, Learn", "Run, Walk, Jump", "Red, Green, Blue"], correctAnswer: "Reduce, Reuse, Recycle", hint: "Environmental principles" },
      { type: 'fill', question: "___ energy comes from sun and wind. (возобновляемая)", correctAnswer: "Renewable", hint: "Can be replenished" },
      { type: 'quiz', question: "'Eco-friendly' means:", options: ["Good for environment", "Expensive", "New product", "Popular"], correctAnswer: "Good for environment", hint: "Environmentally safe" }
    ],
    reward: { stars: 3, message: "Ты знаешь, как защитить природу!" }
  },
  {
    title: "Типы СМИ",
    subject: "Иностранный язык",
    icon: "Newspaper",
    color: "text-pink-400",
    tasks: [
      { type: 'fill', question: "A ___ is a daily or weekly publication. (газета)", correctAnswer: "newspaper", hint: "Print media" },
      { type: 'quiz', question: "What is a 'headline'?", options: ["Article title", "First paragraph", "Last paragraph", "Picture"], correctAnswer: "Article title", hint: "Main title" },
      { type: 'fill', question: "A ___ writes articles for media. (журналист)", correctAnswer: "journalist", hint: "Media professional" },
      { type: 'quiz', question: "'Broadcast' means:", options: ["Transmit on TV/radio", "Print", "Write", "Read"], correctAnswer: "Transmit on TV/radio", hint: "Air transmission" }
    ],
    reward: { stars: 3, message: "Ты разбираешься в типах СМИ!" }
  },
  {
    title: "Социальные сети",
    subject: "Иностранный язык",
    icon: "Share2",
    color: "text-pink-400",
    tasks: [
      { type: 'fill', question: "Viral content spreads ___ online. (быстро)", correctAnswer: "quickly", hint: "Becomes popular" },
      { type: 'quiz', question: "What is 'cyberbullying'?", options: ["Online harassment", "Computer virus", "Video game", "Social platform"], correctAnswer: "Online harassment", hint: "Digital bullying" },
      { type: 'fill', question: "Don't share personal ___ online. (информация)", correctAnswer: "information", hint: "Private data" },
      { type: 'quiz', question: "A 'follower' is:", options: ["Someone who subscribes", "A friend", "Family member", "Coworker"], correctAnswer: "Someone who subscribes", hint: "Social media connection" }
    ],
    reward: { stars: 3, message: "Ты безопасно используешь соцсети!" }
  },
  {
    title: "Технологии будущего",
    subject: "Иностранный язык",
    icon: "Cpu",
    color: "text-pink-400",
    tasks: [
      { type: 'fill', question: "AI stands for Artificial ___ . (интеллект)", correctAnswer: "Intelligence", hint: "Smart machines" },
      { type: 'quiz', question: "What is 'virtual reality'?", options: ["Computer-generated environment", "Real world", "Dream", "Movie"], correctAnswer: "Computer-generated environment", hint: "VR technology" },
      { type: 'fill', question: "___ cars drive without a driver. (автопилотируемые)", correctAnswer: "Self-driving", hint: "Or autonomous" },
      { type: 'quiz', question: "'Automation' means:", options: ["Machines doing work", "Manual labor", "Working slowly", "No work"], correctAnswer: "Machines doing work", hint: "Automatic processes" }
    ],
    reward: { stars: 3, message: "Ты понимаешь технологии будущего!" }
  },
  {
    title: "Цифровая грамотность",
    subject: "Иностранный язык",
    icon: "Shield",
    color: "text-pink-400",
    tasks: [
      { type: 'fill', question: "Use strong ___ to protect accounts. (пароли)", correctAnswer: "passwords", hint: "Security codes" },
      { type: 'quiz', question: "What is 'phishing'?", options: ["Fake emails to steal data", "Fishing hobby", "Computer game", "Website design"], correctAnswer: "Fake emails to steal data", hint: "Online scam" },
      { type: 'fill', question: "Create a ___ of important files. (резервную копию)", correctAnswer: "backup", hint: "Extra copy" },
      { type: 'quiz', question: "'Encryption' means:", options: ["Coding data for security", "Deleting files", "Opening files", "Sharing files"], correctAnswer: "Coding data for security", hint: "Data protection" }
    ],
    reward: { stars: 3, message: "Ты цифровой грамотный пользователь!" }
  }
]
