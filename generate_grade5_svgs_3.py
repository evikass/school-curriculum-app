#!/usr/bin/env python3
"""Generate detailed SVG illustrations for Grade 5 Biology lessons 13-18 (Fungi + Plants start)"""

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
# Lesson 13: Общая характеристика грибов
# ============================================================
svg13 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#EFEBE9"/><stop offset="100%" stop-color="#D7CCC8"/></linearGradient>
<linearGradient id="capGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#A1887F"/><stop offset="100%" stop-color="#795548"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#5D4037" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#3E2723" text-anchor="middle">Общая характеристика грибов</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 13</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#5D4037" stroke-width="1" opacity="0.3"/>

<!-- Mushroom structure -->
<g transform="translate(140,175)">
  <rect x="-90" y="-95" width="180" height="180" rx="8" fill="white" opacity="0.9" stroke="#5D4037" stroke-width="1.5"/>
  <text x="0" y="-78" font-family="Arial,sans-serif" font-size="9" fill="#3E2723" text-anchor="middle" font-weight="bold">СТРОЕНИЕ ГРИБА</text>
  <line x1="-80" y1="-72" x2="80" y2="-72" stroke="#5D4037" stroke-width="0.5"/>
  
  <!-- Cap -->
  <path d="M-45,-50 Q-40,-70 -20,-65 Q0,-60 20,-65 Q40,-70 45,-50 Q30,-40 0,-38 Q-30,-40 -45,-50" fill="url(#capGrad)" stroke="#4E342E" stroke-width="1.5"/>
  <!-- Cap surface texture -->
  <path d="M-30,-58 Q-20,-55 -10,-58" fill="none" stroke="#8D6E63" stroke-width="0.5"/>
  <path d="M10,-58 Q20,-55 30,-58" fill="none" stroke="#8D6E63" stroke-width="0.5"/>
  
  <!-- Gills under cap -->
  <line x1="-25" y1="-42" x2="-15" y2="-32" stroke="#BCAAA4" stroke-width="0.6"/>
  <line x1="-15" y1="-43" x2="-5" y2="-32" stroke="#BCAAA4" stroke-width="0.6"/>
  <line x1="-5" y1="-44" x2="5" y2="-32" stroke="#BCAAA4" stroke-width="0.6"/>
  <line x1="5" y1="-43" x2="15" y2="-32" stroke="#BCAAA4" stroke-width="0.6"/>
  <line x1="15" y1="-42" x2="25" y2="-32" stroke="#BCAAA4" stroke-width="0.6"/>
  
  <!-- Stem -->
  <rect x="-10" y="-38" width="20" height="50" rx="4" fill="#D7CCC8" stroke="#5D4037" stroke-width="1.5"/>
  <!-- Ring on stem -->
  <rect x="-14" y="-25" width="28" height="5" rx="2" fill="#BCAAA4" stroke="#795548" stroke-width="0.8"/>
  
  <!-- Mycelium (грибница) -->
  <path d="M-10,12 Q-25,20 -35,35" fill="none" stroke="#8D6E63" stroke-width="1.5"/>
  <path d="M-5,15 Q-10,25 -15,40" fill="none" stroke="#8D6E63" stroke-width="1.5"/>
  <path d="M0,15 Q5,25 10,38" fill="none" stroke="#8D6E63" stroke-width="1.5"/>
  <path d="M5,12 Q20,20 30,35" fill="none" stroke="#8D6E63" stroke-width="1.5"/>
  <path d="M-15,30 Q-20,38 -30,42" fill="none" stroke="#A1887F" stroke-width="1"/>
  <path d="M-20,22 Q-30,28 -40,35" fill="none" stroke="#A1887F" stroke-width="1"/>
  <path d="M15,30 Q25,38 35,40" fill="none" stroke="#A1887F" stroke-width="1"/>
  <path d="M20,22 Q30,28 40,32" fill="none" stroke="#A1887F" stroke-width="1"/>
  <!-- Hyphae dots -->
  <circle cx="-35" cy="35" r="2" fill="#8D6E63" opacity="0.5"/>
  <circle cx="-15" cy="40" r="2" fill="#8D6E63" opacity="0.5"/>
  <circle cx="10" cy="38" r="2" fill="#8D6E63" opacity="0.5"/>
  <circle cx="30" cy="35" r="2" fill="#8D6E63" opacity="0.5"/>
  
  <!-- Labels -->
  <line x1="45" y1="-55" x2="65" y2="-65" stroke="#666" stroke-width="0.5"/>
  <text x="67" y="-65" font-family="Arial,sans-serif" font-size="5" fill="#666">Шляпка</text>
  
  <line x1="10" y1="-20" x2="65" y2="-20" stroke="#666" stroke-width="0.5"/>
  <text x="67" y="-20" font-family="Arial,sans-serif" font-size="5" fill="#666">Плёнка (кольцо)</text>
  
  <line x1="10" y1="-5" x2="65" y2="-5" stroke="#666" stroke-width="0.5"/>
  <text x="67" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#666">Ножка</text>
  
  <line x1="25" y1="-38" x2="65" y2="-40" stroke="#666" stroke-width="0.5"/>
  <text x="67" y="-40" font-family="Arial,sans-serif" font-size="5" fill="#666">Гименофор (пластинки)</text>
  
  <line x1="30" y1="30" x2="65" y2="30" stroke="#666" stroke-width="0.5"/>
  <text x="67" y="30" font-family="Arial,sans-serif" font-size="5" fill="#666">Грибница</text>
  <text x="67" y="38" font-family="Arial,sans-serif" font-size="5" fill="#666">(мицелий)</text>
</g>

