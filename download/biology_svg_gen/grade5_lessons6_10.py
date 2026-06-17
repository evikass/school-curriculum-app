#!/usr/bin/env python3
"""Generate detailed biology SVG illustrations for Grade 5, Lessons 6-10"""

import os

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade5/biology"
os.makedirs(OUTPUT_DIR, exist_ok=True)

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


# ===== LESSON 6: Химический состав клетки =====
lesson6_illustration = '''
  <!-- Pie chart of cell chemical composition -->
  <g transform="translate(160,190)">
    <!-- Water - 70% (large blue sector) -->
    <path d="M0 0 L0 -100 A100 100 0 1 1 -81 -59 Z" fill="#42A5F5" opacity="0.8"/>
    <!-- Proteins - 15% -->
    <path d="M0 0 L-81 -59 A100 100 0 0 1 -95 31 Z" fill="#EF5350" opacity="0.8"/>
    <!-- Lipids - 8% -->
    <path d="M0 0 L-95 31 A100 100 0 0 1 -56 82 Z" fill="#FFC107" opacity="0.8"/>
    <!-- Carbohydrates - 4% -->
    <path d="M0 0 L-56 82 A100 100 0 0 1 -22 97 Z" fill="#66BB6A" opacity="0.8"/>
    <!-- Nucleic acids - 3% -->
    <path d="M0 0 L-22 97 A100 100 0 0 1 0 100 Z" fill="#AB47BC" opacity="0.8"/>
    <!-- Center circle -->
    <circle cx="0" cy="0" r="35" fill="white" opacity="0.9"/>
    <text x="0" y="-3" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Хим.</text>
    <text x="0" y="10" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">состав</text>
  </g>
  <!-- Legend -->
  <g transform="translate(310,80)">
    <rect x="0" y="0" width="170" height="150" rx="6" fill="white" stroke="#ddd" stroke-width="1" opacity="0.9"/>
    <rect x="10" y="10" width="14" height="14" fill="#42A5F5" opacity="0.8" rx="2"/>
    <text x="30" y="22" font-family="Arial,sans-serif" font-size="10" fill="#333">Вода - 70%</text>
    <rect x="10" y="32" width="14" height="14" fill="#EF5350" opacity="0.8" rx="2"/>
    <text x="30" y="44" font-family="Arial,sans-serif" font-size="10" fill="#333">Белки - 15%</text>
    <rect x="10" y="54" width="14" height="14" fill="#FFC107" opacity="0.8" rx="2"/>
    <text x="30" y="66" font-family="Arial,sans-serif" font-size="10" fill="#333">Липиды - 8%</text>
    <rect x="10" y="76" width="14" height="14" fill="#66BB6A" opacity="0.8" rx="2"/>
    <text x="30" y="88" font-family="Arial,sans-serif" font-size="10" fill="#333">Углеводы - 4%</text>
    <rect x="10" y="98" width="14" height="14" fill="#AB47BC" opacity="0.8" rx="2"/>
    <text x="30" y="110" font-family="Arial,sans-serif" font-size="10" fill="#333">Нуклеиновые к-ты - 3%</text>
    <!-- Chemical symbols -->
    <text x="85" y="135" font-family="Arial,sans-serif" font-size="8" fill="#666" text-anchor="middle">C H O N P S</text>
  </g>
  <!-- Molecule illustrations -->
  <!-- Water molecule -->
  <g transform="translate(80,90)">
    <circle cx="0" cy="0" r="8" fill="#F44336" opacity="0.7"/>
    <text x="0" y="3" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">O</text>
    <circle cx="-12" cy="8" r="5" fill="#fff" stroke="#ccc" stroke-width="1"/>
    <text x="-12" y="11" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">H</text>
    <circle cx="12" cy="8" r="5" fill="#fff" stroke="#ccc" stroke-width="1"/>
    <text x="12" y="11" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">H</text>
    <line x1="-5" y1="4" x2="-9" y2="6" stroke="#999" stroke-width="1"/>
    <line x1="5" y1="4" x2="9" y2="6" stroke="#999" stroke-width="1"/>
    <text x="0" y="25" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">H2O</text>
  </g>
  <!-- Organic/Inorganic label -->
  <rect x="30" y="290" width="200" height="22" rx="4" fill="#2E7D32" opacity="0.1"/>
  <text x="130" y="305" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle">Неорганические и органические вещества</text>
'''

