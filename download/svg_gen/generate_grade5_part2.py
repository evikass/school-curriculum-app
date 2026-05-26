#!/usr/bin/env python3
"""Generate detailed biology SVG illustrations for Grade 5, lessons 10-18."""
import os

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade5/biology"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def svg_header(title, subtitle, bg1="#E8F5E9", bg2="#C8E6C9", accent="#2E7D32"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{bg1}"/>
      <stop offset="100%" stop-color="{bg2}"/>
    </linearGradient>
    <linearGradient id="hdr" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{accent}"/>
      <stop offset="100%" stop-color="{accent}" opacity="0.7"/>
    </linearGradient>
  </defs>
  <rect width="600" height="400" fill="url(#bg)" rx="12"/>
  <rect x="3" y="3" width="594" height="394" rx="10" fill="none" stroke="{accent}" stroke-width="2"/>
  <text x="300" y="38" font-family="Arial,sans-serif" font-size="18" font-weight="bold" fill="{accent}" text-anchor="middle">{title}</text>
  <text x="300" y="56" font-family="Arial,sans-serif" font-size="11" fill="#777" text-anchor="middle">{subtitle}</text>
  <line x1="30" y1="66" x2="570" y2="66" stroke="{accent}" stroke-width="1.5" opacity="0.3"/>
'''

def svg_footer(title, accent="#2E7D32"):
    return f'''  <rect x="15" y="360" width="570" height="28" rx="5" fill="{accent}" opacity="0.85"/>
  <text x="300" y="380" font-family="Arial,sans-serif" font-size="13" text-anchor="middle" fill="white" font-weight="bold">{title}</text>
</svg>'''

def write_svg(num, content):
    path = os.path.join(OUTPUT_DIR, f"lesson{num}.svg")
    with open(path, 'w') as f:
        f.write(content)
    print(f"  Written: lesson{num}.svg")

# ===== LESSON 10: Корень — подземный орган =====
write_svg(10, svg_header("Корень - подземный орган", "Биология 5 класс - Урок 10", "#EFEBE9", "#D7CCC8", "#5D4037") + '''
  <!-- Root types -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="280" height="275" rx="8" fill="white" stroke="#5D4037" stroke-width="1.5"/>
    <rect x="0" y="0" width="280" height="22" rx="8" fill="#5D4037" opacity="0.85"/>
    <rect x="0" y="14" width="280" height="10" fill="#5D4037" opacity="0.85"/>
    <text x="140" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ТИПЫ КОРНЕВЫХ СИСТЕМ</text>

    <!-- Taproot system -->
    <g transform="translate(70,40)">
      <!-- Plant stem -->
      <rect x="-4" y="-10" width="8" height="20" rx="2" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
      <!-- Main root -->
      <line x1="0" y1="10" x2="0" y2="140" stroke="#8D6E63" stroke-width="4"/>
      <!-- Lateral roots -->
      <line x1="0" y1="40" x2="-25" y2="60" stroke="#8D6E63" stroke-width="2"/>
      <line x1="-25" y1="60" x2="-35" y2="75" stroke="#8D6E63" stroke-width="1.2"/>
      <line x1="0" y1="55" x2="20" y2="75" stroke="#8D6E63" stroke-width="2"/>
      <line x1="20" y1="75" x2="30" y2="90" stroke="#8D6E63" stroke-width="1.2"/>
      <line x1="0" y1="80" x2="-20" y2="100" stroke="#8D6E63" stroke-width="2"/>
      <line x1="-20" y1="100" x2="-28" y2="115" stroke="#8D6E63" stroke-width="1"/>
      <line x1="0" y1="100" x2="18" y2="118" stroke="#8D6E63" stroke-width="1.5"/>
      <!-- Root hairs -->
      <line x1="0" y1="130" x2="-5" y2="133" stroke="#A1887F" stroke-width="0.5"/>
      <line x1="0" y1="135" x2="4" y2="138" stroke="#A1887F" stroke-width="0.5"/>
      <!-- Soil -->
      <line x1="-40" y1="10" x2="40" y2="10" stroke="#795548" stroke-width="1" stroke-dasharray="3,2"/>
    </g>
    <text x="70" y="195" font-family="Arial,sans-serif" font-size="9" fill="#5D4037" text-anchor="middle" font-weight="bold">Стержневая</text>
    <text x="70" y="210" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">(горох, фасоль,</text>
    <text x="70" y="222" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">одуванчик)</text>

    <!-- Fibrous root system -->
    <g transform="translate(210,40)">
      <rect x="-4" y="-10" width="8" height="20" rx="2" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
      <!-- Many equal roots -->
      <line x1="0" y1="10" x2="-15" y2="50" stroke="#8D6E63" stroke-width="2"/>
      <line x1="0" y1="10" x2="-8" y2="55" stroke="#8D6E63" stroke-width="2"/>
      <line x1="0" y1="10" x2="0" y2="55" stroke="#8D6E63" stroke-width="2.5"/>
      <line x1="0" y1="10" x2="8" y2="55" stroke="#8D6E63" stroke-width="2"/>
      <line x1="0" y1="10" x2="15" y2="50" stroke="#8D6E63" stroke-width="2"/>
      <!-- Branches -->
      <line x1="-15" y1="50" x2="-25" y2="70" stroke="#8D6E63" stroke-width="1.2"/>
      <line x1="-15" y1="50" x2="-18" y2="72" stroke="#8D6E63" stroke-width="1"/>
      <line x1="0" y1="55" x2="-5" y2="75" stroke="#8D6E63" stroke-width="1.2"/>
      <line x1="0" y1="55" x2="5" y2="75" stroke="#8D6E63" stroke-width="1.2"/>
      <line x1="15" y1="50" x2="25" y2="70" stroke="#8D6E63" stroke-width="1.2"/>
      <line x1="15" y1="50" x2="18" y2="72" stroke="#8D6E63" stroke-width="1"/>
      <!-- More branches -->
      <line x1="-8" y1="55" x2="-15" y2="80" stroke="#8D6E63" stroke-width="1"/>
      <line x1="8" y1="55" x2="15" y2="80" stroke="#8D6E63" stroke-width="1"/>
      <line x1="0" y1="55" x2="0" y2="85" stroke="#8D6E63" stroke-width="1.5"/>
      <!-- Root hairs -->
      <line x1="-25" y1="70" x2="-28" y2="75" stroke="#A1887F" stroke-width="0.5"/>
      <line x1="25" y1="70" x2="28" y2="75" stroke="#A1887F" stroke-width="0.5"/>
      <line x1="-40" y1="10" x2="40" y2="10" stroke="#795548" stroke-width="1" stroke-dasharray="3,2"/>
    </g>
    <text x="210" y="195" font-family="Arial,sans-serif" font-size="9" fill="#5D4037" text-anchor="middle" font-weight="bold">Мочковатая</text>
    <text x="210" y="210" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">(пшеница, лук,</text>
    <text x="210" y="222" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">кукуруза)</text>

    <!-- Root zones -->
    <rect x="10" y="235" width="260" height="30" rx="4" fill="#EFEBE9" stroke="#8D6E63" stroke-width="1"/>
    <text x="140" y="254" font-family="Arial,sans-serif" font-size="8" fill="#5D4037" text-anchor="middle">Зоны корня: деления -> роста -> всасывания -> проведения</text>
  </g>

  <!-- Root cross-section -->
  <g transform="translate(310,75)">
    <rect x="0" y="0" width="275" height="275" rx="8" fill="white" stroke="#5D4037" stroke-width="1.5"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#5D4037" opacity="0.85"/>
    <rect x="0" y="14" width="275" height="10" fill="#5D4037" opacity="0.85"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ЗОНЫ КОРНЯ</text>

    <!-- Longitudinal section of root -->
    <!-- Root tip -->
    <path d="M120,45 Q100,50 90,70 Q85,90 90,110 Q95,140 110,170 Q120,200 120,230" fill="none" stroke="#8D6E63" stroke-width="3"/>
    <path d="M150,45 Q170,50 180,70 Q185,90 180,110 Q175,140 160,170 Q150,200 150,230" fill="none" stroke="#8D6E63" stroke-width="3"/>
    <!-- Fill -->
    <path d="M120,45 Q135,40 150,45 Q170,50 180,70 Q185,90 180,110 Q175,140 160,170 Q150,200 150,230 Q135,240 120,230 Q120,200 110,170 Q95,140 90,110 Q85,90 90,70 Q100,50 120,45 Z" fill="#EFEBE9" stroke="none"/>

    <!-- Root cap -->
    <path d="M120,45 Q135,38 150,45 Q140,55 130,55 Q120,55 120,45 Z" fill="#BCAAA4" stroke="#5D4037" stroke-width="1"/>
    <text x="210" y="50" font-family="Arial,sans-serif" font-size="8" fill="#5D4037">Корневой чехлик</text>
    <line x1="200" y1="48" x2="158" y2="48" stroke="#5D4037" stroke-width="0.6"/>

    <!-- Zone of division -->
    <rect x="118" y="58" width="34" height="30" rx="2" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1" opacity="0.7"/>
    <text x="210" y="75" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32">Зона деления</text>
    <line x1="200" y1="73" x2="155" y2="73" stroke="#2E7D32" stroke-width="0.6"/>
    <!-- Small dividing cells -->
    <rect x="122" y="62" width="5" height="5" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
    <rect x="129" y="62" width="5" height="5" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
    <rect x="136" y="62" width="5" height="5" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
    <rect x="125" y="69" width="5" height="5" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>
    <rect x="132" y="69" width="5" height="5" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/>

    <!-- Zone of elongation -->
    <rect x="116" y="90" width="38" height="25" rx="2" fill="#FFF9C4" stroke="#F9A825" stroke-width="1" opacity="0.7"/>
    <text x="210" y="105" font-family="Arial,sans-serif" font-size="8" fill="#F9A825">Зона роста</text>
    <line x1="200" y1="103" x2="157" y2="103" stroke="#F9A825" stroke-width="0.6"/>

    <!-- Zone of absorption (root hairs) -->
    <rect x="112" y="118" width="46" height="35" rx="2" fill="#BBDEFB" stroke="#1565C0" stroke-width="1" opacity="0.7"/>
    <!-- Root hairs -->
    <line x1="112" y1="125" x2="95" y2="122" stroke="#1565C0" stroke-width="1"/>
    <line x1="112" y1="132" x2="92" y2="130" stroke="#1565C0" stroke-width="1"/>
    <line x1="112" y1="140" x2="93" y2="139" stroke="#1565C0" stroke-width="1"/>
    <line x1="158" y1="125" x2="175" y2="122" stroke="#1565C0" stroke-width="1"/>
    <line x1="158" y1="132" x2="178" y2="130" stroke="#1565C0" stroke-width="1"/>
    <line x1="158" y1="140" x2="177" y2="139" stroke="#1565C0" stroke-width="1"/>
    <text x="210" y="138" font-family="Arial,sans-serif" font-size="8" fill="#1565C0">Зона всасывания</text>
    <line x1="200" y1="136" x2="160" y2="136" stroke="#1565C0" stroke-width="0.6"/>
    <text x="210" y="150" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">(корневые волоски)</text>

    <!-- Zone of conduction -->
    <rect x="108" y="158" width="54" height="70" rx="2" fill="#FFCCBC" stroke="#BF360C" stroke-width="1" opacity="0.5"/>
    <text x="210" y="175" font-family="Arial,sans-serif" font-size="8" fill="#BF360C">Зона проведения</text>
    <line x1="200" y1="173" x2="165" y2="180" stroke="#BF360C" stroke-width="0.6"/>

    <!-- Functions summary -->
    <text x="60" y="245" font-family="Arial,sans-serif" font-size="8" fill="#5D4037">Функции корня:</text>
    <text x="60" y="258" font-family="Arial,sans-serif" font-size="7" fill="#555">1. Закрепление в почве</text>
    <text x="60" y="270" font-family="Arial,sans-serif" font-size="7" fill="#555">2. Всасывание воды и минералов</text>
    <text x="60" y="282" font-family="Arial,sans-serif" font-size="7" fill="#555">3. Транспорт веществ</text>
  </g>
