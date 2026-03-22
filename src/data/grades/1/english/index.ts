import { SubjectData, GameLesson } from '@/data/types'

const createLesson = (
  title: string,
  description: string,
  tasks: string[],
  examples?: string[],
  facts?: string[]
) => ({
  title,
  description,
  tasks,
  ...(examples && { examples }),
  ...(facts && { facts })
})

export const lessons: SubjectData = {
  title: "Иностранный язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: ["Приветствие", "Представление", "Цвета", "Числа 1-10", "Семья", "Животные"],
  detailedTopics: [
    {
      topic: "Знакомство",
      lessons: [
        createLesson(
          "Урок 1: 👋 Hello! Привет!",
          `## 👋 Приветствия на английском языке

Сегодня мы научимся здороваться по-английски! Это самые важные слова для начала разговора.

### Главные слова

**Hello!** [хэ-ло́у] — Здравствуйте! Привет!
Это самое распространённое приветствие. Можно использовать в любой ситуации.

**Hi!** [хай] — Привет!
Это более дружеское приветствие. Используется с друзьями.

**Good morning!** [гуд мо́рнинг] — Доброе утро!
Используется до 12 часов дня.

**Good afternoon!** [гуд а́фтерну́н] — Добрый день!
Используется с 12 до 18 часов.

**Good evening!** [гуд и́внинг] — Добрый вечер!
Используется после 18 часов.

### Диалог-знакомство

**What is your name?** — Как тебя зовут?
**My name is...** — Меня зовут...

— Hello! My name is Tom. What is your name?
— Hello! My name is Ann.`,
          [
            "Научиться говорить Hello! и Hi!",
            "Ответить на приветствие учителя",
            "Разыграть диалог знакомства",
            "Поприветствовать одноклассника"
          ],
          [
            "Hello! — Привет! (формально)",
            "Hi! — Привет! (дружески)",
            "Good morning! — Доброе утро!"
          ],
          [
            "Hello — самое популярное приветствие в мире.",
            "Hi — короткое приветствие для друзей.",
            "Англичане здороваются даже с незнакомцами."
          ]
        ),
        createLesson(
          "Урок 2: ❓ What is your name? Как тебя зовут?",
          `## ❓ Учимся представляться

Сегодня мы научимся спрашивать имя и представляться по-английски!

### Главные фразы

**What is your name?** [уот из ё нейм?] — Как тебя зовут?
Используется, когда хотим узнать имя собеседника.

**My name is...** [май нейм из...] — Меня зовут...
Используется, чтобы назвать своё имя.

**I am...** [ай эм...] — Я...
Более короткий способ представиться.

**Nice to meet you!** [найс ту ми́т ю] — Приятно познакомиться!
Говорят после знакомства.

### Примеры диалогов

— Hello! What is your name?
— My name is Tom. What is your name?
— My name is Ann. Nice to meet you!
— Nice to meet you too!

### Популярные английские имена

**Мальчики:** Tom, Mike, John, David, Nick
**Девочки:** Ann, Kate, Mary, Emma, Lisa`,
          [
            "Спросить имя у соседа по парте",
            "Ответить: My name is...",
            "Выучить 3 английских имени",
            "Написать своё имя по-английски"
          ],
          [
            "What is your name? — Как тебя зовут?",
            "My name is Tom. — Меня зовут Том.",
            "Nice to meet you! — Приятно познакомиться!"
          ],
          [
            "Английские имена пишутся с большой буквы.",
            "Tom, Ann, Mike — популярные имена.",
            "Nice to meet you! говорят после знакомства."
          ]
        ),
        createLesson(
          "Урок 3: 👋 Goodbye! До свидания!",
          `## 👋 Прощаемся по-английски

Мы научились здороваться и знакомиться. Теперь научимся прощаться!

### Главные фразы прощания

**Goodbye!** [гуд-ба́й] — До свидания!
Самое распространённое прощание. Подходит для любой ситуации.

**Bye!** [бай] — Пока!
Короткое, неформальное прощание. Используется с друзьями.

**Bye-bye!** [бай-бай] — Пока-пока!
Очень дружеское, обычно говорят детям.

**See you!** [си ю] — Увидимся!
Неформальное прощание, означает «до встречи».

**Good night!** [гуд найт] — Спокойной ночи!
Говорят только перед сном.

### Диалоги прощания

— Goodbye, Ann!
— Goodbye, Tom!

— Bye, Mike! See you!
— Bye, Kate!`,
          [
            "Научиться говорить Goodbye! и Bye!",
            "Ответить на прощание учителя",
            "Выучить песенку прощания",
            "Разыграть диалог прощания"
          ],
          [
            "Goodbye! — До свидания! (формально)",
            "Bye! — Пока! (дружески)",
            "Good night! — Спокойной ночи!"
          ],
          [
            "Goodbye — самое популярное прощание.",
            "Bye — короткое прощание для друзей.",
            "Good night говорят только перед сном."
          ]
        )
      ]
    },
    {
      topic: "Цвета и числа",
      lessons: [
        createLesson(
          "Урок 4: 🎨 Colours — Цвета",
          `## 🎨 Цвета по-английски

Сегодня выучим названия цветов! Это очень полезные слова.

### Основные цвета

**Red** [ред] — красный
Apple is red. — Яблоко красное.

**Blue** [блу] — синий
Sky is blue. — Небо синее.

**Green** [грин] — зелёный
Grass is green. — Трава зелёная.

**Yellow** [йе́ллоу] — жёлтый
Sun is yellow. — Солнце жёлтое.

**Orange** [о́риндж] — оранжевый
Orange is orange. — Апельсин оранжевый.

**Purple** [пёпл] — фиолетовый
Grape is purple. — Виноград фиолетовый.

**Pink** [пинк] — розовый
Flower is pink. — Цветок розовый.

**Black** [блэк] — чёрный
Cat is black. — Кошка чёрная.

**White** [уа́йт] — белый
Snow is white. — Снег белый.

### Вопрос о цвете

**What colour is it?** — Какого это цвета?
**It is red.** — Это красное.`,
          [
            "Выучить 5 цветов: red, blue, green, yellow, orange",
            "Показать предметы разных цветов",
            "Назвать цвет по-английски",
            "Раскрасить картинку и назвать цвета"
          ],
          [
            "Red — красный (яблоко)",
            "Blue — синий (небо)",
            "Green — зелёный (трава)"
          ],
          [
            "Colour (брит.) = Color (амер.).",
            "Синий — самый популярный цвет в мире.",
            "В радуге 7 цветов по-английски."
          ]
        ),
        createLesson(
          "Урок 5: 🔢 Numbers 1-5 — Числа от 1 до 5",
          `## 🔢 Считаем по-английски от 1 до 5

Сегодня мы научимся считать по-английски! Это очень полезно.

### Числа от 1 до 5

**One** [уан] — один 1
One cat — одна кошка

**Two** [ту] — два 2
Two dogs — две собаки

**Three** [сри] — три 3
Three apples — три яблока

**Four** [фо] — четыре 4
Four books — четыре книги

**Five** [файв] — пять 5
Five pens — пять ручек

### Считаем предметы

**How many?** — Сколько?

— How many cats?
— One, two, three! Three cats!

### Потешка для запоминания

One, two, three,
Look at me!
Four, five,
I can dive!

### Показываем пальцы

One — 1 палец
Two — 2 пальца
Three — 3 пальца
Four — 4 пальца
Five — 5 пальцев`,
          [
            "Выучить: one, two, three, four, five",
            "Посчитать предметы в классе",
            "Показать пальцами числа 1-5",
            "Написать числа словами"
          ],
          [
            "One apple — одно яблоко",
            "Two cats — две кошки",
            "Three books — три книги"
          ],
          [
            "One, two, three — первые три числа.",
            "Пальцы помогают запомнить числа.",
            "В основе счёта — 10 пальцев."
          ]
        ),
        createLesson(
          "Урок 6: 🔢 Numbers 6-10 — Числа от 6 до 10",
          `## 🔢 Считаем по-английски от 6 до 10

Продолжаем учить числа! Теперь от 6 до 10.

### Числа от 6 до 10

**Six** [сикс] — шесть 6
Six flowers — шесть цветов

**Seven** [се́вн] — семь 7
Seven days — семь дней

**Eight** [эйт] — восемь 8
Eight legs — восемь лап

**Nine** [найн] — девять 9
Nine birds — девять птиц

**Ten** [тен] — десять 10
Ten fingers — десять пальцев

### Считаем до 10

One, two, three, four, five,
Six, seven, eight, nine, ten!

### Полезные фразы

**How old are you?** — Сколько тебе лет?
**I am seven.** — Мне семь лет.

### Скороговорка

One, two, three, four, five,
Once I caught a fish alive!
Six, seven, eight, nine, ten,
Then I let it go again!`,
          [
            "Выучить: six, seven, eight, nine, ten",
            "Посчитать от 1 до 10",
            "Назвать свой возраст",
            "Решить примеры: 2+3, 5+5"
          ],
          [
            "Six — шесть (6)",
            "Seven — семь (7)",
            "Ten — десять (10)"
          ],
          [
            "Seven — счастливое число.",
            "Ten — основа счёта.",
            "В неделе 7 дней."
          ]
        )
      ]
    },
    {
      topic: "Животные",
      lessons: [
        createLesson(
          "Урок 7: 🐱 Animals — Животные",
          `## 🐱 Животные по-английски

Сегодня выучим названия животных! Это очень интересная тема.

### Домашние животные

**Cat** [кэт] — кошка
I have a cat. — У меня есть кошка.

**Dog** [дог] — собака
My dog is big. — Моя собака большая.

**Fish** [фиш] — рыба
Fish can swim. — Рыба умеет плавать.

**Bird** [бёрд] — птица
Bird can fly. — Птица умеет летать.

**Rabbit** [ре́бит] — кролик
Rabbit is white. — Кролик белый.

### Дикие животные

**Bear** [беар] — медведь
Bear is big. — Медведь большой.

**Fox** [фокс] — лиса
Fox is red. — Лиса рыжая.

**Wolf** [вулф] — волк
Wolf is grey. — Волк серый.

**Tiger** [та́йгер] — тигр
Tiger is orange. — Тигр оранжевый.

**Lion** [ла́йен] — лев
Lion is strong. — Лев сильный.

### Вопрос о животных

**What is this?** — Что это?
— What is this?
— It is a cat.`,
          [
            "Выучить 5 животных: cat, dog, fish, bird, bear",
            "Назвать животное по картинке",
            "Сказать, какого цвета животное",
            "Нарисовать и подписать животное"
          ],
          [
            "Cat — кошка",
            "Dog — собака",
            "Bear — медведь"
          ],
          [
            "Cat и кот звучат похоже.",
            "Dog — самое популярное домашнее животное.",
            "В Австралии живут кенгуру и коалы."
          ]
        )
      ]
    }
  ]
}

