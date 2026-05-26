#!/usr/bin/env python3
"""Generate Grade 7 Robotics lesson SVG images (8 lessons)."""

import os
import xml.etree.ElementTree as ET

OUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/robotics"
W, H = 800, 600

# ── Color palette ──
C_PRIMARY   = "#0284C7"
C_DARK      = "#0C1B2A"
C_CYAN      = "#06B6D4"
C_LIGHT_BG  = "#0F2744"
C_ACCENT    = "#38BDF8"
C_TEXT      = "#E0F2FE"
C_DIM       = "#7DD3FC"
C_ORANGE    = "#F59E0B"
C_GREEN     = "#22C55E"
C_RED       = "#EF4444"
C_PURPLE    = "#A855F7"
C_GRID      = "#164E7A"
C_PANEL     = "#0D2137"
C_BORDER    = "#1E5A8A"
C_CODE_BG   = "#0A1929"


def escape(text: str) -> str:
    """Escape XML special chars."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


# ── Helpers ──
def svg_root():
    root = ET.Element("svg")
    root.set("xmlns", "http://www.w3.org/2000/svg")
    root.set("width", str(W))
    root.set("height", str(H))
    root.set("viewBox", f"0 0 {W} {H}")
    return root


def add_bg(root):
    """Dark gradient background with grid."""
    defs = ET.SubElement(root, "defs")
    lg = ET.SubElement(defs, "linearGradient")
    lg.set("id", "bg"); lg.set("x1", "0"); lg.set("y1", "0"); lg.set("x2", "0"); lg.set("y2", "1")
    s1 = ET.SubElement(lg, "stop"); s1.set("offset", "0%"); s1.set("stop-color", C_DARK)
    s2 = ET.SubElement(lg, "stop"); s2.set("offset", "100%"); s2.set("stop-color", C_LIGHT_BG)
    rect = ET.SubElement(root, "rect")
    rect.set("width", str(W)); rect.set("height", str(H)); rect.set("fill", "url(#bg)")
    # Grid
    for x in range(0, W + 1, 40):
        l = ET.SubElement(root, "line")
        l.set("x1", str(x)); l.set("y1", "0"); l.set("x2", str(x)); l.set("y2", str(H))
        l.set("stroke", C_GRID); l.set("stroke-width", "0.3"); l.set("opacity", "0.5")
    for y in range(0, H + 1, 40):
        l = ET.SubElement(root, "line")
        l.set("x1", "0"); l.set("y1", str(y)); l.set("x2", str(W)); l.set("y2", str(y))
        l.set("stroke", C_GRID); l.set("stroke-width", "0.3"); l.set("opacity", "0.5")


def add_header(root, lesson_num, title, subtitle=""):
    """Top banner with lesson number and title."""
    # Banner bar
    r = ET.SubElement(root, "rect")
    r.set("x", "0"); r.set("y", "0"); r.set("width", str(W)); r.set("height", "70")
    r.set("fill", C_PRIMARY); r.set("opacity", "0.92")
    # Lesson badge
    badge = ET.SubElement(root, "rect")
    badge.set("x", "16"); badge.set("y", "12"); badge.set("width", "46"); badge.set("height", "46")
    badge.set("rx", "8"); badge.set("fill", C_DARK)
    t = ET.SubElement(root, "text")
    t.set("x", "39"); t.set("y", "44"); t.set("text-anchor", "middle")
    t.set("fill", C_CYAN); t.set("font-size", "22"); t.set("font-weight", "bold"); t.set("font-family", "monospace")
    t.text = str(lesson_num)
    # Title
    tt = ET.SubElement(root, "text")
    tt.set("x", "76"); tt.set("y", "38"); tt.set("fill", C_TEXT)
    tt.set("font-size", "22"); tt.set("font-weight", "bold"); tt.set("font-family", "sans-serif")
    tt.text = title
    # Subtitle
    if subtitle:
        st = ET.SubElement(root, "text")
        st.set("x", "76"); st.set("y", "58"); st.set("fill", C_DIM)
        st.set("font-size", "13"); st.set("font-family", "sans-serif")
        st.text = subtitle
    # Decorative line
    ln = ET.SubElement(root, "line")
    ln.set("x1", "0"); ln.set("y1", "70"); ln.set("x2", str(W)); ln.set("y2", "70")
    ln.set("stroke", C_CYAN); ln.set("stroke-width", "2"); ln.set("opacity", "0.6")


def add_panel(root, x, y, w, h, title="", border_color=C_BORDER):
    """Rounded panel with optional title."""
    r = ET.SubElement(root, "rect")
    r.set("x", str(x)); r.set("y", str(y)); r.set("width", str(w)); r.set("height", str(h))
    r.set("rx", "8"); r.set("fill", C_PANEL); r.set("stroke", border_color); r.set("stroke-width", "1")
    if title:
        t = ET.SubElement(root, "text")
        t.set("x", str(x + 12)); t.set("y", str(y + 22)); t.set("fill", C_ACCENT)
        t.set("font-size", "14"); t.set("font-weight", "bold"); t.set("font-family", "sans-serif")
        t.text = title


def add_text(root, x, y, text, size=13, color=C_TEXT, bold=False, font="sans-serif", anchor="start"):
    t = ET.SubElement(root, "text")
    t.set("x", str(x)); t.set("y", str(y)); t.set("fill", color)
    t.set("font-size", str(size)); t.set("font-family", font); t.set("text-anchor", anchor)
    if bold:
        t.set("font-weight", "bold")
    t.text = text
    return t


def add_code_block(root, x, y, w, h, lines, title=""):
    """Code panel with dark background."""
    add_panel(root, x, y, w, h, title=title, border_color=C_CYAN)
    for i, line in enumerate(lines):
        color = C_TEXT
        if line.startswith("//"):
            color = C_DIM
        elif line.startswith("#"):
            color = C_DIM
        add_text(root, x + 10, y + 36 + i * 16, escape(line), size=11, color=color, font="monospace")


def add_icon_circle(root, cx, cy, r, color, label):
    """Circle icon with label inside."""
    c = ET.SubElement(root, "circle")
    c.set("cx", str(cx)); c.set("cy", str(cy)); c.set("r", str(r))
    c.set("fill", color); c.set("opacity", "0.2"); c.set("stroke", color); c.set("stroke-width", "2")
    t = ET.SubElement(root, "text")
    t.set("x", str(cx)); t.set("y", str(cy + 5)); t.set("text-anchor", "middle")
    t.set("fill", color); t.set("font-size", "13"); t.set("font-weight", "bold"); t.set("font-family", "sans-serif")
    t.text = label


def add_arrow(root, x1, y1, x2, y2, color=C_CYAN):
    """Simple line arrow."""
    l = ET.SubElement(root, "line")
    l.set("x1", str(x1)); l.set("y1", str(y1)); l.set("x2", str(x2)); l.set("y2", str(y2))
    l.set("stroke", color); l.set("stroke-width", "2"); l.set("marker-end", "url(#arrowhead)")
    # arrowhead marker
    if not root.find(".//{http://www.w3.org/2000/svg}marker[@id='arrowhead']") is not None:
        defs = root.find("{http://www.w3.org/2000/svg}defs")
        if defs is None:
            defs = ET.SubElement(root, "defs")
        m = ET.SubElement(defs, "marker")
        m.set("id", "arrowhead"); m.set("markerWidth", "10"); m.set("markerHeight", "7")
        m.set("refX", "10"); m.set("refY", "3.5"); m.set("orient", "auto")
        p = ET.SubElement(m, "polygon")
        p.set("points", "0 0, 10 3.5, 0 7"); p.set("fill", color)


def add_circuit_dot(root, cx, cy, r=3, color=C_CYAN):
    c = ET.SubElement(root, "circle")
    c.set("cx", str(cx)); c.set("cy", str(cy)); c.set("r", str(r)); c.set("fill", color)


def add_glow_circle(root, cx, cy, r, color=C_CYAN):
    """Glowing circle effect."""
    c = ET.SubElement(root, "circle")
    c.set("cx", str(cx)); c.set("cy", str(cy)); c.set("r", str(r))
    c.set("fill", "none"); c.set("stroke", color); c.set("stroke-width", "1.5"); c.set("opacity", "0.3")
    c2 = ET.SubElement(root, "circle")
    c2.set("cx", str(cx)); c2.set("cy", str(cy)); c2.set("r", str(int(r * 0.6)))
    c2.set("fill", "none"); c2.set("stroke", color); c2.set("stroke-width", "1"); c2.set("opacity", "0.6")


# ═══════════════════════════════════════════════════════════
# LESSON 1 — Что такое робототехника
# ═══════════════════════════════════════════════════════════
def lesson1():
    root = svg_root()
    add_bg(root)
    add_header(root, 1, "Что такое робототехника", "Введение, история и законы Азимова")

    # Left panel: Definition
    add_panel(root, 16, 82, 370, 140, "Определение")
    add_text(root, 28, 112, "Робототехника — наука о создании", 13, C_TEXT)
    add_text(root, 28, 130, "и применении роботов, автоматических", 13, C_TEXT)
    add_text(root, 28, 148, "устройств для выполнения задач.", 13, C_TEXT)
    add_text(root, 28, 172, "Слово «робот» — от чешского", 13, C_DIM)
    add_text(root, 28, 190, "«robota» (работа), Карел Чапек, 1920", 13, C_DIM)

    # Right panel: Timeline
    add_panel(root, 400, 82, 384, 140, "История робототехники")
    events = [
        ("1920", "Чапек придумал слово «робот»"),
        ("1942", "Азимов сформулировал 3 закона"),
        ("1954", "Первый промышленный робот"),
        ("1969", "Робот Shakey (Stanford)"),
        ("2000", "ASIMO — гуманоид Honda"),
        ("2020", "Роботы-курьеры, дроны"),
    ]
    for i, (yr, desc) in enumerate(events):
        yy = 114 + i * 18
        add_text(root, 412, yy, yr, 12, C_CYAN, bold=True, font="monospace")
        add_text(root, 456, yy, desc, 12, C_TEXT)

    # Asimov's Laws panel
    add_panel(root, 16, 236, 370, 200, "Три закона робототехники (Азимов)")
    laws = [
        ("1", "Робот не может причинить вред\nчеловеку или бездействовать, если\nчеловеку угрожает опасность.", C_RED),
        ("2", "Робот должен подчиняться командам\nчеловека, если они не противоречат\nПервому закону.", C_ORANGE),
        ("3", "Робот должен защищать себя, если\nэто не противоречит Первому и\nВторому законам.", C_GREEN),
    ]
    for i, (num, text, color) in enumerate(laws):
        yy = 270 + i * 56
        # Number circle
        c = ET.SubElement(root, "circle")
        c.set("cx", "38"); c.set("cy", str(yy - 4)); c.set("r", "14")
        c.set("fill", color); c.set("opacity", "0.25"); c.set("stroke", color); c.set("stroke-width", "1.5")
        add_text(root, 38, yy + 1, num, 16, color, bold=True, font="monospace", anchor="middle")
        lines = text.split("\n")
        for j, line in enumerate(lines):
            add_text(root, 60, yy - 8 + j * 16, line, 12, C_TEXT)

    # Robot icon (stylized)
    add_panel(root, 400, 236, 384, 200, "Робот — основные признаки")
    # Head
    el = ET.SubElement(root, "rect")
    el.set("x", "555"); el.set("y", "270"); el.set("width", "60"); el.set("height", "45"); el.set("rx", "8"); el.set("fill", "none"); el.set("stroke", C_CYAN); el.set("stroke-width", "2")
    # Eyes
    ET.SubElement(root, "circle").set("cx", "573"); root[-1].set("cy", "290"); root[-1].set("r", "6"); root[-1].set("fill", C_ACCENT)
    ET.SubElement(root, "circle").set("cx", "597"); root[-1].set("cy", "290"); root[-1].set("r", "6"); root[-1].set("fill", C_ACCENT)
    # Antenna
    ET.SubElement(root, "line").set("x1", "585"); root[-1].set("y1", "270"); root[-1].set("x2", "585"); root[-1].set("y2", "258"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "2")
    ET.SubElement(root, "circle").set("cx", "585"); root[-1].set("cy", "255"); root[-1].set("r", "4"); root[-1].set("fill", C_CYAN)
    # Body
    ET.SubElement(root, "rect").set("x", "545"); root[-1].set("y", "320"); root[-1].set("width", "80"); root[-1].set("height", "55"); root[-1].set("rx", "6"); root[-1].set("fill", "none"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "2")
    # Arms
    ET.SubElement(root, "line").set("x1", "545"); root[-1].set("y1", "330"); root[-1].set("x2", "525"); root[-1].set("y2", "355"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "2")
    ET.SubElement(root, "line").set("x1", "625"); root[-1].set("y1", "330"); root[-1].set("x2", "645"); root[-1].set("y2", "355"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "2")
    # Legs
    ET.SubElement(root, "line").set("x1", "565"); root[-1].set("y1", "375"); root[-1].set("x2", "565"); root[-1].set("y2", "405"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "2")
    ET.SubElement(root, "line").set("x1", "605"); root[-1].set("y1", "375"); root[-1].set("x2", "605"); root[-1].set("y2", "405"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "2")
    # Labels around robot
    add_text(root, 420, 280, "Датчики", 11, C_GREEN, bold=True)
    add_text(root, 420, 296, "(глаза, уши)", 10, C_DIM)
    add_text(root, 420, 330, "Контроллер", 11, C_ORANGE, bold=True)
    add_text(root, 420, 346, "(мозг)", 10, C_DIM)
    add_text(root, 420, 370, "Приводы", 11, C_RED, bold=True)
    add_text(root, 420, 386, "(руки, ноги)", 10, C_DIM)

    # Bottom panel: Quote
    add_panel(root, 16, 450, 768, 60, border_color=C_CYAN)
    add_text(root, 28, 474, "\"Любая достаточно развитая технология неотличима от магии.\"", 14, C_ACCENT, bold=True)
    add_text(root, 28, 496, "— Артур Кларк", 12, C_DIM)

    # Decorative circuit dots
    for cx, cy in [(760, 90), (770, 550), (30, 550), (770, 82)]:
        add_circuit_dot(root, cx, cy, 2, C_CYAN)

    # Footer
    add_text(root, 400, 530, "7 класс | Робототехника | Урок 1", 11, C_DIM, anchor="middle")

    return root


# ═══════════════════════════════════════════════════════════
# LESSON 2 — Виды роботов
# ═══════════════════════════════════════════════════════════
def lesson2():
    root = svg_root()
    add_bg(root)
    add_header(root, 2, "Виды роботов", "Классификация роботов по назначению")

    # 5 card panels for robot types
    types = [
        ("Промышленные", C_RED, "Сварка, сборка, покраска\nна заводах. Высокая\nточность и скорость.", " fabr"),
        ("Сервисные", C_ORANGE, "Помощники дома:\nробот-пылесос, робот-\nмойщик окон.", " serv"),
        ("Образовательные", C_GREEN, "Наборы Arduino, LEGO,\nмикроконтроллеры для\nобучения.", " edu"),
        ("Гуманоидные", C_PURPLE, "Роботы, похожие на\nчеловека: ASIMO, Atlas,\nSophia.", " hum"),
        ("Мобильные", C_CYAN, "Колёсные, гусеничные,\nшагающие роботы.\nДроны, роверы.", " mob"),
    ]

    card_w = 148
    card_h = 210
    gap = 8
    start_x = 16

    for i, (name, color, desc, _) in enumerate(types):
        x = start_x + i * (card_w + gap)
        y = 86
        add_panel(root, x, y, card_w, card_h, border_color=color)
        # Title bar
        r = ET.SubElement(root, "rect")
        r.set("x", str(x)); r.set("y", str(y + 28)); r.set("width", str(card_w)); r.set("height", "3")
        r.set("fill", color); r.set("opacity", "0.5")
        add_text(root, x + card_w // 2, y + 20, name, 12, color, bold=True, anchor="middle")
        # Icon area
        cx = x + card_w // 2
        cy = y + 72
        # Draw unique icon per type
        if i == 0:  # Industrial - arm
            ET.SubElement(root, "rect").set("x", str(cx-15)); root[-1].set("y", str(cy+10)); root[-1].set("width", "30"); root[-1].set("height", "25"); root[-1].set("rx", "3"); root[-1].set("fill", "none"); root[-1].set("stroke", color); root[-1].set("stroke-width", "1.5")
            ET.SubElement(root, "line").set("x1", str(cx)); root[-1].set("y1", str(cy+10)); root[-1].set("x2", str(cx)); root[-1].set("y2", str(cy-15)); root[-1].set("stroke", color); root[-1].set("stroke-width", "1.5")
            ET.SubElement(root, "line").set("x1", str(cx)); root[-1].set("y1", str(cy-15)); root[-1].set("x2", str(cx+20)); root[-1].set("y2", str(cy-5)); root[-1].set("stroke", color); root[-1].set("stroke-width", "1.5")
        elif i == 1:  # Service - house
            ET.SubElement(root, "rect").set("x", str(cx-18)); root[-1].set("y", str(cy-5)); root[-1].set("width", "36"); root[-1].set("height", "30"); root[-1].set("rx", "3"); root[-1].set("fill", "none"); root[-1].set("stroke", color); root[-1].set("stroke-width", "1.5")
            ET.SubElement(root, "polygon").set("points", f"{cx-22},{cy-5} {cx},{cy-22} {cx+22},{cy-5}"); root[-1].set("fill", "none"); root[-1].set("stroke", color); root[-1].set("stroke-width", "1.5")
        elif i == 2:  # Educational - book/board
            ET.SubElement(root, "rect").set("x", str(cx-18)); root[-1].set("y", str(cy-15)); root[-1].set("width", "36"); root[-1].set("height", "28"); root[-1].set("rx", "3"); root[-1].set("fill", "none"); root[-1].set("stroke", color); root[-1].set("stroke-width", "1.5")
            add_text(root, cx, cy + 2, "{}", 16, color, bold=True, font="monospace", anchor="middle")
        elif i == 3:  # Humanoid - stick figure
            ET.SubElement(root, "circle").set("cx", str(cx)); root[-1].set("cy", str(cy-15)); root[-1].set("r", "8"); root[-1].set("fill", "none"); root[-1].set("stroke", color); root[-1].set("stroke-width", "1.5")
            ET.SubElement(root, "line").set("x1", str(cx)); root[-1].set("y1", str(cy-7)); root[-1].set("x2", str(cx)); root[-1].set("y2", str(cy+10)); root[-1].set("stroke", color); root[-1].set("stroke-width", "1.5")
            ET.SubElement(root, "line").set("x1", str(cx-12)); root[-1].set("y1", str(cy)); root[-1].set("x2", str(cx+12)); root[-1].set("y2", str(cy)); root[-1].set("stroke", color); root[-1].set("stroke-width", "1.5")
            ET.SubElement(root, "line").set("x1", str(cx)); root[-1].set("y1", str(cy+10)); root[-1].set("x2", str(cx-10)); root[-1].set("y2", str(cy+25)); root[-1].set("stroke", color); root[-1].set("stroke-width", "1.5")
            ET.SubElement(root, "line").set("x1", str(cx)); root[-1].set("y1", str(cy+10)); root[-1].set("x2", str(cx+10)); root[-1].set("y2", str(cy+25)); root[-1].set("stroke", color); root[-1].set("stroke-width", "1.5")
        elif i == 4:  # Mobile - wheels
            ET.SubElement(root, "rect").set("x", str(cx-20)); root[-1].set("y", str(cy-10)); root[-1].set("width", "40"); root[-1].set("height", "20"); root[-1].set("rx", "4"); root[-1].set("fill", "none"); root[-1].set("stroke", color); root[-1].set("stroke-width", "1.5")
            ET.SubElement(root, "circle").set("cx", str(cx-12)); root[-1].set("cy", str(cy+15)); root[-1].set("r", "5"); root[-1].set("fill", "none"); root[-1].set("stroke", color); root[-1].set("stroke-width", "1.5")
            ET.SubElement(root, "circle").set("cx", str(cx+12)); root[-1].set("cy", str(cy+15)); root[-1].set("r", "5"); root[-1].set("fill", "none"); root[-1].set("stroke", color); root[-1].set("stroke-width", "1.5")

        # Description text
        lines = desc.split("\n")
        for j, line in enumerate(lines):
            add_text(root, x + 8, y + 112 + j * 16, line, 11, C_TEXT)

    # Bottom comparison table
    add_panel(root, 16, 310, 768, 130, "Сравнение характеристик")
    # Table header
    cols = ["Тип", "Автономность", "Сложность", "Примеры"]
    col_x = [28, 170, 340, 510]
    for ci, col in enumerate(cols):
        add_text(root, col_x[ci], 340, col, 12, C_CYAN, bold=True)
    ET.SubElement(root, "line").set("x1", "24"); root[-1].set("y1", "348"); root[-1].set("x2", "776"); root[-1].set("y2", "348"); root[-1].set("stroke", C_BORDER); root[-1].set("stroke-width", "1")
    rows = [
        ("Промышленные", "Низкая (программа)", "Высокая", "KUKA, ABB, FANUC"),
        ("Сервисные", "Средняя", "Средняя", "Roomba, Aibo, Alexa"),
        ("Образовательные", "Ручное упр.", "Низкая", "Arduino, LEGO Mindstorms"),
        ("Гуманоидные", "Высокая (ИИ)", "Очень высокая", "Atlas, Sophia, ASIMO"),
        ("Мобильные", "Средняя-Высокая", "Средняя", "Марсоход, DJI, Roomba"),
    ]
    for ri, (typ, aut, comp, ex) in enumerate(rows):
        yy = 368 + ri * 16
        add_text(root, col_x[0], yy, typ, 11, C_TEXT)
        add_text(root, col_x[1], yy, aut, 11, C_TEXT)
        add_text(root, col_x[2], yy, comp, 11, C_TEXT)
        add_text(root, col_x[3], yy, ex, 11, C_TEXT)

    # Bottom info
    add_panel(root, 16, 454, 768, 56, border_color=C_CYAN)
    add_text(root, 28, 476, "Роботы становятся всё более распространёнными: от производства до повседневной жизни.", 13, C_ACCENT)
    add_text(root, 28, 496, "К 2030 году ожидается более 20 млн роботов в мире.", 12, C_DIM)

    add_text(root, 400, 530, "7 класс | Робототехника | Урок 2", 11, C_DIM, anchor="middle")
    return root


# ═══════════════════════════════════════════════════════════
# LESSON 3 — Основные компоненты робота
# ═══════════════════════════════════════════════════════════
def lesson3():
    root = svg_root()
    add_bg(root)
    add_header(root, 3, "Основные компоненты робота", "Датчики, контроллер, приводы, питание")

    # Central block diagram
    add_panel(root, 16, 82, 490, 300, "Структурная схема робота")

    # Controller (center)
    cx, cy = 260, 220
    ET.SubElement(root, "rect").set("x", str(cx-55)); root[-1].set("y", str(cy-30)); root[-1].set("width", "110"); root[-1].set("height", "60"); root[-1].set("rx", "6"); root[-1].set("fill", C_PRIMARY); root[-1].set("opacity", "0.4"); root[-1].set("stroke", C_PRIMARY); root[-1].set("stroke-width", "2")
    add_text(root, cx, cy - 6, "КОНТРОЛЛЕР", 13, C_TEXT, bold=True, anchor="middle")
    add_text(root, cx, cy + 12, "(Микроконтроллер)", 10, C_DIM, anchor="middle")

    # Sensors (left)
    sx, sy = 80, 180
    ET.SubElement(root, "rect").set("x", str(sx-50)); root[-1].set("y", str(sy-25)); root[-1].set("width", "100"); root[-1].set("height", "50"); root[-1].set("rx", "6"); root[-1].set("fill", C_GREEN); root[-1].set("opacity", "0.25"); root[-1].set("stroke", C_GREEN); root[-1].set("stroke-width", "2")
    add_text(root, sx, sy, "ДАТЧИКИ", 13, C_GREEN, bold=True, anchor="middle")
    # Arrow sensors -> controller
    ET.SubElement(root, "line").set("x1", str(sx+50)); root[-1].set("y1", str(sy)); root[-1].set("x2", str(cx-55)); root[-1].set("y2", str(cy-10)); root[-1].set("stroke", C_GREEN); root[-1].set("stroke-width", "2"); root[-1].set("stroke-dasharray", "5,3")
    add_text(root, 155, 200, "данные", 10, C_GREEN, anchor="middle")

    # Actuators (right)
    ax, ay = 440, 180
    ET.SubElement(root, "rect").set("x", str(ax-50)); root[-1].set("y", str(ay-25)); root[-1].set("width", "100"); root[-1].set("height", "50"); root[-1].set("rx", "6"); root[-1].set("fill", C_RED); root[-1].set("opacity", "0.25"); root[-1].set("stroke", C_RED); root[-1].set("stroke-width", "2")
    add_text(root, ax, ay, "ПРИВОДЫ", 13, C_RED, bold=True, anchor="middle")
    # Arrow controller -> actuators
    ET.SubElement(root, "line").set("x1", str(cx+55)); root[-1].set("y1", str(cy-10)); root[-1].set("x2", str(ax-50)); root[-1].set("y2", str(ay)); root[-1].set("stroke", C_RED); root[-1].set("stroke-width", "2"); root[-1].set("stroke-dasharray", "5,3")
    add_text(root, 365, 200, "команды", 10, C_RED, anchor="middle")

    # Power (bottom)
    px, py = 260, 310
    ET.SubElement(root, "rect").set("x", str(px-50)); root[-1].set("y", str(py-20)); root[-1].set("width", "100"); root[-1].set("height", "40"); root[-1].set("rx", "6"); root[-1].set("fill", C_ORANGE); root[-1].set("opacity", "0.25"); root[-1].set("stroke", C_ORANGE); root[-1].set("stroke-width", "2")
    add_text(root, px, py + 4, "ПИТАНИЕ", 13, C_ORANGE, bold=True, anchor="middle")
    # Arrow power -> controller
    ET.SubElement(root, "line").set("x1", str(px)); root[-1].set("y1", str(py-20)); root[-1].set("x2", str(cx)); root[-1].set("y2", str(cy+30)); root[-1].set("stroke", C_ORANGE); root[-1].set("stroke-width", "2"); root[-1].set("stroke-dasharray", "5,3")
    add_text(root, 280, 290, "+5V", 10, C_ORANGE)

    # Program (top)
    add_text(root, 260, 115, "ПРОГРАММА", 13, C_PURPLE, bold=True, anchor="middle")
    add_text(root, 260, 132, "(код на C++)", 10, C_DIM, anchor="middle")
    ET.SubElement(root, "line").set("x1", str(cx)); root[-1].set("y1", str(cy-30)); root[-1].set("x2", str(cx)); root[-1].set("y2", str(140)); root[-1].set("stroke", C_PURPLE); root[-1].set("stroke-width", "2"); root[-1].set("stroke-dasharray", "5,3")
    add_text(root, 275, 160, "загрузка", 10, C_PURPLE)

    # Right side: Details
    add_panel(root, 520, 82, 264, 300, "Подробности")

    details = [
        ("Датчики", C_GREEN, [
            "Ультразвуковой (расстояние)",
            "Инфракрасный (препятствия)",
            "Датчик линии (чёрное/белое)",
            "Фоторезистор (свет)",
            "Кнопки (тактильные)",
        ]),
        ("Контроллер", C_PRIMARY, [
            "Arduino Uno (ATmega328P)",
            "14 цифровых пинов",
            "6 аналоговых входов",
            "16 МГц, 32 КБ Flash",
        ]),
        ("Приводы", C_RED, [
            "DC моторы (колёса)",
            "Серводвигатели (поворот)",
            "Шаговые моторы (точность)",
            "Светодиоды, зуммеры",
        ]),
    ]

    yy = 116
    for name, color, items in details:
        add_text(root, 532, yy, name, 13, color, bold=True)
        yy += 18
        for item in items:
            add_text(root, 540, yy, "\u2022 " + item, 11, C_TEXT)
            yy += 15
        yy += 6

    # Bottom: data flow summary
    add_panel(root, 16, 396, 768, 55, "Цикл работы робота")
    flow_items = ["Датчики", "\u2192", "Контроллер", "\u2192", "Приводы", "\u2192", "Действие", "\u2192", "Среда"]
    flow_colors = [C_GREEN, C_DIM, C_PRIMARY, C_DIM, C_RED, C_DIM, C_ORANGE, C_DIM, C_CYAN]
    xx = 40
    for item, col in zip(flow_items, flow_colors):
        add_text(root, xx, 428, item, 14, col, bold=True, font="monospace")
        xx += len(item) * 9 + 20

    # Code snippet
    add_code_block(root, 16, 464, 768, 70, [
        "// Цикл управления роботом:",
        "void loop() {",
        "  int dist = readSensor();   // 1. Чтение датчика",
        "  int cmd  = process(dist);  // 2. Обработка данных",
        "  drive(cmd);                // 3. Управление приводом",
        "}",
    ], title="Пример логики")

    add_text(root, 400, 555, "7 класс | Робототехника | Урок 3", 11, C_DIM, anchor="middle")
    return root


# ═══════════════════════════════════════════════════════════
# LESSON 4 — Arduino — платформа для роботов
# ═══════════════════════════════════════════════════════════
def lesson4():
    root = svg_root()
    add_bg(root)
    add_header(root, 4, "Arduino — платформа для роботов", "Знакомство с Arduino Uno")

    # Board layout diagram
    add_panel(root, 16, 82, 420, 310, "Arduino Uno — вид сверху")

    # Board body
    ET.SubElement(root, "rect").set("x", "60"); root[-1].set("y", "125"); root[-1].set("width", "330"); root[-1].set("height", "220"); root[-1].set("rx", "10"); root[-1].set("fill", "#0A3D6B"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "2")

    # USB connector
    ET.SubElement(root, "rect").set("x", "55"); root[-1].set("y", "155"); root[-1].set("width", "20"); root[-1].set("height", "50"); root[-1].set("rx", "3"); root[-1].set("fill", "#94A3B8"); root[-1].set("stroke", C_TEXT); root[-1].set("stroke-width", "1")
    add_text(root, 56, 186, "USB", 8, C_DARK, bold=True, font="monospace")

    # MCU chip
    ET.SubElement(root, "rect").set("x", "160"); root[-1].set("y", "200"); root[-1].set("width", "80"); root[-1].set("height", "60"); root[-1].set("rx", "3"); root[-1].set("fill", "#1E3A5F"); root[-1].set("stroke", C_DIM); root[-1].set("stroke-width", "1.5")
    add_text(root, 200, 228, "ATmega", 10, C_ACCENT, anchor="middle")
    add_text(root, 200, 242, "328P", 10, C_ACCENT, anchor="middle")

    # Digital pins (top)
    pin_labels_d = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13"]
    for i, p in enumerate(pin_labels_d):
        px = 85 + i * 22
        ET.SubElement(root, "rect").set("x", str(px)); root[-1].set("y", "130"); root[-1].set("width", "16"); root[-1].set("height", "12"); root[-1].set("fill", C_GREEN); root[-1].set("opacity", "0.5")
        add_text(root, px + 3, 139, p, 7, C_TEXT, font="monospace")
    add_text(root, 80, 126, "Цифровые пины", 9, C_GREEN, bold=True)

    # Analog pins (bottom)
    pin_labels_a = ["A0","A1","A2","A3","A4","A5"]
    for i, p in enumerate(pin_labels_a):
        px = 85 + i * 35
        ET.SubElement(root, "rect").set("x", str(px)); root[-1].set("y", "328"); root[-1].set("width", "24"); root[-1].set("height", "12"); root[-1].set("fill", C_ORANGE); root[-1].set("opacity", "0.5")
        add_text(root, px + 2, 337, p, 7, C_TEXT, font="monospace")
    add_text(root, 80, 352, "Аналоговые входы", 9, C_ORANGE, bold=True)

    # Power LED
    ET.SubElement(root, "circle").set("cx", "130"); root[-1].set("cy", "285"); root[-1].set("r", "5"); root[-1].set("fill", C_GREEN)
    add_text(root, 140, 288, "PWR", 8, C_GREEN, font="monospace")
    # LED 13
    ET.SubElement(root, "circle").set("cx", "130"); root[-1].set("cy", "300"); root[-1].set("r", "5"); root[-1].set("fill", C_ORANGE)
    add_text(root, 140, 303, "L13", 8, C_ORANGE, font="monospace")

    # Reset button
    ET.SubElement(root, "circle").set("cx", "310"); root[-1].set("cy", "155"); root[-1].set("r", "10"); root[-1].set("fill", "#475569"); root[-1].set("stroke", C_DIM); root[-1].set("stroke-width", "1")
    add_text(root, 325, 158, "RST", 8, C_DIM, font="monospace")

    # Power header
    pw_labels = ["5V","3.3V","GND","GND","VIN"]
    for i, p in enumerate(pw_labels):
        px = 280 + i * 22
        ET.SubElement(root, "rect").set("x", str(px)); root[-1].set("y", "270"); root[-1].set("width", "18"); root[-1].set("height", "12"); root[-1].set("fill", C_RED); root[-1].set("opacity", "0.4")
        add_text(root, px + 1, 279, p, 6, C_TEXT, font="monospace")

    # Specs panel
    add_panel(root, 450, 82, 334, 310, "Характеристики Arduino Uno")
    specs = [
        ("Микроконтроллер", "ATmega328P"),
        ("Тактовая частота", "16 МГц"),
        ("Flash-память", "32 КБ"),
        ("SRAM", "2 КБ"),
        ("EEPROM", "1 КБ"),
        ("Цифровые пины", "14 (6 PWM)"),
        ("Аналоговые входы", "6"),
        ("Напряжение", "5 В (логика)"),
        ("Питание", "7-12 В (DC)"),
        ("USB", "Type-B"),
        ("Размер", "68.6 x 53.4 мм"),
    ]
    for i, (k, v) in enumerate(specs):
        yy = 116 + i * 22
        add_text(root, 462, yy, k, 12, C_DIM)
        add_text(root, 610, yy, v, 12, C_ACCENT, bold=True, font="monospace")
        ET.SubElement(root, "line").set("x1", "462"); root[-1].set("y1", str(yy+6)); root[-1].set("x2", "770"); root[-1].set("y2", str(yy+6)); root[-1].set("stroke", C_GRID); root[-1].set("stroke-width", "0.5")

    # Why Arduino panel
    add_panel(root, 16, 406, 768, 80, "Почему Arduino?")
    reasons = [
        "Открытый исходный код (Open Source)",
        "Простая среда разработки (Arduino IDE)",
        "Огромное сообщество и библиотеки",
        "Идеально для обучения робототехнике",
    ]
    for i, r in enumerate(reasons):
        add_text(root, 32 + (i % 2) * 380, 440 + (i // 2) * 22, "\u2713 " + r, 12, C_GREEN)

    # Code snippet
    add_code_block(root, 16, 500, 768, 55, [
        "// Мигание светодиодом (Blink)",
        "void setup()   { pinMode(13, OUTPUT); }",
        "void loop()    { digitalWrite(13, HIGH); delay(1000);",
        "                 digitalWrite(13, LOW);  delay(1000); }",
    ])

    add_text(root, 400, 570, "7 класс | Робототехника | Урок 4", 11, C_DIM, anchor="middle")
    return root


# ═══════════════════════════════════════════════════════════
# LESSON 5 — Основы программирования Arduino
# ═══════════════════════════════════════════════════════════
def lesson5():
    root = svg_root()
    add_bg(root)
    add_header(root, 5, "Основы программирования Arduino", "C++, функции setup() и loop(), цифровой ввод/вывод")

    # Structure panel
    add_panel(root, 16, 82, 280, 240, "Структура программы")
    add_text(root, 28, 112, "Каждая программа (скетч)", 12, C_TEXT)
    add_text(root, 28, 128, "состоит из двух функций:", 12, C_TEXT)

    # setup box
    ET.SubElement(root, "rect").set("x", "28"); root[-1].set("y", "144"); root[-1].set("width", "256"); root[-1].set("height", "70"); root[-1].set("rx", "6"); root[-1].set("fill", C_GREEN); root[-1].set("opacity", "0.1"); root[-1].set("stroke", C_GREEN); root[-1].set("stroke-width", "1.5")
    add_text(root, 36, 164, "void setup() { ... }", 13, C_GREEN, bold=True, font="monospace")
    add_text(root, 36, 182, "Выполняется 1 раз при запуске", 11, C_TEXT)
    add_text(root, 36, 198, "Инициализация пинов, переменных", 11, C_DIM)

    # loop box
    ET.SubElement(root, "rect").set("x", "28"); root[-1].set("y", "224"); root[-1].set("width", "256"); root[-1].set("height", "70"); root[-1].set("rx", "6"); root[-1].set("fill", C_CYAN); root[-1].set("opacity", "0.1"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "1.5")
    add_text(root, 36, 244, "void loop()  { ... }", 13, C_CYAN, bold=True, font="monospace")
    add_text(root, 36, 262, "Выполняется бесконечно", 11, C_TEXT)
    add_text(root, 36, 278, "Основная логика программы", 11, C_DIM)

    # Code example
    add_code_block(root, 310, 82, 474, 240, [
        "// Мигание светодиодом",
        "int led = 13;",
        "",
        "void setup() {",
        "  pinMode(led, OUTPUT);",
        "}",
        "",
        "void loop() {",
        "  digitalWrite(led, HIGH);",
        "  delay(1000);",
        "  digitalWrite(led, LOW);",
        "  delay(1000);",
        "}",
    ], title="Пример: Blink")

    # Digital I/O panel
    add_panel(root, 16, 336, 388, 150, "Цифровой ввод/вывод")
    funcs = [
        ("pinMode(pin, MODE)", "Настройка пина: INPUT / OUTPUT"),
        ("digitalWrite(pin, VAL)", "Запись: HIGH / LOW"),
        ("digitalRead(pin)", "Чтение: HIGH / LOW"),
        ("delay(ms)", "Пауза в миллисекундах"),
    ]
    for i, (fn, desc) in enumerate(funcs):
        yy = 370 + i * 28
        add_text(root, 28, yy, fn, 12, C_ACCENT, bold=True, font="monospace")
        add_text(root, 28, yy + 14, desc, 11, C_DIM)

    # Variables & types
    add_panel(root, 416, 336, 368, 150, "Типы данных")
    types_data = [
        ("int", "-32768 ... 32767", "2 байта"),
        ("long", "-2.1 млрд ... 2.1 млрд", "4 байта"),
        ("float", "Дробные числа", "4 байта"),
        ("bool", "true / false", "1 байт"),
        ("char", "Символ ASCII", "1 байт"),
        ("String", "Текстовая строка", "var"),
    ]
    for i, (typ, desc, size) in enumerate(types_data):
        yy = 368 + i * 20
        add_text(root, 428, yy, typ, 12, C_CYAN, bold=True, font="monospace")
        add_text(root, 496, yy, desc, 11, C_TEXT)
        add_text(root, 680, yy, size, 10, C_DIM)

    # Button read example
    add_code_block(root, 16, 500, 768, 60, [
        "// Чтение кнопки на пине 2",
        "void setup() { pinMode(2, INPUT);  pinMode(13, OUTPUT); }",
        "void loop()  { if (digitalRead(2)) digitalWrite(13, HIGH);",
        "               else digitalWrite(13, LOW); }",
    ], title="Пример: чтение кнопки")

    add_text(root, 400, 575, "7 класс | Робототехника | Урок 5", 11, C_DIM, anchor="middle")
    return root


# ═══════════════════════════════════════════════════════════
# LESSON 6 — Управление моторами
# ═══════════════════════════════════════════════════════════
def lesson6():
    root = svg_root()
    add_bg(root)
    add_header(root, 6, "Управление моторами", "DC мотор, серводвигатель, H-мост, ШИМ")

    # DC Motor panel
    add_panel(root, 16, 82, 250, 200, "DC Мотор (постоянного тока)")
    # Motor icon - circle with M
    ET.SubElement(root, "circle").set("cx", "141"); root[-1].set("cy", "160"); root[-1].set("r", "30"); root[-1].set("fill", "none"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "2")
    add_text(root, 141, 166, "M", 20, C_CYAN, bold=True, anchor="middle")
    # Shaft
    ET.SubElement(root, "line").set("x1", "171"); root[-1].set("y1", "160"); root[-1].set("x2", "195"); root[-1].set("y2", "160"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "3")
    # Wires
    ET.SubElement(root, "line").set("x1", "111"); root[-1].set("y1", "155"); root[-1].set("x2", "80"); root[-1].set("y2", "140"); root[-1].set("stroke", C_RED); root[-1].set("stroke-width", "2")
    ET.SubElement(root, "line").set("x1", "111"); root[-1].set("y1", "165"); root[-1].set("x2", "80"); root[-1].set("y2", "180"); root[-1].set("stroke", C_TEXT); root[-1].set("stroke-width", "2")
    add_text(root, 50, 140, "+", 14, C_RED, bold=True)
    add_text(root, 50, 180, "\u2013", 14, C_TEXT, bold=True)
    add_text(root, 30, 218, "Управление скоростью через ШИМ", 10, C_DIM)
    add_text(root, 30, 234, "Направление через H-мост", 10, C_DIM)
    add_text(root, 30, 250, "6-9 В, 200 мА - 2 А", 10, C_DIM)

    # Servo panel
    add_panel(root, 280, 82, 250, 200, "Серводвигатель (Servo)")
    # Servo icon
    ET.SubElement(root, "rect").set("x", "355"); root[-1].set("y", "135"); root[-1].set("width", "60"); root[-1].set("height", "40"); root[-1].set("rx", "4"); root[-1].set("fill", "none"); root[-1].set("stroke", C_ORANGE); root[-1].set("stroke-width", "2")
    # Horn
    ET.SubElement(root, "line").set("x1", "385"); root[-1].set("y1", "135"); root[-1].set("x2", "385"); root[-1].set("y2", "110"); root[-1].set("stroke", C_ORANGE); root[-1].set("stroke-width", "3")
    ET.SubElement(root, "circle").set("cx", "385"); root[-1].set("cy", "135"); root[-1].set("r", "6"); root[-1].set("fill", C_ORANGE); root[-1].set("opacity", "0.5"); root[-1].set("stroke", C_ORANGE); root[-1].set("stroke-width", "1.5")
    # Angle arc
    ET.SubElement(root, "path").set("d", "M 405 135 A 25 25 0 0 0 365 110"); root[-1].set("fill", "none"); root[-1].set("stroke", C_DIM); root[-1].set("stroke-width", "1"); root[-1].set("stroke-dasharray", "3,2")
    add_text(root, 410, 120, "0-180\u00b0", 10, C_DIM)
    add_text(root, 294, 210, "Угол: 0\u00b0 - 180\u00b0", 11, C_TEXT)
    add_text(root, 294, 226, "3 провода: VCC, GND, Signal", 11, C_TEXT)
    add_text(root, 294, 242, "Управление: servo.write(angle)", 11, C_TEXT)
    add_text(root, 294, 258, "Обычно SG90 (микро)", 10, C_DIM)

    # H-bridge panel
    add_panel(root, 544, 82, 240, 200, "H-мост (L298N)")
    # H-bridge diagram
    ET.SubElement(root, "rect").set("x", "600"); root[-1].set("y", "120"); root[-1].set("width", "80"); root[-1].set("height", "60"); root[-1].set("rx", "4"); root[-1].set("fill", C_PRIMARY); root[-1].set("opacity", "0.3"); root[-1].set("stroke", C_PRIMARY); root[-1].set("stroke-width", "1.5")
    add_text(root, 640, 148, "L298N", 12, C_ACCENT, bold=True, anchor="middle")
    add_text(root, 640, 162, "H-Bridge", 9, C_DIM, anchor="middle")
    # Input arrows
    ET.SubElement(root, "line").set("x1", "570"); root[-1].set("y1", "130"); root[-1].set("x2", "600"); root[-1].set("y2", "130"); root[-1].set("stroke", C_GREEN); root[-1].set("stroke-width", "1.5")
    ET.SubElement(root, "line").set("x1", "570"); root[-1].set("y1", "150"); root[-1].set("x2", "600"); root[-1].set("y2", "150"); root[-1].set("stroke", C_GREEN); root[-1].set("stroke-width", "1.5")
    add_text(root, "558", "134", "IN1", 8, C_GREEN, font="monospace")
    add_text(root, "558", "154", "IN2", 8, C_GREEN, font="monospace")
    # Output arrows
    ET.SubElement(root, "line").set("x1", "680"); root[-1].set("y1", "130"); root[-1].set("x2", "720"); root[-1].set("y2", "130"); root[-1].set("stroke", C_RED); root[-1].set("stroke-width", "1.5")
    ET.SubElement(root, "line").set("x1", "680"); root[-1].set("y1", "150"); root[-1].set("x2", "720"); root[-1].set("y2", "150"); root[-1].set("stroke", C_RED); root[-1].set("stroke-width", "1.5")
    add_text(root, 724, "134", "M+", 8, C_RED, font="monospace")
    add_text(root, 724, "154", "M\u2013", 8, C_RED, font="monospace")
    # Motor
    ET.SubElement(root, "circle").set("cx", "755"); root[-1].set("cy", "140"); root[-1].set("r", "12"); root[-1].set("fill", "none"); root[-1].set("stroke", C_ORANGE); root[-1].set("stroke-width", "1.5")
    add_text(root, 755, 144, "M", 10, C_ORANGE, anchor="middle")
    add_text(root, 558, 210, "Управляет направлением", 11, C_TEXT)
    add_text(root, 558, 226, "и скоростью мотора.", 11, C_TEXT)
    add_text(root, 558, 248, "IN1=1, IN2=0 \u2192 вперёд", 10, C_GREEN, font="monospace")
    add_text(root, 558, 262, "IN1=0, IN2=1 \u2192 назад", 10, C_RED, font="monospace")

    # PWM panel
    add_panel(root, 16, 296, 390, 130, "ШИМ (PWM)")
    add_text(root, 28, 326, "Широтно-импульсная модуляция", 12, C_TEXT)
    add_text(root, 28, 344, "управляет мощностью мотора.", 12, C_TEXT)
    # PWM waveform
    for i in range(8):
        x = 30 + i * 45
        ET.SubElement(root, "line").set("x1", str(x)); root[-1].set("y1", "380"); root[-1].set("x2", str(x)); root[-1].set("y2", "365"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "2")
        ET.SubElement(root, "line").set("x1", str(x)); root[-1].set("y1", "365"); root[-1].set("x2", str(x + 20)); root[-1].set("y2", "365"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "2")
        ET.SubElement(root, "line").set("x1", str(x + 20)); root[-1].set("y1", "365"); root[-1].set("x2", str(x + 20)); root[-1].set("y2", "380"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "2")
        ET.SubElement(root, "line").set("x1", str(x + 20)); root[-1].set("y1", "380"); root[-1].set("x2", str(x + 45)); root[-1].set("y2", "380"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "1")
    add_text(root, 28, 405, "analogWrite(pin, 0-255)", 12, C_ACCENT, font="monospace")
    add_text(root, 28, 420, "0 = 0%, 127 = 50%, 255 = 100%", 11, C_DIM, font="monospace")

    # Code examples
    add_code_block(root, 416, 296, 368, 130, [
        "// DC мотор через L298N",
        "void setup() {",
        "  pinMode(5, OUTPUT); // IN1",
        "  pinMode(6, OUTPUT); // IN2",
        "  pinMode(9, OUTPUT); // ENA(PWM)",
        "}",
        "void forward() {",
        "  digitalWrite(5, HIGH);",
        "  digitalWrite(6, LOW);",
        "  analogWrite(9, 200);",
        "}",
    ], title="Пример: DC мотор")

    # Servo code
    add_code_block(root, 16, 440, 370, 100, [
        "#include <Servo.h>",
        "Servo myServo;",
        "void setup() {",
        "  myServo.attach(9);",
        "}",
        "void loop() {",
        "  myServo.write(90);  // 90\u00b0",
        "}",
    ], title="Пример: Серводвигатель")

    # Key info
    add_panel(root, 400, 440, 384, 100, "Важно помнить", border_color=C_ORANGE)
    add_text(root, 412, 466, "\u26A0 Arduino не может напрямую питать мотор!", 12, C_ORANGE, bold=True)
    add_text(root, 412, 486, "\u2022 Мотор потребляет больше 40 мА (предел пина)", 11, C_TEXT)
    add_text(root, 412, 502, "\u2022 Используйте драйвер (L298N, L293D)", 11, C_TEXT)
    add_text(root, 412, 518, "\u2022 Отдельное питание для мотора", 11, C_TEXT)

    add_text(root, 400, 555, "7 класс | Робототехника | Урок 6", 11, C_DIM, anchor="middle")
    return root


# ═══════════════════════════════════════════════════════════
# LESSON 7 — Ультразвуковой датчик расстояния
# ═══════════════════════════════════════════════════════════
def lesson7():
    root = svg_root()
    add_bg(root)
    add_header(root, 7, "Ультразвуковой датчик расстояния", "HC-SR04: принцип работы и подключение")

    # How it works panel
    add_panel(root, 16, 82, 420, 210, "Принцип работы HC-SR04")

    # Sensor body
    ET.SubElement(root, "rect").set("x", "40"); root[-1].set("y", "110"); root[-1].set("width", "70"); root[-1].set("height", "50"); root[-1].set("rx", "6"); root[-1].set("fill", C_PRIMARY); root[-1].set("opacity", "0.3"); root[-1].set("stroke", C_PRIMARY); root[-1].set("stroke-width", "2")
    # Two cylinders (transducers)
    ET.SubElement(root, "circle").set("cx", "56"); root[-1].set("cy", "135"); root[-1].set("r", "10"); root[-1].set("fill", "none"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "2")
    ET.SubElement(root, "circle").set("cx", "94"); root[-1].set("cy", "135"); root[-1].set("r", "10"); root[-1].set("fill", "none"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "2")
    add_text(root, 56, 138, "T", 9, C_CYAN, bold=True, anchor="middle")
    add_text(root, 94, 138, "R", 9, C_CYAN, bold=True, anchor="middle")

    # Object
    ET.SubElement(root, "rect").set("x", "340"); root[-1].set("y", "115"); root[-1].set("width", "30"); root[-1].set("height", "50"); root[-1].set("rx", "3"); root[-1].set("fill", C_ORANGE); root[-1].set("opacity", "0.3"); root[-1].set("stroke", C_ORANGE); root[-1].set("stroke-width", "1.5")
    add_text(root, 355, 145, "?", 16, C_ORANGE, bold=True, anchor="middle")

    # Ultrasonic wave (outgoing)
    for r in [20, 35, 50]:
        ET.SubElement(root, "path").set("d", f"M 115 {135-r*0.3} Q {200} {135-r*0.5} {330} {135-r*0.1}"); root[-1].set("fill", "none"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "1.5"); root[-1].set("opacity", str(0.8 - r*0.01))
        ET.SubElement(root, "path").set("d", f"M 115 {135+r*0.3} Q {200} {135+r*0.5} {330} {135+r*0.1}"); root[-1].set("fill", "none"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "1.5"); root[-1].set("opacity", str(0.8 - r*0.01))

    # Echo wave (returning)
    for r in [15, 30, 45]:
        ET.SubElement(root, "path").set("d", f"M 335 {135-r*0.2} Q {230} {135-r*0.4} {120} {135-r*0.05}"); root[-1].set("fill", "none"); root[-1].set("stroke", C_GREEN); root[-1].set("stroke-width", "1"); root[-1].set("opacity", "0.5"); root[-1].set("stroke-dasharray", "4,3")
        ET.SubElement(root, "path").set("d", f"M 335 {135+r*0.2} Q {230} {135+r*0.4} {120} {135+r*0.05}"); root[-1].set("fill", "none"); root[-1].set("stroke", C_GREEN); root[-1].set("stroke-width", "1"); root[-1].set("opacity", "0.5"); root[-1].set("stroke-dasharray", "4,3")

    # Labels
    add_text(root, 180, 105, "Ультразвук \u2192", 10, C_CYAN, bold=True)
    add_text(root, 220, 175, "\u2190 Эхо-сигнал", 10, C_GREEN, bold=True)
    add_text(root, 40, 178, "T = передатчик", 10, C_DIM)
    add_text(root, 40, 194, "R = приёмник", 10, C_DIM)

    # Distance formula
    add_text(root, 30, 220, "S = (v \u00d7 t) / 2", 14, C_ACCENT, bold=True, font="monospace")
    add_text(root, 180, 220, "v = 340 м/с (скорость звука)", 11, C_DIM)
    add_text(root, 30, 240, "t = время возврата эха", 11, C_DIM)

    # Timing diagram
    add_panel(root, 450, 82, 334, 210, "Временная диаграмма")
    add_text(root, 462, 114, "Trig \u2192 10 мкс импульс", 11, C_CYAN)
    # Trig pulse
    ET.SubElement(root, "line").set("x1", "462"); root[-1].set("y1", "130"); root[-1].set("x2", "490"); root[-1].set("y2", "130"); root[-1].set("stroke", C_DIM); root[-1].set("stroke-width", "1.5")
    ET.SubElement(root, "line").set("x1", "490"); root[-1].set("y1", "130"); root[-1].set("x2", "490"); root[-1].set("y2", "120"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "1.5")
    ET.SubElement(root, "line").set("x1", "490"); root[-1].set("y1", "120"); root[-1].set("x2", "500"); root[-1].set("y2", "120"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "1.5")
    ET.SubElement(root, "line").set("x1", "500"); root[-1].set("y1", "120"); root[-1].set("x2", "500"); root[-1].set("y2", "130"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "1.5")

    add_text(root, 462, 152, "Echo \u2192 длительность = расстояние", 11, C_GREEN)
    # Echo pulse
    ET.SubElement(root, "line").set("x1", "505"); root[-1].set("y1", "168"); root[-1].set("x2", "505"); root[-1].set("y2", "155"); root[-1].set("stroke", C_GREEN); root[-1].set("stroke-width", "1.5")
    ET.SubElement(root, "line").set("x1", "505"); root[-1].set("y1", "155"); root[-1].set("x2", "700"); root[-1].set("y2", "155"); root[-1].set("stroke", C_GREEN); root[-1].set("stroke-width", "1.5")
    ET.SubElement(root, "line").set("x1", "700"); root[-1].set("y1", "155"); root[-1].set("x2", "700"); root[-1].set("y2", "168"); root[-1].set("stroke", C_GREEN); root[-1].set("stroke-width", "1.5")
    add_text(root, 580, 150, "\u2190 t \u2192", 10, C_GREEN, anchor="middle")

    # Specs
    add_text(root, 462, 200, "Характеристики HC-SR04:", 12, C_ACCENT, bold=True)
    specs = [
        "Диапазон: 2 см \u2013 400 см",
        "Точность: \u00b13 мм",
        "Угол обзора: 30\u00b0",
        "Напряжение: 5 В",
    ]
    for i, s in enumerate(specs):
        add_text(root, 470, 218 + i * 16, "\u2022 " + s, 11, C_TEXT)

    # Wiring diagram
    add_panel(root, 16, 306, 370, 130, "Подключение к Arduino")
    wiring = [
        ("VCC", "\u2192 5V (Arduino)", C_RED),
        ("Trig", "\u2192 Пин 9 (цифровой)", C_ORANGE),
        ("Echo", "\u2192 Пин 10 (цифровой)", C_GREEN),
        ("GND", "\u2192 GND (Arduino)", C_DIM),
    ]
    for i, (pin, conn, color) in enumerate(wiring):
        yy = 340 + i * 22
        add_text(root, 28, yy, pin, 12, color, bold=True, font="monospace")
        add_text(root, 80, yy, conn, 12, C_TEXT)

    # Code
    add_code_block(root, 400, 306, 384, 130, [
        "#define TRIG 9",
        "#define ECHO 10",
        "",
        "long getDistance() {",
        "  digitalWrite(TRIG, LOW);",
        "  delayMicroseconds(2);",
        "  digitalWrite(TRIG, HIGH);",
        "  delayMicroseconds(10);",
        "  digitalWrite(TRIG, LOW);",
        "  long dur = pulseIn(ECHO, HIGH);",
        "  return dur * 0.034 / 2;",
        "}",
    ], title="Код: чтение расстояния")

    # Application examples
    add_panel(root, 16, 450, 768, 56, "Применение", border_color=C_GREEN)
    apps = "Парктроник \u2022 Робот-обходчик препятствий \u2022 Измеритель уровня воды \u2022 Система охраны \u2022 Картирование помещения"
    add_text(root, 28, 484, apps, 13, C_GREEN)

    # Formula reminder
    add_panel(root, 16, 518, 768, 40, border_color=C_ACCENT)
    add_text(root, 28, 543, "Формула: расстояние(см) = время(мкс) \u00d7 0.034 / 2", 13, C_ACCENT, bold=True, font="monospace")

    add_text(root, 400, 575, "7 класс | Робототехника | Урок 7", 11, C_DIM, anchor="middle")
    return root


# ═══════════════════════════════════════════════════════════
# LESSON 8 — Датчик линии и датчик света
# ═══════════════════════════════════════════════════════════
def lesson8():
    root = svg_root()
    add_bg(root)
    add_header(root, 8, "Датчик линии и датчик света", "Принцип работы, подключение и применение")

    # Line sensor panel (left half)
    add_panel(root, 16, 82, 380, 230, "Датчик линии (TCRT5000)")

    # How it works diagram
    # Surface
    ET.SubElement(root, "rect").set("x", "40"); root[-1].set("y", "210"); root[-1].set("width", "100"); root[-1].set("height", "20"); root[-1].set("fill", "#1a1a2e"); root[-1].set("stroke", C_DIM); root[-1].set("stroke-width", "1")
    add_text(root, 90, 224, "Чёрная линия", 9, C_DIM, anchor="middle")
    # White surface
    ET.SubElement(root, "rect").set("x", "140"); root[-1].set("y", "210"); root[-1].set("width", "80"); root[-1].set("height", "20"); root[-1].set("fill", "#e2e8f0"); root[-1].set("stroke", C_DIM); root[-1].set("stroke-width", "1")
    add_text(root, 180, 224, "Белый пол", 9, C_DARK, anchor="middle")

    # Sensor above
    ET.SubElement(root, "rect").set("x", "55"); root[-1].set("y", "145"); root[-1].set("width", "80"); root[-1].set("height", "30"); root[-1].set("rx", "4"); root[-1].set("fill", C_PRIMARY); root[-1].set("opacity", "0.3"); root[-1].set("stroke", C_PRIMARY); root[-1].set("stroke-width", "1.5")
    add_text(root, 95, 164, "TCRT5000", 9, C_ACCENT, anchor="middle")

    # IR LED + phototransistor inside
    ET.SubElement(root, "circle").set("cx", "75"); root[-1].set("cy", "158"); root[-1].set("r", "5"); root[-1].set("fill", C_RED); root[-1].set("opacity", "0.6")
    add_text(root, 75, 175, "IR", 7, C_RED, anchor="middle")
    ET.SubElement(root, "circle").set("cx", "115"); root[-1].set("cy", "158"); root[-1].set("r", "5"); root[-1].set("fill", C_GREEN); root[-1].set("opacity", "0.6")
    add_text(root, 115, 175, "PT", 7, C_GREEN, anchor="middle")

    # IR beam down and reflected
    ET.SubElement(root, "line").set("x1", "75"); root[-1].set("y1", "163"); root[-1].set("x2", "90"); root[-1].set("y2", "207"); root[-1].set("stroke", C_RED); root[-1].set("stroke-width", "1.5"); root[-1].set("opacity", "0.6")
    ET.SubElement(root, "line").set("x1", "90"); root[-1].set("y1", "207"); root[-1].set("x2", "115"); root[-1].set("y2", "163"); root[-1].set("stroke", C_GREEN); root[-1].set("stroke-width", "1.5"); root[-1].set("opacity", "0.6")

    # Principle text
    add_text(root, 30, 115, "Принцип: ИК-светодиод излучает,", 11, C_TEXT)
    add_text(root, 30, 130, "фототранзистор принимает отражение.", 11, C_TEXT)

    # Black/White comparison
    add_text(root, 240, 115, "Белая поверхность:", 11, C_TEXT, bold=True)
    add_text(root, 240, 132, "Много отражения \u2192 HIGH", 11, C_GREEN)
    add_text(root, 240, 152, "Чёрная поверхность:", 11, C_TEXT, bold=True)
    add_text(root, 240, 169, "Мало отражения \u2192 LOW", 11, C_RED)
    add_text(root, 30, 250, "Расстояние до поверхности: 1-15 мм", 10, C_DIM)
    add_text(root, 30, 265, "Аналоговый и цифровой выход", 10, C_DIM)

    # Light sensor panel (right half)
    add_panel(root, 410, 82, 374, 230, "Датчик света (Фоторезистор)")

    # LDR symbol
    ET.SubElement(root, "circle").set("cx", "560"); root[-1].set("cy", "150"); root[-1].set("r", "20"); root[-1].set("fill", "none"); root[-1].set("stroke", C_ORANGE); root[-1].set("stroke-width", "2")
    # Zigzag resistor
    pts = "540,150 545,140 550,160 555,140 560,160 565,140 570,160 575,140 580,150"
    ET.SubElement(root, "polyline").set("points", pts); root[-1].set("fill", "none"); root[-1].set("stroke", C_ORANGE); root[-1].set("stroke-width", "1.5")
    # Arrows (light)
    for dx in [-10, 0, 10]:
        ET.SubElement(root, "line").set("x1", str(560+dx)); root[-1].set("y1", "120"); root[-1].set("x2", str(560+dx)); root[-1].set("y2", "130"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "2")
        ET.SubElement(root, "line").set("x1", str(555+dx)); root[-1].set("y1", "125"); root[-1].set("x2", str(560+dx)); root[-1].set("y2", "130"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "1.5")
        ET.SubElement(root, "line").set("x1", str(565+dx)); root[-1].set("y1", "125"); root[-1].set("x2", str(560+dx)); root[-1].set("y2", "130"); root[-1].set("stroke", C_CYAN); root[-1].set("stroke-width", "1.5")

    add_text(root, 560, 180, "Фоторезистор (LDR)", 11, C_ORANGE, anchor="middle")
    add_text(root, 422, 200, "Сопротивление меняется", 11, C_TEXT)
    add_text(root, 422, 216, "в зависимости от света:", 11, C_TEXT)
    add_text(root, 422, 236, "Яркий свет \u2192 R мало \u2192 V мало", 11, C_CYAN)
    add_text(root, 422, 254, "Темнота   \u2192 R велик \u2192 V велик", 11, C_PURPLE)
    add_text(root, 422, 278, "Подключение: делитель напряжения", 10, C_DIM)
    add_text(root, 422, 294, "с фиксированным резистором 10 кОм", 10, C_DIM)

    # Voltage divider circuit
    add_panel(root, 16, 326, 280, 150, "Делитель напряжения")
    # Circuit diagram
    ET.SubElement(root, "line").set("x1", "60"); root[-1].set("y1", "350"); root[-1].set("x2", "60"); root[-1].set("y2", "375"); root[-1].set("stroke", C_RED); root[-1].set("stroke-width", "2")
    add_text(root, 50, "348", "5V", 9, C_RED, font="monospace")
    # LDR
    ET.SubElement(root, "rect").set("x", "50"); root[-1].set("y", "375"); root[-1].set("width", "20"); root[-1].set("height", "30"); root[-1].set("rx", "3"); root[-1].set("fill", "none"); root[-1].set("stroke", C_ORANGE); root[-1].set("stroke-width", "1.5")
    add_text(root, 60, 394, "LDR", 7, C_ORANGE, anchor="middle", font="monospace")
    # Middle point
    ET.SubElement(root, "circle").set("cx", "60"); root[-1].set("cy", "415"); root[-1].set("r", "3"); root[-1].set("fill", C_ACCENT)
    add_text(root, 70, 418, "\u2192 A0 (аналоговый вход)", 9, C_ACCENT)
    # Fixed resistor
    ET.SubElement(root, "rect").set("x", "50"); root[-1].set("y", "420"); root[-1].set("width", "20"); root[-1].set("height", "25"); root[-1].set("rx", "3"); root[-1].set("fill", "none"); root[-1].set("stroke", C_DIM); root[-1].set("stroke-width", "1.5")
    add_text(root, 60, 436, "10K", 7, C_DIM, anchor="middle", font="monospace")
    # GND
    ET.SubElement(root, "line").set("x1", "60"); root[-1].set("y1", "445"); root[-1].set("x2", "60"); root[-1].set("y2", "460"); root[-1].set("stroke", C_DIM); root[-1].set("stroke-width", "2")
    add_text(root, 50, 468, "GND", 9, C_DIM, font="monospace")
    # Formula
    add_text(root, 120, 385, "Vout = Vcc \u00d7 R2/(R1+R2)", 11, C_ACCENT, font="monospace")
    add_text(root, 120, 405, "R1 = LDR (переменное)", 10, C_DIM)
    add_text(root, 120, 420, "R2 = 10 кОм (фиксированное)", 10, C_DIM)

    # Line sensor code
    add_code_block(root, 310, 326, 474, 110, [
        "// Датчик линии (цифровой)",
        "#define LINE_PIN 3",
        "",
        "void loop() {",
        "  int line = digitalRead(LINE_PIN);",
        "  if (line == HIGH) {",
        "    // На белом - едем",
        "    forward();",
        "  } else {",
        "    // На линии - поворот",
        "    turnRight();",
        "  }",
        "}",
    ], title="Код: датчик линии")

    # Light sensor code
    add_code_block(root, 310, 448, 474, 100, [
        "// Датчик света (аналоговый)",
        "#define LIGHT_PIN A0",
        "",
        "void loop() {",
        "  int val = analogRead(LIGHT_PIN);",
        "  // val: 0 (ярко) - 1023 (темно)",
        "  if (val > 800) {",
        "    digitalWrite(13, HIGH); // свет",
        "  }",
        "}",
    ], title="Код: датчик света")

    # Application panel
    add_panel(root, 16, 494, 768, 52, "Применение", border_color=C_GREEN)
    add_text(root, 28, 516, "Датчик линии: робот-следопыт, сортировка, конвейер", 12, C_GREEN)
    add_text(root, 28, 534, "Датчик света: ночник, солнечный трекер, метеостанция", 12, C_CYAN)

    add_text(root, 400, 565, "7 класс | Робототехника | Урок 8", 11, C_DIM, anchor="middle")
    return root


# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════
def main():
    os.makedirs(OUT_DIR, exist_ok=True)

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

    print("=" * 60)
    print("Generating Grade 7 Robotics SVG files")
    print("=" * 60)

    for num, gen in generators:
        svg_root_el = gen()
        filepath = os.path.join(OUT_DIR, f"lesson-{num}.svg")

        # Write SVG
        tree = ET.ElementTree(svg_root_el)
        ET.indent(tree, space="  ")
        tree.write(filepath, encoding="unicode", xml_declaration=True)

        # Validate
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            ET.fromstring(content)
            size_kb = len(content.encode("utf-8")) / 1024
            print(f"  [OK] lesson-{num}.svg  ({size_kb:.1f} KB) - valid XML")
        except ET.ParseError as e:
            print(f"  [FAIL] lesson-{num}.svg - XML parse error: {e}")

    print("\nDone! All 8 SVGs generated and validated.")
    print(f"Output directory: {OUT_DIR}")


if __name__ == "__main__":
    main()
