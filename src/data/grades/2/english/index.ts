import { SubjectData, GameLesson } from '@/data/types'

export const lessons: SubjectData = {
  title: "Иностранный язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: ["Семья", "Еда", "Животные", "Погода", "Цвета", "Числа", "Дом", "Школа"],
  detailedTopics: [
    {
      topic: "Семья",
      lessons: [
        {
          title: "Урок 1: Члены семьи",
          description: `**Семья по-английски**

Семья — это самое важное в жизни каждого человека. Давайте выучим названия членов семьи на английском языке.

**Члены семьи (Family members):**

- **Mother / Mom / Mum** [ˈmʌðə] — мама
- **Father / Dad** [ˈfɑːðə] — папа
- **Sister** [ˈsɪstə] — сестра
- **Brother** [ˈbrʌðə] — брат
- **Grandmother / Grandma** [ˈɡrænmʌðə] — бабушка
- **Grandfather / Grandpa** [ˈɡrænfɑːðə] — дедушка
- **Son** [sʌn] — сын
- **Daughter** [ˈdɔːtə] — дочь
- **Aunt** [ɑːnt] — тётя
- **Uncle** [ˈʌŋkl] — дядя
- **Cousin** [ˈkʌzn] — двоюродный брат/сестра

**Полезные фразы:**

- This is my mother. — Это моя мама.
- This is my father. — Это мой папа.
- I have a sister. — У меня есть сестра.
- I have a brother. — У меня есть брат.
- My family is big. — Моя семья большая.
- My family is small. — Моя семья маленькая.
- I love my family. — Я люблю свою семью.

**Пример рассказа о семье:**

"Hello! My name is Tom. This is my family. This is my mother. Her name is Ann. This is my father. His name is Bob. I have a sister. Her name is Kate. I love my family!"

**Вопросы для обсуждения:**
- How many people are in your family?
- Do you have a brother or sister?
- What is your mother's name?`,
          tasks: [
            "Выучить названия членов семьи",
            "Произнести слова вслух",
            "Составить рассказ о своей семье",
            "Ответить на вопросы о семье"
          ]
        },
        {
          title: "Урок 2: Описание семьи",
          description: `**Описание семьи**

Научимся описывать свою семью на английском языке. Мы будем использовать простые предложения и знакомые слова.

**Притяжательные местоимения:**

- **My** [maɪ] — мой, моя, моё
- **Your** [jɔː] — твой, твоя, твоё
- **His** [hɪz] — его
- **Her** [hɜː] — её

**Примеры:**
- This is my mother. Her name is Olga.
- This is my father. His name is Ivan.
- This is my sister. Her name is Masha.

**Описываем внешность:**

- **tall** [tɔːl] — высокий
- **short** [ʃɔːt] — низкий, короткий
- **young** [jʌŋ] — молодой
- **old** [əʊld] — старый
- **beautiful** [ˈbjuːtɪfl] — красивый
- **kind** [kaɪnd] — добрый

**Примеры описания:**
- My mother is beautiful. — Моя мама красивая.
- My father is tall. — Мой папа высокий.
- My grandmother is kind. — Моя бабушка добрая.
- My brother is young. — Мой брат молодой.

**Описываем профессии:**

- **doctor** [ˈdɒktə] — врач
- **teacher** [ˈtiːtʃə] — учитель
- **engineer** [ˌendʒɪˈnɪə] — инженер
- **worker** [ˈwɜːkə] — рабочий
- **driver** [ˈdraɪvə] — водитель

**Примеры:**
- My mother is a doctor. — Моя мама врач.
- My father is a teacher. — Мой папа учитель.

**Рассказ о семье:**

"Hello! My name is Peter. Let me tell you about my family. My family is big. I have a mother, a father, a grandmother and a sister.

My mother's name is Anna. She is a doctor. She is beautiful and kind. My father's name is Sergei. He is a teacher. He is tall.

My grandmother's name is Maria. She is old and very kind. My sister's name is Dasha. She is young and funny.

I love my family very much!"

**Вопросы для обсуждения:**
- What is your mother's name?
- What is your father?
- Is your family big or small?`,
          tasks: [
            "Составить рассказ о семье",
            "Описать внешность родителей",
            "Назвать профессии родителей",
            "Ответить на вопросы о семье"
          ]
        }
      ]
    },
    {
      topic: "Еда",
      lessons: [
        {
          title: "Урок 3: Фрукты и овощи",
          description: `**Фрукты и овощи по-английски**

Еда — это важная тема для изучения. Мы выучим названия фруктов и овощей на английском языке.

**Фрукты (Fruits):**

- **Apple** [ˈæpl] — яблоко
- **Pear** [peə] — груша
- **Banana** [bəˈnɑːnə] — банан
- **Orange** [ˈɒrɪndʒ] — апельсин
- **Lemon** [ˈlemən] — лимон
- **Peach** [piːtʃ] — персик
- **Grape** [ɡreɪp] — виноград
- **Cherry** [ˈtʃerɪ] — вишня
- **Strawberry** [ˈstrɔːbərɪ] — клубника
- **Watermelon** [ˈwɔːtəˌmelən] — арбуз

**Овощи (Vegetables):**

- **Tomato** [təˈmɑːtəʊ] — помидор
- **Potato** [pəˈteɪtəʊ] — картофель
- **Carrot** [ˈkærət] — морковь
- **Cucumber** [ˈkjuːkʌmbə] — огурец
- **Cabbage** [ˈkæbɪdʒ] — капуста
- **Onion** [ˈʌnjən] — лук
- **Garlic** [ˈɡɑːlɪk] — чеснок
- **Pepper** [ˈpepə] — перец
- **Corn** [kɔːn] — кукуруза
- **Pumpkin** [ˈpʌmpkɪn] — тыква

**Полезные фразы:**

- I like apples. — Я люблю яблоки.
- I don't like onions. — Я не люблю лук.
- Do you like bananas? — Ты любишь бананы?
- Yes, I do. / No, I don't. — Да. / Нет.
- An apple a day keeps the doctor away. — Одно яблоко в день — и врач не нужен.

**Что мы делаем с едой:**

- **eat** [iːt] — есть
- **drink** [drɪŋk] — пить
- **cook** [kʊk] — готовить
- **buy** [baɪ] — покупать

**Диалог в магазине:**

— Can I have three apples, please?
— Here you are.
— How much is it?
— Two dollars.
— Thank you!

**Вопросы:**
- What is your favourite fruit?
- Do you like vegetables?
- What fruits do you eat in summer?`,
          tasks: [
            "Выучить названия фруктов",
            "Выучить названия овощей",
            "Составить список любимых фруктов",
            "Провести диалог в магазине"
          ]
        },
        {
          title: "Урок 4: Напитки и еда",
          description: `**Напитки и еда**

Продолжаем изучать тему еды. Выучим названия напитков и основных блюд.

**Напитки (Drinks):**

- **Water** [ˈwɔːtə] — вода
- **Milk** [mɪlk] — молоко
- **Juice** [dʒuːs] — сок
- **Tea** [tiː] — чай
- **Coffee** [ˈkɒfɪ] — кофе
- **Lemonade** [ˌleməˈneɪd] — лимонад
- **Cocoa** [ˈkəʊkəʊ] — какао

**Виды сока:**
- Apple juice — яблочный сок
- Orange juice — апельсиновый сок
- Tomato juice — томатный сок

**Основные блюда:**

- **Bread** [bred] — хлеб
- **Butter** [ˈbʌtə] — масло
- **Cheese** [tʃiːz] — сыр
- **Egg** [eɡ] — яйцо
- **Meat** [miːt] — мясо
- **Fish** [fɪʃ] — рыба
- **Soup** [suːp] — суп
- **Sandwich** [ˈsænwɪdʒ] — бутерброд
- **Pizza** [ˈpiːtsə] — пицца
- **Salad** [ˈsæləd] — салат
- **Rice** [raɪs] — рис
- **Pasta** [ˈpæstə] — макароны

**Приём пищи:**

- **Breakfast** [ˈbrekfəst] — завтрак
- **Lunch** [lʌntʃ] — обед
- **Dinner** [ˈdɪnə] — ужин

**Полезные фразы:**

- I have breakfast at 8 o'clock. — Я завтракаю в 8 часов.
- What do you have for breakfast? — Что ты ешь на завтрак?
- I would like some tea. — Я хочу чаю.
- Can I have a sandwich? — Можно мне бутерброд?

**Пример рассказа:**

"In the morning I have breakfast. I eat bread with butter and cheese. I drink tea with milk. For lunch I have soup and salad. In the evening I have dinner. I eat fish with rice."

**Диалог:**

— What would you like to eat?
— I would like a sandwich, please.
— And what would you like to drink?
— Orange juice, please.
— Here you are!
— Thank you!`,
          tasks: [
            "Выучить названия напитков",
            "Назвать любимые блюда",
            "Рассказать, что едят на завтрак",
            "Составить диалог в кафе"
          ]
        }
      ]
    },
    {
      topic: "Животные",
      lessons: [
        {
          title: "Урок 5: Домашние животные",
          description: `**Домашние животные (Pets)**

Домашние животные — это наши любимцы, которые живут вместе с нами. Выучим их названия на английском языке.

**Домашние животные:**

- **Cat** [kæt] — кошка
- **Dog** [dɒɡ] — собака
- **Hamster** [ˈhæmstə] — хомяк
- **Rabbit** [ˈræbɪt] — кролик
- **Parrot** [ˈpærət] — попугай
- **Fish** [fɪʃ] — рыбка
- **Guinea pig** [ˈɡɪnɪ pɪɡ] — морская свинка
- **Turtle** [ˈtɜːtl] — черепаха
- **Mouse** [maʊs] — мышь

**Что делают животные:**

- **run** [rʌn] — бегать
- **jump** [dʒʌmp] — прыгать
- **play** [pleɪ] — играть
- **sleep** [sliːp] — спать
- **eat** [iːt] — есть
- **drink** [drɪŋk] — пить

**Описание животного:**

- **big** [bɪɡ] — большой
- **small** [smɔːl] — маленький
- **fluffy** [ˈflʌfɪ] — пушистый
- **cute** [kjuːt] — милый
- **funny** [ˈfʌnɪ] — забавный
- **friendly** [ˈfrendlɪ] — дружелюбный

**Полезные фразы:**

- I have a cat. — У меня есть кошка.
- My cat is fluffy. — Моя кошка пушистая.
- I like dogs. — Я люблю собак.
- Do you have a pet? — У тебя есть питомец?
- Yes, I have a dog. — Да, у меня есть собака.
- What is your pet's name? — Как зовут твоего питомца?
- My dog's name is Rex. — Мою собаку зовут Рекс.

**Пример рассказа:**

"I have a pet. It is a cat. My cat's name is Murka. She is small and fluffy. She is orange and white. Murka likes to play and sleep. She eats fish and drinks milk. I love my cat!"

**Звуки животных:**
- Cats say "meow" — Кошки говорят "мяу"
- Dogs say "woof" — Собаки говорят "гав"`,
          tasks: [
            "Выучить названия домашних животных",
            "Описать своего питомца",
            "Рассказать о любимом животном",
            "Задать вопросы о питомце"
          ]
        },
        {
          title: "Урок 6: Дикие животные",
          description: `**Дикие животные (Wild animals)**

Дикие животные живут в лесах, джунглях, саваннах и других природных местах. Они не живут дома у людей.

**Дикие животные:**

- **Lion** [ˈlaɪən] — лев
- **Tiger** [ˈtaɪɡə] — тигр
- **Bear** [beə] — медведь
- **Wolf** [wʊlf] — волк
- **Fox** [fɒks] — лиса
- **Rabbit** [ˈræbɪt] — заяц
- **Elephant** [ˈelɪfənt] — слон
- **Monkey** [ˈmʌŋkɪ] — обезьяна
- **Giraffe** [dʒɪˈrɑːf] — жираф
- **Zebra** [ˈzebrə] — зебра
- **Crocodile** [ˈkrɒkədaɪl] — крокодил
- **Snake** [sneɪk] — змея
- **Hippo** [ˈhɪpəʊ] — бегемот
- **Rhino** [ˈraɪnəʊ] — носорог

**Где живут животные:**

- **Forest** [ˈfɒrɪst] — лес
- **Jungle** [ˈdʒʌŋɡl] — джунгли
- **Zoo** [zuː] — зоопарк
- **Africa** [ˈæfrɪkə] — Африка
- **River** [ˈrɪvə] — река

**Что едят животные:**

- **Meat** [miːt] — мясо (хищники)
- **Grass** [ɡrɑːs] — трава (травоядные)
- **Fish** [fɪʃ] — рыба
- **Bananas** [bəˈnɑːnəz] — бананы

**Хищные и травоядные:**

- **Carnivore** [ˈkɑːnɪvɔː] — хищник (ест мясо): lion, tiger, wolf
- **Herbivore** [ˈhɜːbɪvɔː] — травоядное (ест растения): elephant, giraffe, zebra

**Полезные фразы:**

- Lions live in Africa. — Львы живут в Африке.
- The tiger is big and strong. — Тигр большой и сильный.
- Monkeys like bananas. — Обезьяны любят бананы.
- I saw an elephant at the zoo. — Я видел слона в зоопарке.
- What animals live in the forest? — Какие животные живут в лесу?

**Пример рассказа:**

"Wild animals live in forests and jungles. The lion is the king of animals. It is big and strong. The elephant is very big. It has a long nose. The giraffe is tall. It has a long neck. Monkeys are funny. They like to jump and play. Bears live in the forest. They sleep in winter."

**Интересные факты:**
- Lions live in groups called "pride"
- Elephants are the biggest land animals
- Giraffes have the longest necks`,
          tasks: [
            "Выучить названия диких животных",
            "Рассказать, где живут животные",
            "Описать любимое дикое животное",
            "Сравнить хищников и травоядных"
          ]
        }
      ]
    },
    {
      topic: "Цвета и числа",
      lessons: [
        {
          title: "Урок 7: Цвета",
          description: `**Цвета (Colours)**

Цвета окружают нас повсюду. Давайте выучим названия цветов на английском языке.

**Основные цвета:**

- **Red** [red] — красный
- **Blue** [bluː] — синий
- **Yellow** [ˈjeləʊ] — жёлтый
- **Green** [ɡriːn] — зелёный
- **Orange** [ˈɒrɪndʒ] — оранжевый
- **Purple** [ˈpɜːpl] — фиолетовый
- **Pink** [pɪŋk] — розовый
- **Brown** [braʊn] — коричневый
- **Black** [blæk] — чёрный
- **White** [waɪt] — белый
- **Grey** [ɡreɪ] — серый

**Оттенки:**

- **Light** [laɪt] — светлый (light blue — светло-синий)
- **Dark** [dɑːk] — тёмный (dark green — тёмно-зелёный)

**Полезные фразы:**

- What colour is it? — Какой это цвет?
- It is red. — Это красный.
- I like blue. — Мне нравится синий.
- My favourite colour is green. — Мой любимый цвет — зелёный.
- What is your favourite colour? — Какой твой любимый цвет?

**Описываем предметы:**

- The apple is red. — Яблоко красное.
- The sky is blue. — Небо синее.
- The grass is green. — Трава зелёная.
- The sun is yellow. — Солнце жёлтое.
- The snow is white. — Снег белый.

**Игра с цветами:**

Учитель показывает предмет, ученики называют цвет:
— What colour is the banana?
— The banana is yellow!
— What colour is the grass?
— The grass is green!

**Радуга (Rainbow):**

В радуге 7 цветов: Red, Orange, Yellow, Green, Blue, Indigo, Violet.
Запоминалка: Richard Of York Gave Battle In Vain (Ричард Йоркский Битву Проиграл).

**Пример рассказа:**

"I see many colours around me. The sky is blue. The sun is yellow. The grass is green. Trees are green in summer and yellow in autumn. Flowers are red, pink, purple and orange. Snow is white. My favourite colour is blue. What is your favourite colour?"`,
          tasks: [
            "Выучить названия цветов",
            "Назвать цвета предметов",
            "Описать картинку с цветами",
            "Провести игру с цветами"
          ]
        },
        {
          title: "Урок 8: Числа 1-20",
          description: `**Числа от 1 до 20 (Numbers)**

Числа нужны нам каждый день — для счёта, времени, денег. Выучим числа от 1 до 20.

**Числа от 1 до 10:**

- **One** [wʌn] — один (1)
- **Two** [tuː] — два (2)
- **Three** [θriː] — три (3)
- **Four** [fɔː] — четыре (4)
- **Five** [faɪv] — пять (5)
- **Six** [sɪks] — шесть (6)
- **Seven** [ˈsevn] — семь (7)
- **Eight** [eɪt] — восемь (8)
- **Nine** [naɪn] — девять (9)
- **Ten** [ten] — десять (10)

**Числа от 11 до 20:**

- **Eleven** [ɪˈlevn] — одиннадцать (11)
- **Twelve** [twelv] — двенадцать (12)
- **Thirteen** [ˌθɜːˈtiːn] — тринадцать (13)
- **Fourteen** [ˌfɔːˈtiːn] — четырнадцать (14)
- **Fifteen** [ˌfɪfˈtiːn] — пятнадцать (15)
- **Sixteen** [ˌsɪksˈtiːn] — шестнадцать (16)
- **Seventeen** [ˌsevnˈtiːn] — семнадцать (17)
- **Eighteen** [ˌeɪˈtiːn] — восемнадцать (18)
- **Nineteen** [ˌnaɪnˈtiːn] — девятнадцать (19)
- **Twenty** [ˈtwentɪ] — двадцать (20)

**Правила образования чисел 13-19:**

К числам 3-9 добавляется окончание "-teen":
- Three → Thir teen (13)
- Four → Four teen (14)
- Five → Fif teen (15)
- Six → Six teen (16)

**Полезные фразы:**

- How many? — Сколько?
- Count from 1 to 10. — Посчитай от 1 до 10.
- I have five apples. — У меня пять яблок.
- What number is this? — Какое это число?
- It is number seven. — Это число семь.

**Считаем предметы:**

- One cat — одна кошка
- Two dogs — две собаки
- Three birds — три птицы
- Four apples — четыре яблока
- Five books — пять книг

**Пример диалога:**

— How many apples do you have?
— I have three apples.
— How many bananas?
— I have five bananas.
— How many fruits?
— I have eight fruits!

**Математика на английском:**

- 2 + 3 = 5 (Two plus three is five)
- 7 - 2 = 5 (Seven minus two is five)

**Игра в числа:**
Учитель называет число, ученики показывают соответствующее количество пальцев.`,
          tasks: [
            "Выучить числа от 1 до 10",
            "Выучить числа от 11 до 20",
            "Посчитать предметы в классе",
            "Решить примеры на английском"
          ]
        }
      ]
    }
  ]
}

