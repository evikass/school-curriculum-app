#!/usr/bin/env python3
"""Generate Grade 8 Music SVG images for lessons 1-8."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/music"
W, H = 800, 600

# Color scheme
PRIMARY = "#7C3AED"
PRIMARY_LIGHT = "#A78BFA"
PRIMARY_DARK = "#5B21B6"
ACCENT = "#EDE9FE"
ACCENT2 = "#DDD6FE"
BG = "#F5F3FF"
WHITE = "#FFFFFF"
DARK = "#1E1B4B"
TEXT = "#3B0764"
LIGHT_TEXT = "#6D28D9"
BORDER = "#C4B5FD"
GOLD = "#F59E0B"
ROSE = "#F43F5E"
EMERALD = "#10B981"
SKY = "#0EA5E9"
ORANGE = "#F97316"

def escape(text):
    """Escape XML special characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def make_svg():
    svg = ET.Element("svg")
    svg.set("xmlns", "http://www.w3.org/2000/svg")
    svg.set("width", str(W))
    svg.set("height", str(H))
    svg.set("viewBox", f"0 0 {W} {H}")
    return svg

def add_bg(svg, color=BG):
    rect = ET.SubElement(svg, "rect")
    rect.set("width", str(W))
    rect.set("height", str(H))
    rect.set("fill", color)
    rect.set("rx", "0")

def add_header(svg, title, subtitle="", y_offset=0):
    """Add decorative header with title."""
    # Header background
    header = ET.SubElement(svg, "rect")
    header.set("x", "0")
    header.set("y", str(0 + y_offset))
    header.set("width", str(W))
    header.set("height", "80")
    header.set("fill", PRIMARY)
    
    # Decorative line under header
    line = ET.SubElement(svg, "rect")
    line.set("x", "0")
    line.set("y", str(80 + y_offset))
    line.set("width", str(W))
    line.set("height", "4")
    line.set("fill", PRIMARY_DARK)
    
    # Lesson number badge
    badge = ET.SubElement(svg, "rect")
    badge.set("x", "20")
    badge.set("y", str(15 + y_offset))
    badge.set("width", "50")
    badge.set("height", "50")
    badge.set("rx", "12")
    badge.set("fill", PRIMARY_DARK)
    
    # Music note icon in badge
    note = ET.SubElement(svg, "text")
    note.set("x", "45")
    note.set("y", str(50 + y_offset))
    note.set("text-anchor", "middle")
    note.set("font-size", "28")
    note.set("fill", WHITE)
    note.text = "\u266B"
    
    # Title
    t = ET.SubElement(svg, "text")
    t.set("x", "85")
    t.set("y", str(42 + y_offset))
    t.set("font-size", "24")
    t.set("font-weight", "bold")
    t.set("fill", WHITE)
    t.text = escape(title)
    
    if subtitle:
        s = ET.SubElement(svg, "text")
        s.set("x", "85")
        s.set("y", str(64 + y_offset))
        s.set("font-size", "13")
        s.set("fill", ACCENT)
        s.text = escape(subtitle)

def add_footer(svg):
    """Add decorative footer with music symbols."""
    footer = ET.SubElement(svg, "rect")
    footer.set("x", "0")
    footer.set("y", str(H - 30))
    footer.set("width", str(W))
    footer.set("height", "30")
    footer.set("fill", PRIMARY_DARK)
    
    symbols = ["\u266A", "\u266B", "\u266C", "\u2669", "\u266A", "\u266B", "\u266C", "\u2669", "\u266A", "\u266B"]
    for i, sym in enumerate(symbols):
        t = ET.SubElement(svg, "text")
        t.set("x", str(40 + i * 80))
        t.set("y", str(H - 8))
        t.set("text-anchor", "middle")
        t.set("font-size", "14")
        t.set("fill", PRIMARY_LIGHT)
        t.text = sym

def add_decorative_notes(svg, positions=None):
    """Add floating musical notes as decoration."""
    if positions is None:
        positions = [(720, 120, 20), (750, 180, 16), (690, 160, 14), (30, 530, 18), (60, 560, 14)]
    for x, y, size in positions:
        t = ET.SubElement(svg, "text")
        t.set("x", str(x))
        t.set("y", str(y))
        t.set("font-size", str(size))
        t.set("fill", BORDER)
        t.set("opacity", "0.5")
        notes = ["\u266A", "\u266B", "\u266C", "\u2669"]
        t.text = notes[hash((x, y)) % 4]

def add_staff_lines(svg, x, y, width=120, line_gap=8):
    """Draw 5 staff lines."""
    group = ET.SubElement(svg, "g")
    group.set("opacity", "0.15")
    for i in range(5):
        line = ET.SubElement(group, "line")
        line.set("x1", str(x))
        line.set("y1", str(y + i * line_gap))
        line.set("x2", str(x + width))
        line.set("y2", str(y + i * line_gap))
        line.set("stroke", PRIMARY)
        line.set("stroke-width", "1.5")

def add_treble_clef(svg, x, y, size=40):
    """Add a treble clef symbol."""
    t = ET.SubElement(svg, "text")
    t.set("x", str(x))
    t.set("y", str(y))
    t.set("font-size", str(size))
    t.set("fill", PRIMARY_LIGHT)
    t.set("opacity", "0.3")
    t.text = "\uD834\uDD1E"

def add_info_box(svg, x, y, w, h, title, items, color=PRIMARY, text_color=WHITE):
    """Add a colored info box with title and bullet items."""
    # Box
    rect = ET.SubElement(svg, "rect")
    rect.set("x", str(x))
    rect.set("y", str(y))
    rect.set("width", str(w))
    rect.set("height", str(h))
    rect.set("rx", "10")
    rect.set("fill", color)
    rect.set("opacity", "0.9")
    
    # Title
    t = ET.SubElement(svg, "text")
    t.set("x", str(x + 12))
    t.set("y", str(y + 22))
    t.set("font-size", "14")
    t.set("font-weight", "bold")
    t.set("fill", WHITE)
    t.text = escape(title)
    
    # Items
    for i, item in enumerate(items):
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + 18))
        t.set("y", str(y + 40 + i * 18))
        t.set("font-size", "11")
        t.set("fill", WHITE)
        t.text = "\u2022 " + escape(item)

def add_card(svg, x, y, w, h, title, content_lines, color=ACCENT, border_color=PRIMARY):
    """Add a card-style box with title and content."""
    # Shadow
    shadow = ET.SubElement(svg, "rect")
    shadow.set("x", str(x + 3))
    shadow.set("y", str(y + 3))
    shadow.set("width", str(w))
    shadow.set("height", str(h))
    shadow.set("rx", "10")
    shadow.set("fill", "#E0E0E0")
    shadow.set("opacity", "0.3")
    
    # Card background
    rect = ET.SubElement(svg, "rect")
    rect.set("x", str(x))
    rect.set("y", str(y))
    rect.set("width", str(w))
    rect.set("height", str(h))
    rect.set("rx", "10")
    rect.set("fill", color)
    rect.set("stroke", border_color)
    rect.set("stroke-width", "2")
    
    # Title bar
    title_bar = ET.SubElement(svg, "rect")
    title_bar.set("x", str(x))
    title_bar.set("y", str(y))
    title_bar.set("width", str(w))
    title_bar.set("height", "28")
    title_bar.set("rx", "10")
    title_bar.set("fill", border_color)
    # Cover bottom corners of title bar
    cover = ET.SubElement(svg, "rect")
    cover.set("x", str(x))
    cover.set("y", str(y + 18))
    cover.set("width", str(w))
    cover.set("height", "10")
    cover.set("fill", border_color)
    
    # Title text
    t = ET.SubElement(svg, "text")
    t.set("x", str(x + w // 2))
    t.set("y", str(y + 20))
    t.set("text-anchor", "middle")
    t.set("font-size", "13")
    t.set("font-weight", "bold")
    t.set("fill", WHITE)
    t.text = escape(title)
    
    # Content
    for i, line in enumerate(content_lines):
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + 10))
        t.set("y", str(y + 44 + i * 16))
        t.set("font-size", "11")
        t.set("fill", TEXT)
        t.text = escape(line)


