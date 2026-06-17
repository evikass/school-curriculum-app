#!/usr/bin/env python3
"""Generate Grade 7 Technology (Технология) SVG images for all 5 lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/tech"

# Color scheme — brown/amber
PRIMARY = "#B45309"
PRIMARY_LIGHT = "#D97706"
PRIMARY_DARK = "#92400E"
ACCENT = "#F59E0B"
ACCENT_LIGHT = "#FCD34D"
BG_LIGHT = "#FFFBEB"
BG_WARM = "#FEF3C7"
TEXT_DARK = "#78350F"
TEXT_MED = "#92400E"
TEXT_LIGHT = "#B45309"
WHITE = "#FFFFFF"
BORDER = "#D97706"
HIGHLIGHT_BG = "#FEF3C7"
BOX_BG = "#FFF7ED"
GREEN = "#059669"
BLUE = "#2563EB"
RED = "#DC2626"
GRAY = "#6B7280"
LIGHT_GRAY = "#E5E7EB"


def escape(text):
    """Escape XML special characters."""
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def svg_header():
    """Return standard SVG header elements."""
    return f"""<?xml version='1.0' encoding='utf-8'?>
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{BG_LIGHT}" />
      <stop offset="100%" stop-color="{BG_WARM}" />
    </linearGradient>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{PRIMARY_DARK}" />
      <stop offset="100%" stop-color="{PRIMARY}" />
    </linearGradient>
    <linearGradient id="boxGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{WHITE}" />
      <stop offset="100%" stop-color="{BOX_BG}" />
    </linearGradient>
    <filter id="shadow" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="1" dy="1" stdDeviation="2" flood-color="{PRIMARY_DARK}" flood-opacity="0.15"/>
    </filter>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="{PRIMARY}" />
    </marker>
    <marker id="arrowAmber" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="{ACCENT}" />
    </marker>
  </defs>
  <!-- Background -->
  <rect width="800" height="600" fill="url(#bgGrad)" rx="8"/>
  <rect x="0" y="0" width="800" height="4" fill="{PRIMARY}" rx="2"/>
"""


def svg_footer():
    """Return standard SVG footer."""
    return """</svg>"""


def header_bar(lesson_num, title, subtitle=""):
    """Create a header bar with lesson number and title."""
    sub_line = f'\n    <text x="780" y="55" font-size="13" fill="{ACCENT}" text-anchor="end" font-style="italic">{escape(subtitle)}</text>' if subtitle else ""
    return f"""
  <!-- Header -->
  <rect x="20" y="15" width="760" height="60" rx="8" fill="url(#headerGrad)" filter="url(#shadow)"/>
  <text x="40" y="50" font-size="14" fill="{ACCENT_LIGHT}" font-weight="bold">Урок {lesson_num}</text>
  <text x="130" y="50" font-size="20" fill="{WHITE}" font-weight="bold">{escape(title)}</text>{sub_line}
