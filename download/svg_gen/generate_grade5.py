#!/usr/bin/env python3
"""Generate detailed biology SVG illustrations for Grade 5."""
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

# ===== LESSON 1: Что такое клетка =====
write_svg(1, svg_header("Что такое клетка", "Биология 5 класс - Урок 1") + '''
  <!-- Microscope illustration -->
  <g transform="translate(80,80)">
    <!-- Microscope body -->
    <rect x="30" y="10" width="25" height="120" rx="3" fill="#546E7A" stroke="#37474F" stroke-width="1.5"/>
    <rect x="20" y="130" width="45" height="8" rx="2" fill="#455A64" stroke="#37474F" stroke-width="1"/>
    <rect x="10" y="138" width="60" height="6" rx="2" fill="#37474F"/>
    <!-- Eyepiece -->
    <rect x="32" y="-5" width="21" height="18" rx="4" fill="#78909C" stroke="#37474F" stroke-width="1"/>
    <!-- Objective -->
    <rect x="35" y="95" width="15" height="20" rx="2" fill="#78909C" stroke="#37474F" stroke-width="1"/>
    <!-- Stage -->
    <rect x="5" y="85" width="70" height="5" rx="1" fill="#607D8B"/>
    <!-- Slide on stage -->
    <rect x="15" y="82" width="30" height="4" rx="1" fill="#E3F2FD" stroke="#90CAF9" stroke-width="0.5"/>
    <!-- Arm -->
    <rect x="55" y="40" width="8" height="100" rx="2" fill="#546E7A" stroke="#37474F" stroke-width="1"/>
    <!-- Focus knob -->
    <circle cx="63" cy="80" r="8" fill="#607D8B" stroke="#37474F" stroke-width="1"/>
    <circle cx="63" cy="80" r="3" fill="#455A64"/>
    <!-- Base -->
    <ellipse cx="40" cy="148" rx="38" ry="6" fill="#455A64" stroke="#37474F" stroke-width="1"/>
  </g>

  <!-- Cell view through microscope -->
  <g transform="translate(220,80)">
    <circle cx="90" cy="100" r="90" fill="#F1F8E9" stroke="#66BB6A" stroke-width="2.5"/>
    <circle cx="90" cy="100" r="87" fill="none" stroke="#A5D6A7" stroke-width="1" stroke-dasharray="3,3"/>
    <text x="90" y="25" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle" font-weight="bold">Вид под микроскопом</text>

    <!-- Cell 1 -->
    <ellipse cx="65" cy="80" rx="30" ry="22" fill="#C8E6C9" stroke="#388E3C" stroke-width="1.5"/>
    <ellipse cx="65" cy="78" rx="10" ry="8" fill="#81C784" stroke="#1B5E20" stroke-width="1"/>
    <text x="65" y="82" font-family="Arial,sans-serif" font-size="6" fill="#1B5E20" text-anchor="middle">ядро</text>
    <circle cx="50" cy="72" r="4" fill="#A5D6A7" stroke="#2E7D32" stroke-width="0.5"/>
    <circle cx="78" cy="88" r="3.5" fill="#A5D6A7" stroke="#2E7D32" stroke-width="0.5"/>

    <!-- Cell 2 -->
    <ellipse cx="120" cy="90" rx="28" ry="20" fill="#DCEDC8" stroke="#558B2F" stroke-width="1.5"/>
    <ellipse cx="122" cy="88" rx="9" ry="7" fill="#9CCC65" stroke="#33691E" stroke-width="1"/>

    <!-- Cell 3 -->
    <rect x="55" y="115" width="40" height="25" rx="3" fill="#C8E6C9" stroke="#388E3C" stroke-width="1.5"/>
    <ellipse cx="75" cy="128" rx="8" ry="6" fill="#81C784" stroke="#1B5E20" stroke-width="1"/>

    <!-- Cell 4 -->
    <ellipse cx="125" cy="130" rx="22" ry="18" fill="#DCEDC8" stroke="#558B2F" stroke-width="1.5"/>
    <ellipse cx="125" cy="128" rx="7" ry="6" fill="#9CCC65" stroke="#33691E" stroke-width="1"/>

    <!-- Cell 5 -->
    <ellipse cx="95" cy="155" rx="18" ry="14" fill="#C8E6C9" stroke="#388E3C" stroke-width="1"/>
    <circle cx="95" cy="153" r="5" fill="#81C784" stroke="#1B5E20" stroke-width="0.8"/>
  </g>

  <!-- Info panel -->
  <g transform="translate(430,80)">
    <rect x="0" y="0" width="155" height="260" rx="8" fill="white" stroke="#43A047" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="155" height="26" rx="8" fill="#43A047" opacity="0.9"/>
    <rect x="0" y="18" width="155" height="10" fill="#43A047" opacity="0.9"/>
    <text x="78" y="18" font-family="Arial,sans-serif" font-size="11" fill="white" text-anchor="middle" font-weight="bold">КЛЮЧЕВЫЕ ФАКТЫ</text>

    <circle cx="18" cy="48" r="6" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
    <text x="18" y="52" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">1</text>
    <text x="30" y="52" font-family="Arial,sans-serif" font-size="9" fill="#333">Клетка — единица жизни</text>

    <circle cx="18" cy="78" r="6" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
    <text x="18" y="82" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">2</text>
    <text x="30" y="82" font-family="Arial,sans-serif" font-size="9" fill="#333">Открыта Р. Гуком</text>
    <text x="30" y="94" font-family="Arial,sans-serif" font-size="8" fill="#777">в 1665 году</text>

    <circle cx="18" cy="114" r="6" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
    <text x="18" y="118" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">3</text>
    <text x="30" y="118" font-family="Arial,sans-serif" font-size="9" fill="#333">Все живое из клеток</text>

    <circle cx="18" cy="148" r="6" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
    <text x="18" y="152" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">4</text>
    <text x="30" y="152" font-family="Arial,sans-serif" font-size="9" fill="#333">Клетки разнообразны</text>
    <text x="30" y="164" font-family="Arial,sans-serif" font-size="8" fill="#777">по форме и размеру</text>

    <line x1="10" y1="180" x2="145" y2="180" stroke="#C8E6C9" stroke-width="1"/>
    <text x="78" y="198" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Цитология</text>
    <text x="78" y="212" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">наука о клетке</text>

    <line x1="10" y1="225" x2="145" y2="225" stroke="#C8E6C9" stroke-width="1"/>
    <text x="78" y="242" font-family="Arial,sans-serif" font-size="8" fill="#888" text-anchor="middle">Размер клетки:</text>
    <text x="78" y="254" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">0.001 - 0.1 мм</text>
  </g>
''' + svg_footer("Что такое клетка"))