<!-- Hyphae detail -->
<g transform="translate(390,115)">
  <rect x="-65" y="-45" width="130" height="85" rx="6" fill="white" opacity="0.9" stroke="#5D4037" stroke-width="1"/>
  <text x="0" y="-28" font-family="Arial,sans-serif" font-size="7" fill="#3E2723" text-anchor="middle" font-weight="bold">ГИФЫ (нити мицелия)</text>
  <line x1="-55" y1="-22" x2="55" y2="-22" stroke="#5D4037" stroke-width="0.5"/>
  <!-- Hyphae tubes -->
  <path d="M-45,-10 Q-30,-15 -15,-10 Q0,-5 15,-10 Q30,-15 45,-10" fill="none" stroke="#8D6E63" stroke-width="3"/>
  <!-- Septa (cross walls) -->
  <line x1="-30" y1="-14" x2="-30" y2="-6" stroke="#5D4037" stroke-width="0.8"/>
  <line x1="0" y1="-8" x2="0" y2="0" stroke="#5D4037" stroke-width="0.8"/>
  <line x1="30" y1="-14" x2="30" y2="-6" stroke="#5D4037" stroke-width="0.8"/>
  <!-- Nuclei in cells -->
  <circle cx="-15" cy="-10" r="3" fill="#795548" opacity="0.4"/>
  <circle cx="15" cy="-10" r="3" fill="#795548" opacity="0.4"/>
  <text x="-15" y="-8" font-family="Arial,sans-serif" font-size="3" fill="white" text-anchor="middle">я</text>
  <text x="15" y="-8" font-family="Arial,sans-serif" font-size="3" fill="white" text-anchor="middle">я</text>
  <!-- Branch -->
  <path d="M0,-10 Q5,0 15,10 Q20,15 25,15" fill="none" stroke="#A1887F" stroke-width="2"/>
  <text x="0" y="25" font-family="Arial,sans-serif" font-size="5" fill="#3E2723" text-anchor="middle">Разделяются перегородками</text>
  <text x="0" y="33" font-family="Arial,sans-serif" font-size="5" fill="#3E2723" text-anchor="middle">(септами) — многоядерные</text>
</g>

<!-- Fungi characteristics -->
<g transform="translate(390,225)">
  <rect x="-65" y="-45" width="130" height="85" rx="6" fill="white" opacity="0.9" stroke="#5D4037" stroke-width="1"/>
  <text x="0" y="-28" font-family="Arial,sans-serif" font-size="7" fill="#3E2723" text-anchor="middle" font-weight="bold">ПРИЗНАКИ ГРИБОВ</text>
  <line x1="-55" y1="-22" x2="55" y2="-22" stroke="#5D4037" stroke-width="0.5"/>
  <text x="-50" y="-10" font-family="Arial,sans-serif" font-size="5.5" fill="#3E2723">● Гетеротрофы (не фотосинтез.)</text>
  <text x="-50" y="0" font-family="Arial,sans-serif" font-size="5.5" fill="#3E2723">● Клет. стенка из хитина</text>
  <text x="-50" y="10" font-family="Arial,sans-serif" font-size="5.5" fill="#3E2723">● Запасное вещество — гликоген</text>
  <text x="-50" y="20" font-family="Arial,sans-serif" font-size="5.5" fill="#3E2723">● Всасывание пищи всем телом</text>
  <text x="-50" y="30" font-family="Arial,sans-serif" font-size="5.5" fill="#3E2723">● Размножение: споры</text>
  <text x="-50" y="40" font-family="Arial,sans-serif" font-size="5.5" fill="#3E2723">● Неподвижны, растут как растения</text>
</g>

<!-- Spore detail -->
<g transform="translate(40,310)">
  <rect x="-20" y="-12" width="130" height="24" rx="4" fill="#EFEBE9" stroke="#5D4037" stroke-width="0.5"/>
  <circle cx="-5" cy="0" r="4" fill="#8D6E63" stroke="#5D4037" stroke-width="0.5"/>
  <text x="30" y="3" font-family="Arial,sans-serif" font-size="6" fill="#3E2723">Спора — клетка размножения</text>
</g>

