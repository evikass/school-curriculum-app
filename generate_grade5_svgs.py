#!/usr/bin/env python3
"""Generate detailed SVG illustrations for Grade 5 Biology lessons (Пасечник В.В.)"""

import os

OUTPUT_DIR = "/home/z/my-project/images/lessons/grade5/biology"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def write_svg(filename, content):
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    size = os.path.getsize(filepath)
    print(f"  {filename}: {size} bytes")

# ============================================================
# Lesson 1: Биология — наука о живой природе
# ============================================================
svg1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#E8F5E9"/><stop offset="100%" stop-color="#C8E6C9"/></linearGradient>
<linearGradient id="leafGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#66BB6A"/><stop offset="100%" stop-color="#2E7D32"/></linearGradient>
<linearGradient id="circleGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#81C784"/><stop offset="100%" stop-color="#388E3C"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#2E7D32" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#1B5E20" text-anchor="middle">Биология — наука о живой природе</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 1</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#2E7D32" stroke-width="1" opacity="0.3"/>

<!-- Central leaf/book icon -->
<g transform="translate(250,120)">
  <ellipse cx="0" cy="0" rx="50" ry="35" fill="url(#circleGrad)" opacity="0.9" stroke="#1B5E20" stroke-width="2"/>
  <path d="M-15,-15 Q0,-25 15,-15 Q25,-5 15,10 Q0,20 -15,10 Q-25,-5 -15,-15" fill="url(#leafGrad)" stroke="#1B5E20" stroke-width="1.5"/>
  <path d="M0,-12 L0,12" stroke="#1B5E20" stroke-width="1"/>
  <path d="M0,-5 L-8,0" stroke="#1B5E20" stroke-width="0.8"/>
  <path d="M0,-5 L8,0" stroke="#1B5E20" stroke-width="0.8"/>
  <path d="M0,2 L-6,7" stroke="#1B5E20" stroke-width="0.8"/>
  <path d="M0,2 L6,7" stroke="#1B5E20" stroke-width="0.8"/>
  <text x="0" y="50" font-family="Arial,sans-serif" font-size="10" fill="#1B5E20" text-anchor="middle" font-weight="bold">БИОЛОГИЯ</text>
  <text x="0" y="62" font-family="Arial,sans-serif" font-size="7" fill="#388E3C" text-anchor="middle">наука о жизни</text>
</g>

<!-- Branch lines to sub-sciences -->
<line x1="200" y1="120" x2="90" y2="170" stroke="#4CAF50" stroke-width="2"/>
<line x1="250" y1="155" x2="250" y2="175" stroke="#4CAF50" stroke-width="2"/>
<line x1="300" y1="120" x2="410" y2="170" stroke="#4CAF50" stroke-width="2"/>
<line x1="215" y1="145" x2="150" y2="175" stroke="#4CAF50" stroke-width="1.5"/>
<line x1="285" y1="145" x2="350" y2="175" stroke="#4CAF50" stroke-width="1.5"/>

<!-- Botany -->
<g transform="translate(90,200)">
  <rect x="-50" y="-25" width="100" height="50" rx="8" fill="white" opacity="0.9" stroke="#4CAF50" stroke-width="1.5"/>
  <path d="M-30,-10 Q-25,-20 -15,-15 Q-10,-5 -15,0 Q-25,5 -30,-10" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
  <line x1="-22" y1="-10" x2="-22" y2="5" stroke="#2E7D32" stroke-width="1.5"/>
  <text x="10" y="-5" font-family="Arial,sans-serif" font-size="8" fill="#1B5E20" text-anchor="middle" font-weight="bold">Ботаника</text>
  <text x="10" y="7" font-family="Arial,sans-serif" font-size="6" fill="#388E3C" text-anchor="middle">растения</text>
</g>

<!-- Zoology -->
<g transform="translate(250,200)">
  <rect x="-50" y="-25" width="100" height="50" rx="8" fill="white" opacity="0.9" stroke="#FF9800" stroke-width="1.5"/>
  <ellipse cx="-25" cy="-5" rx="10" ry="7" fill="#FFB74D" stroke="#E65100" stroke-width="1"/>
  <circle cx="-29" cy="-7" r="2" fill="#1B5E20"/>
  <path d="M-15,-5 Q-10,-10 -5,-5" fill="none" stroke="#E65100" stroke-width="1"/>
  <text x="10" y="-5" font-family="Arial,sans-serif" font-size="8" fill="#BF360C" text-anchor="middle" font-weight="bold">Зоология</text>
  <text x="10" y="7" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">животные</text>
