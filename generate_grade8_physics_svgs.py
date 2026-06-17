#!/usr/bin/env python3
"""Generate Grade 8 Physics educational SVG images (10 lessons)."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/physics"
W, H = 800, 600

# Color scheme
ORANGE = "#F59E0B"
AMBER = "#D97706"
DARK_AMBER = "#92400E"
LIGHT_AMBER = "#FEF3C7"
LIGHTER_BG = "#FFFBEB"
WHITE = "#FFFFFF"
DARK = "#1C1917"
GRAY = "#78716C"
LIGHT_GRAY = "#F5F5F4"
BLUE = "#3B82F6"
RED = "#EF4444"
GREEN = "#22C55E"
TEAL = "#14B8A6"
PURPLE = "#8B5CF6"


def escape(text):
    """Escape special XML characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def svg_root():
    """Create base SVG element."""
    svg = ET.Element("svg")
    svg.set("xmlns", "http://www.w3.org/2000/svg")
    svg.set("width", str(W))
    svg.set("height", str(H))
    svg.set("viewBox", f"0 0 {W} {H}")
    return svg


def add_bg(svg):
    """Add background with subtle gradient."""
    defs = ET.SubElement(svg, "defs")
    grad = ET.SubElement(defs, "linearGradient")
    grad.set("id", "bgGrad")
    grad.set("x1", "0%")
    grad.set("y1", "0%")
    grad.set("x2", "0%")
    grad.set("y2", "100%")
    stop1 = ET.SubElement(grad, "stop")
    stop1.set("offset", "0%")
    stop1.set("stop-color", LIGHTER_BG)
    stop2 = ET.SubElement(grad, "stop")
    stop2.set("offset", "100%")
    stop2.set("stop-color", "#FFF7ED")
    rect = ET.SubElement(svg, "rect")
    rect.set("width", str(W))
    rect.set("height", str(H))
    rect.set("fill", "url(#bgGrad)")
    # Decorative top bar
    bar = ET.SubElement(svg, "rect")
    bar.set("width", str(W))
    bar.set("height", "6")
    bar.set("fill", ORANGE)
    return defs


def add_header(svg, title, subtitle="", lesson_num=1):
    """Add header bar with title."""
    # Header background
    hdr = ET.SubElement(svg, "rect")
    hdr.set("x", "0")
    hdr.set("y", "6")
    hdr.set("width", str(W))
    hdr.set("height", "70")
    hdr.set("fill", ORANGE)
    # Lesson number badge
    badge = ET.SubElement(svg, "rect")
    badge.set("x", "20")
    badge.set("y", "16")
    badge.set("width", "44")
    badge.set("height", "44")
    badge.set("rx", "10")
    badge.set("fill", DARK_AMBER)
    badge_text = ET.SubElement(svg, "text")
    badge_text.set("x", "42")
    badge_text.set("y", "47")
    badge_text.set("text-anchor", "middle")
    badge_text.set("fill", WHITE)
    badge_text.set("font-size", "22")
    badge_text.set("font-weight", "bold")
    badge_text.set("font-family", "Arial, sans-serif")
    badge_text.text = str(lesson_num)
    # Title
    t = ET.SubElement(svg, "text")
    t.set("x", "78")
    t.set("y", "38")
    t.set("fill", WHITE)
    t.set("font-size", "20")
    t.set("font-weight", "bold")
    t.set("font-family", "Arial, sans-serif")
    t.text = title
    if subtitle:
        s = ET.SubElement(svg, "text")
        s.set("x", "78")
        s.set("y", "58")
        s.set("fill", "#FEF3C7")
        s.set("font-size", "13")
        s.set("font-family", "Arial, sans-serif")
        s.text = subtitle


