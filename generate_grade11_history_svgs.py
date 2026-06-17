#!/usr/bin/env python3
"""Generate 12 detailed SVG files for Grade 11 History (История) lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade11/history"

# Color scheme
PRIMARY = "#5D4037"
PRIMARY_LIGHT = "#8D6E63"
PRIMARY_DARK = "#3E2723"
BG = "#EFEBE9"
BG_DARK = "#D7CCC8"
ACCENT = "#A1887F"
WHITE = "#FFFFFF"
TEXT_DARK = "#3E2723"
TEXT_MED = "#5D4037"
TEXT_LIGHT = "#8D6E63"

LESSONS = [
    {
        "num": 1,
        "title": "Перестройка (1985-1991)",
        "content": {
            "key_figures": ["М.С. Горбачёв", "А.А. Громыко", "Е.К. Лигачёв", "А.Н. Яковлев"],
            "events": [
                ("1985", "Начало перестройки"),
                ("1987", "Закон о госпредприятии"),
                ("1989", "Съезд народных депутатов"),
                ("1990", "Отмена ст. 6 Конституции"),
                ("1991", "Августовский путч"),
            ],
            "concepts": ["Гласность", "Ускорение", "Перестройка", "Новое мышление", "Плюрализм"],
            "diagram_title": "Этапы перестройки",
            "diagram_items": ["1985-87: Ускорение", "1987-89: Реформы", "1989-91: Кризис"],
        }
    },
    {
        "num": 2,
        "title": "Распад СССР",
        "content": {
            "key_figures": ["М.С. Горбачёв", "Б.Н. Ельцин", "Л.М. Кравчук", "С.С. Шушкевич"],
            "events": [
                ("8 дек 1991", "Беловежское соглашение"),
                ("12 дек 1991", "Денонсация Союзного договора"),
                ("25 дек 1991", "Отставка Горбачёва"),
                ("26 дек 1991", "Упразднение СССР"),
                ("1990-91", "Парад суверенитетов"),
            ],
            "concepts": ["СНГ", "Суверенитет", "Независимость", "Сецессия", "Беловежские соглашения"],
            "diagram_title": "Причины распада",
            "diagram_items": ["Экономический кризис", "Национальные противоречия", "Политическая борьба"],
        }
    },
    {
        "num": 3,
        "title": "Россия в 1990-е годы",
        "content": {
            "key_figures": ["Б.Н. Ельцин", "Е.Т. Гайдар", "А.Б. Чубайс", "В.С. Черномырдин"],
            "events": [
                ("1992", "Либерализация цен"),
                ("1993", "Конституционный кризис"),
                ("1993", "Принятие Конституции"),
                ("1994-96", "Первая чеченская война"),
                ("1998", "Дефолт"),
            ],
            "concepts": ["Шоковая терапия", "Ваучеризация", "Приватизация", "Дефолт", "Имpeчмент"],
            "diagram_title": "Реформы 1990-х",
            "diagram_items": ["Цены → Рынок", "Собственность → Частная", "Политика → Демократия"],
        }
    },
    {
        "num": 4,
        "title": "Россия в 2000-е годы",
        "content": {
            "key_figures": ["В.В. Путин", "Д.А. Медведев", "М.Е. Фрадков", "А.Л. Кудрин"],
            "events": [
                ("2000", "Избрание Путина"),
                ("2003", "Дело «ЮКОСа»"),
                ("2004", "Беслан"),
                ("2005", "Нацпроекты"),
                ("2008", "Война в Юж. Осетии"),
            ],
            "concepts": ["Стабилизационный фонд", "Суверенная демократия", "Нацпроекты", "Вертикаль власти", "Энергетическая сверхдержава"],
            "diagram_title": "Ключевые тренды",
            "diagram_items": ["Экономический рост", "Централизация власти", "Внешнеполит. активность"],
        }
    },
    {
        "num": 5,
        "title": "Россия в 2010-е годы",
        "content": {
            "key_figures": ["Д.А. Медведев", "В.В. Путин", "С.В. Лавров", "Э.С. Набиуллина"],
            "events": [
                ("2012", "Возврат Путина"),
                ("2014", "Присоединение Крыма"),
                ("2015", "Операция в Сирии"),
                ("2018", "Чемпионат мира"),
                ("2020", "Поправки к Конституции"),
            ],
            "concepts": ["Санкции", "Крымский вопрос", "Многополярность", "Цифровизация", "Национальные цели"],
            "diagram_title": "Векторы развития",
            "diagram_items": ["Оборона и безопасность", "Социальная политика", "Технологии и инновации"],
        }
    },
    {
        "num": 6,
        "title": "Конституция РФ",
        "content": {
            "key_figures": ["Б.Н. Ельцин", "В.Д. Зорькин", "С.М. Шахрай", "А.А. Собчак"],
            "events": [
                ("12 дек 1993", "Принятие Конституции"),
                ("2008", "Увеличение срока президентства"),
                ("2020", "Поправки к Конституции"),
                ("1995", "Конституционный Суд"),
                ("1996", "Закон о Конст. Суде"),
            ],
            "concepts": ["Референдум", "Разделение властей", "Права человека", "Федерализм", "Верховенство права"],
            "diagram_title": "Структура Конституции",
            "diagram_items": ["Преамбула + 137 статей", "Глава: Права и свободы", "Глава: Федеративное устройство"],
        }
    },
    {
        "num": 7,
        "title": "Государственные символы России",
        "content": {
            "key_figures": ["Пётр I", "Александр II", "Б.Н. Ельцин", "Е.И. Каменева"],
            "events": [
                ("1497", "Двуглавый орёл Ивана III"),
                ("1700", "Флаг Петра I"),
                ("1883", "Триколор — официальный флаг"),
                ("1993", "Восстановление триколора"),
                ("2000", "Закон о гимне"),
            ],
            "concepts": ["Герб", "Флаг", "Гимн", "Двуглавый орёл", "Андреевский флаг"],
            "diagram_title": "Три символа",
            "diagram_items": ["🏛 Герб: Двуглавый орёл", "🏳 Флаг: Бело-сине-красный", "🎵 Гимн: Россия — священная"],
        }
    },
    {
        "num": 8,
        "title": "Глобализация",
        "content": {
            "key_figures": ["Т. Левитт", "С. Хантингтон", "Ф. Фукуяма", "Дж. Стиглиц"],
            "events": [
                ("1944", "Бреттон-Вудская система"),
                ("1995", "Создание ВТО"),
                ("2001", "Вступление Китая в ВТО"),
                ("2008", "Мировой финансовый кризис"),
                ("2020", "COVID-19 и глобализация"),
            ],
            "concepts": ["Транснациональные корпорации", "Мировой рынок", "Информационное общество", "Культурная глобализация", "Антиглобализм"],
            "diagram_title": "Измерения глобализации",
            "diagram_items": ["Экономическое", "Политическое", "Культурное"],
        }
    },
    {
        "num": 9,
        "title": "Международные отношения",
        "content": {
            "key_figures": ["С.В. Лавров", "К. Анфантино", "А. Меркель", "Б. Обама"],
            "events": [
                ("1991", "Конец биполярного мира"),
                ("1999", "Расширение НАТО"),
                ("2014", "Крымский кризис"),
                ("2015", "Сирийский конфликт"),
                ("2022", "Спецоперация на Украине"),
            ],
            "concepts": ["ООН", "НАТО", "БРИКС", "ШОС", "Многополярный мир"],
            "diagram_title": "Модели мироустройства",
            "diagram_items": ["Однополярный мир", "Биполярный мир", "Многополярный мир"],
        }
    },
    {
        "num": 10,
        "title": "Итоги XX века",
        "content": {
            "key_figures": ["В.И. Ленин", "И.В. Сталин", "М.С. Горбачёв", "Ф.Д. Рузвельт"],
            "events": [
                ("1914-18", "Первая мировая война"),
                ("1939-45", "Вторая мировая война"),
                ("1947-91", "Холодная война"),
                ("1991", "Распад СССР"),
                ("XX век", "Научно-техническая революция"),
            ],
            "concepts": ["Тоталитаризм", "Демократия", "НТР", "Глобализация", "Права человека"],
            "diagram_title": "Уроки XX века",
            "diagram_items": ["Мир важнее войны", "Свобода важнее диктатуры", "Сотрудничество важнее конфронтации"],
        }
    },
    {
        "num": 11,
        "title": "Россия в современном мире",
        "content": {
            "key_figures": ["В.В. Путин", "С.В. Лавров", "Э.С. Набиуллина", "А.Л. Кудрин"],
            "events": [
                ("2014", "Присоединение Крыма"),
                ("2015", "Операция в Сирии"),
                ("2020", "Поправки к Конституции"),
                ("2022", "Спецоперация"),
                ("2023", "БРИКС+ расширение"),
            ],
            "concepts": ["Суверенитет", "Многополярность", "Санкционное давление", "Импортозамещение", "Евразийская интеграция"],
            "diagram_title": "Роль России",
            "diagram_items": ["Ядерная держава", "Энергетический поставщик", "Гарант безопасности"],
        }
    },
    {
        "num": 12,
        "title": "Уроки истории",
        "content": {
            "key_figures": ["В.О. Ключевский", "Н.М. Карамзин", "С.М. Соловьёв", "Л.Н. Гумилёв"],
            "events": [
                ("1917", "Революция и её уроки"),
                ("1941-45", "Война и единство"),
                ("1991", "Распад и суверенитет"),
                ("2000-е", "Стабильность и развитие"),
                ("XXI век", "Вызовы будущего"),
            ],
            "concepts": ["Историческая память", "Патриотизм", "Гражданственность", "Преемственность", "Ценностные ориентиры"],
            "diagram_title": "Ценности",
            "diagram_items": ["Память → Опыт", "Единство → Сила", "Знание → Будущее"],
        }
    },
]


def escape_xml(text):
    """Escape special XML characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def build_header(title, lesson_num):
    """Build the SVG header section with title and lesson number."""
    return f'''
    <!-- Header background -->
    <rect x="10" y="10" width="480" height="52" rx="8" fill="{PRIMARY}" opacity="0.95"/>
    
    <!-- Lesson number badge -->
    <rect x="18" y="16" width="40" height="40" rx="8" fill="{WHITE}" opacity="0.2"/>
    <text x="38" y="43" text-anchor="middle" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="{WHITE}">{lesson_num}</text>
    
    <!-- Title -->
    <text x="68" y="33" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{WHITE}">{escape_xml(title)}</text>
    <text x="68" y="50" font-family="Arial, sans-serif" font-size="10" fill="{WHITE}" opacity="0.85">История — Урок {lesson_num}</text>
    '''


