#!/usr/bin/env python3
"""Generate Grade 8 Literature SVG images for 5 lessons.

Warm brown/amber color scheme (#92400E primary), parchment backgrounds,
character diagrams, themes, plot structure, and visual elements.
"""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/literature"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Colour palette ──────────────────────────────────────────────────
PRIMARY      = "#92400E"   # warm brown
PRIMARY_DARK = "#78350F"
PRIMARY_LITE = "#B45309"
ACCENT       = "#D97706"   # amber
ACCENT_LITE  = "#F59E0B"
GOLD         = "#D4A017"
PARCHMENT_L  = "#FFFBF0"
PARCHMENT_D  = "#FEF3C7"
TEXT_DARK    = "#44260A"
TEXT_MED     = "#78350F"
TEXT_LIGHT   = "#A16207"
WHITE        = "#FFFFFF"
CREAM        = "#FEFCE8"
WARM_BG1     = "#FFFBF0"
WARM_BG2     = "#FEF3C7"
BORDER_AMBER = "#D97706"
HIGHLIGHT_BG = "#FEF3C7"
BOX_BG       = "#FFF7ED"
CARD_BG      = "#FFFBEB"


def escape(text: str) -> str:
    """Escape XML special characters in text content."""
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;"))


def svg_root() -> ET.Element:
    """Return a new <svg> root element 800x600."""
    svg = ET.Element("svg",
                     xmlns="http://www.w3.org/2000/svg",
                     width="800", height="600",
                     viewBox="0 0 800 600")
    return svg


def add_defs(svg: ET.Element):
    """Add common gradient / filter defs."""
    defs = ET.SubElement(svg, "defs")

    # Parchment background gradient
    g1 = ET.SubElement(defs, "linearGradient", id="parchBg",
                       x1="0%", y1="0%", x2="0%", y2="100%")
    ET.SubElement(g1, "stop", offset="0%", stopColor=PARCHMENT_L)
    ET.SubElement(g1, "stop", offset="100%", stopColor=PARCHMENT_D)

    # Header gradient (brown)
    g2 = ET.SubElement(defs, "linearGradient", id="headerGrad",
                       x1="0%", y1="0%", x2="100%", y2="0%")
    ET.SubElement(g2, "stop", offset="0%", stopColor=PRIMARY_DARK)
    ET.SubElement(g2, "stop", offset="50%", stopColor=PRIMARY)
    ET.SubElement(g2, "stop", offset="100%", stopColor=PRIMARY_DARK)

    # Accent amber gradient
    g3 = ET.SubElement(defs, "linearGradient", id="amberGrad",
                       x1="0%", y1="0%", x2="0%", y2="100%")
    ET.SubElement(g3, "stop", offset="0%", stopColor=ACCENT_LITE)
    ET.SubElement(g3, "stop", offset="100%", stopColor=ACCENT)

    # Card shadow filter
    f1 = ET.SubElement(defs, "filter", id="cardShadow",
                       x="-3%", y="-3%", width="106%", height="110%")
    ET.SubElement(f1, "feDropShadow", dx="1", dy="2",
                  stdDeviation="2", floodColor="#00000020")

    # Glow filter for icons
    f2 = ET.SubElement(defs, "filter", id="glow",
                       x="-10%", y="-10%", width="120%", height="120%")
    ET.SubElement(f2, "feDropShadow", dx="0", dy="0",
                  stdDeviation="3", floodColor="#D9770660")

    # Parchment texture pattern
    pat = ET.SubElement(defs, "pattern", id="parchTex",
                        width="20", height="20",
                        patternUnits="userSpaceOnUse")
    ET.SubElement(pat, "rect", width="20", height="20", fill="none")
    ET.SubElement(pat, "circle", cx="10", cy="10", r="0.5",
                  fill="#D4A01715")

    # Decorative border pattern
    pat2 = ET.SubElement(defs, "pattern", id="borderPat",
                         width="12", height="12",
                         patternUnits="userSpaceOnUse")
    ET.SubElement(pat2, "rect", width="12", height="12", fill="none")
    ET.SubElement(pat2, "path", d="M0,6 L6,0 L12,6 L6,12 Z",
                  fill="none", stroke="#D9770630", strokeWidth="0.5")


def add_background(svg: ET.Element):
    """Parchment-like background with decorative border."""
    ET.SubElement(svg, "rect", x="0", y="0", width="800", height="600",
                  fill="url(#parchBg)")
    ET.SubElement(svg, "rect", x="0", y="0", width="800", height="600",
                  fill="url(#parchTex)")
    # Decorative border
    ET.SubElement(svg, "rect", x="4", y="4", width="792", height="592",
                  fill="none", stroke=ACCENT, strokeWidth="2", rx="8")
    ET.SubElement(svg, "rect", x="8", y="8", width="784", height="584",
                  fill="none", stroke="#D9770640", strokeWidth="1", rx="6")


