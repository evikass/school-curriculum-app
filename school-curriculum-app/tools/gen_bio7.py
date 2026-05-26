#!/usr/bin/env python3
"""Generate all 32 biology grade 7 (Zoology) SVG lesson illustrations."""
import os

OUT = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade7/biology"
os.makedirs(OUT, exist_ok=True)

P = "#2E7D32"  # primary green
L = "#E8F5E9"  # light
M = "#C8E6C9"  # mid
A = "#4CAF50"  # accent

def hdr(title, num):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{L}"/><stop offset="100%" stop-color="{M}"/></linearGradient></defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="{P}" stroke-width="2.5"/>
<text x="250" y="30" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="{P}" text-anchor="middle">{title}</text>
<text x="250" y="46" font-family="Arial,sans-serif" font-size="10" fill="#888" text-anchor="middle">Биология 7 класс — Урок {num}</text>
<line x1="30" y1="52" x2="470" y2="52" stroke="{P}" stroke-width="1.5" opacity="0.25"/>
'''

ftr = '''
<rect x="10" y="325" width="480" height="20" rx="4" fill="#2E7D32" opacity="0.85"/>
<text x="250" y="339" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="white" font-weight="bold">Биология 7 класс</text>
</svg>'''

def ibox(x,y,w,h,lines,st=P):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="white" stroke="{st}" stroke-width="1" opacity="0.9"/>\n'
    for i,l in enumerate(lines):
        s += f'<text x="{x+w//2}" y="{y+14+i*12}" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">{l}</text>\n'
    return s

# 32 lessons data
svgs = {}

# 1
svgs[1] = hdr("Общая характеристика животного мира",1)+'''
<circle cx="250" cy="170" r="45" fill="#4CAF50" opacity="0.15" stroke="#2E7D32" stroke-width="2"/>
<text x="250" y="165" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle" font-weight="bold">Царство</text>
<text x="250" y="178" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle" font-weight="bold">Животные</text>
<g transform="translate(90,90)"><ellipse rx="38" ry="18" fill="#FF9800" opacity="0.2" stroke="#E65100" stroke-width="1.5"/><text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">Простейшие</text></g>
<g transform="translate(410,90)"><ellipse rx="38" ry="18" fill="#9C27B0" opacity="0.2" stroke="#7B1FA2" stroke-width="1.5"/><text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Черви</text></g>
<g transform="translate(90,250)"><ellipse rx="38" ry="18" fill="#00BCD4" opacity="0.2" stroke="#00838F" stroke-width="1.5"/><text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#00838F" text-anchor="middle" font-weight="bold">Моллюски</text></g>
<g transform="translate(410,250)"><ellipse rx="38" ry="18" fill="#F44336" opacity="0.2" stroke="#C62828" stroke-width="1.5"/><text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">Членистоногие</text></g>
<g transform="translate(250,85)"><ellipse rx="45" ry="18" fill="#2196F3" opacity="0.2" stroke="#1565C0" stroke-width="1.5"/><text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">Кишечнополостные</text></g>
<g transform="translate(250,265)"><ellipse rx="35" ry="18" fill="#795548" opacity="0.2" stroke="#4E342E" stroke-width="1.5"/><text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#4E342E" text-anchor="middle" font-weight="bold">Хордовые</text></g>
<line x1="125" y1="100" x2="210" y2="150" stroke="#999" stroke-width="0.8" stroke-dasharray="3,2"/>
<line x1="375" y1="100" x2="290" y2="150" stroke="#999" stroke-width="0.8" stroke-dasharray="3,2"/>
<line x1="125" y1="245" x2="210" y2="195" stroke="#999" stroke-width="0.8" stroke-dasharray="3,2"/>
<line x1="375" y1="245" x2="290" y2="195" stroke="#999" stroke-width="0.8" stroke-dasharray="3,2"/>
'''+ibox(50,290,400,28,["Гетеротрофы | Нет клеточной стенки | Ограниченный рост | Активное движение | Более 2 млн видов"])+ftr

# 2
svgs[2] = hdr("Классификация животных и методы зоологии",2)+'''
<g transform="translate(30,70)">
<rect x="0" y="0" width="180" height="18" rx="3" fill="#2E7D32" opacity="0.8"/>
<text x="90" y="13" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle" font-weight="bold">Царство Животные</text>
<rect x="10" y="22" width="160" height="16" rx="3" fill="#388E3C" opacity="0.7"/>
<text x="90" y="34" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">Тип Хордовые</text>
<rect x="20" y="42" width="140" height="16" rx="3" fill="#43A047" opacity="0.6"/>
<text x="90" y="54" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">Класс Млекопитающие</text>
<rect x="30" y="62" width="120" height="16" rx="3" fill="#4CAF50" opacity="0.5"/>
<text x="90" y="74" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">Отряд Хищные</text>
<rect x="40" y="82" width="100" height="16" rx="3" fill="#66BB6A" opacity="0.5"/>
<text x="90" y="94" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Семейство Псовые</text>
<rect x="50" y="102" width="80" height="16" rx="3" fill="#81C784" opacity="0.5"/>
<text x="90" y="114" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Род Волки</text>
<rect x="60" y="122" width="60" height="16" rx="3" fill="#A5D6A7" opacity="0.5" stroke="#2E7D32" stroke-width="1"/>
<text x="90" y="134" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Вид</text>
</g>
<g transform="translate(250,70)">
<text x="110" y="10" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Методы зоологии</text>
<g transform="translate(40,45)"><circle cx="0" cy="0" r="14" fill="none" stroke="#FF9800" stroke-width="2"/><line x1="10" y1="10" x2="20" y2="20" stroke="#FF9800" stroke-width="2.5"/><text x="0" y="28" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Наблюдение</text></g>
<g transform="translate(130,45)"><rect x="-5" y="-13" width="10" height="22" rx="2" fill="none" stroke="#E53935" stroke-width="1.5"/><rect x="-4" y="0" width="8" height="7" rx="1" fill="#E53935" opacity="0.3"/><text x="0" y="23" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Эксперимент</text></g>
<g transform="translate(220,45)"><path d="M-8,4 Q-6,-8 0,-10 Q6,-8 8,4 L6,8 Q0,10 -6,8Z" fill="none" stroke="#795548" stroke-width="1.5"/><text x="0" y="23" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Сравнение</text></g>
<g transform="translate(85,110)"><path d="M-18,-8 Q-8,-13 2,-8 Q12,-3 18,-8" stroke="#9C27B0" stroke-width="1.5" fill="none"/><path d="M-18,-1 Q-8,-6 2,-1 Q12,4 18,-1" stroke="#9C27B0" stroke-width="1.5" fill="none"/><text x="0" y="15" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Молекулярный</text></g>
<g transform="translate(185,110)"><ellipse cx="0" cy="-4" rx="14" ry="9" fill="#D7CCC8" stroke="#795548" stroke-width="1.5"/><path d="M-7,-7 Q0,-2 7,-7" stroke="#5D4037" stroke-width="1" fill="none"/><text x="0" y="15" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Палеонтология</text></g>
</g>
<g transform="translate(380,210)"><circle cx="0" cy="-12" r="18" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/><text x="0" y="-14" font-family="Arial,sans-serif" font-size="7" fill="#F57F17" text-anchor="middle" font-weight="bold">К.Линней</text><text x="0" y="-2" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">1707-1778</text><text x="0" y="15" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Бинарная</text><text x="0" y="24" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">номенклатура</text></g>
'''+ftr

# 3
svgs[3] = hdr("Общая характеристика простейших",3)+'''
<g transform="translate(85,155)">
<path d="M-22,8 Q-32,-3 -18,-18 Q-8,-25 5,-22 Q18,-25 22,-12 Q30,-3 22,8 Q12,20 0,18 Q-12,20 -22,8Z" fill="#B2DFDB" stroke="#00897B" stroke-width="2"/>
<ellipse cx="2" cy="-2" rx="7" ry="5" fill="#80CBC4" stroke="#00695C" stroke-width="1.5"/>
<circle cx="2" cy="-2" r="3" fill="#4DB6AC"/>
<path d="M-26,0 Q-40,5 -34,-5" fill="#B2DFDB" stroke="#00897B" stroke-width="1.5"/>
<path d="M18,-18 Q28,-28 22,-12" fill="#B2DFDB" stroke="#00897B" stroke-width="1.5"/>
<circle cx="14" cy="8" r="4" fill="#E0F7FA" stroke="#00BCD4" stroke-width="1"/>
<circle cx="-8" cy="8" r="5" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1" opacity="0.6"/>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Амёба</text>
<text x="0" y="52" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Ложноножки</text>
</g>
<g transform="translate(250,155)">
<ellipse cx="0" cy="0" rx="28" ry="11" fill="#C8E6C9" stroke="#388E3C" stroke-width="2"/>
<path d="M26,-2 Q42,-14 48,-24" stroke="#388E3C" stroke-width="1.5" fill="none"/>
<circle cx="18" cy="-3" r="3" fill="#F44336" opacity="0.7"/>
<ellipse cx="-4" cy="-3" rx="5" ry="2.5" fill="#66BB6A" opacity="0.6"/>
<ellipse cx="5" cy="4" rx="4" ry="2" fill="#66BB6A" opacity="0.6"/>
<circle cx="-8" cy="0" r="4" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Эвглена</text>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Жгутик + хлоропласты</text>
</g>
<g transform="translate(415,155)">
<ellipse cx="0" cy="0" rx="16" ry="32" fill="#E1BEE7" stroke="#7B1FA2" stroke-width="2"/>
<line x1="-16" y1="-18" x2="-22" y2="-20" stroke="#9C27B0" stroke-width="0.7"/>
<line x1="-17" y1="-8" x2="-23" y2="-9" stroke="#9C27B0" stroke-width="0.7"/>
<line x1="-17" y1="2" x2="-23" y2="2" stroke="#9C27B0" stroke-width="0.7"/>
<line x1="-16" y1="12" x2="-22" y2="13" stroke="#9C27B0" stroke-width="0.7"/>
<line x1="16" y1="-18" x2="22" y2="-20" stroke="#9C27B0" stroke-width="0.7"/>
<line x1="17" y1="-8" x2="23" y2="-9" stroke="#9C27B0" stroke-width="0.7"/>
<line x1="17" y1="2" x2="23" y2="2" stroke="#9C27B0" stroke-width="0.7"/>
<line x1="16" y1="12" x2="22" y2="13" stroke="#9C27B0" stroke-width="0.7"/>
<path d="M-8,-12 Q-13,0 -6,12" stroke="#6A1B9A" stroke-width="1.5" fill="none"/>
<ellipse cx="2" cy="-4" rx="7" ry="4" fill="#CE93D8" stroke="#6A1B9A" stroke-width="1"/>
<circle cx="4" cy="3" r="2.5" fill="#AB47BC" stroke="#6A1B9A" stroke-width="1"/>
<text x="0" y="46" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Инфузория</text>
<text x="0" y="56" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Реснички</text>
</g>
'''+ibox(40,235,420,45,["Общие признаки: одна клетка = целый организм | Эукариоты","Сократительная вакуоль | Инцистирование | Гетеротрофы или миксотрофы","Органоиды движения: ложноножки, жгутики, реснички"])+ftr

# 4
svgs[4] = hdr("Общая характеристика кишечнополостных",4)+'''
<g transform="translate(160,180)">
<path d="M-13,-55 Q-16,-18 -18,28 Q-13,45 0,48 Q13,45 18,28 Q16,-18 13,-55Z" fill="#FFCDD2" stroke="#E53935" stroke-width="2"/>
<path d="M-13,-55 Q-30,-72 -26,-85" stroke="#EF5350" stroke-width="2" fill="none"/>
<path d="M-6,-57 Q-16,-78 -12,-90" stroke="#EF5350" stroke-width="2" fill="none"/>
<path d="M0,-58 Q0,-82 0,-95" stroke="#EF5350" stroke-width="2" fill="none"/>
<path d="M6,-57 Q16,-78 12,-90" stroke="#EF5350" stroke-width="2" fill="none"/>
<path d="M13,-55 Q30,-72 26,-85" stroke="#EF5350" stroke-width="2" fill="none"/>
<ellipse cx="0" cy="-50" rx="7" ry="4" fill="#FFCDD2" stroke="#C62828" stroke-width="1.5"/>
<g transform="translate(16,2)"><path d="M0,0 Q4,-12 2,-22 Q0,-26 -2,-22 Q-4,-12 0,0" fill="#FFCDD2" stroke="#E53935" stroke-width="1.2"/><path d="M2,-22 Q8,-28 6,-33" stroke="#EF5350" stroke-width="0.8" fill="none"/><path d="M-2,-22 Q-8,-28 -6,-33" stroke="#EF5350" stroke-width="0.8" fill="none"/></g>
<text x="0" y="62" font-family="Arial,sans-serif" font-size="8" fill="#C62828" text-anchor="middle" font-weight="bold">Гидра</text>
</g>
<g transform="translate(380,175)">
<rect x="-55" y="-65" width="110" height="130" rx="5" fill="white" stroke="#E53935" stroke-width="1.5"/>
<text x="0" y="-50" font-family="Arial,sans-serif" font-size="8" fill="#C62828" text-anchor="middle" font-weight="bold">Стенка тела</text>
<rect x="-38" y="-40" width="76" height="20" rx="3" fill="#FFCDD2" stroke="#E53935" stroke-width="1"/>
<text x="0" y="-26" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle">Эктодерма</text>
<rect x="-38" y="-17" width="76" height="14" rx="3" fill="#FFECB3" stroke="#FF8F00" stroke-width="1"/>
<text x="0" y="-6" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle">Мезоглея</text>
<rect x="-38" y="0" width="76" height="20" rx="3" fill="#FFCDD2" stroke="#E53935" stroke-width="1"/>
<text x="0" y="14" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle">Энтодерма</text>
<g transform="translate(0,38)"><circle cx="0" cy="0" r="5" fill="#FFAB91" stroke="#E53935" stroke-width="1"/><line x1="0" y1="0" x2="7" y2="-7" stroke="#E53935" stroke-width="0.8"/><text x="0" y="15" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">Стрекательная клетка</text></g>
</g>
'''+ibox(30,270,440,40,["Двухслойные: эктодерма + энтодерма | Радиальная симметрия","Кишечная полость | Стрекательные клетки | Почкование"])+ftr

# 5
svgs[5] = hdr("Многообразие кишечнополостных",5)+'''
<g transform="translate(85,165)">
<path d="M-9,-45 Q-10,-8 -12,22 Q-9,36 0,38 Q9,36 12,22 Q10,-8 9,-45Z" fill="#FFCDD2" stroke="#E53935" stroke-width="1.5"/>
<path d="M-9,-45 Q-22,-58 -18,-68" stroke="#EF5350" stroke-width="1.5" fill="none"/>
<path d="M0,-47 Q0,-65 0,-72" stroke="#EF5350" stroke-width="1.5" fill="none"/>
<path d="M9,-45 Q22,-58 18,-68" stroke="#EF5350" stroke-width="1.5" fill="none"/>
<text x="0" y="54" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Гидроидные</text>
</g>
<g transform="translate(250,165)">
<path d="M-35,8 Q-40,-22 -26,-40 Q0,-52 26,-40 Q40,-22 35,8 Q18,12 0,10 Q-18,12 -35,8Z" fill="#E1BEE7" stroke="#7B1FA2" stroke-width="2"/>
<path d="M-30,8 Q-35,30 -25,48" stroke="#9C27B0" stroke-width="1.5" fill="none"/>
<path d="M0,12 Q0,38 4,55" stroke="#9C27B0" stroke-width="1.5" fill="none"/>
<path d="M30,8 Q35,30 25,48" stroke="#9C27B0" stroke-width="1.5" fill="none"/>
<path d="M-10,10 Q-15,28 -8,40" stroke="#6A1B9A" stroke-width="2" fill="none"/>
<path d="M10,10 Q15,28 8,40" stroke="#6A1B9A" stroke-width="2" fill="none"/>
<text x="0" y="70" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Сцифоидные (Медуза)</text>
</g>
<g transform="translate(415,165)">
<path d="M-26,30 Q-30,8 -22,-8 Q-12,-22 0,-26 Q12,-22 22,-8 Q30,8 26,30Z" fill="#FFCC80" stroke="#E65100" stroke-width="2"/>
<path d="M-22,-8 Q-35,-25 -26,-40" stroke="#FF9800" stroke-width="2" fill="none"/>
<path d="M0,-26 Q0,-48 4,-58" stroke="#FF9800" stroke-width="2" fill="none"/>
<path d="M22,-8 Q35,-25 26,-40" stroke="#FF9800" stroke-width="2" fill="none"/>
<text x="0" y="48" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Кораллы</text>
<text x="0" y="58" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Актинии</text>
</g>
'''+ibox(30,245,440,40,["Общие: двухслойные | Радиальная симметрия | Стрекательные клетки","Два поколения: полип (бесполое) и медуза (половое)"])+ftr

# 6
svgs[6] = hdr("Плоские черви",6)+'''
<g transform="translate(120,150)">
<path d="M-30,0 Q-40,-12 -30,-10 Q-20,-12 -12,0 Q0,8 18,4 Q30,0 40,-4 Q44,-8 40,-4 Q30,4 18,8 Q0,12 -12,4 Q-20,12 -30,10 Q-40,12 -30,0Z" fill="#A5D6A7" stroke="#2E7D32" stroke-width="2"/>
<path d="M-30,0 L-42,-8 L-42,8Z" fill="#81C784" stroke="#2E7D32" stroke-width="1.5"/>
<circle cx="-36" cy="-3" r="2.5" fill="#333"/><circle cx="-36" cy="3" r="2.5" fill="#333"/>
<ellipse cx="0" cy="0" rx="4" ry="7" fill="#66BB6A" stroke="#1B5E20" stroke-width="1"/>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Планария</text>
<text x="0" y="31" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Свободноживущий</text>
</g>
<g transform="translate(300,150)">
<path d="M-18,-22 Q-26,-12 -22,0 Q-26,12 -18,22 Q0,30 18,22 Q26,12 22,0 Q26,-12 18,-22 Q0,-30 -18,-22Z" fill="#FFCC80" stroke="#E65100" stroke-width="2"/>
<circle cx="-16" cy="-12" r="5" fill="#FFE0B2" stroke="#BF360C" stroke-width="1.5"/>
<circle cx="-8" cy="0" r="4" fill="#FFE0B2" stroke="#BF360C" stroke-width="1.5"/>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Сосальщик</text>
<text x="0" y="47" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Паразит, 2 присоски</text>
</g>
<g transform="translate(430,150)">
<circle cx="0" cy="-18" r="9" fill="#FFECB3" stroke="#F57F17" stroke-width="1.5"/>
<circle cx="-4" cy="-26" r="1.5" fill="#F57F17"/><circle cx="4" cy="-26" r="1.5" fill="#F57F17"/>
<circle cx="-4" cy="-16" r="2.5" fill="#FFE082" stroke="#F57F17" stroke-width="0.8"/>
<circle cx="4" cy="-16" r="2.5" fill="#FFE082" stroke="#F57F17" stroke-width="0.8"/>
<rect x="-7" y="-7" width="14" height="7" rx="2" fill="#FFF9C4" stroke="#F9A825" stroke-width="1"/>
<rect x="-7" y="2" width="14" height="7" rx="2" fill="#FFF9C4" stroke="#F9A825" stroke-width="1"/>
<rect x="-8" y="11" width="16" height="9" rx="2" fill="#FFF9C4" stroke="#F9A825" stroke-width="1"/>
<text x="0" y="32" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Бычий цепень</text>
<text x="0" y="41" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Паразит, нет ЖКТ</text>
</g>
'''+ibox(30,215,440,45,["Трёхслойные: эктодерма, мезодерма, энтодерма | Двусторонняя симметрия","Кожно-мускульный мешок | Паразиты: присоски, крючья | Нет пищеварения у цепней","Свободноживущие: планария | Паразиты: сосальщики, цепни"])+ftr

# 7
svgs[7] = hdr("Круглые черви",7)+'''
<g transform="translate(180,170)">
<path d="M-65,0 Q-75,-7 -65,-9 Q-35,-12 0,-12 Q35,-12 65,-9 Q75,-7 65,0 Q75,7 65,9 Q35,12 0,12 Q-35,12 -65,9 Q-75,7 -65,0Z" fill="#FFECB3" stroke="#F57F17" stroke-width="2"/>
<ellipse cx="-70" cy="0" rx="7" ry="5" fill="#FFF9C4" stroke="#F57F17" stroke-width="1.5"/>
<circle cx="-74" cy="0" r="1.5" fill="#F57F17"/>
<path d="M65,0 Q75,0 80,-4 Q82,-8 78,-10" stroke="#F57F17" stroke-width="2" fill="none"/>
<line x1="-60" y1="0" x2="60" y2="0" stroke="#FFE082" stroke-width="1.5" stroke-dasharray="4,2"/>
<text x="0" y="26" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Аскарида</text>
</g>
<g transform="translate(390,165)">
<circle cx="0" cy="0" r="42" fill="#FFF9C4" stroke="#F57F17" stroke-width="2"/>
<circle cx="0" cy="0" r="38" fill="none" stroke="#FFB300" stroke-width="2"/>
<circle cx="0" cy="0" r="30" fill="#FFECB3" stroke="#F57F17" stroke-width="0.8" stroke-dasharray="3,2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#F57F17" text-anchor="middle">Первичная</text>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="6" fill="#F57F17" text-anchor="middle">полость</text>
<ellipse cx="0" cy="8" rx="9" ry="6" fill="#FFE082" stroke="#F57F17" stroke-width="1"/>
<text x="0" y="50" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Поперечный срез</text>
</g>
'''+ibox(30,260,440,45,["Цилиндрическое тело | Кутикула | Первичная полость (псевдоцель)","Сквозной кишечник (рот + анальное отверстие) | Раздельнополые","Аскарида, острица, трихинелла — паразиты человека и животных"])+ftr

# 8
svgs[8] = hdr("Кольчатые черви",8)+'''
<g transform="translate(250,145)">
<path d="M-95,-9 Q-105,-4 -100,0 Q-105,4 -95,9 L95,9 Q105,4 100,0 Q105,-4 95,-9Z" fill="#D7CCC8" stroke="#5D4037" stroke-width="2"/>
<line x1="-75" y1="-9" x2="-75" y2="9" stroke="#8D6E63" stroke-width="0.8"/>
<line x1="-55" y1="-9" x2="-55" y2="9" stroke="#8D6E63" stroke-width="0.8"/>
<line x1="-35" y1="-9" x2="-35" y2="9" stroke="#8D6E63" stroke-width="0.8"/>
<line x1="-15" y1="-9" x2="-15" y2="9" stroke="#8D6E63" stroke-width="0.8"/>
<line x1="5" y1="-9" x2="5" y2="9" stroke="#8D6E63" stroke-width="0.8"/>
<line x1="25" y1="-9" x2="25" y2="9" stroke="#8D6E63" stroke-width="0.8"/>
<line x1="45" y1="-9" x2="45" y2="9" stroke="#8D6E63" stroke-width="0.8"/>
<line x1="65" y1="-9" x2="65" y2="9" stroke="#8D6E63" stroke-width="0.8"/>
<line x1="85" y1="-9" x2="85" y2="9" stroke="#8D6E63" stroke-width="0.8"/>
<rect x="-12" y="-11" width="32" height="22" rx="5" fill="#BCAAA4" stroke="#5D4037" stroke-width="1.5"/>
<text x="4" y="3" font-family="Arial,sans-serif" font-size="5" fill="#3E2723" text-anchor="middle">Поясок</text>
<line x1="-65" y1="9" x2="-67" y2="15" stroke="#5D4037" stroke-width="1"/>
<line x1="-45" y1="9" x2="-47" y2="15" stroke="#5D4037" stroke-width="1"/>
<line x1="35" y1="9" x2="33" y2="15" stroke="#5D4037" stroke-width="1"/>
<line x1="55" y1="9" x2="53" y2="15" stroke="#5D4037" stroke-width="1"/>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Дождевой червь</text>
</g>
<g transform="translate(120,245)">
<circle cx="0" cy="0" r="28" fill="#EFEBE9" stroke="#5D4037" stroke-width="1.5"/>
<circle cx="0" cy="0" r="22" fill="#D7CCC8" stroke="#8D6E63" stroke-width="1"/>
<circle cx="0" cy="0" r="12" fill="#BCAAA4" stroke="#8D6E63" stroke-width="0.8"/>
<ellipse cx="0" cy="0" rx="6" ry="4" fill="#A1887F" stroke="#5D4037" stroke-width="1"/>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Вторичная полость</text>
</g>
<g transform="translate(400,245)">
<path d="M-35,-4 Q-42,-2 -38,0 Q-42,2 -35,4 L35,4 Q42,2 38,0 Q42,-2 35,-4Z" fill="#B2DFDB" stroke="#00695C" stroke-width="1.5"/>
<path d="M-25,-4 L-28,-13" stroke="#00897B" stroke-width="1"/><path d="M-25,4 L-28,13" stroke="#00897B" stroke-width="1"/>
<path d="M-8,-4 L-11,-13" stroke="#00897B" stroke-width="1"/><path d="M-8,4 L-11,13" stroke="#00897B" stroke-width="1"/>
<path d="M8,-4 L5,-13" stroke="#00897B" stroke-width="1"/><path d="M8,4 L5,13" stroke="#00897B" stroke-width="1"/>
<path d="M25,-4 L22,-13" stroke="#00897B" stroke-width="1"/><path d="M25,4 L22,13" stroke="#00897B" stroke-width="1"/>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Нереис (параподии)</text>
</g>
'''+ibox(30,280,440,28,["Вторичная полость тела | Сегментация | Щетинки или параподии | Замкнутая кровеносная система"])+ftr

# 9
svgs[9] = hdr("Общая характеристика моллюсков",9)+'''
<g transform="translate(170,175)">
<path d="M-45,28 Q-55,-8 -35,-35 Q-18,-52 0,-52 Q18,-52 35,-35 Q55,-8 45,28Z" fill="#FFE0B2" stroke="#E65100" stroke-width="2"/>
<path d="M-38,22 Q-45,-5 -28,-28 Q-12,-42 0,-42 Q12,-42 28,-28 Q45,-5 38,22" fill="none" stroke="#FF8F00" stroke-width="0.8" opacity="0.5"/>
<path d="M-40,28 Q-45,8 -32,-22 Q-15,-38 5,-38 Q22,-38 35,-22 Q48,8 40,28" fill="#FFECB3" stroke="#FFB300" stroke-width="1.5" opacity="0.6"/>
<path d="M-30,28 Q-35,40 -20,45 Q0,48 20,45 Q35,40 30,28Z" fill="#FFCC80" stroke="#E65100" stroke-width="1.5"/>
<line x1="-15" y1="-48" x2="-22" y2="-62" stroke="#BF360C" stroke-width="1.5"/>
<line x1="-5" y1="-50" x2="-12" y2="-62" stroke="#BF360C" stroke-width="1.5"/>
<circle cx="-22" cy="-63" r="1.5" fill="#333"/><circle cx="-12" cy="-63" r="1.5" fill="#333"/>
<text x="0" y="58" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">Раковина + нога</text>
</g>
<g transform="translate(400,170)">
<rect x="-55" y="-65" width="110" height="130" rx="5" fill="white" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="-50" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">Органы</text>
<path d="M0,-30 Q-4,-35 -2,-30 Q-4,-25 0,-20 Q4,-25 2,-30 Q4,-35 0,-30Z" fill="#E53935" stroke="#C62828" stroke-width="1"/><text x="20" y="-28" font-family="Arial,sans-serif" font-size="5" fill="#333">Сердце</text>
<rect x="10" y="-40" width="14" height="8" rx="2" fill="#A5D6A7" stroke="#2E7D32" stroke-width="0.8"/><text x="35" y="-33" font-family="Arial,sans-serif" font-size="5" fill="#333">Почка</text>
<ellipse cx="-8" y="-8" rx="10" ry="5" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/><text x="15" y="-6" font-family="Arial,sans-serif" font-size="5" fill="#333">Печень</text>
<ellipse cx="-18" cy="15" rx="9" ry="7" fill="#BBDEFB" stroke="#1565C0" stroke-width="0.8"/><text x="10" y="18" font-family="Arial,sans-serif" font-size="5" fill="#333">Жабра</text>
<ellipse cx="5" cy="30" rx="9" ry="5" fill="#F8BBD0" stroke="#C2185B" stroke-width="0.8"/><text x="28" y="33" font-family="Arial,sans-serif" font-size="5" fill="#333">Половая</text>
<circle cx="-22" cy="45" r="4" fill="#CE93D8" stroke="#7B1FA2" stroke-width="0.8"/><circle cx="15" cy="45" r="4" fill="#CE93D8" stroke="#7B1FA2" stroke-width="0.8"/>
<line x1="-18" y1="45" x2="11" y2="45" stroke="#7B1FA2" stroke-width="0.8"/><text x="-3" y="55" font-family="Arial,sans-serif" font-size="5" fill="#333">Нервные узлы</text>
</g>
'''+ibox(30,275,440,30,["Несегментированное тело | Раковина (известковая) | Мускулистая нога | Мантия","Трёхкамерное сердце | Незамкнутая кровеносная система | Вторичная полость"])+ftr

# 10
svgs[10] = hdr("Многообразие и значение моллюсков",10)+'''
<g transform="translate(85,165)">
<path d="M-12,22 Q-25,8 -20,-8 Q-16,-22 -8,-26 Q0,-30 8,-26 Q16,-18 12,-4 Q8,4 4,8" fill="#FFCC80" stroke="#E65100" stroke-width="2"/>
<path d="M-12,22 Q-20,28 -15,32 Q0,36 18,32 Q22,28 12,22" fill="#FFE0B2" stroke="#BF360C" stroke-width="1.5"/>
<circle cx="-18" cy="18" r="5" fill="#FFE0B2" stroke="#BF360C" stroke-width="1"/>
<line x1="-20" y1="14" x2="-24" y2="5" stroke="#BF360C" stroke-width="1.2"/>
<line x1="-16" y1="14" x2="-12" y2="5" stroke="#BF360C" stroke-width="1.2"/>
<text x="0" y="46" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Брюхоногие</text>
</g>
<g transform="translate(250,165)">
<path d="M-4,-32 Q-35,-28 -38,0 Q-35,28 -4,32Z" fill="#FFECB3" stroke="#F57F17" stroke-width="2"/>
<path d="M4,-32 Q35,-28 38,0 Q35,28 4,32Z" fill="#FFF9C4" stroke="#F57F17" stroke-width="2"/>
<line x1="0" y1="-32" x2="0" y2="32" stroke="#F57F17" stroke-width="2"/>
<rect x="-7" y="-42" width="5" height="10" rx="2" fill="#FFE082" stroke="#F57F17" stroke-width="1"/>
<rect x="2" y="-42" width="5" height="10" rx="2" fill="#FFE082" stroke="#F57F17" stroke-width="1"/>
<text x="0" y="48" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Двустворчатые</text>
</g>
<g transform="translate(415,165)">
<path d="M-12,-35 Q-22,-18 -18,8 Q-12,22 0,26 Q12,22 18,8 Q22,-18 12,-35Z" fill="#E1BEE7" stroke="#7B1FA2" stroke-width="2"/>
<circle cx="0" cy="-40" r="13" fill="#CE93D8" stroke="#7B1FA2" stroke-width="1.5"/>
<circle cx="-8" cy="-42" r="4" fill="#F3E5F5" stroke="#4A148C" stroke-width="1"/><circle cx="-8" cy="-42" r="1.5" fill="#333"/>
<circle cx="8" cy="-42" r="4" fill="#F3E5F5" stroke="#4A148C" stroke-width="1"/><circle cx="8" cy="-42" r="1.5" fill="#333"/>
<path d="M-10,26 Q-16,40 -12,50" stroke="#9C27B0" stroke-width="1.5" fill="none"/>
<path d="M0,28 Q0,42 3,52" stroke="#9C27B0" stroke-width="1.5" fill="none"/>
<path d="M10,26 Q16,40 12,50" stroke="#9C27B0" stroke-width="1.5" fill="none"/>
<text x="0" y="65" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Головоногие</text>
</g>
'''+ibox(30,255,440,45,["Брюхоногие: улитки, слизни — 1 раковина, спиральное закручивание","Двустворчатые: мидии, устрицы — 2 створки, фильтраторы, нет головы","Головоногие: кальмары, осьминоги — щупальца, сложные глаза, реактивное движение"])+ftr

print("Writing lessons 1-10...")
for i in range(1,11):
    with open(f"{OUT}/lesson{i}.svg","w") as f:
        f.write(svgs[i])
