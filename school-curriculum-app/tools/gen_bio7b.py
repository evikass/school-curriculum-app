#!/usr/bin/env python3
"""Generate biology grade 7 lessons 11-22"""
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

# 11: Общая характеристика членистоногих
svgs[11] = hdr("Общая характеристика членистоногих",11)+'''
<g transform="translate(140,165)">
<path d="M-45,-18 L45,-18 L45,18 L-45,18Z" fill="#FFCC80" stroke="#E65100" stroke-width="2" rx="5"/>
<path d="M-45,-18 Q0,-28 45,-18" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
<line x1="-22" y1="-20" x2="-22" y2="18" stroke="#BF360C" stroke-width="0.8"/>
<line x1="0" y1="-22" x2="0" y2="18" stroke="#BF360C" stroke-width="0.8"/>
<line x1="22" y1="-20" x2="22" y2="18" stroke="#BF360C" stroke-width="0.8"/>
<path d="M-22,18 L-26,32 L-18,40" stroke="#BF360C" stroke-width="2" fill="none"/>
<path d="M0,18 L-4,32 L4,40" stroke="#BF360C" stroke-width="2" fill="none"/>
<path d="M22,18 L18,32 L26,40" stroke="#BF360C" stroke-width="2" fill="none"/>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle" font-weight="bold">Хитин</text>
<text x="0" y="55" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Членистые конечности</text>
</g>
<g transform="translate(400,120)">
<text x="0" y="0" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">3 класса</text>
<g transform="translate(-55,22)"><rect x="-32" y="-9" width="64" height="20" rx="10" fill="#2196F3" opacity="0.25" stroke="#1565C0" stroke-width="1.5"/><text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">Ракообразные</text></g>
<g transform="translate(55,22)"><rect x="-32" y="-9" width="64" height="20" rx="10" fill="#9C27B0" opacity="0.25" stroke="#7B1FA2" stroke-width="1.5"/><text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Паукообразные</text></g>
<g transform="translate(0,50)"><rect x="-28" y="-9" width="56" height="20" rx="10" fill="#4CAF50" opacity="0.25" stroke="#2E7D32" stroke-width="1.5"/><text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Насекомые</text></g>
</g>
<g transform="translate(380,240)">
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Линька</text>
<path d="M-30,-12 L-10,-12 L-10,12 L-30,12Z" fill="none" stroke="#BF360C" stroke-width="1.5" stroke-dasharray="3,2"/>
<text x="-20" y="22" font-family="Arial,sans-serif" font-size="5" fill="#BF360C" text-anchor="middle">Старый</text>
<path d="M-5,0 L5,0" stroke="#2E7D32" stroke-width="1.5"/><path d="M5,0 L2,-3 M5,0 L2,3" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
<path d="M10,-15 L30,-15 L30,15 L10,15Z" fill="#FFECB3" stroke="#E65100" stroke-width="1.5"/>
<text x="20" y="22" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">Новый</text>
</g>
'''+ibox(30,290,440,22,["Хитиновый покров | Членистые конечности | Сегментация | Линька | Более 1,5 млн видов"])+ftr

# 12: Ракообразные
svgs[12] = hdr("Ракообразные",12)+'''
<g transform="translate(200,170)">
<ellipse cx="0" cy="-12" rx="32" ry="22" fill="#E53935" opacity="0.7" stroke="#B71C1C" stroke-width="2"/>
<path d="M0,-35 L-4,-30 L4,-30Z" fill="#C62828" stroke="#B71C1C" stroke-width="1"/>
<circle cx="-12" cy="-26" r="3.5" fill="#333" stroke="#000" stroke-width="0.5"/>
<circle cx="12" cy="-26" r="3.5" fill="#333" stroke="#000" stroke-width="0.5"/>
<g transform="translate(-36,-8)"><path d="M0,0 L-13,-8 L-22,-4 L-17,4 L-8,2Z" fill="#EF5350" stroke="#B71C1C" stroke-width="1.5"/><path d="M0,0 L-13,8 L-22,4 L-17,-4 L-8,-2Z" fill="#EF5350" stroke="#B71C1C" stroke-width="1.5"/></g>
<g transform="translate(36,-8)"><path d="M0,0 L13,-8 L22,-4 L17,4 L8,2Z" fill="#EF5350" stroke="#B71C1C" stroke-width="1.5"/><path d="M0,0 L13,8 L22,4 L17,-4 L8,-2Z" fill="#EF5350" stroke="#B71C1C" stroke-width="1.5"/></g>
<path d="M-18,8 L-20,16 L-16,22 L-12,26 L-6,28 L0,30 L6,28 L12,26 L16,22 L20,16 L18,8" fill="#C62828" stroke="#B71C1C" stroke-width="1.5"/>
<line x1="-12" y1="12" x2="12" y2="12" stroke="#B71C1C" stroke-width="0.5"/>
<line x1="-14" y1="18" x2="14" y2="18" stroke="#B71C1C" stroke-width="0.5"/>
<line x1="-12" y1="24" x2="12" y2="24" stroke="#B71C1C" stroke-width="0.5"/>
<path d="M-26,4 L-36,16" stroke="#C62828" stroke-width="1.5"/>
<path d="M-24,8 L-34,22" stroke="#C62828" stroke-width="1.5"/>
<path d="M26,4 L36,16" stroke="#C62828" stroke-width="1.5"/>
<path d="M24,8 L34,22" stroke="#C62828" stroke-width="1.5"/>
<path d="M-8,-34 Q-20,-48 -16,-55" stroke="#C62828" stroke-width="1.5" fill="none"/>
<path d="M8,-34 Q20,-48 16,-55" stroke="#C62828" stroke-width="1.5" fill="none"/>
</g>
<g transform="translate(420,220)">
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">Жабры</text>
<path d="M-12,-12 Q-16,-4 -12,4 Q-8,8 -12,12" stroke="#1565C0" stroke-width="1.5" fill="none"/>
<path d="M-2,-12 Q-6,-4 -2,4 Q2,8 -2,12" stroke="#1565C0" stroke-width="1.5" fill="none"/>
<path d="M8,-12 Q4,-4 8,4 Q12,8 8,12" stroke="#1565C0" stroke-width="1.5" fill="none"/>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Под карапаксом</text>
</g>
'''+ibox(30,290,440,22,["5 пар ходильных ног | Клешни | Жабры | Зелёные железы | Антенны и антеннулы"])+ftr

