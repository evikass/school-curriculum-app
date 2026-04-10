import { SubjectData, GameLesson } from '@/data/types'

export const lessons: SubjectData = {
  title: "Иностранный язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: ["Приветствие", "Представление", "Цвета", "Числа 1-10", "Семья", "Животные"],
  detailedTopics: [
    {
      topic: "Знакомство",
      lessons: [
        {
          title: "Урок 1: Hello! 👋",
          image: "/school-curriculum-app/images/lessons/grade1/english/lesson1-hello.svg",
          description: `**Приветствия на английском языке**

Здравствуйте! Сегодня мы начинаем изучать английский язык — язык, на котором говорят люди во многих странах мира.

**Как поздороваться:**

**Hello!** [хэ-ло́у] — Здравствуйте!
Это самое распространённое приветствие. Можно использовать в любой ситуации.

**Hi!** [хай] — Привет!
Это неформальное приветствие для друзей и знакомых.

**Good morning!** [гуд мо́рнинг] — Доброе утро!
Говорим до 12 часов дня.

**Good afternoon!** [гуд афтэну́н] — Добрый день!
Говорим с 12 до 18 часов.

**Good evening!** [гуд и́внинг] — Добрый вечер!
Говорим после 18 часов.

**Правила чтения:**
В квадратных скобках показано, как произносить слова. Читаем так, как написано в скобках.

**Примеры диалогов:**

— Hello! I am Ann.
— Hello! I am Tom.

— Hi! How are you?
— Hi! I am fine!

**Важно запомнить:**
- Hello и Hi — самые частые приветствия
- Good morning/day/evening — более официальные
- Всегда улыбаемся при приветствии!

**Потренируйся:**
Попробуй поздороваться с друзьями и родными по-английски!`,
          tasks: [
            "Выучить Hello! и Hi!",
            "Научиться говорить Good morning",
            "Разыграть диалог с другом",
            "Нарисовать смайлик и подписать Hello!"
          ]
        },
        {
          title: "Урок 2: What is your name? 📛",
          image: "/school-curriculum-app/images/lessons/grade1/english/lesson2-name.svg",
          description: `**Как спросить имя и представиться**

Сегодня научимся знакомиться на английском языке — спрашивать имя и говорить своё.

**Как спросить имя:**

**What is your name?** [уо́т из ё: нэйм?] — Как тебя зовут?
Это вопрос, который задаём новому знакомому.

Короткий вариант: **What's your name?** [уо́тс ё: нэйм?]

**Как ответить:**

**My name is...** [май нэйм из...] — Меня зовут...
Например: My name is Anna. [май нэйм из а́нна]

**I am...** [ай эм...] — Я...
Например: I am Tom. [ай эм том]

Короткий вариант: **I'm...** [айм...]
Например: I'm Kate. [айм кэйт]

**Диалог знакомства:**

— Hello! What is your name?
— My name is Olga. What is your name?
— I am Denis. Nice to meet you!
— Nice to meet you too!

**Полезные фразы:**

**Nice to meet you!** [найс ту ми́т ю!] — Приятно познакомиться!

**How are you?** [ха́у а: ю?] — Как дела?

**I am fine!** [айэм файн!] — Хорошо!

**Английские имена:**
- Boys: Tom, Ben, Nick, Sam, Dan
- Girls: Kate, Ann, Jane, Mary, Emma

**Потренируйся:**
Представься по-английски и спроси имя у друга!`,
          tasks: [
            "Выучить What is your name?",
            "Научиться говорить My name is...",
            "Разыграть диалог знакомства",
            "Написать своё имя по-английски"
          ]
        },
        {
          title: "Урок 3: Goodbye! 👋",
          image: "/school-curriculum-app/images/lessons/grade1/english/lesson3-goodbye.svg",
          description: `**Прощание на английском языке**

Урок посвящён тому, как правильно прощаться на английском языке.

**Основные прощания:**

**Goodbye!** [гудба́й] — До свидания!
Самое распространённое прощание.

**Bye!** [бай] — Пока!
Короткое, неформальное прощание.

**Bye-bye!** [ба́й-бай] — Пока-пока!
Очень дружелюбное, для близких.

**See you!** [си: ю!] — Увидимся!
Неформальное прощание.

**See you later!** [си: ю лэ́йтэ!] — До встречи!
Говорим, если скоро увидимся снова.

**See you tomorrow!** [си: ю тумо́роу!] — До завтра!

**Good night!** [гуд на́йт] — Спокойной ночи!
Говорим перед сном.

**Have a nice day!** [хэв э найс дэй!] — Хорошего дня!

**Диалоги прощания:**

— Goodbye, Tom!
— Goodbye, Ann! See you tomorrow!

— Bye, mum!
— Bye-bye, dear! Have a nice day!

**Песенка прощания:**
Goodbye, goodbye,
See you again!
Goodbye, goodbye,
See you my friend!

**Важно запомнить:**
- Goodbye — официальное
- Bye и Bye-bye — для друзей
- See you — неформальное "до встречи"
- Good night — только перед сном!

**Потренируйся:**
Попрощайся с друзьями по-английски разными способами!`,
          tasks: [
            "Выучить Goodbye и Bye",
            "Научиться говорить See you",
            "Выучить песенку прощания",
            "Попрощаться по-английски с другом"
          ]
        }
      ]
    },
    {
      topic: "Цвета и числа",
      lessons: [
        {
          title: "Урок 4: Colours 🎨",
          image: "/school-curriculum-app/images/lessons/grade1/english/lesson4-colours.svg",
          description: `**Цвета на английском языке**

Сегодня выучим названия основных цветов! Цвета по-английски — Colours [ка́лэз].

**Основные цвета:**

**Red** [рэд] — Красный
🍎 Apple is red. — Яблоко красное.

**Blue** [блу] — Синий
🌊 The sea is blue. — Море синее.

**Green** [грин] — Зелёный
🌳 Grass is green. — Трава зелёная.

**Yellow** [йэ́ллоу] — Жёлтый
☀️ Sun is yellow. — Солнце жёлтое.

**Orange** [о́риндж] — Оранжевый
🍊 Orange is orange. — Апельсин оранжевый.

**Purple** [пёпл] — Фиолетовый
🍇 Grapes are purple. — Виноград фиолетовый.

**Pink** [пинк] — Розовый
🌸 Flower is pink. — Цветок розовый.

**Black** [блэк] — Чёрный
🖤 Black cat. — Чёрная кошка.

**White** [уа́йт] — Белый
☁️ Cloud is white. — Облако белое.

**Brown** [бра́ун] — Коричневый
🐻 Bear is brown. — Медведь коричневый.

**Вопрос о цвете:**

**What colour is it?** [уо́т ка́лэ из ит?] — Какой это цвет?

**It is red.** [ит из рэд] — Это красный.

**Диалог:**
— What colour is the apple?
— It is red!

**Потренируйся:**
Назови цвета предметов вокруг себя!`,
          tasks: [
            "Выучить 10 цветов",
            "Назвать цвет предметов в классе",
            "Раскрасить картинку и подписать цвета",
            "Спросить друга: What colour is it?"
          ]
        },
        {
          title: "Урок 5: Numbers 1-5 🔢",
          image: "/school-curriculum-app/images/lessons/grade1/english/lesson5-numbers-1-5.svg",
          description: `**Числа от 1 до 5**

Сегодня выучим числа от одного до пяти на английском языке!

**Числа 1-5:**

**One** [уа́н] — Один
✏️ One pencil. — Один карандаш.

**Two** [ту] — Два
✏️✏️ Two pencils. — Два карандаша.

**Three** [три] — Три
🍎🍎🍎 Three apples. — Три яблока.

**Four** [фо] — Четыре
🌸🌸🌸🌸 Four flowers. — Четыре цветка.

**Five** [файв] — Пять
⭐⭐⭐⭐⭐ Five stars. — Пять звёзд.

**Правила:**
- После числа идёт существительное (предмет)
- Запомни произношение каждого числа!

**Счёт:**
One, two, three, four, five!
I can count! I am alive!

**Вопрос:**
**How many?** [ха́у мэ́ни?] — Сколько?

**Ответ:**
— How many apples?
— Three apples!

**Математика по-английски:**
1 + 1 = 2 → One plus one is two.
2 + 2 = 4 → Two plus two is four.

**Пальчики:**
Покажи пальцы и посчитай:
One finger, two fingers, three fingers, four!
Five fingers on one hand — count some more!

**Потренируйся:**
Посчитай предметы вокруг себя от 1 до 5!`,
          tasks: [
            "Выучить числа 1-5",
            "Посчитать предметы в классе",
            "Показать на пальцах и назвать",
            "Решить примеры: 1+2, 2+3"
          ]
        },
        {
          title: "Урок 6: Numbers 6-10 🔢",
          image: "/school-curriculum-app/images/lessons/grade1/english/lesson6-numbers-6-10.svg",
          description: `**Числа от 6 до 10**

Продолжаем учить числа! Сегодня от шести до десяти.

**Числа 6-10:**

**Six** [сикс] — Шесть
🌸🌸🌸🌸🌸🌸 Six flowers. — Шесть цветков.

**Seven** [сэ́вэн] — Семь
🌈 Seven colours in rainbow. — Семь цветов в радуге.

**Eight** [эйт] — Восемь
🕷️ Spider has eight legs. — У паука восемь лапок.

**Nine** [найн] — Девять
 九 Nine lives of a cat. — Девять жизней у кошки.

**Ten** [тэн] — Десять
🖐️🖐️ Ten fingers. — Десять пальцев.

**Весь счёт от 1 до 10:**
One, two, three, four, five,
Six, seven, eight, nine, ten!

**Обратный счёт:**
Ten, nine, eight, seven, six,
Five, four, three, two, one!

**Математика:**
3 + 4 = 7 → Three plus four is seven.
5 + 5 = 10 → Five plus five is ten.
8 - 3 = 5 → Eight minus three is five.

**Вопрос:**
**How many fingers?** — Сколько пальцев?
**Ten fingers!** — Десять пальцев!

**Песенка:**
One, two, three, four, five,
Once I caught a fish alive!
Six, seven, eight, nine, ten,
Then I let it go again!

**Потренируйся:**
Посчитай от 1 до 10 и обратно! Реши примеры!`,
          tasks: [
            "Выучить числа 6-10",
            "Посчитать до 10 и обратно",
            "Решить примеры: 5+3, 8-2, 4+6",
            "Выучить песенку"
          ]
        }
      ]
    }
  ]
}

