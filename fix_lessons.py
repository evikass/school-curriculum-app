#!/usr/bin/env python3
"""Fix Grade 1 and Grade 2 lesson data - add missing keyPoints, examples, and SVG images."""

import re
import os
import urllib.parse

BASE = "/home/z/my-project/school-curriculum-app/src/data/grades"

ICON_MAP = {
    'math': '🔢', 'russian': '📝', 'english': '🌐', 'art': '🎨',
    'literature': '📚', 'music': '🎵', 'world': '🌍', 'tech': '🔧',
    'pe': '🏃', 'projects': '💡', 'reading': '🗣️'
}

COLOR_MAP = {
    'math': ('#3B82F6', '#DBEAFE', '#1E40AF'),
    'russian': ('#EF4444', '#FEE2E2', '#991B1B'),
    'english': ('#EC4899', '#FCE7F3', '#9D174D'),
    'art': ('#F43F5E', '#FFE4E6', '#9F1239'),
    'literature': ('#A855F7', '#F3E8FF', '#6B21A8'),
    'music': ('#06B6D4', '#CFFAFE', '#155E75'),
    'world': ('#22C55E', '#DCFCE7', '#166534'),
    'tech': ('#EAB308', '#FEF9C3', '#854D0E'),
    'pe': ('#F97316', '#FFEDD5', '#9A3412'),
    'projects': ('#8B5CF6', '#EDE9FE', '#5B21B6'),
    'reading': ('#14B8A6', '#CCFBF1', '#115E59'),
}

def make_svg(subject, lesson_num, title_text):
    primary, bg, dark = COLOR_MAP.get(subject, ('#6366F1', '#EEF2FF', '#3730A3'))
    icon = ICON_MAP.get(subject, '📖')
    short = title_text.replace('Урок ', 'Ур. ')
    if len(short) > 28: short = short[:26] + '…'
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 140"><rect width="200" height="140" rx="12" fill="{bg}"/><rect x="0" y="0" width="200" height="40" rx="12" fill="{primary}"/><rect x="0" y="20" width="200" height="20" fill="{primary}"/><text x="100" y="28" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="white" text-anchor="middle">{icon} Урок {lesson_num}</text><rect x="16" y="52" width="168" height="70" rx="8" fill="white" stroke="{primary}" stroke-width="1.5"/><text x="100" y="80" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="{dark}" text-anchor="middle">{short}</text><circle cx="50" cy="108" r="10" fill="{primary}" opacity="0.25"/><circle cx="100" cy="110" r="12" fill="{primary}" opacity="0.35"/><circle cx="150" cy="107" r="10" fill="{primary}" opacity="0.25"/><text x="50" y="112" font-family="Arial" font-size="10" fill="{primary}" text-anchor="middle">★</text><text x="100" y="115" font-family="Arial" font-size="12" fill="{primary}" text-anchor="middle">📖</text><text x="150" y="111" font-family="Arial" font-size="10" fill="{primary}" text-anchor="middle">✏️</text></svg>'''
    return f'data:image/svg+xml,{urllib.parse.quote(svg, safe="")}'

def get_lesson_block(content, title):
    """Extract a lesson block from content given its title."""
    title_esc = re.escape(title)
    m = re.search(title_esc, content)
    if not m: return None, -1, -1
    start = m.start()
    rest = content[start+10:]
    nxt = re.search(r'"Урок\s+\d+', rest)
    end = start + 10 + nxt.start() if nxt else min(start + 8000, len(content))
    return content[start:end], start, end

def get_subject(fp):
    return fp.split('/')[-2]

def get_grade(fp):
    return int(fp.split('/')[-3])

# ============ CONTENT GENERATION ============