# 13: Паукообразные
svgs[13] = hdr("Паукообразные",13)+'''
<g transform="translate(250,165)">
<line x1="0" y1="-70" x2="0" y2="70" stroke="#BDBDBD" stroke-width="0.5"/>
<line x1="-70" y1="0" x2="70" y2="0" stroke="#BDBDBD" stroke-width="0.5"/>
<line x1="-50" y1="-50" x2="50" y2="50" stroke="#BDBDBD" stroke-width="0.5"/>
<line x1="50" y1="-50" x2="-50" y2="50" stroke="#BDBDBD" stroke-width="0.5"/>
<path d="M9,0 Q9,9 0,9 Q-9,9 -9,0 Q-9,-9 0,-9 Q18,-9 18,9 Q18,27 0,27 Q-27,27 -27,0 Q-27,-27 0,-27 Q36,-27 36,9 Q36,45 0,45 Q-45,45 -45,0 Q-45,-45 0,-45" stroke="#BDBDBD" stroke-width="0.5" fill="none"/>
<ellipse cx="8" cy="-12" rx="7" ry="5" fill="#5D4037" stroke="#3E2723" stroke-width="1.5"/>
<ellipse cx="8" cy="-4" rx="5" ry="4" fill="#795548" stroke="#3E2723" stroke-width="1.5"/>
<path d="M2,-15 Q-8,-24 -12,-28" stroke="#5D4037" stroke-width="1" fill="none"/>
<path d="M3,-12 Q-10,-14 -16,-12" stroke="#5D4037" stroke-width="1" fill="none"/>
<path d="M3,-4 Q-10,-1 -14,5" stroke="#5D4037" stroke-width="1" fill="none"/>
<path d="M13,-15 Q24,-24 28,-28" stroke="#5D4037" stroke-width="1" fill="none"/>
<path d="M13,-12 Q26,-14 32,-12" stroke="#5D4037" stroke-width="1" fill="none"/>
<path d="M13,-4 Q26,-1 30,5" stroke="#5D4037" stroke-width="1" fill="none"/>
</g>
<g transform="translate(85,265)">
<ellipse cx="0" cy="0" rx="10" ry="7" fill="#795548" stroke="#3E2723" stroke-width="1"/>
<ellipse cx="15" cy="0" rx="8" ry="6" fill="#8D6E63" stroke="#3E2723" stroke-width="1"/>
<text x="7" y="14" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle">Головогрудь + Брюшко</text>
</g>
<g transform="translate(420,270)">
<circle cx="0" cy="0" r="8" fill="#8D6E63" stroke="#3E2723" stroke-width="1.5"/>
<circle cx="-8" cy="-4" r="3" fill="#A1887F" stroke="#3E2723" stroke-width="1"/>
<path d="M-5,-7 L-12,-14" stroke="#5D4037" stroke-width="0.8"/>
<path d="M-3,-7 L-8,-15" stroke="#5D4037" stroke-width="0.8"/>
<path d="M5,-7 L12,-14" stroke="#5D4037" stroke-width="0.8"/>
<path d="M3,-7 L8,-15" stroke="#5D4037" stroke-width="0.8"/>
<text x="0" y="16" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Клещ</text>
</g>
'''+ibox(120,295,300,18,["4 пары ходильных ног | Хелицеры + педипальпы | Паутинные бородавки"])+ftr

