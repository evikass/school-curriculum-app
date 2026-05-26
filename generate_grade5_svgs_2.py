#!/usr/bin/env python3
"""Generate detailed SVG illustrations for Grade 5 Biology lessons 5-12"""

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
# Lesson 5: Экологические факторы и их влияние на живые организмы
# ============================================================
svg5 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#FFF8E1"/><stop offset="100%" stop-color="#FFECB3"/></linearGradient>
<linearGradient id="sunGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#FFF176"/><stop offset="100%" stop-color="#FFD54F"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#F57F17" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#E65100" text-anchor="middle">Экологические факторы</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 5</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#F57F17" stroke-width="1" opacity="0.3"/>

<!-- Central organism -->
<g transform="translate(250,120)">
  <circle cx="0" cy="0" r="30" fill="#81C784" opacity="0.3" stroke="#2E7D32" stroke-width="2"/>
  <path d="M-8,-15 Q0,-25 8,-15 Q15,-5 8,5 Q0,15 -8,5 Q-15,-5 -8,-15" fill="#66BB6A" stroke="#2E7D32" stroke-width="1.5"/>
  <path d="M0,-12 L0,5" stroke="#2E7D32" stroke-width="1"/>
  <path d="M0,-5 L-6,0" stroke="#2E7D32" stroke-width="0.8"/>
  <path d="M0,-5 L6,0" stroke="#2E7D32" stroke-width="0.8"/>
  <text x="0" y="42" font-family="Arial,sans-serif" font-size="8" fill="#1B5E20" text-anchor="middle" font-weight="bold">ОРГАНИЗМ</text>
</g>

<!-- Arrow from factors to organism -->
<line x1="90" y1="80" x2="215" y2="105" stroke="#F57F17" stroke-width="1.5"/>
<line x1="250" y1="80" x2="250" y2="90" stroke="#1565C0" stroke-width="1.5"/>
<line x1="410" y1="80" x2="285" y2="105" stroke="#9C27B0" stroke-width="1.5"/>

<!-- АБИОТИЧЕСКИЕ ФАКТОРЫ -->
<g transform="translate(90,165)">
  <rect x="-70" y="-80" width="140" height="150" rx="8" fill="white" opacity="0.9" stroke="#F57F17" stroke-width="1.5"/>
  <text x="0" y="-63" font-family="Arial,sans-serif" font-size="9" fill="#E65100" text-anchor="middle" font-weight="bold">АБИОТИЧЕСКИЕ</text>
  <line x1="-60" y1="-57" x2="60" y2="-57" stroke="#F57F17" stroke-width="0.5"/>
  
  <!-- Sun (light) -->
  <circle cx="-35" cy="-35" r="10" fill="url(#sunGrad)" stroke="#F9A825" stroke-width="1"/>
  <line x1="-35" y1="-48" x2="-35" y2="-52" stroke="#F9A825" stroke-width="1"/>
  <line x1="-22" y1="-35" x2="-18" y2="-35" stroke="#F9A825" stroke-width="1"/>
  <line x1="-48" y1="-35" x2="-52" y2="-35" stroke="#F9A825" stroke-width="1"/>
  <line x1="-44" y1="-44" x2="-47" y2="-47" stroke="#F9A825" stroke-width="1"/>
  <line x1="-26" y1="-44" x2="-23" y2="-47" stroke="#F9A825" stroke-width="1"/>
  <text x="-10" y="-33" font-family="Arial,sans-serif" font-size="7" fill="#E65100">Свет</text>
  
  <!-- Temperature -->
  <rect x="-42" y="-18" width="5" height="20" rx="2" fill="#FFCDD2" stroke="#C62828" stroke-width="0.8"/>
  <rect x="-41" y="-5" width="3" height="6" fill="#F44336"/>
  <circle cx="-39.5" cy="6" r="3" fill="#F44336" stroke="#C62828" stroke-width="0.8"/>
  <text x="-25" y="-5" font-family="Arial,sans-serif" font-size="7" fill="#E65100">Температура</text>
  
  <!-- Water/Humidity -->
  <path d="M-38,18 Q-35,10 -32,18 Q-35,22 -38,18" fill="#42A5F5" stroke="#1565C0" stroke-width="0.8"/>
  <path d="M-35,18 Q-35,25 -35,30" fill="none" stroke="#42A5F5" stroke-width="0.8"/>
  <text x="-20" y="22" font-family="Arial,sans-serif" font-size="7" fill="#E65100">Вода</text>
  
  <!-- Wind -->
  <path d="M-40,38 Q-30,35 -25,38" fill="none" stroke="#90CAF9" stroke-width="1.5"/>
  <path d="M-38,43 Q-28,40 -23,43" fill="none" stroke="#90CAF9" stroke-width="1.5"/>
  <text x="-10" y="42" font-family="Arial,sans-serif" font-size="7" fill="#E65100">Ветер</text>
  
  <text x="0" y="60" font-family="Arial,sans-serif" font-size="5.5" fill="#999" text-anchor="middle">Факторы неживой природы</text>
</g>

<!-- БИОТИЧЕСКИЕ ФАКТОРЫ -->
<g transform="translate(250,270)">
  <rect x="-70" y="-45" width="140" height="80" rx="8" fill="white" opacity="0.9" stroke="#9C27B0" stroke-width="1.5"/>
  <text x="0" y="-28" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" text-anchor="middle" font-weight="bold">БИОТИЧЕСКИЕ</text>
  <line x1="-60" y1="-22" x2="60" y2="-22" stroke="#9C27B0" stroke-width="0.5"/>
  
  <!-- Fox and rabbit -->
  <ellipse cx="-35" cy="-5" rx="8" ry="5" fill="#FFAB91" stroke="#BF360C" stroke-width="0.8"/>
  <circle cx="-40" cy="-7" r="2" fill="#1B5E20"/>
  <path d="M-43,-10 Q-45,-14 -42,-12" fill="none" stroke="#BF360C" stroke-width="0.6"/>
  <path d="M-27,-5 Q-25,-10 -23,-5" fill="none" stroke="#BF360C" stroke-width="1"/>
  <ellipse cx="-10" cy="-5" rx="6" ry="4" fill="#E0E0E0" stroke="#666" stroke-width="0.8"/>
  <circle cx="-13" cy="-7" r="1.5" fill="#1B5E20"/>
  <path d="M-16,-8 Q-18,-12 -15,-10" fill="none" stroke="#666" stroke-width="0.5"/>
  <path d="M-4,-5 Q-2,-8 0,-5" fill="none" stroke="#666" stroke-width="0.5"/>
  
  <text x="30" y="-8" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle">Хищник —</text>
  <text x="30" y="0" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle">жертва</text>
  
  <text x="0" y="22" font-family="Arial,sans-serif" font-size="5.5" fill="#999" text-anchor="middle">Влияние одних организмов на другие</text>
  <text x="0" y="30" font-family="Arial,sans-serif" font-size="5.5" fill="#999" text-anchor="middle">конкуренция, симбиоз, паразитизм</text>
</g>

<!-- АНТРОПОГЕННЫЕ ФАКТОРЫ -->
<g transform="translate(410,165)">
  <rect x="-70" y="-80" width="140" height="150" rx="8" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1.5"/>
  <text x="0" y="-63" font-family="Arial,sans-serif" font-size="9" fill="#0D47A1" text-anchor="middle" font-weight="bold">АНТРОПОГЕННЫЕ</text>
  <line x1="-60" y1="-57" x2="60" y2="-57" stroke="#1565C0" stroke-width="0.5"/>
  
  <!-- Factory -->
  <rect x="-45" y="-35" width="25" height="30" fill="#90CAF9" opacity="0.5" stroke="#1565C0" stroke-width="1"/>
  <rect x="-50" y="-45" width="8" height="15" fill="#90CAF9" stroke="#1565C0" stroke-width="0.8"/>
  <rect x="-35" y="-50" width="8" height="20" fill="#90CAF9" stroke="#1565C0" stroke-width="0.8"/>
  <!-- Smoke -->
  <path d="M-46,-45 Q-48,-52 -42,-55 Q-38,-58 -40,-62" fill="none" stroke="#9E9E9E" stroke-width="1.5" opacity="0.5"/>
  <path d="M-31,-50 Q-28,-57 -24,-60" fill="none" stroke="#9E9E9E" stroke-width="1.5" opacity="0.5"/>
  <text x="-5" y="-30" font-family="Arial,sans-serif" font-size="6" fill="#0D47A1">Загрязнение</text>
  
  <!-- Tractor/deforestation -->
  <rect x="-45" y="5" width="20" height="10" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
  <rect x="-50" y="8" width="5" height="7" fill="#E65100" stroke="#BF360C" stroke-width="0.5"/>
  <circle cx="-38" cy="18" r="4" fill="#8D6E63" stroke="#5D4037" stroke-width="0.8"/>
  <circle cx="-28" cy="18" r="4" fill="#8D6E63" stroke="#5D4037" stroke-width="0.8"/>
  <text x="-5" y="12" font-family="Arial,sans-serif" font-size="6" fill="#0D47A1">Вырубка</text>
  
  <!-- Urbanization -->
  <rect x="-45" y="30" width="10" height="15" fill="#B0BEC5" stroke="#546E7A" stroke-width="0.5"/>
  <rect x="-35" y="35" width="10" height="10" fill="#B0BEC5" stroke="#546E7A" stroke-width="0.5"/>
  <rect x="-25" y="32" width="10" height="13" fill="#B0BEC5" stroke="#546E7A" stroke-width="0.5"/>
  <text x="15" y="40" font-family="Arial,sans-serif" font-size="6" fill="#0D47A1">Города</text>
  
  <text x="0" y="60" font-family="Arial,sans-serif" font-size="5.5" fill="#999" text-anchor="middle">Влияние человека</text>
  <text x="0" y="68" font-family="Arial,sans-serif" font-size="5.5" fill="#999" text-anchor="middle">на природу</text>
