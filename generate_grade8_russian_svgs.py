#!/usr/bin/env python3
"""Generate Grade 8 Russian Language lesson SVG images."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/russian"

# Color scheme - Rose/Pink
PRIMARY = "#EC4899"
PRIMARY_LIGHT = "#F9A8D4"
PRIMARY_DARK = "#BE185D"
ACCENT = "#FDF2F8"
ACCENT2 = "#FCE7F3"
WHITE = "#FFFFFF"
BLACK = "#1F2937"
GRAY = "#6B7280"
GRAY_LIGHT = "#E5E7EB"
DARK_BG = "#831843"
MID_BG = "#9D174D"
SOFT_PINK = "#FBCFE8"
CORAL = "#FB7185"
PURPLE = "#A855F7"
BLUE = "#3B82F6"
GREEN = "#10B981"
ORANGE = "#F59E0B"
TEAL = "#14B8A6"


def escape_xml(text):
    """Escape special XML characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def svg_header():
    """Return standard SVG header string."""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600">
'''


def svg_footer():
    """Return standard SVG footer."""
    return '</svg>\n'


def add_background(svg_content):
    """Add gradient background to SVG."""
    return svg_content + f'''
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{ACCENT};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{ACCENT2};stop-opacity:1"/>
    </linearGradient>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:{PRIMARY};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{PRIMARY_DARK};stop-opacity:1"/>
    </linearGradient>
    <linearGradient id="boxGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:{WHITE};stop-opacity:0.95"/>
      <stop offset="100%" style="stop-color:{SOFT_PINK};stop-opacity:0.9"/>
    </linearGradient>
    <filter id="shadow" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="{PRIMARY_DARK}" flood-opacity="0.15"/>
    </filter>
    <filter id="shadowSmall" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="0" dy="1" stdDeviation="1" flood-color="{BLACK}" flood-opacity="0.1"/>
    </filter>
  </defs>
  <rect width="800" height="600" fill="url(#bgGrad)" rx="0"/>
'''


def add_title_bar(svg, title, subtitle=""):
    """Add a title bar at the top of the SVG."""
    svg += f'''
  <!-- Title Bar -->
  <rect x="0" y="0" width="800" height="70" fill="url(#headerGrad)" rx="0"/>
  <rect x="0" y="65" width="800" height="5" fill="{PRIMARY_DARK}" opacity="0.3"/>
  <text x="400" y="38" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="{WHITE}" text-anchor="middle">{escape_xml(title)}</text>
'''
    if subtitle:
        svg += f'  <text x="400" y="58" font-family="Arial, sans-serif" font-size="13" fill="{PRIMARY_LIGHT}" text-anchor="middle">{escape_xml(subtitle)}</text>\n'
    return svg


def add_lesson_badge(svg, number):
    """Add lesson number badge."""
    svg += f'''
  <circle cx="40" cy="35" r="22" fill="{WHITE}" opacity="0.25"/>
  <text x="40" y="41" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="{WHITE}" text-anchor="middle">{number}</text>
'''
    return svg


def add_content_box(svg, x, y, w, h, title="", fill="url(#boxGrad)", stroke=PRIMARY):
    """Add a content box with optional title."""
    svg += f'''
  <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" rx="8" stroke="{stroke}" stroke-width="1.5" filter="url(#shadow)"/>
'''
    if title:
        svg += f'  <text x="{x + w/2}" y="{y + 18}" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="{PRIMARY_DARK}" text-anchor="middle">{escape_xml(title)}</text>\n'
    return svg


def add_rule_box(svg, x, y, w, h, title, rules):
    """Add a highlighted rule box."""
    svg += f'''
  <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{WHITE}" rx="6" stroke="{CORAL}" stroke-width="2" filter="url(#shadowSmall)"/>
  <rect x="{x}" y="{y}" width="{w}" height="22" fill="{CORAL}" rx="6"/>
  <rect x="{x}" y="{y + 16}" width="{w}" height="6" fill="{CORAL}"/>
  <text x="{x + w/2}" y="{y + 15}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{WHITE}" text-anchor="middle">{escape_xml(title)}</text>
'''
    for i, rule in enumerate(rules):
        svg += f'  <text x="{x + 8}" y="{y + 38 + i * 16}" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">{escape_xml(rule)}</text>\n'
    return svg


def add_colored_word(svg, x, y, word, color, font_size=13, bold=True):
    """Add a colored word/phrase."""
    weight = "bold" if bold else "normal"
    svg += f'  <text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{font_size}" font-weight="{weight}" fill="{color}">{escape_xml(word)}</text>\n'
    return svg


def add_connector_arrow(svg, x1, y1, x2, y2, color=PRIMARY):
    """Add a connector arrow between two points."""
    svg += f'''
  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.5" marker-end="url(#arrowhead)"/>
'''
    return svg


def add_arrow_def(svg):
    """Add arrowhead marker definition."""
    svg += '''
  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="''' + PRIMARY + '''"/>
    </marker>
  </defs>
'''
    return svg


# ============================================================
# LESSON 1: Синтаксис простого предложения
# ============================================================
def generate_lesson1():
    svg = svg_header()
    svg = add_background(svg)
    svg = add_arrow_def(svg)
    svg = add_title_bar(svg, "Синтаксис простого предложения", "Строение предложения: подлежащее и сказуемое")
    svg = add_lesson_badge(svg, 1)

    # Types of sentences by purpose
    svg = add_content_box(svg, 15, 82, 240, 165, "Виды предложений по цели высказывания")
    types = [
        ("Повествовательное", "Сообщает о чём-либо", GREEN),
        ("Вопросительное", "Содержит вопрос", BLUE),
        ("Побудительное", "Побуждает к действию", ORANGE),
    ]
    for i, (t, desc, color) in enumerate(types):
        by = 106 + i * 46
        svg += f'  <rect x="25" y="{by}" width="220" height="38" fill="{WHITE}" rx="5" stroke="{color}" stroke-width="1.5"/>\n'
        svg += f'  <circle cx="42" cy="{by + 14}" r="6" fill="{color}"/>\n'
        svg += f'  <text x="55" y="{by + 18}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{color}">{escape_xml(t)}</text>\n'
        svg += f'  <text x="55" y="{by + 31}" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}">{escape_xml(desc)}</text>\n'

    # Types by intonation
    svg = add_content_box(svg, 270, 82, 240, 165, "Виды по интонации")
    svg += f'''
  <rect x="280" y="104" width="105" height="55" fill="{WHITE}" rx="5" stroke="{GREEN}" stroke-width="1.5"/>
  <text x="332" y="126" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{GREEN}" text-anchor="middle">Невосклиц.</text>
  <text x="332" y="146" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}" text-anchor="middle">Спокойная речь</text>
  <rect x="395" y="104" width="105" height="55" fill="{WHITE}" rx="5" stroke="{CORAL}" stroke-width="1.5"/>
  <text x="447" y="126" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{CORAL}" text-anchor="middle">Восклицат.</text>
  <text x="447" y="146" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}" text-anchor="middle">Эмоциональная!</text>
  <text x="390" y="180" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}" text-anchor="middle">Примеры:</text>
  <text x="390" y="194" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}">Мальчик читает книгу.</text>
  <text x="390" y="208" font-family="Arial, sans-serif" font-size="9" fill="{CORAL}">Какой прекрасный день!</text>
  <text x="390" y="222" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}">Ты пойдёшь в кино?</text>
  <text x="390" y="236" font-family="Arial, sans-serif" font-size="9" fill="{CORAL}">Иди сюда скорее!</text>
'''

    # Grammar basis diagram
    svg = add_content_box(svg, 525, 82, 260, 165, "Грамматическая основа предложения")
    svg += f'''
  <rect x="545" y="108" width="220" height="40" fill="{WHITE}" rx="5" stroke="{PRIMARY}" stroke-width="2"/>
  <text x="655" y="133" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{PRIMARY_DARK}" text-anchor="middle">Грамматическая основа</text>
  <line x1="580" y1="148" x2="580" y2="162" stroke="{PRIMARY}" stroke-width="1.5"/>
  <line x1="730" y1="148" x2="730" y2="162" stroke="{PRIMARY}" stroke-width="1.5"/>
  <rect x="545" y="162" width="100" height="35" fill="{GREEN}" rx="5" opacity="0.15" stroke="{GREEN}" stroke-width="1.5"/>
  <text x="595" y="184" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="{GREEN}" text-anchor="middle">Подлежащее</text>
  <rect x="665" y="162" width="100" height="35" fill="{BLUE}" rx="5" opacity="0.15" stroke="{BLUE}" stroke-width="1.5"/>
  <text x="715" y="184" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="{BLUE}" text-anchor="middle">Сказуемое</text>
  <text x="555" y="215" font-family="Arial, sans-serif" font-size="9" fill="{GREEN}">Кто? Что?</text>
  <text x="675" y="215" font-family="Arial, sans-serif" font-size="9" fill="{BLUE}">Что делает? Что сделает?</text>
  <text x="555" y="230" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}">Именительный падеж</text>
  <text x="675" y="230" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}">Глагол / сущ. / прил.</text>