</g>

<!-- Ecology -->
<g transform="translate(410,200)">
  <rect x="-50" y="-25" width="100" height="50" rx="8" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1.5"/>
  <circle cx="-25" cy="-5" r="10" fill="#64B5F6" stroke="#1565C0" stroke-width="1"/>
  <path d="M-25,-12 Q-20,-8 -25,-5 Q-30,-8 -25,-12" fill="#4CAF50"/>
  <path d="M-25,-5 Q-18,-1 -25,3 Q-32,-1 -25,-5" fill="#4CAF50"/>
  <text x="10" y="-5" font-family="Arial,sans-serif" font-size="8" fill="#0D47A1" text-anchor="middle" font-weight="bold">Экология</text>
  <text x="10" y="7" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">среда</text>
</g>

<!-- Mycology -->
<g transform="translate(150,260)">
  <rect x="-45" y="-20" width="90" height="40" rx="6" fill="white" opacity="0.85" stroke="#795548" stroke-width="1"/>
  <path d="M-30,-5 Q-25,-15 -15,-10 Q-5,-5 -10,0 L-12,8 L-24,8 L-25,0 Z" fill="#A1887F" stroke="#5D4037" stroke-width="0.8"/>
  <text x="10" y="-2" font-family="Arial,sans-serif" font-size="7" fill="#4E342E" text-anchor="middle" font-weight="bold">Микология</text>
  <text x="10" y="9" font-family="Arial,sans-serif" font-size="5.5" fill="#795548" text-anchor="middle">грибы</text>
</g>

<!-- Microbiology -->
<g transform="translate(350,260)">
  <rect x="-45" y="-20" width="90" height="40" rx="6" fill="white" opacity="0.85" stroke="#9C27B0" stroke-width="1"/>
  <ellipse cx="-25" cy="-3" rx="5" ry="3" fill="#CE93D8" stroke="#7B1FA2" stroke-width="0.8"/>
  <circle cx="-18" cy="-6" r="2.5" fill="#BA68C8" stroke="#7B1FA2" stroke-width="0.6"/>
  <circle cx="-32" cy="-1" r="2" fill="#BA68C8" stroke="#7B1FA2" stroke-width="0.6"/>
  <text x="10" y="-2" font-family="Arial,sans-serif" font-size="7" fill="#4A148C" text-anchor="middle" font-weight="bold">Микробиол.</text>
  <text x="10" y="9" font-family="Arial,sans-serif" font-size="5.5" fill="#9C27B0" text-anchor="middle">микроорганизмы</text>
</g>

