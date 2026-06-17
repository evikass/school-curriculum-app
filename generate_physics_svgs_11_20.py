#!/usr/bin/env python3
"""Generate SVG illustrations for Physics Grade 10, Lessons 11-20 (Динамика)
with real visual elements: force diagrams, vectors, springs, friction, etc.
"""

import os

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app-site/public/images/lessons/grade10/physics"
os.makedirs(OUTPUT_DIR, exist_ok=True)

C_PRIMARY = "#1565C0"
C_LIGHT = "#E3F2FD"
C_RED = "#E53935"
C_GREEN = "#2E7D32"
C_ORANGE = "#F57C00"
C_PURPLE = "#7B1FA2"

def header(title, subtitle):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#E3F2FD"/>
      <stop offset="100%" stop-color="#FFFFFF"/>
    </linearGradient>
    <linearGradient id="panel" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#1565C0"/>
      <stop offset="100%" stop-color="#1976D2"/>
    </linearGradient>
  </defs>
  <rect width="500" height="350" fill="url(#bg)" rx="10"/>
  <rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#1565C0" stroke-width="2.5"/>
  <text x="250" y="28" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1565C0" text-anchor="middle">{title}</text>
  <text x="250" y="44" font-family="Arial,sans-serif" font-size="10" fill="#888" text-anchor="middle">{subtitle}</text>
  <line x1="30" y1="52" x2="470" y2="52" stroke="#1565C0" stroke-width="1.5" opacity="0.25"/>
  <clipPath id="ill"><rect x="15" y="56" width="470" height="238" rx="6"/></clipPath>
  <g clip-path="url(#ill)">
    <rect x="15" y="56" width="470" height="238" fill="#E3F2FD" opacity="0.4"/>
'''

def footer(section="Динамика", num=11):
    return f'''
  </g>
  <rect x="12" y="298" width="476" height="42" rx="5" fill="url(#panel)"/>
  <text x="250" y="316" font-family="Arial,sans-serif" font-size="14" text-anchor="middle" fill="white" font-weight="bold">{section}</text>
  <text x="250" y="332" font-family="Arial,sans-serif" font-size="10" text-anchor="middle" fill="white" opacity="0.8">Урок {num}</text>