'''

    # Example sentence diagram
    svg = add_content_box(svg, 15, 260, 490, 150, "Разбор предложения: схема")
    svg += f'''
  <text x="30" y="284" font-family="Arial, sans-serif" font-size="12" fill="{GRAY}">Пример:</text>
  <text x="90" y="284" font-family="Arial, sans-serif" font-size="13">
    <tspan fill="{GREEN}" font-weight="bold">Ветер</tspan>
    <tspan fill="{BLACK}"> </tspan>
    <tspan fill="{BLUE}" font-weight="bold">гнал</tspan>
    <tspan fill="{BLACK}"> </tspan>
    <tspan fill="{PURPLE}">по небу</tspan>
    <tspan fill="{BLACK}"> </tspan>
    <tspan fill="{ORANGE}">тяжёлые</tspan>
    <tspan fill="{BLACK}"> </tspan>
    <tspan fill="{TEAL}">тучи</tspan>
    <tspan fill="{BLACK}">.</tspan>
  </text>
  <!-- Schema line -->
  <line x1="30" y1="296" x2="490" y2="296" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <text x="30" y="312" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{BLACK}">Схема:</text>
  <rect x="30" y="320" width="60" height="24" fill="{GREEN}" rx="4" opacity="0.2"/>
  <text x="60" y="337" font-family="Arial, sans-serif" font-size="10" fill="{GREEN}" text-anchor="middle" font-weight="bold">Ветер</text>
  <text x="97" y="337" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">—</text>
  <rect x="105" y="320" width="45" height="24" fill="{BLUE}" rx="4" opacity="0.2"/>
  <text x="127" y="337" font-family="Arial, sans-serif" font-size="10" fill="{BLUE}" text-anchor="middle" font-weight="bold">гнал</text>
  <rect x="160" y="320" width="80" height="24" fill="{ORANGE}" rx="4" opacity="0.15"/>
  <text x="200" y="337" font-family="Arial, sans-serif" font-size="10" fill="{ORANGE}" text-anchor="middle" font-weight="bold">тяжёлые</text>
  <rect x="250" y="320" width="55" height="24" fill="{TEAL}" rx="4" opacity="0.15"/>
  <text x="277" y="337" font-family="Arial, sans-serif" font-size="10" fill="{TEAL}" text-anchor="middle" font-weight="bold">тучи</text>
  <rect x="315" y="320" width="80" height="24" fill="{PURPLE}" rx="4" opacity="0.15"/>
  <text x="355" y="337" font-family="Arial, sans-serif" font-size="10" fill="{PURPLE}" text-anchor="middle" font-weight="bold">по небу</text>
  <!-- Under-sentence analysis -->
  <text x="30" y="370" font-family="Arial, sans-serif" font-size="10" fill="{GREEN}">подлежащее</text>
  <text x="105" y="370" font-family="Arial, sans-serif" font-size="10" fill="{BLUE}">сказуемое</text>
  <text x="160" y="370" font-family="Arial, sans-serif" font-size="10" fill="{ORANGE}">определение</text>
  <text x="250" y="370" font-family="Arial, sans-serif" font-size="10" fill="{TEAL}">дополнение</text>
  <text x="315" y="370" font-family="Arial, sans-serif" font-size="10" fill="{PURPLE}">обстоятельство</text>
  <text x="30" y="395" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">[_ = - ~ _]</text>
'''

    # Punctuation rule box
    svg = add_rule_box(svg, 520, 260, 265, 150, "Правила пунктуации", [
        "1. Подлежащее и сказуемое",
        "   разделяются тире, если оба",
        "   выражены существительными",
        "   в им. падеже:",
        "   Москва — столица России.",
        "2. Запятая ставится перед",
        "   союзами а, но, да (=но).",
    ])

    # Simple sentence types
    svg = add_content_box(svg, 15, 425, 380, 160, "Типы простых предложений")
    svg += f'''
  <rect x="25" y="448" width="170" height="55" fill="{WHITE}" rx="5" stroke="{GREEN}" stroke-width="1.5"/>
  <text x="110" y="468" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{GREEN}" text-anchor="middle">Двусоставные</text>
  <text x="110" y="484" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}" text-anchor="middle">Подлежащее + Сказуемое</text>
  <text x="110" y="497" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}" text-anchor="middle">Солнце светит.</text>
  <rect x="205" y="448" width="175" height="55" fill="{WHITE}" rx="5" stroke="{BLUE}" stroke-width="1.5"/>
  <text x="292" y="468" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{BLUE}" text-anchor="middle">Односоставные</text>
  <text x="292" y="484" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}" text-anchor="middle">Только один главный член</text>
  <text x="292" y="497" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}" text-anchor="middle">Светает. Мне холодно.</text>
  <!-- One-component types -->
  <text x="25" y="520" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{BLUE}">Виды односоставных:</text>
  <text x="25" y="534" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}">Определённо-личные: Люблю грозу в начале мая.</text>
  <text x="25" y="548" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}">Неопределённо-личные: В дверь постучали.</text>
  <text x="25" y="562" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}">Безличные: Уже стемнело. Мне весело.</text>
  <text x="25" y="576" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}">Назывные: Зима. Мороз. Тишина.</text>
'''

    # Complete/incomplete sentences
    svg = add_content_box(svg, 410, 425, 375, 160, "Распространённые / Нераспространённые")
    svg += f'''
  <rect x="420" y="450" width="175" height="58" fill="{WHITE}" rx="5" stroke="{PURPLE}" stroke-width="1.5"/>
  <text x="507" y="470" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PURPLE}" text-anchor="middle">Нераспространённое</text>
  <text x="507" y="486" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}" text-anchor="middle">Только грамм. основа</text>
  <text x="507" y="500" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}" text-anchor="middle">Ночь наступила.</text>
  <rect x="605" y="450" width="170" height="58" fill="{WHITE}" rx="5" stroke="{ORANGE}" stroke-width="1.5"/>
  <text x="690" y="470" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{ORANGE}" text-anchor="middle">Распространённое</text>
  <text x="690" y="486" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}" text-anchor="middle">Есть второстеп. члены</text>
  <text x="690" y="500" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}" text-anchor="middle">Тёмная ночь быстро наступила.</text>
  <!-- Visual comparison -->
  <text x="420" y="525" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY_DARK}">Сравнение:</text>
  <rect x="420" y="533" width="50" height="18" fill="{GREEN}" rx="3" opacity="0.2"/>
  <rect x="475" y="533" width="50" height="18" fill="{BLUE}" rx="3" opacity="0.2"/>
  <text x="530" y="546" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}">= нераспространённое</text>
  <rect x="420" y="556" width="50" height="18" fill="{GREEN}" rx="3" opacity="0.2"/>
  <rect x="475" y="556" width="50" height="18" fill="{BLUE}" rx="3" opacity="0.2"/>
  <rect x="530" y="556" width="40" height="18" fill="{ORANGE}" rx="3" opacity="0.15"/>
  <rect x="575" y="556" width="40" height="18" fill="{TEAL}" rx="3" opacity="0.15"/>
  <rect x="620" y="556" width="50" height="18" fill="{PURPLE}" rx="3" opacity="0.15"/>
  <text x="675" y="569" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}">= распространённое</text>
'''

    svg += svg_footer()
    return svg


# ============================================================
# LESSON 2: Главные и второстепенные члены предложения
# ============================================================
def generate_lesson2():
    svg = svg_header()
    svg = add_background(svg)
    svg = add_arrow_def(svg)
    svg = add_title_bar(svg, "Главные и второстепенные члены предложения", "Подлежащее, сказуемое, дополнение, обстоятельство, определение")
    svg = add_lesson_badge(svg, 2)

    # Main members box
    svg = add_content_box(svg, 15, 82, 370, 175, "Главные члены предложения")
    svg += f'''
  <rect x="25" y="106" width="170" height="72" fill="{WHITE}" rx="5" stroke="{GREEN}" stroke-width="2"/>
  <text x="110" y="125" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{GREEN}" text-anchor="middle">ПОДЛЕЖАЩЕЕ</text>
  <text x="110" y="143" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}" text-anchor="middle">Кто? Что?</text>
  <text x="110" y="158" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}" text-anchor="middle">Сущ. в им. п., мест.</text>
  <text x="110" y="171" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}" text-anchor="middle">числ., инфинитив</text>
  <rect x="205" y="106" width="170" height="72" fill="{WHITE}" rx="5" stroke="{BLUE}" stroke-width="2"/>
  <text x="290" y="125" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{BLUE}" text-anchor="middle">СКАЗУЕМОЕ</text>
  <text x="290" y="143" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}" text-anchor="middle">Что делает? Что сделает?</text>
  <text x="290" y="158" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}" text-anchor="middle">Глагол, сущ., прил.,</text>
  <text x="290" y="171" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}" text-anchor="middle">кратк. прил., причастие</text>
  <!-- Types of predicate -->
  <text x="25" y="198" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{BLUE}">Виды сказуемых:</text>
  <rect x="25" y="206" width="110" height="22" fill="{BLUE}" rx="3" opacity="0.12"/>
  <text x="80" y="221" font-family="Arial, sans-serif" font-size="9" fill="{BLUE}" text-anchor="middle">Простое глагольное</text>
  <rect x="140" y="206" width="110" height="22" fill="{PURPLE}" rx="3" opacity="0.12"/>
  <text x="195" y="221" font-family="Arial, sans-serif" font-size="9" fill="{PURPLE}" text-anchor="middle">Составное глагольное</text>
  <rect x="255" y="206" width="120" height="22" fill="{ORANGE}" rx="3" opacity="0.12"/>
  <text x="315" y="221" font-family="Arial, sans-serif" font-size="9" fill="{ORANGE}" text-anchor="middle">Составное именное</text>
  <text x="25" y="244" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}">Читаю | Начал читать | Был учителем</text>
