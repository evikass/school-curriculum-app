#!/usr/bin/env python3
"""Generate 12 educational SVG images for Grade 8 Art (ИЗО) lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/art"

# Color scheme
C_PRIMARY = "#EA580C"
C_DARK = "#9A3412"
C_LIGHT = "#FED7AA"
C_ACCENT = "#C2410C"
C_BG = "#FFFBEB"
C_BG2 = "#FFF7ED"
C_TEXT = "#431407"
C_TEXT2 = "#78350F"
C_GOLD = "#D97706"
C_OLIVE = "#6B7210"
C_TERRACOTTA = "#B45309"
C_BLUE = "#1E40AF"
C_GREEN = "#166534"
C_PURPLE = "#6B21A8"
C_RED = "#B91C1C"
C_WARM_GRAY = "#78716C"


def escape_xml(text):
    """Escape special XML characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def svg_header():
    """Return common SVG header attributes and defs."""
    return {
        "xmlns": "http://www.w3.org/2000/svg",
        "width": "800",
        "height": "600",
        "viewBox": "0 0 800 600",
    }


def add_gradient_defs(svg):
    """Add common gradient definitions."""
    defs = ET.SubElement(svg, "defs")

    # Background gradient
    grad = ET.SubElement(defs, "linearGradient", id="bgGrad", x1="0%", y1="0%", x2="0%", y2="100%")
    ET.SubElement(grad, "stop", offset="0%", style="stop-color:#FFFBEB;stop-opacity:1")
    ET.SubElement(grad, "stop", offset="100%", style="stop-color:#FED7AA;stop-opacity:1")

    # Title gradient
    grad2 = ET.SubElement(defs, "linearGradient", id="titleGrad", x1="0%", y1="0%", x2="100%", y2="0%")
    ET.SubElement(grad2, "stop", offset="0%", style="stop-color:#9A3412;stop-opacity:1")
    ET.SubElement(grad2, "stop", offset="100%", style="stop-color:#EA580C;stop-opacity:1")

    # Accent gradient
    grad3 = ET.SubElement(defs, "linearGradient", id="accentGrad", x1="0%", y1="0%", x2="100%", y2="100%")
    ET.SubElement(grad3, "stop", offset="0%", style="stop-color:#EA580C;stop-opacity:1")
    ET.SubElement(grad3, "stop", offset="100%", style="stop-color:#D97706;stop-opacity:1")

    # Gold gradient
    grad4 = ET.SubElement(defs, "linearGradient", id="goldGrad", x1="0%", y1="0%", x2="100%", y2="0%")
    ET.SubElement(grad4, "stop", offset="0%", style="stop-color:#D97706;stop-opacity:1")
    ET.SubElement(grad4, "stop", offset="100%", style="stop-color:#F59E0B;stop-opacity:1")

    # Shadow filter
    filt = ET.SubElement(defs, "filter", id="shadow", x="-5%", y="-5%", width="110%", height="110%")
    ET.SubElement(filt, "feDropShadow", dx="2", dy="2", stdDeviation="3", floodColor="#9A3412", floodOpacity="0.2")

    filt2 = ET.SubElement(defs, "filter", id="softShadow", x="-5%", y="-5%", width="110%", height="110%")
    ET.SubElement(filt2, "feDropShadow", dx="1", dy="1", stdDeviation="2", floodColor="#000", floodOpacity="0.15")


def add_background(svg):
    """Add standard background."""
    ET.SubElement(svg, "rect", width="800", height="600", fill="url(#bgGrad)")
    # Decorative border
    ET.SubElement(svg, "rect", x="8", y="8", width="784", height="584",
                  fill="none", stroke=C_PRIMARY, strokeWidth="2", rx="8")
    ET.SubElement(svg, "rect", x="14", y="14", width="772", height="572",
                  fill="none", stroke=C_GOLD, strokeWidth="1", rx="6", strokeDasharray="8,4")


def add_title(svg, text, subtitle=""):
    """Add standard title bar."""
    # Title background
    ET.SubElement(svg, "rect", x="20", y="16", width="760", height="60",
                  fill="url(#titleGrad)", rx="6", filter="url(#shadow)")
    # Title text
    t = ET.SubElement(svg, "text", x="400", y="48", fill="white",
                      fontSize="22", fontWeight="bold", textAnchor="middle",
                      fontFamily="serif")
    t.text = escape_xml(text)
    if subtitle:
        s = ET.SubElement(svg, "text", x="400", y="68", fill=C_LIGHT,
                          fontSize="12", textAnchor="middle", fontFamily="sans-serif")
        s.text = escape_xml(subtitle)
    # Decorative brush stroke left
    ET.SubElement(svg, "circle", cx="35", cy="46", r="6", fill=C_GOLD, opacity="0.6")
    ET.SubElement(svg, "circle", cx="765", cy="46", r="6", fill=C_GOLD, opacity="0.6")