def build_footer():
    """Build the SVG footer."""
    return f'''
    <!-- Footer -->
    <rect x="10" y="326" width="480" height="16" rx="4" fill="{BG_DARK}" opacity="0.7"/>
    <text x="250" y="338" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_LIGHT}">История · 11 класс</text>
    '''


def build_key_figures(figures, y_start):
    """Build a key figures section."""
    elements = f'''
    <!-- Key Figures Section -->
    <rect x="15" y="{y_start}" width="228" height="90" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1"/>
    <rect x="15" y="{y_start}" width="228" height="20" rx="6" fill="{PRIMARY_LIGHT}" opacity="0.3"/>
    <rect x="15" y="{y_start + 14}" width="228" height="6" fill="{WHITE}"/>
    <text x="22" y="{y_start + 15}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY}">Ключевые фигуры</text>
    '''
    for i, fig in enumerate(figures):
        y = y_start + 33 + i * 16
        elements += f'''
        <circle cx="26" cy="{y - 3}" r="3" fill="{PRIMARY_LIGHT}"/>
        <text x="34" y="{y}" font-family="Arial, sans-serif" font-size="9.5" fill="{TEXT_DARK}">{escape_xml(fig)}</text>
        '''
    return elements


def build_events(events, y_start):
    """Build a timeline/events section."""
    elements = f'''
    <!-- Events Timeline Section -->
    <rect x="257" y="{y_start}" width="228" height="90" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1"/>
    <rect x="257" y="{y_start}" width="228" height="20" rx="6" fill="{PRIMARY_LIGHT}" opacity="0.3"/>
    <rect x="257" y="{y_start + 14}" width="228" height="6" fill="{WHITE}"/>
    <text x="264" y="{y_start + 15}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY}">Хронология событий</text>
    '''
    for i, (date, event) in enumerate(events):
        y = y_start + 33 + i * 12
        elements += f'''
        <rect x="264" y="{y - 8}" width="50" height="12" rx="3" fill="{BG_DARK}" opacity="0.6"/>
        <text x="270" y="{y}" font-family="Arial, sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}">{escape_xml(date)}</text>
        <text x="320" y="{y}" font-family="Arial, sans-serif" font-size="8.5" fill="{TEXT_DARK}">{escape_xml(event)}</text>
        '''
    return elements


