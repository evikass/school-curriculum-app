#!/usr/bin/env python3
"""Generate Grade 7 Coding (Программирование) SVG files for all 8 lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/coding"
WIDTH = 800
HEIGHT = 600

# Emerald/teal color scheme
PRIMARY = "#10B981"
PRIMARY_DARK = "#065F46"
PRIMARY_LIGHT = "#A7F3D0"
ACCENT = "#14B8A6"
BG_GRAD_TOP = "#064E3B"
BG_GRAD_BOT = "#059669"
CODE_BG = "#0F172A"
CODE_BORDER = "#1E293B"
TEXT_WHITE = "#FFFFFF"
TEXT_LIGHT = "#D1FAE5"
TEXT_MUTED = "#6EE7B7"
CARD_BG = "#0F172A"
CARD_BG2 = "#1E293B"
HIGHLIGHT = "#FCD34D"
GREEN = "#4ADE80"
ORANGE = "#FB923C"
RED = "#F87171"
PURPLE = "#C084FC"
CYAN = "#22D3EE"
PINK = "#F472B6"


def esc(text):
    """Escape text for XML."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def svg_open():
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {} {}" width="{}" height="{}">'.format(
        WIDTH, HEIGHT, WIDTH, HEIGHT)


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
  <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" style="stop-color:#064E3B"/>
    <stop offset="100%" style="stop-color:#059669"/>
  </linearGradient>
  <filter id="shadow" x="-2%" y="-2%" width="104%" height="104%">
    <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.3"/>
  </filter>
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
    parts.append(R(0, 0, WIDTH, 70, "url(#headerGrad)"))
    parts.append('<circle cx="40" cy="35" r="22" fill="{}" stroke="{}" stroke-width="2"/>'.format(PRIMARY, ACCENT))
    parts.append(T(40, 42, str(n), TEXT_WHITE, 18, "middle", "sans-serif", "bold"))
    parts.append(T(72, 32, title, TEXT_WHITE, 22, "start", "sans-serif", "bold"))
    if subtitle:
        parts.append(T(72, 52, subtitle, TEXT_MUTED, 13))
    parts.append(R(0, 68, WIDTH, 2, ACCENT))
    return "\n".join(parts)


def footer_bar():
    parts = []
    parts.append(R(0, HEIGHT - 30, WIDTH, 30, "url(#headerGrad)"))
    parts.append(T(WIDTH / 2, HEIGHT - 10, "\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u00b7 7 \u043a\u043b\u0430\u0441\u0441", TEXT_MUTED, 10, "middle"))
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


def info_card(x, y, w, h, title, lines, stroke=PRIMARY, title_color=ACCENT):
    """Card with title and multiple text lines."""
    p = []
    p.append(R(x, y, w, h, CARD_BG, rx=8, stroke=stroke, sw=1))
    p.append(T(x + 15, y + 22, title, title_color, 13, "start", "sans-serif", "bold"))
    ly = y + 40
    for line in lines:
        p.append(T(x + 15, ly, line, TEXT_LIGHT, 11))
        ly += 16
    return "\n".join(p)


def icon_python(x, y, size=30):
    """Simplified Python logo icon."""
    p = []
    r = size / 2
    p.append('<circle cx="{}" cy="{}" r="{}" fill="{}" opacity="0.15"/>'.format(x, y, r + 4, PRIMARY))
    p.append('<text x="{}" y="{}" fill="{}" font-size="{}" text-anchor="middle" font-family="monospace" font-weight="bold">Py</text>'.format(
        x, y + size * 0.35, HIGHLIGHT, int(size * 0.65)))
    return "\n".join(p)


