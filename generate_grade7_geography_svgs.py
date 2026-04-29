#!/usr/bin/env python3
"""Generate Grade 7 Geography SVG files — Russian curriculum, green/teal color scheme."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/geography"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── colour palette ──────────────────────────────────────────────────────────
PRIMARY      = "#059669"
PRIMARY_DARK = "#047857"
PRIMARY_LITE = "#6EE7B7"
TEAL_LIGHT   = "#ECFDF5"
TEAL_MID     = "#A7F3D0"
BG           = "#FFFFFF"
TEXT_DARK    = "#1F2937"
TEXT_MED     = "#4B5563"
TEXT_LIGHT   = "#9CA3AF"
ACCENT_BLUE  = "#0E7490"
ACCENT_AMBER = "#B45309"
ACCENT_VIOLET = "#6D28D9"
OCEAN_BLUE   = "#0284C7"
OCEAN_DEEP   = "#075985"
DESERT_SAND  = "#D97706"
ICE_BLUE     = "#BAE6FD"

W, H = 800, 600


def escape(text: str) -> str:
    """Escape XML special characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


# ── helpers ─────────────────────────────────────────────────────────────────
def svg_root():
    root = ET.Element("svg")
    root.set("xmlns", "http://www.w3.org/2000/svg")
    root.set("width", str(W))
    root.set("height", str(H))
    root.set("viewBox", f"0 0 {W} {H}")
    return root


def add_rect(parent, x, y, w, h, fill, rx=0, stroke=None, sw=0, opacity=None):
    el = ET.SubElement(parent, "rect")
    el.set("x", str(x)); el.set("y", str(y))
    el.set("width", str(w)); el.set("height", str(h))
    el.set("rx", str(rx)); el.set("fill", fill)
    if stroke: el.set("stroke", stroke); el.set("stroke-width", str(sw))
    if opacity is not None: el.set("opacity", str(opacity))
    return el


def add_text(parent, x, y, text, size=14, fill=TEXT_DARK, anchor="middle", weight="normal", ff="sans-serif"):
    el = ET.SubElement(parent, "text")
    el.set("x", str(x)); el.set("y", str(y))
    el.set("text-anchor", anchor); el.set("fill", fill)
    el.set("font-size", str(size)); el.set("font-weight", weight)
    el.set("font-family", ff)
    el.text = escape(text)
    return el


def add_line(parent, x1, y1, x2, y2, stroke=PRIMARY, sw=2, dash=None):
    el = ET.SubElement(parent, "line")
    el.set("x1", str(x1)); el.set("y1", str(y1))
    el.set("x2", str(x2)); el.set("y2", str(y2))
    el.set("stroke", stroke); el.set("stroke-width", str(sw))
    if dash: el.set("stroke-dasharray", dash)
    return el


def add_circle(parent, cx, cy, r, fill, stroke=None, sw=0):
    el = ET.SubElement(parent, "circle")
    el.set("cx", str(cx)); el.set("cy", str(cy)); el.set("r", str(r))
    el.set("fill", fill)
    if stroke: el.set("stroke", stroke); el.set("stroke-width", str(sw))
    return el


def add_ellipse(parent, cx, cy, rx, ry, fill, stroke=None, sw=0):
    el = ET.SubElement(parent, "ellipse")
    el.set("cx", str(cx)); el.set("cy", str(cy))
    el.set("rx", str(rx)); el.set("ry", str(ry))
    el.set("fill", fill)
    if stroke: el.set("stroke", stroke); el.set("stroke-width", str(sw))
    return el


def add_polygon(parent, points, fill, stroke=None, sw=0):
    el = ET.SubElement(parent, "polygon")
    el.set("points", " ".join(f"{x},{y}" for x, y in points))
    el.set("fill", fill)
    if stroke: el.set("stroke", stroke); el.set("stroke-width", str(sw))
    return el


def add_path(parent, d, fill="none", stroke=PRIMARY, sw=2):
    el = ET.SubElement(parent, "path")
    el.set("d", d); el.set("fill", fill); el.set("stroke", stroke); el.set("stroke-width", str(sw))
    return el


