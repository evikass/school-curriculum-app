#!/usr/bin/env python3
"""
Generate 9 educational SVG images for Grade 7 Chemistry lessons.
Each SVG is 800x600, Russian text, purple/violet color scheme (#8B5CF6 primary).
Validated with xml.etree.ElementTree.
"""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/chemistry"
WIDTH = 800
HEIGHT = 600

# Color palette
PRIMARY = "#8B5CF6"
PRIMARY_DARK = "#6D28D9"
PRIMARY_LIGHT = "#A78BFA"
PRIMARY_LIGHTER = "#C4B5FD"
PRIMARY_BG = "#EDE9FE"
ACCENT = "#7C3AED"
WHITE = "#FFFFFF"
DARK = "#1E1B4B"
GRAY = "#6B7280"
LIGHT_GRAY = "#F3F4F6"
MID_GRAY = "#9CA3AF"
SOFT_PURPLE = "#DDD6FE"
DEEP_PURPLE = "#4C1D95"
VIOLET_100 = "#EDE9FE"
VIOLET_200 = "#DDD6FE"
VIOLET_300 = "#C4B5FD"
VIOLET_400 = "#A78BFA"
VIOLET_500 = "#8B5CF6"
VIOLET_600 = "#7C3AED"
VIOLET_700 = "#6D28D9"
VIOLET_800 = "#5B21B6"
VIOLET_900 = "#4C1D95"
METAL_COLOR = "#C0C0C0"
NONMETAL_COLOR = "#FDE68A"
NOBLE_COLOR = "#A5F3FC"
BLUE = "#3B82F6"
RED = "#EF4444"
GREEN = "#10B981"
ORANGE = "#F59E0B"
YELLOW = "#FCD34D"
CYAN = "#06B6D4"
PINK = "#EC4899"


def escape_xml(text):
    """Escape special XML characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def svg_header():
    """Return standard SVG header elements."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">'''


def svg_background():
    """Return background gradient and base rectangle."""
    return f'''
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{VIOLET_900};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{VIOLET_700};stop-opacity:1" />
    </linearGradient>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:{VIOLET_600};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{VIOLET_500};stop-opacity:1" />
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:rgba(255,255,255,0.15);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgba(255,255,255,0.05);stop-opacity:1" />
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="shadow">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="rgba(0,0,0,0.3)"/>
    </filter>
  </defs>
  <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bgGrad)"/>
  <!-- Decorative circles -->
  <circle cx="50" cy="50" r="120" fill="{VIOLET_800}" opacity="0.3"/>
  <circle cx="750" cy="550" r="100" fill="{VIOLET_800}" opacity="0.3"/>
  <circle cx="700" cy="80" r="60" fill="{VIOLET_600}" opacity="0.2"/>
  <circle cx="100" cy="520" r="80" fill="{VIOLET_600}" opacity="0.2"/>
'''


def title_bar(title, subtitle="", lesson_num=1):
    """Return title bar with lesson number and title."""
    return f'''
  <!-- Title bar -->
  <rect x="0" y="0" width="{WIDTH}" height="70" fill="url(#headerGrad)" rx="0"/>
  <rect x="0" y="68" width="{WIDTH}" height="3" fill="{VIOLET_400}" opacity="0.6"/>
  <text x="80" y="44" font-family="Arial, sans-serif" font-size="13" fill="{VIOLET_300}" font-weight="bold">УРОК {lesson_num}</text>
  <text x="160" y="44" font-family="Arial, sans-serif" font-size="20" fill="{WHITE}" font-weight="bold">{escape_xml(title)}</text>
  {f'<text x="160" y="60" font-family="Arial, sans-serif" font-size="12" fill="{VIOLET_300}">{escape_xml(subtitle)}</text>' if subtitle else ''}
  <!-- Lesson number circle -->
  <circle cx="40" cy="35" r="25" fill="{VIOLET_800}" stroke="{VIOLET_400}" stroke-width="2"/>
  <text x="40" y="41" font-family="Arial, sans-serif" font-size="20" fill="{WHITE}" font-weight="bold" text-anchor="middle">{lesson_num}</text>
'''


def card(x, y, w, h, rx=12):
    """Return a semi-transparent card rectangle."""
    return f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="rgba(255,255,255,0.1)" stroke="{VIOLET_500}" stroke-width="1" stroke-opacity="0.3"/>\n'


def text_element(x, y, text, size=14, color=WHITE, anchor="start", weight="normal", family="Arial, sans-serif"):
    """Return a text element with XML-escaped content."""
    return f'  <text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{escape_xml(text)}</text>\n'


def footer():
    """Return footer bar."""
    return f'''
  <rect x="0" y="575" width="{WIDTH}" height="25" fill="rgba(0,0,0,0.2)"/>
  <text x="400" y="592" font-family="Arial, sans-serif" font-size="11" fill="{VIOLET_400}" text-anchor="middle">Химия • 7 класс • ИнеШкола</text>
