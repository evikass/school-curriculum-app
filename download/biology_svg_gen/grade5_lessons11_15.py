#!/usr/bin/env python3
"""Generate detailed biology SVG illustrations for Grade 5, Lessons 11-15"""

import os

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade5/biology"

def svg_wrap(inner, title, subtitle, color="#2E7D32"):
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


# ===== LESSON 11: Разнообразие грибов =====
lesson11_illustration = '''
  <!-- Different types of fungi -->
  <!-- White mushroom (Боровик/Белый гриб) -->
  <g transform="translate(80,140)">
    <path d="M-25 0 Q-30 -20 -15 -28 Q0 -33 15 -28 Q30 -20 25 0 Z" fill="#8D6E63" stroke="#5D4037" stroke-width="1.5"/>
    <rect x="-6" y="0" width="12" height="30" fill="#D7CCC8" stroke="#BCAAA4" stroke-width="1" rx="4"/>
    <path d="M-6 30 Q-15 42 -20 45" stroke="#BCAAA4" stroke-width="2" fill="none"/>
    <path d="M6 30 Q15 42 20 45" stroke="#BCAAA4" stroke-width="2" fill="none"/>
    <text x="0" y="62" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Белый гриб</text>
    <text x="0" y="73" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(съедобный)</text>
  </g>
  <!-- Muhomor (Amanita) -->
  <g transform="translate(200,135)">
    <path d="M-28 0 Q-33 -25 -18 -35 Q0 -42 18 -35 Q33 -25 28 0 Z" fill="#E53935" stroke="#C62828" stroke-width="1.5"/>
    <!-- White spots -->
    <circle cx="-12" cy="-18" r="4" fill="white" opacity="0.8"/>
    <circle cx="8" cy="-22" r="3.5" fill="white" opacity="0.7"/>
    <circle cx="-2" cy="-10" r="3" fill="white" opacity="0.6"/>
    <circle cx="15" cy="-8" r="2.5" fill="white" opacity="0.5"/>
    <circle cx="-18" cy="-5" r="3" fill="white" opacity="0.5"/>
    <rect x="-5" y="0" width="10" height="35" fill="#FFF3E0" stroke="#D7CCC8" stroke-width="1" rx="3"/>
    <!-- Ring -->
    <ellipse cx="0" cy="12" rx="10" ry="3" fill="#FFECB3" stroke="#D7CCC8" stroke-width="0.8"/>
    <path d="M-5 35 Q-12 48 -18 50" stroke="#D7CCC8" stroke-width="1.5" fill="none"/>
    <path d="M5 35 Q12 48 18 50" stroke="#D7CCC8" stroke-width="1.5" fill="none"/>
    <!-- Skull warning -->
    <text x="32" y="-20" font-family="Arial,sans-serif" font-size="12" fill="#C62828" font-weight="bold">!</text>
    <text x="0" y="68" font-family="Arial,sans-serif" font-size="8" fill="#C62828" text-anchor="middle" font-weight="bold">Мухомор</text>
    <text x="0" y="79" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle">(ядовитый)</text>
  </g>
  <!-- Yeast (Дрожжи) -->
  <g transform="translate(330,140)">
    <ellipse cx="-10" cy="-5" rx="10" ry="8" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/>
    <!-- Budding yeast -->
    <ellipse cx="5" cy="-12" rx="7" ry="6" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.2"/>
    <path d="M-2 -8 Q2 -12 2 -10" stroke="#F9A825" stroke-width="1" fill="none"/>
    <ellipse cx="-18" cy="5" rx="8" ry="6" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.2"/>
    <!-- Bubbles -->
    <circle cx="-5" cy="-25" r="3" fill="none" stroke="#FDD835" stroke-width="0.8" opacity="0.6"/>
    <circle cx="5" cy="-30" r="2" fill="none" stroke="#FDD835" stroke-width="0.8" opacity="0.5"/>
    <circle cx="-10" cy="-28" r="2.5" fill="none" stroke="#FDD835" stroke-width="0.8" opacity="0.4"/>
    <text x="0" y="25" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Дрожжи</text>
    <text x="0" y="36" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(одноклеточные)</text>
  </g>
  <!-- Mold (Плесневый гриб) -->
  <g transform="translate(430,140)">
    <!-- Bread substrate -->
    <rect x="-20" y="5" width="40" height="20" fill="#D7CCC8" stroke="#BCAAA4" stroke-width="1" rx="3"/>
    <!-- Mold hyphae -->
    <line x1="-8" y1="5" x2="-10" y2="-15" stroke="#8BC34A" stroke-width="1.5"/>
    <line x1="0" y1="5" x2="2" y2="-18" stroke="#8BC34A" stroke-width="1.5"/>
    <line x1="8" y1="5" x2="12" y2="-12" stroke="#8BC34A" stroke-width="1.5"/>
    <!-- Spore heads -->
    <circle cx="-10" cy="-17" r="5" fill="#689F38" opacity="0.7"/>
    <circle cx="2" cy="-20" r="6" fill="#7CB342" opacity="0.7"/>
    <circle cx="12" cy="-14" r="4" fill="#689F38" opacity="0.7"/>
    <!-- Spores -->
    <circle cx="-14" cy="-22" r="1.5" fill="#33691E" opacity="0.5"/>
    <circle cx="-6" cy="-24" r="1" fill="#33691E" opacity="0.4"/>
    <circle cx="6" cy="-28" r="1.5" fill="#33691E" opacity="0.5"/>
    <circle cx="16" cy="-19" r="1" fill="#33691E" opacity="0.4"/>
    <text x="0" y="40" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Плесень</text>
    <text x="0" y="51" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(Пеницилл)</text>
  </g>
  <!-- Bracket fungus on tree -->
  <g transform="translate(80,260)">
    <!-- Tree trunk -->
    <rect x="-5" y="-30" width="25" height="50" fill="#795548" rx="3"/>
    <!-- Bracket fungi -->
    <path d="M20 -15 Q30 -25 45 -20 Q40 -12 20 -10 Z" fill="#FF8F00" stroke="#E65100" stroke-width="1"/>
    <path d="M20 -2 Q28 -10 40 -7 Q35 0 20 2 Z" fill="#FFA000" stroke="#E65100" stroke-width="1"/>
    <path d="M20 10 Q26 4 36 5 Q32 12 20 14 Z" fill="#FFB300" stroke="#E65100" stroke-width="1"/>
    <text x="25" y="35" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Трутовик</text>
  </g>
  <!-- Summary -->
  <rect x="160" y="255" width="310" height="50" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="315" y="272" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Группы грибов</text>
  <text x="315" y="287" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Шляпочные | Плесневые | Дрожжи | Трутовики</text>
  <text x="315" y="300" font-family="Arial,sans-serif" font-size="7" fill="#999" text-anchor="middle">Съедобные и ядовитые</text>
'''