def header_banner(root, title, subtitle=""):
    """Top green banner with title."""
    add_rect(root, 0, 0, W, 72, PRIMARY)
    add_rect(root, 0, 72, W, 4, PRIMARY_DARK)
    add_text(root, W // 2, 36, title, 22, "#FFFFFF", weight="bold")
    if subtitle:
        add_text(root, W // 2, 58, subtitle, 12, "#FFFFFF", weight="normal")


def footer(root, lesson_num):
    add_rect(root, 0, H - 30, W, 30, TEAL_LIGHT)
    add_line(root, 0, H - 30, W, H - 30, PRIMARY_LITE, 1)
    add_text(root, W // 2, H - 10, f"7 класс — География — Урок {lesson_num}", 10, TEXT_LIGHT)


def info_box(parent, x, y, w, h, title, body_lines, accent=PRIMARY):
    """Rounded info card with accent left border."""
    add_rect(parent, x, y, w, h, "#FFFFFF", rx=6, stroke="#E5E7EB", sw=1)
    add_rect(parent, x, y, 5, h, accent, rx=2)
    add_text(parent, x + 16, y + 20, title, 13, accent, anchor="start", weight="bold")
    ty = y + 38
    for line in body_lines:
        add_text(parent, x + 16, ty, line, 11, TEXT_MED, anchor="start")
        ty += 16


def card_with_header(parent, x, y, w, h, title, body_lines, accent=PRIMARY):
    """Card with colored header bar."""
    add_rect(parent, x, y, w, h, "#FFFFFF", rx=6, stroke=accent, sw=1)
    add_rect(parent, x, y, w, 24, accent, rx=6)
    add_rect(parent, x, y + 20, w, 6, accent)
    add_text(parent, x + w // 2, y + 16, title, 11, "#FFFFFF", weight="bold")
    ty = y + 42
    for line in body_lines:
        add_text(parent, x + 10, ty, line, 10, TEXT_DARK, anchor="start")
        ty += 14


# ════════════════════════════════════════════════════════════════════════════
#  LESSON 1 — Литосфера и рельеф Земли
# ════════════════════════════════════════════════════════════════════════════
def lesson1():
    root = svg_root()
    header_banner(root, "Литосфера и рельеф Земли", "Тектонические плиты, горы и равнины")
    footer(root, 1)

    add_rect(root, 0, 76, W, H - 106, TEAL_LIGHT, opacity=0.4)

    # ── Simplified world map showing major plates ───────────────────────
    add_text(root, W // 2, 98, "Крупнейшие литосферные плиты", 14, PRIMARY_DARK, weight="bold")

    # Simplified map outline (abstract continent shapes)
    map_x, map_y = 60, 110
    map_w, map_h = 440, 200

    # Ocean background
    add_rect(root, map_x, map_y, map_w, map_h, "#DBEAFE", rx=4, stroke="#93C5FD", sw=1)

    # Simplified continent shapes as polygons
    # Eurasia (simplified)
    add_polygon(root, [
        (140, 130), (200, 120), (280, 125), (350, 130), (400, 140),
        (420, 160), (380, 170), (350, 180), (300, 175), (250, 180),
        (200, 170), (150, 160), (130, 145)
    ], "#D1FAE5", PRIMARY, 1)

    # Africa
    add_polygon(root, [
        (220, 195), (250, 190), (270, 200), (275, 230), (265, 260),
        (250, 280), (235, 275), (225, 250), (215, 220), (218, 200)
    ], "#D1FAE5", PRIMARY, 1)

    # North America
    add_polygon(root, [
        (80, 130), (110, 120), (130, 125), (135, 145), (130, 160),
        (120, 175), (105, 180), (90, 170), (75, 155), (72, 140)
    ], "#D1FAE5", PRIMARY, 1)

    # South America
    add_polygon(root, [
        (130, 210), (150, 200), (160, 215), (155, 240), (145, 260),
        (135, 275), (125, 265), (120, 240), (125, 220)
    ], "#D1FAE5", PRIMARY, 1)

    # Australia
    add_polygon(root, [
        (390, 240), (420, 235), (440, 245), (440, 260), (425, 270),
        (400, 265), (388, 255)
    ], "#D1FAE5", PRIMARY, 1)

    # Antarctica
    add_polygon(root, [
        (150, 290), (250, 295), (350, 290), (400, 295), (400, 305),
        (250, 305), (100, 305)
    ], "#E0F2FE", PRIMARY, 1)

    # Plate labels
    add_text(root, 280, 150, "Евразиатская", 9, PRIMARY_DARK, weight="bold")
    add_text(root, 100, 150, "Северо-\nамериканская", 8, PRIMARY_DARK, anchor="middle")
    add_text(root, 240, 240, "Африканская", 8, PRIMARY_DARK, weight="bold")
    add_text(root, 140, 240, "Южно-\nамериканская", 8, PRIMARY_DARK, anchor="middle")
    add_text(root, 415, 255, "Индо-\nавстралийская", 7, PRIMARY_DARK, anchor="middle")

    # Plate boundaries (dashed lines)
    add_line(root, 200, 130, 200, 300, "#DC2626", 1, dash="4,3")
    add_line(root, 320, 130, 320, 300, "#DC2626", 1, dash="4,3")
    add_line(root, 70, 190, 450, 190, "#DC2626", 1, dash="4,3")

    add_text(root, 250, 310, "— границы плит", 8, "#DC2626", anchor="start")

    # ── Right side: Vertical structure of Earth ──────────────────────────
    sx = 530
    add_text(root, 660, 98, "Строение Земли", 14, PRIMARY_DARK, weight="bold")

    # Concentric layers
    cx, cy = 660, 220
    layers = [
        (80, "#F59E0B", "Мантия"),
        (55, "#EF4444", "Внешнее ядро"),
        (30, "#DC2626", "Внутреннее ядро"),
    ]
    for r, color, name in layers:
        add_circle(root, cx, cy, r, color, "#FFFFFF", 1)

    # Lithosphere ring (thin)
    add_circle(root, cx, cy, 85, "none", PRIMARY, 3)
    add_text(root, cx, cy - 92, "Литосфера", 9, PRIMARY, weight="bold")
    add_text(root, cx, cy - 40, "Мантия", 9, "#FFFFFF", weight="bold")
    add_text(root, cx, cy - 5, "Ядро", 9, "#FFFFFF", weight="bold")

    # Earth layer thickness labels
    add_text(root, cx, cy + 95, "Земная кора: 5-70 км", 9, TEXT_MED)
    add_text(root, cx, cy + 110, "Мантия: ~2900 км", 9, TEXT_MED)
    add_text(root, cx, cy + 125, "Ядро: ~3500 км", 9, TEXT_MED)

    # ── Bottom: Mountains and plains ────────────────────────────────────
    add_text(root, W // 2, 345, "Формы рельефа", 14, PRIMARY_DARK, weight="bold")
    add_line(root, 80, 349, W - 80, 349, PRIMARY_LITE, 1)

    # Mountain diagram (left)
    add_text(root, 130, 370, "Горы", 12, PRIMARY, weight="bold")
    # Draw mountain range
    add_polygon(root, [
        (40, 490), (70, 400), (90, 430), (120, 370), (150, 420),
        (170, 380), (200, 440), (220, 490)
    ], "#A7F3D0", PRIMARY, 2)
    # Snow caps
    add_polygon(root, [(110, 370), (120, 370), (130, 390), (115, 395)], "#FFFFFF", "#93C5FD", 1)
    add_polygon(root, [(160, 380), (170, 380), (180, 395), (165, 400)], "#FFFFFF", "#93C5FD", 1)

    add_text(root, 130, 510, "Высшая точка:", 9, TEXT_MED, anchor="middle")
    add_text(root, 130, 524, "г. Джомолунгма", 10, PRIMARY_DARK, anchor="middle", weight="bold")
    add_text(root, 130, 538, "8848 м", 10, PRIMARY, anchor="middle", weight="bold")

    # Plains diagram (center)
    add_text(root, 400, 370, "Равнины", 12, PRIMARY, weight="bold")
    # Draw flat landscape with slight hills
    add_rect(root, 300, 470, 200, 20, "#86EFAC", rx=0, stroke=PRIMARY, sw=1)
    add_path(root, "M 300,470 Q 340,460 370,470 Q 400,475 430,465 Q 460,460 500,470", "#86EFAC", PRIMARY, 1)
    # Lowland
    add_rect(root, 300, 490, 200, 30, "#BBF7D0", rx=0, stroke=PRIMARY_LITE, sw=1)
    add_text(root, 400, 510, "низменности (0-200 м)", 9, TEXT_MED, anchor="middle")
    add_text(root, 400, 465, "возвышенности (200-500 м)", 9, TEXT_MED, anchor="middle")

    types_plain = ["Низменности (0-200 м)", "Возвышенности (200-500 м)", "Плоскогорья (500-1000 м)"]
    for i, t in enumerate(types_plain):
        add_text(root, 400, 540 + i * 14, t, 9, TEXT_MED, anchor="middle")

    # Types of mountains (right)
    add_text(root, 660, 370, "Типы гор", 12, PRIMARY, weight="bold")

    mt_types = [
        ("Складчатые", "Образуются при сжатии\nлитосферных плит", "#059669"),
        ("Глыбовые", "Образуются при разломах\nи поднятиях блоков", "#0E7490"),
        ("Вулканические", "Образуются из\nизвержений магмы", "#B45309"),
    ]
    for i, (name, desc, clr) in enumerate(mt_types):
        y = 390 + i * 58
        add_rect(root, 540, y, 240, 52, "#FFFFFF", rx=4, stroke=clr, sw=1)
        add_rect(root, 540, y, 4, 52, clr, rx=2)
        add_text(root, 554, y + 16, name, 11, clr, anchor="start", weight="bold")
        for j, ln in enumerate(desc.split("\n")):
            add_text(root, 554, y + 30 + j * 12, ln, 9, TEXT_MED, anchor="start")

    return root


# ════════════════════════════════════════════════════════════════════════════
#  LESSON 2 — Атмосфера и климаты Земли
# ════════════════════════════════════════════════════════════════════════════
def lesson2():
    root = svg_root()
    header_banner(root, "Атмосфера и климаты Земли", "Строение атмосферы, температура, давление, ветры")
    footer(root, 2)

    add_rect(root, 0, 76, W, H - 106, TEAL_LIGHT, opacity=0.4)

    # ── Left: Atmosphere layers diagram ─────────────────────────────────
    add_text(root, 170, 98, "Строение атмосферы", 14, PRIMARY_DARK, weight="bold")

    layers = [
        ("Тропосфера", "0-12 км", "#86EFAC", "80% массы воздуха,\nобразование облаков,\nосадки, погода"),
        ("Стратосфера", "12-50 км", "#6EE7B7", "Озоновый слой,\nзащита от УФ-лучей"),
        ("Мезосфера", "50-80 км", "#34D399", "Метеоры сгорают,\nнизкая температура"),
        ("Термосфера", "80-800 км", "#10B981", "Ионосфера,\nполярные сияния"),
        ("Экзосфера", "800+ км", "#059669", "Переход в космос,\nубегание газов"),
    ]
    for i, (name, height, color, desc) in enumerate(layers):
        y = 112 + i * 55
        add_rect(root, 30, y, 300, 50, color, rx=4, stroke=PRIMARY, sw=1, opacity=0.7)
        add_text(root, 45, y + 18, name, 12, TEXT_DARK, anchor="start", weight="bold")
        add_text(root, 45, y + 34, height, 10, PRIMARY_DARK, anchor="start")
        for j, ln in enumerate(desc.split("\n")):
            add_text(root, 170, y + 14 + j * 12, ln, 8, TEXT_MED, anchor="start")

    # ── Right top: Temperature/Pressure diagram ─────────────────────────
    add_text(root, 580, 98, "Температура и давление", 14, PRIMARY_DARK, weight="bold")

    # Simplified temperature graph
    gx, gy = 460, 115
    gw, gh = 280, 130
    add_rect(root, gx, gy, gw, gh, "#FFFFFF", rx=4, stroke=PRIMARY_LITE, sw=1)

    # Axes
    add_line(root, gx + 30, gy + 10, gx + 30, gy + gh - 10, TEXT_LIGHT, 1)
    add_line(root, gx + 30, gy + gh - 10, gx + gw - 10, gy + gh - 10, TEXT_LIGHT, 1)

    # Temperature curve (decreases then increases with altitude)
    add_path(root, f"M {gx+40},{gy+30} Q {gx+90},{gy+90} {gx+140},{gy+110} Q {gx+180},{gy+120} {gx+220},{gy+40} Q {gx+240},{gy+20} {gx+260},{gy+15}",
             "none", "#DC2626", 2)

    add_text(root, gx + 20, gy + gh - 15, "0", 8, TEXT_LIGHT, anchor="end")
    add_text(root, gx + gw // 2, gy + gh, "Высота, км", 8, TEXT_MED)
    add_text(root, gx + 40, gy + gh - 15, "0", 7, TEXT_LIGHT)
    add_text(root, gx + 120, gy + gh - 15, "50", 7, TEXT_LIGHT)
    add_text(root, gx + 200, gy + gh - 15, "100", 7, TEXT_LIGHT)
    add_text(root, gx + 50, gy + 20, "t °C", 8, "#DC2626", anchor="start")

    # Pressure info
    add_text(root, 580, 265, "Атмосферное давление", 12, PRIMARY_DARK, weight="bold")
    add_text(root, 580, 282, "760 мм рт. ст. — норма", 10, TEXT_MED)
    add_text(root, 580, 296, "Падает с высотой: ~1 мм на 10,5 м", 10, TEXT_MED)

    # ── Bottom: Climate zones and winds ─────────────────────────────────
    add_text(root, W // 2, 328, "Климатические пояса и ветры", 14, PRIMARY_DARK, weight="bold")
    add_line(root, 80, 332, W - 80, 332, PRIMARY_LITE, 1)

    # Simplified Earth cross-section showing climate zones
    cx, cy = 400, 460
    # Outer circle = Earth
    add_circle(root, cx, cy, 120, "#DBEAFE", PRIMARY, 1)

    # Climate bands (horizontal strips within circle)
    # Equatorial
    add_rect(root, cx - 118, cy - 15, 236, 30, "#FDE68A", opacity=0.7)
    # Tropical
    add_rect(root, cx - 115, cy - 45, 230, 28, "#FCD34D", opacity=0.5)
    add_rect(root, cx - 115, cy + 17, 230, 28, "#FCD34D", opacity=0.5)
    # Subtropical
    add_rect(root, cx - 110, cy - 75, 220, 26, "#FBBF24", opacity=0.4)
    add_rect(root, cx - 110, cy + 49, 220, 26, "#FBBF24", opacity=0.4)
    # Temperate
    add_rect(root, cx - 100, cy - 100, 200, 22, "#A7F3D0", opacity=0.5)
    add_rect(root, cx - 100, cy + 78, 200, 22, "#A7F3D0", opacity=0.5)

    # Labels on the globe
    add_text(root, cx, cy, "Экваториальный", 8, TEXT_DARK, weight="bold")
    add_text(root, cx, cy - 33, "Тропический", 7, TEXT_DARK)
    add_text(root, cx, cy + 33, "Тропический", 7, TEXT_DARK)
    add_text(root, cx, cy - 63, "Субтропический", 7, TEXT_DARK)
    add_text(root, cx, cy + 63, "Субтропический", 7, TEXT_DARK)
    add_text(root, cx, cy - 90, "Умеренный", 6, TEXT_DARK)
    add_text(root, cx, cy + 90, "Умеренный", 6, TEXT_DARK)

    # Equator line
    add_line(root, cx - 120, cy, cx + 120, cy, "#DC2626", 1, dash="3,2")
    add_text(root, cx + 130, cy, "Экватор", 8, "#DC2626", anchor="start")

    # Wind arrows (trade winds, westerlies)
    # NE Trade winds
    add_path(root, f"M {cx-60},{cy-55} Q {cx-40},{cy-50} {cx-20},{cy-55}", "none", PRIMARY, 1)
    add_text(root, cx - 40, cy - 45, "Пассаты", 6, PRIMARY)

    # Westerlies
    add_path(root, f"M {cx-60},{cy-90} Q {cx-40},{cy-85} {cx-20},{cy-90}", "none", ACCENT_BLUE, 1)
    add_text(root, cx - 40, cy - 80, "Зап. ветры", 6, ACCENT_BLUE)

    # Legend
    add_text(root, 80, 355, "Основные типы воздушных масс:", 10, PRIMARY_DARK, anchor="start", weight="bold")
    wind_info = [
        ("Пассаты", "от 30° к экватору", PRIMARY),
        ("Западные ветры", "от 30° к 60°", ACCENT_BLUE),
        ("Полярные ветры", "от полюсов к 60°", ACCENT_VIOLET),
    ]
    for i, (name, desc, clr) in enumerate(wind_info):
        add_text(root, 80, 375 + i * 16, f"  {name} — {desc}", 9, clr, anchor="start")

    # Right side: key climate facts
    add_text(root, 660, 360, "Главное:", 11, PRIMARY_DARK, anchor="start", weight="bold")
    climate_facts = [
        "Главный фактор —",
        "широта (угол падения",
        "солнечных лучей)",
        "",
        "13 климатических поясов:",
        "7 основных + 6 переходных",
        "",
        "Климатообразующие",
        "факторы: широта,",
        "океанические течения,",
        "рельеф, расстояние",
        "от океана",
    ]
    for i, f in enumerate(climate_facts):
        add_text(root, 660, 376 + i * 13, f, 9, TEXT_MED, anchor="start")

    return root


# ════════════════════════════════════════════════════════════════════════════
#  LESSON 3 — Численность и размещение населения
# ════════════════════════════════════════════════════════════════════════════
def lesson3():
    root = svg_root()
    header_banner(root, "Численность и размещение населения", "Плотность, урбанизация, демография")
    footer(root, 3)

    add_rect(root, 0, 76, W, H - 106, TEAL_LIGHT, opacity=0.4)

    # ── Top: World population key figures ────────────────────────────────
    add_text(root, W // 2, 98, "Население Земли: ключевые данные", 15, PRIMARY_DARK, weight="bold")

    # Big number
    add_rect(root, 220, 108, 360, 48, PRIMARY_DARK, rx=8)
    add_text(root, 400, 138, "8 млрд человек (2022 г.)", 18, "#FFFFFF", weight="bold")

    # ── Map with population density ─────────────────────────────────────
    add_text(root, W // 2, 178, "Размещение населения по регионам", 13, PRIMARY_DARK, weight="bold")

    # Simplified world map
    map_x, map_y = 40, 190
    map_w, map_h = 720, 170
    add_rect(root, map_x, map_y, map_w, map_h, "#DBEAFE", rx=4, stroke="#93C5FD", sw=1)

    # Dots representing population density
    # East Asia (high density)
    for dx, dy in [(540, 230), (555, 225), (550, 240), (565, 235), (535, 220), (560, 245), (545, 250), (570, 228), (530, 235), (555, 250)]:
        add_circle(root, dx, dy, 5, PRIMARY, "#FFFFFF", 1)
    add_text(root, 555, 265, "Восточная Азия", 8, PRIMARY_DARK)
    add_text(root, 555, 275, "(высокая плотность)", 7, TEXT_MED)

    # South Asia (very high)
    for dx, dy in [(480, 250), (495, 245), (490, 260), (505, 255), (475, 240), (500, 265), (485, 270)]:
        add_circle(root, dx, dy, 5, PRIMARY_DARK, "#FFFFFF", 1)
    add_text(root, 490, 285, "Южная Азия", 8, PRIMARY_DARK)
    add_text(root, 490, 295, "(очень высокая)", 7, TEXT_MED)

    # Europe (high)
    for dx, dy in [(360, 210), (375, 205), (370, 220), (385, 215), (355, 220)]:
        add_circle(root, dx, dy, 4, "#0E7490", "#FFFFFF", 1)
    add_text(root, 370, 232, "Европа", 8, "#0E7490")

    # Africa (growing)
    for dx, dy in [(390, 260), (400, 255), (395, 270), (410, 265)]:
        add_circle(root, dx, dy, 4, "#B45309", "#FFFFFF", 1)
    add_text(root, 400, 282, "Африка", 8, "#B45309")
    add_text(root, 400, 292, "(быстрый рост)", 7, TEXT_MED)

    # N. America
    for dx, dy in [(180, 215), (195, 210), (190, 225)]:
        add_circle(root, dx, dy, 4, "#6D28D9", "#FFFFFF", 1)
    add_text(root, 190, 237, "Сев. Америка", 8, "#6D28D9")

    # S. America
    for dx, dy in [(250, 275), (260, 270), (255, 285)]:
        add_circle(root, dx, dy, 3, "#0E7490", "#FFFFFF", 1)
    add_text(root, 255, 295, "Юж. Америка", 8, "#0E7490")

    # Australia
    add_circle(root, 600, 275, 3, "#6D28D9", "#FFFFFF", 1)
    add_text(root, 600, 288, "Австралия", 8, "#6D28D9")

    # Legend
    add_text(root, 80, 205, "Размер точки =", 7, TEXT_MED, anchor="start")
    add_text(root, 80, 215, "плотность населения", 7, TEXT_MED, anchor="start")

    # ── Bottom left: Population density chart ────────────────────────────
    add_text(root, 150, 388, "Плотность населения (чел/км²)", 12, PRIMARY_DARK, weight="bold")

    # Bar chart
    bars = [
        ("Азия", 90, PRIMARY_DARK),
        ("Европа", 34, PRIMARY),
        ("Африка", 35, "#B45309"),
        ("Сев.Америка", 20, ACCENT_BLUE),
        ("Юж.Америка", 22, "#6D28D9"),
        ("Австралия", 3, TEXT_MED),
        ("Океания", 8, TEAL_MID),
    ]
    bar_y = 405
    max_bar = 100
    for i, (name, val, clr) in enumerate(bars):
        y = bar_y + i * 22
        bw = int(val / max_bar * 150)
        add_rect(root, 100, y, bw, 16, clr, rx=2)
        add_text(root, 95, y + 12, name, 8, TEXT_DARK, anchor="end")
        add_text(root, 105 + bw, y + 12, str(val), 8, clr, anchor="start", weight="bold")

    # ── Bottom right: Urbanization ──────────────────────────────────────
    add_text(root, 580, 388, "Урбанизация", 13, PRIMARY_DARK, weight="bold")

    urban_data = [
        ("Доля горожан в мире", "56% (2020 г.)", PRIMARY),
        ("Наиболее урбанизированные", "", PRIMARY_DARK),
        ("  Аргентина, Австралия", "92%", ACCENT_BLUE),
        ("  Великобритания, Бельгия", "83%", ACCENT_BLUE),
        ("Наименее урбанизированные", "", PRIMARY_DARK),
        ("  Руанда, Бурунди", "14%", "#B45309"),
        ("  Эфиопия, Малави", "21%", "#B45309"),
    ]
    for i, (label, val, clr) in enumerate(urban_data):
        add_text(root, 440, 408 + i * 17, label, 10, clr, anchor="start",
                 weight="bold" if val == "" else "normal")
        if val:
            add_text(root, 720, 408 + i * 17, val, 10, clr, anchor="end", weight="bold")

    # Key factors box
    add_rect(root, 440, 530, 320, 30, "#FFFFFF", rx=4, stroke=PRIMARY, sw=1)
    add_rect(root, 440, 530, 4, 30, PRIMARY, rx=2)
    add_text(root, 454, 549, "Факторы размещения: климат, рельеф, ресурсы, транспорт", 9, TEXT_MED, anchor="start")

    return root


# ════════════════════════════════════════════════════════════════════════════
#  LESSON 4 — Народы и религии мира
# ════════════════════════════════════════════════════════════════════════════
def lesson4():
    root = svg_root()
    header_banner(root, "Народы и религии мира", "Языковые семьи и мировые религии")
    footer(root, 4)

    add_rect(root, 0, 76, W, H - 106, TEAL_LIGHT, opacity=0.4)

    # ── Top: Language families ───────────────────────────────────────────
    add_text(root, W // 2, 98, "Крупнейшие языковые семьи", 14, PRIMARY_DARK, weight="bold")

    # Horizontal bar chart
    families = [
        ("Индоевропейская", 45, PRIMARY_DARK, "2,5 млрд чел."),
        ("Сино-тибетская", 22, PRIMARY, "1,2 млрд чел."),
        ("Нигеро-конголезская", 6, "#0E7490", "350 млн чел."),
        ("Афразийская", 5, "#B45309", "300 млн чел."),
        ("Австронезийская", 4, "#6D28D9", "300 млн чел."),
        ("Дравидийская", 3, ACCENT_AMBER, "220 млн чел."),
        ("Алтайская", 2, TEXT_MED, "100 млн чел."),
    ]
    bar_x = 180
    bar_max = 320
    for i, (name, pct, clr, pop) in enumerate(families):
        y = 112 + i * 30
        bw = int(pct / 50 * bar_max)
        add_rect(root, bar_x, y, bw, 20, clr, rx=3)
        add_text(root, bar_x - 5, y + 14, name, 10, TEXT_DARK, anchor="end")
        add_text(root, bar_x + bw + 5, y + 14, pop, 9, clr, anchor="start", weight="bold")

    add_text(root, bar_x + bar_max // 2, 330, "Доля говорящих (%)", 9, TEXT_LIGHT)

    # ── Bottom: World religions ─────────────────────────────────────────
    add_text(root, W // 2, 350, "Мировые религии", 15, PRIMARY_DARK, weight="bold")
    add_line(root, 80, 354, W - 80, 354, PRIMARY_LITE, 1)

    religions = [
        ("Христианство", "2,4 млрд", PRIMARY_DARK, [
            "Католицизм, протестантизм,",
            "православие",
            "Европа, Америка, Африка",
        ]),
        ("Ислам", "1,9 млрд", "#0E7490", [
            "Суннизм, шиизм",
            "Ближний Восток,",
            "Северная Африка, Азия",
        ]),
        ("Буддизм", "500 млн", "#B45309", [
            "Тхеравада, махаяна",
            "Восточная и",
            "Юго-Восточная Азия",
        ]),
        ("Индуизм", "1,2 млрд", "#6D28D9", [
            "Ведическая традиция",
            "Индия, Непал,",
            "Бали",
        ]),
    ]
    for i, (name, pop, clr, lines) in enumerate(religions):
        x = 25 + i * 195
        add_rect(root, x, 370, 185, 170, "#FFFFFF", rx=6, stroke=clr, sw=2)
        add_rect(root, x, 370, 185, 28, clr, rx=6)
        add_rect(root, x, 392, 185, 6, clr)
        add_text(root, x + 92, 388, name, 12, "#FFFFFF", weight="bold")

        # Population
        add_rect(root, x + 30, 408, 125, 20, TEAL_MID, rx=3)
        add_text(root, x + 92, 422, pop, 11, clr, weight="bold")

        for j, ln in enumerate(lines):
            add_text(root, x + 92, 445 + j * 15, ln, 10, TEXT_MED)

    # National religions note
    add_rect(root, 60, 545, 680, 20, "#FFFFFF", rx=3, stroke=PRIMARY_LITE, sw=1)
    add_text(root, 400, 558, "Национальные религии: иудаизм, синтоизм, даосизм, конфуцианство", 10, TEXT_MED)

    return root


# ════════════════════════════════════════════════════════════════════════════
#  LESSON 5 — Тихий и Атлантический океаны
# ════════════════════════════════════════════════════════════════════════════
def lesson5():
    root = svg_root()
    header_banner(root, "Тихий и Атлантический океаны", "Особенности, течения, ресурсы")
    footer(root, 5)

    add_rect(root, 0, 76, W, H - 106, TEAL_LIGHT, opacity=0.4)

    # ── Pacific Ocean (left) ────────────────────────────────────────────
    add_text(root, 200, 98, "Тихий океан", 15, PRIMARY_DARK, weight="bold")

    # Ocean shape
    add_ellipse(root, 200, 260, 150, 120, "#0EA5E9", "#0284C7", 2)

    # Marianas Trench mark
    add_line(root, 180, 200, 180, 210, "#DC2626", 2)
    add_text(root, 180, 195, "Марианский жёлоб", 7, "#DC2626", weight="bold")
    add_text(root, 180, 215, "11 022 м", 7, "#DC2626")

    # Currents arrows (simplified)
    add_path(root, "M 130,200 Q 100,240 130,280", "none", "#DC2626", 1)
    add_text(root, 90, 240, "Курильское", 6, "#DC2626")
    add_path(root, "M 270,200 Q 300,240 270,280", "none", "#DC2626", 1)
    add_text(root, 305, 240, "Куросио", 6, "#DC2626")

    # Key facts
    pacific_facts = [
        "Площадь: 178,6 млн км²",
        "Средняя глубина: 3 976 м",
        "Наибольшая глубина: 11 022 м",
        "Омывает 5 материков",
        "Тихоокеанское огненное кольцо",
        "Богат рыбными ресурсами",
    ]
    for i, f in enumerate(pacific_facts):
        add_text(root, 200, 395 + i * 15, f, 10, TEXT_MED)

    # Pacific data box
    add_rect(root, 50, 380, 300, 25, "#FFFFFF", rx=3, stroke=PRIMARY, sw=1)
    add_rect(root, 50, 380, 4, 25, PRIMARY, rx=2)
    add_text(root, 62, 397, "Самый большой и глубокий океан Земли", 10, PRIMARY, anchor="start", weight="bold")

    # ── Atlantic Ocean (right) ──────────────────────────────────────────
    add_text(root, 600, 98, "Атлантический океан", 15, PRIMARY_DARK, weight="bold")

    # Ocean shape (narrower, S-shaped)
    add_ellipse(root, 600, 260, 100, 130, "#0EA5E9", "#0284C7", 2)

    # Mid-Atlantic Ridge
    add_line(root, 600, 160, 600, 360, "#F59E0B", 2, dash="5,3")
    add_text(root, 620, 200, "Срединно-\nАтлантический\nхребет", 6, "#F59E0B", anchor="start")

    # Gulf Stream
    add_path(root, "M 570,180 Q 560,220 575,260 Q 585,290 570,320", "none", "#DC2626", 2)
    add_text(root, 540, 230, "Гольфстрим", 7, "#DC2626")

    # Key facts
    atlantic_facts = [
        "Площадь: 91,6 млн км²",
        "Средняя глубина: 3 604 м",
        "Наибольшая глубина: 8 742 м",
        "S-образная форма",
        "Срединный хребет — 18 000 км",
        "Гольфстрим влияет на климат Европы",
    ]
    for i, f in enumerate(atlantic_facts):
        add_text(root, 600, 395 + i * 15, f, 10, TEXT_MED)

    # Atlantic data box
    add_rect(root, 450, 380, 300, 25, "#FFFFFF", rx=3, stroke=OCEAN_BLUE, sw=1)
    add_rect(root, 450, 380, 4, 25, OCEAN_BLUE, rx=2)
    add_text(root, 462, 397, "Второй по величине океан", 10, OCEAN_BLUE, anchor="start", weight="bold")

    # ── Bottom: Comparison table ────────────────────────────────────────
    add_text(root, W // 2, 498, "Сравнительная характеристика", 13, PRIMARY_DARK, weight="bold")
    add_line(root, 80, 502, W - 80, 502, PRIMARY_LITE, 1)

    # Table header
    add_rect(root, 80, 510, 640, 20, PRIMARY, rx=3)
    add_text(root, 170, 524, "Показатель", 10, "#FFFFFF", weight="bold")
    add_text(root, 400, 524, "Тихий океан", 10, "#FFFFFF", weight="bold")
    add_text(root, 600, 524, "Атлантический океан", 10, "#FFFFFF", weight="bold")

    rows = [
        ("Площадь", "178,6 млн км²", "91,6 млн км²"),
        ("Макс. глубина", "11 022 м", "8 742 м"),
    ]
    for i, (param, pac, atl) in enumerate(rows):
        y = 532 + i * 18
        bg = "#FFFFFF" if i % 2 == 0 else TEAL_LIGHT
        add_rect(root, 80, y, 640, 18, bg, rx=0, stroke="#E5E7EB", sw=0.5)
        add_text(root, 170, y + 13, param, 9, TEXT_DARK)
        add_text(root, 400, y + 13, pac, 9, PRIMARY_DARK, weight="bold")
        add_text(root, 600, y + 13, atl, 9, OCEAN_BLUE, weight="bold")

    return root


# ════════════════════════════════════════════════════════════════════════════
#  LESSON 6 — Индийский и Северный Ледовитый океаны
# ════════════════════════════════════════════════════════════════════════════
def lesson6():
    root = svg_root()
    header_banner(root, "Индийский и Северный Ледовитый океаны", "Особенности, характерные черты")
    footer(root, 6)

    add_rect(root, 0, 76, W, H - 106, TEAL_LIGHT, opacity=0.4)

    # ── Indian Ocean (left) ─────────────────────────────────────────────
    add_text(root, 200, 98, "Индийский океан", 15, PRIMARY_DARK, weight="bold")

    # Ocean shape
    add_ellipse(root, 200, 240, 130, 100, "#0EA5E9", "#0284C7", 2)

    # Warm currents
    add_path(root, "M 180,180 Q 150,220 170,270", "none", "#DC2626", 2)
    add_text(root, 120, 220, "Муссонное\nтечение", 6, "#DC2626", anchor="end")

    # Monsoon winds
    add_path(root, "M 240,180 Q 270,220 250,270", "none", "#F59E0B", 2)
    add_text(root, 280, 220, "Муссон", 6, "#F59E0B", anchor="start")

    # Key features
    indian_facts = [
        "Площадь: 76,2 млн км²",
        "Средняя глубина: 3 711 м",
        "Наибольшая глубина: 7 729 м",
        "Самый тёплый океан",
        "Муссонный климат",
        "Омывает: Африку, Азию,",
        "Австралию, Антарктиду",
    ]
    for i, f in enumerate(indian_facts):
        add_text(root, 200, 360 + i * 14, f, 10, TEXT_MED)

    # Feature box
    add_rect(root, 50, 345, 300, 22, "#FFFFFF", rx=3, stroke=PRIMARY, sw=1)
    add_rect(root, 50, 345, 4, 22, PRIMARY, rx=2)
    add_text(root, 62, 360, "Тёплый муссонный океан", 10, PRIMARY, anchor="start", weight="bold")

    # Resources
    add_text(root, 200, 468, "Ресурсы:", 10, PRIMARY_DARK, weight="bold")
    resources = ["Нефть (Персидский залив)", "Рыболовство", "Жемчуг, кораллы"]
    for i, r in enumerate(resources):
        add_text(root, 200, 484 + i * 14, r, 9, TEXT_MED)

    # ── Arctic Ocean (right) ────────────────────────────────────────────
    add_text(root, 600, 98, "Северный Ледовитый океан", 14, PRIMARY_DARK, weight="bold")

    # Ocean shape (smaller, round)
    add_ellipse(root, 600, 240, 110, 90, "#BAE6FD", "#0284C7", 2)

    # Ice representation
    add_ellipse(root, 600, 230, 60, 40, "#FFFFFF", "#BAE6FD", 1)
    add_text(root, 600, 233, "Лёд", 9, "#0284C7", weight="bold")

    # Northern Sea Route
    add_path(root, "M 520,200 Q 580,190 640,200 Q 680,210 700,240", "none", "#DC2626", 2)
    add_text(root, 660, 195, "Северный", 7, "#DC2626")
    add_text(root, 660, 207, "морской путь", 7, "#DC2626")

    # Key features
    arctic_facts = [
        "Площадь: 14,8 млн км²",
        "Средняя глубина: 1 225 м",
        "Наибольшая глубина: 5 527 м",
        "Самый маленький океан",
        "Самый холодный океан",
        "Покрыт льдом большую часть года",
        "Омывает: Евразию, Сев. Америку",
    ]
    for i, f in enumerate(arctic_facts):
        add_text(root, 600, 360 + i * 14, f, 10, TEXT_MED)

    # Feature box
    add_rect(root, 450, 345, 300, 22, "#FFFFFF", rx=3, stroke=ICE_BLUE, sw=1)
    add_rect(root, 450, 345, 4, 22, "#0284C7", rx=2)
    add_text(root, 462, 360, "Холодный ледовитый океан", 10, "#0284C7", anchor="start", weight="bold")

    # Resources
    add_text(root, 600, 468, "Ресурсы:", 10, PRIMARY_DARK, weight="bold")
    arctic_res = ["Нефть и газ (шельф)", "Рыболовство", "Морской транспорт"]
    for i, r in enumerate(arctic_res):
        add_text(root, 600, 484 + i * 14, r, 9, TEXT_MED)

    # ── Bottom: Comparison ──────────────────────────────────────────────
    add_text(root, W // 2, 530, "Сравнение океанов", 13, PRIMARY_DARK, weight="bold")
    add_line(root, 80, 534, W - 80, 534, PRIMARY_LITE, 1)

    # Table
    add_rect(root, 80, 542, 640, 18, PRIMARY, rx=3)
    add_text(root, 170, 555, "Показатель", 9, "#FFFFFF", weight="bold")
    add_text(root, 400, 555, "Индийский", 9, "#FFFFFF", weight="bold")
    add_text(root, 600, 555, "Северный Ледовитый", 9, "#FFFFFF", weight="bold")

    rows = [
        ("Площадь", "76,2 млн км²", "14,8 млн км²"),
        ("Температура", "самый тёплый", "самый холодный"),
        ("Ледовитость", "минимальная", "максимальная"),
    ]
    for i, (param, ind, arc) in enumerate(rows):
        y = 562 + i * 16
        bg = "#FFFFFF" if i % 2 == 0 else TEAL_LIGHT
        add_rect(root, 80, y, 640, 16, bg, stroke="#E5E7EB", sw=0.5)
        add_text(root, 170, y + 12, param, 8, TEXT_DARK)
        add_text(root, 400, y + 12, ind, 8, PRIMARY_DARK, weight="bold")
        add_text(root, 600, y + 12, arc, 8, "#0284C7", weight="bold")

    return root


# ════════════════════════════════════════════════════════════════════════════
#  LESSON 7 — Географическое положение и рельеф Африки
# ════════════════════════════════════════════════════════════════════════════
def lesson7():
    root = svg_root()
    header_banner(root, "Географическое положение и рельеф Африки", "Экватор, нагорья, форма материка")
    footer(root, 7)

    add_rect(root, 0, 76, W, H - 106, TEAL_LIGHT, opacity=0.4)

    # ── Left: Map of Africa ─────────────────────────────────────────────
    add_text(root, 220, 98, "Африка на карте мира", 14, PRIMARY_DARK, weight="bold")

    # Simplified Africa shape (pentagonal/irregular)
    africa_points = [
        (180, 120), (220, 110), (260, 115), (280, 130), (290, 155),
        (285, 185), (275, 210), (270, 240), (280, 270), (275, 300),
        (265, 330), (250, 355), (235, 370), (215, 365), (200, 345),
        (190, 320), (180, 290), (175, 260), (170, 230), (168, 200),
        (165, 170), (170, 140)
    ]
    add_polygon(root, africa_points, "#D1FAE5", PRIMARY, 2)

    # Equator line
    eq_y = 245  # approximate equator position
    add_line(root, 140, eq_y, 300, eq_y, "#DC2626", 2, dash="6,3")
    add_text(root, 310, eq_y + 4, "Экватор (0°)", 9, "#DC2626", anchor="start", weight="bold")

    # Tropic of Cancer
    tc_y = 170
    add_line(root, 160, tc_y, 290, tc_y, "#F59E0B", 1, dash="4,3")
    add_text(root, 310, tc_y + 4, "Тропик Рака (23,5° с.ш.)", 7, "#F59E0B", anchor="start")

    # Tropic of Capricorn
    tk_y = 320
    add_line(root, 165, tk_y, 285, tk_y, "#F59E0B", 1, dash="4,3")
    add_text(root, 310, tk_y + 4, "Тропик Козерога (23,5° ю.ш.)", 7, "#F59E0B", anchor="start")

    # Prime Meridian
    add_line(root, 220, 115, 220, 375, "#6D28D9", 1, dash="3,2")
    add_text(root, 220, 385, "0° (Гринвич)", 7, "#6D28D9")

    # Key geographic points
    # Cape Agulhas (southernmost point)
    add_circle(root, 235, 370, 3, "#DC2626")
    add_text(root, 145, 385, "Игольный мысе", 7, "#DC2626", anchor="start")
    add_text(root, 145, 395, "(34° ю.ш. — крайняя ю. точка)", 6, TEXT_MED, anchor="start")

    # Cape Ras Ben Sakka (northernmost)
    add_circle(root, 280, 120, 3, "#DC2626")
    add_text(root, 310, 125, "Рас-Энгела", 7, "#DC2626", anchor="start")
    add_text(root, 310, 135, "(37° с.ш. — крайняя с. точка)", 6, TEXT_MED, anchor="start")

    # Oceans
    add_text(root, 130, 230, "Атл.", 7, OCEAN_BLUE)
    add_text(root, 290, 230, "Инд.", 7, OCEAN_BLUE)

    # Geographic info
    geo_info = [
        "Пересекается экватором",
        "Расположена в Сев. и Юж. полушариях",
        "Омывается Атлантическим и",
        "Индийским океанами",
        "Площадь: 30,3 млн км²",
        "2-й по величине материк",
    ]
    for i, info in enumerate(geo_info):
        add_text(root, 220, 415 + i * 14, info, 9, TEXT_MED)

    # ── Right: Relief of Africa ─────────────────────────────────────────
    add_text(root, 600, 98, "Рельеф Африки", 14, PRIMARY_DARK, weight="bold")

    # Profile/cross-section
    profile_x = 420
    profile_y = 120
    profile_w = 340
    profile_h = 140

    # Background
    add_rect(root, profile_x, profile_y, profile_w, profile_h, "#F0FDF4", rx=4, stroke=PRIMARY_LITE, sw=1)

    # Elevation profile (simplified)
    add_path(root, f"M {profile_x+10},{profile_y+profile_h-20} "
              f"L {profile_x+40},{profile_y+profile_h-40} "
              f"L {profile_x+80},{profile_y+profile_h-70} "
              f"L {profile_x+120},{profile_y+profile_h-90} "
              f"L {profile_x+160},{profile_y+profile_h-60} "
              f"L {profile_x+200},{profile_y+profile_h-80} "
              f"L {profile_x+240},{profile_y+profile_h-50} "
              f"L {profile_x+280},{profile_y+profile_h-35} "
              f"L {profile_x+320},{profile_y+profile_h-20}",
              "#86EFAC", PRIMARY, 2)

    # Sea level line
    add_line(root, profile_x + 10, profile_y + profile_h - 15,
             profile_x + profile_w - 10, profile_y + profile_h - 15, OCEAN_BLUE, 1, dash="3,2")
    add_text(root, profile_x + profile_w - 5, profile_y + profile_h - 12, "Ур. моря", 7, OCEAN_BLUE, anchor="end")

    # Labels on profile
    add_text(root, profile_x + 120, profile_y + profile_h - 95, "Восточно-\nАфриканское\nнагорье", 7, PRIMARY_DARK, anchor="middle")

    # Key relief features
    relief_items = [
        ("Преобладает:", PRIMARY_DARK, True),
        ("  равнины высотой 200-1000 м", TEXT_MED, False),
        ("Горы:", PRIMARY_DARK, True),
        ("  Атласские (северо-запад)", TEXT_MED, False),
        ("  Драконовы (юг)", TEXT_MED, False),
        ("  Килиманджаро (5895 м)", TEXT_MED, False),
        ("Нагорья:", PRIMARY_DARK, True),
        ("  Эфиопское", TEXT_MED, False),
        ("  Восточно-Африканское", TEXT_MED, False),
        ("Впадины:", PRIMARY_DARK, True),
        ("  Калахари, Конго", TEXT_MED, False),
    ]
    for i, (text, clr, bold) in enumerate(relief_items):
        add_text(root, 440, 280 + i * 15, text, 10, clr, anchor="start", weight="bold" if bold else "normal")

    # Highest point box
    add_rect(root, 440, 440, 320, 50, "#FFFFFF", rx=4, stroke=PRIMARY, sw=2)
    add_rect(root, 440, 440, 5, 50, PRIMARY, rx=2)
    add_text(root, 460, 458, "Высшая точка: г. Килиманджаро", 11, PRIMARY, anchor="start", weight="bold")
    add_text(root, 460, 475, "5895 м — потухший вулкан в Танзании", 9, TEXT_MED, anchor="start")

    # Lowest point box
    add_rect(root, 440, 498, 320, 35, "#FFFFFF", rx=4, stroke=ACCENT_AMBER, sw=1)
    add_rect(root, 440, 498, 5, 35, ACCENT_AMBER, rx=2)
    add_text(root, 460, 515, "Низшая точка: оз. Ассаль (-155 м)", 10, ACCENT_AMBER, anchor="start", weight="bold")

    # Key feature
    add_rect(root, 440, 540, 320, 25, "#FFFFFF", rx=3, stroke="#0E7490", sw=1)
    add_rect(root, 440, 540, 4, 25, "#0E7490", rx=2)
    add_text(root, 454, 556, "Африка — самый высокий материк", 10, "#0E7490", anchor="start", weight="bold")

    return root


# ════════════════════════════════════════════════════════════════════════════
#  LESSON 8 — Природа Африки
# ════════════════════════════════════════════════════════════════════════════
def lesson8():
    root = svg_root()
    header_banner(root, "Природа Африки", "Климатические пояса, реки, природные зоны")
    footer(root, 8)

    add_rect(root, 0, 76, W, H - 106, TEAL_LIGHT, opacity=0.4)

    # ── Left: Climate zones of Africa ───────────────────────────────────
    add_text(root, 180, 98, "Климатические пояса Африки", 13, PRIMARY_DARK, weight="bold")

    # Simplified Africa with climate bands
    africa_points = [
        (160, 115), (200, 108), (240, 112), (260, 125), (270, 150),
        (265, 178), (255, 205), (250, 230), (255, 255), (250, 280),
        (242, 305), (230, 325), (218, 335), (200, 330), (188, 315),
        (178, 293), (170, 265), (165, 240), (160, 215), (158, 188),
        (155, 160), (158, 135)
    ]

    # Climate bands as horizontal stripes
    # Equatorial (green)
    add_rect(root, 150, 195, 120, 30, "#22C55E", opacity=0.6)
    # Subequatorial (light green)
    add_rect(root, 148, 165, 125, 28, "#86EFAC", opacity=0.5)
    add_rect(root, 155, 228, 110, 28, "#86EFAC", opacity=0.5)
    # Tropical (yellow)
    add_rect(root, 155, 135, 115, 28, "#FDE68A", opacity=0.5)
    add_rect(root, 165, 258, 100, 28, "#FDE68A", opacity=0.5)
    # Subtropical (orange)
    add_rect(root, 160, 115, 110, 20, "#FDBA74", opacity=0.5)
    add_rect(root, 195, 305, 60, 25, "#FDBA74", opacity=0.5)

    # Africa outline on top
    add_polygon(root, africa_points, "none", PRIMARY, 2)

    # Climate labels inside
    add_text(root, 210, 128, "Субтроп.", 7, "#92400E")
    add_text(root, 210, 150, "Тропический", 7, "#92400E")
    add_text(root, 210, 180, "Субэкв.", 7, "#065F46")
    add_text(root, 210, 213, "Экваториальный", 7, "#065F46", weight="bold")
    add_text(root, 210, 244, "Субэкв.", 7, "#065F46")
    add_text(root, 210, 273, "Тропический", 7, "#92400E")
    add_text(root, 225, 320, "Субтроп.", 6, "#92400E")

    # Legend
    legend_items = [
        ("Экваториальный", "#22C55E"),
        ("Субэкваториальный", "#86EFAC"),
        ("Тропический", "#FDE68A"),
        ("Субтропический", "#FDBA74"),
    ]
    for i, (name, clr) in enumerate(legend_items):
        add_rect(root, 40, 350 + i * 18, 14, 14, clr, rx=2, stroke=PRIMARY, sw=0.5)
        add_text(root, 60, 361 + i * 18, name, 9, TEXT_DARK, anchor="start")

    # ── Right top: Rivers of Africa ─────────────────────────────────────
    add_text(root, 580, 98, "Крупнейшие реки", 13, PRIMARY_DARK, weight="bold")

    rivers = [
        ("Нил", "6 671 км", "Самая длинная река\nмира. Исток — оз. Виктория", OCEAN_BLUE),
        ("Конго", "4 700 км", "Самая полноводная\nрека Африки", "#0E7490"),
        ("Нигер", "4 180 км", "Западная Африка,\nважнейшая транспортная", "#075985"),
        ("Замбези", "2 660 км", "Водопад Виктория —\nодин из крупнейших", PRIMARY),
    ]
    for i, (name, length, desc, clr) in enumerate(rivers):
        y = 112 + i * 52
        add_rect(root, 420, y, 340, 48, "#FFFFFF", rx=4, stroke=clr, sw=1)
        add_rect(root, 420, y, 4, 48, clr, rx=2)
        add_text(root, 436, y + 16, name, 12, clr, anchor="start", weight="bold")
        add_text(root, 530, y + 16, length, 11, PRIMARY_DARK, anchor="start", weight="bold")
        for j, ln in enumerate(desc.split("\n")):
            add_text(root, 436, y + 30 + j * 12, ln, 8, TEXT_MED, anchor="start")

    # ── Bottom: Natural zones ───────────────────────────────────────────
    add_text(root, W // 2, 330, "Природные зоны Африки", 14, PRIMARY_DARK, weight="bold")
    add_line(root, 80, 334, W - 80, 334, PRIMARY_LITE, 1)

    zones = [
        ("Влажные экваториальные леса", "#22C55E", [
            "Осадки: 2000+ мм/год",
            "Темп.: +24...+28 °C",
            "Обезьяны, окапи, шимпанзе",
        ]),
        ("Саванны", "#FDE68A", [
            "Осадки: 500-1500 мм/год",
            "Темп.: +20...+30 °C",
            "Львы, жирафы, слоны",
        ]),
        ("Пустыни", "#FDBA74", [
            "Осадки: менее 250 мм/год",
            "Темп.: до +50 °C днём",
            "Верблюды, скорпионы",
        ]),
        ("Жёстколистные леса", "#86EFAC", [
            "Осадки: 400-700 мм/год",
            "Темп.: +12...+25 °C",
            "Кустарники, дуб, сосна",
        ]),
    ]
    for i, (name, clr, facts) in enumerate(zones):
        x = 25 + i * 193
        add_rect(root, x, 345, 183, 140, "#FFFFFF", rx=5, stroke=clr, sw=2)
        add_rect(root, x, 345, 183, 24, clr, rx=5)
        add_rect(root, x, 365, 183, 4, clr)
        add_text(root, x + 91, 360, name, 9, "#FFFFFF" if clr == "#22C55E" else TEXT_DARK, weight="bold")

        for j, fact in enumerate(facts):
            add_text(root, x + 12, 383 + j * 16, fact, 9, TEXT_MED, anchor="start")

    # Wildlife icons (simplified text)
    add_text(root, W // 2, 508, "Животный мир Африки", 12, PRIMARY_DARK, weight="bold")

    wildlife = [
        "Саванны: львы, жирафы, зебры, слоны, носороги, антилопы",
        "Леса: гориллы, шимпанзе, окапи, попугаи, леопарды",
        "Пустыни: верблюды, фенеки, вараны, скорпионы, змеи",
    ]
    for i, wl in enumerate(wildlife):
        add_text(root, W // 2, 528 + i * 16, wl, 9, TEXT_MED)

    # Lake Victoria note
    add_rect(root, 60, 570, 680, 22, "#FFFFFF", rx=3, stroke=OCEAN_BLUE, sw=1)
    add_rect(root, 60, 570, 4, 22, OCEAN_BLUE, rx=2)
    add_text(root, 74, 585, "Крупнейшие озёра: Виктория (68 тыс. км²), Танганьика, Ньяса — древние тектонические озёра", 9, TEXT_MED, anchor="start")

    return root


# ════════════════════════════════════════════════════════════════════════════
#  MAIN — generate all 8 lessons and validate
# ════════════════════════════════════════════════════════════════════════════

def save_svg(root, filepath):
    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(filepath, encoding="unicode", xml_declaration=True)


def validate_svg(filepath):
    """Validate SVG is well-formed XML using ElementTree."""
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        # Basic SVG checks
        assert root.tag == "{http://www.w3.org/2000/svg}svg" or root.tag == "svg", f"Root is not <svg>: {root.tag}"
        assert root.get("width") == "800", f"Width is not 800: {root.get('width')}"
        assert root.get("height") == "600", f"Height is not 600: {root.get('height')}"
        return True, "OK"
    except ET.ParseError as e:
        return False, f"Parse error: {e}"
    except AssertionError as e:
        return False, f"Validation error: {e}"
    except Exception as e:
        return False, f"Error: {e}"


if __name__ == "__main__":
    lessons = [
        (1, "Литосфера и рельеф Земли", lesson1),
        (2, "Атмосфера и климаты Земли", lesson2),
        (3, "Численность и размещение населения", lesson3),
        (4, "Народы и религии мира", lesson4),
        (5, "Тихий и Атлантический океаны", lesson5),
        (6, "Индийский и Северный Ледовитый океаны", lesson6),
        (7, "Географическое положение и рельеф Африки", lesson7),
        (8, "Природа Африки", lesson8),
    ]

    print("=" * 60)
    print("Generating Grade 7 Geography SVGs")
    print("=" * 60)

    generated = 0
    validated = 0

    for num, title, func in lessons:
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
        print(f"\n  Lesson {num}: {title}")
        print(f"  Generating: {filepath}")

        try:
            root = func()
            save_svg(root, filepath)
            generated += 1
            print(f"  ✓ Generated successfully")

            # Validate
            ok, msg = validate_svg(filepath)
            if ok:
                validated += 1
                print(f"  ✓ Validated: {msg}")
            else:
                print(f"  ✗ Validation FAILED: {msg}")

        except Exception as e:
            print(f"  ✗ ERROR: {e}")

    print("\n" + "=" * 60)
    print(f"Results: {generated}/8 generated, {validated}/8 validated")
    print("=" * 60)

    if generated == 8 and validated == 8:
        print("\n✓ All SVG files generated and validated successfully!")
    else:
        print("\n✗ Some files failed. Check errors above.")
