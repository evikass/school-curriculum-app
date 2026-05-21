#!/usr/bin/env python3
"""Generate detailed biology SVG illustrations for Grade 5, Lessons 21-23"""

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


# ===== LESSON 21: Среды жизни организмов =====
lesson21_illustration = '''
  <!-- Four environments -->
  <!-- Водная среда (Water) -->
  <g transform="translate(75,130)">
    <!-- Water background -->
    <rect x="-55" y="-40" width="110" height="95" fill="#E3F2FD" stroke="#42A5F5" stroke-width="1.5" rx="5"/>
    <!-- Waves on top -->
    <path d="M-55 -40 Q-40 -45 -25 -40 Q-10 -35 0 -40 Q10 -45 25 -40 Q40 -35 55 -40" stroke="#42A5F5" stroke-width="1.5" fill="none"/>
    <!-- Fish -->
    <ellipse cx="0" cy="-5" rx="20" ry="10" fill="#64B5F6" stroke="#1565C0" stroke-width="1"/>
    <path d="M20 -5 L30 -14 L30 4 Z" fill="#64B5F6" stroke="#1565C0" stroke-width="0.8"/>
    <circle cx="-10" cy="-7" r="2" fill="#1565C0"/>
    <!-- Seaweed -->
    <path d="M-25 50 Q-28 30 -22 15" stroke="#4CAF50" stroke-width="2" fill="none"/>
    <path d="M-20 50 Q-15 25 -18 10" stroke="#66BB6A" stroke-width="2" fill="none"/>
    <path d="M25 50 Q28 30 22 18" stroke="#4CAF50" stroke-width="2" fill="none"/>
    <!-- Bubbles -->
    <circle cx="10" cy="-20" r="3" fill="none" stroke="#90CAF9" stroke-width="0.8"/>
    <circle cx="15" cy="-30" r="2" fill="none" stroke="#90CAF9" stroke-width="0.8"/>
    <!-- Sand bottom -->
    <path d="M-55 45 Q-30 50 0 48 Q30 50 55 45" fill="#FFE0B2" stroke="#FFCC80" stroke-width="1"/>
    <text x="0" y="70" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" text-anchor="middle" font-weight="bold">Водная</text>
    <text x="0" y="82" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Обитатели воды</text>
  </g>
  <!-- Наземно-воздушная (Land-Air) -->
  <g transform="translate(210,130)">
    <!-- Sky -->
    <rect x="-55" y="-40" width="110" height="50" fill="#E1F5FE" rx="5"/>
    <!-- Sun -->
    <circle cx="35" cy="-25" r="10" fill="#FFF176" stroke="#FDD835" stroke-width="1"/>
    <!-- Ground -->
    <rect x="-55" y="10" width="110" height="45" fill="#C8E6C9" rx="0 0 5 5"/>
    <!-- Tree -->
    <rect x="-5" y="-5" width="6" height="20" fill="#795548" rx="1"/>
    <circle cx="-2" cy="-15" r="15" fill="#4CAF50" opacity="0.8"/>
    <circle cx="8" cy="-10" r="12" fill="#66BB6A" opacity="0.7"/>
    <!-- Bird -->
    <path d="M-25 -20 Q-20 -28 -15 -22 Q-10 -28 -5 -20" stroke="#333" stroke-width="1.5" fill="none"/>
    <!-- Flower -->
    <line x1="30" y1="15" x2="30" y2="5" stroke="#4CAF50" stroke-width="1.5"/>
    <circle cx="30" cy="2" r="4" fill="#E53935" opacity="0.7"/>
    <!-- Grass -->
    <path d="M-40 12 Q-38 5 -35 10" stroke="#4CAF50" stroke-width="1" fill="none"/>
    <path d="M-35 12 Q-32 3 -30 10" stroke="#66BB6A" stroke-width="1" fill="none"/>
    <text x="0" y="70" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Наземно-воздушная</text>
    <text x="0" y="82" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Растения, животные, грибы</text>
  </g>
  <!-- Почвенная (Soil) -->
  <g transform="translate(340,130)">
    <!-- Soil cross-section -->
    <rect x="-55" y="-40" width="110" height="95" fill="#8D6E63" rx="5"/>
    <!-- Surface with grass -->
    <path d="M-55 -40 Q-30 -45 0 -40 Q30 -35 55 -40" fill="#81C784" stroke="#4CAF50" stroke-width="1.5"/>
    <!-- Grass blades -->
    <line x1="-30" y1="-40" x2="-32" y2="-48" stroke="#4CAF50" stroke-width="1.5"/>
    <line x1="-15" y1="-40" x2="-13" y2="-50" stroke="#4CAF50" stroke-width="1.5"/>
    <line x1="10" y1="-38" x2="12" y2="-48" stroke="#4CAF50" stroke-width="1.5"/>
    <line x1="30" y1="-38" x2="32" y2="-46" stroke="#4CAF50" stroke-width="1.5"/>
    <!-- Roots -->
    <path d="M0 -40 L0 -10 L-10 10 L-15 25" stroke="#795548" stroke-width="2" fill="none"/>
    <path d="M0 -10 L10 10 L15 25" stroke="#795548" stroke-width="2" fill="none"/>
    <path d="M0 5 L-5 20" stroke="#795548" stroke-width="1.5" fill="none"/>
    <!-- Earthworm -->
    <path d="M-30 15 Q-25 10 -20 15 Q-15 20 -10 15 Q-5 10 0 15" stroke="#FFAB91" stroke-width="3" fill="none" stroke-linecap="round"/>
    <!-- Mole -->
    <ellipse cx="30" cy="10" rx="10" ry="7" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
    <circle cx="25" cy="7" r="2" fill="#333"/>
    <path d="M22 10 L18 10" stroke="#5D4037" stroke-width="1"/>
    <!-- Soil layers -->
    <line x1="-50" y1="10" x2="50" y2="10" stroke="#6D4C41" stroke-width="0.5" stroke-dasharray="3,3" opacity="0.5"/>
    <line x1="-45" y1="30" x2="45" y2="30" stroke="#5D4037" stroke-width="0.5" stroke-dasharray="3,3" opacity="0.5"/>
    <!-- Stones -->
    <ellipse cx="-35" cy="25" rx="6" ry="4" fill="#9E9E9E" stroke="#757575" stroke-width="0.5"/>
    <ellipse cx="40" cy="35" rx="5" ry="3" fill="#BDBDBD" stroke="#9E9E9E" stroke-width="0.5"/>
    <text x="0" y="70" font-family="Arial,sans-serif" font-size="9" fill="#5D4037" text-anchor="middle" font-weight="bold">Почвенная</text>
    <text x="0" y="82" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Бактерии, черви, кроты</text>
  </g>
  <!-- Организменная (Inside organisms) -->
  <g transform="translate(450,130)">
    <!-- Host organism outline -->
    <ellipse cx="0" cy="0" rx="35" ry="40" fill="#FFCDD2" stroke="#E53935" stroke-width="1.5" opacity="0.5"/>
    <!-- Parasites inside -->
    <circle cx="-10" cy="-10" r="8" fill="#FF8A65" stroke="#E64A19" stroke-width="1"/>
    <circle cx="10" cy="5" r="6" fill="#FFAB91" stroke="#E64A19" stroke-width="1"/>
    <!-- Tapeworm fragment -->
    <rect x="-5" y="15" width="30" height="8" fill="#FFF9C4" stroke="#F9A825" stroke-width="1" rx="3"/>
    <!-- Bacteria -->
    <ellipse cx="5" cy="-20" rx="5" ry="3" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
    <text x="0" y="58" font-family="Arial,sans-serif" font-size="9" fill="#C62828" text-anchor="middle" font-weight="bold">Организменная</text>
    <text x="0" y="70" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Паразиты, симбионты</text>
  </g>
  <!-- Bottom summary -->
  <rect x="40" y="250" width="420" height="55" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="268" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">4 среды жизни на Земле</text>
  <text x="250" y="283" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Каждая среда имеет свои условия: свет, температура, влажность, кислород</text>
  <text x="250" y="297" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Организмы приспособлены к жизни в определённой среде</text>
'''

