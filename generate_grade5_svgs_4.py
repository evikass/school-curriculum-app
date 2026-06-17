#!/usr/bin/env python3
"""Generate detailed SVG illustrations for Grade 5 Biology lessons 19-24"""

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
# Lesson 19: Лишайники
# ============================================================
svg19 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#F5F5F5"/><stop offset="100%" stop-color="#E0E0E0"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#616161" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#212121" text-anchor="middle">Лишайники</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 19</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#616161" stroke-width="1" opacity="0.3"/>

<!-- Symbiosis diagram -->
<g transform="translate(250,110)">
  <rect x="-120" y="-40" width="240" height="80" rx="8" fill="white" opacity="0.9" stroke="#616161" stroke-width="1.5"/>
  <text x="0" y="-22" font-family="Arial,sans-serif" font-size="9" fill="#212121" text-anchor="middle" font-weight="bold">СИМБИОЗ = ГРИБ + ВОДОРОСЛЬ</text>
  <line x1="-110" y1="-15" x2="110" y2="-15" stroke="#616161" stroke-width="0.5"/>
  
  <!-- Fungus circle -->
  <circle cx="-50" cy="10" r="25" fill="#BCAAA4" stroke="#795548" stroke-width="1.5"/>
  <path d="M-55,5 Q-50,0 -45,5 Q-50,10 -55,5" fill="#8D6E63" stroke="#5D4037" stroke-width="0.5"/>
  <circle cx="-50" cy="12" r="4" fill="#A1887F" stroke="#5D4037" stroke-width="0.5"/>
  <text x="-50" y="26" font-family="Arial,sans-serif" font-size="6" fill="#4E342E" text-anchor="middle" font-weight="bold">Гриб</text>
  
  <!-- Plus sign -->
  <text x="0" y="14" font-family="Arial,sans-serif" font-size="14" fill="#666" text-anchor="middle">+</text>
  
  <!-- Alga circle -->
  <circle cx="50" cy="10" r="25" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1.5"/>
  <ellipse cx="50" cy="8" rx="8" ry="5" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>
  <circle cx="50" cy="15" r="3" fill="#4CAF50"/>
  <text x="50" y="26" font-family="Arial,sans-serif" font-size="6" fill="#1B5E20" text-anchor="middle" font-weight="bold">Водоросль</text>
  
  <!-- Arrows showing benefits -->
  <path d="M-30,0 L25,0" fill="none" stroke="#F44336" stroke-width="0.8" marker-end="url(#arrow)"/>
  <text x="-2" y="-5" font-family="Arial,sans-serif" font-size="4" fill="#F44336" text-anchor="middle">вода, минер.</text>
  <path d="M25,20 L-30,20" fill="none" stroke="#2E7D32" stroke-width="0.8" marker-end="url(#arrow)"/>
  <text x="-2" y="28" font-family="Arial,sans-serif" font-size="4" fill="#2E7D32" text-anchor="middle">органич. вещества</text>
</g>

<!-- Lichen body structure -->
<g transform="translate(130,240)">
  <rect x="-75" y="-50" width="150" height="90" rx="6" fill="white" opacity="0.9" stroke="#616161" stroke-width="1"/>
  <text x="0" y="-33" font-family="Arial,sans-serif" font-size="7" fill="#212121" text-anchor="middle" font-weight="bold">ВНУТРЕННЕЕ СТРОЕНИЕ</text>
  <line x1="-65" y1="-27" x2="65" y2="-27" stroke="#616161" stroke-width="0.5"/>
  
  <!-- Upper cortex (fungal) -->
  <rect x="-50" y="-22" width="100" height="8" fill="#BCAAA4" stroke="#795548" stroke-width="1"/>
  <text x="60" y="-16" font-family="Arial,sans-serif" font-size="4.5" fill="#4E342E">Верхн. кора (гриб)</text>
  
  <!-- Algal layer -->
  <rect x="-50" y="-14" width="100" height="8" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
  <circle cx="-35" cy="-10" r="3" fill="#81C784"/>
  <circle cx="-20" cy="-10" r="3" fill="#81C784"/>
  <circle cx="-5" cy="-10" r="3" fill="#81C784"/>
  <circle cx="10" cy="-10" r="3" fill="#81C784"/>
  <circle cx="25" cy="-10" r="3" fill="#81C784"/>
  <text x="60" y="-8" font-family="Arial,sans-serif" font-size="4.5" fill="#1B5E20">Слой водорослей</text>
  
  <!-- Medulla (fungal) -->
  <rect x="-50" y="-6" width="100" height="10" fill="#EFEBE9" stroke="#795548" stroke-width="1"/>
  <path d="M-40,-3 Q-35,-5 -30,-3" fill="none" stroke="#BCAAA4" stroke-width="0.8"/>
  <path d="M-20,-1 Q-15,-3 -10,-1" fill="none" stroke="#BCAAA4" stroke-width="0.8"/>
  <path d="M5,-3 Q10,-5 15,-3" fill="none" stroke="#BCAAA4" stroke-width="0.8"/>
  <text x="60" y="0" font-family="Arial,sans-serif" font-size="4.5" fill="#4E342E">Сердцевина (гриб)</text>
  
  <!-- Lower cortex -->
  <rect x="-50" y="4" width="100" height="8" fill="#BCAAA4" stroke="#795548" stroke-width="1"/>
  <text x="60" y="10" font-family="Arial,sans-serif" font-size="4.5" fill="#4E342E">Нижн. кора (гриб)</text>
  
  <!-- Rhizines -->
  <path d="M-30,12 L-30,22" stroke="#8D6E63" stroke-width="1"/>
  <path d="M0,12 L0,22" stroke="#8D6E63" stroke-width="1"/>
  <path d="M30,12 L30,22" stroke="#8D6E63" stroke-width="1"/>
  <text x="0" y="32" font-family="Arial,sans-serif" font-size="4.5" fill="#666" text-anchor="middle">Ризины (прикрепление)</text>
</g>

<!-- Three types of lichens -->
<!-- Накипные -->
<g transform="translate(350,190)">
  <rect x="-55" y="-35" width="110" height="65" rx="6" fill="white" opacity="0.9" stroke="#9E9E9E" stroke-width="1"/>
  <text x="0" y="-18" font-family="Arial,sans-serif" font-size="7" fill="#424242" text-anchor="middle" font-weight="bold">НАКИПНЫЕ</text>
  <!-- Rock surface -->
  <rect x="-40" y="5" width="80" height="15" rx="2" fill="#BDBDBD" stroke="#757575" stroke-width="1"/>
  <!-- Crust on rock -->
  <rect x="-35" y="-5" width="70" height="10" rx="2" fill="#8D6E63" stroke="#5D4037" stroke-width="0.8" opacity="0.7"/>
  <circle cx="-20" cy="0" r="3" fill="#A1887F"/>
  <circle cx="0" cy="-2" r="3" fill="#A1887F"/>
  <circle cx="20" cy="0" r="3" fill="#A1887F"/>
  <text x="0" y="28" font-family="Arial,sans-serif" font-size="5" fill="#424242" text-anchor="middle">На камнях, коре</text>
</g>

<!-- Листовые -->
<g transform="translate(350,260)">
  <rect x="-55" y="-25" width="110" height="50" rx="6" fill="white" opacity="0.9" stroke="#4CAF50" stroke-width="1"/>
  <text x="0" y="-8" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">ЛИСТОВЫЕ</text>
  <!-- Leaf-like lobe -->
  <path d="M-25,5 Q-15,-10 0,0 Q15,-10 25,5 Q15,15 0,12 Q-15,15 -25,5" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
  <path d="M-15,3 Q0,-5 15,3" fill="none" stroke="#4CAF50" stroke-width="0.5"/>
  <text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Пармелия, ксантория</text>
