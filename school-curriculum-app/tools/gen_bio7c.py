#!/usr/bin/env python3
"""Generate biology grade 7 lessons 23-32"""
import os
OUT = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade7/biology"
P = "#2E7D32"; L = "#E8F5E9"; M = "#C8E6C9"
def hdr(title, num):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{L}"/><stop offset="100%" stop-color="{M}"/></linearGradient></defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="{P}" stroke-width="2.5"/>
<text x="250" y="30" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="{P}" text-anchor="middle">{title}</text>
<text x="250" y="46" font-family="Arial,sans-serif" font-size="10" fill="#888" text-anchor="middle">Биология 7 класс — Урок {num}</text>
<line x1="30" y1="52" x2="470" y2="52" stroke="{P}" stroke-width="1.5" opacity="0.25"/>
'''
ftr = '\n<rect x="10" y="325" width="480" height="20" rx="4" fill="#2E7D32" opacity="0.85"/>\n<text x="250" y="339" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="white" font-weight="bold">Биология 7 класс</text>\n</svg>'
def ibox(x,y,w,h,lines):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="white" stroke="{P}" stroke-width="1" opacity="0.9"/>\n'
    for i,l in enumerate(lines):
        s += f'<text x="{x+w//2}" y="{y+14+i*12}" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">{l}</text>\n'
    return s

svgs = {}

# 23: Общая характеристика птиц
svgs[23] = hdr("Общая характеристика птиц",23)+'''
<g transform="translate(200,175)">
<!-- Body -->
<ellipse cx="0" cy="0" rx="35" ry="22" fill="#90CAF9" stroke="#1565C0" stroke-width="2"/>
<!-- Head -->
<circle cx="-35" cy="-15" r="14" fill="#BBDEFB" stroke="#1565C0" stroke-width="2"/>
<!-- Beak -->
<path d="M-49,-18 L-60,-15 L-49,-12Z" fill="#FFB300" stroke="#E65100" stroke-width="1.5"/>
<!-- Eye -->
<circle cx="-38" cy="-17" r="3" fill="white" stroke="#333" stroke-width="0.8"/>
<circle cx="-38" cy="-17" r="1.5" fill="#333"/>
<!-- Wing -->
<path d="M-10,-18 Q10,-35 30,-28 Q40,-22 35,-12 Q20,-5 5,-8Z" fill="#64B5F6" stroke="#1565C0" stroke-width="1.5"/>
<!-- Tail -->
<path d="M32,-5 L50,-15 L48,0 L50,10 L32,5Z" fill="#64B5F6" stroke="#1565C0" stroke-width="1"/>
<!-- Legs -->
<path d="M-10,20 L-14,38 L-18,40 M-14,38 L-10,40 M-14,38 L-14,42" stroke="#E65100" stroke-width="2" fill="none"/>
<path d="M10,20 L6,38 L2,40 M6,38 L10,40 M6,38 L6,42" stroke="#E65100" stroke-width="2" fill="none"/>
<!-- Feathers detail -->
<path d="M-5,-10 Q0,-15 5,-10" stroke="#42A5F5" stroke-width="0.5" fill="none"/>
<path d="M10,-8 Q15,-12 20,-8" stroke="#42A5F5" stroke-width="0.5" fill="none"/>
</g>
<g transform="translate(400,120)">
<text x="0" y="0" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" text-anchor="middle" font-weight="bold">Приспособления к полёту</text>
<rect x="-55" y="8" width="110" height="15" rx="3" fill="#BBDEFB" stroke="#1565C0" stroke-width="0.8"/>
<text x="0" y="19" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">Перья (опахало + стержень)</text>
<rect x="-55" y="28" width="110" height="15" rx="3" fill="#BBDEFB" stroke="#1565C0" stroke-width="0.8"/>
<text x="0" y="39" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">Полые кости (пневматич.)</text>
<rect x="-55" y="48" width="110" height="15" rx="3" fill="#BBDEFB" stroke="#1565C0" stroke-width="0.8"/>
<text x="0" y="59" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">Киль на грудине</text>
<rect x="-55" y="68" width="110" height="15" rx="3" fill="#BBDEFB" stroke="#1565C0" stroke-width="0.8"/>
<text x="0" y="79" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">Воздушные мешки</text>
<rect x="-55" y="88" width="110" height="15" rx="3" fill="#BBDEFB" stroke="#1565C0" stroke-width="0.8"/>
<text x="0" y="99" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">4-камерное сердце</text>
</g>
'''+ibox(30,290,440,22,["Теплокровные | Перья | Беззубый клюв | 4-камерное сердце | Двойное дыхание | Яйцекладущие"])+ftr

# 24: Внутреннее строение птиц
svgs[24] = hdr("Внутреннее строение птиц",24)+'''
<g transform="translate(250,175)">
<ellipse cx="0" cy="0" rx="55" ry="40" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5" opacity="0.4"/>
<!-- Spine -->
<path d="M-40,-20 Q0,-25 40,-20" stroke="#795548" stroke-width="2" fill="none"/>
<!-- Brain -->
<ellipse cx="-42" cy="-25" rx="8" ry="6" fill="#FFCDD2" stroke="#C62828" stroke-width="1"/>
<text x="-42" y="-35" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">Мозг</text>
<!-- Heart (4-chamber) -->
<rect x="-35" y="-5" width="14" height="14" rx="2" fill="#E53935" stroke="#C62828" stroke-width="1"/>
<line x1="-35" y1="2" x2="-21" y2="2" stroke="#C62828" stroke-width="0.8"/>
<text x="-28" y="18" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">4-кам.</text>
<!-- Lungs + air sacs -->
<ellipse cx="-15" cy="-10" rx="8" ry="5" fill="#FFCDD2" stroke="#E53935" stroke-width="1"/>
<ellipse cx="5" cy="-10" rx="8" ry="5" fill="#FFCDD2" stroke="#E53935" stroke-width="1"/>
<text x="-5" y="-18" font-family="Arial,sans-serif" font-size="5" fill="#E53935" text-anchor="middle">Лёгкие</text>
<!-- Air sacs -->
<circle cx="-20" cy="18" r="5" fill="#E1F5FE" stroke="#42A5F5" stroke-width="0.8" opacity="0.5"/>
<circle cx="-8" cy="22" r="5" fill="#E1F5FE" stroke="#42A5F5" stroke-width="0.8" opacity="0.5"/>
<circle cx="8" cy="22" r="5" fill="#E1F5FE" stroke="#42A5F5" stroke-width="0.8" opacity="0.5"/>
<circle cx="20" cy="18" r="5" fill="#E1F5FE" stroke="#42A5F5" stroke-width="0.8" opacity="0.5"/>
<text x="0" y="32" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">Воздушные мешки</text>
<!-- Crop -->
<ellipse cx="-12" cy="-2" rx="6" ry="4" fill="#C8E6C9" stroke="#2E7D32" stroke-width="0.8"/>
<!-- Stomach (2 parts) -->
<rect x="-5" y="2" width="10" height="6" rx="2" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
<rect x="8" y="2" width="10" height="7" rx="2" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
<text x="5" y="0" font-family="Arial,sans-serif" font-size="4" fill="#E65100" text-anchor="middle">Желудок</text>
<!-- Intestine -->
<path d="M18,6 Q30,5 32,10 Q34,15 25,18" stroke="#E65100" stroke-width="1.5" fill="none"/>
<!-- Liver -->
<ellipse cx="15" cy="-3" rx="8" ry="5" fill="#8D6E63" opacity="0.4" stroke="#5D4037" stroke-width="0.8"/>
<!-- Kidney -->
<ellipse cx="30" cy="-5" rx="5" ry="8" fill="#A5D6A7" stroke="#2E7D32" stroke-width="0.8"/>
<!-- Gizzard label -->
<text x="13" y="15" font-family="Arial,sans-serif" font-size="4" fill="#E65100" text-anchor="middle">Мускульн.</text>
</g>
'''+ibox(30,275,440,38,["4-камерное сердце: 2 предсердия + 2 желудочка | Двойное дыхание","Желудок: железистый + мускульный (желудок) | Нет зубов | Клюв","Воздушные мешки: облегчение тела, дыхание в полёте | Теплокровность"])+ftr

# 25: Многообразие птиц
svgs[25] = hdr("Многообразие птиц",25)+'''
<g transform="translate(70,130)">
<ellipse cx="0" cy="0" rx="15" ry="10" fill="#90CAF9" stroke="#1565C0" stroke-width="1.5"/>
<circle cx="-12" cy="-6" r="6" fill="#BBDEFB" stroke="#1565C0" stroke-width="1"/>
<path d="M-18,-8 L-25,-6 L-18,-4Z" fill="#FFB300" stroke="#E65100" stroke-width="1"/>
<circle cx="-14" cy="-8" r="1.5" fill="#333"/>
<path d="M12,-5 L18,-12 L14,-3" stroke="#1565C0" stroke-width="1" fill="none"/>
<path d="M10,8 L8,18" stroke="#E65100" stroke-width="1.5" fill="none"/>
<text x="0" y="25" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle" font-weight="bold">Воробей</text>
<text x="0" y="33" font-family="Arial,sans-serif" font-size="4" fill="#666" text-anchor="middle">Воробьинообразные</text>
</g>
<g transform="translate(170,140)">
<ellipse cx="0" cy="0" rx="20" ry="12" fill="#66BB6A" stroke="#2E7D32" stroke-width="1.5"/>
<circle cx="-18" cy="-8" r="7" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
<path d="M-24,-10 L-32,-7 L-24,-4Z" fill="#795548" stroke="#4E342E" stroke-width="1"/>
<circle cx="-20" cy="-10" r="1.5" fill="#333"/>
<path d="M18,-5 L25,-15 L20,-3" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
<path d="M5,10 L3,22" stroke="#E65100" stroke-width="1.5" fill="none"/>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle" font-weight="bold">Утка</text>
<text x="0" y="36" font-family="Arial,sans-serif" font-size="4" fill="#666" text-anchor="middle">Гусеобразные</text>
</g>
<g transform="translate(280,135)">
<ellipse cx="0" cy="0" rx="12" ry="8" fill="#FFAB91" stroke="#BF360C" stroke-width="1.5"/>
<circle cx="-10" cy="-5" r="5" fill="#FFCCBC" stroke="#BF360C" stroke-width="1"/>
<path d="M-14,-7 L-20,-5 L-14,-3Z" fill="#FFB300" stroke="#E65100" stroke-width="1"/>
<circle cx="-12" cy="-7" r="1" fill="#333"/>
<path d="M10,-5 L15,-12 L12,-2" stroke="#BF360C" stroke-width="1" fill="none"/>
<path d="M5,6 L3,16" stroke="#BF360C" stroke-width="1" fill="none"/>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle" font-weight="bold">Сова</text>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="4" fill="#666" text-anchor="middle">Совообразные</text>
</g>
<g transform="translate(380,130)">
<ellipse cx="0" cy="5" rx="18" ry="15" fill="#EF9A9A" stroke="#C62828" stroke-width="1.5"/>
<circle cx="-15" cy="-5" r="6" fill="#FFCDD2" stroke="#C62828" stroke-width="1"/>
<path d="M-20,-7 L-28,-4 L-20,-1Z" fill="#FFB300" stroke="#E65100" stroke-width="1"/>
<circle cx="-17" cy="-7" r="1.5" fill="#333"/>
<path d="M-5,-12 L0,-20" stroke="#C62828" stroke-width="1.5" fill="none"/>
<path d="M15,5 L15,18" stroke="#E65100" stroke-width="1.5" fill="none"/>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle" font-weight="bold">Орёл</text>
<text x="0" y="36" font-family="Arial,sans-serif" font-size="4" fill="#666" text-anchor="middle">Соколообразные</text>
</g>
<g transform="translate(100,240)">
<ellipse cx="0" cy="0" rx="25" ry="15" fill="#8D6E63" stroke="#4E342E" stroke-width="1.5"/>
<ellipse cx="0" cy="-15" rx="10" ry="8" fill="#A1887F" stroke="#4E342E" stroke-width="1"/>
<path d="M-5,-23 L0,-30 L5,-23" fill="#FFB300" stroke="#E65100" stroke-width="1"/>
<circle cx="-3" cy="-17" r="1.5" fill="#333"/><circle cx="3" cy="-17" r="1.5" fill="#333"/>
<path d="M-20,10 L-25,25" stroke="#4E342E" stroke-width="1.5" fill="none"/>
<path d="M20,10 L25,25" stroke="#4E342E" stroke-width="1.5" fill="none"/>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle" font-weight="bold">Страус</text>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="4" fill="#666" text-anchor="middle">Страусообразные</text>
</g>
<g transform="translate(280,240)">
<ellipse cx="0" cy="0" rx="15" ry="12" fill="#4FC3F7" stroke="#0277BD" stroke-width="1.5"/>
<circle cx="-10" cy="-8" r="5" fill="#81D4FA" stroke="#0277BD" stroke-width="1"/>
<path d="M-14,-10 L-20,-8 L-14,-6Z" fill="#FFB300" stroke="#E65100" stroke-width="1"/>
<circle cx="-12" cy="-10" r="1.5" fill="#333"/>
<path d="M12,0 L22,-5 L18,5" stroke="#0277BD" stroke-width="1.5" fill="none"/>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle" font-weight="bold">Пингвин</text>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="4" fill="#666" text-anchor="middle">Пингвинообразные</text>
</g>
<g transform="translate(430,240)">
<ellipse cx="0" cy="0" rx="18" ry="10" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1.5"/>
<circle cx="-15" cy="-5" r="5" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
<path d="M-19,-7 L-26,-5 L-19,-3Z" fill="#795548" stroke="#4E342E" stroke-width="1"/>
<circle cx="-17" cy="-7" r="1.5" fill="#333"/>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle" font-weight="bold">Курица</text>
<text x="0" y="26" font-family="Arial,sans-serif" font-size="4" fill="#666" text-anchor="middle">Курообразные</text>
</g>
'''+ibox(30,295,440,18,["Около 9000 видов | Пингвины, страусы — нелетающие | Дневные и ночные хищники | Водоплавающие"])+ftr

# 26: Общая характеристика млекопитающих
svgs[26] = hdr("Общая характеристика млекопитающих",26)+'''
<g transform="translate(200,170)">
<ellipse cx="0" cy="5" rx="35" ry="22" fill="#A1887F" stroke="#4E342E" stroke-width="2"/>
<ellipse cx="-30" cy="-5" rx="16" ry="12" fill="#BCAAA4" stroke="#4E342E" stroke-width="2"/>
<circle cx="-36" cy="-10" r="3" fill="#333"/>
<circle cx="-36" cy="-10" r="1.2" fill="#666"/>
<path d="M-44,-8 L-52,-6 L-44,-4Z" fill="#6D4C41" stroke="#4E342E" stroke-width="1"/>
<circle cx="-40" cy="-3" r="1" fill="#5D4037"/>
<path d="M-22,-15 Q-25,-25 -20,-28" stroke="#8D6E63" stroke-width="1" fill="none"/>
<path d="M-15,-14 Q-18,-24 -13,-27" stroke="#8D6E63" stroke-width="1" fill="none"/>
<path d="M30,0 L42,-5 Q48,-3 45,2" stroke="#8D6E63" stroke-width="2.5" fill="none"/>
<path d="M-15,25 L-18,40" stroke="#4E342E" stroke-width="2.5" fill="none"/>
<path d="M5,25 L2,40" stroke="#4E342E" stroke-width="2.5" fill="none"/>
<path d="M20,25 L18,40" stroke="#4E342E" stroke-width="2.5" fill="none"/>
</g>
<g transform="translate(410,105)">
<rect x="-55" y="-20" width="110" height="160" rx="5" fill="white" stroke="#4E342E" stroke-width="1.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="8" fill="#4E342E" text-anchor="middle" font-weight="bold">Признаки</text>
<rect x="-45" y="5" width="90" height="15" rx="3" fill="#FFCDD2" stroke="#C62828" stroke-width="0.8"/>
<text x="0" y="16" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">Молочные железы</text>
<rect x="-45" y="25" width="90" height="15" rx="3" fill="#BBDEFB" stroke="#1565C0" stroke-width="0.8"/>
<text x="0" y="36" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">4-камерное сердце</text>
<rect x="-45" y="45" width="90" height="15" rx="3" fill="#C8E6C9" stroke="#2E7D32" stroke-width="0.8"/>
<text x="0" y="56" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Шерсть (волосяной покров)</text>
<rect x="-45" y="65" width="90" height="15" rx="3" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
<text x="0" y="76" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Зубы дифференцированы</text>
<rect x="-45" y="85" width="90" height="15" rx="3" fill="#E1BEE7" stroke="#7B1FA2" stroke-width="0.8"/>
<text x="0" y="96" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle">Альвеолярные лёгкие</text>
<rect x="-45" y="105" width="90" height="15" rx="3" fill="#B2DFDB" stroke="#00695C" stroke-width="0.8"/>
<text x="0" y="116" font-family="Arial,sans-serif" font-size="6" fill="#00695C" text-anchor="middle">Диафрагма</text>
</g>
'''+ibox(30,290,440,22,["Теплокровные | Живорождение (кроме яйцекладущих) | Кормление молоком | Шерсть | Зубы 4 типа"])+ftr

# 27: Внутреннее строение млекопитающих
svgs[27] = hdr("Внутреннее строение млекопитающих",27)+'''
<g transform="translate(250,175)">
<ellipse cx="0" cy="0" rx="65" ry="45" fill="#EFEBE9" stroke="#5D4037" stroke-width="1.5" opacity="0.4"/>
<!-- Spine -->
<path d="M-45,-25 Q0,-30 45,-25" stroke="#795548" stroke-width="2.5" fill="none"/>
<!-- Brain -->
<ellipse cx="-48" cy="-32" rx="10" ry="8" fill="#FFCDD2" stroke="#C62828" stroke-width="1.5"/>
<text x="-48" y="-43" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">Мозг (кора)</text>
<!-- Heart -->
<rect x="-35" y="-8" width="16" height="16" rx="3" fill="#E53935" stroke="#C62828" stroke-width="1.5"/>
<line x1="-35" y1="0" x2="-19" y2="0" stroke="#C62828" stroke-width="1"/>
<text x="-27" y="18" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">4-кам.</text>
<!-- Lungs (2) -->
<ellipse cx="-18" cy="-12" rx="10" ry="8" fill="#FFCDD2" stroke="#E53935" stroke-width="1"/>
<ellipse cx="0" cy="-12" rx="10" ry="8" fill="#FFCDD2" stroke="#E53935" stroke-width="1"/>
<text x="-9" y="-24" font-family="Arial,sans-serif" font-size="5" fill="#E53935" text-anchor="middle">Лёгкие</text>
<!-- Diaphragm -->
<path d="M-40,8 Q-20,14 0,8 Q20,14 40,8" stroke="#9C27B0" stroke-width="2" fill="none"/>
<text x="35" y="14" font-family="Arial,sans-serif" font-size="5" fill="#9C27B0" text-anchor="start">Диафрагма</text>
<!-- Liver -->
<ellipse cx="-10" cy="20" rx="18" ry="8" fill="#8D6E63" opacity="0.4" stroke="#5D4037" stroke-width="1"/>
<text x="-10" y="22" font-family="Arial,sans-serif" font-size="5" fill="#5D4037" text-anchor="middle">Печень</text>
<!-- Stomach -->
<ellipse cx="18" cy="18" rx="10" ry="8" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
<text x="18" y="20" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">Желудок</text>
<!-- Intestine -->
<path d="M28,22 Q38,20 40,28 Q42,35 35,38 Q25,40 20,35" stroke="#E65100" stroke-width="1.5" fill="none"/>
<!-- Kidneys -->
<ellipse cx="-25" cy="30" rx="6" ry="4" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
<ellipse cx="35" cy="30" rx="6" ry="4" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
<text x="5" y="33" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Почки</text>
</g>
'''+ibox(30,275,440,38,["4-камерное сердце | 2 круга кровообращения | Альвеолярные лёгкие | Диафрагма","Дифференцированные зубы: резцы, клыки, коренные | Левая дуга аорты","Нефроны в почках | Высшая нервная деятельность (кора больших полушарий)"])+ftr

# 28: Многообразие млекопитающих. Яйцекладущие и сумчатые
svgs[28] = hdr("Яйцекладущие и сумчатые млекопитающие",28)+'''
<g transform="translate(130,170)">
<!-- Duck-billed platypus -->
<ellipse cx="0" cy="5" rx="25" ry="15" fill="#8D6E63" stroke="#4E342E" stroke-width="1.5"/>
<ellipse cx="-22" cy="-2" rx="12" ry="8" fill="#A1887F" stroke="#4E342E" stroke-width="1.5"/>
<path d="M-32,-4 L-45,-2 L-32,0Z" fill="#FFB300" stroke="#E65100" stroke-width="1.5"/>
<circle cx="-26" cy="-6" r="1.5" fill="#333"/>
<path d="M20,10 L28,18" stroke="#4E342E" stroke-width="1.5" fill="none"/>
<path d="M10,18 L8,28" stroke="#4E342E" stroke-width="1.5" fill="none"/>
<path d="M-10,18 L-12,28" stroke="#4E342E" stroke-width="1.5" fill="none"/>
<!-- Flat tail -->
<path d="M22,5 Q30,8 35,2 Q30,-2 22,0" fill="#A1887F" stroke="#4E342E" stroke-width="1"/>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="7" fill="#4E342E" text-anchor="middle" font-weight="bold">Утконос</text>
<text x="0" y="52" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Яйцекладущий</text>
</g>
<g transform="translate(350,170)">
<!-- Kangaroo -->
<ellipse cx="5" cy="0" rx="20" ry="25" fill="#FFCC80" stroke="#E65100" stroke-width="1.5"/>
<ellipse cx="-5" cy="-30" rx="10" ry="8" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
<circle cx="-9" cy="-34" r="2" fill="#333"/>
<path d="M-13,-32 L-18,-30 L-13,-28Z" fill="#6D4C41"/>
<path d="M-12,-38 Q-15,-45 -12,-48" stroke="#E65100" stroke-width="1" fill="none"/>
<path d="M-4,-38 Q-2,-45 0,-48" stroke="#E65100" stroke-width="1" fill="none"/>
<!-- Pouch with baby -->
<path d="M-5,5 Q0,12 5,5" stroke="#BF360C" stroke-width="1.5" fill="#FFCC80" opacity="0.5"/>
<circle cx="0" cy="8" r="4" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
<!-- Big hind legs -->
<path d="M15,20 L25,35 L20,45" stroke="#E65100" stroke-width="2.5" fill="none"/>
<!-- Small front legs -->
<path d="M-8,-5 L-15,5" stroke="#E65100" stroke-width="1.5" fill="none"/>
<!-- Tail -->
<path d="M20,15 Q35,25 40,35 Q42,40 38,42" stroke="#E65100" stroke-width="3" fill="none"/>
<text x="5" y="55" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">Кенгуру</text>
<text x="5" y="65" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Сумчатый</text>
</g>
'''+ibox(30,265,440,45,["Подкласс Яйцекладущие (Однопроходные): утконос, ехидна","Откладывают яйца, но кормят молоком | Клоака | Самые примитивные млекопитающие","Подкласс Сумчатые: кенгуру, коала, опоссум","Недоразвитые детёныши | Выводковая сумка | Австралия и Южная Америка"])+ftr

# 29: Многообразие млекопитающих. Плацентарные
svgs[29] = hdr("Плацентарные млекопитающие",29)+'''
<g transform="translate(65,115)">
<ellipse cx="0" cy="5" rx="18" ry="12" fill="#EF9A9A" stroke="#C62828" stroke-width="1.5"/>
<ellipse cx="-15" cy="-3" rx="8" ry="6" fill="#FFCDD2" stroke="#C62828" stroke-width="1"/>
<path d="M-21,-5 L-26,-3 L-21,-1Z" fill="#FFB300"/>
<circle cx="-18" cy="-6" r="1.5" fill="#333"/>
<path d="M-8,-8 L-10,-16" stroke="#C62828" stroke-width="0.8" fill="none"/>
<path d="M-4,-8 L-6,-16" stroke="#C62828" stroke-width="0.8" fill="none"/>
<text x="0" y="24" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle" font-weight="bold">Мышь</text>
<text x="0" y="32" font-family="Arial,sans-serif" font-size="4" fill="#666" text-anchor="middle">Грызуны</text>
</g>
<g transform="translate(165,120)">
<ellipse cx="0" cy="5" rx="15" ry="10" fill="#FFCC80" stroke="#E65100" stroke-width="1.5"/>
<ellipse cx="-12" cy="-2" rx="8" ry="6" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
<circle cx="-15" cy="-5" r="1.5" fill="#333"/>
<path d="M-5,12 L-8,22" stroke="#E65100" stroke-width="1.5" fill="none"/>
<path d="M5,12 L3,22" stroke="#E65100" stroke-width="1.5" fill="none"/>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle" font-weight="bold">Волк</text>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="4" fill="#666" text-anchor="middle">Хищные</text>
</g>
<g transform="translate(265,115)">
<ellipse cx="0" cy="8" rx="25" ry="18" fill="#81C784" stroke="#2E7D32" stroke-width="1.5"/>
<ellipse cx="-20" cy="-5" rx="8" ry="6" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
<circle cx="-23" cy="-8" r="1.5" fill="#333"/>
<path d="M15,5 L25,2" stroke="#2E7D32" stroke-width="2" fill="none"/>
<path d="M-15,22 L-18,32" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
<path d="M5,22 L3,32" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle" font-weight="bold">Корова</text>
<text x="0" y="46" font-family="Arial,sans-serif" font-size="4" fill="#666" text-anchor="middle">Парнокопытные</text>
</g>
<g transform="translate(385,115)">
<ellipse cx="0" cy="5" rx="15" ry="12" fill="#B39DDB" stroke="#5E35B1" stroke-width="1.5"/>
<ellipse cx="5" cy="-15" rx="5" ry="6" fill="#D1C4E9" stroke="#5E35B1" stroke-width="1"/>
<circle cx="4" cy="-18" r="1.5" fill="#333"/>
<path d="M5,-21 Q8,-28 6,-32" stroke="#5E35B1" stroke-width="0.8" fill="none"/>
<path d="M3,-21 Q0,-28 2,-32" stroke="#5E35B1" stroke-width="0.8" fill="none"/>
<path d="M-12,10 L-15,20" stroke="#5E35B1" stroke-width="1.5" fill="none"/>
<path d="M12,10 L15,20" stroke="#5E35B1" stroke-width="1.5" fill="none"/>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle" font-weight="bold">Обезьяна</text>
<text x="0" y="36" font-family="Arial,sans-serif" font-size="4" fill="#666" text-anchor="middle">Приматы</text>
</g>
<g transform="translate(100,240)">
<ellipse cx="0" cy="5" rx="30" ry="18" fill="#4FC3F7" stroke="#0277BD" stroke-width="1.5"/>
<ellipse cx="-25" cy="-5" rx="8" ry="6" fill="#81D4FA" stroke="#0277BD" stroke-width="1"/>
<circle cx="-28" cy="-8" r="1.5" fill="#333"/>
<path d="M20,-8 Q30,-20 25,-25" stroke="#0277BD" stroke-width="1.5" fill="none"/>
<path d="M25,-5 Q35,-15 30,-20" stroke="#0277BD" stroke-width="1.5" fill="none"/>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle" font-weight="bold">Дельфин</text>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="4" fill="#666" text-anchor="middle">Китообразные</text>
</g>
<g transform="translate(280,240)">
<ellipse cx="0" cy="5" rx="20" ry="14" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1.5"/>
<ellipse cx="-15" cy="-3" rx="7" ry="5" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
<circle cx="-18" cy="-6" r="1.5" fill="#333"/>
<path d="M15,0 L22,-5 L18,5" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
<path d="M-5,16 L-5,28" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
<path d="M5,16 L5,28" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle" font-weight="bold">Лошадь</text>
<text x="0" y="46" font-family="Arial,sans-serif" font-size="4" fill="#666" text-anchor="middle">Непарнокопытные</text>
</g>
<g transform="translate(430,240)">
<ellipse cx="0" cy="0" rx="12" ry="8" fill="#8D6E63" stroke="#4E342E" stroke-width="1.5"/>
<path d="M-5,-8 Q-8,-15 -4,-18 Q0,-20 4,-18 Q8,-15 5,-8" fill="#A1887F" stroke="#4E342E" stroke-width="1"/>
<path d="M-10,6 L-14,14" stroke="#4E342E" stroke-width="1" fill="none"/>
<path d="M10,6 L14,14" stroke="#4E342E" stroke-width="1" fill="none"/>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle" font-weight="bold">Крот</text>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="4" fill="#666" text-anchor="middle">Насекомоядные</text>
</g>
'''+ibox(30,295,440,18,["18+ отрядов плацентарных | Развитие через плаценту | Наиболее высокоорганизованные животные"])+ftr

# 30: Приматы и значение млекопитающих
svgs[30] = hdr("Приматы и значение млекопитающих",30)+'''
<g transform="translate(130,170)">
<ellipse cx="0" cy="8" rx="15" ry="12" fill="#D7CCC8" stroke="#5D4037" stroke-width="1.5"/>
<circle cx="-5" cy="-8" r="10" fill="#EFEBE9" stroke="#5D4037" stroke-width="1.5"/>
<circle cx="-8" cy="-10" r="2.5" fill="white" stroke="#333" stroke-width="0.8"/><circle cx="-8" cy="-10" r="1.2" fill="#333"/>
<circle cx="-2" cy="-10" r="2.5" fill="white" stroke="#333" stroke-width="0.8"/><circle cx="-2" cy="-10" r="1.2" fill="#333"/>
<path d="M-10,-7 Q-5,-5 0,-7" stroke="#5D4037" stroke-width="1" fill="none"/>
<ellipse cx="-15" cy="-5" rx="4" ry="6" fill="#BCAAA4" stroke="#5D4037" stroke-width="0.8"/>
<path d="M-10,15 L-12,25" stroke="#5D4037" stroke-width="1.5" fill="none"/>
<path d="M0,15 L2,25" stroke="#5D4037" stroke-width="1.5" fill="none"/>
<path d="M12,5 L18,0" stroke="#5D4037" stroke-width="1.5" fill="none"/>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="7" fill="#5D4037" text-anchor="middle" font-weight="bold">Обезьяна</text>
</g>
<g transform="translate(350,140)">
<text x="0" y="0" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Значение млекопитающих</text>
<rect x="-70" y="10" width="140" height="18" rx="3" fill="#C8E6C9" stroke="#2E7D32" stroke-width="0.8"/>
<text x="0" y="23" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Пища: мясо, молоко, яйца</text>
<rect x="-70" y="32" width="140" height="18" rx="3" fill="#FFECB3" stroke="#FF8F00" stroke-width="0.8"/>
<text x="0" y="45" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Шкуры, кожа, шерсть</text>
<rect x="-70" y="54" width="140" height="18" rx="3" fill="#BBDEFB" stroke="#1565C0" stroke-width="0.8"/>
<text x="0" y="67" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">Транспорт: лошади, верблюды</text>
<rect x="-70" y="76" width="140" height="18" rx="3" fill="#F8BBD0" stroke="#C2185B" stroke-width="0.8"/>
<text x="0" y="89" font-family="Arial,sans-serif" font-size="6" fill="#C2185B" text-anchor="middle">Опыление, распространение</text>
<rect x="-70" y="98" width="140" height="18" rx="3" fill="#FFCDD2" stroke="#C62828" stroke-width="0.8"/>
<text x="0" y="111" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">Вред: грызуны, хищники</text>
</g>
'''+ibox(30,290,440,22,["Приматы: обезьяны, полуобезьяны, человек | Обхватывающие руки | Бинокулярное зрение | Большой мозг"])+ftr

# 31: Эволюция и развитие животного мира
svgs[31] = hdr("Эволюция и развитие животного мира",31)+'''
<!-- Evolution timeline -->
<line x1="40" y1="180" x2="460" y2="180" stroke="#2E7D32" stroke-width="3"/>
<!-- Arrow at end -->
<path d="M460,180 L455,175 M460,180 L455,185" stroke="#2E7D32" stroke-width="2" fill="none"/>
<!-- Timeline nodes -->
<circle cx="70" cy="180" r="8" fill="#FF9800" stroke="#E65100" stroke-width="1.5"/>
<text x="70" y="183" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle" font-weight="bold">1</text>
<text x="70" y="205" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Простейшие</text>