</g>

<!-- Connecting arrow from organism to biotic -->
<line x1="250" y1="150" x2="250" y2="220" stroke="#9C27B0" stroke-width="1.5"/>
</svg>'''

# ============================================================
# Lesson 6: Устройство увеличительных приборов
# ============================================================
svg6 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#E8EAF6"/><stop offset="100%" stop-color="#C5CAE9"/></linearGradient>
<linearGradient id="lensGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#E1F5FE"/><stop offset="100%" stop-color="#81D4FA"/></linearGradient>
<linearGradient id="metalGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#78909C"/><stop offset="100%" stop-color="#546E7A"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#283593" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#1A237E" text-anchor="middle">Устройство увеличительных приборов</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 6</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#283593" stroke-width="1" opacity="0.3"/>

<!-- Лупа (hand lens) -->
<g transform="translate(100,175)">
  <rect x="-65" y="-100" width="130" height="185" rx="8" fill="white" opacity="0.9" stroke="#546E7A" stroke-width="1.5"/>
  <text x="0" y="-82" font-family="Arial,sans-serif" font-size="10" fill="#37474F" text-anchor="middle" font-weight="bold">ЛУПА</text>
  <line x1="-55" y1="-76" x2="55" y2="-76" stroke="#546E7A" stroke-width="0.5"/>
  
  <!-- Lens frame -->
  <circle cx="0" cy="-30" r="35" fill="none" stroke="#546E7A" stroke-width="3"/>
  <circle cx="0" cy="-30" r="32" fill="url(#lensGrad)" opacity="0.3"/>
  <!-- Lens shine -->
  <path d="M-12,-50 Q-8,-55 -4,-50" fill="none" stroke="white" stroke-width="2" opacity="0.6"/>
  <!-- Handle -->
  <rect x="-5" y="5" width="10" height="40" rx="3" fill="url(#metalGrad)" stroke="#37474F" stroke-width="1"/>
  <rect x="-3" y="45" width="6" height="15" rx="2" fill="#546E7A"/>
  
  <!-- Label arrows -->
  <line x1="35" y1="-30" x2="48" y2="-50" stroke="#37474F" stroke-width="0.8"/>
  <text x="52" y="-50" font-family="Arial,sans-serif" font-size="6" fill="#37474F">Линза</text>
  <line x1="5" y1="25" x2="48" y2="25" stroke="#37474F" stroke-width="0.8"/>
  <text x="52" y="25" font-family="Arial,sans-serif" font-size="6" fill="#37474F">Ручка</text>
  
  <!-- Magnification note -->
  <rect x="-50" y="68" width="100" height="18" rx="3" fill="#E8EAF6" stroke="#546E7A" stroke-width="0.5"/>
  <text x="0" y="81" font-family="Arial,sans-serif" font-size="7" fill="#37474F" text-anchor="middle" font-weight="bold">Увеличение: 2-25×</text>
</g>

<!-- Микроскоп -->
<g transform="translate(310,175)">
  <rect x="-80" y="-100" width="160" height="185" rx="8" fill="white" opacity="0.9" stroke="#283593" stroke-width="1.5"/>
  <text x="0" y="-82" font-family="Arial,sans-serif" font-size="10" fill="#1A237E" text-anchor="middle" font-weight="bold">МИКРОСКОП</text>
  <line x1="-70" y1="-76" x2="70" y2="-76" stroke="#283593" stroke-width="0.5"/>
  
  <!-- Eyepiece -->
  <rect x="-8" y="-68" width="16" height="10" rx="2" fill="#7986CB" stroke="#283593" stroke-width="1"/>
  <rect x="-6" y="-66" width="12" height="5" rx="1" fill="url(#lensGrad)"/>
  <line x1="10" y1="-63" x2="50" y2="-63" stroke="#1A237E" stroke-width="0.8"/>
  <text x="55" y="-61" font-family="Arial,sans-serif" font-size="5.5" fill="#1A237E">Окуляр</text>
  
  <!-- Tube -->
  <rect x="-5" y="-58" width="10" height="40" rx="1" fill="#5C6BC0" stroke="#283593" stroke-width="1"/>
  
  <!-- Revolving nosepiece -->
  <path d="M-15,-18 Q0,-12 15,-18" fill="none" stroke="#283593" stroke-width="2"/>
  
  <!-- Objectives -->
  <rect x="-18" y="-18" width="5" height="12" rx="1" fill="#7986CB" stroke="#283593" stroke-width="0.8"/>
  <rect x="-3" y="-15" width="5" height="15" rx="1" fill="#5C6BC0" stroke="#283593" stroke-width="0.8"/>
  <rect x="12" y="-18" width="5" height="12" rx="1" fill="#7986CB" stroke="#283593" stroke-width="0.8"/>
  <line x1="18" y1="-10" x2="50" y2="-10" stroke="#1A237E" stroke-width="0.8"/>
  <text x="55" y="-8" font-family="Arial,sans-serif" font-size="5.5" fill="#1A237E">Объективы</text>
  
  <!-- Stage -->
  <rect x="-30" y="2" width="60" height="5" rx="1" fill="#9FA8DA" stroke="#283593" stroke-width="1"/>
  <!-- Slide on stage -->
  <rect x="-15" y="0" width="30" height="3" fill="url(#lensGrad)" stroke="#283593" stroke-width="0.5"/>
  <!-- Clips -->
  <rect x="-28" y="0" width="8" height="2" fill="#546E7A"/>
  <rect x="20" y="0" width="8" height="2" fill="#546E7A"/>
  <line x1="32" y1="5" x2="50" y2="5" stroke="#1A237E" stroke-width="0.8"/>
  <text x="55" y="7" font-family="Arial,sans-serif" font-size="5.5" fill="#1A237E">Предметный</text>
  <text x="55" y="14" font-family="Arial,sans-serif" font-size="5.5" fill="#1A237E">столик</text>
  
  <!-- Arm -->
  <rect x="5" y="-58" width="8" height="75" rx="1" fill="#5C6BC0" stroke="#283593" stroke-width="1"/>
  
  <!-- Coarse focus -->
  <circle cx="13" cy="-15" r="6" fill="#7986CB" stroke="#283593" stroke-width="1"/>
  <line x1="19" y1="-15" x2="50" y2="-30" stroke="#1A237E" stroke-width="0.8"/>
  <text x="55" y="-28" font-family="Arial,sans-serif" font-size="5.5" fill="#1A237E">Винт грубой</text>
  <text x="55" y="-21" font-family="Arial,sans-serif" font-size="5.5" fill="#1A237E">наводки</text>
  
  <!-- Fine focus -->
  <circle cx="13" cy="5" r="4" fill="#9FA8DA" stroke="#283593" stroke-width="0.8"/>
  <line x1="17" y1="5" x2="50" y2="18" stroke="#1A237E" stroke-width="0.8"/>
  <text x="55" y="20" font-family="Arial,sans-serif" font-size="5.5" fill="#1A237E">Микрометрич.</text>
  <text x="55" y="27" font-family="Arial,sans-serif" font-size="5.5" fill="#1A237E">винт</text>
  
  <!-- Mirror/Light -->
  <ellipse cx="-5" cy="15" rx="12" ry="3" fill="#FFD54F" stroke="#F9A825" stroke-width="0.8" opacity="0.6"/>
  <text x="-5" y="25" font-family="Arial,sans-serif" font-size="5" fill="#1A237E" text-anchor="middle">Зеркало/Подсветка</text>
  
  <!-- Base -->
  <rect x="-35" y="18" width="70" height="8" rx="2" fill="#5C6BC0" stroke="#283593" stroke-width="1"/>
  
  <!-- Magnification -->
  <rect x="-65" y="55" width="130" height="25" rx="3" fill="#E8EAF6" stroke="#283593" stroke-width="0.5"/>
  <text x="0" y="68" font-family="Arial,sans-serif" font-size="7" fill="#1A237E" text-anchor="middle" font-weight="bold">Увеличение: окуляр × объектив</text>
  <text x="0" y="78" font-family="Arial,sans-serif" font-size="6" fill="#1A237E" text-anchor="middle">Например: 10× × 40× = 400×</text>
</g>

<!-- Bottom tips -->
<rect x="30" y="310" width="440" height="25" rx="6" fill="white" opacity="0.9" stroke="#283593" stroke-width="1"/>
<text x="250" y="327" font-family="Arial,sans-serif" font-size="7" fill="#1A237E" text-anchor="middle" font-weight="bold">Правила: обе руки · свет сбоку · начинать с малого увеличения · не касаться линз</text>
</svg>'''

