#!/usr/bin/env python3
"""Generate Physics grade 10 SVG lesson illustrations (lessons 31-40)."""
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

# 31: Потенциальная энергия
svg31=hdr("Потенциальная энергия",31)+f'''
<g transform="translate(130,185)">
<!-- Ground -->
<line x1="-80" y1="50" x2="80" y2="50" stroke="#795548" stroke-width="2"/>
<!-- Height reference -->
<line x1="-60" y1="50" x2="-60" y2="-40" stroke="#999" stroke-width="0.5" stroke-dasharray="3,2"/>
<text x="-68" y="5" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="end">h</text>
<line x1="-60" y1="50" x2="-55" y2="50" stroke="#999" stroke-width="0.5"/>
<line x1="-60" y1="-40" x2="-55" y2="-40" stroke="#999" stroke-width="0.5"/>
<!-- Object at height -->
<rect x="-15" y="-55" width="30" height="20" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="-41" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">m</text>
<!-- mg arrow -->
<line x1="0" y1="-35" x2="0" y2="-10" stroke="#E53935" stroke-width="1.5"/>
<polygon points="0,-10 -3,-16 3,-16" fill="#E53935"/>
<text x="10" y="-20" font-family="Arial,sans-serif" font-size="6" fill="#E53935">mg</text>
<!-- h arrow on right -->
<line x1="25" y1="50" x2="25" y2="-55" stroke="#7B1FA2" stroke-width="1"/>
<polygon points="25,-55 22,-49 28,-49" fill="#7B1FA2"/>
<polygon points="25,50 22,44 28,44" fill="#7B1FA2"/>
</g>
<g transform="translate(380,175)">
<!-- Spring diagram -->
<line x1="-70" y1="-60" x2="-70" y2="-45" stroke="#333" stroke-width="2"/>
<!-- Spring coils -->
<path d="M-70,-45 L-60,-40 L-80,-30 L-60,-20 L-80,-10 L-60,0 L-80,10 L-60,20 L-70,25 L-70,35" fill="none" stroke="#1565C0" stroke-width="2"/>
<!-- Block on spring -->
<rect x="-25" y="25" width="50" height="25" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">m</text>
<!-- x displacement arrow -->
<line x1="-25" y1="55" x2="25" y2="55" stroke="#2E7D32" stroke-width="1.5"/>
<polygon points="25,55 19,52 19,58" fill="#2E7D32"/>
<text x="0" y="65" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">x</text>
<!-- Equilibrium mark -->
<line x1="-70" y1="38" x2="-70" y2="60" stroke="#999" stroke-width="0.5" stroke-dasharray="2,2"/>
</g>
<g transform="translate(130,280)">
<rect x="-100" y="-18" width="200" height="36" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle" font-weight="bold">Ep = mgh</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Потенциальная энергия в поле тяжести</text>
</g>
<g transform="translate(380,280)">
<rect x="-100" y="-18" width="200" height="36" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Ep = kx^2/2</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Потенциальная энергия пружины</text>
</g>
<g transform="translate(250,90)">
<rect x="-70" y="-15" width="140" height="30" rx="5" fill="white" stroke="#FF6F00" stroke-width="1.2"/>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle" font-weight="bold">Свойство: Ep зависит от выбора</text>
<text x="0" y="11" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle">нулевого уровня (h=0)</text>
</g>
'''+ftr

