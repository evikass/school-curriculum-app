#!/usr/bin/env python3
"""Generate Physics grade 10 SVG lesson illustrations (lessons 1-10)."""
import os
OUT = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade10/physics"
os.makedirs(OUT, exist_ok=True)
P = "#1565C0"; L = "#E3F2FD"; M = "#BBDEFB"; A = "#0D47A1"

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

titles = {
1:"Классическая механика Ньютона",
2:"Положение тела. Системы отсчёта",
3:"Перемещение. Путь",
4:"Скорость",
5:"Равномерное прямолинейное движение",
6:"Решение задач кинематики",
7:"Сложение движений",
8:"Ускорение. Равноускоренное движение",
9:"Решение задач равноускоренного движения",
10:"Равномерное движение по окружности"
}

# 1
svgs={}
svgs[1]=hdr(titles[1],1)+f'''
<g transform="translate(250,180)">
<circle cx="0" cy="0" r="65" fill="{P}" opacity="0.07" stroke="{P}" stroke-width="2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="12" fill="{P}" text-anchor="middle" font-weight="bold">Механика</text>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Ньютона</text>
</g>
<g transform="translate(90,110)">
<rect x="-50" y="-20" width="100" height="40" rx="5" fill="white" stroke="#E65100" stroke-width="1.2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">Кинематика</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Движение без причин</text>
</g>
<g transform="translate(210,90)">
<rect x="-50" y="-20" width="100" height="40" rx="5" fill="white" stroke="#C62828" stroke-width="1.2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">Динамика</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Причины движения</text>
</g>
<g transform="translate(330,90)">
<rect x="-55" y="-20" width="110" height="40" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Законы сохранения</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Импульс, энергия</text>
</g>
<g transform="translate(430,110)">
<rect x="-45" y="-20" width="90" height="40" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Статика</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Равновесие</text>
</g>
<g transform="translate(120,260)">
<rect x="-70" y="-18" width="140" height="36" rx="5" fill="white" stroke="#0097A7" stroke-width="1.2"/>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="7" fill="#0097A7" text-anchor="middle" font-weight="bold">F = ma</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Второй закон Ньютона</text>
</g>
<g transform="translate(370,260)">
<rect x="-70" y="-18" width="140" height="36" rx="5" fill="white" stroke="#FF6F00" stroke-width="1.2"/>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="7" fill="#FF6F00" text-anchor="middle" font-weight="bold">v &lt;&lt; c</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Границы применимости</text>
</g>
'''+ib(30,295,440,18,["Классическая механика: v << c, макротела | Инерциальные системы отсчёта","Разделы: кинематика, динамика, законы сохранения, статика"])+ftr

# 2
svgs[2]=hdr(titles[2],2)+f'''
<g transform="translate(150,175)">
<line x1="-80" y1="60" x2="80" y2="60" stroke="#333" stroke-width="1.5"/>
<line x1="-60" y1="80" x2="-60" y2="-60" stroke="#333" stroke-width="1.5"/>
<polygon points="80,60 74,57 74,63" fill="#333"/>
<polygon points="-60,-60 -63,-54 -57,-54" fill="#333"/>
<text x="82" y="75" font-family="Arial,sans-serif" font-size="8" fill="#333">x</text>
<text x="-50" y="-55" font-family="Arial,sans-serif" font-size="8" fill="#333">y</text>
<circle cx="20" cy="0" r="5" fill="#E53935" stroke="#C62828" stroke-width="1"/>
<text x="28" y="-5" font-family="Arial,sans-serif" font-size="7" fill="#C62828">M(x,y)</text>
<line x1="20" y1="0" x2="20" y2="60" stroke="#E53935" stroke-width="0.8" stroke-dasharray="3,2"/>
<line x1="20" y1="0" x2="-60" y2="0" stroke="#E53935" stroke-width="0.8" stroke-dasharray="3,2"/>
<text x="-55" y="73" font-family="Arial,sans-serif" font-size="7" fill="#333">O</text>
<line x1="-60" y1="60" x2="18" y2="2" stroke="#1565C0" stroke-width="2"/>
<polygon points="18,2 10,8 14,12" fill="#1565C0"/>
<text x="-30" y="25" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" font-weight="bold">r</text>
</g>
<g transform="translate(370,130)">
<rect x="-80" y="-45" width="160" height="90" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-30" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Система отсчёта</text>
<line x1="-65" y1="-22" x2="65" y2="-22" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-8" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">1. Тело отсчёта</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">2. Система координат</text>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">3. Часы (время)</text>
<text x="0" y="35" font-family="Arial,sans-serif" font-size="5" fill="{P}" text-anchor="middle">СО = тело + оси + часы</text>
</g>
<g transform="translate(370,240)">
<rect x="-70" y="-30" width="140" height="60" rx="5" fill="white" stroke="#FF6F00" stroke-width="1.2"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="7" fill="#FF6F00" text-anchor="middle" font-weight="bold">Материальная точка</text>
<line x1="-55" y1="-8" x2="55" y2="-8" stroke="#FF6F00" stroke-width="0.5"/>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Тело, размерами которого</text>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">можно пренебречь</text>
</g>
'''+ftr

