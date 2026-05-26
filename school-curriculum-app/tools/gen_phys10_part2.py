#!/usr/bin/env python3
"""Generate Physics grade 10 SVG lesson illustrations (lessons 11-20)."""
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

# 11: Поступательное и вращательное движения
svg11=hdr("Поступательное и вращательное движения",11)+f'''
<g transform="translate(130,185)">
<rect x="-70" y="-55" width="140" height="110" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Поступательное</text>
<line x1="-55" y1="-33" x2="55" y2="-33" stroke="{P}" stroke-width="0.5"/>
<rect x="-30" y="-25" width="25" height="15" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
<text x="-17" y="-14" font-family="Arial,sans-serif" font-size="4" fill="#1565C0" text-anchor="middle">A</text>
<rect x="-20" y="-5" width="25" height="15" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
<text x="-7" y="6" font-family="Arial,sans-serif" font-size="4" fill="#1565C0" text-anchor="middle">A</text>
<rect x="-10" y="15" width="25" height="15" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
<text x="3" y="26" font-family="Arial,sans-serif" font-size="4" fill="#1565C0" text-anchor="middle">A</text>
<line x1="15" y1="-18" x2="25" y2="-18" stroke="#E53935" stroke-width="1.5"/>
<polygon points="25,-18 20,-21 20,-15" fill="#E53935"/>
<line x1="25" y1="2" x2="35" y2="2" stroke="#E53935" stroke-width="1.5"/>
<polygon points="35,2 30,-1 30,5" fill="#E53935"/>
<line x1="35" y1="22" x2="45" y2="22" stroke="#E53935" stroke-width="1.5"/>
<polygon points="45,22 40,19 40,25" fill="#E53935"/>
<text x="0" y="45" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Все точки движутся</text>
<text x="0" y="55" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">одинаково</text>
</g>
<g transform="translate(370,185)">
<rect x="-70" y="-55" width="140" height="110" rx="5" fill="white" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">Вращательное</text>
<line x1="-55" y1="-33" x2="55" y2="-33" stroke="#E65100" stroke-width="0.5"/>
<circle cx="0" cy="10" r="30" fill="none" stroke="#E65100" stroke-width="1.5"/>
<circle cx="0" cy="10" r="3" fill="#E65100"/>
<circle cx="0" cy="-20" r="3" fill="#E53935"/>
<line x1="0" y1="10" x2="0" y2="-17" stroke="#999" stroke-width="0.8" stroke-dasharray="3,2"/>
<path d="M5,-20 L15,-25" stroke="#E53935" stroke-width="1.5"/>
<polygon points="15,-25 9,-25 12,-20" fill="#E53935"/>
<text x="20" y="-25" font-family="Arial,sans-serif" font-size="5" fill="#E53935">v</text>
<text x="0" y="55" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Точки на разных R</text>
<text x="0" y="65" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">имеют разные v</text>
</g>
'''+ib(30,275,440,30,["Поступательное: любая прямая тела остаётся параллельна себе","Вращательное: все точки движутся по окружностям вокруг одной оси"])+ftr

