#!/usr/bin/env python3
"""Generate detailed biology SVG illustrations for Grade 5, Lessons 1-5"""

import os

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade5/biology"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def svg_wrap(inner, title, subtitle, color="#2E7D32", accent="#66BB6A"):
    """Wrap illustration content in a standard SVG frame"""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#E8F5E9"/>
      <stop offset="100%" stop-color="#C8E6C9"/>
    </linearGradient>
  </defs>
  <rect width="500" height="350" fill="url(#bg)" rx="10"/>
  <rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="{color}" stroke-width="2.5"/>
  <text x="250" y="30" font-family="Arial,sans-serif" font-size="16" font-weight="bold" fill="{color}" text-anchor="middle">{title}</text>
  <text x="250" y="46" font-family="Arial,sans-serif" font-size="10" fill="#888" text-anchor="middle">{subtitle}</text>
  <line x1="30" y1="52" x2="470" y2="52" stroke="{color}" stroke-width="1.5" opacity="0.25"/>
  {inner}
  <rect x="10" y="325" width="480" height="20" rx="4" fill="{color}" opacity="0.85"/>
  <text x="250" y="339" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="white" font-weight="bold">Биология 5 класс</text>
</svg>'''


# ===== LESSON 1: Биология — наука о живой природе =====
lesson1_illustration = '''
  <!-- Tree trunk -->
  <rect x="245" y="130" width="10" height="140" fill="#795548" rx="3"/>
  <!-- Roots -->
  <path d="M250 270 Q230 290 210 295" stroke="#795548" stroke-width="4" fill="none"/>
  <path d="M250 270 Q270 290 290 295" stroke="#795548" stroke-width="4" fill="none"/>
  <path d="M250 270 Q240 295 235 300" stroke="#795548" stroke-width="3" fill="none"/>
  <!-- Main branches -->
  <path d="M250 200 Q200 170 150 160" stroke="#795548" stroke-width="5" fill="none"/>
  <path d="M250 200 Q300 170 350 160" stroke="#795548" stroke-width="5" fill="none"/>
  <path d="M250 170 Q230 140 180 120" stroke="#795548" stroke-width="4" fill="none"/>
  <path d="M250 170 Q270 140 320 120" stroke="#795548" stroke-width="4" fill="none"/>
  <path d="M250 150 Q250 110 250 80" stroke="#795548" stroke-width="4" fill="none"/>
  <!-- Leaf clusters (Botany - green) -->
  <ellipse cx="140" cy="150" rx="40" ry="25" fill="#4CAF50" opacity="0.7"/>
  <ellipse cx="120" cy="140" rx="30" ry="20" fill="#66BB6A" opacity="0.6"/>
  <text x="140" y="155" font-family="Arial,sans-serif" font-size="10" fill="white" font-weight="bold" text-anchor="middle">Ботаника</text>
  <!-- Leaf clusters (Zoology - orange) -->
  <ellipse cx="360" cy="150" rx="40" ry="25" fill="#FF9800" opacity="0.7"/>
  <ellipse cx="380" cy="140" rx="30" ry="20" fill="#FFB74D" opacity="0.6"/>
  <text x="360" y="155" font-family="Arial,sans-serif" font-size="10" fill="white" font-weight="bold" text-anchor="middle">Зоология</text>
  <!-- Leaf clusters (Microbiology - purple) -->
  <ellipse cx="170" cy="110" rx="35" ry="20" fill="#9C27B0" opacity="0.6"/>
  <text x="170" y="115" font-family="Arial,sans-serif" font-size="9" fill="white" font-weight="bold" text-anchor="middle">Микробиология</text>
  <!-- Leaf clusters (Ecology - teal) -->
  <ellipse cx="330" cy="110" rx="35" ry="20" fill="#009688" opacity="0.6"/>
  <text x="330" y="115" font-family="Arial,sans-serif" font-size="9" fill="white" font-weight="bold" text-anchor="middle">Экология</text>
  <!-- Top leaf cluster (Biology) -->
  <ellipse cx="250" cy="72" rx="45" ry="22" fill="#2E7D32" opacity="0.8"/>
  <text x="250" y="76" font-family="Arial,sans-serif" font-size="11" fill="white" font-weight="bold" text-anchor="middle">БИОЛОГИЯ</text>
  <!-- Small decorative leaves -->
  <path d="M160 165 Q155 175 148 180" stroke="#4CAF50" stroke-width="1.5" fill="none"/>
  <path d="M340 165 Q345 175 352 180" stroke="#FF9800" stroke-width="1.5" fill="none"/>
  <!-- Ground -->
  <ellipse cx="250" cy="300" rx="80" ry="8" fill="#8D6E63" opacity="0.3"/>
