#!/usr/bin/env python3
"""Generate Grade 7 Music lesson SVG images with violet/purple color scheme."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/music"
WIDTH = 800
HEIGHT = 600
PRIMARY = "#7C3AED"
PRIMARY_LIGHT = "#A78BFA"
PRIMARY_DARK = "#5B21B6"
ACCENT = "#EDE9FE"
BG_GRAD_START = "#F5F3FF"
BG_GRAD_END = "#EDE9FE"
TEXT_DARK = "#1E1B4B"
TEXT_MED = "#4C1D95"
TEXT_LIGHT = "#6D28D9"
WHITE = "#FFFFFF"
CARD_BG = "#FAF5FF"

def escape_xml(text):
    """Escape text for XML safety."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def svg_header():
    """Return SVG header string."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">'''

def svg_footer():
    return "</svg>"

def defs_gradient(id_name, x1="0%", y1="0%", x2="100%", y2="100%", stops=None):
    """Create a linear gradient definition."""
    if stops is None:
        stops = [(BG_GRAD_START, "0%"), (BG_GRAD_END, "100%")]
    stop_elements = ""
    for color, offset in stops:
        stop_elements += f'<stop offset="{offset}" stop-color="{color}"/>'
    return f'''<defs><linearGradient id="{id_name}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">{stop_elements}</linearGradient></defs>'''

def rect(x, y, w, h, fill, rx=0, opacity=1.0, stroke=None, stroke_width=0):
    """Create a rectangle."""
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" rx="{rx}" opacity="{opacity}"'
    if stroke:
        s += f' stroke="{stroke}" stroke-width="{stroke_width}"'
    s += '/>'
    return s

def text(x, y, content, font_size=16, fill=TEXT_DARK, font_weight="normal", anchor="start", font_family="Arial, sans-serif"):
    """Create text element."""
    safe = escape_xml(content)
    return f'<text x="{x}" y="{y}" font-size="{font_size}" fill="{fill}" font-weight="{font_weight}" text-anchor="{anchor}" font-family="{font_family}">{safe}</text>'

def circle(cx, cy, r, fill, stroke=None, stroke_width=0, opacity=1.0):
    s = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" opacity="{opacity}"'
    if stroke:
        s += f' stroke="{stroke}" stroke-width="{stroke_width}"'
    s += '/>'
    return s

def ellipse(cx, cy, rx, ry, fill, opacity=1.0):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" opacity="{opacity}"/>'

def line(x1, y1, x2, y2, stroke, stroke_width=2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{stroke_width}"/>'

def path(d, fill="none", stroke=None, stroke_width=2, opacity=1.0):
    s = f'<path d="{d}" fill="{fill}" opacity="{opacity}"'
    if stroke:
        s += f' stroke="{stroke}" stroke-width="{stroke_width}"'
    s += '/>'
    return s

def music_note(x, y, scale=1.0, fill=PRIMARY):
    """Draw a simple eighth note."""
    s = scale
    # Note head (ellipse tilted)
    parts = []
    parts.append(f'<ellipse cx="{x}" cy="{y}" rx="{8*s}" ry="{6*s}" fill="{fill}" transform="rotate(-20 {x} {y})"/>')
    # Stem
    parts.append(line(x + 7*s, y - 2*s, x + 7*s, y - 35*s, fill, 2*s))
    # Flag
    parts.append(path(f"M{x+7*s},{y-35*s} Q{x+18*s},{y-25*s} {x+7*s},{y-18*s}", fill, stroke=fill, stroke_width=1.5*s))
    return "".join(parts)

def treble_clef(x, y, scale=1.0, fill=PRIMARY_DARK):
    """Stylized treble clef using path."""
    s = scale
    d = (f"M{x},{y+20*s} "
         f"C{x-10*s},{y+10*s} {x-15*s},{y-5*s} {x-5*s},{y-15*s} "
         f"C{x+5*s},{y-25*s} {x+15*s},{y-20*s} {x+10*s},{y-10*s} "
         f"C{x+5*s},{y} {x-10*s},{y+5*s} {x-5*s},{y+15*s} "
         f"C{x},{y+25*s} {x+5*s},{y+30*s} {x},{y+40*s} "
         f"C{x-5*s},{y+50*s} {x-15*s},{y+45*s} {x-10*s},{y+35*s}")
    return path(d, stroke=fill, stroke_width=2.5*s) + circle(x, y+45*s, 3*s, fill)

def staff_lines(x, y, width, gap=8, color=PRIMARY_LIGHT):
    """Draw 5 staff lines."""
    parts = []
    for i in range(5):
        parts.append(line(x, y + i * gap, x + width, y + i * gap, color, 1.5))
    return "".join(parts)

def card(x, y, w, h, title, items, icon_func=None, title_color=PRIMARY):
    """Draw a card with title and bullet items."""
    parts = []
    # Card background with shadow
    parts.append(rect(x+2, y+2, w, h, "#DDD6FE", 10, 0.4))
    parts.append(rect(x, y, w, h, CARD_BG, 10, 1.0, PRIMARY_LIGHT, 1.5))
    # Title bar
    parts.append(rect(x, y, w, 36, title_color, "10 10 0 0"))
    parts.append(text(x + w//2, y + 25, title, 15, WHITE, "bold", "middle"))
    # Items
    item_y = y + 56
    for item in items:
        parts.append(circle(x + 18, item_y - 4, 3, PRIMARY))
        parts.append(text(x + 28, item_y, item, 13, TEXT_DARK))
        item_y += 22
    # Icon
    if icon_func:
        parts.append(icon_func(x + w - 30, y + 50))
    return "".join(parts)


# ========== LESSON 1: Жанры вокальной музыки ==========
def lesson1():
    svg_parts = []
    svg_parts.append(svg_header())
    svg_parts.append(defs_gradient("bg1", stops=[(BG_GRAD_START, "0%"), ("#DDD6FE", "100%")]))
    svg_parts.append(rect(0, 0, WIDTH, HEIGHT, "url(#bg1)"))

    # Decorative music notes top-right
    svg_parts.append(music_note(700, 80, 1.2, PRIMARY_LIGHT))
    svg_parts.append(music_note(730, 50, 0.8, "#C4B5FD"))
    svg_parts.append(music_note(680, 40, 0.6, PRIMARY_LIGHT))

    # Decorative circles
    svg_parts.append(circle(50, 560, 40, PRIMARY, opacity=0.08))
    svg_parts.append(circle(750, 550, 30, PRIMARY_LIGHT, opacity=0.1))
    svg_parts.append(circle(100, 60, 25, "#C4B5FD", opacity=0.1))

    # Title area
    svg_parts.append(rect(0, 0, WIDTH, 90, PRIMARY, 0))
    svg_parts.append(rect(0, 88, WIDTH, 4, PRIMARY_DARK, 0))
    svg_parts.append(text(400, 38, "Жанры вокальной музыки", 26, WHITE, "bold", "middle"))
    svg_parts.append(text(400, 65, "Урок 1 • 7 класс • Музыка", 15, "#DDD6FE", "normal", "middle"))

    # Treble clef decoration
    svg_parts.append(treble_clef(60, 110, 1.5, PRIMARY_LIGHT))

    # Staff lines decoration
    svg_parts.append(staff_lines(100, 120, 200, 7, "#C4B5FD"))

    # Central definition
    svg_parts.append(rect(40, 105, 720, 50, WHITE, 8, 0.9, PRIMARY, 1))
    svg_parts.append(text(400, 135, "Вокальная музыка — музыка, исполняемая голосом", 16, TEXT_MED, "bold", "middle"))

    # Cards row 1
    # Card 1: Песня
    svg_parts.append(card(40, 175, 225, 185, "Песня", [
        "Самый распространённый",
        "вокальный жанр",
        "Куплетная форма",
        "Народная и авторская",
        "Песня-романс"
    ]))

    # Card 2: Романс
    svg_parts.append(card(285, 175, 225, 185, "Романс", [
        "Лирическое стихотворение",
        "положенное на музыку",
        "Камерный жанр",
        "Сольное исполнение",
        "Фортепианный аккомпанемент"
    ]))

    # Card 3: Ария
    svg_parts.append(card(530, 175, 230, 185, "Ария", [
        "Сольная номер в опере",
        "Характер героя",
        "Законченный номер",
        "Ария-монолог",
        "Ария-песня (каватина)"
    ]))

    # Cards row 2
    # Card 4: Хоровая музыка
    svg_parts.append(card(40, 380, 350, 185, "Хоровая музыка", [
        "Исполняется хором (ансамбль певцов)",
        "Виды хоров: мужской, женский, смешанный, детский",
        "A cappella — без сопровождения",
        "Духовная и светская хоровая музыка",
        "Хор в опере, кантате, оратории"
    ]))

    # Card 5: Камерная вокальная музыка
    svg_parts.append(card(410, 380, 350, 185, "Камерная вокальная музыка", [
        "Для небольшого зала",
        "Интимное исполнение",
        "Вокальный цикл — цикл романсов",
        "«Зимний путь» Шуберта",
        "«Детская» Мусоргского"
    ]))

    # Decorative notes bottom
    svg_parts.append(music_note(30, 560, 0.7, "#C4B5FD"))
    svg_parts.append(music_note(760, 570, 0.9, PRIMARY_LIGHT))

    svg_parts.append(svg_footer())
    return "".join(svg_parts)


# ========== LESSON 2: Инструментальные жанры ==========
def lesson2():
    svg_parts = []
    svg_parts.append(svg_header())
    svg_parts.append(defs_gradient("bg2", stops=[("#F5F3FF", "0%"), ("#DDD6FE", "100%")]))
    svg_parts.append(rect(0, 0, WIDTH, HEIGHT, "url(#bg2)"))

    # Decorative elements
    svg_parts.append(circle(740, 100, 35, PRIMARY_LIGHT, opacity=0.1))
    svg_parts.append(circle(60, 540, 45, PRIMARY, opacity=0.06))
    svg_parts.append(music_note(710, 55, 1.0, "#C4B5FD"))
    svg_parts.append(music_note(30, 100, 0.6, PRIMARY_LIGHT))

    # Title
    svg_parts.append(rect(0, 0, WIDTH, 90, PRIMARY, 0))
    svg_parts.append(rect(0, 88, WIDTH, 4, PRIMARY_DARK, 0))
    svg_parts.append(text(400, 38, "Инструментальные жанры", 26, WHITE, "bold", "middle"))
    svg_parts.append(text(400, 65, "Урок 2 • 7 класс • Музыка", 15, "#DDD6FE", "normal", "middle"))

    # Staff decoration
    svg_parts.append(staff_lines(20, 100, 120, 6, "#C4B5FD"))
    svg_parts.append(treble_clef(130, 100, 1.2, "#C4B5FD"))

    # Definition bar
    svg_parts.append(rect(40, 105, 720, 50, WHITE, 8, 0.9, PRIMARY, 1))
    svg_parts.append(text(400, 135, "Инструментальная музыка — музыка, исполняемая на инструментах", 15, TEXT_MED, "bold", "middle"))

    # 4 genre cards in 2x2 grid
    # Sonata
    svg_parts.append(card(40, 175, 355, 170, "Соната", [
        "Многочастное произведение",
        "Для 1-2 инструментов",
        "3-4 части: Allegro — Andante — Menuet — Finale",
        "Сонатная форма — главная",
        "Бетховен «Лунная соната»"
    ]))

    # Симфония
    svg_parts.append(card(415, 175, 345, 170, "Симфония", [
        "Для симфонического оркестра",
        "4 части, масштабное произведение",
        "Развитие от сонаты",
        "Гайдн — «отец симфонии»",
        "Чайковский — симфонии №1-6"
    ]))

    # Концерт
    svg_parts.append(card(40, 365, 355, 195, "Концерт", [
        "Соло инструмент + оркестр",
        "Диалог солиста и оркестра",
        "3 части (обычно)",
        "Виртуозная партия солиста",
        "Каденция — сольная импровизация",
        "Чайковский: Концерт №1 для ф-но"
    ]))

    # Сюита
    svg_parts.append(card(415, 365, 345, 195, "Сюита", [
        "Цикл контрастных пьес",
        "Танцевального характера",
        "Старинная сюита: Аллеманда —",
        "Куранта — Сарабанда — Жига",
        "Бах — Французские сюиты",
        "«Щелкунчик» Чайковского"
    ]))

    # Bottom decorative note
    svg_parts.append(music_note(760, 565, 0.8, "#C4B5FD"))

    svg_parts.append(svg_footer())
    return "".join(svg_parts)


# ========== LESSON 3: М.И. Глинка ==========
def lesson3():
    svg_parts = []
    svg_parts.append(svg_header())
    svg_parts.append(defs_gradient("bg3", stops=[("#F5F3FF", "0%"), ("#C4B5FD", "100%")]))
    svg_parts.append(rect(0, 0, WIDTH, HEIGHT, "url(#bg3)"))

    # Decorative
    svg_parts.append(circle(750, 80, 30, PRIMARY_LIGHT, opacity=0.15))
    svg_parts.append(circle(50, 550, 35, PRIMARY, opacity=0.08))

    # Title
    svg_parts.append(rect(0, 0, WIDTH, 90, PRIMARY, 0))
    svg_parts.append(rect(0, 88, WIDTH, 4, PRIMARY_DARK, 0))
    svg_parts.append(text(400, 35, "М.И. Глинка", 28, WHITE, "bold", "middle"))
    svg_parts.append(text(400, 62, "Основоположник русской классической музыки", 16, "#DDD6FE", "normal", "middle"))
    svg_parts.append(text(400, 80, "Урок 3 • 7 класс • Музыка", 13, "#C4B5FD", "normal", "middle"))

    # Portrait placeholder (stylized)
    svg_parts.append(rect(40, 105, 200, 220, WHITE, 12, 0.95, PRIMARY, 2))
    svg_parts.append(ellipse(140, 165, 40, 50, "#EDE9FE"))
    svg_parts.append(rect(100, 220, 80, 60, PRIMARY_LIGHT, 5, 0.5))
    svg_parts.append(text(140, 300, "1804—1857", 14, TEXT_MED, "bold", "middle"))
    svg_parts.append(text(140, 318, "Михаил Иванович", 12, TEXT_DARK, "normal", "middle"))
    svg_parts.append(text(140, 334, "Глинка", 12, TEXT_DARK, "normal", "middle"))

    # Key facts
    svg_parts.append(rect(270, 105, 490, 220, WHITE, 12, 0.95, PRIMARY_LIGHT, 1.5))
    svg_parts.append(rect(270, 105, 490, 36, PRIMARY_DARK, "12 12 0 0"))
    svg_parts.append(text(515, 130, "Ключевые факты", 15, WHITE, "bold", "middle"))

    facts = [
        "Основоположник русской классической музыки",
        "Первые русские оперы: «Иван Сусанин» и «Руслан и Людмила»",
        "«Патриотическая песня» — гимн России (1990-2000)",
        "Реформатор русской оперы: соединил западноевропейскую",
        "форму с русским национальным содержанием",
        "«Камаринская», «Вальс-фантазия» — оркестровые шедевры"
    ]
    fy = 158
    for f in facts:
        svg_parts.append(circle(288, fy - 4, 3, PRIMARY))
        svg_parts.append(text(298, fy, f, 13, TEXT_DARK))
        fy += 26

    # Opera 1: Иван Сусанин
    svg_parts.append(rect(40, 345, 360, 220, WHITE, 12, 0.95, PRIMARY, 1.5))
    svg_parts.append(rect(40, 345, 360, 36, "#5B21B6", "12 12 0 0"))
    svg_parts.append(text(220, 370, "«Иван Сусанин» (1836)", 15, WHITE, "bold", "middle"))
    items1 = [
        "Первая русская героико-патриотическая опера",
        "Подлинно народный сюжет",
        "Сусанин — крестьянин-герой",
        "Хор «Славься» — символ России",
        "Эпилог — торжество народа",
        "Опера-драма с речитативами"
    ]
    iy = 398
    for item in items1:
        svg_parts.append(circle(58, iy - 4, 3, PRIMARY_DARK))
        svg_parts.append(text(68, iy, item, 12.5, TEXT_DARK))
        iy += 26

    # Opera 2: Руслан и Людмила
    svg_parts.append(rect(420, 345, 340, 220, WHITE, 12, 0.95, PRIMARY, 1.5))
    svg_parts.append(rect(420, 345, 340, 36, "#5B21B6", "12 12 0 0"))
    svg_parts.append(text(590, 370, "«Руслан и Людмила» (1842)", 15, WHITE, "bold", "middle"))
    items2 = [
        "Опера-сказка по А.С. Пушкину",
        "5 действий + увертюра",
        "Восточные мотивы (чародей Наина)",
        "Ария Руслана, Рондо Фарлафа",
        "Марш Черномора — знаменитый",
        "Эпико-сказочный жанр"
    ]
    iy = 398
    for item in items2:
        svg_parts.append(circle(438, iy - 4, 3, PRIMARY_DARK))
        svg_parts.append(text(448, iy, item, 12.5, TEXT_DARK))
        iy += 26

    # Decorative notes
    svg_parts.append(music_note(770, 560, 0.7, PRIMARY_LIGHT))
    svg_parts.append(music_note(20, 570, 0.6, "#C4B5FD"))

    svg_parts.append(svg_footer())
    return "".join(svg_parts)


# ========== LESSON 4: «Могучая кучка» и П.И. Чайковский ==========
def lesson4():
    svg_parts = []
    svg_parts.append(svg_header())
    svg_parts.append(defs_gradient("bg4", stops=[(BG_GRAD_START, "0%"), ("#C4B5FD", "100%")]))
    svg_parts.append(rect(0, 0, WIDTH, HEIGHT, "url(#bg4)"))

    # Decorative
    svg_parts.append(circle(760, 70, 25, PRIMARY_LIGHT, opacity=0.12))
    svg_parts.append(music_note(730, 50, 0.8, "#C4B5FD"))

    # Title
    svg_parts.append(rect(0, 0, WIDTH, 90, PRIMARY, 0))
    svg_parts.append(rect(0, 88, WIDTH, 4, PRIMARY_DARK, 0))
    svg_parts.append(text(400, 35, "«Могучая кучка» и П.И. Чайковский", 24, WHITE, "bold", "middle"))
    svg_parts.append(text(400, 62, "Русская композиторская школа XIX века", 15, "#DDD6FE", "normal", "middle"))
    svg_parts.append(text(400, 80, "Урок 4 • 7 класс • Музыка", 13, "#C4B5FD", "normal", "middle"))

    # Mighty Five section
    svg_parts.append(rect(30, 100, 440, 250, WHITE, 12, 0.95, PRIMARY, 1.5))
    svg_parts.append(rect(30, 100, 440, 36, PRIMARY_DARK, "12 12 0 0"))
    svg_parts.append(text(250, 125, "«Могучая кучка» (Балакиревский кружок)", 14, WHITE, "bold", "middle"))

    composers = [
        ("М.А. Балакирев (1837-1910)", "Руководитель кружка, пианист, дирижёр"),
        ("Ц.А. Кюи (1835-1918)", "Музыкальный критик, инженер-строитель"),
        ("М.П. Мусоргский (1839-1881)", "«Борис Годунов», «Картинки с выставки»"),
        ("Н.А. Римский-Корсаков (1844-1908)", "«Шехеразада», «Снегурочка», педагог"),
        ("А.П. Бородин (1833-1887)", "«Князь Игорь», химик-учёный"),
    ]
    cy = 152
    for name, desc in composers:
        svg_parts.append(circle(50, cy - 4, 5, PRIMARY))
        svg_parts.append(text(62, cy, name, 13, TEXT_MED, "bold"))
        svg_parts.append(text(62, cy + 17, desc, 12, TEXT_DARK))
        cy += 38

    # Key ideas
    svg_parts.append(rect(490, 100, 280, 250, WHITE, 12, 0.95, PRIMARY_LIGHT, 1.5))
    svg_parts.append(rect(490, 100, 280, 36, PRIMARY, "12 12 0 0"))
    svg_parts.append(text(630, 125, "Идеи кружка", 14, WHITE, "bold", "middle"))

    ideas = [
        "Национальная русская музыка",
        "Народные песни — основа",
        "Исторические сюжеты",
        "Сказочные образы",
        "Правдивость высказывания",
        "Против академизма",
        "Реализм в музыке"
    ]
    iy = 152
    for idea in ideas:
        svg_parts.append(circle(508, iy - 4, 3, PRIMARY))
        svg_parts.append(text(518, iy, idea, 12.5, TEXT_DARK))
        iy += 27

    # Tchaikovsky section
    svg_parts.append(rect(30, 365, 740, 210, WHITE, 12, 0.95, PRIMARY, 2))
    svg_parts.append(rect(30, 365, 740, 36, PRIMARY_DARK, "12 12 0 0"))
    svg_parts.append(text(400, 390, "П.И. Чайковский (1840-1893)", 16, WHITE, "bold", "middle"))

    # Two columns
    left_items = [
        "Великий русский композитор",
        "Мировое признание при жизни",
        "Профессор Московской консерватории",
        "Глубокий лирик и психолог",
        "6 симфоний, 3 балета, 11 опер"
    ]
    right_items = [
        "«Лебединое озеро» (1876) — балет",
        "«Щелкунчик» (1892) — балет",
        "«Спящая красавица» (1889) — балет",
        "«Евгений Онегин» (1878) — опера",
        "«Пиковая дама» (1890) — опера"
    ]

    ly = 420
    for item in left_items:
        svg_parts.append(circle(50, ly - 4, 3, PRIMARY_DARK))
        svg_parts.append(text(60, ly, item, 12.5, TEXT_DARK))
        ly += 25

    ry = 420
    for item in right_items:
        svg_parts.append(circle(410, ry - 4, 3, PRIMARY_DARK))
        svg_parts.append(text(420, ry, item, 12.5, TEXT_DARK))
        ry += 25

    # Decorative
    svg_parts.append(music_note(20, 575, 0.6, "#C4B5FD"))
    svg_parts.append(music_note(770, 570, 0.7, PRIMARY_LIGHT))

    svg_parts.append(svg_footer())
    return "".join(svg_parts)


# ========== LESSON 5: Венская классическая школа ==========
def lesson5():
    svg_parts = []
    svg_parts.append(svg_header())
    svg_parts.append(defs_gradient("bg5", stops=[(BG_GRAD_START, "0%"), ("#DDD6FE", "100%")]))
    svg_parts.append(rect(0, 0, WIDTH, HEIGHT, "url(#bg5)"))

    # Decorative
    svg_parts.append(circle(760, 80, 30, PRIMARY_LIGHT, opacity=0.1))
    svg_parts.append(music_note(720, 50, 0.9, "#C4B5FD"))
    svg_parts.append(music_note(30, 110, 0.5, PRIMARY_LIGHT))

    # Title
    svg_parts.append(rect(0, 0, WIDTH, 90, PRIMARY, 0))
    svg_parts.append(rect(0, 88, WIDTH, 4, PRIMARY_DARK, 0))
    svg_parts.append(text(400, 35, "Венская классическая школа", 26, WHITE, "bold", "middle"))
    svg_parts.append(text(400, 62, "Фундамент европейской музыкальной культуры", 15, "#DDD6FE", "normal", "middle"))
    svg_parts.append(text(400, 80, "Урок 5 • 7 класс • Музыка", 13, "#C4B5FD", "normal", "middle"))

    # Three composer cards
    # Haydn
    svg_parts.append(rect(30, 105, 235, 240, WHITE, 12, 0.95, PRIMARY, 1.5))
    svg_parts.append(rect(30, 105, 235, 40, "#5B21B6", "12 12 0 0"))
    svg_parts.append(text(147, 131, "Й. Гайдн", 17, WHITE, "bold", "middle"))
    svg_parts.append(text(147, 162, "1732—1809", 13, TEXT_LIGHT, "normal", "middle"))
    haydn = [
        "«Отец симфонии»",
        "104 симфонии",
        "«Отец струнного квартета»",
        "Создал классическую форму",
        "Оратории «Сотворение мира»",
        "«Времена года»",
        "Служил у князя Эстерхази"
    ]
    hy = 180
    for h in haydn:
        svg_parts.append(circle(48, hy - 4, 3, PRIMARY))
        svg_parts.append(text(58, hy, h, 12, TEXT_DARK))
        hy += 22

    # Mozart
    svg_parts.append(rect(283, 105, 235, 240, WHITE, 12, 0.95, PRIMARY, 2))
    svg_parts.append(rect(283, 105, 235, 40, PRIMARY, "12 12 0 0"))
    svg_parts.append(text(400, 131, "В.А. Моцарт", 17, WHITE, "bold", "middle"))
    svg_parts.append(text(400, 162, "1756—1791", 13, TEXT_LIGHT, "normal", "middle"))
    mozart = [
        "Вундеркинд, гений",
        "Более 600 произведений",
        "«Реквием» — незаконченный",
        "«Свадьба Фигаро» — опера",
        "«Дон Жуан» — опера",
        "«Волшебная флейта» — опера",
        "41 симфония, 27 концертов"
    ]
    my = 180
    for m in mozart:
        svg_parts.append(circle(301, my - 4, 3, PRIMARY))
        svg_parts.append(text(311, my, m, 12, TEXT_DARK))
        my += 22

    # Beethoven
    svg_parts.append(rect(535, 105, 235, 240, WHITE, 12, 0.95, PRIMARY, 1.5))
    svg_parts.append(rect(535, 105, 235, 40, "#5B21B6", "12 12 0 0"))
    svg_parts.append(text(652, 131, "Л. Бетховен", 17, WHITE, "bold", "middle"))
    svg_parts.append(text(652, 162, "1770—1827", 13, TEXT_LIGHT, "normal", "middle"))
    beethoven = [
        "Мост классики и романтизма",
        "9 симфоний (Девятая — с хором)",
        "32 фортепианные сонаты",
        "«Лунная соната» №14",
        "«К Элизе» — ф-п миниатюра",
        "Глухота не остановила творчество",
        "«Ода к радости» — гимн ЕС"
    ]
    by = 180
    for b in beethoven:
        svg_parts.append(circle(553, by - 4, 3, PRIMARY))
        svg_parts.append(text(563, by, b, 12, TEXT_DARK))
        by += 22

    # Common achievements section
    svg_parts.append(rect(30, 365, 740, 210, WHITE, 12, 0.95, PRIMARY_LIGHT, 1.5))
    svg_parts.append(rect(30, 365, 740, 36, PRIMARY_DARK, "12 12 0 0"))
    svg_parts.append(text(400, 390, "Достижения венской классической школы", 15, WHITE, "bold", "middle"))

    # Two columns of achievements
    left = [
        "Утверждение сонатной формы",
        "Классическая симфония (4 части)",
        "Струнный квартет как жанр",
        "Классический состав оркестра",
        "Тонально-функциональная система"
    ]
    right = [
        "Развитие оперного жанра",
        "Фортепианный концерт",
        "Оратория и месса",
        "Программная симфония",
        "Переход к романтизму (Бетховен)"
    ]
    ly = 418
    for l in left:
        svg_parts.append(circle(50, ly - 4, 4, PRIMARY_DARK))
        svg_parts.append(text(62, ly, l, 13, TEXT_DARK))
        ly += 28
    ry = 418
    for r in right:
        svg_parts.append(circle(410, ry - 4, 4, PRIMARY_DARK))
        svg_parts.append(text(422, ry, r, 13, TEXT_DARK))
        ry += 28

    # Staff decoration bottom
    svg_parts.append(staff_lines(30, 570, 740, 5, "#C4B5FD"))

    svg_parts.append(svg_footer())
    return "".join(svg_parts)


# ========== LESSON 6: Джаз и рок-музыка ==========
def lesson6():
    svg_parts = []
    svg_parts.append(svg_header())
    svg_parts.append(defs_gradient("bg6", stops=[(BG_GRAD_START, "0%"), ("#DDD6FE", "100%")]))
    svg_parts.append(rect(0, 0, WIDTH, HEIGHT, "url(#bg6)"))

    # Decorative
    svg_parts.append(circle(750, 60, 30, PRIMARY_LIGHT, opacity=0.12))
    svg_parts.append(music_note(720, 40, 0.7, "#C4B5FD"))
    svg_parts.append(music_note(30, 110, 0.5, PRIMARY_LIGHT))

    # Title
    svg_parts.append(rect(0, 0, WIDTH, 90, PRIMARY, 0))
    svg_parts.append(rect(0, 88, WIDTH, 4, PRIMARY_DARK, 0))
    svg_parts.append(text(400, 35, "Джаз и рок-музыка", 28, WHITE, "bold", "middle"))
    svg_parts.append(text(400, 62, "Музыкальные направления XX века", 15, "#DDD6FE", "normal", "middle"))
    svg_parts.append(text(400, 80, "Урок 6 • 7 класс • Музыка", 13, "#C4B5FD", "normal", "middle"))

    # Jazz section
    svg_parts.append(rect(30, 100, 370, 240, WHITE, 12, 0.95, PRIMARY, 2))
    svg_parts.append(rect(30, 100, 370, 40, PRIMARY_DARK, "12 12 0 0"))
    svg_parts.append(text(215, 127, "Джаз", 20, WHITE, "bold", "middle"))

    jazz = [
        ("Происхождение:", "Новый Орлеан, рубеж XIX-XX вв."),
        ("Источники:", "Африканские ритмы + блюзы"),
        ("Спирчуэлс:", "Духовные песни афроамериканцев"),
        ("Импровизация:", "Главный принцип джаза"),
        ("Свинго:", "Особое чувство ритма"),
        ("Стили:", "Нью-Орлеан, свинг, бибоп, кул"),
        ("Выдающиеся:", "Л. Армстронг, Д. Эллингтон"),
        ("", "М. Дэвис, Дж. Колтрейн"),
    ]
    jy = 158
    for label, val in jazz:
        if label:
            svg_parts.append(text(48, jy, label, 12, TEXT_MED, "bold"))
            svg_parts.append(text(140, jy, val, 12, TEXT_DARK))
        else:
            svg_parts.append(text(140, jy, val, 12, TEXT_DARK))
        jy += 22

    # Rock section
    svg_parts.append(rect(410, 100, 360, 240, WHITE, 12, 0.95, PRIMARY, 2))
    svg_parts.append(rect(410, 100, 360, 40, PRIMARY_DARK, "12 12 0 0"))
    svg_parts.append(text(590, 127, "Рок-музыка", 20, WHITE, "bold", "middle"))

    rock = [
        ("Происхождение:", "1950-е гг., США"),
        ("Источники:", "Рок-н-ролл, кантри, блюз"),
        ("Элвис Пресли:", "«Король рок-н-ролла»"),
        ("The Beatles:", "Британское вторжение, 1964"),
        ("Стили:", "Рок, панк, метал, прогрессив"),
        ("Электрогитара:", "Главный инструмент рока"),
        ("Рок-опера:", "«Jesus Christ Superstar»"),
        ("", "«Tommy» (The Who)")
    ]
    ry = 158
    for label, val in rock:
        if label:
            svg_parts.append(text(428, ry, label, 12, TEXT_MED, "bold"))
            svg_parts.append(text(525, ry, val, 12, TEXT_DARK))
        else:
            svg_parts.append(text(525, ry, val, 12, TEXT_DARK))
        ry += 22

    # Instruments section
    svg_parts.append(rect(30, 360, 370, 215, WHITE, 12, 0.95, PRIMARY_LIGHT, 1.5))
    svg_parts.append(rect(30, 360, 370, 36, PRIMARY, "12 12 0 0"))
    svg_parts.append(text(215, 385, "Инструменты", 15, WHITE, "bold", "middle"))

    instruments = [
        ("Джаз:", "саксофон, труба, тромбон"),
        ("", "контрабас, фортепиано, ударные"),
        ("Рок:", "электрогитара, бас-гитара"),
        ("", "ударная установка, синтезатор"),
        ("Общие:", "гитара, ударные, клавишные"),
        ("", "вокал, духовые")
    ]
    iy = 412
    for label, val in instruments:
        if label:
            svg_parts.append(text(48, iy, label, 12.5, TEXT_MED, "bold"))
            svg_parts.append(text(110, iy, val, 12.5, TEXT_DARK))
        else:
            svg_parts.append(text(110, iy, val, 12.5, TEXT_DARK))
        iy += 25

    # Comparison / Key characteristics
    svg_parts.append(rect(410, 360, 360, 215, WHITE, 12, 0.95, PRIMARY_LIGHT, 1.5))
    svg_parts.append(rect(410, 360, 360, 36, PRIMARY, "12 12 0 0"))
    svg_parts.append(text(590, 385, "Общие черты и различия", 15, WHITE, "bold", "middle"))

    comparisons = [
        "Общее: импровизация, ритмичность",
        "Общее: выражение эмоций",
        "Общее: африканские корни",
        "Различие: джаз — свинг и синкопы",
        "Различие: рок — прямая бит-пульсация",
        "Различие: джаз — акустический звук",
        "Различие: рок — электронное звучание",
        "Оба жанра — мировое влияние"
    ]
    cy = 412
    for c in comparisons:
        svg_parts.append(circle(428, cy - 4, 3, PRIMARY))
        svg_parts.append(text(438, cy, c, 12.5, TEXT_DARK))
        cy += 23

    # Bottom decoration
    svg_parts.append(music_note(770, 565, 0.7, "#C4B5FD"))
    svg_parts.append(music_note(20, 575, 0.6, PRIMARY_LIGHT))

    svg_parts.append(svg_footer())
    return "".join(svg_parts)


# ========== MAIN ==========
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    generators = [
        (1, lesson1),
        (2, lesson2),
        (3, lesson3),
        (4, lesson4),
        (5, lesson5),
        (6, lesson6),
    ]

    results = []
    for num, gen_func in generators:
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
        content = gen_func()

        # Write file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        # Validate with xml.etree.ElementTree
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            valid = True
            error_msg = None
        except ET.ParseError as e:
            valid = False
            error_msg = str(e)

        file_size = os.path.getsize(filepath)
        results.append({
            "lesson": num,
            "path": filepath,
            "valid": valid,
            "error": error_msg,
            "size": file_size
        })

    # Print report
    print("=" * 60)
    print("SVG Generation Report — Grade 7 Music")
    print("=" * 60)
    all_valid = True
    for r in results:
        status = "✓ VALID" if r["valid"] else f"✗ INVALID: {r['error']}"
        print(f"  Lesson {r['lesson']}: {r['path']}")
        print(f"    Status: {status}")
        print(f"    Size: {r['size']:,} bytes")
        if not r["valid"]:
            all_valid = False
    print("=" * 60)
    if all_valid:
        print("All 6 SVG files generated and validated successfully!")
    else:
        print("ERROR: Some SVG files failed validation!")
    print("=" * 60)


if __name__ == "__main__":
    main()