# ===== LESSON 1: Музыкальные жанры =====
def generate_lesson1():
    svg = make_svg()
    add_bg(svg)
    add_header(svg, "Музыкальные жанры", "Классификация и характеристика основных жанров музыки")
    add_footer(svg)
    add_decorative_notes(svg)
    
    # Decorative staff lines
    add_staff_lines(svg, 600, 100, 160)
    add_staff_lines(svg, 20, 490, 140)
    
    # Genre cards - 5 main genres
    genres = [
        ("Классика", PRIMARY_DARK, [
            "Симфонии, концерты, сонаты",
            "Сложная форма и структура",
            "Бах, Моцарт, Бетховен",
            "Оркестровое исполнение"
        ]),
        ("Народная", EMERALD, [
            "Традиции поколений",
            "Песни, былины, частушки",
            "Передаётся устно",
            "Национальный колорит"
        ]),
        ("Поп", ROSE, [
            "Массовая популярность",
            "Простой запоминающийся мотив",
            "Эстрадное исполнение",
            "Ритм и танцевальность"
        ]),
        ("Джаз", GOLD, [
            "Импровизация — основа",
            "Синкопированный ритм",
            "Блюзовые интонации",
            "Нью-Орлеан, 1900-е"
        ]),
        ("Рок", "#6366F1", [
            "Электрогитары и барабаны",
            "Энергичный ритм",
            "Рок-группы (ансамбль)",
            "От рок-н-ролла до металла"
        ]),
    ]
    
    card_w = 140
    card_h = 130
    start_x = 30
    start_y = 100
    gap = 14
    
    for i, (name, color, items) in enumerate(genres):
        x = start_x + i * (card_w + gap)
        y = start_y
        
        # Card
        rect = ET.SubElement(svg, "rect")
        rect.set("x", str(x))
        rect.set("y", str(y))
        rect.set("width", str(card_w))
        rect.set("height", str(card_h))
        rect.set("rx", "10")
        rect.set("fill", WHITE)
        rect.set("stroke", color)
        rect.set("stroke-width", "2")
        
        # Color top bar
        bar = ET.SubElement(svg, "rect")
        bar.set("x", str(x))
        bar.set("y", str(y))
        bar.set("width", str(card_w))
        bar.set("height", "30")
        bar.set("rx", "10")
        bar.set("fill", color)
        cover = ET.SubElement(svg, "rect")
        cover.set("x", str(x))
        cover.set("y", str(y + 20))
        cover.set("width", str(card_w))
        cover.set("height", "10")
        cover.set("fill", color)
        
        # Genre name
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + card_w // 2))
        t.set("y", str(y + 22))
        t.set("text-anchor", "middle")
        t.set("font-size", "13")
        t.set("font-weight", "bold")
        t.set("fill", WHITE)
        t.text = escape(name)
        
        # Items
        for j, item in enumerate(items):
            t = ET.SubElement(svg, "text")
            t.set("x", str(x + 8))
            t.set("y", str(y + 46 + j * 22))
            t.set("font-size", "10")
            t.set("fill", TEXT)
            t.text = "\u2022 " + escape(item)
    
    # Comparison table
    table_y = 250
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", str(table_y))
    t.set("text-anchor", "middle")
    t.set("font-size", "16")
    t.set("font-weight", "bold")
    t.set("fill", PRIMARY)
    t.text = "Сравнительная характеристика жанров"
    
    # Table header
    headers = ["Жанр", "Происхождение", "Главная черта", "Инструменты"]
    cols = [100, 210, 350, 530]
    col_w = [110, 140, 180, 230]
    
    th_y = table_y + 20
    header_bg = ET.SubElement(svg, "rect")
    header_bg.set("x", "30")
    header_bg.set("y", str(th_y))
    header_bg.set("width", "740")
    header_bg.set("height", "24")
    header_bg.set("rx", "5")
    header_bg.set("fill", PRIMARY)
    
    for i, h in enumerate(headers):
        t = ET.SubElement(svg, "text")
        t.set("x", str(cols[i] + 8))
        t.set("y", str(th_y + 17))
        t.set("font-size", "11")
        t.set("font-weight", "bold")
        t.set("fill", WHITE)
        t.text = escape(h)
    
    # Table rows
    rows = [
        ["Классика", "Европа, XVI-XIX вв.", "Сложная форма", "Оркестр, фортепиано"],
        ["Народная", "Древние традиции", "Устная передача", "Балалайка, гусли"],
        ["Поп", "США, 1950-е", "Запоминаемость", "Синтезатор, гитара"],
        ["Джаз", "США, Нов. Орлеан", "Импровизация", "Саксофон, труба"],
        ["Рок", "США/UK, 1960-е", "Энергия ритма", "Электрогитара, барабаны"],
    ]
    
    for r, row in enumerate(rows):
        row_y = th_y + 24 + r * 28
        # Alternating row bg
        if r % 2 == 0:
            rb = ET.SubElement(svg, "rect")
            rb.set("x", "30")
            rb.set("y", str(row_y))
            rb.set("width", "740")
            rb.set("height", "28")
            rb.set("fill", ACCENT)
            rb.set("opacity", "0.5")
        
        for c, cell in enumerate(row):
            t = ET.SubElement(svg, "text")
            t.set("x", str(cols[c] + 8))
            t.set("y", str(row_y + 19))
            t.set("font-size", "11")
            t.set("fill", TEXT)
            t.text = escape(cell)
    
    # Table border
    tb = ET.SubElement(svg, "rect")
    tb.set("x", "30")
    tb.set("y", str(th_y))
    tb.set("width", "740")
    tb.set("height", str(24 + len(rows) * 28))
    tb.set("rx", "5")
    tb.set("fill", "none")
    tb.set("stroke", PRIMARY)
    tb.set("stroke-width", "1.5")
    
    # Key concept box
    add_info_box(svg, 30, 440, 740, 50, "Ключевое понятие:", [
        "Музыкальный жанр — исторически сложившееся видовое подразделение музыкальных произведений,"
    ], PRIMARY_DARK)
    
    t = ET.SubElement(svg, "text")
    t.set("x", "48")
    t.set("y", str(476))
    t.set("font-size", "11")
    t.set("fill", WHITE)
    t.text = escape("определяющее его содержание, форму и средства музыкальной выразительности.")
    
    return svg