# ===== LESSON 7: Жизнедеятельность клетки =====
lesson7_illustration = '''
  <!-- Three cells showing different processes -->
  <!-- Cell 1: Обмен веществ (Metabolism) -->
  <g transform="translate(90,170)">
    <ellipse cx="0" cy="0" rx="55" ry="45" fill="#E8F5E9" stroke="#4CAF50" stroke-width="2"/>
    <ellipse cx="0" cy="-5" rx="18" ry="14" fill="#C8E6C9" stroke="#388E3C" stroke-width="1.5"/>
    <circle cx="0" cy="-5" r="5" fill="#81C784"/>
    <!-- Arrows in/out -->
    <path d="M-60 -10 L-65 -10" stroke="#42A5F5" stroke-width="2" fill="none"/>
    <path d="M-65 -10 L-60 -14 M-65 -10 L-60 -6" stroke="#42A5F5" stroke-width="1.5" fill="none"/>
    <text x="-68" y="-14" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="end">O2</text>
    <text x="-68" y="2" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="end">пища</text>
    <path d="M60 5 L65 5" stroke="#EF5350" stroke-width="2" fill="none"/>
    <path d="M65 5 L60 1 M65 5 L60 9" stroke="#EF5350" stroke-width="1.5" fill="none"/>
    <text x="68" y="2" font-family="Arial,sans-serif" font-size="6" fill="#C62828">CO2</text>
    <text x="68" y="12" font-family="Arial,sans-serif" font-size="6" fill="#C62828">энергия</text>
    <text x="0" y="60" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Обмен веществ</text>
  </g>
  <!-- Cell 2: Деление (Division) -->
  <g transform="translate(250,170)">
    <!-- Cell stretching -->
    <ellipse cx="-20" cy="0" rx="30" ry="35" fill="#E8F5E9" stroke="#4CAF50" stroke-width="2"/>
    <ellipse cx="20" cy="0" rx="30" ry="35" fill="#E8F5E9" stroke="#4CAF50" stroke-width="2"/>
    <!-- Pinch in middle -->
    <path d="M0 -35 Q-8 0 0 35" stroke="#4CAF50" stroke-width="2" fill="#E8F5E9"/>
    <path d="M0 -35 Q8 0 0 35" stroke="#4CAF50" stroke-width="2" fill="#E8F5E9"/>
    <!-- Nuclei -->
    <ellipse cx="-20" cy="-5" rx="12" ry="10" fill="#C8E6C9" stroke="#388E3C" stroke-width="1.5"/>
    <circle cx="-20" cy="-5" r="4" fill="#81C784"/>
    <ellipse cx="20" cy="-5" rx="12" ry="10" fill="#C8E6C9" stroke="#388E3C" stroke-width="1.5"/>
    <circle cx="20" cy="-5" r="4" fill="#81C784"/>
    <!-- Chromosomes -->
    <line x1="-24" y1="-8" x2="-16" y2="-2" stroke="#388E3C" stroke-width="1.5"/>
    <line x1="16" y1="-8" x2="24" y2="-2" stroke="#388E3C" stroke-width="1.5"/>
    <text x="0" y="55" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Деление</text>
  </g>
  <!-- Cell 3: Рост (Growth) -->
  <g transform="translate(400,170)">
    <!-- Small cell -->
    <ellipse cx="-15" cy="-15" rx="20" ry="16" fill="#E8F5E9" stroke="#4CAF50" stroke-width="1.5" opacity="0.5"/>
    <ellipse cx="-15" cy="-15" rx="8" ry="6" fill="#C8E6C9" stroke="#388E3C" stroke-width="1" opacity="0.5"/>
    <!-- Arrow -->
    <path d="M5 -15 L20 -15" stroke="#2E7D32" stroke-width="2"/>
    <path d="M20 -15 L15 -19 M20 -15 L15 -11" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
    <!-- Big cell -->
    <ellipse cx="0" cy="10" rx="40" ry="35" fill="#E8F5E9" stroke="#4CAF50" stroke-width="2"/>
    <ellipse cx="0" cy="5" rx="15" ry="12" fill="#C8E6C9" stroke="#388E3C" stroke-width="1.5"/>
    <circle cx="0" cy="5" r="5" fill="#81C784"/>
    <!-- Growth rings -->
    <ellipse cx="0" cy="10" rx="30" ry="26" fill="none" stroke="#81C784" stroke-width="0.5" stroke-dasharray="3,2"/>
    <text x="0" y="60" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Рост</text>
  </g>
  <!-- Bottom summary -->
  <rect x="100" y="260" width="300" height="40" rx="6" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="278" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Жизнедеятельность клетки:</text>
  <text x="250" y="292" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">обмен веществ, деление, рост, развитие</text>
'''

