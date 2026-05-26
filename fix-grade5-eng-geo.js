#!/usr/bin/env node
/**
 * Fix Grade 5 English + Geography: add facts, tests, expand examples
 * - English: 24 lessons (lesson 24 has 0 examples, needs 4+)
 * - Geography: 23 lessons (each has 3 examples, need 4+)
 * For each lesson: add 1-2 examples, 3 facts, tests { quiz:[5], find:[5], match:[5] }
 */

const fs = require('fs');
const path = require('path');

const BASE = path.join(__dirname, 'public/data/grades/5');

// ========== ENGLISH DATA ==========
const englishData = {
  "Урок 1: Приветствие и прощание": {
    examples: [
      "— Goodbye! See you tomorrow! — Bye, have a nice day!",
      "Фраза How do you do используется при официальном знакомстве"
    ],
    facts: [
      "В английском языке есть формальные и неформальные приветствия — выбор зависит от ситуации и собеседника",
      "Слово goodbye произошло от фразы God be with ye («Да пребудет с вами Бог»)",
      "В Великобритании при встрече часто говорят о погоде — это часть культурной традиции вежливого общения"
    ],
    quiz: [
      { question: "Which greeting is formal?", options: ["Hi!", "Good morning!", "Hey!", "Yo!"], correct: 1 },
      { question: "What does 'Good night' mean?", options: ["Good evening greeting", "Morning greeting", "Farewell at night", "Thank you"], correct: 2 },
      { question: "How do you respond to 'How are you?'", options: ["I am fine, thanks!", "Good night!", "Nice to meet you!", "Goodbye!"], correct: 0 },
      { question: "Which phrase is used when meeting someone for the first time?", options: ["See you later!", "Nice to meet you!", "Good night!", "Take care!"], correct: 1 },
      { question: "What is the informal way to say goodbye?", options: ["Farewell!", "Bye!", "Good evening!", "How do you do?"], correct: 1 }
    ],
    find: [
      { text: "Формальное приветствие утром — Good ___", answer: "morning" },
      { text: "Вежливое слово при просьбе — ___", answer: "please" },
      { text: "Фраза прощания вечером — Good ___", answer: "night" },
      { text: "Ответ на How are you? — I am ___, thanks!", answer: "fine" },
      { text: "Неформальное приветствие — ___!", answer: "Hi" }
    ],
    match: [
      { term: "Hello", definition: "Универсальное приветствие" },
      { term: "Goodbye", definition: "Прощание на английском" },
      { term: "Please", definition: "Вежливое слово при просьбе" },
      { term: "Good night", definition: "Прощание перед сном" },
      { term: "Nice to meet you", definition: "Рад знакомству" }
    ]
  },
  "Урок 2: Личная информация": {
    examples: [
      "— Where are you from? — I am from Russia.",
      "Заполнение анкеты: Name: Anna, Age: 11, Country: Russia"
    ],
    facts: [
      "В английском языке для указания возраста используется конструкция I am + число, а не глагол «иметь» как в русском",
      "При заполнении форм на английском Name — это имя, Surname/Family name — фамилия",
      "Адрес на английском записывается от меньшего к большему: номер дома, улица, город, страна"
    ],
    quiz: [
      { question: "How do you ask about someone's age?", options: ["What is your name?", "How old are you?", "Where are you from?", "What is your hobby?"], correct: 1 },
      { question: "What does 'surname' mean?", options: ["Имя", "Отчество", "Фамилия", "Возраст"], correct: 2 },
      { question: "How do you say 'Мне 11 лет' in English?", options: ["I have 11 years", "I am 11 years old", "I am 11 old years", "My age is 11 old"], correct: 1 },
      { question: "Which question asks about origin?", options: ["What is your name?", "How old are you?", "Where are you from?", "What is your job?"], correct: 2 },
      { question: "In English forms, 'Date of birth' means:", options: ["Дата смерти", "Дата рождения", "Дата свадьбы", "Дата переезда"], correct: 1 }
    ],
    find: [
      { text: "Сколько тебе лет? — How ___ are you?", answer: "old" },
      { text: "Откуда ты? — Where are you ___?", answer: "from" },
      { text: "Как тебя зовут? — What is your ___?", answer: "name" },
      { text: "Моя фамилия — My ___ is Ivanov.", answer: "surname" },
      { text: "Я живу в Москве — I ___ in Moscow.", answer: "live" }
    ],
    match: [
      { term: "Name", definition: "Имя человека" },
      { term: "Surname", definition: "Фамилия человека" },
      { term: "Age", definition: "Возраст человека" },
      { term: "Address", definition: "Адрес проживания" },
      { term: "Date of birth", definition: "Дата рождения" }
    ]
  },
  "Урок 3: Страны и национальности": {
    examples: [
      "— I am from Japan. I am Japanese. — I am from Brazil. I am Brazilian.",
      "Страна Italy — национальность Italian, страна France — национальность French"
    ],
    facts: [
      "Названия стран и национальностей в английском всегда пишутся с большой буквы",
      "Не все национальности образуются по правилу — например, Netherlands → Dutch, France → French",
      "Слова для национальностей могут использоваться как существительные и как прилагательные: She is Russian. She speaks Russian."
    ],
    quiz: [
      { question: "What is the nationality of a person from Spain?", options: ["Spainish", "Spanish", "Spainer", "Español"], correct: 1 },
      { question: "Which country corresponds to 'German'?", options: ["Greece", "Germany", "Georgia", "Denmark"], correct: 1 },
      { question: "How do you say 'Я из России'?", options: ["I from Russia", "I am from Russia", "I am Russia", "I come Russia"], correct: 1 },
      { question: "Which nationality does NOT follow the standard -ish/-an pattern?", options: ["Russian", "British", "French", "American"], correct: 2 },
      { question: "Country and nationality are both capitalized:", options: ["Never", "Only in titles", "Always", "Only countries"], correct: 2 }
    ],
    find: [
      { text: "Человек из Англии — ___", answer: "English" },
      { text: "Я из Италии — I am from ___.", answer: "Italy" },
      { text: "Национальность Японии — ___", answer: "Japanese" },
      { text: "Страна для Brazilian — ___", answer: "Brazil" },
      { text: "Национальность Китая — ___", answer: "Chinese" }
    ],
    match: [
      { term: "Russia", definition: "Russian" },
      { term: "France", definition: "French" },
      { term: "Germany", definition: "German" },
      { term: "Japan", definition: "Japanese" },
      { term: "Brazil", definition: "Brazilian" }
    ]
  },
  "Урок 4: Профессии": {
    examples: [
      "— What does your mother do? — She is a doctor. She works in a hospital.",
      "Мой дядя — инженер. He is an engineer. Он проектирует мосты."
    ],
    facts: [
      "Перед названиями профессий в английском используется неопределённый артикль a/an: She is a teacher",
      "Слова профессий часто образуются суффиксами: -er (teacher), -or (actor), -ist (dentist), -man (fireman)",
      "В современном английском нейтральные формы профессий предпочтительнее: police officer вместо policeman"
    ],
    quiz: [
      { question: "Which suffix is common for profession words?", options: ["-ful", "-er", "-ly", "-ing"], correct: 1 },
      { question: "What article do we use before professions?", options: ["The", "A/An", "No article", "Some"], correct: 1 },
      { question: "A person who teaches is a:", options: ["Teachor", "Teacher", "Teachist", "Teachman"], correct: 1 },
      { question: "Which is the gender-neutral form?", options: ["Fireman", "Policeman", "Police officer", "Businessman"], correct: 2 },
      { question: "What does a vet do?", options: ["Teaches children", "Treats animals", "Drives buses", "Cooks food"], correct: 1 }
    ],
    find: [
      { text: "Человек, который лечит людей — a ___", answer: "doctor" },
      { text: "Она учитель — She is a ___.", answer: "teacher" },
      { text: "Артикль перед профессией: He is ___ engineer.", answer: "an" },
      { text: "Человек, который готовит еду — a ___", answer: "cook" },
      { text: "Полицейский на английском — a police ___", answer: "officer" }
    ],
    match: [
      { term: "Doctor", definition: "Лечит людей" },
      { term: "Teacher", definition: "Учит детей" },
      { term: "Engineer", definition: "Проектирует здания и механизмы" },
      { term: "Firefighter", definition: "Тушит пожары" },
      { term: "Programmer", definition: "Пишет компьютерные программы" }
    ]
  },
  "Урок 5: Погода и времена года": {
    examples: [
      "— What's the weather like today? — It's sunny and warm.",
      "В Англии часто идёт дождь, поэтому зонт — обязательный аксессуар ☔"
    ],
    facts: [
      "В английском для описания погоды используется конструкция It is + прилагательное: It is cold / It is hot",
      "В Австралии времена года противоположны северному полушарию — когда в России зима, там лето",
      "Фраза What's the weather like? — стандартный вопрос о погоде в английском языке"
    ],
    quiz: [
      { question: "How do you ask about the weather?", options: ["What is weather?", "What's the weather like?", "How weather?", "Which weather?"], correct: 1 },
      { question: "Which season comes after winter?", options: ["Summer", "Autumn", "Spring", "Winter"], correct: 2 },
      { question: "What does 'It's foggy' mean?", options: ["Солнечно", "Туманно", "Ветрено", "Ясно"], correct: 1 },
      { question: "In Australia, December is in:", options: ["Winter", "Spring", "Summer", "Autumn"], correct: 2 },
      { question: "Which word describes snowy weather?", options: ["Sunny", "Cloudy", "Foggy", "Frosty"], correct: 3 }
    ],
    find: [
      { text: "Какая погода? — What's the ___ like?", answer: "weather" },
      { text: "Весна по-английски — ___", answer: "spring" },
      { text: "Идёт дождь — It is ___.", answer: "raining" },
      { text: "Лето по-английски — ___", answer: "summer" },
      { text: "Холодная погода — ___ weather", answer: "cold" }
    ],
    match: [
      { term: "Winter", definition: "Холодное время года со снегом" },
      { term: "Sunny", definition: "Солнечная погода" },
      { term: "Rainy", definition: "Дождливая погода" },
      { term: "Autumn", definition: "Время года с листопадом" },
      { term: "Wind", definition: "Движение воздуха" }
    ]
  },
  "Урок 6: Природа и животные": {
    examples: [
      "Elephants are the largest land animals. They live in Africa and Asia.",
      "Dolphins are very intelligent. They can communicate with each other."
    ],
    facts: [
      "В английском языке животные часто сопровождаются артиклем the, когда речь о виде: The tiger is a big cat",
      "Многие названия детёнышей животных не похожи на названия взрослых: cat — kitten, dog — puppy, bear — cub",
      "Слово animal происходит от латинского anima — «душа, дыхание»"
    ],
    quiz: [
      { question: "What is a baby cat called?", options: ["Puppy", "Kitten", "Cub", "Foal"], correct: 1 },
      { question: "Which animal is the largest on land?", options: ["Lion", "Giraffe", "Elephant", "Bear"], correct: 2 },
      { question: "Where do dolphins live?", options: ["In the forest", "In the ocean", "In the mountains", "In the desert"], correct: 1 },
      { question: "Which is a wild animal?", options: ["Dog", "Cat", "Wolf", "Cow"], correct: 2 },
      { question: "The word 'animal' comes from Latin:", options: ["Anima (soul)", "Animalis (big)", "Animus (strong)", "Annam (earth)"], correct: 0 }
    ],
    find: [
      { text: "Детёныш собаки — a ___", answer: "puppy" },
      { text: "Самое высокое животное — the ___", answer: "giraffe" },
      { text: "Животное с длинным хоботом — an ___", answer: "elephant" },
      { text: "Дикие животные живут в ___", answer: "forest" },
      { text: "Рыба живёт в воде — Fish live in the ___.", answer: "water" }
    ],
    match: [
      { term: "Kitten", definition: "Детёныш кошки" },
      { term: "Elephant", definition: "Крупнейшее сухопутное животное" },
      { term: "Dolphin", definition: "Умное морское млекопитающее" },
      { term: "Eagle", definition: "Крупная хищная птица" },
      { term: "Bear", definition: "Крупный лесной хищник" }
    ]
  },
  "Урок 7: В городе": {
    examples: [
      "— Excuse me, where is the nearest bank? — Go straight and turn left.",
      "В центре города много магазинов и кафе — There are many shops and cafés in the city centre."
    ],
    facts: [
      "Лондон — один из крупнейших городов мира с населением более 9 миллионов человек",
      "В английском языке для указания направления используются предлоги: turn left, turn right, go straight, go past",
      "Слово city обычно обозначает крупный город, а town — небольшой городок"
    ],
    quiz: [
      { question: "How do you ask for directions politely?", options: ["Where bank?!", "Tell me where the bank is!", "Excuse me, where is the bank?", "Give me the bank!"], correct: 2 },
      { question: "What does 'turn left' mean?", options: ["Поверните направо", "Идите прямо", "Поверните налево", "Развернитесь"], correct: 2 },
      { question: "Which word means a small town?", options: ["City", "Village", "Metropolis", "Capital"], correct: 1 },
      { question: "What is the capital of Great Britain?", options: ["Manchester", "Birmingham", "London", "Liverpool"], correct: 2 },
      { question: "'Go straight' means:", options: ["Идите назад", "Идите прямо", "Поверните", "Остановитесь"], correct: 1 }
    ],
    find: [
      { text: "Поверните направо — turn ___", answer: "right" },
      { text: "Идите прямо — go ___", answer: "straight" },
      { text: "Ближайшая больница — the nearest ___", answer: "hospital" },
      { text: "Городской парк — city ___", answer: "park" },
      { text: "Перейдите улицу — cross the ___", answer: "street" }
    ],
    match: [
      { term: "Hospital", definition: "Больница" },
      { term: "Library", definition: "Библиотека" },
      { term: "Museum", definition: "Музей" },
      { term: "Pharmacy", definition: "Аптека" },
      { term: "Post office", definition: "Почтовое отделение" }
    ]
  },
  "Урок 8: Транспорт": {
    examples: [
      "— How do you get to school? — I go by bus.",
      "Самый быстрый способ добраться до Лондона — на самолёте — The fastest way to get to London is by plane."
    ],
    facts: [
      "Предлог by используется с видами транспорта без артикля: by bus, by car, by train, но in a car / on a bus",
      "Лондонское метро — самое старое в мире, оно открылось в 1863 году",
      "Великобритания — страна с левосторонним движением, в отличие от большинства стран мира"
    ],
    quiz: [
      { question: "Which preposition do we use with transport without an article?", options: ["In", "On", "By", "At"], correct: 2 },
      { question: "The London Underground opened in:", options: ["1901", "1863", "1920", "1850"], correct: 1 },
      { question: "How do you say 'на автобусе'?", options: ["In bus", "On bus", "By bus", "At bus"], correct: 2 },
      { question: "In the UK, cars drive on the:", options: ["Right", "Left", "Middle", "Both sides"], correct: 1 },
      { question: "Which is the fastest means of transport?", options: ["Train", "Bus", "Bicycle", "Plane"], correct: 3 }
    ],
    find: [
      { text: "На поезде — by ___", answer: "train" },
      { text: "На велосипеде — by ___", answer: "bicycle" },
      { text: "Метро по-английски — the ___", answer: "underground" },
      { text: "На автомобиле — by ___", answer: "car" },
      { text: "Такси по-английски — a ___", answer: "taxi" }
    ],
    match: [
      { term: "Bus", definition: "Автобус" },
      { term: "Underground", definition: "Метро" },
      { term: "Bicycle", definition: "Велосипед" },
      { term: "Plane", definition: "Самолёт" },
      { term: "Ship", definition: "Корабль" }
    ]
  },
  "Урок 9: Члены семьи": {
    examples: [
      "My grandmother tells me interesting stories about her childhood.",
      "— Who is this in the photo? — This is my older brother, Alex."
    ],
    facts: [
      "В английском нет различия между бабушкой по маме и по папе — обе называются grandmother",
      "Слова parents означают «родители» (мама и папа), а relatives — «родственники» (все родные)",
      "Близнецы по-английски — twins, а тройняшки — triplets"
    ],
    quiz: [
      { question: "How do you say 'бабушка' in English?", options: ["Grandfather", "Grandmother", "Aunt", "Cousin"], correct: 1 },
      { question: "What does 'siblings' mean?", options: ["Родители", "Братья и сёстры", "Бабушки", "Дяди"], correct: 1 },
      { question: "Your mother's brother is your:", options: ["Uncle", "Cousin", "Nephew", "Aunt"], correct: 0 },
      { question: "'Twins' means:", options: ["Двоюродные братья", "Близнецы", "Родители", "Внуки"], correct: 1 },
      { question: "Which word means 'родственники'?", options: ["Parents", "Family", "Relatives", "Friends"], correct: 2 }
    ],
    find: [
      { text: "Мой папа — my ___", answer: "father" },
      { text: "Младшая сестра — younger ___", answer: "sister" },
      { text: "Двоюродный брат — ___", answer: "cousin" },
      { text: "Дядя по-английски — ___", answer: "uncle" },
      { text: "Моя семья — my ___", answer: "family" }
    ],
    match: [
      { term: "Mother", definition: "Мама" },
      { term: "Grandfather", definition: "Дедушка" },
      { term: "Aunt", definition: "Тётя" },
      { term: "Cousin", definition: "Двоюродный брат/сестра" },
      { term: "Nephew", definition: "Племянник" }
    ]
  },
  "Урок 10: Внешность и характер": {
    examples: [
      "She has long dark hair and blue eyes. She is very kind and cheerful.",
      "Мой друг высокий и стройный, он всегда весёлый — My friend is tall and slim, he is always cheerful."
    ],
    facts: [
      "Прилагательные для описания внешности ставятся в определённом порядке: размер → возраст → цвет",
      "Слова handsome и beautiful означают «красивый», но handsome — о мужчинах, а beautiful — о женщинах",
      "В английском слово look используется для описания внешности: She looks tired — Она выглядит уставшей"
    ],
    quiz: [
      { question: "Which word describes a man's good looks?", options: ["Beautiful", "Pretty", "Handsome", "Cute"], correct: 2 },
      { question: "What does 'tall' mean?", options: ["Низкий", "Высокий", "Полный", "Худой"], correct: 1 },
      { question: "Which adjective describes personality?", options: ["Tall", "Blond", "Generous", "Slim"], correct: 2 },
      { question: "'She looks tired' means:", options: ["Она выглядит усталой", "Она устала от вида", "Она красивая", "Она выглядит молодой"], correct: 0 },
      { question: "Adjective order for appearance: size → age →", options: ["Color", "Height", "Weight", "Shape"], correct: 0 }
    ],
    find: [
      { text: "Красивая женщина — a ___ woman", answer: "beautiful" },
      { text: "Весёлый человек — a ___ person", answer: "cheerful" },
      { text: "Она выглядит уставшей — She ___ tired.", answer: "looks" },
      { text: "Кудрявые волосы — ___ hair", answer: "curly" },
      { text: "Щедрый человек — a ___ person", answer: "generous" }
    ],
    match: [
      { term: "Tall", definition: "Высокий (о росте)" },
      { term: "Slim", definition: "Стройный" },
      { term: "Curly", definition: "Кудрявый (о волосах)" },
      { term: "Kind", definition: "Добрый" },
      { term: "Brave", definition: "Храбрый" }
    ]
  },
  "Урок 11: Друзья": {
    examples: [
      "My best friend and I have been friends since kindergarten.",
      "— Can you help me with my homework? — Of course, that's what friends are for!"
    ],
    facts: [
      "Слово friend переводится как «друг», а best friend — «лучший друг»",
      "Фраза make friends означает «заводить друзей», а не «делать друзей»",
      "В английском есть выражение fair-weather friend — «друг в хорошем», который рядом только в хорошие времена"
    ],
    quiz: [
      { question: "What does 'best friend' mean?", options: ["Хороший знакомый", "Лучший друг", "Старый друг", "Новый друг"], correct: 1 },
      { question: "'Make friends' means:", options: ["Делать друзей", "Заводить друзей", "Терять друзей", "Искать друзей"], correct: 1 },
      { question: "A 'fair-weather friend' is someone who:", options: ["Is always there", "Leaves when things get hard", "Loves rainy weather", "Is very old"], correct: 1 },
      { question: "How do you say 'Мы дружим с детства'?", options: ["We are friends from childhood", "We have been friends since childhood", "We make friends in childhood", "We were friends at childhood"], correct: 1 },
      { question: "Which word means 'дружба'?", options: ["Friend", "Friendly", "Friendship", "Friends"], correct: 2 }
    ],
    find: [
      { text: "Лучший друг — best ___", answer: "friend" },
      { text: "Дружба по-английски — ___", answer: "friendship" },
      { text: "Дружелюбный — ___", answer: "friendly" },
      { text: "Заводить друзей — make ___", answer: "friends" },
      { text: "Мы друзья — We are ___.", answer: "friends" }
    ],
    match: [
      { term: "Friendship", definition: "Дружба" },
      { term: "Best friend", definition: "Лучший друг" },
      { term: "Friendly", definition: "Дружелюбный" },
      { term: "Trust", definition: "Доверие" },
      { term: "Support", definition: "Поддержка" }
    ]
  },
  "Урок 12: Дом и быт": {
    examples: [
      "There is a big kitchen and a cozy living room in our house.",
      "Моя комната на втором этаже — My room is on the second floor."
    ],
    facts: [
      "В британском английском первый этаж называется ground floor, а второй — first floor",
      "Конструкция there is / there are используется для описания помещений: There is a table — There are chairs",
      "Слово home означает «дом» как место жительства, а house — «дом» как здание"
    ],
    quiz: [
      { question: "In British English, the first floor is called:", options: ["First floor", "Ground floor", "Basement", "Top floor"], correct: 1 },
      { question: "Which word means 'дом как место жительства'?", options: ["House", "Building", "Home", "Flat"], correct: 2 },
      { question: "'There ___ a book on the table' — correct form:", options: ["are", "is", "be", "were"], correct: 1 },
      { question: "Which room is for cooking?", options: ["Bedroom", "Bathroom", "Kitchen", "Living room"], correct: 2 },
      { question: "A flat is:", options: ["A house", "An apartment", "A room", "A garden"], correct: 1 }
    ],
    find: [
      { text: "Кухня по-английски — ___", answer: "kitchen" },
      { text: "Есть два стула — There ___ two chairs.", answer: "are" },
      { text: "Гостиная — living ___", answer: "room" },
      { text: "Мой дом — my ___", answer: "home" },
      { text: "Ванная комната — ___", answer: "bathroom" }
    ],
    match: [
      { term: "Kitchen", definition: "Кухня" },
      { term: "Bedroom", definition: "Спальня" },
      { term: "Living room", definition: "Гостиная" },
      { term: "Garden", definition: "Сад" },
      { term: "Roof", definition: "Крыша" }
    ]
  },
  "Урок 13: Школьные предметы": {
    examples: [
      "My favourite subject is Maths because I like solving problems.",
      "В расписание сегодня: English, Science, Art и PE (физкультура)."
    ],
    facts: [
      "PE (Physical Education) — это физкультура, а IT (Information Technology) — информатика",
      "В британских школах математика называется Maths, а в американских — Math",
      "Слово subject означает и «школьный предмет», и «тема»"
    ],
    quiz: [
      { question: "What does PE stand for?", options: ["Primary Education", "Physical Education", "Personal English", "Public Entertainment"], correct: 1 },
      { question: "How is Mathematics called in British English?", options: ["Math", "Maths", "Mathematics only", "Calc"], correct: 1 },
      { question: "Which subject studies the past?", options: ["Geography", "Science", "History", "Art"], correct: 2 },
      { question: "What does 'IT' stand for at school?", options: ["Important Test", "Information Technology", "International Training", "Individual Time"], correct: 1 },
      { question: "Which subject involves painting and drawing?", options: ["Music", "Art", "PE", "Maths"], correct: 1 }
    ],
    find: [
      { text: "Мой любимый предмет — my favourite ___", answer: "subject" },
      { text: "Физкультура — ___", answer: "PE" },
      { text: "История по-английски — ___", answer: "History" },
      { text: "Расписание уроков — school ___", answer: "timetable" },
      { text: "География — ___", answer: "Geography" }
    ],
    match: [
      { term: "Maths", definition: "Математика" },
      { term: "History", definition: "История" },
      { term: "Science", definition: "Естествознание" },
      { term: "Art", definition: "Изобразительное искусство" },
      { term: "Music", definition: "Музыка" }
    ]
  },
  "Урок 14: В классе": {
    examples: [
      "— Open your books at page 15, please. — OK, Miss Johnson.",
      "— Can I borrow your pen? — Sure, here you are."
    ],
    facts: [
      "Фразы в классе: May I come in? (Можно войти?), May I go out? (Можно выйти?)",
      "В британских школах ученики обращаются к учителю Sir (к мужчине) или Miss (к женщине)",
      "Слово board означает доску, а whiteboard — современная маркерная доска"
    ],
    quiz: [
      { question: "How do you ask to enter the classroom?", options: ["Can I go?", "May I come in?", "I want enter!", "Open the door!"], correct: 1 },
      { question: "How do students address a male teacher in Britain?", options: ["Mister", "Teacher", "Sir", "Mr."], correct: 2 },
      { question: "'Open your books at page 10' means:", options: ["Закройте книги", "Откройте книги на странице 10", "Прочитайте страницу 10", "Напишите страницу 10"], correct: 1 },
      { question: "What is a 'whiteboard'?", options: ["Тетрадь", "Маркерная доска", "Учебник", "Парта"], correct: 1 },
      { question: "'May I go out?' is used to:", options: ["Ask to enter", "Ask to leave", "Ask a question", "Ask for help"], correct: 1 }
    ],
    find: [
      { text: "Можно войти? — May I ___ in?", answer: "come" },
      { text: "Откройте книги — ___ your books.", answer: "Open" },
      { text: "Можно одолжить ручку? — Can I borrow your ___?", answer: "pen" },
      { text: "Маркерная доска — ___", answer: "whiteboard" },
      { text: "Домашнее задание — ___", answer: "homework" }
    ],
    match: [
      { term: "Homework", definition: "Домашнее задание" },
      { term: "Whiteboard", definition: "Маркерная доска" },
      { term: "Desk", definition: "Парта" },
      { term: "Timetable", definition: "Расписание" },
      { term: "Break", definition: "Перемена" }
    ]
  },
  "Урок 15: Распорядок дня": {
    examples: [
      "I wake up at 7 am, have breakfast, and go to school at 8 am.",
      "После школы я делаю уроки, а вечером смотрю телевизор — After school I do my homework, and in the evening I watch TV."
    ],
    facts: [
      "Для описания регулярных действий используется Present Simple: I get up at 7 o'clock every day",
      "AM означает до полудня (ante meridiem), а PM — после полудня (post meridiem)",
      "В английском время дня указывается с предлогом: in the morning, in the afternoon, in the evening, но at night"
    ],
    quiz: [
      { question: "What tense is used for daily routines?", options: ["Past Simple", "Present Continuous", "Present Simple", "Future Simple"], correct: 2 },
      { question: "What does AM mean?", options: ["После полудня", "До полудня", "Вечером", "Ночью"], correct: 1 },
      { question: "Which preposition is correct: ___ night?", options: ["In", "On", "At", "By"], correct: 2 },
      { question: "'I wake up at 7 am' means:", options: ["Я просыпаюсь в 7 вечера", "Я просыпаюсь в 7 утра", "Я ложусь в 7 утра", "Я встаю в 7 ночи"], correct: 1 },
      { question: "Which phrase means 'чистить зубы'?", options: ["Do homework", "Brush teeth", "Have lunch", "Take a shower"], correct: 1 }
    ],
    find: [
      { text: "Я просыпаюсь в 7 утра — I ___ up at 7 am.", answer: "wake" },
      { text: "Завтракать — have ___", answer: "breakfast" },
      { text: "Делать уроки — do ___", answer: "homework" },
      { text: "Днём — in the ___", answer: "afternoon" },
      { text: "Ложиться спать — go to ___", answer: "bed" }
    ],
    match: [
      { term: "Wake up", definition: "Просыпаться" },
      { term: "Have breakfast", definition: "Завтракать" },
      { term: "Go to school", definition: "Идти в школу" },
      { term: "Do homework", definition: "Делать уроки" },
      { term: "Go to bed", definition: "Ложиться спать" }
    ]
  },
  "Урок 16: Выходные и каникулы": {
    examples: [
      "At the weekend we usually go to the park or visit our grandparents.",
      "Летние каникулы — это лучшее время для путешествий — Summer holidays are the best time for travelling."
    ],
    facts: [
      "В британском английском говорят at the weekend, а в американском — on the weekend",
      "Слово holiday может означать и «выходной», и «каникулы», а vacation используется в американском английском",
      "Summer holidays в британских школах длятся около 6 недель — с конца июля до начала сентября"
    ],
    quiz: [
      { question: "How do British people say 'на выходных'?", options: ["On the weekend", "At the weekend", "In the weekend", "By the weekend"], correct: 1 },
      { question: "Which word is American English for 'каникулы'?", options: ["Holiday", "Vacation", "Break", "Rest"], correct: 1 },
      { question: "How long are summer holidays in British schools?", options: ["2 weeks", "4 weeks", "About 6 weeks", "3 months"], correct: 2 },
      { question: "'Go camping' means:", options: ["Идти в поход с палаткой", "Идти в магазин", "Ехать на поезде", "Идти в школу"], correct: 0 },
      { question: "Which season has the longest school break?", options: ["Winter", "Spring", "Autumn", "Summer"], correct: 3 }
    ],
    find: [
      { text: "Выходные — the ___", answer: "weekend" },
      { text: "Каникулы — ___", answer: "holidays" },
      { text: "Путешествовать — ___", answer: "travel" },
      { text: "Летний лагерь — summer ___", answer: "camp" },
      { text: "Отдыхать — to ___", answer: "relax" }
    ],
    match: [
      { term: "Weekend", definition: "Выходные (суббота и воскресенье)" },
      { term: "Holiday", definition: "Праздник или каникулы" },
      { term: "Camping", definition: "Отдых с палаткой" },
      { term: "Travel", definition: "Путешествовать" },
      { term: "Sightseeing", definition: "Осмотр достопримечательностей" }
    ]
  },
  "Урок 17: Продукты питания": {
    examples: [
      "I usually have cereal and milk for breakfast, and a sandwich for lunch.",
      "В России популярны борщ и пельмени, а в Англии — fish and chips."
    ],
    facts: [
      "В английском языке исчисляемые продукты (an apple, two eggs) и неисчисляемые (milk, bread, rice)",
      "Традиционный английский завтрак включает яйца, бекон, тосты и чай — English breakfast",
      "Слово food — неисчисляемое, но meal (приём пищи) — исчисляемое: three meals a day"
    ],
    quiz: [
      { question: "Which food word is uncountable?", options: ["Apple", "Egg", "Milk", "Banana"], correct: 2 },
      { question: "Traditional English breakfast includes:", options: ["Borshch", "Fish and chips", "Eggs and bacon", "Pasta"], correct: 2 },
      { question: "How many meals a day are typical?", options: ["One", "Two", "Three", "Five"], correct: 2 },
      { question: "Which is a countable food word?", options: ["Bread", "Rice", "Egg", "Milk"], correct: 2 },
      { question: "'Fish and chips' is a popular dish in:", options: ["Russia", "France", "England", "Japan"], correct: 2 }
    ],
    find: [
      { text: "Завтрак по-английски — ___", answer: "breakfast" },
      { text: "Фрукты по-английски — ___", answer: "fruit" },
      { text: "Овощи по-английски — ___", answer: "vegetables" },
      { text: "Молоко — ___, хлеб — bread", answer: "milk" },
      { text: "Обед — ___", answer: "lunch" }
    ],
    match: [
      { term: "Breakfast", definition: "Завтрак" },
      { term: "Lunch", definition: "Обед" },
      { term: "Dinner", definition: "Ужин" },
      { term: "Snack", definition: "Перекус" },
      { term: "Dessert", definition: "Десерт" }
    ]
  },
  "Урок 18: В кафе и ресторане": {
    examples: [
      "— Can I have a chocolate cake, please? — Here you are. That's £3.50.",
      "— Are you ready to order? — Yes, I'd like a pizza, please."
    ],
    facts: [
      "Фраза I'd like (= I would like) — вежливый способ заказать еду в кафе и ресторане",
      "В британских ресторанах чаевые (tip) обычно составляют 10-15% от суммы заказа",
      "Слово menu означает «меню», а bill (UK) / check (US) — «счёт» в ресторане"
    ],
    quiz: [
      { question: "Which phrase is polite for ordering food?", options: ["Give me pizza!", "I want pizza!", "I'd like a pizza, please.", "Pizza now!"], correct: 2 },
      { question: "What is the British word for a restaurant bill?", options: ["Check", "Bill", "Receipt", "Invoice"], correct: 1 },
      { question: "Standard tip in British restaurants is:", options: ["5%", "10-15%", "20%", "No tip"], correct: 1 },
      { question: "'Are you ready to order?' means:", options: ["Вы готовы платить?", "Вы готовы заказать?", "Вы готовите?", "Вы уходите?"], correct: 1 },
      { question: "What does 'menu' mean?", options: ["Счёт", "Официант", "Меню", "Чаевые"], correct: 2 }
    ],
    find: [
      { text: "Я бы хотел — I'd ___", answer: "like" },
      { text: "Меню по-английски — ___", answer: "menu" },
      { text: "Счёт, пожалуйста — The ___, please.", answer: "bill" },
      { text: "Официант по-английски — ___", answer: "waiter" },
      { text: "Заказать — to ___", answer: "order" }
    ],
    match: [
      { term: "Waiter", definition: "Официант" },
      { term: "Menu", definition: "Меню" },
      { term: "Bill", definition: "Счёт в ресторане" },
      { term: "Tip", definition: "Чаевые" },
      { term: "Order", definition: "Заказ" }
    ]
  },
  "Урок 19: Покупки": {
    examples: [
      "— How much does this cost? — It's five pounds ninety-nine.",
      "— Can I try this on? — Of course, the fitting room is over there."
    ],
    facts: [
      "В английском вопрос о цене: How much is it? или How much does it cost?",
      "Британская валюта — фунт стерлингов (£, pound), 1 фунт = 100 пенсов (pence)",
      "Фраза on sale означает «со скидкой» в американском английском, а в британском — «в продаже»"
    ],
    quiz: [
      { question: "How do you ask about the price?", options: ["How many is it?", "How much is it?", "What cost it?", "How price?"], correct: 1 },
      { question: "What is the British currency?", options: ["Dollar", "Euro", "Pound sterling", "Franc"], correct: 2 },
      { question: "One pound equals:", options: ["10 pence", "50 pence", "100 pence", "200 pence"], correct: 2 },
      { question: "'Can I try this on?' means:", options: ["Можно купить?", "Можно примерить?", "Можно вернуть?", "Можно обменять?"], correct: 1 },
      { question: "'On sale' in American English means:", options: ["В продаже", "Со скидкой", "Распродано", "Дорого"], correct: 1 }
    ],
    find: [
      { text: "Сколько это стоит? — How ___ is it?", answer: "much" },
      { text: "Примерочная — fitting ___", answer: "room" },
      { text: "Покупать — to ___", answer: "buy" },
      { text: "Скидка — a ___", answer: "discount" },
      { text: "Наличные — ___", answer: "cash" }
    ],
    match: [
      { term: "Price", definition: "Цена" },
      { term: "Discount", definition: "Скидка" },
      { term: "Receipt", definition: "Чек" },
      { term: "Cash", definition: "Наличные деньги" },
      { term: "Shop", definition: "Магазин" }
    ]
  },
  "Урок 20: Одежда": {
    examples: [
      "She is wearing a red dress and black shoes. She looks very elegant.",
      "Зимой нужно носить тёплую куртку, шапку и перчатки — In winter you need a warm coat, a hat, and gloves."
    ],
    facts: [
      "Глагол wear (носить одежду) используется для того, что на вас надето сейчас, а put on — для действия «надеть»",
      "Слово clothes всегда множественного числа — нельзя сказать a clothe, можно a piece of clothing",
      "Размеры одежды в Англии отличаются от европейских: UK 10 ≈ EU 38"
    ],
    quiz: [
      { question: "Which verb means 'надеть' (action)?", options: ["Wear", "Put on", "Dress", "Carry"], correct: 1 },
      { question: "The word 'clothes' is:", options: ["Singular only", "Always plural", "Both singular and plural", "Uncountable"], correct: 1 },
      { question: "'She is wearing a red dress' means:", options: ["Она надевает красное платье", "На ней красное платье", "Она покупает платье", "Она шьёт платье"], correct: 1 },
      { question: "Which is NOT a clothing item?", options: ["Scarf", "Gloves", "Umbrella", "Hat"], correct: 2 },
      { question: "UK clothing size 10 is approximately EU size:", options: ["34", "36", "38", "40"], correct: 2 }
    ],
    find: [
      { text: "Надевать одежду — put ___", answer: "on" },
      { text: "Платье по-английски — ___", answer: "dress" },
      { text: "Куртка — ___", answer: "jacket" },
      { text: "Обувь — a pair of ___", answer: "shoes" },
      { text: "Перчатки — a pair of ___", answer: "gloves" }
    ],
    match: [
      { term: "Coat", definition: "Пальто" },
      { term: "Scarf", definition: "Шарф" },
      { term: "Boots", definition: "Сапоги" },
      { term: "Trousers", definition: "Брюки" },
      { term: "Sweater", definition: "Свитер" }
    ]
  },
  "Урок 21: Present Simple": {
    examples: [
      "She plays tennis every Saturday. She doesn't like football.",
      "— Do you speak English? — Yes, I do. / No, I don't."
    ],
    facts: [
      "Present Simple используется для регулярных действий, привычек и общих истин: The Sun rises in the east",
      "В 3-м лице единственного числа к глаголу добавляется -s/-es: I play → He plays, She watches",
      "Отрицательная форма образуется с don't/doesn't: I don't know, She doesn't understand"
    ],
    quiz: [
      { question: "Which sentence is in Present Simple?", options: ["She is playing now", "She plays every day", "She played yesterday", "She will play tomorrow"], correct: 1 },
      { question: "What ending does a verb have in the 3rd person singular?", options: ["-ed", "-ing", "-s/-es", "-er"], correct: 2 },
      { question: "The negative form 'She doesn't like' means:", options: ["Ей нравится", "Ей не нравится", "Ей нравилось", "Ей понравится"], correct: 1 },
      { question: "Which is a general truth in Present Simple?", options: ["I am eating now", "The Sun rises in the east", "She went home", "They will come"], correct: 1 },
      { question: "How do you form a question in Present Simple?", options: ["She likes?", "Does she like?", "Do she like?", "Is she like?"], correct: 1 }
    ],
    find: [
      { text: "Он играет в футбол — He ___ football.", answer: "plays" },
      { text: "Она не любит кофе — She ___ like coffee.", answer: "doesn't" },
      { text: "Ты говоришь по-английски? — ___ you speak English?", answer: "Do" },
      { text: "Мы живём в Москве — We ___ in Moscow.", answer: "live" },
      { text: "Солнце встаёт на востоке — The Sun ___ in the east.", answer: "rises" }
    ],
    match: [
      { term: "Present Simple", definition: "Время для регулярных действий" },
      { term: "doesn't", definition: "Отрицание для he/she/it" },
      { term: "don't", definition: "Отрицание для I/you/we/they" },
      { term: "Does", definition: "Вопросительное слово для he/she/it" },
      { term: "-s/-es", definition: "Окончание глагола в 3-м лице" }
    ]
  },
  "Урок 22: Present Continuous": {
    examples: [
      "She is reading a book right now. She isn't watching TV.",
      "— What are you doing? — I am doing my homework."
    ],
    facts: [
      "Present Continuous образуется с am/is/are + глагол с окончанием -ing: I am reading",
      "Это время используется для действий, происходящих прямо сейчас или в текущий период",
      "Некоторые глаголы не употребляются в Continuous: know, like, want, understand — это stative verbs"
    ],
    quiz: [
      { question: "Which sentence is in Present Continuous?", options: ["She reads every day", "She is reading now", "She read yesterday", "She will read tomorrow"], correct: 1 },
      { question: "Present Continuous is formed with:", options: ["have + V3", "am/is/are + V-ing", "did + V1", "will + V1"], correct: 1 },
      { question: "Which verb is NOT used in Continuous?", options: ["Run", "Read", "Know", "Play"], correct: 2 },
      { question: "'She isn't watching TV' means:", options: ["Она смотрит телевизор", "Она не смотрит телевизор сейчас", "Она не любит телевизор", "Она смотрела телевизор"], correct: 1 },
      { question: "Which signal word goes with Present Continuous?", options: ["Every day", "Usually", "Right now", "Often"], correct: 2 }
    ],
    find: [
      { text: "Она читает сейчас — She ___ reading now.", answer: "is" },
      { text: "Я делаю уроки — I am ___ my homework.", answer: "doing" },
      { text: "Они играют в футбол — They ___ playing football.", answer: "are" },
      { text: "Он не спит — He ___ sleeping.", answer: "isn't" },
      { text: "Что ты делаешь? — What ___ you doing?", answer: "are" }
    ],
    match: [
      { term: "Present Continuous", definition: "Время для действий в данный момент" },
      { term: "am/is/are + V-ing", definition: "Формула Present Continuous" },
      { term: "Right now", definition: "Маркер Present Continuous" },
      { term: "Stative verbs", definition: "Глаголы, не используемые в Continuous" },
      { term: "isn't/aren't", definition: "Отрицание в Present Continuous" }
    ]
  },
  "Урок 23: Past Simple": {
    examples: [
      "I visited my grandmother last weekend. We had a great time together.",
      "— Did you watch the film yesterday? — Yes, I did. It was interesting!"
    ],
    facts: [
      "Past Simple правильных глаголов образуется добавлением -ed: play → played, watch → watched",
      "Неправильные глаголы имеют особые формы прошедшего времени: go → went, see → saw, eat → ate",
      "Вопросительная форма образуется с Did: Did you go? — отрицательная: didn't + глагол в начальной форме"
    ],
    quiz: [
      { question: "How do regular verbs form Past Simple?", options: ["Adding -ing", "Adding -s", "Adding -ed", "Adding -er"], correct: 2 },
      { question: "What is the past form of 'go'?", options: ["Goed", "Gone", "Went", "Going"], correct: 2 },
      { question: "'Did you watch the film?' — the main verb is in:", options: ["Past form", "Base form", "V-ing form", "V3 form"], correct: 1 },
      { question: "Which signal word goes with Past Simple?", options: ["Now", "Every day", "Yesterday", "Tomorrow"], correct: 2 },
      { question: "'She didn't play' means:", options: ["Она играла", "Она не играла", "Она играет", "Она будет играть"], correct: 1 }
    ],
    find: [
      { text: "Я играл вчера — I ___ yesterday.", answer: "played" },
      { text: "Она пошла в магазин — She ___ to the shop.", answer: "went" },
      { text: "Ты смотрел фильм? — ___ you watch the film?", answer: "Did" },
      { text: "Он не пришёл — He ___ come.", answer: "didn't" },
      { text: "Мы видели медведя — We ___ a bear.", answer: "saw" }
    ],
    match: [
      { term: "Past Simple", definition: "Прошедшее простое время" },
      { term: "-ed", definition: "Окончание правильных глаголов" },
      { term: "Did", definition: "Вспомогательный глагол для вопросов" },
      { term: "didn't", definition: "Отрицание в Past Simple" },
      { term: "Irregular verbs", definition: "Неправильные глаголы" }
    ]
  },
  "Урок 24: Future Simple": {
    examples: [
      "I will help you with your homework tomorrow.",
      "— Will you come to the party? — Yes, I will. / No, I won't.",
      "She will be a great doctor one day.",
      "It will rain tomorrow, so take an umbrella."
    ],
    facts: [
      "Future Simple образуется с will + глагол в начальной форме: I will go, She will come",
      "Отрицательная форма: will not = won't — I won't forget your birthday",
      "Future Simple используется для обещаний, предсказаний и спонтанных решений: I'll answer the phone!"
    ],
    quiz: [
      { question: "How is Future Simple formed?", options: ["am/is/are + V-ing", "will + V1", "did + V1", "has + V3"], correct: 1 },
      { question: "What is the short form of 'will not'?", options: ["willn't", "won't", "wouldn't", "don't"], correct: 1 },
      { question: "Future Simple is used for:", options: ["Past habits", "Actions right now", "Promises and predictions", "Regular routines"], correct: 2 },
      { question: "'I'll answer the phone!' is an example of:", options: ["A habit", "A spontaneous decision", "A past event", "A regular action"], correct: 1 },
      { question: "Which signal word goes with Future Simple?", options: ["Yesterday", "Now", "Tomorrow", "Every day"], correct: 2 }
    ],
    find: [
      { text: "Я помогу тебе — I ___ help you.", answer: "will" },
      { text: "Она не придёт — She ___ come.", answer: "won't" },
      { text: "Ты будешь учиться? — ___ you study?", answer: "Will" },
      { text: "Завтра будет дождь — It will ___ tomorrow.", answer: "rain" },
      { text: "Мы поедем в Лондон — We will ___ to London.", answer: "go" }
    ],
    match: [
      { term: "Future Simple", definition: "Будущее простое время" },
      { term: "will", definition: "Вспомогательный глагол будущего времени" },
      { term: "won't", definition: "Отрицание в Future Simple" },
      { term: "Tomorrow", definition: "Маркер будущего времени" },
      { term: "Promise", definition: "Обещание (типичная ситуация для Future Simple)" }
    ]
  }
};