<!-- Bottom properties bar -->
<rect x="30" y="305" width="440" height="30" rx="6" fill="#E8F5E9" stroke="#4CAF50" stroke-width="1"/>
<text x="250" y="324" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Свойства живого: обмен веществ · рост · развитие · размножение · раздражимость</text>
</svg>'''

# ============================================================
# Lesson 2: Методы исследования в биологии
# ============================================================
svg2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#E3F2FD"/><stop offset="100%" stop-color="#BBDEFB"/></linearGradient>
<linearGradient id="lensGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#E1F5FE"/><stop offset="100%" stop-color="#B3E5FC"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#1565C0" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#0D47A1" text-anchor="middle">Методы исследования в биологии</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 2</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#1565C0" stroke-width="1" opacity="0.3"/>

<!-- Microscope illustration -->
<g transform="translate(100,140)">
  <rect x="-40" y="-55" width="80" height="110" rx="6" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1.5"/>
  <text x="0" y="-40" font-family="Arial,sans-serif" font-size="8" fill="#0D47A1" text-anchor="middle" font-weight="bold">МИКРОСКОП</text>
  <line x1="-30" y1="-33" x2="30" y2="-33" stroke="#1565C0" stroke-width="0.5"/>
  <!-- Eyepiece -->
  <rect x="-8" y="-30" width="16" height="8" rx="2" fill="#90CAF9" stroke="#1565C0" stroke-width="1"/>
  <rect x="-6" y="-28" width="12" height="4" rx="1" fill="url(#lensGrad)"/>
  <!-- Tube -->
  <rect x="-4" y="-22" width="8" height="20" fill="#64B5F6" stroke="#1565C0" stroke-width="1"/>
  <!-- Objective -->
  <rect x="-6" y="-2" width="12" height="6" rx="1" fill="#42A5F5" stroke="#1565C0" stroke-width="1"/>
  <!-- Stage -->
  <rect x="-25" y="8" width="50" height="4" rx="1" fill="#BBDEFB" stroke="#1565C0" stroke-width="1"/>
  <rect x="-10" y="6" width="20" height="2" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.5"/>
  <!-- Arm -->
  <rect x="5" y="-22" width="6" height="35" rx="1" fill="#90CAF9" stroke="#1565C0" stroke-width="1"/>
  <!-- Base -->
  <rect x="-25" y="14" width="50" height="6" rx="2" fill="#64B5F6" stroke="#1565C0" stroke-width="1"/>
  <!-- Focus knob -->
  <circle cx="8" cy="5" r="5" fill="#42A5F5" stroke="#1565C0" stroke-width="1"/>
  <text x="0" y="38" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">Наблюдение</text>
</g>

<!-- Experiment illustration -->
<g transform="translate(250,140)">
  <rect x="-50" y="-55" width="100" height="110" rx="6" fill="white" opacity="0.9" stroke="#2E7D32" stroke-width="1.5"/>
  <text x="0" y="-40" font-family="Arial,sans-serif" font-size="8" fill="#1B5E20" text-anchor="middle" font-weight="bold">ЭКСПЕРИМЕНТ</text>
  <line x1="-40" y1="-33" x2="40" y2="-33" stroke="#2E7D32" stroke-width="0.5"/>
  <!-- Test tube 1 -->
  <rect x="-30" y="-25" width="10" height="35" rx="3" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
  <rect x="-30" y="-5" width="10" height="15" rx="3" fill="#81C784" opacity="0.7"/>
  <circle cx="-25" cy="-5" r="2" fill="#4CAF50"/>
  <!-- Test tube 2 -->
  <rect x="-12" y="-25" width="10" height="35" rx="3" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
  <rect x="-12" y="-10" width="10" height="20" rx="3" fill="#FFAB91" opacity="0.7"/>
  <!-- Beaker -->
  <path d="M10,-25 L10,5 Q10,10 15,10 L25,10 Q30,10 30,5 L30,-25" fill="none" stroke="#2E7D32" stroke-width="1.5"/>
  <rect x="11" y="-5" width="18" height="14" rx="2" fill="#C8E6C9" opacity="0.6"/>
  <!-- Arrow showing comparison -->
  <line x1="-35" y1="20" x2="35" y2="20" stroke="#FF9800" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="0" y="35" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Опыт + Контроль</text>
  <text x="0" y="45" font-family="Arial,sans-serif" font-size="5" fill="#666" text-anchor="middle">Сравнение результатов</text>
</g>

<!-- Measurement & comparison -->
<g transform="translate(400,140)">
  <rect x="-40" y="-55" width="80" height="110" rx="6" fill="white" opacity="0.9" stroke="#E65100" stroke-width="1.5"/>
  <text x="0" y="-40" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle" font-weight="bold">ИЗМЕРЕНИЕ</text>
  <line x1="-30" y1="-33" x2="30" y2="-33" stroke="#E65100" stroke-width="0.5"/>
  <!-- Ruler -->
  <rect x="-20" y="-25" width="40" height="8" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
  <line x1="-18" y1="-25" x2="-18" y2="-20" stroke="#E65100" stroke-width="0.5"/>
  <line x1="-10" y1="-25" x2="-10" y2="-21" stroke="#E65100" stroke-width="0.5"/>
  <line x1="-2" y1="-25" x2="-2" y2="-20" stroke="#E65100" stroke-width="0.5"/>
  <line x1="6" y1="-25" x2="6" y2="-21" stroke="#E65100" stroke-width="0.5"/>
  <line x1="14" y1="-25" x2="14" y2="-20" stroke="#E65100" stroke-width="0.5"/>
  <!-- Leaf being measured -->
  <path d="M-5,-5 Q5,-18 15,-5 Q10,5 5,10 Q0,5 -5,-5" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
  <line x1="-5" y1="10" x2="15" y2="10" stroke="#E65100" stroke-width="1" stroke-dasharray="2,1"/>
  <text x="5" y="20" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">5 см</text>
  <!-- Thermometer -->
  <rect x="-5" y="25" width="6" height="25" rx="3" fill="#FFCDD2" stroke="#C62828" stroke-width="0.8"/>
  <rect x="-3" y="35" width="2" height="14" rx="1" fill="#F44336"/>
  <circle cx="-2" cy="48" r="4" fill="#F44336" stroke="#C62828" stroke-width="0.8"/>
  <text x="12" y="38" font-family="Arial,sans-serif" font-size="5" fill="#C62828">t°</text>
</g>

<!-- Bottom method flow -->
<rect x="30" y="260" width="440" height="70" rx="6" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1"/>
<text x="250" y="278" font-family="Arial,sans-serif" font-size="8" fill="#0D47A1" text-anchor="middle" font-weight="bold">Последовательность научного исследования</text>
<rect x="50" y="286" width="70" height="18" rx="4" fill="#E3F2FD" stroke="#1565C0" stroke-width="0.8"/>
<text x="85" y="298" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">Наблюдение</text>
<text x="128" y="298" font-family="Arial,sans-serif" font-size="8" fill="#1565C0">→</text>
<rect x="137" y="286" width="70" height="18" rx="4" fill="#E8F5E9" stroke="#2E7D32" stroke-width="0.8"/>
<text x="172" y="298" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Гипотеза</text>
<text x="215" y="298" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32">→</text>
<rect x="224" y="286" width="70" height="18" rx="4" fill="#FFF3E0" stroke="#E65100" stroke-width="0.8"/>
<text x="259" y="298" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Эксперимент</text>
<text x="302" y="298" font-family="Arial,sans-serif" font-size="8" fill="#E65100">→</text>
<rect x="311" y="286" width="60" height="18" rx="4" fill="#F3E5F5" stroke="#7B1FA2" stroke-width="0.8"/>
<text x="341" y="298" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle">Анализ</text>
<text x="380" y="298" font-family="Arial,sans-serif" font-size="8" fill="#7B1FA2">→</text>
<rect x="389" y="286" width="60" height="18" rx="4" fill="#FFEBEE" stroke="#C62828" stroke-width="0.8"/>
<text x="419" y="298" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">Вывод</text>
<text x="250" y="322" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Моделирование · Сравнение · Описание · Классификация</text>
</svg>'''

