#!/usr/bin/env python3
"""
Generate Grade 7 Literature SVG images (7 lessons).
Warm brown/amber color scheme (#92400E primary).
800x600, Russian text, character diagrams, themes.
"""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/literature"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─── Color Palette ───────────────────────────────────────────────
PRIMARY      = "#92400E"
PRIMARY_DARK = "#78350F"
PRIMARY_MID  = "#B45309"
ACCENT       = "#D97706"
ACCENT_LIGHT = "#F59E0B"
BG_LIGHT     = "#FFFBEB"
BG_WARM      = "#FEF3C7"
CARD_BG      = "#FFFFFF"
TEXT_DARK     = "#78350F"
TEXT_BODY     = "#92400E"
TEXT_LIGHT    = "#FFFFFF"
BORDER       = "#D97706"
LIGHT_AMBER  = "#FDE68A"
PALE_AMBER   = "#FEF3C7"


def escape_xml(text):
    """Escape special XML characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def svg_header():
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">
  <defs>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:{PRIMARY_DARK};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{ACCENT};stop-opacity:1" />
    </linearGradient>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:{BG_LIGHT};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{BG_WARM};stop-opacity:1" />
    </linearGradient>
    <filter id="shadow" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="1" dy="1" stdDeviation="2" flood-color="#00000020"/>
    </filter>
    <filter id="shadowLight" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="0.5" dy="0.5" stdDeviation="1" flood-color="#00000015"/>
    </filter>
  </defs>'''


def svg_background(title, badge_text):
    return f'''
  <!-- Background -->
  <rect width="800" height="600" fill="url(#bgGrad)" rx="8"/>
  <!-- Header bar -->
  <rect x="0" y="0" width="800" height="60" fill="url(#headerGrad)" rx="8"/>
  <rect x="0" y="30" width="800" height="30" fill="url(#headerGrad)"/>
  <text x="400" y="40" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="{TEXT_LIGHT}">{escape_xml(title)}</text>
  <!-- Lesson badge -->
  <rect x="12" y="68" width="105" height="24" rx="12" fill="{ACCENT}" opacity="0.9"/>
  <text x="64" y="84" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{TEXT_LIGHT}" font-weight="bold">{escape_xml(badge_text)}</text>'''


def card(x, y, w, h, title=""):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{CARD_BG}" stroke="{BORDER}" stroke-width="1.5" filter="url(#shadow)"/>'
    if title:
        s += f'<text x="{x + w/2}" y="{y + 18}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{TEXT_DARK}" font-weight="bold">{escape_xml(title)}</text>'
    return s


def section_header(x, y, text, font_size=12):
    return f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{font_size}" fill="{PRIMARY}" font-weight="bold">{escape_xml(text)}</text>'


def bullet_item(x, y, text, font_size=10, color=TEXT_BODY, indent=14):
    return (f'<circle cx="{x + 4}" cy="{y - 3}" r="2.5" fill="{ACCENT}"/>'
            f'<text x="{x + indent}" y="{y}" font-family="Arial, sans-serif" font-size="{font_size}" fill="{color}">{escape_xml(text)}</text>')


def arrow_line(x1, y1, x2, y2, label=""):
    s = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{ACCENT}" stroke-width="1.5" marker-end="url(#arrowhead)"/>'
    if label:
        mx, my = (x1+x2)/2, (y1+y2)/2 - 5
        s += f'<text x="{mx}" y="{my}" text-anchor="middle" font-family="Arial, sans-serif" font-size="8" fill="{PRIMARY}">{escape_xml(label)}</text>'
    return s


def rounded_box(x, y, w, h, fill, stroke, text="", font_size=10, text_color=TEXT_DARK, rx=8):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
    if text:
        s += f'<text x="{x + w/2}" y="{y + h/2 + 4}" text-anchor="middle" font-family="Arial, sans-serif" font-size="{font_size}" fill="{text_color}" font-weight="bold">{escape_xml(text)}</text>'
    return s


def divider_line(x1, y1, x2, y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{LIGHT_AMBER}" stroke-width="1" stroke-dasharray="4,3"/>'


# ══════════════════════════════════════════════════════════════════
# LESSON 1: Былины. Илья Муромец и Соловей-разбойник
# ══════════════════════════════════════════════════════════════════
def lesson_1():
    svg = svg_header()
    svg += svg_background("Былины. Илья Муромец и Соловей-разбойник", "Литература 7")

    # Left card: Features of Bylina
    svg += card(16, 100, 370, 240, "Признаки былины")
    features = [
        "Гиперболизация — преувеличение силы героя",
        "Повторы — троекратные повторы действий",
        "Постоянные эпитеты — «добрый молодец»",
        "Ритмизованная речь, напевность",
        "Историческая основа и фантастический сюжет",
        "Устная передача от сказителей",
    ]
    for i, f in enumerate(features):
        svg += bullet_item(30, 130 + i * 20, f, font_size=9)

    # Right card: Character diagram
    svg += card(414, 100, 370, 240, "Главные герои")
    # Ilya Muromets
    svg += rounded_box(430, 130, 150, 40, PALE_AMBER, ACCENT, "Илья Муромец", font_size=11)
    svg += bullet_item(435, 185, "Богатырь, защитник Руси", font_size=9)
    svg += bullet_item(435, 200, "30 лет сидел «на печи»", font_size=9)
    svg += bullet_item(435, 215, "Освободил дорогу в Киев", font_size=9)
    # Solovey-Razboynik
    svg += rounded_box(610, 130, 155, 40, "#FEE2E2", "#EF4444", "Соловей-разбойник", font_size=10)
    svg += bullet_item(615, 185, "Свистом губил людей", font_size=9)
    svg += bullet_item(615, 200, "Сидел у дороги 30 лет", font_size=9)
    svg += bullet_item(615, 215, "Побеждён Ильёй", font_size=9)
    # Arrow between them
    svg += '<line x1="580" y1="150" x2="610" y2="150" stroke="#EF4444" stroke-width="2" stroke-dasharray="4,2"/>'
    svg += '<text x="595" y="145" text-anchor="middle" font-family="Arial, sans-serif" font-size="8" fill="#EF4444">борьба</text>'

    # Bottom left: Plot structure
    svg += card(16, 355, 370, 230, "Композиция былины")
    steps = [
        ("Зачин", "«Из того ли из города из Мурома»"),
        ("Экспозиция", "Илья едет по дороге в Киев"),
        ("Кульминация", "Бой с Соловьём-разбойником"),
        ("Развязка", "Илья везёт врага в Киев"),
    ]
    for i, (step, desc) in enumerate(steps):
        y_pos = 390 + i * 44
        svg += rounded_box(30, y_pos - 8, 80, 22, ACCENT, ACCENT, step, font_size=9, text_color=TEXT_LIGHT)
        svg += f'<text x="120" y="{y_pos + 4}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">{escape_xml(desc)}</text>'
        if i < len(steps) - 1:
            svg += f'<line x1="70" y1="{y_pos + 14}" x2="70" y2="{y_pos + 36}" stroke="{ACCENT}" stroke-width="1.5"/>'

    # Bottom right: Key themes
    svg += card(414, 355, 370, 230, "Темы и идеи")
    themes = [
        ("Патриотизм", "Защита родной земли от врагов"),
        ("Сила духа", "Настоящая сила — в мужестве"),
        ("Справедливость", "Добро побеждает зло"),
        ("Народный идеал", "Герой — выразитель народных чаяний"),
    ]
    for i, (theme, desc) in enumerate(themes):
        y_pos = 385 + i * 44
        svg += rounded_box(430, y_pos - 8, 120, 22, PALE_AMBER, ACCENT, theme, font_size=9)
        svg += f'<text x="560" y="{y_pos + 4}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">{escape_xml(desc)}</text>'

    # Decorative: shield icon in top-right corner
    svg += f'<circle cx="760" cy="82" r="10" fill="none" stroke="{ACCENT}" stroke-width="1.5"/>'
    svg += f'<text x="760" y="87" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{ACCENT}">⚔</text>'

    svg += '\n</svg>'
    return svg


# ══════════════════════════════════════════════════════════════════
# LESSON 2: Сказки народов мира
# ══════════════════════════════════════════════════════════════════
def lesson_2():
    svg = svg_header()
    svg += svg_background("Сказки народов мира", "Литература 7")

    # Top left: Types of tales
    svg += card(16, 100, 370, 170, "Виды сказок")
    tale_types = [
        ("Волшебные", "Магия, превращения, чудесные помощники", "#FDE68A"),
        ("Бытовые", "Жизнь крестьян, социальный конфликт", "#FED7AA"),
        ("О животных", "Аллегория, животные — носители черт", "#BBF7D0"),
        ("Кумулятивные", "Накопление действий, повтор цепочки", "#DBEAFE"),
    ]
    for i, (ttype, desc, color) in enumerate(tale_types):
        y_pos = 128 + i * 34
        svg += rounded_box(30, y_pos - 6, 100, 20, color, ACCENT, ttype, font_size=9)
        svg += f'<text x="140" y="{y_pos + 5}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">{escape_xml(desc)}</text>'

    # Top right: Structure
    svg += card(414, 100, 370, 170, "Структура сказки")
    structure = [
        ("Присказка", "Настройка на сказочный лад"),
        ("Зачин", "«В некотором царстве...»"),
        ("Завязка", "Начало действия, конфликт"),
        ("Развитие", "Испытания героя"),
        ("Кульминация", "Главное испытание"),
        ("Развязка", "Победа, «и стали жить-поживать»"),
    ]
    for i, (part, desc) in enumerate(structure):
        y_pos = 124 + i * 22
        svg += rounded_box(425, y_pos - 6, 80, 16, PALE_AMBER, ACCENT, part, font_size=8)
        svg += f'<text x="512" y="{y_pos + 2}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">{escape_xml(desc)}</text>'
        if i < len(structure) - 1:
            svg += f'<line x1="465" y1="{y_pos + 10}" x2="465" y2="{y_pos + 16}" stroke="{ACCENT}" stroke-width="1" stroke-dasharray="2,2"/>'

    # Bottom left: Moral lessons
    svg += card(16, 285, 370, 300, "Нравственные уроки сказок")
    morals = [
        "Добро всегда побеждает зло",
        "Труд и честность вознаграждаются",
        "Жадность и зависть наказываются",
        "Ум и смекалка важнее силы",
        "Семья и дружба — главные ценности",
        "Слово — не воробей, вылетит — не поймаешь",
        "За добро плати добром",
        "Не имей сто рублей, а имей сто друзей",
    ]
    for i, m in enumerate(morals):
        svg += bullet_item(30, 315 + i * 26, m, font_size=9)

    # Bottom right: World tales examples
    svg += card(414, 285, 370, 300, "Сказки разных народов")
    world_tales = [
        ("🇷🇺 Русские", "Царевна-лягушка, Василиса Прекрасная"),
        ("🇫🇷 Французские", "Золушка, Кот в сапогах (Перро)"),
        ("🇩🇪 Немецкие", "Бременские музыканты (бр. Гримм)"),
        ("🇦🇪 Арабские", "Тысяча и одна ночь, Аладдин"),
        ("🇮🇳 Индийские", "Панчатантра, Рамаяна"),
        ("🇯🇵 Японские", "Урасима Таро, Momotaro"),
    ]
    for i, (country, tale) in enumerate(world_tales):
        y_pos = 315 + i * 38
        svg += section_header(428, y_pos, country, font_size=10)
        svg += f'<text x="428" y="{y_pos + 15}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">{escape_xml(tale)}</text>'
        if i < len(world_tales) - 1:
            svg += divider_line(428, y_pos + 24, 768, y_pos + 24)

    # Decorative element
    svg += f'<circle cx="760" cy="82" r="10" fill="none" stroke="{ACCENT}" stroke-width="1.5"/>'
    svg += f'<text x="760" y="87" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{ACCENT}">📖</text>'

    svg += '\n</svg>'
    return svg


# ══════════════════════════════════════════════════════════════════
# LESSON 3: Повесть временных лет
# ══════════════════════════════════════════════════════════════════
def lesson_3():
    svg = svg_header()
    svg += svg_background("«Повесть временных лет»", "Литература 7")

    # Top left: About the chronicle
    svg += card(16, 100, 370, 175, "О летописи")
    about = [
        "Древнейший русский летописный свод (XII в.)",
        "Автор — монах Нестор (ок. 1113 г.)",
        "Написана в Киево-Печерском монастыре",
        "Охватывает события от библейских времён",
        "До 1110 года — история Руси",
        "Цель: «откуда есть пошла Русская земля»",
    ]
    for i, a in enumerate(about):
        svg += bullet_item(30, 130 + i * 22, a, font_size=9)

    # Top right: Historical significance
    svg += card(414, 100, 370, 175, "Историческое значение")
    sig = [
        "Первый общерусский летописный свод",
        "Источники по истории Древней Руси",
        "Основа русской историографии",
        "Образец древнерусской литературы",
        "Единство церковной и светской мысли",
    ]
    for i, s in enumerate(sig):
        svg += bullet_item(428, 128 + i * 24, s, font_size=9)

    # Bottom left: Key episodes
    svg += card(16, 290, 370, 295, "Ключевые эпизоды")
    episodes = [
        ("Призвание варягов", "862 г. — Рюрик, начало государственности"),
        ("Путь «из варяг в греки»", "Торговый путь, связь Руси и Византии"),
        ("Крещение Руси", "988 г. — Владимир, принятие христианства"),
        ("Месть Ольги", "Мудрость и хитрость княгини"),
        ("Борьба с печенегами", "Защита рубежей Руси"),
    ]
    for i, (ep, desc) in enumerate(episodes):
        y_pos = 318 + i * 50
        svg += rounded_box(30, y_pos - 8, 145, 22, PALE_AMBER, ACCENT, ep, font_size=9)
        # Word wrap for description
        if len(desc) > 42:
            mid = desc[:42].rfind(' ')
            if mid < 20:
                mid = 42
            svg += f'<text x="185" y="{y_pos + 2}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">{escape_xml(desc[:mid])}</text>'
            svg += f'<text x="185" y="{y_pos + 15}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">{escape_xml(desc[mid:].strip())}</text>'
        else:
            svg += f'<text x="185" y="{y_pos + 4}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">{escape_xml(desc)}</text>'

    # Bottom right: Literary features
    svg += card(414, 290, 370, 295, "Особенности стиля")
    style_features = [
        "Летописный жанр — погодная запись",
        "Сочетание факта и легенды",
        "Религиозная интерпретация событий",
        "Эмоциональность оценок автора",
        "Цитаты из Библии и византийских хроник",
        "Фольклорные элементы (предания, поговорки)",
    ]
    for i, sf in enumerate(style_features):
        svg += bullet_item(428, 320 + i * 26, sf, font_size=9)

    # Sub-card: Authors
    svg += f'<rect x="425" y="485" width="348" height="85" rx="6" fill="{PALE_AMBER}" stroke="{ACCENT}" stroke-width="1" filter="url(#shadowLight)"/>'
    svg += section_header(435, 505, "Летописцы", font_size=11)
    authors = [
        "Нестор — основной автор (ок. 1113 г.)",
        "Сильвестр — редактор (1116 г.)",
        "Игнатий — продолжатель летописи",
    ]
    for i, a in enumerate(authors):
        svg += f'<text x="435" y="{525 + i * 17}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">• {escape_xml(a)}</text>'

    # Decorative
    svg += f'<circle cx="760" cy="82" r="10" fill="none" stroke="{ACCENT}" stroke-width="1.5"/>'
    svg += f'<text x="760" y="87" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{ACCENT}">📜</text>'

    svg += '\n</svg>'
    return svg


# ══════════════════════════════════════════════════════════════════
# LESSON 4: А.С. Пушкин. «Полтава»
# ══════════════════════════════════════════════════════════════════
def lesson_4():
    svg = svg_header()
    svg += svg_background("А.С. Пушкин. «Полтава»", "Литература 7")

    # Top left: About the poem
    svg += card(16, 100, 370, 155, "О поэме")
    about = [
        "Историческая поэма (1828 г.)",
        "Посвящена Полтавской битве (1709 г.)",
        "Три песни (песни-главы)",
        "Сочетание любовной и исторической линий",
        "Пётр I — идеал просвещённого монарха",
    ]
    for i, a in enumerate(about):
        svg += bullet_item(30, 128 + i * 22, a, font_size=9)

    # Top right: Characters
    svg += card(414, 100, 370, 155, "Главные герои")
    # Peter I
    svg += rounded_box(428, 126, 110, 30, PALE_AMBER, ACCENT, "Пётр I", font_size=10)
    svg += f'<text x="428" y="170" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">Царь-реформатор, полководец</text>'
    # Mazeppa
    svg += rounded_box(560, 126, 110, 30, "#FEE2E2", "#EF4444", "Мазепа", font_size=10)
    svg += f'<text x="560" y="170" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">Гетман, предатель Петра</text>'
    # Kochubey
    svg += rounded_box(428, 185, 110, 30, "#DBEAFE", "#3B82F6", "Кочубей", font_size=10)
    svg += f'<text x="428" y="229" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">Судья, отец Марии</text>'
    # Maria
    svg += rounded_box(560, 185, 110, 30, "#FCE7F3", "#EC4899", "Мария", font_size=10)
    svg += f'<text x="560" y="229" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">Дочь Кочубея, возлюбленная</text>'
    # Arrows
    svg += '<line x1="538" y1="141" x2="560" y2="141" stroke="#EF4444" stroke-width="1.5" stroke-dasharray="3,2"/>'
    svg += '<text x="549" y="136" text-anchor="middle" font-family="Arial, sans-serif" font-size="7" fill="#EF4444">враги</text>'
    svg += '<line x1="538" y1="200" x2="560" y2="200" stroke="#EC4899" stroke-width="1.5" stroke-dasharray="3,2"/>'
    svg += '<text x="549" y="195" text-anchor="middle" font-family="Arial, sans-serif" font-size="7" fill="#EC4899">дочь</text>'

    # Middle: Three songs structure
    svg += card(16, 270, 768, 100, "Композиция поэмы (три песни)")
    songs = [
        ("Песнь 1", "Любовь Марии и Мазепы, конфликт с Кочубеем"),
        ("Песнь 2", "Предательство Мазепы, казнь Кочубея"),
        ("Песнь 3", "Полтавская битва, победа Петра"),
    ]
    for i, (song, desc) in enumerate(songs):
        x_pos = 35 + i * 250
        svg += rounded_box(x_pos, 295, 75, 22, ACCENT, ACCENT, song, font_size=9, text_color=TEXT_LIGHT)
        svg += f'<text x="{x_pos + 82}" y="311" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">{escape_xml(desc)}</text>'

    # Bottom left: Historical context
    svg += card(16, 385, 370, 200, "Исторический контекст")
    context = [
        "Северная война (1700–1721 гг.)",
        "Полтавская битва — 27 июня 1709 г.",
        "Решающая победа над шведами Карла XII",
        "Мазепа перешёл на сторону шведов",
        "Битва определила ход войны",
        "Пётр: «Шведы — это враги, но учителя»",
    ]
    for i, c in enumerate(context):
        svg += bullet_item(30, 415 + i * 24, c, font_size=9)

    # Bottom right: Themes
    svg += card(414, 385, 370, 200, "Темы и идеи")
    themes = [
        ("Исторический долг", "Служение Родине выше личного"),
        ("Предательство", "Мазепа — коварный предатель"),
        ("Любовь и долг", "Мария разрывается между чувствами"),
        ("Слава России", "Пётр — воплощение силы державы"),
    ]
    for i, (theme, desc) in enumerate(themes):
        y_pos = 415 + i * 40
        svg += rounded_box(428, y_pos - 6, 120, 20, PALE_AMBER, ACCENT, theme, font_size=8)
        svg += f'<text x="556" y="{y_pos + 5}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">{escape_xml(desc)}</text>'

    # Decorative
    svg += f'<circle cx="760" cy="82" r="10" fill="none" stroke="{ACCENT}" stroke-width="1.5"/>'
    svg += f'<text x="760" y="87" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{ACCENT}">⚔</text>'

    svg += '\n</svg>'
    return svg


# ══════════════════════════════════════════════════════════════════
# LESSON 5: М.Ю. Лермонтов. «Песня про царя Ивана Васильевича»
# ══════════════════════════════════════════════════════════════════
def lesson_5():
    svg = svg_header()
    svg += svg_background("М.Ю. Лермонтов. «Песня про царя Ивана Васильевича»", "Литература 7")

    # Top left: About the poem
    svg += card(16, 100, 370, 130, "О произведении")
    about = [
        "Поэма-песня (1837 г.)",
        "Жанр: историческая песня",
        "Время действия: эпоха Ивана Грозного",
        "Тема: честь, достоинство, справедливость",
    ]
    for i, a in enumerate(about):
        svg += bullet_item(30, 126 + i * 22, a, font_size=9)

    # Top right: Characters diagram
    svg += card(414, 100, 370, 195, "Система персонажей")
    # Tsar Ivan
    svg += rounded_box(490, 124, 140, 30, "#FEE2E2", "#EF4444", "Царь Иван", font_size=10)
    svg += f'<text x="560" y="166" text-anchor="middle" font-family="Arial, sans-serif" font-size="8" fill="{TEXT_BODY}">Власть, произвол, но — справедливость</text>'
    # Kiribeevich
    svg += rounded_box(425, 182, 155, 30, "#FED7AA", "#F97316", "Кирибеевич", font_size=10)
    svg += f'<text x="425" y="224" font-family="Arial, sans-serif" font-size="8" fill="{TEXT_BODY}">Опричник, любимец царя, бесчестен</text>'
    # Kalashnikov
    svg += rounded_box(620, 182, 145, 30, PALE_AMBER, ACCENT, "Калашников", font_size=10)
    svg += f'<text x="620" y="224" font-family="Arial, sans-serif" font-size="8" fill="{TEXT_BODY}">Купец, защитник чести, праведник</text>'
    # Alena Dmitrievna
    svg += rounded_box(520, 242, 145, 24, "#FCE7F3", "#EC4899", "Алёна Дмитриевна", font_size=9)
    svg += f'<text x="520" y="278" font-family="Arial, sans-serif" font-size="8" fill="{TEXT_BODY}">Жена Калашникова, верность</text>'
    # Arrows
    svg += '<line x1="502" y1="154" x2="480" y2="182" stroke="#F97316" stroke-width="1.5" stroke-dasharray="3,2"/>'
    svg += '<text x="475" y="172" text-anchor="middle" font-family="Arial, sans-serif" font-size="7" fill="#F97316">слуги</text>'
    svg += '<line x1="580" y1="212" x2="620" y2="197" stroke="#EF4444" stroke-width="1.5" stroke-dasharray="3,2"/>'
    svg += '<text x="605" y="208" text-anchor="middle" font-family="Arial, sans-serif" font-size="7" fill="#EF4444">враги</text>'
    svg += '<line x1="620" y1="240" x2="590" y2="242" stroke="#EC4899" stroke-width="1.5" stroke-dasharray="3,2"/>'

    # Middle: The conflict
    svg += card(16, 245, 370, 115, "Конфликт")
    svg += f'<text x="30" y="275" font-family="Arial, sans-serif" font-size="9" fill="{PRIMARY}" font-weight="bold">Кирибеевич:</text>'
    svg += f'<text x="30" y="290" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">«Не стыдно тебе, старый, до белого света…» — домогательство</text>'
    svg += f'<text x="30" y="310" font-family="Arial, sans-serif" font-size="9" fill="{PRIMARY}" font-weight="bold">Калашников:</text>'
    svg += f'<text x="30" y="325" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">«Я убил его вольной волею, а за что — не скажу» — защита чести</text>'
    svg += f'<text x="30" y="345" font-family="Arial, sans-serif" font-size="9" fill="{PRIMARY}" font-weight="bold">Итог:</text>'
    svg += f'<text x="72" y="345" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">Казнь Калашникова, но народное уважение</text>'

    # Bottom: Themes and ideas
    svg += card(16, 375, 370, 210, "Темы и идеи")
    themes = [
        ("Честь и достоинство", "Выше жизни, выше царской воли"),
        ("Произвол власти", "Опричнина — вне закона и морали"),
        ("Народная правда", "Калашников — носитель народной правды"),
        ("Личность и государство", "Конфликт человека с деспотизмом"),
        ("Справедливость", "Царь казнит, но признаёт правоту"),
    ]
    for i, (theme, desc) in enumerate(themes):
        y_pos = 403 + i * 34
        svg += rounded_box(30, y_pos - 6, 135, 18, PALE_AMBER, ACCENT, theme, font_size=8)
        svg += f'<text x="172" y="{y_pos + 3}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">{escape_xml(desc)}</text>'

    # Bottom right: Literary devices
    svg += card(414, 375, 370, 210, "Художественные средства")
    devices = [
        "Фольклорный стиль (песня, былина)",
        "Постоянные эпитеты («добрый молодец»)",
        "Риторические вопросы и обращения",
        "Антитеза (Кирибеевич — Калашников)",
        "Гипербола в описании кулачного боя",
        "Символика (заря, тучи — предвестие)",
    ]
    for i, d in enumerate(devices):
        svg += bullet_item(428, 405 + i * 26, d, font_size=9)

    # Decorative
    svg += f'<circle cx="760" cy="82" r="10" fill="none" stroke="{ACCENT}" stroke-width="1.5"/>'
    svg += f'<text x="760" y="87" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{ACCENT}">👑</text>'

    svg += '\n</svg>'
    return svg


# ══════════════════════════════════════════════════════════════════
# LESSON 6: Н.В. Гоголь. «Тарас Бульба»
# ══════════════════════════════════════════════════════════════════
def lesson_6():
    svg = svg_header()
    svg += svg_background("Н.В. Гоголь. «Тарас Бульба»", "Литература 7")

    # Top left: About the story
    svg += card(16, 100, 370, 140, "О повести")
    about = [
        "Повесть (1835 г.), жанр: историческая",
        "Действие — XV век, Запорожская Сечь",
        "Основа — народные песни и предания",
        "Проблема: долг, предательство, патриотизм",
    ]
    for i, a in enumerate(about):
        svg += bullet_item(30, 126 + i * 24, a, font_size=9)

    # Top right: Character diagram
    svg += card(414, 100, 370, 195, "Персонажи: семья Бульба")
    # Taras
    svg += rounded_box(530, 124, 140, 30, PALE_AMBER, ACCENT, "Тарас Бульба", font_size=10)
    svg += f'<text x="600" y="166" text-anchor="middle" font-family="Arial, sans-serif" font-size="8" fill="{TEXT_BODY}">Полковник, идеал казачества</text>'
    # Ostap
    svg += rounded_box(428, 180, 120, 28, "#DBEAFE", "#3B82F6", "Остап", font_size=10)
    svg += f'<text x="428" y="218" font-family="Arial, sans-serif" font-size="8" fill="{TEXT_BODY}">Старший сын, воин, твёрдость</text>'
    # Andriy
    svg += rounded_box(620, 180, 120, 28, "#FEE2E2", "#EF4444", "Андрий", font_size=10)
    svg += f'<text x="620" y="218" font-family="Arial, sans-serif" font-size="8" fill="{TEXT_BODY}">Младший сын, предатель, любовь</text>'
    # Arrows from Taras to sons
    svg += '<line x1="560" y1="154" x2="488" y2="180" stroke="{ACCENT}" stroke-width="1.5"/>'
    svg += '<line x1="640" y1="154" x2="680" y2="180" stroke="{ACCENT}" stroke-width="1.5"/>'
    # Conflict arrow between brothers
    svg += '<line x1="548" y1="194" x2="620" y2="194" stroke="#EF4444" stroke-width="2" stroke-dasharray="4,2"/>'
    svg += '<text x="584" y="190" text-anchor="middle" font-family="Arial, sans-serif" font-size="7" fill="#EF4444">конфликт</text>'
    # Pannochka
    svg += rounded_box(690, 220, 80, 24, "#FCE7F3", "#EC4899", "Панночка", font_size=8)
    svg += '<line x1="680" y1="208" x2="710" y2="220" stroke="#EC4899" stroke-width="1" stroke-dasharray="3,2"/>'
    svg += '<text x="690" y="256" font-family="Arial, sans-serif" font-size="8" fill="{TEXT_BODY}">Ради неё Андрий предаёт</text>'

    # Middle: Cossack life
    svg += card(16, 255, 370, 105, "Казачья жизнь")
    cossack = [
        "Запорожская Сечь — вольное братство",
        "Товарищество — высшая ценность",
        "Война за веру и свободу",
        "Равенство казаков, выборность атамана",
    ]
    for i, c in enumerate(cossack):
        svg += bullet_item(30, 283 + i * 20, c, font_size=9)

    # Middle right: Ostap vs Andriy
    svg += card(414, 310, 370, 105, "Остап и Андрий — сравнение")
    # Ostap column
    svg += f'<text x="428" y="338" font-family="Arial, sans-serif" font-size="9" fill="#3B82F6" font-weight="bold">Остап:</text>'
    svg += f'<text x="428" y="353" font-family="Arial, sans-serif" font-size="8" fill="{TEXT_BODY}">Твёрдый, храбрый, преданный</text>'
    svg += f'<text x="428" y="368" font-family="Arial, sans-serif" font-size="8" fill="{TEXT_BODY}">Долг выше чувств, мученик</text>'
    svg += f'<text x="428" y="383" font-family="Arial, sans-serif" font-size="8" fill="{TEXT_BODY}">«Я вас не продам!»</text>'
    # Andriy column
    svg += f'<text x="610" y="338" font-family="Arial, sans-serif" font-size="9" fill="#EF4444" font-weight="bold">Андрий:</text>'
    svg += f'<text x="610" y="353" font-family="Arial, sans-serif" font-size="8" fill="{TEXT_BODY}">Мягкий, чувствительный</text>'
    svg += f'<text x="610" y="368" font-family="Arial, sans-serif" font-size="8" fill="{TEXT_BODY}">Любовь выше долга, предатель</text>'
    svg += f'<text x="610" y="383" font-family="Arial, sans-serif" font-size="8" fill="{TEXT_BODY}">«Отчизна — это ты!»</text>'
    # Divider
    svg += divider_line(595, 332, 595, 400)

    # Bottom: Themes
    svg += card(16, 375, 768, 210, "Темы и проблематика")
    themes = [
        ("Патриотизм", "Любовь к Родине — высшая добродетель", PALE_AMBER),
        ("Предательство", "Андрий — самое страшное преступление", "#FEE2E2"),
        ("Товарищество", "«Нет уз святее товарищества»", "#DBEAFE"),
        ("Отец и дети", "Тарас убивает сына — трагедия долга", "#FED7AA"),
        ("Свобода", "Казачья воля против угнетения", "#BBF7D0"),
    ]
    for i, (theme, desc, color) in enumerate(themes):
        x_pos = 35 + (i % 3) * 250
        y_pos = 410 + (i // 3) * 80
        svg += rounded_box(x_pos, y_pos, 140, 22, color, ACCENT, theme, font_size=9)
        svg += f'<text x="{x_pos}" y="{y_pos + 38}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">{escape_xml(desc)}</text>'

    # Decorative
    svg += f'<circle cx="760" cy="82" r="10" fill="none" stroke="{ACCENT}" stroke-width="1.5"/>'
    svg += f'<text x="760" y="87" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{ACCENT}">🗡</text>'

    svg += '\n</svg>'
    return svg


# ══════════════════════════════════════════════════════════════════
# LESSON 7: А.П. Платонов. «Юшка»
# ══════════════════════════════════════════════════════════════════
def lesson_7():
    svg = svg_header()
    svg += svg_background("А.П. Платонов. «Юшка»", "Литература 7")

    # Top left: About the story
    svg += card(16, 100, 370, 155, "О рассказе")
    about = [
        "Рассказ (1937 г.)",
        "Жанр: философский рассказ-притча",
        "Главный герой — Юшка, помощник кузнеца",
        "Тема: сострадание, доброта, духовность",
        "Стиль Платонова: «сказовая» простота",
    ]
    for i, a in enumerate(about):
        svg += bullet_item(30, 128 + i * 22, a, font_size=9)

    # Top right: Character diagram
    svg += card(414, 100, 370, 155, "Образ Юшки")
    # Yushka center
    svg += rounded_box(530, 122, 140, 32, PALE_AMBER, ACCENT, "Юшка", font_size=12)
    svg += f'<text x="600" y="168" text-anchor="middle" font-family="Arial, sans-serif" font-size="8" fill="{TEXT_BODY}">Больной, слабый, но — добрый</text>'
    # People
    svg += rounded_box(430, 180, 110, 24, "#FEE2E2", "#EF4444", "Люди", font_size=9)
    svg += f'<text x="430" y="214" font-family="Arial, sans-serif" font-size="8" fill="{TEXT_BODY}">Издеваются, не понимают</text>'
    # Girl-orphan
    svg += rounded_box(630, 180, 130, 24, "#BBF7D0", "#22C55E", "Девочка-сирота", font_size=9)
    svg += f'<text x="630" y="214" font-family="Arial, sans-serif" font-size="8" fill="{TEXT_BODY}">Спасена Юшкой, стала врачом</text>'
    # Arrows
    svg += '<line x1="540" y1="154" x2="485" y2="180" stroke="#EF4444" stroke-width="1.5" stroke-dasharray="3,2"/>'
    svg += '<text x="498" y="172" text-anchor="middle" font-family="Arial, sans-serif" font-size="7" fill="#EF4444">терпит</text>'
    svg += '<line x1="660" y1="154" x2="680" y2="180" stroke="#22C55E" stroke-width="1.5" stroke-dasharray="3,2"/>'
    svg += '<text x="685" y="172" text-anchor="middle" font-family="Arial, sans-serif" font-size="7" fill="#22C55E">спасает</text>'

    # Middle: Plot
    svg += card(16, 270, 768, 95, "Сюжет рассказа")
    plot_steps = [
        ("Жизнь Юшки", "Работает, терпит насмешки"),
        ("Доброта", "Отдаёт деньги девочке-сироте"),
        ("Гибель", "Убит прохожим, не ответил злом"),
        ("Память", "Девочка-врач — память о добре"),
    ]
    for i, (step, desc) in enumerate(plot_steps):
        x_pos = 35 + i * 190
        svg += rounded_box(x_pos, 292, 90, 20, ACCENT, ACCENT, step, font_size=8, text_color=TEXT_LIGHT)
        svg += f'<text x="{x_pos}" y="328" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">{escape_xml(desc)}</text>'
        if i < 3:
            svg += f'<line x1="{x_pos + 90}" y1="302" x2="{x_pos + 100}" y2="302" stroke="{ACCENT}" stroke-width="1.5"/>'

    # Bottom left: Moral themes
    svg += card(16, 380, 370, 205, "Нравственные темы")
    themes = [
        ("Сострадание", "Юшка жалеет людей, несмотря на жестокость"),
        ("Доброта", "Истинная доброта — бескорыстная"),
        ("Духовная сила", "Слабый телом — силён духом"),
        ("Жертвенность", "Юшка отдал всё ради других"),
        ("Память о добре", "Добро живёт после смерти человека"),
    ]
    for i, (theme, desc) in enumerate(themes):
        y_pos = 408 + i * 32
        svg += rounded_box(30, y_pos - 6, 115, 18, PALE_AMBER, ACCENT, theme, font_size=8)
        svg += f'<text x="152" y="{y_pos + 3}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_BODY}">{escape_xml(desc)}</text>'

    # Bottom right: Literary devices
    svg += card(414, 380, 370, 205, "Художественные особенности")
    devices = [
        "Сказовая манера повествования",
        "Простота и лаконичность языка",
        "Контраст: внешняя слабость — духовная сила",
        "Символ: Юшка — «ангел во плоти»",
        "Философский подтекст: в чём смысл жизни?",
        "Отсутствие авторской оценки — читатель судит",
    ]
    for i, d in enumerate(devices):
        svg += bullet_item(428, 408 + i * 26, d, font_size=9)

    # Important quote box
    svg += f'<rect x="425" y="545" width="348" height="32" rx="6" fill="{PALE_AMBER}" stroke="{ACCENT}" stroke-width="1" filter="url(#shadowLight)"/>'
    svg += f'<text x="599" y="566" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="{PRIMARY}" font-style="italic">«Сердце без злобы — как светлая лампада»</text>'

    # Decorative
    svg += f'<circle cx="760" cy="82" r="10" fill="none" stroke="{ACCENT}" stroke-width="1.5"/>'
    svg += f'<text x="760" y="87" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{ACCENT}">💛</text>'

    svg += '\n</svg>'
    return svg


# ══════════════════════════════════════════════════════════════════
# Generate and Validate
# ══════════════════════════════════════════════════════════════════
generators = [
    (1, lesson_1),
    (2, lesson_2),
    (3, lesson_3),
    (4, lesson_4),
    (5, lesson_5),
    (6, lesson_6),
    (7, lesson_7),
]

print("=" * 60)
print("Grade 7 Literature SVG Generator")
print("=" * 60)

results = []
for num, gen_func in generators:
    filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
    try:
        svg_content = gen_func()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)
        # Validate with xml.etree.ElementTree
        tree = ET.parse(filepath)
        root = tree.getroot()
        width = root.get("width")
        height = root.get("height")
        file_size = os.path.getsize(filepath)
        results.append((num, filepath, "OK", f"{width}x{height}", file_size))
        print(f"  ✓ Lesson {num}: {filepath} ({file_size:,} bytes, {width}x{height})")
    except ET.ParseError as e:
        results.append((num, filepath, "XML_ERROR", str(e), 0))
        print(f"  ✗ Lesson {num}: XML PARSE ERROR - {e}")
    except Exception as e:
        results.append((num, filepath, "ERROR", str(e), 0))
        print(f"  ✗ Lesson {num}: ERROR - {e}")

print()
print("=" * 60)
print("VALIDATION SUMMARY")
print("=" * 60)
ok_count = sum(1 for r in results if r[2] == "OK")
for num, path, status, detail, size in results:
    icon = "✓" if status == "OK" else "✗"
    print(f"  {icon} Lesson {num}: {status} | {detail} | {size:,} bytes")

print(f"\nTotal: {ok_count}/{len(results)} passed XML validation")
if ok_count == len(results):
    print("ALL SVG FILES GENERATED AND VALIDATED SUCCESSFULLY!")
