#!/usr/bin/env python3
"""Generate Grade 7 Social Studies (Обществознание) SVG files for lessons 1-9."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/social"
WIDTH = 800
HEIGHT = 600

# Amber/yellow color scheme
PRIMARY = "#D97706"
PRIMARY_DARK = "#92400E"
PRIMARY_LIGHT = "#FDE68A"
ACCENT = "#F59E0B"
BG_GRAD_TOP = "#78350F"
BG_GRAD_BOT = "#B45309"
CARD_BG = "#1C1917"
CARD_BG2 = "#292524"
TEXT_WHITE = "#FFFFFF"
TEXT_LIGHT = "#FEF3C7"
TEXT_MUTED = "#FCD34D"
HIGHLIGHT = "#FBBF24"
GREEN = "#4ADE80"
ORANGE = "#FB923C"
RED = "#F87171"
PURPLE = "#C084FC"
BLUE = "#60A5FA"
TEAL = "#2DD4BF"


def esc(text):
    """Escape text for XML."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


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
  <linearGradient id="pyramidGrad" x1="0%" y1="100%" x2="0%" y2="0%">
    <stop offset="0%" style="stop-color:{}"/>
    <stop offset="50%" style="stop-color:{}"/>
    <stop offset="100%" style="stop-color:{}"/>
  </linearGradient>