</g>

<!-- Кустистые -->
<g transform="translate(350,310)">
  <text x="0" y="0" font-family="Arial,sans-serif" font-size="7" fill="#795548" font-weight="bold">КУСТИСТЫЕ</text>
  <!-- Branching structure -->
  <path d="M0,2 L0,-12 M0,-12 Q-8,-18 -15,-15" stroke="#8D6E63" stroke-width="1.5" fill="none"/>
  <path d="M0,-12 Q8,-18 15,-15" stroke="#8D6E63" stroke-width="1.5" fill="none"/>
  <path d="M-15,-15 Q-20,-20 -18,-22" stroke="#8D6E63" stroke-width="1" fill="none"/>
  <path d="M15,-15 Q20,-20 18,-22" stroke="#8D6E63" stroke-width="1" fill="none"/>
  <text x="0" y="12" font-family="Arial,sans-serif" font-size="5" fill="#795548" text-anchor="middle">Ягель (олений мох)</text>
</g>

<!-- Bottom -->
<rect x="30" y="330" width="440" height="10" rx="4" fill="white" opacity="0.8" stroke="#616161" stroke-width="0.5"/>
<text x="250" y="338" font-family="Arial,sans-serif" font-size="5.5" fill="#212121" text-anchor="middle" font-weight="bold">Лишайники — индикаторы чистоты воздуха: не растут в загрязнённых местах</text>
</svg>'''

# ============================================================
# Lesson 20: Мхи
# ============================================================
svg20 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#E8F5E9"/><stop offset="100%" stop-color="#A5D6A7"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#2E7D32" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#1B5E20" text-anchor="middle">Мхи</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 20</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#2E7D32" stroke-width="1" opacity="0.3"/>

<!-- Кукушкин лён -->
<g transform="translate(130,185)">
  <rect x="-80" y="-100" width="160" height="195" rx="8" fill="white" opacity="0.9" stroke="#2E7D32" stroke-width="1.5"/>
  <text x="0" y="-83" font-family="Arial,sans-serif" font-size="8" fill="#1B5E20" text-anchor="middle" font-weight="bold">КУКУШКИН ЛЁН</text>
  <line x1="-70" y1="-77" x2="70" y2="-77" stroke="#2E7D32" stroke-width="0.5"/>
  
  <!-- Male plant (smaller) -->
  <g transform="translate(-40,0)">
    <rect x="-3" y="-40" width="6" height="60" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.8" rx="2"/>
    <!-- Leaves -->
    <path d="M3,-30 Q10,-28 3,-25" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.5"/>
    <path d="M3,-20 Q10,-18 3,-15" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.5"/>
    <path d="M3,-10 Q10,-8 3,-5" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.5"/>
    <path d="M-3,-25 Q-10,-23 -3,-20" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.5"/>
    <path d="M-3,-15 Q-10,-13 -3,-10" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.5"/>
    <!-- Top flower-like structure -->
    <path d="M-6,-42 Q0,-48 6,-42 Q3,-38 0,-40 Q-3,-38 -6,-42" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>
    <text x="0" y="30" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Мужское</text>
    <text x="0" y="38" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">растение</text>
    <!-- Rhizoids -->
    <path d="M-2,20 Q-5,30 -8,35" fill="none" stroke="#795548" stroke-width="0.8"/>
    <path d="M2,20 Q5,30 8,35" fill="none" stroke="#795548" stroke-width="0.8"/>
  </g>
  
  <!-- Female plant (with sporophyte) -->
  <g transform="translate(35,0)">
    <rect x="-3" y="-40" width="6" height="65" fill="#388E3C" stroke="#1B5E20" stroke-width="0.8" rx="2"/>
    <!-- Leaves -->
    <path d="M3,-30 Q12,-28 3,-25" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.5"/>
    <path d="M3,-20 Q12,-18 3,-15" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.5"/>
    <path d="M3,-10 Q12,-8 3,-5" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.5"/>
    <path d="M-3,-25 Q-12,-23 -3,-20" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.5"/>
    <path d="M-3,-15 Q-12,-13 -3,-10" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.5"/>
    <!-- Sporophyte (seta + capsule) -->
    <line x1="0" y1="-40" x2="0" y2="-75" stroke="#8D6E63" stroke-width="1.5"/>
    <!-- Capsule (коробочка) -->
    <ellipse cx="0" cy="-80" rx="6" ry="10" fill="#A1887F" stroke="#5D4037" stroke-width="1"/>
    <!-- Cap (колпачок) -->
    <path d="M-5,-85 Q0,-92 5,-85" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
    <!-- Lid -->
    <line x1="-5" y1="-73" x2="5" y2="-73" stroke="#5D4037" stroke-width="0.5"/>
    <!-- Spores -->
    <circle cx="-2" cy="-78" r="1" fill="#5D4037"/>
    <circle cx="2" cy="-76" r="1" fill="#5D4037"/>
    <!-- Peristome teeth -->
    <line x1="-3" y1="-72" x2="-3" y2="-69" stroke="#5D4037" stroke-width="0.5"/>
    <line x1="0" y1="-72" x2="0" y2="-69" stroke="#5D4037" stroke-width="0.5"/>
    <line x1="3" y1="-72" x2="3" y2="-69" stroke="#5D4037" stroke-width="0.5"/>
    
    <text x="0" y="35" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Женское растение</text>
    <text x="0" y="43" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">со спорофитом</text>
    <!-- Rhizoids -->
    <path d="M-2,25 Q-5,35 -8,40" fill="none" stroke="#795548" stroke-width="0.8"/>
    <path d="M2,25 Q5,35 8,40" fill="none" stroke="#795548" stroke-width="0.8"/>
  </g>
  
  <!-- Labels -->
  <line x1="42" y1="-80" x2="65" y2="-90" stroke="#666" stroke-width="0.5"/>
  <text x="67" y="-90" font-family="Arial,sans-serif" font-size="5" fill="#666">Коробочка</text>
  <line x1="35" y1="-60" x2="65" y2="-60" stroke="#666" stroke-width="0.5"/>
  <text x="67" y="-60" font-family="Arial,sans-serif" font-size="5" fill="#666">Ножка (сетка)</text>
  <line x1="-30" y1="40" x2="65" y2="50" stroke="#666" stroke-width="0.5"/>
  <text x="67" y="50" font-family="Arial,sans-serif" font-size="5" fill="#666">Ризоиды</text>
</g>

<!-- Сфагнум -->
<g transform="translate(390,175)">
  <rect x="-70" y="-100" width="140" height="195" rx="8" fill="white" opacity="0.9" stroke="#388E3C" stroke-width="1.5"/>
  <text x="0" y="-83" font-family="Arial,sans-serif" font-size="8" fill="#1B5E20" text-anchor="middle" font-weight="bold">СФАГНУМ</text>
  <text x="0" y="-73" font-family="Arial,sans-serif" font-size="6" fill="#388E3C" text-anchor="middle">(торфяной мох)</text>
  <line x1="-60" y1="-67" x2="60" y2="-67" stroke="#388E3C" stroke-width="0.5"/>
  
  <!-- Sphagnum branch -->
  <line x1="0" y1="-55" x2="0" y2="30" stroke="#81C784" stroke-width="3"/>
  <!-- Side branches -->
  <path d="M0,-40 Q15,-45 20,-40" fill="none" stroke="#A5D6A7" stroke-width="2"/>
  <path d="M0,-25 Q-15,-30 -20,-25" fill="none" stroke="#A5D6A7" stroke-width="2"/>
  <path d="M0,-10 Q15,-15 20,-10" fill="none" stroke="#A5D6A7" stroke-width="2"/>
  <path d="M0,5 Q-15,0 -20,5" fill="none" stroke="#A5D6A7" stroke-width="2"/>
  <!-- Head cluster -->
  <circle cx="0" cy="-58" r="6" fill="#C8E6C9" stroke="#81C784" stroke-width="1"/>
  
  <!-- Cell detail -->
  <g transform="translate(0,50)">
    <rect x="-50" y="-15" width="100" height="30" rx="3" fill="#E8F5E9" stroke="#388E3C" stroke-width="0.5"/>
    <text x="0" y="-3" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle" font-weight="bold">Клетки листа:</text>
    <!-- Living cell (green) + dead cell (water-holding) -->
    <rect x="-40" y="2" width="10" height="10" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>
    <rect x="-28" y="2" width="10" height="10" fill="#E0E0E0" stroke="#9E9E9E" stroke-width="0.8"/>
    <text x="-28" y="9" font-family="Arial,sans-serif" font-size="4" fill="#666" text-anchor="middle">O</text>
    <rect x="-16" y="2" width="10" height="10" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>
    <rect x="-4" y="2" width="10" height="10" fill="#E0E0E0" stroke="#9E9E9E" stroke-width="0.8"/>
    <text x="-4" y="9" font-family="Arial,sans-serif" font-size="4" fill="#666" text-anchor="middle">O</text>
    <text x="30" y="5" font-family="Arial,sans-serif" font-size="4" fill="#2E7D32">живые +</text>
    <text x="30" y="11" font-family="Arial,sans-serif" font-size="4" fill="#9E9E9E">мёртвые (H2O)</text>
  </g>
  
  <!-- Sporophyte (simpler than кукушкин лён) -->
  <g transform="translate(35,-35)">
    <circle cx="0" cy="-5" r="4" fill="#8D6E63" stroke="#5D4037" stroke-width="0.8"/>
    <text x="0" y="8" font-family="Arial,sans-serif" font-size="4" fill="#5D4037" text-anchor="middle">Спорофит</text>
    <text x="0" y="14" font-family="Arial,sans-serif" font-size="4" fill="#5D4037" text-anchor="middle">(редуцир.)</text>
  </g>
  
  <!-- Importance -->
  <rect x="-55" y="80" width="110" height="12" rx="2" fill="#FFF3E0" stroke="#FF9800" stroke-width="0.5"/>
  <text x="0" y="89" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle" font-weight="bold">Торф → топливо, удобрение</text>
</g>

<!-- Bottom -->
<rect x="30" y="325" width="440" height="15" rx="4" fill="white" opacity="0.8" stroke="#2E7D32" stroke-width="0.5"/>
<text x="250" y="336" font-family="Arial,sans-serif" font-size="6.5" fill="#1B5E20" text-anchor="middle" font-weight="bold">Мхи: нет корней (ризоиды), нет проводящей системы · размножение спорами · болотообразователи</text>
</svg>'''