# ============================================================
# Lesson 3: Разнообразие живой природы. Царства живых организмов
# ============================================================
svg3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#F3E5F5"/><stop offset="100%" stop-color="#E1BEE7"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#7B1FA2" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#4A148C" text-anchor="middle">Царства живых организмов</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 3</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#7B1FA2" stroke-width="1" opacity="0.3"/>

<!-- Central circle - Живая природа -->
<circle cx="250" cy="130" r="35" fill="#9C27B0" opacity="0.15" stroke="#7B1FA2" stroke-width="2"/>
<text x="250" y="127" font-family="Arial,sans-serif" font-size="8" fill="#4A148C" text-anchor="middle" font-weight="bold">Живая</text>
<text x="250" y="138" font-family="Arial,sans-serif" font-size="8" fill="#4A148C" text-anchor="middle" font-weight="bold">природа</text>

<!-- Branches to kingdoms -->
<line x1="220" y1="115" x2="80" y2="80" stroke="#7B1FA2" stroke-width="1.5"/>
<line x1="220" y1="140" x2="80" y2="165" stroke="#7B1FA2" stroke-width="1.5"/>
<line x1="250" y1="165" x2="250" y2="210" stroke="#7B1FA2" stroke-width="1.5"/>
<line x1="280" y1="115" x2="420" y2="80" stroke="#7B1FA2" stroke-width="1.5"/>
<line x1="280" y1="140" x2="420" y2="165" stroke="#7B1FA2" stroke-width="1.5"/>

