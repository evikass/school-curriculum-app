#!/usr/bin/env python3
"""Generate SVG illustrations for Physics Grade 10, Lessons 21-30
21-23: Динамика (продолжение), 24-28: Законы сохранения, 29-30: Статика
"""

import os, math

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app-site/public/images/lessons/grade10/physics"
os.makedirs(OUTPUT_DIR, exist_ok=True)

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

def footer(section, num):
    return f'''
  </g>
  <rect x="12" y="298" width="476" height="42" rx="5" fill="url(#panel)"/>
  <text x="250" y="316" font-family="Arial,sans-serif" font-size="14" text-anchor="middle" fill="white" font-weight="bold">{section}</text>
  <text x="250" y="332" font-family="Arial,sans-serif" font-size="10" text-anchor="middle" fill="white" opacity="0.8">Урок {num}</text>
</svg>'''

def arrow(x1, y1, x2, y2, color="#1565C0", w=2, h=8):
    dx, dy = x2-x1, y2-y1
    l = math.sqrt(dx*dx+dy*dy)
    if l < 1: return ""
    ux, uy = dx/l, dy/l
    px, py = -uy, ux
    lx, ly = x2-ux*h+px*h*0.4, y2-uy*h+py*h*0.4
    rx, ry = x2-ux*h-px*h*0.4, y2-uy*h-py*h*0.4
    return f'<line x1="{x1}" y1="{y1}" x2="{x2-h*0.5*ux}" y2="{y2-h*0.5*uy}" stroke="{color}" stroke-width="{w}"/>\n    <polygon points="{x2},{y2} {lx},{ly} {rx},{ry}" fill="{color}"/>'

# ============================================================
# LESSON 21: Применение законов Ньютона
# ============================================================
def lesson21():
    svg = header("Применение законов Ньютона", "Физика 10 класс — Урок 21")
    svg += f'''
    <!-- Elevator problem -->
    <rect x="25" y="62" width="220" height="140" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="135" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Лифт</text>

    <!-- Elevator box -->
    <rect x="80" y="88" width="60" height="80" rx="3" fill="none" stroke="#795548" stroke-width="2"/>
    <!-- Cable -->
    <line x1="110" y1="88" x2="110" y2="70" stroke="#555" stroke-width="2"/>
    {arrow(110, 70, 110, 60, "#2E7D32", 2, 7)}

    <!-- Person inside -->
    <circle cx="110" cy="110" r="6" fill="#FFCC80"/>
    <line x1="110" y1="116" x2="110" y2="135" stroke="#333" stroke-width="2"/>
    <line x1="100" y1="125" x2="120" y2="125" stroke="#333" stroke-width="1.5"/>

    <!-- Weight down -->
    {arrow(110, 140, 110, 162, "#E53935", 2, 7)}
    <text x="120" y="158" font-family="Arial,sans-serif" font-size="8" fill="#E53935">mg</text>

    <!-- Normal force up -->
    {arrow(110, 140, 110, 100, "#2E7D32", 1.5, 6)}

    <!-- Cases -->
    <text x="155" y="98" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">Вверх: N > mg</text>
    <text x="155" y="112" font-family="Arial,sans-serif" font-size="7" fill="#E53935">Вниз: N &lt; mg</text>
    <text x="155" y="126" font-family="Arial,sans-serif" font-size="7" fill="#795548">Покой: N = mg</text>
    <text x="155" y="140" font-family="Arial,sans-serif" font-size="7" fill="#F57C00">N = m(g+a)</text>
    <text x="155" y="154" font-family="Arial,sans-serif" font-size="7" fill="#F57C00">N = m(g-a)</text>

    <!-- Atwood machine -->
    <rect x="260" y="62" width="215" height="140" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Машина Атвуда</text>

    <!-- Pulley -->
    <circle cx="367" cy="95" r="12" fill="none" stroke="#555" stroke-width="2"/>
    <circle cx="367" cy="95" r="3" fill="#555"/>

    <!-- Left string -->
    <line x1="355" y1="95" x2="310" y2="175" stroke="#555" stroke-width="1.5"/>
    <!-- Left mass m1 -->
    <rect x="295" y="175" width="30" height="20" rx="3" fill="#E53935" opacity="0.8"/>
    <text x="310" y="189" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">m1</text>

    <!-- Right string -->
    <line x1="379" y1="95" x2="425" y2="165" stroke="#555" stroke-width="1.5"/>
    <!-- Right mass m2 -->
    <rect x="410" y="165" width="30" height="20" rx="3" fill="#1565C0" opacity="0.8"/>
    <text x="425" y="179" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">m2</text>

    <!-- Motion arrows -->
    {arrow(310, 195, 310, 210, "#E53935", 1.5, 5)}
    {arrow(425, 160, 425, 145, "#1565C0", 1.5, 5)}

    <text x="367" y="200" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">a = (m2-m1)g/(m1+m2)</text>

    <!-- Problem-solving approach -->
    <rect x="25" y="215" width="450" height="55" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="250" y="231" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Алгоритм применения законов Ньютона</text>
    <line x1="35" y1="236" x2="465" y2="236" stroke="#2E7D32" stroke-width="0.5" opacity="0.3"/>
    <rect x="35" y="241" width="85" height="20" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="77" y="255" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">1. Рисунок</text>
    <rect x="128" y="241" width="85" height="20" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="170" y="255" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">2. Силы</text>
    <rect x="221" y="241" width="85" height="20" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="263" y="255" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">3. F=ma (ox,oy)</text>
    <rect x="314" y="241" width="85" height="20" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="356" y="255" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">4. Решить</text>
    <rect x="407" y="241" width="58" height="20" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="436" y="255" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">5. Ответ</text>
    '''
    svg += footer("Динамика", 21)
    return svg