def add_header(svg: ET.Element, title: str, subtitle: str):
    """Amber-brown header bar with title and subtitle."""
    ET.SubElement(svg, "rect", x="0", y="0", width="800", height="72",
                  fill="url(#headerGrad)", rx="8")
    ET.SubElement(svg, "rect", x="0", y="70", width="800", height="3",
                  fill=GOLD)
    # Decorative lines
    ET.SubElement(svg, "line", x1="20", y1="68", x2="780", y2="68",
                  stroke="#D4A01760", strokeWidth="0.5")

    t = ET.SubElement(svg, "text", x="400", y="32",
                      fontSize="21", fill=WHITE,
                      textAnchor="middle", fontFamily="sans-serif",
                      fontWeight="bold")
    t.text = title
    s = ET.SubElement(svg, "text", x="400", y="56",
                      fontSize="12", fill="#FEF3C7",
                      textAnchor="middle", fontFamily="sans-serif")
    s.text = subtitle


def add_card(svg: ET.Element, x, y, w, h, title=None, lines=None,
             fill=BOX_BG, title_size=13, line_size=11, title_color=PRIMARY,
             line_color=TEXT_MED, accent_top=True, icon_char=None):
    """Draw a rounded card with optional title + text lines."""
    g = ET.SubElement(svg, "g")
    ET.SubElement(g, "rect", x=str(x), y=str(y), width=str(w), height=str(h),
                  fill=fill, stroke=ACCENT, strokeWidth="1", rx="6",
                  filter="url(#cardShadow)")
    if accent_top:
        ET.SubElement(g, "rect", x=str(x), y=str(y), width=str(w),
                      height="4", fill="url(#amberGrad)", rx="6")
        # Cover bottom corners of accent strip
        ET.SubElement(g, "rect", x=str(x), y=str(y + 2), width=str(w),
                      height="2", fill="url(#amberGrad)")

    cy = y + 18
    if icon_char:
        ic = ET.SubElement(g, "text", x=str(x + 12), y=str(cy),
                           fontSize="16", fill=ACCENT,
                           fontFamily="sans-serif")
        ic.text = icon_char
        if title:
            t = ET.SubElement(g, "text", x=str(x + 32), y=str(cy),
                              fontSize=str(title_size), fill=title_color,
                              fontFamily="sans-serif", fontWeight="bold")
            t.text = title
    elif title:
        t = ET.SubElement(g, "text", x=str(x + 10), y=str(cy),
                          fontSize=str(title_size), fill=title_color,
                          fontFamily="sans-serif", fontWeight="bold")
        t.text = title

    cy += 16
    if lines:
        for line in lines:
            lt = ET.SubElement(g, "text", x=str(x + 14), y=str(cy),
                               fontSize=str(line_size), fill=line_color,
                               fontFamily="sans-serif")
            lt.text = line
            cy += 15


def add_arrow(svg: ET.Element, x1, y1, x2, y2, color=ACCENT, sw=2):
    """Draw a connecting arrow."""
    ET.SubElement(svg, "line", x1=str(x1), y1=str(y1),
                  x2=str(x2), y2=str(y2),
                  stroke=color, strokeWidth=str(sw))
    # arrowhead
    dx = x2 - x1
    dy = y2 - y1
    length = (dx**2 + dy**2) ** 0.5
    if length == 0:
        return
    ux, uy = dx / length, dy / length
    px, py = -uy, ux  # perpendicular
    ax = x2 - ux * 8 + px * 4
    ay = y2 - uy * 8 + py * 4
    bx = x2 - ux * 8 - px * 4
    by = y2 - uy * 8 - py * 4
    ET.SubElement(svg, "polygon",
                  points=f"{x2},{y2} {ax},{ay} {bx},{by}",
                  fill=color)


def add_oval(svg: ET.Element, cx, cy, rx, ry, fill, stroke=ACCENT, text="",
             font_size=11, text_color=TEXT_DARK):
    """Draw a rounded oval with centered text."""
    ET.SubElement(svg, "ellipse", cx=str(cx), cy=str(cy),
                  rx=str(rx), ry=str(ry),
                  fill=fill, stroke=stroke, strokeWidth="1.5")
    if text:
        t = ET.SubElement(svg, "text", x=str(cx), y=str(cy + 4),
                          fontSize=str(font_size), fill=text_color,
                          textAnchor="middle", fontFamily="sans-serif",
                          fontWeight="bold")
        t.text = text


def add_theme_box(svg: ET.Element, x, y, w, h, label, color=ACCENT):
    """Small highlighted theme tag."""
    ET.SubElement(svg, "rect", x=str(x), y=str(y), width=str(w), height=str(h),
                  fill=color, rx="12")
    t = ET.SubElement(svg, "text", x=str(x + w / 2), y=str(y + h / 2 + 4),
                      fontSize="10", fill=WHITE,
                      textAnchor="middle", fontFamily="sans-serif",
                      fontWeight="bold")
    t.text = label


def add_book_icon(svg: ET.Element, x, y, size=20, color=PRIMARY):
    """Simple book icon."""
    g = ET.SubElement(svg, "g", transform=f"translate({x},{y})")
    s = size
    ET.SubElement(g, "rect", x="0", y=str(s * 0.1), width=str(s * 0.8),
                  height=str(s * 0.8), fill=color, rx="2")
    ET.SubElement(g, "rect", x=str(s * 0.1), y="0", width=str(s * 0.8),
                  height=str(s * 0.8), fill=ACCENT, rx="2")
    ET.SubElement(g, "line", x1=str(s * 0.5), y1="0",
                  x2=str(s * 0.5), y2=str(s * 0.8),
                  stroke=WHITE, strokeWidth="1")
    ET.SubElement(g, "line", x1=str(s * 0.2), y1=str(s * 0.25),
                  x2=str(s * 0.45), y2=str(s * 0.25),
                  stroke=WHITE, strokeWidth="0.8")
    ET.SubElement(g, "line", x1=str(s * 0.55), y1=str(s * 0.25),
                  x2=str(s * 0.8), y2=str(s * 0.25),
                  stroke=WHITE, strokeWidth="0.8")


