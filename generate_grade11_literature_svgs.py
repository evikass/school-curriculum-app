#!/usr/bin/env python3
"""Generate 12 detailed SVG files for Grade 11 Literature (Литература) lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade11/literature"

# Color scheme
PRIMARY = "#E65100"
PRIMARY_LIGHT = "#FF8F00"
PRIMARY_DARK = "#BF360C"
BG = "#FFF3E0"
BG_ACCENT = "#FFE0B2"
TEXT_DARK = "#3E2723"
TEXT_MED = "#5D4037"
TEXT_LIGHT = "#8D6E63"
WHITE = "#FFFFFF"
BORDER = "#E65100"

lessons = [
    {
        "num": 1,
        "title": "И.А. Бунин",
        "years": "1870–1953",
        "subtitle": "Литература — Урок 1",
        "portrait_initial": "Б",
        "works": [
            "«Тёмные аллеи»",
            "«Чистый понедельник»",
            "«Антоновские яблоки»",
            "«Господин из Сан-Франциско»",
        ],
        "themes": [
            "Любовь и судьба",
            "Память и время",
            "Утрата дворянства",
            "Жизнь и смерть",
        ],
        "significance": "Первый русский Нобелевский лауреат по литературе (1933). Мастер лирической прозы, продолжатель традиций классической русской литературы в эмиграции.",
    },
    {
        "num": 2,
        "title": "А.И. Куприн",
        "years": "1870–1938",
        "subtitle": "Литература — Урок 2",
        "portrait_initial": "К",
        "works": [
            "«Гранатовый браслет»",
            "«Олеся»",
            "«Поединок»",
            "«Гамбринус»",
        ],
        "themes": [
            "Настоящая любовь",
            "Честь и долг",
            "Армейская жизнь",
            "Талант и общество",
        ],
        "significance": "Выдающийся мастер короткого рассказа и повести. Создатель непревзойдённых образов искреннего чувства и социальной несправедливости в русской прозе.",
    },
    {
        "num": 3,
        "title": "М. Горький",
        "years": "1868–1936",
        "subtitle": "Литература — Урок 3",
        "portrait_initial": "Г",
        "works": [
            "«На дне»",
            "«Старуха Изергиль»",
            "«Челкаш»",
            "«Мать»",
        ],
        "themes": [
            "Правда и утешение",
            "Свобода и ответственность",
            "Босячество",
            "Революция и личность",
        ],
        "significance": "Основоположник социалистического реализма. Создатель образа «человека, звучащего гордо». Философская драма «На дне» — вершина русской драматургии XX века.",
    },
    {
        "num": 4,
        "title": "М.А. Булгаков",
        "years": "1891–1940",
        "subtitle": "Литература — Урок 4",
        "portrait_initial": "Б",
        "works": [
            "«Мастер и Маргарита»",
            "«Собачье сердце»",
            "«Белая гвардия»",
            "«Роковые яйца»",
        ],
        "themes": [
            "Добро и зло",
            "Творчество и цензура",
            "Москвоведение",
            "Сатира и гротеск",
        ],
        "significance": "Автор великого романа XX века. Сочетание реализма, мистики и сатиры. Своеобразный хронотоп, полифония и философская глубина.",
    },
    {
        "num": 5,
        "title": "М.А. Шолохов",
        "years": "1905–1984",
        "subtitle": "Литература — Урок 5",
        "portrait_initial": "Ш",
        "works": [
            "«Тихий Дон»",
            "«Судьба человека»",
            "«Поднятая целина»",
            "«Донские рассказы»",
        ],
        "themes": [
            "Казачество и революция",
            "Трагедия выбора",
            "Человек и война",
            "Родина и дом",
        ],
        "significance": "Нобелевский лауреат (1965). Эпопея «Тихий Дон» — монументальное полотно судьбы донского казачества. Мастер психологического реализма и народной речи.",
    },
    {
        "num": 6,
        "title": "А.Т. Твардовский",
        "years": "1910–1971",
        "subtitle": "Литература — Урок 6",
        "portrait_initial": "Т",
        "works": [
            "«Василий Тёркин»",
            "«По праву памяти»",
            "«За далью — даль»",
            "«Страна Муравия»",
        ],
        "themes": [
            "Война и человек",
            "Память и правда",
            "Народный характер",
            "Коллективизация",
        ],
        "significance": "Создатель бессмертного образа Василия Тёркина. Поэт-фронтовик, чьё творчество стало голосом народной совести. Главный редактор «Нового мира».",
    },
    {
        "num": 7,
        "title": "Б.Л. Васильев",
        "years": "1924–2013",
        "subtitle": "Литература — Урок 7",
        "portrait_initial": "В",
        "works": [
            "«А зори здесь тихие…»",
            "«В списках не значился»",
            "«Завтра была война»",
            "«Ветеран»",
        ],
        "themes": [
            "Женщина на войне",
            "Подвиг и предательство",
            "Юность и война",
            "Память поколений",
        ],
        "significance": "Мастер военной прозы. Его произведения о Великой Отечественной войне проникнуты глубоким гуманизмом и болью за неоправданные потери.",
    },
    {
        "num": 8,
        "title": "В. Быков",
        "years": "1924–2003",
        "subtitle": "Литература — Урок 8",
        "portrait_initial": "Б",
        "works": [
            "«Сотников»",
            "«Обелиск»",
            "«Знак беды»",
            "«Дожить до рассвета»",
        ],
        "themes": [
            "Нравственный выбор",
            "Подвиг и предательство",
            "Партизанская война",
            "Цена жизни",
        ],
        "significance": "Классик белорусской и советской литературы. Мастер психологической повести о войне. Исследователь нравственных пределов человека в экстремальных условиях.",
    },
    {
        "num": 9,
        "title": "А.И. Солженицын",
        "years": "1918–2008",
        "subtitle": "Литература — Урок 9",
        "portrait_initial": "С",
        "works": [
            "«Один день Ивана Денисовича»",
            "«Матрёнин двор»",
            "«Архипелаг ГУЛАГ»",
            "«В круге первом»",
        ],
        "themes": [
            "Гулаг и репрессии",
            "Праведничество",
            "Нравственное сопротивление",
            "Русская деревня",
        ],
        "significance": "Нобелевский лауреат (1970). Писатель-совесть нации. Его произведения открыли миру правду о советских репрессиях и стали нравственным ориентиром.",
    },
    {
        "num": 10,
        "title": "В.Г. Распутин",
        "years": "1937–2015",
        "subtitle": "Литература — Урок 10",
        "portrait_initial": "Р",
        "works": [
            "«Прощание с Матёрой»",
            "«Живи и помни»",
            "«Последний срок»",
            "«Уроки французского»",
        ],
        "themes": [
            "Утрата корней",
            "Нравственная деградация",
            "Память и совесть",
            "Человек и природа",
        ],
        "significance": "Классик «деревенской прозы». Хранитель нравственных традиций русской литературы. Глубокий исследователь народной жизни и духовных ценностей.",
    },
    {
        "num": 11,
        "title": "Теория литературы",
        "years": "",
        "subtitle": "Литература — Урок 11",
        "portrait_initial": "",
        "is_theory": True,
        "concepts": [
            ("Род литературы", "Эпос, лирика, драма"),
            ("Жанр", "Роман, повесть, рассказ, поэма"),
            ("Хронотоп", "Единство времени и пространства"),
            ("Тропы", "Метафора, эпитет, гипербола"),
            ("Композиция", "Экспозиция, завязка, кульминация"),
            ("Стиль", "Реализм, модернизм, постмодернизм"),
        ],
        "significance": "Систематизация литературоведческих понятий. Анализ художественного текста через систему теоретических категорий.",
    },
    {
        "num": 12,
        "title": "Итоговое повторение",
        "years": "",
        "subtitle": "Литература — Урок 12",
        "portrait_initial": "",
        "is_review": True,
        "review_sections": [
            ("Русская классика XX в.", "Бунин, Куприн, Горький"),
            ("Советская литература", "Шолохов, Твардовский"),
            ("Военная проза", "Васильев, Быков"),
            ("Деревенская проза", "Распутин, Солженицын"),
            ("Литература и общество", "Булгаков, Солженицын"),
            ("Теория литературы", "Роды, жанры, тропы"),
        ],
        "significance": "Обобщение и систематизация знаний по курсу литературы 11 класса. Подготовка к итоговой аттестации.",
    },
]


def escape_xml(text):
    """Escape text for XML attributes and content."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def build_author_lesson(l):
    """Build SVG for an author-focused lesson (1-10)."""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <linearGradient id="headerGrad{l['num']}" x1="0" y1="0" x2="500" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="{PRIMARY_DARK}"/>
      <stop offset="100%" stop-color="{PRIMARY}"/>
    </linearGradient>
    <linearGradient id="portraitGrad{l['num']}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{PRIMARY_LIGHT}"/>
      <stop offset="100%" stop-color="{PRIMARY}"/>
    </linearGradient>
    <filter id="shadow{l['num']}" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#00000020"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="500" height="350" rx="12" fill="{BG}" stroke="{BORDER}" stroke-width="2.5"/>

  <!-- Header bar -->
  <rect x="0" y="0" width="500" height="56" rx="12" fill="url(#headerGrad{l['num']})"/>
  <rect x="0" y="20" width="500" height="36" fill="url(#headerGrad{l['num']})"/>

  <!-- Lesson number badge -->
  <circle cx="28" cy="28" r="16" fill="{WHITE}" opacity="0.25"/>
  <text x="28" y="33" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{WHITE}">{l['num']}</text>

  <!-- Title -->
  <text x="52" y="24" font-family="Arial, sans-serif" font-size="15" font-weight="bold" fill="{WHITE}">{escape_xml(l['title'])}</text>
  <text x="52" y="42" font-family="Arial, sans-serif" font-size="10" fill="{BG}" opacity="0.85">{escape_xml(l['subtitle'])}  ·  {escape_xml(l['years'])}</text>

  <!-- Portrait circle -->
  <circle cx="55" cy="100" r="30" fill="url(#portraitGrad{l['num']})" filter="url(#shadow{l['num']})"/>
  <circle cx="55" cy="100" r="28" fill="{PRIMARY}" stroke="{WHITE}" stroke-width="2"/>
  <text x="55" y="108" text-anchor="middle" font-family="Georgia, serif" font-size="26" font-weight="bold" fill="{WHITE}">{l['portrait_initial']}</text>

  <!-- Author name next to portrait -->
  <text x="95" y="90" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="{TEXT_DARK}">{escape_xml(l['title'])}</text>
  <text x="95" y="105" font-family="Arial, sans-serif" font-size="10" fill="{TEXT_MED}">{escape_xml(l['years'])}</text>
  <text x="95" y="120" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_LIGHT}" font-style="italic">{escape_xml(l['significance'][:50])}...)</text>

  <!-- Separator line -->
  <line x1="15" y1="138" x2="485" y2="138" stroke="{PRIMARY}" stroke-width="0.8" opacity="0.3"/>

  <!-- Works section -->
  <rect x="15" y="145" width="225" height="130" rx="8" fill="{WHITE}" stroke="{PRIMARY}" stroke-width="1" opacity="0.9" filter="url(#shadow{l['num']})"/>
  <rect x="15" y="145" width="225" height="24" rx="8" fill="{PRIMARY}" opacity="0.12"/>
  <rect x="15" y="161" width="225" height="8" fill="{PRIMARY}" opacity="0.12"/>
  <text x="127" y="162" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">Произведения</text>'''

    for i, work in enumerate(l["works"]):
        y = 183 + i * 22
        svg += f'''
  <rect x="25" y="{y - 7}" width="8" height="8" rx="2" fill="{PRIMARY}" opacity="0.6"/>
  <text x="39" y="{y}" font-family="Arial, sans-serif" font-size="10" fill="{TEXT_DARK}">{escape_xml(work)}</text>'''

    # Themes section
    svg += f'''
  <!-- Themes section -->
  <rect x="255" y="145" width="230" height="130" rx="8" fill="{WHITE}" stroke="{PRIMARY}" stroke-width="1" opacity="0.9" filter="url(#shadow{l['num']})"/>
  <rect x="255" y="145" width="230" height="24" rx="8" fill="{PRIMARY}" opacity="0.12"/>
  <rect x="255" y="161" width="230" height="8" fill="{PRIMARY}" opacity="0.12"/>
  <text x="370" y="162" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">Темы</text>'''

    for i, theme in enumerate(l["themes"]):
        y = 183 + i * 22
        svg += f'''
  <circle cx="273" cy="{y - 3}" r="3" fill="{PRIMARY_LIGHT}"/>
  <text x="282" y="{y}" font-family="Arial, sans-serif" font-size="10" fill="{TEXT_DARK}">{escape_xml(theme)}</text>'''

    # Significance box at bottom
    svg += f'''
  <!-- Significance -->
  <rect x="15" y="283" width="470" height="42" rx="8" fill="{WHITE}" stroke="{PRIMARY}" stroke-width="1" filter="url(#shadow{l['num']})"/>
  <rect x="15" y="283" width="6" height="42" rx="3" fill="{PRIMARY}"/>
  <text x="30" y="298" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}">Значение:</text>
  <text x="30" y="313" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_MED}">{escape_xml(l['significance'])}</text>

  <!-- Footer -->
  <rect x="0" y="330" width="500" height="20" rx="0" fill="{PRIMARY}" opacity="0.08"/>
  <rect x="0" y="338" width="500" height="12" rx="12" fill="{PRIMARY}" opacity="0.08"/>
  <text x="250" y="344" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_LIGHT}">Литература · 11 класс</text>
</svg>'''
    return svg