# ============================================================
# LESSON 22: Движение в неинерциальных системах отсчёта
# ============================================================
def lesson22():
    svg = header("Движение в неинерциальных СО", "Физика 10 класс — Урок 22")
    svg += f'''
    <!-- Accelerating car -->
    <rect x="25" y="62" width="225" height="130" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Ускоряющаяся система</text>

    <!-- Car body -->
    <rect x="50" y="130" width="90" height="35" rx="5" fill="#42A5F5" opacity="0.7"/>
    <!-- Car top -->
    <path d="M 70 130 L 80 110 L 120 110 L 130 130" fill="#42A5F5" opacity="0.5" stroke="#1565C0" stroke-width="1"/>
    <!-- Wheels -->
    <circle cx="72" cy="168" r="8" fill="#555"/>
    <circle cx="118" cy="168" r="8" fill="#555"/>

    <!-- Acceleration arrow -->
    {arrow(145, 148, 195, 148, "#2E7D32", 2.5, 9)}
    <text x="175" y="142" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" font-weight="bold">a</text>

    <!-- Ball inside car -->
    <circle cx="95" cy="150" r="7" fill="#E53935"/>

    <!-- Pseudoforce on ball (backward) -->
    {arrow(88, 145, 55, 145, "#F57C00", 2, 7)}
    <text x="60" y="140" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" font-weight="bold">F(ин)</text>

    <!-- Ground -->
    <line x1="30" y1="176" x2="240" y2="176" stroke="#795548" stroke-width="1.5"/>

    <text x="137" y="192" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">F(инерции) = -ma</text>
    <text x="137" y="205" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">В НСО шар «отклоняется назад»</text>

    <!-- Rotating reference frame -->
    <rect x="260" y="62" width="215" height="130" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Вращающаяся система</text>

    <!-- Platform circle -->
    <ellipse cx="367" cy="135" rx="55" ry="40" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
    <!-- Center -->
    <circle cx="367" cy="135" r="3" fill="#555"/>

    <!-- Object on platform -->
    <circle cx="410" cy="125" r="6" fill="#E53935"/>

    <!-- Centrifugal force (outward) -->
    {arrow(416, 122, 450, 105, "#E53935", 2, 7)}
    <text x="440" y="100" font-family="Arial,sans-serif" font-size="8" fill="#E53935">F(цб)</text>

    <!-- Coriolis force (perpendicular to v) -->
    {arrow(410, 118, 395, 95, "#7B1FA2", 1.5, 6)}
    <text x="378" y="90" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2">F(кор)</text>

    <!-- Velocity arrow -->
    {arrow(410, 125, 415, 150, "#2E7D32", 1.5, 5)}
    <text x="420" y="145" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">v</text>

    <!-- Rotation direction -->
    <path d="M 340 100 A 40 30 0 0 1 380 95" fill="none" stroke="#F57C00" stroke-width="2"/>
    <polygon points="380,95 374,100 377,92" fill="#F57C00"/>

    <!-- Formulas -->
    <rect x="25" y="205" width="225" height="65" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="137" y="221" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Силы инерции</text>
    <line x1="35" y1="226" x2="240" y2="226" stroke="#F57C00" stroke-width="0.5" opacity="0.3"/>
    <text x="137" y="240" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">F(ин) = -ma0 (поступательная)</text>
    <text x="137" y="254" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle">F(цб) = m*omega*r (центробежная)</text>
    <text x="137" y="268" font-family="Arial,sans-serif" font-size="8" fill="#7B1FA2" text-anchor="middle">F(кор) = -2m(omega x v) (Кориолиса)</text>

    <!-- Key concept -->
    <rect x="260" y="205" width="215" height="65" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="367" y="221" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Неинерциальные СО</text>
    <line x1="270" y1="226" x2="465" y2="226" stroke="#7B1FA2" stroke-width="0.5" opacity="0.3"/>
    <text x="367" y="240" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Система движется с ускорением</text>
    <text x="367" y="254" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">I закон Ньютона не выполняется</text>
    <text x="367" y="268" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Силы инерции НЕ реальные (фиктивные)</text>
    '''
    svg += footer("Динамика", 22)
    return svg