# 32: Закон сохранения механической энергии
svg32=hdr("Закон сохранения механической энергии",32)+f'''
<g transform="translate(120,195)">
<!-- Pendulum -->
<!-- Pivot -->
<circle cx="0" cy="-70" r="3" fill="#333"/>
<line x1="-15" y1="-70" x2="15" y2="-70" stroke="#333" stroke-width="2"/>
<!-- String positions -->
<line x1="0" y1="-70" x2="-55" y2="10" stroke="#999" stroke-width="0.8" stroke-dasharray="3,2"/>
<line x1="0" y1="-70" x2="0" y2="20" stroke="#1565C0" stroke-width="1.5"/>
<!-- Bob at bottom -->
<circle cx="0" cy="20" r="10" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<!-- Bob at left (max height) -->
<circle cx="-55" cy="10" r="10" fill="#FFF3E0" stroke="#E65100" stroke-width="1.5"/>
<!-- Height marker -->
<line x1="-75" y1="20" x2="-75" y2="10" stroke="#7B1FA2" stroke-width="1"/>
<text x="-80" y="18" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="end">h</text>
<line x1="-75" y1="10" x2="-70" y2="10" stroke="#7B1FA2" stroke-width="0.5"/>
<line x1="-75" y1="20" x2="-70" y2="20" stroke="#7B1FA2" stroke-width="0.5"/>
<!-- Labels -->
<text x="-55" y="30" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">Ep max</text>
<text x="0" y="40" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">Ek max</text>
</g>
<g transform="translate(360,100)">
<!-- Energy bar chart -->
<text x="0" y="-30" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Ek + Ep = const</text>
<!-- Position 1: top -->
<text x="-50" y="-15" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle">h max</text>
<rect x="-65" y="-10" width="12" height="50" rx="1" fill="#E53935" opacity="0.3"/>
<rect x="-65" y="-10" width="12" height="5" rx="1" fill="#E53935"/>
<text x="-59" y="-15" font-family="Arial,sans-serif" font-size="4" fill="#E53935" text-anchor="middle">Ek</text>
<rect x="-50" y="-10" width="12" height="50" rx="1" fill="#1565C0" opacity="0.3"/>
<rect x="-50" y="-10" width="12" height="50" rx="1" fill="#1565C0"/>
<text x="-44" y="-15" font-family="Arial,sans-serif" font-size="4" fill="#1565C0" text-anchor="middle">Ep</text>
<!-- Position 2: middle -->
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle">h/2</text>
<rect x="-15" y="-10" width="12" height="50" rx="1" fill="#E53935" opacity="0.3"/>
<rect x="-15" y="-10" width="12" height="25" rx="1" fill="#E53935"/>
<rect x="0" y="-10" width="12" height="50" rx="1" fill="#1565C0" opacity="0.3"/>
<rect x="0" y="15" width="12" height="25" rx="1" fill="#1565C0"/>
<!-- Position 3: bottom -->
<text x="50" y="-15" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle">h=0</text>
<rect x="35" y="-10" width="12" height="50" rx="1" fill="#E53935" opacity="0.3"/>
<rect x="35" y="-10" width="12" height="50" rx="1" fill="#E53935"/>
<rect x="50" y="-10" width="12" height="50" rx="1" fill="#1565C0" opacity="0.3"/>
<rect x="50" y="40" width="12" height="0" rx="1" fill="#1565C0"/>
<!-- Total line -->
<line x1="-70" y1="-10" x2="65" y2="-10" stroke="#FF6F00" stroke-width="1" stroke-dasharray="3,2"/>
<text x="68" y="-7" font-family="Arial,sans-serif" font-size="5" fill="#FF6F00">E</text>
</g>
<g transform="translate(360,240)">
<rect x="-80" y="-35" width="160" height="70" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Закон сохранения</text>
<line x1="-65" y1="-13" x2="65" y2="-13" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="2" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle" font-weight="bold">Ek1 + Ep1 = Ek2 + Ep2</text>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">При отсутствии сил трения</text>
<text x="0" y="29" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">E = Ek + Ep = const</text>
</g>
'''+ftr