# 3
svgs[3]=hdr(titles[3],3)+f'''
<g transform="translate(150,180)">
<path d="M-70,40 Q-30,-30 0,-10 Q30,10 70,-40" stroke="#FF9800" stroke-width="2.5" fill="none"/>
<circle cx="-70" cy="40" r="5" fill="#2E7D32" stroke="#1B5E20" stroke-width="1"/>
<text x="-70" y="55" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">A</text>
<circle cx="70" cy="-40" r="5" fill="#C62828" stroke="#B71C1C" stroke-width="1"/>
<text x="70" y="-48" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle">B</text>
<line x1="-70" y1="40" x2="65" y2="-37" stroke="#1565C0" stroke-width="2.5"/>
<polygon points="65,-37 55,-30 60,-40" fill="#1565C0"/>
<text x="-15" y="10" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold">S</text>
<text x="0" y="-45" font-family="Arial,sans-serif" font-size="6" fill="#FF9800" text-anchor="middle" font-weight="bold">Путь l</text>
<text x="30" y="30" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">Перемещение S</text>
</g>
<g transform="translate(380,140)">
<rect x="-80" y="-60" width="160" height="120" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-45" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Отличия</text>
<line x1="-65" y1="-38" x2="65" y2="-38" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-22" font-family="Arial,sans-serif" font-size="6" fill="#FF9800" text-anchor="middle" font-weight="bold">Путь l — скаляр</text>
<text x="0" y="-8" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Длина траектории</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">Перемещение S — вектор</text>
<text x="0" y="24" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">из A в B (прямая)</text>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">l &gt;= |S|</text>
<text x="0" y="54" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">l = |S| при прямолинейном</text>
</g>
'''+ftr

# 4
svgs[4]=hdr(titles[4],4)+f'''
<g transform="translate(250,170)">
<circle cx="0" cy="0" r="65" fill="white" stroke="{P}" stroke-width="2"/>
<path d="M-55,30 A65,65 0 0,1 55,30" stroke="#E0E0E0" stroke-width="8" fill="none"/>
<path d="M-55,30 A65,65 0 0,1 0,-65" stroke="#4CAF50" stroke-width="8" fill="none"/>
<path d="M0,-65 A65,65 0 0,1 40,-50" stroke="#FF9800" stroke-width="8" fill="none"/>
<path d="M40,-50 A65,65 0 0,1 55,30" stroke="#E53935" stroke-width="8" fill="none"/>
<line x1="0" y1="0" x2="-20" y2="-50" stroke="#333" stroke-width="2.5"/>
<circle cx="0" cy="0" r="5" fill="#333"/>
<text x="0" y="50" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">м/с</text>
</g>
<g transform="translate(100,100)">
<rect x="-60" y="-25" width="120" height="50" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-8" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Средняя скорость</text>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">v = S / t</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">векторная величина</text>
</g>
<g transform="translate(420,100)">
<rect x="-60" y="-25" width="120" height="50" rx="5" fill="white" stroke="#C62828" stroke-width="1.2"/>
<text x="0" y="-8" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">Мгновенная скорость</text>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">v = dS / dt</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">в точке траектории</text>
</g>
<g transform="translate(100,260)">
<rect x="-60" y="-20" width="120" height="40" rx="5" fill="white" stroke="#FF6F00" stroke-width="1.2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle" font-weight="bold">Скалярная скорость</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">|v| — модуль скорости</text>
</g>
<g transform="translate(420,260)">
<rect x="-60" y="-20" width="120" height="40" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Проекция скорости</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">vx, vy — на оси</text>
</g>
'''+ftr

