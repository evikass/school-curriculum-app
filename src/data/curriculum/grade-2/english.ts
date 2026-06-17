import { Subject } from '../../types'

export const grade2English: Subject = {
  title: "Английский",
  icon: "Languages",
  color: "text-pink-400",
  topics: [
    "Приветствие",
    "Мой дом",
    "Еда",
    "Животные",
    "Погода",
    "Present Simple",
    "Дни недели и месяцы"
  ],
  detailedTopics: [
    {
      topic: "Приветствие",
      lessons: [
        {
          title: "Урок 1: Hello! Приветствие и знакомство",
          description: "Как поздороваться и представиться по-английски",
          tasks: [
            "Обвести по контуру слова: Hello, Hi, Good morning",
            "Найти буквы в словах: Hello, name, friend",
            "Составить из карточек диалог приветствия",
            "Дописать пропущенную букву: H_llo, G_od morning"
          ],
          theory: "Hello и Hi — самые распространённые приветствия в английском языке. Hello — более формальное, Hi — неформальное, дружеское. Good morning — доброе утро, Good afternoon — добрый день, Good evening — добрый вечер. При знакомстве говорят: My name is... (Меня зовут...), Nice to meet you! (Приятно познакомиться!).",
          content: "## Hello! Приветствие и знакомство\n\n**Приветствия:**\n- **Hello!** — Здравствуй! (формально)\n- **Hi!** — Привет! (неформально)\n- **Good morning!** — Доброе утро!\n- **Good afternoon!** — Добрый день!\n- **Good evening!** — Добрый вечер!\n\n**Знакомство:**\n- **My name is Anna.** — Меня зовут Анна.\n- **I am 8.** — Мне 8 лет.\n- **Nice to meet you!** — Приятно познакомиться!\n- **How are you?** — Как дела?\n- **I am fine, thank you!** — Хорошо, спасибо!\n\n**Прощание:**\n- **Goodbye!** — До свидания!\n- **Bye!** — Пока!\n- **See you!** — Увидимся!",
          keyPoints: [
            "Hello / Hi — приветствие",
            "My name is... — Меня зовут...",
            "Nice to meet you! — Приятно познакомиться!",
            "How are you? — Как дела?"
          ],
          examples: [
            "— Hello! My name is Tom. — Hi, Tom! I am Lucy.",
            "— Good morning! — Good morning! How are you?",
            "— Nice to meet you! — Nice to meet you too!"
          ],
          facts: [
            "Английский язык — самый распространённый в мире",
            "Hello — одно из самых узнаваемых слов на планете",
            "Впервые слово 'hello' как приветствие использовал Томас Эдисон"
          ],
          image: "/school-curriculum-app/images/lessons/grade-2/english/greetings.svg"
        },
        {
          title: "Урок 2: What is your name? Как тебя зовут?",
          description: "Умение спрашивать имя и отвечать",
          tasks: [
            "Обвести по контуру вопрос What is your name?",
            "Найти буквы в словах: name, your, what, is",
            "Составить из карточек вопрос и ответ",
            "Дописать пропущенную букву: Wh_t is y_ur n_me?"
          ],
          theory: "What is your name? — Как тебя зовут? Это один из самых важных вопросов при знакомстве. Ответ: My name is... или I am... Сокращённые формы: What's your name? (Что сокращается с is). Можно также спросить: How old are you? (Сколько тебе лет?) — I am 8 (Мне 8 лет).",
          content: "## What is your name?\n\n**Вопросы при знакомстве:**\n- **What is your name?** — Как тебя зовут?\n- **My name is Olga.** — Меня зовут Ольга.\n- **I am Olga.** — Я Ольга.\n\n**Сколько тебе лет:**\n- **How old are you?** — Сколько тебе лет?\n- **I am 8.** / **I am 8 years old.** — Мне 8 лет.\n\n**Откуда ты:**\n- **Where are you from?** — Откуда ты?\n- **I am from Russia.** — Я из России.\n\n**Сокращения:**\n- What is → What's\n- My name is → My name's\n- I am → I'm",
          keyPoints: [
            "What is your name? — Как тебя зовут?",
            "My name is... — Меня зовут...",
            "How old are you? — Сколько тебе лет?",
            "I am from Russia. — Я из России."
          ],
          examples: [
            "— What's your name? — My name is Sasha.",
            "— How old are you? — I'm 8.",
            "— Where are you from? — I'm from Russia."
          ],
          facts: [
            "В английском языке имена пишутся с большой буквы",
            "Russia по-английски — Россия",
            "Английские дети тоже учатся представляться в школе"
          ],
          image: "/school-curriculum-app/images/lessons/grade-2/english/what-is-your-name.svg"
        },
        {
          title: "Урок 3: Numbers 1–20. Числа от 1 до 20",
          description: "Числа на английском языке",
          tasks: [
            "Обвести по контуру числа: one, two, three",
            "Найти буквы в числах от 1 до 20",
            "Составить из карточек числа по порядку",
            "Дописать пропущенную букву: th_ee, s_ven, t_lve"
          ],
          theory: "Числа от 1 до 20 — основа английского счёта. 1-10: one, two, three, four, five, six, seven, eight, nine, ten. 11-20 имеют особые формы: eleven, twelve, а с 13 до 19 — добавляется -teen: thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen. Twenty — 20.",
          content: "## Numbers 1–20\n\n**1–10:**\none (1), two (2), three (3), four (4), five (5),\nsix (6), seven (7), eight (8), nine (9), ten (10)\n\n**11–20:**\neleven (11), twelve (12), thirteen (13), fourteen (14),\nfifteen (15), sixteen (16), seventeen (17), eighteen (18),\nnineteen (19), twenty (20)\n\n**Особенности:**\n- 11 и 12 — уникальные формы (не ten-one!)\n- 13–19: число + -teen (three → thir**teen**)\n- 15: fifteen (не fiveteen!)\n- 20: twenty (two → twen**ty**)\n\n**Пример:** How old are you? — I am **eight**.",
          keyPoints: [
            "1-10: one, two, three, four, five, six, seven, eight, nine, ten",
            "11-12: eleven, twelve — уникальные",
            "13-19: число + -teen",
            "20: twenty"
          ],
          examples: [
            "I have **three** cats. — У меня 3 кошки.",
            "There are **seven** days in a week.",
            "I am **eight** years old."
          ],
          facts: [
            "Числа 13-19 в английском называются 'teen' — отсюда слово 'teenager'",
            "Число 13 считается несчастливым в англоязычных странах",
            "В английском нет слова для 1,5 — говорят 'one and a half'"
          ],
          image: "/school-curriculum-app/images/lessons/grade-2/english/numbers.svg"
        }
      ]
    },
    {
      topic: "Мой дом",
      lessons: [
        {
          title: "Урок 4: My house. Мой дом",
          description: "Комнаты и предметы в доме",
          tasks: [
            "Обвести по контуру слова: house, room, kitchen, bedroom",
            "Найти буквы в словах: bathroom, living room, door",
            "Составить из карточек названия комнат",
            "Дописать пропущенную букву: h_use, k_tchen, b_dr_om"
          ],
          theory: "House — дом, room — комната. Основные комнаты: bedroom (спальня), living room (гостиная), kitchen (кухня), bathroom (ванная). Мебель: bed (кровать), table (стол), chair (стул), sofa (диван), wardrobe (шкаф). This is my house. — Это мой дом. There is a bed in the bedroom. — В спальне есть кровать.",
          content: "## My house. Мой дом\n\n**Комнаты:**\n- **House** — дом\n- **Room** — комната\n- **Bedroom** — спальня\n- **Living room** — гостиная\n- **Kitchen** — кухня\n- **Bathroom** — ванная\n- **Hall** — прихожая\n\n**Мебель:**\n- **Bed** — кровать\n- **Table** — стол\n- **Chair** — стул\n- **Sofa** — диван\n- **Wardrobe** — шкаф\n- **Desk** — письменный стол\n\n**Фразы:**\n- This is my house. — Это мой дом.\n- There is a bed in the bedroom. — В спальне есть кровать.\n- I like my room! — Мне нравится моя комната!",
          keyPoints: [
            "House — дом, room — комната",
            "Bedroom, living room, kitchen, bathroom",
            "Bed, table, chair, sofa — мебель",
            "This is my house — Это мой дом"
          ],
          examples: [
            "My bedroom is big. — Моя спальня большая.",
            "There is a table in the kitchen. — На кухне есть стол.",
            "I have a red sofa. — У меня красный диван."
          ],
          facts: [
            "Типичный английский дом — небольшой коттедж с камином",
            "В Англии дома нумеруются от центра города",
            "Англичане говорят 'house' про отдельный дом и 'flat' про квартиру"
          ],
          image: "/school-curriculum-app/images/lessons/grade-2/english/my-house.svg"
        },
        {
          title: "Урок 5: In my room. В моей комнате",
          description: "Описание своей комнаты на английском",
          tasks: [
            "Обвести по контуру слова-описания: big, small, clean",
            "Найти буквы в словах: window, lamp, carpet, picture",
            "Составить из карточек описание комнаты",
            "Дописать пропущенную букву: w_ndow, l_mp, c_rpet"
          ],
          theory: "Чтобы описать комнату, используем прилагательные: big (большой), small (маленький), nice (милый), clean (чистый), cosy (уютный). Конструкция There is / There are: There is a lamp on the desk. — На столе есть лампа. There are books on the shelf. — На полке есть книги. There is — для одного предмета, There are — для нескольких.",
          content: "## In my room. В моей комнате\n\n**Прилагательные:**\n- **Big** — большой\n- **Small** — маленький\n- **Nice** — красивый\n- **Clean** — чистый\n- **Cosy** — уютный\n\n**Предметы:**\n- **Window** — окно\n- **Lamp** — лампа\n- **Carpet** — ковёр\n- **Picture** — картина\n- **Shelf** — полка\n- **Mirror** — зеркало\n\n**Конструкция There is / There are:**\n- **There is** + одно: There is a lamp on the desk.\n- **There are** + много: There are books on the shelf.\n\n**Описание:** My room is small but cosy. There is a bed, a desk and a chair. There are books on the shelf. I like my room!",
          keyPoints: [
            "Big, small, nice, clean, cosy — описания",
            "There is + одно, There are + много",
            "On, in, under — предлоги места",
            "My room is... — Моя комната..."
          ],
          examples: [
            "There is a window in my room.",
            "There are toys under the bed.",
            "My room is small but cosy."
          ],
          facts: [
            "Англичане часто говорят 'my room' вместо 'bedroom'",
            "В английских домах часто есть камин (fireplace)",
            "Carpet в английском — и ковёр, и ковровое покрытие"
          ],
          image: "/school-curriculum-app/images/lessons/grade-2/english/my-room.svg"
        }
      ]
    },
    {
      topic: "Еда",
      lessons: [
        {
          title: "Урок 6: Food. Еда",
          description: "Названия продуктов питания по-английски",
          tasks: [
            "Обвести по контуру слова: apple, bread, milk, cheese",
            "Найти буквы в словах: meat, fish, egg, soup",
            "Составить из карточек продукты на английском",
            "Дописать пропущенную букву: _pple, br_ad, m_lk"
          ],
          theory: "Food — еда. Основные продукты: apple (яблоко), bread (хлеб), milk (молоко), cheese (сыр), meat (мясо), fish (рыба), egg (яйцо), soup (суп), rice (рис), butter (масло). I like apples. — Я люблю яблоки. I don't like fish. — Я не люблю рыбу. Do you like cheese? — Ты любишь сыр?",
          content: "## Food. Еда\n\n**Продукты:**\n- **Apple** — яблоко | **Banana** — банан\n- **Bread** — хлеб | **Butter** — масло\n- **Milk** — молоко | **Cheese** — сыр\n- **Meat** — мясо | **Fish** — рыба\n- **Egg** — яйцо | **Soup** — суп\n- **Rice** — рис | **Potato** — картофель\n- **Tomato** — помидор | **Carrot** — морковь\n\n**Фразы:**\n- I like apples. — Я люблю яблоки.\n- I don't like fish. — Я не люблю рыбу.\n- Do you like cheese? — Ты любишь сыр?\n- Yes, I do. / No, I don't. — Да. / Нет.\n- Can I have some milk, please? — Можно мне молока?",
          keyPoints: [
            "Apple, bread, milk, cheese, meat, fish",
            "I like... — Я люблю...",
            "I don't like... — Я не люблю...",
            "Do you like...? — Ты любишь...?"
          ],
          examples: [
            "I like bananas and milk.",
            "I don't like soup.",
            "Do you like cheese? — Yes, I do!"
          ],
          facts: [
            "В Англии популярен 'fish and chips' — рыба с картошкой",
            "Англичане пьют чай с молоком",
            "Традиционный английский завтрак — яичница, бекон, тосты"
          ],
          image: "/school-curriculum-app/images/lessons/grade-2/english/food.svg"
        },
        {
          title: "Урок 7: I like / I don't like",
          description: "Выражение предпочтений в еде",
          tasks: [
            "Обвести по контуру фразы I like и I don't like",
            "Найти буквы в словах: like, love, prefer, hate",
            "Составить из карточек предложения о предпочтениях",
            "Дописать пропущенную букву: I l_ke _pples"
          ],
          theory: "I like — я люблю, I don't like — я не люблю. Для усиления: I love — я обожаю, I really like — мне очень нравится. Конструкция: I like + существительное во множественном числе или неисчисляемое: I like apples (яблоки), I like milk (молоко). Do you like...? — Вопрос. Yes, I do / No, I don't — ответ.",
          content: "## I like / I don't like\n\n**Выражение предпочтений:**\n- **I like apples.** — Я люблю яблоки.\n- **I don't like fish.** — Я не люблю рыбу.\n- **I love pizza!** — Я обожаю пиццу!\n- **I really like ice cream.** — Мне очень нравится мороженое.\n\n**Вопросы и ответы:**\n- **Do you like cheese?** — Ты любишь сыр?\n- **Yes, I do!** — Да!\n- **No, I don't.** — Нет.\n\n**Правило:**\n- I like + множественное число: I like apples (не 'apple')\n- I like + неисчисляемое: I like milk (не 'milks')\n\n**Диалог:**\n— Do you like bananas? — Yes, I do! I love bananas!\n— Do you like soup? — No, I don't. I don't like soup.",
          keyPoints: [
            "I like... — люблю, I don't like... — не люблю",
            "I love — обожаю (сильнее)",
            "Do you like...? — вопрос",
            "Yes, I do / No, I don't — ответ"
          ],
          examples: [
            "I like pizza and ice cream!",
            "I don't like fish but I love chicken.",
            "— Do you like carrots? — No, I don't."
          ],
          facts: [
            "В Англии говорят 'I'm keen on...' вместо 'I like'",
            "Самая популярная еда в мире — пицца",
            "Англичане говорят 'yummy' — вкусно"
          ],
          image: "/school-curriculum-app/images/lessons/grade-2/english/i-like.svg"
        }
      ]
    },
    {
      topic: "Животные",
      lessons: [
        {
          title: "Урок 8: Animals. Животные",
          description: "Названия животных по-английски",
          tasks: [
            "Обвести по контуру слова: cat, dog, bird, fish",
            "Найти буквы в словах: elephant, monkey, tiger, lion",
            "Составить из карточек названия животных",
            "Дописать пропущенную букву: c_t, d_g, b_rd, f_sh"
          ],
          theory: "Animals — животные. Домашние: cat (кошка), dog (собака), fish (рыбка), hamster (хомяк), parrot (попугай). Дикие: bear (медведь), tiger (тигр), lion (лев), elephant (слон), monkey (обезьяна), giraffe (жираф). I have got a cat. — У меня есть кошка. A cat is a pet. — Кошка — домашнее животное.",
          content: "## Animals. Животные\n\n**Домашние (pets):**\n- **Cat** — кошка | **Dog** — собака\n- **Fish** — рыбка | **Hamster** — хомяк\n- **Parrot** — попугай | **Rabbit** — кролик\n\n**Дикие (wild animals):**\n- **Bear** — медведь | **Tiger** — тигр\n- **Lion** — лев | **Elephant** — слон\n- **Monkey** — обезьяна | **Giraffe** — жираф\n- **Wolf** — волк | **Fox** — лиса\n\n**Фразы:**\n- I have got a cat. — У меня есть кошка.\n- A cat is a pet. — Кошка — домашнее животное.\n- A tiger is a wild animal. — Тигр — дикое животное.\n- My cat is cute! — Моя кошка милая!",
          keyPoints: [
            "Cat, dog, fish, hamster — домашние",
            "Bear, tiger, lion, elephant — дикие",
            "I have got a... — У меня есть...",
            "Pet — домашнее, wild — дикое"
          ],
          examples: [
            "I have got a dog. His name is Rex.",
            "Elephants are big. Mice are small.",
            "My parrot is green and yellow."
          ],
          facts: [
            "Самое популярное домашнее животное в Англии — кошка",
            "Англичане называют собак 'man's best friend'",
            "В Лондонском зоопарке более 750 видов животных"
          ],
          image: "/school-curriculum-app/images/lessons/grade-2/english/animals.svg"
        },
        {
          title: "Урок 9: Can animals do it? Что умеют животные?",
          description: "Глагол can для описания способностей животных",
          tasks: [
            "Обвести по контуру глаголы: run, jump, swim, fly",
            "Найти буквы в словах: can, cannot, climb, sing",
            "Составить из карточек предложения с can",
            "Дописать пропущенную букву: A bird c_n fly"
          ],
          theory: "Can — мочь, уметь. Используется для описания способностей: A bird can fly. — Птица умеет летать. A fish can swim. — Рыба умеет плавать. Отрицание: cannot или can't (не умеет). Вопрос: Can a cat swim? — Умеет ли кошка плавать? Yes, it can. / No, it can't.",
          content: "## Can animals do it?\n\n**Глагол can (мочь, уметь):**\n- **A bird can fly.** — Птица умеет летать.\n- **A fish can swim.** — Рыба умеет плавать.\n- **A monkey can climb.** — Обезьяна умеет лазить.\n- **A dog can run.** — Собака умеет бегать.\n\n**Отрицание (can't / cannot):**\n- **A fish can't fly.** — Рыба не умеет летать.\n- **A bird can't swim.** — Птица не умеет плавать.\n\n**Вопросы:**\n- **Can a cat swim?** — Умеет ли кошка плавать?\n- **Yes, it can.** — Да.\n- **No, it can't.** — Нет.\n\n**Действия:** run (бежать), jump (прыгать), swim (плавать), fly (летать), climb (лазить), sing (петь).",
          keyPoints: [
            "Can — мочь, уметь",
            "can't / cannot — не мочь, не уметь",
            "Can + глагол: can fly, can swim",
            "Can...? — вопрос, Yes, it can / No, it can't"
          ],
          examples: [
            "A kangaroo can jump.",
            "A penguin can swim but can't fly.",
            "Can a dog climb trees? — No, it can't."
          ],
          facts: [
            "Слоны умеют плавать!",
            "Пингвины не умеют летать, но отлично плавают",
            "Кошки умеют поворачивать уши на 180 градусов"
          ],
          image: "/school-curriculum-app/images/lessons/grade-2/english/animals-can.svg"
        }
      ]
    },
    {
      topic: "Погода",
      lessons: [
        {
          title: "Урок 10: Weather. Погода",
          description: "Названия погодных явлений по-английски",
          tasks: [
            "Обвести по контуру слова: sunny, rainy, cloudy, windy",
            "Найти буквы в словах: snow, hot, cold, warm",
            "Составить из карточек описание погоды",
            "Дописать пропущенную букву: s_nny, r_iny, cl_udy"
          ],
          theory: "Weather — погода. Основные слова: sunny (солнечно), rainy (дождливо), cloudy (облачно), windy (ветрено), snowy (снежно), hot (жарко), cold (холодно), warm (тепло). It is sunny today. — Сегодня солнечно. What's the weather like? — Какая погода? It's cold and windy. — Холодно и ветрено.",
          content: "## Weather. Погода\n\n**Погодные слова:**\n- **Sunny** — солнечно | **Rainy** — дождливо\n- **Cloudy** — облачно | **Windy** — ветрено\n- **Snowy** — снежно | **Foggy** — туманно\n- **Hot** — жарко | **Cold** — холодно\n- **Warm** — тепло | **Cool** — прохладно\n\n**Фразы:**\n- **What's the weather like?** — Какая погода?\n- **It is sunny today.** — Сегодня солнечно.\n- **It's cold and windy.** — Холодно и ветрено.\n- **It's raining.** — Идёт дождь.\n- **It's snowing.** — Идёт снег.\n\n**Времена года:**\n- **Spring** — весна | **Summer** — лето\n- **Autumn** — осень | **Winter** — зима",
          keyPoints: [
            "Sunny, rainy, cloudy, windy, snowy",
            "Hot, cold, warm, cool",
            "What's the weather like? — Какая погода?",
            "It is... — Сейчас..."
          ],
          examples: [
            "It's sunny and warm today.",
            "It's raining. Take an umbrella!",
            "In winter it is cold and snowy."
          ],
          facts: [
            "В Англии часто бывает дождливая погода",
            "Англичане любят обсуждать погоду — это часть их культуры",
            "Самая высокая температура в Англии — 40.3°C (2022 год)"
          ],
          image: "/school-curriculum-app/images/lessons/grade-2/english/weather.svg"
        }
      ]
    },
    {
      topic: "Present Simple",
      lessons: [
        {
          title: "Урок 11: Present Simple — настоящее простое время",
          description: "Основное время для регулярных действий",
          tasks: [
            "Обвести по контуру маркеры: every day, usually, always",
            "Найти буквы в словах: every, usually, always, often",
            "Составить из карточек предложения в Present Simple",
            "Дописать пропущенную букву: I g_ to school every day"
          ],
          theory: "Present Simple используется для регулярных, повторяющихся действий. Маркеры: every day (каждый день), usually (обычно), always (всегда), often (часто). Правило: I/you/we/they + глагол (I play), he/she/it + глагол + -s/-es (she plays). Отрицание: I don't play, she doesn't play. Вопрос: Do you play? Does she play?",
          content: "## Present Simple\n\n**Настоящее простое время** — для регулярных действий.\n\n**Маркеры времени:**\nevery day, usually, always, often, sometimes\n\n**Утверждение:**\n- I play football every day. — Я играю в футбол каждый день.\n- She plays tennis. — Она играет в теннис. (+ -s)\n- He goes to school. — Он ходит в школу. (+ -es)\n\n**Отрицание:**\n- I don't play tennis. — Я не играю в теннис.\n- She doesn't play football. — Она не играет в футбол.\n\n**Вопрос:**\n- Do you like apples? — Ты любишь яблоки?\n- Does she play tennis? — Она играет в теннис?\n\n**Правило -s/-es:** he/she/it + глагол с -s или -es",
          keyPoints: [
            "Present Simple — регулярные действия",
            "Маркеры: every day, usually, always",
            "I play / She plays (+ -s)",
            "don't / doesn't — отрицание"
          ],
          examples: [
            "I go to school every day.",
            "She reads books in the evening.",
            "They don't like fish.",
            "Does he play football? — Yes, he does."
          ],
          facts: [
            "Present Simple — самое частое время в английском языке",
            "Окончание -s читается как [s], [z] или [ɪz]",
            "В British English часто используют 'have got' вместо 'have'"
          ],
          image: "/school-curriculum-app/images/lessons/grade-2/english/present-simple.svg"
        }
      ]
    },
    {
      topic: "Дни недели и месяцы",
      lessons: [
        {
          title: "Урок 12: Days of the week. Дни недели",
          description: "Названия дней недели по-английски",
          tasks: [
            "Обвести по контуру дни недели",
            "Найти буквы в словах: Monday, Friday, Sunday",
            "Составить из карточей неделю по порядку",
            "Дописать пропущенную букву: M_nday, Fr_day, S_nday"
          ],
          theory: "В неделе 7 дней. Дни недели по-английски пишутся с большой буквы: Monday (понедельник), Tuesday (вторник), Wednesday (среда), Thursday (четверг), Friday (пятница), Saturday (суббота), Sunday (воскресенье). На выходные — Saturday и Sunday. What day is it today? — Какой сегодня день? Today is Monday. — Сегодня понедельник.",
          content: "## Days of the week\n\n**Дни недели:**\n1. **Monday** — понедельник\n2. **Tuesday** — вторник\n3. **Wednesday** — среда\n4. **Thursday** — четверг\n5. **Friday** — пятница\n6. **Saturday** — суббота\n7. **Sunday** — воскресенье\n\n**Фразы:**\n- **What day is it today?** — Какой сегодня день?\n- **Today is Monday.** — Сегодня понедельник.\n- **I go to school on Monday.** — Я хожу в школу в понедельник.\n- **Weekend** — выходные (Saturday + Sunday)\n\n**Особенности:**\n- Дни недели всегда с большой буквы\n- Перед днём недели ставим **on**: on Monday\n- Wednesday читается [ˈwenzdeɪ] — без буквы d!",
          keyPoints: [
            "7 дней: Monday — Sunday",
            "Пишутся с большой буквы",
            "On Monday — в понедельник",
            "Weekend — выходные"
          ],
          examples: [
            "Today is Tuesday.",
            "I don't go to school on Sunday.",
            "My favourite day is Friday!"
          ],
          facts: [
            "Названия дней произошли от имён богов",
            "Wednesday — самый трудный для произношения день",
            "В некоторых странах неделя начинается с воскресенья"
          ],
          image: "/school-curriculum-app/images/lessons/grade-2/english/days-of-week.svg"
        },
        {
          title: "Урок 13: Months and seasons. Месяцы и времена года",
          description: "Названия месяцев и сезонов",
          tasks: [
            "Обвести по контуру месяцы: January, February, March",
            "Найти буквы в словах: season, spring, summer, winter",
            "Составить из карточек 12 месяцев по порядку",
            "Дописать пропущенную букву: Jan_ary, Febr_ary, M_rch"
          ],
          theory: "В году 12 месяцев и 4 сезона: spring (весна), summer (лето), autumn (осень), winter (зима). Месяцы: January, February, March, April, May, June, July, August, September, October, November, December. When is your birthday? — Когда твой день рождения? My birthday is in May. — Мой день рождения в мае.",
          content: "## Months and seasons\n\n**Времена года (seasons):**\n- **Spring**: March, April, May\n- **Summer**: June, July, August\n- **Autumn**: September, October, November\n- **Winter**: December, January, February\n\n**12 месяцев:**\n1. **January** — январь | 7. **July** — июль\n2. **February** — февраль | 8. **August** — август\n3. **March** — март | 9. **September** — сентябрь\n4. **April** — апрель | 10. **October** — октябрь\n5. **May** — май | 11. **November** — ноябрь\n6. **June** — июнь | 12. **December** — декабрь\n\n**Фразы:**\n- When is your birthday? — Когда твой день рождения?\n- My birthday is in May. — Мой день рождения в мае.\n- I like summer! — Я люблю лето!\n- In winter it snows. — Зимой идёт снег.",
          keyPoints: [
            "4 сезона: spring, summer, autumn, winter",
            "12 месяцев: January — December",
            "In May — в мае (предлог in)",
            "When is your birthday? — Когда день рождения?"
          ],
          examples: [
            "My birthday is in March.",
            "I like summer because it's hot.",
            "Winter is cold and snowy."
          ],
          facts: [
            "В американском английском 'autumn' называют 'fall'",
            "July и August названы в честь римских императоров",
            "February — самый короткий месяц (28 или 29 дней)"
          ],
          image: "/school-curriculum-app/images/lessons/grade-2/english/months-seasons.svg"
        }
      ]
    }
  ]
}