'''

    # Secondary members box
    svg = add_content_box(svg, 400, 82, 385, 175, "Второстепенные члены предложения")
    members = [
        ("Дополнение", "Кого? Чего? Кому? и др.", "Сущ., мест. в косв. п.", TEAL, 108),
        ("Определение", "Какой? Чей? Каков?", "Прил., причастие, сущ.", ORANGE, 156),
        ("Обстоятельство", "Где? Куда? Когда? Как?", "Наречие, сущ. в косв. п.", PURPLE, 204),
    ]
    for name, questions, forms, color, by in members:
        svg += f'''
  <rect x="410" y="{by}" width="365" height="42" fill="{WHITE}" rx="5" stroke="{color}" stroke-width="1.5"/>
  <circle cx="430" cy="{by + 21}" r="10" fill="{color}" opacity="0.2"/>
  <text x="430" y="{by + 25}" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{color}" text-anchor="middle">{name[0]}</text>
  <text x="450" y="{by + 16}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{color}">{name}</text>
  <text x="450" y="{by + 31}" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}">{questions} | {forms}</text>
'''

    # Example sentence with full analysis
    svg = add_content_box(svg, 15, 270, 770, 140, "Полный разбор предложения")
    svg += f'''
  <text x="30" y="296" font-family="Arial, sans-serif" font-size="12" fill="{GRAY}">Пример:</text>
  <text x="30" y="316" font-family="Arial, sans-serif" font-size="14">
    <tspan fill="{GREEN}" font-weight="bold">Старик</tspan>
    <tspan fill="{BLACK}"> </tspan>
    <tspan fill="{BLUE}" font-weight="bold">ловил</tspan>
    <tspan fill="{BLACK}"> </tspan>
    <tspan fill="{ORANGE}" font-weight="bold">рыбу</tspan>
    <tspan fill="{BLACK}"> </tspan>
    <tspan fill="{PURPLE}">в пустынном море</tspan>
    <tspan fill="{BLACK}">.</tspan>
  </text>
  <!-- Word-by-word analysis -->
  <line x1="30" y1="328" x2="770" y2="328" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <text x="30" y="348" font-family="Arial, sans-serif" font-size="10" fill="{GREEN}" font-weight="bold">Старик</text>
  <text x="90" y="348" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">— подлежащее (сущ., им. п.)</text>
  <text x="30" y="365" font-family="Arial, sans-serif" font-size="10" fill="{BLUE}" font-weight="bold">ловил</text>
  <text x="90" y="365" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">— сказуемое (глагол, прош. вр.)</text>
  <text x="30" y="382" font-family="Arial, sans-serif" font-size="10" fill="{ORANGE}" font-weight="bold">рыбу</text>
  <text x="90" y="382" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">— дополнение (сущ., В. п., прямое)</text>
  <text x="400" y="348" font-family="Arial, sans-serif" font-size="10" fill="{PURPLE}" font-weight="bold">в море</text>
  <text x="470" y="348" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">— обстоятельство места (сущ., П. п.)</text>
  <text x="400" y="365" font-family="Arial, sans-serif" font-size="10" fill="{PURPLE}" font-weight="bold">пустынном</text>
  <text x="490" y="365" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">— определение (прил., П. п.)</text>
  <text x="400" y="385" font-family="Arial, sans-serif" font-size="10" fill="{PRIMARY_DARK}" font-weight="bold">Схема:</text>
  <text x="470" y="385" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">[= - ~ _]</text>
'''

    # Tree diagram
    svg = add_content_box(svg, 15, 425, 380, 160, "Схема связей в предложении")
    svg += f'''
  <text x="200" y="448" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY_DARK}" text-anchor="middle">Старик ловил рыбу</text>
  <!-- Tree structure -->
  <rect x="140" y="456" width="55" height="20" fill="{GREEN}" rx="3" opacity="0.2"/>
  <text x="167" y="470" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{GREEN}" text-anchor="middle">Старик</text>
  <rect x="210" y="456" width="45" height="20" fill="{BLUE}" rx="3" opacity="0.2"/>
  <text x="232" y="470" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{BLUE}" text-anchor="middle">ловил</text>
  <rect x="270" y="456" width="45" height="20" fill="{TEAL}" rx="3" opacity="0.15"/>
  <text x="292" y="470" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{TEAL}" text-anchor="middle">рыбу</text>
  <!-- Connection lines -->
  <line x1="167" y1="476" x2="232" y2="476" stroke="{PRIMARY}" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="232" y1="476" x2="292" y2="476" stroke="{PRIMARY}" stroke-width="1" stroke-dasharray="3,2"/>
  <!-- Labels below -->
  <text x="167" y="494" font-family="Arial, sans-serif" font-size="8" fill="{GREEN}" text-anchor="middle">подлеж.</text>
  <text x="232" y="494" font-family="Arial, sans-serif" font-size="8" fill="{BLUE}" text-anchor="middle">сказ.</text>
  <text x="292" y="494" font-family="Arial, sans-serif" font-size="8" fill="{TEAL}" text-anchor="middle">дополн.</text>
  <!-- Question arrows -->
  <text x="195" y="490" font-family="Arial, sans-serif" font-size="7" fill="{GRAY}">кто?</text>
  <text x="255" y="490" font-family="Arial, sans-serif" font-size="7" fill="{GRAY}">что?</text>
  <!-- Extended tree -->
  <line x1="292" y1="476" x2="292" y2="510" stroke="{PURPLE}" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="292" y1="510" x2="200" y2="530" stroke="{PURPLE}" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="292" y1="510" x2="380" y2="530" stroke="{PURPLE}" stroke-width="1" stroke-dasharray="3,2"/>
  <rect x="155" y="528" width="90" height="18" fill="{ORANGE}" rx="3" opacity="0.15"/>
  <text x="200" y="541" font-family="Arial, sans-serif" font-size="8" fill="{ORANGE}" text-anchor="middle">пустынном (опред.)</text>
  <rect x="340" y="528" width="80" height="18" fill="{PURPLE}" rx="3" opacity="0.15"/>
  <text x="380" y="541" font-family="Arial, sans-serif" font-size="8" fill="{PURPLE}" text-anchor="middle">в море (обст.)</text>
  <text x="25" y="565" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}">Вопросы от сказуемого к второстепенным</text>
  <text x="25" y="578" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}">и от определяемого слова к определению</text>
'''

    # Rule box
    svg = add_rule_box(svg, 410, 425, 375, 160, "Правило: Тире между подл. и сказ.", [
        "Тире ставится, если оба главных",
        "члена выражены одной формой:",
        "",
        "  Сущ. в им. п. — Сущ. в им. п.",
        "  Москва — столица России.",
        "",
        "  Числ. — Числ.",
        "  Дважды два — четыре.",
        "",
        "  Инфинитив — Инфинитив",
        "  Жить — Родине служить.",
    ])

    svg += svg_footer()
    return svg


# ============================================================
# LESSON 3: Однородные члены предложения
# ============================================================
def generate_lesson3():
    svg = svg_header()
    svg = add_background(svg)
    svg = add_title_bar(svg, "Однородные члены предложения", "Союзы и знаки препинания при однородных членах")
    svg = add_lesson_badge(svg, 3)

    # Definition box
    svg = add_content_box(svg, 15, 82, 380, 95, "Определение")
    svg += f'''
  <text x="30" y="106" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">Однородные члены — это члены</text>
  <text x="30" y="122" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">предложения, которые:</text>
  <text x="30" y="142" font-family="Arial, sans-serif" font-size="11" fill="{GREEN}" font-weight="bold">1. Отвечают на один вопрос</text>
  <text x="30" y="158" font-family="Arial, sans-serif" font-size="11" fill="{BLUE}" font-weight="bold">2. Являются одним и тем же членом предл.</text>
  <text x="30" y="174" font-family="Arial, sans-serif" font-size="11" fill="{PURPLE}" font-weight="bold">3. Связаны сочинительной связью</text>
'''

    # Conjunctions box
    svg = add_content_box(svg, 410, 82, 375, 95, "Союзы при однородных членах")
    svg += f'''
  <rect x="420" y="106" width="170" height="28" fill="{GREEN}" rx="4" opacity="0.15"/>
  <text x="505" y="124" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{GREEN}" text-anchor="middle">Соединительные: и, да(=и), ни...ни</text>
  <rect x="420" y="138" width="170" height="28" fill="{ORANGE}" rx="4" opacity="0.15"/>
  <text x="505" y="156" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{ORANGE}" text-anchor="middle">Противительные: а, но, да(=но), однако</text>
  <rect x="600" y="106" width="175" height="28" fill="{BLUE}" rx="4" opacity="0.15"/>
  <text x="687" y="124" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{BLUE}" text-anchor="middle">Разделительные: или, либо, то...то</text>
  <rect x="600" y="138" width="175" height="28" fill="{PURPLE}" rx="4" opacity="0.15"/>
  <text x="687" y="156" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PURPLE}" text-anchor="middle">Пояснительные: то есть, а именно</text>