'''

# ===== LESSON 2: Признаки живого =====
lesson2_illustration = '''
  <!-- Sign 1: Питание (Nutrition) - apple -->
  <g transform="translate(70,90)">
    <circle cx="0" cy="12" r="18" fill="#E53935" opacity="0.8"/>
    <path d="M0 -6 Q5 -15 10 -12" stroke="#4CAF50" stroke-width="2" fill="none"/>
    <ellipse cx="6" cy="-10" rx="6" ry="3" fill="#4CAF50" opacity="0.7" transform="rotate(-30,6,-10)"/>
    <text x="0" y="42" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Питание</text>
  </g>
  <!-- Sign 2: Дыхание (Respiration) - lungs -->
  <g transform="translate(180,90)">
    <path d="M0 -15 Q-20 -5 -18 15 Q-15 25 -5 20 Q0 15 0 10" fill="#FFAB91" stroke="#E64A19" stroke-width="1.5"/>
    <path d="M0 -15 Q20 -5 18 15 Q15 25 5 20 Q0 15 0 10" fill="#FFAB91" stroke="#E64A19" stroke-width="1.5"/>
    <path d="M0 -20 L0 -15" stroke="#795548" stroke-width="3"/>
    <text x="0" y="42" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Дыхание</text>
  </g>
  <!-- Sign 3: Рост (Growth) - plant growing -->
  <g transform="translate(290,90)">
    <rect x="-3" y="0" width="6" height="25" fill="#66BB6A" rx="2"/>
    <ellipse cx="-10" cy="-2" rx="12" ry="8" fill="#4CAF50" opacity="0.7" transform="rotate(30,-10,-2)"/>
    <ellipse cx="10" cy="-2" rx="12" ry="8" fill="#4CAF50" opacity="0.7" transform="rotate(-30,10,-2)"/>
    <path d="M0 -5 L0 -18" stroke="#4CAF50" stroke-width="2"/>
    <path d="M0 -18 L-4 -22 M0 -18 L4 -22" stroke="#4CAF50" stroke-width="1.5"/>
    <!-- arrow up -->
    <path d="M20 -10 L20 -25 L15 -20 M20 -25 L25 -20" stroke="#2E7D32" stroke-width="2" fill="none"/>
    <text x="0" y="42" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Рост</text>
  </g>
  <!-- Sign 4: Размножение (Reproduction) - cell division -->
  <g transform="translate(400,90)">
    <ellipse cx="-10" cy="0" rx="16" ry="14" fill="#CE93D8" stroke="#8E24AA" stroke-width="1.5" opacity="0.8"/>
    <ellipse cx="10" cy="0" rx="16" ry="14" fill="#CE93D8" stroke="#8E24AA" stroke-width="1.5" opacity="0.8"/>
    <circle cx="-10" cy="0" r="4" fill="#8E24AA" opacity="0.6"/>
    <circle cx="10" cy="0" r="4" fill="#8E24AA" opacity="0.6"/>
    <line x1="0" y1="-18" x2="0" y2="18" stroke="#8E24AA" stroke-width="1.5" stroke-dasharray="3,2"/>
    <text x="0" y="42" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Размножение</text>
  </g>
  <!-- Sign 5: Движение (Movement) - running figure -->
  <g transform="translate(125,185)">
    <circle cx="0" cy="-15" r="7" fill="#FFB74D" stroke="#E65100" stroke-width="1"/>
    <line x1="0" y1="-8" x2="0" y2="8" stroke="#E65100" stroke-width="2.5"/>
    <line x1="0" y1="-2" x2="-12" y2="-10" stroke="#E65100" stroke-width="2"/>
    <line x1="0" y1="-2" x2="12" y2="2" stroke="#E65100" stroke-width="2"/>
    <line x1="0" y1="8" x2="-8" y2="22" stroke="#E65100" stroke-width="2"/>
    <line x1="0" y1="8" x2="10" y2="20" stroke="#E65100" stroke-width="2"/>
    <!-- motion lines -->
    <line x1="-15" y1="0" x2="-22" y2="-2" stroke="#999" stroke-width="1" opacity="0.5"/>
    <line x1="-14" y1="6" x2="-21" y2="5" stroke="#999" stroke-width="1" opacity="0.5"/>
    <line x1="-13" y1="12" x2="-20" y2="12" stroke="#999" stroke-width="1" opacity="0.5"/>
    <text x="0" y="42" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Движение</text>
  </g>
  <!-- Sign 6: Раздражимость (Irritability) - touch-me-not plant -->
  <g transform="translate(340,185)">
    <rect x="-2" y="0" width="4" height="25" fill="#66BB6A" rx="1"/>
    <path d="M-2 0 Q-15 -10 -20 -5" stroke="#4CAF50" stroke-width="2" fill="none"/>
    <path d="M2 0 Q15 -10 20 -5" stroke="#4CAF50" stroke-width="2" fill="none"/>
    <!-- small leaves on branches -->
    <ellipse cx="-18" cy="-8" rx="5" ry="3" fill="#81C784" transform="rotate(-20,-18,-8)"/>
    <ellipse cx="18" cy="-8" rx="5" ry="3" fill="#81C784" transform="rotate(20,18,-8)"/>
    <!-- lightning bolt (stimulus) -->
    <path d="M25 -15 L22 -5 L27 -5 L23 5" stroke="#F44336" stroke-width="2" fill="none"/>
    <!-- exclamation -->
    <text x="30" y="-8" font-family="Arial,sans-serif" font-size="14" fill="#F44336" font-weight="bold">!</text>
    <text x="0" y="42" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Раздражимость</text>
  </g>
  <!-- Title box -->
  <rect x="120" y="260" width="260" height="30" rx="6" fill="#2E7D32" opacity="0.12"/>
  <text x="250" y="280" font-family="Arial,sans-serif" font-size="12" fill="#2E7D32" text-anchor="middle" font-weight="bold">6 признаков живого организма</text>