# ============================================================
# LESSON 23: Алгоритм решения задач по динамике
# ============================================================
def lesson23():
    svg = header("Алгоритм решения задач по динамике", "Физика 10 класс — Урок 23")
    svg += f'''
    <!-- Algorithm flowchart -->
    <rect x="25" y="62" width="450" height="25" rx="5" fill="#1565C0" opacity="0.1"/>
    <text x="250" y="80" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" font-weight="bold" text-anchor="middle">Пошаговый алгоритм</text>

    <!-- Step 1 -->
    <rect x="30" y="92" width="130" height="35" rx="5" fill="white" stroke="#1565C0" stroke-width="1.5"/>
    <circle cx="45" cy="102" r="8" fill="#1565C0"/>
    <text x="45" y="106" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">1</text>
    <text x="100" y="107" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Чертёж + силы</text>
    <text x="100" y="120" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Все тела + все силы</text>

    <!-- Arrow -->
    {arrow(165, 109, 180, 109, "#1565C0", 1.5, 5)}

    <!-- Step 2 -->
    <rect x="185" y="92" width="130" height="35" rx="5" fill="white" stroke="#1565C0" stroke-width="1.5"/>
    <circle cx="200" cy="102" r="8" fill="#E53935"/>
    <text x="200" y="106" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">2</text>
    <text x="255" y="107" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Выбрать СО</text>
    <text x="255" y="120" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">ИСО + оси ox, oy</text>

    {arrow(320, 109, 335, 109, "#1565C0", 1.5, 5)}

    <!-- Step 3 -->
    <rect x="340" y="92" width="130" height="35" rx="5" fill="white" stroke="#1565C0" stroke-width="1.5"/>
    <circle cx="355" cy="102" r="8" fill="#2E7D32"/>
    <text x="355" y="106" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">3</text>
    <text x="410" y="107" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">F=ma для осей</text>
    <text x="410" y="120" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">ox: Fx = max</text>

    <!-- Step 4-5 row -->
    {arrow(250, 130, 250, 142, "#1565C0", 1.5, 5)}

    <rect x="80" y="145" width="155" height="35" rx="5" fill="white" stroke="#F57C00" stroke-width="1.5"/>
    <circle cx="95" cy="155" r="8" fill="#F57C00"/>
    <text x="95" y="159" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">4</text>
    <text x="165" y="160" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Доп. соотношения</text>
    <text x="165" y="173" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">F(упр)=kx, F(тр)=muN...</text>

    {arrow(240, 162, 265, 162, "#1565C0", 1.5, 5)}

    <rect x="270" y="145" width="155" height="35" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
    <circle cx="285" cy="155" r="8" fill="#2E7D32"/>
    <text x="285" y="159" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">5</text>
    <text x="355" y="160" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Решить систему</text>
    <text x="355" y="173" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Подставить + найти</text>

    <!-- Example: block on inclined plane -->
    <rect x="25" y="195" width="225" height="80" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="137" y="211" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Пример: наклонная плоскость</text>

    <!-- Incline -->
    <polygon points="40,268 200,268 200,220" fill="#795548" opacity="0.3" stroke="#795548" stroke-width="1"/>
    <!-- Block -->
    <rect x="120" y="225" width="25" height="18" rx="2" fill="#1565C0" transform="rotate(-35,132,234)"/>
    <!-- mg down -->
    {arrow(132, 245, 132, 268, "#7B1FA2", 1.5, 5)}
    <!-- N perpendicular -->
    {arrow(130, 238, 108, 215, "#F57C00", 1.5, 5)}
    <!-- Friction up along surface -->
    {arrow(125, 242, 105, 255, "#E53935", 1.5, 5)}

    <text x="137" y="278" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">ox: mg*sin(a)-F(тр)=ma</text>
    <text x="137" y="288" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">oy: N-mg*cos(a)=0</text>

    <!-- Common mistakes -->
    <rect x="260" y="195" width="215" height="80" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="367" y="211" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Типичные ошибки</text>
    <line x1="270" y1="216" x2="465" y2="216" stroke="#E53935" stroke-width="0.5" opacity="0.3"/>
    <circle cx="280" cy="227" r="3" fill="#E53935"/>
    <text x="290" y="231" font-family="Arial,sans-serif" font-size="7" fill="#333">Забыть силу (N, трение)</text>
    <circle cx="280" cy="241" r="3" fill="#E53935"/>
    <text x="290" y="245" font-family="Arial,sans-serif" font-size="7" fill="#333">Неправильные проекции</text>
    <circle cx="280" cy="255" r="3" fill="#E53935"/>
    <text x="290" y="259" font-family="Arial,sans-serif" font-size="7" fill="#333">F=ma не для каждого тела</text>
    <circle cx="280" cy="269" r="3" fill="#E53935"/>
    <text x="290" y="273" font-family="Arial,sans-serif" font-size="7" fill="#333">Путать вес и силу тяжести</text>
    '''
    svg += footer("Динамика", 23)
    return svg