// ========== GEOGRAPHY DATA ==========
const geographyData = {
  "Урок 1: Вселенная и Солнечная система": {
    examples: [
      "Если бы Солнце было размером с basketball, Земля была бы размером с горошину",
      "Расстояние от Земли до Луны — около 384 000 км, туда лететь 3 дня"
    ],
    facts: [
      "Вселенная возникла около 13,8 миллиардов лет назад в результате Большого взрыва",
      "Наша галактика Млечный Путь содержит от 200 до 400 миллиардов звёзд",
      "Ближайшая к Солнцу звезда Проксима Центавра находится на расстоянии 4,24 световых лет"
    ],
    quiz: [
      { question: "Сколько планет в Солнечной системе?", options: ["6", "7", "8", "9"], correct: 2 },
      { question: "Что такое Млечный Путь?", options: ["Река", "Туманность", "Наша галактика", "Созвездие"], correct: 2 },
      { question: "Какая планета самая большая в Солнечной системе?", options: ["Сатурн", "Нептун", "Земля", "Юпитер"], correct: 3 },
      { question: "Сколько лет существует Вселенная?", options: ["1 миллиард", "5 миллиардов", "13,8 миллиардов", "20 миллиардов"], correct: 2 },
      { question: "Солнце — это:", options: ["Планета", "Звезда", "Спутник", "Астероид"], correct: 1 }
    ],
    find: [
      { text: "Наша галактика называется ___ Путь", answer: "Млечный" },
      { text: "В Солнечной системе ___ планет", answer: "8" },
      { text: "Ближайшая к нам звезда — ___", answer: "Солнце" },
      { text: "Вселенная возникла от Большого ___", answer: "взрыва" },
      { text: "Солнечная ___ состоит из Солнца и планет", answer: "система" }
    ],
    match: [
      { term: "Вселенная", definition: "Всё существующее пространство и материя" },
      { term: "Галактика", definition: "Система из миллиардов звёзд" },
      { term: "Солнце", definition: "Ближайшая к Земле звезда" },
      { term: "Планета", definition: "Небесное тело, вращающееся вокруг звезды" },
      { term: "Большой взрыв", definition: "Начало расширения Вселенной" }
    ]
  },
  "Урок 2: Планеты Солнечной системы": {
    examples: [
      "Сатурн знаменит своими кольцами из льда и камней",
      "Меркурий — самая близкая к Солнцу планета, а Венера — самая горячая"
    ],
    facts: [
      "Плутон был исключён из числа планет в 2006 году и переведён в категорию карликовых планет",
      "На Венере температура поверхности достигает 462°C — горячее, чем на Меркурии",
      "Марс называют «красной планетой» из-за оксида железа в его почве"
    ],
    quiz: [
      { question: "Какую планету исключили из числа планет в 2006 году?", options: ["Церера", "Эрида", "Плутон", "Седна"], correct: 2 },
      { question: "Какая планета самая горячая?", options: ["Меркурий", "Венера", "Марс", "Юпитер"], correct: 1 },
      { question: "Почему Марс называют «красной планетой»?", options: ["Из-за атмосферы", "Из-за оксида железа в почве", "Из-за температуры", "Из-за кратеров"], correct: 1 },
      { question: "Какая планета имеет кольца?", options: ["Юпитер", "Уран", "Нептун", "Сатурн"], correct: 3 },
      { question: "Планеты земной группы:", options: ["Юпитер, Сатурн", "Меркурий, Венера, Земля, Марс", "Уран, Нептун", "Плутон, Эрида"], correct: 1 }
    ],
    find: [
      { text: "Самая маленькая планета — ___", answer: "Меркурий" },
      { text: "Красная планета — ___", answer: "Марс" },
      { text: "Планета с кольцами — ___", answer: "Сатурн" },
      { text: "Бывшая девятая планета — ___", answer: "Плутон" },
      { text: "Самая горячая планета — ___", answer: "Венера" }
    ],
    match: [
      { term: "Меркурий", definition: "Ближайшая к Солнцу планета" },
      { term: "Венера", definition: "Самая горячая планета" },
      { term: "Земля", definition: "Единственная планета с жизнью" },
      { term: "Марс", definition: "Красная планета" },
      { term: "Юпитер", definition: "Крупнейшая планета Солнечной системы" }
    ]
  },
  "Урок 3: Земля — уникальная планета": {
    examples: [
      "На Земле есть жидкая вода — это главное условие для жизни",
      "Атмосфера Земли защищает нас от метеоритов и ультрафиолетового излучения"
    ],
    facts: [
      "Земля — единственная известная планета, на которой существует жизнь",
      "71% поверхности Земли покрыт водой, поэтому её называют «голубой планетой»",
      "Магнитное поле Земли защищает атмосферу от солнечного ветра и космического излучения"
    ],
    quiz: [
      { question: "Сколько процентов поверхности Земли покрыто водой?", options: ["51%", "61%", "71%", "81%"], correct: 2 },
      { question: "Почему Землю называют «голубой планетой»?", options: ["Из-за неба", "Из-за океанов", "Из-за атмосферы", "Из-за льда"], correct: 1 },
      { question: "Что защищает Землю от солнечного ветра?", options: ["Атмосфера", "Океаны", "Магнитное поле", "Озоновый слой"], correct: 2 },
      { question: "Что делает Землю уникальной?", options: ["Размер", "Наличие жизни", "Кольца", "Количество спутников"], correct: 1 },
      { question: "Какое условие необходимо для жизни на Земле?", options: ["Наличие кратеров", "Жидкая вода", "Высокая температура", "Отсутствие атмосферы"], correct: 1 }
    ],
    find: [
      { text: "Землю называют ___ планетой", answer: "голубой" },
      { text: "Магнитное ___ защищает Землю", answer: "поле" },
      { text: "У Земли один естественный спутник — ___", answer: "Луна" },
      { text: "71% Земли покрыт ___", answer: "водой" },
      { text: "Земля — третья планета от ___", answer: "Солнца" }
    ],
    match: [
      { term: "Голубая планета", definition: "Прозвище Земли из-за океанов" },
      { term: "Атмосфера", definition: "Воздушная оболочка Земли" },
      { term: "Магнитное поле", definition: "Защита от солнечного ветра" },
      { term: "Жидкая вода", definition: "Главное условие для жизни" },
      { term: "Луна", definition: "Единственный естественный спутник Земли" }
    ]
  },
  "Урок 4: Движения Земли": {
    examples: [
      "Земля совершает оборот вокруг своей оси за 24 часа — это сутки",
      "Полный оборот вокруг Солнца занимает 365 дней и 6 часов — это год"
    ],
    facts: [
      "Земля вращается вокруг своей оси со скоростью около 1670 км/ч на экваторе",
      "Наклон земной оси на 23,5° является причиной смены времён года",
      "Каждые 4 года добавляется високосный год (366 дней) из-за лишних 6 часов каждого года"
    ],
    quiz: [
      { question: "За какое время Земля совершает оборот вокруг своей оси?", options: ["12 часов", "24 часа", "365 дней", "30 дней"], correct: 1 },
      { question: "Что является причиной смены времён года?", options: ["Расстояние до Солнца", "Наклон земной оси", "Вращение Луны", "Скорость вращения"], correct: 1 },
      { question: "На сколько градусов наклонена земная ось?", options: ["15°", "23,5°", "30°", "45°"], correct: 1 },
      { question: "Что такое високосный год?", options: ["Год с 365 днями", "Год с 366 днями", "Год без зимы", "Год с двумя летами"], correct: 1 },
      { question: "Скорость вращения Земли на экваторе:", options: ["500 км/ч", "1000 км/ч", "1670 км/ч", "3000 км/ч"], correct: 2 }
    ],
    find: [
      { text: "Один оборот Земли вокруг оси — это ___", answer: "сутки" },
      { text: "Один оборот Земли вокруг Солнца — это ___", answer: "год" },
      { text: "Наклон земной оси — ___ градусов", answer: "23,5" },
      { text: "Високосный год длится ___ дней", answer: "366" },
      { text: "Смена времён года происходит из-за наклона земной ___", answer: "оси" }
    ],
    match: [
      { term: "Сутки", definition: "Оборот Земли вокруг своей оси (24 часа)" },
      { term: "Год", definition: "Оборот Земли вокруг Солнца (365 дней)" },
      { term: "Наклон оси", definition: "Причина смены времён года (23,5°)" },
      { term: "Високосный год", definition: "Год с 366 днями" },
      { term: "Вращение Земли", definition: "Движение вокруг оси и вокруг Солнца" }
    ]
  },
  "Урок 5: Изображения земной поверхности": {
    examples: [
      "Аэрофотосъёмка показывает Землю сверху, как если бы вы смотрели из самолёта",
      "На космическом снимке видно, что леса тёмно-зелёные, а пустыни — жёлто-коричневые"
    ],
    facts: [
      "Первые карты создавались на глиняных табличках более 4000 лет назад в Месопотамии",
      "Аэрофотосъёмка выполняется с самолётов и дронов, а космическая — со спутников",
      "План — изображение небольшого участка земной поверхности без учёта кривизны Земли"
    ],
    quiz: [
      { question: "Где были созданы первые карты?", options: ["В Египте", "В Месопотамии", "В Греции", "В Китае"], correct: 1 },
      { question: "Чем отличается план от карты?", options: ["Цветом", "План не учитывает кривизну Земли", "Размером бумаги", "Количеством деталей"], correct: 1 },
      { question: "Что такое аэрофотосъёмка?", options: ["Съёмка с горы", "Съёмка с воздуха", "Съёмка из космоса", "Съёмка с моря"], correct: 1 },
      { question: "Сколько лет самым древним картам?", options: ["1000 лет", "2000 лет", "Более 4000 лет", "500 лет"], correct: 2 },
      { question: "Космические снимки делают с помощью:", options: ["Самолётов", "Дронов", "Спутников", "Вертолётов"], correct: 2 }
    ],
    find: [
      { text: "Изображение небольшого участка без кривизны — ___", answer: "план" },
      { text: "Съёмка с воздуха — аэро___", answer: "фотосъёмка" },
      { text: "Первые карты созданы в ___", answer: "Месопотамии" },
      { text: "Снимки со спутников — космические ___", answer: "снимки" },
      { text: "Уменьшенное изображение Земли — ___", answer: "карта" }
    ],
    match: [
      { term: "План", definition: "Изображение участка без учёта кривизны" },
      { term: "Карта", definition: "Уменьшенное изображение Земли" },
      { term: "Аэрофотосъёмка", definition: "Съёмка поверхности с воздуха" },
      { term: "Космический снимок", definition: "Фото Земли из космоса" },
      { term: "Глобус", definition: "Объёмная модель Земли" }
    ]
  },
  "Урок 6: Масштаб и его виды": {
    examples: [
      "Масштаб 1:1000 означает, что 1 см на карте = 10 м на местности",
      "Масштаб 1:100 000 — мелкий (для карт стран), а 1:1000 — крупный (для планов зданий)"
    ],
    facts: [
      "Масштаб показывает, во сколько раз расстояние на карте меньше, чем на местности",
      "Виды масштаба: численный (1:1000), именованный (в 1 см — 10 м), линейный (графическая шкала)",
      "Чем меньше число в знаменателе масштаба, тем крупнее масштаб и тем подробнее карта"
    ],
    quiz: [
      { question: "Что показывает масштаб?", options: ["Цвет карты", "Во сколько раз уменьшено изображение", "Направление", "Рельеф"], correct: 1 },
      { question: "Какой масштаб крупнее?", options: ["1:1000", "1:10000", "1:100000", "1:1000000"], correct: 0 },
      { question: "Масштаб 1:1000 означает:", options: ["1 см = 1000 км", "1 см = 10 м", "1 см = 1000 м", "1 см = 1 км"], correct: 1 },
      { question: "Какой вид масштаба записывается как 1:1000?", options: ["Именованный", "Линейный", "Численный", "Графический"], correct: 2 },
      { question: "Для карты страны используют масштаб:", options: ["Крупный", "Средний", "Мелкий", "Любой"], correct: 2 }
    ],
    find: [
      { text: "Масштаб показывает степень ___ изображения", answer: "уменьшения" },
      { text: "1:1000 — это ___ масштаб", answer: "численный" },
      { text: "В 1 см — 10 м — это ___ масштаб", answer: "именованный" },
      { text: "Шкала на карте — ___ масштаб", answer: "линейный" },
      { text: "Чем ___ знаменатель, тем крупнее масштаб", answer: "меньше" }
    ],
    match: [
      { term: "Численный масштаб", definition: "Запись в виде 1:1000" },
      { term: "Именованный масштаб", definition: "Запись «в 1 см — 10 м»" },
      { term: "Линейный масштаб", definition: "Графическая шкала на карте" },
      { term: "Крупный масштаб", definition: "Подробная карта небольшого участка" },
      { term: "Мелкий масштаб", definition: "Карта большого участка с малой детализацией" }
    ]
  },
  "Урок 7: Условные знаки": {
    examples: [
      "Голубой цвет на карте — это вода: реки, озёра, моря",
      "Точка-пунктир означает тропу, а сплошная линия — дорогу"
    ],
    facts: [
      "Условные знаки — это символы, которыми на карте изображают объекты местности",
      "Три вида условных знаков: площадные (лес, озеро), линейные (река, дорога), внемасштабные (колодец, родник)",
      "Площадные знаки показывают объекты, занимающие большую территорию и сохраняющие свои очертания"
    ],
    quiz: [
      { question: "Что такое условные знаки?", options: ["Цвета карты", "Символы для изображения объектов", "Масштаб", "Градусная сетка"], correct: 1 },
      { question: "Какой знак относится к площадным?", options: ["Колодец", "Река", "Лес", "Дорога"], correct: 2 },
      { question: "К какому виду знаков относится река?", options: ["Площадной", "Линейный", "Внемасштабный", "Точечный"], correct: 1 },
      { question: "Каким цветом на карте обозначают воду?", options: ["Зелёным", "Жёлтым", "Голубым", "Коричневым"], correct: 2 },
      { question: "Внемасштабный знак используется для:", options: ["Больших территорий", "Малых объектов (колодец)", "Длинных объектов", "Рек"], correct: 1 }
    ],
    find: [
      { text: "Символы на карте — ___ знаки", answer: "условные" },
      { text: "Знак для леса — ___ знак", answer: "площадной" },
      { text: "Знак для дороги — ___ знак", answer: "линейный" },
      { text: "Вода на карте обозначена ___ цветом", answer: "голубым" },
      { text: "Знак для колодца — ___ знак", answer: "внемасштабный" }
    ],
    match: [
      { term: "Площадные знаки", definition: "Обозначают большие территории (лес, озеро)" },
      { term: "Линейные знаки", definition: "Обозначают протяжённые объекты (река, дорога)" },
      { term: "Внемасштабные знаки", definition: "Обозначают малые объекты (колодец, родник)" },
      { term: "Голубой цвет", definition: "Обозначает водные объекты" },
      { term: "Зелёный цвет", definition: "Обозначает растительность" }
    ]
  },
  "Урок 8: Ориентирование на местности": {
    examples: [
      "Компас всегда показывает на север — красная стрелка указывает направление",
      "В полдень Солнце находится на юге, тень от предметов падает на север"
    ],
    facts: [
      "Компас — прибор для определения сторон горизонта, его стрелка всегда указывает на север",
      "Основные стороны горизонта: север, юг, запад, восток; промежуточные: северо-запад, северо-восток и др.",
      "Азимут — угол между направлением на север и на предмет, измеряется по часовой стрелке от 0° до 360°"
    ],
    quiz: [
      { question: "Куда всегда указывает стрелка компаса?", options: ["На юг", "На восток", "На север", "На запад"], correct: 2 },
      { question: "Что такое азимут?", options: ["Расстояние до предмета", "Угол от севера до предмета", "Высота предмета", "Скорость движения"], correct: 1 },
      { question: "Сколько основных сторон горизонта?", options: ["2", "4", "6", "8"], correct: 1 },
      { question: "Где находится Солнце в полдень в северном полушарии?", options: ["На севере", "На юге", "На западе", "На востоке"], correct: 1 },
      { question: "Азимут измеряется от 0° до:", options: ["90°", "180°", "270°", "360°"], correct: 3 }
    ],
    find: [
      { text: "Прибор для ориентирования — ___", answer: "компас" },
      { text: "Угол от севера до предмета — ___", answer: "азимут" },
      { text: "Основные стороны горизонта: север, юг, запад и ___", answer: "восток" },
      { text: "В полдень тень падает на ___", answer: "север" },
      { text: "Стрелка компаса указывает на ___", answer: "север" }
    ],
    match: [
      { term: "Компас", definition: "Прибор для определения сторон горизонта" },
      { term: "Азимут", definition: "Угол между севером и направлением на предмет" },
      { term: "Север", definition: "Направление, куда указывает стрелка компаса" },
      { term: "Ориентирование", definition: "Определение своего положения на местности" },
      { term: "Горизонт", definition: "Видимая граница неба и земли" }
    ]
  },
  "Урок 9: Градусная сетка и географические координаты": {
    examples: [
      "Координаты Москвы: 56° с.ш. и 38° в.д. — это её точный «адрес» на Земле",
      "Экватор — это нулевая параллель, он делит Землю на северное и южное полушария"
    ],
    facts: [
      "Географическая широта измеряется от 0° до 90° к северу или югу от экватора",
      "Географическая долгота измеряется от 0° до 180° к востоку или западу от нулевого меридиана (Гринвичского)",
      "Гринвичский меридиан проходит через обсерваторию в Лондоне и считается нулевым"
    ],
    quiz: [
      { question: "Что такое экватор?", options: ["Самый длинный меридиан", "Нулевая параллель", "Самый короткий меридиан", "Гринвичский меридиан"], correct: 1 },
      { question: "От какого меридиана отсчитывается долгота?", options: ["От 90-го", "От Гринвичского", "От экватора", "От 180-го"], correct: 1 },
      { question: "В каких пределах измеряется широта?", options: ["0–180°", "0–90°", "0–360°", "0–45°"], correct: 1 },
      { question: "Где находится Гринвичская обсерватория?", options: ["В Париже", "В Москве", "В Лондоне", "В Нью-Йорке"], correct: 2 },
      { question: "Экватор делит Землю на:", options: ["Восточное и западное", "Северное и южное полушария", "Тёплое и холодное", "Сухое и влажное"], correct: 1 }
    ],
    find: [
      { text: "Нулевая параллель — ___", answer: "экватор" },
      { text: "Нулевой меридиан — ___", answer: "Гринвичский" },
      { text: "Широта измеряется от 0° до ___°", answer: "90" },
      { text: "Долгота измеряется от 0° до ___°", answer: "180" },
      { text: "Координаты — это «___» точки на Земле", answer: "адрес" }
    ],
    match: [
      { term: "Параллель", definition: "Линия, параллельная экватору" },
      { term: "Меридиан", definition: "Линия от полюса до полюса" },
      { term: "Широта", definition: "Расстояние от экватора к северу или югу" },
      { term: "Долгота", definition: "Расстояние от Гринвича к востоку или западу" },
      { term: "Экватор", definition: "Нулевая параллель, делит Землю на полушария" }
    ]
  },
  "Урок 10: Внутреннее строение Земли": {
    examples: [
      "Земная кора — самый тонкий слой Земли, её толщина от 5 до 70 км",
      "Ядро Земли — самое горячее, температура достигает 6000°C, как на поверхности Солнца"
    ],
    facts: [
      "Земля состоит из трёх основных слоёв: земная кора, мантия и ядро",
      "Мантия — самый толстый слой Земли (около 2900 км), она составляет 83% объёма планеты",
      "Ядро Земли состоит из внешнего жидкого и внутреннего твёрдого, именно оно создаёт магнитное поле"
    ],
    quiz: [
      { question: "Какой слой Земли самый тонкий?", options: ["Мантия", "Ядро", "Земная кора", "Литосфера"], correct: 2 },
      { question: "Какой слой составляет 83% объёма Земли?", options: ["Кора", "Мантия", "Ядро", "Атмосфера"], correct: 1 },
      { question: "Какая температура в центре Земли?", options: ["1000°C", "3000°C", "Около 6000°C", "10000°C"], correct: 2 },
      { question: "Что создаёт магнитное поле Земли?", options: ["Кора", "Мантия", "Движение жидкого ядра", "Атмосфера"], correct: 2 },
      { question: "Сколько основных слоёв у Земли?", options: ["2", "3", "4", "5"], correct: 1 }
    ],
    find: [
      { text: "Самый тонкий слой Земли — земная ___", answer: "кора" },
      { text: "Самый толстый слой — ___", answer: "мантия" },
      { text: "Центр Земли — ___", answer: "ядро" },
      { text: "Толщина мантии — около ___ км", answer: "2900" },
      { text: "Магнитное поле создаёт жидкое ___", answer: "ядро" }
    ],
    match: [
      { term: "Земная кора", definition: "Самый тонкий внешний слой Земли" },
      { term: "Мантия", definition: "Самый толстый слой (83% объёма)" },
      { term: "Ядро", definition: "Центр Земли, температура ~6000°C" },
      { term: "Литосфера", definition: "Кора и верхняя часть мантии" },
      { term: "Магнитное поле", definition: "Создаётся движением жидкого ядра" }
    ]
  },
  "Урок 11: Горные породы и минералы": {
    examples: [
      "Гранит — одна из самых распространённых горных пород, из неё делают памятники и ступени",
      "Мрамор образуется из известняка под действием высокой температуры и давления"
    ],
    facts: [
      "Горные породы делятся на три группы: магматические, осадочные и метаморфические",
      "Магматические породы образуются при остывании магмы: гранит, базальт, обсидиан",
      "Осадочные породы формируются из обломков других пород и остатков организмов: песчаник, известняк, мел"
    ],
    quiz: [
      { question: "Какие горные породы образуются из магмы?", options: ["Осадочные", "Метаморфические", "Магматические", "Органические"], correct: 2 },
      { question: "К какой группе относится песчаник?", options: ["Магматической", "Осадочной", "Метаморфической", "Вулканической"], correct: 1 },
      { question: "Из чего образуется мрамор?", options: ["Из гранита", "Из базальта", "Из известняка", "Из песка"], correct: 2 },
      { question: "Сколько групп горных пород существует?", options: ["2", "3", "4", "5"], correct: 1 },
      { question: "Что такое минерал?", options: ["Горная порода", "Природное вещество с определённым составом", "Искусственный камень", "Вид почвы"], correct: 1 }
    ],
    find: [
      { text: "Породы из магмы — ___ породы", answer: "магматические" },
      { text: "Породы из обломков и остатков — ___ породы", answer: "осадочные" },
      { text: "Породы, изменённые температурой и давлением — ___", answer: "метаморфические" },
      { text: "Гранит — ___ горная порода", answer: "магматическая" },
      { text: "Мел — ___ горная порода", answer: "осадочная" }
    ],
    match: [
      { term: "Магматические породы", definition: "Образуются при остывании магмы" },
      { term: "Осадочные породы", definition: "Формируются из обломков и остатков" },
      { term: "Метаморфические породы", definition: "Изменены температурой и давлением" },
      { term: "Гранит", definition: "Распространённая магматическая порода" },
      { term: "Мрамор", definition: "Метаморфическая порода из известняка" }
    ]
  },
  "Урок 12: Рельеф Земли — горы и равнины": {
    examples: [
      "Эверест — высочайшая вершина мира (8848 м), находится в Гималаях",
      "Восточно-Европейская равнина — одна из крупнейших равнин на Земле"
    ],
    facts: [
      "Рельеф — это совокупность неровностей земной поверхности: горы, равнины, впадины",
      "Горы делятся по высоте: низкие (до 1000 м), средние (1000–2000 м), высокие (свыше 2000 м)",
      "Равнины занимают около 60% поверхности суши и бывают плоскими и холмистыми"
    ],
    quiz: [
      { question: "Какая вершина самая высокая в мире?", options: ["Килиманджаро", "Эльбрус", "Эверест", "Монблан"], correct: 2 },
      { question: "Какой процент суши занимают равнины?", options: ["30%", "40%", "60%", "80%"], correct: 2 },
      { question: "Горы высотой до 1000 м называются:", options: ["Высокими", "Средними", "Низкими", "Гигантскими"], correct: 2 },
      { question: "Что такое рельеф?", options: ["Климат", "Неровности земной поверхности", "Тип почвы", "Вид растительности"], correct: 1 },
      { question: "Где находятся Гималаи?", options: ["В Европе", "В Африке", "В Азии", "В Южной Америке"], correct: 2 }
    ],
    find: [
      { text: "Неровности земной поверхности — ___", answer: "рельеф" },
      { text: "Самая высокая вершина — ___", answer: "Эверест" },
      { text: "Плоские и холмистые участки суши — ___", answer: "равнины" },
      { text: "Высокие горы — выше ___ м", answer: "2000" },
      { text: "Эверест находится в горах ___", answer: "Гималаи" }
    ],
    match: [
      { term: "Рельеф", definition: "Совокупность неровностей земной поверхности" },
      { term: "Горы", definition: "Высокие возвышенности с крутыми склонами" },
      { term: "Равнины", definition: "Плоские или холмистые участки суши" },
      { term: "Эверест", definition: "Высочайшая вершина мира (8848 м)" },
      { term: "Низкие горы", definition: "Горы высотой до 1000 м" }
    ]
  },
  "Урок 13: Движения земной коры": {
    examples: [
      "Землетрясения происходят при резком смещении участков земной коры",
      "Вулканические извержения выбрасывают магму, пепел и газы на поверхность"
    ],
    facts: [
      "Землетрясения измеряются по шкале Рихтера от 1 до 10 баллов",
      "Вулканы бывают действующие, уснувшие и потухшие — действующих на Земле более 1500",
      "Медленные движения земной коры (до нескольких см в год) называют тектоническими движениями"
    ],
    quiz: [
      { question: "По какой шкале измеряют силу землетрясений?", options: ["Цельсия", "Бофорта", "Рихтера", "Мооса"], correct: 2 },
      { question: "Сколько действующих вулканов на Земле?", options: ["100", "500", "Более 1500", "5000"], correct: 2 },
      { question: "Какие вулканы могут извергаться?", options: ["Только действующие", "Действующие и уснувшие", "Только потухшие", "Все вулканы"], correct: 1 },
      { question: "Тектонические движения — это:", options: ["Быстрые землетрясения", "Медленные перемещения земной коры", "Извержения вулканов", "Движения воды"], correct: 1 },
      { question: "Что выбрасывает вулкан при извержении?", options: ["Только воду", "Магму, пепел, газы", "Только дым", "Только камни"], correct: 1 }
    ],
    find: [
      { text: "Сила землетрясения измеряется в ___", answer: "баллах" },
      { text: "Шкала для землетрясений — шкала ___", answer: "Рихтера" },
      { text: "Вулкан, который может извергаться — ___", answer: "действующий" },
      { text: "Медленные движения земной коры — ___ движения", answer: "тектонические" },
      { text: "Расплавленная порода внутри Земли — ___", answer: "магма" }
    ],
    match: [
      { term: "Землетрясение", definition: "Резкое смещение участков земной коры" },
      { term: "Вулкан", definition: "Гора с каналом, по которому магма выходит наружу" },
      { term: "Действующий вулкан", definition: "Вулкан, который может извергаться" },
      { term: "Тектонические движения", definition: "Медленные перемещения земной коры" },
      { term: "Шкала Рихтера", definition: "Шкала для измерения силы землетрясений" }
    ]
  },
  "Урок 14: Мировой океан": {
    examples: [
      "Мировой океан покрывает 71% поверхности Земли и делится на 4 океана",
      "Марианская впадина — самое глубокое место в океане (10 994 м)"
    ],
    facts: [
      "Мировой океан делится на четыре океана: Тихий, Атлантический, Индийский, Северный Ледовитый",
      "Тихий океан — самый большой и глубокий океан, он занимает около 1/3 поверхности Земли",
      "Солёность океанской воды составляет в среднем 35 промилле (35 г соли на 1 кг воды)"
    ],
    quiz: [
      { question: "Сколько океанов на Земле?", options: ["3", "4", "5", "6"], correct: 1 },
      { question: "Какой океан самый большой?", options: ["Атлантический", "Индийский", "Тихий", "Северный Ледовитый"], correct: 2 },
      { question: "Какова средняя солёность океанской воды?", options: ["10 промилле", "20 промилле", "35 промилле", "50 промилле"], correct: 2 },
      { question: "Марианская впадина имеет глубину:", options: ["5000 м", "8000 м", "Около 11 000 м", "15 000 м"], correct: 2 },
      { question: "Какую часть поверхности Земли занимает океан?", options: ["51%", "61%", "71%", "81%"], correct: 2 }
    ],
    find: [
      { text: "Самый большой океан — ___", answer: "Тихий" },
      { text: "Самое глубокое место — ___ впадина", answer: "Марианская" },
      { text: "Средняя солёность — ___ промилле", answer: "35" },
      { text: "Часть океана, вдающаяся в сушу — ___", answer: "море" },
      { text: "Мировой ___ покрывает 71% Земли", answer: "океан" }
    ],
    match: [
      { term: "Тихий океан", definition: "Самый большой и глубокий океан" },
      { term: "Марианская впадина", definition: "Самое глубокое место в океане" },
      { term: "Солёность", definition: "Количество соли в океанской воде" },
      { term: "Море", definition: "Часть океана, вдающаяся в сушу" },
      { term: "Залив", definition: "Часть моря или океана, вдающаяся в сушу" }
    ]
  },
  "Урок 15: Воды суши": {
    examples: [
      "Река Нил — самая длинная река в мире (6671 км), она протекает через Африку",
      "Озеро Байкал — самое глубокое пресное озеро (1642 м), содержит 20% мировых запасов пресной воды"
    ],
    facts: [
      "Реки делятся на равнинные (тихие, широкие) и горные (быстрые, порожистые)",
      "Озёра бывают пресными и солёными — самое солёное озеро — Мёртвое море",
      "Подземные воды — важнейший источник питьевой воды, они образуются при просачивании осадков в почву"
    ],
    quiz: [
      { question: "Какая река самая длинная в мире?", options: ["Амазонка", "Нил", "Волга", "Миссисипи"], correct: 1 },
      { question: "Какое озеро самое глубокое?", options: ["Каспийское", "Ладожское", "Байкал", "Мёртвое море"], correct: 2 },
      { question: "Какое озеро самое солёное?", options: ["Байкал", "Мёртвое море", "Каспийское", "Онежское"], correct: 1 },
      { question: "Откуда берутся подземные воды?", options: ["Из океана", "Из просачивания осадков", "Из лавы", "Из озёр"], correct: 1 },
      { question: "Горные реки отличаются:", options: ["Тихим течением", "Быстрым течением и порогами", "Широкой долиной", "Отсутствием рыбы"], correct: 1 }
    ],
    find: [
      { text: "Самая длинная река — ___", answer: "Нил" },
      { text: "Самое глубокое озеро — ___", answer: "Байкал" },
      { text: "Самое солёное озеро — ___ море", answer: "Мёртвое" },
      { text: "Вода под землёй — ___ воды", answer: "подземные" },
      { text: "Начало реки — ___", answer: "исток" }
    ],
    match: [
      { term: "Река", definition: "Поток воды, текущий по руслу" },
      { term: "Озеро", definition: "Замкнутый водоём в углублении суши" },
      { term: "Подземные воды", definition: "Вода, находящаяся под землёй" },
      { term: "Исток", definition: "Начало реки" },
      { term: "Устье", definition: "Место впадения реки в другой водоём" }
    ]
  },
  "Урок 16: Ледники и многолетняя мерзлота": {
    examples: [
      "Ледник Антарктиды содержит 90% мирового льда — если он растает, уровень океана поднимется на 60 м",
      "Многолетняя мерзлота занимает около 25% территории России"
    ],
    facts: [
      "Ледники образуются там, где снега выпадает больше, чем успевает растаять за лето",
      "Многолетняя мерзлота — это постоянно мёрзлый грунт, который не оттаивает годами",
      "Ледники бывают горными (в горах) и покровными (покрывают огромные территории, как в Антарктиде)"
    ],
    quiz: [
      { question: "Сколько процентов мирового льда содержит Антарктида?", options: ["50%", "70%", "90%", "100%"], correct: 2 },
      { question: "Как образуется ледник?", options: ["Из дождя", "Снега больше, чем тает за лето", "Из подземных вод", "Из рек"], correct: 1 },
      { question: "Какой процент территории России занимает мерзлота?", options: ["5%", "15%", "25%", "50%"], correct: 2 },
      { question: "Покровные ледники находятся:", options: ["В горах", "В пустынях", "В Антарктиде и Гренландии", "В тропиках"], correct: 2 },
      { question: "Что такое многолетняя мерзлота?", options: ["Снег, который не тает летом", "Постоянно мёрзлый грунт", "Горный ледник", "Замёрзшая река"], correct: 1 }
    ],
    find: [
      { text: "90% мирового льда — в ___", answer: "Антарктиде" },
      { text: "Постоянно мёрзлый грунт — многолетняя ___", answer: "мерзлота" },
      { text: "Ледники в горах — ___ ледники", answer: "горные" },
      { text: "Ледники на равнинах — ___ ледники", answer: "покровные" },
      { text: "Если ледники Антарктиды растают, океан поднимется на ___ м", answer: "60" }
    ],
    match: [
      { term: "Ледник", definition: "Масса льда, медленно движущаяся по поверхности" },
      { term: "Многолетняя мерзлота", definition: "Постоянно мёрзлый грунт" },
      { term: "Горный ледник", definition: "Ледник, расположенный в горах" },
      { term: "Покровный ледник", definition: "Ледник, покрывающий огромную территорию" },
      { term: "Антарктида", definition: "Континент, содержащий 90% мирового льда" }
    ]
  },
  "Урок 17: Строение атмосферы": {
    examples: [
      "Тропосфера — самый нижний слой атмосферы, в нём образуются облака и погода",
      "В стратосфере находится озоновый слой, который защищает нас от ультрафиолета"
    ],
    facts: [
      "Атмосфера состоит из пяти основных слоёв: тропосфера, стратосфера, мезосфера, термосфера, экзосфера",
      "Тропосфера содержит 80% всей массы атмосферы и простирается до 10–12 км",
      "Озоновый слой в стратосфере поглощает до 99% опасного ультрафиолетового излучения Солнца"
    ],
    quiz: [
      { question: "Сколько основных слоёв в атмосфере?", options: ["3", "4", "5", "6"], correct: 2 },
      { question: "В каком слое формируется погода?", options: ["Стратосфера", "Мезосфера", "Тропосфера", "Термосфера"], correct: 2 },
      { question: "Где находится озоновый слой?", options: ["В тропосфере", "В стратосфере", "В мезосфере", "В экзосфере"], correct: 1 },
      { question: "Сколько процентов массы атмосферы в тропосфере?", options: ["50%", "60%", "70%", "80%"], correct: 3 },
      { question: "Какой слой атмосферы самый верхний?", options: ["Мезосфера", "Термосфера", "Стратосфера", "Экзосфера"], correct: 3 }
    ],
    find: [
      { text: "Нижний слой атмосферы — ___", answer: "тропосфера" },
      { text: "Озоновый слой в ___", answer: "стратосфере" },
      { text: "Самый верхний слой — ___", answer: "экзосфера" },
      { text: "Воздушная оболочка Земли — ___", answer: "атмосфера" },
      { text: "Озоновый слой защищает от ___ излучения", answer: "ультрафиолетового" }
    ],
    match: [
      { term: "Тропосфера", definition: "Нижний слой, где формируется погода" },
      { term: "Стратосфера", definition: "Слой с озоновым экраном" },
      { term: "Озоновый слой", definition: "Защищает от ультрафиолетового излучения" },
      { term: "Экзосфера", definition: "Самый верхний слой атмосферы" },
      { term: "Атмосфера", definition: "Воздушная оболочка Земли" }
    ]
  },
  "Урок 18: Температура воздуха": {
    examples: [
      "Температура уменьшается на 6°C при подъёме на каждый километр вверх",
      "Самая высокая температура на Земле (+56,7°C) зафиксирована в Долине Смерти (США)"
    ],
    facts: [
      "Температура воздуха измеряется термометром в градусах Цельсия (°C)",
      "Амплитуда температуры — это разница между самой высокой и самой низкой температурой за период",
      "На температуру влияют: широта, высота над уровнем моря, удалённость от океана, океанические течения"
    ],
    quiz: [
      { question: "На сколько градусов падает температура при подъёме на 1 км?", options: ["3°C", "6°C", "10°C", "2°C"], correct: 1 },
      { question: "В чём измеряется температура воздуха?", options: ["В градусах Фаренгейта", "В градусах Цельсия", "В кельвинах", "В миллиметрах"], correct: 1 },
      { question: "Что такое амплитуда температуры?", options: ["Средняя температура", "Разница между max и min", "Самая высокая температура", "Скорость изменения"], correct: 1 },
      { question: "Где зафиксирована самая высокая температура (+56,7°C)?", options: ["В Сахаре", "В Долине Смерти", "В Австралии", "В Индии"], correct: 1 },
      { question: "Какой фактор НЕ влияет на температуру?", options: ["Широта", "Высота над уровнем моря", "Цвет почвы", "Океанические течения"], correct: 2 }
    ],
    find: [
      { text: "Прибор для измерения температуры — ___", answer: "термометр" },
      { text: "Разница max и min температуры — ___", answer: "амплитуда" },
      { text: "Температура падает на ___°C на каждый километр", answer: "6" },
      { text: "Единица измерения температуры — градус ___", answer: "Цельсия" },
      { text: "Самая низкая температура на Земле — -89,2°C, на станции ___", answer: "Восток" }
    ],
    match: [
      { term: "Термометр", definition: "Прибор для измерения температуры" },
      { term: "Амплитуда", definition: "Разница между max и min температурой" },
      { term: "Градус Цельсия", definition: "Единица измерения температуры" },
      { term: "Долина Смерти", definition: "Место с самой высокой температурой (+56,7°C)" },
      { term: "Станция Восток", definition: "Место с самой низкой температурой (-89,2°C)" }
    ]
  },
  "Урок 19: Атмосферное давление и ветер": {
    examples: [
      "Нормальное атмосферное давление на уровне моря — 760 мм рт. ст.",
      "Ветер дует из области высокого давления в область низкого"
    ],
    facts: [
      "Атмосферное давление — сила, с которой воздух давит на земную поверхность",
      "Давление измеряется барометром в миллиметрах ртутного столба (мм рт. ст.) или гектопаскалях (гПа)",
      "При подъёме на каждые 10,5 м давление уменьшается примерно на 1 мм рт. ст."
    ],
    quiz: [
      { question: "Какое нормальное атмосферное давление на уровне моря?", options: ["640 мм рт. ст.", "760 мм рт. ст.", "860 мм рт. ст.", "1000 мм рт. ст."], correct: 1 },
      { question: "Куда дует ветер?", options: ["Из низкого в высокое", "Из высокого в низкое", "Не зависит от давления", "Только на север"], correct: 1 },
      { question: "Чем измеряют давление?", options: ["Термометром", "Гигрометром", "Барометром", "Анемометром"], correct: 2 },
      { question: "На сколько метров нужно подняться, чтобы давление упало на 1 мм рт. ст.?", options: ["5 м", "10,5 м", "20 м", "100 м"], correct: 1 },
      { question: "Что такое атмосферное давление?", options: ["Температура воздуха", "Сила давления воздуха на поверхность", "Скорость ветра", "Количество осадков"], correct: 1 }
    ],
    find: [
      { text: "Прибор для измерения давления — ___", answer: "барометр" },
      { text: "Нормальное давление — ___ мм рт. ст.", answer: "760" },
      { text: "Ветер дует из ___ давления в низкое", answer: "высокого" },
      { text: "Движение воздуха — ___", answer: "ветер" },
      { text: "На каждые 10,5 м давление падает на 1 мм ___", answer: "рт. ст." }
    ],
    match: [
      { term: "Барометр", definition: "Прибор для измерения давления" },
      { term: "Ветер", definition: "Движение воздуха из высокого в низкое давление" },
      { term: "760 мм рт. ст.", definition: "Нормальное атмосферное давление" },
      { term: "Циклон", definition: "Область низкого давления" },
      { term: "Антициклон", definition: "Область высокого давления" }
    ]
  },
  "Урок 20: Влага в атмосфере": {
    examples: [
      "Относительная влажность 100% означает, что воздух полностью насыщен влагой",
      "В тропических лесах влажность может достигать 95%, а в пустыне — всего 10–20%"
    ],
    facts: [
      "Влажность воздуха — это количество водяного пара в воздухе, измеряется гигрометром",
      "Облака образуются при охлаждении влажного воздуха — пар конденсируется в капли воды",
      "Осадки бывают жидкие (дождь) и твёрдые (снег, град), их количество измеряется осадкомером"
    ],
    quiz: [
      { question: "Каким прибором измеряют влажность?", options: ["Термометром", "Барометром", "Гигрометром", "Осадкомером"], correct: 2 },
      { question: "Что означает влажность 100%?", options: ["Идёт дождь", "Воздух полностью насыщен влагой", "Очень жарко", "Ветрено"], correct: 1 },
      { question: "Как образуются облака?", options: ["Из дыма", "При конденсации пара", "Из пыли", "Из озона"], correct: 1 },
      { question: "Какой вид осадков является твёрдым?", options: ["Дождь", "Роса", "Снег", "Туман"], correct: 2 },
      { question: "Влажность в пустыне обычно:", options: ["80–90%", "50–60%", "10–20%", "100%"], correct: 2 }
    ],
    find: [
      { text: "Количество пара в воздухе — ___ воздуха", answer: "влажность" },
      { text: "Прибор для влажности — ___", answer: "гигрометр" },
      { text: "Прибор для осадков — ___", answer: "осадкомер" },
      { text: "Процесс превращения пара в воду — ___", answer: "конденсация" },
      { text: "Твёрдые осадки: снег и ___", answer: "град" }
    ],
    match: [
      { term: "Влажность", definition: "Количество водяного пара в воздухе" },
      { term: "Гигрометр", definition: "Прибор для измерения влажности" },
      { term: "Конденсация", definition: "Превращение пара в жидкость" },
      { term: "Осадки", definition: "Вода, выпадающая из атмосферы" },
      { term: "Облака", definition: "Скопление капель воды в атмосфере" }
    ]
  },
  "Урок 21: Биосфера — сфера жизни": {
    examples: [
      "Биосфера включает все живые организмы от глубоководных рыб до бактерий в верхних слоях атмосферы",
      "Самые древние ископаемые останки живых организмов — строматолиты — имеют возраст 3,5 млрд лет"
    ],
    facts: [
      "Биосфера — оболочка Земли, населённая живыми организмами, включает часть литосферы, гидросферы и атмосферы",
      "Термин «биосфера» ввёл австрийский учёный Эдуард Зюсс в 1875 году",
      "Живые организмы существуют от глубин океана (до 11 км) до верхних слоёв атмосферы (до 20 км)"
    ],
    quiz: [
      { question: "Что такое биосфера?", options: ["Воздушная оболочка", "Водная оболочка", "Оболочка, населённая живыми организмами", "Каменная оболочка"], correct: 2 },
      { question: "Кто ввёл термин «биосфера»?", options: ["Вернадский", "Зюсс", "Дарвин", "Ломоносов"], correct: 1 },
      { question: "На какую глубину распространяется жизнь в океане?", options: ["1 км", "5 км", "До 11 км", "20 км"], correct: 2 },
      { question: "Биосфера включает:", options: ["Только атмосферу", "Части литосферы, гидросферы и атмосферы", "Только гидросферу", "Только литосферу"], correct: 1 },
      { question: "Возраст древнейших ископаемых организмов:", options: ["1 млрд лет", "2 млрд лет", "3,5 млрд лет", "5 млрд лет"], correct: 2 }
    ],
    find: [
      { text: "Сфера жизни — ___", answer: "биосфера" },
      { text: "Автор термина «биосфера» — Эдуард ___", answer: "Зюсс" },
      { text: "Биосфера включает части трёх ___", answer: "оболочек" },
      { text: "Древнейшие ископаемые — ___", answer: "строматолиты" },
      { text: "Наука о живых организмах — ___", answer: "биология" }
    ],
    match: [
      { term: "Биосфера", definition: "Оболочка Земли, населённая живыми организмами" },
      { term: "Зюсс", definition: "Учёный, введший термин «биосфера»" },
      { term: "Вернадский", definition: "Учёный, развивший учение о биосфере" },
      { term: "Строматолиты", definition: "Древнейшие ископаемые организмы" },
      { term: "Живые организмы", definition: "Главная составляющая биосферы" }
    ]
  },
  "Урок 22: Природные зоны": {
    examples: [
      "В тундре лето короткое и прохладное, а зима длинная и суровая — растут мхи и лишайники",
      "В экваториальных лесах жарко и влажно круглый год — больше всего видов растений и животных"
    ],
    facts: [
      "Природная зона — крупный природный комплекс с определённым климатом, почвами, растительностью и животными",
      "Главный фактор формирования природных зон — соотношение тепла и влаги",
      "На Земле выделяют более 10 природных зон: от арктических пустынь до экваториальных лесов"
    ],
    quiz: [
      { question: "Что такое природная зона?", options: ["Только климат", "Природный комплекс с климатом, почвами, флорой и фауной", "Только растительность", "Только животные"], correct: 1 },
      { question: "Главный фактор формирования природных зон:", options: ["Высота над уровнем моря", "Соотношение тепла и влаги", "Близость океана", "Направление ветров"], correct: 1 },
      { question: "Какая зона расположена ближе всего к экватору?", options: ["Тундра", "Тайга", "Экваториальный лес", "Пустыня"], correct: 2 },
      { question: "Что растёт в тундре?", options: ["Пальмы", "Мхи и лишайники", "Бананы", "Дубы"], correct: 1 },
      { question: "Сколько природных зон выделяют на Земле?", options: ["3", "5", "Более 10", "Более 50"], correct: 2 }
    ],
    find: [
      { text: "Природная зона определяется ___ и влагой", answer: "теплом" },
      { text: "Самая северная зона — арктическая ___", answer: "пустыня" },
      { text: "Зона вечной мерзлоты — ___", answer: "тундра" },
      { text: "Зона с наибольшим разнообразием видов — ___ лес", answer: "экваториальный" },
      { text: "Зона с очень малым количеством осадков — ___", answer: "пустыня" }
    ],
    match: [
      { term: "Арктическая пустыня", definition: "Зона льдов и снегов у полюсов" },
      { term: "Тундра", definition: "Зона мхов и лишайников с вечной мерзлотой" },
      { term: "Тайга", definition: "Зона хвойных лесов" },
      { term: "Саванна", definition: "Зона высоких трав и редких деревьев" },
      { term: "Экваториальный лес", definition: "Зона наибольшего видового разнообразия" }
    ]
  },
  "Урок 23: Охрана природы": {
    examples: [
      "Красная книга — список видов, которым угрожает исчезновение",
      "В России более 100 заповедников, где запрещена любая хозяйственная деятельность"
    ],
    facts: [
      "Заповедник — территория, где запрещена любая деятельность человека для сохранения природы",
      "Международная Красная книга содержит списки исчезающих видов животных и растений",
      "Ежегодно на Земле уничтожается около 10 миллионов гектаров леса — это площадь примерно равная Исландии"
    ],
    quiz: [
      { question: "Что такое заповедник?", options: ["Парк развлечений", "Территория с полным запретом деятельности человека", "Зоопарк", "Ферма"], correct: 1 },
      { question: "Что содержит Красная книга?", options: ["Рецепты", "Списки исчезающих видов", "Правила поведения", "Карты"], correct: 1 },
      { question: "Сколько гектаров леса уничтожается ежегодно?", options: ["1 миллион", "5 миллионов", "Около 10 миллионов", "50 миллионов"], correct: 2 },
      { question: "Сколько заповедников в России?", options: ["Около 20", "Около 50", "Более 100", "Более 500"], correct: 2 },
      { question: "Главная причина исчезновения видов:", options: ["Извержения вулканов", "Деятельность человека", "Метеориты", "Изменение орбиты Земли"], correct: 1 }
    ],
    find: [
      { text: "Книга исчезающих видов — Красная ___", answer: "книга" },
      { text: "Территория с полным запретом деятельности — ___", answer: "заповедник" },
      { text: "10 млн гектаров ___ уничтожается ежегодно", answer: "леса" },
      { text: "Охрана ___ — забота о сохранении природы", answer: "природы" },
      { text: "Национальный ___ — территория для сохранения и отдыха", answer: "парк" }
    ],
    match: [
      { term: "Заповедник", definition: "Территория с полным запретом деятельности человека" },
      { term: "Красная книга", definition: "Список исчезающих видов" },
      { term: "Национальный парк", definition: "Территория для сохранения природы и отдыха" },
      { term: "Экология", definition: "Наука о взаимодействии организмов и среды" },
      { term: "Рециклинг", definition: "Переработка отходов для повторного использования" }
    ]
  }
};