# 33: Решение задач с использованием законов сохранения
svg33=hdr("Решение задач: законы сохранения",33)+f'''
<g transform="translate(250,165)">
<!-- Central problem-solving flowchart -->
<rect x="-60" y="-80" width="120" height="28" rx="5" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="-62" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">1. Выбрать систему</text>
<line x1="0" y1="-52" x2="0" y2="-42" stroke="{P}" stroke-width="1"/>
<polygon points="0,-42 -3,-47 3,-47" fill="{P}"/>
<rect x="-60" y="-42" width="120" height="28" rx="5" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="-24" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">2. Записать закон</text>
<line x1="0" y1="-14" x2="0" y2="-4" stroke="{P}" stroke-width="1"/>
<polygon points="0,-4 -3,-9 3,-9" fill="{P}"/>
<rect x="-60" y="-4" width="120" height="28" rx="5" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="14" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">3. Подставить данные</text>
<line x1="0" y1="24" x2="0" y2="34" stroke="{P}" stroke-width="1"/>
<polygon points="0,34 -3,29 3,29" fill="{P}"/>
<rect x="-60" y="34" width="120" height="28" rx="5" fill="#FFF3E0" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="52" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">4. Решить уравнение</text>
</g>
<g transform="translate(80,130)">
<rect x="-55" y="-30" width="110" height="60" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle" font-weight="bold">Импульс</text>
<line x1="-40" y1="-8" x2="40" y2="-8" stroke="#E53935" stroke-width="0.5"/>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">m1*v1+m2*v2=</text>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">m1*v1'+m2*v2'</text>
</g>
<g transform="translate(80,230)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Энергия</text>
<line x1="-40" y1="-3" x2="40" y2="-3" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Ek1+Ep1=Ek2+Ep2</text>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">(без трения)</text>
</g>
<g transform="translate(420,130)">
<rect x="-55" y="-30" width="110" height="60" rx="5" fill="white" stroke="#FF6F00" stroke-width="1.2"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle" font-weight="bold">Работа</text>
<line x1="-40" y1="-8" x2="40" y2="-8" stroke="#FF6F00" stroke-width="0.5"/>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">A = Ek2 - Ek1</text>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Теорема о кин. энергии</text>
</g>
<g transform="translate(420,230)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">С трением</text>
<line x1="-40" y1="-3" x2="40" y2="-3" stroke="#7B1FA2" stroke-width="0.5"/>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle">Aтр = Ek1+Ep1-</text>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle">(Ek2+Ep2)</text>
</g>
'''+ftr

# 34: Условия равновесия абсолютно твёрдого тела
svg34=hdr("Условия равновесия твёрдого тела",34)+f'''
<g transform="translate(250,180)">
<!-- Rigid body (beam) -->
<rect x="-80" y="-10" width="160" height="20" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<!-- Forces up -->
<line x1="-50" y1="10" x2="-50" y2="35" stroke="#2E7D32" stroke-width="2"/>
<polygon points="-50,35 -53,29 -47,29" fill="#2E7D32"/>
<text x="-50" y="45" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">F1</text>
<line x1="50" y1="10" x2="50" y2="35" stroke="#2E7D32" stroke-width="2"/>
<polygon points="50,35 47,29 53,29" fill="#2E7D32"/>
<text x="50" y="45" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">F2</text>
<!-- Forces down -->
<line x1="-20" y1="-10" x2="-20" y2="-35" stroke="#E53935" stroke-width="2"/>
<polygon points="-20,-35 -17,-29 -23,-29" fill="#E53935"/>
<text x="-20" y="-40" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle">F3</text>
<line x1="30" y1="-10" x2="30" y2="-35" stroke="#E53935" stroke-width="2"/>
<polygon points="30,-35 33,-29 27,-29" fill="#E53935"/>
<text x="30" y="-40" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle">F4</text>
<!-- Weight -->
<line x1="0" y1="10" x2="0" y2="30" stroke="#795548" stroke-width="1.5"/>
<polygon points="0,30 -3,24 3,24" fill="#795548"/>
<text x="10" y="25" font-family="Arial,sans-serif" font-size="5" fill="#795548">mg</text>
</g>
<g transform="translate(100,110)">
<rect x="-70" y="-30" width="140" height="60" rx="5" fill="white" stroke="#E53935" stroke-width="1.5"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle" font-weight="bold">1-е условие</text>
<line x1="-55" y1="-8" x2="55" y2="-8" stroke="#E53935" stroke-width="0.5"/>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">F1+F2+... = 0</text>
<text x="0" y="23" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Векторная сумма сил = 0</text>
</g>
<g transform="translate(400,110)">
<rect x="-70" y="-30" width="140" height="60" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">2-е условие</text>
<line x1="-55" y1="-8" x2="55" y2="-8" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">M1+M2+... = 0</text>
<text x="0" y="23" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Сумма моментов сил = 0</text>
</g>
<g transform="translate(250,290)">
<rect x="-110" y="-20" width="220" height="40" rx="5" fill="white" stroke="#FF6F00" stroke-width="1.2"/>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle" font-weight="bold">Поступательное + вращательное равновесие</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Тело покоится ИЛИ движется равномерно и прямолинейно</text>
</g>
'''+ftr

