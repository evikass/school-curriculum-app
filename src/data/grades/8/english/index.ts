import { SubjectData, GameLesson } from '@/data/types'

export const lessons: SubjectData = {
  title: "Иностранный язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: [
    "Present Tenses",
    "Past Tenses",
    "Future Tenses",
    "Modal Verbs",
    "Passive Voice",
    "Conditionals",
    "Vocabulary: Daily Life",
    "Reading Comprehension"
  ],
  detailedTopics: [
    {
      topic: "Present Tenses",
      lessons: [
        {
          title: "Present Simple",
          description: `**Present Simple** используется для описания регулярных действий, фактов и постоянных состояний.

**Основные случаи употребления:**
- Регулярные, повторяющиеся действия: *I wake up at 7 o'clock every day.*
- Факты и общеизвестные истины: *The Earth goes round the Sun.*
- Постоянные состояния: *She lives in London.*
- Расписания и программы: *The train leaves at 9:30.*

**Образование утверждений:**
I/You/We/They + V (base form): *I work, we play*
He/She/It + V+s/es: *He works, she watches*

**Образование вопросов:**
Do + I/you/we/they + V?: *Do you like music?*
Does + he/she/it + V?: *Does he play football?*

**Образование отрицаний:**
I/You/We/They + don't + V: *I don't like coffee.*
He/She/It + doesn't + V: *She doesn't work here.*

**Слова-маркеры:**
always, usually, often, sometimes, rarely, never, every day, on Mondays

**Правила правописания:**
- work → works
- play → plays
- watch → watches, teach → teaches
- study → studies
- have → has

**Примеры:**
- *My brother works in a bank.*
- *Do you speak English?*
- *She doesn't eat meat.*`,
          tasks: [
            "Раскройте скобки: He (go) to school every day.",
            "Поставьте вопрос: She plays tennis on Sundays.",
            "Образуйте отрицание: They live in Moscow.",
            "Переведите: Мой папа всегда читает газету утром."
          ],
          examples: [
            "He goes to school every day. — Он ходит в школу каждый день. (3-е лицо ед. ч., окончание -es)",
            "My mother works in a hospital. — Моя мама работает в больнице. (Факт, постоянное состояние)",
            "Do you like pizza? — Ты любишь пиццу? (Вопрос с вспомогательным глаголом do)"
          ],
          keyPoints: [
            "Основные случаи употребления — Регулярные, повторяющиеся действия: I wake up at 7 o'clock every day",
            "Образование утверждений — I/You/We/They + V (base form): I work, we play",
            "Правила правописания — work → works"
          ]
        },
        {
          title: "Present Continuous",
          description: `**Present Continuous** используется для описания действий, происходящих в данный момент.

**Основные случаи употребления:**
- Действие в момент речи: *I am reading a book now.*
- Временные ситуации: *She is staying with her aunt this week.*
- Развивающиеся ситуации: *The population is growing fast.*
- Планы на ближайшее будущее: *We are meeting tomorrow.*

**Образование:**
I + am + V-ing: *I am working.*
He/She/It + is + V-ing: *She is reading.*
We/You/They + are + V-ing: *They are playing.*

**Вопросы:**
Am I working? Is he reading? Are they playing?

**Отрицания:**
I am not working. She is not (isn't) reading. They are not (aren't) playing.

**Правила правописания:**
- work → working
- make → making (немая -e отпадает)
- run → running (удвоение согласной)
- lie → lying (ie → y)

**Слова-маркеры:**
now, at the moment, at present, today, this week, tonight

**Глаголы, не употребляющиеся в Continuous:**
- состояния: be, have, know, understand, believe
- чувства: like, love, hate, want, prefer
- восприятие: see, hear, smell, taste

**Примеры:**
- *Look! It is raining.*
- *What are you doing now?*
- *She isn't watching TV at the moment.*`,
          tasks: [
            "Раскройте скобки: Look! The children (play) in the garden.",
            "Поставьте вопрос: He is reading a newspaper now.",
            "Образуйте отрицание: We are watching TV.",
            "Выберите правильную форму: I (am knowing / know) him well."
          ],
          examples: [
            "Look! The children are playing in the yard. — Смотри! Дети играют во дворе. (Действие в данный момент)",
            "I am reading an interesting book now. — Я сейчас читаю интересную книгу.",
            "She is not watching TV at the moment. — Она сейчас не смотрит телевизор. (Отрицание: isn't + V-ing)"
          ],
          keyPoints: [
            "Основные случаи употребления — Действие в момент речи: I am reading a book now",
            "Правила правописания — work → working",
            "Глаголы, не употребляющиеся в Continuous — состояния: be, have, know, understand, believe"
          ]
        },
        {
          title: "Present Perfect",
          description: `**Present Perfect** связывает прошлое с настоящим.

**Основные случаи употребления:**
- Действие завершилось, результат важен сейчас: *I have lost my keys.* (не могу найти)
- Личный опыт: *I have been to Paris.*
- Недавние действия: *She has just arrived.*
- Действия с незавершённым временем: *I have written three letters today.*

**Образование:**
I/You/We/They + have + V3 (past participle)
He/She/It + has + V3

**Правильные глаголы:** work → worked
**Неправильные глаголы:** go → gone, see → seen, write → written

**Вопросы:**
Have you seen this film? Has she finished her work?

**Отрицания:**
I haven't seen him. She hasn't called me.

**Слова-маркеры:**
just, already, yet, ever, never, recently, lately
for (период времени), since (момент времени)

**Present Perfect vs Past Simple:**
- *I have lost my key.* (результат важен — не могу войти)
- *I lost my key yesterday.* (просто факт прошлого)

**Примеры:**
- *I have just finished my homework.*
- *Have you ever been to London?*
- *She has lived here for 5 years.*
- *We haven't met since 2020.*`,
          tasks: [
            "Раскройте скобки: I (see) this film already.",
            "Поставьте вопрос: She has finished the report.",
            "Заполните: I have known him ___ 2015. (for/since)",
            "Выберите время: We (went / have gone) to Paris last year."
          ],
          examples: [
            "I have already finished my homework. — Я уже закончил домашнее задание. (Результат важен сейчас)",
            "She has lived in Moscow for 10 years. — Она живёт в Москве 10 лет. (Предлог for — период времени)",
            "Have you ever been to St. Petersburg? — Ты когда-нибудь бывал в Санкт-Петербурге? (Опыт)"
          ],
          keyPoints: [
            "Основные случаи употребления — Личный опыт: I have been to Paris",
            "I have lost my key. (результат важен — не могу войти)",
            "Действие завершилось, результат важен сейчас: I have lost my keys. (не могу найти)"
          ]
        }
      ]
    },
    {
      topic: "Past Tenses",
      lessons: [
        {
          title: "Past Simple",
          description: `**Past Simple** используется для описания завершённых действий в прошлом.

**Основные случаи употребления:**
- Завершённые действия в прошлом: *I visited Paris last year.*
- Последовательность действий в прошлом: *He came home, had dinner and went to bed.*
- Повторяющиеся действия в прошлом: *We went to the cinema every weekend.*

**Образование правильных глаголов:**
V + ed: work → worked, play → played, watch → watched

**Образование неправильных глаголов:**
go → went, see → saw, have → had, come → came, do → did

**Вопросы:**
Did + subject + V?: *Did you see him yesterday?*

**Отрицания:**
subject + didn't + V: *I didn't go to school yesterday.*

**Правила правописания:**
- work → worked
- live → lived
- study → studied (y после согласной → i)
- stop → stopped (удвоение согласной)
- play → played

**Слова-маркеры:**
yesterday, last week/month/year, ... ago, in 2020, when I was young

**Глагол to be в Past Simple:**
I/He/She/It was: *I was at home.*
We/You/They were: *They were happy.*

**Примеры:**
- *We went to the cinema yesterday.*
- *Did she call you last night?*
- *He didn't understand the question.*
- *When I was a child, I liked ice cream.*`,
          tasks: [
            "Раскройте скобки: We (go) to the park last Sunday.",
            "Поставьте вопрос: She bought a new dress yesterday.",
            "Образуйте отрицание: He saw his friend at the party.",
            "Напишите 3-ю форму: go, see, have, come, do"
          ],
          examples: [
            "We went to the cinema yesterday. — Мы ходили в кино вчера. (Завершённое действие)",
            "She didn't understand the question. — Она не поняла вопрос. (Отрицание: didn't + V)",
            "Did you see him last night? — Ты видел его вчера вечером? (Вопрос с did)"
          ],
          keyPoints: [
            "Основные случаи употребления — Завершённые действия в прошлом: I visited Paris last year",
            "Образование правильных глаголов — V + ed: work → worked, play → played, watch → watched",
            "Правила правописания — work → worked"
          ]
        },
        {
          title: "Past Continuous",
          description: `**Past Continuous** описывает действия, которые длились в определённый момент в прошлом.

**Основные случаи употребления:**
- Действие в определённый момент прошлого: *At 5 o'clock yesterday I was reading.*
- Два одновременных действия: *While I was cooking, my husband was reading.*
- Прерванное действие: *When the phone rang, I was sleeping.*
- Фоновое действие: *The sun was shining and the birds were singing.*

**Образование:**
was/were + V-ing

I/He/She/It was + V-ing: *She was reading.*
We/You/They were + V-ing: *They were playing.*

**Вопросы:**
Was she reading? Were they playing?

**Отрицания:**
She wasn't reading. They weren't playing.

**Сочетание с Past Simple:**
Когда одно действие прерывает другое:
- Длинное действие — Past Continuous
- Короткое действие — Past Simple

*When I came home, my mother was cooking dinner.*
*While I was walking, it started to rain.*

**Слова-маркеры:**
at 5 o'clock yesterday, at that moment, while, when

**Примеры:**
- *What were you doing at 8 p.m. yesterday?*
- *While he was driving, he was listening to music.*
- *I wasn't sleeping when you called.*`,
          tasks: [
            "Раскройте скобки: At 7 o'clock yesterday I (watch) TV.",
            "Соедините: While she (cook), the phone (ring).",
            "Образуйте отрицание: They were playing football at that time.",
            "Переведите: Когда я пришёл домой, мама готовила ужин."
          ],
          examples: [
            "At 8 o'clock yesterday I was having breakfast. — Вчера в 8 часов я завтракал. (Конкретный момент)",
            "When I came home, my mother was cooking dinner. — Когда я пришёл, мама готовила ужин. (Прерванное действие)",
            "While he was reading, his brother was playing. — Пока он читал, его брат играл. (Одновременные действия)"
          ],
          keyPoints: [
            "Основные случаи употребления — Прерванное действие: When the phone rang, I was sleeping",
            "Сочетание с Past Simple — Когда одно действие прерывает другое:",
            "Когда одно действие прерывает другое — Длинное действие — Past Continuous"
          ]
        }
      ]
    },
    {
      topic: "Future Tenses",
      lessons: [
        {
          title: "Future Simple",
          description: `**Future Simple (will + V)** используется для будущих действий.

**Основные случаи употребления:**
- Мгновенные решения: *It's cold. I'll close the window.*
- Предсказания: *It will rain tomorrow.*
- Обещания: *I'll help you with your homework.*
- Предложения: *I'll carry your bag.*
- Угрозы: *I'll tell mum!*

**Образование:**
will + V (base form)

**Утверждения:**
I/You/He/She/We/They will come. (I'll come)

**Вопросы:**
Will you come to the party?

**Отрицания:**
I won't (will not) come.

**Слова-маркеры:**
tomorrow, next week/month/year, soon, in the future, in 2030

**Will vs Going to:**
- *I'll help you.* — мгновенное решение
- *I'm going to help you.* — запланированное действие

**Примеры:**
- *I think it will snow tomorrow.*
- *Will you marry me?*
- *She won't tell anyone.*
- *I'll call you later.*`,
          tasks: [
            "Раскройте скобки: I think it (be) cold tomorrow.",
            "Поставьте вопрос: She will come to the party.",
            "Образуйте отрицание: We will meet tomorrow.",
            "Выберите: Look at the clouds! It (will / is going to) rain."
          ],
          examples: [
            "I think it will rain tomorrow. — Думаю, завтра пойдёт дождь. (Предсказание с will)",
            "I will help you with your homework. — Я помогу тебе с домашним заданием. (Обещание)",
            "She won't tell anyone your secret. — Она никому не расскажет твой секрет. (Отрицание: won't)"
          ],
          keyPoints: [
            "Основные случаи употребления — Мгновенные решения: It's cold",
            "I'll help you. — мгновенное решение",
            "I'm going to help you. — запланированное действие"
          ]
        },
        {
          title: "To be going to",
          description: `**To be going to + V** используется для планов и намерений.

**Основные случаи употребления:**
- Планы и намерения: *I'm going to study medicine.*
- Предсказания на основе очевидных признаков: *Look at those clouds! It's going to rain.*

**Образование:**
am/is/are going to + V

I am going to + V: *I'm going to visit my grandmother.*
He/She/It is going to + V: *She's going to buy a car.*
We/You/They are going to + V: *They're going to move.*

**Вопросы:**
Am I going to pass? Is she going to come? Are they going to help?

**Отрицания:**
I'm not going to study. She isn't going to come. They aren't going to stay.

**Going to vs Present Continuous для планов:**
Оба используются для планов:
- *I'm going to meet Tom.* (намерение)
- *I'm meeting Tom at 5.* (договорённость)

**Going to vs Will:**
- *I'm going to study tonight.* (план)
- *I'll study tonight.* (решение в момент речи)

**Примеры:**
- *What are you going to do tomorrow?*
- *She's going to have a baby.*
- *He isn't going to sell his house.*`,
          tasks: [
            "Раскройте скобки: I (be going to) visit Paris next summer.",
            "Поставьте вопрос: She is going to buy a new car.",
            "Образуйте отрицание: They are going to leave early.",
            "Переведите: Я собираюсь стать врачом."
          ],
          examples: [
            "I am going to visit my grandmother next weekend. — Я собираюсь навестить бабушку в выходные. (План)",
            "Look at those clouds! It is going to rain. — Посмотри на тучи! Собирается дождь. (Признаки)",
            "They are going to move to a new flat. — Они собираются переехать в новую квартиру. (Намерение)"
          ],
          keyPoints: [
            "Основные случаи употребления — Планы и намерения: I'm going to study medicine",
            "Going to vs Present Continuous для планов — Оба используются для планов:",
            "Оба используются для планов — I'm going to meet Tom"
          ]
        }
      ]
    },
    {
      topic: "Modal Verbs",
      lessons: [
        {
          title: "Modal Verbs: Can, Could, Must",
          description: `**Modal Verbs (Модальные глаголы)** выражают отношение говорящего к действию.

**CAN — физическая возможность, умение:**
- *I can swim.* (Я умею плавать)
- *Can you help me?* (Можешь помочь?)
- *She can't speak French.* (Она не умеет говорить по-французски)

**COULD — вежливая просьба, возможность в прошлом:**
- *Could you open the door?* (Не могли бы вы открыть дверь?)
- *When I was young, I could run fast.* (В молодости я мог бегать быстро)

**MUST — обязанность, настоятельная необходимость:**
- *You must wear a uniform.* (Ты должен носить форму)
- *I must go now.* (Мне пора идти)
- *Must I do it now?* (Я должен делать это сейчас?)

**Особенности модальных глаголов:**
1. Не имеют окончаний -s, -ed, -ing
2. Не требуют вспомогательных глаголов
3. За ними следует инфинитив без to
4. Вопросы и отрицания образуются без do/does

**MUST vs HAVE TO:**
- *I must do it.* (личное решение)
- *I have to do it.* (внешняя необходимость)

**MUSTN'T vs DON'T HAVE TO:**
- *You mustn't smoke here.* (запрещено)
- *You don't have to come.* (не обязательно)

**Примеры:**
- *Can I borrow your pen?*
- *You must stop at the red light.*
- *She couldn't come yesterday.*`,
          tasks: [
            "Выберите: (Can / Must) you swim?",
            "Переведите: Ты должен сделать домашнее задание.",
            "Заполните: You (mustn't / don't have to) smoke here. It's forbidden.",
            "Образуйте вопрос: She can speak English."
          ],
          examples: [
            "She can speak three languages. — Она может говорить на трёх языках. (Умение)",
            "You must do your homework every day. — Ты должен делать домашнее задание каждый день. (Обязанность)",
            "Could you open the window, please? — Не могли бы вы открыть окно? (Вежливая просьба)"
          ],
          keyPoints: [
            "CAN — физическая возможность, умение:",
            "COULD — вежливая просьба, возможность в прошлом:",
            "MUST — обязанность, настоятельная необходимость:"
          ]
        },
        {
          title: "Modal Verbs: Should, May, Might",
          description: `**SHOULD — совет, рекомендация:**
- *You should see a doctor.* (Тебе следует показаться врачу)
- *You shouldn't eat so much sugar.* (Тебе не стоит есть столько сахара)
- *What should I do?* (Что мне делать?)

**MAY — вероятность, разрешение (формально):**
- *It may rain tomorrow.* (Возможно, завтра пойдёт дождь)
- *May I come in?* (Можно войти?) — формально
- *May I help you?* (Разрешите помочь?)

**MIGHT — меньшая вероятность:**
- *It might snow tonight.* (Возможно, ночью пойдёт снег — меньше уверенности)
- *She might be at home.* (Она, возможно, дома)

**Степени вероятности:**
- *must be* — точно, наверняка (She must be tired.)
- *may be / might be* — возможно (She may be at work.)
- *can't be* — не может быть (It can't be true!)

**Модальные глаголы в прошедшем времени:**
- *could have done* — мог бы сделать (но не сделал)
- *should have done* — следовало сделать
- *might have done* — мог бы сделать

**Примеры:**
- *You should study harder.*
- *May I ask a question?*
- *He might come later.*`,
          tasks: [
            "Выберите: You (should / must) see a dentist. Your tooth hurts.",
            "Переведите: Возможно, она придёт завтра.",
            "Заполните: (May / Must) I use your phone?",
            "Образуйте вопрос: I should tell her the truth."
          ],
          examples: [
            "You should eat more vegetables. — Тебе стоит есть больше овощей. (Совет)",
            "It may rain tomorrow. — Завтра может пойти дождь. (Возможность)",
            "He might come to the party. — Он, возможно, придёт на вечеринку. (Меньшая вероятность)"
          ],
          keyPoints: [
            "MAY — вероятность, разрешение (формально):",
            "MIGHT — меньшая вероятность:",
            "It might snow tonight. (Возможно, ночью пойдёт снег — меньше уверенности)"
          ]
        }
      ]
    },
    {
      topic: "Passive Voice",
      lessons: [
        {
          title: "Passive Voice",
          description: `**Passive Voice (Страдательный залог)** — действие производится над подлежащим.

**Active:** *People speak English all over the world.*
**Passive:** *English is spoken all over the world.*

**Образование Passive Voice:**
to be + V3 (past participle)

**Present Simple Passive:**
am/is/are + V3
- *This book is written in English.*
- *Cars are made in Japan.*

**Past Simple Passive:**
was/were + V3
- *The letter was sent yesterday.*
- *The houses were built last year.*

**Future Simple Passive:**
will be + V3
- *The project will be finished soon.*

**Present Perfect Passive:**
have/has been + V3
- *The work has been done.*

**Когда используется Passive:**
1. Важен объект, а не исполнитель
2. Исполнитель неизвестен
3. Официальный стиль

**Предлог BY:**
Если указываем исполнителя:
- *This picture was painted by Picasso.*

**Примеры:**
- *English is spoken here.*
- *The report was written by the manager.*
- *When will the decision be made?*`,
          tasks: [
            "Преобразуйте в Passive: They built this house in 1900.",
            "Преобразуйте в Passive: People speak Spanish in many countries.",
            "Заполните: The book (write) by a famous author.",
            "Переведите: Письмо было отправлено вчера."
          ],
          examples: [
            "This book was written by Pushkin. — Эта книга была написана Пушкиным. (Past Simple Passive с by)",
            "English is spoken in many countries. — На английском говорят во многих странах. (Present Simple Passive)",
            "The work has already been done. — Работа уже выполнена. (Present Perfect Passive)"
          ],
          keyPoints: [
            "Когда используется Passive — Важен объект, а не исполнитель",
            "Если указываем исполнителя — This picture was painted by Picasso",
            "Ключевое понятие: Passive Voice"
          ]
        }
      ]
    },
    {
      topic: "Conditionals",
      lessons: [
        {
          title: "Conditionals: Zero and First",
          description: `**Zero Conditional — факты и истины:**
If + Present Simple, Present Simple
- *If you heat water to 100°C, it boils.*
- *If I'm tired, I go to bed early.*

**First Conditional — реальные условия:**
If + Present Simple, will + V
- *If it rains, I will stay at home.*
- *If you study hard, you will pass the exam.*

**Структура First Conditional:**
If clause (условие) + Main clause (результат)
или
Main clause + If clause

**Вариации Main Clause:**
- *If you go to Paris, you can see the Eiffel Tower.* (can)
- *If you finish early, you may leave.* (may)
- *If you need help, call me.* (imperative)

**Unless = If not:**
- *Unless you hurry, you'll miss the bus.*
- (= If you don't hurry, you'll miss the bus.)

**When vs If:**
- *When I see him* — уверен, что увижу
- *If I see him* — не уверен

**Примеры:**
- *If the weather is good, we'll go for a walk.*
- *I won't come unless you invite me.*
- *If I have time, I'll call you.*`,
          tasks: [
            "Раскройте скобки: If she (come), I (be) happy.",
            "Переделайте: If you don't study, you won't pass. (use unless)",
            "Выберите тип: If you heat ice, it melts. (Zero/First)",
            "Переведите: Если будет хорошая погода, мы пойдём в парк."
          ],
          examples: [
            "If you heat ice, it melts. — Если нагреть лёд, он тает. (Zero Conditional — факт)",
            "If it rains tomorrow, we will stay at home. — Если завтра пойдёт дождь, мы останемся дома. (First Conditional)",
            "Unless you study hard, you won't pass the exam. — Если не будешь стараться, не сдашь. (Unless = if not)"
          ],
          keyPoints: [
            "First Conditional — реальные условия:",
            "When I see him — уверен, что увижу",
            "If I see him — не уверен"
          ]
        },
        {
          title: "Conditionals: Second and Third",
          description: `**Second Conditional — нереальные условия в настоящем:**
If + Past Simple, would + V
- *If I had a million dollars, I would buy a house.*
- *If I were you, I would accept the offer.*

**Важно:** were используется для всех лиц в Second Conditional
- *If I were you... / If she were here...*

**Second Conditional для советов:**
- *If I were you, I would study medicine.*

**Third Conditional — нереальные условия в прошлом:**
If + Past Perfect, would have + V3
- *If I had studied harder, I would have passed the exam.*
- *If she had come earlier, she would have seen him.*

**Таблица условных предложений:**

| Type | Condition | Result | Time |
|------|-----------|--------|------|
| Zero | Present | Present | Always |
| First | Present | will + V | Future |
| Second | Past | would + V | Present/Future (unreal) |
| Third | Past Perfect | would have + V3 | Past (unreal) |

**Примеры:**
- *If I knew the answer, I would tell you.* (Second)
- *If I had known the answer, I would have told you.* (Third)
- *If I were rich, I would travel the world.* (Second)`,
          tasks: [
            "Раскройте скобки: If I (be) you, I (go) to the doctor.",
            "Раскройте скобки: If she (study) harder, she (pass) the exam. (Third Conditional)",
            "Выберите тип: If I won the lottery, I would buy a house. (Second/Third)",
            "Переведите: Если бы я знал правду, я бы сказал тебе."
          ],
          examples: [
            "If I were rich, I would travel around the world. — Если бы я был богат, я бы путешествовал. (Second Conditional)",
            "If I had studied harder, I would have passed the exam. — Если бы учился усерднее, сдал бы. (Third Conditional)",
            "If I knew her phone number, I would call her. — Если бы знал номер, позвонил бы. (Second)"
          ],
          keyPoints: [
            "Second Conditional для советов — If I were you, I would study medicine",
            "Third Conditional — нереальные условия в прошлом:",
            "Ключевое понятие: Conditionals: Second and Third"
          ]
        }
      ]
    },
    {
      topic: "Vocabulary: Daily Life",
      lessons: [
        {
          title: "Daily Routine",
          description: `**Vocabulary: Daily Routine (Повседневные дела)**

**Утро (Morning):**
- wake up — просыпаться
- get up — вставать
- have a shower — принимать душ
- brush teeth — чистить зубы
- get dressed — одеваться
- have breakfast — завтракать
- leave home — выходить из дома
- go to school/work — идти в школу/на работу

**День (Day):**
- have lunch — обедать
- have classes — посещать уроки
- study — учиться
- do homework — делать домашнее задание
- work — работать
- have a break — делать перерыв

**Вечер (Evening):**
- come home — приходить домой
- have dinner — ужинать
- watch TV — смотреть телевизор
- read a book — читать книгу
- surf the Internet — сидеть в Интернете
- go to bed — ложиться спать

**Предлоги времени:**
- at 7 o'clock, at noon, at night
- in the morning, in the afternoon, in the evening
- on Monday, on the 5th of May

**Примеры:**
- *I usually wake up at 7 o'clock.*
- *After school I have lunch and do my homework.*
- *In the evening I watch TV or read a book.*`,
          tasks: [
            "Переведите: Я обычно просыпаюсь в 7 часов.",
            "Заполните: I have breakfast ___ the morning. (at/in/on)",
            "Составьте предложение: she / usually / up / get / at 7 o'clock",
            "Переведите: После школы я делаю домашнее задание."
          ],
          examples: [
            "I usually wake up at 7 o'clock and have a shower. — Я обычно просыпаюсь в 7 часов и принимаю душ.",
            "After school I do my homework and then watch TV. — После школы делаю домашку и смотрю ТВ.",
            "She goes to bed at 10 p.m. every day. — Она ложится спать в 10 вечера. (Предлог at со временем)"
          ],
          keyPoints: [
            "have a shower — принимать душ",
            "brush teeth — чистить зубы",
            "leave home — выходить из дома"
          ]
        },
        {
          title: "Hobbies and Free Time",
          description: `**Vocabulary: Hobbies and Free Time (Хобби и свободное время)**

**Виды хобби:**
- read books / magazines — читать книги/журналы
- watch films / series — смотреть фильмы/сериалы
- listen to music — слушать музыку
- play sports — заниматься спортом
- play computer games — играть в компьютерные игры
- draw / paint — рисовать
- dance — танцевать
- sing — петь
- cook — готовить
- travel — путешествовать
- take photos — фотографировать
- collect (stamps, coins) — коллекционировать

**Музыкальные инструменты:**
- play the piano — играть на пианино
- play the guitar — играть на гитаре
- play the violin — играть на скрипке

**Спорт:**
- play football / tennis / basketball
- go swimming — плавать
- go running — бегать
- go skiing — кататься на лыжах

**Вопросы о хобби:**
- *What do you do in your free time?*
- *What are your hobbies?*
- *Do you like reading?*
- *How often do you play sports?*

**Примеры:**
- *In my free time I like reading and listening to music.*
- *She's interested in photography.*
- *He's fond of playing football.*`,
          tasks: [
            "Переведите: В свободное время я люблю читать книги.",
            "Заполните: She can play ___ piano. (the/-)",
            "Составьте вопрос: you / do / What / do / free time / in your / ?",
            "Переведите: Я увлекаюсь фотографией."
          ],
          examples: [
            "In my free time I like reading books and listening to music. — В свободное время люблю читать и слушать музыку.",
            "She plays the piano very well. — Она очень хорошо играет на пианино. (Артикль the с инструментом)",
            "He is fond of playing football. — Он увлекается футболом. (Конструкция be fond of)"
          ],
          keyPoints: [
            "Виды хобби — read books / magazines — читать книги/журналы",
            "read books / magazines — читать книги/журналы",
            "watch films / series — смотреть фильмы/сериалы"
          ]
        }
      ]
    },
    {
      topic: "Reading Comprehension",
      lessons: [
        {
          title: "Reading Strategies",
          description: `**Reading Strategies (Стратегии чтения)**

**Виды чтения:**

**1. Skimming (Просмотровое чтение):**
- Быстрое прочтение для общего понимания
- Чтение заголовков, первых и последних предложений
- Цель: понять главную идею текста

**2. Scanning (Поисковое чтение):**
- Поиск конкретной информации
- Чтение с вопросом в голове
- Цель: найти нужные факты, даты, имена

**3. Detailed Reading (Изучающее чтение):**
- Внимательное чтение всего текста
- Анализ деталей и деталей
- Цель: полное понимание

**Полезные приёмы:**
1. **Predicting:** предсказать содержание по заголовку
2. **Guessing meaning:** догадаться о значении слова по контексту
3. **Identifying keywords:** находить ключевые слова
4. **Understanding reference:** понимать местоимения (he, she, it, they)

**Структура текста:**
- Introduction (введение) — главная идея
- Body paragraphs (основная часть) — детали и примеры
- Conclusion (заключение) — итоги

**При чтении обращайте внимание на:**
- Title — заголовок
- First sentence — первое предложение
- Linking words — слова-связки (however, therefore, because)
- Numbers and dates — цифры и даты`,
          tasks: [
            "Определите тип чтения: Find all names in the text. (Skimming/Scanning/Detailed)",
            "Что такое skimming?",
            "Перечислите три части структуры текста.",
            "Как догадаться о значении незнакомого слова?"
          ],
          examples: [
            "Skimming — быстрый просмотр заголовков и первого абзаца для понимания главной идеи текста.",
            "Scanning — поиск конкретного имени или даты в тексте, не читая его целиком.",
            "Слова-связки however (однако) и therefore (поэтому) помогают понять логическую структуру текста."
          ],
          keyPoints: [
            "Виды чтения — Skimming (Просмотровое чтение):",
            "Skimming (Просмотровое чтение) — Быстрое прочтение для общего понимания",
            "Scanning (Поисковое чтение) — Поиск конкретной информации"
          ]
        }
      ]
    }
  ]
}