<circle cx="130" cy="180" r="8" fill="#9C27B0" stroke="#7B1FA2" stroke-width="1.5"/>
<text x="130" y="183" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle" font-weight="bold">2</text>
<text x="130" y="205" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle">Кишечнополостные</text>

<circle cx="195" cy="180" r="8" fill="#795548" stroke="#4E342E" stroke-width="1.5"/>
<text x="195" y="183" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle" font-weight="bold">3</text>
<text x="195" y="205" font-family="Arial,sans-serif" font-size="6" fill="#4E342E" text-anchor="middle">Черви</text>

<circle cx="250" cy="180" r="8" fill="#00BCD4" stroke="#00838F" stroke-width="1.5"/>
<text x="250" y="183" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle" font-weight="bold">4</text>
<text x="250" y="205" font-family="Arial,sans-serif" font-size="6" fill="#00838F" text-anchor="middle">Моллюски</text>

<circle cx="305" cy="180" r="8" fill="#F44336" stroke="#C62828" stroke-width="1.5"/>
<text x="305" y="183" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle" font-weight="bold">5</text>
<text x="305" y="205" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">Членистоногие</text>

<circle cx="360" cy="180" r="8" fill="#2196F3" stroke="#1565C0" stroke-width="1.5"/>
<text x="360" y="183" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle" font-weight="bold">6</text>
<text x="360" y="205" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">Рыбы</text>