# ============================================================
# Lesson 21: Плауны. Хвощи. Папоротники
# ============================================================
svg21 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#E0F2F1"/><stop offset="100%" stop-color="#B2DFDB"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#00695C" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#004D40" text-anchor="middle">Плауны, хвощи, папоротники</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 21</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#00695C" stroke-width="1" opacity="0.3"/>

<!-- Плаун -->
<g transform="translate(90,185)">
  <rect x="-65" y="-100" width="130" height="195" rx="8" fill="white" opacity="0.9" stroke="#00695C" stroke-width="1.5"/>
  <text x="0" y="-83" font-family="Arial,sans-serif" font-size="9" fill="#004D40" text-anchor="middle" font-weight="bold">ПЛАУН</text>
  <line x1="-55" y1="-77" x2="55" y2="-77" stroke="#00695C" stroke-width="0.5"/>
  
  <!-- Creeping stem -->
  <path d="M-45,30 Q-20,25 0,30 Q20,35 45,30" fill="none" stroke="#2E7D32" stroke-width="3"/>
  <!-- Vertical stems -->
  <line x1="-15" y1="25" x2="-15" y2="-30" stroke="#388E3C" stroke-width="2"/>
  <line x1="15" y1="30" x2="15" y2="-25" stroke="#388E3C" stroke-width="2"/>
  <!-- Small leaves (микрофиллы) -->
  <path d="M-15,-30 Q-20,-32 -15,-35" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.5"/>
  <path d="M-15,-25 Q-20,-27 -15,-30" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.5"/>
  <path d="M-15,-20 Q-20,-22 -15,-25" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.5"/>
  <path d="M-15,-15 Q-20,-17 -15,-20" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.5"/>
  <path d="M-15,-10 Q-10,-12 -15,-15" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.5"/>
  <path d="M-15,-5 Q-10,-7 -15,-10" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.5"/>
  
  <path d="M15,-25 Q10,-27 15,-30" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.5"/>
  <path d="M15,-20 Q10,-22 15,-25" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.5"/>
  <path d="M15,-15 Q10,-17 15,-20" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.5"/>
  <path d="M15,-10 Q20,-12 15,-15" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.5"/>
  
  <!-- Spore-bearing strobilus -->
  <ellipse cx="-15" cy="-40" rx="4" ry="8" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
  <ellipse cx="15" cy="-35" rx="4" ry="8" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
  <!-- Spores -->
  <circle cx="-15" cy="-42" r="1" fill="#E65100"/>
  <circle cx="-15" cy="-38" r="1" fill="#E65100"/>
  <circle cx="15" cy="-37" r="1" fill="#E65100"/>
  <circle cx="15" cy="-33" r="1" fill="#E65100"/>
  
  <text x="0" y="-55" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">Стробилус</text>
  <text x="0" y="-48" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">(со спорами)</text>
  
  <!-- Roots -->
  <path d="M-30,32 Q-35,42 -38,50" fill="none" stroke="#795548" stroke-width="1"/>
  <path d="M0,30 Q-5,42 -8,50" fill="none" stroke="#795548" stroke-width="1"/>
  <path d="M30,32 Q25,42 22,50" fill="none" stroke="#795548" stroke-width="1"/>
  
  <text x="0" y="62" font-family="Arial,sans-serif" font-size="5" fill="#004D40" text-anchor="middle">Стелющийся стебель</text>
  <text x="0" y="70" font-family="Arial,sans-serif" font-size="5" fill="#004D40" text-anchor="middle">Мелкие листья</text>
  <text x="0" y="78" font-family="Arial,sans-serif" font-size="5" fill="#004D40" text-anchor="middle">Споры в стробилусах</text>
  <text x="0" y="86" font-family="Arial,sans-serif" font-size="5" fill="#00695C" text-anchor="middle">Реликтовое растение!</text>
</g>