# 35: Момент силы. Правило моментов
svg35=hdr("Момент силы. Правило моментов",35)+f'''
<g transform="translate(250,190)">
<!-- Lever / seesaw -->
<!-- Fulcrum (triangle) -->
<polygon points="0,35 -15,55 15,55" fill="#795548" stroke="#5D4037" stroke-width="1.5"/>
<!-- Beam -->
<rect x="-120" y="25" width="240" height="8" rx="2" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<!-- Left force (down) -->
<line x1="-80" y1="25" x2="-80" y2="-5" stroke="#E53935" stroke-width="2"/>
<polygon points="-80,-5 -77,1 -83,1" fill="#E53935"/>
<text x="-80" y="-10" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle" font-weight="bold">F1</text>
<!-- Left arm -->
<line x1="-80" y1="33" x2="-5" y2="33" stroke="#7B1FA2" stroke-width="1" stroke-dasharray="2,1"/>
<text x="-42" y="45" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle">l1</text>
<!-- Right force (down) -->
<line x1="70" y1="25" x2="70" y2="-5" stroke="#2E7D32" stroke-width="2"/>
<polygon points="70,-5 73,1 67,1" fill="#2E7D32"/>
<text x="70" y="-10" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">F2</text>
<!-- Right arm -->
<line x1="5" y1="33" x2="70" y2="33" stroke="#7B1FA2" stroke-width="1" stroke-dasharray="2,1"/>
<text x="38" y="45" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle">l2</text>
<!-- Pivot point -->
<circle cx="0" cy="29" r="3" fill="#333"/>
</g>
<g transform="translate(120,100)">
<rect x="-75" y="-25" width="150" height="50" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Момент силы</text>
<line x1="-60" y1="-3" x2="60" y2="-3" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="9" fill="#E53935" text-anchor="middle" font-weight="bold">M = F * l</text>
<text x="0" y="25" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">[M] = Н*м</text>
</g>
<g transform="translate(400,100)">
<rect x="-75" y="-25" width="150" height="50" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Правило моментов</text>
<line x1="-60" y1="-3" x2="60" y2="-3" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">M1 = M2</text>
<text x="0" y="25" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">F1*l1 = F2*l2</text>
</g>
<g transform="translate(250,290)">
<rect x="-110" y="-15" width="220" height="30" rx="5" fill="white" stroke="#FF6F00" stroke-width="1.2"/>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle" font-weight="bold">Правило рычага: выигрываем в силе — проигрываем в расстоянии</text>
</g>
'''+ftr

