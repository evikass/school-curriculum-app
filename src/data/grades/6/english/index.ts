import { SubjectData, GameLesson } from '@/data/types'

export const lessons: SubjectData = {
  title: "Иностранный язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: ["My Family and Friends", "Daily Routine", "Hobbies and Interests", "Travelling"],
  detailedTopics: [
    {
      topic: "My Family and Friends",
      lessons: [
        {
          title: "Family Members",
          description: `**Family Vocabulary:**

**Immediate Family:**
- Mother / Mom / Mum — мама
- Father / Dad — папа
- Parents — родители
- Sister — сестра
- Brother — брат
- Grandmother / Grandma — бабушка
- Grandfather / Grandpa — дедушка
- Grandparents — бабушка и дедушка

**Extended Family:**
- Aunt — тётя
- Uncle — дядя
- Cousin — двоюродный брат/сестра
- Nephew — племянник
- Niece — племянница

**Possessive Adjectives:**
- I → my (my family)
- You → your (your brother)
- He → his (his father)
- She → her (her mother)
- We → our (our parents)
- They → their (their children)

**Example sentences:**
- This is my mother. Her name is Anna.
- I have a sister. Her name is Kate.
- My uncle lives in Moscow.

**Questions:**
- Do you have any brothers or sisters?
- How many people are in your family?
- What does your father do?`,
          tasks: [
            "Переведите: mother, father, sister, brother",
            "Составьте предложение с 'my mother'",
            "Как будет 'тётя' и 'дядя' по-английски?",
            "Задайте вопрос о семье"
          ]
        },
        {
          title: "Describing People",
          description: `**Physical Appearance:**

**Height and Build:**
- tall — высокий
- short — низкий
- medium height — среднего роста
- slim — стройный
- athletic — атлетический
- plump — полный

**Hair:**
- long / short hair — длинные / короткие волосы
- straight — прямые
- curly — кудрявые
- wavy — волнистые
- fair / blond — светлые
- dark — тёмные
- brown — каштановые
- red / ginger — рыжие

**Eyes:**
- blue eyes — голубые глаза
- brown eyes — карие глаза
- green eyes — зелёные глаза

**Character:**
- kind — добрый
- friendly — дружелюбный
- clever / smart — умный
- funny — смешной
- serious — серьёзный
- shy — застенчивый

**Structure:**
- He has got blue eyes. = He's got blue eyes.
- She is tall and slim.
- My friend is kind and funny.`,
          tasks: [
            "Опишите внешность друга",
            "Как сказать 'у него голубые глаза'?",
            "Переведите: tall, short, slim",
            "Опишите характер члена семьи"
          ]
        }
      ]
    },
    {
      topic: "Daily Routine",
      lessons: [
        {
          title: "Time and Daily Activities",
          description: `**Telling the Time:**

**Full hours:**
- It's 7 o'clock. — 7 часов.
- It's seven a.m. — 7 утра.
- It's seven p.m. — 7 вечера.

**Minutes:**
- It's half past seven. — Половина восьмого.
- It's quarter past seven. — Четверть восьмого.
- It's quarter to eight. — Без четверти восемь.

**Daily Activities:**
- wake up — просыпаться
- get up — вставать
- have breakfast — завтракать
- go to school — идти в школу
- have lunch — обедать
- do homework — делать домашнее задание
- have dinner — ужинать
- watch TV — смотреть телевизор
- go to bed — ложиться спать

**Present Simple for Routine:**
- I wake up at 7 o'clock.
- She goes to school at 8.
- We have dinner at 7 p.m.

**Questions:**
- What time do you get up?
- When do you do your homework?
- What do you do in the evening?`,
          tasks: [
            "Как сказать 'половина восьмого'?",
            "Расскажите о своём утреннем распорядке",
            "Переведите: wake up, have breakfast, go to bed",
            "Задайте вопрос о распорядке дня"
          ]
        },
        {
          title: "Days of the Week and Prepositions",
          description: `**Days of the Week:**
- Monday — понедельник
- Tuesday — вторник
- Wednesday — среда
- Thursday — четверг
- Friday — пятница
- Saturday — суббота
- Sunday — воскресенье

**Prepositions of Time:**

**AT — для времени:**
- at 7 o'clock — в 7 часов
- at noon — в полдень
- at night — ночью

**ON — для дней:**
- on Monday — в понедельник
- on Friday morning — в пятницу утром
- on my birthday — в мой день рождения

**IN — для месяцев, сезонов, времени суток:**
- in September — в сентябре
- in winter — зимой
- in the morning — утром
- in the evening — вечером

**Examples:**
- I go to school at 8 o'clock on weekdays.
- We visit our grandparents on Sunday.
- She reads books in the evening.

**Adverbs of Frequency:**
- always (100%) — всегда
- usually (80%) — обычно
- often (60%) — часто
- sometimes (40%) — иногда
- rarely (20%) — редко
- never (0%) — никогда

**Position:** перед глаголом
- I always have breakfast.
- She never watches TV in the morning.`,
          tasks: [
            "Назовите дни недели по-английски",
            "Когда используем at, on, in?",
            "Составьте предложение с 'usually'",
            "Переведите: всегда, иногда, никогда"
          ]
        }
      ]
    },
    {
      topic: "Hobbies and Interests",
      lessons: [
        {
          title: "Free Time Activities",
          description: `**Hobbies:**

**Sports:**
- play football — играть в футбол
- play basketball — играть в баскетбол
- play tennis — играть в теннис
- swim — плавать
- run — бегать
- ride a bike — кататься на велосипеде

**Creative Activities:**
- draw — рисовать
- paint — писать красками
- play the guitar — играть на гитаре
- play the piano — играть на пианино
- sing — петь
- dance — танцевать

**Other Activities:**
- read books — читать книги
- watch films — смотреть фильмы
- play computer games — играть в компьютерные игры
- listen to music — слушать музыку
- collect stamps — коллекционировать марки
- take photos — фотографировать

**Questions about hobbies:**
- What do you like doing?
- What are your hobbies?
- Do you play any sports?

**Answers:**
- I like reading books.
- My hobby is photography.
- I enjoy playing football.
- I'm interested in music.

**Like / Love / Enjoy + V-ing:**
- I like swimming.
- She loves dancing.
- He enjoys reading.`,
          tasks: [
            "Переведите хобби: читать, плавать, рисовать",
            "Расскажите о своих увлечениях",
            "Как спросить о хобби?",
            "Составьте предложения с 'like' и 'enjoy'"
          ]
        },
        {
          title: "Can / Can't for Abilities",
          description: `**Modal Verb CAN:**

**Ability:**
- I can swim. — Я умею плавать.
- She can play the piano. — Она умеет играть на пианино.
- He can't drive. — Он не умеет водить.

**Questions:**
- Can you swim? — Ты умеешь плавать?
- Can she speak English? — Она умеет говорить по-английски?

**Short answers:**
- Yes, I can. / No, I can't.
- Yes, she can. / No, she can't.

**Abilities:**
- speak English — говорить по-английски
- play chess — играть в шахматы
- cook — готовить
- ride a bike — кататься на велосипеде
- use a computer — пользоваться компьютером
- sing — петь

**Conversation:**
A: Can you play the guitar?
B: No, I can't. But I can play the piano.

A: What languages can you speak?
B: I can speak English and Russian.

**Requests:**
- Can you help me? — Ты можешь мне помочь?
- Can I borrow your pen? — Можно одолжить ручку?`,
          tasks: [
            "Как сказать 'я умею плавать'?",
            "Задайте вопрос об умении",
            "Ответьте кратко: Can you speak English?",
            "Расскажите, что вы умеете делать"
          ]
        }
      ]
    },
    {
      topic: "Travelling",
      lessons: [
        {
          title: "At the Airport",
          description: `**Airport Vocabulary:**

**Places:**
- airport — аэропорт
- departure lounge — зал вылета
- arrival hall — зал прилёта
- gate — выход на посадку
- baggage claim — выдача багажа
- customs — таможня
- check-in desk — стойка регистрации

**Things:**
- passport — паспорт
- ticket — билет
- boarding pass — посадочный талон
- luggage / baggage — багаж
- suitcase — чемодан

**Actions:**
- check in — регистрироваться
- board the plane — садиться в самолёт
- take off — взлетать
- land — приземляться

**Useful Phrases:**
- Where is gate 5? — Где выход 5?
- I'd like a window seat. — Я хотел бы место у окна.
- What time does the flight leave? — Во сколько вылет?
- Here is my passport. — Вот мой паспорт.

**Announcements:**
- Flight KL123 is now boarding. — Рейс KL123 объявляет посадку.
- Please fasten your seatbelts. — Пожалуйста, пристегните ремни.
- The flight is delayed. — Рейс задержан.`,
          tasks: [
            "Переведите: passport, ticket, luggage",
            "Как спросить 'Где выход 5?'",
            "Что говорят при посадке?",
            "Составьте диалог в аэропорту"
          ]
        },
        {
          title: "Countries and Nationalities",
          description: `**Countries and Nationalities:**

| Country | Nationality |
|---------|-------------|
| Russia | Russian |
| England | English |
| the USA | American |
| France | French |
| Germany | German |
| Spain | Spanish |
| Italy | Italian |
| China | Chinese |
| Japan | Japanese |

**Capital Cities:**
- Moscow is the capital of Russia.
- London is the capital of England.
- Paris is the capital of France.
- Washington D.C. is the capital of the USA.

**Questions:**
- Where are you from? — Откуда ты?
- I'm from Russia. — Я из России.
- What nationality are you? — Кто ты по национальности?
- I'm Russian. — Я русский.

**Languages:**
- Russian — русский язык
- English — английский язык
- French — французский язык
- German — немецкий язык
- Spanish — испанский язык

**Speaking languages:**
- I speak Russian. — Я говорю по-русски.
- She speaks English. — Она говорит по-английски.
- They speak French. — Они говорят по-французски.`,
          tasks: [
            "Назовите 5 стран и национальностей",
            "Как спросить 'Откуда ты?'",
            "Расскажите о столицах стран",
            "Составьте диалог о стране"
          ]
        }
      ]
    }
  ]
}

