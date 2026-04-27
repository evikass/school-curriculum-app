#!/usr/bin/env python3
"""
Generate Grade 8 Economy SVG files — 8 lessons
Output: /home/z/my-project/school-curriculum-app/public/images/grades/8/economy/lesson-{n}.svg
Each SVG: 800x600, Russian text, green/gold (#16A34A primary), diagrams, formulas
"""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/economy"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─── Color palette ─────────────────────────────────────────────
GREEN_DARK   = "#15803D"
GREEN_PRIMARY= "#16A34A"
GREEN_LIGHT  = "#22C55E"
GREEN_BG     = "#F0FDF4"
GOLD         = "#D97706"
GOLD_LIGHT   = "#F59E0B"
GOLD_BG      = "#FFFBEB"
WHITE        = "#FFFFFF"
DARK         = "#1E293B"
GRAY         = "#64748B"
LIGHT_GRAY   = "#E2E8F0"
RED_ACCENT   = "#DC2626"
BLUE_ACCENT  = "#2563EB"


def escape(text):
    """Escape text for XML safety."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


# ─── Helpers ───────────────────────────────────────────────────
def svg_root():
    """Create the base SVG element."""
    return ET.Element("svg", {
        "xmlns": "http://www.w3.org/2000/svg",
        "width": "800",
        "height": "600",
        "viewBox": "0 0 800 600",
    })


def add_defs(svg):
    """Add gradient definitions."""
    defs = ET.SubElement(svg, "defs")
    # Title gradient
    g1 = ET.SubElement(defs, "linearGradient", {"id": "titleGrad", "x1": "0%", "y1": "0%", "x2": "100%", "y2": "0%"})
    ET.SubElement(g1, "stop", {"offset": "0%", "style": f"stop-color:{GREEN_DARK}"})
    ET.SubElement(g1, "stop", {"offset": "100%", "style": f"stop-color:{GREEN_PRIMARY}"})
    # Gold gradient
    g2 = ET.SubElement(defs, "linearGradient", {"id": "goldGrad", "x1": "0%", "y1": "0%", "x2": "100%", "y2": "0%"})
    ET.SubElement(g2, "stop", {"offset": "0%", "style": f"stop-color:{GOLD}"})
    ET.SubElement(g2, "stop", {"offset": "100%", "style": f"stop-color:{GOLD_LIGHT}"})
    # Card shadow filter
    f1 = ET.SubElement(defs, "filter", {"id": "shadow", "x": "-2%", "y": "-2%", "width": "104%", "height": "104%"})
    ET.SubElement(f1, "feDropShadow", {"dx": "1", "dy": "2", "stdDeviation": "3", "flood-color": "#00000020"})
    # Background gradient
    g3 = ET.SubElement(defs, "linearGradient", {"id": "bgGrad", "x1": "0%", "y1": "0%", "x2": "0%", "y2": "100%"})
    ET.SubElement(g3, "stop", {"offset": "0%", "style": f"stop-color:{GREEN_BG}"})
    ET.SubElement(g3, "stop", {"offset": "100%", "style": f"stop-color:#DCFCE7"})
    # Accent box gradient
    g4 = ET.SubElement(defs, "linearGradient", {"id": "accentGrad", "x1": "0%", "y1": "0%", "x2": "0%", "y2": "100%"})
    ET.SubElement(g4, "stop", {"offset": "0%", "style": f"stop-color:{GOLD_BG}"})
    ET.SubElement(g4, "stop", {"offset": "100%", "style": f"stop-color:#FEF3C7"})


def add_background(svg):
    """Add background rectangle with subtle pattern."""
    ET.SubElement(svg, "rect", {"width": "800", "height": "600", "fill": "url(#bgGrad)"})
    # Subtle grid pattern
    for x in range(0, 800, 40):
        ET.SubElement(svg, "line", {"x1": str(x), "y1": "0", "x2": str(x), "y2": "600", "stroke": "#D1FAE5", "stroke-width": "0.5"})
    for y in range(0, 600, 40):
        ET.SubElement(svg, "line", {"x1": "0", "y1": str(y), "x2": "800", "y2": str(y), "stroke": "#D1FAE5", "stroke-width": "0.5"})


def add_title(svg, title, lesson_num):
    """Add title bar with lesson number."""
    # Title background
    ET.SubElement(svg, "rect", {"x": "0", "y": "0", "width": "800", "height": "70", "fill": "url(#titleGrad)"})
    # Gold accent line
    ET.SubElement(svg, "rect", {"x": "0", "y": "67", "width": "800", "height": "3", "fill": "url(#goldGrad)"})
    # Lesson badge
    ET.SubElement(svg, "circle", {"cx": "40", "cy": "35", "r": "22", "fill": GOLD})
    ET.SubElement(svg, "text", {"x": "40", "y": "42", "text-anchor": "middle", "fill": WHITE, "font-size": "18", "font-weight": "bold", "font-family": "Arial, sans-serif"}).text = str(lesson_num)
    # Title text
    ET.SubElement(svg, "text", {"x": "75", "y": "32", "fill": WHITE, "font-size": "22", "font-weight": "bold", "font-family": "Arial, sans-serif"}).text = escape(title)
    # Subtitle line
    ET.SubElement(svg, "text", {"x": "75", "y": "54", "fill": "#BBF7D0", "font-size": "13", "font-family": "Arial, sans-serif"}).text = "Экономика \u2022 8 класс"


def add_card(svg, x, y, w, h, fill=WHITE, stroke=GREEN_PRIMARY, rx=10):
    """Add a rounded card rectangle."""
    ET.SubElement(svg, "rect", {"x": str(x), "y": str(y), "width": str(w), "height": str(h), "fill": fill, "stroke": stroke, "stroke-width": "1.5", "rx": str(rx), "filter": "url(#shadow)"})


def add_text(svg, x, y, text, size=14, fill=DARK, anchor="middle", weight="normal", family="Arial, sans-serif"):
    """Add text element."""
    el = ET.SubElement(svg, "text", {"x": str(x), "y": str(y), "text-anchor": anchor, "fill": fill, "font-size": str(size), "font-weight": weight, "font-family": family})
    el.text = escape(text)
    return el


def add_arrow(svg, x1, y1, x2, y2, color=GREEN_PRIMARY, width=2):
    """Add arrow line."""
    ET.SubElement(svg, "line", {"x1": str(x1), "y1": str(y1), "x2": str(x2), "y2": str(y2), "stroke": color, "stroke-width": str(width), "marker-end": "url(#arrowhead)"})
    # Simple arrowhead triangle
    import math
    angle = math.atan2(y2 - y1, x2 - x1)
    size = 8
    ax = x2 - size * math.cos(angle - 0.4)
    ay = y2 - size * math.sin(angle - 0.4)
    bx = x2 - size * math.cos(angle + 0.4)
    by = y2 - size * math.sin(angle + 0.4)
    ET.SubElement(svg, "polygon", {"points": f"{x2},{y2} {ax},{ay} {bx},{by}", "fill": color})


def add_formula_box(svg, x, y, w, h, formula_text, label=""):
    """Add highlighted formula box."""
    ET.SubElement(svg, "rect", {"x": str(x), "y": str(y), "width": str(w), "height": str(h), "fill": "url(#accentGrad)", "stroke": GOLD, "stroke-width": "2", "rx": "8"})
    if label:
        add_text(svg, x + w // 2, y + 18, label, size=12, fill=GOLD, weight="bold")
        add_text(svg, x + w // 2, y + h // 2 + 10, formula_text, size=18, fill=DARK, weight="bold")
    else:
        add_text(svg, x + w // 2, y + h // 2 + 6, formula_text, size=18, fill=DARK, weight="bold")


def add_icon_circle(svg, cx, cy, r, icon_text, bg_color=GREEN_PRIMARY, text_color=WHITE):
    """Add circular icon with emoji/text."""
    ET.SubElement(svg, "circle", {"cx": str(cx), "cy": str(cy), "r": str(r), "fill": bg_color})
    add_text(svg, cx, cy + 6, icon_text, size=int(r * 0.9), fill=text_color, weight="bold")


# ═══════════════════════════════════════════════════════════════
# LESSON 1: Что такое экономика
# ═══════════════════════════════════════════════════════════════
def lesson1():
    svg = svg_root()
    add_defs(svg)
    add_background(svg)
    add_title(svg, "Что такое экономика", 1)

    # ── Central definition ──
    add_card(svg, 30, 85, 740, 55, fill=WHITE, stroke=GREEN_PRIMARY)
    add_text(svg, 400, 108, "Экономика — наука о выборе при ограниченных ресурсах", size=15, fill=GREEN_DARK, weight="bold")
    add_text(svg, 400, 128, "Экономика — система хозяйствования общества", size=12, fill=GRAY)

    # ── Three key concepts: Needs / Resources / Scarcity ──
    # Needs card
    add_card(svg, 30, 155, 230, 150, fill=WHITE)
    add_icon_circle(svg, 145, 185, 18, "Н", bg_color=RED_ACCENT)
    add_text(svg, 145, 215, "Потребности", size=14, fill=DARK, weight="bold")
    needs = ["Еда, одежда, жильё", "Безопасность", "Общение", "Самореализация"]
    for i, n in enumerate(needs):
        add_text(svg, 145, 240 + i * 18, n, size=11, fill=GRAY, anchor="middle")

    # Resources card
    add_card(svg, 285, 155, 230, 150, fill=WHITE)
    add_icon_circle(svg, 400, 185, 18, "Р", bg_color=BLUE_ACCENT)
    add_text(svg, 400, 215, "Ресурсы", size=14, fill=DARK, weight="bold")
    resources = ["Природные", "Трудовые", "Капитальные", "Информационные"]
    for i, r in enumerate(resources):
        add_text(svg, 400, 240 + i * 18, r, size=11, fill=GRAY, anchor="middle")

    # Scarcity card
    add_card(svg, 540, 155, 230, 150, fill=WHITE)
    add_icon_circle(svg, 655, 185, 18, "О", bg_color=GOLD)
    add_text(svg, 655, 215, "Ограниченность", size=14, fill=DARK, weight="bold")
    scarcity = ["Ресурсы ограничены", "Потребности безграничны", "Противоречие", "Необходим выбор"]
    for i, s in enumerate(scarcity):
        add_text(svg, 655, 240 + i * 18, s, size=11, fill=GRAY, anchor="middle")

    # ── Arrow flow: Needs → Scarcity → Choice ──
    add_arrow(svg, 260, 230, 285, 230, color=GOLD)
    add_arrow(svg, 515, 230, 540, 230, color=GOLD)

    # ── Economic choice triangle ──
    add_card(svg, 30, 320, 360, 145, fill=WHITE)
    add_text(svg, 210, 345, "Экономический выбор", size=14, fill=GREEN_DARK, weight="bold")
    # Triangle
    ET.SubElement(svg, "polygon", {"points": "210,365 140,445 280,445", "fill": "none", "stroke": GREEN_PRIMARY, "stroke-width": "2"})
    add_text(svg, 210, 360, "ЧТО", size=11, fill=GREEN_PRIMARY, weight="bold")
    add_text(svg, 155, 460, "КАК", size=11, fill=GREEN_PRIMARY, weight="bold")
    add_text(svg, 265, 460, "ДЛЯ КОГО", size=11, fill=GREEN_PRIMARY, weight="bold")

    # ── Maslow pyramid simplified ──
    add_card(svg, 410, 320, 360, 145, fill=WHITE)
    add_text(svg, 590, 345, "Пирамида потребностей", size=14, fill=GREEN_DARK, weight="bold")
    # Pyramid layers
    layers = [
        ("Самовыражение", 540, 355, 100, 18, "#FEF3C7"),
        ("Уважение", 525, 373, 130, 18, "#FDE68A"),
        ("Социальные", 510, 391, 160, 18, "#FCD34D"),
        ("Безопасность", 495, 409, 190, 18, "#FBBF24"),
        ("Физиологические", 480, 427, 220, 18, "#F59E0B"),
    ]
    for label, lx, ly, lw, lh, color in layers:
        ET.SubElement(svg, "rect", {"x": str(lx), "y": str(ly), "width": str(lw), "height": str(lh), "fill": color, "stroke": GOLD, "stroke-width": "0.5", "rx": "3"})
        add_text(svg, lx + lw // 2, ly + 13, label, size=10, fill=DARK, weight="bold")

    # ── Key formula box ──
    add_formula_box(svg, 30, 480, 740, 50, "Потребности > Ресурсы = Проблема выбора", "Главная проблема экономики")

    # ── Footer ──
    add_text(svg, 400, 560, "Экономика изучает: производство, распределение, обмен, потребление", size=12, fill=GRAY)

    return svg


# ═══════════════════════════════════════════════════════════════
# LESSON 2: Экономические системы
# ═══════════════════════════════════════════════════════════════
def lesson2():
    svg = svg_root()
    add_defs(svg)
    add_background(svg)
    add_title(svg, "Экономические системы", 2)

    # ── Four quadrants ──
    systems = [
        {
            "name": "Традиционная",
            "x": 30, "y": 85, "w": 370, "h": 195,
            "color": "#92400E",
            "bg": "#FEF3C7",
            "icon": "Т",
            "features": ["Обычаи и традиции", "Натуральное хозяйство", "Низкий рост", "Распределение по обычаю"],
            "examples": "Племена, общины"
        },
        {
            "name": "Командная",
            "x": 410, "y": 85, "w": 370, "h": 195,
            "color": RED_ACCENT,
            "bg": "#FEE2E2",
            "icon": "К",
            "features": ["Государственный план", "Централизованное решение", "Гос. собственность", "Нет конкуренции"],
            "examples": "СССР, Куба"
        },
        {
            "name": "Рыночная",
            "x": 30, "y": 295, "w": 370, "h": 195,
            "color": GREEN_PRIMARY,
            "bg": GREEN_BG,
            "icon": "Р",
            "features": ["Свобода выбора", "Конкуренция", "Частная собственность", "Цены формирует рынок"],
            "examples": "США, Гонконг"
        },
        {
            "name": "Смешанная",
            "x": 410, "y": 295, "w": 370, "h": 195,
            "color": BLUE_ACCENT,
            "bg": "#DBEAFE",
            "icon": "С",
            "features": ["Рынок + Государство", "Частная + Гос. собств.", "Социальные гарантии", "Регулирование"],
            "examples": "Россия, Германия"
        }
    ]

    for sys in systems:
        add_card(svg, sys["x"], sys["y"], sys["w"], sys["h"], fill=sys["bg"], stroke=sys["color"])
        # Icon + name
        add_icon_circle(svg, sys["x"] + 30, sys["y"] + 30, 18, sys["icon"], bg_color=sys["color"])
        add_text(svg, sys["x"] + 60, sys["y"] + 35, sys["name"], size=16, fill=sys["color"], anchor="start", weight="bold")
        # Features
        for i, f in enumerate(sys["features"]):
            add_text(svg, sys["x"] + 25, sys["y"] + 65 + i * 22, f, size=12, fill=DARK, anchor="start")
        # Examples
        add_text(svg, sys["x"] + 25, sys["y"] + 155, f'Пример: {sys["examples"]}', size=10, fill=GRAY, anchor="start")

    # ── Comparison scale at bottom ──
    add_card(svg, 30, 505, 740, 75, fill=WHITE)
    add_text(svg, 400, 525, "Шкала экономических систем", size=13, fill=DARK, weight="bold")
    # Scale line
    ET.SubElement(svg, "line", {"x1": "80", "y1": "555", "x2": "720", "y2": "555", "stroke": GRAY, "stroke-width": "3"})
    # Ticks
    positions = [
        (80, "Традиционная", "#92400E"),
        (290, "Командная", RED_ACCENT),
        (500, "Смешанная", BLUE_ACCENT),
        (720, "Рыночная", GREEN_PRIMARY),
    ]
    for px, label, color in positions:
        ET.SubElement(svg, "circle", {"cx": str(px), "cy": "555", "r": "6", "fill": color})
        add_text(svg, px, 575, label, size=9, fill=color, weight="bold")

    return svg


# ═══════════════════════════════════════════════════════════════
# LESSON 3: Рыночный механизм
# ═══════════════════════════════════════════════════════════════
def lesson3():
    svg = svg_root()
    add_defs(svg)
    add_background(svg)
    add_title(svg, "Рыночный механизм", 3)

    # ── Supply and Demand diagram ──
    add_card(svg, 30, 85, 400, 280, fill=WHITE)
    add_text(svg, 230, 110, "Спрос и предложение", size=15, fill=GREEN_DARK, weight="bold")

    # Axes
    ET.SubElement(svg, "line", {"x1": "100", "y1": "340", "x2": "400", "y2": "340", "stroke": DARK, "stroke-width": "2"})  # X
    ET.SubElement(svg, "line", {"x1": "100", "y1": "340", "x2": "100", "y2": "125", "stroke": DARK, "stroke-width": "2"})  # Y
    # Axis labels
    add_text(svg, 250, 360, "Количество (Q)", size=11, fill=GRAY)
    add_text(svg, 70, 230, "Цена (P)", size=11, fill=GRAY)

    # Demand curve (downward) — D
    ET.SubElement(svg, "path", {
        "d": "M120,145 Q200,200 370,310",
        "fill": "none", "stroke": RED_ACCENT, "stroke-width": "2.5"
    })
    add_text(svg, 375, 320, "D", size=16, fill=RED_ACCENT, weight="bold")

    # Supply curve (upward) — S
    ET.SubElement(svg, "path", {
        "d": "M120,310 Q200,250 370,145",
        "fill": "none", "stroke": GREEN_PRIMARY, "stroke-width": "2.5"
    })
    add_text(svg, 375, 140, "S", size=16, fill=GREEN_PRIMARY, weight="bold")

    # Equilibrium point
    eq_x, eq_y = 240, 230
    ET.SubElement(svg, "circle", {"cx": str(eq_x), "cy": str(eq_y), "r": "6", "fill": GOLD})
    add_text(svg, eq_x + 15, eq_y - 8, "E — равновесие", size=11, fill=GOLD, weight="bold", anchor="start")

    # Dashed lines to axes
    ET.SubElement(svg, "line", {"x1": str(eq_x), "y1": str(eq_y), "x2": "100", "y2": str(eq_y), "stroke": GOLD, "stroke-width": "1", "stroke-dasharray": "5,5"})
    ET.SubElement(svg, "line", {"x1": str(eq_x), "y1": str(eq_y), "x2": str(eq_x), "y2": "340", "stroke": GOLD, "stroke-width": "1", "stroke-dasharray": "5,5"})
    add_text(svg, 55, eq_y + 4, "P*", size=12, fill=GOLD, weight="bold")
    add_text(svg, eq_x, 355, "Q*", size=12, fill=GOLD, weight="bold")

    # ── Right side: Key concepts ──
    add_card(svg, 450, 85, 320, 130, fill=WHITE)
    add_text(svg, 610, 110, "Закон спроса", size=14, fill=RED_ACCENT, weight="bold")
    add_text(svg, 610, 135, "При росте цены спрос падает", size=11, fill=DARK)
    add_text(svg, 610, 155, "При снижении цены спрос растёт", size=11, fill=DARK)
    add_text(svg, 610, 180, "P \u2191 \u2192 Q \u2193   |   P \u2193 \u2192 Q \u2191", size=12, fill=RED_ACCENT, weight="bold")

    add_card(svg, 450, 230, 320, 130, fill=WHITE)
    add_text(svg, 610, 255, "Закон предложения", size=14, fill=GREEN_PRIMARY, weight="bold")
    add_text(svg, 610, 280, "При росте цены предложение растёт", size=11, fill=DARK)
    add_text(svg, 610, 300, "При снижении цены предложение падает", size=11, fill=DARK)
    add_text(svg, 610, 325, "P \u2191 \u2192 Q \u2191   |   P \u2193 \u2192 Q \u2193", size=12, fill=GREEN_PRIMARY, weight="bold")

    # ── Equilibrium box ──
    add_formula_box(svg, 30, 380, 740, 55, "P* = цена равновесия   Q* = объём равновесия", "Рыночное равновесие")

    # ── Non-equilibrium states ──
    add_card(svg, 30, 450, 355, 80, fill="#FEE2E2", stroke=RED_ACCENT)
    add_text(svg, 207, 475, "Дефицит (P < P*)", size=13, fill=RED_ACCENT, weight="bold")
    add_text(svg, 207, 498, "Спрос > Предложение", size=11, fill=DARK)
    add_text(svg, 207, 515, "Очереди, нехватка товаров", size=10, fill=GRAY)

    add_card(svg, 410, 450, 355, 80, fill=GREEN_BG, stroke=GREEN_PRIMARY)
    add_text(svg, 587, 475, "Избыток (P > P*)", size=13, fill=GREEN_PRIMARY, weight="bold")
    add_text(svg, 587, 498, "Предложение > Спрос", size=11, fill=DARK)
    add_text(svg, 587, 515, "Непроданные товары, снижение цен", size=10, fill=GRAY)

    # ── Footer ──
    add_text(svg, 400, 560, "Рыночный механизм обеспечивает саморегуляцию через цены", size=12, fill=GRAY)

    return svg


# ═══════════════════════════════════════════════════════════════
# LESSON 4: Производство и прибыль
# ═══════════════════════════════════════════════════════════════
def lesson4():
    svg = svg_root()
    add_defs(svg)
    add_background(svg)
    add_title(svg, "Производство и прибыль", 4)

    # ── Production process flow ──
    add_card(svg, 30, 85, 740, 120, fill=WHITE)
    add_text(svg, 400, 110, "Процесс производства", size=15, fill=GREEN_DARK, weight="bold")

    # Flow: Resources → Production → Goods → Market
    steps = [
        ("Ресурсы", 110, 155, "#92400E"),
        ("Производство", 280, 155, GREEN_PRIMARY),
        ("Товары/услуги", 450, 155, BLUE_ACCENT),
        ("Рынок", 620, 155, GOLD),
    ]
    for label, cx, cy, color in steps:
        ET.SubElement(svg, "rect", {"x": str(cx - 55), "y": str(cy - 18), "width": "110", "height": "36", "fill": color, "rx": "18"})
        add_text(svg, cx, cy + 5, label, size=12, fill=WHITE, weight="bold")

    # Arrows between
    for i in range(len(steps) - 1):
        add_arrow(svg, steps[i][1] + 55, steps[i][2], steps[i+1][1] - 55, steps[i+1][2], color=GRAY)

    # ── Costs breakdown ──
    add_card(svg, 30, 220, 355, 180, fill=WHITE)
    add_text(svg, 207, 245, "Издержки (затраты)", size=14, fill=DARK, weight="bold")

    costs = [
        ("Постоянные (FC)", "Не зависят от объёма", "#DC2626"),
        ("Переменные (VC)", "Зависят от объёма", "#2563EB"),
        ("Общие (TC)", "FC + VC", GREEN_PRIMARY),
    ]
    for i, (name, desc, color) in enumerate(costs):
        cy = 270 + i * 45
        ET.SubElement(svg, "rect", {"x": "50", "y": str(cy - 12), "width": "12", "height": "12", "fill": color, "rx": "2"})
        add_text(svg, 72, cy, name, size=12, fill=DARK, weight="bold", anchor="start")
        add_text(svg, 72, cy + 16, desc, size=10, fill=GRAY, anchor="start")

    # ── Revenue & Profit ──
    add_card(svg, 410, 220, 355, 180, fill=WHITE)
    add_text(svg, 587, 245, "Доход и прибыль", size=14, fill=DARK, weight="bold")

    revenue_items = [
        ("Выручка (TR)", "P \u00d7 Q", GOLD),
        ("Прибыль (Pr)", "TR - TC", GREEN_PRIMARY),
        ("Рентабельность", "Pr / TC \u00d7 100%", BLUE_ACCENT),
    ]
    for i, (name, formula, color) in enumerate(revenue_items):
        cy = 270 + i * 45
        ET.SubElement(svg, "rect", {"x": "430", "y": str(cy - 12), "width": "12", "height": "12", "fill": color, "rx": "2"})
        add_text(svg, 452, cy, name, size=12, fill=DARK, weight="bold", anchor="start")
        add_text(svg, 452, cy + 16, formula, size=11, fill=color, weight="bold", anchor="start")

    # ── Key formula boxes ──
    add_formula_box(svg, 30, 415, 240, 70, "Pr = TR - TC", "Прибыль")
    add_formula_box(svg, 285, 415, 240, 70, "TR = P \u00d7 Q", "Выручка")
    add_formula_box(svg, 540, 415, 230, 70, "TC = FC + VC", "Общие затраты")

    # ── Profit/loss scenarios ──
    add_card(svg, 30, 505, 355, 70, fill="#DCFCE7", stroke=GREEN_PRIMARY)
    add_text(svg, 207, 530, "Pr > 0 — Прибыль", size=13, fill=GREEN_DARK, weight="bold")
    add_text(svg, 207, 555, "Предприятие успешно", size=11, fill=GRAY)

    add_card(svg, 410, 505, 355, 70, fill="#FEE2E2", stroke=RED_ACCENT)
    add_text(svg, 587, 530, "Pr < 0 — Убыток", size=13, fill=RED_ACCENT, weight="bold")
    add_text(svg, 587, 555, "Необходимы изменения", size=11, fill=GRAY)

    return svg


# ═══════════════════════════════════════════════════════════════
# LESSON 5: Функции денег
# ═══════════════════════════════════════════════════════════════
def lesson5():
    svg = svg_root()
    add_defs(svg)
    add_background(svg)
    add_title(svg, "Функции денег", 5)

    # ── Central coin ──
    ET.SubElement(svg, "circle", {"cx": "400", "cy": "190", "r": "55", "fill": GOLD_LIGHT, "stroke": GOLD, "stroke-width": "3"})
    ET.SubElement(svg, "circle", {"cx": "400", "cy": "190", "r": "45", "fill": "none", "stroke": GOLD, "stroke-width": "1.5"})
    add_text(svg, 400, 185, "$", size=40, fill=GOLD, weight="bold")
    add_text(svg, 400, 205, "ДЕНЬГИ", size=10, fill=GOLD, weight="bold")

    # ── Five functions as cards around the coin ──
    functions = [
        {
            "name": "Мера стоимости",
            "desc": "Деньги измеряют\nценность товаров",
            "icon": "М",
            "x": 30, "y": 85, "w": 180, "h": 130,
            "color": GREEN_PRIMARY, "bg": GREEN_BG
        },
        {
            "name": "Средство обращения",
            "desc": "Деньги — посредник\nпри обмене (Т-Д-Т)",
            "icon": "О",
            "x": 590, "y": 85, "w": 180, "h": 130,
            "color": BLUE_ACCENT, "bg": "#DBEAFE"
        },
        {
            "name": "Средство сбережения",
            "desc": "Деньги сохраняют\nценность во времени",
            "icon": "С",
            "x": 30, "y": 260, "w": 180, "h": 130,
            "color": GOLD, "bg": GOLD_BG
        },
        {
            "name": "Средство платежа",
            "desc": "Оплата налогов,\nзарплата, кредиты",
            "icon": "П",
            "x": 590, "y": 260, "w": 180, "h": 130,
            "color": RED_ACCENT, "bg": "#FEE2E2"
        },
        {
            "name": "Мировые деньги",
            "desc": "Международные\nрасчёты, валюта",
            "icon": "В",
            "x": 300, "y": 310, "w": 200, "h": 90,
            "color": "#7C3AED", "bg": "#EDE9FE"
        },
    ]

    for func in functions:
        add_card(svg, func["x"], func["y"], func["w"], func["h"], fill=func["bg"], stroke=func["color"])
        add_icon_circle(svg, func["x"] + 28, func["y"] + 28, 16, func["icon"], bg_color=func["color"])
        add_text(svg, func["x"] + 52, func["y"] + 33, func["name"], size=12, fill=func["color"], weight="bold", anchor="start")
        lines = func["desc"].split("\n")
        for i, line in enumerate(lines):
            add_text(svg, func["x"] + 18, func["y"] + 60 + i * 18, line, size=10, fill=DARK, anchor="start")

    # ── Types of money ──
    add_card(svg, 30, 420, 740, 80, fill=WHITE)
    add_text(svg, 400, 445, "Эволюция форм денег", size=14, fill=DARK, weight="bold")
    money_forms = [
        ("Товарные", 100, "#92400E"),
        ("Металлические", 250, GRAY),
        ("Бумажные", 400, BLUE_ACCENT),
        ("Электронные", 550, GREEN_PRIMARY),
        ("Крипто", 700, "#7C3AED"),
    ]
    for label, cx, color in money_forms:
        ET.SubElement(svg, "circle", {"cx": str(cx), "cy": "475", "r": "8", "fill": color})
        add_text(svg, cx, 492, label, size=10, fill=color, weight="bold")
    # Arrow line
    ET.SubElement(svg, "line", {"x1": "110", "y1": "475", "x2": "690", "y2": "475", "stroke": LIGHT_GRAY, "stroke-width": "2"})

    # ── Properties of money ──
    add_card(svg, 30, 515, 740, 60, fill=GOLD_BG, stroke=GOLD)
    add_text(svg, 400, 537, "Свойства денег: портативность \u2022 долговечность \u2022 делимость \u2022 узнаваемость \u2022 редкость", size=12, fill=DARK, weight="bold")
    add_text(svg, 400, 560, "Деньги — особый товар, выполняющий роль всеобщего эквивалента", size=11, fill=GRAY)

    return svg


# ═══════════════════════════════════════════════════════════════
# LESSON 6: Банковская система
# ═══════════════════════════════════════════════════════════════
def lesson6():
    svg = svg_root()
    add_defs(svg)
    add_background(svg)
    add_title(svg, "Банковская система", 6)

    # ── Two-tier banking system ──
    # Central Bank
    add_card(svg, 200, 85, 400, 100, fill="#FEF3C7", stroke=GOLD)
    add_icon_circle(svg, 240, 120, 20, "Ц", bg_color=GOLD)
    add_text(svg, 270, 115, "Центральный банк (ЦБ)", size=16, fill=GOLD, weight="bold", anchor="start")
    cb_funcs = ["Эмиссия денег", "Регулирование банков", "Кредитование банков"]
    for i, f in enumerate(cb_funcs):
        add_text(svg, 270, 140 + i * 15, f, size=10, fill=DARK, anchor="start")

    # Arrow down
    add_arrow(svg, 400, 185, 400, 210, color=GOLD, width=3)

    # Commercial Banks
    add_card(svg, 30, 210, 350, 120, fill=GREEN_BG, stroke=GREEN_PRIMARY)
    add_icon_circle(svg, 70, 245, 18, "К", bg_color=GREEN_PRIMARY)
    add_text(svg, 100, 240, "Коммерческие банки", size=14, fill=GREEN_PRIMARY, weight="bold", anchor="start")
    bank_funcs = ["Приём вкладов (депозиты)", "Выдача кредитов", "Расчётно-кассовое обслуживание"]
    for i, f in enumerate(bank_funcs):
        add_text(svg, 55, 265 + i * 18, f, size=11, fill=DARK, anchor="start")

    # ── Deposit & Loan diagram ──
    add_card(svg, 410, 210, 360, 120, fill=WHITE)
    add_text(svg, 590, 235, "Операции банка", size=14, fill=DARK, weight="bold")
    # Deposit: People → Bank
    ET.SubElement(svg, "rect", {"x": "425", "y": "250", "width": "70", "height": "30", "fill": GREEN_BG, "stroke": GREEN_PRIMARY, "rx": "5"})
    add_text(svg, 460, 270, "Вклад", size=10, fill=GREEN_PRIMARY, weight="bold")
    add_arrow(svg, 500, 265, 550, 265, color=GREEN_PRIMARY)

    ET.SubElement(svg, "rect", {"x": "555", "y": "250", "width": "70", "height": "30", "fill": GOLD_BG, "stroke": GOLD, "rx": "5"})
    add_text(svg, 590, 270, "Банк", size=10, fill=GOLD, weight="bold")
    add_arrow(svg, 630, 265, 680, 265, color=RED_ACCENT)

    ET.SubElement(svg, "rect", {"x": "685", "y": "250", "width": "70", "height": "30", "fill": "#FEE2E2", "stroke": RED_ACCENT, "rx": "5"})
    add_text(svg, 720, 270, "Кредит", size=10, fill=RED_ACCENT, weight="bold")

    # Interest rates
    add_text(svg, 460, 300, "Ставка по вкладу", size=9, fill=GREEN_PRIMARY, anchor="start")
    add_text(svg, 460, 315, "(доход клиента)", size=9, fill=GRAY, anchor="start")
    add_text(svg, 700, 300, "Ставка по кредиту", size=9, fill=RED_ACCENT, anchor="start")
    add_text(svg, 700, 315, "(плата клиента)", size=9, fill=GRAY, anchor="start")

    # ── Interest formula ──
    add_formula_box(svg, 30, 350, 350, 70, "I = S \u00d7 r \u00d7 t / 100", "Формула процента")
    add_formula_box(svg, 410, 350, 360, 70, "S = P \u00d7 (1 + r/100)^n", "Сложный процент")

    # ── Key terms ──
    add_card(svg, 30, 440, 233, 80, fill=WHITE)
    add_text(svg, 147, 465, "Депозит", size=13, fill=GREEN_PRIMARY, weight="bold")
    add_text(svg, 147, 485, "Вклад в банк под %", size=10, fill=DARK)
    add_text(svg, 147, 500, "Депозит insured до 1,4 млн", size=9, fill=GRAY)

    add_card(svg, 283, 440, 233, 80, fill=WHITE)
    add_text(svg, 400, 465, "Кредит", size=13, fill=RED_ACCENT, weight="bold")
    add_text(svg, 400, 485, "Заём от банка под %", size=10, fill=DARK)
    add_text(svg, 400, 500, "Основной долг + проценты", size=9, fill=GRAY)

    add_card(svg, 536, 440, 233, 80, fill=WHITE)
    add_text(svg, 653, 465, "Ключевая ставка", size=13, fill=GOLD, weight="bold")
    add_text(svg, 653, 485, "Ставка ЦБ для банков", size=10, fill=DARK)
    add_text(svg, 653, 500, "Влияет на все ставки", size=9, fill=GRAY)

    # ── Money multiplier ──
    add_card(svg, 30, 535, 740, 45, fill=GOLD_BG, stroke=GOLD)
    add_text(svg, 400, 562, "Банковский мультипликатор: M = 1 / r  (r — норма резервирования)", size=13, fill=DARK, weight="bold")

    return svg


# ═══════════════════════════════════════════════════════════════
# LESSON 7: Налоги и налогообложение
# ═══════════════════════════════════════════════════════════════
def lesson7():
    svg = svg_root()
    add_defs(svg)
    add_background(svg)
    add_title(svg, "Налоги и налогообложение", 7)

    # ── Definition ──
    add_card(svg, 30, 85, 740, 50, fill=WHITE)
    add_text(svg, 400, 108, "Налог — обязательный платёж в бюджет для финансирования государства", size=14, fill=GREEN_DARK, weight="bold")
    add_text(svg, 400, 126, "Собираются на основе закона, в установленных размерах и срок", size=11, fill=GRAY)

    # ── Types of taxes ──
    add_card(svg, 30, 148, 355, 200, fill=WHITE)
    add_text(svg, 207, 173, "Прямые налоги", size=14, fill=GREEN_DARK, weight="bold")
    direct_taxes = [
        ("НДФЛ", "13% с доходов физлиц"),
        ("Налог на прибыль", "20% с организаций"),
        ("Налог на имущество", "Собственность физлиц"),
        ("Земельный налог", "С владельцев земли"),
        ("Транспортный", "С владельцев авто"),
    ]
    for i, (name, desc) in enumerate(direct_taxes):
        cy = 198 + i * 26
        ET.SubElement(svg, "rect", {"x": "50", "y": str(cy - 10), "width": "8", "height": "8", "fill": GREEN_PRIMARY, "rx": "2"})
        add_text(svg, 65, cy, name, size=11, fill=DARK, weight="bold", anchor="start")
        add_text(svg, 175, cy, desc, size=10, fill=GRAY, anchor="start")

    add_card(svg, 410, 148, 355, 200, fill=WHITE)
    add_text(svg, 587, 173, "Косвенные налоги", size=14, fill=DARK, weight="bold")
    indirect_taxes = [
        ("НДС", "20% добавленная стоимость"),
        ("Акциз", "На подакцизные товары"),
        ("Таможенные", "При ввозе/вывозе"),
        ("Торговый сбор", "С торговой деятельности"),
    ]
    for i, (name, desc) in enumerate(indirect_taxes):
        cy = 198 + i * 26
        ET.SubElement(svg, "rect", {"x": "430", "y": str(cy - 10), "width": "8", "height": "8", "fill": GOLD, "rx": "2"})
        add_text(svg, 445, cy, name, size=11, fill=DARK, weight="bold", anchor="start")
        add_text(svg, 545, cy, desc, size=10, fill=GRAY, anchor="start")

    # Note
    add_text(svg, 587, 312, "Включаются в цену товара", size=10, fill=GOLD, weight="bold")
    add_text(svg, 587, 328, "(платит покупатель)", size=9, fill=GRAY)

    # ── Tax functions ──
    add_card(svg, 30, 362, 233, 100, fill=GREEN_BG, stroke=GREEN_PRIMARY)
    add_icon_circle(svg, 70, 390, 14, "Ф", bg_color=GREEN_PRIMARY)
    add_text(svg, 90, 395, "Фискальная", size=12, fill=GREEN_PRIMARY, weight="bold", anchor="start")
    add_text(svg, 55, 415, "Пополнение бюджета", size=10, fill=DARK, anchor="start")
    add_text(svg, 55, 430, "государства", size=10, fill=DARK, anchor="start")

    add_card(svg, 283, 362, 233, 100, fill="#DBEAFE", stroke=BLUE_ACCENT)
    add_icon_circle(svg, 323, 390, 14, "Р", bg_color=BLUE_ACCENT)
    add_text(svg, 343, 395, "Регулирующая", size=12, fill=BLUE_ACCENT, weight="bold", anchor="start")
    add_text(svg, 308, 415, "Влияние на экономику", size=10, fill=DARK, anchor="start")
    add_text(svg, 308, 430, "и социальные процессы", size=10, fill=DARK, anchor="start")

    add_card(svg, 536, 362, 233, 100, fill="#FEE2E2", stroke=RED_ACCENT)
    add_icon_circle(svg, 576, 390, 14, "С", bg_color=RED_ACCENT)
    add_text(svg, 596, 395, "Социальная", size=12, fill=RED_ACCENT, weight="bold", anchor="start")
    add_text(svg, 561, 415, "Перераспределение", size=10, fill=DARK, anchor="start")
    add_text(svg, 561, 430, "доходов в обществе", size=10, fill=DARK, anchor="start")

    # ── Budget structure ──
    add_card(svg, 30, 478, 740, 55, fill=WHITE)
    add_text(svg, 400, 500, "Государственный бюджет", size=14, fill=DARK, weight="bold")
    ET.SubElement(svg, "rect", {"x": "60", "y": "510", "width": "300", "height": "16", "fill": GREEN_BG, "stroke": GREEN_PRIMARY, "rx": "4"})
    add_text(svg, 210, 522, "Доходы (налоги + сборы)", size=10, fill=GREEN_PRIMARY, weight="bold")
    ET.SubElement(svg, "rect", {"x": "440", "y": "510", "width": "300", "height": "16", "fill": GOLD_BG, "stroke": GOLD, "rx": "4"})
    add_text(svg, 590, 522, "Расходы (соц., оборона, ...)", size=10, fill=GOLD, weight="bold")

    # ── Key formula ──
    add_formula_box(svg, 30, 548, 355, 40, "НДФЛ = Доход \u00d7 13%", "Подоходный налог")
    add_formula_box(svg, 410, 548, 355, 40, "НДС = Цена \u00d7 20% / 120%", "Налог на добавл. стоимость")

    return svg


# ═══════════════════════════════════════════════════════════════
# LESSON 8: Семейный бюджет
# ═══════════════════════════════════════════════════════════════
def lesson8():
    svg = svg_root()
    add_defs(svg)
    add_background(svg)
    add_title(svg, "Семейный бюджет", 8)

    # ── Definition ──
    add_card(svg, 30, 85, 740, 45, fill=WHITE)
    add_text(svg, 400, 108, "Семейный бюджет — план доходов и расходов семьи на определённый период", size=14, fill=GREEN_DARK, weight="bold")

    # ── Income section ──
    add_card(svg, 30, 145, 370, 195, fill=GREEN_BG, stroke=GREEN_PRIMARY)
    add_text(svg, 215, 170, "ДОХОДЫ", size=16, fill=GREEN_PRIMARY, weight="bold")

    incomes = [
        ("Зарплата", "Основной доход", GREEN_PRIMARY),
        ("Пенсия/пособия", "Социальные выплаты", BLUE_ACCENT),
        ("Подработка", "Дополнительный доход", GOLD),
        ("Доход от вкладов", "Проценты по депозитам", "#7C3AED"),
        ("Сдача имущества", "Аренда, продажа", "#92400E"),
    ]
    for i, (name, desc, color) in enumerate(incomes):
        cy = 198 + i * 26
        ET.SubElement(svg, "circle", {"cx": "55", "cy": str(cy - 4), "r": "5", "fill": color})
        add_text(svg, 68, cy, name, size=11, fill=DARK, weight="bold", anchor="start")
        add_text(svg, 200, cy, desc, size=10, fill=GRAY, anchor="start")

    # ── Expenses section ──
    add_card(svg, 400, 145, 370, 195, fill="#FEE2E2", stroke=RED_ACCENT)
    add_text(svg, 585, 170, "РАСХОДЫ", size=16, fill=RED_ACCENT, weight="bold")

    expenses = [
        ("Жильё", "Аренда, коммунальные", RED_ACCENT),
        ("Продукты", "Питание семьи", "#92400E"),
        ("Одежда", "Вещи первой необходимости", BLUE_ACCENT),
        ("Транспорт", "Проезд, бензин", GOLD),
        ("Образование", "Курсы, репетиторы", GREEN_PRIMARY),
    ]
    for i, (name, desc, color) in enumerate(expenses):
        cy = 198 + i * 26
        ET.SubElement(svg, "circle", {"cx": "425", "cy": str(cy - 4), "r": "5", "fill": color})
        add_text(svg, 438, cy, name, size=11, fill=DARK, weight="bold", anchor="start")
        add_text(svg, 570, cy, desc, size=10, fill=GRAY, anchor="start")

    # ── Budget balance ──
    add_card(svg, 30, 355, 740, 90, fill=WHITE)
    add_text(svg, 400, 378, "Баланс бюджета", size=14, fill=DARK, weight="bold")

    # Three scenarios
    scenarios = [
        ("Доходы > Расходы", "Профицит — накопление", GREEN_PRIMARY, 130),
        ("Доходы = Расходы", "Баланс — без накоплений", GOLD, 400),
        ("Доходы < Расходы", "Дефицит — долги", RED_ACCENT, 670),
    ]
    for label, desc, color, cx in scenarios:
        ET.SubElement(svg, "rect", {"x": str(cx - 100), "y": "395", "width": "200", "height": "36", "fill": color + "15", "stroke": color, "rx": "8"})
        add_text(svg, cx, 412, label, size=11, fill=color, weight="bold")
        add_text(svg, cx, 428, desc, size=9, fill=GRAY)

    # ── Financial planning rules ──
    add_card(svg, 30, 460, 355, 120, fill=GOLD_BG, stroke=GOLD)
    add_text(svg, 207, 485, "Правило 50/30/20", size=14, fill=GOLD, weight="bold")
    rules = [
        ("50%", "Обязательные расходы", RED_ACCENT),
        ("30%", "Желания и развлечения", BLUE_ACCENT),
        ("20%", "Сбережения и инвестиции", GREEN_PRIMARY),
    ]
    for i, (pct, desc, color) in enumerate(rules):
        cy = 505 + i * 24
        ET.SubElement(svg, "rect", {"x": "50", "y": str(cy - 10), "width": "45", "height": "18", "fill": color, "rx": "4"})
        add_text(svg, 72, cy + 3, pct, size=11, fill=WHITE, weight="bold")
        add_text(svg, 105, cy + 3, desc, size=11, fill=DARK, anchor="start")

    # ── Savings tips ──
    add_card(svg, 410, 460, 355, 120, fill=WHITE)
    add_text(svg, 587, 485, "Советы по экономии", size=14, fill=GREEN_DARK, weight="bold")
    tips = [
        "Веди учёт расходов",
        "Откладывай сначала себе (10%)",
        "Сравнивай цены перед покупкой",
        "Избегай импульсивных трат",
        "Создай финансовую подушку",
    ]
    for i, tip in enumerate(tips):
        add_text(svg, 430, 505 + i * 15, tip, size=10, fill=DARK, anchor="start")

    # ── Bottom formula ──
    add_formula_box(svg, 30, 590, 740, 35, "Бюджет = Доходы - Расходы", "Формула бюджета")

    return svg


# ═══════════════════════════════════════════════════════════════
# MAIN: Generate all SVGs
# ═══════════════════════════════════════════════════════════════

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
for num, gen_func in generators:
    try:
        svg = gen_func()
        # Validate by converting to string and parsing back
        tree = ET.ElementTree(svg)
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")

        # Write with XML declaration
        ET.indent(tree, space="  ")
        tree.write(filepath, encoding="unicode", xml_declaration=True)

        # Validate by re-reading
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        ET.fromstring(content)  # Will raise if invalid XML

        file_size = os.path.getsize(filepath)
        results.append((num, "OK", file_size))
        print(f"✅ Lesson {num}: Generated successfully ({file_size} bytes)")
    except Exception as e:
        results.append((num, "FAIL", str(e)))
        print(f"❌ Lesson {num}: Error - {e}")

print("\n" + "=" * 60)
print("GENERATION SUMMARY")
print("=" * 60)
for num, status, detail in results:
    if status == "OK":
        print(f"  Lesson {num}: ✅ OK ({detail} bytes)")
    else:
        print(f"  Lesson {num}: ❌ FAILED - {detail}")

ok_count = sum(1 for _, s, _ in results if s == "OK")
print(f"\nTotal: {ok_count}/8 SVGs generated successfully")