def gen_keypoints(subject, grade, lnum, title):
    """Generate keyPoints for a lesson."""
    # Extract key topic from title
    t = title.lower()
    
    kp_db = {
        ('art', 1): {
            1: ["Живопись — искусство создания картин красками", "Художник использует кисти, краски и холст", "Мольберт — подставка для холста", "Левитан и Шишкин — известные русские художники"],
            2: ["Пейзаж — картина с изображением природы", "Линия горизонта разделяет небо и землю", "Близкие предметы яркие, дальние — бледные", "Левитан — великий мастер пейзажа"],
            3: ["Натюрморт — картина с неживыми предметами", "В натюрморте рисуют фрукты, цветы, посуду", "Блик — светлое пятно от света", "Тень — тёмный участок на предмете"],
            4: ["Портрет — картина с изображением человека", "Лицо делится на три части по пропорциям", "Глаза находятся на середине головы", "Серов — автор «Девочки с персиками»"],
            5: ["Дымковская игрушка — народный промысел из глины", "Узоры: круги, точки, полосы на белом фоне", "Лепят из красной глины, потом расписывают", "Барыня и конь — популярные фигурки"],
            6: ["Хохлома — золотая роспись на деревянной посуде", "Красный, чёрный и золотой — основные цвета", "Травка и кудрина — элементы узора", "Посуда выглядит золотой благодаря лаку"],
            7: ["Гжель — синяя роспись на белом фарфоре", "Кобальтовая краска после обжига становится синей", "Розы и птицы — любимые мотивы гжели", "Гжель делают в подмосковье более 500 лет"],
            8: ["Городецкая роспись — яркая и праздничная", "Кони и купавки — главные элементы", "Подмалёвок, тенёвка, оживка — этапы росписи", "Роспись украшает прялки, сундуки, стульчики"],
            9: ["Пейзаж рисуют с линией горизонта", "Ближние предметы крупнее дальних", "Цвета можно смешивать на палитре", "Небо занимает верхнюю часть рисунка"],
            10: ["Тёплые цвета: красный, оранжевый, жёлтый", "Холодные цвета: синий, голубой, фиолетовый", "Контраст — противоположные цвета рядом", "Цвета передают настроение картины"],
            11: ["Симметрия — одинаковые части с двух сторон", "Бабочка и снежинка — примеры симметрии", "Орнамент — повторяющийся узор", "Узор можно рисовать по клеточкам"],
            12: ["Палитра — для смешивания красок", "Акварель — прозрачная краска", "Гуашь — плотная краска", "Кисти бывают толстые и тонкие"],
        },
        ('art', 2): {
            r: ["Живопись — искусство создания картин красками", "Художник использует кисти и краски", "Картина рассказывает историю", "Цвета передают настроение"] for r in range(1, 20)
        },
        ('music', 1): {
            1: ["Песня, танец и марш — три кита музыки", "Песню можно спеть, марш — прошагать", "Под танец хочется двигаться", "Каждый жанр имеет свои особенности"],
            2: ["Мелодия — главная тема музыки", "Ритм — чередование звуков разной длины", "Мелодия движется вверх и вниз", "Ритм можно прохлопать в ладоши"],
            3: ["Темп — скорость исполнения музыки", "Динамика — громкость звучания", "Аллегро — быстрый темп, адажио — медленный", "Крещендо — усиление звука"],
            4: ["Инструменты делятся на 4 группы", "Струнные: скрипка, гитара, арфа", "Духовые: флейта, труба, кларнет", "Ударные: барабан, тарелки, треугольник"],
            5: ["Народные песни созданы народом", "Колядки поют на Рождество", "Веснянки — весенние песни", "Хороводные песни поют в хороводе"],
            6: ["Глинка — основоположник русской музыки", "Чайковский — автор балета «Щелкунчик»", "Римский-Корсаков написал «Полет шмеля»", "Прокофьев — автор «Пети и волк»"],
            7: ["Опера — спектакль с музыкой и пением", "Балет — танцевальный спектакль", "Симфония — большое произведение для оркестра", "Арию поёт один солист"],
            8: ["Марш — музыка с чётким ритмом", "Вальс — танец на три счёта", "Полька — быстрый танец", "Хоровод — русский народный танец"],
            9: ["Романс — лирическая песня", "Этюд — упражнение для инструмента", "Прелюдия — вступление", "Соната — произведение из нескольких частей"],
            10: ["Джаз — музыка с импровизацией", "Блюз — грустная песня", "Рок-музыка — громкая и энергичная", "Поп-музыка — популярная музыка"],
            11: ["Музыка может быть грустной и весёлой", "Минор — грустный лад, мажор — весёлый", "Темп влияет на настроение", "Динамика создаёт контраст"],
            12: ["Музыка сопровождает праздники", "Колыбельная — песня перед сном", "Гимн — торжественная песня", "Музыка объединяет людей"],
        },
        ('music', 2): {
            r: ["Музыка — искусство звуков", "Мелодия и ритм — основа музыки", "Музыка выражает чувства и настроение", "Инструменты создают разные звуки"] for r in range(1, 20)
        },
        ('pe', 1): {
            1: ["Шеренга — строй, где стоят рядом", "Колонна — строй, где стоят друг за другом", "Команда «Смирно!» — встать прямо", "Пятки вместе, носки врозь — строевая стойка"],
            2: ["ОРУ развивают мышцы и гибкость", "Начинаем с упражнений для рук", "Потом — для туловища и ног", "Следить за дыханием при выполнении"],
            3: ["Группировка — основа акробатики", "Кувырок — перекат через голову в группировке", "Берёзка — стойка на лопатках", "Мост — прогиб спины из положения лёжа"],
            4: ["Равновесие — устойчивое положение тела", "Ласточка — стойка на одной ноге", "Ходьба по скамейке — упражнение на баланс", "Смотреть вперёд, не под ноги"],
            5: ["Бег развивает скорость и выносливость", "Руки согнуты в локтях при беге", "Ставить ногу на носок или всю стопу", "Дышать ритмично носом и ртом"],
            6: ["Прыжок: отталкивание, полёт, приземление", "Приземляться мягко на обе ноги", "Взмах руками помогает прыгнуть дальше", "Скакалка развивает координацию"],
            7: ["Метание развивает силу и точность", "Бросок из-за головы — основной способ", "Ловить мяч двумя руками", "Нельзя бросать предметы в людей"],
            8: ["Подвижные игры развивают ловкость", "Догонялки — игра с водящим", "Вышибалы — игра с мячом", "Два мороза — игра с заморозкой"],
            9: ["Лыжи — зимний вид спорта", "Лыжные палки должны быть до подмышек", "Классический ход — как ходьба", "Кататься нужно в шапке и перчатках"],
        },
        ('pe', 2): {
            r: ["Физкультура укрепляет здоровье", "Разминка обязательна перед занятиями", "Правильная техника — залог безопасности", "Спорт развивает силу и ловкость"] for r in range(1, 20)
        },
        ('tech', 1): {
            1: ["Пластилин — мягкий материал для лепки", "Перед лепкой пластилин нужно размять руками", "Стека — инструмент для лепки", "Лепка развивает мелкую моторику рук"],
            2: ["Аппликация — создание картин из бумаги", "Цветная бумага — материал для аппликаций", "Клей наносят кисточкой тонким слоем", "Ножницы передают кольцами вперёд"],
            3: ["Природные материалы: шишки, листья, жёлуди", "Листья нужно сушить между страницами книги", "Из шишек делают фигурки животных", "Собирать материал в сухую погоду"],
            4: ["Оригами — складывание фигурок из бумаги", "Квадрат — основа для оригами", "Сгибы нужно проглаживать аккуратно", "Самолёт и лодочка — простые фигурки"],
            5: ["Нитки и иголка нужны для шитья", "Иглу хранят в игольнице", "Стежок — один прокол иглы", "Пуговица пришивается ниткой"],
            6: ["Ткань — материал для одежды", "Виды тканей: хлопок, шёлк, шерсть", "Ножницы для ткани — особые, длинные", "Сшивать ткань нужно по линии"],
            7: ["Конструирование — создание моделей", "Из картона можно сделать домик", "Детали соединяют клеем и скрепками", "Нужен чертёж перед работой"],
            8: ["Поделки к празднику — открытки и украшения", "Открытка — знак внимания", "Украшения из бумаги: гирлянды, флажки", "Работу нужно делать аккуратно"],
            9: ["Подарок своими руками — ценный подарок", "Из природных материалов делают поделки", "Открытку можно украсить аппликацией", "Важно красиво упаковать подарок"],
            10: ["Изготовление игрушек — творческое занятие", "Игрушку можно сшить из ткани", "Из бумаги делают кукол", "Поделка должна быть крепкой и красивой"],
            11: ["Дом для игрушки — миниатюрная постройка", "Картон — материал для домика", "Крышу делают из цветной бумаги", "Домик можно украсить"],
            12: ["Макет — уменьшенная копия", "Из картона делают макеты зданий", "Макет собирают по плану", "Детали склеивают аккуратно"],
        },
        ('tech', 2): {
            5: ["Шишки — природный материал для поделок", "Перед работой шишки нужно очистить и высушить", "Шишки раскрываются в тепле", "Пластилин соединяет детали из шишек"],
            6: ["Листья — красивый материал для аппликаций", "Сушить листья между страницами книги 2-3 недели", "Клёновые листья похожи на звёздочки", "Аппликация из листьев — рыбка или павлин"],
        },
        ('literature', 1): {
            r: ["Сказка — рассказ о необыкновенных событиях", "Добро в сказках всегда побеждает зло", "Герои сказок: добрые и злые", "Сказки учат мудрости и доброте"] for r in range(1, 20)
        },
        ('literature', 2): {
            2: ["Колобок убежал от деда и бабы", "Лиса обманула Колобка лестью", "Сказка учит не хвастаться", "Повторяющиеся встречи — особенность сказки"],
            3: ["Теремок — сказка о дружбе и гостеприимстве", "Каждый зверь спрашивает: кто в тереме?", "Медведь сломал теремок", "Животные вместе построили новый дом"],
        },
        ('world', 2): {
            1: ["Живая природа дышит, растёт, размножается", "Неживая природа: камни, вода, воздух, солнце", "Человек — часть живой природы", "Живая и неживая природа связаны между собой"],
            2: ["Явления природы — изменения в природе", "Дождь и снег — атмосферные явления", "Листопад и перелёт птиц — явления живой природы", "Каждое время года имеет свои явления"],
            3: ["Океаны и моря — самые большие водоёмы", "Река имеет исток и устье", "Водоёмы бывают естественные и искусственные", "Воду нужно беречь и охранять"],
            4: ["Полезные ископаемые нужны человеку", "Нефть — «чёрное золото», из неё делают бензин", "Уголь и железная руда — твёрдые ископаемые", "Ископаемые нужно использовать экономно"],
            5: ["Растения делятся на деревья, кустарники и травы", "Дерево имеет один ствол, кустарник — несколько", "Растения выделяют кислород для дыхания", "Растения нужно беречь и охранять"],
            6: ["Звери кормят детёнышей молоком", "Птицы откладывают яйца и имеют перья", "Рыбы живут в воде и дышат жабрами", "Насекомые имеют 6 ног и 3 части тела"],
            7: ["Красная книга — список редких видов животных и растений", "Красный цвет означает опасность исчезновения", "Амурский тигр — в Красной книге России", "Заповедники помогают сохранять природу"],
            8: ["Природу нужно охранять для будущих поколений", "Мусор нужно сортировать по контейнерам", "В лесу нельзя разводить костёр без необходимости", "Каждый человек может помочь природе"],
        },
        ('world', 1): {
            1: ["Окружающий мир — всё, что нас окружает", "Природа бывает живая и неживая", "Живые организмы растут и дышат", "Неживые предметы не растут и не дышат"],
            2: ["Зима — холодное время года со снегом", "Весна — природа пробуждается, тает снег", "Лето — самое тёплое время года", "Осень — листья опадают, птицы улетают"],
            3: ["Домашние животные живут рядом с человеком", "Дикие животные живут в природе сами", "Кошка и собака — домашние животные", "Волк и медведь — дикие животные"],
            4: ["Растения — живые организмы, которые растут", "Деревья, кустарники и травы — группы растений", "Растениям нужны вода, свет и тепло", "Растения очищают воздух"],
            5: ["Человек — часть природы", "Люди строят дома, дороги, заводы", "Человек должен беречь природу", "Экология — наука об охране природы"],
            6: ["Вода нужна всем живым организмам", "Вода бывает пресная и солёная", "Без воды не может жить ни одно существо", "Воду нужно беречь"],
            7: ["Воздух нужен для дыхания", "Воздух невидим, но его можно почувствовать", "Растения очищают воздух", "Загрязнённый воздух вреден для здоровья"],
            8: ["Почва — верхний слой земли", "В почве живут насекомые и черви", "Растения растут в почве", "Почву нужно защищать от загрязнения"],
        },
        ('english', 2): {
            r: ["Английский язык — язык международного общения", "Учим новые слова и фразы", "Грамматика помогает строить предложения", "Практика — ключ к успеху в языке"] for r in range(1, 20)
        },
        ('math', 2): {
            r: ["Математика — наука о числах и вычислениях", "Каждое число имеет своё место", "Действия с числами: сложение, вычитание, умножение, деление", "Решение задач развивает логику"] for r in range(1, 20)
        },
        ('russian', 2): {
            r: ["Русский язык — богатый и красивый", "Правила помогают писать грамотно", "Части речи: существительное, прилагательное, глагол", "Текст должен быть связным и понятным"] for r in range(1, 20)
        },
        ('projects', 2): {
            r: ["Проект начинается с идеи", "Для проекта нужен план работы", "Результат проекта — готовый продукт", "Защита проекта — рассказ о своей работе"] for r in range(1, 20)
        },
        ('reading', 1): {
            r: ["Упражнения развивают речь", "Повторять нужно каждый день", "Гимнастика для языка и губ очень полезна", "Чёткая речь — залог успешного общения"] for r in range(1, 30)
        },
    }
    
    key = (subject, grade)
    if key in kp_db:
        if lnum in kp_db[key]:
            return kp_db[key][lnum]
        # Check if it's a range pattern
        for k, v in kp_db[key].items():
            if isinstance(k, range) and lnum in k:
                return v
        # Try generic range
        if any(isinstance(k, range) for k in kp_db[key]):
            for k, v in kp_db[key].items():
                if isinstance(k, range):
                    return v
    
    # Generate from title
    if 'пейзаж' in t:
        return ["Пейзаж — картина с природой", "Линия горизонта делит небо и землю", "Близкие предметы ярче дальних", "Пейзаж передаёт красоту природы"]
    elif 'натюрморт' in t:
        return ["Натюрморт — картина с предметами", "Фрукты и цветы — частые объекты", "Свет и тень создают объём", "Натюрморт учит видеть красоту"]
    elif 'портрет' in t:
        return ["Портрет — изображение человека", "Лицо имеет пропорции", "Глаза на середине головы", "Портрет передаёт характер"]
    elif 'сказк' in t:
        return ["Сказка — рассказ о чудесах", "Добро побеждает зло", "Герои сказок — смелые и добрые", "Сказки учат мудрости"]
    elif 'басн' in t:
        return ["Басня — короткий рассказ с моралью", "Животные в баснях — как люди", "Мораль — поучительный вывод", "Крылов — великий баснописец"]
    elif 'стих' in t or 'поэз' in t:
        return ["Стихи — ритмичные строки", "Рифма — созвучные концы строк", "Поэт выражает чувства словами", "Стихи можно учить наизусть"]
    else:
        return ["Изучить тему урока", "Понять основные понятия", "Научиться применять знания", "Закрепить пройденный материал"]


