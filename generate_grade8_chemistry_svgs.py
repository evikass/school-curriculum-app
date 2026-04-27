#!/usr/bin/env python3
"""
Generate 10 detailed educational SVG images for Grade 8 Chemistry lessons.
Purple/violet color scheme (#8B5CF6 primary).
Each SVG is 800x600 with Russian text, diagrams, formulas, visual elements.
"""

import os
import xml.sax.saxutils as saxutils

BASE_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/chemistry"
os.makedirs(BASE_DIR, exist_ok=True)

# Color scheme
PRIMARY = "#8B5CF6"
PRIMARY_DARK = "#7C3AED"
PRIMARY_LIGHT = "#A78BFA"
PRIMARY_LIGHTER = "#C4B5FD"
PRIMARY_LIGHTEST = "#EDE9FE"
ACCENT = "#6D28D9"
ACCENT2 = "#5B21B6"
BG = "#F5F3FF"
BG2 = "#EDE9FE"
WHITE = "#FFFFFF"
BLACK = "#1E1B4B"
GRAY = "#6B7280"
LIGHT_GRAY = "#E5E7EB"
RED = "#EF4444"
BLUE = "#3B82F6"
GREEN = "#10B981"
ORANGE = "#F59E0B"
CYAN = "#06B6D4"
PINK = "#EC4899"

W, H = 800, 600

def esc(text):
    """Escape text for XML"""
    return saxutils.escape(str(text))

def svg_header(title_text):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{PRIMARY_LIGHTEST};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{BG};stop-opacity:1"/>
    </linearGradient>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:{ACCENT2};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{PRIMARY};stop-opacity:1"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:{WHITE};stop-opacity:0.95"/>
      <stop offset="100%" style="stop-color:{PRIMARY_LIGHTEST};stop-opacity:0.9"/>
    </linearGradient>
    <filter id="shadow" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="{ACCENT2}" flood-opacity="0.15"/>
    </filter>
    <filter id="shadowSm" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="{ACCENT2}" flood-opacity="0.1"/>
    </filter>
  </defs>
  <!-- Background -->
  <rect width="{W}" height="{H}" fill="url(#bgGrad)" rx="0"/>
  <!-- Decorative circles -->
  <circle cx="750" cy="50" r="80" fill="{PRIMARY}" opacity="0.05"/>
  <circle cx="50" cy="550" r="60" fill="{PRIMARY}" opacity="0.05"/>
  <circle cx="400" cy="600" r="100" fill="{PRIMARY_LIGHT}" opacity="0.04"/>
  <!-- Header bar -->
  <rect x="0" y="0" width="{W}" height="60" fill="url(#headerGrad)" rx="0"/>
  <text x="400" y="38" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="22" font-weight="bold" fill="{WHITE}">{esc(title_text)}</text>
  <!-- Small decorative line under header -->
  <rect x="300" y="54" width="200" height="3" fill="{PRIMARY_LIGHTER}" rx="1.5" opacity="0.7"/>
'''

def svg_footer():
    return f'''  <!-- Footer -->
  <rect x="0" y="580" width="{W}" height="20" fill="{PRIMARY_DARK}" opacity="0.1"/>
  <text x="400" y="594" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="10" fill="{GRAY}">Химия — 8 класс</text>