''' + svg_footer("Корень - подземный орган", "#5D4037"))

# ===== LESSON 11: Побег и листья =====
write_svg(11, svg_header("Побег и листья", "Биология 5 класс - Урок 11") + '''
  <!-- Shoot structure -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="280" height="275" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
    <rect x="0" y="0" width="280" height="22" rx="8" fill="#2E7D32" opacity="0.85"/>
    <rect x="0" y="14" width="280" height="10" fill="#2E7D32" opacity="0.85"/>
    <text x="140" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">СТРОЕНИЕ ПОБЕГА</text>

    <!-- Main stem -->
    <rect x="133" y="35" width="8" height="210" rx="2" fill="#81C784" stroke="#2E7D32" stroke-width="1.5"/>
    <!-- Nodes -->
    <ellipse cx="137" cy="70" rx="12" ry="3" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
    <ellipse cx="137" cy="130" rx="12" ry="3" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
    <ellipse cx="137" cy="190" rx="12" ry="3" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
    <!-- Internodes label -->
    <line x1="155" y1="70" x2="175" y2="70" stroke="#2E7D32" stroke-width="0.8"/>
    <line x1="155" y1="130" x2="175" y2="130" stroke="#2E7D32" stroke-width="0.8"/>
    <line x1="175" y1="70" x2="175" y2="130" stroke="#2E7D32" stroke-width="0.8"/>
    <text x="195" y="95" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">междо-</text>
    <text x="195" y="105" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">узлие</text>

    <!-- Node label -->
    <line x1="155" y1="130" x2="175" y2="140" stroke="#2E7D32" stroke-width="0.8"/>
    <text x="178" y="140" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">узел</text>

    <!-- Leaves at nodes -->
    <path d="M133,68 Q100,55 80,65 Q100,80 133,72" fill="#66BB6A" stroke="#2E7D32" stroke-width="1.2"/>
    <line x1="133" y1="70" x2="82" y2="66" stroke="#2E7D32" stroke-width="0.8"/>
    <path d="M141,68 Q170,52 190,62 Q170,78 141,72" fill="#66BB6A" stroke="#2E7D32" stroke-width="1.2"/>
    <line x1="141" y1="70" x2="188" y2="64" stroke="#2E7D32" stroke-width="0.8"/>

    <path d="M133,128 Q100,115 80,125 Q100,140 133,132" fill="#4CAF50" stroke="#2E7D32" stroke-width="1.2"/>
    <path d="M141,128 Q170,112 190,122 Q170,138 141,132" fill="#4CAF50" stroke="#2E7D32" stroke-width="1.2"/>

    <path d="M133,188 Q105,175 90,185 Q105,200 133,192" fill="#388E3C" stroke="#2E7D32" stroke-width="1.2"/>
    <path d="M141,188 Q165,175 180,185 Q165,200 141,192" fill="#388E3C" stroke="#2E7D32" stroke-width="1.2"/>

    <!-- Apical bud -->
    <ellipse cx="137" cy="38" rx="10" ry="8" fill="#A5D6A7" stroke="#1B5E20" stroke-width="1.5"/>
    <text x="137" y="32" font-family="Arial,sans-serif" font-size="7" fill="#1B5E20" text-anchor="middle">почки</text>

    <!-- Axillary buds -->
    <ellipse cx="118" cy="72" rx="6" ry="5" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
    <ellipse cx="156" cy="72" rx="6" ry="5" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>

    <text x="80" y="88" font-family="Arial,sans-serif" font-size="7" fill="#555">лист</text>
    <text x="80" y="148" font-family="Arial,sans-serif" font-size="7" fill="#555">лист</text>
  </g>

  <!-- Leaf structure -->
  <g transform="translate(310,75)">
    <rect x="0" y="0" width="275" height="275" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#2E7D32" opacity="0.85"/>
    <rect x="0" y="14" width="275" height="10" fill="#2E7D32" opacity="0.85"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">СТРОЕНИЕ ЛИСТА</text>

    <!-- Large leaf -->
    <path d="M138,40 Q80,60 50,100 Q40,140 60,160 Q90,180 138,175 Q186,180 216,160 Q236,140 226,100 Q196,60 138,40 Z" fill="#81C784" stroke="#2E7D32" stroke-width="2"/>
    <!-- Main vein (midrib) -->
    <line x1="138" y1="40" x2="138" y2="175" stroke="#4CAF50" stroke-width="2.5"/>
    <!-- Side veins -->
    <line x1="138" y1="65" x2="90" y2="85" stroke="#4CAF50" stroke-width="1.2"/>
    <line x1="138" y1="65" x2="186" y2="85" stroke="#4CAF50" stroke-width="1.2"/>
    <line x1="138" y1="95" x2="75" y2="115" stroke="#4CAF50" stroke-width="1"/>
    <line x1="138" y1="95" x2="201" y2="115" stroke="#4CAF50" stroke-width="1"/>
    <line x1="138" y1="125" x2="80" y2="140" stroke="#4CAF50" stroke-width="1"/>
    <line x1="138" y1="125" x2="196" y2="140" stroke="#4CAF50" stroke-width="1"/>
    <line x1="138" y1="150" x2="95" y2="160" stroke="#4CAF50" stroke-width="0.8"/>
    <line x1="138" y1="150" x2="181" y2="160" stroke="#4CAF50" stroke-width="0.8"/>
    <!-- Fine veins -->
    <line x1="90" y1="85" x2="75" y2="78" stroke="#66BB6A" stroke-width="0.5"/>
    <line x1="186" y1="85" x2="201" y2="78" stroke="#66BB6A" stroke-width="0.5"/>

    <!-- Petiole -->
    <rect x="134" y="175" width="8" height="30" rx="2" fill="#81C784" stroke="#2E7D32" stroke-width="1.5"/>

    <!-- Labels -->
    <text x="30" y="60" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32">Листовая</text>
    <text x="30" y="72" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32">пластинка</text>
    <line x1="80" y1="68" x2="65" y2="100" stroke="#2E7D32" stroke-width="0.6"/>

    <text x="200" y="60" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32">Жилкование</text>
    <line x1="200" y1="62" x2="186" y2="80" stroke="#2E7D32" stroke-width="0.6"/>

    <text x="155" y="215" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32">Черешок</text>
    <line x1="155" y1="210" x2="145" y2="200" stroke="#2E7D32" stroke-width="0.6"/>

    <!-- Leaf types -->
    <rect x="10" y="225" width="255" height="40" rx="4" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
    <text x="138" y="242" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Типы жилкования:</text>
    <text x="138" y="256" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Сетчатое (двудольные) | Параллельное | Дуговое (однодольные)</text>
  </g>
