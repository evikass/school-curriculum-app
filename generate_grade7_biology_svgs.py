#!/usr/bin/env python3
"""Generate 8 Grade 7 Biology SVG lesson images."""

import os
import math
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/biology"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Color scheme
PRIMARY = "#10B981"
PRIMARY_DARK = "#059669"
PRIMARY_LIGHT = "#D1FAE5"
PRIMARY_LIGHTER = "#ECFDF5"
ACCENT = "#065F46"
BG = "#F0FDF4"
WHITE = "#FFFFFF"
DARK = "#1F2937"
GRAY = "#6B7280"
LIGHT_GRAY = "#E5E7EB"
RED = "#EF4444"
BLUE = "#3B82F6"
YELLOW = "#F59E0B"
ORANGE = "#F97316"
PURPLE = "#8B5CF6"
PINK = "#EC4899"
CYAN = "#06B6D4"
BROWN = "#92400E"
BROWN_LIGHT = "#FDE68A"
BROWN_MED = "#D97706"

W = 800
H = 600


def escape(text):
    """Escape XML special characters."""
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;"))


def svg_header(title, lesson_num):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:{ACCENT};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{PRIMARY};stop-opacity:1" />
    </linearGradient>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:{BG};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{PRIMARY_LIGHTER};stop-opacity:1" />
    </linearGradient>
    <filter id="shadow" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="1" dy="1" stdDeviation="2" flood-color="#00000020"/>
    </filter>
  </defs>
  <!-- Background -->
  <rect width="{W}" height="{H}" fill="url(#bgGrad)" rx="8"/>
  <!-- Header bar -->
  <rect x="0" y="0" width="{W}" height="60" fill="url(#headerGrad)" rx="8"/>
  <rect x="0" y="30" width="{W}" height="30" fill="url(#headerGrad)"/>
  <text x="400" y="40" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="{WHITE}">{escape(title)}</text>
  <!-- Lesson badge -->
  <rect x="12" y="68" width="90" height="24" rx="12" fill="{PRIMARY}" opacity="0.9"/>
  <text x="57" y="84" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{WHITE}" font-weight="bold">Биология 7</text>
'''


def svg_footer(lesson_num):
    return f'''  <text x="400" y="590" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">Урок {lesson_num}</text>