def build_concepts(concepts, y_start):
    """Build a concepts section with tag-like boxes."""
    elements = f'''
    <!-- Concepts Section -->
    <rect x="15" y="{y_start}" width="228" height="82" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1"/>
    <rect x="15" y="{y_start}" width="228" height="20" rx="6" fill="{PRIMARY_LIGHT}" opacity="0.3"/>
    <rect x="15" y="{y_start + 14}" width="228" height="6" fill="{WHITE}"/>
    <text x="22" y="{y_start + 15}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY}">Ключевые понятия</text>
    '''
    x_pos = 22
    y_pos = y_start + 32
    for i, concept in enumerate(concepts):
        # Approximate width based on character count
        w = len(concept) * 6.5 + 12
        if x_pos + w > 236:
            x_pos = 22
            y_pos += 20
        elements += f'''
        <rect x="{x_pos}" y="{y_pos - 9}" width="{w}" height="16" rx="4" fill="{BG_DARK}" stroke="{PRIMARY_LIGHT}" stroke-width="0.5"/>
        <text x="{x_pos + 6}" y="{y_pos + 2}" font-family="Arial, sans-serif" font-size="8" fill="{PRIMARY}">{escape_xml(concept)}</text>
        '''
        x_pos += w + 4
    return elements


def build_diagram(diagram_title, diagram_items, y_start):
    """Build a diagram/summary section with connecting elements."""
    elements = f'''
    <!-- Diagram Section -->
    <rect x="257" y="{y_start}" width="228" height="82" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1"/>
    <rect x="257" y="{y_start}" width="228" height="20" rx="6" fill="{PRIMARY_LIGHT}" opacity="0.3"/>
    <rect x="257" y="{y_start + 14}" width="228" height="6" fill="{WHITE}"/>
    <text x="264" y="{y_start + 15}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY}">{escape_xml(diagram_title)}</text>
    '''
    for i, item in enumerate(diagram_items):
        y = y_start + 33 + i * 18
        # Arrow-like connector
        elements += f'''
        <rect x="264" y="{y - 8}" width="214" height="14" rx="3" fill="{BG_DARK}" opacity="0.5"/>
        <polygon points="264,{y - 1} 269,{y - 4} 269,{y + 2}" fill="{PRIMARY}"/>
        <text x="275" y="{y + 1}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_DARK}">{escape_xml(item)}</text>
        '''
    return elements