# 36: Центр тяжести твёрдого тела
svg36=hdr("Центр тяжести твёрдого тела",36)+f'''
<g transform="translate(80,185)">
<!-- Triangle -->
<polygon points="0,-35 -30,25 30,25" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<!-- Medians intersection -->
<line x1="0" y1="-35" x2="0" y2="25" stroke="#999" stroke-width="0.5" stroke-dasharray="2,2"/>
<line x1="-30" y1="25" x2="15" y2="-5" stroke="#999" stroke-width="0.5" stroke-dasharray="2,2"/>
<line x1="30" y1="25" x2="-15" y2="-5" stroke="#999" stroke-width="0.5" stroke-dasharray="2,2"/>
<circle cx="0" cy="5" r="3" fill="#E53935"/>
<text x="0" y="40" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">Треугольник</text>
<text x="0" y="50" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Точка медиан</text>
</g>
<g transform="translate(210,185)">
<!-- Rectangle -->
<rect x="-25" y="-25" width="50" height="50" rx="0" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<!-- Diagonals -->
<line x1="-25" y1="-25" x2="25" y2="25" stroke="#999" stroke-width="0.5" stroke-dasharray="2,2"/>
<line x1="25" y1="-25" x2="-25" y2="25" stroke="#999" stroke-width="0.5" stroke-dasharray="2,2"/>
<circle cx="0" cy="0" r="3" fill="#E53935"/>
<text x="0" y="40" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">Прямоугольник</text>
<text x="0" y="50" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Точка диагоналей</text>
</g>
<g transform="translate(340,185)">
<!-- Circle -->
<circle cx="0" cy="0" r="25" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<!-- Cross -->
<line x1="-25" y1="0" x2="25" y2="0" stroke="#999" stroke-width="0.5" stroke-dasharray="2,2"/>
<line x1="0" y1="-25" x2="0" y2="25" stroke="#999" stroke-width="0.5" stroke-dasharray="2,2"/>
<circle cx="0" cy="0" r="3" fill="#E53935"/>
<text x="0" y="40" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">Круг</text>
<text x="0" y="50" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Геометрический центр</text>
</g>
<g transform="translate(450,185)">
<!-- Semi-circle -->
<path d="M-20,15 A20,20 0 0,1 20,15 Z" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<circle cx="0" cy="6" r="3" fill="#E53935"/>
<text x="0" y="40" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">Полукруг</text>
<text x="0" y="50" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">4R/(3*pi)</text>
</g>
<g transform="translate(250,105)">
<rect x="-85" y="-25" width="170" height="50" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Центр тяжести</text>
<line x1="-70" y1="-3" x2="70" y2="-3" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Точка приложения равнодействующей сил тяжести</text>
<text x="0" y="23" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Однородное тело — центр симметрии</text>
</g>
<g transform="translate(250,290)">
<rect x="-110" y="-15" width="220" height="30" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle" font-weight="bold">Устойчивость: чем ниже ЦТ — тем устойчивее</text>
</g>
'''+ftr

# 37: Давление. Закон Паскаля
svg37=hdr("Давление. Закон Паскаля",37)+f'''
<g transform="translate(130,190)">
<!-- Pascal's law vessel -->
<!-- Container shape -->
<path d="M-40,-50 L-40,30 L40,30 L40,-50 L25,-50 L25,-20 L-25,-20 L-25,-50 Z" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<!-- Fluid inside -->
<path d="M-38,-20 L-38,28 L38,28 L38,-20 Z" fill="#BBDEFB" opacity="0.5"/>
<!-- Pressure arrows from walls -->
<!-- Top arrows -->
<line x1="0" y1="-18" x2="0" y2="-30" stroke="#E53935" stroke-width="1.5"/>
<polygon points="0,-30 -3,-24 3,-24" fill="#E53935"/>
<!-- Left arrows -->
<line x1="-36" y1="5" x2="-20" y2="5" stroke="#E53935" stroke-width="1"/>
<polygon points="-20,5 -26,2 -26,8" fill="#E53935"/>
<line x1="-36" y1="20" x2="-20" y2="20" stroke="#E53935" stroke-width="1"/>
<polygon points="-20,20 -26,17 -26,23" fill="#E53935"/>
<!-- Right arrows -->
<line x1="36" y1="5" x2="20" y2="5" stroke="#E53935" stroke-width="1"/>
<polygon points="20,5 26,2 26,8" fill="#E53935"/>
<line x1="36" y1="20" x2="20" y2="20" stroke="#E53935" stroke-width="1"/>
<polygon points="20,20 26,17 26,23" fill="#E53935"/>
<!-- Bottom arrows -->
<line x1="-15" y1="28" x2="-15" y2="40" stroke="#E53935" stroke-width="1"/>
<polygon points="-15,40 -18,34 -12,34" fill="#E53935"/>
<line x1="15" y1="28" x2="15" y2="40" stroke="#E53935" stroke-width="1"/>
<polygon points="15,40 12,34 18,34" fill="#E53935"/>
<text x="0" y="-55" font-family="Arial,sans-serif" font-size="5" fill="#E53935" text-anchor="middle">p = F/S</text>
</g>
<g transform="translate(390,175)">
<!-- Hydraulic press -->
<!-- Left cylinder (small) -->
<rect x="-55" y="-30" width="30" height="60" rx="2" fill="#BBDEFB" stroke="#1565C0" stroke-width="1.5"/>
<rect x="-60" y="-35" width="40" height="10" rx="2" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<text x="-40" y="-28" font-family="Arial,sans-serif" font-size="4" fill="#1565C0" text-anchor="middle">F1</text>
<line x1="-40" y1="-35" x2="-40" y2="-48" stroke="#E53935" stroke-width="1.5"/>
<polygon points="-40,-48 -43,-42 -37,-42" fill="#E53935"/>
<!-- Right cylinder (large) -->
<rect x="15" y="-30" width="60" height="60" rx="2" fill="#BBDEFB" stroke="#1565C0" stroke-width="1.5"/>
<rect x="10" y="-35" width="70" height="10" rx="2" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<text x="45" y="-28" font-family="Arial,sans-serif" font-size="4" fill="#1565C0" text-anchor="middle">F2</text>
<line x1="45" y1="-48" x2="45" y2="-35" stroke="#2E7D32" stroke-width="1.5"/>
<polygon points="45,-48 42,-42 48,-42" fill="#2E7D32"/>
<!-- Connecting tube -->
<rect x="-25" y="20" width="40" height="10" rx="2" fill="#BBDEFB" stroke="#1565C0" stroke-width="1"/>
<!-- S1, S2 labels -->
<text x="-40" y="50" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="middle">S1</text>
<text x="45" y="50" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="middle">S2</text>
</g>
<g transform="translate(130,105)">
<rect x="-60" y="-18" width="120" height="36" rx="5" fill="white" stroke="{P}" stroke-width="1.2"/>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">p = F / S</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">[p] = Па (Паскаль)</text>
</g>
<g transform="translate(390,105)">
<rect x="-75" y="-18" width="150" height="36" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Гидравлический пресс</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">F1/S1 = F2/S2</text>
</g>
<g transform="translate(250,290)">
<rect x="-130" y="-15" width="260" height="30" rx="5" fill="white" stroke="#FF6F00" stroke-width="1.2"/>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle" font-weight="bold">Закон Паскаля: давление в жидкости передаётся одинаково во все стороны</text>
</g>
'''+ftr

