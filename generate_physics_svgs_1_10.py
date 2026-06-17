#!/usr/bin/env python3
"""Generate SVG illustrations for Physics Grade 10, Lessons 1-10 (Кинематика)
with real visual elements: graphs, vectors, diagrams, trajectories, etc.
"""

import os

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app-site/public/images/lessons/grade10/physics"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Color scheme for physics
C_PRIMARY = "#1565C0"
C_LIGHT = "#E3F2FD"
C_ACCENT = "#42A5F5"
C_DARK = "#0D47A1"
C_RED = "#E53935"
C_GREEN = "#2E7D32"
C_ORANGE = "#F57C00"
C_PURPLE = "#7B1FA2"

def header(title, subtitle, section="Кинематика", lesson_num=1):
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

def footer(section="Кинематика", lesson_num=1):
    return f'''
  </g>
  <rect x="12" y="298" width="476" height="42" rx="5" fill="url(#panel)"/>
  <text x="250" y="316" font-family="Arial,sans-serif" font-size="14" text-anchor="middle" fill="white" font-weight="bold">{section}</text>
  <text x="250" y="332" font-family="Arial,sans-serif" font-size="10" text-anchor="middle" fill="white" opacity="0.8">Урок {lesson_num}</text>
</svg>'''

def arrow(x1, y1, x2, y2, color="#1565C0", width=2):
    """SVG line with arrowhead"""
    import math
    dx = x2 - x1
    dy = y2 - y1
    length = math.sqrt(dx*dx + dy*dy)
    if length == 0:
        return ""
    ux, uy = dx/length, dy/length
    # Arrowhead
    ax = x2 - ux*8 - uy*4
    ay = y2 - uy*8 + ux*4
    bx = x2 - ux*8 + uy*4
    by = y2 - uy*8 - ux*4
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"/>'
    # We'll use marker-based arrows instead

def draw_arrow(x1, y1, x2, y2, color="#1565C0", width=2, head=8):
    """Draw a line with triangular arrowhead"""
    import math
    dx = x2 - x1
    dy = y2 - y1
    length = math.sqrt(dx*dx + dy*dy)
    if length < 1:
        return ""
    ux, uy = dx/length, dy/length
    px, py = -uy, ux  # perpendicular
    tip_x, tip_y = x2, y2
    left_x = tip_x - ux*head + px*head*0.4
    left_y = tip_y - uy*head + py*head*0.4
    right_x = tip_x - ux*head - px*head*0.4
    right_y = tip_y - uy*head - py*head*0.4
    return f'''<line x1="{x1}" y1="{y1}" x2="{x2-head*0.5*ux}" y2="{y2-head*0.5*uy}" stroke="{color}" stroke-width="{width}"/>
    <polygon points="{tip_x},{tip_y} {left_x},{left_y} {right_x},{right_y}" fill="{color}"/>'''

def draw_axis(ox, oy, x_len, y_len, x_label="", y_label=""):
    """Draw coordinate axes with labels"""
    lines = []
    # X axis
    lines.append(draw_arrow(ox, oy, ox+x_len, oy, "#333", 1.5, 7))
    # Y axis
    lines.append(draw_arrow(ox, oy, ox, oy-y_len, "#333", 1.5, 7))
    if x_label:
        lines.append(f'<text x="{ox+x_len-5}" y="{oy+16}" font-family="Arial,sans-serif" font-size="11" fill="#333" font-style="italic" text-anchor="end">{x_label}</text>')
    if y_label:
        lines.append(f'<text x="{ox-8}" y="{oy-y_len+5}" font-family="Arial,sans-serif" font-size="11" fill="#333" font-style="italic" text-anchor="end">{y_label}</text>')
    return "\n    ".join(lines)