<!-- Bottom -->
<rect x="30" y="310" width="440" height="25" rx="6" fill="white" opacity="0.9" stroke="#5D4037" stroke-width="1"/>
<text x="250" y="327" font-family="Arial,sans-serif" font-size="7" fill="#3E2723" text-anchor="middle" font-weight="bold">Грибы — царство: признаки животных (гетеротрофы, хитин) + растений (неподвижны, рост)</text>
</svg>'''

# ============================================================
# Lesson 14: Шляпочные грибы
# ============================================================
svg14 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#F1F8E9"/><stop offset="100%" stop-color="#DCEDC8"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#33691E" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#1B5E20" text-anchor="middle">Шляпочные грибы</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 14</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#33691E" stroke-width="1" opacity="0.3"/>

<!-- White mushroom (Боровик/Белый) -->
<g transform="translate(80,160)">
  <rect x="-55" y="-80" width="110" height="155" rx="8" fill="white" opacity="0.9" stroke="#33691E" stroke-width="1"/>
  <text x="0" y="-63" font-family="Arial,sans-serif" font-size="7" fill="#1B5E20" text-anchor="middle" font-weight="bold">БЕЛЫЙ ГРИБ</text>
  <line x1="-45" y1="-57" x2="45" y2="-57" stroke="#33691E" stroke-width="0.5"/>
  <!-- Cap - brown -->
  <path d="M-35,-45 Q-30,-60 -15,-55 Q0,-52 15,-55 Q30,-60 35,-45 Q25,-38 0,-36 Q-25,-38 -35,-45" fill="#795548" stroke="#4E342E" stroke-width="1.5"/>
  <!-- Stem - thick, light -->
  <rect x="-8" y="-36" width="16" height="45" rx="5" fill="#EFEBE9" stroke="#8D6E63" stroke-width="1"/>
  <!-- Stem texture -->
  <path d="M-5,-20 Q0,-18 5,-20" fill="none" stroke="#BCAAA4" stroke-width="0.5"/>
  <path d="M-5,-10 Q0,-8 5,-10" fill="none" stroke="#BCAAA4" stroke-width="0.5"/>
  <!-- Tubes under cap (not gills) -->
  <rect x="-20" y="-40" width="40" height="5" rx="1" fill="#FFE0B2" stroke="#BCAAA4" stroke-width="0.5"/>
  <text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle">Трубчатый гриб</text>
  <text x="0" y="30" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle">Съедобный</text>
</g>

<!-- Fly agaric (Мухомор) -->
<g transform="translate(220,160)">
  <rect x="-55" y="-80" width="110" height="155" rx="8" fill="white" opacity="0.9" stroke="#C62828" stroke-width="1"/>
  <text x="0" y="-63" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">МУХОМОР</text>
  <line x1="-45" y1="-57" x2="45" y2="-57" stroke="#C62828" stroke-width="0.5"/>
  <!-- Cap - red with white spots -->
  <path d="M-35,-45 Q-30,-60 -15,-55 Q0,-52 15,-55 Q30,-60 35,-45 Q25,-38 0,-36 Q-25,-38 -35,-45" fill="#F44336" stroke="#C62828" stroke-width="1.5"/>
  <!-- White spots -->
  <circle cx="-20" cy="-52" r="4" fill="white" opacity="0.9"/>
  <circle cx="-8" cy="-48" r="3" fill="white" opacity="0.9"/>
  <circle cx="5" cy="-52" r="4" fill="white" opacity="0.9"/>
  <circle cx="18" cy="-48" r="3" fill="white" opacity="0.9"/>
  <circle cx="-12" cy="-43" r="2.5" fill="white" opacity="0.9"/>
  <circle cx="12" cy="-43" r="2.5" fill="white" opacity="0.9"/>
  <!-- Stem - thin, white -->
  <rect x="-6" y="-36" width="12" height="45" rx="4" fill="white" stroke="#BDBDBD" stroke-width="1"/>
  <!-- Ring -->
  <rect x="-10" y="-20" width="20" height="4" rx="2" fill="#E0E0E0" stroke="#9E9E9E" stroke-width="0.5"/>
  <!-- Volva (воронка) at base -->
  <path d="M-12,9 Q-15,15 -8,12 Q0,10 8,12 Q15,15 12,9" fill="#E0E0E0" stroke="#9E9E9E" stroke-width="0.8"/>
  <!-- Gills under cap -->
  <line x1="-20" y1="-38" x2="-10" y2="-32" stroke="#FFCDD2" stroke-width="0.5"/>
  <line x1="-10" y1="-39" x2="0" y2="-32" stroke="#FFCDD2" stroke-width="0.5"/>
  <line x1="0" y1="-40" x2="10" y2="-32" stroke="#FFCDD2" stroke-width="0.5"/>
  <line x1="10" y1="-39" x2="20" y2="-32" stroke="#FFCDD2" stroke-width="0.5"/>
  <text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">Пластинчатый гриб</text>
  <rect x="-25" y="25" width="50" height="15" rx="3" fill="#FFEBEE" stroke="#C62828" stroke-width="0.8"/>
  <text x="0" y="35" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">ЯДОВИТ!</text>
</g>

<!-- Mycorrhiza illustration -->
<g transform="translate(380,140)">
  <rect x="-75" y="-65" width="150" height="120" rx="8" fill="white" opacity="0.9" stroke="#FF9800" stroke-width="1.5"/>
  <text x="0" y="-48" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">МИКОРИЗА</text>
  <text x="0" y="-38" font-family="Arial,sans-serif" font-size="5.5" fill="#E65100" text-anchor="middle">(грибокорень)</text>
  <line x1="-65" y1="-32" x2="65" y2="-32" stroke="#FF9800" stroke-width="0.5"/>
  
  <!-- Tree root -->
  <path d="M-50,-15 Q-25,-20 0,-15 Q25,-10 50,-15" fill="none" stroke="#795548" stroke-width="5" stroke-linecap="round"/>
  <!-- Fungal hyphae wrapping around root -->
  <path d="M-40,-18 Q-35,-25 -25,-18 Q-20,-12 -10,-18 Q-5,-25 5,-18 Q10,-12 20,-18 Q25,-25 35,-18" fill="none" stroke="#FF9800" stroke-width="1.5"/>
  <path d="M-35,-12 Q-30,-18 -20,-12 Q-15,-5 -5,-12 Q0,-18 10,-12 Q15,-5 25,-12 Q30,-18 40,-12" fill="none" stroke="#FF9800" stroke-width="1.5"/>
  <!-- Hyphae going into soil -->
  <path d="M-30,-15 Q-35,5 -40,15" fill="none" stroke="#FF9800" stroke-width="1"/>
  <path d="M-10,-15 Q-15,5 -20,15" fill="none" stroke="#FF9800" stroke-width="1"/>
  <path d="M10,-15 Q5,5 0,15" fill="none" stroke="#FF9800" stroke-width="1"/>
  <path d="M30,-15 Q25,5 20,15" fill="none" stroke="#FF9800" stroke-width="1"/>
  <!-- Root label -->
  <text x="0" y="25" font-family="Arial,sans-serif" font-size="5" fill="#795548" text-anchor="middle">Корень дерева</text>
  <text x="0" y="35" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">Гифы гриба обвивают корень</text>
  <text x="0" y="45" font-family="Arial,sans-serif" font-size="5" fill="#666" text-anchor="middle">Взаимовыгодный симбиоз!</text>
</g>

<!-- Bottom classification -->
<rect x="30" y="265" width="210" height="70" rx="6" fill="white" opacity="0.9" stroke="#33691E" stroke-width="1"/>
<text x="135" y="282" font-family="Arial,sans-serif" font-size="7" fill="#1B5E20" text-anchor="middle" font-weight="bold">Трубчатые грибы</text>
<text x="135" y="293" font-family="Arial,sans-serif" font-size="5.5" fill="#666" text-anchor="middle">Белый, подберёзовик, подосиновик,</text>
<text x="135" y="303" font-family="Arial,sans-serif" font-size="5.5" fill="#666" text-anchor="middle">маслёнок — трубочки под шляпкой</text>
<rect x="260" y="265" width="210" height="70" rx="6" fill="white" opacity="0.9" stroke="#33691E" stroke-width="1"/>
<text x="365" y="282" font-family="Arial,sans-serif" font-size="7" fill="#1B5E20" text-anchor="middle" font-weight="bold">Пластинчатые грибы</text>
<text x="365" y="293" font-family="Arial,sans-serif" font-size="5.5" fill="#666" text-anchor="middle">Сыроежка, рыжик, шампиньон,</text>
<text x="365" y="303" font-family="Arial,sans-serif" font-size="5.5" fill="#666" text-anchor="middle">волнушка — пластинки под шляпкой</text>
</svg>'''

# ============================================================
# Lesson 15: Плесневые грибы и дрожжи
# ============================================================
svg15 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#F3E5F5"/><stop offset="100%" stop-color="#E1BEE7"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#7B1FA2" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#4A148C" text-anchor="middle">Плесневые грибы и дрожжи</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 15</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#7B1FA2" stroke-width="1" opacity="0.3"/>