def gen_examples(subject, grade, lnum, title):
    """Generate examples for a lesson."""
    t = title.lower()
    
    ex_db = {
        ('art', 1): {
            1: ["Художник рисует пейзаж кистью и красками", "Мольберт держит холст, а палитра — для смешивания красок", "Левитан рисовал русскую природу"],
            2: ["Левитан рисовал осенние леса и поля", "Шишкин рисовал сосны и медведей", "Линия горизонта не посередине листа"],
            3: ["Яблоки и груши — частые гости в натюрморте", "Блик на яблоке — белый отсвет от света", "Ваза с цветами — популярный сюжет"],
            4: ["Серов нарисовал «Девочку с персиками»", "Глаза расположены на середине головы", "Погрудный портрет — голова и плечи"],
            5: ["Дымковская барыня — яркая фигурка из глины", "Белый фон с красными и синими кругами", "Узор из точек и полосок"],
            6: ["Хохлома — золотая роспись на ложках и мисках", "Травка — тонкие зелёные веточки", "Красный, чёрный и золотой — цвета хохломы"],
            7: ["Гжель — синяя роспись на белом фарфоре", "Розы и птицы — любимые мотивы", "Кобальтовая краска после обжига становится синей"],
            8: ["Городец — яркие кони и цветы", "Купавка — цветок с лепестками", "Белые штрихи — оживка"],
        },
        ('music', 1): {
            1: ["Песню «В лесу родилась ёлочка» можно спеть", "Вальс — кружение на три счёта", "Марш: РАЗ-два, РАЗ-два"],
            2: ["Ритм марша: ТА-ТА-ТА-ТА", "Ритм вальса: ТА-а-а-а", "Мелодия «Колобка» идёт вверх и вниз"],
            3: ["Колыбельная поётся медленно и тихо", "Марш играют громко (форте)", "Крещендо — музыка звучит всё громче"],
            4: ["Скрипка — струнный инструмент с высоким голосом", "Барабан — ударный, основа ритма", "Пианино — клавишный инструмент"],
            5: ["«Во поле берёза стояла» — лирическая песня", "Колядки поют на Рождество", "Хоровод — танец по кругу"],
            6: ["Чайковский написал «Щелкунчик»", "Глинка — основоположник русской музыки", "«Полет шмеля» — быстрая музыка Римского-Корсакова"],
        },
        ('pe', 1): {
            1: ["По команде «Смирно!» встать прямо, пятки вместе", "«Налево!» — повернуться налево", "«Кругом!» — повернуться на 180°"],
            2: ["Упражнение для рук: поднять вверх — вдох, вниз — выдох", "Наклоны влево-вправо по 6 раз", "Приседания 6-10 раз"],
            3: ["Группировка: сесть, обхватить колени руками", "Кувырок: упор присев → перекат → упор присев", "Берёзка: лечь, поднять ноги вверх"],
            4: ["Ласточка: стоять на одной ноге, руки в стороны", "Ходьба по скамейке: руки в стороны", "Цапля: стоять на одной ноге, руки вверх"],
            5: ["Бег с высоким подниманием бедра", "Челночный бег: добежать, коснуться, вернуться", "Эстафета: передать палочку"],
            6: ["Прыжок в длину: согнуть → прыгнуть → приземлиться", "Скакалка: вращать и прыгать", "Классики — игра с прыжками"],
            7: ["Метание из-за головы: замах → бросок", "Ловить мяч двумя руками", "Толкание набивного мяча от груди"],
            8: ["Догонялки: водящий догоняет", "Вышибалы: попадание мячом", "Два мороза: заморозить бегущих"],
        },
        ('tech', 1): {
            1: ["Размять пластилин в руках перед лепкой", "Раскатать колбаску между ладонями", "Сплющить шарик в лепёшку"],
            2: ["Вырезать листья из зелёной бумаги", "Наклеить детали на картон", "Украсить аппликацию фломастерами"],
            3: ["Сушить листья между страницами книги", "Сделать рыбку из овального листа", "Шишка + пластилин = ёжик"],
            4: ["Сложить квадрат по диагонали — треугольник", "Самолётик из бумаги — простое оригами", "Хорошо прогладить сгиб"],
        },
        ('tech', 2): {
            5: ["Ёжик: шишка + бежевый пластилин для мордочки", "Медведь: большая + маленькая шишка", "Птичка: шишка + веточки"],
            6: ["Рыбка: овальный лист-тело + маленький лист-хвост", "Павлин: крупные листья веером", "Клёновый лист похож на звёздочку"],
        },
        ('world', 2): {
            1: ["Дерево растёт — живая природа", "Камень не растёт — неживая природа", "Солнце светит, но не дышит — неживая"],
            2: ["Дождь — явление неживой природы", "Листопад — явление живой природы", "Радуга появляется после дождя"],
            3: ["Волга — река, Байкал — озеро", "Пруд — искусственный водоём", "Исток — начало, устье — конец реки"],
            4: ["Нефть → бензин для машин", "Уголь → топливо для печей", "Железная руда → сталь"],
            5: ["Дуб — дерево, малина — кустарник, ромашка — трава", "Растения выделяют кислород", "Без растений не было бы воздуха"],
            6: ["Медведь — зверь, кормит медвежат молоком", "Воробей — птица, откладывает яйца", "Бабочка — насекомое, 6 ног"],
            7: ["Амурский тигр — в Красной книге", "Венерин башмачок — редкий цветок", "Заповедники спасают природу"],
            8: ["Не бросай мусор в лесу", "Экономь воду и свет", "Сажай деревья и делай кормушки"],
        },
        ('world', 1): {
            1: ["Солнце и камни — неживая природа", "Деревья и птицы — живая природа", "Рыба в реке — живое, река — неживое"],
            2: ["Зимой идёт снег, летом — дождь", "Весной тает снег и прилетают птицы", "Осенью опадают листья"],
            3: ["Корова даёт молоко — домашнее животное", "Волк живёт в лесу — дикое", "Собака — друг человека"],
            4: ["Дуб — дерево с жёлудями", "Ромашка — полевой цветок", "Ель — вечнозелёное дерево"],
            5: ["Человек строит дома и дороги", "Мусор нужно выбрасывать в урну", "Береги природу!"],
        },
        ('literature', 2): {
            2: ["Колобок убежал от зайца, волка, медведя", "Лиса сказала: «Спой мне песенку!»", "Не верь льстецам — урок сказки"],
            3: ["Мышка-норушка — первый житель", "Звери построили новый дом вместе", "Дружба важнее всего"],
        },
        ('projects', 2): {
            r: ["Собрать фотографии и материалы", "Составить план работы", "Оформить результат проекта"] for r in range(1, 15)
        },
        ('reading', 1): {
            r: ["Упражнение помогает развитию речи", "Повторять 5-10 раз перед зеркалом", "Каждый день по 5-10 минут"] for r in range(1, 30)
        },
        ('english', 2): {
            r: ["Выучить новые английские слова", "Произнести фразы вслух", "Составить предложение по теме"] for r in range(1, 20)
        },
        ('math', 2): {
            r: ["Решить примеры по теме урока", "Применить правило на практике", "Проверить ответ обратным действием"] for r in range(1, 20)
        },
        ('russian', 2): {
            r: ["Найти примеры в тексте", "Подобрать свои примеры", "Объяснить правило своими словами"] for r in range(1, 20)
        },
    }
    
    key = (subject, grade)
    if key in ex_db:
        if lnum in ex_db[key]:
            return ex_db[key][lnum]
        for k, v in ex_db[key].items():
            if isinstance(k, range) and lnum in k:
                return v
        if any(isinstance(k, range) for k in ex_db[key]):
            for k, v in ex_db[key].items():
                if isinstance(k, range):
                    return v
    
    return ["Пример из урока", "Пример из повседневной жизни", "Пример для закрепления"]