# ============================================================
# LESSON 24: Импульс тела. Закон сохранения импульса
# ============================================================
def lesson24():
    svg = header("Импульс тела. Закон сохранения импульса", "Физика 10 класс — Урок 24")
    svg += f'''
    <!-- Momentum vectors -->
    <rect x="25" y="62" width="225" height="130" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Импульс p = mv</text>

    <!-- Body with velocity -->
    <rect x="50" y="105" width="35" height="25" rx="4" fill="#1565C0"/>
    <text x="67" y="122" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle">m</text>

    <!-- Velocity arrow -->
    {arrow(85, 117, 155, 117, "#2E7D32", 2.5, 9)}
    <text x="125" y="110" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" font-weight="bold">v</text>

    <!-- Momentum arrow (same direction, scaled) -->
    {arrow(50, 150, 180, 150, "#E53935", 3, 10)}
    <text x="120" y="145" font-family="Arial,sans-serif" font-size="12" fill="#E53935" font-weight="bold" font-style="italic">p = mv</text>

    <text x="137" y="175" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Вектор! Сонаправлен с v</text>
    <text x="137" y="188" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">[p] = кг*м/с</text>

    <!-- Conservation law -->
    <rect x="260" y="62" width="215" height="130" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Закон сохранения импульса</text>

    <!-- Before collision -->
    <text x="310" y="98" font-family="Arial,sans-serif" font-size="8" fill="#555">До:</text>
    <circle cx="310" cy="115" r="12" fill="#E53935" opacity="0.8"/>
    <text x="310" y="119" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">m1</text>
    {arrow(322, 115, 350, 115, "#E53935", 1.5, 6)}

    <circle cx="400" cy="115" r="9" fill="#1565C0" opacity="0.8"/>
    <text x="400" y="119" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">m2</text>
    {arrow(409, 115, 385, 115, "#1565C0", 1.5, 6)}

    <!-- After collision -->
    <text x="310" y="148" font-family="Arial,sans-serif" font-size="8" fill="#555">После:</text>
    <circle cx="340" cy="165" r="12" fill="#E53935" opacity="0.6"/>
    <text x="340" y="169" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">m1</text>
    {arrow(352, 165, 370, 165, "#E53935", 1.5, 5)}

    <circle cx="400" cy="165" r="9" fill="#1565C0" opacity="0.6"/>
    <text x="400" y="169" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">m2</text>
    {arrow(409, 165, 445, 165, "#1565C0", 1.5, 5)}

    <!-- Formula -->
    <rect x="270" y="180" width="195" height="20" rx="3" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
    <text x="367" y="194" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">m1v1 + m2v2 = m1v1' + m2v2'</text>

    <!-- Impulse of force -->
    <rect x="25" y="205" width="225" height="65" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="137" y="221" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Импульс силы</text>
    <line x1="35" y1="226" x2="240" y2="226" stroke="#F57C00" stroke-width="0.5" opacity="0.3"/>
    <text x="137" y="242" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">F*dt = dp</text>
    <text x="137" y="258" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Импульс силы = изменение импульса</text>
    <text x="137" y="268" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">II закон Ньютона в импульсной форме</text>

    <!-- When conservation applies -->
    <rect x="260" y="205" width="215" height="65" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="367" y="221" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Когда применяется?</text>
    <line x1="270" y1="226" x2="465" y2="226" stroke="#7B1FA2" stroke-width="0.5" opacity="0.3"/>
    <circle cx="280" cy="237" r="3" fill="#2E7D32"/>
    <text x="290" y="241" font-family="Arial,sans-serif" font-size="8" fill="#333">Замкнутая система</text>
    <circle cx="280" cy="252" r="3" fill="#F57C00"/>
    <text x="290" y="256" font-family="Arial,sans-serif" font-size="8" fill="#333">Внешние силы компенсируются</text>
    <circle cx="280" cy="265" r="3" fill="#E53935"/>
    <text x="290" y="269" font-family="Arial,sans-serif" font-size="8" fill="#333">Кратковременное взаимодействие</text>
    '''
    svg += footer("Законы сохранения", 24)
    return svg


# ============================================================
# LESSON 25: Работа силы
# ============================================================
def lesson25():
    svg = header("Работа силы", "Физика 10 класс — Урок 25")
    svg += f'''
    <!-- Work diagram: force at angle -->
    <rect x="25" y="62" width="225" height="140" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Работа силы</text>

    <!-- Surface -->
    <line x1="35" y1="165" x2="240" y2="165" stroke="#795548" stroke-width="2"/>

    <!-- Block -->
    <rect x="80" y="140" width="40" height="25" rx="3" fill="#1565C0"/>
    <text x="100" y="157" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle">m</text>

    <!-- Displacement S -->
    {arrow(120, 152, 210, 152, "#2E7D32", 2.5, 9)}
    <text x="175" y="148" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" font-weight="bold" font-style="italic">S</text>

    <!-- Force F at angle -->
    {arrow(100, 140, 170, 100, "#E53935", 2.5, 9)}
    <text x="145" y="110" font-family="Arial,sans-serif" font-size="10" fill="#E53935" font-weight="bold" font-style="italic">F</text>

    <!-- Angle -->
    <path d="M 130 140 A 15 15 0 0 0 126 130" fill="none" stroke="#F57C00" stroke-width="1.5"/>
    <text x="135" y="130" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" font-style="italic">a</text>

    <!-- Component F*cos(a) along S -->
    {arrow(100, 165, 160, 165, "#42A5F5", 1.5, 6)}
    <text x="130" y="178" font-family="Arial,sans-serif" font-size="7" fill="#42A5F5">F*cos(a)</text>

    <!-- Formula -->
    <rect x="40" y="182" width="195" height="25" rx="3" fill="#E3F2FD" stroke="#E53935" stroke-width="1.5"/>
    <text x="137" y="200" font-family="Arial,sans-serif" font-size="12" fill="#E53935" text-anchor="middle" font-weight="bold">A = F*S*cos(a)</text>

    <!-- Sign of work -->
    <rect x="260" y="62" width="215" height="90" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Знак работы</text>
    <line x1="270" y1="83" x2="465" y2="83" stroke="#2E7D32" stroke-width="0.5" opacity="0.3"/>

    <!-- A > 0 -->
    <rect x="275" y="90" width="55" height="18" rx="3" fill="#E8F5E9" stroke="#2E7D32" stroke-width="0.8"/>
    <text x="302" y="103" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">A > 0</text>
    <text x="345" y="103" font-family="Arial,sans-serif" font-size="7" fill="#555">a &lt; 90 (разгон)</text>

    <!-- A < 0 -->
    <rect x="275" y="112" width="55" height="18" rx="3" fill="#FFEBEE" stroke="#E53935" stroke-width="0.8"/>
    <text x="302" y="125" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle">A &lt; 0</text>
    <text x="345" y="125" font-family="Arial,sans-serif" font-size="7" fill="#555">a > 90 (торможение)</text>

    <!-- A = 0 -->
    <rect x="275" y="134" width="55" height="18" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="302" y="147" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" text-anchor="middle">A = 0</text>
    <text x="345" y="147" font-family="Arial,sans-serif" font-size="7" fill="#555">a = 90 (перпенд.)</text>

    <!-- Units and properties -->
    <rect x="260" y="160" width="215" height="42" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="367" y="176" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">[A] = Дж = Н*м</text>
    <text x="367" y="192" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Работа — скаляр! Аддитивна: A(общ) = A1 + A2 + ...</text>

    <!-- Special cases -->
    <rect x="25" y="215" width="225" height="55" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="137" y="231" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Частные случаи</text>
    <text x="137" y="247" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Тяжести: A = mg*h</text>
    <text x="137" y="260" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Упругости: A = kx*x/2</text>

    <rect x="260" y="215" width="215" height="55" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="367" y="231" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Графический смысл</text>
    <text x="367" y="247" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">A = площадь под F(S)</text>
    <text x="367" y="260" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Работа силы тяжести не зависит от траектории!</text>
    '''
    svg += footer("Законы сохранения", 25)
    return svg