</svg>'''


def label(x, y, text, color=DARK, size=12, anchor="start", bold=False):
    w = "bold" if bold else "normal"
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Arial, sans-serif" font-size="{size}" fill="{color}" font-weight="{w}">{escape(text)}</text>'


def line(x1, y1, x2, y2, color=GRAY, width=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{d}/>'


def pointer(x1, y1, x2, y2, color=PRIMARY_DARK):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.5"/><circle cx="{x2}" cy="{y2}" r="3" fill="{color}"/>'


def box(x, y, w, h, fill=WHITE, stroke=PRIMARY, rx=6):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.5" filter="url(#shadow)"/>'


def infobox(x, y, w, h, title_text, body_text, fill=PRIMARY_LIGHTER, title_color=ACCENT):
    s = box(x, y, w, h, fill=fill)
    s += f'<rect x="{x}" y="{y}" width="{w}" height="22" rx="6" fill="{title_color}"/>'
    s += f'<rect x="{x}" y="{y + 16}" width="{w}" height="6" fill="{title_color}"/>'
    s += label(x + w / 2, y + 15, title_text, WHITE, 11, "middle", True)
    s += label(x + 8, y + 38, body_text, DARK, 10)
    return s


def arrow_line(x1, y1, x2, y2, color=PRIMARY):
    """Line with arrowhead at end."""
    angle = math.atan2(y2 - y1, x2 - x1)
    ax = x2 - 8 * math.cos(angle - 0.4)
    ay = y2 - 8 * math.sin(angle - 0.4)
    bx = x2 - 8 * math.cos(angle + 0.4)
    by = y2 - 8 * math.sin(angle + 0.4)
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2"/>'
            f'<polygon points="{x2},{y2} {ax},{ay} {bx},{by}" fill="{color}"/>')


# ============================================================
# LESSON 1: Строение и жизнедеятельность бактерий
# ============================================================
def lesson1():
    s = svg_header("Строение и жизнедеятельность бактерий", 1)

    # === Left panel: Bacteria structure diagram ===
    s += box(20, 72, 370, 310, fill=WHITE, stroke=PRIMARY)
    s += label(205, 92, "Строение бактериальной клетки", ACCENT, 12, "middle", True)

    # Cell body (capsule outline)
    s += f'<ellipse cx="200" cy="250" rx="100" ry="70" fill="{PRIMARY_LIGHT}" stroke="{PRIMARY}" stroke-width="2" stroke-dasharray="6,3"/>'
    s += label(200, 250, "Капсула", PRIMARY_DARK, 9, "middle", True)

    # Cell wall
    s += f'<ellipse cx="200" cy="250" rx="85" ry="58" fill="#BBF7D0" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>'
    s += label(200, 268, "Клеточная стенка", WHITE, 9, "middle", True)

    # Cell membrane
    s += f'<ellipse cx="200" cy="250" rx="72" ry="46" fill="#D1FAE5" stroke="{PRIMARY}" stroke-width="1.5" stroke-dasharray="3,2"/>'

    # Nucleoid region
    s += f'<ellipse cx="190" cy="240" rx="35" ry="22" fill="{PRIMARY}" opacity="0.3" stroke="{ACCENT}" stroke-width="1.5"/>'
    # DNA strands inside nucleoid
    for i in range(5):
        yy = 230 + i * 5
        s += f'<path d="M165,{yy} Q175,{yy - 3} 185,{yy} Q195,{yy + 3} 205,{yy} Q215,{yy - 3} 220,{yy}" fill="none" stroke="{ACCENT}" stroke-width="0.8"/>'
    s += label(190, 245, "Нуклеоид", ACCENT, 8, "middle", True)
    s += label(190, 255, "(ДНК)", ACCENT, 7, "middle")

    # Ribosomes
    for rx, ry in [(170, 220), (220, 260), (175, 270), (225, 235), (200, 275)]:
        s += f'<circle cx="{rx}" cy="{ry}" r="3" fill="{ORANGE}" stroke="{BROWN_MED}" stroke-width="0.5"/>'

    # Flagella
    s += f'<path d="M200,310 Q230,340 210,360 Q190,380 220,400" fill="none" stroke="{GRAY}" stroke-width="2"/>'
    s += f'<path d="M190,312 Q160,340 180,360 Q200,380 170,400" fill="none" stroke="{GRAY}" stroke-width="2"/>'
    s += pointer(230, 370, 260, 380)
    s += label(265, 383, "Жгутики", ACCENT, 10, "start", True)

    # Pili
    s += f'<line x1="120" y1="240" x2="95" y2="235" stroke="{GRAY}" stroke-width="1"/>'
    s += f'<line x1="118" y1="260" x2="90" y2="265" stroke="{GRAY}" stroke-width="1"/>'
    s += f'<line x1="125" y1="225" x2="100" y2="215" stroke="{GRAY}" stroke-width="1"/>'
    s += label(60, 218, "Пили", GRAY, 8, "start")

    # Pointer labels
    s += pointer(200, 195, 260, 175)
    s += label(265, 178, "Клеточная стенка", ACCENT, 9, "start", True)

    s += pointer(200, 230, 290, 220)
    s += label(295, 223, "Цитоплазматическая мембрана", ACCENT, 8, "start", True)

    s += pointer(225, 260, 310, 260)
    s += label(315, 263, "Рибосомы", ORANGE, 9, "start", True)

    # === Right top panel: Bacteria shapes ===
    s += box(405, 72, 385, 145, fill=WHITE, stroke=PRIMARY)
    s += label(597, 92, "Формы бактерий", ACCENT, 12, "middle", True)

    # Coccus (round)
    s += f'<circle cx="440" cy="130" r="14" fill="#BBF7D0" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>'
    s += label(460, 127, "Кокки", ACCENT, 10, "start", True)
    s += label(460, 140, "(шаровидные)", GRAY, 8)

    # Bacillus (rod)
    s += f'<rect x="420" y="158" width="40" height="16" rx="8" fill="#BBF7D0" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>'
    s += label(470, 170, "Палочки", ACCENT, 10, "start", True)
    s += label(470, 183, "(цилиндрические)", GRAY, 8)

    # Spirillum (spiral)
    s += f'<path d="M425,200 Q435,192 445,200 Q455,208 465,200 Q475,192 485,200" fill="none" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>'
    s += label(495, 200, "Спириллы", ACCENT, 10, "start", True)
    s += label(495, 213, "(спиральные)", GRAY, 8)

    # Vibrio (comma)
    s += f'<path d="M580,125 Q605,145 585,165" fill="none" stroke="{PRIMARY_DARK}" stroke-width="3" stroke-linecap="round"/>'
    s += label(612, 147, "Вибрионы", ACCENT, 10, "start", True)
    s += label(612, 160, "(изогнутые)", GRAY, 8)

    # Staphylococcus cluster
    s += f'<circle cx="640" cy="190" r="8" fill="#BBF7D0" stroke="{PRIMARY_DARK}" stroke-width="1"/>'
    s += f'<circle cx="654" cy="186" r="8" fill="#BBF7D0" stroke="{PRIMARY_DARK}" stroke-width="1"/>'
    s += f'<circle cx="647" cy="200" r="8" fill="#BBF7D0" stroke="{PRIMARY_DARK}" stroke-width="1"/>'
    s += f'<circle cx="660" cy="197" r="8" fill="#BBF7D0" stroke="{PRIMARY_DARK}" stroke-width="1"/>'
    s += label(674, 195, "Стафилококки", ACCENT, 9, "start", True)

    # === Right bottom panel: Reproduction & Nutrition ===
    s += box(405, 228, 385, 155, fill=WHITE, stroke=PRIMARY)
    s += label(597, 248, "Размножение и питание", ACCENT, 12, "middle", True)

    # Binary fission diagram
    s += label(420, 270, "Размножение — деление надвое:", ACCENT, 10, "start", True)
    # Stage 1: single cell
    s += f'<ellipse cx="430" cy="290" rx="15" ry="10" fill="#BBF7D0" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>'
    # Arrow
    s += f'<polygon points="450,290 456,286 456,294" fill="{PRIMARY}"/>'
    # Stage 2: elongating
    s += f'<ellipse cx="475" cy="290" rx="22" ry="10" fill="#BBF7D0" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>'
    s += f'<line x1="475" y1="280" x2="475" y2="300" stroke="{PRIMARY_DARK}" stroke-width="1" stroke-dasharray="2,2"/>'
    # Arrow
    s += f'<polygon points="502,290 508,286 508,294" fill="{PRIMARY}"/>'
    # Stage 3: two cells
    s += f'<ellipse cx="525" cy="290" rx="14" ry="10" fill="#BBF7D0" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>'
    s += f'<ellipse cx="553" cy="290" rx="14" ry="10" fill="#BBF7D0" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>'

    s += label(420, 315, "Время деления: ~20 мин", DARK, 9)
    s += label(420, 330, "Спорообразование — выживание в", DARK, 9)
    s += label(420, 343, "неблагоприятных условиях", DARK, 9)

    # Nutrition types
    s += label(420, 362, "Типы питания:", ACCENT, 10, "start", True)
    # Autotrophs
    s += f'<rect x="420" y="370" width="10" height="10" rx="2" fill="{PRIMARY}" opacity="0.5"/>'
    s += label(435, 379, "Автотрофы (фото- и хемосинтетики)", DARK, 9)
    # Heterotrophs
    s += f'<rect x="420" y="385" width="10" height="10" rx="2" fill="{ORANGE}" opacity="0.5"/>'
    s += label(435, 394, "Гетеротрофы (сапротрофы, паразиты)", DARK, 9)

    # === Bottom panel: Key facts ===
    s += box(20, 395, 370, 190, fill=WHITE, stroke=PRIMARY)
    s += label(35, 415, "Ключевые особенности:", ACCENT, 12, "start", True)

    facts = [
        "• Прокариоты — нет ядра и мембранных органоидов",
        "• Размер: 0,5-5 мкм (в 10-100 раз меньше эукариот)",
        "• ДНК — кольцевая хромосома в нуклеоиде",
        "• Рибосомы 70S (мельче, чем у эукариот — 80S)",
        "• Клеточная стенка из муреина (пептидогликана)",
        "• Жгутики из белка флагеллина",
        "• Обмен веществ разнообразнее эукариот",
        "• Споры выдерживают кипячение до 3 часов",
    ]
    yy = 435
    for fact in facts:
        s += label(35, yy, fact, DARK, 10)
        yy += 17

    # Spore diagram
    s += box(405, 395, 385, 190, fill=WHITE, stroke=PRIMARY)
    s += label(597, 415, "Спорообразование", ACCENT, 12, "middle", True)

    # Vegetative cell
    s += f'<ellipse cx="470" cy="450" rx="25" ry="15" fill="#BBF7D0" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>'
    s += label(470, 454, "Клетка", DARK, 8, "middle")
    s += arrow_line(500, 450, 535, 450)

    # Sporulation
    s += f'<ellipse cx="565" cy="450" rx="25" ry="15" fill="#FDE68A" stroke="{BROWN_MED}" stroke-width="1.5"/>'
    s += f'<ellipse cx="565" cy="450" rx="12" ry="9" fill="{ORANGE}" stroke="{BROWN}" stroke-width="1"/>'
    s += label(565, 454, "Спора", WHITE, 7, "middle", True)
    s += arrow_line(595, 450, 630, 450)

    # Germination
    s += f'<ellipse cx="660" cy="450" rx="25" ry="15" fill="#BBF7D0" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>'
    s += label(660, 454, "Клетка", DARK, 8, "middle")

    s += label(425, 485, "Спора — покоящаяся форма бактерий:", ACCENT, 10, "start", True)
    s += label(425, 500, "• Образуется при неблагоприятных условиях", DARK, 9)
    s += label(425, 515, "• Устойчива к высушиванию, нагреванию,", DARK, 9)
    s += label(425, 528, "  излучению, дезинфицирующим средствам", DARK, 9)
    s += label(425, 548, "• При благоприятных условиях прорастает", DARK, 9)
    s += label(425, 563, "  в вегетативную клетку за 4-5 часов", DARK, 9)

    s += svg_footer(1)
    return s


# ============================================================
# LESSON 2: Роль бактерий в природе и жизни человека
# ============================================================
def lesson2():
    s = svg_header("Роль бактерий в природе и жизни человека", 2)

    # === Top left: Decomposition cycle ===
    s += box(20, 72, 385, 250, fill=WHITE, stroke=PRIMARY)
    s += label(212, 92, "Круговорот веществ", ACCENT, 12, "middle", True)

    # Organic remains
    s += f'<rect x="100" y="115" width="120" height="30" rx="6" fill="{BROWN_LIGHT}" stroke="{BROWN_MED}" stroke-width="1.5"/>'
    s += label(160, 134, "Остатки организмов", DARK, 9, "middle", True)

    # Arrow down to bacteria
    s += arrow_line(160, 150, 160, 175)

    # Bacteria (decomposers)
    s += f'<ellipse cx="160" cy="200" rx="40" ry="18" fill="#BBF7D0" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>'
    s += label(160, 204, "Бактерии-редуценты", DARK, 8, "middle", True)

    # Arrow down to minerals
    s += arrow_line(160, 222, 160, 248)

    # Mineral substances
    s += f'<rect x="100" y="255" width="120" height="30" rx="6" fill="{PRIMARY_LIGHT}" stroke="{PRIMARY}" stroke-width="1.5"/>'
    s += label(160, 274, "Минеральные вещества", DARK, 8, "middle", True)

    # Arrow right to plants
    s += arrow_line(225, 270, 270, 270)

    # Plants
    s += f'<rect x="280" y="255" width="80" height="30" rx="6" fill="#D1FAE5" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>'
    s += label(320, 274, "Растения", PRIMARY_DARK, 9, "middle", True)

    # Arrow up from plants to organic
    s += arrow_line(320, 250, 320, 150)
    s += label(335, 200, "Органические", GRAY, 8)
    s += label(335, 212, "вещества", GRAY, 8)

    # Right side - nitrogen cycle
    s += label(300, 120, "Азотфиксация:", ACCENT, 10, "start", True)
    s += label(300, 136, "N₂ → NH₃", DARK, 9)
    s += label(300, 152, "Клубеньковые бактерии", GRAY, 8)
    s += label(300, 165, "на корнях бобовых", GRAY, 8)

    # === Top right: Beneficial bacteria ===
    s += box(420, 72, 370, 250, fill=WHITE, stroke=PRIMARY)
    s += label(605, 92, "Полезные бактерии", ACCENT, 12, "middle", True)

    beneficial = [
        ("Молочнокислые", "Кисломолочные продукты,", "#FDE68A", "квашение, силос"),
        ("Клубеньковые", "Связывают азот из воздуха,", "#BBF7D0", "обогащают почву"),
        ("Почвенные", "Разлагают органику,", PRIMARY_LIGHT, "образуют перегной"),
        ("Кишечные", "Синтез витаминов B и K,", "#BFDBFE", "защита от патогенов"),
        ("Бактерии брожения", "Производство уксуса,", "#E9D5FF", "сыра, вина"),
    ]
    yy = 112
    for name, desc, clr, desc2 in beneficial:
        s += f'<rect x="435" y="{yy}" width="14" height="14" rx="3" fill="{clr}" stroke="{GRAY}" stroke-width="0.5"/>'
        s += label(456, yy + 11, name, ACCENT, 10, "start", True)
        s += label(456, yy + 24, desc, DARK, 8)
        s += label(456, yy + 35, desc2, GRAY, 8)
        yy += 42

    # === Bottom left: Harmful bacteria ===
    s += box(20, 335, 385, 250, fill=WHITE, stroke=RED)
    s += label(212, 355, "Вредные бактерии (патогены)", RED, 12, "middle", True)

    diseases = [
        ("Туберкулёз", "Mycobacterium tuberculosis"),
        ("Холера", "Vibrio cholerae"),
        ("Столбняк", "Clostridium tetani"),
        ("Дифтерия", "Corynebacterium diphtheriae"),
        ("Сальмонеллёз", "Salmonella"),
        ("Ботулизм", "Clostridium botulinum"),
    ]
    yy = 378
    for disease, bacterium in diseases:
        s += f'<circle cx="40" cy="{yy}" r="5" fill="#FECACA" stroke="{RED}" stroke-width="1"/>'
        s += label(52, yy + 4, disease, DARK, 10, "start", True)
        s += label(160, yy + 4, f"({bacterium})", GRAY, 8)
        yy += 24

    s += label(35, 535, "Меры профилактики:", ACCENT, 10, "start", True)
    s += label(35, 552, "Вакцинация, гигиена, пастеризация,", DARK, 9)
    s += label(35, 567, "стерилизация, антибиотики", DARK, 9)

    # === Bottom right: Bacteria in industry ===
    s += box(420, 335, 370, 250, fill=WHITE, stroke=PRIMARY)
    s += label(605, 355, "Бактерии в промышленности", ACCENT, 12, "middle", True)

    # Food industry
    s += f'<rect x="435" y="370" width="340" height="50" rx="6" fill="{PRIMARY_LIGHTER}"/>'
    s += label(445, 388, "Пищевая промышленность", ACCENT, 10, "start", True)
    s += label(445, 403, "Йогурт, кефир, сыр, квашеная капуста,", DARK, 9)
    s += label(445, 416, "уксус, силос для животных", DARK, 9)

    # Medicine
    s += f'<rect x="435" y="428" width="340" height="40" rx="6" fill="#DBEAFE"/>'
    s += label(445, 446, "Медицина", BLUE, 10, "start", True)
    s += label(445, 460, "Антибиотики (стрептомицин), инсулин, витамины", DARK, 9)

    # Agriculture
    s += f'<rect x="435" y="476" width="340" height="40" rx="6" fill="#D1FAE5"/>'
    s += label(445, 494, "Сельское хозяйство", PRIMARY_DARK, 10, "start", True)
    s += label(445, 508, "Азотфиксация, силосование, компостирование", DARK, 9)

    # Biotechnology
    s += f'<rect x="435" y="524" width="340" height="40" rx="6" fill="#E9D5FF"/>'
    s += label(445, 542, "Биотехнология", PURPLE, 10, "start", True)
    s += label(445, 556, "Генно-инженерные бактерии: инсулин, гормоны", DARK, 9)

    s += svg_footer(2)
    return s


# ============================================================
# LESSON 3: Общая характеристика грибов
# ============================================================
def lesson3():
    s = svg_header("Общая характеристика грибов", 3)

    # === Left: Mushroom structure diagram ===
    s += box(20, 72, 350, 390, fill=WHITE, stroke=PRIMARY)
    s += label(195, 92, "Строение шляпочного гриба", ACCENT, 12, "middle", True)

    # Cap
    s += f'<path d="M110,175 Q195,110 280,175 Z" fill="#D97706" stroke="{BROWN}" stroke-width="2"/>'
    # Cap underside (gills)
    s += f'<path d="M130,175 Q195,195 260,175" fill="#FDE68A" stroke="{BROWN_MED}" stroke-width="1"/>'
    for i in range(8):
        xx = 140 + i * 16
        s += f'<line x1="{xx}" y1="175" x2="{xx + 5}" y2="190" stroke="{BROWN_MED}" stroke-width="0.8"/>'

    # Stipe (stem)
    s += f'<rect x="175" y="195" width="40" height="140" rx="5" fill="#FDE68A" stroke="{BROWN_MED}" stroke-width="1.5"/>'

    # Ring on stipe
    s += f'<rect x="170" y="230" width="50" height="8" rx="3" fill="{WHITE}" stroke="{BROWN_MED}" stroke-width="1"/>'

    # Mycelium (underground)
    s += f'<path d="M175,335 Q150,360 130,380 Q115,395 100,400" fill="none" stroke="{GRAY}" stroke-width="2"/>'
    s += f'<path d="M195,340 Q180,365 170,390 Q160,410 155,430" fill="none" stroke="{GRAY}" stroke-width="2"/>'
    s += f'<path d="M210,340 Q230,370 250,395 Q265,410 275,420" fill="none" stroke="{GRAY}" stroke-width="2"/>'
    s += f'<path d="M215,335 Q240,355 260,370 Q280,385 290,390" fill="none" stroke="{GRAY}" stroke-width="1.5"/>'

    # Hyphae detail
    s += f'<path d="M130,380 Q125,400 135,415 Q140,425 130,435" fill="none" stroke="{GRAY}" stroke-width="1"/>'
    s += f'<path d="M170,390 Q165,410 175,425" fill="none" stroke="{GRAY}" stroke-width="1"/>'

    # Ground line
    s += f'<line x1="90" y1="335" x2="300" y2="335" stroke="{BROWN}" stroke-width="1.5" stroke-dasharray="4,2"/>'
    s += label(310, 333, "Почва", BROWN, 9)

    # Pointer labels
    s += pointer(195, 130, 300, 120)
    s += label(305, 123, "Шляпка", ACCENT, 10, "start", True)

    s += pointer(240, 180, 300, 180)
    s += label(305, 183, "Гименофор (пластинки)", ACCENT, 9, "start", True)

    s += pointer(215, 230, 280, 230)
    s += label(285, 233, "Кольцо", ACCENT, 10, "start", True)

    s += pointer(215, 280, 280, 280)
    s += label(285, 283, "Ножка", ACCENT, 10, "start", True)

    s += pointer(195, 370, 260, 370)
    s += label(265, 373, "Грибница (мицелий)", ACCENT, 9, "start", True)

    # === Right top: Hyphae and mycelium ===
    s += box(385, 72, 405, 180, fill=WHITE, stroke=PRIMARY)
    s += label(587, 92, "Гифы и мицелий", ACCENT, 12, "middle", True)

    # Hyphae threads
    s += f'<path d="M410,130 Q440,120 460,135 Q480,150 510,140 Q530,130 550,145" fill="none" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>'
    s += f'<path d="M410,150 Q435,145 455,160 Q470,175 500,165 Q520,155 555,168" fill="none" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>'
    # Septum
    s += f'<line x1="460" y1="130" x2="460" y2="140" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>'
    s += f'<line x1="510" y1="135" x2="510" y2="145" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>'
    s += label(420, 115, "Септа", ACCENT, 8)

    # Nuclei in cells
    s += f'<circle cx="430" cy="136" r="4" fill="{PRIMARY}" opacity="0.5"/>'
    s += f'<circle cx="480" cy="143" r="4" fill="{PRIMARY}" opacity="0.5"/>'

    s += label(560, 135, "Членистые гифы", DARK, 9, "start", True)
    s += label(560, 150, "(с перегородками)", GRAY, 8)

    # Non-septate hyphae
    s += f'<path d="M410,200 Q445,190 470,205 Q500,220 540,210 Q560,200 580,215" fill="none" stroke="{ORANGE}" stroke-width="3"/>'
    # Multiple nuclei
    for nx in [425, 450, 475, 500, 525, 550]:
        s += f'<circle cx="{nx}" cy="202" r="3" fill="{ORANGE}" opacity="0.6"/>'

    s += label(590, 205, "Нечленистые гифы", DARK, 9, "start", True)
    s += label(590, 220, "(многоядерные)", GRAY, 8)

    # === Right middle: Characteristics ===
    s += box(385, 265, 405, 197, fill=WHITE, stroke=PRIMARY)
    s += label(587, 285, "Характеристика грибов", ACCENT, 12, "middle", True)

    chars = [
        ("Царство:", "Грибы (Fungi) — отдельное царство"),
        ("Признаки растений:", "неподвижны, клеточная стенка,"),
        ("", "размножение спорами"),
        ("Признаки животных:", "гетеротрофы, запасной гликоген,"),
        ("", "хитин в стенке"),
        ("Клеточная стенка:", "хитин (не целлюлоза!)"),
        ("Запасное вещество:", "гликоген (не крахмал!)"),
        ("Питание:", "гетеротрофное (осмотрофное)"),
        ("Виды питания:", "сапротрофы, паразиты, симбионты"),
    ]
    yy = 305
    for title, desc in chars:
        if title:
            s += label(400, yy, title, ACCENT, 9, "start", True)
            s += label(510, yy, desc, DARK, 9)
        else:
            s += label(510, yy, desc, DARK, 9)
        yy += 17

    # === Bottom: Spore reproduction ===
    s += box(20, 475, 350, 110, fill=WHITE, stroke=PRIMARY)
    s += label(195, 495, "Размножение грибов", ACCENT, 11, "middle", True)

    # Spore
    s += f'<circle cx="55" cy="525" r="8" fill="{PRIMARY_LIGHT}" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>'
    s += label(55, 529, "С", WHITE, 7, "middle", True)
    s += arrow_line(70, 525, 100, 525)
    s += label(75, 518, "Спора", ACCENT, 8)

    # Hyphae growing
    s += f'<path d="M105,525 Q115,515 120,525 Q130,540 140,530" fill="none" stroke="{PRIMARY_DARK}" stroke-width="2"/>'
    s += arrow_line(145, 530, 175, 530)

    # Mycelium
    s += f'<path d="M180,530 Q190,520 200,530 Q210,545 225,535 Q235,525 250,535" fill="none" stroke="{GRAY}" stroke-width="1.5"/>'
    s += f'<path d="M190,530 Q195,540 210,545" fill="none" stroke="{GRAY}" stroke-width="1"/>'
    s += label(195, 555, "Мицелий", GRAY, 8, "middle")

    # Vegetative, asexual, sexual
    s += label(270, 515, "Виды размножения:", ACCENT, 9, "start", True)
    s += label(270, 530, "• Вегетативное (частями мицелия)", DARK, 8)
    s += label(270, 544, "• Бесполое (спорами)", DARK, 8)
    s += label(270, 558, "• Половое (слияние гамет)", DARK, 8)

    # Spore types
    s += box(385, 475, 405, 110, fill=WHITE, stroke=PRIMARY)
    s += label(587, 495, "Типы спор", ACCENT, 11, "middle", True)

    spore_types = [
        ("Экзоспоры", "на концах гиф (конидии)", PRIMARY),
        ("Эндоспоры", "внутри спорангиев", ORANGE),
        ("Зооспоры", "с жгутиками (подвижные)", BLUE),
    ]
    yy = 515
    for name, desc, clr in spore_types:
        s += f'<circle cx="410" cy="{yy}" r="6" fill="{clr}" opacity="0.4" stroke="{clr}" stroke-width="1.5"/>'
        s += label(425, yy + 4, name, ACCENT, 10, "start", True)
        s += label(510, yy + 4, desc, DARK, 9)
        yy += 22

    s += svg_footer(3)
    return s


# ============================================================
# LESSON 4: Значение грибов
# ============================================================
def lesson4():
    s = svg_header("Значение грибов", 4)

    # === Top left: Edible vs Poisonous ===
    s += box(20, 72, 385, 260, fill=WHITE, stroke=PRIMARY)
    s += label(212, 92, "Съедобные и ядовитые грибы", ACCENT, 12, "middle", True)

    # Edible column header
    s += f'<rect x="35" y="105" width="165" height="20" rx="4" fill="{PRIMARY}" opacity="0.2"/>'
    s += label(117, 119, "Съедобные", PRIMARY_DARK, 10, "middle", True)

    edible = [
        ("Белый гриб", "#D97706"),
        ("Подберёзовик", "#B45309"),
        ("Лисичка", "#F59E0B"),
        ("Шампиньон", "#F5F5DC"),
        ("Опёнок", "#D97706"),
    ]
    yy = 135
    for name, clr in edible:
        # Simple mushroom icon
        s += f'<path d="M55,{yy + 8} Q63,{yy} 71,{yy + 8} Z" fill="{clr}" stroke="{BROWN}" stroke-width="0.8"/>'
        s += f'<rect x="61" y="{yy + 8}" width="4" height="8" fill="#FDE68A" stroke="{BROWN_MED}" stroke-width="0.5"/>'
        s += label(82, yy + 12, name, DARK, 9)
        yy += 24

    # Poisonous column header
    s += f'<rect x="210" y="105" width="175" height="20" rx="4" fill="#FEE2E2"/>'
    s += label(297, 119, "Ядовитые", RED, 10, "middle", True)

    poisonous = [
        ("Бледная поганка ☠", "#E5E5E5"),
        ("Мухомор красный ☠", "#EF4444"),
        ("Ложный опёнок ☠", "#B45309"),
        ("Сатанинский гриб ☠", "#DC2626"),
    ]
    yy = 135
    for name, clr in poisonous:
        s += f'<path d="M230,{yy + 8} Q238,{yy} 246,{yy + 8} Z" fill="{clr}" stroke="{RED}" stroke-width="0.8"/>'
        s += f'<rect x="236" y="{yy + 8}" width="4" height="8" fill="#FDE68A" stroke="{RED}" stroke-width="0.5"/>'
        s += label(255, yy + 12, name, RED, 9)
        yy += 24

    # Warning box
    s += f'<rect x="35" y="275" width="355" height="45" rx="6" fill="#FEE2E2" stroke="{RED}" stroke-width="1"/>'
    s += label(212, 295, "Бледная поганка — смертельно ядовита!", RED, 10, "middle", True)
    s += label(212, 310, "Не имеет неприятного запаха или вкуса!", DARK, 9, "middle")

    # === Top right: Antibiotics and medicine ===
    s += box(420, 72, 370, 130, fill=WHITE, stroke=PRIMARY)
    s += label(605, 92, "Антибиотики", ACCENT, 12, "middle", True)

    s += label(435, 115, "Пенициллин — первый антибиотик", ACCENT, 10, "start", True)
    s += label(435, 132, "Открыт А. Флемингом в 1928 г.", DARK, 9)
    s += label(435, 148, "Получен из плесневого гриба", DARK, 9)
    s += label(435, 164, "Penicillium notatum", GRAY, 9)
    s += label(435, 182, "Спас миллионы жизней от бактериальных", DARK, 9)
    s += label(435, 195, "инфекций (пневмония, сепсис и др.)", DARK, 9)

    # === Middle right: Decomposition role ===
    s += box(420, 213, 370, 119, fill=WHITE, stroke=PRIMARY)
    s += label(605, 233, "Роль в природе", ACCENT, 12, "middle", True)

    s += label(435, 255, "Редуценты — разрушают органические", DARK, 9)
    s += label(435, 270, "остатки, возвращают вещества в почву", DARK, 9)
    s += label(435, 290, "Участвуют в круговороте углерода", DARK, 9)
    s += label(435, 305, "и азота в природе", DARK, 9)
    s += label(435, 322, "Без грибов Земля покрылась бы", ACCENT, 9)
    s += label(435, 335, "слоем мёртвых остатков!", ACCENT, 9)

    # === Bottom: Mycorrhiza ===
    s += box(20, 345, 385, 240, fill=WHITE, stroke=PRIMARY)
    s += label(212, 365, "Микориза (грибокорень)", ACCENT, 12, "middle", True)

    # Tree root
    s += f'<path d="M80,420 Q120,400 160,410 Q200,420 240,415 Q280,405 320,410" fill="none" stroke="{BROWN}" stroke-width="4"/>'
    # Smaller roots
    s += f'<path d="M120,415 Q130,440 125,460" fill="none" stroke="{BROWN}" stroke-width="2"/>'
    s += f'<path d="M200,420 Q210,445 205,465" fill="none" stroke="{BROWN}" stroke-width="2"/>'
    s += f'<path d="M280,412 Q290,435 285,455" fill="none" stroke="{BROWN}" stroke-width="2"/>'

    # Fungal hyphae around roots
    for rx in [100, 140, 190, 230, 270]:
        s += f'<path d="M{rx},415 Q{rx + 5},430 {rx - 3},445 Q{rx + 2},460 {rx - 5},475" fill="none" stroke="{PRIMARY}" stroke-width="1.5"/>'
        s += f'<path d="M{rx + 10},418 Q{rx + 15},432 {rx + 8},448" fill="none" stroke="{PRIMARY}" stroke-width="1"/>'

    # Labels
    s += pointer(120, 460, 50, 480)
    s += label(30, 493, "Гифы гриба", PRIMARY_DARK, 9, "start", True)

    s += pointer(200, 420, 50, 420)
    s += label(30, 423, "Корень растения", BROWN, 9, "start", True)

    s += label(35, 510, "Симбиоз: гриб даёт воду и минералы,", ACCENT, 9, "start", True)
    s += label(35, 525, "растение — органические вещества", DARK, 9)
    s += label(35, 545, "80% растений образуют микоризу!", ACCENT, 9)
    s += label(35, 565, "Белый гриб, подберёзовик —", DARK, 9)
    s += label(35, 578, "микоризообразователи", DARK, 9)

    # === Bottom right: Other uses ===
    s += box(420, 345, 370, 240, fill=WHITE, stroke=PRIMARY)
    s += label(605, 365, "Использование грибов", ACCENT, 12, "middle", True)

    uses = [
        ("Пищевое", "Шампиньоны, вешенки — выращивание", PRIMARY, "на фермах во всём мире"),
        ("Медицина", "Антибиотики, иммуностимуляторы", BLUE, "(шиитаке, рейши, чага)"),
        ("Хлебопечение", "Дрожжи (Saccharomyces cerevisiae)", ORANGE, "— брожение теста"),
        ("Пивоварение", "Дрожжи — спиртовое брожение:", YELLOW, "глюкоза → этанол + CO₂"),
        ("Сыроделие", "Плесневые грибы (Penicillium)", PRIMARY, "для сыров с плесенью"),
        ("Биотехнология", "Получение лимонной кислоты,", PURPLE, "ферментов, витаминов"),
    ]
    yy = 388
    for title, desc, clr, desc2 in uses:
        s += f'<rect x="435" y="{yy - 8}" width="10" height="10" rx="2" fill="{clr}" opacity="0.5"/>'
        s += label(452, yy, title, ACCENT, 10, "start", True)
        s += label(520, yy, desc, DARK, 8)
        s += label(440, yy + 13, desc2, GRAY, 8)
        yy += 30

    s += svg_footer(4)
    return s


# ============================================================
# LESSON 5: Водоросли
# ============================================================
def lesson5():
    s = svg_header("Водоросли", 5)

    # === Left: Types of algae ===
    s += box(20, 72, 370, 280, fill=WHITE, stroke=PRIMARY)
    s += label(205, 92, "Типы водорослей", ACCENT, 12, "middle", True)

    # Green algae
    s += f'<rect x="35" y="108" width="340" height="50" rx="6" fill="#D1FAE5" opacity="0.5"/>'
    s += label(50, 127, "Зелёные водоросли", ACCENT, 11, "start", True)
    s += label(50, 142, "Хлорофилл a + b, хроматофоры", DARK, 9)
    # Simple green algae shape
    s += f'<circle cx="310" cy="130" r="12" fill="#22C55E" stroke="#15803D" stroke-width="1.5"/>'
    s += f'<circle cx="340" cy="125" r="10" fill="#22C55E" stroke="#15803D" stroke-width="1.5"/>'
    s += f'<line x1="310" y1="142" x2="310" y2="155" stroke="#15803D" stroke-width="1"/>'
    s += f'<line x1="340" y1="135" x2="340" y2="150" stroke="#15803D" stroke-width="1"/>'

    # Brown algae
    s += f'<rect x="35" y="165" width="340" height="50" rx="6" fill="#FEF3C7" opacity="0.5"/>'
    s += label(50, 184, "Бурые водоросли", BROWN_MED, 11, "start", True)
    s += label(50, 199, "Фукоксантин, многоклеточные, морские", DARK, 9)
    # Kelp shape
    s += f'<path d="M300,175 Q310,170 305,195 Q315,200 300,210 Q290,205 295,195 Q285,190 300,175Z" fill="#92400E" stroke="#78350F" stroke-width="1.5"/>'
    s += f'<path d="M325,175 Q335,172 330,190 Q340,195 330,205 Q320,200 323,190 Q313,185 325,175Z" fill="#92400E" stroke="#78350F" stroke-width="1.5"/>'

    # Red algae
    s += f'<rect x="35" y="222" width="340" height="50" rx="6" fill="#FEE2E2" opacity="0.5"/>'
    s += label(50, 241, "Красные водоросли", RED, 11, "start", True)
    s += label(50, 256, "Фикоэритрин, глубоководные (до 200 м)", DARK, 9)
    # Red algae shape
    s += f'<path d="M310,235 Q320,230 325,240 Q330,250 320,255 Q310,250 305,245Z" fill="#DC2626" stroke="#991B1B" stroke-width="1.5"/>'
    s += f'<path d="M335,238 Q342,233 345,243 Q348,253 340,255 Q333,250 330,245Z" fill="#DC2626" stroke="#991B1B" stroke-width="1.5"/>'

    # Diatoms
    s += f'<rect x="35" y="279" width="340" height="50" rx="6" fill="#DBEAFE" opacity="0.5"/>'
    s += label(50, 298, "Диатомеи", BLUE, 11, "start", True)
    s += label(50, 313, "Кремниевый панцирь, планктон", DARK, 9)
    s += f'<ellipse cx="320" cy="300" rx="18" ry="8" fill="none" stroke="{BLUE}" stroke-width="2"/>'
    s += f'<ellipse cx="345" cy="302" rx="15" ry="7" fill="none" stroke="{BLUE}" stroke-width="2"/>'

    # === Right top: Unicellular algae ===
    s += box(405, 72, 390, 175, fill=WHITE, stroke=PRIMARY)
    s += label(600, 92, "Одноклеточная водоросль", ACCENT, 12, "middle", True)

    # Chlamydomonas
    # Cell body
    s += f'<ellipse cx="540" cy="170" rx="40" ry="30" fill="#D1FAE5" stroke="#15803D" stroke-width="2"/>'
    # Chloroplast (cup-shaped)
    s += f'<path d="M515,160 Q520,185 540,190 Q560,185 565,160 Q555,155 540,152 Q525,155 515,160Z" fill="#22C55E" stroke="#15803D" stroke-width="1"/>'
    # Nucleus
    s += f'<circle cx="540" cy="170" r="8" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>'
    s += label(540, 173, "Ядро", ACCENT, 6, "middle", True)
    # Eye spot
    s += f'<circle cx="525" cy="158" r="4" fill="{RED}" stroke="#991B1B" stroke-width="0.8"/>'
    # Flagella
    s += f'<path d="M520,145 Q510,125 515,110" fill="none" stroke="{GRAY}" stroke-width="1.5"/>'
    s += f'<path d="M530,143 Q525,120 535,108" fill="none" stroke="{GRAY}" stroke-width="1.5"/>'

    # Labels
    s += pointer(540, 145, 600, 125)
    s += label(605, 128, "Жгутики", ACCENT, 9, "start", True)
    s += pointer(525, 158, 480, 140)
    s += label(435, 143, "Стигма (глазок)", ACCENT, 9, "start", True)
    s += pointer(510, 175, 450, 180)
    s += label(410, 183, "Хроматофор", ACCENT, 9, "end", True)
    s += pointer(560, 195, 620, 195)
    s += label(625, 198, "Хламидомонада", PRIMARY_DARK, 9, "start", True)

    # === Right bottom: Multicellular algae ===
    s += box(405, 260, 390, 120, fill=WHITE, stroke=PRIMARY)
    s += label(600, 280, "Многоклеточные водоросли", ACCENT, 12, "middle", True)

    # Spirogyra
    s += label(420, 300, "Спирогира — нитчатая водоросль", ACCENT, 10, "start", True)
    # Chain of cells
    for i in range(5):
        cx = 435 + i * 32
        s += f'<rect x="{cx}" y="310" width="28" height="20" rx="4" fill="#D1FAE5" stroke="#15803D" stroke-width="1.2"/>'
        # Spiral chloroplast
        s += f'<path d="M{cx + 3},318 Q{cx + 8},312 {cx + 14},318 Q{cx + 20},324 {cx + 25},318" fill="none" stroke="#22C55E" stroke-width="1.5"/>'
    s += label(420, 345, "Ламинария (морская капуста) — до 20 м", DARK, 9)
    s += label(420, 360, "Саргассум — образует плавучие леса", DARK, 9)

    # === Bottom: Key facts ===
    s += box(20, 365, 770, 220, fill=WHITE, stroke=PRIMARY)
    s += label(400, 385, "Ключевые особенности водорослей", ACCENT, 12, "middle", True)

    # Two columns
    s += label(35, 408, "Общая характеристика:", ACCENT, 10, "start", True)
    left_facts = [
        "• Низшие растения — нет корней, стеблей, листьев",
        "• Тело — слоевище (таллом)",
        "• Орган движения — жгутики (у одноклеточных)",
        "• Хроматофоры — пластиды с пигментами",
        "• Размножение: вегетативное, бесполое, половое",
    ]
    yy = 425
    for f in left_facts:
        s += label(35, yy, f, DARK, 9)
        yy += 16

    s += label(420, 408, "Значение водорослей:", ACCENT, 10, "start", True)
    right_facts = [
        "• Фотосинтез — 80% кислорода атмосферы!",
        "• Начало пищевых цепей в водоёмах",
        "• Пища: морская капуста, нори, агар-агар",
        "• Агар-агар — из красных водорослей",
        "• Альгинаты — загустители в промышленности",
        "• «Цветение» воды — массовое размножение",
        "  водорослей → ухудшает качество воды",
    ]
    yy = 425
    for f in right_facts:
        s += label(420, yy, f, DARK, 9)
        yy += 16

    # Pigment table
    s += f'<rect x="35" y="510" width="740" height="60" rx="4" fill="{PRIMARY_LIGHTER}"/>'
    s += label(400, 527, "Пигменты водорослей:", ACCENT, 10, "middle", True)
    s += f'<rect x="50" y="537" width="30" height="14" rx="3" fill="#22C55E"/>'
    s += label(85, 548, "Зелёные: хлорофилл a+b", DARK, 9)
    s += f'<rect x="270" y="537" width="30" height="14" rx="3" fill="#92400E"/>'
    s += label(305, 548, "Бурые: хлорофилл + фукоксантин", DARK, 9)
    s += f'<rect x="520" y="537" width="30" height="14" rx="3" fill="#DC2626"/>'
    s += label(555, 548, "Красные: хлорофилл + фикоэритрин", DARK, 9)

    s += svg_footer(5)
    return s


# ============================================================
# LESSON 6: Мхи, папоротники, голосеменные
# ============================================================
def lesson6():
    s = svg_header("Мхи, папоротники, голосеменные", 6)

    # === Moss section ===
    s += box(20, 72, 250, 270, fill=WHITE, stroke=PRIMARY)
    s += label(145, 92, "Мхи (Bryophyta)", ACCENT, 11, "middle", True)

    # Moss plant
    # Stem
    s += f'<line x1="120" y1="140" x2="120" y2="260" stroke="#15803D" stroke-width="3"/>'
    # Leaves
    for yy in [150, 170, 190, 210, 230]:
        s += f'<ellipse cx="105" cy="{yy}" rx="12" ry="6" fill="#22C55E" stroke="#15803D" stroke-width="0.8"/>'
        s += f'<ellipse cx="135" cy="{yy + 10}" rx="12" ry="6" fill="#22C55E" stroke="#15803D" stroke-width="0.8"/>'
    # Capsule (sporogonium)
    s += f'<line x1="120" y1="140" x2="120" y2="115" stroke="#15803D" stroke-width="1.5"/>'
    s += f'<ellipse cx="120" cy="112" rx="10" ry="14" fill="#D97706" stroke="{BROWN}" stroke-width="1.5"/>'
    s += f'<rect x="116" y="98" width="8" height="5" rx="2" fill="{WHITE}" stroke="{BROWN_MED}" stroke-width="0.8"/>'

    # Rhizoids
    s += f'<line x1="115" y1="260" x2="108" y2="280" stroke="{GRAY}" stroke-width="1"/>'
    s += f'<line x1="120" y1="260" x2="120" y2="282" stroke="{GRAY}" stroke-width="1"/>'
    s += f'<line x1="125" y1="260" x2="132" y2="280" stroke="{GRAY}" stroke-width="1"/>'

    # Labels
    s += pointer(130, 108, 160, 105)
    s += label(165, 108, "Спорангий", ACCENT, 9, "start", True)
    s += pointer(130, 140, 165, 140)
    s += label(170, 143, "Ножка", ACCENT, 9, "start", True)
    s += pointer(120, 270, 160, 270)
    s += label(165, 273, "Ризоиды", GRAY, 9, "start", True)

    # Key facts
    s += label(35, 300, "Особенности:", ACCENT, 9, "start", True)
    s += label(35, 314, "• Нет корней (ризоиды)", DARK, 8)
    s += label(35, 327, "• Нет проводящей системы", DARK, 8)
    s += label(35, 340, "• Споровые растения", DARK, 8)
    s += label(35, 353, "• Кукушкин лён, сфагнум", DARK, 8)

    # === Fern section ===
    s += box(285, 72, 260, 270, fill=WHITE, stroke=PRIMARY)
    s += label(415, 92, "Папоротники", ACCENT, 11, "middle", True)

    # Fern frond
    # Central rachis
    s += f'<line x1="380" y1="310" x2="380" y2="130" stroke="#15803D" stroke-width="3"/>'
    # Pinnae (leaflets)
    for yy in [140, 165, 190, 215, 240, 265]:
        # Left pinna
        s += f'<path d="M380,{yy} Q365,{yy - 10} 345,{yy} Q365,{yy + 5} 380,{yy}" fill="#22C55E" stroke="#15803D" stroke-width="0.8"/>'
        # Right pinna
        s += f'<path d="M380,{yy} Q395,{yy - 10} 415,{yy} Q395,{yy + 5} 380,{yy}" fill="#22C55E" stroke="#15803D" stroke-width="0.8"/>'

    # Coiled young frond (fiddlehead)
    s += f'<path d="M380,130 Q370,120 375,110 Q382,100 380,95" fill="none" stroke="#15803D" stroke-width="2.5"/>'

    # Sorus on back of leaf
    s += f'<circle cx="360" cy="200" r="4" fill="#D97706" stroke="{BROWN}" stroke-width="0.8"/>'
    s += f'<circle cx="400" cy="215" r="4" fill="#D97706" stroke="{BROWN}" stroke-width="0.8"/>'

    # Labels
    s += pointer(360, 200, 310, 200)
    s += label(295, 203, "Сорусы", ACCENT, 9, "end", True)
    s += label(295, 215, "(споры)", GRAY, 8)

    # Root
    s += f'<line x1="380" y1="310" x2="370" y2="330" stroke="{BROWN}" stroke-width="2"/>'
    s += f'<line x1="380" y1="310" x2="390" y2="330" stroke="{BROWN}" stroke-width="2"/>'

    s += label(300, 314, "Особенности:", ACCENT, 9, "start", True)
    s += label(300, 328, "• Есть корни и стебель", DARK, 8)
    s += label(300, 341, "• Проводящая система", DARK, 8)
    s += label(300, 354, "• Споры на листьях (сорусы)", DARK, 8)

    # === Gymnosperm section ===
    s += box(560, 72, 230, 270, fill=WHITE, stroke=PRIMARY)
    s += label(675, 92, "Голосеменные", ACCENT, 11, "middle", True)

    # Pine tree silhouette
    s += f'<polygon points="675,120 640,200 650,200 620,270 630,270 610,330 740,330 720,270 730,270 700,200 710,200" fill="#15803D" stroke="#0F4C2A" stroke-width="1.5"/>'
    # Trunk
    s += f'<rect x="665" y="330" width="20" height="20" fill="{BROWN_MED}" stroke="{BROWN}" stroke-width="1"/>'

    # Cone
    s += f'<ellipse cx="700" cy="200" rx="12" ry="20" fill="#92400E" stroke="#78350F" stroke-width="1.5"/>'
    for i in range(5):
        yy = 190 + i * 5
        s += f'<line x1="690" y1="{yy}" x2="710" y2="{yy}" stroke="#78350F" stroke-width="0.8"/>'

    # Labels
    s += pointer(712, 200, 740, 190)
    s += label(745, 193, "Шишка", ACCENT, 9, "start", True)

    s += label(575, 314, "Особенности:", ACCENT, 9, "start", True)
    s += label(575, 328, "• Семена без плода", DARK, 8)
    s += label(575, 341, "• Хвоя вместо листьев", DARK, 8)
    s += label(575, 354, "• Сосна, ель, лиственница", DARK, 8)

    # === Bottom: Evolution & Life Cycles ===
    s += box(20, 355, 770, 95, fill=WHITE, stroke=PRIMARY)
    s += label(400, 375, "Эволюция высших растений", ACCENT, 12, "middle", True)

    # Evolution timeline
    stages = [
        ("Водоросли", 80, "#22C55E", "Нет тканей"),
        ("Мхи", 200, "#15803D", "Нет проводящей\nсистемы"),
        ("Папоротники", 360, "#059669", "Споры, есть\nткани"),
        ("Голосеменные", 520, ACCENT, "Семена, нет\nплодов"),
        ("Покрытосеменные", 680, "#065F46", "Семена в плодах"),
    ]
    # Timeline arrow
    s += arrow_line(50, 415, 760, 415, PRIMARY)

    for name, x, clr, desc in stages:
        s += f'<circle cx="{x}" cy="415" r="6" fill="{clr}" stroke="{WHITE}" stroke-width="1.5"/>'
        s += label(x, 400, name, clr, 9, "middle", True)
        s += label(x, 433, desc, GRAY, 8, "middle")

    # === Bottom facts: Spore vs Seed ===
    s += box(20, 462, 380, 125, fill=WHITE, stroke=PRIMARY)
    s += label(210, 482, "Споровые растения", ACCENT, 11, "middle", True)

    s += label(35, 500, "Мхи и папоротники размножаются спорами:", DARK, 9)
    s += label(35, 516, "• Спора → заросток → гаметы → оплодотворение", DARK, 9)
    s += label(35, 532, "• Для оплодотворения нужна вода!", ACCENT, 9)
    s += label(35, 548, "• Споры мелкие, разносятся ветром", DARK, 9)
    s += label(35, 564, "• Жизненный цикл: спорофит + гаметофит", DARK, 9)

    s += box(420, 462, 370, 125, fill=WHITE, stroke=PRIMARY)
    s += label(605, 482, "Семенные растения", ACCENT, 11, "middle", True)

    s += label(435, 500, "Голосеменные размножаются семенами:", DARK, 9)
    s += label(435, 516, "• Семя = зародыш + запас питательных", DARK, 9)
    s += label(435, 532, "• НЕ нужна вода для оплодотворения", ACCENT, 9)
    s += label(435, 548, "• Пыльца переносится ветром", DARK, 9)
    s += label(435, 564, "• Семя защищено кожурой", DARK, 9)

    s += svg_footer(6)
    return s


# ============================================================
# LESSON 7: Корень и побег
# ============================================================
def lesson7():
    s = svg_header("Корень и побег", 7)

    # === Left: Root structure ===
    s += box(20, 72, 380, 330, fill=WHITE, stroke=PRIMARY)
    s += label(210, 92, "Строение корня", ACCENT, 12, "middle", True)

    # Root cap
    s += f'<path d="M170,125 Q190,145 210,125 L205,115 L175,115 Z" fill="#FDE68A" stroke="{BROWN_MED}" stroke-width="1.5"/>'
    s += label(190, 135, "Корневой чехлик", BROWN_MED, 7, "middle", True)

    # Zone of division
    s += f'<rect x="172" y="108" width="36" height="25" rx="3" fill="#BBF7D0" stroke="#15803D" stroke-width="1.5"/>'
    # Small cells
    for i in range(3):
        for j in range(2):
            s += f'<rect x="{175 + i * 10}" y="{112 + j * 10}" width="8" height="8" fill="#22C55E" stroke="#15803D" stroke-width="0.5"/>'

    # Zone of elongation
    s += f'<rect x="175" y="85" width="30" height="22" rx="3" fill="#D1FAE5" stroke="#15803D" stroke-width="1.5"/>'
    s += label(190, 100, "Растяжения", PRIMARY_DARK, 6, "middle")

    # Zone of root hairs
    s += f'<rect x="170" y="58" width="40" height="26" rx="3" fill="#E8F5E9" stroke="#15803D" stroke-width="1.5"/>'
    # Root hairs
    for rx in [175, 183, 192, 200]:
        s += f'<line x1="{rx}" y1="58" x2="{rx - 3}" y2="44" stroke="#15803D" stroke-width="1"/>'
        s += f'<line x1="{rx}" y1="58" x2="{rx + 3}" y2="44" stroke="#15803D" stroke-width="1"/>'

    # Conducting zone
    s += f'<rect x="173" y="35" width="34" height="22" rx="3" fill="{PRIMARY_LIGHT}" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>'

    # Labels with pointers
    s += pointer(210, 42, 260, 42)
    s += label(265, 45, "Зона проведения", ACCENT, 9, "start", True)

    s += pointer(210, 70, 260, 70)
    s += label(265, 73, "Зона всасывания", ACCENT, 9, "start", True)
    s += label(265, 86, "(корневые волоски)", GRAY, 8)

    s += pointer(205, 95, 260, 95)
    s += label(265, 98, "Зона растяжения", ACCENT, 9, "start", True)

    s += pointer(208, 118, 260, 118)
    s += label(265, 121, "Зона деления", ACCENT, 9, "start", True)

    s += pointer(190, 140, 260, 145)
    s += label(265, 148, "Корневой чехлик", ACCENT, 9, "start", True)

    # === Root types (right top) ===
    s += box(420, 72, 370, 165, fill=WHITE, stroke=PRIMARY)
    s += label(605, 92, "Типы корневых систем", ACCENT, 12, "middle", True)

    # Taproot system
    s += f'<line x1="480" y1="108" x2="480" y2="200" stroke="{BROWN}" stroke-width="3"/>'
    s += f'<line x1="480" y1="130" x2="460" y2="180" stroke="{BROWN}" stroke-width="1.5"/>'
    s += f'<line x1="480" y1="130" x2="500" y2="180" stroke="{BROWN}" stroke-width="1.5"/>'
    s += f'<line x1="480" y1="140" x2="470" y2="185" stroke="{BROWN}" stroke-width="1"/>'
    s += f'<line x1="480" y1="140" x2="490" y2="185" stroke="{BROWN}" stroke-width="1"/>'
    s += label(480, 215, "Стержневая", ACCENT, 9, "middle", True)
    s += label(480, 228, "(двулетние, двудольные)", GRAY, 7)

    # Fibrous root system
    s += f'<line x1="650" y1="108" x2="635" y2="195" stroke="{BROWN}" stroke-width="2"/>'
    s += f'<line x1="650" y1="108" x2="645" y2="190" stroke="{BROWN}" stroke-width="2"/>'
    s += f'<line x1="650" y1="108" x2="655" y2="192" stroke="{BROWN}" stroke-width="2"/>'
    s += f'<line x1="650" y1="108" x2="665" y2="195" stroke="{BROWN}" stroke-width="2"/>'
    s += f'<line x1="650" y1="108" x2="675" y2="190" stroke="{BROWN}" stroke-width="2"/>'
    s += label(650, 215, "Мочковатая", ACCENT, 9, "middle", True)
    s += label(650, 228, "(однодольные, злаки)", GRAY, 7)

    # === Shoot structure (right middle) ===
    s += box(420, 250, 370, 152, fill=WHITE, stroke=PRIMARY)
    s += label(605, 270, "Строение побега", ACCENT, 12, "middle", True)

    # Stem
    s += f'<rect x="590" y="285" width="8" height="100" rx="2" fill="#22C55E" stroke="#15803D" stroke-width="1.5"/>'

    # Node
    s += f'<rect x="582" y="310" width="24" height="4" rx="1" fill="#15803D"/>'

    # Leaves
    s += f'<path d="M582,310 Q555,295 540,310 Q555,320 582,315" fill="#22C55E" stroke="#15803D" stroke-width="1"/>'
    s += f'<path d="M606,310 Q630,295 645,310 Q630,320 606,315" fill="#22C55E" stroke="#15803D" stroke-width="1"/>'

    # Terminal bud
    s += f'<ellipse cx="594" cy="283" rx="8" ry="12" fill="#D1FAE5" stroke="#15803D" stroke-width="1.5"/>'
    # Bud scales
    s += f'<path d="M586,283 Q590,275 594,278 Q598,275 602,283" fill="none" stroke="#15803D" stroke-width="1"/>'

    # Axillary bud
    s += f'<ellipse cx="580" cy="312" rx="5" ry="7" fill="#D1FAE5" stroke="#15803D" stroke-width="1"/>'

    # Internode
    s += line(606, 330, 630, 330, GRAY, 0.5, "2,2")
    s += label(635, 333, "Междоузлие", GRAY, 8)

    # Labels
    s += pointer(594, 275, 650, 278)
    s += label(655, 281, "Верхушечная почка", ACCENT, 9, "start", True)

    s += pointer(580, 310, 530, 305)
    s += label(435, 308, "Пазушная почка", ACCENT, 9, "start", True)

    s += pointer(540, 310, 480, 320)
    s += label(435, 323, "Лист", ACCENT, 9, "start", True)

    s += pointer(594, 350, 660, 350)
    s += label(665, 353, "Стебель", ACCENT, 9, "start", True)

    s += pointer(582, 315, 530, 340)
    s += label(435, 343, "Узел", ACCENT, 9, "start", True)

    # === Bottom: Vegetative organs ===
    s += box(20, 415, 380, 172, fill=WHITE, stroke=PRIMARY)
    s += label(210, 435, "Вегетативные органы растения", ACCENT, 11, "middle", True)

    organs = [
        ("Корень", "Закрепление, всасывание воды\nи минеральных веществ,\nзапасание", PRIMARY_DARK),
        ("Стебель", "Опора, транспорт веществ\n(вверх — вода и минералы,\nвниз — органические)", "#15803D"),
        ("Лист", "Фотосинтез, газообмен,\nтранспирация", "#22C55E"),
        ("Почка", "Зачаточный побег,\nобеспечивает рост", PRIMARY_LIGHT),
    ]
    yy = 455
    for name, desc, clr in organs:
        s += f'<rect x="35" y="{yy - 5}" width="12" height="12" rx="2" fill="{clr}" stroke="{GRAY}" stroke-width="0.5"/>'
        s += label(55, yy + 4, name, ACCENT, 10, "start", True)
        s += label(120, yy + 4, desc.split('\n')[0], DARK, 8)
        if '\n' in desc:
            lines = desc.split('\n')
            s += label(120, yy + 16, lines[1], DARK, 8)
            if len(lines) > 2:
                s += label(120, yy + 28, lines[2], DARK, 8)
        yy += 36

    # === Bottom right: Root functions ===
    s += box(420, 415, 370, 172, fill=WHITE, stroke=PRIMARY)
    s += label(605, 435, "Функции корня", ACCENT, 11, "middle", True)

    functions = [
        ("Анкорная", "Закрепление растения в почве"),
        ("Всасывающая", "Вода и минеральные соли"),
        ("Проводящая", "Транспорт веществ к стеблю"),
        ("Запасающая", "Накопление питательных веществ\n(корнеплоды: морковь, свёкла)"),
        ("Симбиотическая", "Микориза и клубеньки\n(азотфиксация)"),
    ]
    yy = 455
    for name, desc in functions:
        s += f'<circle cx="440" cy="{yy}" r="4" fill="{PRIMARY}" opacity="0.5"/>'
        s += label(450, yy + 4, name + ": " + desc.split('\n')[0], DARK, 9)
        if '\n' in desc:
            lines = desc.split('\n')
            s += label(450, yy + 16, lines[1], GRAY, 8)
            yy += 14
        yy += 20

    s += svg_footer(7)
    return s


# ============================================================
# LESSON 8: Лист и его функции
# ============================================================
def lesson8():
    s = svg_header("Лист и его функции", 8)

    # === Left: Leaf structure ===
    s += box(20, 72, 370, 290, fill=WHITE, stroke=PRIMARY)
    s += label(205, 92, "Внешнее строение листа", ACCENT, 12, "middle", True)

    # Leaf blade
    s += f'<path d="M180,120 Q120,180 140,250 Q160,310 200,330 Q240,310 260,250 Q280,180 220,120 Z" fill="#22C55E" stroke="#15803D" stroke-width="2"/>'
    # Midrib
    s += f'<line x1="180" y1="125" x2="200" y2="325" stroke="#15803D" stroke-width="2.5"/>'
    # Side veins
    veins = [
        (175, 150, 150, 180),
        (175, 170, 145, 205),
        (180, 195, 148, 230),
        (185, 220, 155, 255),
        (190, 245, 165, 280),
        (195, 270, 180, 300),
        (205, 150, 230, 180),
        (205, 170, 235, 205),
        (200, 195, 232, 230),
        (200, 220, 225, 255),
        (200, 245, 215, 280),
        (198, 270, 205, 300),
    ]
    for x1, y1, x2, y2 in veins:
        s += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#15803D" stroke-width="1"/>'

    # Petiole
    s += f'<line x1="200" y1="325" x2="200" y2="360" stroke="#15803D" stroke-width="3"/>'

    # Labels
    s += pointer(150, 180, 85, 170)
    s += label(30, 173, "Листовая пластинка", ACCENT, 9, "start", True)

    s += pointer(200, 325, 120, 335)
    s += label(30, 338, "Черешок", ACCENT, 9, "start", True)

    s += pointer(165, 155, 85, 145)
    s += label(30, 148, "Жилки", ACCENT, 9, "start", True)

    s += pointer(190, 260, 110, 280)
    s += label(30, 283, "Основание листа", ACCENT, 9, "start", True)

    # Leaf types
    s += label(30, 358, "Простые — 1 пластинка", DARK, 9)
    s += label(30, 373, "Сложные — несколько листочков", DARK, 9)

    # === Right top: Internal structure ===
    s += box(405, 72, 390, 290, fill=WHITE, stroke=PRIMARY)
    s += label(600, 92, "Внутреннее строение листа", ACCENT, 12, "middle", True)

    # Cross section of leaf
    # Upper epidermis
    s += f'<rect x="440" y="115" width="280" height="14" rx="2" fill="#BBF7D0" stroke="#15803D" stroke-width="1.5"/>'
    # Cuticle
    s += f'<rect x="440" y="112" width="280" height="4" rx="1" fill="{YELLOW}" opacity="0.5"/>'

    # Palisade mesophyll
    s += f'<rect x="440" y="129" width="280" height="50" rx="2" fill="#86EFAC" stroke="#15803D" stroke-width="1"/>'
    # Palisade cells
    for i in range(14):
        cx = 452 + i * 20
        s += f'<rect x="{cx}" y="132" width="8" height="40" rx="2" fill="#22C55E" stroke="#15803D" stroke-width="0.5"/>'
        # Chloroplasts
        s += f'<circle cx="{cx + 2}" cy="142" r="2.5" fill="#15803D"/>'
        s += f'<circle cx="{cx + 6}" cy="155" r="2.5" fill="#15803D"/>'

    # Spongy mesophyll
    s += f'<rect x="440" y="179" width="280" height="50" rx="2" fill="#D1FAE5" stroke="#15803D" stroke-width="1"/>'
    # Spongy cells (round, with gaps)
    for i in range(10):
        cx = 455 + i * 28
        for j in range(2):
            cy = 190 + j * 22
            s += f'<circle cx="{cx}" cy="{cy}" r="8" fill="#22C55E" stroke="#15803D" stroke-width="0.5"/>'
            s += f'<circle cx="{cx + 2}" cy="{cy - 2}" r="2" fill="#15803D"/>'

    # Lower epidermis
    s += f'<rect x="440" y="229" width="280" height="14" rx="2" fill="#BBF7D0" stroke="#15803D" stroke-width="1.5"/>'

    # Stoma
    s += f'<ellipse cx="540" cy="240" rx="14" ry="6" fill="{PRIMARY_LIGHT}" stroke="#15803D" stroke-width="1"/>'
    # Guard cells
    s += f'<path d="M530,237 Q534,233 538,237" fill="#22C55E" stroke="#15803D" stroke-width="1"/>'
    s += f'<path d="M542,237 Q546,233 550,237" fill="#22C55E" stroke="#15803D" stroke-width="1"/>'
    # Stomatal pore
    s += f'<line x1="538" y1="238" x2="542" y2="238" stroke="#15803D" stroke-width="2"/>'

    # Vascular bundle (vein)
    s += f'<rect x="575" y="129" width="12" height="100" rx="2" fill="{PRIMARY_LIGHT}" stroke="#15803D" stroke-width="1"/>'
    # Xylem
    s += f'<rect x="577" y="131" width="4" height="96" rx="1" fill="{BLUE}" opacity="0.5"/>'
    # Phloem
    s += f'<rect x="583" y="131" width="3" height="96" rx="1" fill="{ORANGE}" opacity="0.5"/>'

    # Labels with pointers
    s += pointer(440, 118, 418, 110)
    s += label(355, 110, "Кутикула", YELLOW, 8, "end", True)

    s += pointer(440, 122, 418, 125)
    s += label(340, 128, "Верхняя кожица", ACCENT, 8, "end", True)
    s += label(340, 140, "(эпидермис)", GRAY, 7)

    s += pointer(440, 145, 418, 155)
    s += label(345, 158, "Столбчатая", ACCENT, 8, "end", True)
    s += label(340, 170, "паренхима", ACCENT, 8, "end")

    s += pointer(440, 195, 418, 195)
    s += label(345, 198, "Губчатая", ACCENT, 8, "end", True)
    s += label(340, 210, "паренхима", ACCENT, 8, "end")

    s += pointer(440, 235, 418, 235)
    s += label(345, 238, "Нижняя кожица", ACCENT, 8, "end", True)

    s += pointer(550, 240, 550, 258)
    s += label(550, 270, "Устьице", ACCENT, 8, "middle", True)

    s += pointer(577, 155, 640, 155)
    s += label(645, 150, "Ксилема (вода ↑)", BLUE, 7, "start", True)
    s += label(645, 162, "Флоэма (орг. ↓)", ORANGE, 7, "start", True)

    # === Bottom: Photosynthesis ===
    s += box(20, 375, 390, 212, fill=WHITE, stroke=PRIMARY)
    s += label(215, 395, "Фотосинтез", ACCENT, 12, "middle", True)

    # Equation
    s += f'<rect x="35" y="408" width="360" height="35" rx="6" fill="{PRIMARY_LIGHTER}"/>'
    s += label(215, 420, "6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂", ACCENT, 12, "middle", True)
    s += label(215, 435, "(свет + хлорофилл)", GRAY, 9, "middle")

    # Photosynthesis diagram
    # Sun
    s += f'<circle cx="80" cy="470" r="15" fill="{YELLOW}" stroke="{ORANGE}" stroke-width="1.5"/>'
    # Sun rays
    for angle_deg in [0, 45, 90, 135, 180, 225, 270, 315]:
        rad = math.radians(angle_deg)
        rx1 = 80 + 18 * math.cos(rad)
        ry1 = 470 + 18 * math.sin(rad)
        rx2 = 80 + 25 * math.cos(rad)
        ry2 = 470 + 25 * math.sin(rad)
        s += f'<line x1="{rx1}" y1="{ry1}" x2="{rx2}" y2="{ry2}" stroke="{ORANGE}" stroke-width="1.5"/>'
    s += label(80, 474, "☀", DARK, 14, "middle")
    s += arrow_line(95, 470, 150, 470, YELLOW)

    # Leaf icon
    s += f'<ellipse cx="175" cy="470" rx="25" ry="15" fill="#22C55E" stroke="#15803D" stroke-width="1.5"/>'
    s += label(175, 474, "Лист", WHITE, 8, "middle", True)

    # Inputs
    s += arrow_line(155, 455, 175, 460, BLUE)
    s += label(110, 452, "H₂O", BLUE, 8)

    s += arrow_line(155, 488, 175, 482, GRAY)
    s += label(110, 490, "CO₂", GRAY, 8)

    # Outputs
    s += arrow_line(200, 458, 240, 450, PRIMARY)
    s += label(245, 453, "O₂", PRIMARY, 9, "start", True)

    s += arrow_line(200, 482, 240, 490, ORANGE)
    s += label(245, 493, "Глюкоза", ORANGE, 9, "start", True)

    # Conditions
    s += label(35, 520, "Условия фотосинтеза:", ACCENT, 10, "start", True)
    s += label(35, 536, "1. Свет (энергия)", DARK, 9)
    s += label(35, 550, "2. Хлорофилл (пигмент)", DARK, 9)
    s += label(35, 564, "3. CO₂ и H₂O (вещества)", DARK, 9)

    # === Bottom right: Transpiration ===
    s += box(425, 375, 370, 212, fill=WHITE, stroke=PRIMARY)
    s += label(610, 395, "Транспирация и газообмен", ACCENT, 12, "middle", True)

    # Stomata function
    # Open stoma
    s += f'<rect x="445" y="418" width="70" height="55" rx="4" fill="{PRIMARY_LIGHTER}"/>'
    s += label(480, 430, "Открытое", ACCENT, 8, "middle", True)
    s += label(480, 440, "устьице", ACCENT, 8, "middle")
    # Guard cells open
    s += f'<path d="M458,452 Q465,445 472,452" fill="#22C55E" stroke="#15803D" stroke-width="1.5"/>'
    s += f'<path d="M488,452 Q495,445 502,452" fill="#22C55E" stroke="#15803D" stroke-width="1.5"/>'
    # Opening
    s += f'<ellipse cx="480" cy="455" rx="8" ry="4" fill="{WHITE}" stroke="#15803D" stroke-width="0.5"/>'
    # Arrows for gas exchange
    s += arrow_line(460, 455, 445, 455, BLUE)
    s += label(435, 458, "O₂", BLUE, 7, "end")
    s += arrow_line(500, 455, 515, 455, GRAY)
    s += label(520, 458, "CO₂", GRAY, 7)

    # Closed stoma
    s += f'<rect x="540" y="418" width="70" height="55" rx="4" fill="#FEE2E2"/>'
    s += label(575, 430, "Закрытое", RED, 8, "middle", True)
    s += label(575, 440, "устьице", RED, 8, "middle")
    # Guard cells closed
    s += f'<path d="M553,452 Q558,449 563,452 Q568,455 563,458 Q558,461 553,458Z" fill="#22C55E" stroke="#15803D" stroke-width="1.5"/>'
    s += f'<path d="M583,452 Q588,449 593,452 Q598,455 593,458 Q588,461 583,458Z" fill="#22C55E" stroke="#15803D" stroke-width="1.5"/>'

    # Transpiration info
    s += label(440, 490, "Транспирация — испарение воды", ACCENT, 10, "start", True)
    s += label(440, 506, "через устьица:", DARK, 9)
    s += label(440, 522, "• Охлаждает растение", DARK, 9)
    s += label(440, 536, "• Поднимает воду от корней", DARK, 9)
    s += label(440, 550, "• Обеспечивает поступление минералов", DARK, 9)

    s += label(440, 570, "Газообмен: O₂ ↔ CO₂ через устьица", ACCENT, 9)

    s += svg_footer(8)
    return s


# ============================================================
# MAIN: Generate all SVGs and validate
# ============================================================
lessons = [
    (1, lesson1),
    (2, lesson2),
    (3, lesson3),
    (4, lesson4),
    (5, lesson5),
    (6, lesson6),
    (7, lesson7),
    (8, lesson8),
]

print("Generating Grade 7 Biology SVGs...")
print(f"Output directory: {OUTPUT_DIR}")
print()

results = []
for num, func in lessons:
    filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
    try:
        svg_content = func()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)

        # Validate with xml.etree.ElementTree
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            size = os.path.getsize(filepath)
            results.append((num, filepath, "OK", size))
            print(f"  Lesson {num}: OK ({size:,} bytes)")
        except ET.ParseError as e:
            results.append((num, filepath, f"XML ERROR: {e}", 0))
            print(f"  Lesson {num}: XML ERROR - {e}")
    except Exception as e:
        results.append((num, filepath, f"GEN ERROR: {e}", 0))
        print(f"  Lesson {num}: GENERATION ERROR - {e}")

print()
print("=" * 60)
print("GENERATION SUMMARY")
print("=" * 60)
ok_count = sum(1 for _, _, status, _ in results if status == "OK")
total_size = sum(size for _, _, status, size in results if status == "OK")
for num, path, status, size in results:
    status_icon = "✓" if status == "OK" else "✗"
    print(f"  {status_icon} Lesson {num}: {os.path.basename(path)} - {status} ({size:,} bytes)")

print(f"\nTotal: {ok_count}/{len(lessons)} files generated successfully")
print(f"Total size: {total_size:,} bytes")

if ok_count == len(lessons):
    print("\nAll SVGs generated and validated successfully! ✓")
else:
    print("\nSome SVGs had errors - please review above.")