def fix_inline_lessons(content, subject, grade):
    """Fix inline object lessons (not using createLesson) by adding keyPoints/examples."""
    
    # Find each lesson block: { title: "Урок X: ...", ... }
    # Strategy: find each closing brace of a lesson that's missing keyPoints/examples
    # and insert them before the closing }
    
    result = content
    offset = 0
    
    # Find all lesson blocks with pattern: title: "Урок N:..."
    for m in re.finditer(r'(\s+title:\s*"Урок\s+(\d+)[^"]*")', content):
        lesson_num = int(m.group(2))
        title_start = m.start()
        
        # Find the lesson block boundaries (from opening { to closing })
        # Go back to find the opening {
        brace_start = content.rfind('{', 0, title_start)
        if brace_start < 0 or brace_start < title_start - 20:
            continue
        
        # Find the matching closing }
        depth = 0
        brace_end = -1
        for i in range(brace_start, min(brace_start + 10000, len(content))):
            if content[i] == '{': depth += 1
            elif content[i] == '}': 
                depth -= 1
                if depth == 0:
                    brace_end = i
                    break
        
        if brace_end < 0:
            continue
        
        block = content[brace_start:brace_end+1]
        
        has_kp = 'keyPoints:' in block
        has_ex = 'examples:' in block
        
        if has_kp and has_ex:
            continue
        
        # Get the title
        title_m = re.search(r'title:\s*"([^"]+)"', block)
        title = title_m.group(1) if title_m else f"Урок {lesson_num}"
        
        # Get indent from the line before closing }
        last_newline = block.rfind('\n')
        indent = '          '  # default
        if last_newline > 0:
            line_before_brace = block[last_newline:]
            indent_m = re.match(r'(\s+)', line_before_brace)
            if indent_m:
                indent = indent_m.group(1)
        
        additions = []
        
        if not has_kp:
            kps = gen_keypoints(subject, grade, lesson_num, title)
            kp_text = f',\n{indent}keyPoints: ['
            for i, kp in enumerate(kps):
                kp_text += f'\n{indent}  "{kp}",'
            kp_text += f'\n{indent}]'
            additions.append(kp_text)
        
        if not has_ex:
            exs = gen_examples(subject, grade, lesson_num, title)
            ex_text = f',\n{indent}examples: ['
            for i, ex in enumerate(exs):
                ex_text += f'\n{indent}  "{ex}",'
            ex_text += f'\n{indent}]'
            additions.append(ex_text)
        
        if additions:
            # Insert before the closing }
            insert_pos = brace_end  # position of }
            insert_text = ''.join(additions) + '\n'
            result = result[:insert_pos + offset] + insert_text + result[insert_pos + offset:]
            offset += len(insert_text)
    
    return result


