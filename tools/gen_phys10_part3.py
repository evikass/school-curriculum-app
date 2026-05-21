#!/usr/bin/env python3
"""Generate Physics grade 10 SVG lesson illustrations (lessons 21-30)."""
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

# 21: Движение взаимодействующих тел
svg21=hdr("Движение взаимодействующих тел",21)+f'''
<g transform="translate(250,170)">
<!-- Two blocks connected by rope -->
<rect x="-80" y="-12" width="45" height="30" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<text x="-57" y="8" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">m1</text>
<rect x="35" y="-12" width="45" height="30" rx="3" fill="#FFF3E0" stroke="#E65100" stroke-width="1.5"/>
<text x="57" y="8" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">m2</text>
<!-- Rope -->
<line x1="-35" y1="3" x2="35" y2="3" stroke="#795548" stroke-width="1.5"/>
<!-- Tension forces -->
<line x1="-35" y1="3" x2="-50" y2="3" stroke="#C62828" stroke-width="1.5"/>
<polygon points="-50,3 -44,0 -44,6" fill="#C62828"/>
<text x="-55" y="-3" font-family="Arial,sans-serif" font-size="5" fill="#C62828">T</text>
<line x1="35" y1="3" x2="50" y2="3" stroke="#C62828" stroke-width="1.5"/>
<polygon points="50,3 44,0 44,6" fill="#C62828"/>
<text x="55" y="-3" font-family="Arial,sans-serif" font-size="5" fill="#C62828">T</text>
<!-- Applied force -->
<line x1="80" y1="3" x2="110" y2="3" stroke="#2E7D32" stroke-width="2"/>
<polygon points="110,3 104,0 104,6" fill="#2E7D32"/>
<text x="100" y="-4" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">F</text>
</g>
<g transform="translate(250,250)">
<rect x="-140" y="-30" width="280" height="60" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Уравнения движения системы</text>
<line x1="-125" y1="-8" x2="125" y2="-8" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Для m1: T = m1*a | Для m2: F - T = m2*a</text>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Общее: a = F / (m1 + m2), T = m1*F / (m1 + m2)</text>
</g>
<g transform="translate(120,110)">
<rect x="-70" y="-25" width="140" height="50" rx="5" fill="white" stroke="#E65100" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">Нить невесома</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">T1 = T2 = T</text>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">одинаковое ускорение a</text>
</g>
'''+ftr

# 22: Закон всемирного тяготения
svg22=hdr("Закон всемирного тяготения",22)+f'''
<g transform="translate(170,180)">
<!-- Two masses attracting -->
<circle cx="-50" cy="0" r="25" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<text x="-50" y="4" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">m1</text>
<circle cx="50" cy="0" r="25" fill="#FFF3E0" stroke="#E65100" stroke-width="1.5"/>
<text x="50" y="4" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">m2</text>
<!-- Attraction forces -->
<line x1="-25" y1="0" x2="-40" y2="0" stroke="#E53935" stroke-width="2"/>
<polygon points="-40,0 -34,-3 -34,3" fill="#E53935"/>
<line x1="25" y1="0" x2="40" y2="0" stroke="#E53935" stroke-width="2"/>
<polygon points="40,0 34,-3 34,3" fill="#E53935"/>
<!-- r distance -->
<line x1="-50" y1="35" x2="50" y2="35" stroke="#7B1FA2" stroke-width="1"/>
<text x="0" y="48" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle">r</text>
</g>
<g transform="translate(400,140)">
<rect x="-80" y="-55" width="160" height="110" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Закон тяготения</text>
<line x1="-65" y1="-33" x2="65" y2="-33" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle" font-weight="bold">F = G*m1*m2 / r^2</text>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">G = 6.67*10^-11 Н*м^2/кг^2</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Обратно пропорциональна r^2</text>
<text x="0" y="27" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Прямо пропорциональна m1*m2</text>
<text x="0" y="45" font-family="Arial,sans-serif" font-size="5" fill="#FF6F00" text-anchor="middle">Для материальных точек</text>
</g>
<g transform="translate(400,265)">
<rect x="-60" y="-18" width="120" height="36" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Гравитационная постоянная</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Опыт Кавендиша (1798)</text>
</g>
'''+ftr