# 14: Насекомые
svgs[14] = hdr("Насекомые",14)+'''
<g transform="translate(250,175)">
<ellipse cx="-48" cy="0" rx="13" ry="10" fill="#8D6E63" stroke="#3E2723" stroke-width="2"/>
<ellipse cx="-52" cy="-5" rx="5" ry="4" fill="#FFD54F" stroke="#333" stroke-width="0.8"/>
<ellipse cx="-52" cy="5" rx="5" ry="4" fill="#FFD54F" stroke="#333" stroke-width="0.8"/>
<path d="M-57,-7 Q-68,-18 -64,-26" stroke="#5D4037" stroke-width="1.5" fill="none"/>
<path d="M-57,7 Q-68,18 -64,26" stroke="#5D4037" stroke-width="1.5" fill="none"/>
<ellipse cx="-25" cy="0" rx="10" ry="12" fill="#A1887F" stroke="#3E2723" stroke-width="1.5"/>
<path d="M-15,-12 L35,-10 L35,0 L-15,0Z" fill="#6D4C41" stroke="#3E2723" stroke-width="1.5"/>
<path d="M-15,0 L35,0 L35,10 L-15,12Z" fill="#795548" stroke="#3E2723" stroke-width="1.5"/>
<line x1="-15" y1="0" x2="35" y2="0" stroke="#3E2723" stroke-width="0.8"/>
<ellipse cx="40" cy="0" rx="7" ry="9" fill="#A1887F" stroke="#3E2723" stroke-width="1"/>
<path d="M-27,-10 L-34,-20 L-30,-26" stroke="#5D4037" stroke-width="1.5" fill="none"/>
<path d="M-24,-12 L-26,-24 L-22,-28" stroke="#5D4037" stroke-width="1.5" fill="none"/>
<path d="M-20,-12 L-16,-24 L-12,-28" stroke="#5D4037" stroke-width="1.5" fill="none"/>
<path d="M-27,10 L-34,20 L-30,26" stroke="#5D4037" stroke-width="1.5" fill="none"/>
<path d="M-24,12 L-26,24 L-22,28" stroke="#5D4037" stroke-width="1.5" fill="none"/>
<path d="M-20,12 L-16,24 L-12,28" stroke="#5D4037" stroke-width="1.5" fill="none"/>
</g>
<rect x="50" y="68" width="400" height="18" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
<text x="155" y="81" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Голова</text>
<text x="250" y="81" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Грудь</text>
<text x="370" y="81" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Брюшко</text>
'''+ibox(30,280,440,30,["3 отдела: голова, грудь, брюшко | 3 пары ног | 1-2 пары крыльев","Фасеточные глаза | Усики | Трахеи | Мальпигиевы сосуды | Самый многочисленный класс"])+ftr

# 15: Многообразие насекомых
svgs[15] = hdr("Многообразие насекомых",15)+'''
<g transform="translate(85,150)">
<ellipse cx="0" cy="0" rx="10" ry="7" fill="#81C784" stroke="#2E7D32" stroke-width="1.5"/>
<ellipse cx="14" cy="0" rx="8" ry="5" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
<ellipse cx="14" cy="0" rx="18" ry="12" fill="none" stroke="#A5D6A7" stroke-width="0.8" opacity="0.5"/>
<path d="M-8,-5 Q-15,-15 -12,-22" stroke="#4CAF50" stroke-width="1" fill="none"/>
<path d="M-8,5 Q-15,15 -12,22" stroke="#4CAF50" stroke-width="1" fill="none"/>
<text x="3" y="22" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Кузнечик</text>
</g>
<g transform="translate(250,150)">
<ellipse cx="0" cy="-3" rx="8" ry="5" fill="#FFB74D" stroke="#E65100" stroke-width="1.5"/>
<ellipse cx="12" cy="-2" rx="5" ry="4" fill="#FF9800" stroke="#E65100" stroke-width="1"/>
<path d="M12,-5 Q22,-12 20,-20" stroke="#FF9800" stroke-width="0.8" fill="none"/>
<path d="M12,0 Q22,6 20,12" stroke="#FF9800" stroke-width="0.8" fill="none"/>
<path d="M-6,-6 Q-12,-14 -10,-20" stroke="#E65100" stroke-width="1" fill="none"/>
<path d="M-6,2 Q-12,10 -10,16" stroke="#E65100" stroke-width="1" fill="none"/>
<path d="M-3,-6 Q-5,-15 -2,-22" stroke="#E65100" stroke-width="1" fill="none"/>
<path d="M-3,2 Q-5,10 -2,16" stroke="#E65100" stroke-width="1" fill="none"/>
<text x="3" y="22" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Бабочка</text>
</g>
<g transform="translate(415,150)">
<ellipse cx="0" cy="0" rx="10" ry="7" fill="#EF9A9A" stroke="#C62828" stroke-width="1.5"/>
<ellipse cx="12" cy="-2" rx="6" ry="4" fill="#E53935" stroke="#C62828" stroke-width="1"/>
<path d="M-7,-5 Q-14,-14 -12,-20" stroke="#C62828" stroke-width="1" fill="none"/>
<path d="M-7,5 Q-14,14 -12,20" stroke="#C62828" stroke-width="1" fill="none"/>
<line x1="18" y1="-4" x2="28" y2="-12" stroke="#C62828" stroke-width="1"/>
<line x1="18" y1="0" x2="28" y2="4" stroke="#C62828" stroke-width="1"/>
<text x="5" y="22" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Муха</text>
</g>
<g transform="translate(100,250)">
<path d="M0,-12 L5,-8 L5,8 L0,12 L-5,8 L-5,-8Z" fill="#FFD54F" stroke="#F9A825" stroke-width="1.5"/>
<path d="M-5,-4 L-18,-4 L-15,0 L-18,4 L-5,4Z" fill="#FFE082" stroke="#F9A825" stroke-width="1"/>
<path d="M5,-4 L18,-4 L15,0 L18,4 L5,4Z" fill="#FFE082" stroke="#F9A825" stroke-width="1"/>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Пчела</text>
</g>
<g transform="translate(250,250)">
<circle cx="0" cy="0" r="6" fill="#4CAF50" stroke="#2E7D32" stroke-width="1.5"/>
<ellipse cx="10" cy="0" rx="8" ry="4" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
<path d="M10,-3 Q18,-8 16,-14" stroke="#81C784" stroke-width="0.8" fill="none"/>
<path d="M10,3 Q18,8 16,14" stroke="#81C784" stroke-width="0.8" fill="none"/>
<text x="5" y="20" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Тля</text>
</g>
<g transform="translate(400,250)">
<ellipse cx="0" cy="-5" rx="8" ry="10" fill="#795548" stroke="#3E2723" stroke-width="1.5"/>
<ellipse cx="0" cy="8" rx="7" ry="6" fill="#8D6E63" stroke="#3E2723" stroke-width="1"/>
<path d="M-6,-12 Q-12,-20 -10,-25" stroke="#5D4037" stroke-width="0.8" fill="none"/>
<path d="M6,-12 Q12,-20 10,-25" stroke="#5D4037" stroke-width="0.8" fill="none"/>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Жук</text>
</g>
'''+ibox(30,295,440,18,["Развитие: полное (яйцо-личинка-куколка-взрослое) и неполное (без куколки) превращение"])+ftr