<!-- Хвощ -->
<g transform="translate(250,185)">
  <rect x="-65" y="-100" width="130" height="195" rx="8" fill="white" opacity="0.9" stroke="#795548" stroke-width="1.5"/>
  <text x="0" y="-83" font-family="Arial,sans-serif" font-size="9" fill="#4E342E" text-anchor="middle" font-weight="bold">ХВОЩ</text>
  <line x1="-55" y1="-77" x2="55" y2="-77" stroke="#795548" stroke-width="0.5"/>
  
  <!-- Spring stem (with strobilus) -->
  <line x1="-25" y1="40" x2="-25" y2="-40" stroke="#8D6E63" stroke-width="2.5"/>
  <!-- Whorls of leaves -->
  <path d="M-25,-20 Q-38,-25 -35,-28" fill="none" stroke="#66BB6A" stroke-width="1.5"/>
  <path d="M-25,-20 Q-12,-25 -15,-28" fill="none" stroke="#66BB6A" stroke-width="1.5"/>
  <path d="M-25,-20 Q-25,-30 -25,-32" fill="none" stroke="#66BB6A" stroke-width="1"/>
  <path d="M-25,-5 Q-38,-10 -35,-13" fill="none" stroke="#66BB6A" stroke-width="1.5"/>
  <path d="M-25,-5 Q-12,-10 -15,-13" fill="none" stroke="#66BB6A" stroke-width="1.5"/>
  <!-- Strobilus -->
  <ellipse cx="-25" cy="-52" rx="5" ry="12" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
  <line x1="-30" y1="-55" x2="-20" y2="-55" stroke="#5D4037" stroke-width="0.5"/>
  <line x1="-30" y1="-50" x2="-20" y2="-50" stroke="#5D4037" stroke-width="0.5"/>
  <line x1="-30" y1="-45" x2="-20" y2="-45" stroke="#5D4037" stroke-width="0.5"/>
  <text x="-25" y="-68" font-family="Arial,sans-serif" font-size="4.5" fill="#4E342E" text-anchor="middle">Весенний</text>
  <text x="-25" y="-62" font-family="Arial,sans-serif" font-size="4.5" fill="#4E342E" text-anchor="middle">(споровый)</text>
  
  <!-- Summer stem (green, branched) -->
  <line x1="25" y1="40" x2="25" y2="-15" stroke="#4CAF50" stroke-width="2.5"/>
  <!-- Whorls of branches -->
  <path d="M25,-10 Q35,-15 40,-20" fill="none" stroke="#66BB6A" stroke-width="1.5"/>
  <path d="M25,-10 Q15,-15 10,-20" fill="none" stroke="#66BB6A" stroke-width="1.5"/>
  <path d="M25,5 Q35,0 40,-5" fill="none" stroke="#66BB6A" stroke-width="1.5"/>
  <path d="M25,5 Q15,0 10,-5" fill="none" stroke="#66BB6A" stroke-width="1.5"/>
  <!-- Side branches with secondary whorls -->
  <path d="M40,-20 Q45,-23 48,-28" fill="none" stroke="#81C784" stroke-width="1"/>
  <path d="M40,-20 Q42,-17 45,-20" fill="none" stroke="#81C784" stroke-width="1"/>
  <path d="M10,-20 Q5,-23 2,-28" fill="none" stroke="#81C784" stroke-width="1"/>
  <path d="M10,-20 Q8,-17 5,-20" fill="none" stroke="#81C784" stroke-width="1"/>
  
  <text x="25" y="-25" font-family="Arial,sans-serif" font-size="4.5" fill="#2E7D32" text-anchor="middle">Летний</text>
  <text x="25" y="-20" font-family="Arial,sans-serif" font-size="4.5" fill="#2E7D32" text-anchor="middle">(фотосинт.)</text>
  
  <!-- Roots -->
  <path d="M-25,42 Q-28,52 -30,58" fill="none" stroke="#795548" stroke-width="1"/>
  <path d="M-25,42 Q-22,52 -20,58" fill="none" stroke="#795548" stroke-width="1"/>
  <path d="M25,42 Q22,52 20,58" fill="none" stroke="#795548" stroke-width="1"/>
  <path d="M25,42 Q28,52 30,58" fill="none" stroke="#795548" stroke-width="1"/>
  
  <!-- Stem cross-section -->
  <circle cx="0" cy="72" r="8" fill="#E8F5E9" stroke="#4CAF50" stroke-width="1"/>
  <circle cx="0" cy="72" r="3" fill="#FFCDD2" stroke="#C62828" stroke-width="0.5"/>
  <text x="15" y="72" font-family="Arial,sans-serif" font-size="4" fill="#4E342E">Полый стебель</text>
  
  <text x="0" y="86" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Мутовки листьев</text>
</g>

<!-- Папоротник -->
<g transform="translate(410,185)">
  <rect x="-65" y="-100" width="130" height="195" rx="8" fill="white" opacity="0.9" stroke="#2E7D32" stroke-width="1.5"/>
  <text x="0" y="-83" font-family="Arial,sans-serif" font-size="8" fill="#1B5E20" text-anchor="middle" font-weight="bold">ПАПОРОТНИК</text>
  <line x1="-55" y1="-77" x2="55" y2="-77" stroke="#2E7D32" stroke-width="0.5"/>
  
  <!-- Frond (вайя) - large compound leaf -->
  <line x1="0" y1="40" x2="0" y2="-60" stroke="#2E7D32" stroke-width="2"/>
  <!-- Pinnae (leaflets) -->
  <path d="M0,-55 Q-15,-50 -20,-55 Q-15,-60 0,-55" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
  <path d="M0,-55 Q15,-50 20,-55 Q15,-60 0,-55" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
  <path d="M0,-45 Q-15,-40 -20,-45 Q-15,-50 0,-45" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
  <path d="M0,-45 Q15,-40 20,-45 Q15,-50 0,-45" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
  <path d="M0,-35 Q-15,-30 -20,-35 Q-15,-40 0,-35" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
  <path d="M0,-35 Q15,-30 20,-35 Q15,-40 0,-35" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
  <path d="M0,-25 Q-15,-20 -20,-25 Q-15,-30 0,-25" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
  <path d="M0,-25 Q15,-20 20,-25 Q15,-30 0,-25" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
  <path d="M0,-15 Q-12,-10 -15,-15 Q-12,-20 0,-15" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <path d="M0,-15 Q12,-10 15,-15 Q12,-20 0,-15" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <path d="M0,-5 Q-10,0 -12,-5 Q-10,-10 0,-5" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <path d="M0,-5 Q10,0 12,-5 Q10,-10 0,-5" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  
  <!-- Sori (spore clusters) on back of frond -->
  <circle cx="-18" cy="-47" r="2" fill="#8D6E63" stroke="#5D4037" stroke-width="0.5"/>
  <circle cx="-18" cy="-37" r="2" fill="#8D6E63" stroke="#5D4037" stroke-width="0.5"/>
  <circle cx="18" cy="-47" r="2" fill="#8D6E63" stroke="#5D4037" stroke-width="0.5"/>
  <circle cx="18" cy="-37" r="2" fill="#8D6E63" stroke="#5D4037" stroke-width="0.5"/>
  
  <!-- Fiddlehead (развёртывающийся лист) -->
  <path d="M30,30 Q28,20 30,10 Q35,5 30,0" fill="none" stroke="#4CAF50" stroke-width="2"/>
  <circle cx="30" cy="-2" r="4" fill="#81C784" stroke="#4CAF50" stroke-width="1"/>
  <text x="30" y="40" font-family="Arial,sans-serif" font-size="4" fill="#2E7D32" text-anchor="middle">Молодой лист</text>
  <text x="30" y="46" font-family="Arial,sans-serif" font-size="4" fill="#2E7D32" text-anchor="middle">(улитка)</text>
  
  <!-- Roots/rhizome -->
  <path d="M0,42 Q-10,50 -15,55" fill="none" stroke="#795548" stroke-width="1.5"/>
  <path d="M0,42 Q10,50 15,55" fill="none" stroke="#795548" stroke-width="1.5"/>
  
  <text x="0" y="65" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle">Крупные листья (вайи)</text>
  <text x="0" y="73" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle">Сорусы на нижней</text>
  <text x="0" y="81" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle">стороне листа</text>
  <text x="0" y="89" font-family="Arial,sans-serif" font-size="5" fill="#00695C" text-anchor="middle">Цветков НЕ бывает!</text>
</g>

