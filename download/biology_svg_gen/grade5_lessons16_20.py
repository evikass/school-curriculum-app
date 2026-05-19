#!/usr/bin/env python3
"""Generate detailed biology SVG illustrations for Grade 5, Lessons 16-20"""

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


# ===== LESSON 16: Общая характеристика животных =====
lesson16_illustration = '''
  <!-- Animal kingdom classification -->
  <!-- Central circle -->
  <circle cx="250" cy="185" r="40" fill="#2E7D32" opacity="0.8"/>
  <text x="250" y="182" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">Животные</text>
  <text x="250" y="195" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">(гетеротрофы)</text>
  <!-- Branches to groups -->
  <!-- Простейшие -->
  <line x1="215" y1="160" x2="130" y2="100" stroke="#2E7D32" stroke-width="2"/>
  <circle cx="120" cy="92" r="32" fill="#CE93D8" opacity="0.6" stroke="#8E24AA" stroke-width="1.5"/>
  <text x="120" y="90" font-family="Arial,sans-serif" font-size="8" fill="#4A148C" text-anchor="middle" font-weight="bold">Простейшие</text>
  <text x="120" y="102" font-family="Arial,sans-serif" font-size="7" fill="#4A148C" text-anchor="middle">1 клетка</text>
  <!-- Кишечнополостные -->
  <line x1="220" y1="215" x2="130" y2="260" stroke="#2E7D32" stroke-width="2"/>
  <circle cx="120" cy="268" r="32" fill="#FF8A65" opacity="0.6" stroke="#E64A19" stroke-width="1.5"/>
  <text x="120" y="266" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle" font-weight="bold">Кишечнополостные</text>
  <text x="120" y="278" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle">2 слоя клеток</text>
  <!-- Черви -->
  <line x1="250" y1="145" x2="250" y2="95" stroke="#2E7D32" stroke-width="2"/>
  <circle cx="250" cy="82" r="28" fill="#A1887F" opacity="0.6" stroke="#5D4037" stroke-width="1.5"/>
  <text x="250" y="80" font-family="Arial,sans-serif" font-size="8" fill="#3E2723" text-anchor="middle" font-weight="bold">Черви</text>
  <text x="250" y="92" font-family="Arial,sans-serif" font-size="7" fill="#3E2723" text-anchor="middle">3 слоя</text>
  <!-- Моллюски -->
  <line x1="285" y1="160" x2="370" y2="100" stroke="#2E7D32" stroke-width="2"/>
  <circle cx="380" cy="92" r="32" fill="#90CAF9" opacity="0.6" stroke="#1565C0" stroke-width="1.5"/>
  <text x="380" y="90" font-family="Arial,sans-serif" font-size="8" fill="#0D47A1" text-anchor="middle" font-weight="bold">Моллюски</text>
  <text x="380" y="102" font-family="Arial,sans-serif" font-size="7" fill="#0D47A1" text-anchor="middle">раковина</text>
  <!-- Членистоногие -->
  <line x1="285" y1="205" x2="370" y2="185" stroke="#2E7D32" stroke-width="2"/>
  <circle cx="400" cy="180" r="32" fill="#FFCC80" opacity="0.6" stroke="#E65100" stroke-width="1.5"/>
  <text x="400" y="178" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle" font-weight="bold">Членистоногие</text>
  <text x="400" y="190" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle">хитин. покров</text>
  <!-- Позвоночные -->
  <line x1="285" y1="215" x2="370" y2="265" stroke="#2E7D32" stroke-width="2"/>
  <circle cx="380" cy="272" r="35" fill="#81C784" opacity="0.6" stroke="#2E7D32" stroke-width="1.5"/>
  <text x="380" y="268" font-family="Arial,sans-serif" font-size="8" fill="#1B5E20" text-anchor="middle" font-weight="bold">Позвоночные</text>
  <text x="380" y="280" font-family="Arial,sans-serif" font-size="7" fill="#1B5E20" text-anchor="middle">скелет внутри</text>
  <!-- Animal features box -->
  <rect x="15" y="290" width="220" height="25" rx="4" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="125" y="307" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Гетеротрофы, подвижны, растут, размножаются</text>
'''