def build_theory_lesson(l):
    """Build SVG for the theory lesson (11)."""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <linearGradient id="headerGrad{l['num']}" x1="0" y1="0" x2="500" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="{PRIMARY_DARK}"/>
      <stop offset="100%" stop-color="{PRIMARY}"/>
    </linearGradient>
    <filter id="shadow{l['num']}" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#00000020"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="500" height="350" rx="12" fill="{BG}" stroke="{BORDER}" stroke-width="2.5"/>

  <!-- Header bar -->
  <rect x="0" y="0" width="500" height="56" rx="12" fill="url(#headerGrad{l['num']})"/>
  <rect x="0" y="20" width="500" height="36" fill="url(#headerGrad{l['num']})"/>

  <!-- Lesson number badge -->
  <circle cx="28" cy="28" r="16" fill="{WHITE}" opacity="0.25"/>
  <text x="28" y="33" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{WHITE}">{l['num']}</text>

  <!-- Title -->
  <text x="52" y="24" font-family="Arial, sans-serif" font-size="15" font-weight="bold" fill="{WHITE}">{escape_xml(l['title'])}</text>
  <text x="52" y="42" font-family="Arial, sans-serif" font-size="10" fill="{BG}" opacity="0.85">{escape_xml(l['subtitle'])}</text>

  <!-- Book icon -->
  <rect x="420" y="14" width="36" height="28" rx="4" fill="{WHITE}" opacity="0.2"/>
  <line x1="438" y1="16" x2="438" y2="40" stroke="{WHITE}" stroke-width="1.5" opacity="0.6"/>
  <rect x="423" y="18" width="13" height="20" rx="2" fill="{WHITE}" opacity="0.15"/>
  <rect x="440" y="18" width="13" height="20" rx="2" fill="{WHITE}" opacity="0.15"/>

  <!-- Concept grid - 2 columns x 3 rows -->
  <text x="250" y="72" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">Основные литературоведческие понятия</text>'''

    concepts = l["concepts"]
    col_width = 225
    row_height = 62
    start_x = 15
    start_y = 82

    for i, (term, definition) in enumerate(concepts):
        col = i % 2
        row = i // 2
        x = start_x + col * (col_width + 20)
        y = start_y + row * (row_height + 6)

        svg += f'''
  <!-- Concept {i+1}: {term} -->
  <rect x="{x}" y="{y}" width="{col_width}" height="{row_height}" rx="8" fill="{WHITE}" stroke="{PRIMARY}" stroke-width="1" filter="url(#shadow{l['num']})"/>
  <rect x="{x}" y="{y}" width="{col_width}" height="20" rx="8" fill="{PRIMARY}" opacity="0.12"/>
  <rect x="{x}" y="{y + 12}" width="{col_width}" height="8" fill="{PRIMARY}" opacity="0.12"/>
  <circle cx="{x + 14}" cy="{y + 10}" r="4" fill="{PRIMARY}"/>
  <text x="{x + 24}" y="{y + 14}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY_DARK}">{escape_xml(term)}</text>
  <text x="{x + 12}" y="{y + 34}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_MED}">{escape_xml(definition)}</text>'''

    # Significance box
    sig_y = start_y + 3 * (row_height + 6) + 2
    svg += f'''
  <!-- Significance -->
  <rect x="15" y="{sig_y}" width="470" height="42" rx="8" fill="{WHITE}" stroke="{PRIMARY}" stroke-width="1" filter="url(#shadow{l['num']})"/>
  <rect x="15" y="{sig_y}" width="6" height="42" rx="3" fill="{PRIMARY}"/>
  <text x="30" y="{sig_y + 15}" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}">Значение:</text>
  <text x="30" y="{sig_y + 30}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_MED}">{escape_xml(l['significance'])}</text>

  <!-- Footer -->
  <rect x="0" y="330" width="500" height="20" rx="0" fill="{PRIMARY}" opacity="0.08"/>
  <rect x="0" y="338" width="500" height="12" rx="12" fill="{PRIMARY}" opacity="0.08"/>
  <text x="250" y="344" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_LIGHT}">Литература · 11 класс</text>
</svg>'''
    return svg