def add_info_box(svg, x, y, w, h, title, items, color=C_PRIMARY, title_color="white"):
    """Add a colored info box with title and bullet items."""
    # Box
    ET.SubElement(svg, "rect", x=str(x), y=str(y), width=str(w), height=str(h),
                  fill="white", stroke=color, strokeWidth="1.5", rx="6", filter="url(#softShadow)")
    # Title bar
    ET.SubElement(svg, "rect", x=str(x), y=str(y), width=str(w), height="26",
                  fill=color, rx="6")
    ET.SubElement(svg, "rect", x=str(x), y=str(y + 18), width=str(w), height="8",
                  fill=color)
    # Title text
    tt = ET.SubElement(svg, "text", x=str(x + w // 2), y=str(y + 18),
                       fill=title_color, fontSize="12", fontWeight="bold",
                       textAnchor="middle", fontFamily="sans-serif")
    tt.text = escape_xml(title)
    # Items
    for i, item in enumerate(items):
        ty = y + 38 + i * 17
        if ty + 10 > y + h:
            break
        # Bullet
        ET.SubElement(svg, "circle", cx=str(x + 14), cy=str(ty - 4), r="3", fill=color, opacity="0.6")
        it = ET.SubElement(svg, "text", x=str(x + 22), y=str(ty),
                           fill=C_TEXT2, fontSize="11", fontFamily="sans-serif")
        it.text = escape_xml(item)


def add_palette_icon(svg, x, y, size=30):
    """Add a small painter's palette icon."""
    # Palette shape
    ET.SubElement(svg, "ellipse", cx=str(x), cy=str(y), rx=str(size), ry=str(size * 0.7),
                  fill=C_TERRACOTTA, opacity="0.8")
    # Color dots
    for dx, dy, c in [(-8, -3, "#EF4444"), (0, -7, "#3B82F6"), (8, -3, "#EAB308"),
                       (-5, 5, "#22C55E"), (5, 5, "#8B5CF6")]:
        ET.SubElement(svg, "circle", cx=str(x + dx), cy=str(y + dy), r="3", fill=c)


def add_brush_stroke(svg, x1, y1, x2, y2, color=C_PRIMARY, width=3):
    """Add a decorative brush stroke line."""
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2 - 5
    path = f"M{x1},{y1} Q{mid_x},{mid_y} {x2},{y2}"
    ET.SubElement(svg, "path", d=path, fill="none", stroke=color,
                  strokeWidth=str(width), strokeLinecap="round", opacity="0.5")


def add_lesson_number(svg, number):
    """Add lesson number badge."""
    ET.SubElement(svg, "circle", cx="52", cy="100", r="18",
                  fill=C_PRIMARY, filter="url(#softShadow)")
    t = ET.SubElement(svg, "text", x="52", y="106", fill="white",
                      fontSize="16", fontWeight="bold", textAnchor="middle",
                      fontFamily="sans-serif")
    t.text = str(number)


def add_footer(svg, text="ИЗО · 8 класс"):
    """Add decorative footer."""
    ET.SubElement(svg, "rect", x="20", y="570", width="760", height="22",
                  fill=C_DARK, rx="4", opacity="0.8")
    t = ET.SubElement(svg, "text", x="400", y="585", fill=C_LIGHT,
                      fontSize="11", textAnchor="middle", fontFamily="sans-serif")
    t.text = escape_xml(text)
    # Small palette in footer
    add_palette_icon(svg, 48, 581, 8)


# =====================================================================
# LESSON 1: Искусство Древней Руси
# =====================================================================
def lesson_1():
    svg = ET.Element("svg", **svg_header())
    add_gradient_defs(svg)
    add_background(svg)
    add_title(svg, "Искусство Древней Руси", "Архитектура, фрески, ремёсла X–XVII вв.")
    add_lesson_number(svg, 1)

    # Church silhouette (stylized onion dome)
    ET.SubElement(svg, "rect", x="580", y="200", width="80", height="120", fill=C_TERRACOTTA, opacity="0.3")
    ET.SubElement(svg, "polygon", points="620,130 590,200 650,200", fill=C_TERRACOTTA, opacity="0.3")
    # Onion dome
    ET.SubElement(svg, "path", d="M600,130 Q620,90 640,130", fill=C_GOLD, opacity="0.4")
    # Cross
    ET.SubElement(svg, "rect", x="618", y="85", width="4", height="20", fill=C_GOLD, opacity="0.5")
    ET.SubElement(svg, "rect", x="612", y="91", width="16", height="4", fill=C_GOLD, opacity="0.5")

    # Second smaller church
    ET.SubElement(svg, "rect", x="690", y="240", width="50", height="80", fill=C_ACCENT, opacity="0.2")
    ET.SubElement(svg, "polygon", points="715,190 695,240 735,240", fill=C_ACCENT, opacity="0.2")
    ET.SubElement(svg, "path", d="M700,190 Q715,165 730,190", fill=C_GOLD, opacity="0.3")

    # Info box: Architecture
    add_info_box(svg, 30, 90, 240, 140, "Архитектура", [
        "Крестово-купольные храмы",
        "Шатровые храмы (XVI в.)",
        "Покрова на Нерли (1165)",
        "Успенский собор (Москва)",
        "Золотые купола — символ неба",
        "Кокошники — декор. элемент",
    ], color=C_PRIMARY)

    # Info box: Frescoes
    add_info_box(svg, 30, 245, 240, 120, "Фрески и мозаики", [
        "Фреска — живопись по сырой штукатурке",
        "Мозаика — изображение из смальты",
        "Софийский собор (Киев, XI в.)",
        "Ярославские фрески (XVII в.)",
        "Библейские сюжеты на стенах",
    ], color=C_GOLD)

    # Info box: Crafts
    add_info_box(svg, 290, 90, 240, 140, "Ремёсла", [
        "Хохломская роспись (золото)",
        "Гжель (белый + синий)",
        "Дымковская игрушка (глина)",
        "Финифть (эмаль по металлу)",
        "Чернение серебра",
        "Резьба по дереву и кости",
    ], color=C_TERRACOTTA)

    # Timeline
    ET.SubElement(svg, "rect", x="30", y="400", width="740", height="2", fill=C_PRIMARY, opacity="0.6")
    timeline = [
        (60, "988", "Крещение Руси"),
        (190, "1040", "София Киевская"),
        (320, "1165", "Покрова на Нерли"),
        (450, "1405", "Рублёв"),
        (580, "1475", "Успенский собор"),
        (700, "1552", "Покровский собор"),
    ]
    for x, year, desc in timeline:
        ET.SubElement(svg, "circle", cx=str(x), cy="400", r="5", fill=C_PRIMARY)
        t1 = ET.SubElement(svg, "text", x=str(x), y="388", fill=C_DARK,
                           fontSize="10", fontWeight="bold", textAnchor="middle",
                           fontFamily="sans-serif")
        t1.text = year
        t2 = ET.SubElement(svg, "text", x=str(x), y="420", fill=C_TEXT2,
                           fontSize="9", textAnchor="middle", fontFamily="sans-serif")
        t2.text = escape_xml(desc)

    # Decorative elements - ornamental border pattern
    for i in range(12):
        x = 60 + i * 58
        ET.SubElement(svg, "rect", x=str(x), y="440", width="30", height="8",
                      fill=C_PRIMARY, opacity="0.3", rx="2")
        ET.SubElement(svg, "rect", x=str(x + 5), y="448", width="20", height="4",
                      fill=C_GOLD, opacity="0.3", rx="1")

    # Key concept box
    ET.SubElement(svg, "rect", x="30", y="470", width="740", height="80",
                  fill="white", stroke=C_GOLD, strokeWidth="1.5", rx="6")
    ET.SubElement(svg, "rect", x="30", y="470", width="740", height="24",
                  fill=C_GOLD, rx="6")
    ET.SubElement(svg, "rect", x="30", y="488", width="740", height="6", fill=C_GOLD)
    tt = ET.SubElement(svg, "text", x="400", y="488", fill="white",
                       fontSize="12", fontWeight="bold", textAnchor="middle",
                       fontFamily="sans-serif")
    tt.text = "Ключевые особенности древнерусского искусства"
    concepts = [
        "• Синтез архитектуры, живописи и декоративного искусства",
        "• Духовность и символизм каждого элемента",
        "• Византийские традиции + национальное своеобразие"
    ]
    for i, c in enumerate(concepts):
        t = ET.SubElement(svg, "text", x="50", y=str(512 + i * 16), fill=C_TEXT2,
                          fontSize="11", fontFamily="sans-serif")
        t.text = escape_xml(c)

    # Decorative brush strokes
    add_brush_stroke(svg, 550, 120, 700, 150, C_GOLD, 4)
    add_brush_stroke(svg, 560, 180, 720, 200, C_TERRACOTTA, 3)

    add_footer(svg)
    return svg


# =====================================================================
# LESSON 2: Русская икона
# =====================================================================
def lesson_2():
    svg = ET.Element("svg", **svg_header())
    add_gradient_defs(svg)
    add_background(svg)
    add_title(svg, "Русская икона", "Техника, символика, великие иконописцы")
    add_lesson_number(svg, 2)

    # Icon frame (decorative)
    ET.SubElement(svg, "rect", x="560", y="100", width="190", height="240",
                  fill="#FEF3C7", stroke=C_GOLD, strokeWidth="3", rx="4")
    ET.SubElement(svg, "rect", x="570", y="110", width="170", height="220",
                  fill="#FFFBEB", stroke=C_DARK, strokeWidth="1", rx="2")
    # Simplified icon figure
    ET.SubElement(svg, "circle", cx="655", cy="155", r="20", fill=C_GOLD, opacity="0.4")
    ET.SubElement(svg, "rect", x="640", y="175", width="30", height="50",
                  fill=C_PRIMARY, opacity="0.3", rx="3")
    # Nimbus
    ET.SubElement(svg, "circle", cx="655", cy="155", r="25",
                  fill="none", stroke=C_GOLD, strokeWidth="2", opacity="0.6")
    # Label inside icon
    t = ET.SubElement(svg, "text", x="655", y="260", fill=C_DARK,
                      fontSize="10", textAnchor="middle", fontFamily="serif")
    t.text = "Схема иконы"

    # Info box: Technique
    add_info_box(svg, 30, 90, 250, 155, "Техника иконописи", [
        "Доска из липы/кипариса",
        "Паволока — тканевая основа",
        "Левкас — меловой грунт",
        "Яичная темпера (краски)",
        "Золочение нимбов и фона",
        "Олифа — защитный слой",
        "Прорись — контурный рисунок",
    ], color=C_PRIMARY)

    # Info box: Symbolism
    add_info_box(svg, 30, 260, 250, 130, "Символика иконы", [
        "Золотой фон — мир горний (небесный)",
        "Обратная перспектива — выход к зрителю",
        "Нимб — святость, божественный свет",
        "Цвета: красный — мученичество",
        "Синий — божественная мудрость",
    ], color=C_GOLD)

    # Info box: Famous icons
    add_info_box(svg, 300, 90, 240, 155, "Знаменитые иконы", [
        "«Троица» — А. Рублёв (XV в.)",
        "«Владимирская Б.М.» (XII в.)",
        "«Успение» — Феофан Грек",
        "«Спас Златая Риза»",
        "«Богоматерь Донская»",
      "Иконостас — иконы в ряд",
    ], color=C_TERRACOTTA)

    # Icon painters
    add_info_box(svg, 300, 260, 240, 130, "Великие иконописцы", [
        "Андрей Рублёв (1360–1430)",
        "Феофан Грек (1340–1410)",
        "Дионисий (1440–1502)",
        "Симон Ушаков (1626–1686)",
        "Прохор с Городца",
    ], color=C_PURPLE)

    # Layers diagram (cross-section of icon)
    ET.SubElement(svg, "text", x="400", y="420", fill=C_DARK, fontSize="13",
                  fontWeight="bold", textAnchor="middle", fontFamily="sans-serif")
    svg[-1].text = "Слои иконы (схема)"

    layers = [
        ("Доска", C_TERRACOTTA, 440),
        ("Паволока (ткань)", C_OLIVE, 460),
        ("Левкас (грунт)", "#D4C5A9", 480),
        ("Красочный слой", C_PRIMARY, 500),
        ("Золочение", C_GOLD, 520),
        ("Олифа (защита)", "#A0522D", 540),
    ]
    for name, color, y in layers:
        ET.SubElement(svg, "rect", x="280", y=str(y), width="240", height="16",
                      fill=color, opacity="0.7", rx="2")
        t = ET.SubElement(svg, "text", x="400", y=str(y + 12), fill="white" if color not in ["#D4C5A9"] else C_DARK,
                          fontSize="10", fontWeight="bold", textAnchor="middle",
                          fontFamily="sans-serif")
        t.text = escape_xml(name)

    add_brush_stroke(svg, 560, 350, 750, 380, C_GOLD, 3)
    add_footer(svg)
    return svg


# =====================================================================
# LESSON 3: Жанры изобразительного искусства
# =====================================================================
def lesson_3():
    svg = ET.Element("svg", **svg_header())
    add_gradient_defs(svg)
    add_background(svg)
    add_title(svg, "Жанры изобразительного искусства", "Классификация по содержанию и сюжету")
    add_lesson_number(svg, 3)

    # Central hub diagram
    ET.SubElement(svg, "circle", cx="400", cy="300", r="55",
                  fill=C_PRIMARY, opacity="0.9", filter="url(#shadow)")
    t = ET.SubElement(svg, "text", x="400", y="295", fill="white",
                      fontSize="11", fontWeight="bold", textAnchor="middle",
                      fontFamily="sans-serif")
    t.text = "Жанры"
    t2 = ET.SubElement(svg, "text", x="400", y="310", fill=C_LIGHT,
                       fontSize="10", textAnchor="middle", fontFamily="sans-serif")
    t2.text = "искусства"

    # Genre nodes around center
    genres = [
        (400, 160, "Портрет", C_RED),
        (550, 200, "Пейзаж", C_GREEN),
        (640, 300, "Натюрморт", C_GOLD),
        (550, 400, "Исторический", C_BLUE),
        (400, 440, "Батальный", C_DARK),
        (250, 400, "Бытовой", C_TERRACOTTA),
        (160, 300, "Анималистический", C_OLIVE),
        (250, 200, "Религиозный", C_PURPLE),
    ]

    for gx, gy, name, color in genres:
        # Line from center to genre
        ET.SubElement(svg, "line", x1="400", y1="300", x2=str(gx), y2=str(gy),
                      stroke=color, strokeWidth="2", opacity="0.4")
        # Genre circle
        ET.SubElement(svg, "circle", cx=str(gx), cy=str(gy), r="35",
                      fill="white", stroke=color, strokeWidth="2", filter="url(#softShadow)")
        # Colored top half
        ET.SubElement(svg, "path", d=f"M{gx-35},{gy} A35,35 0 0,1 {gx+35},{gy} Z",
                      fill=color, opacity="0.2")
        t = ET.SubElement(svg, "text", x=str(gx), y=str(gy + 4), fill=C_TEXT,
                          fontSize="9", fontWeight="bold", textAnchor="middle",
                          fontFamily="sans-serif")
        t.text = escape_xml(name)

    # Descriptions in corners
    add_info_box(svg, 30, 90, 150, 85, "Портрет", [
        "Изображение человека",
        "Передача характера",
    ], color=C_RED)

    add_info_box(svg, 620, 90, 150, 85, "Пейзаж", [
        "Изображение природы",
        "Состояние и свет",
    ], color=C_GREEN)

    add_info_box(svg, 30, 480, 150, 70, "Натюрморт", [
        "Неодушевлённые предметы",
        "Композиция и свет",
    ], color=C_GOLD)

    add_info_box(svg, 620, 480, 150, 70, "Исторический", [
        "Исторические события",
        "Герои и сюжеты",
    ], color=C_BLUE)

    add_footer(svg)
    return svg


# =====================================================================
# LESSON 4: Портрет как жанр
# =====================================================================
def lesson_4():
    svg = ET.Element("svg", **svg_header())
    add_gradient_defs(svg)
    add_background(svg)
    add_title(svg, "Портрет как жанр", "Виды портрета, техника, великие портретисты")
    add_lesson_number(svg, 4)

    # Stylized face outline on right
    ET.SubElement(svg, "ellipse", cx="650", cy="250", rx="65", ry="80",
                  fill="#FEF3C7", stroke=C_TERRACOTTA, strokeWidth="2")
    # Eyes
    ET.SubElement(svg, "ellipse", cx="630", cy="230", rx="10", ry="6",
                  fill="none", stroke=C_TEXT, strokeWidth="1.5")
    ET.SubElement(svg, "ellipse", cx="670", cy="230", rx="10", ry="6",
                  fill="none", stroke=C_TEXT, strokeWidth="1.5")
    # Nose
    ET.SubElement(svg, "path", d="M650,240 L645,260 L655,260", fill="none",
                  stroke=C_TEXT, strokeWidth="1")
    # Mouth
    ET.SubElement(svg, "path", d="M638,272 Q650,280 662,272", fill="none",
                  stroke=C_TERRACOTTA, strokeWidth="1.5")
    # Labels pointing to face
    ET.SubElement(svg, "line", x1="585", y1="230", x2="560", y2="220", stroke=C_PRIMARY, strokeWidth="1", strokeDasharray="3,2")
    t = ET.SubElement(svg, "text", x="520", y="218", fill=C_DARK, fontSize="9", textAnchor="end", fontFamily="sans-serif")
    t.text = "Взгляд"

    ET.SubElement(svg, "line", x1="715", y1="250", x2="740", y2="245", stroke=C_PRIMARY, strokeWidth="1", strokeDasharray="3,2")
    t = ET.SubElement(svg, "text", x="745", y="248", fill=C_DARK, fontSize="9", fontFamily="sans-serif")
    t.text = "Светотень"

    ET.SubElement(svg, "line", x1="650", y1="170", x2="650", y2="155", stroke=C_PRIMARY, strokeWidth="1", strokeDasharray="3,2")
    t = ET.SubElement(svg, "text", x="650", y="148", fill=C_DARK, fontSize="9", textAnchor="middle", fontFamily="sans-serif")
    t.text = "Композиция"

    # Types of portrait
    add_info_box(svg, 30, 90, 240, 155, "Виды портрета", [
        "Парадный — торжественный",
        "Камерный — интимный, домашний",
      "Психологический — внутренний мир",
        "Автопортрет — изображение себя",
        "Групповой — несколько лиц",
        "Погрудный / поясной / в рост",
    ], color=C_PRIMARY)

    # Famous portraitists
    add_info_box(svg, 30, 260, 240, 130, "Великие портретисты", [
        "Леонардо да Винчи (Мона Лиза)",
        "Рембрандт (Автопортреты)",
        "В. Серов (Девочка с персиками)",
        "И. Репин (Бурлаки на Волге)",
        "Ван Гог (Автопортреты)",
    ], color=C_GOLD)

    # Technique box
    add_info_box(svg, 300, 90, 240, 155, "Техника портрета", [
        "Пропорции лица (3 части)",
        "Светотеневая моделировка",
        "Цвет и колорит кожи",
        "Характерная поза и жест",
        "Выражение глаз — душа",
        "Фон и атрибуты",
    ], color=C_TERRACOTTA)

    # Proportions diagram
    ET.SubElement(svg, "text", x="400", y="420", fill=C_DARK, fontSize="13",
                  fontWeight="bold", textAnchor="middle", fontFamily="sans-serif")
    svg[-1].text = "Пропорции лица"
    # Face outline simplified
    ET.SubElement(svg, "ellipse", cx="400", cy="490", rx="40", ry="55",
                  fill="none", stroke=C_PRIMARY, strokeWidth="1.5", strokeDasharray="4,2")
    # Horizontal lines for proportions
    for y, label in [(445, "Волосы"), (465, "Брови"), (485, "Нос"), (505, "Рот"), (525, "Подбородок")]:
        ET.SubElement(svg, "line", x1="360", y1=str(y), x2="440", y2=str(y),
                      stroke=C_ACCENT, strokeWidth="0.5", strokeDasharray="2,2")
        t = ET.SubElement(svg, "text", x="450", y=str(y + 4), fill=C_TEXT2,
                          fontSize="9", fontFamily="sans-serif")
        t.text = label

    add_info_box(svg, 560, 280, 210, 90, "Ключевое", [
        "Портрет — зеркало души",
        "Передаёт не только внешность,",
        "но и характер, настроение,",
      "социальное положение модели",
    ], color=C_PURPLE)

    add_footer(svg)
    return svg


# =====================================================================
# LESSON 5: Пейзаж в искусстве
# =====================================================================
def lesson_5():
    svg = ET.Element("svg", **svg_header())
    add_gradient_defs(svg)
    add_background(svg)
    add_title(svg, "Пейзаж в искусстве", "Виды пейзажа, законы перспективы, великие пейзажисты")
    add_lesson_number(svg, 5)

    # Mini landscape sketch on right
    # Sky
    ET.SubElement(svg, "rect", x="530", y="95", width="240", height="70", fill="#BFDBFE", rx="4")
    # Mountains
    ET.SubElement(svg, "polygon", points="530,165 600,110 670,165", fill="#86EFAC", opacity="0.7")
    ET.SubElement(svg, "polygon", points="610,165 680,120 770,165", fill="#4ADE80", opacity="0.7")
    # Water
    ET.SubElement(svg, "rect", x="530", y="165", width="240", height="30", fill="#93C5FD", rx="2", opacity="0.6")
    # Sun
    ET.SubElement(svg, "circle", cx="700", cy="115", r="15", fill=C_GOLD, opacity="0.7")

    # Types of landscape
    add_info_box(svg, 30, 90, 240, 155, "Виды пейзажа", [
        "Сельский — природа и деревня",
        "Городской — улицы и здания",
        "Морской (марина) — море",
        "Горный — горы и вершины",
        "Лесной — деревья и чаща",
        "Промышленный — заводы",
    ], color=C_PRIMARY)

    # Perspective rules
    add_info_box(svg, 30, 260, 240, 130, "Законы перспективы", [
        "Линия горизонта — уровень глаз",
        "Точка схода на горизонте",
        "Дальше = выше и меньше",
        "Воздушная перспектива:",
        "  Дальше = бледнее и синее",
    ], color=C_BLUE)

    # Famous landscape painters
    add_info_box(svg, 290, 90, 220, 155, "Великие пейзажисты", [
        "И. Левитан («Золотая осень»)",
        "И. Шишкин («Утро в лесу»)",
        "Ф. Васильев («Мокрый луг»)",
        "А. Саврасов («Грачи прилетели»)",
        "К. Моне (« Впечатление»)",
        "У. Тёрнер (английский)",
    ], color=C_GREEN)

    # Techniques
    add_info_box(svg, 290, 260, 220, 130, "Техника пейзажа", [
        "Пленэр — работа на природе",
        "Этюд — быстрый набросок",
        "Передача освещения",
        "Рефлексы и цветовые связи",
        "Состояние: утро, день, вечер",
    ], color=C_GOLD)

    # Perspective diagram
    ET.SubElement(svg, "text", x="400", y="420", fill=C_DARK, fontSize="13",
                  fontWeight="bold", textAnchor="middle", fontFamily="sans-serif")
    svg[-1].text = "Линейная перспектива (схема)"

    # Horizon line
    ET.SubElement(svg, "line", x1="80", y1="470", x2="720", y2="470",
                  stroke=C_BLUE, strokeWidth="2", strokeDasharray="8,4")
    t = ET.SubElement(svg, "text", x="730", y="473", fill=C_BLUE, fontSize="10",
                      fontFamily="sans-serif")
    t.text = "Линия горизонта"

    # Vanishing point
    ET.SubElement(svg, "circle", cx="400", cy="470", r="5", fill=C_RED)
    t = ET.SubElement(svg, "text", x="400", y="465", fill=C_RED, fontSize="9",
                      textAnchor="middle", fontFamily="sans-serif")
    t.text = "Точка схода"

    # Converging lines
    ET.SubElement(svg, "line", x1="80", y1="550", x2="400", y2="470", stroke=C_PRIMARY, strokeWidth="1.5", opacity="0.5")
    ET.SubElement(svg, "line", x1="720", y1="550", x2="400", y2="470", stroke=C_PRIMARY, strokeWidth="1.5", opacity="0.5")
    ET.SubElement(svg, "line", x1="200", y1="550", x2="400", y2="470", stroke=C_PRIMARY, strokeWidth="1", opacity="0.3")
    ET.SubElement(svg, "line", x1="600", y1="550", x2="400", y2="470", stroke=C_PRIMARY, strokeWidth="1", opacity="0.3")

    # Objects getting smaller
    for i, (x, w) in enumerate([(200, 30), (300, 20), (400, 12), (500, 20), (600, 30)]):
        h = 25 - abs(i - 2) * 5
        y_top = 470 - h
        ET.SubElement(svg, "rect", x=str(x - w // 2), y=str(y_top), width=str(w), height=str(h),
                      fill=C_TERRACOTTA, opacity="0.5", rx="1")

    add_footer(svg)
    return svg


# =====================================================================
# LESSON 6: Натюрморт
# =====================================================================
def lesson_6():
    svg = ET.Element("svg", **svg_header())
    add_gradient_defs(svg)
    add_background(svg)
    add_title(svg, "Натюрморт", "Композиция, освещение, великие натюрморты")
    add_lesson_number(svg, 6)

    # Mini still life sketch (vase + fruit)
    # Table
    ET.SubElement(svg, "rect", x="560", y="250", width="200", height="8", fill=C_TERRACOTTA, rx="2")
    # Vase
    ET.SubElement(svg, "path", d="M630,250 Q620,220 625,200 Q630,180 640,170 Q650,180 655,200 Q660,220 650,250 Z",
                  fill="#7DD3FC", stroke=C_BLUE, strokeWidth="1", opacity="0.7")
    # Apple
    ET.SubElement(svg, "circle", cx="680", cy="240", r="14", fill="#EF4444", opacity="0.7")
    # Orange
    ET.SubElement(svg, "circle", cx="710", cy="238", r="12", fill="#F97316", opacity="0.7")
    # Lemon
    ET.SubElement(svg, "ellipse", cx="590", cy="242", rx="15", ry="10", fill="#FDE047", opacity="0.7")
    # Shadow
    ET.SubElement(svg, "ellipse", cx="650", cy="258", rx="60", ry="5", fill="#000", opacity="0.1")
    t = ET.SubElement(svg, "text", x="660", y="290", fill=C_TEXT2, fontSize="10",
                      textAnchor="middle", fontFamily="sans-serif")
    t.text = "Схема натюрморта"

    # Composition rules
    add_info_box(svg, 30, 90, 240, 145, "Композиция натюрморта", [
        "Центр композиции — главный предмет",
        "Правило золотого сечения",
        "Контраст форм и размеров",
        "Ритм предметов (ближе-дальше)",
        "Передний, средний, задний план",
        "Диагональная композиция",
    ], color=C_PRIMARY)

    # Lighting
    add_info_box(svg, 30, 250, 240, 130, "Освещение", [
        "Свет (блик) — самый светлый",
        "Полутень — переходная область",
        "Тень — собственная и падающая",
        "Рефлекс — отражённый свет в тени",
        "Направление света задаёт тон",
    ], color=C_GOLD)

    # Famous still lifes
    add_info_box(svg, 290, 90, 240, 145, "Знаменитые натюрморты", [
        "П. Сезанн («Яблоки и апельсины»)",
        "В. ван Гог («Подсолнухи»)",
        "Я. де Хем (голландский)",
        "В. Серов и К. Коровин",
        "И. Машков («Снедь московская»)",
        "П. Кончаловский («Сирень»)",
    ], color=C_TERRACOTTA)

    # Types
    add_info_box(svg, 290, 250, 240, 130, "Виды натюрморта", [
        "«Vanitas» — бренность бытия",
        "Цветочный — букеты и растения",
        "Завтрак — стол с яствами",
        "Охотничий — дичь и утварь",
        "Декоративный — украшение",
    ], color=C_GREEN)

    # Tonal scale diagram
    ET.SubElement(svg, "text", x="400", y="420", fill=C_DARK, fontSize="13",
                  fontWeight="bold", textAnchor="middle", fontFamily="sans-serif")
    svg[-1].text = "Шкала светотени"

    tones = [
        ("Свет", "#FFFFF0", 440),
        ("Полутень", "#D4C5A9", 462),
        ("Собств. тень", "#8B7355", 484),
        ("Рефлекс", "#A0522D", 506),
        ("Пад. тень", "#3D2B1F", 528),
    ]
    for name, color, y in tones:
        ET.SubElement(svg, "rect", x="200", y=str(y), width="400", height="18",
                      fill=color, stroke=C_WARM_GRAY, strokeWidth="0.5", rx="2")
        text_color = "white" if color in ["#8B7355", "#A0522D", "#3D2B1F"] else C_DARK
        t = ET.SubElement(svg, "text", x="400", y=str(y + 13), fill=text_color,
                          fontSize="10", fontWeight="bold", textAnchor="middle",
                          fontFamily="sans-serif")
        t.text = escape_xml(name)

    add_footer(svg)
    return svg


# =====================================================================
# LESSON 7: Скульптура
# =====================================================================
def lesson_7():
    svg = ET.Element("svg", **svg_header())
    add_gradient_defs(svg)
    add_background(svg)
    add_title(svg, "Скульптура", "Виды, материалы, великие скульпторы")
    add_lesson_number(svg, 7)

    # Stylized sculpture (bust outline)
    ET.SubElement(svg, "rect", x="610", y="180", width="80", height="10", fill="#78716C", rx="2")  # Base
    ET.SubElement(svg, "rect", x="625", y="130", width="50", height="50", fill="#D4C5A9", stroke=C_WARM_GRAY, strokeWidth="1", rx="4")  # Head
    ET.SubElement(svg, "path", d="M615,190 Q615,170 625,180 L675,180 Q685,170 685,190 L685,200 L615,200 Z",
                  fill="#D4C5A9", stroke=C_WARM_GRAY, strokeWidth="1")  # Shoulders
    t = ET.SubElement(svg, "text", x="650", y="225", fill=C_TEXT2, fontSize="10",
                      textAnchor="middle", fontFamily="sans-serif")
    t.text = "Круглая скульптура"

    # Relief examples
    ET.SubElement(svg, "rect", x="560", y="260", width="160", height="60", fill="#E5E7EB", stroke=C_WARM_GRAY, strokeWidth="1", rx="2")
    # Raised elements on relief
    ET.SubElement(svg, "circle", cx="600", cy="285", r="12", fill="#D4C5A9", stroke=C_WARM_GRAY, strokeWidth="0.5")
    ET.SubElement(svg, "circle", cx="640", cy="280", r="10", fill="#C4B599", stroke=C_WARM_GRAY, strokeWidth="0.5")
    ET.SubElement(svg, "rect", x="665", y="270", width="30", height="20", fill="#C4B599", stroke=C_WARM_GRAY, strokeWidth="0.5", rx="2")
    t = ET.SubElement(svg, "text", x="640", y="340", fill=C_TEXT2, fontSize="10",
                      textAnchor="middle", fontFamily="sans-serif")
    t.text = "Рельеф (барельеф / горельеф)"

    # Types of sculpture
    add_info_box(svg, 30, 90, 240, 155, "Виды скульптуры", [
        "Круглая — осмотр со всех сторон",
        "Барельеф — выступ < половины",
        "Горельеф — выступ > половины",
        "Контррельеф — углублённый",
        "Статуя — фигура в рост",
        "Бюст — голова и плечи",
    ], color=C_PRIMARY)

    # Materials
    add_info_box(svg, 30, 260, 240, 130, "Материалы", [
        "Мрамор — благородный камень",
        "Бронза — прочный металл (литьё)",
        "Дерево — резьба по дереву",
        "Глина — лепка и обжиг",
        "Камень — высекание (карьер)",
    ], color=C_TERRACOTTA)

    # Famous sculptors and works
    add_info_box(svg, 290, 90, 240, 155, "Великие скульпторы", [
        "Микеланджело («Давид»)",
        "А. Роден («Мыслитель»)",
        "Фидий (Парфенон, Афины)",
      "Донателло («Давид» бронза)",
        "О. Роден («Поцелуй»)",
        "П. Трубецкой (Россия)",
    ], color=C_BLUE)

    # Russian sculpture
    add_info_box(svg, 290, 260, 240, 130, "Русская скульптура", [
        "Ф. Шубин (портреты-бюсты)",
        "И. Мартос (Минин и Пожарский)",
        "П. Клодт (укротители коней)",
        "В. Мухина (Рабочий и колхозница)",
        "А. Опекушин (Пушкин на Тверском)",
    ], color=C_GOLD)

    # Sculpture process diagram
    ET.SubElement(svg, "text", x="400", y="420", fill=C_DARK, fontSize="13",
                  fontWeight="bold", textAnchor="middle", fontFamily="sans-serif")
    svg[-1].text = "Процесс создания скульптуры"

    steps = [
        ("Эскиз", "Рисунок", 80),
        ("Каркас", "Проволока", 210),
        ("Лепка", "Глина/воск", 340),
        ("Форма", "Гипс/резина", 470),
        ("Отливка", "Бронза", 600),
    ]
    for name, desc, x in steps:
        ET.SubElement(svg, "rect", x=str(x), y="445", width="110", height="35",
                      fill=C_PRIMARY, opacity="0.15", stroke=C_PRIMARY, strokeWidth="1", rx="6")
        t = ET.SubElement(svg, "text", x=str(x + 55), y="460", fill=C_DARK,
                          fontSize="10", fontWeight="bold", textAnchor="middle",
                          fontFamily="sans-serif")
        t.text = escape_xml(name)
        t2 = ET.SubElement(svg, "text", x=str(x + 55), y="473", fill=C_TEXT2,
                           fontSize="8", textAnchor="middle", fontFamily="sans-serif")
        t2.text = escape_xml(desc)
    # Arrows between steps
    for i in range(len(steps) - 1):
        x1 = steps[i][2] + 110
        x2 = steps[i + 1][2]
        ET.SubElement(svg, "line", x1=str(x1), y1="462", x2=str(x2), y2="462",
                      stroke=C_PRIMARY, strokeWidth="2", markerEnd="url(#arrow)")

    # Arrow marker
    defs = svg.find("defs")
    marker = ET.SubElement(defs, "marker", id="arrow", viewBox="0 0 10 10",
                           refX="10", refY="5", markerWidth="6", markerHeight="6",
                           orient="auto-start-reverse")
    ET.SubElement(marker, "path", d="M 0 0 L 10 5 L 0 10 z", fill=C_PRIMARY)

    add_footer(svg)
    return svg


# =====================================================================
# LESSON 8: Архитектура
# =====================================================================
def lesson_8():
    svg = ET.Element("svg", **svg_header())
    add_gradient_defs(svg)
    add_background(svg)
    add_title(svg, "Архитектура", "Стили, элементы, великие здания")
    add_lesson_number(svg, 8)

    # Building silhouettes (3 columns)
    # Classical column
    ET.SubElement(svg, "rect", x="580", y="160", width="40", height="130", fill="#D4C5A9", stroke=C_WARM_GRAY, strokeWidth="1")
    ET.SubElement(svg, "rect", x="572", y="150", width="56", height="12", fill="#E5E7EB", stroke=C_WARM_GRAY, strokeWidth="1")
    ET.SubElement(svg, "rect", x="572", y="290", width="56", height="10", fill="#E5E7EB", stroke=C_WARM_GRAY, strokeWidth="1")
    # Entablature
    ET.SubElement(svg, "rect", x="565", y="140", width="70", height="10", fill="#D4C5A9", stroke=C_WARM_GRAY, strokeWidth="1")
    # Pediment
    ET.SubElement(svg, "polygon", points="565,140 600,110 635,140", fill="#E5E7EB", stroke=C_WARM_GRAY, strokeWidth="1")
    t = ET.SubElement(svg, "text", x="600", y="320", fill=C_TEXT2, fontSize="9",
                      textAnchor="middle", fontFamily="sans-serif")
    t.text = "Ордер"

    # Gothic building
    ET.SubElement(svg, "polygon", points="680,120 660,290 700,290", fill="#A8A29E", stroke=C_WARM_GRAY, strokeWidth="1")
    ET.SubElement(svg, "rect", x="660", y="290", width="40", height="10", fill="#78716C")
    # Spire
    ET.SubElement(svg, "polygon", points="680,70 675,120 685,120", fill="#D4C5A9", stroke=C_WARM_GRAY, strokeWidth="0.5")
    # Pointed window
    ET.SubElement(svg, "path", d="M680,220 Q674,250 677,270 L683,270 Q686,250 680,220", fill="#7DD3FC", opacity="0.5")
    t = ET.SubElement(svg, "text", x="680", y="320", fill=C_TEXT2, fontSize="9",
                      textAnchor="middle", fontFamily="sans-serif")
    t.text = "Готика"

    # Dome building
    ET.SubElement(svg, "rect", x="730", y="220", width="45", height="80", fill="#D4C5A9", stroke=C_WARM_GRAY, strokeWidth="1")
    ET.SubElement(svg, "path", d="M730,220 Q752,170 775,220", fill=C_GOLD, opacity="0.5", stroke=C_WARM_GRAY, strokeWidth="1")
    t = ET.SubElement(svg, "text", x="752", y="320", fill=C_TEXT2, fontSize="9",
                      textAnchor="middle", fontFamily="sans-serif")
    t.text = "Купол"

    # Architectural styles
    add_info_box(svg, 30, 90, 240, 155, "Архитектурные стили", [
        "Античность — ордера, храмы",
        "Романский — массив, толщина",
        "Готика — стрельчатые арки",
        "Ренессанс — гармония, симметрия",
        "Барокко — пышность, динамика",
        "Классицизм — порядок, колонны",
    ], color=C_PRIMARY)

    # Elements
    add_info_box(svg, 30, 260, 240, 130, "Элементы здания", [
        "Фундамент — основание",
        "Колонна — вертикальная опора",
        "Арка — криволинейное перекрытие",
        "Купол — сводчатое покрытие",
        "Фронтон — треугольная деталь",
    ], color=C_GOLD)

    # Famous buildings
    add_info_box(svg, 290, 90, 250, 155, "Знаменитые здания", [
        "Парфенон (Афины, 447 до н.э.)",
        "Колизей (Рим, 80 н.э.)",
        "Нотр-Дам (Париж, 1345)",
        "Собор Св. Петра (Рим, 1626)",
        "Тадж-Махал (Индия, 1653)",
        "Кремль (Москва, XV в.)",
    ], color=C_BLUE)

    # Russian architecture
    add_info_box(svg, 290, 260, 250, 130, "Русская архитектура", [
        "Белокаменное зодчество",
        "Шатровые храмы (XVI в.)",
        "Нарышкинское барокко",
        "Псевдорусский стиль (XIX в.)",
        "Конструктивизм (XX в.)",
    ], color=C_TERRACOTTA)

    # Timeline of styles
    ET.SubElement(svg, "text", x="400", y="420", fill=C_DARK, fontSize="13",
                  fontWeight="bold", textAnchor="middle", fontFamily="sans-serif")
    svg[-1].text = "Хронология стилей"

    ET.SubElement(svg, "rect", x="50", y="440", width="700", height="3", fill=C_PRIMARY, opacity="0.4")

    style_timeline = [
        (80, "Античн.", "#8B4513"),
        (200, "Роман.", "#A0522D"),
        (310, "Готика", "#78350F"),
        (420, "Ренесс.", C_GOLD),
        (530, "Барокко", C_TERRACOTTA),
        (640, "Класс.", C_PRIMARY),
    ]
    for x, name, color in style_timeline:
        ET.SubElement(svg, "circle", cx=str(x), cy="441", r="6", fill=color)
        t = ET.SubElement(svg, "text", x=str(x), y="462", fill=C_TEXT,
                          fontSize="9", fontWeight="bold", textAnchor="middle",
                          fontFamily="sans-serif")
        t.text = escape_xml(name)

    # Architecture formula
    ET.SubElement(svg, "rect", x="100", y="480", width="600", height="55",
                  fill="white", stroke=C_GOLD, strokeWidth="1.5", rx="6")
    t = ET.SubElement(svg, "text", x="400", y="500", fill=C_DARK,
                      fontSize="12", fontWeight="bold", textAnchor="middle",
                      fontFamily="sans-serif")
    t.text = "Формула Витрувия: «Прочность, Польза, Красота»"
    t2 = ET.SubElement(svg, "text", x="400", y="520", fill=C_TEXT2,
                       fontSize="10", textAnchor="middle", fontFamily="sans-serif")
    t2.text = "Firmitas, Utilitas, Venustas — три начала архитектуры"

    add_footer(svg)
    return svg


# =====================================================================
# LESSON 9: Искусство Возрождения
# =====================================================================
def lesson_9():
    svg = ET.Element("svg", **svg_header())
    add_gradient_defs(svg)
    add_background(svg)
    add_title(svg, "Искусство Возрождения", "Леонардо, Микеланджело, Рафаэль — титаны Ренессанса")
    add_lesson_number(svg, 9)

    # Three great masters - diagram
    # Leonardo
    ET.SubElement(svg, "circle", cx="160", cy="310", r="45", fill="#FEF3C7", stroke=C_GOLD, strokeWidth="2")
    ET.SubElement(svg, "text", x="160", y="305", fill=C_DARK, fontSize="9", fontWeight="bold",
                  textAnchor="middle", fontFamily="sans-serif")
    svg[-1].text = "Леонардо"
    ET.SubElement(svg, "text", x="160", y="318", fill=C_TEXT2, fontSize="8",
                  textAnchor="middle", fontFamily="sans-serif")
    svg[-1].text = "да Винчи"

    # Michelangelo
    ET.SubElement(svg, "circle", cx="400", cy="280", r="45", fill="#FEF3C7", stroke=C_PRIMARY, strokeWidth="2")
    ET.SubElement(svg, "text", x="400", y="275", fill=C_DARK, fontSize="9", fontWeight="bold",
                  textAnchor="middle", fontFamily="sans-serif")
    svg[-1].text = "Микеланджело"
    ET.SubElement(svg, "text", x="400", y="288", fill=C_TEXT2, fontSize="8",
                  textAnchor="middle", fontFamily="sans-serif")
    svg[-1].text = "Буонарроти"

    # Raphael
    ET.SubElement(svg, "circle", cx="640", cy="310", r="45", fill="#FEF3C7", stroke=C_BLUE, strokeWidth="2")
    ET.SubElement(svg, "text", x="640", y="305", fill=C_DARK, fontSize="9", fontWeight="bold",
                  textAnchor="middle", fontFamily="sans-serif")
    svg[-1].text = "Рафаэль"
    ET.SubElement(svg, "text", x="640", y="318", fill=C_TEXT2, fontSize="8",
                  textAnchor="middle", fontFamily="sans-serif")
    svg[-1].text = "Санти"

    # Connecting lines
    ET.SubElement(svg, "line", x1="205", y1="300", x2="355", y2="285", stroke=C_GOLD, strokeWidth="1", opacity="0.4")
    ET.SubElement(svg, "line", x1="445", y1="285", x2="595", y2="300", stroke=C_GOLD, strokeWidth="1", opacity="0.4")
    ET.SubElement(svg, "line", x1="205", y1="315", x2="595", y2="315", stroke=C_GOLD, strokeWidth="1", opacity="0.3")
    # Label
    ET.SubElement(svg, "text", x="400", y="370", fill=C_GOLD, fontSize="12",
                  fontWeight="bold", textAnchor="middle", fontFamily="serif")
    svg[-1].text = "Титаны Возрождения"

    # Leonardo works
    add_info_box(svg, 30, 90, 210, 140, "Леонардо да Винчи", [
        "«Мона Лиза» (Джоконда)",
        "«Тайная вечеря» (фреска)",
        "«Дама с горностаем»",
        "Сфумато — мягкие тени",
        "Учёный + художник",
      "Зеркальный почерк",
    ], color=C_GOLD)

    # Michelangelo works
    add_info_box(svg, 260, 90, 210, 140, "Микеланджело", [
        "«Давид» (мрамор, 5 м)",
        "Сикстинская капелла (фреска)",
        "«Сотворение Адама»",
        "«Пьета» (Ватикан)",
        "Скульптор + живописец",
        "Терракотовые эскизы",
    ], color=C_PRIMARY)

    # Raphael works
    add_info_box(svg, 490, 90, 210, 140, "Рафаэль Санти", [
        "«Сикстинская Мадонна»",
        "«Афинская школа» (фреска)",
        "«Мадонна Конестабиле»",
        "Идеал красоты и гармонии",
        "Мастер композиции",
        "Станцы Ватикана",
    ], color=C_BLUE)

    # Key features of Renaissance
    ET.SubElement(svg, "rect", x="30", y="395", width="740", height="80",
                  fill="white", stroke=C_GOLD, strokeWidth="1.5", rx="6")
    ET.SubElement(svg, "rect", x="30", y="395", width="740", height="24",
                  fill=C_GOLD, rx="6")
    ET.SubElement(svg, "rect", x="30", y="413", width="740", height="6", fill=C_GOLD)
    t = ET.SubElement(svg, "text", x="400", y="413", fill="white",
                      fontSize="12", fontWeight="bold", textAnchor="middle",
                      fontFamily="sans-serif")
    t.text = "Главные черты Возрождения (Ренессанса)"
    features = [
        "• Антропоцентризм — человек мера всех вещей",
        "• Возрождение античных идеалов красоты и гармонии",
        "• Перспектива, анатомия, законы композиции"
    ]
    for i, f in enumerate(features):
        t = ET.SubElement(svg, "text", x="50", y=str(437 + i * 15), fill=C_TEXT2,
                          fontSize="11", fontFamily="sans-serif")
        t.text = escape_xml(f)

    # Timeline
    ET.SubElement(svg, "rect", x="50", y="490", width="700", height="3", fill=C_GOLD, opacity="0.4")
    renaissance_timeline = [
        (100, "1401", "Конкурс дверей"),
        (230, "1452", "Рождение Л."),
        (360, "1504", "Давид М."),
        (490, "1512", "Сикстинская"),
        (620, "1520", "Смерть Рафаэля"),
    ]
    for x, year, desc in renaissance_timeline:
        ET.SubElement(svg, "circle", cx=str(x), cy="491", r="4", fill=C_GOLD)
        t = ET.SubElement(svg, "text", x=str(x), y="480", fill=C_DARK,
                          fontSize="9", fontWeight="bold", textAnchor="middle",
                          fontFamily="sans-serif")
        t.text = year
        t2 = ET.SubElement(svg, "text", x=str(x), y="510", fill=C_TEXT2,
                           fontSize="8", textAnchor="middle", fontFamily="sans-serif")
        t2.text = escape_xml(desc)

    # Sfumato explanation
    ET.SubElement(svg, "rect", x="100", y="525", width="600", height="35",
                  fill="#FEF3C7", stroke=C_GOLD, strokeWidth="1", rx="4")
    t = ET.SubElement(svg, "text", x="400", y="547", fill=C_DARK,
                      fontSize="11", fontWeight="bold", textAnchor="middle",
                      fontFamily="sans-serif")
    t.text = "Сфумато (леонардовский дым) — плавный переход света в тень без резких границ"

    add_footer(svg)
    return svg


# =====================================================================
# LESSON 10: Русские художники 19 века
# =====================================================================
def lesson_10():
    svg = ET.Element("svg", **svg_header())
    add_gradient_defs(svg)
    add_background(svg)
    add_title(svg, "Русские художники XIX века", "Передвижники, реализм, великие полотна")
    add_lesson_number(svg, 10)

    # Peredvizhniki info
    add_info_box(svg, 30, 90, 240, 145, "Товарищество передвижников", [
        "Основано в 1870 году",
        "Иван Крамской — идейный лидер",
        "Выставки по городам России",
        "Реализм и народная тема",
        "Против академизма",
      "17 выставок за 50 лет",
    ], color=C_PRIMARY)

    # Key painters
    add_info_box(svg, 290, 90, 240, 145, "Великие художники", [
        "И. Репин — мастер портрета",
        "В. Суриков — историч. картины",
        "И. Левитан — пейзажист",
        "И. Шишкин — лесной пейзаж",
        "В. Серов — портрет и жанр",
        "В. Васнецов — сказочные темы",
    ], color=C_GOLD)

    # Famous paintings
    add_info_box(svg, 540, 90, 230, 145, "Знаменитые картины", [
        "«Бурлаки на Волге» — Репин",
        "«Утро стрелецкой казни» — Суриков",
        "«Золотая осень» — Левитан",
        "«Утро в сосновом лесу» — Шишкин",
        "«Девочка с персиками» — Серов",
        "«Богатыри» — Васнецов",
    ], color=C_TERRACOTTA)

    # Painting style analysis
    add_info_box(svg, 30, 250, 240, 120, "Особенности живописи", [
        "Реалистичное изображение",
        "Социальная тематика",
        "Жанровые сцены из жизни",
        "Психологизм портретов",
        "Эпический размах",
    ], color=C_BLUE)

    # Historical context
    add_info_box(svg, 290, 250, 240, 120, "Исторический контекст", [
        "Отмена крепостного права (1861)",
        "Реформы Александра II",
        "Развитие критич. реализма",
        "Влияние В. Белинского",
        "Журнал «Отечественные записки»",
    ], color=C_GREEN)

    # Timeline of key works
    ET.SubElement(svg, "text", x="400", y="410", fill=C_DARK, fontSize="13",
                  fontWeight="bold", textAnchor="middle", fontFamily="sans-serif")
    svg[-1].text = "Хронология великих полотен"

    ET.SubElement(svg, "rect", x="50", y="430", width="700", height="3", fill=C_PRIMARY, opacity="0.4")
    works_timeline = [
        (80, "1863", "Бунт 14-ти"),
        (180, "1870", "ТПХВ"),
        (280, "1873", "Бурлаки"),
        (380, "1880", "Кружевница"),
        (480, "1889", "Богатыри"),
        (580, "1895", "Зол. осень"),
        (680, "1899", "Девочка"),
    ]
    for x, year, desc in works_timeline:
        ET.SubElement(svg, "circle", cx=str(x), cy="431", r="5", fill=C_PRIMARY)
        t = ET.SubElement(svg, "text", x=str(x), y="420", fill=C_DARK,
                          fontSize="9", fontWeight="bold", textAnchor="middle",
                          fontFamily="sans-serif")
        t.text = year
        t2 = ET.SubElement(svg, "text", x=str(x), y="452", fill=C_TEXT2,
                           fontSize="8", textAnchor="middle", fontFamily="sans-serif")
        t2.text = escape_xml(desc)

    # Key concept
    ET.SubElement(svg, "rect", x="100", y="475", width="600", height="70",
                  fill="white", stroke=C_PRIMARY, strokeWidth="1.5", rx="6")
    t = ET.SubElement(svg, "text", x="400", y="498", fill=C_DARK,
                      fontSize="12", fontWeight="bold", textAnchor="middle",
                      fontFamily="sans-serif")
    t.text = "Главный принцип передвижников"
    t2 = ET.SubElement(svg, "text", x="400", y="518", fill=C_TEXT2,
                       fontSize="11", textAnchor="middle", fontFamily="sans-serif")
    t2.text = "«Искусство должно служить народу, отражать правду жизни»"
    t3 = ET.SubElement(svg, "text", x="400", y="535", fill=C_WARM_GRAY,
                       fontSize="10", textAnchor="middle", fontFamily="sans-serif")
    t3.text = "Критический реализм — правда без прикрас, но с сочувствием"

    add_footer(svg)
    return svg


# =====================================================================
# LESSON 11: Импрессионизм
# =====================================================================
def lesson_11():
    svg = ET.Element("svg", **svg_header())
    add_gradient_defs(svg)
    add_background(svg)
    add_title(svg, "Импрессионизм", "Моне, Ренуар, Дега — революция в живописи")
    add_lesson_number(svg, 11)

    # Color dots (impressionist technique)
    for cx, cy, colors in [
        (620, 150, ["#EF4444", "#F97316", "#EAB308", "#22C55E", "#3B82F6", "#8B5CF6"]),
        (700, 200, ["#FDE047", "#FB923C", "#F87171", "#A78BFA", "#60A5FA"]),
        (660, 250, ["#86EFAC", "#FCA5A5", "#FDE68A", "#C4B5FD", "#FDBA74"]),
    ]:
        for i, c in enumerate(colors):
            import math
            angle = i * (2 * 3.14159 / len(colors))
            dx = int(20 * math.cos(angle))
            dy = int(20 * math.sin(angle))
            ET.SubElement(svg, "circle", cx=str(cx + dx), cy=str(cy + dy), r="6", fill=c, opacity="0.7")

    t = ET.SubElement(svg, "text", x="660", y="290", fill=C_TEXT2, fontSize="10",
                      textAnchor="middle", fontFamily="sans-serif")
    t.text = "Живопись чистым цветом"

    # Monet
    add_info_box(svg, 30, 90, 210, 145, "Клод Моне (1840–1926)", [
        "«Впечатление. Восход солнца»",
        "Название движения!",
        "Серия «Руанский собор»",
        "«Кувшинки» (сад в Живерни)",
        "Пленэр — основа метода",
      "Живопись вибрации света",
    ], color=C_PRIMARY)

    # Renoir
    add_info_box(svg, 260, 90, 210, 145, "Огюст Ренуар", [
        "«Бал в Мулен де ла Галетт»",
        "«Завтрак гребцов»",
        "Радость жизни и света",
        "Розовые и голубые тона",
        "Мастер фигуры и портрета",
      "Нежность и чувственность",
    ], color=C_GOLD)

    # Degas
    add_info_box(svg, 490, 90, 210, 145, "Эдгар Дега", [
        "«Танцевальный класс»",
        "Балерины — главная тема",
        "Необычные ракурсы",
        "Мастер пастели",
        "Движение и момент",
      "Влияние фотографии",
    ], color=C_BLUE)

    # Technique
    add_info_box(svg, 30, 250, 240, 120, "Техника импрессионистов", [
        "Раздельные мазки чистого цвета",
        "Оптическое смешение (глазом)",
        "Работа на пленэре (на улице)",
        "Передача мгновенного впечатления",
        "Отказ от чёрного цвета",
    ], color=C_TERRACOTTA)

    # Principles
    add_info_box(svg, 290, 250, 240, 120, "Принципы импрессионизма", [
        "Свет важнее предмета",
        "Мгновение вместо вечности",
        "Цвет вместо линии",
        "Впечатление вместо описания",
        "Эмоция вместо рассудка",
    ], color=C_PURPLE)

    # Other impressionists
    add_info_box(svg, 540, 250, 230, 120, "Другие импрессионисты", [
        "К. Писсарро — «отец» группы",
        "Б. Моризо — женщина-художник",
        "А. Сислей — пейзажист",
        "П. Сезанн — постимпрессионизм",
        "А. Тулуз-Лотрек — плакат",
    ], color=C_GREEN)

    # Key dates
    ET.SubElement(svg, "rect", x="50", y="400", width="700", height="3", fill=C_PRIMARY, opacity="0.4")
    imp_timeline = [
        (100, "1863", "Салон отверженных"),
        (230, "1874", "1-я выставка"),
        (360, "1886", "Последняя выставка"),
        (490, "1890", "Моне: серии"),
        (620, "1900", "Признание"),
    ]
    for x, year, desc in imp_timeline:
        ET.SubElement(svg, "circle", cx=str(x), cy="401", r="5", fill=C_PRIMARY)
        t = ET.SubElement(svg, "text", x=str(x), y="390", fill=C_DARK,
                          fontSize="9", fontWeight="bold", textAnchor="middle",
                          fontFamily="sans-serif")
        t.text = year
        t2 = ET.SubElement(svg, "text", x=str(x), y="422", fill=C_TEXT2,
                           fontSize="8", textAnchor="middle", fontFamily="sans-serif")
        t2.text = escape_xml(desc)

    # Key message
    ET.SubElement(svg, "rect", x="100", y="445", width="600", height="55",
                  fill="white", stroke=C_PRIMARY, strokeWidth="1.5", rx="6")
    t = ET.SubElement(svg, "text", x="400", y="468", fill=C_DARK,
                      fontSize="12", fontWeight="bold", textAnchor="middle",
                      fontFamily="sans-serif")
    t.text = "Импрессионизм = Впечатление (impression)"
    t2 = ET.SubElement(svg, "text", x="400", y="488", fill=C_TEXT2,
                       fontSize="10", textAnchor="middle", fontFamily="sans-serif")
    t2.text = "Живопись, которая уловила мгновение света и изменила искусство навсегда"

    add_footer(svg)
    return svg


# =====================================================================
# LESSON 12: Современное искусство
# =====================================================================
def lesson_12():
    svg = ET.Element("svg", **svg_header())
    add_gradient_defs(svg)
    add_background(svg)
    add_title(svg, "Современное искусство", "Абстракция, поп-арт, инсталляция, цифровое искусство")
    add_lesson_number(svg, 12)

    # Abstract art element (geometric shapes)
    ET.SubElement(svg, "rect", x="600", y="100", width="50", height="50",
                  fill="#EF4444", opacity="0.5", transform="rotate(15 625 125)")
    ET.SubElement(svg, "circle", cx="680", cy="120", r="25",
                  fill="#3B82F6", opacity="0.5")
    ET.SubElement(svg, "polygon", points="650,180 630,210 670,210",
                  fill="#EAB308", opacity="0.5")

    # Pop art element
    ET.SubElement(svg, "rect", x="600", y="230", width="150", height="100",
                  fill="#FDE047", stroke=C_PRIMARY, strokeWidth="2", rx="4")
    ET.SubElement(svg, "circle", cx="675", cy="280", r="30",
                  fill="#EF4444", stroke=C_DARK, strokeWidth="2")
    # Dots pattern (pop art)
    for dx in range(5):
        for dy in range(3):
            ET.SubElement(svg, "circle", cx=str(612 + dx * 28), cy=str(248 + dy * 20),
                          r="4", fill=C_PRIMARY, opacity="0.3")

    # Directions of modern art
    add_info_box(svg, 30, 90, 240, 155, "Направления XX–XXI вв.", [
        "Абстракционизм (Кандинский)",
        "Кубизм (Пикассо, Брак)",
        "Сюрреализм (Дали, Магритт)",
        "Поп-арт (Уорхол, Лихтенштейн)",
        "Минимализм (Малевич, Джадд)",
        "Концептуализм (идея важнее)",
    ], color=C_PRIMARY)

    # Digital art
    add_info_box(svg, 30, 260, 240, 130, "Цифровое искусство", [
        "Компьютерная графика",
        "Генеративное искусство (AI)",
        "NFT и блокчейн",
        "Виртуальная реальность (VR)",
        "Интерактивные инсталляции",
    ], color=C_BLUE)

    # Installations and performance
    add_info_box(svg, 290, 90, 240, 155, "Инсталляция и перформанс", [
        "Инсталляция — пространств. объект",
        "Перформанс — живое действие",
        "Хэппенинг — зрители участвуют",
        "Видеоарт — экранное искусство",
        "Лэнд-арт — природные объекты",
        "Реди-мейд (Дюшан — «Фонтан»)",
    ], color=C_TERRACOTTA)

    # Key artists
    add_info_box(svg, 290, 260, 240, 130, "Ключевые фигуры", [
        "В. Кандинский (абстракция)",
        "К. Малевич («Чёрный квадрат»)",
        "С. Дали (сюрреализм)",
        "П. Пикассо (кубизм)",
        "Э. Уорхол (поп-арт)",
    ], color=C_GOLD)

    # Timeline
    ET.SubElement(svg, "text", x="400", y="420", fill=C_DARK, fontSize="13",
                  fontWeight="bold", textAnchor="middle", fontFamily="sans-serif")
    svg[-1].text = "Хронология современного искусства"

    ET.SubElement(svg, "rect", x="50", y="440", width="700", height="3", fill=C_PRIMARY, opacity="0.4")
    modern_timeline = [
        (80, "1910", "Абстракция"),
        (180, "1915", "Чёрный квадрат"),
        (280, "1930", "Сюрреализм"),
        (380, "1950", "Поп-арт"),
        (480, "1970", "Концепт-арт"),
        (580, "1990", "Цифровое"),
        (680, "2020", "AI-арт"),
    ]
    for x, year, desc in modern_timeline:
        ET.SubElement(svg, "circle", cx=str(x), cy="441", r="5", fill=C_PRIMARY)
        t = ET.SubElement(svg, "text", x=str(x), y="430", fill=C_DARK,
                          fontSize="9", fontWeight="bold", textAnchor="middle",
                          fontFamily="sans-serif")
        t.text = year
        t2 = ET.SubElement(svg, "text", x=str(x), y="462", fill=C_TEXT2,
                           fontSize="8", textAnchor="middle", fontFamily="sans-serif")
        t2.text = escape_xml(desc)

    # Key question
    ET.SubElement(svg, "rect", x="100", y="480", width="600", height="70",
                  fill="white", stroke=C_PRIMARY, strokeWidth="1.5", rx="6")
    t = ET.SubElement(svg, "text", x="400", y="502", fill=C_DARK,
                      fontSize="12", fontWeight="bold", textAnchor="middle",
                      fontFamily="sans-serif")
    t.text = "Что такое искусство сегодня?"
    concepts = [
        "• Границы расширились: от холста до виртуального пространства",
        "• Идея и концепт могут быть важнее мастерства исполнения",
        "• Зритель становится соавтором произведения"
    ]
    for i, c in enumerate(concepts):
        t = ET.SubElement(svg, "text", x="120", y=str(520 + i * 14), fill=C_TEXT2,
                          fontSize="10", fontFamily="sans-serif")
        t.text = escape_xml(c)

    add_footer(svg)
    return svg


# =====================================================================
# MAIN: Generate all SVGs and validate
# =====================================================================
def main():
    generators = [
        lesson_1, lesson_2, lesson_3, lesson_4, lesson_5, lesson_6,
        lesson_7, lesson_8, lesson_9, lesson_10, lesson_11, lesson_12,
    ]

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    results = []
    for i, gen in enumerate(generators, 1):
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{i}.svg")
        try:
            svg_elem = gen()
            tree = ET.ElementTree(svg_elem)
            ET.indent(tree, space="  ")

            # Validate by writing and re-reading
            tree.write(filepath, encoding="unicode", xml_declaration=True)

            # Re-read and validate
            try:
                parsed = ET.parse(filepath)
                root = parsed.getroot()
                # Count elements
                elem_count = sum(1 for _ in root.iter())
                results.append((i, filepath, "OK", elem_count))
                print(f"  ✓ Lesson {i}: {filepath} ({elem_count} elements)")
            except ET.ParseError as e:
                results.append((i, filepath, f"PARSE ERROR: {e}", 0))
                print(f"  ✗ Lesson {i}: {filepath} - PARSE ERROR: {e}")

        except Exception as e:
            results.append((i, filepath, f"GENERATION ERROR: {e}", 0))
            print(f"  ✗ Lesson {i}: {filepath} - GENERATION ERROR: {e}")

    print("\n" + "=" * 60)
    print("GENERATION RESULTS")
    print("=" * 60)
    ok_count = 0
    for i, fp, status, count in results:
        symbol = "✓" if status == "OK" else "✗"
        print(f"  {symbol} Lesson {i:2d}: {status} ({count} elements)")
        if status == "OK":
            ok_count += 1

    print(f"\nTotal: {ok_count}/{len(generators)} SVG files generated and validated successfully")


if __name__ == "__main__":
    main()