<!-- Bottom -->
<rect x="30" y="320" width="440" height="20" rx="6" fill="white" opacity="0.9" stroke="#00695C" stroke-width="1"/>
<text x="250" y="334" font-family="Arial,sans-serif" font-size="7" fill="#004D40" text-anchor="middle" font-weight="bold">Все — высшие споровые: есть корни, стебли, листья · размножаются спорами · нужны вода для оплодотворения</text>
</svg>'''

# ============================================================
# Lesson 22: Голосеменные
# ============================================================
svg22 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#E3F2FD"/><stop offset="100%" stop-color="#BBDEFB"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#1565C0" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#0D47A1" text-anchor="middle">Голосеменные</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 22</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#1565C0" stroke-width="1" opacity="0.3"/>

<!-- Сосна (Pine) -->
<g transform="translate(100,175)">
  <rect x="-70" y="-90" width="140" height="175" rx="8" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1.5"/>
  <text x="0" y="-73" font-family="Arial,sans-serif" font-size="9" fill="#0D47A1" text-anchor="middle" font-weight="bold">СОСНА</text>
  <line x1="-60" y1="-67" x2="60" y2="-67" stroke="#1565C0" stroke-width="0.5"/>
  
  <!-- Tree trunk -->
  <rect x="-5" y="-55" width="10" height="70" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
  <!-- Crown layers -->
  <path d="M-40,-55 Q0,-85 40,-55" fill="#2E7D32" stroke="#1B5E20" stroke-width="1"/>
  <path d="M-45,-45 Q0,-70 45,-45" fill="#388E3C" stroke="#1B5E20" stroke-width="1"/>
  <path d="M-50,-35 Q0,-55 50,-35" fill="#43A047" stroke="#1B5E20" stroke-width="1"/>
  
  <!-- Needles -->
  <path d="M-30,-50 L-35,-55" stroke="#2E7D32" stroke-width="1"/>
  <path d="M-25,-45 L-30,-50" stroke="#2E7D32" stroke-width="1"/>
  <path d="M25,-45 L30,-50" stroke="#2E7D32" stroke-width="1"/>
  <path d="M30,-50 L35,-55" stroke="#2E7D32" stroke-width="1"/>
  
  <!-- Cone (шишка) -->
  <g transform="translate(35,-25)">
    <ellipse cx="0" cy="0" rx="7" ry="14" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
    <!-- Scales -->
    <path d="M-6,-10 Q0,-8 6,-10" fill="none" stroke="#5D4037" stroke-width="0.8"/>
    <path d="M-7,-5 Q0,-3 7,-5" fill="none" stroke="#5D4037" stroke-width="0.8"/>
    <path d="M-7,0 Q0,2 7,0" fill="none" stroke="#5D4037" stroke-width="0.8"/>
    <path d="M-6,5 Q0,7 6,5" fill="none" stroke="#5D4037" stroke-width="0.8"/>
    <text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#5D4037" text-anchor="middle">Шишка</text>
  </g>
  
  <!-- Root system -->
  <path d="M-5,15 Q-20,30 -25,40" fill="none" stroke="#795548" stroke-width="1.5"/>
  <path d="M5,15 Q20,30 25,38" fill="none" stroke="#795548" stroke-width="1.5"/>
  <path d="M0,15 Q0,30 0,38" fill="none" stroke="#795548" stroke-width="1.5"/>
  
  <!-- Needle detail -->
  <g transform="translate(-35,30)">
    <path d="M0,0 L15,-3" stroke="#2E7D32" stroke-width="1.5" stroke-linecap="round"/>
    <path d="M0,5 L15,2" stroke="#2E7D32" stroke-width="1.5" stroke-linecap="round"/>
    <text x="20" y="-1" font-family="Arial,sans-serif" font-size="4" fill="#2E7D32">Хвоинки</text>
    <text x="20" y="5" font-family="Arial,sans-serif" font-size="4" fill="#2E7D32">по 2 в пучке</text>
  </g>
  
  <text x="0" y="60" font-family="Arial,sans-serif" font-size="5" fill="#0D47A1" text-anchor="middle">Стержневая корневая</text>
  <text x="0" y="68" font-family="Arial,sans-serif" font-size="5" fill="#0D47A1" text-anchor="middle">система, глубоко</text>
  <text x="0" y="76" font-family="Arial,sans-serif" font-size="5" fill="#0D47A1" text-anchor="middle">идущие корни</text>
</g>

<!-- Ель (Spruce) -->
<g transform="translate(250,175)">
  <rect x="-55" y="-90" width="110" height="175" rx="8" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1.5"/>
  <text x="0" y="-73" font-family="Arial,sans-serif" font-size="9" fill="#0D47A1" text-anchor="middle" font-weight="bold">ЕЛЬ</text>
  <line x1="-45" y1="-67" x2="45" y2="-67" stroke="#1565C0" stroke-width="0.5"/>
  
  <!-- Tree - triangular shape -->
  <rect x="-4" y="-25" width="8" height="40" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
  <path d="M-40,-25 L0,-65 L40,-25" fill="#1B5E20" stroke="#0D47A1" stroke-width="1"/>
  <path d="M-35,-15 L0,-50 L35,-15" fill="#2E7D32" stroke="#1B5E20" stroke-width="1"/>
  <path d="M-30,-5 L0,-35 L30,-5" fill="#388E3C" stroke="#1B5E20" stroke-width="1"/>
  
  <!-- Hanging cone -->
  <g transform="translate(15,-10)">
    <ellipse cx="0" cy="0" rx="5" ry="12" fill="#A1887F" stroke="#5D4037" stroke-width="1"/>
    <line x1="-4" y1="-5" x2="4" y2="-5" stroke="#5D4037" stroke-width="0.5"/>
    <line x1="-4" y1="0" x2="4" y2="0" stroke="#5D4037" stroke-width="0.5"/>
    <line x1="-4" y1="5" x2="4" y2="5" stroke="#5D4037" stroke-width="0.5"/>
    <line x1="0" y1="-12" x2="0" y2="-15" stroke="#5D4037" stroke-width="0.8"/>
  </g>
  
  <!-- Needle detail -->
  <path d="M-25,25 L-10,22" stroke="#2E7D32" stroke-width="1" stroke-linecap="round"/>
  <path d="M-25,28 L-10,25" stroke="#2E7D32" stroke-width="1" stroke-linecap="round"/>
  <text x="-5" y="25" font-family="Arial,sans-serif" font-size="4" fill="#2E7D32">Хвоинки</text>
  <text x="-5" y="31" font-family="Arial,sans-serif" font-size="4" fill="#2E7D32">по 1</text>
  
  <text x="0" y="50" font-family="Arial,sans-serif" font-size="5" fill="#0D47A1" text-anchor="middle">Поверхностная</text>
  <text x="0" y="58" font-family="Arial,sans-serif" font-size="5" fill="#0D47A1" text-anchor="middle">корневая система</text>
  <text x="0" y="68" font-family="Arial,sans-serif" font-size="5" fill="#0D47A1" text-anchor="middle">Шишки висят вниз</text>
  <text x="0" y="76" font-family="Arial,sans-serif" font-size="5" fill="#0D47A1" text-anchor="middle">Ветви до земли</text>
</g>

<!-- Cone structure (seed detail) -->
<g transform="translate(400,145)">
  <rect x="-60" y="-60" width="120" height="115" rx="6" fill="white" opacity="0.9" stroke="#FF9800" stroke-width="1"/>
  <text x="0" y="-43" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">СЕМЯ ГОЛОСЕМЕННЫХ</text>
  <line x1="-50" y1="-37" x2="50" y2="-37" stroke="#FF9800" stroke-width="0.5"/>
  
  <!-- Cone scale with seed -->
  <path d="M-30,-25 Q-20,-30 0,-25 Q20,-30 30,-25 Q25,-15 0,-10 Q-25,-15 -30,-25" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
  <!-- Seed on scale -->
  <ellipse cx="0" cy="-20" rx="5" ry="3" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
  <text x="0" y="-18" font-family="Arial,sans-serif" font-size="3" fill="#E65100" text-anchor="middle">семя</text>
  <!-- Wing -->
  <path d="M5,-20 Q15,-25 20,-20 Q15,-15 5,-20" fill="#FFE0B2" stroke="#E65100" stroke-width="0.5" opacity="0.7"/>
  <text x="25" y="-18" font-family="Arial,sans-serif" font-size="4" fill="#E65100">крыло</text>
  
  <!-- Seed detail -->
  <ellipse cx="-15" cy="10" rx="10" ry="6" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
  <text x="-15" y="13" font-family="Arial,sans-serif" font-size="4" fill="#E65100" text-anchor="middle">Семя</text>
  <text x="20" y="5" font-family="Arial,sans-serif" font-size="5" fill="#E65100">Семя открыто</text>
  <text x="20" y="13" font-family="Arial,sans-serif" font-size="5" fill="#E65100">(не в плоде!)</text>
  <text x="20" y="21" font-family="Arial,sans-serif" font-size="5" fill="#E65100">голосеменное</text>
  
  <!-- Pollen -->
  <circle cx="-25" cy="30" r="4" fill="#FFD54F" stroke="#F9A825" stroke-width="0.8"/>
  <path d="M-25,26 L-25,24" stroke="#F9A825" stroke-width="0.5"/>
  <path d="M-21,30 L-19,30" stroke="#F9A825" stroke-width="0.5"/>
  <path d="M-29,30 L-31,30" stroke="#F9A825" stroke-width="0.5"/>
  <text x="10" y="33" font-family="Arial,sans-serif" font-size="5" fill="#F9A825">Пыльца</text>
  <text x="10" y="40" font-family="Arial,sans-serif" font-size="5" fill="#F9A825">(ветром)</text>
  
  <text x="0" y="50" font-family="Arial,sans-serif" font-size="4.5" fill="#E65100" text-anchor="middle">Опыление ветром</text>
</g>

<!-- Bottom -->
<rect x="30" y="310" width="440" height="25" rx="6" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1"/>
<text x="250" y="322" font-family="Arial,sans-serif" font-size="6.5" fill="#0D47A1" text-anchor="middle" font-weight="bold">Голосеменные: семена не в плодах (голые) · хвоя · смола · вечнозелёные и листопадные</text>
<text x="250" y="332" font-family="Arial,sans-serif" font-size="5.5" fill="#666" text-anchor="middle">Сосна, ель, лиственница, пихта, кедр, можжевельник · Лесообразователи</text>
</svg>'''

