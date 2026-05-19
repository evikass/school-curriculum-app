#!/usr/bin/env python3
"""Generate detailed biology SVG illustrations for Grade 6, Lessons 9-16"""
import os

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade6/biology"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def W(inner, title, subtitle, color="#2E7D32"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#E8F5E9"/><stop offset="100%" stop-color="#C8E6C9"/></linearGradient></defs>
  <rect width="500" height="350" fill="url(#bg)" rx="10"/>
  <rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="{color}" stroke-width="2.5"/>
  <text x="250" y="30" font-family="Arial,sans-serif" font-size="16" font-weight="bold" fill="{color}" text-anchor="middle">{title}</text>
  <text x="250" y="46" font-family="Arial,sans-serif" font-size="10" fill="#888" text-anchor="middle">{subtitle}</text>
  <line x1="30" y1="52" x2="470" y2="52" stroke="{color}" stroke-width="1.5" opacity="0.25"/>
  {inner}
  <rect x="10" y="325" width="480" height="20" rx="4" fill="{color}" opacity="0.85"/>
  <text x="250" y="339" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="white" font-weight="bold">Биология 6 класс</text>
</svg>'''

# ===== LESSON 9: Разнообразие грибов =====
l9 = '''
  <!-- 4 types of fungi -->
  <g transform="translate(70,120)">
    <!-- Chanterelle -->
    <path d="M-18 0 Q-22 -15 -10 -22 Q0 -25 10 -22 Q22 -15 18 0 Z" fill="#FFB300" stroke="#E65100" stroke-width="1.5"/>
    <rect x="-4" y="0" width="8" height="25" fill="#FFCC80" stroke="#E65100" stroke-width="1" rx="3"/>
    <text x="0" y="40" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Лисичка</text>
  </g>
  <g transform="translate(180,115)">
    <!-- Amanita -->
    <path d="M-25 0 Q-30 -25 -15 -35 Q0 -40 15 -35 Q30 -25 25 0 Z" fill="#E53935" stroke="#C62828" stroke-width="1.5"/>
    <circle cx="-10" cy="-18" r="4" fill="white" opacity="0.7"/>
    <circle cx="8" cy="-22" r="3.5" fill="white" opacity="0.6"/>
    <circle cx="-2" cy="-8" r="3" fill="white" opacity="0.5"/>
    <rect x="-5" y="0" width="10" height="30" fill="#FFF3E0" stroke="#D7CCC8" stroke-width="1" rx="3"/>
    <ellipse cx="0" cy="10" rx="10" ry="3" fill="#FFECB3" stroke="#D7CCC8" stroke-width="0.8"/>
    <text x="35" y="-25" font-family="Arial,sans-serif" font-size="11" fill="#C62828" font-weight="bold">!</text>
    <text x="0" y="48" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">Мухомор</text>
  </g>
  <g transform="translate(310,120)">
    <!-- Yeast budding -->
    <ellipse cx="-8" cy="0" rx="10" ry="8" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/>
    <ellipse cx="8" cy="-10" rx="7" ry="6" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.2"/>
    <path d="M-2 -5 Q2 -10 4 -8" stroke="#F9A825" stroke-width="1" fill="none"/>
    <circle cx="-8" cy="0" r="3" fill="#FDD835"/>
    <circle cx="8" cy="-10" r="2" fill="#FDD835"/>
    <text x="0" y="25" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Дрожжи</text>
  </g>
  <g transform="translate(420,120)">
    <!-- Mold -->
    <rect x="-18" y="5" width="36" height="18" fill="#D7CCC8" stroke="#BCAAA4" stroke-width="1" rx="3"/>
    <line x1="-6" y1="5" x2="-8" y2="-15" stroke="#8BC34A" stroke-width="1.5"/>
    <line x1="0" y1="5" x2="2" y2="-18" stroke="#8BC34A" stroke-width="1.5"/>
    <line x1="8" y1="5" x2="12" y2="-12" stroke="#8BC34A" stroke-width="1.5"/>
    <circle cx="-8" cy="-17" r="5" fill="#689F38" opacity="0.7"/>
    <circle cx="2" cy="-20" r="6" fill="#7CB342" opacity="0.7"/>
    <circle cx="12" cy="-14" r="4" fill="#689F38" opacity="0.7"/>
    <text x="0" y="38" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Плесень</text>
  </g>
  <!-- Bracket fungus on tree -->
  <g transform="translate(70,230)">
    <rect x="-5" y="-20" width="20" height="40" fill="#795548" rx="3"/>
    <path d="M15 -10 Q22 -20 35 -15 Q30 -8 15 -5 Z" fill="#FF8F00" stroke="#E65100" stroke-width="1"/>
    <path d="M15 0 Q20 -8 32 -5 Q28 2 15 3 Z" fill="#FFA000" stroke="#E65100" stroke-width="1"/>
    <text x="15" y="35" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Трутовик</text>
  </g>
  <!-- Morel -->
  <g transform="translate(200,225)">
    <path d="M-12 0 Q-15 -15 -10 -25 Q-5 -30 0 -28 Q5 -30 10 -25 Q15 -15 12 0 Z" fill="#8D6E63" stroke="#5D4037" stroke-width="1.5"/>
    <!-- Pits -->
    <ellipse cx="-5" cy="-18" rx="3" ry="2" fill="#5D4037" opacity="0.3"/>
    <ellipse cx="5" cy="-12" rx="3" ry="2" fill="#5D4037" opacity="0.3"/>
    <ellipse cx="0" cy="-6" rx="3" ry="2" fill="#5D4037" opacity="0.3"/>
    <rect x="-4" y="0" width="8" height="20" fill="#D7CCC8" stroke="#BCAAA4" stroke-width="1" rx="3"/>
    <text x="0" y="35" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Сморчок</text>
  </g>
  <!-- Summary -->
  <rect x="300" y="220" width="175" height="85" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="387" y="237" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Группы грибов</text>
  <text x="310" y="253" font-family="Arial,sans-serif" font-size="7" fill="#555">- Шляпочные (съедобные/ядовитые)</text>
  <text x="310" y="265" font-family="Arial,sans-serif" font-size="7" fill="#555">- Плесневые (пеницилл, мукор)</text>
  <text x="310" y="277" font-family="Arial,sans-serif" font-size="7" fill="#555">- Дрожжи (одноклеточные)</text>
  <text x="310" y="289" font-family="Arial,sans-serif" font-size="7" fill="#555">- Трутовики (паразиты деревьев)</text>
  <text x="310" y="301" font-family="Arial,sans-serif" font-size="7" fill="#C62828">Правило: не ешь незнакомые грибы!</text>
