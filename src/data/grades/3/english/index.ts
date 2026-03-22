import { SubjectData, GameLesson } from '@/data/types'

const L = (title: string, description: string, tasks: string[]) => ({ title, description, tasks, theory: description })

export const lessons: SubjectData = {
  title: "Иностранный язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: ["Alphabet", "Numbers", "Colors", "Family", "Animals", "Food", "Daily routine"],
  detailedTopics: [
    {
      topic: "Alphabet and Sounds",
      lessons: [
        {
          title: "Урок 1: English Alphabet",
          description: `**Английский алфавит**

Английский алфавит состоит из 26 букв. Он называется латинским алфавитом.

**Буквы английского алфавита:**

**Гласные буквы (5):** A, E, I, O, U
**Согласные буквы (21):** B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z

**Алфавит по порядку:**

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

**Произношение букв:**

- A [эй] — apple (яблоко)
- B [би] — book (книга)
- C [си] — cat (кошка)
- D [ди] — dog (собака)
- E [и] — egg (яйцо)
- F [эф] — fish (рыба)
- G [джи] — girl (девочка)
- H [эйч] — house (дом)
- I [ай] — ice (лёд)
- J [джей] — jam (джем)
- K [кей] — kite (воздушный змей)
- L [эл] — lion (лев)
- M [эм] — mother (мама)
- N [эн] — nose (нос)
- O [оу] — orange (апельсин)
- P [пи] — pen (ручка)
- Q [кью] — queen (королева)
- R [ар] — red (красный)
- S [эс] — sun (солнце)
- T [ти] — tree (дерево)
- U [ю] — umbrella (зонт)
- V [ви] — violin (скрипка)
- W [дабл-ю] — water (вода)
- X [экс] — box (коробка)
- Y [уай] — yellow (жёлтый)
- Z [зед] — zoo (зоопарк)

**Песенка ABC:**

A-B-C-D-E-F-G
H-I-J-K-L-M-N-O-P
Q-R-S, T-U-V
W-X, Y and Z
Now I know my ABCs,
Next time won't you sing with me?

**Важные правила:**
- В английском языке 26 букв, но 44 звука
- Одна буква может читаться по-разному
- Y иногда работает как гласная`,
          tasks: [
            "Выучить все 26 букв",
            "Спеть песенку ABC",
            "Запомнить порядок букв",
            "Назвать буквы вразброс"
          ]
        },
        {
          title: "Урок 2: Vowels and Consonants",
          description: `**Гласные и согласные буквы**

В английском языке буквы делятся на гласные и согласные.

**Гласные буквы (Vowels):**

A, E, I, O, U — это 5 гласных букв.

**Особенности гласных:**
- Гласные звуки образуются без преград
- Воздух свободно проходит через рот
- Гласные можно пропевать

**Долгие и краткие звуки:**

**A:**
- Долгий [эй] — name, cake, late
- Краткий [э] — cat, hat, map

**E:**
- Долгий [и] — me, he, she
- Краткий [э] — pen, bed, red

**I:**
- Долгий [ай] — time, like, five
- Краткий [и] — sit, big, pig

**O:**
- Долгий [оу] — home, go, no
- Краткий [о] — dog, hot, box

**U:**
- Долгий [ю] — student, music, use
- Краткий [а] — sun, cup, bus

**Y как гласная:**
Буква Y иногда работает как гласная:
- В конце слова: happy, family, baby [и]
- В середине слова: my, fly, sky [ай]

**Согласные буквы (Consonants):**

B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z

**Особенности согласных:**
- При произнесении воздух встречает преграду
- Согласные нельзя пропевать

**Звонкие и глухие согласные:**

Звонкие (voiced): B, D, G, V, Z, L, M, N, R
Глухие (voiceless): P, T, K, F, S, H

**Парные согласные:**
- P — B (pin — bin)
- T — D (ten — den)
- K — G (cat — gate)
- F — V (fine — vine)
- S — Z (sea — zoo)`,
          tasks: [
            "Назвать 5 гласных букв",
            "Разделить буквы на гласные и согласные",
            "Произнести долгие и краткие звуки",
            "Определить тип буквы"
          ]
        },
        {
          title: "Урок 3: Reading Rules",
          description: `**Правила чтения в английском языке**

В английском языке буквы читаются по-разному в зависимости от положения в слове.

**Открытый слог (Open Syllable):**

Открытый слог заканчивается на гласную букву. Гласная читается как в алфавите.

**Примеры:**
- **A** — name [нейм], cake [кейк], lake [лейк]
- **E** — me [ми], he [хи], be [би]
- **I** — time [тайм], like [лайк], five [файв]
- **O** — home [хоум], no [ноу], go [гоу]
- **U** — student [стьюдент], music [мьюзик], use [ьюз]

**Признак открытого слога:**
- Слова заканчиваются на гласную: go, me, no
- После гласной стоит одна согласная + e (немая): name, like, home

**Закрытый слог (Closed Syllable):**

Закрытый слог заканчивается на согласную. Гласная читается кратко.

**Примеры:**
- **A** — cat [кэт], hat [хэт], map [мэп]
- **E** — pen [пэн], bed [бэд], red [рэд]
- **I** — sit [сит], big [биг], pig [пиг]
- **O** — dog [дог], hot [хот], box [бокс]
- **U** — sun [сан], cup [кап], bus [бас]

**Признак закрытого слога:**
- Слова заканчиваются на согласную: cat, pen, sit
- После гласной стоит одна или несколько согласных

**Правило «Magic E» (Магическая E):**

Если в конце слова стоит немая E, она делает гласную долгой:
- hat → hate (шляпа → ненавидеть)
- kit → kite (набор → воздушный змей)
- hop → hope (прыгать → надеяться)
- cut → cute (резать → милый)
- bit → bite (кусочек → кусать)

**Буквосочетания:**

**SH** [ш] — she, ship, shop, sheep
**CH** [ч] — cheese, chair, child, church
**TH** [с/з] — this, that, the, they
**PH** [ф] — phone, photo, elephant
**WH** [в] — what, where, when, white
**NG** [нг] — sing, ring, king, long
**NK** [нгк] — pink, ink, drink, think`,
          tasks: [
            "Открытый слог: name, like, home",
            "Закрытый слог: cat, pen, sit",
            "Правило Magic E: hat → hate",
            "Прочитать слова по правилам"
          ]
        },
        {
          title: "Урок 4: Common Words",
          description: `**Самые частые слова английского языка**

Эти слова встречаются в текстах чаще всего. Их нужно знать наизусть.

**Топ-20 самых частых слов:**

**1. the** [зэ] — определённый артикль
the cat, the dog, the book

**2. a / an** [э/эн] — неопределённый артикль
a cat, a dog, an apple, an orange

**3. and** [энд] — и
cat and dog, Tom and Ann

**4. is** [из] — есть (глагол быть)
He is happy. She is sad.

**5. it** [ит] — это, оно
It is a cat. It is nice.

**6. to** [ту] — к, в (направление)
go to school, go to bed

**7. in** [ин] — в (внутри)
in the box, in the bag

**8. on** [он] — на
on the table, on the chair

**9. at** [эт] — в (место)
at school, at home, at work

**10. we** [ви] — мы
We are happy. We go to school.

**11. you** [ю] — ты, вы
You are my friend. You are students.

**12. he** [хи] — он
He is a boy. He is tall.

**13. she** [ши] — она
She is a girl. She is kind.

**14. they** [зэй] — они
They are friends. They play games.

**15. I** [ай] — я
I am a student. I am happy.

**16. can** [кэн] — мочь, уметь
I can swim. She can sing.

**17. do** [ду] — делать
Do you like cats? I do not know.

**18. not** [нот] — не
I do not know. He is not sad.

**19. have** [хэв] — иметь
I have a cat. She has a dog.

**20. for** [фо] — для
This is for you. It is for me.

**Примеры предложений:**

- I have a cat and a dog.
- She is happy.
- They go to school.
- We can swim.
- He is in the house.`,
          tasks: [
            "Выучить 20 частых слов",
            "Составить предложения с these words",
            "Использовать слова в речи",
            "Прочитать текст с these words"
          ]
        }
      ]
    },
    {
      topic: "Numbers and Colors",
      lessons: [
        {
          title: "Урок 5: Numbers 1-20",
          description: `**Числа от 1 до 20**

Числа — это основа для счёта, возраста, времени и многого другого.

**Числа от 1 до 10:**

- **One** [уан] — один (1)
- **Two** [ту] — два (2)
- **Three** [три] — три (3)
- **Four** [фо] — четыре (4)
- **Five** [файв] — пять (5)
- **Six** [сикс] — шесть (6)
- **Seven** [севен] — семь (7)
- **Eight** [эйт] — восемь (8)
- **Nine** [найн] — девять (9)
- **Ten** [тен] — десять (10)

**Числа от 11 до 20:**

- **Eleven** [илевен] — одиннадцать (11)
- **Twelve** [туелв] — двенадцать (12)
- **Thirteen** [сётин] — тринадцать (13)
- **Fourteen** [фотин] — четырнадцать (14)
- **Fifteen** [фифтин] — пятнадцать (15)
- **Sixteen** [сикстин] — шестнадцать (16)
- **Seventeen** [севентин] — семнадцать (17)
- **Eighteen** [эйтин] — восемнадцать (18)
- **Nineteen** [найнтин] — девятнадцать (19)
- **Twenty** [туенти] — двадцать (20)

**Правила образования чисел 13-19:**

К числам 3-9 добавляется окончание **-teen**:
- Three → Thir teen (обратите внимание: three → thirteen)
- Four → Four teen
- Five → Fif teen (five → fifteen)
- Six → Six teen
- Seven → Seven teen
- Eight → Eigh teen
- Nine → Nine teen (nine → nineteen)

**Ударение в числах 13-19:**
Ударение падает на окончание -teen: thirTEEN, fourTEEN, fifTEEN

**Использование чисел:**

**Возраст:**
- I am seven. — Мне семь лет.
- How old are you? — Сколько тебе лет?

**Количество:**
- I have three cats. — У меня три кошки.
- There are five books. — Там пять книг.

**Телефонный номер:**
- My number is 5-7-9-2-4. — Мой номер 5-7-9-2-4.

**Время:**
- It's five o'clock. — Сейчас пять часов.

**Математика:**
- Two plus three is five. (2 + 3 = 5)
- Ten minus four is six. (10 - 4 = 6)`,
          tasks: [
            "Выучить числа от 1 до 10",
            "Выучить числа от 11 до 20",
            "Посчитать предметы",
            "Назвать свой возраст"
          ]
        },
        {
          title: "Урок 6: Numbers 20-100",
          description: `**Десятки до ста**

После 20 числа образуются по правилу: десятки + единицы.

**Десятки (Tens):**

- **Twenty** [туенти] — двадцать (20)
- **Thirty** [сёти] — тридцать (30)
- **Forty** [фоти] — сорок (40)
- **Fifty** [фифти] — пятьдесят (50)
- **Sixty** [сиксти] — шестьдесят (60)
- **Seventy** [севенти] — семьдесят (70)
- **Eighty** [эйти] — восемьдесят (80)
- **Ninety** [найнти] — девяносто (90)
- **One hundred** [уан хандред] — сто (100)

**Правила образования десятков:**

К числам 3-9 добавляется окончание **-ty**:
- Three → Thir ty (three → thirty)
- Four → For ty (four → forty — без u!)
- Five → Fif ty (five → fifty)
- Six → Six ty
- Seven → Seven ty
- Eight → Eigh ty
- Nine → Nine ty (nine → ninety)

**Образование составных чисел:**

Десятки + дефис + единицы:

- 21 = twenty-one
- 35 = thirty-five
- 47 = forty-seven
- 58 = fifty-eight
- 63 = sixty-three
- 74 = seventy-four
- 82 = eighty-two
- 99 = ninety-nine

**Примеры использования:**

**Возраст:**
- My mother is thirty-five. — Моей маме тридцать пять.
- My grandfather is seventy. — Моему дедушке семьдесят.

**Количество:**
- There are twenty-five students. — Там двадцать пять учеников.
- I have forty books. — У меня сорок книг.

**Года:**
- nineteen ninety-five (1995)
- two thousand (2000)
- two thousand twenty-three (2023)

**Цены:**
- It costs fifty dollars. — Это стоит пятьдесят долларов.
- The price is ninety-nine cents. — Цена — девяносто девять центов.

**Номера:**
- Room twenty-three — комната двадцать три
- Page forty-seven — страница сорок семь`,
          tasks: [
            "Выучить десятки от 20 до 90",
            "Образовать числа 25, 37, 48, 56",
            "Назвать возраст родителей",
            "Решить примеры на английском"
          ]
        },
        {
          title: "Урок 7: Colors",
          description: `**Цвета (Colors)**

Цвета помогают описывать предметы, одежду, природу.

**Основные цвета:**

- **Red** [ред] — красный
- **Blue** [блу] — синий
- **Yellow** [йеллоу] — жёлтый
- **Green** [грин] — зелёный
- **Orange** [ориндж] — оранжевый
- **Purple** [пёпл] — фиолетовый
- **Pink** [пинк] — розовый
- **Brown** [браун] — коричневый
- **Black** [блэк] — чёрный
- **White** [уайт] — белый
- **Grey** [грей] — серый

**Оттенки:**

- **Light** [лайт] — светлый
- **Dark** [дак] — тёмный
- **Light blue** — голубой (светло-синий)
- **Dark green** — тёмно-зелёный

**Вопрос о цвете:**

**What colour is it?** — Какой это цвет?
**What colour is the cat?** — Какого цвета кошка?

**Ответ:**
- It is red. — Он красный.
- It is blue and white. — Он синий с белым.

**Примеры описания предметов:**

- The apple is red. — Яблоко красное.
- The sky is blue. — Небо синее.
- The grass is green. — Трава зелёная.
- The sun is yellow. — Солнце жёлтое.
- The snow is white. — Снег белый.

**Сочетание цветов:**

- black and white — чёрно-белый
- red and white — красно-белый
- blue and yellow — сине-жёлтый

**Мой любимый цвет:**

**What is your favourite colour?** — Какой твой любимый цвет?
**My favourite colour is blue.** — Мой любимый цвет — синий.

**Радуга (Rainbow):**

В радуге 7 цветов: **Red, Orange, Yellow, Green, Blue, Indigo, Violet.**
Запоминалка: **R**ichard **O**f **Y**ork **G**ave **B**attle **I**n **V**ain.`,
          tasks: [
            "Выучить названия цветов",
            "Описать предметы по цвету",
            "Назвать свой любимый цвет",
            "Описать картинку"
          ]
        },
        {
          title: "Урок 8: Shapes",
          description: `**Фигуры (Shapes)**

Геометрические фигуры — это основа описания форм предметов.

**Основные фигуры:**

- **Circle** [сёкл] — круг
- **Square** [сквэа] — квадрат
- **Triangle** [трайэнгл] — треугольник
- **Rectangle** [ректэнгл] — прямоугольник
- **Oval** [оувал] — овал
- **Star** [ста] — звезда
- **Heart** [хат] — сердце
- **Diamond** [даймонд] — ромб

**Описание фигур:**

**Circle (Круг):**
A circle is round. It has no corners. — Круг круглый. У него нет углов.
Example: The sun is a circle. The clock is a circle.

**Square (Квадрат):**
A square has four equal sides. — У квадрата четыре равные стороны.
Example: A box is a square. The window is a square.

**Triangle (Треугольник):**
A triangle has three sides. — У треугольника три стороны.
Example: A roof is a triangle. The sign is a triangle.

**Rectangle (Прямоугольник):**
A rectangle has four sides. Two sides are long, two sides are short. — У прямоугольника четыре стороны. Две стороны длинные, две короткие.
Example: A door is a rectangle. A book is a rectangle.

**Oval (Овал):**
An oval is like a long circle. — Овал похож на длинный круг.
Example: An egg is an oval. A face is an oval.

**Вопросы о фигурах:**

**What shape is it?** — Какая это фигура?
- It is a circle. — Это круг.
- It is a square. — Это квадрат.

**How many sides?** — Сколько сторон?
- A triangle has three sides. — У треугольника три стороны.
- A square has four sides. — У квадрата четыре стороны.

**How many corners?** — Сколько углов?
- A triangle has three corners. — У треугольника три угла.
- A rectangle has four corners. — У прямоугольника четыре угла.

**Игра «Что похоже на фигуру?»:**
- What looks like a circle? — The sun, the moon, a ball.
- What looks like a square? — A window, a box, a book.
- What looks like a triangle? — A roof, a tree, a mountain.`,
          tasks: [
            "Выучить названия фигур",
            "Найти фигуры в классе",
            "Нарисовать фигуры и назвать",
            "Описать предмет по форме"
          ]
        }
      ]
    },
    {
      topic: "Family and People",
      lessons: [
        {
          title: "Урок 9: Family Members",
          description: `**Члены семьи (Family Members)**

Семья — это самые близкие люди. Давайте выучим их названия.

**Члены семьи:**

- **Mother / Mom / Mum** [маза/мом/мам] — мама
- **Father / Dad** [фаза/дэд] — папа
- **Sister** [систа] — сестра
- **Brother** [браза] — брат
- **Grandmother / Grandma** [грэндмаза/грэндма] — бабушка
- **Grandfather / Grandpa** [грэндфаза/грэндпа] — дедушка
- **Son** [сан] — сын
- **Daughter** [дота] — дочь
- **Aunt** [ант] — тётя
- **Uncle** [анкл] — дядя
- **Cousin** [казн] — двоюродный брат/сестра
- **Nephew** [нефью] — племянник
- **Niece** [нис] — племянница

**Примеры предложений:**

- This is my mother. — Это моя мама.
- This is my father. — Это мой папа.
- I have a sister. — У меня есть сестра.
- I have a brother. — У меня есть брат.
- My grandmother is kind. — Моя бабушка добрая.
- My grandfather is old. — Мой дедушка старый.

**Вопросы о семье:**

**How many people are in your family?** — Сколько человек в твоей семье?
- There are four people in my family. — В моей семье четыре человека.

**Do you have any brothers or sisters?** — У тебя есть братья или сёстры?
- Yes, I have a brother. — Да, у меня есть брат.
- No, I am an only child. — Нет, я единственный ребёнок.

**What is your mother's name?** — Как зовут твою маму?
- My mother's name is Anna. — Мою маму зовут Анна.

**Рассказ о семье:**

"Hello! My name is Tom. Let me tell you about my family. My family is big. I have a mother, a father, a grandmother, a grandfather, and a sister.

My mother's name is Olga. She is a teacher. She is kind and beautiful. My father's name is Ivan. He is a doctor. He is tall and strong.

My sister's name is Kate. She is five years old. She is funny and cute. My grandmother and grandfather live with us. They are old but very kind.

I love my family very much!"`,
          tasks: [
            "Выучить названия членов семьи",
            "Описать свою семью",
            "Нарисовать семейное дерево",
            "Рассказать о семье"
          ]
        },
        {
          title: "Урок 10: Describing People",
          description: `**Описание людей (Describing People)**

Чтобы описать человека, нужно знать слова для внешности и характера.

**Внешность (Appearance):**

**Рост:**
- **Tall** [тоол] — высокий
- **Short** [шот] — низкий
- **Medium height** — среднего роста

**Возраст:**
- **Young** [янг] — молодой
- **Old** [оулд] — старый

**Волосы (Hair):**
- **Long hair** — длинные волосы
- **Short hair** — короткие волосы
- **Curly hair** — кудрявые волосы
- **Straight hair** — прямые волосы
- **Blond hair** — светлые волосы
- **Dark hair** — тёмные волосы
- **Red hair** — рыжие волосы

**Цвет глаз (Eye colour):**
- **Blue eyes** — голубые глаза
- **Brown eyes** — карие глаза
- **Green eyes** — зелёные глаза
- **Grey eyes** — серые глаза

**Характер (Character):**

Положительные качества:
- **Kind** [кайнд] — добрый
- **Nice** [найс] — милый
- **Friendly** [френдли] — дружелюбный
- **Funny** [фани] — весёлый
- **Smart** [смат] — умный
- **Brave** [брейв] — храбрый
- **Clever** [клева] — умный, способный

Отрицательные качества:
- **Angry** [энгри] — злой
- **Lazy** [лэйзи] — ленивый
- **Silly** [сили] — глупый

**Примеры описания:**

**Рост и возраст:**
- He is tall and young. — Он высокий и молодой.
- She is short and old. — Она низкая и старая.

**Волосы и глаза:**
- She has long curly hair. — У неё длинные кудрявые волосы.
- He has short dark hair. — У него короткие тёмные волосы.
- She has blue eyes. — У неё голубые глаза.
- He has brown eyes. — У него карие глаза.

**Характер:**
- She is very kind. — Она очень добрая.
- He is funny and friendly. — Он весёлый и дружелюбный.

**Полное описание:**

"My best friend is Anna. She is tall and thin. She has long blond hair and blue eyes. She is very kind, friendly and funny. I like her very much!

My father is tall and strong. He has short dark hair and brown eyes. He is smart and brave. He is a doctor."`,
          tasks: [
            "Выучить слова для описания",
            "Описать внешность друга",
            "Описать характер мамы",
            "Написать описание человека"
          ]
        },
        {
          title: "Урок 11: Body Parts",
          description: `**Части тела (Body Parts)**

Знание частей тела важно для описания внешности и разговора о здоровье.

**Голова (Head):**

- **Head** [хед] — голова
- **Face** [фейс] — лицо
- **Hair** [хэа] — волосы
- **Eye** [ай] — глаз (eyes — глаза)
- **Ear** [иа] — ухо (ears — уши)
- **Nose** [ноуз] — нос
- **Mouth** [маус] — рот
- **Lip** [лип] — губа (lips — губы)
- **Tooth** [туус] — зуб (teeth — зубы)
- **Tongue** [танг] — язык
- **Cheek** [чик] — щека (cheeks — щёки)
- **Forehead** [форед] — лоб
- **Chin** [чин] — подбородок
- **Neck** [нек] — шея

**Тело (Body):**

- **Shoulder** [шоулда] — плечо (shoulders — плечи)
- **Arm** [ам] — рука (рука от плеча до кисти)
- **Hand** [хэнд] — кисть руки
- **Finger** [финга] — палец руки
- **Thumb** [сам] — большой палец
- **Chest** [чест] — грудь
- **Stomach** [стомак] — живот
- **Back** [бэк] — спина
- **Leg** [лег] — нога
- **Knee** [ни] — колено (knees — колени)
- **Foot** [фут] — стопа (feet — стопы)
- **Toe** [тоу] — палец ноги

**Песенка «Head, Shoulders, Knees and Toes»:**

Head, shoulders, knees and toes, knees and toes,
Head, shoulders, knees and toes, knees and toes,
And eyes and ears and mouth and nose,
Head, shoulders, knees and toes, knees and toes!

**Примеры предложений:**

- I have two eyes. — У меня два глаза.
- I have one nose. — У меня один нос.
- My hands are clean. — Мои руки чистые.
- Close your eyes. — Закрой глаза.
- Open your mouth. — Открой рот.

**Действия:**
- Touch your nose. — Дотронься до носа.
- Shake your hands. — Потряси руками.
- Clap your hands. — Похлопай в ладоши.
- Stamp your feet. — Потопай ногами.

**У врача (At the doctor):**
- My head hurts. — У меня болит голова.
- My stomach hurts. — У меня болит живот.
- I have a toothache. — У меня болит зуб.`,
          tasks: [
            "Выучить части тела",
            "Показать и назвать части тела",
            "Спеть песенку Head, Shoulders",
            "Описать лицо человека"
          ]
        },
        {
          title: "Урок 12: Clothes",
          description: `**Одежда (Clothes)**

Одежда — важная тема для описания внешности и покупок.

**Верхняя одежда:**

- **Coat** [коут] — пальто
- **Jacket** [джэкет] — куртка
- **Raincoat** [рейнкоут] — плащ
- **Hat** [хэт] — шляпа, шапка
- **Cap** [кэп] — кепка
- **Scarf** [скаф] — шарф
- **Gloves** [главз] — перчатки

**Верхняя повседневная одежда:**

- **Shirt** [шёт] — рубашка
- **T-shirt** [ти-шёт] — футболка
- **Sweater** [свитэ] — свитер
- **Dress** [дрес] — платье
- **Skirt** [скёт] — юбка
- **Blouse** [блауз] — блузка

**Нижняя одежда:**

- **Trousers** [тразэз] — брюки
- **Jeans** [джинз] — джинсы
- **Shorts** [шотс] — шорты

**Обувь:**

- **Shoes** [шуз] — туфли, обувь
- **Boots** [буц] — ботинки, сапоги
- **Trainers** [трейнэз] — кроссовки
- **Sandals** [сэндлз] — сандалии

**Аксессуары:**

- **Socks** [сокс] — носки
- **Tights** [тайц] — колготки
- **Belt** [белт] — ремень
- **Tie** [тай] — галстук

**Вопросы об одежде:**

**What are you wearing?** — Что на тебе надето?
- I am wearing a red dress. — На мне красное платье.
- I am wearing blue jeans and a white T-shirt. — На мне синие джинсы и белая футболка.

**What is he/she wearing?** — Что на нём/ней надето?
- He is wearing a black suit. — На нём чёрный костюм.
- She is wearing a beautiful dress. — На ней красивое платье.

**Цвет одежды:**
- a red shirt — красная рубашка
- blue jeans — синие джинсы
- a white T-shirt — белая футболка
- black shoes — чёрные туфли

**Погода и одежда:**

**What do you wear in winter?** — Что ты носишь зимой?
- I wear a coat, a hat, a scarf and gloves. — Я ношу пальто, шапку, шарф и перчатки.

**What do you wear in summer?** — Что ты носишь летом?
- I wear a T-shirt, shorts and sandals. — Я ношу футболку, шорты и сандалии.`,
          tasks: [
            "Выучить названия одежды",
            "Описать свою одежду",
            "Что носить зимой/летом",
            "Одеться по погоде"
          ]
        }
      ]
    },
    {
      topic: "Animals and Nature",
      lessons: [
        {
          title: "Урок 13: Pets",
          description: `**Домашние питомцы (Pets)**

Домашние животные живут вместе с людьми и являются нашими друзьями.

**Домашние питомцы:**

- **Cat** [кэт] — кошка
- **Dog** [дог] — собака
- **Hamster** [хэмста] — хомяк
- **Rabbit** [рэбит] — кролик
- **Guinea pig** [гини пиг] — морская свинка
- **Parrot** [пэрэт] — попугай
- **Fish** [фиш] — рыбка
- **Turtle** [тётл] — черепаха
- **Mouse** [маус] — мышь

**Части тела животных:**

- **Tail** [тейл] — хвост
- **Paw** [по] — лапа
- **Ear** [иа] — ухо
- **Fur** [фё] — шерсть
- **Beak** [бик] — клюв
- **Wing** [уинг] — крыло
- **Fin** [фин] — плавник

**Глаголы для описания животных:**

- **run** — бегать
- **jump** — прыгать
- **swim** — плавать
- **fly** — летать
- **climb** — лазить
- **play** — играть
- **sleep** — спать
- **eat** — есть

**Описание питомца:**

**I have a cat.** — У меня есть кошка.
**Her name is Murka.** — Её зовут Мурка.
**She is three years old.** — Ей три года.
**She is small and cute.** — Она маленькая и милая.
**She has grey fur and green eyes.** — У неё серая шерсть и зелёные глаза.
**She likes to play and sleep.** — Она любит играть и спать.

**Вопросы о питомце:**

**Do you have a pet?** — У тебя есть питомец?
- Yes, I have a dog. — Да, у меня есть собака.
- No, I don't have a pet. — Нет, у меня нет питомца.

**What is your pet's name?** — Как зовут твоего питомца?
- My dog's name is Rex. — Мою собаку зовут Рекс.

**What does it look like?** — Как он выглядит?
- He is big and brown. — Он большой и коричневый.

**Звуки животных:**
- Cats say «meow». — Кошки говорят «мяу».
- Dogs say «woof» or «bark». — Собаки говорят «гав».
- Birds say «tweet». — Птицы говорят «чирик».
- Mice say «squeak». — Мыши говорят «пи-пи».`,
          tasks: [
            "Выучить названия питомцев",
            "Описать своего питомца",
            "Рассказать о любимом животном",
            "Сравнить разных питомцев"
          ]
        },
        {
          title: "Урок 14: Wild Animals",
          description: `**Дикие животные (Wild Animals)**

Дикие животные живут в лесах, джунглях, саваннах и не живут дома у людей.

**Дикие животные:**

**В лесу (In the forest):**
- **Bear** [бэа] — медведь
- **Wolf** [вульф] — волк
- **Fox** [фокс] — лиса
- **Rabbit** [рэбит] — заяц
- **Deer** [диа] — олень
- **Squirrel** [сквирал] — белка
- **Hedgehog** [хеджог] — ёж

**В джунглях и саванне (In the jungle and savanna):**
- **Lion** [лайен] — лев
- **Tiger** [тайга] — тигр
- **Elephant** [элифант] — слон
- **Giraffe** [джираф] — жираф
- **Zebra** [зебра] — зебра
- **Monkey** [манки] — обезьяна
- **Crocodile** [крокодайл] — крокодил
- **Hippo** [хипо] — бегемот
- **Rhino** [райно] — носорог

**Другие животные:**
- **Snake** [снейк] — змея
- **Frog** [фрог] — лягушка
- **Owl** [аул] — сова
- **Eagle** [игл] — орёл

**Где живут животные:**

- **Forest** [форист] — лес
- **Jungle** [джангл] — джунгли
- **Zoo** [зу] — зоопарк
- **Africa** [эфрика] — Африка
- **River** [рива] — река
- **Mountain** [маунтин] — гора

**Описание животных:**

**The lion is big and strong.** — Лев большой и сильный.
**The giraffe is tall.** — Жираф высокий.
**The elephant is very big.** — Слон очень большой.
**The monkey is funny.** — Обезьяна смешная.
**The bear is strong.** — Медведь сильный.
**The fox is clever.** — Лиса хитрая.

**Что едят животные:**

**Хищники (Meat-eaters):**
- Lions eat meat. — Львы едят мясо.
- Wolves eat meat. — Волки едят мясо.

**Травоядные (Plant-eaters):**
- Elephants eat grass and leaves. — Слоны едят траву и листья.
- Giraffes eat leaves. — Жирафы едят листья.
- Rabbits eat grass and carrots. — Кролики едят траву и морковь.

**Интересные факты:**
- Lions are the kings of animals. — Львы — цари зверей.
- Elephants are the biggest land animals. — Слоны — самые большие сухопутные животные.
- Giraffes have the longest necks. — У жирафов самые длинные шеи.`,
          tasks: [
            "Выучить названия диких животных",
            "Рассказать, где живут животные",
            "Описать любимое дикое животное",
            "Сравнить хищников и травоядных"
          ]
        },
        {
          title: "Урок 15: Farm Animals",
          description: `**Домашние сельскохозяйственные животные (Farm Animals)**

Эти животные живут на ферме и приносят пользу людям.

**Животные фермы:**

- **Cow** [кау] — корова
- **Pig** [пиг] — свинья
- **Sheep** [шип] — овца
- **Goat** [гоут] — коза
- **Horse** [хос] — лошадь
- **Chicken** [чикен] — курица
- **Rooster** [руста] — петух
- **Duck** [дак] — утка
- **Goose** [гус] — гусь
- **Turkey** [тёки] — индюк
- **Donkey** [донки] — осёл

**Детёныши животных:**

- Cow → **Calf** [каф] — телёнок
- Pig → **Piglet** [пиглит] — поросёнок
- Sheep → **Lamb** [лэм] — ягнёнок
- Horse → **Foal** [фоул] — жеребёнок
- Chicken → **Chick** [чик] — цыплёнок
- Duck → **Duckling** [даклинг] — утёнок
- Dog → **Puppy** [папи] — щенок
- Cat → **Kitten** [китн] — котёнок

**Что дают животные:**

**Cow** даёт:
- **Milk** — молоко
- **Meat** — мясо (beef — говядина)

**Chicken** даёт:
- **Eggs** — яйца
- **Meat** — мясо

**Sheep** даёт:
- **Wool** — шерсть
- **Meat** — мясо (mutton — баранина)

**Honey** даёт:
- **Bee** — пчела

**Звуки животных:**
- Cows say «moo». — Коровы мычат «му».
- Pigs say «oink». — Свиньи хрюкают «хрю».
- Sheep say «baa». — Овцы блеют «бее».
- Horses say «neigh». — Лошади ржут «иго-го».
- Ducks say «quack». — Утки крякают «кря».
- Roosters say «cock-a-doodle-doo». — Петухи кукарекают «кукареку».

**Описание фермы:**

"On the farm there are many animals. There are cows, pigs, sheep, chickens and horses. Cows give us milk. Chickens give us eggs. Sheep give us wool. Farmers take care of the animals."`,
          tasks: [
            "Выучить названия фермерских животных",
            "Назвать детёнышей животных",
            "Рассказать, что дают животные",
            "Изобразить звуки животных"
          ]
        },
        {
          title: "Урок 16: Weather",
          description: `**Погода (Weather)**

Погода — важная тема для повседневного общения.

**Виды погоды:**

**Основные слова:**
- **Sunny** [сани] — солнечно
- **Cloudy** [клауди] — облачно
- **Rainy** [рейни] — дождливо
- **Snowy** [сноуи] — снежно
- **Windy** [винди] — ветрено
- **Foggy** [фоги] — туманно
- **Stormy** [стоми] — буря, гроза
- **Hot** [хот] — жарко
- **Warm** [вом] — тепло
- **Cold** [коулд] — холодно
- **Cool** [кул] — прохладно

**Вопрос о погоде:**

**What is the weather like today?** — Какая сегодня погода?
- It is sunny today. — Сегодня солнечно.
- It is rainy today. — Сегодня дождливо.
- It is cold today. — Сегодня холодно.

**Времена года (Seasons):**

- **Winter** [винта] — зима
- **Spring** [спринг] — весна
- **Summer** [сама] — лето
- **Autumn** [отом] — осень

**Погода по сезонам:**

**Winter (Зима):**
- It is cold in winter. — Зимой холодно.
- It snows in winter. — Зимой идёт снег.
- We can ski and skate. — Мы можем кататься на лыжах и коньках.

**Spring (Весна):**
- It is warm in spring. — Весной тепло.
- It rains in spring. — Весной идёт дождь.
- Flowers bloom in spring. — Весной цветут цветы.

**Summer (Лето):**
- It is hot in summer. — Летом жарко.
- The sun shines in summer. — Летом светит солнце.
- We can swim in summer. — Летом можно плавать.

**Autumn (Осень):**
- It is cool in autumn. — Осенью прохладно.
- It rains in autumn. — Осенью идёт дождь.
- Leaves fall in autumn. — Осенью падают листья.

**Одежда по погоде:**

**When it is cold, I wear...** — Когда холодно, я ношу...
- a coat, a hat, a scarf, gloves, boots

**When it is hot, I wear...** — Когда жарко, я ношу...
- a T-shirt, shorts, sandals

**When it rains, I wear...** — Когда идёт дождь, я ношу...
- a raincoat, boots, take an umbrella`,
          tasks: [
            "Выучить слова о погоде",
            "Описать погоду сегодня",
            "Назвать времена года",
            "Выбрать одежду по погоде"
          ]
        }
      ]
    },
    {
      topic: "Food and Drinks",
      lessons: [
        {
          title: "Урок 17: Fruits and Vegetables",
          description: `**Фрукты и овощи (Fruits and Vegetables)**

Фрукты и овощи — это полезная еда.

**Фрукты (Fruits):**

- **Apple** [эпл] — яблоко
- **Pear** [пеа] — груша
- **Banana** [банана] — банан
- **Orange** [ориндж] — апельсин
- **Lemon** [лемон] — лимон
- **Peach** [пич] — персик
- **Plum** [плам] — слива
- **Grape** [грейп] — виноград
- **Cherry** [чери] — вишня
- **Strawberry** [стробери] — клубника
- **Watermelon** [вотамелон] — арбуз
- **Melon** [мелон] — дыня
- **Pineapple** [пайнэпл] — ананас

**Овощи (Vegetables):**

- **Tomato** [томэйтоу] — помидор
- **Potato** [потэйтоу] — картофель
- **Carrot** [кэрот] — морковь
- **Cucumber** [кьюкамба] — огурец
- **Cabbage** [кэбидж] — капуста
- **Onion** [аньон] — лук
- **Garlic** [галик] — чеснок
- **Pepper** [пепа] — перец
- **Corn** [кон] — кукуруза
- **Pumpkin** [пампкин] — тыква
- **Beet** [бит] — свёкла
- **Radish** [рэдиш] — редис

**Вопросы о еде:**

**Do you like apples?** — Ты любишь яблоки?
- Yes, I do. I like apples. — Да. Я люблю яблоки.
- No, I don't. I don't like apples. — Нет. Я не люблю яблоки.

**What is your favourite fruit?** — Какой твой любимый фрукт?
- My favourite fruit is banana. — Мой любимый фрукт — банан.

**What vegetables do you like?** — Какие овощи ты любишь?
- I like carrots and tomatoes. — Я люблю морковь и помидоры.

**Описание вкуса:**

- **Sweet** [суит] — сладкий (apples are sweet)
- **Sour** [сауа] — кислый (lemons are sour)
- **Fresh** [фреш] — свежий
- **Tasty** [тейсти] — вкусный
- **Yummy** [ями] — вкусно

**Предложения:**

- Apples are red, green or yellow. — Яблоки бывают красными, зелёными или жёлтыми.
- Bananas are yellow and sweet. — Бананы жёлтые и сладкие.
- Carrots are orange. — Морковь оранжевая.
- Cucumbers are green. — Огурцы зелёные.
- I eat fruit every day. — Я ем фрукты каждый день.`,
          tasks: [
            "Выучить названия фруктов",
            "Выучить названия овощей",
            "Сказать, что любишь",
            "Описать фрукты по цвету"
          ]
        },
        {
          title: "Урок 18: Food",
          description: `**Еда (Food)**

Еда — важная часть нашей жизни.

**Основные продукты:**

- **Bread** [бред] — хлеб
- **Rice** [райс] — рис
- **Pasta** [паста] — макароны
- **Meat** [мит] — мясо
- **Fish** [фиш] — рыба
- **Cheese** [чиз] — сыр
- **Butter** [бата] — масло
- **Egg** [эг] — яйцо
- **Soup** [суп] — суп
- **Salad** [салад] — салат
- **Pizza** [пицца] — пицца
- **Sandwich** [сэндуич] — бутерброд

**Мясные продукты:**
- **Chicken** — курица
- **Beef** — говядина
- **Pork** — свинина

**Молочные продукты:**
- **Milk** — молоко
- **Cheese** — сыр
- **Butter** — масло
- **Yogurt** — йогурт
- **Cottage cheese** — творог

**Приёмы пищи:**

- **Breakfast** [брекфаст] — завтрак
- **Lunch** [ланч] — обед
- **Dinner** [дина] — ужин

**Вопросы о еде:**

**What do you have for breakfast?** — Что ты ешь на завтрак?
- I have eggs and toast for breakfast. — Я ем яйца и тосты на завтрак.

**What do you have for lunch?** — Что ты ешь на обед?
- I have soup and salad for lunch. — Я ем суп и салат на обед.

**What do you have for dinner?** — Что ты ешь на ужин?
- I have meat and rice for dinner. — Я ем мясо и рис на ужин.

**Что есть в холодильнике:**

**There is some milk in the fridge.** — В холодильнике есть молоко.
**There are some eggs in the fridge.** — В холодильнике есть яйца.
**There is some cheese on the table.** — На столе есть сыр.

**Описание еды:**

- This soup is tasty. — Этот суп вкусный.
- I like pizza. — Я люблю пиццу.
- My favourite food is pasta. — Моя любимая еда — макароны.
- I don't like fish. — Я не люблю рыбу.`,
          tasks: [
            "Выучить названия продуктов",
            "Назвать любимую еду",
            "Составить меню на день",
            "Описать, что в холодильнике"
          ]
        },
        {
          title: "Урок 19: Drinks",
          description: `**Напитки (Drinks)**

Напитки утоляют жажду и сопровождают приёмы пищи.

**Напитки:**

- **Water** [вота] — вода
- **Milk** [милк] — молоко
- **Juice** [джус] — сок
- **Tea** [ти] — чай
- **Coffee** [кофи] — кофе
- **Cocoa** [кокоу] — какао
- **Lemonade** [лемонейд] — лимонад
- **Soda** [соуда] — газировка
- **Compote** [компоут] — компот
- **Kefir** [кефир] — кефир

**Виды сока:**
- Apple juice — яблочный сок
- Orange juice — апельсиновый сок
- Tomato juice — томатный сок
- Grape juice — виноградный сок

**Вопросы о напитках:**

**What would you like to drink?** — Что ты хочешь выпить?
- I would like some water, please. — Я хочу воды, пожалуйста.
- I would like some orange juice. — Я хочу апельсиновый сок.

**Do you like tea or coffee?** — Ты любишь чай или кофе?
- I like tea. — Я люблю чай.
- I don't like coffee. — Я не люблю кофе.

**Что ты пьёшь:**

**I drink water every day.** — Я пью воду каждый день.
**I drink milk in the morning.** — Я пью молоко утром.
**I drink tea with lemon.** — Я пью чай с лимоном.
**Children drink juice.** — Дети пьют сок.

**Полезные напитки:**
- Water is very healthy. — Вода очень полезна.
- Milk is good for children. — Молоко полезно для детей.
- Juice has vitamins. — В соке есть витамины.

**Описание напитков:**
- This tea is hot. — Этот чай горячий.
- This water is cold. — Эта вода холодная.
- Fresh juice is tasty. — Свежий сок вкусный.

**Фразы:**

- Can I have a glass of water? — Можно мне стакан воды?
- Can I have a cup of tea? — Можно мне чашку чая?
- I'm thirsty. — Я хочу пить.
- Would you like some tea? — Хочешь чаю?`,
          tasks: [
            "Выучить названия напитков",
            "Назвать любимый напиток",
            "Спросить, что хотят выпить",
            "Описать напитки"
          ]
        },
        {
          title: "Урок 20: At the Cafe",
          description: `**В кафе (At the Cafe)**

Кафе — это место, где можно заказать еду и напитки.

**Полезные фразы:**

**Приветствие:**
- Hello! Can I help you? — Здравствуйте! Чем могу помочь?
- Good afternoon! — Добрый день!

**Заказ:**
- I would like a pizza, please. — Я хотел бы пиццу, пожалуйста.
- Can I have a hamburger? — Можно мне гамбургер?
- I'll have tea with lemon. — Я буду чай с лимоном.
- I'd like some orange juice. — Я хочу апельсиновый сок.

**Вопросы официанта:**
- What would you like? — Что вы хотите?
- Would you like anything to drink? — Хотите что-нибудь выпить?
- Anything else? — Что-нибудь ещё?

**Ответы:**
- Yes, please. — Да, пожалуйста.
- No, thank you. — Нет, спасибо.
- That's all. — Это всё.

**Еда в кафе:**

- **Hamburger** [хэмбёгэ] — гамбургер
- **Cheeseburger** — чизбургер
- **French fries** — картофель фри
- **Pizza** — пицца
- **Hot dog** — хот-дог
- **Sandwich** — бутерброд
- **Salad** — салат
- **Ice cream** — мороженое
- **Cake** — торт

**Напитки в кафе:**
- Cola — кола
- Lemonade — лимонад
- Tea — чай
- Coffee — кофе
- Juice — сок

**Диалог в кафе:**

**Waiter:** Hello! Can I help you?
**Customer:** Yes, please. I would like a hamburger and French fries.
**Waiter:** Would you like anything to drink?
**Customer:** Yes, can I have a lemonade, please?
**Waiter:** Here you are!
**Customer:** Thank you!
**Waiter:** You're welcome! Enjoy your meal!

**Оплата:**
- How much is it? — Сколько это стоит?
- It's five dollars. — Это стоит пять долларов.
- Here you are. — Вот, держите.
- Thank you! Have a nice day! — Спасибо! Хорошего дня!

**Жалобы:**
- This soup is cold. — Этот суп холодный.
- This is not what I ordered. — Это не то, что я заказал.`,
          tasks: [
            "Выучить фразы для заказа",
            "Разыграть диалог в кафе",
            "Заказать еду и напитки",
            "Спросить цену"
          ]
        }
      ]
    },
    {
      topic: "Daily Routine",
      lessons: [
        {
          title: "Урок 21: Time",
          description: `**Время (Time)**

Время помогает нам планировать день.

**Циферблат часов:**

- **Clock** [клок] — часы (настенные, настольные)
- **Watch** [воч] — наручные часы
- **Hour hand** — часовая стрелка
- **Minute hand** — минутная стрелка

**Как спросить время:**

**What time is it?** — Который час?
**What's the time?** — Сколько времени?

**Как ответить:**

**It's ... o'clock.** — ... часов.
- It's one o'clock. — Один час.
- It's five o'clock. — Пять часов.
- It's twelve o'clock. — Двенадцать часов.

**Половина часа:**

**It's half past ...** — Половина ... (30 минут)
- It's half past one. — Половина второго (1:30).
- It's half past three. — Половина четвёртого (3:30).
- It's half past six. — Половина седьмого (6:30).

**Четверть часа:**

**It's a quarter past ...** — Четверть ... (15 минут)
- It's a quarter past two. — Четверть третьего (2:15).

**It's a quarter to ...** — Без четверти ...
- It's a quarter to three. — Без четверти три (2:45).

**Минуты:**
- It's ten past five. — Десять минут шестого (5:10).
- It's twenty past three. — Двадцать минут четвёртого (3:20).
- It's ten to six. — Без десяти шесть (5:50).

**Части дня:**

- **Morning** [монинг] — утро
- **Afternoon** [афтанун] — день
- **Evening** [ивнинг] — вечер
- **Night** [найт] — ночь

**Приветствия по времени:**
- Good morning! — Доброе утро! (до 12:00)
- Good afternoon! — Добрый день! (12:00-18:00)
- Good evening! — Добрый вечер! (после 18:00)
- Good night! — Спокойной ночи! (перед сном)

**Вопросы о времени:**
- What time do you get up? — Во сколько ты встаёшь?
- What time do you go to school? — Во сколько ты идёшь в школу?
- What time do you go to bed? — Во сколько ты ложишься спать?`,
          tasks: [
            "Выучить слова о времени",
            "Назвать время по часам",
            "Спросить и ответить о времени",
            "Составить расписание"
          ]
        },
        {
          title: "Урок 22: Daily Activities",
          description: `**Ежедневные дела (Daily Activities)**

Режим дня — это порядок действий в течение дня.

**Утро (Morning):**

- **Wake up** — просыпаться
- **Get up** — вставать (с постели)
- **Wash my face** — умываться
- **Brush my teeth** — чистить зубы
- **Comb my hair** — причёсываться
- **Get dressed** — одеваться
- **Have breakfast** — завтракать
- **Go to school** — идти в школу

**День (Afternoon):**

- **Have lunch** — обедать
- **Go home** — идти домой
- **Do homework** — делать домашнюю работу
- **Play** — играть
- **Read** — читать

**Вечер (Evening):**

- **Have dinner** — ужинать
- **Watch TV** — смотреть телевизор
- **Take a shower** — принимать душ
- **Go to bed** — ложиться спать

**Рассказ о своём дне:**

"In the morning I wake up at seven o'clock. I wash my face and brush my teeth. I have breakfast at half past seven. I go to school at eight o'clock.

In the afternoon I have lunch at school. I come home at two o'clock. I do my homework at three o'clock. I play with my friends at four o'clock.

In the evening I have dinner at six o'clock. I watch TV or read a book. I go to bed at nine o'clock."

**Вопросы о режиме дня:**

**What time do you wake up?** — Во сколько ты просыпаешься?
- I wake up at 7 o'clock. — Я просыпаюсь в 7 часов.

**What do you do in the morning?** — Что ты делаешь утром?
- I wash my face and have breakfast. — Я умываюсь и завтракаю.

**When do you do your homework?** — Когда ты делаешь домашнюю работу?
- I do my homework after school. — Я делаю домашнюю работу после школы.`,
          tasks: [
            "Выучить фразы о режиме дня",
            "Рассказать о своём утре",
            "Описать свой день",
            "Сравнить режим дня"
          ]
        },
        {
          title: "Урок 23: Days of Week",
          description: `**Дни недели (Days of the Week)**

В неделе 7 дней. Нужно знать их названия и порядок.

**Дни недели:**

- **Monday** [манди] — понедельник
- **Tuesday** [тьюздди] — вторник
- **Wednesday** [уэнздди] — среда
- **Thursday** [сёздди] — четверг
- **Friday** [фрайди] — пятница
- **Saturday** [сэтади] — суббота
- **Понедельник — Saturday — выходные

**Вопросы о днях недели:**

**What day is it today?** — Какой сегодня день?
- Today is Monday. — Сегодня понедельник.
- Today is Friday. — Сегодня пятница.

**What day was yesterday?** — Какой день был вчера?
- Yesterday was Sunday. — Вчера было воскресенье.

**What day is tomorrow?** — Какой день будет завтра?
- Tomorrow is Tuesday. — Завтра будет вторник.

**Что ты делаешь в разные дни:**

**What do you do on Monday?** — Что ты делаешь в понедельник?
- I go to school on Monday. — В понедельник я хожу в школу.

**What do you do on Sunday?** — Что ты делаешь в воскресенье?
- I stay at home on Sunday. — В воскресенье я остаюсь дома.
- I visit my grandmother on Sunday. — В воскресенье я навещаю бабушку.

**Расписание:**

- On Monday I have Math and English. — В понедельник у меня математика и английский.
- On Tuesday I have PE and Art. — Во вторник у меня физкультура и ИЗО.
- On Wednesday I have Music and Russian. — В среду у меня музыка и русский язык.
- On Saturday I play football. — В субботу я играю в футбол.
- On Sunday I rest. — В воскресенье я отдыхаю.

**Песенка дней недели:**

Monday, Tuesday, Wednesday, Thursday,
Friday, Saturday, Sunday too.
One, two, three, four, five, six, seven days,
Every week I play with you!`,
          tasks: [
            "Выучить дни недели",
            "Назвать сегодняшний день",
            "Рассказать, что делаешь в разные дни",
            "Составить расписание недели"
          ]
        },
        {
          title: "Урок 24: Months and Seasons",
          description: `**Месяцы и сезоны (Months and Seasons)**

В году 12 месяцев и 4 сезона.

**Сезоны (Seasons):**

- **Winter** [винта] — зима
- **Spring** [спринг] — весна
- **Summer** [сама] — лето
- **Autumn** [отом] — осень (в США: fall)

**Месяцы (Months):**

**Зима (Winter):**
- **December** [дисэмба] — декабрь
- **January** [джэньюари] — январь
- **February** [фебруари] — февраль

**Весна (Spring):**
- **March** [мач] — март
- **April** [эйпрал] — апрель
- **May** [мэй] — май

**Лето (Summer):**
- **June** [джун] — июнь
- **July** [джулай] — июль
- **August** [огаст] — август

**Осень (Autumn):**
- **September** [сэптэмба] — сентябрь
- **October** [октоуба] — октябрь
- **November** [новемба] — ноябрь

**Вопросы:**

**What season is it now?** — Какое сейчас время года?
- It is winter. — Сейчас зима.

**What month is it?** — Какой сейчас месяц?
- It is January. — Сейчас январь.

**What is your favourite season?** — Какое твоё любимое время года?
- My favourite season is summer. — Моё любимое время года — лето.

**When is your birthday?** — Когда твой день рождения?
- My birthday is in May. — Мой день рождения в мае.

**Особенности сезонов:**

**Winter is cold.** — Зимой холодно.
- It snows in winter. — Зимой идёт снег.
- We can ski and skate. — Можно кататься на лыжах и коньках.

**Spring is warm.** — Весной тепло.
- Flowers bloom in spring. — Весной цветут цветы.
- Birds come back. — Птицы возвращаются.

**Summer is hot.** — Летом жарко.
- The sun shines. — Солнце светит.
- We can swim. — Можно плавать.

**Autumn is cool.** — Осенью прохладно.
- It rains in autumn. — Осенью идёт дождь.
- Leaves fall. — Листья падают.`,
          tasks: [
            "Выучить названия месяцев",
            "Выучить названия сезонов",
            "Назвать текущий месяц и сезон",
            "Рассказать о любимом времени года"
          ]
        }
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
      { type: 'quiz', question: "Как будет «5» на английском?", options: ["four", "five", "six"], correctAnswer: "five", hint: "1-one, 2-two, 3-three, 4-four, 5-?" },
      { type: 'quiz', question: "Как будет «12» на английском?", options: ["twelve", "twenty", "two"], correctAnswer: "twelve", hint: "11-eleven, 12-?" },
      { type: 'fill', question: "«25» по-английски: twenty-__", correctAnswer: "five", hint: "25 = twenty-five" },
      { type: 'quiz', question: "Какое число «seventeen»?", options: ["16", "17", "18"], correctAnswer: "17", hint: "Seven + teen = seventeen" }
    ],
    reward: { stars: 3, message: "Great! You know numbers! 🔢" }
  },
  {
    title: "Colors in English",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Как будет «красный» на английском?", options: ["red", "blue", "green"], correctAnswer: "red", hint: "Apple is red" },
      { type: 'quiz', question: "Какой цвет «yellow»?", options: ["жёлтый", "зелёный", "синий"], correctAnswer: "жёлтый", hint: "Sun is yellow" },
      { type: 'find', question: "Выбери названия цветов:", options: ["Red", "Cat", "Blue", "Green", "Dog", "Yellow"], correctAnswer: ["Red", "Blue", "Green", "Yellow"], hint: "Colors are: red, blue, green, yellow..." },
      { type: 'quiz', question: "Как будет «оранжевый»?", options: ["orange", "purple", "pink"], correctAnswer: "orange", hint: "Orange fruit is orange!" }
    ],
    reward: { stars: 3, message: "Excellent! You know colors! 🎨" }
  },
  {
    title: "Family Members",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "«Mother» — это:", options: ["папа", "мама", "сестра"], correctAnswer: "мама", hint: "Mother = мама" },
      { type: 'quiz', question: "Как будет «бабушка» на английском?", options: ["grandmother", "grandfather", "mother"], correctAnswer: "grandmother", hint: "Grand + mother = grandmother" },
      { type: 'fill', question: "Brother — это __", correctAnswer: "брат", hint: "Brother = брат, Sister = сестра" },
      { type: 'quiz', question: "«Father» — это:", options: ["отец", "дедушка", "брат"], correctAnswer: "отец", hint: "Father = папа, отец" }
    ],
    reward: { stars: 3, message: "Great! You know family! 👨‍👩‍👧‍👦" }
  },
  {
    title: "Animals in English",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Как будет «кошка» на английском?", options: ["dog", "cat", "bird"], correctAnswer: "cat", hint: "Meow! 🐱" },
      { type: 'quiz', question: "«Dog» — это:", options: ["собака", "кошка", "лошадь"], correctAnswer: "собака", hint: "Woof! 🐕" },
      { type: 'quiz', question: "Как будет «лев»?", options: ["tiger", "lion", "bear"], correctAnswer: "lion", hint: "King of the jungle 🦁" },
      { type: 'fill', question: "Elephant — это __", correctAnswer: "слон", hint: "Big grey animal with a trunk 🐘" }
    ],
    reward: { stars: 3, message: "Super! You know animals! 🐾" }
  },
  {
    title: "Food and Drinks",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "«Apple» — это:", options: ["апельсин", "яблоко", "банан"], correctAnswer: "яблоко", hint: "Red or green fruit 🍎" },
      { type: 'quiz', question: "Как будет «хлеб» на английском?", options: ["bread", "water", "milk"], correctAnswer: "bread", hint: "Bread 🍞" },
      { type: 'quiz', question: "«Water» — это:", options: ["молоко", "вода", "сок"], correctAnswer: "вода", hint: "We drink water 💧" },
      { type: 'fill', question: "Banana — это __", correctAnswer: "банан", hint: "Yellow fruit 🍌" }
    ],
    reward: { stars: 3, message: "Excellent! You know food! 🍎" }
  },
  {
    title: "Days and Months",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Как будет «понедельник»?", options: ["Monday", "Sunday", "Friday"], correctAnswer: "Monday", hint: "First day of the week" },
      { type: 'quiz', question: "«Sunday» — это:", options: ["суббота", "воскресенье", "понедельник"], correctAnswer: "воскресенье", hint: "Last day of the week" },
      { type: 'quiz', question: "Какой месяц «January»?", options: ["февраль", "январь", "март"], correctAnswer: "январь", hint: "First month of the year" },
      { type: 'quiz', question: "Как будет «лето»?", options: ["spring", "summer", "winter"], correctAnswer: "summer", hint: "Hot season with holidays ☀️" }
    ],
    reward: { stars: 3, message: "Great! You know calendar! 📅" }
  },
  {
    title: "Body Parts",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "«Head» — это:", options: ["рука", "голова", "нога"], correctAnswer: "голова", hint: "On your shoulders" },
      { type: 'quiz', question: "Как будет «глаза»?", options: ["ears", "eyes", "nose"], correctAnswer: "eyes", hint: "Two eyes to see 👀" },
      { type: 'fill', question: "Nose — это __", correctAnswer: "нос", hint: "On your face, you breathe with it 👃" },
      { type: 'quiz', question: "«Hands» — это:", options: ["ноги", "руки", "уши"], correctAnswer: "руки", hint: "You write with your hands ✋" }
    ],
    reward: { stars: 3, message: "Super! You know body parts! 🫀" }
  },
  {
    title: "Basic Phrases",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "«Hello» — это:", options: ["пока", "привет", "спасибо"], correctAnswer: "привет", hint: "Greeting" },
      { type: 'quiz', question: "Как сказать «спасибо»?", options: ["Please", "Thank you", "Sorry"], correctAnswer: "Thank you", hint: "When someone helps you" },
      { type: 'quiz', question: "«Goodbye» — это:", options: ["здравствуйте", "до свидания", "извините"], correctAnswer: "до свидания", hint: "When you leave" },
      { type: 'fill', question: "«Как дела?» — How __ you?", correctAnswer: "are", hint: "How are you?" }
    ],
    reward: { stars: 3, message: "Excellent! You know phrases! 💬" }
  }
]