# ===== LESSON 12: Лишайники =====
lesson12_illustration = '''
  <!-- Three types of lichens -->
  <!-- Crustose (Корковые/Накипные) -->
  <g transform="translate(80,100)">
    <!-- Rock substrate -->
    <ellipse cx="0" cy="15" rx="45" ry="20" fill="#9E9E9E" stroke="#757575" stroke-width="1.5"/>
    <!-- Crustose lichen on rock -->
    <ellipse cx="-5" cy="5" rx="25" ry="10" fill="#8BC34A" opacity="0.7" stroke="#689F38" stroke-width="1"/>
    <ellipse cx="10" cy="0" rx="15" ry="8" fill="#9CCC65" opacity="0.5"/>
    <circle cx="-10" cy="3" r="2" fill="#33691E" opacity="0.4"/>
    <circle cx="0" cy="5" r="1.5" fill="#33691E" opacity="0.3"/>
    <circle cx="8" cy="2" r="2" fill="#33691E" opacity="0.4"/>
    <text x="0" y="42" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Накипные</text>
  </g>
  <!-- Foliose (Листоватые) -->
  <g transform="translate(230,100)">
    <!-- Tree bark -->
    <rect x="-30" y="10" width="60" height="30" fill="#795548" stroke="#5D4037" stroke-width="1" rx="3"/>
    <!-- Foliose lichen -->
    <path d="M-20 8 Q-15 -5 0 -8 Q15 -5 20 8 Q10 5 0 6 Q-10 5 -20 8 Z" fill="#81C784" stroke="#4CAF50" stroke-width="1.5"/>
    <path d="M-15 5 Q-10 -2 0 -3 Q10 -2 15 5" fill="#A5D6A7" opacity="0.6"/>
    <!-- Ruffled edges -->
    <path d="M-18 8 Q-22 6 -25 10" stroke="#4CAF50" stroke-width="1" fill="none"/>
    <path d="M18 8 Q22 6 25 10" stroke="#4CAF50" stroke-width="1" fill="none"/>
    <text x="0" y="55" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Листоватые</text>
  </g>
  <!-- Fruticose (Кустистые) -->
  <g transform="translate(380,95)">
    <!-- Ground -->
    <ellipse cx="0" cy="40" rx="35" ry="6" fill="#8D6E63" opacity="0.3"/>
    <!-- Fruticose lichen branches -->
    <path d="M0 40 L0 15 L-10 -5 L-15 -15" stroke="#7CB342" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M0 15 L10 -5 L15 -15" stroke="#7CB342" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M0 25 L-15 10 L-20 0" stroke="#8BC34A" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <path d="M0 25 L12 8 L18 -5" stroke="#8BC34A" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <!-- Small branches -->
    <path d="M-10 -5 L-18 -8" stroke="#9CCC65" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <path d="M10 -5 L18 -8" stroke="#9CCC65" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <path d="M-15 10 L-22 5" stroke="#9CCC65" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <path d="M12 8 L20 3" stroke="#9CCC65" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <text x="0" y="58" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Кустистые</text>
  </g>
  <!-- Symbiosis diagram -->
  <g transform="translate(250,230)">
    <!-- Fungus circle -->
    <circle cx="-50" cy="0" r="30" fill="#FFCC80" stroke="#E65100" stroke-width="2" opacity="0.7"/>
    <text x="-50" y="-3" font-family="Arial,sans-serif" font-size="8" fill="#BF360C" text-anchor="middle" font-weight="bold">Гриб</text>
    <text x="-50" y="8" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle">(гетеротроф)</text>
    <!-- Alga circle -->
    <circle cx="50" cy="0" r="30" fill="#A5D6A7" stroke="#2E7D32" stroke-width="2" opacity="0.7"/>
    <text x="50" y="-3" font-family="Arial,sans-serif" font-size="8" fill="#1B5E20" text-anchor="middle" font-weight="bold">Водоросль</text>
    <text x="50" y="8" font-family="Arial,sans-serif" font-size="7" fill="#1B5E20" text-anchor="middle">(автотроф)</text>
    <!-- Overlap = lichen -->
    <ellipse cx="0" cy="0" rx="15" ry="20" fill="#C8E6C9" stroke="#689F38" stroke-width="1.5"/>
    <text x="0" y="3" font-family="Arial,sans-serif" font-size="7" fill="#33691E" text-anchor="middle" font-weight="bold">Лишайник</text>
    <!-- Arrows -->
    <text x="-28" y="-15" font-family="Arial,sans-serif" font-size="6" fill="#555">вода, минералы</text>
    <path d="M-25 -18 L-10 -12" stroke="#555" stroke-width="0.8" fill="none"/>
    <text x="8" y="25" font-family="Arial,sans-serif" font-size="6" fill="#555">органические вещества</text>
    <path d="M12 22 L-5 15" stroke="#555" stroke-width="0.8" fill="none"/>
  </g>
  <!-- Bottom note -->
  <text x="250" y="310" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Лишайники - индикаторы чистоты воздуха</text>
'''