"""


def info_box(x, y, w, h, title, items, title_color=PRIMARY):
    """Create an info box with title and bullet items."""
    lines = []
    lines.append(f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="url(#boxGrad)" stroke="{BORDER}" stroke-width="1.5" filter="url(#shadow)"/>')
    lines.append(f'  <rect x="{x}" y="{y}" width="{w}" height="26" rx="6" fill="{title_color}"/>')
    lines.append(f'  <rect x="{x}" y="{y+20}" width="{w}" height="6" fill="{title_color}"/>')
    lines.append(f'  <text x="{x+w//2}" y="{y+18}" font-size="13" fill="{WHITE}" text-anchor="middle" font-weight="bold">{escape(title)}</text>')
    for i, item in enumerate(items):
        ty = y + 40 + i * 20
        if ty + 10 > y + h:
            break
        lines.append(f'  <text x="{x+12}" y="{ty}" font-size="12" fill="{TEXT_DARK}">&#8226; {escape(item)}</text>')
    return "\n".join(lines)


def highlight_box(x, y, w, h, text_lines, border_color=ACCENT, bg_color=HIGHLIGHT_BG):
    """Create a highlighted info box."""
    lines = []
    lines.append(f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{bg_color}" stroke="{border_color}" stroke-width="2" stroke-dasharray="6,3" filter="url(#shadow)"/>')
    for i, tl in enumerate(text_lines):
        lines.append(f'  <text x="{x+12}" y="{y+20+i*18}" font-size="12" fill="{TEXT_DARK}" font-weight="bold">{escape(tl)}</text>')
    return "\n".join(lines)


def stage_arrow(x, y, w, h, label, color=PRIMARY, text_color=WHITE):
    """Create a stage box with arrow shape."""
    arrow_pts = f"{x},{y} {x+w-10},{y} {x+w},{y+h//2} {x+w-10},{y+h} {x},{y+h} {x+10},{y+h//2}"
    return f"""  <polygon points="{arrow_pts}" fill="{color}" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <text x="{x+w//2}" y="{y+h//2+5}" font-size="12" fill="{text_color}" text-anchor="middle" font-weight="bold">{escape(label)}</text>"""


# ============================================================
# LESSON 1: Свойства и пороки древесины
# ============================================================
def lesson_1():
    svg = svg_header()
    svg += header_bar(1, "Свойства и пороки древесины", "Физические, механические и технологические свойства")

    # Tree cross-section diagram (top-left)
    svg += f"""
  <!-- Tree cross-section diagram -->
  <circle cx="150" cy="215" r="90" fill="#DEB887" stroke="{PRIMARY_DARK}" stroke-width="2" filter="url(#shadow)"/>
  <circle cx="150" cy="215" r="65" fill="#D2B48C" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <circle cx="150" cy="215" r="38" fill="#C4A882" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <circle cx="150" cy="215" r="14" fill="#8B7355" stroke="{PRIMARY_DARK}" stroke-width="1"/>

  <!-- Growth rings -->
  <ellipse cx="150" cy="190" rx="82" ry="7" fill="none" stroke="#A0845C" stroke-width="0.5" opacity="0.5"/>
  <ellipse cx="150" cy="235" rx="78" ry="6" fill="none" stroke="#A0845C" stroke-width="0.5" opacity="0.5"/>

  <!-- Labels with leader lines -->
  <line x1="150" y1="125" x2="150" y2="108" stroke="{TEXT_DARK}" stroke-width="1"/>
  <text x="150" y="102" font-size="10" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Кора</text>
  <line x1="215" y1="160" x2="252" y2="145" stroke="{TEXT_DARK}" stroke-width="1"/>
  <text x="265" y="148" font-size="10" fill="{TEXT_DARK}">Луб</text>
  <line x1="215" y1="215" x2="260" y2="215" stroke="{TEXT_DARK}" stroke-width="1"/>
  <text x="298" y="219" font-size="10" fill="{TEXT_DARK}">Заболонь</text>
  <line x1="188" y1="245" x2="252" y2="268" stroke="{TEXT_DARK}" stroke-width="1"/>
  <text x="280" y="272" font-size="10" fill="{TEXT_DARK}">Ядро</text>
  <text x="150" y="219" font-size="8" fill="{WHITE}" text-anchor="middle">Сердцевина</text>

  <!-- Properties: Physical -->
  {info_box(395, 90, 385, 135, "Физические свойства", [
      "Плотность: лёгкая (&lt;540 кг/м&#179;), средняя, тяжёлая (&gt;740)",
      "Влажность: свободная и связанная вода",
      "Усушка: уменьшение размеров при высыхании",
      "Разбухание: увеличение объёма при увлажнении",
      "Теплопроводность: низкая (хороший изолятор)"
  ], PRIMARY)}

  <!-- Properties: Mechanical -->
  {info_box(395, 238, 385, 120, "Механические свойства", [
      "Прочность — сопротивление разрушению (сжатие, изгиб)",
      "Твёрдость — сопротивление вдавливанию",
      "Упругость — способность восстанавливать форму",
      "Пластичность — изменение формы без разрушения",
      "Хрупкость — разрушение без заметной деформации"
  ], PRIMARY_LIGHT)}

  <!-- Technological properties -->
  {info_box(25, 325, 250, 120, "Технологические свойства", [
      "Обрабатываемость резанием",
      "Способность к гнутью",
      "Склеиваемость",
      "Способность к отделке",
      "Гвоздимость и шурупимость"
  ], ACCENT)}

  <!-- Wood defects -->
  {info_box(290, 325, 250, 120, "Пороки древесины", [
      "Сучки — снижают прочность",
      "Трещины — нарушают целостность",
      "Смоляные кармашки",
      "Гниль — разрушает структуру",
      "Наклон волокон"
  ], RED)}

  <!-- Defects continued -->
  {info_box(555, 325, 225, 120, "Влияние пороков", [
      "Сучки — ослабляют сечение",
      "Трещины — снижают прочность",
      "Гниль — делают непригодной",
      "Косослой — коробление",
      "Червоточины — разрушение"
  ], GRAY)}

  <!-- Bottom highlight -->
  {highlight_box(25, 460, 750, 50, [
      "Древесина — возобновляемый природный материал. Выбор породы зависит от назначения изделия!",
      "Пороки снижают качество: сучки ослабляют, трещины разрушают, гниль делает непригодной"
  ])}

  <!-- Comparison of wood types -->
  {info_box(25, 525, 375, 60, "Хвойные породы (мягкие)", [
      "Сосна, ель, лиственница, кедр — строительные и столярные изделия"
  ], PRIMARY_DARK)}

  {info_box(415, 525, 360, 60, "Лиственные породы (твёрдые)", [
      "Дуб, берёза, бук, ясень, липа — мебель, резьба, декор"
  ], PRIMARY)}