'''

# ===== LESSON 10: Лишайники — симбиоз гриба и водоросли =====
l10 = '''
  <!-- Three lichen types + symbiosis diagram -->
  <g transform="translate(80,110)">
    <ellipse cx="0" cy="15" rx="35" ry="15" fill="#9E9E9E" stroke="#757575" stroke-width="1"/>
    <ellipse cx="-5" cy="5" rx="20" ry="8" fill="#8BC34A" opacity="0.7" stroke="#689F38" stroke-width="1"/>
    <ellipse cx="8" cy="0" rx="12" ry="6" fill="#9CCC65" opacity="0.5"/>
    <text x="0" y="42" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Накипные</text>
  </g>
  <g transform="translate(210,110)">
    <rect x="-25" y="10" width="50" height="25" fill="#795548" stroke="#5D4037" stroke-width="1" rx="3"/>
    <path d="M-18 8 Q-12 -5 0 -8 Q12 -5 18 8 Q8 5 0 6 Q-8 5 -18 8 Z" fill="#81C784" stroke="#4CAF50" stroke-width="1.5"/>
    <text x="0" y="52" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Листоватые</text>
  </g>
  <g transform="translate(350,100)">
    <path d="M0 40 L0 15 L-12 -5 L-18 -15" stroke="#7CB342" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M0 15 L12 -5 L18 -15" stroke="#7CB342" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M0 25 L-15 10 L-20 0" stroke="#8BC34A" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <path d="M0 25 L15 10 L20 0" stroke="#8BC34A" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <path d="M-12 -5 L-20 -10" stroke="#9CCC65" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <path d="M12 -5 L20 -10" stroke="#9CCC65" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <text x="0" y="58" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Кустистые</text>
    <text x="0" y="70" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(ягель - олений мох)</text>
  </g>
  <!-- Symbiosis Venn diagram -->
  <g transform="translate(150,230)">
    <circle cx="-40" cy="0" r="35" fill="#FFCC80" stroke="#E65100" stroke-width="2" opacity="0.5"/>
    <circle cx="40" cy="0" r="35" fill="#A5D6A7" stroke="#2E7D32" stroke-width="2" opacity="0.5"/>
    <text x="-40" y="-8" font-family="Arial,sans-serif" font-size="9" fill="#BF360C" text-anchor="middle" font-weight="bold">Гриб</text>
    <text x="-40" y="6" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle">вода, минер.</text>
    <text x="40" y="-8" font-family="Arial,sans-serif" font-size="9" fill="#1B5E20" text-anchor="middle" font-weight="bold">Водоросль</text>
    <text x="40" y="6" font-family="Arial,sans-serif" font-size="7" fill="#1B5E20" text-anchor="middle">орг. вещества</text>
    <text x="0" y="3" font-family="Arial,sans-serif" font-size="8" fill="#33691E" text-anchor="middle" font-weight="bold">Лишайник</text>
  </g>
  <!-- Info -->
  <rect x="280" y="210" width="190" height="90" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="375" y="227" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Особенности лишайников</text>
  <text x="290" y="243" font-family="Arial,sans-serif" font-size="7" fill="#555">- Симбиоз гриба и водоросли</text>
  <text x="290" y="255" font-family="Arial,sans-serif" font-size="7" fill="#555">- Растут очень медленно</text>
  <text x="290" y="267" font-family="Arial,sans-serif" font-size="7" fill="#555">- Впервые поселяются на скалах</text>
  <text x="290" y="279" font-family="Arial,sans-serif" font-size="7" fill="#555">- Индикаторы чистого воздуха</text>
  <text x="290" y="293" font-family="Arial,sans-serif" font-size="7" fill="#C62828">- Погибают от загрязнения!</text>
