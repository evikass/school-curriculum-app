#!/usr/bin/env python3
"""Generate SVG illustrations for Physics Grade 10, Lessons 31-40
31: Статика, 32-39: Молекулярная физика, 40: Термодинамика
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

# ===== LESSON 31: Простые механизмы =====
def lesson31():
    s = hdr("Простые механизмы","Золотое правило механики — Урок 31")
    s += f'''
    <!-- Lever -->
    <rect x="25" y="62" width="145" height="115" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="97" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Рычаг</text>
    <rect x="40" y="115" width="110" height="5" rx="2" fill="#795548"/>
    <polygon points="97,120 90,138 104,138" fill="#555"/>
    {arr(55,100,55,115,"#E53935",2,7)}
    <text x="55" y="96" font-family="Arial,sans-serif" font-size="8" fill="#E53935">F1</text>
    {arr(135,125,135,148,"#2E7D32",2,7)}
    <text x="135" y="162" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32">F2</text>
    <text x="97" y="170" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">F1*l1 = F2*l2</text>

    <!-- Inclined plane -->
    <rect x="180" y="62" width="145" height="115" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="252" y="78" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Наклонная плоскость</text>
    <polygon points="200,160 310,160 310,110" fill="#795548" opacity="0.3" stroke="#795548" stroke-width="1.5"/>
    <rect x="255" y="115" width="22" height="16" rx="2" fill="#1565C0" transform="rotate(-35,266,123)"/>
    {arr(265,108,285,90,"#2E7D32",1.5,6)}
    <text x="290" y="88" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">F (мало)</text>
    {arr(266,128,266,158,"#E53935",1.5,6)}
    <text x="278" y="150" font-family="Arial,sans-serif" font-size="7" fill="#E53935">mg</text>
    <text x="252" y="172" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">F = mg*sin(a)</text>

    <!-- Block (pulley) -->
    <rect x="335" y="62" width="145" height="115" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="407" y="78" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Блок</text>
    <!-- Fixed pulley -->
    <circle cx="390" cy="105" r="15" fill="none" stroke="#555" stroke-width="2"/>
    <circle cx="390" cy="105" r="3" fill="#555"/>
    <line x1="390" y1="90" x2="390" y2="82" stroke="#555" stroke-width="2"/>
    <!-- Rope left -->
    <line x1="375" y1="105" x2="360" y2="155" stroke="#795548" stroke-width="1.5"/>
    <!-- Rope right -->
    <line x1="405" y1="105" x2="420" y2="155" stroke="#795548" stroke-width="1.5"/>
    <!-- Load -->
    <rect x="352" y="155" width="20" height="15" rx="2" fill="#E53935"/>
    <!-- Force -->
    {arr(420,155,440,140,"#2E7D32",1.5,6)}
    <text x="442" y="138" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">F=mg</text>
    <text x="390" y="178" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Неподвижный: F=mg</text>

    <!-- Movable pulley -->
    <circle cx="450" cy="115" r="12" fill="none" stroke="#555" stroke-width="2"/>
    <circle cx="450" cy="115" r="3" fill="#555"/>
    <line x1="438" y1="100" x2="438" y2="82" stroke="#795548" stroke-width="1.5"/>
    <line x1="462" y1="100" x2="462" y2="82" stroke="#795548" stroke-width="1.5"/>
    <!-- Load below -->
    <line x1="450" y1="127" x2="450" y2="145" stroke="#795548" stroke-width="1.5"/>
    <rect x="442" y="145" width="16" height="12" rx="2" fill="#E53935"/>
    <text x="450" y="166" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">F=mg/2</text>

    <!-- Golden rule -->
    <rect x="25" y="190" width="450" height="50" rx="5" fill="white" stroke="#F57C00" stroke-width="1.5"/>
    <text x="250" y="208" font-family="Arial,sans-serif" font-size="10" fill="#F57C00" font-weight="bold" text-anchor="middle">Золотое правило механики</text>
    <text x="250" y="225" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">Во сколько раз выигрываем в силе, во столько раз проигрываем в расстоянии</text>
    <text x="250" y="237" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">A1 = A2 | F1*S1 = F2*S2 | Никакой механизм не даёт выигрыша в работе!</text>

    <!-- Other mechanisms -->
    <rect x="25" y="250" width="145" height="35" rx="4" fill="white" stroke="#7B1FA2" stroke-width="1"/>
    <text x="97" y="268" font-family="Arial,sans-serif" font-size="8" fill="#7B1FA2" text-anchor="middle">Ворот (ворот)</text>
    <rect x="180" y="250" width="145" height="35" rx="4" fill="white" stroke="#1565C0" stroke-width="1"/>
    <text x="252" y="268" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" text-anchor="middle">Клин</text>
    <rect x="335" y="250" width="140" height="35" rx="4" fill="white" stroke="#2E7D32" stroke-width="1"/>
    <text x="405" y="268" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">Винт</text>
    '''
    s += ftr("Статика", 31)
    return s

# ===== LESSON 32: Основные положения МКТ =====
def lesson32():
    s = hdr("Основные положения МКТ","Физика 10 класс — Урок 32")
    s += f'''
    <!-- Three positions of MKT -->
    <rect x="25" y="62" width="145" height="120" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="97" y="78" font-family="Arial,sans-serif" font-size="8" fill="#E53935" font-weight="bold" text-anchor="middle">I: Вещество = частицы</text>
    <!-- Molecules scattered -->
    <circle cx="55" cy="100" r="4" fill="#E53935" opacity="0.7"/>
    <circle cx="80" cy="115" r="4" fill="#E53935" opacity="0.6"/>
    <circle cx="110" cy="95" r="4" fill="#E53935" opacity="0.8"/>
    <circle cx="130" cy="120" r="4" fill="#E53935" opacity="0.5"/>
    <circle cx="65" cy="140" r="4" fill="#E53935" opacity="0.7"/>
    <circle cx="95" cy="130" r="4" fill="#E53935" opacity="0.6"/>
    <circle cx="120" cy="145" r="4" fill="#E53935" opacity="0.8"/>
    <circle cx="45" cy="125" r="3" fill="#1565C0" opacity="0.5"/>
    <circle cx="140" cy="105" r="3" fill="#1565C0" opacity="0.5"/>
    <text x="97" y="168" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Атомы и молекулы</text>

    <rect x="180" y="62" width="145" height="120" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="252" y="78" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" font-weight="bold" text-anchor="middle">II: Частицы движутся</text>
    <!-- Molecules with motion trails -->
    <circle cx="220" cy="110" r="4" fill="#2E7D32" opacity="0.8"/>
    <path d="M 220 110 Q 225 100 235 95" fill="none" stroke="#2E7D32" stroke-width="1" stroke-dasharray="2,2"/>
    <circle cx="235" cy="95" r="3" fill="#2E7D32" opacity="0.4"/>
    <circle cx="270" cy="130" r="4" fill="#2E7D32" opacity="0.8"/>
    <path d="M 270 130 Q 280 125 290 128" fill="none" stroke="#2E7D32" stroke-width="1" stroke-dasharray="2,2"/>
    <circle cx="290" cy="128" r="3" fill="#2E7D32" opacity="0.4"/>
    <circle cx="240" cy="145" r="4" fill="#2E7D32" opacity="0.8"/>
    <path d="M 240 145 Q 250 150 255 140" fill="none" stroke="#2E7D32" stroke-width="1" stroke-dasharray="2,2"/>
    <!-- Random arrows -->
    {arr(210,100,225,88,"#2E7D32",1,4)}
    {arr(280,135,300,140,"#2E7D32",1,4)}
    {arr(250,150,245,165,"#2E7D32",1,4)}
    <text x="252" y="168" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Хаотично, непрерывно</text>

    <rect x="335" y="62" width="145" height="120" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="407" y="78" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" font-weight="bold" text-anchor="middle">III: Взаимодействуют</text>
    <!-- Molecules with attraction/repulsion -->
    <circle cx="380" cy="110" r="5" fill="#F57C00" opacity="0.8"/>
    <circle cx="400" cy="110" r="5" fill="#F57C00" opacity="0.8"/>
    <!-- Attraction line -->
    <line x1="386" y1="108" x2="394" y2="108" stroke="#2E7D32" stroke-width="1.5" stroke-dasharray="2,1"/>
    <text x="390" y="100" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">притяжение</text>

    <circle cx="380" cy="140" r="5" fill="#F57C00" opacity="0.8"/>
    <circle cx="393" cy="140" r="5" fill="#F57C00" opacity="0.8"/>
    <!-- Repulsion arrows -->
    {arr(386,138,378,138,"#E53935",1,3)}
    {arr(387,138,395,138,"#E53935",1,3)}
    <text x="390" y="158" font-family="Arial,sans-serif" font-size="6" fill="#E53935">отталкивание</text>

    <text x="407" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Притяжение и отталкивание</text>

    <!-- Evidence -->
    <rect x="25" y="195" width="225" height="70" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="137" y="211" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Доказательства МКТ</text>
    <line x1="35" y1="216" x2="240" y2="216" stroke="#7B1FA2" stroke-width="0.5" opacity="0.3"/>
    <circle cx="45" cy="227" r="3" fill="#1565C0"/>
    <text x="55" y="231" font-family="Arial,sans-serif" font-size="8" fill="#333">Броуновское движение</text>
    <circle cx="45" cy="242" r="3" fill="#2E7D32"/>
    <text x="55" y="246" font-family="Arial,sans-serif" font-size="8" fill="#333">Диффузия</text>
    <circle cx="45" cy="257" r="3" fill="#F57C00"/>
    <text x="55" y="261" font-family="Arial,sans-serif" font-size="8" fill="#333">Деформации (сжатие/растяжение)</text>

    <!-- Molecular sizes -->
    <rect x="260" y="195" width="215" height="70" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="367" y="211" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Масштабы</text>
    <line x1="270" y1="216" x2="465" y2="216" stroke="#E53935" stroke-width="0.5" opacity="0.3"/>
    <text x="367" y="232" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">d(молекулы) ~ 10^(-10) м</text>
    <text x="367" y="247" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">m(молекулы) ~ 10^(-26) кг</text>
    <text x="367" y="262" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">N(A) = 6*10^23 моль^(-1) — число Авогадро</text>
    '''
    s += ftr("Молекулярная физика", 32)
    return s

# ===== LESSON 33: Масса и размеры молекул =====
def lesson33():
    s = hdr("Масса и размеры молекул","Физика 10 класс — Урок 33")
    s += f'''
    <!-- Molecule size calculation -->
    <rect x="25" y="62" width="225" height="130" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Оценка размеров молекулы</text>

    <!-- Oil drop on water -->
    <rect x="40" y="100" width="190" height="60" rx="3" fill="#42A5F5" opacity="0.2" stroke="#42A5F5" stroke-width="1"/>
    <text x="135" y="95" font-family="Arial,sans-serif" font-size="7" fill="#42A5F5">Поверхность воды</text>
    <!-- Oil film -->
    <rect x="55" y="102" width="160" height="3" fill="#F57C00" opacity="0.6"/>
    <text x="135" y="115" font-family="Arial,sans-serif" font-size="7" fill="#F57C00" text-anchor="middle">Масляная плёнка (1 молекула)</text>

    <!-- Cross section of film -->
    <rect x="60" y="125" width="150" height="25" rx="2" fill="#F57C00" opacity="0.15"/>
    <line x1="60" y1="125" x2="210" y2="125" stroke="#F57C00" stroke-width="1"/>
    <line x1="60" y1="150" x2="210" y2="150" stroke="#F57C00" stroke-width="1"/>
    <!-- Molecules as circles -->
    <circle cx="72" cy="138" r="5" fill="#E53935" opacity="0.6" stroke="#E53935" stroke-width="0.5"/>
    <circle cx="84" cy="138" r="5" fill="#E53935" opacity="0.6" stroke="#E53935" stroke-width="0.5"/>
    <circle cx="96" cy="138" r="5" fill="#E53935" opacity="0.6" stroke="#E53935" stroke-width="0.5"/>
    <circle cx="108" cy="138" r="5" fill="#E53935" opacity="0.6" stroke="#E53935" stroke-width="0.5"/>
    <circle cx="120" cy="138" r="5" fill="#E53935" opacity="0.6" stroke="#E53935" stroke-width="0.5"/>
    <circle cx="132" cy="138" r="5" fill="#E53935" opacity="0.6" stroke="#E53935" stroke-width="0.5"/>
    <circle cx="144" cy="138" r="5" fill="#E53935" opacity="0.6" stroke="#E53935" stroke-width="0.5"/>
    <circle cx="156" cy="138" r="5" fill="#E53935" opacity="0.6" stroke="#E53935" stroke-width="0.5"/>

    <!-- d label -->
    <line x1="68" y1="155" x2="78" y2="155" stroke="#E53935" stroke-width="1"/>
    <line x1="68" y1="150" x2="68" y2="160" stroke="#E53935" stroke-width="0.8"/>
    <line x1="78" y1="150" x2="78" y2="160" stroke="#E53935" stroke-width="0.8"/>
    <text x="73" y="168" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle" font-style="italic">d</text>

    <!-- S label -->
    <line x1="60" y1="170" x2="210" y2="170" stroke="#1565C0" stroke-width="1"/>
    <text x="135" y="180" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle">S — площадь</text>

    <!-- Formulas -->
    <rect x="260" y="62" width="215" height="130" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Формулы</text>
    <line x1="270" y1="83" x2="465" y2="83" stroke="#E53935" stroke-width="0.5" opacity="0.3"/>
    <text x="367" y="100" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">d = V / S</text>
    <text x="367" y="115" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">m0 = M / N(A)</text>
    <text x="367" y="130" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">N = m*N(A) / M</text>
    <text x="367" y="148" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">d — диаметр молекулы</text>
    <text x="367" y="160" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">m0 — масса одной молекулы</text>
    <text x="367" y="172" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">M — молярная масса (кг/моль)</text>
    <text x="367" y="184" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">N(A) = 6.02*10^23 моль^(-1)</text>

    <!-- Amount of substance -->
    <rect x="25" y="205" width="225" height="65" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="137" y="221" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Количество вещества</text>
    <line x1="35" y1="226" x2="240" y2="226" stroke="#2E7D32" stroke-width="0.5" opacity="0.3"/>
    <text x="137" y="242" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">nu = m/M = N/N(A)</text>
    <text x="137" y="258" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">[nu] = моль</text>
    <text x="137" y="268" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">1 моль = N(A) частиц</text>

    <!-- Example values -->
    <rect x="260" y="205" width="215" height="65" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="367" y="221" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Примеры молярных масс</text>
    <line x1="270" y1="226" x2="465" y2="226" stroke="#F57C00" stroke-width="0.5" opacity="0.3"/>
    <text x="290" y="240" font-family="Arial,sans-serif" font-size="8" fill="#333">H2O: 18 г/моль</text>
    <text x="290" y="255" font-family="Arial,sans-serif" font-size="8" fill="#333">O2: 32 г/моль</text>
    <text x="290" y="268" font-family="Arial,sans-serif" font-size="8" fill="#333">N2: 28 г/моль</text>
    <text x="395" y="240" font-family="Arial,sans-serif" font-size="8" fill="#333">CO2: 44 г/моль</text>
    <text x="395" y="255" font-family="Arial,sans-serif" font-size="8" fill="#333">Fe: 56 г/моль</text>
    '''
    s += ftr("Молекулярная физика", 33)
    return s

# ===== LESSON 34: Идеальный газ. Основное уравнение МКТ =====
def lesson34():
    s = hdr("Идеальный газ. Основное уравнение МКТ","Физика 10 класс — Урок 34")
    s += f'''
    <!-- Gas molecules in container -->
    <rect x="25" y="62" width="225" height="140" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Модель идеального газа</text>

    <!-- Container -->
    <rect x="45" y="88" width="180" height="90" rx="3" fill="none" stroke="#555" stroke-width="2"/>

    <!-- Molecules bouncing -->
    <circle cx="80" cy="115" r="4" fill="#E53935" opacity="0.8"/>
    {arr(84,113,100,105,"#E53935",1,4)}
    <circle cx="140" cy="100" r="4" fill="#2E7D32" opacity="0.8"/>
    {arr(140,96,155,88,"#2E7D32",1,4)}
    <circle cx="180" cy="140" r="4" fill="#F57C00" opacity="0.8"/>
    {arr(176,138,160,130,"#F57C00",1,4)}
    <circle cx="100" cy="150" r="4" fill="#7B1FA2" opacity="0.8"/>
    {arr(104,148,120,145,"#7B1FA2",1,4)}
    <circle cx="160" cy="120" r="4" fill="#1565C0" opacity="0.8"/>
    {arr(156,118,140,115,"#1565C0",1,4)}
    <circle cx="70" cy="140" r="3" fill="#E53935" opacity="0.5"/>
    <circle cx="200" cy="105" r="3" fill="#2E7D32" opacity="0.5"/>
    <circle cx="120" cy="165" r="3" fill="#F57C00" opacity="0.5"/>

    <!-- Wall collision -->
    <circle cx="210" cy="130" r="4" fill="#E53935" opacity="0.8"/>
    {arr(206,130,195,130,"#E53935",1.5,5)}
    <!-- Force on wall -->
    {arr(222,130,238,130,"#E53935",1.5,5)}
    <text x="240" y="128" font-family="Arial,sans-serif" font-size="7" fill="#E53935">F</text>

    <text x="137" y="192" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Молекулы — материальные точки, не взаимодействуют</text>
    <text x="137" y="202" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Упругие столкновения со стенками</text>

    <!-- Main formula -->
    <rect x="260" y="62" width="215" height="70" rx="5" fill="white" stroke="#E53935" stroke-width="1.5"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Основное уравнение МКТ</text>
    <line x1="270" y1="83" x2="465" y2="83" stroke="#E53935" stroke-width="0.5" opacity="0.3"/>
    <text x="367" y="102" font-family="Arial,sans-serif" font-size="13" fill="#333" text-anchor="middle" font-weight="bold">p = (1/3)*n*m0*v*v</text>
    <text x="367" y="118" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">p = (2/3)*n*E(k) — через энергию</text>
    <text x="367" y="128" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">v*v — средний квадрат скорости</text>

    <!-- Variables -->
    <rect x="260" y="140" width="215" height="62" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="367" y="156" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Величины</text>
    <line x1="270" y1="161" x2="465" y2="161" stroke="#2E7D32" stroke-width="0.5" opacity="0.3"/>
    <text x="280" y="174" font-family="Arial,sans-serif" font-size="7" fill="#333">p — давление (Па)</text>
    <text x="280" y="186" font-family="Arial,sans-serif" font-size="7" fill="#333">n — концентрация (1/м3)</text>
    <text x="390" y="174" font-family="Arial,sans-serif" font-size="7" fill="#333">m0 — масса молекулы</text>
    <text x="390" y="186" font-family="Arial,sans-serif" font-size="7" fill="#333">v — скорость (м/с)</text>

    <!-- Connection to temperature -->
    <rect x="25" y="215" width="450" height="55" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="250" y="231" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Связь с температурой</text>
    <text x="250" y="248" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">E(k) = (3/2)*k*T | k = 1.38*10^(-23) Дж/К — постоянная Больцмана</text>
    <text x="250" y="263" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">p = n*k*T — связывающее уравнение (давление через температуру)</text>
    '''
    s += ftr("Молекулярная физика", 34)
    return s

# ===== LESSON 35: Температура и её измерение =====
def lesson35():
    s = hdr("Температура и её измерение","Физика 10 класс — Урок 35")
    s += f'''
    <!-- Thermometer -->
    <rect x="25" y="62" width="140" height="175" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="95" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Шкалы</text>

    <!-- Thermometer body -->
    <rect x="85" y="88" width="20" height="110" rx="10" fill="none" stroke="#555" stroke-width="1.5"/>
    <circle cx="95" cy="200" r="12" fill="#E53935" opacity="0.6"/>
    <!-- Mercury column -->
    <rect x="89" y="130" width="12" height="70" fill="#E53935" opacity="0.7"/>

    <!-- Scale marks -->
    <line x1="105" y1="130" x2="115" y2="130" stroke="#555" stroke-width="1"/>
    <text x="118" y="134" font-family="Arial,sans-serif" font-size="7" fill="#555">100 C</text>
    <line x1="105" y1="165" x2="115" y2="165" stroke="#555" stroke-width="1"/>
    <text x="118" y="169" font-family="Arial,sans-serif" font-size="7" fill="#555">0 C</text>
    <line x1="105" y1="195" x2="115" y2="195" stroke="#555" stroke-width="1"/>
    <text x="118" y="199" font-family="Arial,sans-serif" font-size="7" fill="#555">-273 C</text>

    <!-- Kelvin scale -->
    <line x1="65" y1="130" x2="75" y2="130" stroke="#1565C0" stroke-width="1"/>
    <text x="62" y="134" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="end">373 K</text>
    <line x1="65" y1="165" x2="75" y2="165" stroke="#1565C0" stroke-width="1"/>
    <text x="62" y="169" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="end">273 K</text>
    <line x1="65" y1="195" x2="75" y2="195" stroke="#1565C0" stroke-width="1"/>
    <text x="62" y="199" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="end">0 K</text>

    <!-- Temperature and kinetic energy -->
    <rect x="180" y="62" width="295" height="90" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="327" y="78" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Температура = мера энергии</text>
    <line x1="190" y1="83" x2="465" y2="83" stroke="#2E7D32" stroke-width="0.5" opacity="0.3"/>
    <text x="327" y="100" font-family="Arial,sans-serif" font-size="11" fill="#333" text-anchor="middle" font-weight="bold">E(k) = (3/2)*k*T</text>
    <text x="327" y="118" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">k = 1.38*10^(-23) Дж/К — постоянная Больцмана</text>
    <text x="327" y="132" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">T — абсолютная температура (Кельвин)</text>
    <text x="327" y="146" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle">T = 0 K => E(k) = 0 (абсолютный нуль!)</text>

    <!-- Conversion -->
    <rect x="180" y="160" width="295" height="45" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="327" y="176" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Перевод шкал</text>
    <text x="327" y="192" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">T(K) = t(C) + 273</text>

    <!-- Root mean square velocity -->
    <rect x="25" y="250" width="225" height="28" rx="4" fill="white" stroke="#7B1FA2" stroke-width="1"/>
    <text x="137" y="268" font-family="Arial,sans-serif" font-size="8" fill="#7B1FA2" text-anchor="middle">v(кв) = sqrt(3kT/m0) = sqrt(3RT/M)</text>

    <rect x="260" y="218" width="215" height="60" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="367" y="234" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Измерение температуры</text>
    <line x1="270" y1="239" x2="465" y2="239" stroke="#1565C0" stroke-width="0.5" opacity="0.3"/>
    <circle cx="280" cy="250" r="3" fill="#E53935"/>
    <text x="290" y="254" font-family="Arial,sans-serif" font-size="7" fill="#333">Жидкостные термометры</text>
    <circle cx="280" cy="263" r="3" fill="#2E7D32"/>
    <text x="290" y="267" font-family="Arial,sans-serif" font-size="7" fill="#333">Термопары, пирометры</text>
    <circle cx="280" cy="275" r="3" fill="#F57C00"/>
    <text x="290" y="279" font-family="Arial,sans-serif" font-size="7" fill="#333">Газовые термометры (точные)</text>
    '''
    s += ftr("Молекулярная физика", 35)
    return s

# ===== LESSON 36: Уравнение состояния идеального газа =====
def lesson36():
    s = hdr("Уравнение состояния идеального газа","Физика 10 класс — Урок 36")
    s += f'''
    <!-- Mendeleev-Clapeyron -->
    <rect x="25" y="62" width="250" height="100" rx="5" fill="white" stroke="#E53935" stroke-width="1.5"/>
    <text x="150" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Уравнение Менделеева-Клапейрона</text>
    <line x1="35" y1="83" x2="265" y2="83" stroke="#E53935" stroke-width="0.5" opacity="0.3"/>
    <text x="150" y="105" font-family="Arial,sans-serif" font-size="16" fill="#333" text-anchor="middle" font-weight="bold">pV = (m/M)*R*T</text>
    <text x="150" y="125" font-family="Arial,sans-serif" font-size="9" fill="#555" text-anchor="middle">R = 8.31 Дж/(моль*К) — универсальная газовая постоянная</text>
    <text x="150" y="140" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">R = N(A)*k — связь R и k</text>

    <!-- Variables -->
    <rect x="285" y="62" width="190" height="100" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="380" y="78" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Величины</text>
    <line x1="295" y1="83" x2="465" y2="83" stroke="#2E7D32" stroke-width="0.5" opacity="0.3"/>
    <text x="305" y="97" font-family="Arial,sans-serif" font-size="8" fill="#333">p — давление (Па)</text>
    <text x="305" y="110" font-family="Arial,sans-serif" font-size="8" fill="#333">V — объём (м3)</text>
    <text x="305" y="123" font-family="Arial,sans-serif" font-size="8" fill="#333">m — масса газа (кг)</text>
    <text x="305" y="136" font-family="Arial,sans-serif" font-size="8" fill="#333">M — молярная масса (кг/моль)</text>
    <text x="305" y="149" font-family="Arial,sans-serif" font-size="8" fill="#333">T — температура (К)</text>

    <!-- Other forms -->
    <rect x="25" y="172" width="225" height="60" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="137" y="188" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Другие формы записи</text>
    <line x1="35" y1="193" x2="240" y2="193" stroke="#F57C00" stroke-width="0.5" opacity="0.3"/>
    <text x="137" y="208" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">p = n*k*T</text>
    <text x="137" y="224" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">pV = nu*R*T</text>

    <!-- Isoprocess formula -->
    <rect x="260" y="172" width="215" height="60" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="367" y="188" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Для изопроцессов</text>
    <line x1="270" y1="193" x2="465" y2="193" stroke="#7B1FA2" stroke-width="0.5" opacity="0.3"/>
    <text x="367" y="208" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">p1*V1/T1 = p2*V2/T2</text>
    <text x="367" y="224" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Если m = const</text>

    <!-- Important -->
    <rect x="25" y="245" width="450" height="30" rx="4" fill="white" stroke="#E53935" stroke-width="1"/>
    <text x="250" y="264" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle">Уравнение состояния связывает p, V, T — достаточно знать 2, чтобы найти 3-е! | 1 атм = 10^5 Па | 0 C = 273 K</text>
    '''
    s += ftr("Молекулярная физика", 36)
    return s

# ===== LESSON 37: Газовые законы =====
def lesson37():
    s = hdr("Газовые законы","Физика 10 класс — Урок 37")
    s += f'''
    <!-- Isothermal p(V) -->
    <rect x="25" y="62" width="155" height="115" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="102" y="77" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" font-weight="bold" text-anchor="middle">Изотермический</text>
    <text x="102" y="87" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">T = const</text>
    <!-- Axes -->
    {arr(45,155,45,95,"#333",1,5)}
    {arr(45,155,155,155,"#333",1,5)}
    <text x="155" y="168" font-family="Arial,sans-serif" font-size="8" fill="#333">V</text>
    <text x="38" y="95" font-family="Arial,sans-serif" font-size="8" fill="#333">p</text>
    <!-- Hyperbola -->
    <path d="M 55 105 Q 80 130 135 150" fill="none" stroke="#2E7D32" stroke-width="2.5"/>
    <text x="102" y="145" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">pV=const</text>

    <!-- Isobaric V(T) -->
    <rect x="190" y="62" width="155" height="115" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="267" y="77" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" font-weight="bold" text-anchor="middle">Изобарный</text>
    <text x="267" y="87" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">p = const</text>
    {arr(210,155,210,95,"#333",1,5)}
    {arr(210,155,320,155,"#333",1,5)}
    <text x="320" y="168" font-family="Arial,sans-serif" font-size="8" fill="#333">T</text>
    <text x="203" y="95" font-family="Arial,sans-serif" font-size="8" fill="#333">V</text>
    <!-- Linear V/T -->
    <line x1="210" y1="155" x2="310" y2="105" stroke="#F57C00" stroke-width="2.5"/>
    <text x="267" y="145" font-family="Arial,sans-serif" font-size="7" fill="#F57C00" text-anchor="middle">V/T=const</text>

    <!-- Isochoric p(T) -->
    <rect x="355" y="62" width="125" height="115" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="417" y="77" font-family="Arial,sans-serif" font-size="8" fill="#E53935" font-weight="bold" text-anchor="middle">Изохорный</text>
    <text x="417" y="87" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">V = const</text>
    {arr(375,155,375,95,"#333",1,5)}
    {arr(375,155,465,155,"#333",1,5)}
    <text x="465" y="168" font-family="Arial,sans-serif" font-size="8" fill="#333">T</text>
    <text x="368" y="95" font-family="Arial,sans-serif" font-size="8" fill="#333">p</text>
    <line x1="375" y1="155" x2="455" y2="105" stroke="#E53935" stroke-width="2.5"/>
    <text x="417" y="145" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle">p/T=const</text>

    <!-- Laws table -->
    <rect x="25" y="190" width="155" height="80" rx="5" fill="white" stroke="#2E7D32" stroke-width="1"/>
    <text x="102" y="206" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" font-weight="bold" text-anchor="middle">Бойль-Мариотт</text>
    <text x="102" y="222" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">p1V1 = p2V2</text>
    <text x="102" y="240" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">T = const, m = const</text>
    <text x="102" y="255" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Гипербола</text>

    <rect x="190" y="190" width="155" height="80" rx="5" fill="white" stroke="#F57C00" stroke-width="1"/>
    <text x="267" y="206" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" font-weight="bold" text-anchor="middle">Гей-Люссак</text>
    <text x="267" y="222" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">V1/T1 = V2/T2</text>
    <text x="267" y="240" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">p = const, m = const</text>
    <text x="267" y="255" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Прямая через 0 K</text>

    <rect x="355" y="190" width="125" height="80" rx="5" fill="white" stroke="#E53935" stroke-width="1"/>
    <text x="417" y="206" font-family="Arial,sans-serif" font-size="8" fill="#E53935" font-weight="bold" text-anchor="middle">Шарль</text>
    <text x="417" y="222" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">p1/T1 = p2/T2</text>
    <text x="417" y="240" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">V = const, m = const</text>
    <text x="417" y="255" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Прямая через 0 K</text>

    <!-- Note -->
    <rect x="25" y="280" width="455" height="20" rx="4" fill="white" stroke="#1565C0" stroke-width="1"/>
    <text x="252" y="294" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle">Все законы — частные случаи уравнения Менделеева-Клапейрона | T в Кельвинах!</text>
    '''
    s += ftr("Молекулярная физика", 37)
    return s

# ===== LESSON 38: Взаимодействие молекул =====
def lesson38():
    s = hdr("Взаимодействие молекул газа и жидкости","Физика 10 класс — Урок 38")
    s += f'''
    <!-- Potential energy curve -->
    <rect x="25" y="62" width="250" height="140" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="150" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Потенциальная энергия взаимодействия</text>
    <!-- Axes -->
    {arr(70,175,70,85,"#333",1,5)}
    {arr(70,175,260,175,"#333",1,5)}
    <text x="258" y="188" font-family="Arial,sans-serif" font-size="9" fill="#333">r</text>
    <text x="63" y="88" font-family="Arial,sans-serif" font-size="9" fill="#333">E</text>
    <!-- r0 label -->
    <line x1="140" y1="175" x2="140" y2="130" stroke="#555" stroke-width="0.5" stroke-dasharray="2,2"/>
    <text x="140" y="190" font-family="Arial,sans-serif" font-size="7" fill="#555">r0</text>
    <!-- E=0 line -->
    <line x1="70" y1="145" x2="260" y2="145" stroke="#555" stroke-width="0.5" stroke-dasharray="3,3"/>
    <text x="60" y="149" font-family="Arial,sans-serif" font-size="7" fill="#555">0</text>
    <!-- Potential curve -->
    <path d="M 80 145 Q 110 190 140 125 Q 165 85 200 95 Q 230 105 255 135" fill="none" stroke="#E53935" stroke-width="2.5"/>
    <!-- r0 point -->
    <circle cx="140" cy="125" r="3" fill="#2E7D32"/>
    <text x="148" y="120" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">min E</text>
    <!-- Attraction region -->
    <text x="200" y="160" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">притяжение</text>
    <!-- Repulsion region -->
    <text x="95" y="170" font-family="Arial,sans-serif" font-size="7" fill="#E53935">отталкивание</text>

    <!-- Surface tension -->
    <rect x="285" y="62" width="190" height="140" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="380" y="78" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Поверхностное натяжение</text>

    <!-- Water surface with molecules -->
    <rect x="300" y="120" width="160" height="55" fill="#42A5F5" opacity="0.2" rx="3"/>
    <!-- Surface molecules (unbalanced forces) -->
    <circle cx="340" cy="118" r="4" fill="#E53935" opacity="0.8"/>
    <!-- Force arrows down into liquid -->
    {arr(340,122,340,135,"#E53935",1,4)}
    <!-- No force up (air side) -->

    <!-- Interior molecule (balanced) -->
    <circle cx="380" cy="145" r="4" fill="#2E7D32" opacity="0.8"/>
    {arr(380,141,380,133,"#2E7D32",0.8,3)}
    {arr(380,149,380,157,"#2E7D32",0.8,3)}
    {arr(376,145,368,145,"#2E7D32",0.8,3)}
    {arr(384,145,392,145,"#2E7D32",0.8,3)}

    <!-- Surface tension force -->
    {arr(310,118,340,118,"#F57C00",1.5,5)}
    <text x="320" y="113" font-family="Arial,sans-serif" font-size="7" fill="#F57C00">F(пов)</text>

    <text x="380" y="185" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">sigma = F/l</text>
    <text x="380" y="197" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">[sigma] = Н/м</text>

    <!-- Phenomena -->
    <rect x="25" y="215" width="225" height="55" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="137" y="231" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Явления в жидкостях</text>
    <circle cx="45" cy="243" r="3" fill="#2E7D32"/>
    <text x="55" y="247" font-family="Arial,sans-serif" font-size="7" fill="#333">Смачивание</text>
    <circle cx="130" cy="243" r="3" fill="#1565C0"/>
    <text x="140" y="247" font-family="Arial,sans-serif" font-size="7" fill="#333">Капилляры</text>
    <circle cx="45" cy="258" r="3" fill="#E53935"/>
    <text x="55" y="262" font-family="Arial,sans-serif" font-size="7" fill="#333">Мениск</text>
    <circle cx="130" cy="258" r="3" fill="#F57C00"/>
    <text x="140" y="262" font-family="Arial,sans-serif" font-size="7" fill="#333">Капиллярность</text>

    <rect x="260" y="215" width="215" height="55" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="367" y="231" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Формула Жюрена</text>
    <text x="367" y="248" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">h = 2*sigma/(rho*g*r)</text>
    <text x="367" y="264" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">r — радиус капилляра</text>
    '''
    s += ftr("Молекулярная физика", 38)
    return s

# ===== LESSON 39: Внутренняя энергия =====
def lesson39():
    s = hdr("Внутренняя энергия","Физика 10 класс — Урок 39")
    s += f'''
    <!-- Internal energy components -->
    <rect x="25" y="62" width="225" height="130" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="137" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Внутренняя энергия U</text>

    <!-- Central circle -->
    <circle cx="137" cy="135" r="30" fill="#1565C0" opacity="0.1" stroke="#1565C0" stroke-width="2"/>
    <text x="137" y="133" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" text-anchor="middle" font-weight="bold">U</text>
    <text x="137" y="145" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">внутр. энергия</text>

    <!-- Kinetic component -->
    <rect x="35" y="95" width="75" height="22" rx="3" fill="#E53935" opacity="0.2" stroke="#E53935" stroke-width="1"/>
    <text x="72" y="110" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle">E(кин) молекул</text>
    <line x1="110" y1="106" x2="115" y2="120" stroke="#E53935" stroke-width="1"/>

    <!-- Potential component -->
    <rect x="155" y="95" width="75" height="22" rx="3" fill="#2E7D32" opacity="0.2" stroke="#2E7D32" stroke-width="1"/>
    <text x="192" y="110" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">E(пот) молекул</text>
    <line x1="155" y1="106" x2="150" y2="120" stroke="#2E7D32" stroke-width="1"/>

    <text x="137" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">U = сумма E(кин) + E(пот) всех молекул</text>
    <text x="137" y="186" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">[U] = Дж</text>

    <!-- Ideal gas -->
    <rect x="260" y="62" width="215" height="70" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="367" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Идеальный газ</text>
    <text x="367" y="95" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">E(пот) = 0 (нет взаимодействия)</text>
    <text x="367" y="110" font-family="Arial,sans-serif" font-size="10" fill="#E53935" text-anchor="middle" font-weight="bold">U = (3/2)*(m/M)*R*T</text>
    <text x="367" y="125" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">U зависит только от T!</text>

    <!-- Ways to change U -->
    <rect x="260" y="140" width="215" height="52" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="367" y="156" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Изменение U</text>
    <rect x="270" y="163" width="90" height="20" rx="3" fill="#FFEBEE" stroke="#E53935" stroke-width="0.8"/>
    <text x="315" y="177" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle">Теплопередача Q</text>
    <rect x="370" y="163" width="95" height="20" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
    <text x="417" y="177" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle">Работа A</text>

    <!-- Work and heat -->
    <rect x="25" y="205" width="225" height="65" rx="5" fill="white" stroke="#F57C00" stroke-width="1.2"/>
    <text x="137" y="221" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" font-weight="bold" text-anchor="middle">Работа в термодинамике</text>
    <line x1="35" y1="226" x2="240" y2="226" stroke="#F57C00" stroke-width="0.5" opacity="0.3"/>
    <text x="137" y="242" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">A = p*dV (газ расширяется)</text>
    <text x="137" y="256" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">A > 0: газ совершает работу</text>
    <text x="137" y="268" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">A' = -A (работа над газом)</text>

    <rect x="260" y="205" width="215" height="65" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="367" y="221" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Виды теплопередачи</text>
    <circle cx="275" cy="235" r="3" fill="#E53935"/>
    <text x="285" y="239" font-family="Arial,sans-serif" font-size="7" fill="#333">Теплопроводность</text>
    <circle cx="275" cy="248" r="3" fill="#F57C00"/>
    <text x="285" y="252" font-family="Arial,sans-serif" font-size="7" fill="#333">Конвекция</text>
    <circle cx="275" cy="261" r="3" fill="#2E7D32"/>
    <text x="285" y="265" font-family="Arial,sans-serif" font-size="7" fill="#333">Излучение</text>
    <text x="390" y="239" font-family="Arial,sans-serif" font-size="7" fill="#555">(без переноса в-ва)</text>
    <text x="390" y="252" font-family="Arial,sans-serif" font-size="7" fill="#555">(поток жидкости/газа)</text>
    <text x="390" y="265" font-family="Arial,sans-serif" font-size="7" fill="#555">(электромагнитные волны)</text>
    '''
    s += ftr("Молекулярная физика", 39)
    return s

# ===== LESSON 40: Работа в термодинамике =====
def lesson40():
    s = hdr("Работа в термодинамике","Физика 10 класс — Урок 40")
    s += f'''
    <!-- p-V diagram with work = area -->
    <rect x="25" y="62" width="250" height="155" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
    <text x="150" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold" text-anchor="middle">Работа газа на p-V диаграмме</text>

    <!-- Axes -->
    {arr(55,195,55,88,"#333",1.5,6)}
    {arr(55,195,260,195,"#333",1.5,6)}
    <text x="258" y="208" font-family="Arial,sans-serif" font-size="10" fill="#333" font-style="italic">V</text>
    <text x="48" y="88" font-family="Arial,sans-serif" font-size="10" fill="#333" font-style="italic">p</text>

    <!-- Isobaric process line -->
    <line x1="55" y1="130" x2="230" y2="130" stroke="#E53935" stroke-width="2.5"/>
    <text x="150" y="125" font-family="Arial,sans-serif" font-size="8" fill="#E53935">p = const</text>

    <!-- Shaded area = work -->
    <rect x="55" y="130" width="175" height="65" fill="#E53935" opacity="0.15" stroke="none"/>
    <text x="150" y="168" font-family="Arial,sans-serif" font-size="10" fill="#E53935" text-anchor="middle" font-weight="bold">A = p*dV</text>
    <text x="150" y="185" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle">= площадь</text>

    <!-- V1 and V2 marks -->
    <line x1="55" y1="195" x2="55" y2="200" stroke="#333" stroke-width="1"/>
    <text x="55" y="212" font-family="Arial,sans-serif" font-size="8" fill="#333">V1</text>
    <line x1="230" y1="195" x2="230" y2="200" stroke="#333" stroke-width="1"/>
    <text x="230" y="212" font-family="Arial,sans-serif" font-size="8" fill="#333">V2</text>

    <!-- Isothermal work (curved) -->
    <path d="M 55 130 Q 120 105 230 92" fill="none" stroke="#2E7D32" stroke-width="2" stroke-dasharray="4,2"/>
    <text x="170" y="98" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">T = const</text>

    <!-- Formulas -->
    <rect x="285" y="62" width="190" height="155" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
    <text x="380" y="78" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold" text-anchor="middle">Формулы работы</text>
    <line x1="295" y1="83" x2="465" y2="83" stroke="#E53935" stroke-width="0.5" opacity="0.3"/>

    <text x="380" y="100" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Изобарная:</text>
    <text x="380" y="115" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">A = p*(V2-V1)</text>

    <text x="380" y="135" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Изотермическая:</text>
    <text x="380" y="150" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">A = (m/M)*R*T*ln(V2/V1)</text>

    <text x="380" y="170" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Изохорная:</text>
    <text x="380" y="185" font-family="Arial,sans-serif" font-size="9" fill="#E53935" text-anchor="middle">A = 0 (V = const)</text>

    <text x="380" y="205" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">dV > 0: A > 0 (газ работает)</text>
    <text x="380" y="215" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">dV &lt; 0: A &lt; 0 (над газом)</text>

    <!-- Cyclic process -->
    <rect x="25" y="228" width="225" height="45" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
    <text x="137" y="244" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" font-weight="bold" text-anchor="middle">Циклический процесс</text>
    <text x="137" y="260" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">A(цикл) = площадь внутри цикла</text>

    <rect x="260" y="228" width="215" height="45" rx="5" fill="white" stroke="#2E7D32" stroke-width="1"/>
    <text x="367" y="244" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold" text-anchor="middle">Графический смысл</text>
    <text x="367" y="260" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">A = площадь под кривой p(V)</text>
    '''
    s += ftr("Термодинамика", 40)
    return s

# Generate
gens = {31:lesson31,32:lesson32,33:lesson33,34:lesson34,35:lesson35,
        36:lesson36,37:lesson37,38:lesson38,39:lesson39,40:lesson40}

for n,g in gens.items():
    svg = g()
    with open(os.path.join(OUT,f"lesson{n}.svg"),'w',encoding='utf-8') as f:
        f.write(svg)
    print(f"lesson{n}.svg ({len(svg)} bytes)")

print("Done!")