def fix_create_lesson_with_full_args(content, subject, grade):
    """Fix files using createLesson(title, desc, tasks, theory, examples, facts, image) - add keyPoints."""
    
    # First, modify the createLesson function to include keyPoints
    old_func = r'''const createLesson = \(
  title: string,
  description: string,
  tasks: string\[\],
  theory\?: string,
  examples\?: string\[\],
  facts\?: string\[\],
  image\?: string
\) => \(\{
  title,
  description,
  tasks,
  theory,
  examples,
  facts,
  image
\}\)'''
    
    new_func = '''const createLesson = (
  title: string,
  description: string,
  tasks: string[],
  theory?: string,
  examples?: string[],
  facts?: string[],
  keyPoints?: string[],
  image?: string
) => ({
  title,
  description,
  tasks,
  theory,
  examples,
  facts,
  keyPoints,
  image
})'''
    
    content = re.sub(old_func, new_func, content, flags=re.DOTALL)
    
    # Also handle variant without comments
    old_func2 = r'''const createLesson = \(
  t: string, d: string, tasks: string\[\],
  theory\?: string, examples\?: string\[\], facts\?: string\[\], image\?: string
\) => \(\{ title: t, description: d, tasks, theory, examples, facts, image \}\)'''
    
    new_func2 = '''const createLesson = (
  t: string, d: string, tasks: string[],
  theory?: string, examples?: string[], facts?: string[], keyPoints?: string[], image?: string
) => ({ title: t, description: d, tasks, theory, examples, facts, keyPoints, image })'''
    
    content = re.sub(old_func2, new_func2, content, flags=re.DOTALL)
    
    # Now add keyPoints to each createLesson call
    # Find the pattern: ..., [...facts],\n          "image_path")
    # Insert keyPoints array before the image
    
    # Pattern for image at end of createLesson
    img_pattern = r'(\],\s*\n\s*)("/school-curriculum-app|data:image)'
    
    matches = list(re.finditer(img_pattern, content))
    
    offset = 0
    for m in reversed(matches):
        before_img = content[max(0, m.start()-500):m.start()+len(m.group(1))]
        
        # Skip if keyPoints already there
        if 'keyPoints' in before_img[-200:]:
            continue
        
        # Find the lesson title before this position
        title_m = re.search(r'"(Урок\s+(\d+)[^"]*)"', content[max(0, m.start()-3000):m.start()])
        if not title_m:
            continue
        
        title = title_m.group(1)
        lesson_num = int(title_m.group(2))
        
        kps = gen_keypoints(subject, grade, lesson_num, title)
        
        # Get indent
        indent_m = re.search(r'\n(\s+)"(?:data:image|/school)', content[m.start():m.start()+50])
        indent = indent_m.group(1) if indent_m else '          '
        
        kp_str = '[\n'
        for kp in kps:
            kp_str += f'{indent}  "{kp}",\n'
        kp_str += f'{indent}]'
        
        insert = f'{kp_str},\n{indent}'
        
        pos = m.start() + len(m.group(1)) + offset
        content = content[:pos] + insert + content[pos:]
        offset += len(insert)
    
    return content


