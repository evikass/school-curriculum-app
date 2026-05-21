#!/usr/bin/env python3
"""Generate detailed biology SVG illustrations for Grade 6, Lessons 1-8"""

import os

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade6/biology"
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
  <text x="250" y="339" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="white" font-weight="bold">Биология 6 класс</text>
</svg>'''

W = svg_wrap

# ===== LESSON 1: Биология — наука о живой природе =====
l1 = '''
  <!-- Open book with nature symbols -->
  <g transform="translate(250,180)">
    <!-- Book -->
    <path d="M-100 50 L-100 -40 Q-50 -55 0 -40 Q50 -55 100 -40 L100 50 Q50 35 0 50 Q-50 35 -100 50 Z" fill="#FFF9C4" stroke="#F9A825" stroke-width="2"/>
    <!-- Left page lines -->
    <line x1="-80" y1="-20" x2="-20" y2="-25" stroke="#E0E0E0" stroke-width="0.8"/>
    <line x1="-80" y1="-8" x2="-20" y2="-13" stroke="#E0E0E0" stroke-width="0.8"/>
    <line x1="-80" y1="4" x2="-20" y2="-1" stroke="#E0E0E0" stroke-width="0.8"/>
    <line x1="-80" y1="16" x2="-20" y2="11" stroke="#E0E0E0" stroke-width="0.8"/>
    <!-- Right page lines -->
    <line x1="20" y1="-25" x2="80" y2="-20" stroke="#E0E0E0" stroke-width="0.8"/>
    <line x1="20" y1="-13" x2="80" y2="-8" stroke="#E0E0E0" stroke-width="0.8"/>
    <line x1="20" y1="-1" x2="80" y2="4" stroke="#E0E0E0" stroke-width="0.8"/>
    <line x1="20" y1="11" x2="80" y2="16" stroke="#E0E0E0" stroke-width="0.8"/>
    <!-- Spine -->
    <line x1="0" y1="-40" x2="0" y2="50" stroke="#F9A825" stroke-width="1.5"/>
    <!-- Plant symbol on left -->
    <g transform="translate(-50,-10)">
      <line x1="0" y1="15" x2="0" y2="-5" stroke="#4CAF50" stroke-width="2"/>
      <ellipse cx="-8" cy="-3" rx="8" ry="5" fill="#81C784" transform="rotate(30,-8,-3)"/>
      <ellipse cx="8" cy="-3" rx="8" ry="5" fill="#81C784" transform="rotate(-30,8,-3)"/>
    </g>
    <!-- Animal symbol on right -->
    <g transform="translate(50,-10)">
      <ellipse cx="0" cy="0" rx="10" ry="7" fill="#FFAB91" stroke="#E64A19" stroke-width="1"/>
      <circle cx="-7" cy="-3" r="3" fill="#FFAB91" stroke="#E64A19" stroke-width="1"/>
      <circle cx="-8" cy="-4" r="1" fill="#333"/>
    </g>
  </g>
  <!-- Branches of biology around the book -->
  <g transform="translate(80,85)">
    <rect x="-35" y="-12" width="70" height="24" rx="12" fill="#4CAF50" opacity="0.7"/>
    <text x="0" y="4" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Ботаника</text>
  </g>
  <g transform="translate(250,72)">
    <rect x="-45" y="-12" width="90" height="24" rx="12" fill="#2E7D32" opacity="0.8"/>
    <text x="0" y="4" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">БИОЛОГИЯ</text>
  </g>
  <g transform="translate(420,85)">
    <rect x="-35" y="-12" width="70" height="24" rx="12" fill="#FF9800" opacity="0.7"/>
    <text x="0" y="4" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Зоология</text>
  </g>
  <g transform="translate(100,280)">
    <rect x="-45" y="-12" width="90" height="24" rx="12" fill="#9C27B0" opacity="0.5"/>
    <text x="0" y="4" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">Микробиология</text>
  </g>
  <g transform="translate(400,280)">
    <rect x="-35" y="-12" width="70" height="24" rx="12" fill="#009688" opacity="0.5"/>
    <text x="0" y="4" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle">Экология</text>
  </g>