# ===== LESSON 8: Строение и жизнедеятельность бактерий =====
lesson8_illustration = '''
  <!-- Various bacteria shapes -->
  <!-- Cocci (шарообразные) -->
  <g transform="translate(80,120)">
    <circle cx="0" cy="0" r="15" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="12" fill="#FFCC80" opacity="0.5"/>
    <circle cx="25" cy="0" r="15" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
    <circle cx="25" cy="0" r="12" fill="#FFCC80" opacity="0.5"/>
    <circle cx="50" cy="0" r="15" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
    <circle cx="50" cy="0" r="12" fill="#FFCC80" opacity="0.5"/>
    <!-- Flagella absent -->
    <text x="25" y="35" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Кокки</text>
    <text x="25" y="46" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(шарообразные)</text>
  </g>
  <!-- Bacilli (палочковидные) -->
  <g transform="translate(220,110)">
    <rect x="-30" y="-10" width="60" height="20" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5" rx="10"/>
    <rect x="-25" y="-6" width="50" height="12" fill="#FFCC80" opacity="0.4" rx="6"/>
    <!-- Internal structure -->
    <ellipse cx="0" cy="0" rx="10" ry="5" fill="#E65100" opacity="0.3"/>
    <!-- Flagella -->
    <path d="M-30 0 Q-40 -5 -45 0 Q-50 5 -55 0" stroke="#E65100" stroke-width="1" fill="none"/>
    <text x="0" y="35" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Палочки</text>
    <text x="0" y="46" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(палочковидные)</text>
  </g>
  <!-- Spirilla (спиральные) -->
  <g transform="translate(370,110)">
    <path d="M-30 0 Q-20 -15 -10 0 Q0 15 10 0 Q20 -15 30 0" stroke="#E65100" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path d="M-30 0 Q-20 -15 -10 0 Q0 15 10 0 Q20 -15 30 0" stroke="#FFCC80" stroke-width="4" fill="none" stroke-linecap="round"/>
    <!-- Flagella -->
    <path d="M30 0 Q40 -5 45 0 Q50 5 55 0" stroke="#E65100" stroke-width="1" fill="none"/>
    <text x="0" y="35" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Спириллы</text>
    <text x="0" y="46" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(спиральные)</text>
  </g>
  <!-- Bacteria cell structure (detailed) -->
  <g transform="translate(250,240)">
    <ellipse cx="0" cy="0" rx="65" ry="35" fill="#FFE0B2" stroke="#E65100" stroke-width="2"/>
    <!-- Cell wall -->
    <ellipse cx="0" cy="0" rx="60" ry="30" fill="none" stroke="#BF360C" stroke-width="1.5" stroke-dasharray="4,2"/>
    <!-- Cell membrane -->
    <ellipse cx="0" cy="0" rx="55" ry="26" fill="#FFF3E0" opacity="0.5"/>
    <!-- Nucleoid (circular DNA) -->
    <ellipse cx="-10" cy="-3" rx="20" ry="10" fill="none" stroke="#E65100" stroke-width="1.5"/>
    <!-- Ribosomes -->
    <circle cx="15" cy="-8" r="3" fill="#FF8A65"/>
    <circle cx="20" cy="5" r="3" fill="#FF8A65"/>
    <circle cx="10" cy="10" r="3" fill="#FF8A65"/>
    <circle cx="-20" cy="8" r="3" fill="#FF8A65"/>
    <!-- Plasmid -->
    <circle cx="25" cy="-3" r="6" fill="none" stroke="#D84315" stroke-width="1"/>
    <!-- Flagellum -->
    <path d="M65 0 Q75 -5 80 0 Q85 5 90 0 Q95 -5 100 0" stroke="#E65100" stroke-width="1.5" fill="none"/>
    <!-- Capsule hint -->
    <path d="M-50 -30 Q0 -42 50 -30" stroke="#FFB74D" stroke-width="1" fill="none" stroke-dasharray="2,2"/>
  </g>
  <!-- Structure labels -->
  <text x="370" y="218" font-family="Arial,sans-serif" font-size="7" fill="#333">Жгутик</text>
  <line x1="368" y1="220" x2="340" y2="235" stroke="#333" stroke-width="0.5"/>
  <text x="140" y="220" font-family="Arial,sans-serif" font-size="7" fill="#333">Клеточная стенка</text>
  <line x1="190" y1="222" x2="210" y2="232" stroke="#333" stroke-width="0.5"/>
  <text x="250" y="290" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Нуклеоид (ДНК)</text>
  <line x1="240" y1="250" x2="242" y2="265" stroke="#333" stroke-width="0.5"/>
  <text x="80" y="270" font-family="Arial,sans-serif" font-size="7" fill="#333">Рибосомы</text>
  <line x1="118" y1="268" x2="155" y2="252" stroke="#333" stroke-width="0.5"/>
  <text x="150" y="290" font-family="Arial,sans-serif" font-size="7" fill="#333">Плазмида</text>
  <line x1="195" y1="286" x2="240" y2="250" stroke="#333" stroke-width="0.5"/>
'''

