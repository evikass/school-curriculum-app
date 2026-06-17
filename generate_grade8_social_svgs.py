#!/usr/bin/env python3
"""Generate Grade 8 Social Studies (Обществознание) educational SVG images (8 lessons)."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/social"
W, H = 800, 600

# Color scheme — Amber/Yellow
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
INDIGO = "#6366F1"
PINK = "#EC4899"
CYAN = "#06B6D4"
EMERALD = "#10B981"


def escape(text):
    """Escape special XML characters."""
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;"))


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
    hdr = ET.SubElement(svg, "rect")
    hdr.set("x", "0")
    hdr.set("y", "6")
    hdr.set("width", str(W))
    hdr.set("height", "70")
    hdr.set("fill", AMBER)
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
        s.set("fill", LIGHT_AMBER)
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
        tb = ET.SubElement(svg, "rect")
        tb.set("x", str(x))
        tb.set("y", str(y))
        tb.set("width", str(w))
        tb.set("height", "26")
        tb.set("rx", "8")
        tb.set("fill", title_bg)
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


def add_path(svg, d, stroke=ORANGE, sw=2, fill="none"):
    """Add path."""
    p = ET.SubElement(svg, "path")
    p.set("d", d)
    p.set("stroke", stroke)
    p.set("stroke-width", str(sw))
    p.set("fill", fill)
    return p


def add_arrowhead_marker(defs, marker_id="arrowhead", color=ORANGE):
    """Add arrowhead marker definition."""
    marker = ET.SubElement(defs, "marker")
    marker.set("id", marker_id)
    marker.set("markerWidth", "10")
    marker.set("markerHeight", "7")
    marker.set("refX", "10")
    marker.set("refY", "3.5")
    marker.set("orient", "auto")
    polygon = ET.SubElement(marker, "polygon")
    polygon.set("points", "0 0, 10 3.5, 0 7")
    polygon.set("fill", color)


def add_arrow_line(svg, x1, y1, x2, y2, stroke=ORANGE, sw=2, marker="url(#arrowhead)"):
    """Add arrow line with marker."""
    l = ET.SubElement(svg, "line")
    l.set("x1", str(x1))
    l.set("y1", str(y1))
    l.set("x2", str(x2))
    l.set("y2", str(y2))
    l.set("stroke", stroke)
    l.set("stroke-width", str(sw))
    l.set("marker-end", marker)
    return l


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
    t.text = "Обществознание \u2022 8 класс \u2022 Интернет-Школа"


def add_connector(svg, x1, y1, x2, y2, color=AMBER, sw=2, curved=False):
    """Add a connector line between two points."""
    if curved:
        mx = (x1 + x2) // 2
        my = (y1 + y2) // 2
        d = f"M{x1},{y1} Q{mx},{my - 30} {x2},{y2}"
        add_path(svg, d, color, sw)
    else:
        add_line(svg, x1, y1, x2, y2, color, sw)


def add_rounded_box(svg, x, y, w, h, fill, stroke=ORANGE, sw=1.5, rx=12, text="", text_color=WHITE, text_size=13, text_weight="bold"):
    """Add a rounded box with centered text."""
    r = ET.SubElement(svg, "rect")
    r.set("x", str(x))
    r.set("y", str(y))
    r.set("width", str(w))
    r.set("height", str(h))
    r.set("rx", str(rx))
    r.set("fill", fill)
    r.set("stroke", stroke)
    r.set("stroke-width", str(sw))
    if text:
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + w // 2))
        t.set("y", str(y + h // 2 + 5))
        t.set("text-anchor", "middle")
        t.set("fill", text_color)
        t.set("font-size", str(text_size))
        t.set("font-weight", text_weight)
        t.set("font-family", "Arial, sans-serif")
        t.text = text


# ============================================================
# LESSON 1: Общество как динамическая система
# ============================================================
def lesson1():
    svg = svg_root()
    defs = add_bg(svg)
    add_arrowhead_marker(defs, "arrowAmber", AMBER)
    add_header(svg, "Общество как динамическая система", "Подсистемы общества: экономическая, политическая, социальная, духовная", 1)

    # Central circle — Общество
    add_circle(svg, 400, 260, 60, AMBER, DARK_AMBER, 3)
    add_text(svg, 400, 255, "ОБЩЕСТВО", 14, WHITE, "middle", "bold")
    add_text(svg, 400, 272, "динамичная", 10, LIGHT_AMBER, "middle")
    add_text(svg, 400, 285, "система", 10, LIGHT_AMBER, "middle")

    # 4 Subsystem boxes around the center
    # Top-left: Экономическая
    add_rounded_box(svg, 80, 110, 170, 60, BLUE, BLUE, 2, 10, "Экономическая", WHITE, 13, "bold")
    add_text(svg, 165, 155, "производство, обмен", 10, DARK, "middle")
    # Connector
    add_arrow_line(svg, 250, 155, 345, 230, BLUE, 2, "url(#arrowAmber)")

    # Top-right: Политическая
    add_rounded_box(svg, 550, 110, 170, 60, RED, RED, 2, 10, "Политическая", WHITE, 13, "bold")
    add_text(svg, 635, 155, "власть, управление", 10, DARK, "middle")
    add_arrow_line(svg, 550, 155, 455, 230, RED, 2, "url(#arrowAmber)")

    # Bottom-left: Социальная
    add_rounded_box(svg, 80, 350, 170, 60, GREEN, GREEN, 2, 10, "Социальная", WHITE, 13, "bold")
    add_text(svg, 165, 395, "группы, слои", 10, DARK, "middle")
    add_arrow_line(svg, 250, 370, 345, 290, GREEN, 2, "url(#arrowAmber)")

    # Bottom-right: Духовная
    add_rounded_box(svg, 550, 350, 170, 60, PURPLE, PURPLE, 2, 10, "Духовная", WHITE, 13, "bold")
    add_text(svg, 635, 395, "культура, ценности", 10, DARK, "middle")
    add_arrow_line(svg, 550, 370, 455, 290, PURPLE, 2, "url(#arrowAmber)")

    # Details for each subsystem
    add_section_box(svg, 15, 430, 185, 120, "Экономическая", WHITE, BLUE, BLUE)
    add_text(svg, 25, 468, "\u2022 Производство благ", 11, DARK)
    add_text(svg, 25, 484, "\u2022 Распределение", 11, DARK)
    add_text(svg, 25, 500, "\u2022 Обмен и потребление", 11, DARK)
    add_text(svg, 25, 516, "\u2022 Собственность", 11, DARK)
    add_text(svg, 25, 532, "\u2022 Рыночные отношения", 11, DARK)

    add_section_box(svg, 210, 430, 185, 120, "Политическая", WHITE, RED, RED)
    add_text(svg, 220, 468, "\u2022 Государство и власть", 11, DARK)
    add_text(svg, 220, 484, "\u2022 Политические партии", 11, DARK)
    add_text(svg, 220, 500, "\u2022 Право и закон", 11, DARK)
    add_text(svg, 220, 516, "\u2022 Избирательная система", 11, DARK)
    add_text(svg, 220, 532, "\u2022 Гражданское общество", 11, DARK)

    add_section_box(svg, 405, 430, 185, 120, "Социальная", WHITE, GREEN, GREEN)
    add_text(svg, 415, 468, "\u2022 Социальные группы", 11, DARK)
    add_text(svg, 415, 484, "\u2022 Классы и слои", 11, DARK)
    add_text(svg, 415, 500, "\u2022 Семья и быт", 11, DARK)
    add_text(svg, 415, 516, "\u2022 Социальная мобильность", 11, DARK)
    add_text(svg, 415, 532, "\u2022 Национальные отношения", 11, DARK)

    add_section_box(svg, 600, 430, 185, 120, "Духовная", WHITE, PURPLE, PURPLE)
    add_text(svg, 610, 468, "\u2022 Мораль и ценности", 11, DARK)
    add_text(svg, 610, 484, "\u2022 Образование", 11, DARK)
    add_text(svg, 610, 500, "\u2022 Наука и искусство", 11, DARK)
    add_text(svg, 610, 516, "\u2022 Религия", 11, DARK)
    add_text(svg, 610, 532, "\u2022 Мировоззрение", 11, DARK)

    # Central dynamic label
    add_text(svg, 400, 320, "Взаимосвязь", 11, DARK_AMBER, "middle", "bold")
    add_text(svg, 400, 335, "подсистем", 11, DARK_AMBER, "middle", "bold")

    add_footer(svg)
    return svg


# ============================================================
# LESSON 2: Общественный прогресс
# ============================================================
def lesson2():
    svg = svg_root()
    defs = add_bg(svg)
    add_arrowhead_marker(defs, "arrowGreen", GREEN)
    add_arrowhead_marker(defs, "arrowRed", RED)
    add_header(svg, "Общественный прогресс", "Критерии, противоречия, регресс и прогресс", 2)

    # Progress arrow — big horizontal arrow
    add_section_box(svg, 15, 90, 770, 100, "Направление развития общества", WHITE, AMBER, AMBER)
    # Progress arrow (left to right, green)
    add_rect(svg, 40, 125, 300, 30, GREEN, "none", 0, 5)
    add_text(svg, 190, 146, "ПРОГРЕСС \u2192", 15, WHITE, "middle", "bold")
    # Regression arrow (right to left, red)
    add_rect(svg, 460, 125, 300, 30, RED, "none", 0, 5)
    add_text(svg, 610, 146, "\u2190 РЕГРЕСС", 15, WHITE, "middle", "bold")
    # Center divider
    add_text(svg, 400, 146, "|", 18, DARK, "middle", "bold")
    add_text(svg, 400, 182, "Общество развивается неравномерно!", 12, DARK_AMBER, "middle", "bold")

    # Left: Progress criteria
    add_section_box(svg, 15, 200, 380, 170, "Критерии прогресса", WHITE, GREEN, GREEN)
    add_text(svg, 30, 238, "\u2022 Развитие производительных сил", 12, DARK)
    add_text(svg, 30, 256, "\u2022 Уровень свободы личности", 12, DARK)
    add_text(svg, 30, 274, "\u2022 Качество и продолжительность жизни", 12, DARK)
    add_text(svg, 30, 292, "\u2022 Развитие науки и образования", 12, DARK)
    add_text(svg, 30, 310, "\u2022 Расширение прав человека", 12, DARK)
    add_text(svg, 30, 328, "\u2022 Укрепление демократии", 12, DARK)
    add_text(svg, 30, 350, "Современный подход:", 12, DARK_AMBER, weight="bold")
    add_text(svg, 30, 365, "  качество жизни человека", 12, DARK_AMBER, weight="bold")

    # Right: Contradictions
    add_section_box(svg, 405, 200, 380, 170, "Противоречия прогресса", WHITE, RED, RED)
    add_text(svg, 420, 238, "\u2022 Прогресс одной сферы может", 12, DARK)
    add_text(svg, 435, 256, "вызвать регресс в другой", 12, RED)
    add_text(svg, 420, 274, "\u2022 Научные открытия могут быть", 12, DARK)
    add_text(svg, 435, 292, "использованы во вред", 12, RED)
    add_text(svg, 420, 310, "\u2022 Урбанизация: комфорт + стрессы", 12, DARK)
    add_text(svg, 420, 328, "\u2022 Необратимость: нельзя вернуться", 12, DARK)
    add_text(svg, 435, 346, "к прежнему состоянию", 12, DARK)
    add_text(svg, 420, 365, "Цена прогресса!", 12, RED, weight="bold")

    # Forms of social change
    add_section_box(svg, 15, 380, 380, 105, "Формы изменений", WHITE, AMBER, AMBER)
    add_text(svg, 30, 418, "\u2022 Эволюция \u2014 медленное,", 12, DARK)
    add_text(svg, 45, 436, "постепенное изменение", 12, DARK_AMBER)
    add_text(svg, 30, 454, "\u2022 Революция \u2014 быстрый,", 12, DARK)
    add_text(svg, 45, 472, "качественный скачок", 12, RED, weight="bold")

    # Key concepts
    add_section_box(svg, 405, 380, 380, 105, "Ключевые понятия", WHITE, DARK_AMBER, DARK_AMBER)
    add_text(svg, 420, 418, "\u2022 Прогресс \u2014 движение вперёд,", 12, DARK)
    add_text(svg, 435, 436, "от низшего к высшему", 12, GREEN, weight="bold")
    add_text(svg, 420, 454, "\u2022 Регресс \u2014 движение назад,", 12, DARK)
    add_text(svg, 435, 472, "от высшего к низшему", 12, RED, weight="bold")

    # Bottom insight
    add_section_box(svg, 15, 495, 770, 55, "Главная мысль", WHITE, AMBER, DARK_AMBER)
    add_text(svg, 400, 525, "Прогресс нелинеен: в одной сфере \u2014 прогресс, в другой \u2014 регресс", 13, DARK, "middle", "bold")

    add_footer(svg)
    return svg


# ============================================================
# LESSON 3: Экономика и её структура
# ============================================================
def lesson3():
    svg = svg_root()
    defs = add_bg(svg)
    add_arrowhead_marker(defs, "arrowAmber", AMBER)
    add_header(svg, "Экономика и её структура", "Производство, распределение, обмен, потребление", 3)

    # Central circular flow diagram
    add_section_box(svg, 15, 90, 500, 310, "Круговорот экономической деятельности", WHITE, AMBER, AMBER)

    # Circular flow: Production -> Distribution -> Exchange -> Consumption -> back
    cx, cy = 265, 250
    r = 95

    # 4 nodes in a circle
    import math
    positions = []
    labels = ["Производство", "Распределение", "Обмен", "Потребление"]
    colors = [BLUE, GREEN, PURPLE, RED]
    icons = ["\u2699", "\u2261", "\u21C4", "\u2714"]
    for i in range(4):
        angle = -math.pi / 2 + i * (2 * math.pi / 4)
        px = cx + int(r * math.cos(angle))
        py = cy + int(r * math.sin(angle))
        positions.append((px, py))
        add_rounded_box(svg, px - 55, py - 18, 110, 36, colors[i], colors[i], 2, 8, labels[i], WHITE, 12, "bold")

    # Curved arrows between nodes (clockwise)
    for i in range(4):
        x1, y1 = positions[i]
        x2, y2 = positions[(i + 1) % 4]
        # Offset for arrows from box edges
        mx = (x1 + x2) // 2
        my = (y1 + y2) // 2
        # Simple line connectors
        add_arrow_line(svg, x1 + (30 if x2 > x1 else -30 if x2 < x1 else 0),
                       y1 + (20 if y2 > y1 else -20 if y2 < y1 else 0),
                       x2 + (-30 if x2 > x1 else 30 if x2 < x1 else 0),
                       y2 + (-20 if y2 > y1 else 20 if y2 < y1 else 0),
                       AMBER, 2.5, "url(#arrowAmber)")

    # Center label
    add_circle(svg, cx, cy, 30, LIGHT_AMBER, AMBER, 2)
    add_text(svg, cx, cy - 3, "Экономи-", 9, DARK_AMBER, "middle", "bold")
    add_text(svg, cx, cy + 9, "ческий", 9, DARK_AMBER, "middle", "bold")
    add_text(svg, cx, cy + 21, "цикл", 9, DARK_AMBER, "middle", "bold")

    # Right side: Details for each stage
    add_section_box(svg, 530, 90, 255, 75, "Производство", WHITE, BLUE, BLUE)
    add_text(svg, 545, 128, "\u2022 Создание благ и услуг", 11, DARK)
    add_text(svg, 545, 146, "\u2022 Факторы: труд, земля,", 11, DARK)
    add_text(svg, 555, 160, "капитал, предпр-во", 10, DARK_AMBER)

    add_section_box(svg, 530, 175, 255, 75, "Распределение", WHITE, GREEN, GREEN)
    add_text(svg, 545, 213, "\u2022 Деление произведённого", 11, DARK)
    add_text(svg, 555, 231, "между участниками", 11, DARK_AMBER)
    add_text(svg, 545, 246, "\u2022 Доходы: зарплата, рента", 10, DARK)

    add_section_box(svg, 530, 260, 255, 75, "Обмен", WHITE, PURPLE, PURPLE)
    add_text(svg, 545, 298, "\u2022 Товарно-денежные", 11, DARK)
    add_text(svg, 555, 316, "отношения, рынок", 11, DARK_AMBER)
    add_text(svg, 545, 331, "\u2022 Торговля, бартер", 10, DARK)

    add_section_box(svg, 530, 345, 255, 75, "Потребление", WHITE, RED, RED)
    add_text(svg, 545, 383, "\u2022 Использование благ", 11, DARK)
    add_text(svg, 555, 401, "для удовлетворения", 11, DARK_AMBER)
    add_text(svg, 545, 416, "\u2022 Личное и производств.", 10, DARK)

    # Bottom: Key definitions
    add_section_box(svg, 15, 410, 500, 80, "Определение экономики", WHITE, AMBER, DARK_AMBER)
    add_text(svg, 30, 446, "Экономика \u2014 система хозяйствования,", 13, DARK, weight="bold")
    add_text(svg, 30, 466, "обеспечивающая общество благами и услугами.", 13, DARK_AMBER)
    add_text(svg, 30, 484, "Главная цель \u2014 удовлетворение потребностей.", 12, GREEN, weight="bold")

    # Types of economy
    add_section_box(svg, 530, 430, 255, 60, "Типы экономик", WHITE, AMBER, AMBER)
    add_text(svg, 545, 466, "Традиционная | Рыночная", 11, DARK)
    add_text(svg, 545, 483, "Командная | Смешанная", 11, DARK_AMBER, weight="bold")

    add_footer(svg)
    return svg


# ============================================================
# LESSON 4: Государство и экономика
# ============================================================
def lesson4():
    svg = svg_root()
    defs = add_bg(svg)
    add_arrowhead_marker(defs, "arrowAmber", AMBER)
    add_header(svg, "Государство и экономика", "Рыночное регулирование, налоги, бюджет, ВВП", 4)

    # Left: State regulation diagram
    add_section_box(svg, 15, 90, 385, 195, "Роль государства в экономике", WHITE, AMBER, AMBER)

    # State circle at top
    add_rounded_box(svg, 130, 115, 140, 35, DARK_AMBER, DARK_AMBER, 2, 8, "ГОСУДАРСТВО", WHITE, 13, "bold")

    # Three functions below
    funcs = [("Правовое\nрегулирование", 55, 190, BLUE),
             ("Экономическая\nполитика", 195, 190, GREEN),
             ("Социальная\nзащита", 335, 190, PURPLE)]
    for text, fx, fy, color in funcs:
        add_rounded_box(svg, fx - 50, fy, 100, 40, color, color, 2, 6, "", WHITE, 10, "bold")
        lines = text.split("\n")
        for j, line in enumerate(lines):
            add_text(svg, fx, fy + 17 + j * 14, line, 10, WHITE, "middle", "bold")
        add_line(svg, 200, 150, fx, fy, color, 2)

    # Bottom of box: tools
    add_text(svg, 30, 250, "Инструменты:", 12, DARK_AMBER, weight="bold")
    add_text(svg, 30, 268, "\u2022 Налоги и субсидии", 11, DARK)
    add_text(svg, 30, 284, "\u2022 Государственные закупки", 11, DARK)
    add_text(svg, 200, 268, "\u2022 Кредитно-денежная", 11, DARK)
    add_text(svg, 215, 284, "политика", 11, DARK)
    add_text(svg, 30, 300, "\u2022 Антимонопольное законодательство", 11, DARK)

    # Right: Taxes
    add_section_box(svg, 415, 90, 370, 100, "Налоги", WHITE, RED, RED)
    add_text(svg, 430, 128, "Налог \u2014 обязательный платёж в бюджет", 12, DARK, weight="bold")
    add_text(svg, 430, 150, "Прямые: подоходный, на прибыль,", 11, DARK)
    add_text(svg, 445, 166, "на имущество", 11, BLUE)
    add_text(svg, 430, 182, "Косвенные: НДС, акцизы, тамож.", 11, DARK)

    # Budget
    add_section_box(svg, 415, 200, 370, 100, "Государственный бюджет", WHITE, GREEN, GREEN)
    # Budget diagram: income vs expenses
    add_rounded_box(svg, 425, 232, 160, 50, "#DCFCE7", GREEN, 1.5, 6, "", DARK, 11, "bold")
    add_text(svg, 505, 253, "Доходы", 12, GREEN, "middle", "bold")
    add_text(svg, 505, 270, "Налоги, пошлины", 10, DARK, "middle")

    add_rounded_box(svg, 615, 232, 160, 50, "#FEE2E2", RED, 1.5, 6, "", DARK, 11, "bold")
    add_text(svg, 695, 253, "Расходы", 12, RED, "middle", "bold")
    add_text(svg, 695, 270, "Оборона, соц. сфера", 10, DARK, "middle")

    add_text(svg, 600, 296, "Профицит (Д > Р) | Дефицит (Д < Р)", 11, DARK_AMBER, "middle", weight="bold")

    # GDP
    add_section_box(svg, 15, 295, 385, 110, "ВВП (Валовой внутренний продукт)", WHITE, BLUE, BLUE)
    add_text(svg, 30, 333, "ВВП \u2014 стоимость всех конечных", 12, DARK, weight="bold")
    add_text(svg, 30, 351, "товаров и услуг, произведённых", 12, DARK)
    add_text(svg, 30, 369, "в стране за год.", 12, DARK_AMBER, weight="bold")
    add_text(svg, 30, 393, "ВВП = C + I + G + NX", 14, BLUE, weight="bold")
    add_text(svg, 230, 333, "C \u2014 потребление", 10, GRAY)
    add_text(svg, 230, 348, "I \u2014 инвестиции", 10, GRAY)
    add_text(svg, 230, 363, "G \u2014 гос. расходы", 10, GRAY)
    add_text(svg, 230, 378, "NX \u2014 чистый экспорт", 10, GRAY)

    # Market regulation
    add_section_box(svg, 415, 310, 370, 110, "Рыночное регулирование", WHITE, AMBER, AMBER)
    add_text(svg, 430, 348, "Рынок: спрос, предложение, цена", 12, DARK, weight="bold")
    add_text(svg, 430, 370, "\u2022 Невидимая рука рынка", 11, DARK_AMBER)
    add_text(svg, 430, 388, "\u2022 Конкуренция и свобода выбора", 11, DARK)
    add_text(svg, 430, 406, "\u2022 Государство компенсирует", 11, DARK)
    add_text(svg, 445, 422, "\"провалы\" рынка", 11, RED, weight="bold")

    # Bottom: Mixed economy
    add_section_box(svg, 15, 415, 770, 60, "Смешанная экономика", WHITE, AMBER, DARK_AMBER)
    add_text(svg, 30, 445, "Рыночный механизм + Государственное регулирование = Смешанная экономика", 13, DARK, weight="bold")
    add_text(svg, 400, 465, "Современная модель экономического развития", 12, DARK_AMBER, "middle")

    add_footer(svg)
    return svg


# ============================================================
# LESSON 5: Социальная структура общества
# ============================================================
def lesson5():
    svg = svg_root()
    defs = add_bg(svg)
    add_arrowhead_marker(defs, "arrowGreen", GREEN)
    add_arrowhead_marker(defs, "arrowRed", RED)
    add_header(svg, "Социальная структура общества", "Классы, социальная мобильность, стратификация", 5)

    # Social pyramid / stratification
    add_section_box(svg, 15, 90, 385, 320, "Социальная стратификация", WHITE, AMBER, AMBER)

    # Pyramid layers (trapezoids approximated by rects)
    layers = [
        ("Элита", 155, 120, 90, 30, DARK_AMBER),
        ("Высший средний класс", 120, 155, 160, 30, ORANGE),
        ("Средний класс", 85, 190, 230, 35, AMBER),
        ("Низший средний класс", 55, 230, 290, 35, "#FCD34D"),
        ("Рабочий класс", 30, 270, 340, 35, LIGHT_AMBER),
        ("Маргинальные слои", 30, 310, 340, 35, "#FDE68A"),
    ]
    for label, lx, ly, lw, lh, color in layers:
        add_rect(svg, lx, ly, lw, lh, color, AMBER, 1, 3)
        text_c = WHITE if color in [DARK_AMBER, ORANGE, AMBER] else DARK
        add_text(svg, lx + lw // 2, ly + lh // 2 + 5, label, 11, text_c, "middle", "bold")

    # Arrow up
    add_text(svg, 400, 180, "\u2191", 30, GREEN)
    add_text(svg, 400, 210, "Доход", 9, GREEN, "middle")
    add_text(svg, 400, 225, "Власть", 9, GREEN, "middle")
    add_text(svg, 400, 240, "Престиж", 9, GREEN, "middle")

    # Right: Social mobility
    add_section_box(svg, 415, 90, 370, 160, "Социальная мобильность", WHITE, GREEN, GREEN)
    add_text(svg, 430, 128, "Социальная мобильность \u2014", 12, DARK, weight="bold")
    add_text(svg, 430, 146, "перемещение людей между", 12, DARK)
    add_text(svg, 430, 164, "социальными слоями.", 12, DARK)

    # Upward mobility
    add_rounded_box(svg, 430, 180, 170, 30, GREEN, GREEN, 1.5, 6, "", WHITE, 11, "bold")
    add_text(svg, 515, 200, "\u2191 Восходящая", 11, WHITE, "middle", "bold")

    # Downward mobility
    add_rounded_box(svg, 610, 180, 170, 30, RED, RED, 1.5, 6, "", WHITE, 11, "bold")
    add_text(svg, 695, 200, "\u2193 Нисходящая", 11, WHITE, "middle", "bold")

    add_text(svg, 430, 230, "Внутрипоколенная \u2014 в течение", 11, DARK)
    add_text(svg, 445, 244, "одной жизни", 11, DARK_AMBER)
    add_text(svg, 430, 260, "Межпоколенная \u2014 от родителей", 11, DARK)
    add_text(svg, 445, 274, "к детям", 11, DARK_AMBER)

    # Right bottom: Social groups
    add_section_box(svg, 415, 260, 370, 130, "Социальные группы", WHITE, BLUE, BLUE)
    add_text(svg, 430, 298, "\u2022 Классы \u2014 по отношению к", 11, DARK)
    add_text(svg, 445, 314, "собственности и труду", 11, DARK_AMBER)
    add_text(svg, 430, 332, "\u2022 Слои (страты) \u2014 по доходу,", 11, DARK)
    add_text(svg, 445, 348, "образованию, престижу", 11, DARK_AMBER)
    add_text(svg, 430, 366, "\u2022 Маргиналы \u2014 вне социальных", 11, DARK)
    add_text(svg, 445, 382, "групп (безработные, мигранты)", 11, RED)

    # Criteria of stratification
    add_section_box(svg, 15, 420, 770, 65, "Критерии стратификации", WHITE, AMBER, DARK_AMBER)
    add_text(svg, 40, 452, "Доход", 14, BLUE, "middle", "bold")
    add_text(svg, 200, 452, "Власть", 14, RED, "middle", "bold")
    add_text(svg, 370, 452, "Образование", 14, GREEN, "middle", "bold")
    add_text(svg, 560, 452, "Престиж", 14, PURPLE, "middle", "bold")
    add_text(svg, 400, 475, "Социальное неравенство \u2014 неравный доступ к ресурсам", 12, DARK_AMBER, "middle")

    add_footer(svg)
    return svg


# ============================================================
# LESSON 6: Социальный конфликт и его решение
# ============================================================
def lesson6():
    svg = svg_root()
    defs = add_bg(svg)
    add_arrowhead_marker(defs, "arrowAmber", AMBER)
    add_arrowhead_marker(defs, "arrowGreen", GREEN)
    add_header(svg, "Социальный конфликт и его решение", "Виды, причины, стадии и методы разрешения", 6)

    # Left: Conflict stages
    add_section_box(svg, 15, 90, 385, 215, "Стадии конфликта", WHITE, RED, RED)
    stages = [
        ("1. Предпосылки", "Накопление противоречий", 120, RED),
        ("2. Инцидент", "Повод для начала конфликта", 155, ORANGE),
        ("3. Эскалация", "Нарастание напряжённости", 190, AMBER),
        ("4. Кульминация", "Высшая точка конфликта", 225, DARK_AMBER),
        ("5. Разрешение", "Выход из конфликта", 260, GREEN),
    ]
    for label, desc, sy, color in stages:
        add_rounded_box(svg, 30, sy - 12, 130, 24, color, color, 1.5, 5, "", WHITE, 10, "bold")
        add_text(svg, 95, sy + 4, label, 10, WHITE, "middle", "bold")
        add_text(svg, 170, sy + 4, desc, 11, DARK)
    # Arrow along stages
    add_arrow_line(svg, 95, 135, 95, 255, AMBER, 2, "url(#arrowAmber)")

    # Right: Types of conflicts
    add_section_box(svg, 415, 90, 370, 215, "Виды социальных конфликтов", WHITE, AMBER, AMBER)
    types = [
        ("\u2022 Политические", "борьба за власть", BLUE),
        ("\u2022 Экономические", "распределение ресурсов", GREEN),
        ("\u2022 Национальные", "межнациональные споры", PURPLE),
        ("\u2022 Религиозные", "вероисповедные разногласия", INDIGO),
        ("\u2022 Классовые", "классовые противоречия", RED),
        ("\u2022 Межличностные", "столкновение личностей", PINK),
    ]
    for i, (label, desc, color) in enumerate(types):
        ty = 128 + i * 28
        add_circle(svg, 430, ty - 3, 5, color)
        add_text(svg, 442, ty, label, 12, DARK, weight="bold")
        add_text(svg, 600, ty, desc, 11, GRAY)

    # Bottom left: Causes
    add_section_box(svg, 15, 315, 385, 130, "Причины конфликтов", WHITE, DARK_AMBER, DARK_AMBER)
    add_text(svg, 30, 353, "\u2022 Неравенство в доходах и статусе", 12, DARK)
    add_text(svg, 30, 373, "\u2022 Неудовлетворённость потребностей", 12, DARK)
    add_text(svg, 30, 393, "\u2022 Ценностные разногласия", 12, DARK)
    add_text(svg, 30, 413, "\u2022 Борьба за ограниченные ресурсы", 12, DARK)
    add_text(svg, 30, 433, "\u2022 Необъективность законов и правил", 12, DARK)

    # Bottom right: Resolution methods
    add_section_box(svg, 415, 315, 370, 130, "Методы разрешения", WHITE, GREEN, GREEN)
    methods = [
        ("\u2022 Компромисс", "взаимные уступки", 353, GREEN),
        ("\u2022 Переговоры", "поиск общего решения", 373, TEAL),
        ("\u2022 Медиация", "привлечение посредника", 393, BLUE),
        ("\u2022 Арбитраж", "решение третьей стороны", 413, INDIGO),
        ("\u2022 Сотрудничество", "совместный поиск выхода", 433, EMERALD),
    ]
    for label, desc, my, color in methods:
        add_text(svg, 430, my, label, 12, DARK, weight="bold")
        add_text(svg, 560, my, "\u2014 " + desc, 11, GRAY)

    # Bottom insight
    add_section_box(svg, 15, 455, 770, 55, "Конструктивная роль конфликта", WHITE, AMBER, DARK_AMBER)
    add_text(svg, 400, 480, "Конфликт не всегда вреден \u2014 он выявляет проблемы и стимулирует", 13, DARK, "middle")
    add_text(svg, 400, 498, "развитие общества при конструктивном разрешении", 13, GREEN, "middle", "bold")

    add_footer(svg)
    return svg


# ============================================================
# LESSON 7: Политическая система общества
# ============================================================
def lesson7():
    svg = svg_root()
    defs = add_bg(svg)
    add_arrowhead_marker(defs, "arrowAmber", AMBER)
    add_header(svg, "Политическая система общества", "Государство, партии, выборы, демократия", 7)

    # Central: Political system structure
    add_section_box(svg, 15, 90, 500, 260, "Структура политической системы", WHITE, AMBER, AMBER)

    # Central node: Political System
    add_rounded_box(svg, 185, 170, 160, 40, DARK_AMBER, DARK_AMBER, 2, 8, "Политическая система", WHITE, 12, "bold")

    # 5 components around
    components = [
        ("Государство", 50, 115, 110, 30, RED),
        ("Партии", 350, 115, 110, 30, BLUE),
        ("Обществ. организации", 50, 280, 140, 30, GREEN),
        ("Средства информации", 290, 280, 140, 30, PURPLE),
        ("Полит. культура", 175, 310, 120, 30, INDIGO),
    ]
    for label, cx_pos, cy_pos, cw, ch, color in components:
        add_rounded_box(svg, cx_pos, cy_pos, cw, ch, color, color, 1.5, 6, label, WHITE, 10, "bold")
        # Connect to center
        add_line(svg, cx_pos + cw // 2, cy_pos + ch // 2, 265, 190, color, 1.5, "4,3")

    # Right: State features
    add_section_box(svg, 530, 90, 255, 140, "Признаки государства", WHITE, RED, RED)
    features = [
        "\u2022 Территория и население",
        "\u2022 Публичная власть",
        "\u2022 Система права",
        "\u2022 Налоги и сборы",
        "\u2022 Суверенитет",
        "\u2022 Монополия на насилие",
    ]
    for i, f in enumerate(features):
        add_text(svg, 545, 128 + i * 17, f, 11, DARK)

    # Right: Forms of government
    add_section_box(svg, 530, 240, 255, 110, "Формы правления", WHITE, BLUE, BLUE)
    add_text(svg, 545, 278, "Монархия:", 12, DARK, weight="bold")
    add_text(svg, 560, 295, "Абсолютная, ограниченная", 10, DARK_AMBER)
    add_text(svg, 545, 315, "Республика:", 12, DARK, weight="bold")
    add_text(svg, 560, 332, "Президентская, парламентская,", 10, DARK_AMBER)
    add_text(svg, 560, 346, "смешанная", 10, DARK_AMBER)

    # Bottom: Democracy
    add_section_box(svg, 15, 360, 385, 110, "Демократия", WHITE, GREEN, GREEN)
    add_text(svg, 30, 398, "Демократия \u2014 власть народа", 13, DARK, weight="bold")
    add_text(svg, 30, 420, "\u2022 Свободные выборы", 11, DARK)
    add_text(svg, 200, 420, "\u2022 Многопартийность", 11, DARK)
    add_text(svg, 30, 438, "\u2022 Права и свободы", 11, DARK)
    add_text(svg, 200, 438, "\u2022 Разделение властей", 11, DARK)
    add_text(svg, 30, 456, "\u2022 Гласность", 11, DARK)
    add_text(svg, 200, 456, "\u2022 Законность", 11, DARK)

    # Elections
    add_section_box(svg, 415, 360, 370, 110, "Избирательная система", WHITE, AMBER, AMBER)
    add_text(svg, 430, 398, "Типы выборов:", 12, DARK, weight="bold")
    add_text(svg, 430, 418, "\u2022 Мажоритарная система", 11, DARK)
    add_text(svg, 445, 434, "побеждает большинство голосов", 10, DARK_AMBER)
    add_text(svg, 430, 452, "\u2022 Пропорциональная система", 11, DARK)
    add_text(svg, 445, 466, "места по проценту голосов", 10, DARK_AMBER)

    # Bottom bar
    add_section_box(svg, 15, 480, 770, 50, "Принципы демократических выборов", WHITE, AMBER, DARK_AMBER)
    add_text(svg, 50, 510, "Всеобщность", 12, BLUE, "middle", "bold")
    add_text(svg, 185, 510, "Равенство", 12, GREEN, "middle", "bold")
    add_text(svg, 315, 510, "Тайность", 12, PURPLE, "middle", "bold")
    add_text(svg, 440, 510, "Прямое голосование", 12, RED, "middle", "bold")
    add_text(svg, 620, 510, "Свобода выбора", 12, DARK_AMBER, "middle", "bold")

    add_footer(svg)
    return svg


# ============================================================
# LESSON 8: Правовое государство
# ============================================================
def lesson8():
    svg = svg_root()
    defs = add_bg(svg)
    add_arrowhead_marker(defs, "arrowAmber", AMBER)
    add_header(svg, "Правовое государство", "Разделение властей, права и обязанности, конституция", 8)

    # Central: Separation of powers triangle
    add_section_box(svg, 15, 90, 500, 280, "Разделение властей", WHITE, AMBER, AMBER)

    # Triangle: top = legislature, bottom-left = executive, bottom-right = judicial
    # Top vertex
    tx, ty = 265, 135
    add_rounded_box(svg, tx - 70, ty - 10, 140, 35, RED, RED, 2, 8, "Законодательная", WHITE, 11, "bold")
    add_text(svg, tx, ty + 40, "Парламент", 11, RED, "middle", "bold")
    add_text(svg, tx, ty + 55, "(Федеральное Собрание)", 9, GRAY, "middle")

    # Bottom-left
    lx, ly = 100, 290
    add_rounded_box(svg, lx - 60, ly - 10, 140, 35, BLUE, BLUE, 2, 8, "Исполнительная", WHITE, 11, "bold")
    add_text(svg, lx + 10, ly + 40, "Правительство", 11, BLUE, "middle", "bold")

    # Bottom-right
    rx, ry = 410, 290
    add_rounded_box(svg, rx - 60, ry - 10, 140, 35, PURPLE, PURPLE, 2, 8, "Судебная", WHITE, 11, "bold")
    add_text(svg, rx + 10, ry + 40, "Конституционный Суд", 10, PURPLE, "middle", "bold")
    add_text(svg, rx + 10, ry + 55, "Верховный Суд", 10, PURPLE, "middle")

    # Triangle lines
    add_line(svg, tx, ty + 25, lx + 10, ly - 10, AMBER, 2)
    add_line(svg, tx, ty + 25, rx + 10, ry - 10, AMBER, 2)
    add_line(svg, lx + 80, ly + 5, rx - 60, ry + 5, AMBER, 2)

    # System of checks and balances
    add_text(svg, 265, 245, "Система сдержек", 11, DARK_AMBER, "middle", "bold")
    add_text(svg, 265, 260, "и противовесов", 11, DARK_AMBER, "middle", "bold")

    # Small arrows for checks
    add_text(svg, 190, 200, "\u2199", 14, RED)
    add_text(svg, 340, 200, "\u2198", 14, BLUE)
    add_text(svg, 265, 280, "\u2193\u2191", 12, PURPLE)

    # Right: Rule of law principles
    add_section_box(svg, 530, 90, 255, 155, "Признаки правового гос-ва", WHITE, GREEN, GREEN)
    principles = [
        "\u2022 Верховенство закона",
        "\u2022 Разделение властей",
        "\u2022 Взаимная ответственность",
        "  государства и личности",
        "\u2022 Права и свободы человека",
        "\u2022 Независимый суд",
        "\u2022 Гражданское общество",
    ]
    for i, p in enumerate(principles):
        add_text(svg, 545, 126 + i * 17, p, 11, DARK)

    # Bottom left: Rights and duties
    add_section_box(svg, 15, 380, 385, 130, "Права и обязанности гражданина", WHITE, BLUE, BLUE)
    add_text(svg, 30, 415, "Права:", 12, BLUE, weight="bold")
    add_text(svg, 30, 433, "\u2022 На жизнь, свободу, личную неприкосновенность", 10, DARK)
    add_text(svg, 30, 448, "\u2022 На образование, труд, отдых", 10, DARK)
    add_text(svg, 30, 463, "\u2022 Свобода слова, собраний, религии", 10, DARK)
    add_text(svg, 30, 483, "Обязанности:", 12, RED, weight="bold")
    add_text(svg, 30, 498, "\u2022 Соблюдать законы, платить налоги,", 10, DARK)
    add_text(svg, 40, 512, "защищать Родину", 10, DARK_AMBER)

    # Bottom right: Constitution
    add_section_box(svg, 415, 380, 370, 130, "Конституция РФ", WHITE, DARK_AMBER, DARK_AMBER)
    add_text(svg, 430, 418, "Конституция \u2014 Основной закон", 12, DARK, weight="bold")
    add_text(svg, 430, 438, "государства, обладающий высшей", 12, DARK)
    add_text(svg, 430, 458, "юридической силой.", 12, DARK_AMBER, weight="bold")
    add_text(svg, 430, 483, "Принята 12 декабря 1993 г.", 11, GRAY)
    add_text(svg, 430, 500, "День Конституции \u2014 12 декабря", 11, DARK_AMBER)

    add_footer(svg)
    return svg


# ============================================================
# Main: Generate all SVGs
# ============================================================
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    lessons = [
        ("lesson-1.svg", lesson1),
        ("lesson-2.svg", lesson2),
        ("lesson-3.svg", lesson3),
        ("lesson-4.svg", lesson4),
        ("lesson-5.svg", lesson5),
        ("lesson-6.svg", lesson6),
        ("lesson-7.svg", lesson7),
        ("lesson-8.svg", lesson8),
    ]

    for filename, func in lessons:
        svg = func()
        # Validate XML by writing and parsing
        filepath = os.path.join(OUTPUT_DIR, filename)
        tree = ET.ElementTree(svg)
        ET.indent(tree, space="  ")
        tree.write(filepath, encoding="unicode", xml_declaration=True)

        # Validate
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            ET.fromstring(content)
            print(f"OK: {filename} — valid XML ({len(content)} bytes)")
        except ET.ParseError as e:
            print(f"ERROR: {filename} — XML parse error: {e}")


if __name__ == "__main__":
    main()