# ===== LESSON 17: Простейшие — одноклеточные животные =====
lesson17_illustration = '''
  <!-- Amoeba -->
  <g transform="translate(100,170)">
    <!-- Irregular cell shape -->
    <path d="M-40 10 Q-50 -15 -30 -30 Q-10 -45 15 -35 Q35 -25 40 -5 Q45 15 30 30 Q15 45 -10 40 Q-30 35 -40 10 Z" fill="#E1F5FE" stroke="#42A5F5" stroke-width="2"/>
    <!-- Inner lighter -->
    <path d="M-30 5 Q-35 -10 -20 -22 Q0 -32 10 -25 Q25 -18 28 -3 Q30 10 18 20 Q5 30 -10 25 Q-22 20 -30 5 Z" fill="#BBDEFB" opacity="0.5"/>
    <!-- Nucleus -->
    <ellipse cx="-5" cy="-5" rx="12" ry="9" fill="#90CAF9" stroke="#1E88E5" stroke-width="1.5"/>
    <circle cx="-5" cy="-5" r="4" fill="#42A5F5"/>
    <!-- Contractile vacuole -->
    <circle cx="20" cy="-15" r="7" fill="#E3F2FD" stroke="#64B5F6" stroke-width="1"/>
    <circle cx="20" cy="-15" r="4" fill="#BBDEFB"/>
    <!-- Food vacuoles -->
    <circle cx="-20" cy="10" r="5" fill="#C8E6C9" stroke="#66BB6A" stroke-width="0.8"/>
    <circle cx="10" cy="15" r="4" fill="#C8E6C9" stroke="#66BB6A" stroke-width="0.8"/>
    <!-- Pseudopods -->
    <path d="M-40 10 Q-55 15 -60 5" stroke="#42A5F5" stroke-width="2" fill="#E1F5FE"/>
    <path d="M30 30 Q45 35 50 25" stroke="#42A5F5" stroke-width="2" fill="#E1F5FE"/>
    <path d="M15 -35 Q20 -45 30 -42" stroke="#42A5F5" stroke-width="2" fill="#E1F5FE"/>
    <!-- Labels -->
    <text x="0" y="55" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Амёба</text>
  </g>
  <!-- Amoeba labels -->
  <text x="20" y="85" font-family="Arial,sans-serif" font-size="7" fill="#333">Ложноножки</text>
  <line x1="48" y1="88" x2="55" y2="130" stroke="#333" stroke-width="0.5"/>
  <text x="160" y="95" font-family="Arial,sans-serif" font-size="7" fill="#333">Ядро</text>
  <line x1="100" y1="160" x2="88" y2="168" stroke="#333" stroke-width="0.5"/>
  <text x="170" y="150" font-family="Arial,sans-serif" font-size="7" fill="#333">Сократит. вакуоль</text>
  <line x1="120" y1="152" x2="115" y2="155" stroke="#333" stroke-width="0.5"/>
  <!-- Euglena -->
  <g transform="translate(310,170)">
    <!-- Elongated body -->
    <ellipse cx="0" cy="0" rx="12" ry="35" fill="#E8F5E9" stroke="#4CAF50" stroke-width="2"/>
    <!-- Flagellum -->
    <path d="M0 -35 Q5 -50 10 -55 Q15 -50 12 -45 Q8 -40 15 -35" stroke="#4CAF50" stroke-width="1.5" fill="none"/>
    <!-- Eye spot -->
    <circle cx="-3" cy="-22" r="4" fill="#E53935"/>
    <!-- Chloroplasts -->
    <ellipse cx="-5" cy="-5" rx="4" ry="7" fill="#81C784" opacity="0.6"/>
    <ellipse cx="4" cy="8" rx="3" ry="6" fill="#81C784" opacity="0.5"/>
    <!-- Nucleus -->
    <ellipse cx="0" cy="12" rx="5" ry="4" fill="#A5D6A7" stroke="#4CAF50" stroke-width="1"/>
    <!-- Contractile vacuole -->
    <circle cx="5" cy="-15" r="3" fill="#E3F2FD" stroke="#64B5F6" stroke-width="0.8"/>
    <text x="0" y="50" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Эвглена</text>
    <text x="0" y="62" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(жгутиконосец)</text>
  </g>
  <!-- Euglena labels -->
  <text x="370" y="115" font-family="Arial,sans-serif" font-size="7" fill="#333">Жгутик</text>
  <line x1="370" y1="118" x2="325" y2="128" stroke="#333" stroke-width="0.5"/>
  <text x="370" y="135" font-family="Arial,sans-serif" font-size="7" fill="#333">Светочувст. глазок</text>
  <line x1="370" y1="138" x2="315" y2="148" stroke="#333" stroke-width="0.5"/>
  <!-- Paramecium -->
  <g transform="translate(440,170)">
    <!-- Slipper shape -->
    <path d="M-15 -30 Q-20 -15 -18 0 Q-15 20 -8 30 Q0 35 8 30 Q15 20 18 0 Q20 -15 15 -30 Q8 -38 0 -38 Q-8 -38 -15 -30 Z" fill="#FFF3E0" stroke="#FF9800" stroke-width="2"/>
    <!-- Cilia -->
    <line x1="-18" y1="-15" x2="-24" y2="-18" stroke="#FF9800" stroke-width="0.8"/>
    <line x1="-20" y1="-5" x2="-26" y2="-7" stroke="#FF9800" stroke-width="0.8"/>
    <line x1="-20" y1="5" x2="-26" y2="4" stroke="#FF9800" stroke-width="0.8"/>
    <line x1="-18" y1="15" x2="-24" y2="14" stroke="#FF9800" stroke-width="0.8"/>
    <line x1="18" y1="-15" x2="24" y2="-18" stroke="#FF9800" stroke-width="0.8"/>
    <line x1="20" y1="-5" x2="26" y2="-7" stroke="#FF9800" stroke-width="0.8"/>
    <line x1="20" y1="5" x2="26" y2="4" stroke="#FF9800" stroke-width="0.8"/>
    <line x1="18" y1="15" x2="24" y2="14" stroke="#FF9800" stroke-width="0.8"/>
    <!-- Macronucleus -->
    <ellipse cx="0" cy="-5" rx="8" ry="5" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
    <!-- Micronucleus -->
    <circle cx="5" cy="0" r="3" fill="#FFB74D" stroke="#E65100" stroke-width="0.8"/>
    <!-- Oral groove -->
    <path d="M-10 -10 Q-12 0 -8 10" stroke="#E65100" stroke-width="1.5" fill="none"/>
    <!-- Contractile vacuoles -->
    <circle cx="-5" cy="-20" r="4" fill="#E3F2FD" stroke="#64B5F6" stroke-width="0.8"/>
    <circle cx="3" cy="18" r="4" fill="#E3F2FD" stroke="#64B5F6" stroke-width="0.8"/>
    <text x="0" y="50" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Инфузория</text>
    <text x="0" y="62" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(туфелька)</text>
  </g>
  <!-- Bottom info -->
  <rect x="60" y="265" width="380" height="40" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="282" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Общие признаки простейших</text>
  <text x="250" y="297" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">1 клетка = целый организм, сократительная вакуоль, гетеротрофы</text>
'''