# ============================================================
# LESSON 1: Что такое программирование
# ============================================================
def lesson_1():
    p = []

    # Top left: What is an algorithm
    p.append(R(20, 80, 370, 230, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "\u0427\u0442\u043e \u0442\u0430\u043a\u043e\u0435 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c?", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(T(35, 122, "\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c \u2014 \u0447\u0451\u0442\u043a\u0430\u044f \u043f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c", TEXT_LIGHT, 11))
    p.append(T(35, 138, "\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0439 \u0434\u043b\u044f \u0440\u0435\u0448\u0435\u043d\u0438\u044f \u0437\u0430\u0434\u0430\u0447\u0438.", TEXT_LIGHT, 11))

    # Algorithm flowchart: making tea
    p.append(flow_box(130, 155, 140, 28, "\u041d\u0430\u0447\u0430\u043b\u043e", PRIMARY_DARK))
    p.append(arrow(200, 183, 200, 195, ACCENT))
    p.append(flow_box(120, 195, 160, 28, "\u0412\u0437\u044f\u0442\u044c \u0447\u0430\u0439\u043d\u0438\u043a", CARD_BG2))
    p.append(arrow(200, 223, 200, 235, ACCENT))
    p.append(flow_box(120, 235, 160, 28, "\u041d\u0430\u043b\u0438\u0442\u044c \u0432\u043e\u0434\u0443", CARD_BG2))
    p.append(arrow(200, 263, 200, 275, ACCENT))
    p.append(flow_box(120, 275, 160, 28, "\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043f\u043b\u0438\u0442\u0443", CARD_BG2))

    # Top right: What is programming
    p.append(R(400, 80, 380, 230, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(415, 102, "\u0427\u0442\u043e \u0442\u0430\u043a\u043e\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435?", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(T(415, 122, "\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u2014 \u043f\u0440\u043e\u0446\u0435\u0441\u0441 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", TEXT_LIGHT, 11))
    p.append(T(415, 138, "\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c \u0434\u043b\u044f \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u0430.", TEXT_LIGHT, 11))

    # Chain: Idea -> Algorithm -> Code -> Program
    chain_items = [
        ("\u0418\u0434\u0435\u044f", HIGHLIGHT, 415),
        ("\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c", CYAN, 515),
        ("\u041a\u043e\u0434", GREEN, 615),
        ("\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", PRIMARY, 700),
    ]
    for label, color, cx in chain_items:
        p.append(R(cx - 40, 155, 80, 35, CARD_BG2, rx=6, stroke=color, sw=1.5))
        p.append(T(cx, 177, label, color, 11, "middle", "sans-serif", "bold"))

    p.append(arrow(475, 172, 515, 172, ACCENT))
    p.append(arrow(575, 172, 615, 172, ACCENT))
    p.append(arrow(675, 172, 700, 172, ACCENT))

    # Programming languages
    p.append(T(415, 215, "\u042f\u0437\u044b\u043a\u0438 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:", TEXT_WHITE, 12, "start", "sans-serif", "bold"))
    p.append(badge(415, 228, "Python", PRIMARY))
    p.append(badge(495, 228, "JavaScript", "#EAB308"))
    p.append(badge(595, 228, "Java", ORANGE))
    p.append(badge(660, 228, "C++", PURPLE))
    p.append(badge(415, 254, "C#", GREEN))
    p.append(badge(470, 254, "Go", CYAN))
    p.append(badge(520, 254, "Swift", ORANGE))
    p.append(badge(585, 254, "Kotlin", PINK))

    p.append(T(415, 292, "\u041c\u044b \u0431\u0443\u0434\u0435\u043c \u0443\u0447\u0438\u0442\u044c Python! \U0001f40d", HIGHLIGHT, 12, "start", "sans-serif", "bold"))

    # Middle: Why Python
    p.append(R(20, 320, 380, 120, CARD_BG, rx=8, stroke=GREEN, sw=1))
    p.append(T(35, 342, "\u041f\u043e\u0447\u0435\u043c\u0443 Python?", GREEN, 14, "start", "sans-serif", "bold"))
    reasons = [
        ("\u2713 \u041f\u0440\u043e\u0441\u0442\u043e\u0439 \u0441\u0438\u043d\u0442\u0430\u043a\u0441\u0438\u0441", GREEN),
        ("\u2713 \u041f\u043e\u043d\u044f\u0442\u043d\u044b\u0439 \u0434\u043b\u044f \u043d\u0430\u0447\u0438\u043d\u0430\u044e\u0449\u0438\u0445", GREEN),
        ("\u2713 \u041e\u0433\u0440\u043e\u043c\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u0441\u0442\u0432\u043e", GREEN),
        ("\u2713 \u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0432\u0435\u0437\u0434\u0435: AI, web, games", GREEN),
    ]
    for i, (txt, color) in enumerate(reasons):
        p.append(T(40, 360 + i * 18, txt, color, 11))

    # Middle right: Translators
    p.append(R(410, 320, 370, 120, CARD_BG, rx=8, stroke=ORANGE, sw=1))
    p.append(T(425, 342, "\u0422\u0440\u0430\u043d\u0441\u043b\u044f\u0442\u043e\u0440\u044b", ORANGE, 14, "start", "sans-serif", "bold"))
    p.append(R(425, 355, 160, 55, CARD_BG2, rx=6, stroke=GREEN, sw=1))
    p.append(T(505, 375, "\u0418\u043d\u0442\u0435\u0440\u043f\u0440\u0435\u0442\u0430\u0442\u043e\u0440", GREEN, 11, "middle", "sans-serif", "bold"))
    p.append(T(505, 395, "Python, JavaScript", TEXT_MUTED, 9, "middle"))
    p.append(R(605, 355, 160, 55, CARD_BG2, rx=6, stroke=ORANGE, sw=1))
    p.append(T(685, 375, "\u041a\u043e\u043c\u043f\u0438\u043b\u044f\u0442\u043e\u0440", ORANGE, 11, "middle", "sans-serif", "bold"))
    p.append(T(685, 395, "C++, Go, Rust", TEXT_MUTED, 9, "middle"))
    p.append(T(425, 428, "\u041a\u043e\u0434 \u2192 \u0442\u0440\u0430\u043d\u0441\u043b\u044f\u0442\u043e\u0440 \u2192 \u043c\u0430\u0448\u0438\u043d\u043d\u044b\u0439 \u043a\u043e\u0434", TEXT_MUTED, 10))

    # Bottom: First Python code preview
    p.append(R(20, 450, 760, 120, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 472, "\u041f\u0435\u0440\u0432\u044b\u0439 \u0432\u0437\u0433\u043b\u044f\u0434 \u043d\u0430 Python", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 482, 460, [
        'print("\u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!")',
        '# \u042d\u0442\u043e \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439',
        'name = input("\u041a\u0430\u043a \u0442\u0435\u0431\u044f \u0437\u043e\u0432\u0443\u0442? ")',
        'print("\u041f\u0440\u0438\u0432\u0435\u0442, " + name)',
    ], title="hello.py", lh=18))
    # Output
    p.append(R(510, 487, 255, 75, CARD_BG2, rx=6))
    p.append(T(520, 505, "\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442:", TEXT_WHITE, 11, "start", "sans-serif", "bold"))
    p.append(T(520, 523, ">>> \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!", GREEN, 12, "start", "monospace"))
    p.append(T(520, 541, ">>> \u041f\u0440\u0438\u0432\u0435\u0442, \u0410\u043d\u043d\u0430!", GREEN, 12, "start", "monospace"))

    return wrap(1, "\u0427\u0442\u043e \u0442\u0430\u043a\u043e\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435",
                "\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c, \u044f\u0437\u044b\u043a\u0438, \u0437\u043d\u0430\u043a\u043e\u043c\u0441\u0442\u0432\u043e \u0441 Python", p)


# ============================================================
# LESSON 2: Первая программа
# ============================================================
def lesson_2():
    p = []

    # Top left: print() function
    p.append(R(20, 80, 380, 170, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "\u0424\u0443\u043d\u043a\u0446\u0438\u044f print()", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(T(35, 122, "print() \u2014 \u0432\u044b\u0432\u043e\u0434\u0438\u0442 \u0442\u0435\u043a\u0441\u0442 \u043d\u0430 \u044d\u043a\u0440\u0430\u043d", TEXT_LIGHT, 11))
    p.append(code_block(35, 135, 350, [
        'print("\u041f\u0440\u0438\u0432\u0435\u0442!")',
        'print(5 + 3)  # \u0432\u044b\u0432\u0435\u0434\u0435\u0442 8',
        'print(2, 4, 6)  # 2 4 6',
        'print("a", "b", sep="-")  # a-b',
    ], title="print_demo.py", lh=16, sz=11))

    # Top right: input() function
    p.append(R(410, 80, 370, 170, CARD_BG, rx=8, stroke=GREEN, sw=1))
    p.append(T(425, 102, "\u0424\u0443\u043d\u043a\u0446\u0438\u044f input()", GREEN, 14, "start", "sans-serif", "bold"))
    p.append(T(425, 122, "input() \u2014 \u0441\u0447\u0438\u0442\u044b\u0432\u0430\u0435\u0442 \u0432\u0432\u043e\u0434 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", TEXT_LIGHT, 11))
    p.append(code_block(425, 135, 340, [
        'name = input("\u0412\u0430\u0448\u0435 \u0438\u043c\u044f: ")',
        'print("\u041f\u0440\u0438\u0432\u0435\u0442, " + name)',
        '',
        '# input() \u0432\u0441\u0435\u0433\u0434\u0430 \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u0442 str',
        'age = input("\u0412\u043e\u0437\u0440\u0430\u0441\u0442: ")',
    ], title="input_demo.py", lh=16, sz=11))

    # Middle: Comments
    p.append(R(20, 260, 250, 100, CARD_BG, rx=8, stroke=HIGHLIGHT, sw=1))
    p.append(T(35, 282, "\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438", HIGHLIGHT, 14, "start", "sans-serif", "bold"))
    p.append(T(35, 302, "# \u2014 \u043e\u0434\u043d\u043e\u0441\u0442\u0440\u043e\u0447\u043d\u044b\u0439 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", TEXT_LIGHT, 11))
    p.append(T(35, 320, '"""...""" \u2014 \u043c\u043d\u043e\u0433\u043e\u0441\u0442\u0440\u043e\u0447\u043d\u044b\u0439', TEXT_LIGHT, 11))
    p.append(T(35, 338, "\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438 \u043d\u0435 \u0432\u044b\u043f\u043e\u043b\u043d\u044f\u044e\u0442\u0441\u044f!", TEXT_MUTED, 10))

    # Middle: IDE
    p.append(R(280, 260, 500, 100, CARD_BG, rx=8, stroke=CYAN, sw=1))
    p.append(T(295, 282, "\u0421\u0440\u0435\u0434\u0430 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0438 (IDE)", CYAN, 14, "start", "sans-serif", "bold"))
    p.append(T(295, 302, "IDE \u2014 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0434\u043b\u044f \u043d\u0430\u043f\u0438\u0441\u0430\u043d\u0438\u044f \u043a\u043e\u0434\u0430", TEXT_LIGHT, 11))
    p.append(badge(295, 312, "IDLE", GREEN))
    p.append(badge(345, 312, "PyCharm", PRIMARY))
    p.append(badge(425, 312, "VS Code", CYAN))
    p.append(badge(505, 312, "Thonny", ORANGE))
    p.append(T(295, 345, "IDLE \u043f\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0432\u043c\u0435\u0441\u0442\u0435 \u0441 Python", TEXT_MUTED, 10))

    # Bottom: Complete program
    p.append(R(20, 370, 760, 200, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 392, "\u041f\u043e\u043b\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430-\u0434\u0438\u0430\u043b\u043e\u0433", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 402, 460, [
        '# \u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430-\u043f\u0440\u0438\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0435',
        'print("\u041f\u0440\u0438\u0432\u0435\u0442! \u042f \u2014 Python!")',
        '',
        'name = input("\u041a\u0430\u043a \u0442\u0435\u0431\u044f \u0437\u043e\u0432\u0443\u0442? ")',
        'age = input("\u0421\u043a\u043e\u043b\u044c\u043a\u043e \u0442\u0435\u0431\u0435 \u043b\u0435\u0442? ")',
        '',
        'print("\u041f\u0440\u0438\u0432\u0435\u0442, " + name + "!")',
        'print("\u0422\u0435\u0431\u0435 " + age + " \u043b\u0435\u0442!")',
    ], title="greeting.py", lh=17))
    # Output simulation
    p.append(R(510, 407, 255, 148, CARD_BG2, rx=6, stroke=GREEN, sw=1))
    p.append(T(520, 425, "\u041a\u043e\u043d\u0441\u043e\u043b\u044c:", GREEN, 11, "start", "sans-serif", "bold"))
    p.append(T(520, 445, "\u041f\u0440\u0438\u0432\u0435\u0442! \u042f \u2014 Python!", TEXT_LIGHT, 11, "start", "monospace"))
    p.append(T(520, 462, "\u041a\u0430\u043a \u0442\u0435\u0431\u044f \u0437\u043e\u0432\u0443\u0442? \u0410\u043d\u043d\u0430", TEXT_MUTED, 10, "start", "monospace"))
    p.append(T(520, 479, "\u0421\u043a\u043e\u043b\u044c\u043a\u043e \u0442\u0435\u0431\u0435 \u043b\u0435\u0442? 13", TEXT_MUTED, 10, "start", "monospace"))
    p.append(T(520, 500, "\u041f\u0440\u0438\u0432\u0435\u0442, \u0410\u043d\u043d\u0430!", GREEN, 11, "start", "monospace"))
    p.append(T(520, 517, "\u0422\u0435\u0431\u0435 13 \u043b\u0435\u0442!", GREEN, 11, "start", "monospace"))

    return wrap(2, "\u041f\u0435\u0440\u0432\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430",
                "print(), input(), \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438, IDE", p)


# ============================================================
# LESSON 3: Переменные в Python
# ============================================================
def lesson_3():
    p = []

    # Top left: Variable concept
    p.append(R(20, 80, 380, 200, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "\u0427\u0442\u043e \u0442\u0430\u043a\u043e\u0435 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u0430\u044f?", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(T(35, 122, "\u041f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u0430\u044f \u2014 \u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u043d\u0430\u044f \u044f\u0447\u0435\u0439\u043a\u0430 \u043f\u0430\u043c\u044f\u0442\u0438,", TEXT_LIGHT, 11))
    p.append(T(35, 138, "\u0433\u0434\u0435 \u0445\u0440\u0430\u043d\u0438\u0442\u0441\u044f \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435.", TEXT_LIGHT, 11))

    # Variable box diagram
    vars_data = [
        ("name", "\u0410\u043d\u043d\u0430", HIGHLIGHT, 35),
        ("age", "13", GREEN, 135),
        ("height", "1.58", ORANGE, 215),
        ("ok", "True", PURPLE, 310),
    ]
    for vname, vval, color, bx in vars_data:
        p.append('<rect x="{}" y="155" width="85" height="45" fill="{}" rx="4" stroke="{}" stroke-width="1.5"/>'.format(bx, CARD_BG2, color))
        p.append(T(bx + 42, 170, vname, color, 11, "middle", "monospace", "bold"))
        p.append(T(bx + 42, 190, vval, TEXT_WHITE, 11, "middle", "monospace"))
    # Assignment arrow
    p.append(T(35, 225, "name = \"\u0410\u043d\u043d\u0430\"  \u2190 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044f \u043f\u0440\u0438\u0441\u0432\u0430\u0438\u0432\u0430\u043d\u0438\u044f", ACCENT, 11, "start", "monospace"))

    # Top right: Naming rules
    p.append(R(410, 80, 370, 200, CARD_BG, rx=8, stroke=HIGHLIGHT, sw=1))
    p.append(T(425, 102, "\u041f\u0440\u0430\u0432\u0438\u043b\u0430 \u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u044f", HIGHLIGHT, 14, "start", "sans-serif", "bold"))
    good = [
        "\u2713 my_name, age, x1",
        "\u2713 \u0411\u0443\u043a\u0432\u044b, \u0446\u0438\u0444\u0440\u044b, _",
        "\u2713 lowercase_with_underscore",
        "\u2713 \u041d\u0430\u0447\u0438\u043d\u0430\u0435\u0442\u0441\u044f \u0441 \u0431\u0443\u043a\u0432\u044b \u0438\u043b\u0438 _",
    ]
    bad = [
        "\u2717 1name (\u0446\u0438\u0444\u0440\u0430 \u043f\u0435\u0440\u0432\u043e\u0439)",
        "\u2717 my-name (\u0434\u0435\u0444\u0438\u0441)",
        "\u2717 class, for (\u043a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430)",
        "\u2717 my name (\u043f\u0440\u043e\u0431\u0435\u043b)",
    ]
    for i, txt in enumerate(good):
        p.append(T(425, 122 + i * 18, txt, GREEN, 11))
    for i, txt in enumerate(bad):
        p.append(T(425, 200 + i * 18, txt, RED, 11))

    # Middle: Assignment examples
    p.append(R(20, 290, 480, 160, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 312, "\u041f\u0440\u0438\u0441\u0432\u0430\u0438\u0432\u0430\u043d\u0438\u0435 \u0438 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 322, 450, [
        'x = 10          # \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0439',
        'x = 20          # \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0438\u0437\u043c\u0435\u043d\u0438\u043b\u043e\u0441\u044c',
        'y = x + 5       # y = 25',
        'x = x + 1       # x = 21',
        'a, b = 1, 2     # \u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435',
        'c = a           # c = 1',
    ], title="assign.py", lh=16, sz=11))

    # Right: type()
    p.append(R(510, 290, 270, 160, CARD_BG, rx=8, stroke=CYAN, sw=1))
    p.append(T(525, 312, "\u0424\u0443\u043d\u043a\u0446\u0438\u044f type()", CYAN, 14, "start", "sans-serif", "bold"))
    p.append(code_block(525, 322, 240, [
        'x = 42',
        'print(type(x))',
        "# <class 'int'>",
        '',
        'y = 3.14',
        'print(type(y))',
        "# <class 'float'>",
    ], title="type_check.py", lh=16, sz=11))

    # Bottom: More examples
    p.append(R(20, 460, 760, 110, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 482, "\u041e\u0431\u043c\u0435\u043d \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u0438 \u0441\u043e\u0441\u0442\u0430\u0432\u043d\u044b\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 492, 370, [
        '# \u041e\u0431\u043c\u0435\u043d \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439',
        'a = 5',
        'b = 10',
        'a, b = b, a  # a=10, b=5',
    ], title="swap.py", lh=16, sz=11))
    p.append(code_block(420, 492, 350, [
        '# \u0421\u043e\u0441\u0442\u0430\u0432\u043d\u044b\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438',
        'x = 10',
        'x += 5   # x = x + 5 = 15',
        'x -= 3   # x = x - 3 = 12',
    ], title="compound.py", lh=16, sz=11))

    return wrap(3, "\u041f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0435 \u0432 Python",
                "\u041f\u0440\u0438\u0441\u0432\u0430\u0438\u0432\u0430\u043d\u0438\u0435, \u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435, type()", p)


# ============================================================
# LESSON 4: Типы данных
# ============================================================
def lesson_4():
    p = []

    # Top: Four data types
    types_data = [
        ("int", "\u0426\u0435\u043b\u044b\u0435 \u0447\u0438\u0441\u043b\u0430", "42, -7, 0, 1000", GREEN, 20),
        ("float", "\u0412\u0435\u0449\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435", "3.14, -0.5, 2.0", ORANGE, 210),
        ("str", "\u0421\u0442\u0440\u043e\u043a\u0438", '"\u041f\u0440\u0438\u0432\u0435\u0442", "123"', HIGHLIGHT, 400),
        ("bool", "\u041b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0439", "True, False", PURPLE, 590),
    ]
    for tname, tdesc, texample, color, bx in types_data:
        p.append(R(bx, 80, 180, 105, CARD_BG, rx=8, stroke=color, sw=1.5))
        p.append(T(bx + 90, 100, tname, color, 16, "middle", "monospace", "bold"))
        p.append(T(bx + 90, 120, tdesc, TEXT_WHITE, 11, "middle", "sans-serif", "bold"))
        p.append(T(bx + 90, 140, texample, TEXT_MUTED, 10, "middle", "monospace"))
        p.append(R(bx + 10, 150, 160, 25, CARD_BG2, rx=4))
        p.append(T(bx + 90, 167, tname + "()", color, 11, "middle", "monospace"))

    # Middle: Code examples
    p.append(R(20, 195, 480, 185, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 217, "\u0420\u0430\u0431\u043e\u0442\u0430 \u0441 \u0442\u0438\u043f\u0430\u043c\u0438 \u0434\u0430\u043d\u043d\u044b\u0445", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 227, 450, [
        '# int \u2014 \u0446\u0435\u043b\u044b\u0435 \u0447\u0438\u0441\u043b\u0430',
        'age = 13',
        'count = -5',
        '',
        '# float \u2014 \u0432\u0435\u0449\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435',
        'pi = 3.14',
        'temp = -2.5',
        '',
        '# str \u2014 \u0441\u0442\u0440\u043e\u043a\u0438',
        'name = "\u0410\u043d\u043d\u0430"',
        'letter = "A"',
    ], title="data_types.py", lh=15, sz=11))

    # Right: Type checking
    p.append(R(510, 195, 270, 185, CARD_BG, rx=8, stroke=CYAN, sw=1))
    p.append(T(525, 217, "\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u0442\u0438\u043f\u043e\u0432", CYAN, 14, "start", "sans-serif", "bold"))
    p.append(code_block(525, 227, 240, [
        'x = 42',
        'print(type(x))',
        "# <class 'int'>",
        '',
        'y = "hello"',
        'print(type(y))',
        "# <class 'str'>",
        '',
        'z = True',
        'print(type(z))',
        "# <class 'bool'>",
    ], title="check.py", lh=15, sz=11))

    # Bottom: Type conversion
    p.append(R(20, 390, 760, 180, CARD_BG, rx=8, stroke=ORANGE, sw=1))
    p.append(T(35, 412, "\u041f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0438\u043f\u043e\u0432", ORANGE, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 422, 460, [
        '# \u0421\u0442\u0440\u043e\u043a\u0430 \u2192 \u0447\u0438\u0441\u043b\u043e',
        's = "42"',
        'n = int(s)      # 42',
        'f = float(s)    # 42.0',
        '',
        '# \u0427\u0438\u0441\u043b\u043e \u2192 \u0441\u0442\u0440\u043e\u043a\u0430',
        'x = 100',
        's = str(x)      # "100"',
        '',
        '# \u0427\u0438\u0441\u043b\u043e \u2192 \u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0435',
        'b = bool(0)     # False',
        'b = bool(1)     # True',
    ], title="convert.py", lh=15, sz=11))
    # Conversion diagram
    p.append(R(510, 427, 255, 130, CARD_BG2, rx=6))
    p.append(T(520, 445, "\u0426\u0435\u043f\u043e\u0447\u043a\u0430 \u043f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0439:", TEXT_WHITE, 11, "start", "sans-serif", "bold"))
    p.append(T(520, 465, 'input() \u2192 str', ACCENT, 11, "start", "monospace"))
    p.append(T(520, 483, 'int(input()) \u2192 int', GREEN, 11, "start", "monospace"))
    p.append(T(520, 501, 'float(input()) \u2192 float', ORANGE, 11, "start", "monospace"))
    p.append(T(520, 525, "\u0412\u0430\u0436\u043d\u043e! \u041d\u0435\u043b\u044c\u0437\u044f \u0441\u043a\u043b\u0430\u0434\u044b\u0432\u0430\u0442\u044c str \u0438 int:", RED, 10, "start", "sans-serif", "bold"))
    p.append(T(520, 543, '"5" + 3  # TypeError!', RED, 11, "start", "monospace"))
    p.append(T(520, 557, 'int("5") + 3  # 8 \u2713', GREEN, 11, "start", "monospace"))

    return wrap(4, "\u0422\u0438\u043f\u044b \u0434\u0430\u043d\u043d\u044b\u0445",
                "int, float, str, bool, \u043f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0438\u043f\u043e\u0432", p)


# ============================================================
# LESSON 5: Условный оператор if
# ============================================================
def lesson_5():
    p = []

    # Top left: Flowchart
    p.append(R(20, 80, 270, 280, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "\u0411\u043b\u043e\u043a-\u0441\u0445\u0435\u043c\u0430 if", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(flow_box(95, 115, 120, 26, "\u041d\u0430\u0447\u0430\u043b\u043e", PRIMARY_DARK))
    p.append(arrow(155, 141, 155, 155, ACCENT))
    p.append(diamond(80, 155, 150, 50, "\u0423\u0441\u043b\u043e\u0432\u0438\u0435?"))
    p.append(arrow(155, 205, 155, 220, GREEN))
    p.append(T(160, 217, "\u0414\u0430", GREEN, 9))
    p.append(flow_box(90, 220, 130, 26, "\u0411\u043b\u043e\u043a if", "#166534"))
    p.append(arrow(230, 180, 255, 180, RED))
    p.append(T(237, 173, "\u041d\u0435\u0442", RED, 9))
    p.append(arrow(255, 180, 255, 230, RED))
    p.append(flow_box(195, 230, 80, 26, "\u0411\u043b\u043e\u043a else", "#7F1D1D"))
    p.append(arrow(155, 246, 155, 265, ACCENT))
    p.append(arrow(235, 256, 155, 265, ACCENT))
    p.append(flow_box(95, 265, 120, 26, "\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0435\u043d\u0438\u0435", PRIMARY_DARK))

    # Top right: Comparison operators
    p.append(R(300, 80, 480, 145, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(315, 102, "\u041e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u044b \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f", ACCENT, 14, "start", "sans-serif", "bold"))
    ops = [
        ("==", "\u0440\u0430\u0432\u043d\u043e", "5 == 5 \u2192 True"),
        ("!=", "\u043d\u0435 \u0440\u0430\u0432\u043d\u043e", "5 != 3 \u2192 True"),
        (">", "\u0431\u043e\u043b\u044c\u0448\u0435", "7 > 3 \u2192 True"),
        ("<", "\u043c\u0435\u043d\u044c\u0448\u0435", "2 < 5 \u2192 True"),
        (">=", "\u0431\u043e\u043b\u044c\u0448\u0435 \u0438\u043b\u0438 \u0440\u0430\u0432\u043d\u043e", "5 >= 5 \u2192 True"),
        ("<=", "\u043c\u0435\u043d\u044c\u0448\u0435 \u0438\u043b\u0438 \u0440\u0430\u0432\u043d\u043e", "3 <= 5 \u2192 True"),
    ]
    for i, (op, desc, example) in enumerate(ops):
        col = i % 2
        row = i // 2
        bx = 315 + col * 235
        by = 112 + row * 30
        p.append(R(bx, by, 225, 25, CARD_BG2, rx=4))
        p.append(T(bx + 8, by + 17, op, HIGHLIGHT, 12, "start", "monospace"))
        p.append(T(bx + 45, by + 17, desc, TEXT_LIGHT, 10))
        p.append(T(bx + 140, by + 17, example, TEXT_MUTED, 9))

    # Middle: if/elif/else code
    p.append(R(300, 235, 480, 125, CARD_BG, rx=8, stroke=GREEN, sw=1))
    p.append(T(315, 257, "\u041a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f if / elif / else", GREEN, 14, "start", "sans-serif", "bold"))
    p.append(code_block(315, 267, 450, [
        'age = int(input("\u0412\u043e\u0437\u0440\u0430\u0441\u0442: "))',
        '',
        'if age >= 18:',
        '    print("\u0414\u043e\u0441\u0442\u0443\u043f \u0440\u0430\u0437\u0440\u0435\u0448\u0451\u043d")',
        'elif age >= 14:',
        '    print("\u0421 \u0441\u043e\u0433\u043b\u0430\u0441\u0438\u0435\u043c \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u0435\u0439")',
        'else:',
        '    print("\u0414\u043e\u0441\u0442\u0443\u043f \u0437\u0430\u043f\u0440\u0435\u0449\u0451\u043d")',
    ], title="access.py", lh=15, sz=11))

    # Bottom left: Indentation
    p.append(R(20, 370, 380, 200, CARD_BG, rx=8, stroke=HIGHLIGHT, sw=1))
    p.append(T(35, 392, "\u041e\u0442\u0441\u0442\u0443\u043f\u044b (\u0438\u043d\u0434\u0435\u043d\u0442\u0430\u0446\u0438\u044f)", HIGHLIGHT, 14, "start", "sans-serif", "bold"))
    p.append(T(35, 412, "\u0412 Python \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b!", TEXT_LIGHT, 11))
    p.append(code_block(35, 425, 350, [
        'if True:',
        '    print("\u0414\u0430")  # 4 \u043f\u0440\u043e\u0431\u0435\u043b\u0430',
        '    print("\u0414\u0430 2")',
        '',
        '# \u041e\u0448\u0438\u0431\u043a\u0430:',
        '# if True:',
        '# print("\u041d\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f\u0430")  # Error!',
    ], title="indent.py", lh=15, sz=11))

    # Bottom right: Nested if
    p.append(R(410, 370, 370, 200, CARD_BG, rx=8, stroke=PURPLE, sw=1))
    p.append(T(425, 392, "\u0412\u043b\u043e\u0436\u0435\u043d\u043d\u044b\u0435 \u0443\u0441\u043b\u043e\u0432\u0438\u044f", PURPLE, 14, "start", "sans-serif", "bold"))
    p.append(code_block(425, 402, 340, [
        'x = int(input("\u0427\u0438\u0441\u043b\u043e: "))',
        '',
        'if x > 0:',
        '    print("\u041f\u043e\u043b\u043e\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435")',
        '    if x > 100:',
        '        print("\u041e\u0447\u0435\u043d\u044c \u0431\u043e\u043b\u044c\u0448\u043e\u0435")',
        '    else:',
        '        print("\u041e\u0431\u044b\u0447\u043d\u043e\u0435")',
        'elif x == 0:',
        '    print("\u041d\u0443\u043b\u044c")',
        'else:',
        '    print("\u041e\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0435")',
    ], title="nested_if.py", lh=14, sz=10))

    return wrap(5, "\u0423\u0441\u043b\u043e\u0432\u043d\u044b\u0439 \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440 if",
                "if / elif / else, \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435, \u043e\u0442\u0441\u0442\u0443\u043f\u044b", p)


# ============================================================
# LESSON 6: Логические операторы
# ============================================================
def lesson_6():
    p = []

    # Top: Three logical operators
    p.append(R(20, 80, 245, 140, CARD_BG, rx=8, stroke=GREEN, sw=1.5))
    p.append(T(142, 102, "and", GREEN, 20, "middle", "monospace", "bold"))
    p.append(T(142, 125, "\u041b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0418", TEXT_WHITE, 11, "middle"))
    p.append(T(142, 143, "\u041e\u0431\u0430 \u0443\u0441\u043b\u043e\u0432\u0438\u044f True", TEXT_MUTED, 10, "middle"))
    p.append(T(142, 160, "True and True \u2192 True", GREEN, 10, "middle", "monospace"))
    p.append(T(142, 175, "True and False \u2192 False", RED, 10, "middle", "monospace"))

    p.append(R(275, 80, 245, 140, CARD_BG, rx=8, stroke=ORANGE, sw=1.5))
    p.append(T(397, 102, "or", ORANGE, 20, "middle", "monospace", "bold"))
    p.append(T(397, 125, "\u041b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0418\u041b\u0418", TEXT_WHITE, 11, "middle"))
    p.append(T(397, 143, "\u0425\u043e\u0442\u044f \u0431\u044b \u043e\u0434\u043d\u043e True", TEXT_MUTED, 10, "middle"))
    p.append(T(397, 160, "True or False \u2192 True", GREEN, 10, "middle", "monospace"))
    p.append(T(397, 175, "False or False \u2192 False", RED, 10, "middle", "monospace"))

    p.append(R(530, 80, 250, 140, CARD_BG, rx=8, stroke=PURPLE, sw=1.5))
    p.append(T(655, 102, "not", PURPLE, 20, "middle", "monospace", "bold"))
    p.append(T(655, 125, "\u041b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u041d\u0415", TEXT_WHITE, 11, "middle"))
    p.append(T(655, 143, "\u0418\u043d\u0432\u0435\u0440\u0442\u0438\u0440\u0443\u0435\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", TEXT_MUTED, 10, "middle"))
    p.append(T(655, 160, "not True \u2192 False", RED, 10, "middle", "monospace"))
    p.append(T(655, 175, "not False \u2192 True", GREEN, 10, "middle", "monospace"))

    # Middle: Truth tables
    p.append(R(20, 230, 380, 165, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 252, "\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0438\u0441\u0442\u0438\u043d\u043d\u043e\u0441\u0442\u0438 (and)", ACCENT, 13, "start", "sans-serif", "bold"))
    # Table header
    p.append(R(35, 265, 80, 22, CARD_BG2, rx=4, stroke=PRIMARY, sw=1))
    p.append(T(75, 281, "A", TEXT_WHITE, 11, "middle", "sans-serif", "bold"))
    p.append(R(120, 265, 80, 22, CARD_BG2, rx=4, stroke=PRIMARY, sw=1))
    p.append(T(160, 281, "B", TEXT_WHITE, 11, "middle", "sans-serif", "bold"))
    p.append(R(205, 265, 100, 22, CARD_BG2, rx=4, stroke=GREEN, sw=1))
    p.append(T(255, 281, "A and B", GREEN, 11, "middle", "monospace", "bold"))
    p.append(R(310, 265, 80, 22, CARD_BG2, rx=4, stroke=ORANGE, sw=1))
    p.append(T(350, 281, "A or B", ORANGE, 11, "middle", "monospace", "bold"))
    # Rows
    rows_and = [
        ("True", "True", "True", "True"),
        ("True", "False", "False", "True"),
        ("False", "True", "False", "True"),
        ("False", "False", "False", "False"),
    ]
    for i, (a, b, aandb, aorb) in enumerate(rows_and):
        ry = 290 + i * 20
        ac = GREEN if a == "True" else RED
        bc = GREEN if b == "True" else RED
        rc = GREEN if aandb == "True" else RED
        oc = GREEN if aorb == "True" else RED
        p.append(T(75, ry + 13, a, ac, 10, "middle", "monospace"))
        p.append(T(160, ry + 13, b, bc, 10, "middle", "monospace"))
        p.append(T(255, ry + 13, aandb, rc, 10, "middle", "monospace"))
        p.append(T(350, ry + 13, aorb, oc, 10, "middle", "monospace"))

    # Right: Priority and examples
    p.append(R(410, 230, 370, 165, CARD_BG, rx=8, stroke=HIGHLIGHT, sw=1))
    p.append(T(425, 252, "\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442 \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u043e\u0432", HIGHLIGHT, 13, "start", "sans-serif", "bold"))
    priorities = [
        ("1.", "not", "\u0441\u0430\u043c\u044b\u0439 \u0432\u044b\u0441\u043e\u043a\u0438\u0439", PURPLE),
        ("2.", "and", "\u0441\u0440\u0435\u0434\u043d\u0438\u0439", GREEN),
        ("3.", "or", "\u0441\u0430\u043c\u044b\u0439 \u043d\u0438\u0437\u043a\u0438\u0439", ORANGE),
    ]
    for i, (num, op, desc, color) in enumerate(priorities):
        by = 268 + i * 22
        p.append(T(425, by + 13, num, TEXT_MUTED, 11))
        p.append(T(450, by + 13, op, color, 12, "start", "monospace", "bold"))
        p.append(T(510, by + 13, desc, TEXT_MUTED, 10))
    p.append(T(425, 348, "\u041f\u0440\u0438\u043c\u0435\u0440:", TEXT_WHITE, 11, "start", "sans-serif", "bold"))
    p.append(T(425, 366, "True or False and False", TEXT_LIGHT, 11, "start", "monospace"))
    p.append(T(425, 382, "= True or (False and False)", TEXT_MUTED, 10, "start", "monospace"))
    p.append(T(425, 396, "= True or False = True", GREEN, 10, "start", "monospace"))

    # Bottom: Code examples
    p.append(R(20, 405, 760, 165, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 427, "\u041f\u0440\u0438\u043c\u0435\u0440\u044b \u0432 \u043a\u043e\u0434\u0435", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 437, 360, [
        '# \u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u0430',
        'age = 15',
        'if age >= 6 and age <= 17:',
        '    print("\u0428\u043a\u043e\u043b\u044c\u043d\u0438\u043a")',
        '',
        '# \u041b\u044e\u0431\u043e\u0435 \u0443\u0441\u043b\u043e\u0432\u0438\u0435',
        'day = "\u0441\u0443\u0431\u0431\u043e\u0442\u0430"',
        'if day == "\u0441\u0443\u0431\u0431\u043e\u0442\u0430" or day == "\u0432\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435":',
        '    print("\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439!")',
    ], title="logic.py", lh=15, sz=11))
    p.append(code_block(410, 437, 355, [
        '# \u041e\u0442\u0440\u0438\u0446\u0430\u043d\u0438\u0435',
        'is_rain = False',
        'if not is_rain:',
        '    print("\u0418\u0434\u0451\u043c \u0433\u0443\u043b\u044f\u0442\u044c!")',
        '',
        '# \u041a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044f',
        'x = 10',
        'if x > 0 and not x > 100:',
        '    print("\u041e\u0442 1 \u0434\u043e 100")',
    ], title="not_example.py", lh=15, sz=11))

    return wrap(6, "\u041b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u044b",
                "and, or, not, \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u0438\u0441\u0442\u0438\u043d\u043d\u043e\u0441\u0442\u0438", p)


# ============================================================
# LESSON 7: Цикл for
# ============================================================
def lesson_7():
    p = []

    # Top left: for loop syntax
    p.append(R(20, 80, 380, 155, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "\u0421\u0438\u043d\u0442\u0430\u043a\u0441\u0438\u0441 for", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 112, 350, [
        'for \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u0430\u044f in \u043f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c:',
        '    \u0442\u0435\u043b\u043e_\u0446\u0438\u043a\u043b\u0430',
        '',
        '# \u041f\u0440\u0438\u043c\u0435\u0440:',
        'for i in range(5):',
        '    print(i)  # 0 1 2 3 4',
    ], title="for_syntax.py", lh=17, sz=11))

    # Top right: range() function
    p.append(R(410, 80, 370, 155, CARD_BG, rx=8, stroke=GREEN, sw=1))
    p.append(T(425, 102, "\u0424\u0443\u043d\u043a\u0446\u0438\u044f range()", GREEN, 14, "start", "sans-serif", "bold"))
    p.append(R(425, 115, 340, 28, CARD_BG2, rx=4, stroke=PRIMARY, sw=1))
    p.append(T(595, 134, "range(stop)", PRIMARY, 12, "middle", "monospace"))
    p.append(T(595, 152, "0, 1, 2, ..., stop-1", TEXT_MUTED, 10, "middle"))
    p.append(R(425, 157, 340, 28, CARD_BG2, rx=4, stroke=ORANGE, sw=1))
    p.append(T(595, 176, "range(start, stop)", ORANGE, 12, "middle", "monospace"))
    p.append(T(595, 194, "start, start+1, ..., stop-1", TEXT_MUTED, 10, "middle"))
    p.append(R(425, 199, 340, 28, CARD_BG2, rx=4, stroke=PURPLE, sw=1))
    p.append(T(595, 218, "range(start, stop, step)", PURPLE, 12, "middle", "monospace"))
    p.append(T(595, 236, "\u0441 \u0448\u0430\u0433\u043e\u043c step", TEXT_MUTED, 10, "middle"))

    # Middle: Iteration examples
    p.append(R(20, 245, 480, 155, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 267, "\u041f\u0440\u0438\u043c\u0435\u0440\u044b \u043f\u0435\u0440\u0435\u0431\u043e\u0440\u0430", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 277, 450, [
        '# \u0427\u0438\u0441\u043b\u0430 \u043e\u0442 1 \u0434\u043e 10',
        'for i in range(1, 11):',
        '    print(i, end=" ")  # 1 2 3 ... 10',
        '',
        '# \u0421 \u0448\u0430\u0433\u043e\u043c 2',
        'for i in range(0, 10, 2):',
        '    print(i, end=" ")  # 0 2 4 6 8',
        '',
        '# \u041f\u0435\u0440\u0435\u0431\u043e\u0440 \u0441\u0442\u0440\u043e\u043a\u0438',
        'for ch in "Python":',
        '    print(ch)  # P y t h o n',
    ], title="iteration.py", lh=14, sz=10))

    # Right: break/continue
    p.append(R(510, 245, 270, 155, CARD_BG, rx=8, stroke=RED, sw=1))
    p.append(T(525, 267, "break \u0438 continue", RED, 14, "start", "sans-serif", "bold"))
    p.append(code_block(525, 277, 240, [
        '# break \u2014 \u0432\u044b\u0445\u043e\u0434',
        'for i in range(10):',
        '    if i == 5:',
        '        break  # \u0441\u0442\u043e\u043f',
        '    print(i)  # 0..4',
        '',
        '# continue \u2014 \u043f\u0440\u043e\u043f\u0443\u0441\u043a',
        'for i in range(5):',
        '    if i == 2:',
        '        continue',
        '    print(i)  # 0,1,3,4',
    ], title="control.py", lh=14, sz=10))

    # Bottom: Practical examples
    p.append(R(20, 410, 760, 160, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 432, "\u041f\u0440\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043f\u0440\u0438\u043c\u0435\u0440\u044b", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 442, 360, [
        '# \u0421\u0443\u043c\u043c\u0430 \u0447\u0438\u0441\u0435\u043b \u043e\u0442 1 \u0434\u043e N',
        'n = int(input("N: "))',
        'total = 0',
        'for i in range(1, n + 1):',
        '    total += i',
        'print("\u0421\u0443\u043c\u043c\u0430 =", total)',
    ], title="sum.py", lh=15, sz=11))
    p.append(code_block(410, 442, 355, [
        '# \u0420\u0438\u0441\u0443\u0435\u043c \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a',
        'n = int(input("\u0420\u0430\u0437\u043c\u0435\u0440: "))',
        'for i in range(1, n + 1):',
        '    print("*" * i)',
        '',
        '# \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0434\u043b\u044f n=4:',
        '# *',
        '# **',
        '# ***',
        '# ****',
    ], title="triangle.py", lh=14, sz=10))

    return wrap(7, "\u0426\u0438\u043a\u043b for",
                "range(), \u043f\u0435\u0440\u0435\u0431\u043e\u0440, break, continue", p)


# ============================================================
# LESSON 8: Цикл while
# ============================================================
def lesson_8():
    p = []

    # Top left: while syntax
    p.append(R(20, 80, 380, 135, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 102, "\u0421\u0438\u043d\u0442\u0430\u043a\u0441\u0438\u0441 while", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 112, 350, [
        'while \u0443\u0441\u043b\u043e\u0432\u0438\u0435:',
        '    \u0442\u0435\u043b\u043e_\u0446\u0438\u043a\u043b\u0430',
        '',
        '# \u041f\u0440\u0438\u043c\u0435\u0440:',
        'count = 0',
        'while count < 5:',
        '    print(count)',
        '    count += 1',
    ], title="while_syntax.py", lh=16, sz=11))

    # Top right: while flowchart
    p.append(R(410, 80, 370, 135, CARD_BG, rx=8, stroke=ORANGE, sw=1))
    p.append(T(425, 102, "\u0411\u043b\u043e\u043a-\u0441\u0441\u0445\u0435\u043c\u0430 while", ORANGE, 14, "start", "sans-serif", "bold"))
    p.append(flow_box(530, 112, 100, 24, "\u041d\u0430\u0447\u0430\u043b\u043e", PRIMARY_DARK))
    p.append(arrow(580, 136, 580, 148, ACCENT))
    p.append(diamond(515, 148, 130, 42, "\u0423\u0441\u043b\u043e\u0432\u0438\u0435?"))
    p.append(T(583, 168, "\u0414\u0430", GREEN, 9))
    p.append(arrow(580, 190, 580, 200, GREEN))
    p.append(flow_box(520, 200, 120, 22, "\u0422\u0435\u043b\u043e \u0446\u0438\u043a\u043b\u0430", CARD_BG2))
    # Loop back arrow
    p.append(arrow(520, 211, 480, 211, ACCENT))
    p.append(arrow(480, 211, 480, 169, ACCENT))
    p.append(arrow(480, 169, 515, 169, ACCENT))
    p.append(T(645, 168, "\u041d\u0435\u0442", RED, 9))
    p.append(arrow(645, 169, 680, 169, RED))
    p.append(flow_box(660, 185, 90, 22, "\u041a\u043e\u043d\u0435\u0446", PRIMARY_DARK))

    # Middle: Conditions and infinite loops
    p.append(R(20, 225, 380, 175, CARD_BG, rx=8, stroke=RED, sw=1))
    p.append(T(35, 247, "\u0411\u0435\u0441\u043a\u043e\u043d\u0435\u0447\u043d\u044b\u0439 \u0446\u0438\u043a\u043b", RED, 14, "start", "sans-serif", "bold"))
    p.append(T(35, 267, "\u0415\u0441\u043b\u0438 \u0443\u0441\u043b\u043e\u0432\u0438\u0435 \u0432\u0441\u0435\u0433\u0434\u0430 True,", TEXT_LIGHT, 11))
    p.append(T(35, 283, "\u0446\u0438\u043a\u043b \u043d\u0435 \u0437\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u0441\u044f!", TEXT_LIGHT, 11))
    p.append(code_block(35, 295, 350, [
        '# \u0411\u0435\u0441\u043a\u043e\u043d\u0435\u0447\u043d\u044b\u0439 \u0446\u0438\u043a\u043b!',
        'while True:',
        '    print("\u0411\u0435\u0441\u043a\u043e\u043d\u0435\u0447\u043d\u043e...")',
        '',
        '# \u0421\u0442\u043e\u043f \u0447\u0435\u0440\u0435\u0437 break',
        'while True:',
        '    cmd = input(">> ")',
        '    if cmd == "exit":',
        '        break',
    ], title="infinite.py", lh=14, sz=10))

    # Right: Practical while examples
    p.append(R(410, 225, 370, 175, CARD_BG, rx=8, stroke=GREEN, sw=1))
    p.append(T(425, 247, "\u041f\u0440\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043f\u0440\u0438\u043c\u0435\u0440\u044b", GREEN, 14, "start", "sans-serif", "bold"))
    p.append(code_block(425, 257, 340, [
        '# \u0412\u0432\u043e\u0434 \u0434\u043e \u0441\u0442\u043e\u043f-\u0441\u043b\u043e\u0432\u0430',
        'word = ""',
        'while word != "\u0441\u0442\u043e\u043f":',
        '    word = input("\u0421\u043b\u043e\u0432\u043e: ")',
        'print("\u041a\u043e\u043d\u0435\u0446!")',
        '',
        '# \u041f\u043e\u0434\u0441\u0447\u0451\u0442 \u0441\u0443\u043c\u043c\u044b',
        'total = 0',
        'num = 1',
        'while num != 0:',
        '    num = int(input("\u0427\u0438\u0441\u043b\u043e: "))',
        '    total += num',
    ], title="practical.py", lh=14, sz=10))

    # Bottom: Pattern drawing
    p.append(R(20, 410, 760, 160, CARD_BG, rx=8, stroke=PRIMARY, sw=1))
    p.append(T(35, 432, "\u0420\u0438\u0441\u0443\u0435\u043c \u0443\u0437\u043e\u0440\u044b \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e while", ACCENT, 14, "start", "sans-serif", "bold"))
    p.append(code_block(35, 442, 360, [
        '# \u0423\u0437\u043e\u0440 \u2014 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a',
        'n = int(input("\u0412\u044b\u0441\u043e\u0442\u0430: "))',
        'i = 1',
        'while i <= n:',
        '    spaces = " " * (n - i)',
        '    stars = "*" * (2 * i - 1)',
        '    print(spaces + stars)',
        '    i += 1',
    ], title="pattern.py", lh=15, sz=11))
    # Output preview
    p.append(R(410, 447, 355, 110, CARD_BG2, rx=6, stroke=GREEN, sw=1))
    p.append(T(420, 465, "\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 (n=5):", GREEN, 11, "start", "sans-serif", "bold"))
    p.append(T(500, 482, "*", TEXT_LIGHT, 12, "middle", "monospace"))
    p.append(T(500, 496, "***", TEXT_LIGHT, 12, "middle", "monospace"))
    p.append(T(500, 510, "*****", TEXT_LIGHT, 12, "middle", "monospace"))
    p.append(T(500, 524, "*******", TEXT_LIGHT, 12, "middle", "monospace"))
    p.append(T(500, 538, "*********", TEXT_LIGHT, 12, "middle", "monospace"))

    return wrap(8, "\u0426\u0438\u043a\u043b while",
                "\u0423\u0441\u043b\u043e\u0432\u0438\u044f, \u0431\u0435\u0441\u043a\u043e\u043d\u0435\u0447\u043d\u044b\u0435 \u0446\u0438\u043a\u043b\u044b, \u0443\u0437\u043e\u0440\u044b", p)


# ============================================================
# MAIN: Generate all SVGs and validate
# ============================================================
def main():
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
    ]

    results = []
    for num, func in lessons:
        filepath = os.path.join(OUTPUT_DIR, "lesson-{}.svg".format(num))
        svg_content = func()

        # Validate XML
        try:
            root = ET.fromstring(svg_content)
            valid = True
            error_msg = ""
        except ET.ParseError as e:
            valid = False
            error_msg = str(e)

        if valid:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(svg_content)
            size_kb = os.path.getsize(filepath) / 1024
            results.append("  Lesson {} -> OK ({} KB)".format(num, round(size_kb, 1)))
        else:
            results.append("  Lesson {} -> XML ERROR: {}".format(num, error_msg))

    print("=" * 60)
    print("Grade 7 Coding SVG Generation Results")
    print("=" * 60)
    print("Output: {}".format(OUTPUT_DIR))
    for r in results:
        print(r)

    # Summary
    ok_count = sum(1 for r in results if "OK" in r)
    print("\n{}/{} SVGs generated successfully".format(ok_count, len(lessons)))

    # Additional validation: re-read and parse all files
    print("\nRe-validating all generated files...")
    for num in range(1, 9):
        filepath = os.path.join(OUTPUT_DIR, "lesson-{}.svg".format(num))
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            w = root.get("width")
            h = root.get("height")
            print("  lesson-{}.svg: {}x{} - Valid XML".format(num, w, h))
        except Exception as e:
            print("  lesson-{}.svg: INVALID - {}".format(num, e))


if __name__ == "__main__":
    main()