<!-- Бактерии -->
<g transform="translate(80,80)">
  <rect x="-45" y="-30" width="90" height="55" rx="8" fill="white" opacity="0.9" stroke="#FF9800" stroke-width="1.5"/>
  <ellipse cx="-20" cy="-5" rx="12" ry="5" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
  <path d="M-8,-5 Q-3,-8 2,-5" fill="none" stroke="#E65100" stroke-width="0.8"/>
  <circle cx="-28" cy="-7" r="3" fill="#FFCC80" stroke="#E65100" stroke-width="0.6"/>
  <text x="5" y="-8" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle" font-weight="bold">Бактерии</text>
  <text x="5" y="2" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">без ядра</text>
  <text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#999" text-anchor="middle">доядерные</text>
</g>

<!-- Грибы -->
<g transform="translate(80,165)">
  <rect x="-45" y="-30" width="90" height="55" rx="8" fill="white" opacity="0.9" stroke="#795548" stroke-width="1.5"/>
  <path d="M-25,-5 Q-20,-20 -10,-15 Q0,-10 -5,0 L-8,10 L-22,10 L-23,0 Z" fill="#A1887F" stroke="#5D4037" stroke-width="1"/>
  <circle cx="-15" cy="-15" r="3" fill="#BCAAA4" stroke="#5D4037" stroke-width="0.5"/>
  <text x="15" y="-5" font-family="Arial,sans-serif" font-size="7" fill="#4E342E" text-anchor="middle" font-weight="bold">Грибы</text>
  <text x="15" y="5" font-family="Arial,sans-serif" font-size="5" fill="#795548" text-anchor="middle">хитин + гетеротрофы</text>
  <text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#999" text-anchor="middle">ядерные</text>
</g>

<!-- Растения -->
<g transform="translate(250,240)">
  <rect x="-55" y="-25" width="110" height="55" rx="8" fill="white" opacity="0.9" stroke="#2E7D32" stroke-width="1.5"/>
  <path d="M-35,-5 Q-30,-18 -20,-12 Q-15,-5 -20,0 Q-30,5 -35,-5" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
  <line x1="-27" y1="-2" x2="-27" y2="10" stroke="#2E7D32" stroke-width="1.5"/>
  <path d="M-27,10 Q-32,12 -35,15" fill="none" stroke="#2E7D32" stroke-width="0.8"/>
  <text x="15" y="-5" font-family="Arial,sans-serif" font-size="7" fill="#1B5E20" text-anchor="middle" font-weight="bold">Растения</text>
  <text x="15" y="5" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">автотрофы · фотосинтез</text>
  <text x="0" y="23" font-family="Arial,sans-serif" font-size="5" fill="#999" text-anchor="middle">ядерные</text>
</g>

<!-- Животные -->
<g transform="translate(420,80)">
  <rect x="-45" y="-30" width="90" height="55" rx="8" fill="white" opacity="0.9" stroke="#E64A19" stroke-width="1.5"/>
  <ellipse cx="-22" cy="-5" rx="10" ry="7" fill="#FFAB91" stroke="#BF360C" stroke-width="1"/>
  <circle cx="-26" cy="-7" r="2" fill="#1B5E20"/>
  <path d="M-12,-5 Q-8,-10 -5,-5" fill="none" stroke="#BF360C" stroke-width="1"/>
  <path d="M-22,-12 Q-18,-16 -14,-12" fill="none" stroke="#BF360C" stroke-width="0.8"/>
  <path d="M-28,-12 Q-32,-16 -35,-12" fill="none" stroke="#BF360C" stroke-width="0.8"/>
  <text x="10" y="-8" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle" font-weight="bold">Животные</text>
  <text x="10" y="2" font-family="Arial,sans-serif" font-size="5" fill="#E64A19" text-anchor="middle">гетеротрофы</text>
  <text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#999" text-anchor="middle">ядерные</text>
</g>