</svg>'''

def card(x, y, w, h, rx=12):
    return f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#cardGrad)" stroke="{PRIMARY_LIGHTER}" stroke-width="1.5" rx="{rx}" filter="url(#shadow)"/>\n'

def section_title(x, y, text, color=PRIMARY_DARK, size=15):
    return f'  <text x="{x}" y="{y}" font-family="Arial,Helvetica,sans-serif" font-size="{size}" font-weight="bold" fill="{color}">{esc(text)}</text>\n'

def body_text(x, y, text, size=13, color=BLACK, anchor="start"):
    return f'  <text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Arial,Helvetica,sans-serif" font-size="{size}" fill="{color}">{esc(text)}</text>\n'

def formula_text(x, y, text, size=16, color=ACCENT2, anchor="middle"):
    return f'  <text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Arial,Helvetica,sans-serif" font-size="{size}" font-weight="bold" fill="{color}">{esc(text)}</text>\n'

def highlight_box(x, y, w, h, color=PRIMARY_LIGHTEST, stroke=PRIMARY_LIGHT):
    return f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}" stroke="{stroke}" stroke-width="1" rx="8"/>\n'


# ===== LESSON 1: Периодический закон Д.И. Менделеева =====
def lesson1():
    s = svg_header("Периодический закон Д.И. Менделеева")
    # Periodic law definition card
    s += card(20, 75, 760, 80)
    s += section_title(40, 100, "Периодический закон (1869 г.)")
    s += body_text(40, 120, "Свойства химических элементов и образованных ими веществ находятся в периодической", 12, GRAY)
    s += body_text(40, 136, "зависимости от величины зарядов их атомных ядер.", 12, GRAY)
    s += formula_text(400, 155, "Закон: свойства ~ Z (заряд ядра)", 13, ACCENT2)

    # Mini periodic table fragment
    s += card(20, 165, 400, 250)
    s += section_title(40, 190, "Фрагмент периодической таблицы")
    # Period 1
    s += highlight_box(40, 200, 55, 40, "#DBEAFE", BLUE)
    s += body_text(48, 216, "1 H", 11, BLUE)
    s += body_text(55, 232, "1", 9, GRAY)
    s += highlight_box(325, 200, 55, 40, "#FEF3C7", ORANGE)
    s += body_text(333, 216, "2 He", 11, ORANGE)
    s += body_text(340, 232, "2", 9, GRAY)
    # Period 2
    s += highlight_box(40, 248, 55, 40, "#FEE2E2", RED)
    s += body_text(50, 264, "3 Li", 11, RED)
    s += body_text(55, 280, "3", 9, GRAY)
    s += highlight_box(95, 248, 55, 40, "#FEE2E2", RED)
    s += body_text(103, 264, "4 Be", 11, RED)
    s += highlight_box(155, 248, 55, 40, "#D1FAE5", GREEN)
    s += body_text(167, 264, "5 B", 11, GREEN)
    s += highlight_box(210, 248, 55, 40, "#D1FAE5", GREEN)
    s += body_text(216, 264, "6 C", 11, GREEN)
    s += highlight_box(265, 248, 55, 40, "#D1FAE5", GREEN)
    s += body_text(273, 264, "7 N", 11, GREEN)
    s += highlight_box(325, 248, 55, 40, "#FEF3C7", ORANGE)
    s += body_text(333, 264, "8 O", 11, ORANGE)
    # Period 3
    s += highlight_box(40, 296, 55, 40, "#FEE2E2", RED)
    s += body_text(48, 312, "11 Na", 10, RED)
    s += highlight_box(95, 296, 55, 40, "#FEE2E2", RED)
    s += body_text(103, 312, "12 Mg", 10, RED)
    s += highlight_box(155, 296, 55, 40, "#D1FAE5", GREEN)
    s += body_text(167, 312, "13 Al", 10, GREEN)
    s += highlight_box(210, 296, 55, 40, "#D1FAE5", GREEN)
    s += body_text(220, 312, "14 Si", 10, GREEN)
    s += highlight_box(265, 296, 55, 40, "#D1FAE5", GREEN)
    s += body_text(273, 312, "15 P", 10, GREEN)
    s += highlight_box(325, 296, 55, 40, "#FEF3C7", ORANGE)
    s += body_text(333, 312, "16 S", 10, ORANGE)

    # Legend
    s += highlight_box(40, 345, 12, 12, "#FEE2E2", RED)
    s += body_text(58, 355, "Металлы", 11, RED)
    s += highlight_box(120, 345, 12, 12, "#D1FAE5", GREEN)
    s += body_text(138, 355, "Неметаллы", 11, GREEN)
    s += highlight_box(215, 345, 12, 12, "#FEF3C7", ORANGE)
    s += body_text(233, 355, "Благородные газы", 11, ORANGE)

    # Structure info card
    s += card(430, 165, 350, 250)
    s += section_title(450, 190, "Структура таблицы")
    s += highlight_box(450, 202, 310, 45, "#FEE2E2", RED)
    s += body_text(460, 220, "7 периодов (горизонтальные ряды)", 12, RED)
    s += body_text(460, 238, "Номер периода = число энергоуровней", 11, GRAY)
    s += highlight_box(450, 257, 310, 45, "#DBEAFE", BLUE)
    s += body_text(460, 275, "8 групп (вертикальные столбцы)", 12, BLUE)
    s += body_text(460, 293, "Номер группы = число электронов на", 11, GRAY)
    s += body_text(460, 308, "внешнем уровне (для главных подгрупп)", 11, GRAY)
    s += highlight_box(450, 322, 310, 40, "#EDE9FE", PRIMARY)
    s += body_text(460, 340, "Главные подгруппы (A) и побочные (B)", 12, PRIMARY_DARK)
    s += body_text(460, 356, "s-, p-, d-, f- элементы", 11, GRAY)

    # Key trends card
    s += card(20, 425, 760, 145)
    s += section_title(40, 450, "Закономерности изменения свойств")
    # Arrows and labels for trends
    # Left: period trend
    s += highlight_box(40, 460, 350, 100, "#F5F3FF", PRIMARY_LIGHT)
    s += body_text(55, 480, "В периоде (слева направо):", 12, PRIMARY_DARK)
    s += body_text(55, 498, "Металлические свойства убывают", 12, RED)
    s += body_text(55, 516, "Неметаллические свойства возрастают", 12, GREEN)
    s += body_text(55, 534, "Электроотрицательность возрастает", 12, BLUE)
    # Arrow
    s += f'  <line x1="300" y1="540" x2="370" y2="540" stroke="{PRIMARY}" stroke-width="2" marker-end="url(#arrowR)"/>\n'
    s += f'  <defs><marker id="arrowR" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="{PRIMARY}"/></marker></defs>\n'

    # Right: group trend
    s += highlight_box(410, 460, 350, 100, "#F5F3FF", PRIMARY_LIGHT)
    s += body_text(425, 480, "В группе (сверху вниз):", 12, PRIMARY_DARK)
    s += body_text(425, 498, "Металлические свойства возрастают", 12, RED)
    s += body_text(425, 516, "Неметаллические свойства убывают", 12, GREEN)
    s += body_text(425, 534, "Радиус атома увеличивается", 12, BLUE)
    # Down arrow
    s += f'  <line x1="720" y1="480" x2="720" y2="545" stroke="{PRIMARY}" stroke-width="2" marker-end="url(#arrowD)"/>\n'
    s += f'  <defs><marker id="arrowD" markerWidth="6" markerHeight="8" refX="3" refY="8" orient="auto"><path d="M0,0 L6,0 L3,8 Z" fill="{PRIMARY}"/></marker></defs>\n'

    s += svg_footer()
    return s


# ===== LESSON 2: Характеристика элемента по положению в таблице =====
def lesson2():
    s = svg_header("Характеристика элемента по положению в таблице")
    # Main example: Sulfur (S)
    s += card(20, 75, 340, 280)
    s += section_title(40, 100, "Пример: Сера (S)")

    # Element card styled box
    s += highlight_box(50, 115, 130, 150, "#EDE9FE", PRIMARY)
    s += body_text(115, 140, "16", 28, ACCENT2, "middle")
    s += body_text(115, 180, "S", 40, ACCENT2, "middle")
    s += body_text(115, 210, "Сера", 12, GRAY, "middle")
    s += body_text(115, 230, "32,06", 12, GRAY, "middle")

    # Characteristics
    s += body_text(200, 135, "Z = 16 (порядковый номер)", 12, PRIMARY_DARK)
    s += body_text(200, 155, "Период: 3", 12, PRIMARY_DARK)
    s += body_text(200, 175, "Группа: VIA (16)", 12, PRIMARY_DARK)
    s += body_text(200, 195, "Подгруппа: главная", 12, PRIMARY_DARK)
    s += body_text(200, 215, "Ar = 32,06 (относ. ат. масса)", 12, PRIMARY_DARK)
    s += highlight_box(200, 230, 145, 40, "#FEF3C7", ORANGE)
    s += body_text(210, 248, "Неметалл", 14, ORANGE)
    s += body_text(210, 263, "p-элемент", 11, GRAY)

    # Atom structure for Sulfur
    s += card(380, 75, 400, 280)
    s += section_title(400, 100, "Электронное строение серы")
    # Nucleus
    s += f'  <circle cx="580" cy="210" r="22" fill="{ACCENT2}" opacity="0.3"/>\n'
    s += f'  <circle cx="580" cy="210" r="16" fill="{ACCENT2}" opacity="0.5"/>\n'
    s += body_text(580, 215, "+16", 11, WHITE, "middle")
    # Energy levels
    s += f'  <circle cx="580" cy="210" r="45" fill="none" stroke="{PRIMARY_LIGHT}" stroke-width="1.5" stroke-dasharray="4,3"/>\n'
    s += f'  <circle cx="580" cy="210" r="75" fill="none" stroke="{PRIMARY_LIGHT}" stroke-width="1.5" stroke-dasharray="4,3"/>\n'
    s += f'  <circle cx="580" cy="210" r="105" fill="none" stroke="{PRIMARY_LIGHT}" stroke-width="1.5" stroke-dasharray="4,3"/>\n'
    # Electrons on levels
    # Level 1: 2e
    s += f'  <circle cx="580" cy="165" r="5" fill="{CYAN}"/>\n'
    s += f'  <circle cx="580" cy="255" r="5" fill="{CYAN}"/>\n'
    # Level 2: 8e
    for angle in range(0, 360, 45):
        import math
        ex = 580 + 75 * math.cos(math.radians(angle))
        ey = 210 + 75 * math.sin(math.radians(angle))
        s += f'  <circle cx="{ex:.1f}" cy="{ey:.1f}" r="4" fill="{BLUE}"/>\n'
    # Level 3: 6e
    for angle in range(0, 360, 60):
        ex = 580 + 105 * math.cos(math.radians(angle))
        ey = 210 + 105 * math.sin(math.radians(angle))
        s += f'  <circle cx="{ex:.1f}" cy="{ey:.1f}" r="4" fill="{GREEN}"/>\n'
    # Level labels
    s += body_text(630, 178, "n=1: 2e", 10, CYAN)
    s += body_text(660, 210, "n=2: 8e", 10, BLUE)
    s += body_text(688, 250, "n=3: 6e", 10, GREEN)
    # Formula
    s += formula_text(580, 340, "1s\u00b2 2s\u00b2 2p\u2076 3s\u00b2 3p\u2074", 15, ACCENT2)

    # Rules card
    s += card(20, 365, 760, 205)
    s += section_title(40, 390, "Правила определения характеристик элемента")
    # Table-like layout
    s += highlight_box(40, 405, 350, 30, "#EDE9FE", PRIMARY_LIGHT)
    s += body_text(50, 424, "Порядковый номер = заряд ядра (Z)", 13, ACCENT2)
    s += highlight_box(40, 440, 350, 30, "#DBEAFE", "#93C5FD")
    s += body_text(50, 459, "Номер периода = число энергоуровней", 13, BLUE)
    s += highlight_box(40, 475, 350, 30, "#D1FAE5", "#6EE7B7")
    s += body_text(50, 494, "Номер группы = число e на внешн. уровне", 13, GREEN)
    s += highlight_box(40, 510, 350, 30, "#FEF3C7", "#FCD34D")
    s += body_text(50, 529, "Число протонов = Z, нейтронов = Ar - Z", 13, ORANGE)

    # Another example
    s += highlight_box(410, 405, 350, 30, "#FEE2E2", "#FCA5A5")
    s += body_text(420, 424, "Na (11): Z=11, 3 период, IA группа", 12, RED)
    s += highlight_box(410, 440, 350, 30, "#FEE2E2", "#FCA5A5")
    s += body_text(420, 459, "Na: металлические свойства, 1e внешн.", 12, RED)
    s += highlight_box(410, 475, 350, 30, "#D1FAE5", "#6EE7B7")
    s += body_text(420, 494, "Cl (17): Z=17, 3 период, VIIA группа", 12, GREEN)
    s += highlight_box(410, 510, 350, 30, "#D1FAE5", "#6EE7B7")
    s += body_text(420, 529, "Cl: неметалл, 7e на внешнем уровне", 12, GREEN)
    s += highlight_box(410, 545, 160, 25, "#FEF3C7", "#FCD34D")
    s += body_text(420, 562, "Формула: e = N группы (A)", 11, ORANGE)

    s += svg_footer()
    return s


# ===== LESSON 3: Состав атома =====
def lesson3():
    s = svg_header("Состав атома")
    # Atom model large
    s += card(20, 75, 360, 310)
    s += section_title(40, 100, "Модель атома")
    # Nucleus
    s += f'  <circle cx="200" cy="260" r="35" fill="{ACCENT2}" opacity="0.25"/>\n'
    s += f'  <circle cx="200" cy="260" r="25" fill="{ACCENT2}" opacity="0.4"/>\n'
    s += f'  <circle cx="200" cy="260" r="15" fill="{ACCENT2}" opacity="0.6"/>\n'
    # Protons and neutrons in nucleus
    s += f'  <circle cx="192" cy="253" r="7" fill="{RED}" opacity="0.8"/>\n'  # proton
    s += f'  <circle cx="208" cy="253" r="7" fill="{BLUE}" opacity="0.8"/>\n'  # neutron
    s += f'  <circle cx="200" cy="267" r="7" fill="{RED}" opacity="0.8"/>\n'  # proton
    s += f'  <circle cx="192" cy="267" r="7" fill="{BLUE}" opacity="0.8"/>\n'  # neutron
    # Energy levels
    s += f'  <circle cx="200" cy="260" r="65" fill="none" stroke="{PRIMARY_LIGHT}" stroke-width="1.5" stroke-dasharray="5,3"/>\n'
    s += f'  <circle cx="200" cy="260" r="100" fill="none" stroke="{PRIMARY_LIGHT}" stroke-width="1.5" stroke-dasharray="5,3"/>\n'
    # Electrons
    s += f'  <circle cx="200" cy="195" r="6" fill="{GREEN}"/>\n'
    s += f'  <circle cx="200" cy="325" r="6" fill="{GREEN}"/>\n'
    s += f'  <circle cx="300" cy="260" r="6" fill="{GREEN}"/>\n'
    s += f'  <circle cx="100" cy="260" r="6" fill="{GREEN}"/>\n'
    # Labels
    s += body_text(200, 290, "Ядро", 12, WHITE, "middle")
    s += body_text(255, 195, "e\u207b (электрон)", 10, GREEN)
    s += body_text(130, 260, "Электронные", 10, PRIMARY_DARK)
    s += body_text(130, 273, "оболочки", 10, PRIMARY_DARK)

    # Legend for particles
    s += f'  <circle cx="55" cy="355" r="6" fill="{RED}"/>\n'
    s += body_text(68, 359, "p\u207a (протон)", 12, RED)
    s += f'  <circle cx="55" cy="375" r="6" fill="{BLUE}"/>\n'
    s += body_text(68, 379, "n\u2070 (нейтрон)", 12, BLUE)
    s += f'  <circle cx="220" cy="355" r="6" fill="{GREEN}"/>\n'
    s += body_text(233, 359, "e\u207b (электрон)", 12, GREEN)

    # Table of subatomic particles
    s += card(400, 75, 380, 310)
    s += section_title(420, 100, "Частицы атома")
    # Table header
    s += highlight_box(420, 115, 340, 28, ACCENT2, ACCENT2)
    s += body_text(440, 134, "Частица", 12, WHITE)
    s += body_text(540, 134, "Заряд", 12, WHITE)
    s += body_text(640, 134, "Масса", 12, WHITE)
    # Proton row
    s += highlight_box(420, 148, 340, 28, "#FEE2E2", "#FCA5A5")
    s += body_text(440, 167, "Протон (p)", 12, RED)
    s += body_text(540, 167, "+1", 12, RED)
    s += body_text(640, 167, "1 а.е.м.", 12, RED)
    # Neutron row
    s += highlight_box(420, 181, 340, 28, "#DBEAFE", "#93C5FD")
    s += body_text(440, 200, "Нейтрон (n)", 12, BLUE)
    s += body_text(540, 200, "0", 12, BLUE)
    s += body_text(640, 200, "1 а.е.м.", 12, BLUE)
    # Electron row
    s += highlight_box(420, 214, 340, 28, "#D1FAE5", "#6EE7B7")
    s += body_text(440, 233, "Электрон (e)", 12, GREEN)
    s += body_text(540, 233, "-1", 12, GREEN)
    s += body_text(640, 233, "1/1836", 12, GREEN)

    # Key formulas
    s += section_title(420, 265, "Ключевые формулы")
    s += highlight_box(420, 275, 340, 30, "#FEF3C7", "#FCD34D")
    s += formula_text(590, 295, "Z = число протонов = порядковый номер", 11, ORANGE)
    s += highlight_box(420, 310, 340, 30, "#EDE9FE", PRIMARY_LIGHT)
    s += formula_text(590, 330, "N = Ar - Z  (число нейтронов)", 11, PRIMARY_DARK)
    s += highlight_box(420, 345, 340, 30, "#FEE2E2", "#FCA5A5")
    s += formula_text(590, 365, "Атом электронейтрален: p\u207a = e\u207b", 11, RED)

    # Isotopes section
    s += card(20, 400, 760, 170)
    s += section_title(40, 425, "Изотопы")
    s += body_text(40, 445, "Изотопы — атомы одного элемента с разным числом нейтронов", 13, GRAY)
    # Examples
    s += highlight_box(40, 455, 220, 55, "#FEE2E2", "#FCA5A5")
    s += formula_text(150, 478, "\u00b9H (протий)", 14, RED)
    s += body_text(60, 500, "p=1, n=0", 11, GRAY)

    s += highlight_box(270, 455, 220, 55, "#FEF3C7", "#FCD34D")
    s += formula_text(380, 478, "\u00b2H (дейтерий)", 14, ORANGE)
    s += body_text(290, 500, "p=1, n=1", 11, GRAY)

    s += highlight_box(500, 455, 220, 55, "#DBEAFE", "#93C5FD")
    s += formula_text(610, 478, "\u00b3H (тритий)", 14, BLUE)
    s += body_text(520, 500, "p=1, n=2", 11, GRAY)

    s += highlight_box(40, 520, 720, 40, "#EDE9FE", PRIMARY_LIGHT)
    s += formula_text(400, 544, "Химические свойства изотопов одинаковы, физические — различаются", 12, PRIMARY_DARK)

    s += svg_footer()
    return s


# ===== LESSON 4: Строение электронной оболочки =====
def lesson4():
    s = svg_header("Строение электронной оболочки")
    # Electron configuration rules
    s += card(20, 75, 380, 200)
    s += section_title(40, 100, "Правила заполнения")
    s += highlight_box(40, 115, 340, 35, "#EDE9FE", PRIMARY_LIGHT)
    s += body_text(55, 130, "1. Принцип наименьшей энергии:", 12, PRIMARY_DARK)
    s += body_text(55, 145, "   электроны заполняют уровни от 1 к 7", 11, GRAY)
    s += highlight_box(40, 155, 340, 35, "#DBEAFE", "#93C5FD")
    s += body_text(55, 170, "2. Правило Клечковского:", 12, BLUE)
    s += body_text(55, 185, "   заполнение по (n+l), затем по n", 11, GRAY)
    s += highlight_box(40, 195, 340, 35, "#D1FAE5", "#6EE7B7")
    s += body_text(55, 210, "3. Правило Хунда:", 12, GREEN)
    s += body_text(55, 225, "   электроны заполняют ячейки по одному", 11, GRAY)
    s += highlight_box(40, 235, 340, 30, "#FEF3C7", "#FCD34D")
    s += body_text(55, 250, "4. Макс. электронов на уровне: 2n\u00b2", 12, ORANGE)

    # Energy levels table
    s += card(410, 75, 370, 200)
    s += section_title(430, 100, "Энергетические уровни")
    s += highlight_box(430, 115, 330, 25, ACCENT2, ACCENT2)
    s += body_text(445, 132, "Уровень (n)", 11, WHITE)
    s += body_text(555, 132, "Подур.", 11, WHITE)
    s += body_text(640, 132, "Макс. e", 11, WHITE)
    levels = [("1", "s", "2"), ("2", "s, p", "8"), ("3", "s, p, d", "18"), ("4", "s, p, d, f", "32"), ("5", "s, p, d, f", "32"), ("6", "s, p, d", "18"), ("7", "s, p", "8")]
    colors = [CYAN, BLUE, GREEN, ORANGE, RED, PINK, PRIMARY_DARK]
    bgs = ["#ECFEFF", "#DBEAFE", "#D1FAE5", "#FEF3C7", "#FEE2E2", "#FCE7F3", "#EDE9FE"]
    for i, (lv, sub, mx) in enumerate(levels):
        y = 145 + i * 19
        s += highlight_box(430, y, 330, 19, bgs[i], colors[i])
        s += body_text(445, y + 14, lv, 11, colors[i])
        s += body_text(555, y + 14, sub, 11, colors[i])
        s += body_text(640, y + 14, mx, 11, colors[i])

    # Electron configuration examples
    s += card(20, 285, 760, 145)
    s += section_title(40, 310, "Примеры электронных конфигураций")
    examples = [
        ("O (8)", "1s\u00b2 2s\u00b2 2p\u2074", 2, 6, "#3B82F6"),
        ("Na (11)", "1s\u00b2 2s\u00b2 2p\u2076 3s\u00b9", 2, 8, 1, "#EF4444"),
        ("Cl (17)", "1s\u00b2 2s\u00b2 2p\u2076 3s\u00b2 3p\u2075", 2, 8, 7, "#10B981"),
        ("Ca (20)", "1s\u00b2 2s\u00b2 2p\u2076 3s\u00b2 3p\u2076 4s\u00b2", 2, 8, 8, 2, "#F59E0B"),
    ]
    for i, ex in enumerate(examples):
        x = 40 + i * 185
        elem = ex[0]
        config = ex[1]
        col = ex[-1]
        s += highlight_box(x, 325, 175, 45, "#F5F3FF", PRIMARY_LIGHT)
        s += body_text(x + 10, 343, elem, 14, col)
        s += body_text(x + 10, 362, config, 9, GRAY)

    # Visual electron shell for Oxygen
    s += card(20, 440, 760, 130)
    s += section_title(40, 465, "Схема электронной оболочки O (кислород)")
    # Nucleus
    s += f'  <circle cx="400" cy="530" r="14" fill="{ACCENT2}" opacity="0.5"/>\n'
    s += body_text(400, 534, "+8", 9, WHITE, "middle")
    # Level 1
    s += f'  <circle cx="400" cy="530" r="40" fill="none" stroke="{PRIMARY_LIGHT}" stroke-width="1.5" stroke-dasharray="4,3"/>\n'
    s += f'  <circle cx="400" cy="490" r="5" fill="{CYAN}"/>\n'
    s += f'  <circle cx="400" cy="570" r="5" fill="{CYAN}"/>\n'
    s += body_text(360, 490, "2e", 10, CYAN)
    # Level 2
    s += f'  <circle cx="400" cy="530" r="80" fill="none" stroke="{PRIMARY_LIGHT}" stroke-width="1.5" stroke-dasharray="4,3"/>\n'
    import math
    for angle in range(0, 360, 60):
        ex2 = 400 + 80 * math.cos(math.radians(angle))
        ey2 = 530 + 80 * math.sin(math.radians(angle))
        s += f'  <circle cx="{ex2:.1f}" cy="{ey2:.1f}" r="4" fill="{BLUE}"/>\n'
    s += body_text(440, 470, "6e", 10, BLUE)

    # Schematic notation
    s += formula_text(140, 510, "O +8))", 18, ACCENT2)
    s += body_text(100, 535, "2e на 1 уровне", 11, CYAN)
    s += body_text(100, 555, "6e на 2 уровне", 11, BLUE)
    s += highlight_box(620, 475, 150, 70, "#FEF3C7", "#FCD34D")
    s += body_text(635, 495, "Всего электронов:", 11, ORANGE)
    s += formula_text(695, 525, "2 + 6 = 8", 16, ORANGE)

    s += svg_footer()
    return s


# ===== LESSON 5: Типы химической связи =====
def lesson5():
    s = svg_header("Типы химической связи")
    # Three main types
    # Ionic bond
    s += card(20, 75, 245, 250)
    s += highlight_box(30, 85, 225, 30, "#FEE2E2", RED)
    s += section_title(45, 105, "Ионная связь", RED, 14)
    s += body_text(35, 130, "Металл + Неметалл", 11, GRAY)
    s += body_text(35, 148, "Передача электронов", 11, GRAY)
    # Diagram: Na + Cl
    s += f'  <circle cx="90" cy="190" r="25" fill="#FEE2E2" stroke="{RED}" stroke-width="1.5"/>\n'
    s += body_text(90, 194, "Na\u207a", 14, RED, "middle")
    s += f'  <circle cx="195" cy="190" r="25" fill="#D1FAE5" stroke="{GREEN}" stroke-width="1.5"/>\n'
    s += body_text(195, 194, "Cl\u207b", 14, GREEN, "middle")
    # Arrow for electron transfer
    s += f'  <line x1="120" y1="185" x2="165" y2="185" stroke="{ORANGE}" stroke-width="2"/>\n'
    s += body_text(143, 178, "e\u207b", 10, ORANGE, "middle")
    # Formula
    s += formula_text(142, 245, "NaCl", 18, ACCENT2)
    s += body_text(35, 270, "Примеры: NaCl, KBr, CaO", 10, GRAY)

    # Covalent bond
    s += card(275, 75, 245, 250)
    s += highlight_box(285, 85, 225, 30, "#D1FAE5", GREEN)
    s += section_title(300, 105, "Ковалентная связь", GREEN, 14)
    s += body_text(285, 130, "Неметалл + Неметалл", 11, GRAY)
    s += body_text(285, 148, "Общий электронный пар", 11, GRAY)
    # Diagram: Cl-Cl
    s += f'  <circle cx="355" cy="190" r="25" fill="#D1FAE5" stroke="{GREEN}" stroke-width="1.5"/>\n'
    s += body_text(355, 194, "Cl", 14, GREEN, "middle")
    s += f'  <circle cx="440" cy="190" r="25" fill="#D1FAE5" stroke="{GREEN}" stroke-width="1.5"/>\n'
    s += body_text(440, 194, "Cl", 14, GREEN, "middle")
    # Shared electron pair
    s += f'  <circle cx="394" cy="183" r="4" fill="{BLUE}"/>\n'
    s += f'  <circle cx="401" cy="183" r="4" fill="{BLUE}"/>\n'
    s += body_text(397, 210, "общая пара", 9, BLUE, "middle")
    # Formula
    s += formula_text(397, 245, "Cl\u2082", 18, ACCENT2)
    s += body_text(285, 270, "Примеры: H\u2082O, CO\u2082, NH\u2083", 10, GRAY)
    # Nonpolar vs Polar
    s += highlight_box(285, 280, 225, 35, "#EDE9FE", PRIMARY_LIGHT)
    s += body_text(295, 296, "Неполярная: H\u2082, O\u2082, N\u2082", 10, PRIMARY_DARK)
    s += body_text(295, 310, "Полярная: HCl, H\u2082O, SO\u2082", 10, PRIMARY_DARK)

    # Metallic bond
    s += card(530, 75, 250, 250)
    s += highlight_box(540, 85, 230, 30, "#DBEAFE", BLUE)
    s += section_title(555, 105, "Металлическая связь", BLUE, 14)
    s += body_text(540, 130, "Металл + Металл", 11, GRAY)
    s += body_text(540, 148, "Общие электроны (электронный газ)", 11, GRAY)
    # Metal lattice diagram
    for mx in [590, 640, 690]:
        for my in [185, 225, 265]:
            s += f'  <circle cx="{mx}" cy="{my}" r="10" fill="#DBEAFE" stroke="{BLUE}" stroke-width="1.5"/>\n'
            s += body_text(mx, my + 4, "+", 10, BLUE, "middle")
    # Electron cloud dots
    for pos in [(605, 195), (655, 210), (670, 245), (610, 255), (630, 200), (650, 250), (600, 240), (680, 190), (595, 270)]:
        s += f'  <circle cx="{pos[0]}" cy="{pos[1]}" r="3" fill="{ORANGE}" opacity="0.7"/>\n'
    s += body_text(540, 300, "Примеры: Fe, Cu, Al, Na", 10, GRAY)

    # Comparison table
    s += card(20, 340, 760, 230)
    s += section_title(40, 365, "Сравнительная характеристика типов связи")
    # Table header
    s += highlight_box(40, 380, 720, 25, ACCENT2, ACCENT2)
    s += body_text(60, 397, "Свойство", 11, WHITE)
    s += body_text(210, 397, "Ионная", 11, WHITE)
    s += body_text(400, 397, "Ковалентная", 11, WHITE)
    s += body_text(620, 397, "Металлическая", 11, WHITE)
    # Rows
    props = [
        ("Образуется между", "Ме + НеМе", "НеМе + НеМе", "Ме + Ме"),
        ("Механизм", "Передача e\u207b", "Обобщение e\u207b", "Обобщение e\u207b"),
        ("Частицы", "Ионы", "Молекулы / атомы", "Ионы + e\u207b газ"),
        ("Твёрдость", "Твёрдые", "Разная", "Разная"),
        ("Электропровод.", "Расплавы, р-ры", "Нет / слабая", "Высокая"),
        ("Пример", "NaCl, CaO", "H\u2082O, CO\u2082", "Fe, Cu, Al"),
    ]
    colors_list = ["#FEE2E2", "#FFFFFF", "#D1FAE5", "#FFFFFF", "#DBEAFE", "#FFFFFF"]
    for i, (prop, ionic, covalent, metallic) in enumerate(props):
        y = 410 + i * 25
        s += highlight_box(40, y, 720, 25, colors_list[i], colors_list[i])
        s += body_text(60, y + 17, prop, 11, BLACK)
        s += body_text(210, y + 17, ionic, 11, RED)
        s += body_text(400, y + 17, covalent, 11, GREEN)
        s += body_text(620, y + 17, metallic, 11, BLUE)

    s += svg_footer()
    return s


# ===== LESSON 6: Электроотрицательность =====
def lesson6():
    s = svg_header("Электроотрицательность")
    # Definition
    s += card(20, 75, 760, 80)
    s += section_title(40, 100, "Определение")
    s += body_text(40, 120, "Электроотрицательность (ЭО) — способность атома притягивать к себе", 13, GRAY)
    s += body_text(40, 136, "электронную плотность при образовании химической связи.", 13, GRAY)
    s += formula_text(400, 150, "Шкала Полинга (1960)", 14, ACCENT2)

    # Periodic table with electronegativity values
    s += card(20, 165, 420, 260)
    s += section_title(40, 190, "Значения ЭО (шкала Полинга)")
    # Row of elements with EO values
    elements_eo = [
        ("H", "2,1", "#D1FAE5", GREEN),
        ("Li", "1,0", "#FEE2E2", RED),
        ("Be", "1,5", "#FEE2E2", RED),
        ("B", "2,0", "#D1FAE5", GREEN),
        ("C", "2,5", "#D1FAE5", GREEN),
        ("N", "3,0", "#D1FAE5", GREEN),
        ("O", "3,5", "#DBEAFE", BLUE),
        ("F", "4,0", "#DBEAFE", BLUE),
    ]
    for i, (sym, eo, bg, col) in enumerate(elements_eo):
        x = 40 + i * 48
        y = 210
        s += highlight_box(x, y, 44, 50, bg, col)
        s += body_text(x + 22, y + 18, sym, 13, col, "middle")
        s += body_text(x + 22, y + 35, eo, 10, GRAY, "middle")

    # Second row
    elements_eo2 = [
        ("Na", "0,9", "#FEE2E2", RED),
        ("Mg", "1,2", "#FEE2E2", RED),
        ("Al", "1,5", "#FEF3C7", ORANGE),
        ("Si", "1,8", "#D1FAE5", GREEN),
        ("P", "2,1", "#D1FAE5", GREEN),
        ("S", "2,5", "#D1FAE5", GREEN),
        ("Cl", "3,0", "#DBEAFE", BLUE),
    ]
    for i, (sym, eo, bg, col) in enumerate(elements_eo2):
        x = 40 + i * 48
        y = 270
        s += highlight_box(x, y, 44, 50, bg, col)
        s += body_text(x + 22, y + 18, sym, 12, col, "middle")
        s += body_text(x + 22, y + 35, eo, 10, GRAY, "middle")

    # Color legend
    s += body_text(40, 340, "Мин. ЭО", 10, RED)
    s += body_text(40, 355, "Ме: 0,7-1,5", 10, GRAY)
    s += body_text(150, 340, "Средн. ЭО", 10, GREEN)
    s += body_text(150, 355, "НеМе: 2,0-2,5", 10, GRAY)
    s += body_text(280, 340, "Макс. ЭО", 10, BLUE)
    s += body_text(280, 355, "Галогены: 3,0-4,0", 10, GRAY)

    # Trends card
    s += card(450, 165, 330, 260)
    s += section_title(470, 190, "Закономерности ЭО")
    # Arrow diagram for period
    s += highlight_box(470, 205, 290, 55, "#EDE9FE", PRIMARY_LIGHT)
    s += body_text(485, 225, "В периоде (вправо):", 12, PRIMARY_DARK)
    s += body_text(485, 245, "ЭО увеличивается \u2192", 12, BLUE)
    # Arrow diagram for group
    s += highlight_box(470, 270, 290, 55, "#EDE9FE", PRIMARY_LIGHT)
    s += body_text(485, 290, "В группе (вниз):", 12, PRIMARY_DARK)
    s += body_text(485, 310, "ЭО уменьшается \u2193", 12, RED)

    # Most/least electronegative
    s += highlight_box(470, 335, 140, 55, "#DBEAFE", BLUE)
    s += body_text(485, 355, "Макс. ЭО:", 10, BLUE)
    s += formula_text(540, 378, "F = 4,0", 14, BLUE)
    s += highlight_box(620, 335, 140, 55, "#FEE2E2", RED)
    s += body_text(635, 355, "Мин. ЭО:", 10, RED)
    s += formula_text(690, 378, "Fr = 0,7", 14, RED)

    # Application
    s += card(20, 435, 760, 135)
    s += section_title(40, 460, "Применение ЭО")
    s += highlight_box(40, 475, 350, 45, "#D1FAE5", GREEN)
    s += body_text(55, 495, "Ковалентная полярная связь:", 12, GREEN)
    s += body_text(55, 510, "Разность ЭО 0,4 - 1,7", 11, GRAY)
    s += body_text(55, 524, "Пример: H-Cl (\u0394\u03a7 = 0,9)", 11, GRAY)

    s += highlight_box(410, 475, 350, 45, "#FEE2E2", RED)
    s += body_text(425, 495, "Ионная связь:", 12, RED)
    s += body_text(425, 510, "Разность ЭО > 1,7", 11, GRAY)
    s += body_text(425, 524, "Пример: Na-Cl (\u0394\u03a7 = 2,1)", 11, GRAY)

    s += highlight_box(40, 530, 720, 30, "#FEF3C7", "#FCD34D")
    s += formula_text(400, 550, "\u0394\u03a7 = ЭО(А) - ЭО(Б) — разность электроотрицательностей", 12, ORANGE)

    s += svg_footer()
    return s


# ===== LESSON 7: Типы химических реакций =====
def lesson7():
    s = svg_header("Типы химических реакций")
    # Four types in 2x2 grid
    # 1. Combination (Соединение)
    s += card(20, 75, 375, 155)
    s += highlight_box(30, 85, 355, 28, "#D1FAE5", GREEN)
    s += section_title(45, 104, "1. Реакция соединения", GREEN, 14)
    s += body_text(40, 128, "Два и более веществ \u2192 одно новое", 12, GRAY)
    s += formula_text(207, 152, "A + B \u2192 AB", 16, GREEN)
    s += body_text(40, 175, "2Mg + O\u2082 \u2192 2MgO", 13, ACCENT2)
    s += body_text(40, 192, "2H\u2082 + O\u2082 \u2192 2H\u2082O", 13, ACCENT2)
    s += body_text(40, 209, "CaO + H\u2082O \u2192 Ca(OH)\u2082", 13, ACCENT2)

    # 2. Decomposition (Разложение)
    s += card(405, 75, 375, 155)
    s += highlight_box(415, 85, 355, 28, "#FEE2E2", RED)
    s += section_title(430, 104, "2. Реакция разложения", RED, 14)
    s += body_text(420, 128, "Одно вещество \u2192 два и более", 12, GRAY)
    s += formula_text(592, 152, "AB \u2192 A + B", 16, RED)
    s += body_text(420, 175, "2H\u2082O \u2192 2H\u2082 + O\u2082", 13, ACCENT2)
    s += body_text(420, 192, "CaCO\u2083 \u2192 CaO + CO\u2082", 13, ACCENT2)
    s += body_text(420, 209, "2KMnO\u2084 \u2192 K\u2082MnO\u2084 + MnO\u2082 + O\u2082", 13, ACCENT2)

    # 3. Replacement (Замещение)
    s += card(20, 240, 375, 155)
    s += highlight_box(30, 250, 355, 28, "#DBEAFE", BLUE)
    s += section_title(45, 269, "3. Реакция замещения", BLUE, 14)
    s += body_text(40, 293, "Атом замещает атом в соединении", 12, GRAY)
    s += formula_text(207, 317, "A + BC \u2192 AC + B", 16, BLUE)
    s += body_text(40, 340, "Zn + 2HCl \u2192 ZnCl\u2082 + H\u2082", 13, ACCENT2)
    s += body_text(40, 357, "Fe + CuSO\u2084 \u2192 FeSO\u2084 + Cu", 13, ACCENT2)
    s += body_text(40, 374, "2Na + 2H\u2082O \u2192 2NaOH + H\u2082", 13, ACCENT2)

    # 4. Exchange (Обмен)
    s += card(405, 240, 375, 155)
    s += highlight_box(415, 250, 355, 28, "#FEF3C7", ORANGE)
    s += section_title(430, 269, "4. Реакция обмена", ORANGE, 14)
    s += body_text(420, 293, "Обмен составными частями", 12, GRAY)
    s += formula_text(592, 317, "AB + CD \u2192 AD + CB", 16, ORANGE)
    s += body_text(420, 340, "NaOH + HCl \u2192 NaCl + H\u2082O", 13, ACCENT2)
    s += body_text(420, 357, "BaCl\u2082 + Na\u2082SO\u2084 \u2192 BaSO\u2084 + 2NaCl", 13, ACCENT2)
    s += body_text(420, 374, "AgNO\u2083 + NaCl \u2192 AgCl + NaNO\u2083", 13, ACCENT2)

    # Classification summary
    s += card(20, 405, 760, 165)
    s += section_title(40, 430, "Классификация реакций")
    # By number of substances
    s += highlight_box(40, 445, 230, 50, "#EDE9FE", PRIMARY_LIGHT)
    s += body_text(55, 462, "По числу веществ:", 12, PRIMARY_DARK)
    s += body_text(55, 478, "Обратимые \u21cc", 11, PRIMARY_DARK)
    s += body_text(55, 492, "Необратимые \u2192", 11, PRIMARY_DARK)

    # By heat
    s += highlight_box(285, 445, 230, 50, "#FEE2E2", "#FCA5A5")
    s += body_text(300, 462, "По тепловому эффекту:", 12, RED)
    s += body_text(300, 478, "Экзотермические (+Q)", 11, RED)
    s += body_text(300, 492, "Эндотермические (-Q)", 11, BLUE)

    # By phase
    s += highlight_box(530, 445, 230, 50, "#D1FAE5", "#6EE7B7")
    s += body_text(545, 462, "По фазовому составу:", 12, GREEN)
    s += body_text(545, 478, "Гомогенные (одна фаза)", 11, GREEN)
    s += body_text(545, 492, "Гетерогенные (неск. фаз)", 11, GREEN)

    # By catalyst
    s += highlight_box(40, 505, 350, 50, "#DBEAFE", "#93C5FD")
    s += body_text(55, 522, "По участию катализатора:", 12, BLUE)
    s += body_text(55, 538, "Каталитические / Некаталитические", 11, BLUE)

    # By redox
    s += highlight_box(410, 505, 350, 50, "#FEF3C7", "#FCD34D")
    s += body_text(425, 522, "По изменению степ. окисления:", 12, ORANGE)
    s += body_text(425, 538, "Окислительно-восстановительные / Без изменений", 11, ORANGE)

    s += svg_footer()
    return s


# ===== LESSON 8: Окислительно-восстановительные реакции =====
def lesson8():
    s = svg_header("Окислительно-восстановительные реакции")
    # Definitions
    s += card(20, 75, 760, 100)
    s += section_title(40, 100, "Основные понятия")
    s += highlight_box(40, 112, 360, 55, "#FEE2E2", RED)
    s += body_text(55, 130, "Окислитель — принимает электроны", 12, RED)
    s += body_text(55, 148, "(степень окисления понижается)", 11, GRAY)

    s += highlight_box(415, 112, 350, 55, "#D1FAE5", GREEN)
    s += body_text(430, 130, "Восстановитель — отдаёт электроны", 12, GREEN)
    s += body_text(430, 148, "(степень окисления повышается)", 11, GRAY)

    s += formula_text(400, 178, "Окислитель + e\u207b \u2192 восстановление    |    Восстановитель - e\u207b \u2192 окисление", 12, ACCENT2)

    # Oxidation number rules
    s += card(20, 185, 380, 200)
    s += section_title(40, 210, "Степень окисления (правила)")
    rules = [
        "Элементы: с.о. = 0 (Na, O\u2082, Cl\u2082)",
        "H: +1 (кроме гидридов: -1)",
        "O: -2 (кроме пероксидов: -1, OF\u2082)",
        "Щелочные металлы (IA): +1",
        "Щёлочноземельные (IIA): +2",
        "Al: +3, F: -1",
        "Сумма с.о. в молекуле = 0",
    ]
    colors_r = [GRAY, BLUE, RED, ORANGE, GREEN, CYAN, ACCENT2]
    for i, rule in enumerate(rules):
        y = 230 + i * 22
        s += body_text(45, y, f"{i+1}. {rule}", 11, colors_r[i])

    # Example: Fe2O3 + CO
    s += card(410, 185, 370, 200)
    s += section_title(430, 210, "Пример: Fe\u2082O\u2083 + CO")
    # Show oxidation states
    s += body_text(430, 235, "Fe\u2082\u207a\u00b3O\u2083\u207b\u00b2  +  C\u207a\u00b2O\u207b\u00b2  \u2192  Fe\u2070  +  C\u207a\u2074O\u2082\u207b\u00b2", 13, ACCENT2)
    s += highlight_box(430, 250, 165, 55, "#D1FAE5", GREEN)
    s += body_text(445, 268, "Восстановитель: C\u207a\u00b2 \u2192 C\u207a\u2074", 11, GREEN)
    s += body_text(445, 284, "C\u207a\u00b2 - 2e\u207b \u2192 C\u207a\u2074 (окисление)", 11, GREEN)

    s += highlight_box(605, 250, 165, 55, "#FEE2E2", RED)
    s += body_text(620, 268, "Окислитель: Fe\u207a\u00b3 \u2192 Fe\u2070", 11, RED)
    s += body_text(620, 284, "Fe\u207a\u00b3 + 3e\u207b \u2192 Fe\u2070 (восст.)", 11, RED)

    # Electron balance
    s += highlight_box(430, 315, 340, 50, "#FEF3C7", "#FCD34D")
    s += body_text(445, 335, "Электронный баланс:", 12, ORANGE)
    s += body_text(445, 353, "Fe\u207a\u00b3 + 3e\u207b \u2192 Fe\u2070  | x2", 11, ORANGE)
    s += body_text(445, 367, "C\u207a\u00b2 - 2e\u207b \u2192 C\u207a\u2074  | x3", 11, ORANGE)

    # Second example: MnO2 + HCl
    s += card(20, 395, 760, 175)
    s += section_title(40, 420, "Пример: MnO\u2082 + HCl")
    s += formula_text(400, 448, "MnO\u2082 + 4HCl \u2192 MnCl\u2082 + Cl\u2082 + 2H\u2082O", 15, ACCENT2)
    s += highlight_box(40, 460, 350, 50, "#D1FAE5", GREEN)
    s += body_text(55, 478, "Восстановитель: Cl\u207b \u2192 Cl\u2070", 12, GREEN)
    s += body_text(55, 496, "2Cl\u207b - 2e\u207b \u2192 Cl\u2082\u2070 (окисление)", 11, GREEN)
    s += highlight_box(410, 460, 350, 50, "#FEE2E2", RED)
    s += body_text(425, 478, "Окислитель: Mn\u207a\u2074 \u2192 Mn\u207a\u00b2", 12, RED)
    s += body_text(425, 496, "Mn\u207a\u2074 + 2e\u207b \u2192 Mn\u207a\u00b2 (восстановление)", 11, RED)

    # Mnemonic
    s += highlight_box(40, 520, 720, 40, "#EDE9FE", PRIMARY_LIGHT)
    s += formula_text(400, 544, "Запомни: Окислитель ВОССТАНАВЛИВАЕТСЯ, Восстановитель ОКИСЛЯЕТСЯ!", 13, PRIMARY_DARK)

    s += svg_footer()
    return s


# ===== LESSON 9: Оксиды =====
def lesson9():
    s = svg_header("Оксиды")
    # Definition
    s += card(20, 75, 760, 55)
    s += section_title(40, 97, "Оксиды — сложные вещества, состоящие из двух элементов, один из которых кислород (O) со с.о. -2")
    s += formula_text(400, 120, "Общая формула: E\u2093O\u1d67", 14, ACCENT2)

    # Three types
    # Acidic oxides
    s += card(20, 140, 245, 210)
    s += highlight_box(30, 150, 225, 28, "#DBEAFE", BLUE)
    s += section_title(45, 168, "Кислотные оксиды", BLUE, 13)
    s += body_text(35, 195, "Образованы неметаллами", 11, GRAY)
    s += body_text(35, 212, "Соответствуют кислотам", 11, GRAY)
    s += body_text(35, 230, " + H\u2082O \u2192 кислота", 12, BLUE)
    s += body_text(35, 248, " + щёлочь \u2192 соль + H\u2082O", 12, BLUE)
    # Examples
    s += highlight_box(35, 260, 215, 80, "#DBEAFE", "#93C5FD")
    s += formula_text(142, 280, "SO\u2083 + H\u2082O \u2192 H\u2082SO\u2084", 11, BLUE)
    s += formula_text(142, 298, "CO\u2082 + H\u2082O \u2192 H\u2082CO\u2083", 11, BLUE)
    s += formula_text(142, 316, "P\u2082O\u2085 + H\u2082O \u2192 H\u2083PO\u2084", 11, BLUE)
    s += body_text(35, 338, "SO\u2083, CO\u2082, SiO\u2082, P\u2082O\u2085, NO\u2082", 10, GRAY)

    # Basic oxides
    s += card(275, 140, 245, 210)
    s += highlight_box(285, 150, 225, 28, "#FEE2E2", RED)
    s += section_title(300, 168, "Основные оксиды", RED, 13)
    s += body_text(285, 195, "Образованы металлами", 11, GRAY)
    s += body_text(285, 212, "Соответствуют основаниям", 11, GRAY)
    s += body_text(285, 230, " + H\u2082O \u2192 основание", 12, RED)
    s += body_text(285, 248, " + кислота \u2192 соль + H\u2082O", 12, RED)
    s += highlight_box(285, 260, 215, 80, "#FEE2E2", "#FCA5A5")
    s += formula_text(392, 280, "CaO + H\u2082O \u2192 Ca(OH)\u2082", 11, RED)
    s += formula_text(392, 298, "Na\u2082O + H\u2082O \u2192 2NaOH", 11, RED)
    s += formula_text(392, 316, "CuO + 2HCl \u2192 CuCl\u2082 + H\u2082O", 10, RED)
    s += body_text(285, 338, "CaO, Na\u2082O, K\u2082O, MgO, CuO", 10, GRAY)

    # Amphoteric oxides
    s += card(530, 140, 250, 210)
    s += highlight_box(540, 150, 230, 28, "#FEF3C7", ORANGE)
    s += section_title(555, 168, "Амфотерные оксиды", ORANGE, 13)
    s += body_text(540, 195, "Обладают двойственными", 11, GRAY)
    s += body_text(540, 212, "свойствами", 11, GRAY)
    s += body_text(540, 230, " + кислота \u2192 соль + H\u2082O", 12, ORANGE)
    s += body_text(540, 248, " + щёлочь \u2192 соль + H\u2082O", 12, ORANGE)
    s += highlight_box(540, 260, 230, 80, "#FEF3C7", "#FCD34D")
    s += formula_text(655, 280, "ZnO + 2HCl \u2192 ZnCl\u2082 + H\u2082O", 10, ORANGE)
    s += formula_text(655, 298, "ZnO + 2NaOH \u2192 Na\u2082ZnO\u2082 + H\u2082O", 9, ORANGE)
    s += body_text(540, 338, "ZnO, Al\u2082O\u2083, Cr\u2082O\u2083, BeO", 10, GRAY)

    # Naming and properties
    s += card(20, 360, 760, 210)
    s += section_title(40, 385, "Номенклатура оксидов")
    s += highlight_box(40, 400, 350, 70, "#EDE9FE", PRIMARY_LIGHT)
    s += body_text(55, 420, "Название: \"Оксид\" + элемент (в род. падеже)", 12, PRIMARY_DARK)
    s += body_text(55, 438, "Если несколько с.о. — указать римскую цифру:", 11, GRAY)
    s += body_text(55, 456, "FeO — оксид железа(II)", 12, ACCENT2)
    s += body_text(55, 470, "Fe\u2082O\u2083 — оксид железа(III)", 12, ACCENT2)

    s += highlight_box(410, 400, 350, 70, "#D1FAE5", "#6EE7B7")
    s += body_text(425, 420, "Получение оксидов:", 12, GREEN)
    s += body_text(425, 438, "1. Горение: 2Mg + O\u2082 \u2192 2MgO", 11, ACCENT2)
    s += body_text(425, 456, "2. Разложение: CaCO\u2083 \u2192 CaO + CO\u2082", 11, ACCENT2)
    s += body_text(425, 470, "3. Окисление: 2Zn + O\u2082 \u2192 2ZnO", 11, ACCENT2)

    # Key property
    s += highlight_box(40, 480, 720, 80, "#FEF3C7", "#FCD34D")
    s += section_title(60, 502, "Ключевое свойство:", ORANGE, 14)
    s += body_text(60, 522, "Кислотный оксид + Основный оксид \u2192 Соль", 13, ACCENT2)
    s += formula_text(400, 548, "CaO + SiO\u2082 \u2192 CaSiO\u2083 (силикат кальция)", 14, ACCENT2)

    s += svg_footer()
    return s


# ===== LESSON 10: Кислоты, основания, соли =====
def lesson10():
    s = svg_header("Кислоты, основания, соли")
    # Three columns
    # Acids
    s += card(20, 75, 245, 280)
    s += highlight_box(30, 85, 225, 28, "#FEE2E2", RED)
    s += section_title(55, 103, "КИСЛОТЫ", RED, 16)
    s += body_text(35, 128, "Содержат H\u207a и кислотный остаток", 11, GRAY)
    s += formula_text(142, 150, "Общ. ф-ла: H\u2099A", 13, RED)
    # Examples
    s += highlight_box(35, 162, 215, 120, "#FEE2E2", "#FCA5A5")
    s += body_text(45, 180, "HCl — соляная", 12, RED)
    s += body_text(45, 198, "H\u2082SO\u2084 — серная", 12, RED)
    s += body_text(45, 216, "HNO\u2083 — азотная", 12, RED)
    s += body_text(45, 234, "H\u2083PO\u2084 — фосфорная", 12, RED)
    s += body_text(45, 252, "H\u2082CO\u2083 — угольная", 12, RED)
    s += body_text(45, 270, "CH\u2083COOH — уксусная", 12, RED)
    # Properties
    s += body_text(35, 295, "pH < 7, лакмус \u2192 красный", 11, RED)
    s += body_text(35, 312, "Me + кислота \u2192 соль + H\u2082", 11, RED)
    s += body_text(35, 329, "осн. оксид + к-та \u2192 соль + H\u2082O", 10, RED)

    # Bases
    s += card(275, 75, 245, 280)
    s += highlight_box(285, 85, 225, 28, "#DBEAFE", BLUE)
    s += section_title(310, 103, "ОСНОВАНИЯ", BLUE, 16)
    s += body_text(285, 128, "Содержат Me\u207f\u207a и OH\u207b (гидроксид)", 11, GRAY)
    s += formula_text(397, 150, "Общ. ф-ла: Me(OH)\u2099", 13, BLUE)
    # Examples
    s += highlight_box(285, 162, 215, 100, "#DBEAFE", "#93C5FD")
    s += body_text(295, 180, "NaOH — гидроксид натрия", 11, BLUE)
    s += body_text(295, 198, "Ca(OH)\u2082 — гашёная известь", 11, BLUE)
    s += body_text(295, 216, "KOH — гидроксид калия", 11, BLUE)
    s += body_text(295, 234, "Fe(OH)\u2083 — нерастворимое", 11, BLUE)
    # Solubility
    s += body_text(285, 256, "Растворимые (щёлочи): NaOH, KOH", 10, GREEN)
    s += body_text(285, 272, "Нерастворимые: Cu(OH)\u2082, Fe(OH)\u2083", 10, ORANGE)
    s += body_text(285, 295, "pH > 7, лакмус \u2192 синий", 11, BLUE)
    s += body_text(285, 312, "к-та + основание \u2192 соль + H\u2082O", 10, BLUE)
    s += body_text(285, 329, "осн. оксид + H\u2082O \u2192 основание", 10, BLUE)

    # Salts
    s += card(530, 75, 250, 280)
    s += highlight_box(540, 85, 230, 28, "#D1FAE5", GREEN)
    s += section_title(565, 103, "СОЛИ", GREEN, 16)
    s += body_text(535, 128, "Me\u207f\u207a + кислотный остаток", 11, GRAY)
    s += formula_text(655, 150, "Общ. ф-ла: Me\u2099A\u2098", 13, GREEN)
    # Examples
    s += highlight_box(535, 162, 230, 120, "#D1FAE5", "#6EE7B7")
    s += body_text(545, 180, "NaCl — поваренная соль", 11, GREEN)
    s += body_text(545, 198, "CaCO\u2083 — мел, мрамор", 11, GREEN)
    s += body_text(545, 216, "CuSO\u2084 — медный купорос", 11, GREEN)
    s += body_text(545, 234, "Na\u2082SO\u2084 — сульфат натрия", 11, GREEN)
    s += body_text(545, 252, "KNO\u2083 — селитра", 11, GREEN)
    s += body_text(545, 270, "Ca\u2083(PO\u2084)\u2082 — фосфат кальция", 11, GREEN)
    # Types
    s += body_text(535, 295, "Средние: Na\u2082SO\u2084", 10, GREEN)
    s += body_text(535, 312, "Кислые: NaHSO\u2084", 10, GREEN)
    s += body_text(535, 329, "Основные: (CuOH)\u2082CO\u2083", 10, GREEN)

    # pH scale
    s += card(20, 365, 760, 80)
    s += section_title(40, 390, "Шкала pH")
    # pH bar
    import math
    for i in range(14):
        x = 60 + i * 50
        # Color gradient from red to green to blue
        if i < 4:
            r, g, b = 239, 68, 68  # Red
        elif i < 6:
            r, g, b = 245, 158, 11  # Orange
        elif i == 7:
            r, g, b = 16, 185, 129  # Green
        elif i < 10:
            r, g, b = 59, 130, 246  # Blue
        else:
            r, g, b = 109, 40, 217  # Purple
        color = f"#{r:02x}{g:02x}{b:02x}"
        s += f'  <rect x="{x}" y="405" width="46" height="22" fill="{color}" rx="3"/>\n'
        s += body_text(x + 23, 438, str(i), 11, color, "middle")
    # Labels
    s += body_text(80, 398, "Кислая среда", 10, RED)
    s += body_text(410, 398, "Нейтральная", 10, GREEN)
    s += body_text(700, 398, "Щелочная", 10, BLUE)

    # Reaction summary
    s += card(20, 455, 760, 115)
    s += section_title(40, 480, "Взаимосвязь: Кислоты \u2194 Основания \u2194 Соли")
    # Reaction arrows
    s += highlight_box(40, 495, 230, 30, "#FEE2E2", "#FCA5A5")
    s += body_text(55, 515, "Кислота + Основание \u2192 Соль + H\u2082O", 11, RED)

    s += highlight_box(280, 495, 230, 30, "#DBEAFE", "#93C5FD")
    s += body_text(295, 515, "Основание + Кисл. оксид \u2192 Соль + H\u2082O", 11, BLUE)

    s += highlight_box(520, 495, 240, 30, "#D1FAE5", "#6EE7B7")
    s += body_text(535, 515, "Кислота + Основн. оксид \u2192 Соль + H\u2082O", 11, GREEN)

    # Neutralization
    s += highlight_box(40, 535, 720, 30, "#FEF3C7", "#FCD34D")
    s += formula_text(400, 555, "Реакция нейтрализации: HCl + NaOH \u2192 NaCl + H\u2082O", 14, ORANGE)

    s += svg_footer()
    return s


# ===== Generate all files =====
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

lesson_names = [
    "Периодический закон Д.И. Менделеева",
    "Характеристика элемента по положению в таблице",
    "Состав атома",
    "Строение электронной оболочки",
    "Типы химической связи",
    "Электроотрицательность",
    "Типы химических реакций",
    "Окислительно-восстановительные реакции",
    "Оксиды",
    "Кислоты, основания, соли",
]

print("=" * 60)
print("Generating Grade 8 Chemistry SVG files")
print("=" * 60)

success = 0
errors = []

for n, gen_func in generators:
    filepath = os.path.join(BASE_DIR, f"lesson-{n}.svg")
    try:
        svg_content = gen_func()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)
        size = os.path.getsize(filepath)
        print(f"  [OK] lesson-{n}.svg ({size:,} bytes) — {lesson_names[n-1]}")
        success += 1
    except Exception as e:
        print(f"  [ERROR] lesson-{n}.svg — {e}")
        errors.append((n, str(e)))

print()
print(f"Results: {success}/10 files generated successfully")
if errors:
    print("Errors:")
    for n, err in errors:
        print(f"  Lesson {n}: {err}")
print(f"Output directory: {BASE_DIR}")