def add_quill_icon(svg: ET.Element, x, y, size=24, color=PRIMARY):
    """Simple quill/feather icon."""
    g = ET.SubElement(svg, "g", transform=f"translate({x},{y})")
    s = size
    ET.SubElement(g, "path",
                  d=f"M{s*0.5},{0} Q{s*0.8},{s*0.3} {s*0.6},{s*0.7} "
                    f"L{s*0.5},{s} L{s*0.4},{s*0.7} Q{s*0.2},{s*0.3} {s*0.5},{0}Z",
                  fill=color, opacity="0.7")
    ET.SubElement(g, "line", x1=str(s * 0.5), y1=str(s * 0.6),
                  x2=str(s * 0.5), y2=str(s),
                  stroke=PRIMARY_DARK, strokeWidth="1")


def add_footer(svg: ET.Element, text: str):
    """Footer bar with lesson label."""
    ET.SubElement(svg, "rect", x="0", y="580", width="800", height="20",
                  fill=PRIMARY_DARK, rx="0")
    ET.SubElement(svg, "rect", x="0", y="578", width="800", height="2",
                  fill=GOLD)
    t = ET.SubElement(svg, "text", x="400", y="594",
                      fontSize="10", fill=CREAM,
                      textAnchor="middle", fontFamily="sans-serif")
    t.text = text


# ════════════════════════════════════════════════════════════════════
# LESSON 1 – Золотой век русской литературы
# ════════════════════════════════════════════════════════════════════
def lesson1():
    svg = svg_root()
    add_defs(svg)
    add_background(svg)
    add_header(svg,
               "Золотой век русской литературы",
               "Пушкин · Лермонтов · Гоголь — великая классика XIX века")
    add_footer(svg, "8 класс · Литература · Урок 1")

    # ── Timeline ribbon (top area) ──
    ET.SubElement(svg, "rect", x="20", y="82", width="760", height="48",
                  fill="#FFFBEB", stroke=ACCENT, strokeWidth="1", rx="6")
    # Timeline line
    ET.SubElement(svg, "line", x1="50", y1="106", x2="750", y2="106",
                  stroke=PRIMARY, strokeWidth="2")
    # Dots on timeline
    for (cx, yr) in [(100, "1799"), (250, "1814"), (400, "1809"), (550, "1820-е"), (700, "1830-е")]:
        ET.SubElement(svg, "circle", cx=str(cx), cy="106", r="6",
                      fill=ACCENT_LITE, stroke=PRIMARY, strokeWidth="1.5")
        yt = ET.SubElement(svg, "text", x=str(cx), y="98",
                           fontSize="9", fill=PRIMARY,
                           textAnchor="middle", fontFamily="sans-serif",
                           fontWeight="bold")
        yt.text = yr
    tl1 = ET.SubElement(svg, "text", x="50", y="122",
                        fontSize="8", fill=TEXT_LIGHT, fontFamily="sans-serif")
    tl1.text = "Рождение Пушкина"
    tl2 = ET.SubElement(svg, "text", x="200", y="122",
                        fontSize="8", fill=TEXT_LIGHT, fontFamily="sans-serif")
    tl2.text = "Рождение Лермонтова"
    tl3 = ET.SubElement(svg, "text", x="350", y="122",
                        fontSize="8", fill=TEXT_LIGHT, fontFamily="sans-serif")
    tl3.text = "Рождение Гоголя"
    tl4 = ET.SubElement(svg, "text", x="510", y="122",
                        fontSize="8", fill=TEXT_LIGHT, fontFamily="sans-serif")
    tl4.text = "Расцвет романтизма"
    tl5 = ET.SubElement(svg, "text", x="660", y="122",
                        fontSize="8", fill=TEXT_LIGHT, fontFamily="sans-serif")
    tl5.text = "Зрелый реализм"

    # ── Three author cards ──
    # Pushkin
    add_card(svg, 20, 140, 245, 175,
             title="А.С. Пушкин (1799–1837)",
             lines=[
                 "Основоположник русского",
                 "литературного языка",
                 "",
                 "Произведения:",
                 "• «Евгений Онегин»",
                 "• «Капитанская дочка»",
                 "• «Медный всадник»",
                 "• Лирика: любовь, свобода",
                 "• Сказки"
             ],
             icon_char="\u270E")

    # Lermontov
    add_card(svg, 278, 140, 245, 175,
             title="М.Ю. Лермонтов (1814–1841)",
             lines=[
                 "Продолжатель пушкинских",
                 "традиций, бунтарь и мечтатель",
                 "",
                 "Произведения:",
                 "• «Герой нашего времени»",
                 "• «Мцыри»",
                 "• «Песня про царя Ивана»",
                 "• «Смерть поэта»",
                 "• Лирика: одиночество"
             ],
             icon_char="\u270E")

    # Gogol
    add_card(svg, 536, 140, 245, 175,
             title="Н.В. Гоголь (1809–1852)",
             lines=[
                 "Мастер сатиры и гротеска,",
                 "гениальный юмор и грусть",
                 "",
                 "Произведения:",
                 "• «Ревизор»",
                 "• «Мёртвые души»",
                 "• «Шинель»",
                 "• «Тарас Бульба»",
                 "• «Вечера на хуторе»"
             ],
             icon_char="\u270E")

    # ── Key themes section ──
    add_card(svg, 20, 325, 760, 100,
             title="Ключевые темы Золотого века",
             lines=[], fill="#FEF3C7")
    # Theme tags
    themes = ["Свобода", "Любовь", "Долг и честь", "Одиночество",
              "Россия и народ", "Человек и общество", "Сатира",
              "Реализм"]
    tx = 35
    for i, th in enumerate(themes):
        w = len(th) * 9 + 20
        add_theme_box(svg, tx, 360, w, 24, th,
                      color=[PRIMARY, ACCENT, PRIMARY_LITE, ACCENT_LITE,
                             PRIMARY, ACCENT, PRIMARY_LITE, ACCENT_LITE][i])
        tx += w + 8
        if tx > 720:
            tx = 35

    # Sub-text
    st = ET.SubElement(svg, "text", x="400", y="413",
                       fontSize="10", fill=TEXT_LIGHT,
                       textAnchor="middle", fontFamily="sans-serif")
    st.text = "XIX век — эпоха, когда русская литература обрела мировое значение"

    # ── Literary movements diagram ──
    add_card(svg, 20, 435, 370, 135,
             title="Литературные направления",
             lines=[
                 "Сентиментализм → Романтизм → Реализм",
                 "",
                 "Карамзин        Пушкин      Гоголь",
                 "                 Лермонтов   Пушкин",
                 "",
                 "От чувств — к мечте — к правде жизни"
             ],
             fill=BOX_BG, line_color=TEXT_MED)

    # ── Significance box ──
    add_card(svg, 400, 435, 380, 135,
             title="Значение Золотого века",
             lines=[
                 "• Формирование русского лит. языка",
                 "• Мировое признание русской культуры",
                 "• Создание национального эпоса",
                 "• Глубокий психологизм и реализм",
                 "• Влияние на всю мировую литературу",
                 "• «Умом Россию не понять...»"
             ],
             fill=BOX_BG, line_color=TEXT_MED)

    # Decorative quill
    add_quill_icon(svg, 740, 545, 28, PRIMARY_DARK)

    return svg