// ========== MAIN SCRIPT ==========
function processSubject(filename) {
  const filepath = path.join(BASE, filename);
  const data = JSON.parse(fs.readFileSync(filepath, 'utf-8'));
  const source = filename === 'english.json' ? englishData : geographyData;
  let lessonsProcessed = 0;

  for (const topic of data.lessons.detailedTopics) {
    for (const lesson of topic.lessons) {
      const lessonData = source[lesson.title];
      if (!lessonData) {
        console.warn(`  ⚠ No data for lesson: ${lesson.title}`);
        continue;
      }

      // Add examples (keep existing, add new)
      if (!lesson.examples) {
        lesson.examples = [];
      }
      for (const ex of lessonData.examples) {
        lesson.examples.push(ex);
      }

      // Add facts
      lesson.facts = lessonData.facts;

      // Add tests
      lesson.tests = {
        quiz: lessonData.quiz,
        find: lessonData.find,
        match: lessonData.match
      };

      lessonsProcessed++;
    }
  }

  // Write back
  fs.writeFileSync(filepath, JSON.stringify(data, null, 2), 'utf-8');
  console.log(`✅ ${filename}: processed ${lessonsProcessed} lessons`);
  return lessonsProcessed;
}

console.log('🔧 Fixing Grade 5 English + Geography...\n');
const engCount = processSubject('english.json');
const geoCount = processSubject('geography.json');
console.log(`\n🏁 Done! English: ${engCount} lessons, Geography: ${geoCount} lessons`);