'''

# ===== LESSON 11: Общая характеристика царства Растения =====
l11 = '''
  <!-- Plant kingdom overview -->
  <g transform="translate(250,185)">
    <!-- Central title -->
    <circle cx="0" cy="0" r="35" fill="#2E7D32" opacity="0.8"/>
    <text x="0" y="-3" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">Растения</text>
    <text x="0" y="10" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">(автотрофы)</text>
    <!-- Branches -->
    <line x1="-30" y1="-25" x2="-100" y2="-70" stroke="#795548" stroke-width="2"/>
    <line x1="30" y1="-25" x2="100" y2="-70" stroke="#795548" stroke-width="2"/>
    <line x1="-35" y1="0" x2="-120" y2="0" stroke="#795548" stroke-width="2"/>
    <line x1="35" y1="0" x2="120" y2="0" stroke="#795548" stroke-width="2"/>
    <line x1="-25" y1="25" x2="-90" y2="70" stroke="#795548" stroke-width="2"/>
    <line x1="25" y1="25" x2="90" y2="70" stroke="#795548" stroke-width="2"/>
    <!-- Водоросли -->
    <ellipse cx="-115" cy="-75" rx="40" ry="16" fill="#4CAF50" opacity="0.6"/>
    <text x="-115" y="-72" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">Водоросли</text>
    <!-- Мхи -->
    <ellipse cx="115" cy="-75" rx="35" ry="16" fill="#66BB6A" opacity="0.6"/>
    <text x="115" y="-72" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">Мхи</text>
    <!-- Папоротники -->
    <ellipse cx="-135" cy="0" rx="45" ry="16" fill="#43A047" opacity="0.6"/>
    <text x="-135" y="3" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle" font-weight="bold">Папоротники</text>
    <!-- Голосеменные -->
    <ellipse cx="135" cy="0" rx="45" ry="16" fill="#2E7D32" opacity="0.6"/>
    <text x="135" y="3" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle" font-weight="bold">Голосеменные</text>
    <!-- Покрытосеменные -->
    <ellipse cx="-105" cy="75" rx="50" ry="16" fill="#1B5E20" opacity="0.6"/>
    <text x="-105" y="72" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle" font-weight="bold">Покрытосеменные</text>
    <text x="-105" y="83" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle">(цветковые)</text>
    <!-- Evolution arrow -->
    <text x="105" y="68" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">Цветковые</text>
    <text x="105" y="78" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">самые</text>
    <text x="105" y="88" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">сложные</text>
  </g>
  <!-- Characteristics -->
  <rect x="20" y="280" width="460" height="35" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="296" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Признаки растений: автотрофы (фотосинтез), клеточная стенка из целлюлозы, неподвижны</text>
  <text x="250" y="310" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Растут всю жизнь, запасное вещество - крахмал</text>
