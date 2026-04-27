#!/usr/bin/env python3
"""Generate Grade 8 Geography educational SVG images (9 lessons)."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/geography"
W, H = 800, 600

# Color scheme - green/teal
GREEN = "#059669"
DARK_GREEN = "#065F46"
LIGHT_GREEN = "#D1FAE5"
LIGHTER_BG = "#ECFDF5"
PALE_BG = "#F0FDF4"
WHITE = "#FFFFFF"
DARK = "#1C1917"
GRAY = "#78716C"
LIGHT_GRAY = "#F5F5F4"
BLUE = "#3B82F6"
DARK_BLUE = "#1E3A5F"
LIGHT_BLUE = "#BFDBFE"
RED = "#EF4444"
AMBER = "#F59E0B"
TEAL = "#14B8A6"
DARK_TEAL = "#0D9488"
LIGHT_TEAL = "#CCFBF1"
ORANGE = "#F97316"
PURPLE = "#8B5CF6"
YELLOW = "#EAB308"
BROWN = "#92400E"
SAND = "#FDE68A"
ICE_BLUE = "#DBEAFE"
SNOW = "#EFF6FF"


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
    stop2.set("stop-color", PALE_BG)
    rect = ET.SubElement(svg, "rect")
    rect.set("width", str(W))
    rect.set("height", str(H))
    rect.set("fill", "url(#bgGrad)")
    # Decorative top bar
    bar = ET.SubElement(svg, "rect")
    bar.set("width", str(W))
    bar.set("height", "6")
    bar.set("fill", GREEN)
    return defs


def add_header(svg, title, subtitle="", lesson_num=1):
    """Add header bar with title."""
    hdr = ET.SubElement(svg, "rect")
    hdr.set("x", "0")
    hdr.set("y", "6")
    hdr.set("width", str(W))
    hdr.set("height", "70")
    hdr.set("fill", GREEN)
    # Lesson number badge
    badge = ET.SubElement(svg, "rect")
    badge.set("x", "20")
    badge.set("y", "16")
    badge.set("width", "44")
    badge.set("height", "44")
    badge.set("rx", "10")
    badge.set("fill", DARK_GREEN)
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
        s.set("fill", LIGHT_GREEN)
        s.set("font-size", "13")
        s.set("font-family", "Arial, sans-serif")
        s.text = subtitle


def add_section_box(svg, x, y, w, h, title="", fill=WHITE, border=GREEN, title_bg=GREEN):
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


def add_rect(svg, x, y, w, h, fill=GREEN, stroke="none", sw=0, rx=0):
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


def add_circle(svg, cx, cy, r, fill=GREEN, stroke="none", sw=0):
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


def add_ellipse(svg, cx, cy, rx, ry, fill="none", stroke=GREEN, sw=2):
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


def add_line(svg, x1, y1, x2, y2, stroke=GREEN, sw=2, dasharray=""):
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


def add_polyline(svg, points, stroke=GREEN, sw=2, fill="none"):
    """Add polyline."""
    p = ET.SubElement(svg, "polyline")
    p.set("points", points)
    p.set("stroke", stroke)
    p.set("stroke-width", str(sw))
    p.set("fill", fill)
    return p


def add_path(svg, d, stroke=GREEN, sw=2, fill="none"):
    """Add path."""
    p = ET.SubElement(svg, "path")
    p.set("d", d)
    p.set("stroke", stroke)
    p.set("stroke-width", str(sw))
    p.set("fill", fill)
    return p


def add_polygon(svg, points, fill=GREEN, stroke="none", sw=0):
    """Add polygon."""
    p = ET.SubElement(svg, "polygon")
    p.set("points", points)
    p.set("fill", fill)
    if stroke != "none":
        p.set("stroke", stroke)
        p.set("stroke-width", str(sw))
    return p


def add_russia_silhouette(svg, x, y, w, h, fill=LIGHT_GREEN, stroke=GREEN, sw=1.5):
    """Add a simplified Russia map silhouette."""
    # Simplified Russia outline scaled to bounding box
    # Real Russia spans roughly from 20E to 170W, 42N to 82N
    # We create a recognizable simplified shape
    points = []
    # Normalized coordinates (0-1 range) for Russia shape
    russia_coords = [
        (0.05, 0.40), (0.08, 0.30), (0.12, 0.20), (0.15, 0.15),
        (0.20, 0.10), (0.30, 0.08), (0.40, 0.06), (0.50, 0.05),
        (0.60, 0.07), (0.70, 0.10), (0.80, 0.12), (0.90, 0.15),
        (0.95, 0.20), (0.98, 0.25), (1.00, 0.30), (0.98, 0.35),
        (0.95, 0.30), (0.92, 0.35), (0.88, 0.30), (0.85, 0.35),
        (0.82, 0.32), (0.78, 0.38), (0.72, 0.42), (0.68, 0.45),
        (0.65, 0.48), (0.60, 0.52), (0.55, 0.55), (0.50, 0.58),
        (0.45, 0.60), (0.40, 0.62), (0.35, 0.60), (0.30, 0.58),
        (0.25, 0.60), (0.20, 0.62), (0.15, 0.65), (0.12, 0.62),
        (0.10, 0.58), (0.08, 0.52), (0.05, 0.48), (0.03, 0.44),
    ]
    for nx, ny in russia_coords:
        px = x + nx * w
        py = y + ny * h
        points.append(f"{px:.1f},{py:.1f}")

    poly = ET.SubElement(svg, "polygon")
    poly.set("points", " ".join(points))
    poly.set("fill", fill)
    poly.set("stroke", stroke)
    poly.set("stroke-width", str(sw))
    return poly


def add_russia_detailed(svg, x, y, w, h, fill=LIGHT_GREEN, stroke=GREEN, sw=1.5):
    """Add more detailed Russia outline."""
    # More detailed simplified Russia shape with Kamchatka, etc.
    russia_coords = [
        (0.02, 0.50), (0.04, 0.42), (0.06, 0.35), (0.09, 0.28),
        (0.12, 0.22), (0.16, 0.16), (0.20, 0.12), (0.25, 0.10),
        (0.32, 0.08), (0.38, 0.06), (0.45, 0.05), (0.52, 0.04),
        (0.58, 0.05), (0.63, 0.07), (0.68, 0.10), (0.72, 0.08),
        (0.76, 0.12), (0.80, 0.15), (0.84, 0.13), (0.88, 0.18),
        (0.92, 0.16), (0.95, 0.22), (0.97, 0.28), (1.00, 0.32),
        # Kamchatka extension
        (0.98, 0.28), (0.96, 0.32), (0.93, 0.36),
        # Southern border back
        (0.90, 0.33), (0.87, 0.38), (0.84, 0.35), (0.80, 0.40),
        (0.76, 0.38), (0.72, 0.42), (0.68, 0.46), (0.64, 0.50),
        (0.60, 0.54), (0.56, 0.56), (0.52, 0.58), (0.48, 0.60),
        (0.44, 0.62), (0.40, 0.64), (0.36, 0.62), (0.32, 0.60),
        (0.28, 0.62), (0.24, 0.64), (0.20, 0.66), (0.16, 0.68),
        (0.12, 0.66), (0.10, 0.62), (0.08, 0.56), (0.05, 0.52),
    ]
    points = []
    for nx, ny in russia_coords:
        px = x + nx * w
        py = y + ny * h
        points.append(f"{px:.1f},{py:.1f}")
    poly = ET.SubElement(svg, "polygon")
    poly.set("points", " ".join(points))
    poly.set("fill", fill)
    poly.set("stroke", stroke)
    poly.set("stroke-width", str(sw))
    return poly


def add_footer(svg):
    """Add footer with branding."""
    bar = ET.SubElement(svg, "rect")
    bar.set("x", "0")
    bar.set("y", str(H - 30))
    bar.set("width", str(W))
    bar.set("height", "30")
    bar.set("fill", DARK_GREEN)
    t = ET.SubElement(svg, "text")
    t.set("x", str(W // 2))
    t.set("y", str(H - 10))
    t.set("text-anchor", "middle")
    t.set("fill", LIGHT_GREEN)
    t.set("font-size", "11")
    t.set("font-family", "Arial, sans-serif")
    t.text = "География \u2022 8 класс \u2022 Интернет-Школа"


def add_map_label(svg, x, y, name, color=DARK, size=10, anchor="middle"):
    """Add a map label with a small dot."""
    add_circle(svg, x, y, 2.5, RED)
    add_text(svg, x, y - 6, name, size, color, anchor)


def add_city(svg, x, y, name, color=DARK, size=9, anchor="start"):
    """Add a city marker on the map."""
    add_circle(svg, x, y, 3, RED, DARK, 1)
    add_text(svg, x + 5, y + 4, name, size, color, anchor)


def add_sea(svg, x, y, name, color=DARK_BLUE, size=9, anchor="middle"):
    """Add a sea label with wave styling."""
    add_text(svg, x, y, name, size, color, anchor, "bold")


def add_compass(svg, cx, cy, size=30):
    """Add a compass rose."""
    # Outer circle
    add_circle(svg, cx, cy, size, "none", GREEN, 1.5)
    # N arrow
    add_line(svg, cx, cy - size + 5, cx, cy - 5, RED, 2)
    # S arrow
    add_line(svg, cx, cy + 5, cx, cy + size - 5, GREEN, 2)
    # E arrow
    add_line(svg, cx + 5, cy, cx + size - 5, cy, GREEN, 2)
    # W arrow
    add_line(svg, cx - size + 5, cy, cx - 5, cy, GREEN, 2)
    # Labels
    add_text(svg, cx, cy - size - 4, "С", 10, RED, "middle", "bold")
    add_text(svg, cx, cy + size + 10, "Ю", 10, GREEN, "middle", "bold")
    add_text(svg, cx + size + 8, cy + 4, "В", 10, GREEN, "middle", "bold")
    add_text(svg, cx - size - 8, cy + 4, "З", 10, GREEN, "middle", "bold")


# ============================================================
# LESSON 1: Россия на карте мира
# ============================================================
def lesson1():
    svg = svg_root()
    defs = add_bg(svg)
    add_header(svg, "Россия на карте мира", "Географическое положение, площадь, границы, часовые пояса", 1)

    # Russia map (large, central)
    add_section_box(svg, 15, 90, 480, 310, "Карта России", WHITE, GREEN, GREEN)
    add_russia_detailed(svg, 35, 115, 440, 265, LIGHT_GREEN, GREEN, 2)

    # Major cities on map
    add_city(svg, 85, 230, "Москва", DARK, 9)
    add_city(svg, 420, 145, "Владивосток", DARK, 9)
    add_city(svg, 280, 165, "Новосибирск", DARK, 9)
    add_city(svg, 55, 210, "С.-Петербург", DARK, 9)
    add_city(svg, 380, 180, "Якутск", DARK, 9)
    add_city(svg, 345, 260, "Иркутск", DARK, 9)

    # Compass
    add_compass(svg, 460, 375)

    # Key facts panel
    add_section_box(svg, 510, 90, 275, 310, "Ключевые факты", WHITE, GREEN, DARK_GREEN)

    facts = [
        ("Площадь:", "17 125 000 км\u00b2"),
        ("Место:", "1-е в мире"),
        ("Население:", "~146 млн чел."),
        ("Столица:", "Москва"),
        ("Границы:", "с 18 странами"),
        ("Сухопут.:", "14 500 км"),
        ("Морские:", "38 000 км"),
        ("Часовые пояса:", "11 (с UTC+2 до UTC+12)"),
    ]
    for i, (label, value) in enumerate(facts):
        yy = 130 + i * 32
        add_text(svg, 525, yy, label, 12, GRAY)
        add_text(svg, 525, yy + 14, value, 13, DARK, weight="bold")

    # Time zones diagram
    add_section_box(svg, 15, 410, 770, 105, "Часовые пояса России (11 зон)", WHITE, GREEN, TEAL)

    # Time zone bars
    tz_colors = [DARK_BLUE, BLUE, "#2563EB", "#3B82F6", "#0EA5E9",
                 TEAL, GREEN, "#16A34A", "#22C55E", AMBER, ORANGE]
    tz_names = ["Кал-г", "Мск", "Самра", "Екб", "Омск",
                "Красн", "Иркт", "Якту", "Влдв", "Магд", "Камч"]
    tz_offsets = ["+2", "+3", "+4", "+5", "+6", "+7", "+8", "+9", "+10", "+11", "+12"]

    for i in range(11):
        xx = 40 + i * 67
        add_rect(svg, xx, 450, 58, 30, tz_colors[i], "none", 0, 4)
        add_text(svg, xx + 29, 470, tz_names[i], 9, WHITE, "middle", "bold")
        add_text(svg, xx + 29, 498, tz_offsets[i], 10, DARK, "middle", weight="bold")

    # Neighbors info
    add_section_box(svg, 510, 410, 275, 105, "Соседи России", WHITE, GREEN, GREEN)
    add_text(svg, 525, 448, "Сухопутные: Норвегия, Финляндия,", 10, DARK)
    add_text(svg, 525, 462, "Эстония, Латвия, Литва, Польша,", 10, DARK)
    add_text(svg, 525, 476, "Беларусь, Украина, Грузия, Азер.,", 10, DARK)
    add_text(svg, 525, 490, "Казахстан, Китай, Монголия, КНДР", 10, DARK)
    add_text(svg, 525, 506, "Морские: Япония, США", 10, DARK_BLUE, weight="bold")

    add_footer(svg)
    return svg


# ============================================================
# LESSON 2: Моря и острова России
# ============================================================
def lesson2():
    svg = svg_root()
    defs = add_bg(svg)
    add_header(svg, "Моря и острова России", "Моря трёх океанов, крупные острова", 2)

    # Map with seas
    add_section_box(svg, 15, 90, 480, 310, "Моря России на карте", WHITE, GREEN, GREEN)

    # Background ocean
    add_rect(svg, 25, 120, 460, 270, "#DBEAFE", "none", 0, 4)

    # Russia silhouette
    add_russia_detailed(svg, 60, 130, 380, 240, LIGHT_GREEN, GREEN, 2)

    # Arctic seas (top area)
    add_sea(svg, 150, 140, "Баренцево", DARK_BLUE, 8)
    add_sea(svg, 250, 130, "Карское", DARK_BLUE, 8)
    add_sea(svg, 350, 130, "Лаптевых", DARK_BLUE, 8)
    add_sea(svg, 420, 140, "Вост.-Сиб.", DARK_BLUE, 8)

    # Pacific seas (right area)
    add_sea(svg, 445, 260, "Охотское", DARK_BLUE, 8)
    add_sea(svg, 440, 320, "Японское", DARK_BLUE, 8)
    add_sea(svg, 455, 190, "Берингово", DARK_BLUE, 8)

    # Baltic & Black seas (left)
    add_sea(svg, 45, 230, "Балтийское", DARK_BLUE, 8)
    add_sea(svg, 55, 310, "Чёрное", DARK_BLUE, 8)
    add_sea(svg, 40, 340, "Азовское", DARK_BLUE, 7)

    # Islands on map
    # Novaya Zemlya
    add_circle(svg, 265, 155, 3, ORANGE)
    add_text(svg, 265, 150, "Н.Земля", 7, ORANGE, "middle")
    # Novosibirsk Islands
    add_circle(svg, 385, 155, 3, ORANGE)
    add_text(svg, 385, 150, "Новосиб.", 7, ORANGE, "middle")
    # Sakhalin
    add_circle(svg, 440, 290, 3, ORANGE)
    add_text(svg, 448, 288, "Сахалин", 7, ORANGE, "start")
    # Kuril Islands
    add_circle(svg, 450, 305, 3, ORANGE)
    add_text(svg, 450, 315, "Курилы", 7, ORANGE, "middle")

    # Seas classification
    add_section_box(svg, 510, 90, 275, 155, "Моря по океанам", WHITE, GREEN, DARK_GREEN)

    add_text(svg, 525, 128, "Северный Ледовитый океан:", 11, DARK_BLUE, weight="bold")
    arctic = ["Баренцево", "Белое", "Карское", "Лаптевых",
              "Восточно-Сибирское", "Чукотское"]
    for i, sea in enumerate(arctic):
        add_text(svg, 530, 144 + i * 13, f"\u2022 {sea}", 10, DARK)

    add_text(svg, 525, 224, "Тихий океан:", 11, DARK_BLUE, weight="bold")
    pacific = ["Берингово", "Охотское", "Японское"]
    for i, sea in enumerate(pacific):
        add_text(svg, 530, 238 + i * 13, f"\u2022 {sea}", 10, DARK)

    # Islands info
    add_section_box(svg, 510, 255, 275, 145, "Крупнейшие острова", WHITE, GREEN, TEAL)

    islands = [
        ("Остров", "Площадь (км\u00b2)"),
        ("Сахалин", "76 400"),
        ("Новая Земля", "82 600"),
        ("Врангеля", "7 608"),
        ("Курильские", "10 500"),
        ("Новосибирские", "38 400"),
        ("Земля Франца-И.", "16 100"),
    ]
    for i, (name, area) in enumerate(islands):
        yy = 290 + i * 16
        if i == 0:
            add_text(svg, 525, yy, name, 10, WHITE, weight="bold")
            add_text(svg, 680, yy, area, 10, WHITE, "end", weight="bold")
            add_rect(svg, 520, yy - 12, 250, 16, GREEN, "none", 0, 2)
        else:
            add_text(svg, 525, yy, name, 10, DARK)
            add_text(svg, 680, yy, area, 10, DARK_GREEN, "end", weight="bold")

    # Key fact
    add_section_box(svg, 15, 410, 480, 105, "Особенности морей", WHITE, GREEN, GREEN)
    add_text(svg, 30, 448, "\u2022 Россия омывается 13 морями трёх океанов", 12, DARK)
    add_text(svg, 30, 466, "\u2022 Арктические моря замерзают на 6-9 месяцев", 12, DARK)
    add_text(svg, 30, 484, "\u2022 Северный морской путь \u2014 кратчайший маршрут", 12, DARK)
    add_text(svg, 30, 502, "\u2022 Курильские о-ва \u2014 предмет спора с Японией", 12, DARK_BLUE)

    # Caspian note
    add_section_box(svg, 510, 410, 275, 105, "Каспийское море", WHITE, GREEN, AMBER)
    add_text(svg, 525, 448, "Крупнейшее озеро мира!", 12, BROWN, weight="bold")
    add_text(svg, 525, 466, "Площадь: 371 000 км\u00b2", 11, DARK)
    add_text(svg, 525, 482, "Глубина: до 1025 м", 11, DARK)
    add_text(svg, 525, 498, "Омывает берега 5 стран", 11, DARK)

    add_footer(svg)
    return svg


# ============================================================
# LESSON 3: Рельеф России
# ============================================================
def lesson3():
    svg = svg_root()
    defs = add_bg(svg)
    add_header(svg, "Рельеф России", "Равнины, горы, крупнейшие формы рельефа", 3)

    # Elevation profile
    add_section_box(svg, 15, 90, 770, 200, "Профиль рельефа России (запад \u2192 восток)", WHITE, GREEN, GREEN)

    # Profile base line
    add_line(svg, 50, 260, 760, 260, DARK, 1.5)
    add_line(svg, 50, 260, 50, 110, DARK, 1.5)

    # Y-axis labels (elevation)
    add_text(svg, 42, 118, "3000", 8, GRAY, "end")
    add_text(svg, 42, 155, "2000", 8, GRAY, "end")
    add_text(svg, 42, 195, "1000", 8, GRAY, "end")
    add_text(svg, 42, 260, "0", 8, GRAY, "end")
    add_line(svg, 50, 120, 760, 120, GRAY, 0.5, "3,3")
    add_line(svg, 50, 155, 760, 155, GRAY, 0.5, "3,3")
    add_line(svg, 50, 195, 760, 195, GRAY, 0.5, "3,3")

    # Elevation profile line (west to east)
    profile = "50,245 80,240 110,242 140,248 160,250 "  # East European Plain
    profile += "200,230 220,190 240,150 260,120 270,135 "  # Ural Mountains
    profile += "290,230 310,240 340,245 370,248 400,240 "  # West Siberian Plain
    profile += "430,225 445,210 455,235 465,242 "  # Central Siberian Plateau
    profile += "490,200 510,140 530,110 540,130 "  # Altai/Sayan
    profile += "560,220 580,230 600,225 "  # Transbaikal
    profile += "620,180 640,130 650,110 660,140 "  # Kamchatka ranges
    profile += "680,200 700,230 720,240 750,248 760,252"

    add_polyline(svg, profile, GREEN, 2.5, "none")
    # Fill under the profile
    fill_profile = profile + f" 760,260 50,260"
    add_polygon(svg, fill_profile, LIGHT_GREEN, "none", 0)

    # Labels on profile
    add_text(svg, 105, 258, "Вост.-Европейская равнина", 8, DARK, "middle")
    add_text(svg, 255, 112, "Урал", 9, RED, "middle", "bold")
    add_text(svg, 370, 258, "Зап.-Сибирская равнина", 8, DARK, "middle")
    add_text(svg, 455, 258, "Ср.-Сиб. плоскогорье", 8, DARK, "middle")
    add_text(svg, 525, 102, "Алтай", 9, RED, "middle", "bold")
    add_text(svg, 645, 102, "Камчатка", 9, RED, "middle", "bold")

    # Major landforms map
    add_section_box(svg, 15, 300, 380, 170, "Крупнейшие формы рельефа", WHITE, GREEN, TEAL)

    items = [
        ("Восточно-Европейская равнина", "~4 млн км\u00b2", "0-400 м"),
        ("Западно-Сибирская равнина", "~2.6 млн км\u00b2", "0-200 м"),
        ("Среднесибирское плоскогорье", "~3.5 млн км\u00b2", "500-1700 м"),
        ("Уральские горы", "~2400 км", "1895 м (Народная)"),
        ("Кавказские горы", "~1500 км", "5642 м (Эльбрус)"),
        ("Алтай", "~2000 км", "4506 м (Белуха)"),
    ]
    for i, (name, size, elev) in enumerate(items):
        yy = 335 + i * 21
        add_text(svg, 25, yy, f"\u2022 {name}", 10, DARK)
        add_text(svg, 290, yy, size, 9, DARK_GREEN, weight="bold")
        add_text(svg, 340, yy + 10, elev, 8, GRAY)

    # Mountains diagram
    add_section_box(svg, 410, 300, 375, 170, "Высочайшие вершины", WHITE, GREEN, GREEN)

    # Bar chart of mountain heights
    mountains = [
        ("Эльбрус", 5642),
        ("Дыхтау", 5204),
        ("Белуха", 4506),
        ("Ключевская", 4750),
        ("Народная", 1895),
    ]
    max_h = 6000
    bar_w = 45
    for i, (name, height) in enumerate(mountains):
        xx = 435 + i * 68
        bar_h = int((height / max_h) * 110)
        add_rect(svg, xx, 430 - bar_h, bar_w, bar_h, TEAL if i < 4 else GREEN, "none", 0, 3)
        add_text(svg, xx + bar_w // 2, 442, f"{height}", 8, DARK, "middle", weight="bold")
        add_text(svg, xx + bar_w // 2, 455, name, 7, DARK, "middle")

    add_text(svg, 597, 345, "м над ур. моря", 9, GRAY, "middle")
    add_line(svg, 430, 430, 770, 430, GRAY, 1)

    # Key fact
    add_section_box(svg, 15, 480, 770, 50, "Закономерность", WHITE, GREEN, DARK_GREEN)
    add_text(svg, 400, 510, "Рельеф России: равнины на западе и севере, горы \u2014 на юге и востоке", 13, DARK, "middle")
    add_text(svg, 400, 524, "Высшая точка \u2014 г. Эльбрус (5642 м), низшая \u2014 Каспийское море (-28 м)", 11, DARK_GREEN, "middle")

    add_footer(svg)
    return svg


# ============================================================
# LESSON 4: Полезные ископаемые
# ============================================================
def lesson4():
    svg = svg_root()
    defs = add_bg(svg)
    add_header(svg, "Полезные ископаемые", "Нефть, газ, уголь, руды \u2014 размещение и значение", 4)

    # Minerals map
    add_section_box(svg, 15, 90, 480, 290, "Карта полезных ископаемых", WHITE, GREEN, GREEN)

    # Russia silhouette
    add_russia_detailed(svg, 35, 115, 440, 250, "#FEF9C3", GREEN, 1.5)

    # Oil & Gas (Western Siberia)
    add_circle(svg, 280, 220, 8, "#1C1917")
    add_text(svg, 290, 215, "Нефть", 8, "#1C1917")
    add_circle(svg, 260, 235, 8, "#7C3AED")
    add_text(svg, 270, 232, "Газ", 8, "#7C3AED")

    # Coal (Kuzbass)
    add_circle(svg, 330, 230, 8, "#374151")
    add_text(svg, 340, 228, "Уголь (Кузбасс)", 8, "#374151")

    # Iron ore (KMA)
    add_circle(svg, 100, 230, 8, "#B91C1C")
    add_text(svg, 110, 228, "Жел. руда (КМА)", 8, "#B91C1C")

    # Gold (Lena region)
    add_circle(svg, 370, 200, 8, "#CA8A04")
    add_text(svg, 380, 197, "Золото", 8, "#CA8A04")

    # Diamonds (Yakutia)
    add_circle(svg, 395, 175, 8, "#06B6D4")
    add_text(svg, 405, 172, "Алмазы", 8, "#06B6D4")

    # Nickel (Norilsk)
    add_circle(svg, 320, 155, 8, "#6B7280")
    add_text(svg, 330, 153, "Никель", 8, "#6B7280")

    # Oil (Volga-Ural)
    add_circle(svg, 140, 230, 8, "#1C1917")
    add_text(svg, 85, 243, "Нефть (Волго-Урал)", 8, "#1C1917")

    # Legend
    add_section_box(svg, 510, 90, 275, 180, "Легенда", WHITE, GREEN, DARK_GREEN)

    legend_items = [
        ("#1C1917", "Нефть"),
        ("#7C3AED", "Природный газ"),
        ("#374151", "Уголь"),
        ("#B91C1C", "Железная руда"),
        ("#CA8A04", "Золото"),
        ("#06B6D4", "Алмазы"),
        ("#6B7280", "Цветные металлы"),
        ("#DC2626", "Алюминиевые руды"),
    ]
    for i, (color, name) in enumerate(legend_items):
        yy = 130 + i * 18
        add_circle(svg, 530, yy - 3, 5, color)
        add_text(svg, 542, yy, name, 11, DARK)

    # Major basins table
    add_section_box(svg, 15, 390, 380, 140, "Крупнейшие бассейны", WHITE, GREEN, TEAL)

    basins = [
        ("Нефть", "Зап.-Сибирский, Волго-Уральский"),
        ("Газ", "Зап.-Сибирский (Уренгой), Оренбург"),
        ("Уголь", "Кузбасс, Канско-Ачинский, Донбасс"),
        ("Жел. руда", "КМА, Кольский п-ов, Урал"),
        ("Алмазы", "Якутия (Мирный)"),
        ("Золото", "Ленский р-н, Колыма, Алдан"),
    ]
    for i, (mineral, location) in enumerate(basins):
        yy = 425 + i * 17
        add_text(svg, 25, yy, mineral, 10, DARK_GREEN, weight="bold")
        add_text(svg, 105, yy, location, 10, DARK)

    # Russia's rank
    add_section_box(svg, 410, 390, 375, 140, "Мировые рейтинги России", WHITE, GREEN, GREEN)

    ranks = [
        ("Нефть", "2-е место"),
        ("Природный газ", "1-е место"),
        ("Уголь", "6-е место"),
        ("Железная руда", "4-е место"),
        ("Алмазы", "1-е место"),
        ("Никель", "3-е место"),
    ]
    for i, (mineral, rank) in enumerate(ranks):
        yy = 425 + i * 17
        add_text(svg, 425, yy, mineral, 11, DARK)
        is_first = "1-е" in rank
        add_text(svg, 650, yy, rank, 12, RED if is_first else DARK_GREEN, "end", "bold" if is_first else "normal")

    add_footer(svg)
    return svg


# ============================================================
# LESSON 5: Климатообразующие факторы
# ============================================================
def lesson5():
    svg = svg_root()
    defs = add_bg(svg)
    add_header(svg, "Климатообразующие факторы", "Солнечная радиация, циркуляция, подстилающая поверхность", 5)

    # Solar radiation diagram
    add_section_box(svg, 15, 90, 260, 200, "Солнечная радиация", WHITE, GREEN, GREEN)

    # Sun
    add_circle(svg, 145, 145, 25, AMBER, ORANGE, 2)
    # Rays
    for angle_offset in range(0, 360, 45):
        import math
        x1 = 145 + 30 * math.cos(math.radians(angle_offset))
        y1 = 145 + 30 * math.sin(math.radians(angle_offset))
        x2 = 145 + 40 * math.cos(math.radians(angle_offset))
        y2 = 145 + 40 * math.sin(math.radians(angle_offset))
        add_line(svg, int(x1), int(y1), int(x2), int(y2), AMBER, 2)

    # Radiation arrows
    add_text(svg, 145, 195, "\u2193 \u2193 \u2193", 14, ORANGE, "middle")
    add_text(svg, 145, 215, "Радиация", 11, DARK, "middle", "bold")

    # North-South gradient
    add_text(svg, 25, 240, "Мало (70\u00b0 с.ш.)", 9, BLUE)
    add_text(svg, 160, 240, "Много (45\u00b0 с.ш.)", 9, RED)
    add_rect(svg, 80, 250, 130, 15, AMBER, "none", 0, 3)

    # Radiation gradient bar
    add_rect(svg, 80, 250, 25, 15, "#DBEAFE", "none", 0, 3)
    add_rect(svg, 105, 250, 25, 15, "#BFDBFE", "none", 0, 3)
    add_rect(svg, 130, 250, 25, 15, "#FDE68A", "none", 0, 3)
    add_rect(svg, 155, 250, 25, 15, "#F59E0B", "none", 0, 3)
    add_rect(svg, 180, 250, 25, 15, "#D97706", "none", 0, 3)

    add_text(svg, 25, 275, "Суммарная радиация:", 9, DARK, weight="bold")
    add_text(svg, 25, 287, "от 60 ккал/см\u00b2 (север)", 8, DARK)
    add_text(svg, 25, 298, "до 120 ккал/см\u00b2 (юг)", 8, DARK)

    # Atmospheric circulation
    add_section_box(svg, 290, 90, 250, 200, "Циркуляция ВМ", WHITE, GREEN, TEAL)

    add_text(svg, 415, 125, "Воздушные массы:", 11, DARK, weight="bold")

    vm_types = [
        ("Арктическая", "#DBEAFE", BLUE, "Холодная, сухая"),
        ("Умеренная", "#D1FAE5", GREEN, "Различная"),
        ("Тропическая", "#FDE68A", AMBER, "Тёплая, влажная"),
    ]
    for i, (name, bg, color, desc) in enumerate(vm_types):
        yy = 148 + i * 42
        add_rect(svg, 300, yy - 10, 230, 35, bg, color, 1.5, 5)
        add_text(svg, 415, yy + 3, name, 11, color, "middle", "bold")
        add_text(svg, 415, yy + 16, desc, 9, DARK, "middle")

    # Cyclone/Anticyclone
    add_text(svg, 305, 270, "Циклон: Н \u2192 облачность, осадки", 9, BLUE, weight="bold")
    add_text(svg, 305, 283, "Антициклон: В \u2192 ясная погода", 9, RED, weight="bold")

    # Underlying surface
    add_section_box(svg, 555, 90, 230, 200, "Подстилающая пов-сть", WHITE, GREEN, DARK_GREEN)

    surface_items = [
        ("Рельеф", "Горы преграждают путь ВМ"),
        ("Океаны", "Морской климат (влажный)"),
        ("Континенты", "Континентальный (сухой)"),
        ("Снег/Лёд", "Высокое альбедо (0.8)"),
        ("Леса", "Низкое альбедо (0.15)"),
    ]
    for i, (name, desc) in enumerate(surface_items):
        yy = 130 + i * 28
        add_text(svg, 565, yy, name, 11, DARK_GREEN, weight="bold")
        add_text(svg, 565, yy + 13, desc, 9, GRAY)

    # Interaction diagram
    add_section_box(svg, 15, 300, 770, 130, "Взаимодействие факторов", WHITE, GREEN, GREEN)

    # Three circles overlap diagram
    cx1, cy1 = 200, 370
    cx2, cy2 = 350, 370
    cx3, cy3 = 275, 340

    add_ellipse(svg, cx1, cy1, 80, 45, LIGHT_BLUE, BLUE, 1.5)
    add_ellipse(svg, cx2, cy2, 80, 45, LIGHT_GREEN, GREEN, 1.5)
    add_ellipse(svg, cx3, cy3, 80, 45, LIGHT_TEAL, TEAL, 1.5)

    add_text(svg, cx1 - 35, cy1 + 5, "Радиация", 10, BLUE, "middle", "bold")
    add_text(svg, cx2 + 35, cy2 + 5, "Циркуляция", 10, GREEN, "middle", "bold")
    add_text(svg, cx3, cy3 - 5, "Поверхность", 10, TEAL, "middle", "bold")

    # Climate result
    add_text(svg, 275, 365, "Климат", 12, DARK, "middle", "bold")

    # Types of climate in Russia
    add_text(svg, 520, 335, "Типы климата России:", 12, DARK_GREEN, weight="bold")
    climates = [
        "Арктический",
        "Субарктический",
        "Умеренно-континентальный",
        "Континентальный",
        "Резко континентальный",
        "Муссонный",
    ]
    for i, cl in enumerate(climates):
        add_text(svg, 530, 355 + i * 14, f"\u2022 {cl}", 10, DARK)

    # Key fact
    add_section_box(svg, 15, 440, 770, 90, "Главное", WHITE, GREEN, DARK_GREEN)
    add_text(svg, 400, 472, "Климат определяется тремя факторами: солнечной радиацией,", 13, DARK, "middle")
    add_text(svg, 400, 490, "атмосферной циркуляцией и подстилающей поверхностью", 13, DARK_GREEN, "middle", "bold")
    add_text(svg, 400, 510, "Россия \u2014 самая холодная страна мира (ср. t \u2248 -5.5\u00b0C)", 11, BLUE, "middle")

    add_footer(svg)
    return svg


# ============================================================
# LESSON 6: Температура и осадки
# ============================================================
def lesson6():
    svg = svg_root()
    defs = add_bg(svg)
    add_header(svg, "Температура и осадки", "Климатические пояса, карты температур января и июля", 6)

    # January temperature map
    add_section_box(svg, 15, 90, 380, 200, "Температура января (\u00b0C)", WHITE, GREEN, GREEN)

    # Simplified Russia with isotherms
    add_rect(svg, 30, 120, 350, 155, "#DBEAFE", "none", 0, 3)
    add_russia_silhouette(svg, 50, 125, 310, 140, "#FEF3C7", GREEN, 1.5)

    # Isotherms
    add_path(svg, "M60,150 Q180,170 330,155", BLUE, 1.5, "none")
    add_text(svg, 340, 152, "0\u00b0C", 9, BLUE, weight="bold")

    add_path(svg, "M60,175 Q180,190 330,175", "#3B82F6", 1.5, "none")
    add_text(svg, 340, 172, "-10\u00b0C", 9, "#3B82F6", weight="bold")

    add_path(svg, "M60,200 Q180,215 330,200", "#1D4ED8", 1.5, "none")
    add_text(svg, 340, 197, "-20\u00b0C", 9, "#1D4ED8", weight="bold")

    add_path(svg, "M60,225 Q180,240 330,225", DARK_BLUE, 1.5, "none")
    add_text(svg, 340, 222, "-30\u00b0C", 9, DARK_BLUE, weight="bold")

    add_path(svg, "M100,248 Q200,260 300,248", "#1E3A5F", 1.5, "none")
    add_text(svg, 310, 248, "-40\u00b0C", 9, "#1E3A5F", weight="bold")

    # Cold pole
    add_circle(svg, 260, 240, 4, RED)
    add_text(svg, 268, 248, "Оймякон -71\u00b0C", 8, RED, weight="bold")

    add_text(svg, 205, 268, "Полюс холода: Оймякон и Верхоянск", 8, RED)

    # July temperature map
    add_section_box(svg, 410, 90, 375, 200, "Температура июля (\u00b0C)", WHITE, GREEN, TEAL)

    add_rect(svg, 425, 120, 345, 155, "#FEF3C7", "none", 0, 3)
    add_russia_silhouette(svg, 445, 125, 310, 140, "#FDE68A", GREEN, 1.5)

    # July isotherms
    add_path(svg, "M455,150 Q570,145 740,155", RED, 1.5, "none")
    add_text(svg, 740, 152, "+20\u00b0C", 9, RED, weight="bold")

    add_path(svg, "M455,175 Q570,168 740,178", ORANGE, 1.5, "none")
    add_text(svg, 740, 175, "+15\u00b0C", 9, ORANGE, weight="bold")

    add_path(svg, "M455,200 Q570,195 740,205", AMBER, 1.5, "none")
    add_text(svg, 740, 202, "+10\u00b0C", 9, AMBER, weight="bold")

    add_path(svg, "M455,225 Q570,220 740,230", "#CA8A04", 1.5, "none")
    add_text(svg, 740, 227, "+5\u00b0C", 9, "#CA8A04", weight="bold")

    add_text(svg, 600, 268, "Лето: тёплое на большей части", 8, DARK_GREEN)

    # Precipitation map
    add_section_box(svg, 15, 300, 380, 140, "Осадки (мм/год)", WHITE, GREEN, GREEN)

    # Precipitation bar chart by region
    regions = [
        ("Черномор.", 1200),
        ("Зап. Сибирь", 400),
        ("Центр. Сиб.", 300),
        ("Сев.-Вост.", 200),
        ("Дальн. Вост.", 700),
    ]
    max_p = 1300
    for i, (name, precip) in enumerate(regions):
        xx = 30 + i * 72
        bar_h = int((precip / max_p) * 80)
        add_rect(svg, xx, 410 - bar_h, 50, bar_h, TEAL, "none", 0, 3)
        add_text(svg, xx + 25, 425, f"{precip}", 8, DARK, "middle", weight="bold")
        add_text(svg, xx + 25, 435, name, 7, DARK, "middle")

    add_text(svg, 195, 435, "мм/год", 9, GRAY, "middle")

    # Climate zones
    add_section_box(svg, 410, 300, 375, 140, "Климатические пояса", WHITE, GREEN, DARK_GREEN)

    zones = [
        ("Арктический", ICE_BLUE, "T < 0\u00b0C, осадков мало"),
        ("Субарктический", LIGHT_BLUE, "T -10...-30\u00b0C (янв)"),
        ("Умеренный", LIGHT_GREEN, "T -5...-40\u00b0C (янв)"),
        ("Субтропический", "#FDE68A", "T +5...+10\u00b0C (янв)"),
    ]
    for i, (name, color, desc) in enumerate(zones):
        yy = 335 + i * 25
        add_rect(svg, 420, yy - 8, 15, 15, color, DARK, 1, 3)
        add_text(svg, 440, yy + 3, name, 11, DARK, weight="bold")
        add_text(svg, 555, yy + 3, desc, 9, GRAY)

    # Amplitude
    add_section_box(svg, 15, 450, 770, 80, "Континентальность климата", WHITE, GREEN, GREEN)
    add_text(svg, 30, 478, "Амплитуда температур:", 13, DARK, weight="bold")
    add_text(svg, 30, 498, "Мурманск: 13\u00b0C (морской)", 11, BLUE)
    add_text(svg, 230, 498, "Москва: 28\u00b0C (умер.-конт.)", 11, DARK_GREEN)
    add_text(svg, 440, 498, "Верхоянск: 63\u00b0C (резко конт.)", 11, RED)
    add_text(svg, 680, 498, "Якутск: 62\u00b0C", 11, ORANGE)
    add_text(svg, 400, 520, "Чем дальше от океана \u2014 тем больше амплитуда и континентальнее климат", 11, DARK_GREEN, "middle")

    add_footer(svg)
    return svg


# ============================================================
# LESSON 7: Реки России
# ============================================================
def lesson7():
    svg = svg_root()
    defs = add_bg(svg)
    add_header(svg, "Реки России", "Волга, Обь, Енисей, Лена, Амур \u2014 речные системы", 7)

    # Rivers map
    add_section_box(svg, 15, 90, 480, 260, "Крупнейшие реки России", WHITE, GREEN, GREEN)

    # Russia silhouette
    add_russia_detailed(svg, 30, 110, 450, 230, "#E0F2FE", GREEN, 1.5)

    # River lines with labels
    # Volga
    add_polyline(svg, "85,225 100,220 115,218 130,225 140,235 145,250 148,265", BLUE, 2.5, "none")
    add_text(svg, 125, 213, "Волга", 9, BLUE, "middle", "bold")

    # Ob
    add_polyline(svg, "230,140 235,160 240,180 245,200 250,220 255,240", BLUE, 2.5, "none")
    add_text(svg, 258, 185, "Обь", 9, BLUE, "middle", "bold")

    # Yenisei
    add_polyline(svg, "290,140 295,165 300,190 305,215 310,240", BLUE, 2.5, "none")
    add_text(svg, 315, 190, "Енисей", 9, BLUE, "middle", "bold")

    # Lena
    add_polyline(svg, "360,130 365,155 370,180 375,210 380,240", BLUE, 2.5, "none")
    add_text(svg, 390, 180, "Лена", 9, BLUE, "middle", "bold")

    # Amur
    add_polyline(svg, "395,250 410,245 425,240 440,245 450,255", BLUE, 2.5, "none")
    add_text(svg, 425, 236, "Амур", 9, BLUE, "middle", "bold")

    # Don
    add_polyline(svg, "105,240 115,248 125,260 130,275", "#60A5FA", 1.5, "none")
    add_text(svg, 118, 255, "Дон", 8, "#60A5FA", "middle", "bold")

    # Ocean basins
    add_text(svg, 150, 135, "Бассейн Сев. Ледовитого ок.", 8, DARK_BLUE, "middle")
    add_text(svg, 430, 270, "Бассейн Тихого ок.", 8, DARK_BLUE, "middle")
    add_text(svg, 80, 270, "Бассейн Каспия", 8, DARK_BLUE, "middle")

    # River data table
    add_section_box(svg, 510, 90, 275, 260, "Характеристики рек", WHITE, GREEN, DARK_GREEN)

    # Table header
    add_rect(svg, 520, 122, 255, 18, GREEN, "none", 0, 3)
    add_text(svg, 530, 136, "Река", 9, WHITE, weight="bold")
    add_text(svg, 580, 136, "Длина", 9, WHITE, "middle", weight="bold")
    add_text(svg, 635, 136, "Бассейн", 9, WHITE, "middle", weight="bold")
    add_text(svg, 710, 136, "Куда", 9, WHITE, "middle", weight="bold")

    rivers = [
        ("Волга", "3530", "1 360", "Каспий"),
        ("Обь", "3650", "2 990", "Карск."),
        ("Енисей", "3487", "2 580", "Карск."),
        ("Лена", "4400", "2 490", "Лапт."),
        ("Амур", "2824", "1 855", "Охот."),
        ("Дон", "1870", "422", "Азов."),
        ("Печора", "1809", "322", "Баренц."),
        ("Колыма", "2129", "643", "В.-Сиб."),
        ("Сев. Двина", "744", "357", "Белое"),
    ]
    for i, (name, length, basin, dest) in enumerate(rivers):
        yy = 155 + i * 18
        if i % 2 == 0:
            add_rect(svg, 520, yy - 11, 255, 17, LIGHT_GREEN, "none", 0, 2)
        add_text(svg, 530, yy, name, 9, DARK_GREEN, weight="bold")
        add_text(svg, 580, yy, length, 9, DARK, "middle")
        add_text(svg, 635, yy, basin, 9, DARK, "middle")
        add_text(svg, 710, yy, dest, 9, GRAY, "middle")

    add_text(svg, 647, 140, "(км)", 7, LIGHT_GREEN)
    add_text(svg, 647, 150, "тыс.км\u00b2", 7, LIGHT_GREEN)

    # River system diagram
    add_section_box(svg, 15, 360, 380, 130, "Речная система", WHITE, GREEN, TEAL)

    # Simplified river system tree
    add_line(svg, 200, 380, 200, 470, BLUE, 2.5)  # Main river
    add_text(svg, 208, 435, "Главная река", 9, BLUE, weight="bold")

    # Tributaries
    add_line(svg, 150, 400, 200, 410, "#60A5FA", 1.5)  # Left tributary
    add_line(svg, 200, 410, 250, 395, "#60A5FA", 1.5)  # Right tributary
    add_line(svg, 120, 430, 200, 440, "#60A5FA", 1.5)  # Left tributary
    add_line(svg, 200, 450, 260, 440, "#60A5FA", 1.5)  # Right tributary

    add_text(svg, 105, 405, "Приток", 8, "#60A5FA", "middle")
    add_text(svg, 265, 392, "Приток", 8, "#60A5FA", "middle")

    # River terms
    add_text(svg, 260, 410, "Устье \u2014 место впадения", 9, DARK)
    add_text(svg, 260, 425, "Исток \u2014 начало реки", 9, DARK)
    add_text(svg, 260, 440, "Бассейн \u2014 площадь стока", 9, DARK)
    add_text(svg, 260, 455, "Водораздел \u2014 граница", 9, DARK)
    add_text(svg, 260, 470, "  между бассейнами", 9, GRAY)

    # Feeding types
    add_section_box(svg, 410, 360, 375, 130, "Питание рек", WHITE, GREEN, GREEN)

    feed_types = [
        ("Снеговое", "~55% всех рек", LIGHT_BLUE),
        ("Дождевое", "Дальний Восток", "#BFDBFE"),
        ("Ледниковое", "Кавказ, Алтай", "#E0F2FE"),
        ("Подземное", "Равнинные реки", LIGHT_GREEN),
        ("Смешанное", "Большинство рек", LIGHT_TEAL),
    ]
    for i, (name, desc, color) in enumerate(feed_types):
        yy = 395 + i * 18
        add_rect(svg, 420, yy - 8, 12, 12, color, GREEN, 1, 3)
        add_text(svg, 440, yy + 2, name, 11, DARK_GREEN, weight="bold")
        add_text(svg, 560, yy + 2, desc, 10, GRAY)

    add_footer(svg)
    return svg


# ============================================================
# LESSON 8: Озёра и водохранилища
# ============================================================
def lesson8():
    svg = svg_root()
    defs = add_bg(svg)
    add_header(svg, "Озёра и водохранилища", "Байкал, Ладога, Онега \u2014 крупнейшие озёра", 8)

    # Lakes map
    add_section_box(svg, 15, 90, 480, 240, "Крупнейшие озёра России", WHITE, GREEN, GREEN)

    add_russia_detailed(svg, 30, 110, 440, 210, "#E0F2FE", GREEN, 1.5)

    # Lake markers (approximate positions)
    lake_positions = [
        (82, 205, "Ладога"),
        (78, 195, "Онега"),
        (200, 170, "Байкал"),
        (55, 240, "Чудское"),
        (100, 230, "Ильмень"),
        (260, 140, "Таймыр"),
        (130, 290, "Каспийское"),
        (350, 155, "Ханка"),
    ]
    for lx, ly, name in lake_positions:
        add_ellipse(svg, lx, ly, 8, 5, BLUE, BLUE, 1.5)
        add_text(svg, lx, ly - 9, name, 8, DARK_BLUE, "middle", "bold")

    # Baikal close-up
    add_section_box(svg, 510, 90, 275, 240, "Озеро Байкал", WHITE, GREEN, DARK_GREEN)

    # Baikal shape (elongated)
    add_ellipse(svg, 647, 180, 35, 90, "#3B82F6", BLUE, 2)
    add_text(svg, 647, 180, "Байкал", 10, WHITE, "middle", "bold")

    baikal_facts = [
        ("Глубина:", "1642 м (1-е в мире)"),
        ("Объём:", "23 615 км\u00b3 (20% пресн.)"),
        ("Длина:", "636 км"),
        ("Возраст:", "~25 млн лет"),
        ("Видов:", ">3500 (80% эндем.)"),
        ("Прозрачность:", "до 40 м"),
        ("Толщина льда:", "до 1.5 м"),
    ]
    for i, (label, value) in enumerate(baikal_facts):
        yy = 125 + i * 17
        add_text(svg, 525, yy, label, 10, GRAY)
        add_text(svg, 610, yy, value, 10, DARK_GREEN, weight="bold")

    add_text(svg, 647, 250, "Жемчужина Сибири!", 10, BLUE, "middle", "bold")

    # Lake types
    add_section_box(svg, 15, 340, 380, 120, "Типы озёрных котловин", WHITE, GREEN, TEAL)

    lake_types = [
        ("Тектонические", "Байкал, Телецкое", "Глубокие, вытянутые"),
        ("Ледниковые", "Ладога, Онега", "Крупные, на севере"),
        ("Вулканические", "Кроноцкое", "В кратерах вулканов"),
        ("Старицы", "Мелкие, пойменные", "Пожилые русла рек"),
        ("Карстовые", "На юге России", "В растворимых породах"),
    ]
    for i, (name, examples, desc) in enumerate(lake_types):
        yy = 370 + i * 18
        add_text(svg, 25, yy, name, 10, DARK_GREEN, weight="bold")
        add_text(svg, 155, yy, examples, 9, DARK)
        add_text(svg, 310, yy, desc, 8, GRAY)

    # Largest lakes table
    add_section_box(svg, 410, 340, 375, 120, "Крупнейшие озёра", WHITE, GREEN, GREEN)

    # Table header
    add_rect(svg, 420, 372, 355, 16, GREEN, "none", 0, 3)
    add_text(svg, 435, 385, "Озеро", 9, WHITE, weight="bold")
    add_text(svg, 530, 385, "Площадь", 9, WHITE, "middle", weight="bold")
    add_text(svg, 620, 385, "Глубина", 9, WHITE, "middle", weight="bold")
    add_text(svg, 710, 385, "Тип", 9, WHITE, "middle", weight="bold")

    lakes_data = [
        ("Каспийское", "371 000", "1025", "Тект."),
        ("Байкал", "31 500", "1642", "Тект."),
        ("Ладога", "17 700", "230", "Ледн."),
        ("Онега", "9 700", "127", "Ледн."),
        ("Таймыр", "4 560", "26", "Ледн."),
        ("Ханка", "4 190", "10.6", "Тект."),
    ]
    for i, (name, area, depth, ltype) in enumerate(lakes_data):
        yy = 402 + i * 14
        if i % 2 == 0:
            add_rect(svg, 420, yy - 10, 355, 14, LIGHT_GREEN, "none", 0, 2)
        add_text(svg, 435, yy, name, 9, DARK_GREEN, weight="bold")
        add_text(svg, 530, yy, area, 8, DARK, "middle")
        add_text(svg, 620, yy, depth, 8, DARK, "middle")
        add_text(svg, 710, yy, ltype, 8, GRAY, "middle")

    # Reservoirs
    add_section_box(svg, 15, 470, 770, 60, "Водохранилища", WHITE, GREEN, DARK_GREEN)
    add_text(svg, 30, 495, "Водохранилища \u2014 искусственные водоёмы для ГЭС, водоснабжения, судоходства", 12, DARK)
    add_text(svg, 30, 512, "Крупнейшие: Куйбышевское, Рыбинское, Братское, Волгоградское, Красноярское", 11, DARK_GREEN, weight="bold")
    add_text(svg, 630, 512, "ГЭС \u2192 энергия", 10, TEAL, weight="bold")

    add_footer(svg)
    return svg


# ============================================================
# LESSON 9: Природные зоны России
# ============================================================
def lesson9():
    svg = svg_root()
    defs = add_bg(svg)
    add_header(svg, "Природные зоны России", "Тундра, тайга, степь, пустыня \u2014 от севера к югу", 9)

    # Zonal map
    add_section_box(svg, 15, 90, 480, 200, "Карта природных зон", WHITE, GREEN, GREEN)

    # Horizontal zones from north to south
    zone_colors = [
        (SNOW, "Арктическая пустыня"),
        ("#BFDBFE", "Тундра"),
        ("#A7F3D0", "Лесотундра"),
        ("#34D399", "Тайга"),
        ("#86EFAC", "Смешанные леса"),
        ("#BEF264", "Лесостепь"),
        (SAND, "Степь"),
        ("#FDE68A", "Полупустыня"),
        ("#FDBA74", "Пустыня"),
    ]

    for i, (color, name) in enumerate(zone_colors):
        y_start = 120 + i * 18
        add_rect(svg, 30, y_start, 450, 18, color, GREEN, 0.5, 2)
        add_text(svg, 255, y_start + 13, name, 8, DARK, "middle", "bold")

    # Direction arrow
    add_text(svg, 485, 200, "С", 12, RED, "middle", "bold")
    add_line(svg, 485, 210, 485, 280, DARK, 1.5)
    add_text(svg, 485, 295, "Ю", 12, GREEN, "middle", "bold")

    # Zone characteristics
    add_section_box(svg, 510, 90, 275, 200, "Характеристики зон", WHITE, GREEN, DARK_GREEN)

    zone_data = [
        ("Аркт. пустыня", "-30\u00b0C", "200", "Лишайники"),
        ("Тундра", "-15\u00b0C", "300", "Мхи, ягель"),
        ("Тайга", "-10\u00b0C", "600", "Хвойные леса"),
        ("Смеш. леса", "-5\u00b0C", "700", "Хв.+лист."),
        ("Степь", "-2\u00b0C", "400", "Травы"),
        ("Пустыня", "+10\u00b0C", "150", "Саксаул"),
    ]

    # Mini table
    add_rect(svg, 520, 120, 245, 14, GREEN, "none", 0, 2)
    add_text(svg, 535, 132, "Зона", 8, WHITE, weight="bold")
    add_text(svg, 610, 132, "Янв.", 8, WHITE, "middle", weight="bold")
    add_text(svg, 660, 132, "Ос.", 8, WHITE, "middle", weight="bold")
    add_text(svg, 730, 132, "Раст.", 8, WHITE, "middle", weight="bold")

    for i, (zone, temp, precip, veg) in enumerate(zone_data):
        yy = 150 + i * 20
        if i % 2 == 0:
            add_rect(svg, 520, yy - 10, 245, 18, LIGHT_GREEN, "none", 0, 2)
        add_text(svg, 535, yy, zone, 8, DARK_GREEN, weight="bold")
        add_text(svg, 610, yy, temp, 8, DARK, "middle")
        add_text(svg, 660, yy, precip, 8, DARK, "middle")
        add_text(svg, 730, yy, veg, 8, GRAY, "middle")

    add_text(svg, 535, 278, "Осадки (мм/год)", 8, GRAY)

    # Law of zonality
    add_section_box(svg, 15, 300, 380, 130, "Закон широтной зональности", WHITE, GREEN, GREEN)

    add_text(svg, 30, 335, "Смена природных зон от экватора", 12, DARK)
    add_text(svg, 30, 352, "к полюсам \u2014 широтная зональность.", 12, DARK_GREEN, weight="bold")
    add_text(svg, 30, 375, "Причина: изменение количества", 11, DARK)
    add_text(svg, 30, 392, "солнечной радиации с широтой.", 11, DARK)
    add_text(svg, 30, 415, "Высотная поясность \u2014 смена зон", 11, DARK)
    add_text(svg, 30, 432, "в горах с высотой (аналог зональности).", 11, DARK_GREEN)

    # Altitudinal zonation
    add_section_box(svg, 410, 300, 375, 130, "Высотная поясность (Кавказ)", WHITE, GREEN, TEAL)

    # Mountain with zones
    # Peak
    add_polygon(svg, "520,310 580,370 460,370", SNOW, GREEN, 1)
    add_text(svg, 520, 345, "Ледники", 7, DARK_BLUE, "middle")

    # Alpine meadows
    add_polygon(svg, "460,370 580,370 595,400 445,400", "#BFDBFE", GREEN, 0.5)
    add_text(svg, 520, 390, "Альп. луга", 7, DARK, "middle")

    # Subalpine
    add_polygon(svg, "445,400 595,400 610,425 430,425", "#A7F3D0", GREEN, 0.5)
    add_text(svg, 520, 417, "Субальп.", 7, DARK, "middle")

    # Forest
    add_polygon(svg, "430,425 610,425 625,445 415,445", "#34D399", GREEN, 0.5)
    add_text(svg, 520, 440, "Лесной", 7, DARK, "middle")

    # Steppe
    add_polygon(svg, "415,445 625,445 640,465 400,465", SAND, GREEN, 0.5)
    add_text(svg, 520, 460, "Степной", 7, DARK, "middle")

    add_text(svg, 700, 330, "5600 м", 8, DARK_BLUE)
    add_text(svg, 700, 380, "3000 м", 8, GRAY)
    add_text(svg, 700, 410, "2000 м", 8, GRAY)
    add_text(svg, 700, 440, "1000 м", 8, GRAY)
    add_text(svg, 700, 460, "0 м", 8, GRAY)

    # Key fact
    add_section_box(svg, 15, 440, 770, 90, "Главное о природных зонах", WHITE, GREEN, DARK_GREEN)
    add_text(svg, 400, 470, "Природная зона \u2014 крупный природный комплекс со своими условиями", 13, DARK, "middle")
    add_text(svg, 400, 490, "тепла и влаги, почвами, растительностью и животным миром", 13, DARK_GREEN, "middle")
    add_text(svg, 400, 510, "Тайга \u2014 крупнейшая природная зона России (~50% территории)", 12, GREEN, "middle", "bold")

    add_footer(svg)
    return svg


# ============================================================
# MAIN
# ============================================================
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    lessons = [
        (1, lesson1),
        (2, lesson2),
        (3, lesson3),
        (4, lesson4),
        (5, lesson5),
        (6, lesson6),
        (7, lesson7),
        (8, lesson8),
        (9, lesson9),
    ]

    results = []
    for num, func in lessons:
        svg = func()
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
        tree = ET.ElementTree(svg)
        ET.indent(tree, space="  ")
        tree.write(filepath, encoding="unicode", xml_declaration=True)

        # Validate
        try:
            ET.parse(filepath)
            status = "OK"
        except ET.ParseError as e:
            status = f"FAIL: {e}"

        results.append((num, filepath, status))
        print(f"Lesson {num}: {filepath} - {status}")

    print("\n" + "=" * 60)
    print("GENERATION COMPLETE")
    print("=" * 60)
    for num, path, status in results:
        print(f"  Lesson {num}: {status}")

    # Count total valid
    valid = sum(1 for _, _, s in results if s == "OK")
    print(f"\nValid: {valid}/{len(results)}")


if __name__ == "__main__":
    main()