# ============================================================
# Lesson 23: Покрытосеменные, или Цветковые
# ============================================================
svg23 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#FCE4EC"/><stop offset="100%" stop-color="#F8BBD0"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#C2185B" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#880E4F" text-anchor="middle">Покрытосеменные (Цветковые)</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 23</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#C2185B" stroke-width="1" opacity="0.3"/>

<!-- Flower structure -->
<g transform="translate(155,175)">
  <rect x="-110" y="-95" width="220" height="185" rx="8" fill="white" opacity="0.9" stroke="#C2185B" stroke-width="1.5"/>
  <text x="0" y="-78" font-family="Arial,sans-serif" font-size="9" fill="#880E4F" text-anchor="middle" font-weight="bold">СТРОЕНИЕ ЦВЕТКА</text>
  <line x1="-100" y1="-72" x2="100" y2="-72" stroke="#C2185B" stroke-width="0.5"/>
  
  <!-- Pedicel -->
  <line x1="0" y1="60" x2="0" y2="80" stroke="#4CAF50" stroke-width="3"/>
  <text x="15" y="75" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">Цветоножка</text>
  
  <!-- Receptacle -->
  <ellipse cx="0" cy="55" rx="15" ry="5" fill="#81C784" stroke="#4CAF50" stroke-width="1"/>
  <text x="25" y="58" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">Цветоложе</text>
  
  <!-- Sepals (чашелистики) -->
  <path d="M-30,40 Q-35,30 -25,25 Q-15,35 -20,45" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
  <path d="M30,40 Q35,30 25,25 Q15,35 20,45" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
  <path d="M-10,20 Q-15,10 -5,5 Q0,15 -5,25" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>
  <path d="M10,20 Q15,10 5,5 Q0,15 5,25" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>
  <text x="-55" y="35" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">Чашелистики</text>
  <text x="-55" y="42" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">(чашечка)</text>
  
  <!-- Petals (лепестки) -->
  <path d="M-40,15 Q-50,-10 -30,-20 Q-10,-15 -20,5" fill="#F48FB1" stroke="#C2185B" stroke-width="1"/>
  <path d="M40,15 Q50,-10 30,-20 Q10,-15 20,5" fill="#F48FB1" stroke="#C2185B" stroke-width="1"/>
  <path d="M-25,-15 Q-30,-45 0,-50 Q30,-45 25,-15" fill="#EC407A" stroke="#C2185B" stroke-width="1"/>
  <text x="55" y="-10" font-family="Arial,sans-serif" font-size="5" fill="#C2185B">Лепестки</text>
  <text x="55" y="-3" font-family="Arial,sans-serif" font-size="5" fill="#C2185B">(венчик)</text>
  
  <!-- Stamens (тычинки) -->
  <line x1="-12" y1="-10" x2="-18" y2="-35" stroke="#FFD54F" stroke-width="1.5"/>
  <ellipse cx="-18" cy="-38" rx="4" ry="6" fill="#FFD54F" stroke="#F9A825" stroke-width="1"/>
  <line x1="12" y1="-10" x2="18" y2="-35" stroke="#FFD54F" stroke-width="1.5"/>
  <ellipse cx="18" cy="-38" rx="4" ry="6" fill="#FFD54F" stroke="#F9A825" stroke-width="1"/>
  <line x1="0" y1="-5" x2="0" y2="-30" stroke="#FFD54F" stroke-width="1.5"/>
  <ellipse cx="0" cy="-33" rx="4" ry="6" fill="#FFD54F" stroke="#F9A825" stroke-width="1"/>
  <!-- Pollen dots -->
  <circle cx="-18" cy="-40" r="1" fill="#F9A825"/>
  <circle cx="18" cy="-40" r="1" fill="#F9A825"/>
  <circle cx="0" cy="-35" r="1" fill="#F9A825"/>
  <text x="-45" y="-35" font-family="Arial,sans-serif" font-size="5" fill="#F9A825">Тычинки</text>
  <text x="-45" y="-28" font-family="Arial,sans-serif" font-size="4" fill="#F9A825">(пыльца)</text>
  
  <!-- Pistil (пестик) -->
  <ellipse cx="0" cy="-20" rx="5" ry="6" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
  <line x1="0" y1="-14" x2="0" y2="10" stroke="#66BB6A" stroke-width="2"/>
  <!-- Stigma -->
  <path d="M-3,-25 Q0,-30 3,-25" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
  <text x="30" y="-20" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">Пестик</text>
  <text x="30" y="-13" font-family="Arial,sans-serif" font-size="4" fill="#2E7D32">рыльце</text>
  <text x="30" y="-6" font-family="Arial,sans-serif" font-size="4" fill="#2E7D32">столбик</text>
  <text x="30" y="1" font-family="Arial,sans-serif" font-size="4" fill="#2E7D32">завязь</text>
  
  <!-- Ovules inside -->
  <circle cx="-2" cy="0" r="2" fill="#FFEB3B" stroke="#F9A825" stroke-width="0.5"/>
  <circle cx="3" cy="3" r="2" fill="#FFEB3B" stroke="#F9A825" stroke-width="0.5"/>
  <text x="30" y="8" font-family="Arial,sans-serif" font-size="4" fill="#F9A825">семязачатки</text>
