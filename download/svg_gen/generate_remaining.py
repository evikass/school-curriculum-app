#!/usr/bin/env python3
"""Generate detailed biology SVG illustrations for Grades 6-11."""
import os

BASE_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons"

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

def write_svg(grade, subject, num, content):
    d = os.path.join(BASE_DIR, f"grade{grade}", subject)
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, f"lesson{num}.svg")
    with open(path, 'w') as f:
        f.write(content)

counts = {}

#############################
# GRADE 6: Бактерии. Грибы. Растения (23 lessons)
#############################
def gen_grade6():
    grade = 6
    sub = "Бактерии. Грибы. Растения"
    n = 0

    # Lesson 1: Биология - наука о живой природе
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Биология - наука о живой природе", f"Биология {grade} класс - Урок {n}",
        "#E8F5E9", "#C8E6C9", "#2E7D32") + '''
  <!-- Microscope and nature scene -->
  <g transform="translate(30,75)">
    <!-- Tree silhouette -->
    <rect x="10" y="160" width="12" height="50" rx="2" fill="#5D4037"/>
    <ellipse cx="16" cy="130" rx="30" ry="35" fill="#4CAF50" stroke="#2E7D32" stroke-width="1.5"/>
    <ellipse cx="16" cy="110" rx="20" ry="22" fill="#66BB6A"/>
    <!-- Bird -->
    <path d="M50,90 Q55,85 60,88 Q65,85 70,90" fill="none" stroke="#333" stroke-width="1.5"/>
    <path d="M55,92 Q60,87 65,90 Q70,87 75,92" fill="none" stroke="#333" stroke-width="1.2"/>
    <!-- Flower -->
    <line x1="80" y1="210" x2="80" y2="170" stroke="#4CAF50" stroke-width="2"/>
    <circle cx="80" cy="165" r="8" fill="#E91E63" stroke="#C2185B" stroke-width="1"/>
    <circle cx="80" cy="165" r="3" fill="#FFC107"/>
    <ellipse cx="73" cy="162" rx="6" ry="4" fill="#F48FB1" transform="rotate(-30,73,162)"/>
    <ellipse cx="87" cy="162" rx="6" ry="4" fill="#F48FB1" transform="rotate(30,87,162)"/>
    <ellipse cx="75" cy="170" rx="6" ry="4" fill="#F48FB1" transform="rotate(-60,75,170)"/>
    <ellipse cx="85" cy="170" rx="6" ry="4" fill="#F48FB1" transform="rotate(60,85,170)"/>
    <!-- Mushroom -->
    <rect x="110" y="185" width="8" height="25" rx="2" fill="#D7CCC8" stroke="#8D6E63" stroke-width="1"/>
    <ellipse cx="114" cy="185" rx="18" ry="10" fill="#FF8A65" stroke="#E64A19" stroke-width="1.2"/>
    <circle cx="106" cy="182" r="2" fill="white" opacity="0.7"/>
    <circle cx="118" cy="180" r="1.5" fill="white" opacity="0.7"/>
    <circle cx="112" cy="186" r="2" fill="white" opacity="0.7"/>
    <!-- Butterfly -->
    <ellipse cx="55" cy="175" rx="3" ry="6" fill="#795548" stroke="#4E342E" stroke-width="0.8"/>
    <ellipse cx="48" cy="168" rx="8" ry="5" fill="#FF9800" stroke="#E65100" stroke-width="0.8" transform="rotate(-20,48,168)"/>
    <ellipse cx="62" cy="168" rx="8" ry="5" fill="#FF9800" stroke="#E65100" stroke-width="0.8" transform="rotate(20,62,168)"/>
    <ellipse cx="50" cy="176" rx="5" ry="3" fill="#FFB74D" stroke="#E65100" stroke-width="0.6" transform="rotate(-10,50,176)"/>
    <ellipse cx="60" cy="176" rx="5" ry="3" fill="#FFB74D" stroke="#E65100" stroke-width="0.6" transform="rotate(10,60,176)"/>
  </g>
  <!-- Microscope -->
  <g transform="translate(150,80)">
    <rect x="30" y="5" width="22" height="110" rx="3" fill="#546E7A" stroke="#37474F" stroke-width="1.5"/>
    <rect x="20" y="115" width="42" height="8" rx="2" fill="#455A64" stroke="#37474F" stroke-width="1"/>
    <rect x="10" y="123" width="60" height="6" rx="2" fill="#37474F"/>
    <rect x="32" y="-8" width="18" height="16" rx="4" fill="#78909C" stroke="#37474F" stroke-width="1"/>
    <rect x="35" y="82" width="14" height="18" rx="2" fill="#78909C" stroke="#37474F" stroke-width="1"/>
    <rect x="5" y="75" width="65" height="4" rx="1" fill="#607D8B"/>
    <rect x="15" y="72" width="28" height="4" rx="1" fill="#E3F2FD" stroke="#90CAF9" stroke-width="0.5"/>
    <rect x="52" y="35" width="8" height="90" rx="2" fill="#546E7A" stroke="#37474F" stroke-width="1"/>
    <circle cx="60" cy="70" r="7" fill="#607D8B" stroke="#37474F" stroke-width="1"/>
    <circle cx="60" cy="70" r="3" fill="#455A64"/>
    <ellipse cx="40" cy="132" rx="36" ry="5" fill="#455A64" stroke="#37474F" stroke-width="1"/>
    <text x="40" y="155" font-family="Arial,sans-serif" font-size="8" fill="#37474F" text-anchor="middle">Микроскоп</text>
  </g>
  <!-- Info panels -->
  <g transform="translate(310,75)">
    <rect x="0" y="0" width="270" height="130" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="270" height="24" rx="8" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="16" width="270" height="10" fill="#2E7D32" opacity="0.9"/>
    <text x="135" y="17" font-family="Arial,sans-serif" font-size="11" fill="white" text-anchor="middle" font-weight="bold">БИОЛОГИЯ - НАУКА О ЖИЗНИ</text>
    <circle cx="20" cy="46" r="5" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
    <text x="20" y="49" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">1</text>
    <text x="32" y="49" font-family="Arial,sans-serif" font-size="9" fill="#333">Ботаника - наука о растениях</text>
    <circle cx="20" cy="68" r="5" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
    <text x="20" y="71" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">2</text>
    <text x="32" y="71" font-family="Arial,sans-serif" font-size="9" fill="#333">Зоология - наука о животных</text>
    <circle cx="20" cy="90" r="5" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
    <text x="20" y="93" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">3</text>
    <text x="32" y="93" font-family="Arial,sans-serif" font-size="9" fill="#333">Микробиология - бактерии, грибы</text>
    <circle cx="20" cy="112" r="5" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
    <text x="20" y="115" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">4</text>
    <text x="32" y="115" font-family="Arial,sans-serif" font-size="9" fill="#333">Анатомия - строение человека</text>
  </g>
  <!-- Methods panel -->
  <g transform="translate(310,215)">
    <rect x="0" y="0" width="270" height="130" rx="8" fill="white" stroke="#388E3C" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="270" height="24" rx="8" fill="#388E3C" opacity="0.9"/>
    <rect x="0" y="16" width="270" height="10" fill="#388E3C" opacity="0.9"/>
    <text x="135" y="17" font-family="Arial,sans-serif" font-size="11" fill="white" text-anchor="middle" font-weight="bold">МЕТОДЫ БИОЛОГИИ</text>
    <text x="15" y="46" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold">Наблюдение</text>
    <text x="15" y="58" font-family="Arial,sans-serif" font-size="8" fill="#555">Изучение объектов в природе</text>
    <text x="15" y="76" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold">Эксперимент</text>
    <text x="15" y="88" font-family="Arial,sans-serif" font-size="8" fill="#555">Опыт в лабораторных условиях</text>
    <text x="15" y="106" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold">Измерение</text>
    <text x="15" y="118" font-family="Arial,sans-serif" font-size="8" fill="#555">Точные количественные данные</text>
  </g>
''' + svg_footer("Биология - наука о живой природе"))

    # Lesson 2: Признаки живого и уровни организации
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Признаки живого и уровни организации", f"Биология {grade} класс - Урок {n}",
        "#E8F5E9", "#C8E6C9", "#2E7D32") + '''
  <!-- Signs of life -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="280" height="135" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="280" height="22" rx="8" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="16" width="280" height="8" fill="#2E7D32" opacity="0.9"/>
    <text x="140" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ПРИЗНАКИ ЖИВОГО</text>
    <!-- Icons for each sign -->
    <circle cx="28" cy="48" r="10" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
    <text x="28" y="44" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">&#9790;</text>
    <text x="28" y="53" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">D</text>
    <text x="45" y="52" font-family="Arial,sans-serif" font-size="9" fill="#333">Дыхание</text>
    <circle cx="148" cy="48" r="10" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
    <text x="148" y="52" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="bold">P</text>
    <text x="165" y="52" font-family="Arial,sans-serif" font-size="9" fill="#333">Питание</text>
    <circle cx="28" cy="75" r="10" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
    <text x="28" y="79" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="bold">R</text>
    <text x="45" y="79" font-family="Arial,sans-serif" font-size="9" fill="#333">Размножение</text>
    <circle cx="148" cy="75" r="10" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
    <text x="148" y="79" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="bold">G</text>
    <text x="165" y="79" font-family="Arial,sans-serif" font-size="9" fill="#333">Рост</text>
    <circle cx="28" cy="102" r="10" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
    <text x="28" y="106" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="bold">V</text>
    <text x="45" y="106" font-family="Arial,sans-serif" font-size="9" fill="#333">Развитие</text>
    <circle cx="148" cy="102" r="10" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
    <text x="148" y="106" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="bold">I</text>
    <text x="165" y="106" font-family="Arial,sans-serif" font-size="9" fill="#333">Раздражимость</text>
    <text x="140" y="128" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Обмен веществ, выделение, движение</text>
  </g>
  <!-- Levels of organization -->
  <g transform="translate(310,75)">
    <rect x="0" y="0" width="270" height="135" rx="8" fill="white" stroke="#388E3C" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="270" height="22" rx="8" fill="#388E3C" opacity="0.9"/>
    <rect x="0" y="16" width="270" height="8" fill="#388E3C" opacity="0.9"/>
    <text x="135" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">УРОВНИ ОРГАНИЗАЦИИ</text>
    <!-- Pyramid of levels -->
    <polygon points="135,30 165,50 105,50" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
    <text x="135" y="46" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle" font-weight="bold">Биосфера</text>
    <polygon points="95,50 175,50 185,65 85,65" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
    <text x="135" y="60" font-family="Arial,sans-serif" font-size="6" fill="#1B5E20" text-anchor="middle">Биоценоз</text>
    <polygon points="85,65 185,65 195,80 75,80" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
    <text x="135" y="75" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Популяция</text>
    <polygon points="75,80 195,80 205,95 65,95" fill="#DCEDC8" stroke="#558B2F" stroke-width="1"/>
    <text x="135" y="90" font-family="Arial,sans-serif" font-size="6" fill="#558B2F" text-anchor="middle">Организм</text>
    <polygon points="65,95 205,95 215,110 55,110" fill="#F1F8E9" stroke="#558B2F" stroke-width="1"/>
    <text x="135" y="105" font-family="Arial,sans-serif" font-size="6" fill="#558B2F" text-anchor="middle">Орган</text>
    <polygon points="55,110 215,110 225,125 45,125" fill="#FFF9C4" stroke="#F9A825" stroke-width="1"/>
    <text x="135" y="120" font-family="Arial,sans-serif" font-size="6" fill="#F57F17" text-anchor="middle">Ткань</text>
    <polygon points="45,125 225,125 235,135 35,135" fill="#FFECB3" stroke="#FF8F00" stroke-width="1"/>
    <text x="135" y="132" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Клетка - Молекула</text>
  </g>
  <!-- Living cell detail -->
  <g transform="translate(15,220)">
    <rect x="0" y="0" width="570" height="128" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <text x="285" y="20" font-family="Arial,sans-serif" font-size="11" fill="#2E7D32" text-anchor="middle" font-weight="bold">ЖИВОЙ ОРГАНИЗМ - ЕДИНОЕ ЦЕЛОЕ</text>
    <!-- Cat silhouette -->
    <g transform="translate(30,30)">
      <ellipse cx="40" cy="55" rx="30" ry="20" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
      <circle cx="18" cy="40" r="15" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
      <polygon points="8,28 12,38 5,38" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
      <polygon points="25,28 22,38 28,38" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
      <circle cx="13" cy="38" r="2" fill="#333"/>
      <circle cx="22" cy="38" r="2" fill="#333"/>
      <line x1="15" y1="43" x2="20" y2="43" stroke="#E65100" stroke-width="1"/>
      <path d="M70,55 Q80,45 85,55" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
      <!-- Tissue magnification -->
      <line x1="42" y1="50" x2="100" y2="50" stroke="#E65100" stroke-width="0.8" stroke-dasharray="3,2"/>
    </g>
    <!-- Tissue cells -->
    <g transform="translate(155,30)">
      <text x="50" y="10" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle">Ткань (эпителий)</text>
      <rect x="5" y="15" width="22" height="16" rx="2" fill="#FFF3E0" stroke="#E65100" stroke-width="1"/>
      <ellipse cx="16" cy="23" rx="5" ry="4" fill="#FFE0B2" stroke="#BF360C" stroke-width="0.8"/>
      <rect x="27" y="15" width="22" height="16" rx="2" fill="#FFF3E0" stroke="#E65100" stroke-width="1"/>
      <ellipse cx="38" cy="23" rx="5" ry="4" fill="#FFE0B2" stroke="#BF360C" stroke-width="0.8"/>
      <rect x="49" y="15" width="22" height="16" rx="2" fill="#FFF3E0" stroke="#E65100" stroke-width="1"/>
      <ellipse cx="60" cy="23" rx="5" ry="4" fill="#FFE0B2" stroke="#BF360C" stroke-width="0.8"/>
      <rect x="71" y="15" width="22" height="16" rx="2" fill="#FFF3E0" stroke="#E65100" stroke-width="1"/>
      <ellipse cx="82" cy="23" rx="5" ry="4" fill="#FFE0B2" stroke="#BF360C" stroke-width="0.8"/>
      <rect x="16" y="31" width="22" height="16" rx="2" fill="#FFF3E0" stroke="#E65100" stroke-width="1"/>
      <ellipse cx="27" cy="39" rx="5" ry="4" fill="#FFE0B2" stroke="#BF360C" stroke-width="0.8"/>
      <rect x="38" y="31" width="22" height="16" rx="2" fill="#FFF3E0" stroke="#E65100" stroke-width="1"/>
      <ellipse cx="49" cy="39" rx="5" ry="4" fill="#FFE0B2" stroke="#BF360C" stroke-width="0.8"/>
      <rect x="60" y="31" width="22" height="16" rx="2" fill="#FFF3E0" stroke="#E65100" stroke-width="1"/>
      <ellipse cx="71" cy="39" rx="5" ry="4" fill="#FFE0B2" stroke="#BF360C" stroke-width="0.8"/>
    </g>
    <!-- Single cell -->
    <g transform="translate(310,30)">
      <text x="55" y="10" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">Клетка</text>
      <ellipse cx="55" cy="50" rx="40" ry="30" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1.5"/>
      <ellipse cx="55" cy="47" rx="14" ry="10" fill="#81C784" stroke="#1B5E20" stroke-width="1"/>
      <text x="55" y="51" font-family="Arial,sans-serif" font-size="6" fill="#1B5E20" text-anchor="middle">ядро</text>
      <ellipse cx="35" cy="55" rx="8" ry="4" fill="#A5D6A7" stroke="#2E7D32" stroke-width="0.8"/>
      <circle cx="70" cy="40" r="3" fill="#FFCC80" stroke="#E65100" stroke-width="0.5"/>
      <text x="70" y="43" font-family="Arial,sans-serif" font-size="4" fill="#E65100" text-anchor="middle">M</text>
    </g>
    <!-- Organelles -->
    <g transform="translate(430,30)">
      <text x="60" y="10" font-family="Arial,sans-serif" font-size="8" fill="#7B1FA2" text-anchor="middle">Органоиды</text>
      <ellipse cx="30" cy="40" rx="16" ry="7" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
      <path d="M18,40 Q24,35 30,40 Q36,45 42,40" fill="none" stroke="#E65100" stroke-width="0.7"/>
      <text x="30" y="55" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">митохондрия</text>
      <ellipse cx="85" cy="40" rx="14" ry="8" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
      <line x1="73" y1="40" x2="97" y2="40" stroke="#2E7D32" stroke-width="0.5"/>
      <text x="85" y="55" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">хлоропласт</text>
      <circle cx="30" cy="75" r="5" fill="#EF9A9A" stroke="#C62828" stroke-width="0.8"/>
      <circle cx="42" cy="73" r="5" fill="#EF9A9A" stroke="#C62828" stroke-width="0.8"/>
      <text x="36" y="88" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">рибосомы</text>
      <ellipse cx="85" cy="75" rx="15" ry="10" fill="#BBDEFB" stroke="#1565C0" stroke-width="1"/>
      <text x="85" y="79" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">вакуоль</text>
    </g>
  </g>
''' + svg_footer("Признаки живого и уровни организации"))

    # Lesson 3: Строение клетки
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Строение клетки", f"Биология {grade} класс - Урок {n}",
        "#E8F5E9", "#C8E6C9", "#2E7D32") + '''
  <!-- Detailed plant cell -->
  <g transform="translate(20,75)">
    <rect x="0" y="0" width="340" height="275" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="340" height="24" rx="8" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="16" width="340" height="10" fill="#2E7D32" opacity="0.9"/>
    <text x="170" y="17" font-family="Arial,sans-serif" font-size="11" fill="white" text-anchor="middle" font-weight="bold">РАСТИТЕЛЬНАЯ КЛЕТКА</text>
    <!-- Cell wall -->
    <rect x="30" y="35" width="280" height="220" rx="12" fill="none" stroke="#795548" stroke-width="3" stroke-dasharray="8,3"/>
    <text x="315" y="55" font-family="Arial,sans-serif" font-size="7" fill="#795548">клеточная стенка</text>
    <!-- Cell membrane -->
    <rect x="35" y="38" width="270" height="214" rx="10" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/>
    <!-- Cytoplasm label -->
    <text x="55" y="58" font-family="Arial,sans-serif" font-size="9" fill="#558B2F" font-style="italic">цитоплазма</text>
    <!-- Large central vacuole -->
    <rect x="100" y="120" width="180" height="100" rx="15" fill="#BBDEFB" stroke="#1565C0" stroke-width="1.5" opacity="0.7"/>
    <text x="190" y="175" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" text-anchor="middle">вакуоль</text>
    <text x="190" y="188" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle">клеточный сок</text>
    <!-- Nucleus -->
    <ellipse cx="190" cy="80" rx="35" ry="28" fill="#A5D6A7" stroke="#1B5E20" stroke-width="2"/>
    <text x="190" y="78" font-family="Arial,sans-serif" font-size="9" fill="#1B5E20" text-anchor="middle" font-weight="bold">ядро</text>
    <circle cx="195" cy="85" r="8" fill="#66BB6A" stroke="#1B5E20" stroke-width="1"/>
    <text x="195" y="88" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle">ядрышко</text>
    <!-- Nuclear membrane -->
    <ellipse cx="190" cy="80" rx="38" ry="30" fill="none" stroke="#1B5E20" stroke-width="0.8" stroke-dasharray="3,2"/>
    <!-- Chloroplasts -->
    <ellipse cx="60" cy="100" rx="20" ry="10" fill="#81C784" stroke="#2E7D32" stroke-width="1.2"/>
    <line x1="45" y1="100" x2="75" y2="100" stroke="#2E7D32" stroke-width="0.5"/>
    <ellipse cx="60" cy="97" rx="5" ry="3" fill="#4CAF50" opacity="0.5"/>
    <text x="60" y="118" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">хлоропласт</text>
    <ellipse cx="290" cy="90" rx="20" ry="10" fill="#81C784" stroke="#2E7D32" stroke-width="1.2"/>
    <line x1="275" y1="90" x2="305" y2="90" stroke="#2E7D32" stroke-width="0.5"/>
    <ellipse cx="290" cy="87" rx="5" ry="3" fill="#4CAF50" opacity="0.5"/>
    <text x="290" y="108" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">хлоропласт</text>
    <!-- Mitochondria -->
    <ellipse cx="80" cy="160" rx="16" ry="7" fill="#FFCC80" stroke="#E65100" stroke-width="1.2"/>
    <path d="M68,160 Q74,154 80,160 Q86,166 92,160" fill="none" stroke="#E65100" stroke-width="0.8"/>
    <text x="80" y="175" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">митохондрия</text>
    <!-- Ribosomes -->
    <circle cx="55" cy="200" r="3" fill="#EF9A9A" stroke="#C62828" stroke-width="0.8"/>
    <circle cx="62" cy="197" r="3" fill="#EF9A9A" stroke="#C62828" stroke-width="0.8"/>
    <circle cx="52" cy="195" r="3" fill="#EF9A9A" stroke="#C62828" stroke-width="0.8"/>
    <text x="58" y="212" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">рибосомы</text>
    <!-- ER -->
    <path d="M250,140 Q260,135 255,145 Q250,155 260,150 Q270,145 265,155" fill="none" stroke="#7E57C2" stroke-width="1.5"/>
    <text x="268" y="163" font-family="Arial,sans-serif" font-size="6" fill="#7E57C2">ЭПС</text>
    <!-- Golgi -->
    <path d="M120,230 Q135,225 150,230" fill="none" stroke="#FF7043" stroke-width="2"/>
    <path d="M122,235 Q137,230 152,235" fill="none" stroke="#FF7043" stroke-width="1.8"/>
    <path d="M124,240 Q139,235 154,240" fill="none" stroke="#FF7043" stroke-width="1.5"/>
    <text x="138" y="254" font-family="Arial,sans-serif" font-size="6" fill="#FF7043" text-anchor="middle">комплекс Гольджи</text>
    <!-- Plasmodesmata -->
    <line x1="30" y1="150" x2="35" y2="150" stroke="#795548" stroke-width="1.5"/>
    <line x1="30" y1="155" x2="35" y2="155" stroke="#795548" stroke-width="1.5"/>
    <text x="30" y="145" font-family="Arial,sans-serif" font-size="5" fill="#795548">плазмодесмы</text>
  </g>
  <!-- Info panel -->
  <g transform="translate(375,75)">
    <rect x="0" y="0" width="205" height="275" rx="8" fill="white" stroke="#388E3C" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="205" height="24" rx="8" fill="#388E3C" opacity="0.9"/>
    <rect x="0" y="16" width="205" height="10" fill="#388E3C" opacity="0.9"/>
    <text x="103" y="17" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ОРГАНОИДЫ КЛЕТКИ</text>
    <rect x="8" y="34" width="8" height="8" rx="2" fill="#795548"/>
    <text x="22" y="42" font-family="Arial,sans-serif" font-size="8" fill="#795548" font-weight="bold">Клеточная стенка</text>
    <text x="22" y="52" font-family="Arial,sans-serif" font-size="7" fill="#555">Защита и форма (целлюлоза)</text>
    <rect x="8" y="62" width="8" height="8" rx="2" fill="#2E7D32"/>
    <text x="22" y="70" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" font-weight="bold">Мембрана</text>
    <text x="22" y="80" font-family="Arial,sans-serif" font-size="7" fill="#555">Обмен веществ, избирательна</text>
    <rect x="8" y="90" width="8" height="8" rx="2" fill="#1B5E20"/>
    <text x="22" y="98" font-family="Arial,sans-serif" font-size="8" fill="#1B5E20" font-weight="bold">Ядро</text>
    <text x="22" y="108" font-family="Arial,sans-serif" font-size="7" fill="#555">Хранение ДНК, управление</text>
    <rect x="8" y="118" width="8" height="8" rx="2" fill="#1565C0"/>
    <text x="22" y="126" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" font-weight="bold">Вакуоль</text>
    <text x="22" y="136" font-family="Arial,sans-serif" font-size="7" fill="#555">Запас воды и веществ</text>
    <rect x="8" y="146" width="8" height="8" rx="2" fill="#2E7D32"/>
    <text x="22" y="154" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" font-weight="bold">Хлоропласты</text>
    <text x="22" y="164" font-family="Arial,sans-serif" font-size="7" fill="#555">Фотосинтез (хлорофилл)</text>
    <rect x="8" y="174" width="8" height="8" rx="2" fill="#E65100"/>
    <text x="22" y="182" font-family="Arial,sans-serif" font-size="8" fill="#E65100" font-weight="bold">Митохондрии</text>
    <text x="22" y="192" font-family="Arial,sans-serif" font-size="7" fill="#555">Энергия (АТФ)</text>
    <rect x="8" y="202" width="8" height="8" rx="2" fill="#C62828"/>
    <text x="22" y="210" font-family="Arial,sans-serif" font-size="8" fill="#C62828" font-weight="bold">Рибосомы</text>
    <text x="22" y="220" font-family="Arial,sans-serif" font-size="7" fill="#555">Синтез белка</text>
    <rect x="8" y="230" width="8" height="8" rx="2" fill="#7E57C2"/>
    <text x="22" y="238" font-family="Arial,sans-serif" font-size="8" fill="#7E57C2" font-weight="bold">ЭПС</text>
    <text x="22" y="248" font-family="Arial,sans-serif" font-size="7" fill="#555">Транспорт синтез</text>
    <rect x="8" y="258" width="8" height="8" rx="2" fill="#FF7043"/>
    <text x="22" y="266" font-family="Arial,sans-serif" font-size="8" fill="#FF7043" font-weight="bold">Гольджи</text>
  </g>
''' + svg_footer("Строение клетки"))

    # Lesson 4: Химический состав клетки
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Химический состав клетки", f"Биология {grade} класс - Урок {n}",
        "#FFF3E0", "#FFE0B2", "#E65100") + '''
  <!-- Chemical composition pie chart -->
  <g transform="translate(20,75)">
    <rect x="0" y="0" width="260" height="270" rx="8" fill="white" stroke="#E65100" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="260" height="24" rx="8" fill="#E65100" opacity="0.9"/>
    <rect x="0" y="16" width="260" height="10" fill="#E65100" opacity="0.9"/>
    <text x="130" y="17" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">СОСТАВ КЛЕТКИ</text>
    <!-- Pie chart -->
    <circle cx="130" cy="140" r="80" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
    <!-- Water 70-80% -->
    <path d="M130,140 L130,60 A80,80 0 1,1 50,140 Z" fill="#42A5F5" stroke="#1565C0" stroke-width="1"/>
    <text x="90" y="160" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Вода</text>
    <text x="90" y="172" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">70-80%</text>
    <!-- Proteins 10-20% -->
    <path d="M130,140 L50,140 A80,80 0 0,1 80,75 Z" fill="#EF5350" stroke="#C62828" stroke-width="1"/>
    <text x="78" y="118" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">Белки</text>
    <text x="78" y="128" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle">10-20%</text>
    <!-- Lipids 1-5% -->
    <path d="M130,140 L80,75 A80,80 0 0,1 115,62 Z" fill="#FFC107" stroke="#F57F17" stroke-width="1"/>
    <text x="102" y="88" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Липиды</text>
    <!-- Carbs 1% -->
    <path d="M130,140 L115,62 A80,80 0 0,1 130,60 Z" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
    <!-- Nucleic acids -->
    <path d="M130,140 L130,60 A80,80 0 0,1 80,75 Z" fill="#AB47BC" stroke="#6A1B9A" stroke-width="0.5" opacity="0.3"/>
    <!-- Mineral salts -->
    <path d="M210,140 A80,80 0 0,1 130,60 Z" fill="none" stroke="#E65100" stroke-width="0.5"/>
    <text x="180" y="100" font-family="Arial,sans-serif" font-size="7" fill="#6A1B9A" text-anchor="middle">Нуклеиновые</text>
    <text x="180" y="110" font-family="Arial,sans-serif" font-size="7" fill="#6A1B9A" text-anchor="middle">кислоты</text>
    <text x="195" y="125" font-family="Arial,sans-serif" font-size="7" fill="#F57F17" text-anchor="middle">Липиды 1-5%</text>
    <text x="200" y="145" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Углеводы 1%</text>
    <text x="195" y="165" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle">Минеральные соли 1-1.5%</text>
  </g>
  <!-- Molecules -->
  <g transform="translate(295,75)">
    <rect x="0" y="0" width="285" height="270" rx="8" fill="white" stroke="#E65100" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="285" height="24" rx="8" fill="#E65100" opacity="0.9"/>
    <rect x="0" y="16" width="285" height="10" fill="#E65100" opacity="0.9"/>
    <text x="143" y="17" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ОРГАНИЧЕСКИЕ ВЕЩЕСТВА</text>
    <!-- Water molecule H2O -->
    <circle cx="40" cy="52" r="10" fill="#EF5350" stroke="#C62828" stroke-width="1"/>
    <text x="40" y="56" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">O</text>
    <circle cx="28" cy="62" r="6" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
    <text x="28" y="65" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">H</text>
    <circle cx="52" cy="62" r="6" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
    <text x="52" y="65" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">H</text>
    <line x1="34" y1="58" x2="32" y2="60" stroke="#999" stroke-width="1"/>
    <line x1="46" y1="58" x2="48" y2="60" stroke="#999" stroke-width="1"/>
    <text x="40" y="78" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle">H2O</text>
    <!-- Protein chain -->
    <text x="143" y="48" font-family="Arial,sans-serif" font-size="8" fill="#C62828" font-weight="bold">Белок (полипептид)</text>
    <circle cx="85" cy="62" r="7" fill="#EF9A9A" stroke="#C62828" stroke-width="1"/>
    <text x="85" y="65" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">АК</text>
    <line x1="92" y1="62" x2="98" y2="62" stroke="#C62828" stroke-width="1.5"/>
    <circle cx="105" cy="62" r="7" fill="#EF9A9A" stroke="#C62828" stroke-width="1"/>
    <text x="105" y="65" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">АК</text>
    <line x1="112" y1="62" x2="118" y2="62" stroke="#C62828" stroke-width="1.5"/>
    <circle cx="125" cy="62" r="7" fill="#EF9A9A" stroke="#C62828" stroke-width="1"/>
    <text x="125" y="65" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">АК</text>
    <line x1="132" y1="62" x2="138" y2="62" stroke="#C62828" stroke-width="1.5"/>
    <circle cx="145" cy="62" r="7" fill="#EF9A9A" stroke="#C62828" stroke-width="1"/>
    <text x="145" y="65" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">АК</text>
    <line x1="152" y1="62" x2="158" y2="62" stroke="#C62828" stroke-width="1.5"/>
    <circle cx="165" cy="62" r="7" fill="#EF9A9A" stroke="#C62828" stroke-width="1"/>
    <text x="165" y="65" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">АК</text>
    <text x="125" y="80" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">АК = аминокислота (20 видов)</text>
    <!-- Lipid -->
    <text x="143" y="100" font-family="Arial,sans-serif" font-size="8" fill="#F57F17" font-weight="bold">Липид (жир)</text>
    <circle cx="115" cy="118" r="8" fill="#FFC107" stroke="#F57F17" stroke-width="1"/>
    <line x1="115" y1="126" x2="105" y2="140" stroke="#F57F17" stroke-width="1.5"/>
    <line x1="115" y1="126" x2="115" y2="140" stroke="#F57F17" stroke-width="1.5"/>
    <line x1="115" y1="126" x2="125" y2="140" stroke="#F57F17" stroke-width="1.5"/>
    <text x="105" y="150" font-family="Arial,sans-serif" font-size="5" fill="#F57F17" text-anchor="middle">жирн.к.</text>
    <text x="115" y="150" font-family="Arial,sans-serif" font-size="5" fill="#F57F17" text-anchor="middle">жирн.к.</text>
    <text x="125" y="150" font-family="Arial,sans-serif" font-size="5" fill="#F57F17" text-anchor="middle">жирн.к.</text>
    <!-- Glucose -->
    <text x="200" y="100" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" font-weight="bold">Глюкоза C6H12O6</text>
    <polygon points="215,118 230,110 245,118 245,132 230,140 215,132" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1.2"/>
    <text x="230" y="128" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">C6</text>
    <!-- DNA -->
    <text x="143" y="175" font-family="Arial,sans-serif" font-size="8" fill="#6A1B9A" font-weight="bold">ДНК - двойная спираль</text>
    <g transform="translate(80,185)">
      <path d="M0,0 Q15,-8 30,0 Q45,8 60,0 Q75,-8 90,0 Q105,8 120,0" fill="none" stroke="#AB47BC" stroke-width="2"/>
      <path d="M0,10 Q15,18 30,10 Q45,2 60,10 Q75,18 90,10 Q105,2 120,10" fill="none" stroke="#7E57C2" stroke-width="2"/>
      <line x1="15" y1="1" x2="15" y2="9" stroke="#E1BEE7" stroke-width="1"/>
      <line x1="30" y1="0" x2="30" y2="10" stroke="#E1BEE7" stroke-width="1"/>
      <line x1="45" y1="2" x2="45" y2="8" stroke="#E1BEE7" stroke-width="1"/>
      <line x1="60" y1="0" x2="60" y2="10" stroke="#E1BEE7" stroke-width="1"/>
      <line x1="75" y1="1" x2="75" y2="9" stroke="#E1BEE7" stroke-width="1"/>
      <line x1="90" y1="0" x2="90" y2="10" stroke="#E1BEE7" stroke-width="1"/>
      <line x1="105" y1="2" x2="105" y2="8" stroke="#E1BEE7" stroke-width="1"/>
    </g>
    <text x="143" y="215" font-family="Arial,sans-serif" font-size="7" fill="#6A1B9A" text-anchor="middle">А-Т, Г-Ц (комплементарность)</text>
    <!-- ATP -->
    <text x="143" y="240" font-family="Arial,sans-serif" font-size="8" fill="#E65100" font-weight="bold">АТФ - энергия клетки</text>
    <rect x="95" y="248" width="20" height="12" rx="2" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
    <text x="105" y="258" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">А</text>
    <rect x="118" y="248" width="20" height="12" rx="2" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
    <text x="128" y="258" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Р</text>
    <rect x="141" y="248" width="20" height="12" rx="2" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
    <text x="151" y="258" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Р</text>
    <rect x="164" y="248" width="20" height="12" rx="2" fill="#FFCC80" stroke="#E65100" stroke-width="1.5"/>
    <text x="174" y="258" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Р~</text>
    <text x="128" y="246" font-family="Arial,sans-serif" font-size="5" fill="#888">аденозин</text>
    <text x="175" y="246" font-family="Arial,sans-serif" font-size="5" fill="#E65100">макроэрг</text>
  </g>
''' + svg_footer("Химический состав клетки"))

    # Lesson 5: Строение и жизнедеятельность бактерий
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Строение и жизнедеятельность бактерий", f"Биология {grade} класс - Урок {n}",
        "#FFF3E0", "#FFE0B2", "#E65100") + '''
  <!-- Bacteria structure detailed -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="350" height="170" rx="8" fill="white" stroke="#E65100" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="350" height="22" rx="8" fill="#E65100" opacity="0.9"/>
    <rect x="0" y="16" width="350" height="8" fill="#E65100" opacity="0.9"/>
    <text x="175" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">СТРОЕНИЕ БАКТЕРИАЛЬНОЙ КЛЕТКИ</text>
    <!-- Large bacterium -->
    <ellipse cx="160" cy="100" rx="80" ry="40" fill="#FFE0B2" stroke="#E65100" stroke-width="2"/>
    <!-- Capsule -->
    <ellipse cx="160" cy="100" rx="90" ry="48" fill="none" stroke="#FF8F00" stroke-width="2" stroke-dasharray="5,3"/>
    <text x="75" y="60" font-family="Arial,sans-serif" font-size="8" fill="#FF8F00" font-weight="bold">капсула</text>
    <line x1="100" y1="62" x2="110" y2="68" stroke="#FF8F00" stroke-width="0.8"/>
    <!-- Cell wall -->
    <text x="250" y="62" font-family="Arial,sans-serif" font-size="8" fill="#E65100" font-weight="bold">клеточная стенка</text>
    <line x1="248" y1="64" x2="230" y2="72" stroke="#E65100" stroke-width="0.8"/>
    <!-- Cytoplasm -->
    <text x="120" y="100" font-family="Arial,sans-serif" font-size="8" fill="#BF360C" font-style="italic">цитоплазма</text>
    <!-- Nucleoid -->
    <ellipse cx="185" cy="95" rx="25" ry="15" fill="#FFCC80" stroke="#BF360C" stroke-width="1.5" stroke-dasharray="3,2"/>
    <text x="185" y="99" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle">нуклеоид (ДНК)</text>
    <!-- Plasmid -->
    <circle cx="125" cy="85" r="8" fill="none" stroke="#D84315" stroke-width="1.2"/>
    <text x="125" y="73" font-family="Arial,sans-serif" font-size="6" fill="#D84315" text-anchor="middle">плазмида</text>
    <!-- Ribosomes -->
    <circle cx="140" cy="110" r="3" fill="#BF360C"/>
    <circle cx="150" cy="115" r="3" fill="#BF360C"/>
    <circle cx="195" cy="112" r="3" fill="#BF360C"/>
    <circle cx="205" cy="108" r="3" fill="#BF360C"/>
    <text x="210" y="118" font-family="Arial,sans-serif" font-size="6" fill="#888">рибосомы</text>
    <!-- Flagellum -->
    <path d="M240,100 Q250,93 255,100 Q260,107 265,100 Q270,93 275,100 Q280,107 285,100" fill="none" stroke="#E65100" stroke-width="2"/>
    <text x="270" y="88" font-family="Arial,sans-serif" font-size="7" fill="#E65100">жгутик</text>
    <!-- Pili -->
    <line x1="100" y1="80" x2="82" y2="68" stroke="#BF360C" stroke-width="1"/>
    <line x1="95" y1="100" x2="78" y2="100" stroke="#BF360C" stroke-width="1"/>
    <line x1="100" y1="120" x2="82" y2="130" stroke="#BF360C" stroke-width="1"/>
    <text x="65" y="138" font-family="Arial,sans-serif" font-size="6" fill="#888">пили (ворсинки)</text>
    <!-- Mesosome -->
    <path d="M220,110 Q225,105 230,110 Q235,115 240,110" fill="none" stroke="#D84315" stroke-width="1.5"/>
    <text x="240" y="125" font-family="Arial,sans-serif" font-size="6" fill="#D84315">мезосома</text>
  </g>
  <!-- Bacteria shapes and reproduction -->
  <g transform="translate(380,75)">
    <rect x="0" y="0" width="200" height="170" rx="8" fill="white" stroke="#E65100" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="200" height="22" rx="8" fill="#E65100" opacity="0.9"/>
    <rect x="0" y="16" width="200" height="8" fill="#E65100" opacity="0.9"/>
    <text x="100" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ФОРМЫ БАКТЕРИЙ</text>
    <!-- Cocci -->
    <circle cx="40" cy="45" r="10" fill="#FFE0B2" stroke="#E65100" stroke-width="1.2"/>
    <circle cx="58" cy="45" r="10" fill="#FFE0B2" stroke="#E65100" stroke-width="1.2"/>
    <text x="49" y="62" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">кокки</text>
    <!-- Bacilli -->
    <rect x="100" y="37" width="30" height="14" rx="7" fill="#FFCC80" stroke="#E65100" stroke-width="1.2"/>
    <rect x="140" y="37" width="30" height="14" rx="7" fill="#FFCC80" stroke="#E65100" stroke-width="1.2"/>
    <text x="135" y="62" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">бациллы</text>
    <!-- Spirillum -->
    <path d="M30,80 Q40,72 50,80 Q60,88 70,80" fill="none" stroke="#E65100" stroke-width="2.5"/>
    <text x="50" y="98" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">спирилла</text>
    <!-- Vibrio -->
    <path d="M110,80 Q125,70 130,82" fill="none" stroke="#E65100" stroke-width="3" stroke-linecap="round"/>
    <text x="120" y="98" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">вибрион</text>
    <!-- Spore -->
    <ellipse cx="50" cy="125" rx="18" ry="12" fill="#FFCC80" stroke="#E65100" stroke-width="1.2"/>
    <ellipse cx="50" cy="125" rx="8" ry="7" fill="#FFE0B2" stroke="#BF360C" stroke-width="1"/>
    <text x="50" y="146" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">спора</text>
    <!-- Binary fission -->
    <ellipse cx="140" cy="118" rx="12" ry="9" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
    <line x1="152" y1="109" x2="152" y2="127" stroke="#E65100" stroke-width="1.5" stroke-dasharray="2,1"/>
    <ellipse cx="168" cy="118" rx="12" ry="9" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
    <text x="155" y="146" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">деление надвое</text>
    <!-- Arrows showing division -->
    <path d="M155,155 L155,160" stroke="#E65100" stroke-width="1"/>
  </g>
  <!-- Nutrition types -->
  <g transform="translate(15,260)">
    <rect x="0" y="0" width="570" height="88" rx="8" fill="white" stroke="#E65100" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="570" height="22" rx="8" fill="#BF360C" opacity="0.9"/>
    <rect x="0" y="16" width="570" height="8" fill="#BF360C" opacity="0.9"/>
    <text x="285" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ПИТАНИЕ БАКТЕРИЙ</text>
    <rect x="10" y="32" width="130" height="46" rx="5" fill="#FFF3E0" stroke="#E65100" stroke-width="1"/>
    <text x="75" y="48" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">Автотрофы</text>
    <text x="75" y="60" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Сами создают</text>
    <text x="75" y="70" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">органические вещества</text>
    <rect x="150" y="32" width="130" height="46" rx="5" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
    <text x="215" y="48" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">Гетеротрофы</text>
    <text x="215" y="60" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Потребляют готовые</text>
    <text x="215" y="70" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">органические вещества</text>
    <rect x="290" y="32" width="130" height="46" rx="5" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
    <text x="355" y="48" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">Сапротрофы</text>
    <text x="355" y="60" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Питаются мёртвыми</text>
    <text x="355" y="70" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">остатками</text>
    <rect x="430" y="32" width="130" height="46" rx="5" fill="#FFB74D" stroke="#E65100" stroke-width="1"/>
    <text x="495" y="48" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">Паразиты</text>
    <text x="495" y="60" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">За счёт живых</text>
    <text x="495" y="70" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">организмов</text>
  </g>
''' + svg_footer("Строение и жизнедеятельность бактерий"))

    counts[grade] = n
    print(f"Grade {grade}: {n} SVGs generated")


    # Lesson 6: Роль бактерий в природе и жизни человека
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Роль бактерий в природе и жизни человека", f"Биология {grade} класс - Урок {n}",
        "#E8F5E9", "#C8E6C9", "#2E7D32") + '''
  <!-- Beneficial bacteria -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="280" height="130" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="280" height="22" rx="8" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="16" width="280" height="8" fill="#2E7D32" opacity="0.9"/>
    <text x="140" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ПОЛЕЗНЫЕ БАКТЕРИИ</text>
    <!-- Nitrogen fixation -->
    <g transform="translate(10,30)">
      <line x1="20" y1="55" x2="20" y2="30" stroke="#795548" stroke-width="2"/>
      <ellipse cx="20" cy="25" rx="8" ry="5" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
      <circle cx="20" cy="60" r="5" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
      <circle cx="15" cy="65" r="4" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
      <circle cx="25" cy="65" r="4" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
      <text x="20" y="80" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Клубеньковые</text>
      <text x="20" y="88" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">бактерии</text>
    </g>
    <!-- Fermentation -->
    <g transform="translate(60,30)">
      <rect x="5" y="25" width="16" height="25" rx="3" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
      <rect x="5" y="20" width="16" height="8" rx="2" fill="#BBDEFB" stroke="#1565C0" stroke-width="1"/>
      <circle cx="10" cy="35" r="2" fill="#FFE0B2" stroke="#E65100" stroke-width="0.5"/>
      <circle cx="16" cy="38" r="2" fill="#FFE0B2" stroke="#E65100" stroke-width="0.5"/>
      <text x="13" y="62" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">Молочнокислые</text>
      <text x="13" y="70" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">бактерии</text>
    </g>
    <!-- Soil bacteria -->
    <g transform="translate(110,30)">
      <rect x="0" y="30" width="50" height="30" rx="3" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
      <rect x="0" y="25" width="50" height="10" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
      <circle cx="15" cy="38" r="3" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
      <circle cx="30" cy="42" r="3" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
      <circle cx="40" cy="36" r="2" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
      <text x="25" y="72" font-family="Arial,sans-serif" font-size="6" fill="#5D4037" text-anchor="middle">Почвенные</text>
      <text x="25" y="80" font-family="Arial,sans-serif" font-size="6" fill="#5D4037" text-anchor="middle">бактерии</text>
    </g>
    <!-- Decomposition -->
    <g transform="translate(175,30)">
      <rect x="0" y="30" width="50" height="25" rx="2" fill="#8D6E63"/>
      <path d="M5,30 L15,25 L25,30 L35,22 L45,30" fill="#A5D6A7" stroke="#2E7D32" stroke-width="0.8"/>
      <circle cx="20" cy="42" r="3" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
      <circle cx="35" cy="45" r="2" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
      <text x="25" y="67" font-family="Arial,sans-serif" font-size="6" fill="#5D4037" text-anchor="middle">Гниение</text>
      <text x="25" y="75" font-family="Arial,sans-serif" font-size="6" fill="#5D4037" text-anchor="middle">(редуценты)</text>
    </g>
    <!-- Intestinal flora -->
    <g transform="translate(235,30)">
      <ellipse cx="20" cy="35" rx="18" ry="12" fill="#FFCDD2" stroke="#E57373" stroke-width="1.5"/>
      <circle cx="12" cy="33" r="3" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
      <circle cx="20" cy="38" r="3" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
      <circle cx="28" cy="33" r="3" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
      <text x="20" y="58" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">Кишечная</text>
      <text x="20" y="66" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">микрофлора</text>
    </g>
  </g>
  <!-- Harmful bacteria -->
  <g transform="translate(310,75)">
    <rect x="0" y="0" width="275" height="130" rx="8" fill="white" stroke="#C62828" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#C62828" opacity="0.9"/>
    <rect x="0" y="16" width="275" height="8" fill="#C62828" opacity="0.9"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ВРЕДНЫЕ БАКТЕРИИ</text>
    <!-- Pathogenic bacteria -->
    <circle cx="40" cy="50" r="12" fill="#FFCDD2" stroke="#C62828" stroke-width="1.5"/>
    <line x1="35" y1="50" x2="45" y2="50" stroke="#C62828" stroke-width="1"/>
    <line x1="40" y1="45" x2="40" y2="55" stroke="#C62828" stroke-width="1"/>
    <text x="40" y="70" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">Стрептококк</text>
    <!-- Tetanus -->
    <rect x="85" y="42" width="25" height="12" rx="6" fill="#FFCDD2" stroke="#C62828" stroke-width="1"/>
    <circle cx="82" cy="48" r="5" fill="#FFCDD2" stroke="#C62828" stroke-width="1"/>
    <text x="95" y="65" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">Столбняк</text>
    <!-- Tuberculosis -->
    <rect x="135" y="43" width="20" height="10" rx="5" fill="#FFCDD2" stroke="#C62828" stroke-width="1"/>
    <rect x="158" y="43" width="20" height="10" rx="5" fill="#FFCDD2" stroke="#C62828" stroke-width="1"/>
    <text x="155" y="65" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">Туберкулёз</text>
    <!-- Cholera -->
    <path d="M210,48 Q220,38 225,50" fill="none" stroke="#C62828" stroke-width="2.5"/>
    <text x="218" y="65" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">Холера</text>
    <!-- Prevention -->
    <rect x="10" y="80" width="255" height="40" rx="5" fill="#FFEBEE" stroke="#C62828" stroke-width="1"/>
    <text x="138" y="96" font-family="Arial,sans-serif" font-size="9" fill="#C62828" text-anchor="middle" font-weight="bold">Борьба с бактериями</text>
    <text x="138" y="112" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Антибиотики, вакцины, пастеризация, стерилизация, гигиена</text>
  </g>
  <!-- Role summary -->
  <g transform="translate(15,218)">
    <rect x="0" y="0" width="570" height="130" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <text x="285" y="20" font-family="Arial,sans-serif" font-size="11" fill="#2E7D32" text-anchor="middle" font-weight="bold">КРУГОВОРОТ ВЕЩЕСТВ В ПРИРОДЕ</text>
    <!-- Cycle diagram -->
    <g transform="translate(140,30)">
      <!-- Sun -->
      <circle cx="150" cy="20" r="15" fill="#FFC107" stroke="#F57F17" stroke-width="1.5"/>
      <line x1="150" y1="3" x2="150" y2="-2" stroke="#FFC107" stroke-width="1.5"/>
      <line x1="165" y1="10" x2="170" y2="6" stroke="#FFC107" stroke-width="1.5"/>
      <line x1="170" y1="20" x2="175" y2="20" stroke="#FFC107" stroke-width="1.5"/>
      <line x1="135" y1="10" x2="130" y2="6" stroke="#FFC107" stroke-width="1.5"/>
      <!-- Plant -->
      <rect x="135" y="45" width="8" height="20" fill="#4CAF50"/>
      <ellipse cx="139" cy="40" rx="15" ry="12" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
      <text x="139" y="75" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Растения</text>
      <!-- Arrow plant to animal -->
      <path d="M155,55 L190,55" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
      <polygon points="188,52 194,55 188,58" fill="#2E7D32"/>
      <!-- Animal -->
      <ellipse cx="220" cy="50" rx="20" ry="12" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
      <circle cx="208" cy="42" r="8" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
      <text x="220" y="72" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle">Животные</text>
      <!-- Arrow animal to bacteria -->
      <path d="M220,65 L220,85" stroke="#E65100" stroke-width="1.5" fill="none"/>
      <polygon points="217,83 220,89 223,83" fill="#E65100"/>
      <!-- Dead matter -->
      <rect x="200" y="90" width="40" height="15" rx="3" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
      <text x="220" y="100" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle">Отходы</text>
      <!-- Arrow to bacteria -->
      <path d="M200,98 L130,80" stroke="#5D4037" stroke-width="1.5" fill="none"/>
      <polygon points="132,78 126,78 130,84" fill="#5D4037"/>
      <!-- Bacteria -->
      <circle cx="100" cy="85" r="8" fill="#FFE0B2" stroke="#E65100" stroke-width="1.2"/>
      <circle cx="112" cy="82" r="6" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
      <text x="100" y="100" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle">Бактерии</text>
      <!-- Arrow bacteria to minerals -->
      <path d="M92,90 L60,80" stroke="#E65100" stroke-width="1.5" fill="none"/>
      <polygon points="62,78 56,78 60,84" fill="#E65100"/>
      <!-- Minerals in soil -->
      <rect x="20" y="70" width="50" height="20" rx="3" fill="#A1887F" stroke="#5D4037" stroke-width="1"/>
      <text x="45" y="83" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle">Минералы</text>
      <!-- Arrow minerals to plant -->
      <path d="M70,75 L125,55" stroke="#5D4037" stroke-width="1.5" fill="none"/>
      <polygon points="123,53 127,52 124,58" fill="#5D4037"/>
    </g>
  </g>
''' + svg_footer("Роль бактерий в природе и жизни человека"))

    # Lesson 7: Общая характеристика грибов
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Общая характеристика грибов", f"Биология {grade} класс - Урок {n}",
        "#FFF3E0", "#FFE0B2", "#795548") + '''
  <!-- Mushroom structure -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="280" height="270" rx="8" fill="white" stroke="#795548" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="280" height="22" rx="8" fill="#795548" opacity="0.9"/>
    <rect x="0" y="16" width="280" height="8" fill="#795548" opacity="0.9"/>
    <text x="140" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">СТРОЕНИЕ ГРИБА</text>
    <!-- Full mushroom -->
    <ellipse cx="140" cy="75" rx="55" ry="30" fill="#FF8A65" stroke="#E64A19" stroke-width="2"/>
    <!-- Spots on cap -->
    <circle cx="120" cy="68" r="5" fill="white" opacity="0.7"/>
    <circle cx="150" cy="72" r="4" fill="white" opacity="0.7"/>
    <circle cx="135" cy="80" r="3" fill="white" opacity="0.6"/>
    <text x="220" y="72" font-family="Arial,sans-serif" font-size="7" fill="#E64A19">шляпка</text>
    <line x1="195" y1="72" x2="185" y2="72" stroke="#E64A19" stroke-width="0.8"/>
    <!-- Stem -->
    <rect x="130" y="105" width="20" height="65" rx="4" fill="#FFECB3" stroke="#FF8F00" stroke-width="1.5"/>
    <text x="170" y="140" font-family="Arial,sans-serif" font-size="7" fill="#FF8F00">ножка</text>
    <line x1="150" y1="138" x2="155" y2="138" stroke="#FF8F00" stroke-width="0.8"/>
    <!-- Ring on stem -->
    <ellipse cx="140" cy="120" rx="14" ry="3" fill="none" stroke="#FF8F00" stroke-width="1"/>
    <text x="170" y="120" font-family="Arial,sans-serif" font-size="6" fill="#FF8F00">кольцо</text>
    <!-- Mycelium -->
    <line x1="120" y1="170" x2="100" y2="195" stroke="#A1887F" stroke-width="1.5"/>
    <line x1="100" y1="195" x2="80" y2="210" stroke="#A1887F" stroke-width="1"/>
    <line x1="100" y1="195" x2="95" y2="215" stroke="#A1887F" stroke-width="1"/>
    <line x1="140" y1="170" x2="140" y2="200" stroke="#A1887F" stroke-width="1.5"/>
    <line x1="140" y1="200" x2="125" y2="218" stroke="#A1887F" stroke-width="1"/>
    <line x1="140" y1="200" x2="155" y2="218" stroke="#A1887F" stroke-width="1"/>
    <line x1="155" y1="170" x2="175" y2="195" stroke="#A1887F" stroke-width="1.5"/>
    <line x1="175" y1="195" x2="190" y2="210" stroke="#A1887F" stroke-width="1"/>
    <line x1="175" y1="195" x2="185" y2="218" stroke="#A1887F" stroke-width="1"/>
    <text x="140" y="235" font-family="Arial,sans-serif" font-size="8" fill="#795548" text-anchor="middle" font-weight="bold">Грибница (мицелий)</text>
    <!-- Soil line -->
    <line x1="20" y1="170" x2="260" y2="170" stroke="#8D6E63" stroke-width="1.5" stroke-dasharray="5,3"/>
    <text x="240" y="168" font-family="Arial,sans-serif" font-size="6" fill="#8D6E63">почва</text>
    <!-- Hyphae detail -->
    <rect x="15" y="245" width="120" height="20" rx="3" fill="#EFEBE9" stroke="#A1887F" stroke-width="1"/>
    <line x1="20" y1="255" x2="40" y2="255" stroke="#8D6E63" stroke-width="1.5"/>
    <line x1="40" y1="255" x2="55" y2="252" stroke="#8D6E63" stroke-width="1.5"/>
    <line x1="55" y1="252" x2="70" y2="258" stroke="#8D6E63" stroke-width="1.5"/>
    <line x1="70" y1="258" x2="90" y2="255" stroke="#8D6E63" stroke-width="1.5"/>
    <line x1="90" y1="255" x2="110" y2="252" stroke="#8D6E63" stroke-width="1.5"/>
    <text x="155" y="258" font-family="Arial,sans-serif" font-size="7" fill="#8D6E63">гифы</text>
  </g>
  <!-- Fungal cell and reproduction -->
  <g transform="translate(310,75)">
    <rect x="0" y="0" width="275" height="130" rx="8" fill="white" stroke="#795548" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#795548" opacity="0.9"/>
    <rect x="0" y="16" width="275" height="8" fill="#795548" opacity="0.9"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">КЛЕТКА ГРИБА</text>
    <!-- Fungal cell -->
    <ellipse cx="80" cy="72" rx="45" ry="30" fill="#EFEBE9" stroke="#795548" stroke-width="1.5"/>
    <!-- Cell wall -->
    <text x="80" y="48" font-family="Arial,sans-serif" font-size="6" fill="#795548" text-anchor="middle">хитиновая стенка</text>
    <!-- Nucleus -->
    <ellipse cx="75" cy="68" rx="12" ry="8" fill="#BCAAA4" stroke="#5D4037" stroke-width="1.2"/>
    <text x="75" y="72" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle">ядро</text>
    <!-- Vacuole -->
    <ellipse cx="100" cy="75" rx="10" ry="7" fill="#BBDEFB" stroke="#1565C0" stroke-width="0.8"/>
    <!-- Mitochondria -->
    <ellipse cx="60" cy="78" rx="10" ry="4" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
    <!-- Ribosomes -->
    <circle cx="90" cy="62" r="2" fill="#795548"/>
    <circle cx="95" cy="65" r="2" fill="#795548"/>
    <!-- Spores -->
    <text x="200" y="40" font-family="Arial,sans-serif" font-size="8" fill="#795548" font-weight="bold">Споры гриба</text>
    <circle cx="185" cy="55" r="5" fill="#FFECB3" stroke="#FF8F00" stroke-width="0.8"/>
    <circle cx="200" cy="50" r="5" fill="#FFECB3" stroke="#FF8F00" stroke-width="0.8"/>
    <circle cx="215" cy="55" r="5" fill="#FFECB3" stroke="#FF8F00" stroke-width="0.8"/>
    <circle cx="195" cy="68" r="5" fill="#FFECB3" stroke="#FF8F00" stroke-width="0.8"/>
    <circle cx="210" cy="65" r="5" fill="#FFECB3" stroke="#FF8F00" stroke-width="0.8"/>
    <text x="200" y="82" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">размножение спорами</text>
  </g>
  <!-- Features of fungi -->
  <g transform="translate(310,215)">
    <rect x="0" y="0" width="275" height="130" rx="8" fill="white" stroke="#795548" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#5D4037" opacity="0.9"/>
    <rect x="0" y="16" width="275" height="8" fill="#5D4037" opacity="0.9"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ПРИЗНАКИ ГРИБОВ</text>
    <text x="15" y="42" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" font-weight="bold">Как растения:</text>
    <text x="15" y="54" font-family="Arial,sans-serif" font-size="7" fill="#555">неподвижны, растут всю жизнь</text>
    <text x="15" y="66" font-family="Arial,sans-serif" font-size="7" fill="#555">клеточная стенка, запас гликоген</text>
    <text x="15" y="82" font-family="Arial,sans-serif" font-size="8" fill="#E65100" font-weight="bold">Как животные:</text>
    <text x="15" y="94" font-family="Arial,sans-serif" font-size="7" fill="#555">гетеротрофы (не фотосинтез)</text>
    <text x="15" y="106" font-family="Arial,sans-serif" font-size="7" fill="#555">хитин в клеточной стенке</text>
    <text x="15" y="118" font-family="Arial,sans-serif" font-size="7" fill="#555">запасной углевод - гликоген</text>
  </g>
''' + svg_footer("Общая характеристика грибов"))

    # Lesson 8: Многообразие и значение грибов
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Многообразие и значение грибов", f"Биология {grade} класс - Урок {n}",
        "#FFF3E0", "#FFE0B2", "#795548") + '''
  <!-- Different mushroom types -->
  <g transform="translate(15,75)">
    <!-- Shelf mushrooms -->
    <rect x="0" y="0" width="180" height="130" rx="8" fill="white" stroke="#795548" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="180" height="22" rx="8" fill="#795548" opacity="0.9"/>
    <rect x="0" y="16" width="180" height="8" fill="#795548" opacity="0.9"/>
    <text x="90" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ТРУТОВИК</text>
    <!-- Tree trunk -->
    <rect x="10" y="70" width="25" height="50" rx="2" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
    <!-- Shelf fungus -->
    <ellipse cx="55" cy="78" rx="30" ry="15" fill="#FF8A65" stroke="#E64A19" stroke-width="1.5"/>
    <rect x="25" y="78" width="60" height="5" rx="2" fill="#D84315"/>
    <ellipse cx="55" cy="83" rx="28" ry="8" fill="#FFECB3" stroke="#FF8F00" stroke-width="1"/>
    <text x="90" y="110" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Паразит деревьев</text>
  </g>
  <!-- Mould -->
  <g transform="translate(205,75)">
    <rect x="0" y="0" width="180" height="130" rx="8" fill="white" stroke="#795548" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="180" height="22" rx="8" fill="#795548" opacity="0.9"/>
    <rect x="0" y="16" width="180" height="8" fill="#795548" opacity="0.9"/>
    <text x="90" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ПЛЕСНЕВЫЕ ГРИБЫ</text>
    <!-- Bread -->
    <rect x="20" y="60" width="60" height="30" rx="5" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
    <!-- Mould spots -->
    <circle cx="35" cy="68" r="6" fill="#4CAF50" opacity="0.6" stroke="#2E7D32" stroke-width="0.5"/>
    <circle cx="55" cy="72" r="8" fill="#66BB6A" opacity="0.5" stroke="#2E7D32" stroke-width="0.5"/>
    <circle cx="45" cy="80" r="5" fill="#81C784" opacity="0.5" stroke="#2E7D32" stroke-width="0.5"/>
    <!-- Mucor -->
    <line x1="100" y1="90" x2="100" y2="55" stroke="#9E9E9E" stroke-width="1.5"/>
    <ellipse cx="100" cy="52" rx="8" ry="6" fill="#90A4AE" stroke="#607D8B" stroke-width="1"/>
    <circle cx="100" cy="48" r="3" fill="#B0BEC5" stroke="#607D8B" stroke-width="0.8"/>
    <line x1="120" y1="90" x2="120" y2="60" stroke="#9E9E9E" stroke-width="1.5"/>
    <ellipse cx="120" cy="57" rx="7" ry="5" fill="#90A4AE" stroke="#607D8B" stroke-width="1"/>
    <text x="110" y="105" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Мукор / Пеницилл</text>
  </g>
  <!-- Yeast -->
  <g transform="translate(395,75)">
    <rect x="0" y="0" width="190" height="130" rx="8" fill="white" stroke="#795548" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="190" height="22" rx="8" fill="#795548" opacity="0.9"/>
    <rect x="0" y="16" width="190" height="8" fill="#795548" opacity="0.9"/>
    <text x="95" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ДРОЖЖИ</text>
    <!-- Budding yeast -->
    <ellipse cx="60" cy="60" rx="12" ry="9" fill="#FFECB3" stroke="#FF8F00" stroke-width="1.2"/>
    <ellipse cx="75" cy="55" rx="8" ry="6" fill="#FFECB3" stroke="#FF8F00" stroke-width="1"/>
    <ellipse cx="120" cy="70" rx="12" ry="9" fill="#FFECB3" stroke="#FF8F00" stroke-width="1.2"/>
    <ellipse cx="133" cy="65" rx="8" ry="6" fill="#FFECB3" stroke="#FF8F00" stroke-width="1"/>
    <ellipse cx="50" cy="90" rx="10" ry="8" fill="#FFECB3" stroke="#FF8F00" stroke-width="1"/>
    <text x="95" y="108" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Почкование</text>
    <text x="95" y="120" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Спиртовое брожение</text>
  </g>
  <!-- Edible vs Poisonous -->
  <g transform="translate(15,218)">
    <rect x="0" y="0" width="570" height="130" rx="8" fill="white" stroke="#795548" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="570" height="22" rx="8" fill="#4E342E" opacity="0.9"/>
    <rect x="0" y="16" width="570" height="8" fill="#4E342E" opacity="0.9"/>
    <text x="285" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">СЪЕДОБНЫЕ И ЯДОВИТЫЕ ГРИБЫ</text>
    <!-- Edible -->
    <g transform="translate(20,30)">
      <rect x="0" y="30" width="8" height="20" rx="2" fill="#FFECB3" stroke="#FF8F00" stroke-width="1"/>
      <ellipse cx="4" cy="30" rx="18" ry="12" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
      <text x="4" y="65" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Белый</text>
    </g>
    <g transform="translate(65,30)">
      <rect x="0" y="30" width="8" height="20" rx="2" fill="#FFECB3" stroke="#FF8F00" stroke-width="1"/>
      <ellipse cx="4" cy="30" rx="18" ry="12" fill="#FF8A65" stroke="#E64A19" stroke-width="1"/>
      <text x="4" y="65" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Подосиновик</text>
    </g>
    <g transform="translate(110,30)">
      <rect x="0" y="28" width="8" height="22" rx="2" fill="#FFECB3" stroke="#FF8F00" stroke-width="1"/>
      <ellipse cx="4" cy="28" rx="16" ry="10" fill="#A1887F" stroke="#795548" stroke-width="1"/>
      <ellipse cx="4" cy="20" rx="12" ry="8" fill="#A1887F" stroke="#795548" stroke-width="1"/>
      <text x="4" y="65" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Лисичка</text>
    </g>
    <!-- Divider -->
    <line x1="285" y1="30" x2="285" y2="125" stroke="#C62828" stroke-width="2" stroke-dasharray="5,3"/>
    <text x="285" y="125" font-family="Arial,sans-serif" font-size="8" fill="#C62828" text-anchor="middle" font-weight="bold">НЕ СОБИРАЙ!</text>
    <!-- Poisonous -->
    <g transform="translate(310,30)">
      <rect x="0" y="30" width="8" height="18" rx="2" fill="#FFECB3" stroke="#FF8F00" stroke-width="1"/>
      <ellipse cx="4" cy="30" rx="20" ry="14" fill="#EF5350" stroke="#C62828" stroke-width="1.5"/>
      <circle cx="-5" cy="24" r="3" fill="white" opacity="0.8"/>
      <circle cx="10" cy="26" r="2.5" fill="white" opacity="0.8"/>
      <circle cx="4" cy="35" r="2" fill="white" opacity="0.7"/>
      <text x="4" y="62" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">Мухомор</text>
    </g>
    <g transform="translate(370,30)">
      <rect x="0" y="30" width="8" height="16" rx="2" fill="#FFECB3" stroke="#FF8F00" stroke-width="1"/>
      <ellipse cx="4" cy="30" rx="18" ry="12" fill="#81C784" stroke="#2E7D32" stroke-width="1.5"/>
      <text x="4" y="58" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">Бледная</text>
      <text x="4" y="66" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">поганка</text>
    </g>
    <g transform="translate(430,30)">
      <rect x="0" y="30" width="8" height="14" rx="2" fill="#FFECB3" stroke="#FF8F00" stroke-width="1"/>
      <ellipse cx="4" cy="30" rx="14" ry="10" fill="#CE93D8" stroke="#7B1FA2" stroke-width="1.5"/>
      <text x="4" y="58" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">Сатанинский</text>
    </g>
    <!-- Lichen -->
    <g transform="translate(490,25)">
      <text x="45" y="10" font-family="Arial,sans-serif" font-size="8" fill="#795548" font-weight="bold">Лишайник</text>
      <ellipse cx="45" cy="45" rx="30" ry="18" fill="#C8E6C9" stroke="#558B2F" stroke-width="1"/>
      <circle cx="35" cy="42" r="4" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>
      <circle cx="50" cy="45" r="3" fill="#A5D6A7" stroke="#558B2F" stroke-width="0.8"/>
      <text x="45" y="72" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Гриб + Водоросль</text>
      <text x="45" y="82" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Симбиоз</text>
    </g>
  </g>
''' + svg_footer("Многообразие и значение грибов"))

    # Lesson 9: Общая характеристика растений. Водоросли
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Водоросли", f"Биология {grade} класс - Урок {n}",
        "#E3F2FD", "#BBDEFB", "#0277BD") + '''
  <!-- Algae types -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="180" height="170" rx="8" fill="white" stroke="#0277BD" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="180" height="22" rx="8" fill="#0277BD" opacity="0.9"/>
    <rect x="0" y="16" width="180" height="8" fill="#0277BD" opacity="0.9"/>
    <text x="90" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ЗЕЛЁНЫЕ ВОДОРОСЛИ</text>
    <!-- Chlamydomonas -->
    <ellipse cx="50" cy="65" rx="18" ry="14" fill="#81C784" stroke="#2E7D32" stroke-width="1.5"/>
    <circle cx="48" cy="62" r="6" fill="#4CAF50" stroke="#1B5E20" stroke-width="0.8"/>
    <circle cx="48" cy="60" r="2.5" fill="#C62828"/>
    <!-- Flagella -->
    <path d="M50,52 Q55,42 52,35" fill="none" stroke="#2E7D32" stroke-width="1"/>
    <path d="M46,52 Q42,42 45,35" fill="none" stroke="#2E7D32" stroke-width="1"/>
    <text x="50" y="88" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Хламидомонада</text>
    <!-- Chlorella -->
    <circle cx="130" cy="65" r="14" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1.2"/>
    <circle cx="130" cy="62" r="5" fill="#4CAF50" stroke="#1B5E20" stroke-width="0.8"/>
    <text x="130" y="88" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Хлорелла</text>
    <!-- Spirogyra -->
    <rect x="10" y="100" width="160" height="50" rx="3" fill="#E8F5E9"/>
    <path d="M20,125 Q30,115 40,125 Q50,135 60,125 Q70,115 80,125 Q90,135 100,125 Q110,115 120,125 Q130,135 140,125 Q150,115 160,125" fill="none" stroke="#4CAF50" stroke-width="3"/>
    <text x="90" y="155" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Спирогира (нитчатая)</text>
  </g>
  <!-- Brown and Red algae -->
  <g transform="translate(205,75)">
    <rect x="0" y="0" width="180" height="170" rx="8" fill="white" stroke="#0277BD" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="180" height="22" rx="8" fill="#4E342E" opacity="0.9"/>
    <rect x="0" y="16" width="180" height="8" fill="#4E342E" opacity="0.9"/>
    <text x="90" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">БУРЫЕ ВОДОРОСЛИ</text>
    <!-- Kelp/Laminaria -->
    <line x1="50" y1="35" x2="50" y2="120" stroke="#5D4037" stroke-width="3"/>
    <path d="M35,120 Q50,140 65,120" fill="#8D6E63" stroke="#5D4037" stroke-width="1.5"/>
    <path d="M30,70 Q45,75 50,85 Q55,75 70,70" fill="#A1887F" stroke="#795548" stroke-width="1.5"/>
    <path d="M28,80 Q43,88 50,100 Q57,88 72,80" fill="#8D6E63" stroke="#5D4037" stroke-width="1.5"/>
    <path d="M25,92 Q40,100 50,115 Q60,100 75,92" fill="#A1887F" stroke="#795548" stroke-width="1.5"/>
    <text x="50" y="155" font-family="Arial,sans-serif" font-size="7" fill="#5D4037" text-anchor="middle">Ламинария (морская капуста)</text>
    <!-- Fucus -->
    <line x1="140" y1="35" x2="140" y2="80" stroke="#6D4C41" stroke-width="2.5"/>
    <path d="M125,80 Q133,95 140,105 Q147,95 155,80" fill="#8D6E63" stroke="#5D4037" stroke-width="1.5"/>
    <ellipse cx="128" cy="65" rx="8" ry="12" fill="#A1887F" stroke="#795548" stroke-width="1" transform="rotate(-20,128,65)"/>
    <ellipse cx="152" cy="65" rx="8" ry="12" fill="#A1887F" stroke="#795548" stroke-width="1" transform="rotate(20,152,65)"/>
    <text x="140" y="120" font-family="Arial,sans-serif" font-size="7" fill="#5D4037" text-anchor="middle">Фукус</text>
  </g>
  <!-- Features and significance -->
  <g transform="translate(395,75)">
    <rect x="0" y="0" width="190" height="170" rx="8" fill="white" stroke="#0277BD" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="190" height="22" rx="8" fill="#C62828" opacity="0.9"/>
    <rect x="0" y="16" width="190" height="8" fill="#C62828" opacity="0.9"/>
    <text x="95" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">КРАСНЫЕ ВОДОРОСЛИ</text>
    <!-- Red algae -->
    <path d="M70,50 Q65,55 70,65 Q60,70 55,80 Q50,90 60,95 Q70,90 75,80 Q80,70 75,60 Q85,55 90,50" fill="none" stroke="#C62828" stroke-width="2"/>
    <path d="M55,80 Q45,85 50,95" fill="none" stroke="#E57373" stroke-width="1.5"/>
    <path d="M75,80 Q85,85 80,95" fill="none" stroke="#E57373" stroke-width="1.5"/>
    <text x="70" y="110" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle">Порфира</text>
    <text x="95" y="128" font-family="Arial,sans-serif" font-size="8" fill="#0277BD" text-anchor="middle" font-weight="bold">Значение:</text>
    <text x="95" y="142" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Кислород (фотосинтез)</text>
    <text x="95" y="154" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Пища, агар-агар</text>
    <text x="95" y="166" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Йод, альгинаты</text>
  </g>
  <!-- General features -->
  <g transform="translate(15,260)">
    <rect x="0" y="0" width="570" height="88" rx="8" fill="white" stroke="#0277BD" stroke-width="1.5" opacity="0.95"/>
    <text x="285" y="20" font-family="Arial,sans-serif" font-size="11" fill="#0277BD" text-anchor="middle" font-weight="bold">ОБЩАЯ ХАРАКТЕРИСТИКА ВОДОРОСЛЕЙ</text>
    <text x="100" y="42" font-family="Arial,sans-serif" font-size="8" fill="#333">Низшие растения, нет тканей и органов</text>
    <text x="100" y="56" font-family="Arial,sans-serif" font-size="8" fill="#333">Тело - слоевище (таллом)</text>
    <text x="100" y="70" font-family="Arial,sans-serif" font-size="8" fill="#333">Обитают в воде, фотосинтез</text>
    <text x="400" y="42" font-family="Arial,sans-serif" font-size="8" fill="#333">Одноклеточные и многоклеточные</text>
    <text x="400" y="56" font-family="Arial,sans-serif" font-size="8" fill="#333">Размножение: вегет., бесполое, половое</text>
    <text x="400" y="70" font-family="Arial,sans-serif" font-size="8" fill="#333">70% кислорода Земли - из водорослей</text>
  </g>
''' + svg_footer("Общая характеристика растений. Водоросли"))


    # Lesson 10: Мхи
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Мхи", f"Биология {grade} класс - Урок {n}",
        "#E8F5E9", "#C8E6C9", "#2E7D32") + '''
  <!-- Moss plants -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="270" height="270" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="270" height="22" rx="8" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="16" width="270" height="8" fill="#2E7D32" opacity="0.9"/>
    <text x="135" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">КУКУШКИН ЛЁН</text>
    <!-- Moss stems -->
    <g transform="translate(30,30)">
      <rect x="15" y="30" width="4" height="100" rx="1" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.8"/>
      <rect x="10" y="30" width="3" height="12" rx="1" fill="#81C784"/>
      <rect x="20" y="35" width="3" height="10" rx="1" fill="#81C784"/>
      <rect x="8" y="50" width="3" height="10" rx="1" fill="#81C784"/>
      <rect x="22" y="55" width="3" height="10" rx="1" fill="#81C784"/>
      <rect x="10" y="70" width="3" height="10" rx="1" fill="#81C784"/>
      <rect x="21" y="75" width="3" height="10" rx="1" fill="#81C784"/>
      <!-- Sporophyte -->
      <line x1="17" y1="30" x2="17" y2="0" stroke="#8D6E63" stroke-width="1.5"/>
      <ellipse cx="17" cy="-5" rx="6" ry="8" fill="#A1887F" stroke="#795548" stroke-width="1"/>
      <text x="30" y="-3" font-family="Arial,sans-serif" font-size="6" fill="#795548">коробочка</text>
      <text x="17" y="145" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">мужской</text>
    </g>
    <g transform="translate(100,30)">
      <rect x="15" y="30" width="4" height="100" rx="1" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.8"/>
      <rect x="10" y="30" width="3" height="12" rx="1" fill="#81C784"/>
      <rect x="20" y="38" width="3" height="10" rx="1" fill="#81C784"/>
      <rect x="8" y="52" width="3" height="10" rx="1" fill="#81C784"/>
      <rect x="22" y="60" width="3" height="10" rx="1" fill="#81C784"/>
      <!-- Archegonia at top -->
      <ellipse cx="17" cy="26" rx="8" ry="6" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
      <text x="17" y="145" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">женский</text>
    </g>
    <!-- Rhizoids -->
    <g transform="translate(40,160)">
      <line x1="10" y1="0" x2="5" y2="20" stroke="#8D6E63" stroke-width="1"/>
      <line x1="15" y1="0" x2="18" y2="18" stroke="#8D6E63" stroke-width="1"/>
      <line x1="12" y1="0" x2="10" y2="22" stroke="#8D6E63" stroke-width="1"/>
    </g>
    <g transform="translate(110,160)">
      <line x1="10" y1="0" x2="5" y2="20" stroke="#8D6E63" stroke-width="1"/>
      <line x1="15" y1="0" x2="18" y2="18" stroke="#8D6E63" stroke-width="1"/>
    </g>
    <text x="85" y="190" font-family="Arial,sans-serif" font-size="7" fill="#8D6E63" text-anchor="middle">ризоиды (вместо корней)</text>
  </g>
  <!-- Sphagnum -->
  <g transform="translate(300,75)">
    <rect x="0" y="0" width="285" height="130" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="285" height="22" rx="8" fill="#1B5E20" opacity="0.9"/>
    <rect x="0" y="16" width="285" height="8" fill="#1B5E20" opacity="0.9"/>
    <text x="143" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ТОРФЯНОЙ МОХ (СФАГНУМ)</text>
    <!-- Sphagnum stems -->
    <g transform="translate(20,30)">
      <line x1="30" y1="10" x2="30" y2="80" stroke="#4CAF50" stroke-width="2"/>
      <circle cx="20" cy="25" r="3" fill="#81C784"/>
      <circle cx="40" cy="25" r="3" fill="#81C784"/>
      <circle cx="15" cy="35" r="3" fill="#81C784"/>
      <circle cx="45" cy="35" r="3" fill="#81C784"/>
      <circle cx="20" cy="45" r="3" fill="#81C784"/>
      <circle cx="40" cy="45" r="3" fill="#81C784"/>
      <circle cx="15" cy="55" r="3" fill="#81C784"/>
      <circle cx="45" cy="55" r="3" fill="#81C784"/>
      <circle cx="20" cy="65" r="3" fill="#81C784"/>
      <circle cx="40" cy="65" r="3" fill="#81C784"/>
    </g>
    <!-- Sphagnum cell detail -->
    <g transform="translate(110,30)">
      <text x="80" y="5" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" font-weight="bold">Клетка сфагнума</text>
      <rect x="30" y="12" width="40" height="30" rx="3" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1.5"/>
      <rect x="35" y="15" width="10" height="10" rx="1" fill="#4CAF50" stroke="#1B5E20" stroke-width="0.5"/>
      <rect x="48" y="18" width="5" height="5" rx="1" fill="#4CAF50" stroke="#1B5E20" stroke-width="0.5"/>
      <rect x="55" y="15" width="10" height="10" rx="1" fill="#BBDEFB" stroke="#1565C0" stroke-width="0.5"/>
      <text x="40" y="50" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20">живые</text>
      <text x="60" y="50" font-family="Arial,sans-serif" font-size="5" fill="#1565C0">мёртвые</text>
      <text x="50" y="62" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Мёртвые клетки</text>
      <text x="50" y="72" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">впитывают воду</text>
    </g>
  </g>
  <!-- Moss features -->
  <g transform="translate(300,215)">
    <rect x="0" y="0" width="285" height="130" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="285" height="22" rx="8" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="16" width="285" height="8" fill="#2E7D32" opacity="0.9"/>
    <text x="143" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ОСОБЕННОСТИ МХОВ</text>
    <text x="15" y="42" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" font-weight="bold">Высшие споровые растения</text>
    <text x="15" y="56" font-family="Arial,sans-serif" font-size="7" fill="#555">Нет корней - ризоиды</text>
    <text x="15" y="68" font-family="Arial,sans-serif" font-size="7" fill="#555">Нет проводящей системы</text>
    <text x="15" y="80" font-family="Arial,sans-serif" font-size="7" fill="#555">Размножаются спорами</text>
    <text x="15" y="92" font-family="Arial,sans-serif" font-size="7" fill="#555">Нужна вода для оплодотворения</text>
    <text x="15" y="108" font-family="Arial,sans-serif" font-size="8" fill="#795548" font-weight="bold">Значение:</text>
    <text x="15" y="120" font-family="Arial,sans-serif" font-size="7" fill="#555">Торф - топливо, удобрение</text>
  </g>
''' + svg_footer("Мхи"))

    # Lesson 11: Папоротники, хвощи и плауны
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Папоротники, хвощи и плауны", f"Биология {grade} класс - Урок {n}",
        "#E8F5E9", "#C8E6C9", "#1B5E20") + '''
  <!-- Fern -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="190" height="270" rx="8" fill="white" stroke="#1B5E20" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="190" height="22" rx="8" fill="#1B5E20" opacity="0.9"/>
    <rect x="0" y="16" width="190" height="8" fill="#1B5E20" opacity="0.9"/>
    <text x="95" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ПАПОРОТНИК</text>
    <!-- Fern frond -->
    <line x1="95" y1="240" x2="95" y2="50" stroke="#2E7D32" stroke-width="2.5"/>
    <!-- Left pinnae -->
    <path d="M95,80 L60,65 L65,60" fill="none" stroke="#4CAF50" stroke-width="2"/>
    <path d="M60,65 L45,55" fill="none" stroke="#66BB6A" stroke-width="1.2"/>
    <path d="M60,65 L50,72" fill="none" stroke="#66BB6A" stroke-width="1"/>
    <path d="M95,110 L55,95 L60,90" fill="none" stroke="#4CAF50" stroke-width="2"/>
    <path d="M55,95 L40,85" fill="none" stroke="#66BB6A" stroke-width="1.2"/>
    <path d="M55,95 L42,102" fill="none" stroke="#66BB6A" stroke-width="1"/>
    <path d="M95,140 L55,125 L60,120" fill="none" stroke="#4CAF50" stroke-width="2"/>
    <path d="M55,125 L40,115" fill="none" stroke="#66BB6A" stroke-width="1.2"/>
    <!-- Right pinnae -->
    <path d="M95,80 L130,65 L125,60" fill="none" stroke="#4CAF50" stroke-width="2"/>
    <path d="M130,65 L145,55" fill="none" stroke="#66BB6A" stroke-width="1.2"/>
    <path d="M130,65 L140,72" fill="none" stroke="#66BB6A" stroke-width="1"/>
    <path d="M95,110 L135,95 L130,90" fill="none" stroke="#4CAF50" stroke-width="2"/>
    <path d="M135,95 L150,85" fill="none" stroke="#66BB6A" stroke-width="1.2"/>
    <path d="M95,140 L135,125 L130,120" fill="none" stroke="#4CAF50" stroke-width="2"/>
    <!-- Curled top -->
    <path d="M95,50 Q90,40 95,35" fill="none" stroke="#2E7D32" stroke-width="2.5"/>
    <text x="95" y="30" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">вайя (лист)</text>
    <!-- Sorus -->
    <circle cx="55" cy="92" r="6" fill="#795548" stroke="#4E342E" stroke-width="0.8"/>
    <circle cx="135" cy="92" r="6" fill="#795548" stroke="#4E342E" stroke-width="0.8"/>
    <text x="95" y="165" font-family="Arial,sans-serif" font-size="7" fill="#795548" text-anchor="middle">сорусы (споры)</text>
    <!-- Rhizome -->
    <ellipse cx="95" cy="245" rx="25" ry="10" fill="#8D6E63" stroke="#5D4037" stroke-width="1.5"/>
    <line x1="75" y1="250" x2="60" y2="262" stroke="#8D6E63" stroke-width="1.5"/>
    <line x1="115" y1="250" x2="130" y2="262" stroke="#8D6E63" stroke-width="1.5"/>
    <text x="95" y="268" font-family="Arial,sans-serif" font-size="6" fill="#5D4037" text-anchor="middle">корневище + придат. корни</text>
  </g>
  <!-- Horsetail and Clubmoss -->
  <g transform="translate(215,75)">
    <rect x="0" y="0" width="175" height="130" rx="8" fill="white" stroke="#1B5E20" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="175" height="22" rx="8" fill="#1B5E20" opacity="0.9"/>
    <rect x="0" y="16" width="175" height="8" fill="#1B5E20" opacity="0.9"/>
    <text x="88" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ХВОЩ</text>
    <!-- Horsetail stem -->
    <line x1="60" y1="110" x2="60" y2="35" stroke="#4CAF50" stroke-width="3"/>
    <!-- Nodes -->
    <ellipse cx="60" cy="50" rx="8" ry="2" fill="#388E3C" stroke="#1B5E20" stroke-width="0.8"/>
    <ellipse cx="60" cy="70" rx="8" ry="2" fill="#388E3C" stroke="#1B5E20" stroke-width="0.8"/>
    <ellipse cx="60" cy="90" rx="8" ry="2" fill="#388E3C" stroke="#1B5E20" stroke-width="0.8"/>
    <!-- Branches -->
    <line x1="52" y1="50" x2="35" y2="42" stroke="#66BB6A" stroke-width="1.5"/>
    <line x1="35" y1="42" x2="25" y2="38" stroke="#66BB6A" stroke-width="1"/>
    <line x1="68" y1="50" x2="85" y2="42" stroke="#66BB6A" stroke-width="1.5"/>
    <line x1="52" y1="70" x2="35" y2="62" stroke="#66BB6A" stroke-width="1.5"/>
    <line x1="68" y1="70" x2="85" y2="62" stroke="#66BB6A" stroke-width="1.5"/>
    <line x1="52" y1="90" x2="35" y2="82" stroke="#66BB6A" stroke-width="1.5"/>
    <line x1="68" y1="90" x2="85" y2="82" stroke="#66BB6A" stroke-width="1.5"/>
    <!-- Spore cone -->
    <ellipse cx="60" cy="32" rx="6" ry="8" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
    <text x="120" y="55" font-family="Arial,sans-serif" font-size="7" fill="#1B5E20">членистый</text>
    <text x="120" y="65" font-family="Arial,sans-serif" font-size="7" fill="#1B5E20">стебель</text>
    <text x="120" y="80" font-family="Arial,sans-serif" font-size="7" fill="#795548">спороносный</text>
    <text x="120" y="90" font-family="Arial,sans-serif" font-size="7" fill="#795548">колосок</text>
  </g>
  <!-- Clubmoss -->
  <g transform="translate(215,215)">
    <rect x="0" y="0" width="175" height="130" rx="8" fill="white" stroke="#1B5E20" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="175" height="22" rx="8" fill="#1B5E20" opacity="0.9"/>
    <rect x="0" y="16" width="175" height="8" fill="#1B5E20" opacity="0.9"/>
    <text x="88" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ПЛАУН</text>
    <!-- Clubmoss creeping stem -->
    <path d="M20,70 Q50,65 80,70 Q110,75 140,70" fill="none" stroke="#2E7D32" stroke-width="2.5"/>
    <!-- Small leaves -->
    <line x1="30" y1="67" x2="25" y2="58" stroke="#4CAF50" stroke-width="1"/>
    <line x1="40" y1="66" x2="38" y2="56" stroke="#4CAF50" stroke-width="1"/>
    <line x1="55" y1="66" x2="52" y2="57" stroke="#4CAF50" stroke-width="1"/>
    <line x1="65" y1="68" x2="68" y2="58" stroke="#4CAF50" stroke-width="1"/>
    <line x1="80" y1="70" x2="78" y2="60" stroke="#4CAF50" stroke-width="1"/>
    <line x1="95" y1="72" x2="98" y2="62" stroke="#4CAF50" stroke-width="1"/>
    <line x1="110" y1="74" x2="108" y2="64" stroke="#4CAF50" stroke-width="1"/>
    <line x1="125" y1="72" x2="128" y2="62" stroke="#4CAF50" stroke-width="1"/>
    <!-- Upright stems with strobili -->
    <line x1="60" y1="66" x2="60" y2="40" stroke="#2E7D32" stroke-width="2"/>
    <ellipse cx="60" cy="36" rx="4" ry="7" fill="#795548" stroke="#5D4037" stroke-width="1"/>
    <line x1="110" y1="74" x2="110" y2="45" stroke="#2E7D32" stroke-width="2"/>
    <ellipse cx="110" cy="41" rx="4" ry="7" fill="#795548" stroke="#5D4037" stroke-width="1"/>
    <text x="60" y="30" font-family="Arial,sans-serif" font-size="5" fill="#795548" text-anchor="middle">стробил</text>
    <text x="88" y="100" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Стелющийся стебель</text>
    <text x="88" y="112" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">с мелкими листьями</text>
  </g>
  <!-- Life cycle -->
  <g transform="translate(400,75)">
    <rect x="0" y="0" width="185" height="270" rx="8" fill="white" stroke="#1B5E20" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="185" height="22" rx="8" fill="#1B5E20" opacity="0.9"/>
    <rect x="0" y="16" width="185" height="8" fill="#1B5E20" opacity="0.9"/>
    <text x="93" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ЖИЗНЕННЫЙ ЦИКЛ</text>
    <!-- Spore -->
    <circle cx="93" cy="50" r="8" fill="#FFECB3" stroke="#FF8F00" stroke-width="1"/>
    <text x="93" y="54" font-family="Arial,sans-serif" font-size="6" fill="#FF8F00" text-anchor="middle">спора</text>
    <line x1="93" y1="60" x2="93" y2="72" stroke="#1B5E20" stroke-width="1"/>
    <polygon points="90,70 93,76 96,70" fill="#1B5E20"/>
    <!-- Prothallus -->
    <ellipse cx="93" cy="85" rx="20" ry="8" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
    <text x="93" y="89" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">заросток</text>
    <line x1="93" y1="95" x2="93" y2="107" stroke="#1B5E20" stroke-width="1"/>
    <polygon points="90,105 93,111 96,105" fill="#1B5E20"/>
    <!-- Fertilization -->
    <text x="93" y="120" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">Оплодотворение</text>
    <text x="93" y="130" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">(нужна вода!)</text>
    <line x1="93" y1="135" x2="93" y2="147" stroke="#1B5E20" stroke-width="1"/>
    <polygon points="90,145 93,151 96,145" fill="#1B5E20"/>
    <!-- Young fern -->
    <line x1="93" y1="155" x2="93" y2="175" stroke="#2E7D32" stroke-width="2"/>
    <path d="M93,175 Q85,170 80,165" fill="none" stroke="#4CAF50" stroke-width="1.5"/>
    <path d="M93,175 Q101,170 106,165" fill="none" stroke="#4CAF50" stroke-width="1.5"/>
    <text x="93" y="190" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">молодой папоротник</text>
    <line x1="93" y1="195" x2="93" y2="207" stroke="#1B5E20" stroke-width="1"/>
    <polygon points="90,205 93,211 96,205" fill="#1B5E20"/>
    <!-- Adult fern -->
    <rect x="73" y="215" width="40" height="25" rx="2" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
    <path d="M93,215 Q85,205 80,200" fill="none" stroke="#4CAF50" stroke-width="1.5"/>
    <path d="M93,215 Q101,205 106,200" fill="none" stroke="#4CAF50" stroke-width="1.5"/>
    <text x="93" y="255" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">взрослое растение</text>
    <!-- Arrows back to spore -->
    <path d="M115,240 Q140,240 140,50 Q140,40 105,50" fill="none" stroke="#FF8F00" stroke-width="1" stroke-dasharray="3,2"/>
  </g>
''' + svg_footer("Папоротники, хвощи и плауны"))

    # Lesson 12: Голосеменные растения
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Голосеменные растения", f"Биология {grade} класс - Урок {n}",
        "#E8F5E9", "#C8E6C9", "#2E7D32") + '''
  <!-- Pine tree -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="190" height="270" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="190" height="22" rx="8" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="16" width="190" height="8" fill="#2E7D32" opacity="0.9"/>
    <text x="95" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">СОСНА</text>
    <!-- Trunk -->
    <rect x="80" y="150" width="30" height="100" rx="3" fill="#8D6E63" stroke="#5D4037" stroke-width="1.5"/>
    <!-- Crown layers -->
    <polygon points="95,30 50,80 140,80" fill="#2E7D32" stroke="#1B5E20" stroke-width="1.5"/>
    <polygon points="95,55 40,110 150,110" fill="#388E3C" stroke="#1B5E20" stroke-width="1.5"/>
    <polygon points="95,80 35,140 155,140" fill="#43A047" stroke="#2E7D32" stroke-width="1.5"/>
    <!-- Roots -->
    <line x1="80" y1="250" x2="55" y2="265" stroke="#8D6E63" stroke-width="2"/>
    <line x1="95" y1="250" x2="95" y2="268" stroke="#8D6E63" stroke-width="2"/>
    <line x1="110" y1="250" x2="135" y2="265" stroke="#8D6E63" stroke-width="2"/>
  </g>
  <!-- Pine needle and cone -->
  <g transform="translate(215,75)">
    <rect x="0" y="0" width="175" height="130" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="175" height="22" rx="8" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="16" width="175" height="8" fill="#2E7D32" opacity="0.9"/>
    <text x="88" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ХВОЯ И ШИШКИ</text>
    <!-- Needles -->
    <line x1="30" y1="45" x2="30" y2="95" stroke="#2E7D32" stroke-width="2.5" stroke-linecap="round"/>
    <line x1="40" y1="45" x2="40" y2="95" stroke="#2E7D32" stroke-width="2.5" stroke-linecap="round"/>
    <text x="35" y="108" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">хвоя</text>
    <!-- Female cone -->
    <ellipse cx="110" cy="55" rx="18" ry="25" fill="#8D6E63" stroke="#5D4037" stroke-width="1.5"/>
    <line x1="95" y1="40" x2="125" y2="40" stroke="#5D4037" stroke-width="0.8"/>
    <line x1="93" y1="50" x2="127" y2="50" stroke="#5D4037" stroke-width="0.8"/>
    <line x1="93" y1="60" x2="127" y2="60" stroke="#5D4037" stroke-width="0.8"/>
    <line x1="95" y1="70" x2="125" y2="70" stroke="#5D4037" stroke-width="0.8"/>
    <text x="110" y="90" font-family="Arial,sans-serif" font-size="6" fill="#795548" text-anchor="middle">женская шишка</text>
    <!-- Male cone -->
    <ellipse cx="150" cy="100" rx="6" ry="10" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
    <text x="150" y="118" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">мужская</text>
  </g>
  <!-- Seed detail -->
  <g transform="translate(215,215)">
    <rect x="0" y="0" width="375" height="130" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="375" height="22" rx="8" fill="#1B5E20" opacity="0.9"/>
    <rect x="0" y="16" width="375" height="8" fill="#1B5E20" opacity="0.9"/>
    <text x="188" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">СЕМЯ ГОЛОСЕМЕННОГО (СЕМЯ СОСНЫ)</text>
    <!-- Seed cross-section -->
    <ellipse cx="100" cy="78" rx="40" ry="30" fill="#8D6E63" stroke="#5D4037" stroke-width="1.5"/>
    <text x="100" y="58" font-family="Arial,sans-serif" font-size="6" fill="#5D4037" text-anchor="middle">кожура</text>
    <ellipse cx="100" cy="80" rx="25" ry="18" fill="#FFECB3" stroke="#FF8F00" stroke-width="1"/>
    <text x="100" y="78" font-family="Arial,sans-serif" font-size="6" fill="#FF8F00" text-anchor="middle">эндосперм</text>
    <ellipse cx="100" cy="82" rx="10" ry="8" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
    <text x="100" y="86" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle">зародыш</text>
    <!-- Wing -->
    <path d="M60,78 Q30,60 20,78 Q30,95 60,78" fill="#D7CCC8" stroke="#8D6E63" stroke-width="0.8"/>
    <text x="38" y="82" font-family="Arial,sans-serif" font-size="5" fill="#8D6E63" text-anchor="middle">крыло</text>
    <!-- Key features -->
    <text x="220" y="42" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" font-weight="bold">Признаки голосеменных:</text>
    <text x="220" y="56" font-family="Arial,sans-serif" font-size="7" fill="#555">Семя открытое (без плода)</text>
    <text x="220" y="68" font-family="Arial,sans-serif" font-size="7" fill="#555">Листья - хвоя (игольчатые)</text>
    <text x="220" y="80" font-family="Arial,sans-serif" font-size="7" fill="#555">Смола, древесина</text>
    <text x="220" y="92" font-family="Arial,sans-serif" font-size="7" fill="#555">Вечнозелёные (большинство)</text>
    <text x="220" y="108" font-family="Arial,sans-serif" font-size="7" fill="#555">Опыление ветром</text>
    <text x="220" y="120" font-family="Arial,sans-serif" font-size="7" fill="#795548" font-weight="bold">Представители: сосна, ель, лиственница, кедр</text>
  </g>
  <!-- Other gymnosperms -->
  <g transform="translate(400,75)">
    <rect x="0" y="0" width="185" height="130" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="185" height="22" rx="8" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="16" width="185" height="8" fill="#2E7D32" opacity="0.9"/>
    <text x="93" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">МНОГООБРАЗИЕ</text>
    <!-- Spruce -->
    <polygon points="45,35 30,80 60,80" fill="#1B5E20" stroke="#0D3B0F" stroke-width="1"/>
    <polygon points="45,50 25,95 65,95" fill="#2E7D32" stroke="#1B5E20" stroke-width="1"/>
    <rect x="42" y="95" width="6" height="15" fill="#795548"/>
    <text x="45" y="118" font-family="Arial,sans-serif" font-size="6" fill="#1B5E20" text-anchor="middle">Ель</text>
    <!-- Juniper -->
    <rect x="110" y="65" width="6" height="25" fill="#795548"/>
    <ellipse cx="113" cy="55" rx="15" ry="18" fill="#388E3C" stroke="#1B5E20" stroke-width="1"/>
    <circle cx="113" cy="65" r="4" fill="#1565C0" stroke="#0D47A1" stroke-width="0.8"/>
    <text x="113" y="100" font-family="Arial,sans-serif" font-size="6" fill="#1B5E20" text-anchor="middle">Можжевельник</text>
  </g>
''' + svg_footer("Голосеменные растения"))


    # Lesson 13: Общая характеристика покрытосеменных
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Общая характеристика покрытосеменных", f"Биология {grade} класс - Урок {n}",
        "#FCE4EC", "#F8BBD0", "#C2185B") + '''
  <!-- Flowering plant -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="280" height="270" rx="8" fill="white" stroke="#C2185B" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="280" height="22" rx="8" fill="#C2185B" opacity="0.9"/>
    <rect x="0" y="16" width="280" height="8" fill="#C2185B" opacity="0.9"/>
    <text x="140" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ЦВЕТКОВОЕ РАСТЕНИЕ</text>
    <!-- Root system -->
    <line x1="140" y1="220" x2="140" y2="265" stroke="#795548" stroke-width="3"/>
    <line x1="140" y1="235" x2="110" y2="260" stroke="#795548" stroke-width="2"/>
    <line x1="140" y1="235" x2="170" y2="260" stroke="#795548" stroke-width="2"/>
    <line x1="140" y1="245" x2="120" y2="268" stroke="#795548" stroke-width="1.5"/>
    <line x1="140" y1="245" x2="160" y2="268" stroke="#795548" stroke-width="1.5"/>
    <text x="140" y="258" font-family="Arial,sans-serif" font-size="7" fill="#5D4037" text-anchor="middle">корневая система</text>
    <!-- Stem -->
    <rect x="135" y="95" width="10" height="130" rx="2" fill="#66BB6A" stroke="#2E7D32" stroke-width="1.5"/>
    <text x="165" y="175" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">стебель</text>
    <!-- Leaves -->
    <path d="M135,170 L95,155 L90,160 L135,180" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
    <line x1="135" y1="175" x2="95" y2="158" stroke="#2E7D32" stroke-width="0.8"/>
    <path d="M145,150 L185,135 L190,140 L145,160" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
    <line x1="145" y1="155" x2="185" y2="138" stroke="#2E7D32" stroke-width="0.8"/>
    <text x="75" y="155" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">листья</text>
    <!-- Flower -->
    <g transform="translate(140,75)">
      <line x1="0" y1="20" x2="0" y2="45" stroke="#4CAF50" stroke-width="1.5"/>
      <ellipse cx="-12" cy="15" rx="12" ry="8" fill="#F48FB1" stroke="#E91E63" stroke-width="1" transform="rotate(-30,-12,15)"/>
      <ellipse cx="12" cy="15" rx="12" ry="8" fill="#F48FB1" stroke="#E91E63" stroke-width="1" transform="rotate(30,12,15)"/>
      <ellipse cx="0" cy="5" rx="12" ry="8" fill="#F48FB1" stroke="#E91E63" stroke-width="1"/>
      <ellipse cx="-10" cy="22" rx="10" ry="7" fill="#F48FB1" stroke="#E91E63" stroke-width="1" transform="rotate(-60,-10,22)"/>
      <ellipse cx="10" cy="22" rx="10" ry="7" fill="#F48FB1" stroke="#E91E63" stroke-width="1" transform="rotate(60,10,22)"/>
      <circle cx="0" cy="15" r="8" fill="#FFC107" stroke="#F57F17" stroke-width="1"/>
      <text x="30" y="15" font-family="Arial,sans-serif" font-size="7" fill="#C2185B">цветок</text>
    </g>
    <!-- Fruit -->
    <g transform="translate(200,100)">
      <ellipse cx="15" cy="10" rx="10" ry="14" fill="#EF5350" stroke="#C62828" stroke-width="1"/>
      <text x="15" y="32" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">плод</text>
    </g>
  </g>
  <!-- Classes comparison -->
  <g transform="translate(310,75)">
    <rect x="0" y="0" width="275" height="135" rx="8" fill="white" stroke="#C2185B" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#C2185B" opacity="0.9"/>
    <rect x="0" y="16" width="275" height="8" fill="#C2185B" opacity="0.9"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ДВА КЛАССА ПОКРЫТОСЕМЕННЫХ</text>
    <!-- Dicotyledons -->
    <rect x="10" y="30" width="125" height="95" rx="5" fill="#FCE4EC" stroke="#C2185B" stroke-width="1"/>
    <text x="73" y="45" font-family="Arial,sans-serif" font-size="8" fill="#C2185B" text-anchor="middle" font-weight="bold">Двудольные</text>
    <!-- Two cotyledons -->
    <ellipse cx="35" cy="65" rx="8" ry="5" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
    <ellipse cx="55" cy="65" rx="8" ry="5" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
    <text x="45" y="80" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">2 семядоли</text>
    <!-- Net venation -->
    <ellipse cx="100" cy="65" rx="12" ry="8" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.8"/>
    <line x1="92" y1="65" x2="108" y2="60" stroke="#2E7D32" stroke-width="0.3"/>
    <line x1="92" y1="65" x2="105" y2="70" stroke="#2E7D32" stroke-width="0.3"/>
    <text x="100" y="80" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">сетчатое</text>
    <!-- 4-5 petal flower -->
    <circle cx="45" cy="100" r="5" fill="#F48FB1" stroke="#C2185B" stroke-width="0.5"/>
    <circle cx="53" cy="105" r="5" fill="#F48FB1" stroke="#C2185B" stroke-width="0.5"/>
    <circle cx="53" cy="95" r="5" fill="#F48FB1" stroke="#C2185B" stroke-width="0.5"/>
    <circle cx="45" cy="108" r="5" fill="#F48FB1" stroke="#C2185B" stroke-width="0.5"/>
    <circle cx="49" cy="101" r="3" fill="#FFC107"/>
    <text x="75" y="108" font-family="Arial,sans-serif" font-size="5" fill="#C2185B">4-5 лепестков</text>
    <!-- Monocotyledons -->
    <rect x="145" y="30" width="125" height="95" rx="5" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
    <text x="208" y="45" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Однодольные</text>
    <!-- One cotyledon -->
    <ellipse cx="205" cy="65" rx="10" ry="5" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
    <text x="205" y="80" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">1 семядоля</text>
    <!-- Parallel venation -->
    <rect x="235" y="56" width="15" height="18" rx="2" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
    <line x1="239" y1="56" x2="239" y2="74" stroke="#2E7D32" stroke-width="0.3"/>
    <line x1="243" y1="56" x2="243" y2="74" stroke="#2E7D32" stroke-width="0.3"/>
    <line x1="247" y1="56" x2="247" y2="74" stroke="#2E7D32" stroke-width="0.3"/>
    <text x="243" y="85" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">параллельное</text>
    <!-- 3 petal flower -->
    <ellipse cx="195" cy="100" rx="5" ry="8" fill="#FFF176" stroke="#F9A825" stroke-width="0.5" transform="rotate(-30,195,100)"/>
    <ellipse cx="210" cy="100" rx="5" ry="8" fill="#FFF176" stroke="#F9A825" stroke-width="0.5" transform="rotate(30,210,100)"/>
    <ellipse cx="202" cy="95" rx="5" ry="8" fill="#FFF176" stroke="#F9A825" stroke-width="0.5"/>
    <circle cx="202" cy="100" r="2.5" fill="#FF8F00"/>
    <text x="202" y="115" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">3 лепестка</text>
  </g>
  <!-- Advantages -->
  <g transform="translate(310,220)">
    <rect x="0" y="0" width="275" height="125" rx="8" fill="white" stroke="#C2185B" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#AD1457" opacity="0.9"/>
    <rect x="0" y="16" width="275" height="8" fill="#AD1457" opacity="0.9"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ПРЕИМУЩЕСТВА ПОКРЫТОСЕМЕННЫХ</text>
    <text x="15" y="42" font-family="Arial,sans-serif" font-size="8" fill="#C2185B" font-weight="bold">1.</text>
    <text x="30" y="42" font-family="Arial,sans-serif" font-size="8" fill="#333">Семя защищено плодом</text>
    <text x="15" y="58" font-family="Arial,sans-serif" font-size="8" fill="#C2185B" font-weight="bold">2.</text>
    <text x="30" y="58" font-family="Arial,sans-serif" font-size="8" fill="#333">Цветок - орган размножения</text>
    <text x="15" y="74" font-family="Arial,sans-serif" font-size="8" fill="#C2185B" font-weight="bold">3.</text>
    <text x="30" y="74" font-family="Arial,sans-serif" font-size="8" fill="#333">Опыление насекомыми (эффективнее)</text>
    <text x="15" y="90" font-family="Arial,sans-serif" font-size="8" fill="#C2185B" font-weight="bold">4.</text>
    <text x="30" y="90" font-family="Arial,sans-serif" font-size="8" fill="#333">Разнообразие плодов для распространения</text>
    <text x="15" y="106" font-family="Arial,sans-serif" font-size="8" fill="#C2185B" font-weight="bold">5.</text>
    <text x="30" y="106" font-family="Arial,sans-serif" font-size="8" fill="#333">Проводящая система совершеннее</text>
  </g>
''' + svg_footer("Общая характеристика покрытосеменных"))

    # Lesson 14: Корень
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Корень", f"Биология {grade} класс - Урок {n}",
        "#FFF3E0", "#FFE0B2", "#795548") + '''
  <!-- Root structure -->
  <g transform="translate(20,75)">
    <rect x="0" y="0" width="250" height="275" rx="8" fill="white" stroke="#795548" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="250" height="22" rx="8" fill="#795548" opacity="0.9"/>
    <rect x="0" y="16" width="250" height="8" fill="#795548" opacity="0.9"/>
    <text x="125" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">СТРОЕНИЕ КОРНЯ</text>
    <!-- Root with zones -->
    <g transform="translate(80,30)">
      <!-- Main root -->
      <path d="M40,10 L40,200" stroke="#8D6E63" stroke-width="8"/>
      <path d="M40,200 Q40,220 30,230" fill="none" stroke="#8D6E63" stroke-width="3"/>
      <path d="M40,200 Q40,220 50,230" fill="none" stroke="#8D6E63" stroke-width="3"/>
      <!-- Lateral roots -->
      <path d="M40,80 Q25,90 15,100" fill="none" stroke="#A1887F" stroke-width="2.5"/>
      <path d="M40,80 Q55,90 65,100" fill="none" stroke="#A1887F" stroke-width="2.5"/>
      <path d="M40,130 Q25,140 18,150" fill="none" stroke="#A1887F" stroke-width="2"/>
      <path d="M40,130 Q55,140 62,150" fill="none" stroke="#A1887F" stroke-width="2"/>
      <path d="M40,170 Q30,178 22,185" fill="none" stroke="#A1887F" stroke-width="1.5"/>
      <path d="M40,170 Q50,178 58,185" fill="none" stroke="#A1887F" stroke-width="1.5"/>
      <!-- Root cap -->
      <ellipse cx="40" cy="16" rx="12" ry="8" fill="#D7CCC8" stroke="#8D6E63" stroke-width="1"/>
      <!-- Zone markers -->
      <line x1="60" y1="10" x2="75" y2="10" stroke="#C62828" stroke-width="0.8"/>
      <text x="78" y="14" font-family="Arial,sans-serif" font-size="6" fill="#C62828">корневой чехлик</text>
      <line x1="60" y1="30" x2="75" y2="30" stroke="#FF8F00" stroke-width="0.8"/>
      <text x="78" y="34" font-family="Arial,sans-serif" font-size="6" fill="#FF8F00">зона деления</text>
      <line x1="60" y1="55" x2="75" y2="55" stroke="#2E7D32" stroke-width="0.8"/>
      <text x="78" y="59" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">зона роста</text>
      <line x1="60" y1="85" x2="75" y2="85" stroke="#1565C0" stroke-width="0.8"/>
      <text x="78" y="89" font-family="Arial,sans-serif" font-size="6" fill="#1565C0">зона всасывания</text>
      <!-- Root hairs -->
      <line x1="36" y1="75" x2="25" y2="70" stroke="#4CAF50" stroke-width="0.5"/>
      <line x1="36" y1="80" x2="22" y2="78" stroke="#4CAF50" stroke-width="0.5"/>
      <line x1="36" y1="85" x2="20" y2="85" stroke="#4CAF50" stroke-width="0.5"/>
      <line x1="36" y1="90" x2="22" y2="92" stroke="#4CAF50" stroke-width="0.5"/>
      <line x1="36" y1="95" x2="25" y2="100" stroke="#4CAF50" stroke-width="0.5"/>
      <line x1="44" y1="75" x2="55" y2="70" stroke="#4CAF50" stroke-width="0.5"/>
      <line x1="44" y1="80" x2="58" y2="78" stroke="#4CAF50" stroke-width="0.5"/>
      <line x1="44" y1="85" x2="60" y2="85" stroke="#4CAF50" stroke-width="0.5"/>
      <line x1="44" y1="90" x2="58" y2="92" stroke="#4CAF50" stroke-width="0.5"/>
      <line x1="44" y1="95" x2="55" y2="100" stroke="#4CAF50" stroke-width="0.5"/>
      <text x="78" y="100" font-family="Arial,sans-serif" font-size="5" fill="#4CAF50">корневые волоски</text>
      <line x1="60" y1="130" x2="75" y2="130" stroke="#795548" stroke-width="0.8"/>
      <text x="78" y="134" font-family="Arial,sans-serif" font-size="6" fill="#795548">зона проведения</text>
    </g>
  </g>
  <!-- Root systems -->
  <g transform="translate(285,75)">
    <rect x="0" y="0" width="300" height="135" rx="8" fill="white" stroke="#795548" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="300" height="22" rx="8" fill="#795548" opacity="0.9"/>
    <rect x="0" y="16" width="300" height="8" fill="#795548" opacity="0.9"/>
    <text x="150" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ТИПЫ КОРНЕВЫХ СИСТЕМ</text>
    <!-- Taproot -->
    <g transform="translate(50,30)">
      <line x1="0" y1="5" x2="0" y2="90" stroke="#795548" stroke-width="4"/>
      <path d="M0,25 Q-20,40 -25,55" fill="none" stroke="#A1887F" stroke-width="2"/>
      <path d="M0,25 Q20,40 25,55" fill="none" stroke="#A1887F" stroke-width="2"/>
      <path d="M0,50 Q-15,60 -20,75" fill="none" stroke="#A1887F" stroke-width="1.5"/>
      <path d="M0,50 Q15,60 20,75" fill="none" stroke="#A1887F" stroke-width="1.5"/>
      <path d="M0,70 Q-10,78 -12,88" fill="none" stroke="#A1887F" stroke-width="1"/>
      <path d="M0,70 Q10,78 12,88" fill="none" stroke="#A1887F" stroke-width="1"/>
      <text x="0" y="100" font-family="Arial,sans-serif" font-size="7" fill="#795548" text-anchor="middle" font-weight="bold">Стержневая</text>
      <text x="0" y="110" font-family="Arial,sans-serif" font-size="6" fill="#888" text-anchor="middle">(двудольные)</text>
    </g>
    <!-- Fibrous -->
    <g transform="translate(200,30)">
      <path d="M-15,5 Q-20,30 -25,55" fill="none" stroke="#A1887F" stroke-width="2"/>
      <path d="M-5,5 Q-8,30 -12,55" fill="none" stroke="#A1887F" stroke-width="2"/>
      <path d="M5,5 Q8,30 12,55" fill="none" stroke="#A1887F" stroke-width="2"/>
      <path d="M15,5 Q20,30 25,55" fill="none" stroke="#A1887F" stroke-width="2"/>
      <path d="M0,5 Q0,30 0,55" fill="none" stroke="#795548" stroke-width="2"/>
      <path d="M-20,55 Q-25,70 -22,85" fill="none" stroke="#A1887F" stroke-width="1.5"/>
      <path d="M-8,55 Q-12,70 -10,85" fill="none" stroke="#A1887F" stroke-width="1.5"/>
      <path d="M8,55 Q12,70 10,85" fill="none" stroke="#A1887F" stroke-width="1.5"/>
      <path d="M20,55 Q25,70 22,85" fill="none" stroke="#A1887F" stroke-width="1.5"/>
      <text x="0" y="100" font-family="Arial,sans-serif" font-size="7" fill="#795548" text-anchor="middle" font-weight="bold">Мочковатая</text>
      <text x="0" y="110" font-family="Arial,sans-serif" font-size="6" fill="#888" text-anchor="middle">(однодольные)</text>
    </g>
  </g>
  <!-- Root functions -->
  <g transform="translate(285,220)">
    <rect x="0" y="0" width="300" height="130" rx="8" fill="white" stroke="#795548" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="300" height="22" rx="8" fill="#5D4037" opacity="0.9"/>
    <rect x="0" y="16" width="300" height="8" fill="#5D4037" opacity="0.9"/>
    <text x="150" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ФУНКЦИИ КОРНЯ И ВИДОИЗМЕНЕНИЯ</text>
    <text x="15" y="42" font-family="Arial,sans-serif" font-size="8" fill="#795548" font-weight="bold">Функции:</text>
    <text x="15" y="54" font-family="Arial,sans-serif" font-size="7" fill="#555">Закрепление, всасывание воды и минералов</text>
    <text x="15" y="66" font-family="Arial,sans-serif" font-size="7" fill="#555">Транспорт веществ, запасание</text>
    <text x="15" y="82" font-family="Arial,sans-serif" font-size="8" fill="#795548" font-weight="bold">Видоизменения:</text>
    <!-- Carrot root -->
    <path d="M180,35 Q185,50 180,75 Q178,85 175,90" fill="#FF8A65" stroke="#E64A19" stroke-width="1.5"/>
    <path d="M190,35 Q195,50 190,75 Q188,85 185,90" fill="#FF8A65" stroke="#E64A19" stroke-width="1.5"/>
    <line x1="185" y1="25" x2="185" y2="35" stroke="#4CAF50" stroke-width="1.5"/>
    <text x="185" y="100" font-family="Arial,sans-serif" font-size="6" fill="#E64A19" text-anchor="middle">корнеплод</text>
    <!-- Air roots -->
    <path d="M240,35 Q235,45 240,55" fill="none" stroke="#795548" stroke-width="1.5"/>
    <path d="M250,35 Q255,45 250,55" fill="none" stroke="#795548" stroke-width="1.5"/>
    <text x="245" y="65" font-family="Arial,sans-serif" font-size="6" fill="#795548" text-anchor="middle">воздушные</text>
    <!-- Contractile roots -->
    <path d="M280,40 L278,55 L282,55 L280,65" fill="none" stroke="#795548" stroke-width="2"/>
    <path d="M290,40 L288,55 L292,55 L290,65" fill="none" stroke="#795548" stroke-width="2"/>
    <text x="285" y="75" font-family="Arial,sans-serif" font-size="5" fill="#795548" text-anchor="middle">втягивающие</text>
  </g>
''' + svg_footer("Корень"))

    # Lesson 15: Побег и стебель
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Побег и стебель", f"Биология {grade} класс - Урок {n}",
        "#E8F5E9", "#C8E6C9", "#2E7D32") + '''
  <!-- Shoot structure -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="280" height="270" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="280" height="22" rx="8" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="16" width="280" height="8" fill="#2E7D32" opacity="0.9"/>
    <text x="140" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">СТРОЕНИЕ ПОБЕГА</text>
    <!-- Main stem -->
    <line x1="120" y1="30" x2="120" y2="250" stroke="#4CAF50" stroke-width="4"/>
    <!-- Terminal bud -->
    <ellipse cx="120" cy="30" rx="8" ry="12" fill="#81C784" stroke="#2E7D32" stroke-width="1.5"/>
    <text x="145" y="32" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">верхушечная</text>
    <text x="145" y="42" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">почка</text>
    <!-- Node -->
    <ellipse cx="120" cy="70" rx="15" ry="3" fill="#388E3C" stroke="#2E7D32" stroke-width="1"/>
    <text x="155" y="72" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">узел</text>
    <!-- Leaf at node -->
    <path d="M120,70 L70,55 L65,60 L120,80" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
    <line x1="120" y1="75" x2="72" y2="58" stroke="#2E7D32" stroke-width="0.8"/>
    <text x="55" y="52" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">лист</text>
    <!-- Axillary bud -->
    <ellipse cx="107" cy="72" rx="4" ry="6" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
    <text x="55" y="75" font-family="Arial,sans-serif" font-size="6" fill="#388E3C">пазушная почка</text>
    <!-- Internode -->
    <line x1="85" y1="90" x2="85" y2="130" stroke="#FF8F00" stroke-width="1.5"/>
    <text x="75" y="115" font-family="Arial,sans-serif" font-size="7" fill="#FF8F00" text-anchor="end">междоузлие</text>
    <!-- Another node -->
    <ellipse cx="120" cy="140" rx="15" ry="3" fill="#388E3C" stroke="#2E7D32" stroke-width="1"/>
    <!-- Leaf -->
    <path d="M120,140 L170,125 L175,130 L120,150" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
    <line x1="120" y1="145" x2="168" y2="128" stroke="#2E7D32" stroke-width="0.8"/>
    <!-- Lateral shoot -->
    <line x1="120" y1="140" x2="175" y2="120" stroke="#4CAF50" stroke-width="2.5"/>
    <ellipse cx="175" cy="118" rx="5" ry="8" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
    <text x="195" y="118" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">боковой</text>
    <text x="195" y="128" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">побег</text>
  </g>
  <!-- Stem cross-section -->
  <g transform="translate(310,75)">
    <rect x="0" y="0" width="275" height="270" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="16" width="275" height="8" fill="#2E7D32" opacity="0.9"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ПОПЕРЕЧНЫЙ СРЕЗ СТЕБЛЯ</text>
    <!-- Cross section diagram -->
    <circle cx="110" cy="120" r="90" fill="#FFE0B2" stroke="#795548" stroke-width="1.5"/>
    <!-- Bark -->
    <circle cx="110" cy="120" r="90" fill="none" stroke="#5D4037" stroke-width="4"/>
    <text x="110" y="32" font-family="Arial,sans-serif" font-size="7" fill="#5D4037" text-anchor="middle">кора</text>
    <!-- Phloem -->
    <circle cx="110" cy="120" r="82" fill="none" stroke="#FF8F00" stroke-width="3"/>
    <text x="200" y="55" font-family="Arial,sans-serif" font-size="6" fill="#FF8F00">луб (флоэма)</text>
    <!-- Cambium -->
    <circle cx="110" cy="120" r="78" fill="none" stroke="#4CAF50" stroke-width="1.5" stroke-dasharray="2,1"/>
    <text x="200" y="70" font-family="Arial,sans-serif" font-size="6" fill="#4CAF50">камбий</text>
    <!-- Wood (xylem) - annual rings -->
    <circle cx="110" cy="120" r="75" fill="#FFECB3" stroke="#D7CCC8" stroke-width="1"/>
    <circle cx="110" cy="120" r="65" fill="none" stroke="#A1887F" stroke-width="1.5"/>
    <circle cx="110" cy="120" r="55" fill="none" stroke="#A1887F" stroke-width="1.5"/>
    <circle cx="110" cy="120" r="45" fill="none" stroke="#A1887F" stroke-width="1.5"/>
    <circle cx="110" cy="120" r="35" fill="none" stroke="#A1887F" stroke-width="1.5"/>
    <text x="110" y="125" font-family="Arial,sans-serif" font-size="7" fill="#795548" text-anchor="middle">древесина</text>
    <text x="110" y="135" font-family="Arial,sans-serif" font-size="6" fill="#795548" text-anchor="middle">(ксилема)</text>
    <text x="110" y="165" font-family="Arial,sans-serif" font-size="5" fill="#795548" text-anchor="middle">годичные кольца</text>
    <!-- Pith -->
    <circle cx="110" cy="120" r="15" fill="#FFF9C4" stroke="#F9A825" stroke-width="1"/>
    <text x="110" y="123" font-family="Arial,sans-serif" font-size="6" fill="#F57F17" text-anchor="middle">сердцевина</text>
    <!-- Key -->
    <g transform="translate(215,100)">
      <rect x="0" y="0" width="50" height="10" fill="#5D4037"/>
      <text x="55" y="9" font-family="Arial,sans-serif" font-size="6" fill="#5D4037">кора</text>
      <rect x="0" y="15" width="50" height="10" fill="#FF8F00"/>
      <text x="55" y="24" font-family="Arial,sans-serif" font-size="6" fill="#FF8F00">флоэма</text>
      <rect x="0" y="30" width="50" height="10" fill="#FFECB3" stroke="#795548" stroke-width="0.5"/>
      <text x="55" y="39" font-family="Arial,sans-serif" font-size="6" fill="#795548">ксилема</text>
      <rect x="0" y="45" width="50" height="10" fill="#FFF9C4" stroke="#F9A825" stroke-width="0.5"/>
      <text x="55" y="54" font-family="Arial,sans-serif" font-size="6" fill="#F57F17">сердцевина</text>
    </g>
  </g>
''' + svg_footer("Побег и стебель"))


    # Lesson 16: Лист
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Лист", f"Биология {grade} класс - Урок {n}",
        "#E8F5E9", "#C8E6C9", "#2E7D32") + '''
  <!-- Leaf structure -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="280" height="270" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="280" height="22" rx="8" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="16" width="280" height="8" fill="#2E7D32" opacity="0.9"/>
    <text x="140" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ВНЕШНЕЕ И ВНУТРЕННЕЕ СТРОЕНИЕ ЛИСТА</text>
    <!-- Leaf shape -->
    <g transform="translate(20,30)">
      <path d="M60,5 Q90,0 120,5 L110,70 Q90,90 60,70 Z" fill="#66BB6A" stroke="#2E7D32" stroke-width="1.5"/>
      <!-- Midrib -->
      <line x1="90" y1="5" x2="75" y2="70" stroke="#2E7D32" stroke-width="2"/>
      <!-- Side veins -->
      <line x1="90" y1="20" x2="55" y2="35" stroke="#2E7D32" stroke-width="1"/>
      <line x1="90" y1="20" x2="115" y2="32" stroke="#2E7D32" stroke-width="1"/>
      <line x1="85" y1="35" x2="50" y2="50" stroke="#2E7D32" stroke-width="0.8"/>
      <line x1="85" y1="35" x2="115" y2="48" stroke="#2E7D32" stroke-width="0.8"/>
      <line x1="80" y1="50" x2="55" y2="60" stroke="#2E7D32" stroke-width="0.6"/>
      <line x1="80" y1="50" x2="110" y2="60" stroke="#2E7D32" stroke-width="0.6"/>
      <!-- Petiole -->
      <line x1="90" y1="5" x2="90" y2="-15" stroke="#4CAF50" stroke-width="3"/>
      <text x="90" y="82" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">листовая пластинка</text>
      <text x="90" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#4CAF50" text-anchor="middle">черешок</text>
      <text x="58" y="40" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20">жилка</text>
    </g>
    <!-- Cross section -->
    <g transform="translate(150,30)">
      <text x="60" y="5" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Срез листа</text>
      <!-- Upper epidermis -->
      <rect x="10" y="12" width="120" height="8" rx="2" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
      <text x="135" y="20" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">верх. эпидермис</text>
      <!-- Palisade mesophyll -->
      <rect x="10" y="20" width="120" height="25" fill="#A5D6A7" stroke="#2E7D32" stroke-width="0.8"/>
      <line x1="25" y1="20" x2="25" y2="45" stroke="#4CAF50" stroke-width="1.5"/>
      <line x1="40" y1="20" x2="40" y2="45" stroke="#4CAF50" stroke-width="1.5"/>
      <line x1="55" y1="20" x2="55" y2="45" stroke="#4CAF50" stroke-width="1.5"/>
      <line x1="70" y1="20" x2="70" y2="45" stroke="#4CAF50" stroke-width="1.5"/>
      <line x1="85" y1="20" x2="85" y2="45" stroke="#4CAF50" stroke-width="1.5"/>
      <line x1="100" y1="20" x2="100" y2="45" stroke="#4CAF50" stroke-width="1.5"/>
      <line x1="115" y1="20" x2="115" y2="45" stroke="#4CAF50" stroke-width="1.5"/>
      <text x="135" y="35" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">столбч.</text>
      <text x="135" y="44" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">ткань</text>
      <!-- Spongy mesophyll -->
      <rect x="10" y="45" width="120" height="22" fill="#C8E6C9" stroke="#2E7D32" stroke-width="0.8"/>
      <circle cx="25" cy="55" r="5" fill="#DCEDC8" stroke="#66BB6A" stroke-width="0.8"/>
      <circle cx="45" cy="52" r="5" fill="#DCEDC8" stroke="#66BB6A" stroke-width="0.8"/>
      <circle cx="65" cy="56" r="5" fill="#DCEDC8" stroke="#66BB6A" stroke-width="0.8"/>
      <circle cx="85" cy="53" r="5" fill="#DCEDC8" stroke="#66BB6A" stroke-width="0.8"/>
      <circle cx="105" cy="56" r="5" fill="#DCEDC8" stroke="#66BB6A" stroke-width="0.8"/>
      <circle cx="115" cy="53" r="4" fill="#DCEDC8" stroke="#66BB6A" stroke-width="0.8"/>
      <text x="135" y="58" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">губч.</text>
      <text x="135" y="66" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">ткань</text>
      <!-- Lower epidermis -->
      <rect x="10" y="67" width="120" height="8" rx="2" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
      <text x="135" y="75" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">ниж. эпидермис</text>
      <!-- Stomata -->
      <ellipse cx="40" cy="71" rx="8" ry="3" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
      <line x1="36" y1="71" x2="44" y2="71" stroke="#1B5E20" stroke-width="0.5"/>
      <ellipse cx="90" cy="71" rx="8" ry="3" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
      <line x1="86" y1="71" x2="94" y2="71" stroke="#1B5E20" stroke-width="0.5"/>
      <text x="65" y="88" font-family="Arial,sans-serif" font-size="6" fill="#1B5E20" text-anchor="middle">устьица</text>
      <!-- Vein in section -->
      <circle cx="70" cy="35" r="5" fill="#FFECB3" stroke="#FF8F00" stroke-width="1"/>
      <circle cx="70" cy="35" r="2" fill="#8D6E63"/>
    </g>
  </g>
  <!-- Leaf types and venation -->
  <g transform="translate(310,75)">
    <rect x="0" y="0" width="275" height="135" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="16" width="275" height="8" fill="#2E7D32" opacity="0.9"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ЖИЛКОВАНИЕ И ТИПЫ ЛИСТЬЕВ</text>
    <!-- Net venation -->
    <path d="M30,40 Q45,30 60,40 Q50,60 30,55 Z" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
    <line x1="45" y1="35" x2="35" y2="52" stroke="#2E7D32" stroke-width="0.8"/>
    <line x1="45" y1="42" x2="32" y2="48" stroke="#2E7D32" stroke-width="0.4"/>
    <line x1="45" y1="42" x2="55" y2="50" stroke="#2E7D32" stroke-width="0.4"/>
    <text x="45" y="70" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">сетчатое</text>
    <!-- Parallel venation -->
    <path d="M80,40 L110,35 L115,55 L85,58 Z" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
    <line x1="88" y1="38" x2="90" y2="55" stroke="#2E7D32" stroke-width="0.4"/>
    <line x1="95" y1="37" x2="96" y2="56" stroke="#2E7D32" stroke-width="0.4"/>
    <line x1="102" y1="36" x2="103" y2="55" stroke="#2E7D32" stroke-width="0.4"/>
    <line x1="108" y1="37" x2="109" y2="54" stroke="#2E7D32" stroke-width="0.4"/>
    <text x="97" y="70" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">параллельное</text>
    <!-- Simple leaf -->
    <path d="M140,40 Q155,28 170,40 Q165,60 140,58 Z" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
    <line x1="155" y1="35" x2="152" y2="56" stroke="#2E7D32" stroke-width="1"/>
    <text x="155" y="70" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">простой</text>
    <!-- Compound leaf -->
    <line x1="210" y1="30" x2="210" y2="60" stroke="#4CAF50" stroke-width="1.5"/>
    <path d="M200,32 Q205,28 210,32 Q208,40 200,38 Z" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>
    <path d="M210,32 Q215,28 220,32 Q218,40 210,38 Z" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>
    <path d="M200,42 Q205,38 210,42 Q208,50 200,48 Z" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>
    <path d="M210,42 Q215,38 220,42 Q218,50 210,48 Z" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>
    <path d="M205,52 Q210,48 215,52 Q213,60 205,58 Z" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>
    <text x="210" y="70" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">сложный</text>
  </g>
  <!-- Leaf functions -->
  <g transform="translate(310,220)">
    <rect x="0" y="0" width="275" height="130" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#1B5E20" opacity="0.9"/>
    <rect x="0" y="16" width="275" height="8" fill="#1B5E20" opacity="0.9"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ФУНКЦИИ ЛИСТА</text>
    <text x="15" y="42" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" font-weight="bold">Фотосинтез</text>
    <text x="15" y="54" font-family="Arial,sans-serif" font-size="7" fill="#555">Создание органических веществ</text>
    <text x="15" y="68" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" font-weight="bold">Дыхание</text>
    <text x="15" y="80" font-family="Arial,sans-serif" font-size="7" fill="#555">Поглощение O2, выделение CO2</text>
    <text x="15" y="94" font-family="Arial,sans-serif" font-size="8" fill="#E65100" font-weight="bold">Испарение (транспирация)</text>
    <text x="15" y="106" font-family="Arial,sans-serif" font-size="7" fill="#555">Охлаждение и водообмен</text>
    <text x="15" y="120" font-family="Arial,sans-serif" font-size="8" fill="#7B1FA2" font-weight="bold">Листопад - приспособление к зиме</text>
  </g>
''' + svg_footer("Лист"))

    # Lesson 17: Цветок и плод
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Цветок и плод", f"Биология {grade} класс - Урок {n}",
        "#FCE4EC", "#F8BBD0", "#C2185B") + '''
  <!-- Flower structure -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="340" height="270" rx="8" fill="white" stroke="#C2185B" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="340" height="22" rx="8" fill="#C2185B" opacity="0.9"/>
    <rect x="0" y="16" width="340" height="8" fill="#C2185B" opacity="0.9"/>
    <text x="170" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">СТРОЕНИЕ ЦВЕТКА</text>
    <!-- Flower diagram -->
    <g transform="translate(130,130)">
      <!-- Peduncle -->
      <line x1="0" y1="100" x2="0" y2="70" stroke="#4CAF50" stroke-width="3"/>
      <!-- Receptacle -->
      <ellipse cx="0" cy="68" rx="12" ry="5" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
      <!-- Sepals -->
      <ellipse cx="-18" cy="55" rx="10" ry="20" fill="#4CAF50" stroke="#2E7D32" stroke-width="1" transform="rotate(-25,-18,55)"/>
      <ellipse cx="18" cy="55" rx="10" ry="20" fill="#4CAF50" stroke="#2E7D32" stroke-width="1" transform="rotate(25,18,55)"/>
      <ellipse cx="0" cy="48" rx="8" ry="18" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
      <text x="-40" y="52" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">чашелистик</text>
      <!-- Petals -->
      <ellipse cx="-30" cy="20" rx="12" ry="28" fill="#F48FB1" stroke="#E91E63" stroke-width="1" transform="rotate(-40,-30,20)"/>
      <ellipse cx="30" cy="20" rx="12" ry="28" fill="#F48FB1" stroke="#E91E63" stroke-width="1" transform="rotate(40,30,20)"/>
      <ellipse cx="-15" cy="10" rx="12" ry="28" fill="#F48FB1" stroke="#E91E63" stroke-width="1" transform="rotate(-15,-15,10)"/>
      <ellipse cx="15" cy="10" rx="12" ry="28" fill="#F48FB1" stroke="#E91E63" stroke-width="1" transform="rotate(15,15,10)"/>
      <ellipse cx="0" cy="-5" rx="10" ry="25" fill="#F48FB1" stroke="#E91E63" stroke-width="1"/>
      <text x="50" y="20" font-family="Arial,sans-serif" font-size="6" fill="#E91E63">лепесток (венчик)</text>
      <!-- Stamens -->
      <line x1="-10" y1="25" x2="-15" y2="5" stroke="#FFC107" stroke-width="1.5"/>
      <ellipse cx="-15" cy="0" rx="4" ry="6" fill="#FFD54F" stroke="#F57F17" stroke-width="1"/>
      <line x1="10" y1="25" x2="15" y2="5" stroke="#FFC107" stroke-width="1.5"/>
      <ellipse cx="15" cy="0" rx="4" ry="6" fill="#FFD54F" stroke="#F57F17" stroke-width="1"/>
      <line x1="0" y1="22" x2="0" y2="2" stroke="#FFC107" stroke-width="1.5"/>
      <ellipse cx="0" cy="-3" rx="4" ry="6" fill="#FFD54F" stroke="#F57F17" stroke-width="1"/>
      <text x="-35" y="8" font-family="Arial,sans-serif" font-size="6" fill="#F57F17">тычинка</text>
      <text x="-40" y="0" font-family="Arial,sans-serif" font-size="5" fill="#F57F17">(пыльник)</text>
      <!-- Pistil -->
      <ellipse cx="0" cy="28" rx="5" ry="8" fill="#81C784" stroke="#1B5E20" stroke-width="1.2"/>
      <line x1="0" y1="20" x2="0" y2="5" stroke="#4CAF50" stroke-width="2"/>
      <circle cx="0" cy="3" r="4" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
      <text x="25" y="30" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">пестик</text>
      <text x="25" y="22" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">рыльце</text>
      <text x="25" y="8" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">столбик</text>
      <text x="25" y="36" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">завязь</text>
    </g>
  </g>
  <!-- Fruit types -->
  <g transform="translate(370,75)">
    <rect x="0" y="0" width="215" height="270" rx="8" fill="white" stroke="#C2185B" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="215" height="22" rx="8" fill="#AD1457" opacity="0.9"/>
    <rect x="0" y="16" width="215" height="8" fill="#AD1457" opacity="0.9"/>
    <text x="108" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">МНОГООБРАЗИЕ ПЛОДОВ</text>
    <!-- Apple (pome) -->
    <circle cx="35" cy="52" r="14" fill="#EF5350" stroke="#C62828" stroke-width="1"/>
    <line x1="35" y1="38" x2="35" y2="33" stroke="#4CAF50" stroke-width="1.5"/>
    <text x="35" y="74" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">Яблоко</text>
    <!-- Plum (drupe) -->
    <ellipse cx="100" cy="50" rx="12" ry="14" fill="#7B1FA2" stroke="#4A148C" stroke-width="1"/>
    <line x1="100" y1="36" x2="100" y2="32" stroke="#4CAF50" stroke-width="1"/>
    <text x="100" y="72" font-family="Arial,sans-serif" font-size="6" fill="#4A148C" text-anchor="middle">Костянка</text>
    <!-- Pea pod (legume) -->
    <rect x="145" y="40" width="40" height="14" rx="5" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
    <circle cx="158" cy="47" r="3" fill="#8BC34A" stroke="#558B2F" stroke-width="0.5"/>
    <circle cx="170" cy="47" r="3" fill="#8BC34A" stroke="#558B2F" stroke-width="0.5"/>
    <text x="165" y="65" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Боб</text>
    <!-- Grain (caryopsis) -->
    <ellipse cx="35" cy="95" rx="8" ry="14" fill="#FFC107" stroke="#F57F17" stroke-width="1"/>
    <text x="35" y="118" font-family="Arial,sans-serif" font-size="6" fill="#F57F17" text-anchor="middle">Зерновка</text>
    <!-- Nut -->
    <circle cx="100" cy="95" r="10" fill="#8D6E63" stroke="#5D4037" stroke-width="1.5"/>
    <path d="M90,88 Q100,82 110,88" fill="#795548" stroke="#5D4037" stroke-width="1"/>
    <text x="100" y="114" font-family="Arial,sans-serif" font-size="6" fill="#5D4037" text-anchor="middle">Орех</text>
    <!-- Berry -->
    <circle cx="165" cy="95" r="10" fill="#E91E63" stroke="#AD1457" stroke-width="1"/>
    <circle cx="162" cy="92" r="1.5" fill="#FFE0B2"/>
    <circle cx="168" cy="97" r="1.5" fill="#FFE0B2"/>
    <text x="165" y="114" font-family="Arial,sans-serif" font-size="6" fill="#AD1457" text-anchor="middle">Ягода</text>
    <!-- Achene -->
    <ellipse cx="35" cy="135" rx="6" ry="10" fill="#D7CCC8" stroke="#8D6E63" stroke-width="1"/>
    <path d="M35,125 Q30,120 28,118" fill="none" stroke="#E64A19" stroke-width="0.8"/>
    <text x="35" y="155" font-family="Arial,sans-serif" font-size="6" fill="#8D6E63" text-anchor="middle">Семянка</text>
    <!-- Samara -->
    <ellipse cx="100" cy="138" rx="6" ry="5" fill="#A1887F" stroke="#795548" stroke-width="1"/>
    <path d="M106,138 Q120,130 130,135" fill="#D7CCC8" stroke="#8D6E63" stroke-width="0.8"/>
    <text x="110" y="155" font-family="Arial,sans-serif" font-size="6" fill="#795548" text-anchor="middle">Крылатка</text>
  </g>
''' + svg_footer("Цветок и плод"))

    # Lesson 18: Фотосинтез и дыхание растений
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Фотосинтез и дыхание растений", f"Биология {grade} класс - Урок {n}",
        "#E8F5E9", "#C8E6C9", "#1B5E20") + '''
  <!-- Photosynthesis diagram -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="350" height="270" rx="8" fill="white" stroke="#1B5E20" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="350" height="22" rx="8" fill="#1B5E20" opacity="0.9"/>
    <rect x="0" y="16" width="350" height="8" fill="#1B5E20" opacity="0.9"/>
    <text x="175" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ФОТОСИНТЕЗ</text>
    <!-- Leaf shape -->
    <path d="M175,40 Q220,35 260,50 Q240,140 175,160 Q110,140 90,50 Q130,35 175,40" fill="#81C784" stroke="#2E7D32" stroke-width="2"/>
    <line x1="175" y1="40" x2="175" y2="160" stroke="#2E7D32" stroke-width="1.5"/>
    <!-- Sun -->
    <circle cx="50" cy="50" r="20" fill="#FFC107" stroke="#F57F17" stroke-width="1.5"/>
    <line x1="50" y1="25" x2="50" y2="18" stroke="#FFC107" stroke-width="2"/>
    <line x1="70" y1="50" x2="77" y2="50" stroke="#FFC107" stroke-width="2"/>
    <line x1="30" y1="50" x2="23" y2="50" stroke="#FFC107" stroke-width="2"/>
    <line x1="40" y1="32" x2="35" y2="27" stroke="#FFC107" stroke-width="2"/>
    <line x1="60" y1="32" x2="65" y2="27" stroke="#FFC107" stroke-width="2"/>
    <!-- Sunlight arrow -->
    <path d="M65,55 Q90,80 120,90" fill="none" stroke="#FFC107" stroke-width="2"/>
    <polygon points="118,87 125,92 118,94" fill="#FFC107"/>
    <text x="55" y="80" font-family="Arial,sans-serif" font-size="7" fill="#F57F17" transform="rotate(30,55,80)">свет</text>
    <!-- CO2 input -->
    <text x="30" y="120" font-family="Arial,sans-serif" font-size="9" fill="#795548" font-weight="bold">CO2</text>
    <path d="M50,118 Q80,110 120,105" fill="none" stroke="#795548" stroke-width="1.5"/>
    <polygon points="118,102 125,105 118,108" fill="#795548"/>
    <!-- H2O input -->
    <text x="30" y="155" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold">H2O</text>
    <path d="M50,153 Q80,145 120,135" fill="none" stroke="#1565C0" stroke-width="1.5"/>
    <polygon points="118,132 125,135 118,138" fill="#1565C0"/>
    <!-- Inside leaf - chloroplasts -->
    <ellipse cx="175" cy="85" rx="20" ry="8" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
    <ellipse cx="155" cy="110" rx="18" ry="7" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
    <ellipse cx="195" cy="115" rx="18" ry="7" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
    <text x="175" y="88" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle">хлоропласт</text>
    <!-- O2 output -->
    <path d="M230,100 Q260,90 280,85" fill="none" stroke="#2196F3" stroke-width="1.5"/>
    <polygon points="278,82 285,84 280,89" fill="#2196F3"/>
    <text x="285" y="85" font-family="Arial,sans-serif" font-size="9" fill="#2196F3" font-weight="bold">O2</text>
    <!-- Organic matter output -->
    <path d="M200,135 Q230,150 260,155" fill="none" stroke="#FF8F00" stroke-width="1.5"/>
    <polygon points="258,152 265,155 258,158" fill="#FF8F00"/>
    <text x="268" y="150" font-family="Arial,sans-serif" font-size="8" fill="#FF8F00" font-weight="bold">C6H12O6</text>
    <text x="268" y="162" font-family="Arial,sans-serif" font-size="7" fill="#555">(глюкоза)</text>
    <!-- Equation -->
    <text x="175" y="185" font-family="Arial,sans-serif" font-size="9" fill="#1B5E20" text-anchor="middle" font-weight="bold">6CO2 + 6H2O = C6H12O6 + 6O2</text>
    <text x="175" y="200" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Свет + хлорофилл</text>
  </g>
  <!-- Respiration -->
  <g transform="translate(380,75)">
    <rect x="0" y="0" width="205" height="270" rx="8" fill="white" stroke="#C62828" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="205" height="22" rx="8" fill="#C62828" opacity="0.9"/>
    <rect x="0" y="16" width="205" height="8" fill="#C62828" opacity="0.9"/>
    <text x="103" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ДЫХАНИЕ РАСТЕНИЙ</text>
    <!-- Mitochondria -->
    <ellipse cx="103" cy="80" rx="45" ry="22" fill="#FFCDD2" stroke="#C62828" stroke-width="1.5"/>
    <path d="M65,80 Q75,70 85,80 Q95,90 105,80 Q115,70 125,80 Q135,90 140,80" fill="none" stroke="#C62828" stroke-width="1"/>
    <text x="103" y="84" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle">митохондрия</text>
    <!-- Input -->
    <text x="30" y="50" font-family="Arial,sans-serif" font-size="8" fill="#1565C0">O2</text>
    <path d="M40,52 L60,62" fill="none" stroke="#1565C0" stroke-width="1"/>
    <text x="30" y="120" font-family="Arial,sans-serif" font-size="8" fill="#FF8F00">C6H12O6</text>
    <path d="M60,118 L70,100" fill="none" stroke="#FF8F00" stroke-width="1"/>
    <!-- Output -->
    <text x="150" y="50" font-family="Arial,sans-serif" font-size="8" fill="#795548">CO2</text>
    <text x="150" y="120" font-family="Arial,sans-serif" font-size="8" fill="#1565C0">H2O</text>
    <!-- Energy -->
    <text x="103" y="140" font-family="Arial,sans-serif" font-size="9" fill="#FF8F00" text-anchor="middle" font-weight="bold">ЭНЕРГИЯ (АТФ)</text>
    <!-- Equation -->
    <text x="103" y="165" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle">C6H12O6 + 6O2 =</text>
    <text x="103" y="178" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle">6CO2 + 6H2O + энергия</text>
    <!-- Comparison -->
    <rect x="10" y="195" width="185" height="60" rx="5" fill="#FFF3E0" stroke="#E65100" stroke-width="1"/>
    <text x="103" y="210" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">Фотосинтез vs Дыхание</text>
    <text x="103" y="225" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Ф: поглощает CO2, выделяет O2</text>
    <text x="103" y="238" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Д: поглощает O2, выделяет CO2</text>
    <text x="103" y="250" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Оба процесса идут постоянно!</text>
  </g>
''' + svg_footer("Фотосинтез и дыхание растений"))

    # Lesson 19: Минеральное питание и транспорт веществ
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Минеральное питание и транспорт", f"Биология {grade} класс - Урок {n}",
        "#E3F2FD", "#BBDEFB", "#1565C0") + '''
  <!-- Water and mineral transport -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="280" height="270" rx="8" fill="white" stroke="#1565C0" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="280" height="22" rx="8" fill="#1565C0" opacity="0.9"/>
    <rect x="0" y="16" width="280" height="8" fill="#1565C0" opacity="0.9"/>
    <text x="140" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ТРАНСПОРТ ВЕЩЕСТВ</text>
    <!-- Plant with arrows -->
    <line x1="140" y1="220" x2="140" y2="60" stroke="#4CAF50" stroke-width="4"/>
    <ellipse cx="140" cy="50" rx="35" ry="20" fill="#66BB6A" stroke="#2E7D32" stroke-width="1.5"/>
    <!-- Roots -->
    <path d="M140,220 Q115,240 100,255" fill="none" stroke="#8D6E63" stroke-width="2.5"/>
    <path d="M140,220 Q165,240 180,255" fill="none" stroke="#8D6E63" stroke-width="2.5"/>
    <path d="M140,220 Q130,245 125,260" fill="none" stroke="#A1887F" stroke-width="2"/>
    <path d="M140,220 Q150,245 155,260" fill="none" stroke="#A1887F" stroke-width="2"/>
    <!-- Root hairs -->
    <line x1="100" y1="252" x2="88" y2="248" stroke="#8D6E63" stroke-width="0.8"/>
    <line x1="105" y1="258" x2="92" y2="260" stroke="#8D6E63" stroke-width="0.8"/>
    <line x1="180" y1="252" x2="192" y2="248" stroke="#8D6E63" stroke-width="0.8"/>
    <line x1="175" y1="258" x2="188" y2="260" stroke="#8D6E63" stroke-width="0.8"/>
    <!-- Soil -->
    <rect x="50" y="240" width="180" height="30" rx="3" fill="#D7CCC8" stroke="#8D6E63" stroke-width="1"/>
    <text x="140" y="260" font-family="Arial,sans-serif" font-size="6" fill="#5D4037" text-anchor="middle">почва + минеральные соли</text>
    <!-- Upward flow (xylem) - blue arrows -->
    <path d="M130,230 L130,70" fill="none" stroke="#2196F3" stroke-width="2.5"/>
    <polygon points="127,72 130,62 133,72" fill="#2196F3"/>
    <text x="110" y="150" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="end">ксилема</text>
    <text x="110" y="160" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="end">вода+минер.</text>
    <!-- Downward flow (phloem) - orange arrows -->
    <path d="M150,70 L150,230" fill="none" stroke="#FF8F00" stroke-width="2.5"/>
    <polygon points="147,228 150,238 153,228" fill="#FF8F00"/>
    <text x="170" y="150" font-family="Arial,sans-serif" font-size="7" fill="#FF8F00">флоэма</text>
    <text x="170" y="160" font-family="Arial,sans-serif" font-size="6" fill="#FF8F00">орг. вещества</text>
    <!-- Leaf labels -->
    <text x="140" y="32" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">испарение воды</text>
  </g>
  <!-- Mineral elements -->
  <g transform="translate(310,75)">
    <rect x="0" y="0" width="275" height="270" rx="8" fill="white" stroke="#1565C0" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#1565C0" opacity="0.9"/>
    <rect x="0" y="16" width="275" height="8" fill="#1565C0" opacity="0.9"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">МИНЕРАЛЬНЫЕ ЭЛЕМЕНТЫ</text>
    <!-- Macro elements -->
    <text x="138" y="42" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" text-anchor="middle" font-weight="bold">Макроэлементы</text>
    <rect x="10" y="50" width="55" height="35" rx="5" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
    <text x="38" y="67" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" text-anchor="middle" font-weight="bold">N</text>
    <text x="38" y="80" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Азот</text>
    <rect x="72" y="50" width="55" height="35" rx="5" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
    <text x="100" y="67" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" text-anchor="middle" font-weight="bold">P</text>
    <text x="100" y="80" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Фосфор</text>
    <rect x="134" y="50" width="55" height="35" rx="5" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
    <text x="162" y="67" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" text-anchor="middle" font-weight="bold">K</text>
    <text x="162" y="80" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Калий</text>
    <rect x="196" y="50" width="55" height="35" rx="5" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
    <text x="224" y="67" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" text-anchor="middle" font-weight="bold">Ca</text>
    <text x="224" y="80" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Кальций</text>
    <!-- Functions -->
    <text x="138" y="100" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" text-anchor="middle" font-weight="bold">Значение элементов</text>
    <text x="15" y="115" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" font-weight="bold">N</text>
    <text x="30" y="115" font-family="Arial,sans-serif" font-size="7" fill="#555">- рост, белки, хлорофилл</text>
    <text x="15" y="130" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" font-weight="bold">P</text>
    <text x="30" y="130" font-family="Arial,sans-serif" font-size="7" fill="#555">- энергетический обмен, ДНК</text>
    <text x="15" y="145" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" font-weight="bold">K</text>
    <text x="30" y="145" font-family="Arial,sans-serif" font-size="7" fill="#555">- осмотическое давление, ферменты</text>
    <text x="15" y="160" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" font-weight="bold">Ca</text>
    <text x="30" y="160" font-family="Arial,sans-serif" font-size="7" fill="#555">- клеточная стенка, рост</text>
    <!-- Micro elements -->
    <text x="138" y="180" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" text-anchor="middle" font-weight="bold">Микроэлементы</text>
    <rect x="15" y="188" width="35" height="20" rx="3" fill="#FFF3E0" stroke="#E65100" stroke-width="1"/>
    <text x="33" y="202" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle">Fe</text>
    <rect x="55" y="188" width="35" height="20" rx="3" fill="#FFF3E0" stroke="#E65100" stroke-width="1"/>
    <text x="73" y="202" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle">Cu</text>
    <rect x="95" y="188" width="35" height="20" rx="3" fill="#FFF3E0" stroke="#E65100" stroke-width="1"/>
    <text x="113" y="202" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle">Zn</text>
    <rect x="135" y="188" width="35" height="20" rx="3" fill="#FFF3E0" stroke="#E65100" stroke-width="1"/>
    <text x="153" y="202" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle">Mn</text>
    <rect x="175" y="188" width="35" height="20" rx="3" fill="#FFF3E0" stroke="#E65100" stroke-width="1"/>
    <text x="193" y="202" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle">B</text>
    <!-- Fertilizers -->
    <text x="138" y="225" font-family="Arial,sans-serif" font-size="9" fill="#795548" text-anchor="middle" font-weight="bold">Удобрения</text>
    <rect x="15" y="235" width="120" height="25" rx="4" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
    <text x="75" y="252" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Органические (навоз, торф)</text>
    <rect x="145" y="235" width="120" height="25" rx="4" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
    <text x="205" y="252" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle">Минеральные (NPK)</text>
  </g>
''' + svg_footer("Минеральное питание и транспорт"))


    # Lesson 20: Рост и развитие растений
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Рост и развитие растений", f"Биология {grade} класс - Урок {n}",
        "#E8F5E9", "#C8E6C9", "#2E7D32") + '''
  <!-- Plant growth stages -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="570" height="270" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="570" height="22" rx="8" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="16" width="570" height="8" fill="#2E7D32" opacity="0.9"/>
    <text x="285" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">РОСТ И РАЗВИТИЕ РАСТЕНИЙ</text>
    <!-- Seed -->
    <g transform="translate(30,40)">
      <ellipse cx="30" cy="60" rx="22" ry="15" fill="#8D6E63" stroke="#5D4037" stroke-width="1.5"/>
      <ellipse cx="30" cy="60" rx="14" ry="9" fill="#FFECB3" stroke="#FF8F00" stroke-width="1"/>
      <ellipse cx="28" cy="58" rx="5" ry="4" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>
      <text x="30" y="85" font-family="Arial,sans-serif" font-size="7" fill="#5D4037" text-anchor="middle">Семя</text>
    </g>
    <!-- Arrow -->
    <path d="M85,100 L100,100" stroke="#2E7D32" stroke-width="1.5"/>
    <polygon points="98,97 104,100 98,103" fill="#2E7D32"/>
    <!-- Sprouting -->
    <g transform="translate(110,40)">
      <ellipse cx="20" cy="75" rx="15" ry="10" fill="#D7CCC8" stroke="#8D6E63" stroke-width="1"/>
      <line x1="20" y1="68" x2="20" y2="40" stroke="#4CAF50" stroke-width="2"/>
      <path d="M20,40 Q15,30 10,25" fill="none" stroke="#4CAF50" stroke-width="2"/>
      <path d="M20,45 Q28,35 35,30" fill="none" stroke="#4CAF50" stroke-width="1.5"/>
      <line x1="20" y1="85" x2="20" y2="100" stroke="#8D6E63" stroke-width="1.5"/>
      <text x="20" y="115" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Проросток</text>
    </g>
    <!-- Arrow -->
    <path d="M175,100 L190,100" stroke="#2E7D32" stroke-width="1.5"/>
    <polygon points="188,97 194,100 188,103" fill="#2E7D32"/>
    <!-- Young plant -->
    <g transform="translate(200,35)">
      <rect x="28" y="50" width="6" height="55" rx="1" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
      <path d="M31,50 Q20,40 15,30" fill="none" stroke="#66BB6A" stroke-width="2"/>
      <path d="M31,55 Q42,45 47,35" fill="none" stroke="#66BB6A" stroke-width="2"/>
      <path d="M31,65 Q18,55 12,48" fill="none" stroke="#66BB6A" stroke-width="1.5"/>
      <path d="M31,70 Q44,60 50,52" fill="none" stroke="#66BB6A" stroke-width="1.5"/>
      <line x1="31" y1="105" x2="31" y2="125" stroke="#8D6E63" stroke-width="2"/>
      <line x1="31" y1="115" x2="18" y2="125" stroke="#8D6E63" stroke-width="1.5"/>
      <line x1="31" y1="115" x2="44" y2="125" stroke="#8D6E63" stroke-width="1.5"/>
      <text x="31" y="140" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Росток</text>
    </g>
    <!-- Arrow -->
    <path d="M280,100 L295,100" stroke="#2E7D32" stroke-width="1.5"/>
    <polygon points="293,97 299,100 293,103" fill="#2E7D32"/>
    <!-- Vegetative -->
    <g transform="translate(305,25)">
      <rect x="35" y="45" width="8" height="70" rx="2" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
      <ellipse cx="39" cy="38" rx="20" ry="15" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
      <path d="M35,60 Q15,50 10,40" fill="none" stroke="#66BB6A" stroke-width="2.5"/>
      <path d="M43,60 Q63,50 68,40" fill="none" stroke="#66BB6A" stroke-width="2.5"/>
      <path d="M35,75 Q18,65 12,58" fill="none" stroke="#66BB6A" stroke-width="2"/>
      <path d="M43,75 Q60,65 66,58" fill="none" stroke="#66BB6A" stroke-width="2"/>
      <line x1="39" y1="115" x2="39" y2="140" stroke="#8D6E63" stroke-width="3"/>
      <line x1="39" y1="130" x2="22" y2="145" stroke="#8D6E63" stroke-width="2"/>
      <line x1="39" y1="130" x2="56" y2="145" stroke="#8D6E63" stroke-width="2"/>
      <text x="39" y="158" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Вегетативное</text>
    </g>
    <!-- Arrow -->
    <path d="M395,100 L410,100" stroke="#C2185B" stroke-width="1.5"/>
    <polygon points="408,97 414,100 408,103" fill="#C2185B"/>
    <!-- Flowering -->
    <g transform="translate(420,20)">
      <rect x="35" y="50" width="8" height="70" rx="2" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
      <path d="M35,65 Q15,55 10,45" fill="none" stroke="#66BB6A" stroke-width="2.5"/>
      <path d="M43,65 Q63,55 68,45" fill="none" stroke="#66BB6A" stroke-width="2.5"/>
      <path d="M35,80 Q20,72 15,65" fill="none" stroke="#66BB6A" stroke-width="2"/>
      <path d="M43,80 Q58,72 63,65" fill="none" stroke="#66BB6A" stroke-width="2"/>
      <!-- Flower -->
      <ellipse cx="39" cy="35" rx="10" ry="7" fill="#F48FB1" stroke="#E91E63" stroke-width="1" transform="rotate(-30,39,35)"/>
      <ellipse cx="39" cy="35" rx="10" ry="7" fill="#F48FB1" stroke="#E91E63" stroke-width="1" transform="rotate(30,39,35)"/>
      <ellipse cx="39" cy="30" rx="8" ry="6" fill="#F48FB1" stroke="#E91E63" stroke-width="1"/>
      <circle cx="39" cy="35" r="5" fill="#FFC107" stroke="#F57F17" stroke-width="0.8"/>
      <line x1="39" y1="120" x2="39" y2="145" stroke="#8D6E63" stroke-width="3"/>
      <text x="39" y="160" font-family="Arial,sans-serif" font-size="7" fill="#C2185B" text-anchor="middle">Генеративное</text>
    </g>
    <!-- Growth types info -->
    <text x="285" y="240" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Рост: верхушечный (камбий) и вставочный</text>
    <text x="285" y="255" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Развитие: от прорастания до плодоношения</text>
  </g>
''' + svg_footer("Рост и развитие растений"))

    # Lesson 21: Вегетативное размножение растений
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Вегетативное размножение растений", f"Биология {grade} класс - Урок {n}",
        "#E8F5E9", "#C8E6C9", "#2E7D32") + '''
  <!-- Vegetative reproduction methods -->
  <g transform="translate(15,75)">
    <!-- By stem cuttings -->
    <rect x="0" y="0" width="180" height="130" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="180" height="22" rx="8" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="16" width="180" height="8" fill="#2E7D32" opacity="0.9"/>
    <text x="90" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">СТЕБЛЕВЫМИ ЧЕРЕНКАМИ</text>
    <line x1="60" y1="35" x2="60" y2="85" stroke="#4CAF50" stroke-width="2.5"/>
    <path d="M60,50 Q50,45 45,50" fill="none" stroke="#66BB6A" stroke-width="1.5"/>
    <path d="M60,65 Q70,60 75,65" fill="none" stroke="#66BB6A" stroke-width="1.5"/>
    <line x1="60" y1="85" x2="50" y2="100" stroke="#8D6E63" stroke-width="1"/>
    <line x1="60" y1="85" x2="70" y2="100" stroke="#8D6E63" stroke-width="1"/>
    <rect x="40" y="98" width="40" height="20" rx="2" fill="#D7CCC8" stroke="#8D6E63" stroke-width="0.8"/>
    <text x="90" y="110" font-family="Arial,sans-serif" font-size="7" fill="#555">черенок в почве</text>
    <text x="130" y="55" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">корни</text>
    <text x="130" y="70" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">почки</text>
  </g>
  <!-- By runners -->
  <g transform="translate(205,75)">
    <rect x="0" y="0" width="180" height="130" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="180" height="22" rx="8" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="16" width="180" height="8" fill="#2E7D32" opacity="0.9"/>
    <text x="90" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">УСАМИ (СТОЛАНАМИ)</text>
    <!-- Mother plant -->
    <ellipse cx="35" cy="70" rx="20" ry="12" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
    <line x1="35" y1="82" x2="35" y2="95" stroke="#8D6E63" stroke-width="1.5"/>
    <!-- Runner -->
    <path d="M55,75 Q80,85 105,80" fill="none" stroke="#4CAF50" stroke-width="2"/>
    <!-- Daughter plant -->
    <ellipse cx="115" cy="75" rx="18" ry="10" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
    <line x1="115" y1="85" x2="115" y2="95" stroke="#8D6E63" stroke-width="1.5"/>
    <line x1="115" y1="95" x2="108" y2="105" stroke="#8D6E63" stroke-width="1"/>
    <line x1="115" y1="95" x2="122" y2="105" stroke="#8D6E63" stroke-width="1"/>
    <!-- Another runner -->
    <path d="M55,80 Q80,95 140,85" fill="none" stroke="#4CAF50" stroke-width="1.5"/>
    <ellipse cx="150" cy="82" rx="15" ry="9" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
    <text x="90" y="120" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">клубника, земляника</text>
  </g>
  <!-- By tubers and bulbs -->
  <g transform="translate(395,75)">
    <rect x="0" y="0" width="190" height="130" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="190" height="22" rx="8" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="16" width="190" height="8" fill="#2E7D32" opacity="0.9"/>
    <text x="95" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">КЛУБНЯМИ И ЛУКОВИЦАМИ</text>
    <!-- Potato tuber -->
    <ellipse cx="50" cy="65" rx="22" ry="16" fill="#FFCC80" stroke="#E65100" stroke-width="1.5"/>
    <circle cx="40" cy="58" r="3" fill="#D7CCC8" stroke="#8D6E63" stroke-width="0.8"/>
    <circle cx="55" cy="60" r="3" fill="#D7CCC8" stroke="#8D6E63" stroke-width="0.8"/>
    <circle cx="48" cy="72" r="3" fill="#D7CCC8" stroke="#8D6E63" stroke-width="0.8"/>
    <text x="40" y="57" font-family="Arial,sans-serif" font-size="4" fill="#5D4037">Г</text>
    <text x="55" y="59" font-family="Arial,sans-serif" font-size="4" fill="#5D4037">Г</text>
    <text x="48" y="71" font-family="Arial,sans-serif" font-size="4" fill="#5D4037">Г</text>
    <text x="50" y="95" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle">Клубень (картофель)</text>
    <text x="50" y="105" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Г = глазки (почки)</text>
    <!-- Bulb -->
    <ellipse cx="140" cy="60" rx="16" ry="22" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/>
    <ellipse cx="140" cy="55" rx="10" ry="6" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.8"/>
    <line x1="140" y1="38" x2="140" y2="30" stroke="#4CAF50" stroke-width="2"/>
    <text x="140" y="95" font-family="Arial,sans-serif" font-size="7" fill="#F9A825" text-anchor="middle">Луковица (лук)</text>
  </g>
  <!-- Other methods -->
  <g transform="translate(15,218)">
    <rect x="0" y="0" width="570" height="130" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="570" height="22" rx="8" fill="#1B5E20" opacity="0.9"/>
    <rect x="0" y="16" width="570" height="8" fill="#1B5E20" opacity="0.9"/>
    <text x="285" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ДРУГИЕ СПОСОБЫ И ЗНАЧЕНИЕ</text>
    <!-- Grafting -->
    <g transform="translate(20,30)">
      <line x1="20" y1="10" x2="20" y2="60" stroke="#8D6E63" stroke-width="3"/>
      <line x1="20" y1="25" x2="20" y2="5" stroke="#4CAF50" stroke-width="2.5"/>
      <line x1="20" y1="15" x2="10" y2="8" stroke="#4CAF50" stroke-width="1.5"/>
      <line x1="20" y1="20" x2="30" y2="13" stroke="#4CAF50" stroke-width="1.5"/>
      <text x="20" y="75" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Прививка</text>
      <text x="20" y="85" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">подвой+привой</text>
    </g>
    <!-- Rhizome -->
    <g transform="translate(100,30)">
      <path d="M5,40 Q25,35 45,40 Q65,45 85,40" fill="none" stroke="#8D6E63" stroke-width="3"/>
      <line x1="25" y1="35" x2="25" y2="20" stroke="#4CAF50" stroke-width="2"/>
      <ellipse cx="25" cy="17" rx="8" ry="5" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
      <line x1="65" y1="38" x2="65" y2="22" stroke="#4CAF50" stroke-width="2"/>
      <ellipse cx="65" cy="19" rx="8" ry="5" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
      <text x="45" y="58" font-family="Arial,sans-serif" font-size="7" fill="#795548" text-anchor="middle">Корневище</text>
      <text x="45" y="68" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">пырей, ирис</text>
    </g>
    <!-- Leaf cutting -->
    <g transform="translate(220,30)">
      <ellipse cx="25" cy="20" rx="18" ry="10" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
      <line x1="25" y1="30" x2="25" y2="60" stroke="#4CAF50" stroke-width="1.5"/>
      <line x1="25" y1="50" x2="15" y2="60" stroke="#8D6E63" stroke-width="1"/>
      <line x1="25" y1="50" x2="35" y2="60" stroke="#8D6E63" stroke-width="1"/>
      <rect x="15" y="58" width="20" height="12" rx="2" fill="#D7CCC8"/>
      <text x="25" y="82" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Листовой черенок</text>
      <text x="25" y="92" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">фиалка, бегония</text>
    </g>
    <!-- Advantages -->
    <g transform="translate(340,28)">
      <text x="110" y="10" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold">Преимущества вегетативного размножения:</text>
      <text x="10" y="28" font-family="Arial,sans-serif" font-size="8" fill="#555">Быстрое получение взрослого растения</text>
      <text x="10" y="42" font-family="Arial,sans-serif" font-size="8" fill="#555">Сохранение признаков материнского растения</text>
      <text x="10" y="56" font-family="Arial,sans-serif" font-size="8" fill="#555">Не нужно опыление</text>
      <text x="10" y="72" font-family="Arial,sans-serif" font-size="9" fill="#C62828" font-weight="bold">Недостаток:</text>
      <text x="10" y="86" font-family="Arial,sans-serif" font-size="8" fill="#555">Малая изменчивость, нет приспособления</text>
    </g>
  </g>
''' + svg_footer("Вегетативное размножение растений"))

    # Lesson 22: Семенное размножение и прорастание семян
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Семенное размножение и прорастание семян", f"Биология {grade} класс - Урок {n}",
        "#FFF3E0", "#FFE0B2", "#795548") + '''
  <!-- Seed structure -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="280" height="270" rx="8" fill="white" stroke="#795548" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="280" height="22" rx="8" fill="#795548" opacity="0.9"/>
    <rect x="0" y="16" width="280" height="8" fill="#795548" opacity="0.9"/>
    <text x="140" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">СТРОЕНИЕ СЕМЕНИ</text>
    <!-- Bean seed (dicot) -->
    <text x="140" y="40" font-family="Arial,sans-serif" font-size="9" fill="#795548" text-anchor="middle" font-weight="bold">Фасоль (двудольное)</text>
    <ellipse cx="90" cy="100" rx="50" ry="35" fill="#D7CCC8" stroke="#795548" stroke-width="2"/>
    <text x="90" y="60" font-family="Arial,sans-serif" font-size="6" fill="#795548" text-anchor="middle">семенная кожура</text>
    <!-- Two cotyledons -->
    <path d="M55,80 Q70,65 90,80 L90,120 Q70,135 55,120 Z" fill="#FFECB3" stroke="#FF8F00" stroke-width="1.5"/>
    <path d="M90,80 Q110,65 125,80 L125,120 Q110,135 90,120 Z" fill="#FFE0B2" stroke="#FF8F00" stroke-width="1.5"/>
    <text x="72" y="105" font-family="Arial,sans-serif" font-size="6" fill="#FF8F00" text-anchor="middle">семя-</text>
    <text x="72" y="114" font-family="Arial,sans-serif" font-size="6" fill="#FF8F00" text-anchor="middle">доля 1</text>
    <text x="108" y="105" font-family="Arial,sans-serif" font-size="6" fill="#FF8F00" text-anchor="middle">семя-</text>
    <text x="108" y="114" font-family="Arial,sans-serif" font-size="6" fill="#FF8F00" text-anchor="middle">доля 2</text>
    <!-- Embryo -->
    <g transform="translate(90,92)">
      <line x1="0" y1="0" x2="0" y2="-12" stroke="#4CAF50" stroke-width="1.5"/>
      <ellipse cx="0" cy="-14" rx="4" ry="3" fill="#81C784" stroke="#2E7D32" stroke-width="0.8"/>
      <text x="8" y="-10" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">почечка</text>
      <line x1="0" y1="0" x2="0" y2="12" stroke="#8D6E63" stroke-width="1.5"/>
      <text x="8" y="10" font-family="Arial,sans-serif" font-size="5" fill="#8D6E63">корешок</text>
      <line x1="0" y1="0" x2="12" y2="0" stroke="#4CAF50" stroke-width="1"/>
      <text x="14" y="0" font-family="Arial,sans-serif" font-size="5" fill="#4CAF50">стебелёк</text>
    </g>
    <!-- Corn seed (monocot) -->
    <text x="140" y="155" font-family="Arial,sans-serif" font-size="9" fill="#795548" text-anchor="middle" font-weight="bold">Пшеница (однодольное)</text>
    <ellipse cx="90" cy="210" rx="40" ry="25" fill="#FFC107" stroke="#F57F17" stroke-width="2"/>
    <ellipse cx="80" cy="210" rx="12" ry="15" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
    <text x="80" y="213" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle">зародыш</text>
    <text x="110" y="205" font-family="Arial,sans-serif" font-size="6" fill="#F57F17" text-anchor="middle">эндо-</text>
    <text x="110" y="214" font-family="Arial,sans-serif" font-size="6" fill="#F57F17" text-anchor="middle">сперм</text>
    <rect x="50" y="185" width="80" height="5" rx="1" fill="#D7CCC8" stroke="#8D6E63" stroke-width="0.8"/>
    <text x="90" y="183" font-family="Arial,sans-serif" font-size="5" fill="#795548" text-anchor="middle">семенная кожура + плодовая оболочка</text>
    <!-- Shield -->
    <line x1="90" y1="208" x2="92" y2="208" stroke="#2E7D32" stroke-width="1"/>
    <text x="98" y="225" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">щиток</text>
  </g>
  <!-- Germination conditions -->
  <g transform="translate(310,75)">
    <rect x="0" y="0" width="275" height="135" rx="8" fill="white" stroke="#795548" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#795548" opacity="0.9"/>
    <rect x="0" y="16" width="275" height="8" fill="#795548" opacity="0.9"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">УСЛОВИЯ ПРОРАСТАНИЯ</text>
    <!-- Water -->
    <circle cx="55" cy="65" r="25" fill="#BBDEFB" stroke="#1565C0" stroke-width="1.5"/>
    <path d="M42,65 Q55,45 68,65 Q55,75 42,65" fill="#42A5F5" opacity="0.5"/>
    <text x="55" y="98" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" text-anchor="middle">Вода</text>
    <!-- Temperature -->
    <circle cx="138" cy="65" r="25" fill="#FFCDD2" stroke="#C62828" stroke-width="1.5"/>
    <text x="138" y="62" font-family="Arial,sans-serif" font-size="16" fill="#C62828" text-anchor="middle">&#176;</text>
    <text x="138" y="98" font-family="Arial,sans-serif" font-size="8" fill="#C62828" text-anchor="middle">Тепло</text>
    <!-- Air -->
    <circle cx="220" cy="65" r="25" fill="#E3F2FD" stroke="#90CAF9" stroke-width="1.5"/>
    <text x="220" y="68" font-family="Arial,sans-serif" font-size="10" fill="#90CAF9" text-anchor="middle">O2</text>
    <text x="220" y="98" font-family="Arial,sans-serif" font-size="8" fill="#90CAF9" text-anchor="middle">Воздух</text>
  </g>
  <!-- Pollination and fertilization -->
  <g transform="translate(310,220)">
    <rect x="0" y="0" width="275" height="130" rx="8" fill="white" stroke="#C2185B" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#C2185B" opacity="0.9"/>
    <rect x="0" y="16" width="275" height="8" fill="#C2185B" opacity="0.9"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ДВОЙНОЕ ОПЛОДОТВОРЕНИЕ</text>
    <text x="138" y="42" font-family="Arial,sans-serif" font-size="8" fill="#C2185B" text-anchor="middle" font-weight="bold">Особенность покрытосеменных!</text>
    <text x="15" y="60" font-family="Arial,sans-serif" font-size="7" fill="#555">1 спермий + яйцеклетка = зародыш (2n)</text>
    <text x="15" y="75" font-family="Arial,sans-serif" font-size="7" fill="#555">2 спермий + центральная клетка = эндосперм (3n)</text>
    <text x="15" y="95" font-family="Arial,sans-serif" font-size="8" fill="#795548" font-weight="bold">Опыление:</text>
    <text x="15" y="108" font-family="Arial,sans-serif" font-size="7" fill="#555">Насекомыми (яркие цветки, нектар)</text>
    <text x="15" y="121" font-family="Arial,sans-serif" font-size="7" fill="#555">Ветром (много пыльцы, мелкая)</text>
  </g>
''' + svg_footer("Семенное размножение и прорастание семян"))

    # Lesson 23: Природные сообщества и взаимосвязи организмов
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Природные сообщества", f"Биология {grade} класс - Урок {n}",
        "#E8F5E9", "#C8E6C9", "#2E7D32") + '''
  <!-- Ecosystem -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="570" height="270" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="570" height="22" rx="8" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="16" width="570" height="8" fill="#2E7D32" opacity="0.9"/>
    <text x="285" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ПРИРОДНОЕ СООБЩЕСТВО (БИОЦЕНОЗ)</text>
    <!-- Sun -->
    <circle cx="50" cy="50" r="18" fill="#FFC107" stroke="#F57F17" stroke-width="1.5"/>
    <line x1="50" y1="28" x2="50" y2="22" stroke="#FFC107" stroke-width="1.5"/>
    <line x1="68" y1="50" x2="74" y2="50" stroke="#FFC107" stroke-width="1.5"/>
    <!-- Producers -->
    <text x="180" y="50" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold">Продуценты</text>
    <text x="180" y="62" font-family="Arial,sans-serif" font-size="7" fill="#555">(растения - фотосинтез)</text>
    <!-- Tree -->
    <rect x="90" y="100" width="10" height="50" rx="2" fill="#795548"/>
    <ellipse cx="95" cy="85" rx="22" ry="20" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
    <!-- Grass -->
    <line x1="140" y1="150" x2="135" y2="125" stroke="#66BB6A" stroke-width="2"/>
    <line x1="145" y1="150" x2="148" y2="128" stroke="#66BB6A" stroke-width="2"/>
    <line x1="150" y1="150" x2="155" y2="130" stroke="#66BB6A" stroke-width="2"/>
    <!-- Bush -->
    <rect x="170" y="120" width="6" height="30" rx="1" fill="#795548"/>
    <ellipse cx="173" cy="112" rx="16" ry="12" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
    <!-- Arrow to consumers -->
    <path d="M120,155 L120,170" stroke="#E65100" stroke-width="2"/>
    <polygon points="117,168 120,175 123,168" fill="#E65100"/>
    <!-- Consumers -->
    <text x="350" y="50" font-family="Arial,sans-serif" font-size="9" fill="#E65100" font-weight="bold">Консументы</text>
    <text x="350" y="62" font-family="Arial,sans-serif" font-size="7" fill="#555">(животные - гетеротрофы)</text>
    <!-- Herbivore - rabbit -->
    <ellipse cx="95" cy="195" rx="20" ry="14" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
    <circle cx="78" cy="188" r="10" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
    <circle cx="75" cy="186" r="2" fill="#333"/>
    <ellipse cx="70" cy="180" rx="4" ry="6" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
    <!-- Predator - fox -->
    <ellipse cx="200" cy="195" rx="25" ry="14" fill="#FF8A65" stroke="#E64A19" stroke-width="1"/>
    <circle cx="178" cy="186" r="10" fill="#FF8A65" stroke="#E64A19" stroke-width="1"/>
    <polygon points="172,178 174,186 168,182" fill="#FF8A65" stroke="#E64A19" stroke-width="0.8"/>
    <polygon points="182,178 184,186 188,182" fill="#FF8A65" stroke="#E64A19" stroke-width="0.8"/>
    <circle cx="175" cy="184" r="2" fill="#333"/>
    <path d="M225,190 Q235,185 240,192" fill="none" stroke="#E64A19" stroke-width="3"/>
    <!-- Bird -->
    <ellipse cx="290" cy="190" rx="12" ry="8" fill="#90CAF9" stroke="#1565C0" stroke-width="1"/>
    <circle cx="281" cy="187" r="5" fill="#90CAF9" stroke="#1565C0" stroke-width="1"/>
    <circle cx="279" cy="186" r="1.5" fill="#333"/>
    <path d="M302,190 Q310,185 315,190" fill="none" stroke="#1565C0" stroke-width="1.5"/>
    <!-- Arrow to decomposers -->
    <path d="M200,212 L200,228" stroke="#795548" stroke-width="2"/>
    <polygon points="197,226 200,233 203,226" fill="#795548"/>
    <!-- Decomposers -->
    <text x="430" y="50" font-family="Arial,sans-serif" font-size="9" fill="#795548" font-weight="bold">Редуценты</text>
    <text x="430" y="62" font-family="Arial,sans-serif" font-size="7" fill="#555">(бактерии, грибы)</text>
    <!-- Mushroom -->
    <rect x="295" y="248" width="6" height="15" rx="1" fill="#D7CCC8" stroke="#8D6E63" stroke-width="1"/>
    <ellipse cx="298" cy="245" rx="14" ry="8" fill="#FF8A65" stroke="#E64A19" stroke-width="1"/>
    <!-- Bacteria -->
    <circle cx="340" cy="252" r="5" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
    <circle cx="350" cy="250" r="4" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
    <circle cx="355" cy="256" r="4" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
    <!-- Dead matter -->
    <rect x="270" y="232" width="110" height="10" rx="2" fill="#8D6E63" opacity="0.5"/>
    <text x="325" y="240" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle">остатки организмов</text>
    <!-- Nutrient cycle arrow -->
    <path d="M380,250 Q400,200 380,100 Q360,40 100,40" fill="none" stroke="#2E7D32" stroke-width="1.5" stroke-dasharray="5,3"/>
    <polygon points="102,37 95,40 102,43" fill="#2E7D32"/>
    <text x="410" y="140" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">минеральные</text>
    <text x="410" y="150" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">вещества</text>
  </g>
''' + svg_footer("Природные сообщества и взаимосвязи организмов"))

    counts[grade] = n
    print(f"Grade {grade}: {n} SVGs generated")