# ===== LESSON 18: Кишечнополостные и черви =====
lesson18_illustration = '''
  <!-- Hydra (Кишечнополостное) -->
  <g transform="translate(130,180)">
    <!-- Body column -->
    <path d="M-15 -20 Q-18 0 -15 30 Q-12 50 -8 55" stroke="#EF5350" stroke-width="2" fill="#FFCDD2"/>
    <path d="M15 -20 Q18 0 15 30 Q12 50 8 55" stroke="#EF5350" stroke-width="2" fill="#FFCDD2"/>
    <path d="M-8 55 Q0 60 8 55" fill="#FFCDD2" stroke="#EF5350" stroke-width="1.5"/>
    <!-- Tentacles -->
    <path d="M-15 -20 Q-30 -40 -35 -50" stroke="#EF5350" stroke-width="2" fill="none"/>
    <path d="M-10 -22 Q-15 -45 -12 -55" stroke="#EF5350" stroke-width="2" fill="none"/>
    <path d="M-5 -23 Q0 -48 5 -55" stroke="#EF5350" stroke-width="2" fill="none"/>
    <path d="M5 -23 Q10 -45 12 -52" stroke="#EF5350" stroke-width="2" fill="none"/>
    <path d="M10 -22 Q20 -40 28 -48" stroke="#EF5350" stroke-width="2" fill="none"/>
    <path d="M15 -20 Q30 -38 38 -45" stroke="#EF5350" stroke-width="2" fill="none"/>
    <!-- Tentacle knobs (cnidocytes) -->
    <circle cx="-35" cy="-50" r="3" fill="#E53935"/>
    <circle cx="-12" cy="-55" r="3" fill="#E53935"/>
    <circle cx="5" cy="-55" r="3" fill="#E53935"/>
    <circle cx="12" cy="-52" r="3" fill="#E53935"/>
    <circle cx="28" cy="-48" r="3" fill="#E53935"/>
    <circle cx="38" cy="-45" r="3" fill="#E53935"/>
    <!-- Mouth/hypostome -->
    <ellipse cx="0" cy="-18" rx="12" ry="5" fill="#EF9A9A" stroke="#E53935" stroke-width="1"/>
    <!-- Inner cavity (gastrovascular) -->
    <path d="M-8 -15 Q-10 10 -6 35 Q0 40 6 35 Q10 10 8 -15" fill="#FFAB91" opacity="0.3"/>
    <!-- Basal disc -->
    <ellipse cx="0" cy="57" rx="10" ry="4" fill="#EF9A9A" stroke="#E53935" stroke-width="1"/>
    <!-- Bud (asexual reproduction) -->
    <path d="M15 10 Q25 5 28 12 Q30 20 22 22 Q15 20 15 10 Z" fill="#FFCDD2" stroke="#EF5350" stroke-width="1"/>
    <text x="0" y="80" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Гидра</text>
    <text x="0" y="92" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(кишечнополостное)</text>
  </g>
  <!-- Hydra labels -->
  <text x="230" y="100" font-family="Arial,sans-serif" font-size="7" fill="#333">Щупальца</text>
  <line x1="229" y1="102" x2="160" y2="128" stroke="#333" stroke-width="0.5"/>
  <text x="250" y="135" font-family="Arial,sans-serif" font-size="7" fill="#333">Рот</text>
  <line x1="240" y1="137" x2="145" y2="162" stroke="#333" stroke-width="0.5"/>
  <text x="250" y="170" font-family="Arial,sans-serif" font-size="7" fill="#333">Кишечная полость</text>
  <line x1="250" y1="172" x2="135" y2="185" stroke="#333" stroke-width="0.5"/>
  <text x="250" y="200" font-family="Arial,sans-serif" font-size="7" fill="#333">Подошва</text>
  <line x1="250" y1="202" x2="140" y2="235" stroke="#333" stroke-width="0.5"/>
  <text x="250" y="115" font-family="Arial,sans-serif" font-size="7" fill="#C62828">Стрекательные клетки</text>
  <line x1="265" y1="113" x2="170" y2="130" stroke="#333" stroke-width="0.5"/>
  <!-- Flatworm (Плоский червь) -->
  <g transform="translate(400,150)">
    <!-- Planaria body -->
    <path d="M-10 -35 Q-25 -40 -35 -35 Q-40 -30 -35 -25 Q-25 -20 -10 -22 L-10 22 Q-25 20 -35 25 Q-40 30 -35 35 Q-25 40 -10 35 L10 35 Q25 40 35 35 Q40 30 35 25 Q25 20 10 22 L10 -22 Q25 -20 35 -25 Q40 -30 35 -35 Q25 -40 10 -35 Z" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
    <!-- Eyespots -->
    <circle cx="-20" cy="-32" r="4" fill="#333"/>
    <circle cx="20" cy="-32" r="4" fill="#333"/>
    <!-- Auricles -->
    <path d="M-30 -35 Q-35 -45 -25 -42" stroke="#E65100" stroke-width="1.5" fill="#FFE0B2"/>
    <path d="M30 -35 Q35 -45 25 -42" stroke="#E65100" stroke-width="1.5" fill="#FFE0B2"/>
    <!-- Pharynx -->
    <ellipse cx="0" cy="0" rx="6" ry="8" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
    <!-- Gut branches -->
    <path d="M0 -8 Q-15 -20 -25 -15" stroke="#E65100" stroke-width="0.8" fill="none"/>
    <path d="M0 -8 Q15 -20 25 -15" stroke="#E65100" stroke-width="0.8" fill="none"/>
    <path d="M0 8 Q-15 20 -25 15" stroke="#E65100" stroke-width="0.8" fill="none"/>
    <path d="M0 8 Q15 20 25 15" stroke="#E65100" stroke-width="0.8" fill="none"/>
    <text x="0" y="55" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">Планария</text>
    <text x="0" y="67" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(плоский червь)</text>
  </g>
  <!-- Roundworm -->
  <g transform="translate(400,270)">
    <path d="M-40 0 Q-35 -8 0 -6 Q35 -8 40 0 Q35 8 0 6 Q-35 8 -40 0 Z" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/>
    <!-- Pointed ends -->
    <path d="M-40 0 L-48 -2 L-48 2 Z" fill="#F9A825"/>
    <path d="M40 0 L48 -2 L48 2 Z" fill="#F9A825"/>
    <!-- Mouth -->
    <circle cx="-45" cy="0" r="2" fill="#F57F17"/>
    <!-- Gut -->
    <line x1="-40" y1="0" x2="40" y2="0" stroke="#F57F17" stroke-width="1" opacity="0.5"/>
    <text x="0" y="25" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Круглый червь (аскарида)</text>
  </g>
  <!-- Comparison -->
  <rect x="280" y="85" width="200" height="18" rx="3" fill="#2E7D32" opacity="0.1"/>
  <text x="380" y="97" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Двусторонняя симметрия, 3 слоя клеток</text>
'''

