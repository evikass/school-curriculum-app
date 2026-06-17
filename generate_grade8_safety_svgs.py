#!/usr/bin/env python3
"""Generate Grade 8 Safety/Life Safety (ОБЖ) SVG images for lessons 1-12."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/safety"
WIDTH = 800
HEIGHT = 600

# Colors
ORANGE = "#EA580C"
RED = "#DC2626"
DARK_RED = "#991B1B"
GREEN = "#16A34A"
DARK_GREEN = "#166534"
BLUE = "#2563EB"
YELLOW = "#EAB308"
WHITE = "#FFFFFF"
LIGHT_GRAY = "#F3F4F6"
GRAY = "#9CA3AF"
DARK_GRAY = "#374151"
BLACK = "#111827"
AMBER = "#F59E0B"
LIGHT_ORANGE = "#FFF7ED"
LIGHT_RED = "#FEF2F2"
LIGHT_GREEN = "#F0FDF4"
LIGHT_BLUE = "#EFF6FF"
LIGHT_YELLOW = "#FEFCE8"


def escape(text):
    """Escape special XML characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def svg_root():
    """Create base SVG element."""
    svg = ET.Element("svg")
    svg.set("xmlns", "http://www.w3.org/2000/svg")
    svg.set("width", str(WIDTH))
    svg.set("height", str(HEIGHT))
    svg.set("viewBox", f"0 0 {WIDTH} {HEIGHT}")
    return svg


def add_def(svg):
    """Add defs with gradients and filters."""
    defs = ET.SubElement(svg, "defs")
    # Header gradient
    grad = ET.SubElement(defs, "linearGradient")
    grad.set("id", "headerGrad")
    grad.set("x1", "0%")
    grad.set("y1", "0%")
    grad.set("x2", "100%")
    grad.set("y2", "100%")
    stop1 = ET.SubElement(grad, "stop")
    stop1.set("offset", "0%")
    stop1.set("style", f"stop-color:{ORANGE}")
    stop2 = ET.SubElement(grad, "stop")
    stop2.set("offset", "100%")
    stop2.set("style", f"stop-color:{RED}")
    # Shadow filter
    filt = ET.SubElement(defs, "filter")
    filt.set("id", "shadow")
    filt.set("x", "-5%")
    filt.set("y", "-5%")
    filt.set("width", "110%")
    filt.set("height", "110%")
    off = ET.SubElement(filt, "feDropShadow")
    off.set("dx", "1")
    off.set("dy", "2")
    off.set("stdDeviation", "2")
    off.set("flood-color", "#00000030")
    # Danger gradient
    grad2 = ET.SubElement(defs, "linearGradient")
    grad2.set("id", "dangerGrad")
    grad2.set("x1", "0%")
    grad2.set("y1", "0%")
    grad2.set("x2", "100%")
    grad2.set("y2", "100%")
    stop1 = ET.SubElement(grad2, "stop")
    stop1.set("offset", "0%")
    stop1.set("style", f"stop-color:{RED}")
    stop2 = ET.SubElement(grad2, "stop")
    stop2.set("offset", "100%")
    stop2.set("style", f"stop-color:{DARK_RED}")
    return defs


def add_background(svg):
    """Add background rectangle."""
    bg = ET.SubElement(svg, "rect")
    bg.set("width", str(WIDTH))
    bg.set("height", str(HEIGHT))
    bg.set("fill", LIGHT_GRAY)
    return bg


