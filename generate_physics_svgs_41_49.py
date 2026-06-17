#!/usr/bin/env python3
"""Generate SVG illustrations for Physics Grade 10, Lessons 41-49
41-43: Термодинамика, 44-49: Электростатика
"""
import os, math

OUT = "/home/z/my-project/school-curriculum-app-site/public/images/lessons/grade10/physics"
os.makedirs(OUT, exist_ok=True)

def hdr(title, subtitle):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#E3F2FD"/><stop offset="100%" stop-color="#FFF"/></linearGradient>
  <linearGradient id="panel" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#1565C0"/><stop offset="100%" stop-color="#1976D2"/></linearGradient></defs>
  <rect width="500" height="350" fill="url(#bg)" rx="10"/>
  <rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#1565C0" stroke-width="2.5"/>
  <text x="250" y="28" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1565C0" text-anchor="middle">{title}</text>
  <text x="250" y="44" font-family="Arial,sans-serif" font-size="10" fill="#888" text-anchor="middle">{subtitle}</text>
  <line x1="30" y1="52" x2="470" y2="52" stroke="#1565C0" stroke-width="1.5" opacity="0.25"/>
  <clipPath id="ill"><rect x="15" y="56" width="470" height="238" rx="6"/></clipPath>
  <g clip-path="url(#ill)"><rect x="15" y="56" width="470" height="238" fill="#E3F2FD" opacity="0.4"/>