<!-- Мукор (Mucor) -->
<g transform="translate(130,175)">
  <rect x="-95" y="-95" width="190" height="180" rx="8" fill="white" opacity="0.9" stroke="#7B1FA2" stroke-width="1.5"/>
  <text x="0" y="-78" font-family="Arial,sans-serif" font-size="9" fill="#4A148C" text-anchor="middle" font-weight="bold">МУКОР (белая плесень)</text>
  <line x1="-85" y1="-72" x2="85" y2="-72" stroke="#7B1FA2" stroke-width="0.5"/>
  
  <!-- Substrate (bread) -->
  <rect x="-70" y="45" width="140" height="20" rx="3" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
  <text x="0" y="58" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">Субстрат (хлеб)</text>
  
  <!-- Mycelium in substrate -->
  <path d="M-50,45 Q-55,35 -60,30" fill="none" stroke="#CE93D8" stroke-width="1"/>
  <path d="M-30,45 Q-25,35 -20,30" fill="none" stroke="#CE93D8" stroke-width="1"/>
  <path d="M0,45 Q5,35 10,30" fill="none" stroke="#CE93D8" stroke-width="1"/>
  <path d="M30,45 Q35,35 40,30" fill="none" stroke="#CE93D8" stroke-width="1"/>
  <path d="M50,45 Q55,35 60,30" fill="none" stroke="#CE93D8" stroke-width="1"/>
  
  <!-- Sporangiophores (stalks) -->
  <line x1="-50" y1="30" x2="-50" y2="-40" stroke="#9C27B0" stroke-width="2"/>
  <line x1="-20" y1="30" x2="-20" y2="-50" stroke="#9C27B0" stroke-width="2"/>
  <line x1="10" y1="30" x2="10" y2="-45" stroke="#9C27B0" stroke-width="2"/>
  <line x1="40" y1="30" x2="40" y2="-35" stroke="#9C27B0" stroke-width="2"/>
  
  <!-- Sporangia (heads with spores) -->
  <circle cx="-50" cy="-50" r="12" fill="#CE93D8" stroke="#7B1FA2" stroke-width="1.5"/>
  <circle cx="-20" cy="-60" r="14" fill="#BA68C8" stroke="#7B1FA2" stroke-width="1.5"/>
  <circle cx="10" cy="-55" r="13" fill="#CE93D8" stroke="#7B1FA2" stroke-width="1.5"/>
  <circle cx="40" cy="-45" r="11" fill="#BA68C8" stroke="#7B1FA2" stroke-width="1.5"/>
  
  <!-- Spores inside -->
  <circle cx="-52" cy="-52" r="1.5" fill="#4A148C"/>
  <circle cx="-47" cy="-48" r="1.5" fill="#4A148C"/>
  <circle cx="-50" cy="-46" r="1.5" fill="#4A148C"/>
  <circle cx="-22" cy="-62" r="1.5" fill="#4A148C"/>
  <circle cx="-18" cy="-58" r="1.5" fill="#4A148C"/>
  <circle cx="-20" cy="-55" r="1.5" fill="#4A148C"/>
  <circle cx="8" cy="-57" r="1.5" fill="#4A148C"/>
  <circle cx="12" cy="-53" r="1.5" fill="#4A148C"/>
  <circle cx="38" cy="-47" r="1.5" fill="#4A148C"/>
  <circle cx="42" cy="-43" r="1.5" fill="#4A148C"/>
  
  <!-- Labels -->
  <line x1="55" y1="-55" x2="75" y2="-65" stroke="#666" stroke-width="0.5"/>
  <text x="77" y="-65" font-family="Arial,sans-serif" font-size="5" fill="#666">Спорангий</text>
  <text x="77" y="-58" font-family="Arial,sans-serif" font-size="5" fill="#666">(со спорами)</text>
  
  <line x1="45" y1="-10" x2="75" y2="-10" stroke="#666" stroke-width="0.5"/>
  <text x="77" y="-10" font-family="Arial,sans-serif" font-size="5" fill="#666">Спорангиеносец</text>
  
  <line x1="60" y1="38" x2="77" y2="30" stroke="#666" stroke-width="0.5"/>
  <text x="77" y="30" font-family="Arial,sans-serif" font-size="5" fill="#666">Мицелий</text>
  
  <text x="0" y="70" font-family="Arial,sans-serif" font-size="5" fill="#4A148C" text-anchor="middle">Несептированный мицелий (одна клетка)</text>
  <text x="0" y="78" font-family="Arial,sans-serif" font-size="5" fill="#4A148C" text-anchor="middle">Размножение спорами</text>
</g>

<!-- Пеницилл (Penicillium) -->
<g transform="translate(385,120)">
  <rect x="-70" y="-45" width="140" height="85" rx="6" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1"/>
  <text x="0" y="-28" font-family="Arial,sans-serif" font-size="7" fill="#0D47A1" text-anchor="middle" font-weight="bold">ПЕНИЦИЛЛ (зелёная плесень)</text>
  <line x1="-60" y1="-22" x2="60" y2="-22" stroke="#1565C0" stroke-width="0.5"/>
  
  <!-- Branching conidiophores -->
  <line x1="-20" y1="20" x2="-20" y2="-5" stroke="#2E7D32" stroke-width="1.5"/>
  <line x1="-20" y1="-5" x2="-35" y2="-15" stroke="#2E7D32" stroke-width="1"/>
  <line x1="-20" y1="-5" x2="-5" y2="-15" stroke="#2E7D32" stroke-width="1"/>
  <line x1="-35" y1="-15" x2="-40" y2="-25" stroke="#2E7D32" stroke-width="0.8"/>
  <line x1="-35" y1="-15" x2="-30" y2="-25" stroke="#2E7D32" stroke-width="0.8"/>
  <line x1="-5" y1="-15" x2="-10" y2="-25" stroke="#2E7D32" stroke-width="0.8"/>
  <line x1="-5" y1="-15" x2="0" y2="-25" stroke="#2E7D32" stroke-width="0.8"/>
  
  <!-- Conidia chains -->
  <circle cx="-40" cy="-27" r="2" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <circle cx="-37" cy="-30" r="2" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <circle cx="-34" cy="-33" r="2" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <circle cx="-30" cy="-27" r="2" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <circle cx="-27" cy="-30" r="2" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <circle cx="-10" cy="-27" r="2" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <circle cx="-7" cy="-30" r="2" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <circle cx="0" cy="-27" r="2" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <circle cx="3" cy="-30" r="2" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  
  <text x="30" y="-15" font-family="Arial,sans-serif" font-size="5" fill="#0D47A1">Конидии</text>
  <text x="30" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#0D47A1">(споры)</text>
  <text x="0" y="32" font-family="Arial,sans-serif" font-size="5" fill="#0D47A1" text-anchor="middle">Септированный мицелий → антибиотик</text>
</g>