# ===== LESSON 9: Роль бактерий в природе и жизни человека =====
lesson9_illustration = '''
  <!-- Positive roles (left side) -->
  <g transform="translate(130,100)">
    <rect x="-100" y="-30" width="200" height="25" rx="4" fill="#4CAF50" opacity="0.15"/>
    <text x="0" y="-12" font-family="Arial,sans-serif" font-size="11" fill="#2E7D32" text-anchor="middle" font-weight="bold">Положительная роль</text>
    <!-- Nitrogen fixation -->
    <g transform="translate(-60,30)">
      <circle cx="0" cy="0" r="22" fill="#E8F5E9" stroke="#4CAF50" stroke-width="1.5"/>
      <text x="0" y="-5" font-family="Arial,sans-serif" font-size="16" fill="#4CAF50" text-anchor="middle">N</text>
      <text x="0" y="10" font-family="Arial,sans-serif" font-size="7" fill="#4CAF50" text-anchor="middle">2</text>
      <path d="M0 22 L0 30" stroke="#4CAF50" stroke-width="1.5"/>
      <path d="M0 30 L-3 26 M0 30 L3 26" stroke="#4CAF50" stroke-width="1"/>
      <text x="0" y="42" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Азото-</text>
      <text x="0" y="52" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">фиксация</text>
    </g>
    <!-- Decomposition -->
    <g transform="translate(0,30)">
      <path d="M-12 5 L-8 -5 L-2 5 L2 -5 L8 5 L12 -5" stroke="#795548" stroke-width="2" fill="none"/>
      <path d="M-5 10 Q0 8 5 10" stroke="#8D6E63" stroke-width="1" fill="none"/>
      <circle cx="0" cy="-12" r="3" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
      <circle cx="8" cy="-8" r="2.5" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
      <circle cx="-8" cy="-8" r="2.5" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
      <text x="0" y="25" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Разрушение</text>
      <text x="0" y="35" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">органики</text>
    </g>
    <!-- Food production -->
    <g transform="translate(60,30)">
      <rect x="-12" y="-10" width="24" height="20" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5" rx="3"/>
      <text x="0" y="4" font-family="Arial,sans-serif" font-size="8" fill="#F57F17" text-anchor="middle">M</text>
      <text x="0" y="25" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Молочные</text>
      <text x="0" y="35" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">продукты</text>
    </g>
  </g>
  <!-- Negative roles (right side) -->
  <g transform="translate(370,100)">
    <rect x="-100" y="-30" width="200" height="25" rx="4" fill="#F44336" opacity="0.12"/>
    <text x="0" y="-12" font-family="Arial,sans-serif" font-size="11" fill="#C62828" text-anchor="middle" font-weight="bold">Отрицательная роль</text>
    <!-- Diseases -->
    <g transform="translate(-50,30)">
      <circle cx="0" cy="0" r="18" fill="#FFCDD2" stroke="#E53935" stroke-width="1.5"/>
      <path d="M-5 -5 L5 5 M5 -5 L-5 5" stroke="#E53935" stroke-width="2"/>
      <text x="0" y="30" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Заболевания</text>
    </g>
    <!-- Food spoilage -->
    <g transform="translate(0,30)">
      <rect x="-15" y="-12" width="30" height="24" fill="#FFF3E0" stroke="#FF9800" stroke-width="1.5" rx="3"/>
      <!-- Mold spots -->
      <circle cx="-5" cy="-3" r="4" fill="#8BC34A" opacity="0.6"/>
      <circle cx="5" cy="3" r="3" fill="#8BC34A" opacity="0.5"/>
      <circle cx="0" cy="7" r="3" fill="#8BC34A" opacity="0.4"/>
      <text x="0" y="30" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Порча</text>
      <text x="0" y="40" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">продуктов</text>
    </g>
    <!-- Bioterrorism/industrial damage -->
    <g transform="translate(50,30)">
      <path d="M-10 -10 L0 -15 L10 -10 L10 0 Q0 10 -10 0 Z" fill="#FFCDD2" stroke="#E53935" stroke-width="1"/>
      <text x="0" y="20" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Опасные</text>
      <text x="0" y="30" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">инфекции</text>
    </g>
  </g>
  <!-- Divider -->
  <line x1="250" y1="65" x2="250" y2="260" stroke="#999" stroke-width="1" stroke-dasharray="5,3"/>
  <!-- Bottom note -->
  <rect x="80" y="268" width="340" height="35" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="283" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Бактерии - самые древние организмы на Земле</text>
  <text x="250" y="296" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Существуют более 3,5 млрд лет</text>
'''