# 38: Давление жидкости и газа. Сообщающиеся сосуды
svg38=hdr("Давление жидкости. Сообщающиеся сосуды",38)+f'''
<g transform="translate(120,190)">
<!-- Connected vessels (U-tube) -->
<!-- Left arm -->
<rect x="-30" y="-40" width="25" height="70" rx="0" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<!-- Right arm -->
<rect x="5" y="-20" width="25" height="50" rx="0" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<!-- Bottom connecting part -->
<rect x="-30" y="30" width="60" height="12" rx="2" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<!-- Fluid in left arm -->
<rect x="-28" y="-10" width="21" height="40" rx="0" fill="#BBDEFB" opacity="0.7"/>
<!-- Fluid in right arm -->
<rect x="7" y="-10" width="21" height="40" rx="0" fill="#BBDEFB" opacity="0.7"/>
<!-- Fluid in bottom -->
<rect x="-28" y="32" width="56" height="8" rx="1" fill="#BBDEFB" opacity="0.7"/>
<!-- Level line -->
<line x1="-35" y1="-10" x2="35" y2="-10" stroke="#E53935" stroke-width="0.8" stroke-dasharray="3,2"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="5" fill="#E53935" text-anchor="middle">одинаковый уровень</text>
<!-- Height markers -->
<line x1="-35" y1="30" x2="-35" y2="-10" stroke="#7B1FA2" stroke-width="1"/>
<text x="-42" y="10" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="end">h</text>
</g>
<g transform="translate(370,195)">
<!-- Hydrostatic pressure diagram -->
<!-- Water column -->
<rect x="-30" y="-60" width="60" height="90" rx="2" fill="#BBDEFB" stroke="#1565C0" stroke-width="1.5"/>
<!-- Pressure arrows at different depths -->
<line x1="-30" y1="-40" x2="-45" y2="-40" stroke="#E53935" stroke-width="1.5"/>
<polygon points="-45,-40 -39,-43 -39,-37" fill="#E53935"/>
<text x="-50" y="-38" font-family="Arial,sans-serif" font-size="5" fill="#E53935" text-anchor="end">p1</text>
<line x1="-30" y1="-10" x2="-55" y2="-10" stroke="#E53935" stroke-width="2"/>
<polygon points="-55,-10 -49,-13 -49,-7" fill="#E53935"/>
<text x="-60" y="-8" font-family="Arial,sans-serif" font-size="5" fill="#E53935" text-anchor="end">p2</text>
<line x1="-30" y1="20" x2="-65" y2="20" stroke="#E53935" stroke-width="2.5"/>
<polygon points="-65,20 -59,17 -59,23" fill="#E53935"/>
<text x="-70" y="22" font-family="Arial,sans-serif" font-size="5" fill="#E53935" text-anchor="end">p3</text>
<!-- Depth labels -->
<line x1="35" y1="-60" x2="35" y2="-40" stroke="#7B1FA2" stroke-width="0.8"/>
<text x="42" y="-48" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2">h1</text>
<line x1="35" y1="-60" x2="35" y2="-10" stroke="#7B1FA2" stroke-width="0.8"/>
<text x="42" y="-30" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2">h2</text>
<line x1="35" y1="-60" x2="35" y2="20" stroke="#7B1FA2" stroke-width="0.8"/>
<text x="42" y="-10" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2">h3</text>
<text x="0" y="-65" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle">поверхность</text>
</g>
<g transform="translate(250,100)">
<rect x="-85" y="-20" width="170" height="40" rx="5" fill="white" stroke="#E53935" stroke-width="1.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle" font-weight="bold">p = rho * g * h</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Гидростатическое давление жидкости</text>
</g>
<g transform="translate(250,290)">
<rect x="-130" y="-15" width="260" height="30" rx="5" fill="white" stroke="#FF6F00" stroke-width="1.2"/>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle" font-weight="bold">Сообщающиеся сосуды: однородная жидкость — один уровень</text>
</g>
'''+ftr