# ════════════════════════════════════════════════════════════════════
# LESSON 2 – Роман «Капитанская дочка»
# ════════════════════════════════════════════════════════════════════
def lesson2():
    svg = svg_root()
    add_defs(svg)
    add_background(svg)
    add_header(svg,
               "Роман «Капитанская дочка»",
               "А.С. Пушкин — исторический роман о чести и долге")
    add_footer(svg, "8 класс · Литература · Урок 2")

    # ── Character diagram (left side) ──
    add_card(svg, 20, 82, 260, 235,
             title="Главные герои",
             lines=[], fill=BOX_BG)

    # Central oval — Grinev
    add_oval(svg, 150, 122, 55, 20, "#FEF3C7", PRIMARY, "Гринёв П.А.")
    # Left oval — Masha
    add_oval(svg, 70, 168, 55, 20, CREAM, ACCENT, "Маша Миронова")
    # Right oval — Pugachev
    add_oval(svg, 230, 168, 55, 20, "#FDE68A", PRIMARY_LITE, "Пугачёв")
    # Bottom left — Shvabrin
    add_oval(svg, 70, 220, 55, 20, "#FFFBEB", "#B91C1C", "Швабрин")
    # Bottom center — parents
    add_oval(svg, 150, 270, 60, 20, CREAM, TEXT_LIGHT, "Семья Гринёвых")
    # Bottom right — Catherine
    add_oval(svg, 240, 270, 55, 20, "#FEF3C7", ACCENT, "Екатерина II")

    # Arrows between characters
    add_arrow(svg, 120, 138, 90, 152, ACCENT, 1.5)
    add_arrow(svg, 180, 138, 210, 152, PRIMARY_LITE, 1.5)
    add_arrow(svg, 85, 185, 85, 202, "#B91C1C", 1.5)
    add_arrow(svg, 130, 185, 140, 254, TEXT_LIGHT, 1.5)
    add_arrow(svg, 150, 138, 150, 254, TEXT_LIGHT, 1)
    add_arrow(svg, 220, 185, 225, 254, ACCENT, 1)

    # Relationship labels
    rl1 = ET.SubElement(svg, "text", x="85", y="150",
                        fontSize="8", fill=TEXT_LIGHT, fontFamily="sans-serif")
    rl1.text = "любовь"
    rl2 = ET.SubElement(svg, "text", x="200", y="150",
                        fontSize="8", fill=TEXT_LIGHT, fontFamily="sans-serif")
    rl2.text = "милость"
    rl3 = ET.SubElement(svg, "text", x="50", y="198",
                        fontSize="8", fill="#B91C1C", fontFamily="sans-serif")
    rl3.text = "вражда"

    # ── Themes (right side) ──
    add_card(svg, 295, 82, 240, 235,
             title="Основные темы",
             lines=[
                 "\u2666 Честь и достоинство",
                 "  «Береги честь смолоду»",
                 "",
                 "\u2666 Долг перед Родиной",
                 "  Верность присяге",
                 "",
                 "\u2666 Любовь и верность",
                 "  Маша спасает Гринёва",
                 "",
                 "\u2666 Милосердие",
                 "  Пугачёв помиловал Гринёва",
                 "",
                 "\u2666 Народ и власть",
                 "  Пугачёвщина — бунт"
             ],
             fill=CREAM, line_color=TEXT_MED)

    # ── Plot structure ──
    add_card(svg, 550, 82, 230, 235,
             title="Структура романа",
             lines=[
                 "Эпиграф: пословица",
                 "  «Береги честь смолоду»",
                 "",
                 "I. Детство Гринёва",
                 "   Савельич, подарок, дуэль",
                 "",
                 "II. Служба в крепости",
                 "   Маша, Швабрин, любовь",
                 "",
                 "III. Пугачёвский бунт",
                 "   Захват крепости, суд",
                 "",
                 "IV. Освобождение Маши",
                 "   Екатерина II, финал"
             ],
             fill=BOX_BG, line_color=TEXT_MED)

    # ── Quote box ──
    add_card(svg, 20, 328, 760, 60,
             title="",
             lines=[],
             fill="#FEF3C7")
    qt = ET.SubElement(svg, "text", x="400", y="352",
                       fontSize="14", fill=PRIMARY,
                       textAnchor="middle", fontFamily="sans-serif",
                       fontStyle="italic", fontWeight="bold")
    qt.text = "«Береги платье снову, а честь смолоду»"
    qa = ET.SubElement(svg, "text", x="400", y="372",
                       fontSize="10", fill=TEXT_LIGHT,
                       textAnchor="middle", fontFamily="sans-serif")
    qa.text = "— Эпиграф к роману (народная пословица)"

    # ── Grinev vs Shvabrin comparison ──
    add_card(svg, 20, 398, 380, 88,
             title="Гринёв — Честь",
             lines=[
                 "• Верность присяге и долгу",
                 "• Благородство к врагам",
                 "• Искренняя любовь к Маше",
                 "• Честность перед судом"
             ],
             fill=CREAM, accent_top=True)

    add_card(svg, 400, 398, 380, 88,
             title="Швабрин — Бесчестие",
             lines=[
                 "• Переход на сторону бунта",
                 "• Клевета и предательство",
                 "• Насилие над Машей",
                 "• Утрата человеческого облика"
             ],
             fill="#FFFBEB", accent_top=True)

    # ── Historical context ──
    add_card(svg, 20, 496, 760, 76,
             title="Исторический контекст",
             lines=[
                 "Крестьянская война 1773–1775 гг. под предводительством Емельяна Пугачёва. Пушкин изучал",
                 "архивные документы и создал художественное произведение, где переплетаются история и личная",
                 "судьба. Роман написан в форме мемуаров Петра Гринёва — воспоминания очевидца событий."
             ],
             fill=BOX_BG, line_color=TEXT_MED)

    add_book_icon(svg, 748, 540, 22, PRIMARY_DARK)

    return svg