# ===== LESSON 2: Части клетки =====
write_svg(2, svg_header("Части клетки", "Биология 5 класс - Урок 2") + '''
  <!-- Large cell diagram -->
  <g transform="translate(30,80)">
    <rect x="0" y="0" width="280" height="265" rx="8" fill="white" stroke="#388E3C" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="280" height="24" rx="8" fill="#388E3C" opacity="0.9"/>
    <rect x="0" y="16" width="280" height="10" fill="#388E3C" opacity="0.9"/>
    <text x="140" y="17" font-family="Arial,sans-serif" font-size="11" fill="white" text-anchor="middle" font-weight="bold">СТРОЕНИЕ КЛЕТКИ</text>

    <!-- Cell membrane (outer) -->
    <ellipse cx="140" cy="155" rx="115" ry="90" fill="#E8F5E9" stroke="#2E7D32" stroke-width="3"/>
    <text x="260" y="100" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32">мембрана</text>
    <line x1="225" y1="102" x2="205" y2="108" stroke="#2E7D32" stroke-width="0.8"/>

    <!-- Cytoplasm label -->
    <text x="55" y="130" font-family="Arial,sans-serif" font-size="9" fill="#558B2F" font-style="italic">цитоплазма</text>

    <!-- Nucleus -->
    <ellipse cx="140" cy="150" rx="40" ry="30" fill="#A5D6A7" stroke="#1B5E20" stroke-width="2"/>
    <circle cx="140" cy="148" r="10" fill="#66BB6A" stroke="#1B5E20" stroke-width="1"/>
    <text x="140" y="152" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">ядрышко</text>
    <text x="140" y="175" font-family="Arial,sans-serif" font-size="9" fill="#1B5E20" text-anchor="middle" font-weight="bold">ядро</text>

    <!-- Mitochondria -->
    <ellipse cx="80" cy="140" rx="18" ry="8" fill="#FFCC80" stroke="#E65100" stroke-width="1.2"/>
    <path d="M66,140 Q72,134 80,140 Q88,146 94,140" fill="none" stroke="#E65100" stroke-width="0.8"/>
    <text x="80" y="158" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">митохондрия</text>

    <!-- Ribosomes -->
    <circle cx="100" cy="180" r="3" fill="#EF9A9A" stroke="#C62828" stroke-width="0.8"/>
    <circle cx="108" cy="175" r="3" fill="#EF9A9A" stroke="#C62828" stroke-width="0.8"/>
    <circle cx="96" cy="174" r="3" fill="#EF9A9A" stroke="#C62828" stroke-width="0.8"/>
    <text x="100" y="192" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">рибосомы</text>

    <!-- Vacuole -->
    <ellipse cx="195" cy="170" rx="22" ry="15" fill="#BBDEFB" stroke="#1565C0" stroke-width="1.2"/>
    <text x="195" y="174" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">вакуоль</text>

    <!-- Chloroplast (for plant cell) -->
    <ellipse cx="200" cy="130" rx="16" ry="9" fill="#81C784" stroke="#2E7D32" stroke-width="1.2"/>
    <line x1="188" y1="130" x2="212" y2="130" stroke="#2E7D32" stroke-width="0.5"/>
    <text x="200" y="148" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">хлоропласт</text>

    <!-- Cell wall indicator (outer dashed) -->
    <ellipse cx="140" cy="155" rx="122" ry="96" fill="none" stroke="#795548" stroke-width="1.5" stroke-dasharray="5,3"/>
    <text x="50" y="210" font-family="Arial,sans-serif" font-size="7" fill="#795548">клеточная стенка</text>

    <!-- ER -->
    <path d="M155,195 Q165,190 160,200 Q155,210 165,205 Q175,200 170,210" fill="none" stroke="#7E57C2" stroke-width="1.5"/>
    <text x="172" y="220" font-family="Arial,sans-serif" font-size="6" fill="#7E57C2">ЭПС</text>
  </g>

  <!-- Summary panel -->
  <g transform="translate(330,80)">
    <rect x="0" y="0" width="255" height="265" rx="8" fill="white" stroke="#43A047" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="255" height="24" rx="8" fill="#43A047" opacity="0.9"/>
    <rect x="0" y="16" width="255" height="10" fill="#43A047" opacity="0.9"/>
    <text x="128" y="17" font-family="Arial,sans-serif" font-size="11" fill="white" text-anchor="middle" font-weight="bold">ФУНКЦИИ ЧАСТЕЙ КЛЕТКИ</text>

    <!-- Membrane -->
    <rect x="10" y="35" width="8" height="8" rx="2" fill="#2E7D32"/>
    <text x="24" y="43" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" font-weight="bold">Мембрана</text>
    <text x="24" y="55" font-family="Arial,sans-serif" font-size="8" fill="#555">Защита, обмен веществ, форма</text>

    <!-- Cytoplasm -->
    <rect x="10" y="68" width="8" height="8" rx="2" fill="#558B2F"/>
    <text x="24" y="76" font-family="Arial,sans-serif" font-size="10" fill="#558B2F" font-weight="bold">Цитоплазма</text>
    <text x="24" y="88" font-family="Arial,sans-serif" font-size="8" fill="#555">Среда для органоидов, обмен</text>

    <!-- Nucleus -->
    <rect x="10" y="101" width="8" height="8" rx="2" fill="#1B5E20"/>
    <text x="24" y="109" font-family="Arial,sans-serif" font-size="10" fill="#1B5E20" font-weight="bold">Ядро</text>
    <text x="24" y="121" font-family="Arial,sans-serif" font-size="8" fill="#555">Наследственная информация, ДНК</text>

    <!-- Mitochondria -->
    <rect x="10" y="134" width="8" height="8" rx="2" fill="#E65100"/>
    <text x="24" y="142" font-family="Arial,sans-serif" font-size="10" fill="#E65100" font-weight="bold">Митохондрии</text>
    <text x="24" y="154" font-family="Arial,sans-serif" font-size="8" fill="#555">Энергетические станции клетки</text>

    <!-- Ribosomes -->
    <rect x="10" y="167" width="8" height="8" rx="2" fill="#C62828"/>
    <text x="24" y="175" font-family="Arial,sans-serif" font-size="10" fill="#C62828" font-weight="bold">Рибосомы</text>
    <text x="24" y="187" font-family="Arial,sans-serif" font-size="8" fill="#555">Синтез белка</text>

    <!-- Vacuole -->
    <rect x="10" y="200" width="8" height="8" rx="2" fill="#1565C0"/>
    <text x="24" y="208" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" font-weight="bold">Вакуоль</text>
    <text x="24" y="220" font-family="Arial,sans-serif" font-size="8" fill="#555">Запасание веществ и воды</text>

    <!-- Chloroplast -->
    <rect x="10" y="233" width="8" height="8" rx="2" fill="#2E7D32"/>
    <text x="24" y="241" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" font-weight="bold">Хлоропласт</text>
    <text x="24" y="253" font-family="Arial,sans-serif" font-size="8" fill="#555">Фотосинтез (только у растений)</text>
  </g>
''' + svg_footer("Части клетки"))