<!-- Дрожжи (Yeast) -->
<g transform="translate(385,260)">
  <rect x="-70" y="-55" width="140" height="100" rx="6" fill="white" opacity="0.9" stroke="#FF9800" stroke-width="1"/>
  <text x="0" y="-38" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">ДРОЖЖИ</text>
  <line x1="-60" y1="-32" x2="60" y2="-32" stroke="#FF9800" stroke-width="0.5"/>
  
  <!-- Yeast cells - oval with budding -->
  <ellipse cx="-30" cy="-10" rx="8" ry="6" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
  <circle cx="-30" cy="-13" r="2.5" fill="#FFCC80" stroke="#E65100" stroke-width="0.5"/>
  
  <ellipse cx="-5" cy="-5" rx="8" ry="6" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
  <!-- Budding -->
  <ellipse cx="7" cy="-9" rx="5" ry="4" fill="#FFF3E0" stroke="#E65100" stroke-width="0.8"/>
  <circle cx="-5" cy="-8" r="2" fill="#FFCC80"/>
  
  <ellipse cx="25" cy="-15" rx="7" ry="5" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
  
  <ellipse cx="15" cy="8" rx="8" ry="6" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
  <!-- Budding chain -->
  <ellipse cx="28" cy="5" rx="5" ry="4" fill="#FFF3E0" stroke="#E65100" stroke-width="0.8"/>
  <ellipse cx="37" cy="3" rx="3.5" ry="3" fill="#FFF8E1" stroke="#E65100" stroke-width="0.6"/>
  
  <ellipse cx="-20" cy="10" rx="7" ry="5" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
  
  <text x="0" y="28" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">Почкование — бесполое размножение</text>
  <text x="0" y="37" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">Спиртовое брожение: C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂</text>
</g>

<!-- Bottom -->
<rect x="30" y="325" width="440" height="15" rx="4" fill="white" opacity="0.8" stroke="#7B1FA2" stroke-width="0.5"/>
<text x="250" y="336" font-family="Arial,sans-serif" font-size="6" fill="#4A148C" text-anchor="middle" font-weight="bold">Мукор → порча продуктов | Пеницилл → антибиотики | Дрожжи → хлеб, квас, вино</text>
</svg>'''

# ============================================================
# Lesson 16: Грибы-паразиты
# ============================================================
svg16 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#FFEBEE"/><stop offset="100%" stop-color="#FFCDD2"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#C62828" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#B71C1C" text-anchor="middle">Грибы-паразиты</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 16</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#C62828" stroke-width="1" opacity="0.3"/>

<!-- Головня (Smut) -->
<g transform="translate(90,160)">
  <rect x="-65" y="-80" width="130" height="150" rx="6" fill="white" opacity="0.9" stroke="#C62828" stroke-width="1"/>
  <text x="0" y="-63" font-family="Arial,sans-serif" font-size="7" fill="#B71C1C" text-anchor="middle" font-weight="bold">ГОЛОВНЯ</text>
  <line x1="-55" y1="-57" x2="55" y2="-57" stroke="#C62828" stroke-width="0.5"/>
  <!-- Wheat ear with dark spores -->
  <line x1="0" y1="-45" x2="0" y2="30" stroke="#8D6E63" stroke-width="2"/>
  <!-- Normal grains on left -->
  <ellipse cx="-5" cy="-35" rx="4" ry="3" fill="#FFD54F" stroke="#F9A825" stroke-width="0.5"/>
  <ellipse cx="-5" cy="-28" rx="4" ry="3" fill="#FFD54F" stroke="#F9A825" stroke-width="0.5"/>
  <!-- Infected grains - black spore masses -->
  <ellipse cx="5" cy="-35" rx="5" ry="4" fill="#333" stroke="#000" stroke-width="0.5"/>
  <ellipse cx="5" cy="-28" rx="5" ry="4" fill="#333" stroke="#000" stroke-width="0.5"/>
  <ellipse cx="5" cy="-21" rx="5" ry="4" fill="#333" stroke="#000" stroke-width="0.5"/>
  <!-- Spores coming out -->
  <circle cx="12" cy="-35" r="1" fill="#333"/>
  <circle cx="14" cy="-30" r="1" fill="#333"/>
  <circle cx="11" cy="-25" r="1" fill="#333"/>
  <text x="0" y="45" font-family="Arial,sans-serif" font-size="5" fill="#B71C1C" text-anchor="middle">Поражает злаки:</text>
  <text x="0" y="53" font-family="Arial,sans-serif" font-size="5" fill="#B71C1C" text-anchor="middle">колос → чёрная масса</text>
  <text x="0" y="61" font-family="Arial,sans-serif" font-size="5" fill="#B71C1C" text-anchor="middle">спор вместо зерна</text>
</g>

<!-- Ржавчина (Rust) -->
<g transform="translate(240,160)">
  <rect x="-65" y="-80" width="130" height="150" rx="6" fill="white" opacity="0.9" stroke="#E65100" stroke-width="1"/>
  <text x="0" y="-63" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle" font-weight="bold">РЖАВЧИНА</text>
  <line x1="-55" y1="-57" x2="55" y2="-57" stroke="#E65100" stroke-width="0.5"/>
  <!-- Wheat leaf with rust spots -->
  <path d="M-40,-40 Q0,-45 40,-40 Q38,-30 0,-25 Q-38,-30 -40,-40" fill="#81C784" stroke="#2E7D32" stroke-width="1.5"/>
  <!-- Rust pustules -->
  <ellipse cx="-20" cy="-37" rx="5" ry="3" fill="#FF9800" stroke="#E65100" stroke-width="0.8"/>
  <ellipse cx="0" cy="-35" rx="6" ry="3" fill="#FF9800" stroke="#E65100" stroke-width="0.8"/>
  <ellipse cx="20" cy="-37" rx="5" ry="3" fill="#FF9800" stroke="#E65100" stroke-width="0.8"/>
  <!-- Spores -->
  <circle cx="-20" cy="-42" r="1" fill="#E65100"/>
  <circle cx="0" cy="-40" r="1" fill="#E65100"/>
  <circle cx="20" cy="-42" r="1" fill="#E65100"/>
  <!-- Second leaf -->
  <path d="M-35,-10 Q0,-15 35,-10 Q33,0 0,5 Q-33,0 -35,-10" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
  <ellipse cx="-10" cy="-7" rx="4" ry="2" fill="#FF9800" stroke="#E65100" stroke-width="0.5"/>
  <ellipse cx="10" cy="-7" rx="4" ry="2" fill="#FF9800" stroke="#E65100" stroke-width="0.5"/>
  <!-- Stem -->
  <line x1="0" y1="5" x2="0" y2="30" stroke="#795548" stroke-width="2"/>
  <text x="0" y="45" font-family="Arial,sans-serif" font-size="5" fill="#BF360C" text-anchor="middle">Рыжие пятна на листьях</text>
  <text x="0" y="53" font-family="Arial,sans-serif" font-size="5" fill="#BF360C" text-anchor="middle">и стеблях злаков</text>
  <text x="0" y="61" font-family="Arial,sans-serif" font-size="5" fill="#BF360C" text-anchor="middle">Снижает урожайность</text>
</g>

<!-- Трутовик (Bracket fungus) -->
<g transform="translate(390,160)">
  <rect x="-65" y="-80" width="130" height="150" rx="6" fill="white" opacity="0.9" stroke="#795548" stroke-width="1"/>
  <text x="0" y="-63" font-family="Arial,sans-serif" font-size="7" fill="#4E342E" text-anchor="middle" font-weight="bold">ТРУТОВИК</text>
  <line x1="-55" y1="-57" x2="55" y2="-57" stroke="#795548" stroke-width="0.5"/>
  <!-- Tree trunk -->
  <rect x="-45" y="-40" width="25" height="80" rx="2" fill="#8D6E63" stroke="#5D4037" stroke-width="1.5"/>
  <!-- Bark texture -->
  <line x1="-45" y1="-30" x2="-20" y2="-30" stroke="#6D4C41" stroke-width="0.5"/>
  <line x1="-45" y1="-15" x2="-20" y2="-15" stroke="#6D4C41" stroke-width="0.5"/>
  <line x1="-45" y1="0" x2="-20" y2="0" stroke="#6D4C41" stroke-width="0.5"/>
  <line x1="-45" y1="15" x2="-20" y2="15" stroke="#6D4C41" stroke-width="0.5"/>
  <!-- Bracket fungus (shelf-like) -->
  <path d="M-20,-30 Q-10,-35 0,-30 Q10,-35 20,-30 Q25,-25 20,-20 Q10,-15 0,-18 Q-10,-15 -20,-20 Q-25,-25 -20,-30" fill="#A1887F" stroke="#5D4037" stroke-width="1.5"/>
  <!-- Concentric rings on top -->
  <path d="M-15,-27 Q0,-32 15,-27" fill="none" stroke="#8D6E63" stroke-width="0.5"/>
  <path d="M-10,-24 Q0,-28 10,-24" fill="none" stroke="#8D6E63" stroke-width="0.5"/>
  <!-- Pores underneath -->
  <circle cx="-8" cy="-21" r="1" fill="#5D4037"/>
  <circle cx="0" cy="-20" r="1" fill="#5D4037"/>
  <circle cx="8" cy="-21" r="1" fill="#5D4037"/>
  <!-- Another bracket -->
  <path d="M-20,-5 Q-10,-10 5,-5 Q15,-10 25,-5 Q28,0 25,5 Q15,10 5,7 Q-5,10 -15,5 Q-20,0 -20,-5" fill="#BCAAA4" stroke="#795548" stroke-width="1"/>
  <!-- Hyphae inside trunk -->
  <path d="M-20,-10 Q-10,-8 -5,-15" fill="none" stroke="#FF9800" stroke-width="0.8" stroke-dasharray="2,1"/>
  <path d="M-20,5 Q-10,8 -5,2" fill="none" stroke="#FF9800" stroke-width="0.8" stroke-dasharray="2,1"/>
  <path d="M-20,20 Q-10,22 -5,15" fill="none" stroke="#FF9800" stroke-width="0.8" stroke-dasharray="2,1"/>
  <!-- Rot indication -->
  <rect x="-45" y="10" width="25" height="20" fill="#FFE0B2" opacity="0.3"/>
  <text x="20" y="20" font-family="Arial,sans-serif" font-size="5" fill="#4E342E">Гниль древесины</text>
  <text x="0" y="45" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Паразит деревьев</text>
  <text x="0" y="53" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Вызывает гниль</text>
  <text x="0" y="61" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Гифы разрушают ствол</text>
</g>

<!-- Bottom -->
<rect x="30" y="310" width="440" height="25" rx="6" fill="white" opacity="0.9" stroke="#C62828" stroke-width="1"/>
<text x="250" y="327" font-family="Arial,sans-serif" font-size="7" fill="#B71C1C" text-anchor="middle" font-weight="bold">Грибы-паразиты питаются органическими веществами живых организмов</text>
</svg>'''

