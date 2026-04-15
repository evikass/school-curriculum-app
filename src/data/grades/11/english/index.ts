import { SubjectData, GameLesson } from '@/data/types'

const L = (title: string, description: string, tasks: string[], content?: string, examples?: string[], facts?: string[], keyPoints?: string[]) => ({ 
  title, description, tasks, content, examples, facts, keyPoints
})

export const lessons: SubjectData = {
  title: "Английский язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: ["Advanced Grammar", "Academic Vocabulary", "Essay Writing", "Communication"],
  detailedTopics: [
    {
      topic: "Продвинутая грамматика",
      lessons: [
        L("Урок 1: Mixed Conditionals", "Смешанные условные предложения.", [
          "Mixed Conditional: II + III",
          "Mixed Conditional: III + II",
          "Отличие от стандартных Conditionals",
          "Употребление в речи"
        ],
        "**Mixed Conditionals** — смешанные условные предложения.\n\nСочетают части разных типов Conditionals.\n\n---\n\n**Mixed Conditional: II + III**\n\n**Структура:**\nIf + Past Perfect, would + V\n\n**Значение:**\n- Условие в прошлом (III)\n- Результат в настоящем (II)\n\n**Примеры:**\n- If I had studied harder at school, I would have a better job now.\n  (Если бы я учился лучше в школе, у меня была бы лучшая работа сейчас)\n  \n- If she hadn't missed the train, she would be here now.\n  (Если бы она не опоздала на поезд, она была бы здесь сейчас)\n\n---\n\n**Mixed Conditional: III + II**\n\n**Структура:**\nIf + Past Simple, would have + V3\n\n**Значение:**\n- Условие в настоящем/общее (II)\n- Результат в прошлом (III)\n\n**Примеры:**\n- If I were braver, I would have jumped.\n  (Если бы я был смелее, я бы прыгнул)\n  \n- If she spoke French, she would have got that job.\n  (Если бы она говорила по-французски, она бы получила ту работу)\n\n---\n\n**Таблица смешанных Conditionals:**\n\n| Тип | Условие | Результат | Пример |\n|-----|---------|-----------|--------|\n| II+III | Past Perfect | would + V | If I had saved money, I would buy a car now. |\n| III+II | Past Simple | would have + V3 | If I were you, I would have accepted. |\n\n---\n\n**Инверсия в Conditionals:**\n\nБез IF:\n- If I were you → Were I you\n- If I had known → Had I known\n- If it should rain → Should it rain\n\n**Примеры:**\n- Were I rich, I would travel the world.\n- Had I known, I would have come.\n- Should you need help, call me.",
        ["If I had studied, I would have a degree now. (II+III)", "If I were you, I would have done it differently. (III+II)", "Had I known... = If I had known..."],
        ["Mixed Conditionals связывают прошлое с настоящим", "Инверсия делает речь более формальной", "Без 'if' предложение звучит литературнее"],
        [
          "If + Past Perfect, would + V — условие в прошлом, результат сейчас",
          "If + Past Simple, would have + V3 — условие сейчас, результат в прошлом",
          "Инверсия: Had I known = If I had known"
        ]),
        L("Урок 2: Inversion", "Инверсия в английском языке.", [
          "Грамматическая инверсия",
          "Инверсия после отрицательных наречий",
          "Инверсия в Conditionals",
          "Стилистическая инверсия"
        ],
        "**Inversion** — изменение обычного порядка слов в предложении.\n\nОбычный порядок: Подлежащее + Сказуемое\nИнверсия: Сказуемое (часть) + Подлежащее\n\n---\n\n**1. Инверсия после отрицательных наречий:**\n\nКогда отрицательное наречие стоит в начале предложения.\n\n**Отрицательные наречия:**\n- never (никогда)\n- rarely, seldom (редко)\n- hardly, scarcely (едва)\n- little (мало)\n- nowhere (нигде)\n\n**Структура:**\nОтрицательное слово + вспомогательный глагол + подлежащее\n\n**Примеры:**\n- Never have I seen such a beautiful sunset.\n  (Никогда я не видел такого красивого заката)\n  \n- Rarely does she make mistakes.\n  (Редко она делает ошибки)\n  \n- Seldom do we go to the cinema.\n  (Редко мы ходим в кино)\n\n---\n\n**2. Инверсия с 'only':**\n\n**Структура:**\nOnly + обстоятельство + вспомогательный глагол + подлежащее\n\n**Примеры:**\n- Only after the meeting did I realize my mistake.\n  (Только после встречи я понял свою ошибку)\n  \n- Only then did she understand the truth.\n  (Только тогда она поняла правду)\n\n---\n\n**3. Инверсия с 'not only... but also':**\n\n**Примеры:**\n- Not only did he arrive late, but he also forgot his documents.\n  (Он не только опоздал, но и забыл документы)\n\n---\n\n**4. Инверсия с 'so' и 'neither/nor':**\n\n**Примеры:**\n- She likes coffee. So do I.\n  (Она любит кофе. Я тоже.)\n  \n- He doesn't speak French. Neither do I.\n  (Он не говорит по-французски. Я тоже.)\n\n---\n\n**5. Инверсия с 'no sooner... than':**\n\n**Примеры:**\n- No sooner had I arrived than it started to rain.\n  (Едва я прибыл, как начался дождь)\n\n---\n\n**6. Инверсия в Conditionals:**\n\nБез 'if':\n- Were I you, I would accept. (If I were you)\n- Had I known, I would have come. (If I had known)\n- Should you need help, call me. (If you should need help)",
        ["Never have I seen... = Я никогда не видел...", "Only then did I understand... = Только тогда я понял...", "So do I = Я тоже; Neither do I = Я тоже нет"],
        ["Инверсия делает речь формальной и выразительной", "Используется в литературе и публичных выступлениях", "В обычной речи чаще используют обычный порядок слов"],
        [
          "Инверсия после отрицательных наречий: Never have I...",
          "Only then did I... — инверсия с 'only'",
          "So do I / Neither do I — согласие"
        ]),
        L("Урок 3: Subjunctive Mood", "Сослагательное наклонение.", [
          "Present Subjunctive",
          "Past Subjunctive",
          "Использование после глаголов и прилагательных",
          "Формальное и разговорное употребление"
        ],
        "**Subjunctive Mood** — сослагательное наклонение.\n\nВыражает желание, рекомендацию, необходимость.\n\n---\n\n**1. Present Subjunctive:**\n\n**Форма:** инфинитив без 'to' (base form) для всех лиц.\n\n**Использование:**\n- После глаголов: suggest, recommend, insist, demand, require, order\n- После прилагательных: essential, important, necessary, vital, imperative\n- После выражений: it's time, I wish, would rather\n\n**Примеры:**\n- I suggest that he be more careful.\n  (Я предлагаю, чтобы он был осторожнее)\n  \n- It is essential that she be present.\n  (Необходимо, чтобы она присутствовала)\n  \n- The doctor recommended that he take a rest.\n  (Врач рекомендовал ему отдохнуть)\n\n**Важно:** 'be' и 'take' — без окончаний!\n\n---\n\n**2. Past Subjunctive:**\n\n**Использование:**\n- После 'wish' для сожаления о настоящем\n- После 'as if', 'as though'\n- В структуре 'it's time'\n\n**Примеры:**\n- I wish I were rich. (Жаль, что я не богат)\n- He talks as if he knew everything. (Он говорит так, будто всё знает)\n- It's time we left. (Пора нам уходить)\n\n**Важно:** 'were' для всех лиц!\n\n---\n\n**3. Wish + разные формы:**\n\n| Конструкция | Значение | Пример |\n|-------------|----------|--------|\n| wish + Past Simple | Сожаление о настоящем | I wish I knew. |\n| wish + Past Perfect | Сожаление о прошлом | I wish I had known. |\n| wish + would | Недовольство, желание изменений | I wish you would stop. |\n\n**Примеры:**\n- I wish I spoke French. (Жаль, что я не говорю по-французски)\n- I wish I had studied harder. (Жаль, что я не учился лучше)\n- I wish you would be quiet. (Хотелось бы, чтобы ты помолчал)\n\n---\n\n**4. Would rather / Had better:**\n\n**Would rather + V:** предпочтение\n- I would rather stay at home. (Я бы лучше остался дома)\n\n**Would rather + Past Simple:** предпочтение о другом человеке\n- I would rather you stayed. (Я бы предпочёл, чтобы ты остался)\n\n**Had better + V:** совет, предупреждение\n- You had better study. (Тебе лучше учиться)",
        ["I suggest he be careful. (сослагательное)", "I wish I were... (форма were для всех)", "I wish I had known... (сожаление о прошлом)"],
        ["Present Subjunctive использует базовую форму глагола", "В разговорной речи часто заменяется на should + V", "'I wish I was' допустимо в разговорной речи, но 'were' — правильно"],
        [
          "Present Subjunctive: I suggest that he be...",
          "Past Subjunctive: I wish I were... (were для всех)",
          "Wish + Past Perfect — сожаление о прошлом"
        ]),
        L("Урок 4: Complex Structures", "Сложные грамматические конструкции.", [
          "Cleft sentences",
          "Inversion with adverbs",
          "Participle clauses",
          "Advanced sentence structures"
        ],
        "**Сложные грамматические конструкции:**\n\n**1. Cleft Sentences (расщеплённые предложения):**\n\n**It-cleft:**\nIt + be + выделяемый элемент + that/who\n\n**Примеры:**\n- It was John who broke the window.\n  (Именно Джон разбил окно)\n  \n- It is this book that I recommend.\n  (Именно эту книгу я рекомендую)\n\n**Wh-cleft:**\nWhat + clause + be + X\n\n**Примеры:**\n- What I need is a cup of coffee.\n  (То, что мне нужно — чашка кофе)\n  \n- What surprises me is his attitude.\n  (Что меня удивляет — его отношение)\n\n---\n\n**2. Participle Clauses (причастные обороты):**\n\n**Present Participle (-ing):**\n- Active действие\n- Walking down the street, I met an old friend.\n  (Гуляя по улице, я встретил старого друга)\n\n**Past Participle (-ed/irregular):**\n- Passive действие\n- Written in 1960, the book became a classic.\n  (Написанная в 1960 году, книга стала классикой)\n\n**Perfect Participle (having + V3):**\n- Действие завершено до другого\n- Having finished the work, he went home.\n  (Закончив работу, он пошёл домой)\n\n---\n\n**3. So / Such... that:**\n\n**So + прилагательное/наречие + that:**\n- He was so tired that he fell asleep immediately.\n\n**Such + (a/an) + существительное + that:**\n- It was such a good movie that I watched it twice.\n\n---\n\n**4. Too / Enough:**\n\n**Too + прилагательное/наречие + to + V:**\n- He is too young to drive. (Слишком молод, чтобы водить)\n\n**Прилагательное/наречие + enough + to + V:**\n- He is old enough to vote. (Достаточно взрослый, чтобы голосовать)\n\n---\n\n**5. Demonstrative + of + possessive:**\n\n- That brother of yours is annoying.\n  (Этот твой брат раздражает)\n  \n- This idea of mine might work.\n  (Эта моя идея может сработать)",
        ["It was John who... = Именно Джон...", "Walking down the street, I... = Гуляя по улице, я...", "He was so tired that... = Он был так уставшим, что..."],
        ["Cleft sentences выделяют важную информацию", "Participle clauses делают речь более плавной", "Эти конструкции типичны для письменной речи"],
        [
          "Cleft sentences: It was John who... = Именно Джон...",
          "Participle clauses: Walking..., Written...",
          "Too... to / enough to — степень"
        ])
      ]
    },
    {
      topic: "Академическая лексика",
      lessons: [
        L("Урок 5: Academic Vocabulary", "Академическая и научная лексика.", [
          "Слова для академического письма",
          "Связующие слова для эссе",
          "Фразы для аргументации",
          "Научный стиль"
        ],
        "**Академическая лексика** — слова для научного и формального письма.\n\n**Глаголы для академического письма:**\n\n| Глагол | Значение | Пример |\n|--------|----------|--------|\n| analyse | анализировать | analyse the data |\n| assess | оценивать | assess the impact |\n| claim | утверждать | claim that... |\n| demonstrate | демонстрировать | demonstrate the effects |\n| evaluate | оценивать | evaluate the results |\n| imply | подразумевать | imply that... |\n| indicate | указывать | indicate a trend |\n| maintain | утверждать | maintain that... |\n| propose | предлагать | propose a theory |\n| suggest | предлагать | suggest that... |\n\n---\n\n**Существительные для академического письма:**\n\n| Слово | Значение | Пример |\n|-------|----------|--------|\n| approach | подход | a new approach |\n| aspect | аспект | this aspect of... |\n| assumption | предположение | this assumption is... |\n| concept | концепция | the concept of... |\n| context | контекст | in this context |\n| factor | фактор | a key factor |\n| issue | проблема | a controversial issue |\n| perspective | перспектива | from this perspective |\n| significance | значимость | of great significance |\n| tendency | тенденция | a tendency to... |\n\n---\n\n**Связующие слова для эссе:**\n\n**Введение темы:**\n- The purpose of this essay is to...\n- This paper aims to discuss...\n- The issue of... has become increasingly important.\n\n**Добавление информации:**\n- Furthermore, ... / Moreover, ...\n- In addition, ... / Additionally, ...\n- Another significant point is that...\n\n**Противопоставление:**\n- However, ... / Nevertheless, ...\n- On the other hand, ...\n- Despite this, ... / In spite of this, ...\n\n**Причина и следствие:**\n- Consequently, ... / As a result, ...\n- Therefore, ... / Thus, ...\n- This leads to... / This results in...\n\n**Примеры:**\n- For instance, ... / For example, ...\n- To illustrate, ...\n- A case in point is...\n\n**Заключение:**\n- In conclusion, ... / To conclude, ...\n- In summary, ... / To sum up, ...\n- Overall, it can be seen that...",
        ["analyse, assess, evaluate — ключевые академические глаголы", "Furthermore, Moreover, However — связующие слова", "In conclusion, To sum up — для заключения"],
        ["Академический стиль избегает сокращений (don't → do not)", "Предпочтение пассивному залогу в научных текстах", "Формальные слова вместо разговорных (get → obtain)"],
        [
          "Ключевые глаголы: analyse, assess, evaluate",
          "Связующие слова: furthermore, moreover, however",
          "Заключение: in conclusion, to sum up"
        ]),
        L("Урок 6: Essay Writing", "Написание эссе.", [
          "Структура эссе",
          "Введение и тезис",
          "Основная часть и аргументы",
          "Заключение"
        ],
        "**Структура эссе:**\n\n**1. Introduction (Введение)**\n\n**Компоненты:**\n- General statement (общее введение в тему)\n- Background information (контекст)\n- Thesis statement (тезис — главная мысль)\n\n**Пример введения:**\n\"In recent years, the issue of climate change has become increasingly prominent in public discourse. With rising global temperatures and extreme weather events, governments and individuals are facing critical decisions about environmental policy. This essay will examine the causes of climate change and evaluate potential solutions.\"\n\n---\n\n**2. Body Paragraphs (Основная часть)**\n\n**Структура абзаца:**\n1. Topic sentence (тематическое предложение)\n2. Supporting sentences (поддерживающие предложения)\n3. Evidence/examples (доказательства/примеры)\n4. Concluding sentence (заключительное предложение)\n\n**Пример абзаца:**\n\"One significant cause of climate change is the burning of fossil fuels. When coal, oil, and natural gas are burned for energy, they release carbon dioxide into the atmosphere. For instance, the transportation sector accounts for approximately 24% of global CO2 emissions. This accumulation of greenhouse gases contributes to the warming of the planet.\"\n\n---\n\n**3. Conclusion (Заключение)**\n\n**Компоненты:**\n- Restate thesis (переформулировать тезис)\n- Summarize main points (обобщить основные пункты)\n- Final thought/recommendation (финальная мысль)\n\n**Пример заключения:**\n\"In conclusion, climate change is driven primarily by human activities, particularly the burning of fossil fuels and deforestation. While the challenges are significant, solutions such as renewable energy adoption and reforestation offer hope for the future. It is essential that both governments and individuals take immediate action to address this global crisis.\"\n\n---\n\n**Типы эссе:**\n\n| Тип | Цель | Структура |\n|-----|------|-----------|\n| Opinion | Выразить мнение | Введение + 2-3 аргумента + Заключение |\n| Discussion | Обсудить обе стороны | Введение + Аргументы за + Аргументы против + Заключение |\n| Problem-Solution | Проблема и решение | Введение + Проблема + Решения + Заключение |\n| Advantages-Disadvantages | Плюсы и минусы | Введение + Преимущества + Недостатки + Заключение |",
        ["Introduction: General statement → Thesis", "Body: Topic sentence → Evidence → Concluding sentence", "Conclusion: Restate thesis → Summarize → Final thought"],
        ["Тезис — самая важная часть введения", "Каждый абзац — одна главная идея", "Заключение НЕ должно содержать новой информации"],
        [
          "Структура: Introduction → Body → Conclusion",
          "Topic sentence — главная мысль абзаца",
          "Тезис — центральная идея эссе"
        ]),
        L("Урок 7: Debating Skills", "Навыки дебатов и дискуссий.", [
          "Структура дебатов",
          "Аргументация",
          "Опровержение",
          "Риторические приёмы"
        ],
        "**Структура дебатов:**\n\n**Типичная структура:**\n1. Opening statements (вступительные заявления)\n2. Arguments (аргументы)\n3. Rebuttal (опровержение)\n4. Closing statements (заключительные заявления)\n\n---\n\n**Выражения для дебатов:**\n\n**Представление аргумента:**\n- The first point I'd like to make is...\n- My primary argument is that...\n- There are several reasons why I believe...\n- Let me begin by stating...\n\n**Поддержка аргумента:**\n- Research has shown that...\n- According to recent studies...\n- For instance, ... / For example, ...\n- This is illustrated by...\n\n**Опровержение:**\n- While it may be true that..., I would argue that...\n- I understand the point about..., however...\n- That's an interesting perspective, but...\n- I see your point, but I must disagree because...\n- The evidence actually suggests otherwise...\n\n**Заключение:**\n- In conclusion, I strongly believe that...\n- To summarise my position...\n- For these reasons, I urge you to support/oppose...\n\n---\n\n**Логические ошибки (Logical Fallacies):**\n\n**1. Ad Hominem** — атака на личность\n- «Ты не можешь быть прав, ты даже не учился в университете!»\n\n**2. Straw Man** — искажение аргумента оппонента\n- «Ты хочешь открыть границы? Значит, ты хочешь уничтожить нашу страну!»\n\n**3. False Dichotomy** — ложная дилемма\n- «Или ты с нами, или против нас!»\n\n**4. Slippery Slope** — скользкая дорожка\n- «Если разрешить это, то всё рухнет!»\n\n**5. Appeal to Authority** — обращение к авторитету\n- «Знаменитый актёр сказал, что это правда!»\n\n---\n\n**Риторические приёмы:**\n\n**Rhetorical questions:**\n- Can we really afford to ignore this problem?\n\n**Repetition:**\n- We need change. We need progress. We need action.\n\n**Tripling (правило трёх):**\n- Government of the people, by the people, for the people.",
        ["My primary argument is that... — Мой главный аргумент...", "I see your point, but... — Я понимаю вашу точку зрения, но...", "In conclusion, I strongly believe that... — В заключение, я твёрдо верю, что..."],
        ["Избегайте логических ошибок в аргументах", "Приводите доказательства и примеры", "Уважайте противоположную точку зрения"],
        [
          "My primary argument is that... — представление аргумента",
          "I see your point, but I disagree — опровержение",
          "Избегайте логических ошибок в аргументах"
        ])
      ]
    },
    {
      topic: "Карьера и общение",
      lessons: [
        L("Урок 8: Business English", "Деловой английский.", [
          "Деловая переписка",
          "Презентации",
          "Переговоры",
          "Деловой этикет"
        ],
        "**Деловая переписка:**\n\n**Структура делового письма:**\n\n1. **Salutation (приветствие):**\n- Dear Mr./Ms. [Last Name],\n- Dear Sir/Madam, (если неизвестно имя)\n\n2. **Opening (открытие):**\n- I am writing to inquire about...\n- I am writing in response to...\n- Thank you for your letter/email regarding...\n\n3. **Body (основная часть):**\n- I would like to request...\n- Please find attached...\n- Could you please provide...?\n\n4. **Closing (закрытие):**\n- I look forward to hearing from you.\n- Please do not hesitate to contact me if you need further information.\n- Thank you for your time and consideration.\n\n5. **Sign-off (подпись):**\n- Yours sincerely, (если знаете имя)\n- Yours faithfully, (если не знаете имя)\n- Best regards, / Kind regards, (менее формально)\n\n---\n\n**Пример делового письма:**\n\nDear Ms. Johnson,\n\nI am writing to apply for the Marketing Manager position advertised on your company website.\n\nWith over five years of experience in digital marketing and a proven track record of increasing brand awareness, I believe I would be a valuable addition to your team. Please find attached my CV and cover letter for your consideration.\n\nI would welcome the opportunity to discuss my application with you further. I am available for an interview at your convenience.\n\nThank you for your time and consideration.\n\nYours sincerely,\n\nJohn Smith\n\n---\n\n**Фразы для презентаций:**\n\n**Введение:**\n- Good morning/afternoon everyone. Thank you for coming.\n- The purpose of my presentation is to...\n- I've divided my presentation into three parts.\n\n**Переходы:**\n- Let's move on to...\n- Now I'd like to discuss...\n- Turning to my next point...\n\n**Визуальные материалы:**\n- As you can see from this chart...\n- This graph shows...\n- Let me draw your attention to...\n\n**Заключение:**\n- To sum up, ... / In conclusion, ...\n- Thank you for your attention.\n- I'd be happy to answer any questions.",
        ["Dear Mr./Ms. [Last Name], ... Yours sincerely,", "I am writing to inquire about... — Я пишу, чтобы узнать о...", "Please find attached... — Пожалуйста, найдите во вложении..."],
        ["Деловой стиль требует формальности", "Отвечайте на письма в течение 24-48 часов", "Всегда проверяйте правописание перед отправкой"],
        [
          "Dear Mr./Ms. [Name], ... Yours sincerely,",
          "I am writing to inquire about...",
          "Please find attached..."
        ]),
        L("Урок 9: Job Interview", "Собеседование на английском.", [
          "Подготовка к собеседованию",
          "Типичные вопросы и ответы",
          "Questions to ask the interviewer",
          "После собеседования"
        ],
        "**Типичные вопросы на собеседовании:**\n\n**1. Tell me about yourself.**\n- I have [number] years of experience in [field].\n- I graduated from [university] with a degree in [subject].\n- My key strengths are [strength 1], [strength 2], and [strength 3].\n\n**2. Why do you want to work for this company?**\n- I admire your company's commitment to [value].\n- I've been following your company's growth and success in [area].\n- This position aligns perfectly with my career goals.\n\n**3. What are your strengths?**\n- I'm a quick learner and adapt easily to new situations.\n- I have strong communication skills.\n- I'm highly organised and meet deadlines consistently.\n\n**4. What are your weaknesses?**\n- I sometimes focus too much on details, but I'm learning to prioritise.\n- I tend to take on too much responsibility, but I'm working on delegation.\n\n**5. Where do you see yourself in 5 years?**\n- I see myself growing with the company and taking on more responsibilities.\n- I hope to develop my skills in [area] and contribute to the team's success.\n\n**6. Why should we hire you?**\n- I bring a unique combination of [skill 1] and [skill 2].\n- I'm passionate about this industry and eager to contribute.\n- My experience in [area] makes me well-suited for this role.\n\n---\n\n**Questions to ask the interviewer:**\n\n- Can you tell me more about the team I'd be working with?\n- What does a typical day look like in this position?\n- What are the biggest challenges facing the team right now?\n- How do you measure success for this role?\n- What opportunities are there for professional development?\n- When can I expect to hear back about the next steps?\n\n---\n\n**Фразы для описания опыта:**\n\n- I was responsible for...\n- I successfully completed...\n- I led a team of [number] people.\n- I increased sales by [percentage].\n- I managed a budget of [amount].\n\n---\n\n**После собеседования:**\n\n**Thank you email:**\n\nDear [Interviewer's Name],\n\nThank you for taking the time to meet with me yesterday. I enjoyed learning more about the [position] role and [Company Name].\n\nOur discussion reinforced my interest in the position, and I am confident that my experience in [area] would enable me to contribute effectively to your team.\n\nPlease don't hesitate to contact me if you need any additional information. I look forward to hearing from you.\n\nBest regards,\n[Your Name]",
        ["Tell me about yourself. — Расскажите о себе.", "What are your strengths? — Ваши сильные стороны?", "Why should we hire you? — Почему мы должны вас нанять?"],
        ["Готовьтесь к собеседованию заранее", "Изучите компанию перед интервью", "Отправьте благодарственное письмо в течение 24 часов"],
        [
          "Tell me about yourself — представление",
          "Thank you email — в течение 24 часов",
          "Изучите компанию перед собеседованием"
        ]),
        L("Урок 10: Presentation Skills", "Навыки презентации.", [
          "Структура презентации",
          "Визуальные материалы",
          "Работа с аудиторией",
          "Ответы на вопросы"
        ],
        "**Структура презентации:**\n\n**1. Introduction (10-15% времени)**\n\n**Компоненты:**\n- Greeting (приветствие)\n- Self-introduction (представление)\n- Topic announcement (объявление темы)\n- Outline (план)\n\n**Пример:**\n\"Good morning everyone. My name is [Name], and I'm the [Position] at [Company]. Today I'm going to talk about [Topic]. I've divided my presentation into three main parts: first, I'll discuss [Point 1]; then I'll move on to [Point 2]; and finally, I'll look at [Point 3]. The presentation will take about [X] minutes, and I'll be happy to answer any questions at the end.\"\n\n---\n\n**2. Body (75-80% времени)**\n\n**Структура каждого раздела:**\n- Topic sentence (введение в пункт)\n- Explanation (объяснение)\n- Example (пример)\n- Transition (переход)\n\n**Фразы переходов:**\n- Let's begin with...\n- Moving on to my next point...\n- Now I'd like to discuss...\n- This brings me to...\n\n---\n\n**3. Conclusion (10-15% времени)**\n\n**Компоненты:**\n- Summary (обобщение)\n- Final message (финальное сообщение)\n- Call to action (призыв к действию)\n- Q&A invitation (приглашение к вопросам)\n\n**Пример:**\n\"To sum up, we've looked at [Point 1], [Point 2], and [Point 3]. The key takeaway is that [Main message]. I encourage you all to [Call to action]. Thank you for your attention. I'd be happy to answer any questions you may have.\"\n\n---\n\n**Работа с визуальными материалами:**\n\n**Фразы:**\n- As you can see from this chart/graph...\n- This diagram illustrates...\n- Let me draw your attention to this figure.\n- The table shows the comparison between...\n\n**Советы:**\n- Не читайте со слайдов!\n- Используйте простые графики\n- Минимум текста на слайдах\n- Делайте зрительный контакт\n\n---\n\n**Ответы на вопросы:**\n\n**Если знаете ответ:**\n- That's a good question. The answer is...\n- I'm glad you asked that. As I mentioned...\n\n**Если не знаете ответ:**\n- That's an interesting question. I don't have the exact figures with me, but I can get back to you on that.\n- I'm not entirely sure, but I would guess that...\n\n**Если вопрос не по теме:**\n- That's slightly outside the scope of this presentation, but I'd be happy to discuss it afterwards.\n\n**Если не поняли вопрос:**\n- Could you please rephrase your question?\n- I'm not sure I understand. Could you clarify?",
        ["Today I'm going to talk about... — Сегодня я расскажу о...", "To sum up, we've looked at... — Подводя итог, мы рассмотрели...", "I'd be happy to answer any questions. — С удовольствием отвечу на вопросы."],
        ["Практикуйте презентацию заранее", "Не читайте со слайдов!", "Делайте зрительный контакт с аудиторией"],
        [
          "Введение (10-15%) → Основная часть (75-80%) → Заключение (10-15%)",
          "Let's move on to... — переход между частями",
          "Не читайте со слайдов, делайте зрительный контакт"
        ])
      ]
    }
  ]
}