# ===== LESSON 2: Музыкальные инструменты =====
def generate_lesson2():
    svg = make_svg()
    add_bg(svg)
    add_header(svg, "Музыкальные инструменты", "Классификация и расположение в оркестре")
    add_footer(svg)
    add_decorative_notes(svg)
    
    # Instrument families - 4 main families
    families = [
        ("Струнные", PRIMARY, ["Скрипка", "Альт", "Виолончель", "Контрабас", "Арфа"], "\uD83C\uDFBB"),
        ("Духовые", SKY, ["Флейта", "Кларнет", "Гобой", "Фагот", "Труба", "Валторна"], "\uD83C\uDFBA"),
        ("Ударные", ORANGE, ["Литавры", "Барабан", "Тарелки", "Ксилофон", "Треугольник"], "\uD83E\uDD41"),
        ("Клавишные", EMERALD, ["Фортепиано", "Орган", "Клавесин", "Аккордеон"], "\uD83C\uDFB9"),
    ]
    
    card_w = 180
    card_h = 160
    start_x = 20
    gap = 13
    
    for i, (name, color, instruments, icon) in enumerate(families):
        x = start_x + i * (card_w + gap)
        y = 98
        
        # Card
        rect = ET.SubElement(svg, "rect")
        rect.set("x", str(x))
        rect.set("y", str(y))
        rect.set("width", str(card_w))
        rect.set("height", str(card_h))
        rect.set("rx", "10")
        rect.set("fill", WHITE)
        rect.set("stroke", color)
        rect.set("stroke-width", "2")
        
        # Color header
        hdr = ET.SubElement(svg, "rect")
        hdr.set("x", str(x))
        hdr.set("y", str(y))
        hdr.set("width", str(card_w))
        hdr.set("height", "32")
        hdr.set("rx", "10")
        hdr.set("fill", color)
        cover = ET.SubElement(svg, "rect")
        cover.set("x", str(x))
        cover.set("y", str(y + 22))
        cover.set("width", str(card_w))
        cover.set("height", "10")
        cover.set("fill", color)
        
        # Name
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + card_w // 2))
        t.set("y", str(y + 23))
        t.set("text-anchor", "middle")
        t.set("font-size", "14")
        t.set("font-weight", "bold")
        t.set("fill", WHITE)
        t.text = escape(name)
        
        # Instruments
        for j, inst in enumerate(instruments):
            t = ET.SubElement(svg, "text")
            t.set("x", str(x + 12))
            t.set("y", str(y + 50 + j * 20))
            t.set("font-size", "11")
            t.set("fill", TEXT)
            t.text = "\u266A " + escape(inst)
    
    # Orchestra layout diagram
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", "285")
    t.set("text-anchor", "middle")
    t.set("font-size", "16")
    t.set("font-weight", "bold")
    t.set("fill", PRIMARY)
    t.text = "Схема расположения симфонического оркестра"
    
    # Stage shape (semi-ellipse)
    stage = ET.SubElement(svg, "ellipse")
    stage.set("cx", "400")
    stage.set("cy", "440")
    stage.set("rx", "340")
    stage.set("ry", "120")
    stage.set("fill", ACCENT2)
    stage.set("stroke", PRIMARY)
    stage.set("stroke-width", "2")
    stage.set("opacity", "0.6")
    
    # Conductor position
    cond = ET.SubElement(svg, "circle")
    cond.set("cx", "400")
    cond.set("cy", "370")
    cond.set("r", "15")
    cond.set("fill", PRIMARY)
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", "375")
    t.set("text-anchor", "middle")
    t.set("font-size", "10")
    t.set("fill", WHITE)
    t.text = "\u2669"
    
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", "395")
    t.set("text-anchor", "middle")
    t.set("font-size", "10")
    t.set("font-weight", "bold")
    t.set("fill", PRIMARY_DARK)
    t.text = "Дирижёр"
    
    # Orchestra sections - positioned in semi-circle
    sections = [
        ("Струнные", 200, 410, PRIMARY),
        ("Дерев. дух.", 320, 415, SKY),
        ("Медн. дух.", 480, 415, GOLD),
        ("Ударные", 600, 410, ORANGE),
        ("Клавишные", 400, 440, EMERALD),
    ]
    
    for name, sx, sy, color in sections:
        box = ET.SubElement(svg, "rect")
        box.set("x", str(sx - 40))
        box.set("y", str(sy - 12))
        box.set("width", "80")
        box.set("height", "26")
        box.set("rx", "6")
        box.set("fill", color)
        box.set("opacity", "0.85")
        t = ET.SubElement(svg, "text")
        t.set("x", str(sx))
        t.set("y", str(sy + 5))
        t.set("text-anchor", "middle")
        t.set("font-size", "10")
        t.set("font-weight", "bold")
        t.set("fill", WHITE)
        t.text = escape(name)
    
    # Audience arrow
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", "530")
    t.set("text-anchor", "middle")
    t.set("font-size", "11")
    t.set("fill", PRIMARY)
    t.text = "\u2193 Зрительный зал \u2193"
    
    # Decorative notes
    add_staff_lines(svg, 620, 95, 160, 7)
    
    return svg


# ===== LESSON 3: Русская народная музыка =====
def generate_lesson3():
    svg = make_svg()
    add_bg(svg)
    add_header(svg, "Русская народная музыка", "Традиции, песни и народные инструменты")
    add_footer(svg)
    add_decorative_notes(svg)
    
    # Decorative kokoshnik-inspired pattern at top right
    for i in range(7):
        arc = ET.SubElement(svg, "path")
        d = f"M {640 + i*20} 90 Q {650 + i*20} 80 {660 + i*20} 90"
        arc.set("d", d)
        arc.set("stroke", PRIMARY_LIGHT)
        arc.set("stroke-width", "2")
        arc.set("fill", "none")
        arc.set("opacity", "0.4")
    
    # Folk song types
    song_types = [
        ("Календарные", ["Колядки", "Масленичные", "Троицкие", "Жатвенные"]),
        ("Семейные", ["Колыбельные", "Свадебные", "Плачи", "Причитания"]),
        ("Лирические", ["Любовные", "Раздумья", "Тоска", "Романсы"]),
        ("Эпические", ["Былины", "Исторические", "Богатырские", "Сказы"]),
    ]
    
    add_card(svg, 20, 96, 180, 150, "Календарные песни", song_types[0][1], ACCENT, PRIMARY)
    add_card(svg, 210, 96, 180, 150, "Семейные песни", song_types[1][1], ACCENT, "#C2410C")
    add_card(svg, 400, 96, 180, 150, "Лирические песни", song_types[2][1], ACCENT, ROSE)
    add_card(svg, 590, 96, 190, 150, "Эпические песни", song_types[3][1], ACCENT, "#6366F1")
    
    # Traditional instruments section
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", "275")
    t.set("text-anchor", "middle")
    t.set("font-size", "16")
    t.set("font-weight", "bold")
    t.set("fill", PRIMARY)
    t.text = "Русские народные инструменты"
    
    instruments = [
        ("Балалайка", PRIMARY, [
            "3-струнный щипковый",
            "Треугольный корпус",
            "Символ России",
            "XVIII век"
        ]),
        ("Баян", ROSE, [
            "Клавишный духовой",
            "Правая и левая клавиатуры",
            "Мех для нагнетания воздуха",
            "Назван в честь Баяна"
        ]),
        ("Гусли", GOLD, [
            "Струнный щипковый",
            "Самый древний инструмент",
            "От 15 до 30 струн",
            "Игры Бояна (Слово)"
        ]),
        ("Гармонь", EMERALD, [
            "Духовой клавишный",
            "Ручная гармоника",
            "Русский народный",
            "Тульская, саратовская"
        ]),
    ]
    
    card_w = 185
    for i, (name, color, items) in enumerate(instruments):
        x = 15 + i * (card_w + 8)
        y = 290
        
        rect = ET.SubElement(svg, "rect")
        rect.set("x", str(x))
        rect.set("y", str(y))
        rect.set("width", str(card_w))
        rect.set("height", "130")
        rect.set("rx", "10")
        rect.set("fill", WHITE)
        rect.set("stroke", color)
        rect.set("stroke-width", "2")
        
        # Header
        hdr = ET.SubElement(svg, "rect")
        hdr.set("x", str(x))
        hdr.set("y", str(y))
        hdr.set("width", str(card_w))
        hdr.set("height", "28")
        hdr.set("rx", "10")
        hdr.set("fill", color)
        cover = ET.SubElement(svg, "rect")
        cover.set("x", str(x))
        cover.set("y", str(y + 18))
        cover.set("width", str(card_w))
        cover.set("height", "10")
        cover.set("fill", color)
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + card_w // 2))
        t.set("y", str(y + 20))
        t.set("text-anchor", "middle")
        t.set("font-size", "13")
        t.set("font-weight", "bold")
        t.set("fill", WHITE)
        t.text = escape(name)
        
        for j, item in enumerate(items):
            t = ET.SubElement(svg, "text")
            t.set("x", str(x + 10))
            t.set("y", str(y + 46 + j * 22))
            t.set("font-size", "10")
            t.set("fill", TEXT)
            t.text = "\u2022 " + escape(item)
    
    # Key traditions box
    add_info_box(svg, 20, 440, 760, 55, "Народные традиции:", [
        "Хоровод — круговой танец-песня, сопровождает календарные и семейные обряды",
        "Частушка — короткая ритмичная песенка, выражает настроение и юмор"
    ], PRIMARY_DARK)
    
    # Decorative staff
    add_staff_lines(svg, 20, 510, 140, 7)
    
    return svg