# ===== LESSON 19: Моллюски и членистоногие =====
lesson19_illustration = '''
  <!-- Mollusks section -->
  <g transform="translate(0,55)">
    <rect x="20" y="0" width="210" height="20" rx="4" fill="#1565C0" opacity="0.15"/>
    <text x="125" y="14" font-family="Arial,sans-serif" font-size="11" fill="#1565C0" text-anchor="middle" font-weight="bold">Моллюски</text>
    <!-- Snail -->
    <g transform="translate(70,90)">
      <!-- Shell spiral -->
      <path d="M0 0 Q5 -15 15 -15 Q25 -15 25 -5 Q25 5 15 5 Q5 5 0 0 Z" fill="#D7CCC8" stroke="#795548" stroke-width="1.5"/>
      <path d="M15 -15 Q25 -25 30 -15 Q35 -5 25 0 Q20 3 15 5" fill="#BCAAA4" stroke="#795548" stroke-width="1"/>
      <!-- Body -->
      <path d="M-5 0 Q-20 5 -25 15 Q-20 25 -5 20 Q0 18 5 15" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
      <!-- Tentacles -->
      <line x1="-20" y1="10" x2="-25" y2="-5" stroke="#E65100" stroke-width="1.5"/>
      <line x1="-18" y1="8" x2="-22" y2="-3" stroke="#E65100" stroke-width="1.5"/>
      <!-- Eyes -->
      <circle cx="-25" cy="-5" r="2" fill="#333"/>
      <circle cx="-22" cy="-3" r="2" fill="#333"/>
      <!-- Foot -->
      <path d="M-25 15 Q-30 25 -20 28 Q-10 25 -5 20" fill="#FFCC80" opacity="0.6"/>
      <text x="-5" y="45" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Улитка</text>
    </g>
    <!-- Bivalve -->
    <g transform="translate(175,85)">
      <!-- Left shell -->
      <path d="M0 -20 Q-25 -15 -30 0 Q-25 20 0 25 Z" fill="#E0E0E0" stroke="#9E9E9E" stroke-width="1.5"/>
      <!-- Right shell -->
      <path d="M0 -20 Q25 -15 30 0 Q25 20 0 25 Z" fill="#EEEEEE" stroke="#9E9E9E" stroke-width="1.5"/>
      <!-- Shell lines -->
      <path d="M0 -15 Q-15 -10 -20 0" stroke="#BDBDBD" stroke-width="0.8" fill="none"/>
      <path d="M0 -10 Q-12 -5 -15 5" stroke="#BDBDBD" stroke-width="0.8" fill="none"/>
      <path d="M0 -15 Q15 -10 20 0" stroke="#BDBDBD" stroke-width="0.8" fill="none"/>
      <path d="M0 -10 Q12 -5 15 5" stroke="#BDBDBD" stroke-width="0.8" fill="none"/>
      <!-- Hinge -->
      <line x1="-3" y1="-20" x2="3" y2="-20" stroke="#757575" stroke-width="2"/>
      <!-- Gaping slightly -->
      <text x="0" y="45" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Двустворчатые</text>
    </g>
  </g>
  <!-- Arthropods section -->
  <g transform="translate(0,55)">
    <rect x="260" y="0" width="220" height="20" rx="4" fill="#E65100" opacity="0.12"/>
    <text x="370" y="14" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle" font-weight="bold">Членистоногие</text>
    <!-- Crab/Crustacean -->
    <g transform="translate(310,90)">
      <!-- Body -->
      <ellipse cx="0" cy="0" rx="20" ry="12" fill="#FF8A65" stroke="#E64A19" stroke-width="1.5"/>
      <!-- Claws -->
      <path d="M-20 -5 Q-30 -15 -35 -10 Q-38 -5 -32 -2 Q-25 0 -20 -2" fill="#FFAB91" stroke="#E64A19" stroke-width="1"/>
      <path d="M20 -5 Q30 -15 35 -10 Q38 -5 32 -2 Q25 0 20 -2" fill="#FFAB91" stroke="#E64A19" stroke-width="1"/>
      <!-- Legs -->
      <line x1="-15" y1="10" x2="-22" y2="22" stroke="#E64A19" stroke-width="1.5"/>
      <line x1="-8" y1="12" x2="-12" y2="24" stroke="#E64A19" stroke-width="1.5"/>
      <line x1="8" y1="12" x2="12" y2="24" stroke="#E64A19" stroke-width="1.5"/>
      <line x1="15" y1="10" x2="22" y2="22" stroke="#E64A19" stroke-width="1.5"/>
      <!-- Eyes -->
      <circle cx="-8" cy="-8" r="3" fill="#333"/>
      <circle cx="8" cy="-8" r="3" fill="#333"/>
      <!-- Eye stalks -->
      <line x1="-5" y1="-8" x2="-8" y2="-15" stroke="#E64A19" stroke-width="1"/>
      <line x1="5" y1="-8" x2="8" y2="-15" stroke="#E64A19" stroke-width="1"/>
      <text x="0" y="38" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Ракообразные</text>
    </g>
    <!-- Spider/Arachnid -->
    <g transform="translate(410,85)">
      <!-- Body: cephalothorax + abdomen -->
      <circle cx="0" cy="-5" r="10" fill="#5D4037" stroke="#3E2723" stroke-width="1"/>
      <ellipse cx="0" cy="12" rx="14" ry="10" fill="#795548" stroke="#5D4037" stroke-width="1"/>
      <!-- Legs -->
      <line x1="-8" y1="-8" x2="-25" y2="-20" stroke="#5D4037" stroke-width="1.5"/>
      <line x1="-8" y1="-2" x2="-28" y2="-5" stroke="#5D4037" stroke-width="1.5"/>
      <line x1="-8" y1="3" x2="-25" y2="15" stroke="#5D4037" stroke-width="1.5"/>
      <line x1="-5" y1="8" x2="-20" y2="25" stroke="#5D4037" stroke-width="1.5"/>
      <line x1="8" y1="-8" x2="25" y2="-20" stroke="#5D4037" stroke-width="1.5"/>
      <line x1="8" y1="-2" x2="28" y2="-5" stroke="#5D4037" stroke-width="1.5"/>
      <line x1="8" y1="3" x2="25" y2="15" stroke="#5D4037" stroke-width="1.5"/>
      <line x1="5" y1="8" x2="20" y2="25" stroke="#5D4037" stroke-width="1.5"/>
      <!-- Eyes -->
      <circle cx="-4" cy="-8" r="1.5" fill="#333"/>
      <circle cx="4" cy="-8" r="1.5" fill="#333"/>
      <!-- Chelicerae -->
      <path d="M-3 -15 L-5 -20" stroke="#3E2723" stroke-width="1"/>
      <path d="M3 -15 L5 -20" stroke="#3E2723" stroke-width="1"/>
      <text x="0" y="38" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Паукообразные</text>
    </g>
    <!-- Insect -->
    <g transform="translate(360,170)">
      <!-- Head -->
      <circle cx="-20" cy="0" r="7" fill="#FDD835" stroke="#F57F17" stroke-width="1"/>
      <!-- Eyes -->
      <circle cx="-23" cy="-2" r="2" fill="#333"/>
      <!-- Antennae -->
      <path d="M-22 -5 Q-28 -15 -25 -20" stroke="#F57F17" stroke-width="1" fill="none"/>
      <path d="M-20 -5 Q-18 -18 -15 -22" stroke="#F57F17" stroke-width="1" fill="none"/>
      <!-- Thorax -->
      <ellipse cx="-8" cy="0" rx="10" ry="8" fill="#FDD835" stroke="#F57F17" stroke-width="1"/>
      <!-- Wings -->
      <path d="M-8 -8 Q-15 -30 10 -28 Q20 -25 -3 -8" fill="#E3F2FD" stroke="#90CAF9" stroke-width="0.8" opacity="0.7"/>
      <path d="M-8 -8 Q5 -32 25 -22 Q20 -15 -3 -8" fill="#BBDEFB" stroke="#90CAF9" stroke-width="0.8" opacity="0.6"/>
      <!-- Abdomen -->
      <ellipse cx="12" cy="0" rx="14" ry="9" fill="#FBC02D" stroke="#F57F17" stroke-width="1"/>
      <!-- Abdomen stripes -->
      <line x1="5" y1="-8" x2="5" y2="8" stroke="#F57F17" stroke-width="0.5" opacity="0.5"/>
      <line x1="10" y1="-9" x2="10" y2="9" stroke="#F57F17" stroke-width="0.5" opacity="0.5"/>
      <line x1="15" y1="-8" x2="15" y2="8" stroke="#F57F17" stroke-width="0.5" opacity="0.5"/>
      <!-- Legs -->
      <line x1="-12" y1="8" x2="-18" y2="18" stroke="#F57F17" stroke-width="1"/>
      <line x1="-5" y1="8" x2="-8" y2="20" stroke="#F57F17" stroke-width="1"/>
      <line x1="2" y1="8" x2="2" y2="20" stroke="#F57F17" stroke-width="1"/>
      <text x="0" y="35" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Насекомые</text>
    </g>
  </g>
  <!-- Common features -->
  <rect x="30" y="280" width="440" height="30" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="295" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Общее: мягкое тело (моллюски) / хитиновый покров и членистые ноги (членистоногие)</text>
  <text x="250" y="307" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Моллюски: раковина, мантия, нога | Членистоногие: хитин, сегментация, 6-8 ног</text>
'''