# ============================================================
# LESSON 1: Классическая механика Ньютона
# ============================================================
def lesson1():
    svg = header("Классическая механика Ньютона", "Физика 10 класс — Урок 1")
    # Newton with apple tree sketch + 3 laws boxes
    # Tree trunk
    svg += '''
    <!-- Tree trunk -->
    <rect x="55" y="110" width="12" height="80" rx="3" fill="#795548"/>
    <!-- Tree crown -->
    <ellipse cx="61" cy="95" rx="35" ry="30" fill="#4CAF50" opacity="0.8"/>
    <ellipse cx="50" cy="85" rx="20" ry="18" fill="#66BB6A" opacity="0.7"/>
    <ellipse cx="75" cy="88" rx="18" ry="16" fill="#43A047" opacity="0.7"/>
    <!-- Apple falling -->
    <circle cx="88" cy="135" r="6" fill="#E53935"/>
    <line x1="88" y1="141" x2="88" y2="170" stroke="#E53935" stroke-width="1" stroke-dasharray="3,3"/>
    <!-- Small apple on tree -->
    <circle cx="75" cy="100" r="4" fill="#E53935"/>
    <!-- Newton figure (simplified) -->
    <circle cx="35" cy="155" r="8" fill="#FFCC80"/>
    <rect x="29" y="163" width="12" height="25" rx="3" fill="#5C6BC0"/>
    <!-- Ground -->
    <line x1="20" y1="190" x2="110" y2="190" stroke="#795548" stroke-width="1.5"/>
    <text x="65" y="205" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Закон тяготения</text>

    <!-- Three laws diagram -->
    <rect x="130" y="70" width="120" height="60" rx="6" fill="white" stroke="#1565C0" stroke-width="1.5"/>
    <text x="190" y="88" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">I закон</text>
    <text x="190" y="102" font-family="Arial,sans-serif" font-size="8" fill="#444" text-anchor="middle">Инерция: F=0</text>
    <!-- Arrow showing constant velocity -->
    <line x1="160" y1="118" x2="215" y2="118" stroke="#1565C0" stroke-width="2"/>
    <polygon points="215,118 208,114 208,122" fill="#1565C0"/>
    <text x="190" y="127" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">v = const</text>

    <rect x="265" y="70" width="120" height="60" rx="6" fill="white" stroke="#E53935" stroke-width="1.5"/>
    <text x="325" y="88" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">II закон</text>
    <text x="325" y="102" font-family="Arial,sans-serif" font-size="8" fill="#444" text-anchor="middle">F = m*a</text>
    <!-- Force arrow -->
    <line x1="295" y1="118" x2="355" y2="118" stroke="#E53935" stroke-width="2.5"/>
    <polygon points="355,118 348,113 348,123" fill="#E53935"/>
    <!-- Acceleration arrow -->
    <line x1="295" y1="126" x2="345" y2="126" stroke="#F57C00" stroke-width="1.5"/>
    <polygon points="345,126 339,122 339,130" fill="#F57C00"/>

    <rect x="130" y="145" width="120" height="55" rx="6" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
    <text x="190" y="163" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">III закон</text>
    <text x="190" y="177" font-family="Arial,sans-serif" font-size="8" fill="#444" text-anchor="middle">F1 = -F2</text>
    <!-- Two opposing arrows -->
    <line x1="170" y1="192" x2="210" y2="192" stroke="#2E7D32" stroke-width="2"/>
    <polygon points="210,192 204,188 204,196" fill="#2E7D32"/>
    <line x1="210" y1="192" x2="170" y2="192" stroke="#2E7D32" stroke-width="2" opacity="0.5"/>
    <polygon points="170,192 176,188 176,196" fill="#2E7D32" opacity="0.5"/>

    <!-- Scope of mechanics -->
    <rect x="265" y="145" width="120" height="55" rx="6" fill="white" stroke="#7B1FA2" stroke-width="1.5"/>
    <text x="325" y="163" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Область</text>
    <text x="325" y="175" font-family="Arial,sans-serif" font-size="8" fill="#444" text-anchor="middle">v &lt;&lt; c</text>
    <text x="325" y="187" font-family="Arial,sans-serif" font-size="8" fill="#444" text-anchor="middle">m &gt;&gt; m(атома)</text>
    <text x="325" y="197" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">Макромир</text>

    <!-- Bottom info bar -->
    <rect x="25" y="215" width="450" height="25" rx="4" fill="white" stroke="#1565C0" stroke-width="1" opacity="0.9"/>
    <text x="250" y="232" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">Классическая механика: кинематика + динамика + законы сохранения | Границы: релятивистские и квантовые эффекты</text>

    <!-- Decorative gear -->
    <circle cx="420" cy="100" r="18" fill="none" stroke="#1565C0" stroke-width="1.5" opacity="0.3"/>
    <circle cx="420" cy="100" r="12" fill="none" stroke="#1565C0" stroke-width="1" opacity="0.3"/>
    <circle cx="420" cy="100" r="5" fill="#1565C0" opacity="0.2"/>
    '''
    svg += footer("Кинематика", 1)
    return svg


# ============================================================
# LESSON 2: Положение тела в пространстве. Системы отсчёта
# ============================================================
def lesson2():
    svg = header("Положение тела в пространстве", "Системы отсчёта — Урок 2")
    # Coordinate system with reference point, body, and vectors
    svg += f'''
    <!-- 3D coordinate system -->
    {draw_axis(200, 200, 150, 120, "x", "y")}
    <!-- Z axis (perspective) -->
    <line x1="200" y1="200" x2="155" y2="230" stroke="#333" stroke-width="1.5"/>
    <polygon points="155,230 160,222 150,225" fill="#333"/>
    <text x="148" y="242" font-family="Arial,sans-serif" font-size="11" fill="#333" font-style="italic" text-anchor="end">z</text>

    <!-- Reference point O -->
    <circle cx="200" cy="200" r="4" fill="#E53935"/>
    <text x="208" y="210" font-family="Arial,sans-serif" font-size="10" fill="#E53935" font-weight="bold">O</text>

    <!-- Body position -->
    <circle cx="310" cy="130" r="7" fill="#1565C0"/>
    <text x="320" y="128" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold">M</text>

    <!-- Position vector r -->
    <line x1="200" y1="200" x2="306" y2="134" stroke="#E53935" stroke-width="2" stroke-dasharray="5,3"/>
    <polygon points="306,134 296,137 299,128" fill="#E53935"/>
    <text x="245" y="158" font-family="Arial,sans-serif" font-size="12" fill="#E53935" font-weight="bold" font-style="italic">r</text>

    <!-- Projections on axes -->
    <line x1="310" y1="130" x2="310" y2="200" stroke="#42A5F5" stroke-width="1" stroke-dasharray="3,2"/>
    <line x1="310" y1="200" x2="200" y2="200" stroke="#42A5F5" stroke-width="1" stroke-dasharray="3,2"/>
    <text x="310" y="212" font-family="Arial,sans-serif" font-size="9" fill="#42A5F5">x</text>
    <text x="185" y="130" font-family="Arial,sans-serif" font-size="9" fill="#42A5F5">y</text>

    <!-- Reference body -->
    <rect x="25" y="70" width="115" height="80" rx="6" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="82" y="86" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Система отсчёта</text>
    <line x1="35" y1="92" x2="130" y2="92" stroke="#1565C0" stroke-width="0.5" opacity="0.3"/>
    <rect x="35" y="97" width="95" height="18" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="82" y="110" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Тело отсчёта</text>
    <rect x="35" y="120" width="95" height="18" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="82" y="133" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Система координат</text>

    <!-- Clock icon for time -->
    <circle cx="82" cy="168" r="14" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <line x1="82" y1="168" x2="82" y2="158" stroke="#1565C0" stroke-width="1.5"/>
    <line x1="82" y1="168" x2="90" y2="168" stroke="#1565C0" stroke-width="1"/>
    <text x="82" y="192" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Часы (время)</text>

    <!-- Info boxes on the right -->
    <rect x="370" y="70" width="100" height="50" rx="5" fill="white" stroke="#2E7D32" stroke-width="1"/>
    <text x="420" y="88" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" font-weight="bold" text-anchor="middle">Материальная</text>
    <text x="420" y="100" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" font-weight="bold" text-anchor="middle">точка</text>
    <text x="420" y="114" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Модель: размер ~ 0</text>

    <rect x="370" y="130" width="100" height="50" rx="5" fill="white" stroke="#F57C00" stroke-width="1"/>
    <text x="420" y="148" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" font-weight="bold" text-anchor="middle">Радиус-вектор</text>
    <text x="420" y="160" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">r = x*i + y*j + z*k</text>
    <text x="420" y="174" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">|r| = sqrt(x+y+z)</text>

    <!-- Bottom -->
    <rect x="25" y="240" width="450" height="22" rx="4" fill="white" stroke="#1565C0" stroke-width="1" opacity="0.9"/>
    <text x="250" y="255" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Система отсчёта = тело отсчёта + система координат + часы | Положение задаётся радиус-вектором</text>
    '''
    svg += footer("Кинематика", 2)
    return svg