# 23: Сила тяжести. Вес. Невесомость
svg23=hdr("Сила тяжести. Вес. Невесомость",23)+f'''
<g transform="translate(120,185)">
<!-- Elevator diagram -->
<rect x="-40" y="-60" width="80" height="100" rx="3" fill="white" stroke="#333" stroke-width="1.5"/>
<text x="0" y="-45" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Лифт</text>
<!-- Person -->
<circle cx="0" cy="-20" r="8" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
<rect x="-8" y="-12" width="16" height="25" rx="2" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
<!-- Weight arrow up -->
<line x1="15" y1="0" x2="15" y2="-25" stroke="#2E7D32" stroke-width="1.5"/>
<polygon points="15,-25 12,-19 18,-19" fill="#2E7D32"/>
<text x="25" y="-15" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">P</text>
<!-- mg arrow down -->
<line x1="-15" y1="0" x2="-15" y2="25" stroke="#E53935" stroke-width="1.5"/>
<polygon points="-15,25 -18,19 -12,19" fill="#E53935"/>
<text x="-28" y="18" font-family="Arial,sans-serif" font-size="5" fill="#E53935">mg</text>
<!-- Acceleration arrow -->
<line x1="0" y1="45" x2="0" y2="60" stroke="#7B1FA2" stroke-width="1.5"/>
<polygon points="0,60 -3,54 3,54" fill="#7B1FA2"/>
<text x="8" y="55" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2">a</text>
</g>
<g transform="translate(370,135)">
<rect x="-85" y="-65" width="170" height="130" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-50" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Вес тела в лифте</text>
<line x1="-70" y1="-43" x2="70" y2="-43" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-28" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Покой: P = mg</text>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Вверх с a: P = m(g + a)</text>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="5" fill="#E53935" text-anchor="middle">Вниз с a: P = m(g - a)</text>
<line x1="-70" y1="8" x2="70" y2="8" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="23" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Невесомость</text>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">a = g: P = 0</text>
<text x="0" y="52" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Свободное падение</text>
</g>
<g transform="translate(370,270)">
<rect x="-70" y="-18" width="140" height="36" rx="5" fill="white" stroke="#FF6F00" stroke-width="1.2"/>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle" font-weight="bold">Сила тяжести</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">F = mg, g = G*M/R^2</text>
</g>
'''+ftr

# 24: Движение планет и спутников
svg24=hdr("Движение планет и искусственных спутников",24)+f'''
<g transform="translate(170,180)">
<!-- Earth -->
<circle cx="0" cy="0" r="40" fill="#E3F2FD" stroke="#1565C0" stroke-width="2"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">M</text>
<!-- Orbit -->
<circle cx="0" cy="0" r="70" fill="none" stroke="#999" stroke-width="0.8" stroke-dasharray="4,2"/>
<!-- Satellite -->
<circle cx="0" cy="-70" r="6" fill="#E53935" stroke="#C62828" stroke-width="1"/>
<text x="12" y="-68" font-family="Arial,sans-serif" font-size="5" fill="#C62828">m</text>
<!-- Velocity -->
<line x1="6" y1="-70" x2="30" y2="-70" stroke="#2E7D32" stroke-width="1.5"/>
<polygon points="30,-70 24,-73 24,-67" fill="#2E7D32"/>
<text x="22" y="-75" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">v</text>
<!-- Gravity -->
<line x1="0" y1="-64" x2="0" y2="-44" stroke="#E53935" stroke-width="1.5"/>
<polygon points="0,-44 -3,-50 3,-50" fill="#E53935"/>
<!-- R+h label -->
<line x1="0" y1="-40" x2="0" y2="-70" stroke="#7B1FA2" stroke-width="0.5" stroke-dasharray="2,2"/>
<text x="15" y="-55" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2">R+h</text>
</g>
<g transform="translate(400,140)">
<rect x="-80" y="-60" width="160" height="120" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-45" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Космические скорости</text>
<line x1="-65" y1="-38" x2="65" y2="-38" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-22" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">v1 = sqrt(g*R) = 7.9 км/с</text>
<text x="0" y="-8" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">v2 = sqrt(2*g*R) = 11.2 км/с</text>
<text x="0" y="6" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="middle">v3 = 16.7 км/с</text>
<line x1="-65" y1="15" x2="65" y2="15" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">v1: круговая орбита</text>
<text x="0" y="43" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">v2: парабола (покидает Землю)</text>
<text x="0" y="56" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">v3: покидает Солн. систему</text>
</g>
'''+ftr