'''


def atom_model(cx, cy, r_nucleus=12, r_orbit=30, electrons=3, nucleus_color=PRIMARY, electron_color=CYAN):
    """Draw a simplified atom model with electron orbits and electrons."""
    parts = []
    # Nucleus
    parts.append(f'  <circle cx="{cx}" cy="{cy}" r="{r_nucleus}" fill="{nucleus_color}" filter="url(#glow)"/>')
    parts.append(f'  <circle cx="{cx}" cy="{cy}" r="{r_nucleus-3}" fill="{nucleus_color}" opacity="0.6"/>')
    # Orbits
    for i in range(min(electrons, 3)):
        angle = i * 60
        parts.append(f'  <ellipse cx="{cx}" cy="{cy}" rx="{r_orbit}" ry="{r_orbit*0.4}" fill="none" stroke="{VIOLET_400}" stroke-width="1" opacity="0.5" transform="rotate({angle},{cx},{cy})"/>')
    # Electrons on orbits
    for i in range(electrons):
        orbit_idx = i % 3
        angle = (i * 120 + orbit_idx * 60) * 3.14159 / 180
        orbit_angle = orbit_idx * 60
        ea = angle + orbit_angle * 3.14159 / 180
        ex = cx + r_orbit * (0.7 + 0.3 * (i % 2)) * ((-1)**i)
        ey = cy + r_orbit * 0.3 * ((-1)**(i+1))
        # Position electrons at cardinal points on orbits
        if i == 0:
            ex, ey = cx + r_orbit, cy
        elif i == 1:
            ex, ey = cx - r_orbit * 0.5, cy - r_orbit * 0.7
        elif i == 2:
            ex, ey = cx - r_orbit * 0.5, cy + r_orbit * 0.7
        elif i == 3:
            ex, ey = cx, cy - r_orbit
        elif i == 4:
            ex, ey = cx, cy + r_orbit
        else:
            ex, ey = cx + r_orbit * 0.7, cy + r_orbit * 0.5
        parts.append(f'  <circle cx="{ex:.1f}" cy="{ey:.1f}" r="5" fill="{electron_color}" filter="url(#glow)"/>')
    return '\n'.join(parts)


def generate_lesson1():
    """Lesson 1: Периодический закон Д.И. Менделеева"""
    svg = svg_header()
    svg += svg_background()
    svg += title_bar("Периодический закон Д.И. Менделеева", "Основы периодической системы элементов", 1)

    # Main content area
    # Left side: Mendeleev info card
    svg += card(20, 85, 370, 230)
    svg += text_element(35, 110, "Дмитрий Иванович Менделеев", 16, VIOLET_300, weight="bold")
    svg += text_element(35, 130, "1869 год — открытие периодического закона", 12, VIOLET_200)

    svg += text_element(35, 160, "Формулировка закона:", 13, VIOLET_400, weight="bold")
    svg += text_element(35, 180, "Свойства химических элементов", 12, WHITE)
    svg += text_element(35, 196, "и их соединений находятся в", 12, WHITE)
    svg += text_element(35, 212, "периодической зависимости", 12, WHITE)
    svg += text_element(35, 228, "от величины атомных масс.", 12, WHITE)

    svg += text_element(35, 258, "Современная формулировка:", 13, VIOLET_400, weight="bold")
    svg += text_element(35, 278, "Свойства элементов находятся в", 12, WHITE)
    svg += text_element(35, 294, "периодической зависимости от", 12, WHITE)
    svg += text_element(35, 310, "заряда атомного ядра (Z).", 12, WHITE)

    # Right side: Mini periodic table fragment
    svg += card(410, 85, 370, 230)
    svg += text_element(595, 108, "Фрагмент таблицы Менделеева", 13, VIOLET_400, weight="bold", anchor="middle")

    # Draw a mini periodic table (first 3 periods)
    elements = [
        (0,0,"H","1",VIOLET_400), (17,0,"He","2",CYAN),
        (0,1,"Li","3",ORANGE), (1,1,"Be","4",ORANGE), (12,1,"B","5",YELLOW), (13,1,"C","6",YELLOW),
        (14,1,"N","7",YELLOW), (15,1,"O","8",YELLOW), (16,1,"F","9",YELLOW), (17,1,"Ne","10",CYAN),
        (0,2,"Na","11",ORANGE), (1,2,"Mg","12",ORANGE), (12,2,"Al","13",YELLOW), (13,2,"Si","14",YELLOW),
        (14,2,"P","15",YELLOW), (15,2,"S","16",YELLOW), (16,2,"Cl","17",YELLOW), (17,2,"Ar","18",CYAN),
    ]
    cell_w = 18
    cell_h = 20
    table_x = 425
    table_y = 118
    for (col, row, sym, num, clr) in elements:
        cx = table_x + col * cell_w
        cy = table_y + row * cell_h
        svg += f'  <rect x="{cx}" y="{cy}" width="{cell_w-1}" height="{cell_h-1}" rx="2" fill="{clr}" opacity="0.3" stroke="{clr}" stroke-width="0.5"/>\n'
        svg += text_element(cx + cell_w/2, cy + 8, num, 7, VIOLET_200, anchor="middle")
        svg += text_element(cx + cell_w/2, cy + 17, sym, 9, WHITE, anchor="middle", weight="bold")

    # Legend for table
    svg += text_element(425, 198, "Условные обозначения:", 11, VIOLET_400, weight="bold")
    svg += f'  <rect x="425" y="206" width="12" height="12" rx="2" fill="{ORANGE}" opacity="0.4"/>\n'
    svg += text_element(442, 216, "— Металлы", 11, VIOLET_200)
    svg += f'  <rect x="510" y="206" width="12" height="12" rx="2" fill="{YELLOW}" opacity="0.4"/>\n'
    svg += text_element(527, 216, "— Неметаллы", 11, VIOLET_200)
    svg += f'  <rect x="610" y="206" width="12" height="12" rx="2" fill="{CYAN}" opacity="0.4"/>\n'
    svg += text_element(627, 216, "— Благородные газы", 11, VIOLET_200)

    # Key concept
    svg += text_element(425, 248, "Закономерности:", 12, VIOLET_400, weight="bold")
    svg += text_element(425, 268, "• В периоде: слева направо", 11, WHITE)
    svg += text_element(435, 284, "металлич. свойства убывают", 11, VIOLET_300)
    svg += text_element(425, 304, "• В группе: сверху вниз", 11, WHITE)
    svg += text_element(435, 320, "металлич. свойства возрастают", 11, VIOLET_300)

    # Bottom left: Atom model
    svg += card(20, 330, 250, 230)
    svg += text_element(145, 355, "Модель атома", 14, VIOLET_400, weight="bold", anchor="middle")
    svg += atom_model(145, 455, 15, 50, 3, PRIMARY, CYAN)
    svg += text_element(145, 520, "Z — заряд ядра", 12, VIOLET_300, anchor="middle")
    svg += text_element(145, 538, "e\u207B — электроны", 12, VIOLET_300, anchor="middle")

    # Bottom middle: Periodicity visualization
    svg += card(290, 330, 250, 230)
    svg += text_element(415, 355, "Периодичность свойств", 14, VIOLET_400, weight="bold", anchor="middle")

    # Draw wave pattern showing periodicity
    wave_y = 440
    svg += f'  <line x1="310" y1="{wave_y}" x2="520" y2="{wave_y}" stroke="{VIOLET_500}" stroke-width="1" opacity="0.3"/>\n'
    points = []
    for i in range(22):
        x = 310 + i * 10
        y = wave_y - 40 * (1 if (i % 7 < 3) else -1) * ((i % 7) / 3.0 if (i % 7) < 3 else (7 - i % 7) / 4.0)
        points.append(f"{x:.0f},{y:.0f}")
    svg += f'  <polyline points="{" ".join(points)}" fill="none" stroke="{VIOLET_400}" stroke-width="2"/>\n'

    svg += text_element(415, 500, "Свойства повторяются", 11, VIOLET_300, anchor="middle")
    svg += text_element(415, 516, "через определённые промежутки", 11, VIOLET_300, anchor="middle")
    svg += text_element(415, 540, "Z = 1, 2, 3 ... 118", 13, WHITE, anchor="middle", weight="bold")

    # Bottom right: Key formulas
    svg += card(560, 330, 220, 230)
    svg += text_element(670, 355, "Ключевые формулы", 14, VIOLET_400, weight="bold", anchor="middle")

    svg += text_element(580, 390, "Заряд ядра:", 12, VIOLET_300)
    svg += text_element(580, 412, "Z = число протонов", 14, WHITE, weight="bold")
    svg += text_element(580, 432, "   = порядковый номер", 12, VIOLET_200)

    svg += text_element(580, 462, "Массовое число:", 12, VIOLET_300)
    svg += text_element(580, 484, "A = Z + N", 16, WHITE, weight="bold")
    svg += text_element(580, 504, "N — число нейтронов", 12, VIOLET_200)

    svg += text_element(580, 534, "Число электронов", 12, VIOLET_300)
    svg += text_element(580, 552, "= Z (для атома)", 14, WHITE, weight="bold")

    svg += footer()
    svg += '</svg>'
    return svg


def generate_lesson2():
    """Lesson 2: Структура периодической системы"""
    svg = svg_header()
    svg += svg_background()
    svg += title_bar("Структура периодической системы", "Периоды, группы, семейства", 2)

    # Left: Period table structure
    svg += card(20, 85, 380, 300)
    svg += text_element(210, 110, "Структура таблицы", 15, VIOLET_400, weight="bold", anchor="middle")

    # Draw schematic periodic table
    # 7 periods on left
    svg += text_element(35, 140, "Периоды (7)", 13, VIOLET_400, weight="bold")
    period_labels = ["I", "II", "III", "IV", "V", "VI", "VII"]
    for i, label in enumerate(period_labels):
        y = 155 + i * 28
        svg += f'  <rect x="35" y="{y}" width="55" height="24" rx="4" fill="{VIOLET_700}" stroke="{VIOLET_500}" stroke-width="1"/>\n'
        svg += text_element(62, y + 17, label, 12, WHITE, anchor="middle", weight="bold")
        # Show number of elements
        if i < 3:
            count = ["2","8","8"][i]
            svg += text_element(100, y + 17, f"— малый ({count} элем.)", 11, VIOLET_200)
        else:
            count = ["18","18","32","32"][i-3]
            svg += text_element(100, y + 17, f"— большой ({count} элем.)", 11, VIOLET_200)

    # Right: Groups
    svg += card(410, 85, 370, 300)
    svg += text_element(595, 110, "Группы (18)", 15, VIOLET_400, weight="bold", anchor="middle")

    svg += text_element(425, 140, "Главная подгруппа (A)", 13, VIOLET_300, weight="bold")
    svg += text_element(435, 158, "Содержит элементы больших", 11, WHITE)
    svg += text_element(435, 174, "и малых периодов", 11, WHITE)

    svg += text_element(425, 200, "Побочная подгруппа (B)", 13, VIOLET_300, weight="bold")
    svg += text_element(435, 218, "Только элементы больших", 11, WHITE)
    svg += text_element(435, 234, "периодов (d-элементы)", 11, WHITE)

    # Chemical families
    svg += text_element(425, 265, "Семейства элементов:", 13, VIOLET_400, weight="bold")

    families = [
        ("Щёлочные металлы", "IA группа: Li, Na, K, Rb, Cs", ORANGE),
        ("Щёлочноземельные", "IIA группа: Be, Mg, Ca, Sr, Ba", ORANGE),
        ("Галогены", "VIIA группа: F, Cl, Br, I", YELLOW),
        ("Благородные газы", "VIIIA группа: He, Ne, Ar, Kr", CYAN),
    ]
    for i, (name, desc, clr) in enumerate(families):
        y = 283 + i * 25
        svg += f'  <rect x="425" y="{y-5}" width="8" height="8" rx="2" fill="{clr}"/>\n'
        svg += text_element(438, y + 3, name, 11, clr, weight="bold")
        svg += text_element(438, y + 16, desc, 10, VIOLET_200)

    # Bottom: Detailed period/group diagram
    svg += card(20, 400, 760, 165)
    svg += text_element(400, 425, "Схема: Периоды и Группы", 14, VIOLET_400, weight="bold", anchor="middle")

    # Draw grid representing periodic table
    grid_x = 60
    grid_y = 440
    cell_w = 36
    cell_h = 22
    # Columns = groups
    for g in range(8):
        gx = grid_x + g * cell_w
        svg += f'  <rect x="{gx}" y="{grid_y}" width="{cell_w-1}" height="{cell_h-1}" rx="2" fill="{VIOLET_700}" stroke="{VIOLET_500}" stroke-width="0.5"/>\n'
        svg += text_element(gx + cell_w/2, grid_y + 15, f"{g+1}", 9, WHITE, anchor="middle", weight="bold")

    svg += text_element(45, grid_y + 16, "Гр.", 8, VIOLET_300, anchor="end")

    # Rows = periods with sample elements
    sample_elements = [
        ["H","","","","","","","He"],
        ["Li","Be","","B","C","N","O","Ne"],
        ["Na","Mg","","Al","Si","P","S","Ar"],
    ]
    for p in range(3):
        ry = grid_y + (p + 1) * cell_h
        svg += text_element(45, ry + 15, f"P{p+1}", 8, VIOLET_300, anchor="end")
        for g in range(8):
            gx = grid_x + g * cell_w
            elem = sample_elements[p][g] if g < len(sample_elements[p]) else ""
            fill = VIOLET_800 if elem else "rgba(255,255,255,0.03)"
            svg += f'  <rect x="{gx}" y="{ry}" width="{cell_w-1}" height="{cell_h-1}" rx="2" fill="{fill}" stroke="{VIOLET_600}" stroke-width="0.5"/>\n'
            if elem:
                svg += text_element(gx + cell_w/2, ry + 15, elem, 10, WHITE, anchor="middle", weight="bold")

    # Period number arrow
    svg += text_element(grid_x + 8 * cell_w + 15, grid_y + 20, "Периоды", 11, VIOLET_300)
    svg += f'  <line x1="{grid_x + 8*cell_w + 10}" y1="{grid_y+25}" x2="{grid_x + 8*cell_w + 10}" y2="{grid_y + 4*cell_h - 5}" stroke="{VIOLET_400}" stroke-width="1.5" marker-end="url(#arrow)"/>\n'

    # Group number arrow
    svg += text_element(grid_x + 2 * cell_w, grid_y + 5 * cell_h + 10, "Группы", 11, VIOLET_300)
    svg += f'  <line x1="{grid_x}" y1="{grid_y + 5*cell_h + 5}" x2="{grid_x + 8*cell_w - 5}" y2="{grid_y + 5*cell_h + 5}" stroke="{VIOLET_400}" stroke-width="1.5"/>\n'
    # Arrow heads (simple triangles)
    svg += f'  <polygon points="{grid_x + 8*cell_w - 5},{grid_y + 5*cell_h + 5} {grid_x + 8*cell_w - 12},{grid_y + 5*cell_h + 1} {grid_x + 8*cell_w - 12},{grid_y + 5*cell_h + 9}" fill="{VIOLET_400}"/>\n'
    svg += f'  <polygon points="{grid_x + 8*cell_w + 10},{grid_y + 4*cell_h - 5} {grid_x + 8*cell_w + 6},{grid_y + 4*cell_h - 12} {grid_x + 8*cell_w + 14},{grid_y + 4*cell_h - 12}" fill="{VIOLET_400}"/>\n'

    # Key info
    svg += text_element(grid_x + 8 * cell_w + 15, grid_y + 55, "↓ Свойства", 10, VIOLET_300)
    svg += text_element(grid_x + 8 * cell_w + 15, grid_y + 68, "меняются в периоде", 10, VIOLET_200)

    svg += text_element(grid_x + 8 * cell_w + 15, grid_y + 88, "→ Свойства", 10, VIOLET_300)
    svg += text_element(grid_x + 8 * cell_w + 15, grid_y + 101, "сходны в группе", 10, VIOLET_200)

    svg += footer()
    svg += '</svg>'
    return svg


def generate_lesson3():
    """Lesson 3: Металлы и неметаллы"""
    svg = svg_header()
    svg += svg_background()
    svg += title_bar("Металлы и неметаллы", "Сравнение свойств и положение в таблице", 3)

    # Left: Metals
    svg += card(20, 85, 370, 280)
    svg += f'  <rect x="25" y="90" width="360" height="30" rx="6" fill="{ORANGE}" opacity="0.3"/>\n'
    svg += text_element(205, 110, "МЕТАЛЛЫ", 18, ORANGE, anchor="middle", weight="bold")

    # Metal atom model
    svg += atom_model(90, 175, 12, 35, 2, ORANGE, CYAN)
    svg += text_element(90, 215, "Металлический атом", 10, VIOLET_200, anchor="middle")
    svg += text_element(90, 228, "1-3 e\u207B на внешнем уровне", 10, VIOLET_300, anchor="middle")

    # Metal properties
    props_m = [
        "• Твёрдые (кроме Hg)",
        "• Металлический блеск",
        "• Пластичные, ковкие",
        "• Хорошо проводят тепло",
        "• Хорошо проводят ток",
        "• Отдают электроны (восстанов.)",
    ]
    for i, p in enumerate(props_m):
        svg += text_element(160, 150 + i * 20, p, 12, WHITE)

    # Metal examples
    svg += text_element(40, 290, "Примеры:", 12, ORANGE, weight="bold")
    metal_examples = [("Na", 11), ("Mg", 12), ("Fe", 26), ("Cu", 29), ("Al", 13)]
    for i, (sym, num) in enumerate(metal_examples):
        mx = 110 + i * 55
        svg += f'  <rect x="{mx}" y="278" width="45" height="40" rx="6" fill="{ORANGE}" opacity="0.2" stroke="{ORANGE}" stroke-width="1"/>\n'
        svg += text_element(mx + 22, 294, sym, 14, ORANGE, anchor="middle", weight="bold")
        svg += text_element(mx + 22, 312, f"Z={num}", 9, VIOLET_300, anchor="middle")

    # Right: Nonmetals
    svg += card(410, 85, 370, 280)
    svg += f'  <rect x="415" y="90" width="360" height="30" rx="6" fill="{YELLOW}" opacity="0.3"/>\n'
    svg += text_element(595, 110, "НЕМЕТАЛЛЫ", 18, YELLOW, anchor="middle", weight="bold")

    # Nonmetal atom model
    svg += atom_model(480, 175, 12, 35, 6, YELLOW, PINK)
    svg += text_element(480, 215, "Неметаллический атом", 10, VIOLET_200, anchor="middle")
    svg += text_element(480, 228, "4-8 e\u207B на внешнем уровне", 10, VIOLET_300, anchor="middle")

    # Nonmetal properties
    props_n = [
        "• Разные агрег. состояния",
        "• Без блеска",
        "• Хрупкие (твёрдые)",
        "• Плохо проводят тепло",
        "• Не проводят ток (кроме C)",
        "• Принимают электроны (окисл.)",
    ]
    for i, p in enumerate(props_n):
        svg += text_element(550, 150 + i * 20, p, 12, WHITE)

    # Nonmetal examples
    svg += text_element(430, 290, "Примеры:", 12, YELLOW, weight="bold")
    nonmetal_examples = [("C", 6), ("N", 7), ("O", 8), ("F", 9), ("Cl", 17)]
    for i, (sym, num) in enumerate(nonmetal_examples):
        mx = 500 + i * 55
        svg += f'  <rect x="{mx}" y="278" width="45" height="40" rx="6" fill="{YELLOW}" opacity="0.2" stroke="{YELLOW}" stroke-width="1"/>\n'
        svg += text_element(mx + 22, 294, sym, 14, YELLOW, anchor="middle", weight="bold")
        svg += text_element(mx + 22, 312, f"Z={num}", 9, VIOLET_300, anchor="middle")

    # Bottom: Position in table diagram
    svg += card(20, 380, 760, 185)
    svg += text_element(400, 405, "Положение в периодической системе", 14, VIOLET_400, weight="bold", anchor="middle")

    # Diagonal line showing metal/nonmetal boundary
    table_x = 50
    table_y = 425
    cell_w = 38
    cell_h = 18

    # Draw simplified table rows
    for p in range(4):
        for g in range(18):
            gx = table_x + g * cell_w
            gy = table_y + p * cell_h
            # Determine if metal or nonmetal
            is_metal = g < 12
            clr = ORANGE if is_metal else YELLOW
            if g >= 17:
                clr = CYAN  # noble gases
            svg += f'  <rect x="{gx}" y="{gy}" width="{cell_w-1}" height="{cell_h-1}" rx="1" fill="{clr}" opacity="0.15" stroke="{VIOLET_600}" stroke-width="0.3"/>\n'

    # Labels
    svg += text_element(50, 505, "← Металлы", 12, ORANGE, weight="bold")
    svg += text_element(400, 505, "Неметаллы →", 12, YELLOW, weight="bold")
    svg += text_element(680, 505, "Благородные", 12, CYAN, weight="bold")

    # Diagonal line
    svg += f'  <line x1="{table_x + 12*cell_w}" y1="{table_y}" x2="{table_x + 16*cell_w}" y2="{table_y + 4*cell_h}" stroke="{WHITE}" stroke-width="2" stroke-dasharray="4,2" opacity="0.7"/>\n'
    svg += text_element(table_x + 15 * cell_w, table_y - 5, "Граница", 10, WHITE, anchor="middle")

    # Summary
    svg += text_element(400, 540, "В периоде слева направо: металлические свойства убывают, неметаллические возрастают", 11, VIOLET_200, anchor="middle")
    svg += text_element(400, 556, "В группе сверху вниз: металлические свойства возрастают, неметаллические убывают", 11, VIOLET_200, anchor="middle")

    svg += footer()
    svg += '</svg>'
    return svg


def generate_lesson4():
    """Lesson 4: Типы химической связи"""
    svg = svg_header()
    svg += svg_background()
    svg += title_bar("Типы химической связи", "Ионная, ковалентная, металлическая", 4)

    # Three cards for three bond types
    card_w = 240
    card_h = 280

    # Card 1: Ionic bond
    x1 = 15
    svg += card(x1, 85, card_w, card_h)
    svg += f'  <rect x="{x1+5}" y="90" width="{card_w-10}" height="28" rx="6" fill="{BLUE}" opacity="0.3"/>\n'
    svg += text_element(x1 + card_w/2, 109, "ИОННАЯ СВЯЗЬ", 15, BLUE, anchor="middle", weight="bold")

    # Ionic bond diagram: Na + Cl -> Na+ Cl-
    # Na atom
    svg += f'  <circle cx="{x1+55}" cy="165" r="25" fill="{ORANGE}" opacity="0.4" stroke="{ORANGE}" stroke-width="1.5"/>\n'
    svg += text_element(x1+55, 170, "Na", 14, WHITE, anchor="middle", weight="bold")

    # Arrow
    svg += f'  <line x1="{x1+85}" y1="165" x2="{x1+120}" y2="165" stroke="{VIOLET_400}" stroke-width="2"/>\n'
    svg += f'  <polygon points="{x1+120},165 {x1+113},161 {x1+113},169" fill="{VIOLET_400}"/>\n'
    svg += text_element(x1+103, 158, "e\u207B", 10, CYAN, anchor="middle")

    # Cl atom
    svg += f'  <circle cx="{x1+155}" cy="165" r="28" fill="{YELLOW}" opacity="0.4" stroke="{YELLOW}" stroke-width="1.5"/>\n'
    svg += text_element(x1+155, 170, "Cl", 14, WHITE, anchor="middle", weight="bold")

    # Result: Na+ ... Cl-
    svg += text_element(x1 + card_w/2, 215, "Na\u207A  ···  Cl\u207B", 16, WHITE, anchor="middle", weight="bold")

    svg += text_element(x1+15, 240, "Между металлом и", 11, VIOLET_200)
    svg += text_element(x1+15, 255, "неметаллом", 11, VIOLET_200)
    svg += text_element(x1+15, 280, "Примеры: NaCl, CaO,", 10, WHITE)
    svg += text_element(x1+15, 295, "KBr, MgCl\u2082", 10, WHITE)
    svg += text_element(x1+15, 320, "Передача электронов", 11, BLUE, weight="bold")
    svg += text_element(x1+15, 335, "от металла к неметаллу", 10, VIOLET_300)

    # Card 2: Covalent bond
    x2 = 275
    svg += card(x2, 85, card_w, card_h)
    svg += f'  <rect x="{x2+5}" y="90" width="{card_w-10}" height="28" rx="6" fill="{GREEN}" opacity="0.3"/>\n'
    svg += text_element(x2 + card_w/2, 109, "КОВАЛЕНТНАЯ", 15, GREEN, anchor="middle", weight="bold")

    # Covalent bond diagram: H + H -> H-H
    svg += f'  <circle cx="{x2+45}" cy="165" r="20" fill="{YELLOW}" opacity="0.4" stroke="{YELLOW}" stroke-width="1.5"/>\n'
    svg += text_element(x2+45, 170, "H", 14, WHITE, anchor="middle", weight="bold")
    # Shared electron pair
    svg += f'  <circle cx="{x2+70}" cy="158" r="4" fill="{CYAN}" opacity="0.8"/>\n'
    svg += f'  <circle cx="{x2+70}" cy="172" r="4" fill="{CYAN}" opacity="0.8"/>\n'
    svg += f'  <circle cx="{x2+95}" cy="165" r="20" fill="{YELLOW}" opacity="0.4" stroke="{YELLOW}" stroke-width="1.5"/>\n'
    svg += text_element(x2+95, 170, "H", 14, WHITE, anchor="middle", weight="bold")

    svg += text_element(x2 + card_w/2, 215, "H — H", 16, WHITE, anchor="middle", weight="bold")

    # Subtypes
    svg += text_element(x2+15, 240, "Неполярная:", 11, GREEN, weight="bold")
    svg += text_element(x2+15, 255, "Одинаковые атомы (H\u2082, O\u2082, N\u2082)", 10, WHITE)
    svg += text_element(x2+15, 275, "Полярная:", 11, GREEN, weight="bold")
    svg += text_element(x2+15, 290, "Разные неметаллы (HCl, H\u2082O)", 10, WHITE)
    svg += text_element(x2+15, 315, "Общий электронный пар", 11, GREEN, weight="bold")
    svg += text_element(x2+15, 330, "(или общая пара)", 10, VIOLET_300)

    # Card 3: Metallic bond
    x3 = 535
    svg += card(x3, 85, card_w, card_h)
    svg += f'  <rect x="{x3+5}" y="90" width="{card_w-10}" height="28" rx="6" fill="{ORANGE}" opacity="0.3"/>\n'
    svg += text_element(x3 + card_w/2, 109, "МЕТАЛЛИЧЕСКАЯ", 15, ORANGE, anchor="middle", weight="bold")

    # Metallic bond diagram: metal ions in electron cloud
    positions = [(x3+70, 155), (x3+130, 155), (x3+100, 195), (x3+160, 195), (x3+70, 195)]
    # Electron cloud
    svg += f'  <rect x="{x3+55}" y="145" width="120" height="65" rx="10" fill="{CYAN}" opacity="0.1" stroke="{CYAN}" stroke-width="0.5" stroke-dasharray="3,2"/>\n'
    for (px, py) in positions:
        svg += f'  <circle cx="{px}" cy="{py}" r="12" fill="{ORANGE}" opacity="0.5" stroke="{ORANGE}" stroke-width="1"/>\n'
        svg += text_element(px, py+4, "+", 10, WHITE, anchor="middle", weight="bold")
    # Free electrons
    e_positions = [(x3+85, 165), (x3+115, 175), (x3+145, 165), (x3+90, 195), (x3+140, 200)]
    for (ex, ey) in e_positions:
        svg += f'  <circle cx="{ex}" cy="{ey}" r="3" fill="{CYAN}"/>\n'

    svg += text_element(x3 + card_w/2, 235, "Me\u207A + e\u207B (свободные)", 13, WHITE, anchor="middle", weight="bold")

    svg += text_element(x3+15, 260, "Между атомами металлов", 11, VIOLET_200)
    svg += text_element(x3+15, 280, "Атомы в решётке +", 10, WHITE)
    svg += text_element(x3+15, 295, "электронный газ", 10, WHITE)
    svg += text_element(x3+15, 320, "Общие электроны для", 11, ORANGE, weight="bold")
    svg += text_element(x3+15, 335, "всех атомов металла", 10, VIOLET_300)

    # Bottom: Comparison table
    svg += card(20, 380, 760, 185)
    svg += text_element(400, 405, "Сравнение типов химической связи", 14, VIOLET_400, weight="bold", anchor="middle")

    # Table header
    headers = ["Свойство", "Ионная", "Ковалентная", "Металлическая"]
    col_x = [40, 220, 400, 600]
    for i, h in enumerate(headers):
        svg += f'  <rect x="{col_x[i]-5}" y="418" width="{170 if i>0 else 170}" height="22" rx="3" fill="{VIOLET_700}"/>\n'
        svg += text_element(col_x[i] + 80, 434, h, 12, WHITE, anchor="middle", weight="bold")

    rows = [
        ["Между кем", "Металл + Неметалл", "Неметалл + Неметалл", "Металл + Металл"],
        ["Механизм", "Передача e\u207B", "Общий e\u207B-пара", "Общий e\u207B-газ"],
        ["Примеры", "NaCl, CaO", "H\u2082O, CO\u2082, Cl\u2082", "Fe, Cu, Au"],
        ["Прочность", "Высокая", "Разная", "Разная"],
    ]
    for ri, row in enumerate(rows):
        y = 448 + ri * 25
        bg = VIOLET_800 if ri % 2 == 0 else "rgba(255,255,255,0.05)"
        for ci, cell in enumerate(row):
            svg += f'  <rect x="{col_x[ci]-5}" y="{y-3}" width="170" height="22" rx="2" fill="{bg}" opacity="0.5"/>\n'
            color = WHITE if ci > 0 else VIOLET_300
            svg += text_element(col_x[ci] + 80, y + 12, cell, 11, color, anchor="middle")

    svg += footer()
    svg += '</svg>'
    return svg


def generate_lesson5():
    """Lesson 5: Типы химических реакций"""
    svg = svg_header()
    svg += svg_background()
    svg += title_bar("Типы химических реакций", "Соединение, разложение, замещение, обмен", 5)

    # Four reaction type cards
    card_w = 375
    card_h = 155

    # Card 1: Combination (Соединение)
    x1, y1 = 20, 85
    svg += card(x1, y1, card_w, card_h)
    svg += f'  <rect x="{x1+5}" y="{y1+5}" width="180" height="24" rx="6" fill="{BLUE}" opacity="0.3"/>\n'
    svg += text_element(x1+95, y1+22, "РЕАКЦИЯ СОЕДИНЕНИЯ", 13, BLUE, anchor="middle", weight="bold")
    svg += text_element(x1+15, y1+48, "A + B = AB", 18, WHITE, weight="bold")
    svg += text_element(x1+15, y1+72, "Два и более вещества → одно сложное", 11, VIOLET_200)
    svg += text_element(x1+15, y1+95, "Примеры:", 11, BLUE, weight="bold")
    svg += text_element(x1+15, y1+112, "2Mg + O\u2082 = 2MgO", 14, WHITE, weight="bold")
    svg += text_element(x1+15, y1+132, "4Al + 3O\u2082 = 2Al\u2082O\u2083", 14, WHITE, weight="bold")
    # Visual: two circles combining
    svg += f'  <circle cx="{x1+300}" cy="{y1+60}" r="22" fill="{ORANGE}" opacity="0.4" stroke="{ORANGE}" stroke-width="1.5"/>\n'
    svg += f'  <circle cx="{x1+340}" cy="{y1+60}" r="18" fill="{YELLOW}" opacity="0.4" stroke="{YELLOW}" stroke-width="1.5"/>\n'
    svg += f'  <text x="{x1+320}" y="{y1+48}" font-family="Arial" font-size="10" fill="{WHITE}">+</text>\n'
    svg += f'  <line x1="{x1+320}" y1="{y1+85}" x2="{x1+320}" y2="{y1+100}" stroke="{VIOLET_400}" stroke-width="1.5"/>\n'
    svg += f'  <polygon points="{x1+320},{y1+100} {x1+316},{y1+93} {x1+324},{y1+93}" fill="{VIOLET_400}"/>\n'
    svg += f'  <circle cx="{x1+320}" cy="{y1+120}" r="28" fill="{VIOLET_500}" opacity="0.4" stroke="{VIOLET_400}" stroke-width="1.5"/>\n'

    # Card 2: Decomposition (Разложение)
    x2, y2 = 405, 85
    svg += card(x2, y2, card_w, card_h)
    svg += f'  <rect x="{x2+5}" y="{y2+5}" width="180" height="24" rx="6" fill="{RED}" opacity="0.3"/>\n'
    svg += text_element(x2+95, y2+22, "РЕАКЦИЯ РАЗЛОЖЕНИЯ", 13, RED, anchor="middle", weight="bold")
    svg += text_element(x2+15, y2+48, "AB = A + B", 18, WHITE, weight="bold")
    svg += text_element(x2+15, y2+72, "Одно сложное → два и более простых", 11, VIOLET_200)
    svg += text_element(x2+15, y2+95, "Примеры:", 11, RED, weight="bold")
    svg += text_element(x2+15, y2+112, "2H\u2082O = 2H\u2082 + O\u2082", 14, WHITE, weight="bold")
    svg += text_element(x2+15, y2+132, "CaCO\u2083 = CaO + CO\u2082", 14, WHITE, weight="bold")
    # Visual: one circle splitting
    svg += f'  <circle cx="{x2+320}" cy="{y2+60}" r="28" fill="{VIOLET_500}" opacity="0.4" stroke="{VIOLET_400}" stroke-width="1.5"/>\n'
    svg += f'  <line x1="{x2+320}" y1="{y2+92}" x2="{x2+320}" y2="{y2+105}" stroke="{VIOLET_400}" stroke-width="1.5"/>\n'
    svg += f'  <polygon points="{x2+320},{y2+105} {x2+316},{y2+98} {x2+324},{y2+98}" fill="{VIOLET_400}"/>\n'
    svg += f'  <circle cx="{x2+300}" cy="{y2+125}" r="18" fill="{YELLOW}" opacity="0.4" stroke="{YELLOW}" stroke-width="1.5"/>\n'
    svg += f'  <circle cx="{x2+340}" cy="{y2+125}" r="22" fill="{ORANGE}" opacity="0.4" stroke="{ORANGE}" stroke-width="1.5"/>\n'

    # Card 3: Single replacement (Замещение)
    x3, y3 = 20, 255
    svg += card(x3, y3, card_w, card_h)
    svg += f'  <rect x="{x3+5}" y="{y3+5}" width="220" height="24" rx="6" fill="{GREEN}" opacity="0.3"/>\n'
    svg += text_element(x3+115, y3+22, "РЕАКЦИЯ ЗАМЕЩЕНИЯ", 13, GREEN, anchor="middle", weight="bold")
    svg += text_element(x3+15, y3+48, "A + BC = AC + B", 18, WHITE, weight="bold")
    svg += text_element(x3+15, y3+72, "Простое вещ-во вытесняет", 11, VIOLET_200)
    svg += text_element(x3+15, y3+88, "элемент из сложного", 11, VIOLET_200)
    svg += text_element(x3+15, y3+110, "Примеры:", 11, GREEN, weight="bold")
    svg += text_element(x3+15, y3+127, "Zn + 2HCl = ZnCl\u2082 + H\u2082", 14, WHITE, weight="bold")
    svg += text_element(x3+15, y3+147, "Fe + CuSO\u2084 = FeSO\u2084 + Cu", 14, WHITE, weight="bold")

    # Visual: swap
    svg += f'  <circle cx="{x3+290}" cy="{y3+60}" r="16" fill="{ORANGE}" opacity="0.5"/>\n'
    svg += f'  <rect x="{x3+310}" y="{y3+48}" width="35" height="24" rx="4" fill="{BLUE}" opacity="0.3"/>\n'
    svg += f'  <line x1="{x3+320}" y1="{y3+80}" x2="{x3+320}" y2="{y3+95}" stroke="{VIOLET_400}" stroke-width="1.5"/>\n'
    svg += f'  <polygon points="{x3+320},{y3+95} {x3+316},{y3+88} {x3+324},{y3+88}" fill="{VIOLET_400}"/>\n'
    svg += f'  <rect x="{x3+280}" y="{y3+100}" width="35" height="24" rx="4" fill="{BLUE}" opacity="0.3"/>\n'
    svg += f'  <circle cx="{x3+340}" cy="{y3+112}" r="16" fill="{YELLOW}" opacity="0.5"/>\n'
    # Swap arrow
    svg += f'  <path d="M{x3+285},{y3+55} Q{x3+270},{y3+35} {x3+310},{y3+55}" fill="none" stroke="{GREEN}" stroke-width="1.5" stroke-dasharray="3,2"/>\n'
    svg += f'  <path d="M{x3+345},{y3+107} Q{x3+365},{y3+130} {x3+285},{y3+107}" fill="none" stroke="{GREEN}" stroke-width="1.5" stroke-dasharray="3,2"/>\n'

    # Card 4: Double replacement / Exchange (Обмен)
    x4, y4 = 405, 255
    svg += card(x4, y4, card_w, card_h)
    svg += f'  <rect x="{x4+5}" y="{y4+5}" width="180" height="24" rx="6" fill="{PINK}" opacity="0.3"/>\n'
    svg += text_element(x4+95, y4+22, "РЕАКЦИЯ ОБМЕНА", 13, PINK, anchor="middle", weight="bold")
    svg += text_element(x4+15, y4+48, "AB + CD = AD + CB", 18, WHITE, weight="bold")
    svg += text_element(x4+15, y4+72, "Сложные вещества обмениваются", 11, VIOLET_200)
    svg += text_element(x4+15, y4+88, "составными частями", 11, VIOLET_200)
    svg += text_element(x4+15, y4+110, "Примеры:", 11, PINK, weight="bold")
    svg += text_element(x4+15, y4+127, "NaOH + HCl = NaCl + H\u2082O", 13, WHITE, weight="bold")
    svg += text_element(x4+15, y4+147, "AgNO\u2083 + NaCl = AgCl + NaNO\u2083", 13, WHITE, weight="bold")

    # Visual: cross-swap
    svg += f'  <rect x="{x4+270}" y="{y4+48}" width="30" height="20" rx="3" fill="{BLUE}" opacity="0.3"/>\n'
    svg += f'  <rect x="{x4+310}" y="{y4+48}" width="30" height="20" rx="3" fill="{RED}" opacity="0.3"/>\n'
    svg += f'  <rect x="{x4+270}" y="{y4+78}" width="30" height="20" rx="3" fill="{GREEN}" opacity="0.3"/>\n'
    svg += f'  <rect x="{x4+310}" y="{y4+78}" width="30" height="20" rx="3" fill="{ORANGE}" opacity="0.3"/>\n'
    # Cross arrows
    svg += f'  <line x1="{x4+285}" y1="{y4+72}" x2="{x4+285}" y2="{y4+95}" stroke="{VIOLET_400}" stroke-width="1"/>\n'
    svg += f'  <line x1="{x4+325}" y1="{y4+72}" x2="{x4+325}" y2="{y4+95}" stroke="{VIOLET_400}" stroke-width="1"/>\n'
    svg += text_element(x4+345, y4+60, "+", 14, WHITE)
    svg += text_element(x4+345, y4+90, "+", 14, WHITE)

    # Bottom: Summary
    svg += card(20, 425, 760, 140)
    svg += text_element(400, 450, "Классификация по числу и составу веществ", 14, VIOLET_400, weight="bold", anchor="middle")

    # Summary diagram with arrows
    types_info = [
        ("Соединение", "A + B → AB", "2H\u2082 + O\u2082 → 2H\u2082O", BLUE),
        ("Разложение", "AB → A + B", "2H\u2082O → 2H\u2082 + O\u2082", RED),
        ("Замещение", "A + BC → AC + B", "Zn + CuCl\u2082 → ZnCl\u2082 + Cu", GREEN),
        ("Обмен", "AB + CD → AD + CB", "NaOH + HCl → NaCl + H\u2082O", PINK),
    ]
    for i, (name, formula, example, clr) in enumerate(types_info):
        bx = 45 + i * 185
        by = 470
        svg += f'  <rect x="{bx}" y="{by}" width="170" height="80" rx="8" fill="{clr}" opacity="0.1" stroke="{clr}" stroke-width="1"/>\n'
        svg += text_element(bx + 85, by + 18, name, 13, clr, anchor="middle", weight="bold")
        svg += text_element(bx + 85, by + 40, formula, 14, WHITE, anchor="middle", weight="bold")
        svg += text_element(bx + 85, by + 60, example, 10, VIOLET_200, anchor="middle")
        svg += text_element(bx + 85, by + 75, "↑ нагрев / ∆t", 9, VIOLET_400, anchor="middle")

    svg += footer()
    svg += '</svg>'
    return svg


def generate_lesson6():
    """Lesson 6: Уравнения химических реакций"""
    svg = svg_header()
    svg += svg_background()
    svg += title_bar("Уравнения химических реакций", "Закон сохранения массы, балансировка", 6)

    # Top left: Law of conservation
    svg += card(20, 85, 380, 200)
    svg += text_element(210, 112, "Закон сохранения массы", 15, VIOLET_400, weight="bold", anchor="middle")
    svg += text_element(210, 138, "М.В. Ломоносов, 1748 г.", 12, VIOLET_300, anchor="middle")

    svg += text_element(35, 170, "Масса веществ, вступивших", 13, WHITE)
    svg += text_element(35, 188, "в реакцию, равна массе", 13, WHITE)
    svg += text_element(35, 206, "веществ, получившихся", 13, WHITE)
    svg += text_element(35, 224, "в результате реакции.", 13, WHITE)

    # Balance visualization
    svg += f'  <line x1="120" y1="255" x2="300" y2="255" stroke="{VIOLET_400}" stroke-width="2"/>\n'
    svg += f'  <polygon points="210,248 205,258 215,258" fill="{VIOLET_400}"/>\n'
    svg += f'  <rect x="90" y="238" width="60" height="20" rx="4" fill="{BLUE}" opacity="0.3" stroke="{BLUE}" stroke-width="1"/>\n'
    svg += text_element(120, 252, "Реаг.", 10, BLUE, anchor="middle")
    svg += f'  <rect x="270" y="238" width="60" height="20" rx="4" fill="{GREEN}" opacity="0.3" stroke="{GREEN}" stroke-width="1"/>\n'
    svg += text_element(300, 252, "Прод.", 10, GREEN, anchor="middle")
    svg += text_element(120, 275, "m = m", 16, WHITE, anchor="middle", weight="bold")
    svg += text_element(160, 270, "реаг", 10, BLUE, anchor="start")
    svg += text_element(300, 275, "m", 16, WHITE, anchor="middle", weight="bold")
    svg += text_element(310, 270, "прод", 10, GREEN, anchor="start")

    # Top right: Coefficients
    svg += card(410, 85, 370, 200)
    svg += text_element(595, 112, "Правила расстановки", 15, VIOLET_400, weight="bold", anchor="middle")
    svg += text_element(595, 132, "коэффициентов", 15, VIOLET_400, weight="bold", anchor="middle")

    rules = [
        "1. Подсчитать атомы каждого",
        "   элемента слева и справа",
        "2. Начать с элемента с",
        "   наибольшим числом атомов",
        "3. Ставить коэффициенты",
        "   ПЕРЕД формулами",
        "4. Проверить баланс каждого",
        "   элемента",
    ]
    for i, r in enumerate(rules):
        svg += text_element(425, 158 + i * 17, r, 11, WHITE)

    # Bottom: Balancing example
    svg += card(20, 300, 760, 265)
    svg += text_element(400, 325, "Пример: Уравнивание реакции", 15, VIOLET_400, weight="bold", anchor="middle")

    # Step by step
    svg += text_element(35, 355, "Шаг 1: Незаписанная реакция", 12, VIOLET_300, weight="bold")
    svg += text_element(35, 378, "Fe + O\u2082 \u2192 Fe\u2082O\u2083", 20, WHITE, weight="bold")

    svg += text_element(35, 408, "Шаг 2: Подсчёт атомов", 12, VIOLET_300, weight="bold")
    # Table
    svg += text_element(60, 430, "Элемент", 12, VIOLET_400, weight="bold")
    svg += text_element(180, 430, "Слева", 12, VIOLET_400, weight="bold")
    svg += text_element(280, 430, "Справа", 12, VIOLET_400, weight="bold")

    svg += f'  <line x1="40" y1="435" x2="350" y2="435" stroke="{VIOLET_600}" stroke-width="0.5"/>\n'
    svg += text_element(60, 450, "Fe", 13, ORANGE, weight="bold")
    svg += text_element(180, 450, "1", 13, RED, weight="bold")
    svg += text_element(280, 450, "2", 13, GREEN, weight="bold")
    svg += text_element(60, 468, "O", 13, CYAN, weight="bold")
    svg += text_element(180, 468, "2", 13, RED, weight="bold")
    svg += text_element(280, 468, "3", 13, RED, weight="bold")

    svg += text_element(35, 498, "Шаг 3: Расставляем коэффициенты", 12, VIOLET_300, weight="bold")

    svg += text_element(35, 522, "4Fe + 3O\u2082 \u2192 2Fe\u2082O\u2083", 22, WHITE, weight="bold")
    svg += f'  <rect x="30" y="506" width="280" height="28" rx="5" fill="{GREEN}" opacity="0.1" stroke="{GREEN}" stroke-width="1"/>\n'

    # Verify
    svg += text_element(370, 498, "Проверка:", 12, GREEN, weight="bold")
    svg += text_element(370, 518, "Fe: 4=2\u00B72=4 \u2713", 13, GREEN)
    svg += text_element(370, 536, "O:  3\u00B72=6=2\u00B73=6 \u2713", 13, GREEN)

    # More examples on the right
    svg += card(550, 340, 220, 210)
    svg += text_element(660, 362, "Ещё примеры", 13, VIOLET_400, weight="bold", anchor="middle")

    svg += text_element(565, 390, "H\u2082 + Cl\u2082 = 2HCl", 14, WHITE, weight="bold")
    svg += text_element(565, 418, "2Na + 2H\u2082O =", 13, WHITE, weight="bold")
    svg += text_element(575, 436, "2NaOH + H\u2082", 13, WHITE, weight="bold")
    svg += text_element(565, 462, "CH\u2084 + 2O\u2082 =", 13, WHITE, weight="bold")
    svg += text_element(575, 480, "CO\u2082 + 2H\u2082O", 13, WHITE, weight="bold")
    svg += text_element(565, 510, "Al\u2082O\u2083 + 6HCl =", 12, WHITE, weight="bold")
    svg += text_element(575, 528, "2AlCl\u2083 + 3H\u2082O", 12, WHITE, weight="bold")

    svg += footer()
    svg += '</svg>'
    return svg


def generate_lesson7():
    """Lesson 7: Скорость химических реакций"""
    svg = svg_header()
    svg += svg_background()
    svg += title_bar("Скорость химических реакций", "Факторы: температура, концентрация, катализаторы", 7)

    # Top: Definition
    svg += card(20, 85, 760, 80)
    svg += text_element(400, 112, "Скорость реакции v = \u0394n / (\u0394t \u00B7 V)", 20, WHITE, anchor="middle", weight="bold")
    svg += text_element(400, 135, "\u0394n — изменение количества вещества (моль)   \u0394t — время (с)   V — объём (л)", 12, VIOLET_300, anchor="middle")
    svg += text_element(400, 152, "Единица: моль/(л\u00B7с)", 12, VIOLET_400, anchor="middle")

    # Four factor cards
    card_w = 180
    card_h = 210

    # Factor 1: Temperature
    x1 = 15
    svg += card(x1, 180, card_w, card_h)
    svg += f'  <rect x="{x1+5}" y="185" width="{card_w-10}" height="26" rx="6" fill="{RED}" opacity="0.3"/>\n'
    svg += text_element(x1 + card_w/2, 203, "Температура", 14, RED, anchor="middle", weight="bold")

    # Thermometer icon
    svg += f'  <rect x="{x1+80}" y="220" width="10" height="50" rx="5" fill="{WHITE}" opacity="0.3"/>\n'
    svg += f'  <rect x="{x1+82}" y="240" width="6" height="28" rx="3" fill="{RED}"/>\n'
    svg += f'  <circle cx="{x1+85}" cy="275" r="8" fill="{RED}"/>\n'

    svg += text_element(x1+15, 300, "Правило Вант-Гоффа:", 10, VIOLET_300)
    svg += text_element(x1+15, 316, "При повышении t на 10\u00B0C", 10, WHITE)
    svg += text_element(x1+15, 330, "скорость увеличивается", 10, WHITE)
    svg += text_element(x1+15, 344, "в 2-4 раза", 13, RED, weight="bold")
    svg += text_element(x1+15, 365, "v\u2082/v\u2081 = \u03B3^((t\u2082-t\u2081)/10)", 12, WHITE, weight="bold")
    svg += text_element(x1+15, 382, "\u03B3 = 2\u20134 (температурный коэфф.)", 9, VIOLET_200)

    # Factor 2: Concentration
    x2 = 210
    svg += card(x2, 180, card_w, card_h)
    svg += f'  <rect x="{x2+5}" y="185" width="{card_w-10}" height="26" rx="6" fill="{BLUE}" opacity="0.3"/>\n'
    svg += text_element(x2 + card_w/2, 203, "Концентрация", 14, BLUE, anchor="middle", weight="bold")

    # Concentration visual: more dots = faster
    svg += f'  <rect x="{x2+20}" y="220" width="60" height="45" rx="4" fill="{WHITE}" opacity="0.1" stroke="{VIOLET_500}" stroke-width="0.5"/>\n'
    for dx in range(3):
        for dy in range(3):
            svg += f'  <circle cx="{x2+30+dx*18}" cy="{230+dy*14}" r="4" fill="{BLUE}" opacity="0.5"/>\n'
    svg += text_element(x2+50, 278, "Низкая", 10, VIOLET_300, anchor="middle")

    svg += f'  <rect x="{x2+95}" y="220" width="60" height="45" rx="4" fill="{WHITE}" opacity="0.1" stroke="{VIOLET_500}" stroke-width="0.5"/>\n'
    for dx in range(5):
        for dy in range(4):
            svg += f'  <circle cx="{x2+105+dx*11}" cy="{228+dy*10}" r="3.5" fill="{BLUE}" opacity="0.7"/>\n'
    svg += text_element(x2+125, 278, "Высокая", 10, VIOLET_300, anchor="middle")

    svg += text_element(x2+15, 300, "Чем больше концентрация", 10, WHITE)
    svg += text_element(x2+15, 314, "реагентов, тем выше", 10, WHITE)
    svg += text_element(x2+15, 328, "скорость реакции", 10, WHITE)
    svg += text_element(x2+15, 350, "v = k \u00B7 [A]\u207F \u00B7 [B]\u1D50", 12, WHITE, weight="bold")
    svg += text_element(x2+15, 370, "Закон действующих масс", 10, VIOLET_200)

    # Factor 3: Catalyst
    x3 = 405
    svg += card(x3, 180, card_w, card_h)
    svg += f'  <rect x="{x3+5}" y="185" width="{card_w-10}" height="26" rx="6" fill="{GREEN}" opacity="0.3"/>\n'
    svg += text_element(x3 + card_w/2, 203, "Катализатор", 14, GREEN, anchor="middle", weight="bold")

    # Energy diagram
    svg += f'  <rect x="{x3+20}" y="220" width="140" height="60" rx="4" fill="rgba(255,255,255,0.05)" stroke="{VIOLET_500}" stroke-width="0.5"/>\n'
    # Without catalyst (higher barrier)
    svg += f'  <path d="M{x3+25},270 Q{x3+55},220 {x3+90},270" fill="none" stroke="{RED}" stroke-width="2"/>\n'
    # With catalyst (lower barrier)
    svg += f'  <path d="M{x3+25},270 Q{x3+55},245 {x3+90},270" fill="none" stroke="{GREEN}" stroke-width="2"/>\n'
    svg += text_element(x3+35, 288, "— без катализ.", 9, RED)
    svg += text_element(x3+35, 300, "— с катализ.", 9, GREEN)
    svg += text_element(x3+100, 232, "E\u2090", 10, RED)

    svg += text_element(x3+15, 320, "Ускоряет реакцию,", 10, WHITE)
    svg += text_element(x3+15, 334, "но не расходуется", 10, WHITE)
    svg += text_element(x3+15, 354, "Снижает энергию", 10, WHITE)
    svg += text_element(x3+15, 368, "активации (E\u2090)", 10, WHITE)
    svg += text_element(x3+15, 385, "Пример: MnO\u2082 для O\u2082 из H\u2082O\u2082", 10, VIOLET_200)

    # Factor 4: Surface area
    x4 = 600
    svg += card(x4, 180, card_w, card_h)
    svg += f'  <rect x="{x4+5}" y="185" width="{card_w-10}" height="26" rx="6" fill="{ORANGE}" opacity="0.3"/>\n'
    svg += text_element(x4 + card_w/2, 203, "Площадь поверхности", 13, ORANGE, anchor="middle", weight="bold")

    # Solid vs powder visual
    # Big piece
    svg += f'  <rect x="{x4+15}" y="225" width="35" height="35" rx="3" fill="{ORANGE}" opacity="0.5" stroke="{ORANGE}" stroke-width="1"/>\n'
    svg += text_element(x4+33, 275, "Цельный", 9, VIOLET_300, anchor="middle")

    # Powder
    for i in range(8):
        px = x4 + 70 + (i % 4) * 12
        py = 225 + (i // 4) * 14
        svg += f'  <rect x="{px}" y="{py}" width="9" height="9" rx="1" fill="{ORANGE}" opacity="0.7"/>\n'
    svg += text_element(x4+95, 275, "Порошок", 9, VIOLET_300, anchor="middle")

    svg += text_element(x4+15, 298, "Чем больше площадь", 10, WHITE)
    svg += text_element(x4+15, 312, "контакта, тем быстрее", 10, WHITE)
    svg += text_element(x4+15, 326, "идёт реакция", 10, WHITE)
    svg += text_element(x4+15, 350, "Измельчение \u2192", 10, WHITE)
    svg += text_element(x4+15, 364, "\u2191 площадь поверхности", 10, ORANGE, weight="bold")
    svg += text_element(x4+15, 380, "\u2192 \u2191 скорость реакции", 10, ORANGE, weight="bold")

    # Bottom: Speed graph
    svg += card(20, 405, 760, 160)
    svg += text_element(400, 428, "Зависимость скорости от температуры", 14, VIOLET_400, weight="bold", anchor="middle")

    # Axes
    ax_x = 60
    ax_y = 440
    ax_w = 680
    ax_h = 100
    svg += f'  <line x1="{ax_x}" y1="{ax_y + ax_h}" x2="{ax_x + ax_w}" y2="{ax_y + ax_h}" stroke="{VIOLET_400}" stroke-width="1.5"/>\n'
    svg += f'  <line x1="{ax_x}" y1="{ax_y}" x2="{ax_x}" y2="{ax_y + ax_h}" stroke="{VIOLET_400}" stroke-width="1.5"/>\n'
    svg += text_element(ax_x - 5, ax_y - 5, "v", 12, WHITE, anchor="end")
    svg += text_element(ax_x + ax_w + 5, ax_y + ax_h + 15, "t, \u00B0C", 12, WHITE)

    # Exponential curve
    points = []
    for i in range(50):
        x = ax_x + 10 + i * (ax_w - 20) / 50
        # Exponential growth
        t = i / 50.0
        y = ax_y + ax_h - 10 - (ax_h - 20) * (1 - (1 - t) ** 0.3)
        points.append(f"{x:.1f},{y:.1f}")
    svg += f'  <polyline points="{" ".join(points)}" fill="none" stroke="{RED}" stroke-width="2.5"/>\n'

    # Mark points
    for i, temp in enumerate(["0\u00B0", "10\u00B0", "20\u00B0", "30\u00B0"]):
        tx = ax_x + 50 + i * 160
        svg += f'  <line x1="{tx}" y1="{ax_y + ax_h}" x2="{tx}" y2="{ax_y + ax_h + 5}" stroke="{VIOLET_400}" stroke-width="1"/>\n'
        svg += text_element(tx, ax_y + ax_h + 15, temp, 10, VIOLET_300, anchor="middle")

    svg += text_element(ax_x + ax_w / 2, ax_y + ax_h + 30, "При +10\u00B0C скорость возрастает в 2\u20134 раза (правило Вант-Гоффа)", 12, VIOLET_300, anchor="middle")

    svg += footer()
    svg += '</svg>'
    return svg


def generate_lesson8():
    """Lesson 8: Кислоты и основания"""
    svg = svg_header()
    svg += svg_background()
    svg += title_bar("Кислоты и основания", "pH, свойства, индикаторы, нейтрализация", 8)

    # Left: Acids
    svg += card(20, 85, 370, 240)
    svg += f'  <rect x="25" y="90" width="360" height="28" rx="6" fill="{RED}" opacity="0.3"/>\n'
    svg += text_element(205, 109, "КИСЛОТЫ", 16, RED, anchor="middle", weight="bold")

    svg += text_element(35, 135, "Содержат H\u207A (протоны H\u2083O\u207A)", 12, WHITE)
    svg += text_element(35, 155, "pH &lt; 7 (кислая среда)", 13, RED, weight="bold")

    svg += text_element(35, 180, "Примеры кислот:", 12, VIOLET_400, weight="bold")
    acids = [
        ("HCl", "соляная"), ("H\u2082SO\u2084", "серная"),
        ("HNO\u2083", "азотная"), ("H\u2083PO\u2084", "фосфорная"),
        ("CH\u2083COOH", "уксусная"),
    ]
    for i, (formula, name) in enumerate(acids):
        y = 198 + i * 18
        svg += text_element(45, y, formula, 13, WHITE, weight="bold")
        svg += text_element(170, y, f"— {name}", 11, VIOLET_200)

    svg += text_element(35, 300, "Свойства:", 12, VIOLET_400, weight="bold")
    svg += text_element(35, 316, "Кислый вкус, изменяют окраску", 11, WHITE)
    svg += text_element(35, 332, "индикаторов, реагируют с металлами", 11, WHITE)

    # Right: Bases
    svg += card(410, 85, 370, 240)
    svg += f'  <rect x="415" y="90" width="360" height="28" rx="6" fill="{BLUE}" opacity="0.3"/>\n'
    svg += text_element(595, 109, "ОСНОВАНИЯ (ЩЁЛОЧИ)", 16, BLUE, anchor="middle", weight="bold")

    svg += text_element(425, 135, "Содержат OH\u207B (гидроксид-ионы)", 12, WHITE)
    svg += text_element(425, 155, "pH &gt; 7 (щелочная среда)", 13, BLUE, weight="bold")

    svg += text_element(425, 180, "Примеры оснований:", 12, VIOLET_400, weight="bold")
    bases = [
        ("NaOH", "едкий натр"), ("KOH", "едкое кали"),
        ("Ca(OH)\u2082", "гашёная известь"), ("Ba(OH)\u2082", "барит. вода"),
        ("Al(OH)\u2083", "гидроксид алюм."),
    ]
    for i, (formula, name) in enumerate(bases):
        y = 198 + i * 18
        svg += text_element(435, y, formula, 13, WHITE, weight="bold")
        svg += text_element(560, y, f"— {name}", 11, VIOLET_200)

    svg += text_element(425, 300, "Свойства:", 12, VIOLET_400, weight="bold")
    svg += text_element(425, 316, "Мылокопающие на ощупь,", 11, WHITE)
    svg += text_element(425, 332, "изменяют окраску индикаторов", 11, WHITE)

    # Middle: pH Scale
    svg += card(20, 340, 760, 100)
    svg += text_element(400, 362, "ШКАЛА pH", 15, VIOLET_400, weight="bold", anchor="middle")

    # pH scale bar
    scale_x = 60
    scale_y = 380
    scale_w = 680
    scale_h = 25

    # Gradient: red -> yellow -> green -> blue -> violet
    ph_colors = [
        (0, RED), (1, "#FF3333"), (2, "#FF6633"), (3, "#FF9933"),
        (4, ORANGE), (5, YELLOW), (6, "#CCFF33"), (7, GREEN),
        (8, "#33CC99"), (9, CYAN), (10, "#3399FF"),
        (11, BLUE), (12, "#3333FF"), (13, "#6633CC"), (14, "#660066"),
    ]
    for i, (ph, clr) in enumerate(ph_colors):
        px = scale_x + i * (scale_w / 14)
        pw = scale_w / 14 + 1
        svg += f'  <rect x="{px:.0f}" y="{scale_y}" width="{pw:.0f}" height="{scale_h}" fill="{clr}" opacity="0.7"/>\n'

    svg += text_element(scale_x + scale_w / 2, scale_y + scale_h + 15, "7 — нейтральная среда", 11, WHITE, anchor="middle")
    svg += text_element(scale_x + 40, scale_y + scale_h + 15, "Кислота", 11, RED, anchor="middle")
    svg += text_element(scale_x + scale_w - 40, scale_y + scale_h + 15, "Щёлочь", 11, BLUE, anchor="middle")

    # pH labels
    for i in [0, 7, 14]:
        px = scale_x + i * (scale_w / 14)
        svg += text_element(px, scale_y - 3, str(i), 10, WHITE, anchor="middle")

    # Arrow
    svg += f'  <line x1="{scale_x}" y1="{scale_y - 12}" x2="{scale_x + scale_w}" y2="{scale_y - 12}" stroke="{VIOLET_400}" stroke-width="1"/>\n'
    svg += text_element(scale_x, scale_y - 17, "pH\u2191", 9, VIOLET_300)
    svg += text_element(scale_x + scale_w, scale_y - 17, "pH\u2193", 9, VIOLET_300)

    # Bottom: Indicators table + Neutralization
    svg += card(20, 455, 460, 110)
    svg += text_element(250, 477, "Индикаторы", 14, VIOLET_400, weight="bold", anchor="middle")

    # Indicator table
    ind_x = 35
    ind_y = 490
    # Headers
    headers = ["Индикатор", "Кислая", "Нейтр.", "Щёлочная"]
    hx = [ind_x, ind_x + 120, ind_x + 210, ind_x + 300]
    for i, h in enumerate(headers):
        svg += f'  <rect x="{hx[i]-5}" y="{ind_y}" width="85" height="20" rx="3" fill="{VIOLET_700}"/>\n'
        svg += text_element(hx[i] + 37, ind_y + 14, h, 10, WHITE, anchor="middle", weight="bold")

    indicators = [
        ("Лакмус", RED, VIOLET_500, BLUE),
        ("Фенолфталеин", "transparent", "transparent", PINK),
        ("Метилоранж", RED, ORANGE, YELLOW),
    ]
    for i, (name, acid_c, neut_c, base_c) in enumerate(indicators):
        y = ind_y + 25 + i * 22
        bg = VIOLET_800 if i % 2 == 0 else "rgba(255,255,255,0.03)"
        for ci in range(4):
            svg += f'  <rect x="{hx[ci]-5}" y="{y}" width="85" height="20" rx="2" fill="{bg}" opacity="0.5"/>\n'
        svg += text_element(hx[0] + 37, y + 14, name, 10, WHITE, anchor="middle")
        colors = [acid_c, neut_c, base_c]
        for ci, c in enumerate(colors):
            if c != "transparent":
                svg += f'  <rect x="{hx[ci+1]+10}" y="{y+3}" width="55" height="14" rx="3" fill="{c}" opacity="0.5"/>\n'
                svg += text_element(hx[ci+1] + 37, y + 14, {"red": "Красн.", "pink": "Малин.", "orange": "Оранж.", "yellow": "Жёлт.", "blue": "Синий"}.get(c.lower().replace("#",""), ""), 9, WHITE, anchor="middle")
            else:
                svg += text_element(hx[ci+1] + 37, y + 14, "Бесцв.", 9, VIOLET_300, anchor="middle")

    # Neutralization reaction
    svg += card(500, 455, 280, 110)
    svg += text_element(640, 477, "Нейтрализация", 14, VIOLET_400, weight="bold", anchor="middle")

    svg += text_element(640, 500, "Кислота + Основание", 12, WHITE, anchor="middle")
    svg += text_element(640, 518, "= Соль + Вода", 13, WHITE, anchor="middle", weight="bold")
    svg += text_element(640, 540, "HCl + NaOH =", 12, WHITE, anchor="middle")
    svg += text_element(640, 555, "NaCl + H\u2082O", 14, GREEN, anchor="middle", weight="bold")

    svg += footer()
    svg += '</svg>'
    return svg


def generate_lesson9():
    """Lesson 9: Оксиды и соли"""
    svg = svg_header()
    svg += svg_background()
    svg += title_bar("Оксиды и соли", "Классификация, свойства, образование", 9)

    # Left: Oxides
    svg += card(20, 85, 370, 280)
    svg += f'  <rect x="25" y="90" width="360" height="28" rx="6" fill="{ORANGE}" opacity="0.3"/>\n'
    svg += text_element(205, 109, "ОКСИДЫ", 16, ORANGE, anchor="middle", weight="bold")

    svg += text_element(35, 138, "Общая формула: Э_xO_y", 14, WHITE, weight="bold")
    svg += text_element(35, 158, "Состоят из элемента и кислорода", 12, VIOLET_200)

    svg += text_element(35, 183, "Классификация оксидов:", 12, VIOLET_400, weight="bold")

    # Basic oxides
    svg += f'  <rect x="35" y="192" width="160" height="55" rx="5" fill="{BLUE}" opacity="0.15" stroke="{BLUE}" stroke-width="1"/>\n'
    svg += text_element(115, 210, "Основные", 12, BLUE, anchor="middle", weight="bold")
    svg += text_element(115, 225, "из металлов", 10, VIOLET_200, anchor="middle")
    svg += text_element(115, 240, "Na\u2082O, CaO, FeO", 10, WHITE, anchor="middle")

    # Acidic oxides
    svg += f'  <rect x="205" y="192" width="160" height="55" rx="5" fill="{RED}" opacity="0.15" stroke="{RED}" stroke-width="1"/>\n'
    svg += text_element(285, 210, "Кислотные", 12, RED, anchor="middle", weight="bold")
    svg += text_element(285, 225, "из неметаллов", 10, VIOLET_200, anchor="middle")
    svg += text_element(285, 240, "CO\u2082, SO\u2083, P\u2082O\u2085", 10, WHITE, anchor="middle")

    # Amphoteric
    svg += f'  <rect x="120" y="255" width="160" height="50" rx="5" fill="{GREEN}" opacity="0.15" stroke="{GREEN}" stroke-width="1"/>\n'
    svg += text_element(200, 273, "Амфотерные", 12, GREEN, anchor="middle", weight="bold")
    svg += text_element(200, 288, "Al\u2082O\u2083, ZnO, Cr\u2082O\u2083", 10, WHITE, anchor="middle")
    svg += text_element(200, 300, "(двойственные свойства)", 9, VIOLET_200, anchor="middle")

    # Properties
    svg += text_element(35, 325, "Свойства:", 12, VIOLET_400, weight="bold")
    svg += text_element(35, 342, "Основные + Кислота = Соль + H\u2082O", 11, WHITE)
    svg += text_element(35, 358, "Кислотные + Основание = Соль + H\u2082O", 11, WHITE)

    # Right: Salts
    svg += card(410, 85, 370, 280)
    svg += f'  <rect x="415" y="90" width="360" height="28" rx="6" fill="{GREEN}" opacity="0.3"/>\n'
    svg += text_element(595, 109, "СОЛИ", 16, GREEN, anchor="middle", weight="bold")

    svg += text_element(425, 138, "Общая формула: Me_x(Кисл.остаток)_y", 13, WHITE, weight="bold")

    svg += text_element(425, 165, "Классификация солей:", 12, VIOLET_400, weight="bold")

    salt_types = [
        ("Средние (нормальные)", "NaCl, CaSO\u2084, KNO\u2083", "Полное замещение H кислоты"),
        ("Кислые", "NaHSO\u2084, KHCO\u2083", "Частичное замещение H"),
        ("Основные", "Mg(OH)Cl, Cu\u2082(OH)\u2082CO\u2083", "Содержат OH\u207B группу"),
    ]
    for i, (name, examples, desc) in enumerate(salt_types):
        y = 183 + i * 58
        svg += f'  <rect x="425" y="{y-5}" width="340" height="52" rx="5" fill="rgba(255,255,255,0.05)" stroke="{VIOLET_500}" stroke-width="0.5"/>\n'
        svg += text_element(435, y + 10, name, 12, GREEN, weight="bold")
        svg += text_element(435, y + 26, examples, 12, WHITE, weight="bold")
        svg += text_element(435, y + 42, desc, 10, VIOLET_200)

    svg += text_element(425, 362, "Растворимость — по таблице", 12, VIOLET_300)

    # Bottom: Formation reactions
    svg += card(20, 380, 760, 185)
    svg += text_element(400, 405, "Способы получения солей и оксидов", 14, VIOLET_400, weight="bold", anchor="middle")

    # Formation paths
    paths = [
        ("Металл + Кислота", "Zn + 2HCl = ZnCl\u2082 + H\u2082\u2191", BLUE),
        ("Основание + Кислота", "NaOH + HCl = NaCl + H\u2082O", GREEN),
        ("Оксид + Кислота", "CuO + H\u2082SO\u2084 = CuSO\u2084 + H\u2082O", ORANGE),
        ("Оксид + Основание", "CO\u2082 + Ca(OH)\u2082 = CaCO\u2083 + H\u2082O", PINK),
        ("Соль + Соль", "AgNO\u2083 + NaCl = AgCl\u2193 + NaNO\u2083", CYAN),
    ]

    for i, (name, equation, clr) in enumerate(paths):
        col = i % 3
        row = i // 3
        bx = 35 + col * 250
        by = 425 + row * 70
        svg += f'  <rect x="{bx}" y="{by}" width="235" height="60" rx="6" fill="{clr}" opacity="0.08" stroke="{clr}" stroke-width="1"/>\n'
        svg += text_element(bx + 10, by + 18, name, 11, clr, weight="bold")
        svg += text_element(bx + 10, by + 38, equation, 12, WHITE, weight="bold")
        svg += text_element(bx + 10, by + 52, "\u2193 осадок / \u2191 газ", 9, VIOLET_300)

    svg += footer()
    svg += '</svg>'
    return svg


def validate_svg(svg_content, filename):
    """Validate SVG content as valid XML."""
    try:
        ET.fromstring(svg_content)
        return True, "Valid XML"
    except ET.ParseError as e:
        return False, str(e)


def main():
    # Create output directory
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
        (9, generate_lesson9),
    ]

    results = []
    for lesson_num, generator in generators:
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{lesson_num}.svg")
        svg_content = generator()

        # Validate before writing
        is_valid, msg = validate_svg(svg_content, filepath)

        if is_valid:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(svg_content)
            file_size = os.path.getsize(filepath)
            results.append((lesson_num, filepath, "✓ VALID", file_size, msg))
            print(f"  ✓ Lesson {lesson_num}: VALID XML — {filepath} ({file_size} bytes)")
        else:
            results.append((lesson_num, filepath, "✗ INVALID", 0, msg))
            print(f"  ✗ Lesson {lesson_num}: INVALID XML — {msg}")

    # Final validation: re-read and parse all files
    print("\n--- Final Validation ---")
    all_valid = True
    for lesson_num, filepath, status, size, msg in results:
        if status == "✓ VALID":
            try:
                tree = ET.parse(filepath)
                root = tree.getroot()
                w = root.get('width')
                h = root.get('height')
                print(f"  Lesson {lesson_num}: {w}x{h} — {size} bytes — OK")
            except Exception as e:
                print(f"  Lesson {lesson_num}: RE-PARSE ERROR — {e}")
                all_valid = False
        else:
            all_valid = False
            print(f"  Lesson {lesson_num}: FAILED — {msg}")

    if all_valid:
        print(f"\n✓ All {len(generators)} SVG files generated and validated successfully!")
    else:
        print(f"\n✗ Some SVG files failed validation!")

    return all_valid


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