'''

# ===== LESSON 2: Признаки живого и уровни организации =====
l2 = '''
  <!-- Levels of organization pyramid -->
  <g transform="translate(150,190)">
    <!-- Bottom: Молекулярный -->
    <path d="M-120 80 L120 80 L90 55 L-90 55 Z" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
    <text x="0" y="72" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" text-anchor="middle">Молекулярный</text>
    <!-- Клеточный -->
    <path d="M-90 55 L90 55 L60 30 L-60 30 Z" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1.5"/>
    <text x="0" y="47" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">Клеточный</text>
    <!-- Тканевый -->
    <path d="M-60 30 L60 30 L35 5 L-35 5 Z" fill="#FFF3E0" stroke="#E65100" stroke-width="1.5"/>
    <text x="0" y="22" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle">Тканевый</text>
    <!-- Органный -->
    <path d="M-35 5 L35 5 L20 -18 L-20 -18 Z" fill="#FCE4EC" stroke="#C62828" stroke-width="1.5"/>
    <text x="0" y="-2" font-family="Arial,sans-serif" font-size="8" fill="#C62828" text-anchor="middle">Органный</text>
    <!-- Организменный -->
    <path d="M-20 -18 L20 -18 L8 -38 L-8 -38 Z" fill="#E8EAF6" stroke="#283593" stroke-width="1.5"/>
    <text x="0" y="-24" font-family="Arial,sans-serif" font-size="7" fill="#283593" text-anchor="middle">Организменный</text>
  </g>
  <!-- Signs of living on right -->
  <rect x="290" y="65" width="190" height="230" rx="8" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="385" y="82" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle" font-weight="bold">Признаки живого</text>
  <circle cx="310" cy="100" r="6" fill="#4CAF50" opacity="0.7"/><text x="325" y="104" font-family="Arial,sans-serif" font-size="8" fill="#333">Питание</text>
  <circle cx="310" cy="125" r="6" fill="#42A5F5" opacity="0.7"/><text x="325" y="129" font-family="Arial,sans-serif" font-size="8" fill="#333">Дыхание</text>
  <circle cx="310" cy="150" r="6" fill="#FF9800" opacity="0.7"/><text x="325" y="154" font-family="Arial,sans-serif" font-size="8" fill="#333">Выделение</text>
  <circle cx="310" cy="175" r="6" fill="#9C27B0" opacity="0.7"/><text x="325" y="179" font-family="Arial,sans-serif" font-size="8" fill="#333">Размножение</text>
  <circle cx="310" cy="200" r="6" fill="#E53935" opacity="0.7"/><text x="325" y="204" font-family="Arial,sans-serif" font-size="8" fill="#333">Рост и развитие</text>
  <circle cx="310" cy="225" r="6" fill="#009688" opacity="0.7"/><text x="325" y="229" font-family="Arial,sans-serif" font-size="8" fill="#333">Движение</text>
  <circle cx="310" cy="250" r="6" fill="#795548" opacity="0.7"/><text x="325" y="254" font-family="Arial,sans-serif" font-size="8" fill="#333">Раздражимость</text>
  <circle cx="310" cy="275" r="6" fill="#607D8B" opacity="0.7"/><text x="325" y="279" font-family="Arial,sans-serif" font-size="8" fill="#333">Обмен веществ</text>
'''

# ===== LESSON 3: Устройство увеличительных приборов. Клетка =====
l3 = '''
  <!-- Microscope with light path and cell view -->
  <g transform="translate(150,170)">
    <!-- Microscope simplified -->
    <rect x="-35" y="60" width="70" height="10" fill="#546E7A" rx="3"/>
    <rect x="-5" y="-30" width="10" height="95" fill="#78909C" rx="2"/>
    <rect x="-25" y="35" width="50" height="5" fill="#90A4AE"/>
    <rect x="-8" y="-42" width="16" height="15" fill="#607D8B" rx="3"/>
    <ellipse cx="0" cy="-42" rx="10" ry="4" fill="#455A64"/>
    <circle cx="10" cy="15" r="6" fill="#546E7A" stroke="#455A64" stroke-width="1"/>
  </g>
  <!-- What you see through eyepiece -->
  <g transform="translate(370,170)">
    <circle cx="0" cy="0" r="80" fill="white" stroke="#455A64" stroke-width="2"/>
    <circle cx="0" cy="0" r="78" fill="#F1F8E9" stroke="#90A4AE" stroke-width="0.5"/>
    <!-- Cells in view -->
    <rect x="-55" y="-45" width="35" height="30" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1.5" rx="2"/>
    <ellipse cx="-38" cy="-30" rx="8" ry="6" fill="#A5D6A7" stroke="#388E3C" stroke-width="1"/>
    <circle cx="-38" cy="-30" r="3" fill="#81C784"/>
    <rect x="-15" y="-45" width="35" height="30" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1.5" rx="2"/>
    <ellipse cx="2" cy="-30" rx="8" ry="6" fill="#A5D6A7" stroke="#388E3C" stroke-width="1"/>
    <rect x="-55" y="-10" width="35" height="30" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1.5" rx="2"/>
    <ellipse cx="-38" cy="5" rx="8" ry="6" fill="#A5D6A7" stroke="#388E3C" stroke-width="1"/>
    <rect x="-15" y="-10" width="35" height="30" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1.5" rx="2"/>
    <rect x="25" y="-45" width="30" height="30" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1.5" rx="2"/>
    <rect x="25" y="-10" width="30" height="30" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1.5" rx="2"/>
    <rect x="-55" y="25" width="35" height="30" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1.5" rx="2"/>
    <rect x="-15" y="25" width="35" height="30" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1.5" rx="2"/>
    <rect x="25" y="25" width="30" height="30" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1.5" rx="2"/>
    <!-- Cross-hair -->
    <line x1="-78" y1="0" x2="78" y2="0" stroke="#333" stroke-width="0.3" opacity="0.4"/>
    <line x1="0" y1="-78" x2="0" y2="78" stroke="#333" stroke-width="0.3" opacity="0.4"/>
  </g>
  <!-- Labels -->
  <text x="150" y="270" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Микроскоп</text>
  <text x="370" y="270" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Вид в окуляр</text>
  <!-- Arrow between -->
  <path d="M220 170 L280 170" stroke="#2E7D32" stroke-width="2"/>
  <path d="M280 170 L275 166 M280 170 L275 174" stroke="#2E7D32" stroke-width="2" fill="none"/>
  <!-- Magnification note -->
  <rect x="80" y="290" width="340" height="22" rx="4" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="305" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">Увеличение = окуляр (10x) x объектив (10x, 40x) = 100x - 400x</text>