'''

# ===== LESSON 12: Водоросли — древнейшие растения =====
l12 = '''
  <!-- Three algae types -->
  <g transform="translate(85,140)">
    <rect x="-50" y="-45" width="100" height="100" fill="#E0F7FA" stroke="#80DEEA" stroke-width="1" rx="5" opacity="0.5"/>
    <!-- Chlamydomonas -->
    <circle cx="0" cy="0" r="18" fill="#81C784" stroke="#4CAF50" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="6" fill="#C8E6C9" opacity="0.5"/>
    <!-- Cup-shaped chloroplast -->
    <path d="M-10 5 Q-12 -8 0 -10 Q12 -8 10 5 Q5 8 0 8 Q-5 8 -10 5 Z" fill="#388E3C" opacity="0.4"/>
    <!-- Flagella -->
    <path d="M5 -15 Q8 -25 5 -35" stroke="#4CAF50" stroke-width="1.5" fill="none"/>
    <path d="M-5 -15 Q-8 -25 -5 -35" stroke="#4CAF50" stroke-width="1.5" fill="none"/>
    <!-- Eye spot -->
    <circle cx="-5" cy="-8" r="2.5" fill="#E53935"/>
    <text x="0" y="30" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Хламидомонада</text>
    <text x="0" y="42" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(одноклеточная)</text>
  </g>
  <g transform="translate(250,135)">
    <rect x="-55" y="-45" width="110" height="105" fill="#FFF3E0" stroke="#FFE0B2" stroke-width="1" rx="5" opacity="0.5"/>
    <!-- Kelp/Laminaria -->
    <path d="M0 40 L0 -10" stroke="#795548" stroke-width="4"/>
    <path d="M-5 -10 Q-25 -20 -30 -5 Q-25 5 -5 0" fill="#A1887F" stroke="#795548" stroke-width="1"/>
    <path d="M5 -10 Q25 -20 30 -5 Q25 5 5 0" fill="#A1887F" stroke="#795548" stroke-width="1"/>
    <path d="M-3 -10 Q-15 -30 -10 -38 Q0 -30 3 -10" fill="#BCAAA4" stroke="#795548" stroke-width="0.8"/>
    <path d="M3 -10 Q15 -30 10 -38 Q0 -30 -3 -10" fill="#BCAAA4" stroke="#795548" stroke-width="0.8"/>
    <circle cx="-15" cy="-15" r="3.5" fill="#D7CCC8" stroke="#8D6E63" stroke-width="0.8"/>
    <text x="0" y="55" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Ламинария</text>
    <text x="0" y="67" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(многоклеточная бурая)</text>
  </g>
  <g transform="translate(415,140)">
    <rect x="-45" y="-45" width="90" height="100" fill="#FCE4EC" stroke="#F8BBD0" stroke-width="1" rx="5" opacity="0.5"/>
    <!-- Red algae - branching -->
    <path d="M0 40 L0 10 L-15 -10 L-22 -20" stroke="#E91E63" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <path d="M0 10 L15 -10 L22 -20" stroke="#E91E63" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <path d="M0 25 L-18 10 L-25 0" stroke="#EC407A" stroke-width="2" fill="none" stroke-linecap="round"/>
    <path d="M0 25 L18 10 L25 0" stroke="#EC407A" stroke-width="2" fill="none" stroke-linecap="round"/>
    <path d="M-15 -10 L-22 -15" stroke="#F06292" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <path d="M15 -10 L22 -15" stroke="#F06292" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <text x="0" y="55" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Порфира</text>
    <text x="0" y="67" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(красная водоросль)</text>
  </g>
  <!-- Info -->
  <rect x="40" y="260" width="420" height="45" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="277" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Особенности водорослей</text>
  <text x="250" y="292" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Нет корней, стеблей, листьев - тело: слоевище (таллом)</text>
  <text x="250" y="304" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Обитают в воде, выделяют 50-80% кислорода на планете</text>