# 16: Общая характеристика рыб
svgs[16] = hdr("Общая характеристика рыб",16)+'''
<g transform="translate(250,170)">
<ellipse cx="0" cy="0" rx="70" ry="28" fill="#64B5F6" stroke="#1565C0" stroke-width="2"/>
<path d="M70,0 L95,-18 L95,18Z" fill="#64B5F6" stroke="#1565C0" stroke-width="1.5"/>
<path d="M0,-28 L-10,-50 L10,-50Z" fill="#42A5F5" stroke="#1565C0" stroke-width="1"/>
<path d="M-30,-25 L-35,-40 L-22,-35Z" fill="#42A5F5" stroke="#1565C0" stroke-width="1"/>
<path d="M-40,-15 L-48,-25 L-48,-5Z" fill="#42A5F5" stroke="#1565C0" stroke-width="1"/>
<circle cx="-52" cy="-5" r="5" fill="white" stroke="#1565C0" stroke-width="1"/>
<circle cx="-52" cy="-5" r="2.5" fill="#333"/>
<path d="M-38,0 Q-30,5 -20,2" stroke="#1565C0" stroke-width="1" fill="none"/>
<line x1="-60" y1="0" x2="-60" y2="8" stroke="#1565C0" stroke-width="0.5"/>
<path d="M-30,20 L-28,25 L-20,22" stroke="#90CAF9" stroke-width="0.8" fill="none"/>
<path d="M-10,22 L-8,27 L0,24" stroke="#90CAF9" stroke-width="0.8" fill="none"/>
<path d="M10,22 L12,27 L20,24" stroke="#90CAF9" stroke-width="0.8" fill="none"/>
<path d="M30,20 L32,25 L38,22" stroke="#90CAF9" stroke-width="0.8" fill="none"/>
<path d="M-20,-2 Q-15,-5 -5,-2" stroke="#BBDEFB" stroke-width="0.5" fill="none"/>
<path d="M5,-2 Q15,-5 25,-2" stroke="#BBDEFB" stroke-width="0.5" fill="none"/>
<text x="0" y="45" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" text-anchor="middle" font-weight="bold">Рыба</text>
</g>
<g transform="translate(85,260)">
<rect x="-40" y="-15" width="80" height="30" rx="5" fill="#BBDEFB" stroke="#1565C0" stroke-width="1"/>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">Жабры</text>
<path d="M-20,5 Q-10,0 0,5 Q10,0 20,5" stroke="#1565C0" stroke-width="1" fill="none"/>
</g>
<g transform="translate(250,260)">
<rect x="-45" y="-15" width="90" height="30" rx="5" fill="#BBDEFB" stroke="#1565C0" stroke-width="1"/>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">Боковая линия</text>
<line x1="-35" y1="6" x2="35" y2="6" stroke="#1565C0" stroke-width="1.5" stroke-dasharray="4,2"/>
</g>
<g transform="translate(415,260)">
<rect x="-35" y="-15" width="70" height="30" rx="5" fill="#BBDEFB" stroke="#1565C0" stroke-width="1"/>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">Чешуя</text>
<path d="M-15,5 L-5,-2 L5,5 L15,-2" stroke="#1565C0" stroke-width="1" fill="none"/>
</g>
'''+ibox(30,295,440,18,["Водный образ жизни | Жабры | Двухкамерное сердце | Один круг кровообращения | Холоднокровные"])+ftr