"""
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 2: Ручная обработка древесины
# ============================================================
def lesson_2():
    svg = svg_header()
    svg += header_bar(2, "Ручная обработка древесины", "Инструменты, операции и техника безопасности")

    # Saw illustration (top-left)
    svg += f"""
  <!-- Saw illustration -->
  <rect x="35" y="100" width="180" height="7" rx="2" fill="{GRAY}" stroke="#4B5563" stroke-width="1"/>
  <rect x="215" y="90" width="60" height="27" rx="4" fill="#8B7355" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <!-- Saw teeth -->
  <polygon points="35,107 40,114 45,107 50,114 55,107 60,114 65,107 70,114 75,107 80,114 85,107 90,114 95,107 100,114 105,107 110,114 115,107 120,114 125,107 130,114 135,107 140,114 145,107 150,114 155,107 160,114 165,107 170,114 175,107 180,114 185,107 190,114 195,107 200,114 205,107 210,114 215,107" fill="{GRAY}" stroke="#4B5563" stroke-width="0.5"/>
  <text x="125" y="130" font-size="10" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Ножовка</text>

  <!-- Plane illustration -->
  <rect x="35" y="155" width="120" height="18" rx="3" fill="#8B7355" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <rect x="65" y="145" width="45" height="10" rx="2" fill="#A0845C" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <rect x="80" y="138" width="15" height="7" rx="1" fill="{GRAY}" stroke="#4B5563" stroke-width="1"/>
  <rect x="35" y="173" width="120" height="4" fill="#8B7355" stroke="{PRIMARY_DARK}" stroke-width="0.5"/>
  <rect x="75" y="177" width="35" height="2" fill="{GRAY}"/>
  <text x="95" y="195" font-size="10" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Рубанок</text>

  <!-- Chisel illustration -->
  <rect x="55" y="210" width="7" height="42" fill="{GRAY}" stroke="#4B5563" stroke-width="1"/>
  <rect x="46" y="252" width="25" height="7" rx="1" fill="#8B7355" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <polygon points="46,210 62,210 54,182" fill="{GRAY}" stroke="#4B5563" stroke-width="1"/>
  <text x="54" y="275" font-size="10" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Стамеска</text>

  <!-- Hammer illustration -->
  <rect x="130" y="210" width="6" height="45" fill="#8B7355" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <rect x="118" y="200" width="30" height="15" rx="2" fill="{GRAY}" stroke="#4B5563" stroke-width="1"/>
  <text x="133" y="275" font-size="10" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Киянка</text>

  <!-- Tools for sawing -->
  {info_box(310, 90, 470, 105, "Инструменты для пиления", [
      "Ножовка — продольное и поперечное пиление",
      "Лучковая пила — криволинейный распил",
      "Ножовка с обушком — точный тонкий распил",
      "Лобзик — фигурное выпиливание"
  ])}

  <!-- Tools for planing -->
  {info_box(310, 208, 470, 105, "Инструменты для строгания", [
      "Рубанок — черновое и чистовое строгание",
      "Шерхебель — грубое снятие материала",
      "Фуганок — выравнивание длинных деталей",
      "Цикля — окончательная зачистка поверхности"
  ])}

  <!-- Drilling tools -->
  {info_box(25, 295, 250, 105, "Сверление и долбление", [
      "Коловорот — ручное сверление",
      "Ручная дрель — быстрое сверление",
      "Сверло перьевое — отверстия в дереве",
      "Стамеска и долото — выборка гнёзд"
  ])}

  <!-- Measuring tools -->
  {info_box(290, 325, 250, 75, "Разметка и измерение", [
      "Угольник — проверка прямых углов",
      "Рейсмус — разметка толщины",
      "Линейка и рулетка — измерение",
      "Шаблон — контроль формы"
  ])}

  <!-- Auxiliary tools -->
  {info_box(555, 325, 225, 75, "Вспомогательные", [
      "Зажимы, струбцины",
      "Верстак с клиньями",
      "Наждачная бумага",
      "Киянка деревянная"
  ])}

  <!-- Safety rules -->
  {info_box(25, 415, 750, 90, "Техника безопасности при работе с деревом", [
      "Надёжно закрепляй заготовку в зажимах верстака перед обработкой!",
      "Не держи руку на линии реза — используй упор для нажима",
      "Работай только острым инструментом — тупой требует большего усилия и опаснее",
      "Опилки убирай щёткой, а не рукой — опасность занозы!"
  ], RED)}

  <!-- Operations sequence -->
  {highlight_box(25, 520, 750, 60, [
      "Последовательность обработки: разметка &#8594; закрепление &#8594; пиление &#8594; строгание &#8594; сверление &#8594; зачистка",
      "Правило мастера: измеряй дважды, режь один раз!"
  ])}
