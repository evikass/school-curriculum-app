import { SubjectData, GameLesson } from '@/data/types'

const L = (title: string, description: string, tasks: string[], image?: string, content?: string, examples?: string[], facts?: string[]) => ({
  title, description, tasks, theory: description, image, content, examples, facts
})

export const lessons: SubjectData = {
  title: "Иностранный язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: ["Alphabet", "Numbers", "Colors", "Family", "Animals", "Food", "Daily routine"],
  detailedTopics: [
    {
      topic: "Alphabet and Sounds",
      lessons: [
        L("Урок 1: English Alphabet", "Английский алфавит.", [
          "26 букв в алфавите",
          "A B C D E F G...",
          "Спеть песенку ABC",
          "Запомнить порядок букв"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson1.svg",
        `## 🔤 English Alphabet (Английский алфавит)

В английском алфавите **26 букв**. Это меньше, чем в русском (33 буквы)!

### 📚 The Alphabet:

**A B C D E F G H I J K L M N O P Q R S T U V W X Y Z**

### 🎵 ABC Song:

«A-B-C-D-E-F-G
H-I-J-K-L-M-N-O-P
Q-R-S, T-U-V
W-X, Y and Z
Now I know my ABCs
Next time won't you sing with me?»

### 📝 Буквы и их названия:

| Буква | Название | Буква | Название |
|-------|----------|-------|----------|
| Aa | эй | Nn | эн |
| Bb | би | Oo | оу |
| Cc | си | Pp | пи |
| Dd | ди | Qq | кью |
| Ee | и | Rr | ар |
| Ff | эф | Ss | эс |
| Gg | джи | Tt | ти |
| Hh | эйч | Uu | ю |
| Ii | ай | Vv | ви |
| Jj | джей | Ww | дабл-ю |
| Kk | кей | Xx | экс |
| Ll | эл | Yy | уай |
| Mm | эм | Zz | зед/зи |

### 💡 Интересные факты:

- Буква **E** — самая частая в английском
- Буква **Z** произносится «зед» в Британии и «зи» в США`,
        ["A = эй, B = би, C = си", "Английский алфавит = 26 букв", "E — самая частая буква"],
        ["В английском нет букв Ё, Й, Ъ, Ы, Ь, Э, Ю, Я", "Буква E встречается в каждом 8 слове", "ABC Song — самая известная песня для детей"]),
        L("Урок 2: Vowels and Consonants", "Гласные и согласные.", [
          "Гласные: A, E, I, O, U",
          "Y иногда гласная",
          "Произношение звуков",
          "Прочитать слова"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson2.svg",
        `## 🗣️ Vowels and Consonants (Гласные и согласные)

В английском языке буквы делятся на гласные и согласные.

### 🅰️ Vowels (Гласные):

**A, E, I, O, U** — всегда гласные

**Y** — иногда гласная (в конце слова: my, why, fly)

### 📚 Short Vowels (Краткие гласные):

| Буква | Звук | Примеры |
|-------|------|---------|
| Aa | [æ] | cat, bat, map |
| Ee | [e] | pen, bed, red |
| Ii | [ɪ] | pig, sit, big |
| Oo | [ɒ] | dog, box, hot |
| Uu | [ʌ] | cup, bus, sun |

### 📚 Long Vowels (Долгие гласные):

| Буква | Звук | Примеры |
|-------|------|---------|
| Aa | [eɪ] | name, cake, face |
| Ee | [iː] | me, see, tree |
| Ii | [aɪ] | like, time, five |
| Oo | [əʊ] | go, home, nose |
| Uu | [juː] | student, music, cute |

### 🔡 Consonants (Согласные):

Все остальные буквы: **B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z**

### 💡 Правило:

- Гласные = 5-6 букв
- Согласные = 20-21 буква`,
        ["Гласные: A, E, I, O, U", "Y — иногда гласная", "Cat [kæt], Name [neɪm]"],
        ["Y — особая буква: в «my» она гласная, в «yes» — согласная", "Гласные могут быть краткими и долгими", "В каждом слове есть хотя бы одна гласная"]),
        L("Урок 3: Reading Rules", "Правила чтения.", [
          "Open syllable: name, like",
          "Closed syllable: cat, dog",
          "Прочитать слова",
          "Найти различия"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson3.svg",
        `## 📖 Reading Rules (Правила чтения)

В английском языке есть правила чтения, которые помогают правильно читать слова.

### 📖 Open Syllable (Открытый слог):

Слог заканчивается на гласную букву.
**Гласная читается как в алфавите!**

| Буква | Чтение | Примеры |
|-------|--------|---------|
| A | эй | name, cake, late |
| E | и | me, he, she |
| I | ай | like, time, five |
| O | оу | go, home, no |
| U | ю | student, music |

### 📖 Closed Syllable (Закрытый слог):

Слог заканчивается на согласную букву.
**Гласная читается кратко!**

| Буква | Чтение | Примеры |
|-------|--------|---------|
| A | э | cat, map, hat |
| E | е | pen, bed, red |
| I | и | pig, sit, big |
| O | о | dog, box, hot |
| U | а | cup, bus, sun |

### 🔄 Сравним:

| Открытый | Закрытый |
|----------|----------|
| name (эй) | cat (э) |
| like (ай) | pig (и) |
| go (оу) | dog (о) |

### 💡 Как определить тип слога:

- **Открытый:** после гласной нет согласной или она одна в конце (no, he, my)
- **Закрытый:** после гласной стоит согласная (cat, dog, pen)`,
        ["Name — открытый слог (эй)", "Cat — закрытый слог (э)", "Like [laɪk], Pig [pɪg]"],
        ["Одна буква может читаться по-разному", "Правила помогают, но есть исключения", "Чем больше читаешь, тем легче запомнить"]),
        L("Урок 4: Common Words", "Частые слова.", [
          "the, and, is, it, to",
          "Прочитать предложения",
          "Составить фразы",
          "Использовать в речи"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson4.svg",
        `## 📝 Common Words (Частые слова)

Эти слова встречаются чаще всего в английском языке. Выучи их!

### 📚 Top 20 Words:

| Слово | Перевод | Пример |
|-------|---------|--------|
| the | определённый артикль | the cat |
| a / an | неопределённый артикль | a cat, an apple |
| and | и | cat and dog |
| is | есть (он/она/оно) | He is happy |
| it | это | It is a cat |
| to | к, в (направление) | go to school |
| I | я | I am a student |
| you | ты, вы | You are my friend |
| he | он | He is tall |
| she | она | She is kind |
| we | мы | We are friends |
| they | они | They are students |
| have | иметь | I have a cat |
| this | это | This is my book |
| that | тот | That is a dog |
| what | что, какой | What is this? |
| my | мой | My name is Tom |
| your | твой | What is your name? |
| yes | да | Yes, I can |
| no | нет | No, I can't |

### 📝 Простые предложения:

- **This is a cat.** — Это кошка.
- **I have a dog.** — У меня есть собака.
- **She is my friend.** — Она моя подруга.
- **What is your name?** — Как тебя зовут?
- **My name is Tom.** — Меня зовут Том.

### 💡 Местоимения:

| Русский | Английский |
|---------|------------|
| я | I |
| ты | you |
| он | he |
| она | she |
| оно | it |
| мы | we |
| они | they |`,
        ["The cat, A dog, An apple", "I am, You are, He is", "What is your name?"],
        ["«The» — самое частое слово в английском", "Местоимения помогают говорить о себе и других", "Глагол «to be» — am, is, are"])
      ]
    },
    {
      topic: "Numbers and Colors",
      lessons: [
        L("Урок 5: Numbers 1-20", "Числа от 1 до 20.", [
          "One, two, three, four...",
          "Eleven, twelve, thirteen...",
          "Посчитать предметы",
          "Назвать возраст"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson5.svg",
        `## 🔢 Numbers 1-20 (Числа от 1 до 20)

Числа в английском языке имеют свои названия. Выучи их!

### 📚 Numbers 1-10:

| Цифра | Английский | Транскрипция |
|-------|------------|--------------|
| 1 | one | уан |
| 2 | two | ту |
| 3 | three | сри |
| 4 | four | фо |
| 5 | five | файв |
| 6 | six | сикс |
| 7 | seven | севен |
| 8 | eight | эйт |
| 9 | nine | найн |
| 10 | ten | тен |

### 📚 Numbers 11-20:

| Цифра | Английский | Транскрипция |
|-------|------------|--------------|
| 11 | eleven | илéвен |
| 12 | twelve | туэлв |
| 13 | thirteen | сётин |
| 14 | fourteen | фóтин |
| 15 | fifteen | фифтúн |
| 16 | sixteen | сикстúн |
| 17 | seventeen | севентúн |
| 18 | eighteen | эйтúн |
| 19 | nineteen | нáйтин |
| 20 | twenty | твéнти |

### 💡 Правила:

**13-19:** добавляем **-teen** к числу 3-9
- three → thirteen
- four → fourteen
- six → sixteen

**Исключения:**
- 11, 12 — особые слова
- 13 — three → thirteen (меняется)
- 15 — five → fifteen (меняется)
- 18 — eight → eighteen (один t)`,
        ["1-one, 2-two, 3-three", "11-eleven, 12-twelve, 13-thirteen", "How old are you? — I am 9"],
        ["«teen» означает возраст 13-19 лет (teenager)", "13-19 = цифра + teen", "12 — особое слово, не «twoteen»"]),
        L("Урок 6: Numbers 20-100", "Десятки до ста.", [
          "Twenty, thirty, forty...",
          "25 = twenty-five",
          "Назвать числа",
          "Решить примеры"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson6.svg",
        `## 🔢 Numbers 20-100 (Десятки до ста)

После 20 числа образуются по правилу!

### 📚 Tens (Десятки):

| Число | Английский | Транскрипция |
|-------|------------|--------------|
| 20 | twenty | твéнти |
| 30 | thirty | сёти |
| 40 | forty | фóти |
| 50 | fifty | фúфти |
| 60 | sixty | сúксти |
| 70 | seventy | сéвенти |
| 80 | eighty | эйти |
| 90 | ninety | нáйти |
| 100 | one hundred | уан хáндред |

### 🔄 Составные числа:

**Правило:** десятки + единицы (через дефис)

| Число | Английский |
|-------|------------|
| 21 | twenty-one |
| 35 | thirty-five |
| 47 | forty-seven |
| 58 | fifty-eight |
| 63 | sixty-three |
| 72 | seventy-two |
| 84 | eighty-four |
| 99 | ninety-nine |

### 📝 Примеры:

- **25 books** — twenty-five books
- **37 apples** — thirty-seven apples
- **50 students** — fifty students

### 💡 Математика на английском:

- **plus** — плюс
- **minus** — минус
- **equals** — равно

**5 + 3 = 8** → Five plus three equals eight.
**10 - 4 = 6** → Ten minus four equals six.`,
        ["20-twenty, 30-thirty, 40-forty", "25 = twenty-five", "100 = one hundred"],
        ["Forty пишется без 'u' (не fourty!)", "Десятки образуются с -ty", "Дефис обязателен: twenty-one"]),
        L("Урок 7: Colors", "Цвета.", [
          "Red, blue, green, yellow",
          "Orange, purple, pink, brown",
          "Описать предметы",
          "Назвать любимый цвет"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson7.svg",
        `## 🎨 Colors (Цвета)

Цвета помогают описывать предметы. Выучи названия цветов!

### 📚 Basic Colors:

| Цвет | Английский | Транскрипция |
|------|------------|--------------|
| красный | red | ред |
| синий | blue | блу |
| зелёный | green | гри́н |
| жёлтый | yellow | йéллоу |
| оранжевый | orange | óриндж |
| фиолетовый | purple | пёпл |
| розовый | pink | пик |
| коричневый | brown | бра́ун |
| чёрный | black | блэк |
| белый | white | уáйт |
| серый | grey | грэй |

### 📝 Примеры:

- **The apple is red.** — Яблоко красное.
- **The sky is blue.** — Небо синее.
- **The grass is green.** — Трава зелёная.
- **My favourite color is yellow.** — Мой любимый цвет — жёлтый.

### ❓ Вопросы и ответы:

- **What color is it?** — Какого это цвета?
- **It is red.** — Оно красное.
- **What is your favourite color?** — Какой твой любимый цвет?
- **My favourite color is blue.** — Мой любимый цвет — синий.

### 💡 Интересные факты:

- **Orange** — это и цвет, и фрукт!
- **Black + white = grey**
- **Blue + yellow = green**`,
        ["Red apple, Blue sky, Green grass", "What color is it? — It is red", "My favourite color is..."],
        ["Orange — и цвет, и фрукт", "RGB = Red, Green, Blue (цифровые цвета", "В радуге 7 цветов: red, orange, yellow, green, blue, indigo, violet"]),
        L("Урок 8: Shapes", "Фигуры.", [
          "Circle, square, triangle",
          "Rectangle, oval",
          "Найти фигуры",
          "Нарисовать фигуры"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson8.svg",
        `## 📐 Shapes (Фигуры)

Геометрические фигуры в английском языке.

### 📚 Basic Shapes:

| Фигура | Английский | Транскрипция |
|--------|------------|--------------|
| круг | circle | сёкл |
| квадрат | square | сквэа |
| треугольник | triangle | трáйэнгл |
| прямоугольник | rectangle | рéктэнгл |
| овал | oval | óувл |
| ромб | diamond | dáймонд |
| звезда | star | ста |
| сердце | heart | хаат |

### 📝 Примеры:

- **It is a circle.** — Это круг.
- **It is a square.** — Это квадрат.
- **The box is square.** — Коробка квадратная.
- **The ball is round.** — Мяч круглый.

### 🔢 Сравнения:

| Фигура | Сколько сторон? |
|--------|-----------------|
| Triangle | 3 sides |
| Square | 4 sides |
| Rectangle | 4 sides |

### 📝 Описание фигур:

- **A circle has no corners.** — У круга нет углов.
- **A square has 4 equal sides.** — У квадрата 4 равные стороны.
- **A rectangle has 4 sides.** — У прямоугольника 4 стороны.

### 💡 Интересные факты:

- «Triangle» = tri (три) + angle (угол)
- Круг — единственная фигура без углов
- Квадрат — это особый прямоугольник`,
        ["Circle = круг, Square = квадрат", "Triangle = три угла", "A square has 4 sides"],
        ["Triangle = tri (три) + angle (угол)", "Circle — единственная фигура без углов", "Diamond — алмаз и ромб"])
      ]
    },
    {
      topic: "Family and People",
      lessons: [
        L("Урок 9: Family Members", "Члены семьи.", [
          "Mother, father, sister, brother",
          "Grandmother, grandfather",
          "Описать семью",
          "Нарисовать семейное дерево"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson9.svg",
        `## 👨‍👩‍👧‍👦 Family Members (Члены семьи)

Семья — это самые близкие люди. Выучи названия членов семьи!

### 📚 Close Family:

| Русский | Английский | Транскрипция |
|---------|------------|--------------|
| мама | mother / mom | máзэ / мом |
| папа | father / dad | fáзэ / дэд |
| сестра | sister | сúстэ |
| брат | brother | брáзэ |
| бабушка | grandmother / grandma | грэндмáзэ / грэндма |
| дедушка | grandfather / grandpa | грэндфáзэ / грэндпа |

### 📚 Extended Family:

| Русский | Английский |
|---------|------------|
| тётя | aunt |
| дядя | uncle |
| двоюродный брат/сестра | cousin |
| племянник | nephew |
| племянница | niece |

### 📝 Примеры:

- **This is my mother.** — Это моя мама.
- **I have a brother.** — У меня есть брат.
- **She is my sister.** — Она моя сестра.
- **My grandmother is kind.** — Моя бабушка добрая.

### ❓ Вопросы:

- **Do you have a sister?** — У тебя есть сестра?
- **Yes, I have a sister.** — Да, у меня есть сестра.
- **No, I don't have a sister.** — Нет, у меня нет сестры.

### 🌳 Family Tree:

Grandmother + Grandfather → Mother + Father → I + Brother/Sister

Или в виде схемы:
- Grandmother и Grandfather (бабушка и дедушка)
  - Mother и Father (мама и папа)
    - I (я) и Brother/Sister (брат/сестра)`,
        ["Mother = мама, Father = папа", "Sister = сестра, Brother = брат", "I have a big family"],
        ["«Grand» означает «пра-» или «старший»", "Mom, Dad — разговорные формы", "Cousin — двоюродный брат или сестра"]),
        L("Урок 10: Describing People", "Описание людей.", [
          "Tall, short, young, old",
          "Hair: long, short, curly",
          "Eyes: blue, brown, green",
          "Описать друга"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson10.svg",
        `## 👤 Describing People (Описание людей)

Чтобы описать человека, используем прилагательные.

### 📚 Height (Рост):

| Русский | Английский | Пример |
|---------|------------|--------|
| высокий | tall | He is tall. |
| низкий | short | She is short. |
| среднего роста | medium height | He is medium height. |

### 📚 Age (Возраст):

| Русский | Английский | Пример |
|---------|------------|--------|
| молодой | young | She is young. |
| старый | old | He is old. |

### 📚 Hair (Волосы):

| Русский | Английский |
|---------|------------|
| длинные | long hair |
| короткие | short hair |
| кудрявые | curly hair |
| прямые | straight hair |
| тёмные | dark hair |
| светлые | fair hair |
| рыжие | red hair |

### 📚 Eyes (Глаза):

| Русский | Английский |
|---------|------------|
| синие глаза | blue eyes |
| карие глаза | brown eyes |
| зелёные глаза | green eyes |
| серые глаза | grey eyes |

### 📝 Примеры описания:

- **She has long dark hair.** — У неё длинные тёмные волосы.
- **He has blue eyes.** — У него синие глаза.
- **He is tall and young.** — Он высокий и молодой.
- **She is short with curly hair.** — Она низкая с кудрявыми волосами.

### 💡 Грамматика:

**To have (иметь):**
- I have — у меня есть
- He/She has — у него/неё есть`,
        ["He is tall. She is short.", "Long hair, Short hair, Curly hair", "Blue eyes, Brown eyes, Green eyes"],
        ["He has, She has (не have!)", "Волосы — всегда hair (не hairs!)", "Eyes — всегда множественное число"]),
        L("Урок 11: Body Parts", "Части тела.", [
          "Head, shoulders, knees, toes",
          "Eyes, ears, nose, mouth",
          "Спеть песенку",
          "Показать на себе"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson11.svg",
        `## 🫀 Body Parts (Части тела)

Знание частей тела помогает описывать людей и говорить о здоровье.

### 📚 Head and Face (Голова и лицо):

| Русский | Английский | Транскрипция |
|---------|------------|--------------|
| голова | head | хед |
| лицо | face | фейс |
| глаз (глаза) | eye (eyes) | ай (айз) |
| ухо (уши) | ear (ears) | иэ (иэз) |
| нос | nose | нóуз |
| рот | mouth | ма́ус |
| зуб (зубы) | tooth (teeth) | ту́с (ти́с) |
| волосы | hair | хэа |

### 📚 Body (Тело):

| Русский | Английский |
|---------|------------|
| плечо | shoulder |
| рука | arm |
| кисть | hand |
| палец (руки) | finger |
| нога | leg |
| ступня | foot (feet) |
| палец (ноги) | toe |
| колено | knee |

### 🎵 Song: «Head, Shoulders, Knees and Toes»

«Head, shoulders, knees and toes, knees and toes
Head, shoulders, knees and toes, knees and toes
And eyes and ears and mouth and nose
Head, shoulders, knees and toes, knees and toes!»

### 📝 Примеры:

- **I have two eyes.** — У меня два глаза.
- **My nose is small.** — Мой нос маленький.
- **Touch your head.** — Дотронься до головы.
- **Clap your hands.** — Хлопни в ладоши.

### 💡 Множественное число:

- foot → feet (нога → ноги)
- tooth → teeth (зуб → зубы)`,
        ["Head, shoulders, knees, toes", "Eyes, ears, nose, mouth", "Hand = кисть, Arm = рука"],
        ["Foot → feet, Tooth → teeth (исключения)", "Hair — всегда единственное число", "Песня про части тела — самая известная детская песня"]),
        L("Урок 12: Clothes", "Одежда.", [
          "Shirt, dress, pants, skirt",
          "Hat, coat, shoes, socks",
          "Описать одежду",
          "Что ты носишь?"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson12.svg",
        `## 👕 Clothes (Одежда)

Одежда помогает нам описывать людей и говорить о моде.

### 📚 Upper Body (Верхняя часть):

| Русский | Английский |
|---------|------------|
| рубашка | shirt |
| футболка | T-shirt |
| свитер | sweater |
| куртка | jacket |
| пальто | coat |
| шапка | hat |
| платье | dress |

### 📚 Lower Body (Нижняя часть):

| Русский | Английский |
|---------|------------|
| брюки | pants / trousers |
| джинсы | jeans |
| юбка | skirt |
| шорты | shorts |

### 📚 Footwear (Обувь):

| Русский | Английский |
|---------|------------|
| обувь | shoes |
| ботинки | boots |
| носки | socks |
| кроссовки | sneakers |

### 📝 Примеры:

- **I am wearing a blue shirt.** — Я ношу синюю рубашку.
- **She is wearing a red dress.** — Она в красном платье.
- **Put on your hat.** — Надень шапку.
- **Take off your shoes.** — Сними обувь.

### ❓ Вопросы:

- **What are you wearing?** — Что на тебе надето?
- **I am wearing a T-shirt and jeans.** — На мне футболка и джинсы.

### 💡 Грамматика:

**To wear (носить):**
- I am wearing — я ношу (сейчас)
- wear — носить (вообще)`,
        ["Shirt = рубашка, Dress = платье", "Pants = брюки, Skirt = юбка", "Shoes = обувь, Socks = носки"],
        ["Pants, Jeans, Shorts — всегда множественное число", "«Put on» = надеть, «Take off» = снять", "I am wearing = Я сейчас ношу"])
      ]
    },
    {
      topic: "Animals and Nature",
      lessons: [
        L("Урок 13: Pets", "Домашние питомцы.", [
          "Cat, dog, fish, hamster",
          "Bird, rabbit, turtle",
          "Описать питомца",
          "У кого есть питомец?"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson13.svg",
        `## 🐱 Pets (Домашние питомцы)

Питомцы — это наши любимцы! Выучи названия животных.

### 📚 Common Pets:

| Русский | Английский | Транскрипция |
|---------|------------|--------------|
| кошка | cat | кэт |
| собака | dog | дог |
| рыбка | fish | фиш |
| хомяк | hamster | хáмстэ |
| птица | bird | бёд |
| кролик | rabbit | рэбит |
| черепаха | turtle | тётл |
| попугай | parrot | пэрот |
| морская свинка | guinea pig | гúни пиг |

### 📝 Примеры:

- **I have a cat.** — У меня есть кошка.
- **My dog is big.** — Моя собака большая.
- **She has a fish.** — У неё есть рыбка.
- **Do you have a pet?** — У тебя есть питомец?

### ❓ Вопросы и ответы:

- **Do you have a pet?** — У тебя есть питомец?
- **Yes, I have a cat.** — Да, у меня есть кошка.
- **No, I don't have a pet.** — Нет, у меня нет питомца.

### 🗣️ Описание питомца:

- **My cat is white.** — Моя кошка белая.
- **My dog is small.** — Моя собака маленькая.
- **My fish is orange.** — Моя рыбка оранжевая.
- **My hamster is cute.** — Мой хомяк милый.

### 💡 Sounds Animals Make:

- Cat: Meow! 🐱
- Dog: Woof! 🐕
- Bird: Tweet! 🐦`,
        ["Cat = кошка, Dog = собака", "I have a cat. Do you have a pet?", "My cat is white and small."],
        ["Fish — множественное число = fish", "Guinea pig — не свинка, а морская свинка", "Кошки говорят «meow», собаки — «woof»"]),
        L("Урок 14: Wild Animals", "Дикие животные.", [
          "Lion, tiger, elephant, bear",
          "Monkey, giraffe, zebra",
          "Где они живут?",
          "Описать животное"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson14.svg",
        `## 🦁 Wild Animals (Дикие животные)

Дикие животные живут в лесах, джунглях и саваннах.

### 📚 Wild Animals:

| Русский | Английский | Транскрипция |
|---------|------------|--------------|
| лев | lion | лáйен |
| тигр | tiger | тáйгэ |
| слон | elephant | элифант |
| медведь | bear | бэа |
| обезьяна | monkey | мáнки |
| жираф | giraffe | джиráf |
| зебра | zebra | зéбрэ |
| волк | wolf | вульф |
| лиса | fox | фокс |
| заяц | hare | хэа |
| олень | deer | диэ |
| крокодил | crocodile | крóкодайл |

### 📝 Примеры:

- **The lion is big.** — Лев большой.
- **Elephants are strong.** — Слоны сильные.
- **A tiger has stripes.** — У тигра полосы.
- **Giraffes are tall.** — Жирафы высокие.

### 🌍 Where do they live?

- **Lions live in Africa.** — Львы живут в Африке.
- **Bears live in the forest.** — Медведи живут в лесу.
- **Penguins live in Antarctica.** — Пингвины живут в Антарктиде.

### 💡 Интересные факты:

- **Lion** — царь зверей (King of the jungle)
- **Elephant** — самое большое наземное животное
- **Giraffe** — самое высокое животное`,
        ["Lion = лев, Tiger = тигр, Bear = медведь", "Elephant = слон, Giraffe = жираф", "Lions live in Africa."],
        ["Lion — царь зверей", "Elephant — самое большое животное", "Giraffe — самое высокое животное"]),
        L("Урок 15: Farm Animals", "Домашние животные.", [
          "Cow, pig, sheep, horse",
          "Chicken, duck, goat",
          "Что они дают?",
          "Звуки животных"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson15.svg",
        `## 🐄 Farm Animals (Домашние животные)

Домашние животные живут на ферме и приносят пользу человеку.

### 📚 Farm Animals:

| Русский | Английский | Транскрипция |
|---------|------------|--------------|
| корова | cow | ка́у |
| свинья | pig | пиг |
| овца | sheep | ши́п |
| лошадь | horse | хо́с |
| курица | chicken | чúкен |
| утка | duck | дак |
| коза | goat | гóут |
| петух | rooster | рýстэ |
| гусь | goose | гус |

### 📝 Что дают животные:

| Животное | Что даёт |
|----------|----------|
| Cow | milk (молоко) |
| Chicken | eggs (яйца) |
| Sheep | wool (шерсть) |
| Duck | eggs, meat |
| Goose | eggs, meat |

### 📝 Примеры:

- **Cows give milk.** — Коровы дают молоко.
- **Chickens lay eggs.** — Курицы несут яйца.
- **Sheep give wool.** — Овцы дают шерсть.
- **Horses can run fast.** — Лошади могут быстро бегать.

### 🗣️ Звуки животных:

| Животное | Звук (русский) | Звук (английский) |
|----------|----------------|-------------------|
| Cow | Му! | Moo! |
| Pig | Хрю! | Oink! |
| Duck | Кря! | Quack! |
| Chicken | Ко-ко! | Cluck! |
| Horse | Иго-го! | Neigh! |
| Sheep | Бе! | Baa! |

### 💡 Интересные факты:

- Sheep — множественное число от sheep (одинаково!)
- Goose → Geese (гусь → гуси)`,
        ["Cow = корова, Pig = свинья, Horse = лошадь", "Cows give milk. Chickens lay eggs.", "Moo, Oink, Quack, Neigh"],
        ["Sheep — одинаково в единственном и множественном числе", "Goose → Geese (исключение)", "На ферме много животных = farm animals"]),
        L("Урок 16: Weather", "Погода.", [
          "Sunny, rainy, cloudy, windy",
          "Snowy, hot, cold, warm",
          "Какая сегодня погода?",
          "Одежда по погоде"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson16.svg",
        `## 🌤️ Weather (Погода)

Погода влияет на нашу одежду и планы. Выучи слова о погоде!

### 📚 Weather Words:

| Русский | Английский | Транскрипция |
|---------|------------|--------------|
| солнечно | sunny | сáни |
| дождливо | rainy | рéйни |
| облачно | cloudy | клáуди |
| ветрено | windy | вúнди |
| снежно | snowy | снóуи |
| туманно | foggy | фóги |

### 📚 Temperature:

| Русский | Английский |
|---------|------------|
| жарко | hot |
| холодно | cold |
| тепло | warm |
| прохладно | cool |

### 📝 Примеры:

- **It is sunny today.** — Сегодня солнечно.
- **It is rainy.** — Дождливо.
- **It is cold in winter.** — Зимой холодно.
- **It is hot in summer.** — Летом жарко.

### ❓ Вопросы:

- **What is the weather like today?** — Какая сегодня погода?
- **It is sunny and warm.** — Солнечно и тепло.
- **Is it cold?** — Холодно?
- **Yes, it is cold.** — Да, холодно.

### 👕 Одежда по погоде:

| Погода | Одежда |
|--------|--------|
| sunny | T-shirt, sunglasses |
| rainy | raincoat, umbrella |
| cold | coat, hat, gloves |
| snowy | warm jacket, boots |

### 💡 Seasons:

- **Spring** — весна
- **Summer** — лето
- **Autumn / Fall** — осень
- **Winter** — зима`,
        ["Sunny = солнечно, Rainy = дождливо", "What is the weather like today?", "It is sunny and warm."],
        ["Sunny, Rainy — добавляем -y к существительным", "Umbrella — зонтик, Raincoat — дождевик", "What's the weather like? — стандартный вопрос"])
      ]
    },
    {
      topic: "Food and Drinks",
      lessons: [
        L("Урок 17: Fruits and Vegetables", "Фрукты и овощи.", [
          "Apple, banana, orange",
          "Carrot, potato, tomato",
          "Что ты любишь?",
          "I like... / I don't like..."
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson17.svg",
        `## 🍎 Fruits and Vegetables (Фрукты и овощи)

Фрукты и овощи полезны для здоровья!

### 📚 Fruits (Фрукты):

| Русский | Английский | Транскрипция |
|---------|------------|--------------|
| яблоко | apple | эпл |
| банан | banana | банáна |
| апельсин | orange | óриндж |
| лимон | lemon | лéмон |
| груша | pear | пэа |
| виноград | grapes | грéйпс |
| клубника | strawberry | стрóбери |
| арбуз | watermelon | вóтэmelon |

### 📚 Vegetables (Овощи):

| Русский | Английский | Транскрипция |
|---------|------------|--------------|
| морковь | carrot | кэрот |
| картофель | potato | потéйтоу |
| помидор | tomato | томáтоу |
| огурец | cucumber | кьюкáмбэ |
| капуста | cabbage | кэбидж |
| лук | onion | áниан |

### 📝 Выражаем предпочтения:

- **I like apples.** — Я люблю яблоки.
- **I don't like carrots.** — Я не люблю морковь.
- **Do you like bananas?** — Ты любишь бананы?
- **Yes, I do. / No, I don't.** — Да. / Нет.

### 🗣️ Вопросы:

- **What is your favourite fruit?** — Какой твой любимый фрукт?
- **My favourite fruit is apple.** — Мой любимый фрукт — яблоко.

### 💡 Интересные факты:

- Tomato — это и фрукт, и овощ (научно — фрукт!)
- Banana — самый популярный фрукт в мире
- Strawberry — клубника (berry = ягода)`,
        ["Apple, Banana, Orange = фрукты", "Carrot, Potato, Tomato = овощи", "I like apples. I don't like carrots."],
        ["Tomato — и фрукт, и овощ", "Banana — самый популярный фрукт", "Grapes — всегда множественное число"]),
        L("Урок 18: Food", "Еда.", [
          "Bread, cheese, meat, fish",
          "Rice, pasta, soup, salad",
          "Что на обед?",
          "Составить меню"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson18.svg",
        `## 🍞 Food (Еда)

Еда даёт нам энергию. Выучи названия продуктов!

### 📚 Basic Food:

| Русский | Английский | Транскрипция |
|---------|------------|--------------|
| хлеб | bread | бред |
| сыр | cheese | чиз |
| мясо | meat | мит |
| рыба | fish | фиш |
| яйцо | egg | эг |
| рис | rice | райс |
| макароны | pasta | пáста |
| суп | soup | суп |
| салат | salad | сэлэд |
| бутерброд | sandwich | сэндвич |
| пицца | pizza | пúца |
| бургер | burger | бёгэ |

### 📚 Meals (Приёмы пищи):

| Русский | Английский |
|---------|------------|
| завтрак | breakfast |
| обед | lunch |
| ужин | dinner |

### 📝 Примеры:

- **I have breakfast at 8 o'clock.** — Я завтракаю в 8 часов.
- **What's for lunch?** — Что на обед?
- **I eat soup for lunch.** — Я ем суп на обед.
- **I like pizza.** — Я люблю пиццу.

### ❓ Вопросы:

- **What do you eat for breakfast?** — Что ты ешь на завтрак?
- **I eat eggs and toast.** — Я ем яйца и тосты.

### 💡 Полезные фразы:

- **I'm hungry.** — Я голоден.
- **I'm thirsty.** — Я хочу пить.
- **Let's have lunch!** — Давай пообедаем!`,
        ["Bread = хлеб, Cheese = сыр, Meat = мясо", "Breakfast, Lunch, Dinner", "What do you eat for breakfast?"],
        ["Breakfast = break + fast (прервать голод)", "Lunch — обед, Dinner — ужин", "Sandwich назван в честь графа Сэндвича"]),
        L("Урок 19: Drinks", "Напитки.", [
          "Water, milk, juice, tea",
          "Coffee, soda",
          "Что ты пьёшь?",
          "В кафе"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson19.svg",
        `## 🥤 Drinks (Напитки)

Напитки утоляют жажду. Выучи их названия!

### 📚 Common Drinks:

| Русский | Английский | Транскрипция |
|---------|------------|--------------|
| вода | water | вóтэ |
| молоко | milk | милк |
| сок | juice | джу́с |
| чай | tea | ти |
| кофе | coffee | кóфи |
| лимонад | soda / lemonade | сóда / лемонéйд |
| какао | hot chocolate | хот шоколéт |

### 📚 Types of Juice:

| Русский | Английский |
|---------|------------|
| апельсиновый сок | orange juice |
| яблочный сок | apple juice |
| томатный сок | tomato juice |

### 📝 Примеры:

- **I drink water.** — Я пью воду.
- **I like orange juice.** — Я люблю апельсиновый сок.
- **Do you like tea?** — Ты любишь чай?
- **Yes, I do. / No, I don't.** — Да. / Нет.

### ❓ Вопросы:

- **What do you drink?** — Что ты пьёшь?
- **I drink milk.** — Я пью молоко.
- **Would you like some tea?** — Хочешь чаю?
- **Yes, please. / No, thank you.** — Да, пожалуйста. / Нет, спасибо.

### 💡 Вежливые фразы:

- **I'm thirsty.** — Я хочу пить.
- **Can I have some water?** — Можно воды?
- **Here you are.** — Вот, пожалуйста.`,
        ["Water = вода, Milk = молоко, Juice = сок", "Tea = чай, Coffee = кофе", "I drink water. I like juice."],
        ["«Would you like...?» — вежливое предложение", "«Yes, please» — да, пожалуйста", "«No, thank you» — нет, спасибо"]),
        L("Урок 20: At the Cafe", "В кафе.", [
          "Can I have...?",
          "Here you are",
          "Thank you",
          "Диалог в кафе"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson20.svg",
        `## 🍽️ At the Cafe (В кафе)

Как заказать еду и напитки в кафе на английском.

### 📚 Полезные фразы:

| Русский | Английский |
|---------|------------|
| Можно мне...? | Can I have...? |
| Я бы хотел... | I would like... |
| Вот, пожалуйста | Here you are |
| Спасибо | Thank you |
| Пожалуйста | You're welcome |
| Сколько стоит? | How much is it? |
| Меню, пожалуйста | Menu, please |

### 📝 Примеры заказов:

- **Can I have a pizza, please?** — Можно мне пиццу, пожалуйста?
- **I would like an orange juice.** — Я бы хотел апельсиновый сок.
- **Can I have the menu?** — Можно меню?

### 🗣️ Диалог в кафе:

**Waiter:** Hello! Can I help you?
**Customer:** Yes, please. Can I have a sandwich?
**Waiter:** Here you are.
**Customer:** Thank you. How much is it?
**Waiter:** It's 5 dollars.
**Customer:** Here you are.
**Waiter:** Thank you. Have a nice day!

### 📚 Счёт и оплата:

| Русский | Английский |
|---------|------------|
| Счёт, пожалуйста | The bill, please |
| Наличные | cash |
| Карта | card |
| Сдача | change |

### 💡 Вежливость:

Всегда говори «please» и «thank you»!
- **Can I have... please?**
- **Thank you!**
- **You're welcome!**`,
        ["Can I have a pizza, please?", "How much is it?", "Thank you! You're welcome!"],
        ["«Please» и «Thank you» — обязательны в английском", "«Can I have...?» = Можно мне...?", "«How much is it?» = Сколько это стоит?"])
      ]
    },
    {
      topic: "Daily Routine",
      lessons: [
        L("Урок 21: Time", "Время.", [
          "What time is it?",
          "o'clock, half past",
          "It's 3 o'clock",
          "Режим дня"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson21.svg",
        `## ⏰ Time (Время)

Умение говорить о времени важно для ежедневной жизни.

### 📚 Как спросить время:

- **What time is it?** — Сколько времени?
- **What's the time?** — Который час?

### 📚 Full Hours (Целые часы):

- **It's one o'clock.** — Один час.
- **It's two o'clock.** — Два часа.
- **It's twelve o'clock.** — Двенадцать часов.

### 📚 Half Past (Половина):

- **It's half past one.** — Половина второго (1:30).
- **It's half past three.** — Половина четвёртого (3:30).

### 📚 Quarter (Четверть):

- **It's quarter past two.** — Четверть третьего (2:15).
- **It's quarter to three.** — Без четверти три (2:45).

### 📚 Minutes (Минуты):

- **It's ten past three.** — Десять минут четвёртого (3:10).
- **It's twenty to four.** — Без двадцати четыре (3:40).

### 📝 Таблица:

| Время | Английский |
|-------|------------|
| 1:00 | one o'clock |
| 1:15 | quarter past one |
| 1:30 | half past one |
| 1:45 | quarter to two |
| 2:00 | two o'clock |

### 💡 Интересные факты:

- **o'clock** = of the clock
- **past** = после (прошло)
- **to** = до (осталось)`,
        ["What time is it? — It's 3 o'clock.", "Half past one = 1:30", "Quarter past = 15 минут после"],
        ["o'clock — только для целых часов", "В США часто говорят 1:30 как «one thirty»", "a.m. = утра, p.m. = после полудня"]),
        L("Урок 22: Daily Activities", "Ежедневные дела.", [
          "Wake up, get up, wash",
          "Have breakfast, go to school",
          "Describe your day",
          "Приёмы пищи"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson22.svg",
        `## 🌅 Daily Activities (Ежедневные дела)

Расскажем о своём распорядке дня!

### 📚 Morning (Утро):

| Русский | Английский |
|---------|------------|
| просыпаться | wake up |
| вставать | get up |
| умываться | wash |
| чистить зубы | brush teeth |
| одеваться | get dressed |
| завтракать | have breakfast |
| идти в школу | go to school |

### 📚 Day (День):

| Русский | Английский |
|---------|------------|
| быть в школе | be at school |
| обедать | have lunch |
| делать уроки | do homework |
| играть | play |

### 📚 Evening (Вечер):

| Русский | Английский |
|---------|------------|
| ужинать | have dinner |
| смотреть ТВ | watch TV |
| читать книгу | read a book |
| ложиться спать | go to bed |

### 📝 Распорядок дня:

- **I wake up at 7 o'clock.** — Я просыпаюсь в 7 часов.
- **I have breakfast at 8 o'clock.** — Я завтракаю в 8 часов.
- **I go to school at 9 o'clock.** — Я иду в школу в 9 часов.
- **I go to bed at 10 o'clock.** — Я ложусь спать в 10 часов.

### 💡 Грамматика:

**Present Simple** (обычно делаю):
- I wake up, I go, I have

### 🗣️ Вопросы:

- **What time do you get up?** — Во сколько ты встаёшь?
- **I get up at 7 o'clock.** — Я встаю в 7 часов.`,
        ["Wake up = просыпаться, Get up = вставать", "Have breakfast, Have lunch, Have dinner", "I wake up at 7 o'clock."],
        ["Wake up ≠ get up (проснуться ≠ встать)", "Do homework — делать домашку", "Go to bed — ложиться спать"]),
        L("Урок 23: Days of Week", "Дни недели.", [
          "Monday, Tuesday, Wednesday...",
          "Sunday is the first day",
          "Что ты делаешь в...?",
          "Расписание"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson23.svg",
        `## 📅 Days of Week (Дни недели)

В неделе 7 дней. Выучи их названия!

### 📚 Days of Week:

| Русский | Английский | Транскрипция |
|---------|------------|--------------|
| понедельник | Monday | мáнди |
| вторник | Tuesday | тью́зди |
| среда | Wednesday | вéнзди |
| четверг | Thursday | сё́зди |
| пятница | Friday | фрáйди |
| суббота | Saturday | сэ́тэди |
| воскресенье | Sunday | сáнди |

### 📝 Особенности:

- Все дни пишутся с **большой буквы**!
- Каждый день заканчивается на **-day**
- **Sunday** — первый день недели в Англии и США

### 📝 Примеры:

- **Today is Monday.** — Сегодня понедельник.
- **Tomorrow is Tuesday.** — Завтра вторник.
- **What day is it today?** — Какой сегодня день?

### ❓ Вопросы и ответы:

- **What do you do on Monday?** — Что ты делаешь в понедельник?
- **I go to school on Monday.** — Я иду в школу в понедельник.

### 📚 Weekdays vs Weekend:

| Weekdays (будни) | Weekend (выходные) |
|------------------|-------------------|
| Monday | Saturday |
| Tuesday | Sunday |
| Wednesday | |
| Thursday | |
| Friday | |

### 💡 Интересные факты:

- Monday = Moon day (день луны)
- Sunday = Sun day (день солнца)
- Weekend — любимое время всех!`,
        ["Monday, Tuesday, Wednesday, Thursday, Friday", "Saturday, Sunday = weekend", "What day is it today?"],
        ["Дни недели пишутся с большой буквы", "Sunday — первый день в Англии и США", "Weekdays = будни, Weekend = выходные"]),
        L("Урок 24: Months and Seasons", "Месяцы и сезоны.", [
          "January, February, March...",
          "Winter, spring, summer, autumn",
          "Какой сейчас месяц?",
          "Любимое время года"
        ], "/school-curriculum-app/images/lessons/grade3/english/lesson24.svg",
        `## 📆 Months and Seasons (Месяцы и сезоны)

В году 12 месяцев и 4 сезона.

### 📚 Months (Месяцы):

| Русский | Английский | Транскрипция |
|---------|------------|--------------|
| январь | January | джэньюэри |
| февраль | February | фебруэри |
| март | March | мач |
| апрель | April | эйприл |
| май | May | мэй |
| июнь | June | джун |
| июль | July | джулáй |
| август | August | óгест |
| сентябрь | September | сэптéмбэ |
| октябрь | October | окtóубэ |
| ноябрь | November | нувéмбэ |
| декабрь | December | дисéмбэ |

### 📚 Seasons (Сезоны):

| Русский | Английский | Месяцы |
|---------|------------|--------|
| зима | winter | December, January, February |
| весна | spring | March, April, May |
| лето | summer | June, July, August |
| осень | autumn / fall | September, October, November |

### 📝 Примеры:

- **My birthday is in May.** — Мой день рождения в мае.
- **It is cold in winter.** — Зимой холодно.
- **I like summer.** — Я люблю лето.
- **What month is it now?** — Какой сейчас месяц?

### ❓ Вопросы:

- **What is your favourite season?** — Какое твоё любимое время года?
- **My favourite season is summer.** — Моё любимое время года — лето.
- **When is your birthday?** — Когда твой день рождения?
- **My birthday is in June.** — Мой день рождения в июне.

### 💡 Интересные факты:

- Все месяцы пишутся с большой буквы
- Autumn — британский, Fall — американский
- September = septem (7), October = octo (8) — от латинских чисел`,
        ["January, February, March, April, May...", "Winter, Spring, Summer, Autumn", "My birthday is in May."],
        ["Месяцы пишутся с большой буквы", "Autumn (UK) = Fall (US)", "September, October, November, December — от латинских чисел"])
      ]
    }
  ]
}

export const games: GameLesson[] = [
  {
    title: "Numbers in English",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Как будет «5» на английском?", options: ["four", "five", "six", "Никто не знает", "Не знаю"], correctAnswer: "five", hint: "1-one, 2-two, 3-three, 4-four, 5-?" },
      { type: 'quiz', question: "Как будет «12» на английском?", options: ["twelve", "twenty", "two", "Никто не знает", "Не знаю"], correctAnswer: "twelve", hint: "11-eleven, 12-?" },
      { type: 'quiz', question: "«25» по-английски: twenty-__", options: ["five", "four", "six", "seven", "eight", "nine"], correctAnswer: "five", hint: "25 = twenty-five" },
      { type: 'quiz', question: "Какое число «seventeen»?", options: ["16", "17", "18", "Никто не знает", "Не знаю"], correctAnswer: "17", hint: "Seven + teen = seventeen" },
      { type: 'quiz', question: "Как будет «100» на английском?", options: ["a hundred", "one hundred", "ten ten", "Никто не знает", "Не знаю"], correctAnswer: "one hundred", hint: "100 = one hundred" }
    ],
    reward: { stars: 3, message: "Great! You know numbers! 🔢" }
  },
  {
    title: "Colors in English",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Как будет «красный» на английском?", options: ["red", "blue", "green", "Никто не знает", "Не знаю"], correctAnswer: "red", hint: "Apple is red" },
      { type: 'quiz', question: "Какой цвет «yellow»?", options: ["жёлтый", "зелёный", "синий", "Никто не знает", "Не знаю"], correctAnswer: "жёлтый", hint: "Sun is yellow" },
      { type: 'find', question: "Выбери названия цветов:", options: ["Red", "Cat", "Blue", "Green", "Dog", "Yellow"], correctAnswer: ["Red", "Blue", "Green", "Yellow"], hint: "Colors are: red, blue, green, yellow..." },
      { type: 'quiz', question: "Как будет «оранжевый»?", options: ["orange", "purple", "pink", "Никто не знает", "Не знаю"], correctAnswer: "orange", hint: "Orange fruit is orange!" },
      { type: 'quiz', question: "Как будет «чёрный» на английском?", options: ["white", "brown", "black", "Никто не знает", "Не знаю"], correctAnswer: "black", hint: "Ночь — чёрная, night is black" },
      { type: 'quiz', question: "Какой цвет «brown»?", options: ["красный", "коричневый", "серый", "Никто не знает", "Не знаю"], correctAnswer: "коричневый", hint: "Chocolate is brown 🍫" }
    ],
    reward: { stars: 3, message: "Excellent! You know colors! 🎨" }
  },
  {
    title: "Family Members",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "«Mother» — это:", options: ["папа", "мама", "сестра", "Никто не знает", "Не знаю"], correctAnswer: "мама", hint: "Mother = мама" },
      { type: 'quiz', question: "Как будет «бабушка» на английском?", options: ["grandmother", "grandfather", "mother", "Никто не знает", "Не знаю"], correctAnswer: "grandmother", hint: "Grand + mother = grandmother" },
      { type: 'quiz', question: "Brother — это __", options: ["брат", "сестра", "отец", "мать", "дядя", "дедушка"], correctAnswer: "брат", hint: "Brother = брат, Sister = сестра" },
      { type: 'quiz', question: "«Father» — это:", options: ["отец", "дедушка", "брат", "Никто не знает", "Не знаю"], correctAnswer: "отец", hint: "Father = папа, отец" },
      { type: 'quiz', question: "Как будет «дядя» на английском?", options: ["aunt", "uncle", "cousin", "Никто не знает", "Не знаю"], correctAnswer: "uncle", hint: "Uncle = дядя, Aunt = тётя" }
    ],
    reward: { stars: 3, message: "Great! You know family! 👨‍👩‍👧‍👦" }
  },
  {
    title: "Animals in English",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Как будет «кошка» на английском?", options: ["dog", "cat", "bird", "Никто не знает", "Не знаю"], correctAnswer: "cat", hint: "Meow! 🐱" },
      { type: 'quiz', question: "«Dog» — это:", options: ["собака", "кошка", "лошадь", "Никто не знает", "Не знаю"], correctAnswer: "собака", hint: "Woof! 🐕" },
      { type: 'quiz', question: "Как будет «лев»?", options: ["tiger", "lion", "bear", "Никто не знает", "Не знаю"], correctAnswer: "lion", hint: "King of the jungle 🦁" },
      { type: 'quiz', question: "Elephant — это __", options: ["слон", "тигр", "медведь", "лев", "зебра", "обезьяна"], correctAnswer: "слон", hint: "Big grey animal with a trunk 🐘" },
      { type: 'quiz', question: "Как будет «лошадь» на английском?", options: ["cow", "horse", "pig", "Никто не знает", "Не знаю"], correctAnswer: "horse", hint: "Fast animal you can ride 🐴" }
    ],
    reward: { stars: 3, message: "Super! You know animals! 🐾" }
  },
  {
    title: "Food and Drinks",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "«Apple» — это:", options: ["апельсин", "яблоко", "банан", "Никто не знает", "Не знаю"], correctAnswer: "яблоко", hint: "Red or green fruit 🍎" },
      { type: 'quiz', question: "Как будет «хлеб» на английском?", options: ["bread", "water", "milk", "Никто не знает", "Не знаю"], correctAnswer: "bread", hint: "Bread 🍞" },
      { type: 'quiz', question: "«Water» — это:", options: ["молоко", "вода", "сок", "Никто не знает", "Не знаю"], correctAnswer: "вода", hint: "We drink water 💧" },
      { type: 'quiz', question: "Banana — это __", options: ["банан", "яблоко", "апельсин", "груша", "виноград", "арбуз"], correctAnswer: "банан", hint: "Yellow fruit 🍌" },
      { type: 'quiz', question: "Как будет «молоко» на английском?", options: ["juice", "water", "milk", "Никто не знает", "Не знаю"], correctAnswer: "milk", hint: "White drink from a cow 🥛" }
    ],
    reward: { stars: 3, message: "Excellent! You know food! 🍎" }
  },
  {
    title: "Days and Months",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Как будет «понедельник»?", options: ["Monday", "Sunday", "Friday", "Никто не знает", "Не знаю"], correctAnswer: "Monday", hint: "First day of the week" },
      { type: 'quiz', question: "«Sunday» — это:", options: ["суббота", "воскресенье", "понедельник", "Никто не знает", "Не знаю"], correctAnswer: "воскресенье", hint: "Last day of the week" },
      { type: 'quiz', question: "Какой месяц «January»?", options: ["февраль", "январь", "март", "Никто не знает", "Не знаю"], correctAnswer: "январь", hint: "First month of the year" },
      { type: 'quiz', question: "Как будет «лето»?", options: ["spring", "summer", "winter", "Никто не знает", "Не знаю"], correctAnswer: "summer", hint: "Hot season with holidays ☀️" },
      { type: 'quiz', question: "Какой месяц «December»?", options: ["октябрь", "ноябрь", "декабрь", "Никто не знает", "Не знаю"], correctAnswer: "декабрь", hint: "December — последний месяц года 🎄" }
    ],
    reward: { stars: 3, message: "Great! You know calendar! 📅" }
  },
  {
    title: "Body Parts",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "«Head» — это:", options: ["рука", "голова", "нога", "Никто не знает", "Не знаю"], correctAnswer: "голова", hint: "On your shoulders" },
      { type: 'quiz', question: "Как будет «глаза»?", options: ["ears", "eyes", "nose", "Никто не знает", "Не знаю"], correctAnswer: "eyes", hint: "Two eyes to see 👀" },
      { type: 'quiz', question: "Nose — это __", options: ["нос", "рот", "глаз", "ухо", "голова", "лицо"], correctAnswer: "нос", hint: "On your face, you breathe with it 👃" },
      { type: 'quiz', question: "«Hands» — это:", options: ["ноги", "руки", "уши", "Никто не знает", "Не знаю"], correctAnswer: "руки", hint: "You write with your hands ✋" },
      { type: 'quiz', question: "Как будет «нога» на английском?", options: ["arm", "leg", "hand", "Никто не знает", "Не знаю"], correctAnswer: "leg", hint: "You walk with your legs 🦵" }
    ],
    reward: { stars: 3, message: "Super! You know body parts! 🫀" }
  },
  {
    title: "Basic Phrases",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "«Hello» — это:", options: ["пока", "привет", "спасибо", "Никто не знает", "Не знаю"], correctAnswer: "привет", hint: "Greeting" },
      { type: 'quiz', question: "Как сказать «спасибо»?", options: ["Please", "Thank you", "Sorry", "Никто не знает", "Не знаю"], correctAnswer: "Thank you", hint: "When someone helps you" },
      { type: 'quiz', question: "«Goodbye» — это:", options: ["здравствуйте", "до свидания", "извините", "Никто не знает", "Не знаю"], correctAnswer: "до свидания", hint: "When you leave" },
      { type: 'quiz', question: "«Как дела?» — How __ you?", options: ["are", "is", "am", "do", "can", "have"], correctAnswer: "are", hint: "How are you?" },
      { type: 'quiz', question: "Как сказать «извините» по-английски?", options: ["Hello", "Please", "Sorry", "Никто не знает", "Не знаю"], correctAnswer: "Sorry", hint: "Мы говорим sorry, когда извиняемся" }
    ],
    reward: { stars: 3, message: "Excellent! You know phrases! 💬" }
  }
]