'''

    # Punctuation rules
    svg = add_rule_box(svg, 15, 190, 380, 200, "Знаки препинания при однородных членах", [
        "БЕЗ союза — запятая:",
        "  Ветер, дождь, снег бушевали.",
        "",
        "Союз И (одиночный) — БЕЗ запятой:",
        "  Ветер и дождь бушевали.",
        "",
        "Союз И (повторяющийся) — запятая:",
        "  И ветер, и дождь бушевали.",
        "",
        "Союз А, НО — запятая:",
        "  Не ветер, а дождь бушевал.",
        "",
        "Парные союзы — запятая + запятая:",
        "  Как ветер, так и дождь бушевали.",
    ])

    # Examples
    svg = add_content_box(svg, 410, 190, 375, 200, "Примеры")
    examples = [
        ("В саду росли", "яблони, груши, вишни", "и сливы", TEAL),
        ("Он читал", "и думал, и мечтал", "", BLUE),
        ("Не рыба, а мясо", "было на столе", "", ORANGE),
        ("Мы были", "и рады, и удивлены", "одновременно", PURPLE),
    ]
    for i, (start, mid, end, color) in enumerate(examples):
        by = 216 + i * 42
        svg += f'  <rect x="420" y="{by}" width="355" height="34" fill="{WHITE}" rx="4" stroke="{color}" stroke-width="1"/>\n'
        svg += f'  <text x="430" y="{by + 21}" font-family="Arial, sans-serif" font-size="10">{escape_xml(start)} <tspan fill="{color}" font-weight="bold">{escape_xml(mid)}</tspan> {escape_xml(end)}</text>\n'

    # Diagram: sentence structure
    svg = add_content_box(svg, 15, 405, 380, 180, "Схема предложения с однородными")
    svg += f'''
  <text x="30" y="430" font-family="Arial, sans-serif" font-size="12" fill="{BLACK}">
    <tspan fill="{GREEN}" font-weight="bold">Мальчик</tspan>
    <tspan fill="{BLACK}"> </tspan>
    <tspan fill="{BLUE}" font-weight="bold">читал</tspan>
    <tspan fill="{BLACK}"> </tspan>
    <tspan fill="{ORANGE}" font-weight="bold">книги, журналы</tspan>
    <tspan fill="{BLACK}"> </tspan>
    <tspan fill="{GRAY}">и</tspan>
    <tspan fill="{BLACK}"> </tspan>
    <tspan fill="{ORANGE}" font-weight="bold">газеты</tspan>
    <tspan fill="{BLACK}">.</tspan>
  </text>
  <!-- Schema diagram -->
  <rect x="30" y="445" width="70" height="22" fill="{GREEN}" rx="3" opacity="0.2"/>
  <text x="65" y="460" font-family="Arial, sans-serif" font-size="9" fill="{GREEN}" text-anchor="middle">подлежащее</text>
  <rect x="110" y="445" width="55" height="22" fill="{BLUE}" rx="3" opacity="0.2"/>
  <text x="137" y="460" font-family="Arial, sans-serif" font-size="9" fill="{BLUE}" text-anchor="middle">сказуемое</text>
  <!-- Homogeneous members -->
  <rect x="30" y="478" width="60" height="22" fill="{ORANGE}" rx="3" opacity="0.2"/>
  <text x="60" y="493" font-family="Arial, sans-serif" font-size="9" fill="{ORANGE}" text-anchor="middle">книги</text>
  <text x="95" y="493" font-family="Arial, sans-serif" font-size="9" fill="{CORAL}">,</text>
  <rect x="105" y="478" width="65" height="22" fill="{ORANGE}" rx="3" opacity="0.2"/>
  <text x="137" y="493" font-family="Arial, sans-serif" font-size="9" fill="{ORANGE}" text-anchor="middle">журналы</text>
  <text x="175" y="493" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}">и</text>
  <rect x="190" y="478" width="65" height="22" fill="{ORANGE}" rx="3" opacity="0.2"/>
  <text x="222" y="493" font-family="Arial, sans-serif" font-size="9" fill="{ORANGE}" text-anchor="middle">газеты</text>
  <!-- Arrow showing they answer same question -->
  <line x1="60" y1="500" x2="60" y2="512" stroke="{ORANGE}" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="137" y1="500" x2="137" y2="512" stroke="{ORANGE}" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="222" y1="500" x2="222" y2="512" stroke="{ORANGE}" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="60" y1="512" x2="222" y2="512" stroke="{ORANGE}" stroke-width="1"/>
  <text x="140" y="526" font-family="Arial, sans-serif" font-size="9" fill="{ORANGE}" text-anchor="middle">всё — дополнения (что?)</text>
  <!-- Formula -->
  <text x="30" y="555" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY_DARK}">Формула:</text>
  <text x="30" y="572" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">[= -, -, и -]</text>
'''

    # Generalizing words
    svg = add_content_box(svg, 410, 405, 375, 180, "Обобщающие слова при однородных членах")
    svg += f'''
  <text x="425" y="428" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY_DARK}">Обобщающее слово = то же, что однородные</text>
  <line x1="425" y1="436" x2="770" y2="436" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <text x="425" y="454" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Если обобщ. слово ПЕРЕД однородными:</text>
  <text x="425" y="470" font-family="Arial, sans-serif" font-size="10" fill="{CORAL}" font-weight="bold">Двоеточие</text>
  <text x="500" y="470" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">после обобщ. слова</text>
  <text x="425" y="486" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">Весенние цветы: нарциссы, тюльпаны, гиацинты.</text>
  <line x1="425" y1="496" x2="770" y2="496" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <text x="425" y="514" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Если обобщ. слово ПОСЛЕ однородных:</text>
  <text x="425" y="530" font-family="Arial, sans-serif" font-size="10" fill="{CORAL}" font-weight="bold">Тире</text>
  <text x="470" y="530" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">перед обобщ. словом</text>
  <text x="425" y="546" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">Нарциссы, тюльпаны, гиацинты — весенние цветы.</text>
  <line x1="425" y1="556" x2="770" y2="556" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <text x="425" y="574" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Если предложение продолжается:</text>
  <text x="425" y="590" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">Цветы: нарциссы, тюльпаны — росли в саду.</text>
'''

    svg += svg_footer()
    return svg


# ============================================================
# LESSON 4: Обособленные члены предложения
# ============================================================
def generate_lesson4():
    svg = svg_header()
    svg = add_background(svg)
    svg = add_title_bar(svg, "Обособленные члены предложения", "Причастные и деепричастные обороты, приложения")
    svg = add_lesson_badge(svg, 4)

    # Definition
    svg = add_content_box(svg, 15, 82, 380, 80, "Что такое обособление?")
    svg += f'''
  <text x="30" y="106" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">Обособление — выделение второстепенного</text>
  <text x="30" y="122" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">члена предложения запятыми или тире для</text>
  <text x="30" y="138" font-family="Arial, sans-serif" font-size="11" fill="{PRIMARY}" font-weight="bold">придания ему большей самостоятельности.</text>
  <text x="30" y="154" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">Выделяются интонацией на письме запятыми.</text>
'''

    # Participial phrase
    svg = add_content_box(svg, 410, 82, 375, 80, "Причастный оборот")
    svg += f'''
  <text x="425" y="106" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">Причастный оборот = причастие + зависимые слова</text>
  <text x="425" y="124" font-family="Arial, sans-serif" font-size="11" fill="{CORAL}" font-weight="bold">Обособляется запятыми:</text>
  <text x="425" y="142" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Книга, <tspan fill="{ORANGE}" font-weight="bold">лежащая на столе</tspan>, интересная.</text>
  <text x="425" y="158" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">После определяемого слова — обособляется!</text>
'''

    # Detailed: participial
    svg = add_content_box(svg, 15, 175, 380, 200, "Причастный оборот: правила")
    svg += f'''
  <text x="30" y="198" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY_DARK}">1. После определяемого слова — обособляется:</text>
  <text x="30" y="216" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Мальчик, <tspan fill="{CORAL}">читающий книгу</tspan>, сидел у окна.</text>
  <text x="30" y="238" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY_DARK}">2. Перед определяемым словом — НЕ обособляется:</text>
  <text x="30" y="256" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}"><tspan fill="{ORANGE}">Читающий книгу</tspan> мальчик сидел у окна.</text>
  <text x="30" y="278" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY_DARK}">3. Всегда обособляется (любая позиция):</text>
  <text x="30" y="296" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Его сестра, <tspan fill="{PURPLE}">учившаяся в Москве</tspan>, приехала.</text>
  <text x="30" y="314" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">(относится к личному местоимению)</text>
  <text x="30" y="334" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY_DARK}">4. С союзом «как» — обособляется:</text>
  <text x="30" y="352" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Студент, <tspan fill="{BLUE}">как отличник учёбы</tspan>, получил стипендию.</text>
  <text x="30" y="368" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">(причина = значение «будучи»)</text>
'''

    # Adverbial phrase
    svg = add_content_box(svg, 410, 175, 375, 200, "Деепричастный оборот")
    svg += f'''
  <text x="425" y="198" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">Деепричастный оборот = деепричастие + зав. сл.</text>
  <rect x="425" y="208" width="350" height="26" fill="{CORAL}" rx="4" opacity="0.15"/>
  <text x="435" y="226" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{CORAL}">Обособляется ВСЕГДА, независимо от позиции!</text>
  <text x="425" y="250" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY_DARK}">Примеры:</text>
  <text x="425" y="268" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}"><tspan fill="{PURPLE}">Читая книгу</tspan>, мальчик сидел у окна.</text>
  <text x="425" y="286" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Мальчик, <tspan fill="{PURPLE}">читая книгу</tspan>, сидел у окна.</text>
  <text x="425" y="304" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Мальчик сидел у окна, <tspan fill="{PURPLE}">читая книгу</tspan>.</text>
  <line x1="425" y1="314" x2="770" y2="314" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <text x="425" y="332" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{CORAL}">Не обособляются:</text>
  <text x="425" y="348" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Фразеологизмы: спустя рукава, засучив рукава</text>
  <text x="425" y="364" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Одиночные деепричастия (нареч. знач.): молча, сидя</text>