# ============================================================
# LESSON 26: Кинетическая и потенциальная энергия
# ============================================================
def lesson26():
    svg = header("Кинетическая и потенциальная энергия", "Физика 10 класс — Урок 26")
    svg += f'''
    <!-- Kinetic energy -->
    <rect x="25" y="62" width="225" height="130" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Кинетическая энергия</text>

    <!-- Moving body -->
    <rect x="40" y="110" width="35" height="25" rx="3" fill="#E53935" opacity="0.8"/>
    <text x="57" y="127" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle">m</text>

    <!-- Velocity -->
    {arrow(75, 122, 150, 122, "#2E7D32", 2.5, 9)}
    <text x="118" y="116" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" font-weight="bold">v</text>

    <!-- Formula -->
    <rect x="40" y="145" width="190" height="25" rx="3" fill="#FFEBEE" stroke="#E53935" stroke-width="1.5"/>
    <text x="135" y="163" font-family="Arial,sans-serif" font-size="12" fill="#E53935" text-anchor="middle" font-weight="bold">E(k) = mv*v/2</text>

    <text x="137" y="185" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Энергия движения | [E] = Дж</text>

    <!-- Potential energy -->
    <rect x="260" y="62" width="215" height="130" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Потенциальная энергия</text>

    <!-- Object at height h -->
    <rect x="345" y="100" width="30" height="22" rx="3" fill="#2E7D32" opacity="0.8"/>
    <text x="360" y="115" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">m</text>

    <!-- Height -->
    <line x1="340" y1="122" x2="340" y2="168" stroke="#F57C00" stroke-width="1.5" stroke-dasharray="3,2"/>
    <line x1="335" y1="122" x2="345" y2="122" stroke="#F57C00" stroke-width="1"/>
    <line x1="335" y1="168" x2="345" y2="168" stroke="#F57C00" stroke-width="1"/>
    <text x="330" y="150" font-family="Arial,sans-serif" font-size="10" fill="#F57C00" text-anchor="end" font-style="italic">h</text>

    <!-- Ground -->
    <line x1="300" y1="168" x2="460" y2="168" stroke="#795548" stroke-width="2"/>

    <!-- Gravity force -->
    {arrow(360, 122, 360, 158, "#E53935", 1.5, 6)}
    <text x="370" y="145" font-family="Arial,sans-serif" font-size="8" fill="#E53935">mg</text>

    <!-- Formula -->
    <rect x="270" y="145" width="195" height="25" rx="3" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1.5"/>
    <text x="367" y="163" font-family="Arial,sans-serif" font-size="12" fill="#2E7D32" text-anchor="middle" font-weight="bold">E(п) = mgh</text>

    <text x="367" y="185" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Энергия взаимодействия | [E] = Дж</text>

    <!-- Spring potential energy -->
    <rect x="25" y="205" width="225" height="65" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="137" y="221" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Потенциальная энергия пружины</text>

    <!-- Spring -->
    <path d="M 40 248 L 50 248 L 55 238 L 65 258 L 75 238 L 85 258 L 95 238 L 105 258 L 115 248 L 125 248" fill="none" stroke="#E53935" stroke-width="2"/>

    <!-- Extension -->
    {arrow(125, 248, 160, 248, "#F57C00", 2, 7)}
    <text x="145" y="243" font-family="Arial,sans-serif" font-size="8" fill="#F57C00">x</text>

    <text x="137" y="268" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">E(п) = kx*x/2</text>

    <!-- Relationship with work -->
    <rect x="260" y="205" width="215" height="65" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="367" y="221" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Связь с работой</text>
    <line x1="270" y1="226" x2="465" y2="226" stroke="#7B1FA2" stroke-width="0.5" opacity="0.3"/>
    <text x="367" y="242" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle">A = E(k2) - E(k1)</text>
    <text x="367" y="258" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">A = -(E(п2) - E(п1))</text>
    <text x="367" y="268" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Работа = изменение энергии</text>
    '''
    svg += footer("Законы сохранения", 26)
    return svg