# ===== LESSON 4: Русские композиторы =====
def generate_lesson4():
    svg = make_svg()
    add_bg(svg)
    add_header(svg, "Русские композиторы", "Великая пятёрка и основоположники русской музыки")
    add_footer(svg)
    add_decorative_notes(svg)
    
    # "Mighty Five" section
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", "100")
    t.set("text-anchor", "middle")
    t.set("font-size", "15")
    t.set("font-weight", "bold")
    t.set("fill", PRIMARY)
    t.text = "Могучая кучка"
    
    composers = [
        ("М.И. Глинка", "1804-1857", PRIMARY, [
            "Основоположник",
            "русской классики",
            "\"Иван Сусанин\"",
            "\"Руслан и Людмила\"",
            "\"Камаринская\""
        ]),
        ("М.П. Мусоргский", "1839-1881", SKY, [
            "Реализм в музыке",
            "\"Борис Годунов\"",
            "\"Хованщина\"",
            "\"Картинки с выставки\"",
            "\"Ночь на Лысой горе\""
        ]),
        ("Н.А. Римский-Корсаков", "1844-1908", EMERALD, [
            "Мастер оркестровки",
            "\"Щелкунчик\" — нет",
            "\"Снегурочка\"",
            "\"Шехеразада\"",
            "\"Золотой петушок\""
        ]),
        ("А.П. Бородин", "1833-1887", GOLD, [
            "Учёный-химик",
            "и композитор",
            "\"Князь Игорь\"",
            "\"Половецкие пляски\"",
            "Симфония №2"
        ]),
    ]
    
    card_w = 185
    for i, (name, years, color, works) in enumerate(composers):
        x = 12 + i * (card_w + 8)
        y = 112
        
        rect = ET.SubElement(svg, "rect")
        rect.set("x", str(x))
        rect.set("y", str(y))
        rect.set("width", str(card_w))
        rect.set("height", "180")
        rect.set("rx", "10")
        rect.set("fill", WHITE)
        rect.set("stroke", color)
        rect.set("stroke-width", "2")
        
        # Portrait circle placeholder
        circle = ET.SubElement(svg, "circle")
        circle.set("cx", str(x + card_w // 2))
        circle.set("cy", str(y + 40))
        circle.set("r", "25")
        circle.set("fill", color)
        circle.set("opacity", "0.2")
        circle.set("stroke", color)
        circle.set("stroke-width", "2")
        
        # Note icon in circle
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + card_w // 2))
        t.set("y", str(y + 47))
        t.set("text-anchor", "middle")
        t.set("font-size", "20")
        t.set("fill", color)
        t.text = "\u266B"
        
        # Name
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + card_w // 2))
        t.set("y", str(y + 82))
        t.set("text-anchor", "middle")
        t.set("font-size", "12")
        t.set("font-weight", "bold")
        t.set("fill", TEXT)
        t.text = escape(name)
        
        # Years
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + card_w // 2))
        t.set("y", str(y + 97))
        t.set("text-anchor", "middle")
        t.set("font-size", "10")
        t.set("fill", PRIMARY_LIGHT)
        t.text = escape(years)
        
        # Works
        for j, work in enumerate(works):
            t = ET.SubElement(svg, "text")
            t.set("x", str(x + 10))
            t.set("y", str(y + 115 + j * 14))
            t.set("font-size", "10")
            t.set("fill", TEXT)
            t.text = "\u266A " + escape(work)
    
    # Timeline bar at bottom
    bar_y = 320
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", str(bar_y))
    t.set("text-anchor", "middle")
    t.set("font-size", "14")
    t.set("font-weight", "bold")
    t.set("fill", PRIMARY)
    t.text = "Хронология развития русской музыки"
    
    # Timeline line
    line = ET.SubElement(svg, "line")
    line.set("x1", "40")
    line.set("y1", str(bar_y + 30))
    line.set("x2", "760")
    line.set("y2", str(bar_y + 30))
    line.set("stroke", PRIMARY)
    line.set("stroke-width", "3")
    
    # Timeline events
    events = [
        (80, "1836", "Иван\nСусанин"),
        (200, "1869", "Борис\nГодунов"),
        (340, "1874", "Картинки\nс выставки"),
        (470, "1880", "Шехеразада"),
        (590, "1890", "Князь\nИгорь"),
        (710, "1891", "Пиковая\nдама"),
    ]
    
    for ex, year, label in events:
        # Dot
        dot = ET.SubElement(svg, "circle")
        dot.set("cx", str(ex))
        dot.set("cy", str(bar_y + 30))
        dot.set("r", "6")
        dot.set("fill", PRIMARY)
        
        # Year
        t = ET.SubElement(svg, "text")
        t.set("x", str(ex))
        t.set("y", str(bar_y + 50))
        t.set("text-anchor", "middle")
        t.set("font-size", "10")
        t.set("font-weight", "bold")
        t.set("fill", PRIMARY_DARK)
        t.text = year
        
        # Label
        lines = label.split("\n")
        for li, ln in enumerate(lines):
            t = ET.SubElement(svg, "text")
            t.set("x", str(ex))
            t.set("y", str(bar_y + 64 + li * 13))
            t.set("text-anchor", "middle")
            t.set("font-size", "9")
            t.set("fill", TEXT)
            t.text = escape(ln)
    
    # Additional info box
    add_info_box(svg, 20, 430, 760, 70, "Значение Могучей кучки:", [
        "Группа композиторов (Балакирев, Мусоргский, Римский-Корсаков, Бородин, Кюи)",
        "Цель — создание национальной русской музыки на основе народных традиций",
        "Противопоставление академизму западноевропейской школы"
    ], PRIMARY_DARK)
    
    add_staff_lines(svg, 630, 95, 150, 7)
    
    return svg


# ===== LESSON 5: П.И. Чайковский =====
def generate_lesson5():
    svg = make_svg()
    add_bg(svg)
    add_header(svg, "П.И. Чайковский", "Жизнь и творчество великого композитора")
    add_footer(svg)
    add_decorative_notes(svg)
    
    # Biography section
    bio_y = 98
    
    # Large portrait placeholder
    rect = ET.SubElement(svg, "rect")
    rect.set("x", "20")
    rect.set("y", str(bio_y))
    rect.set("width", "200")
    rect.set("height", "170")
    rect.set("rx", "12")
    rect.set("fill", WHITE)
    rect.set("stroke", PRIMARY)
    rect.set("stroke-width", "2")
    
    # Portrait circle
    circle = ET.SubElement(svg, "circle")
    circle.set("cx", "120")
    circle.set("cy", str(bio_y + 60))
    circle.set("r", "40")
    circle.set("fill", ACCENT2)
    circle.set("stroke", PRIMARY)
    circle.set("stroke-width", "2")
    
    # Icon
    t = ET.SubElement(svg, "text")
    t.set("x", "120")
    t.set("y", str(bio_y + 70))
    t.set("text-anchor", "middle")
    t.set("font-size", "30")
    t.set("fill", PRIMARY)
    t.text = "\u266B"
    
    # Name and dates
    t = ET.SubElement(svg, "text")
    t.set("x", "120")
    t.set("y", str(bio_y + 120))
    t.set("text-anchor", "middle")
    t.set("font-size", "14")
    t.set("font-weight", "bold")
    t.set("fill", TEXT)
    t.text = "Пётр Ильич"
    
    t = ET.SubElement(svg, "text")
    t.set("x", "120")
    t.set("y", str(bio_y + 138))
    t.set("text-anchor", "middle")
    t.set("font-size", "14")
    t.set("font-weight", "bold")
    t.set("fill", TEXT)
    t.text = "Чайковский"
    
    t = ET.SubElement(svg, "text")
    t.set("x", "120")
    t.set("y", str(bio_y + 158))
    t.set("text-anchor", "middle")
    t.set("font-size", "12")
    t.set("fill", PRIMARY)
    t.text = "1840 \u2014 1893"
    
    # Biography facts
    facts = [
        "Родился в Воткинске, Пермская губерния",
        "Окончил Петербургскую консерваторию",
        "Профессор Московской консерватории",
        "Гастролировал в Европе и Америке",
        "Автор 6 симфоний, 3 балетов, 10 опер",
        "Самый исполняемый русский композитор",
    ]
    
    rect2 = ET.SubElement(svg, "rect")
    rect2.set("x", "235")
    rect2.set("y", str(bio_y))
    rect2.set("width", "545")
    rect2.set("height", "170")
    rect2.set("rx", "12")
    rect2.set("fill", WHITE)
    rect2.set("stroke", PRIMARY)
    rect2.set("stroke-width", "2")
    
    # Title
    hdr = ET.SubElement(svg, "rect")
    hdr.set("x", "235")
    hdr.set("y", str(bio_y))
    hdr.set("width", "545")
    hdr.set("height", "28")
    hdr.set("rx", "12")
    hdr.set("fill", PRIMARY)
    cover = ET.SubElement(svg, "rect")
    cover.set("x", "235")
    cover.set("y", str(bio_y + 18))
    cover.set("width", "545")
    cover.set("height", "10")
    cover.set("fill", PRIMARY)
    
    t = ET.SubElement(svg, "text")
    t.set("x", "507")
    t.set("y", str(bio_y + 20))
    t.set("text-anchor", "middle")
    t.set("font-size", "13")
    t.set("font-weight", "bold")
    t.set("fill", WHITE)
    t.text = "Биография"
    
    for i, fact in enumerate(facts):
        t = ET.SubElement(svg, "text")
        t.set("x", "250")
        t.set("y", str(bio_y + 48 + i * 22))
        t.set("font-size", "11")
        t.set("fill", TEXT)
        t.text = "\u266A " + escape(fact)
    
    # Major works
    works_y = 285
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", str(works_y))
    t.set("text-anchor", "middle")
    t.set("font-size", "16")
    t.set("font-weight", "bold")
    t.set("fill", PRIMARY)
    t.text = "Главные произведения"
    
    major_works = [
        ("Лебединое озеро", "Балет, 1876", PRIMARY, "Мечта и реальность, добро и зло\nТанец маленьких лебедей"),
        ("Щелкунчик", "Балет, 1892", ROSE, "Рождественская сказка\nВальс цветов, Танец феи Драже"),
        ("Увертюра 1812 год", "Симфония, 1880", GOLD, "Победа в Отечественной войне\nКолокола и пушечные выстрелы"),
    ]
    
    card_w = 245
    for i, (name, desc, color, details) in enumerate(major_works):
        x = 20 + i * (card_w + 15)
        y = works_y + 15
        
        rect = ET.SubElement(svg, "rect")
        rect.set("x", str(x))
        rect.set("y", str(y))
        rect.set("width", str(card_w))
        rect.set("height", "130")
        rect.set("rx", "10")
        rect.set("fill", WHITE)
        rect.set("stroke", color)
        rect.set("stroke-width", "2")
        
        # Header
        hdr = ET.SubElement(svg, "rect")
        hdr.set("x", str(x))
        hdr.set("y", str(y))
        hdr.set("width", str(card_w))
        hdr.set("height", "30")
        hdr.set("rx", "10")
        hdr.set("fill", color)
        cover = ET.SubElement(svg, "rect")
        cover.set("x", str(x))
        cover.set("y", str(y + 20))
        cover.set("width", str(card_w))
        cover.set("height", "10")
        cover.set("fill", color)
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + card_w // 2))
        t.set("y", str(y + 21))
        t.set("text-anchor", "middle")
        t.set("font-size", "13")
        t.set("font-weight", "bold")
        t.set("fill", WHITE)
        t.text = escape(name)
        
        # Description
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + 12))
        t.set("y", str(y + 50))
        t.set("font-size", "11")
        t.set("fill", PRIMARY_LIGHT)
        t.text = escape(desc)
        
        # Details
        lines = details.split("\n")
        for li, ln in enumerate(lines):
            t = ET.SubElement(svg, "text")
            t.set("x", str(x + 12))
            t.set("y", str(y + 70 + li * 18))
            t.set("font-size", "10")
            t.set("fill", TEXT)
            t.text = "\u2022 " + escape(ln)
    
    # Other works
    add_info_box(svg, 20, 450, 760, 50, "Другие значимые произведения:", [
        "Симфония №6 \"Патетическая\" | Опера \"Евгений Онегин\" | Опера \"Пиковая дама\" | \"Иоланта\" | Концерт для фортепиано №1"
    ], PRIMARY_DARK)
    
    add_staff_lines(svg, 620, 100, 160, 7)
    
    return svg