# ============================================================
# Lesson 7: Строение клетки
# ============================================================
svg7 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#E8F5E9"/><stop offset="100%" stop-color="#C8E6C9"/></linearGradient>
<linearGradient id="cellGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#A5D6A7"/><stop offset="100%" stop-color="#66BB6A"/></linearGradient>
<linearGradient id="nucleusGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#66BB6A"/><stop offset="100%" stop-color="#2E7D32"/></linearGradient>
<linearGradient id="animalGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#FFAB91"/><stop offset="100%" stop-color="#FF8A65"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#2E7D32" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#1B5E20" text-anchor="middle">Строение клетки</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 7</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#2E7D32" stroke-width="1" opacity="0.3"/>

<!-- Plant cell -->
<g transform="translate(145,185)">
  <text x="0" y="-85" font-family="Arial,sans-serif" font-size="10" fill="#1B5E20" text-anchor="middle" font-weight="bold">Растительная клетка</text>
  
  <!-- Cell wall -->
  <rect x="-90" y="-75" width="180" height="155" rx="4" fill="none" stroke="#2E7D32" stroke-width="3"/>
  <!-- Cell membrane -->
  <rect x="-85" y="-70" width="170" height="145" rx="3" fill="url(#cellGrad)" opacity="0.3" stroke="#4CAF50" stroke-width="1.5" stroke-dasharray="4,2"/>
  
  <!-- Nucleus -->
  <ellipse cx="-20" cy="-20" rx="28" ry="22" fill="url(#nucleusGrad)" opacity="0.5" stroke="#1B5E20" stroke-width="1.5"/>
  <ellipse cx="-20" cy="-20" rx="12" ry="9" fill="#1B5E20" opacity="0.4"/>
  <text x="-20" y="-17" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle" font-weight="bold">Ядро</text>
  <text x="-20" y="-9" font-family="Arial,sans-serif" font-size="5" fill="#E8F5E9" text-anchor="middle">ядрышко</text>
  
  <!-- Chloroplasts -->
  <ellipse cx="40" cy="-40" rx="14" ry="8" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
  <path d="M30,-40 L50,-40" stroke="#2E7D32" stroke-width="0.5"/>
  <path d="M35,-44 L45,-36" stroke="#2E7D32" stroke-width="0.5"/>
  <text x="40" y="-28" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle">Хлоропласт</text>
  
  <ellipse cx="35" cy="15" rx="12" ry="7" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
  <path d="M26,15 L44,15" stroke="#2E7D32" stroke-width="0.5"/>
  
  <!-- Vacuole -->
  <ellipse cx="40" cy="45" rx="35" ry="20" fill="#C8E6C9" opacity="0.5" stroke="#4CAF50" stroke-width="1.5"/>
  <text x="40" y="48" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Вакуоль</text>
  <text x="40" y="56" font-family="Arial,sans-serif" font-size="4.5" fill="#4CAF50" text-anchor="middle">клеточный сок</text>
  
  <!-- Mitochondria -->
  <ellipse cx="-55" cy="30" rx="14" ry="7" fill="#FF9800" opacity="0.5" stroke="#E65100" stroke-width="1"/>
  <path d="M-64,30 Q-58,26 -55,30 Q-52,34 -46,30" fill="none" stroke="#E65100" stroke-width="0.8"/>
  <text x="-55" y="43" font-family="Arial,sans-serif" font-size="4.5" fill="#E65100" text-anchor="middle">Митохондрия</text>
  
  <!-- ER -->
  <path d="M-55,-5 Q-45,0 -50,10 Q-55,20 -45,25" fill="none" stroke="#795548" stroke-width="1.2"/>
  <path d="M-52,-3 Q-42,2 -47,12 Q-52,22 -42,27" fill="none" stroke="#795548" stroke-width="1.2"/>
  
  <!-- Ribosomes -->
  <circle cx="-50" cy="-5" r="1.5" fill="#9C27B0"/>
  <circle cx="-45" cy="5" r="1.5" fill="#9C27B0"/>
  <circle cx="-50" cy="15" r="1.5" fill="#9C27B0"/>
  
  <!-- Label: Cell wall -->
  <line x1="-90" y1="-50" x2="-105" y2="-60" stroke="#2E7D32" stroke-width="0.8"/>
  <text x="-108" y="-62" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="end">Клеточная</text>
  <text x="-108" y="-56" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="end">стенка</text>
  
  <!-- Label: Membrane -->
  <line x1="-85" y1="50" x2="-105" y2="60" stroke="#4CAF50" stroke-width="0.8"/>
  <text x="-108" y="62" font-family="Arial,sans-serif" font-size="5" fill="#4CAF50" text-anchor="end">Мембрана</text>
</g>

<!-- Animal cell -->
<g transform="translate(385,185)">
  <text x="0" y="-85" font-family="Arial,sans-serif" font-size="10" fill="#BF360C" text-anchor="middle" font-weight="bold">Животная клетка</text>
  
  <!-- Cell membrane only (no wall) -->
  <ellipse cx="0" cy="0" rx="80" ry="65" fill="url(#animalGrad)" opacity="0.3" stroke="#E64A19" stroke-width="2"/>
  <ellipse cx="0" cy="0" rx="76" ry="61" fill="none" stroke="#FF8A65" stroke-width="1" stroke-dasharray="3,2"/>
  
  <!-- Nucleus -->
  <ellipse cx="-10" cy="-10" rx="25" ry="20" fill="#FF8A65" opacity="0.5" stroke="#BF360C" stroke-width="1.5"/>
  <ellipse cx="-10" cy="-10" rx="10" ry="8" fill="#BF360C" opacity="0.4"/>
  <text x="-10" y="-7" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle" font-weight="bold">Ядро</text>
  
  <!-- Mitochondria -->
  <ellipse cx="35" cy="-25" rx="14" ry="7" fill="#FF9800" opacity="0.5" stroke="#E65100" stroke-width="1"/>
  <path d="M26,-25 Q32,-29 35,-25 Q38,-21 44,-25" fill="none" stroke="#E65100" stroke-width="0.8"/>
  
  <ellipse cx="-40" cy="25" rx="12" ry="6" fill="#FF9800" opacity="0.5" stroke="#E65100" stroke-width="1"/>
  
  <!-- ER -->
  <path d="M25,5 Q35,0 30,10 Q25,20 35,25" fill="none" stroke="#795548" stroke-width="1.2"/>
  <path d="M28,7 Q38,2 33,12 Q28,22 38,27" fill="none" stroke="#795548" stroke-width="1.2"/>
  
  <!-- Lysosomes -->
  <circle cx="-35" cy="-30" r="6" fill="#F44336" opacity="0.4" stroke="#C62828" stroke-width="1"/>
  <text x="-35" y="-28" font-family="Arial,sans-serif" font-size="4" fill="white" text-anchor="middle">Лиз</text>
  
  <circle cx="45" cy="15" r="5" fill="#F44336" opacity="0.4" stroke="#C62828" stroke-width="1"/>
  
  <!-- Centrioles -->
  <rect x="20" y="35" width="8" height="3" rx="1" fill="#546E7A" stroke="#37474F" stroke-width="0.5"/>
  <rect x="22" y="40" width="8" height="3" rx="1" fill="#546E7A" stroke="#37474F" stroke-width="0.5" transform="rotate(90,26,41.5)"/>
  <text x="26" y="52" font-family="Arial,sans-serif" font-size="4.5" fill="#37474F" text-anchor="middle">Центриоли</text>
  
  <!-- Ribosomes -->
  <circle cx="15" cy="-10" r="1.5" fill="#9C27B0"/>
  <circle cx="10" cy="-5" r="1.5" fill="#9C27B0"/>
  <circle cx="20" cy="0" r="1.5" fill="#9C27B0"/>
  
  <!-- No chloroplasts, no vacuole, no cell wall labels -->
  <text x="0" y="50" font-family="Arial,sans-serif" font-size="5" fill="#BF360C" text-anchor="middle">Нет: клеточной стенки,</text>
  <text x="0" y="58" font-family="Arial,sans-serif" font-size="5" fill="#BF360C" text-anchor="middle">хлоропластов, вакуоли</text>
  
  <!-- Label: Membrane -->
  <line x1="70" y1="-30" x2="85" y2="-45" stroke="#E64A19" stroke-width="0.8"/>
  <text x="88" y="-45" font-family="Arial,sans-serif" font-size="5" fill="#E64A19">Мембрана</text>
</g>