def add_section_box(svg, x, y, w, h, title="", fill=WHITE, border=ORANGE, title_bg=ORANGE):
    """Add a colored section box with optional title."""
    # Shadow
    sh = ET.SubElement(svg, "rect")
    sh.set("x", str(x + 2))
    sh.set("y", str(y + 2))
    sh.set("width", str(w))
    sh.set("height", str(h))
    sh.set("rx", "8")
    sh.set("fill", "#E5E7EB")
    sh.set("opacity", "0.5")
    # Box
    box = ET.SubElement(svg, "rect")
    box.set("x", str(x))
    box.set("y", str(y))
    box.set("width", str(w))
    box.set("height", str(h))
    box.set("rx", "8")
    box.set("fill", fill)
    box.set("stroke", border)
    box.set("stroke-width", "1.5")
    if title:
        # Title bar
        tb = ET.SubElement(svg, "rect")
        tb.set("x", str(x))
        tb.set("y", str(y))
        tb.set("width", str(w))
        tb.set("height", "26")
        tb.set("rx", "8")
        tb.set("fill", title_bg)
        # Cover bottom corners of title bar
        cover = ET.SubElement(svg, "rect")
        cover.set("x", str(x))
        cover.set("y", str(y + 18))
        cover.set("width", str(w))
        cover.set("height", "8")
        cover.set("fill", title_bg)
        tt = ET.SubElement(svg, "text")
        tt.set("x", str(x + w // 2))
        tt.set("y", str(y + 18))
        tt.set("text-anchor", "middle")
        tt.set("fill", WHITE)
        tt.set("font-size", "13")
        tt.set("font-weight", "bold")
        tt.set("font-family", "Arial, sans-serif")
        tt.text = title


def add_text(svg, x, y, text, size=14, fill=DARK, anchor="start", weight="normal", family="Arial, sans-serif"):
    """Add text element."""
    t = ET.SubElement(svg, "text")
    t.set("x", str(x))
    t.set("y", str(y))
    t.set("text-anchor", anchor)
    t.set("fill", fill)
    t.set("font-size", str(size))
    t.set("font-weight", weight)
    t.set("font-family", family)
    t.text = text
    return t


def add_formula(svg, x, y, formula, size=22, fill=DARK_AMBER):
    """Add a prominent formula."""
    t = ET.SubElement(svg, "text")
    t.set("x", str(x))
    t.set("y", str(y))
    t.set("text-anchor", "middle")
    t.set("fill", fill)
    t.set("font-size", str(size))
    t.set("font-weight", "bold")
    t.set("font-family", "Arial, sans-serif")
    t.text = formula
    # Decorative underline
    ul = ET.SubElement(svg, "line")
    ul.set("x1", str(x - len(formula) * size // 4))
    ul.set("y1", str(y + 6))
    ul.set("x2", str(x + len(formula) * size // 4))
    ul.set("y2", str(y + 6))
    ul.set("stroke", ORANGE)
    ul.set("stroke-width", "2")
    ul.set("opacity", "0.4")


def add_arrow(svg, x1, y1, x2, y2, color=ORANGE, width=2):
    """Add arrow line."""
    line = ET.SubElement(svg, "line")
    line.set("x1", str(x1))
    line.set("y1", str(y1))
    line.set("x2", str(x2))
    line.set("y2", str(y2))
    line.set("stroke", color)
    line.set("stroke-width", str(width))
    line.set("marker-end", "url(#arrowhead)")
    # Add arrowhead marker if not exists
    return line


def add_arrowhead_marker(defs):
    """Add arrowhead marker definition."""
    marker = ET.SubElement(defs, "marker")
    marker.set("id", "arrowhead")
    marker.set("markerWidth", "10")
    marker.set("markerHeight", "7")
    marker.set("refX", "10")
    marker.set("refY", "3.5")
    marker.set("orient", "auto")
    polygon = ET.SubElement(marker, "polygon")
    polygon.set("points", "0 0, 10 3.5, 0 7")
    polygon.set("fill", ORANGE)


def add_circle(svg, cx, cy, r, fill=ORANGE, stroke="none", sw=0):
    """Add circle."""
    c = ET.SubElement(svg, "circle")
    c.set("cx", str(cx))
    c.set("cy", str(cy))
    c.set("r", str(r))
    c.set("fill", fill)
    if stroke != "none":
        c.set("stroke", stroke)
        c.set("stroke-width", str(sw))
    return c


def add_ellipse(svg, cx, cy, rx, ry, fill="none", stroke=ORANGE, sw=2):
    """Add ellipse."""
    e = ET.SubElement(svg, "ellipse")
    e.set("cx", str(cx))
    e.set("cy", str(cy))
    e.set("rx", str(rx))
    e.set("ry", str(ry))
    e.set("fill", fill)
    e.set("stroke", stroke)
    e.set("stroke-width", str(sw))
    return e


def add_rect(svg, x, y, w, h, fill=ORANGE, stroke="none", sw=0, rx=0):
    """Add rectangle."""
    r = ET.SubElement(svg, "rect")
    r.set("x", str(x))
    r.set("y", str(y))
    r.set("width", str(w))
    r.set("height", str(h))
    r.set("fill", fill)
    if stroke != "none":
        r.set("stroke", stroke)
        r.set("stroke-width", str(sw))
    if rx:
        r.set("rx", str(rx))
    return r


def add_line(svg, x1, y1, x2, y2, stroke=ORANGE, sw=2, dasharray=""):
    """Add line."""
    l = ET.SubElement(svg, "line")
    l.set("x1", str(x1))
    l.set("y1", str(y1))
    l.set("x2", str(x2))
    l.set("y2", str(y2))
    l.set("stroke", stroke)
    l.set("stroke-width", str(sw))
    if dasharray:
        l.set("stroke-dasharray", dasharray)
    return l


def add_polyline(svg, points, stroke=ORANGE, sw=2, fill="none"):
    """Add polyline."""
    p = ET.SubElement(svg, "polyline")
    p.set("points", points)
    p.set("stroke", stroke)
    p.set("stroke-width", str(sw))
    p.set("fill", fill)
    return p


def add_path(svg, d, stroke=ORANGE, sw=2, fill="none"):
    """Add path."""
    p = ET.SubElement(svg, "path")
    p.set("d", d)
    p.set("stroke", stroke)
    p.set("stroke-width", str(sw))
    p.set("fill", fill)
    return p


def add_footer(svg):
    """Add footer with branding."""
    bar = ET.SubElement(svg, "rect")
    bar.set("x", "0")
    bar.set("y", str(H - 30))
    bar.set("width", str(W))
    bar.set("height", "30")
    bar.set("fill", DARK_AMBER)
    t = ET.SubElement(svg, "text")
    t.set("x", str(W // 2))
    t.set("y", str(H - 10))
    t.set("text-anchor", "middle")
    t.set("fill", LIGHT_AMBER)
    t.set("font-size", "11")
    t.set("font-family", "Arial, sans-serif")
    t.text = "Физика \u2022 8 класс \u2022 Интернет-Школа"


# ============================================================
# LESSON 1: Внутренняя энергия и способы её изменения
# ============================================================
def lesson1():
    svg = svg_root()
    defs = add_bg(svg)
    add_arrowhead_marker(defs)
    add_header(svg, "Внутренняя энергия и способы её изменения", "Тепловое движение, работа и теплопередача", 1)

    # Left section: Internal energy definition
    add_section_box(svg, 15, 90, 370, 175, "Определение", WHITE, ORANGE, ORANGE)
    add_text(svg, 25, 130, "Внутренняя энергия (U) \u2014 сумма", 13, DARK)
    add_text(svg, 25, 148, "кинетической энергии хаотичного", 13, DARK)
    add_text(svg, 25, 166, "движения частиц и потенциальной", 13, DARK)
    add_text(svg, 25, 184, "энергии их взаимодействия.", 13, DARK)
    add_text(svg, 25, 210, "U = E\u043a\u0438\u043d + E\u043f\u043e\u0442", 16, DARK_AMBER, weight="bold")

    # Molecule motion diagram
    add_section_box(svg, 15, 275, 370, 135, "Тепловое движение молекул", WHITE, ORANGE, AMBER)
    # Container
    add_rect(svg, 70, 305, 120, 80, "none", ORANGE, 2, 4)
    # Molecules (small circles with motion indicators)
    molecules = [(95, 325), (150, 340), (115, 360), (80, 350), (160, 315), (130, 380)]
    for mx, my in molecules:
        add_circle(svg, mx, my, 5, RED)
    # Motion arrows (small curved paths around molecules)
    add_text(svg, 220, 330, "\u2022 Молекулы движутся", 12, DARK)
    add_text(svg, 220, 348, "  хаотично", 12, DARK)
    add_text(svg, 220, 370, "\u2022 T \u2191 \u2192 скорость \u2191", 12, DARK)
    add_text(svg, 220, 390, "\u2022 T \u2193 \u2192 скорость \u2193", 12, DARK)

    # Right section: Ways to change internal energy
    add_section_box(svg, 400, 90, 385, 320, "Способы изменения U", WHITE, ORANGE, ORANGE)
    # Work
    add_rect(svg, 415, 128, 170, 30, LIGHT_AMBER, AMBER, 1, 5)
    add_text(svg, 500, 149, "Совершение работы", 13, DARK_AMBER, "middle", "bold")
    add_text(svg, 415, 178, "A\u2022 над телом \u2192 U \u2191", 13, DARK)
    add_text(svg, 415, 198, "A\u2022 телом \u2192 U \u2193", 13, DARK)
    # Example: friction
    add_rect(svg, 425, 210, 140, 40, "#FEF9C3", ORANGE, 1, 3)
    add_text(svg, 495, 227, "\U0001f528 Трение рук", 11, DARK, "middle")
    add_text(svg, 495, 243, "U \u2191 (нагревание)", 11, RED, "middle")

    # Heat transfer
    add_rect(svg, 415, 268, 170, 30, LIGHT_AMBER, AMBER, 1, 5)
    add_text(svg, 500, 289, "Теплопередача", 13, DARK_AMBER, "middle", "bold")
    add_text(svg, 415, 318, "Q > 0: тепло поступает \u2192 U \u2191", 12, DARK)
    add_text(svg, 415, 338, "Q < 0: тепло отдаётся \u2192 U \u2193", 12, DARK)
    # Heat transfer types
    add_rect(svg, 425, 350, 140, 40, "#FEF9C3", ORANGE, 1, 3)
    add_text(svg, 495, 365, "Теплопроводность", 10, DARK, "middle")
    add_text(svg, 495, 379, "Конвекция, Излучение", 10, DARK, "middle")

    # Central formula
    add_section_box(svg, 15, 420, 770, 65, "Ключевая формула", WHITE, ORANGE, DARK_AMBER)
    add_formula(svg, 200, 462, "\u0394U = A + Q", 28, DARK_AMBER)
    add_text(svg, 380, 450, "\u0394U \u2014 изменение внутренней энергии", 13, DARK)
    add_text(svg, 380, 468, "A \u2014 работа, Q \u2014 количество теплоты", 13, GRAY)

    # Venn-like diagram at bottom
    add_section_box(svg, 15, 495, 770, 70, "Первый закон термодинамики", WHITE, ORANGE, AMBER)
    add_text(svg, 400, 530, "Количество теплоты, переданное системе, идёт на изменение её внутренней энергии", 13, DARK, "middle")
    add_text(svg, 400, 550, "и на совершение работы над внешними телами", 13, DARK, "middle")

    add_footer(svg)
    return svg


# ============================================================
# LESSON 2: Количество теплоты и удельная теплоёмкость
# ============================================================
def lesson2():
    svg = svg_root()
    defs = add_bg(svg)
    add_arrowhead_marker(defs)
    add_header(svg, "Количество теплоты и удельная теплоёмкость", "Q = cm\u0394t, калориметрия", 2)

    # Main formula box
    add_section_box(svg, 15, 90, 385, 120, "Главная формула", WHITE, ORANGE, ORANGE)
    add_formula(svg, 200, 145, "Q = c \u00b7 m \u00b7 \u0394t", 30, DARK_AMBER)
    add_text(svg, 30, 170, "Q \u2014 количество теплоты (Дж)", 13, DARK)
    add_text(svg, 30, 188, "c \u2014 удельная теплоёмкость (Дж/кг\u00b7\u00b0C)", 13, DARK)
    add_text(svg, 30, 206, "m \u2014 масса (кг), \u0394t \u2014 разность темп.", 13, DARK)

    # Specific heat table
    add_section_box(svg, 415, 90, 370, 200, "Удельная теплоёмкость", WHITE, ORANGE, AMBER)
    # Table header
    add_rect(svg, 425, 122, 350, 22, ORANGE, "none", 0, 3)
    add_text(svg, 440, 138, "Вещество", 12, WHITE, weight="bold")
    add_text(svg, 570, 138, "c (Дж/кг\u00b7\u00b0C)", 12, WHITE, weight="bold")
    # Table rows
    rows = [("Вода", "4200"), ("Лёд", "2100"), ("Железо", "460"),
            ("Алюминий", "920"), ("Свинец", "140"), ("Медь", "400")]
    for i, (sub, val) in enumerate(rows):
        y_pos = 152 + i * 20
        if i % 2 == 0:
            add_rect(svg, 425, y_pos - 14, 350, 20, LIGHT_AMBER, "none", 0, 2)
        add_text(svg, 440, y_pos, sub, 12, DARK)
        add_text(svg, 570, y_pos, val, 12, DARK_AMBER, weight="bold")

    # Calorimetry
    add_section_box(svg, 15, 220, 385, 155, "Уравнение теплового баланса", WHITE, ORANGE, ORANGE)
    add_formula(svg, 200, 265, "Q\u2081 + Q\u2082 = 0", 24, DARK_AMBER)
    add_text(svg, 30, 290, "Q\u043e\u0442\u0434 + Q\u043f\u043e\u043b = 0", 16, DARK, weight="bold")
    add_text(svg, 30, 312, "Тепло, отданное горячим телом,", 12, DARK)
    add_text(svg, 30, 328, "равно теплу, полученному холодным.", 12, DARK)
    add_text(svg, 30, 350, "c\u2081m\u2081(t\u2081-t) = c\u2082m\u2082(t-t\u2082)", 13, BLUE, weight="bold")

    # Calorimeter diagram
    add_section_box(svg, 415, 300, 370, 195, "Калориметр", WHITE, ORANGE, AMBER)
    # Outer container
    add_rect(svg, 480, 335, 120, 100, "none", GRAY, 2, 5)
    # Inner container
    add_rect(svg, 490, 345, 100, 80, "none", ORANGE, 2, 4)
    # Liquid
    add_rect(svg, 492, 370, 96, 53, "#93C5FD", "none", 0, 2)
    add_text(svg, 540, 400, "H\u2082O", 14, WHITE, "middle", "bold")
    # Hot object
    add_circle(svg, 520, 380, 8, RED)
    add_text(svg, 520, 365, "t\u2081", 11, RED, "middle")
    # Labels
    add_text(svg, 540, 450, "Теплообмен", 12, DARK, "middle")
    add_text(svg, 620, 350, "Теплоизоляция", 11, GRAY)
    add_line(svg, 615, 355, 610, 385, GRAY, 1, "3,3")

    # Δt formula box
    add_section_box(svg, 15, 385, 385, 70, "Расчёт \u0394t", WHITE, ORANGE, AMBER)
    add_text(svg, 30, 420, "\u0394t = t\u043a\u043e\u043d \u2013 t\u043d\u0430\u0447", 18, DARK_AMBER, weight="bold")
    add_text(svg, 280, 418, "при нагревании", 12, DARK)
    add_text(svg, 280, 436, "\u0394t > 0, Q > 0", 12, RED)

    # Example
    add_section_box(svg, 15, 465, 770, 65, "Пример", WHITE, ORANGE, GREEN)
    add_text(svg, 30, 492, "Сколько тепла для нагревания 2 кг воды на 50\u00b0C?", 13, DARK, weight="bold")
    add_text(svg, 30, 514, "Q = 4200 \u00d7 2 \u00d7 50 = 420 000 Дж = 420 кДж", 14, DARK_AMBER, weight="bold")

    add_footer(svg)
    return svg


# ============================================================
# LESSON 3: Плавление и кристаллизация
# ============================================================
def lesson3():
    svg = svg_root()
    defs = add_bg(svg)
    add_arrowhead_marker(defs)
    add_header(svg, "Плавление и кристаллизация", "Температурные графики, удельная теплота плавления", 3)

    # Temperature graph - the key diagram
    add_section_box(svg, 15, 90, 440, 250, "График плавления и кристаллизации", WHITE, ORANGE, ORANGE)
    # Axes
    add_line(svg, 70, 310, 70, 110, DARK, 2)
    add_line(svg, 70, 310, 430, 310, DARK, 2)
    add_text(svg, 45, 210, "t,\u00b0C", 12, DARK, "middle")
    add_text(svg, 400, 328, "время", 12, DARK)
    # Graph: heating -> melting -> heating -> cooling -> crystallization -> cooling
    points_heating = "70,280 140,230"
    points_melting = "140,230 230,230"
    points_liquid = "230,230 290,170"
    points_cooling = "290,170 350,230"
    points_crystal = "350,230 420,230"
    add_polyline(svg, points_heating, BLUE, 3, "none")
    add_polyline(svg, points_melting, RED, 3, "none")
    add_polyline(svg, points_liquid, BLUE, 3, "none")
    add_polyline(svg, points_cooling, TEAL, 3, "none")
    add_polyline(svg, points_crystal, PURPLE, 3, "none")
    # Labels on graph
    add_text(svg, 90, 268, "нагрев", 10, BLUE)
    add_text(svg, 170, 222, "плавление", 10, RED, weight="bold")
    add_text(svg, 250, 165, "нагрев", 10, BLUE)
    add_text(svg, 300, 165, "жидк.", 10, TEAL)
    add_text(svg, 370, 222, "кристалл.", 10, PURPLE, weight="bold")
    # Temperature line label
    add_line(svg, 70, 230, 420, 230, RED, 1, "5,5")
    add_text(svg, 432, 234, "t\u043f\u043b", 11, RED, weight="bold")
    # Phase labels
    add_text(svg, 100, 298, "твёрдое", 9, GRAY)
    add_text(svg, 190, 244, "тв.+жидк.", 9, GRAY)
    add_text(svg, 260, 298, "жидкое", 9, GRAY)
    add_text(svg, 380, 244, "ж.+тв.", 9, GRAY)

    # Formulas box
    add_section_box(svg, 470, 90, 315, 250, "Формулы", WHITE, ORANGE, ORANGE)
    add_text(svg, 485, 130, "Удельная теплота", 14, DARK, weight="bold")
    add_text(svg, 485, 148, "плавления:", 14, DARK, weight="bold")
    add_formula(svg, 627, 185, "Q = \u03bb \u00b7 m", 24, DARK_AMBER)
    add_text(svg, 485, 210, "\u03bb (лямбда) \u2014 уд. теплота", 12, DARK)
    add_text(svg, 485, 228, "плавления [Дж/кг]", 12, DARK)
    add_text(svg, 485, 256, "При плавлении:", 13, DARK, weight="bold")
    add_text(svg, 485, 274, "Q > 0 (тепло поглощается)", 12, RED)
    add_text(svg, 485, 296, "При кристаллизации:", 13, DARK, weight="bold")
    add_text(svg, 485, 314, "Q < 0 (тепло выделяется)", 12, BLUE)

    # Table of melting points
    add_section_box(svg, 15, 350, 385, 115, "Температуры плавления", WHITE, ORANGE, AMBER)
    add_rect(svg, 25, 382, 365, 20, ORANGE, "none", 0, 3)
    add_text(svg, 40, 397, "Вещество", 11, WHITE, weight="bold")
    add_text(svg, 180, 397, "t\u043f\u043b, \u00b0C", 11, WHITE, weight="bold")
    add_text(svg, 290, 397, "\u03bb, кДж/кг", 11, WHITE, weight="bold")
    data = [("Лёд", "0", "334"), ("Железо", "1539", "270"), ("Свинец", "327", "25"), ("Олово", "232", "59")]
    for i, (s, t, l) in enumerate(data):
        y = 412 + i * 18
        if i % 2 == 0:
            add_rect(svg, 25, y - 12, 365, 18, LIGHT_AMBER, "none", 0, 2)
        add_text(svg, 40, y, s, 11, DARK)
        add_text(svg, 180, y, t, 11, DARK_AMBER, weight="bold")
        add_text(svg, 290, y, l, 11, DARK_AMBER)

    # Key concept
    add_section_box(svg, 415, 350, 370, 115, "Ключевые моменты", WHITE, ORANGE, DARK_AMBER)
    add_text(svg, 430, 383, "\u2022 При плавлении t = const", 13, DARK)
    add_text(svg, 430, 403, "\u2022 При кристаллизации t = const", 13, DARK)
    add_text(svg, 430, 423, "\u2022 Плавление и кристаллизация", 13, DARK)
    add_text(svg, 430, 441, "  происходят при одной t\u043f\u043b", 13, DARK_AMBER, weight="bold")

    # Example
    add_section_box(svg, 15, 475, 770, 55, "Пример", WHITE, ORANGE, GREEN)
    add_text(svg, 30, 500, "Расплавить 5 кг льда при 0\u00b0C: Q = 334 000 \u00d7 5 = 1 670 000 Дж = 1.67 МДж", 14, DARK_AMBER, weight="bold")
    add_text(svg, 640, 516, "Q = \u03bbm", 13, GRAY)

    add_footer(svg)
    return svg


# ============================================================
# LESSON 4: Испарение и конденсация
# ============================================================
def lesson4():
    svg = svg_root()
    defs = add_bg(svg)
    add_arrowhead_marker(defs)
    add_header(svg, "Испарение и конденсация", "Кипение, удельная теплота парообразования", 4)

    # Evaporation diagram
    add_section_box(svg, 15, 90, 385, 195, "Испарение", WHITE, ORANGE, ORANGE)
    # Container with liquid
    add_rect(svg, 55, 150, 180, 90, "none", BLUE, 2, 4)
    add_rect(svg, 57, 190, 176, 48, "#93C5FD", "none", 0, 2)
    # Molecules leaving surface
    for mx, my in [(80, 140), (120, 120), (160, 110), (200, 125)]:
        add_circle(svg, mx, my, 4, RED)
    # Arrows going up from surface
    add_line(svg, 80, 180, 75, 148, RED, 1.5)
    add_line(svg, 120, 180, 125, 128, RED, 1.5)
    add_line(svg, 160, 180, 155, 118, RED, 1.5)
    add_line(svg, 200, 180, 205, 133, RED, 1.5)
    # Molecules in liquid
    for mx, my in [(80, 205), (110, 215), (140, 200), (170, 210), (200, 205), (125, 225)]:
        add_circle(svg, mx, my, 4, BLUE)
    add_text(svg, 250, 165, "Молекулы вылетают", 12, DARK)
    add_text(svg, 250, 183, "с поверхности", 12, DARK)
    add_text(svg, 250, 208, "Испарение \u2192", 12, RED, weight="bold")
    add_text(svg, 250, 226, "охлаждение!", 12, BLUE)

    # Factors
    add_section_box(svg, 415, 90, 370, 195, "Факторы испарения", WHITE, ORANGE, AMBER)
    add_text(svg, 430, 128, "\u2022 Температура: T \u2191 \u2192 испарение \u2191", 13, DARK)
    add_text(svg, 430, 150, "\u2022 Площадь поверхности: S \u2191", 13, DARK)
    add_text(svg, 445, 168, "\u2192 испарение \u2191", 13, DARK)
    add_text(svg, 430, 190, "\u2022 Ветер: уносит пар \u2192 исп. \u2191", 13, DARK)
    add_text(svg, 430, 212, "\u2022 Род вещества:", 13, DARK)
    add_text(svg, 445, 230, "эфир исп. быстрее воды", 12, DARK_AMBER)
    add_text(svg, 430, 260, "Конденсация \u2014 обратный", 13, BLUE, weight="bold")
    add_text(svg, 430, 278, "процесс (пар \u2192 жидкость)", 13, BLUE)

    # Boiling
    add_section_box(svg, 15, 295, 385, 155, "Кипение", WHITE, ORANGE, ORANGE)
    add_text(svg, 30, 330, "Кипение \u2014 интенсивное", 14, DARK, weight="bold")
    add_text(svg, 30, 350, "испарение по всему объёму.", 14, DARK)
    # Boiling pot sketch
    add_rect(svg, 240, 310, 80, 70, "none", ORANGE, 2, 4)
    add_rect(svg, 242, 340, 76, 38, "#93C5FD", "none", 0, 2)
    # Bubbles
    add_circle(svg, 260, 340, 6, "none", BLUE, 1.5)
    add_circle(svg, 280, 325, 5, "none", BLUE, 1.5)
    add_circle(svg, 295, 335, 4, "none", BLUE, 1.5)
    # Steam
    add_path(svg, "M260,310 Q265,295 258,280", GRAY, 1.5, "none")
    add_path(svg, "M280,310 Q285,290 278,275", GRAY, 1.5, "none")
    add_text(svg, 30, 380, "t\u043a\u0438\u043f = const при давлении = const", 13, RED, weight="bold")
    add_text(svg, 30, 400, "Вода: t\u043a\u0438\u043f = 100\u00b0C (атм. давл.)", 12, DARK)

    # Vaporization heat formula
    add_section_box(svg, 415, 295, 370, 155, "Теплота парообразования", WHITE, ORANGE, ORANGE)
    add_formula(svg, 600, 340, "Q = L \u00b7 m", 26, DARK_AMBER)
    add_text(svg, 430, 365, "L \u2014 удельная теплота", 13, DARK)
    add_text(svg, 430, 383, "парообразования [Дж/кг]", 13, DARK)
    add_text(svg, 430, 410, "Вода: L = 2.3 \u00d7 10\u2076 Дж/кг", 13, RED, weight="bold")
    add_text(svg, 430, 430, "Испарение: Q > 0 (поглощ.)", 12, RED)
    add_text(svg, 430, 445, "Конденсация: Q < 0 (выдел.)", 12, BLUE)

    # Comparison table
    add_section_box(svg, 15, 460, 770, 70, "Испарение vs Кипение", WHITE, ORANGE, AMBER)
    add_text(svg, 30, 490, "Испарение: при любой t, с поверхности, медленно", 13, DARK)
    add_text(svg, 30, 510, "Кипение: при t\u043a\u0438\u043f, по всему объёму, бурно, t = const", 13, DARK_AMBER, weight="bold")
    add_text(svg, 600, 490, "Оба: Q = L\u00b7m", 14, RED, weight="bold")

    add_footer(svg)
    return svg


# ============================================================
# LESSON 5: Электрический ток и его характеристики
# ============================================================
def lesson5():
    svg = svg_root()
    defs = add_bg(svg)
    add_arrowhead_marker(defs)
    add_header(svg, "Электрический ток и его характеристики", "Сила тока I = q/t, напряжение, сопротивление", 5)

    # Current definition
    add_section_box(svg, 15, 90, 385, 140, "Электрический ток", WHITE, ORANGE, ORANGE)
    add_text(svg, 30, 128, "Направленное движение", 14, DARK, weight="bold")
    add_text(svg, 30, 148, "заряженных частиц!", 14, DARK, weight="bold")
    add_text(svg, 30, 175, "Условия тока:", 13, DARK_AMBER, weight="bold")
    add_text(svg, 30, 195, "\u2022 Свободные заряды", 13, DARK)
    add_text(svg, 30, 213, "\u2022 Электрическое поле (источник)", 13, DARK)

    # Amperage formula
    add_section_box(svg, 415, 90, 370, 140, "Сила тока", WHITE, ORANGE, ORANGE)
    add_formula(svg, 600, 135, "I = q / t", 28, DARK_AMBER)
    add_text(svg, 430, 160, "I \u2014 сила тока [А] (Ампер)", 13, DARK)
    add_text(svg, 430, 180, "q \u2014 заряд [Кл] (Кулон)", 13, DARK)
    add_text(svg, 430, 200, "t \u2014 время [с]", 13, DARK)
    add_text(svg, 430, 220, "1 А = 1 Кл / 1 с", 13, DARK_AMBER, weight="bold")

    # Circuit diagram
    add_section_box(svg, 15, 240, 385, 165, "Простая цепь", WHITE, ORANGE, AMBER)
    # Battery
    add_line(svg, 55, 280, 55, 350, DARK, 2)
    add_line(svg, 45, 290, 65, 290, DARK, 3)
    add_line(svg, 48, 310, 62, 310, DARK, 2)
    add_line(svg, 45, 330, 65, 330, DARK, 3)
    add_text(svg, 35, 272, "+", 12, RED, weight="bold")
    add_text(svg, 35, 352, "\u2013", 12, BLUE, weight="bold")
    add_text(svg, 25, 315, "E", 12, DARK_AMBER, weight="bold")
    # Wire top
    add_line(svg, 55, 280, 160, 280, DARK, 2)
    # Resistor
    add_rect(svg, 160, 270, 70, 20, "none", DARK, 2, 3)
    add_text(svg, 195, 285, "R", 12, DARK, "middle", weight="bold")
    # Wire to ammeter
    add_line(svg, 230, 280, 290, 280, DARK, 2)
    add_circle(svg, 310, 280, 15, "none", BLUE, 2)
    add_text(svg, 310, 285, "A", 12, BLUE, "middle", weight="bold")
    # Wire right side
    add_line(svg, 325, 280, 355, 280, DARK, 2)
    add_line(svg, 355, 280, 355, 350, DARK, 2)
    # Wire bottom
    add_line(svg, 55, 350, 355, 350, DARK, 2)
    # Current direction arrow
    add_text(svg, 200, 268, "I \u2192", 11, RED, weight="bold")
    # Voltmeter (parallel to resistor)
    add_line(svg, 195, 300, 195, 330, BLUE, 1, "4,4")
    add_circle(svg, 195, 345, 12, "none", RED, 2)
    add_text(svg, 195, 350, "V", 11, RED, "middle", weight="bold")
    add_line(svg, 195, 357, 195, 350, BLUE, 1, "4,4")

    # Voltage
    add_section_box(svg, 415, 240, 370, 100, "Напряжение", WHITE, ORANGE, ORANGE)
    add_formula(svg, 600, 278, "U = A / q", 24, DARK_AMBER)
    add_text(svg, 430, 300, "U \u2014 напряжение [В] (Вольт)", 13, DARK)
    add_text(svg, 430, 318, "A \u2014 работа поля, q \u2014 заряд", 13, DARK)
    add_text(svg, 430, 335, "1 В = 1 Дж / 1 Кл", 13, DARK_AMBER, weight="bold")

    # Resistance
    add_section_box(svg, 415, 350, 370, 80, "Сопротивление", WHITE, ORANGE, AMBER)
    add_formula(svg, 600, 380, "R = \u03c1 \u00b7 l / S", 22, DARK_AMBER)
    add_text(svg, 430, 400, "\u03c1 \u2014 уд. сопротивление, l \u2014 длина", 12, DARK)
    add_text(svg, 430, 418, "S \u2014 площадь сечения [Ом]", 12, DARK)

    # Key values
    add_section_box(svg, 15, 415, 770, 70, "Единицы измерения", WHITE, ORANGE, GREEN)
    add_text(svg, 40, 445, "I: Ампер [А]", 14, DARK, weight="bold")
    add_text(svg, 210, 445, "U: Вольт [В]", 14, DARK, weight="bold")
    add_text(svg, 380, 445, "R: Ом [\u03a9]", 14, DARK, weight="bold")
    add_text(svg, 540, 445, "q: Кулон [Кл]", 14, DARK, weight="bold")
    add_text(svg, 40, 468, "Амперметр \u2014 последовательно", 12, BLUE)
    add_text(svg, 280, 468, "Вольтметр \u2014 параллельно", 12, RED)

    add_footer(svg)
    return svg


# ============================================================
# LESSON 6: Закон Ома
# ============================================================
def lesson6():
    svg = svg_root()
    defs = add_bg(svg)
    add_arrowhead_marker(defs)
    add_header(svg, "Закон Ома", "I = U/R, график, расчёты", 6)

    # Main formula - big and central
    add_section_box(svg, 15, 90, 385, 130, "Закон Ома для участка цепи", WHITE, ORANGE, ORANGE)
    add_formula(svg, 200, 145, "I = U / R", 34, DARK_AMBER)
    add_text(svg, 30, 175, "Сила тока прямо пропорциональна", 13, DARK)
    add_text(svg, 30, 193, "напряжению и обратно пропорц.", 13, DARK)
    add_text(svg, 30, 211, "сопротивлению.", 13, DARK_AMBER, weight="bold")

    # Triangle formula
    add_section_box(svg, 415, 90, 370, 130, "Треугольник формул", WHITE, ORANGE, AMBER)
    # Triangle
    add_path(svg, "M600,120 L660,200 L540,200 Z", ORANGE, 3, "none")
    add_text(svg, 600, 155, "U", 18, DARK_AMBER, "middle", "bold")
    add_text(svg, 565, 198, "I", 16, DARK, "middle", "bold")
    add_text(svg, 635, 198, "R", 16, DARK, "middle", "bold")
    add_text(svg, 600, 195, "\u00d7", 12, DARK, "middle")
    add_text(svg, 430, 140, "U = I \u00b7 R", 14, DARK, weight="bold")
    add_text(svg, 430, 160, "I = U / R", 14, DARK, weight="bold")
    add_text(svg, 430, 180, "R = U / I", 14, DARK, weight="bold")

    # Graph I(U)
    add_section_box(svg, 15, 230, 385, 195, "График зависимости I(U)", WHITE, ORANGE, ORANGE)
    # Axes
    add_line(svg, 60, 400, 60, 250, DARK, 2)
    add_line(svg, 60, 400, 370, 400, DARK, 2)
    add_text(svg, 40, 325, "I", 14, DARK, "middle", weight="bold")
    add_text(svg, 350, 418, "U", 14, DARK, weight="bold")
    # Line through origin - R1 (larger slope = less R)
    add_line(svg, 60, 400, 340, 270, BLUE, 2.5)
    # R2 (steeper slope = more R)
    add_line(svg, 60, 400, 250, 280, RED, 2.5)
    # Labels
    add_text(svg, 345, 268, "R\u2081 (мало)", 11, BLUE, weight="bold")
    add_text(svg, 255, 278, "R\u2082 (велико)", 11, RED, weight="bold")
    add_text(svg, 100, 420, "I \u221d U при R = const", 12, DARK_AMBER)
    # Origin label
    add_text(svg, 52, 415, "0", 11, GRAY)

    # Calculations
    add_section_box(svg, 415, 230, 370, 195, "Примеры расчётов", WHITE, ORANGE, GREEN)
    add_text(svg, 430, 262, "1) U = 12 В, R = 4 Ом", 13, DARK)
    add_text(svg, 430, 282, "   I = U/R = 12/4 = 3 А", 13, DARK_AMBER, weight="bold")
    add_text(svg, 430, 310, "2) I = 2 А, R = 10 Ом", 13, DARK)
    add_text(svg, 430, 330, "   U = I\u00b7R = 2\u00b710 = 20 В", 13, DARK_AMBER, weight="bold")
    add_text(svg, 430, 358, "3) U = 220 В, I = 0.5 А", 13, DARK)
    add_text(svg, 430, 378, "   R = U/I = 220/0.5 = 440 Ом", 13, DARK_AMBER, weight="bold")
    add_text(svg, 430, 405, "Short circuit: R \u2192 0, I \u2192 \u221e !", 12, RED, weight="bold")

    # Key rules
    add_section_box(svg, 15, 435, 770, 55, "Важные закономерности", WHITE, ORANGE, DARK_AMBER)
    add_text(svg, 30, 460, "U \u2191 \u2192 I \u2191 (прямая пропорц.)", 13, BLUE)
    add_text(svg, 300, 460, "R \u2191 \u2192 I \u2193 (обратная пропорц.)", 13, RED)
    add_text(svg, 580, 460, "I \u221d 1/R", 14, DARK_AMBER, weight="bold")

    add_footer(svg)
    return svg


# ============================================================
# LESSON 7: Работа и мощность тока
# ============================================================
def lesson7():
    svg = svg_root()
    defs = add_bg(svg)
    add_arrowhead_marker(defs)
    add_header(svg, "Работа и мощность тока", "A = IUt, P = IU, Закон Джоуля-Ленца", 7)

    # Work of current
    add_section_box(svg, 15, 90, 385, 130, "Работа электрического тока", WHITE, ORANGE, ORANGE)
    add_formula(svg, 200, 135, "A = I \u00b7 U \u00b7 t", 28, DARK_AMBER)
    add_text(svg, 30, 160, "A \u2014 работа тока [Дж]", 13, DARK)
    add_text(svg, 30, 180, "I \u2014 сила тока [А]", 13, DARK)
    add_text(svg, 30, 200, "U \u2014 напряжение [В], t \u2014 время [с]", 13, DARK)
    # Alternative forms
    add_text(svg, 30, 215, "A = I\u00b2Rt = U\u00b2t/R", 13, BLUE, weight="bold")

    # Power of current
    add_section_box(svg, 415, 90, 370, 130, "Мощность тока", WHITE, ORANGE, ORANGE)
    add_formula(svg, 600, 135, "P = I \u00b7 U", 28, DARK_AMBER)
    add_text(svg, 430, 160, "P \u2014 мощность [Вт] (Ватт)", 13, DARK)
    add_text(svg, 430, 180, "P = A / t", 13, DARK)
    add_text(svg, 430, 200, "1 Вт = 1 Дж/с = 1 В\u00b7А", 13, DARK_AMBER, weight="bold")
    add_text(svg, 430, 215, "P = I\u00b2R = U\u00b2/R", 13, BLUE, weight="bold")

    # Joule-Lenz Law
    add_section_box(svg, 15, 230, 500, 150, "Закон Джоуля\u2013Ленца", WHITE, ORANGE, RED)
    add_formula(svg, 265, 280, "Q = I\u00b2 \u00b7 R \u00b7 t", 28, RED)
    add_text(svg, 30, 310, "Количество теплоты, выделяемое", 13, DARK)
    add_text(svg, 30, 330, "проводником с током, равно", 13, DARK)
    add_text(svg, 30, 350, "произведению квадрата силы тока,", 13, DARK)
    add_text(svg, 30, 370, "сопротивления и времени.", 13, DARK_AMBER, weight="bold")

    # Heating diagram
    add_section_box(svg, 530, 230, 255, 150, "Нагревание", WHITE, RED, RED)
    # Coil
    add_path(svg, "M570,290 L590,275 L610,305 L630,275 L650,305 L670,275 L690,290", RED, 3, "none")
    # Heat waves
    add_path(svg, "M590,310 Q585,320 590,330", ORANGE, 1.5, "none")
    add_path(svg, "M620,310 Q615,320 620,330", ORANGE, 1.5, "none")
    add_path(svg, "M650,310 Q645,320 650,330", ORANGE, 1.5, "none")
    add_text(svg, 657, 355, "Q \u2192 тепло", 12, RED, weight="bold")
    add_text(svg, 657, 372, "Нихром, фехраль", 11, GRAY)

    # Practical units
    add_section_box(svg, 15, 390, 385, 100, "Практические единицы", WHITE, ORANGE, AMBER)
    add_text(svg, 30, 420, "1 кВт\u00b7ч = 3 600 000 Дж", 14, DARK_AMBER, weight="bold")
    add_text(svg, 30, 445, "Счётчик электрической энергии", 13, DARK)
    add_text(svg, 30, 465, "измеряет расход в кВт\u00b7ч", 13, DARK)

    # Example
    add_section_box(svg, 415, 390, 370, 100, "Пример", WHITE, ORANGE, GREEN)
    add_text(svg, 430, 420, "U=220В, I=5А, t=30мин", 13, DARK)
    add_text(svg, 430, 442, "A = 5\u00b7220\u00b71800 = 1 980 000 Дж", 13, DARK_AMBER, weight="bold")
    add_text(svg, 430, 462, "P = 5\u00b7220 = 1100 Вт = 1.1 кВт", 13, BLUE, weight="bold")
    add_text(svg, 430, 482, "Q = 25\u00b744\u00b71800 = 1 980 000 Дж", 12, RED)

    # Devices table
    add_section_box(svg, 15, 500, 770, 30, "Мощности приборов", WHITE, ORANGE, AMBER)
    add_text(svg, 30, 521, "Лампа: 60-100 Вт", 11, DARK)
    add_text(svg, 200, 521, "Утюг: 1000-2000 Вт", 11, DARK)
    add_text(svg, 400, 521, "Чайник: 1500-2200 Вт", 11, DARK)
    add_text(svg, 600, 521, "СВЧ: 700-1200 Вт", 11, DARK)

    add_footer(svg)
    return svg


# ============================================================
# LESSON 8: Магнитное поле и его свойства
# ============================================================
def lesson8():
    svg = svg_root()
    defs = add_bg(svg)
    add_arrowhead_marker(defs)
    add_header(svg, "Магнитное поле и его свойства", "Линии поля, электромагниты, сила Лоренца", 8)

    # Magnetic field lines around magnet
    add_section_box(svg, 15, 90, 385, 195, "Магнитное поле", WHITE, ORANGE, ORANGE)
    # Bar magnet
    add_rect(svg, 120, 175, 120, 35, RED, "none", 0, 4)
    add_rect(svg, 180, 175, 60, 35, BLUE, "none", 0, 0)
    add_text(svg, 150, 198, "N", 14, WHITE, "middle", "bold")
    add_text(svg, 210, 198, "S", 14, WHITE, "middle", "bold")
    # Field lines (simplified curves from N to S)
    add_path(svg, "M150,175 Q150,130 210,130 Q270,130 210,175", ORANGE, 1.5, "none")
    add_path(svg, "M150,175 Q130,120 180,110 Q230,100 210,175", AMBER, 1.5, "none")
    add_path(svg, "M210,210 Q210,250 150,250 Q90,250 150,210", ORANGE, 1.5, "none")
    add_path(svg, "M210,210 Q230,260 180,270 Q130,280 150,210", AMBER, 1.5, "none")
    # Arrowheads on field lines
    add_text(svg, 180, 125, "\u2192", 14, ORANGE)
    add_text(svg, 180, 255, "\u2190", 14, ORANGE)
    add_text(svg, 30, 130, "Линии поля:", 12, DARK, weight="bold")
    add_text(svg, 30, 148, "N \u2192 вне \u2192 S", 12, DARK_AMBER)
    add_text(svg, 30, 166, "S \u2192 внутри \u2192 N", 12, DARK_AMBER)
    add_text(svg, 280, 150, "Не пересекаются!", 11, RED, weight="bold")
    add_text(svg, 280, 168, "Замкнутые кривые", 11, DARK)

    # Electromagnet
    add_section_box(svg, 415, 90, 370, 195, "Электромагнит", WHITE, ORANGE, AMBER)
    # Coil
    add_rect(svg, 470, 160, 120, 30, "none", ORANGE, 2, 5)
    # Core
    add_rect(svg, 480, 165, 100, 20, GRAY, "none", 0, 3)
    # Wire wraps
    for i in range(8):
        x = 478 + i * 13
        add_line(svg, x, 155, x, 190, BLUE, 1.5)
    # Current direction
    add_text(svg, 475, 150, "\u00d7", 14, RED, weight="bold")
    add_text(svg, 560, 150, "\u2022", 16, RED, weight="bold")
    add_text(svg, 530, 140, "I", 12, RED, weight="bold")
    # N and S poles
    add_text(svg, 468, 180, "N", 12, RED, "middle", weight="bold")
    add_text(svg, 595, 180, "S", 12, BLUE, "middle", weight="bold")
    # Field lines from electromagnet
    add_path(svg, "M468,170 Q430,140 468,120 Q530,90 595,120 Q630,140 595,170", ORANGE, 1.5, "none")
    add_text(svg, 430, 215, "Правило буравчика:", 12, DARK, weight="bold")
    add_text(svg, 430, 233, "I по час. \u2192 N справа", 12, DARK_AMBER)
    add_text(svg, 430, 253, "Усиление: железный", 12, DARK)
    add_text(svg, 430, 268, "сердечник + больше витков", 12, DARK)

    # Lorentz force
    add_section_box(svg, 15, 295, 385, 155, "Сила Лоренца", WHITE, ORANGE, ORANGE)
    add_formula(svg, 200, 340, "F = q\u20d7v \u00d7 B\u20d7", 22, DARK_AMBER)
    # Diagram: charge in magnetic field
    add_circle(svg, 160, 420, 10, RED)
    add_text(svg, 160, 425, "q", 10, WHITE, "middle", weight="bold")
    # Velocity arrow
    add_line(svg, 170, 420, 230, 420, BLUE, 2)
    add_text(svg, 210, 412, "v", 12, BLUE, weight="bold")
    # Magnetic field (into page)
    for mx, my in [(200, 390), (220, 390), (240, 390), (260, 390)]:
        add_text(svg, mx, my, "\u2297", 10, PURPLE)
    add_text(svg, 270, 390, "B", 12, PURPLE, weight="bold")
    # Force arrow (upward)
    add_line(svg, 160, 410, 160, 370, RED, 2)
    add_text(svg, 148, 370, "F", 12, RED, weight="bold")
    add_text(svg, 30, 440, "Левая рука: 4 пальца \u2192 v,", 12, DARK)
    add_text(svg, 30, 455, "B в ладонь, большой \u2192 F", 12, DARK)

    # Right-hand rule for current
    add_section_box(svg, 415, 295, 370, 155, "Правило правой руки", WHITE, ORANGE, AMBER)
    # Straight wire cross section
    add_circle(svg, 600, 370, 12, ORANGE)
    add_text(svg, 600, 375, "\u2022", 16, DARK, "middle", weight="bold")
    add_text(svg, 600, 395, "I \u2192 к нам", 11, DARK)
    # Circular field lines
    add_circle(svg, 600, 370, 30, "none", BLUE, 1.5)
    add_circle(svg, 600, 370, 50, "none", BLUE, 1)
    add_circle(svg, 600, 370, 70, "none", BLUE, 1)
    # Direction arrows on circles
    add_text(svg, 570, 340, "\u2190", 12, BLUE)
    add_text(svg, 630, 400, "\u2192", 12, BLUE)
    add_text(svg, 430, 425, "Большой палец \u2192 I", 12, DARK)
    add_text(svg, 430, 443, "4 пальца \u2192 B (линии)", 12, DARK_AMBER)

    # Key facts
    add_section_box(svg, 15, 460, 770, 55, "Ключевые свойства", WHITE, ORANGE, DARK_AMBER)
    add_text(svg, 30, 485, "\u2022 Магнитное поле \u2014 материально", 13, DARK)
    add_text(svg, 310, 485, "\u2022 Порождается движущимися зарядами", 13, DARK)
    add_text(svg, 30, 505, "\u2022 Обнаруживается по действию на проводник с током", 13, DARK)

    add_footer(svg)
    return svg


# ============================================================
# LESSON 9: Законы распространения и отражения света
# ============================================================
def lesson9():
    svg = svg_root()
    defs = add_bg(svg)
    add_arrowhead_marker(defs)
    add_header(svg, "Законы распространения и отражения света", "Прямолинейное распространение, закон отражения, зеркала", 9)

    # Law of reflection
    add_section_box(svg, 15, 90, 385, 210, "Закон отражения", WHITE, ORANGE, ORANGE)
    # Mirror surface
    add_line(svg, 60, 260, 260, 260, DARK, 3)
    # Hatch marks on mirror
    for hx in range(70, 260, 15):
        add_line(svg, hx, 260, hx - 8, 270, GRAY, 1)
    # Normal line
    add_line(svg, 160, 170, 160, 260, GRAY, 1, "5,5")
    add_text(svg, 165, 175, "N", 11, GRAY)
    # Incident ray
    add_line(svg, 60, 160, 160, 260, BLUE, 2.5)
    add_text(svg, 80, 200, "\u03b1", 16, BLUE, weight="bold")
    add_text(svg, 75, 180, "Падающий", 11, BLUE)
    # Reflected ray
    add_line(svg, 160, 260, 260, 160, RED, 2.5)
    add_text(svg, 220, 200, "\u03b2", 16, RED, weight="bold")
    add_text(svg, 215, 180, "Отражённый", 11, RED)
    # Angles
    add_formula(svg, 160, 290, "\u03b1 = \u03b2", 20, DARK_AMBER)
    add_text(svg, 270, 130, "Угол падения =", 13, DARK)
    add_text(svg, 270, 148, "углу отражения", 13, DARK_AMBER, weight="bold")
    add_text(svg, 270, 175, "Лучи и нормаль \u2014", 12, DARK)
    add_text(svg, 270, 193, "в одной плоскости", 12, DARK_AMBER, weight="bold")

    # Light propagation
    add_section_box(svg, 415, 90, 370, 110, "Распространение света", WHITE, ORANGE, AMBER)
    add_text(svg, 430, 128, "Свет распространяется", 14, DARK, weight="bold")
    add_text(svg, 430, 148, "прямолинейно!", 14, DARK_AMBER, weight="bold")
    add_text(svg, 430, 175, "Скорость света:", 13, DARK)
    add_formula(svg, 600, 192, "c = 3\u00d710\u2078 м/с", 18, DARK_AMBER)
    add_text(svg, 430, 192, "в вакууме", 12, GRAY)

    # Mirror imaging
    add_section_box(svg, 415, 210, 370, 165, "Изображение в зеркале", WHITE, ORANGE, ORANGE)
    # Mirror
    add_line(svg, 540, 225, 540, 355, DARK, 2.5)
    for hy in range(230, 355, 12):
        add_line(svg, 540, hy, 548, hy + 8, GRAY, 1)
    # Object (arrow)
    add_line(svg, 500, 345, 500, 265, BLUE, 2.5)
    add_path(svg, "M495,270 L500,255 L505,270", BLUE, 2, "none")
    add_text(svg, 490, 260, "A", 12, BLUE, weight="bold")
    # Image (arrow, dashed)
    add_line(svg, 580, 345, 580, 265, RED, 1.5, "4,4")
    add_path(svg, "M575,270 L580,255 L585,270", RED, 1.5, "none")
    add_text(svg, 590, 260, "A'", 12, RED, weight="bold")
    # Properties
    add_text(svg, 555, 280, "Мнимое", 11, RED)
    add_text(svg, 555, 295, "Равное", 11, DARK)
    add_text(svg, 555, 310, "Прямое", 11, DARK)
    add_text(svg, 555, 325, "Симметричное", 11, DARK_AMBER)

    # Shadow/Penumbra
    add_section_box(svg, 15, 310, 385, 120, "Тень и полутень", WHITE, ORANGE, AMBER)
    # Point source
    add_circle(svg, 60, 360, 5, ORANGE)
    add_text(svg, 45, 350, "S", 10, DARK_AMBER, weight="bold")
    # Object
    add_rect(svg, 130, 340, 10, 40, DARK, "none", 0)
    # Shadow rays
    add_line(svg, 60, 360, 130, 340, ORANGE, 1, "3,3")
    add_line(svg, 60, 360, 130, 380, ORANGE, 1, "3,3")
    # Shadow area
    add_rect(svg, 250, 335, 60, 50, "#1C1917", "none", 0, 2)
    add_text(svg, 280, 365, "тень", 10, WHITE, "middle")
    add_text(svg, 200, 375, "\u2192", 14, ORANGE)
    # Extended source
    add_circle(svg, 60, 405, 8, "#FBBF24", "none", 0)
    add_text(svg, 80, 408, "\u2192 полутень", 11, DARK_AMBER)

    # Key concepts
    add_section_box(svg, 15, 440, 770, 75, "Важные выводы", WHITE, ORANGE, DARK_AMBER)
    add_text(svg, 30, 468, "\u2022 Зеркало \u2014 мнимое, прямое, равное изображение", 13, DARK)
    add_text(svg, 30, 488, "\u2022 Угол падения = угол отражения (всегда!)", 13, DARK_AMBER, weight="bold")
    add_text(svg, 500, 468, "\u2022 Точечный источник \u2192 резкая тень", 13, DARK)
    add_text(svg, 500, 488, "\u2022 Протяжённый \u2192 тень + полутень", 13, DARK)

    add_footer(svg)
    return svg


# ============================================================
# LESSON 10: Линзы и оптические приборы
# ============================================================
def lesson10():
    svg = svg_root()
    defs = add_bg(svg)
    add_arrowhead_marker(defs)
    add_header(svg, "Линзы и оптические приборы", "Собирающая/рассеивающая линза, D=1/F, глаз/камера", 10)

    # Convex lens ray diagram
    add_section_box(svg, 15, 90, 385, 200, "Собирающая линза", WHITE, ORANGE, ORANGE)
    # Principal axis
    add_line(svg, 30, 200, 380, 200, GRAY, 1, "5,5")
    # Lens
    add_path(svg, "M190,125 Q210,200 190,275", BLUE, 2.5, "none")
    add_path(svg, "M190,125 Q170,200 190,275", BLUE, 2.5, "none")
    # Focal points
    add_circle(svg, 120, 200, 4, RED)
    add_text(svg, 115, 218, "F", 12, RED, weight="bold")
    add_circle(svg, 260, 200, 4, RED)
    add_text(svg, 255, 218, "F", 12, RED, weight="bold")
    # 2F points
    add_circle(svg, 50, 200, 3, DARK)
    add_text(svg, 45, 218, "2F", 10, DARK)
    add_circle(svg, 330, 200, 3, DARK)
    add_text(svg, 325, 218, "2F", 10, DARK)
    # Ray 1: parallel to axis, then through F
    add_line(svg, 40, 160, 190, 160, ORANGE, 2)
    add_line(svg, 190, 160, 340, 230, ORANGE, 2)
    # Ray 2: through center
    add_line(svg, 40, 160, 190, 200, TEAL, 2)
    add_line(svg, 190, 200, 340, 240, TEAL, 2)
    # Ray 3: through F on left, then parallel
    add_line(svg, 40, 220, 190, 200, PURPLE, 1.5, "3,3")
    add_line(svg, 190, 200, 340, 200, PURPLE, 1.5, "3,3")
    # Image
    add_line(svg, 310, 240, 310, 200, RED, 2)
    add_path(svg, "M305,205 L310,195 L315,205", RED, 2, "none")
    add_text(svg, 315, 240, "A'", 11, RED, weight="bold")
    # Object
    add_line(svg, 55, 160, 55, 200, BLUE, 2)
    add_path(svg, "M50,165 L55,155 L60,165", BLUE, 2, "none")
    add_text(svg, 40, 160, "A", 11, BLUE, weight="bold")
    add_text(svg, 150, 280, "Действит., перевёрнутое", 11, RED)

    # Concave lens
    add_section_box(svg, 415, 90, 370, 200, "Рассеивающая линза", WHITE, ORANGE, AMBER)
    add_line(svg, 430, 200, 770, 200, GRAY, 1, "5,5")
    # Concave lens shape
    add_path(svg, "M590,125 Q570,200 590,275", PURPLE, 2.5, "none")
    add_path(svg, "M590,125 Q610,200 590,275", PURPLE, 2.5, "none")
    # Focal points (virtual)
    add_circle(svg, 520, 200, 4, RED)
    add_text(svg, 515, 218, "F", 12, RED)
    add_circle(svg, 660, 200, 4, RED)
    add_text(svg, 655, 218, "F", 12, RED)
    # Parallel ray
    add_line(svg, 440, 160, 590, 160, ORANGE, 2)
    add_line(svg, 590, 160, 700, 185, ORANGE, 2)
    # Dashed extension back to F
    add_line(svg, 590, 160, 520, 200, ORANGE, 1, "4,4")
    # Through center ray
    add_line(svg, 440, 165, 590, 200, TEAL, 2)
    add_line(svg, 590, 200, 700, 215, TEAL, 2)
    add_text(svg, 540, 280, "Мнимое, прямое, уменьш.", 11, PURPLE)

    # Optical power
    add_section_box(svg, 15, 300, 385, 105, "Оптическая сила", WHITE, ORANGE, ORANGE)
    add_formula(svg, 200, 340, "D = 1 / F", 28, DARK_AMBER)
    add_text(svg, 30, 365, "D \u2014 оптическая сила [дптр]", 13, DARK)
    add_text(svg, 30, 385, "F \u2014 фокусное расстояние [м]", 13, DARK)
    add_text(svg, 30, 400, "1 дптр = 1 м\u207b\u00b9", 13, DARK_AMBER, weight="bold")
    add_text(svg, 250, 395, "F\u0441\u043e\u0431 > 0, D > 0", 12, BLUE)
    add_text(svg, 250, 400, "F\u0440\u0430\u0441 < 0, D < 0", 12, PURPLE)

    # Thin lens formula
    add_section_box(svg, 415, 300, 370, 105, "Формула тонкой линзы", WHITE, ORANGE, AMBER)
    add_formula(svg, 600, 338, "1/F = 1/d + 1/f", 22, DARK_AMBER)
    add_text(svg, 430, 360, "d \u2014 расстояние до предмета", 12, DARK)
    add_text(svg, 430, 378, "f \u2014 расстояние до изображения", 12, DARK)
    add_text(svg, 430, 396, "F \u2012 фокусное расстояние", 12, DARK)

    # Eye and camera
    add_section_box(svg, 15, 415, 385, 90, "Глаз как оптическая система", WHITE, ORANGE, DARK_AMBER)
    # Simplified eye
    add_ellipse(svg, 120, 460, 50, 30, LIGHT_AMBER, ORANGE, 2)
    add_circle(svg, 95, 460, 10, BLUE, DARK, 1)
    add_text(svg, 95, 464, "L", 9, WHITE, "middle", weight="bold")
    add_text(svg, 120, 445, "хрусталик", 9, DARK)
    # Retina
    add_path(svg, "M155,440 Q170,460 155,480", RED, 2, "none")
    add_text(svg, 175, 465, "сетчатка", 9, RED)
    add_text(svg, 210, 445, "Аккомодация \u2014", 12, DARK, weight="bold")
    add_text(svg, 210, 462, "изменение формы", 12, DARK)
    add_text(svg, 210, 479, "хрусталика", 12, DARK)
    add_text(svg, 210, 496, "D\u0433\u043b \u2248 60 дптр", 12, DARK_AMBER)

    # Camera
    add_section_box(svg, 415, 415, 370, 90, "Фотоаппарат", WHITE, ORANGE, AMBER)
    add_rect(svg, 450, 435, 100, 50, "none", ORANGE, 2, 6)
    add_circle(svg, 480, 460, 12, "none", DARK, 2)
    add_circle(svg, 480, 460, 6, BLUE, "none", 0)
    add_text(svg, 470, 420, "объектив", 10, DARK)
    add_text(svg, 565, 445, "F \u2012 фикс., фокус \u2012", 12, DARK)
    add_text(svg, 565, 462, "перемещ. объектива", 12, DARK)
    add_text(svg, 565, 479, "Матрица/плёнка", 12, DARK_AMBER)
    add_text(svg, 565, 496, "= сетчатка глаза", 12, GRAY)

    add_footer(svg)
    return svg


# ============================================================
# MAIN: Generate all SVGs
# ============================================================
generators = [
    (lesson1, "lesson-1.svg"),
    (lesson2, "lesson-2.svg"),
    (lesson3, "lesson-3.svg"),
    (lesson4, "lesson-4.svg"),
    (lesson5, "lesson-5.svg"),
    (lesson6, "lesson-6.svg"),
    (lesson7, "lesson-7.svg"),
    (lesson8, "lesson-8.svg"),
    (lesson9, "lesson-9.svg"),
    (lesson10, "lesson-10.svg"),
]

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    results = []

    for gen_func, filename in generators:
        filepath = os.path.join(OUTPUT_DIR, filename)
        try:
            svg = gen_func()
            tree = ET.ElementTree(svg)
            ET.indent(tree, space="  ")

            # Write file
            tree.write(filepath, encoding="unicode", xml_declaration=True)

            # Validate by re-parsing
            try:
                test_tree = ET.parse(filepath)
                root = test_tree.getroot()
                status = "OK"
            except ET.ParseError as e:
                status = f"XML INVALID: {e}"

            # File size
            fsize = os.path.getsize(filepath)
            results.append((filename, status, fsize))
            print(f"  {filename}: {status} ({fsize:,} bytes)")

        except Exception as e:
            results.append((filename, f"ERROR: {e}", 0))
            print(f"  {filename}: ERROR - {e}")

    print("\n" + "=" * 60)
    print("GENERATION SUMMARY")
    print("=" * 60)
    ok_count = 0
    total_size = 0
    for fname, status, fsize in results:
        icon = "\u2713" if status == "OK" else "\u2717"
        print(f"  {icon} {fname}: {status} ({fsize:,} bytes)")
        if status == "OK":
            ok_count += 1
            total_size += fsize

    print(f"\n  {ok_count}/10 files generated successfully")
    print(f"  Total size: {total_size:,} bytes")
    print(f"  Output dir: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