'''

# ===== LESSON 13: Мхи: строение и разнообразие =====
l13 = '''
  <!-- Two moss types: Sphagnum and Kukushkin flax -->
  <!-- Kukushkin flax -->
  <g transform="translate(120,170)">
    <!-- Ground -->
    <ellipse cx="0" cy="80" rx="45" ry="6" fill="#8D6E63" opacity="0.3"/>
    <!-- Stem -->
    <rect x="-3" y="-10" width="6" height="90" fill="#66BB6A" rx="2"/>
    <!-- Leaves -->
    <ellipse cx="-12" cy="10" rx="8" ry="3" fill="#4CAF50" opacity="0.7" transform="rotate(25,-12,10)"/>
    <ellipse cx="12" cy="10" rx="8" ry="3" fill="#4CAF50" opacity="0.7" transform="rotate(-25,12,10)"/>
    <ellipse cx="-14" cy="25" rx="8" ry="3" fill="#66BB6A" opacity="0.6" transform="rotate(20,-14,25)"/>
    <ellipse cx="14" cy="25" rx="8" ry="3" fill="#66BB6A" opacity="0.6" transform="rotate(-20,14,25)"/>
    <ellipse cx="-12" cy="40" rx="7" ry="3" fill="#81C784" opacity="0.6" transform="rotate(22,-12,40)"/>
    <ellipse cx="12" cy="40" rx="7" ry="3" fill="#81C784" opacity="0.6" transform="rotate(-22,12,40)"/>
    <!-- Capsule on stalk -->
    <line x1="0" y1="-10" x2="0" y2="-40" stroke="#8D6E63" stroke-width="1.5"/>
    <ellipse cx="0" cy="-45" rx="7" ry="12" fill="#A5D6A7" stroke="#4CAF50" stroke-width="1.5"/>
    <ellipse cx="0" cy="-55" rx="5" ry="2" fill="#81C784"/>
    <!-- Rhizoids -->
    <path d="M0 80 Q-5 90 -8 95" stroke="#BCAAA4" stroke-width="1" fill="none"/>
    <path d="M0 80 Q5 90 8 95" stroke="#BCAAA4" stroke-width="1" fill="none"/>
    <path d="M0 80 Q0 92 0 98" stroke="#BCAAA4" stroke-width="0.8" fill="none"/>
    <text x="0" y="108" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Кукушкин лён</text>
    <text x="0" y="120" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(зелёный мох)</text>
  </g>
  <!-- Sphagnum -->
  <g transform="translate(350,170)">
    <ellipse cx="0" cy="80" rx="50" ry="6" fill="#E0F2F1" opacity="0.5"/>
    <!-- Multiple stems -->
    <rect x="-15" y="10" width="4" height="70" fill="#B2DFDB" rx="1.5"/>
    <rect x="-3" y="5" width="4" height="75" fill="#80CBC4" rx="1.5"/>
    <rect x="9" y="10" width="4" height="70" fill="#B2DFDB" rx="1.5"/>
    <!-- Heads (capitulum) -->
    <circle cx="-13" cy="5" r="8" fill="#E0F2F1" stroke="#80CBC4" stroke-width="1"/>
    <circle cx="-1" cy="0" r="10" fill="#B2DFDB" stroke="#80CBC4" stroke-width="1"/>
    <circle cx="11" cy="5" r="8" fill="#E0F2F1" stroke="#80CBC4" stroke-width="1"/>
    <!-- Small branch leaves -->
    <ellipse cx="-20" cy="25" rx="5" ry="2" fill="#80CBC4" opacity="0.6"/>
    <ellipse cx="18" cy="25" rx="5" ry="2" fill="#80CBC4" opacity="0.6"/>
    <ellipse cx="-22" cy="40" rx="5" ry="2" fill="#B2DFDB" opacity="0.5"/>
    <ellipse cx="20" cy="40" rx="5" ry="2" fill="#B2DFDB" opacity="0.5"/>
    <!-- Water-holding capacity indicator -->
    <circle cx="-1" cy="0" r="6" fill="#E0F7FA" opacity="0.4"/>
    <text x="0" y="108" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Сфагнум</text>
    <text x="0" y="120" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(торфяной мох)</text>
  </g>
  <!-- Comparison -->
  <rect x="40" y="255" width="420" height="55" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="272" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Особенности мхов</text>
  <text x="250" y="287" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Нет корней (ризоиды), нет цветков и семян, размножаются спорами</text>
  <text x="250" y="301" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Сфагнум впитывает воду 25x своего веса! Образует торф</text>
