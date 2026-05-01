#!/usr/bin/env python3
"""Generate 12 Grade 8 Biology SVG lesson images."""

import os

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/biology"
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
BONE = "#FEF3C7"
BONE_DARK = "#D97706"

W = 800
H = 600

def escape(text):
    """Escape XML special characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def svg_header(title):
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
  <text x="400" y="40" text-anchor="middle" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="{WHITE}">{escape(title)}</text>
  <!-- Lesson badge -->
  <rect x="12" y="68" width="90" height="24" rx="12" fill="{PRIMARY}" opacity="0.9"/>
  <text x="57" y="84" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{WHITE}" font-weight="bold">Биология 8</text>
'''

def svg_footer():
    return '''</svg>'''

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
    s += f'<rect x="{x}" y="{y+16}" width="{w}" height="6" fill="{title_color}"/>'
    s += label(x + w/2, y + 15, title_text, WHITE, 11, "middle", True)
    s += label(x + 8, y + 38, body_text, DARK, 10)
    return s


# ============================================================
# LESSON 1: Строение скелета человека
# ============================================================
def lesson1():
    s = svg_header("Строение скелета человека")
    # Skeleton figure (simplified)
    # Skull
    s += f'<ellipse cx="280" cy="130" rx="30" ry="35" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="2"/>'
    s += label(280, 135, "Череп", BONE_DARK, 10, "middle", True)
    # Spine
    s += f'<rect x="275" y="165" width="10" height="130" rx="3" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="1.5"/>'
    for i in range(7):
        yy = 170 + i*18
        s += f'<line x1="273" y1="{yy}" x2="287" y2="{yy}" stroke="{BONE_DARK}" stroke-width="1"/>'
    # Ribcage
    s += f'<path d="M240,200 Q280,230 240,270" fill="none" stroke="{BONE_DARK}" stroke-width="2"/>'
    s += f'<path d="M260,195 Q280,225 260,265" fill="none" stroke="{BONE_DARK}" stroke-width="2"/>'
    s += f'<path d="M300,200 Q280,230 300,270" fill="none" stroke="{BONE_DARK}" stroke-width="2"/>'
    s += f'<path d="M300,195 Q280,225 300,265" fill="none" stroke="{BONE_DARK}" stroke-width="2"/>'
    # Pelvis
    s += f'<ellipse cx="280" cy="305" rx="40" ry="20" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="1.5"/>'
    # Arms
    s += f'<line x1="250" y1="190" x2="210" y2="250" stroke="{BONE_DARK}" stroke-width="3"/>'
    s += f'<line x1="210" y1="250" x2="190" y2="330" stroke="{BONE_DARK}" stroke-width="3"/>'
    s += f'<line x1="310" y1="190" x2="350" y2="250" stroke="{BONE_DARK}" stroke-width="3"/>'
    s += f'<line x1="350" y1="250" x2="370" y2="330" stroke="{BONE_DARK}" stroke-width="3"/>'
    # Legs
    s += f'<line x1="265" y1="320" x2="255" y2="420" stroke="{BONE_DARK}" stroke-width="3.5"/>'
    s += f'<line x1="255" y1="420" x2="250" y2="510" stroke="{BONE_DARK}" stroke-width="3.5"/>'
    s += f'<line x1="295" y1="320" x2="305" y2="420" stroke="{BONE_DARK}" stroke-width="3.5"/>'
    s += f'<line x1="305" y1="420" x2="310" y2="510" stroke="{BONE_DARK}" stroke-width="3.5"/>'

    # Pointer labels
    s += pointer(310, 125, 370, 115)
    s += label(375, 118, "Череп (22 кости)", ACCENT, 11, "start", True)
    s += pointer(287, 220, 350, 215)
    s += label(355, 218, "Грудная клетка", ACCENT, 11, "start", True)
    s += pointer(287, 300, 350, 300)
    s += label(355, 303, "Таз", ACCENT, 11, "start", True)
    s += pointer(210, 240, 160, 220)
    s += label(105, 223, "Плечевая кость", ACCENT, 11, "start", True)
    s += pointer(370, 310, 420, 310)
    s += label(425, 313, "Лучевая/Локтевая", ACCENT, 11, "start", True)
    s += pointer(305, 440, 360, 440)
    s += label(365, 443, "Берцовые кости", ACCENT, 11, "start", True)
    s += pointer(275, 175, 160, 175)
    s += label(105, 178, "Позвоночник (33-34 позвонка)", ACCENT, 11, "start", True)

    # Axial vs Appendicular info boxes
    s += infobox(530, 75, 255, 110, "Осевой скелет",
        "• Череп — защита мозга\n• Позвоночник — опора тела\n  (7 шейных, 12 грудных,\n   5 поясничных, 5 крестцовых,\n   4-5 копчиковых)\n• Грудная клетка — защита органов",
        PRIMARY_LIGHTER, PRIMARY_DARK)
    s += infobox(530, 200, 255, 105, "Добавочный скелет",
        "• Пояс верхних конечностей\n  (лопатки, ключицы)\n• Свободные конечности\n  (руки — 30 костей каждая)\n• Пояс нижних конечностей (таз)\n• Свободные конечности (ноги)",
        PRIMARY_LIGHTER, ACCENT)

    # Bottom section - facts
    s += box(20, 430, 490, 155, fill=WHITE, stroke=PRIMARY)
    s += label(30, 450, "Ключевые факты:", ACCENT, 13, "start", True)
    s += label(30, 470, "• Скелет человека состоит из 206 костей", DARK, 11)
    s += label(30, 488, "• Самая длинная кость — бедренная (~45 см)", DARK, 11)
    s += label(30, 506, "• Самая маленькая — стремя в ухе (3 мм)", DARK, 11)
    s += label(30, 524, "• Скелет составляет ~15% массы тела", DARK, 11)
    s += label(30, 542, "• Функции: опора, защита, движение, кроветворение", DARK, 11)
    s += label(30, 560, "• Соединения костей: неподвижные, полуподвижные, подвижные (суставы)", DARK, 11)

    # Vertebral column detail
    s += box(530, 320, 255, 130, fill=WHITE, stroke=PRIMARY)
    s += label(540, 340, "Отделы позвоночника:", ACCENT, 11, "start", True)
    sections = [("Шейный", 7, "#7DD3FC"), ("Грудной", 12, PRIMARY_LIGHT), ("Поясничный", 5, "#FDE68A"), ("Крестцовый", 5, "#FECACA"), ("Копчиковый", "4-5", "#E9D5FF")]
    yy = 355
    for name, count, clr in sections:
        s += f'<rect x="545" y="{yy}" width="12" height="14" rx="2" fill="{clr}" stroke="{GRAY}" stroke-width="0.5"/>'
        s += label(563, yy+11, f"{name} — {count} позвонков", DARK, 10)
        yy += 20

    s += label(400, 590, "Урок 1", GRAY, 10, "middle")
    s += svg_footer()
    return s


# ============================================================
# LESSON 2: Строение и виды костей
# ============================================================
def lesson2():
    s = svg_header("Строение и виды костей")
    # Cross section of a long bone
    s += box(20, 72, 360, 260, fill=WHITE, stroke=PRIMARY)
    s += label(200, 92, "Строение длинной кости", ACCENT, 13, "middle", True)

    # Bone shaft (diaphysis)
    s += f'<rect x="100" y="130" width="200" height="120" rx="10" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="2"/>'
    # Medullary cavity
    s += f'<rect x="120" y="145" width="160" height="90" rx="5" fill="#FCA5A5" stroke="{RED}" stroke-width="1"/>'
    s += label(200, 195, "Костномозговая", DARK, 9, "middle")
    s += label(200, 207, "полость", DARK, 9, "middle")
    # Compact bone layer
    s += f'<rect x="100" y="130" width="200" height="15" rx="0" fill="#FBBF24" stroke="{BONE_DARK}" stroke-width="1" opacity="0.7"/>'
    s += f'<rect x="100" y="235" width="200" height="15" rx="0" fill="#FBBF24" stroke="{BONE_DARK}" stroke-width="1" opacity="0.7"/>'
    # Periosteum
    s += f'<rect x="96" y="125" width="208" height="8" rx="3" fill="{PRIMARY}" opacity="0.5"/>'
    s += f'<rect x="96" y="247" width="208" height="8" rx="3" fill="{PRIMARY}" opacity="0.5"/>'
    # Epiphysis top
    s += f'<ellipse cx="200" cy="120" rx="55" ry="20" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="2"/>'
    # Spongy bone in epiphysis
    for i in range(5):
        for j in range(2):
            s += f'<circle cx="{165+i*18}" cy="{115+j*8}" r="3" fill="none" stroke="{BONE_DARK}" stroke-width="0.8"/>'
    # Epiphysis bottom
    s += f'<ellipse cx="200" cy="260" rx="55" ry="20" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="2"/>'
    for i in range(5):
        for j in range(2):
            s += f'<circle cx="{165+i*18}" cy="{256+j*8}" r="3" fill="none" stroke="{BONE_DARK}" stroke-width="0.8"/>'

    # Labels with pointers
    s += pointer(96, 125, 55, 110)
    s += label(10, 113, "Надкостница", ACCENT, 10, "start", True)
    s += pointer(100, 137, 55, 137)
    s += label(10, 140, "Компактное вещество", ACCENT, 10, "start", True)
    s += pointer(120, 190, 55, 170)
    s += label(10, 173, "Губчатое вещество", ACCENT, 10, "start", True)
    s += pointer(200, 260, 55, 260)
    s += label(10, 263, "Эпифиз", ACCENT, 10, "start", True)
    s += pointer(200, 190, 200, 290)
    s += label(200, 300, "Диафиз", ACCENT, 11, "middle", True)

    # Bone types section
    s += box(400, 72, 385, 260, fill=WHITE, stroke=PRIMARY)
    s += label(592, 92, "Виды костей", ACCENT, 13, "middle", True)

    # Long bone
    s += f'<rect x="420" y="115" width="20" height="70" rx="5" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="1.5"/>'
    s += f'<ellipse cx="430" cy="115" rx="12" ry="6" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="1.5"/>'
    s += f'<ellipse cx="430" cy="185" rx="12" ry="6" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="1.5"/>'
    s += label(448, 155, "Трубчатые", DARK, 10, "start", True)
    s += label(448, 168, "(бедренная, плечевая)", GRAY, 9)

    # Short bone
    s += f'<rect x="420" y="200" width="25" height="25" rx="6" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="1.5"/>'
    s += label(448, 216, "Короткие", DARK, 10, "start", True)
    s += label(448, 229, "(запястные, предплюсны)", GRAY, 9)

    # Flat bone
    s += f'<rect x="415" y="242" width="35" height="10" rx="2" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="1.5"/>'
    s += label(448, 252, "Плоские", DARK, 10, "start", True)
    s += label(448, 265, "(лопатка, рёбра, череп)", GRAY, 9)

    # Mixed bone
    s += f'<path d="M600,115 L615,130 L625,125 L640,140 L630,155 L610,150 L600,115Z" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="1.5"/>'
    s += label(650, 135, "Смешанные", DARK, 10, "start", True)
    s += label(650, 148, "(позвонки)", GRAY, 9)

    # Air bone
    s += f'<rect x="598" y="185" width="30" height="28" rx="8" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="1.5"/>'
    s += f'<ellipse cx="608" cy="199" rx="5" ry="6" fill="#E0F2FE" stroke="{GRAY}" stroke-width="0.5"/>'
    s += f'<ellipse cx="620" cy="196" rx="4" ry="5" fill="#E0F2FE" stroke="{GRAY}" stroke-width="0.5"/>'
    s += label(638, 203, "Воздухоносные", DARK, 10, "start", True)
    s += label(638, 216, "(клиновидная, решётчатая)", GRAY, 9)

    # Sesamoid
    s += f'<ellipse cx="610" cy="255" rx="8" ry="6" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="1.5"/>'
    s += label(626, 258, "Сесамовидные", DARK, 10, "start", True)
    s += label(626, 271, "(надколенник)", GRAY, 9)

    # Bottom section - bone composition
    s += box(20, 345, 765, 240, fill=WHITE, stroke=PRIMARY)
    s += label(400, 365, "Химический состав кости", ACCENT, 13, "middle", True)

    # Pie chart - organic vs inorganic
    s += f'<circle cx="160" cy="470" r="70" fill="{PRIMARY}" opacity="0.3"/>'
    s += f'<path d="M160,470 L160,400 A70,70 0 0,1 227,490 Z" fill="{PRIMARY}" opacity="0.7"/>'
    s += label(120, 435, "Органические", WHITE, 9, "middle", True)
    s += label(120, 448, "вещества", WHITE, 9, "middle", True)
    s += label(120, 461, "~30%", WHITE, 9, "middle", True)
    s += label(195, 490, "Неорганические", DARK, 9, "middle", True)
    s += label(195, 503, "вещества ~70%", DARK, 9, "middle", True)

    # Info text
    s += label(270, 395, "Органические вещества (белки — оссеин, коллаген):", ACCENT, 11, "start", True)
    s += label(270, 413, "• Придают кости упругость и эластичность", DARK, 10)
    s += label(270, 433, "Неорганические вещества (соли Ca, P):", ACCENT, 11, "start", True)
    s += label(270, 451, "• Придают кости твёрдость и прочность", DARK, 10)
    s += label(270, 475, "Свойства кости:", ACCENT, 11, "start", True)
    s += label(270, 493, "• У детей — больше органических, кости гибкие", DARK, 10)
    s += label(270, 509, "• У пожилых — больше неорганических, кости хрупкие", DARK, 10)
    s += label(270, 533, "• Оптимальное соотношение — прочность + упругость", DARK, 10)
    s += label(270, 555, "Остеоны — структурные единицы компактного вещества", DARK, 10)
    s += label(270, 571, "Клетки: остеоциты, остеобласты, остеокласты", DARK, 10)

    s += label(400, 590, "Урок 2", GRAY, 10, "middle")
    s += svg_footer()
    return s


# ============================================================
# LESSON 3: Мышцы и их работа
# ============================================================
def lesson3():
    s = svg_header("Мышцы и их работа")
    # Muscle types section
    s += box(20, 72, 245, 230, fill=WHITE, stroke=PRIMARY)
    s += label(142, 92, "Виды мышечной ткани", ACCENT, 12, "middle", True)

    # Skeletal muscle - striated
    s += f'<rect x="40" y="108" width="80" height="25" rx="4" fill="#FCA5A5" stroke="{RED}" stroke-width="1.5"/>'
    for i in range(8):
        s += f'<line x1="{50+i*10}" y1="108" x2="{50+i*10}" y2="133" stroke="{RED}" stroke-width="0.5" opacity="0.5"/>'
    s += label(130, 124, "Поперечнополосатая", DARK, 10, "start", True)
    s += label(130, 137, "(скелетная)", GRAY, 9)
    s += label(40, 153, "Произвольная, быстро утомляется", DARK, 9)

    # Smooth muscle
    s += f'<rect x="40" y="170" width="80" height="25" rx="4" fill="#BBF7D0" stroke="{PRIMARY}" stroke-width="1.5"/>'
    for i in range(4):
        s += f'<ellipse cx="{55+i*20}" cy="183" rx="8" ry="10" fill="none" stroke="{PRIMARY}" stroke-width="0.8"/>'
    s += label(130, 186, "Гладкая", DARK, 10, "start", True)
    s += label(130, 199, "(непроизвольная)", GRAY, 9)
    s += label(40, 215, "Непроизвольная, медленная", DARK, 9)

    # Cardiac muscle
    s += f'<rect x="40" y="232" width="80" height="25" rx="4" fill="#FDE68A" stroke="{YELLOW}" stroke-width="1.5"/>'
    for i in range(3):
        s += f'<path d="M{52+i*25},245 L{58+i*25},237 L{64+i*25},245 L{70+i*25},237 L{76+i*25},245" fill="none" stroke="{BONE_DARK}" stroke-width="1"/>'
    s += label(130, 248, "Сердечная", DARK, 10, "start", True)
    s += label(130, 261, "(непроизвольная)", GRAY, 9)
    s += label(40, 277, "Непроизвольная, неутомимая", DARK, 9)

    # Muscle contraction diagram
    s += box(280, 72, 505, 230, fill=WHITE, stroke=PRIMARY)
    s += label(532, 92, "Механизм сокращения мышцы", ACCENT, 12, "middle", True)

    # Relaxed muscle
    s += f'<rect x="310" y="115" width="150" height="35" rx="6" fill="#FCA5A5" stroke="{RED}" stroke-width="1.5"/>'
    s += f'<rect x="300" y="120" width="15" height="25" rx="3" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="1"/>'
    s += f'<rect x="455" y="120" width="15" height="25" rx="3" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="1"/>'
    s += label(385, 137, "Расслабленная", DARK, 10, "middle")

    # Arrow
    s += f'<path d="M385,158 L385,178" stroke="{PRIMARY}" stroke-width="2" marker-end="url(#arrow)"/>'
    s += f'<polygon points="385,183 380,175 390,175" fill="{PRIMARY}"/>'

    # Contracted muscle
    s += f'<rect x="330" y="190" width="110" height="50" rx="6" fill="#EF4444" stroke="{RED}" stroke-width="2"/>'
    s += f'<rect x="300" y="203" width="15" height="25" rx="3" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="1"/>'
    s += f'<rect x="455" y="203" width="15" height="25" rx="3" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="1"/>'
    s += label(385, 220, "Сокращённая", WHITE, 10, "middle")

    # Sarcomere detail
    s += label(560, 115, "Саркомер:", ACCENT, 11, "start", True)
    s += f'<rect x="540" y="125" width="180" height="20" rx="3" fill="#FEE2E2" stroke="{RED}" stroke-width="1"/>'
    # actin (thin)
    s += f'<rect x="540" y="125" width="45" height="20" rx="3" fill="#BFDBFE" stroke="{BLUE}" stroke-width="1"/>'
    s += f'<rect x="675" y="125" width="45" height="20" rx="3" fill="#BFDBFE" stroke="{BLUE}" stroke-width="1"/>'
    # myosin (thick)
    s += f'<rect x="600" y="128" width="60" height="14" rx="2" fill="#FCA5A5" stroke="{RED}" stroke-width="1"/>'
    s += label(560, 139, "Актин", BLUE, 8, "middle")
    s += label(630, 139, "Миозин", RED, 8, "middle")
    s += label(697, 139, "Актин", BLUE, 8, "middle")

    # Contraction steps
    s += label(510, 170, "Этапы сокращения:", ACCENT, 11, "start", True)
    steps = ["1. Нервный импульс → мышца", "2. Высвобождение Ca²⁺ из саркоплазматич. ретикулума",
             "3. Миозин связывается с актином", "4. Головки миозина совершают «гребок»",
             "5. Актиновые нити сближаются", "6. Мышца укорачивается (сокращение)"]
    for i, step in enumerate(steps):
        s += label(510, 188 + i*16, step, DARK, 9)

    # Bottom section - muscle groups
    s += box(20, 315, 385, 270, fill=WHITE, stroke=PRIMARY)
    s += label(212, 335, "Основные мышцы человека", ACCENT, 12, "middle", True)

    muscle_groups = [
        ("Голова и шея:", "мимические, жевательные, грудино-ключично-сосцевидная"),
        ("Туловище:", "трапециевидная, широчайшая спины, грудные, пресс"),
        ("Руки:", "дельтовидная, бицепс, трицепс, сгибатели/разгибатели"),
        ("Ноги:", "ягодичные, четырёхглавая, икроножная, камбаловидная"),
    ]
    yy = 358
    for title, desc in muscle_groups:
        s += label(35, yy, title, ACCENT, 10, "start", True)
        s += label(35, yy+14, desc, DARK, 9)
        yy += 36

    s += label(35, 510, "Правило рычага:", ACCENT, 10, "start", True)
    s += label(35, 526, "Кость = рычаг, сустав = точка опоры,", DARK, 9)
    s += label(35, 540, "мышца = сила, груз = сопротивление", DARK, 9)
    s += label(35, 558, "Движение — результат работы мышц-антагонистов", DARK, 9)
    s += label(35, 574, "(сгибатели + разгибатели)", GRAY, 9)

    # Work and energy
    s += box(420, 315, 365, 270, fill=WHITE, stroke=PRIMARY)
    s += label(602, 335, "Работа мышц", ACCENT, 12, "middle", True)

    s += label(435, 360, "Энергия сокращения:", ACCENT, 11, "start", True)
    s += label(435, 378, "АТФ → АДФ + энергия", DARK, 10)
    s += f'<rect x="435" y="390" width="335" height="2" fill="{LIGHT_GRAY}"/>'
    s += label(435, 408, "Динамическая работа:", ACCENT, 10, "start", True)
    s += label(435, 424, "• Изотоническое сокращение (длина меняется)", DARK, 9)
    s += label(435, 440, "• Изометрическое сокращение (длина постоянна)", DARK, 9)
    s += f'<rect x="435" y="452" width="335" height="2" fill="{LIGHT_GRAY}"/>'
    s += label(435, 468, "Утомление мышцы:", ACCENT, 10, "start", True)
    s += label(435, 484, "• Накопление молочной кислоты", DARK, 9)
    s += label(435, 498, "• Истощение запасов АТФ и гликогена", DARK, 9)
    s += label(435, 512, "• Отдых восстанавливает работоспособность", DARK, 9)
    s += f'<rect x="435" y="524" width="335" height="2" fill="{LIGHT_GRAY}"/>'
    s += label(435, 540, "Гиподинамия — недостаток движений", RED, 10, "start", True)
    s += label(435, 556, "→ ослабление мышц, нарушение осанки", DARK, 9)
    s += label(435, 572, "Тренировка → гипертрофия мышц", PRIMARY, 10, "start", True)

    s += label(400, 590, "Урок 3", GRAY, 10, "middle")
    s += svg_footer()
    return s


# ============================================================
# LESSON 4: Состав крови
# ============================================================
def lesson4():
    s = svg_header("Состав крови")
    # Blood composition pie/diagram
    s += box(20, 72, 380, 260, fill=WHITE, stroke=PRIMARY)
    s += label(210, 92, "Состав крови", ACCENT, 13, "middle", True)

    # Test tube representation
    s += f'<rect x="80" y="108" width="70" height="200" rx="5" fill="none" stroke="{DARK}" stroke-width="2"/>'
    # Plasma layer (top ~55%)
    s += f'<rect x="82" y="110" width="66" height="108" rx="3" fill="#FDE68A" opacity="0.7"/>'
    s += label(120, 165, "Плазма", DARK, 10, "middle", True)
    s += label(120, 178, "55%", DARK, 10, "middle")
    # Buffy coat
    s += f'<rect x="82" y="218" width="66" height="10" fill="{WHITE}" stroke="{GRAY}" stroke-width="0.5"/>'
    # RBC layer (bottom ~45%)
    s += f'<rect x="82" y="228" width="66" height="78" rx="3" fill="#EF4444" opacity="0.8"/>'
    s += label(120, 270, "Эритроциты", WHITE, 9, "middle", True)
    s += label(120, 283, "44%", WHITE, 9, "middle")

    # Detailed breakdown
    s += label(175, 115, "Плазма крови (55%):", ACCENT, 11, "start", True)
    s += label(175, 132, "• Вода — 90-92%", DARK, 9)
    s += label(175, 146, "• Белки: альбумины, глобулины,", DARK, 9)
    s += label(175, 159, "  фибриноген — 7%", DARK, 9)
    s += label(175, 173, "• Глюкоза, жиры, соли — 1-2%", DARK, 9)

    s += label(175, 195, "Форменные элементы (45%):", ACCENT, 11, "start", True)
    s += f'<circle cx="185" cy="218" r="7" fill="#EF4444" stroke="{BONE_DARK}" stroke-width="0.5"/>'
    s += label(198, 221, "Эритроциты (4-5·10¹²/л)", DARK, 9)
    s += f'<circle cx="185" cy="240" r="8" fill="#DBEAFE" stroke="{BLUE}" stroke-width="1"/>'
    s += f'<circle cx="185" cy="240" r="4" fill="{BLUE}" opacity="0.5"/>'
    s += label(198, 243, "Лейкоциты (4-9·10⁹/л)", DARK, 9)
    s += f'<circle cx="185" cy="260" r="4" fill="#E9D5FF" stroke="{PURPLE}" stroke-width="1"/>'
    s += label(198, 263, "Тромбоциты (200-400·10⁹/л)", DARK, 9)

    # Blood cells detail
    s += box(420, 72, 365, 260, fill=WHITE, stroke=PRIMARY)
    s += label(602, 92, "Форменные элементы крови", ACCENT, 13, "middle", True)

    # Erythrocyte
    s += f'<ellipse cx="462" cy="130" rx="22" ry="12" fill="#EF4444" stroke="{BONE_DARK}" stroke-width="1.5"/>'
    s += f'<ellipse cx="462" cy="130" rx="8" ry="5" fill="#FCA5A5" stroke="none"/>'
    s += label(492, 127, "Эритроцит", ACCENT, 11, "start", True)
    s += label(492, 141, "Двояковогнутый диск", DARK, 9)
    s += label(492, 154, "Без ядра, содержит гемоглобин", DARK, 9)
    s += label(492, 167, "Живёт ~120 дней", DARK, 9)
    s += label(492, 180, "Функция: транспорт O₂ и CO₂", DARK, 9)

    # Leukocyte
    s += f'<circle cx="462" cy="220" r="18" fill="#DBEAFE" stroke="{BLUE}" stroke-width="1.5"/>'
    s += f'<circle cx="462" cy="220" r="8" fill="{BLUE}" opacity="0.4"/>'
    s += label(492, 217, "Лейкоцит", ACCENT, 11, "start", True)
    s += label(492, 231, "Есть ядро, способен к движению", DARK, 9)
    s += label(492, 244, "Виды: нейтрофилы, лимфоциты,", DARK, 9)
    s += label(492, 257, "моноциты, эозинофилы, базофилы", DARK, 9)
    s += label(492, 270, "Функция: иммунитет, фагоцитоз", DARK, 9)

    # Thrombocyte
    s += f'<ellipse cx="462" cy="295" rx="10" ry="5" fill="#E9D5FF" stroke="{PURPLE}" stroke-width="1"/>'
    s += label(492, 298, "Тромбоцит", ACCENT, 11, "start", True)
    s += label(492, 311, "Функция: свёртывание крови", DARK, 9)

    # Bottom section - Hemoglobin formula and blood types
    s += box(20, 345, 385, 240, fill=WHITE, stroke=PRIMARY)
    s += label(212, 365, "Гемоглобин и свёртывание", ACCENT, 12, "middle", True)

    s += label(35, 388, "Гемоглобин (Hb):", ACCENT, 11, "start", True)
    s += label(35, 406, "Hb + O₂ → HbO₂ (оксигемоглобин)", DARK, 10)
    s += label(35, 424, "HbO₂ → Hb + O₂ (в тканях)", DARK, 10)
    s += f'<rect x="35" y="436" width="355" height="2" fill="{LIGHT_GRAY}"/>'
    s += label(35, 454, "Свёртывание крови:", ACCENT, 11, "start", True)
    s += label(35, 472, "1. Повреждение сосуда", DARK, 10)
    s += label(35, 488, "2. Тромбоциты → тромбопластин", DARK, 10)
    s += label(35, 504, "3. Протромбин → тромбин", DARK, 10)
    s += label(35, 520, "4. Фибриноген → фибрин (нити)", DARK, 10)
    s += label(35, 536, "5. Формирование тромба (сгустка)", DARK, 10)

    # Blood types
    s += box(420, 345, 365, 240, fill=WHITE, stroke=PRIMARY)
    s += label(602, 365, "Группы крови", ACCENT, 12, "middle", True)

    blood_types = [
        ("I (0)", "Нет агглютиногенов", "α и β агглютинины", "#BBF7D0"),
        ("II (A)", "Агглютиноген A", "β агглютинин", "#FDE68A"),
        ("III (B)", "Агглютиноген B", "α агглютинин", "#BFDBFE"),
        ("IV (AB)", "A и B агглютиногены", "Нет агглютининов", "#FECACA"),
    ]
    yy = 388
    for name, ag, acl, clr in blood_types:
        s += f'<rect x="435" y="{yy}" width="16" height="16" rx="3" fill="{clr}" stroke="{GRAY}" stroke-width="0.5"/>'
        s += label(458, yy+12, name, ACCENT, 11, "start", True)
        s += label(435, yy+27, f"Эритроциты: {ag}", DARK, 9)
        s += label(435, yy+40, f"Плазма: {acl}", DARK, 9)
        yy += 52

    s += label(435, 574, "Rh-фактор: D-антиген (+/-)", ACCENT, 10, "start", True)

    s += label(400, 590, "Урок 4", GRAY, 10, "middle")
    s += svg_footer()
    return s


# ============================================================
# LESSON 5: Строение сердца
# ============================================================
def lesson5():
    s = svg_header("Строение сердца")
    # Heart diagram
    s += box(20, 72, 370, 370, fill=WHITE, stroke=PRIMARY)
    s += label(205, 92, "Сердце человека", ACCENT, 13, "middle", True)

    # Heart shape - simplified
    # Right atrium
    s += f'<path d="M170,160 L170,220 Q130,220 130,180 Q130,140 160,140 Z" fill="#DBEAFE" stroke="{BLUE}" stroke-width="2"/>'
    # Left atrium
    s += f'<path d="M240,160 L240,220 Q280,220 280,180 Q280,140 250,140 Z" fill="#FECACA" stroke="{RED}" stroke-width="2"/>'
    # Right ventricle
    s += f'<path d="M140,230 L170,230 L170,340 Q130,340 120,300 Q110,260 130,240 Z" fill="#BFDBFE" stroke="{BLUE}" stroke-width="2"/>'
    # Left ventricle
    s += f'<path d="M240,230 L270,230 L280,300 Q290,340 250,340 L240,340 Z" fill="#FCA5A5" stroke="{RED}" stroke-width="2"/>'
    # Septum
    s += f'<line x1="205" y1="140" x2="205" y2="340" stroke="{DARK}" stroke-width="2" stroke-dasharray="4,2"/>'

    # Valves
    s += f'<ellipse cx="170" cy="228" rx="15" ry="5" fill="{YELLOW}" stroke="{BONE_DARK}" stroke-width="1.5"/>'
    s += f'<ellipse cx="240" cy="228" rx="15" ry="5" fill="{YELLOW}" stroke="{BONE_DARK}" stroke-width="1.5"/>'

    # Labels with pointers
    s += pointer(160, 170, 100, 155)
    s += label(55, 153, "Правое предсердие", BLUE, 10, "start", True)
    s += pointer(250, 170, 310, 155)
    s += label(310, 153, "Левое предсердие", RED, 10, "start", True)
    s += pointer(140, 290, 75, 290)
    s += label(28, 293, "Правый желудочек", BLUE, 10, "start", True)
    s += pointer(270, 290, 330, 290)
    s += label(330, 293, "Левый желудочек", RED, 10, "start", True)
    s += pointer(170, 228, 90, 228)
    s += label(28, 231, "Трёхстворчатый клапан", BONE_DARK, 9, "start", True)
    s += pointer(240, 228, 325, 228)
    s += label(325, 231, "Двухстворчатый (митр.)", BONE_DARK, 9, "start", True)
    s += label(205, 135, "Перегородка", DARK, 9, "middle")

    # Vessels
    s += f'<path d="M170,140 L155,110" stroke="{BLUE}" stroke-width="3"/>'
    s += label(130, 108, "Полая вена", BLUE, 9, "end", True)
    s += f'<path d="M240,140 L255,110" stroke="{RED}" stroke-width="3"/>'
    s += label(260, 108, "Лёгочные вены", RED, 9, "start", True)
    s += f'<path d="M140,240 L100,240 L100,350" stroke="{BLUE}" stroke-width="3"/>'
    s += label(55, 360, "Лёгочная артерия", BLUE, 9, "start", True)
    s += f'<path d="M270,240 L310,240 L310,350" stroke="{RED}" stroke-width="3"/>'
    s += label(315, 360, "Аорта", RED, 9, "start", True)

    # Info panels
    s += box(410, 72, 375, 175, fill=WHITE, stroke=PRIMARY)
    s += label(597, 92, "Особенности строения", ACCENT, 12, "middle", True)

    s += label(425, 115, "Стенка сердца — 3 слоя:", ACCENT, 10, "start", True)
    s += f'<rect x="425" y="125" width="12" height="12" rx="2" fill="#FECACA" stroke="{RED}" stroke-width="0.5"/>'
    s += label(442, 135, "Эндокард (внутренний)", DARK, 9)
    s += f'<rect x="425" y="143" width="12" height="12" rx="2" fill="#FCA5A5" stroke="{RED}" stroke-width="0.5"/>'
    s += label(442, 153, "Миокард (средний, мышечный)", DARK, 9)
    s += f'<rect x="425" y="161" width="12" height="12" rx="2" fill="#FDE68A" stroke="{YELLOW}" stroke-width="0.5"/>'
    s += label(442, 171, "Эпикард (наружный)", DARK, 9)

    s += label(425, 195, "Левый желудочек толще правого", DARK, 9)
    s += label(425, 210, "(т.к. толкает кровь по большому кругу)", GRAY, 9)
    s += label(425, 228, "Перикард — околосердечная сумка", DARK, 9)
    s += label(425, 243, "с жидкостью для уменьшения трения", GRAY, 9)

    # Cardiac cycle
    s += box(410, 260, 375, 182, fill=WHITE, stroke=PRIMARY)
    s += label(597, 280, "Сердечный цикл", ACCENT, 12, "middle", True)

    s += f'<rect x="425" y="295" width="350" height="28" rx="4" fill="{PRIMARY_LIGHT}"/>'
    s += f'<rect x="425" y="295" width="130" height="28" rx="4" fill="{PRIMARY}" opacity="0.4"/>'
    s += f'<rect x="555" y="295" width="140" height="28" rx="4" fill="{YELLOW}" opacity="0.4"/>'
    s += f'<rect x="695" y="295" width="80" height="28" rx="4" fill="{BLUE}" opacity="0.3"/>'
    s += label(490, 313, "Систола предс.", WHITE, 9, "middle", True)
    s += label(625, 313, "Систола желуд.", WHITE, 9, "middle", True)
    s += label(735, 313, "Диастола", WHITE, 9, "middle", True)

    s += label(425, 340, "0,1 с + 0,3 с + 0,4 с = 0,8 с", ACCENT, 11, "start", True)
    s += label(425, 358, "ЧСС в покое: 60-80 уд/мин", DARK, 10)
    s += label(425, 375, "Автоматия сердца — способность", ACCENT, 10, "start", True)
    s += label(425, 390, "сокращаться без внешних стимулов", DARK, 9)
    s += label(425, 408, "Водитель ритма — синусно-предсердный узел", DARK, 9)
    s += label(425, 423, "Проводящая система: СА-узел → АВ-узел → пучок Гиса → волокна Пуркинье", DARK, 8)

    # Bottom fact
    s += box(20, 455, 765, 130, fill=PRIMARY_LIGHTER, stroke=PRIMARY)
    s += label(400, 475, "Ключевые формулы", ACCENT, 12, "middle", True)
    s += label(40, 498, "Минутный объём крови (МОК) = ЧСС × УО", DARK, 10)
    s += label(40, 516, "Ударный объём (УО) ≈ 70 мл (в покое)", DARK, 10)
    s += label(40, 534, "МОК = 70 × 70 = 4900 мл/мин ≈ 5 л/мин", ACCENT, 10)
    s += label(450, 498, "За сутки сердце перекачивает ~7000 л крови", DARK, 10)
    s += label(450, 516, "Масса сердца: ~300 г (0,5% массы тела)", DARK, 10)
    s += label(450, 534, "Клапаны обеспечивают односторонний ток крови", DARK, 10)

    s += label(400, 590, "Урок 5", GRAY, 10, "middle")
    s += svg_footer()
    return s


# ============================================================
# LESSON 6: Кровообращение
# ============================================================
def lesson6():
    s = svg_header("Кровообращение")
    # Circulation diagram
    s += box(20, 72, 765, 300, fill=WHITE, stroke=PRIMARY)
    s += label(402, 92, "Круги кровообращения", ACCENT, 13, "middle", True)

    # Heart center
    s += f'<path d="M385,180 L385,230 Q360,230 360,210 Q360,170 378,165 Z" fill="#DBEAFE" stroke="{BLUE}" stroke-width="2"/>'
    s += f'<path d="M415,180 L415,230 Q440,230 440,210 Q440,170 422,165 Z" fill="#FECACA" stroke="{RED}" stroke-width="2"/>'
    s += f'<path d="M370,235 L385,235 L385,310 Q360,310 350,280 Q345,255 360,240 Z" fill="#BFDBFE" stroke="{BLUE}" stroke-width="2"/>'
    s += f'<path d="M415,235 L430,235 L440,280 Q445,310 420,310 L415,310 Z" fill="#FCA5A5" stroke="{RED}" stroke-width="2"/>'
    s += label(400, 225, "Сердце", DARK, 9, "middle", True)

    # Pulmonary circuit (small circle) - top
    # Right ventricle → pulmonary artery → lungs → pulmonary veins → left atrium
    s += f'<path d="M355,260 L200,260 L200,140" stroke="{BLUE}" stroke-width="3" fill="none" marker-end="none"/>'
    s += f'<polygon points="200,140 195,150 205,150" fill="{BLUE}"/>'
    # Lungs
    s += f'<ellipse cx="200" cy="120" rx="50" ry="30" fill="#D1FAE5" stroke="{PRIMARY}" stroke-width="1.5"/>'
    s += label(200, 122, "Лёгкие", PRIMARY_DARK, 10, "middle", True)
    # Lungs → left atrium
    s += f'<path d="M250,120 L425,165" stroke="{RED}" stroke-width="3" fill="none"/>'
    s += f'<polygon points="425,165 415,160 418,170" fill="{RED}"/>'

    s += label(250, 250, "Лёгочная артерия (венозная)", BLUE, 9, "middle")
    s += label(340, 135, "Лёгочные вены (артериальная)", RED, 9, "middle")

    # Small circle label
    s += f'<rect x="155" y="85" width="140" height="20" rx="10" fill="{PRIMARY}" opacity="0.2"/>'
    s += label(225, 99, "Малый круг", PRIMARY_DARK, 10, "middle", True)

    # Systemic circuit (big circle) - bottom
    # Left ventricle → aorta → body → vena cava → right atrium
    s += f'<path d="M445,290 L600,290 L600,340" stroke="{RED}" stroke-width="3" fill="none"/>'
    s += f'<polygon points="600,340 595,330 605,330" fill="{RED}"/>'
    # Body/organs
    s += f'<ellipse cx="600" cy="365" rx="60" ry="25" fill="#FDE68A" stroke="{BONE_DARK}" stroke-width="1.5"/>'
    s += label(600, 367, "Органы тела", BONE_DARK, 10, "middle", True)
    # Body → vena cava → right atrium
    s += f'<path d="M540,365 L200,365 L200,340 L370,230" stroke="{BLUE}" stroke-width="3" fill="none"/>'
    s += f'<polygon points="370,230 363,238 373,236" fill="{BLUE}"/>'

    s += label(530, 280, "Аорта (артериальная)", RED, 9, "middle")
    s += label(330, 355, "Полые вены (венозная)", BLUE, 9, "middle")

    # Big circle label
    s += f'<rect x="530" y="330" width="140" height="20" rx="10" fill="{YELLOW}" opacity="0.3"/>'
    s += label(600, 344, "Большой круг", BONE_DARK, 10, "middle", True)

    # Comparison table
    s += box(20, 385, 380, 200, fill=WHITE, stroke=PRIMARY)
    s += label(210, 405, "Сравнение кругов", ACCENT, 12, "middle", True)

    # Table header
    s += f'<rect x="30" y="415" width="360" height="22" rx="4" fill="{PRIMARY}" opacity="0.2"/>'
    s += label(60, 430, "Признак", ACCENT, 10, "middle", True)
    s += label(180, 430, "Малый круг", ACCENT, 10, "middle", True)
    s += label(320, 430, "Большой круг", ACCENT, 10, "middle", True)

    rows = [
        ("Начало", "Правый желудочек", "Левый желудочек"),
        ("Конец", "Левое предсердие", "Правое предсердие"),
        ("Артерии несут", "Венозную кровь", "Артериальную кровь"),
        ("Вены несут", "Артериальную кровь", "Венозную кровь"),
        ("Время", "~4-5 секунд", "~20-25 секунд"),
    ]
    yy = 445
    for feature, small, big in rows:
        s += f'<line x1="30" y1="{yy}" x2="390" y2="{yy}" stroke="{LIGHT_GRAY}" stroke-width="0.5"/>'
        s += label(35, yy+13, feature, DARK, 9, "start", True)
        s += label(120, yy+13, small, DARK, 8)
        s += label(250, yy+13, big, DARK, 8)
        yy += 20

    # Vessels info
    s += box(420, 385, 365, 200, fill=WHITE, stroke=PRIMARY)
    s += label(602, 405, "Типы кровеносных сосудов", ACCENT, 12, "middle", True)

    # Artery
    s += f'<rect x="435" y="420" width="340" height="24" rx="4" fill="#FECACA" opacity="0.5"/>'
    s += label(440, 436, "Артерии — толстые стенки, нет клапанов, высокое давление, несут кровь от сердца", DARK, 9)

    # Vein
    s += f'<rect x="435" y="450" width="340" height="24" rx="4" fill="#DBEAFE" opacity="0.5"/>'
    s += label(440, 466, "Вены — тонкие стенки, есть клапаны, низкое давление, несут кровь к сердцу", DARK, 9)

    # Capillary
    s += f'<rect x="435" y="480" width="340" height="24" rx="4" fill="#D1FAE5" opacity="0.5"/>'
    s += label(440, 496, "Капилляры — стенка 1 слой клеток, обмен O₂/CO₂ и веществ", DARK, 9)

    s += label(435, 530, "Давление: 120/80 мм рт. ст. (норма)", ACCENT, 10, "start", True)
    s += label(435, 548, "Пульс — колебание стенки артерии", DARK, 9)
    s += label(435, 566, "Скорость крови: аорта 0,5 м/с → капилляры 0,5 мм/с", DARK, 9)

    s += label(400, 590, "Урок 6", GRAY, 10, "middle")
    s += svg_footer()
    return s


# ============================================================
# LESSON 7: Строение дыхательной системы
# ============================================================
def lesson7():
    s = svg_header("Строение дыхательной системы")
    # Respiratory system diagram
    s += box(20, 72, 380, 410, fill=WHITE, stroke=PRIMARY)
    s += label(210, 92, "Органы дыхания", ACCENT, 13, "middle", True)

    # Nasal cavity
    s += f'<path d="M180,120 Q170,120 170,140 L170,170 L220,170 L220,140 Q220,120 210,120 Z" fill="#D1FAE5" stroke="{PRIMARY}" stroke-width="1.5"/>'
    s += label(195, 152, "Носовая полость", DARK, 8, "middle", True)

    # Pharynx
    s += f'<rect x="188" y="170" width="24" height="30" rx="4" fill="#FDE68A" stroke="{BONE_DARK}" stroke-width="1.5"/>'
    s += label(230, 188, "Глотка", DARK, 8)

    # Larynx
    s += f'<path d="M185,200 L215,200 L210,240 L190,240 Z" fill="#FECACA" stroke="{RED}" stroke-width="1.5"/>'
    s += label(230, 222, "Гортань", DARK, 8)
    # Vocal cords
    s += f'<line x1="193" y1="215" x2="207" y2="215" stroke="{RED}" stroke-width="1"/>'
    s += f'<line x1="193" y1="220" x2="207" y2="220" stroke="{RED}" stroke-width="1"/>'
    s += label(230, 240, "↖ Голосовые связки", GRAY, 7)

    # Trachea
    s += f'<rect x="190" y="240" width="20" height="80" rx="4" fill="#E0F2FE" stroke="{BLUE}" stroke-width="1.5"/>'
    # Tracheal rings
    for i in range(5):
        s += f'<line x1="190" y1="{250+i*14}" x2="210" y2="{250+i*14}" stroke="{BLUE}" stroke-width="1" opacity="0.5"/>'
    s += label(230, 280, "Трахея", DARK, 8)

    # Bronchi
    s += f'<path d="M195,320 L160,370" stroke="{BLUE}" stroke-width="3" fill="none"/>'
    s += f'<path d="M205,320 L240,370" stroke="{BLUE}" stroke-width="3" fill="none"/>'
    s += label(140, 355, "Левый бронх", DARK, 8, "end")
    s += label(255, 355, "Правый бронх", DARK, 8)

    # Lungs
    s += f'<ellipse cx="145" cy="390" rx="65" ry="70" fill="#D1FAE5" stroke="{PRIMARY}" stroke-width="2" opacity="0.7"/>'
    s += f'<ellipse cx="255" cy="390" rx="65" ry="70" fill="#D1FAE5" stroke="{PRIMARY}" stroke-width="2" opacity="0.7"/>'
    # Bronchial tree inside lungs
    s += f'<path d="M160,370 L130,400 L110,430" stroke="{PRIMARY_DARK}" stroke-width="1.5" fill="none"/>'
    s += f'<path d="M130,400 L150,435" stroke="{PRIMARY_DARK}" stroke-width="1" fill="none"/>'
    s += f'<path d="M240,370 L270,400 L290,430" stroke="{PRIMARY_DARK}" stroke-width="1.5" fill="none"/>'
    s += f'<path d="M270,400 L250,435" stroke="{PRIMARY_DARK}" stroke-width="1" fill="none"/>'

    s += label(145, 400, "Левое", DARK, 9, "middle", True)
    s += label(145, 413, "лёгкое", DARK, 9, "middle", True)
    s += label(255, 400, "Правое", DARK, 9, "middle", True)
    s += label(255, 413, "лёгкое", DARK, 9, "middle", True)

    # Diaphragm
    s += f'<path d="M80,460 Q200,480 320,460" fill="none" stroke="{BONE_DARK}" stroke-width="2.5" stroke-dasharray="6,3"/>'
    s += label(340, 462, "Диафрагма", BONE_DARK, 9)

    # Alveoli detail
    s += box(420, 72, 365, 200, fill=WHITE, stroke=PRIMARY)
    s += label(602, 92, "Альвеола — газообмен", ACCENT, 12, "middle", True)

    # Alveolus
    s += f'<circle cx="520" cy="185" r="40" fill="#D1FAE5" stroke="{PRIMARY}" stroke-width="2"/>'
    # Blood vessel around alveolus
    s += f'<path d="M480,175 Q470,185 480,195 Q490,205 510,210 Q530,215 550,210 Q570,205 575,195 Q580,185 570,175 Q560,165 540,162 Q520,158 500,162 Q485,165 480,175" fill="none" stroke="{RED}" stroke-width="2"/>'
    # Capillary
    s += f'<path d="M485,185 Q510,170 530,185 Q550,200 565,185" fill="none" stroke="{BLUE}" stroke-width="1.5"/>'

    s += pointer(520, 145, 520, 112)
    s += label(520, 108, "Воздух (O₂)", ACCENT, 9, "middle", True)

    s += label(580, 170, "→ CO₂", BLUE, 9)
    s += label(452, 170, "O₂ →", RED, 9)
    s += label(580, 200, "Кровь", BLUE, 8)
    s += label(452, 200, "Кровь", RED, 8)

    s += label(440, 235, "300 млн альвеол, площадь ~100 м²", DARK, 9)
    s += label(440, 252, "Стенка альвеолы — 1 слой клеток", DARK, 9)
    s += label(440, 267, "Сурфактант — не даёт спадаться", DARK, 9)

    # Breathing mechanics
    s += box(420, 285, 365, 200, fill=WHITE, stroke=PRIMARY)
    s += label(602, 305, "Механизм дыхания", ACCENT, 12, "middle", True)

    s += label(435, 328, "Вдох (инспирация):", ACCENT, 10, "start", True)
    s += label(435, 344, "• Диафрагма сокращается (опускается)", DARK, 9)
    s += label(435, 358, "• Мышцы грудной клетки сокращаются", DARK, 9)
    s += label(435, 372, "• Объём грудной полости ↑", DARK, 9)
    s += label(435, 386, "• Давление в лёгких ↓ → воздух входит", DARK, 9)

    s += label(435, 408, "Выдох (экспирация):", ACCENT, 10, "start", True)
    s += label(435, 424, "• Диафрагма расслабляется (поднимается)", DARK, 9)
    s += label(435, 438, "• Мышцы расслабляются", DARK, 9)
    s += label(435, 452, "• Объём грудной полости ↓", DARK, 9)
    s += label(435, 466, "• Давление в лёгких ↑ → воздух выходит", DARK, 9)

    # Vital capacity
    s += box(20, 495, 765, 90, fill=PRIMARY_LIGHTER, stroke=PRIMARY)
    s += label(400, 515, "Жизненная ёмкость лёгких (ЖЁЛ)", ACCENT, 12, "middle", True)
    s += label(40, 538, "ЖЁЛ = ДО + РОвд + РОвыд", DARK, 10)
    s += label(40, 555, "ДО (дыхательный объём) ≈ 500 мл", GRAY, 9)
    s += label(350, 538, "РОвд (резерв вдоха) ≈ 1500 мл", GRAY, 9)
    s += label(350, 555, "РОвыд (резерв выдоха) ≈ 1500 мл", GRAY, 9)
    s += label(650, 538, "ЖЁЛ ≈ 3500 мл", ACCENT, 10, "start", True)
    s += label(650, 555, "Остаточный объём ≈ 1200 мл", GRAY, 9)

    s += label(400, 590, "Урок 7", GRAY, 10, "middle")
    s += svg_footer()
    return s


# ============================================================
# LESSON 8: Газообмен и регуляция дыхания
# ============================================================
def lesson8():
    s = svg_header("Газообмен и регуляция дыхания")

    # Gas exchange diagram
    s += box(20, 72, 380, 260, fill=WHITE, stroke=PRIMARY)
    s += label(210, 92, "Газообмен в альвеолах", ACCENT, 12, "middle", True)

    # Alveolus
    s += f'<circle cx="210" cy="210" r="60" fill="#D1FAE5" stroke="{PRIMARY}" stroke-width="2"/>'
    s += label(210, 205, "Альвеола", PRIMARY_DARK, 10, "middle", True)
    s += label(210, 220, "(воздух)", PRIMARY_DARK, 9, "middle")

    # O2 arrow going in
    s += f'<path d="M130,180 L160,200" stroke="{RED}" stroke-width="3"/>'
    s += f'<polygon points="160,200 150,195 155,205" fill="{RED}"/>'
    s += label(95, 178, "O₂", RED, 14, "middle", True)

    # CO2 arrow going out
    s += f'<path d="M260,200 L290,180" stroke="{BLUE}" stroke-width="3"/>'
    s += f'<polygon points="290,180 280,178 285,188" fill="{BLUE}"/>'
    s += label(310, 178, "CO₂", BLUE, 14, "middle", True)

    # Blood vessel
    s += f'<ellipse cx="210" cy="210" rx="75" ry="75" fill="none" stroke="{RED}" stroke-width="2" stroke-dasharray="4,3"/>'
    s += label(100, 140, "Венозная кровь", BLUE, 9, "start", True)
    s += label(100, 153, "O₂: 40 мм рт.ст.", BLUE, 8)
    s += label(100, 165, "CO₂: 46 мм рт.ст.", BLUE, 8)
    s += label(270, 260, "Артериальная кровь", RED, 9, "start", True)
    s += label(270, 273, "O₂: 100 мм рт.ст.", RED, 8)
    s += label(270, 285, "CO₂: 40 мм рт.ст.", RED, 8)

    # Diffusion principle
    s += box(420, 72, 365, 120, fill=WHITE, stroke=PRIMARY)
    s += label(602, 92, "Диффузия газов", ACCENT, 12, "middle", True)
    s += label(435, 115, "Газ переходит из области", ACCENT, 10, "start", True)
    s += label(435, 130, "высокого давления в область низкого", DARK, 9)
    s += label(435, 150, "O₂: альвеола (100) → кровь (40)", DARK, 9)
    s += label(435, 165, "CO₂: кровь (46) → альвеола (40)", DARK, 9)
    s += label(435, 183, "Диффузия через тонкую стенку альвеолы + капилляра", GRAY, 8)

    # Gas transport in blood
    s += box(420, 205, 365, 127, fill=WHITE, stroke=PRIMARY)
    s += label(602, 225, "Транспорт газов кровью", ACCENT, 12, "middle", True)

    s += label(435, 248, "Кислород (O₂):", ACCENT, 10, "start", True)
    s += label(435, 263, "• 98% — связано с гемоглобином (HbO₂)", DARK, 9)
    s += label(435, 277, "• 2% — растворено в плазме", DARK, 9)
    s += label(435, 295, "Углекислый газ (CO₂):", ACCENT, 10, "start", True)
    s += label(435, 310, "• 70% — в виде HCO₃⁻ (бикарбонат)", DARK, 9)
    s += label(435, 324, "• 23% — связано с Hb (карбгемоглобин)", DARK, 9)

    # Tissue gas exchange
    s += box(20, 345, 380, 110, fill=WHITE, stroke=PRIMARY)
    s += label(210, 365, "Газообмен в тканях", ACCENT, 11, "middle", True)

    # Tissue cell
    s += f'<rect x="150" y="385" width="60" height="40" rx="8" fill="#FDE68A" stroke="{BONE_DARK}" stroke-width="1.5"/>'
    s += label(180, 408, "Клетка", DARK, 9, "middle", True)

    s += f'<path d="M110,395 L150,395" stroke="{RED}" stroke-width="2.5"/>'
    s += f'<polygon points="150,395 142,390 142,400" fill="{RED}"/>'
    s += label(85, 393, "O₂", RED, 10, "end", True)

    s += f'<path d="M210,405 L260,405" stroke="{BLUE}" stroke-width="2.5"/>'
    s += f'<polygon points="260,405 252,400 252,410" fill="{BLUE}"/>'
    s += label(265, 403, "CO₂", BLUE, 10, "start", True)

    s += label(55, 425, "Кровь отдаёт O₂, забирает CO₂", DARK, 9)
    s += label(55, 440, "Артериальная → Венозная", GRAY, 9)

    # Regulation
    s += box(420, 345, 365, 110, fill=WHITE, stroke=PRIMARY)
    s += label(602, 365, "Регуляция дыхания", ACCENT, 11, "middle", True)

    s += label(435, 388, "Нервная регуляция:", ACCENT, 10, "start", True)
    s += label(435, 403, "• Дыхательный центр — продолговатый мозг", DARK, 9)
    s += label(435, 417, "• Рефлекторная дуга: рецепторы → ЦНС → мышцы", DARK, 9)
    s += label(435, 435, "Гуморальная регуляция:", ACCENT, 10, "start", True)
    s += label(435, 450, "• CO₂ ↑ → дыхание учащается", DARK, 9)

    # Bottom facts
    s += box(20, 468, 765, 118, fill=PRIMARY_LIGHTER, stroke=PRIMARY)
    s += label(400, 488, "Важные факты о дыхании", ACCENT, 12, "middle", True)
    s += label(40, 510, "• Частота дыхания: 16-20 в минуту в покое", DARK, 10)
    s += label(40, 526, "• За 1 вдох ~500 мл воздуха (дыхательный объём)", DARK, 10)
    s += label(40, 542, "• Вдыхаемый воздух: O₂=21%, CO₂=0,03%", DARK, 10)
    s += label(40, 558, "• Выдыхаемый воздух: O₂=16%, CO₂=4%", DARK, 10)
    s += label(450, 510, "• Гипервентиляция — избыток O₂, дефицит CO₂", DARK, 10)
    s += label(450, 526, "• Удушье — недостаток O₂, избыток CO₂", DARK, 10)
    s += label(450, 542, "• Искусственное дыхание — спасение при остановке", DARK, 10)
    s += label(450, 558, "• Дыхательная гимнастика укрепляет лёгкие", DARK, 10)

    s += label(400, 590, "Урок 8", GRAY, 10, "middle")
    s += svg_footer()
    return s


# ============================================================
# LESSON 9: Пищеварение в ротовой полости и желудке
# ============================================================
def lesson9():
    s = svg_header("Пищеварение в ротовой полости и желудке")

    # Mouth digestion
    s += box(20, 72, 385, 240, fill=WHITE, stroke=PRIMARY)
    s += label(212, 92, "Ротовая полость", ACCENT, 12, "middle", True)

    # Simplified mouth cross-section
    s += f'<path d="M120,130 Q210,110 300,130 L290,200 Q210,210 130,200 Z" fill="#FECDD3" stroke="{RED}" stroke-width="1.5"/>'
    # Teeth
    s += f'<path d="M130,130 L135,155 L170,155 L175,130" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="1"/>'
    s += f'<path d="M245,130 L250,155 L285,155 L290,130" fill="{BONE}" stroke="{BONE_DARK}" stroke-width="1"/>'
    # Tongue
    s += f'<ellipse cx="210" cy="175" rx="50" ry="15" fill="#F87171" stroke="{RED}" stroke-width="1"/>'
    # Salivary glands
    s += f'<ellipse cx="140" cy="115" rx="20" ry="10" fill="#FDE68A" stroke="{BONE_DARK}" stroke-width="1"/>'
    s += f'<ellipse cx="280" cy="115" rx="20" ry="10" fill="#FDE68A" stroke="{BONE_DARK}" stroke-width="1"/>'
    s += f'<path d="M280,125 L260,140" stroke="{BONE_DARK}" stroke-width="1" stroke-dasharray="3,2"/>'
    s += f'<path d="M140,125 L160,140" stroke="{BONE_DARK}" stroke-width="1" stroke-dasharray="3,2"/>'

    s += pointer(140, 115, 85, 110)
    s += label(40, 113, "Слюнные железы", BONE_DARK, 9, "start", True)
    s += pointer(210, 175, 85, 175)
    s += label(40, 178, "Язык (вкусовые рецепторы)", BONE_DARK, 9, "start", True)
    s += pointer(155, 145, 85, 145)
    s += label(40, 148, "Зубы (механическая обработка)", BONE_DARK, 9, "start", True)

    s += label(40, 215, "Слюна: муцин + амилаза + лизоцим", DARK, 9)
    s += label(40, 230, "Механическая + химическая обработка", DARK, 9)
    s += label(40, 247, "Формирование пищевого комка → глотание", DARK, 9)

    # Stomach digestion
    s += box(420, 72, 365, 240, fill=WHITE, stroke=PRIMARY)
    s += label(602, 92, "Желудок", ACCENT, 12, "middle", True)

    # Stomach shape
    s += f'<path d="M540,130 Q500,130 500,180 L500,260 Q500,290 540,290 L640,290 Q680,290 680,260 L680,160 Q680,130 640,130 Z" fill="#FECACA" stroke="{RED}" stroke-width="2"/>'
    # Inner lining
    s += f'<path d="M510,145 Q510,270 530,280 L650,280 Q670,270 670,145" fill="none" stroke="#E5A0A0" stroke-width="1" stroke-dasharray="3,2"/>'
    # Sphincters
    s += f'<rect x="555" y="122" width="40" height="10" rx="3" fill="{YELLOW}" stroke="{BONE_DARK}" stroke-width="1"/>'
    s += f'<rect x="545" y="288" width="50" height="10" rx="3" fill="{YELLOW}" stroke="{BONE_DARK}" stroke-width="1"/>'

    s += label(575, 115, "Кардиальный сфинктер", BONE_DARK, 8, "middle")
    s += label(570, 310, "Пилорический сфинктер", BONE_DARK, 8, "middle")

    # Gastric glands
    s += f'<rect x="515" y="170" width="30" height="60" rx="5" fill="#FDE68A" stroke="{BONE_DARK}" stroke-width="1"/>'
    s += label(552, 200, "Железы желудка", BONE_DARK, 8)

    # Bottom section - enzymes
    s += box(20, 325, 385, 260, fill=WHITE, stroke=PRIMARY)
    s += label(212, 345, "Ферменты ротовой полости", ACCENT, 11, "middle", True)

    s += label(35, 370, "Амилаза (птиалин):", ACCENT, 10, "start", True)
    s += label(35, 386, "Крахмал → Мальтоза (дисахарид)", DARK, 9)
    s += label(35, 400, "Условие: t=37°C, pH ≈ 6,8 (слабокислая)", GRAY, 8)

    s += f'<rect x="35" y="410" width="355" height="2" fill="{LIGHT_GRAY}"/>'

    s += label(35, 425, "Мальтаза:", ACCENT, 10, "start", True)
    s += label(35, 441, "Мальтоза → Глюкоза", DARK, 9)

    s += f'<rect x="35" y="451" width="355" height="2" fill="{LIGHT_GRAY}"/>'

    s += label(35, 466, "Лизоцим:", ACCENT, 10, "start", True)
    s += label(35, 482, "Антибактериальное действие", DARK, 9)
    s += label(35, 496, "Разрушает клеточную стенку бактерий", GRAY, 8)

    s += f'<rect x="35" y="506" width="355" height="2" fill="{LIGHT_GRAY}"/>'

    s += label(35, 520, "Зубы: резцы, клыки, малые/большие коренные", DARK, 9)
    s += label(35, 536, "Молочные: 20 зубов, Постоянные: 32 зуба", DARK, 9)
    s += label(35, 555, "Формула зуба: I-C-P-M", GRAY, 9)

    # Stomach enzymes
    s += box(420, 325, 365, 260, fill=WHITE, stroke=PRIMARY)
    s += label(602, 345, "Ферменты желудка", ACCENT, 11, "middle", True)

    s += label(435, 370, "Состав желудочного сока:", ACCENT, 10, "start", True)
    s += label(435, 386, "• Пепсин — расщепляет белки", DARK, 9)
    s += label(435, 400, "  Белки → Пептоны + Альбумозы", GRAY, 8)
    s += label(435, 416, "• Соляная кислота (HCl):", DARK, 9)
    s += label(435, 430, "  — активирует пепсиноген → пепсин", GRAY, 8)
    s += label(435, 444, "  — создаёт pH ≈ 1,5-2,0", GRAY, 8)
    s += label(435, 458, "  — обеззараживает пищу", GRAY, 8)
    s += label(435, 474, "• Липаза — расщепляет жиры молока", DARK, 9)
    s += label(435, 488, "  (в желудке жиры почти не перевариваются)", GRAY, 8)
    s += label(435, 504, "• Слизь — защита стенки желудка", DARK, 9)

    s += f'<rect x="435" y="516" width="335" height="2" fill="{LIGHT_GRAY}"/>'
    s += label(435, 530, "Время нахождения пищи: 4-8 часов", ACCENT, 9)
    s += label(435, 546, "Объём желудка: 1,5-2 литра", DARK, 9)
    s += label(435, 562, "Перистальтика — волнообразные сокращения", DARK, 9)

    s += label(400, 590, "Урок 9", GRAY, 10, "middle")
    s += svg_footer()
    return s


# ============================================================
# LESSON 10: Пищеварение в кишечнике
# ============================================================
def lesson10():
    s = svg_header("Пищеварение в кишечнике")

    # Digestive tract diagram
    s += box(20, 72, 380, 310, fill=WHITE, stroke=PRIMARY)
    s += label(210, 92, "Пищеварительный тракт", ACCENT, 12, "middle", True)

    # Stomach
    s += f'<path d="M140,115 Q120,115 120,145 L120,175 Q120,195 140,195 L175,195 Q195,195 195,175 L195,125 Q195,115 175,115 Z" fill="#FECACA" stroke="{RED}" stroke-width="1.5"/>'
    s += label(157, 158, "Желудок", DARK, 8, "middle", True)

    # Duodenum
    s += f'<path d="M195,180 Q230,180 240,200 Q250,220 240,240 Q230,260 210,260 Q190,260 185,250" fill="none" stroke="{ORANGE}" stroke-width="4"/>'
    s += label(260, 220, "12-перстная", ORANGE, 8)
    s += label(260, 233, "кишка", ORANGE, 8)

    # Liver
    s += f'<path d="M60,200 Q50,200 50,220 L50,280 Q50,310 80,310 L130,310 Q160,310 160,280 L160,220 Q160,200 140,200 Z" fill="#8B5CF6" opacity="0.3" stroke="{PURPLE}" stroke-width="1.5"/>'
    s += label(105, 260, "Печень", PURPLE, 9, "middle", True)

    # Gallbladder
    s += f'<ellipse cx="155" cy="305" rx="10" ry="14" fill="#4ADE80" stroke="{PRIMARY}" stroke-width="1"/>'
    s += label(170, 308, "Жёлчный пузырь", PRIMARY_DARK, 7)

    # Pancreas
    s += f'<ellipse cx="185" cy="280" rx="35" ry="10" fill="#FDE68A" stroke="{BONE_DARK}" stroke-width="1.5" transform="rotate(-30 185 280)"/>'
    s += label(225, 285, "Поджелудочная", BONE_DARK, 8)

    # Small intestine (coiled)
    for i in range(8):
        x_start = 90 + (i % 2) * 30
        y_pos = 330 + i * 6
        s += f'<path d="M{x_start},{y_pos} Q{x_start+15},{y_pos-5} {x_start+30},{y_pos}" fill="none" stroke="{PRIMARY}" stroke-width="2"/>'

    s += label(210, 360, "Тонкий кишечник", PRIMARY_DARK, 9)
    s += label(210, 375, "(3-5 м)", GRAY, 8)

    # Large intestine
    s += f'<path d="M80,320 L60,320 L55,340 L55,370 L60,385 L330,385 L335,370 L335,340 L330,320" fill="none" stroke="#8B5CF6" stroke-width="3"/>'
    s += label(195, 378, "Толстый кишечник (1,5-2 м)", PURPLE, 8, "middle")

    # Enzyme details
    s += box(420, 72, 365, 175, fill=WHITE, stroke=PRIMARY)
    s += label(602, 92, "Ферменты тонкого кишечника", ACCENT, 11, "middle", True)

    enzymes = [
        ("Амилаза", "Крахмал → Мальтоза", PRIMARY),
        ("Мальтаза", "Мальтоза → Глюкоза", PRIMARY),
        ("Липаза", "Жиры → Глицерин + Жирные к-ты", ORANGE),
        ("Трипсин", "Белки → Аминокислоты", RED),
        ("Пептидаза", "Пептиды → Аминокислоты", RED),
    ]
    yy = 115
    for name, reaction, clr in enzymes:
        s += f'<rect x="435" y="{yy-2}" width="8" height="14" rx="2" fill="{clr}" opacity="0.5"/>'
        s += label(450, yy+9, f"{name}: {reaction}", DARK, 9)
        yy += 22

    s += label(435, yy+8, "Панкреатический сок + жёлчь + кишечный сок", ACCENT, 8)

    # Liver and pancreas
    s += box(420, 260, 365, 122, fill=WHITE, stroke=PRIMARY)
    s += label(602, 280, "Печень и поджелудочная", ACCENT, 11, "middle", True)

    s += label(435, 300, "Печень — крупнейшая железа (1,5 кг):", PURPLE, 10, "start", True)
    s += label(435, 315, "• Жёлчь — эмульгация жиров", DARK, 9)
    s += label(435, 329, "• Обезвреживание токсинов", DARK, 9)
    s += label(435, 343, "• Хранение гликогена, витаминов", DARK, 9)
    s += label(435, 360, "Поджелудочная железа:", BONE_DARK, 10, "start", True)
    s += label(435, 374, "• Панкреатический сок (ферменты + бикарбонат)", DARK, 9)

    # Absorption
    s += box(20, 395, 380, 190, fill=WHITE, stroke=PRIMARY)
    s += label(210, 415, "Всасывание в кишечнике", ACCENT, 11, "middle", True)

    # Villi diagram
    s += f'<path d="M80,450 L90,430 L100,450" fill="#D1FAE5" stroke="{PRIMARY}" stroke-width="1.5"/>'
    s += f'<path d="M110,450 L120,420 L130,450" fill="#D1FAE5" stroke="{PRIMARY}" stroke-width="1.5"/>'
    s += f'<path d="M140,450 L150,425 L160,450" fill="#D1FAE5" stroke="{PRIMARY}" stroke-width="1.5"/>'
    s += f'<path d="M170,450 L180,430 L190,450" fill="#D1FAE5" stroke="{PRIMARY}" stroke-width="1.5"/>'
    # Base
    s += f'<rect x="70" y="450" width="130" height="15" rx="3" fill="#FDE68A" stroke="{BONE_DARK}" stroke-width="1"/>'
    s += label(135, 462, "Стенка кишечника", DARK, 7, "middle")

    s += pointer(120, 420, 215, 420)
    s += label(220, 418, "Ворсинка", ACCENT, 9, "start", True)
    s += label(220, 432, "(увеличивает площадь)", GRAY, 8)

    s += label(35, 480, "Всасываются:", ACCENT, 10, "start", True)
    s += label(35, 496, "• Аминокислоты, глюкоза → в кровь", DARK, 9)
    s += label(35, 510, "• Глицерин + жирные к-ты → в лимфу", DARK, 9)
    s += label(35, 524, "• Витамины, минеральные вещества", DARK, 9)
    s += label(35, 540, "Площадь всасывания: ~200 м²", ACCENT, 9)
    s += label(35, 556, "Ворсинок: ~4-5 млн в тонком кишечнике", GRAY, 8)

    # Large intestine
    s += box(420, 395, 365, 190, fill=WHITE, stroke=PRIMARY)
    s += label(602, 415, "Толстый кишечник", ACCENT, 11, "middle", True)

    s += label(435, 440, "Функции:", ACCENT, 10, "start", True)
    s += label(435, 456, "• Всасывание воды и минеральных солей", DARK, 9)
    s += label(435, 470, "• Формирование каловых масс", DARK, 9)
    s += label(435, 484, "• Микрофлора (E. coli и др.):", DARK, 9)
    s += label(435, 498, "  — синтез витаминов K, B", GRAY, 8)
    s += label(435, 512, "  — подавление гнилостных бактерий", GRAY, 8)

    s += f'<rect x="435" y="524" width="335" height="2" fill="{LIGHT_GRAY}"/>'
    s += label(435, 540, "Аппендикс — червеобразный отросток", DARK, 9)
    s += label(435, 554, "Аппендицит — воспаление аппендикса", RED, 9)
    s += label(435, 570, "Дисбактериоз — нарушение микрофлоры", ORANGE, 9)

    s += label(400, 590, "Урок 10", GRAY, 10, "middle")
    s += svg_footer()
    return s


# ============================================================
# LESSON 11: Строение нервной системы
# ============================================================
def lesson11():
    s = svg_header("Строение нервной системы")

    # Nervous system overview
    s += box(20, 72, 360, 310, fill=WHITE, stroke=PRIMARY)
    s += label(200, 92, "Нервная система", ACCENT, 12, "middle", True)

    # Central NS - brain and spinal cord
    # Brain
    s += f'<ellipse cx="180" cy="135" rx="40" ry="30" fill="#D1FAE5" stroke="{PRIMARY}" stroke-width="2"/>'
    s += label(180, 138, "Головной мозг", DARK, 8, "middle", True)
    # Spinal cord
    s += f'<rect x="175" y="165" width="10" height="180" rx="3" fill="#D1FAE5" stroke="{PRIMARY}" stroke-width="1.5"/>'
    # Spinal nerves
    for i in range(8):
        yy = 185 + i*20
        s += f'<line x1="175" y1="{yy}" x2="140" y2="{yy+10}" stroke="{PRIMARY}" stroke-width="1.5"/>'
        s += f'<line x1="185" y1="{yy}" x2="220" y2="{yy+10}" stroke="{PRIMARY}" stroke-width="1.5"/>'

    s += label(100, 200, "Спинномозговые нервы", GRAY, 7)
    s += label(180, 265, "Спинной мозг", DARK, 8, "middle", True)

    # Labels
    s += pointer(220, 135, 260, 120)
    s += label(265, 118, "ЦНС", ACCENT, 11, "start", True)
    s += f'<rect x="260" y="125" width="100" height="30" rx="4" fill="{PRIMARY_LIGHT}"/>'
    s += label(310, 138, "Центральная НС", DARK, 8, "middle", True)
    s += label(310, 150, "(мозг + спинной мозг)", GRAY, 7)

    s += f'<rect x="260" y="168" width="100" height="30" rx="4" fill="#DBEAFE"/>'
    s += label(310, 181, "Периферическая НС", BLUE, 8, "middle", True)
    s += label(310, 193, "(нервы + ганглии)", GRAY, 7)

    # PNS subdivisions
    s += f'<rect x="260" y="210" width="100" height="24" rx="4" fill="#FDE68A"/>'
    s += label(310, 226, "Соматическая", BONE_DARK, 8, "middle", True)
    s += f'<rect x="260" y="240" width="100" height="24" rx="4" fill="#FECACA"/>'
    s += label(310, 256, "Вегетативная", RED, 8, "middle", True)
    s += f'<rect x="265" y="270" width="44" height="20" rx="3" fill="#BBF7D0"/>'
    s += label(287, 283, "Симпат.", DARK, 7, "middle")
    s += f'<rect x="315" y="270" width="44" height="20" rx="3" fill="#FECDD3"/>'
    s += label(337, 283, "Парасим.", DARK, 7, "middle")

    # Neuron structure
    s += box(400, 72, 385, 200, fill=WHITE, stroke=PRIMARY)
    s += label(592, 92, "Строение нейрона", ACCENT, 12, "middle", True)

    # Cell body
    s += f'<circle cx="500" cy="170" r="25" fill="#D1FAE5" stroke="{PRIMARY}" stroke-width="2"/>'
    s += f'<circle cx="500" cy="170" r="10" fill="{PRIMARY}" opacity="0.4"/>'
    s += label(500, 173, "Ядро", DARK, 7, "middle")

    # Dendrites
    s += f'<line x1="480" y1="155" x2="445" y2="135" stroke="{PRIMARY}" stroke-width="2"/>'
    s += f'<line x1="445" y1="135" x2="430" y2="125" stroke="{PRIMARY}" stroke-width="1.5"/>'
    s += f'<line x1="445" y1="135" x2="435" y2="140" stroke="{PRIMARY}" stroke-width="1.5"/>'
    s += f'<line x1="480" y1="165" x2="440" y2="160" stroke="{PRIMARY}" stroke-width="2"/>'
    s += f'<line x1="440" y1="160" x2="425" y2="155" stroke="{PRIMARY}" stroke-width="1.5"/>'
    s += f'<line x1="440" y1="160" x2="425" y2="168" stroke="{PRIMARY}" stroke-width="1.5"/>'
    label_x = 420
    s += label(label_x, 120, "Дендриты", PRIMARY_DARK, 9, "start", True)

    # Axon
    s += f'<line x1="525" y1="170" x2="700" y2="170" stroke="{BONE_DARK}" stroke-width="2.5"/>'
    # Myelin sheath
    for i in range(5):
        xx = 550 + i*28
        s += f'<rect x="{xx}" y="160" width="20" height="20" rx="5" fill="#FDE68A" stroke="{BONE_DARK}" stroke-width="0.8"/>'
    s += label(620, 155, "Миелиновая оболочка", BONE_DARK, 8, "middle")

    # Axon terminals
    s += f'<line x1="700" y1="170" x2="720" y2="155" stroke="{BONE_DARK}" stroke-width="1.5"/>'
    s += f'<line x1="700" y1="170" x2="720" y2="170" stroke="{BONE_DARK}" stroke-width="1.5"/>'
    s += f'<line x1="700" y1="170" x2="720" y2="185" stroke="{BONE_DARK}" stroke-width="1.5"/>'
    s += label(725, 170, "Терминали", BONE_DARK, 8)

    s += label(620, 185, "Аксон", DARK, 9, "middle", True)

    # Synapse
    s += box(400, 285, 385, 97, fill=WHITE, stroke=PRIMARY)
    s += label(592, 305, "Синапс", ACCENT, 11, "middle", True)

    # Presynaptic
    s += f'<ellipse cx="470" cy="340" rx="30" ry="20" fill="#D1FAE5" stroke="{PRIMARY}" stroke-width="1.5"/>'
    # Vesicles
    s += f'<circle cx="460" cy="335" r="4" fill="#10B981" opacity="0.5"/>'
    s += f'<circle cx="475" cy="338" r="4" fill="#10B981" opacity="0.5"/>'
    s += f'<circle cx="467" cy="345" r="4" fill="#10B981" opacity="0.5"/>'

    # Synaptic cleft
    s += f'<rect x="500" y="325" width="30" height="30" fill="#FEF3C7" opacity="0.5"/>'
    s += label(515, 345, "Щель", GRAY, 7, "middle")

    # Postsynaptic
    s += f'<path d="M540,330 Q555,340 540,350 L570,350 Q585,340 570,330 Z" fill="#FECACA" stroke="{RED}" stroke-width="1.5"/>'
    # Receptors
    s += f'<circle cx="547" cy="335" r="3" fill="{RED}" opacity="0.5"/>'
    s += f'<circle cx="557" cy="338" r="3" fill="{RED}" opacity="0.5"/>'

    s += label(440, 318, "Пресинаптич.", PRIMARY_DARK, 7, "middle")
    s += label(560, 318, "Постсинаптич.", RED, 7, "middle")

    s += label(620, 330, "Нейромедиаторы:", ACCENT, 9, "start", True)
    s += label(620, 345, "АХ, дофамин, серотонин", DARK, 8)
    s += label(620, 360, "Передача: электрич. → химич. → электрич.", GRAY, 7)

    # Types of neurons
    s += box(20, 395, 250, 190, fill=WHITE, stroke=PRIMARY)
    s += label(145, 415, "Типы нейронов", ACCENT, 11, "middle", True)

    # Sensory
    s += f'<circle cx="60" cy="450" r="10" fill="#BFDBFE" stroke="{BLUE}" stroke-width="1.5"/>'
    s += f'<line x1="70" y1="450" x2="95" y2="450" stroke="{BLUE}" stroke-width="1.5"/>'
    s += f'<circle cx="95" cy="450" r="6" fill="{BLUE}" opacity="0.3"/>'
    s += label(105, 453, "Чувствительный", BLUE, 9)
    s += label(105, 465, "(афферентный)", GRAY, 7)

    # Motor
    s += f'<circle cx="60" cy="490" r="10" fill="#FECACA" stroke="{RED}" stroke-width="1.5"/>'
    s += f'<line x1="70" y1="490" x2="95" y2="490" stroke="{RED}" stroke-width="1.5"/>'
    s += label(105, 493, "Двигательный", RED, 9)
    s += label(105, 505, "(эфферентный)", GRAY, 7)

    # Interneuron
    s += f'<circle cx="60" cy="530" r="10" fill="#D1FAE5" stroke="{PRIMARY}" stroke-width="1.5"/>'
    s += f'<line x1="70" y1="530" x2="95" y2="530" stroke="{PRIMARY}" stroke-width="1.5"/>'
    s += label(105, 533, "Вставочный", PRIMARY, 9)
    s += label(105, 545, "(промежуточный)", GRAY, 7)

    # Reflex arc
    s += box(285, 395, 500, 190, fill=WHITE, stroke=PRIMARY)
    s += label(535, 415, "Рефлекторная дуга", ACCENT, 11, "middle", True)

    steps = [
        ("1", "Рецептор", "Воспринимает раздражение", "#BFDBFE"),
        ("2", "Чувств. нейрон", "Передаёт импульс в ЦНС", "#BFDBFE"),
        ("3", "Вставочный нейрон", "Обработка в ЦНС", "#D1FAE5"),
        ("4", "Двигат. нейрон", "Передаёт импульс к органу", "#FECACA"),
        ("5", "Рабочий орган", "Осуществляет реакцию", "#FDE68A"),
    ]
    xx = 310
    for num, name, desc, clr in steps:
        s += f'<circle cx="{xx+15}" cy="450" r="14" fill="{clr}" stroke="{GRAY}" stroke-width="1"/>'
        s += label(xx+15, 454, num, DARK, 10, "middle", True)
        s += label(xx+15, 475, name, DARK, 8, "middle", True)
        s += label(xx+15, 487, desc, GRAY, 7, "middle")
        if num != "5":
            s += f'<path d="M{xx+30},450 L{xx+45},450" stroke="{GRAY}" stroke-width="1.5"/>'
            s += f'<polygon points="{xx+45},450 {xx+40},445 {xx+40},455" fill="{GRAY}"/>'
        xx += 90

    s += label(310, 520, "Рефлекс — ответная реакция организма на раздражение", ACCENT, 9, "start", True)
    s += label(310, 536, "Безусловные (врождённые) и Условные (приобретённые)", DARK, 9)
    s += label(310, 554, "Рефлекторная дуга — путь нервного импульса", GRAY, 8)

    s += label(400, 590, "Урок 11", GRAY, 10, "middle")
    s += svg_footer()
    return s


# ============================================================
# LESSON 12: Головной мозг
# ============================================================
def lesson12():
    s = svg_header("Головной мозг")

    # Brain diagram
    s += box(20, 72, 420, 320, fill=WHITE, stroke=PRIMARY)
    s += label(230, 92, "Головной мозг человека", ACCENT, 12, "middle", True)

    # Brain outline
    s += f'<path d="M160,180 Q120,180 110,200 Q100,220 110,250 Q120,280 150,300 Q170,310 200,310 Q230,310 260,300 Q300,280 310,250 Q320,220 310,200 Q300,180 270,175 Q250,170 230,170 Q210,165 190,170 Q175,172 160,180 Z" fill="#D1FAE5" stroke="{PRIMARY}" stroke-width="2"/>'

    # Cerebrum - divided
    s += f'<line x1="210" y1="170" x2="210" y2="300" stroke="{PRIMARY_DARK}" stroke-width="1.5" stroke-dasharray="4,2"/>'
    # Frontal lobe
    s += f'<path d="M160,180 Q140,180 130,195 Q125,210 135,235" fill="none" stroke="{BLUE}" stroke-width="1.5"/>'
    s += label(145, 210, "Лобная", BLUE, 8, "middle", True)
    # Parietal lobe
    s += f'<path d="M135,235 Q130,260 150,280" fill="none" stroke="{PURPLE}" stroke-width="1.5"/>'
    s += label(135, 260, "Теменная", PURPLE, 8, "middle", True)
    # Temporal lobe
    s += f'<path d="M135,235 Q155,240 165,225" fill="none" stroke="{ORANGE}" stroke-width="1.5"/>'
    s += label(115, 240, "Височная", ORANGE, 7, "end", True)
    # Occipital lobe
    s += f'<path d="M150,280 Q175,295 210,300 Q245,295 270,280" fill="none" stroke="{RED}" stroke-width="1.5"/>'
    s += label(210, 295, "Затылочная", RED, 7, "middle", True)

    # Cerebellum
    s += f'<ellipse cx="280" cy="290" rx="30" ry="18" fill="#FDE68A" stroke="{BONE_DARK}" stroke-width="1.5"/>'
    s += label(280, 293, "Мозжечок", DARK, 7, "middle", True)

    # Brainstem
    s += f'<rect x="195" y="300" width="25" height="30" rx="4" fill="#FECACA" stroke="{RED}" stroke-width="1.5"/>'
    s += label(240, 315, "Ствол мозга", RED, 7)

    # Cerebrum label
    s += pointer(210, 200, 100, 140)
    s += label(55, 138, "Большие полушария", ACCENT, 9, "start", True)
    s += label(55, 152, "(кора ~2-4 мм, извилины)", GRAY, 8)

    # Brain mass
    s += label(230, 365, "Масса: ~1400 г (2% массы тела)", ACCENT, 9, "middle", True)
    s += label(230, 380, "Потребляет 20% O₂ и глюкозы", GRAY, 8)

    # Brain parts functions
    s += box(460, 72, 325, 320, fill=WHITE, stroke=PRIMARY)
    s += label(622, 92, "Функции отделов мозга", ACCENT, 11, "middle", True)

    parts = [
        ("Большие полушария", "Мышление, речь, память,\nпроизвольные движения,\nорганы чувств", "#D1FAE5", PRIMARY),
        ("Мозжечок", "Координация движений,\nравновесие, мышечный тонус", "#FDE68A", BONE_DARK),
        ("Ствол мозга:", "", "#FECACA", RED),
        ("  Промежуточный мозг", "Таламус (ретранслятор),\nгипоталамус (гомеостаз)", "#FECACA", RED),
        ("  Средний мозг", "Рефлексы на свет/звук,\nмышечный тонус", "#FECACA", RED),
        ("  Мост", "Связь полушарий мозжечка", "#FECACA", RED),
        ("  Продолговатый мозг", "Дыхание, сердцебиение,\nглотание, чихание, рвота", "#FECACA", RED),
    ]
    yy = 110
    for name, func, bg, clr in parts:
        s += f'<rect x="475" y="{yy-3}" width="10" height="14" rx="2" fill="{bg}" stroke="{clr}" stroke-width="0.5"/>'
        s += label(490, yy+7, name, clr, 9, "start", True)
        if func:
            lines = func.split("\n")
            for i, ln in enumerate(lines):
                s += label(490, yy+20+i*12, ln, DARK, 8)
            yy += 20 + len(lines)*12 + 5
        else:
            yy += 17

    # Lobes detail
    s += box(20, 405, 765, 180, fill=WHITE, stroke=PRIMARY)
    s += label(400, 425, "Доли коры больших полушарий и их зоны", ACCENT, 11, "middle", True)

    lobes = [
        ("Лобная доля", "Мышление, планирование,\nречь (зона Брока),\nпроизвольные движения\n(моторная зона)", BLUE, "#DBEAFE"),
        ("Теменная доля", "Осязание, температура,\nболь, проприоцепция\n(сенсорная зона),\nпространственное восприятие", PURPLE, "#E9D5FF"),
        ("Височная доля", "Слух, память,\nузнавание лиц,\nречь (зона Вернике),\nэмоции", ORANGE, "#FEF3C7"),
        ("Затылочная доля", "Зрение,\nобработка\nзрительной\nинформации", RED, "#FEE2E2"),
    ]
    xx = 35
    for name, func, clr, bg in lobes:
        s += f'<rect x="{xx}" y="440" width="175" height="130" rx="6" fill="{bg}" stroke="{clr}" stroke-width="1.5"/>'
        s += label(xx+87, 458, name, clr, 10, "middle", True)
        lines = func.split("\n")
        for i, ln in enumerate(lines):
            s += label(xx+10, 475+i*15, ln, DARK, 9)
        xx += 185

    s += label(400, 590, "Урок 12", GRAY, 10, "middle")
    s += svg_footer()
    return s


# ============================================================
# Generate all SVGs
# ============================================================
generators = [
    (1, lesson1), (2, lesson2), (3, lesson3), (4, lesson4),
    (5, lesson5), (6, lesson6), (7, lesson7), (8, lesson8),
    (9, lesson9), (10, lesson10), (11, lesson11), (12, lesson12),
]

results = []
for num, gen_func in generators:
    filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
    content = gen_func()
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    size = os.path.getsize(filepath)
    results.append(f"lesson-{num}.svg — {size} bytes")

print("=" * 50)
print("Generated 12 Biology SVG files:")
print("=" * 50)
for r in results:
    print(f"  ✓ {r}")
print("=" * 50)
print(f"Output directory: {OUTPUT_DIR}")