# 25: Динамика движения по окружности
svg25=hdr("Динамика движения по окружности",25)+f'''
<g transform="translate(160,185)">
<!-- Car on circular track -->
<path d="M-60,40 A70,70 0 0,1 60,40" fill="none" stroke="#333" stroke-width="2"/>
<!-- Car -->
<rect x="-10" y="-15" width="25" height="12" rx="2" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
<text x="3" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">m</text>
<!-- Centripetal force -->
<line x1="3" y1="0" x2="3" y2="30" stroke="#E53935" stroke-width="2"/>
<polygon points="3,30 0,24 6,24" fill="#E53935"/>
<text x="15" y="20" font-family="Arial,sans-serif" font-size="5" fill="#E53935">Fцс</text>
<!-- Velocity -->
<line x1="15" y1="-10" x2="40" y2="-15" stroke="#2E7D32" stroke-width="1.5"/>
<polygon points="40,-15 34,-17 35,-11" fill="#2E7D32"/>
<text x="35" y="-20" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">v</text>
<!-- Center -->
<circle cx="0" cy="60" r="2" fill="#333"/>
<text x="0" y="72" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle">O</text>
</g>
<g transform="translate(400,150)">
<rect x="-80" y="-60" width="160" height="120" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-45" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Равнодействующая</text>
<line x1="-65" y1="-38" x2="65" y2="-38" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-22" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Fравн = m*aцс</text>
<text x="0" y="-8" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Fравн = m*v^2/R</text>
<line x1="-65" y1="2" x2="65" y2="2" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="5" fill="#E53935" text-anchor="middle">Конический маятник</text>
<text x="0" y="32" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Автомобиль на повороте</text>
<text x="0" y="47" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="middle">Самолёт в вираже</text>
</g>
'''+ftr

# 26: Импульс. Изменение импульса
svg26=hdr("Импульс. Изменение импульса",26)+f'''
<g transform="translate(250,175)">
<circle cx="0" cy="0" r="60" fill="{P}" opacity="0.05" stroke="{P}" stroke-width="2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="14" fill="{P}" text-anchor="middle" font-weight="bold">p = mv</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Импульс тела</text>
</g>
<g transform="translate(90,115)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle" font-weight="bold">Импульс силы</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">F*t = delta(p)</text>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Изменение импульса</text>
</g>
<g transform="translate(420,115)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Единица</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">кг*м/с</text>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Н*с</text>
</g>
<g transform="translate(90,260)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#FF6F00" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle" font-weight="bold">Вектор</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">p сонаправлен с v</text>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Имеет направление</text>
</g>
<g transform="translate(420,260)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Теорема</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">F*t = p - p0</text>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Импульс силы = изм. импульса</text>
</g>
'''+ftr

# 27: Закон сохранения импульса
svg27=hdr("Закон сохранения импульса",27)+f'''
<g transform="translate(250,175)">
<!-- Before collision -->
<circle cx="-60" cy="-30" r="15" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<text x="-60" y="-26" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">m1</text>
<line x1="-45" y1="-30" x2="-20" y2="-30" stroke="#1565C0" stroke-width="1.5"/>
<polygon points="-20,-30 -26,-33 -26,-27" fill="#1565C0"/>
<text x="-35" y="-36" font-family="Arial,sans-serif" font-size="5" fill="#1565C0">v1</text>
<circle cx="60" cy="-30" r="15" fill="#FFF3E0" stroke="#E65100" stroke-width="1.5"/>
<text x="60" y="-26" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">m2</text>
<line x1="45" y1="-30" x2="20" y2="-30" stroke="#E65100" stroke-width="1.5"/>
<polygon points="20,-30 26,-33 26,-27" fill="#E65100"/>
<text x="35" y="-36" font-family="Arial,sans-serif" font-size="5" fill="#E65100">v2</text>
<text x="0" y="-50" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">До столкновения</text>
<!-- After collision -->
<circle cx="-50" cy="30" r="15" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<text x="-50" y="34" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">m1</text>
<circle cx="50" cy="30" r="15" fill="#FFF3E0" stroke="#E65100" stroke-width="1.5"/>
<text x="50" y="34" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">m2</text>
<line x1="-35" y1="30" x2="-15" y2="30" stroke="#1565C0" stroke-width="1.5"/>
<polygon points="-15,30 -21,27 -21,33" fill="#1565C0"/>
<line x1="65" y1="30" x2="85" y2="30" stroke="#E65100" stroke-width="1.5"/>
<polygon points="85,30 79,27 79,33" fill="#E65100"/>
<text x="0" y="55" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">После</text>
</g>
<g transform="translate(400,120)">
<rect x="-70" y="-35" width="140" height="70" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="6" fill="{P}" text-anchor="middle" font-weight="bold">Закон сохранения</text>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle">m1*v1 + m2*v2 =</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle">m1*v1 + m2*v2</text>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Fвнешн = 0</text>
</g>
'''+ftr

