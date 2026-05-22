import { SubjectData, GameLesson } from '@/data/types'

export const lessons: SubjectData = {
  title: "Иностранный язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: [
    "Present Tenses",
    "Past Tenses",
    "Future Tenses",
    "Modal Verbs",
    "Passive Voice",
    "Conditionals",
    "Vocabulary: Daily Life",
    "Reading Comprehension"
  ],
  detailedTopics: [
    {
      topic: "Present Tenses",
      lessons: [
        {
          title: "Present Simple",
          description: `**Present Simple** используется для описания регулярных действий, фактов и постоянных состояний.

**Основные случаи употребления:**
- Регулярные, повторяющиеся действия: *I wake up at 7 o'clock every day.*
- Факты и общеизвестные истины: *The Earth goes round the Sun.*
- Постоянные состояния: *She lives in London.*
- Расписания и программы: *The train leaves at 9:30.*

**Образование утверждений:**
I/You/We/They + V (base form): *I work, we play*
He/She/It + V+s/es: *He works, she watches*

**Образование вопросов:**
Do + I/you/we/they + V?: *Do you like music?*
Does + he/she/it + V?: *Does he play football?*

**Образование отрицаний:**
I/You/We/They + don't + V: *I don't like coffee.*
He/She/It + doesn't + V: *She doesn't work here.*

**Слова-маркеры:**
always, usually, often, sometimes, rarely, never, every day, on Mondays

**Правила правописания:**
- work → works
- play → plays
- watch → watches, teach → teaches
- study → studies
- have → has

**Примеры:**
- *My brother works in a bank.*
- *Do you speak English?*
- *She doesn't eat meat.*`,
          tasks: [
            "Раскройте скобки: He (go) to school every day.",
            "Поставьте вопрос: She plays tennis on Sundays.",
            "Образуйте отрицание: They live in Moscow.",
            "Переведите: Мой папа всегда читает газету утром."
          ]
        },
        {
          title: "Present Continuous",
          description: `**Present Continuous** используется для описания действий, происходящих в данный момент.

**Основные случаи употребления:**
- Действие в момент речи: *I am reading a book now.*
- Временные ситуации: *She is staying with her aunt this week.*
- Развивающиеся ситуации: *The population is growing fast.*
- Планы на ближайшее будущее: *We are meeting tomorrow.*

**Образование:**
I + am + V-ing: *I am working.*
He/She/It + is + V-ing: *She is reading.*
We/You/They + are + V-ing: *They are playing.*

**Вопросы:**
Am I working? Is he reading? Are they playing?

**Отрицания:**
I am not working. She is not (isn't) reading. They are not (aren't) playing.

**Правила правописания:**
- work → working
- make → making (немая -e отпадает)
- run → running (удвоение согласной)
- lie → lying (ie → y)

**Слова-маркеры:**
now, at the moment, at present, today, this week, tonight

**Глаголы, не употребляющиеся в Continuous:**
- состояния: be, have, know, understand, believe
- чувства: like, love, hate, want, prefer
- восприятие: see, hear, smell, taste

**Примеры:**
- *Look! It is raining.*
- *What are you doing now?*
- *She isn't watching TV at the moment.*`,
          tasks: [
            "Раскройте скобки: Look! The children (play) in the garden.",
            "Поставьте вопрос: He is reading a newspaper now.",
            "Образуйте отрицание: We are watching TV.",
            "Выберите правильную форму: I (am knowing / know) him well."
          ]
        },
        {
          title: "Present Perfect",
          description: `**Present Perfect** связывает прошлое с настоящим.

**Основные случаи употребления:**
- Действие завершилось, результат важен сейчас: *I have lost my keys.* (не могу найти)
- Личный опыт: *I have been to Paris.*
- Недавние действия: *She has just arrived.*
- Действия с незавершённым временем: *I have written three letters today.*

**Образование:**
I/You/We/They + have + V3 (past participle)
He/She/It + has + V3

**Правильные глаголы:** work → worked
**Неправильные глаголы:** go → gone, see → seen, write → written

**Вопросы:**
Have you seen this film? Has she finished her work?

**Отрицания:**
I haven't seen him. She hasn't called me.

**Слова-маркеры:**
just, already, yet, ever, never, recently, lately
for (период времени), since (момент времени)

**Present Perfect vs Past Simple:**
- *I have lost my key.* (результат важен — не могу войти)
- *I lost my key yesterday.* (просто факт прошлого)

**Примеры:**
- *I have just finished my homework.*
- *Have you ever been to London?*
- *She has lived here for 5 years.*
- *We haven't met since 2020.*`,
          tasks: [
            "Раскройте скобки: I (see) this film already.",
            "Поставьте вопрос: She has finished the report.",
            "Заполните: I have known him ___ 2015. (for/since)",
            "Выберите время: We (went / have gone) to Paris last year."
          ]
        }
      ]
    },
    {
      topic: "Past Tenses",
      lessons: [
        {
          title: "Past Simple",
          description: `**Past Simple** используется для описания завершённых действий в прошлом.

**Основные случаи употребления:**
- Завершённые действия в прошлом: *I visited Paris last year.*
- Последовательность действий в прошлом: *He came home, had dinner and went to bed.*
- Повторяющиеся действия в прошлом: *We went to the cinema every weekend.*

**Образование правильных глаголов:**
V + ed: work → worked, play → played, watch → watched

**Образование неправильных глаголов:**
go → went, see → saw, have → had, come → came, do → did

**Вопросы:**
Did + subject + V?: *Did you see him yesterday?*

**Отрицания:**
subject + didn't + V: *I didn't go to school yesterday.*

**Правила правописания:**
- work → worked
- live → lived
- study → studied (y после согласной → i)
- stop → stopped (удвоение согласной)
- play → played

**Слова-маркеры:**
yesterday, last week/month/year, ... ago, in 2020, when I was young

**Глагол to be в Past Simple:**
I/He/She/It was: *I was at home.*
We/You/They were: *They were happy.*

**Примеры:**
- *We went to the cinema yesterday.*
- *Did she call you last night?*
- *He didn't understand the question.*
- *When I was a child, I liked ice cream.*`,
          tasks: [
            "Раскройте скобки: We (go) to the park last Sunday.",
            "Поставьте вопрос: She bought a new dress yesterday.",
            "Образуйте отрицание: He saw his friend at the party.",
            "Напишите 3-ю форму: go, see, have, come, do"
          ]
        },
        {
          title: "Past Continuous",
          description: `**Past Continuous** описывает действия, которые длились в определённый момент в прошлом.

**Основные случаи употребления:**
- Действие в определённый момент прошлого: *At 5 o'clock yesterday I was reading.*
- Два одновременных действия: *While I was cooking, my husband was reading.*
- Прерванное действие: *When the phone rang, I was sleeping.*
- Фоновое действие: *The sun was shining and the birds were singing.*

**Образование:**
was/were + V-ing

I/He/She/It was + V-ing: *She was reading.*
We/You/They were + V-ing: *They were playing.*

**Вопросы:**
Was she reading? Were they playing?

**Отрицания:**
She wasn't reading. They weren't playing.

**Сочетание с Past Simple:**
Когда одно действие прерывает другое:
- Длинное действие — Past Continuous
- Короткое действие — Past Simple

*When I came home, my mother was cooking dinner.*
*While I was walking, it started to rain.*

**Слова-маркеры:**
at 5 o'clock yesterday, at that moment, while, when

**Примеры:**
- *What were you doing at 8 p.m. yesterday?*
- *While he was driving, he was listening to music.*
- *I wasn't sleeping when you called.*`,
          tasks: [
            "Раскройте скобки: At 7 o'clock yesterday I (watch) TV.",
            "Соедините: While she (cook), the phone (ring).",
            "Образуйте отрицание: They were playing football at that time.",
            "Переведите: Когда я пришёл домой, мама готовила ужин."
          ]
        }
      ]
    },
    {
      topic: "Future Tenses",
      lessons: [
        {
          title: "Future Simple",
          description: `**Future Simple (will + V)** используется для будущих действий.

**Основные случаи употребления:**
- Мгновенные решения: *It's cold. I'll close the window.*
- Предсказания: *It will rain tomorrow.*
- Обещания: *I'll help you with your homework.*
- Предложения: *I'll carry your bag.*
- Угрозы: *I'll tell mum!*

**Образование:**
will + V (base form)

**Утверждения:**
I/You/He/She/We/They will come. (I'll come)

**Вопросы:**
Will you come to the party?

**Отрицания:**
I won't (will not) come.

**Слова-маркеры:**
tomorrow, next week/month/year, soon, in the future, in 2030

**Will vs Going to:**
- *I'll help you.* — мгновенное решение
- *I'm going to help you.* — запланированное действие

**Примеры:**
- *I think it will snow tomorrow.*
- *Will you marry me?*
- *She won't tell anyone.*
- *I'll call you later.*`,
          tasks: [
            "Раскройте скобки: I think it (be) cold tomorrow.",
            "Поставьте вопрос: She will come to the party.",
            "Образуйте отрицание: We will meet tomorrow.",
            "Выберите: Look at the clouds! It (will / is going to) rain."
          ]
        },
        {
          title: "To be going to",
          description: `**To be going to + V** используется для планов и намерений.

**Основные случаи употребления:**
- Планы и намерения: *I'm going to study medicine.*
- Предсказания на основе очевидных признаков: *Look at those clouds! It's going to rain.*

**Образование:**
am/is/are going to + V

I am going to + V: *I'm going to visit my grandmother.*
He/She/It is going to + V: *She's going to buy a car.*
We/You/They are going to + V: *They're going to move.*

**Вопросы:**
Am I going to pass? Is she going to come? Are they going to help?

**Отрицания:**
I'm not going to study. She isn't going to come. They aren't going to stay.

**Going to vs Present Continuous для планов:**
Оба используются для планов:
- *I'm going to meet Tom.* (намерение)
- *I'm meeting Tom at 5.* (договорённость)

**Going to vs Will:**
- *I'm going to study tonight.* (план)
- *I'll study tonight.* (решение в момент речи)

**Примеры:**
- *What are you going to do tomorrow?*
- *She's going to have a baby.*
- *He isn't going to sell his house.*`,
          tasks: [
            "Раскройте скобки: I (be going to) visit Paris next summer.",
            "Поставьте вопрос: She is going to buy a new car.",
            "Образуйте отрицание: They are going to leave early.",
            "Переведите: Я собираюсь стать врачом."
          ]
        }
      ]
    },
    {
      topic: "Modal Verbs",
      lessons: [
        {
          title: "Modal Verbs: Can, Could, Must",
          description: `**Modal Verbs (Модальные глаголы)** выражают отношение говорящего к действию.

**CAN — физическая возможность, умение:**
- *I can swim.* (Я умею плавать)
- *Can you help me?* (Можешь помочь?)
- *She can't speak French.* (Она не умеет говорить по-французски)

**COULD — вежливая просьба, возможность в прошлом:**
- *Could you open the door?* (Не могли бы вы открыть дверь?)
- *When I was young, I could run fast.* (В молодости я мог бегать быстро)

**MUST — обязанность, настоятельная необходимость:**
- *You must wear a uniform.* (Ты должен носить форму)
- *I must go now.* (Мне пора идти)
- *Must I do it now?* (Я должен делать это сейчас?)

**Особенности модальных глаголов:**
1. Не имеют окончаний -s, -ed, -ing
2. Не требуют вспомогательных глаголов
3. За ними следует инфинитив без to
4. Вопросы и отрицания образуются без do/does

**MUST vs HAVE TO:**
- *I must do it.* (личное решение)
- *I have to do it.* (внешняя необходимость)

**MUSTN'T vs DON'T HAVE TO:**
- *You mustn't smoke here.* (запрещено)
- *You don't have to come.* (не обязательно)

**Примеры:**
- *Can I borrow your pen?*
- *You must stop at the red light.*
- *She couldn't come yesterday.*`,
          tasks: [
            "Выберите: (Can / Must) you swim?",
            "Переведите: Ты должен сделать домашнее задание.",
            "Заполните: You (mustn't / don't have to) smoke here. It's forbidden.",
            "Образуйте вопрос: She can speak English."
          ]
        },
        {
          title: "Modal Verbs: Should, May, Might",
          description: `**SHOULD — совет, рекомендация:**
- *You should see a doctor.* (Тебе следует показаться врачу)
- *You shouldn't eat so much sugar.* (Тебе не стоит есть столько сахара)
- *What should I do?* (Что мне делать?)

**MAY — вероятность, разрешение (формально):**
- *It may rain tomorrow.* (Возможно, завтра пойдёт дождь)
- *May I come in?* (Можно войти?) — формально
- *May I help you?* (Разрешите помочь?)

**MIGHT — меньшая вероятность:**
- *It might snow tonight.* (Возможно, ночью пойдёт снег — меньше уверенности)
- *She might be at home.* (Она, возможно, дома)

**Степени вероятности:**
- *must be* — точно, наверняка (She must be tired.)
- *may be / might be* — возможно (She may be at work.)
- *can't be* — не может быть (It can't be true!)

**Модальные глаголы в прошедшем времени:**
- *could have done* — мог бы сделать (но не сделал)
- *should have done* — следовало сделать
- *might have done* — мог бы сделать

**Примеры:**
- *You should study harder.*
- *May I ask a question?*
- *He might come later.*`,
          tasks: [
            "Выберите: You (should / must) see a dentist. Your tooth hurts.",
            "Переведите: Возможно, она придёт завтра.",
            "Заполните: (May / Must) I use your phone?",
            "Образуйте вопрос: I should tell her the truth."
          ]
        }
      ]
    },
    {
      topic: "Passive Voice",
      lessons: [
        {
          title: "Passive Voice",
          description: `**Passive Voice (Страдательный залог)** — действие производится над подлежащим.

**Active:** *People speak English all over the world.*
**Passive:** *English is spoken all over the world.*

**Образование Passive Voice:**
to be + V3 (past participle)

**Present Simple Passive:**
am/is/are + V3
- *This book is written in English.*
- *Cars are made in Japan.*

**Past Simple Passive:**
was/were + V3
- *The letter was sent yesterday.*
- *The houses were built last year.*

**Future Simple Passive:**
will be + V3
- *The project will be finished soon.*

**Present Perfect Passive:**
have/has been + V3
- *The work has been done.*

**Когда используется Passive:**
1. Важен объект, а не исполнитель
2. Исполнитель неизвестен
3. Официальный стиль

**Предлог BY:**
Если указываем исполнителя:
- *This picture was painted by Picasso.*

**Примеры:**
- *English is spoken here.*
- *The report was written by the manager.*
- *When will the decision be made?*`,
          tasks: [
            "Преобразуйте в Passive: They built this house in 1900.",
            "Преобразуйте в Passive: People speak Spanish in many countries.",
            "Заполните: The book (write) by a famous author.",
            "Переведите: Письмо было отправлено вчера."
          ]
        }
      ]
    },
    {
      topic: "Conditionals",
      lessons: [
        {
          title: "Conditionals: Zero and First",
          description: `**Zero Conditional — факты и истины:**
If + Present Simple, Present Simple
- *If you heat water to 100°C, it boils.*
- *If I'm tired, I go to bed early.*

**First Conditional — реальные условия:**
If + Present Simple, will + V
- *If it rains, I will stay at home.*
- *If you study hard, you will pass the exam.*

**Структура First Conditional:**
If clause (условие) + Main clause (результат)
или
Main clause + If clause

**Вариации Main Clause:**
- *If you go to Paris, you can see the Eiffel Tower.* (can)
- *If you finish early, you may leave.* (may)
- *If you need help, call me.* (imperative)

**Unless = If not:**
- *Unless you hurry, you'll miss the bus.*
- (= If you don't hurry, you'll miss the bus.)

**When vs If:**
- *When I see him* — уверен, что увижу
- *If I see him* — не уверен

**Примеры:**
- *If the weather is good, we'll go for a walk.*
- *I won't come unless you invite me.*
- *If I have time, I'll call you.*`,
          tasks: [
            "Раскройте скобки: If she (come), I (be) happy.",
            "Переделайте: If you don't study, you won't pass. (use unless)",
            "Выберите тип: If you heat ice, it melts. (Zero/First)",
            "Переведите: Если будет хорошая погода, мы пойдём в парк."
          ]
        },
        {
          title: "Conditionals: Second and Third",
          description: `**Second Conditional — нереальные условия в настоящем:**
If + Past Simple, would + V
- *If I had a million dollars, I would buy a house.*
- *If I were you, I would accept the offer.*

**Важно:** were используется для всех лиц в Second Conditional
- *If I were you... / If she were here...*

**Second Conditional для советов:**
- *If I were you, I would study medicine.*

**Third Conditional — нереальные условия в прошлом:**
If + Past Perfect, would have + V3
- *If I had studied harder, I would have passed the exam.*
- *If she had come earlier, she would have seen him.*

**Таблица условных предложений:**

| Type | Condition | Result | Time |
|------|-----------|--------|------|
| Zero | Present | Present | Always |
| First | Present | will + V | Future |
| Second | Past | would + V | Present/Future (unreal) |
| Third | Past Perfect | would have + V3 | Past (unreal) |

**Примеры:**
- *If I knew the answer, I would tell you.* (Second)
- *If I had known the answer, I would have told you.* (Third)
- *If I were rich, I would travel the world.* (Second)`,
          tasks: [
            "Раскройте скобки: If I (be) you, I (go) to the doctor.",
            "Раскройте скобки: If she (study) harder, she (pass) the exam. (Third Conditional)",
            "Выберите тип: If I won the lottery, I would buy a house. (Second/Third)",
            "Переведите: Если бы я знал правду, я бы сказал тебе."
          ]
        }
      ]
    },
    {
      topic: "Vocabulary: Daily Life",
      lessons: [
        {
          title: "Daily Routine",
          description: `**Vocabulary: Daily Routine (Повседневные дела)**

**Утро (Morning):**
- wake up — просыпаться
- get up — вставать
- have a shower — принимать душ
- brush teeth — чистить зубы
- get dressed — одеваться
- have breakfast — завтракать
- leave home — выходить из дома
- go to school/work — идти в школу/на работу

**День (Day):**
- have lunch — обедать
- have classes — посещать уроки
- study — учиться
- do homework — делать домашнее задание
- work — работать
- have a break — делать перерыв

**Вечер (Evening):**
- come home — приходить домой
- have dinner — ужинать
- watch TV — смотреть телевизор
- read a book — читать книгу
- surf the Internet — сидеть в Интернете
- go to bed — ложиться спать

**Предлоги времени:**
- at 7 o'clock, at noon, at night
- in the morning, in the afternoon, in the evening
- on Monday, on the 5th of May

**Примеры:**
- *I usually wake up at 7 o'clock.*
- *After school I have lunch and do my homework.*
- *In the evening I watch TV or read a book.*`,
          tasks: [
            "Переведите: Я обычно просыпаюсь в 7 часов.",
            "Заполните: I have breakfast ___ the morning. (at/in/on)",
            "Составьте предложение: she / usually / up / get / at 7 o'clock",
            "Переведите: После школы я делаю домашнее задание."
          ]
        },
        {
          title: "Hobbies and Free Time",
          description: `**Vocabulary: Hobbies and Free Time (Хобби и свободное время)**

**Виды хобби:**
- read books / magazines — читать книги/журналы
- watch films / series — смотреть фильмы/сериалы
- listen to music — слушать музыку
- play sports — заниматься спортом
- play computer games — играть в компьютерные игры
- draw / paint — рисовать
- dance — танцевать
- sing — петь
- cook — готовить
- travel — путешествовать
- take photos — фотографировать
- collect (stamps, coins) — коллекционировать

**Музыкальные инструменты:**
- play the piano — играть на пианино
- play the guitar — играть на гитаре
- play the violin — играть на скрипке

**Спорт:**
- play football / tennis / basketball
- go swimming — плавать
- go running — бегать
- go skiing — кататься на лыжах

**Вопросы о хобби:**
- *What do you do in your free time?*
- *What are your hobbies?*
- *Do you like reading?*
- *How often do you play sports?*

**Примеры:**
- *In my free time I like reading and listening to music.*
- *She's interested in photography.*
- *He's fond of playing football.*`,
          tasks: [
            "Переведите: В свободное время я люблю читать книги.",
            "Заполните: She can play ___ piano. (the/-)",
            "Составьте вопрос: you / do / What / do / free time / in your / ?",
            "Переведите: Я увлекаюсь фотографией."
          ]
        }
      ]
    },
    {
      topic: "Reading Comprehension",
      lessons: [
        {
          title: "Reading Strategies",
          description: `**Reading Strategies (Стратегии чтения)**

**Виды чтения:**

**1. Skimming (Просмотровое чтение):**
- Быстрое прочтение для общего понимания
- Чтение заголовков, первых и последних предложений
- Цель: понять главную идею текста

**2. Scanning (Поисковое чтение):**
- Поиск конкретной информации
- Чтение с вопросом в голове
- Цель: найти нужные факты, даты, имена

**3. Detailed Reading (Изучающее чтение):**
- Внимательное чтение всего текста
- Анализ деталей и деталей
- Цель: полное понимание

**Полезные приёмы:**
1. **Predicting:** предсказать содержание по заголовку
2. **Guessing meaning:** догадаться о значении слова по контексту
3. **Identifying keywords:** находить ключевые слова
4. **Understanding reference:** понимать местоимения (he, she, it, they)

**Структура текста:**
- Introduction (введение) — главная идея
- Body paragraphs (основная часть) — детали и примеры
- Conclusion (заключение) — итоги

**При чтении обращайте внимание на:**
- Title — заголовок
- First sentence — первое предложение
- Linking words — слова-связки (however, therefore, because)
- Numbers and dates — цифры и даты`,
          tasks: [
            "Определите тип чтения: Find all names in the text. (Skimming/Scanning/Detailed)",
            "Что такое skimming?",
            "Перечислите три части структуры текста.",
            "Как догадаться о значении незнакомого слова?"
          ]
        }
      ]
    }
  ]
}