"""
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 3: Свойства металлов и сплавов
# ============================================================
def lesson_3():
    svg = svg_header()
    svg += header_bar(3, "Свойства металлов и сплавов", "Чёрные и цветные металлы, механические свойства")

    # Classification tree diagram (top)
    svg += f"""
  <!-- Classification tree: Metals -->
  <rect x="280" y="88" width="240" height="32" rx="6" fill="{PRIMARY_DARK}" filter="url(#shadow)"/>
  <text x="400" y="110" font-size="14" fill="{WHITE}" text-anchor="middle" font-weight="bold">Металлы и сплавы</text>

  <!-- Branches to subcategories -->
  <line x1="330" y1="120" x2="200" y2="148" stroke="{PRIMARY}" stroke-width="2"/>
  <line x1="470" y1="120" x2="600" y2="148" stroke="{PRIMARY}" stroke-width="2"/>

  <!-- Ferrous metals -->
  <rect x="80" y="148" width="240" height="28" rx="5" fill="{GRAY}" filter="url(#shadow)"/>
  <text x="200" y="167" font-size="13" fill="{WHITE}" text-anchor="middle" font-weight="bold">Чёрные металлы</text>

  <line x1="130" y1="176" x2="100" y2="192" stroke="{GRAY}" stroke-width="1.5"/>
  <line x1="200" y1="176" x2="200" y2="192" stroke="{GRAY}" stroke-width="1.5"/>
  <line x1="270" y1="176" x2="300" y2="192" stroke="{GRAY}" stroke-width="1.5"/>

  <rect x="30" y="192" width="120" height="22" rx="4" fill="#6B7280"/>
  <text x="90" y="208" font-size="10" fill="{WHITE}" text-anchor="middle">Чугун</text>
  <rect x="160" y="192" width="120" height="22" rx="4" fill="#4B5563"/>
  <text x="220" y="208" font-size="10" fill="{WHITE}" text-anchor="middle">Сталь</text>
  <rect x="290" y="192" width="60" height="22" rx="4" fill="#9CA3AF"/>
  <text x="320" y="208" font-size="9" fill="{WHITE}" text-anchor="middle">Феррит</text>

  <!-- Non-ferrous metals -->
  <rect x="480" y="148" width="240" height="28" rx="5" fill="{ACCENT}" filter="url(#shadow)"/>
  <text x="600" y="167" font-size="13" fill="{WHITE}" text-anchor="middle" font-weight="bold">Цветные металлы</text>

  <line x1="530" y1="176" x2="500" y2="192" stroke="{ACCENT}" stroke-width="1.5"/>
  <line x1="600" y1="176" x2="600" y2="192" stroke="{ACCENT}" stroke-width="1.5"/>
  <line x1="670" y1="176" x2="700" y2="192" stroke="{ACCENT}" stroke-width="1.5"/>

  <rect x="430" y="192" width="110" height="22" rx="4" fill="#D97706"/>
  <text x="485" y="208" font-size="10" fill="{WHITE}" text-anchor="middle">Медь</text>
  <rect x="550" y="192" width="110" height="22" rx="4" fill="#B45309"/>
  <text x="605" y="208" font-size="10" fill="{WHITE}" text-anchor="middle">Алюминий</text>
  <rect x="670" y="192" width="100" height="22" rx="4" fill="#92400E"/>
  <text x="720" y="208" font-size="10" fill="{WHITE}" text-anchor="middle">Цинк, Олово</text>

  <!-- Physical properties -->
  {info_box(25, 230, 250, 155, "Физические свойства", [
      "Плотность (кг/м&#179;):",
      "  Al=2700, Fe=7870, Cu=8960",
      "Температура плавления:",
      "  Al 660°C, Cu 1083°C",
      "  Fe 1538°C, Sn 232°C",
      "Электропроводность: Cu &gt; Al &gt; Fe",
      "Теплопроводность: Cu &gt; Al &gt; Fe"
  ])}

  <!-- Mechanical properties -->
  {info_box(290, 230, 250, 155, "Механические свойства", [
      "Прочность — сопротивление разрушению",
      "Пластичность — изменение формы",
      "Твёрдость — сопротивление вдавливанию",
      "Упругость — возврат формы",
      "Хрупкость — разрушение без деформации",
      "Вязкость — работа на разрушение",
      "Усталость — разрушение при циклах"
  ])}

  <!-- Alloys and applications -->
  {info_box(555, 230, 225, 155, "Сплавы и применение", [
      "Сталь — конструкции, инструменты",
      "Чугун — детали машин, трубы",
      "Бронза — подшипники, скульптуры",
      "Латунь — фурнитура, приборы",
      "Дюралюминий — авиация",
      "Припой — пайка деталей",
      "Нержавейка — посуда, медицина"
  ])}

  <!-- Highlight -->
  {highlight_box(25, 400, 750, 45, [
      "Сталь = железо + углерод (до 2%). Чем больше углерода — тем твёрже, но хрупче!",
      "Легирующие добавки (Cr, Ni, W) придают стали специальные свойства"
  ])}

  <!-- Steel types -->
  {info_box(25, 460, 370, 120, "Виды стали", [
      "Углеродистая: низко-, средне-, высокоуглеродистая",
      "Легированная: хромистая, никелевая, вольфрамовая",
      "Инструментальная: для резцов, свёрл, напильников",
      "Конструкционная: для деталей машин и сооружений",
      "Нержавеющая: стойкость к коррозии (Cr + Ni)"
  ])}

  <!-- Metal processing -->
  {info_box(410, 460, 370, 120, "Обработка металлов", [
      "Механическая: резание, гибка, штамповка, прокат",
      "Термическая: закалка, отпуск, отжиг, нормализация",
      "Термохимическая: цементация, азотирование",
      "Литейная: отливка в формы",
      "Деформационная: ковка, прессование, волочение"
  ])}

  <!-- Bottom decorative -->
  <rect x="25" y="590" width="750" height="3" rx="1" fill="{PRIMARY}" opacity="0.3"/>