def add_header(svg, title, subtitle=""):
    """Add header bar with title."""
    # Header background
    header_bg = ET.SubElement(svg, "rect")
    header_bg.set("width", str(WIDTH))
    header_bg.set("height", "70")
    header_bg.set("fill", "url(#headerGrad)")
    # Title
    t = ET.SubElement(svg, "text")
    t.set("x", str(WIDTH // 2))
    t.set("y", "35")
    t.set("text-anchor", "middle")
    t.set("fill", WHITE)
    t.set("font-size", "22")
    t.set("font-weight", "bold")
    t.set("font-family", "Arial, sans-serif")
    t.text = escape(title)
    # Subtitle
    if subtitle:
        s = ET.SubElement(svg, "text")
        s.set("x", str(WIDTH // 2))
        s.set("y", "58")
        s.set("text-anchor", "middle")
        s.set("fill", "#FEE2E2")
        s.set("font-size", "13")
        s.set("font-family", "Arial, sans-serif")
        s.text = escape(subtitle)
    # Lesson number badge
    badge = ET.SubElement(svg, "rect")
    badge.set("x", "10")
    badge.set("y", "8")
    badge.set("width", "50")
    badge.set("height", "24")
    badge.set("rx", "12")
    badge.set("fill", WHITE)
    badge.set("fill-opacity", "0.3")
    badge_text = ET.SubElement(svg, "text")
    badge_text.set("x", "35")
    badge_text.set("y", "25")
    badge_text.set("text-anchor", "middle")
    badge_text.set("fill", WHITE)
    badge_text.set("font-size", "12")
    badge_text.set("font-weight", "bold")
    badge_text.set("font-family", "Arial, sans-serif")
    badge_text.text = "ОБЖ"
    # Bottom border line
    line = ET.SubElement(svg, "rect")
    line.set("x", "0")
    line.set("y", "70")
    line.set("width", str(WIDTH))
    line.set("height", "3")
    line.set("fill", YELLOW)


def add_warning_icon(svg, x, y, size=20):
    """Add a warning triangle icon."""
    g = ET.SubElement(svg, "g")
    g.set("transform", f"translate({x},{y})")
    # Triangle
    pts = f"{size//2},0 {size},{size} 0,{size}"
    poly = ET.SubElement(g, "polygon")
    poly.set("points", pts)
    poly.set("fill", YELLOW)
    poly.set("stroke", DARK_GRAY)
    poly.set("stroke-width", "1")
    # Exclamation mark
    t = ET.SubElement(g, "text")
    t.set("x", str(size // 2))
    t.set("y", str(size - 4))
    t.set("text-anchor", "middle")
    t.set("fill", BLACK)
    t.set("font-size", str(size // 2))
    t.set("font-weight", "bold")
    t.set("font-family", "Arial, sans-serif")
    t.text = "!"
    return g


def add_danger_icon(svg, x, y, size=20):
    """Add a danger/X icon (red circle with X)."""
    g = ET.SubElement(svg, "g")
    c = ET.SubElement(g, "circle")
    c.set("cx", str(x + size // 2))
    c.set("cy", str(y + size // 2))
    c.set("r", str(size // 2))
    c.set("fill", RED)
    # X mark
    t = ET.SubElement(g, "text")
    t.set("x", str(x + size // 2))
    t.set("y", str(y + size // 2 + 5))
    t.set("text-anchor", "middle")
    t.set("fill", WHITE)
    t.set("font-size", str(size - 4))
    t.set("font-weight", "bold")
    t.set("font-family", "Arial, sans-serif")
    t.text = "X"
    return g


def add_check_icon(svg, x, y, size=20):
    """Add a check/green circle icon."""
    g = ET.SubElement(svg, "g")
    c = ET.SubElement(g, "circle")
    c.set("cx", str(x + size // 2))
    c.set("cy", str(y + size // 2))
    c.set("r", str(size // 2))
    c.set("fill", GREEN)
    # Check mark
    t = ET.SubElement(g, "text")
    t.set("x", str(x + size // 2))
    t.set("y", str(y + size // 2 + 5))
    t.set("text-anchor", "middle")
    t.set("fill", WHITE)
    t.set("font-size", str(size - 6))
    t.set("font-weight", "bold")
    t.set("font-family", "Arial, sans-serif")
    t.text = "+"
    return g


def add_info_box(svg, x, y, w, h, title, lines, bg_color=LIGHT_ORANGE, border_color=ORANGE, title_color=ORANGE):
    """Add an info box with title and text lines."""
    # Box
    rect = ET.SubElement(svg, "rect")
    rect.set("x", str(x))
    rect.set("y", str(y))
    rect.set("width", str(w))
    rect.set("height", str(h))
    rect.set("rx", "8")
    rect.set("fill", bg_color)
    rect.set("stroke", border_color)
    rect.set("stroke-width", "2")
    rect.set("filter", "url(#shadow)")
    # Title
    t = ET.SubElement(svg, "text")
    t.set("x", str(x + 10))
    t.set("y", str(y + 20))
    t.set("fill", title_color)
    t.set("font-size", "13")
    t.set("font-weight", "bold")
    t.set("font-family", "Arial, sans-serif")
    t.text = escape(title)
    # Lines
    for i, line in enumerate(lines):
        lt = ET.SubElement(svg, "text")
        lt.set("x", str(x + 10))
        lt.set("y", str(y + 38 + i * 17))
        lt.set("fill", DARK_GRAY)
        lt.set("font-size", "11")
        lt.set("font-family", "Arial, sans-serif")
        lt.text = escape(line)
    return rect


def add_rule_box(svg, x, y, w, lines, is_correct=True):
    """Add a rule box - green for correct, red for dangerous."""
    h = 30 + len(lines) * 16
    bg = LIGHT_GREEN if is_correct else LIGHT_RED
    border = GREEN if is_correct else RED
    icon_fn = add_check_icon if is_correct else add_danger_icon
    label = "ПРАВИЛЬНО" if is_correct else "ОПАСНО"
    
    rect = ET.SubElement(svg, "rect")
    rect.set("x", str(x))
    rect.set("y", str(y))
    rect.set("width", str(w))
    rect.set("height", str(h))
    rect.set("rx", "6")
    rect.set("fill", bg)
    rect.set("stroke", border)
    rect.set("stroke-width", "1.5")
    
    icon_fn(svg, x + 5, y + 5, 16)
    
    lt = ET.SubElement(svg, "text")
    lt.set("x", str(x + 26))
    lt.set("y", str(y + 18))
    lt.set("fill", border)
    lt.set("font-size", "11")
    lt.set("font-weight", "bold")
    lt.set("font-family", "Arial, sans-serif")
    lt.text = label
    
    for i, line in enumerate(lines):
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + 10))
        t.set("y", str(y + 34 + i * 16))
        t.set("fill", DARK_GRAY)
        t.set("font-size", "11")
        t.set("font-family", "Arial, sans-serif")
        t.text = escape(line)
    return rect


def add_step(svg, x, y, step_num, text, color=ORANGE):
    """Add a numbered step."""
    # Circle with number
    c = ET.SubElement(svg, "circle")
    c.set("cx", str(x + 12))
    c.set("cy", str(y + 12))
    c.set("r", "12")
    c.set("fill", color)
    nt = ET.SubElement(svg, "text")
    nt.set("x", str(x + 12))
    nt.set("y", str(y + 16))
    nt.set("text-anchor", "middle")
    nt.set("fill", WHITE)
    nt.set("font-size", "11")
    nt.set("font-weight", "bold")
    nt.set("font-family", "Arial, sans-serif")
    nt.text = str(step_num)
    # Step text
    st = ET.SubElement(svg, "text")
    st.set("x", str(x + 30))
    st.set("y", str(y + 16))
    st.set("fill", DARK_GRAY)
    st.set("font-size", "12")
    st.set("font-family", "Arial, sans-serif")
    st.text = escape(text)
    return c


def add_section_title(svg, x, y, text, color=ORANGE):
    """Add a section title with underline."""
    t = ET.SubElement(svg, "text")
    t.set("x", str(x))
    t.set("y", str(y))
    t.set("fill", color)
    t.set("font-size", "15")
    t.set("font-weight", "bold")
    t.set("font-family", "Arial, sans-serif")
    t.text = escape(text)
    line = ET.SubElement(svg, "line")
    line.set("x1", str(x))
    line.set("y1", str(y + 4))
    line.set("x2", str(x + len(text) * 8))
    line.set("y2", str(y + 4))
    line.set("stroke", color)
    line.set("stroke-width", "2")
    return t


def add_emergency_number(svg, x, y, number, label):
    """Add an emergency number display."""
    rect = ET.SubElement(svg, "rect")
    rect.set("x", str(x))
    rect.set("y", str(y))
    rect.set("width", "110")
    rect.set("height", "45")
    rect.set("rx", "8")
    rect.set("fill", RED)
    rect.set("filter", "url(#shadow)")
    nt = ET.SubElement(svg, "text")
    nt.set("x", str(x + 55))
    nt.set("y", str(y + 22))
    nt.set("text-anchor", "middle")
    nt.set("fill", WHITE)
    nt.set("font-size", "20")
    nt.set("font-weight", "bold")
    nt.set("font-family", "Arial, sans-serif")
    nt.text = number
    lt = ET.SubElement(svg, "text")
    lt.set("x", str(x + 55))
    lt.set("y", str(y + 38))
    lt.set("text-anchor", "middle")
    lt.set("fill", "#FEE2E2")
    lt.set("font-size", "9")
    lt.set("font-family", "Arial, sans-serif")
    lt.text = escape(label)


# ============================================================
# LESSON 1: Безопасность в квартире
# ============================================================
def generate_lesson_1():
    svg = svg_root()
    add_def(svg)
    add_background(svg)
    add_header(svg, "Безопасность в квартире", "Электричество, газ, вода — правила безопасного поведения дома")
    
    # Section: Electrical hazards
    add_section_title(svg, 20, 95, "Электробезопасность")
    add_warning_icon(svg, 160, 80)
    
    # Electrical icon - lightning bolt
    bolt = ET.SubElement(svg, "polygon")
    bolt.set("points", "220,85 230,100 225,100 232,118 218,103 223,103 215,85")
    bolt.set("fill", YELLOW)
    bolt.set("stroke", ORANGE)
    bolt.set("stroke-width", "1")
    
    add_rule_box(svg, 20, 105, 240, [
        "Не прикасайтесь к розеткам мокрыми руками",
        "Не вставляйте посторонние предметы в розетки",
        "Не перегружайте розетки множеством приборов",
        "Отключайте приборы уходя из дома"
    ], is_correct=True)
    
    add_rule_box(svg, 20, 205, 240, [
        "Тянуть за шнур при отключении",
        "Использовать повреждённые провода",
        "Оставлять включённые приборы без присмотра",
        "Самостоятельно ремонтировать электроприборы"
    ], is_correct=False)
    
    # Section: Gas safety
    add_section_title(svg, 280, 95, "Газовая безопасность")
    # Gas flame icon
    flame_g = ET.SubElement(svg, "g")
    flame_g.set("transform", "translate(420,78)")
    flame1 = ET.SubElement(flame_g, "ellipse")
    flame1.set("cx", "8")
    flame1.set("cy", "14")
    flame1.set("rx", "8")
    flame1.set("ry", "14")
    flame1.set("fill", "#FBBF24")
    flame2 = ET.SubElement(flame_g, "ellipse")
    flame2.set("cx", "8")
    flame2.set("cy", "16")
    flame2.set("rx", "5")
    flame2.set("ry", "10")
    flame2.set("fill", "#3B82F6")
    
    add_info_box(svg, 280, 105, 240, 120, "При запахе газа:", [
        "1. Не включайте свет и электроприборы",
        "2. Откройте окна и двери",
        "3. Закройте газовый кран",
        "4. Выйдите из квартиры",
        "5. Вызовите газовую службу: 04",
        "6. Не зажигайте спички и огонь"
    ], LIGHT_RED, RED, RED)
    
    # Section: Water safety
    add_section_title(svg, 540, 95, "Водная безопасность")
    # Water drop icon
    drop = ET.SubElement(svg, "path")
    drop.set("d", "M570,82 Q575,70 580,82 Q580,92 575,95 Q570,92 570,82 Z")
    drop.set("fill", BLUE)
    
    add_info_box(svg, 540, 105, 240, 95, "Правила:", [
        "Проверяйте краны перед уходом",
        "Не оставляйте воду без присмотра",
        "Знайте расположение вентилей",
        "При прорыве: отключите воду",
        "Сообщите в УК или аварииную службу"
    ], LIGHT_BLUE, BLUE, BLUE)
    
    # Emergency numbers section
    add_section_title(svg, 20, 340, "Телефоны экстренных служб")
    add_emergency_number(svg, 20, 360, "112", "Единый номер")
    add_emergency_number(svg, 145, 360, "101", "Пожарная/МЧС")
    add_emergency_number(svg, 270, 360, "104", "Газовая служба")
    add_emergency_number(svg, 395, 360, "03", "Скорая помощь")
    
    # Home safety diagram
    add_section_title(svg, 20, 430, "Схема безопасности квартиры")
    
    # Draw apartment outline
    apt = ET.SubElement(svg, "rect")
    apt.set("x", "40")
    apt.set("y", "450")
    apt.set("width", "720")
    apt.set("height", "130")
    apt.set("rx", "4")
    apt.set("fill", WHITE)
    apt.set("stroke", DARK_GRAY)
    apt.set("stroke-width", "2")
    
    # Rooms
    rooms = [
        (45, 455, 170, 55, "Кухня\n(газ, вода)", ORANGE),
        (220, 455, 170, 55, "Ванная\n(вода, электричество)", BLUE),
        (395, 455, 170, 55, "Комната\n(электроприборы)", AMBER),
        (570, 455, 185, 55, "Прихожая\n(щиток, дверь)", GREEN),
    ]
    for rx, ry, rw, rh, label, color in rooms:
        r = ET.SubElement(svg, "rect")
        r.set("x", str(rx))
        r.set("y", str(ry))
        r.set("width", str(rw))
        r.set("height", str(rh))
        r.set("rx", "3")
        r.set("fill", color)
        r.set("fill-opacity", "0.15")
        r.set("stroke", color)
        r.set("stroke-width", "1.5")
        lines = label.split("\n")
        for i, ln in enumerate(lines):
            t = ET.SubElement(svg, "text")
            t.set("x", str(rx + rw // 2))
            t.set("y", str(ry + 22 + i * 16))
            t.set("text-anchor", "middle")
            t.set("fill", color)
            t.set("font-size", "11")
            t.set("font-weight", "bold" if i == 0 else "normal")
            t.set("font-family", "Arial, sans-serif")
            t.text = escape(ln)
    
    # Key items in apartment
    items = [
        (70, 520, "⚡ Розетки"),
        (250, 520, "🔥 Плита"),
        (420, 520, "💡 Свет"),
        (600, 520, "🚪 Дверь"),
        (70, 545, "🔌 Щиток"),
        (250, 545, "🚿 Краны"),
        (420, 545, "📺 ТВ"),
        (600, 545, "🔑 Замок"),
    ]
    for ix, iy, ilabel in items:
        t = ET.SubElement(svg, "text")
        t.set("x", str(ix))
        t.set("y", str(iy))
        t.set("fill", DARK_GRAY)
        t.set("font-size", "10")
        t.set("font-family", "Arial, sans-serif")
        t.text = escape(ilabel)
    
    return svg


# ============================================================
# LESSON 2: Безопасность при общении с незнакомцами
# ============================================================
def generate_lesson_2():
    svg = svg_root()
    add_def(svg)
    add_background(svg)
    add_header(svg, "Безопасность при общении с незнакомцами", "Правила поведения и опасные ситуации")
    
    # Main rules section
    add_section_title(svg, 20, 95, "Главные правила")
    
    rules = [
        "Никогда не уходи с незнакомым человеком",
        "Не садись в машину к незнакомцу",
        "Не открывай дверь незнакомым людям",
        "Не бери угощения от незнакомых",
        "Сообщай родителям о подозрительных людях",
        "Зови на помощь, если тебе угрожают"
    ]
    for i, rule in enumerate(rules):
        add_step(svg, 20, 108 + i * 28, i + 1, rule, ORANGE)
    
    # Dangerous situations
    add_section_title(svg, 380, 95, "Опасные ситуации")
    
    dangers = [
        ("Просьба о помощи", "Взрослый просит ребёнка о помощи — это ловушка!"),
        ("Предложение подарка", "Незнакомец предлагает конфеты, игрушки — отказывайся!"),
        ("Просьба показать дорогу", "Не ходи показывать дорогу — отправь к другим взрослым"),
        ("Сообщение о беде", "Скажи: \"Я позвоню родителям и проверю\""),
    ]
    for i, (title, desc) in enumerate(dangers):
        y_pos = 108 + i * 60
        add_danger_icon(svg, 385, y_pos, 18)
        t = ET.SubElement(svg, "text")
        t.set("x", "410")
        t.set("y", str(y_pos + 14))
        t.set("fill", RED)
        t.set("font-size", "12")
        t.set("font-weight", "bold")
        t.set("font-family", "Arial, sans-serif")
        t.text = escape(title)
        d = ET.SubElement(svg, "text")
        d.set("x", "410")
        d.set("y", str(y_pos + 30))
        d.set("fill", DARK_GRAY)
        d.set("font-size", "10")
        d.set("font-family", "Arial, sans-serif")
        d.text = escape(desc)
    
    # Correct behavior
    add_section_title(svg, 380, 360, "Правильное поведение")
    
    correct = [
        "Громко скажи: \"Я вас не знаю!\"",
        "Беги в безопасное место (магазин, школа)",
        "Звони родителям или 112",
        "Обратись к полицейскому или охраннику",
    ]
    for i, rule in enumerate(correct):
        add_step(svg, 385, 373 + i * 28, i + 1, rule, GREEN)
    
    # Safe/unsafe people diagram
    add_section_title(svg, 20, 490, "К кому можно обратиться за помощью")
    
    safe_people = [
        ("Полицейский", BLUE),
        ("Охранник магазина", GREEN),
        ("Семья с детьми", ORANGE),
        ("Учитель", AMBER),
    ]
    for i, (name, color) in enumerate(safe_people):
        x = 25 + i * 190
        # Person icon (circle head + body)
        head = ET.SubElement(svg, "circle")
        head.set("cx", str(x + 20))
        head.set("cy", str(510))
        head.set("r", "10")
        head.set("fill", color)
        body = ET.SubElement(svg, "line")
        body.set("x1", str(x + 20))
        body.set("y1", "520")
        body.set("x2", str(x + 20))
        body.set("y2", "540")
        body.set("stroke", color)
        body.set("stroke-width", "3")
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + 40))
        t.set("y", str(525))
        t.set("fill", color)
        t.set("font-size", "11")
        t.set("font-weight", "bold")
        t.set("font-family", "Arial, sans-serif")
        t.text = escape(name)
    
    # Phone reminder
    phone_box = ET.SubElement(svg, "rect")
    phone_box.set("x", "580")
    phone_box.set("y", "490")
    phone_box.set("width", "195")
    phone_box.set("height", "50")
    phone_box.set("rx", "8")
    phone_box.set("fill", RED)
    phone_box.set("filter", "url(#shadow)")
    pt = ET.SubElement(svg, "text")
    pt.set("x", "677")
    pt.set("y", "513")
    pt.set("text-anchor", "middle")
    pt.set("fill", WHITE)
    pt.set("font-size", "22")
    pt.set("font-weight", "bold")
    pt.set("font-family", "Arial, sans-serif")
    pt.text = "112"
    pt2 = ET.SubElement(svg, "text")
    pt2.set("x", "677")
    pt2.set("y", "532")
    pt2.set("text-anchor", "middle")
    pt2.set("fill", "#FEE2E2")
    pt2.set("font-size", "11")
    pt2.set("font-family", "Arial, sans-serif")
    pt2.text = "Единый номер экстренного вызова"
    
    # Password rule
    add_rule_box(svg, 20, 555, 750, [
        "Договоритесь с семьёй о \"пароле безопасности\" — если незнакомец говорит, что его прислали родители, он должен знать пароль!"
    ], is_correct=True)
    
    return svg


# ============================================================
# LESSON 3: Причины пожаров и их профилактика
# ============================================================
def generate_lesson_3():
    svg = svg_root()
    add_def(svg)
    add_background(svg)
    add_header(svg, "Причины пожаров и их профилактика", "Правила пожарной безопасности")
    
    # Fire causes
    add_section_title(svg, 20, 95, "Основные причины пожаров")
    
    causes = [
        ("Неосторожное обращение с огнём", "40%", RED),
        ("Нарушение правил эксплуатации\nэлектрооборудования", "25%", ORANGE),
        ("Детские шалости с огнём", "15%", AMBER),
        ("Нарушение правил\nпожарной безопасности", "12%", YELLOW),
        ("Поджоги", "8%", GRAY),
    ]
    
    # Simple bar chart
    bar_x = 20
    bar_y = 115
    for i, (cause, pct_str, color) in enumerate(causes):
        pct = int(pct_str.replace("%", ""))
        bar_w = pct * 3.8
        # Bar
        bar = ET.SubElement(svg, "rect")
        bar.set("x", str(bar_x))
        bar.set("y", str(bar_y + i * 40))
        bar.set("width", str(bar_w))
        bar.set("height", "28")
        bar.set("rx", "4")
        bar.set("fill", color)
        # Percentage
        pt = ET.SubElement(svg, "text")
        pt.set("x", str(bar_x + bar_w + 8))
        pt.set("y", str(bar_y + i * 40 + 20))
        pt.set("fill", color)
        pt.set("font-size", "13")
        pt.set("font-weight", "bold")
        pt.set("font-family", "Arial, sans-serif")
        pt.text = pct_str
        # Label
        lt = ET.SubElement(svg, "text")
        lt.set("x", str(bar_x + 5))
        lt.set("y", str(bar_y + i * 40 + 18))
        lt.set("fill", WHITE if color in [RED, ORANGE] else BLACK)
        lt.set("font-size", "10")
        lt.set("font-family", "Arial, sans-serif")
        lt.text = escape(cause.split("\n")[0])
    
    # Prevention rules
    add_section_title(svg, 460, 95, "Профилактика пожаров")
    
    prevention = [
        "Не играйте со спичками и зажигалками",
        "Не оставляйте включённые приборы",
        "Не курите в постели и на балконе",
        "Не перегружайте электросеть",
        "Установите дымовые датчики",
        "Храните спички в недоступном месте",
        "Не разжигайте костёр без взрослых",
        "Следите за состоянием проводки"
    ]
    for i, rule in enumerate(prevention):
        add_check_icon(svg, 465, 108 + i * 28, 14)
        t = ET.SubElement(svg, "text")
        t.set("x", "485")
        t.set("y", str(120 + i * 28))
        t.set("fill", DARK_GRAY)
        t.set("font-size", "11")
        t.set("font-family", "Arial, sans-serif")
        t.text = escape(rule)
    
    # Fire triangle
    add_section_title(svg, 20, 340, "Треугольник пожара")
    
    # Triangle
    tri_x, tri_y = 160, 370
    tri = ET.SubElement(svg, "polygon")
    tri.set("points", f"{tri_x},{tri_y} {tri_x+140},{tri_y+130} {tri_x-140},{tri_y+130}")
    tri.set("fill", LIGHT_RED)
    tri.set("stroke", RED)
    tri.set("stroke-width", "2")
    
    # Labels at vertices
    labels = [
        (tri_x, tri_y - 5, "Тепло", RED),
        (tri_x + 155, tri_y + 140, "Кислород", BLUE),
        (tri_x - 155, tri_y + 140, "Горючее\nвещество", ORANGE),
    ]
    for lx, ly, text, color in labels:
        lines = text.split("\n")
        for j, ln in enumerate(lines):
            t = ET.SubElement(svg, "text")
            t.set("x", str(lx))
            t.set("y", str(ly + j * 14))
            t.set("text-anchor", "middle")
            t.set("fill", color)
            t.set("font-size", "12")
            t.set("font-weight", "bold")
            t.set("font-family", "Arial, sans-serif")
            t.text = escape(ln)
    
    # Center text
    ct = ET.SubElement(svg, "text")
    ct.set("x", str(tri_x))
    ct.set("y", str(tri_y + 95))
    ct.set("text-anchor", "middle")
    ct.set("fill", RED)
    ct.set("font-size", "14")
    ct.set("font-weight", "bold")
    ct.set("font-family", "Arial, sans-serif")
    ct.text = "ПОЖАР"
    
    # To stop fire, remove one element
    add_info_box(svg, 20, 520, 310, 65, "Уберите один элемент:", [
        "Тепло — залейте водой",
        "Кислород — закройте доступ воздуха",
        "Горючее — уберите источник"
    ], LIGHT_YELLOW, AMBER, DARK_GRAY)
    
    # Right side: fire extinguisher info
    add_info_box(svg, 460, 370, 320, 95, "Огнетушитель:", [
        "1. Сорвите пломбу",
        "2. Направьте шланг на огонь",
        "3. Нажмите на рычаг",
        "4. Сбивайте пламя с расстояния 2-3 м"
    ], LIGHT_ORANGE, ORANGE, ORANGE)
    
    # Fire extinguisher icon
    fe = ET.SubElement(svg, "rect")
    fe.set("x", "660")
    fe.set("y", "480")
    fe.set("width", "30")
    fe.set("height", "50")
    fe.set("rx", "5")
    fe.set("fill", RED)
    fe.set("stroke", DARK_RED)
    fe.set("stroke-width", "2")
    # Handle
    handle = ET.SubElement(svg, "line")
    handle.set("x1", "675")
    handle.set("y1", "475")
    handle.set("x2", "695")
    handle.set("y2", "465")
    handle.set("stroke", DARK_GRAY)
    handle.set("stroke-width", "3")
    
    add_rule_box(svg, 460, 500, 320, [
        "Проверяйте срок годности огнетушителя",
        "Установите дымовые датчики дома"
    ], is_correct=True)
    
    return svg


# ============================================================
# LESSON 4: Действия при пожаре
# ============================================================
def generate_lesson_4():
    svg = svg_root()
    add_def(svg)
    add_background(svg)
    add_header(svg, "Действия при пожаре", "Эвакуация и вызов экстренных служб")
    
    # Step-by-step actions
    add_section_title(svg, 20, 95, "Порядок действий при пожаре")
    
    steps = [
        "Оцените обстановку и не паникуйте",
        "Вызовите пожарную охрану: 101 или 112",
        "Предупредите окружающих о пожаре",
        "Попробуйте потушить огонь (если безопасно)",
        "Эвакуируйтесь по плану эвакуации",
        "Не пользуйтесь лифтом!",
        "Прикройте нос и рот влажной тканью",
        "Двигайтесь пригнувшись или ползком",
        "Не возвращайтесь в горящее помещение"
    ]
    for i, step in enumerate(steps):
        color = RED if "лифтом" in step.lower() else (GREEN if "вызовите" in step.lower() else ORANGE)
        add_step(svg, 20, 110 + i * 28, i + 1, step, color)
    
    # Emergency call template
    add_section_title(svg, 420, 95, "Как звонить в 101/112")
    
    call_box = ET.SubElement(svg, "rect")
    call_box.set("x", "425")
    call_box.set("y", "108")
    call_box.set("width", "350")
    call_box.set("height", "145")
    call_box.set("rx", "8")
    call_box.set("fill", WHITE)
    call_box.set("stroke", RED)
    call_box.set("stroke-width", "2")
    call_box.set("filter", "url(#shadow)")
    
    call_steps = [
        "Назовите: ЧТО горит",
        "Назовите: АДРЕС (улица, дом, квартира)",
        "Назовите: ЕСТЬ ЛИ люди в опасности",
        "Назовите: СВОЁ ИМЯ и фамилию",
        "Ответьте на вопросы диспетчера",
        "Не вешайте трубку первыми!"
    ]
    for i, step in enumerate(call_steps):
        icon = "!" if i < 4 else "+"
        add_warning_icon(svg, 435, 118 + i * 22, 16)
        t = ET.SubElement(svg, "text")
        t.set("x", "458")
        t.set("y", str(130 + i * 22))
        t.set("fill", DARK_GRAY)
        t.set("font-size", "11")
        t.set("font-family", "Arial, sans-serif")
        t.text = escape(step)
    
    # Smoke behavior
    add_section_title(svg, 420, 270, "Если путь в дыму")
    
    add_info_box(svg, 425, 283, 350, 120, "Правила движения в дыму:", [
        "1. Смочите ткань водой и прикройте рот и нос",
        "2. Двигайтесь пригнувшись или ползком",
        "3. Держитесь за стены для ориентации",
        "4. Двигайтесь к выходу против ветра",
        "5. Если одежда загорелась — упадите и катитесь",
        "6. Не прячьтесь под кровать или в шкаф!"
    ], LIGHT_RED, RED, RED)
    
    # Evacuation plan
    add_section_title(svg, 20, 390, "План эвакуации")
    
    # Building diagram
    bldg = ET.SubElement(svg, "rect")
    bldg.set("x", "30")
    bldg.set("y", "410")
    bldg.set("width", "360")
    bldg.set("height", "170")
    bldg.set("rx", "4")
    bldg.set("fill", WHITE)
    bldg.set("stroke", DARK_GRAY)
    bldg.set("stroke-width", "2")
    
    # Floors
    floor_labels = ["3 этаж", "2 этаж", "1 этаж"]
    floor_colors = [RED, ORANGE, GREEN]
    for i, (fl, fc) in enumerate(zip(floor_labels, floor_colors)):
        fy = 415 + i * 55
        # Floor background
        fr = ET.SubElement(svg, "rect")
        fr.set("x", "35")
        fr.set("y", str(fy))
        fr.set("width", "350")
        fr.set("height", "50")
        fr.set("rx", "3")
        fr.set("fill", fc)
        fr.set("fill-opacity", "0.1")
        fr.set("stroke", fc)
        fr.set("stroke-width", "1")
        # Floor label
        flt = ET.SubElement(svg, "text")
        flt.set("x", "45")
        flt.set("y", str(fy + 30))
        flt.set("fill", fc)
        flt.set("font-size", "11")
        flt.set("font-weight", "bold")
        flt.set("font-family", "Arial, sans-serif")
        flt.text = escape(fl)
        # Arrow pointing to exit
        arrow_x = 200
        arrow = ET.SubElement(svg, "text")
        arrow.set("x", str(arrow_x))
        arrow.set("y", str(fy + 30))
        arrow.set("fill", fc)
        arrow.set("font-size", "16")
        arrow.set("font-family", "Arial, sans-serif")
        arrow.text = ">>> ВЫХОД"
    
    # Exit sign
    exit_rect = ET.SubElement(svg, "rect")
    exit_rect.set("x", "320")
    exit_rect.set("y", "520")
    exit_rect.set("width", "60")
    exit_rect.set("height", "25")
    exit_rect.set("rx", "4")
    exit_rect.set("fill", GREEN)
    exit_t = ET.SubElement(svg, "text")
    exit_t.set("x", "350")
    exit_t.set("y", "537")
    exit_t.set("text-anchor", "middle")
    exit_t.set("fill", WHITE)
    exit_t.set("font-size", "10")
    exit_t.set("font-weight", "bold")
    exit_t.set("font-family", "Arial, sans-serif")
    exit_t.text = "ВЫХОД"
    
    # Rules on right side
    add_rule_box(svg, 420, 420, 350, [
        "Используйте лестницу, НЕ ЛИФТ",
        "Не берите вещи — спасайте жизнь!",
        "Не открывайте горящую дверь настежь"
    ], is_correct=False)
    
    add_rule_box(svg, 420, 510, 350, [
        "Предупредите соседей",
        "Помогите детям и пожилым",
        "Встретьте пожарных и укажите путь"
    ], is_correct=True)
    
    return svg


# ============================================================
# LESSON 5: Правила дорожного движения для пешеходов
# ============================================================
def generate_lesson_5():
    svg = svg_root()
    add_def(svg)
    add_background(svg)
    add_header(svg, "Правила дорожного движения для пешеходов", "Знаки, переходы и безопасное поведение")
    
    # Traffic signs section
    add_section_title(svg, 20, 95, "Важные дорожные знаки")
    
    signs = [
        (80, 130, 25, BLUE, WHITE, "Пешеходный\nпереход", "5.19.1"),
        (210, 130, 25, RED, WHITE, "Движение\nпешеходов\nзапрещено", "3.10"),
        (340, 130, 25, BLUE, WHITE, "Подземный\nпереход", "6.6"),
        (470, 130, 25, BLUE, WHITE, "Надземный\nпереход", "6.7"),
        (600, 130, 25, YELLOW, BLACK, "Осторожно\nдети!", "1.23"),
    ]
    
    for sx, sy, sr, bg_color, fg_color, label, sign_num in signs:
        # Sign circle
        sc = ET.SubElement(svg, "circle")
        sc.set("cx", str(sx))
        sc.set("cy", str(sy))
        sc.set("r", str(sr))
        sc.set("fill", bg_color)
        sc.set("stroke", DARK_GRAY)
        sc.set("stroke-width", "2")
        # Sign number
        nt = ET.SubElement(svg, "text")
        nt.set("x", str(sx))
        nt.set("y", str(sy + 4))
        nt.set("text-anchor", "middle")
        nt.set("fill", fg_color)
        nt.set("font-size", "9")
        nt.set("font-weight", "bold")
        nt.set("font-family", "Arial, sans-serif")
        nt.text = sign_num
        # Label
        lines = label.split("\n")
        for j, ln in enumerate(lines):
            lt = ET.SubElement(svg, "text")
            lt.set("x", str(sx))
            lt.set("y", str(sy + sr + 15 + j * 12))
            lt.set("text-anchor", "middle")
            lt.set("fill", DARK_GRAY)
            lt.set("font-size", "9")
            lt.set("font-family", "Arial, sans-serif")
            lt.text = escape(ln)
    
    # Pedestrian crossing rules
    add_section_title(svg, 20, 215, "Правила перехода дороги")
    
    crossing_steps = [
        "Подойдите к краю тротуара",
        "Посмотрите НАЛЕВО",
        "Посмотрите НАПРАВО",
        "Ещё раз посмотрите НАЛЕВО",
        "Убедитесь, что транспорт остановился",
        "Переходите дорогу спокойным шагом",
        "Не играйте и не бегите на переходе"
    ]
    for i, step in enumerate(crossing_steps):
        color = BLUE if "НАЛЕВО" in step else (ORANGE if "НАПРАВО" in step else DARK_GRAY)
        add_step(svg, 20, 230 + i * 25, i + 1, step, ORANGE if i < 6 else RED)
    
    # Road diagram
    add_section_title(svg, 420, 215, "Схема перехода")
    
    # Road
    road = ET.SubElement(svg, "rect")
    road.set("x", "430")
    road.set("y", "240")
    road.set("width", "350")
    road.set("height", "200")
    road.set("fill", "#374151")
    
    # Road markings
    for i in range(6):
        dash = ET.SubElement(svg, "rect")
        dash.set("x", str(445 + i * 55))
        dash.set("y", "337")
        dash.set("width", "30")
        dash.set("height", "4")
        dash.set("fill", WHITE)
    
    # Sidewalks
    sw1 = ET.SubElement(svg, "rect")
    sw1.set("x", "430")
    sw1.set("y", "230")
    sw1.set("width", "350")
    sw1.set("height", "15")
    sw1.set("fill", "#9CA3AF")
    sw2 = ET.SubElement(svg, "rect")
    sw2.set("x", "430")
    sw2.set("y", "435")
    sw2.set("width", "350")
    sw2.set("height", "15")
    sw2.set("fill", "#9CA3AF")
    
    # Zebra crossing
    for i in range(8):
        stripe = ET.SubElement(svg, "rect")
        stripe.set("x", "540")
        stripe.set("y", str(245 + i * 24))
        stripe.set("width", "50")
        stripe.set("height", "16")
        stripe.set("fill", WHITE)
    
    # Pedestrian figure
    ped = ET.SubElement(svg, "circle")
    ped.set("cx", "565")
    ped.set("cy", "260")
    ped.set("r", "8")
    ped.set("fill", GREEN)
    # Arrow showing direction
    arrow = ET.SubElement(svg, "line")
    arrow.set("x1", "565")
    arrow.set("y1", "270")
    arrow.set("x2", "565")
    arrow.set("y2", "420")
    arrow.set("stroke", GREEN)
    arrow.set("stroke-width", "2")
    arrow.set("stroke-dasharray", "5,5")
    # Arrow head
    ah = ET.SubElement(svg, "polygon")
    ah.set("points", "565,425 558,415 572,415")
    ah.set("fill", GREEN)
    
    # Direction labels
    lt = ET.SubElement(svg, "text")
    lt.set("x", "520")
    lt.set("y", "290")
    lt.set("fill", YELLOW)
    lt.set("font-size", "10")
    lt.set("font-weight", "bold")
    lt.set("font-family", "Arial, sans-serif")
    lt.text = "<< НАЛЕВО"
    rt = ET.SubElement(svg, "text")
    rt.set("x", "520")
    rt.set("y", "395")
    rt.set("fill", YELLOW)
    rt.set("font-size", "10")
    rt.set("font-weight", "bold")
    rt.set("font-family", "Arial, sans-serif")
    rt.text = "НАПРАВО >>"
    
    # Traffic light
    tl_bg = ET.SubElement(svg, "rect")
    tl_bg.set("x", "650")
    tl_bg.set("y", "260")
    tl_bg.set("width", "30")
    tl_bg.set("height", "80")
    tl_bg.set("rx", "6")
    tl_bg.set("fill", "#1F2937")
    tl_bg.set("stroke", DARK_GRAY)
    tl_bg.set("stroke-width", "2")
    # Red
    r_c = ET.SubElement(svg, "circle")
    r_c.set("cx", "665")
    r_c.set("cy", "278")
    r_c.set("r", "10")
    r_c.set("fill", "#991B1B")
    # Yellow
    y_c = ET.SubElement(svg, "circle")
    y_c.set("cx", "665")
    y_c.set("cy", "300")
    y_c.set("r", "10")
    y_c.set("fill", "#854D0E")
    # Green (active)
    g_c = ET.SubElement(svg, "circle")
    g_c.set("cx", "665")
    g_c.set("cy", "322")
    g_c.set("r", "10")
    g_c.set("fill", GREEN)
    g_c.set("stroke", "#86EFAC")
    g_c.set("stroke-width", "2")
    
    # Bottom rules
    add_rule_box(svg, 20, 460, 375, [
        "Переходите только по зебре или подземному переходу",
        "На красный сигнал — стойте, на зелёный — идите",
        "Не перебегайте дорогу перед близким транспортом"
    ], is_correct=True)
    
    add_rule_box(svg, 420, 460, 355, [
        "Переходить на красный или жёлтый сигнал",
        "Играть на проезжей части",
        "Выходить из-за стоящего транспорта без осмотра"
    ], is_correct=False)
    
    return svg


# ============================================================
# LESSON 6: Безопасность пассажира
# ============================================================
def generate_lesson_6():
    svg = svg_root()
    add_def(svg)
    add_background(svg)
    add_header(svg, "Безопасность пассажира", "Общественный транспорт и автомобиль")
    
    # Public transport rules
    add_section_title(svg, 20, 95, "Общественный транспорт")
    
    transport_rules = [
        "Ожидайте транспорт на остановке, не на проезжей части",
        "Входите через заднюю дверь, выходите через переднюю",
        "Держитесь за поручни во время движения",
        "Не прислоняйтесь к дверям",
        "Не отвлекайте водителя разговорами",
        "При аварии — покиньте транспорт через окна/двери"
    ]
    for i, rule in enumerate(transport_rules):
        add_step(svg, 20, 112 + i * 26, i + 1, rule, BLUE)
    
    # Car safety
    add_section_title(svg, 420, 95, "Безопасность в автомобиле")
    
    car_rules = [
        "Всегда пристёгивайте ремень безопасности",
        "Дети до 12 лет — в детском кресле",
        "Не высовывайте руки и голову из окна",
        "Не отвлекайте водителя",
        "Садитесь и выходите со стороны тротуара",
        "Не открывайте двери на ходу"
    ]
    for i, rule in enumerate(car_rules):
        add_check_icon(svg, 425, 107 + i * 26, 14)
        t = ET.SubElement(svg, "text")
        t.set("x", "445")
        t.set("y", str(119 + i * 26))
        t.set("fill", DARK_GRAY)
        t.set("font-size", "11")
        t.set("font-family", "Arial, sans-serif")
        t.text = escape(rule)
    
    # Seatbelt diagram
    add_section_title(svg, 20, 290, "Ремень безопасности")
    
    # Person with seatbelt
    person_x, person_y = 100, 320
    # Body
    body = ET.SubElement(svg, "rect")
    body.set("x", str(person_x - 20))
    body.set("y", str(person_y))
    body.set("width", "40")
    body.set("height", "70")
    body.set("rx", "5")
    body.set("fill", BLUE)
    body.set("fill-opacity", "0.3")
    body.set("stroke", BLUE)
    body.set("stroke-width", "2")
    # Head
    head = ET.SubElement(svg, "circle")
    head.set("cx", str(person_x))
    head.set("cy", str(person_y - 15))
    head.set("r", "15")
    head.set("fill", "#FBBF24")
    body_stroke = ET.SubElement(svg, "rect")
    body_stroke.set("x", str(person_x - 20))
    body_stroke.set("y", str(person_y))
    body_stroke.set("width", "40")
    body_stroke.set("height", "70")
    body_stroke.set("rx", "5")
    body_stroke.set("fill", "none")
    body_stroke.set("stroke", BLUE)
    body_stroke.set("stroke-width", "2")
    # Seatbelt
    belt = ET.SubElement(svg, "line")
    belt.set("x1", str(person_x + 20))
    belt.set("y1", str(person_y - 5))
    belt.set("x2", str(person_x - 15))
    belt.set("y2", str(person_y + 60))
    belt.set("stroke", RED)
    belt.set("stroke-width", "4")
    # Lap belt
    lap = ET.SubElement(svg, "line")
    lap.set("x1", str(person_x - 20))
    lap.set("y1", str(person_y + 45))
    lap.set("x2", str(person_x + 20))
    lap.set("y2", str(person_y + 45))
    lap.set("stroke", RED)
    lap.set("stroke-width", "4")
    
    # Seatbelt facts
    add_info_box(svg, 170, 310, 250, 105, "Факты о ремнях безопасности:", [
        "Снижают риск гибели на 50%",
        "Снижают риск тяжёлых травм на 65%",
        "Защищают при перевороте автомобиля",
        "Пристёгиваться нужно ВСЕМ пассажирам!",
        "Штраф за непристёгнутый ремень"
    ], LIGHT_BLUE, BLUE, BLUE)
    
    # Emergency in transport
    add_section_title(svg, 460, 290, "При аварии в транспорте")
    
    emergency_steps = [
        "Сохраняйте спокойствие",
        "Оцените обстановку",
        "Покиньте транспорт через двери/окна",
        "Помогите тем, кто не может сам",
        "Отойдите на безопасное расстояние",
        "Вызовите 112"
    ]
    for i, step in enumerate(emergency_steps):
        add_step(svg, 465, 305 + i * 26, i + 1, step, RED if i > 4 else ORANGE)
    
    # Bottom: dangerous behavior
    add_rule_box(svg, 20, 460, 375, [
        "Пристёгиваться ремнём безопасности",
        "Держаться за поручни в автобусе",
        "Садиться/выходить со стороны тротуара"
    ], is_correct=True)
    
    add_rule_box(svg, 420, 460, 355, [
        "Стоять в автобусе без опоры",
        "Открывать двери на ходу",
        "Высовываться из окон автомобиля"
    ], is_correct=False)
    
    return svg


# ============================================================
# LESSON 7: Правила поведения на воде
# ============================================================
def generate_lesson_7():
    svg = svg_root()
    add_def(svg)
    add_background(svg)
    add_header(svg, "Правила поведения на воде", "Безопасное купание и опасные ситуации")
    
    # Swimming rules
    add_section_title(svg, 20, 95, "Правила безопасного купания")
    
    swim_rules = [
        "Купайтесь только в разрешённых местах",
        "Не заплывайте за ограничительные знаки",
        "Не купайтесь в нетрезвом состоянии",
        "Не ныряйте в незнакомых местах",
        "Не купайтесь сразу после еды (подождите 1-2 часа)",
        "Не оставляйте детей без присмотра у воды",
        "Не плавайте на надувных матрасах далеко",
        "Не заходите в воду при волнении более 3 баллов"
    ]
    for i, rule in enumerate(swim_rules):
        add_step(svg, 20, 112 + i * 26, i + 1, rule, BLUE)
    
    # Danger signs on water
    add_section_title(svg, 420, 95, "Опасности на воде")
    
    dangers = [
        ("Запрещено купаться", "Красный флаг на пляже", RED),
        ("Осторожно, глубоко!", "Резкое понижение дна", ORANGE),
        ("Сильное течение", "Река с быстрым потоком", AMBER),
        ("Водоросли", "Можно запутаться под водой", GREEN),
        ("Холодные ключи", "Резкое охлаждение воды", BLUE),
    ]
    for i, (title, desc, color) in enumerate(dangers):
        y_pos = 110 + i * 50
        # Icon
        add_warning_icon(svg, 425, y_pos, 16)
        t = ET.SubElement(svg, "text")
        t.set("x", "448")
        t.set("y", str(y_pos + 12))
        t.set("fill", color)
        t.set("font-size", "12")
        t.set("font-weight", "bold")
        t.set("font-family", "Arial, sans-serif")
        t.text = escape(title)
        d = ET.SubElement(svg, "text")
        d.set("x", "448")
        d.set("y", str(y_pos + 28))
        d.set("fill", DARK_GRAY)
        d.set("font-size", "10")
        d.set("font-family", "Arial, sans-serif")
        d.text = escape(desc)
    
    # What to do if you're caught in current
    add_section_title(svg, 20, 345, "Если вы попали в течении")
    
    current_steps = [
        "Не паникуйте и не боритесь с течением",
        "Плывите параллельно берегу",
        "Постепенно смещайтесь к берегу",
        "Зовите на помощь, подняв руку"
    ]
    for i, step in enumerate(current_steps):
        add_step(svg, 25, 360 + i * 28, i + 1, step, BLUE)
    
    # Water safety diagram - depth markers
    add_section_title(svg, 420, 360, "Зоны глубины воды")
    
    # Water area
    water = ET.SubElement(svg, "rect")
    water.set("x", "430")
    water.set("y", "380")
    water.set("width", "340")
    water.set("height", "100")
    water.set("fill", "#BFDBFE")
    
    # Shore line
    shore = ET.SubElement(svg, "rect")
    shore.set("x", "430")
    shore.set("y", "380")
    shore.set("width", "340")
    shore.set("height", "15")
    shore.set("fill", "#FDE68A")
    
    # Depth zones
    zones = [
        (430, 395, 80, "Мелко\nдо 1 м", GREEN),
        (510, 395, 80, "Средне\n1-1.5 м", YELLOW),
        (590, 395, 80, "Глубоко\n1.5-3 м", ORANGE),
        (670, 395, 100, "Опасно\n>3 м", RED),
    ]
    for zx, zy, zw, label, color in zones:
        zr = ET.SubElement(svg, "rect")
        zr.set("x", str(zx))
        zr.set("y", str(zy))
        zr.set("width", str(zw))
        zr.set("height", "85")
        zr.set("fill", color)
        zr.set("fill-opacity", "0.2")
        zr.set("stroke", color)
        zr.set("stroke-width", "1.5")
        lines = label.split("\n")
        for j, ln in enumerate(lines):
            t = ET.SubElement(svg, "text")
            t.set("x", str(zx + zw // 2))
            t.set("y", str(zy + 35 + j * 16))
            t.set("text-anchor", "middle")
            t.set("fill", color)
            t.set("font-size", "10")
            t.set("font-weight", "bold" if j == 0 else "normal")
            t.set("font-family", "Arial, sans-serif")
            t.text = escape(ln)
    
    # Bottom rules
    add_rule_box(svg, 20, 490, 375, [
        "Купайтесь только в специально отведённых местах",
        "Не заплывайте за буйки",
        "Соблюдайте температурный режим воды"
    ], is_correct=True)
    
    add_rule_box(svg, 420, 490, 355, [
        "Купаться в незнакомых водоёмах",
        "Нырять с мостов и обрывов",
        "Купаться в шторм или грозу"
    ], is_correct=False)
    
    return svg


# ============================================================
# LESSON 8: Помощь утопающему
# ============================================================
def generate_lesson_8():
    svg = svg_root()
    add_def(svg)
    add_background(svg)
    add_header(svg, "Помощь утопающему", "Спасательные техники и первая помощь")
    
    # Warning box
    warn_box = ET.SubElement(svg, "rect")
    warn_box.set("x", "20")
    warn_box.set("y", "80")
    warn_box.set("width", str(WIDTH - 40))
    warn_box.set("height", "40")
    warn_box.set("rx", "6")
    warn_box.set("fill", LIGHT_RED)
    warn_box.set("stroke", RED)
    warn_box.set("stroke-width", "2")
    wt = ET.SubElement(svg, "text")
    wt.set("x", str(WIDTH // 2))
    wt.set("y", "105")
    wt.set("text-anchor", "middle")
    wt.set("fill", RED)
    wt.set("font-size", "14")
    wt.set("font-weight", "bold")
    wt.set("font-family", "Arial, sans-serif")
    wt.text = "ВАЖНО: Не прыгайте в воду, если не умеете плавать! Используйте подручные средства!"
    
    # Rescue steps
    add_section_title(svg, 20, 140, "Порядок спасения утопающего")
    
    rescue_steps = [
        "Оцените ситуацию, позовите на помощь",
        "Бросьте утопающему плавательный предмет",
        "Используйте спасательный круг или шест",
        "Если плывёте — подплывайте сзади",
        "Обхватите утопающего под руки",
        "Плывите к берегу боком или на спине"
    ]
    for i, step in enumerate(rescue_steps):
        color = RED if i < 2 else BLUE
        add_step(svg, 20, 155 + i * 28, i + 1, step, color)
    
    # Rescue equipment
    add_section_title(svg, 420, 140, "Спасательные средства")
    
    equipment = [
        ("Спасательный круг", "Бросить так, чтобы упал рядом", ORANGE),
        ("Спасательный шест", "Протянуть утопающему", BLUE),
        ("Верёвка с узлами", "Бросить конец утопающему", GREEN),
        ("Подручные средства", "Бутылки, доски, брёвна", AMBER),
    ]
    for i, (name, desc, color) in enumerate(equipment):
        y_pos = 155 + i * 48
        # Item box
        ib = ET.SubElement(svg, "rect")
        ib.set("x", "425")
        ib.set("y", str(y_pos))
        ib.set("width", "345")
        ib.set("height", "42")
        ib.set("rx", "4")
        ib.set("fill", color)
        ib.set("fill-opacity", "0.1")
        ib.set("stroke", color)
        ib.set("stroke-width", "1")
        nt = ET.SubElement(svg, "text")
        nt.set("x", "435")
        nt.set("y", str(y_pos + 17))
        nt.set("fill", color)
        nt.set("font-size", "12")
        nt.set("font-weight", "bold")
        nt.set("font-family", "Arial, sans-serif")
        nt.text = escape(name)
        dt = ET.SubElement(svg, "text")
        dt.set("x", "435")
        dt.set("y", str(y_pos + 33))
        dt.set("fill", DARK_GRAY)
        dt.set("font-size", "10")
        dt.set("font-family", "Arial, sans-serif")
        dt.text = escape(desc)
    
    # First aid after rescue
    add_section_title(svg, 20, 340, "Первая помощь после извлечения")
    
    aid_steps = [
        "Положите пострадавшего на живот, голову набок",
        "Очистите рот от воды и пены",
        "При отсутствии дыхания — начните СЛР",
        "30 нажатий на грудь : 2 вдоха",
        "Продолжайте до приезда скорой",
        "Согрейте пострадавшего, снимите мокрую одежду"
    ]
    for i, step in enumerate(aid_steps):
        color = RED if "СЛР" in step or "нажатий" in step else GREEN
        add_step(svg, 20, 355 + i * 28, i + 1, step, color)
    
    # CPR diagram
    add_section_title(svg, 420, 355, "Сердечно-лёгочная реанимация")
    
    cpr_box = ET.SubElement(svg, "rect")
    cpr_box.set("x", "425")
    cpr_box.set("y", "370")
    cpr_box.set("width", "345")
    cpr_box.set("height", "130")
    cpr_box.set("rx", "8")
    cpr_box.set("fill", WHITE)
    cpr_box.set("stroke", RED)
    cpr_box.set("stroke-width", "2")
    cpr_box.set("filter", "url(#shadow)")
    
    # Heart icon
    heart = ET.SubElement(svg, "text")
    heart.set("x", "445")
    heart.set("y", "400")
    heart.set("fill", RED)
    heart.set("font-size", "28")
    heart.set("font-family", "Arial, sans-serif")
    heart.text = "+"
    
    cpr_info = [
        "Соотношение: 30 нажатий : 2 вдоха",
        "Глубина нажатий: 5-6 см",
        "Частота: 100-120 нажатий/мин",
        "Не прерывайте СЛР более чем на 10 сек",
        "Продолжайте до прибытия медиков"
    ]
    for i, info in enumerate(cpr_info):
        t = ET.SubElement(svg, "text")
        t.set("x", "480")
        t.set("y", str(395 + i * 20))
        t.set("fill", DARK_GRAY)
        t.set("font-size", "11")
        t.set("font-family", "Arial, sans-serif")
        t.text = escape(info)
    
    # Bottom warning
    add_rule_box(svg, 20, 530, 750, [
        "НИКОГДА не прыгайте в воду за утопающим, если не уверены в своих силах! Лучше бросить плавсредство и вызвать помощь!"
    ], is_correct=False)
    
    return svg


# ============================================================
# LESSON 9: Поведение в экстремальных ситуациях
# ============================================================
def generate_lesson_9():
    svg = svg_root()
    add_def(svg)
    add_background(svg)
    add_header(svg, "Поведение в экстремальных ситуациях", "Стихийные бедствия и тревожный чемоданчик")
    
    # Types of extreme situations
    add_section_title(svg, 20, 95, "Виды экстремальных ситуаций")
    
    situations = [
        ("Землетрясение", "Дрожь земли, разрушения зданий", ORANGE),
        ("Наводнение", "Подъём уровня воды, затопление", BLUE),
        ("Ураган/Шторм", "Сильный ветер, разрушения", "#7C3AED"),
        ("Пожар", "Открытый огонь, дым", RED),
        ("Авария ХОО", "Химическая опасность", "#059669"),
    ]
    for i, (name, desc, color) in enumerate(situations):
        y_pos = 112 + i * 38
        # Colored indicator
        ind = ET.SubElement(svg, "rect")
        ind.set("x", "25")
        ind.set("y", str(y_pos))
        ind.set("width", "6")
        ind.set("height", "28")
        ind.set("fill", color)
        ind.set("rx", "3")
        nt = ET.SubElement(svg, "text")
        nt.set("x", "40")
        nt.set("y", str(y_pos + 14))
        nt.set("fill", color)
        nt.set("font-size", "12")
        nt.set("font-weight", "bold")
        nt.set("font-family", "Arial, sans-serif")
        nt.text = escape(name)
        dt = ET.SubElement(svg, "text")
        dt.set("x", "175")
        dt.set("y", str(y_pos + 14))
        dt.set("fill", DARK_GRAY)
        dt.set("font-size", "10")
        dt.set("font-family", "Arial, sans-serif")
        dt.text = escape(desc)
    
    # General rules
    add_section_title(svg, 20, 305, "Общие правила поведения")
    
    general_rules = [
        "Не паникуйте — паника опаснее ситуации",
        "Оцените обстановку и определите угрозу",
        "Действуйте по плану или инструкциям",
        "Информируйте родных и экстренные службы",
        "Помогайте тем, кто рядом, если это безопасно",
        "Не приближайтесь к месту ЧП"
    ]
    for i, rule in enumerate(general_rules):
        add_step(svg, 20, 320 + i * 26, i + 1, rule, ORANGE)
    
    # Emergency kit
    add_section_title(svg, 420, 95, "Тревожный чемоданчик")
    
    # Kit bag icon
    bag = ET.SubElement(svg, "rect")
    bag.set("x", "435")
    bag.set("y", "108")
    bag.set("width", "60")
    bag.set("height", "45")
    bag.set("rx", "8")
    bag.set("fill", ORANGE)
    bag.set("stroke", "#9A3412")
    bag.set("stroke-width", "2")
    # Handle
    bh = ET.SubElement(svg, "path")
    bh.set("d", "M450,108 Q465,90 480,108")
    bh.set("fill", "none")
    bh.set("stroke", "#9A3412")
    bh.set("stroke-width", "3")
    
    kit_items = [
        "Документы (копии) и деньги",
        "Вода (3 л на человека)",
        "Консервы и сухой паёк на 3 дня",
        "Аптечка первой помощи",
        "Фонарик и батарейки",
        "Радиоприёмник",
        "Тёплая одежда и одеяло",
        "Средства гигиены",
        "Зарядное устройство для телефона",
        "Свисток и нож"
    ]
    for i, item in enumerate(kit_items):
        col = 0 if i < 5 else 1
        row = i % 5
        x = 505 + col * 160
        y = 115 + row * 22
        add_check_icon(svg, x, y - 8, 12)
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + 16))
        t.set("y", str(y))
        t.set("fill", DARK_GRAY)
        t.set("font-size", "10")
        t.set("font-family", "Arial, sans-serif")
        t.text = escape(item)
    
    # Earthquake specific
    add_info_box(svg, 420, 335, 350, 90, "При землетрясении:", [
        "В помещении: встаньте в дверном проёме или",
        "под крепким столом,远离 окон",
        "На улице: отойдите от зданий и линий ЭП",
        "Не пользуйтесь лифтом!",
        "После толчков: выйдите из здания"
    ], LIGHT_ORANGE, ORANGE, ORANGE)
    
    # Flood specific
    add_info_box(svg, 420, 440, 350, 80, "При наводнении:", [
        "Поднимитесь на верхний этаж или крышу",
        "Не пытайтесь плыть в паводковых водах",
        "Подайте сигнал спасателям",
        "Ждите помощи, не покидайте укрытие"
    ], LIGHT_BLUE, BLUE, BLUE)
    
    # Bottom reminder
    add_rule_box(svg, 20, 490, 380, [
        "Заранее подготовьте тревожный чемоданчик",
        "Знайте пути эвакуации из дома",
        "Сохраняйте спокойствие"
    ], is_correct=True)
    
    return svg


# ============================================================
# LESSON 10: Террористическая угроза
# ============================================================
def generate_lesson_10():
    svg = svg_root()
    add_def(svg)
    add_background(svg)
    add_header(svg, "Террористическая угроза", "Правила поведения и порядок действий")
    
    # Warning banner
    warn = ET.SubElement(svg, "rect")
    warn.set("x", "20")
    warn.set("y", "80")
    warn.set("width", str(WIDTH - 40))
    warn.set("height", "35")
    warn.set("rx", "6")
    warn.set("fill", RED)
    add_warning_icon(svg, 30, 85, 22)
    wt = ET.SubElement(svg, "text")
    wt.set("x", str(WIDTH // 2))
    wt.set("y", "102")
    wt.set("text-anchor", "middle")
    wt.set("fill", WHITE)
    wt.set("font-size", "14")
    wt.set("font-weight", "bold")
    wt.set("font-family", "Arial, sans-serif")
    wt.text = "При обнаружении подозрительного предмета — НЕ ТРОГАЙТЕ ЕГО!"
    
    # Rules of behavior
    add_section_title(svg, 20, 130, "Правила поведения при угрозе")
    
    threat_rules = [
        "Не трогайте подозрительные предметы",
        "Немедленно сообщите в полицию: 102 или 112",
        "Отойдите на безопасное расстояние",
        "Не пользуйтесь мобильным телефоном рядом",
        "Эвакуируйтесь спокойно, без паники",
        "Не создавайте давку у выходов",
        "Помогите детям и пожилым людям",
        "Не возвращайтесь в опасную зону"
    ]
    for i, rule in enumerate(threat_rules):
        color = RED if i < 3 else ORANGE
        add_step(svg, 20, 145 + i * 26, i + 1, rule, color)
    
    # If taken hostage
    add_section_title(svg, 420, 130, "Если вы захвачены в заложники")
    
    hostage_rules = [
        "Не сопротивляйтесь и не пытайтесь бежать",
        "Выполняйте требования террористов",
        "Не смотрите им в глаза, не спорьте",
        "Спрашивайте разрешение на любые действия",
        "Старайтесь запомнить приметы террористов",
        "Не делайте резких движений",
        "При штурме — лягте на пол, закройте голову",
        "Не бегите навстречу спецназу"
    ]
    for i, rule in enumerate(hostage_rules):
        add_step(svg, 425, 145 + i * 26, i + 1, rule, RED if i < 3 else AMBER)
    
    # Suspicious items
    add_section_title(svg, 20, 375, "Подозрительные предметы")
    
    suspicious = [
        "Бесхозные сумки, пакеты, коробки",
        "Машину, оставленную в неположенном месте",
        "Провода, торчащие из предметов",
        "Предметы с запахом химикатов",
        "Письма/посылки с подозрительным содержимым"
    ]
    for i, item in enumerate(suspicious):
        add_danger_icon(svg, 25, 385 + i * 24, 14)
        t = ET.SubElement(svg, "text")
        t.set("x", "45")
        t.set("y", str(397 + i * 24))
        t.set("fill", DARK_GRAY)
        t.set("font-size", "11")
        t.set("font-family", "Arial, sans-serif")
        t.text = escape(item)
    
    # Reporting template
    add_section_title(svg, 420, 375, "Как сообщить об угрозе")
    
    report_box = ET.SubElement(svg, "rect")
    report_box.set("x", "425")
    report_box.set("y", "390")
    report_box.set("width", "345")
    report_box.set("height", "110")
    report_box.set("rx", "8")
    report_box.set("fill", WHITE)
    report_box.set("stroke", RED)
    report_box.set("stroke-width", "2")
    report_box.set("filter", "url(#shadow)")
    
    report_items = [
        "1. Точный адрес и описание объекта",
        "2. Время обнаружения",
        "3. Описание подозрительного предмета",
        "4. Есть ли люди рядом",
        "5. Ваше имя и телефон",
        "6. Ждите указаний диспетчера!"
    ]
    for i, item in enumerate(report_items):
        t = ET.SubElement(svg, "text")
        t.set("x", "440")
        t.set("y", str(410 + i * 17))
        t.set("fill", DARK_GRAY)
        t.set("font-size", "11")
        t.set("font-family", "Arial, sans-serif")
        t.text = escape(item)
    
    # Emergency numbers
    add_section_title(svg, 20, 515, "Телефоны")
    add_emergency_number(svg, 20, 535, "112", "Единый номер")
    add_emergency_number(svg, 145, 535, "102", "Полиция")
    add_emergency_number(svg, 270, 535, "101", "МЧС/Пожарная")
    add_emergency_number(svg, 395, 535, "103", "Скорая")
    
    # Final rule
    fr = ET.SubElement(svg, "rect")
    fr.set("x", "530")
    fr.set("y", "530")
    fr.set("width", "240")
    fr.set("height", "50")
    fr.set("rx", "8")
    fr.set("fill", DARK_RED)
    fr.set("filter", "url(#shadow)")
    ft = ET.SubElement(svg, "text")
    ft.set("x", "650")
    ft.set("y", "553")
    ft.set("text-anchor", "middle")
    ft.set("fill", WHITE)
    ft.set("font-size", "11")
    ft.set("font-weight", "bold")
    ft.set("font-family", "Arial, sans-serif")
    ft.text = "Бдительность спасает жизни!"
    ft2 = ET.SubElement(svg, "text")
    ft2.set("x", "650")
    ft2.set("y", "570")
    ft2.set("text-anchor", "middle")
    ft2.set("fill", "#FEE2E2")
    ft2.set("font-size", "10")
    ft2.set("font-family", "Arial, sans-serif")
    ft2.text = "Сообщайте о любых подозрениях"
    
    return svg


# ============================================================
# LESSON 11: Основы первой помощи
# ============================================================
def generate_lesson_11():
    svg = svg_root()
    add_def(svg)
    add_background(svg)
    add_header(svg, "Основы первой помощи", "АВС, кровотечения, ожоги, переломы")
    
    # ABCs of first aid
    add_section_title(svg, 20, 95, "Алгоритм АВС первой помощи")
    
    abc_items = [
        ("A", "Airway", "Воздух — обеспечить проходимость дыхательных путей", RED),
        ("B", "Breathing", "Дыхание — проверить наличие дыхания", BLUE),
        ("C", "Circulation", "Кровообращение — проверить пульс, остановить кровотечение", GREEN),
    ]
    for i, (letter, eng, desc, color) in enumerate(abc_items):
        y_pos = 112 + i * 50
        # Letter circle
        lc = ET.SubElement(svg, "circle")
        lc.set("cx", "40")
        lc.set("cy", str(y_pos + 15))
        lc.set("r", "18")
        lc.set("fill", color)
        lt = ET.SubElement(svg, "text")
        lt.set("x", "40")
        lt.set("y", str(y_pos + 22))
        lt.set("text-anchor", "middle")
        lt.set("fill", WHITE)
        lt.set("font-size", "18")
        lt.set("font-weight", "bold")
        lt.set("font-family", "Arial, sans-serif")
        lt.text = letter
        # English term
        et = ET.SubElement(svg, "text")
        et.set("x", "68")
        et.set("y", str(y_pos + 12))
        et.set("fill", color)
        et.set("font-size", "13")
        et.set("font-weight", "bold")
        et.set("font-family", "Arial, sans-serif")
        et.text = f"{letter} — {eng}"
        # Description
        dt = ET.SubElement(svg, "text")
        dt.set("x", "68")
        dt.set("y", str(y_pos + 28))
        dt.set("fill", DARK_GRAY)
        dt.set("font-size", "11")
        dt.set("font-family", "Arial, sans-serif")
        dt.text = escape(desc)
    
    # Bleeding types
    add_section_title(svg, 20, 275, "Виды кровотечений")
    
    bleed_types = [
        ("Капиллярное", "Кровь сочится каплями", "Промыть, наложить повязку", ORANGE),
        ("Венозное", "Тёмная кровь, течёт равномерно", "Давящая повязка, приподнять", BLUE),
        ("Артериальное", "Алая кровь, пульсирует", "Жгут выше раны, записать время!", RED),
    ]
    for i, (btype, symptom, action, color) in enumerate(bleed_types):
        y_pos = 292 + i * 55
        # Type box
        tb = ET.SubElement(svg, "rect")
        tb.set("x", "25")
        tb.set("y", str(y_pos))
        tb.set("width", "370")
        tb.set("height", "48")
        tb.set("rx", "4")
        tb.set("fill", color)
        tb.set("fill-opacity", "0.1")
        tb.set("stroke", color)
        tb.set("stroke-width", "1.5")
        # Color indicator
        ci = ET.SubElement(svg, "circle")
        ci.set("cx", "45")
        ci.set("cy", str(y_pos + 15))
        ci.set("r", "8")
        ci.set("fill", color)
        # Type name
        nt = ET.SubElement(svg, "text")
        nt.set("x", "60")
        nt.set("y", str(y_pos + 18))
        nt.set("fill", color)
        nt.set("font-size", "12")
        nt.set("font-weight", "bold")
        nt.set("font-family", "Arial, sans-serif")
        nt.text = escape(btype)
        # Symptom
        st = ET.SubElement(svg, "text")
        st.set("x", "170")
        st.set("y", str(y_pos + 18))
        st.set("fill", DARK_GRAY)
        st.set("font-size", "10")
        st.set("font-family", "Arial, sans-serif")
        st.text = escape(symptom)
        # Action
        at = ET.SubElement(svg, "text")
        at.set("x", "35")
        at.set("y", str(y_pos + 38))
        at.set("fill", DARK_GRAY)
        at.set("font-size", "10")
        at.set("font-family", "Arial, sans-serif")
        at.text = escape("Действие: " + action)
    
    # Burns
    add_section_title(svg, 420, 95, "Ожоги и первая помощь")
    
    burn_degrees = [
        ("I степень", "Покраснение, боль", "Охладить водой 10-15 мин", YELLOW),
        ("II степень", "Пузыри, сильная боль", "Охладить, не вскрывать пузыри", ORANGE),
        ("III степень", "Омертвение кожи", "Накрыть чистой тканью, скорую!", RED),
    ]
    for i, (degree, symptom, action, color) in enumerate(burn_degrees):
        y_pos = 112 + i * 48
        db = ET.SubElement(svg, "rect")
        db.set("x", "425")
        db.set("y", str(y_pos))
        db.set("width", "345")
        db.set("height", "42")
        db.set("rx", "4")
        db.set("fill", color)
        db.set("fill-opacity", "0.1")
        db.set("stroke", color)
        db.set("stroke-width", "1.5")
        nt = ET.SubElement(svg, "text")
        nt.set("x", "435")
        nt.set("y", str(y_pos + 16))
        nt.set("fill", color)
        nt.set("font-size", "12")
        nt.set("font-weight", "bold")
        nt.set("font-family", "Arial, sans-serif")
        nt.text = escape(degree)
        st = ET.SubElement(svg, "text")
        st.set("x", "535")
        st.set("y", str(y_pos + 16))
        st.set("fill", DARK_GRAY)
        st.set("font-size", "10")
        st.set("font-family", "Arial, sans-serif")
        st.text = escape(symptom)
        at = ET.SubElement(svg, "text")
        at.set("x", "435")
        nt.set("y", str(y_pos + 34))
        at.set("x", "435")
        at.set("y", str(y_pos + 34))
        at.set("fill", DARK_GRAY)
        at.set("font-size", "10")
        at.set("font-family", "Arial, sans-serif")
        at.text = escape(action)
    
    # Fractures
    add_section_title(svg, 420, 270, "Переломы")
    
    fracture_info = [
        "Признаки: боль, отёк, деформация",
        "Открытый: кость видна, кровотечение",
        "Закрытый: без повреждения кожи",
        "Действие: обездвижить (иммобилизация)",
        "Не пытайтесь вправить кость!",
        "Наложите шину из подручных средств",
        "При открытом — остановите кровь сначала"
    ]
    for i, info in enumerate(fracture_info):
        color = RED if "Не пытайтесь" in info else ORANGE
        add_warning_icon(svg, 425, 280 + i * 22, 14)
        t = ET.SubElement(svg, "text")
        t.set("x", "445")
        t.set("y", str(292 + i * 22))
        t.set("fill", DARK_GRAY)
        t.set("font-size", "10")
        t.set("font-family", "Arial, sans-serif")
        t.text = escape(info)
    
    # Important reminder
    add_rule_box(svg, 20, 470, 375, [
        "Перед оказанием помощи убедитесь в безопасности",
        "Вызовите скорую: 103 или 112",
        "Действуйте спокойно и чётко"
    ], is_correct=True)
    
    add_rule_box(svg, 420, 470, 355, [
        "Не давайте таблетки без назначения",
        "Не прикладывайте лёд к ожогу напрямую",
        "Не перемещайте человека с переломом позвоночника"
    ], is_correct=False)
    
    return svg


# ============================================================
# LESSON 12: Первая помощь при травмах
# ============================================================
def generate_lesson_12():
    svg = svg_root()
    add_def(svg)
    add_background(svg)
    add_header(svg, "Первая помощь при травмах", "Растяжения, вывихи, раны, повязки")
    
    # Sprains
    add_section_title(svg, 20, 95, "Растяжения связок")
    
    sprain_info = [
        "Признаки: боль, отёк, ограничение движения",
        "Действия по правилу RICE:",
    ]
    for i, info in enumerate(sprain_info):
        t = ET.SubElement(svg, "text")
        t.set("x", "25")
        t.set("y", str(112 + i * 18))
        t.set("fill", DARK_GRAY)
        t.set("font-size", "11")
        t.set("font-family", "Arial, sans-serif")
        t.text = escape(info)
    
    # RICE protocol
    rice = [
        ("R", "Rest", "Покой — обездвижьте сустав", RED),
        ("I", "Ice", "Лёд — холодный компресс на 20 мин", BLUE),
        ("C", "Compression", "Давление — тугая повязка", GREEN),
        ("E", "Elevation", "Возвышение — поднимите конечность", ORANGE),
    ]
    for i, (letter, eng, desc, color) in enumerate(rice):
        y_pos = 150 + i * 30
        lc = ET.SubElement(svg, "circle")
        lc.set("cx", "40")
        lc.set("cy", str(y_pos + 8))
        lc.set("r", "12")
        lc.set("fill", color)
        lt = ET.SubElement(svg, "text")
        lt.set("x", "40")
        lt.set("y", str(y_pos + 13))
        lt.set("text-anchor", "middle")
        lt.set("fill", WHITE)
        lt.set("font-size", "12")
        lt.set("font-weight", "bold")
        lt.set("font-family", "Arial, sans-serif")
        lt.text = letter
        rt = ET.SubElement(svg, "text")
        rt.set("x", "60")
        rt.set("y", str(y_pos + 13))
        rt.set("fill", color)
        rt.set("font-size", "11")
        rt.set("font-weight", "bold")
        rt.set("font-family", "Arial, sans-serif")
        rt.text = f"{eng}:"
        dt = ET.SubElement(svg, "text")
        dt.set("x", "130")
        dt.set("y", str(y_pos + 13))
        dt.set("fill", DARK_GRAY)
        dt.set("font-size", "11")
        dt.set("font-family", "Arial, sans-serif")
        dt.text = escape(desc)
    
    # Dislocations
    add_section_title(svg, 20, 280, "Вывихи")
    
    disloc_info = [
        "Признаки: сильная боль, деформация сустава,",
        "невозможность движения, отёк",
        "ПЕРВАЯ ПОМОЩЬ:",
        "1. Обездвижьте сустав в том положении, каком он есть",
        "2. Приложите холод",
        "3. Обратитесь к врачу",
        "4. НЕ пытайтесь вправить вывих самостоятельно!"
    ]
    for i, info in enumerate(disloc_info):
        color = RED if "НЕ пытайтесь" in info else DARK_GRAY
        fw = "bold" if "ПЕРВАЯ ПОМОЩЬ" in info or "НЕ пытайтесь" in info else "normal"
        t = ET.SubElement(svg, "text")
        t.set("x", "25")
        t.set("y", str(296 + i * 18))
        t.set("fill", color)
        t.set("font-size", "11")
        t.set("font-weight", fw)
        t.set("font-family", "Arial, sans-serif")
        t.text = escape(info)
    
    # Wounds
    add_section_title(svg, 420, 95, "Раны и их обработка")
    
    wound_types = [
        ("Ссадина", "Поверхностное повреждение", "Промыть, обработать антисептиком"),
        ("Резаная рана", "Ровные края, обильное кровотечение", "Наложить стерильную повязку"),
        ("Колота рана", "Глубокая, узкая рана", "Не извлекать предмет! Наложить повязку"),
        ("Рваная рана", "Неровные края", "Остановить кровь, наложить повязку"),
    ]
    for i, (wtype, desc, action) in enumerate(wound_types):
        y_pos = 112 + i * 55
        wb = ET.SubElement(svg, "rect")
        wb.set("x", "425")
        wb.set("y", str(y_pos))
        wb.set("width", "345")
        wb.set("height", "48")
        wb.set("rx", "4")
        wb.set("fill", LIGHT_ORANGE)
        wb.set("stroke", ORANGE)
        wb.set("stroke-width", "1")
        wt = ET.SubElement(svg, "text")
        wt.set("x", "435")
        wt.set("y", str(y_pos + 16))
        wt.set("fill", ORANGE)
        wt.set("font-size", "12")
        wt.set("font-weight", "bold")
        wt.set("font-family", "Arial, sans-serif")
        wt.text = escape(wtype)
        dt = ET.SubElement(svg, "text")
        dt.set("x", "540")
        dt.set("y", str(y_pos + 16))
        dt.set("fill", DARK_GRAY)
        dt.set("font-size", "10")
        dt.set("font-family", "Arial, sans-serif")
        dt.text = escape(desc)
        at = ET.SubElement(svg, "text")
        at.set("x", "435")
        at.set("y", str(y_pos + 36))
        at.set("fill", GREEN)
        at.set("font-size", "10")
        at.set("font-family", "Arial, sans-serif")
        at.text = escape(action)
    
    # Bandaging types
    add_section_title(svg, 420, 340, "Виды повязок")
    
    bandages = [
        ("Круговая", "Для запястья, лодыжки", BLUE),
        ("Спиральная", "Для предплечья, голени", GREEN),
        ("Крестообразная", "Для затылка, грудной клетки", ORANGE),
        ("Восьмиобразная", "Для суставов (колено, локоть)", "#7C3AED"),
    ]
    for i, (btype, use, color) in enumerate(bandages):
        y_pos = 357 + i * 30
        # Bandage icon (spiral line)
        for j in range(3):
            seg = ET.SubElement(svg, "line")
            seg.set("x1", str(430 + j * 8))
            seg.set("y1", str(y_pos + j * 4))
            seg.set("x2", str(438 + j * 8))
            seg.set("y2", str(y_pos - 4 + j * 4))
            seg.set("stroke", color)
            seg.set("stroke-width", "2")
        bt = ET.SubElement(svg, "text")
        bt.set("x", "465")
        bt.set("y", str(y_pos + 8))
        bt.set("fill", color)
        bt.set("font-size", "11")
        bt.set("font-weight", "bold")
        bt.set("font-family", "Arial, sans-serif")
        bt.text = escape(btype)
        ut = ET.SubElement(svg, "text")
        ut.set("x", "590")
        ut.set("y", str(y_pos + 8))
        ut.set("fill", DARK_GRAY)
        ut.set("font-size", "10")
        ut.set("font-family", "Arial, sans-serif")
        ut.text = escape(use)
    
    # First aid kit contents
    add_section_title(svg, 20, 430, "Аптечка первой помощи")
    
    kit = [
        "Бинты стерильные и нестерильные",
        "Вата, марлевые салфетки",
        "Пластырь бактерицидный",
        "Перекись водорода 3%",
        "Йод или зелёнка",
        "Жгут кровеостанавливающий",
        "Анальгетики (обезболивающие)",
        "Ножницы, пинцет"
    ]
    for i, item in enumerate(kit):
        col = 0 if i < 4 else 1
        row = i % 4
        x = 25 + col * 200
        y = 448 + row * 22
        add_check_icon(svg, x, y - 8, 12)
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + 16))
        t.set("y", str(y))
        t.set("fill", DARK_GRAY)
        t.set("font-size", "10")
        t.set("font-family", "Arial, sans-serif")
        t.text = escape(item)
    
    # Bottom rules
    add_rule_box(svg, 420, 490, 355, [
        "Обездвижьте травмированную конечность",
        "Приложите холод к месту травмы",
        "Обратитесь к врачу"
    ], is_correct=True)
    
    add_rule_box(svg, 20, 545, 750, [
        "Не вправляйте вывихи самостоятельно!",
        "Не извлекайте инородные предметы из ран!",
        "Не прикладывайте лёд напрямую к коже!"
    ], is_correct=False)
    
    return svg


# ============================================================
# Main execution
# ============================================================
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    generators = [
        (1, generate_lesson_1),
        (2, generate_lesson_2),
        (3, generate_lesson_3),
        (4, generate_lesson_4),
        (5, generate_lesson_5),
        (6, generate_lesson_6),
        (7, generate_lesson_7),
        (8, generate_lesson_8),
        (9, generate_lesson_9),
        (10, generate_lesson_10),
        (11, generate_lesson_11),
        (12, generate_lesson_12),
    ]
    
    results = []
    for num, gen_fn in generators:
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
        try:
            svg = gen_fn()
            tree = ET.ElementTree(svg)
            ET.indent(tree, space="  ")
            tree.write(filepath, encoding="unicode", xml_declaration=True)
            
            # Validate
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                ET.fromstring(content)
                file_size = os.path.getsize(filepath)
                results.append(f"  Lesson {num}: OK ({file_size:,} bytes)")
            except ET.ParseError as e:
                results.append(f"  Lesson {num}: VALIDATION FAILED - {e}")
        except Exception as e:
            results.append(f"  Lesson {num}: GENERATION FAILED - {e}")
    
    print(f"\nGenerated {len(generators)} SVG files in: {OUTPUT_DIR}")
    print("Results:")
    for r in results:
        print(r)
    
    # Summary
    ok_count = sum(1 for r in results if "OK" in r)
    fail_count = sum(1 for r in results if "FAILED" in r)
    print(f"\nSummary: {ok_count} successful, {fail_count} failed")


if __name__ == "__main__":
    main()