''' + svg_footer("Побег и листья"))

# ===== LESSON 12: Цветок и плод =====
write_svg(12, svg_header("Цветок и плод", "Биология 5 класс - Урок 12", "#FCE4EC", "#F8BBD0", "#AD1457") + '''
  <!-- Flower anatomy -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="280" height="275" rx="8" fill="white" stroke="#AD1457" stroke-width="1.5"/>
    <rect x="0" y="0" width="280" height="22" rx="8" fill="#AD1457" opacity="0.85"/>
    <rect x="0" y="14" width="280" height="10" fill="#AD1457" opacity="0.85"/>
    <text x="140" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">СТРОЕНИЕ ЦВЕТКА</text>

    <!-- Flower diagram centered -->
    <g transform="translate(140,145)">
      <!-- Peduncle -->
      <rect x="-4" y="60" width="8" height="50" rx="2" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
      <!-- Receptacle -->
      <ellipse cx="0" cy="58" rx="15" ry="6" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>

      <!-- Sepals (calyx) -->
      <path d="M0,50 Q-30,30 -35,45 Q-25,55 0,50 Z" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
      <path d="M0,50 Q30,30 35,45 Q25,55 0,50 Z" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
      <path d="M0,50 Q-15,25 -20,42 Q-10,55 0,50 Z" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>
      <path d="M0,50 Q15,25 20,42 Q10,55 0,50 Z" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>

      <!-- Petals (corolla) -->
      <path d="M0,40 Q-35,0 -25,-30 Q-10,-20 0,40 Z" fill="#F48FB1" stroke="#C2185B" stroke-width="1.2"/>
      <path d="M0,40 Q35,0 25,-30 Q10,-20 0,40 Z" fill="#F48FB1" stroke="#C2185B" stroke-width="1.2"/>
      <path d="M0,40 Q-45,10 -45,-15 Q-25,-10 0,40 Z" fill="#EC407A" stroke="#C2185B" stroke-width="1"/>
      <path d="M0,40 Q45,10 45,-15 Q25,-10 0,40 Z" fill="#EC407A" stroke="#C2185B" stroke-width="1"/>
      <path d="M0,40 Q-20,-15 0,-40 Q20,-15 0,40 Z" fill="#F06292" stroke="#C2185B" stroke-width="1.2"/>

      <!-- Stamens (androeceum) -->
      <line x1="-15" y1="20" x2="-22" y2="-5" stroke="#FFB300" stroke-width="1.5"/>
      <circle cx="-22" cy="-8" r="4" fill="#FDD835" stroke="#F9A825" stroke-width="1"/>
      <line x1="15" y1="20" x2="22" y2="-5" stroke="#FFB300" stroke-width="1.5"/>
      <circle cx="22" cy="-8" r="4" fill="#FDD835" stroke="#F9A825" stroke-width="1"/>
      <line x1="-8" y1="15" x2="-12" y2="-10" stroke="#FFB300" stroke-width="1.2"/>
      <circle cx="-12" cy="-13" r="3.5" fill="#FDD835" stroke="#F9A825" stroke-width="0.8"/>
      <line x1="8" y1="15" x2="12" y2="-10" stroke="#FFB300" stroke-width="1.2"/>
      <circle cx="12" cy="-13" r="3.5" fill="#FDD835" stroke="#F9A825" stroke-width="0.8"/>

      <!-- Pistil (gynoeceum) -->
      <ellipse cx="0" cy="15" rx="8" ry="12" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1.5"/>
      <line x1="0" y1="3" x2="0" y2="-20" stroke="#4CAF50" stroke-width="1.5"/>
      <ellipse cx="0" cy="-22" rx="4" ry="5" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
    </g>

    <!-- Labels with lines -->
    <text x="20" y="85" font-family="Arial,sans-serif" font-size="7" fill="#C2185B">лепестки</text>
    <line x1="55" y1="87" x2="95" y2="100" stroke="#C2185B" stroke-width="0.5"/>
    <text x="200" y="90" font-family="Arial,sans-serif" font-size="7" fill="#F9A825">тычинки</text>
    <line x1="200" y1="92" x2="162" y2="115" stroke="#F9A825" stroke-width="0.5"/>
    <text x="20" y="130" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">пестик</text>
    <line x1="45" y1="128" x2="125" y2="145" stroke="#2E7D32" stroke-width="0.5"/>
    <text x="200" y="155" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">чашелистики</text>
    <line x1="200" y1="153" x2="170" y2="175" stroke="#2E7D32" stroke-width="0.5"/>
    <text x="20" y="200" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">цветоложе</text>
    <line x1="60" y1="198" x2="120" y2="200" stroke="#2E7D32" stroke-width="0.5"/>
    <text x="200" y="220" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">цветоножка</text>
    <line x1="200" y1="218" x2="145" y2="215" stroke="#2E7D32" stroke-width="0.5"/>
  </g>

  <!-- Fruit types -->
  <g transform="translate(310,75)">
    <rect x="0" y="0" width="275" height="275" rx="8" fill="white" stroke="#AD1457" stroke-width="1.5"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#AD1457" opacity="0.85"/>
    <rect x="0" y="14" width="275" height="10" fill="#AD1457" opacity="0.85"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ТИПЫ ПЛОДОВ</text>

    <!-- Apple (pomum) -->
    <circle cx="55" cy="70" r="22" fill="#EF5350" stroke="#C62828" stroke-width="1.5"/>
    <line x1="55" y1="48" x2="55" y2="42" stroke="#2E7D32" stroke-width="1.5"/>
    <ellipse cx="55" cy="42" rx="6" ry="3" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>
    <!-- Cross section inset -->
    <circle cx="55" cy="110" r="18" fill="#FFCDD2" stroke="#C62828" stroke-width="1"/>
    <circle cx="55" cy="110" r="10" fill="#EF9A9A" stroke="none"/>
    <circle cx="48" cy="108" r="2.5" fill="#5D4037" stroke="#3E2723" stroke-width="0.5"/>
    <circle cx="62" cy="108" r="2.5" fill="#5D4037" stroke="#3E2723" stroke-width="0.5"/>
    <circle cx="55" cy="118" r="2.5" fill="#5D4037" stroke="#3E2723" stroke-width="0.5"/>
    <text x="55" y="140" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Яблоко</text>
    <text x="55" y="152" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">(яблоко)</text>

    <!-- Plum (drupe) -->
    <ellipse cx="138" cy="65" rx="16" ry="20" fill="#7B1FA2" stroke="#4A148C" stroke-width="1.5"/>
    <line x1="138" y1="45" x2="138" y2="40" stroke="#2E7D32" stroke-width="1.2"/>
    <!-- Cross section -->
    <ellipse cx="138" cy="110" rx="14" ry="18" fill="#CE93D8" stroke="#4A148C" stroke-width="1"/>
    <ellipse cx="138" cy="110" rx="6" ry="8" fill="#5D4037" stroke="#3E2723" stroke-width="1"/>
    <text x="138" y="140" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Слива</text>
    <text x="138" y="152" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">(костянка)</text>

    <!-- Pea pod (legume) -->
    <path d="M200,55 Q210,50 225,55 Q235,65 225,80 Q210,85 200,75 Q195,65 200,55 Z" fill="#8BC34A" stroke="#558B2F" stroke-width="1.5"/>
    <circle cx="210" cy="65" r="4" fill="#689F38" stroke="#33691E" stroke-width="0.8"/>
    <circle cx="220" cy="68" r="3.5" fill="#689F38" stroke="#33691E" stroke-width="0.8"/>
    <line x1="200" y1="65" x2="235" y2="68" stroke="#33691E" stroke-width="0.5"/>
    <!-- Open pod -->
    <path d="M200,100 Q205,95 225,98 L220,120 Q210,115 200,120 Z" fill="#CDDC39" stroke="#558B2F" stroke-width="1"/>
    <path d="M225,98 Q230,95 235,100 L230,120 Q225,115 220,120 Z" fill="#C5E1A5" stroke="#558B2F" stroke-width="1"/>
    <circle cx="212" cy="110" r="4" fill="#689F38" stroke="#33691E" stroke-width="0.8"/>
    <circle cx="222" cy="108" r="3.5" fill="#689F38" stroke="#33691E" stroke-width="0.8"/>
    <text x="218" y="140" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Горох</text>
    <text x="218" y="152" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">(боб)</text>

    <!-- Sunflower seeds (achene) -->
    <ellipse cx="55" cy="185" rx="6" ry="10" fill="#5D4037" stroke="#3E2723" stroke-width="1"/>
    <ellipse cx="68" cy="183" rx="6" ry="10" fill="#5D4037" stroke="#3E2723" stroke-width="1"/>
    <ellipse cx="55" cy="205" rx="6" ry="10" fill="#795548" stroke="#4E342E" stroke-width="1"/>
    <text x="60" y="228" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Подсолнух</text>
    <text x="60" y="240" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">(семянка)</text>

    <!-- Raspberry (multiple fruit) -->
    <circle cx="145" cy="195" r="8" fill="#EF5350" stroke="#C62828" stroke-width="0.8"/>
    <circle cx="155" cy="192" r="8" fill="#F44336" stroke="#C62828" stroke-width="0.8"/>
    <circle cx="150" cy="202" r="8" fill="#E53935" stroke="#C62828" stroke-width="0.8"/>
    <circle cx="140" cy="200" r="7" fill="#EF5350" stroke="#C62828" stroke-width="0.8"/>
    <circle cx="148" cy="188" r="7" fill="#F44336" stroke="#C62828" stroke-width="0.8"/>
    <text x="148" y="225" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Малина</text>
    <text x="148" y="237" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">(многокостянка)</text>

    <!-- Strawberry -->
    <path d="M220,180 Q235,170 245,180 Q250,195 240,205 Q225,210 215,200 Q210,190 220,180 Z" fill="#F44336" stroke="#C62828" stroke-width="1.5"/>
    <circle cx="225" cy="188" r="1.5" fill="#FDD835"/>
    <circle cx="235" cy="185" r="1.5" fill="#FDD835"/>
    <circle cx="230" cy="195" r="1.5" fill="#FDD835"/>
    <circle cx="240" cy="195" r="1.5" fill="#FDD835"/>
    <circle cx="220" cy="198" r="1.5" fill="#FDD835"/>
    <text x="230" y="225" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Земляника</text>
    <text x="230" y="237" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">(многоорешек)</text>

    <!-- Diagram: flower to fruit -->
    <rect x="10" y="248" width="255" height="20" rx="3" fill="#FCE4EC" stroke="#AD1457" stroke-width="0.8"/>
    <text x="138" y="262" font-family="Arial,sans-serif" font-size="8" fill="#AD1457" text-anchor="middle">Цветок -> Опыление -> Оплодотворение -> Плод с семенами</text>
  </g>
