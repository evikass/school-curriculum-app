import { Subject } from '../../types'

export const grade1English: Subject = {
  title: "Английский язык",
  icon: "Globe",
  color: "text-indigo-400",
  topics: [
    "Приветствие и знакомство",
    "Цвета и числа",
    "Моя семья",
    "Животные и еда"
  ],
  detailedTopics: [
    {
      topic: "Приветствие и знакомство",
      lessons: [
        {
          title: "Урок 1: Hello! Привет!",
          description: "Знакомство с приветствиями на английском языке",
          tasks: [
            "Обвести слово Hello по контуру",
            "Найти слово Hello среди других английских слов",
            "Составить диалог приветствия с карточками",
            "Разыграть сценку знакомства с одноклассником"
          ],
          theory: "Английский язык — один из самых распространённых языков мира. Приветствие — первое, что нужно уметь сказать. «Hello» [хэлоу] — здравствуйте, привет. «Hi» [хай] — привет (неформально). «Good morning» [гуд мОрнинг] — доброе утро. Английские слова произносятся не так, как пишутся, поэтому важно слушать и повторять.",
          content: "## Hello! Привет!\n\n**Hello!** [хэлоу] — здравствуйте, привет. Это самое распространённое приветствие в английском языке.\n\n**Hi!** [хай] — привет. Неформальное приветствие для друзей.\n\n**Good morning!** [гуд мОрнинг] — доброе утро.\n\n**Goodbye!** [гудбАй] — до свидания.\n\nПри знакомстве говорят: **My name is...** [май нэйм из] — Меня зовут...",
          keyPoints: [
            "Hello — здравствуйте, привет",
            "Hi — привет (неформально)",
            "Good morning — доброе утро",
            "My name is... — Меня зовут..."
          ],
          examples: [
            "Hello! My name is Anna.",
            "Hi! I am Peter.",
            "Good morning, teacher!"
          ],
          facts: [
            "Английский язык — родной для 400 миллионов людей",
            "Слово «hello» стало популярным после изобретения телефона",
            "В Англии принято здороваться даже с незнакомыми людьми"
          ],
          image: "/school-curriculum-app/images/lessons/grade-1/english/hello.svg"
        },
        {
          title: "Урок 2: How are you? Как дела?",
          description: "Умение спрашивать и отвечать о самочувствии",
          tasks: [
            "Обвести фразу How are you по точкам",
            "Найти правильный ответ к вопросу How are you?",
            "Разыграть диалог: приветствие + вопрос о делах",
            "Соединить фразу по-английски с переводом на русский"
          ],
          theory: "Вежливое общение на английском включает вопрос о делах и самочувствии. «How are you?» [хау а ю] — Как дела? Типичные ответы: «I am fine» [ай эм файн] — Я в порядке, «I am good» — У меня всё хорошо, «Not bad» — Неплохо. После ответа принято спросить: «And you?» [энд ю] — А у тебя?",
          content: "## How are you? Как дела?\n\n**How are you?** [хау а ю] — Как дела? Как поживаете?\n\nОтветы:\n- **I am fine.** [ай эм файн] — Я в порядке.\n- **I am good.** [ай эм гуд] — У меня всё хорошо.\n- **Not bad.** [нот бэд] — Неплохо.\n- **And you?** [энд ю] — А у тебя?\n\nВежливая беседа: Hello! → How are you? → I am fine, and you? → I am good too.",
          keyPoints: [
            "How are you? — Как дела?",
            "I am fine — Я в порядке",
            "And you? — А у тебя?",
            "Вежливость — важная часть английского общения"
          ],
          examples: [
            "— How are you? — I am fine, thank you!",
            "— How are you? — Not bad, and you?",
            "— Hello! How are you? — I am good!"
          ],
          facts: [
            "Англичане спрашивают «How are you?» даже у незнакомых",
            "Обычно не ожидают подробного рассказа о делах",
            "Фраза «How do you do?» — более формальное приветствие"
          ],
          image: "/school-curriculum-app/images/lessons/grade-1/english/how-are-you.svg"
        },
        {
          title: "Урок 3: What is your name? Как тебя зовут?",
          description: "Знакомство: вопрос и ответ об имени",
          tasks: [
            "Обвести фразу What is your name по контуру",
            "Составить диалог знакомства двух персонажей",
            "Найти имя на карточке и назвать его по-английски",
            "Представить себя: My name is..."
          ],
          theory: "Для знакомства на английском нужно уметь спросить имя и назвать своё. «What is your name?» [вот из ё нэйм] — Как тебя зовут? Ответ: «My name is...» [май нэйм из] — Меня зовут... Или короче: «I am...» [ай эм] — Я... Английские имена: John, Mary, Tom, Ann, Peter, Kate.",
          content: "## What is your name? Как тебя зовут?\n\n**What is your name?** [вот из ё нэйм] — Как тебя зовут?\n\nОтветы:\n- **My name is Anna.** [май нэйм из Анна] — Меня зовут Анна.\n- **I am Tom.** [ай эм Том] — Я Том.\n\nПопулярные английские имена: **John** [Джон], **Mary** [Мэри], **Tom** [Том], **Ann** [Энн], **Peter** [Питер], **Kate** [Кейт].\n\nДиалог знакомства: Hello! → What is your name? → My name is... → Nice to meet you!",
          keyPoints: [
            "What is your name? — Как тебя зовут?",
            "My name is... — Меня зовут...",
            "I am... — Я...",
            "Nice to meet you! — Приятно познакомиться!"
          ],
          examples: [
            "— What is your name? — My name is Kate.",
            "— I am John. Nice to meet you!",
            "— Hello! My name is Ann. What is your name?"
          ],
          facts: [
            "Самое популярное мужское имя в Англии — Oliver",
            "Самое популярное женское имя — Olivia",
            "В Англии детей часто называют в честь родственников"
          ],
          image: "/school-curriculum-app/images/lessons/grade-1/english/what-is-your-name.svg"
        }
      ]
    },
    {
      topic: "Цвета и числа",
      lessons: [
        {
          title: "Урок 4: Colours — Цвета",
          description: "Знакомство с названиями цветов на английском языке",
          tasks: [
            "Обвести слова-цвета по контуру",
            "Раскрасить предмет нужным цветом по инструкции",
            "Найти предмет заданного цвета на картинке",
            "Соединить английское слово с нужным цветом"
          ],
          theory: "Цвета на английском: red [рэд] — красный, blue [блу] — синий, green [грин] — зелёный, yellow [йэлоу] — жёлтый, orange [Ориндж] — оранжевый, pink [пинк] — розовый, white [уайт] — белый, black [блэк] — чёрный. Чтобы сказать «это красный», говорят: «It is red» [ит из рэд].",
          content: "## Colours — Цвета\n\nОсновные цвета на английском:\n- **Red** [рэд] — красный\n- **Blue** [блу] — синий\n- **Green** [грин] — зелёный\n- **Yellow** [йэлоу] — жёлтый\n- **Orange** [Ориндж] — оранжевый\n- **Pink** [пинк] — розовый\n- **White** [уайт] — белый\n- **Black** [блэк] — чёрный\n\nКонструкция: **It is red.** — Это красный. **The apple is red.** — Яблоко красное.",
          keyPoints: [
            "Red — красный, Blue — синий, Green — зелёный",
            "Yellow — жёлтый, Orange — оранжевый",
            "It is + цвет — это (какой-то) цвет",
            "Названия цветов — самые частые прилагательные"
          ],
          examples: [
            "The sun is yellow. — Солнце жёлтое.",
            "The grass is green. — Трава зелёная.",
            "My pen is blue. — Моя ручка синяя."
          ],
          facts: [
            "Слово «orange» означает и цвет, и фрукт",
            "В английском есть слово «purple» [пёрпл] — фиолетовый",
            "Светофор: red — стой, green — иди"
          ],
          image: "/school-curriculum-app/images/lessons/grade-1/english/colours.svg"
        },
        {
          title: "Урок 5: Numbers 1-10 — Числа",
          description: "Счёт от 1 до 10 на английском языке",
          tasks: [
            "Обвести числа по точкам: one, two, three...",
            "Показать нужное количество пальцев и назвать число",
            "Найти число на карточке и назвать его по-английски",
            "Сосчитать предметы на картинке по-английски"
          ],
          theory: "Числа от 1 до 10 на английском: one [уан], two [ту], three [сри], four [фо], five [файв], six [сикс], seven [сэвн], eight [эйт], nine [найн], ten [тэн]. Английские числа нужно выучить наизусть — они основа для дальнейшего счёта. Обратите внимание: два пишется two, а не too или to.",
          content: "## Numbers 1-10 — Числа\n\nСчитаем по-английски:\n- **1** — one [уан]\n- **2** — two [ту]\n- **3** — three [сри]\n- **4** — four [фо]\n- **5** — five [файв]\n- **6** — six [сикс]\n- **7** — seven [сэвн]\n- **8** — eight [эйт]\n- **9** — nine [найн]\n- **10** — ten [тэн]\n\nКонструкция: **How many?** [хау мЭни] — Сколько? — **Three cats.** — Три кошки.",
          keyPoints: [
            "One, two, three — первые три числа",
            "Four, five — средние числа",
            "Six, seven, eight, nine, ten — старшие числа",
            "How many? — Сколько?"
          ],
          examples: [
            "One apple, two bananas, three oranges",
            "I have five pencils. — У меня 5 карандашей.",
            "How many cats? — Three cats."
          ],
          facts: [
            "Слово «two» произносится так же, как «too» и «to»",
            "Слово «eight» начинается с немой буквы e",
            "Английские числа — основа для чисел до 100"
          ],
          image: "/school-curriculum-app/images/lessons/grade-1/english/numbers.svg"
        }
      ]
    },
    {
      topic: "Моя семья",
      lessons: [
        {
          title: "Урок 6: My family — Моя семья",
          description: "Названия членов семьи на английском языке",
          tasks: [
            "Обвести слова: mother, father, sister, brother по контуру",
            "Найти на семейном фото нужного члена семьи",
            "Составить фразу: This is my mother",
            "Нарисовать свою семью и подписать по-английски"
          ],
          theory: "Члены семьи на английском: mother [мАзэр] / mom [мам] — мама, father [фАзэр] / dad [дэд] — папа, sister [сИстэр] — сестра, brother [брАзэр] — брат, grandmother [грэндмАзэр] / grandma [грэндма] — бабушка, grandfather [грэндфАзэр] / grandpa [грэндпа] — дедушка. «This is my...» [зис из май] — Это мой/моя...",
          content: "## My family — Моя семья\n\nЧлены семьи на английском:\n- **Mother / Mom** [мАзэр / мам] — мама\n- **Father / Dad** [фАзэр / дэд] — папа\n- **Sister** [сИстэр] — сестра\n- **Brother** [брАзэр] — брат\n- **Grandmother / Grandma** [грэндма] — бабушка\n- **Grandfather / Grandpa** [грэндпа] — дедушка\n\nКонструкция: **This is my mother.** — Это моя мама. **I love my family.** — Я люблю свою семью.",
          keyPoints: [
            "Mother/Mom — мама, Father/Dad — папа",
            "Sister — сестра, Brother — брат",
            "Grandma — бабушка, Grandpa — дедушка",
            "This is my... — Это мой/моя..."
          ],
          examples: [
            "This is my mom. Her name is Olga.",
            "This is my dad. His name is Ivan.",
            "I have a sister and a brother."
          ],
          facts: [
            "Слово «family» произошло от латинского «familia»",
            "В Англии принято называть маму «mum» или «mummy»",
            "Слово «parents» [пЭрэнтс] означает «родители»"
          ],
          image: "/school-curriculum-app/images/lessons/grade-1/english/my-family.svg"
        }
      ]
    },
    {
      topic: "Животные и еда",
      lessons: [
        {
          title: "Урок 7: Animals — Животные",
          description: "Названия животных на английском языке",
          tasks: [
            "Обвести названия животных по контуру",
            "Найти животное на картинке и назвать его по-английски",
            "Соединить животное с его названием",
            "Составить фразу: It is a cat"
          ],
          theory: "Животные на английском: cat [кэт] — кошка, dog [дог] — собака, bird [бёрд] — птица, fish [фиш] — рыба, frog [фрог] — лягушка, monkey [мАнки] — обезьяна, bear [бэр] — медведь, elephant [Элифант] — слон. «It is a...» [ит из э] — Это... Английские слова для животных часто короткие и легко запоминаются.",
          content: "## Animals — Животные\n\nЖивотные на английском:\n- **Cat** [кэт] — кошка\n- **Dog** [дог] — собака\n- **Bird** [бёрд] — птица\n- **Fish** [фиш] — рыба\n- **Frog** [фрог] — лягушка\n- **Monkey** [мАнки] — обезьяна\n- **Bear** [бэр] — медведь\n- **Elephant** [Элифант] — слон\n\nКонструкция: **It is a cat.** — Это кошка. **I like dogs.** — Я люблю собак.",
          keyPoints: [
            "Cat — кошка, Dog — собака",
            "Bird — птица, Fish — рыба",
            "It is a... — Это...",
            "I like... — Я люблю..."
          ],
          examples: [
            "It is a cat. The cat is black.",
            "I like dogs. Dogs are smart.",
            "The elephant is big. The frog is small."
          ],
          facts: [
            "Самое популярное домашнее животное в Англии — кошка",
            "Слово «pet» [пэт] означает «домашнее животное»",
            "В Лондонском зоопарке более 750 видов животных"
          ],
          image: "/school-curriculum-app/images/lessons/grade-1/english/animals.svg"
        },
        {
          title: "Урок 8: Food — Еда",
          description: "Названия продуктов питания на английском языке",
          tasks: [
            "Обвести слова: apple, banana, bread по точкам",
            "Найти продукт на картинке и назвать по-английски",
            "Соединить продукт с его названием",
            "Составить фразу: I like apples"
          ],
          theory: "Еда на английском: apple [Эпл] — яблоко, banana [бэнАна] — банан, bread [брэд] — хлеб, milk [милк] — молоко, water [вОтэр] — вода, cake [кэйк] — торт, egg [эг] — яйцо, cheese [чиз] — сыр. «I like...» [ай лайк] — Я люблю... «I don't like...» [ай донт лайк] — Я не люблю...",
          content: "## Food — Еда\n\nПродукты на английском:\n- **Apple** [Эпл] — яблоко\n- **Banana** [бэнАна] — банан\n- **Bread** [брэд] — хлеб\n- **Milk** [милк] — молоко\n- **Water** [вОтэр] — вода\n- **Cake** [кэйк] — торт\n- **Egg** [эг] — яйцо\n- **Cheese** [чиз] — сыр\n\nКонструкция: **I like apples.** — Я люблю яблоки. **I don't like cheese.** — Я не люблю сыр.",
          keyPoints: [
            "Apple — яблоко, Banana — банан",
            "Bread — хлеб, Milk — молоко",
            "I like... — Я люблю...",
            "I don't like... — Я не люблю..."
          ],
          examples: [
            "I like bananas and milk.",
            "I don't like cheese.",
            "Give me water, please."
          ],
          facts: [
            "Англичане любят пить чай с молоком",
            "Самый популярный английский завтрак — eggs and bacon",
            "Слово «breakfast» [брэкфаст] означает «завтрак»"
          ],
          image: "/school-curriculum-app/images/lessons/grade-1/english/food.svg"
        }
      ]
    }
  ]
}
