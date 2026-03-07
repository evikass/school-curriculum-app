import { SubjectData, GameLesson } from '@/data/types'
const L = (t: string, d: string, tasks: string[]) => ({ title: t, description: d, tasks })

export const lessons: SubjectData = {
  title: "Иностранный язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: ["Знакомство", "Мир вокруг нас", "Семья и друзья", "Школа", "Путешествия", "Грамматика"],
  detailedTopics: [
    {
      topic: "Знакомство и общение",
      lessons: [
        L("Урок 1: Приветствие и прощание", "В английском языке существует несколько способов поздороваться. Самые распространённые: Hello (здравствуйте), Hi (привет — более неформальное), Good morning (доброе утро), Good afternoon (добрый день), Good evening (добрый вечер). Для прощания используются: Goodbye (до свидания), Bye (пока), See you later (увидимся позже), Good night (спокойной ночи). Важно выбирать подходящее приветствие в зависимости от ситуации и времени суток.", [
          "Приветствовать разными способами",
          "Прощаться по-английски",
          "Знакомиться с людьми",
          "Представлять себя и других",
          "Использовать вежливые фразы",
          "Различать формальный и неформальный стиль"
        ]),
        L("Урок 2: Личная информация", "При знакомстве люди обмениваются личной информацией. Фразы: What is your name? (Как тебя зовут?), My name is... (Меня зовут...), How old are you? (Сколько тебе лет?), I am... years old (Мне... лет), Where are you from? (Откуда ты?), I am from... (Я из...), What is your address? (Какой твой адрес?), What is your phone number? (Какой твой номер телефона?). Числительные от 1 до 100 необходимы для называния возраста, номера телефона и адреса.", [
          "Называть имя и фамилию",
          "Говорить о возрасте",
          "Рассказывать о себе",
          "Задавать вопросы о человеке",
          "Использовать числительные",
          "Заполнять анкету на английском"
        ]),
        L("Урок 3: Страны и национальности", "Названия стран и национальностей в английском языке часто отличаются. Страны: Russia (Россия), Great Britain (Великобритания), the USA (США), France (Франция), Germany (Германия), Spain (Испания), Italy (Италия), China (Китай), Japan (Япония). Национальности: Russian (русский), British (британский), American (американский), French (французский), German (немецкий). Конструкция: I am from Russia. I am Russian. (Я из России. Я русский.)", [
          "Называть страны на английском",
          "Определять национальности",
          "Говорить «Я из...»",
          "Спрашивать о происхождении",
          "Различать страну и национальность",
          "Работать с картой мира"
        ]),
        L("Урок 4: Профессии", "Названия профессий образуются с помощью суффиксов -er, -or, -ist. Профессии: teacher (учитель), doctor (врач), engineer (инженер), driver (водитель), worker (рабочий), actor (актёр), scientist (учёный), artist (художник), writer (писатель), pilot (лётчик), cook (повар). Фразы: What is your job? (Кем ты работаешь?), What do you do? (Чем ты занимаешься?), I am a teacher. (Я учитель.), I want to be a doctor. (Я хочу быть врачом.)", [
          "Называть профессии",
          "Спрашивать о работе",
          "Рассказывать о профессии",
          "Обсуждать будущую профессию",
          "Образовывать названия профессий",
          "Говорить о профессиях семьи"
        ])
      ]
    },
    {
      topic: "Мир вокруг нас",
      lessons: [
        L("Урок 5: Погода и времена года", "Времена года: winter (зима), spring (весна), summer (лето), autumn (осень). Месяцы: January, February, March, April, May, June, July, August, September, October, November, December. Погода: sunny (солнечно), cloudy (облачно), rainy (дождливо), snowy (снежно), windy (ветрено), cold (холодно), warm (тепло), hot (жарко). Фразы: What is the weather like today? (Какая сегодня погода?), It is sunny. (Солнечно.), What season is it? (Какое сейчас время года?).", [
          "Описывать погоду",
          "Называть времена года и месяцы",
          "Говорить о погоде сегодня",
          "Обсуждать климат",
          "Понимать прогноз погоды",
          "Описывать погоду в разные сезоны"
        ]),
        L("Урок 6: Природа и животные", "Названия животных: wild animals (дикие животные) — lion (лев), tiger (тигр), elephant (слон), bear (медведь), wolf (волк), fox (лиса); domestic animals (домашние животные) — cat (кошка), dog (собака), horse (лошадь), cow (корова). Описание внешности: big (большой), small (маленький), beautiful (красивый), dangerous (опасный). Среда обитания: forest (лес), zoo (зоопарк), farm (ферма), home (дом). Животные из Красной книги: panda (панда), tiger (тигр), whale (кит).", [
          "Называть животных",
          "Описывать внешность животных",
          "Говорить о среде обитания",
          "Обсуждать охрану природы",
          "Рассказывать о любимом животном",
          "Сравнивать животных"
        ]),
        L("Урок 7: В городе", "Места в городе: school (школа), hospital (больница), shop (магазин), supermarket (супермаркет), bank (банк), post office (почта), library (библиотека), museum (музей), park (парк), cinema (кино), theatre (театр), restaurant (ресторан), café (кафе), hotel (отель), station (станция), airport (аэропорт). Спрашивать дорогу: Where is...? (Где...?), How can I get to...? (Как добраться до...?), Go straight (идите прямо), Turn left/right (поверните налево/направо).", [
          "Называть места в городе",
          "Описывать маршрут",
          "Спрашивать дорогу",
          "Давать указания",
          "Понимать план города",
          "Рассказывать о своём городе"
        ]),
        L("Урок 8: Транспорт", "Виды транспорта: car (машина), bus (автобус), train (поезд), plane (самолёт), ship (корабль), bicycle (велосипед), taxi (такси), metro (метро), tram (трамвай). Глаголы движения: go (идти, ехать), drive (вести машину), fly (лететь), sail (плыть). Фразы: take a bus (сесть на автобус), by car (на машине), on foot (пешком), buy a ticket (купить билет), catch a train (успеть на поезд). Транспорт в Лондоне: double-decker (двухэтажный автобус), underground/tube (метро).", [
          "Называть виды транспорта",
          "Обсуждать путешествия",
          "Покупать билеты",
          "Описывать поездку",
          "Сравнивать виды транспорта",
          "Рассказывать о транспорте в городе"
        ])
      ]
    },
    {
      topic: "Семья и друзья",
      lessons: [
        L("Урок 9: Члены семьи", "Члены семьи: mother/mum (мама), father/dad (папа), sister (сестра), brother (брат), grandmother/grandma (бабушка), grandfather/grandpa (дедушка), aunt (тётя), uncle (дядя), cousin (двоюродный брат/сестра), nephew (племянник), niece (племянница). Притяжательный падеж: mother's car (мамина машина), Tom's book (книга Тома). Описание семьи: I have got a mother and a father. (У меня есть мама и папа.), This is my sister. (Это моя сестра.)", [
          "Называть родственников",
          "Описывать семью",
          "Говорить о возрасте членов семьи",
          "Сравнивать членов семьи",
          "Использовать притяжательный падеж",
          "Рассказывать о семье"
        ]),
        L("Урок 10: Внешность и характер", "Описание внешности: tall (высокий), short (низкий), young (молодой), old (старый), beautiful (красивый), handsome (красивый о мужчине), pretty (миловидный). Цвет волос и глаз: fair hair (светлые волосы), dark hair (тёмные волосы), blue eyes (голубые глаза), brown eyes (карие глаза). Черты характера: kind (добрый), clever (умный), friendly (дружелюбный), funny (смешной), brave (смелый), lazy (ленивый), honest (честный). Конструкция: He/She has got... (У него/неё есть...), He/She is... (Он/Она...).", [
          "Описывать внешность",
          "Называть черты характера",
          "Сравнивать людей",
          "Составлять описание человека",
          "Использовать прилагательные",
          "Описывать друзей и родственников"
        ]),
        L("Урок 11: Друзья", "Словарь по теме: friend (друг), friendship (дружба), best friend (лучший друг), classmate (одноклассник), neighbour (сосед). Что делают друзья: play together (играют вместе), go for a walk (гуляют), help each other (помогают друг другу), share (делиться), talk (разговаривать). Качества друга: loyal (верный), helpful (помогающий), honest (честный), funny (весёлый). Фразы: My best friend is... (Мой лучший друг —...), We like to... (Мы любим...), He/She is my friend because... (Он/Она мой друг, потому что...).", [
          "Говорить о друзьях",
          "Описывать дружбу",
          "Обсуждать общение с друзьями",
          "Рассказывать истории о друзьях",
          "Объяснять, почему человек друг",
          "Писать о друге"
        ]),
        L("Урок 12: Дом и быт", "Комнаты и части дома: house (дом), flat/apartment (квартира), room (комната), bedroom (спальня), living room (гостиная), kitchen (кухня), bathroom (ванная), hall (коридор), garden (сад). Мебель: bed (кровать), table (стол), chair (стул), sofa (диван), wardrobe (шкаф), bookcase (книжный шкаф), desk (письменный стол). Предлоги места: in (в), on (на), under (под), next to (рядом с), behind (за), in front of (перед). Фразы: There is/There are... (Есть...), My room has... (В моей комнате есть...).", [
          "Описывать дом",
          "Называть комнаты",
          "Говорить о мебели",
          "Описывать свою комнату",
          "Использовать предлоги места",
          "Рассказывать о доме"
        ])
      ]
    },
    {
      topic: "Школа и образование",
      lessons: [
        L("Урок 13: Школьные предметы", "Предметы: Maths/Mathematics (математика), English (английский), Russian (русский), History (история), Geography (география), Biology (биология), Physics (физика), Chemistry (химия), Physical Education/PE (физкультура), Art (изобразительное искусство), Music (музыка), Information Technology/IT (информатика). Отношение к предметам: I like... (Мне нравится...), I don't like... (Мне не нравится...), My favourite subject is... (Мой любимый предмет —...), interesting (интересный), boring (скучный), difficult (трудный), easy (лёгкий).", [
          "Называть предметы",
          "Говорить о расписании",
          "Обсуждать любимые предметы",
          "Сравнивать предметы",
          "Описывать отношение к предметам",
          "Составлять расписание"
        ]),
        L("Урок 14: В классе", "Классная комната: classroom (класс), blackboard (доска), desk (парта), chair (стул), teacher's desk (учительский стол), bookcase (шкаф для книг), window (окно), door (дверь). Школьные принадлежности: pen (ручка), pencil (карандаш), ruler (линейка), rubber/eraser (ластик), sharpener (точилка), textbook (учебник), exercise book (тетрадь), dictionary (словарь), schoolbag (рюкзак). Команды учителя: Open your books (Откройте книги), Close your books (Закройте книги), Listen to me (Послушайте меня), Read the text (Прочитайте текст), Write down (Запишите).", [
          "Называть школьные принадлежности",
          "Описывать класс",
          "Понимать инструкции учителя",
          "Давать инструкции",
          "Просить о помощи",
          "Разыгрывать диалоги"
        ]),
        L("Урок 15: Распорядок дня", "Распорядок дня: wake up (просыпаться), get up (вставать), wash (умываться), brush teeth (чистить зубы), have breakfast (завтракать), go to school (идти в школу), have lessons (иметь уроки), have lunch (обедать), go home (идти домой), do homework (делать домашнее задание), have dinner (ужинать), watch TV (смотреть телевизор), go to bed (ложиться спать). Время: What time is it? (Который час?), It is... o'clock. (...часов.), at 7 o'clock (в 7 часов), in the morning (утром), in the afternoon (днём), in the evening (вечером). Present Simple для регулярных действий.", [
          "Говорить о режиме дня",
          "Использовать Present Simple",
          "Указывать время",
          "Описывать будни",
          "Составлять рассказ о своём дне",
          "Спрашивать о времени"
        ]),
        L("Урок 16: Выходные и каникулы", "Дни недели: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday. Weekend (выходные) — Saturday и Sunday. Деятельность в выходные: visit friends (навещать друзей), go shopping (идти за покупками), play sports (заниматься спортом), read books (читать книги), listen to music (слушать музыку), watch films (смотреть фильмы), go to the cinema (идти в кино). Каникулы: holidays (каникулы), summer holidays (летние каникулы), winter holidays (зимние каникулы). Past Simple для рассказа о прошедших событиях.", [
          "Говорить о выходных",
          "Обсуждать планы",
          "Рассказывать о каникулах",
          "Использовать Past Simple",
          "Описывать отдых",
          "Сравнивать будни и выходные"
        ])
      ]
    },
    {
      topic: "Еда и покупки",
      lessons: [
        L("Урок 17: Продукты питания", "Продукты: bread (хлеб), butter (масло), cheese (сыр), milk (молоко), eggs (яйца), meat (мясо), fish (рыба), chicken (курица), fruit (фрукты), vegetables (овощи), apple (яблоко), orange (апельсин), banana (банан), potato (картофель), tomato (помидор), carrot (морковь), sugar (сахар), salt (соль). Еда и напитки: breakfast (завтрак), lunch (обед), dinner (ужин), snack (перекус), water (вода), tea (чай), coffee (кофе), juice (сок). Отношение к еде: I like... (Мне нравится...), I don't like... (Мне не нравится...), delicious (вкусно), tasty (вкусный).", [
          "Называть продукты",
          "Обсуждать предпочтения в еде",
          "Составлять меню",
          "Говорить о здоровом питании",
          "Описывать приёмы пищи",
          "Разыгрывать диалоги о еде"
        ]),
        L("Урок 18: В кафе и ресторане", "Диалоги в кафе: Can I help you? (Чем могу помочь?), I would like... (Я хотел бы...), What would you like to eat/drink? (Что вы хотели бы съесть/выпить?), Here is the menu (Вот меню), Anything else? (Что-нибудь ещё?), That's all (Это всё). Блюда: pizza (пицца), hamburger (гамбургер), sandwich (сандвич), salad (салат), soup (суп), ice cream (мороженое), cake (торт). Оплата: How much is it? (Сколько это стоит?), Here you are (Вот, пожалуйста), Thank you (Спасибо), Keep the change (Сдачи не надо).", [
          "Делать заказ в кафе",
          "Спрашивать о блюдах",
          "Платить за заказ",
          "Выражать мнение о еде",
          "Разыгрывать диалог в кафе",
          "Понимать меню"
        ]),
        L("Урок 19: Покупки", "Магазины: shop (магазин), supermarket (супермаркет), bakery (булочная), butcher's (мясной магазин), greengrocer's (овощной магазин), bookshop (книжный магазин), clothes shop (магазин одежды). Совершение покупок: How much is this? (Сколько это стоит?), How much are these? (Сколько стоят эти?), Can I try it on? (Можно примерить?), What size do you need? (Какой размер вам нужен?), It's too big/small (Это слишком большое/маленькое), I'll take it (Я возьму это). Денежные единицы: pound (фунт), dollar (доллар), euro (евро), rouble (рубль).", [
          "Называть магазины",
          "Спрашивать цену",
          "Совершать покупки",
          "Обсуждать одежду",
          "Разыгрывать диалог в магазине",
          "Сравнивать цены"
        ]),
        L("Урок 20: Одежда", "Предметы одежды: clothes (одежда), coat (пальто), jacket (куртка), dress (платье), skirt (юбка), trousers (брюки), jeans (джинсы), shirt (рубашка), T-shirt (футболка), sweater (свитер), hat (шляпа), cap (кепка), shoes (туфли), boots (ботинки), trainers (кроссовки). Размеры: size (размер), small (маленький), medium (средний), large (большой). Цвета: black (чёрный), white (белый), red (красный), blue (синий), green (зелёный), yellow (жёлтый), brown (коричневый), grey (серый). Сезонная одежда: summer clothes (летняя одежда), winter clothes (зимняя одежда).", [
          "Называть предметы одежды",
          "Описывать наряд",
          "Обсуждать моду",
          "Говорить о размерах",
          "Описывать одежду по цвету",
          "Выбирать одежду для сезона"
        ])
      ]
    },
    {
      topic: "Грамматика",
      lessons: [
        L("Урок 21: Present Simple", "Present Simple используется для регулярных, повторяющихся действий, фактов и истин. Утверждения: I/You/We/They work, He/She/It works (добавляется -s). Отрицания: I/You/We/They do not (don't) work, He/She/It does not (doesn't) work. Вопросы: Do I/you/we/they work? Does he/she/it work? Наречия частотности: always (всегда), usually (обычно), often (часто), sometimes (иногда), rarely (редко), never (никогда). Они ставятся перед глаголом.", [
          "Образовывать утверждения",
          "Задавать вопросы",
          "Отвечать на вопросы",
          "Использовать наречия частотности",
          "Правильно добавлять -s к глаголу",
          "Описывать регулярные действия"
        ]),
        L("Урок 22: Present Continuous", "Present Continuous используется для действий, происходящих в данный момент (сейчас). Образование: am/is/are + глагол с окончанием -ing. I am reading now. He/She/It is reading. We/You/They are reading. Вопросы: Am I reading? Is he reading? Are they reading? Слова-маркеры: now (сейчас), at the moment (в данный момент), Look! (Смотри!), Listen! (Слушай!). Отличие от Present Simple: Present Simple — регулярные действия, Present Continuous — действие сейчас.", [
          "Образовывать форму Continuous",
          "Отличать от Present Simple",
          "Использовать для текущих действий",
          "Задавать вопросы",
          "Понимать слова-маркеры",
          "Выбирать правильное время"
        ]),
        L("Урок 23: Past Simple", "Past Simple используется для действий, завершённых в прошлом. Правильные глаголы добавляют -ed: work — worked, play — played. Неправильные глаголы меняют форму: go — went, see — saw, have — had, do — did, come — came, take — took, give — gave, know — knew. Отрицания: did not (didn't) + глагол в начальной форме. Вопросы: Did + подлежащее + глагол? Слова-маркеры: yesterday (вчера), last week (на прошлой неделе), ago (тому назад), in 2010 (в 2010 году).", [
          "Образовывать правильные глаголы",
          "Запоминать неправильные глаголы",
          "Задавать вопросы в прошедшем",
          "Рассказывать о прошлом",
          "Понимать слова-маркеры",
          "Отличать от других времён"
        ]),
        L("Урок 24: Future Simple", "Future Simple используется для будущих действий, предсказаний, мгновенных решений. Образование: will + глагол. Утверждение: I will go. Отрицание: I will not (won't) go. Вопрос: Will you go? Слова-маркеры: tomorrow (завтра), next week (на следующей неделе), soon (скоро), in the future (в будущем), in two days (через два дня). Разница с конструкцией to be going to: will — для мгновенных решений и предсказаний, going to — для запланированных действий.", [
          "Использовать will для будущего",
          "Говорить о планах",
          "Делать предсказания",
          "Обсуждать будущее",
          "Образовывать отрицания и вопросы",
          "Различать will и going to"
        ])
      ]
    }
  ]
}