''' + svg_footer("Цветок и плод", "#AD1457"))

# ===== LESSON 13: Одноклеточные животные =====
write_svg(13, svg_header("Одноклеточные животные", "Биология 5 класс - Урок 13", "#E3F2FD", "#BBDEFB", "#0D47A1") + '''
  <!-- Amoeba -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="185" height="165" rx="8" fill="white" stroke="#0D47A1" stroke-width="1.5"/>
    <rect x="0" y="0" width="185" height="22" rx="8" fill="#0D47A1" opacity="0.85"/>
    <rect x="0" y="14" width="185" height="10" fill="#0D47A1" opacity="0.85"/>
    <text x="93" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">АМЕБА</text>

    <!-- Amoeba shape (irregular) -->
    <path d="M80,60 Q50,50 40,70 Q30,90 50,100 Q40,115 55,130 Q70,140 90,135 Q110,140 120,125 Q135,120 130,100 Q140,85 125,70 Q115,55 100,60 Q90,50 80,60 Z" fill="#BBDEFB" stroke="#0D47A1" stroke-width="2"/>
    <!-- Nucleus -->
    <circle cx="85" cy="90" r="12" fill="#90CAF9" stroke="#0D47A1" stroke-width="1.5"/>
    <text x="85" y="93" font-family="Arial,sans-serif" font-size="6" fill="#0D47A1" text-anchor="middle">ядро</text>
    <!-- Contractile vacuole -->
    <circle cx="110" cy="75" r="6" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
    <text x="128" y="75" font-family="Arial,sans-serif" font-size="5" fill="#1565C0">сокр.</text>
    <text x="128" y="82" font-family="Arial,sans-serif" font-size="5" fill="#1565C0">вакуоль</text>
    <!-- Food vacuole -->
    <circle cx="65" cy="105" r="7" fill="#FFCDD2" stroke="#C62828" stroke-width="0.8"/>
    <text x="65" y="108" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">пища</text>
    <!-- Pseudopods -->
    <path d="M40,70 Q25,60 20,55" fill="none" stroke="#0D47A1" stroke-width="1.5"/>
    <path d="M55,130 Q45,140 35,138" fill="none" stroke="#0D47A1" stroke-width="1.5"/>
    <text x="25" y="55" font-family="Arial,sans-serif" font-size="5" fill="#0D47A1">ложно-</text>
    <text x="25" y="62" font-family="Arial,sans-serif" font-size="5" fill="#0D47A1">ножки</text>
  </g>

  <!-- Paramecium -->
  <g transform="translate(210,75)">
    <rect x="0" y="0" width="185" height="165" rx="8" fill="white" stroke="#0D47A1" stroke-width="1.5"/>
    <rect x="0" y="0" width="185" height="22" rx="8" fill="#0D47A1" opacity="0.85"/>
    <rect x="0" y="14" width="185" height="10" fill="#0D47A1" opacity="0.85"/>
    <text x="93" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ИНФУЗОРИЯ-ТУФЕЛЬКА</text>

    <!-- Paramecium shape (slipper) -->
    <path d="M75,45 Q55,55 50,80 Q48,105 60,125 Q75,140 95,138 Q115,135 125,115 Q135,95 130,70 Q125,50 105,45 Q90,40 75,45 Z" fill="#BBDEFB" stroke="#0D47A1" stroke-width="2"/>
    <!-- Cilia -->
    <line x1="52" y1="60" x2="42" y2="57" stroke="#1565C0" stroke-width="0.8"/>
    <line x1="48" y1="75" x2="38" y2="73" stroke="#1565C0" stroke-width="0.8"/>
    <line x1="48" y1="90" x2="38" y2="88" stroke="#1565C0" stroke-width="0.8"/>
    <line x1="50" y1="105" x2="40" y2="103" stroke="#1565C0" stroke-width="0.8"/>
    <line x1="55" y1="118" x2="45" y2="117" stroke="#1565C0" stroke-width="0.8"/>
    <line x1="130" y1="65" x2="140" y2="63" stroke="#1565C0" stroke-width="0.8"/>
    <line x1="132" y1="80" x2="142" y2="78" stroke="#1565C0" stroke-width="0.8"/>
    <line x1="130" y1="95" x2="140" y2="93" stroke="#1565C0" stroke-width="0.8"/>
    <line x1="125" y1="110" x2="135" y2="108" stroke="#1565C0" stroke-width="0.8"/>
    <!-- Macronucleus -->
    <ellipse cx="85" cy="85" rx="15" ry="10" fill="#90CAF9" stroke="#0D47A1" stroke-width="1.5"/>
    <!-- Micronucleus -->
    <circle cx="95" cy="82" r="4" fill="#64B5F6" stroke="#0D47A1" stroke-width="1"/>
    <!-- Oral groove -->
    <path d="M75,55 Q70,70 72,85 Q75,95 80,100" fill="none" stroke="#0D47A1" stroke-width="1.5"/>
    <!-- Contractile vacuoles -->
    <circle cx="110" cy="60" r="5" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
    <circle cx="105" cy="115" r="5" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
    <!-- Labels -->
    <text x="155" y="55" font-family="Arial,sans-serif" font-size="6" fill="#1565C0">реснички</text>
    <text x="155" y="75" font-family="Arial,sans-serif" font-size="6" fill="#0D47A1">макроядро</text>
    <text x="155" y="90" font-family="Arial,sans-serif" font-size="6" fill="#0D47A1">микроядро</text>
    <text x="155" y="110" font-family="Arial,sans-serif" font-size="6" fill="#1565C0">сокр. вакуоли</text>
    <text x="155" y="130" font-family="Arial,sans-serif" font-size="6" fill="#0D47A1">ротовая ямка</text>
  </g>

  <!-- Euglena -->
  <g transform="translate(405,75)">
    <rect x="0" y="0" width="185" height="165" rx="8" fill="white" stroke="#0D47A1" stroke-width="1.5"/>
    <rect x="0" y="0" width="185" height="22" rx="8" fill="#0D47A1" opacity="0.85"/>
    <rect x="0" y="14" width="185" height="10" fill="#0D47A1" opacity="0.85"/>
    <text x="93" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ЭВГЛЕНА ЗЕЛЁНАЯ</text>

    <!-- Euglena shape (spindle) -->
    <path d="M70,80 Q55,65 60,50 Q75,35 95,35 Q115,35 125,50 Q130,65 115,80 Q120,100 105,115 Q90,125 75,115 Q60,100 70,80 Z" fill="#C8E6C9" stroke="#2E7D32" stroke-width="2"/>
    <!-- Flagellum -->
    <path d="M95,35 Q100,20 110,15 Q120,10 125,20" fill="none" stroke="#2E7D32" stroke-width="1.5"/>
    <!-- Eye spot -->
    <circle cx="88" cy="45" r="4" fill="#EF5350" stroke="#C62828" stroke-width="0.8"/>
    <text x="120" y="45" font-family="Arial,sans-serif" font-size="6" fill="#C62828">глазок</text>
    <!-- Chloroplasts -->
    <ellipse cx="80" cy="70" rx="8" ry="4" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
    <ellipse cx="100" cy="75" rx="8" ry="4" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
    <ellipse cx="90" cy="90" rx="8" ry="4" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
    <!-- Nucleus -->
    <circle cx="90" cy="100" r="7" fill="#A5D6A7" stroke="#1B5E20" stroke-width="1"/>
    <!-- Pellicle lines -->
    <line x1="65" y1="60" x2="120" y2="60" stroke="#388E3C" stroke-width="0.3" opacity="0.4"/>
    <line x1="60" y1="75" x2="120" y2="75" stroke="#388E3C" stroke-width="0.3" opacity="0.4"/>
    <line x1="65" y1="90" x2="115" y2="90" stroke="#388E3C" stroke-width="0.3" opacity="0.4"/>
    <text x="130" y="70" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">хлоропласты</text>
    <text x="130" y="85" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">(фотосинтез)</text>
    <text x="130" y="105" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">ядро</text>
    <text x="90" y="140" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Жгутик для движения</text>
  </g>

  <!-- Comparison table -->
  <g transform="translate(15,255)">
    <rect x="0" y="0" width="570" height="95" rx="8" fill="white" stroke="#0D47A1" stroke-width="1.5"/>
    <text x="285" y="18" font-family="Arial,sans-serif" font-size="10" fill="#0D47A1" text-anchor="middle" font-weight="bold">СРАВНЕНИЕ ОДНОКЛЕТОЧНЫХ</text>
    <line x1="10" y1="25" x2="560" y2="25" stroke="#BBDEFB" stroke-width="1"/>
    <text x="95" y="38" font-family="Arial,sans-serif" font-size="8" fill="#0D47A1" font-weight="bold" text-anchor="middle">Признак</text>
    <text x="250" y="38" font-family="Arial,sans-serif" font-size="8" fill="#0D47A1" font-weight="bold" text-anchor="middle">Амеба</text>
    <text x="400" y="38" font-family="Arial,sans-serif" font-size="8" fill="#0D47A1" font-weight="bold" text-anchor="middle">Инфузория</text>
    <text x="520" y="38" font-family="Arial,sans-serif" font-size="8" fill="#0D47A1" font-weight="bold" text-anchor="middle">Эвглена</text>
    <line x1="10" y1="42" x2="560" y2="42" stroke="#BBDEFB" stroke-width="0.5"/>
    <text x="95" y="55" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Движение</text>
    <text x="250" y="55" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Ложноножки</text>
    <text x="400" y="55" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Реснички</text>
    <text x="520" y="55" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Жгутик</text>
    <text x="95" y="70" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Питание</text>
    <text x="250" y="70" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Захват пищи</text>
    <text x="400" y="70" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Ротовая ямка</text>
    <text x="520" y="70" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Свет + захват</text>
    <text x="95" y="85" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Особенность</text>
    <text x="250" y="85" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Изменяет форму</text>
    <text x="400" y="85" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Два ядра</text>
    <text x="520" y="85" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Хлоропласты</text>
  </g>