<!-- Bottom: common parts -->
<rect x="30" y="305" width="440" height="30" rx="6" fill="white" opacity="0.9" stroke="#2E7D32" stroke-width="1"/>
<text x="250" y="318" font-family="Arial,sans-serif" font-size="7" fill="#1B5E20" text-anchor="middle" font-weight="bold">Общие части клетки: оболочка (мембрана) · цитоплазма · ядро</text>
<text x="250" y="330" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Органоиды: митохондрии, ЭПС, рибосомы, лизосомы</text>
</svg>'''

# ============================================================
# Lesson 8: Химический состав клетки
# ============================================================
svg8 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#FFF3E0"/><stop offset="100%" stop-color="#FFE0B2"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#E65100" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#BF360C" text-anchor="middle">Химический состав клетки</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 8</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#E65100" stroke-width="1" opacity="0.3"/>

<!-- Pie chart: Cell composition -->
<g transform="translate(120,180)">
  <text x="0" y="-90" font-family="Arial,sans-serif" font-size="9" fill="#BF360C" text-anchor="middle" font-weight="bold">Состав клетки</text>
  
  <!-- Water 70-80% -->
  <path d="M0,0 L0,-70 A70,70 0 0,1 66.6,23 Z" fill="#42A5F5" opacity="0.7" stroke="#1565C0" stroke-width="1"/>
  <text x="35" y="-30" font-family="Arial,sans-serif" font-size="7" fill="#0D47A1" font-weight="bold">Вода</text>
  <text x="35" y="-20" font-family="Arial,sans-serif" font-size="6" fill="#0D47A1">70-80%</text>
  
  <!-- Organic 20-30% -->
  <path d="M0,0 L66.6,23 A70,70 0 0,1 -30,63 Z" fill="#66BB6A" opacity="0.7" stroke="#2E7D32" stroke-width="1"/>
  <text x="15" y="40" font-family="Arial,sans-serif" font-size="7" fill="#1B5E20" font-weight="bold">Орган.</text>
  <text x="15" y="50" font-family="Arial,sans-serif" font-size="6" fill="#1B5E20">20-30%</text>
  
  <!-- Minerals 1-1.5% -->
  <path d="M0,0 L-30,63 A70,70 0 0,1 -60,-35 Z" fill="#FFB74D" opacity="0.7" stroke="#E65100" stroke-width="1"/>
  <text x="-40" y="15" font-family="Arial,sans-serif" font-size="6" fill="#BF360C" font-weight="bold">Минер.</text>
  <text x="-40" y="24" font-family="Arial,sans-serif" font-size="5" fill="#BF360C">1-1.5%</text>
  
  <!-- Water molecule -->
  <g transform="translate(0,85)">
    <circle cx="-8" cy="0" r="6" fill="#F44336" opacity="0.6" stroke="#C62828" stroke-width="0.8"/>
    <text x="-8" y="3" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle">O</text>
    <line x1="-3" y1="-2" x2="5" y2="-6" stroke="#999" stroke-width="1"/>
    <circle cx="8" cy="-8" r="4" fill="#E0E0E0" stroke="#999" stroke-width="0.8"/>
    <text x="8" y="-6" font-family="Arial,sans-serif" font-size="4" fill="#666" text-anchor="middle">H</text>
    <line x1="-3" y1="2" x2="5" y2="6" stroke="#999" stroke-width="1"/>
    <circle cx="8" cy="8" r="4" fill="#E0E0E0" stroke="#999" stroke-width="0.8"/>
    <text x="8" y="10" font-family="Arial,sans-serif" font-size="4" fill="#666" text-anchor="middle">H</text>
  </g>
</g>

<!-- Organic substances detail -->
<g transform="translate(350,180)">
  <rect x="-110" y="-95" width="220" height="185" rx="8" fill="white" opacity="0.9" stroke="#E65100" stroke-width="1.5"/>
  <text x="0" y="-78" font-family="Arial,sans-serif" font-size="9" fill="#BF360C" text-anchor="middle" font-weight="bold">Органические вещества</text>
  <line x1="-100" y1="-72" x2="100" y2="-72" stroke="#E65100" stroke-width="0.5"/>
  
  <!-- Белки (Proteins) -->
  <rect x="-95" y="-65" width="100" height="35" rx="4" fill="#FFEBEE" stroke="#C62828" stroke-width="1"/>
  <path d="M-80,-50 Q-75,-58 -70,-50 Q-65,-42 -60,-50" fill="none" stroke="#C62828" stroke-width="1.5"/>
  <path d="M-80,-45 Q-75,-38 -70,-45" fill="none" stroke="#C62828" stroke-width="1"/>
  <text x="20" y="-50" font-family="Arial,sans-serif" font-size="7" fill="#C62828" font-weight="bold">Белки</text>
  <text x="20" y="-40" font-family="Arial,sans-serif" font-size="5" fill="#C62828">аминокислоты</text>
  
  <!-- Жиры (Lipids) -->
  <rect x="5" y="-65" width="100" height="35" rx="4" fill="#FFF3E0" stroke="#E65100" stroke-width="1"/>
  <path d="M25,-50 L20,-45 L25,-40" fill="none" stroke="#E65100" stroke-width="1.2"/>
  <path d="M28,-50 L23,-45 L28,-40" fill="none" stroke="#E65100" stroke-width="1.2"/>
  <path d="M31,-50 L26,-45 L31,-40" fill="none" stroke="#E65100" stroke-width="1.2"/>
  <text x="70" y="-50" font-family="Arial,sans-serif" font-size="7" fill="#E65100" font-weight="bold">Жиры</text>
  <text x="70" y="-40" font-family="Arial,sans-serif" font-size="5" fill="#E65100">глицерин + к-ты</text>
  
  <!-- Углеводы (Carbohydrates) -->
  <rect x="-95" y="-25" width="100" height="35" rx="4" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
  <path d="M-80,-10 L-75,-15 L-70,-10 L-65,-15 L-60,-10" fill="none" stroke="#2E7D32" stroke-width="1.5"/>
  <circle cx="-58" cy="-10" r="4" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <text x="20" y="-10" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" font-weight="bold">Углеводы</text>
  <text x="20" y="0" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">C, H, O</text>
  
  <!-- Нуклеиновые кислоты (Nucleic acids) -->
  <rect x="5" y="-25" width="100" height="35" rx="4" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
  <path d="M25,-15 C28,-10 22,-5 25,0" fill="none" stroke="#1565C0" stroke-width="1.5"/>
  <path d="M30,-15 C27,-10 33,-5 30,0" fill="none" stroke="#C62828" stroke-width="1.5"/>
  <line x1="26" y1="-12" x2="29" y2="-12" stroke="#666" stroke-width="0.8"/>
  <line x1="24" y1="-7" x2="31" y2="-7" stroke="#666" stroke-width="0.8"/>
  <line x1="26" y1="-2" x2="29" y2="-2" stroke="#666" stroke-width="0.8"/>
  <text x="70" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" font-weight="bold">ДНК</text>
  <text x="70" y="0" font-family="Arial,sans-serif" font-size="5" fill="#1565C0">нуклеотиды</text>
  
  <!-- Functions summary -->
  <rect x="-95" y="18" width="200" height="60" rx="4" fill="#FFF8E1" stroke="#F9A825" stroke-width="0.5"/>
  <text x="5" y="33" font-family="Arial,sans-serif" font-size="6" fill="#BF360C" text-anchor="middle" font-weight="bold">Функции органических веществ:</text>
  <text x="5" y="44" font-family="Arial,sans-serif" font-size="5.5" fill="#666" text-anchor="middle">Белки — строительная, ферменты</text>
  <text x="5" y="53" font-family="Arial,sans-serif" font-size="5.5" fill="#666" text-anchor="middle">Жиры — запас энергии, защита</text>
  <text x="5" y="62" font-family="Arial,sans-serif" font-size="5.5" fill="#666" text-anchor="middle">Углеводы — энергия, ДНК — наследств.</text>
</g>

<!-- Bottom -->
<rect x="30" y="310" width="440" height="25" rx="6" fill="white" opacity="0.9" stroke="#E65100" stroke-width="1"/>
<text x="250" y="327" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle" font-weight="bold">Неорганические: вода (80%) + минеральные соли (1%) | Органические: белки, жиры, углеводы, нуклеиновые кислоты</text>
</svg>'''

# ============================================================
# Lesson 9: Жизнедеятельность клетки, её деление и рост
# ============================================================
svg9 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#FCE4EC"/><stop offset="100%" stop-color="#F8BBD0"/></linearGradient>
<linearGradient id="cellGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#F48FB1"/><stop offset="100%" stop-color="#E91E63"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#880E4F" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#880E4F" text-anchor="middle">Жизнедеятельность клетки: деление и рост</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 9</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#880E4F" stroke-width="1" opacity="0.3"/>

<!-- Cell division stages -->
<!-- Stage 1: Interphase -->
<g transform="translate(80,130)">
  <rect x="-55" y="-55" width="110" height="100" rx="8" fill="white" opacity="0.9" stroke="#880E4F" stroke-width="1.5"/>
  <text x="0" y="-38" font-family="Arial,sans-serif" font-size="7" fill="#880E4F" text-anchor="middle" font-weight="bold">ИНТЕРФАЗА</text>
  <line x1="-45" y1="-32" x2="45" y2="-32" stroke="#880E4F" stroke-width="0.5"/>
  <!-- Cell with nucleus -->
  <ellipse cx="0" cy="5" rx="35" ry="25" fill="url(#cellGrad)" opacity="0.2" stroke="#880E4F" stroke-width="1.5"/>
  <ellipse cx="0" cy="3" rx="12" ry="9" fill="#880E4F" opacity="0.3" stroke="#880E4F" stroke-width="1"/>
  <!-- Chromatin (threadlike) -->
  <path d="M-5,-2 Q0,-6 5,-2 Q3,2 0,5 Q-3,2 -5,-2" fill="none" stroke="#880E4F" stroke-width="0.8"/>
  <text x="0" y="30" font-family="Arial,sans-serif" font-size="5" fill="#880E4F" text-anchor="middle">Рост, синтез ДНК</text>