export const games: GameLesson[] = [
  {
    title: "Приветствие и знакомство",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Как сказать «Как тебя зовут?»", options: ["How old are you?", "What is your name?", "Where are you from?"], correctAnswer: "What is your name?", hint: "Name = имя" },
      { type: 'quiz', question: "Как ответить на «How are you?»?", options: ["I am 12", "I am fine", "I am from Russia"], correctAnswer: "I am fine", hint: "Fine = хорошо" },
      { type: 'find', question: "Выбери фразы приветствия:", options: ["Hello", "Goodbye", "Hi", "Good night", "Good morning", "See you"], correctAnswer: ["Hello", "Hi", "Good morning"], hint: "Hello, Hi, Good morning = приветствие" },
      { type: 'quiz', question: "Nice to meet you = ?", options: ["До свидания", "Приятно познакомиться", "Как дела"], correctAnswer: "Приятно познакомиться", hint: "Meet = встречать, знакомиться" }
    ],
    reward: { stars: 3, message: "Great! Ты умеешь знакомиться! 👋" }
  },
  {
    title: "Погода и времена года",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Как сказать «солнечно»?", options: ["Rainy", "Sunny", "Cloudy"], correctAnswer: "Sunny", hint: "Sun = солнце" },
      { type: 'find', question: "Выбери названия времён года:", options: ["Monday", "Winter", "Spring", "January", "Summer", "Autumn"], correctAnswer: ["Winter", "Spring", "Summer", "Autumn"], hint: "Seasons = времена года" },
      { type: 'quiz', question: "What's the weather like? = ?", options: ["Который час?", "Какая погода?", "Как дела?"], correctAnswer: "Какая погода?", hint: "Weather = погода" },
      { type: 'quiz', question: "Какая погода: It's raining?", options: ["Солнечно", "Дождливо", "Снежно"], correctAnswer: "Дождливо", hint: "Rain = дождь" }
    ],
    reward: { stars: 3, message: "Excellent! Ты говоришь о погоде! ☀️" }
  },
  {
    title: "Семья и дом",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Mother - это?", options: ["Папа", "Мама", "Бабушка"], correctAnswer: "Мама", hint: "Mother = мама" },
      { type: 'find', question: "Выбери названия комнат:", options: ["Kitchen", "Car", "Bedroom", "Garden", "Bathroom", "Living room"], correctAnswer: ["Kitchen", "Bedroom", "Bathroom", "Living room"], hint: "Rooms = комнаты" },
      { type: 'quiz', question: "Как будет «семья»?", options: ["Friend", "Family", "House"], correctAnswer: "Family", hint: "Family = семья" },
      { type: 'quiz', question: "Sister - это?", options: ["Сестра", "Брат", "Тётя"], correctAnswer: "Сестра", hint: "Sister = сестра" }
    ],
    reward: { stars: 3, message: "Wonderful! Ты говоришь о семье! 🏠" }
  },
  {
    title: "Present Simple vs Present Continuous",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Когда используем Present Simple?", options: ["Для регулярных действий", "Для действий сейчас", "Для прошлого"], correctAnswer: "Для регулярных действий", hint: "Present Simple: I play tennis every day" },
      { type: 'quiz', question: "Когда используем Present Continuous?", options: ["Для регулярных действий", "Для действий в данный момент", "Для будущего"], correctAnswer: "Для действий в данный момент", hint: "Present Continuous: I am playing now" },
      { type: 'find', question: "Выбери предложения в Present Continuous:", options: ["I am reading now", "She reads every day", "They are playing", "He works here", "We are watching TV"], correctAnswer: ["I am reading now", "They are playing", "We are watching TV"], hint: "Present Continuous = am/is/are + verb-ing" },
      { type: 'quiz', question: "I ___ to school every day. (go)", options: ["am going", "go", "went"], correctAnswer: "go", hint: "Present Simple для регулярных действий" }
    ],
    reward: { stars: 3, message: "Great! Ты знаешь времена! ⏰" }
  },
  {
    title: "Past Simple - прошедшее время",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Go в прошедшем времени = ?", options: ["goed", "went", "gone"], correctAnswer: "went", hint: "Go - неправильный глагол: went" },
      { type: 'quiz', question: "Play в прошедшем времени = ?", options: ["played", "plaied", "playd"], correctAnswer: "played", hint: "Play - правильный глагол + ed" },
      { type: 'find', question: "Выбери глаголы в Past Simple:", options: ["Went", "Go", "Played", "Eat", "Visited", "See"], correctAnswer: ["Went", "Played", "Visited"], hint: "Past Simple = прошедшее время" },
      { type: 'quiz', question: "I ___ to the cinema yesterday.", options: ["go", "went", "am going"], correctAnswer: "went", hint: "Yesterday = вчера (прошедшее время)" }
    ],
    reward: { stars: 3, message: "Excellent! Ты знаешь прошедшее время! 📅" }
  }
]