# 17: Внутреннее строение рыб
svgs[17] = hdr("Внутреннее строение рыб",17)+'''
<g transform="translate(250,180)">
<ellipse cx="0" cy="0" rx="70" ry="25" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5" opacity="0.5"/>
<path d="M70,0 L90,-15 L90,15Z" fill="#E3F2FD" stroke="#1565C0" stroke-width="1" opacity="0.5"/>
<!-- Spine -->
<path d="M-60,0 Q-30,-2 0,0 Q30,2 60,0" stroke="#795548" stroke-width="2" fill="none"/>
<!-- Brain -->
<ellipse cx="-58" cy="-5" rx="8" ry="5" fill="#FFCDD2" stroke="#C62828" stroke-width="1"/>
<!-- Heart -->
<path d="M-45,8 Q-42,2 -38,8 Q-42,14 -45,8Z" fill="#E53935" stroke="#C62828" stroke-width="1"/>
<!-- Gill arches -->
<path d="M-35,-6 Q-30,-10 -25,-6" stroke="#90CAF9" stroke-width="2" fill="none"/>
<path d="M-32,-3 Q-27,-7 -22,-3" stroke="#90CAF9" stroke-width="2" fill="none"/>
<path d="M-29,0 Q-24,-4 -19,0" stroke="#90CAF9" stroke-width="2" fill="none"/>
<!-- Liver -->
<ellipse cx="-15" cy="5" rx="10" ry="6" fill="#8D6E63" opacity="0.4" stroke="#5D4037" stroke-width="1"/>
<!-- Stomach -->
<ellipse cx="5" cy="5" rx="10" ry="7" fill="#FFCC80" opacity="0.5" stroke="#E65100" stroke-width="1"/>
<!-- Intestine -->
<path d="M15,3 Q25,0 30,5 Q35,10 28,12" stroke="#E65100" stroke-width="1.5" fill="none"/>
<!-- Kidney -->
<path d="M-30,-10 Q0,-12 30,-10" stroke="#A5D6A7" stroke-width="3" fill="none" opacity="0.5"/>
<!-- Swim bladder -->
<ellipse cx="20" cy="-8" rx="25" ry="6" fill="#E1F5FE" stroke="#42A5F5" stroke-width="1" opacity="0.6"/>
<!-- Labels -->
<text x="-58" y="-15" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">Мозг</text>
<text x="-44" y="20" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">Сердце</text>
<text x="20" y="-18" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">Плават. пузырь</text>
<text x="5" y="18" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">Желудок</text>
<text x="-15" y="15" font-family="Arial,sans-serif" font-size="5" fill="#5D4037" text-anchor="middle">Печень</text>
<text x="-28" y="-15" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">Жабры</text>
</g>
'''+ibox(30,270,440,40,["Двухкамерное сердце: предсердие + желудочек | Один круг кровообращения","Плавательный пузырь — гидростатический орган | Жабры — дыхание в воде","Почки | Печень с желчным пузырём | Спинной мозг"])+ftr

# 18: Многообразие рыб
svgs[18] = hdr("Многообразие рыб",18)+'''
<g transform="translate(90,130)">
<ellipse cx="0" cy="0" rx="40" ry="15" fill="#90CAF9" stroke="#1565C0" stroke-width="1.5"/>
<path d="M40,0 L55,-10 L55,10Z" fill="#90CAF9" stroke="#1565C0" stroke-width="1"/>
<circle cx="-30" cy="-3" r="3" fill="white" stroke="#1565C0" stroke-width="0.8"/><circle cx="-30" cy="-3" r="1.5" fill="#333"/>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Карась</text>
<text x="0" y="37" font-family="Arial,sans-serif" font-size="5" fill="#666" text-anchor="middle">Костные</text>
</g>
<g transform="translate(250,130)">
<path d="M-35,-8 Q-40,-18 -35,-22 Q0,-28 35,-22 Q40,-18 35,-8 L35,8 Q35,18 0,20 Q-35,18 -35,8Z" fill="#B0BEC5" stroke="#546E7A" stroke-width="1.5"/>
<path d="M35,0 L55,-12 L55,12Z" fill="#B0BEC5" stroke="#546E7A" stroke-width="1"/>
<path d="M0,-22 L5,-35 L-5,-35Z" fill="#90A4AE" stroke="#546E7A" stroke-width="1"/>
<circle cx="-25" cy="-5" r="3" fill="white" stroke="#546E7A" stroke-width="0.8"/><circle cx="-25" cy="-5" r="1.5" fill="#333"/>
<text x="0" y="35" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Акула</text>
<text x="0" y="44" font-family="Arial,sans-serif" font-size="5" fill="#666" text-anchor="middle">Хрящевые</text>
</g>
<g transform="translate(415,130)">
<ellipse cx="0" cy="0" rx="25" ry="18" fill="#FFAB91" stroke="#BF360C" stroke-width="1.5"/>
<path d="M-5,-18 Q0,-28 5,-18" fill="#FF8A65" stroke="#BF360C" stroke-width="1"/>
<path d="M25,0 L38,-8 L38,8Z" fill="#FFAB91" stroke="#BF360C" stroke-width="1"/>
<circle cx="-15" cy="-3" r="3" fill="white" stroke="#BF360C" stroke-width="0.8"/><circle cx="-15" cy="-3" r="1.5" fill="#333"/>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Окунь</text>
<text x="0" y="39" font-family="Arial,sans-serif" font-size="5" fill="#666" text-anchor="middle">Костные</text>
</g>
<g transform="translate(120,235)">
<ellipse cx="0" cy="0" rx="35" ry="12" fill="#CE93D8" stroke="#7B1FA2" stroke-width="1.5"/>
<path d="M-15,-12 Q-10,-22 -5,-12" fill="#BA68C8" stroke="#7B1FA2" stroke-width="1"/>
<path d="M35,0 L48,-8 L48,8Z" fill="#CE93D8" stroke="#7B1FA2" stroke-width="1"/>
<circle cx="-25" cy="-2" r="3" fill="white" stroke="#7B1FA2" stroke-width="0.8"/><circle cx="-25" cy="-2" r="1.5" fill="#333"/>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Латимерия</text>
<text x="0" y="31" font-family="Arial,sans-serif" font-size="5" fill="#666" text-anchor="middle">Лопастепёрые</text>
</g>
<g transform="translate(350,235)">
<ellipse cx="0" cy="0" rx="30" ry="20" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1.5"/>
<path d="M-10,-20 L-5,-32 L5,-32 L10,-20" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
<path d="M30,0 L45,-10 L45,10Z" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
<circle cx="-20" cy="-5" r="4" fill="white" stroke="#2E7D32" stroke-width="0.8"/><circle cx="-20" cy="-5" r="2" fill="#333"/>
<text x="0" y="32" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Осётр</text>
<text x="0" y="41" font-family="Arial,sans-serif" font-size="5" fill="#666" text-anchor="middle">Хрящекостные</text>
</g>
'''+ibox(30,295,440,18,["Хрящевые: акулы, скаты | Костные: карп, окунь, треска | Лопастепёрые: латимерия"])+ftr