# ============================================================
# Lesson 17: Разнообразие, распространение, значение растений
# ============================================================
svg17 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#E8F5E9"/><stop offset="100%" stop-color="#C8E6C9"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#2E7D32" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#1B5E20" text-anchor="middle">Разнообразие, распространение, значение растений</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 17</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#2E7D32" stroke-width="1" opacity="0.3"/>

<!-- Plant diversity tree -->
<g transform="translate(250,160)">
  <!-- Main trunk -->
  <rect x="-5" y="-70" width="10" height="80" fill="#795548" stroke="#5D4037" stroke-width="1"/>
  
  <!-- Branches to plant groups -->
  <line x1="-5" y1="-55" x2="-100" y2="-85" stroke="#4CAF50" stroke-width="2"/>
  <line x1="0" y1="-50" x2="-50" y2="-85" stroke="#4CAF50" stroke-width="2"/>
  <line x1="0" y1="-50" x2="50" y2="-85" stroke="#4CAF50" stroke-width="2"/>
  <line x1="5" y1="-55" x2="100" y2="-85" stroke="#4CAF50" stroke-width="2"/>
  
  <!-- Водоросли -->
  <g transform="translate(-100,-100)">
    <rect x="-40" y="-20" width="80" height="40" rx="6" fill="white" opacity="0.9" stroke="#00BCD4" stroke-width="1.5"/>
    <path d="M-25,-5 Q-20,-15 -15,-5 Q-10,-15 -5,-5" fill="none" stroke="#00BCD4" stroke-width="2"/>
    <text x="15" y="-5" font-family="Arial,sans-serif" font-size="7" fill="#006064" font-weight="bold">Водоросли</text>
    <text x="15" y="5" font-family="Arial,sans-serif" font-size="5" fill="#006064">нет тканей</text>
  </g>
  
  <!-- Мхи -->
  <g transform="translate(-50,-100)">
    <rect x="-35" y="-20" width="70" height="40" rx="6" fill="white" opacity="0.9" stroke="#4CAF50" stroke-width="1.5"/>
    <path d="M-15,-5 L-15,-15 M-12,-5 L-12,-15 M-9,-5 L-9,-15" stroke="#2E7D32" stroke-width="1.5"/>
    <circle cx="-15" cy="-16" r="2" fill="#66BB6A"/>
    <circle cx="-12" cy="-16" r="2" fill="#66BB6A"/>
    <circle cx="-9" cy="-16" r="2" fill="#66BB6A"/>
    <text x="15" y="-5" font-family="Arial,sans-serif" font-size="7" fill="#1B5E20" font-weight="bold">Мхи</text>
    <text x="15" y="5" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20">нет корней</text>
  </g>
  
  <!-- Папоротники -->
  <g transform="translate(50,-100)">
    <rect x="-40" y="-20" width="80" height="40" rx="6" fill="white" opacity="0.9" stroke="#388E3C" stroke-width="1.5"/>
    <path d="M-20,-5 Q-15,-15 -5,-10 Q0,-5 5,-10 Q15,-15 20,-5" fill="none" stroke="#388E3C" stroke-width="1.5"/>
    <path d="M-10,-8 Q-5,-12 0,-8 Q5,-12 10,-8" fill="none" stroke="#388E3C" stroke-width="1"/>
    <text x="25" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#1B5E20" font-weight="bold">Папоротники</text>
    <text x="25" y="5" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20">споры</text>
  </g>
  
  <!-- Семенные -->
  <g transform="translate(100,-100)">
    <rect x="-40" y="-20" width="80" height="40" rx="6" fill="white" opacity="0.9" stroke="#FF9800" stroke-width="1.5"/>
    <ellipse cx="-15" cy="-5" rx="8" ry="10" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
    <circle cx="-15" cy="-5" r="4" fill="#8D6E63" stroke="#5D4037" stroke-width="0.5"/>
    <text x="20" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#E65100" font-weight="bold">Семенные</text>
    <text x="20" y="5" font-family="Arial,sans-serif" font-size="5" fill="#E65100">семена</text>
  </g>
  
  <!-- Root system -->
  <path d="M-5,10 Q-20,30 -30,40" fill="none" stroke="#8D6E63" stroke-width="1.5"/>
  <path d="M0,10 Q5,30 10,40" fill="none" stroke="#8D6E63" stroke-width="1.5"/>
  <path d="M5,10 Q20,30 30,35" fill="none" stroke="#8D6E63" stroke-width="1.5"/>
