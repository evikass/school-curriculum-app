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
          ]
        }
      ]
    }
  ]
}

export const games: GameLesson[] = [
  {
    title: "Daily Routines and Habits",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Daily Routines?",
        options: ["повседневные дела и привычки.", "Это понятие из другого раздела", "Вспомогательный термин", "Специальный метод вычисления", "Понятие, обратное данному"],
        correctAnswer: "повседневные дела и привычки.",
        hint: "Вспомни определение из урока про Daily Routines"
      },
      {
        type: 'quiz',
        question: "Что такое Present Simple for Routines:?",
        options: ["Вспомогательный термин", "Это понятие из другого раздела", "Специальный метод вычисления", "I usually wake up at 7 o'clock.", "Понятие, обратное данному"],
        correctAnswer: "I usually wake up at 7 o'clock.",
        hint: "Вспомни определение из урока про Present Simple for Routines:"
      },
      {
        type: 'quiz',
        question: "Что такое Frequency Adverbs:?",
        options: ["Понятие, обратное данному", "Always — всегда (100%)", "Это понятие из другого раздела", "Вспомогательный термин", "Специальный метод вычисления"],
        correctAnswer: "Always — всегда (100%)",
        hint: "Вспомни определение из урока про Frequency Adverbs:"
      },
      {
        type: 'quiz',
        question: "Что такое Position in sentence:?",
        options: ["Понятие, обратное данному", "Специальный метод вычисления", "Вспомогательный термин", "Это понятие из другого раздела", "Before the main verb: I always eat breakfast."],
        correctAnswer: "Before the main verb: I always eat breakfast.",
        hint: "Вспомни определение из урока про Position in sentence:"
      },
      {
        type: 'quiz',
        question: "Что такое Daily Activities:?",
        options: ["Специальный метод вычисления", "Понятие, обратное данному", "Это понятие из другого раздела", "Wake up — просыпаться", "Вспомогательный термин"],
        correctAnswer: "Wake up — просыпаться",
        hint: "Вспомни определение из урока про Daily Activities:"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Household Chores",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Household Chores?",
        options: ["домашние обязанности.", "Понятие, обратное данному", "Вспомогательный термин", "Это понятие из другого раздела", "Специальный метод вычисления"],
        correctAnswer: "домашние обязанности.",
        hint: "Вспомни определение из урока про Household Chores"
      },
      {
        type: 'quiz',
        question: "Что такое Common Chores:?",
        options: ["Do the washing-up — мыть посуду", "Понятие, обратное данному", "Вспомогательный термин", "Специальный метод вычисления", "Это понятие из другого раздела"],
        correctAnswer: "Do the washing-up — мыть посуду",
        hint: "Вспомни определение из урока про Common Chores:"
      },
      {
        type: 'quiz',
        question: "Что такое Have to / Has to:?",
        options: ["Вспомогательный термин", "I have to clean my room.", "Специальный метод вычисления", "Это понятие из другого раздела", "Понятие, обратное данному"],
        correctAnswer: "I have to clean my room.",
        hint: "Вспомни определение из урока про Have to / Has to:"
      },
      {
        type: 'quiz',
        question: "Что такое Must:?",
        options: ["Специальный метод вычисления", "Понятие, обратное данному", "You must help your parents.", "Вспомогательный термин", "Это понятие из другого раздела"],
        correctAnswer: "You must help your parents.",
        hint: "Вспомни определение из урока про Must:"
      },
      {
        type: 'quiz',
        question: "Что такое Should:?",
        options: ["Понятие, обратное данному", "Это понятие из другого раздела", "Вспомогательный термин", "Специальный метод вычисления", "You should help your mother."],
        correctAnswer: "You should help your mother.",
        hint: "Вспомни определение из урока про Should:"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Planning a Trip",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Travel Vocabulary:?",
        options: ["Понятие, обратное данному", "Journey — путешествие", "Вспомогательный термин", "Специальный метод вычисления", "Это понятие из другого раздела"],
        correctAnswer: "Journey — путешествие",
        hint: "Вспомни определение из урока про Travel Vocabulary:"
      },
      {
        type: 'quiz',
        question: "Что такое Transport:?",
        options: ["Понятие, обратное данному", "Специальный метод вычисления", "Это понятие из другого раздела", "Вспомогательный термин", "By plane — самолётом"],
        correctAnswer: "By plane — самолётом",
        hint: "Вспомни определение из урока про Transport:"
      },
      {
        type: 'quiz',
        question: "Что такое At the Airport:?",
        options: ["Вспомогательный термин", "Специальный метод вычисления", "Понятие, обратное данному", "Это понятие из другого раздела", "Check-in — регистрация"],
        correctAnswer: "Check-in — регистрация",
        hint: "Вспомни определение из урока про At the Airport:"
      },
      {
        type: 'quiz',
        question: "Что такое Booking a Hotel:?",
        options: ["Специальный метод вычисления", "Это понятие из другого раздела", "Вспомогательный термин", "Book a room — забронировать номер", "Понятие, обратное данному"],
        correctAnswer: "Book a room — забронировать номер",
        hint: "Вспомни определение из урока про Booking a Hotel:"
      },
      {
        type: 'quiz',
        question: "Что такое Going to:?",
        options: ["Специальный метод вычисления", "Это понятие из другого раздела", "Понятие, обратное данному", "Вспомогательный термин", "I'm going to visit Paris."],
        correctAnswer: "I'm going to visit Paris.",
        hint: "Вспомни определение из урока про Going to:"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Sightseeing and Activities",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Places to Visit:?",
        options: ["Это понятие из другого раздела", "Вспомогательный термин", "Museum — музей", "Понятие, обратное данному", "Специальный метод вычисления"],
        correctAnswer: "Museum — музей",
        hint: "Вспомни определение из урока про Places to Visit:"
      },
      {
        type: 'quiz',
        question: "Что такое Useful Phrases:?",
        options: ["Вспомогательный термин", "What's there to see?", "Понятие, обратное данному", "Это понятие из другого раздела", "Специальный метод вычисления"],
        correctAnswer: "What's there to see?",
        hint: "Вспомни определение из урока про Useful Phrases:"
      },
      {
        type: 'quiz',
        question: "Что такое Describing Places:?",
        options: ["Это понятие из другого раздела", "Вспомогательный термин", "Beautiful — красивый", "Специальный метод вычисления", "Понятие, обратное данному"],
        correctAnswer: "Beautiful — красивый",
        hint: "Вспомни определение из урока про Describing Places:"
      },
      {
        type: 'quiz',
        question: "Что такое Past Simple for Travel Stories:?",
        options: ["Специальный метод вычисления", "I visited the Louvre last year.", "Понятие, обратное данному", "Это понятие из другого раздела", "Вспомогательный термин"],
        correctAnswer: "I visited the Louvre last year.",
        hint: "Вспомни определение из урока про Past Simple for Travel Stories:"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Places to Visit:»",
        options: ["Другой термин", "Связанный термин", "Дополнительный элемент", "Places to Visit:", "Вспомогательное понятие"],
        correctAnswer: "Places to Visit:",
        hint: "Это ключевое понятие из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Environmental Problems",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Environmental Issues:?",
        options: ["Pollution — загрязнение", "Это понятие из другого раздела", "Специальный метод вычисления", "Вспомогательный термин", "Понятие, обратное данному"],
        correctAnswer: "Pollution — загрязнение",
        hint: "Вспомни определение из урока про Environmental Issues:"
      },
      {
        type: 'quiz',
        question: "Что такое Causes:?",
        options: ["Cars produce exhaust fumes.", "Понятие, обратное данному", "Вспомогательный термин", "Это понятие из другого раздела", "Специальный метод вычисления"],
        correctAnswer: "Cars produce exhaust fumes.",
        hint: "Вспомни определение из урока про Causes:"
      },
      {
        type: 'quiz',
        question: "Что такое Consequences:?",
        options: ["Это понятие из другого раздела", "Специальный метод вычисления", "Animals lose their habitats.", "Понятие, обратное данному", "Вспомогательный термин"],
        correctAnswer: "Animals lose their habitats.",
        hint: "Вспомни определение из урока про Consequences:"
      },
      {
        type: 'quiz',
        question: "Что такое Should:?",
        options: ["Понятие, обратное данному", "Специальный метод вычисления", "Вспомогательный термин", "Это понятие из другого раздела", "We should recycle more."],
        correctAnswer: "We should recycle more.",
        hint: "Вспомни определение из урока про Should:"
      },
      {
        type: 'quiz',
        question: "Что такое Must:?",
        options: ["Специальный метод вычисления", "We must protect nature.", "Вспомогательный термин", "Понятие, обратное данному", "Это понятие из другого раздела"],
        correctAnswer: "We must protect nature.",
        hint: "Вспомни определение из урока про Must:"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Digital World",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Technology Vocabulary:?",
        options: ["Computer — компьютер", "Специальный метод вычисления", "Понятие, обратное данному", "Это понятие из другого раздела", "Вспомогательный термин"],
        correctAnswer: "Computer — компьютер",
        hint: "Вспомни определение из урока про Technology Vocabulary:"
      },
      {
        type: 'quiz',
        question: "Что такое Digital Activities:?",
        options: ["Специальный метод вычисления", "Понятие, обратное данному", "Это понятие из другого раздела", "Вспомогательный термин", "Go online — выходить в интернет"],
        correctAnswer: "Go online — выходить в интернет",
        hint: "Вспомни определение из урока про Digital Activities:"
      },
      {
        type: 'quiz',
        question: "Что такое Present Perfect for Experience:?",
        options: ["Понятие, обратное данному", "I have bought a new smartphone.", "Специальный метод вычисления", "Это понятие из другого раздела", "Вспомогательный термин"],
        correctAnswer: "I have bought a new smartphone.",
        hint: "Вспомни определение из урока про Present Perfect for Experience:"
      },
      {
        type: 'quiz',
        question: "Что такое Internet Safety:?",
        options: ["Это понятие из другого раздела", "Специальный метод вычисления", "Вспомогательный термин", "Понятие, обратное данному", "Keep your password safe."],
        correctAnswer: "Keep your password safe.",
        hint: "Вспомни определение из урока про Internet Safety:"
      },
      {
        type: 'quiz',
        question: "Что такое Pros:?",
        options: ["Это понятие из другого раздела", "Вспомогательный термин", "Специальный метод вычисления", "Понятие, обратное данному", "Easy communication"],
        correctAnswer: "Easy communication",
        hint: "Вспомни определение из урока про Pros:"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  }
]