# 12: Сложение движений. Плоское движение
svg12=hdr("Сложение движений. Плоское движение",12)+f'''
<g transform="translate(170,180)">
<!-- Rolling wheel decomposition -->
<circle cx="0" cy="0" r="40" fill="none" stroke="{P}" stroke-width="2"/>
<circle cx="0" cy="0" r="3" fill="{P}"/>
<!-- Velocity at center (translational) -->
<line x1="0" y1="0" x2="40" y2="0" stroke="#2E7D32" stroke-width="2"/>
<polygon points="40,0 34,-3 34,3" fill="#2E7D32"/>
<text x="20" y="-6" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" font-weight="bold">v0</text>
<!-- Velocity at top (2v0) -->
<line x1="0" y1="-40" x2="60" y2="-40" stroke="#E53935" stroke-width="2"/>
<polygon points="60,-40 54,-43 54,-37" fill="#E53935"/>
<text x="30" y="-44" font-family="Arial,sans-serif" font-size="6" fill="#E53935" font-weight="bold">2v0</text>
<!-- Velocity at bottom (0) -->
<text x="0" y="55" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle">v = 0</text>
<!-- Radius lines -->
<line x1="0" y1="0" x2="0" y2="-37" stroke="#999" stroke-width="0.8" stroke-dasharray="3,2"/>
<line x1="0" y1="0" x2="0" y2="37" stroke="#999" stroke-width="0.8" stroke-dasharray="3,2"/>
</g>
<g transform="translate(390,150)">
<rect x="-80" y="-60" width="160" height="120" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-45" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Плоское (вал) движение</text>
<line x1="-65" y1="-38" x2="65" y2="-38" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-22" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">v = vпост + vвращ</text>
<text x="0" y="-8" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Поступательное + вращательное</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#E53935" text-anchor="middle">Верх: vпост + vвращ = 2v0</text>
<text x="0" y="24" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="middle">Низ: vпост - vвращ = 0</text>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Центр: только vпост = v0</text>
<text x="0" y="56" font-family="Arial,sans-serif" font-size="5" fill="#FF6F00" text-anchor="middle">Мгновенная ось — в точке касания</text>
</g>
'''+ftr

# 13: Обгон
svg13=hdr("Обгон",13)+f'''
<g transform="translate(250,180)">
<!-- Two objects on parallel tracks -->
<line x1="-120" y1="30" x2="120" y2="30" stroke="#CCC" stroke-width="1"/>
<line x1="-120" y1="-30" x2="120" y2="-30" stroke="#CCC" stroke-width="1"/>
<!-- Slow object -->
<rect x="-40" y="-42" width="30" height="24" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<text x="-25" y="-27" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">1</text>
<line x1="-10" y1="-30" x2="20" y2="-30" stroke="#1565C0" stroke-width="1.5"/>
<polygon points="20,-30 14,-33 14,-27" fill="#1565C0"/>
<text x="5" y="-36" font-family="Arial,sans-serif" font-size="5" fill="#1565C0">v1</text>
<!-- Fast object -->
<rect x="-70" y="18" width="30" height="24" rx="3" fill="#FFF3E0" stroke="#E65100" stroke-width="1.5"/>
<text x="-55" y="33" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">2</text>
<line x1="-40" y1="30" x2="20" y2="30" stroke="#E65100" stroke-width="1.5"/>
<polygon points="20,30 14,27 14,33" fill="#E65100"/>
<text x="-10" y="24" font-family="Arial,sans-serif" font-size="5" fill="#E65100">v2 &gt; v1</text>
</g>
<g transform="translate(370,130)">
<rect x="-80" y="-45" width="160" height="90" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-30" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Условие обгона</text>
<line x1="-65" y1="-22" x2="65" y2="-22" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-7" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">v2 &gt; v1</text>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">x2(t) = x1(t)</text>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">tобг = L / (v2 - v1)</text>
<text x="0" y="36" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">L — расстояние между телами</text>
</g>
<g transform="translate(370,250)">
<rect x="-70" y="-25" width="140" height="50" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Относительная скорость</text>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">vотн = v2 - v1</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">при движении в одном направлении</text>
</g>
'''+ftr