# ============================================================
# LESSON 27: Закон сохранения энергии в механике
# ============================================================
def lesson27():
    svg = header("Закон сохранения энергии в механике", "Физика 10 класс — Урок 27")
    svg += f'''
    <!-- Pendulum at different positions -->
    <rect x="25" y="62" width="300" height="170" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="175" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Маятник: превращение энергии</text>

    <!-- Pivot -->
    <circle cx="175" cy="90" r="4" fill="#555"/>

    <!-- Position 1: top left (max height, v=0) -->
    <line x1="175" y1="90" x2="100" y2="130" stroke="#555" stroke-width="1.5"/>
    <circle cx="100" cy="130" r="8" fill="#E53935"/>
    <text x="100" y="134" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle">1</text>
    <text x="72" y="120" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">E(п)=max</text>
    <text x="72" y="130" font-family="Arial,sans-serif" font-size="7" fill="#E53935">E(k)=0</text>

    <!-- Position 2: bottom (max v, h=0) -->
    <line x1="175" y1="90" x2="175" y2="210" stroke="#555" stroke-width="1.5"/>
    <circle cx="175" cy="210" r="8" fill="#2E7D32"/>
    <text x="175" y="214" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle">2</text>
    <text x="195" y="205" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">E(п)=0</text>
    <text x="195" y="215" font-family="Arial,sans-serif" font-size="7" fill="#E53935">E(k)=max</text>
    <!-- Velocity at bottom -->
    {arrow(185, 210, 220, 210, "#2E7D32", 1.5, 5)}
    <text x="215" y="205" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">v(max)</text>

    <!-- Position 3: top right -->
    <line x1="175" y1="90" x2="250" y2="130" stroke="#555" stroke-width="1.5"/>
    <circle cx="250" cy="130" r="8" fill="#E53935"/>
    <text x="250" y="134" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle">3</text>
    <text x="262" y="120" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">E(п)=max</text>
    <text x="262" y="130" font-family="Arial,sans-serif" font-size="7" fill="#E53935">E(k)=0</text>

    <!-- Arc path -->
    <path d="M 100 130 Q 175 220 250 130" fill="none" stroke="#42A5F5" stroke-width="1.5" stroke-dasharray="4,2"/>

    <!-- Height labels -->
    <line x1="100" y1="215" x2="100" y2="130" stroke="#F57C00" stroke-width="1" stroke-dasharray="2,2"/>
    <text x="88" y="175" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" text-anchor="end">h</text>

    <!-- Formula -->
    <rect x="335" y="62" width="140" height="80" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
    <text x="405" y="78" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Закон сохранения</text>
    <line x1="345" y1="83" x2="465" y2="83" stroke="#2E7D32" stroke-width="0.5" opacity="0.3"/>
    <text x="405" y="100" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">E = const</text>
    <text x="405" y="118" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">E(k) + E(п) = const</text>
    <text x="405" y="132" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Если F(тр) = 0</text>

    <!-- Energy bar chart -->
    <rect x="335" y="150" width="140" height="82" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="405" y="165" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" font-weight="bold" text-anchor="middle">Распределение энергии</text>

    <!-- Position 1 bars -->
    <rect x="350" y="170" width="15" height="50" rx="1" fill="#2E7D32" opacity="0.7"/>
    <rect x="367" y="218" width="15" height="2" rx="1" fill="#E53935" opacity="0.7"/>
    <text x="365" y="228" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">1</text>

    <!-- Position 2 bars -->
    <rect x="395" y="218" width="15" height="2" rx="1" fill="#2E7D32" opacity="0.7"/>
    <rect x="412" y="170" width="15" height="50" rx="1" fill="#E53935" opacity="0.7"/>
    <text x="410" y="228" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">2</text>

    <!-- Position 3 bars -->
    <rect x="440" y="170" width="15" height="50" rx="1" fill="#2E7D32" opacity="0.7"/>
    <rect x="457" y="218" width="15" height="2" rx="1" fill="#E53935" opacity="0.7"/>
    <text x="455" y="228" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">3</text>

    <!-- Legend -->
    <rect x="350" y="217" width="10" height="5" fill="#2E7D32" opacity="0.7"/>
    <text x="365" y="222" font-family="Arial,sans-serif" font-size="6" fill="#555">E(п)</text>
    <rect x="395" y="217" width="10" height="5" fill="#E53935" opacity="0.7"/>
    <text x="410" y="222" font-family="Arial,sans-serif" font-size="6" fill="#555">E(k)</text>

    <!-- With friction -->
    <rect x="25" y="248" width="450" height="28" rx="4" fill="white" stroke="#E53935" stroke-width="1"/>
    <text x="250" y="266" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle">С трением: E(k1)+E(п1) = E(k2)+E(п2) + A(тр) | A(тр) = Q (теплота) | Энергия не исчезает!</text>
    '''
    svg += footer("Законы сохранения", 27)
    return svg