export const games: GameLesson[] = [
  {
    title: "Урок 1: Mixed Conditionals",
    subject: "Английский язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "If I had studied, I ____ have a degree now.", options: ["would", "will", "would have"], correctAnswer: "would", hint: "Mixed: условие в прошлом, результат сейчас" },
      { type: 'quiz', question: "Had I known = ?", options: ["If I had known", "If I knew", "If I have known"], correctAnswer: "If I had known", hint: "Инверсия в условном предложении" },
      { type: 'quiz', question: "If I were you, I ____ have accepted. (III+II)", options: ["would", "will", "should", "could", "might"], correctAnswer: "would", hint: "would have + V3" },
      { type: 'quiz', question: "Were I rich... — это:", options: ["Past Simple", "Инверсия (без if)", "Present Simple"], correctAnswer: "Инверсия (без if)", hint: "Were I = If I were" }
    ],
    reward: { stars: 3, message: "Excellent! You know Mixed Conditionals! 🎓" }
  },
  {
    title: "Урок 2: Inversion",
    subject: "Английский язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Never ____ I seen such beauty.", options: ["have", "has", "did"], correctAnswer: "have", hint: "Never have I seen..." },
      { type: 'quiz', question: "Only then ____ she understand.", options: ["did", "does", "has"], correctAnswer: "did", hint: "Only then did she understand." },
      { type: 'quiz', question: "____ had I arrived than it started to rain. (No sooner)", options: ["No sooner", "Hardly", "Scarcely", "Seldom", "Never"], correctAnswer: "No sooner", hint: "No sooner had... than..." },
      { type: 'quiz', question: "She likes coffee. So __ I.", options: ["do", "am", "like"], correctAnswer: "do", hint: "So do I = Я тоже" }
    ],
    reward: { stars: 3, message: "Great! You know Inversion! 📚" }
  },
  {
    title: "Урок 3: Subjunctive Mood",
    subject: "Английский язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I suggest that he ____ more careful. (subjunctive)", options: ["be", "is", "was"], correctAnswer: "be", hint: "Present Subjunctive — базовая форма" },
      { type: 'quiz', question: "I wish I ____ rich. (сожаление о настоящем)", options: ["am", "were", "be"], correctAnswer: "were", hint: "Past Subjunctive — were для всех лиц" },
      { type: 'quiz', question: "I wish I ____ known the truth. (сожаление о прошлом)", options: ["had", "have", "would have", "could have", "should have"], correctAnswer: "had", hint: "wish + Past Perfect" },
      { type: 'quiz', question: "You ____ better study. (совет)", options: ["had", "would", "should"], correctAnswer: "had", hint: "Had better = тебе лучше" }
    ],
    reward: { stars: 3, message: "Perfect! You know Subjunctive Mood! ✨" }
  },
  {
    title: "Урок 4: Complex Structures",
    subject: "Английский язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "It was John ____ broke the window. (cleft sentence)", options: ["who", "which", "what"], correctAnswer: "who", hint: "It was... who... = Именно..." },
      { type: 'quiz', question: "____ down the street, I met an old friend.", options: ["Walking", "Walked", "Walk"], correctAnswer: "Walking", hint: "Present Participle = активное действие" },
      { type: 'quiz', question: "What I need ____ a cup of coffee.", options: ["is", "are", "was", "were", "be"], correctAnswer: "is", hint: "Wh-cleft: What... is..." },
      { type: 'quiz', question: "He is ____ young to drive.", options: ["too", "so", "very"], correctAnswer: "too", hint: "Too... to = слишком... чтобы" }
    ],
    reward: { stars: 3, message: "Excellent! You know Complex Structures! 🏗️" }
  },
  {
    title: "Урок 5: Academic Vocabulary",
    subject: "Английский язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Анализировать данные — ____ the data.", options: ["analyse", "make", "do"], correctAnswer: "analyse", hint: "Analyse = анализировать" },
      { type: 'quiz', question: "Ключевой фактор — a key ____.", options: ["issue", "factor", "aspect"], correctAnswer: "factor", hint: "Factor = фактор" },
      { type: 'quiz', question: "Furthermore, Moreover, ____ = кроме того", options: ["In addition", "Additionally", "Besides", "Also", "Plus"], correctAnswer: "In addition", hint: "In addition = дополнительно" },
      { type: 'quiz', question: "В заключение — In ____.", options: ["end", "conclusion", "finish"], correctAnswer: "conclusion", hint: "In conclusion" }
    ],
    reward: { stars: 3, message: "Super! You know Academic Vocabulary! ✍️" }
  },
  {
    title: "Урок 6: Essay Writing",
    subject: "Английский язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Главная мысль эссе — ____ statement.", options: ["thesis", "topic", "main"], correctAnswer: "thesis", hint: "Thesis statement = тезис" },
      { type: 'quiz', question: "Первое предложение абзаца — ____ sentence.", options: ["topic", "main", "first"], correctAnswer: "topic", hint: "Topic sentence = тематическое предложение" },
      { type: 'quiz', question: "This essay will ____ the causes of climate change.", options: ["examine", "examination", "examining", "examines", "examined"], correctAnswer: "examine", hint: "examine = рассматривать" },
      { type: 'quiz', question: "Заключение эссе должно:", options: ["Вводить новые идеи", "Обобщать основные пункты", "Быть самым длинным"], correctAnswer: "Обобщать основные пункты", hint: "Заключение = summary" }
    ],
    reward: { stars: 3, message: "Great! You know Essay Writing! 📝" }
  },
  {
    title: "Урок 7: Debating Skills",
    subject: "Английский язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "My primary ____ is that... (аргумент)", options: ["argument", "point", "idea"], correctAnswer: "argument", hint: "Argument = аргумент" },
      { type: 'quiz', question: "Атака на личность — логическая ошибка:", options: ["Straw Man", "Ad Hominem", "False Dichotomy"], correctAnswer: "Ad Hominem", hint: "Ad Hominem = к человеку" },
      { type: 'quiz', question: "I see your point, ____ I must disagree.", options: ["but", "and", "so", "or", "yet"], correctAnswer: "but", hint: "I see your point, but..." },
      { type: 'quiz', question: "«Или ты с нами, или против нас» — это:", options: ["Straw Man", "False Dichotomy", "Slippery Slope"], correctAnswer: "False Dichotomy", hint: "Ложная дилемма" }
    ],
    reward: { stars: 3, message: "Excellent! You know Debating Skills! 🎤" }
  },
  {
    title: "Урок 8: Business English",
    subject: "Английский язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Dear Mr. Smith, ... Yours ____.", options: ["faithfully", "sincerely", "truly"], correctAnswer: "sincerely", hint: "Yours sincerely — когда знаете имя" },
      { type: 'quiz', question: "Я пишу, чтобы узнать о... — I am writing to ____ about...", options: ["inquire", "ask", "know"], correctAnswer: "inquire", hint: "Inquire = узнавать, справляться" },
      { type: 'quiz', question: "Please find ____ my CV. (во вложении)", options: ["attached", "attach", "attachment", "attaching", "attaches"], correctAnswer: "attached", hint: "Please find attached..." },
      { type: 'quiz', question: "I look forward ____ from you.", options: ["hear", "to hear", "to hearing"], correctAnswer: "to hearing", hint: "look forward to + -ing" }
    ],
    reward: { stars: 3, message: "Excellent! You know Business English! 💼" }
  },
  {
    title: "Урок 9: Job Interview",
    subject: "Английский язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Tell me about ____. (о себе)", options: ["you", "yourself", "yours"], correctAnswer: "yourself", hint: "Tell me about yourself" },
      { type: 'quiz', question: "What are your ____? (сильные стороны)", options: ["strengths", "powers", "forces"], correctAnswer: "strengths", hint: "Strengths = сильные стороны" },
      { type: 'quiz', question: "Why should we ____ you?", options: ["hire", "hired", "hiring", "hires", "fire"], correctAnswer: "hire", hint: "hire = нанять" },
      { type: 'quiz', question: "Спасибо за интервью — Thank you email отправить:", options: ["В тот же день", "В течение 24 часов", "Через неделю"], correctAnswer: "В течение 24 часов", hint: "Thank you email — в течение 24 часов" }
    ],
    reward: { stars: 3, message: "Perfect! You're ready for Job Interview! 💪" }
  },
  {
    title: "Урок 10: Presentation Skills",
    subject: "Английский язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Today I'm going to ____ about...", options: ["talk", "speak", "tell"], correctAnswer: "talk", hint: "talk about = говорить о" },
      { type: 'quiz', question: "Какой процент времени — введение?", options: ["5%", "10-15%", "30%"], correctAnswer: "10-15%", hint: "Introduction = 10-15%" },
      { type: 'quiz', question: "To ____ up, we've looked at three main points.", options: ["sum", "add", "total", "count", "wrap"], correctAnswer: "sum", hint: "To sum up = подводя итог" },
      { type: 'quiz', question: "I'd be happy to ____ any questions.", options: ["answer", "reply", "respond"], correctAnswer: "answer", hint: "answer questions = отвечать на вопросы" }
    ],
    reward: { stars: 3, message: "Excellent! You know Presentation Skills! 🎯" }
  }
]