# 14: Решение задач кинематики в общем виде
svg14=hdr("Решение задач кинематики в общем виде",14)+f'''
<g transform="translate(250,105)">
<rect x="-140" y="-40" width="280" height="80" rx="8" fill="white" stroke="{P}" stroke-width="2"/>
<text x="0" y="-22" font-family="Arial,sans-serif" font-size="8" fill="{P}" text-anchor="middle" font-weight="bold">Общий подход к решению задач кинематики</text>
<line x1="-125" y1="-14" x2="125" y2="-14" stroke="{P}" stroke-width="0.5"/>
<text x="-70" y="2" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">1. Выбрать СО, записать данные</text>
<text x="70" y="2" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">2. Записать уравнения в проекциях</text>
<text x="-70" y="16" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">3. Решить систему уравнений</text>
<text x="70" y="16" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">4. Получить ответ в общем виде</text>
<text x="0" y="34" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">5. Проверить размерность и проанализировать ответ!</text>
</g>
<g transform="translate(150,230)">
<rect x="-90" y="-40" width="180" height="80" rx="5" fill="white" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">Анализ ответа</text>
<line x1="-75" y1="-18" x2="75" y2="-18" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Предельные случаи (t=0, t-&gt;inf)</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Размерность величин</text>
<text x="0" y="23" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Числовой порядок</text>
<text x="0" y="36" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Физический смысл</text>
</g>
<g transform="translate(390,230)">
<rect x="-90" y="-40" width="180" height="80" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Общий вид</text>
<line x1="-75" y1="-18" x2="75" y2="-18" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Ответ через данные задачи</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Не подставлять числа сразу</text>
<text x="0" y="23" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Позволяет анализировать</text>
<text x="0" y="36" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">зависимость от параметров</text>
</g>
'''+ftr

# 15: Сила. Измерение сил
svg15=hdr("Сила. Измерение сил",15)+f'''
<g transform="translate(130,180)">
<!-- Dynamometer -->
<rect x="-20" y="-70" width="40" height="120" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-55" font-family="Arial,sans-serif" font-size="6" fill="{P}" text-anchor="middle" font-weight="bold">Динамо-</text>
<text x="0" y="-45" font-family="Arial,sans-serif" font-size="6" fill="{P}" text-anchor="middle" font-weight="bold">метр</text>
<!-- Scale marks -->
<line x1="-15" y1="-30" x2="-5" y2="-30" stroke="#333" stroke-width="0.8"/>
<text x="5" y="-27" font-family="Arial,sans-serif" font-size="5" fill="#333">0</text>
<line x1="-15" y1="-10" x2="-5" y2="-10" stroke="#333" stroke-width="0.8"/>
<text x="5" y="-7" font-family="Arial,sans-serif" font-size="5" fill="#333">2</text>
<line x1="-15" y1="10" x2="-5" y2="10" stroke="#333" stroke-width="0.8"/>
<text x="5" y="13" font-family="Arial,sans-serif" font-size="5" fill="#333">4</text>
<line x1="-15" y1="30" x2="-5" y2="30" stroke="#333" stroke-width="0.8"/>
<text x="5" y="33" font-family="Arial,sans-serif" font-size="5" fill="#333">6 Н</text>
<!-- Spring inside -->
<line x1="0" y1="-40" x2="0" y2="-25" stroke="#999" stroke-width="1"/>
<path d="M0,-25 L5,-20 L-5,-12 L5,-5 L-5,3 L5,10 L-5,17 L5,24 L0,28" stroke="#E53935" stroke-width="1.5" fill="none"/>
<!-- Hook -->
<line x1="0" y1="28" x2="0" y2="50" stroke="#333" stroke-width="1"/>
<path d="M0,50 Q10,55 0,60" stroke="#333" stroke-width="1.5" fill="none"/>
</g>
<g transform="translate(350,130)">
<rect x="-90" y="-55" width="180" height="110" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Сила — векторная величина</text>
<line x1="-75" y1="-33" x2="75" y2="-33" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Характеризуется:</text>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="5" fill="#E53935" text-anchor="middle">1. Модулем |F|</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">2. Направлением</text>
<text x="0" y="27" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">3. Точкой приложения</text>
<text x="0" y="45" font-family="Arial,sans-serif" font-size="5" fill="#FF6F00" text-anchor="middle">Единица: 1 Ньютон (Н) = кг*м/с^2</text>
</g>
<g transform="translate(350,255)">
<rect x="-70" y="-25" width="140" height="50" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Виды сил в механике</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Тяжести, упругости, трения,</text>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">тяготения, реакции опоры</text>
</g>
'''+ftr