</g>

<!-- Arrow -->
<path d="M140,130 L160,130" fill="none" stroke="#880E4F" stroke-width="2" marker-end="url(#arrow)"/>

<!-- Stage 2: Prophase -->
<g transform="translate(220,130)">
  <rect x="-55" y="-55" width="110" height="100" rx="8" fill="white" opacity="0.9" stroke="#880E4F" stroke-width="1.5"/>
  <text x="0" y="-38" font-family="Arial,sans-serif" font-size="7" fill="#880E4F" text-anchor="middle" font-weight="bold">ПРОФАЗА</text>
  <line x1="-45" y1="-32" x2="45" y2="-32" stroke="#880E4F" stroke-width="0.5"/>
  <!-- Cell with chromosomes visible -->
  <ellipse cx="0" cy="5" rx="35" ry="25" fill="url(#cellGrad)" opacity="0.2" stroke="#880E4F" stroke-width="1.5"/>
  <!-- Chromosomes (X shapes) -->
  <path d="M-10,-8 L-5,2 M-5,-8 L-10,2" stroke="#C62828" stroke-width="2"/>
  <path d="M5,-8 L10,2 M10,-8 L5,2" stroke="#C62828" stroke-width="2"/>
  <path d="M-2,-6 L2,4 M2,-6 L-2,4" stroke="#1565C0" stroke-width="2"/>
  <!-- Dissolving nuclear membrane -->
  <ellipse cx="0" cy="3" rx="15" ry="11" fill="none" stroke="#880E4F" stroke-width="0.8" stroke-dasharray="2,2" opacity="0.4"/>
  <text x="0" y="30" font-family="Arial,sans-serif" font-size="5" fill="#880E4F" text-anchor="middle">Хромосомы видны</text>
</g>

<!-- Arrow -->
<path d="M280,130 L300,130" fill="none" stroke="#880E4F" stroke-width="2"/>

<!-- Stage 3: Metaphase/Anaphase -->
<g transform="translate(370,130)">
  <rect x="-55" y="-55" width="110" height="100" rx="8" fill="white" opacity="0.9" stroke="#880E4F" stroke-width="1.5"/>
  <text x="0" y="-38" font-family="Arial,sans-serif" font-size="7" fill="#880E4F" text-anchor="middle" font-weight="bold">МЕТА/АНАФАЗА</text>
  <line x1="-45" y1="-32" x2="45" y2="-32" stroke="#880E4F" stroke-width="0.5"/>
  <!-- Cell elongating -->
  <ellipse cx="0" cy="5" rx="35" ry="25" fill="url(#cellGrad)" opacity="0.2" stroke="#880E4F" stroke-width="1.5"/>
  <!-- Spindle fibers -->
  <line x1="-20" y1="-15" x2="-20" y2="15" stroke="#9C27B0" stroke-width="0.5" opacity="0.6"/>
  <line x1="20" y1="-15" x2="20" y2="15" stroke="#9C27B0" stroke-width="0.5" opacity="0.6"/>
  <line x1="0" y1="-15" x2="0" y2="15" stroke="#9C27B0" stroke-width="0.5" opacity="0.6"/>
  <!-- Chromosomes separating -->
  <path d="M-15,-8 L-12,0 M-12,-8 L-15,0" stroke="#C62828" stroke-width="1.5"/>
  <path d="M-15,5 L-12,13 M-12,5 L-15,13" stroke="#C62828" stroke-width="1.5"/>
  <path d="M10,-8 L13,0 M13,-8 L10,0" stroke="#1565C0" stroke-width="1.5"/>
  <path d="M10,5 L13,13 M13,5 L10,13" stroke="#1565C0" stroke-width="1.5"/>
  <text x="0" y="30" font-family="Arial,sans-serif" font-size="5" fill="#880E4F" text-anchor="middle">Хромосомы расходятся</text>
</g>

<!-- Final: Two daughter cells -->
<g transform="translate(250,275)">
  <rect x="-120" y="-35" width="240" height="65" rx="8" fill="white" opacity="0.9" stroke="#880E4F" stroke-width="1.5"/>
  <text x="0" y="-18" font-family="Arial,sans-serif" font-size="7" fill="#880E4F" text-anchor="middle" font-weight="bold">ТЕЛОФАЗА — Две дочерние клетки</text>
  <!-- Left daughter cell -->
  <ellipse cx="-45" cy="5" rx="30" ry="18" fill="url(#cellGrad)" opacity="0.2" stroke="#880E4F" stroke-width="1.5"/>
  <ellipse cx="-45" cy="3" rx="8" ry="6" fill="#880E4F" opacity="0.3" stroke="#880E4F" stroke-width="0.8"/>
  <!-- Right daughter cell -->
  <ellipse cx="45" cy="5" rx="30" ry="18" fill="url(#cellGrad)" opacity="0.2" stroke="#880E4F" stroke-width="1.5"/>
  <ellipse cx="45" cy="3" rx="8" ry="6" fill="#880E4F" opacity="0.3" stroke="#880E4F" stroke-width="0.8"/>
  <!-- Arrow between -->
  <text x="0" y="8" font-family="Arial,sans-serif" font-size="6" fill="#880E4F" text-anchor="middle">=</text>
  <text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#666" text-anchor="middle">Каждая получает копию ДНК</text>
</g>