# 39: Закон Архимеда. Плавание тел
svg39=hdr("Закон Архимеда. Плавание тел",39)+f'''
<g transform="translate(120,185)">
<!-- Water container -->
<rect x="-50" y="-30" width="100" height="80" rx="2" fill="#BBDEFB" stroke="#1565C0" stroke-width="1.5" opacity="0.6"/>
<!-- Floating object -->
<rect x="-20" y="-20" width="40" height="25" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
<!-- Water level on object -->
<line x1="-50" y1="-8" x2="50" y2="-8" stroke="#1565C0" stroke-width="0.5" stroke-dasharray="2,1"/>
<!-- Archimedes force (up) -->
<line x1="0" y1="5" x2="0" y2="-40" stroke="#2E7D32" stroke-width="2"/>
<polygon points="0,-40 -3,-34 3,-34" fill="#2E7D32"/>
<text x="12" y="-35" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" font-weight="bold">Fa</text>
<!-- Gravity (down) -->
<line x1="0" y1="5" x2="0" y2="35" stroke="#E53935" stroke-width="2"/>
<polygon points="0,35 -3,29 3,29" fill="#E53935"/>
<text x="12" y="30" font-family="Arial,sans-serif" font-size="7" fill="#E53935" font-weight="bold">mg</text>
<!-- Submerged part highlight -->
<rect x="-18" y="-6" width="36" height="11" rx="1" fill="#90CAF9" opacity="0.4"/>
</g>
<g transform="translate(380,115)">
<rect x="-80" y="-40" width="160" height="80" rx="5" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Закон Архимеда</text>
<line x1="-65" y1="-18" x2="65" y2="-18" stroke="{P}" stroke-width="0.5"/>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Fa = rho * g * V</text>
<text x="0" y="14" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">V — объём погружённой части</text>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">rho — плотность жидкости</text>
</g>
<g transform="translate(300,240)">
<!-- Floating conditions -->
<rect x="-60" y="-30" width="120" height="25" rx="3" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="-13" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Плавает: rho_т &lt; rho_ж</text>
<rect x="-60" y="0" width="120" height="25" rx="3" fill="#FFF9C4" stroke="#F9A825" stroke-width="1"/>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="6" fill="#F9A825" text-anchor="middle">В толще: rho_т = rho_ж</text>
<rect x="-60" y="30" width="120" height="25" rx="3" fill="#FFCDD2" stroke="#E53935" stroke-width="1"/>
<text x="0" y="47" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle">Тонет: rho_т &gt; rho_ж</text>
</g>
'''+ftr