# 5
svgs[5]=hdr(titles[5],5)+f'''
<g transform="translate(140,200)">
<rect x="-80" y="-75" width="160" height="150" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-60" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">График x(t)</text>
<line x1="-55" y1="50" x2="65" y2="50" stroke="#333" stroke-width="1"/>
<line x1="-55" y1="50" x2="-55" y2="-50" stroke="#333" stroke-width="1"/>
<text x="65" y="62" font-family="Arial,sans-serif" font-size="6" fill="#333">t</text>
<text x="-62" y="-48" font-family="Arial,sans-serif" font-size="6" fill="#333">x</text>
<line x1="-40" y1="30" x2="55" y2="-35" stroke="#E53935" stroke-width="2"/>
<text x="30" y="-15" font-family="Arial,sans-serif" font-size="6" fill="#E53935">x = x0 + vt</text>
<line x1="-55" y1="30" x2="-40" y2="30" stroke="#1565C0" stroke-width="0.8" stroke-dasharray="3,2"/>
<text x="-55" y="27" font-family="Arial,sans-serif" font-size="5" fill="#1565C0">x0</text>
</g>
<g transform="translate(370,180)">
<rect x="-80" y="-75" width="160" height="150" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-60" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">График v(t)</text>
<line x1="-55" y1="50" x2="65" y2="50" stroke="#333" stroke-width="1"/>
<line x1="-55" y1="50" x2="-55" y2="-50" stroke="#333" stroke-width="1"/>
<text x="65" y="62" font-family="Arial,sans-serif" font-size="6" fill="#333">t</text>
<text x="-62" y="-48" font-family="Arial,sans-serif" font-size="6" fill="#333">v</text>
<line x1="-40" y1="10" x2="55" y2="10" stroke="#2E7D32" stroke-width="2"/>
<text x="10" y="5" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">v = const</text>
<line x1="-55" y1="10" x2="-40" y2="10" stroke="#2E7D32" stroke-width="0.8" stroke-dasharray="3,2"/>
<rect x="-40" y="10" width="95" height="40" fill="#2E7D32" opacity="0.1" stroke="#2E7D32" stroke-width="0.5"/>
<text x="8" y="35" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">S = v*t</text>
</g>
'''+ib(30,295,440,18,["Равномерное прямолинейное: v = const | x = x0 + vx*t","График x(t) — прямая, v(t) — горизонтальная прямая, площадь = S"])+ftr

# 6
svgs[6]=hdr(titles[6],6)+f'''
<g transform="translate(250,100)">
<rect x="-120" y="-40" width="240" height="80" rx="8" fill="white" stroke="{P}" stroke-width="2"/>
<text x="0" y="-22" font-family="Arial,sans-serif" font-size="9" fill="{P}" text-anchor="middle" font-weight="bold">Алгоритм решения задач</text>
<line x1="-100" y1="-14" x2="100" y2="-14" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">1. Выбрать систему отсчёта</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">2. Записать условия в проекциях</text>
<text x="0" y="24" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">3. Составить уравнения движения</text>
<text x="0" y="36" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">4. Решить систему уравнений</text>
</g>
<g transform="translate(130,230)">
<rect x="-80" y="-40" width="160" height="80" rx="5" fill="white" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">Графический способ</text>
<line x1="-65" y1="-18" x2="65" y2="-18" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Построить графики x(t)</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Точка пересечения =</text>
<text x="0" y="23" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">место и время встречи</text>
</g>
<g transform="translate(380,230)">
<rect x="-80" y="-40" width="160" height="80" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Аналитический способ</text>
<line x1="-65" y1="-18" x2="65" y2="-18" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">x1(t) = x2(t)</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Решить уравнение</text>
<text x="0" y="23" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">относительно t</text>
</g>
'''+ftr