# ===== LESSON 6: Симфоническая музыка =====
def generate_lesson6():
    svg = make_svg()
    add_bg(svg)
    add_header(svg, "Симфоническая музыка", "Оркестр, структура симфонии и знаменитые произведения")
    add_footer(svg)
    add_decorative_notes(svg)
    
    # Symphony structure
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", "100")
    t.set("text-anchor", "middle")
    t.set("font-size", "15")
    t.set("font-weight", "bold")
    t.set("fill", PRIMARY)
    t.text = "Структура симфонии"
    
    movements = [
        ("I часть", "Allegro", "Сонатная форма", "Экспозиция — Разработка — Реприза", PRIMARY),
        ("II часть", "Andante", "Медленная часть", "Лирический центр, раздумья", PRIMARY_LIGHT),
        ("III часть", "Scherzo", "Скерцо/Менуэт", "Танцевальный характер", GOLD),
        ("IV часть", "Finale", "Финал", "Торжественное завершение", EMERALD),
    ]
    
    card_w = 185
    for i, (num, tempo, form, desc, color) in enumerate(movements):
        x = 12 + i * (card_w + 8)
        y = 112
        
        rect = ET.SubElement(svg, "rect")
        rect.set("x", str(x))
        rect.set("y", str(y))
        rect.set("width", str(card_w))
        rect.set("height", "110")
        rect.set("rx", "10")
        rect.set("fill", WHITE)
        rect.set("stroke", color)
        rect.set("stroke-width", "2")
        
        # Number badge
        badge = ET.SubElement(svg, "rect")
        badge.set("x", str(x + 5))
        badge.set("y", str(y + 5))
        badge.set("width", str(card_w - 10))
        badge.set("height", "24")
        badge.set("rx", "8")
        badge.set("fill", color)
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + card_w // 2))
        t.set("y", str(y + 22))
        t.set("text-anchor", "middle")
        t.set("font-size", "12")
        t.set("font-weight", "bold")
        t.set("fill", WHITE)
        t.text = f"{num}: {tempo}"
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + 10))
        t.set("y", str(y + 48))
        t.set("font-size", "11")
        t.set("font-weight", "bold")
        t.set("fill", TEXT)
        t.text = escape(form)
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + 10))
        t.set("y", str(y + 70))
        t.set("font-size", "10")
        t.set("fill", TEXT)
        # Wrap long text
        words = desc.split()
        line1 = " ".join(words[:len(words)//2 + 1])
        line2 = " ".join(words[len(words)//2 + 1:])
        t.text = escape(line1)
        if line2:
            t2 = ET.SubElement(svg, "text")
            t2.set("x", str(x + 10))
            t2.set("y", str(y + 85))
            t2.set("font-size", "10")
            t2.set("fill", TEXT)
            t2.text = escape(line2)
    
    # Orchestra sections diagram
    orch_y = 248
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", str(orch_y))
    t.set("text-anchor", "middle")
    t.set("font-size", "15")
    t.set("font-weight", "bold")
    t.set("fill", PRIMARY)
    t.text = "Состав симфонического оркестра"
    
    sections = [
        ("Струнные", "~60 музыкантов", "Скрипки, альты,\nвиолончели, контрабасы", PRIMARY),
        ("Деревянные духовые", "~16 музыкантов", "Флейты, гобои,\nкларнеты, фаготы", SKY),
        ("Медные духовые", "~14 музыкантов", "Валторны, трубы,\nтромбоны, туба", GOLD),
        ("Ударные", "~4 музыканта", "Литавры, барабаны,\nтарелки, колокола", ORANGE),
    ]
    
    card_w = 185
    for i, (name, count, instruments, color) in enumerate(sections):
        x = 12 + i * (card_w + 8)
        y = orch_y + 12
        
        rect = ET.SubElement(svg, "rect")
        rect.set("x", str(x))
        rect.set("y", str(y))
        rect.set("width", str(card_w))
        rect.set("height", "100")
        rect.set("rx", "10")
        rect.set("fill", color)
        rect.set("opacity", "0.9")
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + card_w // 2))
        t.set("y", str(y + 22))
        t.set("text-anchor", "middle")
        t.set("font-size", "12")
        t.set("font-weight", "bold")
        t.set("fill", WHITE)
        t.text = escape(name)
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + card_w // 2))
        t.set("y", str(y + 40))
        t.set("text-anchor", "middle")
        t.set("font-size", "10")
        t.set("fill", WHITE)
        t.set("opacity", "0.85")
        t.text = escape(count)
        
        lines = instruments.split("\n")
        for li, ln in enumerate(lines):
            t = ET.SubElement(svg, "text")
            t.set("x", str(x + card_w // 2))
            t.set("y", str(y + 58 + li * 15))
            t.set("text-anchor", "middle")
            t.set("font-size", "10")
            t.set("fill", WHITE)
            t.text = escape(ln)
    
    # Famous symphonies
    famous_y = 380
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", str(famous_y))
    t.set("text-anchor", "middle")
    t.set("font-size", "15")
    t.set("font-weight", "bold")
    t.set("fill", PRIMARY)
    t.text = "Знаменитые симфонии"
    
    symphonies = [
        ("Бетховен", "Симфония №5", "Тема судьбы", PRIMARY),
        ("Бетховен", "Симфония №9", "Ода к радости", PRIMARY_DARK),
        ("Чайковский", "Симфония №6", "Патетическая", ROSE),
        ("Моцарт", "Симфония №40", "Соль минор", SKY),
        ("Дворжак", "Симфония №9", "Из Нового света", EMERALD),
        ("Шостакович", "Симфония №7", "Ленинградская", GOLD),
    ]
    
    cols = 3
    card_w2 = 245
    for i, (comp, sym, nick, color) in enumerate(symphonies):
        row = i // cols
        col = i % cols
        x = 20 + col * (card_w2 + 10)
        y = famous_y + 12 + row * 55
        
        rect = ET.SubElement(svg, "rect")
        rect.set("x", str(x))
        rect.set("y", str(y))
        rect.set("width", str(card_w2))
        rect.set("height", "48")
        rect.set("rx", "8")
        rect.set("fill", WHITE)
        rect.set("stroke", color)
        rect.set("stroke-width", "2")
        
        # Left color bar
        bar = ET.SubElement(svg, "rect")
        bar.set("x", str(x))
        bar.set("y", str(y))
        bar.set("width", "6")
        bar.set("height", "48")
        bar.set("rx", "3")
        bar.set("fill", color)
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + 16))
        t.set("y", str(y + 19))
        t.set("font-size", "11")
        t.set("font-weight", "bold")
        t.set("fill", TEXT)
        t.text = f"{comp}: {sym}"
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + 16))
        t.set("y", str(y + 36))
        t.set("font-size", "10")
        t.set("fill", color)
        t.text = "\u266B " + escape(nick)
    
    add_staff_lines(svg, 620, 98, 160, 7)
    
    return svg


# ===== LESSON 7: Оперное искусство =====
def generate_lesson7():
    svg = make_svg()
    add_bg(svg)
    add_header(svg, "Оперное искусство", "Структура оперы, ария, речитатив, хор и знаменитые оперы")
    add_footer(svg)
    add_decorative_notes(svg)
    
    # Opera structure
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", "100")
    t.set("text-anchor", "middle")
    t.set("font-size", "15")
    t.set("font-weight", "bold")
    t.set("fill", PRIMARY)
    t.text = "Структура оперы"
    
    # Flow diagram: Overture → Acts → Scenes
    elements = [
        ("Увертюра", "Вступление,\nзадаёт настроение", PRIMARY),
        ("Действие", "Акт оперы,\nразвитие сюжета", ROSE),
        ("Ария", "Сольная песня\nгероя", GOLD),
        ("Речитатив", "Пение-речь,\nдиалог", SKY),
        ("Хор", "Массовая\nсцена", EMERALD),
        ("Ансамбль", "Групповое\nпение", "#6366F1"),
    ]
    
    card_w = 120
    for i, (name, desc, color) in enumerate(elements):
        x = 18 + i * (card_w + 8)
        y = 112
        
        rect = ET.SubElement(svg, "rect")
        rect.set("x", str(x))
        rect.set("y", str(y))
        rect.set("width", str(card_w))
        rect.set("height", "95")
        rect.set("rx", "10")
        rect.set("fill", WHITE)
        rect.set("stroke", color)
        rect.set("stroke-width", "2")
        
        # Header
        hdr = ET.SubElement(svg, "rect")
        hdr.set("x", str(x))
        hdr.set("y", str(y))
        hdr.set("width", str(card_w))
        hdr.set("height", "26")
        hdr.set("rx", "10")
        hdr.set("fill", color)
        cover = ET.SubElement(svg, "rect")
        cover.set("x", str(x))
        cover.set("y", str(y + 16))
        cover.set("width", str(card_w))
        cover.set("height", "10")
        cover.set("fill", color)
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + card_w // 2))
        t.set("y", str(y + 19))
        t.set("text-anchor", "middle")
        t.set("font-size", "11")
        t.set("font-weight", "bold")
        t.set("fill", WHITE)
        t.text = escape(name)
        
        lines = desc.split("\n")
        for li, ln in enumerate(lines):
            t = ET.SubElement(svg, "text")
            t.set("x", str(x + card_w // 2))
            t.set("y", str(y + 46 + li * 15))
            t.set("text-anchor", "middle")
            t.set("font-size", "10")
            t.set("fill", TEXT)
            t.text = escape(ln)
        
        # Arrow to next
        if i < len(elements) - 1:
            arrow = ET.SubElement(svg, "text")
            arrow.set("x", str(x + card_w + 1))
            arrow.set("y", str(y + 50))
            arrow.set("font-size", "14")
            arrow.set("fill", PRIMARY_LIGHT)
            arrow.text = "\u25B6"
    
    # Voice types
    voice_y = 230
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", str(voice_y))
    t.set("text-anchor", "middle")
    t.set("font-size", "15")
    t.set("font-weight", "bold")
    t.set("fill", PRIMARY)
    t.text = "Голосовые партии в опере"
    
    voices = [
        ("Сопрано", "Высокий женский", "Царевна-Лебедь, Татьяна", ROSE),
        ("Меццо-сопрано", "Средний женский", "Кармен, Амнерис", "#EC4899"),
        ("Тенор", "Высокий мужской", "Ленский, Германн", SKY),
        ("Баритон", "Средний мужской", "Онегин, Риголетто", PRIMARY),
        ("Бас", "Низкий мужской", "Борис Годунов, Иван Сусанин", PRIMARY_DARK),
    ]
    
    card_w = 150
    for i, (name, desc, roles, color) in enumerate(voices):
        x = 10 + i * (card_w + 6)
        y = voice_y + 10
        
        rect = ET.SubElement(svg, "rect")
        rect.set("x", str(x))
        rect.set("y", str(y))
        rect.set("width", str(card_w))
        rect.set("height", "85")
        rect.set("rx", "8")
        rect.set("fill", color)
        rect.set("opacity", "0.9")
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + card_w // 2))
        t.set("y", str(y + 22))
        t.set("text-anchor", "middle")
        t.set("font-size", "12")
        t.set("font-weight", "bold")
        t.set("fill", WHITE)
        t.text = escape(name)
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + card_w // 2))
        t.set("y", str(y + 40))
        t.set("text-anchor", "middle")
        t.set("font-size", "10")
        t.set("fill", WHITE)
        t.set("opacity", "0.85")
        t.text = escape(desc)
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + card_w // 2))
        t.set("y", str(y + 60))
        t.set("text-anchor", "middle")
        t.set("font-size", "9")
        t.set("fill", WHITE)
        t.set("opacity", "0.8")
        t.text = escape(roles)
    
    # Famous operas
    operas_y = 345
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", str(operas_y))
    t.set("text-anchor", "middle")
    t.set("font-size", "15")
    t.set("font-weight", "bold")
    t.set("fill", PRIMARY)
    t.text = "Знаменитые оперы"
    
    operas = [
        ("Евгений Онегин", "Чайковский", "Лирические сцены", ROSE),
        ("Борис Годунов", "Мусоргский", "Народная драма", PRIMARY),
        ("Князь Игорь", "Бородин", "Эпическая опера", GOLD),
        ("Кармен", "Бизе", "Драма любви", "#EC4899"),
        ("Травиата", "Верди", "Трагедия", ROSE),
        ("Снегурочка", "Римский-Корсаков", "Весенняя сказка", SKY),
    ]
    
    cols = 3
    card_w2 = 245
    for i, (name, comp, desc, color) in enumerate(operas):
        row = i // cols
        col = i % cols
        x = 20 + col * (card_w2 + 10)
        y = operas_y + 12 + row * 55
        
        rect = ET.SubElement(svg, "rect")
        rect.set("x", str(x))
        rect.set("y", str(y))
        rect.set("width", str(card_w2))
        rect.set("height", "48")
        rect.set("rx", "8")
        rect.set("fill", WHITE)
        rect.set("stroke", color)
        rect.set("stroke-width", "2")
        
        bar = ET.SubElement(svg, "rect")
        bar.set("x", str(x))
        bar.set("y", str(y))
        bar.set("width", "6")
        bar.set("height", "48")
        bar.set("rx", "3")
        bar.set("fill", color)
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + 16))
        t.set("y", str(y + 19))
        t.set("font-size", "11")
        t.set("font-weight", "bold")
        t.set("fill", TEXT)
        t.text = f"{name} ({comp})"
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + 16))
        t.set("y", str(y + 36))
        t.set("font-size", "10")
        t.set("fill", color)
        t.text = "\u266B " + escape(desc)
    
    add_staff_lines(svg, 620, 98, 160, 7)
    
    return svg