# ============================================================
# LESSON 3: Перемещение. Путь
# ============================================================
def lesson3():
    svg = header("Перемещение. Путь", "Физика 10 класс — Урок 3")
    svg += f'''
    <!-- Trajectory (curved path) -->
    <path d="M 80 200 C 130 180, 170 100, 220 120 S 310 80, 350 150" fill="none" stroke="#42A5F5" stroke-width="2.5" stroke-linecap="round"/>

    <!-- Start point -->
    <circle cx="80" cy="200" r="5" fill="#2E7D32"/>
    <text x="68" y="215" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold">A</text>

    <!-- End point -->
    <circle cx="350" cy="150" r="5" fill="#E53935"/>
    <text x="358" y="148" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold">B</text>

    <!-- Displacement vector (straight line A to B) -->
    <line x1="80" y1="200" x2="345" y2="154" stroke="#E53935" stroke-width="2"/>
    <polygon points="345,154 335,160 338,150" fill="#E53935"/>
    <text x="200" y="165" font-family="Arial,sans-serif" font-size="12" fill="#E53935" font-weight="bold" font-style="italic">S</text>
    <text x="212" y="165" font-family="Arial,sans-serif" font-size="8" fill="#E53935">— перемещение</text>

    <!-- Path label on curve -->
    <text x="180" y="95" font-family="Arial,sans-serif" font-size="10" fill="#42A5F5" font-weight="bold" font-style="italic">l</text>
    <text x="190" y="95" font-family="Arial,sans-serif" font-size="8" fill="#42A5F5">— путь</text>

    <!-- Arrow on trajectory -->
    <polygon points="285,102 278,110 275,100" fill="#42A5F5"/>

    <!-- Comparison box -->
    <rect x="30" y="62" width="200" height="60" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="130" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Путь vs Перемещение</text>
    <line x1="40" y1="83" x2="220" y2="83" stroke="#1565C0" stroke-width="0.5" opacity="0.3"/>
    <circle cx="50" cy="94" r="4" fill="#42A5F5"/>
    <text x="60" y="98" font-family="Arial,sans-serif" font-size="8" fill="#333">l — длина траектории (скаляр)</text>
    <circle cx="50" cy="110" r="4" fill="#E53935"/>
    <text x="60" y="114" font-family="Arial,sans-serif" font-size="8" fill="#333">S — вектор от A к B</text>

    <!-- Key formula -->
    <rect x="370" y="62" width="105" height="70" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="422" y="80" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Формулы</text>
    <line x1="380" y1="85" x2="465" y2="85" stroke="#F57C00" stroke-width="0.5" opacity="0.3"/>
    <text x="422" y="100" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">|S| &lt;= l</text>
    <text x="422" y="116" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">S = r - r0</text>
    <text x="422" y="128" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Sx = x - x0</text>

    <!-- Circular path example -->
    <circle cx="420" cy="210" r="40" fill="none" stroke="#42A5F5" stroke-width="2" stroke-dasharray="4,2"/>
    <circle cx="380" cy="210" r="4" fill="#2E7D32"/>
    <circle cx="380" cy="170" r="4" fill="#E53935"/>
    <text x="370" y="225" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">A</text>
    <text x="370" y="167" font-family="Arial,sans-serif" font-size="7" fill="#E53935">B</text>
    <!-- Displacement for half circle -->
    <line x1="380" y1="210" x2="380" y2="174" stroke="#E53935" stroke-width="1.5"/>
    <polygon points="380,174 376,182 384,182" fill="#E53935"/>
    <text x="400" y="195" font-family="Arial,sans-serif" font-size="7" fill="#555">l = pi*R</text>
    <text x="400" y="207" font-family="Arial,sans-serif" font-size="7" fill="#555">|S| = 2R</text>

    <!-- Bottom note -->
    <rect x="25" y="250" width="450" height="20" rx="4" fill="white" stroke="#1565C0" stroke-width="1" opacity="0.9"/>
    <text x="250" y="264" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">При прямолинейном движении в одну сторону: |S| = l | При криволинейном: |S| &lt; l</text>
    '''
    svg += footer("Кинематика", 3)
    return svg


