#!/usr/bin/env python3
"""Grade 6 Biology, Lessons 25-32: Flower to Communities"""
import os
D = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade6/biology"
os.makedirs(D, exist_ok=True)

def W(inner, title, sub, c="#2E7D32"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350"><defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#E8F5E9"/><stop offset="100%" stop-color="#C8E6C9"/></linearGradient></defs><rect width="500" height="350" fill="url(#bg)" rx="10"/><rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="{c}" stroke-width="2.5"/><text x="250" y="30" font-family="Arial,sans-serif" font-size="16" font-weight="bold" fill="{c}" text-anchor="middle">{title}</text><text x="250" y="46" font-family="Arial,sans-serif" font-size="10" fill="#888" text-anchor="middle">{sub}</text><line x1="30" y1="52" x2="470" y2="52" stroke="{c}" stroke-width="1.5" opacity="0.25"/>{inner}<rect x="10" y="325" width="480" height="20" rx="4" fill="{c}" opacity="0.85"/><text x="250" y="339" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="white" font-weight="bold">Биология 6 класс</text></svg>'

# 25: Цветок — орган семенного размножения
l25 = W('''
  <!-- Detailed flower diagram -->
  <g transform="translate(180,190)">
    <!-- Peduncle -->
    <rect x="-3" y="50" width="6" height="40" fill="#795548" rx="2"/>
    <!-- Receptacle -->
    <ellipse cx="0" cy="48" rx="12" ry="5" fill="#A5D6A7" stroke="#4CAF50" stroke-width="1"/>
    <!-- Sepals -->
    <path d="M-12 45 Q-25 30 -20 20 Q-15 25 -5 40 Z" fill="#66BB6A" stroke="#4CAF50" stroke-width="1"/>
    <path d="M12 45 Q25 30 20 20 Q15 25 5 40 Z" fill="#66BB6A" stroke="#4CAF50" stroke-width="1"/>
    <path d="M0 45 Q0 25 0 18 Q5 28 5 42 Z" fill="#81C784" stroke="#4CAF50" stroke-width="0.8"/>
    <!-- Petals -->
    <ellipse cx="0" cy="-25" rx="15" ry="30" fill="#E91E63" opacity="0.7" stroke="#C2185B" stroke-width="1"/>
    <ellipse cx="28" cy="-8" rx="15" ry="30" fill="#E91E63" opacity="0.7" stroke="#C2185B" stroke-width="1" transform="rotate(72,0,0)"/>
    <ellipse cx="17" cy="22" rx="15" ry="30" fill="#E91E63" opacity="0.7" stroke="#C2185B" stroke-width="1" transform="rotate(144,0,0)"/>
    <ellipse cx="-17" cy="22" rx="15" ry="30" fill="#E91E63" opacity="0.7" stroke="#C2185B" stroke-width="1" transform="rotate(216,0,0)"/>
    <ellipse cx="-28" cy="-8" rx="15" ry="30" fill="#E91E63" opacity="0.7" stroke="#C2185B" stroke-width="1" transform="rotate(288,0,0)"/>
    <!-- Stamens (filament + anther) -->
    <line x1="-8" y1="-5" x2="-12" y2="-25" stroke="#FF9800" stroke-width="1.5"/>
    <ellipse cx="-12" cy="-28" rx="3" ry="5" fill="#FFC107" stroke="#FF9800" stroke-width="1"/>
    <line x1="8" y1="-5" x2="12" y2="-25" stroke="#FF9800" stroke-width="1.5"/>
    <ellipse cx="12" cy="-28" rx="3" ry="5" fill="#FFC107" stroke="#FF9800" stroke-width="1"/>
    <line x1="0" y1="-2" x2="0" y2="-22" stroke="#FF9800" stroke-width="1.5"/>
    <ellipse cx="0" cy="-25" rx="3" ry="5" fill="#FFC107" stroke="#FF9800" stroke-width="1"/>
    <!-- Pistil (stigma + style + ovary) -->
    <line x1="0" y1="10" x2="0" y2="-18" stroke="#4CAF50" stroke-width="2"/>
    <path d="M-4 -18 Q0 -24 4 -18" stroke="#4CAF50" stroke-width="2" fill="#81C784"/>
    <!-- Ovary -->
    <ellipse cx="0" cy="15" rx="8" ry="10" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1.5"/>
    <!-- Ovules inside -->
    <circle cx="-3" cy="15" r="2" fill="#81C784"/>
    <circle cx="3" cy="15" r="2" fill="#81C784"/>
  </g>
  <!-- Labels -->
  <g transform="translate(350,70)">
    <rect x="-60" y="-10" width="170" height="215" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
    <text x="25" y="6" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Строение цветка</text>
    <line x1="-55" y1="12" x2="105" y2="12" stroke="#ddd" stroke-width="0.5"/>
    <circle cx="-42" cy="28" r="4" fill="#E91E63" opacity="0.7"/><text x="-32" y="32" font-family="Arial,sans-serif" font-size="8" fill="#333">Лепесток (венчик)</text>
    <circle cx="-42" cy="48" r="4" fill="#66BB6A"/><text x="-32" y="52" font-family="Arial,sans-serif" font-size="8" fill="#333">Чашелистик (чашечка)</text>
    <circle cx="-42" cy="68" r="4" fill="#FFC107"/><text x="-32" y="72" font-family="Arial,sans-serif" font-size="8" fill="#333">Тычинка (андроцей)</text>
    <circle cx="-42" cy="88" r="4" fill="#4CAF50"/><text x="-32" y="92" font-family="Arial,sans-serif" font-size="8" fill="#333">Пестик (гинецей)</text>
    <circle cx="-42" cy="108" r="4" fill="#81C784"/><text x="-32" y="112" font-family="Arial,sans-serif" font-size="8" fill="#333">Рыльце пестика</text>
    <circle cx="-42" cy="128" r="4" fill="#795548"/><text x="-32" y="132" font-family="Arial,sans-serif" font-size="8" fill="#333">Цветоложе</text>
    <text x="25" y="155" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Тычинка = нить + пыльник</text>
    <text x="25" y="168" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Пестик = рыльце + столбик</text>
    <text x="25" y="181" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">+ завязь (семяпочки)</text>
    <text x="25" y="198" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Обоеполые и раздельнополые</text>
  </g>
''', "Цветок - орган семенного размножения", "Биология 6 класс - Урок 25")

# 26: Плод и семя
l26 = W('''
  <!-- Fruit types -->
  <!-- Bean pod (dry) -->
  <g transform="translate(70,120)">
    <rect x="-25" y="-6" width="50" height="12" fill="#8BC34A" stroke="#689F38" stroke-width="1.5" rx="5"/>
    <!-- Seeds inside -->
    <circle cx="-12" cy="0" r="4" fill="#A5D6A7" stroke="#689F38" stroke-width="0.8"/>
    <circle cx="0" cy="0" r="4" fill="#A5D6A7" stroke="#689F38" stroke-width="0.8"/>
    <circle cx="12" cy="0" r="4" fill="#A5D6A7" stroke="#689F38" stroke-width="0.8"/>
    <!-- Open pod -->
    <path d="M-25 -6 Q-15 -15 -10 -8" stroke="#689F38" stroke-width="1" fill="#C8E6C9" opacity="0.5"/>
    <path d="M-25 6 Q-15 15 -10 8" stroke="#689F38" stroke-width="1" fill="#C8E6C9" opacity="0.5"/>
    <text x="0" y="25" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Боб (сухой)</text>
  </g>
  <!-- Apple (fleshy) -->
  <g transform="translate(190,120)">
    <circle cx="0" cy="0" r="22" fill="#E53935" stroke="#C62828" stroke-width="1.5"/>
    <path d="M-3 -22 Q0 -28 3 -22" fill="#795548" stroke="#5D4037" stroke-width="1"/>
    <!-- Cross-section hint -->
    <circle cx="0" cy="0" r="8" fill="#FFCDD2" opacity="0.5"/>
    <!-- Seeds visible -->
    <ellipse cx="-3" cy="2" rx="2" ry="4" fill="#5D4037"/>
    <ellipse cx="3" cy="2" rx="2" ry="4" fill="#5D4037"/>
    <text x="0" y="35" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Яблоко (сочный)</text>
  </g>
  <!-- Nut -->
  <g transform="translate(310,120)">
    <circle cx="0" cy="0" r="16" fill="#8D6E63" stroke="#5D4037" stroke-width="1.5"/>
    <path d="M-12 -8 Q0 -15 12 -8" fill="#A1887F" stroke="#5D4037" stroke-width="1"/>
    <text x="0" y="30" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Орех (сухой)</text>
  </g>
  <!-- Drupe (peach) -->
  <g transform="translate(430,120)">
    <circle cx="0" cy="0" r="20" fill="#FF8A65" stroke="#E64A19" stroke-width="1.5"/>
    <path d="M-2 -20 Q0 -25 2 -20" fill="#795548" stroke="#5D4037" stroke-width="1"/>
    <!-- Stone inside -->
    <ellipse cx="0" cy="2" rx="8" ry="10" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
    <text x="0" y="35" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Костянка (персик)</text>
  </g>
  <!-- Seed structure -->
  <g transform="translate(150,260)">
    <!-- Bean seed cross-section -->
    <ellipse cx="0" cy="0" rx="35" ry="22" fill="#FFF9C4" stroke="#F9A825" stroke-width="2"/>
    <!-- Seed coat -->
    <ellipse cx="0" cy="0" rx="35" ry="22" fill="none" stroke="#F57F17" stroke-width="1" stroke-dasharray="3,2"/>
    <!-- Two cotyledons -->
    <path d="M0 -18 L0 18" stroke="#F9A825" stroke-width="1"/>
    <ellipse cx="-12" cy="0" rx="15" ry="16" fill="#FFE082" stroke="#F9A825" stroke-width="0.8"/>
    <ellipse cx="12" cy="0" rx="15" ry="16" fill="#FFE082" stroke="#F9A825" stroke-width="0.8"/>
    <!-- Embryo -->
    <ellipse cx="14" cy="-6" rx="4" ry="8" fill="#81C784" stroke="#4CAF50" stroke-width="0.8"/>
    <!-- Radicle -->
    <path d="M14 2 Q18 10 15 14" stroke="#4CAF50" stroke-width="1.5" fill="none"/>
  </g>
  <!-- Seed labels -->
  <text x="150" y="235" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Строение семени</text>
  <g transform="translate(330,235)">
    <rect x="-80" y="-15" width="170" height="80" rx="4" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
    <text x="5" y="0" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Части семени</text>
    <text x="-70" y="15" font-family="Arial,sans-serif" font-size="7" fill="#555">- Семенная кожура (защита)</text>
    <text x="-70" y="27" font-family="Arial,sans-serif" font-size="7" fill="#555">- Семядоли (запас питательных)</text>
    <text x="-70" y="39" font-family="Arial,sans-serif" font-size="7" fill="#555">- Зародыш: корешок, стебелёк</text>
    <text x="-70" y="51" font-family="Arial,sans-serif" font-size="7" fill="#555">- Эндосперм (у однодольных)</text>
    <text x="-70" y="63" font-family="Arial,sans-serif" font-size="7" fill="#C62828">Двудольные: 2 семядоли</text>
  </g>
''', "Плод и семя", "Биология 6 класс - Урок 26")

# 27: Минеральное питание и водный обмен растений
l27 = W('''
  <!-- Water and mineral uptake diagram -->
  <g transform="translate(130,180)">
    <!-- Soil -->
    <rect x="-80" y="30" width="160" height="50" fill="#D7CCC8" stroke="#BCAAA4" stroke-width="1" rx="3"/>
    <!-- Water drops in soil -->
    <circle cx="-40" cy="45" r="4" fill="#42A5F5" opacity="0.5"/>
    <circle cx="0" cy="50" r="3" fill="#42A5F5" opacity="0.5"/>
    <circle cx="30" cy="42" r="4" fill="#42A5F5" opacity="0.5"/>
    <circle cx="50" cy="55" r="3" fill="#42A5F5" opacity="0.5"/>
    <!-- Mineral ions -->
    <text x="-55" y="60" font-family="Arial,sans-serif" font-size="6" fill="#E65100">N</text>
    <text x="-20" y="68" font-family="Arial,sans-serif" font-size="6" fill="#E65100">P</text>
    <text x="40" y="65" font-family="Arial,sans-serif" font-size="6" fill="#E65100">K</text>
    <!-- Roots -->
    <path d="M0 30 L0 -10" stroke="#795548" stroke-width="3"/>
    <path d="M0 10 Q-30 20 -45 30" stroke="#795548" stroke-width="2" fill="none"/>
    <path d="M0 15 Q25 22 40 30" stroke="#795548" stroke-width="2" fill="none"/>
    <path d="M0 5 Q-15 15 -25 30" stroke="#795548" stroke-width="1.5" fill="none"/>
    <!-- Root hairs -->
    <line x1="-30" y1="22" x2="-35" y2="18" stroke="#A1887F" stroke-width="0.5"/>
    <line x1="-20" y1="18" x2="-25" y2="14" stroke="#A1887F" stroke-width="0.5"/>
    <line x1="25" y1="22" x2="30" y2="18" stroke="#A1887F" stroke-width="0.5"/>
    <!-- Stem -->
    <rect x="-3" y="-60" width="6" height="50" fill="#795548" rx="2"/>
    <!-- Leaves -->
    <ellipse cx="-18" cy="-45" rx="15" ry="7" fill="#81C784" stroke="#4CAF50" stroke-width="1" transform="rotate(30,-18,-45)"/>
    <ellipse cx="18" cy="-45" rx="15" ry="7" fill="#81C784" stroke="#4CAF50" stroke-width="1" transform="rotate(-30,18,-45)"/>
    <ellipse cx="-18" cy="-25" rx="15" ry="7" fill="#81C784" stroke="#4CAF50" stroke-width="1" transform="rotate(30,-18,-25)"/>
    <ellipse cx="18" cy="-25" rx="15" ry="7" fill="#81C784" stroke="#4CAF50" stroke-width="1" transform="rotate(-30,18,-25)"/>
    <!-- Upward arrows (xylem) -->
    <path d="M-2 25 L-2 -10" stroke="#42A5F5" stroke-width="2"/>
    <path d="M-2 -10 L-5 -5 M-2 -10 L1 -5" stroke="#42A5F5" stroke-width="1.5" fill="none"/>
  </g>
  <!-- Water path labels -->
  <text x="130" y="105" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" text-anchor="middle" font-weight="bold">Восходящий ток</text>
  <text x="130" y="117" font-family="Arial,sans-serif" font-size="7" fill="#42A5F5" text-anchor="middle">вода + минералы (ксилема)</text>
  <!-- Right side: process diagram -->
  <g transform="translate(370,150)">
    <rect x="-100" y="-70" width="200" height="185" rx="6" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
    <text x="0" y="-52" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Путь воды</text>
    <!-- Steps -->
    <rect x="-80" y="-40" width="160" height="18" rx="3" fill="#E3F2FD"/>
    <text x="0" y="-27" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle">1. Всасывание корневыми волосками</text>
    <rect x="-80" y="-15" width="160" height="18" rx="3" fill="#E8F5E9"/>
    <text x="0" y="-2" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">2. Движение по ксилеме вверх</text>
    <rect x="-80" y="10" width="160" height="18" rx="3" fill="#FFF3E0"/>
    <text x="0" y="23" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle">3. Поступление в листья</text>
    <rect x="-80" y="35" width="160" height="18" rx="3" fill="#FCE4EC"/>
    <text x="0" y="48" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle">4. Испарение через устьица</text>
    <text x="0" y="72" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Корневое давление + испарение</text>
    <text x="0" y="84" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">= движение воды вверх</text>
    <!-- Minerals -->
    <text x="0" y="105" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">Минеральные вещества: N, P, K</text>
  </g>
''', "Минеральное питание и водный обмен растений", "Биология 6 класс - Урок 27")

# 28: Фотосинтез и дыхание растений
l28 = W('''
  <!-- Photosynthesis equation diagram -->
  <g transform="translate(250,140)">
    <!-- Sun -->
    <circle cx="-180" cy="-60" r="25" fill="#FFF176" stroke="#FDD835" stroke-width="2"/>
    <line x1="-180" y1="-90" x2="-180" y2="-98" stroke="#FDD835" stroke-width="2"/>
    <line x1="-210" y1="-75" x2="-216" y2="-80" stroke="#FDD835" stroke-width="2"/>
    <line x1="-155" y1="-75" x2="-148" y2="-80" stroke="#FDD835" stroke-width="2"/>
    <line x1="-200" y1="-50" x2="-208" y2="-46" stroke="#FDD835" stroke-width="2"/>
    <!-- Light arrow to leaf -->
    <path d="M-155 -50 Q-120 -20 -90 0" stroke="#FDD835" stroke-width="2" fill="none"/>
    <!-- Leaf (large) -->
    <path d="M-60 -40 Q-30 -55 0 -45 Q30 -30 35 0 Q30 25 0 35 Q-30 30 -60 10 Q-65 -15 -60 -40 Z" fill="#81C784" stroke="#4CAF50" stroke-width="2"/>
    <line x1="-60" y1="-10" x2="30" y2="-5" stroke="#388E3C" stroke-width="1.5"/>
    <!-- CO2 arrow in -->
    <path d="M-100 30 Q-80 20 -60 15" stroke="#795548" stroke-width="2" fill="none"/>
    <text x="-115" y="25" font-family="Arial,sans-serif" font-size="9" fill="#5D4037" font-weight="bold">CO2</text>
    <!-- H2O arrow in -->
    <path d="M-70 55 Q-50 40 -30 30" stroke="#42A5F5" stroke-width="2" fill="none"/>
    <text x="-85" y="60" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold">H2O</text>
    <!-- O2 arrow out -->
    <path d="M30 -30 Q60 -45 80 -50" stroke="#4CAF50" stroke-width="2" fill="none"/>
    <text x="85" y="-48" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold">O2</text>
    <!-- Glucose arrow out -->
    <path d="M30 20 Q60 30 80 35" stroke="#FF9800" stroke-width="2" fill="none"/>
    <text x="85" y="33" font-family="Arial,sans-serif" font-size="9" fill="#E65100" font-weight="bold">C6H12O6</text>
    <!-- Chloroplast in leaf -->
    <ellipse cx="-15" cy="-5" rx="15" ry="8" fill="#4CAF50" opacity="0.4" stroke="#2E7D32" stroke-width="1"/>
    <rect x="-22" y="-8" width="2" height="6" fill="#2E7D32" rx="0.5"/>
    <rect x="-16" y="-9" width="2" height="8" fill="#2E7D32" rx="0.5"/>
    <rect x="-10" y="-7" width="2" height="5" fill="#2E7D32" rx="0.5"/>
  </g>
  <!-- Comparison: Photosynthesis vs Respiration -->
  <rect x="20" y="220" width="220" height="90" rx="5" fill="#E8F5E9" stroke="#4CAF50" stroke-width="1"/>
  <text x="130" y="238" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Фотосинтез (на свету)</text>
  <text x="30" y="255" font-family="Arial,sans-serif" font-size="7" fill="#555">CO2 + H2O -> C6H12O6 + O2</text>
  <text x="30" y="268" font-family="Arial,sans-serif" font-size="7" fill="#555">Идёт в хлоропластах</text>
  <text x="30" y="281" font-family="Arial,sans-serif" font-size="7" fill="#555">Поглощает CO2, выделяет O2</text>
  <text x="30" y="294" font-family="Arial,sans-serif" font-size="7" fill="#555">Накапливает энергию</text>
  <rect x="260" y="220" width="220" height="90" rx="5" fill="#FFF3E0" stroke="#FF9800" stroke-width="1"/>
  <text x="370" y="238" font-family="Arial,sans-serif" font-size="9" fill="#E65100" text-anchor="middle" font-weight="bold">Дыхание (постоянно)</text>
  <text x="270" y="255" font-family="Arial,sans-serif" font-size="7" fill="#555">C6H12O6 + O2 -> CO2 + H2O</text>
  <text x="270" y="268" font-family="Arial,sans-serif" font-size="7" fill="#555">Идёт в митохондриях</text>
  <text x="270" y="281" font-family="Arial,sans-serif" font-size="7" fill="#555">Поглощает O2, выделяет CO2</text>
  <text x="270" y="294" font-family="Arial,sans-serif" font-size="7" fill="#555">Освобождает энергию</text>
''', "Фотосинтез и дыхание растений", "Биология 6 класс - Урок 28")

# 29: Рост и развитие растений
l29 = W('''
  <!-- Seed germination stages -->
  <g transform="translate(60,150)">
    <!-- Stage 1: Dry seed -->
    <ellipse cx="0" cy="0" rx="15" ry="10" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/>
    <text x="0" y="25" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Семя</text>
  </g>
  <path d="M80 150 L110 150" stroke="#2E7D32" stroke-width="1.5"/>
  <path d="M110 150 L106 146 M110 150 L106 154" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
  <g transform="translate(140,150)">
    <!-- Stage 2: Root emerges -->
    <ellipse cx="0" cy="-5" rx="15" ry="10" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/>
    <path d="M0 5 L0 25" stroke="#795548" stroke-width="2.5" stroke-linecap="round"/>
    <text x="0" y="42" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Корешок</text>
  </g>
  <path d="M165 150 L195 150" stroke="#2E7D32" stroke-width="1.5"/>
  <path d="M195 150 L191 146 M195 150 L191 154" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
  <g transform="translate(225,150)">
    <!-- Stage 3: Sprout -->
    <path d="M0 15 L0 30" stroke="#795548" stroke-width="2.5" stroke-linecap="round"/>
    <ellipse cx="0" cy="5" rx="12" ry="8" fill="#FFE082" stroke="#F9A825" stroke-width="1"/>
    <path d="M0 -5 L0 -20" stroke="#66BB6A" stroke-width="2"/>
    <ellipse cx="-5" cy="-22" rx="6" ry="4" fill="#81C784" stroke="#4CAF50" stroke-width="0.8"/>
    <text x="0" y="48" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Росток</text>
  </g>
  <path d="M250 150 L280 150" stroke="#2E7D32" stroke-width="1.5"/>
  <path d="M280 150 L276 146 M280 150 L276 154" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
  <g transform="translate(315,145)">
    <!-- Stage 4: Seedling -->
    <path d="M0 20 L0 50" stroke="#795548" stroke-width="2"/>
    <ellipse cx="-10" cy="10" rx="10" ry="5" fill="#81C784" stroke="#4CAF50" stroke-width="1" transform="rotate(25,-10,10)"/>
    <ellipse cx="10" cy="10" rx="10" ry="5" fill="#81C784" stroke="#4CAF50" stroke-width="1" transform="rotate(-25,10,10)"/>
    <path d="M0 5 L0 -15" stroke="#66BB6A" stroke-width="2.5"/>
    <ellipse cx="-5" cy="-18" rx="7" ry="4" fill="#81C784" stroke="#4CAF50" stroke-width="0.8"/>
    <ellipse cx="5" cy="-18" rx="7" ry="4" fill="#81C784" stroke="#4CAF50" stroke-width="0.8"/>
    <!-- Cotyledons fading -->
    <ellipse cx="0" cy="15" rx="8" ry="4" fill="#FFE082" opacity="0.4"/>
    <text x="0" y="65" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Проросток</text>
  </g>
  <path d="M340 145 L370 145" stroke="#2E7D32" stroke-width="1.5"/>
  <path d="M370 145 L366 141 M370 145 L366 149" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
  <g transform="translate(420,130)">
    <!-- Stage 5: Young plant -->
    <rect x="-3" y="0" width="6" height="40" fill="#795548" rx="2"/>
    <circle cx="0" cy="-10" r="15" fill="#4CAF50" opacity="0.7"/>
    <circle cx="-8" cy="-5" r="10" fill="#66BB6A" opacity="0.6"/>
    <circle cx="8" cy="-5" r="10" fill="#81C784" opacity="0.5"/>
    <path d="M0 40 Q-10 50 -12 58" stroke="#795548" stroke-width="1.5" fill="none"/>
    <path d="M0 40 Q10 50 12 58" stroke="#795548" stroke-width="1.5" fill="none"/>
    <text x="0" y="72" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Растение</text>
  </g>
  <!-- Conditions -->
  <rect x="30" y="240" width="440" height="65" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="258" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Условия прорастания семян</text>
  <text x="250" y="274" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">1. Вода (набухание семени) | 2. Кислород (дыхание) | 3. Температура (тепло)</text>
  <text x="250" y="290" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Рост: деление + растяжение клеток | Развитие: качественные изменения</text>
  <text x="250" y="303" font-family="Arial,sans-serif" font-size="7" fill="#999" text-anchor="middle">Витамины и гормоны (ауксины, гиббереллины) регулируют рост</text>
''', "Рост и развитие растений", "Биология 6 класс - Урок 29")

# 30: Вегетативное размножение растений
l30 = W('''
  <!-- Natural and artificial vegetative reproduction -->
  <text x="250" y="72" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle" font-weight="bold">Естественное вегетативное размножение</text>
  <!-- Runner/столон (strawberry) -->
  <g transform="translate(120,130)">
    <path d="M-30 0 Q0 -8 30 0 Q60 8 90 0" stroke="#795548" stroke-width="2" fill="none"/>
    <!-- Parent plant -->
    <rect x="-30" y="-20" width="5" height="20" fill="#795548" rx="1"/>
    <circle cx="-27" cy="-25" r="8" fill="#4CAF50" opacity="0.7"/>
    <!-- Daughter plants at nodes -->
    <rect x="27" y="-5" width="4" height="12" fill="#795548" rx="1"/>
    <circle cx="29" cy="-8" r="6" fill="#66BB6A" opacity="0.7"/>
    <rect x="87" y="-5" width="4" height="12" fill="#795548" rx="1"/>
    <circle cx="89" cy="-8" r="6" fill="#66BB6A" opacity="0.7"/>
    <!-- Roots at daughter -->
    <line x1="29" y1="7" x2="27" y2="14" stroke="#795548" stroke-width="1"/>
    <line x1="89" y1="7" x2="87" y2="14" stroke="#795548" stroke-width="1"/>
    <text x="30" y="25" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Усы (земляника)</text>
  </g>
  <!-- Tuber (potato) -->
  <g transform="translate(310,120)">
    <path d="M-30 0 L-50 0" stroke="#795548" stroke-width="2" fill="none"/>
    <ellipse cx="0" cy="0" rx="22" ry="14" fill="#D7CCC8" stroke="#8D6E63" stroke-width="1.5"/>
    <!-- Eyes/buds -->
    <circle cx="-8" cy="-5" r="2.5" fill="#A1887F" stroke="#795548" stroke-width="0.5"/>
    <circle cx="5" cy="-8" r="2" fill="#A1887F" stroke="#795548" stroke-width="0.5"/>
    <circle cx="12" cy="2" r="2.5" fill="#A1887F" stroke="#795548" stroke-width="0.5"/>
    <!-- Sprouts from eyes -->
    <path d="M-8 -7 L-10 -15" stroke="#66BB6A" stroke-width="1.5"/>
    <path d="M5 -10 L6 -18" stroke="#66BB6A" stroke-width="1.5"/>
    <text x="0" y="25" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Клубень (картофель)</text>
  </g>
  <!-- Bulb (onion) -->
  <g transform="translate(440,120)">
    <ellipse cx="0" cy="0" rx="15" ry="20" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/>
    <!-- Scales -->
    <ellipse cx="0" cy="0" rx="10" ry="15" fill="#FFE082" stroke="#F9A825" stroke-width="0.5"/>
    <ellipse cx="0" cy="0" rx="5" ry="8" fill="#FFE0B2" opacity="0.5"/>
    <!-- Sprout -->
    <path d="M0 -20 L0 -32" stroke="#66BB6A" stroke-width="2"/>
    <ellipse cx="0" cy="-34" rx="4" ry="3" fill="#81C784"/>
    <!-- Roots -->
    <line x1="-5" y1="20" x2="-8" y2="30" stroke="#BCAAA4" stroke-width="1"/>
    <line x1="0" y1="20" x2="0" y2="32" stroke="#BCAAA4" stroke-width="1"/>
    <line x1="5" y1="20" x2="8" y2="30" stroke="#BCAAA4" stroke-width="1"/>
    <text x="0" y="45" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Луковица (лук)</text>
  </g>
  <!-- Artificial methods -->
  <text x="250" y="185" font-family="Arial,sans-serif" font-size="10" fill="#E65100" text-anchor="middle" font-weight="bold">Искусственное вегетативное размножение</text>
  <!-- Cuttings -->
  <g transform="translate(80,240)">
    <rect x="-2" y="-15" width="4" height="30" fill="#795548" rx="1"/>
    <ellipse cx="-8" cy="-12" rx="8" ry="5" fill="#81C784" stroke="#4CAF50" stroke-width="0.8" transform="rotate(20,-8,-12)"/>
    <ellipse cx="8" cy="-12" rx="8" ry="5" fill="#81C784" stroke="#4CAF50" stroke-width="0.8" transform="rotate(-20,8,-12)"/>
    <line x1="0" y1="15" x2="0" y2="25" stroke="#795548" stroke-width="1.5"/>
    <text x="0" y="40" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Черенок</text>
  </g>
  <!-- Layering -->
  <g transform="translate(200,250)">
    <rect x="-20" y="-20" width="5" height="20" fill="#795548" rx="1"/>
    <circle cx="-17" cy="-25" r="8" fill="#4CAF50" opacity="0.7"/>
    <path d="M-15 0 Q0 5 15 5 Q25 5 30 0" stroke="#795548" stroke-width="2" fill="none"/>
    <rect x="28" y="-5" width="4" height="12" fill="#795548" rx="1"/>
    <circle cx="30" cy="-8" r="5" fill="#66BB6A" opacity="0.7"/>
    <line x1="30" y1="7" x2="30" y2="14" stroke="#795548" stroke-width="1"/>
    <text x="5" y="28" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Отводок</text>
  </g>
  <!-- Grafting -->
  <g transform="translate(340,240)">
    <!-- Rootstock -->
    <rect x="-3" y="-5" width="6" height="30" fill="#8D6E63" rx="2"/>
    <!-- Scion -->
    <rect x="-3" y="-25" width="6" height="22" fill="#795548" rx="2"/>
    <circle cx="0" cy="-30" r="8" fill="#4CAF50" opacity="0.7"/>
    <!-- Graft junction -->
    <line x1="-8" y1="-5" x2="8" y2="-5" stroke="#E53935" stroke-width="1.5"/>
    <text x="0" y="40" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Прививка</text>
    <text x="0" y="50" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle">подвой + привой</text>
  </g>
  <!-- Division -->
  <g transform="translate(450,240)">
    <circle cx="-12" cy="-10" r="12" fill="#81C784" stroke="#4CAF50" stroke-width="1"/>
    <line x1="0" y1="-22" x2="0" y2="2" stroke="#E53935" stroke-width="1" stroke-dasharray="2,2"/>
    <circle cx="12" cy="-10" r="12" fill="#81C784" stroke="#4CAF50" stroke-width="1"/>
    <path d="M-12 2 L-12 12" stroke="#795548" stroke-width="1.5"/>
    <path d="M12 2 L12 12" stroke="#795548" stroke-width="1.5"/>
    <text x="0" y="28" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Деление</text>
  </g>
''', "Вегетативное размножение растений", "Биология 6 класс - Урок 30")

# 31: Половое размножение покрытосеменных
l31 = W('''
  <!-- Double fertilization diagram -->
  <!-- Flower to fruit sequence -->
  <!-- Step 1: Pollination -->
  <g transform="translate(70,130)">
    <circle cx="0" cy="0" r="25" fill="#E91E63" opacity="0.3" stroke="#C2185B" stroke-width="1"/>
    <!-- Stigma -->
    <path d="M-8 -25 Q0 -32 8 -25" stroke="#4CAF50" stroke-width="2" fill="#81C784"/>
    <line x1="0" y1="-25" x2="0" y2="-10" stroke="#4CAF50" stroke-width="1.5"/>
    <!-- Pollen grains on stigma -->
    <circle cx="-5" cy="-30" r="3" fill="#FFC107" stroke="#FF9800" stroke-width="1"/>
    <circle cx="3" cy="-28" r="2.5" fill="#FFC107" stroke="#FF9800" stroke-width="1"/>
    <!-- Pollen tube growing -->
    <path d="M-5 -27 Q-3 -15 -2 0" stroke="#FF9800" stroke-width="1.5" fill="none" stroke-dasharray="2,1"/>
    <!-- Ovary -->
    <ellipse cx="0" cy="8" rx="10" ry="12" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1.5"/>
    <!-- Ovule -->
    <ellipse cx="0" cy="8" rx="5" ry="7" fill="#A5D6A7"/>
    <text x="0" y="38" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Опыление</text>
  </g>
  <!-- Arrow -->
  <path d="M105 130 L135 130" stroke="#2E7D32" stroke-width="1.5"/>
  <path d="M135 130 L131 126 M135 130 L131 134" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
  <!-- Step 2: Double fertilization -->
  <g transform="translate(200,130)">
    <ellipse cx="0" cy="8" rx="18" ry="22" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1.5"/>
    <!-- Ovule detail -->
    <ellipse cx="0" cy="5" rx="10" ry="15" fill="#A5D6A7" stroke="#388E3C" stroke-width="1"/>
    <!-- Two sperm cells -->
    <circle cx="-3" cy="0" r="3" fill="#E53935" opacity="0.7"/>
    <circle cx="3" cy="5" r="3" fill="#1565C0" opacity="0.7"/>
    <!-- Sperm 1 + Egg = Zygote -->
    <text x="-15" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#E53935">спермий 1</text>
    <text x="8" y="5" font-family="Arial,sans-serif" font-size="6" fill="#1565C0">спермий 2</text>
    <!-- Egg cell -->
    <circle cx="-3" cy="5" r="4" fill="#FFAB91" stroke="#E64A19" stroke-width="0.8"/>
    <!-- Central cell -->
    <ellipse cx="3" cy="12" rx="6" ry="4" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
    <text x="0" y="45" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Двойное оплодотворение</text>
  </g>
  <!-- Arrow -->
  <path d="M245 130 L275 130" stroke="#2E7D32" stroke-width="1.5"/>
  <path d="M275 130 L271 126 M275 130 L271 134" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
  <!-- Step 3: Seed and fruit -->
  <g transform="translate(350,130)">
    <!-- Fruit -->
    <circle cx="0" cy="0" r="22" fill="#E53935" stroke="#C62828" stroke-width="1.5"/>
    <path d="M-2 -22 Q0 -27 2 -22" fill="#795548" stroke="#5D4037" stroke-width="1"/>
    <!-- Seed inside -->
    <ellipse cx="0" cy="0" rx="8" ry="10" fill="#FFF9C4" stroke="#F9A825" stroke-width="1"/>
    <!-- Embryo in seed -->
    <ellipse cx="0" cy="-2" rx="3" ry="5" fill="#81C784" stroke="#4CAF50" stroke-width="0.8"/>
    <!-- Endosperm -->
    <ellipse cx="0" cy="5" rx="5" ry="3" fill="#FFE082" opacity="0.5"/>
    <text x="0" y="35" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Плод + семя</text>
  </g>
  <!-- Results -->
  <rect x="30" y="210" width="440" height="95" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="228" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Двойное оплодотворение (особенность покрытосеменных)</text>
  <text x="50" y="246" font-family="Arial,sans-serif" font-size="8" fill="#E53935">Спермий 1 + Яйцеклетка = Зигота (зародыш)</text>
  <text x="50" y="262" font-family="Arial,sans-serif" font-size="8" fill="#1565C0">Спермий 2 + Центральная клетка = Эндосперм (запас питательных)</text>
  <text x="50" y="280" font-family="Arial,sans-serif" font-size="8" fill="#555">Опыление: перенос пыльцы (ветер, насекомые, птицы)</text>
  <text x="50" y="296" font-family="Arial,sans-serif" font-size="8" fill="#555">Самоопыление vs Перекрёстное опыление (лучше - генетическое разнообразие)</text>
''', "Половое размножение покрытосеменных", "Биология 6 класс - Урок 31")

# 32: Природные сообщества и взаимодействие организмов
l32 = W('''
  <!-- Ecosystem with interactions -->
  <!-- Sky -->
  <rect x="25" y="55" width="450" height="65" fill="#E1F5FE" rx="5" opacity="0.4"/>
  <circle cx="430" cy="80" r="18" fill="#FFF176" stroke="#FDD835" stroke-width="1.5"/>
  <!-- Birds -->
  <path d="M80 80 Q85 73 90 80 Q95 73 100 80" stroke="#333" stroke-width="1.5" fill="none"/>
  <!-- Trees -->
  <rect x="75" y="120" width="8" height="55" fill="#795548" rx="2"/>
  <circle cx="79" cy="105" r="22" fill="#4CAF50" opacity="0.8"/>
  <circle cx="65" cy="110" r="15" fill="#66BB6A" opacity="0.6"/>
  <rect x="185" y="125" width="7" height="50" fill="#795548" rx="2"/>
  <circle cx="188" cy="110" r="18" fill="#388E3C" opacity="0.7"/>
  <!-- Shrubs -->
  <ellipse cx="140" cy="145" rx="20" ry="12" fill="#81C784" opacity="0.6"/>
  <!-- Grass -->
  <path d="M30 175 Q35 160 40 175" stroke="#4CAF50" stroke-width="1.5" fill="none"/>
  <path d="M45 175 Q50 155 55 175" stroke="#66BB6A" stroke-width="1.5" fill="none"/>
  <path d="M60 175 Q62 160 65 175" stroke="#4CAF50" stroke-width="1.5" fill="none"/>
  <!-- Ground line -->
  <line x1="25" y1="175" x2="475" y2="175" stroke="#8D6E63" stroke-width="1"/>
  <!-- Underground -->
  <rect x="25" y="175" width="450" height="65" fill="#D7CCC8" rx="0 0 5 5" opacity="0.5"/>
  <!-- Roots -->
  <path d="M79 175 L79 210" stroke="#795548" stroke-width="2"/>
  <path d="M79 195 Q65 205 55 215" stroke="#795548" stroke-width="1.5" fill="none"/>
  <path d="M79 195 Q90 205 100 215" stroke="#795548" stroke-width="1.5" fill="none"/>
  <path d="M188 175 L188 200" stroke="#795548" stroke-width="1.5"/>
  <!-- Fungi -->
  <g transform="translate(310,165)">
    <path d="M-8 0 Q-10 -8 0 -10 Q10 -8 8 0 Z" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
    <rect x="-2" y="0" width="4" height="10" fill="#D7CCC8" rx="1"/>
  </g>
  <!-- Animals -->
  <!-- Caterpillar -->
  <path d="M100 120 Q105 115 110 120 Q115 125 120 120" stroke="#8BC34A" stroke-width="3.5" fill="none" stroke-linecap="round"/>
  <circle cx="98" cy="120" r="2.5" fill="#689F38"/>
  <!-- Mouse -->
  <g transform="translate(260,168)">
    <ellipse cx="0" cy="0" rx="10" ry="6" fill="#BCAAA4" stroke="#8D6E63" stroke-width="1"/>
    <ellipse cx="-8" cy="-2" rx="4" ry="3" fill="#BCAAA4" stroke="#8D6E63" stroke-width="0.8"/>
    <circle cx="-9" cy="-3" r="1" fill="#333"/>
    <path d="M10 0 Q15 -2 18 0" stroke="#8D6E63" stroke-width="1" fill="none"/>
  </g>
  <!-- Fox -->
  <g transform="translate(420,155)">
    <ellipse cx="0" cy="0" rx="14" ry="8" fill="#FF8A65" stroke="#E64A19" stroke-width="1"/>
    <ellipse cx="-12" cy="-2" rx="7" ry="5" fill="#FF8A65" stroke="#E64A19" stroke-width="1"/>
    <path d="M-14 -6 L-16 -14 L-10 -8 Z" fill="#FFAB91"/>
    <path d="M-8 -6 L-6 -14 L-4 -8 Z" fill="#FFAB91"/>
    <circle cx="-14" cy="-2" r="1.5" fill="#333"/>
    <path d="M14 0 Q20 -3 22 0" stroke="#E64A19" stroke-width="2" fill="none" stroke-linecap="round"/>
  </g>
  <!-- Worm -->
  <path d="M240 200 Q245 195 250 200 Q255 205 260 200" stroke="#FFAB91" stroke-width="2" fill="none" stroke-linecap="round"/>
  <!-- Bacteria dots -->
  <circle cx="300" cy="210" r="2" fill="#FFCC80"/>
  <circle cx="310" cy="215" r="1.5" fill="#FFCC80"/>
  <circle cx="295" cy="218" r="2" fill="#FFCC80"/>
  <!-- Food web arrows -->
  <path d="M95 140 Q130 135 245 165" stroke="#E64A19" stroke-width="1.2" fill="none" marker-end="url(#a)"/>
  <path d="M275 165 Q350 150 410 155" stroke="#E64A19" stroke-width="1.2" fill="none" marker-end="url(#a)"/>
  <defs><marker id="a" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="3" markerHeight="3" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#E64A19"/></marker></defs>
  <!-- Legend -->
  <rect x="30" y="250" width="440" height="60" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="267" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Взаимодействия в природном сообществе</text>
  <text x="250" y="282" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Продуценты (растения) -> Консументы I (травоядные) -> Консументы II (хищники) -> Редуценты (грибы, бактерии)</text>
  <text x="250" y="295" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Конкуренция, симбиоз, паразитизм, хищничество - типы связей между организмами</text>
  <text x="250" y="307" font-family="Arial,sans-serif" font-size="7" fill="#999" text-anchor="middle">Ярусы: деревья -> кустарники -> травы -> мхи - распределение по свету</text>
''', "Природные сообщества и взаимодействие организмов", "Биология 6 класс - Урок 32")

lessons = [
    (25, "Цветок - орган семенного размножения", l25),
    (26, "Плод и семя", l26),
    (27, "Минеральное питание и водный обмен растений", l27),
    (28, "Фотосинтез и дыхание растений", l28),
    (29, "Рост и развитие растений", l29),
    (30, "Вегетативное размножение растений", l30),
    (31, "Половое размножение покрытосеменных", l31),
    (32, "Природные сообщества и взаимодействие организмов", l32),
]

for num, title, svg in lessons:
    with open(os.path.join(D, f"lesson{num}.svg"), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"lesson{num}.svg")

print("Done! 8 SVGs for Grade 6 Lessons 25-32.")