# ════════════════════════════════════════════════════════════════════
# LESSON 3 – Роман «Герой нашего времени»
# ════════════════════════════════════════════════════════════════════
def lesson3():
    svg = svg_root()
    add_defs(svg)
    add_background(svg)
    add_header(svg,
               "Роман «Герой нашего времени»",
               "М.Ю. Лермонтов — психологический портрет поколения")
    add_footer(svg, "8 класс · Литература · Урок 3")

    # ── Pechorin portrait diagram ──
    add_card(svg, 20, 82, 260, 230,
             title="Печорин — «лишний человек»",
             lines=[], fill=BOX_BG)

    # Central character oval
    add_oval(svg, 150, 118, 65, 22, "#FDE68A", PRIMARY, "Печорин")

    # Trait ovals radiating out
    traits = [
        (50, 160, "Скептицизм"),
        (150, 160, "Жажда жизни"),
        (250, 160, "Разочарование"),
        (50, 210, "Эгоизм"),
        (150, 210, "Рефлексия"),
        (250, 210, "Гордость"),
        (100, 265, "Страсть"),
        (200, 265, "Одиночество"),
    ]
    for (cx, cy, label) in traits:
        add_oval(svg, cx, cy, 50, 16, CREAM, ACCENT, label, 9, TEXT_MED)
        # Line from Pechorin to trait
        ET.SubElement(svg, "line", x1="150", y1="136",
                      x2=str(cx), y2=str(cy - 14),
                      stroke="#D9770640", strokeWidth="0.8",
                      strokeDasharray="3,3")

    # ── Chapters / structure ──
    add_card(svg, 295, 82, 240, 230,
             title="Структура романа",
             lines=[
                 "Нарушенная хронология:",
                 "",
                 "1. «Бэла» — любовь горянки",
                 "2. «Максим Максимыч» —",
                 "    встреча спустя годы",
                 "3. «Тамань» — контрабандисты",
                 "4. «Княжна Мери» —",
                 "    светское общество, дуэль",
                 "5. «Фаталист» — предопределение",
                 "",
                 "Хронологический порядок:",
                 "Тамань → Княжна Мери →",
                 "Бэла → Фаталист"
             ],
             fill=CREAM, line_color=TEXT_MED)

    # ── Key themes ──
    add_card(svg, 550, 82, 230, 230,
             title="Ключевые темы",
             lines=[
                 "\u2666 Лишний человек",
                 "  Непонятый, ненужный обществу",
                 "",
                 "\u2666 Свобода и судьба",
                 "  Фатализм vs воля",
                 "",
                 "\u2666 Любовь и разрушение",
                 "  Печорин губит тех,",
                 "  кого любит",
                 "",
                 "\u2666 Маски и лицемерие",
                 "  Светское общество —",
                 "  театр притворства"
             ],
             fill=BOX_BG, line_color=TEXT_MED)

    # ── Quote ──
    add_card(svg, 20, 322, 760, 55,
             title="",
             lines=[], fill="#FEF3C7")
    qt = ET.SubElement(svg, "text", x="400", y="346",
                       fontSize="13", fill=PRIMARY,
                       textAnchor="middle", fontFamily="sans-serif",
                       fontStyle="italic", fontWeight="bold")
    qt.text = "«Герой нашего времени... это портрет, но не одного человека»"
    qa = ET.SubElement(svg, "text", x="400", y="364",
                       fontSize="10", fill=TEXT_LIGHT,
                       textAnchor="middle", fontFamily="sans-serif")
    qa.text = "— М.Ю. Лермонтов, Предисловие к роману"

    # ── Pechorin's relationships ──
    add_card(svg, 20, 387, 380, 95,
             title="Любовь в романе",
             lines=[
                 "Бэла — искренняя, но погибшая любовь",
                 "Княжна Мери — игра в чувства, дуэль",
                 "Вера — единственная понятая им женщина",
                 "Каждая любовь — разочарование и боль"
             ],
             fill=CREAM, line_color=TEXT_MED)

    add_card(svg, 400, 387, 380, 95,
             title="Печорин и общество",
             lines=[
                 "Максим Максимыч — доброта и простота",
                 "Грушницкий — карикатура на романтика",
                 "Доктор Вернер — циничный друг",
                 "Контрабандисты — свобода вне закона"
             ],
             fill=BOX_BG, line_color=TEXT_MED)

    # ── Psychological portrait detail ──
    add_card(svg, 20, 492, 760, 80,
             title="Психологический метод Лермонтова",
             lines=[
                 "Лермонтов первым в русской литературе создал глубокий психологический портрет героя.",
                 "Роман раскрывает внутренний мир Печорина через его поступки, дневник и восприятие",
                 "окружающих. Герой анализирует себя, но не может измениться — трагедия рефлексии."
             ],
             fill=BOX_BG, line_color=TEXT_MED)

    add_quill_icon(svg, 740, 548, 26, PRIMARY_DARK)

    return svg