''' + svg_footer("Одноклеточные животные", "#0D47A1"))

# ===== LESSON 14: Кишечнополостные =====
write_svg(14, svg_header("Кишечнополостные", "Биология 5 класс - Урок 14", "#E0F7FA", "#B2EBF2", "#00695C") + '''
  <!-- Hydra -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="280" height="275" rx="8" fill="white" stroke="#00695C" stroke-width="1.5"/>
    <rect x="0" y="0" width="280" height="22" rx="8" fill="#00695C" opacity="0.85"/>
    <rect x="0" y="14" width="280" height="10" fill="#00695C" opacity="0.85"/>
    <text x="140" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ГИДРА</text>

    <!-- Hydra body -->
    <path d="M120,40 Q100,50 95,80 Q90,130 100,180 Q105,200 110,220 Q120,240 130,250 Q140,240 150,220 Q155,200 160,180 Q170,130 165,80 Q160,50 140,40 Z" fill="#B2EBF2" stroke="#00695C" stroke-width="2"/>
    <!-- Tentacles -->
    <path d="M110,42 Q90,20 80,30 Q70,40 75,50" fill="none" stroke="#00695C" stroke-width="2" stroke-linecap="round"/>
    <path d="M120,38 Q110,10 100,15 Q90,20 95,30" fill="none" stroke="#00695C" stroke-width="2" stroke-linecap="round"/>
    <path d="M130,36 Q130,5 125,5 Q120,5 120,15" fill="none" stroke="#00695C" stroke-width="2" stroke-linecap="round"/>
    <path d="M140,38 Q150,10 160,15 Q170,20 165,30" fill="none" stroke="#00695C" stroke-width="2" stroke-linecap="round"/>
    <path d="M150,42 Q170,20 180,30 Q190,40 185,50" fill="none" stroke="#00695C" stroke-width="2" stroke-linecap="round"/>
    <!-- Mouth -->
    <ellipse cx="130" cy="48" rx="12" ry="4" fill="#E0F7FA" stroke="#00695C" stroke-width="1"/>
    <!-- Bud -->
    <path d="M165,130 Q185,120 190,135 Q195,150 175,145 Q160,142 165,130 Z" fill="#80CBC4" stroke="#00695C" stroke-width="1.2"/>
    <text x="205" y="135" font-family="Arial,sans-serif" font-size="7" fill="#00695C">почка</text>
    <!-- Basal disc -->
    <ellipse cx="130" cy="250" rx="18" ry="6" fill="#80CBC4" stroke="#00695C" stroke-width="1.5"/>
    <text x="130" y="268" font-family="Arial,sans-serif" font-size="7" fill="#00695C" text-anchor="middle">подошва</text>

    <!-- Internal structure labels -->
    <text x="30" y="60" font-family="Arial,sans-serif" font-size="7" fill="#00695C">щупальца</text>
    <text x="170" y="48" font-family="Arial,sans-serif" font-size="7" fill="#00695C">рот</text>
    <text x="30" y="100" font-family="Arial,sans-serif" font-size="7" fill="#00695C">кишечная</text>
    <text x="30" y="110" font-family="Arial,sans-serif" font-size="7" fill="#00695C">полость</text>
  </g>

  <!-- Jellyfish -->
  <g transform="translate(310,75)">
    <rect x="0" y="0" width="275" height="145" rx="8" fill="white" stroke="#00695C" stroke-width="1.5"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#00695C" opacity="0.85"/>
    <rect x="0" y="14" width="275" height="10" fill="#00695C" opacity="0.85"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">МЕДУЗА</text>

    <!-- Bell -->
    <path d="M60,80 Q60,35 138,30 Q216,35 216,80 Z" fill="#B2EBF2" stroke="#00695C" stroke-width="2"/>
    <path d="M70,80 Q70,50 138,45 Q206,50 206,80 Z" fill="#E0F7FA" stroke="none"/>
    <!-- Tentacles -->
    <path d="M75,80 Q70,110 65,130" fill="none" stroke="#00695C" stroke-width="1" stroke-linecap="round"/>
    <path d="M95,80 Q90,115 88,135" fill="none" stroke="#00695C" stroke-width="1.2" stroke-linecap="round"/>
    <path d="M120,80 Q118,120 115,140" fill="none" stroke="#00695C" stroke-width="1.5" stroke-linecap="round"/>
    <path d="M155,80 Q158,120 160,140" fill="none" stroke="#00695C" stroke-width="1.5" stroke-linecap="round"/>
    <path d="M180,80 Q185,115 188,135" fill="none" stroke="#00695C" stroke-width="1.2" stroke-linecap="round"/>
    <path d="M200,80 Q205,110 210,130" fill="none" stroke="#00695C" stroke-width="1" stroke-linecap="round"/>
    <!-- Oral arms -->
    <path d="M130,80 Q125,105 128,125" fill="none" stroke="#00897B" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M146,80 Q150,105 148,125" fill="none" stroke="#00897B" stroke-width="2.5" stroke-linecap="round"/>
    <!-- Radial canals -->
    <line x1="138" y1="55" x2="80" y2="75" stroke="#4DB6AC" stroke-width="0.8"/>
    <line x1="138" y1="55" x2="196" y2="75" stroke="#4DB6AC" stroke-width="0.8"/>
    <line x1="138" y1="55" x2="138" y2="80" stroke="#4DB6AC" stroke-width="0.8"/>
  </g>

  <!-- Coral polyp -->
  <g transform="translate(310,230)">
    <rect x="0" y="0" width="275" height="120" rx="8" fill="white" stroke="#00695C" stroke-width="1.5"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#00695C" opacity="0.85"/>
    <rect x="0" y="14" width="275" height="10" fill="#00695C" opacity="0.85"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">КОРАЛЛОВЫЙ ПОЛИП</text>

    <!-- Coral skeleton -->
    <rect x="50" y="70" width="180" height="40" rx="3" fill="#FFCCBC" stroke="#BF360C" stroke-width="1"/>
    <rect x="60" y="60" width="20" height="15" rx="2" fill="#FFAB91" stroke="#BF360C" stroke-width="0.8"/>
    <rect x="90" y="55" width="20" height="20" rx="2" fill="#FFAB91" stroke="#BF360C" stroke-width="0.8"/>
    <rect x="120" y="60" width="20" height="15" rx="2" fill="#FFAB91" stroke="#BF360C" stroke-width="0.8"/>
    <rect x="150" y="55" width="20" height="20" rx="2" fill="#FFAB91" stroke="#BF360C" stroke-width="0.8"/>
    <rect x="180" y="60" width="20" height="15" rx="2" fill="#FFAB91" stroke="#BF360C" stroke-width="0.8"/>

    <!-- Polyp on top -->
    <path d="M95,55 Q90,35 95,28 Q100,22 105,28 Q110,35 105,55" fill="#B2EBF2" stroke="#00695C" stroke-width="1.2"/>
    <path d="M95,30 Q85,22 82,28 Q80,34 88,32" fill="none" stroke="#00695C" stroke-width="1"/>
    <path d="M105,30 Q115,22 118,28 Q120,34 112,32" fill="none" stroke="#00695C" stroke-width="1"/>

    <path d="M155,55 Q150,35 155,28 Q160,22 165,28 Q170,35 165,55" fill="#B2EBF2" stroke="#00695C" stroke-width="1.2"/>
    <path d="M155,30 Q145,22 142,28 Q140,34 148,32" fill="none" stroke="#00695C" stroke-width="1"/>
    <path d="M165,30 Q175,22 178,28 Q180,34 172,32" fill="none" stroke="#00695C" stroke-width="1"/>

    <text x="138" y="95" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle">Известковый скелет</text>
    <text x="138" y="105" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Колония полипов образует риф</text>
  </g>