export const games: GameLesson[] = [
  {
    title: "Family and Appearance",
    subject: "English",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say 'мама' in English?", options: ["Father", "Mother", "Sister", "Brother"], correctAnswer: "Mother", hint: "Female parent" },
      { type: 'find', question: "Choose family members:", options: ["Mother", "Teacher", "Father", "Doctor", "Sister", "Driver"], correctAnswer: ["Mother", "Father", "Sister"], hint: "People in a family" },
      { type: 'quiz', question: "What does 'slim' mean?", options: ["Высокий", "Стройный", "Полный", "Низкий"], correctAnswer: "Стройный", hint: "Body type" },
      { type: 'quiz', question: "How do you say 'у него голубые глаза'?", options: ["He has green eyes", "He has blue eyes", "He has brown eyes", "He has black eyes"], correctAnswer: "He has blue eyes", hint: "Eye color" }
    ],
    reward: { stars: 3, message: "Great! You know family vocabulary! 👨‍👩‍👧‍👦" }
  },
  {
    title: "Time and Routine",
    subject: "English",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What time is 'half past seven'?", options: ["7:00", "7:15", "7:30", "7:45"], correctAnswer: "7:30", hint: "30 minutes after 7" },
      { type: 'find', question: "Choose daily activities:", options: ["Wake up", "Play", "Have breakfast", "Sleep", "Go to school", "Run"], correctAnswer: ["Wake up", "Have breakfast", "Go to school"], hint: "Morning activities" },
      { type: 'quiz', question: "Which preposition: '___ Monday'?", options: ["at", "on", "in", "to"], correctAnswer: "on", hint: "For days of the week" },
      { type: 'quiz', question: "What does 'usually' mean?", options: ["Всегда", "Обычно", "Иногда", "Никогда"], correctAnswer: "Обычно", hint: "Adverb of frequency" }
    ],
    reward: { stars: 3, message: "Great! You know daily routine! ⏰" }
  }
]
