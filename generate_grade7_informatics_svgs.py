#!/usr/bin/env python3
"""Generate Grade 7 Informatics SVG files for all 11 lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/informatics"
WIDTH = 800
HEIGHT = 600

# Color scheme
PRIMARY = "#0EA5E9"
PRIMARY_DARK = "#0369A1"
PRIMARY_LIGHT = "#BAE6FD"
ACCENT = "#38BDF8"
BG_GRAD_TOP = "#0C4A6E"
BG_GRAD_BOT = "#0284C7"
CODE_BG = "#0F172A"
CODE_BORDER = "#1E293B"
TEXT_WHITE = "#FFFFFF"
TEXT_LIGHT = "#E0F2FE"
TEXT_MUTED = "#7DD3FC"
CARD_BG = "#0F172A"
CARD_BG2 = "#1E293B"
HIGHLIGHT = "#FACC15"
GREEN = "#4ADE80"
ORANGE = "#FB923C"
RED = "#F87171"
PURPLE = "#C084FC"


def esc(text):
    """Escape text for XML."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


# ---- SVG building helpers (no f-strings in content, use .format() or concat) ----

def svg_open():
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {} {}" width="{}" height="{}">'.format(WIDTH, HEIGHT, WIDTH, HEIGHT)


def defs():
    return '''<defs>
  <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" style="stop-color:{}"/>
    <stop offset="100%" style="stop-color:{}"/>
  </linearGradient>
  <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" style="stop-color:{}"/>
    <stop offset="100%" style="stop-color:{}"/>
  </linearGradient>
</defs>'''.format(BG_GRAD_TOP, BG_GRAD_BOT, PRIMARY, ACCENT)


def bg_rect():
    return '<rect x="0" y="0" width="{}" height="{}" fill="url(#bg)"/>'.format(WIDTH, HEIGHT)


def R(x, y, w, h, fill, rx=8, stroke=None, sw=1, opacity=None):
    """SVG rect."""
    s = '<rect x="{}" y="{}" width="{}" height="{}" fill="{}" rx="{}"'.format(x, y, w, h, fill, rx)
    if stroke:
        s += ' stroke="{}" stroke-width="{}"'.format(stroke, sw)
    if opacity is not None:
        s += ' opacity="{}"'.format(opacity)
    s += '/>'
    return s


def T(x, y, txt, fill=TEXT_WHITE, size=14, anchor="start", family="sans-serif", weight="normal"):
    """SVG text."""
    return '<text x="{}" y="{}" fill="{}" font-size="{}" text-anchor="{}" font-family="{}" font-weight="{}">{}</text>'.format(
        x, y, fill, size, anchor, family, weight, esc(txt))


def header_bar(n, title, subtitle=""):
    parts = []
    parts.append(R(0, 0, WIDTH, 70, "url(#bg)"))
    # lesson number circle
    parts.append('<circle cx="40" cy="35" r="22" fill="{}" stroke="{}" stroke-width="2"/>'.format(PRIMARY, ACCENT))
    parts.append(T(40, 42, str(n), TEXT_WHITE, 18, "middle", "sans-serif", "bold"))
    parts.append(T(72, 32, title, TEXT_WHITE, 22, "start", "sans-serif", "bold"))
    if subtitle:
        parts.append(T(72, 52, subtitle, TEXT_MUTED, 13))
    parts.append(R(0, 68, WIDTH, 2, ACCENT))
    return "\n".join(parts)


def footer_bar():
    parts = []
    parts.append(R(0, HEIGHT - 30, WIDTH, 30, "url(#bg)"))
    parts.append(T(WIDTH / 2, HEIGHT - 10, "\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430 \u00b7 7 \u043a\u043b\u0430\u0441\u0441", TEXT_MUTED, 10, "middle"))
    return "\n".join(parts)


def arrow(x1, y1, x2, y2, color=ACCENT, width=2):
    dx, dy = x2 - x1, y2 - y1
    length = (dx**2 + dy**2)**0.5
    if length == 0:
        return ""
    ux, uy = dx / length, dy / length
    ax1 = x2 - ux * 8 - uy * 4
    ay1 = y2 - uy * 8 + ux * 4
    ax2 = x2 - ux * 8 + uy * 4
    ay2 = y2 - uy * 8 - ux * 4
    return '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="{}" stroke-width="{}"/>\n<polygon points="{},{},{},{},{},{}" fill="{}"/>'.format(
        x1, y1, x2, y2, color, width, x2, y2, ax1, ay1, ax2, ay2, color)


def flow_box(x, y, w, h, label, fill=CARD_BG, tc=TEXT_WHITE):
    parts = []
    parts.append(R(x, y, w, h, fill, rx=6, stroke=PRIMARY, sw=1.5))
    parts.append(T(x + w / 2, y + h / 2 + 5, label, tc, 12, "middle", "sans-serif", "bold"))
    return "\n".join(parts)


def diamond(x, y, w, h, label, fill=CARD_BG, tc=TEXT_WHITE):
    cx, cy = x + w / 2, y + h / 2
    pts = "{},{},{},{},{},{},{},{}".format(cx, y, x + w, cy, cx, y + h, x, cy)
    parts = []
    parts.append('<polygon points="{}" fill="{}" stroke="{}" stroke-width="1.5"/>'.format(pts, fill, PRIMARY))
    parts.append(T(cx, cy + 5, label, tc, 11, "middle", "sans-serif", "bold"))
    return "\n".join(parts)


def badge(x, y, label, color=PRIMARY, tc=TEXT_WHITE, size=11):
    w = len(label) * 7 + 16
    parts = []
    parts.append(R(x, y, w, 20, color, rx=10))
    parts.append(T(x + w / 2, y + 14, label, tc, size, "middle", "sans-serif", "bold"))
    return "\n".join(parts)


def code_block(x, y, w, lines, title="", lh=18, sz=12):
    """Dark code block with line numbers."""
    h = len(lines) * lh + 20
    if title:
        h += 24
    parts = []
    parts.append(R(x, y, w, h, CODE_BG, rx=6, stroke=CODE_BORDER, sw=1))
    ty = y
    if title:
        parts.append(R(x, y, w, 24, CARD_BG2, rx=6))
        parts.append(R(x, y + 18, w, 6, CARD_BG2))
        parts.append(T(x + 10, y + 16, title, TEXT_MUTED, 10, "start", "monospace"))
        parts.append('<circle cx="{}" cy="{}" r="4" fill="{}"/>'.format(x + w - 40, y + 12, RED))
        parts.append('<circle cx="{}" cy="{}" r="4" fill="{}"/>'.format(x + w - 26, y + 12, HIGHLIGHT))
        parts.append('<circle cx="{}" cy="{}" r="4" fill="{}"/>'.format(x + w - 12, y + 12, GREEN))
        ty = y + 24
    for i, line in enumerate(lines):
        ly = ty + 16 + i * lh
        parts.append(T(x + 8, ly, str(i + 1), "#475569", sz, "start", "monospace"))
        parts.append(T(x + 30, ly, line, TEXT_LIGHT, sz, "start", "monospace"))
    return "\n".join(parts)


def wrap(lesson_num, title, subtitle, body_parts):
    """Wrap content into complete SVG."""
    parts = [svg_open(), defs(), bg_rect(), header_bar(lesson_num, title, subtitle)]
    parts.extend(body_parts)
    parts.append(footer_bar())
    parts.append("</svg>")
    return "\n".join(parts)