# 19: Общая характеристика земноводных
svgs[19] = hdr("Общая характеристика земноводных",19)+'''
<g transform="translate(200,170)">
<!-- Frog body -->
<ellipse cx="0" cy="5" rx="30" ry="20" fill="#66BB6A" stroke="#2E7D32" stroke-width="2"/>
<!-- Head -->
<ellipse cx="-25" cy="-5" rx="18" ry="14" fill="#81C784" stroke="#2E7D32" stroke-width="2"/>
<!-- Eyes bulging -->
<circle cx="-32" cy="-14" r="6" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1.5"/>
<circle cx="-32" cy="-14" r="3" fill="#333"/>
<circle cx="-20" cy="-14" r="6" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1.5"/>
<circle cx="-20" cy="-14" r="3" fill="#333"/>
<!-- Front legs -->
<path d="M-20,20 L-30,35 L-35,38" stroke="#2E7D32" stroke-width="2.5" fill="none"/>
<!-- Back legs (jumping) -->
<path d="M20,15 L30,25 L25,40 L22,45" stroke="#2E7D32" stroke-width="2.5" fill="none"/>
<path d="M15,18 L22,30 L18,42" stroke="#2E7D32" stroke-width="2" fill="none"/>
<!-- Nostril -->
<circle cx="-38" cy="-3" r="1.5" fill="#2E7D32"/>
<!-- Tympanum -->
<circle cx="-18" cy="2" r="4" fill="#81C784" stroke="#1B5E20" stroke-width="1"/>
<text x="0" y="58" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Лягушка</text>
</g>
<g transform="translate(400,160)">
<rect x="-55" y="-55" width="110" height="110" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Особенности</text>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Кожа голая, влажная</text>
<text x="0" y="-13" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Два круга кровообр.</text>
<text x="0" y="-1" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">3-камерное сердце</text>
<text x="0" y="11" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Лёгкие + кожное дых.</text>
<text x="0" y="23" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Два типа зрения</text>
<text x="0" y="35" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Наружное оплодотв.</text>
<text x="0" y="47" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Метаморфоз: головастик</text>
</g>
'''+ftr