'''

# ===== LESSON 4: Химический состав клетки =====
l4 = '''
  <!-- Molecular models and chart -->
  <!-- Pie chart -->
  <g transform="translate(130,185)">
    <path d="M0 0 L0 -80 A80 80 0 1 1 -65 -47 Z" fill="#42A5F5" opacity="0.7"/>
    <path d="M0 0 L-65 -47 A80 80 0 0 1 -76 26 Z" fill="#EF5350" opacity="0.7"/>
    <path d="M0 0 L-76 26 A80 80 0 0 1 -45 66 Z" fill="#FFC107" opacity="0.7"/>
    <path d="M0 0 L-45 66 A80 80 0 0 1 0 80 Z" fill="#66BB6A" opacity="0.7"/>
    <path d="M0 0 L0 80 A80 80 0 0 1 45 66 Z" fill="#AB47BC" opacity="0.7"/>
    <path d="M0 0 L45 66 A80 80 0 0 1 72 35 Z" fill="#FF7043" opacity="0.7"/>
    <circle cx="0" cy="0" r="30" fill="white" opacity="0.9"/>
    <text x="0" y="-3" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Вода</text>
    <text x="0" y="9" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">70-80%</text>
  </g>
  <!-- Legend -->
  <g transform="translate(290,75)">
    <rect x="0" y="0" width="185" height="155" rx="6" fill="white" stroke="#ddd" stroke-width="1" opacity="0.9"/>
    <rect x="8" y="8" width="12" height="12" fill="#42A5F5" opacity="0.7" rx="2"/><text x="26" y="18" font-family="Arial,sans-serif" font-size="9" fill="#333">Вода 70-80%</text>
    <rect x="8" y="28" width="12" height="12" fill="#EF5350" opacity="0.7" rx="2"/><text x="26" y="38" font-family="Arial,sans-serif" font-size="9" fill="#333">Белки 10-20%</text>
    <rect x="8" y="48" width="12" height="12" fill="#FFC107" opacity="0.7" rx="2"/><text x="26" y="58" font-family="Arial,sans-serif" font-size="9" fill="#333">Липиды 1-5%</text>
    <rect x="8" y="68" width="12" height="12" fill="#66BB6A" opacity="0.7" rx="2"/><text x="26" y="78" font-family="Arial,sans-serif" font-size="9" fill="#333">Углеводы 1-2%</text>
    <rect x="8" y="88" width="12" height="12" fill="#AB47BC" opacity="0.7" rx="2"/><text x="26" y="98" font-family="Arial,sans-serif" font-size="9" fill="#333">Нуклеиновые к-ты 1-3%</text>
    <rect x="8" y="108" width="12" height="12" fill="#FF7043" opacity="0.7" rx="2"/><text x="26" y="118" font-family="Arial,sans-serif" font-size="9" fill="#333">Минеральные в-ва 1-1.5%</text>
    <text x="92" y="143" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Органические и неорганические</text>
  </g>
  <!-- DNA helix -->
  <g transform="translate(350,270)">
    <path d="M-30 -15 Q-15 -25 0 -15 Q15 -5 30 -15" stroke="#AB47BC" stroke-width="2.5" fill="none"/>
    <path d="M-30 -15 Q-15 -5 0 -15 Q15 -25 30 -15" stroke="#CE93D8" stroke-width="2.5" fill="none"/>
    <line x1="-15" y1="-20" x2="-15" y2="-10" stroke="#CE93D8" stroke-width="1"/>
    <line x1="0" y1="-20" x2="0" y2="-10" stroke="#CE93D8" stroke-width="1"/>
    <line x1="15" y1="-20" x2="15" y2="-10" stroke="#CE93D8" stroke-width="1"/>
    <path d="M-30 15 Q-15 5 0 15 Q15 25 30 15" stroke="#AB47BC" stroke-width="2.5" fill="none"/>
    <path d="M-30 15 Q-15 25 0 15 Q15 5 30 15" stroke="#CE93D8" stroke-width="2.5" fill="none"/>
    <text x="0" y="35" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle">ДНК</text>
  </g>
  <!-- Protein chain -->
  <g transform="translate(100,290)">
    <circle cx="-20" cy="0" r="5" fill="#EF5350" opacity="0.6"/>
    <circle cx="-8" cy="0" r="5" fill="#42A5F5" opacity="0.6"/>
    <circle cx="4" cy="0" r="5" fill="#66BB6A" opacity="0.6"/>
    <circle cx="16" cy="0" r="5" fill="#FFC107" opacity="0.6"/>
    <circle cx="28" cy="0" r="5" fill="#AB47BC" opacity="0.6"/>
    <text x="4" y="16" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Аминокислоты - белок</text>
  </g>
