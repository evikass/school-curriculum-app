#!/usr/bin/env python3
"""Generate 8 educational SVG images for Grade 7 Ecology lessons.
Output: /home/z/my-project/school-curriculum-app/public/images/grades/7/ecology/lesson-{n}.svg
Each SVG: 800x600, Russian text, green/lime color scheme (#65A30D primary), ecological diagrams/cycles.
"""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/ecology"
W, H = 800, 600

# Color palette
PRIMARY = "#65A30D"
PRIMARY_DARK = "#4D7C0F"
PRIMARY_LIGHT = "#A3E635"
ACCENT = "#166534"
BG = "#F7FEE7"
BG_DARK = "#ECFCCB"
WHITE = "#FFFFFF"
TEXT_DARK = "#1A2E05"
TEXT_MED = "#365314"
BORDER = "#84CC16"
SKY = "#BFDBFE"
WATER = "#3B82F6"
BROWN = "#92400E"
SOIL = "#78350F"
ORANGE = "#EA580C"
RED = "#DC2626"
GRAY = "#6B7280"
LIGHT_GRAY = "#D1D5DB"

def escape_xml(text):
    """Escape special XML characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def svg_header(title):
    """Return the SVG root with namespace, viewBox, and a subtle background."""
    svg = ET.Element("svg")
    svg.set("xmlns", "http://www.w3.org/2000/svg")
    svg.set("viewBox", f"0 0 {W} {H}")
    svg.set("width", str(W))
    svg.set("height", str(H))
    # Background rect
    bg = ET.SubElement(svg, "rect")
    bg.set("width", str(W))
    bg.set("height", str(H))
    bg.set("fill", BG)
    bg.set("rx", "12")
    # Border
    border = ET.SubElement(svg, "rect")
    border.set("x", "2")
    border.set("y", "2")
    border.set("width", str(W - 4))
    border.set("height", str(H - 4))
    border.set("fill", "none")
    border.set("stroke", BORDER)
    border.set("stroke-width", "3")
    border.set("rx", "12")
    # Title bar
    tbar = ET.SubElement(svg, "rect")
    tbar.set("x", "3")
    tbar.set("y", "3")
    tbar.set("width", str(W - 6))
    tbar.set("height", "56")
    tbar.set("fill", PRIMARY)
    tbar.set("rx", "10")
    # Title text
    tt = ET.SubElement(svg, "text")
    tt.set("x", str(W // 2))
    tt.set("y", "38")
    tt.set("text-anchor", "middle")
    tt.set("fill", WHITE)
    tt.set("font-size", "22")
    tt.set("font-weight", "bold")
    tt.set("font-family", "Arial, sans-serif")
    tt.text = title
    # Decorative leaf icon
    leaf = ET.SubElement(svg, "text")
    leaf.set("x", "28")
    leaf.set("y", "40")
    leaf.set("font-size", "26")
    leaf.text = "\U0001F33F"
    leaf2 = ET.SubElement(svg, "text")
    leaf2.set("x", str(W - 48))
    leaf2.set("y", "40")
    leaf2.set("font-size", "26")
    leaf2.text = "\U0001F33F"
    return svg


def add_subtitle(svg, text, y=82):
    """Add a subtitle line below the title bar."""
    t = ET.SubElement(svg, "text")
    t.set("x", str(W // 2))
    t.set("y", str(y))
    t.set("text-anchor", "middle")
    t.set("fill", ACCENT)
    t.set("font-size", "15")
    t.set("font-style", "italic")
    t.set("font-family", "Arial, sans-serif")
    t.text = text


def add_text(svg, x, y, text, size=14, fill=TEXT_DARK, anchor="middle", bold=False, font_family="Arial, sans-serif"):
    t = ET.SubElement(svg, "text")
    t.set("x", str(x))
    t.set("y", str(y))
    t.set("text-anchor", anchor)
    t.set("fill", fill)
    t.set("font-size", str(size))
    t.set("font-family", font_family)
    if bold:
        t.set("font-weight", "bold")
    t.text = text
    return t


def add_rect(svg, x, y, w, h, fill, stroke=None, rx=8, opacity=None):
    r = ET.SubElement(svg, "rect")
    r.set("x", str(x))
    r.set("y", str(y))
    r.set("width", str(w))
    r.set("height", str(h))
    r.set("fill", fill)
    if stroke:
        r.set("stroke", stroke)
        r.set("stroke-width", "2")
    r.set("rx", str(rx))
    if opacity:
        r.set("opacity", str(opacity))
    return r


def add_circle(svg, cx, cy, r, fill, stroke=None, opacity=None):
    c = ET.SubElement(svg, "circle")
    c.set("cx", str(cx))
    c.set("cy", str(cy))
    c.set("r", str(r))
    c.set("fill", fill)
    if stroke:
        c.set("stroke", stroke)
        c.set("stroke-width", "2")
    if opacity:
        c.set("opacity", str(opacity))
    return c


def add_line(svg, x1, y1, x2, y2, stroke=PRIMARY, width=2, dash=None):
    l = ET.SubElement(svg, "line")
    l.set("x1", str(x1)); l.set("y1", str(y1))
    l.set("x2", str(x2)); l.set("y2", str(y2))
    l.set("stroke", stroke); l.set("stroke-width", str(width))
    if dash:
        l.set("stroke-dasharray", dash)
    return l


def add_arrow(svg, x1, y1, x2, y2, stroke=PRIMARY, width=2):
    """Draw a line with an arrowhead."""
    add_line(svg, x1, y1, x2, y2, stroke, width)
    # Arrowhead
    import math
    angle = math.atan2(y2 - y1, x2 - x1)
    arrow_len = 10
    arrow_angle = math.pi / 6
    ax1 = x2 - arrow_len * math.cos(angle - arrow_angle)
    ay1 = y2 - arrow_len * math.sin(angle - arrow_angle)
    ax2 = x2 - arrow_len * math.cos(angle + arrow_angle)
    ay2 = y2 - arrow_len * math.sin(angle + arrow_angle)
    poly = ET.SubElement(svg, "polygon")
    poly.set("points", f"{x2},{y2} {ax1},{ay1} {ax2},{ay2}")
    poly.set("fill", stroke)


def add_curved_arrow(svg, path_d, stroke=PRIMARY, width=2):
    """Draw a curved arrow using a path element."""
    p = ET.SubElement(svg, "path")
    p.set("d", path_d)
    p.set("fill", "none")
    p.set("stroke", stroke)
    p.set("stroke-width", str(width))
    return p


def add_rounded_box(svg, x, y, w, h, fill, stroke=None, text_lines=None, text_size=13, text_fill=WHITE, rx=10):
    """Draw a rounded rectangle with optional centered text."""
    add_rect(svg, x, y, w, h, fill, stroke, rx)
    if text_lines:
        cy = y + h // 2
        if len(text_lines) == 1:
            add_text(svg, x + w // 2, cy + 5, text_lines[0], text_size, text_fill, bold=True)
        else:
            line_h = text_size + 4
            start_y = cy - (len(text_lines) - 1) * line_h // 2 + 5
            for i, line in enumerate(text_lines):
                add_text(svg, x + w // 2, start_y + i * line_h, line, text_size, text_fill, bold=True)


# ============================================================
# LESSON 1: Предмет экологии
# ============================================================
def lesson1():
    svg = svg_header("Предмет экологии")
    add_subtitle(svg, "Экология — наука о взаимодействии организмов с окружающей средой")

    # Definition box
    add_rect(svg, 50, 100, 700, 60, "#FEF9C3", BORDER, 10)
    add_text(svg, 400, 125, "Экология (от греч. oikos — дом, logos — наука)", 14, TEXT_DARK, bold=True)
    add_text(svg, 400, 145, "наука о взаимоотношениях организмов между собой и с окружающей средой", 12, TEXT_MED)

    # Levels of ecological organization — nested rectangles (concentric)
    levels = [
        (100, 200, 600, 360, PRIMARY_LIGHT, "Биосфера", 20),
        (150, 230, 500, 300, "#BEF264", "Экосистема", 18),
        (200, 260, 400, 240, "#D9F99D", "Сообщество", 16),
        (250, 290, 300, 180, "#ECFCCB", "Популяция", 15),
        (320, 340, 160, 100, WHITE, "Организм", 14),
    ]
    for x, y, w, h, fill, label, fs in levels:
        add_rect(svg, x, y, w, h, fill, PRIMARY_DARK, 12)
        add_text(svg, x + w // 2, y + 22, label, fs, TEXT_DARK, bold=True)

    # Labels on the right pointing to each level
    labels_right = [
        (710, 230, "Биосфера — все живые организмы Земли"),
        (710, 260, "Экосистема — организм + среда"),
        (710, 290, "Сообщество — группа популяций"),
        (710, 320, "Популяция — особи одного вида"),
        (710, 350, "Организм — отдельная особь"),
    ]
    # Actually let's put descriptions at the bottom
    add_rect(svg, 40, 430, 720, 145, WHITE, BORDER, 10)
    add_text(svg, 400, 455, "Уровни организации живой природы", 15, ACCENT, bold=True)

    items = [
        ("Организм", "отдельная живая особь (дерево, волк)"),
        ("Популяция", "группа особей одного вида в одной местности"),
        ("Сообщество", "несколько популяций разных видов вместе"),
        ("Экосистема", "сообщество + неживая среда (почва, вода, свет)"),
        ("Биосфера", "все экосистемы планеты Земля"),
    ]
    for i, (level, desc) in enumerate(items):
        yy = 478 + i * 19
        add_text(svg, 70, yy, "\u2022", 13, PRIMARY, anchor="start")
        add_text(svg, 85, yy, f"{level}:", 12, TEXT_DARK, anchor="start", bold=True)
        add_text(svg, 200, yy, f"— {desc}", 12, TEXT_MED, anchor="start")

    # Small leaf decoration
    add_text(svg, 720, 570, "\U0001F333", 22)

    return svg


# ============================================================
# LESSON 2: Методы экологических исследований
# ============================================================
def lesson2():
    svg = svg_header("Методы экологических исследований")
    add_subtitle(svg, "Основные методы: наблюдение, эксперимент, моделирование, мониторинг")

    # Four method cards
    methods = [
        ("Наблюдение", "\U0001F441", PRIMARY_DARK,
         ["Изучение без вмешательства",
          "Полевые наблюдения",
          "Фенологические записи",
          "Учёт численности видов"]),
        ("Эксперимент", "\U0001F52C", "#15803D",
         ["Целенаправленное воздействие",
          "Лабораторные опыты",
          "Сравнение опытной и контрольной",
          "Повторяемость результатов"]),
        ("Моделирование", "\U0001F4BB", PRIMARY,
         ["Создание моделей экосистем",
          "Компьютерное моделирование",
          "Прогнозирование изменений",
          "Математические модели"]),
        ("Мониторинг", "\U0001F4CA", "#166534",
         ["Регулярные наблюдения",
          "Отслеживание изменений",
          "Оценка состояния среды",
          "Система предупреждений"]),
    ]

    card_w = 170
    card_h = 210
    gap = 15
    total_w = 4 * card_w + 3 * gap
    start_x = (W - total_w) // 2

    for i, (title, icon, color, items) in enumerate(methods):
        x = start_x + i * (card_w + gap)
        y = 100
        # Card background
        add_rect(svg, x, y, card_w, card_h, WHITE, color, 10)
        # Icon circle
        add_circle(svg, x + card_w // 2, y + 40, 28, color)
        add_text(svg, x + card_w // 2, y + 48, icon, 24, WHITE)
        # Title
        add_text(svg, x + card_w // 2, y + 85, title, 14, color, bold=True)
        # Items
        for j, item in enumerate(items):
            add_text(svg, x + card_w // 2, y + 110 + j * 22, item, 10, TEXT_MED)

    # Bottom: process flow
    add_rect(svg, 40, 335, 720, 55, WHITE, BORDER, 10)
    add_text(svg, 400, 358, "Последовательность экологического исследования:", 14, ACCENT, bold=True)
    add_text(svg, 400, 378, "Наблюдение \u2192 Гипотеза \u2192 Эксперимент \u2192 Анализ \u2192 Моделирование \u2192 Мониторинг", 13, TEXT_DARK)

    # Example: ecological monitoring diagram
    add_rect(svg, 40, 405, 720, 170, WHITE, BORDER, 10)
    add_text(svg, 400, 430, "Пример: Мониторинг загрязнения водоёма", 14, ACCENT, bold=True)

    # Water body
    add_rect(svg, 60, 450, 250, 110, "#DBEAFE", "#3B82F6", 10)
    add_text(svg, 185, 480, "\U0001F30A", 30)
    add_text(svg, 185, 510, "Водоём", 13, "#1E40AF", bold=True)
    add_text(svg, 185, 528, "Отбор проб воды", 11, TEXT_MED)

    # Arrow
    add_arrow(svg, 320, 505, 370, 505, PRIMARY, 3)

    # Lab analysis
    add_rect(svg, 380, 450, 160, 110, "#DCFCE7", PRIMARY, 10)
    add_text(svg, 460, 480, "\U0001F9EA", 28)
    add_text(svg, 460, 510, "Лаборатория", 13, TEXT_DARK, bold=True)
    add_text(svg, 460, 528, "Анализ проб", 11, TEXT_MED)

    # Arrow
    add_arrow(svg, 550, 505, 600, 505, PRIMARY, 3)

    # Report
    add_rect(svg, 610, 450, 130, 110, "#FEF9C3", ORANGE, 10)
    add_text(svg, 675, 480, "\U0001F4CB", 28)
    add_text(svg, 675, 510, "Отчёт", 13, TEXT_DARK, bold=True)
    add_text(svg, 675, 528, "Выводы и меры", 11, TEXT_MED)

    return svg


# ============================================================
# LESSON 3: Классификация экологических факторов
# ============================================================
def lesson3():
    svg = svg_header("Классификация экологических факторов")
    add_subtitle(svg, "Три группы факторов: абиотические, биотические, антропогенные")

    # Three main columns
    groups = [
        ("Абиотические", PRIMARY_DARK, "#DCFCE7", [
            "Свет", "Температура", "Влажность",
            "Давление", "Ветер", "Рельеф",
            "Солёность воды", "Кислотность почвы"
        ], "\u2600"),
        ("Биотические", "#15803D", "#F0FDF4", [
            "Конкуренция", "Хищничество",
            "Симбиоз", "Паразитизм",
            "Мутуализм", "Комменсализм",
            "Аменсализм", "Протокооперация"
        ], "\U0001F43E"),
        ("Антропогенные", "#991B1B", "#FEF2F2", [
            "Загрязнение", "Вырубка лесов",
            "Осушение болот", "Урбанизация",
            "Промышленность", "Сельское хозяйство",
            "Транспорт", "Радиация"
        ], "\U0001F3ED"),
    ]

    col_w = 230
    gap = 15
    total = 3 * col_w + 2 * gap
    sx = (W - total) // 2

    for i, (title, color, bg_color, items, icon) in enumerate(groups):
        x = sx + i * (col_w + gap)
        # Column background
        add_rect(svg, x, 95, col_w, 410, bg_color, color, 12)
        # Icon
        add_text(svg, x + col_w // 2, 125, icon, 30)
        # Title
        add_text(svg, x + col_w // 2, 150, title, 16, color, bold=True)
        # Separator
        add_line(svg, x + 15, 162, x + col_w - 15, 162, color, 1)
        # Items
        for j, item in enumerate(items):
            yy = 182 + j * 28
            add_rect(svg, x + 15, yy - 12, col_w - 30, 24, WHITE, color, 6, "0.8")
            add_text(svg, x + col_w // 2, yy + 3, item, 12, TEXT_DARK)

    # Bottom: key concept
    add_rect(svg, 40, 520, 720, 55, WHITE, BORDER, 10)
    add_text(svg, 400, 542, "Важно: факторы действуют совместно!", 15, ACCENT, bold=True)
    add_text(svg, 400, 562, "Организм испытывает одновременное влияние абиотических, биотических и антропогенных факторов", 11, TEXT_MED)

    return svg


# ============================================================
# LESSON 4: Свет и температура как факторы
# ============================================================
def lesson4():
    svg = svg_header("Свет и температура как экологические факторы")
    add_subtitle(svg, "Фотопериодизм, адаптации к свету и температуре")

    # LEFT SECTION: Light
    add_rect(svg, 30, 95, 370, 245, WHITE, PRIMARY, 10)
    add_text(svg, 215, 118, "\u2600 Свет как фактор", 15, PRIMARY_DARK, bold=True)

    # Sun
    add_circle(svg, 120, 170, 30, "#FCD34D", "#F59E0B")
    # Sun rays
    for angle_deg in range(0, 360, 45):
        import math
        angle = math.radians(angle_deg)
        x1 = 120 + 35 * math.cos(angle)
        y1 = 170 + 35 * math.sin(angle)
        x2 = 120 + 45 * math.cos(angle)
        y2 = 170 + 45 * math.sin(angle)
        add_line(svg, int(x1), int(y1), int(x2), int(y2), "#F59E0B", 2)

    # Light-dependent items
    light_items = [
        "Фотосинтез — основа жизни",
        "Фотопериод — длина дня",
        "Светолюбивые (гелиофиты)",
        "Тенелюбивые (сциофиты)",
        "Теневыносливые растения",
    ]
    for j, item in enumerate(light_items):
        add_text(svg, 250, 162 + j * 22, item, 12, TEXT_DARK, anchor="start")

    # Photoperiod diagram
    add_text(svg, 215, 290, "Фотопериодизм:", 12, ACCENT, bold=True)
    # Day/night bar
    add_rect(svg, 60, 300, 180, 18, "#FEF08A", "#F59E0B", 4)  # day
    add_text(svg, 150, 314, "День (свет)", 10, TEXT_DARK)
    add_rect(svg, 240, 300, 120, 18, "#1E293B", "#475569", 4)  # night
    add_text(svg, 300, 314, "Ночь", 10, WHITE)
    add_text(svg, 215, 330, "Долгий день \u2192 цветение; Короткий день \u2192 покой", 10, TEXT_MED)

    # RIGHT SECTION: Temperature
    add_rect(svg, 410, 95, 370, 245, WHITE, "#DC2626", 10)
    add_text(svg, 595, 118, "\U0001F321 Температура", 15, "#DC2626", bold=True)

    # Thermometer
    add_rect(svg, 450, 140, 16, 100, "#FEE2E2", "#EF4444", 4)
    add_circle(svg, 458, 250, 14, "#EF4444", "#DC2626")
    add_rect(svg, 453, 180, 10, 70, "#EF4444")
    # Temperature marks
    add_text(svg, 445, 158, "40\u00b0", 9, "#DC2626", anchor="end")
    add_text(svg, 445, 200, "20\u00b0", 9, "#DC2626", anchor="end")
    add_text(svg, 445, 235, "0\u00b0", 9, "#DC2626", anchor="end")

    temp_items = [
        "Оптимум — лучшие условия",
        "Предел выносливости",
        "Эвритермные (широкий диапазон)",
        "Стенотермные (узкий диапазон)",
        "Правило оптимума",
    ]
    for j, item in enumerate(temp_items):
        add_text(svg, 490, 162 + j * 22, item, 12, TEXT_DARK, anchor="start")

    # Temperature optimum curve (simplified)
    add_text(svg, 595, 290, "Кривая выноживания:", 12, ACCENT, bold=True)
    # Axes
    add_line(svg, 460, 330, 460, 295, GRAY, 1)
    add_line(svg, 460, 330, 750, 330, GRAY, 1)
    add_text(svg, 455, 295, "Ж", 9, GRAY, anchor="end")
    add_text(svg, 750, 340, "t\u00b0C", 9, GRAY)
    # Bell curve approximation using a path
    add_curved_arrow(svg, "M470,328 Q510,295 560,298 Q600,300 640,298 Q690,295 730,328", "#DC2626", 2)
    # Optimum zone
    add_rect(svg, 570, 298, 80, 32, "#FEF08A", "none", 0, "0.3")
    add_text(svg, 610, 345, "оптимум", 9, "#DC2626")

    # BOTTOM: Adaptations
    add_rect(svg, 30, 355, 740, 60, "#FEF9C3", BORDER, 10)
    add_text(svg, 400, 378, "Адаптации к экстремальным температурам:", 14, ACCENT, bold=True)
    add_text(svg, 400, 398, "Холод: мех, спячка, миграция | Жара: потоотделение, ночная активность, восковой налёт", 11, TEXT_MED)

    # Animal examples
    add_rect(svg, 30, 425, 355, 150, WHITE, PRIMARY, 10)
    add_text(svg, 207, 448, "\U0001F428 Адаптации к холоду", 13, PRIMARY_DARK, bold=True)
    cold_items = [
        "Толстый мех и подкожный жир",
        "Спячка (медведь, сурок)",
        "Миграция (птицы на юг)",
        "Группирование (пингвины)",
        "Мелкие уши (песец)",
    ]
    for j, item in enumerate(cold_items):
        add_text(svg, 55, 470 + j * 20, item, 11, TEXT_DARK, anchor="start")

    add_rect(svg, 415, 425, 355, 150, WHITE, "#DC2626", 10)
    add_text(svg, 592, 448, "\U0001F406 Адаптации к жаре", 13, "#DC2626", bold=True)
    hot_items = [
        "Ночная активность (тушканчик)",
        "Длинные уши (фенек)",
        "Тонкая шерсть (верблюд)",
        "Потоотделение (человек)",
        "Восковой налёт (кактус)",
    ]
    for j, item in enumerate(hot_items):
        add_text(svg, 440, 470 + j * 20, item, 11, TEXT_DARK, anchor="start")

    return svg


# ============================================================
# LESSON 5: Понятие экосистемы
# ============================================================
def lesson5():
    svg = svg_header("Понятие экосистемы")
    add_subtitle(svg, "Экосистема = биоценоз + биотоп (живые + неживые компоненты)")

    # Main ecosystem diagram
    # Central circle: Ecosystem
    add_circle(svg, 400, 300, 180, "#DCFCE7", PRIMARY, 3)
    add_text(svg, 400, 230, "Экосистема", 18, PRIMARY_DARK, bold=True)

    # Biotic part (left)
    add_ellipse(svg, 280, 310, 110, 80, "#BBF7D0", "#15803D")
    add_text(svg, 280, 305, "Биоценоз", 14, "#15803D", bold=True)
    add_text(svg, 280, 322, "(живые)", 11, TEXT_MED)

    # Abiotic part (right)
    add_ellipse(svg, 520, 310, 110, 80, "#DBEAFE", "#3B82F6")
    add_text(svg, 520, 305, "Биотоп", 14, "#3B82F6", bold=True)
    add_text(svg, 520, 322, "(неживые)", 11, TEXT_MED)

    # Components of biocenosis
    add_text(svg, 280, 350, "Продуценты", 10, "#15803D")
    add_text(svg, 280, 363, "Консументы", 10, "#15803D")
    add_text(svg, 280, 376, "Редуценты", 10, "#15803D")

    # Components of biotope
    add_text(svg, 520, 350, "Свет, температура", 10, "#3B82F6")
    add_text(svg, 520, 363, "Вода, воздух", 10, "#3B82F6")
    add_text(svg, 520, 376, "Почва, минералы", 10, "#3B82F6")

    # Three roles box at bottom
    y_base = 430
    # Producers
    add_rect(svg, 40, y_base, 230, 140, "#DCFCE7", PRIMARY, 10)
    add_text(svg, 155, y_base + 22, "\U0001F33F Продуценты", 14, PRIMARY_DARK, bold=True)
    add_text(svg, 155, y_base + 42, "(производители)", 11, TEXT_MED)
    add_text(svg, 155, y_base + 62, "Растения, водоросли", 12, TEXT_DARK)
    add_text(svg, 155, y_base + 80, "Создают органику из", 11, TEXT_MED)
    add_text(svg, 155, y_base + 95, "CO\u2082 + H\u2082O + свет", 11, TEXT_MED)
    add_text(svg, 155, y_base + 112, "Фотосинтез!", 12, PRIMARY_DARK, bold=True)

    # Consumers
    add_rect(svg, 285, y_base, 230, 140, "#FEF9C3", ORANGE, 10)
    add_text(svg, 400, y_base + 22, "\U0001F43E Консументы", 14, ORANGE, bold=True)
    add_text(svg, 400, y_base + 42, "(потребители)", 11, TEXT_MED)
    add_text(svg, 400, y_base + 62, "Животные, человек", 12, TEXT_DARK)
    add_text(svg, 400, y_base + 80, "I порядка — травоядные", 11, TEXT_MED)
    add_text(svg, 400, y_base + 95, "II порядка — хищники", 11, TEXT_MED)
    add_text(svg, 400, y_base + 112, "III порядка — сверххищники", 11, TEXT_MED)

    # Decomposers
    add_rect(svg, 530, y_base, 230, 140, "#FEE2E2", "#991B1B", 10)
    add_text(svg, 645, y_base + 22, "\U0001F9EA Редуценты", 14, "#991B1B", bold=True)
    add_text(svg, 645, y_base + 42, "(разрушители)", 11, TEXT_MED)
    add_text(svg, 645, y_base + 62, "Бактерии, грибы", 12, TEXT_DARK)
    add_text(svg, 645, y_base + 80, "Разлагают органику до", 11, TEXT_MED)
    add_text(svg, 645, y_base + 95, "неорганических веществ", 11, TEXT_MED)
    add_text(svg, 645, y_base + 112, "Замыкают круговорот!", 12, "#991B1B", bold=True)

    # Arrows between the three
    add_arrow(svg, 270, y_base + 70, 285, y_base + 70, PRIMARY, 2)
    add_arrow(svg, 515, y_base + 70, 530, y_base + 70, ORANGE, 2)

    return svg


def add_ellipse(svg, cx, cy, rx, ry, fill, stroke):
    e = ET.SubElement(svg, "ellipse")
    e.set("cx", str(cx))
    e.set("cy", str(cy))
    e.set("rx", str(rx))
    e.set("ry", str(ry))
    e.set("fill", fill)
    e.set("stroke", stroke)
    e.set("stroke-width", "2")
    return e


# ============================================================
# LESSON 6: Пищевые цепи и сети
# ============================================================
def lesson6():
    svg = svg_header("Пищевые цепи и сети")
    add_subtitle(svg, "Трофические уровни, поток энергии, экологические пирамиды")

    # Food chain
    add_rect(svg, 30, 95, 740, 120, WHITE, BORDER, 10)
    add_text(svg, 400, 115, "Пищевая цепь (цепь питания)", 14, ACCENT, bold=True)

    # Chain: Grass -> Rabbit -> Fox -> Eagle
    chain = [
        ("\U0001F33F", "Трава", "Продуцент", PRIMARY_DARK),
        ("\U0001F407", "Заяц", "Консумент I", "#15803D"),
        ("\U0001F98A", "Лиса", "Консумент II", ORANGE),
        ("\U0001F985", "Орёл", "Консумент III", RED),
    ]
    ch_w = 150
    ch_gap = 20
    ch_total = len(chain) * ch_w + (len(chain) - 1) * ch_gap
    ch_sx = (W - ch_total) // 2

    for i, (icon, name, role, color) in enumerate(chain):
        x = ch_sx + i * (ch_w + ch_gap) + ch_w // 2
        add_circle(svg, x, 155, 25, color)
        add_text(svg, x, 163, icon, 22, WHITE)
        add_text(svg, x, 192, name, 12, TEXT_DARK, bold=True)
        add_text(svg, x, 206, role, 10, color)
        if i < len(chain) - 1:
            ax = ch_sx + (i + 1) * (ch_w + ch_gap) - ch_gap // 2
            add_arrow(svg, x + 28, 155, ax, 155, PRIMARY, 2)

    # Energy flow
    add_rect(svg, 30, 225, 740, 55, "#FEF9C3", BORDER, 10)
    add_text(svg, 400, 248, "Поток энергии: Солнце \u2192 Продуценты \u2192 Консументы I \u2192 Консументы II \u2192 Консументы III \u2192 Редуценты", 12, TEXT_DARK)
    add_text(svg, 400, 268, "На каждом уровне теряется ~90% энергии (правило 10%)", 11, RED)

    # Food web
    add_rect(svg, 30, 290, 380, 280, WHITE, BORDER, 10)
    add_text(svg, 220, 312, "Пищевая сеть", 14, ACCENT, bold=True)

    # Web nodes
    web_producers = [("Растения", 120, 350, PRIMARY), ("Водоросли", 300, 350, PRIMARY)]
    web_cons1 = [("Заяц", 80, 410, "#15803D"), ("Мышь", 200, 410, "#15803D"), ("Рыба", 320, 410, "#15803D")]
    web_cons2 = [("Лиса", 120, 470, ORANGE), ("Сова", 280, 470, ORANGE)]
    web_cons3 = [("Орёл", 200, 530, RED)]

    all_nodes = web_producers + web_cons1 + web_cons2 + web_cons3
    for name, x, y, color in all_nodes:
        add_rounded_box(svg, x - 40, y - 14, 80, 28, color, text_lines=[name], text_size=10)

    # Web connections (simplified lines)
    web_lines = [
        (120, 364, 80, 396), (120, 364, 200, 396),
        (300, 364, 320, 396), (300, 364, 200, 396),
        (80, 424, 120, 456), (200, 424, 120, 456),
        (200, 424, 280, 456), (320, 424, 280, 456),
        (120, 484, 200, 516), (280, 484, 200, 516),
    ]
    for x1, y1, x2, y2 in web_lines:
        add_line(svg, x1, y1, x2, y2, LIGHT_GRAY, 1)

    # Ecological pyramid
    add_rect(svg, 420, 290, 360, 280, WHITE, BORDER, 10)
    add_text(svg, 600, 312, "Экологическая пирамида", 14, ACCENT, bold=True)

    # Pyramid tiers (inverted trapezoids simplified as rectangles)
    pyr = [
        (480, 330, 240, 40, "#FEF9C3", "Продуценты (1000 кДж)", "#15803D"),
        (510, 375, 180, 40, "#FED7AA", "Консументы I (100 кДж)", ORANGE),
        (540, 420, 120, 40, "#FECACA", "Консументы II (10 кДж)", RED),
        (570, 465, 60, 40, "#F3E8FF", "Конс. III (1 кДж)", "#7C3AED"),
    ]
    for x, y, w, h, fill, label, color in pyr:
        add_rect(svg, x, y, w, h, fill, color, 4)
        add_text(svg, x + w // 2, y + h // 2 + 5, label, 9, color, bold=True)

    # Pyramid side labels
    add_text(svg, 600, 520, "Правило 10%: на каждый", 11, TEXT_MED)
    add_text(svg, 600, 535, "следующий уровень переходит", 11, TEXT_MED)
    add_text(svg, 600, 550, "~10% энергии предыдущего", 11, TEXT_MED)

    return svg


# ============================================================
# LESSON 7: Круговорот воды и углерода
# ============================================================
def lesson7():
    svg = svg_header("Круговорот воды и углерода")
    add_subtitle(svg, "Глобальные циклы веществ в биосфере")

    # LEFT: Water cycle
    add_rect(svg, 25, 92, 380, 495, WHITE, "#3B82F6", 10)
    add_text(svg, 215, 112, "\U0001F4A7 Круговорот воды", 14, "#1E40AF", bold=True)

    # Mountain/hill
    add_curved_arrow(svg, "M60,450 Q60,350 100,300 Q140,250 180,280 Q220,310 250,350 Q280,380 300,450", "#84CC16", 2)
    add_rect(svg, 50, 450, 330, 100, "#DBEAFE", "#3B82F6", 0)
    add_text(svg, 215, 490, "\U0001F30A Океан", 14, "#1E40AF", bold=True)

    # Evaporation arrow
    add_arrow(svg, 200, 450, 200, 350, "#3B82F6", 2)
    add_text(svg, 150, 400, "Испарение", 10, "#3B82F6", anchor="end")

    # Cloud
    add_ellipse(svg, 200, 320, 50, 25, WHITE, "#94A3B8")
    add_ellipse(svg, 185, 325, 30, 20, WHITE, "#94A3B8")
    add_ellipse(svg, 220, 325, 35, 22, WHITE, "#94A3B8")
    add_text(svg, 200, 298, "\u2601 Облако", 10, "#475569")

    # Rain
    add_arrow(svg, 130, 345, 100, 400, "#3B82F6", 2)
    add_text(svg, 80, 380, "Осадки", 10, "#3B82F6", anchor="end")

    # Infiltration
    add_arrow(svg, 300, 450, 320, 500, "#3B82F6", 1, )
    add_text(svg, 340, 480, "Инфильтрация", 9, "#3B82F6", anchor="start")

    # Runoff
    add_arrow(svg, 100, 400, 150, 450, "#3B82F6", 2)
    add_text(svg, 80, 430, "Сток", 10, "#3B82F6", anchor="end")

    # Transpiration
    add_arrow(svg, 280, 380, 280, 320, "#22C55E", 2)
    add_text(svg, 300, 350, "Транспирация", 9, "#22C55E", anchor="start")

    # Tree
    add_rect(svg, 260, 380, 30, 70, BROWN, "none", 0)
    add_circle(svg, 275, 360, 25, "#22C55E", "#15803D")

    # Underground water
    add_text(svg, 215, 530, "\U0001F4A7 Подземные воды", 10, "#3B82F6")

    # Key processes box
    add_rect(svg, 35, 540, 360, 38, "#EFF6FF", "#3B82F6", 6)
    add_text(svg, 215, 563, "Испарение \u2192 Конденсация \u2192 Осадки \u2192 Сток", 10, "#1E40AF", bold=True)

    # RIGHT: Carbon cycle
    add_rect(svg, 415, 92, 365, 495, WHITE, "#65A30D", 10)
    add_text(svg, 597, 112, "\u2623 Круговорот углерода", 14, PRIMARY_DARK, bold=True)

    # Atmosphere CO2
    add_ellipse(svg, 597, 175, 90, 40, "#DBEAFE", "#3B82F6")
    add_text(svg, 597, 172, "CO\u2082 в атмосфере", 11, "#1E40AF", bold=True)

    # Photosynthesis arrow (down to plant)
    add_arrow(svg, 555, 215, 510, 260, "#22C55E", 2)
    add_text(svg, 510, 240, "Фотосинтез", 9, "#22C55E", anchor="end")

    # Plant
    add_circle(svg, 500, 290, 30, "#86EFAC", "#22C55E")
    add_text(svg, 500, 294, "\U0001F33F", 22, WHITE)
    add_text(svg, 500, 330, "Растения", 10, "#15803D", bold=True)

    # Respiration arrow (up from plant)
    add_arrow(svg, 530, 270, 560, 210, ORANGE, 2)
    add_text(svg, 565, 245, "Дыхание", 9, ORANGE, anchor="start")

    # Animal consumption arrow
    add_arrow(svg, 535, 290, 600, 290, PRIMARY, 2)
    add_text(svg, 570, 282, "Поедание", 9, TEXT_MED)

    # Animal
    add_circle(svg, 650, 290, 30, "#FED7AA", ORANGE)
    add_text(svg, 650, 295, "\U0001F43E", 22, WHITE)
    add_text(svg, 650, 330, "Животные", 10, ORANGE, bold=True)

    # Animal respiration
    add_arrow(svg, 640, 260, 610, 210, ORANGE, 2)
    add_text(svg, 635, 230, "Дыхание", 9, ORANGE, anchor="end")

    # Decomposition arrow
    add_arrow(svg, 650, 320, 660, 380, "#991B1B", 2)
    add_text(svg, 680, 350, "Отмирание", 9, "#991B1B", anchor="start")

    # Decomposers
    add_ellipse(svg, 600, 410, 70, 30, "#FEE2E2", "#991B1B")
    add_text(svg, 600, 414, "Редуценты", 10, "#991B1B", bold=True)

    # Decomposition to CO2
    add_arrow(svg, 560, 400, 540, 215, "#991B1B", 2)
    add_text(svg, 530, 310, "Разложение", 9, "#991B1B", anchor="end", )

    # Fossil fuels
    add_rect(svg, 520, 460, 140, 50, SOIL, "#78350F", 8)
    add_text(svg, 590, 480, "\u26FD Ископаемое", 10, WHITE, bold=True)
    add_text(svg, 590, 495, "топливо", 10, WHITE)

    # Fossil fuel burning
    add_arrow(svg, 600, 460, 597, 220, "#DC2626", 2)
    add_text(svg, 625, 370, "Сжигание", 9, "#DC2626", anchor="start")

    # Key processes box
    add_rect(svg, 425, 540, 345, 38, "#F0FDF4", PRIMARY, 6)
    add_text(svg, 597, 563, "Фотосинтез \u2192 Дыхание \u2192 Разложение \u2192 Сжигание", 10, PRIMARY_DARK, bold=True)

    return svg


# ============================================================
# LESSON 8: Круговорот кислорода и азота
# ============================================================
def lesson8():
    svg = svg_header("Круговорот кислорода и азота")
    add_subtitle(svg, "Азотфиксация, нитрификация, денитрификация, кислородный цикл")

    # LEFT: Oxygen cycle
    add_rect(svg, 25, 92, 380, 245, WHITE, "#0EA5E9", 10)
    add_text(svg, 215, 112, "\U0001F52D Круговорот кислорода", 14, "#0369A1", bold=True)

    # Atmosphere O2
    add_ellipse(svg, 215, 165, 100, 35, "#E0F2FE", "#0EA5E9")
    add_text(svg, 215, 168, "O\u2082 в атмосфере (21%)", 11, "#0369A1", bold=True)

    # Photosynthesis down
    add_arrow(svg, 175, 200, 140, 240, "#22C55E", 2)
    add_text(svg, 120, 222, "Фотосинтез", 10, "#22C55E", anchor="end")

    # Plant
    add_circle(svg, 140, 270, 28, "#86EFAC", "#22C55E")
    add_text(svg, 140, 275, "\U0001F33F", 20, WHITE)
    add_text(svg, 140, 310, "Растения", 10, "#15803D")

    # Respiration up
    add_arrow(svg, 170, 255, 200, 200, ORANGE, 2)
    add_text(svg, 215, 225, "Дыхание", 10, ORANGE, anchor="start")

    # Ozone layer
    add_rect(svg, 60, 145, 310, 14, "#E0E7FF", "#818CF8", 4)
    add_text(svg, 215, 155, "Озоновый слой (O\u2083) — защита от УФ", 8, "#4338CA")

    # Water splitting
    add_text(svg, 315, 275, "O\u2082 из воды", 9, "#0369A1", anchor="start")
    add_text(svg, 315, 290, "при фотосинтезе:", 9, "#0369A1", anchor="start")
    add_text(svg, 315, 305, "2H\u2082O \u2192 O\u2082 + 4H", 9, "#0369A1", anchor="start")

    # Right: Nitrogen cycle
    add_rect(svg, 415, 92, 365, 495, WHITE, "#7C3AED", 10)
    add_text(svg, 597, 112, "\U0001F9EA Круговорот азота", 14, "#6D28D9", bold=True)

    # Atmosphere N2
    add_ellipse(svg, 597, 160, 100, 35, "#EDE9FE", "#7C3AED")
    add_text(svg, 597, 163, "N\u2082 в атмосфере (78%)", 11, "#6D28D9", bold=True)

    # Nitrogen fixation
    add_arrow(svg, 555, 195, 500, 225, "#7C3AED", 2)
    add_text(svg, 510, 205, "Азотфиксация", 9, "#6D28D9", anchor="end")

    # Bacteria node
    add_ellipse(svg, 470, 240, 55, 22, "#DDD6FE", "#7C3AED")
    add_text(svg, 470, 244, "Клубеньковые", 9, "#6D28D9")
    add_text(svg, 470, 256, "бактерии", 9, "#6D28D9")

    # NH3 / NH4+
    add_rect(svg, 440, 280, 80, 30, "#F5F3FF", "#7C3AED", 8)
    add_text(svg, 480, 300, "NH\u2084\u207a", 12, "#6D28D9", bold=True)

    # Arrow: fixation to NH4
    add_arrow(svg, 470, 262, 470, 280, "#7C3AED", 2)

    # Nitrification
    add_arrow(svg, 520, 295, 560, 295, "#7C3AED", 2)
    add_text(svg, 540, 288, "Нитрификация", 9, "#6D28D9")

    # NO2-
    add_rect(svg, 560, 280, 60, 30, "#F5F3FF", "#7C3AED", 8)
    add_text(svg, 590, 300, "NO\u2082\u207b", 12, "#6D28D9", bold=True)

    # NO3-
    add_arrow(svg, 620, 295, 660, 295, "#7C3AED", 2)
    add_rect(svg, 660, 280, 60, 30, "#F5F3FF", "#7C3AED", 8)
    add_text(svg, 690, 300, "NO\u2083\u207b", 12, "#6D28D9", bold=True)

    # Plant uptake
    add_arrow(svg, 690, 310, 690, 340, "#22C55E", 2)
    add_text(svg, 720, 330, "Усвоение", 9, "#22C55E", anchor="start")

    # Plant
    add_circle(svg, 680, 370, 25, "#86EFAC", "#22C55E")
    add_text(svg, 680, 374, "\U0001F33F", 18, WHITE)

    # Animal
    add_arrow(svg, 705, 370, 730, 370, PRIMARY, 2)
    add_circle(svg, 750, 370, 20, "#FED7AA", ORANGE)
    add_text(svg, 750, 374, "\U0001F43E", 15, WHITE)

    # Death/decomposition
    add_arrow(svg, 750, 390, 720, 430, "#991B1B", 2)
    add_text(svg, 755, 415, "Отмирание", 8, "#991B1B", anchor="start")

    # Decomposers
    add_ellipse(svg, 660, 445, 60, 22, "#FEE2E2", "#991B1B")
    add_text(svg, 660, 448, "Редуценты", 9, "#991B1B")

    # Back to NH4
    add_arrow(svg, 620, 440, 530, 310, "#991B1B", 2)
    add_text(svg, 560, 380, "Аммонификация", 9, "#991B1B", anchor="end")

    # Denitrification
    add_arrow(svg, 460, 310, 430, 360, "#DC2626", 2)
    add_text(svg, 420, 340, "Денитрификация", 9, "#DC2626", anchor="end")

    # Denitrifying bacteria
    add_ellipse(svg, 440, 380, 60, 22, "#FEE2E2", "#DC2626")
    add_text(svg, 440, 383, "N\u2082 \u2191 атмосфера", 9, "#DC2626")

    # Arrow back to atmosphere
    add_arrow(svg, 470, 360, 530, 195, "#DC2626", 2)

    # Bottom: Summary table
    add_rect(svg, 25, 345, 380, 245, WHITE, "#0EA5E9", 10)
    add_text(svg, 215, 365, "Ключевые процессы:", 13, "#0369A1", bold=True)

    oxy_processes = [
        ("Фотосинтез", "CO\u2082 + H\u2082O \u2192 глюкоза + O\u2082"),
        ("Дыхание", "Глюкоза + O\u2082 \u2192 CO\u2082 + H\u2082O"),
        ("Озонообразование", "3O\u2082 \u2192 2O\u2083 (в стратосфере)"),
        ("Источники O\u2082", "Растения, фитопланктон"),
        ("Значение", "Дыхание всех организмов"),
    ]
    for i, (name, desc) in enumerate(oxy_processes):
        yy = 390 + i * 36
        add_text(svg, 45, yy, name + ":", 11, "#0369A1", anchor="start", bold=True)
        add_text(svg, 45, yy + 15, desc, 10, TEXT_MED, anchor="start")

    # Nitrogen processes summary
    add_rect(svg, 415, 475, 365, 115, "#F5F3FF", "#7C3AED", 10)
    add_text(svg, 597, 495, "Процессы круговорота азота:", 12, "#6D28D9", bold=True)

    nit_processes = [
        ("Азотфиксация", "N\u2082 \u2192 NH\u2083 (бактерии, молнии)"),
        ("Нитрификация", "NH\u2084\u207a \u2192 NO\u2082\u207b \u2192 NO\u2083\u207b"),
        ("Аммонификация", "Органика \u2192 NH\u2084\u207a (редуценты)"),
        ("Денитрификация", "NO\u2083\u207b \u2192 N\u2082 (бактерии)"),
    ]
    for i, (name, desc) in enumerate(nit_processes):
        yy = 512 + i * 20
        add_text(svg, 430, yy, name + ":", 10, "#6D28D9", anchor="start", bold=True)
        add_text(svg, 570, yy, desc, 10, TEXT_MED, anchor="start")

    return svg


# ============================================================
# MAIN: Generate all 8 SVGs and validate
# ============================================================
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}")

    generators = [
        (1, lesson1),
        (2, lesson2),
        (3, lesson3),
        (4, lesson4),
        (5, lesson5),
        (6, lesson6),
        (7, lesson7),
        (8, lesson8),
    ]

    results = []
    for n, gen_func in generators:
        svg = gen_func()
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{n}.svg")

        # Serialize to string
        tree = ET.ElementTree(svg)
        ET.indent(tree, space="  ")

        # Write
        tree.write(filepath, encoding="unicode", xml_declaration=True)

        # Validate
        try:
            tree2 = ET.parse(filepath)
            root = tree2.getroot()
            # Check viewBox
            vb = root.get("viewBox", "")
            w_attr = root.get("width", "")
            h_attr = root.get("height", "")
            assert vb == f"0 0 {W} {H}", f"viewBox mismatch: {vb}"
            assert w_attr == str(W), f"width mismatch: {w_attr}"
            assert h_attr == str(H), f"height mismatch: {h_attr}"
            results.append((n, filepath, "OK", ""))
            print(f"  Lesson {n}: VALID - {filepath}")
        except ET.ParseError as e:
            results.append((n, filepath, "FAIL", str(e)))
            print(f"  Lesson {n}: INVALID - {e}")
        except AssertionError as e:
            results.append((n, filepath, "WARN", str(e)))
            print(f"  Lesson {n}: WARNING - {e}")

    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    ok = sum(1 for _, _, s, _ in results if s == "OK")
    fail = sum(1 for _, _, s, _ in results if s == "FAIL")
    warn = sum(1 for _, _, s, _ in results if s == "WARN")
    print(f"  OK: {ok}  |  FAIL: {fail}  |  WARN: {warn}")
    for n, fp, status, msg in results:
        status_icon = "\u2705" if status == "OK" else ("\u274C" if status == "FAIL" else "\u26A0\uFE0F")
        print(f"  {status_icon} Lesson {n}: {os.path.basename(fp)} - {status}" + (f" ({msg})" if msg else ""))

    return results


if __name__ == "__main__":
    main()