# ===== LESSON 22: Природные сообщества =====
lesson22_illustration = '''
  <!-- Ecosystem with food chains -->
  <!-- Sky area -->
  <rect x="30" y="55" width="440" height="60" fill="#E1F5FE" rx="5" opacity="0.5"/>
  <!-- Sun -->
  <circle cx="440" cy="80" r="20" fill="#FFF176" stroke="#FDD835" stroke-width="1.5"/>
  <line x1="440" y1="55" x2="440" y2="50" stroke="#FDD835" stroke-width="1.5"/>
  <line x1="460" y1="65" x2="465" y2="60" stroke="#FDD835" stroke-width="1.5"/>
  <line x1="465" y1="80" x2="470" y2="80" stroke="#FDD835" stroke-width="1.5"/>
  <line x1="460" y1="95" x2="465" y2="100" stroke="#FDD835" stroke-width="1.5"/>
  <!-- Birds -->
  <path d="M80 75 Q85 68 90 75 Q95 68 100 75" stroke="#333" stroke-width="1.5" fill="none"/>
  <path d="M120 85 Q124 80 128 85 Q132 80 136 85" stroke="#333" stroke-width="1.2" fill="none"/>
  <!-- Ground area -->
  <rect x="30" y="115" width="440" height="120" fill="#C8E6C9" rx="0" opacity="0.4"/>
  <!-- Producers - Plants -->
  <!-- Large tree -->
  <rect x="95" y="130" width="10" height="60" fill="#795548" rx="2"/>
  <circle cx="100" cy="115" r="25" fill="#4CAF50" opacity="0.8"/>
  <circle cx="85" cy="120" r="18" fill="#66BB6A" opacity="0.6"/>
  <circle cx="115" cy="118" r="15" fill="#81C784" opacity="0.6"/>
  <text x="100" y="205" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Дуб</text>
  <!-- Grass -->
  <path d="M40 190 Q42 175 45 185" stroke="#4CAF50" stroke-width="1.5" fill="none"/>
  <path d="M50 190 Q48 170 55 185" stroke="#66BB6A" stroke-width="1.5" fill="none"/>
  <path d="M60 190 Q62 172 58 185" stroke="#4CAF50" stroke-width="1.5" fill="none"/>
  <text x="50" y="205" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Трава</text>
  <!-- Consumers - Animals -->
  <!-- Caterpillar on tree -->
  <path d="M80 135 Q85 130 90 135 Q95 140 100 135 Q105 130 110 135" stroke="#8BC34A" stroke-width="4" fill="none" stroke-linecap="round"/>
  <circle cx="80" cy="135" r="3" fill="#689F38"/>
  <text x="95" y="150" font-family="Arial,sans-serif" font-size="6" fill="#333">Гусеница</text>
  <!-- Mouse -->
  <g transform="translate(170,185)">
    <ellipse cx="0" cy="0" rx="12" ry="8" fill="#BCAAA4" stroke="#8D6E63" stroke-width="1"/>
    <ellipse cx="-10" cy="-3" rx="5" ry="4" fill="#BCAAA4" stroke="#8D6E63" stroke-width="1"/>
    <circle cx="-12" cy="-4" r="1.5" fill="#333"/>
    <ellipse cx="-8" cy="-10" rx="3" ry="6" fill="#D7CCC8" stroke="#8D6E63" stroke-width="0.5"/>
    <ellipse cx="-5" cy="-10" rx="3" ry="6" fill="#D7CCC8" stroke="#8D6E63" stroke-width="0.5"/>
    <path d="M12 0 Q18 -3 22 0" stroke="#8D6E63" stroke-width="1" fill="none"/>
    <text x="0" y="18" font-family="Arial,sans-serif" font-size="7" fill="#5D4037" text-anchor="middle">Мышь</text>
  </g>
  <!-- Fox -->
  <g transform="translate(320,175)">
    <ellipse cx="0" cy="0" rx="22" ry="12" fill="#FF8A65" stroke="#E64A19" stroke-width="1.5"/>
    <ellipse cx="-20" cy="-3" rx="10" ry="8" fill="#FF8A65" stroke="#E64A19" stroke-width="1"/>
    <!-- Ears -->
    <path d="M-22 -10 L-26 -22 L-18 -12 Z" fill="#FFAB91" stroke="#E64A19" stroke-width="0.8"/>
    <path d="M-14 -10 L-12 -22 L-8 -12 Z" fill="#FFAB91" stroke="#E64A19" stroke-width="0.8"/>
    <circle cx="-23" cy="-3" r="2" fill="#333"/>
    <path d="M-28 -1 L-32 0" stroke="#333" stroke-width="0.8"/>
    <path d="M28 0 Q35 -5 38 0" stroke="#E64A19" stroke-width="3" fill="none" stroke-linecap="round"/>
    <!-- Legs -->
    <line x1="-8" y1="12" x2="-10" y2="22" stroke="#E64A19" stroke-width="2"/>
    <line x1="8" y1="12" x2="10" y2="22" stroke="#E64A19" stroke-width="2"/>
    <text x="0" y="35" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle">Лиса</text>
  </g>
  <!-- Decomposers -->
  <!-- Mushroom -->
  <g transform="translate(440,185)">
    <path d="M-10 0 Q-12 -12 0 -15 Q12 -12 10 0 Z" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
    <rect x="-3" y="0" width="6" height="12" fill="#D7CCC8" stroke="#BCAAA4" stroke-width="0.8" rx="2"/>
    <text x="0" y="25" font-family="Arial,sans-serif" font-size="7" fill="#5D4037" text-anchor="middle">Гриб</text>
  </g>
  <!-- Food chain arrows -->
  <path d="M55 185 Q80 170 170 178" stroke="#E64A19" stroke-width="1.5" fill="none" marker-end="url(#arr)"/>
  <path d="M185 172 Q240 150 310 170" stroke="#E64A19" stroke-width="1.5" fill="none" marker-end="url(#arr)"/>
  <defs><marker id="arr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#E64A19"/></marker></defs>
  <!-- Food chain labels -->
  <rect x="30" y="240" width="440" height="65" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="257" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Пищевая цепь</text>
  <text x="250" y="272" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Растения (продуценты) -> Травоядные (консументы I) -> Хищники (консументы II)</text>
  <text x="250" y="287" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">-> Грибы и бактерии (редуценты) -> Возврат веществ в почву</text>
  <text x="250" y="300" font-family="Arial,sans-serif" font-size="7" fill="#999" text-anchor="middle">Природное сообщество = живые организмы + неживая природа</text>
'''