'''

# ===== LESSON 5: Жизнедеятельность клетки: деление и рост =====
l5 = '''
  <!-- Cell division stages (mitosis simplified) -->
  <!-- Stage 1: Interphase -->
  <g transform="translate(80,130)">
    <circle cx="0" cy="0" r="28" fill="#E8F5E9" stroke="#4CAF50" stroke-width="2"/>
    <ellipse cx="0" cy="0" rx="10" ry="8" fill="#C8E6C9" stroke="#388E3C" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="3" fill="#81C784"/>
    <text x="0" y="40" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Интерфаза</text>
  </g>
  <!-- Arrow -->
  <path d="M115 130 L140 130" stroke="#2E7D32" stroke-width="1.5"/>
  <path d="M140 130 L136 126 M140 130 L136 134" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
  <!-- Stage 2: Prophase -->
  <g transform="translate(180,130)">
    <circle cx="0" cy="0" r="28" fill="#E8F5E9" stroke="#4CAF50" stroke-width="2"/>
    <!-- Condensed chromosomes -->
    <line x1="-8" y1="-6" x2="8" y2="6" stroke="#E53935" stroke-width="2.5"/>
    <line x1="-8" y1="6" x2="8" y2="-6" stroke="#E53935" stroke-width="2.5"/>
    <!-- Nuclear membrane dissolving -->
    <ellipse cx="0" cy="0" rx="12" ry="9" fill="none" stroke="#388E3C" stroke-width="1" stroke-dasharray="3,2"/>
    <text x="0" y="40" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Профаза</text>
  </g>
  <!-- Arrow -->
  <path d="M215 130 L240 130" stroke="#2E7D32" stroke-width="1.5"/>
  <path d="M240 130 L236 126 M240 130 L236 134" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
  <!-- Stage 3: Metaphase -->
  <g transform="translate(280,130)">
    <circle cx="0" cy="0" r="28" fill="#E8F5E9" stroke="#4CAF50" stroke-width="2"/>
    <!-- Spindle fibers -->
    <line x1="-20" y1="-20" x2="0" y2="0" stroke="#999" stroke-width="0.5"/>
    <line x1="20" y1="-20" x2="0" y2="0" stroke="#999" stroke-width="0.5"/>
    <line x1="-20" y1="20" x2="0" y2="0" stroke="#999" stroke-width="0.5"/>
    <line x1="20" y1="20" x2="0" y2="0" stroke="#999" stroke-width="0.5"/>
    <!-- Chromosomes at equator -->
    <line x1="-6" y1="-4" x2="6" y2="4" stroke="#E53935" stroke-width="2.5"/>
    <line x1="-6" y1="4" x2="6" y2="-4" stroke="#E53935" stroke-width="2.5"/>
    <text x="0" y="40" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Метафаза</text>
  </g>
  <!-- Arrow -->
  <path d="M315 130 L340 130" stroke="#2E7D32" stroke-width="1.5"/>
  <path d="M340 130 L336 126 M340 130 L336 134" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
  <!-- Stage 4: Anaphase -->
  <g transform="translate(380,130)">
    <circle cx="0" cy="0" r="28" fill="#E8F5E9" stroke="#4CAF50" stroke-width="2"/>
    <!-- Chromosomes separating -->
    <line x1="-10" y1="-4" x2="-4" y2="4" stroke="#E53935" stroke-width="2"/>
    <line x1="-10" y1="4" x2="-4" y2="-4" stroke="#E53935" stroke-width="2"/>
    <line x1="4" y1="-4" x2="10" y2="4" stroke="#E53935" stroke-width="2"/>
    <line x1="4" y1="4" x2="10" y2="-4" stroke="#E53935" stroke-width="2"/>
    <!-- Spindle -->
    <line x1="-18" y1="-15" x2="-7" y2="0" stroke="#999" stroke-width="0.5"/>
    <line x1="-18" y1="15" x2="-7" y2="0" stroke="#999" stroke-width="0.5"/>
    <line x1="18" y1="-15" x2="7" y2="0" stroke="#999" stroke-width="0.5"/>
    <line x1="18" y1="15" x2="7" y2="0" stroke="#999" stroke-width="0.5"/>
    <text x="0" y="40" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Анафаза</text>
  </g>
  <!-- Arrow -->
  <path d="M415 130 L440 130" stroke="#2E7D32" stroke-width="1.5"/>
  <path d="M440 130 L436 126 M440 130 L436 134" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
  <!-- Stage 5: Telophase / Two cells -->
  <g transform="translate(470,130)">
    <ellipse cx="-12" cy="0" rx="20" ry="22" fill="#E8F5E9" stroke="#4CAF50" stroke-width="2"/>
    <ellipse cx="12" cy="0" rx="20" ry="22" fill="#E8F5E9" stroke="#4CAF50" stroke-width="2"/>
    <ellipse cx="-12" cy="0" rx="7" ry="5" fill="#C8E6C9" stroke="#388E3C" stroke-width="1"/>
    <ellipse cx="12" cy="0" rx="7" ry="5" fill="#C8E6C9" stroke="#388E3C" stroke-width="1"/>
    <text x="0" y="36" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Телофаза</text>
  </g>
  <!-- Growth phases below -->
  <g transform="translate(100,220)">
    <!-- Small cell -->
    <circle cx="0" cy="0" r="12" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="4" fill="#81C784"/>
    <path d="M15 0 L40 0" stroke="#2E7D32" stroke-width="1.5"/>
    <path d="M40 0 L36 -4 M40 0 L36 4" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
    <!-- Medium cell -->
    <circle cx="70" cy="0" r="20" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1.5"/>
    <ellipse cx="70" cy="0" rx="8" ry="6" fill="#A5D6A7" stroke="#388E3C" stroke-width="1"/>
    <path d="M95 0 L120 0" stroke="#2E7D32" stroke-width="1.5"/>
    <path d="M120 0 L116 -4 M120 0 L116 4" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
    <!-- Large cell -->
    <circle cx="155" cy="0" r="28" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1.5"/>
    <ellipse cx="155" cy="0" rx="10" ry="8" fill="#A5D6A7" stroke="#388E3C" stroke-width="1"/>
    <!-- Vacuole -->
    <circle cx="160" cy="5" r="8" fill="#E1F5FE" stroke="#42A5F5" stroke-width="0.8" opacity="0.6"/>
  </g>
  <text x="250" y="260" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Рост клетки: деление -> увеличение объёма</text>
  <!-- Summary -->
  <rect x="50" y="275" width="400" height="35" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="292" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Жизненный цикл клетки: интерфаза (подготовка) -> митоз (деление)</text>
  <text x="250" y="304" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">В результате из 1 материнской клетки образуются 2 дочерние</text>