# ============================================================
# LESSON 4: Скорость
# ============================================================
def lesson4():
    svg = header("Скорость", "Физика 10 класс — Урок 4")
    svg += f'''
    <!-- Speedometer/gauge -->
    <path d="M 95 210 A 55 55 0 0 1 35 210" fill="none" stroke="#1565C0" stroke-width="3" stroke-linecap="round"/>
    <!-- Speedometer ticks -->
    <line x1="42" y1="195" x2="52" y2="190" stroke="#1565C0" stroke-width="1.5"/>
    <line x1="55" y1="175" x2="63" y2="170" stroke="#1565C0" stroke-width="1.5"/>
    <line x1="75" y1="163" x2="80" y2="172" stroke="#1565C0" stroke-width="1.5"/>
    <line x1="95" y1="158" x2="95" y2="168" stroke="#1565C0" stroke-width="1.5"/>
    <line x1="115" y1="163" x2="110" y2="172" stroke="#1565C0" stroke-width="1.5"/>
    <line x1="135" y1="175" x2="127" y2="170" stroke="#E53935" stroke-width="1.5"/>
    <line x1="148" y1="195" x2="138" y2="190" stroke="#E53935" stroke-width="1.5"/>
    <!-- Needle -->
    <line x1="95" y1="210" x2="128" y2="178" stroke="#E53935" stroke-width="2"/>
    <circle cx="95" cy="210" r="4" fill="#E53935"/>
    <text x="30" y="225" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">0</text>
    <text x="140" y="225" font-family="Arial,sans-serif" font-size="7" fill="#E53935">max</text>
    <text x="95" y="245" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-style="italic">v, м/с</text>

    <!-- Velocity vector diagram -->
    <circle cx="260" cy="160" r="5" fill="#1565C0"/>
    <!-- v vector -->
    <line x1="260" y1="160" x2="370" y2="160" stroke="#E53935" stroke-width="2.5"/>
    <polygon points="370,160 362,155 362,165" fill="#E53935"/>
    <text x="320" y="155" font-family="Arial,sans-serif" font-size="11" fill="#E53935" font-weight="bold" font-style="italic">v</text>

    <!-- Trajectory for velocity -->
    <path d="M 230 185 Q 280 175 340 185" fill="none" stroke="#42A5F5" stroke-width="1.5" stroke-dasharray="4,2"/>
    <text x="290" y="200" font-family="Arial,sans-serif" font-size="8" fill="#42A5F5">траектория</text>

    <!-- Formulas box -->
    <rect x="175" y="68" width="140" height="70" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="245" y="84" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Формулы</text>
    <line x1="185" y1="88" x2="305" y2="88" stroke="#1565C0" stroke-width="0.5" opacity="0.3"/>
    <text x="195" y="103" font-family="Arial,sans-serif" font-size="9" fill="#333">v = S / t</text>
    <text x="195" y="117" font-family="Arial,sans-serif" font-size="9" fill="#333">v = dx/dt</text>
    <text x="195" y="131" font-family="Arial,sans-serif" font-size="8" fill="#555">[v] = м/с</text>

    <!-- Average vs Instantaneous -->
    <rect x="340" y="68" width="140" height="70" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="410" y="84" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Виды скорости</text>
    <line x1="350" y1="88" x2="470" y2="88" stroke="#F57C00" stroke-width="0.5" opacity="0.3"/>
    <text x="360" y="103" font-family="Arial,sans-serif" font-size="8" fill="#333">v(ср) = l / t</text>
    <text x="360" y="117" font-family="Arial,sans-serif" font-size="8" fill="#333">v(мгн) = lim(dS/dt)</text>
    <text x="360" y="131" font-family="Arial,sans-serif" font-size="7" fill="#555">Скорость — вектор!</text>

    <!-- Graph: v(t) = const -->
    <rect x="390" y="160" width="90" height="70" rx="4" fill="white" stroke="#1565C0" stroke-width="1"/>
    {draw_axis(400, 220, 70, 50, "t", "v")}
    <line x1="400" y1="195" x2="465" y2="195" stroke="#E53935" stroke-width="2"/>
    <text x="420" y="190" font-family="Arial,sans-serif" font-size="7" fill="#E53935">v = const</text>

    <!-- Bottom note -->
    <rect x="25" y="258" width="450" height="20" rx="4" fill="white" stroke="#1565C0" stroke-width="1" opacity="0.9"/>
    <text x="250" y="272" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Скорость — векторная величина | Направление v совпадает с направлением перемещения</text>
    '''
    svg += footer("Кинематика", 4)
    return svg


# ============================================================
# LESSON 5: Равномерное прямолинейное движение
# ============================================================
def lesson5():
    svg = header("Равномерное прямолинейное движение", "Физика 10 класс — Урок 5")
    svg += f'''
    <!-- Graph x(t) - linear -->
    <rect x="25" y="62" width="220" height="115" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="135" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">График x(t)</text>
    <!-- Axes -->
    {draw_axis(55, 160, 170, 85, "t", "x")}
    <!-- Linear graph x = x0 + vt -->
    <line x1="55" y1="145" x2="210" y2="82" stroke="#E53935" stroke-width="2.5"/>
    <!-- x0 mark -->
    <line x1="50" y1="145" x2="55" y2="145" stroke="#333" stroke-width="1"/>
    <text x="47" y="149" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="end">x0</text>
    <!-- Slope label -->
    <text x="150" y="105" font-family="Arial,sans-serif" font-size="8" fill="#E53935" font-style="italic">tg(a) = v</text>
    <!-- Angle arc -->
    <path d="M 70 160 A 20 20 0 0 1 65 145" fill="none" stroke="#E53935" stroke-width="1"/>
    <text x="78" y="155" font-family="Arial,sans-serif" font-size="8" fill="#E53935">a</text>

    <!-- Graph v(t) - horizontal line -->
    <rect x="260" y="62" width="215" height="115" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">График v(t)</text>
    {draw_axis(290, 160, 160, 85, "t", "v")}
    <!-- Horizontal line v = const -->
    <line x1="290" y1="120" x2="445" y2="120" stroke="#2E7D32" stroke-width="2.5"/>
    <text x="300" y="115" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32">v = const</text>

    <!-- Shaded area = displacement -->
    <rect x="290" y="120" width="100" height="40" fill="#2E7D32" opacity="0.15" stroke="none"/>
    <text x="340" y="145" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">S = v*t</text>

    <!-- Moving body diagram -->
    <rect x="25" y="195" width="450" height="50" rx="5" fill="white" stroke="#1565C0" stroke-width="1"/>
    <!-- Body at positions -->
    <rect x="40" y="208" width="20" height="14" rx="3" fill="#1565C0"/>
    <text x="50" y="235" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">t1</text>

    <rect x="110" y="208" width="20" height="14" rx="3" fill="#1565C0" opacity="0.9"/>
    <text x="120" y="235" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">t2</text>

    <rect x="180" y="208" width="20" height="14" rx="3" fill="#1565C0" opacity="0.8"/>
    <text x="190" y="235" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">t3</text>

    <!-- Equal spacing arrows -->
    <line x1="65" y1="215" x2="105" y2="215" stroke="#E53935" stroke-width="1.5"/>
    <polygon points="105,215 99,211 99,219" fill="#E53935"/>
    <line x1="135" y1="215" x2="175" y2="215" stroke="#E53935" stroke-width="1.5"/>
    <polygon points="175,215 169,211 169,219" fill="#E53935"/>
    <text x="85" y="210" font-family="Arial,sans-serif" font-size="7" fill="#E53935">v*dt</text>
    <text x="155" y="210" font-family="Arial,sans-serif" font-size="7" fill="#E53935">v*dt</text>

    <!-- Formula box -->
    <rect x="250" y="195" width="225" height="50" rx="4" fill="white" stroke="#F57C00" stroke-width="1"/>
    <text x="362" y="210" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Уравнение движения</text>
    <text x="362" y="228" font-family="Arial,sans-serif" font-size="11" fill="#333" text-anchor="middle">x(t) = x0 + v*t</text>
    <text x="362" y="240" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">v = const, a = 0</text>
    '''
    svg += footer("Кинематика", 5)
    return svg


