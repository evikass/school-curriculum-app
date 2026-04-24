import { SubjectData, GameLesson } from '@/data/types'

export const lessons: SubjectData = {
  title: "Иностранный язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: ["Daily Life", "Travel and Tourism", "Environment", "Technology"],
  detailedTopics: [
    {
      topic: "Daily Life",
      lessons: [
        {
          title: "Daily Routines and Habits",
          image: "/school-curriculum-app/images/lessons/grade7/english/lesson1.svg",
          description: `**Daily Routines** — повседневные дела и привычки.

**Present Simple for Routines:**
- I usually wake up at 7 o'clock.
- She always has breakfast at 8 am.
- We often go to school by bus.

**Frequency Adverbs:**
- Always — всегда (100%)
- Usually — обычно (80%)
- Often — часто (60%)
- Sometimes — иногда (40%)
- Rarely — редко (20%)
- Never — никогда (0%)

**Position in sentence:**
- Before the main verb: I always eat breakfast.
- After 'to be': She is never late.

**Daily Activities:**
- Wake up — просыпаться
- Get up — вставать
- Have breakfast — завтракать
- Go to school — идти в школу
- Have lunch — обедать
- Do homework — делать домашнюю работу
- Have dinner — ужинать
- Go to bed — ложиться спать

**Time Expressions:**
- In the morning — утром
- In the afternoon — днём
- In the evening — вечером
- At night — ночью
- At noon — в полдень`,
          tasks: [
            "Translate: Я обычно просыпаюсь в 7 часов",
            "Put the adverb: She (often) is late for school",
            "Make a sentence: always / I / breakfast / have",
            "Write 5 daily activities"
          ],
          examples: [
            "Present Simple: I usually wake up at 7 o'clock 🕐",
            "Наречия частотности: always (100%) → usually → often → sometimes → rarely → never (0%)"
          ],
          keyPoints: [
            "Present Simple for routines: I wake up at 7 AM every day",
            "Present Continuous for actions happening now: I am reading now",
            "Adverbs of frequency: always, usually, often, sometimes, never"
          ]
        },
        {
          title: "Household Chores",
          image: "/school-curriculum-app/images/lessons/grade7/english/lesson2.svg",
          description: `**Household Chores** — домашние обязанности.

**Common Chores:**
- Do the washing-up — мыть посуду
- Do the laundry — стирать бельё
- Do the ironing — гладить
- Do the cleaning — убираться
- Make the bed — заправлять постель
- Take out the rubbish — выносить мусор
- Vacuum the carpet — пылесосить ковёр
- Water the plants — поливать растения
- Walk the dog — гулять с собакой

**Modal Verbs for Obligation:**

**Have to / Has to:**
- I have to clean my room.
- She has to wash the dishes.
- Do you have to cook dinner?

**Must:**
- You must help your parents.
- I must do my homework.

**Should:**
- You should help your mother.
- Children should make their beds.

**Questions:**
- What chores do you do?
- Who has to do the washing-up?
- How often do you clean your room?

**Making Requests:**
- Can you help me, please?
- Could you take out the rubbish?
- Would you mind doing the dishes?`,
          tasks: [
            "Translate: Мне нужно помыть посуду",
            "Make a question: you / have to / do / chores / what?",
            "Write 5 household chores",
            "Use 'should': help / parents / you / your"
          ],
          examples: [
            "I have to do the washing-up — мне нужно помыть посуду 🧽",
            "Should: You should help your parents — тебе следует помочь родителям"
          ],
          keyPoints: [
            "Household chores vocabulary: do the dishes, vacuum the floor, do the laundry",
            "Make vs do: make breakfast (создать), do homework (выполнить)",
            "Have to / must for obligations: I have to clean my room"
          ]
        }
      ]
    },
    {
      topic: "Travel and Tourism",
      lessons: [
        {
          title: "Planning a Trip",
          image: "/school-curriculum-app/images/lessons/grade7/english/lesson3.svg",
          description: `**Travel Vocabulary:**
- Journey — путешествие
- Trip — поездка
- Tour — тур, экскурсия
- Voyage — морское путешествие
- Excursion — экскурсия

**Transport:**
- By plane — самолётом
- By train — поездом
- By bus — автобусом
- By car — на машине
- By ship — кораблём
- On foot — пешком

**At the Airport:**
- Check-in — регистрация
- Boarding pass — посадочный талон
- Gate — выход на посадку
- Departure — отправление
- Arrival — прибытие
- Luggage / baggage — багаж
- Delay — задержка

**Booking a Hotel:**
- Book a room — забронировать номер
- Single room — одноместный номер
- Double room — двухместный номер
- Check in — заселиться
- Check out — выселиться

**Future Tenses for Plans:**

**Going to:**
- I'm going to visit Paris.
- We're going to stay at a hotel.

**Present Continuous:**
- I'm flying to London tomorrow.
- She's leaving next week.`,
          tasks: [
            "Translate: Я собираюсь посетить Лондон",
            "Write 5 types of transport",
            "Make a sentence: going to / I / visit / Paris",
            "What's the difference: journey / trip / voyage?"
          ],
          examples: [
            "I'm going to visit London next summer — планирую посетить Лондон ✈️",
            "by plane — самолётом, by train — поездом, on foot — пешком"
          ],
          keyPoints: [
            "Travel vocabulary: book a hotel, pack luggage, check in, boarding pass",
            "Future with going to: I'm going to visit Paris next summer",
            "Conditional: If I have time, I will go to the museum"
          ]
        },
        {
          title: "Sightseeing and Activities",
          image: "/school-curriculum-app/images/lessons/grade7/english/lesson4.svg",
          description: `**Places to Visit:**
- Museum — музей
- Gallery — галерея
- Cathedral — собор
- Castle — замок
- Palace — дворец
- Monument — памятник
- Fountain — фонтан
- Square — площадь
- Bridge — мост

**Useful Phrases:**
- What's there to see?
- How do I get to...?
- Is it far from here?
- Can you show me on the map?
- How much is the entrance fee?
- What time does it open/close?

**Describing Places:**
- Beautiful — красивый
- Magnificent — величественный
- Ancient — древний
- Modern — современный
- Crowded — переполненный
- Peaceful — спокойный
- Touristy — туристический

**Past Simple for Travel Stories:**
- I visited the Louvre last year.
- We saw many interesting places.
- Did you go to the Eiffel Tower?
- We didn't have enough time.

**Writing a Postcard:**
Dear [Name],
I'm writing from [city].
Yesterday I visited [place].
It was [adjective].
Tomorrow I'm going to [plan].
See you soon!
Love,
[Your name]`,
          tasks: [
            "Translate: Как добраться до музея?",
            "Write 5 adjectives to describe places",
            "Tell about your last trip (5 sentences)",
            "Write a postcard from London"
          ],
          examples: [
            "Past Simple: I visited the Louvre last year — прошлым летом я посетил Лувр 🏛️",
            "How do I get to the museum? — как добраться до музея?"
          ],
          keyPoints: [
            "Sightseeing vocabulary: monument, museum, gallery, cathedral, square",
            "Would like to for polite requests and offers: I'd like to see the Eiffel Tower",
            "Directions: turn left/right, go straight, opposite, next to"
          ]
        }
      ]
    },
    {
      topic: "Environment",
      lessons: [
        {
          title: "Environmental Problems",
          image: "/school-curriculum-app/images/lessons/grade7/english/lesson5.svg",
          description: `**Environmental Issues:**
- Pollution — загрязнение
- Air pollution — загрязнение воздуха
- Water pollution — загрязнение воды
- Global warming — глобальное потепление
- Climate change — изменение климата
- Deforestation — вырубка лесов
- Endangered species — исчезающие виды
- Waste — отходы
- Plastic — пластик

**Causes:**
- Cars produce exhaust fumes.
- Factories pollute the air.
- People cut down forests.
- We use too much plastic.

**Consequences:**
- Animals lose their habitats.
- The ice caps are melting.
- Sea levels are rising.
- Weather is becoming extreme.

**Modal Verbs for Environment:**

**Should:**
- We should recycle more.
- People should use public transport.

**Must:**
- We must protect nature.
- Governments must take action.

**First Conditional:**
- If we don't act, the climate will change.
- If people recycle, there will be less waste.

**Vocabulary for Solutions:**
- Recycle — перерабатывать
- Reuse — использовать повторно
- Reduce — уменьшать
- Save energy — экономить энергию
- Use public transport — пользоваться общественным транспортом
- Plant trees — сажать деревья`,
          tasks: [
            "Translate: Мы должны защищать природу",
            "Write 5 environmental problems",
            "Make a sentence with First Conditional",
            "What should people do to help?"
          ],
          examples: [
            "We must protect nature — мы должны защищать природу 🌍",
            "First Conditional: If we recycle, there will be less waste"
          ],
          keyPoints: [
            "Environmental vocabulary: pollution, recycling, global warming, endangered species",
            "Should / shouldn't for advice: We should recycle paper and plastic",
            "Passive voice: The air is polluted by factories"
          ]
        }
      ]
    },
    {
      topic: "Technology",
      lessons: [
        {
          title: "Digital World",
          image: "/school-curriculum-app/images/lessons/grade7/english/lesson6.svg",
          description: `**Technology Vocabulary:**
- Computer — компьютер
- Laptop — ноутбук
- Smartphone — смартфон
- Tablet — планшет
- Internet — интернет
- Website — веб-сайт
- App — приложение
- Social media — социальные сети
- Email — электронная почта

**Digital Activities:**
- Go online — выходить в интернет
- Browse the web — просматривать веб-страницы
- Download files — скачивать файлы
- Upload photos — загружать фото
- Send messages — отправлять сообщения
- Make video calls — делать видеозвонки
- Play online games — играть в онлайн-игры

**Present Perfect for Experience:**
- I have bought a new smartphone.
- Have you ever used this app?
- She has never played this game.
- We have downloaded many songs.

**Internet Safety:**
- Keep your password safe.
- Don't share personal information.
- Be careful with strangers online.
- Ask parents for help.

**Advantages and Disadvantages:**

**Pros:**
- Easy communication
- Access to information
- Entertainment
- Online shopping

**Cons:**
- Addiction to gadgets
- Less physical activity
- Cyberbullying
- Fake information`,
          tasks: [
            "Translate: Я никогда не играл в эту игру",
            "Write 5 digital devices",
            "Present Perfect: you / ever / use / this app?",
            "Write about pros and cons of the Internet"
          ],
          examples: [
            "Present Perfect: I have bought a new smartphone — я купил новый телефон 📱",
            "Internet safety: don't share personal information online"
          ],
          keyPoints: [
            "Digital vocabulary: social media, download, upload, password, account",
            "Present Perfect for experiences: I have already sent the email",
            "Online safety: never share your password with strangers"
          ]
        }
      ]
    }
  ]
}

