import { SubjectData, GameLesson } from '@/data/types'

const createLesson = (
  title: string,
  description: string,
  tasks: string[],
  theory?: string,
  examples?: string[],
  facts?: string[],
  image?: string
) => ({
  title,
  description,
  tasks,
  theory,
  examples,
  facts,
  image
})

export const lessons: SubjectData = {
  title: "Иностранный язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: ["Семья", "Еда", "Животные", "Погода", "Цвета", "Числа", "Дом", "Школа"],
  detailedTopics: [
    {
      topic: "Семья",
      lessons: [
        createLesson(
          "Урок 1: Члены семьи",
          "Изучаем названия членов семьи на английском языке.",
          [
            "Выучить слова о семье",
            "Произнести слова вслух",
            "Составить предложения",
            "Описать свою семью"
          ],
          `## 📚 Члены семьи (Family Members)

**Семья — Family**

Изучим названия членов семьи на английском языке. Эти слова очень важны, ведь семья есть у каждого!

**Основные члены семьи:**

| Английский | Русский | Транскрипция |
|------------|---------|--------------|
| Mother | Мама | [ˈmʌðə] |
| Father | Папа | [ˈfɑːðə] |
| Sister | Сестра | [ˈsɪstə] |
| Brother | Брат | [ˈbrʌðə] |
| Grandmother | Бабушка | [ˈɡrænmʌðə] |
| Grandfather | Дедушка | [ˈɡrænfɑːðə] |

**Другие родственники:**

- **Son** [sʌn] — сын
- **Daughter** [ˈdɔːtə] — дочь
- **Uncle** [ˈʌŋkl] — дядя
- **Aunt** [ɑːnt] — тётя
- **Cousin** [ˈkʌzn] — кузен/кузина

**Полезные фразы:**

- This is my mother. — Это моя мама.
- This is my father. — Это мой папа.
- I have a sister. — У меня есть сестра.
- I have a brother. — У меня есть брат.
- My family is big. — Моя семья большая.
- My family is small. — Моя семья маленькая.

**Притяжательные местоимения:**

- My — мой/моя/мои
- Your — твой/твоя/твои
- His — его
- Her — её

**Примеры:**
- My mother is kind. — Моя мама добрая.
- His father is tall. — Его папа высокий.
- Her sister is young. — Её сестра молодая.`,
          [
            "👨‍👩‍👧 Mother = мама, Father = папа",
            "👧 Sister = сестра, Brother = брат",
            "👵 Grandmother = бабушка, Grandfather = дедушка"
          ],
          [
            "💡 Слово 'family' происходит от латинского 'familia' — семья!",
            "💡 В английском языке нет различия между старшей и младшей сестрой — обе 'sister'!",
            "💡 Слово 'cousin' обозначает и кузена, и кузину — пол не указывается!"
          ],
          "/school-curriculum-app/images/lessons/grade2/english/lesson1.svg"
        ),
        createLesson(
          "Урок 2: Описание семьи",
          "Учимся рассказывать о своей семье на английском языке.",
          [
            "Составить рассказ о семье",
            "Использовать новые слова",
            "Задать вопросы",
            "Ответить на вопросы"
          ],
          `## 📚 Описание семьи (Describing Family)

**Как рассказать о семье**

Чтобы рассказать о своей семье, нужно знать несколько полезных фраз и слов.

**Числительные для возраста:**

| Число | Английский | Число | Английский |
|-------|------------|-------|------------|
| 1 | one | 7 | seven |
| 2 | two | 8 | eight |
| 3 | three | 9 | nine |
| 4 | four | 10 | ten |
| 5 | five | 20 | twenty |
| 6 | six | 30 | thirty |

**Глагол to be (быть):**

- I am (I'm) — я есть
- He is (He's) — он есть
- She is (She's) — она есть
- We are (We're) — мы есть
- They are (They're) — они есть

**Описываем внешность:**

- tall — высокий
- short — низкий
- young — молодой
- old — старый
- beautiful — красивый
- handsome — красивый (о мужчине)

**Описываем характер:**

- kind — добрый
- nice — милый
- funny — смешной
- clever — умный
- friendly — дружелюбный

**Пример рассказа:**

"My name is Tom. I am 8. I have a family. My mother's name is Ann. She is 35. She is kind and beautiful. My father's name is John. He is 38. He is tall and funny. I have a sister. Her name is Kate. She is 5. She is nice. I love my family!"

Перевод: «Меня зовут Том. Мне 8 лет. У меня есть семья. Мою маму зовут Энн. Ей 35 лет. Она добрая и красивая. Моего папу зовут Джон. Ему 38 лет. Он высокий и смешной. У меня есть сестра. Её зовут Кейт. Ей 5 лет. Она милая. Я люблю свою семью!»

**Вопросы о семье:**

- What is your mother's name? — Как зовут твою маму?
- How old is your father? — Сколько лет твоему папе?
- Do you have a sister? — У тебя есть сестра?
- Do you have a brother? — У тебя есть брат?`,
          [
            "📝 'My mother is kind' — Моя мама добрая",
            "📝 'He is 35 years old' — Ему 35 лет",
            "📝 'I have a sister' — У меня есть сестра"
          ],
          [
            "💡 Глагол 'to be' — самый важный глагол в английском языке!",
            "💡 В английском возрасте используют 'years old': 'I am 8 years old'",
            "💡 'Do you have...?' — вопрос 'У тебя есть...?'"
          ],
          "/school-curriculum-app/images/lessons/grade2/english/lesson2.svg"
        )
      ]
    },
    {
      topic: "Еда",
      lessons: [
        createLesson(
          "Урок 3: Фрукты и овощи",
          "Изучаем названия фруктов и овощей на английском языке.",
          [
            "Выучить слова о фруктах",
            "Назвать овощи",
            "Составить список покупок",
            "Описать любимые фрукты"
          ],
          `## 📚 Фрукты и овощи (Fruits and Vegetables)

**Фрукты (Fruits):**

| Английский | Русский | Транскрипция |
|------------|---------|--------------|
| Apple | Яблоко | [ˈæpl] |
| Banana | Банан | [bəˈnɑːnə] |
| Orange | Апельсин | [ˈɒrɪndʒ] |
| Pear | Груша | [peə] |
| Lemon | Лимон | [ˈlemən] |
| Peach | Персик | [piːtʃ] |
| Grapes | Виноград | [ɡreɪps] |
| Strawberry | Клубника | [ˈstrɔːbəri] |

**Овощи (Vegetables):**

| Английский | Русский | Транскрипция |
|------------|---------|--------------|
| Tomato | Помидор | [təˈmɑːtəʊ] |
| Potato | Картофель | [pəˈteɪtəʊ] |
| Carrot | Морковь | [ˈkærət] |
| Cucumber | Огурец | [ˈkjuːkʌmbə] |
| Onion | Лук | [ˈʌnjən] |
| Cabbage | Капуста | [ˈkæbɪdʒ] |
| Pepper | Перец | [ˈpepə] |

**Полезные фразы:**

- I like apples. — Я люблю яблоки.
- I don't like onions. — Я не люблю лук.
- Do you like bananas? — Ты любишь бананы?
- Yes, I do. — Да.
- No, I don't. — Нет.

**Артикли a/an:**

Используем 'a' перед согласной, 'an' перед гласной:
- a banana — банан
- an apple — яблоко
- an orange — апельсин

**Множественное число:**

Обычно добавляем -s:
- apple → apples
- banana → bananas
- carrot → carrots

**Слова для описания вкуса:**

- sweet — сладкий
- sour — кислый
- tasty — вкусный
- yummy — вкусненький
- fresh — свежий`,
          [
            "🍎 Apple = яблоко, Banana = банан, Orange = апельсин",
            "🥕 Carrot = морковь, Potato = картофель, Tomato = помидор",
            "📝 'I like apples' — Я люблю яблоки"
          ],
          [
            "💡 Помидор в английском называется 'tomato', хотя это фрукт с ботанической точки зрения!",
            "💡 'Grape' — виноградина, 'grapes' — виноград (множество ягод)",
            "💡 'Strawberry' — клубника, буквально 'соломенная ягода'!"
          ],
          "/school-curriculum-app/images/lessons/grade2/english/lesson3.svg"
        ),
        createLesson(
          "Урок 4: Напитки и еда",
          "Изучаем названия напитков и базовых продуктов питания.",
          [
            "Выучить названия напитков",
            "Произнести слова вслух",
            "Описать вкус еды",
            "Составить диалог в кафе"
          ],
          `## 📚 Напитки и еда (Drinks and Food)

**Напитки (Drinks):**

| Английский | Русский | Транскрипция |
|------------|---------|--------------|
| Water | Вода | [ˈwɔːtə] |
| Milk | Молоко | [mɪlk] |
| Juice | Сок | [dʒuːs] |
| Tea | Чай | [tiː] |
| Coffee | Кофе | [ˈkɒfi] |

**Виды сока:**
- apple juice — яблочный сок
- orange juice — апельсиновый сок
- tomato juice — томатный сок

**Еда (Food):**

| Английский | Русский | Транскрипция |
|------------|---------|--------------|
| Bread | Хлеб | [bred] |
| Cheese | Сыр | [tʃiːz] |
| Butter | Масло | [ˈbʌtə] |
| Egg | Яйцо | [eɡ] |
| Meat | Мясо | [miːt] |
| Fish | Рыба | [fɪʃ] |
| Chicken | Курица | [ˈtʃɪkɪn] |
| Soup | Суп | [suːp] |

**Диалог в кафе:**

**A:** Can I have a sandwich, please?
(A: Можно мне сэндвич, пожалуйста?)

**B:** Here you are.
(B: Вот, пожалуйста.)

**A:** Thank you!
(A: Спасибо!)

**B:** You're welcome!
(B: Пожалуйста!)

**Полезные фразы:**

- I'm hungry. — Я голоден.
- I'm thirsty. — Я хочу пить.
- I want... — Я хочу...
- Can I have...? — Можно мне...?
- What would you like? — Что бы вы хотели?

**Счёт в кафе:**

- How much is it? — Сколько это стоит?
- It's 5 dollars. — Это стоит 5 долларов.
- Here you are. — Вот (подают деньги или еду).`,
          [
            "🥛 Milk = молоко, Water = вода, Juice = сок",
            "🍞 Bread = хлеб, Cheese = сыр, Butter = масло",
            "📝 'Can I have...?' — Можно мне...?"
          ],
          [
            "💡 Английское 'tea' произошло от китайского 'te'!",
            "💡 'Sandwich' назван в честь лорда Сэндвича, который любил есть мясо между кусками хлеба!",
            "💡 В Англии очень популярна традиция '5 o'clock tea' — чай в 5 часов вечера!"
          ],
          "/school-curriculum-app/images/lessons/grade2/english/lesson4.svg"
        )
      ]
    },
    {
      topic: "Животные",
      lessons: [
        createLesson(
          "Урок 5: Домашние животные",
          "Изучаем названия домашних животных на английском языке.",
          [
            "Выучить названия животных",
            "Описать своего питомца",
            "Рассказать о любимом животном",
            "Задать вопросы о питомце"
          ],
          `## 📚 Домашние животные (Pets)

**Домашние питомцы:**

| Английский | Русский | Транскрипция |
|------------|---------|--------------|
| Cat | Кошка | [kæt] |
| Dog | Собака | [dɒɡ] |
| Fish | Рыбка | [fɪʃ] |
| Bird | Птица | [bɜːd] |
| Hamster | Хомяк | [ˈhæmstə] |
| Rabbit | Кролик | [ˈræbɪt] |
| Parrot | Попугай | [ˈpærət] |
| Guinea pig | Морская свинка | [ˈɡɪni pɪɡ] |

**Слова для описания:**

**Размер:**
- big — большой
- small — маленький
- little — маленький (милый)

**Цвет:**
- white — белый
- black — чёрный
- brown — коричневый
- grey — серый
- orange — рыжий

**Характер:**
- cute — милый
- funny — смешной
- friendly — дружелюбный
- lazy — ленивый
- active — активный

**Части тела животных:**

- tail — хвост
- ear — ухо
- eye — глаз
- nose — нос
- paw — лапа
- fur — шерсть

**Глаголы:**

- run — бегать
- jump — прыгать
- play — играть
- sleep — спать
- eat — есть
- drink — пить

**Пример описания питомца:**

"I have a cat. Her name is Mimi. She is small and white. She has green eyes and a long tail. She likes to play and sleep. She is very cute!"

Перевод: «У меня есть кошка. Её зовут Мими. Она маленькая и белая. У неё зелёные глаза и длинный хвост. Она любит играть и спать. Она очень милая!»

**Вопросы о питомце:**

- Do you have a pet? — У тебя есть питомец?
- What pet do you have? — Какой у тебя питомец?
- What is its name? — Как его зовут?
- What colour is it? — Какого он цвета?`,
          [
            "🐱 Cat = кошка, Dog = собака, Fish = рыбка",
            "🐹 Hamster = хомяк, Rabbit = кролик, Bird = птица",
            "📝 'I have a cat. Her name is Mimi.' — У меня есть кошка. Её зовут Мими."
          ],
          [
            "💡 Кошки — самые популярные домашние питомцы в мире!",
            "💡 Слово 'puppy' — это щенок, 'kitten' — это котёнок!",
            "💡 Guinea pig (морская свинка) не из Гвинеи и не свинья!"
          ],
          "/school-curriculum-app/images/lessons/grade2/english/lesson5.svg"
        ),
        createLesson(
          "Урок 6: Дикие животные",
          "Изучаем названия диких животных на английском языке.",
          [
            "Выучить названия животных",
            "Описать дикое животное",
            "Рассказать, где живёт животное",
            "Что ест животное"
          ],
          `## 📚 Дикие животные (Wild Animals)

**Дикие животные:**

| Английский | Русский | Транскрипция |
|------------|---------|--------------|
| Lion | Лев | [ˈlaɪən] |
| Tiger | Тигр | [ˈtaɪɡə] |
| Bear | Медведь | [beə] |
| Wolf | Волк | [wʊlf] |
| Fox | Лиса | [fɒks] |
| Rabbit | Заяц | [ˈræbɪt] |
| Elephant | Слон | [ˈelɪfənt] |
| Monkey | Обезьяна | [ˈmʌŋki] |
| Giraffe | Жираф | [dʒɪˈrɑːf] |
| Zebra | Зебра | [ˈzebrə] |

**Где живут животные:**

- forest — лес
- jungle — джунгли
- savanna — саванна
- zoo — зоопарк
- Africa — Африка
- India — Индия

**Примеры:**
- Lions live in Africa. — Львы живут в Африке.
- Bears live in the forest. — Медведи живут в лесу.
- Monkeys live in the jungle. — Обезьяны живут в джунглях.

**Что едят животные:**

- meat — мясо (хищники)
- grass — трава (травоядные)
- fruit — фрукты
- fish — рыба

**Примеры:**
- Lions eat meat. — Львы едят мясо.
- Elephants eat grass. — Слоны едят траву.
- Monkeys eat fruit. — Обезьяны едят фрукты.

**Глаголы движения:**

- run — бегать
- walk — ходить
- jump — прыгать
- climb — лазить
- swim — плавать
- fly — летать

**Примеры:**
- Tigers can run. — Тигры умеют бегать.
- Monkeys can climb. — Обезьяны умеют лазить.
- Birds can fly. — Птицы умеют летать.

**Описание животного:**

"A lion is a big wild animal. It is yellow and brown. It has a big head and a long tail. Lions live in Africa. They eat meat. They can run fast."

Перевод: «Лев — это большое дикое животное. Оно жёлто-коричневое. У него большая голова и длинный хвост. Львы живут в Африке. Они едят мясо. Они могут быстро бегать.»`,
          [
            "🦁 Lion = лев, Tiger = тигр, Bear = медведь",
            "🐘 Elephant = слон, Monkey = обезьяна, Giraffe = жираф",
            "📝 'Lions live in Africa. They eat meat.' — Львы живут в Африке. Они едят мясо."
          ],
          [
            "💡 Лев — царь зверей, но тигр больше льва!",
            "💡 Жираф — самое высокое животное в мире, до 6 метров!",
            "💡 Слоны — единственные животные, которые не могут прыгать!"
          ],
          "/school-curriculum-app/images/lessons/grade2/english/lesson6.svg"
        )
      ]
    },
    {
      topic: "Цвета и числа",
      lessons: [
        createLesson(
          "Урок 7: Цвета",
          "Изучаем названия цветов на английском языке.",
          [
            "Выучить названия цветов",
            "Назвать цвета предметов",
            "Описать картинку",
            "Игра в цвета"
          ],
          `## 📚 Цвета (Colors)

**Основные цвета:**

| Английский | Русский | Транскрипция |
|------------|---------|--------------|
| Red | Красный | [red] |
| Blue | Синий | [bluː] |
| Green | Зелёный | [ɡriːn] |
| Yellow | Жёлтый | [ˈjeləʊ] |
| Orange | Оранжевый | [ˈɒrɪndʒ] |
| Purple | Фиолетовый | [ˈpɜːpl] |
| Pink | Розовый | [pɪŋk] |
| Brown | Коричневый | [braʊn] |
| Black | Чёрный | [blæk] |
| White | Белый | [waɪt] |
| Grey | Серый | [ɡreɪ] |

**Оттенки:**

- light — светлый (light blue — светло-синий)
- dark — тёмный (dark green — тёмно-зелёный)

**Примеры использования:**

**Описываем предметы:**
- a red apple — красное яблоко
- a blue car — синяя машина
- a green tree — зелёное дерево
- a yellow banana — жёлтый банан

**Вопрос о цвете:**

- What colour is it? — Какого это цвета?
- What colour is the cat? — Какого цвета кошка?
- It is black. — Она чёрная.

**Описываем несколько предметов:**
- red apples — красные яблоки
- blue cars — синие машины
- green trees — зелёные деревья

**Глагол to be с цветами:**

- The apple is red. — Яблоко красное.
- The sky is blue. — Небо синее.
- The grass is green. — Трава зелёная.

**Радуга (Rainbow):**

В английском запоминают цвета радуги по фразе:
**R**ichard **O**f **Y**ork **G**ave **B**attle **I**n **V**ain

- **R**ed — красный
- **O**range — оранжевый
- **Y**ellow — жёлтый
- **G**reen — зелёный
- **B**lue — синий
- **I**ndigo — индиго
- **V**iolet — фиолетовый

**Цвета в природе:**

- The sun is yellow. — Солнце жёлтое.
- The sky is blue. — Небо синее.
- The grass is green. — Трава зелёная.
- Snow is white. — Снег белый.`,
          [
            "🔴 Red = красный, Blue = синий, Green = зелёный",
            "🟡 Yellow = жёлтый, Orange = оранжевый, Purple = фиолетовый",
            "📝 'What colour is it? — It is red.' — Какого это цвета? — Красного."
          ],
          [
            "💡 Английское 'orange' — это и цвет, и фрукт!",
            "💡 Слово 'pink' (розовый) появилось в английском только в XVII веке!",
            "💡 В английском цвет 'blue' означает и голубой, и синий!"
          ],
          "/school-curriculum-app/images/lessons/grade2/english/lesson7.svg"
        ),
        createLesson(
          "Урок 8: Числа 1-20",
          "Учимся считать на английском языке от 1 до 20.",
          [
            "Посчитать предметы",
            "Назвать число",
            "Решить примеры",
            "Игра в числа"
          ],
          `## 📚 Числа от 1 до 20 (Numbers 1-20)

**Числа от 1 до 10:**

| Число | Английский | Транскрипция |
|-------|------------|--------------|
| 1 | One | [wʌn] |
| 2 | Two | [tuː] |
| 3 | Three | [θriː] |
| 4 | Four | [fɔː] |
| 5 | Five | [faɪv] |
| 6 | Six | [sɪks] |
| 7 | Seven | [ˈsevn] |
| 8 | Eight | [eɪt] |
| 9 | Nine | [naɪn] |
| 10 | Ten | [ten] |

**Числа от 11 до 20:**

| Число | Английский | Транскрипция |
|-------|------------|--------------|
| 11 | Eleven | [ɪˈlevn] |
| 12 | Twelve | [twelv] |
| 13 | Thirteen | [θɜːˈtiːn] |
| 14 | Fourteen | [fɔːˈtiːn] |
| 15 | Fifteen | [fɪfˈtiːn] |
| 16 | Sixteen | [sɪksˈtiːn] |
| 17 | Seventeen | [sevnˈtiːn] |
| 18 | Eighteen | [eɪˈtiːn] |
| 19 | Nineteen | [naɪnˈtiːn] |
| 20 | Twenty | [ˈtwenti] |

**Правила:**

1. Числа 11 и 12 — особые, их нужно запомнить!
2. Числа 13-19 образуются добавлением -teen к числу:
   - three + teen = thirteen (обратите внимание: thir-)
   - five + teen = fifteen (обратите внимание: fif-)
   - eight + teen = eighteen (только одна t)

**Десятки:**

- twenty — 20
- thirty — 30
- forty — 40
- fifty — 50

**Составные числа:**

- 21 — twenty-one
- 22 — twenty-two
- 35 — thirty-five
- 47 — forty-seven

**Примеры использования:**

- I have five apples. — У меня 5 яблок.
- There are seven days in a week. — В неделе 7 дней.
- I am eight years old. — Мне 8 лет.

**Математика:**

- 2 + 3 = 5 — Two plus three is five.
- 7 - 2 = 5 — Seven minus two is five.

**Вопросы с числами:**

- How many? — Сколько?
- How many apples? — Сколько яблок?
- How old are you? — Сколько тебе лет?
- I am eight. — Мне восемь.`,
          [
            "🔢 1-one, 2-two, 3-three, 4-four, 5-five",
            "🔢 6-six, 7-seven, 8-eight, 9-nine, 10-ten",
            "📝 'How many? — Five.' — Сколько? — Пять."
          ],
          [
            "💡 Числа 13-19 называются 'teen numbers' — отсюда слово 'teenager' (подросток)!",
            "💡 Число 0 читается как 'zero' или 'nought'!",
            "💡 В английском телефонные номера читают по цифрам: 12345 = one-two-three-four-five!"
          ],
          "/school-curriculum-app/images/lessons/grade2/english/lesson8.svg"
        )
      ]
    }
  ]
}