<!-- Life processes -->
<rect x="30" y="55" width="440" height="20" rx="4" fill="white" opacity="0.7" stroke="#880E4F" stroke-width="0.5"/>
<text x="250" y="69" font-family="Arial,sans-serif" font-size="7" fill="#880E4F" text-anchor="middle" font-weight="bold">Процессы жизнедеятельности: обмен веществ · биосинтез · дыхание · рост · деление</text>
</svg>'''

# ============================================================
# Lesson 10: Ткани
# ============================================================
svg10 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#EFEBE9"/><stop offset="100%" stop-color="#D7CCC8"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#5D4037" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#3E2723" text-anchor="middle">Ткани растений и животных</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 10</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#5D4037" stroke-width="1" opacity="0.3"/>

<!-- Растительные ткани -->
<g transform="translate(130,185)">
  <text x="0" y="-110" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle" font-weight="bold">Ткани растений</text>
  
  <!-- Покровная ткань -->
  <rect x="-90" y="-95" width="80" height="60" rx="6" fill="white" opacity="0.9" stroke="#2E7D32" stroke-width="1"/>
  <text x="-50" y="-80" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Покровная</text>
  <!-- Brick-like cells -->
  <rect x="-80" y="-72" width="14" height="10" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <rect x="-64" y="-72" width="14" height="10" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <rect x="-48" y="-72" width="14" height="10" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <rect x="-72" y="-62" width="14" height="10" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.5"/>
  <rect x="-56" y="-62" width="14" height="10" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.5"/>
  <rect x="-40" y="-62" width="14" height="10" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.5"/>
  <rect x="-80" y="-52" width="14" height="10" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <rect x="-64" y="-52" width="14" height="10" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  <rect x="-48" y="-52" width="14" height="10" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
  
  <!-- Образовательная ткань -->
  <rect x="10" y="-95" width="80" height="60" rx="6" fill="white" opacity="0.9" stroke="#FF9800" stroke-width="1"/>
  <text x="50" y="-80" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">Образовательная</text>
  <!-- Small dividing cells -->
  <circle cx="25" cy="-65" r="5" fill="#FFE0B2" stroke="#E65100" stroke-width="0.5"/>
  <circle cx="38" cy="-65" r="5" fill="#FFCC80" stroke="#E65100" stroke-width="0.5"/>
  <circle cx="51" cy="-65" r="5" fill="#FFE0B2" stroke="#E65100" stroke-width="0.5"/>
  <circle cx="64" cy="-65" r="5" fill="#FFCC80" stroke="#E65100" stroke-width="0.5"/>
  <circle cx="32" cy="-55" r="5" fill="#FFCC80" stroke="#E65100" stroke-width="0.5"/>
  <circle cx="45" cy="-55" r="5" fill="#FFE0B2" stroke="#E65100" stroke-width="0.5"/>
  <circle cx="58" cy="-55" r="5" fill="#FFCC80" stroke="#E65100" stroke-width="0.5"/>
  <circle cx="25" cy="-45" r="5" fill="#FFE0B2" stroke="#E65100" stroke-width="0.5"/>
  <circle cx="38" cy="-45" r="5" fill="#FFCC80" stroke="#E65100" stroke-width="0.5"/>
  <circle cx="51" cy="-45" r="5" fill="#FFE0B2" stroke="#E65100" stroke-width="0.5"/>
  <!-- Some cells dividing (dots inside) -->
  <path d="M23,-67 L27,-63 M27,-67 L23,-63" stroke="#E65100" stroke-width="0.5"/>
  <path d="M49,-57 L53,-53 M53,-57 L49,-53" stroke="#E65100" stroke-width="0.5"/>
  
  <!-- Проводящая ткань -->
  <rect x="-90" y="-28" width="80" height="60" rx="6" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1"/>
  <text x="-50" y="-13" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">Проводящая</text>
  <!-- Vessel tubes -->
  <rect x="-82" y="-5" width="10" height="30" rx="2" fill="#90CAF9" stroke="#1565C0" stroke-width="0.8"/>
  <line x1="-82" y1="0" x2="-72" y2="0" stroke="#1565C0" stroke-width="0.5"/>
  <line x1="-82" y1="8" x2="-72" y2="8" stroke="#1565C0" stroke-width="0.5"/>
  <line x1="-82" y1="16" x2="-72" y2="16" stroke="#1565C0" stroke-width="0.5"/>
  <rect x="-68" y="-5" width="10" height="30" rx="2" fill="#BBDEFB" stroke="#1565C0" stroke-width="0.8"/>
  <!-- Arrows showing flow -->
  <path d="M-77,5 L-77,-3" fill="none" stroke="#0D47A1" stroke-width="0.8"/>
  <polygon points="-77,-3 -79,0 -75,0" fill="#0D47A1"/>
  <path d="M-63,5 L-63,13" fill="none" stroke="#0D47A1" stroke-width="0.8"/>
  <polygon points="-63,13 -65,10 -61,10" fill="#0D47A1"/>
  <text x="-50" y="5" font-family="Arial,sans-serif" font-size="5" fill="#1565C0">Сосуды</text>
  <text x="-50" y="13" font-family="Arial,sans-serif" font-size="5" fill="#1565C0">Ситовидные</text>
  <text x="-50" y="20" font-family="Arial,sans-serif" font-size="5" fill="#1565C0">трубки</text>
  
  <!-- Основная ткань -->
  <rect x="10" y="-28" width="80" height="60" rx="6" fill="white" opacity="0.9" stroke="#4CAF50" stroke-width="1"/>
  <text x="50" y="-13" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Основная</text>
  <!-- Parenchyma cells with chloroplasts -->
  <circle cx="25" cy="-2" r="8" fill="#C8E6C9" stroke="#4CAF50" stroke-width="0.8"/>
  <ellipse cx="25" cy="-2" rx="4" ry="2.5" fill="#4CAF50" opacity="0.6"/>
  <circle cx="42" cy="-2" r="8" fill="#C8E6C9" stroke="#4CAF50" stroke-width="0.8"/>
  <ellipse cx="42" cy="-2" rx="4" ry="2.5" fill="#4CAF50" opacity="0.6"/>
  <circle cx="33" cy="12" r="8" fill="#C8E6C9" stroke="#4CAF50" stroke-width="0.8"/>
  <ellipse cx="33" cy="12" rx="4" ry="2.5" fill="#4CAF50" opacity="0.6"/>
  <circle cx="58" cy="8" r="8" fill="#C8E6C9" stroke="#4CAF50" stroke-width="0.8"/>
  <ellipse cx="58" cy="8" rx="4" ry="2.5" fill="#4CAF50" opacity="0.6"/>
  <text x="50" y="26" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Фотосинтез</text>
</g>

<!-- Животные ткани -->
<g transform="translate(380,185)">
  <text x="0" y="-110" font-family="Arial,sans-serif" font-size="10" fill="#C62828" text-anchor="middle" font-weight="bold">Ткани животных</text>
  
  <!-- Эпителиальная -->
  <rect x="-90" y="-95" width="55" height="60" rx="6" fill="white" opacity="0.9" stroke="#C62828" stroke-width="1"/>
  <text x="-62" y="-80" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle" font-weight="bold">Эпителиал.</text>
  <rect x="-85" y="-72" width="10" height="8" fill="#FFCDD2" stroke="#C62828" stroke-width="0.5"/>
  <rect x="-73" y="-72" width="10" height="8" fill="#FFCDD2" stroke="#C62828" stroke-width="0.5"/>
  <rect x="-61" y="-72" width="10" height="8" fill="#FFCDD2" stroke="#C62828" stroke-width="0.5"/>
  <rect x="-49" y="-72" width="10" height="8" fill="#FFCDD2" stroke="#C62828" stroke-width="0.5"/>
  <rect x="-85" y="-64" width="10" height="8" fill="#EF9A9A" stroke="#C62828" stroke-width="0.5"/>
  <rect x="-73" y="-64" width="10" height="8" fill="#EF9A9A" stroke="#C62828" stroke-width="0.5"/>
  <rect x="-61" y="-64" width="10" height="8" fill="#EF9A9A" stroke="#C62828" stroke-width="0.5"/>
  <rect x="-49" y="-64" width="10" height="8" fill="#EF9A9A" stroke="#C62828" stroke-width="0.5"/>
  <rect x="-80" y="-52" width="40" height="8" rx="2" fill="#FFEBEE" stroke="#C62828" stroke-width="0.5"/>
  <text x="-62" y="-46" font-family="Arial,sans-serif" font-size="4" fill="#C62828" text-anchor="middle">базальная мембрана</text>
  
  <!-- Соединительная -->
  <rect x="-30" y="-95" width="55" height="60" rx="6" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1"/>
  <text x="-2" y="-80" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle" font-weight="bold">Соедinit.</text>
  <!-- Fibers -->
  <path d="M-25,-70 Q-15,-65 -20,-55 Q-15,-45 -25,-40" fill="none" stroke="#1565C0" stroke-width="1"/>
  <path d="M-20,-70 Q-10,-65 -15,-55 Q-10,-45 -20,-40" fill="none" stroke="#42A5F5" stroke-width="1"/>
  <!-- Cells -->
  <circle cx="5" cy="-65" r="4" fill="#90CAF9" stroke="#1565C0" stroke-width="0.5"/>
  <circle cx="-5" cy="-50" r="3" fill="#BBDEFB" stroke="#1565C0" stroke-width="0.5"/>
  <ellipse cx="15" cy="-55" rx="6" ry="3" fill="#FF9800" opacity="0.4" stroke="#E65100" stroke-width="0.5"/>
  <text x="-2" y="-38" font-family="Arial,sans-serif" font-size="4" fill="#1565C0" text-anchor="middle">кость, кровь,</text>
  <text x="-2" y="-32" font-family="Arial,sans-serif" font-size="4" fill="#1565C0" text-anchor="middle">хрящ, жир</text>
  
  <!-- Мышечная -->
  <rect x="35" y="-95" width="55" height="60" rx="6" fill="white" opacity="0.9" stroke="#E65100" stroke-width="1"/>
  <text x="62" y="-80" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle" font-weight="bold">Мышечная</text>
  <!-- Striated muscle fibers -->
  <rect x="42" y="-72" width="40" height="6" rx="1" fill="#FFCC80" stroke="#E65100" stroke-width="0.5"/>
  <line x1="48" y1="-72" x2="48" y2="-66" stroke="#BF360C" stroke-width="0.5"/>
  <line x1="54" y1="-72" x2="54" y2="-66" stroke="#BF360C" stroke-width="0.5"/>
  <line x1="60" y1="-72" x2="60" y2="-66" stroke="#BF360C" stroke-width="0.5"/>
  <line x1="66" y1="-72" x2="66" y2="-66" stroke="#BF360C" stroke-width="0.5"/>
  <line x1="72" y1="-72" x2="72" y2="-66" stroke="#BF360C" stroke-width="0.5"/>
  <rect x="42" y="-64" width="40" height="6" rx="1" fill="#FFE0B2" stroke="#E65100" stroke-width="0.5"/>
  <line x1="48" y1="-64" x2="48" y2="-58" stroke="#BF360C" stroke-width="0.5"/>
  <line x1="54" y1="-64" x2="54" y2="-58" stroke="#BF360C" stroke-width="0.5"/>
  <line x1="60" y1="-64" x2="60" y2="-58" stroke="#BF360C" stroke-width="0.5"/>
  <line x1="66" y1="-64" x2="66" y2="-58" stroke="#BF360C" stroke-width="0.5"/>
  <line x1="72" y1="-64" x2="72" y2="-58" stroke="#BF360C" stroke-width="0.5"/>
  <rect x="42" y="-56" width="40" height="6" rx="1" fill="#FFCC80" stroke="#E65100" stroke-width="0.5"/>
  <text x="62" y="-42" font-family="Arial,sans-serif" font-size="4" fill="#E65100" text-anchor="middle">поперечно-</text>
  <text x="62" y="-37" font-family="Arial,sans-serif" font-size="4" fill="#E65100" text-anchor="middle">полосатая</text>
  
  <!-- Нервная -->
  <rect x="-90" y="-28" width="180" height="60" rx="6" fill="white" opacity="0.9" stroke="#9C27B0" stroke-width="1"/>
  <text x="0" y="-13" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Нервная ткань</text>
  <!-- Neuron -->
  <circle cx="-30" cy="5" r="10" fill="#E1BEE7" stroke="#9C27B0" stroke-width="1"/>
  <circle cx="-32" cy="3" r="2" fill="#9C27B0"/>
  <!-- Dendrites -->
  <path d="M-38,0 Q-48,-5 -50,-12" fill="none" stroke="#9C27B0" stroke-width="1"/>
  <path d="M-38,5 Q-50,5 -55,0" fill="none" stroke="#9C27B0" stroke-width="1"/>
  <path d="M-35,12 Q-45,15 -48,20" fill="none" stroke="#9C27B0" stroke-width="1"/>
  <!-- Axon -->
  <path d="M-20,5 Q0,5 30,5" fill="none" stroke="#9C27B0" stroke-width="2"/>
  <!-- Myelin sheath -->
  <rect x="-10" y="0" width="8" height="10" rx="3" fill="#CE93D8" opacity="0.4"/>
  <rect x="5" y="0" width="8" height="10" rx="3" fill="#CE93D8" opacity="0.4"/>
  <rect x="20" y="0" width="8" height="10" rx="3" fill="#CE93D8" opacity="0.4"/>
  <!-- Axon terminals -->
  <path d="M30,5 Q35,0 38,-5" fill="none" stroke="#9C27B0" stroke-width="1"/>
  <path d="M30,5 Q35,5 40,5" fill="none" stroke="#9C27B0" stroke-width="1"/>
  <path d="M30,5 Q35,10 38,15" fill="none" stroke="#9C27B0" stroke-width="1"/>
  <text x="-30" y="25" font-family="Arial,sans-serif" font-size="4.5" fill="#7B1FA2" text-anchor="middle">тело</text>
  <text x="50" y="5" font-family="Arial,sans-serif" font-size="4.5" fill="#7B1FA2">аксон</text>
</g>

<!-- Bottom -->
<rect x="30" y="310" width="440" height="25" rx="6" fill="white" opacity="0.9" stroke="#5D4037" stroke-width="1"/>
<text x="250" y="327" font-family="Arial,sans-serif" font-size="7" fill="#3E2723" text-anchor="middle" font-weight="bold">Ткань — группа клеток, сходных по строению и выполняющих общую функцию</text>
</svg>'''