# ===== LESSON 20: Позвоночные животные =====
lesson20_illustration = '''
  <!-- Evolution of vertebrates - fish to mammals -->
  <!-- Fish (Рыбы) -->
  <g transform="translate(70,120)">
    <!-- Body -->
    <ellipse cx="0" cy="0" rx="30" ry="15" fill="#64B5F6" stroke="#1565C0" stroke-width="1.5"/>
    <!-- Tail -->
    <path d="M30 0 L45 -12 L45 12 Z" fill="#64B5F6" stroke="#1565C0" stroke-width="1"/>
    <!-- Dorsal fin -->
    <path d="M-5 -15 L5 -25 L15 -15" fill="#90CAF9" stroke="#1565C0" stroke-width="1"/>
    <!-- Pectoral fin -->
    <path d="M-10 8 L-18 18 L-5 14" fill="#90CAF9" stroke="#1565C0" stroke-width="1"/>
    <!-- Eye -->
    <circle cx="-15" cy="-3" r="4" fill="white" stroke="#1565C0" stroke-width="0.8"/>
    <circle cx="-15" cy="-3" r="2" fill="#1565C0"/>
    <!-- Gill -->
    <path d="M-5 -5 Q-5 5 -8 5" stroke="#1565C0" stroke-width="1" fill="none"/>
    <!-- Scales -->
    <path d="M5 0 Q10 -3 15 0" stroke="#1565C0" stroke-width="0.5" fill="none" opacity="0.5"/>
    <path d="M5 5 Q10 2 15 5" stroke="#1565C0" stroke-width="0.5" fill="none" opacity="0.5"/>
    <text x="0" y="32" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" text-anchor="middle" font-weight="bold">Рыбы</text>
    <text x="0" y="42" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Жабры, чешуя</text>
  </g>
  <!-- Amphibian (Земноводные) -->
  <g transform="translate(190,120)">
    <!-- Body -->
    <ellipse cx="0" cy="0" rx="22" ry="14" fill="#81C784" stroke="#2E7D32" stroke-width="1.5"/>
    <!-- Head -->
    <ellipse cx="-18" cy="-2" rx="12" ry="10" fill="#81C784" stroke="#2E7D32" stroke-width="1.5"/>
    <!-- Eyes (bulging) -->
    <circle cx="-22" cy="-8" r="4" fill="#A5D6A7" stroke="#2E7D32" stroke-width="0.8"/>
    <circle cx="-22" cy="-8" r="2" fill="#333"/>
    <!-- Front legs -->
    <line x1="-8" y1="12" x2="-18" y2="25" stroke="#2E7D32" stroke-width="2"/>
    <line x1="5" y1="12" x2="15" y2="25" stroke="#2E7D32" stroke-width="2"/>
    <!-- Back legs (bent) -->
    <path d="M10 10 L20 5 L25 15" stroke="#2E7D32" stroke-width="2.5" fill="none"/>
    <!-- Toes -->
    <line x1="-18" y1="25" x2="-22" y2="28" stroke="#2E7D32" stroke-width="1"/>
    <line x1="-18" y1="25" x2="-16" y2="28" stroke="#2E7D32" stroke-width="1"/>
    <line x1="15" y1="25" x2="11" y2="28" stroke="#2E7D32" stroke-width="1"/>
    <line x1="15" y1="25" x2="17" y2="28" stroke="#2E7D32" stroke-width="1"/>
    <text x="0" y="42" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Земноводные</text>
    <text x="0" y="52" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Лёгкие + кожа</text>
  </g>
  <!-- Reptile (Пресмыкающиеся) -->
  <g transform="translate(310,120)">
    <!-- Body -->
    <ellipse cx="5" cy="0" rx="28" ry="10" fill="#8BC34A" stroke="#33691E" stroke-width="1.5"/>
    <!-- Head -->
    <ellipse cx="-22" cy="-2" rx="12" ry="7" fill="#8BC34A" stroke="#33691E" stroke-width="1.5"/>
    <!-- Eye -->
    <circle cx="-26" cy="-4" r="2.5" fill="#FFEB3B" stroke="#33691E" stroke-width="0.8"/>
    <ellipse cx="-26" cy="-4" rx="1" ry="2.5" fill="#333"/>
    <!-- Tail -->
    <path d="M33 0 Q40 -3 48 -8 Q52 -5 55 -10" stroke="#33691E" stroke-width="2.5" fill="none"/>
    <!-- Legs -->
    <line x1="-5" y1="10" x2="-12" y2="22" stroke="#33691E" stroke-width="2"/>
    <line x1="15" y1="10" x2="22" y2="22" stroke="#33691E" stroke-width="2"/>
    <line x1="-12" y1="22" x2="-18" y2="20" stroke="#33691E" stroke-width="1.5"/>
    <line x1="22" y1="22" x2="28" y2="20" stroke="#33691E" stroke-width="1.5"/>
    <!-- Scales pattern -->
    <path d="M-5 -5 Q0 -8 5 -5" stroke="#33691E" stroke-width="0.5" fill="none" opacity="0.4"/>
    <path d="M5 -5 Q10 -8 15 -5" stroke="#33691E" stroke-width="0.5" fill="none" opacity="0.4"/>
    <path d="M0 3 Q5 0 10 3" stroke="#33691E" stroke-width="0.5" fill="none" opacity="0.4"/>
    <text x="0" y="42" font-family="Arial,sans-serif" font-size="8" fill="#33691E" text-anchor="middle" font-weight="bold">Пресмыкающиеся</text>
    <text x="0" y="52" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Чешуя, лёгкие</text>
  </g>
  <!-- Bird (Птицы) -->
  <g transform="translate(420,115)">
    <!-- Body -->
    <ellipse cx="0" cy="5" rx="18" ry="12" fill="#90CAF9" stroke="#1565C0" stroke-width="1.5"/>
    <!-- Head -->
    <circle cx="-18" cy="-5" r="8" fill="#90CAF9" stroke="#1565C0" stroke-width="1.5"/>
    <!-- Beak -->
    <path d="M-26 -5 L-32 -3 L-26 -1 Z" fill="#FF9800" stroke="#E65100" stroke-width="0.8"/>
    <!-- Eye -->
    <circle cx="-20" cy="-6" r="2" fill="#333"/>
    <!-- Wing -->
    <path d="M-5 -5 Q5 -25 25 -20 Q20 -10 5 0 Z" fill="#64B5F6" stroke="#1565C0" stroke-width="1" opacity="0.8"/>
    <!-- Tail -->
    <path d="M18 0 L30 -8 L28 5 Z" fill="#64B5F6" stroke="#1565C0" stroke-width="1"/>
    <!-- Legs -->
    <line x1="-5" y1="17" x2="-8" y2="28" stroke="#E65100" stroke-width="1.5"/>
    <line x1="5" y1="17" x2="8" y2="28" stroke="#E65100" stroke-width="1.5"/>
    <!-- Toes -->
    <path d="M-8 28 L-12 30 M-8 28 L-5 30" stroke="#E65100" stroke-width="1"/>
    <path d="M8 28 L4 30 M8 28 L11 30" stroke="#E65100" stroke-width="1"/>
    <text x="0" y="45" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" text-anchor="middle" font-weight="bold">Птицы</text>
    <text x="0" y="55" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Перья, полёт</text>
  </g>
  <!-- Mammal (Млекопитающие) -->
  <g transform="translate(250,235)">
    <!-- Body -->
    <ellipse cx="0" cy="0" rx="30" ry="18" fill="#BCAAA4" stroke="#5D4037" stroke-width="1.5"/>
    <!-- Head -->
    <ellipse cx="-30" cy="-5" rx="14" ry="12" fill="#BCAAA4" stroke="#5D4037" stroke-width="1.5"/>
    <!-- Ears -->
    <ellipse cx="-36" cy="-15" rx="5" ry="8" fill="#D7CCC8" stroke="#5D4037" stroke-width="1"/>
    <ellipse cx="-26" cy="-15" rx="5" ry="8" fill="#D7CCC8" stroke="#5D4037" stroke-width="1"/>
    <!-- Eye -->
    <circle cx="-33" cy="-5" r="2.5" fill="#333"/>
    <!-- Nose -->
    <circle cx="-42" cy="-3" r="2" fill="#5D4037"/>
    <!-- Legs -->
    <rect x="-15" y="16" width="6" height="18" fill="#BCAAA4" stroke="#5D4037" stroke-width="1" rx="2"/>
    <rect x="10" y="16" width="6" height="18" fill="#BCAAA4" stroke="#5D4037" stroke-width="1" rx="2"/>
    <!-- Tail -->
    <path d="M30 0 Q40 -5 42 -12" stroke="#5D4037" stroke-width="2" fill="none"/>
    <!-- Fur texture -->
    <path d="M-10 -15 Q-8 -18 -6 -15" stroke="#8D6E63" stroke-width="0.5" fill="none" opacity="0.5"/>
    <path d="M5 -15 Q7 -18 9 -15" stroke="#8D6E63" stroke-width="0.5" fill="none" opacity="0.5"/>
    <text x="0" y="48" font-family="Arial,sans-serif" font-size="8" fill="#5D4037" text-anchor="middle" font-weight="bold">Млекопитающие</text>
    <text x="0" y="58" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Шерсть, молоко</text>
  </g>
  <!-- Evolution arrow -->
  <path d="M40 170 L460 170" stroke="#2E7D32" stroke-width="1.5" stroke-dasharray="5,3"/>
  <path d="M460 170 L455 166 M460 170 L455 174" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
  <text x="250" y="185" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">Эволюция позвоночных</text>
  <!-- Key feature -->
  <rect x="60" y="300" width="380" height="18" rx="3" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="313" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Общее: позвоночник, череп, внутренний скелет, замкнутая кровеносная система</text>
'''

# Generate all SVGs
lessons = [
    (16, "Общая характеристика животных", lesson16_illustration),
    (17, "Простейшие - одноклеточные животные", lesson17_illustration),
    (18, "Кишечнополостные и черви", lesson18_illustration),
    (19, "Моллюски и членистоногие", lesson19_illustration),
    (20, "Позвоночные животные", lesson20_illustration),
]

for num, title, illustration in lessons:
    subtitle = f"Биология 5 класс - Урок {num}"
    svg_content = svg_wrap(illustration, title, subtitle)
    filepath = os.path.join(OUTPUT_DIR, f"lesson{num}.svg")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Generated: {filepath}")

print("\nDone! 5 SVGs generated for Grade 5 Biology Lessons 16-20.")