export const games: GameLesson[] = [
  {
    title: "Present Simple 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Вопрос 1 по теме \"Present Simple\"", options: ["Примеры:","При чтении обращайте внимание на:","Present Simple","Going to vs Will:","Особенности модальных глаголов:"], correctAnswer: "Present Simple", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 2 по теме \"Present Simple\"", options: ["Виды хобби:","Образование Passive Voice:","Present Simple","Структура First Conditional:","Утверждения:"], correctAnswer: "Present Simple", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 3 по теме \"Present Simple\"", options: ["Passive:","Модальные глаголы в прошедшем времени:","Present Simple","Примеры:","Глаголы, не употребляющиеся в Continuous:"], correctAnswer: "Present Simple", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 4 по теме \"Present Simple\"", options: ["Образование правильных глаголов:","Спорт:","Утро (Morning):","Present Simple","Вопросы:"], correctAnswer: "Present Simple", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 5 по теме \"Present Simple\"", options: ["Present Simple","COULD — вежливая просьба, возможность в прошлом:","Отрицания:","3. Detailed Reading (Изучающее чтение):","При чтении обращайте внимание на:"], correctAnswer: "Present Simple", hint: "Ответ связан с материалом урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Present Continuous 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"Развивающиеся ситуации: *The population is growing...\"?", options: ["Виды чтения:","Развивающиеся ситуации","Основные случаи употребления:","3. Detailed Reading (Изучающее чтение):","Образование:"], correctAnswer: "Развивающиеся ситуации", hint: "Этот термин связан с темой: Present Continuous" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Present Continuous\"?", options: ["Going to vs Will:","Правила правописания:","Основные случаи употребления:","Виды чтения:","Образование:"], correctAnswer: "Правила правописания:", hint: "Ответ связан с уроком: Present Continuous" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Present Continuous\"?", options: ["состояния","working","Основные случаи употребления:","SHOULD — совет, рекомендация:","MIGHT — меньшая вероятность:"], correctAnswer: "working", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Present Continuous\":", options: ["Основные случаи употребления:","Примеры:","Слова-маркеры:","Глаголы, не употребляющиеся в Continuous:","Present Continuous","Образование:"], correctAnswer: ["Примеры:","Слова-маркеры:","Глаголы, не употребляющиеся в Continuous:"], hint: "Ищите термины, которые встречаются в уроке Present Continuous" },
      { type: 'quiz', question: "Что является основным понятием урока \"Present Continuous\"?", options: ["Глаголы, не употребляющиеся в Continuous:","Правила правописания:","Развивающиеся ситуации","**Основные случаи употребления:** - Действие в момент речи: ","Планы на ближайшее будущее"], correctAnswer: "**Основные случаи употребления:** - Действие в момент речи: ", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Present Perfect 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"Недавние действия: *She has just arrived...\"?", options: ["Guessing meaning:","Недавние действия","Глагол to be в Past Simple:","Present Continuous","Present Perfect Passive:"], correctAnswer: "Недавние действия", hint: "Этот термин связан с темой: Present Perfect" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Present Perfect\"?", options: ["MUST vs HAVE TO:","Модальные глаголы в прошедшем времени:","Слова-маркеры:","Present Perfect","COULD — вежливая просьба, возможность в прошлом:"], correctAnswer: "Present Perfect", hint: "Ответ связан с уроком: Present Perfect" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Present Perfect\"?", options: ["keys","Основные случаи употребления:","Слова-маркеры:","Reading Strategies (Стратегии чтения)","Guessing meaning:"], correctAnswer: "keys", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Present Perfect\":", options: ["Примеры:","Отрицания:","Present Perfect vs Past Simple:","Неправильные глаголы:","Present Perfect","Образование:"], correctAnswer: ["Present Perfect vs Past Simple:","Неправильные глаголы:","Примеры:"], hint: "Ищите термины, которые встречаются в уроке Present Perfect" },
      { type: 'quiz', question: "Что является основным понятием урока \"Present Perfect\"?", options: ["Правильные глаголы:","Недавние действия","Действие завершилось, результат важен сейчас","She has lived here for 5 years.","**Основные случаи употребления:** - Действие завершилось"], correctAnswer: "**Основные случаи употребления:** - Действие завершилось", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Past Simple 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Примеры:","Guessing meaning:","He didn't understand the question.","Основные случаи употребления:","Past Simple Passive:"], correctAnswer: "He didn't understand the question.", hint: "Этот термин связан с темой: Past Simple" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Past Simple\"?", options: ["Past Continuous","3. Detailed Reading (Изучающее чтение):","Глаголы, не употребляющиеся в Continuous:","Образование правильных глаголов:","Present Perfect vs Past Simple:"], correctAnswer: "Образование правильных глаголов:", hint: "Ответ связан с уроком: Past Simple" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Past Simple\"?", options: ["Present Perfect","прошлом","Past Simple","Степени вероятности:","Примеры:"], correctAnswer: "прошлом", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Past Simple\":", options: ["Образование правильных глаголов:","Вопросы:","Основные случаи употребления:","Past Simple","Отрицания:","Правила правописания:"], correctAnswer: ["Образование правильных глаголов:","Основные случаи употребления:","Past Simple"], hint: "Ищите термины, которые встречаются в уроке Past Simple" },
      { type: 'quiz', question: "Что является основным понятием урока \"Past Simple\"?", options: ["**Основные случаи употребления:** - Завершённые действия в п","Слова-маркеры:","Past Simple","We went to the cinema yesterday.","Образование неправильных глаголов:"], correctAnswer: "**Основные случаи употребления:** - Завершённые действия в п", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Past Continuous 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Образование неправильных глаголов:","What were you doing at 8 p.m. yesterday?","MUST — обязанность, настоятельная необходимость:","Вопросы о хобби:","Вопросы:"], correctAnswer: "What were you doing at 8 p.m. yesterday?", hint: "Этот термин связан с темой: Past Continuous" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Past Continuous\"?", options: ["При чтении обращайте внимание на:","Отрицания:","Основные случаи употребления:","Вопросы:","Third Conditional — нереальные условия в прошлом:"], correctAnswer: "Вопросы:", hint: "Ответ связан с уроком: Past Continuous" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Past Continuous\"?", options: ["Фоновое действие","Примеры:","Вопросы о хобби:","прошлом","MAY — вероятность, разрешение (формально):"], correctAnswer: "прошлом", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Past Continuous\":", options: ["Вопросы:","Слова-маркеры:","Past Continuous","Примеры:","Образование:","Отрицания:"], correctAnswer: ["Past Continuous","Вопросы:","Слова-маркеры:"], hint: "Ищите термины, которые встречаются в уроке Past Continuous" },
      { type: 'quiz', question: "Что является основным понятием урока \"Past Continuous\"?", options: ["**Основные случаи употребления:** - Действие в определённый ","Длинное действие","маркеры","Примеры:","Образование:"], correctAnswer: "**Основные случаи употребления:** - Действие в определённый ", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Future Simple 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Образование:","Active:","Особенности модальных глаголов:","Примеры:","маркеры"], correctAnswer: "маркеры", hint: "Этот термин связан с темой: Future Simple" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Future Simple\"?", options: ["Образование:","Unless = If not:","Полезные приёмы:","Основные случаи употребления:","Modal Verbs (Модальные глаголы)"], correctAnswer: "Основные случаи употребления:", hint: "Ответ связан с уроком: Future Simple" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Future Simple\"?", options: ["MUST vs HAVE TO:","Образование:","Understanding reference:","Основные случаи употребления:","your"], correctAnswer: "your", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Future Simple\":", options: ["Примеры:","Утверждения:","Слова-маркеры:","Отрицания:","Future Simple (will + V)","Образование:"], correctAnswer: ["Слова-маркеры:","Примеры:","Образование:"], hint: "Ищите термины, которые встречаются в уроке Future Simple" },
      { type: 'quiz', question: "Что является основным понятием урока \"Future Simple\"?", options: ["Отрицания:","**Основные случаи употребления:** - Мгновенные решения: *It'","маркеры","Will vs Going to:","Мгновенные решения"], correctAnswer: "**Основные случаи употребления:** - Мгновенные решения: *It'", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "To be going to 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"Предсказания на основе очевидных признаков: *Look ...\"?", options: ["Passive Voice (Страдательный залог)","Утро (Morning):","Виды чтения:","Past Simple","Предсказания на основе очевидных признаков"], correctAnswer: "Предсказания на основе очевидных признаков", hint: "Этот термин связан с темой: To be going to" },
      { type: 'quiz', question: "Какое понятие относится к теме \"To be going to\"?", options: ["Примеры:","Going to vs Present Continuous для планов:","Таблица условных предложений:","Вопросы:","When vs If:"], correctAnswer: "Going to vs Present Continuous для планов:", hint: "Ответ связан с уроком: To be going to" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"To be going to\"?", options: ["Предлог BY:","Вариации Main Clause:","grandmother","Вопросы:","Правила правописания:"], correctAnswer: "grandmother", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"To be going to\":", options: ["Going to vs Will:","Образование:","Вопросы:","Основные случаи употребления:","Going to vs Present Continuous для планов:","To be going to + V"], correctAnswer: ["To be going to + V","Going to vs Will:","Вопросы:"], hint: "Ищите термины, которые встречаются в уроке To be going to" },
      { type: 'quiz', question: "Что является основным понятием урока \"To be going to\"?", options: ["Вопросы:","Going to vs Will:","**Основные случаи употребления:** - Планы и намерения: *I'm ","Образование:","What are you going to do tomorrow?"], correctAnswer: "**Основные случаи употребления:** - Планы и намерения: *I'm ", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Modal Verbs: Can, Could, Must 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["MUSTN'T vs DON'T HAVE TO:","MAY — вероятность, разрешение (формально):","Can I borrow your pen?","Примеры:","Вопросы:"], correctAnswer: "Can I borrow your pen?", hint: "Этот термин связан с темой: Modal Verbs: Can, Could, Must" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Modal Verbs: Can, Could, Must\"?", options: ["Вопросы:","Слова-маркеры:","День (Day):","Примеры:","Особенности модальных глаголов:"], correctAnswer: "Особенности модальных глаголов:", hint: "Ответ связан с уроком: Modal Verbs: Can, Could, Must" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Modal Verbs: Can, Could, Must\"?", options: ["Vocabulary: Daily Routine (Повседневные дела)","При чтении обращайте внимание на:","Утро (Morning):","MUST vs HAVE TO:","must"], correctAnswer: "must", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Modal Verbs: Can, Could, Must\":", options: ["MUST — обязанность, настоятельная необходимость:","Особенности модальных глаголов:","Примеры:","CAN — физическая возможность, умение:","Modal Verbs (Модальные глаголы)","MUSTN'T vs DON'T HAVE TO:"], correctAnswer: ["Особенности модальных глаголов:","Modal Verbs (Модальные глаголы)","MUST — обязанность, настоятельная необходимость:"], hint: "Ищите термины, которые встречаются в уроке Modal Verbs: Can, Could, Must" },
      { type: 'quiz', question: "Что является основным понятием урока \"Modal Verbs: Can, Could, Must\"?", options: ["MUST — обязанность, настоятельная необходимость:","**CAN — физическая возможность","s, -ed,","CAN — физическая возможность, умение:","Примеры:"], correctAnswer: "**CAN — физическая возможность", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Modal Verbs: Should, May, Might 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"may be / might be* — возможно (She may be at work...\"?", options: ["Understanding reference:","Спорт:","Present Continuous","may be / might be","Will vs Going to:"], correctAnswer: "may be / might be", hint: "Этот термин связан с темой: Modal Verbs: Should, May, Might" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Modal Verbs: Should, May, Might\"?", options: ["Степени вероятности:","Present Perfect","Отрицания:","Second Conditional для советов:","1. Skimming (Просмотровое чтение):"], correctAnswer: "Степени вероятности:", hint: "Ответ связан с уроком: Modal Verbs: Should, May, Might" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Modal Verbs: Should, May, Might\"?", options: ["Past Simple Passive:","Future Simple (will + V)","tired","Правильные глаголы:","Глаголы, не употребляющиеся в Continuous:"], correctAnswer: "tired", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Modal Verbs: Should, May, Might\":", options: ["Степени вероятности:","Примеры:","MIGHT — меньшая вероятность:","MAY — вероятность, разрешение (формально):","Модальные глаголы в прошедшем времени:","SHOULD — совет, рекомендация:"], correctAnswer: ["Примеры:","Модальные глаголы в прошедшем времени:","SHOULD — совет, рекомендация:"], hint: "Ищите термины, которые встречаются в уроке Modal Verbs: Should, May, Might" },
      { type: 'quiz', question: "Что является основным понятием урока \"Modal Verbs: Should, May, Might\"?", options: ["MIGHT — меньшая вероятность:","Модальные глаголы в прошедшем времени:","could have done","* (Тебе следует показаться врачу) - *You shouldn't eat so mu","might have done"], correctAnswer: "* (Тебе следует показаться врачу) - *You shouldn't eat so mu", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Passive Voice 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["The letter was sent yesterday.","Present Perfect","Reading Strategies (Стратегии чтения)","Спорт:","Образование:"], correctAnswer: "The letter was sent yesterday.", hint: "Этот термин связан с темой: Passive Voice" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Passive Voice\"?", options: ["При чтении обращайте внимание на:","Образование утверждений:","First Conditional — реальные условия:","Present Simple Passive:","Going to vs Will:"], correctAnswer: "Present Simple Passive:", hint: "Ответ связан с уроком: Passive Voice" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Passive Voice\"?", options: ["Present Perfect Passive:","Отрицания:","Present Simple","Future Simple Passive:","Japan"], correctAnswer: "Japan", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Passive Voice\":", options: ["Passive Voice (Страдательный залог)","Present Perfect Passive:","Active:","Present Simple Passive:","Past Simple Passive:","Passive:"], correctAnswer: ["Present Simple Passive:","Passive:","Active:"], hint: "Ищите термины, которые встречаются в уроке Passive Voice" },
      { type: 'quiz', question: "Что является основным понятием урока \"Passive Voice\"?", options: ["Present Simple Passive:","Предлог BY:","Примеры:","Passive:","**Active:** *People speak English all over the world"], correctAnswer: "**Active:** *People speak English all over the world", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Conditionals: Zero and First 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Present Perfect","Примеры:","If the weather is good, we'll go for a walk.","If you heat water to 100°C, it boils.","Вопросы:"], correctAnswer: "If the weather is good, we'll go for a walk.", hint: "Этот термин связан с темой: Conditionals: Zero and First" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Conditionals: Zero and First\"?", options: ["Understanding reference:","Passive:","Виды чтения:","Вариации Main Clause:","Слова-маркеры:"], correctAnswer: "Вариации Main Clause:", hint: "Ответ связан с уроком: Conditionals: Zero and First" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Conditionals: Zero and First\"?", options: ["Вопросы:","Важно:","Identifying keywords:","Unless = If not:","Tower"], correctAnswer: "Tower", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Conditionals: Zero and First\":", options: ["Примеры:","Вариации Main Clause:","Zero Conditional — факты и истины:","First Conditional — реальные условия:","Unless = If not:","Структура First Conditional:"], correctAnswer: ["Структура First Conditional:","First Conditional — реальные условия:","Примеры:"], hint: "Ищите термины, которые встречаются в уроке Conditionals: Zero and First" },
      { type: 'quiz', question: "Что является основным понятием урока \"Conditionals: Zero and First\"?", options: ["* - *If I'm tired","If the weather is good, we'll go for a walk.","If it rains, I will stay at home.","Unless = If not:","When I see him"], correctAnswer: "* - *If I'm tired", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Conditionals: Second and Third 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Правила правописания:","Отрицания:","MUSTN'T vs DON'T HAVE TO:","Present Simple","-----|-----------|--------|-----"], correctAnswer: "-----|-----------|--------|-----", hint: "Этот термин связан с темой: Conditionals: Second and Third" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Conditionals: Second and Third\"?", options: ["MIGHT — меньшая вероятность:","Важно:","Спорт:","Отрицания:","Модальные глаголы в прошедшем времени:"], correctAnswer: "Важно:", hint: "Ответ связан с уроком: Conditionals: Second and Third" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Conditionals: Second and Third\"?", options: ["Going to vs Will:","Вариации Main Clause:","Образование:","house","MUST — обязанность, настоятельная необходимость:"], correctAnswer: "house", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Conditionals: Second and Third\":", options: ["Second Conditional — нереальные условия в настоящем:","Third Conditional — нереальные условия в прошлом:","Важно:","Second Conditional для советов:","Примеры:","Таблица условных предложений:"], correctAnswer: ["Second Conditional — нереальные условия в настоящем:","Second Conditional для советов:","Таблица условных предложений:"], hint: "Ищите термины, которые встречаются в уроке Conditionals: Second and Third" },
      { type: 'quiz', question: "Что является основным понятием урока \"Conditionals: Second and Third\"?", options: ["If I had a million dollars, I would buy a house.","Third Conditional — нереальные условия в прошлом:","* - *If I were you","-----|-----------|--------|-----","Примеры:"], correctAnswer: "* - *If I were you", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Daily Routine 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"go to bed — ложиться спать...\"?", options: ["Active:","2. Scanning (Поисковое чтение):","go to bed","brush teeth","Вопросы:"], correctAnswer: "go to bed", hint: "Этот термин связан с темой: Daily Routine" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Daily Routine\"?", options: ["Present Simple Passive:","Основные случаи употребления:","Вопросы:","Примеры:","Предлоги времени:"], correctAnswer: "Предлоги времени:", hint: "Ответ связан с уроком: Daily Routine" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Daily Routine\":", options: ["День (Day):","Вечер (Evening):","Vocabulary: Daily Routine (Повседневные дела)","Утро (Morning):","Предлоги времени:","Примеры:"], correctAnswer: ["День (Day):","Вечер (Evening):","Предлоги времени:"], hint: "Ищите термины, которые встречаются в уроке Daily Routine" },
      { type: 'quiz', question: "Что является основным понятием урока \"Daily Routine\"?", options: ["go to bed","study","I usually wake up at 7 o'clock.","* - *In the evening I watch TV or read a book","Вечер (Evening):"], correctAnswer: "* - *In the evening I watch TV or read a book", hint: "Ответ содержится в описании урока" },
      { type: 'quiz', question: "Вопрос 5 по теме \"Daily Routine\"", options: ["Образование:","Предлоги времени:","Таблица условных предложений:","Third Conditional — нереальные условия в прошлом:","wake up"], correctAnswer: "Предлоги времени:", hint: "Ответ связан с материалом урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Hobbies and Free Time 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"go skiing — кататься на лыжах...\"?", options: ["go skiing","Музыкальные инструменты:","Unless = If not:","MUST — обязанность, настоятельная необходимость:","Примеры:"], correctAnswer: "go skiing", hint: "Этот термин связан с темой: Hobbies and Free Time" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Hobbies and Free Time\":", options: ["Спорт:","Vocabulary: Hobbies and Free Time (Хобби и свободное время)","Виды хобби:","Вопросы о хобби:","Примеры:","Музыкальные инструменты:"], correctAnswer: ["Спорт:","Музыкальные инструменты:","Vocabulary: Hobbies and Free Time (Хобби и свободное время)"], hint: "Ищите термины, которые встречаются в уроке Hobbies and Free Time" },
      { type: 'quiz', question: "Что является основным понятием урока \"Hobbies and Free Time\"?", options: ["* - *He's fond of playing football","travel","dance","Примеры:","listen to music"], correctAnswer: "* - *He's fond of playing football", hint: "Ответ содержится в описании урока" },
      { type: 'quiz', question: "Вопрос 4 по теме \"Hobbies and Free Time\"", options: ["Спорт:","Going to vs Will:","CAN — физическая возможность, умение:","Правила правописания:","Слова-маркеры:"], correctAnswer: "Спорт:", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 5 по теме \"Hobbies and Free Time\"", options: ["Unless = If not:","Вопросы о хобби:","Примеры:","Passive:","Предлоги времени:"], correctAnswer: "Вопросы о хобби:", hint: "Ответ связан с материалом урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Reading Strategies 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"Цель: понять главную идею текста...\"?", options: ["Глагол to be в Past Simple:","Future Simple Passive:","Understanding reference:","Цель","Виды чтения:"], correctAnswer: "Цель", hint: "Этот термин связан с темой: Reading Strategies" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Reading Strategies\"?", options: ["Вариации Main Clause:","Слова-маркеры:","Reading Strategies (Стратегии чтения)","Утро (Morning):","Образование утверждений:"], correctAnswer: "Reading Strategies (Стратегии чтения)", hint: "Ответ связан с уроком: Reading Strategies" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Reading Strategies\"?", options: ["First Conditional — реальные условия:","контексту","Introduction (введение)","Past Simple","Примеры:"], correctAnswer: "контексту", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Reading Strategies\":", options: ["Полезные приёмы:","Структура текста:","При чтении обращайте внимание на:","Identifying keywords:","Reading Strategies (Стратегии чтения)","1. Skimming (Просмотровое чтение):"], correctAnswer: ["Reading Strategies (Стратегии чтения)","При чтении обращайте внимание на:","Структура текста:"], hint: "Ищите термины, которые встречаются в уроке Reading Strategies" },
      { type: 'quiz', question: "Что является основным понятием урока \"Reading Strategies\"?", options: ["2. Scanning (Поисковое чтение):","Цель","Skimming (Просмотровое чтение):** - Быстрое прочтение для об","Внимательное чтение всего текста","Reading Strategies (Стратегии чтения)"], correctAnswer: "Skimming (Просмотровое чтение):** - Быстрое прочтение для об", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  }
] = [
  {
    title: "Present Simple 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Вопрос 1 по теме \"Present Simple\"", options: ["2. Scanning (Поисковое чтение):","Структура текста:","Примеры:","Виды чтения:","Present Simple"], correctAnswer: "Present Simple", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 2 по теме \"Present Simple\"", options: ["Примеры:","Правила правописания:","Образование:","Present Continuous","Present Simple"], correctAnswer: "Present Simple", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 3 по теме \"Present Simple\"", options: ["Примеры:","Vocabulary: Daily Routine (Повседневные дела)","Passive Voice (Страдательный залог)","Слова-маркеры:","Present Simple"], correctAnswer: "Present Simple", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 4 по теме \"Present Simple\"", options: ["1. Skimming (Просмотровое чтение):","2. Scanning (Поисковое чтение):","Present Simple","Present Perfect vs Past Simple:","Особенности модальных глаголов:"], correctAnswer: "Present Simple", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 5 по теме \"Present Simple\"", options: ["Примеры:","Образование Passive Voice:","Present Simple","Active:","Полезные приёмы:"], correctAnswer: "Present Simple", hint: "Ответ связан с материалом урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Present Continuous 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["маркеры","Present Simple Passive:","Правила правописания:","Вечер (Evening):","Основные случаи употребления:"], correctAnswer: "маркеры", hint: "Этот термин связан с темой: Present Continuous" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Present Continuous\"?", options: ["При чтении обращайте внимание на:","Отрицания:","Основные случаи употребления:","3. Detailed Reading (Изучающее чтение):","Образование:"], correctAnswer: "Основные случаи употребления:", hint: "Ответ связан с уроком: Present Continuous" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Present Continuous\"?", options: ["fast","Примеры:","Образование:","Важно:","Will vs Going to:"], correctAnswer: "fast", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Present Continuous\":", options: ["Present Continuous","Примеры:","Слова-маркеры:","Глаголы, не употребляющиеся в Continuous:","Правила правописания:","Образование:"], correctAnswer: ["Глаголы, не употребляющиеся в Continuous:","Примеры:","Present Continuous"], hint: "Ищите термины, которые встречаются в уроке Present Continuous" },
      { type: 'quiz', question: "Что является основным понятием урока \"Present Continuous\"?", options: ["Временные ситуации","Действие в момент речи","Отрицания:","**Основные случаи употребления:** - Действие в момент речи: ","Глаголы, не употребляющиеся в Continuous:"], correctAnswer: "**Основные случаи употребления:** - Действие в момент речи: ", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Present Perfect 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"Личный опыт: *I have been to Paris...\"?", options: ["Present Perfect vs Past Simple:","Личный опыт","Музыкальные инструменты:","Образование:","Future Simple Passive:"], correctAnswer: "Личный опыт", hint: "Этот термин связан с темой: Present Perfect" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Present Perfect\"?", options: ["Неправильные глаголы:","Identifying keywords:","MIGHT — меньшая вероятность:","MUSTN'T vs DON'T HAVE TO:","Слова-маркеры:"], correctAnswer: "Неправильные глаголы:", hint: "Ответ связан с уроком: Present Perfect" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Present Perfect\"?", options: ["CAN — физическая возможность, умение:","Слова-маркеры:","Passive:","Образование отрицаний:","Paris"], correctAnswer: "Paris", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Present Perfect\":", options: ["Слова-маркеры:","Вопросы:","Present Perfect","Отрицания:","Неправильные глаголы:","Примеры:"], correctAnswer: ["Примеры:","Present Perfect","Отрицания:"], hint: "Ищите термины, которые встречаются в уроке Present Perfect" },
      { type: 'quiz', question: "Что является основным понятием урока \"Present Perfect\"?", options: ["**Основные случаи употребления:** - Действие завершилось","Примеры:","Present Perfect","She has lived here for 5 years.","Правильные глаголы:"], correctAnswer: "**Основные случаи употребления:** - Действие завершилось", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Past Simple 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["He didn't understand the question.","Образование:","Примеры:","Modal Verbs (Модальные глаголы)","Present Continuous"], correctAnswer: "He didn't understand the question.", hint: "Этот термин связан с темой: Past Simple" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Past Simple\"?", options: ["Образование вопросов:","To be going to + V","Passive:","Предлог BY:","Past Simple"], correctAnswer: "Past Simple", hint: "Ответ связан с уроком: Past Simple" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Past Simple\"?", options: ["Неправильные глаголы:","weekend","Слова-маркеры:","Примеры:","Vocabulary: Daily Routine (Повседневные дела)"], correctAnswer: "weekend", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Past Simple\":", options: ["Основные случаи употребления:","Past Simple","Образование неправильных глаголов:","Отрицания:","Слова-маркеры:","Образование правильных глаголов:"], correctAnswer: ["Образование правильных глаголов:","Past Simple","Основные случаи употребления:"], hint: "Ищите термины, которые встречаются в уроке Past Simple" },
      { type: 'quiz', question: "Что является основным понятием урока \"Past Simple\"?", options: ["work → worked","Повторяющиеся действия в прошлом","**Основные случаи употребления:** - Завершённые действия в п","He didn't understand the question.","Отрицания:"], correctAnswer: "**Основные случаи употребления:** - Завершённые действия в п", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Past Continuous 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"Прерванное действие: *When the phone rang, I was s...\"?", options: ["Примеры:","День (Day):","Вечер (Evening):","Предлог BY:","Прерванное действие"], correctAnswer: "Прерванное действие", hint: "Этот термин связан с темой: Past Continuous" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Past Continuous\"?", options: ["Фоновое действие","Образование:","MUST — обязанность, настоятельная необходимость:","Отрицания:","Слова-маркеры:"], correctAnswer: "Образование:", hint: "Ответ связан с уроком: Past Continuous" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Past Continuous\"?", options: ["SHOULD — совет, рекомендация:","Отрицания:","Основные случаи употребления:","reading","Сочетание с Past Simple:"], correctAnswer: "reading", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Past Continuous\":", options: ["Отрицания:","Слова-маркеры:","Образование:","Вопросы:","Примеры:","Past Continuous"], correctAnswer: ["Вопросы:","Past Continuous","Отрицания:"], hint: "Ищите термины, которые встречаются в уроке Past Continuous" },
      { type: 'quiz', question: "Что является основным понятием урока \"Past Continuous\"?", options: ["Фоновое действие","**Основные случаи употребления:** - Действие в определённый ","Два одновременных действия","Примеры:","Основные случаи употребления:"], correctAnswer: "**Основные случаи употребления:** - Действие в определённый ", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Future Simple 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Образование:","Примеры:","Глагол to be в Past Simple:","Модальные глаголы в прошедшем времени:","I think it will snow tomorrow."], correctAnswer: "I think it will snow tomorrow.", hint: "Этот термин связан с темой: Future Simple" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Future Simple\"?", options: ["Угрозы","Слова-маркеры:","2. Scanning (Поисковое чтение):","Will vs Going to:","Предложения"], correctAnswer: "Will vs Going to:", hint: "Ответ связан с уроком: Future Simple" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Future Simple\"?", options: ["She won't tell anyone.","Примеры:","homework","Степени вероятности:","Образование:"], correctAnswer: "homework", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Future Simple\":", options: ["Вопросы:","Утверждения:","Отрицания:","Future Simple (will + V)","Will vs Going to:","Основные случаи употребления:"], correctAnswer: ["Will vs Going to:","Future Simple (will + V)","Вопросы:"], hint: "Ищите термины, которые встречаются в уроке Future Simple" },
      { type: 'quiz', question: "Что является основным понятием урока \"Future Simple\"?", options: ["Вопросы:","**Основные случаи употребления:** - Мгновенные решения: *It'","маркеры","Обещания","I'll help you."], correctAnswer: "**Основные случаи употребления:** - Мгновенные решения: *It'", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "To be going to 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"Предсказания на основе очевидных признаков: *Look ...\"?", options: ["Modal Verbs (Модальные глаголы)","Слова-маркеры:","Правила правописания:","Предсказания на основе очевидных признаков","Vocabulary: Daily Routine (Повседневные дела)"], correctAnswer: "Предсказания на основе очевидных признаков", hint: "Этот термин связан с темой: To be going to" },
      { type: 'quiz', question: "Какое понятие относится к теме \"To be going to\"?", options: ["Вопросы о хобби:","Present Simple Passive:","Примеры:","To be going to + V","Правила правописания:"], correctAnswer: "To be going to + V", hint: "Ответ связан с уроком: To be going to" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"To be going to\"?", options: ["намерений","Present Perfect","Слова-маркеры:","Образование:","Вопросы:"], correctAnswer: "намерений", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"To be going to\":", options: ["Going to vs Present Continuous для планов:","Отрицания:","Going to vs Will:","Основные случаи употребления:","To be going to + V","Вопросы:"], correctAnswer: ["Отрицания:","To be going to + V","Going to vs Present Continuous для планов:"], hint: "Ищите термины, которые встречаются в уроке To be going to" },
      { type: 'quiz', question: "Что является основным понятием урока \"To be going to\"?", options: ["Going to vs Present Continuous для планов:","Отрицания:","**Основные случаи употребления:** - Планы и намерения: *I'm ","Going to vs Will:","Примеры:"], correctAnswer: "**Основные случаи употребления:** - Планы и намерения: *I'm ", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Modal Verbs: Can, Could, Must 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Отрицания:","Can I borrow your pen?","SHOULD — совет, рекомендация:","To be going to + V","Примеры:"], correctAnswer: "Can I borrow your pen?", hint: "Этот термин связан с темой: Modal Verbs: Can, Could, Must" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Modal Verbs: Can, Could, Must\"?", options: ["MUST vs HAVE TO:","Образование:","Примеры:","Глагол to be в Past Simple:","Отрицания:"], correctAnswer: "MUST vs HAVE TO:", hint: "Ответ связан с уроком: Modal Verbs: Can, Could, Must" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Modal Verbs: Can, Could, Must\"?", options: ["Will vs Going to:","Zero Conditional — факты и истины:","swim","Примеры:","Вопросы:"], correctAnswer: "swim", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Modal Verbs: Can, Could, Must\":", options: ["MUST vs HAVE TO:","MUST — обязанность, настоятельная необходимость:","Особенности модальных глаголов:","COULD — вежливая просьба, возможность в прошлом:","Modal Verbs (Модальные глаголы)","MUSTN'T vs DON'T HAVE TO:"], correctAnswer: ["Modal Verbs (Модальные глаголы)","MUST vs HAVE TO:","Особенности модальных глаголов:"], hint: "Ищите термины, которые встречаются в уроке Modal Verbs: Can, Could, Must" },
      { type: 'quiz', question: "Что является основным понятием урока \"Modal Verbs: Can, Could, Must\"?", options: ["MUST — обязанность, настоятельная необходимость:","Modal Verbs (Модальные глаголы)","**CAN — физическая возможность","CAN — физическая возможность, умение:","Примеры:"], correctAnswer: "**CAN — физическая возможность", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Modal Verbs: Should, May, Might 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"may be / might be* — возможно (She may be at work...\"?", options: ["Правила правописания:","Предлог BY:","must be","may be / might be","Слова-маркеры:"], correctAnswer: "may be / might be", hint: "Этот термин связан с темой: Modal Verbs: Should, May, Might" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Modal Verbs: Should, May, Might\"?", options: ["Слова-маркеры:","Вопросы о хобби:","Образование вопросов:","Примеры:","Предлог BY:"], correctAnswer: "Примеры:", hint: "Ответ связан с уроком: Modal Verbs: Should, May, Might" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Modal Verbs: Should, May, Might\"?", options: ["Present Continuous","Отрицания:","tomorrow","Вечер (Evening):","Образование неправильных глаголов:"], correctAnswer: "tomorrow", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Modal Verbs: Should, May, Might\":", options: ["Примеры:","MIGHT — меньшая вероятность:","Модальные глаголы в прошедшем времени:","MAY — вероятность, разрешение (формально):","Степени вероятности:","SHOULD — совет, рекомендация:"], correctAnswer: ["Примеры:","MIGHT — меньшая вероятность:","Степени вероятности:"], hint: "Ищите термины, которые встречаются в уроке Modal Verbs: Should, May, Might" },
      { type: 'quiz', question: "Что является основным понятием урока \"Modal Verbs: Should, May, Might\"?", options: ["may be / might be","SHOULD — совет, рекомендация:","might have done","Степени вероятности:","* (Тебе следует показаться врачу) - *You shouldn't eat so mu"], correctAnswer: "* (Тебе следует показаться врачу) - *You shouldn't eat so mu", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Passive Voice 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Guessing meaning:","English is spoken here.","MIGHT — меньшая вероятность:","The letter was sent yesterday.","Примеры:"], correctAnswer: "The letter was sent yesterday.", hint: "Этот термин связан с темой: Passive Voice" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Passive Voice\"?", options: ["Вариации Main Clause:","MUSTN'T vs DON'T HAVE TO:","Passive Voice (Страдательный залог)","Утверждения:","Основные случаи употребления:"], correctAnswer: "Passive Voice (Страдательный залог)", hint: "Ответ связан с уроком: Passive Voice" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Passive Voice\"?", options: ["Слова-маркеры:","CAN — физическая возможность, умение:","Образование утверждений:","English","Active:"], correctAnswer: "English", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Passive Voice\":", options: ["Образование Passive Voice:","Future Simple Passive:","Present Simple Passive:","Present Perfect Passive:","Примеры:","Предлог BY:"], correctAnswer: ["Future Simple Passive:","Present Simple Passive:","Образование Passive Voice:"], hint: "Ищите термины, которые встречаются в уроке Passive Voice" },
      { type: 'quiz', question: "Что является основным понятием урока \"Passive Voice\"?", options: ["Предлог BY:","Future Simple Passive:","Past Simple Passive:","**Active:** *People speak English all over the world","The letter was sent yesterday."], correctAnswer: "**Active:** *People speak English all over the world", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Conditionals: Zero and First 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Present Perfect vs Past Simple:","Виды чтения:","Unless you hurry, you'll miss the bus.","Вопросы:","Основные случаи употребления:"], correctAnswer: "Unless you hurry, you'll miss the bus.", hint: "Этот термин связан с темой: Conditionals: Zero and First" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Conditionals: Zero and First\"?", options: ["Understanding reference:","Структура First Conditional:","Образование Passive Voice:","Вопросы:","Слова-маркеры:"], correctAnswer: "Структура First Conditional:", hint: "Ответ связан с уроком: Conditionals: Zero and First" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Conditionals: Zero and First\"?", options: ["Going to vs Present Continuous для планов:","Tower","Примеры:","Образование:","Спорт:"], correctAnswer: "Tower", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Conditionals: Zero and First\":", options: ["First Conditional — реальные условия:","Zero Conditional — факты и истины:","Unless = If not:","Примеры:","When vs If:","Вариации Main Clause:"], correctAnswer: ["Unless = If not:","Zero Conditional — факты и истины:","Примеры:"], hint: "Ищите термины, которые встречаются в уроке Conditionals: Zero and First" },
      { type: 'quiz', question: "Что является основным понятием урока \"Conditionals: Zero and First\"?", options: ["First Conditional — реальные условия:","* - *If I'm tired","If you heat water to 100°C, it boils.","Unless = If not:","Zero Conditional — факты и истины:"], correctAnswer: "* - *If I'm tired", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Conditionals: Second and Third 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Present Simple","If I had a million dollars, I would buy a house.","-----|-----------|--------|-----","Сочетание с Past Simple:","Образование:"], correctAnswer: "If I had a million dollars, I would buy a house.", hint: "Этот термин связан с темой: Conditionals: Second and Third" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Conditionals: Second and Third\"?", options: ["Zero Conditional — факты и истины:","SHOULD — совет, рекомендация:","Таблица условных предложений:","Future Simple (will + V)","Образование Passive Voice:"], correctAnswer: "Таблица условных предложений:", hint: "Ответ связан с уроком: Conditionals: Second and Third" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Conditionals: Second and Third\"?", options: ["Образование:","Guessing meaning:","Second Conditional для советов:","offer","Основные случаи употребления:"], correctAnswer: "offer", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Conditionals: Second and Third\":", options: ["Second Conditional — нереальные условия в настоящем:","Third Conditional — нереальные условия в прошлом:","Таблица условных предложений:","Важно:","Примеры:","Second Conditional для советов:"], correctAnswer: ["Third Conditional — нереальные условия в прошлом:","Second Conditional для советов:","Важно:"], hint: "Ищите термины, которые встречаются в уроке Conditionals: Second and Third" },
      { type: 'quiz', question: "Что является основным понятием урока \"Conditionals: Second and Third\"?", options: ["Third Conditional — нереальные условия в прошлом:","* - *If I were you","Важно:","If I had a million dollars, I would buy a house.","-----|-----------|--------|-----"], correctAnswer: "* - *If I were you", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Daily Routine 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"get up — вставать...\"?", options: ["get up","Основные случаи употребления:","Zero Conditional — факты и истины:","Примеры:","Understanding reference:"], correctAnswer: "get up", hint: "Этот термин связан с темой: Daily Routine" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Daily Routine\"?", options: ["Слова-маркеры:","Примеры:","Основные случаи употребления:","1. Skimming (Просмотровое чтение):","Предлоги времени:"], correctAnswer: "Предлоги времени:", hint: "Ответ связан с уроком: Daily Routine" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Daily Routine\":", options: ["Предлоги времени:","Примеры:","Утро (Morning):","Vocabulary: Daily Routine (Повседневные дела)","Вечер (Evening):","День (Day):"], correctAnswer: ["Примеры:","Vocabulary: Daily Routine (Повседневные дела)","День (Day):"], hint: "Ищите термины, которые встречаются в уроке Daily Routine" },
      { type: 'quiz', question: "Что является основным понятием урока \"Daily Routine\"?", options: ["leave home","Утро (Morning):","come home","Vocabulary: Daily Routine (Повседневные дела)","* - *In the evening I watch TV or read a book"], correctAnswer: "* - *In the evening I watch TV or read a book", hint: "Ответ содержится в описании урока" },
      { type: 'quiz', question: "Вопрос 5 по теме \"Daily Routine\"", options: ["Will vs Going to:","Предлог BY:","Примеры:","go to school/work","Предлоги времени:"], correctAnswer: "Предлоги времени:", hint: "Ответ связан с материалом урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Hobbies and Free Time 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"sing — петь...\"?", options: ["Глаголы, не употребляющиеся в Continuous:","First Conditional — реальные условия:","MAY — вероятность, разрешение (формально):","Going to vs Present Continuous для планов:","sing"], correctAnswer: "sing", hint: "Этот термин связан с темой: Hobbies and Free Time" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Hobbies and Free Time\"?", options: ["CAN — физическая возможность, умение:","Образование:","Примеры:","read books / magazines","Вопросы о хобби:"], correctAnswer: "Вопросы о хобби:", hint: "Ответ связан с уроком: Hobbies and Free Time" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Hobbies and Free Time\":", options: ["Вопросы о хобби:","Музыкальные инструменты:","Примеры:","Виды хобби:","Vocabulary: Hobbies and Free Time (Хобби и свободное время)","Спорт:"], correctAnswer: ["Музыкальные инструменты:","Vocabulary: Hobbies and Free Time (Хобби и свободное время)","Примеры:"], hint: "Ищите термины, которые встречаются в уроке Hobbies and Free Time" },
      { type: 'quiz', question: "Что является основным понятием урока \"Hobbies and Free Time\"?", options: ["watch films / series","* - *He's fond of playing football","play football / tennis / basketball","play the piano","Музыкальные инструменты:"], correctAnswer: "* - *He's fond of playing football", hint: "Ответ содержится в описании урока" },
      { type: 'quiz', question: "Вопрос 5 по теме \"Hobbies and Free Time\"", options: ["Модальные глаголы в прошедшем времени:","Вопросы о хобби:","Present Perfect vs Past Simple:","Сочетание с Past Simple:","Полезные приёмы:"], correctAnswer: "Вопросы о хобби:", hint: "Ответ связан с материалом урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Reading Strategies 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"Цель: понять главную идею текста...\"?", options: ["Вопросы:","Когда используется Passive:","Цель","Passive Voice (Страдательный залог)","День (Day):"], correctAnswer: "Цель", hint: "Этот термин связан с темой: Reading Strategies" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Reading Strategies\"?", options: ["Полезные приёмы:","Passive:","Примеры:","Слова-маркеры:","Present Perfect Passive:"], correctAnswer: "Полезные приёмы:", hint: "Ответ связан с уроком: Reading Strategies" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Reading Strategies\"?", options: ["Примеры:","Predicting:","Степени вероятности:","заголовку","Past Continuous"], correctAnswer: "заголовку", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Reading Strategies\":", options: ["Виды чтения:","2. Scanning (Поисковое чтение):","Predicting:","Identifying keywords:","Guessing meaning:","1. Skimming (Просмотровое чтение):"], correctAnswer: ["1. Skimming (Просмотровое чтение):","2. Scanning (Поисковое чтение):","Identifying keywords:"], hint: "Ищите термины, которые встречаются в уроке Reading Strategies" },
      { type: 'quiz', question: "Что является основным понятием урока \"Reading Strategies\"?", options: ["Title","2. Scanning (Поисковое чтение):","Linking words","Reading Strategies (Стратегии чтения)","Skimming (Просмотровое чтение):** - Быстрое прочтение для об"], correctAnswer: "Skimming (Просмотровое чтение):** - Быстрое прочтение для об", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  }
] = [
  // Тема: Present Tenses
  {
    title: "Present Simple",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I ___ to school every day.", options: ["am going", "go", "have gone", "went", "Другой ответ"], correctAnswer: "go", hint: "Regular action = Present Simple" },
      { type: 'quiz', question: "She ___ in London.", options: ["live", "lives", "living", "is living", "Другой ответ"], correctAnswer: "lives", hint: "He/She/It + V+s" },
      { type: 'quiz', question: "My brother ___ (work) in a bank.", options: ["is working", "works", "has worked", "working", "work"], correctAnswer: "works", hint: "He + V+s" },
      { type: 'quiz', question: "___ you like coffee?", options: ["Do", "Does", "Is", "Are", "Другой ответ"], correctAnswer: "Do", hint: "Question with I/you/we/they = Do" }
    ],
    reward: { stars: 3, message: "Excellent! You know Present Simple! 🌟" }
  },
  {
    title: "Present Continuous",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Look! It ___ .", options: ["rains", "is raining", "rained", "has rained", "Другой ответ"], correctAnswer: "is raining", hint: "Happening now = Present Continuous" },
      { type: 'quiz', question: "They ___ football at the moment.", options: ["play", "plays", "are playing", "is playing", "Другой ответ"], correctAnswer: "are playing", hint: "They + are + V-ing" },
      { type: 'quiz', question: "I am ___ (read) a book now.", options: ["readed", "reader", "read", "reading", "reads"], correctAnswer: "reading", hint: "am + V-ing" },
      { type: 'quiz', question: "She isn't ___ TV right now.", options: ["watch", "watches", "watching", "watched", "Другой ответ"], correctAnswer: "watching", hint: "isn't + V-ing" }
    ],
    reward: { stars: 3, message: "Great! You understand Present Continuous! ⏰" }
  },
  {
    title: "Present Perfect",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "She ___ in London for 5 years.", options: ["lives", "is living", "has lived", "lived", "Другой ответ"], correctAnswer: "has lived", hint: "For + period = Present Perfect" },
      { type: 'quiz', question: "I have ___ (see) this film already.", options: ["been", "seeing", "see", "seen", "saw"], correctAnswer: "seen", hint: "Present Perfect uses V3" },
      { type: 'quiz', question: "Have you ever ___ to Paris?", options: ["be", "been", "being", "was", "Другой ответ"], correctAnswer: "been", hint: "Have + V3 (be → been)" },
      { type: 'quiz', question: "I have known him ___ 2015.", options: ["for", "since", "at", "in", "Другой ответ"], correctAnswer: "since", hint: "Since + point in time" }
    ],
    reward: { stars: 3, message: "Perfect! You know Present Perfect! ✅" }
  },
  // Тема: Past Tenses
  {
    title: "Past Simple",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "We ___ to the cinema yesterday.", options: ["go", "are going", "went", "have gone", "Другой ответ"], correctAnswer: "went", hint: "Yesterday = Past Simple" },
      { type: 'quiz', question: "Did she ___ (come) to the party?", options: ["comes", "came", "has come", "come", "coming"], correctAnswer: "come", hint: "Did + base form" },
      { type: 'quiz', question: "He ___ his homework last night.", options: ["doesn", ",", "t do", "didn", "—"], correctAnswer: "didn't do", hint: "didn't + base form" },
      { type: 'quiz', question: "They were ___ home yesterday.", options: ["at", "in", "on", "to", "Другой ответ"], correctAnswer: "at", hint: "at home" }
    ],
    reward: { stars: 3, message: "Great job! You understand Past Simple! ⏮️" }
  },
  {
    title: "Past Continuous",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "At 5 o'clock yesterday I ___ TV.", options: ["watched", "was watching", "have watched", "watch", "Другой ответ"], correctAnswer: "was watching", hint: "At specific time in the past = Past Continuous" },
      { type: 'quiz', question: "When the phone rang, I ___ .", options: ["slept", "was sleeping", "have slept", "sleep", "Другой ответ"], correctAnswer: "was sleeping", hint: "Interrupted action = Past Continuous" },
      { type: 'quiz', question: "They were ___ (play) football at that time.", options: ["plays", "play", "played", "playing", "to play"], correctAnswer: "playing", hint: "were + V-ing" },
      { type: 'quiz', question: "While she ___ (cook), the phone rang.", options: ["cooked", "was cooking", "cooks", "has cooked", "Другой ответ"], correctAnswer: "was cooking", hint: "While = ongoing action in past" }
    ],
    reward: { stars: 3, message: "Excellent! You know Past Continuous! 🕐" }
  },
  // Тема: Future Tenses
  {
    title: "Future Simple",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I think it ___ rain tomorrow.", options: ["will", "is going to", "would", "shall", "Другой ответ"], correctAnswer: "will", hint: "Prediction = will" },
      { type: 'quiz', question: "I ___ help you with your homework.", options: ["will", "am going to", "was", "had", "Другой ответ"], correctAnswer: "will", hint: "Promise = will" },
      { type: 'quiz', question: "She won't ___ (tell) anyone.", options: ["told", "telling", "tells", "has told", "tell"], correctAnswer: "tell", hint: "won't + base form" },
      { type: 'quiz', question: "___ you come to the party?", options: ["Will", "Are", "Do", "Did", "Другой ответ"], correctAnswer: "Will", hint: "Future question = Will + subject + V" }
    ],
    reward: { stars: 3, message: "Well done! You know Future Simple! 🔮" }
  },
  {
    title: "To be going to",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Look at the clouds! It ___ rain.", options: ["will", "is going to", "would", "shall", "Другой ответ"], correctAnswer: "is going to", hint: "Evidence now = going to" },
      { type: 'quiz', question: "I'm going ___ (study) tonight.", options: ["to study", "studying", "studied", "has studied", "study"], correctAnswer: "to study", hint: "going to + V" },
      { type: 'quiz', question: "She is ___ buy a new car.", options: ["will", "going to", "will to", "going", "Другой ответ"], correctAnswer: "going to", hint: "is going to + V" },
      { type: 'quiz', question: "What are you ___ do tomorrow?", options: ["will", "going to", "would", "shall", "Другой ответ"], correctAnswer: "going to", hint: "are going to + V" }
    ],
    reward: { stars: 3, message: "Great! You understand 'going to'! 📅" }
  },
  // Тема: Modal Verbs
  {
    title: "Modal Verbs: Can, Could, Must",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "You ___ smoke here. It's forbidden.", options: ["mustn", "can", "Другой ответ", "t", ","], correctAnswer: "mustn't", hint: "Forbidden = mustn't" },
      { type: 'quiz', question: "She can ___ (speak) three languages.", options: ["speaking", "has spoken", "speak", "spoke", "speaks"], correctAnswer: "speak", hint: "can + base form" },
      { type: 'quiz', question: "___ you help me, please?", options: ["Can", "Must", "Should", "Have to", "Другой ответ"], correctAnswer: "Can", hint: "Request = Can/Could" },
      { type: 'quiz', question: "You ___ wear a uniform at school.", options: ["can", "must", "should", "may", "Другой ответ"], correctAnswer: "must", hint: "Obligation = must" }
    ],
    reward: { stars: 3, message: "Perfect! You understand Can, Could, Must! ✨" }
  },
  {
    title: "Modal Verbs: Should, May, Might",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "You ___ see a doctor. You look ill.", options: ["can", "must", "should", "may", "Другой ответ"], correctAnswer: "should", hint: "Advice = should" },
      { type: 'quiz', question: "It ___ rain tomorrow. (possibility)", options: ["must", "should", "may", "have to", "Другой ответ"], correctAnswer: "may", hint: "Possibility = may/might" },
      { type: 'quiz', question: "You shouldn't ___ (eat) so much sugar.", options: ["eat", "eating", "has eaten", "ate", "to eat"], correctAnswer: "eat", hint: "shouldn't + base form" },
      { type: 'quiz', question: "___ I use your phone?", options: ["Must", "Should", "May", "Have to", "Другой ответ"], correctAnswer: "May", hint: "Formal request = May" }
    ],
    reward: { stars: 3, message: "Excellent! You know Should, May, Might! 💡" }
  },
  // Тема: Passive Voice
  {
    title: "Passive Voice",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "English ___ all over the world.", options: ["speaks", "is spoken", "spoke", "is speaking", "Другой ответ"], correctAnswer: "is spoken", hint: "Present Simple Passive" },
      { type: 'quiz', question: "The letter ___ yesterday.", options: ["sent", "was sent", "is sent", "sends", "Другой ответ"], correctAnswer: "was sent", hint: "Past Simple Passive" },
      { type: 'quiz', question: "The book will be ___ (finish) soon.", options: ["finishing", "finished", "to finish", "finishes", "finish"], correctAnswer: "finished", hint: "will be + V3" },
      { type: 'quiz', question: "This picture was painted ___ Picasso.", options: ["with", "by", "from", "of", "Другой ответ"], correctAnswer: "by", hint: "Agent = by" }
    ],
    reward: { stars: 3, message: "Excellent! You know Passive Voice! 📝" }
  },
  // Тема: Conditionals
  {
    title: "Conditionals: Zero and First",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "If you heat water to 100°C, it ___.", options: ["will boil", "would boil", "boils", "boiled", "Другой ответ"], correctAnswer: "boils", hint: "Zero Conditional = fact" },
      { type: 'quiz', question: "If it rains, I ___ at home.", options: ["stay", "will stay", "would stay", "stayed", "Другой ответ"], correctAnswer: "will stay", hint: "First Conditional" },
      { type: 'quiz', question: "If you don't hurry, you'll miss the bus. = ___ you hurry, you'll miss the bus.", options: ["When", "Before", "Unless", "After", "If"], correctAnswer: "Unless", hint: "Unless = If not" },
      { type: 'quiz', question: "If she ___ (come), I will be happy.", options: ["comes", "will come", "came", "would come", "Другой ответ"], correctAnswer: "comes", hint: "If + Present Simple" }
    ],
    reward: { stars: 3, message: "Great! You understand Zero and First Conditionals! 🔀" }
  },
  {
    title: "Conditionals: Second and Third",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "If I were you, I ___ accept.", options: ["will", "would", "would have", "had", "Другой ответ"], correctAnswer: "would", hint: "Second Conditional" },
      { type: 'quiz', question: "If I had known, I ___ have told you.", options: ["would", "have", "t", "had", "will"], correctAnswer: "would", hint: "Third Conditional" },
      { type: 'quiz', question: "If I ___ (be) you, I would study harder.", options: ["am", "was", "were", "be", "Другой ответ"], correctAnswer: "were", hint: "Second Conditional uses 'were' for all persons" },
      { type: 'quiz', question: "If she ___ (study) harder, she would have passed.", options: ["studies", "studied", "had studied", "would study", "Другой ответ"], correctAnswer: "had studied", hint: "Third Conditional: If + Past Perfect" }
    ],
    reward: { stars: 3, message: "Perfect! You know Second and Third Conditionals! 🎯" }
  },
  // Тема: Vocabulary: Daily Life
  {
    title: "Daily Routine",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I usually ___ at 7 o'clock.", options: ["wake up", "get up", "go to bed", "have dinner", "Другой ответ"], correctAnswer: "wake up", hint: "Morning activity" },
      { type: 'quiz', question: "I have breakfast ___ the morning. (preposition)", options: ["in", "at", "by", "on", "for"], correctAnswer: "in", hint: "in the morning" },
      { type: 'quiz', question: "After school I ___ my homework.", options: ["make", "do", "have", "take", "Другой ответ"], correctAnswer: "do", hint: "do homework" },
      { type: 'quiz', question: "I go ___ bed at 10 p.m.", options: ["at", "in", "to", "on", "Другой ответ"], correctAnswer: "to", hint: "go to bed" }
    ],
    reward: { stars: 3, message: "Excellent! You know Daily Routine vocabulary! 🌅" }
  },
  {
    title: "Hobbies and Free Time",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "She can play ___ piano.", options: ["a", "an", "the", "-", "Другой ответ"], correctAnswer: "the", hint: "play THE piano (instrument)" },
      { type: 'quiz', question: "In my free time I like ___ (read) books.", options: ["to reading", "reader", "read", "reading", "reads"], correctAnswer: "reading", hint: "like + V-ing" },
      { type: 'quiz', question: "He's fond ___ playing football.", options: ["in", "on", "of", "at", "Другой ответ"], correctAnswer: "of", hint: "fond of" },
      { type: 'quiz', question: "What do you do ___ your free time?", options: ["in", "on", "at", "for", "Другой ответ"], correctAnswer: "in", hint: "in your free time" }
    ],
    reward: { stars: 3, message: "Great! You know Hobbies vocabulary! 🎨" }
  },
  // Тема: Reading Comprehension
  {
    title: "Reading Strategies",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "___ reading is for general understanding.", options: ["Detailed", "Scanning", "Skimming", "Intensive", "Другой ответ"], correctAnswer: "Skimming", hint: "Skimming = quick reading for gist" },
      { type: 'quiz', question: "___ reading is looking for specific information.", options: ["Detailed", "Scanning", "Skimming", "Extensive", "Другой ответ"], correctAnswer: "Scanning", hint: "Scanning = searching for details" },
      { type: 'quiz', question: "The three parts of a text are: Introduction, Body paragraphs, and ___.", options: ["Result", "Conclusion", "Output", "Summary", "Finish"], correctAnswer: "Conclusion", hint: "Text structure" },
      { type: 'quiz', question: "What does 'predicting' mean?", options: ["Guessing meaning from context", "Predicting content from title", "Finding keywords", "Understanding pronouns", "Другой ответ"], correctAnswer: "Predicting content from title", hint: "Before reading strategy" }
    ],
    reward: { stars: 3, message: "Perfect! You understand Reading Strategies! 📖" }
  }
]