# ===== LESSON 3: Разнообразие клеток =====
write_svg(3, svg_header("Разнообразие клеток", "Биология 5 класс - Урок 3", "#E3F2FD", "#BBDEFB", "#1565C0") + '''
  <!-- Different cell types -->
  <g transform="translate(20,75)">
    <!-- Nerve cell -->
    <rect x="0" y="0" width="170" height="120" rx="8" fill="white" stroke="#1565C0" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="22" rx="8" fill="#1565C0" opacity="0.85"/>
    <rect x="0" y="14" width="170" height="10" fill="#1565C0" opacity="0.85"/>
    <text x="85" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Нервная клетка</text>
    <!-- Cell body -->
    <ellipse cx="85" cy="65" rx="20" ry="18" fill="#BBDEFB" stroke="#1565C0" stroke-width="1.5"/>
    <circle cx="85" cy="63" r="6" fill="#64B5F6" stroke="#0D47A1" stroke-width="0.8"/>
    <!-- Axon -->
    <line x1="85" y1="83" x2="85" y2="115" stroke="#1565C0" stroke-width="2"/>
    <line x1="85" y1="115" x2="75" y2="118" stroke="#1565C0" stroke-width="1.5"/>
    <line x1="85" y1="115" x2="95" y2="118" stroke="#1565C0" stroke-width="1.5"/>
    <!-- Dendrites -->
    <line x1="65" y1="60" x2="40" y2="48" stroke="#1565C0" stroke-width="1.5"/>
    <line x1="40" y1="48" x2="30" y2="42" stroke="#1565C0" stroke-width="1"/>
    <line x1="40" y1="48" x2="35" y2="55" stroke="#1565C0" stroke-width="1"/>
    <line x1="105" y1="55" x2="130" y2="42" stroke="#1565C0" stroke-width="1.5"/>
    <line x1="130" y1="42" x2="140" y2="35" stroke="#1565C0" stroke-width="1"/>
    <line x1="130" y1="42" x2="135" y2="50" stroke="#1565C0" stroke-width="1"/>
    <line x1="75" y1="48" x2="68" y2="35" stroke="#1565C0" stroke-width="1.5"/>
    <line x1="95" y1="50" x2="102" y2="38" stroke="#1565C0" stroke-width="1.5"/>

    <!-- Muscle cell -->
    <rect x="180" y="0" width="170" height="120" rx="8" fill="white" stroke="#C62828" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="22" rx="8" fill="#C62828" opacity="0.85" transform="translate(180,0)"/>
    <rect x="180" y="14" width="170" height="10" fill="#C62828" opacity="0.85"/>
    <text x="265" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Мышечная клетка</text>
    <!-- Spindle shape -->
    <ellipse cx="265" cy="70" rx="50" ry="14" fill="#FFCDD2" stroke="#C62828" stroke-width="1.5"/>
    <line x1="220" y1="70" x2="310" y2="70" stroke="#E57373" stroke-width="0.8"/>
    <line x1="225" y1="63" x2="305" y2="63" stroke="#E57373" stroke-width="0.6" opacity="0.7"/>
    <line x1="225" y1="77" x2="305" y2="77" stroke="#E57373" stroke-width="0.6" opacity="0.7"/>
    <!-- Nuclei -->
    <ellipse cx="265" cy="68" rx="12" ry="8" fill="#EF9A9A" stroke="#C62828" stroke-width="1"/>
    <text x="265" y="100" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Веретеновидная</text>
    <text x="265" y="112" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">форма</text>

    <!-- Blood cells -->
    <rect x="360" y="0" width="220" height="120" rx="8" fill="white" stroke="#D32F2F" stroke-width="1.5"/>
    <rect x="360" y="0" width="220" height="22" rx="8" fill="#D32F2F" opacity="0.85"/>
    <rect x="360" y="14" width="220" height="10" fill="#D32F2F" opacity="0.85"/>
    <text x="470" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Клетки крови</text>
    <!-- Red blood cells (biconcave discs) -->
    <ellipse cx="400" cy="55" rx="14" ry="10" fill="#EF5350" stroke="#C62828" stroke-width="1"/>
    <ellipse cx="400" cy="55" rx="6" ry="4" fill="#FFCDD2" stroke="none"/>
    <ellipse cx="430" cy="60" rx="14" ry="10" fill="#EF5350" stroke="#C62828" stroke-width="1"/>
    <ellipse cx="430" cy="60" rx="6" ry="4" fill="#FFCDD2" stroke="none"/>
    <ellipse cx="415" cy="75" rx="14" ry="10" fill="#EF5350" stroke="#C62828" stroke-width="1"/>
    <ellipse cx="415" cy="75" rx="6" ry="4" fill="#FFCDD2" stroke="none"/>
    <text x="420" y="100" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle">эритроциты</text>
    <!-- White blood cell -->
    <circle cx="510" cy="65" r="16" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
    <circle cx="510" cy="63" r="6" fill="#90CAF9" stroke="#0D47A1" stroke-width="0.8"/>
    <path d="M496,58 Q493,50 500,55" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
    <path d="M524,60 Q530,55 526,62" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
    <text x="510" y="95" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle">лейкоцит</text>
    <!-- Platelet -->
    <ellipse cx="550" cy="80" rx="6" ry="4" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
    <text x="550" y="95" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">тромбоцит</text>
  </g>

  <!-- More cell types -->
  <g transform="translate(20,210)">
    <!-- Epithelial cell -->
    <rect x="0" y="0" width="170" height="140" rx="8" fill="white" stroke="#FF8F00" stroke-width="1.5"/>
    <rect x="0" y="0" width="170" height="22" rx="8" fill="#FF8F00" opacity="0.85"/>
    <rect x="0" y="14" width="170" height="10" fill="#FF8F00" opacity="0.85"/>
    <text x="85" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Клетки эпителия</text>
    <!-- Flat cells arranged like tiles -->
    <rect x="15" y="32" width="35" height="25" rx="3" fill="#FFF3E0" stroke="#FF8F00" stroke-width="1"/>
    <ellipse cx="32" cy="44" rx="8" ry="5" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
    <rect x="50" y="32" width="35" height="25" rx="3" fill="#FFF3E0" stroke="#FF8F00" stroke-width="1"/>
    <ellipse cx="67" cy="44" rx="8" ry="5" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
    <rect x="85" y="32" width="35" height="25" rx="3" fill="#FFF3E0" stroke="#FF8F00" stroke-width="1"/>
    <ellipse cx="102" cy="44" rx="8" ry="5" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
    <rect x="120" y="32" width="35" height="25" rx="3" fill="#FFF3E0" stroke="#FF8F00" stroke-width="1"/>
    <ellipse cx="137" cy="44" rx="8" ry="5" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
    <rect x="30" y="57" width="35" height="25" rx="3" fill="#FFF3E0" stroke="#FF8F00" stroke-width="1"/>
    <ellipse cx="47" cy="69" rx="8" ry="5" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
    <rect x="65" y="57" width="35" height="25" rx="3" fill="#FFF3E0" stroke="#FF8F00" stroke-width="1"/>
    <ellipse cx="82" cy="69" rx="8" ry="5" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
    <rect x="100" y="57" width="35" height="25" rx="3" fill="#FFF3E0" stroke="#FF8F00" stroke-width="1"/>
    <ellipse cx="117" cy="69" rx="8" ry="5" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
    <text x="85" y="100" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Плоская форма</text>
    <text x="85" y="115" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">Покрывают поверхность</text>
    <text x="85" y="127" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">кожи и органов</text>

    <!-- Egg cell -->
    <rect x="180" y="0" width="170" height="140" rx="8" fill="white" stroke="#AD1457" stroke-width="1.5"/>
    <rect x="180" y="0" width="170" height="22" rx="8" fill="#AD1457" opacity="0.85"/>
    <rect x="180" y="14" width="170" height="10" fill="#AD1457" opacity="0.85"/>
    <text x="265" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Яйцеклетка</text>
    <!-- Large spherical cell -->
    <circle cx="265" cy="80" r="40" fill="#FCE4EC" stroke="#AD1457" stroke-width="2"/>
    <circle cx="265" cy="75" r="15" fill="#F48FB1" stroke="#AD1457" stroke-width="1.5"/>
    <circle cx="265" cy="73" r="5" fill="#E91E63" stroke="#880E4F" stroke-width="0.8"/>
    <!-- Protective layers -->
    <circle cx="265" cy="80" r="45" fill="none" stroke="#F48FB1" stroke-width="1" stroke-dasharray="3,2"/>
    <text x="265" y="98" font-family="Arial,sans-serif" font-size="7" fill="#880E4F" text-anchor="middle">ядро</text>
    <text x="265" y="135" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Самая крупная клетка</text>

    <!-- Plant cell -->
    <rect x="360" y="0" width="220" height="140" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
    <rect x="360" y="0" width="220" height="22" rx="8" fill="#2E7D32" opacity="0.85"/>
    <rect x="360" y="14" width="220" height="10" fill="#2E7D32" opacity="0.85"/>
    <text x="470" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Растительная клетка</text>
    <!-- Rectangular plant cell -->
    <rect x="385" y="35" width="55" height="40" rx="2" fill="#E8F5E9" stroke="#795548" stroke-width="2"/>
    <rect x="387" y="37" width="51" height="36" rx="1" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
    <ellipse cx="412" cy="52" rx="10" ry="8" fill="#81C784" stroke="#1B5E20" stroke-width="1"/>
    <ellipse cx="400" cy="58" rx="8" ry="5" fill="#BBDEFB" stroke="#1565C0" stroke-width="0.8"/>
    <text x="412" y="85" font-family="Arial,sans-serif" font-size="6" fill="#795548" text-anchor="middle">стенка</text>
    <text x="412" y="95" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">ядро+вакуоль</text>

    <rect x="450" y="35" width="55" height="40" rx="2" fill="#E8F5E9" stroke="#795548" stroke-width="2"/>
    <rect x="452" y="37" width="51" height="36" rx="1" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
    <ellipse cx="477" cy="52" rx="10" ry="8" fill="#81C784" stroke="#1B5E20" stroke-width="1"/>
    <ellipse cx="490" cy="58" rx="8" ry="5" fill="#BBDEFB" stroke="#1565C0" stroke-width="0.8"/>

    <rect x="415" y="75" width="55" height="40" rx="2" fill="#E8F5E9" stroke="#795548" stroke-width="2"/>
    <rect x="417" y="77" width="51" height="36" rx="1" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
    <ellipse cx="442" cy="92" rx="10" ry="8" fill="#81C784" stroke="#1B5E20" stroke-width="1"/>

    <rect x="510" y="35" width="55" height="40" rx="2" fill="#E8F5E9" stroke="#795548" stroke-width="2"/>
    <rect x="512" y="37" width="51" height="36" rx="1" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
    <ellipse cx="537" cy="52" rx="10" ry="8" fill="#81C784" stroke="#1B5E20" stroke-width="1"/>

    <text x="470" y="125" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Прямоугольная форма</text>
    <text x="470" y="137" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">Клеточная стенка + хлоропласты</text>
  </g>
''' + svg_footer("Разнообразие клеток", "#1565C0"))

