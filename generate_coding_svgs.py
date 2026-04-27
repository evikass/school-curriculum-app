#!/usr/bin/env python3
"""Generate 12 educational SVG images for Grade 8 Coding (Кодирование) lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/coding"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Color Palette ──────────────────────────────────────────────
EMERALD       = "#10B981"
EMERALD_DARK  = "#059669"
EMERALD_LIGHT = "#34D399"
TEAL          = "#14B8A6"
TEAL_DARK     = "#0D9488"
DARK_BG       = "#1E293B"
DARK_BG2      = "#0F172A"
CODE_BG       = "#1E293B"
SLATE_700     = "#334155"
SLATE_600     = "#475569"
SLATE_400     = "#94A3B8"
SLATE_300     = "#CBD5E1"
WHITE         = "#F8FAFC"
ORANGE        = "#F59E0B"
RED_ACCENT    = "#EF4444"
BLUE_ACCENT   = "#3B82F6"
PURPLE_ACCENT = "#8B5CF6"
YELLOW_ACCENT = "#FBBF24"
PINK_ACCENT   = "#EC4899"
BG_GRAD_TOP   = "#0F172A"
BG_GRAD_BOT   = "#1E293B"

# ── Syntax colors ──────────────────────────────────────────────
SYN_KEYWORD = "#10B981"   # green
SYN_STRING  = "#F59E0B"   # orange
SYN_COMMENT = "#64748B"   # gray
SYN_FUNC    = "#60A5FA"   # light blue
SYN_NUMBER  = "#C084FC"   # purple
SYN_BUILTIN = "#38BDF8"   # sky
SYN_OP      = "#F472B6"   # pink
SYN_DEFAULT = "#E2E8F0"   # light gray

def esc(text):
    """XML-escape text."""
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&apos;"))

def svg_root():
    """Create base SVG element with defs."""
    svg = ET.Element("svg")
    svg.set("xmlns", "http://www.w3.org/2000/svg")
    svg.set("width", "800")
    svg.set("height", "600")
    svg.set("viewBox", "0 0 800 600")
    svg.set("font-family", "'Segoe UI', Arial, sans-serif")

    # Defs: gradients, filters
    defs = ET.SubElement(svg, "defs")

    # Background gradient
    bg = ET.SubElement(defs, "linearGradient", id="bgGrad", x1="0%", y1="0%", x2="0%", y2="100%")
    ET.SubElement(bg, "stop", offset="0%", **{"stop-color": BG_GRAD_TOP})
    ET.SubElement(bg, "stop", offset="100%", **{"stop-color": BG_GRAD_BOT})

    # Header gradient
    hg = ET.SubElement(defs, "linearGradient", id="headerGrad", x1="0%", y1="0%", x2="100%", y2="0%")
    ET.SubElement(hg, "stop", offset="0%", **{"stop-color": EMERALD_DARK})
    ET.SubElement(hg, "stop", offset="100%", **{"stop-color": TEAL_DARK})

    # Card glow
    filt = ET.SubElement(defs, "filter", id="glow", x="-5%", y="-5%", width="110%", height="110%")
    gb = ET.SubElement(filt, "feGaussianBlur", stdDeviation="3", result="blur")
    merge = ET.SubElement(filt, "feMerge")
    ET.SubElement(merge, "feMergeNode", **{"in": "blur"})
    ET.SubElement(merge, "feMergeNode", **{"in": "SourceGraphic"})

    # Shadow
    shfilt = ET.SubElement(defs, "filter", id="shadow", x="-5%", y="-5%", width="115%", height="115%")
    ET.SubElement(shfilt, "feDropShadow", dx="2", dy="2", stdDeviation="3", **{"flood-color": "#000000", "flood-opacity": "0.4"})

    # Accent gradient
    ag = ET.SubElement(defs, "linearGradient", id="accentGrad", x1="0%", y1="0%", x2="100%", y2="100%")
    ET.SubElement(ag, "stop", offset="0%", **{"stop-color": EMERALD})
    ET.SubElement(ag, "stop", offset="100%", **{"stop-color": TEAL})

    return svg, defs

def add_bg(svg):
    """Add background rectangle."""
    rect = ET.SubElement(svg, "rect", width="800", height="600", fill="url(#bgGrad)")
    return rect

def add_header(svg, title, subtitle="", lesson_num=1):
    """Add header bar with lesson number and title."""
    # Header background
    ET.SubElement(svg, "rect", x="0", y="0", width="800", height="70", fill="url(#headerGrad)", rx="0")
    # Decorative line
    ET.SubElement(svg, "rect", x="0", y="70", width="800", height="3", fill=EMERALD_LIGHT)

    # Lesson badge
    ET.SubElement(svg, "circle", cx="45", cy="35", r="25", fill=DARK_BG, stroke=EMERALD_LIGHT, **{"stroke-width": "2"})
    ET.SubElement(svg, "text", x="45", y="42", fill=EMERALD_LIGHT, **{"font-size": "20", "font-weight": "bold", "text-anchor": "middle", "font-family": "monospace"}).text = str(lesson_num)

    # Title
    ET.SubElement(svg, "text", x="85", y="32", fill="white", **{"font-size": "22", "font-weight": "bold"}).text = title
    if subtitle:
        ET.SubElement(svg, "text", x="85", y="54", fill=SLATE_300, **{"font-size": "14"}).text = subtitle

    # Python logo hint - small snake icon
    ET.SubElement(svg, "circle", cx="760", cy="35", r="20", fill=DARK_BG, stroke=EMERALD, **{"stroke-width": "1.5"})
    ET.SubElement(svg, "text", x="760", y="42", fill=EMERALD, **{"font-size": "18", "font-weight": "bold", "text-anchor": "middle", "font-family": "monospace"}).text = "Py"

def add_code_box(svg, x, y, w, h, code_lines, title="Python"):
    """Add a code editor box with syntax-highlighted code.
    code_lines: list of tuples [(text, color), ...] per line, or just strings (default color).
    """
    # Outer container
    ET.SubElement(svg, "rect", x=str(x), y=str(y), width=str(w), height=str(h), rx="8",
                  fill=CODE_BG, stroke=SLATE_700, **{"stroke-width": "1", "filter": "url(#shadow)"})
    # Title bar
    ET.SubElement(svg, "rect", x=str(x), y=str(y), width=str(w), height="28", rx="8",
                  fill=SLATE_700)
    ET.SubElement(svg, "rect", x=str(x), y=str(y+20), width=str(w), height="8",
                  fill=SLATE_700)
    # Dots
    for i, color in enumerate([RED_ACCENT, YELLOW_ACCENT, EMERALD]):
        ET.SubElement(svg, "circle", cx=str(x+16+i*20), cy=str(y+14), r="5", fill=color)
    # Title
    ET.SubElement(svg, "text", x=str(x+w//2), y=str(y+19), fill=SLATE_400,
                  **{"font-size": "11", "text-anchor": "middle", "font-family": "monospace"}).text = title

    # Code lines
    line_y = y + 44
    for line in code_lines:
        if isinstance(line, str):
            ET.SubElement(svg, "text", x=str(x+14), y=str(line_y), fill=SYN_DEFAULT,
                          **{"font-size": "13", "font-family": "monospace"}).text = esc(line)
        elif isinstance(line, list):
            # list of (text, color) tuples
            cx = x + 14
            for segment, color in line:
                if segment:
                    ET.SubElement(svg, "text", x=str(cx), y=str(line_y), fill=color,
                                  **{"font-size": "13", "font-family": "monospace"}).text = esc(segment)
                    # Estimate width
                    cx += len(segment) * 7.8
        line_y += 20

def add_concept_box(svg, x, y, w, h, title, items, accent=EMERALD):
    """Add a concept/key points box."""
    # Box
    ET.SubElement(svg, "rect", x=str(x), y=str(y), width=str(w), height=str(h), rx="8",
                  fill=DARK_BG2, stroke=accent, **{"stroke-width": "2", "filter": "url(#shadow)"})
    # Accent bar
    ET.SubElement(svg, "rect", x=str(x), y=str(y), width="4", height=str(h), rx="2", fill=accent)
    # Title
    ET.SubElement(svg, "text", x=str(x+16), y=str(y+22), fill=accent,
                  **{"font-size": "14", "font-weight": "bold"}).text = title
    # Items
    iy = y + 40
    for item in items:
        ET.SubElement(svg, "text", x=str(x+16), y=str(iy), fill=SLATE_300,
                      **{"font-size": "12"}).text = f"\u2022 {esc(item)}"
        iy += 18

def add_arrow(svg, x1, y1, x2, y2, color=EMERALD_LIGHT):
    """Add a simple arrow line."""
    ET.SubElement(svg, "line", x1=str(x1), y1=str(y1), x2=str(x2), y2=str(y2),
                  stroke=color, **{"stroke-width": "2", "marker-end": "url(#arrowhead)"})
    # Simple triangle arrowhead
    # We'll just draw a small triangle at the end
    dx = x2 - x1
    dy = y2 - y1
    length = (dx*dx + dy*dy) ** 0.5
    if length == 0:
        return
    ux, uy = dx/length, dy/length
    px, py = -uy, ux  # perpendicular
    s = 6  # arrow size
    points = [
        f"{x2},{y2}",
        f"{x2 - ux*s + px*s*0.5},{y2 - uy*s + py*s*0.5}",
        f"{x2 - ux*s - px*s*0.5},{y2 - uy*s - py*s*0.5}",
    ]
    ET.SubElement(svg, "polygon", points=" ".join(points), fill=color)

def add_rounded_box(svg, x, y, w, h, text, fill_color, text_color="white", font_size=14, bold=False):
    """Add a rounded rectangle with centered text."""
    ET.SubElement(svg, "rect", x=str(x), y=str(y), width=str(w), height=str(h), rx="8",
                  fill=fill_color, **{"filter": "url(#shadow)"})
    fw = "bold" if bold else "normal"
    ET.SubElement(svg, "text", x=str(x+w//2), y=str(y+h//2+5), fill=text_color,
                  **{"font-size": str(font_size), "font-weight": fw, "text-anchor": "middle"}).text = esc(text)

def add_diamond(svg, cx, cy, w, h, text, fill_color=EMERALD, text_color="white"):
    """Add a diamond shape (for flowcharts)."""
    points = [
        f"{cx},{cy-h//2}",
        f"{cx+w//2},{cy}",
        f"{cx},{cy+h//2}",
        f"{cx-w//2},{cy}",
    ]
    ET.SubElement(svg, "polygon", points=" ".join(points), fill=fill_color,
                  stroke="white", **{"stroke-width": "1", "filter": "url(#shadow)"})
    ET.SubElement(svg, "text", x=str(cx), y=str(cy+5), fill=text_color,
                  **{"font-size": "11", "font-weight": "bold", "text-anchor": "middle"}).text = esc(text)

def add_connector(svg, x1, y1, x2, y2, color=SLATE_400):
    """Add connecting line."""
    ET.SubElement(svg, "line", x1=str(x1), y1=str(y1), x2=str(x2), y2=str(y2),
                  stroke=color, **{"stroke-width": "2"})

def add_label(svg, x, y, text, color=SLATE_300, size=12, bold=False):
    """Add a text label."""
    fw = "bold" if bold else "normal"
    ET.SubElement(svg, "text", x=str(x), y=str(y), fill=color,
                  **{"font-size": str(size), "font-weight": fw}).text = esc(text)

def add_footer(svg):
    """Add footer."""
    ET.SubElement(svg, "rect", x="0", y="582", width="800", height="18", fill=SLATE_700, rx="0")
    ET.SubElement(svg, "text", x="400", y="595", fill=SLATE_400,
                  **{"font-size": "10", "text-anchor": "middle"}).text = "8 класс \u2022 Кодирование \u2022 Python"

# ═══════════════════════════════════════════════════════════════
# LESSON GENERATORS
# ═══════════════════════════════════════════════════════════════

def lesson1():
    svg, defs = svg_root()
    add_bg(svg)
    add_header(svg, "Введение в Python", "Что такое программирование, особенности Python, IDLE, первая программа", 1)

    # Left column: What is programming
    add_concept_box(svg, 20, 85, 240, 160, "Что такое программирование?",
                    ["Создание инструкций для компьютера",
                     "Язык программирования — способ общения",
                     "Python — один из самых популярных",
                     "Простой и читаемый синтаксис",
                     "Используется: веб, ИИ, игры, данные"], EMERALD)

    # Middle: Python features
    add_concept_box(svg, 275, 85, 245, 160, "Особенности Python", [
        "Интерпретируемый язык",
        "Динамическая типизация",
        "Кроссплатформенный",
        "Огромная библиотека модулей",
        "Активное сообщество"
    ], TEAL)

    # Right: IDLE info
    add_concept_box(svg, 535, 85, 245, 160, "Среда разработки IDLE", [
        "IDLE — встроенная среда Python",
        "Режим интерпретатора (>>>)",
        "Редактор скриптов",
        "Запуск: F5",
        "Подсветка синтаксиса"
    ], BLUE_ACCENT)

    # Code box: first program
    add_code_box(svg, 20, 260, 370, 200, [
        [(">>> ", SYN_COMMENT), ("print(", SYN_DEFAULT), ('"Привет, мир!"', SYN_STRING), (")", SYN_DEFAULT)],
        "Привет, мир!",
        "",
        [(">>> ", SYN_COMMENT), ("print(", SYN_DEFAULT), ('"Я изучаю Python!"', SYN_STRING), (")", SYN_DEFAULT)],
        "Я изучаю Python!",
        "",
        [("# Первая программа", SYN_COMMENT)],
        [("name = ", SYN_DEFAULT), ("input", SYN_BUILTIN), ("(", SYN_DEFAULT), ('"Как тебя зовут? "', SYN_STRING), (")", SYN_DEFAULT)],
        [("print(", SYN_DEFAULT), ('"Привет, "', SYN_STRING), ("+ name)", SYN_DEFAULT)],
    ], "IDLE — Интерактивный режим")

    # Right side: Execution diagram
    add_label(svg, 430, 285, "Как работает Python:", EMERALD_LIGHT, 14, True)

    boxes = [
        (470, 300, 160, 30, "Исходный код (.py)", SLATE_700),
        (470, 360, 160, 30, "Интерпретатор Python", EMERALD_DARK),
        (470, 420, 160, 30, "Результат выполнения", DARK_BG2),
        (470, 480, 160, 30, "Вывод на экран", BLUE_ACCENT),
    ]
    for bx, by, bw, bh, bt, bc in boxes:
        add_rounded_box(svg, bx, by, bw, bh, bt, bc, font_size=12)

    add_arrow(svg, 550, 330, 550, 358, EMERALD_LIGHT)
    add_arrow(svg, 550, 390, 550, 418, EMERALD_LIGHT)
    add_arrow(svg, 550, 450, 550, 478, EMERALD_LIGHT)

    # Labels for arrows
    add_label(svg, 570, 348, "чтение", SLATE_400, 10)
    add_label(svg, 570, 410, "выполнение", SLATE_400, 10)
    add_label(svg, 570, 468, "вывод", SLATE_400, 10)

    # Fun fact
    add_concept_box(svg, 640, 260, 140, 200, "Интересно!", [
        "Python назван в честь комикта Monty Python",
        "Создан Гвидо ван Россумом в 1991",
        "Философия: import this",
        "Дзен Python: Красивое лучше уродливого"
    ], ORANGE)

    add_footer(svg)
    return svg


def lesson2():
    svg, defs = svg_root()
    add_bg(svg)
    add_header(svg, "Переменные и типы данных", "int, float, str, bool — правила именования", 2)

    # Code box - declaring variables
    add_code_box(svg, 20, 85, 370, 240, [
        [("# Объявление переменных", SYN_COMMENT)],
        [("age = ", SYN_DEFAULT), ("15", SYN_NUMBER)],                # int
        [("height = ", SYN_DEFAULT), ("1.72", SYN_NUMBER)],           # float
        [("name = ", SYN_DEFAULT), ('"Алиса"', SYN_STRING)],          # str
        [("is_student = ", SYN_DEFAULT), ("True", SYN_KEYWORD)],      # bool
        "",
        [("type", SYN_BUILTIN), ("(age)      ", SYN_DEFAULT), ("# ", SYN_COMMENT), ("<class 'int'>", SYN_COMMENT)],
        [("type", SYN_BUILTIN), ("(height)   ", SYN_DEFAULT), ("# ", SYN_COMMENT), ("<class 'float'>", SYN_COMMENT)],
        [("type", SYN_BUILTIN), ("(name)     ", SYN_DEFAULT), ("# ", SYN_COMMENT), ("<class 'str'>", SYN_COMMENT)],
        [("type", SYN_BUILTIN), ("(is_student)", SYN_DEFAULT), ("# ", SYN_COMMENT), ("<class 'bool'>", SYN_COMMENT)],
        "",
        [("# Динамическая типизация", SYN_COMMENT)],
        [("x = ", SYN_DEFAULT), ("10", SYN_NUMBER), ("        # int", SYN_COMMENT)],
        [("x = ", SYN_DEFAULT), ('"текст"', SYN_STRING), ("   # str — можно!", SYN_COMMENT)],
    ], "Переменные в Python")

    # Type cards on the right
    types = [
        ("int", "Целые числа", "-5, 0, 42, 1000", EMERALD),
        ("float", "Дробные числа", "3.14, -0.5, 2.0", BLUE_ACCENT),
        ("str", "Строки (текст)", "'Привет', \"мир\"", ORANGE),
        ("bool", "Логический", "True, False", PURPLE_ACCENT),
    ]
    ty = 85
    for name, desc, examples, color in types:
        ET.SubElement(svg, "rect", x="410", y=str(ty), width="370", height="52", rx="8",
                      fill=DARK_BG2, stroke=color, **{"stroke-width": "2"})
        ET.SubElement(svg, "rect", x="410", y=str(ty), width="80", height="52", rx="8",
                      fill=color)
        # Clip right side of the colored box
        ET.SubElement(svg, "rect", x="460", y=str(ty), width="30", height="52", fill=color)
        add_label(svg, 425, ty+33, name, "white", 16, True)
        add_label(svg, 500, ty+22, desc, WHITE, 13, True)
        add_label(svg, 500, ty+40, examples, SLATE_400, 11)
        ty += 62

    # Naming rules
    add_concept_box(svg, 20, 340, 370, 130, "Правила именования переменных", [
        "Начинается с буквы или _",
        "Может содержать буквы, цифры, _",
        "Нельзя: my-var, 2name, class",
        "Регистрочувствительные: Age != age",
        "Стиль: snake_case (my_variable)"
    ], EMERALD)

    # Type conversion
    add_code_box(svg, 410, 340, 370, 130, [
        [("# Преобразование типов", SYN_COMMENT)],
        [("x = ", SYN_DEFAULT), ("int", SYN_BUILTIN), ("(", SYN_DEFAULT), ('"42"', SYN_STRING), (")   # 42", SYN_COMMENT)],
        [("y = ", SYN_DEFAULT), ("float", SYN_BUILTIN), ("(", SYN_DEFAULT), ("3", SYN_NUMBER), (")     # 3.0", SYN_COMMENT)],
        [("z = ", SYN_DEFAULT), ("str", SYN_BUILTIN), ("(", SYN_DEFAULT), ("100", SYN_NUMBER), (")    # '100'", SYN_COMMENT)],
        "",
        [("age_str = ", SYN_DEFAULT), ("input", SYN_BUILTIN), ("(", SYN_DEFAULT), ('"Возраст: "', SYN_STRING), (")", SYN_DEFAULT)],
        [("age = ", SYN_DEFAULT), ("int", SYN_BUILTIN), ("(age_str)", SYN_DEFAULT)],
    ], "Преобразование типов")

    # Memory model
    add_label(svg, 20, 490, "Модель памяти:", EMERALD_LIGHT, 14, True)

    vars = [("age", "15", EMERALD), ("height", "1.72", BLUE_ACCENT), ("name", '"Алиса"', ORANGE)]
    vx = 20
    for vname, vval, vcol in vars:
        # Variable name box
        add_rounded_box(svg, vx, 505, 100, 28, vname, vcol, font_size=12, bold=True)
        # Arrow
        add_arrow(svg, vx+50, 533, vx+50, 548, vcol)
        # Value box
        add_rounded_box(svg, vx+10, 550, 80, 25, vval, DARK_BG, SLATE_300, 11)
        vx += 130

    add_footer(svg)
    return svg


def lesson3():
    svg, defs = svg_root()
    add_bg(svg)
    add_header(svg, "Арифметические операции", "+, -, *, /, //, %, ** — порядок операций", 3)

    # Operations table
    ops = [
        ("+", "Сложение", "5 + 3 = 8", EMERALD),
        ("-", "Вычитание", "10 - 4 = 6", BLUE_ACCENT),
        ("*", "Умножение", "6 * 7 = 42", ORANGE),
        ("/", "Деление", "15 / 4 = 3.75", PURPLE_ACCENT),
        ("//", "Целое деление", "15 // 4 = 3", TEAL),
        ("%", "Остаток", "15 % 4 = 3", PINK_ACCENT),
        ("**", "Степень", "2 ** 10 = 1024", RED_ACCENT),
    ]

    oy = 85
    for sym, name, example, color in ops:
        ET.SubElement(svg, "rect", x="20", y=str(oy), width="380", height="36", rx="6",
                      fill=DARK_BG2, stroke=SLATE_700, **{"stroke-width": "1"})
        ET.SubElement(svg, "rect", x="20", y=str(oy), width="50", height="36", rx="6", fill=color)
        ET.SubElement(svg, "rect", x="50", y=str(oy), width="20", height="36", fill=color)
        add_label(svg, 30, oy+25, sym, "white", 16, True)
        add_label(svg, 80, oy+24, name, WHITE, 13)
        add_label(svg, 280, oy+24, example, SYN_NUMBER, 13, True)
        oy += 42

    # Code box with operations
    add_code_box(svg, 420, 85, 360, 200, [
        [("# Арифметика в Python", SYN_COMMENT)],
        [("a = ", SYN_DEFAULT), ("17", SYN_NUMBER)],
        [("b = ", SYN_DEFAULT), ("5", SYN_NUMBER)],
        "",
        [("print", SYN_BUILTIN), ("(a + b)  ", SYN_DEFAULT), ("# 22", SYN_COMMENT)],
        [("print", SYN_BUILTIN), ("(a - b)  ", SYN_DEFAULT), ("# 12", SYN_COMMENT)],
        [("print", SYN_BUILTIN), ("(a * b)  ", SYN_DEFAULT), ("# 85", SYN_COMMENT)],
        [("print", SYN_BUILTIN), ("(a / b)  ", SYN_DEFAULT), ("# 3.4", SYN_COMMENT)],
        [("print", SYN_BUILTIN), ("(a // b) ", SYN_DEFAULT), ("# 3", SYN_COMMENT)],
        [("print", SYN_BUILTIN), ("(a % b)  ", SYN_DEFAULT), ("# 2", SYN_COMMENT)],
    ], "Операции в коде")

    # Order of operations
    add_concept_box(svg, 420, 300, 360, 160, "Приоритет операций", [
        "1. ** (степень) — высший",
        "2. *, /, //, % (умножение/деление)",
        "3. +, - (сложение/вычитание)",
        "4. Скобки () меняют порядок",
        "5. Одинаковый приоритет: слева направо",
    ], EMERALD)

    # Example with order
    add_code_box(svg, 20, 395, 380, 90, [
        [("# Порядок операций", SYN_COMMENT)],
        [("result = ", SYN_DEFAULT), ("2", SYN_NUMBER), (" + ", SYN_DEFAULT), ("3", SYN_NUMBER), (" * ", SYN_DEFAULT), ("4", SYN_NUMBER), ("   # = 14, не 20", SYN_COMMENT)],
        [("result = ", SYN_DEFAULT), ("(", SYN_DEFAULT), ("2", SYN_NUMBER), (" + ", SYN_DEFAULT), ("3", SYN_NUMBER), (")", SYN_DEFAULT), (" * ", SYN_DEFAULT), ("4", SYN_NUMBER), ("   # = 20", SYN_COMMENT)],
    ], "Скобки меняют порядок!")

    # Fun formula
    add_label(svg, 20, 510, "Полезные формулы:", EMERALD_LIGHT, 14, True)
    add_code_box(svg, 20, 520, 380, 55, [
        [("seconds = hours * ", SYN_DEFAULT), ("60", SYN_NUMBER), (" * ", SYN_DEFAULT), ("60", SYN_NUMBER)],
        [("avg = (a + b + c) / ", SYN_DEFAULT), ("3", SYN_NUMBER)],
    ], "Примеры")

    add_footer(svg)
    return svg


def lesson4():
    svg, defs = svg_root()
    add_bg(svg)
    add_header(svg, "Условные операторы", "if / elif / else — операторы сравнения и логика", 4)

    # Code box
    add_code_box(svg, 20, 85, 380, 230, [
        [("age = ", SYN_DEFAULT), ("int", SYN_BUILTIN), ("(", SYN_DEFAULT), ("input", SYN_BUILTIN), ("(", SYN_DEFAULT), ('"Возраст: "', SYN_STRING), ("))", SYN_DEFAULT)],
        "",
        [("if", SYN_KEYWORD), (" age >= ", SYN_DEFAULT), ("18", SYN_NUMBER), (":", SYN_DEFAULT)],
        [("    print", SYN_BUILTIN), ("(", SYN_DEFAULT), ('"Доступ разрешён"', SYN_STRING), (")", SYN_DEFAULT)],
        [("elif", SYN_KEYWORD), (" age >= ", SYN_DEFAULT), ("14", SYN_NUMBER), (":", SYN_DEFAULT)],
        [("    print", SYN_BUILTIN), ("(", SYN_DEFAULT), ('"С разрешением родителей"', SYN_STRING), (")", SYN_DEFAULT)],
        [("else", SYN_KEYWORD), (":", SYN_DEFAULT)],
        [("    print", SYN_BUILTIN), ("(", SYN_DEFAULT), ('"Доступ запрещён"', SYN_STRING), (")", SYN_DEFAULT)],
        "",
        [("# Тернарный оператор", SYN_COMMENT)],
        [("status = ", SYN_DEFAULT), ('"взрослый"', SYN_STRING), (" if age >= ", SYN_DEFAULT), ("18", SYN_NUMBER), (" else ", SYN_DEFAULT), ('"ребёнок"', SYN_STRING)],
    ], "Условные операторы")

    # Flowchart on the right
    add_label(svg, 440, 100, "Блок-схема:", EMERALD_LIGHT, 14, True)

    # Start
    add_rounded_box(svg, 480, 110, 120, 28, "Начало", SLATE_700, font_size=11)
    add_connector(svg, 540, 138, 540, 155)

    # Diamond 1
    add_diamond(svg, 540, 190, 140, 50, "age >= 18?", EMERALD)
    add_label(svg, 475, 185, "Да", EMERALD_LIGHT, 11, True)
    add_label(svg, 610, 185, "Нет", RED_ACCENT, 11, True)

    # Yes branch
    add_connector(svg, 470, 190, 420, 190)
    add_rounded_box(svg, 340, 175, 130, 30, "Доступ разрешён", EMERALD_DARK, font_size=10)

    # No branch
    add_connector(svg, 610, 190, 660, 190)
    add_diamond(svg, 720, 240, 120, 45, "age >= 14?", BLUE_ACCENT)

    add_connector(svg, 540, 215, 540, 235)
    add_connector(svg, 540, 235, 720, 235)
    add_connector(svg, 720, 235, 720, 218)

    # Yes2 branch
    add_label(svg, 660, 235, "Да", EMERALD_LIGHT, 10, True)
    add_rounded_box(svg, 610, 275, 130, 30, "С родителями", BLUE_ACCENT, font_size=10)
    add_connector(svg, 660, 262, 660, 275)

    # No2 branch
    add_label(svg, 785, 235, "Нет", RED_ACCENT, 10, True)
    add_rounded_box(svg, 620, 320, 130, 30, "Запрещён", RED_ACCENT, font_size=10)
    add_connector(svg, 780, 240, 800, 240)
    add_connector(svg, 800, 240, 800, 335)
    add_connector(svg, 800, 335, 750, 335)

    # Comparison operators
    add_concept_box(svg, 410, 375, 370, 130, "Операторы сравнения", [
        "==  равно        !=  не равно",
        ">   больше       <   меньше",
        ">=  больше/равно  <= меньше/равно",
        "",
        "Логические: and, or, not",
        "if a > 0 and b > 0: ..."
    ], TEAL)

    # Logical operators
    add_concept_box(svg, 20, 330, 380, 120, "Логические операторы", [
        "and — оба условия истинны",
        "or  — хотя бы одно истинно",
        "not — отрицание (инверсия)",
        "if (x > 0) and (x < 10): ...",
        "if (a == 1) or (b == 1): ...",
    ], BLUE_ACCENT)

    # Truth table mini
    add_label(svg, 20, 470, "Таблица истинности:", EMERALD_LIGHT, 13, True)
    # Header
    ET.SubElement(svg, "rect", x="20", y="480", width="380", height="22", rx="4", fill=SLATE_700)
    add_label(svg, 30, 496, "A", WHITE, 11, True)
    add_label(svg, 90, 496, "B", WHITE, 11, True)
    add_label(svg, 150, 496, "A and B", WHITE, 11, True)
    add_label(svg, 260, 496, "A or B", WHITE, 11, True)

    rows = [
        ("True", "True", "True", "True"),
        ("True", "False", "False", "True"),
        ("False", "True", "False", "True"),
        ("False", "False", "False", "False"),
    ]
    ry = 502
    for a, b, aand, aor in rows:
        ET.SubElement(svg, "rect", x="20", y=str(ry), width="380", height="20", rx="0",
                      fill=DARK_BG2, stroke=SLATE_700, **{"stroke-width": "0.5"})
        add_label(svg, 30, ry+14, a, SYN_KEYWORD, 11)
        add_label(svg, 90, ry+14, b, SYN_KEYWORD, 11)
        add_label(svg, 150, ry+14, aand, EMERALD if aand == "True" else RED_ACCENT, 11)
        add_label(svg, 260, ry+14, aor, EMERALD if aor == "True" else RED_ACCENT, 11)
        ry += 20

    add_footer(svg)
    return svg


def lesson5():
    svg, defs = svg_root()
    add_bg(svg)
    add_header(svg, "Цикл for", "range(), итерация по последовательностям, break/continue", 5)

    # Code box - basic for
    add_code_box(svg, 20, 85, 380, 190, [
        [("# Цикл for с range()", SYN_COMMENT)],
        [("for", SYN_KEYWORD), (" i ", SYN_DEFAULT), ("in", SYN_KEYWORD), (" range", SYN_BUILTIN), ("(", SYN_DEFAULT), ("5", SYN_NUMBER), ("):", SYN_DEFAULT)],
        [("    print", SYN_BUILTIN), ("(i)  ", SYN_DEFAULT), ("# 0 1 2 3 4", SYN_COMMENT)],
        "",
        [("for", SYN_KEYWORD), (" i ", SYN_DEFAULT), ("in", SYN_KEYWORD), (" range", SYN_BUILTIN), ("(", SYN_DEFAULT), ("1", SYN_NUMBER), (", ", SYN_DEFAULT), ("6", SYN_NUMBER), ("):", SYN_DEFAULT)],
        [("    print", SYN_BUILTIN), ("(i)  ", SYN_DEFAULT), ("# 1 2 3 4 5", SYN_COMMENT)],
        "",
        [("for", SYN_KEYWORD), (" i ", SYN_DEFAULT), ("in", SYN_KEYWORD), (" range", SYN_BUILTIN), ("(", SYN_DEFAULT), ("0", SYN_NUMBER), (", ", SYN_DEFAULT), ("10", SYN_NUMBER), (", ", SYN_DEFAULT), ("2", SYN_NUMBER), ("):", SYN_DEFAULT)],
        [("    print", SYN_BUILTIN), ("(i)  ", SYN_DEFAULT), ("# 0 2 4 6 8", SYN_COMMENT)],
    ], "for + range()")

    # range() explanation
    add_concept_box(svg, 420, 85, 360, 140, "range(старт, стоп, шаг)", [
        "range(5)        → 0,1,2,3,4",
        "range(1,6)      → 1,2,3,4,5",
        "range(0,10,2)   → 0,2,4,6,8",
        "range(5,0,-1)   → 5,4,3,2,1",
        "Стоп не включается!"
    ], EMERALD)

    # Iterate over string
    add_code_box(svg, 420, 240, 360, 100, [
        [("# Итерация по строке", SYN_COMMENT)],
        [("word = ", SYN_DEFAULT), ('"Привет"', SYN_STRING)],
        [("for", SYN_KEYWORD), (" ch ", SYN_DEFAULT), ("in", SYN_KEYWORD), (" word:", SYN_DEFAULT)],
        [("    print", SYN_BUILTIN), ("(ch)  ", SYN_DEFAULT), ("# П р и в е т", SYN_COMMENT)],
    ], "Итерация по строке")

    # break/continue
    add_code_box(svg, 20, 290, 380, 140, [
        [("# break — выход из цикла", SYN_COMMENT)],
        [("for", SYN_KEYWORD), (" i ", SYN_DEFAULT), ("in", SYN_KEYWORD), (" range", SYN_BUILTIN), ("(100):", SYN_DEFAULT)],
        [("    if", SYN_KEYWORD), (" i == ", SYN_DEFAULT), ("5", SYN_NUMBER), (":", SYN_DEFAULT)],
        [("        break", SYN_KEYWORD), ("  # выход", SYN_COMMENT)],
        "",
        [("# continue — пропуск итерации", SYN_COMMENT)],
        [("for", SYN_KEYWORD), (" i ", SYN_DEFAULT), ("in", SYN_KEYWORD), (" range", SYN_BUILTIN), ("(10):", SYN_DEFAULT)],
        [("    if", SYN_KEYWORD), (" i % ", SYN_DEFAULT), ("2", SYN_NUMBER), (" == ", SYN_DEFAULT), ("0", SYN_NUMBER), (":", SYN_DEFAULT)],
        [("        continue", SYN_KEYWORD), ("  # чётные пропускаем", SYN_COMMENT)],
    ], "break и continue")

    # Flowchart for loop
    add_label(svg, 430, 360, "Блок-схема for:", EMERALD_LIGHT, 14, True)

    add_rounded_box(svg, 480, 375, 120, 28, "i в range()", EMERALD_DARK, font_size=10)
    add_connector(svg, 540, 403, 540, 420)

    add_diamond(svg, 540, 445, 120, 40, "есть i?", EMERALD)
    add_connector(svg, 540, 465, 540, 485)
    add_label(svg, 555, 478, "Да", EMERALD_LIGHT, 10, True)

    add_rounded_box(svg, 480, 490, 120, 28, "Тело цикла", BLUE_ACCENT, font_size=10)
    add_connector(svg, 480, 504, 430, 504)
    add_connector(svg, 430, 504, 430, 445)
    add_connector(svg, 430, 445, 480, 445)

    # No branch
    add_label(svg, 610, 440, "Нет", RED_ACCENT, 10, True)
    add_connector(svg, 600, 445, 650, 445)
    add_rounded_box(svg, 650, 430, 120, 28, "Конец цикла", SLATE_700, font_size=10)

    # Sum example
    add_code_box(svg, 20, 445, 380, 120, [
        [("# Сумма чисел от 1 до N", SYN_COMMENT)],
        [("n = ", SYN_DEFAULT), ("int", SYN_BUILTIN), ("(input", SYN_DEFAULT), ("(", SYN_DEFAULT), ('"N: "', SYN_STRING), ("))", SYN_DEFAULT)],
        [("total = ", SYN_DEFAULT), ("0", SYN_NUMBER)],
        [("for", SYN_KEYWORD), (" i ", SYN_DEFAULT), ("in", SYN_KEYWORD), (" range", SYN_BUILTIN), ("(", SYN_DEFAULT), ("1", SYN_NUMBER), (", n+", SYN_DEFAULT), ("1", SYN_NUMBER), ("):", SYN_DEFAULT)],
        [("    total += i", SYN_DEFAULT)],
        [("print", SYN_BUILTIN), ("(", SYN_DEFAULT), ('"Сумма:"', SYN_STRING), (", total)", SYN_DEFAULT)],
    ], "Практический пример")

    add_footer(svg)
    return svg


def lesson6():
    svg, defs = svg_root()
    add_bg(svg)
    add_header(svg, "Цикл while", "Условие цикла, бесконечные циклы, паттерны", 6)

    # Basic while
    add_code_box(svg, 20, 85, 380, 170, [
        [("# Цикл while", SYN_COMMENT)],
        [("count = ", SYN_DEFAULT), ("0", SYN_NUMBER)],
        [("while", SYN_KEYWORD), (" count ", SYN_DEFAULT), ("<", SYN_OP), (" ", SYN_DEFAULT), ("5", SYN_NUMBER), (":", SYN_DEFAULT)],
        [("    print", SYN_BUILTIN), ("(count)", SYN_DEFAULT)],
        [("    count += ", SYN_DEFAULT), ("1", SYN_NUMBER)],
        "",
        [("# Вывод: 0 1 2 3 4", SYN_COMMENT)],
        "",
        [("# Условие проверяется ПЕРЕД", SYN_COMMENT)],
        [("# каждой итерацией", SYN_COMMENT)],
    ], "while — цикл с условием")

    # While vs For
    add_concept_box(svg, 420, 85, 360, 170, "while vs for", [
        "for — когда знаем количество повторений",
        "while — когда неизвестно заранее",
        "while нужен для ожидания событий",
        "while True — бесконечный цикл",
        "break для выхода из бесконечного цикла",
        "Обязательно менять условие!"
    ], TEAL)

    # Infinite loop example
    add_code_box(svg, 20, 270, 380, 130, [
        [("# Бесконечный цикл + break", SYN_COMMENT)],
        [("while", SYN_KEYWORD), (" True", SYN_KEYWORD), (":", SYN_DEFAULT)],
        [("    answer = ", SYN_DEFAULT), ("input", SYN_BUILTIN), ("(", SYN_DEFAULT), ('"Выйти? (да/нет): "', SYN_STRING), (")", SYN_DEFAULT)],
        [("    if", SYN_KEYWORD), (" answer == ", SYN_DEFAULT), ('"да"', SYN_STRING), (":", SYN_DEFAULT)],
        [("        break", SYN_KEYWORD)],
        [("print", SYN_BUILTIN), ("(", SYN_DEFAULT), ('"Пока!"', SYN_STRING), (")", SYN_DEFAULT)],
    ], "Бесконечный цикл с break")

    # Guessing game
    add_code_box(svg, 420, 270, 360, 160, [
        [("# Игра: угадай число", SYN_COMMENT)],
        [("import", SYN_KEYWORD), (" random", SYN_DEFAULT)],
        [("secret = random.randint", SYN_BUILTIN), ("(", SYN_DEFAULT), ("1", SYN_NUMBER), (", ", SYN_DEFAULT), ("100", SYN_NUMBER), (")", SYN_DEFAULT)],
        [("guess = ", SYN_DEFAULT), ("0", SYN_NUMBER)],
        "",
        [("while", SYN_KEYWORD), (" guess != secret:", SYN_DEFAULT)],
        [("    guess = ", SYN_DEFAULT), ("int", SYN_BUILTIN), ("(input", SYN_DEFAULT), ("(", SYN_DEFAULT), ('"Угадай: "', SYN_STRING), ("))", SYN_DEFAULT)],
        [("    if", SYN_KEYWORD), (" guess ", SYN_DEFAULT), ("<", SYN_OP), (" secret:", SYN_DEFAULT)],
        [("        print", SYN_BUILTIN), ("(", SYN_DEFAULT), ('"Больше!"', SYN_STRING), (")", SYN_DEFAULT)],
        [("    elif", SYN_KEYWORD), (" guess ", SYN_DEFAULT), (">", SYN_OP), (" secret:", SYN_DEFAULT)],
        [("        print", SYN_BUILTIN), ("(", SYN_DEFAULT), ('"Меньше!"', SYN_STRING), (")", SYN_DEFAULT)],
    ], "Игра: угадай число")

    # Flowchart
    add_label(svg, 20, 420, "Блок-схема while:", EMERALD_LIGHT, 14, True)

    add_rounded_box(svg, 30, 435, 110, 25, "Инициализация", SLATE_700, font_size=10)
    add_connector(svg, 85, 460, 85, 475)

    add_diamond(svg, 85, 500, 120, 40, "Условие?", EMERALD)

    # Yes
    add_label(svg, 25, 497, "Да", EMERALD_LIGHT, 10, True)
    add_connector(svg, 25, 500, -10, 500)
    add_connector(svg, -10, 500, -10, 545)
    add_connector(svg, -10, 545, 30, 545)
    add_rounded_box(svg, 30, 530, 110, 30, "Тело цикла", BLUE_ACCENT, font_size=10)
    # Loop back
    add_connector(svg, 85, 560, 85, 575)
    add_connector(svg, 85, 575, -40, 575)
    add_connector(svg, -40, 575, -40, 500)
    add_connector(svg, -40, 500, 25, 500)

    # No
    add_label(svg, 150, 497, "Нет", RED_ACCENT, 10, True)
    add_connector(svg, 145, 500, 200, 500)
    add_rounded_box(svg, 200, 487, 110, 25, "Конец цикла", SLATE_700, font_size=10)

    # Common patterns
    add_concept_box(svg, 420, 450, 360, 120, "Паттерны циклов", [
        "Счётчик: count = 0; while count < n:",
        "Накопление: total = 0; total += x",
        "Ожидание: while not condition:",
        "Ввод до sentinel: while x != 0:",
        "Флаг: found = False; while not found:"
    ], PURPLE_ACCENT)

    add_footer(svg)
    return svg


def lesson7():
    svg, defs = svg_root()
    add_bg(svg)
    add_header(svg, "Строки", "Индексация, срезы, методы (upper, lower, find, replace)", 7)

    # Indexing visualization
    add_label(svg, 20, 95, "Индексация строки:", EMERALD_LIGHT, 14, True)
    word = "PYTHON"
    wx = 30
    # Positive indices
    for i, ch in enumerate(word):
        ET.SubElement(svg, "rect", x=str(wx), y="105", width="50", height="40", rx="4",
                      fill=EMERALD_DARK if i % 2 == 0 else TEAL_DARK, stroke=EMERALD, **{"stroke-width": "1"})
        add_label(svg, wx+17, y=133, text=ch, color="white", size=18, bold=True)
        add_label(svg, wx+15, y=100, text=str(i), color=EMERALD_LIGHT, size=11, bold=True)
        wx += 55

    # Negative indices
    wx = 30
    for i, ch in enumerate(word):
        add_label(svg, wx+10, y=157, text=str(i - len(word)), color=PINK_ACCENT, size=11, bold=True)
        wx += 55

    # Slicing
    add_code_box(svg, 20, 170, 380, 180, [
        [("s = ", SYN_DEFAULT), ('"PYTHON"', SYN_STRING)],
        "",
        [("s[0]    ", SYN_DEFAULT), ("# 'P'  — первый символ", SYN_COMMENT)],
        [("s[-1]   ", SYN_DEFAULT), ("# 'N'  — последний", SYN_COMMENT)],
        [("s[1:4]  ", SYN_DEFAULT), ("# 'YTH' — с 1 по 3", SYN_COMMENT)],
        [("s[:3]   ", SYN_DEFAULT), ("# 'PYT' — с начала", SYN_COMMENT)],
        [("s[2:]   ", SYN_DEFAULT), ("# 'THON' — до конца", SYN_COMMENT)],
        [("s[::2]  ", SYN_DEFAULT), ("# 'PTO' — каждый 2-й", SYN_COMMENT)],
        [("s[::-1] ", SYN_DEFAULT), ("# 'NOHTYP' — реверс", SYN_COMMENT)],
    ], "Срезы строк [start:stop:step]")

    # String methods
    add_concept_box(svg, 420, 170, 360, 180, "Методы строк", [
        '.upper()   → "PYTHON" (верхний регистр)',
        '.lower()   → "python" (нижний регистр)',
        '.find("TH") → 2 (позиция)',
        '.replace("PY","JS") → "JSTHON"',
        '.split(",") → список частей',
        '.strip()   → убрать пробелы',
        '.len(s)    → длина строки',
        '.count("P") → количество вхождений',
    ], EMERALD)

    # Code box - methods demo
    add_code_box(svg, 20, 365, 380, 150, [
        [("name = ", SYN_DEFAULT), ('"  Алиса  "', SYN_STRING)],
        "",
        [("print", SYN_BUILTIN), ("(name.strip())   ", SYN_DEFAULT), ("# 'Алиса'", SYN_COMMENT)],
        [("print", SYN_BUILTIN), ("(name.upper())   ", SYN_DEFAULT), ("# '  АЛИСА  '", SYN_COMMENT)],
        [("print", SYN_BUILTIN), ("(name.lower())   ", SYN_DEFAULT), ("# '  алиса  '", SYN_COMMENT)],
        "",
        [("text = ", SYN_DEFAULT), ('"Привет, мир!"', SYN_STRING)],
        [("print", SYN_BUILTIN), ("(text.replace", SYN_DEFAULT), ("(", SYN_DEFAULT), ('"мир"', SYN_STRING), (", ", SYN_DEFAULT), ('"Python"', SYN_STRING), ("))", SYN_DEFAULT)],
    ], "Методы строк в действии")

    # Strings are immutable
    add_concept_box(svg, 420, 365, 360, 75, "Важно: строки неизменяемы!", [
        "s[0] = 'J'  → ОШИБКА!",
        "Нужно: s = 'J' + s[1:]",
        "Методы создают новую строку"
    ], RED_ACCENT)

    # Format strings
    add_code_box(svg, 420, 455, 360, 110, [
        [("# Форматирование строк", SYN_COMMENT)],
        [("name = ", SYN_DEFAULT), ('"Миша"', SYN_STRING)],
        [("age = ", SYN_DEFAULT), ("14", SYN_NUMBER)],
        "",
        [("print", SYN_BUILTIN), ("(", SYN_DEFAULT), ("f", SYN_STRING), ('"Привет, {name}!"', SYN_STRING), (")", SYN_DEFAULT)],
        [("print", SYN_BUILTIN), ("(", SYN_DEFAULT), ("f", SYN_STRING), ('"Тебе {age} лет"', SYN_STRING), (")", SYN_DEFAULT)],
    ], "f-строки (Python 3.6+)")

    add_footer(svg)
    return svg


def lesson8():
    svg, defs = svg_root()
    add_bg(svg)
    add_header(svg, "Списки", "Создание, индексация, методы (append, remove, sort)", 8)

    # List creation
    add_code_box(svg, 20, 85, 380, 170, [
        [("# Создание списков", SYN_COMMENT)],
        [("fruits = ", SYN_DEFAULT), ("[", SYN_OP), ('"яблоко"', SYN_STRING), (", ", SYN_OP), ('"банан"', SYN_STRING), (", ", SYN_OP), ('"вишня"', SYN_STRING), ("]", SYN_OP)],
        [("numbers = ", SYN_DEFAULT), ("[", SYN_OP), ("1", SYN_NUMBER), (", ", SYN_OP), ("2", SYN_NUMBER), (", ", SYN_OP), ("3", SYN_NUMBER), (", ", SYN_OP), ("4", SYN_NUMBER), (", ", SYN_OP), ("5", SYN_NUMBER), ("]", SYN_OP)],
        [("mixed = ", SYN_DEFAULT), ("[", SYN_OP), ("1", SYN_NUMBER), (", ", SYN_OP), ('"hi"', SYN_STRING), (", ", SYN_OP), ("True", SYN_KEYWORD), ("]", SYN_OP)],
        [("empty = ", SYN_DEFAULT), ("[]", SYN_OP)],
        "",
        [("print", SYN_BUILTIN), ("(fruits[0])  ", SYN_DEFAULT), ("# 'яблоко'", SYN_COMMENT)],
        [("print", SYN_BUILTIN), ("(fruits[-1]) ", SYN_DEFAULT), ("# 'вишня'", SYN_COMMENT)],
        [("print", SYN_BUILTIN), ("(len(fruits))", SYN_DEFAULT), ("# 3", SYN_COMMENT)],
    ], "Списки в Python")

    # Visual list
    add_label(svg, 420, 100, "Визуализация списка:", EMERALD_LIGHT, 13, True)
    items = ["яблоко", "банан", "вишня", "дыня"]
    lx = 420
    for i, item in enumerate(items):
        ET.SubElement(svg, "rect", x=str(lx), y="115", width="85", height="45", rx="6",
                      fill=DARK_BG2, stroke=EMERALD, **{"stroke-width": "2"})
        add_label(svg, lx+8, 143, item, WHITE, 11, True)
        add_label(svg, lx+30, 110, str(i), EMERALD_LIGHT, 10, True)
        add_label(svg, lx+25, 168, str(i-len(items)), PINK_ACCENT, 10, True)
        lx += 90

    # List methods
    add_concept_box(svg, 420, 190, 360, 170, "Методы списков", [
        ".append(x)    — добавить в конец",
        ".insert(i, x) — вставить по индексу",
        ".remove(x)    — удалить по значению",
        ".pop(i)       — удалить по индексу",
        ".sort()       — сортировка на месте",
        ".reverse()    — реверс списка",
        ".count(x)     — количество x",
        ".index(x)     — индекс элемента",
    ], EMERALD)

    # Methods demo
    add_code_box(svg, 20, 270, 380, 200, [
        [("fruits = ", SYN_DEFAULT), ("[", SYN_OP), ('"яблоко"', SYN_STRING), (", ", SYN_OP), ('"банан"', SYN_STRING), ("]", SYN_OP)],
        "",
        [("fruits.append", SYN_DEFAULT), ("(", SYN_DEFAULT), ('"вишня"', SYN_STRING), (")", SYN_DEFAULT), ("  # +в конец", SYN_COMMENT)],
        [("fruits.insert", SYN_DEFAULT), ("(", SYN_DEFAULT), ("1", SYN_NUMBER), (", ", SYN_DEFAULT), ('"киви"', SYN_STRING), (")", SYN_DEFAULT), (" # на позицию 1", SYN_COMMENT)],
        "",
        [("# ['яблоко', 'киви', 'банан', 'вишня']", SYN_COMMENT)],
        "",
        [("fruits.sort()", SYN_DEFAULT), ("  # сортировка", SYN_COMMENT)],
        [("fruits.reverse()", SYN_DEFAULT), ("  # реверс", SYN_COMMENT)],
        "",
        [("nums = [", SYN_DEFAULT), ("3", SYN_NUMBER), (", ", SYN_DEFAULT), ("1", SYN_NUMBER), (", ", SYN_DEFAULT), ("4", SYN_NUMBER), (", ", SYN_DEFAULT), ("1", SYN_NUMBER), (", ", SYN_DEFAULT), ("5", SYN_NUMBER), ("]", SYN_DEFAULT)],
        [("nums.sort()", SYN_DEFAULT), ("  # [1, 1, 3, 4, 5]", SYN_COMMENT)],
    ], "Методы списков")

    # List comprehension
    add_code_box(svg, 20, 485, 380, 85, [
        [("# Генератор списка (list comprehension)", SYN_COMMENT)],
        [("squares = [", SYN_DEFAULT), ("i**", SYN_NUMBER), ("2", SYN_NUMBER), (" for i in range", SYN_BUILTIN), ("(", SYN_DEFAULT), ("10", SYN_NUMBER), (")]", SYN_DEFAULT)],
        [("# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]", SYN_COMMENT)],
        "",
        [("evens = [i for i in range", SYN_BUILTIN), ("(", SYN_DEFAULT), ("20", SYN_NUMBER), (") if i % ", SYN_DEFAULT), ("2", SYN_NUMBER), (" == ", SYN_DEFAULT), ("0", SYN_NUMBER), ("]", SYN_DEFAULT)],
    ], "List Comprehension")

    # Slice visual
    add_label(svg, 420, 375, "Срезы списков:", EMERALD_LIGHT, 13, True)
    add_code_box(svg, 420, 390, 360, 80, [
        [("nums = [", SYN_DEFAULT), ("0", SYN_NUMBER), (", ", SYN_DEFAULT), ("1", SYN_NUMBER), (", ", SYN_DEFAULT), ("2", SYN_NUMBER), (", ", SYN_DEFAULT), ("3", SYN_NUMBER), (", ", SYN_DEFAULT), ("4", SYN_NUMBER), (", ", SYN_DEFAULT), ("5", SYN_NUMBER), ("]", SYN_DEFAULT)],
        [("nums[1:4]  ", SYN_DEFAULT), ("# [1, 2, 3]", SYN_COMMENT)],
        [("nums[::2]  ", SYN_DEFAULT), ("# [0, 2, 4]", SYN_COMMENT)],
    ], "Срезы")

    add_footer(svg)
    return svg


def lesson9():
    svg, defs = svg_root()
    add_bg(svg)
    add_header(svg, "Словари", "Ключ-значение, методы, итерация, практические примеры", 9)

    # Dict creation
    add_code_box(svg, 20, 85, 380, 170, [
        [("# Создание словаря", SYN_COMMENT)],
        [("student = {", SYN_DEFAULT)],
        [("    ", SYN_DEFAULT), ('"имя"', SYN_STRING), (": ", SYN_DEFAULT), ('"Алиса"', SYN_STRING), (",", SYN_DEFAULT)],
        [("    ", SYN_DEFAULT), ('"возраст"', SYN_STRING), (": ", SYN_DEFAULT), ("14", SYN_NUMBER), (",", SYN_DEFAULT)],
        [("    ", SYN_DEFAULT), ('"класс"', SYN_STRING), (": ", SYN_DEFAULT), ('"8А"', SYN_STRING), (",", SYN_DEFAULT)],
        [("    ", SYN_DEFAULT), ('"оценки"', SYN_STRING), (": [", SYN_DEFAULT), ("5", SYN_NUMBER), (", ", SYN_DEFAULT), ("4", SYN_NUMBER), (", ", SYN_DEFAULT), ("5", SYN_NUMBER), ("]", SYN_DEFAULT)],
        ("}", ),
        "",
        [("print", SYN_BUILTIN), ("(student[", SYN_DEFAULT), ('"имя"', SYN_STRING), ("])  ", SYN_DEFAULT), ("# 'Алиса'", SYN_COMMENT)],
    ], "Словари в Python")

    # Visual dictionary
    add_label(svg, 420, 100, "Структура словаря:", EMERALD_LIGHT, 13, True)
    pairs = [("имя", "Алиса", EMERALD), ("возраст", "14", BLUE_ACCENT), ("класс", "8А", ORANGE), ("оценки", "[5,4,5]", PURPLE_ACCENT)]
    py = 115
    for key, val, color in pairs:
        # Key box
        add_rounded_box(svg, 420, py, 90, 28, key, color, font_size=11, bold=True)
        add_label(svg, 515, py+19, "→", SLATE_400, 16, True)
        # Value box
        add_rounded_box(svg, 535, py, 120, 28, val, DARK_BG2, SLATE_300, 11)
        py += 36

    # Methods
    add_concept_box(svg, 420, 275, 360, 140, "Методы словарей", [
        ".keys()     → все ключи",
        ".values()   → все значения",
        ".items()    → пары (ключ, значение)",
        ".get(k, d)  → значение или d по умолчанию",
        ".pop(k)     → удалить и вернуть",
        '"k" in dict  → проверка ключа',
    ], EMERALD)

    # Iteration
    add_code_box(svg, 20, 270, 380, 140, [
        [("# Итерация по словарю", SYN_COMMENT)],
        [("for", SYN_KEYWORD), (" key ", SYN_DEFAULT), ("in", SYN_KEYWORD), (" student:", SYN_DEFAULT)],
        [("    print", SYN_BUILTIN), ("(key, student[key])", SYN_DEFAULT)],
        "",
        [("# Или через items()", SYN_COMMENT)],
        [("for", SYN_KEYWORD), (" key, value ", SYN_DEFAULT), ("in", SYN_KEYWORD), (" student.items():", SYN_DEFAULT)],
        [("    print", SYN_BUILTIN), ("(", SYN_DEFAULT), ("f", SYN_STRING), ('"{key}: {value}"', SYN_STRING), (")", SYN_DEFAULT)],
    ], "Итерация по словарю")

    # Practical example
    add_code_box(svg, 20, 425, 380, 150, [
        [("# Подсчёт частоты символов", SYN_COMMENT)],
        [("text = ", SYN_DEFAULT), ('"привет мир"', SYN_STRING)],
        [("freq = {}", SYN_DEFAULT)],
        "",
        [("for", SYN_KEYWORD), (" ch ", SYN_DEFAULT), ("in", SYN_KEYWORD), (" text:", SYN_DEFAULT)],
        [("    if", SYN_KEYWORD), (" ch ", SYN_DEFAULT), ("in", SYN_KEYWORD), (" freq:", SYN_DEFAULT)],
        [("        freq[ch] += ", SYN_DEFAULT), ("1", SYN_NUMBER)],
        [("    else", SYN_KEYWORD), (":", SYN_DEFAULT)],
        [("        freq[ch] = ", SYN_DEFAULT), ("1", SYN_NUMBER)],
        "",
        [("print", SYN_BUILTIN), ("(freq)  ", SYN_DEFAULT), ("# {'п':1, 'р':2, ...}", SYN_COMMENT)],
    ], "Практика: частотный словарь")

    # get() method
    add_code_box(svg, 420, 430, 360, 80, [
        [("# Безопасное получение значения", SYN_COMMENT)],
        [("email = student.get", SYN_DEFAULT), ("(", SYN_DEFAULT), ('"email"', SYN_STRING), (", ", SYN_DEFAULT), ('"не указан"', SYN_STRING), (")", SYN_DEFAULT)],
        "",
        [("# Добавление/обновление", SYN_COMMENT)],
        [("student[", SYN_DEFAULT), ('"телефон"', SYN_STRING), ("] = ", SYN_DEFAULT), ('"+7-999..."', SYN_STRING)],
    ], "get() и добавление")

    add_footer(svg)
    return svg


def lesson10():
    svg, defs = svg_root()
    add_bg(svg)
    add_header(svg, "Функции", "def, параметры, return, область видимости, docstrings", 10)

    # Basic function
    add_code_box(svg, 20, 85, 380, 200, [
        [("# Определение функции", SYN_COMMENT)],
        [("def", SYN_KEYWORD), (" greet", SYN_FUNC), ("(name):", SYN_DEFAULT)],
        [('    """Приветствие пользователя"""', SYN_STRING)],
        [("    print", SYN_BUILTIN), ("(", SYN_DEFAULT), ("f", SYN_STRING), ('"Привет, {name}!"', SYN_STRING), (")", SYN_DEFAULT)],
        "",
        [("greet", SYN_FUNC), ("(", SYN_DEFAULT), ('"Алиса"', SYN_STRING), (")  ", SYN_DEFAULT), ("# Привет, Алиса!", SYN_COMMENT)],
        "",
        [("# Функция с возвратом", SYN_COMMENT)],
        [("def", SYN_KEYWORD), (" add", SYN_FUNC), ("(a, b):", SYN_DEFAULT)],
        [("    return", SYN_KEYWORD), (" a + b", SYN_DEFAULT)],
        "",
        [("result = add", SYN_FUNC), ("(", SYN_DEFAULT), ("3", SYN_NUMBER), (", ", SYN_DEFAULT), ("5", SYN_NUMBER), (")  ", SYN_DEFAULT), ("# 8", SYN_COMMENT)],
    ], "Функции в Python")

    # Parameters types
    add_concept_box(svg, 420, 85, 360, 200, "Типы параметров", [
        "Обязательные: def f(a, b):",
        "По умолчанию: def f(a, b=10):",
        "Именованные: f(a=1, b=2)",
        "*args — произвольное кол-во",
        "**kwargs — именованные аргументы",
        "",
        "def f(a, b=0, *args, **kwargs):",
        "  порядок важен!"
    ], EMERALD)

    # Scope
    add_code_box(svg, 20, 300, 380, 150, [
        [("# Область видимости", SYN_COMMENT)],
        [("x = ", SYN_DEFAULT), ("10", SYN_NUMBER), ("  # глобальная", SYN_COMMENT)],
        "",
        [("def", SYN_KEYWORD), (" my_func", SYN_FUNC), ("():", SYN_DEFAULT)],
        [("    x = ", SYN_DEFAULT), ("20", SYN_NUMBER), ("  # локальная", SYN_COMMENT)],
        [("    print", SYN_BUILTIN), ("(x)  ", SYN_DEFAULT), ("# 20 (локальная)", SYN_COMMENT)],
        "",
        [("my_func", SYN_FUNC), ("()", SYN_DEFAULT)],
        [("print", SYN_BUILTIN), ("(x)  ", SYN_DEFAULT), ("# 10 (глобальная)", SYN_COMMENT)],
    ], "Область видимости (scope)")

    # Scope diagram
    add_label(svg, 420, 300, "Области видимости:", EMERALD_LIGHT, 13, True)

    # Global scope
    ET.SubElement(svg, "rect", x="420", y="315", width="360", height="55", rx="8",
                  fill=DARK_BG2, stroke=EMERALD, **{"stroke-width": "2"})
    add_label(svg, 430, 335, "Глобальная область (Global)", EMERALD, 11, True)
    add_label(svg, 430, 355, "x = 10, доступна везде", SLATE_300, 10)

    # Local scope
    ET.SubElement(svg, "rect", x="445", y="375", width="310", height="55", rx="8",
                  fill=DARK_BG2, stroke=BLUE_ACCENT, **{"stroke-width": "2"})
    add_label(svg, 455, 395, "Локальная область (Local)", BLUE_ACCENT, 11, True)
    add_label(svg, 455, 415, "x = 20, только внутри функции", SLATE_300, 10)

    # Built-in
    ET.SubElement(svg, "rect", x="470", y="435", width="260", height="40", rx="8",
                  fill=DARK_BG2, stroke=PURPLE_ACCENT, **{"stroke-width": "2"})
    add_label(svg, 480, 460, "Встроенная (Built-in): print, len, ...", PURPLE_ACCENT, 10)

    # Docstring
    add_code_box(svg, 20, 465, 380, 105, [
        [("def", SYN_KEYWORD), (" calculate_area", SYN_FUNC), ("(radius):", SYN_DEFAULT)],
        [('    """Вычисляет площадь круга.', SYN_STRING)],
        [('    Args: radius (float): радиус', SYN_STRING)],
        [('    Returns: float: площадь круга"""', SYN_STRING)],
        [("    import", SYN_KEYWORD), (" math", SYN_DEFAULT)],
        [("    return", SYN_KEYWORD), (" math.pi * radius**", SYN_NUMBER), ("2", SYN_NUMBER)],
    ], "Docstrings — документация")

    # Why functions
    add_concept_box(svg, 420, 490, 360, 85, "Зачем функции?", [
        "DRY — Don't Repeat Yourself",
        "Переиспользование кода",
        "Читаемость и организация",
        "Тестирование по отдельности"
    ], ORANGE)

    add_footer(svg)
    return svg