'''

    # Application
    svg = add_content_box(svg, 15, 390, 380, 195, "Приложение")
    svg += f'''
  <text x="30" y="414" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">Приложение — определение, выраженное сущ.,</text>
  <text x="30" y="430" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">которое даёт предмету другое название.</text>
  <line x1="30" y1="438" x2="380" y2="438" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <text x="30" y="456" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY_DARK}">Обособляется запятыми:</text>
  <text x="30" y="474" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Иван, <tspan fill="{BLUE}">мой брат</tspan>, учится в университете.</text>
  <text x="30" y="492" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}"><tspan fill="{BLUE}">Упрямый</tspan>, он не хотел уступать. (к местоимению)</text>
  <text x="30" y="514" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY_DARK}">Обособляется дефисом (одиночное):</text>
  <text x="30" y="532" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Девочка-подросток, город-герой, учёный-биолог</text>
  <text x="30" y="554" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY_DARK}">С союзом «как» (причина):</text>
  <text x="30" y="572" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Как <tspan fill="{ORANGE}">истинный художник</tspan>, он видел красоту.</text>
'''

    # Rule summary
    svg = add_rule_box(svg, 410, 390, 375, 195, "Сводная таблица обособления", [
        "Причастный оборот:",
        "  После опред. слова → запятые",
        "  Перед опред. словом → без запятых",
        "  К местоимению → всегда запятые",
        "",
        "Деепричастный оборот:",
        "  Всегда обособляется запятыми!",
        "",
        "Приложение:",
        "  Распространённое → запятые",
        "  К местоимению → запятые",
        "  Одиночное → дефис",
        "  С «как» (причина) → запятые",
    ])

    svg += svg_footer()
    return svg


# ============================================================
# LESSON 5: Вводные слова и предложения
# ============================================================
def generate_lesson5():
    svg = svg_header()
    svg = add_background(svg)
    svg = add_title_bar(svg, "Вводные слова и предложения", "Группы по значению и знаки препинания")
    svg = add_lesson_badge(svg, 5)

    # Definition
    svg = add_content_box(svg, 15, 82, 770, 55, "Что такое вводные слова?")
    svg += f'''
  <text x="30" y="104" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">Вводные слова — слова, не входящие в грамматическую основу, выражающие отношение говорящего к высказыванию.</text>
  <text x="30" y="122" font-family="Arial, sans-serif" font-size="11" fill="{CORAL}" font-weight="bold">Они не являются членами предложения и выделяются запятыми!</text>
'''

    # Meaning groups
    svg = add_content_box(svg, 15, 148, 250, 225, "Группы по значению (1)")
    groups1 = [
        ("Уверенность", "конечно, несомненно, безусловно, разумеется", GREEN),
        ("Неуверенность", "кажется, вероятно, возможно, может быть", BLUE),
        ("Чувства", "к счастью, к сожалению, к ужасу, на радость", CORAL),
        ("Источник", "по-моему, по словам, говорят, по сообщению", PURPLE),
    ]
    for i, (name, words, color) in enumerate(groups1):
        by = 170 + i * 50
        svg += f'''
  <rect x="25" y="{by}" width="230" height="42" fill="{WHITE}" rx="4" stroke="{color}" stroke-width="1"/>
  <text x="35" y="{by + 16}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{color}">{name}</text>
  <text x="35" y="{by + 32}" font-family="Arial, sans-serif" font-size="8" fill="{GRAY}">{words}</text>
'''

    svg = add_content_box(svg, 280, 148, 250, 225, "Группы по значению (2)")
    groups2 = [
        ("Способ оформл.", "итак, таким образом, словом, наконец", ORANGE),
        ("Обращение к соб.", "видишь ли, понимаешь, скажем, пожалуйста", TEAL),
        ("Порядок мыслей", "во-первых, во-вторых, с одной стороны", PRIMARY),
        ("Оценка меры", "без преувеличения, самое большее", PRIMARY_DARK),
    ]
    for i, (name, words, color) in enumerate(groups2):
        by = 170 + i * 50
        svg += f'''
  <rect x="290" y="{by}" width="230" height="42" fill="{WHITE}" rx="4" stroke="{color}" stroke-width="1"/>
  <text x="300" y="{by + 16}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{color}">{name}</text>
  <text x="300" y="{by + 32}" font-family="Arial, sans-serif" font-size="8" fill="{GRAY}">{words}</text>
'''

    # NOT introductory words
    svg = add_rule_box(svg, 545, 148, 240, 225, "НЕ являются вводными!", [
        "Якобы, будто, вряд ли, едва ли",
      "— частицы и наречия",
        "",
        "Ведь, всё-таки, примерно",
      "— частицы",
        "",
        "Может быть, должно быть",
      "— могут быть вводными",
        "И НЕ вводными (смотря по смыслу!)",
        "",
        "Сравните:",
        "Он, <может быть>, придёт. (вводн.)",
        "Это <может быть> правдой. (сказ.)",
    ])

    # Examples
    svg = add_content_box(svg, 15, 386, 380, 200, "Примеры с вводными словами")
    examples = [
        ("К счастью,", "день был тёплый и ясный.", CORAL, "чувство"),
        ("Наверное,", "завтра будет дождь.", BLUE, "неуверенность"),
        ("По-моему,", "это правильное решение.", PURPLE, "источник"),
        ("Итак,", "подведём итоги.", ORANGE, "итог"),
        ("Во-первых,", "это выгодно; во-вторых, удобно.", PRIMARY, "порядок"),
    ]
    for i, (word, rest, color, group) in enumerate(examples):
        by = 410 + i * 34
        svg += f'  <rect x="25" y="{by}" width="360" height="26" fill="{WHITE}" rx="3" stroke="{color}" stroke-width="1"/>\n'
        svg += f'  <text x="35" y="{by + 17}" font-family="Arial, sans-serif" font-size="10" fill="{color}" font-weight="bold">{escape_xml(word)}</text>\n'
        svg += f'  <text x="35" y="{by + 17}" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}" dx="{len(word) * 7}"> {escape_xml(rest)}</text>\n'
        svg += f'  <text x="370" y="{by + 17}" font-family="Arial, sans-serif" font-size="8" fill="{GRAY}" text-anchor="end">({group})</text>\n'

    # Punctuation rules
    svg = add_rule_box(svg, 410, 386, 375, 200, "Знаки препинания при вводных словах", [
        "1. Запятые с двух сторон (в середине):",
        "   Он, к счастью, вернулся вовремя.",
        "",
        "2. Запятая перед (в начале):",
        "   Конечно, я согласен с тобой.",
        "",
        "3. Запятая после (в конце):",
        "   Я согласен, конечно.",
        "",
        "4. Тире вместо запятой (при паузе):",
        "   Он — к сожалению — опоздал.",
        "",
        "5. Вводное предложение:",
        '   Он, я думаю, скоро придёт.',
    ])

    svg += svg_footer()
    return svg


# ============================================================
# LESSON 6: Обращения и междометия
# ============================================================
def generate_lesson6():
    svg = svg_header()
    svg = add_background(svg)
    svg = add_title_bar(svg, "Обращения и междометия", "Знаки препинания при обращениях и междометиях")
    svg = add_lesson_badge(svg, 6)

    # Vocatives definition
    svg = add_content_box(svg, 15, 82, 380, 130, "Обращение")
    svg += f'''
  <text x="30" y="106" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">Обращение — слово (или словосочетание),</text>
  <text x="30" y="122" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">называющее того, к кому обращаются с речью.</text>
  <text x="30" y="142" font-family="Arial, sans-serif" font-size="11" fill="{CORAL}" font-weight="bold">Не является членом предложения!</text>
  <text x="30" y="162" font-family="Arial, sans-serif" font-size="11" fill="{GRAY}">Выделяется запятыми, редко — восклицательным знаком.</text>
  <text x="30" y="182" font-family="Arial, sans-serif" font-size="11" fill="{GREEN}" font-weight="bold">Форма: именительный падеж, звательная интонация</text>
  <text x="30" y="200" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Пример: <tspan fill="{ORANGE}" font-weight="bold">Мама</tspan>, я пришёл!</text>
'''

    # Punctuation with addresses
    svg = add_content_box(svg, 410, 82, 375, 130, "Знаки препинания при обращениях")
    svg += f'''
  <text x="425" y="106" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY_DARK}">В начале предложения:</text>
  <text x="425" y="122" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}"><tspan fill="{ORANGE}">Друзья</tspan>, пора отправляться в путь!</text>
  <text x="425" y="140" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY_DARK}">В середине предложения:</text>
  <text x="425" y="156" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Ты, <tspan fill="{ORANGE}">брат</tspan>, конечно, прав.</text>
  <text x="425" y="174" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY_DARK}">В конце предложения:</text>
  <text x="425" y="190" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Помоги мне, <tspan fill="{ORANGE}">мама</tspan>.</text>
  <text x="425" y="206" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{CORAL}">С восклицательным знаком:</text>
  <text x="425" y="206" font-family="Arial, sans-serif" font-size="10" fill="{CORAL}" dx="195">Мама!</text>