def build_summary_bar(y_start):
    """Build a bottom summary/insight bar."""
    return f'''
    <!-- Summary bar -->
    <rect x="15" y="{y_start}" width="470" height="24" rx="5" fill="{PRIMARY}" opacity="0.08"/>
    <rect x="15" y="{y_start}" width="4" height="24" rx="2" fill="{PRIMARY}"/>
    <text x="28" y="{y_start + 16}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_MED}" font-style="italic">💡 Изучение истории помогает понять настоящее и предвидеть будущее</text>
    '''


def generate_svg(lesson):
    """Generate a complete SVG for a lesson."""
    num = lesson["num"]
    title = lesson["title"]
    c = lesson["content"]

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350" width="500" height="350">
  <defs>
    <filter id="shadow" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="{PRIMARY_DARK}" flood-opacity="0.1"/>
    </filter>
  </defs>
  
  <!-- Background -->
  <rect x="0" y="0" width="500" height="350" rx="12" fill="{BG}"/>
  
  <!-- Border -->
  <rect x="5" y="5" width="490" height="340" rx="10" fill="none" stroke="{PRIMARY}" stroke-width="2.5" opacity="0.7"/>
  
  <!-- Inner border accent -->
  <rect x="8" y="8" width="484" height="334" rx="9" fill="none" stroke="{ACCENT}" stroke-width="0.5" opacity="0.3"/>
  
  {build_header(title, num)}
  
  {build_key_figures(c["key_figures"], 70)}
  
  {build_events(c["events"], 70)}
  
  {build_concepts(c["concepts"], 168)}
  
  {build_diagram(c["diagram_title"], c["diagram_items"], 168)}
  
  {build_summary_bar(258)}
  
  <!-- Decorative timeline line -->
  <line x1="30" y1="295" x2="470" y2="295" stroke="{ACCENT}" stroke-width="1" stroke-dasharray="4,3" opacity="0.4"/>
  
  <!-- Decorative corner elements -->
  <circle cx="15" cy="310" r="2" fill="{PRIMARY_LIGHT}" opacity="0.3"/>
  <circle cx="485" cy="310" r="2" fill="{PRIMARY_LIGHT}" opacity="0.3"/>
  <circle cx="250" cy="295" r="2" fill="{PRIMARY}" opacity="0.3"/>
  
  <!-- Lesson-specific icon area -->
  <rect x="200" y="290" width="100" height="30" rx="5" fill="{WHITE}" stroke="{ACCENT}" stroke-width="0.8" filter="url(#shadow)"/>
  <text x="250" y="309" text-anchor="middle" font-family="Arial, sans-serif" font-size="8" fill="{PRIMARY}" font-weight="bold">УРОК {num} из 12</text>
  
  {build_footer()}