# ============================================================
# Lesson 11: Строение и жизнедеятельность бактерий
# ============================================================
svg11 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#FFF3E0"/><stop offset="100%" stop-color="#FFE0B2"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#E65100" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#BF360C" text-anchor="middle">Строение и жизнедеятельность бактерий</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 11</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#E65100" stroke-width="1" opacity="0.3"/>

<!-- Detailed bacterium structure -->
<g transform="translate(160,180)">
  <rect x="-110" y="-105" width="220" height="200" rx="8" fill="white" opacity="0.9" stroke="#E65100" stroke-width="1.5"/>
  <text x="0" y="-88" font-family="Arial,sans-serif" font-size="9" fill="#BF360C" text-anchor="middle" font-weight="bold">СТРОЕНИЕ БАКТЕРИИ</text>
  <line x1="-100" y1="-82" x2="100" y2="-82" stroke="#E65100" stroke-width="0.5"/>
  
  <!-- Large bacterium cell -->
  <ellipse cx="0" cy="5" rx="60" ry="35" fill="#FFE0B2" stroke="#E65100" stroke-width="2"/>
  
  <!-- Capsule -->
  <ellipse cx="0" cy="5" rx="68" ry="42" fill="none" stroke="#FF9800" stroke-width="2.5" stroke-dasharray="4,2" opacity="0.6"/>
  
  <!-- Cell wall -->
  <ellipse cx="0" cy="5" rx="55" ry="30" fill="none" stroke="#BF360C" stroke-width="1.5" stroke-dasharray="2,1"/>
  
  <!-- Cell membrane -->
  <ellipse cx="0" cy="5" rx="50" ry="26" fill="#FFF8E1" stroke="#FF9800" stroke-width="1" opacity="0.5"/>
  
  <!-- Nucleoid (circular DNA) -->
  <path d="M-15,-8 Q-10,-18 0,-15 Q10,-12 15,-5 Q18,5 10,10 Q0,15 -10,10 Q-18,5 -15,-8" fill="none" stroke="#1565C0" stroke-width="1.5"/>
  <text x="0" y="-2" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">Нуклеоид</text>
  <text x="0" y="5" font-family="Arial,sans-serif" font-size="4" fill="#1565C0" text-anchor="middle">(ДНК)</text>
  
  <!-- Ribosomes -->
  <circle cx="-25" cy="-10" r="3" fill="#9C27B0" opacity="0.6"/>
  <circle cx="20" cy="-8" r="3" fill="#9C27B0" opacity="0.6"/>
  <circle cx="-15" cy="15" r="3" fill="#9C27B0" opacity="0.6"/>
  <circle cx="25" cy="12" r="3" fill="#9C27B0" opacity="0.6"/>
  <circle cx="30" cy="-2" r="3" fill="#9C27B0" opacity="0.6"/>
  
  <!-- Flagellum -->
  <path d="M55,5 Q65,0 75,5 Q85,10 95,5 Q105,0 115,5" fill="none" stroke="#E65100" stroke-width="2"/>
  
  <!-- Pili -->
  <line x1="-30" y1="-30" x2="-40" y2="-45" stroke="#BF360C" stroke-width="0.8"/>
  <line x1="-20" y1="-30" x2="-25" y2="-48" stroke="#BF360C" stroke-width="0.8"/>
  <line x1="30" y1="-30" x2="35" y2="-48" stroke="#BF360C" stroke-width="0.8"/>
  
  <!-- Labels with lines -->
  <line x1="-68" y1="5" x2="-90" y2="-15" stroke="#666" stroke-width="0.5"/>
  <text x="-92" y="-15" font-family="Arial,sans-serif" font-size="5" fill="#666" text-anchor="end">Капсула</text>
  
  <line x1="-55" y1="5" x2="-90" y2="0" stroke="#666" stroke-width="0.5"/>
  <text x="-92" y="0" font-family="Arial,sans-serif" font-size="5" fill="#666" text-anchor="end">Клет. стенка</text>
  
  <line x1="-50" y1="10" x2="-90" y2="15" stroke="#666" stroke-width="0.5"/>
  <text x="-92" y="15" font-family="Arial,sans-serif" font-size="5" fill="#666" text-anchor="end">Мембрана</text>
  
  <line x1="100" y1="5" x2="90" y2="25" stroke="#666" stroke-width="0.5"/>
  <text x="92" y="27" font-family="Arial,sans-serif" font-size="5" fill="#666">Жгутик</text>
  
  <line x1="-35" y1="-40" x2="-50" y2="-55" stroke="#666" stroke-width="0.5"/>
  <text x="-52" y="-55" font-family="Arial,sans-serif" font-size="5" fill="#666" text-anchor="end">Пили</text>
  
  <line x1="25" y1="-8" x2="55" y2="-30" stroke="#666" stroke-width="0.5"/>
  <text x="57" y="-30" font-family="Arial,sans-serif" font-size="5" fill="#666">Рибосомы</text>
  
  <!-- "No nucleus" note -->
  <rect x="-45" y="55" width="90" height="25" rx="3" fill="#FFEBEE" stroke="#C62828" stroke-width="0.5"/>
  <text x="0" y="68" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">Нет ядра!</text>
  <text x="0" y="77" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">Доядерный организм</text>
</g>

<!-- Bacteria shapes -->
<g transform="translate(400,120)">
  <rect x="-65" y="-55" width="130" height="100" rx="8" fill="white" opacity="0.9" stroke="#E65100" stroke-width="1.5"/>
  <text x="0" y="-38" font-family="Arial,sans-serif" font-size="8" fill="#BF360C" text-anchor="middle" font-weight="bold">Формы бактерий</text>
  <line x1="-55" y1="-32" x2="55" y2="-32" stroke="#E65100" stroke-width="0.5"/>
  
  <!-- Cocci (spherical) -->
  <circle cx="-30" cy="-12" r="8" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
  <circle cx="-18" cy="-12" r="8" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
  <circle cx="-24" cy="-22" r="8" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
  <text x="-24" y="5" font-family="Arial,sans-serif" font-size="5" fill="#BF360C" text-anchor="middle">Кокки</text>
  
  <!-- Bacillus (rod) -->
  <rect x="5" y="-20" width="20" height="10" rx="5" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
  <text x="15" y="5" font-family="Arial,sans-serif" font-size="5" fill="#BF360C" text-anchor="middle">Палочки</text>
  
  <!-- Spirillum -->
  <path d="M35,-15 Q40,-20 45,-15 Q50,-10 55,-15 Q60,-20 55,-10 Q50,0 55,-5" fill="none" stroke="#E65100" stroke-width="2.5" stroke-linecap="round"/>
  <text x="45" y="5" font-family="Arial,sans-serif" font-size="5" fill="#BF360C" text-anchor="middle">Спириллы</text>
  
  <!-- Vibrio -->
  <path d="M-40,25 Q-30,15 -25,25" fill="none" stroke="#E65100" stroke-width="3" stroke-linecap="round"/>
  <text x="-32" y="38" font-family="Arial,sans-serif" font-size="5" fill="#BF360C" text-anchor="middle">Вибрионы</text>
</g>

<!-- Spore formation -->
<g transform="translate(400,245)">
  <rect x="-65" y="-30" width="130" height="55" rx="6" fill="white" opacity="0.9" stroke="#795548" stroke-width="1"/>
  <text x="0" y="-15" font-family="Arial,sans-serif" font-size="7" fill="#5D4037" text-anchor="middle" font-weight="bold">Спорообразование</text>
  <ellipse cx="-35" cy="5" rx="12" ry="7" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
  <circle cx="-35" cy="3" r="4" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
  <text x="-35" y="18" font-family="Arial,sans-serif" font-size="4" fill="#5D4037" text-anchor="middle">спора</text>
  <text x="20" y="3" font-family="Arial,sans-serif" font-size="5" fill="#5D4037" text-anchor="middle">Выживание в</text>
  <text x="20" y="11" font-family="Arial,sans-serif" font-size="5" fill="#5D4037" text-anchor="middle">неблагопр. условиях</text>