'''

# ===== LESSON 6: Строение и жизнедеятельность бактерий =====
l6 = '''
  <!-- Bacterial cell detailed structure -->
  <g transform="translate(200,190)">
    <!-- Outer capsule -->
    <ellipse cx="0" cy="0" rx="75" ry="45" fill="none" stroke="#FFCC80" stroke-width="2" stroke-dasharray="4,3"/>
    <!-- Cell wall -->
    <ellipse cx="0" cy="0" rx="68" ry="40" fill="#FFE0B2" stroke="#E65100" stroke-width="2.5"/>
    <!-- Cell membrane -->
    <ellipse cx="0" cy="0" rx="62" ry="35" fill="#FFF3E0" stroke="#E65100" stroke-width="1" stroke-dasharray="3,2"/>
    <!-- Nucleoid (circular DNA) -->
    <path d="M-20 -8 Q-25 -20 -10 -22 Q5 -24 10 -12 Q15 0 5 8 Q-5 15 -15 10 Q-25 5 -20 -8 Z" fill="none" stroke="#E65100" stroke-width="2"/>
    <!-- Plasmids -->
    <circle cx="30" cy="-12" r="8" fill="none" stroke="#D84315" stroke-width="1.5"/>
    <circle cx="-30" cy="15" r="6" fill="none" stroke="#D84315" stroke-width="1.2"/>
    <!-- Ribosomes -->
    <circle cx="-15" cy="-15" r="3" fill="#FF8A65"/>
    <circle cx="10" cy="10" r="3" fill="#FF8A65"/>
    <circle cx="25" cy="5" r="3" fill="#FF8A65"/>
    <circle cx="-25" cy="-5" r="3" fill="#FF8A65"/>
    <circle cx="15" cy="-8" r="2.5" fill="#FF8A65"/>
    <circle cx="-10" cy="15" r="2.5" fill="#FF8A65"/>
    <circle cx="0" cy="-15" r="2.5" fill="#FF8A65"/>
    <circle cx="35" cy="8" r="2.5" fill="#FF8A65"/>
    <!-- Flagellum -->
    <path d="M68 0 Q80 -8 88 0 Q96 8 104 0 Q112 -8 120 0" stroke="#E65100" stroke-width="2" fill="none"/>
    <!-- Pilli -->
    <line x1="-50" y1="30" x2="-60" y2="42" stroke="#E65100" stroke-width="1"/>
    <line x1="-40" y1="35" x2="-48" y2="48" stroke="#E65100" stroke-width="1"/>
    <line x1="-30" y1="38" x2="-35" y2="50" stroke="#E65100" stroke-width="1"/>
  </g>
  <!-- Labels -->
  <text x="350" y="95" font-family="Arial,sans-serif" font-size="8" fill="#333" font-weight="bold">Капсула</text>
  <line x1="348" y1="97" x2="275" y2="148" stroke="#333" stroke-width="0.5"/>
  <text x="400" y="130" font-family="Arial,sans-serif" font-size="8" fill="#333" font-weight="bold">Клеточная стенка</text>
  <line x1="398" y1="132" x2="268" y2="162" stroke="#333" stroke-width="0.5"/>
  <text x="400" y="160" font-family="Arial,sans-serif" font-size="8" fill="#333" font-weight="bold">Цитоплазма</text>
  <line x1="398" y1="162" x2="240" y2="185" stroke="#333" stroke-width="0.5"/>
  <text x="80" y="120" font-family="Arial,sans-serif" font-size="8" fill="#333" font-weight="bold">Нуклеоид (ДНК)</text>
  <line x1="140" y1="122" x2="190" y2="175" stroke="#333" stroke-width="0.5"/>
  <text x="80" y="150" font-family="Arial,sans-serif" font-size="8" fill="#333" font-weight="bold">Плазмида</text>
  <line x1="130" y1="152" x2="170" y2="200" stroke="#333" stroke-width="0.5"/>
  <text x="340" y="200" font-family="Arial,sans-serif" font-size="8" fill="#333" font-weight="bold">Жгутик</text>
  <line x1="338" y1="202" x2="280" y2="195" stroke="#333" stroke-width="0.5"/>
  <text x="80" y="250" font-family="Arial,sans-serif" font-size="8" fill="#333" font-weight="bold">Рибосомы</text>
  <line x1="120" y1="248" x2="180" y2="210" stroke="#333" stroke-width="0.5"/>
  <text x="80" y="275" font-family="Arial,sans-serif" font-size="8" fill="#333" font-weight="bold">Пили (ворсинки)</text>
  <line x1="140" y1="273" x2="155" y2="235" stroke="#333" stroke-width="0.5"/>
  <!-- Info box -->
  <rect x="300" y="250" width="175" height="55" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="387" y="267" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Особенности бактерий</text>
  <text x="310" y="281" font-family="Arial,sans-serif" font-size="7" fill="#555">- Нет ядра (прокариоты)</text>
  <text x="310" y="293" font-family="Arial,sans-serif" font-size="7" fill="#555">- Кольцевая ДНК (нуклеоид)</text>
  <text x="310" y="305" font-family="Arial,sans-serif" font-size="7" fill="#555">- Размножение делением надвое</text>