def lesson11():
    svg, defs = svg_root()
    add_bg(svg)
    add_header(svg, "Работа с файлами", "open, read, write, with, режимы открытия", 11)

    # File modes
    add_concept_box(svg, 20, 85, 370, 155, "Режимы открытия файлов", [
        "'r' — чтение (по умолчанию)",
        "'w' — запись (создаёт/перезаписывает)",
        "'a' — дописывание в конец",
        "'x' — создание (ошибка если есть)",
        "'r+' — чтение и запись",
        "Добавь 'b' для бинарного: 'rb', 'wb'"
    ], EMERALD)

    # Write to file
    add_code_box(svg, 20, 255, 370, 145, [
        [("# Запись в файл", SYN_COMMENT)],
        [("with", SYN_KEYWORD), (" open", SYN_BUILTIN), ("(", SYN_DEFAULT), ('"data.txt"', SYN_STRING), (", ", SYN_DEFAULT), ('"w"', SYN_STRING), (") ", SYN_DEFAULT), ("as", SYN_KEYWORD), (" f:", SYN_DEFAULT)],
        [("    f.write", SYN_DEFAULT), ("(", SYN_DEFAULT), ('"Привет!\\n"', SYN_STRING), (")", SYN_DEFAULT)],
        [("    f.write", SYN_DEFAULT), ("(", SYN_DEFAULT), ('"Вторая строка\\n"', SYN_STRING), (")", SYN_DEFAULT)],
        "",
        [("# Список строк в файл", SYN_COMMENT)],
        [("lines = [", SYN_DEFAULT), ('"стр1\\n"', SYN_STRING), (", ", SYN_DEFAULT), ('"стр2\\n"', SYN_STRING), ("]", SYN_DEFAULT)],
        [("f.writelines", SYN_DEFAULT), ("(lines)", SYN_DEFAULT)],
    ], "Запись в файл")

    # Read from file
    add_code_box(svg, 410, 85, 370, 175, [
        [("# Чтение файла", SYN_COMMENT)],
        [("with", SYN_KEYWORD), (" open", SYN_BUILTIN), ("(", SYN_DEFAULT), ('"data.txt"', SYN_STRING), (", ", SYN_DEFAULT), ('"r"', SYN_STRING), (") ", SYN_DEFAULT), ("as", SYN_KEYWORD), (" f:", SYN_DEFAULT)],
        [("    content = f.read", SYN_DEFAULT), ("()  ", SYN_DEFAULT), ("# весь файл", SYN_COMMENT)],
        "",
        [("# Построчное чтение", SYN_COMMENT)],
        [("with", SYN_KEYWORD), (" open", SYN_BUILTIN), ("(", SYN_DEFAULT), ('"data.txt"', SYN_STRING), (") ", SYN_DEFAULT), ("as", SYN_KEYWORD), (" f:", SYN_DEFAULT)],
        [("    for", SYN_KEYWORD), (" line ", SYN_DEFAULT), ("in", SYN_KEYWORD), (" f:", SYN_DEFAULT)],
        [("        print", SYN_BUILTIN), ("(line.strip", SYN_DEFAULT), ("())", SYN_DEFAULT)],
        "",
        [("lines = f.readlines", SYN_DEFAULT), ("()  ", SYN_DEFAULT), ("# список строк", SYN_COMMENT)],
    ], "Чтение из файла")

    # File lifecycle diagram
    add_label(svg, 410, 275, "Жизненный цикл файла:", EMERALD_LIGHT, 13, True)
    steps = [
        ("open()", "Открыть файл", EMERALD),
        ("read/write", "Работать с данными", BLUE_ACCENT),
        ("close()", "Закрыть файл", ORANGE),
    ]
    sx = 420
    for func, desc, color in steps:
        add_rounded_box(svg, sx, 290, 110, 35, func, color, font_size=11, bold=True)
        add_label(svg, sx, 338, desc, SLATE_300, 9)
        if func != "close()":
            add_arrow(svg, sx+110, 307, sx+125, 307, EMERALD_LIGHT)
        sx += 125

    # with statement
    add_concept_box(svg, 410, 355, 370, 80, "Конструкция with", [
        "Автоматически закрывает файл!",
        "with open('f.txt') as f:",
        "    # даже при ошибке файл закроется",
        "Лучше всегда использовать with"
    ], TEAL)

    # Practical example
    add_code_box(svg, 20, 415, 380, 160, [
        [("# Практика: подсчёт строк", SYN_COMMENT)],
        [("def", SYN_KEYWORD), (" count_lines", SYN_FUNC), ("(filename):", SYN_DEFAULT)],
        [("    with", SYN_KEYWORD), (" open", SYN_BUILTIN), ("(filename) ", SYN_DEFAULT), ("as", SYN_KEYWORD), (" f:", SYN_DEFAULT)],
        [("        count = ", SYN_DEFAULT), ("0", SYN_NUMBER)],
        [("        for", SYN_KEYWORD), (" line ", SYN_DEFAULT), ("in", SYN_KEYWORD), (" f:", SYN_DEFAULT)],
        [("            count += ", SYN_DEFAULT), ("1", SYN_NUMBER)],
        [("    return", SYN_KEYWORD), (" count", SYN_DEFAULT)],
        "",
        [("# CSV: простая запись", SYN_COMMENT)],
        [("with", SYN_KEYWORD), (" open", SYN_BUILTIN), ("(", SYN_DEFAULT), ('"data.csv"', SYN_STRING), (", ", SYN_DEFAULT), ('"w"', SYN_STRING), (") ", SYN_DEFAULT), ("as", SYN_KEYWORD), (" f:", SYN_DEFAULT)],
        [("    f.write", SYN_DEFAULT), ("(", SYN_DEFAULT), ('"имя,возраст\\n"', SYN_STRING), (")", SYN_DEFAULT)],
        [("    f.write", SYN_DEFAULT), ("(", SYN_DEFAULT), ('"Алиса,14\\n"', SYN_STRING), (")", SYN_DEFAULT)],
    ], "Практический пример")

    # Error handling with files
    add_code_box(svg, 410, 445, 370, 130, [
        [("# Обработка ошибок", SYN_COMMENT)],
        [("try", SYN_KEYWORD), (":", SYN_DEFAULT)],
        [("    with", SYN_KEYWORD), (" open", SYN_BUILTIN), ("(", SYN_DEFAULT), ('"data.txt"', SYN_STRING), (") ", SYN_DEFAULT), ("as", SYN_KEYWORD), (" f:", SYN_DEFAULT)],
        [("        content = f.read", SYN_DEFAULT), ("()", SYN_DEFAULT)],
        [("except", SYN_KEYWORD), (" FileNotFoundError:", SYN_DEFAULT)],
        [("    print", SYN_BUILTIN), ("(", SYN_DEFAULT), ('"Файл не найден!"', SYN_STRING), (")", SYN_DEFAULT)],
        [("except", SYN_KEYWORD), (" PermissionError:", SYN_DEFAULT)],
        [("    print", SYN_BUILTIN), ("(", SYN_DEFAULT), ('"Нет доступа!"', SYN_STRING), (")", SYN_DEFAULT)],
    ], "Обработка ошибок")

    add_footer(svg)
    return svg