# ===== LESSON 4: Деление клетки =====
write_svg(4, svg_header("Деление клетки", "Биология 5 класс - Урок 4", "#F3E5F5", "#E1BEE7", "#7B1FA2") + '''
  <!-- Cell division stages -->
  <g transform="translate(15,75)">
    <!-- Stage 1: Interphase -->
    <rect x="0" y="0" width="135" height="165" rx="8" fill="white" stroke="#7B1FA2" stroke-width="1.5"/>
    <rect x="0" y="0" width="135" height="22" rx="8" fill="#7B1FA2" opacity="0.85"/>
    <rect x="0" y="14" width="135" height="10" fill="#7B1FA2" opacity="0.85"/>
    <text x="68" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Интерфаза</text>
    <ellipse cx="68" cy="85" rx="40" ry="32" fill="#F3E5F5" stroke="#7B1FA2" stroke-width="1.5"/>
    <circle cx="68" cy="82" r="14" fill="#CE93D8" stroke="#4A148C" stroke-width="1.5"/>
    <text x="68" y="86" font-family="Arial,sans-serif" font-size="7" fill="#4A148C" text-anchor="middle">ядро</text>
    <!-- Chromatin threads -->
    <line x1="58" y1="78" x2="78" y2="78" stroke="#4A148C" stroke-width="0.8" opacity="0.5"/>
    <line x1="62" y1="85" x2="74" y2="85" stroke="#4A148C" stroke-width="0.8" opacity="0.5"/>
    <text x="68" y="130" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Рост и подготовка</text>
    <text x="68" y="143" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">Удвоение ДНК</text>
    <text x="68" y="156" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle">1 клетка</text>

    <!-- Arrow 1 -->
    <path d="M140,85 L155,85" stroke="#7B1FA2" stroke-width="2" marker-end="url(#arr1)"/>
    <defs><marker id="arr1" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6" fill="#7B1FA2"/></marker></defs>

    <!-- Stage 2: Prophase -->
    <rect x="160" y="0" width="135" height="165" rx="8" fill="white" stroke="#7B1FA2" stroke-width="1.5"/>
    <rect x="160" y="0" width="135" height="22" rx="8" fill="#7B1FA2" opacity="0.85"/>
    <rect x="160" y="14" width="135" height="10" fill="#7B1FA2" opacity="0.85"/>
    <text x="228" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Профаза</text>
    <ellipse cx="228" cy="85" rx="40" ry="32" fill="#F3E5F5" stroke="#7B1FA2" stroke-width="1.5"/>
    <!-- Chromosomes visible -->
    <line x1="215" y1="72" x2="225" y2="88" stroke="#4A148C" stroke-width="2.5"/>
    <line x1="225" y1="72" x2="235" y2="88" stroke="#4A148C" stroke-width="2.5"/>
    <line x1="220" y1="72" x2="230" y2="88" stroke="#6A1B9A" stroke-width="2"/>
    <line x1="233" y1="72" x2="243" y2="88" stroke="#6A1B9A" stroke-width="2"/>
    <!-- Nuclear membrane dissolving -->
    <ellipse cx="228" cy="82" rx="22" ry="16" fill="none" stroke="#4A148C" stroke-width="0.8" stroke-dasharray="3,2" opacity="0.5"/>
    <text x="228" y="130" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Хромосомы видны</text>
    <text x="228" y="143" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">Ядерная оболочка</text>
    <text x="228" y="156" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">исчезает</text>

    <!-- Arrow 2 -->
    <path d="M300,85 L315,85" stroke="#7B1FA2" stroke-width="2" marker-end="url(#arr2)"/>
    <defs><marker id="arr2" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6" fill="#7B1FA2"/></marker></defs>

    <!-- Stage 3: Metaphase/Anaphase -->
    <rect x="320" y="0" width="135" height="165" rx="8" fill="white" stroke="#7B1FA2" stroke-width="1.5"/>
    <rect x="320" y="0" width="135" height="22" rx="8" fill="#7B1FA2" opacity="0.85"/>
    <rect x="320" y="14" width="135" height="10" fill="#7B1FA2" opacity="0.85"/>
    <text x="388" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Метафаза</text>
    <ellipse cx="388" cy="85" rx="40" ry="32" fill="#F3E5F5" stroke="#7B1FA2" stroke-width="1.5"/>
    <!-- Spindle fibers -->
    <line x1="365" y1="65" x2="388" y2="80" stroke="#9C27B0" stroke-width="0.5" opacity="0.6"/>
    <line x1="410" y1="65" x2="388" y2="80" stroke="#9C27B0" stroke-width="0.5" opacity="0.6"/>
    <line x1="365" y1="100" x2="388" y2="80" stroke="#9C27B0" stroke-width="0.5" opacity="0.6"/>
    <line x1="410" y1="100" x2="388" y2="80" stroke="#9C27B0" stroke-width="0.5" opacity="0.6"/>
    <!-- Chromosomes at equator -->
    <line x1="378" y1="75" x2="378" y2="85" stroke="#4A148C" stroke-width="2.5"/>
    <line x1="383" y1="75" x2="383" y2="85" stroke="#4A148C" stroke-width="2.5"/>
    <line x1="393" y1="75" x2="393" y2="85" stroke="#4A148C" stroke-width="2.5"/>
    <line x1="398" y1="75" x2="398" y2="85" stroke="#4A148C" stroke-width="2.5"/>
    <!-- Equator line -->
    <line x1="360" y1="80" x2="416" y2="80" stroke="#CE93D8" stroke-width="0.8" stroke-dasharray="2,2"/>
    <text x="388" y="130" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Хромосомы на экваторе</text>
    <text x="388" y="143" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">Веретено деления</text>

    <!-- Arrow 3 -->
    <path d="M460,85 L475,85" stroke="#7B1FA2" stroke-width="2" marker-end="url(#arr3)"/>
    <defs><marker id="arr3" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6" fill="#7B1FA2"/></marker></defs>

    <!-- Stage 4: Two daughter cells -->
    <rect x="480" y="0" width="105" height="165" rx="8" fill="white" stroke="#7B1FA2" stroke-width="1.5"/>
    <rect x="480" y="0" width="105" height="22" rx="8" fill="#7B1FA2" opacity="0.85"/>
    <rect x="480" y="14" width="105" height="10" fill="#7B1FA2" opacity="0.85"/>
    <text x="533" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Результат</text>
    <ellipse cx="510" cy="80" rx="25" ry="20" fill="#F3E5F5" stroke="#7B1FA2" stroke-width="1.5"/>
    <circle cx="510" cy="78" r="8" fill="#CE93D8" stroke="#4A148C" stroke-width="1"/>
    <ellipse cx="556" cy="80" rx="25" ry="20" fill="#F3E5F5" stroke="#7B1FA2" stroke-width="1.5"/>
    <circle cx="556" cy="78" r="8" fill="#CE93D8" stroke="#4A148C" stroke-width="1"/>
    <text x="533" y="120" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Две дочерние</text>
    <text x="533" y="133" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">клетки</text>
    <text x="533" y="148" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">2 клетки</text>
  </g>

  <!-- Bottom info -->
  <g transform="translate(15,255)">
    <rect x="0" y="0" width="570" height="95" rx="8" fill="white" stroke="#7B1FA2" stroke-width="1" opacity="0.9"/>
    <text x="285" y="20" font-family="Arial,sans-serif" font-size="11" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Значение деления клетки</text>
    <line x1="20" y1="28" x2="550" y2="28" stroke="#E1BEE7" stroke-width="1"/>

    <circle cx="40" cy="50" r="12" fill="#F3E5F5" stroke="#7B1FA2" stroke-width="1"/>
    <text x="40" y="54" font-family="Arial,sans-serif" font-size="10" fill="#7B1FA2" text-anchor="middle">1</text>
    <text x="58" y="54" font-family="Arial,sans-serif" font-size="9" fill="#333">Рост организма</text>

    <circle cx="200" cy="50" r="12" fill="#F3E5F5" stroke="#7B1FA2" stroke-width="1"/>
    <text x="200" y="54" font-family="Arial,sans-serif" font-size="10" fill="#7B1FA2" text-anchor="middle">2</text>
    <text x="218" y="54" font-family="Arial,sans-serif" font-size="9" fill="#333">Замена старых клеток</text>

    <circle cx="400" cy="50" r="12" fill="#F3E5F5" stroke="#7B1FA2" stroke-width="1"/>
    <text x="400" y="54" font-family="Arial,sans-serif" font-size="10" fill="#7B1FA2" text-anchor="middle">3</text>
    <text x="418" y="54" font-family="Arial,sans-serif" font-size="9" fill="#333">Размножение</text>

    <text x="285" y="80" font-family="Arial,sans-serif" font-size="9" fill="#555" text-anchor="middle">Перед делением ДНК удваивается, чтобы каждая дочерняя клетка получила полную копию</text>
  </g>
''' + svg_footer("Деление клетки", "#7B1FA2"))

