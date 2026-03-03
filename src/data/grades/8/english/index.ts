import { SubjectData, GameLesson } from '@/data/types'

const L = (title: string, description: string, tasks: string[], image?: string, content?: string, examples?: string[], facts?: string[]) => ({
  title, description, tasks, image, content, examples, facts
})

export const lessons: SubjectData = {
  title: "Английский язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: ["Грамматика", "Лексика", "Говорение", "Чтение"],
  detailedTopics: [
    {
      topic: "Времена глагола",
      lessons: [
        L("Урок 1: Present Perfect", "Настоящее совершённое время.", [
          "Изучить образование времени",
          "Понять употребление",
          "Выучить маркеры",
          "Отработать упражнения"
        ], "/school-curriculum-app/images/lessons/english/present-perfect.png",
        "**Present Perfect** — настоящее совершённое время.\n\n---\n\n**Образование:**\n\n| Утверждение | have/has + V3 |\n|-------------|----------------|\n| I have visited | Я посетил |\n| She has seen | Она видела |\n| They have done | Они сделали |\n\n| Отрицание | have/has not + V3 |\n|-----------|-------------------|\n| I have not (haven't) visited | Я не посетил |\n\n| Вопрос | Have/Has + подлежащее + V3? |\n|--------|------------------------------|\n| Have you visited? | Ты посетил? |\n\n---\n\n**Маркеры времени:**\n\n| Маркер | Значение | Пример |\n|--------|----------|--------|\n| ever | когда-либо | Have you ever been to London? |\n| never | никогда | I have never seen this film |\n| already | уже | She has already finished |\n| yet | ещё (в отрицании и вопросе) | I haven't done it yet |\n| just | только что | He has just arrived |\n| for | в течение | I have lived here for 5 years |\n| since | с тех пор как | She has known him since 2010 |\n\n---\n\n**Употребление:**\n1. Действие завершено, результат важен в настоящем\n2. Жизненный опыт\n3. Действие началось в прошлом и продолжается",
        ["have/has + V3", "Результат важен в настоящем", "Маркеры: ever, never, already, yet, just"],
        ["Present Perfect связывает прошлое с настоящим", "В американском английском Past Simple используется чаще", "Самое употребительное время в английском"]),
        L("Урок 2: Past Simple vs Present Perfect", "Различие времён.", [
          "Понять различие",
          "Изучить маркеры каждого времени",
          "Отработать упражнения",
          "Выбрать правильное время"
        ], "/school-curriculum-app/images/lessons/english/past-perfect-compare.png",
        "**Past Simple vs Present Perfect** — важное различие.\n\n---\n\n**Past Simple:**\n\n| Характеристика | Описание |\n|----------------|----------|\n| Время действия | Конкретное время в прошлом |\n| Маркеры | yesterday, last week, in 2010, ago |\n| Фокус | КОГДА произошло |\n\n**Present Perfect:**\n\n| Характеристика | Описание |\n|----------------|----------|\n| Время действия | Не важно когда |\n| Маркеры | ever, never, just, yet, already |\n| Фокус | РЕЗУЛЬТАТ |\n\n---\n\n**Сравнение:**\n\n| Past Simple | Present Perfect |\n|-------------|-----------------|\n| I visited Paris last year. | I have visited Paris. |\n| (Важно КОГДА — в прошлом году) | (Важно, что БЫЛ там) |\n| She wrote a letter yesterday. | She has written a letter. |\n| He lost his key last week. | He has lost his key. (Не может войти сейчас) |\n\n---\n\n**Правило выбора:**\n\n```\nЕсть точное время (yesterday, last...)?\n    ↓ Да → Past Simple\n    ↓ Нет\nЕсть маркер Present Perfect (ever, just...)?\n    ↓ Да → Present Perfect\n    ↓ Нет\nВажен результат в настоящем?\n    ↓ Да → Present Perfect\n    ↓ Нет → Past Simple\n```",
        ["Past Simple — точное время в прошлом", "Present Perfect — результат в настоящем", "С маркером yesterday — всегда Past Simple"],
        ["Носители часто используют Past Simple вместо Present Perfect", "Британский английск в Present Perfect чаще американского", "С for/since можно использовать Present Perfect"]),
        L("Урок 3: Present Perfect Continuous", "Длительное совершённое.", [
          "Изучить образование",
          "Понять употребление",
          "Сравнить с Present Perfect",
          "Отработать упражнения"
        ], "/school-curriculum-app/images/lessons/english/perfect-continuous.png",
        "**Present Perfect Continuous** — совершённое длительное.\n\n---\n\n**Образование:**\n\nhave/has + been + V-ing\n\n| Утверждение | Пример |\n|-------------|--------|\n| I have been waiting | Я жду (уже какое-то время) |\n| She has been working | Она работает (уже какое-то время) |\n\n---\n\n**Употребление:**\n\n| Случай | Пример |\n|---------|--------|\n| Действие длилось и продолжается | I have been reading for 2 hours |\n| Действие только что закончилось с видимым результатом | Your eyes are red. Have you been crying? |\n\n---\n\n**Маркеры:**\n\n| Маркер | Пример |\n|--------|--------|\n| for 2 hours | I have been sleeping for 2 hours |\n| since morning | She has been working since morning |\n| all day | They have been playing all day |\n| how long | How long have you been waiting? |\n\n---\n\n**Present Perfect vs Present Perfect Continuous:**\n\n| Present Perfect | Present Perfect Continuous |\n|-----------------|---------------------------|\n| Результат важен | Процесс важен |\n| I have painted the room. (Готово) | I have been painting the room. (Процесс) |\n| I have written 3 letters. | I have been writing letters. |",
        ["have/has + been + V-ing", "Акцент на длительности процесса", "for/since — типичные маркеры"],
        ["Continuous подчёркивает процесс", "Perfect Continuous — редкое время", "В разговоре часто заменяется на Present Perfect"]),
        L("Урок 4: Past Perfect", "Прошедшее совершённое.", [
          "Изучить образование",
          "Понять употребление",
          "Сравнить с Past Simple",
          "Отработать упражнения"
        ], "/school-curriculum-app/images/lessons/english/past-perfect.png",
        "**Past Perfect** — прошедшее совершённое время.\n\n---\n\n**Образование:**\n\nhad + V3\n\n| Форма | Пример |\n|-------|--------|\n| Утверждение | I had finished before you came |\n| Отрицание | I had not (hadn't) finished |\n| Вопрос | Had you finished before he came? |\n\n---\n\n**Употребление:**\n\nДействие, которое произошло ДО другого действия в прошлом.\n\n```\nВчера:\n1. Я закончил работу (раньше) → Past Perfect\n2. Ты пришёл (позже) → Past Simple\n```\n\n**Примеры:**\n\n- When I arrived, she had already left.\n- By the time he called, I had finished dinner.\n- I realized that I had forgotten my keys.\n\n---\n\n**Маркеры:**\n\n| Маркер | Пример |\n|--------|--------|\n| by the time | By the time we arrived, they had left |\n| before | I had seen him before you mentioned him |\n| after | After she had finished, she went home |\n| already | He had already eaten when we came |\n\n---\n\n**Порядок действий:**\n\n| Время | Действие |\n|-------|----------|\n| Past Perfect | То, что было раньше |\n| Past Simple | То, что было позже |",
        ["had + V3", "Действие ДО другого прошлого действия", "by the time, before, after — маркеры"],
        ["Past Perfect — «предпрошедшее» время", "Используется в косвенной речи", "Without Past Perfect история была бы непонятна"])
      ]
    },
    {
      topic: "Модальные глаголы",
      lessons: [
        L("Урок 5: Модальные глаголы: can, could, be able to", "Способность и возможность.", [
          "Изучить can/could",
          "Понять be able to",
          "Отработать употребление",
          "Сравнить формы"
        ], "/school-curriculum-app/images/lessons/english/modal-can.png",
        "**Can, could, be able to** — способность и возможность.\n\n---\n\n**Can:**\n\n| Значение | Пример |\n|----------|--------|\n| Способность (физическая, умственная) | I can swim |\n| Возможность | You can buy it here |\n| Просьба (неформальная) | Can you help me? |\n| Разрешение | You can go now |\n\n**Could:**\n\n| Значение | Пример |\n|----------|--------|\n| Способность в прошлом | I could swim when I was 5 |\n| Вежливая просьба | Could you help me, please? |\n| Возможность (менее уверенно) | It could be true |\n\n**Be able to:**\n\n| Значение | Пример |\n|----------|--------|\n| Способность (любое время) | I will be able to come tomorrow |\n| Достигнутая способность | I was able to pass the exam |\n\n---\n\n**Сравнение:**\n\n| Форма | Время | Пример |\n|-------|-------|--------|\n| can | Настоящее | I can help you |\n| could | Прошедшее / Вежливость | I could help you |\n| be able to | Любое | I will be able to help you |\n\n---\n\n**Could vs Was able to:**\n\n- I could swim — умел плавать (общая способность)\n- I was able to swim across the river — смог переплыть (конкретный случай)",
        ["can — способность сейчас", "could — способность в прошлом или вежливость", "be able to — для будущего времени"],
        ["Can — самый частый модальный глагол", "Could бы вежливее can", "Be able to — не модальный, но похож"]),
        L("Урок 6: Модальные глаголы: must, have to, should", "Обязанность и совет.", [
          "Изучить must/have to",
          "Понять should",
          "Сравнить значения",
          "Отработать упражнения"
        ], "/school-curriculum-app/images/lessons/english/modal-must.png",
        "**Must, have to, should** — обязанность, необходимость, совет.\n\n---\n\n**Must:**\n\n| Значение | Пример |\n|----------|--------|\n| Внутренняя обязанность | I must study harder |\n| Уверенное предположение | She must be tired |\n| Сильный совет | You must see this film |\n\n**Have to:**\n\n| Значение | Пример |\n|----------|--------|\n| Внешняя обязанность | I have to go to school |\n| Необходимость | You have to wear a uniform |\n\n**Should:**\n\n| Значение | Пример |\n|----------|--------|\n| Совет | You should rest more |\n| Ожидание | She should be here by now |\n\n---\n\n**Сравнение:**\n\n| Глагол | Тип обязанности | Пример |\n|--------|-----------------|--------|\n| must | Внутренняя, личная | I must lose weight (решил сам) |\n| have to | Внешняя, вынужденная | I have to work (работа требует) |\n| should | Совет, рекомендация | You should see a doctor |\n\n---\n\n**Отрицание:**\n\n| Форма | Значение | Пример |\n|-------|----------|--------|\n| mustn't | Запрещение | You mustn't smoke here |\n| don't have to | Не обязательно | You don't have to come (можешь не приходить) |\n| shouldn't | Не стоит | You shouldn't eat so much |",
        ["must — личная обязанность", "have to — вынужденная необходимость", "should — совет"],
        ["Mustn't ≠ don't have to — это разные значения!", "Have to можно в любом времени", "Should — более мягкий совет чем must"]),
        L("Урок 7: Модальные глаголы: may, might", "Возможность и разрешение.", [
          "Изучить may/might",
          "Понять различие",
          "Изучить формы просьбы",
          "Отработать упражнения"
        ], "/school-curriculum-app/images/lessons/english/modal-may.png",
        "**May, might** — возможность и разрешение.\n\n---\n\n**May:**\n\n| Значение | Пример |\n|----------|--------|\n| Возможность (высокая) | It may rain today |\n| Разрешение (формальное) | May I come in? |\n| Пожелание | May you be happy! |\n\n**Might:**\n\n| Значение | Пример |\n|----------|--------|\n| Возможность (низкая) | It might rain (но вряд ли) |\n| Вежливая просьба | Might I ask a question? |\n| Could have + V3 в прошедшем | He might have missed the bus |\n\n---\n\n**Степень уверенности:**\n\n```\nОпределённо ← ─ ─ ─ ─ ─ ─ ─ → Маловероятно\n   must       may      might      could\n  (100%)     (50%)     (30%)      (20%)\n```\n\n---\n\n**Сравнение:**\n\n| May | Might |\n|-----|-------|\n| Высокая вероятность | Низкая вероятность |\n| Более формальное | Менее формальное |\n| It may rain (похоже на дождь) | It might rain (может и пойти) |\n\n---\n\n**May vs Can для разрешения:**\n\n| Глагол | Тон | Пример |\n|--------|-----|--------|\n| Can | Нейтральный | Can I open the window? |\n| May | Формальный | May I open the window? |\n| Could | Вежливый | Could I open the window? |",
        ["may — высокая вероятность", "might — низкая вероятность", "May I — формальная просьба"],
        ["May — самый формальный модальный глагол", "Might — прошедшая форма may исторически", "В разговоре may и might взаимозаменяемы"]),
        L("Урок 8: Conditionals (Условные предложения)", "Типы условных предложений.", [
          "Изучить 4 типа условий",
          "Понять структуру каждого",
          "Выучить маркеры",
          "Отработать упражнения"
        ], "/school-curriculum-app/images/lessons/english/conditionals.png",
        "**Conditionals** — условные предложения.\n\n---\n\n**Zero Conditional (реальное условие):**\n\nIf + Present Simple, Present Simple\n\n| Пример | Значение |\n|--------|----------|\n| If you heat water to 100°C, it boils. | Закономерность |\n| If I'm tired, I go to bed. | Привычка |\n\n---\n\n**First Conditional (реальное будущее):**\n\nIf + Present Simple, will + V\n\n| Пример | Значение |\n|--------|----------|\n| If it rains, I will stay at home. | Реальное будущее |\n| If you study hard, you will pass the exam. | Возможное условие |\n\n---\n\n**Second Conditional (нереальное настоящее):**\n\nIf + Past Simple, would + V\n\n| Пример | Значение |\n|--------|----------|\n| If I had money, I would buy a car. | Нереальное желание |\n| If I were you, I would accept. | Совет |\n\n---\n\n**Third Conditional (нереальное прошлое):**\n\nIf + Past Perfect, would have + V3\n\n| Пример | Значение |\n|--------|----------|\n| If I had studied, I would have passed. | Сожаление о прошлом |\n\n---\n\n**Таблица Conditionals:**\n\n| Тип | If-часть | Главная часть | Значение |\n|-----|----------|---------------|----------|\n| 0 | Present | Present | Всегда правда |\n| 1 | Present | will + V | Реальное будущее |\n| 2 | Past | would + V | Нереальное настоящее |\n| 3 | Past Perfect | would have + V3 | Нереальное прошлое |",
        ["0 тип — законы и факты", "1 тип — реальное будущее", "2 тип — мечты и советы", "3 тип — сожаления"],
        ["If I were you — стандартный совет", "Could/might вместо would — возможно", "Смешанные Conditionals существуют"])
      ]
    },
    {
      topic: "Косвенная речь",
      lessons: [
        L("Урок 9: Reported Speech (Косвенная речь)", "Передача чужих слов.", [
          "Изучить правила согласования времён",
          "Понять изменения местоимений",
          "Изучить изменения наречий",
          "Отработать упражнения"
        ], "/school-curriculum-app/images/lessons/english/reported-speech.png",
        "**Reported Speech** — косвенная речь.\n\n---\n\n**Согласование времён:**\n\nПри передаче чужих слов времена сдвигаются назад.\n\n| Прямая речь | Косвенная речь |\n|-------------|----------------|\n| Present Simple | Past Simple |\n| Present Continuous | Past Continuous |\n| Present Perfect | Past Perfect |\n| Past Simple | Past Perfect |\n| will | would |\n| can | could |\n| must | had to |\n\n---\n\n**Примеры:**\n\n| Прямая речь | Косвенная речь |\n|-------------|----------------|\n| «I like music» | He said he liked music |\n| «I am working» | She said she was working |\n| «I have finished» | He said he had finished |\n| «I will come» | She said she would come |\n\n---\n\n**Изменение местоимений:**\n\n| Прямая речь | Косвенная речь |\n|-------------|----------------|\n| I | he/she |\n| my | his/her |\n| me | him/her |\n| we | they |\n| our | their |\n\n---\n\n**Изменение наречий времени и места:**\n\n| Прямая речь | Косвенная речь |\n|-------------|----------------|\n| now | then |\n| today | that day |\n| yesterday | the day before |\n| tomorrow | the next day |\n| here | there |\n| this | that |",
        ["Времена сдвигаются назад", "Местоимения меняются", "Наречия времени и места меняются"],
        ["«Tell me» не требует согласования", "Настоящие факты не меняют время", "Согласование — особенность английского"]),
        L("Урок 10: Reported Questions", "Косвенные вопросы.", [
          "Изучить структуру косвенных вопросов",
          "Понять изменения порядка слов",
          "Отработать Yes/No вопросы",
          "Отработать Wh-вопросы"
        ], "/school-curriculum-app/images/lessons/english/reported-questions.png",
        "**Reported Questions** — косвенные вопросы.\n\n---\n\n**Правила:**\n\n1. Прямой порядок слов (как в утверждении)\n2. Нет вспомогательных do/does/did\n3. Согласование времён\n\n---\n\n**Yes/No вопросы:**\n\nИспользуется if или whether.\n\n| Прямой вопрос | Косвенный вопрос |\n|---------------|------------------|\n| «Do you like coffee?» | He asked if I liked coffee |\n| «Are you busy?» | She asked if I was busy |\n| «Have you seen this film?» | He asked whether I had seen that film |\n\n---\n\n**Wh-вопросы:**\n\nВопросительное слово сохраняется.\n\n| Прямой вопрос | Косвенный вопрос |\n|---------------|------------------|\n| «What is your name?» | He asked what my name was |\n| «Where do you live?» | She asked where I lived |\n| «When will you come?» | He asked when I would come |\n\n---\n\n**Сравнение:**\n\n| Прямой вопрос | Порядок слов | Косвенный вопрос |\n|---------------|--------------|------------------|\n| Where do you live? | Обратный | where I lived (прямой) |\n| What is he doing? | Обратный | what he was doing (прямой) |\n| Why did she leave? | Обратный | why she had left (прямой) |",
        ["Прямой порядок слов в косвенных вопросах", "if/whether для Yes/No вопросов", "Wh-слова сохраняются"],
        ["Косвенные вопросы — это не вопросы!", "Точка в конце, не вопросительный знак", "Polite requests используют косвенную форму"]),
        L("Урок 11: Passive Voice (Страдательный залог)", "Пассивные конструкции.", [
          "Изучить образование пассива",
          "Понять употребление",
          "Изучить пассив в разных временах",
          "Отработать упражнения"
        ], "/school-curriculum-app/images/lessons/english/passive.png",
        "**Passive Voice** — страдательный залог.\n\n---\n\n**Образование:**\n\nbe + V3 (3-я форма глагола)\n\n| Залог | Фокус |\n|-------|--------|\n| Active (активный) | Кто делает действие |\n| Passive (пассивный) | Что подвергается действию |\n\n---\n\n**Сравнение:**\n\n| Active | Passive |\n|--------|----------|\n| Someone stole my car. | My car was stolen. |\n| They built this house in 1900. | This house was built in 1900. |\n| Shakespeare wrote Hamlet. | Hamlet was written by Shakespeare. |\n\n---\n\n**Passive в разных временах:**\n\n| Время | Формула | Пример |\n|-------|---------|--------|\n| Present Simple | am/is/are + V3 | English is spoken here |\n| Past Simple | was/were + V3 | The book was written in 1990 |\n| Present Perfect | have/has been + V3 | The work has been finished |\n| Future Simple | will be + V3 | The letter will be sent tomorrow |\n| Present Continuous | am/is/are being + V3 | The house is being built |\n\n---\n\n**Когда используем Passive:**\n\n1. Не знаем, кто сделал\n2. Неважно, кто сделал\n3. Официальный стиль",
        ["be + V3", "Фокус на объекте действия", "by + агент — кто сделал"],
        ["В английском пассив используется чаще чем в русском", "The book was given to me - типичный пассив", "Get + V3 - разговорный пассив"]),
        L("Урок 12: Итоговое повторение", "Грамматика 8 класс.", [
          "Повторить времена",
          "Повторить модальные глаголы",
          "Повторить косвенную речь",
          "Повторить пассив"
        ], "/school-curriculum-app/images/lessons/english/review-8.png",
        "**Итоговое повторение грамматики 8 класса.**\n\n---\n\n**Времена:**\n\n| Время | Формула | Маркеры |\n|-------|---------|----------|\n| Present Perfect | have/has + V3 | ever, never, just, yet, already |\n| Present Perfect Continuous | have/has been + V-ing | for, since |\n| Past Perfect | had + V3 | by the time, before, after |\n\n---\n\n**Модальные глаголы:**\n\n| Глагол | Значение |\n|--------|----------|\n| can/could | Способность, возможность |\n| must | Обязанность (личная) |\n| have to | Необходимость (внешняя) |\n| should | Совет |\n| may/might | Возможность, разрешение |\n\n---\n\n**Conditionals:**\n\n| Тип | If-часть | Главная часть |\n|-----|----------|---------------|\n| 0 | Present | Present |\n| 1 | Present | will + V |\n| 2 | Past | would + V |\n| 3 | Past Perfect | would have + V3 |\n\n---\n\n**Reported Speech:**\n\n- Согласование времён (сдвиг назад)\n- Изменение местоимений\n- Изменение наречий\n\n---\n\n**Passive Voice:**\n\nbe + V3",
        ["Времена системы Perfect", "Модальные глаголы", "Условные предложения", "Косвенная речь", "Страдательный залог"],
        ["Грамматика — фундамент языка", "Практика важнее правил", "Читайте на английском!"])
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
  },
  {
    title: "Modal Verbs",
    subject: "Английский язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Must — это:", options: ["Совет", "Личная обязанность", "Возможность", "Запрет"], correctAnswer: "Личная обязанность", hint: "Внутренняя необходимость" },
      { type: 'quiz', question: "You __ smoke here. (запрет)", options: ["mustn't", "don't have to", "shouldn't", "needn't"], correctAnswer: "mustn't", hint: "Строгий запрет" },
      { type: 'fill', question: "You __ see a doctor. (совет)", correctAnswer: "should", hint: "Рекомендация" },
      { type: 'quiz', question: "Can vs Could для просьбы:", options: ["Can вежливее", "Could вежливее", "Одинаково", "Could только в прошедшем"], correctAnswer: "Could вежливее", hint: "Could — более формально" }
    ],
    reward: { stars: 3, message: "Excellent! You know modal verbs! 🌟" }
  },
  {
    title: "Conditionals & Passive",
    subject: "Английский язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "First Conditional: If it rains, I __ at home.", options: ["stay", "will stay", "would stay", "stayed"], correctAnswer: "will stay", hint: "Реальное будущее условие" },
      { type: 'quiz', question: "Second Conditional: If I __ you, I would accept.", options: ["am", "was", "were", "be"], correctAnswer: "were", hint: "Сослагательное наклонение" },
      { type: 'fill', question: "Passive: The book __ written by Pushkin. (Past)", correctAnswer: "was", hint: "be + V3" },
      { type: 'quiz', question: "Active: They built it. → Passive:", options: ["It built.", "It was built.", "It is built.", "It has built."], correctAnswer: "It was built.", hint: "Past Simple Passive" }
    ],
    reward: { stars: 3, message: "Wonderful! You know conditionals and passive! 🏆" }
  }
]
