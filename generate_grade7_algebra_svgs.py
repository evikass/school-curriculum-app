#!/usr/bin/env python3
"""Generate Grade 7 Algebra SVG files for educational app."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/algebra"

# Color scheme
PRIMARY = "#4F46E5"
PRIMARY_LIGHT = "#818CF8"
PRIMARY_LIGHTER = "#C7D2FE"
PRIMARY_DARK = "#3730A3"
PRIMARY_DARKER = "#1E1B4B"
ACCENT = "#6366F1"
ACCENT2 = "#A78BFA"
BG = "#F8FAFC"
BG2 = "#EEF2FF"
WHITE = "#FFFFFF"
TEXT_DARK = "#1E293B"
TEXT_MED = "#475569"
TEXT_LIGHT = "#94A3B8"
SUCCESS = "#10B981"
WARNING = "#F59E0B"
DANGER = "#EF4444"
INFO = "#3B82F6"

W, H = 800, 600


def svg_header():
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'''


def svg_footer():
    return "</svg>"


def draw_background():
    return f'''
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{PRIMARY_DARKER};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{PRIMARY_DARK};stop-opacity:1"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:{WHITE};stop-opacity:0.95"/>
      <stop offset="100%" style="stop-color:{BG2};stop-opacity:0.9"/>
    </linearGradient>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:{PRIMARY};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{ACCENT2};stop-opacity:1"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:{ACCENT};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{PRIMARY_LIGHT};stop-opacity:1"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="{PRIMARY_DARKER}" flood-opacity="0.3"/>
    </filter>
    <filter id="shadowSm" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="{PRIMARY_DARKER}" flood-opacity="0.2"/>
    </filter>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bgGrad)"/>
  <!-- Decorative circles -->
  <circle cx="750" cy="50" r="80" fill="{PRIMARY}" opacity="0.15"/>
  <circle cx="50" cy="560" r="60" fill="{ACCENT2}" opacity="0.1"/>
  <circle cx="700" cy="550" r="40" fill="{PRIMARY_LIGHT}" opacity="0.1"/>
  <!-- Subtle grid pattern -->
  <line x1="0" y1="0" x2="800" y2="600" stroke="{PRIMARY}" stroke-width="0.3" opacity="0.05"/>
  <line x1="800" y1="0" x2="0" y2="600" stroke="{PRIMARY}" stroke-width="0.3" opacity="0.05"/>
'''


def draw_header(lesson_num, title, subtitle=""):
    subtitle_svg = ""
    if subtitle:
        subtitle_svg = f'''
    <text x="400" y="82" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="{PRIMARY_LIGHTER}" opacity="0.9">{subtitle}</text>'''
    return f'''
  <!-- Header bar -->
  <rect x="30" y="15" width="740" height="70" rx="12" fill="url(#headerGrad)" filter="url(#shadow)"/>
  <text x="60" y="48" font-family="Arial, sans-serif" font-size="16" fill="{WHITE}" opacity="0.8">Урок {lesson_num}</text>
  <text x="400" y="55" text-anchor="middle" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="{WHITE}">{title}</text>{subtitle_svg}
'''


def card(x, y, w, h, rx=10):
    return f'''  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="url(#cardGrad)" filter="url(#shadow)"/>\n'''


def card_colored(x, y, w, h, color=PRIMARY, rx=10):
    return f'''  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{color}" filter="url(#shadowSm)"/>\n'''


def text_el(x, y, content, size=16, color=TEXT_DARK, anchor="start", bold=False, italic=False):
    weight = ' font-weight="bold"' if bold else ""
    style = ' font-style="italic"' if italic else ""
    # Escape XML special characters
    content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
    return f'''  <text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Arial, sans-serif" font-size="{size}" fill="{color}"{weight}{style}>{content}</text>\n'''


def formula_box(x, y, w, h, formula_text, label="", color=PRIMARY):
    svg = card_colored(x, y, w, h, color, 8)
    if label:
        svg += text_el(x + w/2, y + 20, label, 11, WHITE, "middle", True)
        svg += text_el(x + w/2, y + h/2 + 10, formula_text, 20, WHITE, "middle", True)
    else:
        svg += text_el(x + w/2, y + h/2 + 7, formula_text, 22, WHITE, "middle", True)
    return svg


def section_label(x, y, text, color=PRIMARY):
    return f'''  <rect x="{x}" y="{y-14}" width="8" height="16" rx="2" fill="{color}"/>
  <text x="{x+14}" y="{y}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{color}">{text}</text>
'''


def arrow_line(x1, y1, x2, y2, color=PRIMARY_LIGHT):
    return f'''  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2" marker-end="url(#arrowhead)"/>
'''


def number_line(x, y, width, points, labels, highlight=None, color=PRIMARY):
    """Draw a number line with points."""
    svg = f'''  <line x1="{x}" y1="{y}" x2="{x+width}" y2="{y}" stroke="{TEXT_MED}" stroke-width="2"/>
  <!-- Arrowhead -->
  <polygon points="{x+width},{y} {x+width-8},{y-4} {x+width-8},{y+4}" fill="{TEXT_MED}"/>
  <polygon points="{x},{y} {x+8},{y-4} {x+8},{y+4}" fill="{TEXT_MED}"/>
'''
    step = width / (len(labels) - 1) if len(labels) > 1 else width
    for i, (pt, lbl) in enumerate(zip(points, labels)):
        px = x + i * step
        fill_color = color if (highlight is not None and i in highlight) else TEXT_DARK
        r = 5 if (highlight is not None and i in highlight) else 3
        svg += f'''  <circle cx="{px}" cy="{y}" r="{r}" fill="{fill_color}"/>
  <text x="{px}" y="{y+20}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{TEXT_MED}">{lbl}</text>
'''
    return svg


def coordinate_grid(ox, oy, w, h, x_range, y_range, points=None, line_func=None):
    """Draw a coordinate grid with optional points and function line."""
    svg = ""
    # Background
    svg += f'  <rect x="{ox}" y="{oy}" width="{w}" height="{h}" rx="4" fill="{WHITE}" stroke="{PRIMARY_LIGHTER}" stroke-width="1"/>\n'
    
    # Grid lines
    x_step = w / (x_range[1] - x_range[0])
    y_step = h / (y_range[1] - y_range[0])
    origin_x = ox + (0 - x_range[0]) * x_step
    origin_y = oy + (y_range[1] - 0) * y_step
    
    for xi in range(x_range[0], x_range[1] + 1):
        lx = ox + (xi - x_range[0]) * x_step
        svg += f'  <line x1="{lx}" y1="{oy}" x2="{lx}" y2="{oy+h}" stroke="{PRIMARY_LIGHTER}" stroke-width="0.5" opacity="0.5"/>\n'
    
    for yi in range(y_range[0], y_range[1] + 1):
        ly = oy + (y_range[1] - yi) * y_step
        svg += f'  <line x1="{ox}" y1="{ly}" x2="{ox+w}" y2="{ly}" stroke="{PRIMARY_LIGHTER}" stroke-width="0.5" opacity="0.5"/>\n'
    
    # Axes
    svg += f'  <line x1="{ox}" y1="{origin_y}" x2="{ox+w}" y2="{origin_y}" stroke="{TEXT_DARK}" stroke-width="2"/>\n'
    svg += f'  <line x1="{origin_x}" y1="{oy}" x2="{origin_x}" y2="{oy+h}" stroke="{TEXT_DARK}" stroke-width="2"/>\n'
    
    # Axis labels
    for xi in range(x_range[0], x_range[1] + 1):
        if xi == 0:
            continue
        lx = ox + (xi - x_range[0]) * x_step
        svg += text_el(lx, origin_y + 16, str(xi), 10, TEXT_MED, "middle")
    
    for yi in range(y_range[0], y_range[1] + 1):
        if yi == 0:
            continue
        ly = oy + (y_range[1] - yi) * y_step
        svg += text_el(origin_x - 14, ly + 4, str(yi), 10, TEXT_MED, "middle")
    
    svg += text_el(ox + w - 10, origin_y - 8, "x", 12, TEXT_DARK, "middle", True)
    svg += text_el(origin_x + 12, oy + 12, "y", 12, TEXT_DARK, "middle", True)
    svg += text_el(origin_x - 10, origin_y + 14, "0", 10, TEXT_MED, "middle")
    
    # Draw function line if provided
    if line_func is not None:
        pts = []
        for px_i in range(w * 2):
            x_val = x_range[0] + (px_i / (w * 2)) * (x_range[1] - x_range[0])
            y_val = line_func(x_val)
            if y_range[0] <= y_val <= y_range[1]:
                sx = ox + (x_val - x_range[0]) * x_step
                sy = oy + (y_range[1] - y_val) * y_step
                pts.append(f"{sx:.1f},{sy:.1f}")
        if len(pts) > 1:
            svg += f'  <polyline points="{" ".join(pts)}" fill="none" stroke="{PRIMARY}" stroke-width="2.5" stroke-linecap="round"/>\n'
    
    # Draw points if provided
    if points:
        for (px, py, label) in points:
            sx = ox + (px - x_range[0]) * x_step
            sy = oy + (y_range[1] - py) * y_step
            svg += f'  <circle cx="{sx:.1f}" cy="{sy:.1f}" r="4" fill="{DANGER}"/>\n'
            if label:
                svg += text_el(sx + 8, sy - 6, label, 11, DANGER, "start", True)
    
    return svg


# =====================================================================
# LESSON 1: Числовые выражения
# =====================================================================
def lesson1():
    svg = svg_header()
    svg += draw_background()
    svg += draw_header(1, "Числовые выражения", "Порядок действий и вычисление")
    
    # Main card
    svg += card(30, 95, 740, 490)
    
    # Section 1: What is a numerical expression
    svg += section_label(50, 130, "Числовое выражение", PRIMARY)
    svg += text_el(50, 150, "Запись, состоящая из чисел, знаков действий и скобок", 14, TEXT_MED)
    
    # Example expressions
    svg += formula_box(50, 165, 220, 50, "5 + 3 × 2", "Пример:")
    svg += formula_box(285, 165, 220, 50, "(12 - 4) ÷ 2", "Пример:")
    svg += formula_box(520, 165, 220, 50, "2³ + 3²", "Пример:")
    
    # Section 2: Order of operations
    svg += section_label(50, 240, "Порядок действий", ACCENT)
    
    # Step boxes for order
    steps = [
        ("1", "Скобки", "( )"),
        ("2", "Степень", "aⁿ"),
        ("3", "Умнож./Дел.", "×  ÷"),
        ("4", "Слож./Выч.", "+  −"),
    ]
    for i, (num, name, sym) in enumerate(steps):
        bx = 50 + i * 180
        svg += card_colored(bx, 255, 165, 65, PRIMARY if i < 2 else ACCENT, 8)
        svg += text_el(bx + 82, 278, f"{num}. {name}", 13, WHITE, "middle", True)
        svg += text_el(bx + 82, 300, sym, 20, WHITE, "middle", True)
        if i < 3:
            svg += f'  <polygon points="{bx+170},287 {bx+178},282 {bx+178},292" fill="{PRIMARY_LIGHT}"/>\n'
    
    # Section 3: Worked example
    svg += section_label(50, 345, "Пример вычисления", SUCCESS)
    
    # Step by step solution
    svg += card(50, 360, 700, 60, 8)
    svg += text_el(65, 385, "3 + 4 × (5 − 2)² − 6 ÷ 3", 18, TEXT_DARK, "start", True)
    svg += text_el(580, 385, "= ?", 18, DANGER, "start", True)
    
    svg += card(50, 430, 700, 140, 8)
    steps_text = [
        ("1) Скобки:", "5 − 2 = 3", INFO),
        ("2) Степень:", "3² = 9", INFO),
        ("3) Умножение:", "4 × 9 = 36", PRIMARY),
        ("4) Деление:", "6 ÷ 3 = 2", PRIMARY),
        ("5) Сложение:", "3 + 36 = 39", SUCCESS),
        ("6) Вычитание:", "39 − 2 = 37", SUCCESS),
    ]
    for i, (step, result, color) in enumerate(steps_text):
        col = i // 3
        row = i % 3
        sx = 70 + col * 340
        sy = 455 + row * 35
        svg += text_el(sx, sy, step, 13, color, "start", True)
        svg += text_el(sx + 110, sy, result, 13, TEXT_DARK)
    
    # Final answer highlight
    svg += card_colored(550, 530, 195, 40, SUCCESS, 8)
    svg += text_el(647, 555, "Ответ: 37", 18, WHITE, "middle", True)
    
    svg += svg_footer()
    return svg


# =====================================================================
# LESSON 2: Выражения с переменными
# =====================================================================
def lesson2():
    svg = svg_header()
    svg += draw_background()
    svg += draw_header(2, "Выражения с переменными", "Подстановка и упрощение")
    
    svg += card(30, 95, 740, 490)
    
    # Section 1: Definition
    svg += section_label(50, 130, "Выражение с переменной", PRIMARY)
    svg += text_el(50, 150, "Содержит буквы (переменные), числа и знаки действий", 14, TEXT_MED)
    
    # Example
    svg += formula_box(50, 165, 340, 50, "3x + 5y − 2", "Выражение:")
    svg += formula_box(410, 165, 340, 50, "a² + 2ab + b²", "Формула:")
    
    # Section 2: Substitution
    svg += section_label(50, 240, "Подстановка значений", ACCENT)
    
    svg += card(50, 255, 700, 110, 8)
    svg += text_el(70, 280, "Найти значение выражения  2x + 3  при x = 4:", 15, TEXT_DARK)
    
    # Step-by-step
    svg += text_el(70, 305, "2x + 3 =", 16, TEXT_MED)
    svg += text_el(180, 305, "2 · 4 + 3 =", 16, PRIMARY, bold=True)
    svg += text_el(320, 305, "8 + 3 =", 16, PRIMARY, bold=True)
    svg += text_el(420, 305, "11", 18, SUCCESS, bold=True)
    
    svg += text_el(70, 340, "Найти значение  5a − b  при a = 2, b = 3:", 15, TEXT_DARK)
    svg += text_el(70, 360, "5 · 2 − 3 = 10 − 3 = 7", 16, PRIMARY, bold=True)
    
    # Section 3: Simplifying
    svg += section_label(50, 390, "Упрощение выражений", SUCCESS)
    
    svg += card(50, 405, 340, 80, 8)
    svg += text_el(65, 430, "Приведение подобных:", 13, TEXT_MED, bold=True)
    svg += text_el(65, 455, "3x + 5x = 8x", 16, PRIMARY, bold=True)
    svg += text_el(65, 475, "7a − 2a + 3a = 8a", 16, PRIMARY, bold=True)
    
    svg += card(410, 405, 340, 80, 8)
    svg += text_el(425, 430, "Раскрытие скобок:", 13, TEXT_MED, bold=True)
    svg += text_el(425, 455, "2(x + 3) = 2x + 6", 16, ACCENT, bold=True)
    svg += text_el(425, 475, "−(a − b) = −a + b", 16, ACCENT, bold=True)
    
    # Key rule box
    svg += card_colored(50, 505, 700, 65, PRIMARY_DARK, 10)
    svg += text_el(400, 530, "Правило: Подобные слагаемые — с одинаковой переменной частью", 14, WHITE, "middle", True)
    svg += text_el(400, 555, "3xy + 5xy = 8xy    |    4a² − a² = 3a²", 16, PRIMARY_LIGHTER, "middle", True)
    
    svg += svg_footer()
    return svg


# =====================================================================
# LESSON 3: Линейные уравнения
# =====================================================================
def lesson3():
    svg = svg_header()
    svg += draw_background()
    svg += draw_header(3, "Линейные уравнения", "ax + b = 0 и алгоритм решения")
    
    svg += card(30, 95, 740, 490)
    
    # General form
    svg += section_label(50, 130, "Общий вид линейного уравнения", PRIMARY)
    svg += formula_box(200, 140, 400, 55, "ax + b = 0", "Линейное уравнение:")
    
    # Section 2: Algorithm
    svg += section_label(50, 215, "Алгоритм решения", ACCENT)
    
    algo_steps = [
        ("1", "Раскрыть скобки", "2(x + 3) − x = 7"),
        ("2", "Перенести слагаемые", "2x + 6 − x = 7"),
        ("3", "Привести подобные", "x + 6 = 7"),
        ("4", "Найти корень", "x = 7 − 6 = 1"),
    ]
    for i, (num, name, expr) in enumerate(algo_steps):
        by = 232 + i * 48
        color = PRIMARY if i < 2 else ACCENT if i < 3 else SUCCESS
        svg += card_colored(50, by, 36, 36, color, 6)
        svg += text_el(68, by + 25, num, 18, WHITE, "middle", True)
        svg += text_el(98, by + 25, name, 14, TEXT_DARK, "start", True)
        svg += text_el(400, by + 25, expr, 15, color, "start", italic=True)
        if i < 3:
            svg += f'  <line x1="68" y1="{by+38}" x2="68" y2="{by+48}" stroke="{PRIMARY_LIGHT}" stroke-width="2"/>\n'
    
    # Section 3: More examples
    svg += section_label(50, 430, "Примеры", SUCCESS)
    
    svg += card(50, 445, 345, 55, 8)
    svg += text_el(65, 468, "3x − 5 = x + 3", 14, TEXT_DARK, bold=True)
    svg += text_el(65, 488, "3x − x = 3 + 5 → 2x = 8 → x = 4", 13, PRIMARY)
    
    svg += card(415, 445, 335, 55, 8)
    svg += text_el(430, 468, "5 − 2x = −3x + 1", 14, TEXT_DARK, bold=True)
    svg += text_el(430, 488, "−2x + 3x = 1 − 5 → x = −4", 13, PRIMARY)
    
    # Root concept
    svg += card_colored(50, 518, 700, 55, PRIMARY, 10)
    svg += text_el(400, 542, "Корень уравнения — значение переменной, при котором уравнение обращается в верное равенство", 13, WHITE, "middle", True)
    svg += text_el(400, 562, "Проверка: подставить найденное значение в исходное уравнение", 12, PRIMARY_LIGHTER, "middle")
    
    svg += svg_footer()
    return svg


# =====================================================================
# LESSON 4: Уравнения с модулями
# =====================================================================
def lesson4():
    svg = svg_header()
    svg += draw_background()
    svg += draw_header(4, "Уравнения с модулями", "|x| = a и разбор случаев")
    
    svg += card(30, 95, 740, 490)
    
    # Definition
    svg += section_label(50, 130, "Определение модуля", PRIMARY)
    svg += formula_box(50, 140, 340, 55, "|a| = a, a ≥ 0", "Если a ≥ 0:")
    svg += formula_box(410, 140, 340, 55, "|a| = −a, a &lt; 0", "Если a &lt; 0:")
    
    # Section 2: Key property
    svg += section_label(50, 220, "Уравнение |x| = a", ACCENT)
    
    svg += card(50, 235, 350, 95, 8)
    svg += text_el(65, 260, "Если a &gt; 0:", 14, SUCCESS, bold=True)
    svg += text_el(65, 282, "|x| = a  →  x = a  или  x = −a", 16, PRIMARY, bold=True)
    svg += text_el(65, 310, "Два корня!", 13, TEXT_MED)
    
    svg += card(415, 235, 335, 95, 8)
    svg += text_el(430, 260, "Если a = 0:", 14, WARNING, bold=True)
    svg += text_el(430, 282, "|x| = 0  →  x = 0", 16, WARNING, bold=True)
    svg += text_el(430, 310, "Один корень", 13, TEXT_MED)
    
    # Number line visualization
    svg += section_label(50, 355, "Геометрический смысл", INFO)
    svg += text_el(50, 375, "|x| — расстояние от числа x до нуля на числовой прямой", 14, TEXT_MED)
    
    # Number line for |x| = 3
    svg += card(50, 388, 700, 70, 8)
    svg += text_el(70, 410, "|x| = 3", 14, PRIMARY, bold=True)
    
    # Draw number line
    svg += f'  <line x1="90" y1="435" x2="710" y2="435" stroke="{TEXT_MED}" stroke-width="2"/>\n'
    svg += f'  <polygon points="710,435 702,431 702,439" fill="{TEXT_MED}"/>\n'
    
    # Points
    nl_center = 400
    svg += f'  <circle cx="{nl_center}" cy="435" r="4" fill="{TEXT_DARK}"/>\n'
    svg += text_el(nl_center, 452, "0", 11, TEXT_MED, "middle")
    
    svg += f'  <circle cx="{nl_center-90}" cy="435" r="5" fill="{DANGER}"/>\n'
    svg += text_el(nl_center-90, 452, "−3", 11, DANGER, "middle", True)
    
    svg += f'  <circle cx="{nl_center+90}" cy="435" r="5" fill="{DANGER}"/>\n'
    svg += text_el(nl_center+90, 452, "3", 11, DANGER, "middle", True)
    
    # Distance arrows
    svg += f'  <line x1="{nl_center-85}" y1="420" x2="{nl_center-5}" y2="420" stroke="{DANGER}" stroke-width="1.5" stroke-dasharray="4,3"/>\n'
    svg += f'  <line x1="{nl_center+5}" y1="420" x2="{nl_center+85}" y2="420" stroke="{DANGER}" stroke-width="1.5" stroke-dasharray="4,3"/>\n'
    svg += text_el(nl_center, 418, "3", 11, DANGER, "middle", True)
    
    # Worked example
    svg += card(50, 470, 700, 100, 8)
    svg += text_el(65, 495, "Пример: |2x − 1| = 5", 15, TEXT_DARK, bold=True)
    svg += text_el(65, 520, "Случай 1: 2x − 1 = 5 → 2x = 6 → x = 3", 14, PRIMARY, bold=True)
    svg += text_el(65, 542, "Случай 2: 2x − 1 = −5 → 2x = −4 → x = −2", 14, ACCENT, bold=True)
    svg += text_el(65, 562, "Ответ: x = 3  или  x = −2", 14, SUCCESS, bold=True)
    
    svg += svg_footer()
    return svg


# =====================================================================
# LESSON 5: Что такое функция
# =====================================================================
def lesson5():
    svg = svg_header()
    svg += draw_background()
    svg += draw_header(5, "Что такое функция", "Область определения и значения")
    
    svg += card(30, 95, 740, 490)
    
    # Definition
    svg += section_label(50, 130, "Определение функции", PRIMARY)
    svg += card(50, 140, 700, 55, 8)
    svg += text_el(400, 163, "Функция — зависимость, где каждому x соответствует единственное y", 15, TEXT_DARK, "middle", True)
    svg += text_el(400, 183, "Запись: y = f(x)", 16, PRIMARY, "middle", True)
    
    # Key concepts
    svg += section_label(50, 215, "Ключевые понятия", ACCENT)
    
    # Three concept boxes
    svg += card_colored(50, 230, 220, 80, PRIMARY, 8)
    svg += text_el(160, 255, "x — аргумент", 14, WHITE, "middle", True)
    svg += text_el(160, 278, "Независимая", 12, PRIMARY_LIGHTER, "middle")
    svg += text_el(160, 295, "переменная", 12, PRIMARY_LIGHTER, "middle")
    
    # Arrow
    svg += f'  <polygon points="275,270 290,264 290,276" fill="{ACCENT2}"/>\n'
    svg += text_el(283, 260, "f", 16, ACCENT2, "middle", True)
    
    svg += card_colored(300, 230, 220, 80, ACCENT, 8)
    svg += text_el(410, 255, "f — функция", 14, WHITE, "middle", True)
    svg += text_el(410, 278, "Правило", 12, PRIMARY_LIGHTER, "middle")
    svg += text_el(410, 295, "соответствия", 12, PRIMARY_LIGHTER, "middle")
    
    # Arrow
    svg += f'  <polygon points="525,270 540,264 540,276" fill="{ACCENT2}"/>\n'
    
    svg += card_colored(550, 230, 220, 80, PRIMARY_DARK, 8)
    svg += text_el(660, 255, "y — значение", 14, WHITE, "middle", True)
    svg += text_el(660, 278, "Зависимая", 12, PRIMARY_LIGHTER, "middle")
    svg += text_el(660, 295, "переменная", 12, PRIMARY_LIGHTER, "middle")
    
    # Domain and Range
    svg += section_label(50, 335, "Область определения и значений", SUCCESS)
    
    svg += card(50, 350, 345, 90, 8)
    svg += text_el(65, 375, "Область определения D(f)", 14, PRIMARY, bold=True)
    svg += text_el(65, 398, "Все допустимые значения x", 13, TEXT_MED)
    svg += text_el(65, 420, "Пример: y = 1/x  →  D(f) = R\\{0}", 13, ACCENT, italic=True)
    
    svg += card(415, 350, 335, 90, 8)
    svg += text_el(430, 375, "Множество значений E(f)", 14, ACCENT, bold=True)
    svg += text_el(430, 398, "Все значения функции y", 13, TEXT_MED)
    svg += text_el(430, 420, "Пример: y = x²  →  E(f) = [0; +∞)", 13, PRIMARY, italic=True)
    
    # Mapping diagram
    svg += section_label(50, 460, "Диаграмма соответствия", INFO)
    svg += card(50, 475, 700, 95, 8)
    
    # Left ellipse (domain)
    svg += f'  <ellipse cx="140" cy="522" rx="70" ry="35" fill="{PRIMARY_LIGHTER}" stroke="{PRIMARY}" stroke-width="2"/>\n'
    svg += text_el(140, 510, "D(f)", 12, PRIMARY, "middle", True)
    svg += text_el(120, 530, "1", 14, TEXT_DARK, "middle")
    svg += text_el(140, 530, "2", 14, TEXT_DARK, "middle")
    svg += text_el(160, 530, "3", 14, TEXT_DARK, "middle")
    
    # Arrows
    svg += f'  <line x1="210" y1="515" x2="580" y2="510" stroke="{PRIMARY}" stroke-width="1.5" marker-end="url(#arrowMarker)"/>\n'
    svg += f'  <line x1="210" y1="525" x2="580" y2="525" stroke="{PRIMARY}" stroke-width="1.5"/>\n'
    svg += f'  <line x1="210" y1="535" x2="580" y2="540" stroke="{PRIMARY}" stroke-width="1.5"/>\n'
    
    # Right ellipse (range)
    svg += f'  <ellipse cx="650" cy="522" rx="70" ry="35" fill="{PRIMARY_LIGHTER}" stroke="{ACCENT}" stroke-width="2"/>\n'
    svg += text_el(650, 510, "E(f)", 12, ACCENT, "middle", True)
    svg += text_el(630, 530, "a", 14, TEXT_DARK, "middle")
    svg += text_el(650, 530, "b", 14, TEXT_DARK, "middle")
    svg += text_el(670, 530, "c", 14, TEXT_DARK, "middle")
    
    # Arrowhead marker
    svg += f'  <defs><marker id="arrowMarker" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0,0 8,3 0,6" fill="{PRIMARY}"/></marker></defs>\n'
    
    svg += svg_footer()
    return svg


# =====================================================================
# LESSON 6: Линейная функция
# =====================================================================
def lesson6():
    svg = svg_header()
    svg += draw_background()
    svg += draw_header(6, "Линейная функция", "y = kx + b, график и коэффициенты")
    
    svg += card(30, 95, 740, 490)
    
    # General form
    svg += section_label(50, 130, "Общий вид", PRIMARY)
    svg += formula_box(200, 140, 400, 55, "y = kx + b", "Линейная функция:")
    
    # Coefficients explanation
    svg += section_label(50, 215, "Коэффициенты", ACCENT)
    
    svg += card(50, 230, 345, 70, 8)
    svg += text_el(65, 255, "k — угловой коэффициент (наклон)", 14, PRIMARY, bold=True)
    svg += text_el(65, 278, "k &gt; 0 — возрастает ↗", 13, SUCCESS)
    svg += text_el(65, 293, "k &lt; 0 — убывает ↘", 13, DANGER)
    
    svg += card(415, 230, 335, 70, 8)
    svg += text_el(430, 255, "b — свободный член (сдвиг)", 14, ACCENT, bold=True)
    svg += text_el(430, 278, "b — точка пересечения с осью y", 13, TEXT_MED)
    svg += text_el(430, 293, "График через (0; b)", 13, TEXT_MED)
    
    # Graph
    svg += section_label(50, 320, "Графики", SUCCESS)
    
    # Coordinate grid
    svg += coordinate_grid(80, 335, 380, 230, (-4, 6), (-3, 5),
                          points=[(0, 2, ""), (1, 4, "")],
                          line_func=lambda x: 2*x + 2)
    
    # Second line on same grid: y = -x + 1
    # We'll draw it manually with a different color
    svg += text_el(270, 355, "y = 2x + 2", 12, PRIMARY, "start", True)
    svg += text_el(270, 370, "y = −x + 1", 12, DANGER, "start", True)
    
    # Draw second line manually
    svg += f'  <line x1="80" y1="507" x2="460" y2="415" stroke="{DANGER}" stroke-width="2" stroke-dasharray="6,3"/>\n'
    
    # Right side: special cases
    svg += card(490, 335, 280, 230, 8)
    svg += text_el(505, 360, "Частные случаи:", 14, PRIMARY, bold=True)
    
    svg += card_colored(505, 375, 250, 45, PRIMARY, 6)
    svg += text_el(630, 395, "y = kx (b = 0)", 14, WHITE, "middle", True)
    svg += text_el(630, 410, "Прямая через (0,0)", 11, PRIMARY_LIGHTER, "middle")
    
    svg += card_colored(505, 430, 250, 45, ACCENT, 6)
    svg += text_el(630, 450, "y = b (k = 0)", 14, WHITE, "middle", True)
    svg += text_el(630, 465, "Горизонтальная прямая", 11, PRIMARY_LIGHTER, "middle")
    
    svg += card_colored(505, 485, 250, 45, SUCCESS, 6)
    svg += text_el(630, 505, "x = a", 14, WHITE, "middle", True)
    svg += text_el(630, 520, "Вертикальная прямая", 11, PRIMARY_LIGHTER, "middle")
    
    # Bottom info
    svg += text_el(630, 555, "Пересечение с ox: y=0", 11, TEXT_MED, "middle")
    svg += text_el(630, 568, "Пересечение с oy: x=0", 11, TEXT_MED, "middle")
    
    svg += svg_footer()
    return svg


# =====================================================================
# LESSON 7: Степень и её свойства
# =====================================================================
def lesson7():
    svg = svg_header()
    svg += draw_background()
    svg += draw_header(7, "Степень и её свойства", "aⁿ и операции со степенями")
    
    svg += card(30, 95, 740, 490)
    
    # Definition
    svg += section_label(50, 130, "Определение степени", PRIMARY)
    
    # a^n definition with visual
    svg += card(50, 140, 700, 60, 8)
    svg += text_el(70, 168, "aⁿ = a · a · a · ... · a", 20, PRIMARY, bold=True)
    svg += text_el(360, 158, "n раз", 13, TEXT_MED)
    svg += text_el(460, 168, "2⁵ = 2·2·2·2·2 = 32", 16, ACCENT, bold=True)
    
    # Properties
    svg += section_label(50, 225, "Свойства степеней", ACCENT)
    
    props = [
        ("Умножение", "aⁿ · aᵐ = aⁿ⁺ᵐ", "2³ · 2⁴ = 2⁷ = 128", PRIMARY),
        ("Деление", "aⁿ ÷ aᵐ = aⁿ⁻ᵐ", "3⁵ ÷ 3² = 3³ = 27", ACCENT),
        ("Степень степени", "(aⁿ)ᵐ = aⁿˣᵐ", "(2³)² = 2⁶ = 64", INFO),
        ("Степень произведения", "(ab)ⁿ = aⁿbⁿ", "(2·3)² = 4·9 = 36", SUCCESS),
        ("Степень частного", "(a/b)ⁿ = aⁿ/bⁿ", "(4/2)³ = 64/8 = 8", WARNING),
    ]
    
    for i, (name, formula, example, color) in enumerate(props):
        by = 240 + i * 56
        svg += card(50, by, 700, 48, 6)
        svg += card_colored(50, by, 8, 48, color, 3)
        svg += text_el(70, by + 18, name, 13, color, bold=True)
        svg += text_el(70, by + 38, formula, 15, TEXT_DARK, bold=True)
        svg += text_el(460, by + 30, example, 14, color)
    
    svg += svg_footer()
    return svg


# =====================================================================
# LESSON 8: Степень с нулевым показателем
# =====================================================================
def lesson8():
    svg = svg_header()
    svg += draw_background()
    svg += draw_header(8, "Степень с нулевым показателем", "a⁰ = 1 и отрицательные степени")
    
    svg += card(30, 95, 740, 490)
    
    # Main rule
    svg += section_label(50, 130, "Главное правило", PRIMARY)
    svg += formula_box(150, 140, 500, 60, "a⁰ = 1  (a ≠ 0)", "Нулевая степень:")
    
    # Explanation
    svg += section_label(50, 225, "Почему a⁰ = 1?", ACCENT)
    svg += card(50, 240, 700, 85, 8)
    svg += text_el(70, 265, "Рассмотрим:  a³ ÷ a³ = a³⁻³ = a⁰", 15, TEXT_DARK)
    svg += text_el(70, 290, "Но:  a³ ÷ a³ = 1  (любое число делится само на себя)", 15, TEXT_DARK)
    svg += text_el(70, 315, "Значит:  a⁰ = 1", 18, PRIMARY, bold=True)
    
    # Pattern visualization
    svg += section_label(50, 345, "Закономерность степеней", INFO)
    svg += card(50, 360, 700, 80, 8)
    
    powers = [
        ("2³", "= 8"),
        ("2²", "= 4"),
        ("2¹", "= 2"),
        ("2⁰", "= 1"),
        ("2⁻¹", "= 1/2"),
        ("2⁻²", "= 1/4"),
    ]
    for i, (pw, val) in enumerate(powers):
        px = 70 + i * 112
        color = SUCCESS if i < 3 else PRIMARY if i == 3 else DANGER
        svg += text_el(px, 390, pw, 14, color, bold=True)
        svg += text_el(px, 415, val, 13, TEXT_DARK)
        # Arrow showing ÷2
        if i < 5:
            svg += text_el(px + 65, 402, "÷2", 10, TEXT_LIGHT)
    
    # Negative exponents
    svg += section_label(50, 460, "Отрицательные степени", DANGER)
    svg += card(50, 475, 340, 95, 8)
    svg += text_el(65, 500, "a⁻ⁿ = 1 / aⁿ", 18, PRIMARY, bold=True)
    svg += text_el(65, 525, "3⁻² = 1/3² = 1/9", 14, ACCENT)
    svg += text_el(65, 548, "5⁻¹ = 1/5", 14, ACCENT)
    
    svg += card(415, 475, 335, 95, 8)
    svg += text_el(430, 500, "Важные примеры:", 14, TEXT_DARK, bold=True)
    svg += text_el(430, 525, "0⁰ — не определено!", 14, DANGER, bold=True)
    svg += text_el(430, 548, "1⁰ = 1;  (−5)⁰ = 1", 14, SUCCESS)
    
    svg += svg_footer()
    return svg


# =====================================================================
# LESSON 9: Одночлены и многочлены
# =====================================================================
def lesson9():
    svg = svg_header()
    svg += draw_background()
    svg += draw_header(9, "Одночлены и многочлены", "Стандартный вид и степень")
    
    svg += card(30, 95, 740, 490)
    
    # Monomial definition
    svg += section_label(50, 130, "Одночлен", PRIMARY)
    svg += card(50, 140, 700, 60, 8)
    svg += text_el(70, 165, "Одночлен — произведение чисел, переменных и их степеней", 14, TEXT_DARK)
    svg += text_el(70, 190, "3x²y    −5a³b    7    x⁴    −2m", 16, PRIMARY, bold=True)
    
    # Standard form
    svg += section_label(50, 220, "Стандартный вид одночлена", ACCENT)
    svg += card(50, 235, 345, 80, 8)
    svg += text_el(65, 258, "Коэффициент × степени переменных", 13, TEXT_MED)
    svg += text_el(65, 282, "3x × 2x² = 6x³", 16, PRIMARY, bold=True)
    svg += text_el(65, 305, "Коэфф.=6, степень=3", 12, ACCENT)
    
    svg += card(415, 235, 335, 80, 8)
    svg += text_el(430, 258, "Степень одночлена:", 13, TEXT_MED, bold=True)
    svg += text_el(430, 282, "Сумма показателей степеней", 13, TEXT_MED)
    svg += text_el(430, 305, "5x³y² → ст.= 3+2 = 5", 15, ACCENT, bold=True)
    
    # Polynomial definition
    svg += section_label(50, 340, "Многочлен", INFO)
    svg += card(50, 355, 700, 55, 8)
    svg += text_el(70, 378, "Многочлен — сумма одночленов", 14, TEXT_DARK)
    svg += text_el(70, 400, "3x² + 5x − 7    |    a²b − 2ab + b²    |    4m³n − mn² + 8", 15, INFO, bold=True)
    
    # Polynomial properties
    svg += section_label(50, 430, "Свойства многочлена", SUCCESS)
    
    svg += card(50, 445, 345, 65, 8)
    svg += text_el(65, 468, "Степень многочлена:", 13, TEXT_DARK, bold=True)
    svg += text_el(65, 490, "Наибольшая степень входящих", 12, TEXT_MED)
    svg += text_el(65, 505, "в него одночленов", 12, TEXT_MED)
    
    svg += card(415, 445, 335, 65, 8)
    svg += text_el(430, 468, "Пример:", 13, TEXT_DARK, bold=True)
    svg += text_el(430, 490, "3x⁴ + 2x² − x + 5", 15, PRIMARY, bold=True)
    svg += text_el(430, 505, "Степень = 4", 13, SUCCESS, bold=True)
    
    # Terms breakdown
    svg += card(50, 525, 700, 50, 8)
    svg += text_el(70, 548, "Члены многочлена: 3x⁴  |  +2x²  |  −x  |  +5 (свободный член)", 14, TEXT_DARK)
    svg += text_el(70, 565, "Подобные члены: 3x² и 5x² (одинаковая переменная часть)", 12, ACCENT)
    
    svg += svg_footer()
    return svg


# =====================================================================
# LESSON 10: Сложение и вычитание многочленов
# =====================================================================
def lesson10():
    svg = svg_header()
    svg += draw_background()
    svg += draw_header(10, "Сложение и вычитание многочленов", "Подобные слагаемые и скобки")
    
    svg += card(30, 95, 740, 490)
    
    # Rule 1: Addition
    svg += section_label(50, 130, "Сложение многочленов", PRIMARY)
    svg += card(50, 140, 700, 90, 8)
    svg += text_el(70, 165, "Правило: раскрыть скобки и привести подобные слагаемые", 14, TEXT_DARK, bold=True)
    svg += text_el(70, 190, "(3x² + 2x − 1) + (x² − 3x + 4)", 15, PRIMARY, bold=True)
    svg += text_el(70, 215, "= 3x² + 2x − 1 + x² − 3x + 4 = 4x² − x + 3", 15, SUCCESS, bold=True)
    
    # Rule 2: Subtraction
    svg += section_label(50, 250, "Вычитание многочленов", DANGER)
    svg += card(50, 260, 700, 90, 8)
    svg += text_el(70, 285, "Правило: поменять знаки в вычитаемом и привести подобные", 14, TEXT_DARK, bold=True)
    svg += text_el(70, 310, "(5a² − 3a + 2) − (2a² + a − 1)", 15, PRIMARY, bold=True)
    svg += text_el(70, 335, "= 5a² − 3a + 2 − 2a² − a + 1 = 3a² − 4a + 3", 15, SUCCESS, bold=True)
    
    # Key concept: like terms
    svg += section_label(50, 370, "Подобные слагаемые", ACCENT)
    svg += card(50, 385, 345, 80, 8)
    svg += text_el(65, 408, "Имеют одинаковую", 13, TEXT_MED)
    svg += text_el(65, 428, "переменную часть:", 13, TEXT_MED)
    svg += text_el(65, 453, "3x² и −5x² ✓", 14, SUCCESS, bold=True)
    svg += text_el(65, 470, "2xy и 3x²  ✗", 14, DANGER, bold=True)
    
    svg += card(415, 385, 335, 80, 8)
    svg += text_el(430, 408, "Приведение подобных:", 13, TEXT_MED, bold=True)
    svg += text_el(430, 430, "3x² + 5x² = 8x²", 15, PRIMARY, bold=True)
    svg += text_el(430, 453, "7ab − 2ab = 5ab", 15, PRIMARY, bold=True)
    
    # Parentheses rules
    svg += section_label(50, 485, "Правила раскрытия скобок", WARNING)
    svg += card(50, 500, 345, 70, 8)
    svg += text_el(65, 522, "Перед скобкой + :", 13, WARNING, bold=True)
    svg += text_el(65, 545, "+(a − b) = a − b", 15, TEXT_DARK, bold=True)
    svg += text_el(65, 562, "Знаки не меняются", 12, TEXT_MED)
    
    svg += card(415, 500, 335, 70, 8)
    svg += text_el(430, 522, "Перед скобкой − :", 13, DANGER, bold=True)
    svg += text_el(430, 545, "−(a − b) = −a + b", 15, TEXT_DARK, bold=True)
    svg += text_el(430, 562, "Знаки меняются!", 12, DANGER, bold=True)
    
    svg += svg_footer()
    return svg


# =====================================================================
# Main: Generate all SVGs
# =====================================================================
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
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
        (10, lesson10),
    ]
    
    for num, gen_func in generators:
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
        svg_content = gen_func()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"✅ Generated: {filepath}")
        
        # Validate
        try:
            ET.parse(filepath)
            print(f"   ✅ Valid XML")
        except ET.ParseError as e:
            print(f"   ❌ XML validation error: {e}")
    
    print(f"\n🎉 All {len(generators)} SVG files generated in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