</g>

<!-- Plant significance -->
<rect x="30" y="235" width="440" height="90" rx="8" fill="white" opacity="0.9" stroke="#2E7D32" stroke-width="1.5"/>
<text x="250" y="252" font-family="Arial,sans-serif" font-size="8" fill="#1B5E20" text-anchor="middle" font-weight="bold">ЗНАЧЕНИЕ РАСТЕНИЙ</text>
<line x1="40" y1="258" x2="460" y2="258" stroke="#2E7D32" stroke-width="0.5"/>

<!-- Oxygen/Photosynthesis -->
<g transform="translate(100,280)">
  <circle cx="0" cy="0" r="10" fill="#B3E5FC" stroke="#0277BD" stroke-width="1"/>
  <text x="0" y="3" font-family="Arial,sans-serif" font-size="5" fill="#0277BD" text-anchor="middle">O2</text>
  <text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle" font-weight="bold">Кислород</text>
</g>

<!-- Food -->
<g transform="translate(200,280)">
  <path d="M-5,-8 Q0,-12 5,-8 Q8,-4 5,2 Q0,8 -5,2 Q-8,-4 -5,-8" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
  <text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle" font-weight="bold">Пища</text>
</g>

<!-- Building materials -->
<g transform="translate(300,280)">
  <rect x="-8" y="-8" width="16" height="16" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
  <text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle" font-weight="bold">Строит-во</text>
</g>

<!-- Medicine -->
<g transform="translate(400,280)">
  <rect x="-8" y="-5" width="16" height="10" rx="5" fill="#FFCDD2" stroke="#C62828" stroke-width="0.8"/>
  <line x1="0" y1="-5" x2="0" y2="5" stroke="#C62828" stroke-width="0.5"/>
  <text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle" font-weight="bold">Медицина</text>
</g>

