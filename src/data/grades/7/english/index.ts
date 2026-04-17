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

export const games: GameLesson[] = [
  {
    title: "Daily Routines and Habits 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Вопрос 1 по теме \"Daily Routines and Habits\"", options: ["Present Perfect for Experience:","Daily Routines and Habits","Past Simple for Travel Stories:","Causes:","Time Expressions:"], correctAnswer: "Daily Routines and Habits", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 2 по теме \"Daily Routines and Habits\"", options: ["Present Perfect for Experience:","Questions:","Technology Vocabulary:","Daily Routines and Habits","Household Chores"], correctAnswer: "Daily Routines and Habits", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 3 по теме \"Daily Routines and Habits\"", options: ["Questions:","Travel Vocabulary:","Past Simple for Travel Stories:","Daily Routines and Habits","Technology Vocabulary:"], correctAnswer: "Daily Routines and Habits", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 4 по теме \"Daily Routines and Habits\"", options: ["Future Tenses for Plans:","Should:","Must:","Daily Routines and Habits","Writing a Postcard:"], correctAnswer: "Daily Routines and Habits", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 5 по теме \"Daily Routines and Habits\"", options: ["Daily Activities:","Consequences:","Daily Routines and Habits","Future Tenses for Plans:","Present Simple for Routines:"], correctAnswer: "Daily Routines and Habits", hint: "Ответ связан с материалом урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Household Chores 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Modal Verbs for Obligation:","Common Chores:","Making Requests:","Can you help me, please?","Position in sentence:"], correctAnswer: "Can you help me, please?", hint: "Этот термин связан с темой: Household Chores" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Household Chores\"?", options: ["You should help your mother.","Common Chores:","Present Continuous:","Must:","Daily Activities:"], correctAnswer: "Must:", hint: "Ответ связан с уроком: Household Chores" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Household Chores\"?", options: ["At the Airport:","Past Simple for Travel Stories:","Internet Safety:","parents","Must:"], correctAnswer: "parents", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Household Chores\":", options: ["Modal Verbs for Obligation:","Making Requests:","Household Chores","Must:","Should:","Common Chores:"], correctAnswer: ["Making Requests:","Should:","Must:"], hint: "Ищите термины, которые встречаются в уроке Household Chores" },
      { type: 'quiz', question: "Что является основным понятием урока \"Household Chores\"?", options: ["What chores do you do?","Walk the dog","- She has to wash the dishes","I have to clean my room.","Do the laundry"], correctAnswer: "- She has to wash the dishes", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Planning a Trip 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"By plane — самолётом...\"?", options: ["Internet Safety:","Check out","Present Perfect for Experience:","By plane","Position in sentence:"], correctAnswer: "By plane", hint: "Этот термин связан с темой: Planning a Trip" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Planning a Trip\"?", options: ["Modal Verbs for Environment:","Booking a Hotel:","Check out","Departure","I'm flying to London tomorrow."], correctAnswer: "Booking a Hotel:", hint: "Ответ связан с уроком: Planning a Trip" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Planning a Trip\"?", options: ["Must:","Book a room","Daily Activities:","By plane","hotel"], correctAnswer: "hotel", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Planning a Trip\":", options: ["At the Airport:","Travel Vocabulary:","Future Tenses for Plans:","Going to:","Present Continuous:","Transport:"], correctAnswer: ["Future Tenses for Plans:","At the Airport:","Travel Vocabulary:"], hint: "Ищите термины, которые встречаются в уроке Planning a Trip" },
      { type: 'quiz', question: "Что является основным понятием урока \"Planning a Trip\"?", options: ["I'm going to visit Paris.","**Present Continuous:** - I'm flying to London tomorrow","By train","Single room","Delay"], correctAnswer: "**Present Continuous:** - I'm flying to London tomorrow", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Sightseeing and Activities 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"Palace — дворец...\"?", options: ["Questions:","How much is the entrance fee?","Must:","Palace","Should:"], correctAnswer: "Palace", hint: "Этот термин связан с темой: Sightseeing and Activities" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Sightseeing and Activities\"?", options: ["Pros:","Useful Phrases:","Palace","Going to:","Museum"], correctAnswer: "Useful Phrases:", hint: "Ответ связан с уроком: Sightseeing and Activities" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Sightseeing and Activities\"?", options: ["places","Have to / Has to:","Should:","First Conditional:","Time Expressions:"], correctAnswer: "places", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Sightseeing and Activities\":", options: ["Writing a Postcard:","Places to Visit:","Useful Phrases:","Past Simple for Travel Stories:","Describing Places:"], correctAnswer: ["Describing Places:","Useful Phrases:","Past Simple for Travel Stories:"], hint: "Ищите термины, которые встречаются в уроке Sightseeing and Activities" },
      { type: 'quiz', question: "Что является основным понятием урока \"Sightseeing and Activities\"?", options: ["Writing a Postcard:","Fountain","How much is the entrance fee?","Describing Places:","- Did you go to the Eiffel Tower? - We didn't have enough ti"], correctAnswer: "- Did you go to the Eiffel Tower? - We didn't have enough ti", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Environmental Problems 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"Climate change — изменение климата...\"?", options: ["Modal Verbs for Obligation:","Describing Places:","Writing a Postcard:","Past Simple for Travel Stories:","Climate change"], correctAnswer: "Climate change", hint: "Этот термин связан с темой: Environmental Problems" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Environmental Problems\"?", options: ["Technology Vocabulary:","Vocabulary for Solutions:","Modal Verbs for Environment:","Pros:","Internet Safety:"], correctAnswer: "Vocabulary for Solutions:", hint: "Ответ связан с уроком: Environmental Problems" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Environmental Problems\"?", options: ["forests","Vocabulary for Solutions:","Common Chores:","Modal Verbs for Environment:","Describing Places:"], correctAnswer: "forests", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Environmental Problems\":", options: ["First Conditional:","Causes:","Should:","Vocabulary for Solutions:","Must:","Consequences:"], correctAnswer: ["Should:","Causes:","Consequences:"], hint: "Ищите термины, которые встречаются в уроке Environmental Problems" },
      { type: 'quiz', question: "Что является основным понятием урока \"Environmental Problems\"?", options: ["Plastic","Causes:","Endangered species","Climate change","- People cut down forests"], correctAnswer: "- People cut down forests", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Digital World 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"Browse the web — просматривать веб-страницы...\"?", options: ["Tablet","Present Continuous:","Browse the web","Going to:","I have bought a new smartphone."], correctAnswer: "Browse the web", hint: "Этот термин связан с темой: Digital World" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Digital World\"?", options: ["Addiction to gadgets","Modal Verbs for Environment:","Keep your password safe.","Technology Vocabulary:","Pros:"], correctAnswer: "Technology Vocabulary:", hint: "Ответ связан с уроком: Digital World" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Digital World\"?", options: ["Internet Safety:","Must:","songs","Household Chores","Cons:"], correctAnswer: "songs", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Digital World\":", options: ["Internet Safety:","Present Perfect for Experience:","Technology Vocabulary:","Cons:","Pros:","Advantages and Disadvantages:"], correctAnswer: ["Cons:","Advantages and Disadvantages:","Present Perfect for Experience:"], hint: "Ищите термины, которые встречаются в уроке Digital World" },
      { type: 'quiz', question: "Что является основным понятием урока \"Digital World\"?", options: ["Advantages and Disadvantages:","- We have downloaded many songs","Addiction to gadgets","сайт","Computer"], correctAnswer: "- We have downloaded many songs", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  }
] = [
  {
    title: "Daily Routines and Habits 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Вопрос 1 по теме \"Daily Routines and Habits\"", options: ["Daily Routines and Habits","First Conditional:","Future Tenses for Plans:","Internet Safety:","Vocabulary for Solutions:"], correctAnswer: "Daily Routines and Habits", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 2 по теме \"Daily Routines and Habits\"", options: ["Daily Routines","Present Simple for Routines:","Household Chores","Past Simple for Travel Stories:","Daily Routines and Habits"], correctAnswer: "Daily Routines and Habits", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 3 по теме \"Daily Routines and Habits\"", options: ["Time Expressions:","Modal Verbs for Environment:","Daily Routines","Daily Routines and Habits","Transport:"], correctAnswer: "Daily Routines and Habits", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 4 по теме \"Daily Routines and Habits\"", options: ["Present Continuous:","Daily Routines and Habits","Writing a Postcard:","Useful Phrases:","Daily Routines"], correctAnswer: "Daily Routines and Habits", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 5 по теме \"Daily Routines and Habits\"", options: ["Daily Routines and Habits","Useful Phrases:","Environmental Issues:","Advantages and Disadvantages:","Technology Vocabulary:"], correctAnswer: "Daily Routines and Habits", hint: "Ответ связан с материалом урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Household Chores 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"Do the washing-up — мыть посуду...\"?", options: ["Must:","Modal Verbs for Obligation:","Do the washing-up","First Conditional:","Pros:"], correctAnswer: "Do the washing-up", hint: "Этот термин связан с темой: Household Chores" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Household Chores\"?", options: ["Frequency Adverbs:","Common Chores:","Environmental Issues:","Questions:","Travel Vocabulary:"], correctAnswer: "Questions:", hint: "Ответ связан с уроком: Household Chores" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Household Chores\"?", options: ["Do the washing-up","Common Chores:","Position in sentence:","beds","Daily Activities:"], correctAnswer: "beds", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Household Chores\":", options: ["Household Chores","Questions:","Have to / Has to:","Must:","Modal Verbs for Obligation:","Should:"], correctAnswer: ["Should:","Household Chores","Modal Verbs for Obligation:"], hint: "Ищите термины, которые встречаются в уроке Household Chores" },
      { type: 'quiz', question: "Что является основным понятием урока \"Household Chores\"?", options: ["Make the bed","Should:","- She has to wash the dishes","Questions:","Can you help me, please?"], correctAnswer: "- She has to wash the dishes", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Planning a Trip 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"By bus — автобусом...\"?", options: ["Boarding pass","Present Continuous:","By bus","Frequency Adverbs:","Excursion"], correctAnswer: "By bus", hint: "Этот термин связан с темой: Planning a Trip" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Planning a Trip\"?", options: ["Present Continuous:","Tour","Daily Activities:","Environmental Issues:","Technology Vocabulary:"], correctAnswer: "Present Continuous:", hint: "Ответ связан с уроком: Planning a Trip" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Planning a Trip\"?", options: ["Household Chores","Luggage / baggage","Past Simple for Travel Stories:","Time Expressions:","week"], correctAnswer: "week", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Planning a Trip\":", options: ["Going to:","Travel Vocabulary:","Booking a Hotel:","Transport:","Future Tenses for Plans:","At the Airport:"], correctAnswer: ["Future Tenses for Plans:","At the Airport:","Travel Vocabulary:"], hint: "Ищите термины, которые встречаются в уроке Planning a Trip" },
      { type: 'quiz', question: "Что является основным понятием урока \"Planning a Trip\"?", options: ["**Present Continuous:** - I'm flying to London tomorrow","Book a room","At the Airport:","By ship","On foot"], correctAnswer: "**Present Continuous:** - I'm flying to London tomorrow", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Sightseeing and Activities 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"Gallery — галерея...\"?", options: ["Bridge","Gallery","Is it far from here?","Beautiful","Frequency Adverbs:"], correctAnswer: "Gallery", hint: "Этот термин связан с темой: Sightseeing and Activities" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Sightseeing and Activities\"?", options: ["Useful Phrases:","Environmental Issues:","Monument","How much is the entrance fee?","Transport:"], correctAnswer: "Useful Phrases:", hint: "Ответ связан с уроком: Sightseeing and Activities" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Sightseeing and Activities\"?", options: ["Cons:","Must:","Peaceful","Ancient","[plan]"], correctAnswer: "[plan]", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Sightseeing and Activities\":", options: ["Past Simple for Travel Stories:","Places to Visit:","Useful Phrases:","Writing a Postcard:","Describing Places:"], correctAnswer: ["Places to Visit:","Past Simple for Travel Stories:","Describing Places:"], hint: "Ищите термины, которые встречаются в уроке Sightseeing and Activities" },
      { type: 'quiz', question: "Что является основным понятием урока \"Sightseeing and Activities\"?", options: ["Past Simple for Travel Stories:","Useful Phrases:","Ancient","- Did you go to the Eiffel Tower? - We didn't have enough ti","Castle"], correctAnswer: "- Did you go to the Eiffel Tower? - We didn't have enough ti", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Environmental Problems 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"Use public transport — пользоваться общественным т...\"?", options: ["Internet Safety:","Use public transport","Pros:","Must:","Vocabulary for Solutions:"], correctAnswer: "Use public transport", hint: "Этот термин связан с темой: Environmental Problems" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Environmental Problems\"?", options: ["Booking a Hotel:","First Conditional:","Should:","Consequences:","Waste"], correctAnswer: "Consequences:", hint: "Ответ связан с уроком: Environmental Problems" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Environmental Problems\"?", options: ["Causes:","Global warming","Past Simple for Travel Stories:","Vocabulary for Solutions:","plastic"], correctAnswer: "plastic", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Environmental Problems\":", options: ["Consequences:","Should:","Vocabulary for Solutions:","First Conditional:","Must:","Modal Verbs for Environment:"], correctAnswer: ["Should:","Modal Verbs for Environment:","Vocabulary for Solutions:"], hint: "Ищите термины, которые встречаются в уроке Environmental Problems" },
      { type: 'quiz', question: "Что является основным понятием урока \"Environmental Problems\"?", options: ["- People cut down forests","Reuse","Pollution","People cut down forests.","Modal Verbs for Environment:"], correctAnswer: "- People cut down forests", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Digital World 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Household Chores","Transport:","Describing Places:","Keep your password safe.","Digital Activities:"], correctAnswer: "Keep your password safe.", hint: "Этот термин связан с темой: Digital World" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Digital World\"?", options: ["Consequences:","Play online games","Advantages and Disadvantages:","Make video calls","Upload photos"], correctAnswer: "Advantages and Disadvantages:", hint: "Ответ связан с уроком: Digital World" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Digital World\"?", options: ["Must:","Present Continuous:","Smartphone","Have to / Has to:","information"], correctAnswer: "information", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Digital World\":", options: ["Cons:","Present Perfect for Experience:","Digital Activities:","Internet Safety:","Technology Vocabulary:","Advantages and Disadvantages:"], correctAnswer: ["Internet Safety:","Present Perfect for Experience:","Advantages and Disadvantages:"], hint: "Ищите термины, которые встречаются в уроке Digital World" },
      { type: 'quiz', question: "Что является основным понятием урока \"Digital World\"?", options: ["страницы","- We have downloaded many songs","Present Perfect for Experience:","Computer","Entertainment"], correctAnswer: "- We have downloaded many songs", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  }
] = [
  {
    title: "Daily Life",
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
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Which tense do we use for daily routines?", options: ["Present Continuous", "Present Simple", "Past Simple", "Future Simple", "Другой ответ"], correctAnswer: "Present Simple", hint: "I wake up at 7 AM every day" },
      { type: 'quiz', question: "What does 'usually' mean in Russian?", options: ["Никогда", "Обычно", "Иногда", "Всегда", "Другой ответ"], correctAnswer: "Обычно", hint: "Frequency adverb — 80%" },
      { type: 'quiz', question: "Where do you place frequency adverbs with 'to be'?", options: ["After 'to be'", "Before 'to be'", "At the beginning", "At the end", "Before the subject"], correctAnswer: "After 'to be'", hint: "She is never late" },
      { type: 'quiz', question: "What does 'go to bed' mean?", options: ["Идти в школу", "Ложиться спать", "Делать уборку", "Идти гулять", "Другой ответ"], correctAnswer: "Ложиться спать", hint: "Daily activity before sleeping" },
      { type: 'quiz', question: "Which phrase means 'вечером'?", options: ["In the morning", "In the afternoon", "In the evening", "At night", "Другой ответ"], correctAnswer: "In the evening", hint: "Time of day" }
    ],
    reward: { stars: 3, message: "Great! You know daily routines! 🕐" }
  },
  {
    title: "Household Chores",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What does 'do the washing-up' mean?", options: ["Стирать бельё", "Мыть посуду", "Убираться", "Гладить", "Другой ответ"], correctAnswer: "Мыть посуду", hint: "Work with dishes" },
      { type: 'quiz', question: "Which modal verb expresses strong obligation?", options: ["Should", "Must", "Can", "May", "Другой ответ"], correctAnswer: "Must", hint: "You must help your parents" },
      { type: 'quiz', question: "What does 'make the bed' mean?", options: ["Построить кровать", "Заправлять постель", "Купить кровать", "Убрать комнату", "Другой ответ"], correctAnswer: "Заправлять постель", hint: "Morning household task" },
      { type: 'quiz', question: "What's the difference between 'make' and 'do'?", options: ["They are the same", "Make = create, Do = perform/complete", "Make = clean, Do = build", "Make = destroy, Do = fix", "Другой ответ"], correctAnswer: "Make = create, Do = perform/complete", hint: "Make breakfast vs do homework" },
      { type: 'quiz', question: "How do you ask: «Какие домашние дела ты делаешь?»", options: ["What chores do you do?", "When do you clean?", "Where is your room?", "Why do you work?", "Другой ответ"], correctAnswer: "What chores do you do?", hint: "Question about household tasks" }
    ],
    reward: { stars: 3, message: "Great! You know household chores! 🧹" }
  },
  {
    title: "Planning a Trip",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What does 'boarding pass' mean in Russian?", options: ["Билет", "Посадочный талон", "Загранпаспорт", "Регистрация", "Другой ответ"], correctAnswer: "Посадочный талон", hint: "Document needed to board a plane" },
      { type: 'quiz', question: "Which phrase means 'I'm going to visit London'?", options: ["I will visit London", "I'm going to visit London", "I visit London", "I visited London", "Другой ответ"], correctAnswer: "I'm going to visit London", hint: "Going to + infinitive for plans" },
      { type: 'quiz', question: "What does 'by plane' mean?", options: ["На поезде", "Самолётом", "На машине", "Пешком", "Другой ответ"], correctAnswer: "Самолётом", hint: "Type of air transport" },
      { type: 'quiz', question: "What does 'check in' mean at a hotel?", options: ["Выселиться", "Заселиться", "Забронировать", "Оплатить", "Другой ответ"], correctAnswer: "Заселиться", hint: "Arrival procedure" },
      { type: 'quiz', question: "What's the difference between 'journey' and 'voyage'?", options: ["They are the same", "Journey = general trip, Voyage = sea journey", "Journey = sea, Voyage = land", "Journey = short, Voyage = long walk", "Другой ответ"], correctAnswer: "Journey = general trip, Voyage = sea journey", hint: "Voyage is specifically by ship" }
    ],
    reward: { stars: 3, message: "Great! You can plan a trip! ✈️" }
  },
  {
    title: "Sightseeing and Activities",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What does 'monument' mean in Russian?", options: ["Музей", "Памятник", "Площадь", "Фонтан", "Другой ответ"], correctAnswer: "Памятник", hint: "A structure commemorating a person or event" },
      { type: 'quiz', question: "Which tense is used for travel stories?", options: ["Present Simple", "Present Continuous", "Past Simple", "Future Simple", "Другой ответ"], correctAnswer: "Past Simple", hint: "I visited the Louvre last year" },
      { type: 'quiz', question: "How do you ask for directions to a museum?", options: ["What is a museum?", "How do I get to the museum?", "Where is the museum from?", "Do you like museums?", "Другой ответ"], correctAnswer: "How do I get to the museum?", hint: "Useful phrase for tourists" },
      { type: 'quiz', question: "What does 'ancient' mean?", options: ["Современный", "Древний", "Красивый", "Переполненный", "Другой ответ"], correctAnswer: "Древний", hint: "Adjective describing old places" },
      { type: 'quiz', question: "What is the Past Simple of 'see'?", options: ["Seed", "Saw", "Seen", "Seeing", "Другой ответ"], correctAnswer: "Saw", hint: "Irregular verb" }
    ],
    reward: { stars: 3, message: "Great! You're a sightseeing expert! 🏛️" }
  },
  {
    title: "Environmental Problems",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What does 'global warming' mean in Russian?", options: ["Глобальное потепление", "Глобальное заморозка", "Загрязнение воды", "Вырубка лесов", "Другой ответ"], correctAnswer: "Глобальное потепление", hint: "Rising temperatures on Earth" },
      { type: 'quiz', question: "Which modal verb gives advice?", options: ["Must", "Should", "Can", "Will", "Другой ответ"], correctAnswer: "Should", hint: "We should recycle more" },
      { type: 'quiz', question: "What does 'deforestation' mean?", options: ["Посадка деревьев", "Вырубка лесов", "Загрязнение воздуха", "Рекультивация", "Другой ответ"], correctAnswer: "Вырубка лесов", hint: "Cutting down forests" },
      { type: 'quiz', question: "Complete: If people recycle, there ___ less waste.", options: ["is", "will be", "was", "are", "Другой ответ"], correctAnswer: "will be", hint: "First Conditional: If + present, will + infinitive" },
      { type: 'quiz', question: "What does 'endangered species' mean?", options: ["Опасные животные", "Исчезающие виды", "Домашние питомцы", "Водные организмы", "Другой ответ"], correctAnswer: "Исчезающие виды", hint: "Animals at risk of extinction" }
    ],
    reward: { stars: 3, message: "Great! You care about the environment! 🌍" }
  },
  {
    title: "Digital World",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What does 'social media' mean in Russian?", options: ["Электронная почта", "Социальные сети", "Веб-сайт", "Блог", "Другой ответ"], correctAnswer: "Социальные сети", hint: "VK, Instagram, TikTok..." },
      { type: 'quiz', question: "Which tense is used for experiences?", options: ["Past Simple", "Present Simple", "Present Perfect", "Future Simple", "Другой ответ"], correctAnswer: "Present Perfect", hint: "I have already bought a new smartphone" },
      { type: 'quiz', question: "What does 'download' mean?", options: ["Загружать онлайн", "Скачивать файлы", "Удалять данные", "Отправлять письмо", "Другой ответ"], correctAnswer: "Скачивать файлы", hint: "Getting files from the internet" },
      { type: 'quiz', question: "Which is an important internet safety rule?", options: ["Share your password with friends", "Post personal information publicly", "Don't share personal information", "Accept all friend requests", "Другой ответ"], correctAnswer: "Don't share personal information", hint: "Stay safe online" },
      { type: 'quiz', question: "What does 'cyberbullying' mean?", options: ["Онлайн-игры", "Кибербуллинг — травля в интернете", "Компьютерные вирусы", "Социальные сети", "Другой ответ"], correctAnswer: "Кибербуллинг — травля в интернете", hint: "Disadvantage of technology" }
    ],
    reward: { stars: 3, message: "Great! You're a digital citizen! 📱" }
  }
]