</svg>'''
    return svg


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"Generating 12 SVG files in: {OUTPUT_DIR}\n")

    generated = []
    for lesson in LESSONS:
        num = lesson["num"]
        filename = f"lesson{num}.svg"
        filepath = os.path.join(OUTPUT_DIR, filename)

        svg_content = generate_svg(lesson)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)

        generated.append(filepath)
        print(f"  ✓ Created {filename} — {lesson['title']}")

    print(f"\nAll 12 SVG files generated successfully!")

    # Validate all SVGs
    print("\nValidating SVGs as proper XML...")
    all_valid = True
    for filepath in generated:
        filename = os.path.basename(filepath)
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            # Check basic SVG structure
            ns = "{http://www.w3.org/2000/svg}"
            if root.tag != f"{ns}svg":
                print(f"  ✗ {filename}: Root element is not <svg> (found {root.tag})")
                all_valid = False
            else:
                vb = root.get("viewBox")
                if vb != "0 0 500 350":
                    print(f"  ✗ {filename}: viewBox is '{vb}', expected '0 0 500 350'")
                    all_valid = False
                else:
                    # Count child elements to make sure content is rich
                    children = list(root)
                    if len(children) < 5:
                        print(f"  ✗ {filename}: Too few child elements ({len(children)})")
                        all_valid = False
                    else:
                        print(f"  ✓ {filename}: Valid XML, viewBox correct, {len(children)} root children")
        except ET.ParseError as e:
            print(f"  ✗ {filename}: XML Parse Error — {e}")
            all_valid = False
        except Exception as e:
            print(f"  ✗ {filename}: Error — {e}")
            all_valid = False

    if all_valid:
        print("\n✅ All 12 SVGs are valid XML with correct viewBox!")
    else:
        print("\n❌ Some SVGs have validation issues!")

    # Also check file sizes
    print("\nFile sizes:")
    for filepath in generated:
        size = os.path.getsize(filepath)
        filename = os.path.basename(filepath)
        print(f"  {filename}: {size:,} bytes")


if __name__ == "__main__":
    main()