def build_review_lesson(l):
    """Build SVG for the review lesson (12)."""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <linearGradient id="headerGrad{l['num']}" x1="0" y1="0" x2="500" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="{PRIMARY_DARK}"/>
      <stop offset="100%" stop-color="{PRIMARY}"/>
    </linearGradient>
    <filter id="shadow{l['num']}" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#00000020"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="500" height="350" rx="12" fill="{BG}" stroke="{BORDER}" stroke-width="2.5"/>

  <!-- Header bar -->
  <rect x="0" y="0" width="500" height="56" rx="12" fill="url(#headerGrad{l['num']})"/>
  <rect x="0" y="20" width="500" height="36" fill="url(#headerGrad{l['num']})"/>

  <!-- Lesson number badge -->
  <circle cx="28" cy="28" r="16" fill="{WHITE}" opacity="0.25"/>
  <text x="28" y="33" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{WHITE}">{l['num']}</text>

  <!-- Title -->
  <text x="52" y="24" font-family="Arial, sans-serif" font-size="15" font-weight="bold" fill="{WHITE}">{escape_xml(l['title'])}</text>
  <text x="52" y="42" font-family="Arial, sans-serif" font-size="10" fill="{BG}" opacity="0.85">{escape_xml(l['subtitle'])}</text>

  <!-- Checklist icon -->
  <rect x="430" y="14" width="28" height="28" rx="4" fill="{WHITE}" opacity="0.2"/>
  <line x1="438" y1="22" x2="450" y2="22" stroke="{WHITE}" stroke-width="1.5" opacity="0.6"/>
  <line x1="438" y1="28" x2="448" y2="28" stroke="{WHITE}" stroke-width="1.5" opacity="0.6"/>
  <line x1="438" y1="34" x2="452" y2="34" stroke="{WHITE}" stroke-width="1.5" opacity="0.6"/>
  <polyline points="434,20 436,22 434,24" stroke="{WHITE}" stroke-width="1" fill="none" opacity="0.5"/>

  <text x="250" y="72" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">Разделы курса для повторения</text>'''

    sections = l["review_sections"]
    col_width = 225
    row_height = 52
    start_x = 15
    start_y = 82

    for i, (section, detail) in enumerate(sections):
        col = i % 2
        row = i // 2
        x = start_x + col * (col_width + 20)
        y = start_y + row * (row_height + 6)

        # Number badge
        badge_x = x + 16
        badge_y = y + 16

        svg += f'''
  <!-- Section {i+1}: {section} -->
  <rect x="{x}" y="{y}" width="{col_width}" height="{row_height}" rx="8" fill="{WHITE}" stroke="{PRIMARY}" stroke-width="1" filter="url(#shadow{l['num']})"/>
  <rect x="{x}" y="{y}" width="{col_width}" height="22" rx="8" fill="{PRIMARY}" opacity="0.12"/>
  <rect x="{x}" y="{y + 14}" width="{col_width}" height="8" fill="{PRIMARY}" opacity="0.12"/>
  <circle cx="{badge_x}" cy="{badge_y}" r="8" fill="{PRIMARY}"/>
  <text x="{badge_x}" y="{badge_y + 3.5}" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{WHITE}">{i+1}</text>
  <text x="{x + 30}" y="{badge_y + 3}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY_DARK}">{escape_xml(section)}</text>
  <text x="{x + 12}" y="{y + 40}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_MED}">{escape_xml(detail)}</text>'''

    # Significance box
    sig_y = start_y + 3 * (row_height + 6) + 8
    svg += f'''
  <!-- Significance -->
  <rect x="15" y="{sig_y}" width="470" height="42" rx="8" fill="{WHITE}" stroke="{PRIMARY}" stroke-width="1" filter="url(#shadow{l['num']})"/>
  <rect x="15" y="{sig_y}" width="6" height="42" rx="3" fill="{PRIMARY}"/>
  <text x="30" y="{sig_y + 15}" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}">Значение:</text>
  <text x="30" y="{sig_y + 30}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_MED}">{escape_xml(l['significance'])}</text>

  <!-- Footer -->
  <rect x="0" y="330" width="500" height="20" rx="0" fill="{PRIMARY}" opacity="0.08"/>
  <rect x="0" y="338" width="500" height="12" rx="12" fill="{PRIMARY}" opacity="0.08"/>
  <text x="250" y="344" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_LIGHT}">Литература · 11 класс</text>
</svg>'''
    return svg