# ============================================================
# LESSON 1: Введение в программирование
# ============================================================
def lesson_1():
    p = []
    # Left: What is programming
    p.append(R(20, 80, 370, 240, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "Что такое программа?", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(T(35, 124, "Программа \u2014 это набор инструкций для компьютера,", TEXT_LIGHT, 11))
    p.append(T(35, 140, "выполненных на языке программирования.", TEXT_LIGHT, 11))

    # Monitor icon: source code
    p.append('<rect x="35" y="155" width="36" height="28" fill="none" stroke="{}" stroke-width="2" rx="2"/>'.format(ACCENT))
    p.append(T(80, 172, "Исходный код", TEXT_WHITE, 11, "start", "sans-serif", "bold"))
    p.append(T(80, 186, "Текст на языке программирования", TEXT_MUTED, 10))
    p.append(arrow(55, 188, 55, 200, ACCENT))
    p.append(T(65, 196, "компиляция / интерпретация", HIGHLIGHT, 10))
    # Gear icon
    p.append('<circle cx="45" cy="215" r="10" fill="none" stroke="{}" stroke-width="2"/>'.format(ORANGE))
    p.append('<circle cx="45" cy="215" r="4" fill="{}"/>'.format(ORANGE))
    p.append(T(80, 220, "Транслятор", TEXT_WHITE, 11, "start", "sans-serif", "bold"))
    p.append(T(80, 234, "Компилятор или интерпретатор", TEXT_MUTED, 10))
    p.append(arrow(55, 238, 55, 250, ACCENT))
    # Monitor icon: result
    p.append('<rect x="35" y="258" width="36" height="28" fill="none" stroke="{}" stroke-width="2" rx="2"/>'.format(GREEN))
    p.append(T(80, 275, "Результат", TEXT_WHITE, 11, "start", "sans-serif", "bold"))
    p.append(T(80, 289, "Работающая программа", TEXT_MUTED, 10))

    # Right: Programming Languages
    p.append(R(400, 80, 380, 240, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(415, 102, "Языки программирования", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(badge(415, 112, "Python", PRIMARY))
    p.append(badge(490, 112, "JavaScript", "#EAB308"))
    p.append(badge(585, 112, "Java", ORANGE))
    p.append(badge(650, 112, "C++", PURPLE))
    p.append(badge(415, 140, "C#", GREEN))
    p.append(badge(470, 140, "Ruby", RED))
    p.append(badge(530, 140, "Go", "#06B6D4"))
    p.append(badge(580, 140, "Swift", ORANGE))
    p.append(T(415, 180, "Типы языков:", TEXT_WHITE, 12, "start", "sans-serif", "bold"))
    p.append(R(415, 190, 170, 50, CARD_BG2, rx=6, stroke=GREEN, sw=1))
    p.append(T(500, 210, "Компилируемые", GREEN, 11, "middle", "sans-serif", "bold"))
    p.append(T(500, 228, "C++, Go, Rust", TEXT_MUTED, 9, "middle"))
    p.append(R(595, 190, 170, 50, CARD_BG2, rx=6, stroke=ORANGE, sw=1))
    p.append(T(680, 210, "Интерпретируемые", ORANGE, 11, "middle", "sans-serif", "bold"))
    p.append(T(680, 228, "Python, JS, Ruby", TEXT_MUTED, 9, "middle"))
    p.append(T(415, 262, "Среды разработки (IDE):", TEXT_WHITE, 12, "start", "sans-serif", "bold"))
    p.append(badge(415, 272, "PyCharm", PRIMARY))
    p.append(badge(500, 272, "VS Code", "#06B6D4"))
    p.append(badge(585, 272, "IDLE", GREEN))

    # Bottom: First Python program
    p.append(R(20, 330, 760, 240, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 354, "Первая программа на Python", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 365, 460, [
        'print("Привет, мир!")',
        '# Вывод текста на экран',
        'name = input("Как тебя зовут? ")',
        'print("Привет, " + name + "!")',
        '',
        '# Переменные',
        'age = 13',
        'print(f"Мне {age} лет")',
    ], title="hello.py"))
    # Explanation boxes
    p.append(R(510, 370, 255, 35, CARD_BG2, rx=6))
    p.append(T(520, 385, "print()", GREEN, 11, "start", "monospace"))
    p.append(T(520, 398, "Вывод текста на экран", TEXT_MUTED, 10))
    p.append(R(510, 415, 255, 35, CARD_BG2, rx=6))
    p.append(T(520, 430, "input()", GREEN, 11, "start", "monospace"))
    p.append(T(520, 443, "Ввод данных от пользователя", TEXT_MUTED, 10))
    p.append(R(510, 460, 255, 35, CARD_BG2, rx=6))
    p.append(T(520, 475, "# комментарий", HIGHLIGHT, 11, "start", "monospace"))
    p.append(T(520, 488, "Комментарий \u2014 не выполняется", TEXT_MUTED, 10))
    p.append(R(510, 505, 255, 50, CARD_BG2, rx=6))
    p.append(T(520, 520, "Результат:", TEXT_WHITE, 11, "start", "sans-serif", "bold"))
    p.append(T(520, 538, ">>> Привет, мир!", GREEN, 12, "start", "monospace"))
    p.append(T(520, 552, ">>> Привет, Анна!", GREEN, 12, "start", "monospace"))

    return wrap(1, "Введение в программирование", "Что такое программа, языки программирования, IDE", p)


# ============================================================
# LESSON 2: Переменные и типы данных
# ============================================================
def lesson_2():
    p = []
    # Left: Variable concept
    p.append(R(20, 80, 370, 155, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "Что такое переменная?", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(T(35, 122, "Переменная \u2014 именованная ячейка памяти,", TEXT_LIGHT, 11))
    p.append(T(35, 138, "в которой хранится значение.", TEXT_LIGHT, 11))
    # Variable boxes
    p.append('<rect x="35" y="150" width="90" height="40" fill="{}" rx="4" stroke="{}" stroke-width="1.5"/>'.format(CARD_BG2, PRIMARY))
    p.append(T(80, 163, "name", HIGHLIGHT, 11, "middle", "monospace", "bold"))
    p.append(T(80, 183, '"Анна"', TEXT_WHITE, 11, "middle", "monospace"))
    p.append('<rect x="145" y="150" width="70" height="40" fill="{}" rx="4" stroke="{}" stroke-width="1.5"/>'.format(CARD_BG2, GREEN))
    p.append(T(180, 163, "age", GREEN, 11, "middle", "monospace", "bold"))
    p.append(T(180, 183, "13", TEXT_WHITE, 11, "middle", "monospace"))
    p.append('<rect x="235" y="150" width="80" height="40" fill="{}" rx="4" stroke="{}" stroke-width="1.5"/>'.format(CARD_BG2, ORANGE))
    p.append(T(275, 163, "height", ORANGE, 11, "middle", "monospace", "bold"))
    p.append(T(275, 183, "1.58", TEXT_WHITE, 11, "middle", "monospace"))
    p.append('<rect x="335" y="150" width="40" height="40" fill="{}" rx="4" stroke="{}" stroke-width="1.5"/>'.format(CARD_BG2, PURPLE))
    p.append(T(355, 163, "ok", PURPLE, 11, "middle", "monospace", "bold"))
    p.append(T(355, 183, "T", TEXT_WHITE, 11, "middle", "monospace"))

    # Right: Data types
    p.append(R(400, 80, 380, 155, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(415, 102, "Типы данных Python", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(R(415, 112, 170, 50, CARD_BG2, rx=6, stroke=GREEN, sw=1))
    p.append(T(425, 130, "int", GREEN, 12, "start", "monospace", "bold"))
    p.append(T(425, 150, "Целые числа: 13, -5, 0", TEXT_MUTED, 10))
    p.append(R(595, 112, 170, 50, CARD_BG2, rx=6, stroke=ORANGE, sw=1))
    p.append(T(605, 130, "float", ORANGE, 12, "start", "monospace", "bold"))
    p.append(T(605, 150, "Вещественные: 3.14, -0.5", TEXT_MUTED, 10))
    p.append(R(415, 172, 170, 50, CARD_BG2, rx=6, stroke=HIGHLIGHT, sw=1))
    p.append(T(425, 190, "str", HIGHLIGHT, 12, "start", "monospace", "bold"))
    p.append(T(425, 210, 'Строки: "Привет", "123"', TEXT_MUTED, 10))
    p.append(R(595, 172, 170, 50, CARD_BG2, rx=6, stroke=PURPLE, sw=1))
    p.append(T(605, 190, "bool", PURPLE, 12, "start", "monospace", "bold"))
    p.append(T(605, 210, "Логический: True / False", TEXT_MUTED, 10))

    # Middle: Code example
    p.append(R(20, 245, 480, 200, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 267, "Примеры работы с переменными", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 278, 450, [
        "# Целое число",
        "age = 13",
        "x = -7",
        "",
        "# Вещественное число",
        "pi = 3.14",
        "temp = -2.5",
        "",
        "# Строка",
        'name = "Анна"',
        "",
        "# Логический тип",
        "is_student = True",
    ], title="variables.py"))

    # Right: Naming rules
    p.append(R(510, 245, 270, 200, CARD_BG, rx=8, stroke=HIGHLIGHT, sw=1))
    p.append(T(525, 267, "Правила именования", HIGHLIGHT, 14, "start", "sans-serif", "bold"))
    p.append(T(525, 292, "\u2713 my_name, age, x1", GREEN, 11))
    p.append(T(525, 314, "\u2713 Буквы, цифры, _", GREEN, 11))
    p.append(T(525, 336, "\u2713 lowercase_with_underscore", GREEN, 11))
    p.append(T(525, 362, "\u2717 1name (цифра первой)", RED, 11))
    p.append(T(525, 384, "\u2717 my-name (дефис)", RED, 11))
    p.append(T(525, 406, "\u2717 class, for (ключ. слова)", RED, 11))
    p.append(T(525, 432, "type() \u2014 узнать тип переменной", ACCENT, 11, "start", "sans-serif", "bold"))

    # Bottom: type() function
    p.append(R(20, 455, 760, 115, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 477, "Функция type() и преобразование типов", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 488, 380, [
        "x = 42",
        "print(type(x))  # <class 'int'>",
        "y = str(x)  # '42'",
        "z = int('5')  # 5",
        "w = float('3.2')  # 3.2",
    ], title="types.py"))
    p.append(R(430, 493, 340, 65, CARD_BG2, rx=6))
    p.append(T(445, 512, "Преобразование типов:", TEXT_WHITE, 11, "start", "sans-serif", "bold"))
    p.append(T(445, 530, "int() \u2014 в целое число", GREEN, 11, "start", "monospace"))
    p.append(T(445, 548, "float() \u2014 в вещественное", ORANGE, 11, "start", "monospace"))

    return wrap(2, "Переменные и типы данных", "int, float, str, bool, правила именования", p)


# ============================================================
# LESSON 3: Условия и ветвления
# ============================================================
def lesson_3():
    p = []
    # Left: Flowchart
    p.append(R(20, 80, 280, 300, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "Блок-схема ветвления", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(flow_box(105, 112, 110, 30, "Начало", PRIMARY_DARK))
    p.append(arrow(160, 142, 160, 155, ACCENT))
    p.append(diamond(90, 155, 140, 50, "Условие?"))
    p.append(arrow(160, 205, 160, 220, ACCENT))
    p.append(T(165, 218, "Да", GREEN, 9))
    p.append(flow_box(100, 220, 120, 30, "Действие 1", "#166534"))
    p.append(arrow(160, 250, 160, 275, ACCENT))
    p.append(T(233, 182, "Нет", RED, 9))
    p.append(arrow(230, 180, 260, 180, RED))
    p.append(arrow(260, 180, 260, 235, RED))
    p.append(flow_box(200, 235, 80, 30, "Действие 2", "#7F1D1D"))
    p.append(arrow(240, 265, 160, 275, RED))
    p.append(flow_box(105, 275, 110, 30, "Продолжение", PRIMARY_DARK))

    # Right: Comparison operators
    p.append(R(310, 80, 470, 160, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(325, 102, "Операторы сравнения", ACCENT, 14, "start", "sans-serif", "bold"))
    ops = [("==", "равно"), ("!=", "не равно"), (">", "больше"), ("<", "меньше"), (">=", "больше или равно"), ("<=", "меньше или равно")]
    for i, (op, desc) in enumerate(ops):
        col = 0 if i % 2 == 0 else 1
        row = i // 2
        bx = 325 + col * 225
        by = 112 + row * 30
        p.append(R(bx, by, 215, 25, CARD_BG2, rx=4))
        p.append(T(bx + 10, by + 17, op, HIGHLIGHT, 12, "start", "monospace"))
        p.append(T(bx + 55, by + 17, desc, TEXT_LIGHT, 11))
    p.append(R(325, 202, 440, 25, CARD_BG2, rx=4))
    p.append(T(335, 219, "and  or  not", PURPLE, 12, "start", "monospace"))
    p.append(T(445, 219, "логические операторы", TEXT_MUTED, 11))

    # Bottom left: Code
    p.append(R(310, 250, 470, 200, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(325, 272, "Конструкция if / elif / else", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(325, 282, 440, [
        'age = int(input("Возраст: "))',
        '',
        'if age >= 18:',
        '    print("Доступ разрешён")',
        'elif age >= 14:',
        '    print("С согласием родителей")',
        'else:',
        '    print("Доступ запрещён")',
    ], title="conditions.py"))

    # Bottom: Nested conditions
    p.append(R(20, 390, 760, 180, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 412, "Вложенные условия и тернарный оператор", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 422, 370, [
        "# Вложенное условие",
        "if x > 0:",
        "    if x > 10:",
        '        print("Большое")',
        "    else:",
        '        print("Маленькое")',
    ], title="nested.py"))
    p.append(code_block(420, 422, 350, [
        "# Тернарный оператор",
        'msg = "Да" if x > 0 else "Нет"',
        "",
        "# Пример",
        'status = "Взрослый"',
        "    if age >= 18 else",
        '    "Ребёнок"',
    ], title="ternary.py"))

    return wrap(3, "Условия и ветвления", "if / elif / else, операторы сравнения", p)


# ============================================================
# LESSON 4: Циклы в программировании
# ============================================================
def lesson_4():
    p = []
    # Top left: for loop
    p.append(R(20, 80, 380, 245, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "Цикл for", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 112, 350, [
        "# Перебор чисел",
        "for i in range(5):",
        "    print(i)  # 0,1,2,3,4",
        "",
        "# С шагом",
        "for i in range(0, 10, 2):",
        "    print(i)  # 0,2,4,6,8",
        "",
        "# Перебор строки",
        'for ch in "Привет":',
        "    print(ch)",
    ], title="for_loop.py"))

    # Top right: while loop
    p.append(R(410, 80, 370, 245, CARD_BG, rx=8, stroke=ORANGE, sw=1))
    p.append(T(425, 102, "Цикл while", ORANGE, 14, "start", "sans-serif", "bold"))
    p.append(code_block(425, 112, 340, [
        "# Цикл с условием",
        "count = 0",
        "while count < 5:",
        "    print(count)",
        "    count += 1",
        "",
        "# Ввод до стоп-слова",
        'word = ""',
        'while word != "стоп":',
        "    word = input()",
    ], title="while_loop.py"))

    # Middle: break & continue
    p.append(R(20, 335, 380, 130, CARD_BG, rx=8, stroke=RED, sw=1))
    p.append(T(35, 357, "break и continue", RED, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 367, 350, [
        "# break \u2014 выход из цикла",
        "for i in range(10):",
        "    if i == 5:",
        "        break",
        "    print(i)  # 0..4",
        "",
        "# continue \u2014 пропуск шага",
        "for i in range(5):",
        "    if i == 2:",
        "        continue",
        "    print(i)  # 0,1,3,4",
    ], title="control.py", lh=16))

    # Right: Nested loops
    p.append(R(410, 335, 370, 130, CARD_BG, rx=8, stroke=PURPLE, sw=1))
    p.append(T(425, 357, "Вложенные циклы", PURPLE, 14, "start", "sans-serif", "bold"))
    p.append(code_block(425, 367, 340, [
        "# Таблица умножения",
        "for i in range(1, 10):",
        "    for j in range(1, 10):",
        "        print(i*j, end='\\t')",
        "    print()  # новая строка",
        "",
        "# Рисунок звёздочками",
        "for i in range(5):",
        "    print('*' * (i+1))",
    ], title="nested.py", lh=16))

    # Bottom: Comparison table
    p.append(R(20, 475, 760, 95, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 497, "Сравнение циклов", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(R(35, 507, 230, 50, CARD_BG2, rx=6, stroke=PRIMARY, sw=1))
    p.append(T(150, 525, "for", PRIMARY, 12, "middle", "monospace", "bold"))
    p.append(T(150, 543, "Число повторений известно", TEXT_MUTED, 10, "middle"))
    p.append(R(275, 507, 230, 50, CARD_BG2, rx=6, stroke=ORANGE, sw=1))
    p.append(T(390, 525, "while", ORANGE, 12, "middle", "monospace", "bold"))
    p.append(T(390, 543, "Повторяется пока условие True", TEXT_MUTED, 10, "middle"))
    p.append(R(515, 507, 250, 50, CARD_BG2, rx=6, stroke=RED, sw=1))
    p.append(T(640, 525, "break / continue", RED, 12, "middle", "monospace", "bold"))
    p.append(T(640, 543, "Управление внутри цикла", TEXT_MUTED, 10, "middle"))

    return wrap(4, "Циклы в программировании", "for, while, break, continue, вложенные циклы", p)


# ============================================================
# LESSON 5: Основы HTML
# ============================================================
def lesson_5():
    p = []
    # Left: HTML structure
    p.append(R(20, 80, 380, 260, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "Структура HTML-документа", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 112, 350, [
        "<!DOCTYPE html>",
        '<html lang="ru">',
        "<head>",
        '  <meta charset="UTF-8">',
        "  <title>Моя страница</title>",
        "</head>",
        "<body>",
        "  <h1>Привет!</h1>",
        "  <p>Текст абзаца</p>",
        "</body>",
        "</html>",
    ], title="index.html"))

    # Right: Common tags
    p.append(R(410, 80, 370, 260, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(425, 102, "Основные теги HTML", ACCENT, 14, "start", "sans-serif", "bold"))
    tags = [
        ("&lt;h1&gt;-&lt;h6&gt;", "Заголовки", GREEN),
        ("&lt;p&gt;", "Абзац", ACCENT),
        ("&lt;a href&gt;", "Ссылка", HIGHLIGHT),
        ("&lt;img src&gt;", "Изображение", ORANGE),
        ("&lt;ul&gt; &lt;ol&gt;", "Списки", PURPLE),
        ("&lt;div&gt; &lt;span&gt;", "Контейнеры", RED),
    ]
    for i, (tag, desc, color) in enumerate(tags):
        by = 112 + i * 36
        p.append(R(425, by, 165, 30, CARD_BG2, rx=4, stroke=color, sw=1))
        p.append(T(430, by + 19, tag, color, 11, "start", "monospace"))
        p.append(T(600, by + 19, desc, TEXT_MUTED, 10))

    # Bottom left: Attributes
    p.append(R(20, 350, 380, 220, CARD_BG, rx=8, stroke=HIGHLIGHT, sw=1))
    p.append(T(35, 372, "Атрибуты тегов", HIGHLIGHT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 382, 350, [
        '<a href="https://site.ru">Ссылка</a>',
        '',
        '<img src="photo.jpg" alt="Фото">',
        '',
        '<p class="intro" id="main">',
        '  Текст параграфа',
        '</p>',
        '',
        '<input type="text" placeholder="Имя">',
    ], title="attributes.html"))

    # Bottom right: DOM tree
    p.append(R(410, 350, 370, 220, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(425, 372, "DOM-дерево документа", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(flow_box(540, 385, 100, 26, "html", PURPLE))
    p.append(arrow(570, 411, 530, 425, ACCENT))
    p.append(arrow(570, 411, 640, 425, ACCENT))
    p.append(flow_box(480, 425, 90, 26, "head", GREEN))
    p.append(flow_box(620, 425, 90, 26, "body", GREEN))
    p.append(arrow(525, 451, 500, 462, ACCENT))
    p.append(arrow(525, 451, 555, 462, ACCENT))
    p.append(arrow(665, 451, 620, 462, ACCENT))
    p.append(arrow(665, 451, 690, 462, ACCENT))
    p.append(arrow(665, 451, 750, 462, ACCENT))
    p.append(flow_box(455, 462, 80, 24, "title", HIGHLIGHT))
    p.append(flow_box(545, 462, 80, 24, "meta", HIGHLIGHT))
    p.append(flow_box(585, 490, 70, 24, "h1", ORANGE))
    p.append(flow_box(665, 490, 60, 24, "p", ORANGE))
    p.append(flow_box(740, 490, 50, 24, "a", ORANGE))
    p.append(T(425, 530, "Каждый тег \u2014 узел дерева.", TEXT_MUTED, 10))
    p.append(T(425, 545, "Вложенные теги \u2014 дочерние узлы.", TEXT_MUTED, 10))

    return wrap(5, "Основы HTML", "Теги, структура документа, элементы, атрибуты", p)


# ============================================================
# LESSON 6: Основы CSS
# ============================================================
def lesson_6():
    p = []
    # Top left: CSS syntax
    p.append(R(20, 80, 380, 150, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "Синтаксис CSS", ACCENT, 14, "start", "sans-serif", "bold"))
    # CSS rule visual
    p.append(R(35, 112, 350, 40, CARD_BG2, rx=6))
    p.append(T(45, 130, "h1", GREEN, 13, "start", "monospace", "bold"))
    p.append(T(65, 130, "{", TEXT_MUTED, 13, "start", "monospace"))
    p.append(T(75, 148, "  color", ACCENT, 12, "start", "monospace"))
    p.append(T(120, 148, ":", TEXT_MUTED, 12, "start", "monospace"))
    p.append(T(128, 148, " blue", ORANGE, 12, "start", "monospace"))
    p.append(T(155, 148, ";", TEXT_MUTED, 12, "start", "monospace"))
    p.append(T(165, 148, "  font-size", ACCENT, 12, "start", "monospace"))
    p.append(T(240, 148, ":", TEXT_MUTED, 12, "start", "monospace"))
    p.append(T(248, 148, " 24px", ORANGE, 12, "start", "monospace"))
    p.append(T(285, 148, ";", TEXT_MUTED, 12, "start", "monospace"))
    p.append(T(345, 130, "}", TEXT_MUTED, 13, "start", "monospace"))
    # Labels
    p.append(T(50, 175, "селектор", GREEN, 10))
    p.append(T(120, 175, "свойство", ACCENT, 10))
    p.append(T(210, 175, "значение", ORANGE, 10))

    # Top right: Selectors
    p.append(R(410, 80, 370, 150, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(425, 102, "Селекторы CSS", ACCENT, 14, "start", "sans-serif", "bold"))
    sels = [
        ("h1", "По тегу", GREEN),
        (".intro", "По классу", HIGHLIGHT),
        ("#main", "По id", ORANGE),
        ("div p", "Вложенный", PURPLE),
        ("a:hover", "Псевдокласс", RED),
    ]
    for i, (sel, desc, color) in enumerate(sels):
        by = 112 + i * 22
        p.append(T(425, by + 14, sel, color, 11, "start", "monospace", "bold"))
        p.append(T(510, by + 14, desc, TEXT_MUTED, 10))

    # Middle: Code example
    p.append(R(20, 240, 380, 220, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 262, "Пример CSS", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 272, 350, [
        "/* Стили для страницы */",
        "body {",
        "  background: #f0f0f0;",
        "  font-family: Arial;",
        "}",
        "",
        "h1 {",
        "  color: #0EA5E9;",
        "  font-size: 24px;",
        "}",
        "",
        ".highlight {",
        "  background: yellow;",
        "}",
    ], title="style.css"))

    # Right: Colors and units
    p.append(R(410, 240, 370, 220, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(425, 262, "Цвета и единицы", ACCENT, 14, "start", "sans-serif", "bold"))
    # Color examples
    colors = [("#FF0000", "red"), ("#00FF00", "green"), ("#0000FF", "blue"), ("#0EA5E9", "sky"), ("#FACC15", "yellow"), ("#4ADE80", "lime")]
    for i, (hexc, name) in enumerate(colors):
        bx = 425 + (i % 3) * 120
        by = 275 + (i // 3) * 45
        p.append(R(bx, by, 30, 30, hexc, rx=4))
        p.append(T(bx + 35, by + 12, hexc, TEXT_LIGHT, 9, "start", "monospace"))
        p.append(T(bx + 35, by + 25, name, TEXT_MUTED, 8, "start", "monospace"))
    # Units
    p.append(T(425, 380, "Единицы измерения:", TEXT_WHITE, 11, "start", "sans-serif", "bold"))
    units = [("px", "пиксели"), ("em", "относительно шрифта"), ("%", "проценты"), ("vh/vw", "относительно экрана")]
    for i, (u, desc) in enumerate(units):
        by = 395 + i * 18
        p.append(T(425, by, u, HIGHLIGHT, 11, "start", "monospace", "bold"))
        p.append(T(465, by, desc, TEXT_MUTED, 10))

    # Bottom: Box model
    p.append(R(20, 470, 760, 100, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 492, "Блочная модель CSS", ACCENT, 14, "start", "sans-serif", "bold"))
    # Simplified box model diagram
    p.append(R(280, 482, 200, 70, CARD_BG2, rx=4, stroke=TEXT_MUTED, sw=1))
    p.append(T(380, 498, "margin", TEXT_MUTED, 9, "middle"))
    p.append(R(300, 492, 160, 50, "#1a3a5c", rx=3, stroke=ACCENT, sw=1))
    p.append(T(380, 508, "padding", ACCENT, 9, "middle"))
    p.append(R(320, 502, 120, 30, PRIMARY_DARK, rx=2, stroke=HIGHLIGHT, sw=1))
    p.append(T(380, 522, "content", HIGHLIGHT, 10, "middle", "sans-serif", "bold"))
    p.append(T(520, 498, "margin \u2014 внешний отступ", TEXT_MUTED, 10))
    p.append(T(520, 514, "padding \u2014 внутренний отступ", TEXT_MUTED, 10))
    p.append(T(520, 530, "border \u2014 граница", TEXT_MUTED, 10))
    p.append(T(520, 546, "content \u2014 содержимое", TEXT_MUTED, 10))

    return wrap(6, "Основы CSS", "Селекторы, свойства, цвета, шрифты", p)


# ============================================================
# LESSON 7: Создание веб-страницы
# ============================================================
def lesson_7():
    p = []
    # Left: HTML + CSS integration
    p.append(R(20, 80, 380, 280, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "Подключение CSS к HTML", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 112, 350, [
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        '  <link rel="stylesheet"',
        '    href="style.css">',
        "</head>",
        "<body>",
        '  <h1>Мой сайт</h1>',
        '  <p class="text">Привет!</p>',
        "</body>",
        "</html>",
    ], title="index.html"))
    # Inline style note
    p.append(R(35, 320, 350, 30, CARD_BG2, rx=4))
    p.append(T(45, 339, "Или: <style> в <head>", TEXT_MUTED, 10, "start", "monospace"))

    # Right: CSS file
    p.append(R(410, 80, 370, 280, CARD_BG, rx=8, stroke=ORANGE, sw=1))
    p.append(T(425, 102, "Файл style.css", ORANGE, 14, "start", "sans-serif", "bold"))
    p.append(code_block(425, 112, 340, [
        "body {",
        "  margin: 0;",
        "  font-family: Arial;",
        "  background: #f5f5f5;",
        "}",
        "",
        "h1 {",
        "  color: #0EA5E9;",
        "  text-align: center;",
        "}",
        "",
        ".text {",
        "  font-size: 18px;",
        "  padding: 20px;",
        "}",
    ], title="style.css"))

    # Middle: Layout example
    p.append(R(20, 370, 760, 100, CARD_BG, rx=8, stroke=GREEN, sw=1))
    p.append(T(35, 392, "Макет веб-страницы (Flexbox)", GREEN, 14, "start", "sans-serif", "bold"))
    # Simple layout diagram
    p.append(R(35, 405, 730, 55, CARD_BG2, rx=4))
    p.append(R(40, 410, 720, 16, PRIMARY_DARK, rx=2, stroke=ACCENT, sw=1))
    p.append(T(400, 422, "header", ACCENT, 9, "middle", "sans-serif", "bold"))
    p.append(R(40, 430, 180, 24, "#1a3a5c", rx=2, stroke=HIGHLIGHT, sw=1))
    p.append(T(130, 446, "nav", HIGHLIGHT, 9, "middle", "sans-serif", "bold"))
    p.append(R(225, 430, 350, 24, "#1a3a5c", rx=2, stroke=GREEN, sw=1))
    p.append(T(400, 446, "main", GREEN, 9, "middle", "sans-serif", "bold"))
    p.append(R(580, 430, 180, 24, "#1a3a5c", rx=2, stroke=ORANGE, sw=1))
    p.append(T(670, 446, "aside", ORANGE, 9, "middle", "sans-serif", "bold"))

    # Bottom: Key CSS for layout
    p.append(R(20, 480, 760, 90, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 502, "Ключевые свойства для布局", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 512, 350, [
        ".container {",
        "  display: flex;",
        "  gap: 20px;",
        "}",
    ], title="layout.css", lh=16))
    p.append(R(400, 517, 370, 45, CARD_BG2, rx=6))
    p.append(T(410, 535, "display: flex \u2014 гибкий контейнер", GREEN, 10, "start", "monospace"))
    p.append(T(410, 552, "gap \u2014 расстояние между элементами", ACCENT, 10, "start", "monospace"))

    return wrap(7, "Создание веб-страницы", "HTML + CSS, макет, Flexbox", p)


# ============================================================
# LESSON 8: Растровая и векторная графика
# ============================================================
def lesson_8():
    p = []
    # Left: Raster graphics
    p.append(R(20, 80, 380, 250, CARD_BG, rx=8, stroke=ORANGE, sw=1))
    p.append(T(35, 102, "Растровая графика", ORANGE, 14, "start", "sans-serif", "bold"))
    p.append(T(35, 122, "Изображение из пикселей (точек).", TEXT_LIGHT, 11))
    p.append(T(35, 138, "При увеличении видны квадратики.", TEXT_LIGHT, 11))
    # Pixel grid visualization
    grid_x, grid_y = 35, 155
    cell = 12
    colors_grid = [
        [ACCENT, ACCENT, PRIMARY, PRIMARY, GREEN, GREEN],
        [ACCENT, PRIMARY_DARK, PRIMARY, GREEN, HIGHLIGHT, HIGHLIGHT],
        [PRIMARY, PRIMARY_DARK, CARD_BG2, HIGHLIGHT, ORANGE, ORANGE],
        [PRIMARY, CARD_BG2, CARD_BG2, HIGHLIGHT, ORANGE, RED],
        [TEXT_MUTED, TEXT_MUTED, PURPLE, ORANGE, RED, RED],
    ]
    for r, row in enumerate(colors_grid):
        for c, clr in enumerate(row):
            p.append(R(grid_x + c * cell, grid_y + r * cell, cell - 1, cell - 1, clr, rx=0))
    p.append(T(grid_x + 80, grid_y + 10, "\u2190 пиксели", TEXT_MUTED, 10))
    p.append(T(35, 230, "Форматы: JPEG, PNG, BMP, GIF", TEXT_MUTED, 10))
    p.append(T(35, 248, "Программы: Photoshop, GIMP, Paint", TEXT_MUTED, 10))

    # Right: Vector graphics
    p.append(R(410, 80, 370, 250, CARD_BG, rx=8, stroke=GREEN, sw=1))
    p.append(T(425, 102, "Векторная графика", GREEN, 14, "start", "sans-serif", "bold"))
    p.append(T(425, 122, "Изображение из математических формул:", TEXT_LIGHT, 11))
    p.append(T(425, 138, "линии, кривые, фигуры.", TEXT_LIGHT, 11))
    # Vector shape demonstration
    p.append('<circle cx="500" cy="200" r="40" fill="none" stroke="{}" stroke-width="3"/>'.format(GREEN))
    p.append('<line x1="560" y1="170" x2="640" y2="230" stroke="{}" stroke-width="3"/>'.format(ACCENT))
    p.append('<rect x="660" y="170" width="50" height="60" fill="none" stroke="{}" stroke-width="3" rx="5"/>'.format(HIGHLIGHT))
    p.append(T(425, 248, "Форматы: SVG, EPS, AI", TEXT_MUTED, 10))
    p.append(T(425, 266, "Программы: Inkscape, Illustrator", TEXT_MUTED, 10))
    p.append(T(425, 284, "Масштабируется без потери качества!", GREEN, 10, "start", "sans-serif", "bold"))

    # Middle: Comparison table
    p.append(R(20, 340, 760, 120, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 362, "Сравнение растровой и векторной графики", ACCENT, 14, "start", "sans-serif", "bold"))
    # Table header
    p.append(R(35, 375, 170, 25, CARD_BG2, rx=4, stroke=PRIMARY, sw=1))
    p.append(T(120, 392, "Свойство", TEXT_WHITE, 11, "middle", "sans-serif", "bold"))
    p.append(R(210, 375, 280, 25, CARD_BG2, rx=4, stroke=ORANGE, sw=1))
    p.append(T(350, 392, "Растровая", ORANGE, 11, "middle", "sans-serif", "bold"))
    p.append(R(495, 375, 270, 25, CARD_BG2, rx=4, stroke=GREEN, sw=1))
    p.append(T(630, 392, "Векторная", GREEN, 11, "middle", "sans-serif", "bold"))
    # Table rows
    rows = [
        ("Основа", "Пиксели", "Формулы/пути"),
        ("Масштабирование", "Теряет качество", "Без потерь"),
        ("Размер файла", "Большой", "Малый"),
        ("Фотореализм", "Отлично", "Ограничено"),
    ]
    for i, (prop, raster, vector) in enumerate(rows):
        by = 405 + i * 18
        p.append(T(40, by + 12, prop, TEXT_LIGHT, 10))
        p.append(T(220, by + 12, raster, ORANGE, 10))
        p.append(T(505, by + 12, vector, GREEN, 10))

    # Bottom: SVG code example
    p.append(R(20, 470, 760, 100, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 492, "Пример SVG-кода", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 502, 350, [
        '<svg width="100" height="100">',
        '  <circle cx="50" cy="50"',
        '    r="40" fill="blue"/>',
        '</svg>',
    ], title="circle.svg", lh=16))
    p.append(R(400, 507, 370, 55, CARD_BG2, rx=6))
    p.append(T(410, 525, "SVG \u2014 текстовый формат векторной", GREEN, 11))
    p.append(T(410, 542, "графики, открывается в браузере!", GREEN, 11))

    return wrap(8, "Растровая и векторная графика", "Пиксели vs пути, форматы, SVG", p)


# ============================================================
# LESSON 9: Обработка изображений
# ============================================================
def lesson_9():
    p = []
    # Left: Filters
    p.append(R(20, 80, 380, 200, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "Фильтры обработки", ACCENT, 14, "start", "sans-serif", "bold"))
    filters = [
        ("Яркость", "Увеличение/уменьшение света", HIGHLIGHT),
        ("Контраст", "Разница между светом и тенью", ORANGE),
        ("Насыщенность", "Интенсивность цветов", GREEN),
        ("Размытие", "Сглаживание пикселей", PURPLE),
        ("Резкость", "Выделение границ", RED),
    ]
    for i, (name, desc, color) in enumerate(filters):
        by = 118 + i * 28
        p.append(R(35, by, 350, 24, CARD_BG2, rx=4))
        p.append(T(45, by + 16, name, color, 11, "start", "sans-serif", "bold"))
        p.append(T(155, by + 16, desc, TEXT_MUTED, 10))

    # Right: Formats
    p.append(R(410, 80, 370, 200, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(425, 102, "Форматы изображений", ACCENT, 14, "start", "sans-serif", "bold"))
    fmts = [
        ("JPEG", "Фотографии, сжатие с потерями", ORANGE),
        ("PNG", "Прозрачность, без потерь", GREEN),
        ("GIF", "Анимация, 256 цветов", PURPLE),
        ("BMP", "Без сжатия, большой размер", RED),
        ("SVG", "Вектор, масштабируемый", HIGHLIGHT),
        ("WebP", "Современный, малый размер", ACCENT),
    ]
    for i, (fmt, desc, color) in enumerate(fmts):
        by = 118 + i * 24
        p.append(badge(425, by, fmt, color, TEXT_WHITE, 10))
        p.append(T(500, by + 13, desc, TEXT_MUTED, 10))

    # Middle: Python image processing
    p.append(R(20, 290, 760, 170, CARD_BG, rx=8, stroke=GREEN, sw=1))
    p.append(T(35, 312, "Обработка изображений в Python (Pillow)", GREEN, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 322, 450, [
        "from PIL import Image, ImageFilter",
        "",
        "# Открытие изображения",
        'img = Image.open("photo.jpg")',
        "",
        "# Применение фильтра",
        "blur = img.filter(ImageFilter.BLUR)",
        "",
        "# Изменение размера",
        'small = img.resize((200, 200))',
        "",
        "# Сохранение",
        'small.save("photo_small.png")',
    ], title="process.py"))

    # Bottom: Before/After visualization
    p.append(R(20, 470, 760, 100, CARD_BG, rx=8, stroke=HIGHLIGHT, sw=1))
    p.append(T(35, 492, "Пример: до и после обработки", HIGHLIGHT, 14, "start", "sans-serif", "bold"))
    # "Before" image representation
    p.append(R(35, 505, 150, 50, "#1a3a5c", rx=4, stroke=TEXT_MUTED, sw=1))
    p.append(T(110, 533, "Оригинал", TEXT_MUTED, 9, "middle"))
    # Arrow
    p.append(arrow(200, 530, 250, 530, ACCENT))
    p.append(T(215, 522, "фильтр", ACCENT, 8))
    # "After" image representation
    p.append(R(260, 505, 150, 50, "#0c2d48", rx=4, stroke=GREEN, sw=1))
    p.append(T(335, 533, "Результат", GREEN, 9, "middle"))
    # Steps
    p.append(R(440, 505, 330, 50, CARD_BG2, rx=6))
    p.append(T(450, 523, "Шаги: 1) Открыть  2) Фильтр  3) Сохранить", ACCENT, 10))
    p.append(T(450, 542, "Библиотека: Pillow (PIL)", GREEN, 10, "start", "monospace"))

    return wrap(9, "Обработка изображений", "Фильтры, форматы, Pillow", p)


# ============================================================
# LESSON 10: Что такое алгоритм
# ============================================================
def lesson_10():
    p = []
    # Left: Definition
    p.append(R(20, 80, 380, 150, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "Что такое алгоритм?", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(T(35, 124, "Алгоритм \u2014 конечная последовательность", TEXT_LIGHT, 11))
    p.append(T(35, 140, "точно определённых действий, приводящая", TEXT_LIGHT, 11))
    p.append(T(35, 156, "к решению задачи.", TEXT_LIGHT, 11))
    p.append(T(35, 180, "Пример: рецепт приготовления блюда,", TEXT_MUTED, 10))
    p.append(T(35, 196, "инструкция по сборке мебели.", TEXT_MUTED, 10))

    # Right: Properties
    p.append(R(410, 80, 370, 150, CARD_BG, rx=8, stroke=HIGHLIGHT, sw=1))
    p.append(T(425, 102, "Свойства алгоритма", HIGHLIGHT, 14, "start", "sans-serif", "bold"))
    props = [
        ("Дискретность", "шаги выполняются по порядку"),
        ("Определённость", "каждый шаг чётко описан"),
        ("Результативность", "всегда есть результат"),
        ("Массовость", "работает для разных данных"),
        ("Конечность", "число шагов ограничено"),
    ]
    for i, (name, desc) in enumerate(props):
        by = 118 + i * 22
        p.append(T(425, by + 14, name, ACCENT, 11, "start", "sans-serif", "bold"))
        p.append(T(555, by + 14, desc, TEXT_MUTED, 10))

    # Middle: Flowchart example
    p.append(R(20, 240, 280, 230, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 262, "Блок-схема алгоритма", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(flow_box(85, 278, 130, 28, "Начало", PRIMARY_DARK))
    p.append(arrow(150, 306, 150, 316, ACCENT))
    p.append(flow_box(70, 316, 160, 28, "Ввести a, b", CARD_BG2))
    p.append(arrow(150, 344, 150, 354, ACCENT))
    p.append(diamond(75, 354, 150, 45, "a > b?"))
    p.append(arrow(150, 399, 150, 409, ACCENT))
    p.append(T(155, 407, "Да", GREEN, 9))
    p.append(flow_box(70, 409, 160, 28, "max = a", "#166534"))
    p.append(arrow(225, 377, 260, 377, RED))
    p.append(T(232, 370, "Нет", RED, 9))
    p.append(flow_box(260, 365, 0, 0, "", CARD_BG))  # spacer
    p.append(flow_box(195, 365, 80, 28, "max = b", "#7F1D1D"))
    p.append(arrow(235, 393, 235, 445, RED))
    p.append(flow_box(85, 445, 130, 28, "Вывести max", PRIMARY_DARK))

    # Right: Pseudocode
    p.append(R(310, 240, 470, 230, CARD_BG, rx=8, stroke=GREEN, sw=1))
    p.append(T(325, 262, "Псевдокод и запись алгоритма", GREEN, 14, "start", "sans-serif", "bold"))
    p.append(code_block(325, 272, 440, [
        "Алгоритм: Найти максимум",
        "  Ввести a, b",
        "  ЕСЛИ a > b ТО",
        "    max = a",
        "  ИНАЧЕ",
        "    max = b",
        "  Вывести max",
    ], title="pseudocode"))
    p.append(T(325, 415, "Способы записи алгоритма:", ACCENT, 12, "start", "sans-serif", "bold"))
    ways = [
        ("Словесный", "Текстовое описание шагов"),
        ("Блок-схема", "Графическое изображение"),
        ("Псевдокод", "Условный язык записи"),
        ("Программа", "Код на языке программирования"),
    ]
    for i, (way, desc) in enumerate(ways):
        by = 432 + i * 20
        p.append(T(335, by, way, HIGHLIGHT, 11, "start", "sans-serif", "bold"))
        p.append(T(435, by, desc, TEXT_MUTED, 10))

    # Bottom: Example
    p.append(R(20, 480, 760, 90, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 502, "Пример: алгоритм \u2192 программа", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 512, 350, [
        "a = int(input('a: '))",
        "b = int(input('b: '))",
        "if a > b:",
        "    max_val = a",
        "else:",
        "    max_val = b",
        "print('Максимум:', max_val)",
    ], title="max.py", lh=14))
    p.append(R(400, 517, 370, 45, CARD_BG2, rx=6))
    p.append(T(410, 535, "Псевдокод \u2192 Python: один к одному!", GREEN, 11))
    p.append(T(410, 552, "Алгоритмическое мышление = программирование", ACCENT, 10))

    return wrap(10, "Что такое алгоритм", "Свойства, псевдокод, блок-схемы", p)


# ============================================================
# LESSON 11: Исполнители алгоритмов
# ============================================================
def lesson_11():
    p = []
    # Left: What is an executor
    p.append(R(20, 80, 380, 170, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "Что такое исполнитель?", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(T(35, 124, "Исполнитель \u2014 объект, выполняющий", TEXT_LIGHT, 11))
    p.append(T(35, 140, "команды алгоритма.", TEXT_LIGHT, 11))
    p.append(T(35, 164, "СКИ \u2014 система команд исполнителя", HIGHLIGHT, 11, "start", "sans-serif", "bold"))
    p.append(T(35, 182, "(набор команд, которые он понимает).", TEXT_MUTED, 10))

    # Right: Types of executors
    p.append(R(410, 80, 370, 170, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(425, 102, "Исполнители в информатике", ACCENT, 14, "start", "sans-serif", "bold"))
    executors = [
        ("Робот", "Двигается по клеткам", GREEN),
        ("Черепашка", "Рисует на холсте", ACCENT),
        ("Калькулятор", "Вычисляет выражения", ORANGE),
        ("Компьютер", "Выполняет программы", PURPLE),
    ]
    for i, (name, desc, color) in enumerate(executors):
        by = 118 + i * 28
        p.append(R(425, by, 350, 24, CARD_BG2, rx=4))
        p.append(T(435, by + 16, name, color, 11, "start", "sans-serif", "bold"))
        p.append(T(530, by + 16, desc, TEXT_MUTED, 10))

    # Middle: Robot executor
    p.append(R(20, 260, 380, 190, CARD_BG, rx=8, stroke=GREEN, sw=1))
    p.append(T(35, 282, "Исполнитель Робот", GREEN, 14, "start", "sans-serif", "bold"))
    # Grid for robot
    grid_x, grid_y = 35, 295
    cell = 30
    for r in range(4):
        for c in range(5):
            clr = CARD_BG2
            if r == 1 and c == 3:
                clr = RED  # obstacle
            elif r == 2 and c == 1:
                clr = HIGHLIGHT  # target
            p.append(R(grid_x + c * cell, grid_y + r * cell, cell - 1, cell - 1, clr, rx=2, stroke="#334155", sw=1))
    # Robot position
    p.append(R(grid_x + 2 * cell + 3, grid_y + 0 * cell + 3, cell - 7, cell - 7, GREEN, rx=4))
    p.append(T(grid_x + 2 * cell + cell / 2, grid_y + cell / 2 + 3, "R", TEXT_WHITE, 12, "middle", "sans-serif", "bold"))
    # Commands
    p.append(T(195, 300, "СКИ Робота:", GREEN, 11, "start", "sans-serif", "bold"))
    p.append(T(195, 316, "вверх", ACCENT, 10, "start", "monospace"))
    p.append(T(195, 332, "вниз", ACCENT, 10, "start", "monospace"))
    p.append(T(195, 348, "влево", ACCENT, 10, "start", "monospace"))
    p.append(T(195, 364, "вправо", ACCENT, 10, "start", "monospace"))
    p.append(T(195, 380, "закрасить", HIGHLIGHT, 10, "start", "monospace"))

    # Right: Turtle executor
    p.append(R(410, 260, 370, 190, CARD_BG, rx=8, stroke=ACCENT, sw=1))
    p.append(T(425, 282, "Исполнитель Черепашка", ACCENT, 14, "start", "sans-serif", "bold"))
    # Turtle path visualization
    p.append(R(425, 295, 340, 80, CARD_BG2, rx=4))
    # Draw a square path
    pts = "450,350 550,350 550,310 450,310"
    p.append('<polyline points="{}" fill="none" stroke="{}" stroke-width="2"/>'.format(pts, ACCENT))
    p.append('<circle cx="450" cy="350" r="4" fill="{}"/>'.format(GREEN))
    # Turtle icon
    p.append('<circle cx="450" cy="350" r="8" fill="{}" stroke="{}" stroke-width="2"/>'.format(GREEN, TEXT_WHITE))
    p.append(T(455, 353, "T", TEXT_WHITE, 8, "middle", "sans-serif", "bold"))
    # Commands
    p.append(T(425, 395, "СКИ Черепашки:", ACCENT, 11, "start", "sans-serif", "bold"))
    p.append(code_block(425, 405, 340, [
        "forward(100)   # вперёд 100",
        "right(90)      # направо 90°",
        "penup()        # поднять перо",
        "pendown()      # опустить перо",
    ], title="turtle.py", lh=16))

    # Bottom: Python turtle code
    p.append(R(20, 460, 760, 110, CARD_BG, rx=8, stroke=GREEN, sw=1))
    p.append(T(35, 482, "Рисуем квадрат черепашкой", GREEN, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 492, 450, [
        "import turtle",
        "",
        "for i in range(4):",
        "    turtle.forward(100)",
        "    turtle.right(90)",
        "",
        "turtle.done()",
    ], title="square.py", lh=16))
    p.append(R(500, 497, 270, 65, CARD_BG2, rx=6))
    p.append(T(510, 515, "Результат: квадрат 100x100", GREEN, 11))
    p.append(T(510, 533, "Цикл for повторяет 4 раза", ACCENT, 10))
    p.append(T(510, 551, "forward + right = сторона + поворот", TEXT_MUTED, 10))

    return wrap(11, "Исполнители алгоритмов", "Робот, Черепашка, СКИ, команды", p)


# ============================================================
# MAIN: Generate all 11 SVGs and validate
# ============================================================
if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    lessons = [
        (1, lesson_1),
        (2, lesson_2),
        (3, lesson_3),
        (4, lesson_4),
        (5, lesson_5),
        (6, lesson_6),
        (7, lesson_7),
        (8, lesson_8),
        (9, lesson_9),
        (10, lesson_10),
        (11, lesson_11),
    ]

    results = []
    for num, func in lessons:
        filepath = os.path.join(OUTPUT_DIR, "lesson-{}.svg".format(num))
        try:
            svg_content = func()
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(svg_content)
            size_kb = os.path.getsize(filepath) / 1024

            # Validate with xml.etree.ElementTree
            valid = True
            err_msg = ""
            try:
                ET.fromstring(svg_content)
            except ET.ParseError as e:
                valid = False
                err_msg = str(e)

            results.append((num, filepath, valid, size_kb, err_msg))
            status = "\u2713" if valid else "\u2717"
            print("Lesson {:2d}: {} ({:.1f} KB) {}".format(num, status, size_kb, "VALID" if valid else "INVALID: " + err_msg))
        except Exception as e:
            results.append((num, filepath, False, 0, str(e)))
            print("Lesson {:2d}: \u2717 ERROR: {}".format(num, e))

    # Summary
    valid_count = sum(1 for r in results if r[2])
    total = len(results)
    print("\n" + "=" * 50)
    print("Generated {}/{} valid SVGs".format(valid_count, total))

    if valid_count < total:
        print("\nInvalid SVGs:")
        for num, path, valid, size, err in results:
            if not valid:
                print("  Lesson {}: {}".format(num, err))