# ===== LESSON 23: Охрана природы =====
lesson23_illustration = '''
  <!-- Protected nature scene -->
  <!-- Sky -->
  <rect x="30" y="55" width="440" height="100" fill="#E1F5FE" rx="5" opacity="0.4"/>
  <!-- Clean forest scene (left) -->
  <!-- Tree 1 -->
  <rect x="80" y="130" width="8" height="50" fill="#795548" rx="2"/>
  <circle cx="84" cy="115" r="22" fill="#4CAF50" opacity="0.8"/>
  <!-- Tree 2 -->
  <rect x="140" y="135" width="7" height="45" fill="#795548" rx="2"/>
  <circle cx="143" cy="120" r="18" fill="#66BB6A" opacity="0.8"/>
  <!-- Tree 3 -->
  <rect x="190" y="128" width="8" height="52" fill="#795548" rx="2"/>
  <circle cx="194" cy="112" r="20" fill="#81C784" opacity="0.8"/>
  <!-- Deer -->
  <g transform="translate(110,190)">
    <ellipse cx="0" cy="0" rx="18" ry="10" fill="#BCAAA4" stroke="#8D6E63" stroke-width="1.2"/>
    <ellipse cx="-16" cy="-5" rx="8" ry="6" fill="#BCAAA4" stroke="#8D6E63" stroke-width="1"/>
    <!-- Antlers -->
    <path d="M-18 -11 L-22 -25 L-26 -20" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <path d="M-14 -11 L-10 -22 L-6 -18" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <circle cx="-19" cy="-5" r="1.5" fill="#333"/>
    <!-- Legs -->
    <line x1="-8" y1="10" x2="-10" y2="22" stroke="#8D6E63" stroke-width="1.5"/>
    <line x1="8" y1="10" x2="10" y2="22" stroke="#8D6E63" stroke-width="1.5"/>
    <line x1="-12" y1="10" x2="-14" y2="20" stroke="#8D6E63" stroke-width="1.5"/>
    <line x1="12" y1="10" x2="14" y2="20" stroke="#8D6E63" stroke-width="1.5"/>
  </g>
  <!-- River -->
  <path d="M30 230 Q100 225 200 232 Q300 240 400 230 Q450 228 470 232" fill="#64B5F6" opacity="0.4"/>
  <path d="M30 238 Q100 233 200 240 Q300 248 400 238 Q450 236 470 240" fill="#90CAF9" opacity="0.3"/>
  <!-- Flowers -->
  <circle cx="55" cy="210" r="4" fill="#E53935" opacity="0.7"/>
  <circle cx="65" cy="215" r="3" fill="#FF9800" opacity="0.7"/>
  <line x1="55" y1="214" x2="55" y2="225" stroke="#4CAF50" stroke-width="1"/>
  <line x1="65" y1="218" x2="65" y2="228" stroke="#4CAF50" stroke-width="1"/>
  <!-- Butterfly -->
  <g transform="translate(250,100)">
    <ellipse cx="-8" cy="-5" rx="8" ry="5" fill="#FFAB91" opacity="0.7" transform="rotate(-20,-8,-5)"/>
    <ellipse cx="8" cy="-5" rx="8" ry="5" fill="#FFAB91" opacity="0.7" transform="rotate(20,8,-5)"/>
    <ellipse cx="-5" cy="3" rx="5" ry="3" fill="#FF8A65" opacity="0.6" transform="rotate(-10,-5,3)"/>
    <ellipse cx="5" cy="3" rx="5" ry="3" fill="#FF8A65" opacity="0.6" transform="rotate(10,5,3)"/>
    <line x1="-1" y1="-8" x2="-3" y2="-15" stroke="#333" stroke-width="0.8"/>
    <line x1="1" y1="-8" x2="3" y2="-15" stroke="#333" stroke-width="0.8"/>
    <ellipse cx="0" cy="0" rx="2" ry="6" fill="#333"/>
  </g>
  <!-- Protection sign -->
  <g transform="translate(400,120)">
    <!-- Shield shape -->
    <path d="M0 -30 L25 -20 L25 5 Q25 25 0 35 Q-25 25 -25 5 L-25 -20 Z" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2.5"/>
    <!-- Tree inside shield -->
    <rect x="-3" y="-5" width="6" height="20" fill="#795548" rx="1"/>
    <circle cx="0" cy="-12" r="10" fill="#4CAF50" opacity="0.8"/>
    <!-- Hand protecting -->
    <path d="M-15 8 Q-10 15 0 12 Q10 15 15 8" stroke="#2E7D32" stroke-width="2" fill="none"/>
  </g>
  <!-- Red Book -->
  <g transform="translate(400,210)">
    <rect x="-22" y="-18" width="44" height="36" fill="#E53935" stroke="#B71C1C" stroke-width="2" rx="3"/>
    <text x="0" y="-5" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">Красная</text>
    <text x="0" y="7" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">книга</text>
  </g>
  <!-- Threats (bottom left) -->
  <g transform="translate(60,275)">
    <rect x="-30" y="-12" width="60" height="24" fill="#FFCDD2" stroke="#E53935" stroke-width="1" rx="3"/>
    <text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">Вырубка</text>
  </g>
  <g transform="translate(145,275)">
    <rect x="-30" y="-12" width="60" height="24" fill="#FFCDD2" stroke="#E53935" stroke-width="1" rx="3"/>
    <text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">Загрязнение</text>
  </g>
  <g transform="translate(230,275)">
    <rect x="-30" y="-12" width="60" height="24" fill="#FFCDD2" stroke="#E53935" stroke-width="1" rx="3"/>
    <text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">Браконьерство</text>
  </g>
  <!-- Protection actions (bottom right) -->
  <g transform="translate(330,275)">
    <rect x="-40" y="-12" width="80" height="24" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1" rx="3"/>
    <text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Заповедники</text>
  </g>
  <g transform="translate(435,275)">
    <rect x="-40" y="-12" width="80" height="24" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1" rx="3"/>
    <text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Охрана видов</text>
  </g>
'''

# Generate all SVGs
lessons = [
    (21, "Среды жизни организмов", lesson21_illustration),
    (22, "Природные сообщества", lesson22_illustration),
    (23, "Охрана природы", lesson23_illustration),
]

for num, title, illustration in lessons:
    subtitle = f"Биология 5 класс - Урок {num}"
    svg_content = svg_wrap(illustration, title, subtitle)
    filepath = os.path.join(OUTPUT_DIR, f"lesson{num}.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Generated: {filepath}")

print("\nDone! 3 SVGs generated for Grade 5 Biology Lessons 21-23.")