# ============================================================
# LESSON 6: Решение задач кинематики
# ============================================================
def lesson6():
    svg = header("Решение задач кинематики", "Физика 10 класс — Урок 6")
    svg += f'''
    <!-- Algorithm steps -->
    <rect x="30" y="65" width="440" height="30" rx="5" fill="#1565C0" opacity="0.1" stroke="#1565C0" stroke-width="1"/>
    <text x="250" y="85" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" font-weight="bold" text-anchor="middle">Алгоритм решения задач по кинематике</text>

    <!-- Step boxes -->
    <rect x="30" y="102" width="85" height="40" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <circle cx="42" cy="114" r="8" fill="#1565C0"/>
    <text x="42" y="118" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">1</text>
    <text x="72" y="117" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Записать</text>
    <text x="72" y="128" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">дано</text>
    <!-- Arrow -->
    <line x1="118" y1="122" x2="128" y2="122" stroke="#1565C0" stroke-width="1.5"/>
    <polygon points="128,122 124,118 124,126" fill="#1565C0"/>

    <rect x="132" y="102" width="85" height="40" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <circle cx="144" cy="114" r="8" fill="#1565C0"/>
    <text x="144" y="118" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">2</text>
    <text x="174" y="117" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Выбрать</text>
    <text x="174" y="128" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">с.о.</text>
    <line x1="220" y1="122" x2="230" y2="122" stroke="#1565C0" stroke-width="1.5"/>
    <polygon points="230,122 226,118 226,126" fill="#1565C0"/>

    <rect x="234" y="102" width="85" height="40" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <circle cx="246" cy="114" r="8" fill="#E53935"/>
    <text x="246" y="118" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">3</text>
    <text x="276" y="117" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Записать</text>
    <text x="276" y="128" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">уравнения</text>
    <line x1="322" y1="122" x2="332" y2="122" stroke="#1565C0" stroke-width="1.5"/>
    <polygon points="332,122 328,118 328,126" fill="#1565C0"/>

    <rect x="336" y="102" width="85" height="40" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <circle cx="348" cy="114" r="8" fill="#2E7D32"/>
    <text x="348" y="118" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">4</text>
    <text x="378" y="117" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Решить</text>
    <text x="378" y="128" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">систему</text>

    <!-- Example problem: two bodies meeting -->
    <rect x="30" y="155" width="440" height="105" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="250" y="172" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Пример: встреча двух тел</text>
    <line x1="40" y1="177" x2="460" y2="177" stroke="#F57C00" stroke-width="0.5" opacity="0.3"/>

    <!-- Mini x(t) graph with two lines crossing -->
    {draw_axis(60, 248, 130, 60, "t", "x")}
    <!-- Body 1: from left going right -->
    <line x1="60" y1="210" x2="175" y2="195" stroke="#E53935" stroke-width="2"/>
    <!-- Body 2: from right going left -->
    <line x1="60" y1="195" x2="175" y2="210" stroke="#1565C0" stroke-width="2"/>
    <!-- Meeting point -->
    <circle cx="118" cy="202" r="4" fill="#F57C00"/>
    <text x="128" y="200" font-family="Arial,sans-serif" font-size="7" fill="#F57C00" font-weight="bold">встреча</text>
    <text x="80" y="207" font-family="Arial,sans-serif" font-size="7" fill="#E53935">x1(t)</text>
    <text x="80" y="193" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">x2(t)</text>

    <!-- Equations -->
    <text x="260" y="192" font-family="Arial,sans-serif" font-size="9" fill="#E53935">x1 = x01 + v1*t</text>
    <text x="260" y="207" font-family="Arial,sans-serif" font-size="9" fill="#1565C0">x2 = x02 + v2*t</text>
    <text x="260" y="225" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold">x1 = x2 => t(встр)</text>
    <text x="260" y="240" font-family="Arial,sans-serif" font-size="8" fill="#555">Подставить t в любое уравнение</text>

    <!-- Bottom -->
    <rect x="25" y="268" width="450" height="20" rx="4" fill="white" stroke="#1565C0" stroke-width="1" opacity="0.9"/>
    <text x="250" y="282" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Ключ: правильный выбор системы отсчёта и запись уравнений для каждого тела</text>
    '''
    svg += footer("Кинематика", 6)
    return svg