'''

# ===== LESSON 3: Методы биологических исследований =====
lesson3_illustration = '''
  <!-- Microscope -->
  <g transform="translate(90,100)">
    <!-- Base -->
    <rect x="-25" y="80" width="50" height="8" fill="#546E7A" rx="3"/>
    <!-- Arm -->
    <rect x="-5" y="20" width="10" height="65" fill="#78909C" rx="2"/>
    <!-- Stage -->
    <rect x="-20" y="55" width="40" height="5" fill="#90A4AE" rx="1"/>
    <!-- Eyepiece -->
    <rect x="-8" y="8" width="16" height="15" fill="#607D8B" rx="3"/>
    <ellipse cx="0" cy="8" rx="10" ry="4" fill="#455A64"/>
    <!-- Objective -->
    <rect x="-4" y="60" width="8" height="12" fill="#607D8B" rx="1"/>
    <!-- Focus knob -->
    <circle cx="8" cy="40" r="6" fill="#546E7A" stroke="#455A64" stroke-width="1"/>
    <text x="0" y="105" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Микроскоп</text>
  </g>
  <!-- Notebook -->
  <g transform="translate(230,100)">
    <rect x="-25" y="0" width="50" height="65" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5" rx="3"/>
    <!-- Spiral binding -->
    <circle cx="-25" cy="10" r="3" fill="none" stroke="#9E9E9E" stroke-width="1.5"/>
    <circle cx="-25" cy="22" r="3" fill="none" stroke="#9E9E9E" stroke-width="1.5"/>
    <circle cx="-25" cy="34" r="3" fill="none" stroke="#9E9E9E" stroke-width="1.5"/>
    <circle cx="-25" cy="46" r="3" fill="none" stroke="#9E9E9E" stroke-width="1.5"/>
    <!-- Lines -->
    <line x1="-15" y1="12" x2="20" y2="12" stroke="#BDBDBD" stroke-width="0.8"/>
    <line x1="-15" y1="20" x2="20" y2="20" stroke="#BDBDBD" stroke-width="0.8"/>
    <line x1="-15" y1="28" x2="20" y2="28" stroke="#BDBDBD" stroke-width="0.8"/>
    <line x1="-15" y1="36" x2="20" y2="36" stroke="#BDBDBD" stroke-width="0.8"/>
    <line x1="-15" y1="44" x2="20" y2="44" stroke="#BDBDBD" stroke-width="0.8"/>
    <line x1="-15" y1="52" x2="20" y2="52" stroke="#BDBDBD" stroke-width="0.8"/>
    <!-- Pencil -->
    <line x1="25" y1="5" x2="40" y2="60" stroke="#FDD835" stroke-width="4"/>
    <line x1="40" y1="60" x2="42" y2="65" stroke="#333" stroke-width="2"/>
    <text x="0" y="85" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Записи</text>
  </g>
  <!-- Test tubes -->
  <g transform="translate(380,100)">
    <rect x="-30" y="0" width="12" height="50" fill="#E3F2FD" stroke="#90CAF9" stroke-width="1.5" rx="0 0 6 6"/>
    <rect x="-30" y="30" width="12" height="20" fill="#81D4FA" rx="0 0 6 6" opacity="0.6"/>
    <rect x="-12" y="0" width="12" height="50" fill="#FCE4EC" stroke="#F48FB1" stroke-width="1.5" rx="0 0 6 6"/>
    <rect x="-12" y="25" width="12" height="25" fill="#F48FB1" rx="0 0 6 6" opacity="0.5"/>
    <rect x="6" y="0" width="12" height="50" fill="#E8F5E9" stroke="#A5D6A7" stroke-width="1.5" rx="0 0 6 6"/>
    <rect x="6" y="35" width="12" height="15" fill="#A5D6A7" rx="0 0 6 6" opacity="0.6"/>
    <!-- Rack -->
    <rect x="-35" y="-5" width="55" height="5" fill="#8D6E63" rx="2"/>
    <text x="0" y="70" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Опыты</text>
  </g>
  <!-- Method labels -->
  <rect x="40" y="250" width="130" height="22" rx="4" fill="#2E7D32" opacity="0.1"/>
  <text x="105" y="265" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle">Наблюдение</text>
  <rect x="185" y="250" width="130" height="22" rx="4" fill="#2E7D32" opacity="0.1"/>
  <text x="250" y="265" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle">Эксперимент</text>
  <rect x="330" y="250" width="130" height="22" rx="4" fill="#2E7D32" opacity="0.1"/>
  <text x="395" y="265" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle">Измерение</text>
