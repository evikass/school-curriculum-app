#!/usr/bin/env python3
"""
Generate 6 educational SVG images for Grade 8 Informatics lessons.
Output: /home/z/my-project/school-curriculum-app/public/images/grades/8/informatics/lesson-{n}.svg
"""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/informatics"
W, H = 800, 600

# Color scheme
PRIMARY = "#0EA5E9"       # sky-500
PRIMARY_DARK = "#0284C7"  # sky-600
PRIMARY_LIGHT = "#E0F2FE" # sky-100
PRIMARY_MED = "#7DD3FC"   # sky-300
BG = "#F0F9FF"            # sky-50
WHITE = "#FFFFFF"
DARK = "#0C4A6E"          # sky-900
GRAY = "#64748B"
CODE_BG = "#1E293B"       # slate-800
CODE_GREEN = "#4ADE80"
CODE_YELLOW = "#FACC15"
CODE_ORANGE = "#FB923C"
CODE_PINK = "#F472B6"
CODE_BLUE = "#60A5FA"
CODE_WHITE = "#E2E8F0"
ACCENT = "#38BDF8"        # sky-400
BOX_BORDER = "#BAE6FD"    # sky-200


def esc(text):
    """Escape text for XML."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def svg_root():
    """Create SVG root element."""
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
    grad.set("x1", "0%"); grad.set("y1", "0%")
    grad.set("x2", "0%"); grad.set("y2", "100%")
    stop1 = ET.SubElement(grad, "stop")
    stop1.set("offset", "0%"); stop1.set("style", f"stop-color:{WHITE};stop-opacity:1")
    stop2 = ET.SubElement(grad, "stop")
    stop2.set("offset", "100%"); stop2.set("style", f"stop-color:{BG};stop-opacity:1")
    
    rect = ET.SubElement(svg, "rect")
    rect.set("width", str(W)); rect.set("height", str(H))
    rect.set("fill", "url(#bgGrad)")


def add_title(svg, text, y=38):
    """Add lesson title with decorative line."""
    # Title background bar
    bar = ET.SubElement(svg, "rect")
    bar.set("x", "0"); bar.set("y", "0")
    bar.set("width", str(W)); bar.set("height", "56")
    bar.set("fill", PRIMARY); bar.set("rx", "0")
    
    # Title text
    t = ET.SubElement(svg, "text")
    t.set("x", str(W // 2)); t.set("y", str(y))
    t.set("text-anchor", "middle")
    t.set("fill", WHITE); t.set("font-size", "22")
    t.set("font-weight", "bold"); t.set("font-family", "Arial, sans-serif")
    t.text = text
    
    # Decorative line
    line = ET.SubElement(svg, "line")
    line.set("x1", "50"); line.set("y1", "52")
    line.set("x2", str(W - 50)); line.set("y2", "52")
    line.set("stroke", ACCENT); line.set("stroke-width", "2")


def add_box(svg, x, y, w, h, title=None, fill=WHITE, border=BOX_BORDER, rx=8):
    """Add a rounded box with optional title."""
    # Shadow
    shadow = ET.SubElement(svg, "rect")
    shadow.set("x", str(x + 2)); shadow.set("y", str(y + 2))
    shadow.set("width", str(w)); shadow.set("height", str(h))
    shadow.set("fill", "#94A3B8"); shadow.set("rx", str(rx))
    shadow.set("opacity", "0.15")
    
    # Box
    box = ET.SubElement(svg, "rect")
    box.set("x", str(x)); box.set("y", str(y))
    box.set("width", str(w)); box.set("height", str(h))
    box.set("fill", fill); box.set("stroke", border)
    box.set("stroke-width", "2"); box.set("rx", str(rx))
    
    if title:
        # Title bar
        tbar = ET.SubElement(svg, "rect")
        tbar.set("x", str(x)); tbar.set("y", str(y))
        tbar.set("width", str(w)); tbar.set("height", "28")
        tbar.set("fill", PRIMARY_DARK)
        tbar.set("rx", str(rx))
        # Cover bottom corners of title bar
        tcover = ET.SubElement(svg, "rect")
        tcover.set("x", str(x)); tcover.set("y", str(y + 20))
        tcover.set("width", str(w)); tcover.set("height", "8")
        tcover.set("fill", PRIMARY_DARK)
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + w // 2)); t.set("y", str(y + 19))
        t.set("text-anchor", "middle")
        t.set("fill", WHITE); t.set("font-size", "13")
        t.set("font-weight", "bold"); t.set("font-family", "Arial, sans-serif")
        t.text = title


def add_text(svg, x, y, text, size=13, fill=DARK, anchor="start", weight="normal", family="Arial, sans-serif"):
    """Add text element."""
    t = ET.SubElement(svg, "text")
    t.set("x", str(x)); t.set("y", str(y))
    t.set("text-anchor", anchor)
    t.set("fill", fill); t.set("font-size", str(size))
    t.set("font-weight", weight); t.set("font-family", family)
    t.text = text
    return t


def add_code_block(svg, x, y, w, h, code_lines):
    """Add a code block with syntax-like coloring."""
    # Background
    cb = ET.SubElement(svg, "rect")
    cb.set("x", str(x)); cb.set("y", str(y))
    cb.set("width", str(w)); cb.set("height", str(h))
    cb.set("fill", CODE_BG); cb.set("rx", "6")
    
    # Top bar with dots
    topbar = ET.SubElement(svg, "rect")
    topbar.set("x", str(x)); topbar.set("y", str(y))
    topbar.set("width", str(w)); topbar.set("height", "20")
    topbar.set("fill", "#334155"); topbar.set("rx", "6")
    topcover = ET.SubElement(svg, "rect")
    topcover.set("x", str(x)); topcover.set("y", str(y + 14))
    topcover.set("width", str(w)); topcover.set("height", "6")
    topcover.set("fill", "#334155")
    
    # Dots
    for i, color in enumerate(["#EF4444", "#F59E0B", "#22C55E"]):
        dot = ET.SubElement(svg, "circle")
        dot.set("cx", str(x + 14 + i * 16)); dot.set("cy", str(y + 10))
        dot.set("r", "4"); dot.set("fill", color)
    
    # Code lines
    line_y = y + 34
    for line_text, color in code_lines:
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + 12)); t.set("y", str(line_y))
        t.set("fill", color); t.set("font-size", "12")
        t.set("font-family", "Consolas, monospace")
        t.text = line_text
        line_y += 16


def add_arrow(svg, x1, y1, x2, y2, color=PRIMARY):
    """Add an arrow line."""
    line = ET.SubElement(svg, "line")
    line.set("x1", str(x1)); line.set("y1", str(y1))
    line.set("x2", str(x2)); line.set("y2", str(y2))
    line.set("stroke", color); line.set("stroke-width", "2")
    line.set("marker-end", "url(#arrowhead)")
    
    # Simple arrowhead as polygon
    if y2 > y1:  # downward
        points = f"{x2},{y2} {x2-5},{y2-8} {x2+5},{y2-8}"
    elif x2 > x1:  # rightward
        points = f"{x2},{y2} {x2-8},{y2-5} {x2-8},{y2+5}"
    else:  # leftward
        points = f"{x2},{y2} {x2+8},{y2-5} {x2+8},{y2+5}"
    poly = ET.SubElement(svg, "polygon")
    poly.set("points", points)
    poly.set("fill", color)


def add_flowchart_box(svg, x, y, w, h, text, shape="rect", fill=PRIMARY_LIGHT, border=PRIMARY):
    """Add a flowchart shape (rect, diamond, parallelogram)."""
    if shape == "rect":
        r = ET.SubElement(svg, "rect")
        r.set("x", str(x)); r.set("y", str(y))
        r.set("width", str(w)); r.set("height", str(h))
        r.set("fill", fill); r.set("stroke", border)
        r.set("stroke-width", "2"); r.set("rx", "4")
    elif shape == "diamond":
        cx, cy = x + w // 2, y + h // 2
        points = f"{cx},{y} {x+w},{cy} {cx},{y+h} {x},{cy}"
        p = ET.SubElement(svg, "polygon")
        p.set("points", points)
        p.set("fill", fill); p.set("stroke", border)
        p.set("stroke-width", "2")
    elif shape == "rounded":
        r = ET.SubElement(svg, "rect")
        r.set("x", str(x)); r.set("y", str(y))
        r.set("width", str(w)); r.set("height", str(h))
        r.set("fill", fill); r.set("stroke", border)
        r.set("stroke-width", "2"); r.set("rx", str(h // 2))
    elif shape == "parallelogram":
        offset = 10
        points = f"{x+offset},{y} {x+w},{y} {x+w-offset},{y+h} {x},{y+h}"
        p = ET.SubElement(svg, "polygon")
        p.set("points", points)
        p.set("fill", fill); p.set("stroke", border)
        p.set("stroke-width", "2")
    
    # Center text
    t = ET.SubElement(svg, "text")
    t.set("x", str(x + w // 2)); t.set("y", str(y + h // 2 + 5))
    t.set("text-anchor", "middle")
    t.set("fill", DARK); t.set("font-size", "11")
    t.set("font-weight", "bold"); t.set("font-family", "Arial, sans-serif")
    t.text = text


def add_connector(svg, x1, y1, x2, y2, color=PRIMARY):
    """Simple line connector."""
    line = ET.SubElement(svg, "line")
    line.set("x1", str(x1)); line.set("y1", str(y1))
    line.set("x2", str(x2)); line.set("y2", str(y2))
    line.set("stroke", color); line.set("stroke-width", "2")
    # arrowhead
    if y2 > y1:
        points = f"{x2},{y2} {x2-4},{y2-7} {x2+4},{y2-7}"
    elif x2 > x1:
        points = f"{x2},{y2} {x2-7},{y2-4} {x2-7},{y2+4}"
    elif x2 < x1:
        points = f"{x2},{y2} {x2+7},{y2-4} {x2+7},{y2+4}"
    else:
        return
    poly = ET.SubElement(svg, "polygon")
    poly.set("points", points)
    poly.set("fill", color)


def add_icon(svg, x, y, icon_type, size=24, color=PRIMARY):
    """Add simple geometric icon."""
    if icon_type == "info":
        # Circle with 'i'
        c = ET.SubElement(svg, "circle")
        c.set("cx", str(x + size//2)); c.set("cy", str(y + size//2))
        c.set("r", str(size//2)); c.set("fill", color)
        add_text(svg, x + size//2, y + size//2 + 5, "i", size=14, fill=WHITE, anchor="middle", weight="bold")
    elif icon_type == "gear":
        # Simple gear-like circle
        c = ET.SubElement(svg, "circle")
        c.set("cx", str(x + size//2)); c.set("cy", str(y + size//2))
        c.set("r", str(size//2 - 2)); c.set("fill", "none")
        c.set("stroke", color); c.set("stroke-width", "3")
        c2 = ET.SubElement(svg, "circle")
        c2.set("cx", str(x + size//2)); c2.set("cy", str(y + size//2))
        c2.set("r", str(size//4)); c2.set("fill", color)
    elif icon_type == "code":
        # Angle brackets < >
        add_text(svg, x, y + size - 4, "</>", size=16, fill=color, weight="bold", family="Consolas, monospace")
    elif icon_type == "chip":
        # Square with pins
        r = ET.SubElement(svg, "rect")
        r.set("x", str(x + 4)); r.set("y", str(y + 4))
        r.set("width", str(size - 8)); r.set("height", str(size - 8))
        r.set("fill", color); r.set("rx", "2")
        for dx in [0, size - 4]:
            for dy in [size//3, 2*size//3]:
                l = ET.SubElement(svg, "line")
                l.set("x1", str(x + dx)); l.set("y1", str(y + dy))
                l.set("x2", str(x + dx + (4 if dx == 0 else -4))); l.set("y2", str(y + dy))
                l.set("stroke", color); l.set("stroke-width", "2")


# ============================================================
# LESSON 1: Информация и её свойства
# ============================================================
def generate_lesson1():
    svg = svg_root()
    add_bg(svg)
    add_title(svg, "Урок 1: Информация и её свойства")
    
    # Left column - Types of information
    add_box(svg, 20, 68, 250, 200, "Виды информации")
    types = [
        ("Текстовая", "books, documents"),
        ("Числовая", "numbers, formulas"),
        ("Графическая", "images, charts"),
        ("Звуковая", "audio, speech"),
        ("Видеоинформация", "video clips"),
    ]
    for i, (name, ex) in enumerate(types):
        yy = 112 + i * 32
        # Icon circle
        c = ET.SubElement(svg, "circle")
        c.set("cx", "38"); c.set("cy", str(yy - 4))
        c.set("r", "8"); c.set("fill", PRIMARY if i % 2 == 0 else ACCENT)
        add_text(svg, 38, yy, str(i + 1), size=10, fill=WHITE, anchor="middle", weight="bold")
        add_text(svg, 52, yy, name, size=12, fill=DARK, weight="bold")
        add_text(svg, 160, yy, ex, size=10, fill=GRAY)
    
    # Right top - Units of information
    add_box(svg, 290, 68, 240, 200, "Единицы измерения")
    units = [
        ("1 бит", "0 или 1"),
        ("1 байт", "= 8 бит"),
        ("1 КБ (килобайт)", "= 1024 байт"),
        ("1 МБ (мегабайт)", "= 1024 КБ"),
        ("1 ГБ (гигабайт)", "= 1024 МБ"),
    ]
    for i, (name, val) in enumerate(units):
        yy = 112 + i * 32
        add_text(svg, 302, yy, name, size=12, fill=PRIMARY_DARK, weight="bold", family="Consolas, monospace")
        add_text(svg, 440, yy, val, size=11, fill=GRAY)
    
    # Conversion example
    add_box(svg, 20, 282, 510, 80, "Перевод единиц")
    add_text(svg, 35, 316, "Пример: 2048 байт = 2048 / 1024 = 2 КБ", size=12, fill=DARK, family="Consolas, monospace")
    add_text(svg, 35, 338, "Формула: КБ = байт / 1024", size=12, fill=PRIMARY_DARK, weight="bold")
    
    # Right side - Information processes
    add_box(svg, 548, 68, 232, 294, "Информ. процессы")
    processes = [
        ("Сбор", "#0EA5E9"),
        ("Обработка", "#0284C7"),
        ("Хранение", "#0369A1"),
        ("Передача", "#075985"),
        ("Поиск", "#0C4A6E"),
    ]
    for i, (name, color) in enumerate(processes):
        yy = 112 + i * 48
        r = ET.SubElement(svg, "rect")
        r.set("x", "562"); r.set("y", str(yy - 12))
        r.set("width", "204"); r.set("height", "36")
        r.set("fill", color); r.set("rx", "18")
        add_text(svg, 664, yy + 8, name, size=13, fill=WHITE, anchor="middle", weight="bold")
    
    # Properties section
    add_box(svg, 20, 376, 760, 210, "Свойства информации")
    props = [
        ("Объективность", "Не зависит от мнения"),
        ("Достоверность", "Отражает истинное положение"),
        ("Полнота", "Достаточна для понимания"),
        ("Актуальность", "Важна в данный момент"),
        ("Полезность", "Имеет практическую ценность"),
        ("Понятность", "Доступна для восприятия"),
    ]
    for i, (name, desc) in enumerate(props):
        col = i % 3
        row = i // 3
        bx = 35 + col * 250
        by = 418 + row * 80
        r = ET.SubElement(svg, "rect")
        r.set("x", str(bx)); r.set("y", str(by))
        r.set("width", "230"); r.set("height", "65")
        r.set("fill", PRIMARY_LIGHT); r.set("stroke", BOX_BORDER)
        r.set("stroke-width", "1"); r.set("rx", "6")
        add_text(svg, bx + 12, by + 22, name, size=12, fill=PRIMARY_DARK, weight="bold")
        add_text(svg, bx + 12, by + 44, desc, size=10, fill=GRAY)
    
    return svg


# ============================================================
# LESSON 2: Системы счисления
# ============================================================
def generate_lesson2():
    svg = svg_root()
    add_bg(svg)
    add_title(svg, "Урок 2: Системы счисления")
    
    # Number systems overview
    add_box(svg, 20, 68, 370, 120, "Основные системы счисления")
    systems = [
        ("Двоичная", "2", "0, 1", "0b1010"),
        ("Восьмеричная", "8", "0-7", "0o12"),
        ("Десятичная", "10", "0-9", "10"),
        ("Шестнадцатеричная", "16", "0-9, A-F", "0xA"),
    ]
    # Table header
    headers = ["Система", "Осн.", "Цифры", "Пример"]
    for j, h in enumerate(headers):
        hx = 30 + j * 90
        add_text(svg, hx, 106, h, size=11, fill=WHITE, weight="bold")
    for i, (name, base, digits, ex) in enumerate(systems):
        yy = 124 + i * 22
        vals = [name, base, digits, ex]
        for j, v in enumerate(vals):
            hx = 30 + j * 90
            add_text(svg, hx, yy, v, size=10, fill=DARK, family="Consolas, monospace" if j > 0 else "Arial, sans-serif")
    
    # Conversion table - binary to decimal
    add_box(svg, 20, 200, 370, 185, "Перевод двоичного в десятичное")
    add_text(svg, 35, 240, "Пример: 1011", size=13, fill=DARK, weight="bold", family="Consolas, monospace")
    # Position weights
    add_text(svg, 35, 262, "Разряд:", size=11, fill=GRAY)
    positions = ["3", "2", "1", "0"]
    digits = ["1", "0", "1", "1"]
    weights = ["8", "4", "2", "1"]
    for i in range(4):
        bx = 120 + i * 62
        r = ET.SubElement(svg, "rect")
        r.set("x", str(bx)); r.set("y", "250")
        r.set("width", "50"); r.set("height", "50")
        r.set("fill", PRIMARY_LIGHT if digits[i] == "1" else "#F1F5F9")
        r.set("stroke", PRIMARY); r.set("stroke-width", "1"); r.set("rx", "4")
        add_text(svg, bx + 25, 268, digits[i], size=16, fill=DARK, anchor="middle", weight="bold", family="Consolas, monospace")
        add_text(svg, bx + 25, 286, f"2^{positions[i]}", size=9, fill=GRAY, anchor="middle")
        add_text(svg, bx + 25, 296, f"={weights[i]}", size=9, fill=PRIMARY_DARK, anchor="middle")
    
    add_text(svg, 35, 320, "1*8 + 0*4 + 1*2 + 1*1 = 11", size=13, fill=PRIMARY_DARK, weight="bold", family="Consolas, monospace")
    add_text(svg, 35, 345, "Формула: sum(d[i] * 2^i)", size=11, fill=GRAY)
    
    # Decimal to binary algorithm
    add_box(svg, 20, 397, 370, 190, "Перевод десятичного в двоичное")
    add_text(svg, 35, 435, "Пример: 13 -> ?", size=13, fill=DARK, weight="bold", family="Consolas, monospace")
    steps = [
        "13 / 2 = 6  остаток 1",
        " 6 / 2 = 3  остаток 0",
        " 3 / 2 = 1  остаток 1",
        " 1 / 2 = 0  остаток 1",
    ]
    for i, step in enumerate(steps):
        add_text(svg, 40, 458 + i * 20, step, size=11, fill=DARK, family="Consolas, monospace")
    add_text(svg, 35, 540, "Ответ: 1101 (снизу вверх)", size=12, fill=PRIMARY_DARK, weight="bold")
    
    # Right column - Python code
    add_box(svg, 410, 68, 370, 225, "Python: перевод систем")
    code = [
        ("# Двоичное в десятичное", CODE_GREEN),
        ("binary = '1011'", CODE_WHITE),
        ("decimal = int(binary, 2)", CODE_YELLOW),
        ("print(decimal)  # 11", CODE_GREEN),
        ("", CODE_WHITE),
        ("# Десятичное в двоичное", CODE_GREEN),
        ("num = 13", CODE_WHITE),
        ("print(bin(num))   # 0b1101", CODE_GREEN),
        ("", CODE_WHITE),
        ("# Шестнадцатеричное", CODE_GREEN),
        ("print(hex(255))  # 0xff", CODE_GREEN),
        ("print(int('FF', 16))  # 255", CODE_GREEN),
    ]
    add_code_block(svg, 420, 100, 350, 185, code)
    
    # Conversion diagram
    add_box(svg, 410, 308, 370, 279, "Схема перевода")
    # Central circle - decimal
    cx, cy = 595, 430
    c = ET.SubElement(svg, "circle")
    c.set("cx", str(cx)); c.set("cy", str(cy))
    c.set("r", "30"); c.set("fill", PRIMARY)
    add_text(svg, cx, cy + 5, "10", size=18, fill=WHITE, anchor="middle", weight="bold")
    
    # Binary
    bx, by = 475, 365
    c2 = ET.SubElement(svg, "circle")
    c2.set("cx", str(bx)); c2.set("cy", str(by))
    c2.set("r", "22"); c2.set("fill", ACCENT)
    add_text(svg, bx, by + 5, "2", size=15, fill=WHITE, anchor="middle", weight="bold")
    
    # Octal
    ox, oy = 715, 365
    c3 = ET.SubElement(svg, "circle")
    c3.set("cx", str(ox)); c3.set("cy", str(oy))
    c3.set("r", "22"); c3.set("fill", ACCENT)
    add_text(svg, ox, oy + 5, "8", size=15, fill=WHITE, anchor="middle", weight="bold")
    
    # Hex
    hx2, hy2 = 595, 530
    c4 = ET.SubElement(svg, "circle")
    c4.set("cx", str(hx2)); c4.set("cy", str(hy2))
    c4.set("r", "22"); c4.set("fill", ACCENT)
    add_text(svg, hx2, hy2 + 5, "16", size=15, fill=WHITE, anchor="middle", weight="bold")
    
    # Connectors
    add_connector(svg, bx + 20, by + 15, cx - 25, cy - 20, PRIMARY_DARK)
    add_connector(svg, ox - 20, oy + 15, cx + 25, cy - 20, PRIMARY_DARK)
    add_connector(svg, cx, cy + 30, hx2, hy2 - 22, PRIMARY_DARK)
    
    # Labels
    add_text(svg, 510, 378, "bin()", size=9, fill=GRAY, family="Consolas, monospace")
    add_text(svg, 650, 378, "oct()", size=9, fill=GRAY, family="Consolas, monospace")
    add_text(svg, 610, 500, "hex()", size=9, fill=GRAY, family="Consolas, monospace")
    
    return svg


# ============================================================
# LESSON 3: Понятие алгоритма
# ============================================================
def generate_lesson3():
    svg = svg_root()
    add_bg(svg)
    add_title(svg, "Урок 3: Понятие алгоритма")
    
    # Definition box
    add_box(svg, 20, 68, 760, 60)
    add_text(svg, 35, 95, "Алгоритм", size=14, fill=PRIMARY_DARK, weight="bold")
    add_text(svg, 120, 95, "- конечная последовательность точно определённых действий, приводящая к результату", size=12, fill=DARK)
    add_text(svg, 35, 115, "Слово происходит от имени математика аль-Хорезми (IX век)", size=10, fill=GRAY)
    
    # Properties
    add_box(svg, 20, 140, 380, 200, "Свойства алгоритма")
    props = [
        ("Дискретность", "Разбивается на шаги"),
        ("Детерминированность", "Однозначность каждого шага"),
        ("Конечность", "Завершается за конечное время"),
        ("Массовость", "Применим к классу задач"),
        ("Результативность", "Приводит к результату"),
    ]
    colors = ["#0EA5E9", "#0284C7", "#0369A1", "#075985", "#0C4A6E"]
    for i, (name, desc) in enumerate(props):
        yy = 186 + i * 32
        r = ET.SubElement(svg, "rect")
        r.set("x", "32"); r.set("y", str(yy - 11))
        r.set("width", "8"); r.set("height", "14")
        r.set("fill", colors[i]); r.set("rx", "2")
        add_text(svg, 48, yy, name, size=12, fill=DARK, weight="bold")
        add_text(svg, 195, yy, desc, size=10, fill=GRAY)
    
    # Ways to write algorithms
    add_box(svg, 410, 140, 370, 200, "Способы записи алгоритма")
    ways = [
        ("Словесный", "Описание на естественном языке"),
        ("Формульный", "Математические формулы"),
        ("Блок-схема", "Графическое изображение"),
        ("Псевдокод", "Условный язык программирования"),
        ("Язык программирования", "Python, C++, Java..."),
    ]
    for i, (name, desc) in enumerate(ways):
        yy = 186 + i * 32
        r = ET.SubElement(svg, "circle")
        r.set("cx", "425"); r.set("cy", str(yy - 4))
        r.set("r", "7"); r.set("fill", PRIMARY if i < 3 else ACCENT)
        add_text(svg, 425, yy, str(i + 1), size=9, fill=WHITE, anchor="middle", weight="bold")
        add_text(svg, 438, yy, name, size=11, fill=DARK, weight="bold")
        add_text(svg, 438, yy + 14, desc, size=9, fill=GRAY)
    
    # Flowchart legend
    add_box(svg, 20, 354, 380, 230, "Обозначения блок-схем")
    
    # Start/End - rounded
    add_flowchart_box(svg, 35, 392, 100, 30, "Начало/Конец", shape="rounded", fill=PRIMARY_LIGHT, border=PRIMARY)
    add_text(svg, 150, 412, "- Овал", size=11, fill=GRAY)
    
    # Process - rect
    add_flowchart_box(svg, 35, 432, 100, 30, "Действие", shape="rect", fill=PRIMARY_LIGHT, border=PRIMARY)
    add_text(svg, 150, 452, "- Прямоугольник", size=11, fill=GRAY)
    
    # Decision - diamond
    add_flowchart_box(svg, 35, 472, 100, 35, "Условие", shape="diamond", fill="#FEF3C7", border="#F59E0B")
    add_text(svg, 150, 494, "- Ромб", size=11, fill=GRAY)
    
    # Input/Output - parallelogram
    add_flowchart_box(svg, 35, 520, 100, 30, "Ввод/Вывод", shape="parallelogram", fill="#ECFDF5", border="#10B981")
    add_text(svg, 150, 540, "- Параллелограмм", size=11, fill=GRAY)
    
    # Flowchart example - finding max of two numbers
    add_box(svg, 410, 354, 370, 230, "Пример: max(a, b)")
    
    # Start
    add_flowchart_box(svg, 548, 390, 90, 26, "Начало", shape="rounded", fill=PRIMARY_LIGHT, border=PRIMARY)
    add_connector(svg, 593, 416, 593, 428, PRIMARY)
    
    # Input
    add_flowchart_box(svg, 548, 428, 90, 26, "Ввод a, b", shape="parallelogram", fill="#ECFDF5", border="#10B981")
    add_connector(svg, 593, 454, 593, 466, PRIMARY)
    
    # Decision
    add_flowchart_box(svg, 538, 466, 110, 32, "a > b?", shape="diamond", fill="#FEF3C7", border="#F59E0B")
    
    # Yes branch
    add_connector(svg, 538, 482, 480, 482, "#10B981")
    add_text(svg, 505, 475, "Да", size=10, fill="#10B981", weight="bold")
    add_flowchart_box(svg, 420, 505, 80, 26, "max = a", shape="rect", fill=PRIMARY_LIGHT, border=PRIMARY)
    
    # No branch
    add_connector(svg, 648, 482, 700, 482, "#EF4444")
    add_text(svg, 665, 475, "Нет", size=10, fill="#EF4444", weight="bold")
    add_flowchart_box(svg, 665, 505, 80, 26, "max = b", shape="rect", fill=PRIMARY_LIGHT, border=PRIMARY)
    
    # Merge
    add_connector(svg, 460, 531, 460, 548, PRIMARY)
    add_connector(svg, 705, 531, 705, 548, PRIMARY)
    add_connector(svg, 460, 548, 593, 548, PRIMARY)
    add_connector(svg, 705, 548, 593, 548, PRIMARY)
    add_connector(svg, 593, 548, 593, 555, PRIMARY)
    
    # Output
    add_flowchart_box(svg, 548, 555, 90, 22, "Вывод max", shape="parallelogram", fill="#ECFDF5", border="#10B981")
    
    return svg


# ============================================================
# LESSON 4: Программирование на языке Python
# ============================================================
def generate_lesson4():
    svg = svg_root()
    add_bg(svg)
    add_title(svg, "Урок 4: Программирование на Python")
    
    # Python logo area
    r = ET.SubElement(svg, "rect")
    r.set("x", "650"); r.set("y", "64")
    r.set("width", "130"); r.set("height", "32")
    r.set("fill", "#306998"); r.set("rx", "16")
    add_text(svg, 715, 85, "Python 3", size=14, fill=WHITE, anchor="middle", weight="bold")
    
    # Variables and types
    add_box(svg, 20, 68, 380, 185, "Переменные и типы данных")
    code1 = [
        ("# Объявление переменных", CODE_GREEN),
        ("name = 'Алексей'   # str", CODE_WHITE),
        ("age = 14            # int", CODE_YELLOW),
        ("height = 1.65       # float", CODE_ORANGE),
        ("is_student = True   # bool", CODE_PINK),
        ("", CODE_WHITE),
        ("# Вывод типа", CODE_GREEN),
        ("print(type(age))", CODE_BLUE),
        ("# &lt;class 'int'&gt;", CODE_GREEN),
    ]
    add_code_block(svg, 30, 100, 360, 145, code1)
    
    # Input/Output
    add_box(svg, 410, 68, 370, 185, "Ввод и вывод данных")
    code2 = [
        ("# Ввод данных", CODE_GREEN),
        ("name = input('Имя: ')", CODE_BLUE),
        ("age = int(input('Возраст: '))", CODE_YELLOW),
        ("", CODE_WHITE),
        ("# Вывод данных", CODE_GREEN),
        ("print('Привет,', name)", CODE_WHITE),
        ("print(f'Тебе {age} лет')", CODE_PINK),
        ("", CODE_WHITE),
        ("# Форматированный вывод", CODE_GREEN),
        ("pi = 3.14159", CODE_WHITE),
        ("print(f'pi = {pi:.2f}')", CODE_PINK),
    ]
    add_code_block(svg, 420, 100, 350, 145, code2)
    
    # Arithmetic operations
    add_box(svg, 20, 266, 380, 155, "Арифметические операции")
    ops = [
        ("+ ", "Сложение", "3 + 2 = 5"),
        ("- ", "Вычитание", "7 - 4 = 3"),
        ("* ", "Умножение", "3 * 4 = 12"),
        ("/ ", "Деление", "10 / 3 = 3.33"),
        ("//", "Целочисл. деление", "10 // 3 = 3"),
        ("% ", "Остаток", "10 % 3 = 1"),
        ("**", "Степень", "2 ** 3 = 8"),
    ]
    for i, (op, name, ex) in enumerate(ops):
        yy = 310 + i * 18
        add_text(svg, 35, yy, op, size=11, fill=PRIMARY_DARK, weight="bold", family="Consolas, monospace")
        add_text(svg, 65, yy, name, size=10, fill=DARK)
        add_text(svg, 210, yy, ex, size=10, fill=GRAY, family="Consolas, monospace")
    
    # Basic syntax
    add_box(svg, 410, 266, 370, 155, "Основной синтаксис")
    code3 = [
        ("# Комментарий", CODE_GREEN),
        ("", CODE_WHITE),
        ('&quot;&quot;&quot;Многострочный', CODE_ORANGE),
        ('комментарий&quot;&quot;&quot;', CODE_ORANGE),
        ("", CODE_WHITE),
        ("# Множественное присваивание", CODE_GREEN),
        ("x, y, z = 1, 2, 3", CODE_WHITE),
        ("a = b = c = 0", CODE_WHITE),
        ("", CODE_WHITE),
        ("# Обмен значений", CODE_GREEN),
        ("x, y = y, x", CODE_PINK),
    ]
    add_code_block(svg, 420, 298, 350, 115, code3)
    
    # Simple program example
    add_box(svg, 20, 434, 760, 155, "Пример программы: Калькулятор")
    code4 = [
        ("# Программа-калькулятор", CODE_GREEN),
        ("a = float(input('Введите первое число: '))", CODE_BLUE),
        ("b = float(input('Введите второе число: '))", CODE_BLUE),
        ("print(f'Сумма: {a + b}')", CODE_YELLOW),
        ("print(f'Разность: {a - b}')", CODE_YELLOW),
        ("print(f'Произведение: {a * b}')", CODE_YELLOW),
        ("print(f'Частное: {a / b:.2f}')", CODE_PINK),
    ]
    add_code_block(svg, 30, 466, 740, 115, code4)
    
    return svg


# ============================================================
# LESSON 5: Алгоритмические конструкции в Python
# ============================================================
def generate_lesson5():
    svg = svg_root()
    add_bg(svg)
    add_title(svg, "Урок 5: Алгоритмические конструкции")
    
    # Three main constructs overview
    constructs = [
        ("Следование", "#0EA5E9", 20),
        ("Ветвление", "#F59E0B", 275),
        ("Цикл", "#10B981", 530),
    ]
    for name, color, x in constructs:
        r = ET.SubElement(svg, "rect")
        r.set("x", str(x)); r.set("y", "64")
        r.set("width", "240"); r.set("height", "28")
        r.set("fill", color); r.set("rx", "14")
        add_text(svg, x + 120, 83, name, size=13, fill=WHITE, anchor="middle", weight="bold")
    
    # Sequence
    add_box(svg, 20, 96, 240, 150)
    add_text(svg, 35, 118, "Следование (линейный)", size=11, fill=PRIMARY_DARK, weight="bold")
    code_seq = [
        ("x = 5", CODE_WHITE),
        ("y = x * 2", CODE_YELLOW),
        ("z = y + 3", CODE_YELLOW),
        ("print(z)  # 13", CODE_GREEN),
    ]
    add_code_block(svg, 30, 128, 220, 108, code_seq)
    
    # Branching
    add_box(svg, 275, 96, 240, 150)
    add_text(svg, 290, 118, "Ветвление (if/else)", size=11, fill="#92400E", weight="bold")
    code_if = [
        ("age = int(input())", CODE_BLUE),
        ("if age >= 18:", CODE_PINK),
        ("    print('Взрослый')", CODE_YELLOW),
        ("elif age >= 14:", CODE_PINK),
        ("    print('Подросток')", CODE_YELLOW),
        ("else:", CODE_PINK),
        ("    print('Ребёнок')", CODE_YELLOW),
    ]
    add_code_block(svg, 285, 128, 220, 108, code_if)
    
    # Loops
    add_box(svg, 530, 96, 250, 150)
    add_text(svg, 545, 118, "Циклы (for / while)", size=11, fill="#065F46", weight="bold")
    code_loop = [
        ("# Цикл for", CODE_GREEN),
        ("for i in range(5):", CODE_PINK),
        ("    print(i)  # 0-4", CODE_YELLOW),
        ("", CODE_WHITE),
        ("# Цикл while", CODE_GREEN),
        ("n = 1", CODE_WHITE),
        ("while n &lt;= 10:", CODE_PINK),
        ("    print(n)", CODE_YELLOW),
        ("    n += 1", CODE_ORANGE),
    ]
    add_code_block(svg, 540, 128, 230, 108, code_loop)
    
    # Flowchart for if/else
    add_box(svg, 20, 260, 380, 326, "Блок-схема: ветвление")
    
    # Start
    add_flowchart_box(svg, 145, 296, 90, 24, "Начало", shape="rounded", fill=PRIMARY_LIGHT, border=PRIMARY)
    add_connector(svg, 190, 320, 190, 332, PRIMARY)
    
    # Input
    add_flowchart_box(svg, 140, 332, 100, 24, "Ввод x", shape="parallelogram", fill="#ECFDF5", border="#10B981")
    add_connector(svg, 190, 356, 190, 368, PRIMARY)
    
    # Decision
    add_flowchart_box(svg, 130, 368, 120, 32, "x > 0?", shape="diamond", fill="#FEF3C7", border="#F59E0B")
    
    # Yes
    add_connector(svg, 130, 384, 75, 384, "#10B981")
    add_text(svg, 95, 377, "Да", size=9, fill="#10B981", weight="bold")
    add_flowchart_box(svg, 32, 398, 85, 24, "y = x * 2", shape="rect", fill=PRIMARY_LIGHT, border=PRIMARY)
    
    # No
    add_connector(svg, 250, 384, 305, 384, "#EF4444")
    add_text(svg, 270, 377, "Нет", size=9, fill="#EF4444", weight="bold")
    add_flowchart_box(svg, 268, 398, 85, 24, "y = -x", shape="rect", fill=PRIMARY_LIGHT, border=PRIMARY)
    
    # Merge
    add_connector(svg, 74, 422, 74, 442, PRIMARY)
    add_connector(svg, 310, 422, 310, 442, PRIMARY)
    add_connector(svg, 74, 442, 190, 442, PRIMARY)
    add_connector(svg, 310, 442, 190, 442, PRIMARY)
    add_connector(svg, 190, 442, 190, 450, PRIMARY)
    
    # Output
    add_flowchart_box(svg, 140, 450, 100, 24, "Вывод y", shape="parallelogram", fill="#ECFDF5", border="#10B981")
    add_connector(svg, 190, 474, 190, 486, PRIMARY)
    
    # End
    add_flowchart_box(svg, 150, 486, 80, 24, "Конец", shape="rounded", fill=PRIMARY_LIGHT, border=PRIMARY)
    
    # Flowchart for while loop
    add_box(svg, 410, 260, 370, 326, "Блок-схема: цикл while")
    
    # Start
    add_flowchart_box(svg, 545, 296, 90, 24, "i = 1", shape="rect", fill=PRIMARY_LIGHT, border=PRIMARY)
    add_connector(svg, 590, 320, 590, 334, PRIMARY)
    
    # Condition
    add_flowchart_box(svg, 530, 334, 120, 36, "i &lt;= 5?", shape="diamond", fill="#FEF3C7", border="#F59E0B")
    
    # Yes - body
    add_connector(svg, 590, 370, 590, 384, "#10B981")
    add_text(svg, 598, 378, "Да", size=9, fill="#10B981", weight="bold")
    add_flowchart_box(svg, 540, 384, 100, 24, "print(i)", shape="rect", fill=PRIMARY_LIGHT, border=PRIMARY)
    add_connector(svg, 590, 408, 590, 420, PRIMARY)
    add_flowchart_box(svg, 540, 420, 100, 24, "i = i + 1", shape="rect", fill=PRIMARY_LIGHT, border=PRIMARY)
    
    # Loop back arrow
    add_connector(svg, 540, 432, 480, 432, PRIMARY)
    # Vertical line going up
    l = ET.SubElement(svg, "line")
    l.set("x1", "480"); l.set("y1", "432")
    l.set("x2", "480"); l.set("y2", "352")
    l.set("stroke", PRIMARY); l.set("stroke-width", "2")
    add_connector(svg, 480, 352, 530, 352, PRIMARY)
    
    # No exit
    add_connector(svg, 650, 352, 720, 352, "#EF4444")
    add_text(svg, 668, 345, "Нет", size=9, fill="#EF4444", weight="bold")
    add_flowchart_box(svg, 700, 340, 70, 24, "Конец", shape="rounded", fill=PRIMARY_LIGHT, border=PRIMARY)
    
    # Python code for the while example
    code_while = [
        ("i = 1", CODE_WHITE),
        ("while i &lt;= 5:", CODE_PINK),
        ("    print(i)", CODE_YELLOW),
        ("    i += 1", CODE_ORANGE),
        ("# Вывод: 1 2 3 4 5", CODE_GREEN),
    ]
    add_code_block(svg, 460, 460, 270, 110, code_while)
    
    return svg


# ============================================================
# LESSON 6: Обработка данных
# ============================================================
def generate_lesson6():
    svg = svg_root()
    add_bg(svg)
    add_title(svg, "Урок 6: Обработка данных")
    
    # Lists
    add_box(svg, 20, 68, 380, 180, "Списки (list)")
    code_list = [
        ("# Создание списка", CODE_GREEN),
        ("numbers = [5, 3, 8, 1, 9]", CODE_WHITE),
        ("names = ['Анна', 'Борис']", CODE_WHITE),
        ("", CODE_WHITE),
        ("# Операции со списками", CODE_GREEN),
        ("numbers.append(7)   # добавить", CODE_YELLOW),
        ("numbers.sort()      # сортировка", CODE_YELLOW),
        ("numbers.reverse()   # реверс", CODE_YELLOW),
        ("len(numbers)        # длина", CODE_BLUE),
        ("numbers[0]          # 1-й элем.", CODE_PINK),
    ]
    add_code_block(svg, 30, 100, 360, 140, code_list)
    
    # Data table
    add_box(svg, 410, 68, 370, 180, "Таблицы данных")
    # Draw a simple table
    headers = ["Имя", "Оценка", "Предмет"]
    data = [
        ["Алексей", "5", "Информатика"],
        ["Мария", "4", "Математика"],
        ["Дмитрий", "5", "Физика"],
    ]
    col_widths = [110, 80, 130]
    x_start = 425
    y_start = 105
    row_h = 22
    
    # Header
    cx = x_start
    for j, h in enumerate(headers):
        r = ET.SubElement(svg, "rect")
        r.set("x", str(cx)); r.set("y", str(y_start))
        r.set("width", str(col_widths[j])); r.set("height", str(row_h))
        r.set("fill", PRIMARY_DARK)
        add_text(svg, cx + col_widths[j] // 2, y_start + 15, h, size=11, fill=WHITE, anchor="middle", weight="bold")
        cx += col_widths[j]
    
    # Data rows
    for i, row in enumerate(data):
        cx = x_start
        yy = y_start + (i + 1) * row_h
        for j, val in enumerate(row):
            r = ET.SubElement(svg, "rect")
            r.set("x", str(cx)); r.set("y", str(yy))
            r.set("width", str(col_widths[j])); r.set("height", str(row_h))
            r.set("fill", PRIMARY_LIGHT if i % 2 == 0 else WHITE)
            r.set("stroke", BOX_BORDER); r.set("stroke-width", "1")
            add_text(svg, cx + col_widths[j] // 2, yy + 15, val, size=11, fill=DARK, anchor="middle")
            cx += col_widths[j]
    
    add_text(svg, 425, 200, "Представление данных в виде таблиц", size=10, fill=GRAY)
    
    # Sorting algorithms
    add_box(svg, 20, 260, 380, 175, "Сортировка")
    code_sort = [
        ("# Сортировка пузырьком", CODE_GREEN),
        ("arr = [64, 34, 25, 12, 22]", CODE_WHITE),
        ("n = len(arr)", CODE_WHITE),
        ("for i in range(n):", CODE_PINK),
        ("    for j in range(n-i-1):", CODE_PINK),
        ("        if arr[j] > arr[j+1]:", CODE_YELLOW),
        ("            arr[j], arr[j+1] =", CODE_ORANGE),
        ("                arr[j+1], arr[j]", CODE_ORANGE),
        ("print(arr)  # [12,22,25,34,64]", CODE_GREEN),
    ]
    add_code_block(svg, 30, 292, 360, 135, code_sort)
    
    # Searching
    add_box(svg, 410, 260, 370, 175, "Поиск")
    code_search = [
        ("# Линейный поиск", CODE_GREEN),
        ("def linear_search(arr, x):", CODE_BLUE),
        ("    for i in range(len(arr)):", CODE_PINK),
        ("        if arr[i] == x:", CODE_YELLOW),
        ("            return i", CODE_ORANGE),
        ("    return -1", CODE_ORANGE),
        ("", CODE_WHITE),
        ("# Бинарный поиск", CODE_GREEN),
        ("# (только для отсортированных)", CODE_GREEN),
        ("# Используйте bisect module", CODE_GREEN),
    ]
    add_code_block(svg, 420, 292, 350, 135, code_search)
    
    # Sorting visualization
    add_box(svg, 20, 447, 380, 142, "Визуализация сортировки")
    # Draw bar chart showing sorted state
    values = [12, 22, 25, 34, 64]
    max_val = 64
    bar_w = 40
    bar_gap = 15
    base_y = 568
    max_bar_h = 90
    
    for i, v in enumerate(values):
        bar_h = int(v / max_val * max_bar_h)
        bx = 45 + i * (bar_w + bar_gap)
        by = base_y - bar_h
        
        r = ET.SubElement(svg, "rect")
        r.set("x", str(bx)); r.set("y", str(by))
        r.set("width", str(bar_w)); r.set("height", str(bar_h))
        colors = ["#BAE6FD", "#7DD3FC", "#38BDF8", "#0EA5E9", "#0284C7"]
        r.set("fill", colors[i]); r.set("rx", "3")
        
        add_text(svg, bx + bar_w // 2, by - 5, str(v), size=10, fill=DARK, anchor="middle", weight="bold")
        add_text(svg, bx + bar_w // 2, base_y + 14, f"[{i}]", size=9, fill=GRAY, anchor="middle")
    
    # Data analysis
    add_box(svg, 410, 447, 370, 142, "Анализ данных")
    code_analysis = [
        ("data = [4, 8, 6, 5, 3, 9, 7]", CODE_WHITE),
        ("", CODE_WHITE),
        ("print(min(data))  # 3", CODE_GREEN),
        ("print(max(data))  # 9", CODE_GREEN),
        ("print(sum(data))  # 42", CODE_GREEN),
        ("avg = sum(data)/len(data)", CODE_YELLOW),
        ("print(f'Среднее: {avg:.1f}')", CODE_PINK),
        ("# Среднее: 6.0", CODE_GREEN),
    ]
    add_code_block(svg, 420, 479, 350, 102, code_analysis)
    
    return svg


# ============================================================
# Main
# ============================================================
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    generators = [
        (1, generate_lesson1),
        (2, generate_lesson2),
        (3, generate_lesson3),
        (4, generate_lesson4),
        (5, generate_lesson5),
        (6, generate_lesson6),
    ]
    
    results = []
    for num, gen_func in generators:
        svg = gen_func()
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
        
        # Write SVG
        tree = ET.ElementTree(svg)
        ET.indent(tree, space="  ")
        tree.write(filepath, encoding="unicode", xml_declaration=True)
        
        # Validate
        try:
            tree2 = ET.parse(filepath)
            root = tree2.getroot()
            size = os.path.getsize(filepath)
            results.append(f"  lesson-{num}.svg - VALID XML, {size} bytes")
        except ET.ParseError as e:
            results.append(f"  lesson-{num}.svg - INVALID: {e}")
    
    print("=" * 60)
    print("Grade 8 Informatics SVG Generation Results")
    print("=" * 60)
    for r in results:
        print(r)
    print(f"\nOutput directory: {OUTPUT_DIR}")
    print("Done!")


if __name__ == "__main__":
    main()