export const games: GameLesson[] = [
  {
    title: "Present Simple",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Основные случаи употребления:?",
        options: ["Это понятие из другого раздела", "Понятие, обратное данному", "Специальный метод вычисления", "Регулярные, повторяющиеся действия:", "Вспомогательный термин"],
        correctAnswer: "Регулярные, повторяющиеся действия:",
        hint: "Вспомни определение из урока про Основные случаи употребления:"
      },
      {
        type: 'quiz',
        question: "Что такое Правила правописания:?",
        options: ["work → works", "Это понятие из другого раздела", "Понятие, обратное данному", "Вспомогательный термин", "Специальный метод вычисления"],
        correctAnswer: "work → works",
        hint: "Вспомни определение из урока про Правила правописания:"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Present Simple»",
        options: ["Вспомогательное понятие", "Present Simple", "Дополнительный элемент", "Другой термин", "Связанный термин"],
        correctAnswer: "Present Simple",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Основные случаи употребления:»",
        options: ["Основные случаи употребления:", "Другой термин", "Дополнительный элемент", "Связанный термин", "Вспомогательное понятие"],
        correctAnswer: "Основные случаи употребления:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Образование утверждений:»",
        options: ["Образование утверждений:", "Другой термин", "Вспомогательное понятие", "Дополнительный элемент", "Связанный термин"],
        correctAnswer: "Образование утверждений:",
        hint: "Это ключевое понятие из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Present Continuous",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Основные случаи употребления:?",
        options: ["Это понятие из другого раздела", "Специальный метод вычисления", "Вспомогательный термин", "Понятие, обратное данному", "Действие в момент речи:"],
        correctAnswer: "Действие в момент речи:",
        hint: "Вспомни определение из урока про Основные случаи употребления:"
      },
      {
        type: 'quiz',
        question: "Что такое Правила правописания:?",
        options: ["Вспомогательный термин", "Это понятие из другого раздела", "Понятие, обратное данному", "Специальный метод вычисления", "work → working"],
        correctAnswer: "work → working",
        hint: "Вспомни определение из урока про Правила правописания:"
      },
      {
        type: 'quiz',
        question: "Что такое Глаголы, не употребляющиеся в Continuous:?",
        options: ["Понятие, обратное данному", "состояния: be, have, know, understand, believe", "Специальный метод вычисления", "Вспомогательный термин", "Это понятие из другого раздела"],
        correctAnswer: "состояния: be, have, know, understand, believe",
        hint: "Вспомни определение из урока про Глаголы, не употребляющиеся в Continuous:"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Present Continuous»",
        options: ["Другой термин", "Present Continuous", "Вспомогательное понятие", "Связанный термин", "Дополнительный элемент"],
        correctAnswer: "Present Continuous",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Основные случаи употребления:»",
        options: ["Дополнительный элемент", "Связанный термин", "Вспомогательное понятие", "Другой термин", "Основные случаи употребления:"],
        correctAnswer: "Основные случаи употребления:",
        hint: "Это ключевое понятие из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Present Perfect",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Основные случаи употребления:?",
        options: ["Понятие, обратное данному", "Действие завершилось, результат важен сейчас:", "Специальный метод вычисления", "Это понятие из другого раздела", "Вспомогательный термин"],
        correctAnswer: "Действие завершилось, результат важен сейчас:",
        hint: "Вспомни определение из урока про Основные случаи употребления:"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Present Perfect»",
        options: ["Связанный термин", "Дополнительный элемент", "Present Perfect", "Другой термин", "Вспомогательное понятие"],
        correctAnswer: "Present Perfect",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Основные случаи употребления:»",
        options: ["Связанный термин", "Вспомогательное понятие", "Основные случаи употребления:", "Дополнительный элемент", "Другой термин"],
        correctAnswer: "Основные случаи употребления:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Образование:»",
        options: ["Образование:", "Связанный термин", "Дополнительный элемент", "Вспомогательное понятие", "Другой термин"],
        correctAnswer: "Образование:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Правильные глаголы:»",
        options: ["Вспомогательное понятие", "Дополнительный элемент", "Правильные глаголы:", "Связанный термин", "Другой термин"],
        correctAnswer: "Правильные глаголы:",
        hint: "Это ключевое понятие из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Past Simple",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Основные случаи употребления:?",
        options: ["Завершённые действия в прошлом:", "Понятие, обратное данному", "Специальный метод вычисления", "Вспомогательный термин", "Это понятие из другого раздела"],
        correctAnswer: "Завершённые действия в прошлом:",
        hint: "Вспомни определение из урока про Основные случаи употребления:"
      },
      {
        type: 'quiz',
        question: "Что такое Правила правописания:?",
        options: ["Специальный метод вычисления", "Понятие, обратное данному", "Это понятие из другого раздела", "work → worked", "Вспомогательный термин"],
        correctAnswer: "work → worked",
        hint: "Вспомни определение из урока про Правила правописания:"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Past Simple»",
        options: ["Дополнительный элемент", "Связанный термин", "Past Simple", "Вспомогательное понятие", "Другой термин"],
        correctAnswer: "Past Simple",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Основные случаи употребления:»",
        options: ["Вспомогательное понятие", "Другой термин", "Дополнительный элемент", "Основные случаи употребления:", "Связанный термин"],
        correctAnswer: "Основные случаи употребления:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Вопросы:»",
        options: ["Связанный термин", "Вопросы:", "Другой термин", "Дополнительный элемент", "Вспомогательное понятие"],
        correctAnswer: "Вопросы:",
        hint: "Это ключевое понятие из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Past Continuous",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Основные случаи употребления:?",
        options: ["Понятие, обратное данному", "Действие в определённый момент прошлого:", "Специальный метод вычисления", "Вспомогательный термин", "Это понятие из другого раздела"],
        correctAnswer: "Действие в определённый момент прошлого:",
        hint: "Вспомни определение из урока про Основные случаи употребления:"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Past Continuous»",
        options: ["Вспомогательное понятие", "Другой термин", "Past Continuous", "Дополнительный элемент", "Связанный термин"],
        correctAnswer: "Past Continuous",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Основные случаи употребления:»",
        options: ["Дополнительный элемент", "Основные случаи употребления:", "Вспомогательное понятие", "Другой термин", "Связанный термин"],
        correctAnswer: "Основные случаи употребления:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Образование:»",
        options: ["Дополнительный элемент", "Образование:", "Вспомогательное понятие", "Связанный термин", "Другой термин"],
        correctAnswer: "Образование:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Вопросы:»",
        options: ["Другой термин", "Связанный термин", "Вспомогательное понятие", "Вопросы:", "Дополнительный элемент"],
        correctAnswer: "Вопросы:",
        hint: "Это ключевое понятие из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Future Simple",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Основные случаи употребления:?",
        options: ["Понятие, обратное данному", "Это понятие из другого раздела", "Специальный метод вычисления", "Мгновенные решения:", "Вспомогательный термин"],
        correctAnswer: "Мгновенные решения:",
        hint: "Вспомни определение из урока про Основные случаи употребления:"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Future Simple (will + V)»",
        options: ["Связанный термин", "Дополнительный элемент", "Другой термин", "Вспомогательное понятие", "Future Simple (will + V)"],
        correctAnswer: "Future Simple (will + V)",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Основные случаи употребления:»",
        options: ["Дополнительный элемент", "Другой термин", "Основные случаи употребления:", "Вспомогательное понятие", "Связанный термин"],
        correctAnswer: "Основные случаи употребления:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Образование:»",
        options: ["Образование:", "Связанный термин", "Другой термин", "Дополнительный элемент", "Вспомогательное понятие"],
        correctAnswer: "Образование:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Утверждения:»",
        options: ["Связанный термин", "Вспомогательное понятие", "Утверждения:", "Другой термин", "Дополнительный элемент"],
        correctAnswer: "Утверждения:",
        hint: "Это ключевое понятие из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "To be going to",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Основные случаи употребления:?",
        options: ["Понятие, обратное данному", "Специальный метод вычисления", "Это понятие из другого раздела", "Планы и намерения:", "Вспомогательный термин"],
        correctAnswer: "Планы и намерения:",
        hint: "Вспомни определение из урока про Основные случаи употребления:"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «To be going to + V»",
        options: ["Другой термин", "Связанный термин", "Дополнительный элемент", "Вспомогательное понятие", "To be going to + V"],
        correctAnswer: "To be going to + V",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Основные случаи употребления:»",
        options: ["Связанный термин", "Основные случаи употребления:", "Дополнительный элемент", "Другой термин", "Вспомогательное понятие"],
        correctAnswer: "Основные случаи употребления:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Образование:»",
        options: ["Другой термин", "Дополнительный элемент", "Связанный термин", "Образование:", "Вспомогательное понятие"],
        correctAnswer: "Образование:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Вопросы:»",
        options: ["Вопросы:", "Другой термин", "Вспомогательное понятие", "Дополнительный элемент", "Связанный термин"],
        correctAnswer: "Вопросы:",
        hint: "Это ключевое понятие из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Modal Verbs: Can, Could, Must",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «MUST vs HAVE TO:»",
        options: ["MUST vs HAVE TO:", "Дополнительный элемент", "Другой термин", "Вспомогательное понятие", "Связанный термин"],
        correctAnswer: "MUST vs HAVE TO:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «MUSTN'T vs DON'T HAVE TO:»",
        options: ["MUSTN'T vs DON'T HAVE TO:", "Дополнительный элемент", "Связанный термин", "Другой термин", "Вспомогательное понятие"],
        correctAnswer: "MUSTN'T vs DON'T HAVE TO:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Примеры:»",
        options: ["Связанный термин", "Другой термин", "Дополнительный элемент", "Вспомогательное понятие", "Примеры:"],
        correctAnswer: "Примеры:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: Modal Verbs (Модальные глаголы) выражают отношение говорящего к действию.",
        options: ["Частично верно", "Зависит от контекста", "Нет, неверно", "Только в некоторых случаях", "Да, верно"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: CAN — физическая возможность, умение: - *I can swim.",
        options: ["Нет, неверно", "Только в некоторых случаях", "Частично верно", "Да, верно", "Зависит от контекста"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Modal Verbs: Should, May, Might",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «SHOULD — совет, рекомендация:»",
        options: ["Вспомогательное понятие", "Дополнительный элемент", "SHOULD — совет, рекомендация:", "Другой термин", "Связанный термин"],
        correctAnswer: "SHOULD — совет, рекомендация:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «MIGHT — меньшая вероятность:»",
        options: ["Дополнительный элемент", "MIGHT — меньшая вероятность:", "Связанный термин", "Другой термин", "Вспомогательное понятие"],
        correctAnswer: "MIGHT — меньшая вероятность:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Степени вероятности:»",
        options: ["Вспомогательное понятие", "Дополнительный элемент", "Другой термин", "Степени вероятности:", "Связанный термин"],
        correctAnswer: "Степени вероятности:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Примеры:»",
        options: ["Примеры:", "Другой термин", "Дополнительный элемент", "Вспомогательное понятие", "Связанный термин"],
        correctAnswer: "Примеры:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: SHOULD — совет, рекомендация: - *You should see a doctor.",
        options: ["Зависит от контекста", "Частично верно", "Да, верно", "Нет, неверно", "Только в некоторых случаях"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Passive Voice",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Passive Voice (Страдательный залог)?",
        options: ["действие производится над подлежащим.", "Понятие, обратное данному", "Вспомогательный термин", "Это понятие из другого раздела", "Специальный метод вычисления"],
        correctAnswer: "действие производится над подлежащим.",
        hint: "Вспомни определение из урока про Passive Voice (Страдательный залог)"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Active:»",
        options: ["Active:", "Дополнительный элемент", "Вспомогательное понятие", "Другой термин", "Связанный термин"],
        correctAnswer: "Active:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Passive:»",
        options: ["Дополнительный элемент", "Связанный термин", "Другой термин", "Вспомогательное понятие", "Passive:"],
        correctAnswer: "Passive:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Образование Passive Voice:»",
        options: ["Дополнительный элемент", "Связанный термин", "Вспомогательное понятие", "Другой термин", "Образование Passive Voice:"],
        correctAnswer: "Образование Passive Voice:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Present Simple Passive:»",
        options: ["Вспомогательное понятие", "Другой термин", "Present Simple Passive:", "Дополнительный элемент", "Связанный термин"],
        correctAnswer: "Present Simple Passive:",
        hint: "Это ключевое понятие из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Conditionals: Zero and First",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Структура First Conditional:»",
        options: ["Структура First Conditional:", "Вспомогательное понятие", "Дополнительный элемент", "Связанный термин", "Другой термин"],
        correctAnswer: "Структура First Conditional:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Вариации Main Clause:»",
        options: ["Связанный термин", "Другой термин", "Вспомогательное понятие", "Дополнительный элемент", "Вариации Main Clause:"],
        correctAnswer: "Вариации Main Clause:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Unless = If not:»",
        options: ["Дополнительный элемент", "Связанный термин", "Вспомогательное понятие", "Unless = If not:", "Другой термин"],
        correctAnswer: "Unless = If not:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «When vs If:»",
        options: ["Дополнительный элемент", "Вспомогательное понятие", "Другой термин", "When vs If:", "Связанный термин"],
        correctAnswer: "When vs If:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Примеры:»",
        options: ["Дополнительный элемент", "Примеры:", "Вспомогательное понятие", "Связанный термин", "Другой термин"],
        correctAnswer: "Примеры:",
        hint: "Это ключевое понятие из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Conditionals: Second and Third",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Важно:»",
        options: ["Связанный термин", "Дополнительный элемент", "Другой термин", "Вспомогательное понятие", "Важно:"],
        correctAnswer: "Важно:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Таблица условных предложений:»",
        options: ["Вспомогательное понятие", "Связанный термин", "Дополнительный элемент", "Таблица условных предложений:", "Другой термин"],
        correctAnswer: "Таблица условных предложений:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Примеры:»",
        options: ["Дополнительный элемент", "Вспомогательное понятие", "Примеры:", "Другой термин", "Связанный термин"],
        correctAnswer: "Примеры:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: условия в настоящем: If + Past Simple, would + V - *If I had a million dollars, I would buy a house.",
        options: ["Только в некоторых случаях", "Нет, неверно", "Частично верно", "Зависит от контекста", "Да, верно"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
      {
        type: 'quiz',
        question: "Верно ли утверждение: * - *If I were you, I would accept the offer.",
        options: ["Нет, неверно", "Да, верно", "Зависит от контекста", "Частично верно", "Только в некоторых случаях"],
        correctAnswer: "Да, верно",
        hint: "Это утверждение из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Daily Routine",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Утро (Morning):?",
        options: ["wake up — просыпаться", "Вспомогательный термин", "Понятие, обратное данному", "Это понятие из другого раздела", "Специальный метод вычисления"],
        correctAnswer: "wake up — просыпаться",
        hint: "Вспомни определение из урока про Утро (Morning):"
      },
      {
        type: 'quiz',
        question: "Что такое День (Day):?",
        options: ["Специальный метод вычисления", "have lunch — обедать", "Вспомогательный термин", "Это понятие из другого раздела", "Понятие, обратное данному"],
        correctAnswer: "have lunch — обедать",
        hint: "Вспомни определение из урока про День (Day):"
      },
      {
        type: 'quiz',
        question: "Что такое Вечер (Evening):?",
        options: ["Понятие, обратное данному", "Специальный метод вычисления", "Вспомогательный термин", "Это понятие из другого раздела", "come home — приходить домой"],
        correctAnswer: "come home — приходить домой",
        hint: "Вспомни определение из урока про Вечер (Evening):"
      },
      {
        type: 'quiz',
        question: "Что такое Предлоги времени:?",
        options: ["at 7 o'clock, at noon, at night", "Специальный метод вычисления", "Вспомогательный термин", "Понятие, обратное данному", "Это понятие из другого раздела"],
        correctAnswer: "at 7 o'clock, at noon, at night",
        hint: "Вспомни определение из урока про Предлоги времени:"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Утро (Morning):»",
        options: ["Дополнительный элемент", "Вспомогательное понятие", "Связанный термин", "Другой термин", "Утро (Morning):"],
        correctAnswer: "Утро (Morning):",
        hint: "Это ключевое понятие из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Hobbies and Free Time",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое Виды хобби:?",
        options: ["Это понятие из другого раздела", "Специальный метод вычисления", "read books / magazines — читать книги/журналы", "Вспомогательный термин", "Понятие, обратное данному"],
        correctAnswer: "read books / magazines — читать книги/журналы",
        hint: "Вспомни определение из урока про Виды хобби:"
      },
      {
        type: 'quiz',
        question: "Что такое Музыкальные инструменты:?",
        options: ["Понятие, обратное данному", "Вспомогательный термин", "Это понятие из другого раздела", "Специальный метод вычисления", "play the piano — играть на пианино"],
        correctAnswer: "play the piano — играть на пианино",
        hint: "Вспомни определение из урока про Музыкальные инструменты:"
      },
      {
        type: 'quiz',
        question: "Что такое Спорт:?",
        options: ["Это понятие из другого раздела", "Понятие, обратное данному", "Вспомогательный термин", "play football / tennis / basketball", "Специальный метод вычисления"],
        correctAnswer: "play football / tennis / basketball",
        hint: "Вспомни определение из урока про Спорт:"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Виды хобби:»",
        options: ["Дополнительный элемент", "Связанный термин", "Другой термин", "Виды хобби:", "Вспомогательное понятие"],
        correctAnswer: "Виды хобби:",
        hint: "Это ключевое понятие из урока"
      },
      {
        type: 'quiz',
        question: "Какой термин пропущен? В уроке говорится о «Музыкальные инструменты:»",
        options: ["Вспомогательное понятие", "Музыкальные инструменты:", "Дополнительный элемент", "Другой термин", "Связанный термин"],
        correctAnswer: "Музыкальные инструменты:",
        hint: "Это ключевое понятие из урока"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  },
  {
    title: "Reading Strategies",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Что такое 1. Skimming (Просмотровое чтение):?",
        options: ["Специальный метод вычисления", "Быстрое прочтение для общего понимания", "Понятие, обратное данному", "Вспомогательный термин", "Это понятие из другого раздела"],
        correctAnswer: "Быстрое прочтение для общего понимания",
        hint: "Вспомни определение из урока про 1. Skimming (Просмотровое чтение):"
      },
      {
        type: 'quiz',
        question: "Что такое 2. Scanning (Поисковое чтение):?",
        options: ["Специальный метод вычисления", "Это понятие из другого раздела", "Понятие, обратное данному", "Вспомогательный термин", "Поиск конкретной информации"],
        correctAnswer: "Поиск конкретной информации",
        hint: "Вспомни определение из урока про 2. Scanning (Поисковое чтение):"
      },
      {
        type: 'quiz',
        question: "Что такое 3. Detailed Reading (Изучающее чтение):?",
        options: ["Внимательное чтение всего текста", "Понятие, обратное данному", "Специальный метод вычисления", "Вспомогательный термин", "Это понятие из другого раздела"],
        correctAnswer: "Внимательное чтение всего текста",
        hint: "Вспомни определение из урока про 3. Detailed Reading (Изучающее чтение):"
      },
      {
        type: 'quiz',
        question: "Что такое Структура текста:?",
        options: ["Вспомогательный термин", "Это понятие из другого раздела", "Introduction (введение) — главная идея", "Понятие, обратное данному", "Специальный метод вычисления"],
        correctAnswer: "Introduction (введение) — главная идея",
        hint: "Вспомни определение из урока про Структура текста:"
      },
      {
        type: 'quiz',
        question: "Что такое При чтении обращайте внимание на:?",
        options: ["Вспомогательный термин", "Title — заголовок", "Специальный метод вычисления", "Понятие, обратное данному", "Это понятие из другого раздела"],
        correctAnswer: "Title — заголовок",
        hint: "Вспомни определение из урока про При чтении обращайте внимание на:"
      },
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь тему! 🎉" }
  }
]