'''

# ===== LESSON 4: Устройство увеличительных приборов =====
lesson4_illustration = '''
  <!-- Large microscope diagram -->
  <g transform="translate(180,70)">
    <!-- Base -->
    <path d="M-40 170 L-50 180 L50 180 L40 170 Z" fill="#546E7A"/>
    <rect x="-50" y="180" width="100" height="8" fill="#455A64" rx="2"/>
    <!-- Pillar -->
    <rect x="-6" y="40" width="12" height="135" fill="#78909C" rx="2"/>
    <!-- Arm -->
    <path d="M-6 40 Q-6 25 6 25 L20 25 Q25 25 25 30 L25 50" fill="#78909C" stroke="#607D8B" stroke-width="1"/>
    <!-- Stage -->
    <rect x="-30" y="120" width="60" height="6" fill="#90A4AE" rx="1"/>
    <!-- Stage clips -->
    <rect x="-28" y="118" width="8" height="10" fill="#B0BEC5" rx="1"/>
    <rect x="20" y="118" width="8" height="10" fill="#B0BEC5" rx="1"/>
    <!-- Slide on stage -->
    <rect x="-15" y="117" width="30" height="4" fill="#E3F2FD" stroke="#90CAF9" stroke-width="0.5" rx="1"/>
    <!-- Objective turret -->
    <rect x="-10" y="125" width="20" height="8" fill="#607D8B" rx="2"/>
    <!-- Objective lens -->
    <rect x="-3" y="133" width="6" height="15" fill="#546E7A" rx="1"/>
    <rect x="-5" y="148" width="10" height="3" fill="#455A64" rx="1"/>
    <!-- Eyepiece -->
    <rect x="-8" y="10" width="16" height="18" fill="#607D8B" rx="3"/>
    <ellipse cx="0" cy="10" rx="10" ry="4" fill="#455A64"/>
    <ellipse cx="0" cy="10" rx="6" ry="2.5" fill="#37474F"/>
    <!-- Coarse focus knob -->
    <circle cx="-12" cy="90" r="8" fill="#546E7A" stroke="#455A64" stroke-width="1"/>
    <line x1="-12" y1="82" x2="-12" y2="98" stroke="#455A64" stroke-width="1"/>
    <!-- Fine focus knob -->
    <circle cx="-12" cy="110" r="5" fill="#546E7A" stroke="#455A64" stroke-width="1"/>
    <!-- Mirror/Light -->
    <circle cx="0" cy="165" r="10" fill="#FFF176" stroke="#FDD835" stroke-width="1.5"/>
    <path d="M-7 160 Q0 155 7 160" fill="#FFEE58" opacity="0.5"/>
  </g>
  <!-- Labels with lines -->
  <line x1="230" y1="80" x2="310" y2="70" stroke="#333" stroke-width="0.8"/>
  <text x="315" y="74" font-family="Arial,sans-serif" font-size="9" fill="#333" font-weight="bold">Окуляр</text>
  <line x1="200" y1="210" x2="80" y2="200" stroke="#333" stroke-width="0.8"/>
  <text x="30" y="204" font-family="Arial,sans-serif" font-size="9" fill="#333" font-weight="bold">Объектив</text>
  <line x1="215" y1="195" x2="80" y2="230" stroke="#333" stroke-width="0.8"/>
  <text x="30" y="234" font-family="Arial,sans-serif" font-size="9" fill="#333" font-weight="bold">Предметный столик</text>
  <line x1="168" y1="165" x2="80" y2="165" stroke="#333" stroke-width="0.8"/>
  <text x="35" y="169" font-family="Arial,sans-serif" font-size="9" fill="#333" font-weight="bold">Винт настройки</text>
  <line x1="180" y1="240" x2="80" y2="260" stroke="#333" stroke-width="0.8"/>
  <text x="40" y="264" font-family="Arial,sans-serif" font-size="9" fill="#333" font-weight="bold">Зеркало/Подсветка</text>
  <line x1="230" y1="140" x2="330" y2="130" stroke="#333" stroke-width="0.8"/>
  <text x="335" y="134" font-family="Arial,sans-serif" font-size="9" fill="#333" font-weight="bold">Штатив</text>
  <line x1="245" y1="100" x2="340" y2="95" stroke="#333" stroke-width="0.8"/>
  <text x="345" y="99" font-family="Arial,sans-serif" font-size="8" fill="#333">Зрительная трубка</text>
  <!-- Magnification info -->
  <rect x="330" y="200" width="150" height="55" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="405" y="218" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Увеличение</text>
  <text x="405" y="232" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Окуляр x Объектив</text>
  <text x="405" y="246" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Напр: 10 x 40 = 400x</text>