# ===== LESSON 13: Общая характеристика растений =====
lesson13_illustration = '''
  <!-- Plant kingdom classification tree -->
  <!-- Root -->
  <rect x="235" y="250" width="30" height="40" fill="#795548" rx="3"/>
  <path d="M250 290 Q230 305 220 310" stroke="#795548" stroke-width="3" fill="none"/>
  <path d="M250 290 Q270 305 280 310" stroke="#795548" stroke-width="3" fill="none"/>
  <!-- Trunk -->
  <rect x="240" y="155" width="20" height="100" fill="#795548" rx="3"/>
  <!-- Main title -->
  <ellipse cx="250" cy="135" rx="55" ry="20" fill="#2E7D32" opacity="0.8"/>
  <text x="250" y="140" font-family="Arial,sans-serif" font-size="11" fill="white" text-anchor="middle" font-weight="bold">Растения</text>
  <!-- Branch: Водоросли -->
  <path d="M240 170 Q180 155 130 140" stroke="#795548" stroke-width="3" fill="none"/>
  <ellipse cx="115" cy="135" rx="45" ry="18" fill="#4CAF50" opacity="0.7"/>
  <text x="115" y="140" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Водоросли</text>
  <text x="115" y="165" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Нет тканей и органов</text>
  <!-- Branch: Мхи -->
  <path d="M240 190 Q175 185 130 180" stroke="#795548" stroke-width="3" fill="none"/>
  <ellipse cx="115" cy="175" rx="45" ry="18" fill="#66BB6A" opacity="0.7"/>
  <text x="115" y="180" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Мхи</text>
  <text x="115" y="205" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Нет корней и цветков</text>
  <!-- Branch: Папоротники -->
  <path d="M260 175 Q320 160 370 148" stroke="#795548" stroke-width="3" fill="none"/>
  <ellipse cx="385" cy="143" rx="50" ry="18" fill="#43A047" opacity="0.7"/>
  <text x="385" y="148" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Папоротники</text>
  <text x="385" y="173" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Есть корни, нет семян</text>
  <!-- Branch: Голосеменные -->
  <path d="M260 195 Q325 200 370 205" stroke="#795548" stroke-width="3" fill="none"/>
  <ellipse cx="385" cy="200" rx="50" ry="18" fill="#2E7D32" opacity="0.7"/>
  <text x="385" y="205" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Голосеменные</text>
  <text x="385" y="230" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Семена без плода</text>
  <!-- Branch: Покрытосеменные -->
  <path d="M250 210 Q250 225 250 230" stroke="#795548" stroke-width="3" fill="none"/>
  <ellipse cx="250" cy="250" rx="0" ry="0"/>
  <!-- Arrow pointing down -->
  <rect x="155" y="260" width="190" height="25" rx="6" fill="#1B5E20" opacity="0.8"/>
  <text x="250" y="277" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">Покрытосеменные (цветковые)</text>
  <!-- Plant characteristics -->
  <rect x="20" y="230" width="120" height="70" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="80" y="247" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Признаки растений</text>
  <text x="30" y="261" font-family="Arial,sans-serif" font-size="7" fill="#555">- Автотрофы (фотосинтез)</text>
  <text x="30" y="273" font-family="Arial,sans-serif" font-size="7" fill="#555">- Клетки с клеточ. стенкой</text>
  <text x="30" y="285" font-family="Arial,sans-serif" font-size="7" fill="#555">- Неподвижны</text>
  <text x="30" y="297" font-family="Arial,sans-serif" font-size="7" fill="#555">- Растут всю жизнь</text>
'''