# ===== LESSON 5: Бактерии =====
write_svg(5, svg_header("Бактерии", "Биология 5 класс - Урок 5", "#FFF3E0", "#FFE0B2", "#E65100") + '''
  <!-- Bacteria types -->
  <g transform="translate(15,75)">
    <!-- Cocci -->
    <rect x="0" y="0" width="185" height="120" rx="8" fill="white" stroke="#E65100" stroke-width="1.5"/>
    <rect x="0" y="0" width="185" height="22" rx="8" fill="#E65100" opacity="0.85"/>
    <rect x="0" y="14" width="185" height="10" fill="#E65100" opacity="0.85"/>
    <text x="93" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Кокки (шаровидные)</text>
    <!-- Single coccus -->
    <circle cx="40" cy="60" r="12" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
    <!-- Diplococci -->
    <circle cx="85" cy="58" r="10" fill="#FFE0B2" stroke="#E65100" stroke-width="1.2"/>
    <circle cx="102" cy="62" r="10" fill="#FFE0B2" stroke="#E65100" stroke-width="1.2"/>
    <!-- Streptococci (chain) -->
    <circle cx="38" cy="95" r="8" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
    <circle cx="54" cy="95" r="8" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
    <circle cx="70" cy="95" r="8" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
    <circle cx="86" cy="95" r="8" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
    <!-- Staphylococci (cluster) -->
    <circle cx="140" cy="85" r="8" fill="#FFB74D" stroke="#E65100" stroke-width="1"/>
    <circle cx="155" cy="90" r="8" fill="#FFB74D" stroke="#E65100" stroke-width="1"/>
    <circle cx="148" cy="78" r="8" fill="#FFB74D" stroke="#E65100" stroke-width="1"/>
    <circle cx="163" cy="80" r="8" fill="#FFB74D" stroke="#E65100" stroke-width="1"/>
    <text x="145" y="110" font-family="Arial,sans-serif" font-size="6" fill="#888" text-anchor="middle">гроздья</text>

    <!-- Bacilli -->
    <rect x="195" y="0" width="185" height="120" rx="8" fill="white" stroke="#E65100" stroke-width="1.5"/>
    <rect x="195" y="0" width="185" height="22" rx="8" fill="#E65100" opacity="0.85"/>
    <rect x="195" y="14" width="185" height="10" fill="#E65100" opacity="0.85"/>
    <text x="288" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Бациллы (палочки)</text>
    <!-- Rod-shaped bacteria -->
    <rect x="220" y="48" width="35" height="14" rx="7" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
    <rect x="270" y="52" width="30" height="12" rx="6" fill="#FFCC80" stroke="#E65100" stroke-width="1.2"/>
    <rect x="315" y="46" width="40" height="15" rx="7" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
    <!-- With flagella -->
    <rect x="225" y="85" width="35" height="12" rx="6" fill="#FFCC80" stroke="#E65100" stroke-width="1.2"/>
    <path d="M225,91 Q218,88 215,93 Q212,98 208,95" fill="none" stroke="#E65100" stroke-width="0.8"/>
    <path d="M260,91 Q265,85 270,88" fill="none" stroke="#E65100" stroke-width="0.8"/>
    <rect x="285" y="88" width="32" height="12" rx="6" fill="#FFE0B2" stroke="#E65100" stroke-width="1.2"/>
    <text x="288" y="110" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">с жгутиками</text>

    <!-- Spirilla -->
    <rect x="390" y="0" width="195" height="120" rx="8" fill="white" stroke="#E65100" stroke-width="1.5"/>
    <rect x="390" y="0" width="195" height="22" rx="8" fill="#E65100" opacity="0.85"/>
    <rect x="390" y="14" width="195" height="10" fill="#E65100" opacity="0.85"/>
    <text x="488" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Спириллы (извитые)</text>
    <!-- Spirillum -->
    <path d="M420,55 Q430,45 440,55 Q450,65 460,55 Q470,45 480,55 Q490,65 500,55" fill="none" stroke="#E65100" stroke-width="3" stroke-linecap="round"/>
    <!-- Vibrio (comma) -->
    <path d="M430,85 Q450,75 460,90" fill="none" stroke="#E65100" stroke-width="3.5" stroke-linecap="round"/>
    <text x="445" y="105" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">вибрион</text>
    <!-- Spirochete -->
    <path d="M480,80 Q488,72 496,80 Q504,88 512,80 Q520,72 528,80 Q536,88 544,80" fill="none" stroke="#BF360C" stroke-width="2" stroke-linecap="round"/>
    <text x="512" y="105" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">спирохета</text>
  </g>

  <!-- Bacteria structure -->
  <g transform="translate(15,210)">
    <rect x="0" y="0" width="280" height="140" rx="8" fill="white" stroke="#E65100" stroke-width="1.5"/>
    <rect x="0" y="0" width="280" height="22" rx="8" fill="#E65100" opacity="0.85"/>
    <rect x="0" y="14" width="280" height="10" fill="#E65100" opacity="0.85"/>
    <text x="140" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">СТРОЕНИЕ БАКТЕРИИ</text>

    <!-- Large bacterium -->
    <ellipse cx="120" cy="85" rx="55" ry="30" fill="#FFE0B2" stroke="#E65100" stroke-width="2"/>
    <!-- Capsule -->
    <ellipse cx="120" cy="85" rx="62" ry="35" fill="none" stroke="#FF8F00" stroke-width="1.5" stroke-dasharray="4,2"/>
    <text x="65" y="60" font-family="Arial,sans-serif" font-size="7" fill="#FF8F00">капсула</text>
    <!-- Cell wall -->
    <text x="180" y="60" font-family="Arial,sans-serif" font-size="7" fill="#E65100">клеточная стенка</text>
    <line x1="175" y1="62" x2="165" y2="68" stroke="#E65100" stroke-width="0.8"/>
    <!-- Cytoplasm -->
    <text x="100" y="85" font-family="Arial,sans-serif" font-size="7" fill="#BF360C">цитоплазма</text>
    <!-- Nucleoid -->
    <ellipse cx="135" cy="82" rx="18" ry="10" fill="#FFCC80" stroke="#BF360C" stroke-width="1" stroke-dasharray="2,1"/>
    <text x="135" y="86" font-family="Arial,sans-serif" font-size="6" fill="#BF360C" text-anchor="middle">нуклеоид</text>
    <!-- Ribosomes -->
    <circle cx="95" cy="78" r="2" fill="#BF360C"/>
    <circle cx="100" cy="92" r="2" fill="#BF360C"/>
    <circle cx="150" cy="92" r="2" fill="#BF360C"/>
    <text x="160" y="96" font-family="Arial,sans-serif" font-size="6" fill="#888">рибосомы</text>
    <!-- Flagellum -->
    <path d="M175,85 Q185,78 190,85 Q195,92 200,85 Q205,78 210,85" fill="none" stroke="#E65100" stroke-width="1.5"/>
    <text x="210" y="80" font-family="Arial,sans-serif" font-size="7" fill="#E65100">жгутик</text>
    <!-- Pili -->
    <line x1="80" y1="70" x2="68" y2="60" stroke="#BF360C" stroke-width="0.8"/>
    <line x1="78" y1="95" x2="66" y2="105" stroke="#BF360C" stroke-width="0.8"/>
    <text x="55" y="115" font-family="Arial,sans-serif" font-size="6" fill="#888">пили</text>
  </g>

  <!-- Facts panel -->
  <g transform="translate(310,210)">
    <rect x="0" y="0" width="275" height="140" rx="8" fill="white" stroke="#E65100" stroke-width="1.5"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#E65100" opacity="0.85"/>
    <rect x="0" y="14" width="275" height="10" fill="#E65100" opacity="0.85"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ОСОБЕННОСТИ БАКТЕРИЙ</text>

    <text x="15" y="42" font-family="Arial,sans-serif" font-size="9" fill="#E65100" font-weight="bold">Нет ядра (прокариоты)</text>
    <text x="15" y="55" font-family="Arial,sans-serif" font-size="8" fill="#555">ДНК в виде кольца в цитоплазме</text>

    <text x="15" y="74" font-family="Arial,sans-serif" font-size="9" fill="#E65100" font-weight="bold">Споры для выживания</text>
    <text x="15" y="87" font-family="Arial,sans-serif" font-size="8" fill="#555">Пережидают неблагоприятные условия</text>

    <text x="15" y="106" font-family="Arial,sans-serif" font-size="9" fill="#E65100" font-weight="bold">Размножение делением надвое</text>
    <text x="15" y="119" font-family="Arial,sans-serif" font-size="8" fill="#555">Каждые 20 минут в благоприятных условиях</text>

    <text x="15" y="136" font-family="Arial,sans-serif" font-size="9" fill="#E65100" font-weight="bold">Размер: 0.5 - 5 мкм</text>
  </g>
''' + svg_footer("Бактерии", "#E65100"))