<circle cx="400" cy="180" r="8" fill="#4CAF50" stroke="#2E7D32" stroke-width="1.5"/>
<text x="400" y="183" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle" font-weight="bold">7</text>
<text x="400" y="205" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Земноводные</text>

<circle cx="430" cy="140" r="8" fill="#8D6E63" stroke="#4E342E" stroke-width="1.5"/>
<text x="430" y="143" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle" font-weight="bold">8</text>
<text x="430" y="125" font-family="Arial,sans-serif" font-size="6" fill="#4E342E" text-anchor="middle">Пресмыкающиеся</text>

<circle cx="445" cy="100" r="8" fill="#64B5F6" stroke="#1565C0" stroke-width="1.5"/>
<text x="445" y="103" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle" font-weight="bold">9</text>
<text x="445" y="85" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">Птицы</text>

<circle cx="460" cy="60" r="8" fill="#A1887F" stroke="#4E342E" stroke-width="1.5"/>
<text x="460" y="63" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle" font-weight="bold">10</text>
<text x="460" y="45" font-family="Arial,sans-serif" font-size="6" fill="#4E342E" text-anchor="middle">Млекопитающие</text>

<!-- Increasing complexity arrow -->
<text x="30" y="100" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" transform="rotate(-90,30,130)">Усложнение</text>
'''+ibox(30,230,440,80,["Эволюция — историческое развитие органического мира","Движущие силы: наследственность, изменчивость, естественный отбор","Главные направления: усложнение строения, дифференциация органов","От одноклеточных к многоклеточным | От водных к наземным","Переходные формы: латимерия, ехидна, утконос","Искусственный отбор — основа селекции"])+ftr

# 32: Охрана животного мира
svgs[32] = hdr("Охрана животного мира",32)+'''
<!-- Red Book -->
<g transform="translate(120,170)">
<rect x="-35" y="-45" width="70" height="90" rx="5" fill="#E53935" stroke="#B71C1C" stroke-width="2"/>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">Красная</text>
<text x="0" y="-8" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">книга</text>
<!-- Animal silhouettes on book -->
<path d="M-15,10 Q-10,5 -5,10 Q0,5 5,10 Q10,5 15,10" stroke="white" stroke-width="1.5" fill="none"/>
<ellipse cx="0" cy="22" rx="8" ry="5" fill="none" stroke="white" stroke-width="1"/>
</g>
<!-- Nature reserve sign -->
<g transform="translate(300,170)">
<circle cx="0" cy="0" r="40" fill="#4CAF50" opacity="0.2" stroke="#2E7D32" stroke-width="2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Заповедник</text>
<!-- Tree -->
<path d="M0,10 L0,28" stroke="#5D4037" stroke-width="2"/>
<path d="M-12,10 L0,-5 L12,10Z" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
<!-- Bird -->
<path d="M-20,-15 Q-15,-20 -10,-15" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
<path d="M-10,-15 Q-5,-20 0,-15" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
</g>
<!-- Protection categories -->
<g transform="translate(430,100)">
<rect x="-40" y="-15" width="80" height="20" rx="3" fill="#FFCDD2" stroke="#C62828" stroke-width="1"/>
<text x="0" y="-1" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">Исчезающие</text>
<rect x="-40" y="10" width="80" height="20" rx="3" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
<text x="0" y="24" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">Сокращающиеся</text>
<rect x="-40" y="35" width="80" height="20" rx="3" fill="#FFF9C4" stroke="#F9A825" stroke-width="1"/>
<text x="0" y="49" font-family="Arial,sans-serif" font-size="6" fill="#F57F17" text-anchor="middle" font-weight="bold">Редкие</text>
<rect x="-40" y="60" width="80" height="20" rx="3" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="74" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Восстанавливаемые</text>
</g>
'''+ibox(30,270,440,45,["Красная книга — список редких и исчезающих видов","Заповедники — полная охрана природы | Заказники — частичная охрана","Национальные парки — охрана + туризм | Питомники — разведение редких видов","Причины: разрушение мест обитания, браконьерство, загрязнение среды"])+ftr

for i in range(23,33):
    with open(f"{OUT}/lesson{i}.svg","w") as f:
        f.write(svgs[i])
print("Lessons 23-32 done")