export const games: GameLesson[] = [
  {
    title: "Члены семьи 👨‍👩‍👧",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'match',
        question: "Соедини английское слово с русским:",
        options: ["Mother", "Father", "Sister", "Brother", "Grandmother"],
        correctAnswer: ["Мама", "Папа", "Сестра", "Брат", "Бабушка"],
        hint: "Семья = Family"
      },
      {
        type: 'find',
        question: "Как переводится Grandfather?",
        options: ["Бабушка", "Дедушка", "Дядя", "Тётя", "Кузен"],
        correctAnswer: "Дедушка",
        hint: "Grandfather = дедушка"
      },
      {
        type: 'quiz',
        question: "Как сказать «У меня есть сестра» по-английски?",
        options: ["I have a brother", "I have a sister", "I have a mother", "I have a father", "I have a family"],
        correctAnswer: "I have a sister",
        hint: "Sister = сестра"
      },
      {
        type: 'find',
        question: "Найди притяжательные местоимения:",
        options: ["My", "Mother", "Your", "Sister", "His"],
        correctAnswer: ["My", "Your", "His"],
        hint: "Притяжательные местоимения: мой, твой, его"
      },
      {
        type: 'match',
        question: "Соедини местоимение с переводом:",
        options: ["My", "Your", "His", "Her", "Our"],
        correctAnswer: ["Мой/моя", "Твой/твоя", "Его", "Её", "Наш/наша"],
        hint: "Чьё? — притяжательные местоимения"
      }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь семью! 👨‍👩‍👧" }
  },
  {
    title: "Описание семьи 📝",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'match',
        question: "Соедини описание с переводом:",
        options: ["tall", "short", "kind", "beautiful", "funny"],
        correctAnswer: ["Высокий", "Низкий", "Добрый", "Красивый", "Смешной"],
        hint: "Описываем внешность и характер"
      },
      {
        type: 'quiz',
        question: "Как сказать «Моя мама добрая»?",
        options: ["My mother is tall", "My mother is kind", "My mother is funny", "My mother is old", "My mother is young"],
        correctAnswer: "My mother is kind",
        hint: "Kind = добрый"
      },
      {
        type: 'find',
        question: "Найди формы глагола to be (быть):",
        options: ["am", "is", "like", "are", "have"],
        correctAnswer: ["am", "is", "are"],
        hint: "Глагол to be: am, is, are"
      },
      {
        type: 'quiz',
        question: "Как спросить «Сколько лет твоему папе?»?",
        options: ["What is your father?", "How old is your father?", "Where is your father?", "Who is your father?", "How is your father?"],
        correctAnswer: "How old is your father?",
        hint: "How old = сколько лет"
      },
      {
        type: 'match',
        question: "Соедини вопрос с ответом:",
        options: ["Do you have a sister?", "How old are you?", "What is her name?", "Is he tall?", "Are you kind?"],
        correctAnswer: ["Yes, I do", "I am 8", "Her name is Kate", "Yes, he is", "Yes, I am"],
        hint: "Вопросы и ответы о семье"
      }
    ],
    reward: { stars: 3, message: "Супер! Ты умеешь описывать семью! 📝" }
  },
  {
    title: "Фрукты и овощи 🍎",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'match',
        question: "Соедини фрукт с переводом:",
        options: ["Apple", "Banana", "Orange", "Lemon", "Pear"],
        correctAnswer: ["Яблоко", "Банан", "Апельсин", "Лимон", "Груша"],
        hint: "Fruits = фрукты"
      },
      {
        type: 'match',
        question: "Соедини овощ с переводом:",
        options: ["Carrot", "Potato", "Tomato", "Cucumber", "Onion"],
        correctAnswer: ["Морковь", "Картофель", "Помидор", "Огурец", "Лук"],
        hint: "Vegetables = овощи"
      },
      {
        type: 'quiz',
        question: "Какой артикль используется перед Apple?",
        options: ["a", "an", "the", "no article", "any"],
        correctAnswer: "an",
        hint: "Перед гласной — an"
      },
      {
        type: 'find',
        question: "Найди слова для описания вкуса:",
        options: ["sweet", "sour", "tall", "tasty", "funny"],
        correctAnswer: ["sweet", "sour", "tasty"],
        hint: "Вкус: сладкий, кислый, вкусный"
      },
      {
        type: 'quiz',
        question: "Как сказать «Я люблю яблоки»?",
        options: ["I like apples", "I like bananas", "I don't like apples", "I want apples", "I have apples"],
        correctAnswer: "I like apples",
        hint: "I like = я люблю"
      }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь фрукты и овощи! 🍎" }
  },
  {
    title: "Напитки и еда 🥛",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'match',
        question: "Соедини напиток с переводом:",
        options: ["Water", "Milk", "Juice", "Tea", "Coffee"],
        correctAnswer: ["Вода", "Молоко", "Сок", "Чай", "Кофе"],
        hint: "Drinks = напитки"
      },
      {
        type: 'find',
        question: "Найди продукты питания:",
        options: ["Bread", "Cheese", "Butter", "Kind", "Egg"],
        correctAnswer: ["Bread", "Cheese", "Butter", "Egg"],
        hint: "Food = еда"
      },
      {
        type: 'quiz',
        question: "Как сказать «Можно мне...?» по-английски?",
        options: ["I want...", "Can I have...?", "Give me...", "I need...", "I like..."],
        correctAnswer: "Can I have...?",
        hint: "Вежливая просьба в кафе"
      },
      {
        type: 'quiz',
        question: "Что означает «I'm hungry»?",
        options: ["Я хочу пить", "Я голоден", "Я устал", "Я рад", "Я болен"],
        correctAnswer: "Я голоден",
        hint: "Hungry = голодный"
      },
      {
        type: 'match',
        question: "Соедини фразу с переводом:",
        options: ["I'm thirsty", "Here you are", "Thank you", "You're welcome", "How much is it?"],
        correctAnswer: ["Я хочу пить", "Вот, пожалуйста", "Спасибо", "Пожалуйста", "Сколько это стоит?"],
        hint: "Фразы в кафе"
      }
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь еду и напитки! 🥛" }
  },
  {
    title: "Домашние животные 🐱",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'match',
        question: "Соедини питомца с переводом:",
        options: ["Cat", "Dog", "Fish", "Hamster", "Rabbit"],
        correctAnswer: ["Кошка", "Собака", "Рыбка", "Хомяк", "Кролик"],
        hint: "Pets = домашние животные"
      },
      {
        type: 'find',
        question: "Найди слова для описания характера питомца:",
        options: ["cute", "funny", "friendly", "forest", "lazy"],
        correctAnswer: ["cute", "funny", "friendly", "lazy"],
        hint: "Характер: милый, смешной, дружелюбный, ленивый"
      },
      {
        type: 'quiz',
        question: "Как сказать «У меня есть кошка»?",
        options: ["I have a dog", "I have a cat", "I am a cat", "I like cat", "I see cat"],
        correctAnswer: "I have a cat",
        hint: "I have = у меня есть"
      },
      {
        type: 'find',
        question: "Найди части тела животных:",
        options: ["tail", "ear", "paw", "fur", "kind"],
        correctAnswer: ["tail", "ear", "paw", "fur"],
        hint: "Хвост, ухо, лапа, шерсть"
      },
      {
        type: 'quiz',
        question: "Какой питомец — Guinea pig?",
        options: ["Морская свинка", "Морская свинья", "Гвинейская мышь", "Хомяк", "Кролик"],
        correctAnswer: "Морская свинка",
        hint: "Guinea pig = морская свинка"
      }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь питомцев! 🐱" }
  },
  {
    title: "Дикие животные 🦁",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'match',
        question: "Соедини животное с переводом:",
        options: ["Lion", "Tiger", "Bear", "Elephant", "Monkey"],
        correctAnswer: ["Лев", "Тигр", "Медведь", "Слон", "Обезьяна"],
        hint: "Wild animals = дикие животные"
      },
      {
        type: 'find',
        question: "Найди места обитания животных:",
        options: ["forest", "jungle", "savanna", "kind", "Africa"],
        correctAnswer: ["forest", "jungle", "savanna", "Africa"],
        hint: "Где живут дикие животные"
      },
      {
        type: 'quiz',
        question: "Как сказать «Львы живут в Африке»?",
        options: ["Lions live in Africa", "Lions eat Africa", "Lions run Africa", "Lions like Africa", "Lions see Africa"],
        correctAnswer: "Lions live in Africa",
        hint: "Live in = жить в"
      },
      {
        type: 'find',
        question: "Найди глаголы движения:",
        options: ["run", "jump", "kind", "climb", "swim"],
        correctAnswer: ["run", "jump", "climb", "swim"],
        hint: "Бегать, прыгать, лазить, плавать"
      },
      {
        type: 'quiz',
        question: "Что едят слоны?",
        options: ["Meat", "Grass", "Fish", "Fruit", "Bread"],
        correctAnswer: "Grass",
        hint: "Elephants eat grass"
      }
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь диких животных! 🦁" }
  },
  {
    title: "Цвета по-английски 🌈",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'match',
        question: "Соедини цвет с переводом:",
        options: ["Red", "Blue", "Green", "Yellow", "Orange"],
        correctAnswer: ["Красный", "Синий", "Зелёный", "Жёлтый", "Оранжевый"],
        hint: "Colors = цвета"
      },
      {
        type: 'find',
        question: "Найди название цветов по-английски:",
        options: ["Black", "White", "Pink", "Big", "Brown"],
        correctAnswer: ["Black", "White", "Pink", "Brown"],
        hint: "Чёрный, белый, розовый, коричневый"
      },
      {
        type: 'quiz',
        question: "Как спросить «Какого это цвета?»?",
        options: ["What is it?", "What colour is it?", "How is it?", "Where is it?", "Who is it?"],
        correctAnswer: "What colour is it?",
        hint: "Colour = цвет"
      },
      {
        type: 'quiz',
        question: "Какое слово означает и цвет, и фрукт?",
        options: ["Red", "Apple", "Orange", "Yellow", "Pink"],
        correctAnswer: "Orange",
        hint: "Оранжевый = апельсин"
      },
      {
        type: 'match',
        question: "Соедини цвет с предметом природы:",
        options: ["The sun", "The sky", "The grass", "Snow", "The night"],
        correctAnswer: ["Yellow", "Blue", "Green", "White", "Black"],
        hint: "Цвета в природе"
      }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь цвета! 🌈" }
  },
  {
    title: "Числа по-английски 🔢",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      {
        type: 'match',
        question: "Соедини число с переводом:",
        options: ["One", "Three", "Five", "Ten", "Seven"],
        correctAnswer: ["1", "3", "5", "10", "7"],
        hint: "Numbers = числа"
      },
      {
        type: 'find',
        question: "Найди числа от 11 до 20:",
        options: ["Eleven", "Twelve", "Thirteen", "Two", "Fifteen"],
        correctAnswer: ["Eleven", "Twelve", "Thirteen", "Fifteen"],
        hint: "Числа 11-20 называются teen numbers"
      },
      {
        type: 'quiz',
        question: "Какое число идёт после Three?",
        options: ["One", "Two", "Four", "Five", "Six"],
        correctAnswer: "Four",
        hint: "Один, два, три, четыре..."
      },
      {
        type: 'quiz',
        question: "Как спросить «Сколько?» по-английски?",
        options: ["What?", "How many?", "How old?", "Where?", "Who?"],
        correctAnswer: "How many?",
        hint: "How many = сколько"
      },
      {
        type: 'match',
        question: "Соедини пример с ответом:",
        options: ["2 + 3", "7 - 2", "4 + 4", "10 - 5", "6 + 4"],
        correctAnswer: ["Five", "Five", "Eight", "Five", "Ten"],
        hint: "Математика по-английски"
      }
    ],
    reward: { stars: 3, message: "Супер! Ты умеешь считать! 🔢" }
  }
]