# ===== LESSON 6: Грибы — особое царство =====
write_svg(6, svg_header("Грибы - особое царство", "Биология 5 класс - Урок 6", "#EFEBE9", "#D7CCC8", "#5D4037") + '''
  <!-- Mushroom anatomy -->
  <g transform="translate(30,75)">
    <rect x="0" y="0" width="250" height="275" rx="8" fill="white" stroke="#5D4037" stroke-width="1.5"/>
    <rect x="0" y="0" width="250" height="24" rx="8" fill="#5D4037" opacity="0.85"/>
    <rect x="0" y="16" width="250" height="10" fill="#5D4037" opacity="0.85"/>
    <text x="125" y="17" font-family="Arial,sans-serif" font-size="11" fill="white" text-anchor="middle" font-weight="bold">СТРОЕНИЕ ГРИБА</text>

    <!-- Mushroom cap -->
    <ellipse cx="125" cy="75" rx="70" ry="25" fill="#8D6E63" stroke="#4E342E" stroke-width="2"/>
    <ellipse cx="125" cy="75" rx="65" ry="20" fill="#A1887F" stroke="none"/>
    <!-- Cap spots -->
    <circle cx="100" cy="70" r="5" fill="#795548" opacity="0.5"/>
    <circle cx="140" cy="68" r="4" fill="#795548" opacity="0.5"/>
    <circle cx="120" cy="65" r="3" fill="#795548" opacity="0.5"/>
    <text x="200" y="72" font-family="Arial,sans-serif" font-size="8" fill="#4E342E">шляпка</text>
    <line x1="195" y1="74" x2="185" y2="76" stroke="#4E342E" stroke-width="0.8"/>

    <!-- Gills under cap -->
    <line x1="70" y1="82" x2="80" y2="95" stroke="#D7CCC8" stroke-width="0.8"/>
    <line x1="85" y1="82" x2="90" y2="95" stroke="#D7CCC8" stroke-width="0.8"/>
    <line x1="100" y1="82" x2="103" y2="95" stroke="#D7CCC8" stroke-width="0.8"/>
    <line x1="115" y1="82" x2="116" y2="95" stroke="#D7CCC8" stroke-width="0.8"/>
    <line x1="130" y1="82" x2="129" y2="95" stroke="#D7CCC8" stroke-width="0.8"/>
    <line x1="145" y1="82" x2="142" y2="95" stroke="#D7CCC8" stroke-width="0.8"/>
    <line x1="160" y1="82" x2="155" y2="95" stroke="#D7CCC8" stroke-width="0.8"/>
    <line x1="175" y1="82" x2="168" y2="95" stroke="#D7CCC8" stroke-width="0.8"/>
    <text x="200" y="92" font-family="Arial,sans-serif" font-size="7" fill="#5D4037">пластинки</text>
    <line x1="195" y1="90" x2="178" y2="90" stroke="#5D4037" stroke-width="0.8"/>

    <!-- Stipe (stem) -->
    <rect x="110" y="95" width="30" height="80" rx="4" fill="#BCAAA4" stroke="#5D4037" stroke-width="1.5"/>
    <!-- Ring on stem -->
    <ellipse cx="125" cy="115" rx="20" ry="4" fill="#D7CCC8" stroke="#5D4037" stroke-width="1"/>
    <text x="155" y="130" font-family="Arial,sans-serif" font-size="8" fill="#4E342E">ножка</text>
    <line x1="150" y1="128" x2="142" y2="128" stroke="#4E342E" stroke-width="0.8"/>
    <text x="155" y="115" font-family="Arial,sans-serif" font-size="7" fill="#5D4037">кольцо</text>

    <!-- Mycelium (underground) -->
    <line x1="110" y1="175" x2="90" y2="200" stroke="#8D6E63" stroke-width="2"/>
    <line x1="90" y1="200" x2="70" y2="215" stroke="#8D6E63" stroke-width="1.5"/>
    <line x1="90" y1="200" x2="95" y2="220" stroke="#8D6E63" stroke-width="1.5"/>
    <line x1="70" y1="215" x2="55" y2="225" stroke="#8D6E63" stroke-width="1"/>
    <line x1="125" y1="175" x2="130" y2="205" stroke="#8D6E63" stroke-width="2"/>
    <line x1="130" y1="205" x2="120" y2="225" stroke="#8D6E63" stroke-width="1.5"/>
    <line x1="130" y1="205" x2="145" y2="222" stroke="#8D6E63" stroke-width="1.5"/>
    <line x1="140" y1="175" x2="160" y2="198" stroke="#8D6E63" stroke-width="2"/>
    <line x1="160" y1="198" x2="175" y2="218" stroke="#8D6E63" stroke-width="1.5"/>
    <line x1="160" y1="198" x2="155" y2="220" stroke="#8D6E63" stroke-width="1.5"/>
    <text x="125" y="242" font-family="Arial,sans-serif" font-size="9" fill="#4E342E" text-anchor="middle" font-weight="bold">грибница (мицелий)</text>
    <text x="125" y="258" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">Подземная часть из гифов</text>

    <!-- Soil line -->
    <line x1="10" y1="175" x2="240" y2="175" stroke="#795548" stroke-width="1" stroke-dasharray="5,3" opacity="0.5"/>
    <rect x="10" y="175" width="230" height="10" fill="#795548" opacity="0.1" rx="2"/>
  </g>

  <!-- Fungi characteristics panel -->
  <g transform="translate(300,75)">
    <rect x="0" y="0" width="285" height="275" rx="8" fill="white" stroke="#5D4037" stroke-width="1.5"/>
    <rect x="0" y="0" width="285" height="24" rx="8" fill="#5D4037" opacity="0.85"/>
    <rect x="0" y="16" width="285" height="10" fill="#5D4037" opacity="0.85"/>
    <text x="143" y="17" font-family="Arial,sans-serif" font-size="11" fill="white" text-anchor="middle" font-weight="bold">ПОЧЕМУ ГРИБЫ - ОСОБОЕ ЦАРСТВО</text>

    <!-- Similar to plants -->
    <rect x="10" y="35" width="265" height="55" rx="5" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1" opacity="0.7"/>
    <text x="20" y="52" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" font-weight="bold">Как растения:</text>
    <text x="20" y="66" font-family="Arial,sans-serif" font-size="9" fill="#555">Неподвижны, растут всю жизнь</text>
    <text x="20" y="80" font-family="Arial,sans-serif" font-size="9" fill="#555">Имеют клеточную стенку (из хитина!)</text>

    <!-- Similar to animals -->
    <rect x="10" y="100" width="265" height="55" rx="5" fill="#FFEBEE" stroke="#C62828" stroke-width="1" opacity="0.7"/>
    <text x="20" y="117" font-family="Arial,sans-serif" font-size="10" fill="#C62828" font-weight="bold">Как животные:</text>
    <text x="20" y="131" font-family="Arial,sans-serif" font-size="9" fill="#555">Гетеротрофы (не фотосинтезируют)</text>
    <text x="20" y="145" font-family="Arial,sans-serif" font-size="9" fill="#555">Запасное вещество - гликоген</text>

    <!-- Unique features -->
    <rect x="10" y="165" width="265" height="100" rx="5" fill="#FFF3E0" stroke="#E65100" stroke-width="1" opacity="0.7"/>
    <text x="20" y="182" font-family="Arial,sans-serif" font-size="10" fill="#E65100" font-weight="bold">Уникальные признаки:</text>
    <text x="20" y="198" font-family="Arial,sans-serif" font-size="9" fill="#555">Клеточная стенка из хитина</text>
    <text x="20" y="212" font-family="Arial,sans-serif" font-size="9" fill="#555">Тело из нитей - гифов</text>
    <text x="20" y="226" font-family="Arial,sans-serif" font-size="9" fill="#555">Размножение спорами</text>
    <text x="20" y="240" font-family="Arial,sans-serif" font-size="9" fill="#555">Всасывание питательных веществ</text>
    <text x="20" y="254" font-family="Arial,sans-serif" font-size="9" fill="#555">всей поверхностью</text>
  </g>
''' + svg_footer("Грибы - особое царство", "#5D4037"))

# ===== LESSON 7: Плесневые грибы и дрожжи =====
write_svg(7, svg_header("Плесневые грибы и дрожжи", "Биология 5 класс - Урок 7", "#F1F8E9", "#DCEDC8", "#558B2F") + '''
  <!-- Mucor (bread mold) -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="280" height="275" rx="8" fill="white" stroke="#558B2F" stroke-width="1.5"/>
    <rect x="0" y="0" width="280" height="22" rx="8" fill="#558B2F" opacity="0.85"/>
    <rect x="0" y="14" width="280" height="10" fill="#558B2F" opacity="0.85"/>
    <text x="140" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">МУКОР (белая плесень)</text>

    <!-- Bread slice -->
    <rect x="30" y="180" width="220" height="70" rx="5" fill="#FFECB3" stroke="#F9A825" stroke-width="1.5"/>
    <rect x="35" y="185" width="210" height="60" rx="3" fill="#FFF8E1" stroke="none"/>
    <text x="140" y="240" font-family="Arial,sans-serif" font-size="8" fill="#F9A825" text-anchor="middle">хлеб</text>

    <!-- Mycelium on bread -->
    <path d="M60,180 Q65,175 70,180 Q75,185 80,180" fill="none" stroke="#9E9E9E" stroke-width="0.8"/>
    <path d="M120,180 Q125,175 130,180" fill="none" stroke="#9E9E9E" stroke-width="0.8"/>
    <path d="M180,180 Q185,175 190,180 Q195,185 200,180" fill="none" stroke="#9E9E9E" stroke-width="0.8"/>

    <!-- Sporangiophores (vertical stems) -->
    <line x1="70" y1="180" x2="70" y2="110" stroke="#7B1FA2" stroke-width="2"/>
    <line x1="130" y1="180" x2="130" y2="90" stroke="#7B1FA2" stroke-width="2"/>
    <line x1="190" y1="180" x2="190" y2="120" stroke="#7B1FA2" stroke-width="2"/>

    <!-- Sporangia (round heads) -->
    <circle cx="70" cy="100" r="15" fill="#CE93D8" stroke="#7B1FA2" stroke-width="1.5" opacity="0.8"/>
    <circle cx="70" cy="100" r="10" fill="#E1BEE7" stroke="#9C27B0" stroke-width="0.8"/>
    <text x="70" y="103" font-family="Arial,sans-serif" font-size="6" fill="#4A148C" text-anchor="middle">споры</text>

    <circle cx="130" cy="78" r="18" fill="#CE93D8" stroke="#7B1FA2" stroke-width="1.5" opacity="0.8"/>
    <circle cx="130" cy="78" r="12" fill="#E1BEE7" stroke="#9C27B0" stroke-width="0.8"/>
    <text x="130" y="81" font-family="Arial,sans-serif" font-size="6" fill="#4A148C" text-anchor="middle">спорангий</text>

    <circle cx="190" cy="110" r="14" fill="#CE93D8" stroke="#7B1FA2" stroke-width="1.5" opacity="0.8"/>
    <circle cx="190" cy="110" r="9" fill="#E1BEE7" stroke="#9C27B0" stroke-width="0.8"/>

    <!-- Spores floating -->
    <circle cx="50" cy="60" r="2" fill="#9C27B0" opacity="0.6"/>
    <circle cx="90" cy="50" r="1.5" fill="#9C27B0" opacity="0.5"/>
    <circle cx="160" cy="55" r="2" fill="#9C27B0" opacity="0.6"/>
    <circle cx="210" cy="65" r="1.5" fill="#9C27B0" opacity="0.5"/>
    <circle cx="110" cy="45" r="1.5" fill="#9C27B0" opacity="0.4"/>
    <text x="140" y="155" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Спорангии со спорами</text>
    <text x="140" y="168" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">на ножках-гифах</text>
  </g>

  <!-- Yeast -->
  <g transform="translate(310,75)">
    <rect x="0" y="0" width="275" height="275" rx="8" fill="white" stroke="#558B2F" stroke-width="1.5"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#558B2F" opacity="0.85"/>
    <rect x="0" y="14" width="275" height="10" fill="#558B2F" opacity="0.85"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ДРОЖЖИ</text>

    <!-- Budding yeast cells -->
    <ellipse cx="80" cy="70" rx="18" ry="14" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/>
    <circle cx="78" cy="68" r="5" fill="#FFEE58" stroke="#F57F17" stroke-width="0.8"/>
    <text x="80" y="85" font-family="Arial,sans-serif" font-size="6" fill="#F57F17" text-anchor="middle">почкование</text>

    <!-- Budding cell -->
    <ellipse cx="160" cy="65" rx="18" ry="14" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/>
    <circle cx="158" cy="63" r="5" fill="#FFEE58" stroke="#F57F17" stroke-width="0.8"/>
    <ellipse cx="178" cy="55" rx="10" ry="8" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.2"/>
    <line x1="170" y1="60" x2="174" y2="57" stroke="#F9A825" stroke-width="1"/>

    <!-- Chain of budding -->
    <ellipse cx="80" cy="130" rx="15" ry="12" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.2"/>
    <ellipse cx="95" cy="122" rx="10" ry="8" fill="#FFF9C4" stroke="#F9A825" stroke-width="1"/>
    <ellipse cx="103" cy="115" rx="7" ry="5" fill="#FFF9C4" stroke="#F9A825" stroke-width="0.8"/>

    <!-- Fermentation diagram -->
    <rect x="15" y="160" width="245" height="100" rx="6" fill="#FFF8E1" stroke="#F9A825" stroke-width="1"/>
    <text x="138" y="178" font-family="Arial,sans-serif" font-size="9" fill="#E65100" text-anchor="middle" font-weight="bold">БРОЖЕНИЕ</text>

    <!-- Sugar molecule -->
    <circle cx="60" cy="210" r="12" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
    <text x="60" y="214" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle">C6H12O6</text>
    <text x="60" y="230" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">сахар</text>

    <!-- Arrow -->
    <path d="M85,210 L115,210" stroke="#E65100" stroke-width="2"/>
    <polygon points="115,205 125,210 115,215" fill="#E65100"/>
    <text x="105" y="200" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle">дрожжи</text>

    <!-- Products -->
    <circle cx="160" cy="205" r="10" fill="#FFCDD2" stroke="#C62828" stroke-width="1"/>
    <text x="160" y="209" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle">CO2</text>
    <text x="160" y="225" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">углекислый</text>

    <text x="200" y="209" font-family="Arial,sans-serif" font-size="10" fill="#555">+</text>

    <circle cx="230" cy="205" r="10" fill="#FFF9C4" stroke="#F57F17" stroke-width="1"/>
    <text x="230" y="209" font-family="Arial,sans-serif" font-size="7" fill="#F57F17" text-anchor="middle">C2H5OH</text>
    <text x="230" y="225" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">спирт</text>

    <!-- Bubbles -->
    <circle cx="155" cy="190" r="3" fill="none" stroke="#C62828" stroke-width="0.5" opacity="0.5"/>
    <circle cx="165" cy="185" r="2" fill="none" stroke="#C62828" stroke-width="0.5" opacity="0.4"/>
    <circle cx="150" cy="183" r="2.5" fill="none" stroke="#C62828" stroke-width="0.5" opacity="0.3"/>
  </g>
''' + svg_footer("Плесневые грибы и дрожжи", "#558B2F"))

