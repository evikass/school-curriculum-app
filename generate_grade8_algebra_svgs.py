#!/usr/bin/env python3
"""Generate Grade 8 Algebra lesson SVG images (lessons 1-11)."""

import os
import html

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/algebra"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Color palette - indigo/blue scheme
PRIMARY = "#4F46E5"
PRIMARY_LIGHT = "#818CF8"
PRIMARY_LIGHTER = "#C7D2FE"
PRIMARY_DARK = "#3730A3"
BG_GRADIENT_TOP = "#EEF2FF"
BG_GRADIENT_BOTTOM = "#E0E7FF"
ACCENT = "#6366F1"
ACCENT2 = "#3B82F6"
WHITE = "#FFFFFF"
DARK_TEXT = "#1E1B4B"
LIGHT_TEXT = "#4338CA"
FORMULA_BG = "#F5F3FF"
HIGHLIGHT = "#FCD34D"
SUCCESS = "#10B981"
BORDER = "#A5B4FC"


def xml_escape(text):
    """Escape text for XML/SVG content."""
    return html.escape(text, quote=True)


def svg_header(width=800, height=600):
    """Return SVG header with XML declaration and root element."""
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
'''


def svg_footer():
    """Return SVG closing tag."""
    return '</svg>\n'


def bg_gradient(gradient_id="bgGrad"):
    """Return background gradient definition."""
    return f'''  <defs>
    <linearGradient id="{gradient_id}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:{BG_GRADIENT_TOP};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{BG_GRADIENT_BOTTOM};stop-opacity:1"/>
    </linearGradient>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:{PRIMARY_DARK};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{PRIMARY};stop-opacity:1"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:{ACCENT};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{ACCENT2};stop-opacity:1"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:{WHITE};stop-opacity:0.95"/>
      <stop offset="100%" style="stop-color:{FORMULA_BG};stop-opacity:0.9"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="{PRIMARY_DARK}" flood-opacity="0.15"/>
    </filter>
    <filter id="softShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#000" flood-opacity="0.1"/>
    </filter>
  </defs>