# ════════════════════════════════════════════════════════════════════
# LESSON 4 – Комедия «Ревизор»
# ════════════════════════════════════════════════════════════════════
def lesson4():
    svg = svg_root()
    add_defs(svg)
    add_background(svg)
    add_header(svg,
               "Комедия «Ревизор»",
               "Н.В. Гоголь — сатира на чиновничество и общественные пороки")
    add_footer(svg, "8 класс · Литература · Урок 4")

    # ── Characters map ──
    add_card(svg, 20, 82, 500, 210,
             title="Система персонажей",
             lines=[], fill=BOX_BG)

    # Mayor (center top)
    add_oval(svg, 270, 115, 60, 22, "#FDE68A", PRIMARY, "Городничий")
    # Khlestakov (center)
    add_oval(svg, 270, 165, 55, 22, "#FFFBEB", "#B91C1C", "Хлестаков")
    # Supporting characters
    chars = [
        (80, 130, "Анна Андреевна"),
        (80, 175, "Марья Антоновна"),
        (460, 130, "Ляпкин-Тяпкин"),
        (460, 175, "Земляника"),
        (80, 230, "Бобчинский"),
        (170, 230, "Добчинский"),
        (370, 230, "Шпекин"),
        (460, 230, "Уховертов"),
    ]
    for (cx, cy, label) in chars:
        add_oval(svg, cx, cy, 60, 16, CREAM, ACCENT, label, 9, TEXT_MED)

    # Arrows — fear radiates from Khlestakov
    for (cx, cy, _) in chars:
        ET.SubElement(svg, "line", x1="270", y1=str(cy - 14),
                      x2=str(cx), y2=str(cy - 14),
                      stroke="#D9770630", strokeWidth="0.7",
                      strokeDasharray="2,3")
        # arrows from mayor to khlestakov
    add_arrow(svg, 270, 135, 270, 145, PRIMARY, 1.5)

    # Label "страх"
    sl = ET.SubElement(svg, "text", x="290", y="150",
                       fontSize="8", fill="#B91C1C", fontFamily="sans-serif")
    sl.text = "страх"

    # ── Themes ──
    add_card(svg, 535, 82, 245, 210,
             title="Основные темы",
             lines=[
                 "\u2666 Чиновничий произвол",
                 "  Взятки, казнокрадство",
                 "",
                 "\u2666 Страх перед властью",
                 "  Городничий боится ревизора",
                 "",
                 "\u2666 Хлестаковщина",
                 "  Враньё как образ жизни",
                 "",
                 "\u2666 Чинопочитание",
                 "  Рабская психология",
                 "",
                 "\u2666 Смех сквозь слёзы"
             ],
             fill=CREAM, line_color=TEXT_MED)

    # ── Khlestakov's characteristics ──
    add_card(svg, 20, 302, 380, 130,
             title="Хлестаков и «хлестаковщина»",
             lines=[
                 "Хлестаков — мелкий чиновник, принятый за ревизора.",
                 "Суть «хлестаковщины»:",
                 "• Мнимая значительность без оснований",
                 "• Болтливость и самовосхваление",
                 "• Лёгкость и поверхностность",
                 "• Способность увлечь окружающих враньём",
                 "«Лёгкость в мыслях необыкновенная»"
             ],
             fill=BOX_BG, line_color=TEXT_MED)

    # ── Plot stages ──
    add_card(svg, 400, 302, 380, 130,
             title="Развитие действия",
             lines=[
                 "1. Известие о ревизоре — паника",
                 "2. Ошибка: Хлестаков = ревизор",
                 "3. Враньё Хлестакова растёт",
                 "4. Сватовство к Марье Антоновне",
                 "5. Бегство Хлестакова",
                 "6. Чтение письма — разоблачение",
                 "7. Немая сцена — настоящий ревизор!"
             ],
             fill=BOX_BG, line_color=TEXT_MED)

    # ── Famous quote ──
    add_card(svg, 20, 442, 760, 55,
             title="",
             lines=[], fill="#FEF3C7")
    qt = ET.SubElement(svg, "text", x="400", y="466",
                       fontSize="14", fill=PRIMARY,
                       textAnchor="middle", fontFamily="sans-serif",
                       fontStyle="italic", fontWeight="bold")
    qt.text = "«На зеркало неча пенять, коли рожа крива»"
    qa = ET.SubElement(svg, "text", x="400", y="484",
                       fontSize="10", fill=TEXT_LIGHT,
                       textAnchor="middle", fontFamily="sans-serif")
    qa.text = "— Эпиграф к комедии (народная пословица)"

    # ── Silent scene / significance ──
    add_card(svg, 20, 507, 380, 65,
             title="Немая сцена",
             lines=[
                 "Финал — окаменение всех персонажей.",
                 "Метафора застывшего общества."
             ],
             fill=CREAM, line_color=TEXT_MED)

    add_card(svg, 400, 507, 380, 65,
             title="Значение комедии",
             lines=[
                 "Гоголь обличил пороки всей России.",
                 "«Ревизор» — зеркало русского общества."
             ],
             fill=BOX_BG, line_color=TEXT_MED)

    add_book_icon(svg, 748, 548, 22, PRIMARY_DARK)

    return svg