'''

    # Extended addresses
    svg = add_content_box(svg, 15, 225, 380, 155, "Распространённые обращения")
    svg += f'''
  <text x="30" y="248" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Обращение может состоять из нескольких слов:</text>
  <line x1="30" y1="256" x2="380" y2="256" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <rect x="30" y="264" width="350" height="28" fill="{WHITE}" rx="4" stroke="{ORANGE}" stroke-width="1"/>
  <text x="40" y="283" font-family="Arial, sans-serif" font-size="10" fill="{ORANGE}" font-weight="bold">Милая моя мамочка</text>
  <text x="185" y="283" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">, помоги мне!</text>
  <rect x="30" y="296" width="350" height="28" fill="{WHITE}" rx="4" stroke="{ORANGE}" stroke-width="1"/>
  <text x="40" y="315" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Прости меня, <tspan fill="{ORANGE}" font-weight="bold">родная моя бабушка</tspan>.</text>
  <rect x="30" y="328" width="350" height="28" fill="{WHITE}" rx="4" stroke="{ORANGE}" stroke-width="1"/>
  <text x="40" y="347" font-family="Arial, sans-serif" font-size="10" fill="{ORANGE}" font-weight="bold">Гражданин прохожий</text>
  <text x="200" y="347" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">, скажите, как пройти...</text>
  <text x="30" y="375" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}">Олонецкие обращения: междометие + имя</text>
'''

    # Interjections
    svg = add_content_box(svg, 410, 225, 375, 155, "Междометия")
    svg += f'''
  <text x="425" y="248" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">Междометие — слово, выражающее чувства,</text>
  <text x="425" y="264" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">побуждения, не называя их.</text>
  <line x1="425" y1="272" x2="770" y2="272" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <text x="425" y="290" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{GREEN}">Эмоциональные: ах, ой, увы, браво, фу</text>
  <text x="425" y="308" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{BLUE}">Побудительные: ну, эй, ау, кис-кис</text>
  <text x="425" y="326" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PURPLE}">Этикетные: спасибо, здравствуйте, извините</text>
  <line x1="425" y1="334" x2="770" y2="334" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <text x="425" y="352" font-family="Arial, sans-serif" font-size="10" fill="{CORAL}" font-weight="bold">Выделяются запятой или восклицательным знаком!</text>
  <text x="425" y="370" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Ах, как красиво! | Эй, подождите!</text>
'''

    # Poetic examples
    svg = add_content_box(svg, 15, 395, 380, 190, "Обращения в поэтической речи")
    svg += f'''
  <text x="30" y="418" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">В стихах обращения особенно выразительны:</text>
  <line x1="30" y1="426" x2="380" y2="426" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <rect x="30" y="434" width="350" height="40" fill="{WHITE}" rx="4" stroke="{PURPLE}" stroke-width="1"/>
  <text x="40" y="452" font-family="Arial, sans-serif" font-size="10" fill="{PURPLE}" font-weight="bold">Мороз</text>
  <text x="90" y="452" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">, красный нос!</text>
  <text x="40" y="468" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}">Н. Некрасов (звательный падеж)</text>
  <rect x="30" y="480" width="350" height="40" fill="{WHITE}" rx="4" stroke="{BLUE}" stroke-width="1"/>
  <text x="40" y="498" font-family="Arial, sans-serif" font-size="10" fill="{BLUE}" font-weight="bold">Пушкин</text>
  <text x="100" y="498" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">, ты нам дорог!</text>
  <text x="40" y="514" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}">Обращение к лицу по фамилии</text>
  <rect x="30" y="526" width="350" height="40" fill="{WHITE}" rx="4" stroke="{GREEN}" stroke-width="1"/>
  <text x="40" y="544" font-family="Arial, sans-serif" font-size="10" fill="{GREEN}" font-weight="bold">Родина моя</text>
  <text x="140" y="544" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">, я твой сын!</text>
  <text x="40" y="560" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}">Обращение к неживому предмету (риторическое)</text>
  <text x="30" y="580" font-family="Arial, sans-serif" font-size="9" fill="{CORAL}" font-weight="bold">Риторическое обращение — к неживому или отсутствующему</text>
'''

    # Summary rule box
    svg = add_rule_box(svg, 410, 395, 375, 190, "Правила: запятые и знаки", [
        "ОБРАЩЕНИЕ:",
        "  - Запятая: Мама, я дома.",
        "  - Воскл. знак: Мама! Я дома!",
        "  - В середине: Ты, мама, права.",
        "  - Распростр.: Мой дорогой друг, привет!",
        "",
        "МЕЖДОМЕТИЕ:",
        "  - Запятая: Увы, он опоздал.",
        "  - Воскл. знак: Ой! Как страшно!",
        "  - После междометия-паузы:",
        "    Эй, послушайте!",
    ])

    svg += svg_footer()
    return svg


# ============================================================
# LESSON 7: Прямая и косвенная речь
# ============================================================
def generate_lesson7():
    svg = svg_header()
    svg = add_background(svg)
    svg = add_title_bar(svg, "Прямая и косвенная речь", "Оформление диалога, цитирование, перевод речи")
    svg = add_lesson_badge(svg, 7)

    # Direct speech definition
    svg = add_content_box(svg, 15, 82, 380, 105, "Прямая речь")
    svg += f'''
  <text x="30" y="106" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">Прямая речь — точно воспроизведённая</text>
  <text x="30" y="122" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">чужая речь, сохраняющая её форму и содержание.</text>
  <line x1="30" y1="130" x2="380" y2="130" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <text x="30" y="148" font-family="Arial, sans-serif" font-size="11" fill="{GREEN}" font-weight="bold">Слова автора</text>
  <text x="130" y="148" font-family="Arial, sans-serif" font-size="11" fill="{GRAY}">+ </text>
  <text x="145" y="148" font-family="Arial, sans-serif" font-size="11" fill="{BLUE}" font-weight="bold">Прямая речь</text>
  <text x="30" y="168" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">А: «П!» | А: «П.» | «П», — а. | «П!» — а. | «П?» — а.</text>
  <text x="30" y="184" font-family="Arial, sans-serif" font-size="9" fill="{CORAL}">А — слова автора, П — прямая речь</text>
'''

    # Schemes
    svg = add_content_box(svg, 410, 82, 375, 105, "Схемы прямой речи")
    schemes = [
        ("А: «П!»", "Он сказал: «Я иду!»", GREEN),
        ("А: «П.»", "Она ответила: «Я согласна.»", BLUE),
        ("«П», — а.", "«Я иду», — сказал он.", PURPLE),
        ("«П!» — а.", "«Помогите!» — крикнула она.", CORAL),
        ("«П?» — а.", "«Ты идёшь?» — спросил друг.", ORANGE),
    ]
    for i, (scheme, example, color) in enumerate(schemes):
        by = 100 + i * 16
        svg += f'  <text x="425" y="{by}" font-family="Arial, sans-serif" font-size="10" fill="{color}" font-weight="bold">{escape_xml(scheme)}</text>\n'
        svg += f'  <text x="500" y="{by}" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}">{escape_xml(example)}</text>\n'

    # Dialogue
    svg = add_content_box(svg, 15, 200, 380, 175, "Оформление диалога")
    svg += f'''
  <text x="30" y="224" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">Каждая реплика — с новой строки,</text>
  <text x="30" y="240" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">начинается с тире:</text>
  <line x1="30" y1="248" x2="380" y2="248" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <rect x="30" y="256" width="350" height="100" fill="{WHITE}" rx="4" stroke="{PRIMARY}" stroke-width="1.5"/>
  <text x="45" y="275" font-family="Arial, sans-serif" font-size="11" fill="{PRIMARY_DARK}">— Привет! Как дела?</text>
  <text x="45" y="295" font-family="Arial, sans-serif" font-size="11" fill="{PRIMARY_DARK}">— Спасибо, хорошо. А у тебя?</text>
  <text x="45" y="315" font-family="Arial, sans-serif" font-size="11" fill="{PRIMARY_DARK}">— Тоже отлично!</text>
  <text x="45" y="340" font-family="Arial, sans-serif" font-size="9" fill="{CORAL}" font-weight="bold">Кавычки НЕ ставятся в диалоге!</text>
  <text x="45" y="354" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}">Реплики начинаются с тире</text>
'''

    # Indirect speech
    svg = add_content_box(svg, 410, 200, 375, 175, "Косвенная речь")
    svg += f'''
  <text x="425" y="224" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">Косвенная речь — передача чужой речи</text>
  <text x="425" y="240" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">в виде придаточного предложения.</text>
  <line x1="425" y1="248" x2="770" y2="248" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <text x="425" y="266" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY_DARK}">Прямая → Косвенная:</text>
  <rect x="425" y="276" width="350" height="44" fill="{WHITE}" rx="4" stroke="{GREEN}" stroke-width="1"/>
  <text x="435" y="294" font-family="Arial, sans-serif" font-size="10" fill="{GREEN}">Он сказал: «Я иду домой».</text>
  <text x="435" y="312" font-family="Arial, sans-serif" font-size="10" fill="{BLUE}">Он сказал, что он идёт домой.</text>
  <rect x="425" y="326" width="350" height="44" fill="{WHITE}" rx="4" stroke="{GREEN}" stroke-width="1"/>
  <text x="435" y="344" font-family="Arial, sans-serif" font-size="10" fill="{GREEN}">Она спросила: «Ты придёшь?»</text>
  <text x="435" y="362" font-family="Arial, sans-serif" font-size="10" fill="{BLUE}">Она спросила, приду ли я.</text>