'''


def draw_background():
    """Draw main background rectangle."""
    return f'  <rect width="800" height="600" fill="url(#bgGrad)" rx="0"/>\n'


def draw_header_bar(title, subtitle=""):
    """Draw the top header bar with title."""
    elements = []
    elements.append(f'  <rect x="0" y="0" width="800" height="80" fill="url(#headerGrad)" rx="0"/>')
    elements.append(f'  <line x1="0" y1="80" x2="800" y2="80" stroke="{PRIMARY_LIGHT}" stroke-width="2" opacity="0.5"/>')
    # Title text
    elements.append(f'  <text x="400" y="38" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="bold" fill="{WHITE}">{xml_escape(title)}</text>')
    if subtitle:
        elements.append(f'  <text x="400" y="62" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="{PRIMARY_LIGHTER}" opacity="0.9">{xml_escape(subtitle)}</text>')
    return '\n'.join(elements) + '\n'


def draw_lesson_number(num):
    """Draw lesson number badge."""
    cx, cy, r = 45, 40, 22
    elements = []
    elements.append(f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="{WHITE}" opacity="0.2"/>')
    elements.append(f'  <circle cx="{cx}" cy="{cy}" r="{r-2}" fill="none" stroke="{WHITE}" stroke-width="1.5" opacity="0.5"/>')
    elements.append(f'  <text x="{cx}" y="{cy+1}" text-anchor="middle" dominant-baseline="middle" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="bold" fill="{WHITE}">{num}</text>')
    return '\n'.join(elements) + '\n'


def draw_card(x, y, w, h, rx=12):
    """Draw a rounded card/panel."""
    return f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#cardGrad)" rx="{rx}" filter="url(#shadow)" stroke="{BORDER}" stroke-width="0.5"/>\n'


def draw_formula_box(x, y, w, h, formula_text, font_size=22, rx=8):
    """Draw a formula box with text centered inside."""
    elements = []
    elements.append(f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{FORMULA_BG}" rx="{rx}" stroke="{PRIMARY_LIGHT}" stroke-width="1.5" filter="url(#softShadow)"/>')
    elements.append(f'  <text x="{x + w//2}" y="{y + h//2 + 1}" text-anchor="middle" dominant-baseline="middle" font-family="Arial, Helvetica, sans-serif" font-size="{font_size}" font-weight="bold" fill="{PRIMARY_DARK}">{xml_escape(formula_text)}</text>')
    return '\n'.join(elements) + '\n'


def draw_section_title(x, y, text, color=PRIMARY):
    """Draw a section title with a small colored bar."""
    elements = []
    elements.append(f'  <rect x="{x}" y="{y}" width="4" height="18" fill="{color}" rx="2"/>')
    elements.append(f'  <text x="{x + 12}" y="{y + 14}" font-family="Arial, Helvetica, sans-serif" font-size="16" font-weight="bold" fill="{color}">{xml_escape(text)}</text>')
    return '\n'.join(elements) + '\n'


def draw_text(x, y, text, font_size=14, fill=DARK_TEXT, anchor="start", weight="normal"):
    """Draw a text element."""
    return f'  <text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Arial, Helvetica, sans-serif" font-size="{font_size}" font-weight="{weight}" fill="{fill}">{xml_escape(text)}</text>\n'


def draw_decorative_math_symbols():
    """Draw faint decorative math symbols scattered around."""
    elements = []
    symbols = ["∑", "∫", "√", "π", "∞", "Δ", "±", "≈", "≠", "∝"]
    positions = [(720, 130), (50, 550), (750, 480), (680, 560), (30, 130), (760, 300), (20, 300), (60, 480)]
    for i, (sx, sy) in enumerate(positions):
        sym = symbols[i % len(symbols)]
        elements.append(f'  <text x="{sx}" y="{sy}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="24" fill="{PRIMARY_LIGHTER}" opacity="0.3">{sym}</text>')
    return '\n'.join(elements) + '\n'


def draw_decorative_dots():
    """Draw a subtle dot pattern decoration."""
    elements = []
    for dx in range(0, 800, 40):
        for dy in range(90, 600, 40):
            elements.append(f'  <circle cx="{dx}" cy="{dy}" r="0.7" fill="{PRIMARY_LIGHTER}" opacity="0.15"/>')
    return '\n'.join(elements) + '\n'


def draw_divider(y):
    """Draw a horizontal divider line."""
    return f'  <line x1="40" y1="{y}" x2="760" y2="{y}" stroke="{PRIMARY_LIGHTER}" stroke-width="0.5" opacity="0.4"/>\n'


def draw_footer():
    """Draw footer with subject label."""
    elements = []
    elements.append(f'  <rect x="0" y="575" width="800" height="25" fill="{PRIMARY_DARK}" opacity="0.05"/>')
    elements.append(f'  <text x="400" y="592" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="{PRIMARY_LIGHT}" opacity="0.7">Алгебра · 8 класс</text>')
    return '\n'.join(elements) + '\n'


# ============================================================
# LESSON 1: Рациональные выражения
# ============================================================
def generate_lesson1():
    svg = svg_header()
    svg += bg_gradient()
    svg += draw_background()
    svg += draw_header_bar("Рациональные выражения", "Рациональные дроби и область допустимых значений")
    svg += draw_lesson_number(1)
    svg += draw_decorative_dots()
    svg += draw_decorative_math_symbols()

    # Main concept card
    svg += draw_card(30, 95, 740, 110, 10)
    svg += draw_section_title(50, 115, "Определение")
    svg += draw_text(50, 145, "Рациональное выражение — выражение, составленное из чисел и переменных", 13, DARK_TEXT)
    svg += draw_text(50, 163, "с помощью арифметических операций и возведения в целую степень.", 13, DARK_TEXT)

    # Fraction notation P/Q
    svg += draw_card(50, 175, 340, 60, 8)
    svg += draw_text(70, 195, "Целые выражения:", 12, PRIMARY)
    svg += draw_formula_box(70, 205, 300, 22, "3x² + 2x − 5;  a(b + c)", 13, 6)

    svg += draw_card(410, 175, 340, 60, 8)
    svg += draw_text(430, 195, "Дробные выражения:", 12, PRIMARY)
    svg += draw_formula_box(430, 205, 300, 22, "P/Q, где Q ≠ 0", 15, 6)

    # Big formula: P/Q
    svg += draw_card(200, 250, 400, 80, 10)
    svg += draw_text(220, 270, "Рациональная дробь:", 13, PRIMARY, weight="bold")
    # Draw fraction visually
    svg += f'  <text x="400" y="300" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="28" font-weight="bold" fill="{PRIMARY_DARK}">P / Q</text>\n'
    svg += f'  <text x="400" y="322" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="{LIGHT_TEXT}">где P, Q — многочлены, Q ≠ 0</text>\n'

    # ODZ section
    svg += draw_card(30, 340, 740, 110, 10)
    svg += draw_section_title(50, 360, "Область допустимых значений (ОДЗ)")
    svg += draw_text(50, 388, "ОДЗ — все значения переменных, при которых выражение имеет смысл.", 13, DARK_TEXT)
    svg += draw_text(50, 408, "Для дроби P/Q: знаменатель Q не должен равняться нулю!", 13, DARK_TEXT)
    svg += draw_formula_box(50, 420, 700, 22, "Q ≠ 0  —  условие существования дроби", 14, 6)

    # Example
    svg += draw_card(30, 460, 355, 100, 10)
    svg += draw_section_title(50, 480, "Пример 1")
    svg += draw_text(50, 505, "Дробь:  5 / (x − 3)", 14, DARK_TEXT)
    svg += draw_text(50, 525, "ОДЗ:  x − 3 ≠ 0  →  x ≠ 3", 14, SUCCESS, weight="bold")

    svg += draw_card(415, 460, 355, 100, 10)
    svg += draw_section_title(435, 480, "Пример 2")
    svg += draw_text(435, 505, "Дробь:  (2a + 1) / (a² − 4)", 14, DARK_TEXT)
    svg += draw_text(435, 525, "ОДЗ:  a² − 4 ≠ 0  →  a ≠ ±2", 14, SUCCESS, weight="bold")

    svg += draw_footer()
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 2: Основное свойство дроби
# ============================================================
def generate_lesson2():
    svg = svg_header()
    svg += bg_gradient()
    svg += draw_background()
    svg += draw_header_bar("Основное свойство дроби", "Тождественные преобразования рациональных дробей")
    svg += draw_lesson_number(2)
    svg += draw_decorative_dots()
    svg += draw_decorative_math_symbols()

    # Main property
    svg += draw_card(30, 95, 740, 130, 10)
    svg += draw_section_title(50, 115, "Основное свойство")
    svg += draw_text(50, 140, "Если числитель и знаменатель дроби умножить или разделить", 13, DARK_TEXT)
    svg += draw_text(50, 158, "на одно и то же выражение (≠ 0), получится тождественно равная дробь.", 13, DARK_TEXT)
    # Key formulas
    svg += draw_formula_box(60, 172, 330, 42, "a/b = (a·c)/(b·c),  c ≠ 0", 20, 8)
    svg += draw_formula_box(410, 172, 330, 42, "a/b = (a:c)/(b:c),  c ≠ 0", 20, 8)

    # Simplification
    svg += draw_card(30, 240, 740, 90, 10)
    svg += draw_section_title(50, 260, "Сокращение дробей")
    svg += draw_text(50, 285, "Деление числителя и знаменателя на их общий множитель.", 13, DARK_TEXT)
    svg += draw_formula_box(60, 298, 700, 22, "ax / bx = a / b   (x ≠ 0)", 16, 6)

    # Examples
    svg += draw_card(30, 345, 355, 115, 10)
    svg += draw_section_title(50, 365, "Пример 1: Сокращение")
    svg += draw_text(50, 390, "15x³ / 25x² =", 15, DARK_TEXT)
    svg += draw_text(50, 410, "= (15/25) · x³/x² = (3/5) · x", 14, LIGHT_TEXT)
    svg += draw_text(50, 432, "= 3x / 5", 16, SUCCESS, weight="bold")

    svg += draw_card(415, 345, 355, 115, 10)
    svg += draw_section_title(435, 365, "Пример 2: Приведение к ОЗ")
    svg += draw_text(435, 390, "3/a и 5/b  →  ОЗ = ab", 14, DARK_TEXT)
    svg += draw_text(435, 410, "3/a = 3b/(ab)", 14, LIGHT_TEXT)
    svg += draw_text(435, 432, "5/b = 5a/(ab)", 14, LIGHT_TEXT)

    # Warning box
    svg += draw_card(30, 475, 740, 85, 10)
    svg += f'  <rect x="30" y="475" width="740" height="85" rx="10" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1"/>\n'
    svg += draw_section_title(50, 495, "Внимание!", "#D97706")
    svg += draw_text(50, 518, "Сокращать можно только множители! Слагаемые сокращать нельзя.", 14, "#92400E", weight="bold")
    svg += draw_text(50, 540, "Нельзя: (a + b) / a ≠ b  —  это грубая ошибка!", 14, "#DC2626")

    svg += draw_footer()
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 3: Сложение и вычитание дробей
# ============================================================
def generate_lesson3():
    svg = svg_header()
    svg += bg_gradient()
    svg += draw_background()
    svg += draw_header_bar("Сложение и вычитание дробей", "Алгоритмы работы с рациональными дробями")
    svg += draw_lesson_number(3)
    svg += draw_decorative_dots()
    svg += draw_decorative_math_symbols()

    # Same denominator
    svg += draw_card(30, 95, 740, 110, 10)
    svg += draw_section_title(50, 115, "Одинаковые знаменатели")
    svg += draw_text(50, 140, "При одинаковых знаменателях складываем/вычитаем числители:", 13, DARK_TEXT)
    svg += draw_formula_box(60, 155, 330, 38, "a/c + b/c = (a+b)/c", 19, 8)
    svg += draw_formula_box(410, 155, 330, 38, "a/c − b/c = (a−b)/c", 19, 8)

    # Different denominators
    svg += draw_card(30, 220, 740, 130, 10)
    svg += draw_section_title(50, 240, "Разные знаменатели")
    svg += draw_text(50, 265, "1. Найти общий знаменатель (ОЗ)", 13, DARK_TEXT)
    svg += draw_text(50, 283, "2. Найти дополнительные множители", 13, DARK_TEXT)
    svg += draw_text(50, 301, "3. Привести дроби к ОЗ", 13, DARK_TEXT)
    svg += draw_text(50, 319, "4. Сложить/вычесть числители", 13, DARK_TEXT)
    svg += draw_formula_box(60, 328, 700, 18, "a/b + c/d = (ad + bc) / bd", 14, 6)

    # Example
    svg += draw_card(30, 365, 355, 190, 10)
    svg += draw_section_title(50, 385, "Пример: сложение")
    svg += draw_text(50, 410, "3/x + 5/(x+2)", 15, DARK_TEXT)
    svg += draw_text(50, 435, "ОЗ = x(x+2)", 14, PRIMARY, weight="bold")
    svg += draw_text(50, 458, "Доп. множ.: (x+2) и x", 13, LIGHT_TEXT)
    svg += draw_text(50, 480, "= 3(x+2)/[x(x+2)] + 5x/[x(x+2)]", 13, LIGHT_TEXT)
    svg += draw_text(50, 502, "= (3x+6+5x) / [x(x+2)]", 13, LIGHT_TEXT)
    svg += draw_text(50, 525, "= (8x+6) / [x(x+2)]", 15, SUCCESS, weight="bold")

    svg += draw_card(415, 365, 355, 190, 10)
    svg += draw_section_title(435, 385, "Пример: вычитание")
    svg += draw_text(435, 410, "7/a − 3/a", 15, DARK_TEXT)
    svg += draw_text(435, 435, "Одинаковые знаменатели!", 14, PRIMARY, weight="bold")
    svg += draw_text(435, 458, "= (7 − 3) / a", 14, LIGHT_TEXT)
    svg += draw_text(435, 490, "= 4 / a", 18, SUCCESS, weight="bold")

    svg += draw_footer()
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 4: Арифметический квадратный корень
# ============================================================
def generate_lesson4():
    svg = svg_header()
    svg += bg_gradient()
    svg += draw_background()
    svg += draw_header_bar("Арифметический квадратный корень", "Определение и основные свойства")
    svg += draw_lesson_number(4)
    svg += draw_decorative_dots()
    svg += draw_decorative_math_symbols()

    # Definition
    svg += draw_card(30, 95, 740, 130, 10)
    svg += draw_section_title(50, 115, "Определение")
    svg += draw_text(50, 140, "Арифметическим квадратным корнем из неотрицательного числа a", 13, DARK_TEXT)
    svg += draw_text(50, 158, "называется неотрицательное число, квадрат которого равен a.", 13, DARK_TEXT)
    svg += draw_formula_box(200, 175, 400, 40, "√a = b,  если b² = a  и b ≥ 0", 18, 8)

    # Key properties
    svg += draw_card(30, 240, 740, 120, 10)
    svg += draw_section_title(50, 260, "Основные свойства")
    svg += draw_formula_box(50, 280, 350, 32, "√a ≥ 0  при a ≥ 0", 17, 6)
    svg += draw_formula_box(410, 280, 350, 32, "(√a)² = a  при a ≥ 0", 17, 6)
    svg += draw_formula_box(50, 320, 350, 32, "√0 = 0", 17, 6)
    svg += draw_formula_box(410, 320, 350, 32, "√1 = 1", 17, 6)

    # Important note
    svg += draw_card(30, 375, 740, 60, 10)
    svg += f'  <rect x="30" y="375" width="740" height="60" rx="10" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1"/>\n'
    svg += draw_text(50, 398, "Квадратный корень из отрицательного числа не существует на множестве R!", 14, "#92400E", weight="bold")
    svg += draw_formula_box(50, 410, 700, 20, "a ≥ 0  —  обязательное условие!", 13, 6)

    # Visual: square root on number line
    svg += draw_card(30, 450, 740, 110, 10)
    svg += draw_section_title(50, 470, "Примеры")
    # Draw mini number line
    svg += f'  <line x1="60" y1="510" x2="740" y2="510" stroke="{PRIMARY_LIGHT}" stroke-width="2"/>\n'
    markers = [("0", 60), ("1", 140), ("4", 300), ("9", 500), ("16", 700)]
    for label, px in markers:
        svg += f'  <line x1="{px}" y1="505" x2="{px}" y2="515" stroke="{PRIMARY}" stroke-width="2"/>\n'
        svg += f'  <text x="{px}" y="530" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="{DARK_TEXT}">{label}</text>\n'
    sqrt_markers = [("0", 60), ("1", 140), ("2", 220), ("3", 400), ("4", 600)]
    for label, px in sqrt_markers:
        svg += f'  <circle cx="{px}" cy="510" r="4" fill="{ACCENT}"/>\n'
        svg += f'  <text x="{px}" y="498" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">√{int(label)**2 if label.isdigit() else label}={label}</text>\n'

    svg += draw_footer()
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 5: Свойства квадратного корня
# ============================================================
def generate_lesson5():
    svg = svg_header()
    svg += bg_gradient()
    svg += draw_background()
    svg += draw_header_bar("Свойства квадратного корня", "Три основных свойства корня")
    svg += draw_lesson_number(5)
    svg += draw_decorative_dots()
    svg += draw_decorative_math_symbols()

    # Property 1
    svg += draw_card(30, 95, 740, 100, 10)
    svg += f'  <circle cx="55" cy="118" r="14" fill="{PRIMARY}" opacity="0.15"/>\n'
    svg += f'  <text x="55" y="123" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="bold" fill="{PRIMARY}">1</text>\n'
    svg += draw_text(80, 118, "Корень из произведения", 15, PRIMARY, weight="bold")
    svg += draw_formula_box(60, 135, 700, 48, "√(a · b) = √a · √b    (a ≥ 0, b ≥ 0)", 22, 8)
    svg += draw_text(60, 190, "Пример: √36 = √(9·4) = √9 · √4 = 3 · 2 = 6", 13, SUCCESS, weight="bold")

    # Property 2
    svg += draw_card(30, 205, 740, 100, 10)
    svg += f'  <circle cx="55" cy="228" r="14" fill="{PRIMARY}" opacity="0.15"/>\n'
    svg += f'  <text x="55" y="233" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="bold" fill="{PRIMARY}">2</text>\n'
    svg += draw_text(80, 228, "Корень из частного", 15, PRIMARY, weight="bold")
    svg += draw_formula_box(60, 245, 700, 48, "√(a / b) = √a / √b    (a ≥ 0, b > 0)", 22, 8)
    svg += draw_text(60, 300, "Пример: √(49/4) = √49 / √4 = 7 / 2 = 3.5", 13, SUCCESS, weight="bold")

    # Property 3
    svg += draw_card(30, 315, 740, 100, 10)
    svg += f'  <circle cx="55" cy="338" r="14" fill="{PRIMARY}" opacity="0.15"/>\n'
    svg += f'  <text x="55" y="343" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="bold" fill="{PRIMARY}">3</text>\n'
    svg += draw_text(80, 338, "Корень из квадрата", 15, PRIMARY, weight="bold")
    svg += draw_formula_box(60, 355, 700, 48, "√(a²) = |a|    (для любого a)", 22, 8)
    svg += draw_text(60, 410, "Пример: √((-5)²) = √25 = |−5| = 5", 13, SUCCESS, weight="bold")

    # Important notes
    svg += draw_card(30, 425, 355, 140, 10)
    svg += draw_section_title(50, 445, "Запомни!")
    svg += draw_text(50, 468, "√(a+b) ≠ √a + √b", 14, "#DC2626", weight="bold")
    svg += draw_text(50, 490, "√(a−b) ≠ √a − √b", 14, "#DC2626", weight="bold")
    svg += draw_text(50, 518, "Проверка: √(9+16) = √25 = 5", 12, DARK_TEXT)
    svg += draw_text(50, 536, "Но √9 + √16 = 3+4 = 7 ≠ 5", 12, "#DC2626")

    svg += draw_card(415, 425, 355, 140, 10)
    svg += draw_section_title(435, 445, "Вынесение множителя")
    svg += draw_text(435, 468, "√50 = √(25·2) = 5√2", 14, DARK_TEXT)
    svg += draw_text(435, 493, "√72 = √(36·2) = 6√2", 14, DARK_TEXT)
    svg += draw_text(435, 518, "√98 = √(49·2) = 7√2", 14, DARK_TEXT)
    svg += draw_text(435, 545, "Общий алгоритм: разложить", 12, LIGHT_TEXT)
    svg += draw_text(435, 560, "на квадратный и остаток", 12, LIGHT_TEXT)

    svg += draw_footer()
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 6: Преобразование выражений с корнями
# ============================================================
def generate_lesson6():
    svg = svg_header()
    svg += bg_gradient()
    svg += draw_background()
    svg += draw_header_bar("Преобразование выражений с корнями", "Подобные корни и избавление от иррациональности")
    svg += draw_lesson_number(6)
    svg += draw_decorative_dots()
    svg += draw_decorative_math_symbols()

    # Like radicals
    svg += draw_card(30, 95, 740, 115, 10)
    svg += draw_section_title(50, 115, "Подобные радикалы")
    svg += draw_text(50, 140, "Подобные радикалы — корни с одинаковым подкоренным выражением.", 13, DARK_TEXT)
    svg += draw_text(50, 160, "Их можно складывать и вычитать как подобные слагаемые:", 13, DARK_TEXT)
    svg += draw_formula_box(60, 175, 700, 28, "3√2 + 5√2 = 8√2 ;   7√3 − 4√3 = 3√3", 16, 6)

    # Simplification examples
    svg += draw_card(30, 225, 355, 165, 10)
    svg += draw_section_title(50, 245, "Упрощение выражений")
    svg += draw_text(50, 270, "√12 + √27 − √48", 14, DARK_TEXT)
    svg += draw_text(50, 295, "= 2√3 + 3√3 − 4√3", 13, LIGHT_TEXT)
    svg += draw_text(50, 320, "= (2+3−4) · √3", 13, LIGHT_TEXT)
    svg += draw_text(50, 350, "= √3", 18, SUCCESS, weight="bold")

    svg += draw_card(415, 225, 355, 165, 10)
    svg += draw_section_title(435, 245, "Избавление от иррациональности в знаменателе")
    svg += draw_text(435, 270, "Правило: умножить числитель и", 12, DARK_TEXT)
    svg += draw_text(435, 288, "знаменатель на корень из знаменателя", 12, DARK_TEXT)
    svg += draw_text(435, 315, "5/√3 = 5√3 / (√3·√3) = 5√3/3", 13, DARK_TEXT)
    svg += draw_text(435, 345, "2/√7 = 2√7 / 7", 14, SUCCESS, weight="bold")

    # Conjugate method
    svg += draw_card(30, 405, 740, 80, 10)
    svg += draw_section_title(50, 425, "Метод сопряжённого выражения")
    svg += draw_text(50, 450, "Для a/(√b + √c) умножаем на (√b − √c):", 13, DARK_TEXT)
    svg += draw_formula_box(60, 462, 700, 18, "1/(√2+1) = (√2−1)/[(√2+1)(√2−1)] = (√2−1)/(2−1) = √2−1", 13, 6)

    # Mixed examples
    svg += draw_card(30, 500, 355, 65, 10)
    svg += draw_section_title(50, 518, "Ещё пример")
    svg += draw_text(50, 540, "√18 − √8 = 3√2 − 2√2 = √2", 14, SUCCESS, weight="bold")

    svg += draw_card(415, 500, 355, 65, 10)
    svg += draw_section_title(435, 518, "Формула")
    svg += draw_formula_box(435, 535, 330, 22, "a/√b = a√b / b", 15, 6)

    svg += draw_footer()
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 7: Неполные квадратные уравнения
# ============================================================
def generate_lesson7():
    svg = svg_header()
    svg += bg_gradient()
    svg += draw_background()
    svg += draw_header_bar("Неполные квадратные уравнения", "Три типа неполных уравнений и их решения")
    svg += draw_lesson_number(7)
    svg += draw_decorative_dots()
    svg += draw_decorative_math_symbols()

    # General form
    svg += draw_card(30, 95, 740, 50, 10)
    svg += draw_text(50, 118, "Общий вид квадратного уравнения:", 13, DARK_TEXT)
    svg += draw_formula_box(370, 100, 390, 38, "ax² + bx + c = 0,  a ≠ 0", 17, 8)

    # Type 1: ax² + c = 0
    svg += draw_card(30, 160, 240, 155, 10)
    svg += f'  <rect x="30" y="160" width="240" height="28" rx="10" fill="{PRIMARY}" opacity="0.1"/>\n'
    svg += draw_text(60, 178, "Тип 1: ax² + c = 0", 14, PRIMARY, weight="bold")
    svg += draw_text(50, 205, "bx = 0, c ≠ 0", 12, LIGHT_TEXT)
    svg += draw_text(50, 225, "ax² = −c", 13, DARK_TEXT)
    svg += draw_text(50, 245, "x² = −c/a", 13, DARK_TEXT)
    svg += draw_text(50, 270, "Если −c/a > 0:", 12, LIGHT_TEXT)
    svg += draw_text(50, 288, "x = ±√(−c/a)", 14, SUCCESS, weight="bold")
    svg += draw_text(50, 308, "Если −c/a < 0: нет корней", 11, "#DC2626")

    # Type 2: ax² + bx = 0
    svg += draw_card(280, 160, 240, 155, 10)
    svg += f'  <rect x="280" y="160" width="240" height="28" rx="10" fill="{PRIMARY}" opacity="0.1"/>\n'
    svg += draw_text(310, 178, "Тип 2: ax² + bx = 0", 14, PRIMARY, weight="bold")
    svg += draw_text(300, 205, "c = 0", 12, LIGHT_TEXT)
    svg += draw_text(300, 225, "x(ax + b) = 0", 13, DARK_TEXT)
    svg += draw_text(300, 252, "x = 0", 14, SUCCESS, weight="bold")
    svg += draw_text(300, 278, "ax + b = 0 → x = −b/a", 13, DARK_TEXT)
    svg += draw_text(300, 308, "Два корня всегда!", 12, PRIMARY, weight="bold")

    # Type 3: ax² = 0
    svg += draw_card(530, 160, 240, 155, 10)
    svg += f'  <rect x="530" y="160" width="240" height="28" rx="10" fill="{PRIMARY}" opacity="0.1"/>\n'
    svg += draw_text(560, 178, "Тип 3: ax² = 0", 14, PRIMARY, weight="bold")
    svg += draw_text(550, 205, "b = 0, c = 0", 12, LIGHT_TEXT)
    svg += draw_text(550, 225, "x² = 0/a = 0", 13, DARK_TEXT)
    svg += draw_text(550, 260, "x = 0", 20, SUCCESS, weight="bold")
    svg += draw_text(550, 290, "Один корень", 13, PRIMARY, weight="bold")
    svg += draw_text(550, 308, "(двойной корень)", 11, LIGHT_TEXT)

    # Examples
    svg += draw_card(30, 330, 240, 145, 10)
    svg += draw_section_title(50, 350, "Пример 1")
    svg += draw_text(50, 375, "2x² − 18 = 0", 14, DARK_TEXT)
    svg += draw_text(50, 398, "2x² = 18", 13, LIGHT_TEXT)
    svg += draw_text(50, 418, "x² = 9", 13, LIGHT_TEXT)
    svg += draw_text(50, 445, "x = ±3", 16, SUCCESS, weight="bold")
    svg += draw_text(50, 468, "Ответ: −3; 3", 13, PRIMARY)

    svg += draw_card(280, 330, 240, 145, 10)
    svg += draw_section_title(300, 350, "Пример 2")
    svg += draw_text(300, 375, "3x² + 6x = 0", 14, DARK_TEXT)
    svg += draw_text(300, 398, "3x(x + 2) = 0", 13, LIGHT_TEXT)
    svg += draw_text(300, 418, "x = 0 или x+2 = 0", 13, LIGHT_TEXT)
    svg += draw_text(300, 445, "x₁=0, x₂=−2", 15, SUCCESS, weight="bold")
    svg += draw_text(300, 468, "Ответ: −2; 0", 13, PRIMARY)

    svg += draw_card(530, 330, 240, 145, 10)
    svg += draw_section_title(550, 350, "Пример 3")
    svg += draw_text(550, 375, "5x² = 0", 14, DARK_TEXT)
    svg += draw_text(550, 398, "x² = 0", 13, LIGHT_TEXT)
    svg += draw_text(550, 425, "x = 0", 18, SUCCESS, weight="bold")
    svg += draw_text(550, 455, "Ответ: 0", 13, PRIMARY)

    # Summary
    svg += draw_card(30, 490, 740, 75, 10)
    svg += draw_section_title(50, 510, "Алгоритм решения")
    svg += draw_text(50, 533, "1. Определить тип неполного уравнения  →  2. Применить формулу  →  3. Записать ответ", 13, DARK_TEXT)
    svg += draw_text(50, 555, "Неполные уравнения решаются БЕЗ дискриминанта!", 14, PRIMARY, weight="bold")

    svg += draw_footer()
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 8: Формула корней квадратного уравнения
# ============================================================
def generate_lesson8():
    svg = svg_header()
    svg += bg_gradient()
    svg += draw_background()
    svg += draw_header_bar("Формула корней квадратного уравнения", "Дискриминант и теорема Виета")
    svg += draw_lesson_number(8)
    svg += draw_decorative_dots()
    svg += draw_decorative_math_symbols()

    # Discriminant
    svg += draw_card(30, 95, 740, 95, 10)
    svg += draw_section_title(50, 115, "Дискриминант")
    svg += draw_text(50, 140, "Для уравнения ax² + bx + c = 0:", 13, DARK_TEXT)
    svg += draw_formula_box(220, 152, 360, 32, "D = b² − 4ac", 24, 8)

    # Three cases for D
    svg += draw_card(30, 200, 240, 140, 10)
    svg += f'  <rect x="30" y="200" width="240" height="24" rx="10" fill="{SUCCESS}" opacity="0.15"/>\n'
    svg += draw_text(45, 216, "D > 0 — два корня", 13, SUCCESS, weight="bold")
    svg += draw_formula_box(45, 228, 210, 40, "x = (−b ± √D) / (2a)", 14, 6)
    svg += draw_text(45, 282, "Два различных корня", 11, DARK_TEXT)
    svg += draw_text(45, 300, "x₁ ≠ x₂", 13, SUCCESS)

    svg += draw_card(280, 200, 240, 140, 10)
    svg += f'  <rect x="280" y="200" width="240" height="24" rx="10" fill="{ACCENT2}" opacity="0.15"/>\n'
    svg += draw_text(295, 216, "D = 0 — один корень", 13, ACCENT2, weight="bold")
    svg += draw_formula_box(295, 228, 210, 40, "x = −b / (2a)", 16, 6)
    svg += draw_text(295, 282, "Один корень (двойной)", 11, DARK_TEXT)
    svg += draw_text(295, 300, "x₁ = x₂", 13, ACCENT2)

    svg += draw_card(530, 200, 240, 140, 10)
    svg += f'  <rect x="530" y="200" width="240" height="24" rx="10" fill="#DC2626" opacity="0.1"/>\n'
    svg += draw_text(545, 216, "D < 0 — нет корней", 13, "#DC2626", weight="bold")
    svg += draw_text(545, 255, "На множестве R", 13, DARK_TEXT)
    svg += draw_text(545, 278, "действительных корней", 12, DARK_TEXT)
    svg += draw_text(545, 300, "не существует", 13, "#DC2626")

    # Main formula highlighted
    svg += draw_card(100, 355, 600, 55, 12)
    svg += f'  <rect x="100" y="355" width="600" height="55" rx="12" fill="{HIGHLIGHT}" opacity="0.3" stroke="{HIGHLIGHT}" stroke-width="2"/>\n'
    svg += draw_text(400, 377, "Главная формула:", 12, PRIMARY, "middle", "bold")
    svg += draw_formula_box(120, 387, 560, 20, "x = (−b ± √(b²−4ac)) / (2a)", 16, 6)

    # Vieta's theorem
    svg += draw_card(30, 425, 355, 140, 10)
    svg += draw_section_title(50, 445, "Теорема Виета")
    svg += draw_text(50, 468, "Если x₁, x₂ — корни ax²+bx+c=0:", 12, DARK_TEXT)
    svg += draw_formula_box(50, 482, 330, 24, "x₁ + x₂ = −b/a", 16, 6)
    svg += draw_formula_box(50, 512, 330, 24, "x₁ · x₂ = c/a", 16, 6)
    svg += draw_text(50, 550, "Для x²+px+q=0: x₁+x₂=−p, x₁·x₂=q", 11, LIGHT_TEXT)

    # Example
    svg += draw_card(415, 425, 355, 140, 10)
    svg += draw_section_title(435, 445, "Пример")
    svg += draw_text(435, 468, "x² − 5x + 6 = 0", 14, DARK_TEXT)
    svg += draw_text(435, 488, "D = 25 − 24 = 1 > 0", 13, LIGHT_TEXT)
    svg += draw_text(435, 508, "x = (5 ± 1) / 2", 13, LIGHT_TEXT)
    svg += draw_text(435, 532, "x₁ = 2,  x₂ = 3", 15, SUCCESS, weight="bold")
    svg += draw_text(435, 555, "Проверка Виета: 2+3=5 ✓  2·3=6 ✓", 11, PRIMARY)

    svg += draw_footer()
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 9: Числовые неравенства
# ============================================================
def generate_lesson9():
    svg = svg_header()
    svg += bg_gradient()
    svg += draw_background()
    svg += draw_header_bar("Числовые неравенства", "Свойства и сравнение чисел")
    svg += draw_lesson_number(9)
    svg += draw_decorative_dots()
    svg += draw_decorative_math_symbols()

    # Definition
    svg += draw_card(30, 95, 740, 70, 10)
    svg += draw_section_title(50, 115, "Определение")
    svg += draw_text(50, 138, "Число a больше числа b (a > b), если разность a − b — положительное число.", 13, DARK_TEXT)
    svg += draw_text(50, 156, "Число a меньше числа b (a < b), если разность a − b — отрицательное число.", 13, DARK_TEXT)

    # Properties
    svg += draw_card(30, 180, 740, 165, 10)
    svg += draw_section_title(50, 200, "Свойства неравенств")
    # Property 1
    svg += f'  <circle cx="60" cy="225" r="10" fill="{PRIMARY}" opacity="0.15"/>\n'
    svg += f'  <text x="60" y="229" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">1</text>\n'
    svg += draw_text(78, 229, "Если a > b, то b < a (симметричность)", 13, DARK_TEXT)
    # Property 2
    svg += f'  <circle cx="60" cy="252" r="10" fill="{PRIMARY}" opacity="0.15"/>\n'
    svg += f'  <text x="60" y="256" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">2</text>\n'
    svg += draw_text(78, 256, "Если a > b и b > c, то a > c (транзитивность)", 13, DARK_TEXT)
    # Property 3
    svg += f'  <circle cx="60" cy="279" r="10" fill="{PRIMARY}" opacity="0.15"/>\n'
    svg += f'  <text x="60" y="283" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">3</text>\n'
    svg += draw_text(78, 283, "Если a > b, то a + c > b + c (прибавление числа)", 13, DARK_TEXT)
    # Property 4
    svg += f'  <circle cx="60" cy="306" r="10" fill="{PRIMARY}" opacity="0.15"/>\n'
    svg += f'  <text x="60" y="310" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">4</text>\n'
    svg += draw_text(78, 310, "Если a > b и c > 0, то ac > bc (умножение на +)", 13, DARK_TEXT)
    # Property 5
    svg += f'  <circle cx="60" cy="333" r="10" fill="{PRIMARY}" opacity="0.15"/>\n'
    svg += f'  <text x="60" y="337" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">5</text>\n'
    svg += draw_text(78, 337, "Если a > b и c < 0, то ac < bc (умножение на − меняет знак!)", 13, "#DC2626", weight="bold")

    # Comparison methods
    svg += draw_card(30, 360, 355, 100, 10)
    svg += draw_section_title(50, 380, "Метод сравнения")
    svg += draw_text(50, 403, "Разность a − b:", 13, DARK_TEXT)
    svg += draw_text(50, 423, "> 0  →  a > b", 13, SUCCESS)
    svg += draw_text(50, 443, "= 0  →  a = b", 13, ACCENT2)
    svg += draw_text(50, 460, "< 0  →  a < b", 13, "#DC2626")

    svg += draw_card(415, 360, 355, 100, 10)
    svg += draw_section_title(435, 380, "Пример")
    svg += draw_text(435, 403, "Сравнить: 3√2 и 2√5", 14, DARK_TEXT)
    svg += draw_text(435, 425, "3√2 ≈ 4.24", 13, LIGHT_TEXT)
    svg += draw_text(435, 445, "2√5 ≈ 4.47", 13, LIGHT_TEXT)
    svg += draw_text(435, 468, "3√2 < 2√5", 15, SUCCESS, weight="bold")

    # Number line visual
    svg += draw_card(30, 475, 740, 90, 10)
    svg += draw_section_title(50, 495, "Числовая прямая")
    svg += f'  <line x1="60" y1="530" x2="740" y2="530" stroke="{PRIMARY}" stroke-width="2"/>\n'
    svg += f'  <polygon points="745,530 735,525 735,535" fill="{PRIMARY}"/>\n'
    # Mark points
    pts = [(-3, 120), (-1, 230), (0, 310), (2, 470), (5, 650)]
    for val, px in pts:
        svg += f'  <line x1="{px}" y1="525" x2="{px}" y2="535" stroke="{PRIMARY}" stroke-width="1.5"/>\n'
        svg += f'  <text x="{px}" y="550" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="{DARK_TEXT}">{val}</text>\n'
    svg += f'  <line x1="230" y1="520" x2="470" y2="520" stroke="{ACCENT2}" stroke-width="3"/>\n'
    svg += draw_text(350, 516, "−1 < x < 2", 10, ACCENT2, "middle")

    svg += draw_footer()
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 10: Линейные неравенства
# ============================================================
def generate_lesson10():
    svg = svg_header()
    svg += bg_gradient()
    svg += draw_background()
    svg += draw_header_bar("Линейные неравенства", "Решение неравенств вида ax + b > 0")
    svg += draw_lesson_number(10)
    svg += draw_decorative_dots()
    svg += draw_decorative_math_symbols()

    # Definition
    svg += draw_card(30, 95, 740, 65, 10)
    svg += draw_section_title(50, 115, "Определение")
    svg += draw_text(50, 138, "Линейное неравенство — неравенство вида ax + b > 0 (или <, ≥, ≤),", 13, DARK_TEXT)
    svg += draw_text(50, 154, "где a и b — числа, x — переменная.", 13, DARK_TEXT)

    # Algorithm
    svg += draw_card(30, 175, 740, 130, 10)
    svg += draw_section_title(50, 195, "Алгоритм решения")
    steps = [
        ("1", "Перенести слагаемые с x в одну часть, числа — в другую"),
        ("2", "Привести подобные слагаемые"),
        ("3", "Разделить обе части на коэффициент при x"),
        ("4", "Если делим на отрицательное — поменять знак неравенства!"),
    ]
    for i, (num, text) in enumerate(steps):
        yy = 218 + i * 24
        color = "#DC2626" if i == 3 else DARK_TEXT
        weight = "bold" if i == 3 else "normal"
        svg += f'  <circle cx="62" cy="{yy-4}" r="10" fill="{PRIMARY}" opacity="0.12"/>\n'
        svg += f'  <text x="62" y="{yy}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{num}</text>\n'
        svg += draw_text(80, yy, text, 13, color, weight=weight)

    # Examples
    svg += draw_card(30, 320, 355, 145, 10)
    svg += draw_section_title(50, 340, "Пример 1")
    svg += draw_text(50, 365, "3x − 6 > 0", 14, DARK_TEXT)
    svg += draw_text(50, 387, "3x > 6", 13, LIGHT_TEXT)
    svg += draw_text(50, 409, "x > 2", 15, SUCCESS, weight="bold")
    # Number line
    svg += f'  <line x1="60" y1="440" x2="340" y2="440" stroke="{PRIMARY_LIGHT}" stroke-width="1.5"/>\n'
    svg += f'  <circle cx="200" cy="440" r="4" fill="{WHITE}" stroke="{ACCENT2}" stroke-width="2"/>\n'
    svg += f'  <line x1="204" y1="440" x2="340" y2="440" stroke="{ACCENT2}" stroke-width="3"/>\n'
    svg += f'  <text x="200" y="455" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="10" fill="{DARK_TEXT}">2</text>\n'

    svg += draw_card(415, 320, 355, 145, 10)
    svg += draw_section_title(435, 340, "Пример 2 (деление на −)")
    svg += draw_text(435, 365, "−2x + 4 ≥ 0", 14, DARK_TEXT)
    svg += draw_text(435, 387, "−2x ≥ −4", 13, LIGHT_TEXT)
    svg += draw_text(435, 409, "x ≤ 2   (знак поменялся!)", 14, "#DC2626", weight="bold")
    # Number line
    svg += f'  <line x1="445" y1="440" x2="725" y2="440" stroke="{PRIMARY_LIGHT}" stroke-width="1.5"/>\n'
    svg += f'  <circle cx="585" cy="440" r="4" fill="{ACCENT2}" stroke="{ACCENT2}" stroke-width="2"/>\n'
    svg += f'  <line x1="445" y1="440" x2="585" y2="440" stroke="{ACCENT2}" stroke-width="3"/>\n'
    svg += f'  <text x="585" y="455" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="10" fill="{DARK_TEXT}">2</text>\n'

    # Interval notation
    svg += draw_card(30, 480, 740, 85, 10)
    svg += draw_section_title(50, 500, "Обозначения на числовой прямой")
    svg += draw_text(50, 523, "○ — строгое неравенство (> , <) — точка не входит", 13, DARK_TEXT)
    svg += draw_text(50, 543, "● — нестрогое неравенство (≥ , ≤) — точка входит", 13, DARK_TEXT)
    svg += draw_text(50, 558, "→ или ← — направление решения (луч)", 13, DARK_TEXT)

    svg += draw_footer()
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 11: Степень с целым показателем
# ============================================================
def generate_lesson11():
    svg = svg_header()
    svg += bg_gradient()
    svg += draw_background()
    svg += draw_header_bar("Степень с целым показателем", "Отрицательные показатели и стандартный вид числа")
    svg += draw_lesson_number(11)
    svg += draw_decorative_dots()
    svg += draw_decorative_math_symbols()

    # Definition for positive exponent
    svg += draw_card(30, 95, 355, 75, 10)
    svg += draw_section_title(50, 115, "Положительный показатель")
    svg += draw_formula_box(50, 132, 330, 32, "aⁿ = a · a · ... · a  (n раз)", 15, 6)

    # Definition for zero exponent
    svg += draw_card(415, 95, 355, 75, 10)
    svg += draw_section_title(435, 115, "Нулевой показатель")
    svg += draw_formula_box(435, 132, 330, 32, "a⁰ = 1   (a ≠ 0)", 18, 6)

    # Negative exponent - MAIN CONCEPT
    svg += draw_card(100, 185, 600, 80, 12)
    svg += f'  <rect x="100" y="185" width="600" height="80" rx="12" fill="{HIGHLIGHT}" opacity="0.25" stroke="{HIGHLIGHT}" stroke-width="1.5"/>\n'
    svg += draw_text(400, 207, "Отрицательный показатель:", 13, PRIMARY, "middle", "bold")
    svg += draw_formula_box(120, 218, 560, 38, "a⁻ⁿ = 1 / aⁿ    (a ≠ 0, n — натуральное)", 20, 8)

    # Examples of negative exponents
    svg += draw_card(30, 280, 355, 130, 10)
    svg += draw_section_title(50, 300, "Примеры")
    svg += draw_text(50, 325, "2⁻³ = 1/2³ = 1/8", 14, DARK_TEXT)
    svg += draw_text(50, 350, "5⁻² = 1/5² = 1/25", 14, DARK_TEXT)
    svg += draw_text(50, 375, "10⁻¹ = 1/10 = 0.1", 14, DARK_TEXT)
    svg += draw_text(50, 400, "(−3)⁻² = 1/9", 14, SUCCESS, weight="bold")

    svg += draw_card(415, 280, 355, 130, 10)
    svg += draw_section_title(435, 300, "Обратное преобразование")
    svg += draw_text(435, 325, "1/7 = 7⁻¹", 14, DARK_TEXT)
    svg += draw_text(435, 350, "1/4² = 4⁻² = 1/16", 14, DARK_TEXT)
    svg += draw_text(435, 375, "1/10³ = 10⁻³ = 0.001", 14, DARK_TEXT)
    svg += draw_text(435, 400, "3/x² = 3x⁻²", 14, SUCCESS, weight="bold")

    # Properties
    svg += draw_card(30, 425, 740, 85, 10)
    svg += draw_section_title(50, 445, "Свойства степеней (для целых n, m)")
    svg += draw_formula_box(50, 462, 230, 20, "aⁿ · aᵐ = aⁿ⁺ᵐ", 14, 6)
    svg += draw_formula_box(290, 462, 230, 20, "aⁿ / aᵐ = aⁿ⁻ᵐ", 14, 6)
    svg += draw_formula_box(530, 462, 230, 20, "(aⁿ)ᵐ = aⁿˣᵐ", 14, 6)
    svg += draw_formula_box(50, 488, 350, 20, "(a·b)ⁿ = aⁿ · bⁿ", 14, 6)
    svg += draw_formula_box(410, 488, 350, 20, "(a/b)ⁿ = aⁿ / bⁿ", 14, 6)

    # Standard form
    svg += draw_card(30, 525, 740, 45, 10)
    svg += draw_section_title(50, 540, "Стандартный вид числа")
    svg += draw_formula_box(230, 535, 380, 28, "a · 10ⁿ, где 1 ≤ |a| < 10", 16, 6)

    svg += draw_footer()
    svg += svg_footer()
    return svg


# ============================================================
# MAIN: Generate all SVGs
# ============================================================
generators = [
    (1, generate_lesson1),
    (2, generate_lesson2),
    (3, generate_lesson3),
    (4, generate_lesson4),
    (5, generate_lesson5),
    (6, generate_lesson6),
    (7, generate_lesson7),
    (8, generate_lesson8),
    (9, generate_lesson9),
    (10, generate_lesson10),
    (11, generate_lesson11),
]

print(f"Generating {len(generators)} SVG files...")
print(f"Output directory: {OUTPUT_DIR}")
print()

success_count = 0
error_count = 0

for lesson_num, gen_func in generators:
    filepath = os.path.join(OUTPUT_DIR, f"lesson-{lesson_num}.svg")
    try:
        svg_content = gen_func()
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        file_size = os.path.getsize(filepath)
        print(f"  ✓ lesson-{lesson_num}.svg ({file_size} bytes)")
        success_count += 1
    except Exception as e:
        print(f"  ✗ lesson-{lesson_num}.svg — ERROR: {e}")
        error_count += 1

print()
print(f"Generation complete: {success_count} succeeded, {error_count} failed")