# 16: Инертность. Масса. Второй закон Ньютона
svg16=hdr("Инертность. Масса. Второй закон Ньютона",16)+f'''
<g transform="translate(250,175)">
<!-- F = ma central diagram -->
<circle cx="0" cy="0" r="60" fill="{P}" opacity="0.05" stroke="{P}" stroke-width="2"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="18" fill="{P}" text-anchor="middle" font-weight="bold">F = ma</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Второй закон Ньютона</text>
</g>
<g transform="translate(80,110)">
<rect x="-50" y="-25" width="100" height="50" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle" font-weight="bold">F — сила</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Равнодействующая</text>
<text x="0" y="16" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">всех сил (Н)</text>
</g>
<g transform="translate(420,110)">
<rect x="-50" y="-25" width="100" height="50" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">m — масса</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Мера инертности</text>
<text x="0" y="16" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">(кг)</text>
</g>
<g transform="translate(80,250)">
<rect x="-50" y="-25" width="100" height="50" rx="5" fill="white" stroke="#FF6F00" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle" font-weight="bold">a — ускорение</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Быстрота изменения</text>
<text x="0" y="16" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">скорости (м/с^2)</text>
</g>
<g transform="translate(420,250)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Инертность</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Свойство тела</text>
<text x="0" y="16" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">сопротивляться изменению v</text>
</g>
'''+ftr

# 17: Взаимодействие тел. Третий закон Ньютона
svg17=hdr("Взаимодействие тел. Третий закон Ньютона",17)+f'''
<g transform="translate(250,175)">
<!-- Two blocks pushing each other -->
<rect x="-80" y="-20" width="50" height="40" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<text x="-55" y="5" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle">1</text>
<rect x="30" y="-20" width="50" height="40" rx="3" fill="#FFF3E0" stroke="#E65100" stroke-width="1.5"/>
<text x="55" y="5" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle">2</text>
<!-- Force arrows -->
<line x1="-25" y1="0" x2="-40" y2="0" stroke="#E53935" stroke-width="2.5"/>
<polygon points="-40,0 -34,-3 -34,3" fill="#E53935"/>
<text x="-40" y="-8" font-family="Arial,sans-serif" font-size="6" fill="#E53935" font-weight="bold">F12</text>
<line x1="35" y1="0" x2="50" y2="0" stroke="#2E7D32" stroke-width="2.5"/>
<polygon points="50,0 44,-3 44,3" fill="#2E7D32"/>
<text x="50" y="-8" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" font-weight="bold">F21</text>
<!-- Equal sign -->
<text x="5" y="5" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle">=</text>
</g>
<g transform="translate(250,260)">
<rect x="-120" y="-25" width="240" height="50" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-8" font-family="Arial,sans-serif" font-size="8" fill="{P}" text-anchor="middle" font-weight="bold">Третий закон Ньютона</text>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">F12 = -F21</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Действие = противодействию | Силы одной природы</text>
</g>
<g transform="translate(120,110)">
<rect x="-70" y="-25" width="140" height="50" rx="5" fill="white" stroke="#C62828" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">Силы приложены</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">к РАЗНЫМ телам!</text>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Не компенсируют друг друга</text>
</g>
<g transform="translate(400,110)">
<rect x="-70" y="-25" width="140" height="50" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Одна природа</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Обе силы гравитационные,</text>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">или обе упругости и т.д.</text>
</g>
'''+ftr