'''

    # Conversion rules
    svg = add_rule_box(svg, 15, 390, 380, 195, "Замена прямой речи косвенной", [
        "1. Повествоват. → союз ЧТО:",
        "   «Я читаю» → что он читает",
        "",
        "2. Вопросительная → союз ЛИ:",
        "   «Ты идёшь?» → идёшь ли ты",
        "",
        "3. Побудительная → чтобы:",
        "   «Иди сюда!» → чтобы он шёл сюда",
        "",
        "4. Меняются местоимения:",
        "   я → он, мы → они, мой → его",
        "",
        "5. Меняется время глагола:",
        "   иду → идёт, читал → читал",
    ])

    # Quotations
    svg = add_content_box(svg, 410, 390, 375, 195, "Цитирование")
    svg += f'''
  <text x="425" y="414" font-family="Arial, sans-serif" font-size="11" fill="{BLACK}">Цитата — дословная выдержка из текста.</text>
  <line x1="425" y1="422" x2="770" y2="422" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <text x="425" y="440" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY_DARK}">Правила оформления цитат:</text>
  <text x="425" y="458" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">1. В кавычках с указанием автора:</text>
  <text x="425" y="474" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">Пушкин писал: «Унылая пора! Очей очарованье!»</text>
  <text x="425" y="496" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">2. С пропуском — многоточие:</text>
  <text x="425" y="512" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">«Унылая пора... очарованье!»</text>
  <text x="425" y="534" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">3. Цитата как часть предложения:</text>
  <text x="425" y="550" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">Пушкин называл осень «унылой порой».</text>
  <text x="425" y="572" font-family="Arial, sans-serif" font-size="10" fill="{CORAL}" font-weight="bold">Без кавычек, если оформлена как косвенная речь!</text>
'''

    svg += svg_footer()
    return svg


# ============================================================
# LESSON 8: Сложное предложение
# ============================================================
def generate_lesson8():
    svg = svg_header()
    svg = add_background(svg)
    svg = add_arrow_def(svg)
    svg = add_title_bar(svg, "Сложное предложение", "Виды сложных предложений и средства связи")
    svg = add_lesson_badge(svg, 8)

    # Definition
    svg = add_content_box(svg, 15, 82, 770, 65, "Что такое сложное предложение?")
    svg += f'''
  <text x="30" y="106" font-family="Arial, sans-serif" font-size="12" fill="{BLACK}">Сложное предложение — предложение, состоящее из двух и более грамматических основ,</text>
  <text x="30" y="124" font-family="Arial, sans-serif" font-size="12" fill="{BLACK}">объединённых по смыслу и интонации. Части могут быть связаны </text>
  <text x="30" y="142" font-family="Arial, sans-serif" font-size="12" fill="{PRIMARY}" font-weight="bold">союзами, союзными словами или только интонацией.</text>
'''

    # Types overview diagram
    svg = add_content_box(svg, 15, 160, 770, 130, "Классификация сложных предложений")
    svg += f'''
  <rect x="250" y="180" width="300" height="30" fill="{PRIMARY}" rx="5"/>
  <text x="400" y="200" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{WHITE}" text-anchor="middle">СЛОЖНОЕ ПРЕДЛОЖЕНИЕ</text>
  <!-- Branch lines -->
  <line x1="320" y1="210" x2="200" y2="238" stroke="{PRIMARY}" stroke-width="2"/>
  <line x1="400" y1="210" x2="400" y2="238" stroke="{PRIMARY}" stroke-width="2"/>
  <line x1="480" y1="210" x2="600" y2="238" stroke="{PRIMARY}" stroke-width="2"/>
  <!-- Three types -->
  <rect x="80" y="238" width="230" height="36" fill="{GREEN}" rx="5" opacity="0.15" stroke="{GREEN}" stroke-width="1.5"/>
  <text x="195" y="261" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{GREEN}" text-anchor="middle">Сложносочинённое (ССП)</text>
  <rect x="320" y="238" width="160" height="36" fill="{BLUE}" rx="5" opacity="0.15" stroke="{BLUE}" stroke-width="1.5"/>
  <text x="400" y="261" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{BLUE}" text-anchor="middle">Сложноподчинённое (СПП)</text>
  <rect x="490" y="238" width="230" height="36" fill="{ORANGE}" rx="5" opacity="0.15" stroke="{ORANGE}" stroke-width="1.5"/>
  <text x="605" y="261" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{ORANGE}" text-anchor="middle">Бессоюзное (БСП)</text>
  <!-- Labels -->
  <text x="195" y="283" font-family="Arial, sans-serif" font-size="9" fill="{GREEN}" text-anchor="middle">Союзы: и, а, но, или</text>
  <text x="400" y="283" font-family="Arial, sans-serif" font-size="9" fill="{BLUE}" text-anchor="middle">Союзы: что, чтобы, если...</text>
  <text x="605" y="283" font-family="Arial, sans-serif" font-size="9" fill="{ORANGE}" text-anchor="middle">Только интонация</text>
'''

    # Compound sentences (ССП)
    svg = add_content_box(svg, 15, 305, 380, 140, "Сложносочинённое предложение (ССП)")
    svg += f'''
  <text x="30" y="328" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Части равноправны, связаны сочинительными союзами:</text>
  <rect x="30" y="336" width="350" height="18" fill="{GREEN}" rx="3" opacity="0.1"/>
  <text x="35" y="349" font-family="Arial, sans-serif" font-size="9" fill="{GREEN}" font-weight="bold">Соединительные:</text>
  <text x="140" y="349" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}">и, да(=и), ни...ни, тоже, также</text>
  <rect x="30" y="356" width="350" height="18" fill="{ORANGE}" rx="3" opacity="0.1"/>
  <text x="35" y="369" font-family="Arial, sans-serif" font-size="9" fill="{ORANGE}" font-weight="bold">Противительные:</text>
  <text x="145" y="369" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}">а, но, да(=но), однако, зато</text>
  <rect x="30" y="376" width="350" height="18" fill="{BLUE}" rx="3" opacity="0.1"/>
  <text x="35" y="389" font-family="Arial, sans-serif" font-size="9" fill="{BLUE}" font-weight="bold">Разделительные:</text>
  <text x="140" y="389" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}">или, либо, то...то, не то...не то</text>
  <line x1="30" y1="398" x2="380" y2="398" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <text x="30" y="414" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}"><tspan fill="{GREEN}">Ветер шумел</tspan>, <tspan fill="{CORAL}" font-weight="bold">и</tspan> <tspan fill="{GREEN}">дождь стучал</tspan> в окно.</text>
  <text x="30" y="432" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">[=], и [=]</text>
  <text x="30" y="444" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}"><tspan fill="{GREEN}">Он устал</tspan>, <tspan fill="{CORAL}" font-weight="bold">но</tspan> <tspan fill="{GREEN}">не сдался</tspan>.</text>
'''

    # Complex sentences (СПП)
    svg = add_content_box(svg, 410, 305, 375, 140, "Сложноподчинённое предложение (СПП)")
    svg += f'''
  <text x="425" y="328" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Главное + придаточное (от него вопрос):</text>
  <rect x="425" y="336" width="345" height="22" fill="{BLUE}" rx="3" opacity="0.1"/>
  <text x="435" y="351" font-family="Arial, sans-serif" font-size="9" fill="{BLUE}" font-weight="bold">Союзы:</text>
  <text x="490" y="351" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}">что, чтобы, если, когда, хотя, потому что...</text>
  <rect x="425" y="360" width="345" height="22" fill="{PURPLE}" rx="3" opacity="0.1"/>
  <text x="435" y="375" font-family="Arial, sans-serif" font-size="9" fill="{PURPLE}" font-weight="bold">Союзные слова:</text>
  <text x="540" y="375" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}">кто, что, какой, где, куда, где, откуда...</text>
  <line x1="425" y1="386" x2="770" y2="386" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <text x="425" y="404" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}"><tspan fill="{BLUE}">Я знаю</tspan>, <tspan fill="{CORAL}" font-weight="bold">что</tspan> <tspan fill="{PURPLE}">он придёт</tspan>.</text>
  <text x="425" y="420" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">[=], (что =)</text>
  <text x="425" y="436" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}"><tspan fill="{BLUE}">Мы ушли</tspan>, <tspan fill="{CORAL}" font-weight="bold">потому что</tspan> <tspan fill="{PURPLE}">стемнело</tspan>.</text>
'''

    # Unionless
    svg = add_content_box(svg, 15, 460, 380, 125, "Бессоюзное предложение (БСП)")
    svg += f'''
  <text x="30" y="484" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Части связаны только интонацией:</text>
  <line x1="30" y1="492" x2="380" y2="492" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <text x="30" y="510" font-family="Arial, sans-serif" font-size="10" fill="{ORANGE}" font-weight="bold">Запятая — перечисление:</text>
  <text x="30" y="526" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Светило солнце, птицы пели.</text>
  <text x="30" y="544" font-family="Arial, sans-serif" font-size="10" fill="{ORANGE}" font-weight="bold">Двоеточие — пояснение/причина:</text>
  <text x="30" y="560" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Он не пришёл: заболел.</text>
  <text x="30" y="578" font-family="Arial, sans-serif" font-size="10" fill="{ORANGE}" font-weight="bold">Тире — противопоставление/время:</text>
  <text x="220" y="578" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Лес рубят — щепки летят.</text>