def lesson12():
    svg, defs = svg_root()
    add_bg(svg)
    add_header(svg, "Итоговый проект", "Планирование, структура, обзор всех концепций", 12)

    # Project structure
    add_concept_box(svg, 20, 85, 370, 165, "Этапы проекта", [
        "1. Постановка задачи (что делаем?)",
        "2. Проектирование (как делаем?)",
        "3. Написание кода (кодим!)",
        "4. Тестирование (ищем ошибки)",
        "5. Рефакторинг (улучшаем код)",
        "6. Документация (описываем)"
    ], EMERALD)

    # Project example - quiz game
    add_code_box(svg, 20, 265, 370, 195, [
        [("# Проект: Викторина", SYN_COMMENT)],
        "",
        [("def", SYN_KEYWORD), (" load_questions", SYN_FUNC), ("(filename):", SYN_DEFAULT)],
        [("    questions = []", SYN_DEFAULT)],
        [("    with", SYN_KEYWORD), (" open", SYN_BUILTIN), ("(filename) ", SYN_DEFAULT), ("as", SYN_KEYWORD), (" f:", SYN_DEFAULT)],
        [("        for", SYN_KEYWORD), (" line ", SYN_DEFAULT), ("in", SYN_KEYWORD), (" f:", SYN_DEFAULT)],
        [("            parts = line.strip", SYN_DEFAULT), ("().split", SYN_DEFAULT), ("(", SYN_DEFAULT), ('"|"', SYN_STRING), (")", SYN_DEFAULT)],
        [("            questions.append", SYN_DEFAULT), ("(parts)", SYN_DEFAULT)],
        [("    return", SYN_KEYWORD), (" questions", SYN_DEFAULT)],
        "",
        [("def", SYN_KEYWORD), (" play", SYN_FUNC), ("(questions):", SYN_DEFAULT)],
        [("    score = ", SYN_DEFAULT), ("0", SYN_NUMBER)],
    ], "Проект: Викторина (начало)")

    # Review of concepts
    add_label(svg, 420, 95, "Обзор всех концепций:", EMERALD_LIGHT, 14, True)

    concepts = [
        ("Переменные", "int, float, str, bool", EMERALD),
        ("Операции", "+ - * / // % **", BLUE_ACCENT),
        ("Условия", "if / elif / else", ORANGE),
        ("Циклы", "for, while, break", PURPLE_ACCENT),
        ("Строки", "индексация, срезы, методы", PINK_ACCENT),
        ("Списки", "[], append, sort", TEAL),
        ("Словари", "{ключ: значение}", RED_ACCENT),
        ("Функции", "def, return, scope", YELLOW_ACCENT),
        ("Файлы", "open, read, write, with", SLATE_400),
    ]

    cy = 110
    for name, detail, color in concepts:
        ET.SubElement(svg, "rect", x="420", y=str(cy), width="360", height="26", rx="5",
                      fill=DARK_BG2, stroke=color, **{"stroke-width": "1.5"})
        ET.SubElement(svg, "rect", x="420", y=str(cy), width="6", height="26", rx="3", fill=color)
        add_label(svg, 435, cy+18, name, color, 12, True)
        add_label(svg, 550, cy+18, detail, SLATE_300, 11)
        cy += 32

    # Project tips
    add_concept_box(svg, 420, 415, 360, 100, "Советы для проекта", [
        "Разбей задачу на подзадачи",
        "Пиши функции для каждой части",
        "Тестируй каждый шаг",
        "Используй git для версионности",
        "Добавляй комментарии и docstrings"
    ], ORANGE)

    # Continue the quiz game
    add_code_box(svg, 20, 475, 370, 100, [
        [("    for", SYN_KEYWORD), (" q ", SYN_DEFAULT), ("in", SYN_KEYWORD), (" questions:", SYN_DEFAULT)],
        [("        answer = ", SYN_DEFAULT), ("input", SYN_BUILTIN), ("(q[", SYN_NUMBER), ("0", SYN_NUMBER), ("] + ", SYN_DEFAULT), ('" "', SYN_STRING), (")", SYN_DEFAULT)],
        [("        if", SYN_KEYWORD), (" answer == q[", SYN_DEFAULT), ("1", SYN_NUMBER), ("]:", SYN_DEFAULT)],
        [("            score += ", SYN_DEFAULT), ("1", SYN_NUMBER)],
        [("    return", SYN_KEYWORD), (" score", SYN_DEFAULT)],
    ], "Викторина (продолжение)")

    add_footer(svg)
    return svg


# ═══════════════════════════════════════════════════════════════
# MAIN: Generate all 12 lessons
# ═══════════════════════════════════════════════════════════════

def indent_xml(elem, level=0):
    """Add indentation to XML for pretty printing."""
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

generators = [
    lesson1, lesson2, lesson3, lesson4, lesson5, lesson6,
    lesson7, lesson8, lesson9, lesson10, lesson11, lesson12
]

results = []
for i, gen in enumerate(generators, 1):
    filename = f"lesson-{i}.svg"
    filepath = os.path.join(OUTPUT_DIR, filename)
    try:
        svg = gen()
        indent_xml(svg)

        # Validate
        tree = ET.ElementTree(svg)
        ET.indent(tree, space="  ")

        # Write
        tree.write(filepath, encoding="unicode", xml_declaration=True)

        # Re-validate by parsing
        ET.parse(filepath)
        results.append(f"  ✅ {filename} — OK")
    except Exception as e:
        results.append(f"  ❌ {filename} — ERROR: {e}")

print("=" * 60)
print("Grade 8 Coding SVG Generation Results")
print("=" * 60)
for r in results:
    print(r)
print("=" * 60)
print(f"Total: {len(results)} files generated")
print(f"Output: {OUTPUT_DIR}")
