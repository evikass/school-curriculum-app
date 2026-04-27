#!/usr/bin/env python3
"""Generate Grade 8 Law (Право) SVG educational images - 7 lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/law"
W, H = 800, 600

# Color scheme - slate/blue-gray
PRIMARY = "#475569"
PRIMARY_LIGHT = "#64748b"
PRIMARY_DARK = "#334155"
ACCENT = "#3b82f6"
ACCENT_LIGHT = "#93c5fd"
ACCENT2 = "#8b5cf6"
ACCENT2_LIGHT = "#c4b5fd"
BG = "#f8fafc"
BG2 = "#f1f5f9"
WHITE = "#ffffff"
DARK = "#1e293b"
TEXT = "#1e293b"
TEXT_LIGHT = "#64748b"
BORDER = "#cbd5e1"
SUCCESS = "#10b981"
WARNING = "#f59e0b"
DANGER = "#ef4444"
ORANGE = "#f97316"


def escape(text):
    """Escape XML special characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def svg_header():
    """Return SVG root with namespace."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'''


def svg_footer():
    return "</svg>"


def rect(x, y, w, h, fill, rx=8, stroke=None, stroke_width=1, opacity=1.0):
    """Draw a rounded rectangle."""
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" opacity="{opacity}"'
    if stroke:
        s += f' stroke="{stroke}" stroke-width="{stroke_width}"'
    s += '/>'
    return s


def circle(cx, cy, r, fill, stroke=None, stroke_width=1, opacity=1.0):
    """Draw a circle."""
    s = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" opacity="{opacity}"'
    if stroke:
        s += f' stroke="{stroke}" stroke-width="{stroke_width}"'
    s += '/>'
    return s


def text(x, y, content, size=14, fill=TEXT, anchor="middle", weight="normal", family="sans-serif"):
    """Draw text."""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" font-family="{family}">{escape(content)}</text>'


def line(x1, y1, x2, y2, stroke=BORDER, width=1, dash=None):
    """Draw a line."""
    s = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{width}"'
    if dash:
        s += f' stroke-dasharray="{dash}"'
    s += '/>'
    return s


def arrow_down(x, y1, y2, stroke=PRIMARY, width=2):
    """Draw a downward arrow."""
    s = line(x, y1, x, y2, stroke, width)
    s += f'<polygon points="{x-5},{y2-8} {x+5},{y2-8} {x},{y2}" fill="{stroke}"/>'
    return s


def arrow_right(x1, y, x2, stroke=PRIMARY, width=2):
    """Draw a right arrow."""
    s = line(x1, y, x2, y, stroke, width)
    s += f'<polygon points="{x2-8},{y-5} {x2-8},{y+5} {x2},{y}" fill="{stroke}"/>'
    return s


def rounded_box(x, y, w, h, fill, stroke=None, stroke_width=1.5, rx=10):
    """Colored rounded box with optional border."""
    s = rect(x, y, w, h, fill, rx, stroke, stroke_width)
    return s


def header_bar(title, subtitle=""):
    """Draw the header bar with title."""
    parts = []
    # Gradient background
    parts.append(f'<defs><linearGradient id="headerGrad" x1="0" y1="0" x2="1" y2="0">')
    parts.append(f'  <stop offset="0%" stop-color="{PRIMARY_DARK}"/>')
    parts.append(f'  <stop offset="100%" stop-color="{PRIMARY}"/>')
    parts.append(f'</linearGradient></defs>')
    parts.append(rect(0, 0, W, 70, "url(#headerGrad)", rx=0))
    # Title
    parts.append(text(W // 2, 35, title, 22, WHITE, weight="bold"))
    if subtitle:
        parts.append(text(W // 2, 55, subtitle, 12, ACCENT_LIGHT, weight="normal"))
    # Lesson badge
    parts.append(rect(15, 15, 90, 28, ACCENT, rx=14))
    parts.append(text(60, 34, "8 класс", 12, WHITE, weight="bold"))
    # Subject badge
    parts.append(rect(W - 100, 15, 85, 28, ACCENT2, rx=14))
    parts.append(text(W - 57, 34, "Право", 12, WHITE, weight="bold"))
    return "\n".join(parts)


def footer_bar():
    """Draw footer with subject info."""
    parts = []
    parts.append(rect(0, H - 35, W, 35, PRIMARY_DARK, rx=0))
    parts.append(text(W // 2, H - 14, "Право · 8 класс · Образовательный курс", 11, TEXT_LIGHT))
    return "\n".join(parts)


def info_card(x, y, w, h, title, items, color=ACCENT, title_size=13, item_size=11):
    """Draw an info card with title and bullet items."""
    parts = []
    # Card background
    parts.append(rounded_box(x, y, w, h, WHITE, BORDER, 1, 10))
    # Color stripe on top
    parts.append(rect(x, y, w, 5, color, rx=0))
    parts.append(rect(x, y, 10, 5, color, rx=0))
    # Title
    parts.append(text(x + w // 2, y + 24, title, title_size, color, weight="bold"))
    # Items
    ty = y + 44
    for item in items:
        parts.append(circle(x + 16, ty - 4, 3, color))
        parts.append(text(x + 26, ty, item, item_size, TEXT, anchor="start"))
        ty += 18
    return "\n".join(parts)


def generate_lesson1():
    """Конституция — основной закон государства."""
    parts = [svg_header()]
    parts.append(header_bar("Конституция — основной закон государства", "Структура, принципы и значение"))
    parts.append(footer_bar())

    # Background
    parts.append(rect(0, 70, W, H - 105, BG, rx=0))

    # Left: Hierarchy pyramid
    parts.append(text(200, 100, "Иерархия законов", 15, PRIMARY, weight="bold"))

    # Pyramid levels
    pyramid_data = [
        ("Конституция РФ", ACCENT2, 220, 120, 160, 38),
        ("Федеральные\nконституционные законы", ACCENT, 195, 168, 210, 38),
        ("Федеральные законы", PRIMARY, 170, 216, 260, 38),
        ("Подзаконные акты", PRIMARY_LIGHT, 145, 264, 310, 38),
        ("Акты органов\nместного самоуправления", TEXT_LIGHT, 120, 312, 360, 38),
    ]
    for label, color, x, y, w, h in pyramid_data:
        parts.append(rounded_box(x, y, w, h, color, WHITE, 1, 6))
        lines = label.split("\n")
        for i, ln in enumerate(lines):
            parts.append(text(x + w // 2, y + h // 2 - (len(lines) - 1) * 8 + i * 16, ln, 11, WHITE, weight="bold"))

    # Arrows between levels
    parts.append(arrow_down(300, 158, 166, PRIMARY_LIGHT))
    parts.append(arrow_down(300, 206, 214, PRIMARY_LIGHT))
    parts.append(arrow_down(300, 254, 262, PRIMARY_LIGHT))
    parts.append(arrow_down(300, 302, 310, PRIMARY_LIGHT))

    # Right side: Structure of Constitution
    parts.append(text(600, 100, "Структура Конституции РФ", 15, PRIMARY, weight="bold"))

    structure_items = [
        ("Преамбула", "Введение, цели народа", ACCENT2),
        ("Раздел I", "9 глав, 137 статей", ACCENT),
        ("Глава 1", "Основы конституционного строя", PRIMARY),
        ("Глава 2", "Права и свободы человека", SUCCESS),
        ("Раздел II", "Заключительные положения", PRIMARY_LIGHT),
    ]
    sy = 115
    for title, desc, color in structure_items:
        parts.append(rounded_box(470, sy, 260, 40, WHITE, color, 1.5, 8))
        parts.append(rect(470, sy, 6, 40, color, rx=0))
        parts.append(text(490, sy + 16, title, 12, color, anchor="start", weight="bold"))
        parts.append(text(490, sy + 32, desc, 10, TEXT_LIGHT, anchor="start"))
        sy += 48

    # Bottom: Key principles
    parts.append(text(W // 2, 375, "Основные принципы Конституции РФ", 15, PRIMARY, weight="bold"))

    principles = [
        ("Народовластие", ACCENT),
        ("Федерализм", ACCENT2),
        ("Разделение\nвластей", PRIMARY),
        ("Правовое\nгосударство", SUCCESS),
        ("Многообразие\nформ\nсобственности", WARNING),
    ]
    px = 70
    for label, color in principles:
        parts.append(rounded_box(px, 390, 130, 60, color, WHITE, 1, 8))
        lines = label.split("\n")
        for i, ln in enumerate(lines):
            parts.append(text(px + 65, 413 - (len(lines) - 1) * 8 + i * 14, ln, 11, WHITE, weight="bold"))
        # Connecting line to center
        parts.append(line(px + 65, 450, 400, 480, BORDER, 1, "3,3"))
        px += 140

    # Bottom note
    parts.append(rounded_box(100, 480, 600, 50, BG2, PRIMARY, 1, 8))
    parts.append(text(400, 500, "Конституция принята всенародным голосованием 12 декабря 1993 года", 12, PRIMARY, weight="bold"))
    parts.append(text(400, 518, "Высшая юридическая сила, прямое действие, применяется на всей территории РФ", 10, TEXT_LIGHT))

    parts.append(svg_footer())
    return "\n".join(parts)


def generate_lesson2():
    """Права и свободы человека."""
    parts = [svg_header()]
    parts.append(header_bar("Права и свободы человека", "Всеобщая декларация прав человека, категории прав"))
    parts.append(footer_bar())

    parts.append(rect(0, 70, W, H - 105, BG, rx=0))

    # Top: Universal Declaration info
    parts.append(rounded_box(20, 80, 760, 60, WHITE, ACCENT, 1.5, 10))
    parts.append(rect(20, 80, 6, 60, ACCENT, rx=0))
    parts.append(text(400, 103, "Всеобщая декларация прав человека (1948 г.)", 14, ACCENT, weight="bold"))
    parts.append(text(400, 122, "Принята Генеральной Ассамблеей ООН · 30 статей · Основа международного права прав человека", 11, TEXT_LIGHT))

    # Categories of rights - 4 cards
    categories = [
        ("Личные (гражданские)\nправа", [
            "Право на жизнь",
            "Свобода и личная\nнеприкосновенность",
            "Свобода совести",
            "Неприкосновенность\nжилища"
        ], DANGER),
        ("Политические\nправа", [
            "Свобода слова",
            "Право на собрания",
            "Избирательное право",
            "Свобода союзов"
        ], ACCENT),
        ("Социально-\nэкономические права", [
            "Право на труд",
            "Право на отдых",
            "Право на образование",
            "Право на жилище"
        ], SUCCESS),
        ("Культурные\nправа", [
            "Свобода творчества",
            "Право на участие\nв культ. жизни",
            "Право на образование",
            "Академическая\nсвобода"
        ], ACCENT2),
    ]

    cx = 20
    for title, items, color in categories:
        parts.append(rounded_box(cx, 150, 185, 220, WHITE, BORDER, 1, 8))
        # Color header
        parts.append(rect(cx, 150, 185, 45, color, rx=8))
        parts.append(rect(cx, 180, 185, 15, color, rx=0))
        lines = title.split("\n")
        for i, ln in enumerate(lines):
            parts.append(text(cx + 92, 170 - (len(lines) - 1) * 8 + i * 14, ln, 11, WHITE, weight="bold"))

        iy = 210
        for item in items:
            ilines = item.split("\n")
            parts.append(circle(cx + 14, iy - 3, 3, color))
            for j, il in enumerate(ilines):
                parts.append(text(cx + 24, iy + j * 12, il, 9, TEXT, anchor="start"))
            iy += 14 * len(ilines) + 8
        cx += 192

    # Bottom: Key articles
    parts.append(rounded_box(20, 385, 380, 145, WHITE, PRIMARY, 1, 8))
    parts.append(rect(20, 385, 380, 5, PRIMARY, rx=0))
    parts.append(text(210, 406, "Ключевые статьи Конституции РФ", 13, PRIMARY, weight="bold"))

    articles = [
        "Ст. 17 — Права и свободы принадлежат от рождения",
        "Ст. 18 — Непосредственное действие прав",
        "Ст. 19 — Равенство перед законом",
        "Ст. 20 — Право на жизнь",
        "Ст. 21 — Достоинство личности охраняется государством",
        "Ст. 22 — Свобода и личная неприкосновенность",
    ]
    ay = 424
    for a in articles:
        parts.append(text(35, ay, a, 10, TEXT, anchor="start"))
        ay += 17

    # Right bottom: Obligations
    parts.append(rounded_box(410, 385, 370, 145, WHITE, ACCENT2, 1, 8))
    parts.append(rect(410, 385, 370, 5, ACCENT2, rx=0))
    parts.append(text(595, 406, "Обязанности человека и гражданина", 13, ACCENT2, weight="bold"))

    obligations = [
        "Соблюдать Конституцию и законы",
        "Платить законно установленные налоги",
        "Сохранять природу и окружающую среду",
        "Защищать Отечество",
        "Получать основное общее образование",
        "Заботиться о нетрудоспособных родителях",
    ]
    oy = 424
    for o in obligations:
        parts.append(circle(424, oy - 3, 3, ACCENT2))
        parts.append(text(434, oy, o, 10, TEXT, anchor="start"))
        oy += 17

    parts.append(svg_footer())
    return "\n".join(parts)


def generate_lesson3():
    """Гражданство РФ."""
    parts = [svg_header()]
    parts.append(header_bar("Гражданство РФ", "Приобретение, права и обязанности гражданина"))
    parts.append(footer_bar())

    parts.append(rect(0, 70, W, H - 105, BG, rx=0))

    # Definition box
    parts.append(rounded_box(20, 80, 760, 50, WHITE, ACCENT, 1.5, 10))
    parts.append(rect(20, 80, 6, 50, ACCENT, rx=0))
    parts.append(text(400, 100, "Гражданство — устойчивая правовая связь лица с государством", 14, ACCENT, weight="bold"))
    parts.append(text(400, 118, "Выражается в совокупности взаимных прав, обязанностей и ответственности", 11, TEXT_LIGHT))

    # Left: Ways to acquire citizenship
    parts.append(text(210, 152, "Основания приобретения гражданства", 14, PRIMARY, weight="bold"))

    acquire_data = [
        ("По рождению", "Филиация —自动\nприобретение при рождении", ACCENT2, 170),
        ("Приём в гражданство", "Натурализация — общая\nи упрощённая процедура", ACCENT, 225),
        ("Восстановление", "Для бывших граждан РФ,\nвозвратившихся в РФ", PRIMARY, 280),
        ("Иные основания", "По международному\nдоговору, оптация", PRIMARY_LIGHT, 335),
    ]
    for title, desc, color, y in acquire_data:
        parts.append(rounded_box(20, y, 380, 48, WHITE, color, 1, 8))
        parts.append(rect(20, y, 5, 48, color, rx=0))
        parts.append(text(40, y + 17, title, 12, color, anchor="start", weight="bold"))
        dlines = desc.split("\n")
        for i, dl in enumerate(dlines):
            parts.append(text(40, y + 32 + i * 12, dl, 9, TEXT_LIGHT, anchor="start"))

    # Right: Requirements for naturalization
    parts.append(text(610, 152, "Условия приёма в гражданство", 14, PRIMARY, weight="bold"))

    requirements = [
        "Непрерывное проживание 5 лет",
        "Законный источник средств",
        "Владение русским языком",
        "Отказ от иного гражданства",
        "Соблюдение Конституции РФ",
    ]
    ry = 168
    for r in requirements:
        parts.append(rounded_box(420, ry, 360, 32, WHITE, BORDER, 1, 6))
        parts.append(circle(438, ry + 13, 7, ACCENT))
        parts.append(text(438, ry + 17, str(requirements.index(r) + 1), 9, WHITE, weight="bold"))
        parts.append(text(455, ry + 20, r, 11, TEXT, anchor="start"))
        ry += 38

    # Bottom: Rights and duties comparison
    parts.append(text(210, 398, "Права гражданина РФ", 13, SUCCESS, weight="bold"))
    parts.append(text(600, 398, "Обязанности гражданина РФ", 13, DANGER, weight="bold"))

    # Rights column
    rights = [
        "Избирать и быть избранным",
        "Доступ к гос. службе",
        "Свободно передвигаться",
        "Создавать общественные объединения",
    ]
    rights_y = 412
    for r in rights:
        parts.append(circle(38, rights_y + 5, 3, SUCCESS))
        parts.append(text(48, rights_y + 9, r, 10, TEXT, anchor="start"))
        rights_y += 20

    # Duties column
    duties = [
        "Соблюдать законы РФ",
        "Платить налоги и сборы",
        "Защищать Отечество",
        "Заботиться о памятниках истории",
    ]
    duties_y = 412
    for d in duties:
        parts.append(circle(438, duties_y + 5, 3, DANGER))
        parts.append(text(448, duties_y + 9, d, 10, TEXT, anchor="start"))
        duties_y += 20

    # Divider
    parts.append(line(400, 390, 400, 530, BORDER, 1, "4,4"))

    # Key principle box
    parts.append(rounded_box(20, 505, 760, 45, BG2, ACCENT2, 1, 8))
    parts.append(text(400, 525, "Принцип единого гражданства: гражданин РФ не может быть лишён гражданства", 12, ACCENT2, weight="bold"))
    parts.append(text(400, 540, "или права изменить его (ст. 6 Конституции РФ)", 10, TEXT_LIGHT))

    parts.append(svg_footer())
    return "\n".join(parts)


def generate_lesson4():
    """Конвенция о правах ребёнка."""
    parts = [svg_header()]
    parts.append(header_bar("Конвенция о правах ребёнка", "Ключевые статьи, защита прав детей"))
    parts.append(footer_bar())

    parts.append(rect(0, 70, W, H - 105, BG, rx=0))

    # Top banner
    parts.append(rounded_box(20, 80, 760, 55, WHITE, ACCENT, 1.5, 10))
    parts.append(rect(20, 80, 6, 55, ACCENT, rx=0))
    parts.append(text(400, 100, "Конвенция ООН о правах ребёнка (1989 г.)", 15, ACCENT, weight="bold"))
    parts.append(text(400, 118, "Ратифицирована РФ в 1990 г. · Ребёнок — лицо до 18 лет · 54 статьи", 11, TEXT_LIGHT))

    # Key principles - 4 circles
    principles = [
        ("Недискриминация", "Равные права\nдля всех детей", ACCENT2),
        ("Наилучшие\nинтересы", "Приоритет\nинтересов ребёнка", ACCENT),
        ("Право на жизнь\nи развитие", "Гарантия\nбезопасности", SUCCESS),
        ("Уважение\nмнений", "Участие ребёнка\nв решениях", WARNING),
    ]
    cx = 112
    for title, desc, color in principles:
        # Outer circle
        parts.append(circle(cx, 200, 50, WHITE, color, 2))
        # Inner filled circle
        parts.append(circle(cx, 200, 38, color, opacity=0.15))
        tlines = title.split("\n")
        for i, tl in enumerate(tlines):
            parts.append(text(cx, 195 - (len(tlines) - 1) * 7 + i * 14, tl, 10, color, weight="bold"))
        dlines = desc.split("\n")
        for i, dl in enumerate(dlines):
            parts.append(text(cx, 220 + i * 11, dl, 8, TEXT_LIGHT))
        cx += 170

    # Main rights of the child
    parts.append(text(400, 278, "Основные права ребёнка по Конвенции", 14, PRIMARY, weight="bold"))

    rights_boxes = [
        ("Право на имя\nи гражданство", "Ст. 7", ACCENT2, 20, 295),
        ("Право на\nобразование", "Ст. 28", ACCENT, 200, 295),
        ("Защита от\nнасилия", "Ст. 19", DANGER, 380, 295),
        ("Право на\nотдых и досуг", "Ст. 31", SUCCESS, 560, 295),
    ]
    for title, article, color, x, y in rights_boxes:
        parts.append(rounded_box(x, y, 170, 58, WHITE, color, 1, 8))
        parts.append(rect(x, y, 5, 58, color, rx=0))
        tlines = title.split("\n")
        for i, tl in enumerate(tlines):
            parts.append(text(x + 90, y + 20 - (len(tlines) - 1) * 7 + i * 14, tl, 11, TEXT, weight="bold"))
        parts.append(text(x + 90, y + 48, article, 10, color, weight="bold"))

    # Protection mechanisms
    parts.append(text(210, 378, "Защита прав ребёнка в РФ", 14, PRIMARY, weight="bold"))

    mechs = [
        ("Уполномоченный\nпо правам ребёнка", ACCENT2, 20, 395),
        ("Органы опеки\nи попечительства", ACCENT, 200, 395),
        ("Комиссии по делам\nнесовершеннолетних", PRIMARY, 380, 395),
        ("Социальная\nзащита", SUCCESS, 560, 395),
    ]
    for title, color, x, y in mechs:
        parts.append(rounded_box(x, y, 170, 50, color, WHITE, 1, 8))
        tlines = title.split("\n")
        for i, tl in enumerate(tlines):
            parts.append(text(x + 85, y + 22 - (len(tlines) - 1) * 7 + i * 14, tl, 10, WHITE, weight="bold"))

    # Bottom note
    parts.append(rounded_box(20, 460, 760, 80, BG2, PRIMARY, 1, 8))
    parts.append(text(400, 483, "Федеральный закон № 124-ФЗ «Об основных гарантиях прав ребёнка в РФ»", 12, PRIMARY, weight="bold"))
    parts.append(text(400, 503, "Государство признаёт детство важным этапом жизни человека и гарантирует", 10, TEXT))
    parts.append(text(400, 518, "права детей на образование, охрану здоровья, отдых и труд, социальную защиту", 10, TEXT))

    parts.append(svg_footer())
    return "\n".join(parts)


def generate_lesson5():
    """Ответственность несовершеннолетних."""
    parts = [svg_header()]
    parts.append(header_bar("Ответственность несовершеннолетних", "Возраст ответственности, виды ответственности"))
    parts.append(footer_bar())

    parts.append(rect(0, 70, W, H - 105, BG, rx=0))

    # Age timeline
    parts.append(text(400, 100, "Возраст привлечения к ответственности", 15, PRIMARY, weight="bold"))

    # Timeline bar
    parts.append(rect(80, 125, 640, 4, PRIMARY_LIGHT, rx=2))

    ages = [
        (14, "14 лет", "Уголовная\nответственность\n(тяжкие преступления)", DANGER),
        (16, "16 лет", "Полная уголовная\nи административная\nответственность", WARNING),
        (18, "18 лет", "Полная\nгражданско-правовая\nответственность", ACCENT),
    ]
    for age, label, desc, color in ages:
        x = 80 + (age - 14) * 320
        parts.append(circle(x, 127, 8, color))
        parts.append(text(x, 117, label, 12, color, weight="bold"))
        parts.append(text(x, 150, f"С {age} лет", 11, color, weight="bold"))
        dlines = desc.split("\n")
        for i, dl in enumerate(dlines):
            parts.append(text(x, 166 + i * 13, dl, 9, TEXT_LIGHT))

    # Types of responsibility
    parts.append(text(400, 218, "Виды ответственности несовершеннолетних", 14, PRIMARY, weight="bold"))

    resp_data = [
        ("Уголовная", [
            "С 14 лет — за тяжкие преступления",
            "С 16 лет — за все преступления",
            "Макс. срок — 10 лет лишения свободы",
            "Применяются принудительные меры",
        ], DANGER),
        ("Административная", [
            "С 16 лет",
            "Штраф, предупреждение",
            "Доставление, задержание",
            "Дело рассматривает КДН и ЗП",
        ], WARNING),
        ("Гражданско-правовая", [
            "Возмещение вреда",
            "С 14 лет — самостоятельная",
            "До 14 лет — отвечают родители",
            "Моральный вред",
        ], ACCENT),
        ("Дисциплинарная", [
            "В рамках трудовых отношений",
            "С 16 лет — по ТК РФ",
            "Замечание, выговор, увольнение",
            "Для школьников — по уставу",
        ], ACCENT2),
    ]

    rx = 20
    for title, items, color in resp_data:
        parts.append(rounded_box(rx, 235, 185, 190, WHITE, color, 1, 8))
        parts.append(rect(rx, 235, 185, 35, color, rx=8))
        parts.append(rect(rx, 260, 185, 10, color, rx=0))
        parts.append(text(rx + 92, 258, title, 12, WHITE, weight="bold"))
        iy = 282
        for item in items:
            parts.append(circle(rx + 14, iy - 3, 3, color))
            parts.append(text(rx + 24, iy, item, 9, TEXT, anchor="start"))
            iy += 22
        rx += 192

    # Bottom: Key principles
    parts.append(rounded_box(20, 440, 760, 95, BG2, PRIMARY, 1, 8))
    parts.append(text(400, 463, "Принципы ответственности несовершеннолетних", 13, PRIMARY, weight="bold"))

    bottom_items = [
        "Гуманизм — воспитание, а не наказание — главная цель",
        "Индивидуализация — учёт возраста, личности, обстоятельств",
        "Участие родителей и законных представителей в процессе",
        "Возможность исправления и реабилитации",
    ]
    by = 482
    for bi in bottom_items:
        parts.append(circle(40, by - 3, 3, ACCENT))
        parts.append(text(52, by, bi, 10, TEXT, anchor="start"))
        by += 16

    parts.append(svg_footer())
    return "\n".join(parts)


def generate_lesson6():
    """Виды юридической ответственности."""
    parts = [svg_header()]
    parts.append(header_bar("Виды юридической ответственности", "Уголовная, административная, гражданская, дисциплинарная"))
    parts.append(footer_bar())

    parts.append(rect(0, 70, W, H - 105, BG, rx=0))

    # Central concept
    parts.append(circle(400, 140, 45, ACCENT))
    parts.append(text(400, 137, "Юридическая", 11, WHITE, weight="bold"))
    parts.append(text(400, 152, "ответственность", 11, WHITE, weight="bold"))

    # Branches radiating from center
    branches = [
        ("Уголовная", DANGER, 130, 240, [
            "За преступления (УК РФ)",
            "Лишение свободы",
            "Штраф, исправ. работы",
            "Лишение права занимать\nдолжности",
            "Самый строгий вид",
        ]),
        ("Административная", WARNING, 340, 240, [
            "За правонарушения (КоАП РФ)",
            "Предупреждение",
            "Административный штраф",
            "Конфискация орудия",
            "Административный арест\nдо 15 суток",
        ]),
        ("Гражданско-\nправовая", ACCENT, 550, 240, [
            "За деликты (ГК РФ)",
            "Возмещение убытков",
            "Компенсация мор. вреда",
            "Возврат имущества",
            "Восстановление положения",
        ]),
        ("Дисциплинарная", ACCENT2, 200, 410, [
            "За дисциплин. проступки (ТК РФ)",
            "Замечание",
            "Выговор",
            "Строгий выговор",
            "Увольнение",
        ]),
        ("Материальная", PRIMARY, 500, 410, [
            "За имуществ. ущерб (ТК РФ)",
            "Полная материальная",
            "Ограниченная материальная",
            "Возмещение в пределах\nсреднего заработка",
        ]),
    ]

    for title, color, bx, by, items in branches:
        # Connection line from center
        parts.append(line(400, 140, bx + 90, by, color, 2))
        # Card
        parts.append(rounded_box(bx, by, 185, 155, WHITE, color, 1.5, 8))
        parts.append(rect(bx, by, 185, 30, color, rx=8))
        parts.append(rect(bx, by + 20, 185, 10, color, rx=0))
        tlines = title.split("\n")
        for i, tl in enumerate(tlines):
            parts.append(text(bx + 92, by + 18 - (len(tlines) - 1) * 7 + i * 13, tl, 11, WHITE, weight="bold"))
        iy = by + 42
        for item in items:
            ilines = item.split("\n")
            parts.append(circle(bx + 12, iy - 3, 2, color))
            for j, il in enumerate(ilines):
                parts.append(text(bx + 20, iy + j * 11, il, 8, TEXT, anchor="start"))
            iy += 10 * len(ilines) + 8

    parts.append(svg_footer())
    return "\n".join(parts)


def generate_lesson7():
    """Защита прав граждан."""
    parts = [svg_header()]
    parts.append(header_bar("Защита прав граждан", "Суды, омбудсмен, юридическая помощь"))
    parts.append(footer_bar())

    parts.append(rect(0, 70, W, H - 105, BG, rx=0))

    # Top: Constitutional guarantee
    parts.append(rounded_box(20, 80, 760, 45, WHITE, ACCENT, 1.5, 10))
    parts.append(rect(20, 80, 6, 45, ACCENT, rx=0))
    parts.append(text(400, 100, "Ст. 46 Конституции РФ: каждому гарантируется судебная защита прав и свобод", 13, ACCENT, weight="bold"))
    parts.append(text(400, 117, "Решения и действия органов власти могут быть обжалованы в суд", 10, TEXT_LIGHT))

    # Three main mechanisms
    parts.append(text(400, 150, "Механизмы защиты прав граждан", 15, PRIMARY, weight="bold"))

    # 1. Judicial protection
    parts.append(rounded_box(20, 165, 245, 230, WHITE, DANGER, 1.5, 8))
    parts.append(rect(20, 165, 245, 40, DANGER, rx=8))
    parts.append(rect(20, 195, 245, 10, DANGER, rx=0))
    parts.append(text(142, 190, "Судебная защита", 13, WHITE, weight="bold"))

    court_items = [
        "Конституционный Суд РФ",
        "Верховный Суд РФ",
        "Суды общей юрисдикции",
        "Арбитражные суды",
        "Мировые судьи",
    ]
    cy = 218
    for c in court_items:
        parts.append(circle(38, cy - 3, 3, DANGER))
        parts.append(text(48, cy, c, 10, TEXT, anchor="start"))
        cy += 18

    parts.append(rect(30, 315, 225, 65, BG2, rx=5))
    parts.append(text(142, 332, "Порядок обращения:", 9, DANGER, weight="bold"))
    parts.append(text(142, 348, "1. Исковое заявление", 9, TEXT, anchor="start"))
    parts.append(text(142, 362, "2. Судебное разбирательство", 9, TEXT, anchor="start"))
    parts.append(text(142, 376, "3. Исполнение решения", 9, TEXT, anchor="start"))

    # 2. Ombudsman
    parts.append(rounded_box(278, 165, 245, 230, WHITE, ACCENT2, 1.5, 8))
    parts.append(rect(278, 165, 245, 40, ACCENT2, rx=8))
    parts.append(rect(278, 195, 245, 10, ACCENT2, rx=0))
    parts.append(text(400, 190, "Уполномоченный по правам", 12, WHITE, weight="bold"))

    omb_items = [
        "Уполномоченный по правам\nчеловека в РФ",
        "Уполномоченный по правам\nребёнка в РФ",
        "Уполномоченные в субъектах",
        "Рассмотрение жалоб граждан",
        "Внесение рекомендаций",
    ]
    cy = 218
    for o in omb_items:
        olines = o.split("\n")
        parts.append(circle(296, cy - 3, 3, ACCENT2))
        for i, ol in enumerate(olines):
            parts.append(text(306, cy + i * 12, ol, 9, TEXT, anchor="start"))
        cy += 12 * len(olines) + 6

    parts.append(rect(288, 315, 225, 65, BG2, rx=5))
    parts.append(text(400, 332, "Функции:", 9, ACCENT2, weight="bold"))
    parts.append(text(400, 348, "Защита прав и свобод", 9, TEXT, anchor="start"))
    parts.append(text(400, 362, "Контроль за деятельностью гос. органов", 9, TEXT, anchor="start"))
    parts.append(text(400, 376, "Развитие правового просвещения", 9, TEXT, anchor="start"))

    # 3. Legal aid
    parts.append(rounded_box(535, 165, 245, 230, WHITE, SUCCESS, 1.5, 8))
    parts.append(rect(535, 165, 245, 40, SUCCESS, rx=8))
    parts.append(rect(535, 195, 245, 10, SUCCESS, rx=0))
    parts.append(text(657, 190, "Юридическая помощь", 13, WHITE, weight="bold"))

    aid_items = [
        "Бесплатная юридическая\nпомощь (ФЗ № 324)",
        "Адвокатская помощь",
        "Юридические консультации",
        "Нотариальная помощь",
        "Правовое просвещение",
    ]
    cy = 218
    for a in aid_items:
        alines = a.split("\n")
        parts.append(circle(553, cy - 3, 3, SUCCESS))
        for i, al in enumerate(alines):
            parts.append(text(563, cy + i * 12, al, 9, TEXT, anchor="start"))
        cy += 12 * len(alines) + 6

    parts.append(rect(545, 315, 225, 65, BG2, rx=5))
    parts.append(text(657, 332, "Категории граждан:", 9, SUCCESS, weight="bold"))
    parts.append(text(657, 348, "Малоимущие, инвалиды", 9, TEXT, anchor="start"))
    parts.append(text(657, 362, "Ветераны, дети-сироты", 9, TEXT, anchor="start"))
    parts.append(text(657, 376, "Пенсионеры (по отдельным вопросам)", 9, TEXT, anchor="start"))

    # Bottom: Steps to protect rights
    parts.append(text(400, 420, "Порядок защиты прав гражданина", 14, PRIMARY, weight="bold"))

    steps = [
        ("1", "Нарушение\nправа", DANGER),
        ("2", "Обращение\nв компетентный\nорган", WARNING),
        ("3", "Рассмотрение\nобращения", ACCENT),
        ("4", "Принятие\nрешения", SUCCESS),
        ("5", "Исполнение\nрешения", ACCENT2),
    ]
    sx = 70
    for num, label, color in steps:
        parts.append(rounded_box(sx, 438, 130, 60, color, WHITE, 1, 8))
        parts.append(circle(sx + 65, 455, 10, WHITE))
        parts.append(text(sx + 65, 459, num, 12, color, weight="bold"))
        llines = label.split("\n")
        for i, ll in enumerate(llines):
            parts.append(text(sx + 65, 478 - (len(llines) - 1) * 6 + i * 12, ll, 9, WHITE, weight="bold"))
        # Arrow to next
        if sx < 620:
            parts.append(arrow_right(sx + 132, 468, sx + 148, PRIMARY_LIGHT, 1.5))
        sx += 145

    # Bottom note
    parts.append(rounded_box(20, 510, 760, 40, BG2, PRIMARY, 1, 8))
    parts.append(text(400, 527, "Право на обращение в международные органы по защите прав (ст. 46 ч. 3 Конституции РФ)", 11, PRIMARY, weight="bold"))
    parts.append(text(400, 542, "ЕСПЧ — Европейский суд по правам человека", 9, TEXT_LIGHT))

    parts.append(svg_footer())
    return "\n".join(parts)


def validate_svg(content, filename):
    """Validate SVG as valid XML using ElementTree."""
    try:
        ET.fromstring(content)
        return True, None
    except ET.ParseError as e:
        return False, str(e)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    generators = [
        (1, generate_lesson1),
        (2, generate_lesson2),
        (3, generate_lesson3),
        (4, generate_lesson4),
        (5, generate_lesson5),
        (6, generate_lesson6),
        (7, generate_lesson7),
    ]

    results = []
    for num, gen_func in generators:
        content = gen_func()
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")

        # Validate
        valid, error = validate_svg(content, filepath)
        if not valid:
            print(f"  ❌ VALIDATION FAILED for lesson-{num}.svg: {error}")
            results.append((num, False, error))
            continue

        # Write
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        size = os.path.getsize(filepath)
        print(f"  ✓ lesson-{num}.svg — {size} bytes — valid XML")
        results.append((num, True, f"{size} bytes"))

    print(f"\n{'='*60}")
    print(f"Generated {len([r for r in results if r[1]])} of {len(generators)} SVG files")
    print(f"Output: {OUTPUT_DIR}")
    for num, ok, info in results:
        status = "✓" if ok else "❌"
        print(f"  {status} lesson-{num}.svg — {info}")


if __name__ == "__main__":
    main()