export const games: GameLesson[] = [
  {
    title: "Hello! Привет! 👋",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Как сказать «Привет» по-английски?",
        options: ["Goodbye", "Hello", "Thanks", "Никто не знает", "Не знаю"],
        correctAnswer: "Hello",
        hint: "Это самое популярное приветствие"
      },
      {
        type: 'quiz',
        question: "Как ещё можно поздороваться?",
        options: ["Hi", "Bye", "No", "Никто не знает", "Не знаю"],
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
        question: "What is your name? — это...",
        options: ["Как дела?", "Как тебя зовут?", "Сколько тебе лет?", "Никто не знает", "Не знаю"],
        correctAnswer: "Как тебя зовут?",
        hint: "Name = имя"
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
        options: ["Синий", "Красный", "Зелёный", "Никто не знает", "Не знаю"],
        correctAnswer: "Красный",
        hint: "Red = Красный"
      },
      {
        type: 'quiz',
        question: "Как будет «синий» по-английски?",
        options: ["Red", "Blue", "Green", "Никто не знает", "Не знаю"],
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
        options: ["Red", "Blue", "Green", "Никто не знает", "Не знаю"],
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
        options: ["Один", "Два", "Три", "Никто не знает", "Не знаю"],
        correctAnswer: "Один",
        hint: "One = 1"
      },
      {
        type: 'quiz',
        question: "Как будет «пять» по-английски?",
        options: ["Four", "Five", "Six", "Никто не знает", "Не знаю"],
        correctAnswer: "Five",
        hint: "Five = 5"
      },
      {
        type: 'quiz',
        question: "Какое число идёт после Two?",
        options: ["One", "Three", "Four", "Five", "Six"],
        correctAnswer: "Three",
        hint: "От 1 до 4"
      },
      {
        type: 'quiz',
        question: "Ten - это?",
        options: ["8", "9", "10", "Никто не знает", "Не знаю"],
        correctAnswer: "10",
        hint: "Ten = 10"
      }
    ],
    reward: { stars: 3, message: "Excellent! Ты знаешь числа! 🔢" }
  },
  {
    title: "Животные 🐱",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Cat - это?",
        options: ["Собака", "Кошка", "Птица", "Никто не знает", "Не знаю"],
        correctAnswer: "Кошка",
        hint: "Cat = Кошка"
      },
      {
        type: 'quiz',
        question: "Как будет «собака» по-английски?",
        options: ["Cat", "Dog", "Bird", "Никто не знает", "Не знаю"],
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
        question: "Fish - это?",
        options: ["Птица", "Рыба", "Кошка", "Никто не знает", "Не знаю"],
        correctAnswer: "Рыба",
        hint: "Fish живёт в воде"
      }
    ],
    reward: { stars: 3, message: "Great job! Ты знаешь животных! 🐱" }
  },
  {
    title: "Приветствие и прощание 👋",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Как сказать «Привет» по-английски?",
        options: ["Bye", "Hello", "Thanks", "Никто не знает", "Не знаю"],
        correctAnswer: "Hello",
        hint: "Приветствие"
      },
      {
        type: 'quiz',
        question: "Как сказать «До свидания» по-английски?",
        options: ["Hello", "Goodbye", "Sorry", "Никто не знает", "Не знаю"],
        correctAnswer: "Goodbye",
        hint: "Прощание"
      },
      {
        type: 'find',
        question: "Найди приветствия:",
        options: ["Hello", "Bye", "Hi", "Goodbye", "Good morning"],
        correctAnswer: ["Hello", "Hi", "Good morning"],
        hint: "Приветствия"
      },
      {
        type: 'find',
        question: "Найди прощания:",
        options: ["Hello", "Goodbye", "Bye", "Hi", "Good night"],
        correctAnswer: ["Goodbye", "Bye", "Good night"],
        hint: "Прощания"
      }
    ],
    reward: { stars: 3, message: "Excellent! Ты умеешь здороваться! 👋" }
  },
  {
    title: "Числа 6-10 🔢",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'quiz',
        question: "Как будет «6» по-английски?",
        options: ["Five", "Six", "Seven", "Никто не знает", "Не знаю"],
        correctAnswer: "Six",
        hint: "Six = 6"
      },
      {
        type: 'quiz',
        question: "Как будет «8» по-английски?",
        options: ["Seven", "Eight", "Nine", "Никто не знает", "Не знаю"],
        correctAnswer: "Eight",
        hint: "Eight = 8"
      },
      {
        type: 'match',
        question: "Соедини число с переводом:",
        options: ["Six", "Seven", "Eight", "Nine", "Ten"],
        correctAnswer: ["6", "7", "8", "9", "10"],
        hint: "Числа на английском"
      },
      {
        type: 'find',
        question: "Найди числа от 6 до 10:",
        options: ["Six", "Five", "Seven", "Eight", "Three", "Nine", "Ten"],
        correctAnswer: ["Six", "Seven", "Eight", "Nine", "Ten"],
        hint: "Числа 6-10"
      }
    ],
    reward: { stars: 3, message: "Great! Ты знаешь числа! 🔢" }
  }
]