"""
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 4: Приготовление блюд из яиц и теста
# ============================================================
def lesson_4():
    svg = svg_header()
    svg += header_bar(4, "Приготовление блюд из яиц и теста", "Рецепты, техники, правила гигиены")

    # Egg diagram (top-left)
    svg += f"""
  <!-- Egg cross-section -->
  <ellipse cx="120" cy="195" rx="45" ry="60" fill="#FFF8DC" stroke="{PRIMARY_DARK}" stroke-width="2" filter="url(#shadow)"/>
  <!-- Yolk -->
  <ellipse cx="120" cy="185" rx="20" ry="20" fill="#FCD34D" stroke="#D97706" stroke-width="1"/>
  <!-- White layers -->
  <ellipse cx="120" cy="185" rx="32" ry="42" fill="none" stroke="#E5C8A0" stroke-width="0.5" stroke-dasharray="3,2"/>
  <!-- Shell texture -->
  <ellipse cx="120" cy="195" rx="45" ry="60" fill="none" stroke="#C4A882" stroke-width="0.5"/>

  <!-- Egg labels -->
  <line x1="140" y1="165" x2="185" y2="145" stroke="{TEXT_DARK}" stroke-width="1"/>
  <text x="190" y="148" font-size="10" fill="{TEXT_DARK}" font-weight="bold">Скорлупа</text>
  <line x1="135" y1="185" x2="185" y2="185" stroke="{TEXT_DARK}" stroke-width="1"/>
  <text x="190" y="188" font-size="10" fill="{TEXT_DARK}" font-weight="bold">Желток</text>
  <line x1="140" y1="210" x2="185" y2="225" stroke="{TEXT_DARK}" stroke-width="1"/>
  <text x="190" y="228" font-size="10" fill="{TEXT_DARK}" font-weight="bold">Белок</text>

  <!-- Egg dishes -->
  {info_box(345, 90, 435, 110, "Блюда из яиц", [
      "Яйца всмятку — варка 2-3 минуты",
      "Яйца вкрутую — варка 8-10 минут",
      "Яичница-глазунья — жарка на сковороде",
      "Омлет — взбитые яйца с молоком, жарка"
  ], ACCENT)}

  <!-- Dough types -->
  {info_box(345, 215, 210, 115, "Виды теста", [
      "Пресное — мука, вода, соль",
      "Дрожжевое — мука, дрожжи, вода",
      "Слоёное — мука, масло, вода",
      "Бисквитное — мука, яйца, сахар",
      "Песочное — мука, масло, сахар"
  ])}

  <!-- Cooking steps for dough -->
  {info_box(570, 215, 210, 115, "Приготовление теста", [
      "1. Просеять муку горкой",
      "2. Добавить ингредиенты",
      "3. Замесить тесто",
      "4. Дать расстояться",
      "5. Формовать изделие"
  ])}

  <!-- Dough preparation process (visual flow) -->
  <rect x="25" y="285" width="130" height="28" rx="5" fill="{PRIMARY_DARK}" filter="url(#shadow)"/>
  <text x="90" y="304" font-size="10" fill="{WHITE}" text-anchor="middle" font-weight="bold">Просеивание</text>
  <line x1="155" y1="299" x2="170" y2="299" stroke="{PRIMARY}" stroke-width="2" marker-end="url(#arrow)"/>
  <rect x="170" y="285" width="130" height="28" rx="5" fill="{PRIMARY}" filter="url(#shadow)"/>
  <text x="235" y="304" font-size="10" fill="{WHITE}" text-anchor="middle" font-weight="bold">Замешивание</text>
  <line x1="300" y1="299" x2="315" y2="299" stroke="{PRIMARY}" stroke-width="2" marker-end="url(#arrow)"/>
  <rect x="315" y="285" width="130" height="28" rx="5" fill="{ACCENT}" filter="url(#shadow)"/>
  <text x="380" y="304" font-size="10" fill="{WHITE}" text-anchor="middle" font-weight="bold">Расстойка</text>
  <line x1="445" y1="299" x2="460" y2="299" stroke="{PRIMARY}" stroke-width="2" marker-end="url(#arrow)"/>
  <rect x="460" y="285" width="130" height="28" rx="5" fill="{PRIMARY_LIGHT}" filter="url(#shadow)"/>
  <text x="525" y="304" font-size="10" fill="{WHITE}" text-anchor="middle" font-weight="bold">Формовка</text>
  <line x1="590" y1="299" x2="605" y2="299" stroke="{PRIMARY}" stroke-width="2" marker-end="url(#arrow)"/>
  <rect x="605" y="285" width="170" height="28" rx="5" fill="{GREEN}" filter="url(#shadow)"/>
  <text x="690" y="304" font-size="10" fill="{WHITE}" text-anchor="middle" font-weight="bold">Выпекание/Варка</text>

  <!-- Recipes -->
  {info_box(25, 330, 375, 115, "Рецепт: Омлет натуральный", [
      "Ингредиенты: 2 яйца, 50 мл молока, соль, масло",
      "1. Разбить яйца в миску",
      "2. Добавить молоко и соль",
      "3. Взбить вилкой до однородности",
      "4. Вылить на разогретую сковороду"
  ])}

  {info_box(415, 330, 365, 115, "Рецепт: Блины на молоке", [
      "Ингредиенты: 2 яйца, 500 мл молока, 200 г муки",
      "1. Взбить яйца с сахаром и солью",
      "2. Добавить молоко и муку, размешать",
      "3. Добавить масло в тесто",
      "4. Жарить на раскалённой сковороде"
  ])}

  <!-- Hygiene rules -->
  {info_box(25, 460, 375, 115, "Правила гигиены на кухне", [
      "Мой руки перед приготовлением пищи!",
      "Используй чистую посуду и разделочные доски",
      "Яйца перед варкой мойте тёплой водой",
      "Мясные и овощные доски — раздельно!",
      "Готовую пищу храни в холодильнике"
  ], GREEN)}

  {info_box(415, 460, 365, 115, "Техника безопасности", [
      "Осторожно обращайся с острыми предметами",
      "Горячую посуду бери прихваткой",
      "Не лей воду в раскалённое масло!",
      "Следи за огнём и включёнными конфорками",
      "Не оставляй плиту без присмотра"
  ], RED)}

  <!-- Bottom highlight -->
  {highlight_box(25, 588, 750, 0, [])}