export const games: GameLesson[] = [
  {
    title: "Hello! Привет!",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Как сказать «Привет» по-английски?",
        options: ["Goodbye", "Hello", "Thanks"],
        correctAnswer: "Hello",
        hint: "Это самое популярное приветствие"
      },
      {
        type: 'quiz',
        question: "Как ещё можно поздороваться?",
        options: ["Hi", "Bye", "No"],
        correctAnswer: "Hi",
        hint: "Это короткое приветствие"
      },
      {
        type: 'find',
        question: "Выбери приветствия:",
        options: ["Hello", "Hi", "Goodbye", "Bye", "Thanks"],
        correctAnswer: ["Hello", "Hi"],
        hint: "Приветствия = Greetings"
      },
      {
        type: 'quiz',
        question: "Что говорят утром?",
        options: ["Good morning", "Good night", "Goodbye"],
        correctAnswer: "Good morning",
        hint: "Morning = утро"
      }
    ],
    reward: { stars: 3, message: "Great! Отлично! Ты знаешь приветствия! 👋" }
  },
  {
    title: "Цвета по-английски 🎨",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Red - это какой цвет?",
        options: ["Синий", "Красный", "Зелёный"],
        correctAnswer: "Красный",
        hint: "Red = Красный"
      },
      {
        type: 'quiz',
        question: "Как будет «синий» по-английски?",
        options: ["Red", "Blue", "Green"],
        correctAnswer: "Blue",
        hint: "Blue = Синий"
      },
      {
        type: 'find',
        question: "Выбери названия цветов:",
        options: ["Red", "Cat", "Blue", "Dog", "Green", "Yellow"],
        correctAnswer: ["Red", "Blue", "Green", "Yellow"],
        hint: "Colours = Цвета"
      },
      {
        type: 'quiz',
        question: "Какого цвета трава?",
        options: ["Red", "Blue", "Green"],
        correctAnswer: "Green",
        hint: "Трава зелёная"
      }
    ],
    reward: { stars: 3, message: "Wonderful! Ты знаешь цвета! 🎨" }
  },
  {
    title: "Числа 1-10 🔢",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "One - это какое число?",
        options: ["Один", "Два", "Три"],
        correctAnswer: "Один",
        hint: "One = 1"
      },
      {
        type: 'quiz',
        question: "Как будет «пять» по-английски?",
        options: ["Three", "Four", "Five"],
        correctAnswer: "Five",
        hint: "Five = 5"
      },
      {
        type: 'quiz',
        question: "Ten - это?",
        options: ["9", "10", "8"],
        correctAnswer: "10",
        hint: "Ten = 10"
      },
      {
        type: 'quiz',
        question: "Как будет «семь» по-английски?",
        options: ["Six", "Seven", "Eight"],
        correctAnswer: "Seven",
        hint: "Seven = 7"
      }
    ],
    reward: { stars: 3, message: "Excellent! Ты знаешь числа! 🔢" }
  },
  {
    title: "Животные 🐱🐕",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Cat - это?",
        options: ["Собака", "Кошка", "Птица"],
        correctAnswer: "Кошка",
        hint: "Cat = Кошка"
      },
      {
        type: 'quiz',
        question: "Как будет «собака» по-английски?",
        options: ["Cat", "Dog", "Bird"],
        correctAnswer: "Dog",
        hint: "Dog = Собака"
      },
      {
        type: 'find',
        question: "Выбери названия животных:",
        options: ["Cat", "Red", "Dog", "Blue", "Bird", "Fish"],
        correctAnswer: ["Cat", "Dog", "Bird", "Fish"],
        hint: "Animals = Животные"
      },
      {
        type: 'quiz',
        question: "Bear - это?",
        options: ["Лиса", "Медведь", "Волк"],
        correctAnswer: "Медведь",
        hint: "Bear — большой и бурый"
      }
    ],
    reward: { stars: 3, message: "Great job! Ты знаешь животных! 🐱" }
  }
]