# ============================================================
# LESSON 28: Столкновения
# ============================================================
def lesson28():
    svg = header("Столкновения", "Физика 10 класс — Урок 28")
    svg += f'''
    <!-- Elastic collision -->
    <rect x="25" y="62" width="225" height="115" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Упругий удар</text>

    <!-- Before -->
    <text x="45" y="95" font-family="Arial,sans-serif" font-size="7" fill="#555">До:</text>
    <circle cx="70" cy="105" r="12" fill="#E53935" opacity="0.8"/>
    <text x="70" y="109" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">m1</text>
    {arrow(82, 105, 105, 105, "#E53935", 1.5, 5)}
    <circle cx="175" cy="105" r="9" fill="#1565C0" opacity="0.8"/>
    <text x="175" y="109" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">m2</text>

    <!-- After -->
    <text x="45" y="130" font-family="Arial,sans-serif" font-size="7" fill="#555">После:</text>
    <circle cx="80" cy="140" r="12" fill="#E53935" opacity="0.6"/>
    <text x="80" y="144" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">m1</text>
    {arrow(68, 140, 50, 140, "#E53935", 1, 4)}
    <circle cx="195" cy="140" r="9" fill="#1565C0" opacity="0.6"/>
    <text x="195" y="144" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">m2</text>
    {arrow(204, 140, 225, 140, "#1565C0", 1.5, 5)}

    <text x="137" y="165" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Сохраняются: p и E(k)</text>

    <!-- Inelastic collision -->
    <rect x="260" y="62" width="215" height="115" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Неупругий удар</text>

    <!-- Before -->
    <text x="275" y="95" font-family="Arial,sans-serif" font-size="7" fill="#555">До:</text>
    <circle cx="300" cy="105" r="12" fill="#E53935" opacity="0.8"/>
    <text x="300" y="109" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">m1</text>
    {arrow(312, 105, 335, 105, "#E53935", 1.5, 5)}
    <circle cx="405" cy="105" r="9" fill="#1565C0" opacity="0.8"/>
    <text x="405" y="109" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">m2</text>

    <!-- After: stuck together -->
    <text x="275" y="130" font-family="Arial,sans-serif" font-size="7" fill="#555">После:</text>
    <ellipse cx="360" cy="140" rx="22" ry="12" fill="#7B1FA2" opacity="0.7"/>
    <text x="360" y="144" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">m1+m2</text>
    {arrow(382, 140, 410, 140, "#7B1FA2", 1.5, 5)}
    <text x="400" y="135" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2">v'</text>

    <text x="367" y="165" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle">Сохраняется: p, Теряется: E(k)</text>

    <!-- Formulas -->
    <rect x="25" y="190" width="225" height="75" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="137" y="206" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Формулы</text>
    <line x1="35" y1="211" x2="240" y2="211" stroke="#1565C0" stroke-width="0.5" opacity="0.3"/>
    <text x="137" y="226" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">p = m1*v1 + m2*v2 = const</text>
    <text x="137" y="242" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Неупругий: v' = (m1*v1+m2*v2)/(m1+m2)</text>
    <text x="137" y="258" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle">Q = E(k1) - E(k2) (теплота)</text>

    <!-- Comparison -->
    <rect x="260" y="190" width="215" height="75" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="367" y="206" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Сравнение</text>
    <line x1="270" y1="211" x2="465" y2="211" stroke="#F57C00" stroke-width="0.5" opacity="0.3"/>

    <rect x="275" y="218" width="80" height="20" rx="3" fill="#E8F5E9" stroke="#2E7D32" stroke-width="0.8"/>
    <text x="315" y="232" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Упругий</text>
    <rect x="365" y="218" width="95" height="20" rx="3" fill="#FFEBEE" stroke="#E53935" stroke-width="0.8"/>
    <text x="412" y="232" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle">Неупругий</text>

    <text x="367" y="247" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">p + E(k) сохраняются</text>
    <text x="367" y="260" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle">p сохраняется, E(k) теряется</text>
    '''
    svg += footer("Законы сохранения", 28)
    return svg


# ============================================================
# LESSON 29: Условия равновесия твёрдого тела
# ============================================================
def lesson29():
    svg = header("Условия равновесия твёрдого тела", "Физика 10 класс — Урок 29")
    svg += f'''
    <!-- Two conditions of equilibrium -->
    <rect x="25" y="62" width="225" height="80" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">I условие: F(рез) = 0</text>

    <!-- Body with balanced forces -->
    <rect x="80" y="90" width="50" height="30" rx="4" fill="#1565C0" opacity="0.7"/>
    <!-- Left force -->
    {arrow(80, 105, 45, 105, "#E53935", 2, 7)}
    <!-- Right force -->
    {arrow(130, 105, 165, 105, "#E53935", 2, 7)}
    <!-- Up force -->
    {arrow(105, 90, 105, 70, "#2E7D32", 2, 7)}
    <!-- Down force -->
    {arrow(105, 120, 105, 140, "#2E7D32", 2, 7)}
    <text x="137" y="138" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Нет поступательного ускорения</text>

    <rect x="260" y="62" width="215" height="80" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">II условие: M(рез) = 0</text>

    <!-- Rod with balanced torques -->
    <rect x="290" y="100" width="150" height="6" rx="2" fill="#795548"/>
    <!-- Pivot -->
    <polygon points="365,106 358,120 372,120" fill="#555"/>

    <!-- Left torque -->
    {arrow(310, 98, 310, 80, "#E53935", 2, 7)}
    <text x="310" y="75" font-family="Arial,sans-serif" font-size="7" fill="#E53935">F1</text>
    <!-- Right torque -->
    {arrow(420, 108, 420, 128, "#2E7D32", 2, 7)}
    <text x="420" y="140" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">F2</text>

    <text x="367" y="138" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Нет вращательного ускорения</text>

    <!-- Types of equilibrium -->
    <rect x="25" y="155" width="155" height="110" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="102" y="170" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Устойчивое</text>

    <!-- Ball in valley -->
    <path d="M 45 230 Q 102 190 160 230" fill="none" stroke="#795548" stroke-width="2"/>
    <circle cx="102" cy="215" r="8" fill="#2E7D32" opacity="0.8"/>
    {arrow(110, 215, 118, 220, "#E53935", 1, 4)}
    <text x="102" y="250" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Возвращается</text>
    <text x="102" y="260" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">E(п) минимальна</text>

    <rect x="190" y="155" width="120" height="110" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="250" y="170" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Безразличное</text>

    <!-- Ball on flat surface -->
    <line x1="205" y1="225" x2="295" y2="225" stroke="#795548" stroke-width="2"/>
    <circle cx="250" cy="215" r="8" fill="#F57C00" opacity="0.8"/>
    {arrow(258, 215, 275, 215, "#E53935", 1, 4)}
    <text x="250" y="250" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Остаётся</text>
    <text x="250" y="260" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">E(п) = const</text>

    <rect x="320" y="155" width="155" height="110" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="397" y="170" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Неустойчивое</text>

    <!-- Ball on hill -->
    <path d="M 340 220 Q 397 180 455 220" fill="none" stroke="#795548" stroke-width="2"/>
    <circle cx="397" cy="195" r="8" fill="#E53935" opacity="0.8"/>
    {arrow(405, 195, 420, 210, "#E53935", 1, 4)}
    <text x="397" y="250" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Уходит</text>
    <text x="397" y="260" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">E(п) максимальна</text>
    '''
    svg += footer("Статика", 29)
    return svg