</g>

<!-- Classification -->
<g transform="translate(400,120)">
  <rect x="-70" y="-45" width="140" height="85" rx="6" fill="white" opacity="0.9" stroke="#C2185B" stroke-width="1"/>
  <text x="0" y="-28" font-family="Arial,sans-serif" font-size="7" fill="#880E4F" text-anchor="middle" font-weight="bold">КЛАССЫ</text>
  <line x1="-60" y1="-22" x2="60" y2="-22" stroke="#C2185B" stroke-width="0.5"/>
  
  <!-- Двудольные -->
  <rect x="-55" y="-15" width="55" height="45" rx="4" fill="#FCE4EC" stroke="#C2185B" stroke-width="0.8"/>
  <text x="-28" y="0" font-family="Arial,sans-serif" font-size="5.5" fill="#880E4F" text-anchor="middle" font-weight="bold">Двудольные</text>
  <!-- Two cotyledons -->
  <ellipse cx="-35" cy="12" rx="5" ry="8" fill="#F48FB1" stroke="#C2185B" stroke-width="0.5"/>
  <ellipse cx="-20" cy="12" rx="5" ry="8" fill="#F48FB1" stroke="#C2185B" stroke-width="0.5"/>
  <text x="-28" y="26" font-family="Arial,sans-serif" font-size="4" fill="#880E4F" text-anchor="middle">2 семядоли</text>
  
  <!-- Однодольные -->
  <rect x="5" y="-15" width="55" height="45" rx="4" fill="#E8F5E9" stroke="#2E7D32" stroke-width="0.8"/>
  <text x="32" y="0" font-family="Arial,sans-serif" font-size="5.5" fill="#1B5E20" text-anchor="middle" font-weight="bold">Однодольные</text>
  <!-- One cotyledon -->
  <ellipse cx="32" cy="12" rx="8" ry="6" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <text x="32" y="26" font-family="Arial,sans-serif" font-size="4" fill="#1B5E20" text-anchor="middle">1 семядоля</text>
</g>

<!-- Features -->
<g transform="translate(400,240)">
  <rect x="-70" y="-50" width="140" height="95" rx="6" fill="white" opacity="0.9" stroke="#C2185B" stroke-width="1"/>
  <text x="0" y="-33" font-family="Arial,sans-serif" font-size="7" fill="#880E4F" text-anchor="middle" font-weight="bold">ОСОБЕННОСТИ</text>
  <line x1="-60" y1="-27" x2="60" y2="-27" stroke="#C2185B" stroke-width="0.5"/>
  <text x="-55" y="-15" font-family="Arial,sans-serif" font-size="5.5" fill="#880E4F">● Цветок — орган размножения</text>
  <text x="-55" y="-5" font-family="Arial,sans-serif" font-size="5.5" fill="#880E4F">● Семя внутри плода</text>
  <text x="-55" y="5" font-family="Arial,sans-serif" font-size="5.5" fill="#880E4F">● Двойное оплодотворение</text>
  <text x="-55" y="15" font-family="Arial,sans-serif" font-size="5.5" fill="#880E4F">● Разнообразие форм</text>
  <text x="-55" y="25" font-family="Arial,sans-serif" font-size="5.5" fill="#880E4F">● Опыление: насекомые, ветер</text>
  <text x="-55" y="35" font-family="Arial,sans-serif" font-size="5.5" fill="#880E4F">● 300 000+ видов</text>
</g>