<text x="250" y="315" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Фотосинтез: CO2 + H2O → глюкоза + O2 (на свету с хлорофиллом)</text>
</svg>'''

# ============================================================
# Lesson 18: Водоросли
# ============================================================
svg18 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#E0F7FA"/><stop offset="100%" stop-color="#B2EBF2"/></linearGradient>
<linearGradient id="waterGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#4DD0E1" stop-opacity="0.3"/><stop offset="100%" stop-color="#00838F" stop-opacity="0.5"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#00695C" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#004D40" text-anchor="middle">Водоросли</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 18</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#00695C" stroke-width="1" opacity="0.3"/>

<!-- Water background -->
<rect x="30" y="55" width="440" height="255" rx="6" fill="url(#waterGrad)"/>

<!-- Зелёные водоросли -->
<g transform="translate(100,160)">
  <rect x="-55" y="-70" width="110" height="135" rx="6" fill="white" opacity="0.9" stroke="#2E7D32" stroke-width="1.5"/>
  <text x="0" y="-53" font-family="Arial,sans-serif" font-size="7" fill="#1B5E20" text-anchor="middle" font-weight="bold">ЗЕЛЁНЫЕ</text>
  <line x1="-45" y1="-47" x2="45" y2="-47" stroke="#2E7D32" stroke-width="0.5"/>
  
  <!-- Spirogyra - spiral chloroplast -->
  <rect x="-5" y="-35" width="12" height="55" rx="6" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1" opacity="0.7"/>
  <path d="M1,-30 Q6,-25 1,-20 Q-4,-15 1,-10 Q6,-5 1,0 Q-4,5 1,10 Q6,15 1,20" fill="none" stroke="#2E7D32" stroke-width="1.5"/>
  <!-- Another cell -->
  <rect x="10" y="-25" width="12" height="45" rx="6" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1" opacity="0.7"/>
  <path d="M16,-20 Q21,-15 16,-10 Q11,-5 16,0 Q21,5 16,10" fill="none" stroke="#2E7D32" stroke-width="1.5"/>
  <!-- Nuclei -->
  <circle cx="1" cy="-5" r="3" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <circle cx="16" cy="0" r="3" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  
  <!-- Chlamydomonas -->
  <circle cx="-30" cy="25" r="10" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
  <ellipse cx="-30" cy="25" rx="5" ry="3" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.5"/>
  <circle cx="-33" cy="22" r="2" fill="#F44336" stroke="#C62828" stroke-width="0.5"/>
  <path d="M-25,20 Q-20,18 -18,15" fill="none" stroke="#2E7D32" stroke-width="1"/>
  <path d="M-25,22 Q-20,22 -18,22" fill="none" stroke="#2E7D32" stroke-width="1"/>
  
  <text x="0" y="48" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle">Спирогира, хламидомонада</text>
  <text x="0" y="56" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle">Пресные воды</text>
</g>

<!-- Бурые водоросли -->
<g transform="translate(250,160)">
  <rect x="-55" y="-70" width="110" height="135" rx="6" fill="white" opacity="0.9" stroke="#795548" stroke-width="1.5"/>
  <text x="0" y="-53" font-family="Arial,sans-serif" font-size="7" fill="#4E342E" text-anchor="middle" font-weight="bold">БУРЫЕ</text>
  <line x1="-45" y1="-47" x2="45" y2="-47" stroke="#795548" stroke-width="0.5"/>
  
  <!-- Laminaria (морская капуста) -->
  <path d="M-5,-40 L-5,35" stroke="#8D6E63" stroke-width="3"/>
  <!-- Holdfast -->
  <path d="M-15,35 Q-10,40 -5,35 Q0,40 5,35 Q10,40 15,35" fill="none" stroke="#6D4C41" stroke-width="1.5"/>
  <!-- Blade -->
  <path d="M-5,-40 Q-25,-35 -20,-15 Q-15,5 -20,25" fill="none" stroke="#A1887F" stroke-width="8" stroke-linecap="round" opacity="0.7"/>
  <path d="M-5,-40 Q15,-35 10,-15 Q5,5 10,25" fill="none" stroke="#BCAAA4" stroke-width="6" stroke-linecap="round" opacity="0.6"/>
  <!-- Midrib -->
  <path d="M-5,-40 L-5,30" stroke="#6D4C41" stroke-width="1.5"/>
  
  <!-- Fucus -->
  <path d="M25,-35 Q20,-25 25,-15 Q30,-5 25,5 Q20,15 25,25" fill="none" stroke="#8D6E63" stroke-width="3" stroke-linecap="round"/>
  <path d="M25,-20 Q30,-18 32,-15" fill="none" stroke="#8D6E63" stroke-width="2" stroke-linecap="round"/>
  <!-- Air bladders -->
  <circle cx="28" cy="-10" r="3" fill="#D7CCC8" stroke="#8D6E63" stroke-width="0.5"/>
  
  <text x="0" y="48" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Ламинария, фукус</text>
  <text x="0" y="56" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Моря и океаны</text>
</g>

<!-- Красные водоросли -->
<g transform="translate(400,160)">
  <rect x="-55" y="-70" width="110" height="135" rx="6" fill="white" opacity="0.9" stroke="#C62828" stroke-width="1.5"/>
  <text x="0" y="-53" font-family="Arial,sans-serif" font-size="7" fill="#B71C1C" text-anchor="middle" font-weight="bold">КРАСНЫЕ</text>
  <line x1="-45" y1="-47" x2="45" y2="-47" stroke="#C62828" stroke-width="0.5"/>
  
  <!-- Branching red algae -->
  <path d="M0,-40 L0,-20" stroke="#E57373" stroke-width="2"/>
  <path d="M0,-20 Q-15,-15 -25,-10" stroke="#EF5350" stroke-width="1.5" fill="none"/>
  <path d="M0,-20 Q15,-15 25,-10" stroke="#EF5350" stroke-width="1.5" fill="none"/>
  <path d="M0,-20 Q0,-10 0,0" stroke="#E57373" stroke-width="1.5" fill="none"/>
  <path d="M-25,-10 Q-30,-5 -35,-5" stroke="#EF9A9A" stroke-width="1" fill="none"/>
  <path d="M-25,-10 Q-20,-5 -25,0" stroke="#EF9A9A" stroke-width="1" fill="none"/>
  <path d="M25,-10 Q30,-5 35,-5" stroke="#EF9A9A" stroke-width="1" fill="none"/>
  <path d="M25,-10 Q20,-5 25,0" stroke="#EF9A9A" stroke-width="1" fill="none"/>
  <path d="M0,0 Q-10,5 -15,15" stroke="#E57373" stroke-width="1" fill="none"/>
  <path d="M0,0 Q10,5 15,15" stroke="#E57373" stroke-width="1" fill="none"/>
  
  <!-- Porphyra (лавр) -->
  <path d="M-35,20 Q-25,10 -20,20 Q-15,30 -10,20 Q-5,10 0,20 Q5,30 10,20" fill="none" stroke="#C62828" stroke-width="1.5"/>
  
  <text x="0" y="48" font-family="Arial,sans-serif" font-size="5" fill="#B71C1C" text-anchor="middle">Порфира, родимения</text>
  <text x="0" y="56" font-family="Arial,sans-serif" font-size="5" fill="#B71C1C" text-anchor="middle">Глубокие моря</text>
</g>

<!-- Bottom characteristics -->
<rect x="30" y="310" width="440" height="25" rx="6" fill="white" opacity="0.9" stroke="#00695C" stroke-width="1"/>
<text x="250" y="322" font-family="Arial,sans-serif" font-size="6.5" fill="#004D40" text-anchor="middle" font-weight="bold">Водоросли: нет корней, стеблей, листьев · автотрофы (фотосинтез) · обитатели воды</text>
<text x="250" y="332" font-family="Arial,sans-serif" font-size="5.5" fill="#666" text-anchor="middle">Одноклеточные и многоклеточные · Размножение: вегетативное, бесполое (споры), половое</text>
</svg>'''

print("Generating Grade 5 Biology SVGs (lessons 13-18)...")
print()

write_svg("lesson13.svg", svg13)
write_svg("lesson14.svg", svg14)
write_svg("lesson15.svg", svg15)
write_svg("lesson16.svg", svg16)
write_svg("lesson17.svg", svg17)
write_svg("lesson18.svg", svg18)

print("\nLessons 13-18 done!")