</svg>'''

def draw_arrow(x1, y1, x2, y2, color="#1565C0", width=2, head=8):
    import math
    dx, dy = x2-x1, y2-y1
    length = math.sqrt(dx*dx + dy*dy)
    if length < 1: return ""
    ux, uy = dx/length, dy/length
    px, py = -uy, ux
    lx, ly = x2-ux*head+px*head*0.4, y2-uy*head+py*head*0.4
    rx, ry = x2-ux*head-px*head*0.4, y2-uy*head-py*head*0.4
    return f'''<line x1="{x1}" y1="{y1}" x2="{x2-head*0.5*ux}" y2="{y2-head*0.5*uy}" stroke="{color}" stroke-width="{width}"/>
    <polygon points="{x2},{y2} {lx},{ly} {rx},{ry}" fill="{color}"/>'''


# ============================================================
# LESSON 11: Инерция. Первый закон Ньютона
# ============================================================
def lesson11():
    svg = header("Инерция. Первый закон Ньютона", "Физика 10 класс — Урок 11")
    svg += '''
    <!-- Galileo experiment: inclined planes -->
    <rect x="25" y="62" width="225" height="130" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Опыт Галилея</text>

    <!-- Left ramp -->
    <line x1="40" y1="170" x2="100" y2="110" stroke="#795548" stroke-width="2.5"/>
    <!-- Right ramp - different angles -->
    <line x1="100" y1="170" x2="150" y2="120" stroke="#795548" stroke-width="2.5"/>
    <!-- Flat extension -->
    <line x1="150" y1="120" x2="240" y2="120" stroke="#795548" stroke-width="1.5" stroke-dasharray="4,2"/>

    <!-- Ball on left ramp -->
    <circle cx="72" cy="137" r="6" fill="#E53935"/>
    <!-- Ball rolling up right ramp -->
    <circle cx="130" cy="130" r="6" fill="#E53935" opacity="0.7"/>

    <!-- Ground line -->
    <line x1="35" y1="170" x2="155" y2="170" stroke="#795548" stroke-width="1.5"/>

    <!-- Arrow showing motion -->
    <path d="M 80 132 Q 110 125 125 130" fill="none" stroke="#F57C00" stroke-width="1.5"/>
    <polygon points="125,130 118,127 120,135" fill="#F57C00"/>

    <text x="137" y="190" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Без трения: h1 = h2</text>

    <!-- First law illustration: object at rest / constant velocity -->
    <rect x="260" y="62" width="215" height="130" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">I закон Ньютона</text>

    <!-- Object at rest -->
    <rect x="275" y="95" width="30" height="20" rx="3" fill="#1565C0"/>
    <text x="290" y="125" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">v = 0</text>
    <text x="290" y="135" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Покой</text>

    <!-- Object moving at constant v -->
    <rect x="360" y="95" width="30" height="20" rx="3" fill="#E53935"/>
    ''' + draw_arrow(395, 105, 455, 105, "#2E7D32", 2, 8) + '''
    <text x="425" y="125" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">v = const</text>
    <text x="425" y="135" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Равномерно</text>

    <!-- No net force -->
    <text x="367" y="155" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" font-weight="bold" text-anchor="middle">F(рез) = 0</text>
    <text x="367" y="170" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Существуют ИСО, где:</text>
    <text x="367" y="182" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">если F = 0, то v = const</text>

    <!-- Inertial reference frames -->
    <rect x="25" y="205" width="225" height="70" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="137" y="221" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Инерциальные системы отсчёта</text>
    <line x1="35" y1="226" x2="240" y2="226" stroke="#F57C00" stroke-width="0.5" opacity="0.3"/>
    <text x="137" y="241" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">ИСО — система, где тело без сил</text>
    <text x="137" y="255" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">движется равномерно или покоится</text>
    <text x="137" y="269" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Все ИСО эквивалентны (относительность)</text>

    <!-- Key concept -->
    <rect x="260" y="205" width="215" height="70" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="367" y="221" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Суть инерции</text>
    <line x1="270" y1="226" x2="465" y2="226" stroke="#7B1FA2" stroke-width="0.5" opacity="0.3"/>
    <text x="367" y="241" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Тело сохраняет состояние покоя</text>
    <text x="367" y="255" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">или равномерного движения</text>
    <text x="367" y="269" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Сила нужна для изменения скорости</text>
    '''
    svg += footer("Динамика", 11)
    return svg


# ============================================================
# LESSON 12: Сила. Второй закон Ньютона
# ============================================================
def lesson12():
    svg = header("Сила. Второй закон Ньютона", "Физика 10 класс — Урок 12")
    svg += '''
    <!-- Force diagram: body with force and acceleration -->
    <rect x="25" y="62" width="225" height="130" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Второй закон Ньютона</text>

    <!-- Body (block) -->
    <rect x="95" y="120" width="40" height="30" rx="4" fill="#1565C0"/>
    <text x="115" y="140" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">m</text>

    <!-- Force F -->
    ''' + draw_arrow(135, 135, 220, 135, "#E53935", 3, 10) + '''
    <text x="185" y="128" font-family="Arial,sans-serif" font-size="12" fill="#E53935" font-weight="bold" font-style="italic">F</text>

    <!-- Acceleration a -->
    ''' + draw_arrow(135, 155, 200, 155, "#F57C00", 2, 8) + '''
    <text x="170" y="168" font-family="Arial,sans-serif" font-size="10" fill="#F57C00" font-weight="bold" font-style="italic">a</text>

    <!-- Direction of motion -->
    <text x="80" y="170" font-family="Arial,sans-serif" font-size="7" fill="#555">v0</text>

    <!-- Key formula -->
    <rect x="45" y="178" width="170" height="30" rx="4" fill="#E3F2FD" stroke="#E53935" stroke-width="1.5"/>
    <text x="130" y="198" font-family="Arial,sans-serif" font-size="14" fill="#E53935" text-anchor="middle" font-weight="bold">F = m * a</text>

    <!-- Multiple forces diagram -->
    <rect x="260" y="62" width="215" height="130" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Сложение сил</text>

    <!-- Body -->
    <circle cx="367" cy="130" r="15" fill="#42A5F5" opacity="0.8"/>
    <text x="367" y="134" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle">m</text>

    <!-- F1 right -->
    ''' + draw_arrow(382, 125, 440, 125, "#E53935", 2, 7) + '''
    <text x="415" y="120" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold">F1</text>

    <!-- F2 up-right -->
    ''' + draw_arrow(378, 118, 410, 85, "#2E7D32", 2, 7) + '''
    <text x="415" y="90" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold">F2</text>

    <!-- F3 down -->
    ''' + draw_arrow(367, 145, 367, 180, "#F57C00", 2, 7) + '''
    <text x="378" y="175" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold">F3</text>

    <!-- Resultant -->
    <text x="367" y="197" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">F(рез) = F1+F2+F3</text>
    <text x="367" y="210" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">a = F(рез)/m</text>

    <!-- Properties of force -->
    <rect x="25" y="205" width="225" height="70" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="137" y="221" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Свойства силы</text>
    <line x1="35" y1="226" x2="240" y2="226" stroke="#2E7D32" stroke-width="0.5" opacity="0.3"/>
    <circle cx="45" cy="237" r="3" fill="#E53935"/>
    <text x="55" y="241" font-family="Arial,sans-serif" font-size="8" fill="#333">Векторная величина</text>
    <circle cx="45" cy="252" r="3" fill="#2E7D32"/>
    <text x="55" y="256" font-family="Arial,sans-serif" font-size="8" fill="#333">Имеет точку приложения</text>
    <circle cx="45" cy="267" r="3" fill="#F57C00"/>
    <text x="55" y="271" font-family="Arial,sans-serif" font-size="8" fill="#333">[F] = Н (Ньютон) = кг*м/с/с</text>

    <!-- Important notes -->
    <rect x="260" y="205" width="215" height="70" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="367" y="221" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Важные следствия</text>
    <line x1="270" y1="226" x2="465" y2="226" stroke="#7B1FA2" stroke-width="0.5" opacity="0.3"/>
    <text x="367" y="241" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">F и a всегда сонаправлены</text>
    <text x="367" y="255" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">a = F/m — ускорение пропорц.</text>
    <text x="367" y="269" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">F=0 => a=0 => v=const (I закон)</text>
    '''
    svg += footer("Динамика", 12)
    return svg


# ============================================================
# LESSON 13: Третий закон Ньютона
# ============================================================
def lesson13():
    svg = header("Третий закон Ньютона", "Физика 10 класс — Урок 13")
    svg += '''
    <!-- Two interacting bodies -->
    <rect x="25" y="62" width="450" height="130" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="250" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Третий закон Ньютона: F1 = -F2</text>

    <!-- Body 1 -->
    <rect x="120" y="105" width="55" height="40" rx="5" fill="#E53935" opacity="0.8"/>
    <text x="147" y="130" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">m1</text>

    <!-- Body 2 -->
    <rect x="320" y="105" width="55" height="40" rx="5" fill="#1565C0" opacity="0.8"/>
    <text x="347" y="130" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">m2</text>

    <!-- F12: force on body 1 from body 2 (leftward) -->
    ''' + draw_arrow(175, 118, 120, 118, "#E53935", 2.5, 8) + '''
    <text x="145" y="112" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold">F12</text>

    <!-- F21: force on body 2 from body 1 (rightward) -->
    ''' + draw_arrow(320, 132, 375, 132, "#1565C0", 2.5, 8) + '''
    <text x="350" y="150" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold">F21</text>

    <!-- Equal signs -->
    <text x="250" y="125" font-family="Arial,sans-serif" font-size="14" fill="#333" text-anchor="middle" font-weight="bold">|F12| = |F21|</text>
    <text x="250" y="145" font-family="Arial,sans-serif" font-size="9" fill="#555" text-anchor="middle">Противоположные направления</text>
    <text x="250" y="160" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Приложены к РАЗНЫМ телам!</text>

    <!-- Examples -->
    <rect x="25" y="205" width="145" height="70" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="97" y="221" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" font-weight="bold" text-anchor="middle">Человек и пол</text>
    <!-- Stick figure pushing down, floor pushing up -->
    <line x1="90" y1="232" x2="90" y2="255" stroke="#333" stroke-width="2"/>
    <circle cx="90" cy="228" r="6" fill="#FFCC80"/>
    <line x1="80" y1="240" x2="100" y2="240" stroke="#333" stroke-width="1.5"/>
    <!-- Floor -->
    <line x1="60" y1="258" x2="130" y2="258" stroke="#795548" stroke-width="2"/>
    <!-- Normal force up -->
    ''' + draw_arrow(90, 258, 90, 243, "#2E7D32", 1.5, 5) + '''
    <!-- Weight down -->
    ''' + draw_arrow(90, 255, 90, 268, "#E53935", 1.5, 5) + '''

    <rect x="180" y="205" width="145" height="70" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="252" y="221" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" font-weight="bold" text-anchor="middle">Лодка и вода</text>
    <!-- Boat -->
    <path d="M 220 245 L 235 255 L 270 255 L 285 245 Z" fill="#795548" opacity="0.7"/>
    <!-- Oar pushing water back -->
    ''' + draw_arrow(250, 245, 230, 250, "#1565C0", 1.5, 5) + '''
    <!-- Boat moving forward -->
    ''' + draw_arrow(265, 240, 285, 240, "#F57C00", 1.5, 5) + '''
    <!-- Water surface -->
    <path d="M 210 258 Q 230 255 252 258 Q 275 261 295 258" fill="none" stroke="#42A5F5" stroke-width="1"/>

    <rect x="335" y="205" width="140" height="70" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="405" y="221" font-family="Arial,sans-serif" font-size="8" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Ракета</text>
    <!-- Rocket body -->
    <rect x="395" y="228" width="16" height="30" rx="3" fill="#E53935" opacity="0.8"/>
    <polygon points="403,225 395,228 411,228" fill="#E53935"/>
    <!-- Exhaust -->
    ''' + draw_arrow(403, 260, 403, 270, "#F57C00", 1.5, 5) + '''
    <!-- Thrust up -->
    ''' + draw_arrow(403, 228, 403, 215, "#2E7D32", 1.5, 5) + '''
    <!-- Flames -->
    <ellipse cx="398" cy="265" rx="4" ry="6" fill="#F57C00" opacity="0.6"/>
    <ellipse cx="408" cy="265" rx="4" ry="6" fill="#F57C00" opacity="0.6"/>
    '''
    svg += footer("Динамика", 13)
    return svg


# ============================================================
# LESSON 14: Сила тяжести
# ============================================================
def lesson14():
    svg = header("Сила тяжести", "Физика 10 класс — Урок 14")
    svg += '''
    <!-- Earth with objects falling -->
    <rect x="25" y="62" width="220" height="130" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="135" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Сила тяжести</text>

    <!-- Earth arc -->
    <path d="M 40 185 Q 135 195 230 185" fill="none" stroke="#2E7D32" stroke-width="3"/>
    <ellipse cx="135" cy="190" rx="95" ry="12" fill="#2E7D32" opacity="0.15"/>

    <!-- Object 1: ball -->
    <circle cx="80" cy="100" r="8" fill="#E53935"/>
    <!-- Weight arrow -->
    ''' + draw_arrow(80, 108, 80, 155, "#E53935", 2.5, 8) + '''
    <text x="92" y="130" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" font-style="italic">F(т)</text>
    <text x="92" y="142" font-family="Arial,sans-serif" font-size="7" fill="#555">= mg</text>

    <!-- Object 2: box -->
    <rect x="155" y="92" width="20" height="16" rx="2" fill="#1565C0"/>
    ''' + draw_arrow(165, 108, 165, 160, "#1565C0", 2.5, 8) + '''
    <text x="177" y="135" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" font-style="italic">F(т)</text>

    <!-- Center of Earth arrow -->
    <text x="135" y="178" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">К центру Земли</text>

    <!-- Formula box -->
    <rect x="260" y="62" width="215" height="65" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Формулы</text>
    <line x1="270" y1="83" x2="465" y2="83" stroke="#E53935" stroke-width="0.5" opacity="0.3"/>
    <text x="367" y="100" font-family="Arial,sans-serif" font-size="11" fill="#333" text-anchor="middle" font-weight="bold">F(т) = m * g</text>
    <text x="367" y="118" font-family="Arial,sans-serif" font-size="9" fill="#555" text-anchor="middle">g = 9.8 м/с/с (ускорение своб. падения)</text>

    <!-- Weight vs Mass -->
    <rect x="260" y="135" width="215" height="57" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="367" y="151" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Вес vs Масса</text>
    <line x1="270" y1="156" x2="465" y2="156" stroke="#F57C00" stroke-width="0.5" opacity="0.3"/>
    <text x="290" y="170" font-family="Arial,sans-serif" font-size="8" fill="#E53935">P = mg (вес, Н)</text>
    <text x="290" y="184" font-family="Arial,sans-serif" font-size="8" fill="#1565C0">m (масса, кг)</text>
    <text x="400" y="177" font-family="Arial,sans-serif" font-size="7" fill="#555">P != m!</text>

    <!-- Free fall acceleration on different planets -->
    <rect x="25" y="205" width="225" height="70" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="137" y="221" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">g на разных планетах</text>
    <line x1="35" y1="226" x2="240" y2="226" stroke="#7B1FA2" stroke-width="0.5" opacity="0.3"/>
    <!-- Bar chart for g values -->
    <rect x="45" y="245" width="25" height="20" rx="2" fill="#E53935"/>
    <text x="57" y="240" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Земля</text>
    <text x="57" y="270" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">9.8</text>

    <rect x="85" y="250" width="25" height="15" rx="2" fill="#F57C00"/>
    <text x="97" y="240" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Марс</text>
    <text x="97" y="270" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">3.7</text>

    <rect x="125" y="255" width="25" height="10" rx="2" fill="#42A5F5"/>
    <text x="137" y="240" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Луна</text>
    <text x="137" y="270" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">1.6</text>

    <rect x="165" y="237" width="25" height="28" rx="2" fill="#2E7D32"/>
    <text x="177" y="233" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Юпитер</text>
    <text x="177" y="270" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">24.8</text>

    <rect x="205" y="242" width="25" height="23" rx="2" fill="#7B1FA2"/>
    <text x="217" y="238" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Венера</text>
    <text x="217" y="270" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">8.9</text>

    <!-- Weightlessness -->
    <rect x="260" y="205" width="215" height="70" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="367" y="221" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Невесомость</text>
    <line x1="270" y1="226" x2="465" y2="226" stroke="#1565C0" stroke-width="0.5" opacity="0.3"/>
    <!-- Astronaut in capsule -->
    <ellipse cx="367" cy="255" rx="30" ry="15" fill="none" stroke="#1565C0" stroke-width="1.5"/>
    <!-- Floating figure -->
    <circle cx="367" cy="245" r="5" fill="#FFCC80"/>
    <line x1="367" y1="250" x2="367" y2="260" stroke="#333" stroke-width="1.5"/>
    <line x1="357" y1="255" x2="377" y2="255" stroke="#333" stroke-width="1.5"/>
    <text x="367" y="272" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">P = 0 при свободном падении</text>
    '''
    svg += footer("Динамика", 14)
    return svg


# ============================================================
# LESSON 15: Сила упругости. Закон Гука
# ============================================================
def lesson15():
    svg = header("Сила упругости. Закон Гука", "Физика 10 класс — Урок 15")
    svg += '''
    <!-- Spring with deformation -->
    <rect x="25" y="62" width="225" height="130" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Деформация пружины</text>

    <!-- Wall -->
    <rect x="35" y="95" width="10" height="60" fill="#795548"/>
    <!-- Lines for wall texture -->
    <line x1="35" y1="100" x2="45" y2="95" stroke="#5D4037" stroke-width="1"/>
    <line x1="35" y1="110" x2="45" y2="105" stroke="#5D4037" stroke-width="1"/>
    <line x1="35" y1="120" x2="45" y2="115" stroke="#5D4037" stroke-width="1"/>
    <line x1="35" y1="130" x2="45" y2="125" stroke="#5D4037" stroke-width="1"/>
    <line x1="35" y1="140" x2="45" y2="135" stroke="#5D4037" stroke-width="1"/>
    <line x1="35" y1="150" x2="45" y2="145" stroke="#5D4037" stroke-width="1"/>

    <!-- Natural length spring (top) -->
    <text x="55" y="108" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">l0</text>
    <path d="M 45 105 L 55 105 L 60 95 L 70 115 L 80 95 L 90 115 L 100 95 L 110 115 L 120 95 L 130 105 L 140 105" fill="none" stroke="#2E7D32" stroke-width="2"/>
    <text x="145" y="108" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">свободна</text>

    <!-- Stretched spring (bottom) with force -->
    <path d="M 45 140 L 55 140 L 65 130 L 80 150 L 95 130 L 110 150 L 125 130 L 140 150 L 155 130 L 170 140 L 180 140" fill="none" stroke="#E53935" stroke-width="2"/>
    <!-- Mass block -->
    <rect x="180" y="130" width="25" height="20" rx="3" fill="#1565C0"/>
    <text x="192" y="145" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">m</text>

    <!-- Extension x -->
    <line x1="140" y1="160" x2="180" y2="160" stroke="#F57C00" stroke-width="1.5"/>
    <line x1="140" y1="155" x2="140" y2="165" stroke="#F57C00" stroke-width="1"/>
    <line x1="180" y1="155" x2="180" y2="165" stroke="#F57C00" stroke-width="1"/>
    <text x="160" y="172" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" text-anchor="middle" font-style="italic">x</text>

    <!-- Force on block -->
    ''' + draw_arrow(205, 140, 230, 140, "#E53935", 2, 7) + '''
    <text x="225" y="135" font-family="Arial,sans-serif" font-size="8" fill="#E53935">F(внеш)</text>

    <!-- Restoring force -->
    ''' + draw_arrow(180, 148, 155, 148, "#2E7D32", 1.5, 6) + '''
    <text x="160" y="157" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">F(упр)</text>

    <!-- Hooke's law graph F(x) -->
    <rect x="260" y="62" width="215" height="130" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Закон Гука: F = -kx</text>

    <!-- Axes -->
    ''' + draw_arrow(290, 175, 290, 85, "#333", 1.5, 7) + '''
    ''' + draw_arrow(290, 175, 455, 175, "#333", 1.5, 7) + '''
    <text x="452" y="190" font-family="Arial,sans-serif" font-size="10" fill="#333" font-style="italic">x</text>
    <text x="280" y="88" font-family="Arial,sans-serif" font-size="10" fill="#333" font-style="italic">F</text>

    <!-- Linear F = kx line -->
    <line x1="290" y1="175" x2="430" y2="95" stroke="#E53935" stroke-width="2.5"/>
    <text x="380" y="120" font-family="Arial,sans-serif" font-size="8" fill="#E53935" font-style="italic">tg(a) = k</text>

    <!-- Elastic limit -->
    <line x1="410" y1="85" x2="410" y2="175" stroke="#F57C00" stroke-width="1.5" stroke-dasharray="4,2"/>
    <text x="410" y="82" font-family="Arial,sans-serif" font-size="6" fill="#F57C00" text-anchor="middle">предел</text>

    <!-- Types of deformation -->
    <rect x="25" y="205" width="225" height="70" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="137" y="221" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Виды деформации</text>
    <line x1="35" y1="226" x2="240" y2="226" stroke="#2E7D32" stroke-width="0.5" opacity="0.3"/>
    <!-- Tension -->
    <rect x="35" y="232" width="60" height="18" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="65" y="245" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Растяжение</text>
    <!-- Compression -->
    <rect x="105" y="232" width="60" height="18" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="135" y="245" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Сжатие</text>
    <!-- Bending -->
    <rect x="175" y="232" width="60" height="18" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="205" y="245" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Изгиб</text>
    <!-- Shear -->
    <rect x="35" y="256" width="60" height="18" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="65" y="269" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Сдвиг</text>
    <!-- Torsion -->
    <rect x="105" y="256" width="60" height="18" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="135" y="269" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Кручение</text>

    <!-- Formula summary -->
    <rect x="260" y="205" width="215" height="70" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="367" y="221" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Формулы</text>
    <line x1="270" y1="226" x2="465" y2="226" stroke="#7B1FA2" stroke-width="0.5" opacity="0.3"/>
    <text x="367" y="242" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">F(упр) = -k * x</text>
    <text x="367" y="258" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">k — жёсткость (Н/м)</text>
    <text x="367" y="272" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">x — удлинение (м)</text>
    '''
    svg += footer("Динамика", 15)
    return svg


# ============================================================
# LESSON 16: Сила трения
# ============================================================
def lesson16():
    svg = header("Сила трения", "Физика 10 класс — Урок 16")
    svg += '''
    <!-- Friction diagram: block on surface -->
    <rect x="25" y="62" width="225" height="140" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Сила трения</text>

    <!-- Surface -->
    <rect x="35" y="155" width="210" height="8" rx="2" fill="#795548" opacity="0.6"/>
    <!-- Surface texture -->
    <line x1="40" y1="158" x2="48" y2="163" stroke="#5D4037" stroke-width="0.8"/>
    <line x1="60" y1="158" x2="68" y2="163" stroke="#5D4037" stroke-width="0.8"/>
    <line x1="80" y1="158" x2="88" y2="163" stroke="#5D4037" stroke-width="0.8"/>
    <line x1="100" y1="158" x2="108" y2="163" stroke="#5D4037" stroke-width="0.8"/>
    <line x1="120" y1="158" x2="128" y2="163" stroke="#5D4037" stroke-width="0.8"/>
    <line x1="140" y1="158" x2="148" y2="163" stroke="#5D4037" stroke-width="0.8"/>
    <line x1="160" y1="158" x2="168" y2="163" stroke="#5D4037" stroke-width="0.8"/>
    <line x1="180" y1="158" x2="188" y2="163" stroke="#5D4037" stroke-width="0.8"/>
    <line x1="200" y1="158" x2="208" y2="163" stroke="#5D4037" stroke-width="0.8"/>
    <line x1="220" y1="158" x2="228" y2="163" stroke="#5D4037" stroke-width="0.8"/>

    <!-- Block -->
    <rect x="85" y="125" width="50" height="30" rx="3" fill="#1565C0"/>
    <text x="110" y="145" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle">m</text>

    <!-- Applied force F (right) -->
    ''' + draw_arrow(135, 140, 210, 140, "#2E7D32", 2.5, 8) + '''
    <text x="180" y="133" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" font-weight="bold">F</text>

    <!-- Friction force (left) -->
    ''' + draw_arrow(85, 140, 40, 140, "#E53935", 2.5, 8) + '''
    <text x="55" y="133" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold">F(тр)</text>

    <!-- Normal force (up) -->
    ''' + draw_arrow(110, 125, 110, 95, "#F57C00", 2, 7) + '''
    <text x="120" y="105" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" font-weight="bold">N</text>

    <!-- Weight (down) -->
    ''' + draw_arrow(110, 155, 110, 185, "#7B1FA2", 2, 7) + '''
    <text x="120" y="180" font-family="Arial,sans-serif" font-size="8" fill="#7B1FA2" font-weight="bold">mg</text>

    <!-- Types of friction -->
    <rect x="260" y="62" width="215" height="80" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Виды трения</text>

    <!-- Static friction -->
    <rect x="270" y="87" width="195" height="15" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="367" y="98" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Трение покоя: 0 &lt;= F(тр) &lt;= F(max)</text>

    <!-- Sliding friction -->
    <rect x="270" y="107" width="195" height="15" rx="3" fill="#E3F2FD" stroke="#E53935" stroke-width="0.8"/>
    <text x="367" y="118" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Трение скольжения: F = mu*N</text>

    <!-- Rolling friction -->
    <rect x="270" y="127" width="195" height="15" rx="3" fill="#E3F2FD" stroke="#2E7D32" stroke-width="0.8"/>
    <text x="367" y="138" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Трение качения (наименьшее)</text>

    <!-- F(friction) vs F(applied) graph -->
    <rect x="260" y="150" width="215" height="52" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="367" y="164" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" font-weight="bold" text-anchor="middle">Зависимость F(тр) от F</text>
    <!-- Mini axes -->
    ''' + draw_arrow(280, 195, 280, 158, "#333", 1, 5) + '''
    ''' + draw_arrow(280, 195, 460, 195, "#333", 1, 5) + '''
    <!-- Static: linear increase then drop -->
    <line x1="280" y1="195" x2="370" y2="175" stroke="#2E7D32" stroke-width="2"/>
    <!-- Max static friction -->
    <circle cx="370" cy="175" r="3" fill="#2E7D32"/>
    <!-- Drop to kinetic -->
    <line x1="370" y1="175" x2="375" y2="180" stroke="#E53935" stroke-width="1.5"/>
    <!-- Kinetic: constant -->
    <line x1="375" y1="180" x2="460" y2="180" stroke="#E53935" stroke-width="2"/>
    <text x="290" y="162" font-family="Arial,sans-serif" font-size="6" fill="#333">F(тр)</text>
    <text x="448" y="192" font-family="Arial,sans-serif" font-size="6" fill="#333">F</text>

    <!-- Formulas -->
    <rect x="25" y="215" width="225" height="55" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="137" y="231" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Закон Кулона-Амонтона</text>
    <text x="137" y="248" font-family="Arial,sans-serif" font-size="11" fill="#333" text-anchor="middle" font-weight="bold">F(тр) = mu * N</text>
    <text x="137" y="264" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">mu — коэффициент трения, N — сила нормальной реакции</text>

    <!-- Useful info -->
    <rect x="260" y="215" width="215" height="55" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="367" y="231" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Полезное и вредное</text>
    <rect x="270" y="238" width="90" height="22" rx="3" fill="#E8F5E9" stroke="#2E7D32" stroke-width="0.8"/>
    <text x="315" y="253" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Полезное: ходьба</text>
    <rect x="370" y="238" width="95" height="22" rx="3" fill="#FFEBEE" stroke="#E53935" stroke-width="0.8"/>
    <text x="417" y="253" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle">Вредное: износ</text>
    '''
    svg += footer("Динамика", 16)
    return svg


# ============================================================
# LESSON 17: Закон всемирного тяготения
# ============================================================
def lesson17():
    svg = header("Закон всемирного тяготения", "Физика 10 класс — Урок 17")
    svg += '''
    <!-- Two masses attracting each other -->
    <rect x="25" y="62" width="225" height="130" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Закон всемирного тяготения</text>

    <!-- Mass m1 -->
    <circle cx="75" cy="135" r="22" fill="#E53935" opacity="0.8"/>
    <text x="75" y="139" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">M1</text>

    <!-- Mass m2 -->
    <circle cx="200" cy="135" r="16" fill="#1565C0" opacity="0.8"/>
    <text x="200" y="139" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">M2</text>

    <!-- Attraction forces -->
    ''' + draw_arrow(97, 130, 118, 130, "#F57C00", 2, 7) + '''
    ''' + draw_arrow(184, 130, 162, 130, "#F57C00", 2, 7) + '''
    <text x="137" y="125" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" text-anchor="middle">F</text>

    <!-- Distance r -->
    <line x1="75" y1="168" x2="200" y2="168" stroke="#333" stroke-width="1"/>
    <line x1="75" y1="163" x2="75" y2="173" stroke="#333" stroke-width="1"/>
    <line x1="200" y1="163" x2="200" y2="173" stroke="#333" stroke-width="1"/>
    <text x="137" y="180" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-style="italic">r</text>

    <!-- Formula -->
    <rect x="40" y="160" width="195" height="25" rx="3" fill="#E3F2FD" stroke="#F57C00" stroke-width="1.5" opacity="0"/>
    <text x="137" y="95" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">F = G * M1 * M2 / r*r</text>

    <!-- Newton and apple -->
    <circle cx="240" cy="100" r="4" fill="#E53935"/>
    <line x1="240" y1="104" x2="240" y2="118" stroke="#E53935" stroke-width="1" stroke-dasharray="2,2"/>
    ''' + draw_arrow(240, 118, 240, 130, "#E53935", 1.5, 5) + '''
    <text x="248" y="120" font-family="Arial,sans-serif" font-size="6" fill="#555">mg</text>

    <!-- Formula box -->
    <rect x="260" y="62" width="215" height="90" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Формула</text>
    <line x1="270" y1="83" x2="465" y2="83" stroke="#E53935" stroke-width="0.5" opacity="0.3"/>
    <text x="367" y="102" font-family="Arial,sans-serif" font-size="12" fill="#333" text-anchor="middle" font-weight="bold">F = G*M1*M2 / r*r</text>
    <text x="367" y="120" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">G = 6.67 * 10^(-11) Н*м/кг/кг</text>
    <text x="367" y="135" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Гравитационная постоянная</text>
    <text x="367" y="148" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle">Опыт Кавендиша (1798)</text>

    <!-- g from universal law -->
    <rect x="260" y="160" width="215" height="52" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="367" y="176" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Ускорение свободного падения</text>
    <text x="367" y="194" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle">g = G*M(Земли) / R*R</text>
    <text x="367" y="208" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">На высоте h: g(h) = G*M/(R+h)^2</text>

    <!-- Scope -->
    <rect x="25" y="205" width="225" height="65" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="137" y="221" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Границы применимости</text>
    <line x1="35" y1="226" x2="240" y2="226" stroke="#7B1FA2" stroke-width="0.5" opacity="0.3"/>
    <circle cx="45" cy="237" r="3" fill="#2E7D32"/>
    <text x="55" y="241" font-family="Arial,sans-serif" font-size="8" fill="#333">Материальные точки</text>
    <circle cx="45" cy="252" r="3" fill="#F57C00"/>
    <text x="55" y="256" font-family="Arial,sans-serif" font-size="8" fill="#333">Однородные шары</text>
    <circle cx="45" cy="265" r="3" fill="#E53935"/>
    <text x="55" y="269" font-family="Arial,sans-serif" font-size="8" fill="#333">Тело внутри сферы (F=0!)</text>

    <!-- Historical note -->
    <rect x="260" y="220" width="215" height="50" rx="5" fill="white" stroke="#1565C0" stroke-width="1"/>
    <text x="367" y="236" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" font-weight="bold" text-anchor="middle">История</text>
    <text x="367" y="250" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Ньютон (1687) — закон</text>
    <text x="367" y="263" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Кавендиш (1798) — измерил G</text>
    '''
    svg += footer("Динамика", 17)
    return svg


# ============================================================
# LESSON 18: Движение тела под действием силы тяжести
# ============================================================
def lesson18():
    svg = header("Движение тела под действием силы тяжести", "Физика 10 класс — Урок 18")
    svg += '''
    <!-- Projectile motion parabola -->
    <rect x="25" y="62" width="300" height="155" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="175" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Движение тела, брошенного под углом</text>

    <!-- Ground -->
    <line x1="35" y1="200" x2="315" y2="200" stroke="#795548" stroke-width="2"/>

    <!-- Parabolic trajectory -->
    <path d="M 50 200 Q 175 50 290 200" fill="none" stroke="#E53935" stroke-width="2.5"/>

    <!-- Launch point -->
    <circle cx="50" cy="200" r="4" fill="#2E7D32"/>
    <!-- Landing point -->
    <circle cx="290" cy="200" r="4" fill="#E53935"/>

    <!-- v0 vector (at angle) -->
    ''' + draw_arrow(50, 200, 95, 165, "#2E7D32", 2, 8) + '''
    <text x="80" y="175" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" font-weight="bold">v0</text>

    <!-- Angle alpha -->
    <path d="M 75 200 A 25 25 0 0 0 68 188" fill="none" stroke="#F57C00" stroke-width="1.5"/>
    <text x="82" y="195" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-style="italic">a</text>

    <!-- Horizontal component vx -->
    <line x1="50" y1="200" x2="100" y2="200" stroke="#42A5F5" stroke-width="1.5" stroke-dasharray="4,2"/>
    <polygon points="100,200 94,196 94,204" fill="#42A5F5"/>
    <text x="75" y="212" font-family="Arial,sans-serif" font-size="8" fill="#42A5F5">v0x = v0*cos(a)</text>

    <!-- Vertical component vy -->
    <line x1="100" y1="200" x2="95" y2="165" stroke="#7B1FA2" stroke-width="1.5" stroke-dasharray="4,2"/>
    <polygon points="95,165 91,173 99,173" fill="#7B1FA2"/>
    <text x="105" y="180" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2">v0y</text>

    <!-- Height label -->
    <line x1="170" y1="200" x2="170" y2="90" stroke="#2E7D32" stroke-width="1" stroke-dasharray="3,2"/>
    <text x="180" y="95" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32">h(max)</text>

    <!-- Range label -->
    <line x1="50" y1="210" x2="290" y2="210" stroke="#E53935" stroke-width="1"/>
    <text x="170" y="220" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle">S (дальность)</text>

    <!-- g arrow -->
    ''' + draw_arrow(170, 100, 170, 130, "#F57C00", 2, 7) + '''
    <text x="180" y="120" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold">g</text>

    <!-- Formulas -->
    <rect x="340" y="62" width="135" height="155" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="407" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Формулы</text>
    <line x1="350" y1="83" x2="465" y2="83" stroke="#E53935" stroke-width="0.5" opacity="0.3"/>
    <text x="355" y="97" font-family="Arial,sans-serif" font-size="7" fill="#333">x = v0*cos(a)*t</text>
    <text x="355" y="112" font-family="Arial,sans-serif" font-size="7" fill="#333">y = v0*sin(a)*t</text>
    <text x="355" y="122" font-family="Arial,sans-serif" font-size="7" fill="#333">    - g*t*t/2</text>
    <text x="355" y="140" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">h = v0y*v0y/(2g)</text>
    <text x="355" y="155" font-family="Arial,sans-serif" font-size="7" fill="#E53935">S = v0*v0*sin(2a)/g</text>
    <text x="355" y="170" font-family="Arial,sans-serif" font-size="7" fill="#F57C00">t(пол) = 2*v0*sin(a)/g</text>
    <text x="355" y="188" font-family="Arial,sans-serif" font-size="7" fill="#555">max S при a = 45</text>
    <text x="355" y="200" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2">vx = const</text>
    <text x="355" y="212" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2">vy = v0y - g*t</text>

    <!-- Free fall vs horizontal throw -->
    <rect x="25" y="230" width="225" height="40" rx="5" fill="white" stroke="#2E7D32" stroke-width="1"/>
    <text x="137" y="246" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">Свободное падение = частный случай</text>
    <text x="137" y="260" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">При a = 90: v0x = 0, чисто вертикальное</text>

    <rect x="260" y="230" width="215" height="40" rx="5" fill="white" stroke="#F57C00" stroke-width="1"/>
    <text x="367" y="246" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" text-anchor="middle">Горизонтальный бросок: a = 0</text>
    <text x="367" y="260" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">v0x = v0, v0y = 0, падение с высоты</text>
    '''
    svg += footer("Динамика", 18)
    return svg


# ============================================================
# LESSON 19: Движение искусственных спутников
# ============================================================
def lesson19():
    svg = header("Движение искусственных спутников", "Физика 10 класс — Урок 19")
    svg += '''
    <!-- Earth with orbiting satellite -->
    <rect x="25" y="62" width="280" height="175" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="165" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Орбитальное движение спутника</text>

    <!-- Earth -->
    <circle cx="165" cy="175" r="35" fill="#42A5F5" opacity="0.3" stroke="#1565C0" stroke-width="2"/>
    <!-- Continents hint -->
    <ellipse cx="155" cy="165" rx="12" ry="8" fill="#2E7D32" opacity="0.4"/>
    <ellipse cx="175" cy="180" rx="8" ry="6" fill="#2E7D32" opacity="0.3"/>
    <text x="165" y="178" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" text-anchor="middle">R</text>

    <!-- Orbit -->
    <circle cx="165" cy="175" r="70" fill="none" stroke="#E53935" stroke-width="2" stroke-dasharray="6,3"/>

    <!-- Satellite -->
    <rect x="228" y="102" width="10" height="6" rx="1" fill="#FFD600"/>
    <rect x="224" y="103" width="4" height="4" fill="#42A5F5" opacity="0.6"/>
    <rect x="238" y="103" width="4" height="4" fill="#42A5F5" opacity="0.6"/>

    <!-- Velocity vector (tangential) -->
    ''' + draw_arrow(240, 105, 270, 115, "#2E7D32", 2, 7) + '''
    <text x="265" y="110" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold">v</text>

    <!-- Gravity vector (toward Earth) -->
    ''' + draw_arrow(230, 108, 210, 128, "#E53935", 2, 7) + '''
    <text x="208" y="122" font-family="Arial,sans-serif" font-size="8" fill="#E53935">F(тяж)</text>

    <!-- Orbit radius -->
    <line x1="165" y1="175" x2="235" y2="105" stroke="#795548" stroke-width="1" stroke-dasharray="3,2"/>
    <text x="210" y="138" font-family="Arial,sans-serif" font-size="8" fill="#795548" font-style="italic">R+h</text>

    <!-- Direction of orbit -->
    <path d="M 210 90 A 70 70 0 0 1 240 100" fill="none" stroke="#F57C00" stroke-width="2"/>
    <polygon points="240,100 232,97 236,106" fill="#F57C00"/>

    <!-- First cosmic velocity -->
    <rect x="315" y="62" width="160" height="100" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="395" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Первая космическая</text>
    <line x1="325" y1="83" x2="465" y2="83" stroke="#E53935" stroke-width="0.5" opacity="0.3"/>
    <text x="395" y="100" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">v1 = sqrt(GM/R)</text>
    <text x="395" y="115" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">= sqrt(gR)</text>
    <text x="395" y="132" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">v1 = 7.9 км/с</text>
    <text x="395" y="148" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle">Минимальная для орбиты</text>

    <!-- Second cosmic velocity -->
    <rect x="315" y="170" width="160" height="67" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="395" y="186" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Вторая космическая</text>
    <line x1="325" y1="191" x2="465" y2="191" stroke="#F57C00" stroke-width="0.5" opacity="0.3"/>
    <text x="395" y="207" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">v2 = sqrt(2GM/R)</text>
    <text x="395" y="222" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">v2 = 11.2 км/с</text>
    <text x="395" y="234" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle">Покидает Землю</text>

    <!-- Key condition -->
    <rect x="25" y="248" width="450" height="28" rx="4" fill="white" stroke="#2E7D32" stroke-width="1"/>
    <text x="250" y="266" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">Условие орбиты: mg = mv*v/(R+h) => F(тяж) = F(центростр) => спутник «падает» на Землю, но промахивается</text>
    '''
    svg += footer("Динамика", 19)
    return svg


# ============================================================
# LESSON 20: Силы в механике (повторение и обобщение)
# ============================================================
def lesson20():
    svg = header("Силы в механике", "Повторение и обобщение — Урок 20")
    svg += '''
    <!-- Central diagram: all forces on a body -->
    <rect x="25" y="62" width="220" height="160" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="135" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Все силы в механике</text>

    <!-- Body on inclined plane -->
    <!-- Inclined surface -->
    <polygon points="50,195 200,195 200,120" fill="#795548" opacity="0.3" stroke="#795548" stroke-width="1.5"/>

    <!-- Block on incline -->
    <rect x="110" y="128" width="35" height="22" rx="3" fill="#1565C0" transform="rotate(-33, 127, 139)"/>

    <!-- Weight mg (down) -->
    ''' + draw_arrow(127, 150, 127, 205, "#7B1FA2", 2.5, 8) + '''
    <text x="137" y="185" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold">mg</text>

    <!-- Normal force N (perpendicular to surface) -->
    ''' + draw_arrow(127, 145, 95, 98, "#F57C00", 2.5, 8) + '''
    <text x="85" y="95" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold">N</text>

    <!-- Friction (along surface, upward) -->
    ''' + draw_arrow(115, 152, 80, 175, "#E53935", 2, 7) + '''
    <text x="70" y="170" font-family="Arial,sans-serif" font-size="8" fill="#E53935" font-weight="bold">F(тр)</text>

    <!-- Applied force (along surface, downward) -->
    ''' + draw_arrow(140, 140, 175, 165, "#2E7D32", 2, 7) + '''
    <text x="175" y="158" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" font-weight="bold">F</text>

    <!-- Angle -->
    <path d="M 185 195 A 15 15 0 0 0 178 184" fill="none" stroke="#333" stroke-width="1"/>
    <text x="190" y="188" font-family="Arial,sans-serif" font-size="8" fill="#333" font-style="italic">a</text>

    <!-- Summary table of forces -->
    <rect x="260" y="62" width="215" height="160" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Классификация сил</text>
    <line x1="270" y1="83" x2="465" y2="83" stroke="#E53935" stroke-width="0.5" opacity="0.3"/>

    <!-- Force list -->
    <circle cx="280" cy="93" r="4" fill="#7B1FA2"/>
    <text x="290" y="97" font-family="Arial,sans-serif" font-size="8" fill="#333">Сила тяжести: F = mg</text>

    <circle cx="280" cy="108" r="4" fill="#F57C00"/>
    <text x="290" y="112" font-family="Arial,sans-serif" font-size="8" fill="#333">Сила реакции: N</text>

    <circle cx="280" cy="123" r="4" fill="#E53935"/>
    <text x="290" y="127" font-family="Arial,sans-serif" font-size="8" fill="#333">Сила трения: F = mu*N</text>

    <circle cx="280" cy="138" r="4" fill="#2E7D32"/>
    <text x="290" y="142" font-family="Arial,sans-serif" font-size="8" fill="#333">Сила упругости: F = -kx</text>

    <circle cx="280" cy="153" r="4" fill="#1565C0"/>
    <text x="290" y="157" font-family="Arial,sans-serif" font-size="8" fill="#333">Вес тела: P = mg</text>

    <circle cx="280" cy="168" r="4" fill="#F57C00"/>
    <text x="290" y="172" font-family="Arial,sans-serif" font-size="8" fill="#333">Гравитация: F = GMm/r*r</text>

    <!-- Nature labels -->
    <rect x="270" y="180" width="90" height="15" rx="3" fill="#E8F5E9" stroke="#2E7D32" stroke-width="0.8"/>
    <text x="315" y="191" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Гравитационные</text>
    <rect x="370" y="180" width="90" height="15" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="415" y="191" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle">Электромагнитные</text>

    <rect x="270" y="200" width="90" height="15" rx="3" fill="#FFF3E0" stroke="#F57C00" stroke-width="0.8"/>
    <text x="315" y="211" font-family="Arial,sans-serif" font-size="7" fill="#F57C00" text-anchor="middle">Упругие</text>
    <rect x="370" y="200" width="90" height="15" rx="3" fill="#FFEBEE" stroke="#E53935" stroke-width="0.8"/>
    <text x="415" y="211" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle">Трения</text>

    <!-- Newton's laws reminder -->
    <rect x="25" y="235" width="450" height="40" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="250" y="251" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Законы Ньютона — фундамент механики</text>
    <text x="250" y="267" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">I: F=0 => v=const | II: F=ma | III: F12=-F21 | Все силы имеют природу: гравитация или электромагнетизм</text>
    '''
    svg += footer("Динамика", 20)
    return svg


# ============================================================
# Generate all 10 SVGs (lessons 11-20)
# ============================================================
generators = {
    11: lesson11,
    12: lesson12,
    13: lesson13,
    14: lesson14,
    15: lesson15,
    16: lesson16,
    17: lesson17,
    18: lesson18,
    19: lesson19,
    20: lesson20,
}

for num, gen in generators.items():
    svg_content = gen()
    filepath = os.path.join(OUTPUT_DIR, f"lesson{num}.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Generated lesson{num}.svg ({len(svg_content)} bytes)")

print(f"\nDone! Generated 10 SVGs (lessons 11-20) in {OUTPUT_DIR}")