</defs>'''.format(BG_GRAD_TOP, BG_GRAD_BOT, PRIMARY, ACCENT, PRIMARY_DARK, ACCENT, HIGHLIGHT)


def bg_rect():
    return '<rect x="0" y="0" width="{}" height="{}" fill="url(#bg)"/>'.format(WIDTH, HEIGHT)


def R(x, y, w, h, fill, rx=8, stroke=None, sw=1, opacity=None):
    s = '<rect x="{}" y="{}" width="{}" height="{}" fill="{}" rx="{}"'.format(x, y, w, h, fill, rx)
    if stroke:
        s += ' stroke="{}" stroke-width="{}"'.format(stroke, sw)
    if opacity is not None:
        s += ' opacity="{}"'.format(opacity)
    s += '/>'
    return s


def T(x, y, txt, fill=TEXT_WHITE, size=14, anchor="start", family="sans-serif", weight="normal"):
    return '<text x="{}" y="{}" fill="{}" font-size="{}" text-anchor="{}" font-family="{}" font-weight="{}">{}</text>'.format(
        x, y, fill, size, anchor, family, weight, esc(txt))


def header_bar(n, title, subtitle=""):
    parts = []
    parts.append(R(0, 0, WIDTH, 70, "url(#bg)"))
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
    parts.append(T(WIDTH / 2, HEIGHT - 10, "Обществознание · 7 класс", TEXT_MUTED, 10, "middle"))
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


def flow_box(x, y, w, h, label, fill=CARD_BG, tc=TEXT_WHITE, sc=PRIMARY):
    parts = []
    parts.append(R(x, y, w, h, fill, rx=6, stroke=sc, sw=1.5))
    parts.append(T(x + w / 2, y + h / 2 + 5, label, tc, 12, "middle", "sans-serif", "bold"))
    return "\n".join(parts)


def info_box(x, y, w, h, title, lines, border_color=PRIMARY):
    parts = []
    parts.append(R(x, y, w, h, CARD_BG, rx=8, stroke=border_color, sw=1.5))
    parts.append(T(x + 12, y + 20, title, border_color, 13, "start", "sans-serif", "bold"))
    parts.append(R(x + 5, y + 26, w - 10, 1, border_color, opacity=0.3))
    for i, line in enumerate(lines):
        parts.append(T(x + 12, y + 44 + i * 18, line, TEXT_LIGHT, 11))
    return "\n".join(parts)


def badge(x, y, label, color=PRIMARY, tc=TEXT_WHITE, size=11):
    w = len(label) * 7 + 16
    parts = []
    parts.append(R(x, y, w, 20, color, rx=10))
    parts.append(T(x + w / 2, y + 14, label, tc, size, "middle", "sans-serif", "bold"))
    return "\n".join(parts)


def diamond(x, y, w, h, label, fill=CARD_BG, tc=TEXT_WHITE):
    cx, cy = x + w / 2, y + h / 2
    pts = "{},{},{},{},{},{},{},{}".format(cx, y, x + w, cy, cx, y + h, x, cy)
    parts = []
    parts.append('<polygon points="{}" fill="{}" stroke="{}" stroke-width="1.5"/>'.format(pts, fill, PRIMARY))
    parts.append(T(cx, cy + 5, label, tc, 11, "middle", "sans-serif", "bold"))
    return "\n".join(parts)


def wrap(lesson_num, title, subtitle, body_parts):
    parts = [svg_open(), defs(), bg_rect(), header_bar(lesson_num, title, subtitle)]
    parts.extend(body_parts)
    parts.append(footer_bar())
    parts.append("</svg>")
    return "\n".join(parts)


# ============================================================
# LESSON 1: Что такое человек
# ============================================================
def lesson_1():
    p = []
    # Left: Biosocial nature
    p.append(R(20, 80, 370, 260, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "Биосоциальная природа человека", ACCENT, 14, "start", "sans-serif", "bold"))

    # Biological side
    p.append(R(35, 115, 160, 95, CARD_BG2, rx=6, stroke=GREEN, sw=1))
    p.append(T(115, 135, "Биологическое", GREEN, 11, "middle", "sans-serif", "bold"))
    p.append(T(45, 155, "• Анатомия", TEXT_LIGHT, 10))
    p.append(T(45, 170, "• Физиология", TEXT_LIGHT, 10))
    p.append(T(45, 185, "• Инстинкты", TEXT_LIGHT, 10))
    p.append(T(45, 200, "• Наследственность", TEXT_LIGHT, 10))

    # Social side
    p.append(R(215, 115, 160, 95, CARD_BG2, rx=6, stroke=BLUE, sw=1))
    p.append(T(295, 135, "Социальное", BLUE, 11, "middle", "sans-serif", "bold"))
    p.append(T(225, 155, "• Сознание", TEXT_LIGHT, 10))
    p.append(T(225, 170, "• Мышление", TEXT_LIGHT, 10))
    p.append(T(225, 185, "• Речь", TEXT_LIGHT, 10))
    p.append(T(225, 200, "• Культура", TEXT_LIGHT, 10))

    # Union
    p.append(arrow(115, 212, 165, 228, ACCENT))
    p.append(arrow(295, 212, 245, 228, ACCENT))
    p.append(R(130, 228, 150, 28, PRIMARY_DARK, rx=14, stroke=ACCENT, sw=1.5))
    p.append(T(205, 246, "ЧЕЛОВЕК", TEXT_WHITE, 12, "middle", "sans-serif", "bold"))

    # Key thought
    p.append(R(35, 268, 340, 60, CARD_BG2, rx=6))
    p.append(T(45, 288, "Человек — единство биологического", TEXT_LIGHT, 11))
    p.append(T(45, 304, "и социального начал", TEXT_LIGHT, 11))
    p.append(T(45, 320, "Биосоциальная природа — ключевая идея", HIGHLIGHT, 10, "start", "sans-serif", "bold"))

    # Right: Consciousness and thinking
    p.append(R(400, 80, 380, 260, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(415, 102, "Сознание и мышление", ACCENT, 14, "start", "sans-serif", "bold"))

    # Consciousness box
    p.append(R(415, 115, 350, 55, CARD_BG2, rx=6, stroke=HIGHLIGHT, sw=1))
    p.append(T(425, 135, "Сознание", HIGHLIGHT, 12, "start", "sans-serif", "bold"))
    p.append(T(425, 155, "Способность отражать реальность и осознавать себя", TEXT_LIGHT, 10))

    # Thinking box
    p.append(R(415, 180, 350, 55, CARD_BG2, rx=6, stroke=ORANGE, sw=1))
    p.append(T(425, 200, "Мышление", ORANGE, 12, "start", "sans-serif", "bold"))
    p.append(T(425, 220, "Процесс опосредованного познания мира", TEXT_LIGHT, 10))

    # Types of thinking
    p.append(T(415, 252, "Виды мышления:", TEXT_WHITE, 11, "start", "sans-serif", "bold"))
    p.append(badge(415, 260, "Наглядно-действенное", GREEN))
    p.append(badge(415, 286, "Наглядно-образное", BLUE))
    p.append(badge(415, 312, "Словесно-логическое", PURPLE))

    # Bottom: Differences human vs animal
    p.append(R(20, 350, 760, 220, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 372, "Отличия человека от животных", ACCENT, 14, "start", "sans-serif", "bold"))

    # Table header
    p.append(R(35, 385, 350, 25, CARD_BG2, rx=4, stroke=PRIMARY, sw=1))
    p.append(T(210, 402, "Человек", TEXT_WHITE, 11, "middle", "sans-serif", "bold"))
    p.append(R(390, 385, 370, 25, CARD_BG2, rx=4, stroke=PRIMARY, sw=1))
    p.append(T(575, 402, "Животное", TEXT_WHITE, 11, "middle", "sans-serif", "bold"))

    diffs = [
        ("Сознание и самосознание", "Инстинкты и рефлексы"),
        ("Целенаправленная деятельность", "Приспособительное поведение"),
        ("Речь и язык", "Звуковые сигналы"),
        ("Создание культуры", "Использование природных объектов"),
        ("Социальная преемственность", "Генетическая передача"),
    ]
    for i, (human, animal) in enumerate(diffs):
        by = 415 + i * 22
        p.append(T(45, by + 12, "✓ " + human, GREEN, 10))
        p.append(T(400, by + 12, "• " + animal, TEXT_MUTED, 10))

    # Key concepts at bottom
    p.append(R(35, 530, 225, 30, PRIMARY_DARK, rx=6, stroke=ACCENT, sw=1))
    p.append(T(147, 549, "Антропогенез", TEXT_WHITE, 11, "middle", "sans-serif", "bold"))
    p.append(R(270, 530, 225, 30, PRIMARY_DARK, rx=6, stroke=ACCENT, sw=1))
    p.append(T(382, 549, "Социогенез", TEXT_WHITE, 11, "middle", "sans-serif", "bold"))
    p.append(R(505, 530, 255, 30, PRIMARY_DARK, rx=6, stroke=ACCENT, sw=1))
    p.append(T(632, 549, "Антропосоциогенез", TEXT_WHITE, 11, "middle", "sans-serif", "bold"))

    return wrap(1, "Что такое человек", "Биосоциальная природа, сознание, мышление", p)


# ============================================================
# LESSON 2: Потребности человека
# ============================================================
def lesson_2():
    p = []
    # Left: Maslow pyramid
    p.append(R(20, 80, 380, 490, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "Пирамида потребностей Маслоу", ACCENT, 14, "start", "sans-serif", "bold"))

    # Pyramid levels (bottom to top)
    levels = [
        ("Физиологические", "Еда, вода, сон, тепло", RED, 340, 440),
        ("Безопасность", "Защита, здоровье, порядок", ORANGE, 290, 380),
        ("Социальные", "Общение, любовь, семья", HIGHLIGHT, 230, 320),
        ("Престижные", "Уважение, статус, успех", GREEN, 170, 260),
        ("Духовные", "Самореализация, творчество", BLUE, 110, 200),
    ]

    cx = 210
    for label, desc, color, top_y, bot_y in levels:
        # Trapezoid approximation using polygon
        hw_top = (bot_y - top_y) * 0.8 + 30
        hw_bot = (440 - top_y) * 0.4 + 30
        pts = "{},{},{},{},{},{},{},{}".format(
            cx - hw_bot, bot_y,
            cx + hw_bot, bot_y,
            cx + hw_top, top_y,
            cx - hw_top, top_y
        )
        p.append('<polygon points="{}" fill="{}" stroke="{}" stroke-width="1.5" opacity="0.9"/>'.format(pts, color, PRIMARY_DARK))
        p.append(T(cx, (top_y + bot_y) / 2 + 2, label, CARD_BG, 12, "middle", "sans-serif", "bold"))
        p.append(T(cx, (top_y + bot_y) / 2 + 16, desc, CARD_BG, 9, "middle"))

    # Arrow on the right side of pyramid
    p.append(arrow(375, 460, 375, 120, HIGHLIGHT))
    p.append(T(378, 140, "Высшие", TEXT_MUTED, 9))
    p.append(T(378, 450, "Базовые", TEXT_MUTED, 9))

    # Right: Types of needs
    p.append(R(410, 80, 370, 230, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(425, 102, "Виды потребностей", ACCENT, 14, "start", "sans-serif", "bold"))

    # Material needs
    p.append(R(425, 115, 340, 55, CARD_BG2, rx=6, stroke=ORANGE, sw=1))
    p.append(T(435, 135, "Материальные", ORANGE, 12, "start", "sans-serif", "bold"))
    p.append(T(435, 153, "Еда, одежда, жильё, транспорт", TEXT_LIGHT, 10))

    # Spiritual needs
    p.append(R(425, 178, 340, 55, CARD_BG2, rx=6, stroke=PURPLE, sw=1))
    p.append(T(435, 198, "Духовные", PURPLE, 12, "start", "sans-serif", "bold"))
    p.append(T(435, 216, "Познание, искусство, творчество", TEXT_LIGHT, 10))

    # Social needs
    p.append(R(425, 241, 340, 55, CARD_BG2, rx=6, stroke=BLUE, sw=1))
    p.append(T(435, 261, "Социальные", BLUE, 12, "start", "sans-serif", "bold"))
    p.append(T(435, 279, "Общение, признание, принадлежность", TEXT_LIGHT, 10))

    # Right bottom: Key ideas
    p.append(R(410, 320, 370, 120, CARD_BG, rx=8, stroke=HIGHLIGHT, sw=1))
    p.append(T(425, 342, "Ключевые идеи", HIGHLIGHT, 13, "start", "sans-serif", "bold"))
    p.append(T(425, 362, "• Потребности — нужда в чём-либо", TEXT_LIGHT, 10))
    p.append(T(425, 378, "• Потребности безграничны", TEXT_LIGHT, 10))
    p.append(T(425, 394, "• Ресурсы ограничены", TEXT_LIGHT, 10))
    p.append(T(425, 410, "• Это порождает проблему выбора", TEXT_LIGHT, 10))
    p.append(T(425, 426, "• Потребности развиваются с обществом", TEXT_LIGHT, 10))

    # Bottom: Info box
    p.append(R(410, 450, 370, 120, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(425, 472, "Закон возвышения потребностей", ACCENT, 12, "start", "sans-serif", "bold"))
    p.append(T(425, 492, "По мере удовлетворения одних", TEXT_LIGHT, 10))
    p.append(T(425, 506, "потребностей возникают новые,", TEXT_LIGHT, 10))
    p.append(T(425, 520, "более сложные и разнообразные.", TEXT_LIGHT, 10))
    p.append(T(425, 540, "Развитие потребностей — двигатель", HIGHLIGHT, 10, "start", "sans-serif", "bold"))
    p.append(T(425, 554, "общественного прогресса", HIGHLIGHT, 10, "start", "sans-serif", "bold"))

    return wrap(2, "Потребности человека", "Пирамида Маслоу, материальные, духовные, социальные", p)


# ============================================================
# LESSON 3: Общество как система
# ============================================================
def lesson_3():
    p = []
    # Top left: Society as system
    p.append(R(20, 80, 370, 260, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "Общество как система", ACCENT, 14, "start", "sans-serif", "bold"))

    # Central circle - Society
    p.append('<circle cx="205" cy="210" r="55" fill="{}" stroke="{}" stroke-width="2"/>'.format(PRIMARY_DARK, ACCENT))
    p.append(T(205, 215, "ОБЩЕСТВО", TEXT_WHITE, 13, "middle", "sans-serif", "bold"))

    # Subsystems around the circle
    subs = [
        (95, 140, "Экономическая", ORANGE),
        (315, 140, "Политическая", RED),
        (95, 280, "Социальная", BLUE),
        (315, 280, "Духовная", PURPLE),
    ]
    for sx, sy, label, color in subs:
        p.append('<circle cx="{}" cy="{}" r="35" fill="{}" stroke="{}" stroke-width="1.5"/>'.format(sx, sy, CARD_BG2, color))
        p.append(T(sx, sy + 4, label, color, 9, "middle", "sans-serif", "bold"))
        # Arrow to center
        dx = 205 - sx
        dy = 210 - sy
        dist = (dx**2 + dy**2)**0.5
        if dist > 0:
            start_x = sx + dx / dist * 38
            start_y = sy + dy / dist * 38
            end_x = 205 - dx / dist * 58
            end_y = 210 - dy / dist * 58
            p.append(arrow(start_x, start_y, end_x, end_y, color, 1.5))

    # Top right: Social institutions
    p.append(R(400, 80, 380, 260, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(415, 102, "Социальные институты", ACCENT, 14, "start", "sans-serif", "bold"))

    institutions = [
        ("Семья", "Воспроизводство, воспитание", HIGHLIGHT),
        ("Государство", "Управление, порядок, защита", RED),
        ("Образование", "Передача знаний, социализация", GREEN),
        ("Религия", "Духовные ценности, мировоззрение", PURPLE),
        ("Производство", "Создание благ, экономика", ORANGE),
    ]
    for i, (name, desc, color) in enumerate(institutions):
        by = 118 + i * 40
        p.append(R(415, by, 350, 34, CARD_BG2, rx=4, stroke=color, sw=1))
        p.append(T(425, by + 14, name, color, 11, "start", "sans-serif", "bold"))
        p.append(T(500, by + 14, desc, TEXT_MUTED, 10))
        p.append(T(425, by + 28, "Нормы и правила поведения", TEXT_LIGHT, 8))

    # Bottom: Features of society
    p.append(R(20, 350, 760, 220, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 372, "Признаки общества как системы", ACCENT, 14, "start", "sans-serif", "bold"))

    features = [
        ("Динамичность", "Общество постоянно изменяется и развивается"),
        ("Открытость", "Взаимодействует с природой и другими обществами"),
        ("Сложность", "Множество элементов и связей между ними"),
        ("Иерархичность", "Подсистемы имеют свою структуру"),
        ("Саморегуляция", "Поддержание равновесия через институты"),
        ("Целостность", "Все элементы взаимосвязаны и взаимозависимы"),
    ]
    for i, (name, desc) in enumerate(features):
        col = i % 2
        row = i // 2
        bx = 35 + col * 375
        by = 390 + row * 45
        p.append(R(bx, by, 360, 38, CARD_BG2, rx=4))
        p.append(T(bx + 10, by + 14, name, HIGHLIGHT, 11, "start", "sans-serif", "bold"))
        p.append(T(bx + 10, by + 30, desc, TEXT_LIGHT, 9))

    return wrap(3, "Общество как система", "Подсистемы, социальные институты, признаки", p)


# ============================================================
# LESSON 4: Что такое деятельность
# ============================================================
def lesson_4():
    p = []
    # Top left: Structure of activity
    p.append(R(20, 80, 370, 250, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "Структура деятельности", ACCENT, 14, "start", "sans-serif", "bold"))

    # Activity chain: Motive -> Goal -> Action -> Result
    items = [
        (60, 140, 100, 35, "Мотив", ORANGE),
        (180, 140, 100, 35, "Цель", HIGHLIGHT),
        (60, 200, 100, 35, "Действие", GREEN),
        (180, 200, 100, 35, "Результат", BLUE),
    ]
    for x, y, w, h, label, color in items:
        p.append(R(x, y, w, h, CARD_BG2, rx=6, stroke=color, sw=1.5))
        p.append(T(x + w / 2, y + h / 2 + 5, label, color, 12, "middle", "sans-serif", "bold"))

    p.append(arrow(160, 157, 180, 157, ACCENT))
    p.append(arrow(110, 175, 110, 200, ACCENT))
    p.append(arrow(160, 217, 180, 217, ACCENT))

    # Additional elements
    p.append(R(300, 130, 75, 40, CARD_BG2, rx=6, stroke=PURPLE, sw=1))
    p.append(T(337, 155, "Средства", PURPLE, 10, "middle", "sans-serif", "bold"))
    p.append(arrow(260, 157, 300, 150, PURPLE, 1.5))

    p.append(R(300, 200, 75, 40, CARD_BG2, rx=6, stroke=TEAL, sw=1))
    p.append(T(337, 222, "Методы", TEAL, 10, "middle", "sans-serif", "bold"))
    p.append(arrow(260, 217, 300, 220, TEAL, 1.5))

    # Key definition
    p.append(R(35, 260, 340, 55, CARD_BG2, rx=6, stroke=HIGHLIGHT, sw=1))
    p.append(T(45, 280, "Деятельность — форма активного", HIGHLIGHT, 10, "start", "sans-serif", "bold"))
    p.append(T(45, 296, "отношения человека к окружающему миру", HIGHLIGHT, 10, "start", "sans-serif", "bold"))

    # Top right: Types of activity
    p.append(R(400, 80, 380, 250, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(415, 102, "Виды деятельности", ACCENT, 14, "start", "sans-serif", "bold"))

    types = [
        ("Игра", "Усвоение норм и правил, моделирование", HIGHLIGHT),
        ("Учение", "Приобретение знаний и умений", GREEN),
        ("Труд", "Создание материальных и духовных благ", ORANGE),
        ("Общение", "Обмен информацией и эмоциями", BLUE),
    ]
    for i, (name, desc, color) in enumerate(types):
        by = 118 + i * 48
        p.append(R(415, by, 350, 40, CARD_BG2, rx=6, stroke=color, sw=1))
        p.append(T(425, by + 16, name, color, 12, "start", "sans-serif", "bold"))
        p.append(T(425, by + 32, desc, TEXT_LIGHT, 10))

    # Bottom: Motives
    p.append(R(20, 340, 760, 230, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 362, "Мотивы деятельности", ACCENT, 14, "start", "sans-serif", "bold"))

    # Motive classification
    motives_social = [
        ("Социальные", "Долг, ответственность, помощь", RED),
        ("Познавательные", "Любознательность, интерес", BLUE),
    ]
    motives_personal = [
        ("Материальные", "Выгода, прибыль, комфорт", ORANGE),
        ("Духовные", "Творчество, красота, истина", PURPLE),
    ]

    # Left column
    p.append(T(35, 388, "По характеру:", TEXT_WHITE, 11, "start", "sans-serif", "bold"))
    for i, (name, desc, color) in enumerate(motives_social):
        by = 400 + i * 38
        p.append(R(35, by, 350, 32, CARD_BG2, rx=4, stroke=color, sw=1))
        p.append(T(45, by + 14, name, color, 11, "start", "sans-serif", "bold"))
        p.append(T(155, by + 14, desc, TEXT_LIGHT, 10))

    # Right column
    p.append(T(405, 388, "По содержанию:", TEXT_WHITE, 11, "start", "sans-serif", "bold"))
    for i, (name, desc, color) in enumerate(motives_personal):
        by = 400 + i * 38
        p.append(R(405, by, 350, 32, CARD_BG2, rx=4, stroke=color, sw=1))
        p.append(T(415, by + 14, name, color, 11, "start", "sans-serif", "bold"))
        p.append(T(525, by + 14, desc, TEXT_LIGHT, 10))

    # Key insight
    p.append(R(35, 490, 730, 65, CARD_BG2, rx=6, stroke=HIGHLIGHT, sw=1))
    p.append(T(45, 510, "Особенности деятельности человека:", HIGHLIGHT, 11, "start", "sans-serif", "bold"))
    p.append(T(45, 528, "• Целенаправленность   • Продуктивность   • Орудийный характер   • Общественный характер", TEXT_LIGHT, 10))

    return wrap(4, "Что такое деятельность", "Структура, мотивы, виды деятельности", p)


# ============================================================
# LESSON 5: Трудовая деятельность
# ============================================================
def lesson_5():
    p = []
    # Left: Profession concept
    p.append(R(20, 80, 370, 250, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "Профессия и призвание", ACCENT, 14, "start", "sans-serif", "bold"))

    # Venn-like diagram
    p.append('<circle cx="160" cy="210" r="65" fill="{}" stroke="{}" stroke-width="1.5" opacity="0.7"/>'.format(ORANGE, ORANGE))
    p.append('<circle cx="230" cy="210" r="65" fill="{}" stroke="{}" stroke-width="1.5" opacity="0.7"/>'.format(BLUE, BLUE))
    p.append(T(125, 205, "Хочу", TEXT_WHITE, 12, "middle", "sans-serif", "bold"))
    p.append(T(125, 220, "Интерес", TEXT_MUTED, 9, "middle"))
    p.append(T(265, 205, "Могу", TEXT_WHITE, 12, "middle", "sans-serif", "bold"))
    p.append(T(265, 220, "Способности", TEXT_MUTED, 9, "middle"))
    p.append(T(195, 205, "Надо", TEXT_WHITE, 12, "middle", "sans-serif", "bold"))
    p.append(T(195, 222, "Потребность", TEXT_MUTED, 8, "middle"))

    p.append(R(35, 280, 340, 40, CARD_BG2, rx=6, stroke=HIGHLIGHT, sw=1))
    p.append(T(205, 304, "Профессия — на пересечении", HIGHLIGHT, 11, "middle", "sans-serif", "bold"))

    # Right: Work culture
    p.append(R(400, 80, 380, 250, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(415, 102, "Культура труда", ACCENT, 14, "start", "sans-serif", "bold"))

    culture_items = [
        ("Дисциплина", "Соблюдение правил и режима", RED),
        ("Ответственность", "Добросовестное выполнение", ORANGE),
        ("Профессионализм", "Мастерство и компетентность", GREEN),
        ("Творчество", "Инициатива и новаторство", BLUE),
        ("Сотрудничество", "Командная работа, уважение", PURPLE),
    ]
    for i, (name, desc, color) in enumerate(culture_items):
        by = 120 + i * 38
        p.append(R(415, by, 350, 32, CARD_BG2, rx=4, stroke=color, sw=1))
        p.append(T(425, by + 14, name, color, 11, "start", "sans-serif", "bold"))
        p.append(T(540, by + 14, desc, TEXT_LIGHT, 10))

    # Bottom: Career types
    p.append(R(20, 340, 760, 230, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 362, "Типы профессий (по Климову)", ACCENT, 14, "start", "sans-serif", "bold"))

    prof_types = [
        ("Человек — Природа", "Агроном, ветеринар, биолог", GREEN),
        ("Человек — Техника", "Инженер, механик, программист", ORANGE),
        ("Человек — Человек", "Учитель, врач, менеджер", BLUE),
        ("Человек — Знак", "Бухгалтер, переводчик, аналитик", PURPLE),
        ("Человек — Искусство", "Художник, актёр, дизайнер", RED),
    ]
    for i, (name, desc, color) in enumerate(prof_types):
        col = i % 2
        row = i // 2
        bx = 35 + col * 375
        by = 385 + row * 50
        p.append(R(bx, by, 360, 42, CARD_BG2, rx=6, stroke=color, sw=1))
        p.append(T(bx + 12, by + 16, name, color, 11, "start", "sans-serif", "bold"))
        p.append(T(bx + 12, by + 32, desc, TEXT_LIGHT, 9))

    # Bottom note
    p.append(R(35, 540, 730, 22, CARD_BG2, rx=4))
    p.append(T(400, 555, "Правильный выбор профессии — залог успешной карьеры и удовлетворённости жизнью", TEXT_MUTED, 10, "middle"))

    return wrap(5, "Трудовая деятельность", "Профессия, карьера, культура труда", p)


# ============================================================
# LESSON 6: Общение и его виды
# ============================================================
def lesson_6():
    p = []
    # Top left: What is communication
    p.append(R(20, 80, 370, 200, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "Что такое общение?", ACCENT, 14, "start", "sans-serif", "bold"))

    # Communication model
    p.append(R(35, 118, 80, 35, CARD_BG2, rx=6, stroke=GREEN, sw=1))
    p.append(T(75, 140, "Отправитель", GREEN, 10, "middle", "sans-serif", "bold"))
    p.append(arrow(115, 135, 175, 135, HIGHLIGHT))
    p.append(R(175, 118, 100, 35, CARD_BG2, rx=6, stroke=HIGHLIGHT, sw=1))
    p.append(T(225, 140, "Сообщение", HIGHLIGHT, 10, "middle", "sans-serif", "bold"))
    p.append(arrow(275, 135, 335, 135, ACCENT))
    p.append(R(280, 118, 95, 35, CARD_BG2, rx=6, stroke=BLUE, sw=1))
    p.append(T(327, 140, "Получатель", BLUE, 10, "middle", "sans-serif", "bold"))

    # Feedback arrow
    p.append(arrow(327, 160, 75, 160, PURPLE, 1))
    p.append(T(200, 174, "Обратная связь", PURPLE, 9, "middle"))

    p.append(R(35, 188, 340, 80, CARD_BG2, rx=6))
    p.append(T(45, 206, "Общение — процесс обмена", TEXT_LIGHT, 11))
    p.append(T(45, 222, "информацией, чувствами, мыслями", TEXT_LIGHT, 11))
    p.append(T(45, 244, "между людьми.", HIGHLIGHT, 11, "start", "sans-serif", "bold"))

    # Top right: Types
    p.append(R(400, 80, 380, 200, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(415, 102, "Виды общения", ACCENT, 14, "start", "sans-serif", "bold"))

    # Verbal
    p.append(R(415, 118, 170, 65, CARD_BG2, rx=6, stroke=GREEN, sw=1))
    p.append(T(500, 140, "Вербальное", GREEN, 12, "middle", "sans-serif", "bold"))
    p.append(T(500, 158, "Речь, слова", TEXT_LIGHT, 10, "middle"))
    p.append(T(500, 172, "текст, письмо", TEXT_LIGHT, 10, "middle"))

    # Nonverbal
    p.append(R(595, 118, 170, 65, CARD_BG2, rx=6, stroke=ORANGE, sw=1))
    p.append(T(680, 140, "Невербальное", ORANGE, 12, "middle", "sans-serif", "bold"))
    p.append(T(680, 158, "Жесты, мимика", TEXT_LIGHT, 10, "middle"))
    p.append(T(680, 172, "поза, взгляд", TEXT_LIGHT, 10, "middle"))

    # Formal vs informal
    p.append(R(415, 195, 170, 55, CARD_BG2, rx=6, stroke=BLUE, sw=1))
    p.append(T(500, 215, "Формальное", BLUE, 11, "middle", "sans-serif", "bold"))
    p.append(T(500, 232, "Деловое, официальное", TEXT_LIGHT, 9, "middle"))

    p.append(R(595, 195, 170, 55, CARD_BG2, rx=6, stroke=PURPLE, sw=1))
    p.append(T(680, 215, "Неформальное", PURPLE, 11, "middle", "sans-serif", "bold"))
    p.append(T(680, 232, "Личное, дружеское", TEXT_LIGHT, 9, "middle"))

    # Bottom: Functions of communication
    p.append(R(20, 290, 760, 280, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 312, "Функции общения", ACCENT, 14, "start", "sans-serif", "bold"))

    functions = [
        ("Информационная", "Обмен знаниями и сведениями", BLUE),
        ("Коммуникативная", "Передача мыслей и чувств", GREEN),
        ("Интерактивная", "Организация взаимодействия", ORANGE),
        ("Перцептивная", "Взаимное восприятие людей", PURPLE),
        ("Эмоциональная", "Обмен чувствами и переживаниями", RED),
        ("Социальная", "Формирование отношений, социализация", HIGHLIGHT),
    ]
    for i, (name, desc, color) in enumerate(functions):
        col = i % 2
        row = i // 2
        bx = 35 + col * 375
        by = 330 + row * 50
        p.append(R(bx, by, 360, 42, CARD_BG2, rx=6, stroke=color, sw=1))
        # Function icon (small circle)
        p.append('<circle cx="{}" cy="{}" r="10" fill="{}"/>'.format(bx + 20, by + 21, color))
        p.append(T(bx + 20, by + 25, str(i + 1), CARD_BG, 10, "middle", "sans-serif", "bold"))
        p.append(T(bx + 38, by + 16, name, color, 11, "start", "sans-serif", "bold"))
        p.append(T(bx + 38, by + 32, desc, TEXT_LIGHT, 9))

    # Styles note
    p.append(R(35, 490, 730, 65, CARD_BG2, rx=6, stroke=HIGHLIGHT, sw=1))
    p.append(T(45, 510, "Стили общения:", HIGHLIGHT, 11, "start", "sans-serif", "bold"))
    p.append(badge(160, 502, "Ритуальный", RED))
    p.append(badge(260, 502, "Манипулятивный", ORANGE))
    p.append(badge(380, 502, "Гуманистический", GREEN))
    p.append(T(45, 535, "Гуманистический стиль — самый конструктивный, основан на уважении и понимании", TEXT_LIGHT, 10))

    return wrap(6, "Общение и его виды", "Вербальное и невербальное, функции общения", p)


# ============================================================
# LESSON 7: Конфликты и их решение
# ============================================================
def lesson_7():
    p = []
    # Top left: What is conflict
    p.append(R(20, 80, 370, 230, CARD_BG, rx=8, stroke=RED, sw=1))
    p.append(T(35, 102, "Что такое конфликт?", RED, 14, "start", "sans-serif", "bold"))

    # Two sides clashing
    p.append(R(35, 120, 130, 50, CARD_BG2, rx=6, stroke=ORANGE, sw=1))
    p.append(T(100, 142, "Сторона А", ORANGE, 11, "middle", "sans-serif", "bold"))
    p.append(T(100, 158, "Цели, интересы", TEXT_LIGHT, 9, "middle"))

    p.append(R(245, 120, 130, 50, CARD_BG2, rx=6, stroke=BLUE, sw=1))
    p.append(T(310, 142, "Сторона Б", BLUE, 11, "middle", "sans-serif", "bold"))
    p.append(T(310, 158, "Цели, интересы", TEXT_LIGHT, 9, "middle"))

    # Clash symbol
    p.append(T(205, 148, "⚡", RED, 20, "middle"))
    p.append(T(205, 170, "Столкновение", RED, 9, "middle", "sans-serif", "bold"))

    p.append(R(35, 185, 340, 110, CARD_BG2, rx=6))
    p.append(T(45, 205, "Конфликт — столкновение", TEXT_LIGHT, 11))
    p.append(T(45, 221, "противоположных интересов, целей,", TEXT_LIGHT, 11))
    p.append(T(45, 237, "взглядов субъектов взаимодействия.", TEXT_LIGHT, 11))
    p.append(T(45, 260, "Конфликт неизбежен в обществе!", HIGHLIGHT, 10, "start", "sans-serif", "bold"))
    p.append(T(45, 278, "Важно уметь его разрешать.", HIGHLIGHT, 10, "start", "sans-serif", "bold"))

    # Top right: Types of conflicts
    p.append(R(400, 80, 380, 230, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(415, 102, "Виды конфликтов", ACCENT, 14, "start", "sans-serif", "bold"))

    conflict_types = [
        ("Внутриличностный", "Борьба мотивов в сознании", PURPLE),
        ("Межличностный", "Между двумя людьми", ORANGE),
        ("Личность — Группа", "Человек против коллектива", RED),
        ("Межгрупповой", "Между группами людей", BLUE),
    ]
    for i, (name, desc, color) in enumerate(conflict_types):
        by = 118 + i * 44
        p.append(R(415, by, 350, 36, CARD_BG2, rx=4, stroke=color, sw=1))
        p.append(T(425, by + 14, name, color, 11, "start", "sans-serif", "bold"))
        p.append(T(425, by + 28, desc, TEXT_LIGHT, 9))

    # Bottom: Strategies
    p.append(R(20, 320, 760, 250, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 342, "Стратегии поведения в конфликте", ACCENT, 14, "start", "sans-serif", "bold"))

    # Grid: cooperativeness vs assertiveness
    strategies = [
        ("Сотрудничество", "Высокая кооперативность\nи напористость", GREEN, 130, 370),
        ("Компромисс", "Средний уровень обоих", HIGHLIGHT, 320, 420),
        ("Уступка", "Высокая кооперативность,\nнизкая напористость", BLUE, 130, 470),
        ("Избегание", "Низкий уровень обоих", TEXT_MUTED, 320, 470),
        ("Соперничество", "Высокая напористость,\nнизкая кооперативность", RED, 510, 370),
    ]

    for name, desc, color, bx, by in strategies:
        lines = desc.split("\n")
        p.append(R(bx, by, 170, 55, CARD_BG2, rx=6, stroke=color, sw=1.5))
        p.append(T(bx + 85, by + 16, name, color, 11, "middle", "sans-serif", "bold"))
        for j, line in enumerate(lines):
            p.append(T(bx + 85, by + 32 + j * 13, line, TEXT_LIGHT, 9, "middle"))

    # Axis labels
    p.append(T(400, 365, "Кооперативность →", TEXT_MUTED, 9, "middle"))
    p.append(T(35, 460, "Напористость ↑", TEXT_MUTED, 9))

    # Best strategy note
    p.append(R(35, 535, 730, 25, CARD_BG2, rx=4, stroke=GREEN, sw=1))
    p.append(T(400, 552, "Сотрудничество — самая конструктивная стратегия разрешения конфликта", GREEN, 10, "middle", "sans-serif", "bold"))

    return wrap(7, "Конфликты и их решение", "Виды, стратегии, конструктивное разрешение", p)


# ============================================================
# LESSON 8: Что такое политика
# ============================================================
def lesson_8():
    p = []
    # Top left: What is politics
    p.append(R(20, 80, 370, 220, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "Что такое политика?", ACCENT, 14, "start", "sans-serif", "bold"))

    p.append(R(35, 120, 340, 55, CARD_BG2, rx=6, stroke=HIGHLIGHT, sw=1))
    p.append(T(45, 140, "Политика — сфера деятельности,", HIGHLIGHT, 11, "start", "sans-serif", "bold"))
    p.append(T(45, 158, "связанная с отношениями между людьми", HIGHLIGHT, 11, "start", "sans-serif", "bold"))

    # Key concepts
    concepts = [
        ("Власть", "Способность навязывать волю", RED),
        ("Государство", "Организация управления обществом", BLUE),
        ("Политики", "Люди, занимающиеся политикой", ORANGE),
    ]
    for i, (name, desc, color) in enumerate(concepts):
        by = 185 + i * 34
        p.append(R(35, by, 340, 28, CARD_BG2, rx=4, stroke=color, sw=1))
        p.append(T(45, by + 18, name, color, 11, "start", "sans-serif", "bold"))
        p.append(T(120, by + 18, desc, TEXT_LIGHT, 10))

    # Top right: Political system
    p.append(R(400, 80, 380, 220, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(415, 102, "Политическая система", ACCENT, 14, "start", "sans-serif", "bold"))

    # Central node
    p.append('<circle cx="590" cy="190" r="40" fill="{}" stroke="{}" stroke-width="2"/>'.format(PRIMARY_DARK, ACCENT))
    p.append(T(590, 194, "Власть", TEXT_WHITE, 13, "middle", "sans-serif", "bold"))

    # Surrounding institutions
    insts = [
        (480, 130, "Партии", GREEN),
        (700, 130, "Государство", RED),
        (480, 250, "Выборы", ORANGE),
        (700, 250, "Право", BLUE),
    ]
    for ix, iy, label, color in insts:
        p.append('<circle cx="{}" cy="{}" r="28" fill="{}" stroke="{}" stroke-width="1.5"/>'.format(ix, iy, CARD_BG2, color))
        p.append(T(ix, iy + 4, label, color, 10, "middle", "sans-serif", "bold"))
        # Arrow to center
        dx = 590 - ix
        dy = 190 - iy
        dist = (dx**2 + dy**2)**0.5
        if dist > 0:
            sx = ix + dx / dist * 30
            sy = iy + dy / dist * 30
            ex = 590 - dx / dist * 42
            ey = 190 - dy / dist * 42
            p.append(arrow(sx, sy, ex, ey, color, 1))

    # Bottom: Functions of state
    p.append(R(20, 310, 760, 260, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 332, "Функции государства", ACCENT, 14, "start", "sans-serif", "bold"))

    # Internal functions
    p.append(T(35, 356, "Внутренние:", TEXT_WHITE, 12, "start", "sans-serif", "bold"))
    internal = [
        ("Политическая", "Управление обществом", RED),
        ("Экономическая", "Регулирование экономики", ORANGE),
        ("Социальная", "Поддержка населения", BLUE),
        ("Культурная", "Развитие образования и культуры", PURPLE),
        ("Правоохранительная", "Защита прав и свобод", GREEN),
    ]
    for i, (name, desc, color) in enumerate(internal):
        by = 368 + i * 26
        p.append(R(35, by, 350, 22, CARD_BG2, rx=4))
        p.append(T(45, by + 15, "• " + name, color, 10, "start", "sans-serif", "bold"))
        p.append(T(175, by + 15, desc, TEXT_LIGHT, 9))

    # External functions
    p.append(T(405, 356, "Внешние:", TEXT_WHITE, 12, "start", "sans-serif", "bold"))
    external = [
        ("Оборона", "Защита от внешних угроз", RED),
        ("Дипломатия", "Международные отношения", BLUE),
        ("Сотрудничество", "Экономические и культурные связи", GREEN),
    ]
    for i, (name, desc, color) in enumerate(external):
        by = 368 + i * 26
        p.append(R(405, by, 350, 22, CARD_BG2, rx=4))
        p.append(T(415, by + 15, "• " + name, color, 10, "start", "sans-serif", "bold"))
        p.append(T(540, by + 15, desc, TEXT_LIGHT, 9))

    # State attributes
    p.append(R(35, 510, 730, 50, CARD_BG2, rx=6, stroke=HIGHLIGHT, sw=1))
    p.append(T(45, 530, "Признаки государства:", HIGHLIGHT, 11, "start", "sans-serif", "bold"))
    p.append(badge(215, 522, "Территория", ORANGE))
    p.append(badge(305, 522, "Население", BLUE))
    p.append(badge(395, 522, "Власть", RED))
    p.append(badge(470, 522, "Законы", GREEN))
    p.append(badge(545, 522, "Налоги", PURPLE))
    p.append(badge(620, 522, "Суверенитет", HIGHLIGHT))

    return wrap(8, "Что такое политика", "Власть, государство, политическая система", p)


# ============================================================
# LESSON 9: Формы правления
# ============================================================
def lesson_9():
    p = []
    # Top: Forms of government tree
    p.append(R(20, 80, 760, 200, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "Формы правления", ACCENT, 16, "start", "sans-serif", "bold"))

    # Root: Forms of government
    p.append(R(310, 115, 180, 32, PRIMARY_DARK, rx=6, stroke=ACCENT, sw=2))
    p.append(T(400, 136, "Форма правления", TEXT_WHITE, 12, "middle", "sans-serif", "bold"))

    # Two branches
    p.append(arrow(370, 147, 200, 165, ACCENT))
    p.append(arrow(430, 147, 600, 165, ACCENT))

    # Monarchy
    p.append(R(120, 165, 160, 30, CARD_BG2, rx=6, stroke=RED, sw=1.5))
    p.append(T(200, 185, "Монархия", RED, 12, "middle", "sans-serif", "bold"))

    # Republic
    p.append(R(520, 165, 160, 30, CARD_BG2, rx=6, stroke=GREEN, sw=1.5))
    p.append(T(600, 185, "Республика", GREEN, 12, "middle", "sans-serif", "bold"))

    # Sub-branches: Monarchy
    p.append(arrow(170, 195, 100, 215, RED, 1))
    p.append(arrow(230, 195, 300, 215, RED, 1))

    p.append(R(40, 215, 120, 28, CARD_BG2, rx=4, stroke=ORANGE, sw=1))
    p.append(T(100, 233, "Абсолютная", ORANGE, 10, "middle", "sans-serif", "bold"))

    p.append(R(210, 215, 120, 28, CARD_BG2, rx=4, stroke=HIGHLIGHT, sw=1))
    p.append(T(270, 233, "Ограниченная", HIGHLIGHT, 10, "middle", "sans-serif", "bold"))

    # Sub-branches: Republic
    p.append(arrow(570, 195, 500, 215, GREEN, 1))
    p.append(arrow(630, 195, 700, 215, GREEN, 1))

    p.append(R(440, 215, 120, 28, CARD_BG2, rx=4, stroke=BLUE, sw=1))
    p.append(T(500, 233, "Президентская", BLUE, 10, "middle", "sans-serif", "bold"))

    p.append(R(640, 215, 120, 28, CARD_BG2, rx=4, stroke=PURPLE, sw=1))
    p.append(T(700, 233, "Парламентская", PURPLE, 10, "middle", "sans-serif", "bold"))

    # Middle left: Monarchy details
    p.append(R(20, 290, 370, 160, CARD_BG, rx=8, stroke=RED, sw=1))
    p.append(T(35, 312, "Монархия", RED, 14, "start", "sans-serif", "bold"))
    p.append(T(35, 332, "Власть передаётся по наследству", TEXT_LIGHT, 11))
    p.append(T(35, 350, "и сосредоточена в руках одного лица.", TEXT_LIGHT, 11))

    p.append(R(35, 365, 160, 35, CARD_BG2, rx=4, stroke=ORANGE, sw=1))
    p.append(T(115, 380, "Абсолютная", ORANGE, 10, "middle", "sans-serif", "bold"))
    p.append(T(115, 394, "Вся власть у монарха", TEXT_LIGHT, 8, "middle"))

    p.append(R(205, 365, 170, 35, CARD_BG2, rx=4, stroke=HIGHLIGHT, sw=1))
    p.append(T(290, 380, "Конституционная", HIGHLIGHT, 10, "middle", "sans-serif", "bold"))
    p.append(T(290, 394, "Власть ограничена законом", TEXT_LIGHT, 8, "middle"))

    p.append(T(35, 420, "Примеры: Россия (до 1917),", TEXT_MUTED, 9))
    p.append(T(35, 435, "Великобритания, Япония, Швеция", TEXT_MUTED, 9))

    # Middle right: Republic details
    p.append(R(410, 290, 370, 160, CARD_BG, rx=8, stroke=GREEN, sw=1))
    p.append(T(425, 312, "Республика", GREEN, 14, "start", "sans-serif", "bold"))
    p.append(T(425, 332, "Высшая власть избирается", TEXT_LIGHT, 11))
    p.append(T(425, 350, "народом на определённый срок.", TEXT_LIGHT, 11))

    p.append(R(425, 365, 160, 35, CARD_BG2, rx=4, stroke=BLUE, sw=1))
    p.append(T(505, 380, "Президентская", BLUE, 10, "middle", "sans-serif", "bold"))
    p.append(T(505, 394, "Президент — глава", TEXT_LIGHT, 8, "middle"))

    p.append(R(595, 365, 170, 35, CARD_BG2, rx=4, stroke=PURPLE, sw=1))
    p.append(T(680, 380, "Парламентская", PURPLE, 10, "middle", "sans-serif", "bold"))
    p.append(T(680, 394, "Правительство — глава", TEXT_LIGHT, 8, "middle"))

    p.append(T(425, 420, "Примеры: Россия, США, Франция,", TEXT_MUTED, 9))
    p.append(T(425, 435, "Германия, Италия, Индия", TEXT_MUTED, 9))

    # Bottom: Democracy
    p.append(R(20, 460, 760, 90, CARD_BG, rx=8, stroke=HIGHLIGHT, sw=1.5))
    p.append(T(35, 482, "Демократия", HIGHLIGHT, 16, "start", "sans-serif", "bold"))
    p.append(T(170, 482, "— власть народа", TEXT_WHITE, 14, "start", "sans-serif", "bold"))

    democ_features = [
        ("Народовластие", RED),
        ("Плюрализм", ORANGE),
        ("Права человека", GREEN),
        ("Выборность", BLUE),
        ("Разделение властей", PURPLE),
    ]
    for i, (feature, color) in enumerate(democ_features):
        p.append(badge(35 + i * 148, 496, feature, color))

    p.append(T(35, 536, "Демократия может существовать при любой форме республики и при конституционной монархии", TEXT_LIGHT, 10))

    return wrap(9, "Формы правления", "Монархия, республика, демократия", p)


# ============================================================
# MAIN: Generate all SVGs
# ============================================================
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    lessons = [
        (1, "Что такое человек", lesson_1),
        (2, "Потребности человека", lesson_2),
        (3, "Общество как система", lesson_3),
        (4, "Что такое деятельность", lesson_4),
        (5, "Трудовая деятельность", lesson_5),
        (6, "Общение и его виды", lesson_6),
        (7, "Конфликты и их решение", lesson_7),
        (8, "Что такое политика", lesson_8),
        (9, "Формы правления", lesson_9),
    ]

    results = []
    for num, title, gen_func in lessons:
        svg_content = gen_func()
        filepath = os.path.join(OUTPUT_DIR, "lesson-{}.svg".format(num))

        # Write file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)

        # Validate with xml.etree.ElementTree
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            valid = True
            err = None
        except ET.ParseError as e:
            valid = False
            err = str(e)

        size_kb = os.path.getsize(filepath) / 1024
        status = "OK" if valid else "FAIL"
        results.append((num, title, filepath, status, size_kb, err))
        print("Lesson {}: {} [{}] {:.1f}KB {}".format(num, title, status, size_kb, " - " + err if err else ""))

    print("\n" + "=" * 70)
    print("GRADE 7 SOCIAL STUDIES SVG GENERATION SUMMARY")
    print("=" * 70)
    ok_count = sum(1 for r in results if r[3] == "OK")
    for r in results:
        num, title, path, status, size, err = r
        print("  Lesson {} - {}: {} ({:.1f} KB)".format(num, title, status, size))
        if err:
            print("    ERROR: {}".format(err))
    print("-" * 70)
    print("Total: {}/{} SVGs valid".format(ok_count, len(results)))
    print("Output: {}".format(OUTPUT_DIR))


if __name__ == "__main__":
    main()