# ===== LESSON 8: Джаз =====
def generate_lesson8():
    svg = make_svg()
    add_bg(svg)
    add_header(svg, "Джаз", "Происхождение, импровизация, блюз и великие джазмены")
    add_footer(svg)
    add_decorative_notes(svg)
    
    # Jazz origins
    origins_y = 98
    
    rect = ET.SubElement(svg, "rect")
    rect.set("x", "20")
    rect.set("y", str(origins_y))
    rect.set("width", "760")
    rect.set("height", "110")
    rect.set("rx", "10")
    rect.set("fill", WHITE)
    rect.set("stroke", PRIMARY)
    rect.set("stroke-width", "2")
    
    # Header
    hdr = ET.SubElement(svg, "rect")
    hdr.set("x", "20")
    hdr.set("y", str(origins_y))
    hdr.set("width", "760")
    hdr.set("height", "28")
    hdr.set("rx", "10")
    hdr.set("fill", PRIMARY)
    cover = ET.SubElement(svg, "rect")
    cover.set("x", "20")
    cover.set("y", str(origins_y + 18))
    cover.set("width", "760")
    cover.set("height", "10")
    cover.set("fill", PRIMARY)
    
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", str(origins_y + 20))
    t.set("text-anchor", "middle")
    t.set("font-size", "13")
    t.set("font-weight", "bold")
    t.set("fill", WHITE)
    t.text = "Происхождение джаза"
    
    facts = [
        "\u266A Родина — Новый Орлеан (США), конец XIX века",
        "\u266A Слияние африканских ритмов и европейской гармонии",
        "\u266A Афроамериканские духовные гимны (спиричуэлс) и рабочие песни",
        "\u266A Ритмы рэгтайма и блюза — основа джазовой музыки",
    ]
    for i, fact in enumerate(facts):
        t = ET.SubElement(svg, "text")
        t.set("x", "35")
        t.set("y", str(origins_y + 46 + i * 18))
        t.set("font-size", "11")
        t.set("fill", TEXT)
        t.text = escape(fact)
    
    # Jazz elements
    elem_y = 225
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", str(elem_y))
    t.set("text-anchor", "middle")
    t.set("font-size", "15")
    t.set("font-weight", "bold")
    t.set("fill", PRIMARY)
    t.text = "Основные элементы джаза"
    
    elements = [
        ("Импровизация", "Создание музыки\nв момент исполнения,\nсвобода самовыражения", GOLD, "\u266B"),
        ("Синкопа", "Смещение акцента\nсо слабой доли\nна сильную", ROSE, "\u266A"),
        ("Блюз", "12-тактовая форма,\nминорное звучание,\nвыразительность", PRIMARY, "\u2669"),
        ("Свинг", "Особый ритмический\nрисунок, чувство\nпульса музыки", EMERALD, "\u266C"),
    ]
    
    card_w = 185
    for i, (name, desc, color, icon) in enumerate(elements):
        x = 12 + i * (card_w + 8)
        y = elem_y + 12
        
        rect = ET.SubElement(svg, "rect")
        rect.set("x", str(x))
        rect.set("y", str(y))
        rect.set("width", str(card_w))
        rect.set("height", "115")
        rect.set("rx", "10")
        rect.set("fill", WHITE)
        rect.set("stroke", color)
        rect.set("stroke-width", "2")
        
        # Icon circle
        circle = ET.SubElement(svg, "circle")
        circle.set("cx", str(x + card_w // 2))
        circle.set("cy", str(y + 28))
        circle.set("r", "18")
        circle.set("fill", color)
        circle.set("opacity", "0.15")
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + card_w // 2))
        t.set("y", str(y + 35))
        t.set("text-anchor", "middle")
        t.set("font-size", "20")
        t.set("fill", color)
        t.text = icon
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + card_w // 2))
        t.set("y", str(y + 58))
        t.set("text-anchor", "middle")
        t.set("font-size", "12")
        t.set("font-weight", "bold")
        t.set("fill", TEXT)
        t.text = escape(name)
        
        lines = desc.split("\n")
        for li, ln in enumerate(lines):
            t = ET.SubElement(svg, "text")
            t.set("x", str(x + card_w // 2))
            t.set("y", str(y + 74 + li * 14))
            t.set("text-anchor", "middle")
            t.set("font-size", "10")
            t.set("fill", TEXT)
            t.text = escape(ln)
    
    # Jazz styles timeline
    styles_y = 372
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", str(styles_y))
    t.set("text-anchor", "middle")
    t.set("font-size", "15")
    t.set("font-weight", "bold")
    t.set("fill", PRIMARY)
    t.text = "Стили джаза"
    
    styles = [
        ("Нью-Орлеан", "1900-е", PRIMARY),
        ("Свинг", "1930-е", GOLD),
        ("Бибоп", "1940-е", ROSE),
        ("Кул-джаз", "1950-е", SKY),
        ("Фри-джаз", "1960-е", EMERALD),
        ("Фьюжн", "1970-е", ORANGE),
    ]
    
    # Timeline line
    line = ET.SubElement(svg, "line")
    line.set("x1", "40")
    line.set("y1", str(styles_y + 35))
    line.set("x2", "760")
    line.set("y2", str(styles_y + 35))
    line.set("stroke", PRIMARY)
    line.set("stroke-width", "3")
    
    for i, (name, era, color) in enumerate(styles):
        sx = 60 + i * 120
        # Dot
        dot = ET.SubElement(svg, "circle")
        dot.set("cx", str(sx))
        dot.set("cy", str(styles_y + 35))
        dot.set("r", "8")
        dot.set("fill", color)
        
        # Name
        t = ET.SubElement(svg, "text")
        t.set("x", str(sx))
        t.set("y", str(styles_y + 58))
        t.set("text-anchor", "middle")
        t.set("font-size", "10")
        t.set("font-weight", "bold")
        t.set("fill", color)
        t.text = escape(name)
        
        # Era
        t = ET.SubElement(svg, "text")
        t.set("x", str(sx))
        t.set("y", str(styles_y + 72))
        t.set("text-anchor", "middle")
        t.set("font-size", "9")
        t.set("fill", TEXT)
        t.text = era
    
    # Famous jazz musicians
    musicians_y = 465
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", str(musicians_y))
    t.set("text-anchor", "middle")
    t.set("font-size", "15")
    t.set("font-weight", "bold")
    t.set("fill", PRIMARY)
    t.text = "Великие джазовые музыканты"
    
    musicians = [
        ("Л. Армстронг", "Труба", PRIMARY),
        ("Д. Эллингтон", "Фортепиано", GOLD),
        ("Ч. Паркер", "Саксофон", ROSE),
        ("М. Дэвис", "Труба", SKY),
        ("Э. Фицджеральд", "Вокал", EMERALD),
    ]
    
    card_w2 = 145
    for i, (name, inst, color) in enumerate(musicians):
        x = 18 + i * (card_w2 + 8)
        y = musicians_y + 10
        
        rect = ET.SubElement(svg, "rect")
        rect.set("x", str(x))
        rect.set("y", str(y))
        rect.set("width", str(card_w2))
        rect.set("height", "45")
        rect.set("rx", "8")
        rect.set("fill", color)
        rect.set("opacity", "0.9")
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + card_w2 // 2))
        t.set("y", str(y + 20))
        t.set("text-anchor", "middle")
        t.set("font-size", "11")
        t.set("font-weight", "bold")
        t.set("fill", WHITE)
        t.text = escape(name)
        
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + card_w2 // 2))
        t.set("y", str(y + 36))
        t.set("text-anchor", "middle")
        t.set("font-size", "10")
        t.set("fill", WHITE)
        t.set("opacity", "0.85")
        t.text = "\u266A " + escape(inst)
    
    add_staff_lines(svg, 20, 510, 130, 7)
    
    return svg


# ===== MAIN =====
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    generators = [
        (1, generate_lesson1),
        (2, generate_lesson2),
        (3, generate_lesson3),
        (4, generate_lesson4),
        (5, generate_lesson5),
        (6, generate_lesson6),
        (7, generate_lesson7),
        (8, generate_lesson8),
    ]
    
    results = []
    for num, gen_func in generators:
        svg = gen_func()
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
        
        # Write with XML declaration
        tree = ET.ElementTree(svg)
        ET.indent(tree, space="  ")
        
        # Write manually to ensure XML declaration
        xml_str = ET.tostring(svg, encoding="unicode", xml_declaration=False)
        xml_str = '<?xml version="1.0" encoding="UTF-8"?>\n' + xml_str
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(xml_str)
        
        # Validate
        try:
            tree_val = ET.parse(filepath)
            root = tree_val.getroot()
            w = root.get("width")
            h = root.get("height")
            results.append(f"✅ lesson-{num}.svg — valid XML, {w}x{h}")
        except ET.ParseError as e:
            results.append(f"❌ lesson-{num}.svg — INVALID: {e}")
    
    print("=" * 60)
    print("Grade 8 Music SVG Generation Results")
    print("=" * 60)
    for r in results:
        print(r)
    print("=" * 60)
    print(f"Total: {len(results)} files generated in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