# ===== LESSON 8: Грибы-паразиты и лишайники =====
write_svg(8, svg_header("Грибы-паразиты и лишайники", "Биология 5 класс - Урок 8", "#FBE9E7", "#FFCCBC", "#BF360C") + '''
  <!-- Parasitic fungi -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="280" height="170" rx="8" fill="white" stroke="#BF360C" stroke-width="1.5"/>
    <rect x="0" y="0" width="280" height="22" rx="8" fill="#BF360C" opacity="0.85"/>
    <rect x="0" y="14" width="280" height="10" fill="#BF360C" opacity="0.85"/>
    <text x="140" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ГРИБЫ-ПАРАЗИТЫ</text>

    <!-- Tree with bracket fungus -->
    <rect x="30" y="60" width="25" height="100" rx="2" fill="#795548" stroke="#4E342E" stroke-width="1.5"/>
    <!-- Bracket fungus on tree -->
    <path d="M55,90 Q70,80 80,90 Q70,100 55,95 Z" fill="#FF8F00" stroke="#E65100" stroke-width="1.5"/>
    <path d="M55,95 Q65,88 75,92" fill="none" stroke="#F9A825" stroke-width="0.8"/>
    <path d="M55,100 Q70,92 80,100 Q70,110 55,105 Z" fill="#FFB74D" stroke="#E65100" stroke-width="1.2"/>
    <text x="75" y="120" font-family="Arial,sans-serif" font-size="7" fill="#E65100">трутовик</text>

    <!-- Wheat with rust fungus -->
    <line x1="180" y1="155" x2="180" y2="70" stroke="#8BC34A" stroke-width="2"/>
    <!-- Wheat head -->
    <ellipse cx="180" cy="65" rx="5" ry="12" fill="#CDDC39" stroke="#827717" stroke-width="1"/>
    <!-- Leaves -->
    <path d="M180,110 Q165,100 155,110" fill="none" stroke="#8BC34A" stroke-width="2"/>
    <path d="M180,130 Q195,120 205,130" fill="none" stroke="#8BC34A" stroke-width="2"/>
    <!-- Rust spots -->
    <circle cx="170" cy="105" r="4" fill="#FF5722" stroke="#BF360C" stroke-width="0.8"/>
    <circle cx="190" cy="125" r="3" fill="#FF5722" stroke="#BF360C" stroke-width="0.8"/>
    <circle cx="175" cy="135" r="3.5" fill="#FF5722" stroke="#BF360C" stroke-width="0.8"/>
    <text x="180" y="168" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle">головня / ржавчина</text>

    <!-- Smut on corn -->
    <line x1="250" y1="155" x2="250" y2="75" stroke="#8BC34A" stroke-width="2"/>
    <ellipse cx="250" cy="70" rx="6" ry="10" fill="#4E342E" stroke="#3E2723" stroke-width="1.5"/>
    <circle cx="250" cy="68" r="6" fill="#37474F" stroke="#263238" stroke-width="1"/>
    <text x="250" y="168" font-family="Arial,sans-serif" font-size="7" fill="#3E2723" text-anchor="middle">головнёвые</text>
  </g>

  <!-- Lichens -->
  <g transform="translate(310,75)">
    <rect x="0" y="0" width="275" height="170" rx="8" fill="white" stroke="#BF360C" stroke-width="1.5"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#BF360C" opacity="0.85"/>
    <rect x="0" y="14" width="275" height="10" fill="#BF360C" opacity="0.85"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ЛИШАЙНИКИ</text>

    <!-- Crustose lichen on rock -->
    <ellipse cx="50" cy="130" rx="30" ry="20" fill="#9E9E9E" stroke="#616161" stroke-width="1.5"/>
    <ellipse cx="50" cy="128" rx="20" ry="12" fill="#C8B560" stroke="#8D6E63" stroke-width="1"/>
    <ellipse cx="45" cy="125" rx="8" ry="5" fill="#D4C070" stroke="#8D6E63" stroke-width="0.5"/>
    <text x="50" y="158" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">накипной</text>

    <!-- Foliose lichen -->
    <path d="M120,110 Q130,95 145,105 Q155,95 160,110 Q155,120 140,118 Q125,120 120,110 Z" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1.5"/>
    <path d="M125,112 Q135,102 142,108" fill="none" stroke="#81C784" stroke-width="0.8"/>
    <path d="M148,108 Q155,100 158,110" fill="none" stroke="#81C784" stroke-width="0.8"/>
    <text x="140" y="132" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">листоватый</text>

    <!-- Fruticose lichen (reindeer moss) -->
    <path d="M220,145 Q218,130 222,120 Q220,110 225,100 Q223,95 226,88" fill="none" stroke="#BDBDBD" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M225,130 Q230,120 228,110 Q232,105 230,95" fill="none" stroke="#BDBDBD" stroke-width="2" stroke-linecap="round"/>
    <path d="M218,125 Q212,118 215,110" fill="none" stroke="#BDBDBD" stroke-width="1.5" stroke-linecap="round"/>
    <path d="M228,118 Q235,110 232,100" fill="none" stroke="#BDBDBD" stroke-width="1.5" stroke-linecap="round"/>
    <text x="225" y="158" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">кустистый</text>
  </g>

  <!-- Symbiosis diagram -->
  <g transform="translate(15,260)">
    <rect x="0" y="0" width="570" height="90" rx="8" fill="white" stroke="#BF360C" stroke-width="1.5"/>
    <text x="285" y="20" font-family="Arial,sans-serif" font-size="11" fill="#BF360C" text-anchor="middle" font-weight="bold">Лишайник = Симбиоз гриба и водоросли</text>
    <line x1="20" y1="28" x2="550" y2="28" stroke="#FFCCBC" stroke-width="1"/>

    <!-- Fungus circle -->
    <circle cx="120" cy="60" r="25" fill="#EFEBE9" stroke="#5D4037" stroke-width="2"/>
    <text x="120" y="56" font-family="Arial,sans-serif" font-size="8" fill="#5D4037" text-anchor="middle" font-weight="bold">Гриб</text>
    <text x="120" y="68" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">Вода, минералы</text>

    <!-- Plus -->
    <text x="175" y="65" font-family="Arial,sans-serif" font-size="16" fill="#BF360C" text-anchor="middle">+</text>

    <!-- Alga circle -->
    <circle cx="230" cy="60" r="25" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/>
    <text x="230" y="56" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Водоросль</text>
    <text x="230" y="68" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">Органические вещества</text>

    <!-- Arrow -->
    <path d="M275,60 L305,60" stroke="#BF360C" stroke-width="2"/>
    <polygon points="305,55 315,60 305,65" fill="#BF360C"/>

    <!-- Lichen result -->
    <circle cx="380" cy="60" r="30" fill="#F1F8E9" stroke="#558B2F" stroke-width="2"/>
    <path d="M365,55 Q375,45 385,55 Q395,45 400,55 Q395,65 380,63 Q365,65 365,55 Z" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
    <text x="380" y="78" font-family="Arial,sans-serif" font-size="8" fill="#558B2F" text-anchor="middle" font-weight="bold">Лишайник</text>

    <!-- Benefits -->
    <text x="470" y="50" font-family="Arial,sans-serif" font-size="8" fill="#555">Впервые поселяются</text>
    <text x="470" y="62" font-family="Arial,sans-serif" font-size="8" fill="#555">на голых скалах</text>
    <text x="470" y="78" font-family="Arial,sans-serif" font-size="8" fill="#555">Индикаторы чистого</text>
    <text x="470" y="90" font-family="Arial,sans-serif" font-size="8" fill="#555">воздуха</text>
  </g>
''' + svg_footer("Грибы-паразиты и лишайники", "#BF360C"))