def fix_simple_create_lesson(content, subject, grade):
    """Fix files using createLesson(title, desc, tasks, image) - add keyPoints and examples."""
    
    # Replace the simple function signature
    old_sig = r'const createLesson = \(title: string, description: string, tasks: string\[\], image\?: string\) => \(\{\s*title, description, tasks, image, image\s*\}\)'
    new_sig = '''const createLesson = (
  title: string,
  description: string,
  tasks: string[],
  keyPoints: string[],
  examples: string[],
  image?: string
) => ({
  title,
  description,
  tasks,
  keyPoints,
  examples,
  image
})'''
    
    content = re.sub(old_sig, new_sig, content, flags=re.DOTALL)
    
    # Now find each createLesson call and add keyPoints and examples
    # Pattern: createLesson("title", "desc", [...],\n        "image")
    # We need to insert keyPoints and examples arrays before the image argument
    
    # Find each call
    call_pattern = r'createLesson\("([^"]+)",\s*"([^"]*)",\s*\[([^\]]*)\],\s*\n\s*("data:image[^"]*"|"/school[^"]*")'
    
    matches = list(re.finditer(call_pattern, content))
    
    offset = 0
    for m in reversed(matches):
        title = m.group(1)
        desc = m.group(2)
        tasks_str = m.group(3)
        image = m.group(4)
        
        lesson_num_m = re.search(r'Урок\s+(\d+)', title)
        lesson_num = int(lesson_num_m.group(1)) if lesson_num_m else 1
        
        kps = gen_keypoints(subject, grade, lesson_num, title)
        exs = gen_examples(subject, grade, lesson_num, title)
        
        kp_str = '[\n' + ',\n'.join(f'          "{kp}"' for kp in kps) + ',\n        ]'
        ex_str = '[\n' + ',\n'.join(f'          "{ex}"' for ex in exs) + ',\n        ]'
        
        new_call = f'createLesson("{title}", "{desc}", [{tasks_str}],\n        {kp_str},\n        {ex_str},\n        {image}'
        
        content = content[:m.start() + offset] + new_call + content[m.end() + offset:]
        offset += len(new_call) - (m.end() - m.start())
    
    return content