"""
    # Remove the empty highlight box at bottom, add proper footer line
    svg = svg.replace(
        f'  <rect x="25" y="588" width="750" height="0" rx="6" fill="{HIGHLIGHT_BG}" stroke="{ACCENT}" stroke-width="2" stroke-dasharray="6,3" filter="url(#shadow)"/>\n',
        "",
    )
    svg += f"""
  <!-- Bottom decorative line -->
  <rect x="25" y="590" width="750" height="3" rx="1" fill="{PRIMARY}" opacity="0.3"/>
"""
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 5: Этапы проекта
# ============================================================
def lesson_5():
    svg = svg_header()
    svg += header_bar(5, "Этапы проекта", "От замысла до оценки результата")

    # Main flow: project stages as horizontal arrows
    stages = [
        ("Замысел", PRIMARY_DARK),
        ("Исследование", PRIMARY),
        ("Проектирование", ACCENT),
        ("Изготовление", PRIMARY_LIGHT),
        ("Оценка", GREEN),
    ]
    sx = 30
    for i, (stage, color) in enumerate(stages):
        svg += stage_arrow(sx + i * 152, 90, 145, 38, stage, color)

    # Detailed stages description
    svg += f"""
  <!-- Stage 1: Problem definition -->
  {info_box(25, 148, 240, 130, "1. Определение проблемы", [
      "Выявить потребность или проблему",
      "Сформулировать цель проекта",
      "Определить задачи и ограничения",
      "Выбрать объект проектирования",
      "Обозначить критерии оценки"
  ], PRIMARY_DARK)}

  <!-- Stage 2: Research -->
  {info_box(280, 148, 240, 130, "2. Исследование", [
      "Сбор информации об объекте",
      "Изучение аналогов и прототипов",
      "Анализ материалов и технологий",
      "Определение ресурсов и сроков",
      "Формирование банка идей"
  ], PRIMARY)}

  <!-- Stage 3: Design -->
  {info_box(535, 148, 245, 130, "3. Проектирование", [
      "Разработка вариантов решения",
      "Выбор оптимального варианта",
      "Создание эскиза и чертежа",
      "Составление тех. карты",
      "Планирование последовательности"
  ], ACCENT)}

  <!-- Stage 4: Production -->
  {info_box(25, 295, 375, 130, "4. Изготовление изделия", [
      "Подготовка материалов и инструментов",
      "Выполнение технологических операций",
      "Соблюдение техники безопасности",
      "Пооперационный контроль качества",
      "Сборка и отделка изделия"
  ], PRIMARY_LIGHT)}

  <!-- Stage 5: Evaluation -->
  {info_box(415, 295, 365, 130, "5. Оценка и защита", [
      "Проверка соответствия критериям",
      "Тестирование изделия в работе",
      "Экономическая оценка проекта",
      "Экологическая экспертиза",
      "Презентация и защита проекта"
  ], GREEN)}

  <!-- Project documents -->
  {info_box(25, 445, 375, 120, "Документы проекта", [
      "Паспорт проекта: тема, цель, задачи, сроки",
      "Техническое задание: требования к изделию",
      "Технологическая карта: последовательность",
      "Эскиз и чертёж: графическое представление",
      "Самооценка: анализ результатов и выводы"
  ])}

  <!-- Key principles -->
  {info_box(415, 445, 365, 120, "Принципы проектирования", [
      "Системность — целостный подход к проекту",
      "Ресурсоёмкость — учёт материалов и времени",
      "Безопасность — соблюдение правил ТБ",
      "Экологичность — минимальный вред природе",
      "Эстетичность — красота и эргономика"
  ])}

  <!-- Bottom highlight -->
  {highlight_box(25, 580, 750, 0, [])}