def generate_all():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    generated = 0

    for l in lessons:
        num = l["num"]

        if l.get("is_theory"):
            svg_content = build_theory_lesson(l)
        elif l.get("is_review"):
            svg_content = build_review_lesson(l)
        else:
            svg_content = build_author_lesson(l)

        # Validate as proper XML
        try:
            ET.fromstring(svg_content)
        except ET.ParseError as e:
            print(f"  ERROR: lesson{num}.svg - XML validation failed: {e}")
            continue

        filepath = os.path.join(OUTPUT_DIR, f"lesson{num}.svg")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)

        generated += 1
        print(f"  OK: lesson{num}.svg — {l['title']}")

    return generated


def validate_all():
    """Re-validate all generated SVGs as proper XML."""
    valid = 0
    errors = []
    for i in range(1, 13):
        filepath = os.path.join(OUTPUT_DIR, f"lesson{i}.svg")
        if not os.path.exists(filepath):
            errors.append(f"lesson{i}.svg — FILE NOT FOUND")
            continue
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            # Check basic SVG structure
            assert root.tag == "{http://www.w3.org/2000/svg}svg", f"Root tag is {root.tag}"
            assert root.get("viewBox") == "0 0 500 350", f"viewBox is {root.get('viewBox')}"
            valid += 1
        except Exception as e:
            errors.append(f"lesson{i}.svg — {e}")

    return valid, errors


if __name__ == "__main__":
    print("=" * 60)
    print("Generating Grade 11 Literature SVGs")
    print("=" * 60)
    print()

    count = generate_all()
    print()
    print(f"Generated: {count}/12 SVGs")
    print()

    print("Validating all SVGs...")
    valid, errors = validate_all()

    print(f"Valid: {valid}/12")
    if errors:
        print("Errors:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("All SVGs passed XML validation! ✓")

    print()
    print("Output directory:", OUTPUT_DIR)

    # List files
    files = sorted(os.listdir(OUTPUT_DIR))
    print(f"Files created: {len(files)}")
    for f in files:
        size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
        print(f"  {f} ({size:,} bytes)")