</g>

<!-- Bottom -->
<rect x="30" y="310" width="440" height="25" rx="6" fill="white" opacity="0.9" stroke="#E65100" stroke-width="1"/>
<text x="250" y="327" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle" font-weight="bold">Бактерии — доядерные организмы: нет ядра, митохондрий, хлоропластов</text>
</svg>'''

# ============================================================
# Lesson 12: Роль бактерий в природе и жизни человека
# ============================================================
svg12 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#E8F5E9"/><stop offset="100%" stop-color="#C8E6C9"/></linearGradient>
</defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#2E7D32" stroke-width="2.5"/>
<text x="250" y="28" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1B5E20" text-anchor="middle">Роль бактерий в природе и жизни человека</text>
<text x="250" y="43" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">Биология 5 класс — Урок 12</text>
<line x1="30" y1="50" x2="470" y2="50" stroke="#2E7D32" stroke-width="1" opacity="0.3"/>

<!-- Positive roles -->
<rect x="20" y="55" width="225" height="245" rx="8" fill="white" opacity="0.9" stroke="#2E7D32" stroke-width="1.5"/>
<text x="132" y="72" font-family="Arial,sans-serif" font-size="9" fill="#1B5E20" text-anchor="middle" font-weight="bold">ПОЛОЖИТЕЛЬНАЯ РОЛЬ</text>
<line x1="30" y1="78" x2="235" y2="78" stroke="#2E7D32" stroke-width="0.5"/>

<!-- Soil formation -->
<g transform="translate(70,115)">
  <ellipse cx="0" cy="0" rx="15" ry="7" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
  <circle cx="-5" cy="-2" r="2" fill="#FFCC80"/>
  <circle cx="5" cy="-2" r="2" fill="#FFCC80"/>
  <text x="25" y="-2" font-family="Arial,sans-serif" font-size="6" fill="#1B5E20" font-weight="bold">Почвообразование</text>
  <text x="25" y="7" font-family="Arial,sans-serif" font-size="5" fill="#666">Разложение органики</text>
</g>

<!-- Nitrogen fixation -->
<g transform="translate(70,155)">
  <!-- Root nodules -->
  <path d="M-5,-12 L-5,5" stroke="#795548" stroke-width="2"/>
  <path d="M5,-12 L5,5" stroke="#795548" stroke-width="2"/>
  <circle cx="-5" cy="10" r="5" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>
  <circle cx="5" cy="10" r="5" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>
  <text x="20" y="-2" font-family="Arial,sans-serif" font-size="6" fill="#1B5E20" font-weight="bold">Азотфиксация</text>
  <text x="20" y="7" font-family="Arial,sans-serif" font-size="5" fill="#666">Клубеньковые бактерии</text>
  <text x="20" y="15" font-family="Arial,sans-serif" font-size="5" fill="#666">Связывают азот из воздуха</text>
</g>

<!-- Food production -->
<g transform="translate(70,200)">
  <!-- Milk/cheese -->
  <path d="M-12,-8 L-8,8 L8,8 L12,-8 Z" fill="white" stroke="#90CAF9" stroke-width="1" rx="2"/>
  <rect x="-8" y="-4" width="12" height="8" rx="1" fill="#FFF9C4" opacity="0.6"/>
  <text x="20" y="-2" font-family="Arial,sans-serif" font-size="6" fill="#1B5E20" font-weight="bold">Пищевая промышл.</text>
  <text x="20" y="7" font-family="Arial,sans-serif" font-size="5" fill="#666">Кефир, йогурт, сыр,</text>
  <text x="20" y="15" font-family="Arial,sans-serif" font-size="5" fill="#666">квашеная капуста, уксус</text>
</g>

<!-- Medicine -->
<g transform="translate(70,245)">
  <!-- Pill -->
  <rect x="-12" y="-6" width="24" height="12" rx="6" fill="#FFCDD2" stroke="#C62828" stroke-width="1"/>
  <rect x="0" y="-6" width="12" height="12" rx="0" fill="#EF9A9A" stroke="#C62828" stroke-width="0.5"/>
  <text x="20" y="-2" font-family="Arial,sans-serif" font-size="6" fill="#1B5E20" font-weight="bold">Медицина</text>
  <text x="20" y="7" font-family="Arial,sans-serif" font-size="5" fill="#666">Антибиотики (пенициллин)</text>
  <text x="20" y="15" font-family="Arial,sans-serif" font-size="5" fill="#666">Вакцины, инсулин</text>
</g>

<!-- Digestion -->
<g transform="translate(70,283)">
  <text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#1B5E20" font-weight="bold">Кишечная микрофлора</text>
  <text x="0" y="9" font-family="Arial,sans-serif" font-size="5" fill="#666">Витамины K, B, пищеварение</text>
</g>

<!-- Negative roles -->
<rect x="255" y="55" width="225" height="245" rx="8" fill="white" opacity="0.9" stroke="#C62828" stroke-width="1.5"/>
<text x="367" y="72" font-family="Arial,sans-serif" font-size="9" fill="#C62828" text-anchor="middle" font-weight="bold">ОТРИЦАТЕЛЬНАЯ РОЛЬ</text>
<line x1="265" y1="78" x2="470" y2="78" stroke="#C62828" stroke-width="0.5"/>

<!-- Diseases -->
<g transform="translate(310,115)">
  <circle cx="0" cy="0" r="8" fill="#FFCDD2" stroke="#C62828" stroke-width="1"/>
  <text x="0" y="3" font-family="Arial,sans-serif" font-size="8" fill="#C62828" text-anchor="middle">!</text>
  <text x="15" y="-2" font-family="Arial,sans-serif" font-size="6" fill="#C62828" font-weight="bold">Заболевания</text>
  <text x="15" y="7" font-family="Arial,sans-serif" font-size="5" fill="#666">Холера, туберкулёз,</text>
  <text x="15" y="15" font-family="Arial,sans-serif" font-size="5" fill="#666">дифтерия, столбняк</text>
</g>

<!-- Food spoilage -->
<g transform="translate(310,160)">
  <!-- Spoiled food -->
  <rect x="-10" y="-8" width="15" height="12" rx="2" fill="#C8E6C9" stroke="#2E7D32" stroke-width="0.5" opacity="0.5"/>
  <circle cx="-5" cy="-3" r="2" fill="#795548" opacity="0.6"/>
  <circle cx="0" cy="0" r="2.5" fill="#8D6E63" opacity="0.6"/>
  <path d="M-3,-8 Q-1,-12 2,-8" fill="none" stroke="#9E9E9E" stroke-width="0.5"/>
  <text x="15" y="-2" font-family="Arial,sans-serif" font-size="6" fill="#C62828" font-weight="bold">Порча продуктов</text>
  <text x="15" y="7" font-family="Arial,sans-serif" font-size="5" fill="#666">Гниение, брожение</text>
</g>

<!-- Bioweapons -->
<g transform="translate(310,200)">
  <!-- Biohazard simplified -->
  <circle cx="0" cy="0" r="8" fill="#FFEBEE" stroke="#C62828" stroke-width="1"/>
  <circle cx="0" cy="-3" r="2.5" fill="none" stroke="#C62828" stroke-width="1"/>
  <circle cx="-2" cy="1.5" r="2.5" fill="none" stroke="#C62828" stroke-width="1"/>
  <circle cx="2" cy="1.5" r="2.5" fill="none" stroke="#C62828" stroke-width="1"/>
  <text x="15" y="-2" font-family="Arial,sans-serif" font-size="6" fill="#C62828" font-weight="bold">Биологич. оружие</text>
  <text x="15" y="7" font-family="Arial,sans-serif" font-size="5" fill="#666">Опасные штаммы</text>
</g>

<!-- Infections -->
<g transform="translate(310,240)">
  <text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#C62828" font-weight="bold">Инфекции растений</text>
  <text x="0" y="9" font-family="Arial,sans-serif" font-size="5" fill="#666">Бактериальный рак,</text>
  <text x="0" y="17" font-family="Arial,sans-serif" font-size="5" fill="#666">увядание, гниль</text>
</g>

<!-- Bottom -->
<rect x="30" y="310" width="440" height="25" rx="6" fill="white" opacity="0.9" stroke="#2E7D32" stroke-width="1"/>
<text x="250" y="327" font-family="Arial,sans-serif" font-size="7" fill="#1B5E20" text-anchor="middle" font-weight="bold">Круговорот веществ в природе невозможен без бактерий — они редуценты</text>
</svg>'''

print("Generating Grade 5 Biology SVGs (lessons 5-12)...")
print()

write_svg("lesson5.svg", svg5)
write_svg("lesson6.svg", svg6)
write_svg("lesson7.svg", svg7)
write_svg("lesson8.svg", svg8)
write_svg("lesson9.svg", svg9)
write_svg("lesson10.svg", svg10)
write_svg("lesson11.svg", svg11)
write_svg("lesson12.svg", svg12)

print("\nLessons 5-12 done!")