# 20: Многообразие земноводных
svgs[20] = hdr("Многообразие земноводных",20)+'''
<g transform="translate(85,150)">
<ellipse cx="0" cy="5" rx="22" ry="14" fill="#66BB6A" stroke="#2E7D32" stroke-width="1.5"/>
<ellipse cx="-18" cy="-3" rx="12" ry="10" fill="#81C784" stroke="#2E7D32" stroke-width="1.5"/>
<circle cx="-24" cy="-10" r="4" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/><circle cx="-24" cy="-10" r="2" fill="#333"/>
<circle cx="-14" cy="-10" r="4" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/><circle cx="-14" cy="-10" r="2" fill="#333"/>
<path d="M-12,15 L-18,25" stroke="#2E7D32" stroke-width="2" fill="none"/>
<path d="M15,10 L22,20 L18,30" stroke="#2E7D32" stroke-width="2" fill="none"/>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Лягушка</text>
</g>
<g transform="translate(250,150)">
<ellipse cx="0" cy="8" rx="20" ry="12" fill="#8D6E63" stroke="#4E342E" stroke-width="1.5"/>
<ellipse cx="-15" cy="0" rx="10" ry="8" fill="#A1887F" stroke="#4E342E" stroke-width="1.5"/>
<circle cx="-20" cy="-5" r="3" fill="#BCAAA4" stroke="#4E342E" stroke-width="0.8"/><circle cx="-20" cy="-5" r="1.5" fill="#333"/>
<circle cx="-12" cy="-5" r="3" fill="#BCAAA4" stroke="#4E342E" stroke-width="0.8"/><circle cx="-12" cy="-5" r="1.5" fill="#333"/>
<path d="M-8,15 L-14,25 L-16,28" stroke="#4E342E" stroke-width="1.5" fill="none"/>
<path d="M12,12 L18,22 L15,30" stroke="#4E342E" stroke-width="1.5" fill="none"/>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Жаба</text>
</g>
<g transform="translate(415,150)">
<ellipse cx="0" cy="5" rx="12" ry="18" fill="#FFCC80" stroke="#E65100" stroke-width="1.5"/>
<ellipse cx="0" cy="-15" rx="8" ry="6" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
<circle cx="-3" cy="-18" r="2" fill="#333"/><circle cx="3" cy="-18" r="2" fill="#333"/>
<path d="M-8,20 L-12,30" stroke="#E65100" stroke-width="1.5" fill="none"/>
<path d="M8,20 L12,30" stroke="#E65100" stroke-width="1.5" fill="none"/>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Тритон</text>
</g>
<g transform="translate(100,255)">
<ellipse cx="0" cy="0" rx="30" ry="8" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
<circle cx="-25" cy="-2" r="3" fill="#A5D6A7" stroke="#2E7D32" stroke-width="0.8"/>
<path d="M0,-8 L5,-18" stroke="#2E7D32" stroke-width="0.8" fill="none"/>
<path d="M15,-6 L20,-15" stroke="#2E7D32" stroke-width="0.8" fill="none"/>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Саламандра</text>
</g>
<g transform="translate(300,260)">
<ellipse cx="0" cy="0" rx="25" ry="10" fill="#4CAF50" stroke="#1B5E20" stroke-width="1.5"/>
<path d="M-15,-10 L-20,-25 L-10,-25 Z" fill="#81C784" stroke="#1B5E20" stroke-width="1"/>
<circle cx="-15" cy="-3" r="3" fill="#333"/>
<path d="M20,0 Q30,0 35,-5" stroke="#1B5E20" stroke-width="1" fill="none"/>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Головастик (личинка)</text>
</g>
'''+ibox(30,295,440,18,["Отряды: Бесхвостые (лягушки, жабы) | Хвостатые (тритоны, саламандры) | Безногие (червяги)"])+ftr

# 21: Общая характеристика пресмыкающихся
svgs[21] = hdr("Общая характеристика пресмыкающихся",21)+'''
<g transform="translate(250,170)">
<ellipse cx="-20" cy="0" rx="12" ry="10" fill="#8D6E63" stroke="#4E342E" stroke-width="2"/>
<circle cx="-28" cy="-4" r="2.5" fill="#FFD54F" stroke="#333" stroke-width="0.5"/>
<circle cx="-28" cy="4" r="2.5" fill="#FFD54F" stroke="#333" stroke-width="0.5"/>
<path d="M-32,0 L-40,-3 L-40,3Z" fill="#6D4C41"/>
<path d="M-8,-8 Q0,-5 8,-8" stroke="#4E342E" stroke-width="1" fill="none"/>
<path d="M-8,0 Q0,3 8,0" stroke="#4E342E" stroke-width="1" fill="none"/>
<path d="M-8,8 Q0,5 8,8" stroke="#4E342E" stroke-width="1" fill="none"/>
<ellipse cx="25" cy="0" rx="35" ry="10" fill="#A1887F" stroke="#4E342E" stroke-width="2"/>
<line x1="5" y1="-8" x2="5" y2="8" stroke="#795548" stroke-width="0.5"/>
<line x1="15" y1="-9" x2="15" y2="9" stroke="#795548" stroke-width="0.5"/>
<line x1="25" y1="-9" x2="25" y2="9" stroke="#795548" stroke-width="0.5"/>
<line x1="35" y1="-8" x2="35" y2="8" stroke="#795548" stroke-width="0.5"/>
<line x1="45" y1="-6" x2="45" y2="6" stroke="#795548" stroke-width="0.5"/>
<path d="M60,0 Q70,-5 75,0 Q80,5 85,0 Q90,-5 95,0" stroke="#4E342E" stroke-width="2" fill="none"/>
<path d="M-10,8 L-15,18 L-10,22" stroke="#795548" stroke-width="1.5" fill="none"/>
<path d="M5,9 L2,20 L7,24" stroke="#795548" stroke-width="1.5" fill="none"/>
<path d="M20,9 L18,20 L23,22" stroke="#795548" stroke-width="1.5" fill="none"/>
<path d="M-10,-8 L-15,-18 L-10,-22" stroke="#795548" stroke-width="1.5" fill="none"/>
<path d="M5,-9 L2,-20 L7,-22" stroke="#795548" stroke-width="1.5" fill="none"/>
<path d="M20,-9 L18,-20 L23,-22" stroke="#795548" stroke-width="1.5" fill="none"/>
<text x="25" y="35" font-family="Arial,sans-serif" font-size="8" fill="#4E342E" text-anchor="middle" font-weight="bold">Ящерица</text>
</g>
<g transform="translate(90,265)">
<rect x="-45" y="-12" width="90" height="24" rx="5" fill="#D7CCC8" stroke="#5D4037" stroke-width="1"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="#5D4037" text-anchor="middle" font-weight="bold">Роговая чешуя</text>
</g>
<g transform="translate(250,265)">
<rect x="-45" y="-12" width="90" height="24" rx="5" fill="#FFCDD2" stroke="#C62828" stroke-width="1"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">3-камерное сердце</text>
</g>
<g transform="translate(410,265)">
<rect x="-40" y="-12" width="80" height="24" rx="5" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Внутреннее оплод.</text>
</g>
'''+ibox(30,295,440,18,["Сухая кожа с чешуёй | Лёгочное дыхание | Неполная перегородка в желудочке | Яйца с оболочкой"])+ftr