export const games = [
  {
    title: "Daily Life",
    image: "/school-curriculum-app/images/lessons/grade7/english/lesson19.svg",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What time do you ___ get up?", options: ["usually", "ever", "never", "always", "Другой ответ"], correctAnswer: "usually", hint: "Frequency adverb" },
      { type: 'quiz', question: "She ___ has breakfast at 8 am.", options: ["have to", "has to", "must to", "should to", "Другой ответ"], correctAnswer: "has to", hint: "Obligation for he/she/it" },
      { type: 'find', question: "Select household chores:", options: ["Do homework", "Do the washing-up", "Watch TV", "Make the bed", "Play games"], correctAnswer: ["Do the washing-up", "Make the bed"], hint: "Work around the house" },
      { type: 'quiz', question: "I'm ___ visit Paris next summer.", options: ["will", "going to", "will be", "would", "Другой ответ"], correctAnswer: "going to", hint: "Plans for future" },
      { type: 'quiz', question: "What's the Russian for 'frequency adverb'?", options: ["Глагол", "Наречие частотности", "Прилагательное", "Существительное", "Другой ответ"], correctAnswer: "Наречие частотности", hint: "Always, often, never" }
    ],
    reward: { stars: 3, message: "Excellent! You know daily routines! 🌟" }
  },
  {
    title: "Travel and Environment",
    image: "/school-curriculum-app/images/lessons/grade7/english/lesson20.svg",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What's the Russian for 'boarding pass'?", options: ["Билет", "Посадочный талон", "Багаж", "Регистрация", "Другой ответ"], correctAnswer: "Посадочный талон", hint: "At the airport" },
      { type: 'quiz', question: "We ___ protect nature.", options: ["should", "must", "have", "need", "Другой ответ"], correctAnswer: "must", hint: "Strong obligation" },
      { type: 'find', question: "Select environmental problems:", options: ["Pollution", "Journey", "Global warming", "Deforestation", "Hotel"], correctAnswer: ["Pollution", "Global warming", "Deforestation"], hint: "Issues with nature" },
      { type: 'quiz', question: "Have you ever ___ this app?", options: ["use", "used", "using", "uses", "Другой ответ"], correctAnswer: "used", hint: "Present Perfect" },
      { type: 'quiz', question: "What's the Past Simple of 'go'?", options: ["goed", "went", "gone", "going", "Другой ответ"], correctAnswer: "went", hint: "Irregular verb" }
    ],
    reward: { stars: 3, message: "Great job! You're an English pro! 🎉" }
  },
  {
    title: "Travel and Tourism",
    image: "/school-curriculum-app/images/lessons/grade7/english/lesson21.svg",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What's the Russian for 'boarding pass'?", options: ["Билет", "Посадочный талон", "Загранпаспорт", "Регистрация", "Другой ответ"], correctAnswer: "Посадочный талон", hint: "You need it to board the plane" },
      { type: 'quiz', question: "I'm going ___ visit London next summer.", options: ["for", "to", "at", "on", "Другой ответ"], correctAnswer: "to", hint: "Going to + infinitive" },
      { type: 'quiz', question: "Which word means 'самолётом'?", options: ["By train", "By plane", "By bus", "On foot", "Другой ответ"], correctAnswer: "By plane", hint: "A type of air transport" },
      { type: 'find', question: "Select places to visit:", options: ["Museum", "Cathedral", "Homework", "Palace", "Monument"], correctAnswer: ["Museum", "Cathedral", "Palace", "Monument"], hint: "Tourist attractions and landmarks" },
      { type: 'quiz', question: "How do you ask for directions to a museum?", options: ["What is a museum?", "How do I get to the museum?", "Where is the museum from?", "Do you like museums?", "Другой ответ"], correctAnswer: "How do I get to the museum?", hint: "Useful phrase for tourists" }
    ],
    reward: { stars: 3, message: "Amazing! You're ready to travel! ✈️" }
  },
  {
    title: "Technology",
    image: "/school-curriculum-app/images/lessons/grade7/english/lesson22.svg",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What's the Russian for 'social media'?", options: ["Электронная почта", "Социальные сети", "Веб-сайт", "Блог", "Другой ответ"], correctAnswer: "Социальные сети", hint: "VK, Instagram, TikTok..." },
      { type: 'quiz', question: "I have ___ bought a new smartphone.", options: ["yet", "just", "ever", "never", "Другой ответ"], correctAnswer: "just", hint: "Present Perfect with 'already/just'" },
      { type: 'quiz', question: "What does 'download' mean in Russian?", options: ["Загружать онлайн", "Скачивать файлы", "Удалять данные", "Отправлять письмо", "Другой ответ"], correctAnswer: "Скачивать файлы", hint: "Getting files from the internet" },
      { type: 'quiz', question: "Which is an important internet safety rule?", options: ["Share your password with friends", "Post personal information publicly", "Don't share personal information", "Accept all friend requests", "Другой ответ"], correctAnswer: "Don't share personal information", hint: "Stay safe online" },
      { type: 'quiz', question: "Have you ever ___ this app?", options: ["use", "uses", "using", "used", "Другой ответ"], correctAnswer: "used", hint: "Present Perfect: have/has + Past Participle" }
    ],
    reward: { stars: 3, message: "Great! You're a digital native! 💻" }
  },
  {
    title: "Daily Routines and Habits",
    image: "/school-curriculum-app/images/lessons/grade7/english/lesson23.svg",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Which tense do we use for daily routines?", options: ["Present Continuous", "Present Simple", "Past Simple", "Future Simple", "Другой ответ"],
      keyPoints: [
        "Present Simple for routines: I wake up at 7 AM every day",
        "Present Continuous for actions happening now: I am reading now",
        "Adverbs of frequency: always, usually, often, sometimes, never",
      ],
      examples: [
        "I have to do the washing-up — мне нужно помыть посуду 🧽",
        "Should: You should help your parents — тебе следует помочь родителям",
      ], correctAnswer: "Present Simple", hint: "I wake up at 7 AM every day" },
      { type: 'quiz', question: "What does 'usually' mean in Russian?", options: ["Никогда", "Обычно", "Иногда", "Всегда", "Другой ответ"], correctAnswer: "Обычно", hint: "Frequency adverb — 80%" },
      { type: 'quiz', question: "Where do you place frequency adverbs with 'to be'?", options: ["After 'to be'", "Before 'to be'", "At the beginning", "At the end", "Before the subject"], correctAnswer: "After 'to be'", hint: "She is never late" },
      { type: 'quiz', question: "What does 'go to bed' mean?", options: ["Идти в школу", "Ложиться спать", "Делать уборку", "Идти гулять", "Другой ответ"], correctAnswer: "Ложиться спать", hint: "Daily activity before sleeping" },
      { type: 'quiz', question: "Which phrase means 'вечером'?", options: ["In the morning", "In the afternoon", "In the evening", "At night", "Другой ответ"], correctAnswer: "In the evening", hint: "Time of day" }
    ],
    reward: { stars: 3, message: "Great! You know daily routines! 🕐" }
  },
  {
    title: "Household Chores",
    image: "/school-curriculum-app/images/lessons/grade7/english/lesson24.svg",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What does 'do the washing-up' mean?", options: ["Стирать бельё", "Мыть посуду", "Убираться", "Гладить", "Другой ответ"],
      keyPoints: [
        "Household chores vocabulary: do the dishes, vacuum the floor, do the laundry",
        "Make vs do: make breakfast (создать), do homework (выполнить)",
        "Have to / must for obligations: I have to clean my room",
      ],
      examples: [
        "I'm going to visit London next summer — планирую посетить Лондон ✈️",
        "by plane — самолётом, by train — поездом, on foot — пешком",
      ], correctAnswer: "Мыть посуду", hint: "Work with dishes" },
      { type: 'quiz', question: "Which modal verb expresses strong obligation?", options: ["Should", "Must", "Can", "May", "Другой ответ"], correctAnswer: "Must", hint: "You must help your parents" },
      { type: 'quiz', question: "What does 'make the bed' mean?", options: ["Построить кровать", "Заправлять постель", "Купить кровать", "Убрать комнату", "Другой ответ"], correctAnswer: "Заправлять постель", hint: "Morning household task" },
      { type: 'quiz', question: "What's the difference between 'make' and 'do'?", options: ["They are the same", "Make = create, Do = perform/complete", "Make = clean, Do = build", "Make = destroy, Do = fix", "Другой ответ"], correctAnswer: "Make = create, Do = perform/complete", hint: "Make breakfast vs do homework" },
      { type: 'quiz', question: "How do you ask: «Какие домашние дела ты делаешь?»", options: ["What chores do you do?", "When do you clean?", "Where is your room?", "Why do you work?", "Другой ответ"], correctAnswer: "What chores do you do?", hint: "Question about household tasks" }
    ],
    reward: { stars: 3, message: "Great! You know household chores! 🧹" }
  },
  {
    title: "Planning a Trip",
    image: "/school-curriculum-app/images/lessons/grade7/english/lesson25.svg",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What does 'boarding pass' mean in Russian?", options: ["Билет", "Посадочный талон", "Загранпаспорт", "Регистрация", "Другой ответ"],
      keyPoints: [
        "Travel vocabulary: book a hotel, pack luggage, check in, boarding pass",
        "Future with going to: I'm going to visit Paris next summer",
        "Conditional: If I have time, I will go to the museum",
      ],
      examples: [
        "Past Simple: I visited the Louvre last year — прошлым летом я посетил Лувр 🏛️",
        "How do I get to the museum? — как добраться до музея?",
      ], correctAnswer: "Посадочный талон", hint: "Document needed to board a plane" },
      { type: 'quiz', question: "Which phrase means 'I'm going to visit London'?", options: ["I will visit London", "I'm going to visit London", "I visit London", "I visited London", "Другой ответ"], correctAnswer: "I'm going to visit London", hint: "Going to + infinitive for plans" },
      { type: 'quiz', question: "What does 'by plane' mean?", options: ["На поезде", "Самолётом", "На машине", "Пешком", "Другой ответ"], correctAnswer: "Самолётом", hint: "Type of air transport" },
      { type: 'quiz', question: "What does 'check in' mean at a hotel?", options: ["Выселиться", "Заселиться", "Забронировать", "Оплатить", "Другой ответ"], correctAnswer: "Заселиться", hint: "Arrival procedure" },
      { type: 'quiz', question: "What's the difference between 'journey' and 'voyage'?", options: ["They are the same", "Journey = general trip, Voyage = sea journey", "Journey = sea, Voyage = land", "Journey = short, Voyage = long walk", "Другой ответ"], correctAnswer: "Journey = general trip, Voyage = sea journey", hint: "Voyage is specifically by ship" }
    ],
    reward: { stars: 3, message: "Great! You can plan a trip! ✈️" }
  },
  {
    title: "Sightseeing and Activities",
    image: "/school-curriculum-app/images/lessons/grade7/english/lesson26.svg",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What does 'monument' mean in Russian?", options: ["Музей", "Памятник", "Площадь", "Фонтан", "Другой ответ"],
      keyPoints: [
        "Sightseeing vocabulary: monument, museum, gallery, cathedral, square",
        "Would like to for polite requests and offers: I'd like to see the Eiffel Tower",
        "Directions: turn left/right, go straight, opposite, next to",
      ],
      examples: [
        "We must protect nature — мы должны защищать природу 🌍",
        "First Conditional: If we recycle, there will be less waste",
      ], correctAnswer: "Памятник", hint: "A structure commemorating a person or event" },
      { type: 'quiz', question: "Which tense is used for travel stories?", options: ["Present Simple", "Present Continuous", "Past Simple", "Future Simple", "Другой ответ"], correctAnswer: "Past Simple", hint: "I visited the Louvre last year" },
      { type: 'quiz', question: "How do you ask for directions to a museum?", options: ["What is a museum?", "How do I get to the museum?", "Where is the museum from?", "Do you like museums?", "Другой ответ"], correctAnswer: "How do I get to the museum?", hint: "Useful phrase for tourists" },
      { type: 'quiz', question: "What does 'ancient' mean?", options: ["Современный", "Древний", "Красивый", "Переполненный", "Другой ответ"], correctAnswer: "Древний", hint: "Adjective describing old places" },
      { type: 'quiz', question: "What is the Past Simple of 'see'?", options: ["Seed", "Saw", "Seen", "Seeing", "Другой ответ"], correctAnswer: "Saw", hint: "Irregular verb" }
    ],
    reward: { stars: 3, message: "Great! You're a sightseeing expert! 🏛️" }
  },
  {
    title: "Environmental Problems",
    image: "/school-curriculum-app/images/lessons/grade7/english/lesson27.svg",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What does 'global warming' mean in Russian?", options: ["Глобальное потепление", "Глобальное заморозка", "Загрязнение воды", "Вырубка лесов", "Другой ответ"],
      keyPoints: [
        "Environmental vocabulary: pollution, recycling, global warming, endangered species",
        "Should / shouldn't for advice: We should recycle paper and plastic",
        "Passive voice: The air is polluted by factories",
      ],
      examples: [
        "Present Perfect: I have bought a new smartphone — я купил новый телефон 📱",
        "Internet safety: don't share personal information online",
      ], correctAnswer: "Глобальное потепление", hint: "Rising temperatures on Earth" },
      { type: 'quiz', question: "Which modal verb gives advice?", options: ["Must", "Should", "Can", "Will", "Другой ответ"], correctAnswer: "Should", hint: "We should recycle more" },
      { type: 'quiz', question: "What does 'deforestation' mean?", options: ["Посадка деревьев", "Вырубка лесов", "Загрязнение воздуха", "Рекультивация", "Другой ответ"], correctAnswer: "Вырубка лесов", hint: "Cutting down forests" },
      { type: 'quiz', question: "Complete: If people recycle, there ___ less waste.", options: ["is", "will be", "was", "are", "Другой ответ"], correctAnswer: "will be", hint: "First Conditional: If + present, will + infinitive" },
      { type: 'quiz', question: "What does 'endangered species' mean?", options: ["Опасные животные", "Исчезающие виды", "Домашние питомцы", "Водные организмы", "Другой ответ"], correctAnswer: "Исчезающие виды", hint: "Animals at risk of extinction" }
    ],
    reward: { stars: 3, message: "Great! You care about the environment! 🌍" }
  },
  {
    title: "Digital World",
    image: "/school-curriculum-app/images/lessons/grade7/english/lesson28.svg",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What does 'social media' mean in Russian?", options: ["Электронная почта", "Социальные сети", "Веб-сайт", "Блог", "Другой ответ"],
      keyPoints: [
        "Digital vocabulary: social media, download, upload, password, account",
        "Present Perfect for experiences: I have already sent the email",
        "Online safety: never share your password with strangers",
      ],
      examples: [
        "Сосна — хвойная мягкая порода, дуб — лиственная твёрдая 🪵",
        "Пороки древесины: сучки, трещины, гниль, завиток, смоляной кармашек",
        "Текстура — уникальный рисунок на срезе древесины",
      ], correctAnswer: "Социальные сети", hint: "VK, Instagram, TikTok..." },
      { type: 'quiz', question: "Which tense is used for experiences?", options: ["Past Simple", "Present Simple", "Present Perfect", "Future Simple", "Другой ответ"], correctAnswer: "Present Perfect", hint: "I have already bought a new smartphone" },
      { type: 'quiz', question: "What does 'download' mean?", options: ["Загружать онлайн", "Скачивать файлы", "Удалять данные", "Отправлять письмо", "Другой ответ"], correctAnswer: "Скачивать файлы", hint: "Getting files from the internet" },
      { type: 'quiz', question: "Which is an important internet safety rule?", options: ["Share your password with friends", "Post personal information publicly", "Don't share personal information", "Accept all friend requests", "Другой ответ"], correctAnswer: "Don't share personal information", hint: "Stay safe online" },
      { type: 'quiz', question: "What does 'cyberbullying' mean?", options: ["Онлайн-игры", "Кибербуллинг — травля в интернете", "Компьютерные вирусы", "Социальные сети", "Другой ответ"], correctAnswer: "Кибербуллинг — травля в интернете", hint: "Disadvantage of technology" }
    ],
    reward: { stars: 3, message: "Great! You're a digital citizen! 📱" }
  }
]

