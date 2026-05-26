#!/usr/bin/env python3
"""Generate Physics grade 10 SVG lesson illustrations (lessons 41-50)."""
import os
OUT = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade10/physics"
os.makedirs(OUT, exist_ok=True)
P = "#1565C0"; L = "#E3F2FD"; M = "#BBDEFB"
def hdr(title, num):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{L}"/><stop offset="100%" stop-color="{M}"/></linearGradient></defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="{P}" stroke-width="2.5"/>
<text x="250" y="30" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="{P}" text-anchor="middle">{title}</text>
<text x="250" y="46" font-family="Arial,sans-serif" font-size="10" fill="#888" text-anchor="middle">Физика 10 класс — Урок {num}</text>
<line x1="30" y1="52" x2="470" y2="52" stroke="{P}" stroke-width="1.5" opacity="0.25"/>
'''
ftr = f'\n<rect x="10" y="325" width="480" height="20" rx="4" fill="{P}" opacity="0.85"/>\n<text x="250" y="339" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="white" font-weight="bold">Физика 10 класс</text>\n</svg>'
def ib(x,y,w,h,lines):
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="white" stroke="{P}" stroke-width="1" opacity="0.9"/>\n'
    for i,l in enumerate(lines): s+=f'<text x="{x+w//2}" y="{y+14+i*11}" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">{l}</text>\n'
    return s

# 41: Масса и размеры молекул. Количество вещества
svg41=hdr("Масса и размеры молекул. Количество вещества",41)+f'''
<g transform="translate(130,175)">
<!-- Molecule cluster -->
<circle cx="0" cy="-20" r="8" fill="{L}" stroke="{P}" stroke-width="1.5"/>
<circle cx="12" cy="-5" r="8" fill="{L}" stroke="{P}" stroke-width="1.5"/>
<circle cx="-12" cy="-5" r="8" fill="{L}" stroke="{P}" stroke-width="1.5"/>
<circle cx="0" cy="10" r="8" fill="{L}" stroke="{P}" stroke-width="1.5"/>
<circle cx="18" cy="-20" r="8" fill="{L}" stroke="{P}" stroke-width="1.5"/>
<circle cx="-18" cy="-20" r="8" fill="{L}" stroke="{P}" stroke-width="1.5"/>
<!-- Size bracket -->
<line x1="-8" y1="18" x2="-8" y2="25" stroke="#E53935" stroke-width="1"/>
<line x1="8" y1="18" x2="8" y2="25" stroke="#E53935" stroke-width="1"/>
<line x1="-8" y1="22" x2="8" y2="22" stroke="#E53935" stroke-width="1"/>
<text x="0" y="35" font-family="Arial,sans-serif" font-size="5" fill="#E53935" text-anchor="middle">d ~ 10^-10 м</text>
<text x="0" y="50" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Размер молекулы</text>
</g>
<g transform="translate(370,115)">
<rect x="-95" y="-48" width="190" height="96" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-33" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Постоянная Авогадро</text>
<line x1="-80" y1="-26" x2="80" y2="-26" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="9" fill="#E53935" text-anchor="middle" font-weight="bold">NA = 6.02*10^23 моль^-1</text>
<text x="0" y="6" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Число частиц в 1 моле вещества</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">1 моль = NA молекул</text>
<text x="0" y="34" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Моль — единица количества вещества</text>
</g>
<g transform="translate(370,225)">
<rect x="-95" y="-38" width="190" height="76" rx="5" fill="white" stroke="#E65100" stroke-width="1.2"/>
<text x="0" y="-23" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">Количество вещества</text>
<line x1="-80" y1="-16" x2="80" y2="-16" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">v = N / NA</text>
<text x="0" y="16" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">m0 = M / NA</text>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">v — кол-во вещества (моль), m0 — масса молекулы</text>
</g>
<g transform="translate(130,280)">
<rect x="-80" y="-15" width="160" height="30" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">m = N * m0 = v * M</text>
</g>
'''+ftr

# 42: Идеальный газ. Основное уравнение МКТ
svg42=hdr("Идеальный газ. Основное уравнение МКТ",42)+f'''
<g transform="translate(130,185)">
<!-- Gas container -->
<rect x="-60" y="-55" width="120" height="100" rx="3" fill="white" stroke="{P}" stroke-width="2"/>
<!-- Molecules bouncing -->
<circle cx="-30" cy="-30" r="5" fill="{L}" stroke="{P}" stroke-width="1"/>
<circle cx="20" cy="-20" r="5" fill="{L}" stroke="{P}" stroke-width="1"/>
<circle cx="-10" cy="10" r="5" fill="{L}" stroke="{P}" stroke-width="1"/>
<circle cx="35" cy="15" r="5" fill="{L}" stroke="{P}" stroke-width="1"/>
<circle cx="-40" cy="20" r="5" fill="{L}" stroke="{P}" stroke-width="1"/>
<circle cx="10" cy="-40" r="5" fill="{L}" stroke="{P}" stroke-width="1"/>
<circle cx="40" cy="-35" r="5" fill="{L}" stroke="{P}" stroke-width="1"/>
<!-- Velocity arrows -->
<line x1="-25" y1="-30" x2="-10" y2="-38" stroke="#2E7D32" stroke-width="1"/>
<polygon points="-10,-38 -15,-38 -12,-33" fill="#2E7D32"/>
<line x1="25" y1="-20" x2="35" y2="-10" stroke="#2E7D32" stroke-width="1"/>
<polygon points="35,-10 30,-12 33,-16" fill="#2E7D32"/>
<line x1="-5" y1="15" x2="-20" y2="25" stroke="#2E7D32" stroke-width="1"/>
<polygon points="-20,25 -15,22 -18,28" fill="#2E7D32"/>
<line x1="40" y1="20" x2="45" y2="30" stroke="#2E7D32" stroke-width="1"/>
<polygon points="45,30 41,26 46,27" fill="#2E7D32"/>
<!-- Pressure arrows on walls -->
<line x1="-60" y1="-20" x2="-70" y2="-20" stroke="#E53935" stroke-width="1.5"/>
<polygon points="-70,-20 -64,-23 -64,-17" fill="#E53935"/>
<line x1="60" y1="0" x2="70" y2="0" stroke="#E53935" stroke-width="1.5"/>
<polygon points="70,0 64,-3 64,3" fill="#E53935"/>
<line x1="0" y1="-55" x2="0" y2="-65" stroke="#E53935" stroke-width="1.5"/>
<polygon points="0,-65 -3,-59 3,-59" fill="#E53935"/>
<text x="0" y="58" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Модель идеального газа</text>
</g>
<g transform="translate(370,120)">
<rect x="-95" y="-55" width="190" height="110" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Основное уравнение МКТ</text>
<line x1="-80" y1="-33" x2="80" y2="-33" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="9" fill="#E53935" text-anchor="middle" font-weight="bold">p = (1/3)*n*m0*v^2</text>
<line x1="-80" y1="-5" x2="80" y2="-5" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">p = (2/3)*n*Ek</text>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">n — концентрация (1/м^3)</text>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Ek — средняя кин. энергия молекул</text>
</g>
<g transform="translate(370,248)">
<rect x="-85" y="-28" width="170" height="56" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
<text x="0" y="-13" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Допущения модели</text>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Молекулы — материальные точки</text>
<text x="0" y="15" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Взаимодействие — только столкновения</text>
</g>
'''+ftr

# 43: Температура. Термодинамическое определение температуры
svg43=hdr("Температура. Термодинамическое определение",43)+f'''
<g transform="translate(120,185)">
<!-- Thermometer -->
<rect x="-8" y="-60" width="16" height="90" rx="8" fill="white" stroke="#333" stroke-width="1.5"/>
<!-- Mercury column -->
<rect x="-4" y="-20" width="8" height="50" rx="4" fill="#E53935"/>
<!-- Bulb -->
<circle cx="0" cy="35" r="12" fill="#E53935" stroke="#333" stroke-width="1.5"/>
<!-- Scale marks -->
<line x1="8" y1="-45" x2="15" y2="-45" stroke="#333" stroke-width="1"/>
<text x="20" y="-42" font-family="Arial,sans-serif" font-size="5" fill="#333">100</text>
<line x1="8" y1="-20" x2="15" y2="-20" stroke="#333" stroke-width="1"/>
<text x="20" y="-17" font-family="Arial,sans-serif" font-size="5" fill="#333">0</text>
<line x1="8" y1="5" x2="15" y2="5" stroke="#333" stroke-width="1"/>
<text x="20" y="8" font-family="Arial,sans-serif" font-size="5" fill="#333">-50</text>
<text x="0" y="62" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">°C</text>
</g>
<g transform="translate(310,125)">
<rect x="-110" y="-55" width="220" height="110" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Связь температуры и энергии</text>
<line x1="-95" y1="-33" x2="95" y2="-33" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="10" fill="#E53935" text-anchor="middle" font-weight="bold">Ek = (3/2)*k*T</text>
<line x1="-95" y1="-5" x2="95" y2="-5" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">k = 1.38*10^-23 Дж/К</text>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Постоянная Больцмана</text>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">T — абсолютная температура (Кельвин)</text>
</g>
<g transform="translate(310,245)">
<rect x="-110" y="-35" width="220" height="70" rx="5" fill="white" stroke="#E65100" stroke-width="1.2"/>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">Шкалы температуры</text>
<line x1="-95" y1="-13" x2="95" y2="-13" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">T(K) = t(°C) + 273</text>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">0 K = -273 °C — абсолютный ноль</text>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">Ek = 0 при T = 0 K</text>
</g>
'''+ftr

# 44: Уравнение состояния идеального газа
svg44=hdr("Уравнение состояния идеального газа",44)+f'''
<g transform="translate(130,185)">
<!-- Gas cylinder with piston -->
<rect x="-50" y="-50" width="100" height="80" rx="3" fill="white" stroke="{P}" stroke-width="2"/>
<!-- Piston -->
<rect x="-50" y="-55" width="100" height="8" rx="2" fill="#795548" stroke="#5D4037" stroke-width="1"/>
<!-- Molecules -->
<circle cx="-20" cy="-15" r="4" fill="{L}" stroke="{P}" stroke-width="1"/>
<circle cx="15" cy="-10" r="4" fill="{L}" stroke="{P}" stroke-width="1"/>
<circle cx="-5" cy="5" r="4" fill="{L}" stroke="{P}" stroke-width="1"/>
<circle cx="25" cy="15" r="4" fill="{L}" stroke="{P}" stroke-width="1"/>
<circle cx="-30" cy="10" r="4" fill="{L}" stroke="{P}" stroke-width="1"/>
<circle cx="5" cy="20" r="4" fill="{L}" stroke="{P}" stroke-width="1"/>
<!-- Labels -->
<line x1="55" y1="-55" x2="55" y2="30" stroke="#E53935" stroke-width="1" stroke-dasharray="3,2"/>
<line x1="50" y1="-55" x2="60" y2="-55" stroke="#E53935" stroke-width="1"/>
<line x1="50" y1="30" x2="60" y2="30" stroke="#E53935" stroke-width="1"/>
<text x="70" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#E53935">V</text>
<!-- Pressure arrow -->
<line x1="0" y1="-58" x2="0" y2="-72" stroke="#2E7D32" stroke-width="1.5"/>
<polygon points="0,-72 -3,-66 3,-66" fill="#2E7D32"/>
<text x="10" y="-68" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">p</text>
<!-- Temperature -->
<text x="0" y="45" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle">T</text>
</g>
<g transform="translate(370,120)">
<rect x="-95" y="-55" width="190" height="110" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Уравнение Менделеева-Клапейрона</text>
<line x1="-80" y1="-33" x2="80" y2="-33" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="14" fill="#E53935" text-anchor="middle" font-weight="bold">pV = vRT</text>
<line x1="-80" y1="0" x2="80" y2="0" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">R = 8.31 Дж/(моль*К)</text>
<text x="0" y="33" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Универсальная газовая постоянная</text>
<text x="0" y="46" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">R = NA * k</text>
</g>
<g transform="translate(370,245)">
<rect x="-95" y="-28" width="190" height="56" rx="5" fill="white" stroke="#E65100" stroke-width="1.2"/>
<text x="0" y="-13" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">Другие формы</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">p = nkT | n = N/V</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Уравнение состояния связывает p, V, T</text>
</g>
'''+ftr

# 45: Изопроцессы
svg45=hdr("Изопроцессы",45)+f'''
<!-- Isothermal: p-V graph -->
<g transform="translate(90,150)">
<rect x="-70" y="-65" width="140" height="130" rx="5" fill="white" stroke="{P}" stroke-width="1.2"/>
<text x="0" y="-50" font-family="Arial,sans-serif" font-size="6" fill="{P}" text-anchor="middle" font-weight="bold">Изотермический</text>
<text x="0" y="-38" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">T = const</text>
<!-- Axes -->
<line x1="-45" y1="40" x2="55" y2="40" stroke="#333" stroke-width="1"/>
<line x1="-45" y1="40" x2="-45" y2="-25" stroke="#333" stroke-width="1"/>
<polygon points="55,40 50,37 50,43" fill="#333"/>
<polygon points="-45,-25 -48,-20 -42,-20" fill="#333"/>
<text x="55" y="52" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">V</text>
<text x="-55" y="-25" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">p</text>
<!-- Isotherm curve p~1/V -->
<path d="M-35,-15 Q10,-10 48,35" fill="none" stroke="#E53935" stroke-width="2"/>
<!-- Second isotherm -->
<path d="M-35,5 Q5,10 48,38" fill="none" stroke="#E53935" stroke-width="1.5" stroke-dasharray="4,2"/>
<text x="10" y="55" font-family="Arial,sans-serif" font-size="5" fill="#E53935" text-anchor="middle">pV = const</text>
</g>
<!-- Isobaric: V-T graph -->
<g transform="translate(250,150)">
<rect x="-70" y="-65" width="140" height="130" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-50" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Изобарный</text>
<text x="0" y="-38" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">p = const</text>
<!-- Axes -->
<line x1="-45" y1="40" x2="55" y2="40" stroke="#333" stroke-width="1"/>
<line x1="-45" y1="40" x2="-45" y2="-25" stroke="#333" stroke-width="1"/>
<polygon points="55,40 50,37 50,43" fill="#333"/>
<polygon points="-45,-25 -48,-20 -42,-20" fill="#333"/>
<text x="55" y="52" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">T</text>
<text x="-55" y="-25" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">V</text>
<!-- Isobar line -->
<line x1="-35" y1="35" x2="48" y2="-20" stroke="#2E7D32" stroke-width="2"/>
<!-- Second isobar -->
<line x1="-35" y1="25" x2="48" y2="-5" stroke="#2E7D32" stroke-width="1.5" stroke-dasharray="4,2"/>
<text x="10" y="55" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">V/T = const</text>
</g>
<!-- Isochoric: p-T graph -->
<g transform="translate(410,150)">
<rect x="-70" y="-65" width="140" height="130" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
<text x="0" y="-50" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Изохорный</text>
<text x="0" y="-38" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">V = const</text>
<!-- Axes -->
<line x1="-45" y1="40" x2="55" y2="40" stroke="#333" stroke-width="1"/>
<line x1="-45" y1="40" x2="-45" y2="-25" stroke="#333" stroke-width="1"/>
<polygon points="55,40 50,37 50,43" fill="#333"/>
<polygon points="-45,-25 -48,-20 -42,-20" fill="#333"/>
<text x="55" y="52" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">T</text>
<text x="-55" y="-25" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">p</text>
<!-- Isochor line -->
<line x1="-35" y1="35" x2="48" y2="-20" stroke="#7B1FA2" stroke-width="2"/>
<!-- Second isochor -->
<line x1="-35" y1="25" x2="48" y2="-5" stroke="#7B1FA2" stroke-width="1.5" stroke-dasharray="4,2"/>
<text x="10" y="55" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="middle">p/T = const</text>
</g>
<!-- Laws summary -->
<g transform="translate(250,285)">
<rect x="-200" y="-18" width="400" height="30" rx="5" fill="white" stroke="#FF6F00" stroke-width="1.2"/>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle" font-weight="bold">Закон Бойля-Мариотта | Закон Гей-Люссака | Закон Шарля</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Все изопроцессы — частные случаи уравнения Менделеева-Клапейрона</text>
</g>
'''+ftr

# 46: Внутренняя энергия. Работа в термодинамике
svg46=hdr("Внутренняя энергия. Работа в термодинамике",46)+f'''
<g transform="translate(130,180)">
<!-- Cylinder with piston -->
<rect x="-55" y="-45" width="110" height="80" rx="3" fill="white" stroke="{P}" stroke-width="2"/>
<!-- Piston (moves right) -->
<rect x="20" y="-45" width="10" height="80" rx="2" fill="#795548" stroke="#5D4037" stroke-width="1"/>
<!-- Gas molecules left of piston -->
<circle cx="-30" cy="-20" r="4" fill="{L}" stroke="{P}" stroke-width="1"/>
<circle cx="-10" cy="-5" r="4" fill="{L}" stroke="{P}" stroke-width="1"/>
<circle cx="-25" cy="10" r="4" fill="{L}" stroke="{P}" stroke-width="1"/>
<circle cx="-40" cy="5" r="4" fill="{L}" stroke="{P}" stroke-width="1"/>
<circle cx="0" cy="20" r="4" fill="{L}" stroke="{P}" stroke-width="1"/>
<circle cx="-15" cy="-30" r="4" fill="{L}" stroke="{P}" stroke-width="1"/>
<!-- Displacement arrow -->
<line x1="30" y1="50" x2="60" y2="50" stroke="#2E7D32" stroke-width="1.5"/>
<polygon points="60,50 54,47 54,53" fill="#2E7D32"/>
<text x="45" y="62" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">deltaV</text>
<!-- Work arrow on piston -->
<line x1="30" y1="0" x2="50" y2="0" stroke="#E53935" stroke-width="1.5"/>
<polygon points="50,0 44,-3 44,3" fill="#E53935"/>
<text x="42" y="-6" font-family="Arial,sans-serif" font-size="5" fill="#E53935">A</text>
<!-- p label -->
<text x="-10" y="-50" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">p</text>
</g>
<g transform="translate(380,120)">
<rect x="-100" y="-55" width="200" height="110" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Внутренняя энергия</text>
<line x1="-85" y1="-33" x2="85" y2="-33" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-14" font-family="Arial,sans-serif" font-size="11" fill="#E53935" text-anchor="middle" font-weight="bold">U = (3/2)*vRT</text>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Одноатомный идеальный газ</text>
<line x1="-85" y1="14" x2="85" y2="14" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">deltaU = (3/2)*vR*deltaT</text>
<text x="0" y="44" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Зависит только от температуры</text>
</g>
<g transform="translate(380,245)">
<rect x="-100" y="-30" width="200" height="60" rx="5" fill="white" stroke="#E65100" stroke-width="1.2"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">Работа газа</text>
<line x1="-85" y1="-8" x2="85" y2="-8" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle" font-weight="bold">A = p*deltaV</text>
<text x="0" y="24" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">A &gt; 0 — газ расширяется, A &lt; 0 — газ сжимается</text>
</g>
'''+ftr

# 47: Первый закон термодинамики
svg47=hdr("Первый закон термодинамики",47)+f'''
<g transform="translate(250,180)">
<!-- Central energy system box -->
<rect x="-60" y="-50" width="120" height="80" rx="8" fill="white" stroke="{P}" stroke-width="2.5"/>
<text x="0" y="-30" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Термодинамическая</text>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">система</text>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="10" fill="#E53935" text-anchor="middle" font-weight="bold">deltaU</text>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Внутренняя энергия</text>
<!-- Q arrow coming in (heat) -->
<line x1="-160" y1="0" x2="-65" y2="0" stroke="#E53935" stroke-width="2.5"/>
<polygon points="-65,0 -71,-4 -71,4" fill="#E53935"/>
<text x="-110" y="-10" font-family="Arial,sans-serif" font-size="10" fill="#E53935" text-anchor="middle" font-weight="bold">Q</text>
<text x="-110" y="18" font-family="Arial,sans-serif" font-size="5" fill="#E53935" text-anchor="middle">Теплота</text>
<!-- A arrow going out (work) -->
<line x1="60" y1="0" x2="155" y2="0" stroke="#2E7D32" stroke-width="2.5"/>
<polygon points="155,0 149,-4 149,4" fill="#2E7D32"/>
<text x="110" y="-10" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle" font-weight="bold">A</text>
<text x="110" y="18" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Работа</text>
</g>
<!-- Main formula -->
<g transform="translate(150,275)">
<rect x="-110" y="-20" width="220" height="40" rx="5" fill="white" stroke="#E53935" stroke-width="2"/>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="13" fill="#E53935" text-anchor="middle" font-weight="bold">deltaU = Q - A</text>
<text x="0" y="14" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Q = deltaU + A — переданное тепло идёт на изм. энергии и работу</text>
</g>
<!-- Conservation note -->
<g transform="translate(400,275)">
<rect x="-70" y="-20" width="140" height="40" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Закон сохранения</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Энергия не возникает</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">и не исчезает</text>
</g>
'''+ftr

# 48: Применение первого закона к изопроцессам
svg48=hdr("Применение первого закона к изопроцессам",48)+f'''
<!-- Table header -->
<g transform="translate(250,78)">
<rect x="-220" y="-16" width="440" height="28" rx="4" fill="{P}" opacity="0.9"/>
<text x="-160" y="2" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle" font-weight="bold">Процесс</text>
<text x="-70" y="2" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle" font-weight="bold">Условие</text>
<text x="25" y="2" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle" font-weight="bold">Q</text>
<text x="100" y="2" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle" font-weight="bold">A</text>
<text x="170" y="2" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle" font-weight="bold">deltaU</text>
</g>
<!-- Row 1: Isothermal -->
<g transform="translate(250,115)">
<rect x="-220" y="-14" width="440" height="28" rx="3" fill="white" stroke="{P}" stroke-width="0.8" opacity="0.9"/>
<text x="-160" y="4" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle" font-weight="bold">Изотермический</text>
<text x="-70" y="4" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">T = const</text>
<text x="25" y="4" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Q = A</text>
<text x="100" y="4" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">A = p*deltaV</text>
<text x="170" y="4" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle">0</text>
</g>
<!-- Row 2: Isobaric -->
<g transform="translate(250,150)">
<rect x="-220" y="-14" width="440" height="28" rx="3" fill="{L}" stroke="{P}" stroke-width="0.8" opacity="0.9"/>
<text x="-160" y="4" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Изобарный</text>
<text x="-70" y="4" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">p = const</text>
<text x="25" y="4" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">deltaU + A</text>
<text x="100" y="4" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">A = p*deltaV</text>
<text x="170" y="4" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">(3/2)*vR*deltaT</text>
</g>
<!-- Row 3: Isochoric -->
<g transform="translate(250,185)">
<rect x="-220" y="-14" width="440" height="28" rx="3" fill="white" stroke="{P}" stroke-width="0.8" opacity="0.9"/>
<text x="-160" y="4" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Изохорный</text>
<text x="-70" y="4" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">V = const</text>
<text x="25" y="4" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Q = deltaU</text>
<text x="100" y="4" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle">0</text>
<text x="170" y="4" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">(3/2)*vR*deltaT</text>
</g>
<!-- Row 4: Adiabatic -->
<g transform="translate(250,220)">
<rect x="-220" y="-14" width="440" height="28" rx="3" fill="{L}" stroke="{P}" stroke-width="0.8" opacity="0.9"/>
<text x="-160" y="4" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">Адиабатный</text>
<text x="-70" y="4" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Q = 0</text>
<text x="25" y="4" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle">0</text>
<text x="100" y="4" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">A = -deltaU</text>
<text x="170" y="4" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle">(3/2)*vR*deltaT</text>
</g>
<!-- Footer note -->
<g transform="translate(250,275)">
<rect x="-200" y="-15" width="400" height="30" rx="5" fill="white" stroke="#FF6F00" stroke-width="1.2"/>
<text x="0" y="2" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle" font-weight="bold">Первый закон: Q = deltaU + A для всех процессов</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Адиабатный процесс — без теплообмена с окружающей средой</text>
</g>
'''+ftr

# 49: Распределение молекул газа по скоростям
svg49=hdr("Распределение молекул газа по скоростям",49)+f'''
<g transform="translate(250,195)">
<!-- Maxwell distribution curve -->
<rect x="-190" y="-95" width="380" height="190" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<!-- Axes -->
<line x1="-155" y1="75" x2="165" y2="75" stroke="#333" stroke-width="1.5"/>
<line x1="-155" y1="75" x2="-155" y2="-75" stroke="#333" stroke-width="1.5"/>
<polygon points="165,75 158,72 158,78" fill="#333"/>
<polygon points="-155,-75 -158,-68 -152,-68" fill="#333"/>
<text x="165" y="90" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">v</text>
<text x="-170" y="-72" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">f(v)</text>
<!-- Maxwell curve T1 -->
<path d="M-140,75 Q-120,70 -100,55 Q-80,30 -55,-20 Q-40,-45 -20,-50 Q0,-48 15,-40 Q40,-20 65,10 Q90,40 120,60 Q140,70 155,75" fill="none" stroke="#E53935" stroke-width="2.5"/>
<!-- Fill under curve -->
<path d="M-140,75 Q-120,70 -100,55 Q-80,30 -55,-20 Q-40,-45 -20,-50 Q0,-48 15,-40 Q40,-20 65,10 Q90,40 120,60 Q140,70 155,75 Z" fill="#E53935" opacity="0.08"/>
<!-- Maxwell curve T2 (higher temperature, shifted right, lower peak) -->
<path d="M-140,75 Q-110,73 -85,65 Q-55,45 -25,5 Q-5,-20 15,-28 Q35,-25 55,-15 Q80,5 105,30 Q130,55 155,70" fill="none" stroke="#2E7D32" stroke-width="2" stroke-dasharray="5,3"/>
<!-- Most probable speed line -->
<line x1="-20" y1="-50" x2="-20" y2="75" stroke="#E53935" stroke-width="1" stroke-dasharray="3,2"/>
<text x="-20" y="86" font-family="Arial,sans-serif" font-size="5" fill="#E53935" text-anchor="middle">vнв</text>
<!-- Average speed line -->
<line x1="15" y1="-40" x2="15" y2="75" stroke="#7B1FA2" stroke-width="1" stroke-dasharray="3,2"/>
<text x="15" y="86" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="middle">vср</text>
<!-- RMS speed line -->
<line x1="50" y1="-5" x2="50" y2="75" stroke="#E65100" stroke-width="1" stroke-dasharray="3,2"/>
<text x="50" y="86" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">vкв</text>
<!-- Legend -->
<text x="-120" y="-65" font-family="Arial,sans-serif" font-size="5" fill="#E53935">— T1</text>
<text x="-120" y="-55" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">--- T2 &gt; T1</text>
</g>
<!-- Speed formulas -->
<g transform="translate(100,305)">
<rect x="-80" y="-10" width="160" height="20" rx="4" fill="white" stroke="#E53935" stroke-width="1"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="5" fill="#E53935" text-anchor="middle">vнв = sqrt(2kT/m0)</text>
</g>
<g transform="translate(280,305)">
<rect x="-75" y="-10" width="150" height="20" rx="4" fill="white" stroke="#7B1FA2" stroke-width="1"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="middle">vср = sqrt(8kT/pi*m0)</text>
</g>
<g transform="translate(435,305)">
<rect x="-70" y="-10" width="140" height="20" rx="4" fill="white" stroke="#E65100" stroke-width="1"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">vкв = sqrt(3kT/m0)</text>
</g>
'''+ftr

# 50: Влажность воздуха
svg50=hdr("Влажность воздуха",50)+f'''
<g transform="translate(120,185)">
<!-- Psychrometer (two thermometers) -->
<!-- Dry thermometer -->
<rect x="-40" y="-55" width="12" height="80" rx="6" fill="white" stroke="#333" stroke-width="1.5"/>
<rect x="-37" y="-15" width="6" height="40" rx="3" fill="#E53935"/>
<circle cx="-34" cy="30" r="9" fill="#E53935" stroke="#333" stroke-width="1.5"/>
<text x="-34" y="-60" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle">Сухой</text>
<!-- Wet thermometer -->
<rect x="20" y="-55" width="12" height="80" rx="6" fill="white" stroke="#333" stroke-width="1.5"/>
<rect x="23" y="5" width="6" height="20" rx="3" fill="#2E7D32"/>
<circle cx="26" cy="30" r="9" fill="#2E7D32" stroke="#333" stroke-width="1.5"/>
<!-- Wick connecting to water -->
<line x1="26" y1="39" x2="26" y2="50" stroke="#2E7D32" stroke-width="2"/>
<path d="M15,50 Q26,55 37,50" fill="none" stroke="#1565C0" stroke-width="1.5"/>
<text x="26" y="65" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">Вода</text>
<text x="26" y="-60" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle">Влажный</text>
<!-- Delta T bracket -->
<line x1="-22" y1="-15" x2="-17" y2="-15" stroke="#7B1FA2" stroke-width="0.8"/>
<line x1="-17" y1="-15" x2="-17" y2="10" stroke="#7B1FA2" stroke-width="0.8"/>
<line x1="17" y1="10" x2="22" y2="10" stroke="#7B1FA2" stroke-width="0.8"/>
<line x1="17" y1="-15" x2="17" y2="10" stroke="#7B1FA2" stroke-width="0.8"/>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="middle">deltaT</text>
<text x="-5" y="80" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Психрометр</text>
</g>
<g transform="translate(370,120)">
<rect x="-110" y="-55" width="220" height="110" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Относительная влажность</text>
<line x1="-95" y1="-33" x2="95" y2="-33" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="11" fill="#E53935" text-anchor="middle" font-weight="bold">phi = rho / rho0 * 100%</text>
<line x1="-95" y1="0" x2="95" y2="0" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">rho — абс. влажность (г/м^3)</text>
<text x="0" y="33" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle">rho0 — плотн. насыщ. пара</text>
<text x="0" y="48" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">phi = p / p0 * 100% (через давление)</text>
</g>
<g transform="translate(370,248)">
<rect x="-110" y="-30" width="220" height="60" rx="5" fill="white" stroke="#E65100" stroke-width="1.2"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">Точка росы</text>
<line x1="-95" y1="-8" x2="95" y2="-8" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Температура, при которой пар становится насыщенным</text>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">rho = rho0(T росы) — абс. влажность</text>
</g>
'''+ftr

svgs={41:svg41,42:svg42,43:svg43,44:svg44,45:svg45,46:svg46,47:svg47,48:svg48,49:svg49,50:svg50}
for num, content in svgs.items():
    path = os.path.join(OUT, f"lesson{num}.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written lesson{num}.svg")
print(f"Done! {len(svgs)} SVG files written")