# 22: Многообразие пресмыкающихся
svgs[22] = hdr("Многообразие пресмыкающихся",22)+'''
<g transform="translate(85,155)">
<ellipse cx="0" cy="0" rx="35" ry="10" fill="#A1887F" stroke="#4E342E" stroke-width="1.5"/>
<ellipse cx="-30" cy="-2" rx="8" ry="6" fill="#8D6E63" stroke="#4E342E" stroke-width="1"/>
<circle cx="-35" cy="-4" r="2" fill="#FFD54F"/><circle cx="-35" cy="2" r="2" fill="#FFD54F"/>
<path d="M35,0 Q45,-3 50,0 Q55,3 60,0" stroke="#4E342E" stroke-width="1.5" fill="none"/>
<path d="M-8,8 L-12,16" stroke="#795548" stroke-width="1" fill="none"/>
<path d="M5,8 L3,16" stroke="#795548" stroke-width="1" fill="none"/>
<text x="0" y="25" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Ящерица</text>
</g>
<g transform="translate(250,145)">
<ellipse cx="0" cy="5" rx="15" ry="18" fill="#795548" stroke="#3E2723" stroke-width="1.5"/>
<ellipse cx="0" cy="-15" rx="10" ry="8" fill="#8D6E63" stroke="#3E2723" stroke-width="1.5"/>
<circle cx="-4" cy="-18" r="1.5" fill="#FFD54F"/><circle cx="4" cy="-18" r="1.5" fill="#FFD54F"/>
<path d="M-5,-22 L0,-28" stroke="#3E2723" stroke-width="1" fill="none"/>
<path d="M0,23 Q-5,30 -3,38" stroke="#3E2723" stroke-width="1.5" fill="none"/>
<text x="0" y="50" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Змея</text>
</g>
<g transform="translate(420,150)">
<ellipse cx="0" cy="8" rx="28" ry="18" fill="#66BB6A" stroke="#1B5E20" stroke-width="1.5"/>
<ellipse cx="-22" cy="-8" rx="12" ry="8" fill="#81C784" stroke="#1B5E20" stroke-width="1.5"/>
<circle cx="-28" cy="-12" r="4" fill="white" stroke="#1B5E20" stroke-width="0.8"/><circle cx="-28" cy="-12" r="2" fill="#333"/>
<path d="M-34,-8 L-44,-8" stroke="#1B5E20" stroke-width="2" fill="none"/>
<path d="M-34,-5 L-42,-3" stroke="#1B5E20" stroke-width="2" fill="none"/>
<path d="M-30,18 L-35,28" stroke="#1B5E20" stroke-width="1.5" fill="none"/>
<path d="M-10,20 L-12,30" stroke="#1B5E20" stroke-width="1.5" fill="none"/>
<path d="M10,20 L12,30" stroke="#1B5E20" stroke-width="1.5" fill="none"/>
<path d="M30,18 L35,28" stroke="#1B5E20" stroke-width="1.5" fill="none"/>
<path d="M0,-16 L0,-25" stroke="#1B5E20" stroke-width="1.5" fill="none"/>
<text x="0" y="45" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Крокодил</text>
</g>
<g transform="translate(150,255)">
<ellipse cx="0" cy="0" rx="22" ry="15" fill="#8D6E63" stroke="#5D4037" stroke-width="1.5"/>
<path d="M-8,-15 L-15,-25 L-5,-25Z" fill="#A1887F" stroke="#5D4037" stroke-width="1"/>
<path d="M8,-15 L15,-25 L5,-25Z" fill="#A1887F" stroke="#5D4037" stroke-width="1"/>
<ellipse cx="0" cy="0" rx="12" ry="6" fill="#6D4C41" stroke="#5D4037" stroke-width="1"/>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Черепаха</text>
</g>
<g transform="translate(350,255)">
<ellipse cx="0" cy="3" rx="12" ry="8" fill="#FFAB91" stroke="#BF360C" stroke-width="1.5"/>
<ellipse cx="0" cy="-8" rx="6" ry="5" fill="#FFCCBC" stroke="#BF360C" stroke-width="1"/>
<circle cx="-2" cy="-11" r="1.5" fill="#333"/><circle cx="2" cy="-11" r="1.5" fill="#333"/>
<path d="M-8,8 L-12,16" stroke="#BF360C" stroke-width="1" fill="none"/>
<path d="M8,8 L12,16" stroke="#BF360C" stroke-width="1" fill="none"/>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Хамелеон</text>
</g>
'''+ibox(30,295,440,18,["Чешуйчатые: ящерицы, змеи | Черепахи | Крокодилы | Клювоголовые (гаттерия)"])+ftr

for i in range(11,23):
    with open(f"{OUT}/lesson{i}.svg","w") as f:
        f.write(svgs[i])
print("Lessons 11-22 done")