"""
    # Remove empty highlight box
    svg = svg.replace(
        f'  <rect x="25" y="580" width="750" height="0" rx="6" fill="{HIGHLIGHT_BG}" stroke="{ACCENT}" stroke-width="2" stroke-dasharray="6,3" filter="url(#shadow)"/>\n',
        "",
    )
    svg += f"""
  <!-- Bottom highlight -->
  {highlight_box(25, 578, 750, 16, [
      "Проект начинается с проблемы, а заканчивается результатом и его оценкой!"
  ])}
"""
    svg += svg_footer()
    return svg


# ============================================================
# Main: generate all SVGs and validate
# ============================================================
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    lessons = [
        (1, lesson_1),
        (2, lesson_2),
        (3, lesson_3),
        (4, lesson_4),
        (5, lesson_5),
    ]

    results = []
    for num, func in lessons:
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
        svg_content = func()

        # Validate XML
        try:
            ET.fromstring(svg_content)
            valid = True
            error_msg = None
        except ET.ParseError as e:
            valid = False
            error_msg = str(e)

        # Write file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)

        file_size = os.path.getsize(filepath)
        status = "OK" if valid else f"XML ERROR: {error_msg}"
        results.append((filepath, file_size, status))
        print(f"Lesson {num}: {filepath} ({file_size} bytes) — {status}")

    print("\n" + "=" * 60)
    print("GENERATION SUMMARY")
    print("=" * 60)
    all_ok = True
    for filepath, size, status in results:
        icon = "✅" if status == "OK" else "❌"
        print(f"  {icon} {filepath} ({size} bytes) — {status}")
        if status != "OK":
            all_ok = False

    if all_ok:
        print("\nAll 5 SVG files generated and validated successfully!")
    else:
        print("\nSome SVG files have validation errors!")

    return all_ok


if __name__ == "__main__":
    main()