# ============================================================
# LESSON 7: Сложение движений
# ============================================================
def lesson7():
    svg = header("Сложение движений", "Физика 10 класс — Урок 7")
    svg += f'''
    <!-- Vector addition diagram -->
    <rect x="25" y="62" width="225" height="130" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Сложение скоростей</text>

    <!-- v1 vector -->
    <line x1="60" y1="155" x2="170" y2="155" stroke="#E53935" stroke-width="2.5"/>
    <polygon points="170,155 162,150 162,160" fill="#E53935"/>
    <text x="115" y="150" font-family="Arial,sans-serif" font-size="10" fill="#E53935" font-weight="bold" font-style="italic">v1</text>

    <!-- v2 vector (from tip of v1) -->
    <line x1="170" y1="155" x2="210" y2="100" stroke="#2E7D32" stroke-width="2.5"/>
    <polygon points="210,100 203,108 212,106" fill="#2E7D32"/>
    <text x="200" y="122" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" font-weight="bold" font-style="italic">v2</text>

    <!-- Resultant v vector -->
    <line x1="60" y1="155" x2="210" y2="100" stroke="#F57C00" stroke-width="2" stroke-dasharray="5,3"/>
    <polygon points="210,100 202,105 204,95" fill="#F57C00"/>
    <text x="125" y="115" font-family="Arial,sans-serif" font-size="10" fill="#F57C00" font-weight="bold" font-style="italic">v</text>

    <!-- Formula -->
    <text x="137" y="182" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle">v = v1 + v2</text>

    <!-- River crossing example -->
    <rect x="260" y="62" width="215" height="130" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Переправа через реку</text>

    <!-- River -->
    <rect x="340" y="85" width="120" height="100" fill="#42A5F5" opacity="0.2" rx="3"/>
    <!-- River flow arrows -->
    <line x1="350" y1="100" x2="420" y2="100" stroke="#42A5F5" stroke-width="1.5"/>
    <polygon points="420,100 414,96 414,104" fill="#42A5F5"/>
    <line x1="350" y1="125" x2="420" y2="125" stroke="#42A5F5" stroke-width="1.5"/>
    <polygon points="420,125 414,121 414,129" fill="#42A5F5"/>
    <line x1="350" y1="150" x2="420" y2="150" stroke="#42A5F5" stroke-width="1.5"/>
    <polygon points="420,150 414,146 414,154" fill="#42A5F5"/>
    <text x="390" y="95" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">v(реки)</text>

    <!-- Boat velocity (upward) -->
    <line x1="380" y1="175" x2="380" y2="95" stroke="#2E7D32" stroke-width="2"/>
    <polygon points="380,95 375,103 385,103" fill="#2E7D32"/>
    <text x="374" y="90" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">v(лодки)</text>

    <!-- Resultant path -->
    <line x1="380" y1="175" x2="445" y2="95" stroke="#F57C00" stroke-width="1.5" stroke-dasharray="4,2"/>
    <text x="425" y="130" font-family="Arial,sans-serif" font-size="7" fill="#F57C00">v</text>

    <!-- Banks -->
    <line x1="340" y1="85" x2="340" y2="185" stroke="#795548" stroke-width="2"/>
    <line x1="460" y1="85" x2="460" y2="185" stroke="#795548" stroke-width="2"/>
    <text x="340" y="193" font-family="Arial,sans-serif" font-size="7" fill="#795548">A</text>
    <text x="460" y="193" font-family="Arial,sans-serif" font-size="7" fill="#795548">B</text>

    <!-- Law of addition -->
    <rect x="25" y="205" width="225" height="65" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="137" y="222" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Закон сложения скоростей</text>
    <text x="137" y="240" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle">v = v1 + v2</text>
    <text x="137" y="255" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">v1 — относительная, v2 — переносная</text>
    <text x="137" y="265" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">v — абсолютная скорость</text>

    <!-- Independence of motions -->
    <rect x="260" y="205" width="215" height="65" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="367" y="222" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Независимость движений</text>
    <text x="367" y="240" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">x(t) = x0 + vx*t</text>
    <text x="367" y="255" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">y(t) = y0 + vy*t</text>
    <text x="367" y="265" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Движения по осям независимы</text>
    '''
    svg += footer("Кинематика", 7)
    return svg