# 18: Деформации. Сила упругости. Закон Гука
svg18=hdr("Деформации. Сила упругости. Закон Гука",18)+f'''
<g transform="translate(150,185)">
<!-- Spring with force -->
<rect x="-60" y="-10" width="20" height="20" rx="2" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
<!-- Wall -->
<line x1="-60" y1="-25" x2="-60" y2="25" stroke="#333" stroke-width="3"/>
<line x1="-65" y1="-25" x2="-65" y2="25" stroke="#333" stroke-width="1"/>
<!-- Spring coils -->
<path d="M-40,0 L-32,-12 L-16,12 L0,-12 L16,12 L32,-12 L40,0" stroke="#E53935" stroke-width="2" fill="none"/>
<!-- Arrow for F -->
<line x1="42" y1="0" x2="75" y2="0" stroke="#2E7D32" stroke-width="2.5"/>
<polygon points="75,0 69,-3 69,3" fill="#2E7D32"/>
<text x="60" y="-8" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" font-weight="bold">F</text>
<!-- x mark -->
<line x1="42" y1="10" x2="75" y2="10" stroke="#7B1FA2" stroke-width="0.8" stroke-dasharray="2,2"/>
<text x="58" y="20" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2">x</text>
</g>
<g transform="translate(380,140)">
<rect x="-80" y="-55" width="160" height="110" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Закон Гука</text>
<line x1="-65" y1="-33" x2="65" y2="-33" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle" font-weight="bold">F = -kx</text>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">k — жёсткость (Н/м)</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">x — удлинение (м)</text>
<line x1="-65" y1="18" x2="65" y2="18" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="33" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Деформации:</text>
<text x="0" y="46" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Упругие / Пластические</text>
</g>
<g transform="translate(380,265)">
<rect x="-60" y="-18" width="120" height="36" rx="5" fill="white" stroke="#FF6F00" stroke-width="1.2"/>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle" font-weight="bold">Виды деформаций</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Растяжение, сжатие, сдвиг, кручение, изгиб</text>
</g>
'''+ftr

# 19: Сила трения
svg19=hdr("Сила трения",19)+f'''
<g transform="translate(170,185)">
<!-- Block on surface -->
<line x1="-80" y1="25" x2="80" y2="25" stroke="#333" stroke-width="2"/>
<!-- Hatching for surface -->
<line x1="-80" y1="25" x2="-70" y2="35" stroke="#999" stroke-width="0.5"/>
<line x1="-60" y1="25" x2="-50" y2="35" stroke="#999" stroke-width="0.5"/>
<line x1="-40" y1="25" x2="-30" y2="35" stroke="#999" stroke-width="0.5"/>
<line x1="-20" y1="25" x2="-10" y2="35" stroke="#999" stroke-width="0.5"/>
<line x1="0" y1="25" x2="10" y2="35" stroke="#999" stroke-width="0.5"/>
<line x1="20" y1="25" x2="30" y2="35" stroke="#999" stroke-width="0.5"/>
<line x1="40" y1="25" x2="50" y2="35" stroke="#999" stroke-width="0.5"/>
<line x1="60" y1="25" x2="70" y2="35" stroke="#999" stroke-width="0.5"/>
<!-- Block -->
<rect x="-25" y="-10" width="50" height="35" rx="2" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">m</text>
<!-- Friction force -->
<line x1="-25" y1="15" x2="-55" y2="15" stroke="#E53935" stroke-width="2.5"/>
<polygon points="-55,15 -49,12 -49,18" fill="#E53935"/>
<text x="-45" y="8" font-family="Arial,sans-serif" font-size="6" fill="#E53935" font-weight="bold">Fтр</text>
<!-- Applied force -->
<line x1="25" y1="5" x2="55" y2="5" stroke="#2E7D32" stroke-width="2.5"/>
<polygon points="55,5 49,2 49,8" fill="#2E7D32"/>
<text x="45" y="-2" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" font-weight="bold">F</text>
<!-- Normal force -->
<line x1="0" y1="-10" x2="0" y2="-35" stroke="#7B1FA2" stroke-width="1.5"/>
<polygon points="0,-35 -3,-29 3,-29" fill="#7B1FA2"/>
<text x="8" y="-25" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2">N</text>
<!-- Weight -->
<line x1="0" y1="25" x2="0" y2="50" stroke="#FF6F00" stroke-width="1.5"/>
<polygon points="0,50 -3,44 3,44" fill="#FF6F00"/>
<text x="8" y="45" font-family="Arial,sans-serif" font-size="5" fill="#FF6F00">mg</text>
</g>
<g transform="translate(390,135)">
<rect x="-80" y="-60" width="160" height="120" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-45" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Формула</text>
<line x1="-65" y1="-38" x2="65" y2="-38" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-22" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle" font-weight="bold">Fтр = mu*N</text>
<text x="0" y="-7" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">mu — коэффициент трения</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">N — сила нормальной реакции</text>
<line x1="-65" y1="15" x2="65" y2="15" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Трение покоя</text>
<text x="0" y="43" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Fтр.пок &lt;= mu0*N</text>
<text x="0" y="55" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">mu0 &gt; mu (скольжения)</text>
</g>
<g transform="translate(390,265)">
<rect x="-60" y="-15" width="120" height="30" rx="5" fill="white" stroke="#C62828" stroke-width="1"/>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">Трение: покоя, скольжения, качения</text>
</g>
'''+ftr