'''

# ===== LESSON 14: Значение мхов в природе и хозяйстве =====
l14 = '''
  <!-- Bog ecosystem + uses -->
  <!-- Bog cross-section -->
  <g transform="translate(170,185)">
    <!-- Sky -->
    <rect x="-120" y="-110" width="240" height="60" fill="#E1F5FE" rx="5" opacity="0.4"/>
    <!-- Sphagnum layer -->
    <rect x="-120" y="-50" width="240" height="25" fill="#B2DFDB" stroke="#80CBC4" stroke-width="1"/>
    <text x="0" y="-33" font-family="Arial,sans-serif" font-size="7" fill="#00695C" text-anchor="middle">Живой сфагнум</text>
    <!-- Peat layers -->
    <rect x="-120" y="-25" width="240" height="20" fill="#8D6E63" opacity="0.5"/>
    <text x="0" y="-11" font-family="Arial,sans-serif" font-size="6" fill="#4E342E" text-anchor="middle">Бурый торф</text>
    <rect x="-120" y="-5" width="240" height="20" fill="#5D4037" opacity="0.6"/>
    <text x="0" y="9" font-family="Arial,sans-serif" font-size="6" fill="#FFF" text-anchor="middle">Тёмный торф</text>
    <!-- Clay -->
    <rect x="-120" y="15" width="240" height="15" fill="#FFE0B2" stroke="#FFCC80" stroke-width="1"/>
    <text x="0" y="26" font-family="Arial,sans-serif" font-size="6" fill="#795548" text-anchor="middle">Глина</text>
    <!-- Moss plants on top -->
    <g transform="translate(-60,-55)">
      <rect x="-1" y="-10" width="2" height="12" fill="#80CBC4"/>
      <circle cx="0" cy="-12" r="4" fill="#B2DFDB"/>
    </g>
    <g transform="translate(-30,-55)">
      <rect x="-1" y="-12" width="2" height="14" fill="#80CBC4"/>
      <circle cx="0" cy="-14" r="5" fill="#B2DFDB"/>
    </g>
    <g transform="translate(0,-55)">
      <rect x="-1" y="-10" width="2" height="12" fill="#80CBC4"/>
      <circle cx="0" cy="-12" r="4" fill="#B2DFDB"/>
    </g>
    <g transform="translate(30,-55)">
      <rect x="-1" y="-12" width="2" height="14" fill="#80CBC4"/>
      <circle cx="0" cy="-14" r="5" fill="#B2DFDB"/>
    </g>
    <g transform="translate(60,-55)">
      <rect x="-1" y="-10" width="2" height="12" fill="#80CBC4"/>
      <circle cx="0" cy="-12" r="4" fill="#B2DFDB"/>
    </g>
    <!-- Water -->
    <path d="M-120 -50 Q-100 -55 -80 -50 Q-60 -45 -40 -50 Q-20 -55 0 -50 Q20 -45 40 -50 Q60 -55 80 -50 Q100 -45 120 -50" stroke="#42A5F5" stroke-width="1" fill="none"/>
    <!-- Cranberries -->
    <circle cx="-50" cy="-60" r="3" fill="#E53935"/>
    <circle cx="-45" cy="-58" r="2.5" fill="#C62828"/>
    <!-- Small tree -->
    <rect x="85" y="-65" width="4" height="15" fill="#795548"/>
    <circle cx="87" cy="-72" r="8" fill="#4CAF50" opacity="0.6"/>
  </g>
  <!-- Uses -->
  <g transform="translate(400,100)">
    <rect x="-80" y="-25" width="160" height="200" rx="6" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
    <text x="0" y="-8" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Значение мхов</text>
    <!-- Nature -->
    <text x="0" y="15" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">В природе:</text>
    <text x="-70" y="30" font-family="Arial,sans-serif" font-size="7" fill="#555">- Образуют болота</text>
    <text x="-70" y="42" font-family="Arial,sans-serif" font-size="7" fill="#555">- Накапливают воду</text>
    <text x="-70" y="54" font-family="Arial,sans-serif" font-size="7" fill="#555">- Фильтруют воду</text>
    <text x="-70" y="66" font-family="Arial,sans-serif" font-size="7" fill="#555">- Создают торф</text>
    <!-- Economy -->
    <text x="0" y="85" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">В хозяйстве:</text>
    <text x="-70" y="100" font-family="Arial,sans-serif" font-size="7" fill="#555">- Торф - топливо</text>
    <text x="-70" y="112" font-family="Arial,sans-serif" font-size="7" fill="#555">- Торф - удобрение</text>
    <text x="-70" y="124" font-family="Arial,sans-serif" font-size="7" fill="#555">- Сфагнум - перевяз.</text>
    <text x="-70" y="136" font-family="Arial,sans-serif" font-size="7" fill="#555">- Строит. материал</text>
    <text x="-70" y="148" font-family="Arial,sans-serif" font-size="7" fill="#555">- Клюква, морошка</text>
    <text x="-70" y="160" font-family="Arial,sans-serif" font-size="7" fill="#C62828">- Торф - горючее</text>
  </g>
