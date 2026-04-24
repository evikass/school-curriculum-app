import { Subject } from '../../types'

export const grade3English: Subject = {
  title: "Иностранный язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: ["Animals and Pets", "School and Classroom", "Seasons and Weather", "Numbers and Counting"],
  detailedTopics: [
    {
      topic: "Animals and Pets",
      lessons: [
        {
          title: "Урок 1: Wild Animals",
          description: "Изучение названий диких животных на английском языке. Учимся описывать животных и говорить о том, что они умеют.",
          tasks: [
            "Выучи названия 8 диких животных на английском",
            "Составь 3 предложения по модели: A bear can ___",
            "Опиши любимое дикое животное на английском (3 предложения)",
            "Разгадай кроссворд с названиями животных"
          ],
          theory: "Дикие животные по-английски называются wild animals. Каждое животное имеет свои особенности: медведь умеет плавать, обезьяна умеет лазить по деревьям, а змея ползать. Для описания животных мы используем конструкцию can (мочь, уметь) в утвердительных и отрицательных предложениях: A tiger can run. A penguin can't fly.",
          content: "## Wild Animals\n\n### Названия диких животных\n\n| Английский | Русский | Английский | Русский |\n|---|---|---|---|\n| bear | медведь | wolf | волк |\n| tiger | тигр | fox | лиса |\n| elephant | слон | deer | олень |\n| monkey | обезьяна | snake | змея |\n\n### Конструкция can / can't\n\n**Утверждение:** A bear **can** swim.\n**Отрицание:** A bear **can't** fly.\n**Вопрос:** **Can** a bear swim? — Yes, it can.\n\n### Описание животного\n\n1. Это животное: **It is a…**\n2. Оно умеет: **It can…**\n3. Оно не умеет: **It can't…**\n\n### Пример описания\n\n> It is a tiger. It is big and orange. It can run and swim. It can't fly.",
          keyPoints: [
            "Wild animals — дикие животные",
            "Конструкция can означает «мочь, уметь»",
            "Can't — отрицательная форма (не умеет)",
            "Для описания используем: It is a… / It can… / It can't…"
          ],
          examples: [
            "A monkey can climb trees. — Обезьяна умеет лазить по деревьям",
            "An elephant can't jump. — Слон не умеет прыгать",
            "A tiger can run fast. — Тигр умеет быстро бегать"
          ],
          facts: [
            "Тигры — самые большие дикие кошки в мире",
            "Слоны — единственные животные, которые не умеют прыгать",
            "Дельфины спят с одним открытым глазом"
          ],
          image: "/school-curriculum-app/images/lessons/grade-3/english/wild-animals.svg"
        },
        {
          title: "Урок 2: Pets",
          description: "Изучение названий домашних питомцев на английском. Учимся говорить о своих питомцах и спрашивать о чужих.",
          tasks: [
            "Выучи названия 8 домашних питомцев",
            "Составь диалог: расспроси друга о его питомце",
            "Напиши 4 предложения о своём питомце (или о питомце, которого хотел бы завести)",
            "Спроси одноклассника: Have you got a pet?"
          ],
          theory: "Домашние питомцы по-английски называются pets. Чтобы спросить, есть ли у кого-то питомец, мы используем вопрос: Have you got a pet? Чтобы ответить, говорим: Yes, I have или No, I haven't. Для описания питомца используем прилагательные: big, small, funny, cute, kind. Множественное число существительных образуется добавлением -s: cat — cats, dog — dogs.",
          content: "## Pets\n\n### Названия домашних питомцев\n\n| Английский | Русский | Английский | Русский |\n|---|---|---|---|\n| cat | кошка | dog | собака |\n| hamster | хомяк | parrot | попугай |\n| rabbit | кролик | fish | рыбка |\n| guinea pig | морская свинка | turtle | черепаха |\n\n### Вопрос о питомце\n\n— **Have you got a pet?**\n— **Yes, I have. I've got a cat.**\n— **No, I haven't.**\n\n### Прилагательные для описания\n\n| Английский | Русский | Английский | Русский |\n|---|---|---|---|\n| big | большой | small | маленький |\n| funny | смешной | cute | милый |\n| kind | добрый | brave | храбрый |\n\n### Множественное число\n\ncat → cats, dog → dogs, fish → fish (не меняется!)",
          keyPoints: [
            "Pets — домашние питомцы",
            "Have you got a pet? — вопрос о наличии питомца",
            "Yes, I have / No, I haven't — ответы",
            "Множественное число образуется добавлением -s"
          ],
          examples: [
            "I've got a cat. Her name is Murka. She is funny and cute.",
            "Have you got a dog? — Yes, I have. His name is Rex.",
            "My hamster is small and funny. It can run and jump."
          ],
          facts: [
            "Cats are the most popular pets in the world — кошки — самые популярные питомцы",
            "Dogs can understand about 250 words — собаки понимают около 250 слов",
            "Parrots can learn to say words — попугаи могут научиться говорить"
          ],
          image: "/school-curriculum-app/images/lessons/grade-3/english/pets.svg"
        }
      ]
    },
    {
      topic: "School and Classroom",
      lessons: [
        {
          title: "Урок 1: School Things",
          description: "Изучение названий школьных принадлежностей на английском языке. Учимся говорить, что у нас есть и чего нет.",
          tasks: [
            "Выучи названия 10 школьных принадлежностей",
            "Составь 5 предложений: I have got a ___",
            "Спроси соседа: Have you got a pen?",
            "Найди на картинке и назови все школьные предметы"
          ],
          theory: "Школьные принадлежности по-английски называются school things или school supplies. Чтобы сказать, что у тебя есть что-то, используем: I have got a pen. Чтобы сказать, что у тебя этого нет: I haven't got a ruler. Неопределённый артикль a/an используется перед исчисляемыми существительными в единственном числе: a pen, an eraser (перед гласной — an).",
          content: "## School Things\n\n### Названия школьных принадлежностей\n\n| Английский | Русский | Английский | Русский |\n|---|---|---|---|\n| pen | ручка | pencil | карандаш |\n| ruler | линейка | eraser | ластик |\n| book | книга | notebook | тетрадь |\n| bag | рюкзак | pencil case | пенал |\n| desk | парта | board | доска |\n\n### Артикли a / an\n\n- **a** — перед согласной: a pen, a book, a ruler\n- **an** — перед гласной: an eraser, an English book\n\n### Конструкция have got\n\n✅ I **have got** a pen. — У меня есть ручка.\n❌ I **haven't got** a ruler. — У меня нет линейки.\n❓ **Have you got** a book? — У тебя есть книга?\n✅ Yes, I have. / No, I haven't.",
          keyPoints: [
            "School things — школьные принадлежности",
            "I have got — у меня есть",
            "I haven't got — у меня нет",
            "Артикль a перед согласной, an перед гласной"
          ],
          examples: [
            "I have got a pencil and an eraser in my pencil case.",
            "Have you got a ruler? — Yes, I have. It's in my bag.",
            "I haven't got a red pen. Can you give me one?"
          ],
          facts: [
            "В Великобритании школьники носят форму — school uniform",
            "Pencil в переводе означает «маленький хвост» (от латинского)",
            "Первые ластики делали из хлебного мякиша"
          ],
          image: "/school-curriculum-app/images/lessons/grade-3/english/school-things.svg"
        },
        {
          title: "Урок 2: My Classroom",
          description: "Изучение названий предметов в классе и предлогов места. Учимся описывать расположение вещей в классе.",
          tasks: [
            "Выучи названия предметов в классе",
            "Составь 4 предложения с предлогами: in, on, under, next to",
            "Опиши свой класс на английском (5 предложений)",
            "Спроси: Where is the book? И ответь с предлогом"
          ],
          theory: "Для описания расположения предметов используем вопрос Where is…? и предлоги места: in (в), on (на), under (под), next to (рядом с), behind (за), in front of (перед). Классная комната по-английски — classroom. В классе есть доска (board), парты (desks), стулья (chairs), шкаф (cupboard), окно (window), дверь (door).",
          content: "## My Classroom\n\n### Предметы в классе\n\n| Английский | Русский | Английский | Русский |\n|---|---|---|---|\n| board | доска | desk | парта |\n| chair | стул | cupboard | шкаф |\n| window | окно | door | дверь |\n| wall | стена | floor | пол |\n| bookshelf | книжная полка | computer | компьютер |\n\n### Предлоги места\n\n| Предлог | Русский | Пример |\n|---|---|---|\n| in | в | The pen is **in** the bag |\n| on | на | The book is **on** the desk |\n| under | под | The cat is **under** the desk |\n| next to | рядом с | The chair is **next to** the desk |\n| behind | за | The bag is **behind** the door |\n\n### Вопрос Where is…?\n\n— **Where is** the book?\n— It is **on** the desk.\n\n— **Where are** the pencils?\n— They are **in** the pencil case.",
          keyPoints: [
            "Where is…? — Где…? (для одного предмета)",
            "Where are…? — Где…? (для нескольких предметов)",
            "Предлоги: in, on, under, next to, behind",
            "Classroom — классная комната"
          ],
          examples: [
            "The board is on the wall. — Доска на стене",
            "The bag is under the desk. — Рюкзак под партой",
            "The computer is next to the window. — Компьютер рядом с окном"
          ],
          facts: [
            "В английских школах ученики называют учителя Mr/Miss + фамилия",
            "В Англии учебный год начинается в сентябре и делится на 3 триместра",
            "Английские школьники обедают в school canteen (столовая)"
          ],
          image: "/school-curriculum-app/images/lessons/grade-3/english/classroom.svg"
        }
      ]
    },
    {
      topic: "Seasons and Weather",
      lessons: [
        {
          title: "Урок 1: The Four Seasons",
          description: "Изучение времён года и месяцев на английском языке. Учимся говорить о любимом времени года.",
          tasks: [
            "Выучи названия 4 времён года и 12 месяцев",
            "Составь 3 предложения: I like ___ because ___",
            "Опиши любое время года (4 предложения)",
            "Ответь на вопрос: What is your favourite season?"
          ],
          theory: "Времена года по-английски: spring (весна), summer (лето), autumn (осень), winter (зима). Каждый сезон имеет свои особенности: весной распускаются листья, летом тепло и солнечно, осенью листья падают, зимой идёт снег. Чтобы сказать, какое время года ты любишь: My favourite season is summer. Чтобы объяснить почему: I like summer because I can swim.",
          content: "## The Four Seasons\n\n### Времена года и месяцы\n\n| Сезон | Месяцы | Погода |\n|---|---|---|\n| Spring | March, April, May | Warm, rainy |\n| Summer | June, July, August | Hot, sunny |\n| Autumn | September, October, November | Cool, windy |\n| Winter | December, January, February | Cold, snowy |\n\n### Конструкция I like… because…\n\n- I like **spring** because flowers bloom.\n- I like **summer** because I can swim.\n- I like **autumn** because leaves are beautiful.\n- I like **winter** because I can ski.\n\n### Мой любимый сезон\n\n— What is your favourite season?\n— My favourite season is summer. I like summer because it is hot and sunny. I can swim and play outside.",
          keyPoints: [
            "4 сезона: spring, summer, autumn, winter",
            "12 месяцев: January–December",
            "My favourite season is… — Моё любимое время года…",
            "I like… because… — Я люблю… потому что…"
          ],
          examples: [
            "My favourite season is winter. I like winter because I can ski and play snowballs.",
            "In spring the weather is warm and rainy. Trees are green.",
            "In autumn leaves are yellow and red. It is cool and windy."
          ],
          facts: [
            "В Австралии зимой — наше лето, и наоборот",
            "Слово autumn используется в британском английском, а fall — в американском",
            "Июнь — самый длинный день в году в Северном полушарии"
          ],
          image: "/school-curriculum-app/images/lessons/grade-3/english/seasons.svg"
        },
        {
          title: "Урок 2: Weather",
          description: "Изучение лексики для описания погоды на английском. Учимся говорить о погоде сегодня и спрашивать о ней.",
          tasks: [
            "Выучи 8 слов для описания погоды",
            "Посмотри в окно и опиши погоду на английском",
            "Составь диалог о погоде с одноклассником",
            "Нарисуй 4 вида погоды и подпши по-английски"
          ],
          theory: "Погода по-английски — weather. Чтобы сказать, какая погода, используем: It is + прилагательное: It is sunny. It is rainy. It is cold. Чтобы спросить о погоде: What is the weather like today? Погода бывает разной: sunny (солнечно), cloudy (облачно), rainy (дождливо), snowy (снежно), windy (ветрено), foggy (туманно), hot (жарко), cold (холодно).",
          content: "## Weather\n\n### Слова для описания погоды\n\n| Английский | Русский | Английский | Русский |\n|---|---|---|---|\n| sunny | солнечно | cloudy | облачно |\n| rainy | дождливо | snowy | снежно |\n| windy | ветрено | foggy | туманно |\n| hot | жарко | cold | холодно |\n| warm | тепло | cool | прохладно |\n\n### Как говорить о погоде\n\n— **What is the weather like today?**\n— **It is sunny and warm.**\n— **Is it cold in winter?**\n— **Yes, it is. It is cold and snowy.**\n\n### Описание погоды по сезонам\n\n- **Spring:** It is warm and rainy. The sun shines.\n- **Summer:** It is hot and sunny. There are no clouds.\n- **Autumn:** It is cool and windy. It is often rainy.\n- **Winter:** It is cold and snowy. The wind blows.",
          keyPoints: [
            "Weather — погода",
            "What is the weather like? — Какая погода?",
            "It is sunny/rainy/cold — Солнечно/дождливо/холодно",
            "Is it…? — вопрос о погоде"
          ],
          examples: [
            "It is sunny and hot today. Let's go to the park!",
            "It is rainy and windy. Take your umbrella!",
            "What is the weather like? — It is cloudy and cool."
          ],
          facts: [
            "В Лондоне около 160 дождливых дней в году — поэтому зонт нужен всегда",
            "Самое жаркое место на Земле — Долина Смерти в США (+56°C)",
            "Самый сильный снегопад за год выпал в США — 31 метр снега!"
          ],
          image: "/school-curriculum-app/images/lessons/grade-3/english/weather.svg"
        }
      ]
    },
    {
      topic: "Numbers and Counting",
      lessons: [
        {
          title: "Урок 1: Numbers 1–20",
          description: "Изучение чисел от 1 до 20 на английском. Учимся считать, называть возраст и номер.",
          tasks: [
            "Посчитай от 1 до 20 вслух",
            "Напиши числа цифрами и словами: 7, 13, 15, 20",
            "Спроси соседа: How old are you? И ответь",
            "Реши 5 примеров на английском: 5 + 3 = ?"
          ],
          theory: "Числа от 1 до 20 — основа для счёта на английском. Числа 1–12 нужно запомнить, а 13–19 образуются добавлением -teen к основе: six→sixteen. Число 20 — twenty. Чтобы назвать возраст, говорим: I am nine (years old). Чтобы спросить возраст: How old are you? Для арифметических действий: plus (+), minus (−), equals (=).",
          content: "## Numbers 1–20\n\n### Числа от 1 до 20\n\n| Число | Английский | Число | Английский |\n|---|---|---|---|\n| 1 | one | 11 | eleven |\n| 2 | two | 12 | twelve |\n| 3 | three | 13 | thirteen |\n| 4 | four | 14 | fourteen |\n| 5 | five | 15 | fifteen |\n| 6 | six | 16 | sixteen |\n| 7 | seven | 17 | seventeen |\n| 8 | eight | 18 | eighteen |\n| 9 | nine | 19 | nineteen |\n| 10 | ten | 20 | twenty |\n\n### Возраст\n\n— **How old are you?**\n— **I am nine.** (Мне 9 лет)\n\n### Арифметика\n\n- **Five plus three equals eight.** (5 + 3 = 8)\n- **Ten minus four equals six.** (10 − 4 = 6)\n- **Two plus seven equals nine.** (2 + 7 = 9)",
          keyPoints: [
            "Числа 1–12 нужно запомнить",
            "Числа 13–19 образуются с суффиксом -teen",
            "How old are you? — Сколько тебе лет?",
            "Plus (+), minus (−), equals (=)"
          ],
          examples: [
            "I am nine years old. — Мне 9 лет",
            "Seven plus five equals twelve. (7 + 5 = 12)",
            "There are fifteen desks in our classroom. — В нашем классе 15 парт"
          ],
          facts: [
            "Число 13 считается несчастливым в английской культуре — triskaidekaphobia",
            "В некоторых отелях нет 13-го этажа",
            "Слово teenager (подросток) происходит от суффикса -teen (13–19 лет)"
          ],
          image: "/school-curriculum-app/images/lessons/grade-3/english/numbers.svg"
        },
        {
          title: "Урок 2: Numbers 20–100 and Telling Time",
          description: "Изучение десятков от 20 до 100 и времени на английском. Учимся называть время и цены.",
          tasks: [
            "Посчитай десятками от 20 до 100",
            "Назови время: 3:00, 5:30, 7:15",
            "Прочитай цены: 25p, 50p, 99p",
            "Составь 3 вопроса: What time is it?"
          ],
          theory: "Десятки образуются добавлением -ty к основе: six→sixty. Числа между десятками образуются сложением: twenty-one, thirty-five. Для называния времени используем: What time is it? It is three o'clock. It is half past five. Для цен используем: How much is it? It is fifty pence (50p). Важно правильно произносить -teen (ударение на суффикс) и -ty (ударение на первый слог).",
          content: "## Numbers 20–100 and Telling Time\n\n### Десятки\n\n| Число | Английский | Число | Английский |\n|---|---|---|---|\n| 20 | twenty | 60 | sixty |\n| 30 | thirty | 70 | seventy |\n| 40 | forty | 80 | eighty |\n| 50 | fifty | 90 | ninety |\n| 100 | one hundred | | |\n\n### Время\n\n— **What time is it?**\n— **It is three o'clock.** (3:00)\n— **It is half past five.** (5:30)\n— **It is quarter past seven.** (7:15)\n\n### Цены\n\n— **How much is it?**\n— **It is twenty-five pence.** (25p)\n— **It is one pound fifty.** (£1.50)\n\n### Разница -teen и -ty\n\n- thir**teen** (13) — ударение на **teen**\n- thir**ty** (30) — ударение на **thir**",
          keyPoints: [
            "Десятки образуются с суффиксом -ty",
            "What time is it? — Который час?",
            "It is three o'clock — Сейчас три часа",
            "How much is it? — Сколько это стоит?"
          ],
          examples: [
            "It is half past nine. — Сейчас половина десятого (9:30)",
            "There are one hundred centimetres in a metre. — В метре 100 сантиметров",
            "How much is the book? — It is two pounds fifty. (£2.50)"
          ],
          facts: [
            "В Англии используют фунты стерлингов (£) и пенсы (p)",
            "1 фунт = 100 пенсов",
            "На знаменитой башне Биг-Бен в Лондоне — часы, которые показывают точное время с 1859 года"
          ],
          image: "/school-curriculum-app/images/lessons/grade-3/english/time.svg"
        }
      ]
    }
  ]
}