# ===== LESSON 14: Водоросли — древнейшие растения =====
lesson14_illustration = '''
  <!-- Different algae types -->
  <!-- Green algae (Зелёные водоросли) -->
  <g transform="translate(85,130)">
    <!-- Water background -->
    <rect x="-55" y="-50" width="110" height="110" fill="#E0F7FA" stroke="#80DEEA" stroke-width="1" rx="5" opacity="0.5"/>
    <!-- Spirogyra filament -->
    <rect x="-5" y="-40" width="10" height="20" fill="#81C784" stroke="#4CAF50" stroke-width="1" rx="5"/>
    <rect x="-5" y="-18" width="10" height="20" fill="#81C784" stroke="#4CAF50" stroke-width="1" rx="5"/>
    <rect x="-5" y="4" width="10" height="20" fill="#81C784" stroke="#4CAF50" stroke-width="1" rx="5"/>
    <rect x="-5" y="26" width="10" height="20" fill="#81C784" stroke="#4CAF50" stroke-width="1" rx="5"/>
    <!-- Chloroplast spiral -->
    <path d="M-3 -35 Q3 -30 -3 -25 Q3 -20 -3 -15" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
    <path d="M-3 -13 Q3 -8 -3 -3 Q3 2 -3 7" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
    <!-- Nucleus -->
    <circle cx="0" cy="-28" r="3" fill="#4CAF50"/>
    <circle cx="0" cy="-6" r="3" fill="#4CAF50"/>
    <circle cx="0" cy="16" r="3" fill="#4CAF50"/>
    <text x="0" y="75" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Зелёные</text>
    <text x="0" y="86" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(Спирогира)</text>
  </g>
  <!-- Brown algae (Бурые водоросли) - Kelp -->
  <g transform="translate(250,130)">
    <rect x="-60" y="-50" width="120" height="110" fill="#FFF3E0" stroke="#FFE0B2" stroke-width="1" rx="5" opacity="0.5"/>
    <!-- Holdfast -->
    <path d="M0 45 Q-10 50 -15 55" stroke="#795548" stroke-width="3" fill="none"/>
    <path d="M0 45 Q10 50 15 55" stroke="#795548" stroke-width="3" fill="none"/>
    <!-- Stipe -->
    <rect x="-3" y="-10" width="6" height="55" fill="#8D6E63" rx="2"/>
    <!-- Blade/Thallus -->
    <path d="M-3 -10 Q-30 -25 -35 -5 Q-25 0 -3 -5" fill="#A1887F" stroke="#795548" stroke-width="1"/>
    <path d="M3 -10 Q30 -25 35 -5 Q25 0 3 -5" fill="#A1887F" stroke="#795548" stroke-width="1"/>
    <!-- Top blade -->
    <path d="M-3 -10 Q-20 -35 -15 -40 Q0 -30 3 -10" fill="#BCAAA4" stroke="#795548" stroke-width="0.8"/>
    <path d="M3 -10 Q20 -35 15 -40 Q0 -30 -3 -10" fill="#BCAAA4" stroke="#795548" stroke-width="0.8"/>
    <!-- Air bladders -->
    <circle cx="-15" cy="-15" r="4" fill="#D7CCC8" stroke="#8D6E63" stroke-width="0.8"/>
    <circle cx="15" cy="-15" r="4" fill="#D7CCC8" stroke="#8D6E63" stroke-width="0.8"/>
    <text x="0" y="75" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Бурые</text>
    <text x="0" y="86" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(Ламинария)</text>
  </g>
  <!-- Red algae (Красные водоросли) -->
  <g transform="translate(415,130)">
    <rect x="-50" y="-50" width="100" height="110" fill="#FCE4EC" stroke="#F8BBD0" stroke-width="1" rx="5" opacity="0.5"/>
    <!-- Branching thallus -->
    <path d="M0 45 L0 10 L-15 -10 L-25 -25" stroke="#E91E63" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <path d="M0 10 L15 -10 L25 -25" stroke="#E91E63" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <path d="M0 25 L-20 10 L-30 -5" stroke="#EC407A" stroke-width="2" fill="none" stroke-linecap="round"/>
    <path d="M0 25 L20 10 L30 -5" stroke="#EC407A" stroke-width="2" fill="none" stroke-linecap="round"/>
    <!-- Small branches -->
    <path d="M-15 -10 L-22 -18" stroke="#F06292" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <path d="M15 -10 L22 -18" stroke="#F06292" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <path d="M-20 10 L-28 3" stroke="#F06292" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <path d="M20 10 L28 3" stroke="#F06292" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <text x="0" y="75" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Красные</text>
    <text x="0" y="86" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(Порфира)</text>
  </g>
  <!-- Info box -->
  <rect x="60" y="245" width="380" height="55" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="262" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Особенности водорослей</text>
  <text x="250" y="277" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Нет корней, стеблей и листьев (слоевище/таллом)</text>
  <text x="250" y="292" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Обитают в воде - основа кислородного баланса планеты</text>
'''