# ════════════════════════════════════════════════════════════════════
# LESSON 5 – Поэма «Мёртвые души»
# ════════════════════════════════════════════════════════════════════
def lesson5():
    svg = svg_root()
    add_defs(svg)
    add_background(svg)
    add_header(svg,
               "Поэма «Мёртвые души»",
               "Н.В. Гоголь — русская душа и путь от смерти к возрождению")
    add_footer(svg, "8 класс · Литература · Урок 5")

    # ── Landowners progression ──
    add_card(svg, 20, 82, 760, 195,
             title="Помещики — деградация личности (последовательность Чичикова)",
             lines=[], fill=BOX_BG)

    landowners = [
        ("Манилов", "Сладость,\nпустота", "#FEF3C7", 70),
        ("Коробочка", "Мелочность,\nнакопительство", CREAM, 205),
        ("Ноздрёв", "Разгул,\nбесцельность", "#FDE68A", 340),
        ("Собакевич", "Грубость,\nкулак", "#FFFBEB", 475),
        ("Плюшкин", "Омертвение,\nскука", "#FBBF2430", 610),
    ]

    for (name, desc, bg, x) in landowners:
        # Character card
        ET.SubElement(svg, "rect", x=str(x), y="118", width="120",
                      height="80", fill=bg, stroke=ACCENT,
                      strokeWidth="1", rx="6")
        nt = ET.SubElement(svg, "text", x=str(x + 60), y="138",
                           fontSize="12", fill=PRIMARY,
                           textAnchor="middle", fontFamily="sans-serif",
                           fontWeight="bold")
        nt.text = name
        # Description lines
        dl = desc.split("\n")
        for i, d in enumerate(dl):
            dt = ET.SubElement(svg, "text", x=str(x + 60), y=str(155 + i * 14),
                               fontSize="9", fill=TEXT_MED,
                               textAnchor="middle", fontFamily="sans-serif")
            dt.text = d

    # Arrow connecting them (degradation)
    for i in range(4):
        x1 = landowners[i][3] + 120
        x2 = landowners[i + 1][3]
        add_arrow(svg, x1, 155, x2, 155, PRIMARY_LITE, 2)

    # Degradation label
    dl1 = ET.SubElement(svg, "text", x="400", y="216",
                        fontSize="10", fill="#B91C1C",
                        textAnchor="middle", fontFamily="sans-serif",
                        fontStyle="italic")
    dl1.text = "→ Деградация: от приятной пустоты к полному омертвению души →"

    # Chichikov in center
    add_oval(svg, 400, 255, 60, 18, "#FDE68A", PRIMARY, "Чичиков")

    # ── Themes ──
    add_card(svg, 20, 285, 250, 160,
             title="Основные темы",
             lines=[
                 "\u2666 «Мёртвые души» — живые ли?",
                 "   Мёртвая душа = живой мертвец",
                 "",
                 "\u2666 Русская душа",
                 "   Путь от смерти к возрождению",
                 "",
                 "\u2666 Общество и пороки",
                 "   Взятки, казнокрадство, чин",
                 "",
                 "\u2666 Духовное возрождение",
                 "   2-й том — путь к свету"
             ],
             fill=CREAM, line_color=TEXT_MED)

    # ── Chichikov's method ──
    add_card(svg, 280, 285, 260, 160,
             title="Схема Чичикова",
             lines=[
                 "План Чичикова:",
                 "1. Купить мёртвые души дёшево",
                 "2. Заложить их в Опекунский совет",
                 "3. Получить деньги за «живых»",
                 "4. Стать богатым помещиком",
                 "",
                 "Афера строится на том, что",
                 "ревизские сказки ещё не обновлены,",
                 "и мёртвые числятся живыми."
             ],
             fill=BOX_BG, line_color=TEXT_MED)

    # ── Genre features ──
    add_card(svg, 550, 285, 230, 160,
             title="Жанр: поэма",
             lines=[
                 "Почему Гоголь назвал это",
                 "«поэмой», а не романом?",
                 "",
                 "• Лирические отступления",
                 "• Образ автора-повествователя",
                 "• Философский масштаб",
                 "• Русь-тройка — символ",
                 "• Высокий пафос и смех"
             ],
             fill=BOX_BG, line_color=TEXT_MED)

    # ── Famous quote ──
    add_card(svg, 20, 455, 760, 55,
             title="",
             lines=[], fill="#FEF3C7")
    qt = ET.SubElement(svg, "text", x="400", y="479",
                       fontSize="13", fill=PRIMARY,
                       textAnchor="middle", fontFamily="sans-serif",
                       fontStyle="italic", fontWeight="bold")
    qt.text = "«Русь, куда ж несёшься ты? Дай ответ. Не даёт ответа.»"
    qa = ET.SubElement(svg, "text", x="400", y="497",
                       fontSize="10", fill=TEXT_LIGHT,
                       textAnchor="middle", fontFamily="sans-serif")
    qa.text = "— Лирическое отступление о Руси-тройке (глава 11)"

    # ── Significance ──
    add_card(svg, 20, 520, 760, 52,
             title="",
             lines=[], fill=BOX_BG)
    st1 = ET.SubElement(svg, "text", x="400", y="540",
                        fontSize="10", fill=TEXT_MED,
                        textAnchor="middle", fontFamily="sans-serif")
    st1.text = ("Гоголь задумал три тома: 1 — пороки (ад), 2 — очищение (чистилище), "
                "3 — возрождение (рай).")
    st2 = ET.SubElement(svg, "text", x="400", y="555",
                        fontSize="10", fill=TEXT_MED,
                        textAnchor="middle", fontFamily="sans-serif")
    st2.text = ("Второй том был сожжён автором. «Мёртвые души» — одно из величайших "
                "произведений русской литературы.")

    add_quill_icon(svg, 740, 555, 22, PRIMARY_DARK)

    return svg