'''

# ===== LESSON 15: Папоротники, хвощи и плауны: строение =====
l15 = '''
  <!-- Three plant types -->
  <!-- Fern -->
  <g transform="translate(90,175)">
    <rect x="-3" y="15" width="6" height="45" fill="#795548" rx="2"/>
    <!-- Fronds -->
    <path d="M0 15 Q-40 -15 -55 -35" stroke="#2E7D32" stroke-width="3" fill="none"/>
    <path d="M0 15 Q40 -15 55 -35" stroke="#2E7D32" stroke-width="3" fill="none"/>
    <path d="M0 25 Q-30 5 -45 -15" stroke="#43A047" stroke-width="2.5" fill="none"/>
    <path d="M0 25 Q30 5 45 -15" stroke="#43A047" stroke-width="2.5" fill="none"/>
    <!-- Leaflets -->
    <path d="M-25 -5 Q-35 -10 -30 0" fill="#66BB6A" opacity="0.6"/>
    <path d="M25 -5 Q35 -10 30 0" fill="#66BB6A" opacity="0.6"/>
    <!-- Fiddlehead -->
    <path d="M0 5 Q-5 -5 -3 -10 Q0 -15 3 -10 Q5 -5 0 5" fill="#81C784" stroke="#4CAF50" stroke-width="1"/>
    <!-- Sorus -->
    <circle cx="-35" cy="-15" r="3" fill="#8D6E63" opacity="0.6"/>
    <circle cx="-42" cy="-25" r="2.5" fill="#8D6E63" opacity="0.5"/>
    <circle cx="35" cy="-15" r="3" fill="#8D6E63" opacity="0.6"/>
    <!-- Roots -->
    <path d="M0 60 Q-10 70 -12 78" stroke="#795548" stroke-width="1.5" fill="none"/>
    <path d="M0 60 Q10 70 12 78" stroke="#795548" stroke-width="1.5" fill="none"/>
    <text x="0" y="95" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Папоротник</text>
  </g>
  <!-- Horsetail -->
  <g transform="translate(250,175)">
    <rect x="-2" y="-30" width="4" height="75" fill="#66BB6A" rx="1.5"/>
    <!-- Nodes with whorls -->
    <ellipse cx="0" cy="-20" rx="18" ry="5" fill="#81C784" stroke="#4CAF50" stroke-width="1"/>
    <ellipse cx="0" cy="-5" rx="18" ry="5" fill="#81C784" stroke="#4CAF50" stroke-width="1"/>
    <ellipse cx="0" cy="10" rx="18" ry="5" fill="#81C784" stroke="#4CAF50" stroke-width="1"/>
    <ellipse cx="0" cy="25" rx="18" ry="5" fill="#81C784" stroke="#4CAF50" stroke-width="1"/>
    <!-- Spore cone at top -->
    <ellipse cx="0" cy="-38" rx="6" ry="8" fill="#8D6E63" stroke="#5D4037" stroke-width="1.5"/>
    <!-- Roots -->
    <path d="M0 45 Q-8 55 -10 62" stroke="#795548" stroke-width="1.5" fill="none"/>
    <path d="M0 45 Q8 55 10 62" stroke="#795548" stroke-width="1.5" fill="none"/>
    <text x="0" y="80" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Хвощ</text>
    <text x="0" y="92" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(полевой)</text>
  </g>
  <!-- Clubmoss -->
  <g transform="translate(410,175)">
    <rect x="-2" y="-10" width="4" height="55" fill="#66BB6A" rx="1.5"/>
    <!-- Small leaves along stem -->
    <ellipse cx="-8" cy="0" rx="6" ry="3" fill="#81C784" opacity="0.7" transform="rotate(25,-8,0)"/>
    <ellipse cx="8" cy="0" rx="6" ry="3" fill="#81C784" opacity="0.7" transform="rotate(-25,8,0)"/>
    <ellipse cx="-9" cy="15" rx="6" ry="3" fill="#81C784" opacity="0.6" transform="rotate(20,-9,15)"/>
    <ellipse cx="9" cy="15" rx="6" ry="3" fill="#81C784" opacity="0.6" transform="rotate(-20,9,15)"/>
    <ellipse cx="-8" cy="30" rx="5" ry="3" fill="#81C784" opacity="0.6" transform="rotate(22,-8,30)"/>
    <ellipse cx="8" cy="30" rx="5" ry="3" fill="#81C784" opacity="0.6" transform="rotate(-22,8,30)"/>
    <!-- Spore stalk -->
    <line x1="0" y1="-10" x2="0" y2="-30" stroke="#8D6E63" stroke-width="1.5"/>
    <!-- Sporangia -->
    <ellipse cx="0" cy="-35" rx="5" ry="7" fill="#FDD835" stroke="#F9A825" stroke-width="1"/>
    <!-- Roots -->
    <path d="M0 45 Q-6 55 -8 60" stroke="#795548" stroke-width="1" fill="none"/>
    <path d="M0 45 Q6 55 8 60" stroke="#795548" stroke-width="1" fill="none"/>
    <text x="0" y="78" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Плаун</text>
  </g>
  <!-- Common features -->
  <rect x="40" y="270" width="420" height="40" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="286" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Высшие споровые: есть корни и ткани, но размножаются спорами</text>
  <text x="250" y="300" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Папоротники - вайи (листья) со спорангиями | Хвощи - стебли с мутовками | Плауны - стелющиеся побеги</text>