'''

# ===== LESSON 7: Роль бактерий в природе и жизни человека =====
l7 = '''
  <!-- Split: Positive/Negative -->
  <!-- Positive side -->
  <rect x="20" y="60" width="225" height="245" rx="8" fill="#E8F5E9" stroke="#4CAF50" stroke-width="1.5"/>
  <text x="132" y="82" font-family="Arial,sans-serif" font-size="11" fill="#2E7D32" text-anchor="middle" font-weight="bold">Положительная роль</text>
  <!-- Nitrogen fixation -->
  <g transform="translate(70,120)">
    <circle cx="0" cy="0" r="22" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1.5"/>
    <text x="0" y="-3" font-family="Arial,sans-serif" font-size="12" fill="#2E7D32" text-anchor="middle" font-weight="bold">N</text>
    <text x="0" y="10" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">2</text>
    <path d="M0 22 L0 32" stroke="#4CAF50" stroke-width="1.5"/><path d="M0 32 L-3 28 M0 32 L3 28" stroke="#4CAF50" stroke-width="1"/>
    <text x="0" y="45" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Азотфиксация</text>
  </g>
  <!-- Decomposition -->
  <g transform="translate(185,120)">
    <path d="M-15 8 L-10 -5 L0 -8 L10 -5 L15 8" stroke="#795548" stroke-width="2" fill="none"/>
    <circle cx="0" cy="-15" r="4" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
    <circle cx="-10" cy="-12" r="3" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
    <text x="0" y="28" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Разложение</text>
    <text x="0" y="38" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">органики</text>
  </g>
  <!-- Fermentation -->
  <g transform="translate(70,210)">
    <rect x="-18" y="-12" width="36" height="24" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5" rx="4"/>
    <text x="0" y="3" font-family="Arial,sans-serif" font-size="10" fill="#F57F17" text-anchor="middle">kefir</text>
    <text x="0" y="28" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Кисломолочные</text>
  </g>
  <!-- Medicine -->
  <g transform="translate(185,210)">
    <rect x="-15" y="-15" width="30" height="30" fill="white" stroke="#E53935" stroke-width="1.5" rx="3"/>
    <line x1="0" y1="-15" x2="0" y2="15" stroke="#E53935" stroke-width="1.5"/>
    <line x1="-15" y1="0" x2="15" y2="0" stroke="#E53935" stroke-width="1.5"/>
    <text x="0" y="30" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Антибиотики</text>
  </g>
  <!-- Negative side -->
  <rect x="255" y="60" width="225" height="245" rx="8" fill="#FFEBEE" stroke="#E53935" stroke-width="1.5"/>
  <text x="367" y="82" font-family="Arial,sans-serif" font-size="11" fill="#C62828" text-anchor="middle" font-weight="bold">Отрицательная роль</text>
  <!-- Diseases -->
  <g transform="translate(310,120)">
    <circle cx="0" cy="0" r="22" fill="#FFCDD2" stroke="#E53935" stroke-width="1.5"/>
    <path d="M-8 -8 L8 8 M8 -8 L-8 8" stroke="#E53935" stroke-width="2.5"/>
    <text x="0" y="35" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Инфекции</text>
    <text x="0" y="45" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">холера, туберкулёз</text>
  </g>
  <!-- Food spoilage -->
  <g transform="translate(420,120)">
    <rect x="-18" y="-12" width="36" height="24" fill="#FFF3E0" stroke="#FF9800" stroke-width="1.5" rx="3"/>
    <circle cx="-5" cy="-3" r="5" fill="#8BC34A" opacity="0.6"/>
    <circle cx="8" cy="3" r="4" fill="#8BC34A" opacity="0.5"/>
    <circle cx="3" cy="8" r="3" fill="#8BC34A" opacity="0.4"/>
    <text x="0" y="28" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Порча продуктов</text>
  </g>
  <!-- Bioweapons -->
  <g transform="translate(310,210)">
    <path d="M-12 -12 L12 -12 L12 12 L-12 12 Z" fill="#FFCDD2" stroke="#E53935" stroke-width="1"/>
    <text x="0" y="3" font-family="Arial,sans-serif" font-size="14" fill="#E53935" text-anchor="middle" font-weight="bold">!</text>
    <text x="0" y="28" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Опасные</text>
    <text x="0" y="38" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">заболевания</text>
  </g>
  <!-- Decay -->
  <g transform="translate(420,210)">
    <rect x="-18" y="-12" width="36" height="24" fill="#FFCDD2" stroke="#E53935" stroke-width="1" rx="3"/>
    <path d="M-8 0 L-3 -8 L3 0 L8 -8" stroke="#E53935" stroke-width="1.5" fill="none"/>
    <text x="0" y="28" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Гниение</text>
  </g>