''' + svg_footer("Кишечнополостные", "#00695C"))

# ===== LESSON 15: Черви =====
write_svg(15, svg_header("Черви", "Биология 5 класс - Урок 15", "#FBE9E7", "#FFCCBC", "#BF360C") + '''
  <!-- Planaria (flatworm) -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="185" height="165" rx="8" fill="white" stroke="#BF360C" stroke-width="1.5"/>
    <rect x="0" y="0" width="185" height="22" rx="8" fill="#BF360C" opacity="0.85"/>
    <rect x="0" y="14" width="185" height="10" fill="#BF360C" opacity="0.85"/>
    <text x="93" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ПЛАНАРИЯ (плоский)</text>
    <!-- Body shape -->
    <path d="M55,80 Q40,65 35,75 Q30,85 40,95 Q55,110 93,115 Q131,110 146,95 Q156,85 151,75 Q146,65 131,80 Z" fill="#FFCCBC" stroke="#BF360C" stroke-width="1.5"/>
    <!-- Head with auricles -->
    <path d="M40,75 Q30,60 25,65" fill="none" stroke="#BF360C" stroke-width="1.5"/>
    <path d="M40,85 Q30,100 25,95" fill="none" stroke="#BF360C" stroke-width="1.5"/>
    <!-- Eyes -->
    <circle cx="55" cy="78" r="3" fill="#37474F" stroke="#263238" stroke-width="0.8"/>
    <circle cx="55" cy="82" r="3" fill="#37474F" stroke="#263238" stroke-width="0.8"/>
    <!-- Pharynx -->
    <ellipse cx="93" cy="88" rx="8" ry="10" fill="#FFAB91" stroke="#BF360C" stroke-width="0.8"/>
    <!-- Gut branches -->
    <line x1="93" y1="78" x2="60" y2="72" stroke="#E65100" stroke-width="0.8"/>
    <line x1="93" y1="78" x2="126" y2="72" stroke="#E65100" stroke-width="0.8"/>
    <line x1="93" y1="98" x2="60" y2="105" stroke="#E65100" stroke-width="0.8"/>
    <line x1="93" y1="98" x2="126" y2="105" stroke="#E65100" stroke-width="0.8"/>
    <text x="93" y="135" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Свободноживущий</text>
    <text x="93" y="148" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Двусторонняя симметрия</text>
  </g>

  <!-- Roundworm -->
  <g transform="translate(210,75)">
    <rect x="0" y="0" width="185" height="165" rx="8" fill="white" stroke="#BF360C" stroke-width="1.5"/>
    <rect x="0" y="0" width="185" height="22" rx="8" fill="#BF360C" opacity="0.85"/>
    <rect x="0" y="14" width="185" height="10" fill="#BF360C" opacity="0.85"/>
    <text x="93" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">АСКАРИДА (круглый)</text>
    <!-- Worm body -->
    <path d="M30,80 Q50,55 93,50 Q136,55 156,80 Q136,105 93,110 Q50,105 30,80 Z" fill="#FFF3E0" stroke="#E65100" stroke-width="1.5"/>
    <!-- Tapered ends -->
    <path d="M30,80 Q20,80 15,80" fill="none" stroke="#E65100" stroke-width="2"/>
    <path d="M156,80 Q165,80 170,80" fill="none" stroke="#E65100" stroke-width="2"/>
    <!-- Mouth -->
    <ellipse cx="20" cy="80" rx="3" ry="5" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
    <!-- Gut -->
    <line x1="25" y1="80" x2="150" y2="80" stroke="#E65100" stroke-width="1.5"/>
    <!-- Cuticle ring lines -->
    <line x1="50" y1="62" x2="50" y2="98" stroke="#FFE0B2" stroke-width="0.5"/>
    <line x1="70" y1="56" x2="70" y2="104" stroke="#FFE0B2" stroke-width="0.5"/>
    <line x1="93" y1="53" x2="93" y2="107" stroke="#FFE0B2" stroke-width="0.5"/>
    <line x1="116" y1="56" x2="116" y2="104" stroke="#FFE0B2" stroke-width="0.5"/>
    <line x1="136" y1="62" x2="136" y2="98" stroke="#FFE0B2" stroke-width="0.5"/>
    <text x="93" y="132" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Паразит</text>
    <text x="93" y="145" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Первичная полость тела</text>
    <text x="93" y="158" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle">Кутикула вместо стенки</text>
  </g>

  <!-- Earthworm -->
  <g transform="translate(405,75)">
    <rect x="0" y="0" width="185" height="165" rx="8" fill="white" stroke="#BF360C" stroke-width="1.5"/>
    <rect x="0" y="0" width="185" height="22" rx="8" fill="#BF360C" opacity="0.85"/>
    <rect x="0" y="14" width="185" height="10" fill="#BF360C" opacity="0.85"/>
    <text x="93" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ДОЖД. ЧЕРВЬ (кольчат.)</text>
    <!-- Segmented body -->
    <ellipse cx="93" cy="80" rx="65" ry="16" fill="#FFCCBC" stroke="#BF360C" stroke-width="1.5"/>
    <!-- Segments -->
    <line x1="45" y1="65" x2="45" y2="95" stroke="#BF360C" stroke-width="0.5" opacity="0.5"/>
    <line x1="55" y1="64" x2="55" y2="96" stroke="#BF360C" stroke-width="0.5" opacity="0.5"/>
    <line x1="65" y1="64" x2="65" y2="96" stroke="#BF360C" stroke-width="0.5" opacity="0.5"/>
    <line x1="75" y1="64" x2="75" y2="96" stroke="#BF360C" stroke-width="0.5" opacity="0.5"/>
    <line x1="85" y1="64" x2="85" y2="96" stroke="#BF360C" stroke-width="0.5" opacity="0.5"/>
    <line x1="101" y1="64" x2="101" y2="96" stroke="#BF360C" stroke-width="0.5" opacity="0.5"/>
    <line x1="111" y1="64" x2="111" y2="96" stroke="#BF360C" stroke-width="0.5" opacity="0.5"/>
    <line x1="121" y1="64" x2="121" y2="96" stroke="#BF360C" stroke-width="0.5" opacity="0.5"/>
    <line x1="131" y1="65" x2="131" y2="95" stroke="#BF360C" stroke-width="0.5" opacity="0.5"/>
    <line x1="141" y1="65" x2="141" y2="95" stroke="#BF360C" stroke-width="0.5" opacity="0.5"/>
    <!-- Clitellum (saddle) -->
    <rect x="85" y="65" width="18" height="30" rx="5" fill="#FFAB91" stroke="#BF360C" stroke-width="1"/>
    <text x="94" y="82" font-family="Arial,sans-serif" font-size="5" fill="#BF360C" text-anchor="middle">поясок</text>
    <!-- Setæ (bristles) -->
    <line x1="55" y1="96" x2="52" y2="102" stroke="#8D6E63" stroke-width="0.8"/>
    <line x1="65" y1="96" x2="62" y2="102" stroke="#8D6E63" stroke-width="0.8"/>
    <line x1="121" y1="96" x2="118" y2="102" stroke="#8D6E63" stroke-width="0.8"/>
    <line x1="131" y1="96" x2="128" y2="102" stroke="#8D6E63" stroke-width="0.8"/>
    <text x="93" y="120" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Свободноживущий</text>
    <text x="93" y="132" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Вторичная полость</text>
    <text x="93" y="145" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Кольца (сегменты)</text>
    <text x="93" y="158" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle">Щетинки для движения</text>
  </g>

  <!-- Comparison table -->
  <g transform="translate(15,255)">
    <rect x="0" y="0" width="570" height="95" rx="8" fill="white" stroke="#BF360C" stroke-width="1.5"/>
    <text x="285" y="18" font-family="Arial,sans-serif" font-size="10" fill="#BF360C" text-anchor="middle" font-weight="bold">СРАВНЕНИЕ ТРЁХ ТИПОВ ЧЕРВЕЙ</text>
    <line x1="10" y1="25" x2="560" y2="25" stroke="#FFCCBC" stroke-width="1"/>
    <text x="70" y="40" font-family="Arial,sans-serif" font-size="8" fill="#BF360C" font-weight="bold">Признак</text>
    <text x="200" y="40" font-family="Arial,sans-serif" font-size="8" fill="#BF360C" font-weight="bold">Плоские</text>
    <text x="330" y="40" font-family="Arial,sans-serif" font-size="8" fill="#BF360C" font-weight="bold">Круглые</text>
    <text x="480" y="40" font-family="Arial,sans-serif" font-size="8" fill="#BF360C" font-weight="bold">Кольчатые</text>
    <line x1="10" y1="45" x2="560" y2="45" stroke="#FFCCBC" stroke-width="0.5"/>
    <text x="70" y="58" font-family="Arial,sans-serif" font-size="7" fill="#555">Полость тела</text>
    <text x="200" y="58" font-family="Arial,sans-serif" font-size="7" fill="#555">Нет</text>
    <text x="330" y="58" font-family="Arial,sans-serif" font-size="7" fill="#555">Первичная</text>
    <text x="480" y="58" font-family="Arial,sans-serif" font-size="7" fill="#555">Вторичная</text>
    <text x="70" y="72" font-family="Arial,sans-serif" font-size="7" fill="#555">Сегментация</text>
    <text x="200" y="72" font-family="Arial,sans-serif" font-size="7" fill="#555">Нет</text>
    <text x="330" y="72" font-family="Arial,sans-serif" font-size="7" fill="#555">Нет</text>
    <text x="480" y="72" font-family="Arial,sans-serif" font-size="7" fill="#555">Да</text>
    <text x="70" y="86" font-family="Arial,sans-serif" font-size="7" fill="#555">Образ жизни</text>
    <text x="200" y="86" font-family="Arial,sans-serif" font-size="7" fill="#555">Паразиты и своб.</text>
    <text x="330" y="86" font-family="Arial,sans-serif" font-size="7" fill="#555">Паразиты</text>
    <text x="480" y="86" font-family="Arial,sans-serif" font-size="7" fill="#555">Свободноживущие</text>
  </g>
