#!/usr/bin/env python3
"""Generate Grade 7 History SVG files — Russian curriculum, red/rose color scheme."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/history"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── colour palette ──────────────────────────────────────────────────────────
PRIMARY      = "#EF4444"
PRIMARY_DARK = "#B91C1C"
PRIMARY_LITE = "#FCA5A5"
ROSE_LIGHT   = "#FFF1F2"
ROSE_MID     = "#FECDD3"
BG           = "#FFFFFF"
TEXT_DARK    = "#1F2937"
TEXT_MED     = "#4B5563"
TEXT_LIGHT   = "#9CA3AF"
ACCENT_GOLD  = "#D97706"
ACCENT_BLUE  = "#1D4ED8"

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
    """Top red banner with title."""
    add_rect(root, 0, 0, W, 72, PRIMARY)
    add_rect(root, 0, 72, W, 4, PRIMARY_DARK)
    add_text(root, W // 2, 36, title, 22, "#FFFFFF", weight="bold")
    if subtitle:
        add_text(root, W // 2, 58, subtitle, 12, "#FFFFFF", weight="normal")


def footer(root, lesson_num):
    add_rect(root, 0, H - 30, W, 30, ROSE_LIGHT)
    add_line(root, 0, H - 30, W, H - 30, PRIMARY_LITE, 1)
    add_text(root, W // 2, H - 10, f"7 класс — История России — Урок {lesson_num}", 10, TEXT_LIGHT)


def info_box(parent, x, y, w, h, title, body_lines, accent=PRIMARY):
    """Rounded info card with accent left border."""
    add_rect(parent, x, y, w, h, "#FFFFFF", rx=6, stroke="#E5E7EB", sw=1)
    add_rect(parent, x, y, 5, h, accent, rx=2)
    add_text(parent, x + 16, y + 20, title, 13, accent, anchor="start", weight="bold")
    ty = y + 38
    for line in body_lines:
        add_text(parent, x + 16, ty, line, 11, TEXT_MED, anchor="start")
        ty += 16


def timeline_item(parent, cx, y_top, y_line, date, label, color=PRIMARY):
    """One point on a horizontal timeline."""
    add_circle(parent, cx, y_line, 7, color, "#FFFFFF", 2)
    add_line(parent, cx, y_line - 7, cx, y_line - 22, color, 2)
    add_rect(parent, cx - 36, y_top, 72, 22, ROSE_MID, rx=4, stroke=color, sw=1)
    add_text(parent, cx, y_top + 14, date, 11, PRIMARY_DARK, weight="bold")
    add_text(parent, cx, y_line + 18, label, 10, TEXT_MED)


# ════════════════════════════════════════════════════════════════════════════
#  LESSON 1 — Объединение русских земель
# ════════════════════════════════════════════════════════════════════════════
def lesson1():
    root = svg_root()
    header_banner(root, "Объединение русских земель", "Возвышение Москвы и собирание Руси")
    footer(root, 1)

    # Background subtle pattern
    add_rect(root, 0, 76, W, H - 106, ROSE_LIGHT, opacity=0.4)

    # ── Timeline ────────────────────────────────────────────────────────
    ty = 100
    add_text(root, W // 2, ty, "Хронология объединения", 15, PRIMARY_DARK, weight="bold")
    tl_y = ty + 35
    add_line(root, 80, tl_y, W - 80, tl_y, PRIMARY, 3)

    events = [
        (110, "1325", "Иван Калита"),
        (260, "1340", "Москва —\nцентр Руси"),
        (400, "1359", "Дмитрий\nДонской"),
        (540, "1380", "Куликовская\nбитва"),
        (690, "1389", "Василий I"),
    ]
    for cx, date, label in events:
        add_circle(root, cx, tl_y, 8, PRIMARY, "#FFFFFF", 2)
        add_text(root, cx, tl_y - 14, date, 11, PRIMARY_DARK, weight="bold")
        for i, ln in enumerate(label.split("\n")):
            add_text(root, cx, tl_y + 18 + i * 13, ln, 10, TEXT_MED)

    # ── Info boxes ──────────────────────────────────────────────────────
    info_box(root, 30, 195, 230, 130,
             "Иван Калита (1325–1340)",
             ["Перенос резиденции митрополита",
              "в Москву (1326 г.)",
              "Сбор дани для Орды —",
              "укрепление авторитета",
              "Расширение московских владений"])

    info_box(root, 280, 195, 230, 130,
             "Дмитрий Донской (1359–1389)",
             ["Куликовская битва — 8 сентября",
              "1380 г. — первая крупная победа",
              "Белокаменный Кремль (1367 г.)",
              "Москва — лидер объединения",
              "Передача власти без ханской ярлыки"])

    info_box(root, 530, 195, 240, 130,
             "Причины возвышения Москвы",
             ["Географическое положение",
              "Поддержка православной церкви",
              "Умелая политика московских князей",
              "Пересечение торговых путей",
              "Дальновидная политика по отношению к Орде"])

    # ── Diagram: Concentric circles — Moscow's growing influence ────────
    add_text(root, 400, 370, "Рост влияния Москвы", 14, PRIMARY_DARK, weight="bold")
    cx, cy = 400, 480
    for r, clr, lbl in [(100, ROSE_MID, ""), (70, "#FCA5A5", ""), (40, PRIMARY_LITE, "")]:
        add_circle(root, cx, cy, r, clr, PRIMARY if r == 100 else None, 1 if r == 100 else 0)
    add_text(root, cx, cy - 6, "Москва", 13, PRIMARY_DARK, weight="bold")
    add_text(root, cx, cy + 10, "центр Руси", 10, TEXT_MED)

    add_text(root, cx, cy - 80, "Удельные княжества", 9, TEXT_MED)
    add_text(root, cx, cy - 55, "Земли Великого княжества", 9, TEXT_MED)

    return root


# ════════════════════════════════════════════════════════════════════════════
#  LESSON 2 — Иван III и освобождение Руси
# ════════════════════════════════════════════════════════════════════════════
def lesson2():
    root = svg_root()
    header_banner(root, "Иван III и освобождение Руси", "Конец ордынского ига — 1480 год")
    footer(root, 2)

    add_rect(root, 0, 76, W, H - 106, ROSE_LIGHT, opacity=0.4)

    # Timeline
    ty = 98
    add_text(root, W // 2, ty, "Ключевые даты правления Ивана III", 14, PRIMARY_DARK, weight="bold")
    tl_y = ty + 30
    add_line(root, 60, tl_y, W - 60, tl_y, PRIMARY, 3)

    events = [
        (100, "1440", "Рождение\nИвана III"),
        (220, "1462", "Начало\nправления"),
        (370, "1471", "Поход на\nНовгород"),
        (500, "1478", "Присоедин.\nНовгорода"),
        (620, "1480", "Стояние\nна Угре"),
        (730, "1485", "Тверь\nприсоед."),
    ]
    for cx, date, label in events:
        add_circle(root, cx, tl_y, 7, PRIMARY, "#FFFFFF", 2)
        add_text(root, cx, tl_y - 14, date, 10, PRIMARY_DARK, weight="bold")
        for i, ln in enumerate(label.split("\n")):
            add_text(root, cx, tl_y + 16 + i * 12, ln, 9, TEXT_MED)

    # Info boxes
    info_box(root, 30, 178, 240, 120,
             "Стояние на реке Угре (1480)",
             ["Хан Ахмат подошёл к р. Угре",
              "Иван III отвёл войска на Боровск",
              "Ахмат не решился на сражение",
              "Орда отступила — игу конец!",
              "Без единого крупного сражения"])

    info_box(root, 290, 178, 230, 120,
             "Государственные символы",
             ["Двуглавый орёл — герб (1497)",
              "«Государь всея Руси» — титул",
              "Шапка Мономаха — регалия",
              "Кремль — резиденция государя",
              "«Сводный судебник» — 1497 г."])

    info_box(root, 540, 178, 230, 120,
             "Расширение территории",
             ["Ярославль (1463 г.)",
              "Ростов (1474 г.)",
              "Новгород (1478 г.)",
              "Тверь (1485 г.)",
              "Вятка (1489 г.)"])

    # Diagram: Before/After comparison
    add_text(root, W // 2, 330, "Русь до и после Ивана III", 14, PRIMARY_DARK, weight="bold")

    # Before
    bx, by = 130, 355
    add_rect(root, bx - 100, by, 200, 190, "#FFFFFF", rx=8, stroke=PRIMARY_LITE, sw=1)
    add_text(root, bx, by + 18, "До (раздробленность)", 12, PRIMARY, weight="bold")
    add_line(root, bx - 80, by + 28, bx + 80, by + 28, PRIMARY_LITE, 1)
    fragments = ["Московское княжество", "Тверское княжество", "Рязанское княжество",
                 "Новгородская республика", "Псковская республика", "Зависимость от Орды"]
    for i, f in enumerate(fragments):
        add_rect(root, bx - 80, by + 38 + i * 24, 160, 20, ROSE_MID, rx=3)
        add_text(root, bx, by + 52 + i * 24, f, 9, TEXT_DARK)

    # Arrow
    add_text(root, 320, 445, "→", 36, PRIMARY, weight="bold")

    # After
    ax = 500
    add_rect(root, ax - 100, by, 200, 190, "#FFFFFF", rx=8, stroke=PRIMARY, sw=2)
    add_text(root, ax, by + 18, "После (единое государство)", 12, PRIMARY, weight="bold")
    add_line(root, ax - 80, by + 28, ax + 80, by + 28, PRIMARY, 1)
    results = ["Единое Русское государство", "Освобождение от Орды",
               "Судебник 1497 г.", "Государственные символы",
               "Кирпичный Кремль", "Централизация власти"]
    for i, r in enumerate(results):
        add_rect(root, ax - 80, by + 38 + i * 24, 160, 20, PRIMARY_LITE, rx=3)
        add_text(root, ax, by + 52 + i * 24, r, 9, TEXT_DARK)

    return root


# ════════════════════════════════════════════════════════════════════════════
#  LESSON 3 — Иван IV Грозный
# ════════════════════════════════════════════════════════════════════════════
def lesson3():
    root = svg_root()
    header_banner(root, "Иван IV Грозный", "Первый царь всея Руси — реформы и опричнина")
    footer(root, 3)

    add_rect(root, 0, 76, W, H - 106, ROSE_LIGHT, opacity=0.4)

    # Timeline
    ty = 98
    add_text(root, W // 2, ty, "Правление Ивана IV (1533–1584)", 14, PRIMARY_DARK, weight="bold")
    tl_y = ty + 28
    add_line(root, 60, tl_y, W - 60, tl_y, PRIMARY, 3)

    events = [
        (90,  "1530", "Рождение"),
        (190, "1547", "Венчание\nна царство"),
        (300, "1549", "Избранная\nрада"),
        (410, "1550", "Судебник"),
        (510, "1552", "Взятие\nКазани"),
        (610, "1556", "Взятие\nАстрахани"),
        (710, "1565", "Опричнина"),
    ]
    for cx, date, label in events:
        clr = PRIMARY_DARK if "Опричнина" in label else PRIMARY
        add_circle(root, cx, tl_y, 6, clr, "#FFFFFF", 2)
        add_text(root, cx, tl_y - 12, date, 9, PRIMARY_DARK, weight="bold")
        for i, ln in enumerate(label.split("\n")):
            add_text(root, cx, tl_y + 14 + i * 11, ln, 9, TEXT_MED)

    # Left column — Reforms
    add_text(root, 140, 168, "Реформы Избранной рады", 13, ACCENT_BLUE, weight="bold")
    reforms = [
        ("Судебник 1550", "Единый закон для всей страны"),
        ("Стоглавый собор", "Унификация церковных обрядов"),
        ("Земские соборы", "Представительство сословий"),
        ("Стрелецкое войско", "Первое постоянное войско"),
        ("Губная реформа", "Местное самоуправление"),
    ]
    for i, (title, desc) in enumerate(reforms):
        y = 186 + i * 38
        add_rect(root, 30, y, 250, 34, "#FFFFFF", rx=4, stroke="#E5E7EB", sw=1)
        add_rect(root, 30, y, 4, 34, ACCENT_BLUE, rx=2)
        add_text(root, 44, y + 14, title, 11, ACCENT_BLUE, anchor="start", weight="bold")
        add_text(root, 44, y + 27, desc, 9, TEXT_MED, anchor="start")

    # Right column — Oprichnina
    add_text(root, 580, 168, "Опричнина (1565–1572)", 13, PRIMARY_DARK, weight="bold")
    oprich = [
        ("Разделение страны", "Опричнина и земщина"),
        ("Террор и репрессии", "Казни бояр и князей"),
        ("Экономический упадок", "Разорение земель"),
        ("Новгородский погром", "1570 г. — массовые казни"),
        ("Отмена опричнины", "1572 г. — конец террора"),
    ]
    for i, (title, desc) in enumerate(oprich):
        y = 186 + i * 38
        add_rect(root, 520, y, 250, 34, "#FFFFFF", rx=4, stroke="#E5E7EB", sw=1)
        add_rect(root, 520, y, 4, 34, PRIMARY_DARK, rx=2)
        add_text(root, 534, y + 14, title, 11, PRIMARY_DARK, anchor="start", weight="bold")
        add_text(root, 534, y + 27, desc, 9, TEXT_MED, anchor="start")

    # Bottom — Conquests
    add_text(root, W // 2, 400, "Завоевания Ивана IV", 14, PRIMARY_DARK, weight="bold")
    add_line(root, 80, 404, W - 80, 404, PRIMARY_LITE, 1)

    conquests = [
        (160, "Казанское\nханство", "1552 г.", "Падение Казани\nпосле долгой осады"),
        (400, "Астраханское\nханство", "1556 г.", "Присоединение\nбез сопротивления"),
        (640, "Сибирское\nханство", "1581 г.", "Поход Ермака\nТимофеевича"),
    ]
    for cx, name, date, desc in conquests:
        add_rect(root, cx - 90, 418, 180, 120, "#FFFFFF", rx=6, stroke=PRIMARY, sw=1)
        add_text(root, cx, 436, name.split("\n")[0], 12, PRIMARY, weight="bold")
        if "\n" in name:
            add_text(root, cx, 450, name.split("\n")[1], 12, PRIMARY, weight="bold")
        add_rect(root, cx - 40, 460, 80, 18, PRIMARY, rx=3)
        add_text(root, cx, 473, date, 10, "#FFFFFF", weight="bold")
        for i, ln in enumerate(desc.split("\n")):
            add_text(root, cx, 498 + i * 13, ln, 9, TEXT_MED)

    return root


# ════════════════════════════════════════════════════════════════════════════
#  LESSON 4 — Культура XVI века
# ════════════════════════════════════════════════════════════════════════════
def lesson4():
    root = svg_root()
    header_banner(root, "Культура XVI века", "Зодчество, книгопечатание, литература")
    footer(root, 4)

    add_rect(root, 0, 76, W, H - 106, ROSE_LIGHT, opacity=0.4)

    # ── Timeline of culture ─────────────────────────────────────────────
    ty = 98
    add_text(root, W // 2, ty, "Культурные достижения XVI века", 14, PRIMARY_DARK, weight="bold")
    tl_y = ty + 28
    add_line(root, 60, tl_y, W - 60, tl_y, PRIMARY, 3)

    events = [
        (100, "1475", "Строительство\nКремля"),
        (230, "1479", "Успенский\nсобор"),
        (360, "1554", "Покровский\nсобор"),
        (490, "1564", "Первая\nкнига"),
        (620, "1550-е", "Летописные\nсводы"),
        (730, "1580-е", "Иконопись"),
    ]
    for cx, date, label in events:
        add_circle(root, cx, tl_y, 6, PRIMARY, "#FFFFFF", 2)
        add_text(root, cx, tl_y - 12, date, 9, PRIMARY_DARK, weight="bold")
        for i, ln in enumerate(label.split("\n")):
            add_text(root, cx, tl_y + 14 + i * 11, ln, 9, TEXT_MED)

    # Three columns: Architecture, Printing, Literature
    cols = [
        ("Зодчество", ACCENT_GOLD, [
            ("Кремлёвские стены и башни", "Кирпич, 1475–1495 гг."),
            ("Успенский собор", "Главный храм Руси, Аристотель Фиораванти"),
            ("Покровский собор", "Храм Василия Блаженного, 1555–1561"),
            ("Грановитая палата", "Тронный зал Ивана III, 1487–1491"),
        ]),
        ("Книгопечатание", PRIMARY, [
            ("Иван Фёдоров", "Первопечатник, диакон церкви"),
            ("«Апостол» — 1564 г.", "Первая точно датированная книга"),
            ("Печатный двор", "В Москве, на Никольской улице"),
            ("«Часовник» — 1565 г.", "Вторая печатная книга"),
        ]),
        ("Литература и живопись", ACCENT_BLUE, [
            ("«Домострой»", "Свод правил жизни семьи"),
            ("«Степенная книга»", "История Руси по «степеням»"),
            ("«История о Казанском царстве»", "Повесть о взятии Казани"),
            ("Дионисий", "Великий иконописец, фрески Ферапонтова мон."),
        ]),
    ]
    for ci, (title, color, items) in enumerate(cols):
        x = 30 + ci * 258
        add_rect(root, x, 165, 246, 210, "#FFFFFF", rx=6, stroke=color, sw=2)
        add_rect(root, x, 165, 246, 28, color, rx=6)
        add_rect(root, x, 185, 246, 8, color)
        add_text(root, x + 123, 184, title, 13, "#FFFFFF", weight="bold")
        for i, (t, d) in enumerate(items):
            y = 202 + i * 42
            add_text(root, x + 12, y, t, 11, color, anchor="start", weight="bold")
            add_text(root, x + 12, y + 14, d, 9, TEXT_MED, anchor="start")

    # Bottom: St. Basil's simplified silhouette
    add_text(root, W // 2, 405, "Покровский собор (Храм Василия Блаженного)", 13, PRIMARY_DARK, weight="bold")
    add_line(root, 100, 408, W - 100, 408, PRIMARY_LITE, 1)

    # Simplated cathedral silhouette shapes
    base_y = 555
    add_rect(root, 300, base_y - 50, 200, 50, PRIMARY_LITE, rx=0, stroke=PRIMARY, sw=1)

    # Central dome
    add_path(root, f"M 370,{base_y - 50} Q 370,{base_y - 90} 400,{base_y - 100} Q 430,{base_y - 90} 430,{base_y - 50}", PRIMARY, PRIMARY, 2)
    add_circle(root, 400, base_y - 105, 6, PRIMARY)

    # Left dome
    add_path(root, f"M 310,{base_y - 50} Q 310,{base_y - 75} 330,{base_y - 82} Q 350,{base_y - 75} 350,{base_y - 50}", PRIMARY, PRIMARY, 2)
    add_circle(root, 330, base_y - 87, 5, PRIMARY)

    # Right dome
    add_path(root, f"M 450,{base_y - 50} Q 450,{base_y - 75} 470,{base_y - 82} Q 490,{base_y - 75} 490,{base_y - 50}", PRIMARY, PRIMARY, 2)
    add_circle(root, 470, base_y - 87, 5, PRIMARY)

    # Far domes
    add_path(root, f"M 270,{base_y - 50} Q 270,{base_y - 68} 285,{base_y - 72} Q 300,{base_y - 68} 300,{base_y - 50}", PRIMARY, PRIMARY, 2)
    add_path(root, f"M 500,{base_y - 50} Q 500,{base_y - 68} 515,{base_y - 72} Q 530,{base_y - 68} 530,{base_y - 50}", PRIMARY, PRIMARY, 2)

    add_text(root, 400, base_y + 10, "1555–1561 гг. — зодчие Барма и Постник", 10, TEXT_MED)

    return root


# ════════════════════════════════════════════════════════════════════════════
#  LESSON 5 — Причины и начало Смуты
# ════════════════════════════════════════════════════════════════════════════
def lesson5():
    root = svg_root()
    header_banner(root, "Причины и начало Смуты", "Династический кризис и Лжедмитрии")
    footer(root, 5)

    add_rect(root, 0, 76, W, H - 106, ROSE_LIGHT, opacity=0.4)

    # Causes diagram
    add_text(root, W // 2, 100, "Причины Смутного времени", 15, PRIMARY_DARK, weight="bold")

    causes = [
        (130, 140, "Династический\nкризис", "Прекращение\nдинастии Рюриковичей"),
        (400, 140, "Экономический\nкризис", "Разорение от\nопричнины и войн"),
        (670, 140, "Социальный\nкризис", "Усиление крепостничества\nи побеги крестьян"),
    ]
    for cx, cy, title, desc in causes:
        add_rect(root, cx - 110, cy, 220, 80, "#FFFFFF", rx=6, stroke=PRIMARY, sw=1)
        add_rect(root, cx - 110, cy, 220, 26, PRIMARY, rx=6)
        add_rect(root, cx - 110, cy + 20, 220, 6, PRIMARY)
        add_text(root, cx, cy + 16, title.split("\n")[0], 12, "#FFFFFF", weight="bold")
        if "\n" in title:
            add_text(root, cx, cy + 30, title.split("\n")[1], 10, "#FFFFFF")
        for i, ln in enumerate(desc.split("\n")):
            add_text(root, cx, cy + 50 + i * 13, ln, 10, TEXT_MED)

    # Arrow down
    add_text(root, W // 2, 240, "▼", 24, PRIMARY)

    # Central box
    add_rect(root, 280, 255, 240, 36, PRIMARY_DARK, rx=6)
    add_text(root, 400, 278, "Смутное время (1598–1613)", 14, "#FFFFFF", weight="bold")

    # Three False Dmitrys
    add_text(root, W // 2, 315, "Лжедмитрии — самозванцы на русском престоле", 13, PRIMARY_DARK, weight="bold")

    dmitrys = [
        (130, "Лжедмитрий I", "1605–1606", [
            "Выдавал себя за царевича Дмитрия",
            "Поддержан Польшей и папой римским",
            "Убит в мае 1606 г. в Москве",
        ]),
        (400, "Лжедмитрий II", "1607–1610", [
            "«Тушинский вор» — лагерь в Тушино",
            "Имел свой двор и бояр",
            "Убит в 1610 г. собственным охранником",
        ]),
        (670, "Лжедмитрий III", "1611–1612", [
            "«Псковский вор» — в Пскове",
            "Наименее удачливый самозванец",
            "Выдан властям и казнён",
        ]),
    ]
    for cx, name, dates, lines in dmitrys:
        add_rect(root, cx - 110, 330, 220, 120, "#FFFFFF", rx=6, stroke=PRIMARY_DARK, sw=1)
        add_rect(root, cx - 110, 330, 220, 22, PRIMARY_DARK, rx=6)
        add_rect(root, cx - 110, 348, 220, 4, PRIMARY_DARK)
        add_text(root, cx, 345, name, 11, "#FFFFFF", weight="bold")
        add_rect(root, cx - 40, 358, 80, 16, ROSE_MID, rx=3)
        add_text(root, cx, 370, dates, 9, PRIMARY_DARK, weight="bold")
        for i, ln in enumerate(lines):
            add_text(root, cx, 396 + i * 14, ln, 9, TEXT_MED)

    # Bottom: key events
    add_text(root, W // 2, 475, "Ключевые события начала Смуты", 13, PRIMARY_DARK, weight="bold")
    add_line(root, 60, 479, W - 60, 479, PRIMARY_LITE, 1)

    bottom_events = [
        (130, "1598", "Смерть Фёдора\nИоанновича"),
        (290, "1598", "Борис Годунов\nна троне"),
        (450, "1605", "Смерть\nБ. Годунова"),
        (610, "1606", "Восстание\nИ. Болотникова"),
    ]
    by = 505
    add_line(root, 70, by + 10, 690, by + 10, PRIMARY, 2)
    for cx, date, label in bottom_events:
        add_circle(root, cx, by + 10, 6, PRIMARY, "#FFFFFF", 2)
        add_text(root, cx, by - 4, date, 10, PRIMARY_DARK, weight="bold")
        for i, ln in enumerate(label.split("\n")):
            add_text(root, cx, by + 28 + i * 12, ln, 9, TEXT_MED)

    return root


# ════════════════════════════════════════════════════════════════════════════
#  LESSON 6 — Освобождение Москвы
# ════════════════════════════════════════════════════════════════════════════
def lesson6():
    root = svg_root()
    header_banner(root, "Освобождение Москвы", "Минин и Пожарский — 1612 год")
    footer(root, 6)

    add_rect(root, 0, 76, W, H - 106, ROSE_LIGHT, opacity=0.4)

    # Central event
    add_rect(root, 180, 90, 440, 60, PRIMARY_DARK, rx=8)
    add_text(root, 400, 115, "Освобождение Москвы от поляков", 16, "#FFFFFF", weight="bold")
    add_text(root, 400, 138, "4 ноября 1612 года (22 октября по ст. стилю)", 11, "#FFFFFF")

    # Two heroes
    add_text(root, W // 2, 175, "Организаторы второго земского ополчения", 14, PRIMARY_DARK, weight="bold")

    heroes = [
        (200, "Кузьма Минин", "Нижегородский староста", [
            "Призыв к сбору средств",
            "«Денеги отдадим, жён и детей продадим!»",
            "Организатор финансирования",
            "Выбран «делом и разумом»",
        ]),
        (600, "Князь Дмитрий Пожарский", "Военный руководитель", [
            "Опытный воевода",
            "Не запятнал себя сотрудничеством",
            "Руководил военными действиями",
            "Возглавил поход на Москву",
        ]),
    ]
    for cx, name, role, lines in heroes:
        add_rect(root, cx - 170, 190, 340, 120, "#FFFFFF", rx=6, stroke=PRIMARY, sw=2)
        add_rect(root, cx - 170, 190, 340, 30, PRIMARY, rx=6)
        add_rect(root, cx - 170, 214, 340, 6, PRIMARY)
        add_text(root, cx, 208, name, 13, "#FFFFFF", weight="bold")
        add_rect(root, cx - 80, 228, 160, 16, ROSE_MID, rx=3)
        add_text(root, cx, 240, role, 10, PRIMARY_DARK)
        for i, ln in enumerate(lines):
            add_text(root, cx, 264 + i * 14, ln, 10, TEXT_MED)

    # Timeline of liberation
    add_text(root, W // 2, 340, "Ход освобождения Москвы", 14, PRIMARY_DARK, weight="bold")

    steps = [
        ("1", "Сентябрь 1611", "Сбор ополчения\nв Нижнем Новгороде"),
        ("2", "Март 1612", "Выступление\nополчения в поход"),
        ("3", "Август 1612", "Подход к Москве,\nбитва с гетманом Ходкевичем"),
        ("4", "Октябрь 1612", "Капитуляция\nпольского гарнизона"),
    ]
    for i, (num, date, desc) in enumerate(steps):
        x = 100 + i * 170
        y = 360
        # Number circle
        add_circle(root, x, y + 10, 16, PRIMARY)
        add_text(root, x, y + 15, num, 14, "#FFFFFF", weight="bold")
        # Date
        add_rect(root, x - 65, y + 32, 130, 18, ROSE_MID, rx=3)
        add_text(root, x, y + 44, date, 10, PRIMARY_DARK, weight="bold")
        # Description
        for j, ln in enumerate(desc.split("\n")):
            add_text(root, x, y + 66 + j * 13, ln, 10, TEXT_MED)

    # Connecting arrows
    for i in range(3):
        x1 = 100 + i * 170 + 20
        add_line(root, x1, y + 10, x1 + 130, y + 10, PRIMARY_LITE, 2, dash="4,3")

    # Bottom: significance
    add_rect(root, 60, 500, 680, 55, "#FFFFFF", rx=6, stroke=PRIMARY, sw=1)
    add_rect(root, 60, 500, 5, 55, PRIMARY)
    add_text(root, 80, 518, "Значение:", 12, PRIMARY, anchor="start", weight="bold")
    add_text(root, 80, 534, "Конец польско-литовской интервенции. 4 ноября — День народного единства.", 11, TEXT_DARK, anchor="start")
    add_text(root, 80, 548, "Победа ополчения открыла путь к восстановлению государственности.", 10, TEXT_MED, anchor="start")

    return root


# ════════════════════════════════════════════════════════════════════════════
#  LESSON 7 — Начало династии Романовых
# ════════════════════════════════════════════════════════════════════════════
def lesson7():
    root = svg_root()
    header_banner(root, "Начало династии Романовых", "Земский собор 1613 года — Михаил Фёдорович")
    footer(root, 7)

    add_rect(root, 0, 76, W, H - 106, ROSE_LIGHT, opacity=0.4)

    # Central event box
    add_rect(root, 200, 90, 400, 70, PRIMARY_DARK, rx=8)
    add_text(root, 400, 118, "Земский собор 1613 года", 17, "#FFFFFF", weight="bold")
    add_text(root, 400, 143, "Избрание Михаила Фёдоровича Романова на царство", 11, "#FFFFFF")

    # Why Romanovs
    add_text(root, W // 2, 190, "Почему Романовы?", 14, PRIMARY_DARK, weight="bold")

    reasons = [
        ("Родство с Иваном IV", "Анастасия Романовна — жена Ивана Грозного"),
        ("Компромиссная фигура", "Устраивал разные политические группы"),
        ("Юность Михаила", "16 лет — легко управлять боярам"),
        ("Незапятнанность", "Не участвовал в интригах Смуты напрямую"),
    ]
    for i, (title, desc) in enumerate(reasons):
        y = 208 + i * 36
        add_rect(root, 100, y, 600, 32, "#FFFFFF", rx=4, stroke="#E5E7EB", sw=1)
        add_rect(root, 100, y, 4, 32, PRIMARY, rx=2)
        add_text(root, 116, y + 14, title, 11, PRIMARY, anchor="start", weight="bold")
        add_text(root, 330, y + 14, "— " + desc, 10, TEXT_MED, anchor="start")

    # Timeline of early Romanovs
    add_text(root, W // 2, 370, "Первые Романовы на русском престоле", 14, PRIMARY_DARK, weight="bold")
    tl_y = 395
    add_line(root, 80, tl_y, W - 80, tl_y, PRIMARY, 3)

    tsars = [
        (130, "1613", "Михаил\nФёдорович"),
        (300, "1645", "Алексей\nМихайлович"),
        (470, "1676", "Фёдор\nАлексеевич"),
        (620, "1682", "Пётр I и\nИван V"),
    ]
    for cx, date, name in tsars:
        add_circle(root, cx, tl_y, 8, PRIMARY, "#FFFFFF", 2)
        add_text(root, cx, tl_y - 14, date, 10, PRIMARY_DARK, weight="bold")
        for i, ln in enumerate(name.split("\n")):
            add_text(root, cx, tl_y + 18 + i * 13, ln, 10, TEXT_DARK)

    # Key reforms of Mikhail
    add_text(root, W // 2, 460, "Деятельность Михаила Фёдоровича (1613–1645)", 13, PRIMARY_DARK, weight="bold")

    reforms = [
        ("Внешняя политика", "Столбовский мир 1617 г. (Швеция)\nДеулинское перемирие 1618 г. (Польша)"),
        ("Внутренняя политика", "Восстановление управления\nВозврат пленных и беженцев"),
        ("Экономика", "Восстановление сельского хозяйства\nНовые таможенные пошлины"),
    ]
    for i, (title, desc) in enumerate(reforms):
        x = 30 + i * 260
        add_rect(root, x, 480, 246, 75, "#FFFFFF", rx=5, stroke=PRIMARY, sw=1)
        add_rect(root, x, 480, 246, 20, PRIMARY, rx=5)
        add_rect(root, x, 496, 246, 4, PRIMARY)
        add_text(root, x + 123, 494, title, 11, "#FFFFFF", weight="bold")
        for j, ln in enumerate(desc.split("\n")):
            add_text(root, x + 123, 516 + j * 14, ln, 9, TEXT_MED)

    return root


# ════════════════════════════════════════════════════════════════════════════
#  LESSON 8 — Соборное уложение 1649 года
# ════════════════════════════════════════════════════════════════════════════
def lesson8():
    root = svg_root()
    header_banner(root, "Соборное уложение 1649 года", "Первый свод законов Русского государства")
    footer(root, 8)

    add_rect(root, 0, 76, W, H - 106, ROSE_LIGHT, opacity=0.4)

    # Main banner
    add_rect(root, 150, 90, 500, 50, PRIMARY_DARK, rx=8)
    add_text(root, 400, 112, "Соборное уложение — кодекс законов", 15, "#FFFFFF", weight="bold")
    add_text(root, 400, 130, "Принято Земским собором при царе Алексее Михайловиче", 10, "#FFFFFF")

    # Structure of the Code
    add_text(root, W // 2, 165, "Структура Соборного уложения", 14, PRIMARY_DARK, weight="bold")

    chapters = [
        ("1", "О blasphemи и церковном суде", "#9F1239"),
        ("2", "О государьской чести", "#9F1239"),
        ("3", "О государевом дворе", PRIMARY_DARK),
        ("4–7", "О служилых людях", PRIMARY),
        ("8–10", "О правосудии", PRIMARY),
        ("11", "О крестьянах (заповедные годы)", PRIMARY_DARK),
        ("12–14", "О суде и розыске", PRIMARY),
        ("15–19", "О вотчинах и поместьях", PRIMARY),
        ("20", "О холопах", "#9F1239"),
    ]
    for i, (num, title, clr) in enumerate(chapters):
        x = 50 + (i % 3) * 245
        y = 180 + (i // 3) * 30
        add_rect(root, x, y, 235, 26, "#FFFFFF", rx=3, stroke=clr, sw=1)
        add_rect(root, x, y, 30, 26, clr, rx=3)
        add_rect(root, x + 26, y, 4, 26, clr)
        add_text(root, x + 15, y + 17, num, 10, "#FFFFFF", weight="bold")
        add_text(root, x + 40, y + 17, title, 9, TEXT_DARK, anchor="start")

    # Key provisions — serfdom
    add_text(root, W // 2, 290, "Ключевые положения", 14, PRIMARY_DARK, weight="bold")

    provisions = [
        ("Окончательное закрепощение крестьян", 
         ["Бессрочный сыск беглых крестьян",
          "Отмена «урочных лет»",
          "Крестьянин — собственность феодала",
          "Запрет перехода к другому помещику"]),
        ("Защита личности царя и государства",
         ["Смертная казнь за измену государю",
          "Наказание за умысел против царя",
          "Запрет перехода на службу к иноземцу",
          "Охрана царского двора"]),
        ("Судебная реформа",
         ["Единые законы для всего государства",
          "Отмена «обельных» привилегий",
          "Состязательный суд и розыск",
          "Регламентация пыток и наказаний"]),
    ]
    for i, (title, lines) in enumerate(provisions):
        x = 30 + i * 258
        add_rect(root, x, 308, 246, 150, "#FFFFFF", rx=6, stroke=PRIMARY, sw=1)
        add_rect(root, x, 308, 246, 24, PRIMARY, rx=6)
        add_rect(root, x, 328, 246, 4, PRIMARY)
        add_text(root, x + 123, 324, title, 10, "#FFFFFF", weight="bold")
        for j, ln in enumerate(lines):
            add_text(root, x + 14, 348 + j * 18, "• " + ln, 10, TEXT_DARK, anchor="start")

    # Historical significance
    add_rect(root, 60, 480, 680, 70, "#FFFFFF", rx=6, stroke=ACCENT_GOLD, sw=2)
    add_rect(root, 60, 480, 5, 70, ACCENT_GOLD)
    add_text(root, 80, 500, "Историческое значение", 13, ACCENT_GOLD, anchor="start", weight="bold")
    add_text(root, 80, 518, "Первый печатный свод законов. Действовало до 1832 года.", 11, TEXT_DARK, anchor="start")
    add_text(root, 80, 534, "Юридически оформило крепостное право в России. Централизовало правовую систему.", 10, TEXT_MED, anchor="start")

    return root


# ════════════════════════════════════════════════════════════════════════════
#  LESSON 9 — Церковный раскол
# ════════════════════════════════════════════════════════════════════════════
def lesson9():
    root = svg_root()
    header_banner(root, "Церковный раскол", "Реформы патриарха Никона и старообрядчество")
    footer(root, 9)

    add_rect(root, 0, 76, W, H - 106, ROSE_LIGHT, opacity=0.4)

    # Central event
    add_rect(root, 170, 90, 460, 50, PRIMARY_DARK, rx=8)
    add_text(root, 400, 112, "Раскол Русской православной церкви", 16, "#FFFFFF", weight="bold")
    add_text(root, 400, 130, "1653–1667 гг. — реформы Никона и сопротивление старообрядцев", 10, "#FFFFFF")

    # Two columns: Nikon vs Old Believers
    add_text(root, 200, 170, "Патриарх Никон", 14, PRIMARY, weight="bold")
    add_text(root, 600, 170, "Старообрядцы", 14, ACCENT_GOLD, weight="bold")

    # Nikon side
    nikon_items = [
        ("Реформа богослужения", "Исправление книг по греческим образцам"),
        ("Троеперстие", "Замена двоеперстия на троеперстное крестное знамение"),
        ("Аллилуйя трижды", "Вместо «аллилуйя» дважды — «трегубая аллилуйя»"),
        ("Имя Христа", "«Иисус» вместо «Исус» — лишняя буква"),
        ("Крестный ход", "Против солнца → по солнцу (посолонь)"),
        ("Поклоны", "Земные поклоны заменены поясными"),
    ]
    for i, (title, desc) in enumerate(nikon_items):
        y = 188 + i * 30
        add_rect(root, 30, y, 370, 27, "#FFFFFF", rx=3, stroke="#E5E7EB", sw=1)
        add_rect(root, 30, y, 3, 27, PRIMARY)
        add_text(root, 42, y + 12, title, 10, PRIMARY, anchor="start", weight="bold")
        add_text(root, 42, y + 23, desc, 8, TEXT_MED, anchor="start")

    # Old Believers side
    old_items = [
        ("Аввакум Петрович", "Лидер старообрядческого движения"),
        ("Двоеперстие", "Старинная форма крестного знамения"),
        ("«Исус»", "Древняя форма написания имени"),
        ("Сопротивление", "«Не приемлем новшеств латинских!»"),
        ("Гонения", "Ссылки, казни, самосожжения"),
        ("Соловецкое восстание", "1668–1676 гг. — монастырь против реформ"),
    ]
    for i, (title, desc) in enumerate(old_items):
        y = 188 + i * 30
        add_rect(root, 410, y, 370, 27, "#FFFFFF", rx=3, stroke="#E5E7EB", sw=1)
        add_rect(root, 410, y, 3, 27, ACCENT_GOLD)
        add_text(root, 422, y + 12, title, 10, ACCENT_GOLD, anchor="start", weight="bold")
        add_text(root, 422, y + 23, desc, 8, TEXT_MED, anchor="start")

    # Timeline
    add_text(root, W // 2, 385, "Хронология раскола", 13, PRIMARY_DARK, weight="bold")
    tl_y = 405
    add_line(root, 80, tl_y, W - 80, tl_y, PRIMARY, 2)

    tl_events = [
        (120, "1653", "Начало\nреформ"),
        (260, "1654", "Книжная\nсправка"),
        (400, "1658", "Разрыв Никона\nс царём"),
        (540, "1666", "Собор,\nосуждение"),
        (680, "1667", "Проклятие\nстарообрядцев"),
    ]
    for cx, date, label in tl_events:
        add_circle(root, cx, tl_y, 6, PRIMARY, "#FFFFFF", 2)
        add_text(root, cx, tl_y - 12, date, 9, PRIMARY_DARK, weight="bold")
        for i, ln in enumerate(label.split("\n")):
            add_text(root, cx, tl_y + 16 + i * 12, ln, 9, TEXT_MED)

    # Bottom significance
    add_rect(root, 60, 460, 680, 85, "#FFFFFF", rx=6, stroke=PRIMARY, sw=1)
    add_rect(root, 60, 460, 5, 85, PRIMARY)
    add_text(root, 80, 480, "Последствия раскола", 13, PRIMARY, anchor="start", weight="bold")
    add_text(root, 80, 498, "• Разделение русского общества на два лагеря — никониане и старообрядцы", 10, TEXT_DARK, anchor="start")
    add_text(root, 80, 514, "• Массовые самосожжения (гари) — до 20 000 погибших", 10, TEXT_DARK, anchor="start")
    add_text(root, 80, 530, "• Формирование старообрядческой культуры, сохранённой до наших дней", 10, TEXT_DARK, anchor="start")

    return root


# ════════════════════════════════════════════════════════════════════════════
#  MAIN — Generate and validate all SVGs
# ════════════════════════════════════════════════════════════════════════════
generators = [
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
for num, gen in generators:
    filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
    root = gen()

    # Write
    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(filepath, encoding="unicode", xml_declaration=True)

    # Validate
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        parsed = ET.fromstring(content)
        size_kb = os.path.getsize(filepath) / 1024
        results.append(f"  ✅ lesson-{num}.svg — valid XML, {size_kb:.1f} KB, tag count: {sum(1 for _ in parsed.iter())}")
    except ET.ParseError as e:
        results.append(f"  ❌ lesson-{num}.svg — XML ERROR: {e}")

print("=" * 60)
print("Grade 7 History SVG Generation Results")
print("=" * 60)
for r in results:
    print(r)
print("=" * 60)
print(f"Total: {len(results)} files in {OUTPUT_DIR}")
print("Done!")