# ===== LESSON 10: Общая характеристика грибов =====
lesson10_illustration = '''
  <!-- Mushroom anatomy -->
  <g transform="translate(130,180)">
    <!-- Cap -->
    <path d="M-40 0 Q-45 -30 -20 -40 Q0 -48 20 -40 Q45 -30 40 0 Z" fill="#D84315" stroke="#BF360C" stroke-width="1.5"/>
    <!-- Cap spots -->
    <circle cx="-15" cy="-20" r="5" fill="white" opacity="0.5"/>
    <circle cx="10" cy="-25" r="4" fill="white" opacity="0.5"/>
    <circle cx="0" cy="-12" r="3.5" fill="white" opacity="0.4"/>
    <!-- Gills under cap -->
    <path d="M-35 0 Q-30 8 -10 12" stroke="#FFAB91" stroke-width="0.8" fill="none"/>
    <path d="M-25 0 Q-20 8 -5 12" stroke="#FFAB91" stroke-width="0.8" fill="none"/>
    <path d="M-15 0 Q-10 8 0 12" stroke="#FFAB91" stroke-width="0.8" fill="none"/>
    <path d="M0 0 Q5 8 5 12" stroke="#FFAB91" stroke-width="0.8" fill="none"/>
    <path d="M15 0 Q10 8 10 12" stroke="#FFAB91" stroke-width="0.8" fill="none"/>
    <path d="M25 0 Q20 8 15 12" stroke="#FFAB91" stroke-width="0.8" fill="none"/>
    <path d="M35 0 Q25 8 20 12" stroke="#FFAB91" stroke-width="0.8" fill="none"/>
    <!-- Stipe (stem) -->
    <rect x="-8" y="12" width="16" height="55" fill="#FFF3E0" stroke="#D7CCC8" stroke-width="1.5" rx="5"/>
    <!-- Ring on stipe -->
    <ellipse cx="0" cy="30" rx="12" ry="4" fill="#FFECB3" stroke="#D7CCC8" stroke-width="1"/>
    <!-- Mycelium (roots) -->
    <path d="M-8 67 Q-20 80 -35 85" stroke="#D7CCC8" stroke-width="2" fill="none"/>
    <path d="M0 67 Q-5 80 -10 90" stroke="#D7CCC8" stroke-width="2" fill="none"/>
    <path d="M8 67 Q20 80 35 85" stroke="#D7CCC8" stroke-width="2" fill="none"/>
    <path d="M0 67 Q10 82 20 90" stroke="#D7CCC8" stroke-width="1.5" fill="none"/>
    <path d="M-5 67 Q-15 85 -25 92" stroke="#D7CCC8" stroke-width="1.5" fill="none"/>
    <!-- Small branching mycelium -->
    <path d="M-35 85 Q-40 88 -45 82" stroke="#D7CCC8" stroke-width="1" fill="none"/>
    <path d="M35 85 Q40 88 45 82" stroke="#D7CCC8" stroke-width="1" fill="none"/>
  </g>
  <!-- Labels -->
  <line x1="170" y1="145" x2="260" y2="90" stroke="#333" stroke-width="0.7"/>
  <text x="265" y="90" font-family="Arial,sans-serif" font-size="9" fill="#333" font-weight="bold">Шляпка</text>
  <line x1="138" y1="185" x2="260" y2="120" stroke="#333" stroke-width="0.7"/>
  <text x="265" y="122" font-family="Arial,sans-serif" font-size="9" fill="#333" font-weight="bold">Пластинки</text>
  <line x1="138" y1="210" x2="260" y2="155" stroke="#333" stroke-width="0.7"/>
  <text x="265" y="155" font-family="Arial,sans-serif" font-size="9" fill="#333" font-weight="bold">Кольцо</text>
  <line x1="138" y1="230" x2="260" y2="185" stroke="#333" stroke-width="0.7"/>
  <text x="265" y="187" font-family="Arial,sans-serif" font-size="9" fill="#333" font-weight="bold">Ножка</text>
  <line x1="115" y1="265" x2="260" y2="220" stroke="#333" stroke-width="0.7"/>
  <text x="265" y="222" font-family="Arial,sans-serif" font-size="9" fill="#333" font-weight="bold">Грибница (мицелий)</text>
  <!-- Characteristics box -->
  <rect x="260" y="245" width="220" height="65" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="370" y="260" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Особенности грибов</text>
  <text x="270" y="275" font-family="Arial,sans-serif" font-size="8" fill="#555">- Не фотосинтезируют (гетеротрофы)</text>
  <text x="270" y="287" font-family="Arial,sans-serif" font-size="8" fill="#555">- Клеточная стенка из хитина</text>
  <text x="270" y="299" font-family="Arial,sans-serif" font-size="8" fill="#555">- Запасное вещество - гликоген</text>
  <!-- Spore illustration -->
  <g transform="translate(380,130)">
    <ellipse cx="0" cy="0" rx="8" ry="5" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
    <text x="0" y="20" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Спора</text>
    <!-- Spore dispersal -->
    <path d="M-2 -5 Q-8 -15 -12 -20" stroke="#8D6E63" stroke-width="0.8" fill="none" opacity="0.5"/>
    <path d="M2 -5 Q5 -18 3 -25" stroke="#8D6E63" stroke-width="0.8" fill="none" opacity="0.5"/>
    <path d="M0 -5 Q2 -15 8 -18" stroke="#8D6E63" stroke-width="0.8" fill="none" opacity="0.4"/>
  </g>
  <!-- Hyphae detail -->
  <g transform="translate(380,170)">
    <path d="M-20 0 Q-10 -8 0 0 Q10 8 20 0" stroke="#D7CCC8" stroke-width="3" fill="none"/>
    <path d="M-20 0 Q-10 -8 0 0 Q10 8 20 0" stroke="#EFEBE9" stroke-width="1.5" fill="none"/>
    <!-- Septum -->
    <line x1="0" y1="-4" x2="0" y2="4" stroke="#BCAAA4" stroke-width="1"/>
    <text x="0" y="18" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Гифы</text>
  </g>
'''

# Generate all SVGs
lessons = [
    (6, "Химический состав клетки", lesson6_illustration),
    (7, "Жизнедеятельность клетки", lesson7_illustration),
    (8, "Строение и жизнедеятельность бактерий", lesson8_illustration),
    (9, "Роль бактерий в природе и жизни человека", lesson9_illustration),
    (10, "Общая характеристика грибов", lesson10_illustration),
]

for num, title, illustration in lessons:
    subtitle = f"Биология 5 класс - Урок {num}"
    svg_content = svg_wrap(illustration, title, subtitle)
    filepath = os.path.join(OUTPUT_DIR, f"lesson{num}.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Generated: {filepath}")

print("\nDone! 5 SVGs generated for Grade 5 Biology Lessons 6-10.")