# ===== LESSON 9: Строение растений =====
write_svg(9, svg_header("Строение растений", "Биология 5 класс - Урок 9") + '''
  <!-- Complete plant diagram -->
  <g transform="translate(150,75)">
    <rect x="0" y="0" width="300" height="275" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
    <rect x="0" y="0" width="300" height="22" rx="8" fill="#2E7D32" opacity="0.85"/>
    <rect x="0" y="14" width="300" height="10" fill="#2E7D32" opacity="0.85"/>
    <text x="150" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ОРГАНЫ РАСТЕНИЯ</text>

    <!-- Flower -->
    <g transform="translate(150,50)">
      <!-- Petals -->
      <ellipse cx="0" cy="-15" rx="8" ry="14" fill="#F48FB1" stroke="#C2185B" stroke-width="1" transform="rotate(0)"/>
      <ellipse cx="0" cy="-15" rx="8" ry="14" fill="#F48FB1" stroke="#C2185B" stroke-width="1" transform="rotate(72)"/>
      <ellipse cx="0" cy="-15" rx="8" ry="14" fill="#F48FB1" stroke="#C2185B" stroke-width="1" transform="rotate(144)"/>
      <ellipse cx="0" cy="-15" rx="8" ry="14" fill="#F48FB1" stroke="#C2185B" stroke-width="1" transform="rotate(216)"/>
      <ellipse cx="0" cy="-15" rx="8" ry="14" fill="#F48FB1" stroke="#C2185B" stroke-width="1" transform="rotate(288)"/>
      <!-- Center -->
      <circle cx="0" cy="0" r="6" fill="#FDD835" stroke="#F9A825" stroke-width="1"/>
    </g>
    <text x="195" y="38" font-family="Arial,sans-serif" font-size="8" fill="#C2185B">цветок</text>
    <line x1="190" y1="40" x2="180" y2="48" stroke="#C2185B" stroke-width="0.8"/>

    <!-- Stem -->
    <rect x="145" y="48" width="10" height="140" rx="2" fill="#81C784" stroke="#2E7D32" stroke-width="1.5"/>
    <text x="170" y="120" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32">стебель</text>
    <line x1="165" y1="118" x2="157" y2="118" stroke="#2E7D32" stroke-width="0.8"/>

    <!-- Leaves -->
    <path d="M145,80 Q120,70 110,80 Q120,90 145,85" fill="#66BB6A" stroke="#2E7D32" stroke-width="1.5"/>
    <line x1="145" y1="82" x2="112" y2="80" stroke="#2E7D32" stroke-width="0.8"/>
    <path d="M155,95 Q180,85 190,95 Q180,105 155,100" fill="#66BB6A" stroke="#2E7D32" stroke-width="1.5"/>
    <line x1="155" y1="97" x2="188" y2="95" stroke="#2E7D32" stroke-width="0.8"/>
    <path d="M145,110 Q120,100 110,110 Q120,120 145,115" fill="#4CAF50" stroke="#2E7D32" stroke-width="1.5"/>
    <text x="95" y="72" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32">листья</text>

    <!-- Fruit -->
    <circle cx="130" cy="55" r="8" fill="#EF5350" stroke="#C62828" stroke-width="1"/>
    <line x1="130" y1="47" x2="130" y2="50" stroke="#2E7D32" stroke-width="1"/>
    <text x="115" y="55" font-family="Arial,sans-serif" font-size="7" fill="#C62828">плод</text>

    <!-- Root system -->
    <line x1="150" y1="188" x2="140" y2="210" stroke="#8D6E63" stroke-width="2"/>
    <line x1="150" y1="188" x2="160" y2="215" stroke="#8D6E63" stroke-width="2"/>
    <line x1="150" y1="188" x2="150" y2="220" stroke="#8D6E63" stroke-width="2.5"/>
    <line x1="140" y1="210" x2="130" y2="225" stroke="#8D6E63" stroke-width="1.5"/>
    <line x1="140" y1="210" x2="135" y2="228" stroke="#8D6E63" stroke-width="1"/>
    <line x1="160" y1="215" x2="170" y2="230" stroke="#8D6E63" stroke-width="1.5"/>
    <line x1="160" y1="215" x2="165" y2="232" stroke="#8D6E63" stroke-width="1"/>
    <line x1="150" y1="220" x2="145" y2="238" stroke="#8D6E63" stroke-width="1.5"/>
    <line x1="150" y1="220" x2="155" y2="240" stroke="#8D6E63" stroke-width="1"/>
    <text x="150" y="250" font-family="Arial,sans-serif" font-size="8" fill="#5D4037" text-anchor="middle">корень</text>

    <!-- Soil line -->
    <line x1="20" y1="188" x2="280" y2="188" stroke="#795548" stroke-width="1" stroke-dasharray="4,3"/>
    <rect x="20" y="188" width="260" height="8" fill="#795548" opacity="0.1"/>
    <text x="260" y="198" font-family="Arial,sans-serif" font-size="7" fill="#795548">почва</text>
  </g>

  <!-- Organs classification -->
  <g transform="translate(15,80)">
    <rect x="0" y="0" width="125" height="130" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
    <text x="63" y="18" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Надземные</text>
    <text x="10" y="38" font-family="Arial,sans-serif" font-size="8" fill="#555">Стебель</text>
    <text x="10" y="53" font-family="Arial,sans-serif" font-size="8" fill="#555">Листья</text>
    <text x="10" y="68" font-family="Arial,sans-serif" font-size="8" fill="#555">Цветок</text>
    <text x="10" y="83" font-family="Arial,sans-serif" font-size="8" fill="#555">Плод</text>
    <text x="10" y="98" font-family="Arial,sans-serif" font-size="8" fill="#555">Семена</text>
    <text x="10" y="118" font-family="Arial,sans-serif" font-size="7" fill="#888">Вегетативные</text>
    <text x="10" y="128" font-family="Arial,sans-serif" font-size="7" fill="#888">и генеративные</text>
  </g>

  <g transform="translate(15,225)">
    <rect x="0" y="0" width="125" height="80" rx="8" fill="white" stroke="#5D4037" stroke-width="1.5"/>
    <text x="63" y="18" font-family="Arial,sans-serif" font-size="9" fill="#5D4037" text-anchor="middle" font-weight="bold">Подземные</text>
    <text x="10" y="38" font-family="Arial,sans-serif" font-size="8" fill="#555">Главный корень</text>
    <text x="10" y="53" font-family="Arial,sans-serif" font-size="8" fill="#555">Боковые корни</text>
    <text x="10" y="68" font-family="Arial,sans-serif" font-size="8" fill="#555">Корневые волоски</text>
  </g>

  <g transform="translate(460,80)">
    <rect x="0" y="0" width="125" height="130" rx="8" fill="white" stroke="#1565C0" stroke-width="1.5"/>
    <text x="63" y="18" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" text-anchor="middle" font-weight="bold">Функции</text>
    <text x="10" y="38" font-family="Arial,sans-serif" font-size="8" fill="#555">Корень: опора,</text>
    <text x="10" y="50" font-family="Arial,sans-serif" font-size="8" fill="#555">вода, минералы</text>
    <text x="10" y="68" font-family="Arial,sans-serif" font-size="8" fill="#555">Стебель: транспорт</text>
    <text x="10" y="80" font-family="Arial,sans-serif" font-size="8" fill="#555">веществ</text>
    <text x="10" y="98" font-family="Arial,sans-serif" font-size="8" fill="#555">Лист: фотосинтез,</text>
    <text x="10" y="110" font-family="Arial,sans-serif" font-size="8" fill="#555">дыхание</text>
    <text x="10" y="128" font-family="Arial,sans-serif" font-size="8" fill="#555">Цветок: размножение</text>
  </g>
''' + svg_footer("Строение растений"))

# Continue with lessons 10-18...
# I'll write them in a second script

print("Grade 5 lessons 1-9 generated!")