# ============================================================
# LESSON 8: Ускорение. Равноускоренное движение
# ============================================================
def lesson8():
    svg = header("Ускорение. Равноускоренное движение", "Физика 10 класс — Урок 8")
    svg += f'''
    <!-- Acceleration vector diagram -->
    <rect x="25" y="62" width="220" height="120" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="135" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Ускорение</text>

    <!-- v1 (shorter) -->
    <line x1="50" y1="150" x2="110" y2="150" stroke="#42A5F5" stroke-width="2.5"/>
    <polygon points="110,150 103,145 103,155" fill="#42A5F5"/>
    <text x="80" y="145" font-family="Arial,sans-serif" font-size="9" fill="#42A5F5" font-weight="bold" font-style="italic">v0</text>

    <!-- v2 (longer) -->
    <line x1="50" y1="120" x2="160" y2="120" stroke="#E53935" stroke-width="2.5"/>
    <polygon points="160,120 153,115 153,125" fill="#E53935"/>
    <text x="110" y="115" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" font-style="italic">v</text>

    <!-- Delta v -->
    <line x1="110" y1="150" x2="160" y2="120" stroke="#F57C00" stroke-width="2"/>
    <polygon points="160,120 151,121 155,130" fill="#F57C00"/>
    <text x="145" y="142" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" font-weight="bold">dv</text>

    <!-- Formula -->
    <text x="135" y="170" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle">a = dv/dt = (v-v0)/t</text>

    <!-- v(t) graph -->
    <rect x="260" y="62" width="215" height="120" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">График v(t)</text>
    {draw_axis(285, 165, 160, 75, "t", "v")}
    <!-- v(t) = v0 + at - linear increasing -->
    <line x1="285" y1="140" x2="430" y2="90" stroke="#E53935" stroke-width="2.5"/>
    <!-- v0 -->
    <line x1="280" y1="140" x2="285" y2="140" stroke="#333" stroke-width="1"/>
    <text x="275" y="144" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="end">v0</text>
    <!-- Slope = a -->
    <text x="370" y="110" font-family="Arial,sans-serif" font-size="8" fill="#E53935" font-style="italic">tg(a) = a</text>

    <!-- x(t) parabola -->
    <rect x="25" y="195" width="220" height="85" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="135" y="211" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">График x(t) — парабола</text>
    {draw_axis(50, 268, 170, 55, "t", "x")}
    <!-- Parabolic curve -->
    <path d="M 50 260 Q 130 250 210 215" fill="none" stroke="#2E7D32" stroke-width="2.5"/>

    <!-- Key formulas -->
    <rect x="260" y="195" width="215" height="85" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="367" y="211" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Формулы</text>
    <line x1="270" y1="216" x2="465" y2="216" stroke="#F57C00" stroke-width="0.5" opacity="0.3"/>
    <text x="367" y="232" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">v = v0 + a*t</text>
    <text x="367" y="248" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">x = x0 + v0*t + a*t*t/2</text>
    <text x="367" y="264" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">S = (v*v - v0*v0)/(2a)</text>
    <text x="367" y="276" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">[a] = м/с/с</text>
    '''
    svg += footer("Кинематика", 8)
    return svg


# ============================================================
# LESSON 9: Решение задач равноускоренного движения
# ============================================================
def lesson9():
    svg = header("Решение задач равноускоренного движения", "Физика 10 класс — Урок 9")
    svg += f'''
    <!-- Free fall problem -->
    <rect x="25" y="62" width="225" height="135" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Свободное падение</text>

    <!-- Building -->
    <rect x="45" y="90" width="30" height="90" fill="#78909C" opacity="0.4" stroke="#546E7A" stroke-width="1"/>
    <rect x="50" y="100" width="8" height="10" fill="#42A5F5" opacity="0.5"/>
    <rect x="62" y="100" width="8" height="10" fill="#42A5F5" opacity="0.5"/>
    <rect x="50" y="120" width="8" height="10" fill="#42A5F5" opacity="0.5"/>
    <rect x="62" y="120" width="8" height="10" fill="#42A5F5" opacity="0.5"/>
    <rect x="50" y="140" width="8" height="10" fill="#42A5F5" opacity="0.5"/>
    <rect x="62" y="140" width="8" height="10" fill="#42A5F5" opacity="0.5"/>

    <!-- Falling ball trajectory -->
    <circle cx="60" cy="92" r="5" fill="#E53935"/>
    <circle cx="60" cy="110" r="4" fill="#E53935" opacity="0.7"/>
    <circle cx="60" cy="130" r="4" fill="#E53935" opacity="0.5"/>
    <circle cx="60" cy="155" r="4" fill="#E53935" opacity="0.3"/>
    <!-- Arrow -->
    <line x1="60" y1="160" x2="60" y2="180" stroke="#E53935" stroke-width="1.5"/>
    <polygon points="60,180 56,172 64,172" fill="#E53935"/>

    <!-- Height label -->
    <line x1="35" y1="92" x2="35" y2="180" stroke="#2E7D32" stroke-width="1" stroke-dasharray="3,2"/>
    <line x1="30" y1="92" x2="40" y2="92" stroke="#2E7D32" stroke-width="1"/>
    <line x1="30" y1="180" x2="40" y2="180" stroke="#2E7D32" stroke-width="1"/>
    <text x="33" y="140" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="end">H</text>

    <!-- g arrow -->
    <line x1="95" y1="100" x2="95" y2="140" stroke="#F57C00" stroke-width="2"/>
    <polygon points="95,140 91,132 99,132" fill="#F57C00"/>
    <text x="105" y="125" font-family="Arial,sans-serif" font-size="10" fill="#F57C00" font-weight="bold">g</text>
    <text x="105" y="138" font-family="Arial,sans-serif" font-size="7" fill="#555">= 9.8 м/с/с</text>

    <!-- Equations -->
    <text x="160" y="100" font-family="Arial,sans-serif" font-size="8" fill="#333">y = H - g*t*t/2</text>
    <text x="160" y="115" font-family="Arial,sans-serif" font-size="8" fill="#333">v = g*t</text>
    <text x="160" y="130" font-family="Arial,sans-serif" font-size="8" fill="#333">H = g*T*T/2</text>
    <text x="160" y="148" font-family="Arial,sans-serif" font-size="8" fill="#E53935" font-weight="bold">T = sqrt(2H/g)</text>
    <text x="160" y="165" font-family="Arial,sans-serif" font-size="8" fill="#555">v(кон) = sqrt(2gH)</text>

    <!-- Throw up problem -->
    <rect x="260" y="62" width="215" height="135" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Бросок вертикально вверх</text>

    <!-- Trajectory: parabola up and down -->
    <path d="M 340 185 Q 400 70 340 185" fill="none" stroke="#2E7D32" stroke-width="2"/>
    <!-- v0 arrow up -->
    <line x1="340" y1="185" x2="340" y2="80" stroke="#E53935" stroke-width="2"/>
    <polygon points="340,80 336,88 344,88" fill="#E53935"/>
    <text x="352" y="110" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold">v0</text>

    <!-- Top point -->
    <circle cx="370" cy="88" r="3" fill="#F57C00"/>
    <text x="382" y="92" font-family="Arial,sans-serif" font-size="7" fill="#F57C00">v=0</text>
    <text x="382" y="102" font-family="Arial,sans-serif" font-size="7" fill="#F57C00">h(max)</text>

    <!-- Key results -->
    <text x="370" y="140" font-family="Arial,sans-serif" font-size="8" fill="#333">h(max) = v0*v0/(2g)</text>
    <text x="370" y="155" font-family="Arial,sans-serif" font-size="8" fill="#333">t(под) = v0/g</text>
    <text x="370" y="170" font-family="Arial,sans-serif" font-size="8" fill="#333">t(пол) = 2*v0/g</text>
    <text x="370" y="185" font-family="Arial,sans-serif" font-size="7" fill="#555">Время вверх = вниз</text>

    <!-- Common problem types -->
    <rect x="25" y="210" width="450" height="55" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="250" y="226" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Типы задач</text>
    <rect x="35" y="233" width="100" height="22" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="85" y="248" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Свободное падение</text>
    <rect x="145" y="233" width="100" height="22" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="195" y="248" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Бросок вверх</text>
    <rect x="255" y="233" width="100" height="22" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="305" y="248" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Движение с трением</text>
    <rect x="365" y="233" width="100" height="22" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="415" y="248" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Наклонная плоскость</text>
    '''
    svg += footer("Кинематика", 9)
    return svg


