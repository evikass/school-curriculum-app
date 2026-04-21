import { SubjectData, GameLesson } from '@/data/types'

export const lessons: SubjectData = {
  title: "Иностранный язык",
  icon: "Languages",
  color: "text-pink-400",
  topics: [
    "Путешествия и туризм",
    "Профессии и карьера",
    "Экология и окружающая среда",
    "Средства массовой информации",
    "Научно-технический прогресс"
  ],
  detailedTopics: [
    {
      topic: "Путешествия и туризм",
      lessons: [
        {
          title: "Виды путешествий",
          description: `Изучение лексики по теме путешествия: авиаперелёты, железнодорожные поездки, круизы, автотуризм. Учащиеся научатся описывать различные виды путешествий, их преимущества и недостатки, а также выражать свой опыт путешествий с использованием времени Present Perfect.

**Основная лексика по теме путешествия:**

| Английское слово | Транскрипция | Русский перевод |
|------------------|--------------|-----------------|
| journey | /ˈdʒɜːni/ | путешествие |
| trip | /trɪp/ | поездка |
| voyage | /ˈvɔɪɪdʒ/ | морское путешествие |
| tour | /tʊə/ | тур, экскурсия |
| expedition | /ˌekspəˈdɪʃn/ | экспедиция |
| excursion | /ɪkˈskɜːʃn/ | экскурсия |
| destination | /ˌdestɪˈneɪʃn/ | место назначения |
| itinerary | /aɪˈtɪnərəri/ | маршрут, план поездки |
| accommodation | /əˌkɒməˈdeɪʃn/ | размещение |
| sightseeing | /ˈsaɪtˌsiːɪŋ/ | осмотр достопримечательностей |

**Виды путешествий и их характеристики:**

| Вид путешествия | Английский термин | Преимущества | Недостатки |
|-----------------|-------------------|--------------|------------|
| Авиаперелёт | air travel | быстро, комфортно | дорого, задержки |
| Поездка на поезде | rail travel | удобно, красиво | медленнее самолёта |
| Круиз | cruise | роскошно, развлечения | очень дорого |
| Автотуризм | road trip | свобода, гибкость | усталость от вождения |
| Автостоп | hitchhiking | дёшево, приключения | небезопасно |
| Бэкпэкинг | backpacking | экономично, самостоятельность | тяжёлый рюкзак |

**Present Perfect для описания опыта путешествий:**

Время Present Perfect используется для описания жизненного опыта путешествий без указания конкретного времени. Это одно из важнейших применений данного грамматического времени в разговорной практике.

**Структура утверждения:** Subject + have/has + Past Participle

**Примеры использования:**
- I have visited Paris twice. (Я посещал Париж дважды.)
- She has never been to London. (Она никогда не была в Лондоне.)
- Have you ever travelled by train? (Вы когда-нибудь путешествовали на поезде?)
- We have explored many European countries. (Мы исследовали многие европейские страны.)
- He has just returned from Japan. (Он только что вернулся из Японии.)

**Наречия, часто используемые с Present Perfect:**
- ever (когда-либо) — Have you ever seen the Grand Canyon?
- never (никогда) — I have never visited Australia.
- already (уже) — They have already booked the hotel.
- yet (ещё) — Have you packed your luggage yet?
- just (только что) — She has just arrived at the airport.
- before (ранее) — I have been to this city before.

**Полезные фразы для обсуждения путешествий:**
- What's your dream destination? (Какое твоё место мечты?)
- I prefer travelling by... (Я предпочитаю путешествовать на...)
- The best trip I've ever had was... (Лучшее путешествие, которое у меня было...)
- I would love to visit... (Я хотел бы посетить...)`,
          tasks: [
            "Переведите и составьте предложение с словом 'destination': Опишите место назначения вашей мечты",
            "Образуйте вопросительное предложение в Present Perfect с наречием 'ever' о путешествии в Азию",
            "Напишите три предложения о своём опыте путешествий, используя Present Perfect с наречиями never, already и just"
          ],
          examples: [
          "I have visited Paris twice — Present Perfect для описания опыта путешествий ✈️",
          "Наречия Present Perfect: ever, never, already, yet, just, before",
          "Backpacking — экономичный способ путешествовать с рюкзаком"
          ],
          keyPoints: [
            "Примеры использования — I have visited Paris twice",
            "Наречия, часто используемые с Present Perfect — never (никогда) — I have never visited Australia",
            "just (только что) — She has just arrived at the airport."
          ]
        },
        {
          title: "В аэропорту",
          description: `Лексика для ориентирования в аэропорту: регистрация, паспортный контроль, таможня, посадка. Этот урок научит учащихся успешно взаимодействовать с персоналом аэропорта, понимать объявления и ориентироваться в аэропортовой инфраструктуре.

**Основная аэропортовая лексика:**

| Английское слово | Транскрипция | Русский перевод |
|------------------|--------------|-----------------|
| terminal | /ˈtɜːmɪnl/ | терминал |
| check-in | /ˈtʃek ɪn/ | регистрация |
| boarding pass | /ˈbɔːdɪŋ pɑːs/ | посадочный талон |
| departure lounge | /dɪˈpɑːtʃə laʊndʒ/ | зал вылета |
| gate | /geɪt/ | выход на посадку |
| customs | /ˈkʌstəmz/ | таможня |
| baggage claim | /ˈbæɡɪdʒ kleɪm/ | получение багажа |
| carousel | /ˌkærəˈsel/ | багажная карусель |
| conveyor belt | /kənˈveɪə belt/ | транспортерная лента |
| security check | /sɪˈkjʊərəti tʃek/ | контроль безопасности |
| passport control | /ˈpɑːspɔːt kənˈtrəʊl/ | паспортный контроль |
| duty-free | /ˌdjuːti ˈfriː/ | магазин беспошлинной торговли |

**Типы багажа и связанные термины:**

| Термин | Значение | Пример использования |
|--------|----------|---------------------|
| carry-on luggage | ручная кладь | You can take one carry-on bag. |
| checked baggage | сдаваемый багаж | Maximum weight is 23 kg. |
| suitcase | чемодан | I bought a new suitcase. |
| backpack | рюкзак | Backpacks are convenient for travel. |
| luggage tag | багажная бирка | Attach a luggage tag to your bag. |
| excess baggage | перевес багажа | Excess baggage fees are expensive. |
| lost luggage | потерянный багаж | Report lost luggage immediately. |

**Полезные фразы в аэропорту:**

**На регистрации:**
- I'd like to check in for flight BA123 to London. (Я хотел бы зарегистрироваться на рейс BA123 в Лондон.)
- Can I have a window/aisle seat? (Можно мне место у окна/у прохода?)
- How much luggage can I take? (Сколько багажа я могу взять?)
- Is the flight on time? (Рейс вылетает вовремя?)
- Where is gate 15? (Где находится выход 15?)

**На паспортном контроле:**
- Here is my passport. (Вот мой паспорт.)
- I'm travelling for tourism/business. (Я путешествую как турист/по делам.)
- I'm staying for two weeks. (Я пробуду две недели.)
- This is my return ticket. (Это мой обратный билет.)

**Объявления в аэропорту:**
- Flight BA123 is now boarding at gate 15. (Рейс BA123 сейчас садится у выхода 15.)
- This is the final boarding call for flight BA123. (Это последняя посадка на рейс BA123.)
- Flight BA123 has been delayed by 30 minutes. (Рейс BA123 задержан на 30 минут.)
- Please proceed to gate 15 for boarding. (Пожалуйста, пройдите к выходу 15 для посадки.)

**Проблемные ситуации:**
- My flight has been delayed/cancelled. (Мой рейс задержан/отменён.)
- I've lost my luggage. (Я потерял багаж.)
- My luggage hasn't arrived. (Мой багаж не прибыл.)
- Where is the lost and found office? (Где бюро находок?)`,
          tasks: [
            "Составьте диалог на регистрации: попросите место у окна и уточните норму багажа",
            "Переведите и запомните: 'This is the final boarding call' — когда вы можете услышать эту фразу?",
            "Напишите три фразы для решения проблемы с потерянным багажом"
          ],
          examples: [
          "I\'d like to check in for flight BA123 to London — фраза на регистрации 🛫",
          "Boarding pass — посадочный талон, duty-free — магазин беспошлинной торговли",
          "This is the final boarding call — последнее объявление о посадке"
          ],
          keyPoints: [
            "Полезные фразы в аэропорту — На регистрации:",
            "На регистрации — Can I have a window/aisle seat",
            "Проблемные ситуации — My flight has been delayed/cancelled"
          ]
        },
        {
          title: "В гостинице",
          description: `Бронирование номера, регистрация заезда и выезда, решение проблем в отеле. Учащиеся научатся бронировать проживание, общаться с персоналом отеля и решать типичные проблемы, возникающие во время проживания.

**Основная лексика по теме гостиница:**

| Английское слово | Транскрипция | Русский перевод |
|------------------|--------------|-----------------|
| reservation | /ˌrezəˈveɪʃn/ | бронирование |
| booking | /ˈbʊkɪŋ/ | бронь |
| check-in | /ˈtʃek ɪn/ | заезд, регистрация |
| check-out | /ˈtʃek aʊt/ | выезд |
| reception | /rɪˈsepʃn/ | стойка регистрации |
| receptionist | /rɪˈsepʃənɪst/ | администратор |
| room service | /ˈruːm ˈsɜːvɪs/ | обслуживание номеров |
| amenities | /əˈmiːnɪtiz/ | удобства |
| facilities | /fəˈsɪlɪtiz/ | сооружения, службы |
| deposit | /dɪˈpɒzɪt/ | залог |
| complimentary | /ˌkɒmplɪˈmentri/ | бесплатный |
| vacancy | /ˈveɪkənsi/ | свободный номер |

**Типы номеров в отеле:**

| Тип номера | Описание | Особенности |
|------------|----------|-------------|
| Single room | одноместный номер | Одна кровать |
| Double room | двухместный номер | Одна большая кровать |
| Twin room | двухместный номер | Две отдельные кровати |
| Suite | люкс | Несколько комнат, гостиная |
| Deluxe room | улучшенный номер | Повышенная комфортность |
| Family room | семейный номер | Вместимость 3-4 человека |
| Penthouse | пентхаус | Роскошный номер на верхнем этаже |

**Фразы для бронирования номера:**

**По телефону или онлайн:**
- I'd like to book a room for two nights. (Я хотел бы забронировать номер на две ночи.)
- Do you have any vacancies for next weekend? (У вас есть свободные номера на следующие выходные?)
- What's the rate per night? (Какая цена за ночь?)
- Is breakfast included? (Завтрак включён?)
- Can I cancel my reservation free of charge? (Могу ли я отменить бронирование бесплатно?)
- I'd like a room with a sea view. (Я хотел бы номер с видом на море.)

**При заезде:**
- I have a reservation under the name Smith. (У меня бронирование на фамилию Смит.)
- I'd like to check in, please. (Я хотел бы зарегистрироваться.)
- Can I see your ID/passport, please? (Можно ваш документ?)
- Here's your key card. (Вот ваша ключ-карта.)
- The elevator is on your right. (Лифт справа от вас.)
- Breakfast is served from 7 to 10 am. (Завтрак подаётся с 7 до 10 утра.)

**Услуги и проблемы:**

**Просьбы о услугах:**
- Could I have an extra pillow/blanket/towel? (Можно дополнительную подушку/одеяло/полотенце?)
- The Wi-Fi password, please? (Пароль от Wi-Fi, пожалуйста?)
- What time is check-out? (Во сколько выезд?)
- Can I have a late check-out? (Можно поздний выезд?)
- Could you call a taxi for me? (Не могли бы вы вызвать мне такси?)

**Жалобы и проблемы:**
- The air conditioning isn't working. (Кондиционер не работает.)
- There's no hot water in my room. (В моём номере нет горячей воды.)
- The room is too noisy. (В номере слишком шумно.)
- My room hasn't been cleaned. (Мой номер не убрали.)
- I think there's a mistake in my bill. (Думаю, в моём счёте ошибка.)`,
          tasks: [
            "Составьте диалог для бронирования номера: уточните наличие свободных мест, цену и включён ли завтрак",
            "Опишите вашу жалобу на неубранный номер администратору отеля",
            "Переведите и объясните разницу между double room и twin room"
          ],
          examples: [
          "I\'d like to book a room for two nights — бронирование номера на две ночи 🏨",
          "Double room — одна большая кровать, twin room — две отдельные",
          "The air conditioning isn\'t working — жалоба на неработающий кондиционер"
          ],
          keyPoints: [
            "Фразы для бронирования номера — По телефону или онлайн:",
            "По телефону или онлайн — What's the rate per night",
            "При заезде — I'd like to check in, please"
          ]
        }
      ]
    },
    {
      topic: "Профессии и карьера",
      lessons: [
        {
          title: "Мир профессий",
          description: `Изучение названий профессий, описание обязанностей и требований. Модальные глаголы для описания профессиональных требований. Учащиеся научатся описывать различные профессии, говорить о требованиях к ним и выражать свои карьерные предпочтения.

**Профессии в современном мире:**

| Английское слово | Транскрипция | Русский перевод | Сфера деятельности |
|------------------|--------------|-----------------|-------------------|
| doctor | /ˈdɒktə/ | врач | медицина |
| nurse | /nɜːs/ | медсестра/медбрат | медицина |
| engineer | /ˌendʒɪˈnɪə/ | инженер | техническая |
| lawyer | /ˈlɔːjə/ | юрист | право |
| accountant | /əˈkaʊntənt/ | бухгалтер | финансы |
| software developer | /ˈsɒftweə dɪˈveləpə/ | разработчик ПО | IT |
| journalist | /ˈdʒɜːnəlɪst/ | журналист | медиа |
| architect | /ˈɑːkɪtekt/ | архитектор | строительство |
| teacher | /ˈtiːtʃə/ | учитель | образование |
| chef | /ʃef/ | шеф-повар | общественное питание |
| pilot | /ˈpaɪlət/ | пилот | авиация |
| mechanic | /məˈkænɪk/ | механик | техническая |

**Профессии будущего:**

| Профессия | Описание | Навыки |
|-----------|----------|--------|
| Data scientist | аналитик данных | математика, статистика |
| AI specialist | специалист по ИИ | программирование, машинное обучение |
| Cybersecurity analyst | аналитик кибербезопасности | IT-безопасность |
| Sustainability consultant | консультант по устойчивому развитию | экология, бизнес |
| Virtual reality designer | дизайнер VR | 3D-моделирование, творчество |
| Robotics engineer | инженер-робототехник | механика, электроника |

**Модальные глаголы для описания профессиональных требований:**

| Модальный глагол | Значение | Пример |
|------------------|----------|--------|
| must | обязательность, необходимость | You must have a medical degree to become a doctor. |
| should | рекомендация, желательность | You should be good at math for engineering. |
| need to | необходимость | You need to be creative as a designer. |
| have to | вынужденная необходимость | Teachers have to work with children. |
| can | способность, возможность | A programmer can work remotely. |
| may | возможность, вероятность | You may need to travel for this job. |

**Описание профессиональных обязанностей:**

При описании профессий важно использовать правильные грамматические конструкции:

**Описание обязанностей (Present Simple):**
- A teacher explains new material to students. (Учитель объясняет новый материал ученикам.)
- Doctors treat patients in hospitals. (Врачи лечат пациентов в больницах.)
- Journalists write articles for newspapers. (Журналисты пишут статьи для газет.)

**Описание требований к профессии:**
- You must have excellent communication skills. (У вас должны быть отличные коммуникативные навыки.)
- You should be able to work in a team. (Вы должны уметь работать в команде.)
- You need to be patient and attentive. (Вам нужно быть терпеливым и внимательным.)

**Вопросы о профессиях:**
- What do you do? / What's your job? (Кем вы работаете?)
- What does a software developer do? (Чем занимается разработчик ПО?)
- What skills do you need for this job? (Какие навыки нужны для этой работы?)
- Where do you work? (Где вы работаете?)
- How long have you been working there? (Как долго вы там работаете?)`,
          tasks: [
            "Опишите профессию своей мечты: название, обязанности, необходимые навыки (используя модальные глаголы must, should, need to)",
            "Составьте три предложения о том, что делает учитель, врач и журналист (используя Present Simple)",
            "Переведите и объясните, какие навыки нужны для профессии 'cybersecurity analyst'"
          ],
          examples: [
          "A software developer creates applications using programming languages 💼",
          "Модальные глаголы: must (обязательно), should (рекомендуется), need to (необходимо)",
          "AI specialist и cybersecurity analyst — профессии будущего"
          ],
          keyPoints: [
            "Вопросы о профессиях — What do you do",
            "Ключевое понятие: Мир профессий",
            "Ключевое понятие: Мир профессий"
          ]
        },
        {
          title: "Поиск работы",
          description: `Написание резюме, сопроводительного письма, подготовка к собеседованию. Учащиеся научатся составлять профессиональные документы для трудоустройства и готовиться к собеседованиям на английском языке.

**Лексика по теме поиск работы:**

| Английское слово | Транскрипция | Русский перевод |
|------------------|--------------|-----------------|
| CV / resume | /ˌsiː ˈviː/ /ˈrezjʊmeɪ/ | резюме |
| cover letter | /ˈkʌvə ˈletə/ | сопроводительное письмо |
| interview | /ˈɪntəvjuː/ | собеседование |
| vacancy | /ˈveɪkənsi/ | вакансия |
| applicant | /ˈæplɪkənt/ | соискатель |
| candidate | /ˈkændɪdət/ | кандидат |
| employer | /ɪmˈplɔɪə/ | работодатель |
| employee | /ɪmˈplɔɪiː/ | работник |
| salary | /ˈsæləri/ | зарплата |
| wages | /weɪdʒɪz/ | заработная плата (почасовая) |
| benefits | /ˈbenɪfɪts/ | льготы, пособия |
| position | /pəˈzɪʃn/ | должность |

**Структура резюме (CV):**

| Раздел | Английское название | Содержание |
|--------|---------------------|------------|
| Контактная информация | Contact Information | Имя, телефон, email, адрес |
| Цель | Objective / Career Summary | Кратко о целях и опыте |
| Опыт работы | Work Experience | Места работы, должности, обязанности |
| Образование | Education | Учебные заведения, специальности |
| Навыки | Skills | Профессиональные и языковые навыки |
| Достижения | Achievements | Награды, сертификаты, проекты |

**Пример резюме (фрагменты):**

**Objective:**
"A motivated software developer with 3 years of experience seeking a position at an innovative tech company."

**Work Experience:**
- Software Developer at TechCorp (2021-present)
  - Developed web applications using JavaScript and Python
  - Collaborated with a team of 5 developers
  - Improved website performance by 30%

**Skills:**
- Programming: JavaScript, Python, Java
- Languages: English (Advanced), Russian (Native)
- Soft skills: teamwork, problem-solving, communication

**Сопроводительное письмо (Cover Letter):**

Структура сопроводительного письма:
1. Приветствие: Dear Mr./Ms. [Last Name],
2. Вступление: I am writing to apply for the position of...
3. Почему вы подходите: I believe my experience in... makes me a strong candidate...
4. Детали опыта: In my previous role, I...
5. Заключение: I would welcome the opportunity to discuss my application...
6. Завершение: I look forward to hearing from you. Sincerely, [Name]

**Примеры фраз для cover letter:**
- I am writing to express my interest in the position of... (Я пишу, чтобы выразить интерес к должности...)
- I was excited to see your job posting on... (Я был рад увидеть вашу вакансию на...)
- With my background in... I am confident I can contribute to... (С моим опытом в... я уверен, что могу внести вклад в...)
- Please find my CV attached for your consideration. (Пожалуйста, найдите моё резюме во вложении.)`,
          tasks: [
            "Напишите краткий раздел 'Objective' для резюме, описывающий ваши карьерные цели",
            "Составьте начало сопроводительного письма с указанием должности и источника информации о вакансии",
            "Переведите три ключевых навыка из раздела Skills и объясните их важность для работодателя"
          ],
          examples: [
          "CV (resume) — резюме, cover letter — сопроводительное письмо 📋",
          "I am writing to apply for the position of... — начало сопроводительного письма",
          "Objective — краткое описание карьерных целей в начале резюме"
          ],
          keyPoints: [
            "Пример резюме (фрагменты) — Objective:",
            "Сопроводительное письмо (Cover Letter) — Структура сопроводительного письма:",
            "Структура сопроводительного письма — Приветствие: Dear Mr"
          ]
        },
        {
          title: "Деловое общение",
          description: `Деловая переписка, телефонные разговоры, презентации. Профессиональный этикет. Учащиеся освоят навыки деловой коммуникации на английском языке, включая написание писем, проведение телефонных разговоров и публичные выступления.

**Основная деловая лексика:**

| Английское слово | Транскрипция | Русский перевод |
|------------------|--------------|-----------------|
| meeting | /ˈmiːtɪŋ/ | встреча, совещание |
| conference | /ˈkɒnfərəns/ | конференция |
| deadline | /ˈdedlaɪn/ | крайний срок |
| proposal | /prəˈpəʊzl/ | предложение, заявка |
| negotiation | /nɪˌɡəʊʃiˈeɪʃn/ | переговоры |
| contract | /ˈkɒntrækt/ | контракт, договор |
| agreement | /əˈɡriːmənt/ | соглашение |
| partnership | /ˈpɑːtnəʃɪp/ | партнёрство |
| client | /ˈklaɪənt/ | клиент |
| supplier | /səˈplaɪə/ | поставщик |
| invoice | /ˈɪnvɔɪs/ | счёт-фактура |
| quotation | /kwəʊˈteɪʃn/ | коммерческое предложение |

**Деловая переписка:**

**Типы деловых писем:**
| Тип письма | Цель | Пример начала |
|------------|------|---------------|
| Запрос информации | Inquiry | I am writing to inquire about... |
| Ответ на запрос | Reply | Thank you for your inquiry... |
| Предложение | Proposal | We are pleased to submit our proposal... |
| Жалоба | Complaint | I am writing to express my dissatisfaction... |
| Извинение | Apology | We sincerely apologize for... |
| Благодарность | Thank you | We appreciate your cooperation... |

**Полезные фразы для деловых писем:**

**Начало письма:**
- I am writing to inquire about your services. (Я пишу, чтобы узнать о ваших услугах.)
- I am writing regarding our meeting last week. (Я пишу касательно нашей встречи на прошлой неделе.)
- Thank you for your email dated March 15th. (Спасибо за ваше письмо от 15 марта.)

**Основная часть:**
- Please find attached the requested documents. (Пожалуйста, найдите во вложении запрошенные документы.)
- I would like to confirm our appointment on... (Я хотел бы подтвердить нашу встречу...)
- Could you please provide more information about...? (Не могли бы вы предоставить больше информации о...?)

**Завершение письма:**
- I look forward to hearing from you. (Жду вашего ответа.)
- Thank you for your consideration. (Спасибо за рассмотрение.)
- Please do not hesitate to contact me if you need further information. (Пожалуйста, свяжитесь со мной, если нужна дополнительная информация.)
- Best regards / Sincerely / Yours faithfully (С уважением)

**Телефонные разговоры:**

**Начало разговора:**
- Good morning, ABC Company. How can I help you? (Доброе утро, компания ABC. Чем могу помочь?)
- This is John Smith speaking. (Это Джон Смит.)
- I'm calling about... / I'm calling regarding... (Я звоню по поводу...)

**Просьбы и ответы:**
- Could I speak to Mr. Johnson, please? (Могу я поговорить с мистером Джонсоном?)
- One moment, please. I'll put you through. (Один момент, я вас соединю.)
- I'm afraid he's in a meeting at the moment. (Боюсь, он сейчас на совещании.)
- Would you like to leave a message? (Хотите оставить сообщение?)

**Презентации:**

**Структура презентации:**
1. Вступление: Good morning everyone. Today I'm going to talk about...
2. Цель: The purpose of my presentation is to...
3. Основная часть: First, I'd like to discuss... Secondly... Finally...
4. Графики и таблицы: As you can see from this chart...
5. Заключение: To sum up / In conclusion...
6. Вопросы: Are there any questions?`,
          tasks: [
            "Напишите деловое письмо-запрос о возможности сотрудничества с компанией",
            "Составьте телефонный диалог: вы звоните в компанию и просите соединить с менеджером",
            "Подготовьте начало презентации о своём проекте или идее (3-4 предложения)"
          ],
          examples: [
          "I look forward to hearing from you — стандартное завершение делового письма 📧",
          "Could I speak to Mr. Johnson, please? — просьба соединить по телефону",
          "Good morning everyone. Today I\'m going to talk about... — начало презентации"
          ],
          keyPoints: [
            "Деловая переписка — Типы деловых писем:",
            "Полезные фразы для деловых писем — Начало письма:",
            "Завершение письма — I look forward to hearing from you"
          ]
        }
      ]
    },
    {
      topic: "Экология и окружающая среда",
      lessons: [
        {
          title: "Экологические проблемы",
          description: `Изучение лексики по теме экологии: загрязнение, изменение климата, исчезновение видов. Учащиеся научатся обсуждать экологические проблемы на английском языке, описывать причины и последствия экологических кризисов.

**Основная экологическая лексика:**

| Английское слово | Транскрипция | Русский перевод |
|------------------|--------------|-----------------|
| environment | /ɪnˈvaɪrənmənt/ | окружающая среда |
| pollution | /pəˈluːʃn/ | загрязнение |
| climate change | /ˈklaɪmət tʃeɪndʒ/ | изменение климата |
| global warming | /ˌɡləʊbl ˈwɔːmɪŋ/ | глобальное потепление |
| greenhouse effect | /ˈɡriːnhaʊs ɪˈfekt/ | парниковый эффект |
| deforestation | /diːˌfɒrɪˈsteɪʃn/ | вырубка лесов |
| endangered species | /ɪnˈdeɪndʒəd ˈspiːʃiːz/ | исчезающие виды |
| extinction | /ɪkˈstɪŋkʃn/ | вымирание |
| habitat | /ˈhæbɪtæt/ | среда обитания |
| ecosystem | /ˈiːkəʊsɪstəm/ | экосистема |
| biodiversity | /ˌbaɪəʊdaɪˈvɜːsəti/ | биоразнообразие |
| carbon footprint | /ˈkɑːbən ˈfʊtprɪnt/ | углеродный след |

**Типы загрязнения:**

| Тип загрязнения | Английский термин | Источники | Последствия |
|-----------------|-------------------|-----------|-------------|
| Воздушное | air pollution | заводы, автомобили | заболевания дыхательной системы |
| Водное | water pollution | промышленные стоки | гибель рыб, отравление воды |
| Почвенное | soil pollution | пестициды, свалки | деградация земель |
| Шумовое | noise pollution | транспорт, строительство | стресс, нарушение сна |
| Световое | light pollution | городское освещение | нарушение экосистем |
| Пластиковое | plastic pollution | одноразовая упаковка | загрязнение океанов |

**Причины и последствия экологических проблем:**

**Глобальное потепление:**

Причины (Causes):
- Burning fossil fuels (сжигание ископаемого топлива)
- Deforestation (вырубка лесов)
- Industrial emissions (промышленные выбросы)
- Agriculture and livestock (сельское хозяйство и животноводство)

Последствия (Effects):
- Rising sea levels (повышение уровня моря)
- Melting ice caps (таяние ледников)
- Extreme weather events (экстремальные погодные явления)
- Droughts and floods (засухи и наводнения)

**Исчезновение видов:**

Причины:
- Habitat destruction (разрушение среды обитания)
- Poaching (браконьерство)
- Climate change (изменение климата)
- Pollution (загрязнение)

Примеры исчезающих видов:
- Giant panda (большая панда)
- Siberian tiger (амурский тигр)
- Blue whale (голубой кит)
- Snow leopard (снежный барс)
- Polar bear (белый медведь)

**Грамматика: Cause and Effect (Причина и следствие)**

Для описания причинно-следственных связей используются следующие конструкции:

| Конструкция | Пример | Перевод |
|-------------|--------|---------|
| cause | Pollution causes health problems. | Загрязнение вызывает проблемы со здоровьем. |
| lead to | Deforestation leads to habitat loss. | Вырубка лесов ведёт к потере среды обитания. |
| result in | Emissions result in global warming. | Выбросы приводят к глобальному потеплению. |
| contribute to | Cars contribute to air pollution. | Автомобили способствуют загрязнению воздуха. |
| because of | Sea levels rise because of melting ice. | Уровень моря повышается из-за таяния льда. |
| due to | Species disappear due to hunting. | Виды исчезают из-за охоты. |`,
          tasks: [
            "Опишите три вида загрязнения окружающей среды: их источники и последствия, используя конструкции 'cause', 'lead to', 'result in'",
            "Объясните связь между глобальным потеплением и таянием ледников, используя cause/effect конструкции",
            "Переведите и составьте предложения с терминами 'endangered species' и 'biodiversity'"
          ],
          examples: [
          "Deforestation leads to habitat loss — вырубка лесов ведёт к потере среды обитания 🌍",
          "Global warming causes rising sea levels and melting ice caps",
          "Cause and effect: pollution causes health problems, cars contribute to air pollution"
          ],
          keyPoints: [
            "Причины и последствия экологических проблем — Глобальное потепление:",
            "Глобальное потепление — Причины (Causes):",
            "Исчезновение видов — Причины:"
          ]
        },
        {
          title: "Защита окружающей среды",
          description: `Способы защиты природы: переработка, энергосбережение, устойчивое развитие. Учащиеся изучат практические способы защиты окружающей среды и смогут обсуждать экологические инициативы на английском языке.

**Лексика по защите окружающей среды:**

| Английское слово | Транскрипция | Русский перевод |
|------------------|--------------|-----------------|
| recycling | /riːˈsaɪklɪŋ/ | переработка |
| renewable energy | /rɪˈnjuːəbl ˈenədʒi/ | возобновляемая энергия |
| sustainable development | /səˈsteɪnəbl dɪˈveləpmənt/ | устойчивое развитие |
| conservation | /ˌkɒnsəˈveɪʃn/ | сохранение, охрана |
| eco-friendly | /ˌiːkəʊ ˈfrendli/ | экологичный |
| sustainability | /səˌsteɪnəˈbɪləti/ | устойчивость |
| organic | /ɔːˈɡænɪk/ | органический |
| biodegradable | /ˌbaɪəʊdɪˈɡreɪdəbl/ | биоразлагаемый |
| compost | /ˈkɒmpɒst/ | компост |
| solar power | /ˈsəʊlə ˈpaʊə/ | солнечная энергия |
| wind power | /wɪnd ˈpaʊə/ | ветровая энергия |
| carbon neutral | /ˈkɑːbən ˈnjuːtrəl/ | углеродно-нейтральный |

**Принципы 3R (Three R's):**

| Принцип | Английский термин | Значение | Примеры действий |
|---------|-------------------|----------|------------------|
| Reduce | сокращение | уменьшение потребления | покупать меньше, отключать электроприборы |
| Reuse | повторное использование | использование вещей повторно | многоразовые пакеты, бутылки |
| Recycle | переработка | переработка материалов | сортировка мусора, сдача макулатуры |

**Возобновляемые источники энергии:**

| Источник | Английский термин | Преимущества | Недостатки |
|----------|-------------------|--------------|------------|
| Солнечная энергия | solar energy | чистая, неисчерпаемая | зависит от погоды |
| Ветровая энергия | wind energy | чистая, возобновляемая | шум, визуальное загрязнение |
| Гидроэнергия | hydropower | надёжная, эффективная | воздействие на экосистемы рек |
| Геотермальная | geothermal energy | стабильная, чистая | ограниченная доступность |
| Биомасса | biomass | использует отходы | выбросы при сжигании |

**Действия для защиты окружающей среды:**

**Индивидуальные действия:**
- We should reduce, reuse, and recycle. (Мы должны сокращать, повторно использовать и перерабатывать.)
- We can use public transport instead of driving. (Мы можем использовать общественный транспорт вместо вождения.)
- We need to protect natural habitats. (Нам нужно защищать естественную среду.)
- I will bring my own reusable bag when shopping. (Я буду приносить свою многоразовую сумку при покупках.)
- We can plant trees in our community. (Мы можем сажать деревья в нашем сообществе.)

**Глобальные инициативы:**
- Paris Agreement (Парижское соглашение)
- Sustainable Development Goals (Цели устойчивого развития)
- Green energy transition (Переход на зелёную энергию)
- Protected areas (Охраняемые территории)
- Carbon trading (Торговля выбросами)

**Грамматика: Modal verbs for suggestions and obligations**

| Модальный глагол | Значение | Пример |
|------------------|----------|--------|
| should | рекомендация | We should recycle more. |
| can | возможность | We can use solar panels. |
| need to | необходимость | We need to reduce waste. |
| must | обязательство | We must protect nature. |
| could | возможность, предложение | We could carpool to work. |
| ought to | моральный долг | We ought to think about future generations. |

**Полезные фразы для обсуждения экологии:**
- What can individuals do to help the environment? (Что могут сделать отдельные люди для помощи окружающей среде?)
- We all have a responsibility to... (У всех нас есть ответственность...)
- Small changes can make a big difference. (Маленькие изменения могут иметь большое значение.)
- It's important to raise awareness about... (Важно повышать осведомлённость о...)`,
          tasks: [
            "Объясните принципы 3R (Reduce, Reuse, Recycle) и приведите по два примера действий для каждого принципа",
            "Сравните два вида возобновляемой энергии, используя модальные глаголы should, can, need to",
            "Напишите пять предложений о том, что вы можете делать для защиты окружающей среды"
          ],
          examples: [
          "Принципы 3R: Reduce (сократить), Reuse (использовать повторно), Recycle (переработать) ♻️",
          "Renewable energy: solar power, wind energy, hydropower — чистая энергия",
          "We should reduce, reuse, and recycle — modal verb should для рекомендаций"
          ],
          keyPoints: [
            "Действия для защиты окружающей среды — Индивидуальные действия:",
            "Глобальные инициативы — Paris Agreement (Парижское соглашение)",
            "Ключевое понятие: Защита окружающей среды"
          ]
        }
      ]
    },
    {
      topic: "Средства массовой информации",
      lessons: [
        {
          title: "Типы СМИ",
          description: `Изучение типов средств массовой информации: печать, радио, телевидение, интернет-медиа. Учащиеся научатся классифицировать СМИ, обсуждать их роль в обществе и критически оценивать медиаконтент.

**Основная лексика по теме СМИ:**

| Английское слово | Транскрипция | Русский перевод |
|------------------|--------------|-----------------|
| media | /ˈmiːdiə/ | средства массовой информации |
| newspaper | /ˈnjuːzˌpeɪpə/ | газета |
| magazine | /ˌmæɡəˈziːn/ | журнал |
| television | /ˈtelɪvɪʒn/ | телевидение |
| radio | /ˈreɪdiəʊ/ | радио |
| broadcast | /ˈbrɔːdkɑːst/ | трансляция |
| coverage | /ˈkʌvərɪdʒ/ | освещение (событий) |
| journalist | /ˈdʒɜːnəlɪst/ | журналист |
| editor | /ˈedɪtə/ | редактор |
| headline | /ˈhedlaɪn/ | заголовок |
| article | /ˈɑːtɪkl/ | статья |
| report | /rɪˈpɔːt/ | репортаж, доклад |
| correspondent | /ˌkɒrɪˈspɒndənt/ | корреспондент |

**Типы СМИ и их характеристики:**

| Тип СМИ | Английский термин | Преимущества | Недостатки |
|---------|-------------------|--------------|------------|
| Газеты | newspapers | достоверность, глубина анализа | устаревающая информация |
| Журналы | magazines | качественные фото, специализированный контент | периодичность выхода |
| Радио | radio | мобильность, оперативность | отсутствие визуализации |
| Телевидение | television | визуальность, эмоциональность | пассивное потребление |
| Интернет-медиа | online media | актуальность, интерактивность | фейковые новости |
| Подкасты | podcasts | удобство, глубина темы | требует времени |

**Профессии в СМИ:**

| Профессия | Обязанности | Навыки |
|-----------|-------------|--------|
| Journalist | сбор информации, написание статей | коммуникация, письмо |
| Editor | редактирование, утверждение материалов | внимательность, знание языка |
| News anchor | ведение новостей | дикция, презентация |
| Photographer | съёмка фото | визуальное мышление |
| Producer | организация производства | менеджмент, планирование |
| Blogger | создание онлайн-контента | креативность, технические навыки |

**Категории новостей:**

| Категория | Английский термин | Примеры |
|-----------|-------------------|---------|
| Политика | politics | elections, government decisions |
| Экономика | business/economy | stock market, company news |
| Спорт | sports | football matches, Olympics |
| Развлечения | entertainment | movies, music, celebrities |
| Наука и технологии | science and technology | discoveries, gadgets |
| Погода | weather | forecasts, extreme weather |

**Глаголы для описания работы СМИ:**

| Глагол | Значение | Пример |
|--------|----------|--------|
| report | сообщать | The journalist reported the accident. |
| cover | освещать | They covered the election campaign. |
| publish | публиковать | The newspaper publishes daily. |
| broadcast | транслировать | The match was broadcast live. |
| edit | редактировать | She edits the fashion section. |
| investigate | расследовать | They investigated the scandal. |

**Критическое отношение к информации:**

При работе с информацией важно уметь её оценивать:
- Check the source (проверяйте источник)
- Verify the information (подтверждайте информацию)
- Consider multiple perspectives (рассматривайте разные точки зрения)
- Identify bias (определяйте предвзятость)
- Distinguish fact from opinion (отличайте факты от мнений)`,
          tasks: [
            "Сравните два типа СМИ (например, газеты и интернет-медиа), опишите их преимущества и недостатки",
            "Опишите профессию журналиста: обязанности, необходимые навыки, используя глаголы report, cover, investigate",
            "Переведите и объясните, почему важно 'distinguish fact from opinion' при работе с информацией"
          ],
          examples: [
          "Types of media: newspapers, magazines, television, radio, online media 📺",
          "Headline — заголовок статьи, article — статья, broadcast — трансляция",
          "Fake news — ложные новости, важный навык критического мышления"
          ],
          keyPoints: [
            "Критическое отношение к информации — При работе с информацией важно уметь её оценивать:",
            "При работе с информацией важно уметь её оценивать — Check the source (проверяйте источник)",
            "Ключевое понятие: Типы СМИ"
          ]
        },
        {
          title: "Социальные сети",
          description: `Влияние социальных сетей на общество, преимущества и недостатки. Безопасность в интернете. Учащиеся научатся обсуждать роль социальных сетей в современном обществе и правила безопасного поведения онлайн.

**Лексика по теме социальные сети:**

| Английское слово | Транскрипция | Русский перевод |
|------------------|--------------|-----------------|
| social media | /ˈsəʊʃl ˈmiːdiə/ | социальные сети |
| platform | /ˈplætfɔːm/ | платформа |
| profile | /ˈprəʊfaɪl/ | профиль |
| post | /pəʊst/ | публикация, пост |
| feed | /fiːd/ | лента новостей |
| follower | /ˈfɒləʊə/ | подписчик |
| following | /ˈfɒləʊɪŋ/ | подписки |
| like | /laɪk/ | отметка «нравится» |
| share | /ʃeə/ | поделиться |
| comment | /ˈkɒment/ | комментарий |
| hashtag | /ˈhæʃtæɡ/ | хэштег |
| viral | /ˈvaɪərəl/ | вирусный (популярный) |
| influencer | /ˈɪnfluənsə/ | инфлюенсер, блогер |
| trend | /trend/ | тренд, тенденция |

**Популярные социальные платформы:**

| Платформа | Тип | Особенности |
|-----------|-----|-------------|
| Instagram | фото/видео | визуальный контент, stories |
| TikTok | короткие видео | развлекательный контент |
| Twitter/X | микроблогинг | краткие сообщения, новости |
| Facebook | социальная сеть | общение, группы, события |
| YouTube | видеохостинг | длинные видео, обучение |
| LinkedIn | профессиональная сеть | карьера, бизнес-контакты |
| Telegram | мессенджер | каналы, группы, безопасность |

**Преимущества и недостатки социальных сетей:**

**Advantages (Преимущества):**
- Staying connected with friends and family (поддержание связи с друзьями и семьёй)
- Sharing information and ideas (обмен информацией и идеями)
- Building communities (создание сообществ)
- Learning and education (обучение и образование)
- Business opportunities (бизнес-возможности)
- Raising awareness about important issues (привлечение внимания к важным проблемам)

**Disadvantages (Недостатки):**
- Fake news and misinformation (фейковые новости и дезинформация)
- Cyberbullying (кибербуллинг, интернет-травля)
- Addiction and time wasting (зависимость и трата времени)
- Privacy concerns (проблемы конфиденциальности)
- Negative impact on mental health (негативное влияние на психическое здоровье)
- Comparison with others (сравнение себя с другими)

**Безопасность в интернете:**

| Правило | Английская формулировка | Объяснение |
|---------|------------------------|------------|
| Не делитесь личной информацией | Don't share personal information | адрес, телефон, финансовые данные |
| Используйте надёжные пароли | Use strong passwords | комбинация букв, цифр, символов |
| Будьте осторожны с незнакомцами | Be careful with strangers | не всем можно доверять онлайн |
| Проверяйте информацию | Verify information | не верьте всему, что видите |
| Думайте, прежде чем публиковать | Think before you post | информация остаётся в интернете |
| Настройте приватность | Adjust privacy settings | контролируйте, кто видит ваш контент |

**Типы онлайн-угроз:**

| Угроза | Английский термин | Описание |
|--------|-------------------|----------|
| Фишинг | phishing | попытка украсть данные через поддельные сайты |
| Кибербуллинг | cyberbullying | травля в интернете |
| Мошенничество | scam | обман для получения денег |
| Вредоносное ПО | malware | вирусы, трояны |
| Кража личности | identity theft | использование чужих данных |

**Полезные фразы для обсуждения:**
- Social media has changed the way we communicate. (Социальные сети изменили то, как мы общаемся.)
- It's important to maintain a balance between online and offline life. (Важно поддерживать баланс между онлайн и офлайн жизнью.)
- We should be critical of the information we see online. (Мы должны критически относиться к информации, которую видим онлайн.)`,
          tasks: [
            "Опишите преимущества и недостатки одной социальной платформы (на ваш выбор), используя преимущества и недостатки из урока",
            "Перечислите три правила безопасности в интернете и объясните, почему они важны",
            "Напишите о влиянии социальных сетей на молодёжь, используя лексику урока (viral, influencer, cyberbullying)"
          ],
          examples: [
            "Social media — социальные сети, influencer — блогер, viral — ставший вирусным",
            "Cyberbullying — кибербуллинг, phishing — фишинг, не делитесь личной информацией",
            "Подростки проводят в соцсетях значительную часть дня — важна цифровая гигиена"
          ],
          keyPoints: [
            "Преимущества и недостатки социальных сетей — Advantages (Преимущества):",
            "Ключевое понятие: Социальные сети",
            "Ключевое понятие: Социальные сети"
          ]
        }
      ]
    },
    {
      topic: "Научно-технический прогресс",
      lessons: [
        {
          title: "Технологии будущего",
          description: `Изучение лексики по теме технологий: искусственный интеллект, роботы, виртуальная реальность. Учащиеся научатся обсуждать современные технологии и их влияние на будущее человечества.

**Основная технологическая лексика:**

| Английское слово | Транскрипция | Русский перевод |
|------------------|--------------|-----------------|
| technology | /tekˈnɒlədʒi/ | технология |
| innovation | /ˌɪnəˈveɪʃn/ | инновация |
| artificial intelligence | /ˌɑːtɪfɪʃl ɪnˈtelɪdʒəns/ | искусственный интеллект |
| AI | /eɪ aɪ/ | ИИ (сокращение) |
| robotics | /rəʊˈbɒtɪks/ | робототехника |
| virtual reality | /ˈvɜːtʃuəl riˈæləti/ | виртуальная реальность |
| VR | /viː ɑːr/ | ВР (сокращение) |
| augmented reality | /ɔːɡˈmentɪd riˈæləti/ | дополненная реальность |
| automation | /ˌɔːtəˈmeɪʃn/ | автоматизация |
| machine learning | /məˈʃiːn ˈlɜːnɪŋ/ | машинное обучение |
| blockchain | /ˈblɒktʃeɪn/ | блокчейн |
| quantum computing | /ˈkwɒntəm kəmˈpjuːtɪŋ/ | квантовые вычисления |

**Технологии будущего:**

| Технология | Английский термин | Описание | Применение |
|------------|-------------------|----------|------------|
| Автопилотируемые автомобили | self-driving cars | автомобили без водителя | транспорт |
| Умные дома | smart homes | дома с автоматическим управлением | быт |
| Медицинские роботы | medical robots | роботы для хирургии | медицина |
| Освоение космоса | space exploration | изучение космоса | наука |
| Нанотехнологии | nanotechnology | технологии на молекулярном уровне | медицина, производство |
| Биотехнологии | biotechnology | использование живых организмов | медицина, сельское хозяйство |

**Искусственный интеллект (AI):**

**Области применения ИИ:**
| Область | Примеры применения |
|---------|-------------------|
| Healthcare | диагностика заболеваний, разработка лекарств |
| Transportation | беспилотные автомобили, оптимизация маршрутов |
| Education | персонализированное обучение |
| Finance | анализ рынков, обнаружение мошенничества |
| Entertainment | рекомендации контента, игры |
| Customer service | чат-боты, голосовые помощники |

**Виртуальная и дополненная реальность:**

| Технология | Особенности | Применение |
|------------|-------------|------------|
| VR (Virtual Reality) | полное погружение в виртуальный мир | игры, обучение, терапия |
| AR (Augmented Reality) | наложение цифровых объектов на реальность | навигация, образование, розница |
| MR (Mixed Reality) | смешение реального и виртуального | промышленность, медицина |

**Грамматика: Future tenses for predictions**

Для описания будущих технологий используются различные Future times:

| Время | Использование | Пример |
|-------|---------------|--------|
| Future Simple | прогнозы, предсказания | Robots will do most jobs. |
| Future Continuous | действия в процессе в будущем | In 2050, cars will be driving themselves. |
| Future Perfect | завершённые действия к моменту в будущем | By 2030, scientists will have discovered new treatments. |
| be going to | планы, намерения | AI is going to transform many industries. |

**Полезные фразы для обсуждения технологий:**
- Technology is changing our lives in many ways. (Технологии меняют нашу жизнь во многих отношениях.)
- Artificial intelligence will revolutionise many industries. (Искусственный интеллект революционизирует многие отрасли.)
- We need to consider both benefits and risks of new technologies. (Нам нужно учитывать как преимущества, так и риски новых технологий.)
- The pace of technological change is accelerating. (Темпы технологических изменений ускоряются.)`,
          tasks: [
            "Опишите одну технологию будущего: что она делает, как применяется и как изменит нашу жизнь",
            "Составьте три предложения о развитии ИИ, используя Future Simple и Future Perfect",
            "Объясните разницу между VR (Virtual Reality) и AR (Augmented Reality), приведите примеры применения"
          ],
          examples: [
            "AI (artificial intelligence) — искусственный интеллект, machine learning — машинное обучение",
            "VR (virtual reality) — виртуальная реальность, AR (augmented reality) — дополненная реальность",
            "Self-driving cars, smart homes, medical robots — технологии, меняющие будущее"
          ],
          keyPoints: [
            "Искусственный интеллект (AI) — Области применения ИИ:",
            "Ключевое понятие: Технологии будущего",
            "Ключевое понятие: Технологии будущего"
          ]
        },
        {
          title: "Цифровая грамотность",
          description: `Безопасное использование технологий, защита личных данных, критическое мышление в цифровую эпоху. Учащиеся научатся правилам цифровой безопасности и методам защиты личной информации.

**Лексика по цифровой безопасности:**

| Английское слово | Транскрипция | Русский перевод |
|------------------|--------------|-----------------|
| cybersecurity | /ˌsaɪbəsɪˈkjʊərəti/ | кибербезопасность |
| password | /ˈpɑːswɜːd/ | пароль |
| encryption | /ɪnˈkrɪpʃn/ | шифрование |
| phishing | /ˈfɪʃɪŋ/ | фишинг (мошенничество) |
| malware | /ˈmæleweə/ | вредоносное ПО |
| virus | /ˈvaɪrəs/ | вирус |
| backup | /ˈbækʌp/ | резервная копия |
| firewall | /ˈfaɪəwɔːl/ | брандмауэр |
| authentication | /ɔːˌθentɪˈkeɪʃn/ | аутентификация |
| two-factor authentication | /tuː ˈfæktə.../ | двухфакторная аутентификация |
| privacy settings | /ˈprɪvəsi ˈsetɪŋz/ | настройки приватности |
| digital footprint | /ˈdɪdʒɪtl ˈfʊtprɪnt/ | цифровой след |

**Типы киберугроз:**

| Угроза | Английский термин | Описание | Защита |
|--------|-------------------|----------|--------|
| Фишинг | phishing | поддельные письма для кражи данных | проверяйте отправителя |
| Вирусы | viruses | программы, заражающие компьютер | антивирус, не открывайте подозрительные файлы |
| Трояны | trojans | вредоносные программы под видом безопасных | скачивайте только с официальных сайтов |
| Вымогатели | ransomware | блокировка данных для выкупа | резервное копирование |
| Шпионское ПО | spyware | скрытый сбор информации | антивирус, брандмауэр |
| Социальная инженерия | social engineering | манипуляция людьми | не доверяйте незнакомцам |

**Правила создания надёжного пароля:**

| Правило | Английская формулировка | Пример |
|---------|------------------------|--------|
| Минимум 12 символов | At least 12 characters | MyP@ssw0rd2024! |
| Комбинация букв | Mix of upper and lowercase | AbCdEf |
| Цифры | Include numbers | 123456 |
| Специальные символы | Special characters | !@#$%^&* |
| Не использовать личную информацию | Avoid personal information | не использовать дату рождения |
| Уникальный для каждого сайта | Different for each account | разные пароли везде |

**Правила цифровой безопасности:**

**Онлайн-безопасность:**
- Use strong, unique passwords. (Используйте надёжные уникальные пароли.)
- Enable two-factor authentication. (Включите двухфакторную аутентификацию.)
- Don't share personal information. (Не делитесь личной информацией.)
- Be careful with email attachments. (Будьте осторожны с вложениями в письмах.)
- Update your software regularly. (Регулярно обновляйте программное обеспечение.)
- Don't click on suspicious links. (Не нажимайте на подозрительные ссылки.)
- Use secure Wi-Fi networks. (Используйте защищённые Wi-Fi сети.)

**Защита личных данных:**

| Данные | Что нельзя делать | Почему это опасно |
|--------|-------------------|-------------------|
| Адрес | Не публиковать домашний адрес | риск физической безопасности |
| Телефон | Не давать номер незнакомцам | спам, мошенничество |
| Финансы | Не передавать данные карт | кража денег |
| Пароли | Не сообщать никому | взлом аккаунтов |
| Фото | Не публиковать компрометирующие фото | репутация, шантаж |
| Расписание | Не сообщать, когда вас нет дома | риск кражи |

**Цифровой след (Digital Footprint):**

Цифровой след — это вся информация о вас в интернете. Она включает:
- Social media posts (публикации в соцсетях)
- Comments and likes (комментарии и лайки)
- Search history (история поиска)
- Online purchases (онлайн-покупки)
- Uploaded photos and videos (загруженные фото и видео)

Важно помнить: Once something is online, it can be there forever. (Однажды опубликованное в интернете может остаться там навсегда.)

**Грамматика: Imperatives for instructions**

Для инструкций и правил безопасности используется повелительное наклонение:

| Форма | Пример | Перевод |
|-------|--------|---------|
| Положительная | Use strong passwords. | Используйте надёжные пароли. |
| Отрицательная | Don't share personal information. | Не делитесь личной информацией. |
| С 'always' | Always check the source. | Всегда проверяйте источник. |
| С 'never' | Never open suspicious emails. | Никогда не открывайте подозрительные письма. |`,
          tasks: [
            "Создайте правила для надёжного пароля и объясните, почему каждый элемент важен",
            "Опишите три типа киберугроз и методы защиты от них",
            "Напишите пять правил цифровой безопасности для школьников, используя повелительное наклонение"
          ],
          examples: [
            "Phishing — фишинг, malware — вредоносное ПО, two-factor authentication — двухфакторная аутентификация",
            "Use strong, unique passwords — используйте надёжные уникальные пароли для каждого аккаунта",
            "Digital footprint — цифровой след, вся информация о вас в интернете может остаться навсегда"
          ],
          keyPoints: [
            "Правила цифровой безопасности — Онлайн-безопасность:",
            "Цифровой след (Digital Footprint) — Цифровой след — это вся информация о вас в интернете",
            "Цифровой след — это вся информация о вас в интернете. Она включает:"
          ]
        }
      ]
    }
  ]
}