# ============================================================
# LESSON 30: Момент силы. Правило моментов
# ============================================================
def lesson30():
    svg = header("Момент силы. Правило моментов", "Физика 10 класс — Урок 30")
    svg += f'''
    <!-- Lever with forces -->
    <rect x="25" y="62" width="300" height="170" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="175" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Рычаг и правило моментов</text>

    <!-- Lever beam -->
    <rect x="45" y="140" width="260" height="6" rx="2" fill="#795548"/>

    <!-- Pivot (fulcrum) -->
    <polygon points="175,146 165,168 185,168" fill="#555"/>
    <line x1="155" y1="168" x2="195" y2="168" stroke="#555" stroke-width="2"/>

    <!-- Left force F1 (down) -->
    {arrow(80, 125, 80, 140, "#E53935", 2.5, 8)}
    <text x="80" y="120" font-family="Arial,sans-serif" font-size="10" fill="#E53935" font-weight="bold">F1</text>

    <!-- Right force F2 (down) -->
    {arrow(275, 125, 275, 140, "#2E7D32", 2.5, 8)}
    <text x="275" y="120" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" font-weight="bold">F2</text>

    <!-- Lever arm l1 -->
    <line x1="80" y1="155" x2="175" y2="155" stroke="#F57C00" stroke-width="1.5"/>
    <line x1="80" y1="150" x2="80" y2="160" stroke="#F57C00" stroke-width="1"/>
    <line x1="175" y1="150" x2="175" y2="160" stroke="#F57C00" stroke-width="1"/>
    <text x="127" y="165" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" text-anchor="middle" font-style="italic">l1</text>

    <!-- Lever arm l2 -->
    <line x1="175" y1="155" x2="275" y2="155" stroke="#7B1FA2" stroke-width="1.5"/>
    <line x1="275" y1="150" x2="275" y2="160" stroke="#7B1FA2" stroke-width="1"/>
    <text x="225" y="165" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" text-anchor="middle" font-style="italic">l2</text>

    <!-- Moment directions -->
    <text x="100" y="185" font-family="Arial,sans-serif" font-size="8" fill="#E53935">M1 = F1*l1</text>
    <text x="220" y="185" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32">M2 = F2*l2</text>

    <!-- Rotation arrows -->
    <path d="M 130 178 A 25 25 0 0 0 155 190" fill="none" stroke="#E53935" stroke-width="1.5"/>
    <polygon points="155,190 148,184 150,193" fill="#E53935"/>

    <path d="M 220 178 A 25 25 0 0 1 195 190" fill="none" stroke="#2E7D32" stroke-width="1.5"/>
    <polygon points="195,190 202,184 200,193" fill="#2E7D32"/>

    <!-- Formula -->
    <rect x="60" y="195" width="230" height="25" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
    <text x="175" y="213" font-family="Arial,sans-serif" font-size="11" fill="#1565C0" text-anchor="middle" font-weight="bold">M1 = M2 (равновесие)</text>

    <!-- Right panel: moment definition -->
    <rect x="335" y="62" width="140" height="85" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="405" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Момент силы</text>
    <line x1="345" y1="83" x2="465" y2="83" stroke="#E53935" stroke-width="0.5" opacity="0.3"/>
    <text x="405" y="100" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">M = F * l</text>
    <text x="405" y="115" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">l — плечо силы</text>
    <text x="405" y="128" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">[M] = Н*м</text>
    <text x="405" y="142" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle">+ по часовой, - против</text>

    <!-- Golden rule -->
    <rect x="335" y="155" width="140" height="77" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="405" y="170" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Золотое правило</text>
    <line x1="345" y1="175" x2="465" y2="175" stroke="#F57C00" stroke-width="0.5" opacity="0.3"/>
    <text x="405" y="192" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">F1/F2 = l2/l1</text>
    <text x="405" y="207" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Выигрыш в силе</text>
    <text x="405" y="219" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">= проигрыш в расстоянии</text>
    <text x="405" y="230" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle">A1 = A2 (работа)</text>
    '''
    svg += footer("Статика", 30)
    return svg


# ============================================================
# Generate
# ============================================================
generators = {
    21: lesson21, 22: lesson22, 23: lesson23,
    24: lesson24, 25: lesson25, 26: lesson26,
    27: lesson27, 28: lesson28, 29: lesson29, 30: lesson30,
}

for num, gen in generators.items():
    svg = gen()
    path = os.path.join(OUTPUT_DIR, f"lesson{num}.svg")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"lesson{num}.svg ({len(svg)} bytes)")

print("Done!")
