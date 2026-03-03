import { SubjectData, GameLesson } from '@/data/types'

const L = (t: string, d: string, tasks: string[], content?: string, examples?: string[], facts?: string[]) => ({
  title: t, description: d, tasks, content, examples, facts
})

export const lessons: SubjectData = {
  title: "Иностранный язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: ["Знакомство", "Мир вокруг нас", "Семья и друзья", "Школа", "Путешествия", "Грамматика"],
  detailedTopics: [
    {
      topic: "Знакомство и общение",
      lessons: [
        L("Урок 1: Приветствие и прощание", "Greetings and goodbyes.", [
          "Приветствовать разными способами",
          "Прощаться по-английски",
          "Знакомиться с людьми",
          "Представлять себя"
        ], `**Greetings (Приветствия):**

| Английский | Русский | Когда используем |
|------------|---------|------------------|
| Hello | Привет | Формально и неформально |
| Hi | Привет | Неформально |
| Good morning | Доброе утро | До 12:00 |
| Good afternoon | Добрый день | 12:00-18:00 |
| Good evening | Добрый вечер | После 18:00 |
| Good night | Спокойной ночи | При прощании на ночь |

**Goodbyes (Прощания):**

| Английский | Русский | Когда используем |
|------------|---------|------------------|
| Goodbye | До свидания | Формально |
| Bye | Пока | Неформально |
| See you | Увидимся | Неформально |
| See you later | До встречи | Неформально |
| See you soon | До скорого | Неформально |
| Good night | Спокойной ночи | Вечером/ночью |
| Take care | Береги себя | Дружеское |

**Introductions (Знакомство):**

| Английский | Русский |
|------------|---------|
| What is your name? | Как тебя зовут? |
| My name is... | Меня зовут... |
| I'm... | Я... |
| Nice to meet you | Приятно познакомиться |
| Nice to meet you too | Мне тоже приятно |
| How are you? | Как дела? |
| I'm fine, thanks | Хорошо, спасибо |
| I'm OK | Нормально |
| Not bad | Неплохо |

**Dialogues (Диалоги):**

**Dialogue 1:**
\`\`\`
A: Hello! My name is Tom. What is your name?
B: Hi! I'm Ann. Nice to meet you.
A: Nice to meet you too!
\`\`\`

**Dialogue 2:**
\`\`\`
A: Hi! How are you?
B: I'm fine, thanks! And you?
A: I'm OK. Goodbye!
B: Bye! See you!
\`\`\``,
          ["Hello — самое универсальное приветствие", "Good night — это прощание, не приветствие", "Nice to meet you говорят только при первой встрече"],
          ["Hi более неформально, чем Hello", "Good morning/afternoon/evening — по времени суток", "See you — короткое 'увидимся'"]),
        L("Урок 2: Личная информация", "Personal information.", [
          "Называть имя и фамилию",
          "Говорить о возрасте",
          "Рассказывать о себе",
          "Задавать вопросы"
        ], `**Personal Information (Личная информация):**

**Name (Имя):**

| Английский | Русский |
|------------|---------|
| What is your name? | Как тебя зовут? |
| My name is... | Меня зовут... |
| I'm... | Я... |
| What is your surname? | Какая твоя фамилия? |
| My surname is... | Моя фамилия... |
| What is your full name? | Как твоё полное имя? |

**Age (Возраст):**

| Английский | Русский |
|------------|---------|
| How old are you? | Сколько тебе лет? |
| I am 11 years old | Мне 11 лет |
| I'm 11 | Мне 11 лет |
| I am 12 | Мне 12 лет |

**Numbers 1-20 (Числа 1-20):**

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| one | two | three | four | five | six | seven | eight | nine | ten |

| 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|----|----|----|----|----|----|----|----|----|----|
| eleven | twelve | thirteen | fourteen | fifteen | sixteen | seventeen | eighteen | nineteen | twenty |

**About Me (О себе):**

| Английский | Русский |
|------------|---------|
| I am from Russia | Я из России |
| I live in Moscow | Я живу в Москве |
| I am a student | Я ученик/ученица |
| I go to school | Я хожу в школу |
| I like... | Мне нравится... |
| My hobby is... | Моё хобби... |

**Questions (Вопросы):**

| Английский | Русский |
|------------|---------|
| Where are you from? | Откуда ты? |
| Where do you live? | Где ты живёшь? |
| What do you like? | Что тебе нравится? |
| What is your hobby? | Какое твоё хобби? |

**Пример рассказа о себе:**
\`\`\`
Hello! My name is Ivan. My surname is Petrov. 
I am 11 years old. I am from Russia.
I live in Moscow. I am a student.
I like football and music.
\`\`\``,
          ["В английском название страны пишется с большой буквы", "I'm = I am (краткая форма)", "Years old можно опустить: I'm 11"],
          ["How old are you? — вопрос о возрасте", "Фамилия = surname или last name", "Имя = first name"]),
        L("Урок 3: Страны и национальности", "Countries and nationalities.", [
          "Называть страны",
          "Определять национальности",
          "Говорить «Я из...»",
          "Спрашивать о происхождении"
        ], `**Countries (Страны):**

| Страна | Английский | Столица |
|--------|------------|---------|
| Россия | Russia | Moscow |
| Великобритания | Great Britain / UK | London |
| США | USA / United States | Washington |
| Франция | France | Paris |
| Германия | Germany | Berlin |
| Испания | Spain | Madrid |
| Италия | Italy | Rome |
| Япония | Japan | Tokyo |
| Китай | China | Beijing |
| Австралия | Australia | Canberra |

**Nationalities (Национальности):**

| Страна | Национальность | Окончание |
|--------|----------------|-----------|
| Russia | Russian | -an |
| Great Britain | British | -ish |
| USA | American | -an |
| France | French | - |
| Germany | German | -an |
| Spain | Spanish | -ish |
| Italy | Italian | -an |
| Japan | Japanese | -ese |
| China | Chinese | -ese |
| Australia | Australian | -an |

**Способы образования национальностей:**

| Окончание | Примеры |
|-----------|---------|
| -an | Russian, American, German |
| -ian | Italian, Canadian |
| -ish | British, Spanish, Polish |
| -ese | Japanese, Chinese, Portuguese |
| -i | Israeli, Iraqi |
| Особые | French, Greek, Dutch |

**Говорим о происхождении:**

| Английский | Русский |
|------------|---------|
| Where are you from? | Откуда ты? |
| I am from Russia | Я из России |
| I'm from Russia | Я из России |
| What nationality are you? | Кто ты по национальности? |
| I am Russian | Я русский/русская |
| I'm Russian | Я русский/русская |

**Обратите внимание:**
- I'm from Russia (страна) 
- I'm Russian (национальность)

**Languages (Языки):**

| Страна | Язык |
|--------|------|
| Russia | Russian |
| Great Britain | English |
| USA | English |
| France | French |
| Germany | German |
| Spain | Spanish |
| Italy | Italian |

**I speak English = Я говорю по-английски**`,
          ["Названия стран и языков пишутся с большой буквы", "British = британец (из Великобритании)", "English = английский язык и англичанин"],
          ["Откуда ты? = Where are you from?", "Я из... = I'm from...", "Национальности имеют разные окончания"]),
        L("Урок 4: Профессии", "Jobs and professions.", [
          "Называть профессии",
          "Спрашивать о работе",
          "Рассказывать о профессии",
          "Обсуждать будущую профессию"
        ], `**Jobs and Professions (Профессии):**

**Образование и медицина:**

| Английский | Русский |
|------------|---------|
| teacher | учитель |
| student | ученик, студент |
| doctor | врач |
| nurse | медсестра |

**Бизнес и офис:**

| Английский | Русский |
|------------|---------|
| manager | менеджер |
| secretary | секретарь |
| lawyer | юрист, адвокат |
| accountant | бухгалтер |

**Творчество и спорт:**

| Английский | Русский |
|------------|---------|
| actor | актёр |
| singer | певец |
| artist | художник |
| sportsman | спортсмен |
| football player | футболист |

**Обслуживание и транспорт:**

| Английский | Русский |
|------------|---------|
| waiter | официант |
| cook / chef | повар |
| driver | водитель |
| pilot | пилот |
| police officer | полицейский |

**Вопросы о работе:**

| Английский | Русский |
|------------|---------|
| What do you do? | Кем ты работаешь? |
| What is your job? | Какая у тебя работа? |
| What do you want to be? | Кем ты хочешь стать? |
| I want to be a... | Я хочу стать... |

**Говорим о работе:**

| Английский | Русский |
|------------|---------|
| I am a teacher | Я учитель |
| I work as a doctor | Я работаю врачом |
| He is a pilot | Он пилот |
| She is a singer | Она певица |

**Артикль a/an с профессиями:**
- a teacher (согласная)
- an actor (гласная)
- a doctor (согласная)
- an engineer (гласная)

**Want to be (Хотеть стать):**

\`\`\`
I want to be a doctor.
He wants to be a pilot.
She wants to be a teacher.
\`\`\`

**Вопрос о будущем:**
\`\`\`
— What do you want to be?
— I want to be a programmer.
\`\`\``,
          ["He is a doctor — он врач (артикль a обязателен)", "an + гласная: an actor, an engineer", "What do you do? = Кем ты работаешь?"],
          ["Профессии с артиклем a/an", "want to be = хотеть стать", "I work as... = Я работаю..."])
      ]
    },
    {
      topic: "Мир вокруг нас",
      lessons: [
        L("Урок 5: Погода и времена года", "Weather and seasons.", [
          "Описывать погоду",
          "Называть времена года",
          "Говорить о погоде сегодня",
          "Обсуждать климат"
        ], `**Seasons (Времена года):**

| Английский | Русский | Месяцы |
|------------|---------|--------|
| Spring | Весна | March, April, May |
| Summer | Лето | June, July, August |
| Autumn / Fall | Осень | September, October, November |
| Winter | Зима | December, January, February |

**Months (Месяцы):**

| Зима | Весна | Лето | Осень |
|------|-------|------|-------|
| December | March | June | September |
| January | April | July | October |
| February | May | August | November |

**Weather (Погода):**

| Английский | Русский |
|------------|---------|
| What's the weather like? | Какая погода? |
| What's the weather like today? | Какая погода сегодня? |
| It's... | ... |

**Слова для описания погоды:**

| Английский | Русский |
|------------|---------|
| sunny | солнечно |
| cloudy | облачно |
| rainy | дождливо |
| snowy | снежно |
| windy | ветрено |
| cold | холодно |
| hot | жарко |
| warm | тепло |
| cool | прохладно |
| foggy | туманно |

**Фразы о погоде:**

| Английский | Русский |
|------------|---------|
| It's sunny | Солнечно |
| It's raining | Идёт дождь |
| It's snowing | Идёт снег |
| It's cold today | Сегодня холодно |
| It's hot in summer | Летом жарко |

**Любимое время года:**

| Английский | Русский |
|------------|---------|
| What's your favourite season? | Какое твоё любимое время года? |
| My favourite season is... | Моё любимое время года... |
| I like summer | Мне нравится лето |
| I love winter | Я люблю зиму |

**Пример диалога:**
\`\`\`
A: What's the weather like today?
B: It's sunny and warm.
A: What's your favourite season?
B: My favourite season is summer. 
   I like hot weather.
\`\`\``,
          ["Autumn — британский английский, Fall — американский", "It's raining = Идёт дождь (действие)", "It's rainy = Дождливо (состояние)"],
          ["What's the weather like? — стандартный вопрос о погоде", "It's + прилагательное для описания погоды", "Месяцы пишутся с большой буквы"]),
        L("Урок 6: Природа и животные", "Nature and animals.", [
          "Называть животных",
          "Описывать внешность животных",
          "Говорить о среде обитания",
          "Обсуждать охрану природы"
        ], `**Animals (Животные):**

**Pets (Домашние питомцы):**

| Английский | Русский |
|------------|---------|
| cat | кошка |
| dog | собака |
| hamster | хомяк |
| rabbit | кролик |
| parrot | попугай |
| fish | рыбка |
| guinea pig | морская свинка |

**Farm animals (Домашние животные):**

| Английский | Русский |
|------------|---------|
| cow | корова |
| pig | свинья |
| sheep | овца |
| horse | лошадь |
| chicken | курица |
| duck | утка |
| goat | коза |

**Wild animals (Дикие животные):**

| Английский | Русский |
|------------|---------|
| lion | лев |
| tiger | тигр |
| elephant | слон |
| bear | медведь |
| wolf | волк |
| fox | лиса |
| deer | олень |
| monkey | обезьяна |
| giraffe | жираф |
| zebra | зебра |

**Habitats (Среда обитания):**

| Английский | Русский |
|------------|---------|
| forest | лес |
| jungle | джунгли |
| desert | пустыня |
| ocean | океан |
| river | река |
| mountains | горы |
| farm | ферма |
| zoo | зоопарк |

**Describing animals (Описание животных):**

| Английский | Русский |
|------------|---------|
| big / small | большой / маленький |
| strong | сильный |
| fast | быстрый |
| slow | медленный |
| dangerous | опасный |
| cute | милый |
| beautiful | красивый |
| furry | пушистый |

**Примеры описания:**
\`\`\`
A lion is big and strong.
A rabbit is small and cute.
A turtle is slow.
A cheetah is fast.
\`\`\`

**Множественное число:**
- cat → cats
- dog → dogs
- fox → foxes
- fish → fish (без изменений)`,
          ["Sheep — одинаково в ед. и мн. числе: one sheep, two sheep", "Fish может быть fishes (виды рыб) или fish (рыбы)", "Wild animals = дикие животные"],
          ["Lion — лев, Tiger — тигр", "Forest — лес, Jungle — джунгли", "Zoo — зоопарк"]),
        L("Урок 7: В городе", "In the city.", [
          "Называть места в городе",
          "Описывать маршрут",
          "Спрашивать дорогу",
          "Давать указания"
        ], `**Places in the city (Места в городе):**

| Английский | Русский |
|------------|---------|
| city | город |
| town | маленький город |
| street | улица |
| square | площадь |
| park | парк |
| shop / store | магазин |
| supermarket | супермаркет |
| market | рынок |
| hospital | больница |
| school | школа |
| library | библиотека |
| museum | музей |
| cinema | кинотеатр |
| theatre | театр |
| restaurant | ресторан |
| café | кафе |
| hotel | отель |
| bank | банк |
| post office | почта |
| police station | полицейский участок |
| bus stop | автобусная остановка |
| train station | вокзал |
| airport | аэропорт |

**Asking the way (Как пройти):**

| Английский | Русский |
|------------|---------|
| Excuse me! | Извините! |
| Where is...? | Где находится...? |
| How do I get to...? | Как пройти к...? |
| Can you help me? | Можете мне помочь? |
| I'm looking for... | Я ищу... |

**Giving directions (Указания):**

| Английский | Русский |
|------------|---------|
| Go straight | Идите прямо |
| Turn left | Поверните налево |
| Turn right | Поверните направо |
| Go along the street | Идите вдоль улицы |
| Cross the street | Перейдите улицу |
| It's on the left | Это слева |
| It's on the right | Это справа |
| It's next to... | Это рядом с... |
| It's opposite... | Это напротив... |
| It's between... | Это между... |

**Пример диалога:**
\`\`\`
A: Excuse me! Where is the cinema?
B: Go straight and turn left. 
   The cinema is on the right.
A: Thank you!
B: You're welcome!
\`\`\`

**Prepositions of place (Предлоги места):**

| Английский | Русский |
|------------|---------|
| next to | рядом с |
| opposite | напротив |
| between | между |
| behind | позади |
| in front of | перед |
| near | около |
| on the corner | на углу |`,
          ["Excuse me — вежливое обращение к незнакомцу", "You're welcome — пожалуйста (ответ на спасибо)", "Shop — британский, Store — американский"],
          ["Where is...? = Где находится...?", "Turn left/right = Поверните налево/направо", "Go straight = Идите прямо"]),
        L("Урок 8: Транспорт", "Transport.", [
          "Называть виды транспорта",
          "Обсуждать путешествия",
          "Покупать билеты",
          "Описывать поездку"
        ], `**Transport (Транспорт):**

**Land transport (Наземный транспорт):**

| Английский | Русский |
|------------|---------|
| car | машина |
| bus | автобус |
| train | поезд |
| taxi | такси |
| bicycle / bike | велосипед |
| motorcycle | мотоцикл |
| tram | трамвай |
| underground / subway | метро |
| lorry / truck | грузовик |

**Water transport (Водный транспорт):**

| Английский | Русский |
|------------|---------|
| ship | корабль |
| boat | лодка |
| ferry | паром |
| yacht | яхта |

**Air transport (Воздушный транспорт):**

| Английский | Русский |
|------------|---------|
| plane / airplane | самолёт |
| helicopter | вертолёт |

**Глаголы движения:**

| Английский | Русский |
|------------|---------|
| go | идти, ехать |
| travel | путешествовать |
| drive | вести машину |
| fly | лететь |
| sail | плыть (на судне) |

**By + transport (На + транспорт):**

| Английский | Русский |
|------------|---------|
| by car | на машине |
| by bus | на автобусе |
| by train | на поезде |
| by plane | на самолёте |
| by bike | на велосипеде |
| on foot | пешком |

**At the airport/station (В аэропорту/на вокзале):**

| Английский | Русский |
|------------|---------|
| ticket | билет |
| single ticket | билет в одну сторону |
| return ticket | билет туда-обратно |
| platform | платформа |
| gate | выход (в аэропорту) |
| departure | отправление |
| arrival | прибытие |
| luggage / baggage | багаж |

**Покупка билета:**
\`\`\`
A: One ticket to London, please.
B: Single or return?
A: Return, please.
B: That's £50.
A: Here you are.
\`\`\`

**How do you get to school?**
\`\`\`
— How do you get to school?
— I go by bus. / I go on foot.
\`\`\``,
          ["By car, by bus — без артикля", "On foot — пешком (особый случай)", "Subway — американский, Underground — британский"],
          ["by + транспорт = на + транспорт", "ticket = билет", "How do you get to...? = Как ты добираешься до...?"])
      ]
    },
    {
      topic: "Семья и друзья",
      lessons: [
        L("Урок 9: Члены семьи", "Family members.", [
          "Называть родственников",
          "Описывать семью",
          "Говорить о возрасте",
          "Сравнивать членов семьи"
        ], `**Family members (Члены семьи):**

**Immediate family (Ближайшие родственники):**

| Английский | Русский |
|------------|---------|
| mother / mom | мать / мама |
| father / dad | отец / папа |
| parent | родитель |
| parents | родители |
| sister | сестра |
| brother | брат |
| grandmother / grandma | бабушка |
| grandfather / grandpa | дедушка |
| grandparents | бабушка и дедушка |

**Extended family (Дальние родственники):**

| Английский | Русский |
|------------|---------|
| aunt | тётя |
| uncle | дядя |
| cousin | двоюродный брат/сестра |
| niece | племянница |
| nephew | племянник |

**Family by marriage (Родственники через брак):**

| Английский | Русский |
|------------|---------|
| husband | муж |
| wife | жена |
| son | сын |
| daughter | дочь |
| children | дети |

**Possessive 's (Притяжательный падеж):**

| Английский | Русский |
|------------|---------|
| mother's car | мамина машина |
| father's job | папина работа |
| sister's name | имя сестры |
| Tom's sister | сестра Тома |

**Описываем семью:**

| Английский | Русский |
|------------|---------|
| I have got a... | У меня есть... |
| I have got a sister | У меня есть сестра |
| I have got two brothers | У меня есть два брата |
| I haven't got a sister | У меня нет сестры |
| Have you got a brother? | У тебя есть брат? |

**Пример рассказа о семье:**
\`\`\`
I have got a family. My family is big.
I have got a mother, a father and a sister.
My mother's name is Anna. She is 35.
My father's name is Ivan. He is 38.
My sister's name is Olga. She is 10.
I love my family.
\`\`\`

**Have got / Has got:**

| Полная форма | Краткая форма |
|--------------|---------------|
| I have got | I've got |
| You have got | You've got |
| He has got | He's got |
| She has got | She's got |
| We have got | We've got |
| They have got | They've got |`,
          ["Cousin — и кузен, и кузина", "Mom/Mum — американский/британский вариант", "Have got = have (американский вариант)"],
          ["Притяжательный падеж: mother's car", "I have got = У меня есть", "I haven't got = У меня нет"]),
        L("Урок 10: Внешность и характер", "Appearance and personality.", [
          "Описывать внешность",
          "Называть черты характера",
          "Сравнивать людей",
          "Составлять описание"
        ], `**Appearance (Внешность):**

**Face (Лицо):**

| Английский | Русский |
|------------|---------|
| face | лицо |
| eyes | глаза |
| nose | нос |
| mouth | рот |
| ears | уши |
| hair | волосы |

**Hair (Волосы):**

| Английский | Русский |
|------------|---------|
| long hair | длинные волосы |
| short hair | короткие волосы |
| straight hair | прямые волосы |
| curly hair | кудрявые волосы |
| wavy hair | волнистые волосы |
| fair hair | светлые волосы |
| dark hair | тёмные волосы |
| blonde | блондин/ка |
| brunette | брюнет/ка |

**Body (Тело):**

| Английский | Русский |
|------------|---------|
| tall | высокий |
| short | низкий |
| slim | стройный |
| fat | толстый |
| thin | худой |

**General (Общее):**

| Английский | Русский |
|------------|---------|
| beautiful | красивый (о женщине) |
| handsome | красивый (о мужчине) |
| ugly | некрасивый |
| young | молодой |
| old | старый |

**Personality (Характер):**

| Английский | Русский |
|------------|---------|
| kind | добрый |
| friendly | дружелюбный |
| clever / smart | умный |
| funny | смешной, весёлый |
| serious | серьёзный |
| lazy | ленивый |
| hardworking | трудолюбивый |
| shy | застенчивый |
| brave | смелый |
| honest | честный |

**Describing people (Описание людей):**

\`\`\`
She has got blue eyes and fair hair.
He has got dark hair and brown eyes.
She is tall and slim.
He is short and fat.
\`\`\`

**Пример описания:**
\`\`\`
My friend is Anna. She is 11 years old.
She is tall and slim. She has got long 
fair hair and blue eyes. She is kind 
and friendly. She is clever too.
\`\`\``,
          ["He has got = He's got (У него есть)", "She has got blue eyes = У неё голубые глаза", "Beautiful — о женщинах, Handsome — о мужчинах"],
          ["Hair — неисчисляемое: long hair (не hairs)", "She has got... = У неё есть...", "Kind, friendly, clever — положительные качества"]),
        L("Урок 11: Друзья", "Friends.", [
          "Говорить о друзьях",
          "Описывать дружбу",
          "Обсуждать общение",
          "Рассказывать истории"
        ], `**Friendship (Дружба):**

| Английский | Русский |
|------------|---------|
| friend | друг |
| best friend | лучший друг |
| friendship | дружба |
| make friends | подружиться |
| be friends | дружить |

**Activities with friends (Занятия с друзьями):**

| Английский | Русский |
|------------|---------|
| play together | играть вместе |
| walk together | гулять вместе |
| talk | разговаривать |
| chat | болтать |
| go to the cinema | ходить в кино |
| go shopping | ходить по магазинам |
| play sports | заниматься спортом |
| listen to music | слушать музыку |
| watch films | смотреть фильмы |
| help each other | помогать друг другу |

**Qualities of a friend (Качества друга):**

| Английский | Русский |
|------------|---------|
| loyal | верный, преданный |
| helpful | helpful |
| honest | честный |
| understanding | понимающий |
| generous | щедрый |
| reliable | надёжный |
| supportive | поддерживающий |
| fun | весёлый |

**Phrases (Фразы):**

| Английский | Русский |
|------------|---------|
| My best friend is... | Мой лучший друг... |
| We are good friends | Мы хорошие друзья |
| We have fun together | Нам весело вместе |
| He/She always helps me | Он/Она всегда помогает мне |
| I can trust him/her | Я могу доверять ему/ей |
| We have known each other for... | Мы знакомы уже... |

**Рассказ о друге:**
\`\`\`
My best friend is Tom. He is 11 years old.
We are classmates. Tom is kind and funny.
We play football together after school.
We often go to the cinema.
I can tell him my secrets.
He is a real friend.
\`\`\`

**Questions about friends:**

| Английский | Русский |
|------------|---------|
| Who is your best friend? | Кто твой лучший друг? |
| How long have you been friends? | Как давно вы дружите? |
| What do you do together? | Что вы делаете вместе? |
| Why do you like him/her? | Почему он/она тебе нравится? |`,
          ["Best friend = лучший друг", "Each other = друг друга", "Together = вместе"],
          ["Friend = друг, Friendship = дружба", "We are friends = Мы друзья", "Make friends = подружиться"]),
        L("Урок 12: Дом и быт", "Home and daily life.", [
          "Описывать дом",
          "Называть комнаты",
          "Говорить о мебели",
          "Описывать свою комнату"
        ], `**Home (Дом):**

| Английский | Русский |
|------------|---------|
| house | дом (отдельный) |
| flat / apartment | квартира |
| room | комната |
| bedroom | спальня |
| living room | гостиная |
| kitchen | кухня |
| bathroom | ванная |
| toilet | туалет |
| hall | прихожая |
| garden | сад |
| balcony | балкон |

**Furniture (Мебель):**

| Английский | Русский |
|------------|---------|
| bed | кровать |
| sofa / couch | диван |
| chair | стул |
| table | стол |
| desk | письменный стол |
| wardrobe | шкаф для одежды |
| bookcase | книжный шкаф |
| shelf | полка |
| carpet | ковёр |
| lamp | лампа |
| mirror | зеркало |

**In the bedroom (В спальне):**

| Английский | Русский |
|------------|---------|
| bed | кровать |
| wardrobe | шкаф |
| desk | письменный стол |
| chair | стул |
| window | окно |
| door | дверь |

**In the kitchen (На кухне):**

| Английский | Русский |
|------------|---------|
| cooker / stove | плита |
| fridge | холодильник |
| table | стол |
| chair | стул |
| sink | раковина |

**There is / There are:**

| Английский | Русский |
|------------|---------|
| There is a... | Есть (один)... |
| There are... | Есть (несколько)... |

**Примеры:**
\`\`\`
There is a table in the kitchen.
There are two chairs in the room.
There is a bed in my bedroom.
There are three rooms in our flat.
\`\`\`

**Prepositions of place:**

| Английский | Русский |
|------------|---------|
| in | в |
| on | на |
| under | под |
| next to | рядом с |
| behind | за |

**Описание комнаты:**
\`\`\`
My room is small but nice.
There is a bed next to the window.
There is a desk under the window.
There are books on the shelf.
I like my room.
\`\`\``,
          ["Flat — британский, Apartment — американский", "There is + единственное число", "There are + множественное число"],
          ["House — дом, Flat — квартира", "Furniture — мебель (неисчисляемое)", "There is/are = есть, находится"])
      ]
    },
    {
      topic: "Школа и образование",
      lessons: [
        L("Урок 13: Школьные предметы", "School subjects.", [
          "Называть предметы",
          "Говорить о расписании",
          "Обсуждать любимые предметы",
          "Сравнивать предметы"
        ], `**School subjects (Школьные предметы):**

| Английский | Русский |
|------------|---------|
| Maths / Mathematics | Математика |
| Russian | Русский язык |
| Literature | Литература |
| English | Английский язык |
| History | История |
| Geography | География |
| Biology | Биология |
| Physics | Физика |
| Chemistry | Химия |
| IT / Informatics | Информатика |
| PE / Physical Education | Физкультура |
| Art | ИЗО |
| Music | Музыка |
| Technology | Технология |

**School objects (Школьные принадлежности):**

| Английский | Русский |
|------------|---------|
| book | книга |
| textbook | учебник |
| exercise book | тетрадь |
| notebook | блокнот |
| pen | ручка |
| pencil | карандаш |
| ruler | линейка |
| rubber / eraser | ластик |
| sharpener | точилка |
| desk | парта |
| blackboard | доска |
| chalk | мел |
| marker | маркер |
| bag / schoolbag | портфель |
| pencil case | пенал |

**Talking about subjects (О предметах):**

| Английский | Русский |
|------------|---------|
| What's your favourite subject? | Какой твой любимый предмет? |
| My favourite subject is... | Мой любимый предмет... |
| I like... | Мне нравится... |
| I don't like... | Мне не нравится... |
| I'm good at... | Я хорош в... |
| I'm bad at... | Я плох в... |

**Примеры:**
\`\`\`
My favourite subject is Maths.
I like History and English.
I don't like PE.
I'm good at Russian.
I'm bad at Chemistry.
\`\`\`

**Why? (Почему?):**

| Английский | Русский |
|------------|---------|
| It's interesting | Это интересно |
| It's boring | Это скучно |
| It's easy | Это легко |
| It's difficult / hard | Это трудно |
| I like the teacher | Мне нравится учитель |
| I learn new things | Я узнаю новое |`,
          ["Maths — британский, Math — американский", "PE = Physical Education", "I'm good at + существительное/герундий"],
          ["Favourite subject = любимый предмет", "I like/don't like = мне нравится/не нравится", "Easy = легко, Difficult = трудно"]),
        L("Урок 14: В классе", "In the classroom.", [
          "Называть школьные принадлежности",
          "Описывать класс",
          "Понимать инструкции",
          "Давать инструкции"
        ], `**In the classroom (В классе):**

| Английский | Русский |
|------------|---------|
| classroom | класс, классная комната |
| teacher | учитель |
| student | ученик |
| desk | парта |
| chair | стул |
| blackboard | доска |
| whiteboard | белая доска |
| door | дверь |
| window | окно |
| wall | стена |
| floor | пол |
| ceiling | потолок |
| shelf | полка |
| cupboard | шкаф |

**Classroom instructions (Инструкции):**

| Английский | Русский |
|------------|---------|
| Open your books | Откройте книги |
| Close your books | Закройте книги |
| Listen to me | Послушайте меня |
| Look at the board | Посмотрите на доску |
| Read the text | Прочитайте текст |
| Write in your notebooks | Пишите в тетрадях |
| Answer the question | Ответьте на вопрос |
| Ask a question | Задайте вопрос |
| Work in pairs | Работайте в парах |
| Work in groups | Работайте в группах |
| Stand up | Встаньте |
| Sit down | Сядьте |
| Be quiet | Тихо |
| Raise your hand | Поднимите руку |

**Can I...? (Можно мне...?):**

| Английский | Русский |
|------------|---------|
| Can I go out? | Можно выйти? |
| Can I come in? | Можно войти? |
| Can I open the window? | Можно открыть окно? |
| Can I borrow a pen? | Можно взять ручку? |
| Can I ask a question? | Можно задать вопрос? |

**Ответы учителя:**
\`\`\`
Yes, you can. — Да, можно.
No, you can't. — Нет, нельзя.
Of course. — Конечно.
Wait a minute. — Подожди минуту.
\`\`\`

**Where is...? (Где...?):**

| Английский | Русский |
|------------|---------|
| Where is the pen? | Где ручка? |
| It's on the desk | Она на парте |
| It's in the bag | Она в портфеле |
| It's under the desk | Она под партой |`,
          ["Open your books on page 5 = Откройте книги на странице 5", "Can I...? = Можно мне...?", "Work in pairs = Работайте в парах"],
          ["Listen to me = Послушайте меня", "Look at the board = Посмотрите на доску", "Raise your hand = Поднимите руку"]),
        L("Урок 15: Распорядок дня", "Daily routine.", [
          "Говорить о режиме дня",
          "Использовать Present Simple",
          "Указывать время",
          "Описывать будни"
        ], `**Daily routine (Распорядок дня):**

| Английский | Русский |
|------------|---------|
| wake up | просыпаться |
| get up | вставать |
| have breakfast | завтракать |
| go to school | идти в школу |
| have lessons | иметь уроки |
| have lunch | обедать |
| come home | приходить домой |
| do homework | делать домашнее задание |
| have dinner | ужинать |
| watch TV | смотреть телевизор |
| read a book | читать книгу |
| play games | играть в игры |
| go to bed | ложиться спать |

**Time (Время):**

| Английский | Русский |
|------------|---------|
| What time is it? | Который час? |
| It's... o'clock | ...часов |
| It's half past... | Половина... |
| It's quarter past... | Четверть после... |
| It's quarter to... | Без четверти... |

**Примеры времени:**
\`\`\`
It's 7 o'clock. = 7 часов.
It's half past 3. = Половина четвёртого.
It's quarter past 5. = Четверть шестого.
It's quarter to 8. = Без четверти восемь.
\`\`\`

**Present Simple for daily routine:**

| Утверждение | Вопрос | Отрицание |
|-------------|--------|-----------|
| I get up at 7. | Do you get up at 7? | I don't get up at 7. |
| He gets up at 7. | Does he get up at 7? | He doesn't get up at 7. |

**My day (Мой день):**
\`\`\`
I wake up at 7 o'clock.
I get up and have breakfast.
I go to school at 8 o'clock.
I have lunch at school at 12.
I come home at 3 o'clock.
I do my homework.
I have dinner at 6 o'clock.
I watch TV and play games.
I go to bed at 10 o'clock.
\`\`\`

**Adverbs of frequency (Наречия частотности):**

| Английский | Русский | % |
|------------|---------|---|
| always | всегда | 100% |
| usually | обычно | 80% |
| often | часто | 60% |
| sometimes | иногда | 40% |
| rarely / seldom | редко | 20% |
| never | никогда | 0% |

**Позиция:** перед глаголом
\`\`\`
I always have breakfast.
She usually gets up at 7.
He never watches TV in the morning.
\`\`\``,
          ["Present Simple — для регулярных действий", "Do/Does — вспомогательные глаголы для вопросов", "Наречия частотности — перед глаголом"],
          ["wake up = просыпаться, get up = вставать", "do homework = делать домашнее задание", "always, usually, often, sometimes, never"]),
        L("Урок 16: Выходные и каникулы", "Weekends and holidays.", [
          "Говорить о выходных",
          "Обсуждать планы",
          "Рассказывать о каникулах",
          "Использовать Past Simple"
        ], `**Weekend (Выходные):**

| Английский | Русский |
|------------|---------|
| weekend | выходные |
| Saturday | суббота |
| Sunday | воскресенье |
| What do you do at the weekend? | Что ты делаешь в выходные? |

**Days of the week (Дни недели):**

| Английский | Русский |
|------------|---------|
| Monday | понедельник |
| Tuesday | вторник |
| Wednesday | среда |
| Thursday | четверг |
| Friday | пятница |
| Saturday | суббота |
| Sunday | воскресенье |

**Activities (Занятия):**

| Английский | Русский |
|------------|---------|
| visit friends | навещать друзей |
| go shopping | ходить по магазинам |
| go to the cinema | ходить в кино |
| play sports | заниматься спортом |
| read books | читать книги |
| watch films | смотреть фильмы |
| meet friends | встречаться с друзьями |
| sleep late | спать допоздна |

**Holidays (Праздники):**

| Английский | Русский |
|------------|---------|
| holiday | праздник, каникулы |
| New Year | Новый год |
| Christmas | Рождество |
| birthday | день рождения |
| summer holidays | летние каникулы |
| winter holidays | зимние каникулы |

**Past Simple (Прошедшее время):**

**Правильные глаголы (+ed):**

| Инфинитив | Past Simple |
|-----------|-------------|
| play | played |
| watch | watched |
| visit | visited |
| walk | walked |

**Неправильные глаголы:**

| Инфинитив | Past Simple |
|-----------|-------------|
| go | went |
| see | saw |
| have | had |
| do | did |
| eat | ate |
| buy | bought |

**Рассказ о выходных:**
\`\`\`
Last weekend I went to the cinema.
I saw a very interesting film.
On Sunday I visited my grandmother.
We had dinner together.
I played with my cousin.
It was a great weekend!
\`\`\`

**Past Simple — вопросы:**

| Английский | Русский |
|------------|---------|
| What did you do? | Что ты делал? |
| Where did you go? | Куда ты ходил? |
| Did you have fun? | Тебе было весело? |
| Yes, I did / No, I didn't | Да / Нет |`,
          ["Дни недели пишутся с большой буквы", "Last weekend = прошлые выходные", "Did + глагол для вопросов в Past Simple"],
          ["Saturday, Sunday — выходные", "Holiday = праздник или каникулы", "Last = прошлый"])
      ]
    },
    {
      topic: "Еда и покупки",
      lessons: [
        L("Урок 17: Продукты питания", "Food.", [
          "Называть продукты",
          "Обсуждать предпочтения",
          "Составлять меню",
          "Говорить о здоровом питании"
        ], `**Food (Еда):**

**Fruit (Фрукты):**

| Английский | Русский |
|------------|---------|
| apple | яблоко |
| banana | банан |
| orange | апельсин |
| lemon | лимон |
| pear | груша |
| peach | персик |
| grapes | виноград |
| strawberry | клубника |

**Vegetables (Овощи):**

| Английский | Русский |
|------------|---------|
| potato | картофель |
| tomato | помидор |
| carrot | морковь |
| cucumber | огурец |
| onion | лук |
| cabbage | капуста |

**Meat and fish (Мясо и рыба):**

| Английский | Русский |
|------------|---------|
| meat | мясо |
| chicken | курица |
| beef | говядина |
| pork | свинина |
| fish | рыба |

**Dairy (Молочные продукты):**

| Английский | Русский |
|------------|---------|
| milk | молоко |
| cheese | сыр |
| butter | масло |
| yoghurt | йогурт |
| egg | яйцо |

**Drinks (Напитки):**

| Английский | Русский |
|------------|---------|
| water | вода |
| tea | чай |
| coffee | кофе |
| juice | сок |
| milk | молоко |

**Other (Другое):**

| Английский | Русский |
|------------|---------|
| bread | хлеб |
| rice | рис |
| pasta | макароны |
| soup | суп |
| sandwich | бутерброд |
| cake | торт |
| chocolate | шоколад |
| ice cream | мороженое |

**Like / Don't like:**

| Английский | Русский |
|------------|---------|
| I like apples | Мне нравятся яблоки |
| I don't like fish | Мне не нравится рыба |
| Do you like...? | Тебе нравится...? |
| Yes, I do / No, I don't | Да / Нет |

**Healthy eating (Здоровое питание):**

| Английский | Русский |
|------------|---------|
| healthy food | здоровая еда |
| unhealthy food | нездоровая еда |
| fast food | фастфуд |
| vegetables are healthy | овощи полезны |
| fruit is good for you | фрукты полезны |`,
          ["Fruit — собирательное, fruits — виды фруктов", "Some + неисчисляемые: some water, some bread", "I like apples (мн.ч. для общего предпочтения)"],
          ["Fruit and vegetables — фрукты и овощи", "Healthy = полезный, здоровый", "Fast food = фастфуд"]),
        L("Урок 18: В кафе и ресторане", "At the café.", [
          "Делать заказ",
          "Спрашивать о блюдах",
          "Платить за заказ",
          "Выражать мнение"
        ], `**At the café (В кафе):**

**Useful phrases (Полезные фразы):**

| Английский | Русский |
|------------|---------|
| Can I have...? | Можно мне...? |
| I'd like... | Я хотел бы... |
| I would like... | Я хотел бы... |
| What would you like? | Что вы хотели бы? |
| Here is the menu | Вот меню |
| Are you ready to order? | Вы готовы заказать? |

**Making order (Заказ):**

\`\`\`
Waiter: Hello! What would you like?
Customer: Can I have a pizza, please?
Waiter: Anything to drink?
Customer: I'd like some orange juice.
Waiter: Here you are.
Customer: Thank you.
\`\`\`

**Questions about food (Вопросы о еде):**

| Английский | Русский |
|------------|---------|
| What's this? | Что это? |
| Is it spicy? | Это острое? |
| Is it vegetarian? | Это вегетарианское? |
| How much is it? | Сколько это стоит? |

**Opinions (Мнения):**

| Английский | Русский |
|------------|---------|
| It's delicious | Это вкусно |
| It's tasty | Это вкусно |
| It's good | Это хорошо |
| It's not very good | Это не очень хорошо |
| It's too salty | Это слишком солёно |
| I like it | Мне это нравится |
| I don't like it | Мне это не нравится |

**Paying (Оплата):**

| Английский | Русский |
|------------|---------|
| Can I have the bill, please? | Можно счёт, пожалуйста? |
| How much is it? | Сколько это стоит? |
| Here you are | Вот |
| Keep the change | Сдачи не надо |
| Thank you | Спасибо |
| You're welcome | Пожалуйста |

**Money (Деньги):**

| Английский | Русский |
|------------|---------|
| money | деньги |
| pound (£) | фунт |
| dollar ($) | доллар |
| euro (€) | евро |
| rouble | рубль |`,
          ["I'd like = I would like (вежливая форма)", "Can I have...? = Можно мне...?", "The bill = счёт (британский), the check = счёт (американский)"],
          ["What would you like? = Что вы хотели бы?", "It's delicious = Это очень вкусно", "How much is it? = Сколько это стоит?"]),
        L("Урок 19: Покупки", "Shopping.", [
          "Называть магазины",
          "Спрашивать цену",
          "Совершать покупки",
          "Обсуждать одежду"
        ], `**Shops (Магазины):**

| Английский | Русский |
|------------|---------|
| shop / store | магазин |
| supermarket | супермаркет |
| market | рынок |
| bookshop | книжный магазин |
| clothes shop | магазин одежды |
| shoe shop | обувной магазин |
| toy shop | магазин игрушек |
| bakery | пекарня, булочная |
| butcher's | мясной магазин |
| chemist's / pharmacy | аптека |

**Shopping phrases (Фразы для покупок):**

| Английский | Русский |
|------------|---------|
| I'm looking for... | Я ищу... |
| Can I try it on? | Можно примерить? |
| Where is the fitting room? | Где примерочная? |
| What size is this? | Какой это размер? |
| Do you have this in a bigger/smaller size? | Это есть в большем/меньшем размере? |
| How much is this? | Сколько это стоит? |
| How much are these? | Сколько это стоит? (мн.ч.) |
| It's too expensive | Это слишком дорого |
| It's cheap | Это дешево |
| I'll take it | Я возьму это |
| Can I pay by card? | Можно оплатить картой? |

**Numbers for prices:**

| Английский | Русский |
|------------|---------|
| £5 | five pounds |
| $10 | ten dollars |
| €20 | twenty euros |
| 100 roubles | сто рублей |

**Dialogue:**
\`\`\`
Assistant: Can I help you?
Customer: Yes, I'm looking for a T-shirt.
Assistant: What size?
Customer: Medium, please.
Assistant: Here you are.
Customer: How much is it?
Assistant: It's £15.
Customer: I'll take it.
\`\`\`

**Sizes:**

| Английский | Русский |
|------------|---------|
| small (S) | маленький |
| medium (M) | средний |
| large (L) | большой |
| extra large (XL) | очень большой |`,
          ["How much is...? = Сколько стоит...? (единственное)", "How much are...? = Сколько стоят...? (множественное)", "I'll take it = Я возьму это"],
          ["Shop — британский, Store — американский", "Fitting room = примерочная", "Pay by card = оплатить картой"]),
        L("Урок 20: Одежда", "Clothes.", [
          "Называть предметы одежды",
          "Описывать наряд",
          "Обсуждать моды",
          "Говорить о размерах"
        ], `**Clothes (Одежда):**

**Basic clothes (Базовая одежда):**

| Английский | Русский |
|------------|---------|
| clothes | одежда |
| T-shirt | футболка |
| shirt | рубашка |
| trousers / pants | брюки |
| jeans | джинсы |
| skirt | юбка |
| dress | платье |
| jacket | куртка |
| coat | пальто |
| sweater | свитер |
| shorts | шорты |

**Shoes and accessories (Обувь и аксессуары):**

| Английский | Русский |
|------------|---------|
| shoes | туфли, обувь |
| trainers / sneakers | кроссовки |
| boots | ботинки |
| socks | носки |
| hat | шляпа |
| cap | кепка |
| scarf | шарф |
| gloves | перчатки |
| bag | сумка |

**Colours (Цвета):**

| Английский | Русский |
|------------|---------|
| red | красный |
| blue | синий |
| green | зелёный |
| yellow | жёлтый |
| orange | оранжевый |
| black | чёрный |
| white | белый |
| grey / gray | серый |
| brown | коричневый |
| pink | розовый |
| purple | фиолетовый |

**Describing clothes (Описание одежды):**

| Английский | Русский |
|------------|---------|
| What are you wearing? | Что на тебе надето? |
| I'm wearing... | На мне надето... |
| It's a red T-shirt | Это красная футболка |
| They're blue jeans | Это синие джинсы |

**Example:**
\`\`\`
What are you wearing today?
I'm wearing a blue T-shirt, black jeans 
and white trainers.
\`\`\`

**Seasonal clothes:**

| Сезон | Одежда |
|-------|--------|
| Winter | coat, sweater, boots, scarf, gloves |
| Summer | T-shirt, shorts, sandals, dress |

**Wear / Put on / Take off:**

| Английский | Русский |
|------------|---------|
| wear | носить (одежду) |
| put on | надевать |
| take off | снимать |

\`\`\`
I wear a uniform to school.
I put on my jacket before going out.
I take off my shoes at home.
\`\`\``,
          ["Trousers — британский, Pants — американский", "Trainers — британский, Sneakers — американский", "Clothes — только множественное число"],
          ["I'm wearing = На мне надето (сейчас)", "wear = носить, put on = надевать", "Colours — цвета"])
      ]
    },
    {
      topic: "Грамматика",
      lessons: [
        L("Урок 21: Present Simple", "Настоящее простое.", [
          "Образовывать утверждения",
          "Задавать вопросы",
          "Отвечать на вопросы",
          "Использовать с наречиями"
        ], `**Present Simple** — настоящее простое время.

**Употребление:**
- Регулярные, повторяющиеся действия
- Постоянные состояния
- Факты и истины

**Formation (Образование):**

**Positive (Утверждение):**

| Лицо | Форма | Пример |
|------|-------|--------|
| I | V | I play tennis |
| You | V | You play tennis |
| He | V+s/es | He plays tennis |
| She | V+s/es | She plays tennis |
| It | V+s/es | It works well |
| We | V | We play tennis |
| They | V | They play tennis |

**Окончание -s/-es:**

| Правило | Пример |
|---------|--------|
| Большинство глаголов + s | play → plays |
| Окончание на -o, -s, -x, -ch, -sh + es | watch → watches, go → goes |
| Окончание на согласную + y → ies | study → studies |
| Окончание на гласную + y + s | play → plays |

**Negative (Отрицание):**

| Лицо | Форма | Пример |
|------|-------|--------|
| I/You | don't + V | I don't play |
| He/She/It | doesn't + V | He doesn't play |
| We/They | don't + V | We don't play |

**Question (Вопрос):**

| Лицо | Форма | Пример |
|------|-------|--------|
| I/You | Do + S + V? | Do you play? |
| He/She/It | Does + S + V? | Does he play? |
| We/They | Do + S + V? | Do they play? |

**Short answers (Краткие ответы):**

| Вопрос | Положительный | Отрицательный |
|--------|---------------|---------------|
| Do you play? | Yes, I do. | No, I don't. |
| Does he play? | Yes, he does. | No, he doesn't. |

**Time expressions (Слова-маркеры):**

| Английский | Русский |
|------------|---------|
| always | всегда |
| usually | обычно |
| often | часто |
| sometimes | иногда |
| rarely / seldom | редко |
| never | никогда |
| every day | каждый день |
| on Mondays | по понедельникам |

**Позиция:** перед глаголом
\`\`\`
I always get up at 7.
She never eats meat.
We usually watch TV in the evening.
\`\`\``,
          ["He/She/It + глагол с окончанием -s/-es", "Don't/Doesn't + глагол БЕЗ окончания", "Наречия частотности — перед глаголом"],
          ["Present Simple = регулярные действия", "Do/Does — для вопросов и отрицаний", "Always, usually, often, sometimes, never"]),
        L("Урок 22: Present Continuous", "Настоящее продолженное.", [
          "Образовывать форму",
          "Отличать от Present Simple",
          "Использовать для текущих действий",
          "Задавать вопросы"
        ], `**Present Continuous** — настоящее продолженное время.

**Употребление:**
- Действие происходит прямо сейчас
- Временная ситуация
- Планы на ближайшее будущее

**Formation (Образование):**

\`\`\`
Subject + am/is/are + Verb-ing
\`\`\`

**Positive (Утверждение):**

| Лицо | Форма | Пример |
|------|-------|--------|
| I | am + V-ing | I am reading |
| You | are + V-ing | You are reading |
| He | is + V-ing | He is reading |
| She | is + V-ing | She is reading |
| It | is + V-ing | It is running |
| We | are + V-ing | We are reading |
| They | are + V-ing | They are reading |

**Short forms (Краткие формы):**

| Полная форма | Краткая форма |
|--------------|---------------|
| I am reading | I'm reading |
| You are reading | You're reading |
| He is reading | He's reading |
| She is reading | She's reading |
| We are reading | We're reading |
| They are reading | They're reading |

**Negative (Отрицание):**

| Лицо | Форма | Пример |
|------|-------|--------|
| I | am not + V-ing | I am not reading |
| You | are not + V-ing | You aren't reading |
| He/She/It | is not + V-ing | He isn't reading |
| We/They | are not + V-ing | We aren't reading |

**Question (Вопрос):**

| Форма | Пример |
|-------|--------|
| Am I + V-ing? | Am I reading? |
| Are you + V-ing? | Are you reading? |
| Is he/she/it + V-ing? | Is he reading? |
| Are we/they + V-ing? | Are they reading? |

**Spelling rules (Правила написания):**

| Правило | Инфинитив | -ing форма |
|---------|-----------|------------|
| Большинство глаголов + ing | play | playing |
| Глаголы на немую -e: убираем e, добавляем ing | write | writing |
| Краткие глаголы (CVC): удваиваем последнюю букву | run | running |
| Глаголы на -ie: меняем на -y + ing | die | dying |

**Time expressions (Слова-маркеры):**

| Английский | Русский |
|------------|---------|
| now | сейчас |
| at the moment | в данный момент |
| at present | в настоящее время |
| today | сегодня |
| Look! | Смотри! |
| Listen! | Слушай! |

**Present Simple vs Present Continuous:**

| Present Simple | Present Continuous |
|----------------|-------------------|
| I play tennis every day | I am playing tennis now |
| Регулярное действие | Действие сейчас |
| Always, usually, often | Now, at the moment |`,
          ["am/is/are + Verb-ing", "I'm = I am, He's = He is", "Look! / Listen! — признаки Present Continuous"],
          ["Present Continuous = действие прямо сейчас", "I'm reading = Я читаю (сейчас)", "Now, at the moment — маркеры времени"]),
        L("Урок 23: Past Simple", "Прошедшее простое.", [
          "Образовывать правильные глаголы",
          "Запоминать неправильные глаголы",
          "Задавать вопросы",
          "Рассказывать о прошлом"
        ], `**Past Simple** — прошедшее простое время.

**Употребление:**
- Действие завершилось в прошлом
- Указано время действия
- Последовательность действий в прошлом

**Regular verbs (Правильные глаголы):**

\`\`\`
Инфинитив + -ed
\`\`\`

| Правило | Инфинитив | Past Simple |
|---------|-----------|-------------|
| Большинство глаголов + ed | play | played |
| Окончание на -e + d | live | lived |
| Краткие глаголы (CVC): удваиваем + ed | stop | stopped |
| Согласная + y → ied | study | studied |

**Irregular verbs (Неправильные глаголы):**

| Инфинитив | Past Simple | Русский |
|-----------|-------------|---------|
| be | was/were | быть |
| go | went | идти |
| come | came | приходить |
| see | saw | видеть |
| have | had | иметь |
| do | did | делать |
| make | made | делать |
| take | took | брать |
| give | gave | давать |
| get | got | получать |
| know | knew | знать |
| think | thought | думать |
| say | said | говорить |
| eat | ate | есть |
| drink | drank | пить |
| buy | bought | покупать |
| read | read | читать |
| write | wrote | писать |
| run | ran | бежать |
| speak | spoke | говорить |

**Positive (Утверждение):**

\`\`\`
I played football yesterday.
She went to school last week.
They were happy.
\`\`\`

**Negative (Отрицание):**

\`\`\`
I did not (didn't) play football.
She did not (didn't) go to school.
\`\`\`

**Question (Вопрос):**

\`\`\`
Did you play football?
Did she go to school?
\`\`\`

**Short answers:**

| Вопрос | Положительный | Отрицательный |
|--------|---------------|---------------|
| Did you play? | Yes, I did. | No, I didn't. |

**Time expressions (Слова-маркеры):**

| Английский | Русский |
|------------|---------|
| yesterday | вчера |
| last week | на прошлой неделе |
| last month | в прошлом месяце |
| last year | в прошлом году |
| ... ago | ... назад |
| in 2020 | в 2020 году |`,
          ["Правильные глаголы + ed", "Неправильные глаголы — нужно запоминать", "Did + инфинитив для вопросов и отрицаний"],
          ["Past Simple = прошедшее время", "Yesterday, last week, ... ago — маркеры", "Did you...? = Ты делал...?"]),
        L("Урок 24: Future Simple", "Будущее простое.", [
          "Использовать will",
          "Говорить о планах",
          "Делать предсказания",
          "Обсуждать будущее"
        ], `**Future Simple** — будущее простое время.

**Употребление:**
- Мгновенные решения
- Предсказания
- Обещания
- Предложения и просьбы

**Formation (Образование):**

\`\`\`
Subject + will + Verb
\`\`\`

**Positive (Утверждение):**

| Полная форма | Краткая форма |
|--------------|---------------|
| I will play | I'll play |
| You will play | You'll play |
| He will play | He'll play |
| She will play | She'll play |
| We will play | We'll play |
| They will play | They'll play |

**Negative (Отрицание):**

| Полная форма | Краткая форма |
|--------------|---------------|
| I will not play | I won't play |
| You will not play | You won't play |
| He will not play | He won't play |

**Question (Вопрос):**

\`\`\`
Will you play?
Will he come?
Will they help?
\`\`\`

**Short answers:**

| Вопрос | Положительный | Отрицательный |
|--------|---------------|---------------|
| Will you come? | Yes, I will. | No, I won't. |

**Uses (Употребление):**

**1. Instant decisions (Мгновенные решения):**
\`\`\`
It's cold. I'll close the window.
I'm hungry. I'll make a sandwich.
\`\`\`

**2. Predictions (Предсказания):**
\`\`\`
It will rain tomorrow.
You will pass the exam.
\`\`\`

**3. Promises (Обещания):**
\`\`\`
I'll help you.
I'll call you tomorrow.
\`\`\`

**4. Offers and requests (Предложения и просьбы):**
\`\`\`
I'll help you with that. (offer)
Will you help me? (request)
\`\`\`

**Time expressions (Слова-маркеры):**

| Английский | Русский |
|------------|---------|
| tomorrow | завтра |
| next week | на следующей неделе |
| next month | в следующем месяце |
| next year | в следующем году |
| soon | скоро |
| in the future | в будущем |
| later | позже |

**be going to vs will:**

| be going to | will |
|-------------|------|
| Планы и намерения | Мгновенные решения |
| I'm going to study medicine | I'll have a coffee |
| Уже решено | Решено сейчас |`,
          ["I'll = I will (краткая форма)", "won't = will not", "Tomorrow, next week, soon — маркеры будущего"],
          ["Future Simple = will + глагол", "I'll help = Я помогу", "Will you...? = Ты будешь...?"])
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