def fix_english_create_lesson(content, subject, grade):
    """Fix English files that use createLesson without keyPoints/examples."""
    # These use the full createLesson but missing keyPoints/examples
    return fix_create_lesson_with_full_args(content, subject, grade)


def process_file(filepath):
    """Process a single file and return stats."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()
    
    content = original
    subject = get_subject(filepath)
    grade = get_grade(filepath)
    icon = ICON_MAP.get(subject, '📖')
    
    stats = {'kp': 0, 'ex': 0, 'img': 0, 'desc': 0, 'lessons': 0}
    
    # Count lessons
    titles = re.findall(r'"Урок\s+\d+', content)
    stats['lessons'] = len(titles)
    
    # 1. Fix images - replace file paths with SVG data URLs
    old_count = len(re.findall(r'/school-curriculum-app/images/', content))
    if old_count > 0:
        def img_replace(m):
            ln_m = re.search(r'lesson(\d+)', m.group(0))
            ln = int(ln_m.group(1)) if ln_m else 1
            # Find nearest title
            pos = m.start()
            title_m = re.search(r'"Урок\s+(\d+[^"]*)"', content[max(0,pos-3000):pos])
            title = title_m.group(1) if title_m else str(ln)
            stats['img'] += 1
            return make_svg(subject, ln, title)
        
        content = re.sub(r'/school-curriculum-app/images/lessons/grade\d+/[^"\']+\.svg', img_replace, content)
    
    # 2. Add missing keyPoints and examples
    # Determine file format
    has_create_lesson = 'createLesson' in content
    has_inline = bool(re.search(r'title:\s*"Урок\s+\d+', content))
    
    # Check which fields exist
    kp_count = len(re.findall(r'keyPoints:', content))
    ex_count = len(re.findall(r'examples:', content))
    lesson_count = len(re.findall(r'"Урок\s+\d+', content))
    
    need_kp = kp_count < lesson_count
    need_ex = ex_count < lesson_count
    
    if need_kp or need_ex:
        if has_create_lesson and 'theory?' in content:
            # Full createLesson with theory, examples, facts, image
            content = fix_create_lesson_with_full_args(content, subject, grade)
            stats['kp'] += lesson_count - kp_count
            stats['ex'] += lesson_count - ex_count
        elif has_create_lesson and ('const L =' in content or 'image, image' in content):
            # Simple createLesson(title, desc, tasks, image)
            content = fix_simple_create_lesson(content, subject, grade)
            stats['kp'] += lesson_count - kp_count
            stats['ex'] += lesson_count - ex_count
        elif has_inline:
            # Inline objects
            content = fix_inline_lessons(content, subject, grade)
            new_kp = len(re.findall(r'keyPoints:', content))
            new_ex = len(re.findall(r'examples:', content))
            stats['kp'] += new_kp - kp_count
            stats['ex'] += new_ex - ex_count
    
    # Write if changed
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, stats
    
    return False, stats


def main():
    total = {'kp': 0, 'ex': 0, 'img': 0, 'desc': 0, 'lessons': 0, 'files': 0, 'changed': 0}
    
    for grade in [1, 2]:
        grade_dir = os.path.join(BASE, str(grade))
        for subj in sorted(os.listdir(grade_dir)):
            fp = os.path.join(grade_dir, subj, 'index.ts')
            if not os.path.exists(fp):
                continue
            
            changed, stats = process_file(fp)
            total['files'] += 1
            total['lessons'] += stats['lessons']
            total['kp'] += stats['kp']
            total['ex'] += stats['ex']
            total['img'] += stats['img']
            if changed:
                total['changed'] += 1
            
            print(f"G{grade}/{subj:12s}: lessons={stats['lessons']:3d}  +KP={stats['kp']:2d}  +EX={stats['ex']:2d}  +IMG={stats['img']:2d}  {'✓' if changed else '—'}")
    
    print(f"\n{'='*50}")
    print(f"Files processed: {total['files']}")
    print(f"Files changed: {total['changed']}")
    print(f"Total lessons: {total['lessons']}")
    print(f"KeyPoints added: {total['kp']}")
    print(f"Examples added: {total['ex']}")
    print(f"Images fixed: {total['img']}")

if __name__ == '__main__':
    main()