# 7
svgs[7]=hdr(titles[7],7)+f'''
<g transform="translate(200,185)">
<line x1="-80" y1="0" x2="-10" y2="0" stroke="#E53935" stroke-width="2.5"/>
<polygon points="-10,0 -18,-4 -18,4" fill="#E53935"/>
<text x="-50" y="-8" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle" font-weight="bold">v1</text>
<line x1="-10" y1="0" x2="40" y2="-40" stroke="#2E7D32" stroke-width="2.5"/>
<polygon points="40,-40 32,-34 36,-42" fill="#2E7D32"/>
<text x="25" y="-25" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">v2</text>
<line x1="-80" y1="0" x2="36" y2="-38" stroke="#1565C0" stroke-width="2.5"/>
<polygon points="36,-38 28,-30 32,-40" fill="#1565C0"/>
<text x="-35" y="-25" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" text-anchor="middle" font-weight="bold">v</text>
<line x1="-10" y1="0" x2="50" y2="0" stroke="#999" stroke-width="0.8" stroke-dasharray="3,2"/>
<line x1="40" y1="-40" x2="50" y2="0" stroke="#999" stroke-width="0.8" stroke-dasharray="3,2"/>
</g>
<g transform="translate(400,140)">
<rect x="-70" y="-55" width="140" height="110" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Закон сложения</text>
<line x1="-55" y1="-33" x2="55" y2="-33" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">v = v1 + v2</text>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Векторная сумма</text>
<text x="0" y="15" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Правило треугольника</text>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Правило параллелограмма</text>
<text x="0" y="45" font-family="Arial,sans-serif" font-size="5" fill="{P}" text-anchor="middle">Скорость относительная</text>
</g>
<g transform="translate(400,265)">
<rect x="-60" y="-22" width="120" height="44" rx="5" fill="white" stroke="#FF6F00" stroke-width="1.2"/>
<text x="0" y="-7" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle" font-weight="bold">Относительность</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">v = vотн + vпереносн</text>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Переправа через реку</text>
</g>
'''+ftr

# 8
svgs[8]=hdr(titles[8],8)+f'''
<g transform="translate(140,195)">
<rect x="-80" y="-80" width="160" height="160" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-65" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Графики v(t)</text>
<line x1="-55" y1="55" x2="65" y2="55" stroke="#333" stroke-width="1"/>
<line x1="-55" y1="55" x2="-55" y2="-55" stroke="#333" stroke-width="1"/>
<text x="65" y="67" font-family="Arial,sans-serif" font-size="6" fill="#333">t</text>
<text x="-62" y="-50" font-family="Arial,sans-serif" font-size="6" fill="#333">v</text>
<line x1="-45" y1="40" x2="55" y2="-30" stroke="#E53935" stroke-width="2"/>
<text x="35" y="-20" font-family="Arial,sans-serif" font-size="5" fill="#E53935">v = v0 + at</text>
<line x1="-55" y1="40" x2="-45" y2="40" stroke="#1565C0" stroke-width="0.8" stroke-dasharray="3,2"/>
<text x="-58" y="43" font-family="Arial,sans-serif" font-size="5" fill="#1565C0">v0</text>
</g>
<g transform="translate(390,150)">
<rect x="-80" y="-70" width="160" height="140" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-55" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Формулы</text>
<line x1="-65" y1="-48" x2="65" y2="-48" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-33" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle">v = v0 + at</text>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">S = v0*t + at^2/2</text>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">x = x0 + v0*t + at^2/2</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle">v^2 - v0^2 = 2aS</text>
<line x1="-65" y1="20" x2="65" y2="20" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="35" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">Ускорение</text>
<text x="0" y="50" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">a = (v - v0) / t</text>
<text x="0" y="63" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">м/с^2</text>
</g>
<g transform="translate(390,270)">
<rect x="-60" y="-20" width="120" height="40" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Свободное падение</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">a = g = 9.8 м/с^2</text>
</g>
'''+ftr