# ════════════════════════════════════════════════════════════════════
# MAIN — generate all 5 SVGs
# ════════════════════════════════════════════════════════════════════
def write_svg(svg: ET.Element, filepath: str):
    ET.indent(svg, space="  ")
    tree = ET.ElementTree(svg)
    tree.write(filepath, encoding="unicode", xml_declaration=True)
    # Add DOCTYPE-like XML declaration properly
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    # Ensure proper first line
    if not content.startswith("<?xml"):
        content = '<?xml version="1.0" encoding="UTF-8"?>\n' + content
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✅ Written: {filepath} ({len(content)} bytes)")


def validate_svg(filepath: str) -> bool:
    """Validate SVG as well-formed XML using ElementTree."""
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        # Check it's actually an SVG
        tag = root.tag
        if "svg" not in tag.lower():
            print(f"  ⚠️  Root tag is '{tag}', expected SVG")
            return False
        return True
    except ET.ParseError as e:
        print(f"  ❌ XML Parse Error: {e}")
        return False


def main():
    print("=" * 60)
    print("Generating Grade 8 Literature SVGs")
    print("=" * 60)

    generators = [
        (1, "Золотой век русской литературы", lesson1),
        (2, "Роман «Капитанская дочка»", lesson2),
        (3, "Роман «Герой нашего времени»", lesson3),
        (4, "Комедия «Ревизор»", lesson4),
        (5, "Поэма «Мёртвые души»", lesson5),
    ]

    results = []
    for num, title, gen_func in generators:
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
        print(f"\n📝 Lesson {num}: {title}")
        svg = gen_func()
        write_svg(svg, filepath)
        valid = validate_svg(filepath)
        results.append((num, title, filepath, valid))

    # Summary
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    all_ok = True
    for (num, title, filepath, valid) in results:
        status = "✅ VALID" if valid else "❌ INVALID"
        print(f"  Lesson {num}: {status} — {filepath}")
        if not valid:
            all_ok = False

    if all_ok:
        print("\n🎉 All 5 SVGs generated and validated successfully!")
    else:
        print("\n⚠️  Some SVGs failed validation — review errors above.")

    return all_ok


if __name__ == "__main__":
    main()