# 28: Центр масс
svg28=hdr("Центр масс. Теорема о движении центра масс",28)+f'''
<g transform="translate(150,180)">
<!-- Two masses on a rod -->
<circle cx="-60" cy="0" r="15" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<text x="-60" y="4" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">m1</text>
<circle cx="60" cy="0" r="10" fill="#FFF3E0" stroke="#E65100" stroke-width="1.5"/>
<text x="60" y="4" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">m2</text>
<!-- Rod -->
<line x1="-45" y1="0" x2="50" y2="0" stroke="#333" stroke-width="2"/>
<!-- Center of mass -->
<circle cx="-15" cy="0" r="4" fill="#E53935" stroke="#C62828" stroke-width="1.5"/>
<text x="-15" y="-10" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">ЦМ</text>
</g>
<g transform="translate(400,140)">
<rect x="-80" y="-55" width="160" height="110" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Координата ЦМ</text>
<line x1="-65" y1="-33" x2="65" y2="-33" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">xцм = (m1*x1+m2*x2)</text>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">/ (m1+m2)</text>
<line x1="-65" y1="10" x2="65" y2="10" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="25" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle" font-weight="bold">Теорема</text>
<text x="0" y="40" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Fвнешн = M*aцм</text>
<text x="0" y="52" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">ЦМ движется как материальная точка</text>
</g>
'''+ftr

# 29: Работа силы. Мощность
svg29=hdr("Работа силы. Мощность",29)+f'''
<g transform="translate(160,185)">
<!-- Force at angle -->
<rect x="-20" y="-12" width="40" height="30" rx="2" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">m</text>
<!-- Displacement -->
<line x1="20" y1="3" x2="80" y2="3" stroke="#2E7D32" stroke-width="2"/>
<polygon points="80,3 74,0 74,6" fill="#2E7D32"/>
<text x="55" y="-3" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" font-weight="bold">S</text>
<!-- Force at angle -->
<line x1="20" y1="3" x2="60" y2="-30" stroke="#E53935" stroke-width="2"/>
<polygon points="60,-30 52,-26 56,-34" fill="#E53935"/>
<text x="50" y="-20" font-family="Arial,sans-serif" font-size="6" fill="#E53935" font-weight="bold">F</text>
<!-- Angle -->
<path d="M35,3 A15,15 0 0,1 32,-10" stroke="#7B1FA2" stroke-width="1.2" fill="none"/>
<text x="40" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2">a</text>
</g>
<g transform="translate(400,140)">
<rect x="-80" y="-55" width="160" height="110" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Формулы</text>
<line x1="-65" y1="-33" x2="65" y2="-33" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle">A = F*S*cos(a)</text>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">a=0: A = F*S (макс)</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">a=90: A = 0</text>
<text x="0" y="23" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">a&gt;90: A &lt; 0</text>
<line x1="-65" y1="32" x2="65" y2="32" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="47" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">N = A/t = F*v</text>
<text x="0" y="60" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Ватт (Вт) = Дж/с</text>
</g>
<g transform="translate(250,275)">
<rect x="-80" y="-15" width="160" height="30" rx="5" fill="white" stroke="#FF6F00" stroke-width="1.2"/>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle" font-weight="bold">Работа: Джоуль (Дж) = Н*м</text>
</g>
'''+ftr

# 30: Кинетическая энергия
svg30=hdr("Кинетическая энергия",30)+f'''
<g transform="translate(250,175)">
<circle cx="0" cy="0" r="60" fill="{P}" opacity="0.05" stroke="{P}" stroke-width="2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="14" fill="{P}" text-anchor="middle" font-weight="bold">Ek = mv^2/2</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Кинетическая энергия</text>
</g>
<g transform="translate(90,115)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle" font-weight="bold">Теорема</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">A = Ek2 - Ek1</text>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Работа = изм. кин. энергии</text>
</g>
<g transform="translate(420,115)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Единица</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Джоуль (Дж)</text>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">1 Дж = 1 кг*м^2/с^2</text>
</g>
<g transform="translate(90,260)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#FF6F00" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle" font-weight="bold">Свойства</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Ek &gt;= 0 всегда</text>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Зависит от СО</text>
</g>
<g transform="translate(420,260)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Связь с работой</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">A &gt; 0: Ek растёт</text>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">A &lt; 0: Ek убывает</text>
</g>
'''+ftr

svgs={21:svg21,22:svg22,23:svg23,24:svg24,25:svg25,26:svg26,27:svg27,28:svg28,29:svg29,30:svg30}
for num, content in svgs.items():
    path = os.path.join(OUT, f"lesson{num}.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written lesson{num}.svg")
print(f"Done! {len(svgs)} SVG files written")