export const games: GameLesson[] = [
  {
    title: "Виды путешествий 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Вопрос 1 по теме \"Виды путешествий\"", options: ["Advantages (Преимущества):","Виды путешествий","Телефонные разговоры:","При заезде:","Профессии в СМИ:"], correctAnswer: "Виды путешествий", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 2 по теме \"Виды путешествий\"", options: ["Грамматика: Imperatives for instructions","Индивидуальные действия:","Основная лексика по теме СМИ:","Основная лексика по теме путешествия:","Виды путешествий"], correctAnswer: "Виды путешествий", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 3 по теме \"Виды путешествий\"", options: ["Преимущества и недостатки социальных сетей:","Объявления в аэропорту:","Лексика по теме поиск работы:","Основная технологическая лексика:","Виды путешествий"], correctAnswer: "Виды путешествий", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 4 по теме \"Виды путешествий\"", options: ["Виды путешествий и их характеристики:","Present Perfect для описания опыта путешествий:","Профессии в современном мире:","Виды путешествий","Принципы 3R (Three R's):"], correctAnswer: "Виды путешествий", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 5 по теме \"Виды путешествий\"", options: ["Основная экологическая лексика:","Фразы для бронирования номера:","Виды путешествий","Принципы 3R (Three R's):","Полезные фразы в аэропорту:"], correctAnswer: "Виды путешествий", hint: "Ответ связан с материалом урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "В аэропорту 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Жалобы и проблемы:","Основная технологическая лексика:","Технологии будущего:","Описание требований к профессии:","-----------------|--------------|----------------"], correctAnswer: "-----------------|--------------|----------------", hint: "Этот термин связан с темой: В аэропорту" },
      { type: 'quiz', question: "Какое понятие относится к теме \"В аэропорту\"?", options: ["Объявления в аэропорту:","Work Experience:","Жалобы и проблемы:","Вопросы о профессиях:","Примеры фраз для cover letter:"], correctAnswer: "Объявления в аэропорту:", hint: "Ответ связан с уроком: В аэропорту" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"В аэропорту\"?", options: ["Сопроводительное письмо (Cover Letter):","инфраструктуре","Disadvantages (Недостатки):","Проблемные ситуации:","Пример резюме (фрагменты):"], correctAnswer: "инфраструктуре", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"В аэропорту\":", options: ["На регистрации:","На паспортном контроле:","Типы багажа и связанные термины:","Основная аэропортовая лексика:","Проблемные ситуации:","Полезные фразы в аэропорту:"], correctAnswer: ["Проблемные ситуации:","Типы багажа и связанные термины:","На паспортном контроле:"], hint: "Ищите термины, которые встречаются в уроке В аэропорту" },
      { type: 'quiz', question: "Что является основным понятием урока \"В аэропорту\"?", options: ["На паспортном контроле:","-------|----------|--------------------","Полезные фразы в аэропорту:","На регистрации:","Этот урок научит учащихся успешно взаимодействовать с персон"], correctAnswer: "Этот урок научит учащихся успешно взаимодействовать с персон", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "В гостинице 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["What time is check-out? (Во сколько выезд?)","Полезные фразы в аэропорту:","What's the rate per night? (Какая цена за ночь?)","Профессии в современном мире:","Фразы для бронирования номера:"], correctAnswer: "What's the rate per night? (Какая цена за ночь?)", hint: "Этот термин связан с темой: В гостинице" },
      { type: 'quiz', question: "Какое понятие относится к теме \"В гостинице\"?", options: ["Категории новостей:","Фразы для бронирования номера:","Наречия, часто используемые с Present Perfect:","Деловая переписка:","Просьбы о услугах:"], correctAnswer: "Просьбы о услугах:", hint: "Ответ связан с уроком: В гостинице" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"В гостинице\"?", options: ["море","Проблемные ситуации:","Структура утверждения:","Просьбы и ответы:","Описание требований к профессии:"], correctAnswer: "море", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"В гостинице\":", options: ["Услуги и проблемы:","Фразы для бронирования номера:","По телефону или онлайн:","Жалобы и проблемы:","При заезде:","Типы номеров в отеле:"], correctAnswer: ["Жалобы и проблемы:","Услуги и проблемы:","При заезде:"], hint: "Ищите термины, которые встречаются в уроке В гостинице" },
      { type: 'quiz', question: "Что является основным понятием урока \"В гостинице\"?", options: ["Учащиеся научатся бронировать проживание","Типы номеров в отеле:","The room is too noisy. (В номере слишком шумно.)","Просьбы о услугах:","Услуги и проблемы:"], correctAnswer: "Учащиеся научатся бронировать проживание", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Мир профессий 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"-----------------|--------------|-----------------...\"?", options: ["Present Perfect для описания опыта путешествий:","Типы онлайн-угроз:","На паспортном контроле:","Основная экологическая лексика:","-----------------"], correctAnswer: "-----------------", hint: "Этот термин связан с темой: Мир профессий" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Мир профессий\"?", options: ["На регистрации:","children","Лексика по теме социальные сети:","Типы киберугроз:","Вопросы о профессиях:"], correctAnswer: "children", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Мир профессий\":", options: ["Описание требований к профессии:","Модальные глаголы для описания профессиональных требований:","Описание профессиональных обязанностей:","Профессии в современном мире:","Описание обязанностей (Present Simple):","Вопросы о профессиях:"], correctAnswer: ["Профессии в современном мире:","Описание профессиональных обязанностей:","Модальные глаголы для описания профессиональных требований:"], hint: "Ищите термины, которые встречаются в уроке Мир профессий" },
      { type: 'quiz', question: "Что является основным понятием урока \"Мир профессий\"?", options: ["Модальные глаголы для описания профессиональных требований","-----------------|--------------|----------------","-----------------","Where do you work? (Где вы работаете?)","----------|----------|-------"], correctAnswer: "Модальные глаголы для описания профессиональных требований", hint: "Ответ содержится в описании урока" },
      { type: 'quiz', question: "Вопрос 5 по теме \"Мир профессий\"", options: ["Полезные фразы для обсуждения:","Просьбы о услугах:","Действия для защиты окружающей среды:","Описание обязанностей (Present Simple):","Основная лексика по теме СМИ:"], correctAnswer: "Описание обязанностей (Present Simple):", hint: "Ответ связан с материалом урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Поиск работы 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Software Developer at TechCorp (2021-present)","Жалобы и проблемы:","Типы киберугроз:","Правила создания надёжного пароля:","Профессии в современном мире:"], correctAnswer: "Software Developer at TechCorp (2021-present)", hint: "Этот термин связан с темой: Поиск работы" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Поиск работы\"?", options: ["Полезные фразы для обсуждения экологии:","Примеры использования:","Objective:","Исчезновение видов:","Искусственный интеллект (AI):"], correctAnswer: "Objective:", hint: "Ответ связан с уроком: Поиск работы" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Поиск работы\"?", options: ["Правила цифровой безопасности:","По телефону или онлайн:","собеседованию","Преимущества и недостатки социальных сетей:","Лексика по защите окружающей среды:"], correctAnswer: "собеседованию", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Поиск работы\":", options: ["Skills:","Пример резюме (фрагменты):","Примеры фраз для cover letter:","Лексика по теме поиск работы:","Сопроводительное письмо (Cover Letter):","Objective:"], correctAnswer: ["Примеры фраз для cover letter:","Пример резюме (фрагменты):","Objective:"], hint: "Ищите термины, которые встречаются в уроке Поиск работы" },
      { type: 'quiz', question: "Что является основным понятием урока \"Поиск работы\"?", options: ["Software Developer at TechCorp (2021-present)","Soft skills","Сопроводительное письмо (Cover Letter):","Пример резюме (фрагменты):","Учащиеся научатся составлять профессиональные документы для "], correctAnswer: "Учащиеся научатся составлять профессиональные документы для ", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Деловое общение 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Глобальные инициативы:","Профессии будущего:","-----------------|--------------|----------------","Основная лексика по теме путешествия:","Типы номеров в отеле:"], correctAnswer: "-----------------|--------------|----------------", hint: "Этот термин связан с темой: Деловое общение" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Деловое общение\"?", options: ["Пример резюме (фрагменты):","Искусственный интеллект (AI):","Услуги и проблемы:","Глаголы для описания работы СМИ:","Деловая переписка:"], correctAnswer: "Деловая переписка:", hint: "Ответ связан с уроком: Деловое общение" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Деловое общение\"?", options: ["Disadvantages (Недостатки):","Просьбы о услугах:","Принципы 3R (Three R's):","презентации","Сопроводительное письмо (Cover Letter):"], correctAnswer: "презентации", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Деловое общение\":", options: ["Структура презентации:","Основная часть:","Полезные фразы для деловых писем:","Просьбы и ответы:","Начало письма:","Завершение письма:"], correctAnswer: ["Структура презентации:","Завершение письма:","Основная часть:"], hint: "Ищите термины, которые встречаются в уроке Деловое общение" },
      { type: 'quiz', question: "Что является основным понятием урока \"Деловое общение\"?", options: ["Презентации:","Основная часть:","Начало разговора:","Профессиональный этикет","Завершение письма:"], correctAnswer: "Профессиональный этикет", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Экологические проблемы 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"-----------------|--------------|-----------------...\"?", options: ["Полезные фразы в аэропорту:","Основная лексика по теме гостиница:","------------|--------|--------","---------","Лексика по защите окружающей среды:"], correctAnswer: "---------", hint: "Этот термин связан с темой: Экологические проблемы" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Экологические проблемы\"?", options: ["Начало письма:","Сопроводительное письмо (Cover Letter):","Исчезновение видов:","Цифровой след (Digital Footprint):","Действия для защиты окружающей среды:"], correctAnswer: "Исчезновение видов:", hint: "Ответ связан с уроком: Экологические проблемы" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Экологические проблемы\"?", options: ["Полезные фразы для обсуждения:","Правила создания надёжного пароля:","Принципы 3R (Three R's):","кризисов","Giant panda (большая панда)"], correctAnswer: "кризисов", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Экологические проблемы\":", options: ["Глобальное потепление:","Грамматика: Cause and Effect (Причина и следствие)","Типы загрязнения:","Основная экологическая лексика:","Причины и последствия экологических проблем:","Исчезновение видов:"], correctAnswer: ["Глобальное потепление:","Исчезновение видов:","Причины и последствия экологических проблем:"], hint: "Ищите термины, которые встречаются в уроке Экологические проблемы" },
      { type: 'quiz', question: "Что является основным понятием урока \"Экологические проблемы\"?", options: ["------------|--------|--------","Учащиеся научатся обсуждать экологические проблемы на англий","Deforestation (вырубка лесов)","Habitat destruction (разрушение среды обитания)","Climate change (изменение климата)"], correctAnswer: "Учащиеся научатся обсуждать экологические проблемы на англий", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Защита окружающей среды 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"-----------------|--------------|-----------------...\"?", options: ["Типы СМИ и их характеристики:","Цифровой след (Digital Footprint):","----","Типы деловых писем:","Исчезновение видов:"], correctAnswer: "----", hint: "Этот термин связан с темой: Защита окружающей среды" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Защита окружающей среды\"?", options: ["Преимущества и недостатки социальных сетей:","Present Perfect для описания опыта путешествий:","Действия для защиты окружающей среды:","Грамматика: Imperatives for instructions","-----"], correctAnswer: "Действия для защиты окружающей среды:", hint: "Ответ связан с уроком: Защита окружающей среды" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Защита окружающей среды\"?", options: ["Полезные фразы для обсуждения:","Типы киберугроз:","Основная аэропортовая лексика:","habitats","Лексика по цифровой безопасности:"], correctAnswer: "habitats", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Защита окружающей среды\":", options: ["Индивидуальные действия:","Действия для защиты окружающей среды:","Глобальные инициативы:","Грамматика: Modal verbs for suggestions and obligations","Принципы 3R (Three R's):","Полезные фразы для обсуждения экологии:"], correctAnswer: ["Грамматика: Modal verbs for suggestions and obligations","Индивидуальные действия:","Глобальные инициативы:"], hint: "Ищите термины, которые встречаются в уроке Защита окружающей среды" },
      { type: 'quiz', question: "Что является основным понятием урока \"Защита окружающей среды\"?", options: ["Действия для защиты окружающей среды:","Индивидуальные действия:","Лексика по защите окружающей среды:","Возобновляемые источники энергии:","Учащиеся изучат практические способы защиты окружающей среды"], correctAnswer: "Учащиеся изучат практические способы защиты окружающей среды", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Типы СМИ 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["----------|-------------|-------","Типы загрязнения:","Индивидуальные действия:","Фразы для бронирования номера:","Цифровой след (Digital Footprint):"], correctAnswer: "----------|-------------|-------", hint: "Этот термин связан с темой: Типы СМИ" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Типы СМИ\"?", options: ["Грамматика: Imperatives for instructions","Основная технологическая лексика:","Описание обязанностей (Present Simple):","Полезные фразы в аэропорту:","Критическое отношение к информации:"], correctAnswer: "Критическое отношение к информации:", hint: "Ответ связан с уроком: Типы СМИ" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Типы СМИ\"?", options: ["Objective:","----------|-------------------|--------","медиаконтент","Структура презентации:","Типы СМИ и их характеристики:"], correctAnswer: "медиаконтент", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Типы СМИ\":", options: ["Категории новостей:","Профессии в СМИ:","Глаголы для описания работы СМИ:","Критическое отношение к информации:","Основная лексика по теме СМИ:","Типы СМИ и их характеристики:"], correctAnswer: ["Критическое отношение к информации:","Основная лексика по теме СМИ:","Глаголы для описания работы СМИ:"], hint: "Ищите термины, которые встречаются в уроке Типы СМИ" },
      { type: 'quiz', question: "Что является основным понятием урока \"Типы СМИ\"?", options: ["Check the source (проверяйте источник)","-------|----------|-------","Профессии в СМИ:","Учащиеся научатся классифицировать СМИ","----------|-------------------|--------"], correctAnswer: "Учащиеся научатся классифицировать СМИ", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Социальные сети 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["На регистрации:","-------|-------------------|---------","Безопасность в интернете:","Основная технологическая лексика:","Полезные фразы для обсуждения экологии:"], correctAnswer: "-------|-------------------|---------", hint: "Этот термин связан с темой: Социальные сети" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Социальные сети\"?", options: ["Фразы для бронирования номера:","Грамматика: Imperatives for instructions","Основная экологическая лексика:","Основная лексика по теме гостиница:","Disadvantages (Недостатки):"], correctAnswer: "Disadvantages (Недостатки):", hint: "Ответ связан с уроком: Социальные сети" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Социальные сети\"?", options: ["Building communities (создание сообществ)","общаемся","Полезные фразы в аэропорту:","При заезде:","Защита личных данных:"], correctAnswer: "общаемся", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Социальные сети\":", options: ["Типы онлайн-угроз:","Популярные социальные платформы:","Disadvantages (Недостатки):","Безопасность в интернете:","Лексика по теме социальные сети:","Преимущества и недостатки социальных сетей:"], correctAnswer: ["Disadvantages (Недостатки):","Типы онлайн-угроз:","Преимущества и недостатки социальных сетей:"], hint: "Ищите термины, которые встречаются в уроке Социальные сети" },
      { type: 'quiz', question: "Что является основным понятием урока \"Социальные сети\"?", options: ["Безопасность в интернете","Advantages (Преимущества):","Business opportunities (бизнес-возможности)","Преимущества и недостатки социальных сетей:","----------|-----|------------"], correctAnswer: "Безопасность в интернете", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Технологии будущего 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["--------|------------------","Наречия, часто используемые с Present Perfect:","Основная аэропортовая лексика:","Типы багажа и связанные термины:","-----------|-------------|-----------"], correctAnswer: "-----------|-------------|-----------", hint: "Этот термин связан с темой: Технологии будущего" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Технологии будущего\"?", options: ["Полезные фразы для обсуждения путешествий:","Типы номеров в отеле:","Профессии в современном мире:","Грамматика: Future tenses for predictions","Основная часть:"], correctAnswer: "Грамматика: Future tenses for predictions", hint: "Ответ связан с уроком: Технологии будущего" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Технологии будущего\"?", options: ["Грамматика: Future tenses for predictions","Структура утверждения:","Основная технологическая лексика:","Описание профессиональных обязанностей:","themselves"], correctAnswer: "themselves", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Технологии будущего\":", options: ["Технологии будущего:","Полезные фразы для обсуждения технологий:","Виртуальная и дополненная реальность:","Искусственный интеллект (AI):","Области применения ИИ:","Основная технологическая лексика:"], correctAnswer: ["Виртуальная и дополненная реальность:","Искусственный интеллект (AI):","Основная технологическая лексика:"], hint: "Ищите термины, которые встречаются в уроке Технологии будущего" },
      { type: 'quiz', question: "Что является основным понятием урока \"Технологии будущего\"?", options: ["Виртуальная и дополненная реальность:","Искусственный интеллект (AI):","Грамматика: Future tenses for predictions","--------|------------------","Учащиеся научатся обсуждать современные технологии и их влия"], correctAnswer: "Учащиеся научатся обсуждать современные технологии и их влия", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Цифровая грамотность 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["--------|------------------------|-------","-------|-------------------|------------------","Онлайн-безопасность:","Области применения ИИ:","Лексика по теме поиск работы:"], correctAnswer: "--------|------------------------|-------", hint: "Этот термин связан с темой: Цифровая грамотность" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Цифровая грамотность\"?", options: ["Типы онлайн-угроз:","Основная часть:","Полезные фразы в аэропорту:","Правила цифровой безопасности:","Лексика по цифровой безопасности:"], correctAnswer: "Лексика по цифровой безопасности:", hint: "Ответ связан с уроком: Цифровая грамотность" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Цифровая грамотность\"?", options: ["Услуги и проблемы:","characters","Грамматика: Future tenses for predictions","Описание профессиональных обязанностей:","Жалобы и проблемы:"], correctAnswer: "characters", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Цифровая грамотность\":", options: ["Правила создания надёжного пароля:","Онлайн-безопасность:","Грамматика: Imperatives for instructions","Цифровой след (Digital Footprint):","Правила цифровой безопасности:","Типы киберугроз:"], correctAnswer: ["Правила создания надёжного пароля:","Грамматика: Imperatives for instructions","Типы киберугроз:"], hint: "Ищите термины, которые встречаются в уроке Цифровая грамотность" },
      { type: 'quiz', question: "Что является основным понятием урока \"Цифровая грамотность\"?", options: ["-----------------|--------------|----------------","Правила цифровой безопасности:","Правила создания надёжного пароля:","безопасность","Учащиеся научатся правилам цифровой безопасности и методам з"], correctAnswer: "Учащиеся научатся правилам цифровой безопасности и методам з", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  }
] = [
  {
    title: "Виды путешествий 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Вопрос 1 по теме \"Виды путешествий\"", options: ["Описание профессиональных обязанностей:","Презентации:","Present Perfect для описания опыта путешествий:","Жалобы и проблемы:","Виды путешествий"], correctAnswer: "Виды путешествий", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 2 по теме \"Виды путешествий\"", options: ["Типы киберугроз:","Структура презентации:","Типы деловых писем:","Виды путешествий","Технологии будущего:"], correctAnswer: "Виды путешествий", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 3 по теме \"Виды путешествий\"", options: ["Глобальное потепление:","Виды путешествий","Просьбы и ответы:","Лексика по теме поиск работы:","Типы онлайн-угроз:"], correctAnswer: "Виды путешествий", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 4 по теме \"Виды путешествий\"", options: ["Виды путешествий","Примеры использования:","Лексика по защите окружающей среды:","При заезде:","Презентации:"], correctAnswer: "Виды путешествий", hint: "Ответ связан с материалом урока" },
      { type: 'quiz', question: "Вопрос 5 по теме \"Виды путешествий\"", options: ["Основная лексика по теме СМИ:","Виды путешествий","Профессии в СМИ:","Основная экологическая лексика:","Основная аэропортовая лексика:"], correctAnswer: "Виды путешествий", hint: "Ответ связан с материалом урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "В аэропорту 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Полезные фразы для обсуждения:","Типы номеров в отеле:","Here is my passport. (Вот мой паспорт.)","Типы киберугроз:","Жалобы и проблемы:"], correctAnswer: "Here is my passport. (Вот мой паспорт.)", hint: "Этот термин связан с темой: В аэропорту" },
      { type: 'quiz', question: "Какое понятие относится к теме \"В аэропорту\"?", options: ["Объявления в аэропорту:","Основная лексика по теме гостиница:","Лексика по цифровой безопасности:","Индивидуальные действия:","Глобальное потепление:"], correctAnswer: "Объявления в аэропорту:", hint: "Ответ связан с уроком: В аэропорту" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"В аэропорту\"?", options: ["Грамматика: Future tenses for predictions","На паспортном контроле:","инфраструктуре","Типы загрязнения:","Лексика по теме социальные сети:"], correctAnswer: "инфраструктуре", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"В аэропорту\":", options: ["Объявления в аэропорту:","Полезные фразы в аэропорту:","Типы багажа и связанные термины:","Основная аэропортовая лексика:","Проблемные ситуации:","На паспортном контроле:"], correctAnswer: ["Типы багажа и связанные термины:","На паспортном контроле:","Полезные фразы в аэропорту:"], hint: "Ищите термины, которые встречаются в уроке В аэропорту" },
      { type: 'quiz', question: "Что является основным понятием урока \"В аэропорту\"?", options: ["Этот урок научит учащихся успешно взаимодействовать с персон","Полезные фразы в аэропорту:","-----------------|--------------|----------------","Основная аэропортовая лексика:","На регистрации:"], correctAnswer: "Этот урок научит учащихся успешно взаимодействовать с персон", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "В гостинице 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Популярные социальные платформы:","The room is too noisy. (В номере слишком шумно.)","Основная аэропортовая лексика:","Категории новостей:","Skills:"], correctAnswer: "The room is too noisy. (В номере слишком шумно.)", hint: "Этот термин связан с темой: В гостинице" },
      { type: 'quiz', question: "Какое понятие относится к теме \"В гостинице\"?", options: ["Objective:","Критическое отношение к информации:","Типы загрязнения:","Типы номеров в отеле:","При заезде:"], correctAnswer: "Типы номеров в отеле:", hint: "Ответ связан с уроком: В гостинице" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"В гостинице\"?", options: ["Области применения ИИ:","Проблемные ситуации:","Полезные фразы в аэропорту:","проживания","Глобальное потепление:"], correctAnswer: "проживания", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"В гостинице\":", options: ["По телефону или онлайн:","Типы номеров в отеле:","При заезде:","Основная лексика по теме гостиница:","Жалобы и проблемы:","Услуги и проблемы:"], correctAnswer: ["По телефону или онлайн:","Основная лексика по теме гостиница:","Услуги и проблемы:"], hint: "Ищите термины, которые встречаются в уроке В гостинице" },
      { type: 'quiz', question: "Что является основным понятием урока \"В гостинице\"?", options: ["The Wi-Fi password, please? (Пароль от Wi","Услуги и проблемы:","Here's your key card. (Вот ваша ключ-карта.)","Учащиеся научатся бронировать проживание","-----------|----------|------------"], correctAnswer: "Учащиеся научатся бронировать проживание", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Мир профессий 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"----------------|--------------|-----------------|...\"?", options: ["Вопросы о профессиях:","-----------------|--------------|----------------","На регистрации:","Пример резюме (фрагменты):","Технологии будущего:"], correctAnswer: "-----------------|--------------|----------------", hint: "Этот термин связан с темой: Мир профессий" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Мир профессий\"?", options: ["Основная лексика по теме СМИ:","Профессии в современном мире:","Пример резюме (фрагменты):","Типы СМИ и их характеристики:","Основная технологическая лексика:"], correctAnswer: "Профессии в современном мире:", hint: "Ответ связан с уроком: Мир профессий" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Мир профессий\"?", options: ["Принципы 3R (Three R's):","Профессии в современном мире:","Основная лексика по теме СМИ:","Лексика по теме социальные сети:","предпочтения"], correctAnswer: "предпочтения", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Мир профессий\":", options: ["Профессии в современном мире:","Профессии будущего:","Вопросы о профессиях:","Описание обязанностей (Present Simple):","Описание требований к профессии:","Модальные глаголы для описания профессиональных требований:"], correctAnswer: ["Модальные глаголы для описания профессиональных требований:","Описание обязанностей (Present Simple):","Описание требований к профессии:"], hint: "Ищите термины, которые встречаются в уроке Мир профессий" },
      { type: 'quiz', question: "Что является основным понятием урока \"Мир профессий\"?", options: ["Модальные глаголы для описания профессиональных требований","Профессии будущего:","Профессии в современном мире:","-----------------","Описание требований к профессии:"], correctAnswer: "Модальные глаголы для описания профессиональных требований", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Поиск работы 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Пример резюме (фрагменты):","Типы багажа и связанные термины:","Цифровой след (Digital Footprint):","Телефонные разговоры:","-------|---------------------|-----------"], correctAnswer: "-------|---------------------|-----------", hint: "Этот термин связан с темой: Поиск работы" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Поиск работы\"?", options: ["Профессии будущего:","Пример резюме (фрагменты):","Индивидуальные действия:","Типы СМИ и их характеристики:","Вопросы о профессиях:"], correctAnswer: "Пример резюме (фрагменты):", hint: "Ответ связан с уроком: Поиск работы" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Поиск работы\"?", options: ["Жалобы и проблемы:","candidate","Типы номеров в отеле:","Основная технологическая лексика:","Основная часть:"], correctAnswer: "candidate", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Поиск работы\":", options: ["Skills:","Структура резюме (CV):","Сопроводительное письмо (Cover Letter):","Лексика по теме поиск работы:","Пример резюме (фрагменты):","Work Experience:"], correctAnswer: ["Пример резюме (фрагменты):","Сопроводительное письмо (Cover Letter):","Лексика по теме поиск работы:"], hint: "Ищите термины, которые встречаются в уроке Поиск работы" },
      { type: 'quiz', question: "Что является основным понятием урока \"Поиск работы\"?", options: ["Сопроводительное письмо (Cover Letter):","Пример резюме (фрагменты):","Учащиеся научатся составлять профессиональные документы для ","Soft skills","-----------------|--------------|----------------"], correctAnswer: "Учащиеся научатся составлять профессиональные документы для ", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Деловое общение 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Структура резюме (CV):","На паспортном контроле:","Полезные фразы для обсуждения технологий:","This is John Smith speaking. (Это Джон Смит.)","Objective:"], correctAnswer: "This is John Smith speaking. (Это Джон Смит.)", hint: "Этот термин связан с темой: Деловое общение" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Деловое общение\"?", options: ["Телефонные разговоры:","Онлайн-безопасность:","Основная лексика по теме путешествия:","Принципы 3R (Three R's):","Критическое отношение к информации:"], correctAnswer: "Телефонные разговоры:", hint: "Ответ связан с уроком: Деловое общение" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Деловое общение\"?", options: ["Принципы 3R (Three R's):","Виды путешествий и их характеристики:","Основная часть:","inquiry","На паспортном контроле:"], correctAnswer: "inquiry", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Деловое общение\":", options: ["Деловая переписка:","Завершение письма:","Начало разговора:","Типы деловых писем:","Структура презентации:","Полезные фразы для деловых писем:"], correctAnswer: ["Типы деловых писем:","Завершение письма:","Полезные фразы для деловых писем:"], hint: "Ищите термины, которые встречаются в уроке Деловое общение" },
      { type: 'quiz', question: "Что является основным понятием урока \"Деловое общение\"?", options: ["Профессиональный этикет","Просьбы и ответы:","Основная деловая лексика:","Полезные фразы для деловых писем:","Начало разговора:"], correctAnswer: "Профессиональный этикет", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Экологические проблемы 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"-----------------|--------------|-----------------...\"?", options: ["Структура презентации:","Основная деловая лексика:","Искусственный интеллект (AI):","---------","Skills:"], correctAnswer: "---------", hint: "Этот термин связан с темой: Экологические проблемы" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Экологические проблемы\"?", options: ["Типы загрязнения:","Профессии в современном мире:","На регистрации:","Просьбы и ответы:","Типы киберугроз:"], correctAnswer: "Типы загрязнения:", hint: "Ответ связан с уроком: Экологические проблемы" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Экологические проблемы\"?", options: ["Основная часть:","Rising sea levels (повышение уровня моря)","Advantages (Преимущества):","loss","Структура презентации:"], correctAnswer: "loss", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Экологические проблемы\":", options: ["Исчезновение видов:","Типы загрязнения:","Основная экологическая лексика:","Причины и последствия экологических проблем:","Грамматика: Cause and Effect (Причина и следствие)","Глобальное потепление:"], correctAnswer: ["Грамматика: Cause and Effect (Причина и следствие)","Типы загрязнения:","Исчезновение видов:"], hint: "Ищите термины, которые встречаются в уроке Экологические проблемы" },
      { type: 'quiz', question: "Что является основным понятием урока \"Экологические проблемы\"?", options: ["Учащиеся научатся обсуждать экологические проблемы на англий","Глобальное потепление:","Типы загрязнения:","Habitat destruction (разрушение среды обитания)","Giant panda (большая панда)"], correctAnswer: "Учащиеся научатся обсуждать экологические проблемы на англий", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Защита окружающей среды 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"-----------------|--------------|-----------------...\"?", options: ["Основная технологическая лексика:","Disadvantages (Недостатки):","Типы киберугроз:","Структура утверждения:","----"], correctAnswer: "----", hint: "Этот термин связан с темой: Защита окружающей среды" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Защита окружающей среды\"?", options: ["Типы загрязнения:","Правила создания надёжного пароля:","Глаголы для описания работы СМИ:","На регистрации:","Полезные фразы для обсуждения экологии:"], correctAnswer: "Полезные фразы для обсуждения экологии:", hint: "Ответ связан с уроком: Защита окружающей среды" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Защита окружающей среды\"?", options: ["Objective:","Описание обязанностей (Present Simple):","Примеры использования:","развитие","Возобновляемые источники энергии:"], correctAnswer: "развитие", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Защита окружающей среды\":", options: ["Глобальные инициативы:","Лексика по защите окружающей среды:","Полезные фразы для обсуждения экологии:","Возобновляемые источники энергии:","Индивидуальные действия:","Принципы 3R (Three R's):"], correctAnswer: ["Принципы 3R (Three R's):","Лексика по защите окружающей среды:","Индивидуальные действия:"], hint: "Ищите термины, которые встречаются в уроке Защита окружающей среды" },
      { type: 'quiz', question: "Что является основным понятием урока \"Защита окружающей среды\"?", options: ["Лексика по защите окружающей среды:","Учащиеся изучат практические способы защиты окружающей среды","Принципы 3R (Three R's):","-----------------|----------|-------","Полезные фразы для обсуждения экологии:"], correctAnswer: "Учащиеся изучат практические способы защиты окружающей среды", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Типы СМИ 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Полезные фразы для деловых писем:","Популярные социальные платформы:","Identify bias (определяйте предвзятость)","Типы деловых писем:","Типы номеров в отеле:"], correctAnswer: "Identify bias (определяйте предвзятость)", hint: "Этот термин связан с темой: Типы СМИ" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Типы СМИ\"?", options: ["Критическое отношение к информации:","Описание обязанностей (Present Simple):","Просьбы о услугах:","Просьбы и ответы:","Структура презентации:"], correctAnswer: "Критическое отношение к информации:", hint: "Ответ связан с уроком: Типы СМИ" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Типы СМИ\"?", options: ["Правила цифровой безопасности:","Проблемные ситуации:","медиаконтент","Полезные фразы в аэропорту:","Правила создания надёжного пароля:"], correctAnswer: "медиаконтент", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Типы СМИ\":", options: ["Критическое отношение к информации:","Основная лексика по теме СМИ:","Профессии в СМИ:","Глаголы для описания работы СМИ:","Типы СМИ и их характеристики:","Категории новостей:"], correctAnswer: ["Категории новостей:","Основная лексика по теме СМИ:","Типы СМИ и их характеристики:"], hint: "Ищите термины, которые встречаются в уроке Типы СМИ" },
      { type: 'quiz', question: "Что является основным понятием урока \"Типы СМИ\"?", options: ["Check the source (проверяйте источник)","Критическое отношение к информации:","Глаголы для описания работы СМИ:","Учащиеся научатся классифицировать СМИ","Категории новостей:"], correctAnswer: "Учащиеся научатся классифицировать СМИ", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Социальные сети 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Профессии будущего:","Основная часть:","Лексика по защите окружающей среды:","Правила цифровой безопасности:","--------|------------------------|-----------"], correctAnswer: "--------|------------------------|-----------", hint: "Этот термин связан с темой: Социальные сети" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Социальные сети\"?", options: ["Типы онлайн-угроз:","Проблемные ситуации:","Advantages (Преимущества):","Причины и последствия экологических проблем:","Типы багажа и связанные термины:"], correctAnswer: "Advantages (Преимущества):", hint: "Ответ связан с уроком: Социальные сети" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Социальные сети\"?", options: ["Начало письма:","Advantages (Преимущества):","Завершение письма:","life","Описание обязанностей (Present Simple):"], correctAnswer: "life", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Социальные сети\":", options: ["Лексика по теме социальные сети:","Безопасность в интернете:","Advantages (Преимущества):","Типы онлайн-угроз:","Преимущества и недостатки социальных сетей:","Disadvantages (Недостатки):"], correctAnswer: ["Advantages (Преимущества):","Лексика по теме социальные сети:","Типы онлайн-угроз:"], hint: "Ищите термины, которые встречаются в уроке Социальные сети" },
      { type: 'quiz', question: "Что является основным понятием урока \"Социальные сети\"?", options: ["Безопасность в интернете","Популярные социальные платформы:","----------|-----|------------","Cyberbullying (кибербуллинг, интернет-травля)","Типы онлайн-угроз:"], correctAnswer: "Безопасность в интернете", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Технологии будущего 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"----------|-------------------|----------|--------...\"?", options: ["Типы киберугроз:","-----------|-------------------|----------|-------","Типы онлайн-угроз:","Принципы 3R (Three R's):","Основная деловая лексика:"], correctAnswer: "-----------|-------------------|----------|-------", hint: "Этот термин связан с темой: Технологии будущего" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Технологии будущего\"?", options: ["Глаголы для описания работы СМИ:","Безопасность в интернете:","Искусственный интеллект (AI):","Примеры использования:","Жалобы и проблемы:"], correctAnswer: "Искусственный интеллект (AI):", hint: "Ответ связан с уроком: Технологии будущего" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Технологии будущего\"?", options: ["themselves","Основная технологическая лексика:","Описание обязанностей (Present Simple):","Структура презентации:","-----------|-------------|-----------"], correctAnswer: "themselves", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Технологии будущего\":", options: ["Полезные фразы для обсуждения технологий:","Основная технологическая лексика:","Технологии будущего:","Грамматика: Future tenses for predictions","Виртуальная и дополненная реальность:","Области применения ИИ:"], correctAnswer: ["Виртуальная и дополненная реальность:","Полезные фразы для обсуждения технологий:","Грамматика: Future tenses for predictions"], hint: "Ищите термины, которые встречаются в уроке Технологии будущего" },
      { type: 'quiz', question: "Что является основным понятием урока \"Технологии будущего\"?", options: ["Грамматика: Future tenses for predictions","Полезные фразы для обсуждения технологий:","Виртуальная и дополненная реальность:","Технологии будущего:","Учащиеся научатся обсуждать современные технологии и их влия"], correctAnswer: "Учащиеся научатся обсуждать современные технологии и их влия", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  },
  {
    title: "Цифровая грамотность 📚",
    subject: "Иностранный язык",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Что означает термин \"основное понятие темы...\"?", options: ["Области применения ИИ:","Структура резюме (CV):","безопасность","Услуги и проблемы:","Действия для защиты окружающей среды:"], correctAnswer: "безопасность", hint: "Этот термин связан с темой: Цифровая грамотность" },
      { type: 'quiz', question: "Какое понятие относится к теме \"Цифровая грамотность\"?", options: ["На регистрации:","Защита личных данных:","Advantages (Преимущества):","Основная лексика по теме гостиница:","Жалобы и проблемы:"], correctAnswer: "Защита личных данных:", hint: "Ответ связан с уроком: Цифровая грамотность" },
      { type: 'quiz', question: "Какое из следующих утверждений верно относительно темы \"Цифровая грамотность\"?", options: ["Enable two","Технологии будущего:","-------|-------------------|------------------","Виды путешествий и их характеристики:","characters"], correctAnswer: "characters", hint: "Обратите внимание на ключевое слово в описании урока" },
      { type: 'find', question: "Выберите понятия, связанные с темой \"Цифровая грамотность\":", options: ["Правила цифровой безопасности:","Типы киберугроз:","Грамматика: Imperatives for instructions","Защита личных данных:","Лексика по цифровой безопасности:","Правила создания надёжного пароля:"], correctAnswer: ["Грамматика: Imperatives for instructions","Правила цифровой безопасности:","Типы киберугроз:"], hint: "Ищите термины, которые встречаются в уроке Цифровая грамотность" },
      { type: 'quiz', question: "Что является основным понятием урока \"Цифровая грамотность\"?", options: ["-----------------|--------------|----------------","Social media posts (публикации в соцсетях)","------|--------|--------","Use secure Wi","Учащиеся научатся правилам цифровой безопасности и методам з"], correctAnswer: "Учащиеся научатся правилам цифровой безопасности и методам з", hint: "Ответ содержится в описании урока" }
    ],
    reward: { stars: 3, message: "Отлично! Ты справился! 🎉" }
  }
] = [
  {
    title: "Виды путешествий",
    subject: "Иностранный язык",
    icon: "Plane",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What does 'destination' mean?", options: ["Place to go", "Type of food", "Transport", "Currency", "Другой ответ"],
      keyPoints: [
        "Примеры использования — I have visited Paris twice",
        "Наречия, часто используемые с Present Perfect — never (никогда) — I have never visited Australia",
        "just (только что) — She has just arrived at the airport.",
      ], correctAnswer: "Place to go", hint: "Where you're heading" },
      { type: 'quiz', question: "I have never visited Paris. (никогда не)", options: ["never", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "never", hint: "Negative experience" },
      { type: 'quiz', question: "Present Perfect is used for:", options: ["Life experience", "Past actions with specific time", "Future plans", "Daily routine", "Другой ответ"], correctAnswer: "Life experience", hint: "At any time in your life" },
      { type: 'quiz', question: "Sightseeing means seeing sights. (достопримечательности)", options: ["sights", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "sights", hint: "Tourist attractions" },
      { type: 'quiz', question: "Which word means 'путешествие'?", options: ["journey", "hotel", "ticket", "passport", "Другой ответ"], correctAnswer: "journey", hint: "Going from one place to another" },
      { type: 'quiz', question: "My destination is Paris this summer. (место назначения)", options: ["destination", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "destination", hint: "Where I'm going" },
      { type: 'quiz', question: "'Accommodation' means:", options: ["Place to stay", "Type of food", "Travel method", "Luggage", "Другой ответ"], correctAnswer: "Place to stay", hint: "Where you sleep during travel" },
      { type: 'quiz', question: "Have you ever travelled by train? (путешествовали)", options: ["travelled", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "travelled", hint: "Past participle of travel" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь лексику путешествий!" }
  },
  {
    title: "В аэропорту",
    subject: "Иностранный язык",
    icon: "Plane",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Boarding pass is your ticket to board the plane. (посадочный)", options: ["Boarding", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"],
      keyPoints: [
        "Полезные фразы в аэропорту — На регистрации:",
        "На регистрации — Can I have a window/aisle seat",
        "Проблемные ситуации — My flight has been delayed/cancelled",
      ], correctAnswer: "Boarding", hint: "Required for flight" },
      { type: 'quiz', question: "Where do you pick up luggage after arrival?", options: ["Baggage claim", "Check-in", "Gate", "Customs", "Другой ответ"], correctAnswer: "Baggage claim", hint: "After arrival" },
      { type: 'quiz', question: "My flight was delayed for two hours. (задержан)", options: ["delayed", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "delayed", hint: "Not on time" },
      { type: 'quiz', question: "'Gate' at the airport means:", options: ["Exit to board the plane", "Entrance to building", "Parking area", "Ticket office", "Другой ответ"], correctAnswer: "Exit to board the plane", hint: "Boarding area" },
      { type: 'quiz', question: "I'd like a window seat, please. (место у окна)", options: ["window", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "window", hint: "You can see outside" },
      { type: 'quiz', question: "What is 'customs'?", options: ["Border control for goods", "Ticket office", "Restaurant", "Hotel desk", "Другой ответ"], correctAnswer: "Border control for goods", hint: "Checking what you bring" },
      { type: 'quiz', question: "Where is the check-in counter? (стойка)", options: ["counter", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "counter", hint: "Desk for registration" },
      { type: 'quiz', question: "'Departure lounge' is where you:", options: ["Wait for your flight", "Pick up luggage", "Buy tickets", "Eat dinner", "Другой ответ"], correctAnswer: "Wait for your flight", hint: "Before boarding" }
    ],
    reward: { stars: 3, message: "Ты готов к путешествию на самолёте!" }
  },
  {
    title: "В гостинице",
    subject: "Иностранный язык",
    icon: "Hotel",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I'd like to book a room for two nights. (забронировать)", options: ["book", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"],
      keyPoints: [
        "Фразы для бронирования номера — По телефону или онлайн:",
        "По телефону или онлайн — What's the rate per night",
        "При заезде — I'd like to check in, please",
      ], correctAnswer: "book", hint: "Make a reservation" },
      { type: 'quiz', question: "What does 'complimentary' mean?", options: ["Free of charge", "Expensive", "Reserved", "Unavailable", "Другой ответ"], correctAnswer: "Free of charge", hint: "Included at no cost" },
      { type: 'quiz', question: "Is breakfast included? (включено)", options: ["included", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "included", hint: "Part of the deal" },
      { type: 'quiz', question: "'Check-out' means:", options: ["Leaving the hotel", "Arriving at hotel", "Paying extra", "Ordering food", "Другой ответ"], correctAnswer: "Leaving the hotel", hint: "End of stay" },
      { type: 'quiz', question: "Do you have any vacancies for tonight? (свободные номера)", options: ["vacancies", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "vacancies", hint: "Empty rooms available" },
      { type: 'quiz', question: "'Room service' provides:", options: ["Food delivered to your room", "Cleaning only", "Transportation", "Tickets", "Другой ответ"], correctAnswer: "Food delivered to your room", hint: "Ordering food to your door" },
      { type: 'quiz', question: "What time is check-out? (выезд)", options: ["check-out", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "check-out", hint: "When you leave the hotel" },
      { type: 'quiz', question: "A 'twin room' has:", options: ["Two separate beds", "One double bed", "Three beds", "No bed", "Другой ответ"], correctAnswer: "Two separate beds", hint: "Not for couples" }
    ],
    reward: { stars: 3, message: "Ты можешь заселиться в отеле!" }
  },
  {
    title: "Мир профессий",
    subject: "Иностранный язык",
    icon: "Briefcase",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "A doctor treats patients in a hospital. (врач)", options: ["doctor", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"],
      keyPoints: [
        "Вопросы о профессиях — What do you do",
        "Ключевое понятие: Мир профессий",
        "Ключевое понятие: Мир профессий",
      ], correctAnswer: "doctor", hint: "Medical professional" },
      { type: 'quiz', question: "Who designs buildings?", options: ["Architect", "Doctor", "Teacher", "Driver", "Другой ответ"], correctAnswer: "Architect", hint: "Construction plans" },
      { type: 'quiz', question: "I work as a software developer at Google. (разработчик)", options: ["developer", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "developer", hint: "Creates programs" },
      { type: 'quiz', question: "'Must' expresses:", options: ["Obligation", "Suggestion", "Permission", "Ability", "Другой ответ"], correctAnswer: "Obligation", hint: "Necessity" },
      { type: 'quiz', question: "A journalist writes articles for newspapers. (журналист)", options: ["journalist", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "journalist", hint: "Media professional" },
      { type: 'quiz', question: "What does an accountant do?", options: ["Manages finances", "Treats patients", "Teaches students", "Drives trucks", "Другой ответ"], correctAnswer: "Manages finances", hint: "Numbers and money" },
      { type: 'quiz', question: "You must be good at math to be an engineer. (должны)", options: ["must", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "must", hint: "Requirement" },
      { type: 'quiz', question: "'Software developer' creates:", options: ["Computer programs", "Buildings", "Medicines", "Food", "Другой ответ"], correctAnswer: "Computer programs", hint: "IT professional" }
    ],
    reward: { stars: 3, message: "Ты хорошо знаешь названия профессий!" }
  },
  {
    title: "Поиск работы",
    subject: "Иностранный язык",
    icon: "FileText",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "A CV is a document about your experience. (резюме)", options: ["CV", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"],
      keyPoints: [
        "Пример резюме (фрагменты) — Objective:",
        "Сопроводительное письмо (Cover Letter) — Структура сопроводительного письма:",
        "Структура сопроводительного письма — Приветствие: Dear Mr",
      ], correctAnswer: "CV", hint: "Or resume" },
      { type: 'quiz', question: "What is an 'interview'?", options: ["Job meeting with employer", "Written test", "Email exchange", "Phone call only", "Другой ответ"], correctAnswer: "Job meeting with employer", hint: "Face to face discussion" },
      { type: 'quiz', question: "Please find my CV attached to this email. (приложенным)", options: ["attached", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "attached", hint: "Included in email" },
      { type: 'quiz', question: "'Strengths' means:", options: ["Strong points", "Weaknesses", "Hobbies", "Skills only", "Другой ответ"], correctAnswer: "Strong points", hint: "Positive qualities" },
      { type: 'quiz', question: "A cover letter explains why you want the job. (сопроводительное)", options: ["cover", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "cover", hint: "Goes with CV" },
      { type: 'quiz', question: "A 'vacancy' is:", options: ["An open job position", "A holiday", "A meeting", "A contract", "Другой ответ"], correctAnswer: "An open job position", hint: "Job opening" },
      { type: 'quiz', question: "What are your strengths and weaknesses? (сильные стороны)", options: ["strengths", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "strengths", hint: "Positive qualities" },
      { type: 'quiz', question: "'Applicant' means:", options: ["Person applying for a job", "Employer", "Manager", "Colleague", "Другой ответ"], correctAnswer: "Person applying for a job", hint: "Job seeker" }
    ],
    reward: { stars: 3, message: "Ты готов к поиску работы!" }
  },
  {
    title: "Деловое общение",
    subject: "Иностранный язык",
    icon: "Mail",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "A deadline is the final date for a task. (крайний срок)", options: ["deadline", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"],
      keyPoints: [
        "Деловая переписка — Типы деловых писем:",
        "Полезные фразы для деловых писем — Начало письма:",
        "Завершение письма — I look forward to hearing from you",
      ], correctAnswer: "deadline", hint: "Time limit" },
      { type: 'quiz', question: "How to start a business email?", options: ["I am writing to...", "Hey there!", "What's up?", "Hi buddy", "Другой ответ"], correctAnswer: "I am writing to...", hint: "Formal opening" },
      { type: 'quiz', question: "I look forward to hearing from you. (получить ответ)", options: ["hearing", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "hearing", hint: "Waiting for reply" },
      { type: 'quiz', question: "'Negotiation' means:", options: ["Discussion to reach agreement", "Argument", "Contract signing", "Meeting only", "Другой ответ"], correctAnswer: "Discussion to reach agreement", hint: "Reaching a deal" },
      { type: 'quiz', question: "Please find the document attached. (во вложении)", options: ["attached", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "attached", hint: "Included with email" },
      { type: 'quiz', question: "'Proposal' means:", options: ["A formal suggestion", "A complaint", "A meeting", "A contract", "Другой ответ"], correctAnswer: "A formal suggestion", hint: "Business offer" },
      { type: 'quiz', question: "Thank you for your consideration. (рассмотрение)", options: ["consideration", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "consideration", hint: "Reviewing my request" },
      { type: 'quiz', question: "In business, 'meeting' means:", options: ["A gathering for discussion", "A phone call", "An email", "A contract", "Другой ответ"], correctAnswer: "A gathering for discussion", hint: "Business gathering" }
    ],
    reward: { stars: 3, message: "Ты готов к деловому общению!" }
  },
  {
    title: "Экологические проблемы",
    subject: "Иностранный язык",
    icon: "Leaf",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "What causes global warming?", options: ["Greenhouse gases", "Recycling", "Wind energy", "Solar panels", "Другой ответ"],
      keyPoints: [
        "Причины и последствия экологических проблем — Глобальное потепление:",
        "Глобальное потепление — Причины (Causes):",
        "Исчезновение видов — Причины:",
      ], correctAnswer: "Greenhouse gases", hint: "Carbon dioxide, methane" },
      { type: 'quiz', question: "Endangered species are animals at risk of extinction. (исчезающие)", options: ["Endangered", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "Endangered", hint: "In danger" },
      { type: 'quiz', question: "'Deforestation' means:", options: ["Cutting down forests", "Planting trees", "Forest protection", "Forest fire", "Другой ответ"], correctAnswer: "Cutting down forests", hint: "Removing trees" },
      { type: 'quiz', question: "Pollution causes health problems. (проблемы)", options: ["problems", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "problems", hint: "Negative effects" },
      { type: 'quiz', question: "What is 'biodiversity'?", options: ["Variety of life forms", "Type of pollution", "Renewable energy", "Climate change", "Другой ответ"], correctAnswer: "Variety of life forms", hint: "Many different species" },
      { type: 'quiz', question: "Habitat loss is when animals lose their homes. (потеря)", options: ["loss", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "loss", hint: "Destruction of natural homes" },
      { type: 'quiz', question: "'Extinction' means:", options: ["Complete disappearance of a species", "Moving to a new place", "Growing population", "Changing habitat", "Другой ответ"], correctAnswer: "Complete disappearance of a species", hint: "Gone forever" },
      { type: 'quiz', question: "Carbon footprint is the total emissions caused by a person. (след)", options: ["footprint", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "footprint", hint: "Your environmental impact" }
    ],
    reward: { stars: 3, message: "Ты понимаешь экологические проблемы!" }
  },
  {
    title: "Защита окружающей среды",
    subject: "Иностранный язык",
    icon: "Recycle",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "We need to recycle plastic waste. (перерабатывать)", options: ["recycle", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"],
      keyPoints: [
        "Действия для защиты окружающей среды — Индивидуальные действия:",
        "Глобальные инициативы — Paris Agreement (Парижское соглашение)",
        "Ключевое понятие: Защита окружающей среды",
      ], correctAnswer: "recycle", hint: "Process for reuse" },
      { type: 'quiz', question: "What are the 3 R's?", options: ["Reduce, Reuse, Recycle", "Read, Write, Learn", "Run, Walk, Jump", "Red, Green, Blue", "Другой ответ"], correctAnswer: "Reduce, Reuse, Recycle", hint: "Environmental principles" },
      { type: 'quiz', question: "Renewable energy comes from sun and wind. (возобновляемая)", options: ["Renewable", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "Renewable", hint: "Can be replenished" },
      { type: 'quiz', question: "'Eco-friendly' means:", options: ["Good for the environment", "Expensive", "New product", "Popular", "Другой ответ"], correctAnswer: "Good for the environment", hint: "Environmentally safe" },
      { type: 'quiz', question: "We should save water and electricity. (экономить)", options: ["save", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "save", hint: "Use less" },
      { type: 'quiz', question: "What is 'sustainable development'?", options: ["Development that meets present needs without harming future", "Fast economic growth", "Industrial expansion", "Population increase", "Другой ответ"], correctAnswer: "Development that meets present needs without harming future", hint: "Long-term thinking" },
      { type: 'quiz', question: "Solar panels convert sunlight into energy. (энергию)", options: ["energy", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "energy", hint: "Power from the sun" },
      { type: 'quiz', question: "'Conservation' means:", options: ["Protection and preservation", "Destruction", "Pollution", "Consumption", "Другой ответ"], correctAnswer: "Protection and preservation", hint: "Saving natural resources" }
    ],
    reward: { stars: 3, message: "Ты знаешь, как защитить природу!" }
  },
  {
    title: "Типы СМИ",
    subject: "Иностранный язык",
    icon: "Newspaper",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "A newspaper is a daily or weekly publication. (газета)", options: ["newspaper", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"],
      keyPoints: [
        "Критическое отношение к информации — При работе с информацией важно уметь её оценивать:",
        "При работе с информацией важно уметь её оценивать — Check the source (проверяйте источник)",
        "Ключевое понятие: Типы СМИ",
      ], correctAnswer: "newspaper", hint: "Print media" },
      { type: 'quiz', question: "What is a 'headline'?", options: ["Article title", "First paragraph", "Last paragraph", "Picture", "Другой ответ"], correctAnswer: "Article title", hint: "Main title" },
      { type: 'quiz', question: "A journalist writes articles for media. (журналист)", options: ["journalist", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "journalist", hint: "Media professional" },
      { type: 'quiz', question: "'Broadcast' means:", options: ["Transmit on TV/radio", "Print", "Write", "Read", "Другой ответ"], correctAnswer: "Transmit on TV/radio", hint: "Air transmission" },
      { type: 'quiz', question: "The editor edits the articles before publication. (редактирует)", options: ["edits", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "edits", hint: "Makes corrections" },
      { type: 'quiz', question: "What does a 'correspondent' do?", options: ["Reports from a specific location", "Edits articles", "Prints newspapers", "Manages the company", "Другой ответ"], correctAnswer: "Reports from a specific location", hint: "Field reporter" },
      { type: 'quiz', question: "Media coverage is how news events are reported. (освещение)", options: ["coverage", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "coverage", hint: "Reporting of events" },
      { type: 'quiz', question: "A 'magazine' is:", options: ["A periodic publication with articles and photos", "A daily newspaper", "A radio program", "A TV show", "Другой ответ"], correctAnswer: "A periodic publication with articles and photos", hint: "Weekly or monthly" }
    ],
    reward: { stars: 3, message: "Ты разбираешься в типах СМИ!" }
  },
  {
    title: "Социальные сети",
    subject: "Иностранный язык",
    icon: "Share2",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Viral content spreads quickly online. (быстро)", options: ["quickly", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"],
      keyPoints: [
        "Преимущества и недостатки социальных сетей — Advantages (Преимущества):",
        "Ключевое понятие: Социальные сети",
        "Ключевое понятие: Социальные сети",
      ], correctAnswer: "quickly", hint: "Becomes popular" },
      { type: 'quiz', question: "What is 'cyberbullying'?", options: ["Online harassment", "Computer virus", "Video game", "Social platform", "Другой ответ"], correctAnswer: "Online harassment", hint: "Digital bullying" },
      { type: 'quiz', question: "Don't share personal information online. (информация)", options: ["information", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "information", hint: "Private data" },
      { type: 'quiz', question: "A 'follower' is:", options: ["Someone who subscribes to your content", "A friend", "Family member", "Coworker", "Другой ответ"], correctAnswer: "Someone who subscribes to your content", hint: "Social media connection" },
      { type: 'quiz', question: "An influencer has many followers on social media. (инфлюенсер)", options: ["influencer", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "influencer", hint: "Popular content creator" },
      { type: 'quiz', question: "'Fake news' means:", options: ["False information presented as news", "Real news", "Old news", "Sports news", "Другой ответ"], correctAnswer: "False information presented as news", hint: "Misinformation" },
      { type: 'quiz', question: "Privacy settings control who can see your posts. (настройки)", options: ["settings", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "settings", hint: "Security options" },
      { type: 'quiz', question: "What is a 'hashtag'?", options: ["A label with # symbol", "A photo", "A video", "A message", "Другой ответ"], correctAnswer: "A label with # symbol", hint: "Categorizes content" }
    ],
    reward: { stars: 3, message: "Ты безопасно используешь соцсети!" }
  },
  {
    title: "Технологии будущего",
    subject: "Иностранный язык",
    icon: "Cpu",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "AI stands for Artificial Intelligence . (интеллект)", options: ["Intelligence", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"],
      keyPoints: [
        "Искусственный интеллект (AI) — Области применения ИИ:",
        "Ключевое понятие: Технологии будущего",
        "Ключевое понятие: Технологии будущего",
      ], correctAnswer: "Intelligence", hint: "Smart machines" },
      { type: 'quiz', question: "What is 'virtual reality'?", options: ["Computer-generated environment", "Real world", "Dream", "Movie", "Другой ответ"], correctAnswer: "Computer-generated environment", hint: "VR technology" },
      { type: 'quiz', question: "Self-driving cars drive without a driver. (автопилотируемые)", options: ["Self-driving", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "Self-driving", hint: "Or autonomous" },
      { type: 'quiz', question: "'Automation' means:", options: ["Machines doing work automatically", "Manual labor", "Working slowly", "No work", "Другой ответ"], correctAnswer: "Machines doing work automatically", hint: "Automatic processes" },
      { type: 'quiz', question: "Machine learning allows computers to learn from data. (обучение)", options: ["learning", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "learning", hint: "AI technology" },
      { type: 'quiz', question: "What is 'blockchain'?", options: ["A digital ledger technology", "A type of robot", "A video game", "A social network", "Другой ответ"], correctAnswer: "A digital ledger technology", hint: "Secure record system" },
      { type: 'quiz', question: "Smart homes have automated systems for lighting and temperature. (дома)", options: ["homes", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "homes", hint: "Connected living spaces" },
      { type: 'quiz', question: "'Innovation' means:", options: ["A new idea or method", "Old technology", "Traditional way", "Problem", "Другой ответ"], correctAnswer: "A new idea or method", hint: "Creative solution" }
    ],
    reward: { stars: 3, message: "Ты понимаешь технологии будущего!" }
  },
  {
    title: "Цифровая грамотность",
    subject: "Иностранный язык",
    icon: "Shield",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Use strong passwords to protect accounts. (пароли)", options: ["passwords", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"],
      keyPoints: [
        "Правила цифровой безопасности — Онлайн-безопасность:",
        "Цифровой след (Digital Footprint) — Цифровой след — это вся информация о вас в интернете",
        "Цифровой след — это вся информация о вас в интернете. Она включает:",
      ],
      examples: [
        "При проектировании школьного стола: ТЗ должно содержать габариты, материал (древесина), нагрузку до 30 кг, бюджет 2000 ₽, срок выполнения — 2 недели",
        "Метод морфологического анализа: переберите все комбинации материалов (дерево, металл, пластик) и форм (прямоугольная, круглая, угловая) для поиска оптимального решения",
        "После создания прототипа проведите тестирование: проверьте прочность, удобство использования и соответствие техническому заданию",
      ], correctAnswer: "passwords", hint: "Security codes" },
      { type: 'quiz', question: "What is 'phishing'?", options: ["Fake emails to steal data", "Fishing hobby", "Computer game", "Website design", "Другой ответ"], correctAnswer: "Fake emails to steal data", hint: "Online scam" },
      { type: 'quiz', question: "Create a backup of important files. (резервную копию)", options: ["backup", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "backup", hint: "Extra copy" },
      { type: 'quiz', question: "'Encryption' means:", options: ["Coding data for security", "Deleting files", "Opening files", "Sharing files", "Другой ответ"], correctAnswer: "Coding data for security", hint: "Data protection" },
      { type: 'quiz', question: "Malware is software that harms your computer. (вредоносное ПО)", options: ["Malware", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "Malware", hint: "Viruses and trojans" },
      { type: 'quiz', question: "What is 'two-factor authentication'?", options: ["Extra security layer for login", "Two passwords", "Two computers", "Two users", "Другой ответ"], correctAnswer: "Extra security layer for login", hint: "Additional verification" },
      { type: 'quiz', question: "Your digital footprint is all the information about you online. (след)", options: ["footprint", "Неверно", "Другой ответ", "Не подходит", "Нет ответа"], correctAnswer: "footprint", hint: "Online presence" },
      { type: 'quiz', question: "A 'firewall' is:", options: ["Security system for networks", "A type of virus", "A website", "An email", "Другой ответ"], correctAnswer: "Security system for networks", hint: "Network protection" }
    ],
    reward: { stars: 3, message: "Ты цифровой грамотный пользователь!" }
  }
]