# ===== LESSON 15: Мхи, папоротники и голосеменные =====
lesson15_illustration = '''
  <!-- Three plant groups side by side -->
  <!-- Moss (Мох) -->
  <g transform="translate(85,160)">
    <!-- Ground -->
    <ellipse cx="0" cy="65" rx="55" ry="8" fill="#8D6E63" opacity="0.3"/>
    <!-- Moss stems -->
    <rect x="-2" y="20" width="4" height="45" fill="#66BB6A" rx="2"/>
    <rect x="-17" y="25" width="3" height="40" fill="#81C784" rx="1.5"/>
    <rect x="14" y="22" width="3" height="43" fill="#81C784" rx="1.5"/>
    <!-- Leaves (small) -->
    <ellipse cx="-8" cy="30" rx="6" ry="3" fill="#4CAF50" opacity="0.7"/>
    <ellipse cx="8" cy="28" rx="6" ry="3" fill="#4CAF50" opacity="0.7"/>
    <ellipse cx="-12" cy="40" rx="5" ry="2.5" fill="#66BB6A" opacity="0.6"/>
    <ellipse cx="10" cy="38" rx="5" ry="2.5" fill="#66BB6A" opacity="0.6"/>
    <!-- Sporangium capsule -->
    <ellipse cx="0" cy="10" rx="6" ry="10" fill="#A5D6A7" stroke="#4CAF50" stroke-width="1"/>
    <!-- Lid -->
    <ellipse cx="0" cy="2" rx="5" ry="2" fill="#81C784"/>
    <!-- Seta (stalk) -->
    <line x1="0" y1="20" x2="0" y2="10" stroke="#4CAF50" stroke-width="1.5"/>
    <!-- Rhizoids (not roots!) -->
    <path d="M0 65 Q-5 72 -8 78" stroke="#BCAAA4" stroke-width="1" fill="none"/>
    <path d="M0 65 Q5 72 8 78" stroke="#BCAAA4" stroke-width="1" fill="none"/>
    <path d="M0 65 Q-2 75 -3 80" stroke="#BCAAA4" stroke-width="0.8" fill="none"/>
    <text x="0" y="95" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Мхи</text>
    <text x="0" y="107" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle">Нет корней (ризоиды)</text>
    <text x="0" y="118" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Споры в коробочке</text>
  </g>
  <!-- Fern (Папоротник) -->
  <g transform="translate(250,150)">
    <!-- Ground -->
    <ellipse cx="0" cy="70" rx="60" ry="8" fill="#8D6E63" opacity="0.3"/>
    <!-- Stem -->
    <rect x="-3" y="10" width="6" height="60" fill="#795548" rx="2"/>
    <!-- Fronds (leaves) -->
    <path d="M0 10 Q-40 -20 -60 -40" stroke="#2E7D32" stroke-width="3" fill="none"/>
    <path d="M0 10 Q40 -20 60 -40" stroke="#2E7D32" stroke-width="3" fill="none"/>
    <path d="M0 20 Q-35 -5 -55 -25" stroke="#43A047" stroke-width="2.5" fill="none"/>
    <path d="M0 20 Q35 -5 55 -25" stroke="#43A047" stroke-width="2.5" fill="none"/>
    <!-- Leaflets on fronds -->
    <path d="M-25 -10 Q-35 -15 -30 -5" fill="#66BB6A" opacity="0.6"/>
    <path d="M25 -10 Q35 -15 30 -5" fill="#66BB6A" opacity="0.6"/>
    <path d="M-40 -25 Q-50 -30 -45 -20" fill="#66BB6A" opacity="0.5"/>
    <path d="M40 -25 Q50 -30 45 -20" fill="#66BB6A" opacity="0.5"/>
    <!-- Sorus (spore clusters) on back of leaf -->
    <circle cx="-35" cy="-18" r="3" fill="#8D6E63" opacity="0.6"/>
    <circle cx="-45" cy="-30" r="2.5" fill="#8D6E63" opacity="0.6"/>
    <circle cx="35" cy="-18" r="3" fill="#8D6E63" opacity="0.6"/>
    <circle cx="45" cy="-30" r="2.5" fill="#8D6E63" opacity="0.6"/>
    <!-- Fiddlehead (young frond) -->
    <path d="M0 5 Q-5 -5 -3 -10 Q0 -15 3 -10 Q5 -5 0 5" fill="#81C784" stroke="#4CAF50" stroke-width="1"/>
    <!-- Roots -->
    <path d="M0 70 Q-10 80 -15 88" stroke="#795548" stroke-width="2" fill="none"/>
    <path d="M0 70 Q10 80 15 88" stroke="#795548" stroke-width="2" fill="none"/>
    <path d="M0 70 Q0 82 0 90" stroke="#795548" stroke-width="1.5" fill="none"/>
    <text x="0" y="100" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Папоротники</text>
    <text x="0" y="112" font-family="Arial,sans-serif" font-size="7" fill="#4CAF50" text-anchor="middle">Есть корни и листья</text>
    <text x="0" y="123" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Споры на листьях</text>
  </g>
  <!-- Conifer (Голосеменные) -->
  <g transform="translate(415,150)">
    <!-- Ground -->
    <ellipse cx="0" cy="70" rx="40" ry="6" fill="#8D6E63" opacity="0.3"/>
    <!-- Trunk -->
    <rect x="-5" y="-10" width="10" height="80" fill="#795548" rx="2"/>
    <!-- Tree crown (triangular) -->
    <path d="M0 -60 L-35 -10 L35 -10 Z" fill="#2E7D32" opacity="0.8"/>
    <path d="M0 -50 L-28 -5 L28 -5 Z" fill="#388E3C" opacity="0.7"/>
    <path d="M0 -40 L-20 5 L20 5 Z" fill="#43A047" opacity="0.6"/>
    <!-- Cones -->
    <ellipse cx="-20" cy="0" rx="6" ry="10" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
    <ellipse cx="18" cy="5" rx="5" ry="8" fill="#A1887F" stroke="#795548" stroke-width="1"/>
    <!-- Cone scales -->
    <path d="M-24 -2 L-20 -5 L-16 -2" stroke="#5D4037" stroke-width="0.8" fill="none"/>
    <path d="M-24 3 L-20 0 L-16 3" stroke="#5D4037" stroke-width="0.8" fill="none"/>
    <!-- Roots -->
    <path d="M0 70 Q-15 82 -20 90" stroke="#795548" stroke-width="2" fill="none"/>
    <path d="M0 70 Q15 82 20 90" stroke="#795548" stroke-width="2" fill="none"/>
    <text x="0" y="100" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Голосеменные</text>
    <text x="0" y="112" font-family="Arial,sans-serif" font-size="7" fill="#4CAF50" text-anchor="middle">Семена в шишках</text>
    <text x="0" y="123" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Нет плодов/цветков</text>
  </g>
  <!-- Evolution arrow at top -->
  <rect x="40" y="62" width="420" height="20" rx="4" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.8"/>
  <text x="250" y="76" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">Эволюция: от простых (без корней) к сложным (семена)</text>
  <path d="M60 72 L440 72" stroke="#2E7D32" stroke-width="1.5"/>
  <path d="M440 72 L435 68 M440 72 L435 76" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
'''

# Generate all SVGs
lessons = [
    (11, "Разнообразие грибов", lesson11_illustration),
    (12, "Лишайники", lesson12_illustration),
    (13, "Общая характеристика растений", lesson13_illustration),
    (14, "Водоросли - древнейшие растения", lesson14_illustration),
    (15, "Мхи, папоротники и голосеменные", lesson15_illustration),
]

for num, title, illustration in lessons:
    subtitle = f"Биология 5 класс - Урок {num}"
    svg_content = svg_wrap(illustration, title, subtitle)
    filepath = os.path.join(OUTPUT_DIR, f"lesson{num}.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Generated: {filepath}")

print("\nDone! 5 SVGs generated for Grade 5 Biology Lessons 11-15.")