# ============================================================
# LESSON 10: Равномерное движение по окружности
# ============================================================
def lesson10():
    svg = header("Равномерное движение по окружности", "Физика 10 класс — Урок 10")
    svg += f'''
    <!-- Circular motion diagram -->
    <circle cx="200" cy="170" r="70" fill="none" stroke="#1565C0" stroke-width="2.5"/>
    <!-- Center -->
    <circle cx="200" cy="170" r="3" fill="#333"/>
    <text x="205" y="180" font-family="Arial,sans-serif" font-size="8" fill="#333">O</text>

    <!-- Radius -->
    <line x1="200" y1="170" x2="270" y2="170" stroke="#333" stroke-width="1.5"/>
    <text x="238" y="167" font-family="Arial,sans-serif" font-size="9" fill="#333" font-style="italic">R</text>

    <!-- Body on circle -->
    <circle cx="270" cy="170" r="7" fill="#E53935"/>

    <!-- Velocity vector (tangential) -->
    <line x1="270" y1="170" x2="270" y2="108" stroke="#2E7D32" stroke-width="2.5"/>
    <polygon points="270,108 266,116 274,116" fill="#2E7D32"/>
    <text x="280" y="135" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" font-weight="bold" font-style="italic">v</text>

    <!-- Centripetal acceleration (toward center) -->
    <line x1="263" y1="168" x2="210" y2="170" stroke="#F57C00" stroke-width="2.5"/>
    <polygon points="210,170 218,166 218,174" fill="#F57C00"/>
    <text x="230" y="162" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" font-style="italic">a(ц)</text>

    <!-- Angle arc -->
    <path d="M 220 170 A 20 20 0 0 0 215 155" fill="none" stroke="#7B1FA2" stroke-width="1.5"/>
    <text x="222" y="158" font-family="Arial,sans-serif" font-size="8" fill="#7B1FA2" font-style="italic">dphi</text>

    <!-- Direction of motion arrow on circle -->
    <path d="M 245 102 A 70 70 0 0 1 280 115" fill="none" stroke="#E53935" stroke-width="2"/>
    <polygon points="280,115 273,109 275,120" fill="#E53935"/>

    <!-- Formulas box -->
    <rect x="320" y="62" width="155" height="140" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="397" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Формулы</text>
    <line x1="330" y1="83" x2="465" y2="83" stroke="#1565C0" stroke-width="0.5" opacity="0.3"/>

    <text x="340" y="98" font-family="Arial,sans-serif" font-size="8" fill="#333">v = 2*pi*R / T</text>
    <text x="340" y="113" font-family="Arial,sans-serif" font-size="8" fill="#333">omega = 2*pi / T</text>
    <text x="340" y="128" font-family="Arial,sans-serif" font-size="8" fill="#333">v = omega * R</text>
    <text x="340" y="143" font-family="Arial,sans-serif" font-size="8" fill="#E53935" font-weight="bold">a(ц) = v*v / R</text>
    <text x="340" y="158" font-family="Arial,sans-serif" font-size="8" fill="#333">a(ц) = omega*v</text>
    <text x="340" y="173" font-family="Arial,sans-serif" font-size="8" fill="#333">T = 2*pi*R / v</text>
    <text x="340" y="188" font-family="Arial,sans-serif" font-size="8" fill="#333">nu = 1 / T</text>
    <text x="340" y="198" font-family="Arial,sans-serif" font-size="7" fill="#555">nu — частота (Гц)</text>

    <!-- Period and frequency -->
    <rect x="30" y="260" width="215" height="28" rx="4" fill="white" stroke="#2E7D32" stroke-width="1"/>
    <text x="137" y="278" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">T — период (с) | nu — частота (Гц) | omega — угловая скорость</text>

    <!-- Key insight -->
    <rect x="255" y="260" width="220" height="28" rx="4" fill="white" stroke="#E53935" stroke-width="1"/>
    <text x="365" y="278" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle">v = const, но a(ц) != 0 | Направление v меняется!</text>
    '''
    svg += footer("Кинематика", 10)
    return svg


# ============================================================
# Generate all 10 SVGs
# ============================================================
generators = [lesson1, lesson2, lesson3, lesson4, lesson5, lesson6, lesson7, lesson8, lesson9, lesson10]

for i, gen in enumerate(generators, 1):
    svg_content = gen()
    filepath = os.path.join(OUTPUT_DIR, f"lesson{i}.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Generated lesson{i}.svg ({len(svg_content)} bytes)")

print(f"\nDone! Generated 10 SVGs in {OUTPUT_DIR}")