'''

# ===== LESSON 5: Строение клетки =====
lesson5_illustration = '''
  <!-- Cell membrane (outer) -->
  <ellipse cx="220" cy="190" rx="130" ry="95" fill="#E8F5E9" stroke="#4CAF50" stroke-width="3"/>
  <!-- Cell membrane inner detail -->
  <ellipse cx="220" cy="190" rx="125" ry="90" fill="#F1F8E9" stroke="#81C784" stroke-width="1" stroke-dasharray="5,3"/>
  <!-- Cytoplasm texture (small dots) -->
  <circle cx="140" cy="160" r="2" fill="#A5D6A7" opacity="0.5"/>
  <circle cx="170" cy="220" r="2" fill="#A5D6A7" opacity="0.5"/>
  <circle cx="300" cy="170" r="2" fill="#A5D6A7" opacity="0.5"/>
  <circle cx="280" cy="240" r="2" fill="#A5D6A7" opacity="0.5"/>
  <circle cx="150" cy="200" r="2" fill="#A5D6A7" opacity="0.5"/>
  <circle cx="310" cy="210" r="2" fill="#A5D6A7" opacity="0.5"/>
  <!-- Nucleus -->
  <ellipse cx="220" cy="185" rx="40" ry="32" fill="#C8E6C9" stroke="#388E3C" stroke-width="2.5"/>
  <!-- Nuclear membrane -->
  <ellipse cx="220" cy="185" rx="36" ry="28" fill="none" stroke="#66BB6A" stroke-width="1" stroke-dasharray="3,2"/>
  <!-- Nucleolus -->
  <circle cx="225" cy="180" r="10" fill="#81C784" stroke="#388E3C" stroke-width="1.5"/>
  <!-- Chromatin threads -->
  <path d="M210 175 Q215 185 210 195" stroke="#4CAF50" stroke-width="1" fill="none" opacity="0.6"/>
  <path d="M230 175 Q235 185 230 195" stroke="#4CAF50" stroke-width="1" fill="none" opacity="0.6"/>
  <!-- Endoplasmic reticulum (rough) -->
  <path d="M130 150 Q140 140 155 145 Q170 150 165 160 Q160 170 150 165 Q140 160 130 165" stroke="#66BB6A" stroke-width="1.5" fill="none"/>
  <path d="M135 148 Q145 138 160 143" stroke="#66BB6A" stroke-width="1" fill="none"/>
  <!-- Ribosomes on rough ER -->
  <circle cx="137" cy="152" r="2" fill="#4CAF50"/>
  <circle cx="145" cy="147" r="2" fill="#4CAF50"/>
  <circle cx="155" cy="150" r="2" fill="#4CAF50"/>
  <circle cx="160" cy="158" r="2" fill="#4CAF50"/>
  <circle cx="150" cy="163" r="2" fill="#4CAF50"/>
  <!-- Endoplasmic reticulum (smooth) -->
  <path d="M290 155 Q300 148 310 155 Q315 162 305 165 Q295 168 290 160" stroke="#81C784" stroke-width="1.5" fill="none"/>
  <path d="M285 162 Q295 155 305 162" stroke="#81C784" stroke-width="1" fill="none"/>
  <!-- Mitochondria -->
  <g transform="translate(155,230) rotate(-20)">
    <ellipse cx="0" cy="0" rx="20" ry="10" fill="#FFCC80" stroke="#E65100" stroke-width="1.5"/>
    <path d="M-14 0 Q-7 -7 0 0 Q7 7 14 0" stroke="#E65100" stroke-width="1" fill="none"/>
    <path d="M-10 -2 Q-5 -5 0 -2 Q5 1 10 -2" stroke="#E65100" stroke-width="0.8" fill="none"/>
  </g>
  <!-- Second mitochondria -->
  <g transform="translate(300,210) rotate(30)">
    <ellipse cx="0" cy="0" rx="18" ry="9" fill="#FFCC80" stroke="#E65100" stroke-width="1.5"/>
    <path d="M-12 0 Q-6 -6 0 0 Q6 6 12 0" stroke="#E65100" stroke-width="1" fill="none"/>
    <path d="M-8 -2 Q-4 -5 0 -2 Q4 1 8 -2" stroke="#E65100" stroke-width="0.8" fill="none"/>
  </g>
  <!-- Vacuole -->
  <ellipse cx="280" cy="245" rx="22" ry="15" fill="#E1F5FE" stroke="#42A5F5" stroke-width="1.5" opacity="0.8"/>
  <!-- Golgi apparatus -->
  <g transform="translate(140,260)">
    <path d="M-15 -5 Q0 -12 15 -5" stroke="#AB47BC" stroke-width="2" fill="none"/>
    <path d="M-18 0 Q0 -8 18 0" stroke="#AB47BC" stroke-width="2" fill="none"/>
    <path d="M-15 5 Q0 -3 15 5" stroke="#AB47BC" stroke-width="2" fill="none"/>
    <path d="M-12 10 Q0 3 12 10" stroke="#AB47BC" stroke-width="2" fill="none"/>
    <!-- Vesicles -->
    <circle cx="-22" cy="0" r="4" fill="#CE93D8" stroke="#AB47BC" stroke-width="1"/>
    <circle cx="22" cy="5" r="3" fill="#CE93D8" stroke="#AB47BC" stroke-width="1"/>
  </g>
  <!-- Chloroplast -->
  <g transform="translate(310,240)">
    <ellipse cx="0" cy="0" rx="18" ry="10" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1.5"/>
    <!-- Grana inside -->
    <rect x="-8" y="-4" width="3" height="8" fill="#4CAF50" rx="1"/>
    <rect x="-2" y="-5" width="3" height="10" fill="#4CAF50" rx="1"/>
    <rect x="4" y="-3" width="3" height="7" fill="#4CAF50" rx="1"/>
  </g>
  <!-- Labels -->
  <line x1="220" y1="155" x2="220" y2="80" stroke="#333" stroke-width="0.7"/>
  <text x="220" y="75" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Ядро</text>
  <line x1="225" y1="178" x2="330" y2="90" stroke="#333" stroke-width="0.7"/>
  <text x="335" y="90" font-family="Arial,sans-serif" font-size="8" fill="#333" font-weight="bold">Ядрышко</text>
  <line x1="150" y1="155" x2="70" y2="90" stroke="#333" stroke-width="0.7"/>
  <text x="20" y="90" font-family="Arial,sans-serif" font-size="8" fill="#333" font-weight="bold">ЭПС (шероховатая)</text>
  <line x1="155" y1="235" x2="60" y2="260" stroke="#333" stroke-width="0.7"/>
  <text x="5" y="265" font-family="Arial,sans-serif" font-size="8" fill="#333" font-weight="bold">Митохондрия</text>
  <line x1="300" y1="215" x2="390" y2="160" stroke="#333" stroke-width="0.7"/>
  <text x="395" y="162" font-family="Arial,sans-serif" font-size="8" fill="#333" font-weight="bold">Митохондрия</text>
  <line x1="140" y1="265" x2="60" y2="295" stroke="#333" stroke-width="0.7"/>
  <text x="5" y="300" font-family="Arial,sans-serif" font-size="8" fill="#333" font-weight="bold">Комплекс Гольджи</text>
  <line x1="310" y1="245" x2="400" y2="260" stroke="#333" stroke-width="0.7"/>
  <text x="405" y="262" font-family="Arial,sans-serif" font-size="8" fill="#333" font-weight="bold">Хлоропласт</text>
  <line x1="280" y1="250" x2="390" y2="290" stroke="#333" stroke-width="0.7"/>
  <text x="395" y="293" font-family="Arial,sans-serif" font-size="8" fill="#333" font-weight="bold">Вакуоль</text>
  <line x1="345" y1="95" x2="400" y2="80" stroke="#333" stroke-width="0.7"/>
  <text x="405" y="82" font-family="Arial,sans-serif" font-size="8" fill="#333">ЭПС (гладкая)</text>
  <text x="350" y="310" font-family="Arial,sans-serif" font-size="8" fill="#4CAF50" font-weight="bold">Клеточная мембрана</text>
  <line x1="348" y1="303" x2="340" y2="195" stroke="#333" stroke-width="0.7"/>
'''

# Generate all SVGs
lessons = [
    (1, "Биология - наука о живой природе", lesson1_illustration),
    (2, "Признаки живого", lesson2_illustration),
    (3, "Методы биологических исследований", lesson3_illustration),
    (4, "Устройство увеличительных приборов", lesson4_illustration),
    (5, "Строение клетки", lesson5_illustration),
]

for num, title, illustration in lessons:
    subtitle = f"Биология 5 класс - Урок {num}"
    svg_content = svg_wrap(illustration, title, subtitle)
    filepath = os.path.join(OUTPUT_DIR, f"lesson{num}.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Generated: {filepath}")

print("\nDone! 5 SVGs generated for Grade 5 Biology.")