'''

    # Comparison of types
    svg = add_rule_box(svg, 410, 460, 375, 125, "Сравнение трёх типов", [
        "ССП: равноправные части",
        "  Ветер шумел, и дождь стучал.",
        "  Схема: [...], и [...]",
        "",
        "СПП: главное + придаточное",
        "  Я знаю, что он придёт.",
        "  Схема: [...], (что ...)",
        "",
        "БСП: только интонация",
        "  Светило солнце; шёл дождь.",
        "  Схема: [...]; [...]",
    ])

    svg += svg_footer()
    return svg


# ============================================================
# LESSON 9: Сложносочинённые и сложноподчинённые предложения
# ============================================================
def generate_lesson9():
    svg = svg_header()
    svg = add_background(svg)
    svg = add_title_bar(svg, "Сложносочинённые и сложноподчинённые", "Виды придаточных предложений, союзы и союзные слова")
    svg = add_lesson_badge(svg, 9)

    # SSP details
    svg = add_content_box(svg, 15, 82, 380, 160, "Сложносочинённое (ССП): подробно")
    svg += f'''
  <text x="30" y="106" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Равноправные простые предложения:</text>
  <rect x="30" y="116" width="350" height="50" fill="{WHITE}" rx="4" stroke="{GREEN}" stroke-width="1"/>
  <text x="40" y="133" font-family="Arial, sans-serif" font-size="10" fill="{GREEN}" font-weight="bold">Соединительные (одновременность/последоват.):</text>
  <text x="40" y="149" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Ветер шумел, <tspan fill="{CORAL}" font-weight="bold">и</tspan> дождь стучал, <tspan fill="{CORAL}" font-weight="bold">и</tspan> гром гремел.</text>
  <rect x="30" y="170" width="350" height="35" fill="{WHITE}" rx="4" stroke="{ORANGE}" stroke-width="1"/>
  <text x="40" y="187" font-family="Arial, sans-serif" font-size="10" fill="{ORANGE}" font-weight="bold">Противительные (противопоставление):</text>
  <text x="40" y="200" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Он хотел помочь, <tspan fill="{CORAL}" font-weight="bold">но</tspan> не смог.</text>
  <rect x="30" y="209" width="350" height="28" fill="{WHITE}" rx="4" stroke="{BLUE}" stroke-width="1"/>
  <text x="40" y="226" font-family="Arial, sans-serif" font-size="10" fill="{BLUE}" font-weight="bold">Разделительные (чередование/выбор):</text>
  <text x="40" y="234" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}">То солнце светило, <tspan fill="{CORAL}" font-weight="bold">то</tspan> шёл дождь.</text>
'''

    # SPP - types of subordinate clauses
    svg = add_content_box(svg, 410, 82, 375, 160, "Сложноподчинённое (СПП): виды придаточных")
    svg += f'''
  <text x="425" y="104" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Придаточное отвечает на вопрос от главного:</text>
  <line x1="425" y1="112" x2="770" y2="112" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <rect x="425" y="118" width="175" height="22" fill="{GREEN}" rx="3" opacity="0.12"/>
  <text x="435" y="133" font-family="Arial, sans-serif" font-size="9" fill="{GREEN}" font-weight="bold">Определительное: какой?</text>
  <rect x="610" y="118" width="165" height="22" fill="{BLUE}" rx="3" opacity="0.12"/>
  <text x="620" y="133" font-family="Arial, sans-serif" font-size="9" fill="{BLUE}" font-weight="bold">Изъяснительное: что? о чём?</text>
  <rect x="425" y="144" width="175" height="22" fill="{PURPLE}" rx="3" opacity="0.12"/>
  <text x="435" y="159" font-family="Arial, sans-serif" font-size="9" fill="{PURPLE}" font-weight="bold">Образа действия: как?</text>
  <rect x="610" y="144" width="165" height="22" fill="{ORANGE}" rx="3" opacity="0.12"/>
  <text x="620" y="159" font-family="Arial, sans-serif" font-size="9" fill="{ORANGE}" font-weight="bold">Степени: в какой степени?</text>
  <rect x="425" y="170" width="175" height="22" fill="{TEAL}" rx="3" opacity="0.12"/>
  <text x="435" y="185" font-family="Arial, sans-serif" font-size="9" fill="{TEAL}" font-weight="bold">Места: где? куда? откуда?</text>
  <rect x="610" y="170" width="165" height="22" fill="{CORAL}" rx="3" opacity="0.12"/>
  <text x="620" y="185" font-family="Arial, sans-serif" font-size="9" fill="{CORAL}" font-weight="bold">Времени: когда? как долго?</text>
  <rect x="425" y="196" width="175" height="22" fill="{PRIMARY}" rx="3" opacity="0.12"/>
  <text x="435" y="211" font-family="Arial, sans-serif" font-size="9" fill="{PRIMARY}" font-weight="bold">Условия: при каком условии?</text>
  <rect x="610" y="196" width="165" height="22" fill="{PRIMARY_DARK}" rx="3" opacity="0.12"/>
  <text x="620" y="211" font-family="Arial, sans-serif" font-size="9" fill="{PRIMARY_DARK}" font-weight="bold">Причины: почему? отчего?</text>
  <rect x="425" y="222" width="175" height="14" fill="{GREEN}" rx="2" opacity="0.08"/>
  <text x="435" y="233" font-family="Arial, sans-serif" font-size="9" fill="{GREEN}">Цели: зачем? для чего?</text>
  <rect x="610" y="222" width="165" height="14" fill="{BLUE}" rx="2" opacity="0.08"/>
  <text x="620" y="233" font-family="Arial, sans-serif" font-size="9" fill="{BLUE}">Уступки: несмотря на что?</text>
'''

    # Detailed examples of subordinate clauses
    svg = add_content_box(svg, 15, 257, 770, 170, "Примеры придаточных предложений")
    clauses = [
        ("Определительное", "Книга, которую я читаю, интересная.", "какую?", GREEN),
        ("Изъяснительное", "Я знаю, что он придёт завтра.", "что?", BLUE),
        ("Обстоятельственное места", "Я живу там, где родился.", "где?", TEAL),
        ("Обстоятельственное времени", "Когда наступит утро, мы отправимся в путь.", "когда?", CORAL),
        ("Обстоятельственное причины", "Он остался дома, потому что заболел.", "почему?", PRIMARY_DARK),
        ("Обстоятельственное условия", "Если будет время, я приду.", "при каком условии?", PRIMARY),
        ("Обстоятельственное цели", "Я пришёл, чтобы поговорить с тобой.", "зачем?", GREEN),
        ("Обстоятельственное уступки", "Хотя было холодно, мы гуляли.", "несмотря на что?", ORANGE),
    ]
    for i, (name, example, question, color) in enumerate(clauses):
        by = 280 + i * 18
        svg += f'  <rect x="25" y="{by - 10}" width="8" height="14" fill="{color}" rx="2"/>\n'
        svg += f'  <text x="40" y="{by}" font-family="Arial, sans-serif" font-size="9" fill="{color}" font-weight="bold">{name} ({question})</text>\n'
        svg += f'  <text x="300" y="{by}" font-family="Arial, sans-serif" font-size="9" fill="{BLACK}">{escape_xml(example)}</text>\n'

    # Conjunctions vs. allied words
    svg = add_content_box(svg, 15, 442, 380, 145, "Союзы и союзные слова в СПП")
    svg += f'''
  <text x="30" y="466" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY_DARK}">Союз — не член предложения:</text>
  <text x="30" y="482" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Я знаю, <tspan fill="{CORAL}" font-weight="bold">что</tspan> он придёт.</text>
  <text x="30" y="498" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}">(что — нельзя убрать, не член предл.)</text>
  <line x1="30" y1="506" x2="380" y2="506" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <text x="30" y="522" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY_DARK}">Союзное слово — член предложения:</text>
  <text x="30" y="538" font-family="Arial, sans-serif" font-size="10" fill="{BLACK}">Книга, <tspan fill="{CORAL}" font-weight="bold">которую</tspan> я читаю, интересная.</text>
  <text x="30" y="554" font-family="Arial, sans-serif" font-size="9" fill="{GRAY}">(которую — дополнение, можно заменить: её)</text>
  <line x1="30" y1="562" x2="380" y2="562" stroke="{GRAY_LIGHT}" stroke-width="1"/>
  <text x="30" y="578" font-family="Arial, sans-serif" font-size="9" fill="{CORAL}" font-weight="bold">Проверка: можно ли убрать? Если да — союз.</text>
'''

    # Schema diagrams
    svg = add_rule_box(svg, 410, 442, 375, 145, "Схемы сложных предложений", [
        "ССП:  [...], и [...]  (равноправные)",
        "  Ветер дул, и снег падал.",
        "",
        "СПП:  [...], (что ...)  (главное, придат.)",
        "  Я знаю, (что он придёт).",
        "",
        "СПП:  (Когда ...), [...]  (придат., главное)",
        "  (Когда наступит утро), мы уйдём.",
        "",
        "СПП:  [...], (где ...)  (главное, придат. места)",
        "  Я живу там, (где родился).",
    ])

    svg += svg_footer()
    return svg


# ============================================================
# MAIN: Generate all lessons
# ============================================================
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    generators = [
        (1, generate_lesson1),
        (2, generate_lesson2),
        (3, generate_lesson3),
        (4, generate_lesson4),
        (5, generate_lesson5),
        (6, generate_lesson6),
        (7, generate_lesson7),
        (8, generate_lesson8),
        (9, generate_lesson9),
    ]

    results = []
    for num, gen_func in generators:
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
        try:
            svg_content = gen_func()
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(svg_content)

            # Validate XML
            try:
                tree = ET.parse(filepath)
                root = tree.getroot()
                results.append((num, filepath, "OK", "Valid XML"))
            except ET.ParseError as e:
                results.append((num, filepath, "XML_ERROR", str(e)))

        except Exception as e:
            results.append((num, filepath, "GEN_ERROR", str(e)))

    print("=" * 60)
    print("GENERATION RESULTS: Grade 8 Russian Language SVGs")
    print("=" * 60)
    ok_count = 0
    for num, path, status, detail in results:
        icon = "✅" if status == "OK" else "❌"
        print(f"  {icon} Lesson {num}: {path} — {status} ({detail})")
        if status == "OK":
            ok_count += 1
    print(f"\nTotal: {ok_count}/{len(generators)} files generated successfully")
    print("=" * 60)


if __name__ == "__main__":
    main()