''' + svg_footer("Черви", "#BF360C"))

# ===== LESSON 16: Моллюски =====
write_svg(16, svg_header("Моллюски", "Биология 5 класс - Урок 16", "#F3E5F5", "#E1BEE7", "#6A1B9A") + '''
  <!-- Gastropod (snail) -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="185" height="165" rx="8" fill="white" stroke="#6A1B9A" stroke-width="1.5"/>
    <rect x="0" y="0" width="185" height="22" rx="8" fill="#6A1B9A" opacity="0.85"/>
    <rect x="0" y="14" width="185" height="10" fill="#6A1B9A" opacity="0.85"/>
    <text x="93" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">БРЮХОНОГИЙ</text>
    <!-- Shell (spiral) -->
    <path d="M80,50 Q100,30 120,40 Q140,50 135,70 Q130,85 115,90 Q100,95 90,85 Q80,75 85,60 Q90,50 100,50" fill="none" stroke="#8D6E63" stroke-width="3"/>
    <path d="M80,50 Q100,30 120,40 Q140,50 135,70 Q130,85 115,90 Q100,95 90,85 Q80,75 85,60 Q90,50 100,50 Z" fill="#D7CCC8" stroke="#8D6E63" stroke-width="1.5"/>
    <!-- Spiral lines on shell -->
    <path d="M95,55 Q105,50 115,55 Q120,65 112,72" fill="none" stroke="#A1887F" stroke-width="0.8"/>
    <!-- Body/foot -->
    <path d="M90,90 Q70,100 55,105 Q45,110 50,115 Q60,118 80,110 Q95,105 105,95" fill="#F3E5F5" stroke="#6A1B9A" stroke-width="1.2"/>
    <!-- Head with tentacles -->
    <path d="M55,105 Q45,95 40,85" fill="none" stroke="#6A1B9A" stroke-width="1.5"/>
    <circle cx="38" cy="83" r="2" fill="#37474F"/>
    <path d="M55,105 Q50,95 48,85" fill="none" stroke="#6A1B9A" stroke-width="1.5"/>
    <circle cx="46" cy="83" r="2" fill="#37474F"/>
    <text x="93" y="135" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Раковина спиральная</text>
    <text x="93" y="148" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Нога на брюшке</text>
  </g>

  <!-- Bivalve -->
  <g transform="translate(210,75)">
    <rect x="0" y="0" width="185" height="165" rx="8" fill="white" stroke="#6A1B9A" stroke-width="1.5"/>
    <rect x="0" y="0" width="185" height="22" rx="8" fill="#6A1B9A" opacity="0.85"/>
    <rect x="0" y="14" width="185" height="10" fill="#6A1B9A" opacity="0.85"/>
    <text x="93" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ДВУСТВОРЧАТЫЙ</text>
    <!-- Left valve -->
    <path d="M60,45 Q30,60 25,85 Q25,110 45,125 Q65,135 90,130 Q90,80 60,45 Z" fill="#FFECB3" stroke="#F9A825" stroke-width="1.5"/>
    <!-- Right valve (slightly open) -->
    <path d="M60,45 Q90,35 120,45 Q140,60 145,85 Q145,110 125,125 Q105,135 90,130 Q90,80 60,45 Z" fill="#FFF8E1" stroke="#F9A825" stroke-width="1.5"/>
    <!-- Ridges on shell -->
    <line x1="50" y1="65" x2="50" y2="120" stroke="#FFE082" stroke-width="0.5"/>
    <line x1="65" y1="55" x2="65" y2="128" stroke="#FFE082" stroke-width="0.5"/>
    <line x1="80" y1="50" x2="80" y2="132" stroke="#FFE082" stroke-width="0.5"/>
    <!-- Hinge -->
    <ellipse cx="60" cy="45" rx="5" ry="3" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
    <!-- Foot showing -->
    <path d="M90,130 Q95,140 105,138 Q115,135 108,128" fill="#F3E5F5" stroke="#6A1B9A" stroke-width="1"/>
    <!-- Siphons -->
    <path d="M120,50 Q125,40 130,42" fill="none" stroke="#6A1B9A" stroke-width="1.5"/>
    <path d="M125,55 Q130,45 135,47" fill="none" stroke="#6A1B9A" stroke-width="1.5"/>
    <text x="93" y="148" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Две створки, сифоны</text>
  </g>

  <!-- Cephalopod -->
  <g transform="translate(405,75)">
    <rect x="0" y="0" width="185" height="165" rx="8" fill="white" stroke="#6A1B9A" stroke-width="1.5"/>
    <rect x="0" y="0" width="185" height="22" rx="8" fill="#6A1B9A" opacity="0.85"/>
    <rect x="0" y="14" width="185" height="10" fill="#6A1B9A" opacity="0.85"/>
    <text x="93" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ГОЛОВОНОГИЙ</text>
    <!-- Octopus body -->
    <ellipse cx="93" cy="60" rx="30" ry="25" fill="#E1BEE7" stroke="#6A1B9A" stroke-width="1.5"/>
    <!-- Eyes -->
    <circle cx="78" cy="55" r="6" fill="white" stroke="#37474F" stroke-width="1"/>
    <circle cx="78" cy="55" r="3" fill="#37474F"/>
    <circle cx="108" cy="55" r="6" fill="white" stroke="#37474F" stroke-width="1"/>
    <circle cx="108" cy="55" r="3" fill="#37474F"/>
    <!-- Tentacles -->
    <path d="M70,80 Q55,100 45,120 Q40,130 50,128" fill="none" stroke="#6A1B9A" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M78,82 Q68,105 60,125 Q55,135 65,132" fill="none" stroke="#6A1B9A" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M85,83 Q82,108 78,130 Q76,140 85,135" fill="none" stroke="#6A1B9A" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M93,84 Q93,110 93,132 Q93,142 100,136" fill="none" stroke="#6A1B9A" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M101,83 Q104,108 108,130 Q110,140 115,132" fill="none" stroke="#6A1B9A" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M108,82 Q118,105 126,125 Q130,135 132,128" fill="none" stroke="#6A1B9A" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M115,80 Q130,100 140,120 Q145,130 148,122" fill="none" stroke="#6A1B9A" stroke-width="2.5" stroke-linecap="round"/>
    <!-- Suction cups -->
    <circle cx="52" cy="118" r="2" fill="#CE93D8"/>
    <circle cx="64" cy="122" r="2" fill="#CE93D8"/>
    <circle cx="82" cy="128" r="2" fill="#CE93D8"/>
    <circle cx="104" cy="130" r="2" fill="#CE93D8"/>
    <circle cx="122" cy="122" r="2" fill="#CE93D8"/>
    <text x="93" y="148" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">8 щупалец с присосками</text>
  </g>

  <!-- Mollusk body plan -->
  <g transform="translate(15,255)">
    <rect x="0" y="0" width="570" height="95" rx="8" fill="white" stroke="#6A1B9A" stroke-width="1.5"/>
    <text x="285" y="18" font-family="Arial,sans-serif" font-size="10" fill="#6A1B9A" text-anchor="middle" font-weight="bold">ОБЩИЕ ПРИЗНАКИ МОЛЛЮСКОВ</text>
    <line x1="10" y1="25" x2="560" y2="25" stroke="#E1BEE7" stroke-width="1"/>

    <!-- Mantle -->
    <rect x="15" y="35" width="130" height="50" rx="5" fill="#F3E5F5" stroke="#6A1B9A" stroke-width="1"/>
    <text x="80" y="55" font-family="Arial,sans-serif" font-size="9" fill="#6A1B9A" text-anchor="middle" font-weight="bold">Мантия</text>
    <text x="80" y="70" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Складка кожи, образует раковину</text>

    <!-- Foot -->
    <rect x="155" y="35" width="130" height="50" rx="5" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
    <text x="220" y="55" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Нога</text>
    <text x="220" y="70" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Мышечный орган движения</text>

    <!-- Shell -->
    <rect x="295" y="35" width="130" height="50" rx="5" fill="#FFF8E1" stroke="#F9A825" stroke-width="1"/>
    <text x="360" y="55" font-family="Arial,sans-serif" font-size="9" fill="#F9A825" text-anchor="middle" font-weight="bold">Раковина</text>
    <text x="360" y="70" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Защита (у некоторых нет)</text>

    <!-- Radula -->
    <rect x="435" y="35" width="130" height="50" rx="5" fill="#FFEBEE" stroke="#C62828" stroke-width="1"/>
    <text x="500" y="55" font-family="Arial,sans-serif" font-size="9" fill="#C62828" text-anchor="middle" font-weight="bold">Тёрка (радула)</text>
    <text x="500" y="70" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Орган питания</text>
  </g>