'''

# ===== LESSON 8: Общая характеристика грибов =====
l8 = '''
  <!-- Mushroom structure + hyphae -->
  <g transform="translate(140,185)">
    <!-- Cap -->
    <path d="M-45 0 Q-50 -30 -25 -40 Q0 -48 25 -40 Q50 -30 45 0 Z" fill="#8D6E63" stroke="#5D4037" stroke-width="2"/>
    <!-- Spots -->
    <circle cx="-15" cy="-18" r="5" fill="#A1887F" opacity="0.5"/>
    <circle cx="12" cy="-24" r="4" fill="#A1887F" opacity="0.4"/>
    <circle cx="0" cy="-10" r="3.5" fill="#A1887F" opacity="0.4"/>
    <!-- Gills -->
    <path d="M-38 2 Q-30 10 -15 14" stroke="#BCAAA4" stroke-width="0.8" fill="none"/>
    <path d="M-28 2 Q-20 10 -5 14" stroke="#BCAAA4" stroke-width="0.8" fill="none"/>
    <path d="M-15 2 Q-8 10 5 14" stroke="#BCAAA4" stroke-width="0.8" fill="none"/>
    <path d="M0 2 Q8 10 15 14" stroke="#BCAAA4" stroke-width="0.8" fill="none"/>
    <path d="M15 2 Q22 10 28 12" stroke="#BCAAA4" stroke-width="0.8" fill="none"/>
    <path d="M28 2 Q32 10 38 12" stroke="#BCAAA4" stroke-width="0.8" fill="none"/>
    <!-- Stipe -->
    <rect x="-8" y="14" width="16" height="55" fill="#D7CCC8" stroke="#BCAAA4" stroke-width="1.5" rx="5"/>
    <!-- Volva -->
    <path d="M-15 65 Q-20 72 -12 75 Q0 78 12 75 Q20 72 15 65" fill="#EFEBE9" stroke="#BCAAA4" stroke-width="1"/>
    <!-- Ring -->
    <ellipse cx="0" cy="30" rx="13" ry="4" fill="#FFECB3" stroke="#D7CCC8" stroke-width="1"/>
    <!-- Mycelium -->
    <path d="M-8 69 Q-20 82 -30 85" stroke="#BCAAA4" stroke-width="2" fill="none"/>
    <path d="M8 69 Q20 82 30 85" stroke="#BCAAA4" stroke-width="2" fill="none"/>
    <path d="M0 69 Q-8 85 -15 90" stroke="#BCAAA4" stroke-width="1.5" fill="none"/>
    <path d="M0 69 Q8 85 15 90" stroke="#BCAAA4" stroke-width="1.5" fill="none"/>
  </g>
  <!-- Labels -->
  <line x1="185" y1="155" x2="280" y2="85" stroke="#333" stroke-width="0.7"/>
  <text x="285" y="88" font-family="Arial,sans-serif" font-size="9" fill="#333" font-weight="bold">Шляпка</text>
  <line x1="148" y1="195" x2="280" y2="120" stroke="#333" stroke-width="0.7"/>
  <text x="285" y="123" font-family="Arial,sans-serif" font-size="9" fill="#333" font-weight="bold">Пластинки</text>
  <line x1="148" y1="215" x2="280" y2="155" stroke="#333" stroke-width="0.7"/>
  <text x="285" y="158" font-family="Arial,sans-serif" font-size="9" fill="#333" font-weight="bold">Кольцо</text>
  <line x1="148" y1="235" x2="280" y2="190" stroke="#333" stroke-width="0.7"/>
  <text x="285" y="193" font-family="Arial,sans-serif" font-size="9" fill="#333" font-weight="bold">Ножка</text>
  <line x1="125" y1="265" x2="280" y2="225" stroke="#333" stroke-width="0.7"/>
  <text x="285" y="228" font-family="Arial,sans-serif" font-size="9" fill="#333" font-weight="bold">Грибница (мицелий)</text>
  <line x1="140" y1="260" x2="280" y2="260" stroke="#333" stroke-width="0.7"/>
  <text x="285" y="263" font-family="Arial,sans-serif" font-size="9" fill="#333" font-weight="bold">Вольва</text>
  <!-- Hyphae detail -->
  <g transform="translate(400,130)">
    <path d="M-25 0 Q-15 -10 -5 0 Q5 10 15 0" stroke="#BCAAA4" stroke-width="4" fill="none"/>
    <path d="M-25 0 Q-15 -10 -5 0 Q5 10 15 0" stroke="#D7CCC8" stroke-width="2" fill="none"/>
    <line x1="-5" y1="-5" x2="-5" y2="5" stroke="#A1887F" stroke-width="1"/>
    <text x="-5" y="22" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Гифы с перегородками</text>
  </g>
  <!-- Characteristics -->
  <rect x="290" y="280" width="185" height="35" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="382" y="295" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Грибы - гетеротрофы, хитин в стенке</text>
  <text x="382" y="308" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Запасное вещество - гликоген</text>
'''

# Generate all SVGs
OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade6/biology"
import os
os.makedirs(OUTPUT_DIR, exist_ok=True)

lessons = [
    (1, "Биология - наука о живой природе", l1),
    (2, "Признаки живого и уровни организации", l2),
    (3, "Устройство увеличительных приборов. Клетка", l3),
    (4, "Химический состав клетки", l4),
    (5, "Жизнедеятельность клетки: деление и рост", l5),
    (6, "Строение и жизнедеятельность бактерий", l6),
    (7, "Роль бактерий в природе и жизни человека", l7),
    (8, "Общая характеристика грибов", l8),
]

for num, title, illustration in lessons:
    svg_content = W(illustration, title, f"Биология 6 класс - Урок {num}")
    filepath = os.path.join(OUTPUT_DIR, f"lesson{num}.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Generated: lesson{num}.svg")

print("Done! 8 SVGs for Grade 6 Biology Lessons 1-8.")
