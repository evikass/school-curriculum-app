#!/usr/bin/env python3
"""
Generate Grade 8 History SVG images for 5 lessons.
Russian text, red/rose color scheme (#EF4444 primary), 800x600, educational diagrams.
"""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/history"

# ─── Color Palette ───────────────────────────────────────────────────────────
PRIMARY      = "#EF4444"
PRIMARY_DARK = "#B91C1C"
PRIMARY_LIGHT = "#FCA5A5"
PRIMARY_PALE = "#FEE2E2"
ACCENT       = "#DC2626"
ACCENT_GOLD  = "#D4A017"
ACCENT_GOLD_LIGHT = "#F5DEB3"
BG_LIGHT     = "#FFF5F5"
BG_CREAM     = "#FFFBFB"
TEXT_DARK     = "#1F2937"
TEXT_MEDIUM   = "#374151"
TEXT_LIGHT    = "#6B7280"
WHITE        = "#FFFFFF"
SHADOW       = "#00000020"
BORDER_ROSE  = "#F9A8D4"

W, H = 800, 600

# ─── Helper Functions ─────────────────────────────────────────────────────────

def escape(text):
    """Escape XML special characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def make_svg():
    """Create base SVG element with proper namespaces."""
    svg = ET.Element("svg")
    svg.set("xmlns", "http://www.w3.org/2000/svg")
    svg.set("width", str(W))
    svg.set("height", str(H))
    svg.set("viewBox", f"0 0 {W} {H}")
    return svg

def add_def(svg, def_id, content_func):
    """Add a defs element."""
    defs = svg.find("{http://www.w3.org/2000/svg}defs")
    if defs is None:
        defs = ET.SubElement(svg, "defs")
    return content_func(defs, def_id)

def add_gradient(svg, gid, c1, c2, vertical=True):
    """Add a linear gradient to defs."""
    defs = svg.find("{http://www.w3.org/2000/svg}defs")
    if defs is None:
        defs = ET.SubElement(svg, "defs")
    grad = ET.SubElement(defs, "linearGradient")
    grad.set("id", gid)
    grad.set("x1", "0%")
    grad.set("y1", "0%")
    grad.set("x2", "0%" if vertical else "100%")
    grad.set("y2", "100%" if vertical else "0%")
    s1 = ET.SubElement(grad, "stop")
    s1.set("offset", "0%")
    s1.set("stop-color", c1)
    s2 = ET.SubElement(grad, "stop")
    s2.set("offset", "100%")
    s2.set("stop-color", c2)

def add_filter_shadow(svg, fid):
    """Add a drop shadow filter."""
    defs = svg.find("{http://www.w3.org/2000/svg}defs")
    if defs is None:
        defs = ET.SubElement(svg, "defs")
    f = ET.SubElement(defs, "filter")
    f.set("id", fid)
    f.set("x", "-5%")
    f.set("y", "-5%")
    f.set("width", "110%")
    f.set("height", "110%")
    feOffset = ET.SubElement(f, "feDropShadow")
    feOffset.set("dx", "2")
    feOffset.set("dy", "2")
    feOffset.set("stdDeviation", "3")
    feOffset.set("flood-color", "#00000030")

def rect(parent, x, y, w, h, fill, stroke=None, sw=1, rx=0, ry=0, opacity=None, filter_id=None):
    el = ET.SubElement(parent, "rect")
    el.set("x", str(x))
    el.set("y", str(y))
    el.set("width", str(w))
    el.set("height", str(h))
    el.set("fill", fill)
    if stroke: el.set("stroke", stroke)
    if sw != 1: el.set("stroke-width", str(sw))
    if rx: el.set("rx", str(rx))
    if ry: el.set("ry", str(ry))
    if opacity: el.set("opacity", str(opacity))
    if filter_id: el.set("filter", f"url(#{filter_id})")
    return el

def circle(parent, cx, cy, r, fill, stroke=None, sw=1, opacity=None):
    el = ET.SubElement(parent, "circle")
    el.set("cx", str(cx))
    el.set("cy", str(cy))
    el.set("r", str(r))
    el.set("fill", fill)
    if stroke: el.set("stroke", stroke)
    if sw != 1: el.set("stroke-width", str(sw))
    if opacity: el.set("opacity", str(opacity))
    return el

def ellipse(parent, cx, cy, rx, ry, fill, stroke=None, sw=1):
    el = ET.SubElement(parent, "ellipse")
    el.set("cx", str(cx))
    el.set("cy", str(cy))
    el.set("rx", str(rx))
    el.set("ry", str(ry))
    el.set("fill", fill)
    if stroke: el.set("stroke", stroke)
    if sw != 1: el.set("stroke-width", str(sw))
    return el

def line(parent, x1, y1, x2, y2, stroke, sw=2, dash=None):
    el = ET.SubElement(parent, "line")
    el.set("x1", str(x1))
    el.set("y1", str(y1))
    el.set("x2", str(x2))
    el.set("y2", str(y2))
    el.set("stroke", stroke)
    el.set("stroke-width", str(sw))
    if dash: el.set("stroke-dasharray", dash)
    return el

def polygon(parent, points, fill, stroke=None, sw=1):
    el = ET.SubElement(parent, "polygon")
    el.set("points", points)
    el.set("fill", fill)
    if stroke: el.set("stroke", stroke)
    if sw != 1: el.set("stroke-width", str(sw))
    return el

def text(parent, x, y, content, size=14, fill=TEXT_DARK, anchor="middle", weight="normal", font_family="sans-serif", style=None):
    el = ET.SubElement(parent, "text")
    el.set("x", str(x))
    el.set("y", str(y))
    el.set("font-size", str(size))
    el.set("fill", fill)
    el.set("text-anchor", anchor)
    el.set("font-family", font_family)
    if weight != "normal": el.set("font-weight", weight)
    if style: el.set("font-style", style)
    el.text = content
    return el

def tspan(parent, x, dy, content, size=14, fill=TEXT_DARK, anchor="middle", weight="normal"):
    el = ET.SubElement(parent, "tspan")
    el.set("x", str(x))
    el.set("dy", str(dy))
    el.set("font-size", str(size))
    el.set("fill", fill)
    el.set("text-anchor", anchor)
    if weight != "normal": el.set("font-weight", weight)
    el.text = content
    return el

def path(parent, d, fill="none", stroke=None, sw=2, opacity=None):
    el = ET.SubElement(parent, "path")
    el.set("d", d)
    el.set("fill", fill)
    if stroke: el.set("stroke", stroke)
    if sw != 2: el.set("stroke-width", str(sw))
    if opacity: el.set("opacity", str(opacity))
    return el

def draw_crown(parent, cx, cy, scale=1.0, color=ACCENT_GOLD):
    """Draw a simple crown icon."""
    s = scale
    pts = f"{cx-12*s},{cy+8*s} {cx-12*s},{cy-4*s} {cx-6*s},{cy+2*s} {cx},{cy-10*s} {cx+6*s},{cy+2*s} {cx+12*s},{cy-4*s} {cx+12*s},{cy+8*s}"
    polygon(parent, pts, color, stroke="#8B6914", sw=1)
    # Jewels
    circle(parent, cx, cy - 6*s, 2*s, "#EF4444")
    circle(parent, cx - 8*s, cy - 1*s, 1.5*s, "#3B82F6")
    circle(parent, cx + 8*s, cy - 1*s, 1.5*s, "#3B82F6")

def draw_sword(parent, cx, cy, scale=1.0, color="#9CA3AF"):
    """Draw a simplified sword icon."""
    s = scale
    # Blade
    line(parent, cx, cy - 20*s, cx, cy + 10*s, color, sw=3*s)
    # Crossguard
    line(parent, cx - 8*s, cy + 2*s, cx + 8*s, cy + 2*s, ACCENT_GOLD, sw=2.5*s)
    # Pommel
    circle(parent, cx, cy + 14*s, 3*s, ACCENT_GOLD)

def draw_banner(parent, cx, cy, scale=1.0, color=PRIMARY):
    """Draw a simplified banner/flag icon."""
    s = scale
    # Pole
    line(parent, cx - 8*s, cy - 16*s, cx - 8*s, cy + 14*s, TEXT_MEDIUM, sw=2.5*s)
    # Flag
    pts = f"{cx-8*s},{cy-16*s} {cx+14*s},{cy-10*s} {cx-8*s},{cy-2*s}"
    polygon(parent, pts, color, stroke=PRIMARY_DARK, sw=1)

def draw_star(parent, cx, cy, r, color=ACCENT_GOLD):
    """Draw a 5-pointed star."""
    import math
    pts = []
    for i in range(10):
        angle = math.pi / 2 + i * math.pi / 5
        radius = r if i % 2 == 0 else r * 0.4
        px = cx + radius * math.cos(angle)
        py = cy - radius * math.sin(angle)
        pts.append(f"{px:.1f},{py:.1f}")
    polygon(parent, " ".join(pts), color, stroke="#8B6914", sw=0.5)

def draw_shield(parent, cx, cy, scale=1.0, color=PRIMARY):
    """Draw a shield shape."""
    s = scale
    d = f"M {cx-14*s} {cy-16*s} L {cx+14*s} {cy-16*s} L {cx+14*s} {cy+4*s} L {cx} {cy+18*s} L {cx-14*s} {cy+4*s} Z"
    path(parent, d, color, stroke=PRIMARY_DARK, sw=1.5)

def draw_anchor(parent, cx, cy, scale=1.0, color=TEXT_MEDIUM):
    """Draw an anchor (for naval themes)."""
    s = scale
    # Shaft
    line(parent, cx, cy - 14*s, cx, cy + 12*s, color, sw=2.5*s)
    # Cross bar
    line(parent, cx - 10*s, cy - 6*s, cx + 10*s, cy - 6*s, color, sw=2.5*s)
    # Ring
    circle(parent, cx, cy - 17*s, 4*s, "none", stroke=color, sw=2*s)
    # Flukes
    d_fluke_l = f"M {cx-2*s} {cy+12*s} Q {cx-18*s} {cy+6*s} {cx-12*s} {cy-2*s}"
    path(parent, d_fluke_l, "none", stroke=color, sw=2.5*s)
    d_fluke_r = f"M {cx+2*s} {cy+12*s} Q {cx+18*s} {cy+6*s} {cx+12*s} {cy-2*s}"
    path(parent, d_fluke_r, "none", stroke=color, sw=2.5*s)

def add_background(svg, grad_id="bgGrad"):
    """Add standard background with gradient."""
    add_gradient(svg, grad_id, BG_CREAM, BG_LIGHT)
    rect(svg, 0, 0, W, H, f"url(#{grad_id})")

def add_header(svg, title, subtitle="", grad_id="headerGrad"):
    """Add standard header bar with title."""
    add_gradient(svg, grad_id, PRIMARY_DARK, PRIMARY)
    rect(svg, 0, 0, W, 70, f"url(#{grad_id})")
    # Bottom accent line
    rect(svg, 0, 70, W, 3, ACCENT_GOLD)
    # Title
    text(svg, W//2, 32, title, size=22, fill=WHITE, weight="bold")
    if subtitle:
        text(svg, W//2, 55, subtitle, size=13, fill="#FEE2E2", weight="normal")
    # Decorative crown
    draw_crown(svg, 35, 35, scale=1.1)

def add_footer(svg, lesson_num):
    """Add a standard footer."""
    rect(svg, 0, H - 30, W, 30, PRIMARY_DARK, opacity="0.15")
    text(svg, W//2, H - 10, f"Урок {lesson_num} | История России | 8 класс", size=10, fill=TEXT_LIGHT)

def add_info_box(svg, x, y, w, h, title, desc, color=PRIMARY, title_size=12, desc_size=10):
    """Add an info box with title and description."""
    # Background
    rect(svg, x, y, w, h, WHITE, stroke=color, sw=1.5, rx=6, ry=6)
    # Title bar
    rect(svg, x, y, w, 22, color, rx=6, ry=6)
    rect(svg, x, y + 14, w, 8, color)  # Fill the rounded corners at bottom of title bar
    text(svg, x + w//2, y + 15, title, size=title_size, fill=WHITE, weight="bold")
    # Description - handle multiline with tspan
    lines = desc.split("\n")
    for i, line in enumerate(lines):
        text(svg, x + w//2, y + 36 + i * 14, line, size=desc_size, fill=TEXT_MEDIUM)

def add_timeline_event(svg, x, y, date, event, color=PRIMARY, line_y=None):
    """Add a timeline event marker with date and description."""
    # Dot on timeline
    circle(svg, x, line_y if line_y else y, 6, color, stroke=WHITE, sw=2)
    # Date
    text(svg, x, y - 14 if line_y else y - 16, date, size=10, fill=color, weight="bold")
    # Event description
    text(svg, x, y + 20 if line_y else y + 14, event, size=9, fill=TEXT_DARK)

def draw_map_russia_simplified(svg, cx, cy, scale=1.0, highlight_regions=None):
    """Draw a very simplified Russia outline (European part) for map diagrams."""
    s = scale
    # Simplified outline of European Russia
    d = (
        f"M {cx-60*s} {cy-30*s} "
        f"L {cx-30*s} {cy-40*s} "
        f"L {cx} {cy-35*s} "
        f"L {cx+40*s} {cy-25*s} "
        f"L {cx+50*s} {cy-10*s} "
        f"L {cx+45*s} {cy+5*s} "
        f"L {cx+35*s} {cy+15*s} "
        f"L {cx+20*s} {cy+25*s} "
        f"L {cx} {cy+30*s} "
        f"L {cx-25*s} {cy+25*s} "
        f"L {cx-45*s} {cy+15*s} "
        f"L {cx-55*s} {cy} "
        f"L {cx-60*s} {cy-15*s} "
        f"Z"
    )
    path(svg, d, PRIMARY_PALE, stroke=PRIMARY, sw=2*s)
    # Label
    text(svg, cx, cy + 5, "Россия", size=11*s, fill=PRIMARY_DARK, weight="bold")


# ═══════════════════════════════════════════════════════════════════════════════
# LESSON 1: Начало правления Петра I
# ═══════════════════════════════════════════════════════════════════════════════

def lesson_1():
    svg = make_svg()
    add_gradient(svg, "bg1", BG_CREAM, "#FFF0F0")
    add_filter_shadow(svg, "shadow1")
    add_background(svg, "bg1")
    add_header(svg, "Начало правления Петра I", "Реформы, Великое посольство, модернизация России")

    # ─── Timeline Section ─────────────────────────────────────────────────
    ty = 100
    rect(svg, 20, ty, W-40, 55, WHITE, stroke=PRIMARY_LIGHT, sw=1, rx=8, ry=8)
    line(svg, 40, ty + 28, W-40, ty + 28, PRIMARY, sw=3)

    timeline_events = [
        (100, "1682", "Начало\nправления"),
        (230, "1689", "Единоличная\nвласть"),
        (360, "1695-96", "Азовские\nпоходы"),
        (490, "1697-98", "Великое\nпосольство"),
        (620, "1700", "Северная\nвойна"),
        (730, "1703", "Основание\nСПб"),
    ]
    for (x, date, ev) in timeline_events:
        add_timeline_event(svg, x, ty + 10, date, "", color=PRIMARY, line_y=ty + 28)
        lines = ev.split("\n")
        for i, l in enumerate(lines):
            text(svg, x, ty + 45 + i * 10, l, size=8, fill=TEXT_DARK)

    # ─── Left Column: Key Reforms ─────────────────────────────────────────
    col_x = 30
    col_y = 170

    text(svg, col_x + 120, col_y, "Ключевые реформы Петра I", size=14, fill=PRIMARY_DARK, weight="bold")
    draw_crown(svg, col_x + 15, col_y - 4, scale=0.8, color=ACCENT_GOLD)

    reforms = [
        ("Военная реформа", "Создание регулярной армии,\nрекрутские наборы, флот"),
        ("Губернская реформа", "Разделение России на 8\nгуберний (1708 г.)"),
        ("Церковная реформа", "Упразднение патриаршества,\nСвятейший Синод (1721 г.)"),
        ("Реформа быта", "Бритьё бород, европейская\nодежда, ассамблеи"),
        ("Реформа письма", "Введение гражданского\nшрифта (1708 г.)"),
    ]

    for i, (title, desc) in enumerate(reforms):
        by = col_y + 18 + i * 68
        rect(svg, col_x, by, 235, 62, WHITE, stroke=PRIMARY_LIGHT, sw=1, rx=6, ry=6, filter_id="shadow1")
        rect(svg, col_x, by, 5, 62, PRIMARY, rx=2, ry=2)
        text(svg, col_x + 14, by + 16, title, size=11, fill=PRIMARY_DARK, weight="bold")
        lines = desc.split("\n")
        for j, l in enumerate(lines):
            text(svg, col_x + 14, by + 32 + j * 13, l, size=9, fill=TEXT_MEDIUM, anchor="start")

    # ─── Right Column: Grand Embassy & Modernization ──────────────────────
    rx_start = 290

    text(svg, rx_start + 120, col_y, "Великое посольство (1697-1698)", size=14, fill=PRIMARY_DARK, weight="bold")
    draw_banner(svg, rx_start + 10, col_y - 5, scale=0.8, color=PRIMARY)

    # Grand Embassy info box
    add_info_box(svg, rx_start, col_y + 18, 245, 100,
                 "Цели посольства",
                 "1. Найти союзников против Турции\n2. Изучить европейский опыт\n3. Нанять специалистов\n4. Закупить оружие",
                 color=ACCENT)

    # Countries visited
    add_info_box(svg, rx_start, col_y + 130, 245, 75,
                 "Страны посещения",
                 "Голландия, Англия, Австрия,\nСаксония, Пруссия, Курляндия",
                 color="#7C3AED")

    # Modernization diagram
    mod_y = col_y + 220
    text(svg, rx_start + 120, mod_y, "Модернизация России", size=13, fill=PRIMARY_DARK, weight="bold")

    # Arrow diagram showing transformation
    arrow_y = mod_y + 20
    # From old Russia to new Russia
    rect(svg, rx_start, arrow_y, 90, 50, PRIMARY_PALE, stroke=PRIMARY, sw=1, rx=6, ry=6)
    text(svg, rx_start + 45, arrow_y + 20, "Россия", size=11, fill=PRIMARY_DARK, weight="bold")
    text(svg, rx_start + 45, arrow_y + 36, "допетровская", size=9, fill=TEXT_MEDIUM)

    # Arrow
    line(svg, rx_start + 95, arrow_y + 25, rx_start + 145, arrow_y + 25, PRIMARY, sw=3)
    polygon(svg, f"{rx_start+145},{arrow_y+18} {rx_start+155},{arrow_y+25} {rx_start+145},{arrow_y+32}", PRIMARY)

    rect(svg, rx_start + 160, arrow_y, 85, 50, PRIMARY, stroke=PRIMARY_DARK, sw=1, rx=6, ry=6)
    text(svg, rx_start + 202, arrow_y + 20, "Россия", size=11, fill=WHITE, weight="bold")
    text(svg, rx_start + 202, arrow_y + 36, "империя", size=9, fill="#FEE2E2")

    # Key dates summary
    dates_y = mod_y + 90
    rect(svg, rx_start, dates_y, 245, 60, WHITE, stroke=ACCENT_GOLD, sw=1.5, rx=6, ry=6)
    draw_star(svg, rx_start + 14, dates_y + 12, 8, ACCENT_GOLD)
    text(svg, rx_start + 26, dates_y + 15, "1721 г. — Россия провозглашена Империей", size=10, fill=PRIMARY_DARK, weight="bold", anchor="start")
    text(svg, rx_start + 14, dates_y + 32, "Пётр I принял титул Императора", size=9, fill=TEXT_MEDIUM, anchor="start")
    text(svg, rx_start + 14, dates_y + 46, "и Отца Отечества", size=9, fill=TEXT_MEDIUM, anchor="start")

    # ─── Far Right: Decorative elements & map ─────────────────────────────
    far_x = 555

    # Map of European Russia with route
    rect(svg, far_x, col_y + 18, 225, 130, WHITE, stroke=PRIMARY_LIGHT, sw=1, rx=6, ry=6)
    text(svg, far_x + 112, col_y + 34, "Маршрут Великого посольства", size=9, fill=TEXT_LIGHT)
    draw_map_russia_simplified(svg, far_x + 90, col_y + 85, scale=0.9)

    # Route dots
    circle(svg, far_x + 70, col_y + 72, 3, "#3B82F6")
    text(svg, far_x + 60, col_y + 65, "Москва", size=7, fill="#3B82F6", anchor="end")

    circle(svg, far_x + 140, col_y + 55, 3, "#10B981")
    text(svg, far_x + 152, col_y + 52, "Голландия", size=7, fill="#10B981", anchor="start")

    # Dashed route line
    line(svg, far_x + 73, col_y + 72, far_x + 137, col_y + 57, "#3B82F6", sw=1.5, dash="4,3")

    # Decorative sword
    draw_sword(svg, far_x + 195, col_y + 85, scale=1.0, color="#9CA3AF")

    # Key figures box
    add_info_box(svg, far_x, col_y + 160, 225, 80,
                 "Сподвижники Петра I",
                 "А.Меньшиков, Ф.Апраксин,\nБ.Шереметев, Ф.Лефорт,\nП.Гордон, Я.Брюс",
                 color="#059669")

    # Quote box
    rect(svg, far_x, col_y + 255, 225, 55, PRIMARY_PALE, stroke=PRIMARY_LIGHT, sw=1, rx=6, ry=6)
    text(svg, far_x + 112, col_y + 275, "«За всё браться — всё сделать»,", size=10, fill=PRIMARY_DARK, style="italic", weight="bold")
    text(svg, far_x + 112, col_y + 295, "— девиз Петра I", size=9, fill=TEXT_LIGHT)

    add_footer(svg, 1)
    return svg


# ═══════════════════════════════════════════════════════════════════════════════
# LESSON 2: Северная война
# ═══════════════════════════════════════════════════════════════════════════════

def lesson_2():
    svg = make_svg()
    add_gradient(svg, "bg2", BG_CREAM, "#FFF0F0")
    add_filter_shadow(svg, "shadow2")
    add_background(svg, "bg2")
    add_header(svg, "Северная война (1700-1721)", "Нарва, Полтава, Ништадтский мир, выход к Балтике")

    # ─── Timeline ─────────────────────────────────────────────────────────
    ty = 95
    rect(svg, 20, ty, W-40, 52, WHITE, stroke=PRIMARY_LIGHT, sw=1, rx=8, ry=8)
    line(svg, 40, ty + 26, W-40, ty + 26, PRIMARY, sw=3)

    events = [
        (80, "1700", "Нарва"),
        (195, "1703", "Основ.\nСПб"),
        (310, "1708", "Лесная"),
        (420, "1709", "Полтава"),
        (530, "1714", "Гангут"),
        (645, "1720", "Гренгам"),
        (745, "1721", "Ништадт"),
    ]
    for (x, date, ev) in events:
        add_timeline_event(svg, x, ty + 8, date, "", color=PRIMARY, line_y=ty + 26)
        lines = ev.split("\n")
        for i, l in enumerate(lines):
            text(svg, x, ty + 43 + i * 10, l, size=8, fill=TEXT_DARK)

    # ─── Battle of Narva ──────────────────────────────────────────────────
    bx, by = 25, 160
    rect(svg, bx, by, 245, 140, WHITE, stroke="#DC2626", sw=2, rx=8, ry=8, filter_id="shadow2")
    rect(svg, bx, by, 245, 24, "#DC2626", rx=8, ry=8)
    rect(svg, bx, by + 14, 245, 10, "#DC2626")
    text(svg, bx + 122, by + 17, "Битва при Нарве (1700)", size=12, fill=WHITE, weight="bold")

    text(svg, bx + 122, by + 42, "Поражение русской армии", size=10, fill="#DC2626", weight="bold")
    text(svg, bx + 10, by + 58, "Шведы: ~10 000 чел.  Карл XII", size=9, fill=TEXT_DARK, anchor="start")
    text(svg, bx + 10, by + 72, "Русские: ~35 000 чел.", size=9, fill=TEXT_DARK, anchor="start")
    text(svg, bx + 10, by + 86, "Причины поражения:", size=9, fill=TEXT_MEDIUM, anchor="start", weight="bold")
    text(svg, bx + 10, by + 100, "- Неопытность офицерского состава", size=9, fill=TEXT_MEDIUM, anchor="start")
    text(svg, bx + 10, by + 113, "- Слабая дисциплина", size=9, fill=TEXT_MEDIUM, anchor="start")
    text(svg, bx + 10, by + 126, "- Плохое снабжение", size=9, fill=TEXT_MEDIUM, anchor="start")

    # Sword crossed
    draw_sword(svg, bx + 220, by + 105, scale=0.8, color="#9CA3AF")

    # ─── Battle of Poltava ────────────────────────────────────────────────
    px, py = 285, 160
    rect(svg, px, py, 245, 140, WHITE, stroke="#059669", sw=2, rx=8, ry=8, filter_id="shadow2")
    rect(svg, px, py, 245, 24, "#059669", rx=8, ry=8)
    rect(svg, px, py + 14, 245, 10, "#059669")
    draw_star(svg, px + 15, py + 12, 8, ACCENT_GOLD)
    text(svg, px + 130, py + 17, "Полтавская битва (1709)", size=12, fill=WHITE, weight="bold")

    text(svg, px + 122, py + 42, "Решающая победа России!", size=10, fill="#059669", weight="bold")
    text(svg, px + 10, py + 58, "Русские: ~42 000 чел.  Пётр I", size=9, fill=TEXT_DARK, anchor="start")
    text(svg, px + 10, py + 72, "Шведы: ~30 000 чел.  Карл XII", size=9, fill=TEXT_DARK, anchor="start")
    text(svg, px + 10, py + 86, "Потери шведов: ~9 000 убитых", size=9, fill=TEXT_MEDIUM, anchor="start")
    text(svg, px + 10, py + 100, "Потери русских: ~1 345 убитых", size=9, fill=TEXT_MEDIUM, anchor="start")
    text(svg, px + 10, py + 118, "27 июня 1709 г. — перелом в войне", size=9, fill=PRIMARY_DARK, anchor="start", weight="bold")

    # Shield
    draw_shield(svg, px + 220, py + 105, scale=0.9, color="#059669")

    # ─── Treaty of Nystad ─────────────────────────────────────────────────
    nx, ny = 545, 160
    rect(svg, nx, ny, 235, 140, WHITE, stroke=ACCENT_GOLD, sw=2, rx=8, ry=8, filter_id="shadow2")
    rect(svg, nx, ny, 235, 24, ACCENT_GOLD, rx=8, ry=8)
    rect(svg, nx, ny + 14, 235, 10, ACCENT_GOLD)
    text(svg, nx + 117, ny + 17, "Ништадтский мир (1721)", size=12, fill=WHITE, weight="bold")

    text(svg, nx + 117, ny + 42, "Итоги войны:", size=10, fill=ACCENT_GOLD, weight="bold")
    text(svg, nx + 10, ny + 58, "Россия получила:", size=9, fill=TEXT_DARK, anchor="start", weight="bold")
    text(svg, nx + 10, ny + 72, "- Лифляндию, Эстляндию", size=9, fill=TEXT_MEDIUM, anchor="start")
    text(svg, nx + 10, ny + 86, "- Ингрию, часть Карелии", size=9, fill=TEXT_MEDIUM, anchor="start")
    text(svg, nx + 10, ny + 100, "- Выход к Балтийскому морю", size=9, fill=PRIMARY_DARK, anchor="start", weight="bold")
    text(svg, nx + 10, ny + 118, "Россия стала великой державой!", size=9, fill=PRIMARY, anchor="start", weight="bold")

    # Crown
    draw_crown(svg, nx + 200, ny + 105, scale=1.0, color=ACCENT_GOLD)

    # ─── Baltic Sea Map ───────────────────────────────────────────────────
    map_x, map_y = 25, 315
    rect(svg, map_x, map_y, 350, 230, WHITE, stroke=PRIMARY_LIGHT, sw=1, rx=8, ry=8, filter_id="shadow2")
    text(svg, map_x + 175, map_y + 18, "Выход к Балтийскому морю", size=12, fill=PRIMARY_DARK, weight="bold")

    # Simplified Baltic Sea
    ellipse(svg, map_x + 175, map_y + 125, 130, 70, "#BFDBFE", stroke="#3B82F6", sw=2)
    text(svg, map_x + 175, map_y + 128, "Балтийское\nморе", size=11, fill="#1E40AF", weight="bold")

    # Territories gained (arrows pointing to the sea)
    # South coast - new territories
    rect(svg, map_x + 50, map_y + 170, 80, 30, "#D1FAE5", stroke="#059669", sw=1, rx=4, ry=4)
    text(svg, map_x + 90, map_y + 188, "Лифляндия", size=8, fill="#065F46")

    rect(svg, map_x + 140, map_y + 175, 65, 28, "#D1FAE5", stroke="#059669", sw=1, rx=4, ry=4)
    text(svg, map_x + 172, map_y + 192, "Эстляндия", size=8, fill="#065F46")

    rect(svg, map_x + 215, map_y + 170, 50, 30, "#FEE2E2", stroke=PRIMARY, sw=1, rx=4, ry=4)
    text(svg, map_x + 240, map_y + 188, "Ингрия", size=8, fill=PRIMARY_DARK)

    # St. Petersburg marker
    circle(svg, map_x + 225, map_y + 120, 5, "#DC2626", stroke=WHITE, sw=2)
    text(svg, map_x + 225, map_y + 110, "СПб", size=9, fill="#DC2626", weight="bold")

    # Russia label
    rect(svg, map_x + 250, map_y + 195, 80, 28, PRIMARY_PALE, stroke=PRIMARY, sw=1, rx=4, ry=4)
    text(svg, map_x + 290, map_y + 213, "Россия", size=10, fill=PRIMARY_DARK, weight="bold")

    # Arrow showing access
    line(svg, map_x + 250, map_y + 165, map_x + 200, map_y + 140, "#059669", sw=2, dash="5,3")
    polygon(svg, f"{map_x+195},{map_y+132} {map_x+205},{map_y+137} {map_x+198},{map_y+142}", "#059669")

    draw_anchor(svg, map_x + 320, map_y + 55, scale=0.9, color="#3B82F6")

    # ─── War Phases Diagram ───────────────────────────────────────────────
    ph_x, ph_y = 395, 315
    rect(svg, ph_x, ph_y, 385, 230, WHITE, stroke=PRIMARY_LIGHT, sw=1, rx=8, ry=8, filter_id="shadow2")
    text(svg, ph_x + 192, ph_y + 18, "Этапы Северной войны", size=12, fill=PRIMARY_DARK, weight="bold")

    phases = [
        ("I этап (1700-1706)", "Неудачи и реорганизация армии", "#DC2626", ph_y + 35),
        ("II этап (1707-1709)", "Перелом: Полтавская победа", "#F59E0B", ph_y + 95),
        ("III этап (1710-1721)", "Победы на море и мир", "#059669", ph_y + 155),
    ]

    for (title, desc, color, fy) in phases:
        rect(svg, ph_x + 10, fy, 365, 52, WHITE, stroke=color, sw=1.5, rx=6, ry=6)
        rect(svg, ph_x + 10, fy, 8, 52, color, rx=4, ry=4)
        text(svg, ph_x + 24, fy + 18, title, size=11, fill=color, weight="bold", anchor="start")
        text(svg, ph_x + 24, fy + 36, desc, size=10, fill=TEXT_MEDIUM, anchor="start")
        # Progress arrow
        if fy < ph_y + 150:
            line(svg, ph_x + 192, fy + 54, ph_x + 192, fy + 72, color, sw=2)
            polygon(svg, f"{ph_x+187},{fy+69} {ph_x+192},{fy+78} {ph_x+197},{fy+69}", color)

    # Naval battles info
    text(svg, ph_x + 192, ph_y + 212, "Морские победы: Гангут (1714), Гренгам (1720)", size=9, fill="#1E40AF", weight="bold")

    add_footer(svg, 2)
    return svg


# ═══════════════════════════════════════════════════════════════════════════════
# LESSON 3: Дворцовые перевороты
# ═══════════════════════════════════════════════════════════════════════════════

def lesson_3():
    svg = make_svg()
    add_gradient(svg, "bg3", BG_CREAM, "#FFF0F0")
    add_filter_shadow(svg, "shadow3")
    add_background(svg, "bg3")
    add_header(svg, "Дворцовые перевороты (1725-1762)", "Эпоха нестабильности, Елизавета, Анна, Екатерина I, Пётр III")

    # ─── Timeline of Coups ────────────────────────────────────────────────
    ty = 90
    rect(svg, 20, ty, W-40, 70, WHITE, stroke=PRIMARY_LIGHT, sw=1, rx=8, ry=8)
    text(svg, W//2, ty + 14, "Хронология дворцовых переворотов", size=11, fill=PRIMARY_DARK, weight="bold")
    line(svg, 40, ty + 40, W-40, ty + 40, PRIMARY, sw=3)

    coups = [
        (80, "1725", "Екатери-\nна I"),
        (190, "1727", "Пётр II"),
        (300, "1730", "Анна\nИоанновна"),
        (415, "1740", "Иван VI\n(Браунш.)"),
        (530, "1741", "Елиза-\nвета"),
        (645, "1761", "Пётр III"),
        (740, "1762", "Екате-\nрина II"),
    ]
    for (x, date, name) in coups:
        circle(svg, x, ty + 40, 5, PRIMARY, stroke=WHITE, sw=2)
        text(svg, x, ty + 55, date, size=8, fill=PRIMARY, weight="bold")
        lines = name.split("\n")
        for i, l in enumerate(lines):
            text(svg, x, ty + 66 + i * 9, l, size=7, fill=TEXT_DARK)

    # ─── Ruler Cards ──────────────────────────────────────────────────────
    rulers = [
        ("Екатерина I", "1725-1727", "Вдова Петра I.\nПравление через\nМеньшикова.\nСоздан Верховный\nтайный совет.", "#8B5CF6"),
        ("Пётр II", "1727-1730", "Внук Петра I.\nВлияние Долгоруких.\nПеренёс двор\nв Москву.\nУмер в 14 лет.", "#6366F1"),
        ("Анна Иоанновна", "1730-1740", "Племянница Петра I.\nБироновщина.\nКабинет министров.\nРасходы на двор.\nТайная канцелярия.", "#EC4899"),
        ("Елизавета Петровна", "1741-1761", "Дочь Петра I.\nВернула традиции\nотца. Ломоносов.\nМГУ (1755).\nСемилетняя война.", "#059669"),
        ("Пётр III", "1761-1762", "Внук Петра I.\nМанифест о вольности\nдворянства (1762).\nВыход из войны.\nСвергнут женой.", "#DC2626"),
    ]

    card_w = 144
    card_h = 195
    start_x = 20
    card_y = 175

    for i, (name, years, desc, color) in enumerate(rulers):
        cx = start_x + i * (card_w + 6)
        rect(svg, cx, card_y, card_w, card_h, WHITE, stroke=color, sw=2, rx=8, ry=8, filter_id="shadow3")
        # Title bar
        rect(svg, cx, card_y, card_w, 35, color, rx=8, ry=8)
        rect(svg, cx, card_y + 25, card_w, 10, color)
        text(svg, cx + card_w//2, card_y + 15, name, size=10, fill=WHITE, weight="bold")
        text(svg, cx + card_w//2, card_y + 30, years, size=9, fill="#FFFFFFCC")
        # Crown icon
        draw_crown(svg, cx + 18, card_y + 10, scale=0.6, color=ACCENT_GOLD)
        # Description
        lines = desc.split("\n")
        for j, l in enumerate(lines):
            text(svg, cx + card_w//2, card_y + 50 + j * 14, l, size=9, fill=TEXT_MEDIUM)

    # ─── Bottom: Key Concepts ─────────────────────────────────────────────
    bot_y = 385

    # "Указ о престолонаследии" box
    rect(svg, 20, bot_y, 250, 95, WHITE, stroke=PRIMARY, sw=1.5, rx=8, ry=8)
    rect(svg, 20, bot_y, 250, 24, PRIMARY, rx=8, ry=8)
    rect(svg, 20, bot_y + 14, 250, 10, PRIMARY)
    text(svg, 145, bot_y + 17, "Указ о престолонаследии (1722)", size=10, fill=WHITE, weight="bold")
    text(svg, 30, bot_y + 42, "Пётр I отменил обычный порядок", size=9, fill=TEXT_DARK, anchor="start")
    text(svg, 30, bot_y + 56, "наследования. Монарх сам назначает", size=9, fill=TEXT_DARK, anchor="start")
    text(svg, 30, bot_y + 70, "преемника. Это привело к эпохе", size=9, fill=TEXT_DARK, anchor="start")
    text(svg, 30, bot_y + 84, "дворцовых переворотов.", size=9, fill=PRIMARY_DARK, anchor="start", weight="bold")

    # "Гвардия — главная сила" box
    rect(svg, 285, bot_y, 250, 95, WHITE, stroke="#8B5CF6", sw=1.5, rx=8, ry=8)
    rect(svg, 285, bot_y, 250, 24, "#8B5CF6", rx=8, ry=8)
    rect(svg, 285, bot_y + 14, 250, 10, "#8B5CF6")
    draw_sword(svg, 305, bot_y + 10, scale=0.6, color="#C4B5FD")
    text(svg, 420, bot_y + 17, "Гвардия — главная сила", size=10, fill=WHITE, weight="bold")
    text(svg, 295, bot_y + 42, "Преображенский и Семёновский", size=9, fill=TEXT_DARK, anchor="start")
    text(svg, 295, bot_y + 56, "полки решали исход переворотов.", size=9, fill=TEXT_DARK, anchor="start")
    text(svg, 295, bot_y + 70, "Гвардейцы возводили и свергали", size=9, fill=TEXT_DARK, anchor="start")
    text(svg, 295, bot_y + 84, "императоров по своей воле.", size=9, fill="#7C3AED", anchor="start", weight="bold")

    # "Манифест о вольности дворянства" box
    rect(svg, 550, bot_y, 235, 95, WHITE, stroke="#059669", sw=1.5, rx=8, ry=8)
    rect(svg, 550, bot_y, 235, 24, "#059669", rx=8, ry=8)
    rect(svg, 550, bot_y + 14, 235, 10, "#059669")
    text(svg, 667, bot_y + 17, "Манифест 1762 г.", size=10, fill=WHITE, weight="bold")
    text(svg, 560, bot_y + 42, "Освобождение дворян от", size=9, fill=TEXT_DARK, anchor="start")
    text(svg, 560, bot_y + 56, "обязательной службы. Пётр III", size=9, fill=TEXT_DARK, anchor="start")
    text(svg, 560, bot_y + 70, "подписал манифест. Дворяне", size=9, fill=TEXT_DARK, anchor="start")
    text(svg, 560, bot_y + 84, "могли не служить государству.", size=9, fill="#065F46", anchor="start", weight="bold")

    # ─── Summary banner ───────────────────────────────────────────────────
    rect(svg, 20, 495, W-40, 40, PRIMARY_PALE, stroke=PRIMARY_LIGHT, sw=1, rx=8, ry=8)
    text(svg, W//2, 512, "Эпоха дворцовых переворотов: 37 лет, 6 правителей, постоянная борьба за власть", size=11, fill=PRIMARY_DARK, weight="bold")
    text(svg, W//2, 527, "«Дворцы да шептунов довольно, а войска мало» — современники об эпохе", size=9, fill=TEXT_LIGHT, style="italic")

    add_footer(svg, 3)
    return svg


# ═══════════════════════════════════════════════════════════════════════════════
# LESSON 4: Екатерина II — просвещённый абсолютизм
# ═══════════════════════════════════════════════════════════════════════════════

def lesson_4():
    svg = make_svg()
    add_gradient(svg, "bg4", BG_CREAM, "#FFF0F0")
    add_filter_shadow(svg, "shadow4")
    add_background(svg, "bg4")
    add_header(svg, "Екатерина II — просвещённый абсолютизм", "Реформы, Пугачёв, территориальное расширение (1762-1796)")

    # ─── Timeline ─────────────────────────────────────────────────────────
    ty = 90
    rect(svg, 20, ty, W-40, 52, WHITE, stroke=PRIMARY_LIGHT, sw=1, rx=8, ry=8)
    line(svg, 40, ty + 26, W-40, ty + 26, PRIMARY, sw=3)

    events = [
        (80, "1762", "Восст.\nна трон"),
        (180, "1767", "Уложен.\nкомиссия"),
        (290, "1773-75", "Пугачёв"),
        (400, "1783", "Крым"),
        (500, "1785", "Жалов.\nграмоты"),
        (610, "1787-91", "Русско-\nтурецкая"),
        (720, "1793-95", "Разделы\nПольши"),
    ]
    for (x, date, ev) in events:
        add_timeline_event(svg, x, ty + 8, date, "", color=PRIMARY, line_y=ty + 26)
        lines = ev.split("\n")
        for i, l in enumerate(lines):
            text(svg, x, ty + 43 + i * 10, l, size=8, fill=TEXT_DARK)

    # ─── Left: Enlightened Absolutism ─────────────────────────────────────
    lx, ly = 25, 155
    rect(svg, lx, ly, 265, 155, WHITE, stroke="#7C3AED", sw=1.5, rx=8, ry=8, filter_id="shadow4")
    rect(svg, lx, ly, 265, 24, "#7C3AED", rx=8, ry=8)
    rect(svg, lx, ly + 14, 265, 10, "#7C3AED")
    text(svg, lx + 132, ly + 17, "Просвещённый абсолютизм", size=11, fill=WHITE, weight="bold")

    points = [
        "Следование идеям Просвещения",
        "Переписка с Вольтером, Дидро",
        "Уложенная комиссия (1767)",
        "Наказ Екатерины II",
        "Жалованные грамоты (1785):",
        "  - Дворянству (свободы, привилегии)",
        "  - Городам (самоуправление)",
    ]
    for i, p in enumerate(points):
        bullet = "•" if not p.startswith(" ") else "  -"
        text(svg, lx + 12, ly + 40 + i * 15, p, size=9, fill=TEXT_DARK, anchor="start")

    draw_crown(svg, lx + 245, ly + 12, scale=0.7, color=ACCENT_GOLD)

    # ─── Center: Pugachev Rebellion ───────────────────────────────────────
    cx, cy = 305, 155
    rect(svg, cx, cy, 250, 155, WHITE, stroke=PRIMARY, sw=2, rx=8, ry=8, filter_id="shadow4")
    rect(svg, cx, cy, 250, 24, PRIMARY, rx=8, ry=8)
    rect(svg, cx, cy + 14, 250, 10, PRIMARY)
    draw_banner(svg, cx + 16, cy + 10, scale=0.7, color=WHITE)
    text(svg, cx + 135, cy + 17, "Восстание Пугачёва (1773-75)", size=11, fill=WHITE, weight="bold")

    text(svg, cx + 125, cy + 40, "Емельян Пугачёв", size=10, fill=PRIMARY_DARK, weight="bold")
    text(svg, cx + 125, cy + 56, "Выдавал себя за Петра III", size=9, fill=TEXT_MEDIUM)

    # Phases
    phases_data = [
        ("1773-74", "Осада Оренбурга", "#F59E0B"),
        ("1774", "Поход на Москву", "#DC2626"),
        ("1774-75", "Подавление, казнь", "#6B7280"),
    ]
    for i, (year, desc, col) in enumerate(phases_data):
        py2 = cy + 68 + i * 24
        circle(svg, cx + 20, py2, 4, col)
        text(svg, cx + 30, py2 + 4, f"{year} — {desc}", size=9, fill=TEXT_DARK, anchor="start")

    text(svg, cx + 125, cy + 142, "Крупнейшее восстание в истории России", size=8, fill=PRIMARY, weight="bold")

    # ─── Right: Territorial Expansion ─────────────────────────────────────
    rx2, ry2 = 570, 155
    rect(svg, rx2, ry2, 215, 155, WHITE, stroke="#059669", sw=1.5, rx=8, ry=8, filter_id="shadow4")
    rect(svg, rx2, ry2, 215, 24, "#059669", rx=8, ry=8)
    rect(svg, rx2, ry2 + 14, 215, 10, "#059669")
    text(svg, rx2 + 107, ry2 + 17, "Территориальное расширение", size=11, fill=WHITE, weight="bold")

    territories = [
        ("1783 г.", "Присоединение Крыма", "#059669"),
        ("1774 г.", "Кючук-Кайнарджийский мир", "#059669"),
        ("1783 г.", "Георгиевский трактат", "#7C3AED"),
        ("1793 г.", "2-й раздел Польши", "#DC2626"),
        ("1795 г.", "3-й раздел Польши", "#DC2626"),
        ("1791 г.", "Ясский мир", "#059669"),
    ]
    for i, (year, desc, col) in enumerate(territories):
        ty2 = ry2 + 38 + i * 18
        text(svg, rx2 + 10, ty2, year, size=8, fill=col, weight="bold", anchor="start")
        text(svg, rx2 + 60, ty2, desc, size=8, fill=TEXT_DARK, anchor="start")

    # ─── Bottom: Map of Expansion ─────────────────────────────────────────
    map_y = 325
    rect(svg, 25, map_y, 370, 200, WHITE, stroke=PRIMARY_LIGHT, sw=1, rx=8, ry=8, filter_id="shadow4")
    text(svg, 210, map_y + 18, "Расширение территории при Екатерине II", size=11, fill=PRIMARY_DARK, weight="bold")

    # Simplified map: Russia outline
    d_russia = (
        f"M 60 {map_y+40} L 100 {map_y+35} L 160 {map_y+38} "
        f"L 220 {map_y+32} L 280 {map_y+45} L 320 {map_y+55} "
        f"L 350 {map_y+70} L 360 {map_y+90} L 350 {map_y+110} "
        f"L 330 {map_y+125} L 300 {map_y+140} L 260 {map_y+155} "
        f"L 200 {map_y+165} L 140 {map_y+160} L 80 {map_y+150} "
        f"L 50 {map_y+130} L 40 {map_y+100} L 45 {map_y+65} Z"
    )
    path(svg, d_russia, PRIMARY_PALE, stroke=PRIMARY, sw=1.5)

    # Crimea
    ellipse(svg, 100, map_y + 160, 25, 15, "#D1FAE5", stroke="#059669", sw=1.5)
    text(svg, 100, map_y + 162, "Крым", size=7, fill="#065F46", weight="bold")

    # Poland
    rect(svg, 220, map_y + 70, 40, 35, "#FEE2E2", stroke="#DC2626", sw=1, rx=3, ry=3)
    text(svg, 240, map_y + 90, "Польша", size=7, fill="#DC2626")

    # Black Sea
    ellipse(svg, 110, map_y + 175, 50, 15, "#BFDBFE", stroke="#3B82F6", sw=1)
    text(svg, 110, map_y + 178, "Чёрное м.", size=7, fill="#1E40AF")

    # Labels
    text(svg, 200, map_y + 55, "Россия", size=12, fill=PRIMARY_DARK, weight="bold")

    # ─── Bottom Right: Key Achievements ───────────────────────────────────
    ach_x, ach_y = 410, 325
    rect(svg, ach_x, ach_y, 375, 200, WHITE, stroke=PRIMARY_LIGHT, sw=1, rx=8, ry=8, filter_id="shadow4")
    text(svg, ach_x + 187, ach_y + 18, "Достижения эпохи Екатерины II", size=11, fill=PRIMARY_DARK, weight="bold")

    achievements = [
        ("Образование", "Московский университет,\nСмольный институт (1764)", "#7C3AED"),
        ("Медицина", "Медицинская коллегия,\nбольницы, оспопрививание", "#059669"),
        ("Экономика", "Рост мануфактур,\nсвободная торговля (1775)", "#F59E0B"),
        ("Культура", "Эрмитаж, Академия наук,\nлитература и искусство", "#DC2626"),
        ("Внешняя политика", "Выход к Чёрному морю,\nстрана стала империей №1", "#1E40AF"),
    ]

    for i, (cat, desc, col) in enumerate(achievements):
        ay = ach_y + 32 + i * 33
        rect(svg, ach_x + 10, ay, 8, 26, col, rx=4, ry=4)
        text(svg, ach_x + 25, ay + 10, cat, size=10, fill=col, weight="bold", anchor="start")
        lines = desc.split("\n")
        for j, l in enumerate(lines):
            text(svg, ach_x + 25, ay + 22 + j * 11, l, size=8, fill=TEXT_MEDIUM, anchor="start")

    # ─── Quote ────────────────────────────────────────────────────────────
    rect(svg, 25, 535, W-50, 28, PRIMARY_PALE, stroke=PRIMARY_LIGHT, sw=1, rx=6, ry=6)
    text(svg, W//2, 553, "«Я хочу повелевать людьми и делать их счастливыми» — Екатерина II", size=10, fill=PRIMARY_DARK, style="italic", weight="bold")

    add_footer(svg, 4)
    return svg


# ═══════════════════════════════════════════════════════════════════════════════
# LESSON 5: Отечественная война 1812 года
# ═══════════════════════════════════════════════════════════════════════════════

def lesson_5():
    svg = make_svg()
    add_gradient(svg, "bg5", BG_CREAM, "#FFF0F0")
    add_filter_shadow(svg, "shadow5")
    add_background(svg, "bg5")
    add_header(svg, "Отечественная война 1812 года", "Нашествие Наполеона, Бородино, пожар Москвы, изгнание")

    # ─── Timeline ─────────────────────────────────────────────────────────
    ty = 90
    rect(svg, 20, ty, W-40, 52, WHITE, stroke=PRIMARY_LIGHT, sw=1, rx=8, ry=8)
    line(svg, 40, ty + 26, W-40, ty + 26, PRIMARY, sw=3)

    events = [
        (80, "12 июня", "Втор-\nжение"),
        (200, "авг.", "Смоленск"),
        (320, "26 авг.", "Боро-\nдино"),
        (440, "сент.", "Москва"),
        (560, "окт.", "Отступ-\nление"),
        (680, "нояб.", "Березина"),
        (760, "дек.", "Конец"),
    ]
    for (x, date, ev) in events:
        add_timeline_event(svg, x, ty + 8, date, "", color=PRIMARY, line_y=ty + 26)
        lines = ev.split("\n")
        for i, l in enumerate(lines):
            text(svg, x, ty + 43 + i * 10, l, size=8, fill=TEXT_DARK)

    # ─── Left: Invasion Forces ────────────────────────────────────────────
    ix, iy = 25, 155
    rect(svg, ix, iy, 240, 140, WHITE, stroke="#1E40AF", sw=1.5, rx=8, ry=8, filter_id="shadow5")
    rect(svg, ix, iy, 240, 24, "#1E40AF", rx=8, ry=8)
    rect(svg, ix, iy + 14, 240, 10, "#1E40AF")
    text(svg, ix + 120, iy + 17, "Вторжение Наполеона", size=11, fill=WHITE, weight="bold")

    text(svg, ix + 120, iy + 40, "Великая армия: ~600 000 чел.", size=10, fill="#1E40AF", weight="bold")
    text(svg, ix + 10, iy + 56, "Армия Наполеона — крупнейшая", size=9, fill=TEXT_DARK, anchor="start")
    text(svg, ix + 10, iy + 70, "в истории Европы. Многонацио-", size=9, fill=TEXT_DARK, anchor="start")
    text(svg, ix + 10, iy + 84, "нальное войско: французы,", size=9, fill=TEXT_DARK, anchor="start")
    text(svg, ix + 10, iy + 98, "немцы, поляки, итальянцы...", size=9, fill=TEXT_DARK, anchor="start")
    text(svg, ix + 10, iy + 118, "12 июня 1812 — переход реки", size=9, fill=PRIMARY, anchor="start", weight="bold")
    text(svg, ix + 10, iy + 132, "Неман — начало войны", size=9, fill=PRIMARY, anchor="start", weight="bold")

    # ─── Center: Battle of Borodino ───────────────────────────────────────
    bx, by = 280, 155
    rect(svg, bx, by, 255, 140, WHITE, stroke=PRIMARY, sw=2, rx=8, ry=8, filter_id="shadow5")
    rect(svg, bx, by, 255, 24, PRIMARY, rx=8, ry=8)
    rect(svg, bx, by + 14, 255, 10, PRIMARY)
    draw_star(svg, bx + 15, by + 12, 8, ACCENT_GOLD)
    text(svg, bx + 140, by + 17, "Бородинское сражение", size=11, fill=WHITE, weight="bold")

    text(svg, bx + 127, by + 40, "26 августа (7 сент.) 1812 г.", size=10, fill=PRIMARY_DARK, weight="bold")

    # Comparison table
    # French
    rect(svg, bx + 10, by + 52, 112, 80, "#EFF6FF", stroke="#1E40AF", sw=1, rx=4, ry=4)
    text(svg, bx + 66, by + 66, "Французы", size=9, fill="#1E40AF", weight="bold")
    text(svg, bx + 66, by + 80, "~135 000 чел.", size=9, fill=TEXT_DARK)
    text(svg, bx + 66, by + 94, "~587 орудий", size=9, fill=TEXT_DARK)
    text(svg, bx + 66, by + 110, "Потери: ~35 000", size=9, fill="#1E40AF", weight="bold")

    # Russian
    rect(svg, bx + 132, by + 52, 112, 80, PRIMARY_PALE, stroke=PRIMARY, sw=1, rx=4, ry=4)
    text(svg, bx + 188, by + 66, "Русские", size=9, fill=PRIMARY, weight="bold")
    text(svg, bx + 188, by + 80, "~126 000 чел.", size=9, fill=TEXT_DARK)
    text(svg, bx + 188, by + 94, "~624 орудия", size=9, fill=TEXT_DARK)
    text(svg, bx + 188, by + 110, "Потери: ~44 000", size=9, fill=PRIMARY, weight="bold")

    # VS
    circle(svg, bx + 127, by + 92, 14, ACCENT_GOLD, stroke=WHITE, sw=2)
    text(svg, bx + 127, by + 96, "VS", size=9, fill=WHITE, weight="bold")

    # ─── Right: Fire of Moscow & Retreat ──────────────────────────────────
    rx3, ry3 = 550, 155
    rect(svg, rx3, ry3, 235, 140, WHITE, stroke="#F59E0B", sw=1.5, rx=8, ry=8, filter_id="shadow5")
    rect(svg, rx3, ry3, 235, 24, "#F59E0B", rx=8, ry=8)
    rect(svg, rx3, ry3 + 14, 235, 10, "#F59E0B")
    text(svg, rx3 + 117, ry3 + 17, "Пожар Москвы и отступление", size=11, fill=WHITE, weight="bold")

    fire_points = [
        "Наполеон вошёл в Москву 14 сент.",
        "Москва горела 5 дней",
        "Уничтожено 3/4 зданий",
        "Отсутствие провизии",
        "19 октября — уход из Москвы",
        "Кутузов: тактика заманивания",
        "Переправа через Березину —",
        "катастрофа для французов",
    ]
    for i, p in enumerate(fire_points):
        text(svg, rx3 + 10, ry3 + 38 + i * 13, p, size=8.5, fill=TEXT_DARK, anchor="start")

    # ─── Bottom Left: War Map ─────────────────────────────────────────────
    map_x2, map_y2 = 25, 310
    rect(svg, map_x2, map_y2, 345, 210, WHITE, stroke=PRIMARY_LIGHT, sw=1, rx=8, ry=8, filter_id="shadow5")
    text(svg, map_x2 + 172, map_y2 + 18, "Схема Отечественной войны 1812 г.", size=11, fill=PRIMARY_DARK, weight="bold")

    # Napoleonic advance arrow (red line going in)
    # Moscow marker
    circle(svg, map_x2 + 200, map_y2 + 80, 6, PRIMARY, stroke=WHITE, sw=2)
    text(svg, map_x2 + 200, map_y2 + 72, "Москва", size=9, fill=PRIMARY, weight="bold")

    # Advance arrow (left to center = West to Moscow)
    d_advance = f"M {map_x2+40} {map_y2+50} Q {map_x2+100} {map_y2+60} {map_x2+195} {map_y2+78}"
    path(svg, d_advance, "none", stroke="#1E40AF", sw=3)
    # Arrowhead
    polygon(svg, f"{map_x2+188},{map_y2+72} {map_x2+198},{map_y2+78} {map_x2+190},{map_y2+82}", "#1E40AF")

    text(svg, map_x2 + 80, map_y2 + 42, "Наступление Наполеона", size=8, fill="#1E40AF", weight="bold")

    # Retreat arrow (dashed, going back)
    d_retreat = f"M {map_x2+195} {map_y2+85} Q {map_x2+130} {map_y2+130} {map_x2+60} {map_y2+160}"
    path(svg, d_retreat, "none", stroke="#DC2626", sw=2.5, opacity="0.8")
    line(svg, map_x2 + 70, map_y2 + 158, map_x2 + 55, map_y2 + 162, "#DC2626", sw=2.5)

    text(svg, map_x2 + 80, map_y2 + 140, "Отступление", size=8, fill="#DC2626", weight="bold")

    # Berezina marker
    circle(svg, map_x2 + 100, map_y2 + 115, 4, "#F59E0B", stroke=WHITE, sw=1.5)
    text(svg, map_x2 + 110, map_y2 + 115, "р. Березина", size=7, fill="#F59E0B", anchor="start")

    # Smolensk
    circle(svg, map_x2 + 140, map_y2 + 65, 3, "#6366F1", stroke=WHITE, sw=1.5)
    text(svg, map_x2 + 150, map_y2 + 65, "Смоленск", size=7, fill="#6366F1", anchor="start")

    # Borodino
    circle(svg, map_x2 + 175, map_y2 + 73, 3, PRIMARY, stroke=WHITE, sw=1.5)
    text(svg, map_x2 + 165, map_y2 + 85, "Бородино", size=7, fill=PRIMARY, anchor="end")

    # Neman river
    text(svg, map_x2 + 35, map_y2 + 50, "р. Неман", size=7, fill="#3B82F6", anchor="start")

    # Legend
    rect(svg, map_x2 + 210, map_y2 + 160, 125, 42, "#F9FAFB", stroke="#E5E7EB", sw=1, rx=4, ry=4)
    line(svg, map_x2 + 218, map_y2 + 172, map_x2 + 238, map_y2 + 172, "#1E40AF", sw=2)
    text(svg, map_x2 + 242, map_y2 + 175, "Наступление", size=7, fill=TEXT_DARK, anchor="start")
    line(svg, map_x2 + 218, map_y2 + 190, map_x2 + 238, map_y2 + 190, "#DC2626", sw=2)
    text(svg, map_x2 + 242, map_y2 + 193, "Отступление", size=7, fill=TEXT_DARK, anchor="start")

    # ─── Bottom Right: Key Figures & Results ──────────────────────────────
    fig_x, fig_y = 385, 310
    rect(svg, fig_x, fig_y, 395, 100, WHITE, stroke=PRIMARY_LIGHT, sw=1, rx=8, ry=8, filter_id="shadow5")
    text(svg, fig_x + 197, fig_y + 18, "Полководцы Отечественной войны", size=11, fill=PRIMARY_DARK, weight="bold")

    # Kutuzov
    rect(svg, fig_x + 10, fig_y + 30, 120, 60, PRIMARY_PALE, stroke=PRIMARY, sw=1, rx=6, ry=6)
    text(svg, fig_x + 70, fig_y + 48, "М.И. Кутузов", size=10, fill=PRIMARY_DARK, weight="bold")
    text(svg, fig_x + 70, fig_y + 62, "Главнокомандующий", size=8, fill=TEXT_MEDIUM)
    text(svg, fig_x + 70, fig_y + 76, "Стратегия заманивания", size=8, fill=TEXT_MEDIUM)

    # Barclay de Tolly
    rect(svg, fig_x + 140, fig_y + 30, 120, 60, "#EFF6FF", stroke="#1E40AF", sw=1, rx=6, ry=6)
    text(svg, fig_x + 200, fig_y + 48, "Барклай", size=10, fill="#1E40AF", weight="bold")
    text(svg, fig_x + 200, fig_y + 62, "де Толли", size=10, fill="#1E40AF", weight="bold")
    text(svg, fig_x + 200, fig_y + 78, "Стратегия отступления", size=8, fill=TEXT_MEDIUM)

    # Bagration
    rect(svg, fig_x + 270, fig_y + 30, 115, 60, "#F0FDF4", stroke="#059669", sw=1, rx=6, ry=6)
    text(svg, fig_x + 327, fig_y + 48, "П.И. Багратион", size=10, fill="#059669", weight="bold")
    text(svg, fig_x + 327, fig_y + 64, "Герой Бородино", size=8, fill=TEXT_MEDIUM)
    text(svg, fig_x + 327, fig_y + 78, "Смертельно ранен", size=8, fill=TEXT_MEDIUM)

    # Results box
    res_x, res_y = 385, 420
    rect(svg, res_x, res_y, 395, 100, WHITE, stroke=ACCENT_GOLD, sw=1.5, rx=8, ry=8, filter_id="shadow5")
    rect(svg, res_x, res_y, 395, 24, ACCENT_GOLD, rx=8, ry=8)
    rect(svg, res_x, res_y + 14, 395, 10, ACCENT_GOLD)
    draw_star(svg, res_x + 15, res_y + 12, 8, WHITE)
    text(svg, res_x + 210, res_y + 17, "Итоги войны 1812 года", size=11, fill=WHITE, weight="bold")

    results = [
        "Полное уничтожение армии Наполеона",
        "Из ~600 000 вернулось ~30 000",
        "Россия сохранила независимость",
        "Начало заграничных походов русской армии",
        "Победа стала символом единства нации",
    ]
    for i, r in enumerate(results):
        text(svg, res_x + 20, res_y + 40 + i * 14, "✦ " + r, size=9, fill=TEXT_DARK, anchor="start")

    # ─── Quote ────────────────────────────────────────────────────────────
    rect(svg, 25, 530, W-50, 30, PRIMARY_PALE, stroke=PRIMARY_LIGHT, sw=1, rx=6, ry=6)
    text(svg, W//2, 549, "«Французы показали себя достойными победы, а русские заслужили быть непобедимыми» — Кутузов", size=10, fill=PRIMARY_DARK, style="italic", weight="bold")

    add_footer(svg, 5)
    return svg


# ═══════════════════════════════════════════════════════════════════════════════
# Main: Generate and save all 5 SVGs
# ═══════════════════════════════════════════════════════════════════════════════

def indent_xml(elem, level=0):
    """Pretty-print XML with indentation."""
    indent = "\n" + "  " * level
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = indent + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = indent
        for child in elem:
            indent_xml(child, level + 1)
        if not child.tail or not child.tail.strip():
            child.tail = indent
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = indent
    if level == 0:
        elem.tail = "\n"

def save_svg(svg, filepath):
    """Save SVG element to file with proper XML declaration."""
    indent_xml(svg)
    tree = ET.ElementTree(svg)
    ET.indent(tree, space="  ")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        tree.write(f, encoding="unicode", xml_declaration=False)

def validate_svg(filepath):
    """Validate SVG by parsing it as XML."""
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        # Check it's actually an SVG
        tag = root.tag.replace("{http://www.w3.org/2000/svg}", "")
        assert tag == "svg", f"Root element is '{tag}', not 'svg'"
        # Check dimensions
        w = root.get("width")
        h = root.get("height")
        assert w == "800", f"Width is {w}, expected 800"
        assert h == "600", f"Height is {h}, expected 600"
        return True, "Valid SVG (800x600)"
    except ET.ParseError as e:
        return False, f"XML Parse Error: {e}"
    except Exception as e:
        return False, f"Validation Error: {e}"

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    generators = [
        (1, "Начало правления Петра I", lesson_1),
        (2, "Северная война", lesson_2),
        (3, "Дворцовые перевороты", lesson_3),
        (4, "Екатерина II", lesson_4),
        (5, "Отечественная война 1812", lesson_5),
    ]

    results = []
    for num, title, gen_func in generators:
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
        print(f"Generating lesson {num}: {title}...")

        svg = gen_func()
        save_svg(svg, filepath)

        valid, msg = validate_svg(filepath)
        file_size = os.path.getsize(filepath)
        status = "✓" if valid else "✗"
        results.append((num, title, filepath, valid, msg, file_size))
        print(f"  {status} {msg} | Size: {file_size:,} bytes")

    print("\n" + "=" * 70)
    print("GRADE 8 HISTORY SVG GENERATION - SUMMARY")
    print("=" * 70)
    all_valid = True
    for num, title, filepath, valid, msg, size in results:
        status = "PASS" if valid else "FAIL"
        print(f"  Lesson {num}: [{status}] {title} | {size:,} bytes | {filepath}")
        if not valid:
            all_valid = False

    print("=" * 70)
    if all_valid:
        print("ALL 5 SVG FILES GENERATED AND VALIDATED SUCCESSFULLY!")
    else:
        print("SOME SVG FILES FAILED VALIDATION!")
    print("=" * 70)

if __name__ == "__main__":
    main()
