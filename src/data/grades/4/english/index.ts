import { SubjectData, GameLesson, LessonItem } from '@/data/types'

const L = (
  title: string, 
  description: string, 
  tasks: string[],
  theory?: string,
  examples?: string[],
  facts?: string[]
): LessonItem => ({
  title,
  description,
  tasks,
  theory,
  examples,
  facts
})

export const lessons: SubjectData = {
  title: "Иностранный язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: ["Знакомство", "Мой мир", "Школа", "Семья", "Еда", "Путешествия"],
  detailedTopics: [
    {
      topic: "Знакомство и общение",
      lessons: [
        L("Урок 1: 👋 Приветствие", "Greetings — слова и фразы для приветствия на английском языке.", [
          "Приветствовать по-английски",
          "Прощаться",
          "Спрашивать «Как дела?»",
          "Отвечать на вопросы"
        ],
        `## 👋 Приветствие (Greetings)

### Основные приветствия

| Английский | Произношение | Русский |
|------------|--------------|---------|
| Hello! | хэ-лОу | Здравствуйте! |
| Hi! | хай | Привет! |
| Good morning! | гуд мОрнинг | Доброе утро! |
| Good afternoon! | гуд афтэрнУн | Добрый день! |
| Good evening! | гуд Ивнинг | Добрый вечер! |

### Прощание

| Английский | Произношение | Русский |
|------------|--------------|---------|
| Goodbye! | гудбАй | До свидания! |
| Bye! | бай | Пока! |
| See you! | си ю | Увидимся! |
| Good night! | гуд найт | Спокойной ночи! |

### Как дела?

**Вопрос:**
- How are you? — Как дела?

**Ответы:**
- I'm fine, thanks! — Хорошо, спасибо!
- I'm OK. — Нормально.
- Not bad. — Неплохо.
- I'm great! — Отлично!`,
        [
          "Hello! — Здравствуйте!",
          "Hi! How are you? — Привет! Как дела?",
          "I'm fine, thanks! — Хорошо, спасибо!"
        ],
        [
          "🗣️ Hello — самое популярное слово в мире",
          "🗣️ Hi — неформальное приветление для друзей",
          "🗣️ Англичане всегда спрашивают «How are you?», но не ждут подробного ответа"
        ]),
        L("Урок 2: 🙋 Представление", "Introducing yourself — как представиться и узнать имя собеседника.", [
          "Назвать своё имя",
          "Сказать, откуда ты",
          "Рассказать о возрасте",
          "Задавать вопросы"
        ],
        `## 🙋 Представление (Introducing yourself)

### Как представиться

| Английский | Русский |
|------------|---------|
| My name is... | Меня зовут... |
| I'm... | Я... |
| I am from... | Я из... |
| I am ... years old. | Мне ... лет. |

### Пример диалога

**— Hello! What is your name?**
*— Привет! Как тебя зовут?*

**— My name is Anna. And you?**
*— Меня зовут Анна. А тебя?*

**— I'm Tom. Nice to meet you!**
*— Я Том. Приятно познакомиться!*

**— Nice to meet you too! Where are you from?**
*— Мне тоже! Откуда ты?*

**— I'm from Russia.**
*— Я из России.*

### Вопросительные фразы

- What is your name? — Как тебя зовут?
- How old are you? — Сколько тебе лет?
- Where are you from? — Откуда ты?`,
        [
          "My name is Ivan. — Меня зовут Иван.",
          "I'm 10 years old. — Мне 10 лет.",
          "I'm from Moscow, Russia. — Я из Москвы, Россия."
        ],
        [
          "🙋 Nice to meet you говорят при знакомстве",
          "🙋 В английском имя называют сразу после приветствия",
          "🙋 Англичане часто сокращают I am до I'm"
        ]),
        L("Урок 3: 🙏 Вежливые слова", "Polite words — слова вежливости на английском языке.", [
          "Говорить «пожалуйста»",
          "Благодарить",
          "Извиняться",
          "Просить о помощи"
        ],
        `## 🙏 Вежливые слова (Polite words)

### Спасибо и пожалуйста

| Английский | Русский |
|------------|---------|
| Thank you! | Спасибо! |
| Thanks! | Спасибо! (неформально) |
| You're welcome! | Пожалуйста! (в ответ на спасибо) |
| Please | Пожалуйста (при просьбе) |

### Извинения

| Английский | Русский |
|------------|---------|
| Sorry! | Извините! |
| Excuse me! | Извините! (чтобы обратить внимание) |
| I'm sorry! | Мне жаль! |

### Примеры использования

**Просьба:**
- Can I have water, please? — Можно воды, пожалуйста?
- Please help me. — Пожалуйста, помоги мне.

**Благодарность:**
- Thank you very much! — Большое спасибо!
- Thanks a lot! — Огромное спасибо!

**Ответ на благодарность:**
- You're welcome! — Пожалуйста!
- No problem! — Не за что!`,
        [
          "Please help me. — Пожалуйста, помоги мне.",
          "Thank you very much! — Большое спасибо!",
          "Sorry, I'm late. — Извините, я опоздал."
        ],
        [
          "🙏 Please всегда ставится в конце просьбы",
          "🙏 Thank you — самое важное слово в английском",
          "🙏 Excuse me используют перед вопросом к незнакомцу"
        ]),
        L("Урок 4: ❓ Вопросительные слова", "Question words — слова для вопросов.", [
          "Задавать вопросы с What",
          "Задавать вопросы с Where",
          "Задавать вопросы с Who",
          "Отвечать на вопросы"
        ],
        `## ❓ Вопросительные слова (Question words)

### Основные вопросительные слова

| Слово | Произношение | Значение |
|-------|--------------|----------|
| What? | уот | Что? Какой? |
| Where? | уэа | Где? Куда? |
| Who? | ху | Кто? |
| When? | уэн | Когда? |
| Why? | уай | Почему? |
| How? | хау | Как? |

### Примеры вопросов

**What — Что / Какой:**
- What is this? — Что это?
- What is your name? — Как тебя зовут?
- What time is it? — Который час?

**Where — Где / Куда:**
- Where are you from? — Откуда ты?
- Where is the school? — Где школа?
- Where do you live? — Где ты живёшь?

**Who — Кто:**
- Who is that? — Кто это?
- Who is your friend? — Кто твой друг?

**How — Как:**
- How are you? — Как дела?
- How old are you? — Сколько тебе лет?`,
        [
          "What is your name? — Как тебя зовут?",
          "Where do you live? — Где ты живёшь?",
          "Who is your friend? — Кто твой друг?"
        ],
        [
          "❓ Вопросительные слова всегда стоят в начале вопроса",
          "❓ Who используется только про людей",
          "❓ How old — специальный вопрос о возрасте"
        ])
      ]
    },
    {
      topic: "Мой мир",
      lessons: [
        L("Урок 5: 🎨 Цвета", "Colours — названия цветов на английском языке.", [
          "Называть цвета",
          "Описывать предметы по цвету",
          "Говорить о любимом цвете",
          "Слушать и понимать"
        ],
        `## 🎨 Цвета (Colours)

### Основные цвета

| Английский | Произношение | Русский |
|------------|--------------|---------|
| red | ред | красный |
| orange | Ориндж | оранжевый |
| yellow | Йеллоу | жёлтый |
| green | гриин | зелёный |
| blue | блу | синий |
| purple | Пёпл | фиолетовый |
| pink | пинк | розовый |
| black | блэк | чёрный |
| white | уайт | белый |
| brown | браун | коричневый |
| grey | грэй | серый |

### Как сказать о цвете

**Вопрос:**
- What colour is it? — Какого это цвета?

**Ответ:**
- It is red. — Он красный.
- It's blue. — Он синий.

**О любимом цвете:**
- My favourite colour is green. — Мой любимый цвет — зелёный.
- I like blue. — Мне нравится синий.

### Описание предметов

- The apple is red. — Яблоко красное.
- The sky is blue. — Небо синее.
- The grass is green. — Трава зелёная.`,
        [
          "What colour is it? — It's red.",
          "My favourite colour is blue.",
          "The sun is yellow. The grass is green."
        ],
        [
          "🎨 Colour (брит.) = Color (амер.)",
          "🎨 Blue — самый популярный цвет в мире",
          "🎨 В английском цвета — прилагательные, ставятся после существительного"
        ]),
        L("Урок 6: 🔢 Числа", "Numbers — числа на английском языке.", [
          "Считать от 1 до 20",
          "Считать до 100",
          "Называть возраст",
          "Решать примеры"
        ],
        `## 🔢 Числа (Numbers)

### Числа 1-10

| Число | Английский | Произношение |
|-------|------------|--------------|
| 1 | one | уан |
| 2 | two | ту |
| 3 | three | сри |
| 4 | four | фо |
| 5 | five | файв |
| 6 | six | сикс |
| 7 | seven | сЕвн |
| 8 | eight | эйт |
| 9 | nine | найн |
| 10 | ten | тэн |

### Числа 11-20

| Число | Английский | Произношение |
|-------|------------|--------------|
| 11 | eleven | илЕвн |
| 12 | twelve | туЭлв |
| 13 | thirteen | сётИн |
| 14 | fourteen | фортИн |
| 15 | fifteen | фитИн |
| 16 | sixteen | сикстИн |
| 17 | seventeen | сэвнтИн |
| 18 | eighteen | эйтИн |
| 19 | nineteen | найнтИн |
| 20 | twenty | туЭнти |

### Десятки

- 30 — thirty
- 40 — forty
- 50 — fifty
- 60 — sixty
- 70 — seventy
- 80 — eighty
- 90 — ninety
- 100 — one hundred

### Математика на английском

- 5 + 3 = 8 — Five plus three is eight.
- 10 - 4 = 6 — Ten minus four is six.`,
        [
          "1, 2, 3, 4, 5 — one, two, three, four, five",
          "I am ten years old. — Мне десять лет.",
          "5 + 5 = 10 — Five plus five is ten."
        ],
        [
          "🔢 Числа 13-19 заканчиваются на -teen",
          "🔢 Десятки заканчиваются на -ty",
          "🔢 В английском двузначные числа пишутся через дефис: twenty-one"
        ]),
        L("Урок 7: 🦶 Части тела", "Body parts — названия частей тела.", [
          "Называть части тела",
          "Описывать внешность",
          "Понимать команды",
          "Играть в игры"
        ],
        `## 🦶 Части тела (Body parts)

### Голова и лицо

| Английский | Русский |
|------------|---------|
| head | голова |
| face | лицо |
| eye | глаз |
| ear | ухо |
| nose | нос |
| mouth | рот |
| hair | волосы |
| tooth | зуб |
| teeth | зубы |

### Тело

| Английский | Русский |
|------------|---------|
| body | тело |
| arm | рука |
| hand | кисть |
| finger | палец |
| leg | нога |
| foot | ступня |
| feet | ступни |
| knee | колено |

### Описание внешности

- I have blue eyes. — У меня голубые глаза.
- He has black hair. — У него чёрные волосы.
- She has a small nose. — У неё маленький нос.

### Команды

- Touch your nose! — Дотронься до носа!
- Close your eyes! — Закрой глаза!
- Open your mouth! — Открой рот!`,
        [
          "I have two eyes and one nose.",
          "Touch your head! — Дотронься до головы!",
          "She has long hair. — У неё длинные волосы."
        ],
        [
          "🦶 Eye — eyes, foot — feet, tooth — teeth — неправильные множественные",
          "🦶 Have got = have — оба означают «иметь»",
          "🦶 Head, shoulders, knees and toes — известная детская песенка"
        ]),
        L("Урок 8: 👔 Одежда", "Clothes — названия одежды.", [
          "Называть одежду",
          "Описывать наряд",
          "Говорить о погоде и одежде",
          "Одевать куклу"
        ],
        `## 👔 Одежда (Clothes)

### Основная одежда

| Английский | Русский |
|------------|---------|
| clothes | одежда |
| T-shirt | футболка |
| shirt | рубашка |
| trousers | брюки |
| jeans | джинсы |
| skirt | юбка |
| dress | платье |
| jacket | куртка |
| coat | пальто |
| hat | шляпа |
| cap | кепка |
| shoes | обувь |
| boots | ботинки |

### Описание одежды

- I'm wearing a red T-shirt. — Я ношу красную футболку.
- She is wearing a blue dress. — Она в синем платье.
- These are my favourite jeans. — Это мои любимые джинсы.

### Одежда и погода

- It's cold. Put on your coat. — Холодно. Надень пальто.
- It's hot. Wear a T-shirt. — Жарко. Надень футболку.
- It's raining. Take your umbrella. — Идёт дождь. Возьми зонт.`,
        [
          "I'm wearing a blue T-shirt and jeans.",
          "Put on your jacket. It's cold.",
          "My favourite clothes are jeans and trainers."
        ],
        [
          "👔 Trousers, jeans, clothes — всегда во множественном числе",
          "👔 Wear — носить (одежду), put on — надевать",
          "👔 Trainers — кроссовки (брит.), sneakers — кроссовки (амер.)"
        ])
      ]
    },
    {
      topic: "Школа и учёба",
      lessons: [
        L("Урок 9: 📚 Школьные принадлежности", "School things — названия школьных принадлежностей.", [
          "Называть предметы",
          "Просить одолжить",
          "Описывать школу",
          "Слушать инструкции"
        ],
        `## 📚 Школьные принадлежности (School things)

### Основные предметы

| Английский | Русский |
|------------|---------|
| pen | ручка |
| pencil | карандаш |
| book | книга |
| notebook | тетрадь |
| ruler | линейка |
| eraser | ластик |
| sharpener | точилка |
| pencil case | пенал |
| bag | сумка |
| schoolbag | школьный рюкзак |
| scissors | ножницы |
| glue | клей |

### В классе

- This is my pencil. — Это мой карандаш.
- I have a new book. — У меня новая книга.
- Open your books, please. — Откройте книги, пожалуйста.

### Просьба одолжить

- Can I borrow your pen? — Можно твой карандаш?
- Do you have a ruler? — У тебя есть линейка?
- Here you are. — Вот, пожалуйста.`,
        [
          "I have a pen, a pencil and a ruler.",
          "Can I borrow your eraser, please?",
          "Open your notebook and write."
        ],
        [
          "📚 Eraser (амер.) = rubber (брит.)",
          "📚 Pencil case — пенал, буквально «чехол для карандашей»",
          "📚 Borrow — одолжить, lend — дать взаймы"
        ]),
        L("Урок 10: 🏫 В классе", "In the classroom — названия предметов в классе.", [
          "Называть мебель",
          "Понимать команды учителя",
          "Описывать класс",
          "Играть в игры"
        ],
        `## 🏫 В классе (In the classroom)

### Мебель и предметы

| Английский | Русский |
|------------|---------|
| classroom | класс |
| desk | парта |
| chair | стул |
| board | доска |
| blackboard | чёрная доска |
| whiteboard | белая доска |
| door | дверь |
| window | окно |
| wall | стена |
| floor | пол |
| teacher | учитель |
| student | ученик |

### Команды учителя

| Английский | Русский |
|------------|---------|
| Stand up! | Встаньте! |
| Sit down! | Сядьте! |
| Open your books! | Откройте книги! |
| Close your books! | Закройте книги! |
| Listen! | Слушайте! |
| Look! | Смотрите! |
| Read! | Читайте! |
| Write! | Пишите! |

### Описание класса

- There is a board in the classroom. — В классе есть доска.
- There are 15 desks in our classroom. — В нашем классе 15 парт.`,
        [
          "Stand up, please. — Встаньте, пожалуйста.",
          "Open your books at page 10. — Откройте книги на странице 10.",
          "There is a big window in our classroom."
        ],
        [
          "🏫 There is — для единственного, There are — для множественного",
          "🏫 At page 10 — на странице 10",
          "🏫 Work in pairs — работайте в парах"
        ]),
        L("Урок 11: 📖 Школьные предметы", "School subjects — названия школьных предметов.", [
          "Называть предметы",
          "Говорить о расписании",
          "Выражать предпочтения",
          "Сравнивать предметы"
        ],
        `## 📖 Школьные предметы (School subjects)

### Основные предметы

| Английский | Русский |
|------------|---------|
| Maths / Math | математика |
| Russian | русский язык |
| English | английский язык |
| Reading | чтение |
| Writing | письмо |
| Science | окружающий мир |
| History | история |
| Geography | география |
| Art | изо |
| Music | музыка |
| PE (Physical Education) | физкультура |
| IT (Information Technology) | информатика |

### О предпочтениях

- My favourite subject is Art. — Мой любимый предмет — ИЗО.
- I like English. — Мне нравится английский.
- I don't like Maths. — Мне не нравится математика.
- I'm good at Music. — Я хорош в музыке.

### Расписание

- What's your first lesson? — Какой у тебя первый урок?
- We have English on Monday. — У нас английский в понедельник.
- I have five lessons today. — У меня сегодня пять уроков.`,
        [
          "My favourite subject is English.",
          "I have Maths on Monday and Wednesday.",
          "We have six lessons today."
        ],
        [
          "📖 Math (амер.) = Maths (брит.)",
          "📖 PE — Physical Education — физкультура",
          "📖 I'm good at... — Я хорош в... (сильно в...)"
        ]),
        L("Урок 12: 📅 Расписание", "Timetable — дни недели и расписание.", [
          "Называть дни недели",
          "Говорить о времени",
          "Описывать расписание",
          "Задавать вопросы"
        ],
        `## 📅 Расписание (Timetable)

### Дни недели

| Английский | Русский |
|------------|---------|
| Monday | понедельник |
| Tuesday | вторник |
| Wednesday | среда |
| Thursday | четверг |
| Friday | пятница |
| Saturday | суббота |
| Sunday | воскресенье |

### Время

| Английский | Русский |
|------------|---------|
| What time is it? | Который час? |
| It's 8 o'clock. | 8 часов. |
| It's half past 3. | Половина четвёртого. |
| morning | утро |
| afternoon | день |
| evening | вечер |
| night | ночь |

### О расписании

- School starts at 8 o'clock. — Школа начинается в 8 часов.
- On Monday I have 5 lessons. — В понедельник у меня 5 уроков.
- We have English on Tuesday and Thursday. — У нас английский во вторник и четверг.

### Вопросы

- What day is it today? — Какой сегодня день?
- What time does school start? — Во сколько начинается школа?`,
        [
          "Today is Monday. — Сегодня понедельник.",
          "School starts at 8 o'clock.",
          "On Friday we have PE."
        ],
        [
          "📅 Дни недели всегда с большой буквы",
          "📅 On Monday — в понедельник (предлог on)",
          "📅 At 8 o'clock — в 8 часов (предлог at)"
        ])
      ]
    },
    {
      topic: "Семья и дом",
      lessons: [
        L("Урок 13: 👨‍👩‍👧‍👦 Члены семьи", "Family members — названия членов семьи.", [
          "Называть родственников",
          "Описывать семью",
          "Говорить о возрасте",
          "Задавать вопросы"
        ],
        `## 👨‍👩‍👧‍👦 Члены семьи (Family members)

### Родственники

| Английский | Русский |
|------------|---------|
| family | семья |
| mother / mum | мама |
| father / dad | папа |
| parent | родитель |
| sister | сестра |
| brother | брат |
| grandmother | бабушка |
| grandfather | дедушка |
| grandmother / grandma | бабушка |
| grandfather / grandpa | дедушка |
| aunt | тётя |
| uncle | дядя |
| cousin | двоюродный брат/сестра |

### О семье

- I have a big family. — У меня большая семья.
- I have a mother, a father and a sister. — У меня есть мама, папа и сестра.
- My mum is a teacher. — Моя мама — учитель.
- My dad is 40 years old. — Моему папе 40 лет.

### Вопросы о семье

- How many people are in your family? — Сколько человек в твоей семье?
- Do you have any brothers or sisters? — У тебя есть братья или сёстры?
- What does your father do? — Кем работает твой папа?`,
        [
          "I have a mother, a father and a little brother.",
          "My grandmother is 65 years old.",
          "I love my family."
        ],
        [
          "👨‍👩‍👧‍👦 Mum, dad — неформальные, mother, father — формальные",
          "👨‍👩‍👧‍👦 Parents = mother + father",
          "👨‍👩‍👧‍👦 Grandparents = grandmother + grandfather"
        ]),
        L("Урок 14: 🏠 Мой дом", "My house — названия комнат в доме.", [
          "Называть комнаты",
          "Описывать дом",
          "Говорить о мебели",
          "Сравнивать дома"
        ],
        `## 🏠 Мой дом (My house)

### Типы жилья

| Английский | Русский |
|------------|---------|
| house | дом |
| flat / apartment | квартира |
| room | комната |

### Комнаты

| Английский | Русский |
|------------|---------|
| living room | гостиная |
| bedroom | спальня |
| kitchen | кухня |
| bathroom | ванная |
| toilet | туалет |
| hall | прихожая |
| garden | сад |

### Описание дома

- I live in a house. — Я живу в доме.
- My house has 5 rooms. — В моём доме 5 комнат.
- There is a kitchen and a living room. — Есть кухня и гостиная.
- My bedroom is small. — Моя спальня маленькая.

### Мебель

- sofa — диван
- bed — кровать
- table — стол
- chair — стул
- wardrobe — шкаф для одежды
- fridge — холодильник`,
        [
          "I live in a big house.",
          "There is a kitchen, a living room and two bedrooms.",
          "My favourite room is my bedroom."
        ],
        [
          "🏠 Flat (брит.) = Apartment (амер.)",
          "🏠 Living room — гостиная, буквально «жилая комната»",
          "🏠 Upstairs — наверху, downstairs — внизу"
        ]),
        L("Урок 15: 🛏️ Моя комната", "My room — описание комнаты.", [
          "Описывать комнату",
          "Говорить о вещах",
          "Использовать предлоги места",
          "Рисовать план"
        ],
        `## 🛏️ Моя комната (My room)

### Мебель в комнате

| Английский | Русский |
|------------|---------|
| bed | кровать |
| desk | письменный стол |
| chair | стул |
| wardrobe | шкаф |
| bookshelf | книжная полка |
| lamp | лампа |
| carpet | ковёр |
| window | окно |
| door | дверь |

### Предлоги места

| Английский | Русский | Пример |
|------------|---------|--------|
| in | в | in the room — в комнате |
| on | на | on the desk — на столе |
| under | под | under the bed — под кроватью |
| next to | рядом с | next to the window — рядом с окном |
| behind | за | behind the door — за дверью |
| in front of | перед | in front of the house — перед домом |

### Описание комнаты

- There is a bed in my room. — В моей комнате есть кровать.
- There is a desk next to the window. — Стол стоит рядом с окном.
- The carpet is on the floor. — Ковёр на полу.
- My books are on the shelf. — Мои книги на полке.`,
        [
          "There is a big bed in my room.",
          "My desk is next to the window.",
          "There are books on the shelf."
        ],
        [
          "🛏️ There is — для единственного, There are — для множественного",
          "🛏️ Is there...? / Are there...? — вопросы",
          "🛏️ In the corner — в углу"
        ]),
        L("Урок 16: 📆 Будни и выходные", "Weekdays and weekends — описание дней.", [
          "Рассказывать о буднях",
          "Описывать выходные",
          "Использовать Present Simple",
          "Сравнивать дни"
        ],
        `## 📆 Будни и выходные (Weekdays and weekends)

### Будни и выходные

| Английский | Русский |
|------------|---------|
| weekday | будний день |
| weekend | выходные |
| Monday - Friday | будни |
| Saturday - Sunday | выходные |

### Рутина (Daily routine)

| Английский | Русский |
|------------|---------|
| get up | вставать |
| have breakfast | завтракать |
| go to school | идти в школу |
| have lunch | обедать |
| come home | приходить домой |
| do homework | делать уроки |
| have dinner | ужинать |
| go to bed | ложиться спать |

### Present Simple (Настоящее простое)

**Утверждение:**
- I get up at 7 o'clock. — Я встаю в 7 часов.
- She goes to school at 8. — Она идёт в школу в 8.

**Вопрос:**
- Do you like weekends? — Тебе нравятся выходные?
- What do you do on Sunday? — Что ты делаешь в воскресенье?`,
        [
          "I get up at 7 o'clock on weekdays.",
          "On Saturday I play with my friends.",
          "I do my homework after school."
        ],
        [
          "📆 On weekdays — в будни, at the weekend — на выходных",
          "📆 В Present Simple добавляем -s/-es к глаголу для he/she/it",
          "📆 Do — для вопросов и отрицаний"
        ])
      ]
    },
    {
      topic: "Еда и напитки",
      lessons: [
        L("Урок 17: 🍕 Продукты", "Food — названия продуктов.", [
          "Называть продукты",
          "Говорить о предпочтениях",
          "Описывать вкус",
          "Составлять список покупок"
        ],
        `## 🍕 Продукты (Food)

### Основные продукты

| Английский | Русский |
|------------|---------|
| bread | хлеб |
| cheese | сыр |
| milk | молоко |
| butter | масло |
| egg | яйцо |
| meat | мясо |
| chicken | курица |
| fish | рыба |
| rice | рис |
| pasta | макароны |
| pizza | пицца |
| sandwich | бутерброд |

### О предпочтениях

- I like pizza. — Мне нравится пицца.
- I don't like fish. — Мне не нравится рыба.
- My favourite food is chicken. — Моя любимая еда — курица.

### Вкус

- sweet — сладкий
- salty — солёный
- sour — кислый
- delicious — вкусный
- tasty — вкусный
- yummy — вкусненький

### Немного / Много

- some bread — немного хлеба
- some cheese — немного сыра
- a lot of fruit — много фруктов`,
        [
          "I like pizza and pasta.",
          "My favourite food is chicken with rice.",
          "Do you like cheese?"
        ],
        [
          "🍕 Food — еда, meal — приём пищи",
          "🍕 Some используется для утверждения, any — для вопросов",
          "🍕 Countable — можно посчитать, uncountable — нельзя"
        ]),
        L("Урок 18: 🥤 Напитки", "Drinks — названия напитков.", [
          "Называть напитки",
          "Предлагать угощение",
          "Принимать и отказываться",
          "Заказывать в кафе"
        ],
        `## 🥤 Напитки (Drinks)

### Названия напитков

| Английский | Русский |
|------------|---------|
| water | вода |
| milk | молоко |
| juice | сок |
| tea | чай |
| coffee | кофе |
| lemonade | лимонад |
| cola | кола |
| hot chocolate | горячий шоколад |

### Предложение

- Would you like some tea? — Хотите чаю?
- Do you want some juice? — Хочешь сока?
- Can I have some water? — Можно воды?

### Ответы

- Yes, please. — Да, пожалуйста.
- No, thank you. — Нет, спасибо.
- I'd love some. — С удовольствием.

### В кафе

- Can I have a cup of tea, please? — Можно чашку чая, пожалуйста?
- I'd like some orange juice. — Я бы хотел апельсиновый сок.
- A glass of water, please. — Стакан воды, пожалуйста.`,
        [
          "Would you like some tea? — Yes, please.",
          "Can I have a glass of juice?",
          "I don't like coffee. I prefer tea."
        ],
        [
          "🥤 A cup of — чашка, a glass of — стакан",
          "🥤 Would you like — вежливое предложение",
          "🥤 I'd like = I would like — я бы хотел"
        ]),
        L("Урок 19: 🍎 Фрукты и овощи", "Fruits and vegetables — названия фруктов и овощей.", [
          "Называть фрукты",
          "Называть овощи",
          "Говорить о пользе",
          "Составлять салат"
        ],
        `## 🍎 Фрукты и овощи (Fruits and vegetables)

### Фрукты

| Английский | Русский |
|------------|---------|
| fruit | фрукт |
| apple | яблоко |
| orange | апельсин |
| banana | банан |
| pear | груша |
| peach | персик |
| grape | виноград |
| strawberry | клубника |
| cherry | вишня |

### Овощи

| Английский | Русский |
|------------|---------|
| vegetable | овощ |
| tomato | помидор |
| potato | картофель |
| carrot | морковь |
| cabbage | капуста |
| onion | лук |
| cucumber | огурец |
| pepper | перец |

### Описание

- Apples are red, green or yellow. — Яблоки красные, зелёные или жёлтые.
- Bananas are yellow. — Бананы жёлтые.
- Carrots are orange. — Морковь оранжевая.
- Vegetables are healthy. — Овощи полезные.

### Полезные фразы

- An apple a day keeps the doctor away. — Одно яблоко в день — и доктор не нужен.
- Eat your vegetables! — Ешь овощи!`,
        [
          "I like apples and bananas.",
          "Tomatoes and cucumbers are vegetables.",
          "Fruit and vegetables are healthy."
        ],
        [
          "🍎 Apple — an apple, но Bananas — без артикля",
          "🍎 Tomato — помидор, potato — картофель",
          "🍎 Healthy — полезный, fresh — свежий"
        ]),
        L("Урок 20: ☕ В кафе", "At the café — диалоги в кафе.", [
          "Делать заказ",
          "Спрашивать о меню",
          "Платить за заказ",
          "Благодарить"
        ],
        `## ☕ В кафе (At the café)

### Фразы для заказа

| Английский | Русский |
|------------|---------|
| Can I have...? | Можно мне...? |
| I'd like... | Я бы хотел... |
| What would you like? | Что вы хотите? |
| Here's your order. | Вот ваш заказ. |
| Anything else? | Что-нибудь ещё? |
| That's all. | Это всё. |

### Диалог в кафе

**Waiter:** Hello! What would you like?
*Официант: Привет! Что вы хотите?*

**Customer:** Can I have a pizza and some juice, please?
*Посетитель: Можно пиццу и сок, пожалуйста?*

**Waiter:** Here you are. Anything else?
*Официант: Вот. Что-нибудь ещё?*

**Customer:** No, that's all. How much is it?
*Посетитель: Нет, это всё. Сколько это стоит?*

**Waiter:** That's 5 pounds. Thank you!
*Официант: 5 фунтов. Спасибо!*

**Customer:** Thank you! Goodbye!
*Посетитель: Спасибо! До свидания!*

### Полезные слова

- menu — меню
- order — заказ
- bill — счёт
- tip — чаевые`,
        [
          "Can I have a sandwich and a cup of tea, please?",
          "How much is it? — That's 10 dollars.",
          "Thank you very much! Goodbye!"
        ],
        [
          "☕ How much is it? — Сколько это стоит?",
          "☕ Here you are — Вот, пожалуйста",
          "☕ Enjoy your meal — Приятного аппетита"
        ])
      ]
    },
    {
      topic: "Путешествия",
      lessons: [
        L("Урок 21: 🚌 Транспорт", "Transport — названия транспорта.", [
          "Называть виды транспорта",
          "Описывать поездку",
          "Покупать билет",
          "Спрашивать дорогу"
        ],
        `## 🚌 Транспорт (Transport)

### Виды транспорта

| Английский | Русский |
|------------|---------|
| car | машина |
| bus | автобус |
| train | поезд |
| plane | самолёт |
| ship | корабль |
| boat | лодка |
| bike / bicycle | велосипед |
| taxi | такси |
| underground / subway | метро |
| tram | трамвай |

### Описание поездки

- I go to school by bus. — Я еду в школу на автобусе.
- We go on holiday by plane. — Мы едем в отпуск на самолёте.
- I ride my bike. — Я катаюсь на велосипеде.

### Покупка билета

- One ticket to London, please. — Один билет до Лондона, пожалуйста.
- How much is a ticket? — Сколько стоит билет?
- Single or return? — В одну сторону или туда-обратно?

### Спрашивать дорогу

- How do I get to the station? — Как добраться до станции?
- Where is the bus stop? — Где автобусная остановка?
- Is it far? — Это далеко?`,
        [
          "I go to school by bus.",
          "We travelled to Moscow by train.",
          "How much is a ticket to the city centre?"
        ],
        [
          "🚌 By car / by bus / by plane — на машине/автобусе/самолёте",
          "🚌 On foot — пешком",
          "🚌 Underground (брит.) = Subway (амер.)"
        ]),
        L("Урок 22: 🏙️ В городе", "In the city — названия мест в городе.", [
          "Называть места в городе",
          "Описывать маршрут",
          "Спрашивать дорогу",
          "Давать указания"
        ],
        `## 🏙️ В городе (In the city)

### Места в городе

| Английский | Русский |
|------------|---------|
| city | город |
| street | улица |
| park | парк |
| shop | магазин |
| supermarket | супермаркет |
| hospital | больница |
| school | школа |
| library | библиотека |
| museum | музей |
| cinema | кинотеатр |
| restaurant | ресторан |
| café | кафе |
| bank | банк |
| post office | почта |

### Спрашивать дорогу

- Excuse me, where is the bank? — Извините, где банк?
- How do I get to the park? — Как добраться до парка?
- Is there a café near here? — Здесь рядом есть кафе?

### Давать указания

- Go straight on. — Идите прямо.
- Turn left. — Поверните налево.
- Turn right. — Поверните направо.
- It's on the left. — Это слева.
- It's on the right. — Это справа.
- It's next to the school. — Это рядом со школой.`,
        [
          "Excuse me, where is the cinema?",
          "Go straight on and turn left.",
          "The bank is next to the post office."
        ],
        [
          "🏙️ Excuse me используется, чтобы обратиться к незнакомцу",
          "🏙️ Turn left/right — поверните налево/направо",
          "🏙️ Go straight = Go ahead — идите прямо"
        ]),
        L("Урок 23: 🗼 Достопримечательности", "Sights — названия достопримечательностей.", [
          "Называть достопримечательности",
          "Описывать места",
          "Рассказывать о городе",
          "Быть гидом"
        ],
        `## 🗼 Достопримечательности (Sights)

### Известные места

| Английский | Русский |
|------------|---------|
| sight | достопримечательность |
| monument | памятник |
| castle | замок |
| palace | дворец |
| church | церковь |
| cathedral | собор |
| bridge | мост |
| tower | башня |
| square | площадь |
| fountain | фонтан |

### Достопримечательности мира

| Английский | Где находится |
|------------|---------------|
| Big Ben | Лондон, Англия |
| Tower of London | Лондон, Англия |
| Eiffel Tower | Париж, Франция |
| Statue of Liberty | Нью-Йорк, США |
| Kremlin | Москва, Россия |
| Red Square | Москва, Россия |

### Описание

- Big Ben is a famous clock tower in London. — Биг-Бен — знаменитая часовая башня в Лондоне.
- The Eiffel Tower is in Paris. — Эйфелева башня находится в Париже.
- The Kremlin is in Moscow. — Кремль находится в Москве.
- It's very beautiful. — Это очень красиво.`,
        [
          "Big Ben is a famous clock tower in London.",
          "Red Square is in the centre of Moscow.",
          "The Eiffel Tower is very beautiful."
        ],
        [
          "🗼 Famous — знаменитый, popular — популярный",
          "🗼 In the centre of — в центре",
          "🗼 I want to visit... — Я хочу посетить..."
        ]),
        L("Урок 24: 🌍 Страны", "Countries — названия стран и национальностей.", [
          "Называть страны",
          "Говорить о национальностях",
          "Описывать флаги",
          "Сравнивать страны"
        ],
        `## 🌍 Страны (Countries)

### Страны и национальности

| Страна | Английский | Национальность |
|--------|------------|----------------|
| Россия | Russia | Russian |
| Англия | England | English |
| США | USA / America | American |
| Франция | France | French |
| Германия | Germany | German |
| Испания | Spain | Spanish |
| Италия | Italy | Italian |
| Китай | China | Chinese |
| Япония | Japan | Japanese |

### Языки

- I speak Russian. — Я говорю по-русски.
- I speak English. — Я говорю по-английски.
- I learn English at school. — Я учу английский в школе.

### Описание страны

- Russia is a big country. — Россия — большая страна.
- The capital of Russia is Moscow. — Столица России — Москва.
- Russian flag is white, blue and red. — Российский флаг белый, синий и красный.

### Вопросы

- Where are you from? — Откуда ты?
- What language do you speak? — На каком языке ты говоришь?
- What's the capital of...? — Какая столица...?`,
        [
          "I'm from Russia. I'm Russian.",
          "The capital of France is Paris.",
          "I speak Russian and English."
        ],
        [
          "🌍 Страны и языки пишутся с большой буквы",
          "🌍 Национальности тоже с большой буквы",
          "🌍 The USA = The United States of America"
        ])
      ]
    }
  ]
}
export const games: GameLesson[] = [

  // ========== АНГЛИЙСКИЙ (24 теста) ==========
  {
    title: "Приветствие",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say «Доброе утро» in English?", options: ["Good night", "Good morning", "Good evening", "Good afternoon", "Hello"], correctAnswer: "Good morning", hint: "Morning — утро" },
      { type: 'quiz', question: "What does «Goodbye!» mean?", options: ["Здравствуйте", "Доброе утро", "До свидания", "Спокойной ночи", "Как дела"], correctAnswer: "До свидания", hint: "Goodbye — прощание" },
      { type: 'quiz', question: "«Как дела?» по-английски: How (...)_ you?", options: ["are", "you", "английски", "дела", "how"], correctAnswer: "are", hint: "How are you? — Как дела?" },
      { type: 'quiz', question: "What does «See you!» mean?", options: ["До свидания", "Увидимся", "Привет", "Как дела", "Спасибо"], correctAnswer: "Увидимся", hint: "See you — увидимся позже" },
      { type: 'quiz', question: "How do you answer «How are you?»", options: ["My name is Tom", ",", "I", "Hello", "m fine, thanks!"], correctAnswer: "I'm fine, thanks!", hint: "Отвечаем: I'm fine, thanks!" }
    ],
    reward: { stars: 3, message: "Great! Ты знаешь приветствия! 👋" }
  },

  {
    title: "Представление",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say «Меня зовут Анна»?", options: ["My name is Anna", "I am Anna", "She is Anna", "It is Anna", "Anna is me"], correctAnswer: "My name is Anna", hint: "My name is... — Меня зовут..." },
      { type: 'quiz', question: "What does «I'm from Russia» mean?", options: ["Я говорю по-русски", "Я из России", "Я люблю Россию", "Я живу в Москве", "Я учусь в России"], correctAnswer: "Я из России", hint: "I'm from — Я из..." },
      { type: 'quiz', question: "«Мне 10 лет» по-английски: I'm (...) years old.", options: ["8", "9", "10", "11", "12"], correctAnswer: "10", hint: "I'm [число] years old." },
      { type: 'quiz', question: "What does «Nice to meet you!» mean?", options: ["Как дела?", "Как тебя зовут?", "Приятно познакомиться!", "До свидания!", "Сколько тебе лет?"], correctAnswer: "Приятно познакомиться!", hint: "Nice to meet you — при знакомстве" },
      { type: 'quiz', question: "How do you ask «Откуда ты?»?", options: ["What is your name?", "How old are you?", "Where are you from?", "How are you?", "Who are you?"], correctAnswer: "Where are you from?", hint: "Where — где/откуда" }
    ],
    reward: { stars: 3, message: "Excellent! Ты умеешь представляться! 🙋" }
  },

  {
    title: "Вежливые слова",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say «Пожалуйста» when making a request?", options: ["Thank you", "Sorry", "Please", "Hello", "Goodbye"], correctAnswer: "Please", hint: "Please — пожалуйста (при просьбе)" },
      { type: 'quiz', question: "What does «Thank you very much!» mean?", options: ["Здравствуйте", "Извините", "До свидания", "Большое спасибо!", "Пожалуйста"], correctAnswer: "Большое спасибо!", hint: "Thank you very much — большое спасибо" },
      { type: 'quiz', question: "«Вы здесь» (вот, пожалуйста): Here (...)_ are.", options: ["you", "here", "are", "здесь", "пожалуйста"], correctAnswer: "you", hint: "Here you are — вот, пожалуйста" },
      { type: 'quiz', question: "What does «You're welcome!» mean?", options: ["Добро пожаловать", "Не за что! (пожалуйста)", "Привет", "Спасибо", "До свидания"], correctAnswer: "Не за что! (пожалуйста)", hint: "Ответ на благодарность" },
      { type: 'quiz', question: "How do you say «Извините!»?", options: ["Hello", "Please", "Thanks", "Sorry!", "Goodbye"], correctAnswer: "Sorry!", hint: "Sorry — извини/извините" }
    ],
    reward: { stars: 3, message: "Wonderful! Ты знаешь вежливые слова! 🙏" }
  },

  {
    title: "Вопросительные слова",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What does «Where?» mean?", options: ["Кто?", "Где? Куда?", "Когда?", "Почему?", "Что?"], correctAnswer: "Где? Куда?", hint: "Where — где / куда" },
      { type: 'quiz', question: "Which word asks «Когда?»?", options: ["What", "Where", "Who", "When", "How"], correctAnswer: "When", hint: "When — когда" },
      { type: 'quiz', question: "«Почему?» по-английски: (...)_", options: ["нет", "не знаю", "почему", "английски", "Why"], correctAnswer: "Why", hint: "Why — почему" },
      { type: 'quiz', question: "What does «Who?» mean?", options: ["Что?", "Где?", "Кто?", "Как?", "Когда?"], correctAnswer: "Кто?", hint: "Who — используется только про людей" },
      { type: 'quiz', question: "How do you ask «Что это?»?", options: ["Who is this?", "Where is this?", "When is this?", "What is this?", "How is this?"], correctAnswer: "What is this?", hint: "What — что / какой" }
    ],
    reward: { stars: 3, message: "Good job! Ты знаешь вопросительные слова! ❓" }
  },

  {
    title: "Цвета",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say «красный» in English?", options: ["Blue", "Green", "Red", "Yellow", "Black"], correctAnswer: "Red", hint: "Red — красный" },
      { type: 'quiz', question: "What colour is the grass?", options: ["Red", "Blue", "Yellow", "Green", "White"], correctAnswer: "Green", hint: "Трава зелёная — green" },
      { type: 'quiz', question: "«Жёлтый» по-английски: (...)_", options: ["жёлтый", "нет", "не знаю", "yellow", "английски"], correctAnswer: "yellow", hint: "The sun is yellow." },
      { type: 'quiz', question: "What does «purple» mean?", options: ["Зелёный", "Оранжевый", "Фиолетовый", "Розовый", "Коричневый"], correctAnswer: "Фиолетовый", hint: "Purple — фиолетовый" },
      { type: 'quiz', question: "How do you ask «Какого это цвета?»?", options: ["What is it?", "What colour is it?", "How is it?", "Where is it?", "Who is it?"], correctAnswer: "What colour is it?", hint: "What colour — какой цвет" }
    ],
    reward: { stars: 3, message: "Amazing! Ты знаешь цвета! 🎨" }
  },

  {
    title: "Числа",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say «пятнадцать» in English?", options: ["Fifty", "Fifteen", "Five", "Fourteen", "Sixteen"], correctAnswer: "Fifteen", hint: "Fifteen — 15 (с буквой n: fifTEEN)" },
      { type: 'quiz', question: "What number is «twelve»?", options: ["10", "11", "12", "20", "13"], correctAnswer: "12", hint: "Twelve = 12" },
      { type: 'quiz', question: "«Сорок» по-английски: (...)", options: ["fourty", "forty", "fourteen", "four", "for"], correctAnswer: "forty", hint: "Внимание: forty пишется без 'u'!" },
      { type: 'quiz', question: "What is «one hundred»?", options: ["10", "100", "1000", "50", "99"], correctAnswer: "100", hint: "One hundred = 100" },
      { type: 'quiz', question: "Numbers 13-19 end in:", options: ["-ty", "-teen", "-tion", "-ed", "-ing"], correctAnswer: "-teen", hint: "thirteen, fourteen, fifteen..." }
    ],
    reward: { stars: 3, message: "Super! Ты знаешь числа! 🔢" }
  },

  {
    title: "Части тела",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say «голова» in English?", options: ["Hand", "Head", "Hair", "Heart", "Hat"], correctAnswer: "Head", hint: "Head — голова" },
      { type: 'quiz', question: "What does «eye» mean?", options: ["Ухо", "Нос", "Глаз", "Рот", "Рука"], correctAnswer: "Глаз", hint: "Eye — глаз (множественное: eyes)" },
      { type: 'quiz', question: "«Нога» по-английски: (...)_", options: ["не знаю", "нет", "английски", "нога", "leg"], correctAnswer: "leg", hint: "Leg — нога (от бедра до стопы)" },
      { type: 'quiz', question: "What is the plural of «tooth»?", options: ["Toothes", "Teeth", "Tooths", "Teeths", "Toothes"], correctAnswer: "Teeth", hint: "Tooth → teeth — неправильное множественное" },
      { type: 'quiz', question: "What does «nose» mean?", options: ["Глаз", "Ухо", "Нос", "Рот", "Шея"], correctAnswer: "Нос", hint: "Nose — нос" }
    ],
    reward: { stars: 3, message: "Great! Ты знаешь части тела! 🦶" }
  },

  {
    title: "Одежда",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say «футболка» in English?", options: ["Shirt", "T-shirt", "Dress", "Coat", "Sweater"], correctAnswer: "T-shirt", hint: "T-shirt — футболка" },
      { type: 'quiz', question: "What does «jacket» mean?", options: ["Шляпа", "Куртка", "Рубашка", "Юбка", "Платье"], correctAnswer: "Куртка", hint: "Jacket — куртка" },
      { type: 'quiz', question: "«Брюки» по-английски: (...)_", options: ["trousers", "нет", "не знаю", "английски", "брюки"], correctAnswer: "trousers", hint: "Trousers — брюки (всегда множественное)" },
      { type: 'quiz', question: "What does «shoes» mean?", options: ["Шапка", "Шарф", "Обувь / ботинки", "Носки", "Перчатки"], correctAnswer: "Обувь / ботинки", hint: "Shoes — обувь" },
      { type: 'quiz', question: "How do you say «Я ношу красную футболку»?", options: ["I have a red T-shirt", "I'm wearing a red T-shirt", "I like red T-shirt", "Red is my T-shirt", "My T-shirt is red"], correctAnswer: "I'm wearing a red T-shirt", hint: "I'm wearing — я ношу" }
    ],
    reward: { stars: 3, message: "Nice! Ты знаешь одежду! 👔" }
  },

  {
    title: "Школьные принадлежности",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say «ручка» in English?", options: ["Pencil", "Pen", "Paper", "Book", "Ruler"], correctAnswer: "Pen", hint: "Pen — ручка, pencil — карандаш" },
      { type: 'quiz', question: "What does «eraser» mean?", options: ["Карандаш", "Линейка", "Ластик", "Точилка", "Пенал"], correctAnswer: "Ластик", hint: "Eraser (амер.) = rubber (брит.)" },
      { type: 'quiz', question: "«Линейка» по-английски: (...)_", options: ["нет", "ruler", "не знаю", "линейка", "английски"], correctAnswer: "ruler", hint: "Ruler — линейка" },
      { type: 'quiz', question: "What does «pencil case» mean?", options: ["Карандаш", "Ручка", "Ластик", "Пенал", "Сумка"], correctAnswer: "Пенал", hint: "Pencil case — чехол для карандашей = пенал" },
      { type: 'quiz', question: "How do you ask «Можно одолжить ручку?»?", options: ["Give me a pen", "I need a pen", "Can I borrow your pen?", "Where is my pen?", "Your pen is nice"], correctAnswer: "Can I borrow your pen?", hint: "Borrow — одолжить" }
    ],
    reward: { stars: 3, message: "Perfect! Ты знаешь школьные принадлежности! 📚" }
  },

  {
    title: "В классе",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say «парта» in English?", options: ["Table", "Desk", "Chair", "Board", "Door"], correctAnswer: "Desk", hint: "Desk — школьная парта" },
      { type: 'quiz', question: "What does «board» mean?", options: ["Парта", "Стул", "Доска", "Окно", "Дверь"], correctAnswer: "Доска", hint: "Board — классная доска" },
      { type: 'quiz', question: "«Встаньте!» по-английски: Stand (...)_!", options: ["up", "stand", "английски", "нет", "встаньте"], correctAnswer: "up", hint: "Stand up! — встаньте!" },
      { type: 'quiz', question: "What does «Sit down!» mean?", options: ["Встаньте!", "Сядьте!", "Пишите!", "Читайте!", "Слушайте!"], correctAnswer: "Сядьте!", hint: "Sit down — сядьте" },
      { type: 'quiz', question: "What does «window» mean?", options: ["Дверь", "Стена", "Пол", "Окно", "Потолок"], correctAnswer: "Окно", hint: "Window — окно" }
    ],
    reward: { stars: 3, message: "Well done! Ты знаешь слова для класса! 🏫" }
  },

  {
    title: "Школьные предметы",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say «математика» in English?", options: ["Maths", "Music", "Art", "Science", "History"], correctAnswer: "Maths", hint: "Maths (брит.) / Math (амер.)" },
      { type: 'quiz', question: "What does «PE» stand for?", options: ["Primary English", "Physical Education", "Practical Exercise", "Public Exam", "Personal Education"], correctAnswer: "Physical Education", hint: "PE — физкультура" },
      { type: 'quiz', question: "«Музыка» по-английски: (...)_", options: ["нет", "не знаю", "английски", "музыка", "Music"], correctAnswer: "Music", hint: "Music — музыка" },
      { type: 'quiz', question: "How do you say «Мой любимый предмет — ИЗО»?", options: ["I like Art", "My favourite subject is Art", "I have Art", "Art is good", "I do Art"], correctAnswer: "My favourite subject is Art", hint: "My favourite subject is..." },
      { type: 'quiz', question: "What does «Science» mean?", options: ["История", "География", "Окружающий мир / Естествознание", "Музыка", "Чтение"], correctAnswer: "Окружающий мир / Естествознание", hint: "Science — наука, окружающий мир" }
    ],
    reward: { stars: 3, message: "Fantastic! Ты знаешь школьные предметы! 📖" }
  },

  {
    title: "Расписание",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What day comes after Monday?", options: ["Sunday", "Wednesday", "Tuesday", "Thursday", "Friday"], correctAnswer: "Tuesday", hint: "Monday → Tuesday" },
      { type: 'quiz', question: "How do you say «среда» in English?", options: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], correctAnswer: "Wednesday", hint: "Wednesday — среда (помни букву d!)" },
      { type: 'quiz', question: "«Школа начинается в 8 часов»: School starts at (...) o'clock.", options: ["7", "8", "9", "10", "6"], correctAnswer: "8", hint: "At 8 o'clock — в 8 часов" },
      { type: 'quiz', question: "What does «weekend» mean?", options: ["Будни", "Выходные", "Неделя", "Утро", "Каникулы"], correctAnswer: "Выходные", hint: "Weekend — суббота и воскресенье" },
      { type: 'quiz', question: "How do you ask «Какой сегодня день?»?", options: ["What time is it?", "What day is it today?", "How are you?", "Where is school?", "What is this?"], correctAnswer: "What day is it today?", hint: "What day — какой день" }
    ],
    reward: { stars: 3, message: "Brilliant! Ты знаешь расписание! 📅" }
  },

  {
    title: "Члены семьи",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say «бабушка» in English?", options: ["Mother", "Sister", "Grandmother", "Aunt", "Daughter"], correctAnswer: "Grandmother", hint: "Grandmother / grandma — бабушка" },
      { type: 'quiz', question: "What does «uncle» mean?", options: ["Дедушка", "Дядя", "Брат", "Папа", "Сын"], correctAnswer: "Дядя", hint: "Uncle — дядя" },
      { type: 'quiz', question: "«Двоюродный брат/сестра» по-английски: (...)_", options: ["сестра", "английски", "cousin", "двоюродный", "брат"], correctAnswer: "cousin", hint: "Cousin — двоюродный брат или сестра" },
      { type: 'quiz', question: "What does «parents» mean?", options: ["Дети", "Бабушка и дедушка", "Мама и папа (родители)", "Брат и сестра", "Дядя и тётя"], correctAnswer: "Мама и папа (родители)", hint: "Parents = mother + father" },
      { type: 'quiz', question: "How do you say «У меня есть брат»?", options: ["I have a brother", "I am a brother", "My brother is", "I see a brother", "I like brother"], correctAnswer: "I have a brother", hint: "I have — у меня есть" }
    ],
    reward: { stars: 3, message: "Lovely! Ты знаешь членов семьи! 👨‍👩‍👧‍👦" }
  },

  {
    title: "Мой дом",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say «кухня» in English?", options: ["Bedroom", "Living room", "Kitchen", "Bathroom", "Hall"], correctAnswer: "Kitchen", hint: "Kitchen — кухня" },
      { type: 'quiz', question: "What does «living room» mean?", options: ["Спальня", "Кухня", "Гостиная", "Ванная", "Прихожая"], correctAnswer: "Гостиная", hint: "Living room — гостиная" },
      { type: 'quiz', question: "«Спальня» по-английски: (...)_", options: ["не знаю", "английски", "спальня", "нет", "bedroom"], correctAnswer: "bedroom", hint: "Bedroom — спальня" },
      { type: 'quiz', question: "What does «garden» mean?", options: ["Гараж", "Сад", "Балкон", "Крыша", "Погреб"], correctAnswer: "Сад", hint: "Garden — сад" },
      { type: 'quiz', question: "How do you say «Я живу в большом доме»?", options: ["I live in a big house", "My big house is", "I have big house", "Big house I live", "I am big house"], correctAnswer: "I live in a big house", hint: "I live in — я живу в" }
    ],
    reward: { stars: 3, message: "Great! Ты знаешь слова про дом! 🏠" }
  },

  {
    title: "Моя комната",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say «кровать» in English?", options: ["Desk", "Chair", "Bed", "Sofa", "Table"], correctAnswer: "Bed", hint: "Bed — кровать" },
      { type: 'quiz', question: "What does «next to the window» mean?", options: ["Под окном", "За окном", "Рядом с окном", "На окне", "Над окном"], correctAnswer: "Рядом с окном", hint: "Next to — рядом с" },
      { type: 'quiz', question: "«Ковёр» по-английски: (...)_", options: ["carpet", "нет", "английски", "не знаю", "ковёр"], correctAnswer: "carpet", hint: "Carpet — ковёр" },
      { type: 'quiz', question: "What does «under the bed» mean?", options: ["На кровати", "Рядом с кроватью", "Под кроватью", "За кроватью", "Над кроватью"], correctAnswer: "Под кроватью", hint: "Under — под" },
      { type: 'quiz', question: "How do you say «Книги на полке»?", options: ["Books in the shelf", "Books on the shelf", "Books under the shelf", "Books next to shelf", "The books shelf"], correctAnswer: "Books on the shelf", hint: "On the shelf — на полке" }
    ],
    reward: { stars: 3, message: "Wonderful! Ты описываешь комнату! 🛏️" }
  },

  {
    title: "Будни и выходные",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say «делать уроки» in English?", options: ["Do homework", "Make homework", "Have homework", "Go homework", "Work homework"], correctAnswer: "Do homework", hint: "Do homework — делать домашнее задание" },
      { type: 'quiz', question: "What does «get up» mean?", options: ["Ложиться спать", "Вставать", "Завтракать", "Идти в школу", "Приходить домой"], correctAnswer: "Вставать", hint: "Get up — вставать (с кровати)" },
      { type: 'quiz', question: "«Ложиться спать» по-английски: go to (...)_", options: ["go", "спать", "английски", "ложиться", "bed"], correctAnswer: "bed", hint: "Go to bed — ложиться спать" },
      { type: 'quiz', question: "What does «have breakfast» mean?", options: ["Обедать", "Ужинать", "Завтракать", "Идти гулять", "Просыпаться"], correctAnswer: "Завтракать", hint: "Have breakfast — завтракать" },
      { type: 'quiz', question: "How do you say «Я встаю в 7 часов»?", options: ["I go to school at 7", "I get up at 7 o", ",", "clock", "—"], correctAnswer: "I get up at 7 o'clock", hint: "Get up — вставать, at 7 o'clock — в 7 часов" }
    ],
    reward: { stars: 3, message: "Excellent! Ты знаешь распорядок дня! 📆" }
  },

  {
    title: "Продукты",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say «хлеб» in English?", options: ["Butter", "Bread", "Cheese", "Meat", "Milk"], correctAnswer: "Bread", hint: "Bread — хлеб" },
      { type: 'quiz', question: "What does «cheese» mean?", options: ["Молоко", "Масло", "Сыр", "Мясо", "Рыба"], correctAnswer: "Сыр", hint: "Cheese — сыр" },
      { type: 'quiz', question: "«Курица» по-английски: (...)_", options: ["chicken", "не знаю", "курица", "английски", "нет"], correctAnswer: "chicken", hint: "Chicken — курица" },
      { type: 'quiz', question: "How do you say «Мне нравится пицца»?", options: ["I eat pizza", "I have pizza", "I like pizza", "I want pizza", "My pizza is good"], correctAnswer: "I like pizza", hint: "I like — мне нравится" },
      { type: 'quiz', question: "What does «butter» mean?", options: ["Хлеб", "Сыр", "Молоко", "Масло", "Яйцо"], correctAnswer: "Масло", hint: "Butter — сливочное масло" }
    ],
    reward: { stars: 3, message: "Yummy! Ты знаешь продукты! 🍕" }
  },

  {
    title: "Напитки",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say «сок» in English?", options: ["Water", "Milk", "Juice", "Tea", "Coffee"], correctAnswer: "Juice", hint: "Juice — сок" },
      { type: 'quiz', question: "What does «Would you like some tea?» mean?", options: ["Ты хочешь чаю?", "Где чай?", "Я люблю чай", "Чай вкусный", "Сколько стоит чай?"], correctAnswer: "Ты хочешь чаю?", hint: "Would you like — вежливое предложение" },
      { type: 'quiz', question: "«Вода» по-английски: (...)_", options: ["вода", "water", "нет", "не знаю", "английски"], correctAnswer: "water", hint: "Water — вода" },
      { type: 'quiz', question: "What does «a cup of tea» mean?", options: ["Стакан чая", "Чашка чая", "Бутылка чая", "Банка чая", "Чайник чая"], correctAnswer: "Чашка чая", hint: "A cup of — чашка" },
      { type: 'quiz', question: "How do you refuse politely? «Нет, ___»", options: ["Go away", "No, thank you", "I hate it", "Stop", "Never"], correctAnswer: "No, thank you", hint: "No, thank you — вежливый отказ" }
    ],
    reward: { stars: 3, message: "Delicious! Ты знаешь напитки! 🥤" }
  },

  {
    title: "Фрукты и овощи",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say «яблоко» in English?", options: ["Banana", "Orange", "Apple", "Pear", "Grape"], correctAnswer: "Apple", hint: "Apple — яблоко (с an: an apple)" },
      { type: 'quiz', question: "What does «carrot» mean?", options: ["Картофель", "Капуста", "Морковь", "Огурец", "Помидор"], correctAnswer: "Морковь", hint: "Carrot — морковь" },
      { type: 'quiz', question: "«Банан» по-английски: (...)_", options: ["нет", "banana", "английски", "не знаю", "банан"], correctAnswer: "banana", hint: "Banana — банан" },
      { type: 'quiz', question: "What does «tomato» mean?", options: ["Картофель", "Морковь", "Лук", "Помидор", "Огурец"], correctAnswer: "Помидор", hint: "Tomato — помидор" },
      { type: 'quiz', question: "How do you say «Овощи полезные»?", options: ["Vegetables are healthy", "Vegetables are tasty", "Vegetables are bad", "I like vegetables", "Eat vegetables"], correctAnswer: "Vegetables are healthy", hint: "Healthy — полезный" }
    ],
    reward: { stars: 3, message: "Fresh! Ты знаешь фрукты и овощи! 🍎" }
  },

  {
    title: "В кафе",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you order food politely? «___ I have a pizza?»", options: ["Do", "Can", "Am", "Is", "Are"], correctAnswer: "Can", hint: "Can I have...? — Можно мне...?" },
      { type: 'quiz', question: "What does «I'd like...» mean?", options: ["Я люблю", "Я хочу", "Я ем", "Я знаю", "Я вижу"], correctAnswer: "Я хочу", hint: "I'd like = I would like — я бы хотел" },
      { type: 'quiz', question: "«Сколько это стоит?» по-английски: How (...)_ is it?", options: ["английски", "стоит", "how", "much", "is"], correctAnswer: "much", hint: "How much is it? — сколько стоит?" },
      { type: 'quiz', question: "What does «menu» mean?", options: ["Еда", "Официант", "Меню", "Счёт", "Стол"], correctAnswer: "Меню", hint: "Menu — меню (перечень блюд)" },
      { type: 'quiz', question: "What does «Enjoy your meal!» mean?", options: ["До свидания", "Приятного аппетита!", "Спасибо", "Пожалуйста", "Как вкусно!"], correctAnswer: "Приятного аппетита!", hint: "Enjoy your meal — приятного аппетита" }
    ],
    reward: { stars: 3, message: "Bon appétit! Ты знаешь фразы для кафе! ☕" }
  },

  {
    title: "Транспорт",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say «автобус» in English?", options: ["Car", "Bus", "Train", "Bike", "Taxi"], correctAnswer: "Bus", hint: "Bus — автобус" },
      { type: 'quiz', question: "What does «underground» mean?", options: ["Поезд", "Самолёт", "Метро", "Трамвай", "Велосипед"], correctAnswer: "Метро", hint: "Underground (брит.) = Subway (амер.)" },
      { type: 'quiz', question: "«Самолёт» по-английски: (...)_", options: ["plane", "не знаю", "нет", "самолёт", "английски"], correctAnswer: "plane", hint: "Plane — самолёт" },
      { type: 'quiz', question: "How do you say «Я еду в школу на автобусе»?", options: ["I go to school by car", "I go to school by bus", "I go to school by train", "I go to school by plane", "I go to school by bike"], correctAnswer: "I go to school by bus", hint: "By bus — на автобусе" },
      { type: 'quiz', question: "What does «ship» mean?", options: ["Машина", "Поезд", "Корабль", "Велосипед", "Трамвай"], correctAnswer: "Корабль", hint: "Ship — корабль" }
    ],
    reward: { stars: 3, message: "Excellent! Ты знаешь транспорт! 🚌" }
  },

  {
    title: "В городе",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "How do you say «библиотека» in English?", options: ["Shop", "Hospital", "Library", "Museum", "School"], correctAnswer: "Library", hint: "Library — библиотека" },
      { type: 'quiz', question: "What does «museum» mean?", options: ["Школа", "Больница", "Парк", "Музей", "Магазин"], correctAnswer: "Музей", hint: "Museum — музей" },
      { type: 'quiz', question: "«Больница» по-английски: (...)_", options: ["больница", "не знаю", "нет", "английски", "hospital"], correctAnswer: "hospital", hint: "Hospital — больница" },
      { type: 'quiz', question: "How do you ask «Где банк?»?", options: ["What is the bank?", "Where is the bank?", "Who is the bank?", "How is the bank?", "Why is the bank?"], correctAnswer: "Where is the bank?", hint: "Where is...? — Где...?" },
      { type: 'quiz', question: "What does «park» mean?", options: ["Магазин", "Ресторан", "Парк", "Кинотеатр", "Банк"], correctAnswer: "Парк", hint: "Park — парк" }
    ],
    reward: { stars: 3, message: "Great! Ты знаешь слова про город! 🏙️" }
  },

  {
    title: "Достопримечательности",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Where is Big Ben?", options: ["Paris", "Moscow", "London", "New York", "Rome"], correctAnswer: "London", hint: "Big Ben — знаменитая башня в Лондоне" },
      { type: 'quiz', question: "What does «castle» mean?", options: ["Церковь", "Мост", "Замок", "Башня", "Площадь"], correctAnswer: "Замок", hint: "Castle — замок" },
      { type: 'quiz', question: "«Мост» по-английски: (...)_", options: ["нет", "мост", "bridge", "английски", "не знаю"], correctAnswer: "bridge", hint: "Bridge — мост" },
      { type: 'quiz', question: "Where is the Eiffel Tower?", options: ["London", "Moscow", "Berlin", "Paris", "Rome"], correctAnswer: "Paris", hint: "Eiffel Tower — Эйфелева башня в Париже" },
      { type: 'quiz', question: "What does «square» mean?", options: ["Улица", "Мост", "Фонтан", "Площадь", "Памятник"], correctAnswer: "Площадь", hint: "Square — площадь" }
    ],
    reward: { stars: 3, message: "Fantastic! Ты знаешь достопримечательности! 🗼" }
  },

  {
    title: "Страны",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What is the capital of France?", options: ["London", "Berlin", "Paris", "Madrid", "Rome"], correctAnswer: "Paris", hint: "Столица Франции — Париж" },
      { type: 'quiz', question: "What nationality is someone from Germany?", options: ["French", "English", "Spanish", "German", "Italian"], correctAnswer: "German", hint: "Germany — German" },
      { type: 'quiz', question: "«Япония» по-английски: (...)_", options: ["япония", "нет", "Japan", "английски", "не знаю"], correctAnswer: "Japan", hint: "Japan — Япония" },
      { type: 'quiz', question: "How do you say «Россия — большая страна»?", options: ["Russia is small", "Russia is big", "Russia is old", "Russia is new", "Russia is beautiful"], correctAnswer: "Russia is big", hint: "Big — большой, страна — country" },
      { type: 'quiz', question: "What does «The USA» mean?", options: ["Англия", "Франция", "Германия", "США", "Испания"], correctAnswer: "США", hint: "The USA = The United States of America" }
    ],
    reward: { stars: 3, message: "Amazing! Ты знаешь страны! 🌍" }
  }
]