'''

def ftr(section, num):
    return f'''</g><rect x="12" y="298" width="476" height="42" rx="5" fill="url(#panel)"/>
  <text x="250" y="316" font-family="Arial,sans-serif" font-size="14" text-anchor="middle" fill="white" font-weight="bold">{section}</text>
  <text x="250" y="332" font-family="Arial,sans-serif" font-size="10" text-anchor="middle" fill="white" opacity="0.8">Урок {num}</text></svg>'''

def arr(x1,y1,x2,y2,c="#1565C0",w=2,h=8):
    dx,dy=x2-x1,y2-y1;l=math.sqrt(dx*dx+dy*dy)
    if l<1:return""
    ux,uy=dx/l,dy/l;px,py=-uy,ux
    lx,ly=x2-ux*h+px*h*.4,y2-uy*h+py*h*.4
    rx,ry=x2-ux*h-px*h*.4,y2-uy*h-py*h*.4
    return f'<line x1="{x1}" y1="{y1}" x2="{x2-h*.5*ux}" y2="{y2-h*.5*uy}" stroke="{c}" stroke-width="{w}"/>\n<polygon points="{x2},{y2} {lx},{ly} {rx},{ry}" fill="{c}"/>'

# ===== LESSON 41: Первый закон термодинамики =====
def lesson41():
    s = hdr("Первый закон термодинамики","Физика 10 класс — Урок 41")
    s += f'''
    <!-- First law diagram -->
    <rect x="25" y="62" width="250" height="130" rx="5" fill="white" stroke="#E53935" stroke-width="1.5"/>
    <text x="150" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">I закон термодинамики</text>

    <!-- Central formula -->
    <rect x="45" y="88" width="210" height="35" rx="4" fill="#FFEBEE" stroke="#E53935" stroke-width="2"/>
    <text x="150" y="111" font-family="Arial,sans-serif" font-size="14" fill="#E53935" text-anchor="middle" font-weight="bold">Q = dU + A</text>

    <!-- Q arrow (heat in) -->
    {arr(50,135,110,135,"#F57C00",2.5,9)}
    <text x="70" y="128" font-family="Arial,sans-serif" font-size="10" fill="#F57C00" font-weight="bold">Q</text>

    <!-- dU (internal energy change) -->
    <rect x="120" y="125" width="60" height="30" rx="4" fill="#1565C0" opacity="0.15" stroke="#1565C0" stroke-width="1"/>
    <text x="150" y="145" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" font-weight="bold" text-anchor="middle">dU</text>

    <!-- A (work out) -->
    {arr(190,135,255,135,"#2E7D32",2.5,9)}
    <text x="230" y="128" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" font-weight="bold">A</text>

    <text x="150" y="175" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Q — теплота, переданная газу</text>
    <text x="150" y="188" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">dU — изменение внутренней энергии</text>
    <text x="150" y="200" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">A — работа газа</text>

    <!-- Isoprocess application -->
    <rect x="285" y="62" width="190" height="130" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="380" y="78" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Для изопроцессов</text>
    <line x1="295" y1="83" x2="465" y2="83" stroke="#2E7D32" stroke-width="0.5" opacity="0.3"/>

    <text x="305" y="98" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" font-weight="bold">Изохорный (V=const):</text>
    <text x="315" y="110" font-family="Arial,sans-serif" font-size="7" fill="#333">Q = dU (A=0)</text>

    <text x="305" y="125" font-family="Arial,sans-serif" font-size="7" fill="#F57C00" font-weight="bold">Изобарный (p=const):</text>
    <text x="315" y="137" font-family="Arial,sans-serif" font-size="7" fill="#333">Q = dU + p*dV</text>

    <text x="305" y="152" font-family="Arial,sans-serif" font-size="7" fill="#E53935" font-weight="bold">Изотермический (T=const):</text>
    <text x="315" y="164" font-family="Arial,sans-serif" font-size="7" fill="#333">Q = A (dU=0)</text>

    <text x="305" y="180" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" font-weight="bold">Адиабатный (Q=0):</text>
    <text x="315" y="192" font-family="Arial,sans-serif" font-size="7" fill="#333">dU = -A</text>

    <!-- Adiabatic note -->
    <rect x="25" y="205" width="225" height="65" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="137" y="221" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Адиабатный процесс</text>
    <line x1="35" y1="226" x2="240" y2="226" stroke="#7B1FA2" stroke-width="0.5" opacity="0.3"/>
    <text x="137" y="241" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Q = 0 (без теплообмена)</text>
    <text x="137" y="255" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Быстрое расширение: газ охлаждается</text>
    <text x="137" y="267" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Пример: накачивание шины, облака</text>

    <rect x="260" y="205" width="215" height="65" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="367" y="221" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Закон сохранения энергии</text>
    <line x1="270" y1="226" x2="465" y2="226" stroke="#E53935" stroke-width="0.5" opacity="0.3"/>
    <text x="367" y="242" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Энергия не возникает из ничего</text>
    <text x="367" y="256" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">и не исчезает бесследно</text>
    <text x="367" y="268" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">I закон термодинамики = ЗСЭ</text>
    '''
    s += ftr("Термодинамика", 41)
    return s

# ===== LESSON 42: Второй закон термодинамики =====
def lesson42():
    s = hdr("Второй закон термодинамики","Физика 10 класс — Урок 42")
    s += f'''
    <!-- Heat flow diagram -->
    <rect x="25" y="62" width="300" height="140" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="175" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Направление тепловых процессов</text>

    <!-- Hot reservoir -->
    <rect x="60" y="88" width="90" height="30" rx="4" fill="#E53935" opacity="0.3" stroke="#E53935" stroke-width="1.5"/>
    <text x="105" y="108" font-family="Arial,sans-serif" font-size="9" fill="#E53935" text-anchor="middle" font-weight="bold">T1 (горячий)</text>

    <!-- Cold reservoir -->
    <rect x="60" y="155" width="90" height="30" rx="4" fill="#1565C0" opacity="0.3" stroke="#1565C0" stroke-width="1.5"/>
    <text x="105" y="175" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" text-anchor="middle" font-weight="bold">T2 (холодный)</text>

    <!-- Natural heat flow (down) -->
    {arr(150,120,150,152,"#F57C00",2.5,9)}
    <text x="175" y="140" font-family="Arial,sans-serif" font-size="8" fill="#F57C00">Q1 (само)</text>

    <!-- Impossible: cold to hot without work -->
    <line x1="120" y1="155" x2="120" y2="120" stroke="#E53935" stroke-width="2" stroke-dasharray="4,3"/>
    <line x1="116" y1="125" x2="120" y2="118" stroke="#E53935" stroke-width="2"/>
    <line x1="124" y1="125" x2="120" y2="118" stroke="#E53935" stroke-width="2"/>
    <text x="90" y="138" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="end">невозможно!</text>

    <!-- Heat engine -->
    <rect x="210" y="88" width="100" height="97" rx="5" fill="#FFF3E0" stroke="#F57C00" stroke-width="1.5"/>
    <text x="260" y="108" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" font-weight="bold" text-anchor="middle">Тепловой</text>
    <text x="260" y="120" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" font-weight="bold" text-anchor="middle">двигатель</text>

    <!-- Q1 in -->
    {arr(150,100,207,100,"#E53935",2,7)}
    <text x="178" y="95" font-family="Arial,sans-serif" font-size="8" fill="#E53935">Q1</text>

    <!-- Work out -->
    {arr(310,115,350,115,"#2E7D32",2,7)}
    <text x="340" y="108" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32">A</text>

    <!-- Q2 out -->
    {arr(260,185,260,170,"#1565C0",2,7)}
    <text x="275" y="165" font-family="Arial,sans-serif" font-size="8" fill="#1565C0">Q2</text>

    <!-- Efficiency -->
    <rect x="335" y="62" width="140" height="80" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="405" y="78" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">КПД</text>
    <line x1="345" y1="83" x2="465" y2="83" stroke="#2E7D32" stroke-width="0.5" opacity="0.3"/>
    <text x="405" y="100" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">eta = A/Q1</text>
    <text x="405" y="115" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">= (Q1-Q2)/Q1</text>
    <text x="405" y="130" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">eta &lt; 1 всегда!</text>

    <!-- Carnot -->
    <rect x="335" y="150" width="140" height="52" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="405" y="166" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Цикл Карно (max)</text>
    <text x="405" y="182" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">eta = 1 - T2/T1</text>
    <text x="405" y="196" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">T в Кельвинах</text>

    <!-- Formulations -->
    <rect x="25" y="215" width="225" height="55" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="137" y="231" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Формулировки II закона</text>
    <circle cx="45" cy="243" r="3" fill="#E53935"/>
    <text x="55" y="247" font-family="Arial,sans-serif" font-size="7" fill="#333">Клаузиус: тепло не идёт само от холодного к горячему</text>
    <circle cx="45" cy="258" r="3" fill="#1565C0"/>
    <text x="55" y="262" font-family="Arial,sans-serif" font-size="7" fill="#333">Кельвин: невозможен вечный двигатель II рода</text>

    <rect x="260" y="215" width="215" height="55" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="367" y="231" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Необратимость</text>
    <text x="367" y="247" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Все реальные процессы необратимы</text>
    <text x="367" y="261" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Энтропия изолированной системы растёт</text>
    '''
    s += ftr("Термодинамика", 42)
    return s

# ===== LESSON 43: Тепловые двигатели =====
def lesson43():
    s = hdr("Тепловые двигатели и экология","Физика 10 класс — Урок 43")
    s += f'''
    <!-- Heat engine cycle -->
    <rect x="25" y="62" width="250" height="150" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="150" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Тепловой двигатель</text>

    <!-- Hot body -->
    <rect x="70" y="88" width="80" height="22" rx="4" fill="#E53935" opacity="0.3" stroke="#E53935" stroke-width="1.5"/>
    <text x="110" y="104" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle">Нагреватель T1</text>

    <!-- Working body -->
    <rect x="80" y="130" width="60" height="30" rx="4" fill="#FFF3E0" stroke="#F57C00" stroke-width="1.5"/>
    <text x="110" y="149" font-family="Arial,sans-serif" font-size="7" fill="#F57C00" text-anchor="middle">Рабочее тело</text>

    <!-- Cold body -->
    <rect x="70" y="180" width="80" height="22" rx="4" fill="#1565C0" opacity="0.3" stroke="#1565C0" stroke-width="1.5"/>
    <text x="110" y="196" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" text-anchor="middle">Холодильник T2</text>

    <!-- Q1 -->
    {arr(110,112,110,127,"#E53935",2,7)}
    <text x="125" y="122" font-family="Arial,sans-serif" font-size="8" fill="#E53935">Q1</text>

    <!-- A -->
    {arr(140,145,185,145,"#2E7D32",2.5,8)}
    <text x="170" y="138" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold">A</text>

    <!-- Q2 -->
    {arr(110,162,110,177,"#1565C0",2,7)}
    <text x="125" y="172" font-family="Arial,sans-serif" font-size="8" fill="#1565C0">Q2</text>

    <!-- Engine types -->
    <rect x="285" y="62" width="190" height="150" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="380" y="78" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Типы двигателей</text>
    <line x1="295" y1="83" x2="465" y2="83" stroke="#2E7D32" stroke-width="0.5" opacity="0.3"/>

    <rect x="300" y="90" width="165" height="25" rx="3" fill="#FFEBEE" stroke="#E53935" stroke-width="0.8"/>
    <text x="382" y="107" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">ДВС (авто) eta ~ 25-40%</text>

    <rect x="300" y="120" width="165" height="25" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="382" y="137" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Дизельный eta ~ 35-45%</text>

    <rect x="300" y="150" width="165" height="25" rx="3" fill="#E8F5E9" stroke="#2E7D32" stroke-width="0.8"/>
    <text x="382" y="167" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Паровая турбина eta ~ 40%</text>

    <rect x="300" y="180" width="165" height="25" rx="3" fill="#FFF3E0" stroke="#F57C00" stroke-width="0.8"/>
    <text x="382" y="197" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Реактивный eta ~ 30%</text>

    <!-- Ecology -->
    <rect x="25" y="225" width="225" height="45" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="137" y="241" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Экологические проблемы</text>
    <text x="137" y="258" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">CO2, NOx, парниковый эффект, смог</text>

    <rect x="260" y="225" width="215" height="45" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="367" y="241" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Пути решения</text>
    <text x="367" y="258" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Катализаторы, электромобили, возобновляемая энергия</text>
    '''
    s += ftr("Термодинамика", 43)
    return s

# ===== LESSON 44: Электрический заряд. Закон Кулона =====
def lesson44():
    s = hdr("Электрический заряд. Закон Кулона","Физика 10 класс — Урок 44")
    s += f'''
    <!-- Two charges -->
    <rect x="25" y="62" width="250" height="140" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="150" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Закон Кулона</text>

    <!-- Positive charge q1 -->
    <circle cx="80" cy="135" r="20" fill="#E53935" opacity="0.3" stroke="#E53935" stroke-width="2"/>
    <text x="80" y="131" font-family="Arial,sans-serif" font-size="14" fill="#E53935" text-anchor="middle">+</text>
    <text x="80" y="148" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle">q1</text>

    <!-- Negative charge q2 -->
    <circle cx="220" cy="135" r="16" fill="#1565C0" opacity="0.3" stroke="#1565C0" stroke-width="2"/>
    <text x="220" y="132" font-family="Arial,sans-serif" font-size="14" fill="#1565C0" text-anchor="middle">-</text>
    <text x="220" y="148" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" text-anchor="middle">q2</text>

    <!-- Attraction forces -->
    {arr(100,130,140,130,"#F57C00",2,7)}
    {arr(204,130,165,130,"#F57C00",2,7)}
    <text x="150" y="124" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" text-anchor="middle">F</text>

    <!-- Distance r -->
    <line x1="80" y1="170" x2="220" y2="170" stroke="#333" stroke-width="1"/>
    <line x1="80" y1="165" x2="80" y2="175" stroke="#333" stroke-width="1"/>
    <line x1="220" y1="165" x2="220" y2="175" stroke="#333" stroke-width="1"/>
    <text x="150" y="182" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-style="italic">r</text>

    <!-- Formula -->
    <rect x="40" y="188" width="220" height="25" rx="3" fill="#E3F2FD" stroke="#E53935" stroke-width="1.5"/>
    <text x="150" y="206" font-family="Arial,sans-serif" font-size="11" fill="#E53935" text-anchor="middle" font-weight="bold">F = k*q1*q2/r*r</text>

    <!-- Charge properties -->
    <rect x="285" y="62" width="190" height="95" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="380" y="78" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Свойства заряда</text>
    <line x1="295" y1="83" x2="465" y2="83" stroke="#2E7D32" stroke-width="0.5" opacity="0.3"/>
    <circle cx="305" cy="94" r="3" fill="#E53935"/>
    <text x="315" y="98" font-family="Arial,sans-serif" font-size="7" fill="#333">Два знака: + и -</text>
    <circle cx="305" cy="108" r="3" fill="#2E7D32"/>
    <text x="315" y="112" font-family="Arial,sans-serif" font-size="7" fill="#333">Квантован: e = 1.6*10^(-19) Кл</text>
    <circle cx="305" cy="122" r="3" fill="#F57C00"/>
    <text x="315" y="126" font-family="Arial,sans-serif" font-size="7" fill="#333">Закон сохранения заряда</text>
    <circle cx="305" cy="136" r="3" fill="#7B1FA2"/>
    <text x="315" y="140" font-family="Arial,sans-serif" font-size="7" fill="#333">[q] = Кл (Кулон)</text>
    <circle cx="305" cy="150" r="3" fill="#1565C0"/>
    <text x="315" y="154" font-family="Arial,sans-serif" font-size="7" fill="#333">Одноимённые отталкиваются</text>

    <!-- k constant -->
    <rect x="285" y="165" width="190" height="37" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="380" y="180" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" font-weight="bold" text-anchor="middle">k = 9*10^9 Н*м/Кл/Кл</text>
    <text x="380" y="196" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">k = 1/(4*pi*eps0)</text>

    <!-- Electrization -->
    <rect x="25" y="225" width="225" height="45" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="137" y="241" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Электризация</text>
    <text x="137" y="258" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Трение, контакт, влияние | Тело получает + или - заряд</text>

    <rect x="260" y="225" width="215" height="45" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="367" y="241" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Сравнение: Кулон vs Ньютон</text>
    <text x="367" y="258" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">F=kq1q2/r*r vs F=Gm1m2/r*r | Кулон в 10^36 раз сильнее!</text>
    '''
    s += ftr("Электростатика", 44)
    return s

# ===== LESSON 45: Электрическое поле =====
def lesson45():
    s = hdr("Электрическое поле","Физика 10 класс — Урок 45")
    s += f'''
    <!-- Electric field of point charge -->
    <rect x="25" y="62" width="225" height="150" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Поле точечного заряда</text>

    <!-- Central positive charge -->
    <circle cx="137" cy="140" r="12" fill="#E53935" opacity="0.8"/>
    <text x="137" y="145" font-family="Arial,sans-serif" font-size="14" fill="white" text-anchor="middle">+</text>

    <!-- Field lines radiating outward -->
    {arr(149,135,185,120,"#E53935",1.5,6)}
    {arr(143,152,165,185,"#E53935",1.5,6)}
    {arr(137,128,137,95,"#E53935",1.5,6)}
    {arr(125,135,90,120,"#E53935",1.5,6)}
    {arr(131,152,110,185,"#E53935",1.5,6)}
    {arr(149,145,195,155,"#E53935",1.5,6)}
    {arr(125,145,80,160,"#E53935",1.5,6)}

    <!-- Test charge at a point -->
    <circle cx="185" cy="120" r="5" fill="#1565C0" opacity="0.8"/>
    <text x="185" y="124" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">q0</text>
    <!-- Force on test charge -->
    {arr(190,118,220,105,"#2E7D32",1.5,6)}
    <text x="220" y="100" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">F</text>

    <text x="137" y="205" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Линии выходят из +, входят в -</text>

    <!-- Field strength -->
    <rect x="260" y="62" width="215" height="80" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Напряжённость E</text>
    <line x1="270" y1="83" x2="465" y2="83" stroke="#2E7D32" stroke-width="0.5" opacity="0.3"/>
    <text x="367" y="100" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">E = F/q0</text>
    <text x="367" y="115" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">E = k*q/r*r</text>
    <text x="367" y="130" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">[E] = В/м = Н/Кл | Вектор!</text>

    <!-- Principle of superposition -->
    <rect x="260" y="150" width="215" height="62" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="367" y="166" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Принцип суперпозиции</text>
    <text x="367" y="182" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">E = E1 + E2 + E3 + ...</text>
    <text x="367" y="198" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Векторная сумма полей</text>

    <!-- Dipole field -->
    <rect x="25" y="225" width="225" height="45" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="137" y="241" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Поле диполя</text>
    <!-- + and - charges -->
    <circle cx="95" cy="255" r="6" fill="#E53935"/>
    <text x="95" y="259" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">+</text>
    <circle cx="180" cy="255" r="6" fill="#1565C0"/>
    <text x="180" y="259" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">-</text>
    <!-- Field lines from + to - -->
    <path d="M 101 252 Q 137 235 174 252" fill="none" stroke="#E53935" stroke-width="1"/>
    <path d="M 101 258 Q 137 275 174 258" fill="none" stroke="#E53935" stroke-width="1"/>

    <rect x="260" y="225" width="215" height="45" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="367" y="241" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Однородное поле</text>
    <!-- Parallel lines -->
    <line x1="285" y1="250" x2="445" y2="250" stroke="#E53935" stroke-width="1.5"/>
    <polygon points="445,250 438,246 438,254" fill="#E53935"/>
    <line x1="285" y1="260" x2="445" y2="260" stroke="#E53935" stroke-width="1.5"/>
    <polygon points="445,260 438,256 438,264" fill="#E53935"/>
    <text x="367" y="270" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">E = const (между пластинами)</text>
    '''
    s += ftr("Электростатика", 45)
    return s

# ===== LESSON 46: Работа электрического поля. Разность потенциалов =====
def lesson46():
    s = hdr("Работа поля. Разность потенциалов","Физика 10 класс — Урок 46")
    s += f'''
    <!-- Charge moving in field -->
    <rect x="25" y="62" width="225" height="150" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Работа электрического поля</text>

    <!-- Field lines (horizontal) -->
    {arr(40,140,230,140,"#E53935",1,5)}
    {arr(40,120,230,120,"#E53935",0.8,4)}
    {arr(40,160,230,160,"#E53935",0.8,4)}
    <text x="240" y="143" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold">E</text>

    <!-- Charge +q at point A -->
    <circle cx="70" cy="120" r="7" fill="#E53935"/>
    <text x="70" y="124" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">+q</text>
    <text x="70" y="108" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" font-weight="bold">A</text>

    <!-- Force on charge -->
    {arr(77,120,110,120,"#2E7D32",2,7)}
    <text x="95" y="113" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32">F</text>

    <!-- Charge at point B -->
    <circle cx="190" cy="120" r="7" fill="#E53935" opacity="0.6"/>
    <text x="190" y="124" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">+q</text>
    <text x="190" y="108" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" font-weight="bold">B</text>

    <!-- Path A to B -->
    <path d="M 70 120 Q 130 95 190 120" fill="none" stroke="#F57C00" stroke-width="1.5" stroke-dasharray="4,2"/>

    <!-- Equipotential lines -->
    <line x1="70" y1="88" x2="70" y2="175" stroke="#42A5F5" stroke-width="1" stroke-dasharray="3,3"/>
    <text x="70" y="185" font-family="Arial,sans-serif" font-size="7" fill="#42A5F5">phi1</text>
    <line x1="190" y1="88" x2="190" y2="175" stroke="#42A5F5" stroke-width="1" stroke-dasharray="3,3"/>
    <text x="190" y="185" font-family="Arial,sans-serif" font-size="7" fill="#42A5F5">phi2</text>

    <text x="137" y="200" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">A = q*(phi1 - phi2) = q*U</text>
    <text x="137" y="212" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Работа НЕ зависит от траектории!</text>

    <!-- Potential -->
    <rect x="260" y="62" width="215" height="80" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Потенциал</text>
    <line x1="270" y1="83" x2="465" y2="83" stroke="#2E7D32" stroke-width="0.5" opacity="0.3"/>
    <text x="367" y="100" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">phi = k*q/r</text>
    <text x="367" y="115" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">[phi] = В (Вольт)</text>
    <text x="367" y="130" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Скаляр! phi(бескон) = 0</text>

    <!-- Voltage -->
    <rect x="260" y="150" width="215" height="62" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="367" y="166" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Напряжение (разность потенциалов)</text>
    <text x="367" y="183" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">U = phi1 - phi2 = A/q</text>
    <text x="367" y="198" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">[U] = В | E = -grad(phi)</text>

    <!-- Connection E and U -->
    <rect x="25" y="225" width="450" height="45" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="250" y="241" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Связь E и U</text>
    <text x="250" y="258" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">E = U/d (однородное поле) | Работа поля = убыль потенциальной энергии</text>
    '''
    s += ftr("Электростатика", 46)
    return s

# ===== LESSON 47: Проводники в электрическом поле =====
def lesson47():
    s = hdr("Проводники в электрическом поле","Физика 10 класс — Урок 47")
    s += f'''
    <!-- Conductor in external field -->
    <rect x="25" y="62" width="225" height="155" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Проводник в поле E</text>

    <!-- External field lines -->
    {arr(30,115,70,115,"#E53935",1,5)}
    {arr(30,140,70,140,"#E53935",1,5)}
    {arr(30,165,70,165,"#E53935",1,5)}

    <!-- Conductor body -->
    <ellipse cx="137" cy="140" rx="45" ry="35" fill="#FFCC80" opacity="0.4" stroke="#795548" stroke-width="2"/>

    <!-- Induced charges: - on left, + on right -->
    <text x="105" y="125" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" font-weight="bold">- - -</text>
    <text x="155" y="125" font-family="Arial,sans-serif" font-size="10" fill="#E53935" font-weight="bold">+ + +</text>

    <!-- Internal field = 0 -->
    <text x="137" y="145" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">E = 0</text>

    <!-- Induced field lines inside (opposing) -->
    {arr(160,135,115,135,"#2E7D32",1,4)}

    <!-- Field lines after conductor -->
    {arr(185,120,225,110,"#E53935",1,5)}
    {arr(185,140,225,140,"#E53935",1,5)}
    {arr(185,160,225,170,"#E53935",1,5)}

    <text x="137" y="180" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Электростатическая индукция</text>
    <text x="137" y="192" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Внутри проводника E = 0</text>

    <!-- Key properties -->
    <rect x="260" y="62" width="215" height="100" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Свойства проводника</text>
    <line x1="270" y1="83" x2="465" y2="83" stroke="#2E7D32" stroke-width="0.5" opacity="0.3"/>
    <circle cx="280" cy="94" r="3" fill="#E53935"/>
    <text x="290" y="98" font-family="Arial,sans-serif" font-size="7" fill="#333">E = 0 внутри</text>
    <circle cx="280" cy="108" r="3" fill="#2E7D32"/>
    <text x="290" y="112" font-family="Arial,sans-serif" font-size="7" fill="#333">phi = const (эквипотенциален)</text>
    <circle cx="280" cy="122" r="3" fill="#F57C00"/>
    <text x="290" y="126" font-family="Arial,sans-serif" font-size="7" fill="#333">Заряды на поверхности</text>
    <circle cx="280" cy="136" r="3" fill="#7B1FA2"/>
    <text x="290" y="140" font-family="Arial,sans-serif" font-size="7" fill="#333">E перпендикулярен поверхности</text>
    <circle cx="280" cy="150" r="3" fill="#1565C0"/>
    <text x="290" y="154" font-family="Arial,sans-serif" font-size="7" fill="#333">Заряд distributes по поверхности</text>

    <!-- Electrostatic protection -->
    <rect x="260" y="170" width="215" height="47" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="367" y="186" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Электростатическая защита</text>
    <text x="367" y="200" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Клетка Фарадея: внутри E=0</text>
    <text x="367" y="212" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Машина, самолёт, микроволновка</text>

    <!-- Grounding -->
    <rect x="25" y="230" width="225" height="40" rx="4" fill="white" stroke="#7B1FA2" stroke-width="1"/>
    <text x="137" y="248" font-family="Arial,sans-serif" font-size="8" fill="#7B1FA2" text-anchor="middle">Заземление: phi = 0 | Избыточный заряд уходит в Землю</text>

    <rect x="260" y="225" width="215" height="45" rx="4" fill="white" stroke="#E53935" stroke-width="1"/>
    <text x="367" y="241" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle">E(max) на остриях проводника</text>
    <text x="367" y="255" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Молниеотвод использует этот принцип</text>
    '''
    s += ftr("Электростатика", 47)
    return s

# ===== LESSON 48: Диэлектрики в электрическом поле =====
def lesson48():
    s = hdr("Диэлектрики в электрическом поле","Физика 10 класс — Урок 48")
    s += f'''
    <!-- Polarization -->
    <rect x="25" y="62" width="225" height="150" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Поляризация диэлектрика</text>

    <!-- External field -->
    {arr(30,140,70,140,"#E53935",1.5,6)}
    <text x="50" y="133" font-family="Arial,sans-serif" font-size="8" fill="#E53935">E0</text>

    <!-- Dielectric body -->
    <rect x="75" y="100" width="125" height="80" rx="5" fill="#E8F5E9" opacity="0.5" stroke="#2E7D32" stroke-width="1.5"/>

    <!-- Polarized molecules: -+ aligned -->
    <text x="85" y="130" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">-</text>
    <text x="95" y="130" font-family="Arial,sans-serif" font-size="7" fill="#E53935">+</text>
    <text x="110" y="130" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">-</text>
    <text x="120" y="130" font-family="Arial,sans-serif" font-size="7" fill="#E53935">+</text>
    <text x="135" y="130" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">-</text>
    <text x="145" y="130" font-family="Arial,sans-serif" font-size="7" fill="#E53935">+</text>
    <text x="160" y="130" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">-</text>
    <text x="170" y="130" font-family="Arial,sans-serif" font-size="7" fill="#E53935">+</text>

    <text x="85" y="150" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">-</text>
    <text x="95" y="150" font-family="Arial,sans-serif" font-size="7" fill="#E53935">+</text>
    <text x="110" y="150" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">-</text>
    <text x="120" y="150" font-family="Arial,sans-serif" font-size="7" fill="#E53935">+</text>
    <text x="135" y="150" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">-</text>
    <text x="145" y="150" font-family="Arial,sans-serif" font-size="7" fill="#E53935">+</text>
    <text x="160" y="150" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">-</text>
    <text x="170" y="150" font-family="Arial,sans-serif" font-size="7" fill="#E53935">+</text>

    <!-- Bound charges on surfaces -->
    <text x="80" y="115" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" font-weight="bold">- - -</text>
    <text x="165" y="175" font-family="Arial,sans-serif" font-size="8" fill="#E53935" font-weight="bold">+ + +</text>

    <!-- Internal field (opposing) -->
    {arr(150,140,110,140,"#2E7D32",1,4)}
    <text x="130" y="137" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">E'</text>

    <!-- Resulting field after dielectric -->
    {arr(205,140,240,140,"#E53935",1.5,6)}
    <text x="225" y="133" font-family="Arial,sans-serif" font-size="8" fill="#E53935">E</text>

    <text x="137" y="200" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">E = E0 - E' (ослаблено)</text>

    <!-- Dielectric constant -->
    <rect x="260" y="62" width="215" height="80" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Диэлектрическая проницаемость</text>
    <line x1="270" y1="83" x2="465" y2="83" stroke="#E53935" stroke-width="0.5" opacity="0.3"/>
    <text x="367" y="102" font-family="Arial,sans-serif" font-size="12" fill="#333" text-anchor="middle" font-weight="bold">eps = E0/E</text>
    <text x="367" y="118" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Во сколько раз поле ослабляется</text>
    <text x="367" y="132" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">F = k*q1*q2/(eps*r*r)</text>

    <!-- Types of dielectrics -->
    <rect x="260" y="150" width="215" height="62" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="367" y="166" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Виды диэлектриков</text>
    <line x1="270" y1="171" x2="465" y2="171" stroke="#2E7D32" stroke-width="0.5" opacity="0.3"/>
    <circle cx="280" cy="182" r="3" fill="#E53935"/>
    <text x="290" y="186" font-family="Arial,sans-serif" font-size="7" fill="#333">Полярные (H2O, NH3)</text>
    <circle cx="280" cy="196" r="3" fill="#2E7D32"/>
    <text x="290" y="200" font-family="Arial,sans-serif" font-size="7" fill="#333">Неполярные (O2, CO2, благородные газы)</text>

    <!-- eps values -->
    <rect x="25" y="225" width="225" height="45" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="137" y="241" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Значения eps</text>
    <text x="137" y="258" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Вакуум: 1 | Воздух: 1.0006 | Вода: 81 | Стекло: 5-10</text>

    <rect x="260" y="225" width="215" height="45" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="367" y="241" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Отличие от проводника</text>
    <text x="367" y="258" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">В диэлектрике E != 0, но E &lt; E0 | Свободных зарядов нет</text>
    '''
    s += ftr("Электростатика", 48)
    return s

# ===== LESSON 49: Конденсаторы. Электроёмкость =====
def lesson49():
    s = hdr("Конденсаторы. Электроёмкость","Физика 10 класс — Урок 49")
    s += f'''
    <!-- Parallel plate capacitor -->
    <rect x="25" y="62" width="225" height="150" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Плоский конденсатор</text>

    <!-- Left plate (positive) -->
    <rect x="85" y="92" width="8" height="90" rx="2" fill="#E53935" opacity="0.7"/>
    <text x="60" y="105" font-family="Arial,sans-serif" font-size="8" fill="#E53935">+ + +</text>
    <text x="60" y="120" font-family="Arial,sans-serif" font-size="8" fill="#E53935">+ + +</text>
    <text x="60" y="135" font-family="Arial,sans-serif" font-size="8" fill="#E53935">+ + +</text>
    <text x="60" y="150" font-family="Arial,sans-serif" font-size="8" fill="#E53935">+ + +</text>
    <text x="60" y="165" font-family="Arial,sans-serif" font-size="8" fill="#E53935">+ + +</text>

    <!-- Right plate (negative) -->
    <rect x="180" y="92" width="8" height="90" rx="2" fill="#1565C0" opacity="0.7"/>
    <text x="195" y="105" font-family="Arial,sans-serif" font-size="8" fill="#1565C0">- - -</text>
    <text x="195" y="120" font-family="Arial,sans-serif" font-size="8" fill="#1565C0">- - -</text>
    <text x="195" y="135" font-family="Arial,sans-serif" font-size="8" fill="#1565C0">- - -</text>
    <text x="195" y="150" font-family="Arial,sans-serif" font-size="8" fill="#1565C0">- - -</text>
    <text x="195" y="165" font-family="Arial,sans-serif" font-size="8" fill="#1565C0">- - -</text>

    <!-- Field lines between plates -->
    {arr(95,120,175,120,"#F57C00",1,4)}
    {arr(95,140,175,140,"#F57C00",1,4)}
    {arr(95,160,175,160,"#F57C00",1,4)}
    <text x="137" y="152" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" text-anchor="middle" font-weight="bold">E</text>

    <!-- Distance d -->
    <line x1="95" y1="190" x2="180" y2="190" stroke="#333" stroke-width="1"/>
    <line x1="95" y1="185" x2="95" y2="195" stroke="#333" stroke-width="1"/>
    <line x1="180" y1="185" x2="180" y2="195" stroke="#333" stroke-width="1"/>
    <text x="137" y="202" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-style="italic">d</text>

    <!-- Area S -->
    <text x="137" y="215" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">S — площадь пластин</text>

    <!-- Formulas -->
    <rect x="260" y="62" width="215" height="90" rx="5" fill="white" stroke="#E53935" stroke-width="1.5"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Формулы</text>
    <line x1="270" y1="83" x2="465" y2="83" stroke="#E53935" stroke-width="0.5" opacity="0.3"/>
    <text x="367" y="100" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">C = q/U</text>
    <text x="367" y="118" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">C = eps*eps0*S/d</text>
    <text x="367" y="135" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">[C] = Ф (Фарад) | 1 Ф = Кл/В</text>
    <text x="367" y="148" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">eps0 = 8.85*10^(-12) Ф/м</text>

    <!-- Energy -->
    <rect x="260" y="160" width="215" height="52" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="367" y="176" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Энергия конденсатора</text>
    <text x="367" y="194" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">W = q*U/2 = C*U*U/2 = q*q/(2C)</text>

    <!-- Connections -->
    <rect x="25" y="225" width="120" height="45" rx="4" fill="white" stroke="#1565C0" stroke-width="1"/>
    <text x="85" y="241" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" font-weight="bold" text-anchor="middle">Параллельно</text>
    <text x="85" y="258" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">C = C1+C2</text>

    <rect x="155" y="225" width="120" height="45" rx="4" fill="white" stroke="#E53935" stroke-width="1"/>
    <text x="215" y="241" font-family="Arial,sans-serif" font-size="8" fill="#E53935" font-weight="bold" text-anchor="middle">Последовательно</text>
    <text x="215" y="258" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">1/C = 1/C1+1/C2</text>

    <rect x="285" y="225" width="190" height="45" rx="4" fill="white" stroke="#F57C00" stroke-width="1"/>
    <text x="380" y="241" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" font-weight="bold" text-anchor="middle">Применение</text>
    <text x="380" y="258" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Фотовспышка, фильтры, память, сенсоры</text>
    '''
    s += ftr("Электростатика", 49)
    return s

# Generate
gens = {41:lesson41,42:lesson42,43:lesson43,44:lesson44,
        45:lesson45,46:lesson46,47:lesson47,48:lesson48,49:lesson49}

for n,g in gens.items():
    svg = g()
    with open(os.path.join(OUT,f"lesson{n}.svg"),'w',encoding='utf-8') as f:
        f.write(svg)
    print(f"lesson{n}.svg ({len(svg)} bytes)")

print("Done! All 49 lessons complete!")