<!-- Bottom -->
<rect x="30" y="310" width="440" height="25" rx="6" fill="white" opacity="0.9" stroke="#C2185B" stroke-width="1"/>
<text x="250" y="322" font-family="Arial,sans-serif" font-size="6.5" fill="#880E4F" text-anchor="middle" font-weight="bold">Покрытосеменные — самое молодое и многочисленное отделение растений</text>
<text x="250" y="332" font-family="Arial,sans-serif" font-size="5.5" fill="#666" text-anchor="middle">Семя защищено плодом · цветок → плод с семенами · господствуют на Земле</text>
</svg>'''

# ============================================================
# Lesson 24: Происхождение растений. Основные этапы развития растительного мира
# ============================================================
svg24 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#FFF8E1"/><stop offset="100%" stop-color="#FFECB3"/></linearGradient>
<linearGradient id="timeGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#FFD54F"/><stop offset="100%" stop-color="#FF8F00"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#F57F17" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#E65100" text-anchor="middle">Происхождение растений. Эволюция</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 24</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#F57F17" stroke-width="1" opacity="0.3"/>

<!-- Timeline arrow -->
<line x1="80" y1="280" x2="460" y2="280" stroke="#F57F17" stroke-width="3"/>
<polygon points="460,275 470,280 460,285" fill="#F57F17"/>
<text x="475" y="284" font-family="Arial,sans-serif" font-size="7" fill="#E65100">Время</text>

<!-- Stage 1: Водоросли -->
<g transform="translate(100,180)">
  <rect x="-45" y="-85" width="90" height="80" rx="6" fill="white" opacity="0.9" stroke="#00BCD4" stroke-width="1.5"/>
  <text x="0" y="-68" font-family="Arial,sans-serif" font-size="6" fill="#006064" text-anchor="middle" font-weight="bold">1. ВОДОРОСЛИ</text>
  <line x1="-35" y1="-62" x2="35" y2="-62" stroke="#00BCD4" stroke-width="0.5"/>
  <!-- Simple algae -->
  <path d="M-10,-45 Q-5,-55 0,-45 Q5,-35 10,-45" fill="none" stroke="#00BCD4" stroke-width="2"/>
  <path d="M-15,-35 Q-10,-40 -5,-35" fill="none" stroke="#00BCD4" stroke-width="1.5"/>
  <circle cx="15" cy="-40" r="5" fill="#80DEEA" stroke="#00BCD4" stroke-width="0.8"/>
  <text x="0" y="-18" font-family="Arial,sans-serif" font-size="5" fill="#006064" text-anchor="middle">~3.5 млрд лет</text>
  <text x="0" y="-10" font-family="Arial,sans-serif" font-size="5" fill="#006064" text-anchor="middle">Вода</text>
  <text x="0" y="-2" font-family="Arial,sans-serif" font-size="4.5" fill="#006064" text-anchor="middle">Одноклеточные</text>
  <!-- Timeline dot -->
  <circle cx="0" cy="100" r="4" fill="#00BCD4" stroke="#006064" stroke-width="1"/>
  <line x1="0" y1="5" x2="0" y2="96" stroke="#00BCD4" stroke-width="0.5" stroke-dasharray="2,2"/>
</g>

<!-- Stage 2: Мхи и псилофиты -->
<g transform="translate(200,180)">
  <rect x="-45" y="-85" width="90" height="80" rx="6" fill="white" opacity="0.9" stroke="#2E7D32" stroke-width="1.5"/>
  <text x="0" y="-68" font-family="Arial,sans-serif" font-size="6" fill="#1B5E20" text-anchor="middle" font-weight="bold">2. ПСИЛОФИТЫ</text>
  <line x1="-35" y1="-62" x2="35" y2="-62" stroke="#2E7D32" stroke-width="0.5"/>
  <!-- Simple land plant -->
  <line x1="-5" y1="-20" x2="-5" y2="-45" stroke="#4CAF50" stroke-width="2"/>
  <path d="M-5,-45 Q0,-50 5,-45" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>
  <line x1="-5" y1="-35" x2="-15" y2="-40" stroke="#4CAF50" stroke-width="1"/>
  <line x1="-5" y1="-30" x2="10" y2="-35" stroke="#4CAF50" stroke-width="1"/>
  <!-- No leaves, no roots -->
  <path d="M-5,-20 Q-8,-15 -5,-10" fill="none" stroke="#795548" stroke-width="1"/>
  <text x="0" y="-18" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle">~450 млн лет</text>
  <text x="0" y="-10" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle">Выход на сушу</text>
  <text x="0" y="-2" font-family="Arial,sans-serif" font-size="4.5" fill="#1B5E20" text-anchor="middle">Мхи, псилофиты</text>
  <circle cx="0" cy="100" r="4" fill="#4CAF50" stroke="#1B5E20" stroke-width="1"/>
  <line x1="0" y1="5" x2="0" y2="96" stroke="#4CAF50" stroke-width="0.5" stroke-dasharray="2,2"/>
</g>

<!-- Stage 3: Папоротники, хвощи, плауны -->
<g transform="translate(300,180)">
  <rect x="-45" y="-85" width="90" height="80" rx="6" fill="white" opacity="0.9" stroke="#388E3C" stroke-width="1.5"/>
  <text x="0" y="-68" font-family="Arial,sans-serif" font-size="6" fill="#1B5E20" text-anchor="middle" font-weight="bold">3. ПАПОРОТНИКИ</text>
  <line x1="-35" y1="-62" x2="35" y2="-62" stroke="#388E3C" stroke-width="0.5"/>
  <!-- Fern frond -->
  <line x1="0" y1="-20" x2="0" y2="-50" stroke="#388E3C" stroke-width="2"/>
  <path d="M0,-45 Q-15,-40 -20,-45" fill="none" stroke="#4CAF50" stroke-width="1"/>
  <path d="M0,-40 Q10,-35 15,-40" fill="none" stroke="#4CAF50" stroke-width="1"/>
  <path d="M0,-35 Q-12,-30 -15,-35" fill="none" stroke="#4CAF50" stroke-width="1"/>
  <path d="M0,-30 Q8,-25 12,-30" fill="none" stroke="#4CAF50" stroke-width="1"/>
  <!-- Roots -->
  <path d="M0,-20 Q-5,-12 -8,-8" fill="none" stroke="#795548" stroke-width="1"/>
  <path d="M0,-20 Q5,-12 8,-8" fill="none" stroke="#795548" stroke-width="1"/>
  <text x="0" y="-18" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle">~380 млн лет</text>
  <text x="0" y="-10" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle">Каменноугольный</text>
  <text x="0" y="-2" font-family="Arial,sans-serif" font-size="4.5" fill="#1B5E20" text-anchor="middle">Корни, листья</text>
  <circle cx="0" cy="100" r="4" fill="#388E3C" stroke="#1B5E20" stroke-width="1"/>
  <line x1="0" y1="5" x2="0" y2="96" stroke="#388E3C" stroke-width="0.5" stroke-dasharray="2,2"/>
</g>

<!-- Stage 4: Голосеменные -->
<g transform="translate(380,180)">
  <rect x="-35" y="-85" width="70" height="80" rx="6" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1.5"/>
  <text x="0" y="-68" font-family="Arial,sans-serif" font-size="6" fill="#0D47A1" text-anchor="middle" font-weight="bold">4. ГОЛОСЕМ.</text>
  <line x1="-25" y1="-62" x2="25" y2="-62" stroke="#1565C0" stroke-width="0.5"/>
  <!-- Conifer -->
  <path d="M0,-55 L-12,-35 L12,-35 Z" fill="#2E7D32" stroke="#1B5E20" stroke-width="0.8"/>
  <path d="M0,-42 L-15,-25 L15,-25 Z" fill="#388E3C" stroke="#1B5E20" stroke-width="0.8"/>
  <rect x="-2" y="-25" width="4" height="10" fill="#8D6E63"/>
  <text x="0" y="-18" font-family="Arial,sans-serif" font-size="5" fill="#0D47A1" text-anchor="middle">~300 млн</text>
  <text x="0" y="-10" font-family="Arial,sans-serif" font-size="5" fill="#0D47A1" text-anchor="middle">Семена!</text>
  <text x="0" y="-2" font-family="Arial,sans-serif" font-size="4.5" fill="#0D47A1" text-anchor="middle">Без плода</text>
  <circle cx="0" cy="100" r="4" fill="#1565C0" stroke="#0D47A1" stroke-width="1"/>
  <line x1="0" y1="5" x2="0" y2="96" stroke="#1565C0" stroke-width="0.5" stroke-dasharray="2,2"/>
</g>

<!-- Stage 5: Покрытосеменные -->
<g transform="translate(455,180)">
  <rect x="-30" y="-85" width="60" height="80" rx="6" fill="white" opacity="0.9" stroke="#C2185B" stroke-width="1.5"/>
  <text x="0" y="-68" font-family="Arial,sans-serif" font-size="5.5" fill="#880E4F" text-anchor="middle" font-weight="bold">5. ПОКРЫТОС.</text>
  <line x1="-20" y1="-62" x2="20" y2="-62" stroke="#C2185B" stroke-width="0.5"/>
  <!-- Flower -->
  <circle cx="0" cy="-45" r="6" fill="#F48FB1" stroke="#C2185B" stroke-width="0.8"/>
  <circle cx="0" cy="-45" r="2.5" fill="#FFD54F"/>
  <line x1="0" y1="-39" x2="0" y2="-25" stroke="#4CAF50" stroke-width="1.5"/>
  <path d="M0,-30 Q-8,-28 -5,-25" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <path d="M0,-30 Q8,-28 5,-25" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <text x="0" y="-18" font-family="Arial,sans-serif" font-size="5" fill="#880E4F" text-anchor="middle">~130 млн</text>
  <text x="0" y="-10" font-family="Arial,sans-serif" font-size="5" fill="#880E4F" text-anchor="middle">Цветок!</text>
  <text x="0" y="-2" font-family="Arial,sans-serif" font-size="4.5" fill="#880E4F" text-anchor="middle">Плод</text>
  <circle cx="0" cy="100" r="4" fill="#C2185B" stroke="#880E4F" stroke-width="1"/>
  <line x1="0" y1="5" x2="0" y2="96" stroke="#C2185B" stroke-width="0.5" stroke-dasharray="2,2"/>
</g>

<!-- Evolution summary at bottom -->
<rect x="30" y="290" width="440" height="40" rx="6" fill="white" opacity="0.9" stroke="#F57F17" stroke-width="1"/>
<text x="250" y="305" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">Эволюция: вода → суша · простое → сложное · нет тканей → есть ткани</text>
<text x="250" y="317" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Споры → семена (голосеменные) → семена в плодах (покрытосеменные)</text>
<text x="250" y="327" font-family="Arial,sans-serif" font-size="5.5" fill="#666" text-anchor="middle">Каменный уголь — остатки древних папоротников · Процесс шёл миллионы лет</text>
</svg>'''

print("Generating Grade 5 Biology SVGs (lessons 19-24)...")
print()

write_svg("lesson19.svg", svg19)
write_svg("lesson20.svg", svg20)
write_svg("lesson21.svg", svg21)
write_svg("lesson22.svg", svg22)
write_svg("lesson23.svg", svg23)
write_svg("lesson24.svg", svg24)

print("\nAll 24 lessons done!")