# 20: Движение тела под действием нескольких сил
svg20=hdr("Движение под действием нескольких сил",20)+f'''
<g transform="translate(250,180)">
<!-- Free body diagram -->
<rect x="-25" y="-15" width="50" height="30" rx="2" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle">m</text>
<!-- All forces -->
<line x1="0" y1="-15" x2="0" y2="-50" stroke="#7B1FA2" stroke-width="2"/>
<polygon points="0,-50 -3,-44 3,-44" fill="#7B1FA2"/>
<text x="10" y="-40" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" font-weight="bold">N</text>
<line x1="0" y1="15" x2="0" y2="50" stroke="#FF6F00" stroke-width="2"/>
<polygon points="0,50 -3,44 3,44" fill="#FF6F00"/>
<text x="10" y="45" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" font-weight="bold">mg</text>
<line x1="25" y1="0" x2="60" y2="0" stroke="#2E7D32" stroke-width="2"/>
<polygon points="60,0 54,-3 54,3" fill="#2E7D32"/>
<text x="50" y="-8" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" font-weight="bold">F</text>
<line x1="-25" y1="0" x2="-55" y2="0" stroke="#E53935" stroke-width="2"/>
<polygon points="-55,0 -49,-3 -49,3" fill="#E53935"/>
<text x="-45" y="-8" font-family="Arial,sans-serif" font-size="6" fill="#E53935" font-weight="bold">Fтр</text>
</g>
<g transform="translate(100,105)">
<rect x="-60" y="-30" width="120" height="60" rx="5" fill="white" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">Алгоритм</text>
<line x1="-45" y1="-8" x2="45" y2="-8" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">1. Изобразить все силы</text>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">2. Записать 2-й закон в проекциях</text>
</g>
<g transform="translate(420,105)">
<rect x="-60" y="-30" width="120" height="60" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Проекции</text>
<line x1="-45" y1="-8" x2="45" y2="-8" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Ox: F - Fтр = ma</text>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Oy: N - mg = 0</text>
</g>
<g transform="translate(250,275)">
<rect x="-120" y="-18" width="240" height="36" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Равнодействующая</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Fравн = ma — векторная сумма всех сил, действующих на тело</text>
</g>
'''+ftr

svgs={11:svg11,12:svg12,13:svg13,14:svg14,15:svg15,16:svg16,17:svg17,18:svg18,19:svg19,20:svg20}
for num, content in svgs.items():
    path = os.path.join(OUT, f"lesson{num}.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written lesson{num}.svg")
print(f"Done! {len(svgs)} SVG files written")