export const games: GameLesson[] = [
  {
    title: "Соедини слово и перевод",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'match',
        question: "Соедини английское слово с русским:",
        options: ["Mother", "Father", "Sister", "Brother"],
        correctAnswer: ["Мама", "Папа", "Сестра", "Брат"],
        hint: "Семья = Family"
      },
      {
        type: 'match',
        question: "Соедини слово с переводом:",
        options: ["Cat", "Dog", "Bird", "Fish"],
        correctAnswer: ["Кошка", "Собака", "Птица", "Рыба"],
        hint: "Animals = животные"
      }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь слова! 📚" }
  },
  {
    title: "Найди правильный перевод",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'find',
        question: "Что означает Apple?",
        options: ["Груша", "Яблоко", "Апельсин", "Банан"],
        correctAnswer: "Яблоко",
        hint: "Apple = яблоко"
      },
      {
        type: 'find',
        question: "Что означает Milk?",
        options: ["Вода", "Сок", "Молоко", "Чай"],
        correctAnswer: "Молоко",
        hint: "Milk = молоко"
      },
      {
        type: 'find',
        question: "Что означает Bread?",
        options: ["Молоко", "Хлеб", "Сыр", "Масло"],
        correctAnswer: "Хлеб",
        hint: "Bread = хлеб"
      },
      {
        type: 'find',
        question: "Что означает Water?",
        options: ["Вода", "Молоко", "Сок", "Чай"],
        correctAnswer: "Вода",
        hint: "Water = вода"
      }
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь еду! 🍎" }
  },
  {
    title: "Цвета по-английски",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'match',
        question: "Соедини цвет с переводом:",
        options: ["Red", "Blue", "Green", "Yellow"],
        correctAnswer: ["Красный", "Синий", "Зелёный", "Жёлтый"],
        hint: "Colors = цвета"
      },
      {
        type: 'find',
        question: "Какой цвет означает Black?",
        options: ["Белый", "Чёрный", "Серый", "Коричневый"],
        correctAnswer: "Чёрный",
        hint: "Black = чёрный"
      },
      {
        type: 'find',
        question: "Какой цвет означает White?",
        options: ["Белый", "Чёрный", "Серый", "Жёлтый"],
        correctAnswer: "Белый",
        hint: "White = белый"
      }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь цвета! 🌈" }
  },
  {
    title: "Числа по-английски",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'order',
        question: "Расставь числа по порядку от 1 до 5:",
        options: ["Three", "One", "Five", "Two", "Four"],
        correctAnswer: ["One", "Two", "Three", "Four", "Five"],
        hint: "Один, два, три, четыре, пять"
      },
      {
        type: 'match',
        question: "Соедини число с переводом:",
        options: ["One", "Three", "Five", "Ten"],
        correctAnswer: ["1", "3", "5", "10"],
        hint: "Numbers = числа"
      },
      {
        type: 'find',
        question: "Какое число означает Seven?",
        options: ["5", "6", "7", "8"],
        correctAnswer: "7",
        hint: "Seven = 7"
      }
    ],
    reward: { stars: 3, message: "Супер! Ты умеешь считать! 🔢" }
  },
  {
    title: "Животные",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'find',
        question: "Какое животное означает Cat?",
        options: ["Собака", "Кошка", "Птица", "Рыба"],
        correctAnswer: "Кошка",
        hint: "Cat = кошка"
      },
      {
        type: 'find',
        question: "Какое животное означает Dog?",
        options: ["Кошка", "Собака", "Птица", "Лошадь"],
        correctAnswer: "Собака",
        hint: "Dog = собака"
      },
      {
        type: 'find',
        question: "Найди домашнее животное:",
        options: ["Tiger", "Lion", "Cat", "Wolf"],
        correctAnswer: "Cat",
        hint: "Pet = домашнее животное"
      },
      {
        type: 'find',
        question: "Найди дикое животное:",
        options: ["Cat", "Dog", "Tiger", "Fish"],
        correctAnswer: "Tiger",
        hint: "Wild = дикий"
      }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь животных! 🐱🐶" }
  }
]