''' + svg_footer("Моллюски", "#6A1B9A"))

# ===== LESSON 17: Красная книга =====
write_svg(17, svg_header("Красная книга", "Биология 5 класс - Урок 17", "#FFEBEE", "#FFCDD2", "#C62828") + '''
  <!-- Red Book -->
  <g transform="translate(30,75)">
    <!-- Book shape -->
    <rect x="0" y="0" width="160" height="210" rx="5" fill="#C62828" stroke="#880E4F" stroke-width="2"/>
    <rect x="5" y="5" width="150" height="200" rx="3" fill="#D32F2F"/>
    <!-- Title on book -->
    <text x="80" y="40" font-family="Arial,sans-serif" font-size="12" fill="#FFCDD2" text-anchor="middle" font-weight="bold">КРАСНАЯ</text>
    <text x="80" y="58" font-family="Arial,sans-serif" font-size="12" fill="#FFCDD2" text-anchor="middle" font-weight="bold">КНИГА</text>
    <!-- Decorative line -->
    <line x1="30" y1="68" x2="130" y2="68" stroke="#FFCDD2" stroke-width="1"/>
    <!-- Silhouette of animal -->
    <ellipse cx="80" cy="120" rx="35" ry="25" fill="#B71C1C" opacity="0.6"/>
    <ellipse cx="80" cy="115" rx="20" ry="15" fill="#C62828"/>
    <!-- Simple deer-like silhouette -->
    <path d="M55,110 Q50,95 55,85 Q60,80 65,85 L65,95 Q70,90 75,95 L75,110 Z" fill="#D32F2F" stroke="#FFCDD2" stroke-width="0.5"/>
    <path d="M85,110 Q90,95 95,85 Q100,80 105,85 L105,95 Q100,90 95,95 L95,110 Z" fill="#D32F2F" stroke="#FFCDD2" stroke-width="0.5"/>
    <!-- Star -->
    <polygon points="80,75 83,82 90,82 84,87 86,94 80,90 74,94 76,87 70,82 77,82" fill="#FFCDD2"/>
    <!-- Bottom text -->
    <line x1="30" y1="165" x2="130" y2="165" stroke="#FFCDD2" stroke-width="1"/>
    <text x="80" y="185" font-family="Arial,sans-serif" font-size="7" fill="#FFCDD2" text-anchor="middle">Российская Федерация</text>
    <text x="80" y="198" font-family="Arial,sans-serif" font-size="7" fill="#FFCDD2" text-anchor="middle">Охрана редких видов</text>
  </g>

  <!-- Categories -->
  <g transform="translate(210,75)">
    <rect x="0" y="0" width="375" height="210" rx="8" fill="white" stroke="#C62828" stroke-width="1.5"/>
    <rect x="0" y="0" width="375" height="24" rx="8" fill="#C62828" opacity="0.85"/>
    <rect x="0" y="16" width="375" height="10" fill="#C62828" opacity="0.85"/>
    <text x="188" y="17" font-family="Arial,sans-serif" font-size="11" fill="white" text-anchor="middle" font-weight="bold">КАТЕГОРИИ КРАСНОЙ КНИГИ</text>

    <!-- Category 0 - Probably extinct -->
    <rect x="10" y="32" width="355" height="32" rx="4" fill="#37474F" opacity="0.1"/>
    <rect x="10" y="32" width="6" height="32" rx="2" fill="#37474F"/>
    <text x="25" y="44" font-family="Arial,sans-serif" font-size="8" fill="#37474F" font-weight="bold">0 - Вероятно исчезнувшие</text>
    <text x="25" y="56" font-family="Arial,sans-serif" font-size="7" fill="#555">Не обнаружены в природе, но возможно сохранились</text>

    <!-- Category 1 - Endangered -->
    <rect x="10" y="68" width="355" height="32" rx="4" fill="#C62828" opacity="0.1"/>
    <rect x="10" y="68" width="6" height="32" rx="2" fill="#C62828"/>
    <text x="25" y="80" font-family="Arial,sans-serif" font-size="8" fill="#C62828" font-weight="bold">1 - Исчезающие (на грани вымирания)</text>
    <text x="25" y="92" font-family="Arial,sans-serif" font-size="7" fill="#555">Спасение невозможно без спец. мер</text>

    <!-- Category 2 - Declining -->
    < x="10" y="104" width="355" height="32" rx="4" fill="#E65100" opacity="0.1"/>
    <rect x="10" y="104" width="6" height="32" rx="2" fill="#E65100"/>
    <text x="25" y="116" font-family="Arial,sans-serif" font-size="8" fill="#E65100" font-weight="bold">2 - Сокращающиеся в численности</text>
    <text x="25" y="128" font-family="Arial,sans-serif" font-size="7" fill="#555">Численность снижается, ареал сокращается</text>

    <!-- Category 3 - Rare -->
    <rect x="10" y="140" width="355" height="32" rx="4" fill="#F9A825" opacity="0.1"/>
    <rect x="10" y="140" width="6" height="32" rx="2" fill="#F9A825"/>
    <text x="25" y="152" font-family="Arial,sans-serif" font-size="8" fill="#F57F17" font-weight="bold">3 - Редкие</text>
    <text x="25" y="164" font-family="Arial,sans-serif" font-size="7" fill="#555">Малая численность, ограниченный ареал</text>

    <!-- Category 4 - Indeterminate -->
    <rect x="10" y="176" width="355" height="28" rx="4" fill="#1565C0" opacity="0.1"/>
    <rect x="10" y="176" width="6" height="28" rx="2" fill="#1565C0"/>
    <text x="25" y="188" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" font-weight="bold">4 - Неопределённые (мало данных)</text>
    <text x="25" y="198" font-family="Arial,sans-serif" font-size="7" fill="#555">Статус недостаточно изучен</text>
  </g>

  <!-- Example species -->
  <g transform="translate(15,300)">
    <rect x="0" y="0" width="570" height="50" rx="8" fill="white" stroke="#C62828" stroke-width="1" opacity="0.9"/>
    <text x="285" y="15" font-family="Arial,sans-serif" font-size="9" fill="#C62828" text-anchor="middle" font-weight="bold">Примеры видов Красной книги России</text>
    <text x="285" y="32" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Амурский тигер | Зубр | Снежный барс | Белый медведь | Стерх | Лотос | Женьшень</text>
    <text x="285" y="44" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">Всего в Красной книге РФ: более 500 видов животных и растений</text>
  </g>
''' + svg_footer("Красная книга", "#C62828"))

# ===== LESSON 18: Заповедники и национальные парки =====
write_svg(18, svg_header("Заповедники и нац. парки", "Биология 5 класс - Урок 18", "#E8F5E9", "#C8E6C9", "#1B5E20") + '''
  <!-- Nature scene -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="570" height="200" rx="8" fill="white" stroke="#1B5E20" stroke-width="1.5"/>
    <!-- Sky -->
    <rect x="0" y="0" width="570" height="120" rx="8" fill="#E3F2FD"/>
    <rect x="0" y="112" width="570" height="8" fill="#E3F2FD"/>
    <!-- Mountains -->
    <path d="M0,120 L80,50 L140,100 L200,40 L260,90 L320,55 L380,110 L430,45 L480,95 L540,60 L570,80 L570,120 Z" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
    <!-- Snow caps -->
    <path d="M75,55 L80,50 L85,55 Z" fill="white"/>
    <path d="M195,45 L200,40 L205,45 Z" fill="white"/>
    <path d="M315,60 L320,55 L325,60 Z" fill="white"/>
    <path d="M425,50 L430,45 L435,50 Z" fill="white"/>
    <!-- Trees -->
    <rect x="50" y="105" width="4" height="15" fill="#5D4037"/>
    <path d="M35,105 L52,75 L69,105 Z" fill="#2E7D32"/>
    <rect x="490" y="100" width="5" height="20" fill="#5D4037"/>
    <path d="M472,100 L492,65 L512,100 Z" fill="#388E3C"/>
    <rect x="530" y="105" width="4" height="15" fill="#5D4037"/>
    <path d="M515,105 L532,78 L549,105 Z" fill="#2E7D32"/>
    <!-- Lake -->
    <ellipse cx="285" cy="145" rx="80" ry="20" fill="#90CAF9" stroke="#42A5F5" stroke-width="1"/>
    <!-- Ground -->
    <rect x="0" y="120" width="570" height="80" fill="#A5D6A7" rx="0"/>
    <!-- Deer -->
    <ellipse cx="160" cy="140" rx="15" ry="10" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
    <ellipse cx="148" cy="132" rx="6" ry="5" fill="#A1887F" stroke="#5D4037" stroke-width="0.8"/>
    <line x1="150" y1="128" x2="146" y2="118" stroke="#5D4037" stroke-width="1"/>
    <line x1="146" y1="118" x2="143" y2="112" stroke="#5D4037" stroke-width="0.8"/>
    <line x1="146" y1="118" x2="149" y2="112" stroke="#5D4037" stroke-width="0.8"/>
    <line x1="172" y1="148" x2="172" y2="155" stroke="#5D4037" stroke-width="1"/>
    <line x1="166" y1="148" x2="166" y2="155" stroke="#5D4037" stroke-width="1"/>
    <!-- Bird -->
    <path d="M380,70 Q385,65 390,70 Q395,65 400,70" fill="none" stroke="#37474F" stroke-width="1.5"/>
    <!-- Flowers -->
    <circle cx="100" cy="135" r="3" fill="#F48FB1"/>
    <circle cx="420" cy="140" r="3" fill="#FDD835"/>
    <circle cx="450" cy="135" r="3" fill="#F48FB1"/>
    <!-- Sign -->
    <rect x="240" y="160" width="90" height="30" rx="3" fill="#1B5E20" opacity="0.85"/>
    <text x="285" y="180" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ЗАПОВЕДНИК</text>
  </g>

  <!-- Types of protected areas -->
  <g transform="translate(15,290)">
    <rect x="0" y="0" width="185" height="65" rx="8" fill="white" stroke="#1B5E20" stroke-width="1.5"/>
    <rect x="0" y="0" width="185" height="20" rx="8" fill="#1B5E20" opacity="0.85"/>
    <rect x="0" y="14" width="185" height="8" fill="#1B5E20" opacity="0.85"/>
    <text x="93" y="15" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ЗАПОВЕДНИК</text>
    <text x="93" y="38" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Полный запрет хозяйственной</text>
    <text x="93" y="50" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">деятельности. Научные исследования</text>
    <text x="93" y="60" font-family="Arial,sans-serif" font-size="7" fill="#1B5E20" text-anchor="middle">Строгая охрана</text>
  </g>

  <g transform="translate(210,290)">
    <rect x="0" y="0" width="185" height="65" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
    <rect x="0" y="0" width="185" height="20" rx="8" fill="#2E7D32" opacity="0.85"/>
    <rect x="0" y="14" width="185" height="8" fill="#2E7D32" opacity="0.85"/>
    <text x="93" y="15" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">НАЦ. ПАРК</text>
    <text x="93" y="38" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Охрана природы + отдых людей.</text>
    <text x="93" y="50" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Зонирование территории</text>
    <text x="93" y="60" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Туризм разрешён</text>
  </g>

  <g transform="translate(405,290)">
    <rect x="0" y="0" width="185" height="65" rx="8" fill="white" stroke="#43A047" stroke-width="1.5"/>
    <rect x="0" y="0" width="185" height="20" rx="8" fill="#43A047" opacity="0.85"/>
    <rect x="0" y="14" width="185" height="8" fill="#43A047" opacity="0.85"/>
    <text x="93" y="15" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ЗАКАЗНИК</text>
    <text x="93" y="38" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Частичная охрана. Запрет на</text>
    <text x="93" y="50" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">отдельные виды деятельности</text>
    <text x="93" y="60" font-family="Arial,sans-serif" font-size="7" fill="#43A047" text-anchor="middle">Временная или постоянная</text>
  </g>

  <!-- Famous reserves -->
  <g transform="translate(15,362)">
    <rect x="0" y="0" width="570" height="28" rx="5" fill="#1B5E20" opacity="0.85"/>
    <text x="285" y="18" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Известные: Приокско-Террасный | Байкальский | Кроноцкий | Остров Врангеля | Кавказский</text>
  </g>
''' + svg_footer("Заповедники и национальные парки", "#1B5E20"))

print("Grade 5 lessons 10-18 generated!")