'''

# ===== LESSON 16: Происхождение и значение высших споровых =====
l16 = '''
  <!-- Evolution timeline of spore plants -->
  <!-- Timeline arrow -->
  <path d="M40 160 L460 160" stroke="#2E7D32" stroke-width="2"/>
  <path d="M460 160 L455 156 M460 160 L455 164" stroke="#2E7D32" stroke-width="2" fill="none"/>
  <text x="470" y="164" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32">время</text>
  <!-- Points on timeline -->
  <!-- 400 млн лет: first plants -->
  <circle cx="80" cy="160" r="6" fill="#4CAF50"/>
  <text x="80" y="148" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">400 млн</text>
  <g transform="translate(80,100)">
    <rect x="-30" y="-25" width="60" height="40" rx="4" fill="#E8F5E9" stroke="#4CAF50" stroke-width="1"/>
    <text x="0" y="-10" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Первые</text>
    <text x="0" y="2" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">растения</text>
    <text x="0" y="12" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">на суше</text>
  </g>
  <!-- 350 млн: mosses -->
  <circle cx="160" cy="160" r="6" fill="#66BB6A"/>
  <text x="160" y="148" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">350 млн</text>
  <g transform="translate(160,210)">
    <rect x="-30" y="-15" width="60" height="30" rx="4" fill="#C8E6C9" stroke="#66BB6A" stroke-width="1"/>
    <text x="0" y="0" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Мхи</text>
    <text x="0" y="10" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">простейшие</text>
  </g>
  <!-- 300 млн: ferns dominate (Carboniferous) -->
  <circle cx="260" cy="160" r="8" fill="#2E7D32"/>
  <text x="260" y="148" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">300 млн</text>
  <g transform="translate(260,85)">
    <rect x="-50" y="-25" width="100" height="45" rx="4" fill="#1B5E20" opacity="0.1" stroke="#2E7D32" stroke-width="1.5"/>
    <text x="0" y="-10" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Карбон!</text>
    <text x="0" y="3" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Леса папоротников</text>
    <text x="0" y="14" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">гигантские деревья</text>
  </g>
  <!-- Tree fern -->
  <g transform="translate(260,220)">
    <rect x="-4" y="0" width="8" height="40" fill="#795548" rx="2"/>
    <path d="M0 0 Q-25 -15 -35 -30" stroke="#2E7D32" stroke-width="2" fill="none"/>
    <path d="M0 0 Q25 -15 35 -30" stroke="#2E7D32" stroke-width="2" fill="none"/>
    <path d="M0 -10 Q-20 -20 -25 -35" stroke="#43A047" stroke-width="1.5" fill="none"/>
    <path d="M0 -10 Q20 -20 25 -35" stroke="#43A047" stroke-width="1.5" fill="none"/>
    <circle cx="-28" cy="-25" r="2" fill="#8D6E63"/>
    <circle cx="28" cy="-25" r="2" fill="#8D6E63"/>
  </g>
  <!-- 250 млн: coal formation -->
  <circle cx="370" cy="160" r="6" fill="#5D4037"/>
  <text x="370" y="148" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">250 млн</text>
  <g transform="translate(370,210)">
    <rect x="-35" y="-15" width="70" height="30" rx="4" fill="#5D4037" opacity="0.1" stroke="#5D4037" stroke-width="1"/>
    <text x="0" y="0" font-family="Arial,sans-serif" font-size="7" fill="#5D4037" text-anchor="middle" font-weight="bold">Образование</text>
    <text x="0" y="10" font-family="Arial,sans-serif" font-size="7" fill="#5D4037" text-anchor="middle">каменного угля</text>
  </g>
  <!-- Now -->
  <circle cx="450" cy="160" r="6" fill="#FF9800"/>
  <text x="450" y="148" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Сейчас</text>
  <!-- Coal formation diagram -->
  <rect x="30" y="270" width="440" height="40" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="286" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Древние папоротники -> отмерли -> упали в болото -> без кислорода -> каменный уголь</text>
  <text x="250" y="300" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Уголь - главное ископаемое топливо, созданное древними споровыми растениями</text>
'''

# Generate all SVGs
lessons = [
    (9, "Разнообразие грибов", l9),
    (10, "Лишайники - симбиоз гриба и водоросли", l10),
    (11, "Общая характеристика царства Растения", l11),
    (12, "Водоросли - древнейшие растения", l12),
    (13, "Мхи: строение и разнообразие", l13),
    (14, "Значение мхов в природе и хозяйстве", l14),
    (15, "Папоротники, хвощи и плауны: строение", l15),
    (16, "Происхождение и значение высших споровых", l16),
]

for num, title, illustration in lessons:
    svg_content = W(illustration, title, f"Биология 6 класс - Урок {num}")
    filepath = os.path.join(OUTPUT_DIR, f"lesson{num}.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Generated: lesson{num}.svg")

print("Done! 8 SVGs for Grade 6 Biology Lessons 9-16.")