<!-- Протисты (простейшие) -->
<g transform="translate(420,165)">
  <rect x="-45" y="-30" width="90" height="55" rx="8" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1.5"/>
  <ellipse cx="-22" cy="-5" rx="10" ry="7" fill="#90CAF9" stroke="#1565C0" stroke-width="1"/>
  <circle cx="-25" cy="-7" r="2.5" fill="#42A5F5" stroke="#0D47A1" stroke-width="0.5"/>
  <path d="M-12,-5 L-5,-3" stroke="#1565C0" stroke-width="0.8"/>
  <path d="M-30,0 Q-35,3 -38,0" fill="none" stroke="#1565C0" stroke-width="0.8"/>
  <text x="10" y="-8" font-family="Arial,sans-serif" font-size="7" fill="#0D47A1" text-anchor="middle" font-weight="bold">Протисты</text>
  <text x="10" y="2" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">простейшие</text>
  <text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#999" text-anchor="middle">ядерные</text>
</g>

<!-- Bottom: признаки живого -->
<rect x="30" y="305" width="440" height="30" rx="6" fill="white" opacity="0.9" stroke="#7B1FA2" stroke-width="1"/>
<text x="250" y="320" font-family="Arial,sans-serif" font-size="7" fill="#4A148C" text-anchor="middle" font-weight="bold">Признаки живого: обмен веществ · рост · развитие · размножение · раздражимость · наследственность</text>
<text x="250" y="332" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Доядерные (без ядра) — Бактерии | Ядерные (с ядром) — Растения, Животные, Грибы, Протисты</text>
</svg>'''

# ============================================================
# Lesson 4: Среды обитания организмов
# ============================================================
svg4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#E0F7FA"/><stop offset="100%" stop-color="#B2EBF2"/></linearGradient>
<linearGradient id="waterGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#4FC3F7"/><stop offset="100%" stop-color="#0277BD"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#00838F" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#006064" text-anchor="middle">Среды обитания организмов</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 4</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#00838F" stroke-width="1" opacity="0.3"/>

<!-- Водная среда -->
<g transform="translate(85,170)">
  <rect x="-60" y="-95" width="120" height="175" rx="8" fill="white" opacity="0.9" stroke="#0277BD" stroke-width="1.5"/>
  <text x="0" y="-78" font-family="Arial,sans-serif" font-size="9" fill="#01579B" text-anchor="middle" font-weight="bold">ВОДНАЯ</text>
  <line x1="-50" y1="-72" x2="50" y2="-72" stroke="#0277BD" stroke-width="0.5"/>
  <!-- Water surface -->
  <path d="M-50,-60 Q-40,-65 -30,-60 Q-20,-55 -10,-60 Q0,-65 10,-60 Q20,-55 30,-60 Q40,-65 50,-60" fill="none" stroke="#4FC3F7" stroke-width="1.5"/>
  <rect x="-50" y="-58" width="100" height="120" rx="2" fill="url(#waterGrad)" opacity="0.3"/>
  <!-- Fish -->
  <ellipse cx="-10" cy="-20" rx="15" ry="8" fill="#FFB74D" stroke="#E65100" stroke-width="1"/>
  <polygon points="-25,-20 -35,-28 -35,-12" fill="#FF9800" stroke="#E65100" stroke-width="0.8"/>
  <circle cx="-17" cy="-22" r="2" fill="#1B5E20"/>
  <path d="M-5,-20 Q0,-23 5,-20" fill="none" stroke="#E65100" stroke-width="0.8"/>
  <!-- Jellyfish -->
  <path d="M20,-30 Q30,-45 40,-30" fill="#E1BEE7" stroke="#9C27B0" stroke-width="0.8" opacity="0.7"/>
  <path d="M22,-30 Q22,-15 25,-5" fill="none" stroke="#9C27B0" stroke-width="0.5" opacity="0.5"/>
  <path d="M30,-30 Q30,-10 33,0" fill="none" stroke="#9C27B0" stroke-width="0.5" opacity="0.5"/>
  <path d="M38,-30 Q38,-15 41,-5" fill="none" stroke="#9C27B0" stroke-width="0.5" opacity="0.5"/>
  <!-- Seaweed -->
  <path d="M-30,50 Q-25,30 -30,10" fill="none" stroke="#4CAF50" stroke-width="2"/>
  <path d="M-30,40 Q-22,35 -25,30" fill="none" stroke="#4CAF50" stroke-width="1"/>
  <path d="M-30,25 Q-22,20 -25,15" fill="none" stroke="#4CAF50" stroke-width="1"/>
  <!-- Bottom -->
  <path d="M-50,55 Q-30,50 0,55 Q30,60 50,55" fill="#FFE0B2" stroke="#E65100" stroke-width="0.5"/>
  <text x="0" y="72" font-family="Arial,sans-serif" font-size="5.5" fill="#01579B" text-anchor="middle">Рыбы, водоросли,</text>
  <text x="0" y="80" font-family="Arial,sans-serif" font-size="5.5" fill="#01579B" text-anchor="middle">моллюски, раки</text>
</g>

<!-- Наземно-воздушная среда -->
<g transform="translate(250,170)">
  <rect x="-60" y="-95" width="120" height="175" rx="8" fill="white" opacity="0.9" stroke="#2E7D32" stroke-width="1.5"/>
  <text x="0" y="-78" font-family="Arial,sans-serif" font-size="8" fill="#1B5E20" text-anchor="middle" font-weight="bold">НАЗЕМНО-ВОЗДУШНАЯ</text>
  <line x1="-50" y1="-72" x2="50" y2="-72" stroke="#2E7D32" stroke-width="0.5"/>
  <!-- Sky -->
  <rect x="-50" y="-65" width="100" height="40" fill="#B3E5FC" opacity="0.5"/>
  <!-- Sun -->
  <circle cx="35" cy="-55" r="8" fill="#FFD54F" stroke="#F9A825" stroke-width="1"/>
  <line x1="35" y1="-67" x2="35" y2="-70" stroke="#F9A825" stroke-width="1"/>
  <line x1="47" y1="-55" x2="50" y2="-55" stroke="#F9A825" stroke-width="1"/>
  <line x1="43" y1="-63" x2="46" y2="-66" stroke="#F9A825" stroke-width="1"/>
  <!-- Cloud -->
  <ellipse cx="-15" cy="-55" rx="12" ry="6" fill="white" opacity="0.8"/>
  <ellipse cx="-5" cy="-55" rx="10" ry="5" fill="white" opacity="0.8"/>
  <!-- Tree -->
  <rect x="-5" y="-25" width="6" height="30" fill="#795548" stroke="#5D4037" stroke-width="0.5"/>
  <path d="M-20,-25 Q-10,-55 0,-45 Q10,-55 20,-25" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
  <path d="M-15,-20 Q-8,-35 0,-30 Q8,-35 15,-20" fill="#4CAF50"/>
  <!-- Bird -->
  <path d="M25,-40 Q30,-45 35,-40" fill="none" stroke="#333" stroke-width="1"/>
  <path d="M25,-40 Q30,-35 35,-40" fill="none" stroke="#333" stroke-width="1"/>
  <!-- Grass -->
  <path d="M-40,5 Q-38,-5 -35,5" fill="none" stroke="#4CAF50" stroke-width="1"/>
  <path d="M-35,5 Q-33,-3 -30,5" fill="none" stroke="#4CAF50" stroke-width="1"/>
  <path d="M30,5 Q32,-3 35,5" fill="none" stroke="#4CAF50" stroke-width="1"/>
  <!-- Ground -->
  <rect x="-50" y="5" width="100" height="55" fill="#C8E6C9" opacity="0.5"/>
  <path d="M-50,5 Q-25,0 0,5 Q25,10 50,5" fill="#8D6E63" opacity="0.3"/>
  <!-- Flower -->
  <line x1="30" y1="5" x2="30" y2="-5" stroke="#4CAF50" stroke-width="1"/>
  <circle cx="30" cy="-8" r="4" fill="#F44336" stroke="#C62828" stroke-width="0.5"/>
  <circle cx="30" cy="-8" r="1.5" fill="#FFD54F"/>
  <text x="0" y="40" font-family="Arial,sans-serif" font-size="5.5" fill="#1B5E20" text-anchor="middle">Млекопитающие, птицы,</text>
  <text x="0" y="48" font-family="Arial,sans-serif" font-size="5.5" fill="#1B5E20" text-anchor="middle">насекомые, растения</text>
  <text x="0" y="58" font-family="Arial,sans-serif" font-size="5" fill="#666" text-anchor="middle">Самая разнообразная</text>
  <text x="0" y="66" font-family="Arial,sans-serif" font-size="5" fill="#666" text-anchor="middle">среда обитания</text>
</g>

<!-- Почвенная среда -->
<g transform="translate(415,170)">
  <rect x="-60" y="-95" width="120" height="175" rx="8" fill="white" opacity="0.9" stroke="#795548" stroke-width="1.5"/>
  <text x="0" y="-78" font-family="Arial,sans-serif" font-size="9" fill="#4E342E" text-anchor="middle" font-weight="bold">ПОЧВЕННАЯ</text>
  <line x1="-50" y1="-72" x2="50" y2="-72" stroke="#795548" stroke-width="0.5"/>
  <!-- Surface line -->
  <path d="M-50,-55 Q-25,-50 0,-55 Q25,-60 50,-55" fill="none" stroke="#4CAF50" stroke-width="1"/>
  <path d="M-50,-55 Q-25,-50 0,-55 Q25,-60 50,-55 L50,55 L-50,55 Z" fill="#8D6E63" opacity="0.4"/>
  <!-- Roots -->
  <path d="M-10,-55 Q-12,-40 -15,-30" fill="none" stroke="#795548" stroke-width="1.5"/>
  <path d="M-15,-30 Q-20,-25 -25,-28" fill="none" stroke="#795548" stroke-width="0.8"/>
  <path d="M-15,-30 Q-10,-20 -5,-25" fill="none" stroke="#795548" stroke-width="0.8"/>
  <path d="M-15,-40 Q-8,-35 -3,-40" fill="none" stroke="#795548" stroke-width="0.8"/>
  <!-- Worm -->
  <path d="M-30,-10 Q-20,-15 -10,-10 Q0,-5 10,-10 Q20,-15 25,-10" fill="none" stroke="#FF8A65" stroke-width="3" stroke-linecap="round"/>
  <!-- Mole -->
  <ellipse cx="20" cy="15" rx="10" ry="7" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
  <circle cx="16" cy="12" r="1.5" fill="#1B5E20"/>
  <path d="M10,15 Q8,13 12,15" fill="none" stroke="#5D4037" stroke-width="0.8"/>
  <path d="M24,10 L28,6" stroke="#5D4037" stroke-width="0.8"/>
  <path d="M28,10 L32,6" stroke="#5D4037" stroke-width="0.8"/>
  <!-- Tunnel -->
  <path d="M-40,25 Q-20,20 0,25 Q20,30 40,25" fill="none" stroke="#5D4037" stroke-width="2" stroke-dasharray="3,2" opacity="0.5"/>
  <!-- Small organisms -->
  <circle cx="-25" cy="35" r="2" fill="#FFCC80" stroke="#E65100" stroke-width="0.5"/>
  <circle cx="-15" cy="40" r="1.5" fill="#FFCC80" stroke="#E65100" stroke-width="0.5"/>
  <circle cx="5" cy="38" r="1.5" fill="#FFCC80" stroke="#E65100" stroke-width="0.5"/>
  <text x="0" y="53" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Черви, кроты, насекомые</text>
  <text x="0" y="61" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">бактерии, грибы</text>
  <text x="0" y="72" font-family="Arial,sans-serif" font-size="5" fill="#999" text-anchor="middle">мало света и воздуха</text>
</g>

<!-- Organismal environment note -->
<rect x="30" y="310" width="440" height="25" rx="6" fill="white" opacity="0.9" stroke="#00838F" stroke-width="1"/>
<text x="250" y="327" font-family="Arial,sans-serif" font-size="7" fill="#006064" text-anchor="middle" font-weight="bold">4-я среда: Организм как среда обитания — вирусы, бактерии, паразиты живут внутри других организмов</text>
</svg>'''

print("Generating Grade 5 Biology SVGs...")
print()

write_svg("lesson1.svg", svg1)
write_svg("lesson2.svg", svg2)
write_svg("lesson3.svg", svg3)
write_svg("lesson4.svg", svg4)

print("\nFirst 4 lessons done. Continuing...")