# 9
svgs[9]=hdr(titles[9],9)+f'''
<g transform="translate(250,105)">
<rect x="-130" y="-40" width="260" height="80" rx="8" fill="white" stroke="{P}" stroke-width="2"/>
<text x="0" y="-22" font-family="Arial,sans-serif" font-size="8" fill="{P}" text-anchor="middle" font-weight="bold">Система формул равноускоренного движения</text>
<line x1="-115" y1="-14" x2="115" y2="-14" stroke="{P}" stroke-width="0.5"/>
<text x="-60" y="2" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle">v = v0 + at</text>
<text x="60" y="2" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">S = v0t + at^2/2</text>
<text x="-60" y="18" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">x = x0 + v0t + at^2/2</text>
<text x="60" y="18" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle">v^2 - v0^2 = 2aS</text>
<text x="0" y="34" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="middle">4 формулы, 5 неизвестных — нужно знать 2 величины</text>
</g>
<g transform="translate(130,230)">
<rect x="-80" y="-40" width="160" height="80" rx="5" fill="white" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">Аналитический способ</text>
<line x1="-65" y1="-18" x2="65" y2="-18" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">1. Записать формулы</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">2. Подставить данные</text>
<text x="0" y="23" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">3. Решить уравнение</text>
</g>
<g transform="translate(380,230)">
<rect x="-80" y="-40" width="160" height="80" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Графический способ</text>
<line x1="-65" y1="-18" x2="65" y2="-18" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Площадь под v(t)</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">= перемещение S</text>
<text x="0" y="23" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Трапеция или треугольник</text>
</g>
'''+ftr

# 10
svgs[10]=hdr(titles[10],10)+f'''
<g transform="translate(160,190)">
<circle cx="0" cy="0" r="55" fill="none" stroke="{P}" stroke-width="2"/>
<line x1="39" y1="-39" x2="70" y2="-70" stroke="#E53935" stroke-width="2.5"/>
<polygon points="70,-70 60,-62 64,-72" fill="#E53935"/>
<text x="72" y="-65" font-family="Arial,sans-serif" font-size="7" fill="#E53935" font-weight="bold">v</text>
<line x1="39" y1="-39" x2="10" y2="-10" stroke="#2E7D32" stroke-width="2.5"/>
<polygon points="10,-10 18,-16 14,-6" fill="#2E7D32"/>
<text x="15" y="-18" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" font-weight="bold">a</text>
<circle cx="39" cy="-39" r="4" fill="#FF9800" stroke="#E65100" stroke-width="1.5"/>
<line x1="0" y1="0" x2="36" y2="-36" stroke="#999" stroke-width="1" stroke-dasharray="3,2"/>
<text x="10" y="5" font-family="Arial,sans-serif" font-size="6" fill="#999">R</text>
<path d="M15,0 A15,15 0 0,1 11,-11" stroke="#7B1FA2" stroke-width="1.5" fill="none"/>
<text x="22" y="-3" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2">wt</text>
</g>
<g transform="translate(400,145)">
<rect x="-80" y="-70" width="160" height="140" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-55" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Формулы</text>
<line x1="-65" y1="-48" x2="65" y2="-48" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-33" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle">v = 2*pi*R / T</text>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">w = 2*pi / T</text>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">a = v^2 / R = w^2*R</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle">v = w * R</text>
<line x1="-65" y1="20" x2="65" y2="20" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="35" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle">T = 1 / nu</text>
<text x="0" y="50" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">T — период, nu — частота</text>
<text x="0" y="63" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">w — угловая скорость</text>
</g>
<g transform="translate(400,275)">
<rect x="-60" y="-15" width="120" height="30" rx="5" fill="white" stroke="#C62828" stroke-width="1"/>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">a направлено к центру!</text>
</g>
'''+ftr

for num, content in svgs.items():
    path = os.path.join(OUT, f"lesson{num}.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written lesson{num}.svg")

print(f"Done! {len(svgs)} SVG files written to {OUT}")