#############################
# GRADE 7: Животные (32 lessons)
#############################
def gen_grade7():
    grade = 7
    n = 0

    # Lesson 1: Общая характеристика животных
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Общая характеристика животных", f"Биология {grade} класс - Урок {n}",
        "#FFF3E0", "#FFE0B2", "#E65100") + '''
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="280" height="270" rx="8" fill="white" stroke="#E65100" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="280" height="22" rx="8" fill="#E65100" opacity="0.9"/>
    <rect x="0" y="16" width="280" height="8" fill="#E65100" opacity="0.9"/>
    <text x="140" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ПРИЗНАКИ ЖИВОТНЫХ</text>
    <text x="15" y="42" font-family="Arial,sans-serif" font-size="8" fill="#E65100" font-weight="bold">Гетеротрофы - потребляют пищу</text>
    <text x="15" y="56" font-family="Arial,sans-serif" font-size="8" fill="#555">Активно двигаются</text>
    <text x="15" y="70" font-family="Arial,sans-serif" font-size="8" fill="#555">Рост ограничен</text>
    <text x="15" y="84" font-family="Arial,sans-serif" font-size="8" fill="#555">Запас гликогена</text>
    <text x="15" y="98" font-family="Arial,sans-serif" font-size="8" fill="#555">Нет клеточной стенки</text>
    <!-- Animal cell -->
    <text x="140" y="120" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">Клетка животного</text>
    <ellipse cx="140" cy="175" rx="55" ry="40" fill="#FFECB3" stroke="#E65100" stroke-width="1.5"/>
    <ellipse cx="140" cy="170" rx="18" ry="12" fill="#FFCC80" stroke="#BF360C" stroke-width="1.2"/>
    <text x="140" y="174" font-family="Arial,sans-serif" font-size="6" fill="#BF360C" text-anchor="middle">ядро</text>
    <ellipse cx="110" cy="185" rx="12" ry="5" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
    <path d="M100,185 Q106,180 112,185 Q118,190 124,185" fill="none" stroke="#E65100" stroke-width="0.6"/>
    <text x="110" y="198" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">митох.</text>
    <circle cx="165" cy="160" r="4" fill="#EF9A9A" stroke="#C62828" stroke-width="0.6"/>
    <circle cx="170" cy="168" r="3" fill="#EF9A9A" stroke="#C62828" stroke-width="0.6"/>
    <circle cx="160" cy="190" r="3" fill="#EF9A9A" stroke="#C62828" stroke-width="0.6"/>
    <text x="175" y="192" font-family="Arial,sans-serif" font-size="5" fill="#C62828">риб.</text>
    <!-- No cell wall label -->
    <text x="140" y="228" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle">Нет клеточной стенки и пластид!</text>
  </g>
  <!-- Classification -->
  <g transform="translate(310,75)">
    <rect x="0" y="0" width="275" height="270" rx="8" fill="white" stroke="#E65100" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#BF360C" opacity="0.9"/>
    <rect x="0" y="16" width="275" height="8" fill="#BF360C" opacity="0.9"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">КЛАССИФИКАЦИЯ ЖИВОТНЫХ</text>
    <!-- Tree of animal kingdoms -->
    <rect x="95" y="30" width="85" height="18" rx="4" fill="#E65100" opacity="0.8"/>
    <text x="138" y="43" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle" font-weight="bold">Животные</text>
    <line x1="110" y1="48" x2="60" y2="60" stroke="#E65100" stroke-width="1"/>
    <line x1="138" y1="48" x2="138" y2="60" stroke="#E65100" stroke-width="1"/>
    <line x1="165" y1="48" x2="215" y2="60" stroke="#E65100" stroke-width="1"/>
    <rect x="20" y="60" width="75" height="16" rx="3" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
    <text x="58" y="72" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Простейшие</text>
    <rect x="100" y="60" width="75" height="16" rx="3" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
    <text x="138" y="72" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Кишечнополостные</text>
    <rect x="180" y="60" width="75" height="16" rx="3" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
    <text x="218" y="72" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Черви</text>
    <!-- More branches -->
    <rect x="5" y="90" width="70" height="16" rx="3" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
    <text x="40" y="102" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Моллюски</text>
    <rect x="80" y="90" width="70" height="16" rx="3" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
    <text x="115" y="102" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Членистоногие</text>
    <rect x="155" y="90" width="55" height="16" rx="3" fill="#FFB74D" stroke="#E65100" stroke-width="1"/>
    <text x="183" y="102" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Рыбы</text>
    <rect x="215" y="90" width="55" height="16" rx="3" fill="#FFB74D" stroke="#E65100" stroke-width="1"/>
    <text x="243" y="102" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Земноводн.</text>
    <!-- Vertebrates -->
    <rect x="10" y="120" width="65" height="16" rx="3" fill="#FF8A65" stroke="#E64A19" stroke-width="1"/>
    <text x="43" y="132" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle">Пресмыкающ.</text>
    <rect x="80" y="120" width="55" height="16" rx="3" fill="#FF8A65" stroke="#E64A19" stroke-width="1"/>
    <text x="108" y="132" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle">Птицы</text>
    <rect x="140" y="120" width="85" height="16" rx="3" fill="#FF8A65" stroke="#E64A19" stroke-width="1"/>
    <text x="183" y="132" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle">Млекопитающие</text>
    <!-- Diversity stats -->
    <text x="138" y="160" font-family="Arial,sans-serif" font-size="9" fill="#E65100" text-anchor="middle" font-weight="bold">Более 1.5 млн видов!</text>
    <text x="138" y="178" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Беспозвоночные: ~97% видов</text>
    <text x="138" y="193" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Позвоночные: ~3% видов</text>
    <!-- Habitats -->
    <text x="138" y="218" font-family="Arial,sans-serif" font-size="9" fill="#E65100" text-anchor="middle" font-weight="bold">Среды обитания</text>
    <text x="15" y="235" font-family="Arial,sans-serif" font-size="8" fill="#1565C0">Водная</text>
    <text x="80" y="235" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32">Наземно-воздушная</text>
    <text x="200" y="235" font-family="Arial,sans-serif" font-size="8" fill="#795548">Почвенная</text>
  </g>
''' + svg_footer("Общая характеристика животных"))

    # Lesson 2: Подцарство Одноклеточные
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Подцарство Одноклеточные", f"Биология {grade} класс - Урок {n}",
        "#E3F2FD", "#BBDEFB", "#0277BD") + '''
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="570" height="270" rx="8" fill="white" stroke="#0277BD" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="570" height="22" rx="8" fill="#0277BD" opacity="0.9"/>
    <rect x="0" y="16" width="570" height="8" fill="#0277BD" opacity="0.9"/>
    <text x="285" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ОБЩИЕ СВОЙСТВА ОДНОКЛЕТОЧНЫХ</text>
    <text x="285" y="42" font-family="Arial,sans-serif" font-size="8" fill="#0277BD" text-anchor="middle">Один организм = одна клетка</text>
    <!-- Amoeba features -->
    <text x="15" y="60" font-family="Arial,sans-serif" font-size="8" fill="#555">Псевдоподии (ложноножки)</text>
    <text x="15" y="74" font-family="Arial,sans-serif" font-size="8" fill="#555">Фагоцитоз - захват пищи</text>
    <text x="15" y="88" font-family="Arial,sans-serif" font-size="8" fill="#555">Пиноцитоз - впячивание мембраны</text>
    <text x="15" y="102" font-family="Arial,sans-serif" font-size="8" fill="#555">Сократительная вакуоль - осморегуляция</text>
    <text x="15" y="116" font-family="Arial,sans-serif" font-size="8" fill="#555">Деление надвое (бесполое)</text>
    <!-- Comparison table -->
    <rect x="10" y="130" width="180" height="22" rx="3" fill="#0277BD" opacity="0.8"/>
    <text x="100" y="145" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">Тип Корненожки</text>
    <text x="15" y="165" font-family="Arial,sans-serif" font-size="7" fill="#555">Амёба, фораминиферы</text>
    <text x="15" y="178" font-family="Arial,sans-serif" font-size="7" fill="#555">Ложноножки, раковины</text>
    <rect x="195" y="130" width="180" height="22" rx="3" fill="#2E7D32" opacity="0.8"/>
    <text x="285" y="145" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">Тип Жгутиконосцы</text>
    <text x="200" y="165" font-family="Arial,sans-serif" font-size="7" fill="#555">Эвглена, трипаносома</text>
    <text x="200" y="178" font-family="Arial,sans-serif" font-size="7" fill="#555">Жгутик для движения</text>
    <rect x="380" y="130" width="180" height="22" rx="3" fill="#7B1FA2" opacity="0.8"/>
    <text x="470" y="145" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">Тип Инфузории</text>
    <text x="385" y="165" font-family="Arial,sans-serif" font-size="7" fill="#555">Парамеция, туфелька</text>
    <text x="385" y="178" font-family="Arial,sans-serif" font-size="7" fill="#555">Реснички, два ядра</text>
    <!-- Lifestyle -->
    <text x="285" y="200" font-family="Arial,sans-serif" font-size="9" fill="#0277BD" text-anchor="middle" font-weight="bold">ОБРАЗ ЖИЗНИ</text>
    <rect x="10" y="210" width="175" height="45" rx="5" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
    <text x="98" y="228" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Свободноживущие</text>
    <text x="98" y="242" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">В воде, почве</text>
    <rect x="195" y="210" width="175" height="45" rx="5" fill="#FFEBEE" stroke="#C62828" stroke-width="1"/>
    <text x="283" y="228" font-family="Arial,sans-serif" font-size="8" fill="#C62828" text-anchor="middle" font-weight="bold">Паразиты</text>
    <text x="283" y="242" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">В организмах хозяев</text>
    <rect x="380" y="210" width="175" height="45" rx="5" fill="#FFF3E0" stroke="#E65100" stroke-width="1"/>
    <text x="468" y="228" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">Симбионты</text>
    <text x="468" y="242" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Взаимовыгодные</text>
  </g>
''' + svg_footer("Подцарство Одноклеточные"))

    # Lesson 3: Простейшие
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Простейшие: Амёба, Эвглена, Инфузория", f"Биология {grade} класс - Урок {n}",
        "#E3F2FD", "#BBDEFB", "#0277BD") + '''
  <!-- Amoeba -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="185" height="270" rx="8" fill="white" stroke="#0277BD" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="185" height="22" rx="8" fill="#0277BD" opacity="0.9"/>
    <rect x="0" y="16" width="185" height="8" fill="#0277BD" opacity="0.9"/>
    <text x="93" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">АМЁБА</text>
    <!-- Amoeba shape -->
    <path d="M93,60 Q60,55 50,80 Q35,100 55,130 Q65,155 93,160 Q120,158 135,140 Q155,115 145,85 Q135,60 93,60 Z" fill="#E3F2FD" stroke="#1565C0" stroke-width="2"/>
    <!-- Pseudopodia -->
    <path d="M50,80 Q30,70 25,85" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
    <path d="M55,130 Q35,140 30,130" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
    <path d="M135,140 Q150,150 155,140" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
    <text x="20" y="68" font-family="Arial,sans-serif" font-size="5" fill="#1565C0">ложноножки</text>
    <!-- Nucleus -->
    <circle cx="93" cy="100" r="14" fill="#90CAF9" stroke="#0D47A1" stroke-width="1.5"/>
    <text x="93" y="104" font-family="Arial,sans-serif" font-size="7" fill="#0D47A1" text-anchor="middle">ядро</text>
    <!-- Contractile vacuole -->
    <circle cx="65" cy="75" r="8" fill="#BBDEFB" stroke="#1565C0" stroke-width="1" stroke-dasharray="2,1"/>
    <text x="65" y="65" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">сокр. вак.</text>
    <!-- Food vacuole -->
    <circle cx="120" cy="120" r="7" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
    <text x="120" y="123" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">пища</text>
    <!-- Digestive vacuole -->
    <circle cx="80" cy="135" r="6" fill="#FFCC80" stroke="#FF8F00" stroke-width="0.8"/>
    <!-- Features -->
    <text x="93" y="185" font-family="Arial,sans-serif" font-size="7" fill="#0277BD" text-anchor="middle" font-weight="bold">Движение:</text>
    <text x="93" y="197" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Ложноножки</text>
    <text x="93" y="212" font-family="Arial,sans-serif" font-size="7" fill="#0277BD" text-anchor="middle" font-weight="bold">Питание:</text>
    <text x="93" y="224" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Фагоцитоз</text>
    <text x="93" y="239" font-family="Arial,sans-serif" font-size="7" fill="#0277BD" text-anchor="middle" font-weight="bold">Дыхание:</text>
    <text x="93" y="251" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Всей поверхностью</text>
    <text x="93" y="266" font-family="Arial,sans-serif" font-size="7" fill="#0277BD" text-anchor="middle" font-weight="bold">Размножение:</text>
    <text x="93" y="268" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Деление</text>
  </g>
  <!-- Euglena -->
  <g transform="translate(210,75)">
    <rect x="0" y="0" width="185" height="270" rx="8" fill="white" stroke="#2E7D32" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="185" height="22" rx="8" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="16" width="185" height="8" fill="#2E7D32" opacity="0.9"/>
    <text x="93" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ЭВГЛЕНА ЗЕЛЁНАЯ</text>
    <!-- Euglena body -->
    <ellipse cx="93" cy="95" rx="30" ry="55" fill="#C8E6C9" stroke="#2E7D32" stroke-width="2"/>
    <path d="M93,40 Q85,35 80,30" fill="none" stroke="#C8E6C9" stroke-width="2"/>
    <!-- Flagellum -->
    <path d="M80,30 Q70,20 65,10 Q60,5 55,8" fill="none" stroke="#2E7D32" stroke-width="1.5"/>
    <text x="50" y="5" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">жгутик</text>
    <!-- Eye spot -->
    <circle cx="82" cy="52" r="4" fill="#EF5350" stroke="#C62828" stroke-width="0.8"/>
    <text x="70" y="52" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="end">глазок</text>
    <!-- Nucleus -->
    <ellipse cx="93" cy="100" rx="10" ry="8" fill="#81C784" stroke="#1B5E20" stroke-width="1"/>
    <text x="93" y="104" font-family="Arial,sans-serif" font-size="6" fill="#1B5E20" text-anchor="middle">ядро</text>
    <!-- Chloroplasts -->
    <ellipse cx="78" cy="80" rx="8" ry="4" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.8" transform="rotate(-20,78,80)"/>
    <ellipse cx="108" cy="85" rx="8" ry="4" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.8" transform="rotate(20,108,85)"/>
    <ellipse cx="85" cy="115" rx="8" ry="4" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.8" transform="rotate(-10,85,115)"/>
    <text x="93" y="130" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">хлоропласты</text>
    <!-- Contractile vacuole -->
    <circle cx="78" cy="60" r="5" fill="#BBDEFB" stroke="#1565C0" stroke-width="0.8"/>
    <!-- Pellicle -->
    <line x1="70" y1="55" x2="70" y2="135" stroke="#1B5E20" stroke-width="0.5" stroke-dasharray="2,1"/>
    <line x1="116" y1="55" x2="116" y2="135" stroke="#1B5E20" stroke-width="0.5" stroke-dasharray="2,1"/>
    <text x="140" y="95" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20">пелликула</text>
    <!-- Features -->
    <text x="93" y="160" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Уникальность:</text>
    <text x="93" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">На свету - автотроф</text>
    <text x="93" y="188" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">В темноте - гетеротроф</text>
    <text x="93" y="205" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Движение: жгутик</text>
    <text x="93" y="220" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Светочувствительность:</text>
    <text x="93" y="232" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">глазок (стигма)</text>
    <text x="93" y="250" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Размножение:</text>
    <text x="93" y="262" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Продольное деление</text>
  </g>
  <!-- Paramecium -->
  <g transform="translate(405,75)">
    <rect x="0" y="0" width="180" height="270" rx="8" fill="white" stroke="#7B1FA2" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="180" height="22" rx="8" fill="#7B1FA2" opacity="0.9"/>
    <rect x="0" y="16" width="180" height="8" fill="#7B1FA2" opacity="0.9"/>
    <text x="90" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ИНФУЗОРИЯ-ТУФЕЛЬКА</text>
    <!-- Paramecium body -->
    <path d="M90,45 Q55,50 45,90 Q40,130 55,155 Q70,170 90,165 Q110,170 125,155 Q140,130 135,90 Q125,50 90,45 Z" fill="#F3E5F5" stroke="#7B1FA2" stroke-width="2"/>
    <!-- Cilia -->
    <line x1="45" y1="70" x2="35" y2="65" stroke="#7B1FA2" stroke-width="0.5"/>
    <line x1="42" y1="85" x2="32" y2="82" stroke="#7B1FA2" stroke-width="0.5"/>
    <line x1="42" y1="100" x2="32" y2="100" stroke="#7B1FA2" stroke-width="0.5"/>
    <line x1="45" y1="115" x2="35" y2="118" stroke="#7B1FA2" stroke-width="0.5"/>
    <line x1="135" y1="70" x2="145" y2="65" stroke="#7B1FA2" stroke-width="0.5"/>
    <line x1="138" y1="85" x2="148" y2="82" stroke="#7B1FA2" stroke-width="0.5"/>
    <line x1="138" y1="100" x2="148" y2="100" stroke="#7B1FA2" stroke-width="0.5"/>
    <line x1="135" y1="115" x2="145" y2="118" stroke="#7B1FA2" stroke-width="0.5"/>
    <text x="25" y="95" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2">реснички</text>
    <!-- Oral groove -->
    <path d="M60,75 Q50,90 55,110" fill="none" stroke="#9C27B0" stroke-width="1.5"/>
    <text x="35" y="120" font-family="Arial,sans-serif" font-size="5" fill="#9C27B0">ротовое</text>
    <text x="35" y="128" font-family="Arial,sans-serif" font-size="5" fill="#9C27B0">отверстие</text>
    <!-- Macronucleus -->
    <ellipse cx="90" cy="90" rx="20" ry="12" fill="#CE93D8" stroke="#4A148C" stroke-width="1.2"/>
    <text x="90" y="93" font-family="Arial,sans-serif" font-size="6" fill="#4A148C" text-anchor="middle">макронуклеус</text>
    <!-- Micronucleus -->
    <ellipse cx="85" cy="108" rx="6" ry="4" fill="#AB47BC" stroke="#6A1B9A" stroke-width="1"/>
    <text x="108" y="112" font-family="Arial,sans-serif" font-size="5" fill="#6A1B9A">микронук.</text>
    <!-- Contractile vacuoles -->
    <circle cx="65" cy="65" r="6" fill="#E1BEE7" stroke="#7B1FA2" stroke-width="0.8" stroke-dasharray="2,1"/>
    <circle cx="115" cy="130" r="6" fill="#E1BEE7" stroke="#7B1FA2" stroke-width="0.8" stroke-dasharray="2,1"/>
    <!-- Features -->
    <text x="90" y="190" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Два ядра!</text>
    <text x="90" y="205" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Макро - обмен веществ</text>
    <text x="90" y="217" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Микро - размножение</text>
    <text x="90" y="235" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Движение: реснички</text>
    <text x="90" y="250" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Размножение:</text>
    <text x="90" y="262" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Деление + конъюгация</text>
  </g>
''' + svg_footer("Простейшие: Амёба, Эвглена, Инфузория"))


    # Lesson 4-5: Кишечнополостные
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Кишечнополостные: Гидра, Медузы, Кораллы", f"Биология {grade} класс - Урок {n}",
        "#E3F2FD", "#BBDEFB", "#0277BD") + '''
  <!-- Hydra -->
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="185" height="270" rx="8" fill="white" stroke="#0277BD" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="185" height="22" rx="8" fill="#0277BD" opacity="0.9"/>
    <rect x="0" y="16" width="185" height="8" fill="#0277BD" opacity="0.9"/>
    <text x="93" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ГИДРА</text>
    <!-- Hydra body -->
    <path d="M93,30 Q70,35 65,70 Q60,120 65,170 Q70,200 85,220 Q93,230 93,230 Q93,230 101,220 Q116,200 121,170 Q126,120 121,70 Q116,35 93,30" fill="#BBDEFB" stroke="#0277BD" stroke-width="1.5"/>
    <!-- Tentacles -->
    <path d="M65,45 Q40,55 35,70" fill="none" stroke="#90CAF9" stroke-width="2"/>
    <path d="M70,38 Q55,50 48,65" fill="none" stroke="#90CAF9" stroke-width="2"/>
    <path d="M80,32 Q70,42 65,55" fill="none" stroke="#90CAF9" stroke-width="2"/>
    <path d="M106,32 Q116,42 121,55" fill="none" stroke="#90CAF9" stroke-width="2"/>
    <path d="M116,38 Q131,50 138,65" fill="none" stroke="#90CAF9" stroke-width="2"/>
    <path d="M121,45 Q146,55 151,70" fill="none" stroke="#90CAF9" stroke-width="2"/>
    <!-- Mouth -->
    <ellipse cx="93" cy="42" rx="8" ry="4" fill="#E3F2FD" stroke="#0277BD" stroke-width="1"/>
    <text x="120" y="40" font-family="Arial,sans-serif" font-size="5" fill="#0277BD">рот</text>
    <!-- Body layers -->
    <text x="93" y="100" font-family="Arial,sans-serif" font-size="6" fill="#0277BD" text-anchor="middle">эктодерма</text>
    <text x="93" y="120" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">мезоглея</text>
    <text x="93" y="140" font-family="Arial,sans-serif" font-size="6" fill="#0D47A1" text-anchor="middle">энтодерма</text>
    <text x="93" y="160" font-family="Arial,sans-serif" font-size="6" fill="#01579B" text-anchor="middle">кишечная полость</text>
    <!-- Budding -->
    <path d="M121,100 Q135,95 140,105 Q145,115 135,120 Q125,118 121,110" fill="#BBDEFB" stroke="#0277BD" stroke-width="1"/>
    <text x="148" y="112" font-family="Arial,sans-serif" font-size="5" fill="#0277BD">почкование</text>
    <!-- Sole -->
    <ellipse cx="93" cy="230" rx="12" ry="4" fill="#90CAF9" stroke="#0277BD" stroke-width="1"/>
    <text x="93" y="245" font-family="Arial,sans-serif" font-size="6" fill="#0277BD" text-anchor="middle">подошва</text>
    <!-- Stinging cells -->
    <circle cx="42" cy="68" r="3" fill="#FFCDD2" stroke="#C62828" stroke-width="0.8"/>
    <line x1="39" y1="66" x2="34" y2="62" stroke="#C62828" stroke-width="0.5"/>
    <text x="28" y="80" font-family="Arial,sans-serif" font-size="5" fill="#C62828">стрек.</text>
  </g>
  <!-- Jellyfish -->
  <g transform="translate(210,75)">
    <rect x="0" y="0" width="185" height="130" rx="8" fill="white" stroke="#0277BD" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="185" height="22" rx="8" fill="#0277BD" opacity="0.9"/>
    <rect x="0" y="16" width="185" height="8" fill="#0277BD" opacity="0.9"/>
    <text x="93" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">МЕДУЗА</text>
    <!-- Bell -->
    <path d="M40,70 Q93,30 146,70" fill="#E3F2FD" stroke="#0277BD" stroke-width="1.5"/>
    <ellipse cx="93" cy="70" rx="53" ry="20" fill="#BBDEFB" stroke="#0277BD" stroke-width="1"/>
    <!-- Tentacles -->
    <path d="M50,72 Q45,95 50,115" fill="none" stroke="#90CAF9" stroke-width="1"/>
    <path d="M70,72 Q68,95 72,115" fill="none" stroke="#90CAF9" stroke-width="1"/>
    <path d="M93,72 Q93,95 93,115" fill="none" stroke="#90CAF9" stroke-width="1"/>
    <path d="M116,72 Q118,95 114,115" fill="none" stroke="#90CAF9" stroke-width="1"/>
    <path d="M136,72 Q141,95 136,115" fill="none" stroke="#90CAF9" stroke-width="1"/>
    <text x="93" y="125" font-family="Arial,sans-serif" font-size="6" fill="#0277BD" text-anchor="middle">Реактивное движение</text>
  </g>
  <!-- Coral -->
  <g transform="translate(210,215)">
    <rect x="0" y="0" width="185" height="130" rx="8" fill="white" stroke="#0277BD" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="185" height="22" rx="8" fill="#E65100" opacity="0.9"/>
    <rect x="0" y="16" width="185" height="8" fill="#E65100" opacity="0.9"/>
    <text x="93" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">КОРАЛЛОВЫЙ ПОЛИП</text>
    <!-- Coral branch -->
    <path d="M70,100 L70,55 Q70,45 80,40" fill="none" stroke="#FF8A65" stroke-width="5" stroke-linecap="round"/>
    <path d="M70,75 L95,55 Q100,50 105,45" fill="none" stroke="#FF8A65" stroke-width="4" stroke-linecap="round"/>
    <path d="M70,65 L50,45 Q45,40 40,35" fill="none" stroke="#FF8A65" stroke-width="4" stroke-linecap="round"/>
    <!-- Polyps -->
    <circle cx="80" cy="38" r="5" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
    <circle cx="105" cy="43" r="4" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
    <circle cx="40" cy="33" r="4" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
    <text x="93" y="120" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Колониальные организмы</text>
  </g>
  <!-- Features -->
  <g transform="translate(405,75)">
    <rect x="0" y="0" width="180" height="270" rx="8" fill="white" stroke="#0277BD" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="180" height="22" rx="8" fill="#01579B" opacity="0.9"/>
    <rect x="0" y="16" width="180" height="8" fill="#01579B" opacity="0.9"/>
    <text x="90" y="16" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ОСОБЕННОСТИ ТИПА</text>
    <text x="15" y="42" font-family="Arial,sans-serif" font-size="8" fill="#0277BD" font-weight="bold">Двухслойные:</text>
    <text x="15" y="54" font-family="Arial,sans-serif" font-size="7" fill="#555">Эктодерма + энтодерма</text>
    <text x="15" y="70" font-family="Arial,sans-serif" font-size="8" fill="#0277BD" font-weight="bold">Радиальная симметрия</text>
    <text x="15" y="86" font-family="Arial,sans-serif" font-size="8" fill="#0277BD" font-weight="bold">Кишечная полость</text>
    <text x="15" y="98" font-family="Arial,sans-serif" font-size="7" fill="#555">Одно отверстие (рот)</text>
    <text x="15" y="114" font-family="Arial,sans-serif" font-size="8" fill="#C62828" font-weight="bold">Стрекательные клетки</text>
    <text x="15" y="126" font-family="Arial,sans-serif" font-size="7" fill="#555">Защита и нападение</text>
    <text x="15" y="142" font-family="Arial,sans-serif" font-size="8" fill="#0277BD" font-weight="bold">Нервная сеть</text>
    <text x="15" y="154" font-family="Arial,sans-serif" font-size="7" fill="#555">Диффузный тип</text>
    <text x="15" y="175" font-family="Arial,sans-serif" font-size="8" fill="#0277BD" font-weight="bold">Размножение:</text>
    <text x="15" y="188" font-family="Arial,sans-serif" font-size="7" fill="#555">Бесполое (почкование)</text>
    <text x="15" y="200" font-family="Arial,sans-serif" font-size="7" fill="#555">Половое (сперматозоиды+</text>
    <text x="15" y="212" font-family="Arial,sans-serif" font-size="7" fill="#555">яйцеклетки)</text>
    <text x="15" y="232" font-family="Arial,sans-serif" font-size="8" fill="#7B1FA2" font-weight="bold">Чередование поколений:</text>
    <text x="15" y="244" font-family="Arial,sans-serif" font-size="7" fill="#555">Полип (бесполое)</text>
    <text x="15" y="256" font-family="Arial,sans-serif" font-size="7" fill="#555">Медуза (половое)</text>
  </g>
''' + svg_footer("Кишечнополостные"))

    # Lesson 6: Плоские черви
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Плоские черви: Планария, Цепень", f"Биология {grade} класс - Урок {n}",
        "#FFF3E0", "#FFE0B2", "#E65100") + '''
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="275" height="270" rx="8" fill="white" stroke="#E65100" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#E65100" opacity="0.9"/>
    <rect x="0" y="16" width="275" height="8" fill="#E65100" opacity="0.9"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">БЕЛАЯ ПЛАНАРИЯ</text>
    <!-- Planaria body -->
    <path d="M50,80 Q30,75 25,85 Q20,95 25,105 Q30,110 50,110 L225,110 Q245,105 250,95 Q245,85 225,80 Z" fill="#F5F5F5" stroke="#9E9E9E" stroke-width="1.5"/>
    <!-- Head with auricles -->
    <path d="M50,80 Q40,65 35,70" fill="#F5F5F5" stroke="#9E9E9E" stroke-width="1"/>
    <path d="M50,110 Q40,125 35,120" fill="#F5F5F5" stroke="#9E9E9E" stroke-width="1"/>
    <!-- Eyes -->
    <circle cx="42" cy="88" r="4" fill="#333" stroke="#111" stroke-width="0.8"/>
    <circle cx="42" cy="102" r="4" fill="#333" stroke="#111" stroke-width="0.8"/>
    <text x="55" y="78" font-family="Arial,sans-serif" font-size="5" fill="#555">ушки</text>
    <text x="55" y="96" font-family="Arial,sans-serif" font-size="5" fill="#333">глаза</text>
    <!-- Pharynx -->
    <ellipse cx="138" cy="95" rx="8" ry="5" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
    <text x="138" y="108" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">глотка</text>
    <!-- Branched intestine -->
    <line x1="146" y1="90" x2="180" y2="85" stroke="#E65100" stroke-width="0.8"/>
    <line x1="180" y1="85" x2="200" y2="82" stroke="#E65100" stroke-width="0.6"/>
    <line x1="180" y1="85" x2="195" y2="92" stroke="#E65100" stroke-width="0.6"/>
    <line x1="146" y1="100" x2="180" y2="105" stroke="#E65100" stroke-width="0.8"/>
    <line x1="180" y1="105" x2="200" y2="108" stroke="#E65100" stroke-width="0.6"/>
    <line x1="180" y1="105" x2="195" y2="98" stroke="#E65100" stroke-width="0.6"/>
    <line x1="130" y1="90" x2="100" y2="85" stroke="#E65100" stroke-width="0.8"/>
    <line x1="100" y1="85" x2="80" y2="82" stroke="#E65100" stroke-width="0.6"/>
    <line x1="130" y1="100" x2="100" y2="105" stroke="#E65100" stroke-width="0.8"/>
    <line x1="100" y1="105" x2="80" y2="108" stroke="#E65100" stroke-width="0.6"/>
    <text x="200" y="98" font-family="Arial,sans-serif" font-size="5" fill="#E65100">кишечник</text>
    <!-- Features -->
    <text x="138" y="135" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">Свободноживущая</text>
    <text x="138" y="150" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Трёхслойная (эктодерма, мезодерма, энтодерма)</text>
    <text x="138" y="165" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Двусторонняя симметрия</text>
    <text x="138" y="180" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Кожно-мускульный мешок</text>
    <text x="138" y="195" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Выделительная: протонефридии</text>
    <text x="138" y="210" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Нервная: нервные стволы</text>
    <text x="138" y="230" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">Гермафродиты</text>
    <text x="138" y="245" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Способны к регенерации!</text>
  </g>
  <!-- Tapeworm -->
  <g transform="translate(300,75)">
    <rect x="0" y="0" width="285" height="270" rx="8" fill="white" stroke="#E65100" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="285" height="22" rx="8" fill="#BF360C" opacity="0.9"/>
    <rect x="0" y="16" width="285" height="8" fill="#BF360C" opacity="0.9"/>
    <text x="143" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">БЫЧИЙ ЦЕПЕНЬ (ПАРАЗИТ)</text>
    <!-- Scolex -->
    <circle cx="40" cy="50" r="12" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
    <circle cx="33" cy="46" r="3" fill="#333"/>
    <circle cx="47" cy="46" r="3" fill="#333"/>
    <!-- Hooks/suckers -->
    <circle cx="30" cy="55" r="4" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
    <circle cx="50" cy="55" r="4" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
    <text x="40" y="72" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">сколекс с присосками</text>
    <!-- Neck -->
    <rect x="38" y="75" width="4" height="15" fill="#FFE0B2" stroke="#E65100" stroke-width="0.5"/>
    <!-- Proglottids -->
    <rect x="30" y="90" width="20" height="8" rx="2" fill="#FFF3E0" stroke="#E65100" stroke-width="0.8"/>
    <rect x="30" y="100" width="22" height="9" rx="2" fill="#FFF3E0" stroke="#E65100" stroke-width="0.8"/>
    <rect x="28" y="112" width="24" height="10" rx="2" fill="#FFF3E0" stroke="#E65100" stroke-width="0.8"/>
    <rect x="26" y="125" width="28" height="12" rx="2" fill="#FFF3E0" stroke="#E65100" stroke-width="0.8"/>
    <rect x="24" y="140" width="32" height="14" rx="2" fill="#FFF3E0" stroke="#E65100" stroke-width="0.8"/>
    <rect x="22" y="157" width="36" height="16" rx="3" fill="#FFECB3" stroke="#E65100" stroke-width="1"/>
    <text x="40" y="170" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">яйца</text>
    <text x="80" y="100" font-family="Arial,sans-serif" font-size="7" fill="#E65100">членики (проглоттиды)</text>
    <!-- Life cycle -->
    <text x="143" y="200" font-family="Arial,sans-serif" font-size="8" fill="#C62828" text-anchor="middle" font-weight="bold">Жизненный цикл</text>
    <text x="143" y="215" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">1. Членики с яйцами выходят</text>
    <text x="143" y="228" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">2. Промежуточный хозяин (корова)</text>
    <text x="143" y="241" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">3. Финна в мышцах</text>
    <text x="143" y="254" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">4. Основной хозяин (человек)</text>
    <text x="143" y="267" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">Нет пищеварительной системы!</text>
  </g>
''' + svg_footer("Плоские черви"))

    # Lesson 7: Круглые черви
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Круглые черви: Аскарида", f"Биология {grade} класс - Урок {n}",
        "#FFF3E0", "#FFE0B2", "#E65100") + '''
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="280" height="270" rx="8" fill="white" stroke="#E65100" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="280" height="22" rx="8" fill="#E65100" opacity="0.9"/>
    <rect x="0" y="16" width="280" height="8" fill="#E65100" opacity="0.9"/>
    <text x="140" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">АСКАРИДА ЧЕЛОВЕЧЕСКАЯ</text>
    <!-- Female ascaris -->
    <path d="M80,45 Q40,60 35,100 Q30,140 40,180 Q50,210 80,220 Q90,215 85,210 Q60,200 50,180 Q40,160 45,130 Q50,90 80,60 Z" fill="#FFCC80" stroke="#E65100" stroke-width="1.5"/>
    <path d="M80,45 Q110,60 115,100 Q120,140 110,180 Q100,210 80,220" fill="#FFCC80" stroke="#E65100" stroke-width="1.5"/>
    <text x="75" y="130" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" transform="rotate(-90,75,130)">самка (20-40 см)</text>
    <!-- Male ascaris -->
    <path d="M180,55 Q150,65 145,100 Q140,135 150,165 Q155,175 165,180 Q170,175 168,170 Q155,165 150,155 Q145,135 150,110 Q155,80 180,65 Z" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
    <path d="M180,55 Q210,65 215,100 Q220,135 210,165 Q200,175 180,180" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
    <!-- Curved tail of male -->
    <path d="M165,180 Q160,190 170,195" fill="none" stroke="#E65100" stroke-width="1.5"/>
    <text x="182" y="130" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" transform="rotate(-90,182,130)">самец (15-25 см)</text>
    <!-- Internal structure labels -->
    <text x="200" y="50" font-family="Arial,sans-serif" font-size="7" fill="#E65100">Первичная полость</text>
    <text x="200" y="62" font-family="Arial,sans-serif" font-size="7" fill="#E65100">Кутикула (покров)</text>
    <text x="200" y="74" font-family="Arial,sans-serif" font-size="7" fill="#E65100">Сквозной кишечник</text>
    <text x="200" y="86" font-family="Arial,sans-serif" font-size="7" fill="#E65100">Рот + анус!</text>
  </g>
  <!-- Features and life cycle -->
  <g transform="translate(310,75)">
    <rect x="0" y="0" width="275" height="270" rx="8" fill="white" stroke="#E65100" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="275" height="22" rx="8" fill="#BF360C" opacity="0.9"/>
    <rect x="0" y="16" width="275" height="8" fill="#BF360C" opacity="0.9"/>
    <text x="138" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ОСОБЕННОСТИ И ЖИЗНЕННЫЙ ЦИКЛ</text>
    <text x="15" y="42" font-family="Arial,sans-serif" font-size="8" fill="#E65100" font-weight="bold">Отличия от плоских червей:</text>
    <text x="15" y="56" font-family="Arial,sans-serif" font-size="7" fill="#555">Сквозной кишечник (рот + анус)</text>
    <text x="15" y="68" font-family="Arial,sans-serif" font-size="7" fill="#555">Первичная полость тела</text>
    <text x="15" y="80" font-family="Arial,sans-serif" font-size="7" fill="#555">Раздельнополые</text>
    <text x="15" y="92" font-family="Arial,sans-serif" font-size="7" fill="#555">Кутикула вместо ресничек</text>
    <text x="15" y="112" font-family="Arial,sans-serif" font-size="8" fill="#C62828" font-weight="bold">Жизненный цикл аскариды:</text>
    <text x="15" y="128" font-family="Arial,sans-serif" font-size="7" fill="#555">1. Яйца выходят с фекалиями</text>
    <text x="15" y="140" font-family="Arial,sans-serif" font-size="7" fill="#555">2. Развитие в почве (2-3 нед.)</text>
    <text x="15" y="152" font-family="Arial,sans-serif" font-size="7" fill="#555">3. Заражение через немытые руки</text>
    <text x="15" y="164" font-family="Arial,sans-serif" font-size="7" fill="#555">4. Личинка в кишечнике</text>
    <text x="15" y="176" font-family="Arial,sans-serif" font-size="7" fill="#555">5. Миграция: печень-лёгкие-глотка</text>
    <text x="15" y="188" font-family="Arial,sans-serif" font-size="7" fill="#555">6. Возврат в кишечник, взросление</text>
    <text x="15" y="210" font-family="Arial,sans-serif" font-size="8" fill="#C62828" font-weight="bold">Профилактика:</text>
    <text x="15" y="225" font-family="Arial,sans-serif" font-size="7" fill="#555">Мыть руки, овощи, фрукты</text>
    <text x="15" y="238" font-family="Arial,sans-serif" font-size="7" fill="#555">Не удобрять навозом</text>
    <text x="15" y="251" font-family="Arial,sans-serif" font-size="7" fill="#555">Борьба с мухами</text>
  </g>
''' + svg_footer("Круглые черви"))

    # Lesson 8: Кольчатые черви
    n += 1
    write_svg(grade, "biology", n, svg_header(
        "Кольчатые черви: Дождевой червь", f"Биология {grade} класс - Урок {n}",
        "#EFEBE9", "#D7CCC8", "#5D4037") + '''
  <g transform="translate(15,75)">
    <rect x="0" y="0" width="570" height="270" rx="8" fill="white" stroke="#5D4037" stroke-width="1.5" opacity="0.95"/>
    <rect x="0" y="0" width="570" height="22" rx="8" fill="#5D4037" opacity="0.9"/>
    <rect x="0" y="16" width="570" height="8" fill="#5D4037" opacity="0.9"/>
    <text x="285" y="16" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ДОЖДЕВОЙ ЧЕРВЬ (ЛИМБРИЦИДА)</text>
    <!-- Earthworm body -->
    <g transform="translate(50,80)">
      <ellipse cx="0" cy="40" rx="15" ry="10" fill="#D7CCC8" stroke="#8D6E63" stroke-width="1.5"/>
      <rect x="15" y="30" width="30" height="20" rx="3" fill="#EFEBE9" stroke="#8D6E63" stroke-width="1"/>
      <rect x="45" y="30" width="30" height="20" rx="3" fill="#D7CCC8" stroke="#8D6E63" stroke-width="1"/>
      <rect x="75" y="30" width="30" height="20" rx="3" fill="#EFEBE9" stroke="#8D6E63" stroke-width="1"/>
      <rect x="105" y="30" width="30" height="20" rx="3" fill="#D7CCC8" stroke="#8D6E63" stroke-width="1"/>
      <rect x="135" y="30" width="30" height="20" rx="3" fill="#EFEBE9" stroke="#8D6E63" stroke-width="1"/>
      <rect x="165" y="30" width="30" height="20" rx="3" fill="#D7CCC8" stroke="#8D6E63" stroke-width="1"/>
      <rect x="195" y="30" width="30" height="20" rx="3" fill="#EFEBE9" stroke="#8D6E63" stroke-width="1"/>
      <rect x="225" y="30" width="30" height="20" rx="3" fill="#D7CCC8" stroke="#8D6E63" stroke-width="1"/>
      <rect x="255" y="30" width="30" height="20" rx="3" fill="#EFEBE9" stroke="#8D6E63" stroke-width="1"/>
      <rect x="285" y="30" width="30" height="20" rx="3" fill="#D7CCC8" stroke="#8D6E63" stroke-width="1"/>
      <rect x="315" y="30" width="30" height="20" rx="3" fill="#EFEBE9" stroke="#8D6E63" stroke-width="1"/>
      <rect x="345" y="30" width="30" height="20" rx="3" fill="#D7CCC8" stroke="#8D6E63" stroke-width="1"/>
      <rect x="375" y="30" width="30" height="20" rx="3" fill="#EFEBE9" stroke="#8D6E63" stroke-width="1"/>
      <!-- Clitellum (saddle) -->
      <rect x="255" y="28" width="90" height="24" rx="5" fill="#BCAAA4" stroke="#795548" stroke-width="1.5"/>
      <text x="300" y="22" font-family="Arial,sans-serif" font-size="6" fill="#795548" text-anchor="middle">поясок</text>
      <!-- Labels -->
      <text x="0" y="22" font-family="Arial,sans-serif" font-size="6" fill="#5D4037">рот</text>
      <text x="405" y="22" font-family="Arial,sans-serif" font-size="6" fill="#5D4037">анус</text>
      <!-- Setae -->
      <line x1="30" y1="50" x2="30" y2="55" stroke="#5D4037" stroke-width="1"/>
      <line x1="60" y1="50" x2="60" y2="55" stroke="#5D4037" stroke-width="1"/>
      <line x1="90" y1="50" x2="90" y2="55" stroke="#5D4037" stroke-width="1"/>
      <text x="60" y="65" font-family="Arial,sans-serif" font-size="5" fill="#5D4037" text-anchor="middle">щетинки</text>
      <!-- Segment lines -->
      <text x="200" y="60" font-family="Arial,sans-serif" font-size="6" fill="#8D6E63" text-anchor="middle">сегменты (кольца)</text>
    </g>
    <!-- Features -->
    <text x="285" y="165" font-family="Arial,sans-serif" font-size="9" fill="#5D4037" text-anchor="middle" font-weight="bold">ОСОБЕННОСТИ КОЛЬЧАТЫХ ЧЕРВЕЙ</text>
    <text x="100" y="185" font-family="Arial,sans-serif" font-size="7" fill="#555">Вторичная полость (целом)</text>
    <text x="100" y="198" font-family="Arial,sans-serif" font-size="7" fill="#555">Замкнутая кровеносная система</text>
    <text x="350" y="185" font-family="Arial,sans-serif" font-size="7" fill="#555">Метамерия (сегментация)</text>
    <text x="350" y="198" font-family="Arial,sans-serif" font-size="7" fill="#555">Органы выделения: нефридии</text>
    <text x="100" y="215" font-family="Arial,sans-serif" font-size="7" fill="#555">Гермафродиты</text>
    <text x="350" y="215" font-family="Arial,sans-serif" font-size="7" fill="#555">Дыхание кожей</text>
    <text x="285" y="235" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Значение: рыхлят почву, улучшают плодородие</text>
    <text x="285" y="250" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Дарвин изучал дождевых червей 39 лет!</text>
  </g>
''' + svg_footer("Кольчатые черви: Дождевой червь"))