# 40: Основные положения МКТ
svg40=hdr("Основные положения МКТ",40)+f'''
<g transform="translate(250,185)">
<!-- Molecules in gas (random motion) -->
<circle cx="-50" cy="-30" r="4" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.2"/>
<line x1="-46" y1="-30" x2="-30" y2="-20" stroke="#2E7D32" stroke-width="0.8"/>
<polygon points="-30,-20 -36,-22 -34,-17" fill="#2E7D32"/>
<circle cx="-20" cy="10" r="4" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.2"/>
<line x1="-16" y1="10" x2="0" y2="20" stroke="#2E7D32" stroke-width="0.8"/>
<polygon points="0,20 -6,18 -4,23" fill="#2E7D32"/>
<circle cx="30" cy="-25" r="4" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.2"/>
<line x1="34" y1="-25" x2="50" y2="-15" stroke="#2E7D32" stroke-width="0.8"/>
<polygon points="50,-15 44,-17 46,-12" fill="#2E7D32"/>
<circle cx="50" cy="20" r="4" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.2"/>
<line x1="46" y1="20" x2="30" y2="30" stroke="#2E7D32" stroke-width="0.8"/>
<polygon points="30,30 36,28 34,33" fill="#2E7D32"/>
<circle cx="-40" cy="25" r="4" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.2"/>
<line x1="-36" y1="25" x2="-20" y2="15" stroke="#2E7D32" stroke-width="0.8"/>
<polygon points="-20,15 -26,17 -24,12" fill="#2E7D32"/>
<circle cx="10" cy="-10" r="4" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.2"/>
<line x1="14" y1="-10" x2="30" y2="-5" stroke="#2E7D32" stroke-width="0.8"/>
<polygon points="30,-5 24,-7 26,-2" fill="#2E7D32"/>
<circle cx="-10" cy="-50" r="4" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.2"/>
<line x1="-6" y1="-50" x2="10" y2="-45" stroke="#2E7D32" stroke-width="0.8"/>
<polygon points="10,-45 4,-47 6,-42" fill="#2E7D32"/>
<circle cx="60" cy="-5" r="4" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.2"/>
<line x1="56" y1="-5" x2="40" y2="5" stroke="#2E7D32" stroke-width="0.8"/>
<polygon points="40,5 46,3 44,8" fill="#2E7D32"/>
<!-- Container outline -->
<rect x="-65" y="-60" width="140" height="100" rx="3" fill="none" stroke="#1565C0" stroke-width="1" stroke-dasharray="4,2"/>
</g>
<g transform="translate(90,110)">
<rect x="-65" y="-25" width="130" height="50" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle" font-weight="bold">1. Вещество = частицы</text>
<line x1="-50" y1="-3" x2="50" y2="-3" stroke="#E53935" stroke-width="0.5"/>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Молекулы/атомы разделены</text>
<text x="0" y="21" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">промежутками</text>
</g>
<g transform="translate(410,110)">
<rect x="-65" y="-25" width="130" height="50" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">2. Частицы движутся</text>
<line x1="-50" y1="-3" x2="50" y2="-3" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Непрерывное хаотическое</text>
<text x="0" y="21" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">(броуновское движение)</text>
</g>
<g transform="translate(250,290)">
<rect x="-85" y="-20" width="170" height="40" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">3. Частицы взаимодействуют</text>
<line x1="-70" y1="2" x2="70" y2="2" stroke="#7B1FA2" stroke-width="0.5"/>
<text x="0" y="15" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Притяжение (дальше) и отталкивание (ближе)</text>
</g>
'''+ftr

svgs={31:svg31,32:svg32,33:svg33,34:svg34,35:svg35,36:svg36,37:svg37,38:svg38,39:svg39,40:svg40}
for num, content in svgs.items():
    path = os.path.join(OUT, f"lesson{num}.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written lesson{num}.svg")
print(f"Done! {len(svgs)} SVG files written")
