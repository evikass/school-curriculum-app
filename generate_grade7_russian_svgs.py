#!/usr/bin/env python3
"""
Generate Grade 7 Russian Language SVG lesson images.
Each SVG is 800x600, uses rose/pink color scheme (#EC4899 primary),
contains sentence diagrams, rules, and educational content in Russian.
Validated with xml.etree.ElementTree.
"""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/russian"

# ─── Color Palette ───
PRIMARY = "#EC4899"
PRIMARY_LIGHT = "#F9A8D4"
PRIMARY_DARK = "#BE185D"
BG = "#FFF1F2"
BG_CARD = "#FFFFFF"
TEXT_DARK = "#1F2937"
TEXT_MED = "#6B7280"
ACCENT = "#8B5CF6"
ACCENT2 = "#F59E0B"
BORDER = "#FBCFE8"
HIGHLIGHT = "#FDF2F8"
GREEN = "#10B981"
RED = "#EF4444"
BLUE = "#3B82F6"

W, H = 800, 600


def escape_xml(text):
    """Escape special XML characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def svg_header():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'''


def svg_footer():
    return "</svg>"


def card(x, y, w, h, rx=12, fill=BG_CARD, stroke=BORDER, sw=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def text_el(x, y, content, size=16, fill=TEXT_DARK, anchor="middle", weight="normal", family="Arial, sans-serif"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" font-family="{family}">{escape_xml(content)}</text>'


def text_left(x, y, content, size=16, fill=TEXT_DARK, weight="normal", family="Arial, sans-serif"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="start" font-weight="{weight}" font-family="{family}">{escape_xml(content)}</text>'


def title_bar(y, text, h=48):
    """Rose header bar with centered title."""
    parts = [
        f'<rect x="0" y="{y}" width="{W}" height="{h}" fill="{PRIMARY}"/>',
        text_el(W // 2, y + 32, text, size=22, fill="#FFFFFF", weight="bold"),
    ]
    return "\n".join(parts)


def subtitle_badge(x, y, text, fill=PRIMARY):
    """Small rounded badge with text."""
    w = len(text) * 10 + 24
    parts = [
        f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="14" fill="{fill}"/>',
        text_el(x + w // 2, y + 19, text, size=13, fill="#FFFFFF", weight="bold"),
    ]
    return "\n".join(parts)


def arrow_line(x1, y1, x2, y2, stroke=PRIMARY, sw=2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" marker-end="url(#arrowhead)"/>'


def defs_arrow():
    return '''<defs><marker id="arrowhead" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="#EC4899"/></marker></defs>'''


def rounded_box_with_text(x, y, w, h, text, fill=HIGHLIGHT, stroke=PRIMARY, text_color=TEXT_DARK, size=14, rx=8):
    parts = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>',
        text_el(x + w // 2, y + h // 2 + 5, text, size=size, fill=text_color),
    ]
    return "\n".join(parts)


def lesson_number_badge(n):
    """Top-left lesson number circle."""
    return f'''<circle cx="40" cy="30" r="20" fill="{PRIMARY_DARK}"/>
    <text x="40" y="36" font-size="16" fill="#FFFFFF" text-anchor="middle" font-weight="bold" font-family="Arial, sans-serif">{n}</text>'''


# ═══════════════════════════════════════════════════════════
# LESSON 1: Фонетика и графика
# ═══════════════════════════════════════════════════════════
def lesson_1():
    s = svg_header()
    # Background
    s += f'<rect width="{W}" height="{H}" fill="{BG}"/>'
    # Title bar
    s += title_bar(0, "Фонетика и графика")
    s += lesson_number_badge(1)

    # --- Left column: Vowels ---
    s += card(20, 60, 370, 250)
    s += subtitle_badge(30, 68, "Гласные звуки", PRIMARY)
    # Table header
    s += f'<rect x="30" y="102" width="350" height="26" rx="4" fill="{PRIMARY}" opacity="0.15"/>'
    s += text_left(38, 120, "Звук", 13, PRIMARY_DARK, "bold")
    s += text_left(110, 120, "Буквы", 13, PRIMARY_DARK, "bold")
    s += text_left(230, 120, "Пример", 13, PRIMARY_DARK, "bold")

    vowels = [
        ("[а]", "а, я", "м**я**со"),
        ("[о]", "о, ё", "в**ё**дра"),
        ("[у]", "у, ю", "л**ю**к"),
        ("[ы]", "ы, и", "м**ы**ло"),
        ("[и]", "и, е", "л**е**с"),
        ("[э]", "э, е", "м**э**р"),
    ]
    for i, (sound, letters, example) in enumerate(vowels):
        y_pos = 140 + i * 26
        bg_fill = HIGHLIGHT if i % 2 == 0 else BG_CARD
        s += f'<rect x="30" y="{y_pos}" width="350" height="26" fill="{bg_fill}"/>'
        s += text_left(38, y_pos + 18, sound, 13, PRIMARY_DARK)
        s += text_left(110, y_pos + 18, letters, 13, TEXT_DARK)
        s += text_left(230, y_pos + 18, example, 13, TEXT_MED)

    # --- Right column: Consonants ---
    s += card(410, 60, 370, 250)
    s += subtitle_badge(420, 68, "Согласные звуки", ACCENT)

    # Voiced
    s += text_left(420, 106, "Звонкие:", 14, ACCENT, "bold")
    s += text_left(420, 126, "б в г д ж з", 15, TEXT_DARK)
    s += text_left(420, 148, "б' в' г' д' ж' з'", 15, TEXT_MED)

    # Voiceless
    s += text_left(420, 176, "Глухие:", 14, BLUE, "bold")
    s += text_left(420, 196, "п ф к т ш с", 15, TEXT_DARK)
    s += text_left(420, 218, "п' ф' к' т' ш' с'", 15, TEXT_MED)

    # Sonorants
    s += text_left(420, 246, "Сонорные:", 14, GREEN, "bold")
    s += text_left(420, 266, "л м н р й", 15, TEXT_DARK)
    s += text_left(420, 286, "л' м' н' р'", 15, TEXT_MED)

    # --- Bottom: Hard/Soft table ---
    s += card(20, 320, 760, 130)
    s += subtitle_badge(30, 328, "Твёрдые и мягкие согласные", PRIMARY_DARK)

    # Hard column
    s += f'<rect x="35" y="366" width="355" height="70" rx="8" fill="{HIGHLIGHT}" stroke="{PRIMARY_LIGHT}" stroke-width="1"/>'
    s += text_el(212, 386, "Твёрдые", 15, PRIMARY_DARK, weight="bold")
    s += text_el(212, 408, "Перед а, о, у, ы, э", 13, TEXT_DARK)
    s += text_el(212, 426, "лук, мэр, сок, дым", 13, TEXT_MED)

    # Soft column
    s += f'<rect x="410" y="366" width="355" height="70" rx="8" fill="#EEF2FF" stroke="{ACCENT}" stroke-width="1"/>'
    s += text_el(587, 386, "Мягкие", 15, ACCENT, weight="bold")
    s += text_el(587, 408, "Перед я, ё, ю, и, е, ь", 13, TEXT_DARK)
    s += text_el(587, 426, "люк, мёрз, люк, мир", 13, TEXT_MED)

    # --- Bottom rule ---
    s += card(20, 460, 760, 130)
    s += subtitle_badge(30, 468, "Правила фонетики", ACCENT2)
    rules = [
        "1. Гласные звуки — слогообразующие: ск**о**р, **а**лый",
        "2. [й'] — всегда мягкий согласный",
        "3. [ж], [ш], [ц] — всегда твёрдые",
        "4. [ч'], [щ'] — всегда мягкие",
        "5. Буквы е, ё, ю, я = [й'э], [й'о], [й'у], [й'а] в начале слова",
    ]
    for i, rule in enumerate(rules):
        s += text_left(40, 510 + i * 18, rule, 13, TEXT_DARK)

    s += svg_footer()
    return s


# ═══════════════════════════════════════════════════════════
# LESSON 2: Состав слова
# ═══════════════════════════════════════════════════════════
def lesson_2():
    s = svg_header()
    s += f'<rect width="{W}" height="{H}" fill="{BG}"/>'
    s += title_bar(0, "Состав слова")
    s += lesson_number_badge(2)

    # --- Morpheme diagram: word breakdown ---
    s += card(20, 60, 760, 150)
    s += subtitle_badge(30, 68, "Морфемный разбор слова", PRIMARY)

    # Word: ПЕРЕЛЕСОВЫЙ
    # Breakdown: пере-лес-ов-ый
    word_parts = [
        ("пере-", "приставка", 40, PRIMARY),
        ("лес", "корень", 160, GREEN),
        ("-ов-", "суффикс", 280, ACCENT),
        ("-ый", "окончание", 390, ACCENT2),
    ]

    # Draw the full word
    s += text_el(250, 118, "пере  +  лес  +  ов  +  ый", 26, TEXT_DARK, weight="bold")

    # Morpheme boxes below
    for i, (part, label, x, color) in enumerate(word_parts):
        bx = 50 + i * 185
        s += f'<rect x="{bx}" y="132" width="160" height="36" rx="6" fill="{color}" opacity="0.15" stroke="{color}" stroke-width="1.5"/>'
        s += text_el(bx + 80, 155, f"{part}", 16, color, weight="bold")
        s += text_el(bx + 80, 176, label, 12, color, weight="bold")

    # Connecting lines
    # Main morpheme descriptions
    s += card(20, 220, 760, 180)
    s += subtitle_badge(30, 228, "Морфемы русского языка", PRIMARY_DARK)

    morphemes = [
        ("Корень", "Главная значимая часть слова.\nОднокоренные слова: лес, лесной, лесник", GREEN),
        ("Приставка", "Стоит перед корнем.\nОбразует новые слова: бежать → прибежать", PRIMARY),
        ("Суффикс", "Стоит после корня.\nОбразует новые слова: лес → лесной", ACCENT),
        ("Окончание", "Изменяемая часть слова.\nСвязывает слова: лес, леса, лесу", ACCENT2),
    ]

    for i, (name, desc, color) in enumerate(morphemes):
        bx = 30 + i * 188
        s += f'<rect x="{bx}" y="260" width="175" height="128" rx="8" fill="{BG_CARD}" stroke="{color}" stroke-width="1.5"/>'
        s += f'<rect x="{bx}" y="260" width="175" height="28" rx="8" fill="{color}"/>'
        s += text_el(bx + 87, 280, name, 14, "#FFFFFF", weight="bold")
        # Description lines
        lines = desc.split("\n")
        for j, line in enumerate(lines):
            s += text_left(bx + 8, 302 + j * 18, line, 11, TEXT_DARK)

    # --- Word formation example ---
    s += card(20, 410, 760, 80)
    s += subtitle_badge(30, 418, "Способы словообразования", ACCENT)

    methods = [
        ("Приставочный", "читать → прочитать", PRIMARY),
        ("Суффиксальный", "дом → домик", GREEN),
        ("Приставочно-\nсуффиксальный", "под + окно → подоконник", ACCENT),
    ]
    for i, (method, example, color) in enumerate(methods):
        bx = 30 + i * 253
        s += f'<rect x="{bx}" y="452" width="240" height="30" rx="6" fill="{color}" opacity="0.12"/>'
        s += text_left(bx + 8, 462, method.replace("\n", " "), 12, color, weight="bold")
        s += text_left(bx + 8, 478, example, 12, TEXT_DARK)

    # --- Bottom tip ---
    s += card(20, 500, 760, 90)
    s += subtitle_badge(30, 508, "Запомни!", RED)
    tips = [
        "• Нулевое окончание — есть в слове, но не выражено звуком: столØ, читалØ",
        "• Основа — часть слова без окончания: пере-лес-ов- (ый — окончание)",
        "• Соединительная гласная о/е — не морфема: лес-о-руб, земл-е-мер",
    ]
    for i, tip in enumerate(tips):
        s += text_left(40, 544 + i * 18, tip, 12, TEXT_DARK)

    s += svg_footer()
    return s


# ═══════════════════════════════════════════════════════════
# LESSON 3: Причастие как часть речи
# ═══════════════════════════════════════════════════════════
def lesson_3():
    s = svg_header()
    s += f'<rect width="{W}" height="{H}" fill="{BG}"/>'
    s += title_bar(0, "Причастие как часть речи")
    s += lesson_number_badge(3)

    # --- Definition ---
    s += card(20, 60, 760, 55)
    s += text_el(W // 2, 92, "Причастие — особая форма глагола, которая обозначает признак предмета по действию", 14, TEXT_DARK, weight="normal")

    # --- Properties: Verb + Adjective ---
    s += card(20, 125, 370, 175)
    s += subtitle_badge(30, 133, "Свойства глагола", PRIMARY)
    verb_props = [
        "• Вид: совершенный / несовершенный",
        "• Возвратность: -ся / -сь",
        "• Время: настоящее / прошедшее",
        "• Переходность",
    ]
    for i, prop in enumerate(verb_props):
        s += text_left(40, 170 + i * 22, prop, 13, TEXT_DARK)

    s += card(410, 125, 370, 175)
    s += subtitle_badge(420, 133, "Свойства прилагательного", ACCENT)
    adj_props = [
        "• Род: мужской / женский / средний",
        "• Число: единственное / множественное",
        "• Падеж (полная форма)",
        "• Полная и краткая формы",
    ]
    for i, prop in enumerate(adj_props):
        s += text_left(430, 170 + i * 22, prop, 13, TEXT_DARK)

    # --- Types of participles ---
    s += card(20, 310, 760, 155)
    s += subtitle_badge(30, 318, "Виды причастий", PRIMARY_DARK)

    # Actual participles
    s += f'<rect x="35" y="356" width="355" height="96" rx="8" fill="{HIGHLIGHT}" stroke="{PRIMARY}" stroke-width="1.5"/>'
    s += text_el(212, 376, "Действительные причастия", 14, PRIMARY_DARK, weight="bold")
    s += text_left(50, 396, "Обозначают признак предмета,", 12, TEXT_DARK)
    s += text_left(50, 412, "который сам совершает действие", 12, TEXT_DARK)
    s += text_left(50, 434, "читающий мальчик, решившая задачу", 12, PRIMARY_DARK)

    # Passive participles
    s += f'<rect x="410" y="356" width="355" height="96" rx="8" fill="#EEF2FF" stroke="{ACCENT}" stroke-width="1.5"/>'
    s += text_el(587, 376, "Страдательные причастия", 14, ACCENT, weight="bold")
    s += text_left(425, 396, "Обозначают признак предмета,", 12, TEXT_DARK)
    s += text_left(425, 412, "который испытывает действие", 12, TEXT_DARK)
    s += text_left(425, 434, "читаемая книга, решённая задача", 12, ACCENT)

    # --- Formation scheme ---
    s += card(20, 475, 760, 115)
    s += subtitle_badge(30, 483, "Образование причастий", GREEN)

    # Scheme table
    s += f'<rect x="35" y="516" width="350" height="24" rx="4" fill="{PRIMARY}" opacity="0.1"/>'
    s += text_left(42, 533, "Настоящее время", 12, PRIMARY_DARK, "bold")
    s += text_left(250, 533, "Прошедшее время", 12, PRIMARY_DARK, "bold")

    s += f'<rect x="35" y="542" width="175" height="20" fill="{HIGHLIGHT}"/>'
    s += text_left(42, 556, "читать → читающ-", 11, TEXT_DARK)
    s += f'<rect x="215" y="542" width="170" height="20" fill="{HIGHLIGHT}"/>'
    s += text_left(222, 556, "читать → читавш-", 11, TEXT_DARK)

    s += f'<rect x="35" y="564" width="175" height="20" fill="{BG_CARD}"/>'
    s += text_left(42, 578, "решить → решащ-", 11, TEXT_DARK)
    s += f'<rect x="215" y="564" width="170" height="20" fill="{BG_CARD}"/>'
    s += text_left(222, 578, "решить → решивш-", 11, TEXT_DARK)

    # Right side examples
    s += text_left(420, 516, "Вопросы к причастию:", 12, PRIMARY_DARK, "bold")
    s += text_left(420, 536, "какой? какая? какое? какие?", 12, TEXT_DARK)
    s += text_left(420, 556, "что делающий? что сделавший?", 12, TEXT_DARK)
    s += text_left(420, 576, "что делаемый? что сделанный?", 12, TEXT_DARK)

    s += svg_footer()
    return s


# ═══════════════════════════════════════════════════════════
# LESSON 4: Правописание причастий
# ═══════════════════════════════════════════════════════════
def lesson_4():
    s = svg_header()
    s += f'<rect width="{W}" height="{H}" fill="{BG}"/>'
    s += title_bar(0, "Правописание причастий")
    s += lesson_number_badge(4)

    # --- Suffix rules ---
    s += card(20, 60, 760, 155)
    s += subtitle_badge(30, 68, "Гласные в суффиксах причастий", PRIMARY)

    # Present tense
    s += f'<rect x="35" y="100" width="355" height="100" rx="8" fill="{HIGHLIGHT}" stroke="{PRIMARY}" stroke-width="1"/>'
    s += text_el(212, 118, "Настоящее время", 14, PRIMARY_DARK, weight="bold")
    s += text_left(45, 138, "I спр. → -ущ-/-ющ-  (читающий)", 12, TEXT_DARK)
    s += text_left(45, 156, "II спр. → -ащ-/-ящ-  (кричащий)", 12, TEXT_DARK)
    s += text_left(45, 176, "Страд.: -ом-/-ем- / -им-", 12, TEXT_MED)

    # Past tense
    s += f'<rect x="410" y="100" width="355" height="100" rx="8" fill="#EEF2FF" stroke="{ACCENT}" stroke-width="1"/>'
    s += text_el(587, 118, "Прошедшее время", 14, ACCENT, weight="bold")
    s += text_left(420, 138, "Перед -вш- та же гласная, что", 12, TEXT_DARK)
    s += text_left(420, 156, "в инфинитиве перед -ть:", 12, TEXT_DARK)
    s += text_left(420, 176, "видеть → видевший; клеить → клеивший", 12, TEXT_MED)

    # --- Н and НН in participles ---
    s += card(20, 225, 760, 220)
    s += subtitle_badge(30, 233, "Н и НН в причастиях и отглагольных прилагательных", RED)

    # NN conditions
    s += f'<rect x="35" y="268" width="355" height="165" rx="8" fill="#FEF2F2" stroke="{RED}" stroke-width="1.5"/>'
    s += text_el(212, 286, "НН пишется:", 15, RED, weight="bold")
    nn_rules = [
        "1. Есть приставка (кроме не-):",
        "   связа**нн**ый, выкрашен**н**ый",
        "2. Есть суффикс -ова-/-ева-/-ирова-:",
        "   балова**нн**ый, маринова**нн**ый",
        "3. Есть зависимые слова:",
        "   крашен**н**ый (краской) забор",
        "4. Образовано от бесприст. глагола сов. вида:",
        "   решённый (решить — сов. вид)",
    ]
    for i, rule in enumerate(nn_rules):
        s += text_left(45, 304 + i * 16, rule, 11, TEXT_DARK)

    # N conditions
    s += f'<rect x="410" y="268" width="355" height="165" rx="8" fill="{HIGHLIGHT}" stroke="{GREEN}" stroke-width="1.5"/>'
    s += text_el(587, 286, "Н пишется:", 15, GREEN, weight="bold")
    n_rules = [
        "1. Нет приставки, нет -ова-/-ева-,",
        "   нет зависимых слов:",
        "   крашеный забор",
        "2. Образовано от глагола несов. вида:",
        "   брошенный → бросить (сов.) — НН",
        "   но: ране**н**ый (ранить — несов.) — Н",
        "3. Исключения:",
        "   названый брат, посажёный отец,",
        "   смышлёный мальчик, конченый человек",
    ]
    for i, rule in enumerate(n_rules):
        s += text_left(420, 304 + i * 16, rule, 11, TEXT_DARK)

    # --- Не с причастиями ---
    s += card(20, 455, 760, 135)
    s += subtitle_badge(30, 463, "НЕ с причастиями", ACCENT2)

    s += f'<rect x="35" y="496" width="355" height="82" rx="8" fill="#FFFBEB" stroke="{ACCENT2}" stroke-width="1"/>'
    s += text_el(212, 514, "Слитно", 14, ACCENT2, weight="bold")
    s += text_left(45, 534, "• Без НЕ не употребляется: ненавидевший", 11, TEXT_DARK)
    s += text_left(45, 550, "• Нет зависимых слов, нет противопоставления:", 11, TEXT_DARK)
    s += text_left(45, 566, "  непрочитанная книга", 11, TEXT_MED)

    s += f'<rect x="410" y="496" width="355" height="82" rx="8" fill="#FEF2F2" stroke="{RED}" stroke-width="1"/>'
    s += text_el(587, 514, "Раздельно", 14, RED, weight="bold")
    s += text_left(420, 534, "• Есть зависимые слова:", 11, TEXT_DARK)
    s += text_left(420, 550, "  не прочитанная учеником книга", 11, TEXT_MED)
    s += text_left(420, 566, "• Есть противопоставление с а:", 11, TEXT_DARK)
    s += text_left(420, 582, "  не прочитанная, а просмотренная книга", 11, TEXT_MED)

    s += svg_footer()
    return s


# ═══════════════════════════════════════════════════════════
# LESSON 5: Деепричастие как часть речи
# ═══════════════════════════════════════════════════════════
def lesson_5():
    s = svg_header()
    s += f'<rect width="{W}" height="{H}" fill="{BG}"/>'
    s += title_bar(0, "Деепричастие как часть речи")
    s += lesson_number_badge(5)

    # --- Definition ---
    s += card(20, 60, 760, 60)
    s += text_el(W // 2, 84, "Деепричастие — особая форма глагола, которая обозначает добавочное действие", 14, TEXT_DARK)
    s += text_el(W // 2, 104, "и совмещает свойства глагола и наречия", 14, PRIMARY_DARK, weight="bold")

    # --- Properties ---
    s += card(20, 130, 370, 150)
    s += subtitle_badge(30, 138, "Свойства глагола", PRIMARY)
    verb_props = [
        "• Вид: совершенный / несовершенный",
        "• Переходность / непереходность",
        "• Возвратность: -ся / -сь",
        "• Управляет тем же падежом,",
        "  что и глагол: читать (что?) книгу",
        "  → читая книгу",
    ]
    for i, prop in enumerate(verb_props):
        s += text_left(40, 172 + i * 18, prop, 12, TEXT_DARK)

    s += card(410, 130, 370, 150)
    s += subtitle_badge(420, 138, "Свойства наречия", ACCENT)
    adv_props = [
        "• Не изменяется (не спрягается,",
        "  не склоняется)",
        "• В предложении — обстоятельство",
        "• Отвечает на вопрос: что делая?",
        "  что сделав?",
        "• Зависит от глагола-сказуемого",
    ]
    for i, prop in enumerate(adv_props):
        s += text_left(430, 172 + i * 18, prop, 12, TEXT_DARK)

    # --- Formation ---
    s += card(20, 290, 760, 115)
    s += subtitle_badge(30, 298, "Образование деепричастий", GREEN)

    # Imperfective
    s += f'<rect x="35" y="332" width="355" height="60" rx="8" fill="{HIGHLIGHT}" stroke="{PRIMARY}" stroke-width="1"/>'
    s += text_el(212, 350, "Несовершенный вид", 13, PRIMARY_DARK, weight="bold")
    s += text_left(45, 368, "читать → читая, рисовать → рисуя, думать → думая", 11, TEXT_DARK)
    s += text_left(45, 384, "Основа наст. вр. + -а/-я", 11, TEXT_MED)

    # Perfective
    s += f'<rect x="410" y="332" width="355" height="60" rx="8" fill="#EEF2FF" stroke="{ACCENT}" stroke-width="1"/>'
    s += text_el(587, 350, "Совершенный вид", 13, ACCENT, weight="bold")
    s += text_left(420, 368, "прочитать → прочитав, решить → решив", 11, TEXT_DARK)
    s += text_left(420, 384, "Основа прош. вр. + -в / -вши / -ши", 11, TEXT_MED)

    # --- Function in sentence ---
    s += card(20, 415, 760, 80)
    s += subtitle_badge(30, 423, "Деепричастный оборот", ACCENT2)

    s += text_left(35, 455, "Деепричастный оборот = деепричастие + зависимые слова", 13, TEXT_DARK, weight="bold")
    s += text_left(35, 475, "Мальчик, читая книгу, сидел у окна.    [читая книгу] — деепричастный оборот", 12, TEXT_MED)
    s += text_left(35, 492, "На письме выделяется запятыми!", 12, RED, weight="bold")

    # --- Important rules ---
    s += card(20, 505, 760, 85)
    s += subtitle_badge(30, 513, "Важно!", RED)
    important = [
        "• Деепричастие и сказуемое должны обозначать действия одного и того же лица:",
        "  Правильно: Читая книгу, я отдыхал.    Неправильно: Читая книгу, шёл дождь.",
        "• НЕ с деепричастиями пишется раздельно: не прочитав, не думая",
    ]
    for i, line in enumerate(important):
        color = RED if "Неправильно" in line else TEXT_DARK
        s += text_left(40, 543 + i * 17, line, 11, color)

    s += svg_footer()
    return s


# ═══════════════════════════════════════════════════════════
# LESSON 6: Наречие как часть речи
# ═══════════════════════════════════════════════════════════
def lesson_6():
    s = svg_header()
    s += f'<rect width="{W}" height="{H}" fill="{BG}"/>'
    s += title_bar(0, "Наречие как часть речи")
    s += lesson_number_badge(6)

    # --- Definition ---
    s += card(20, 60, 760, 50)
    s += text_el(W // 2, 90, "Наречие — неизменяемая часть речи, обозначающая признак действия, предмета или другого признака", 14, TEXT_DARK)

    # --- Questions ---
    s += card(20, 120, 760, 50)
    s += subtitle_badge(30, 128, "Вопросы наречий", PRIMARY)
    s += text_el(W // 2, 155, "как? куда? откуда? где? когда? зачем? почему? насколько?", 14, PRIMARY_DARK, weight="bold")

    # --- Categories of meaning ---
    s += card(20, 180, 760, 240)
    s += subtitle_badge(30, 188, "Разряды наречий по значению", PRIMARY_DARK)

    categories = [
        ("Образа действия", "как?", "быстро, медленно, громко, тихо, внимательно", PRIMARY),
        ("Меры и степени", "насколько? в какой степени?", "очень, слишком, почти, вдвое, совсем", ACCENT),
        ("Места", "где? куда? откуда?", "здесь, там, внизу, вперёд, издалека", GREEN),
        ("Времени", "когда? с каких пор? до каких пор?", "сегодня, вчера, утром, давно, всегда", BLUE),
        ("Причины", "почему? отчего?", "сослепу, сгоряча, поневоле, случайно", ACCENT2),
        ("Цели", "зачем? для чего?", "нарочно, специально, назло, напоказ", RED),
    ]

    for i, (cat, questions, examples, color) in enumerate(categories):
        y_pos = 218 + i * 32
        bg = HIGHLIGHT if i % 2 == 0 else BG_CARD
        s += f'<rect x="35" y="{y_pos}" width="730" height="30" rx="4" fill="{bg}"/>'
        # Category name
        s += f'<rect x="38" y="{y_pos + 3}" width="{len(cat) * 8 + 12}" height="24" rx="12" fill="{color}"/>'
        s += text_el(38 + (len(cat) * 8 + 12) // 2, y_pos + 20, cat, 11, "#FFFFFF", weight="bold")
        # Questions
        s += text_left(200, y_pos + 20, questions, 11, TEXT_MED)
        # Examples
        s += text_left(430, y_pos + 20, examples, 11, TEXT_DARK)

    # --- Degrees of comparison ---
    s += card(20, 430, 760, 80)
    s += subtitle_badge(30, 438, "Степени сравнения наречий", GREEN)

    s += text_left(40, 470, "Сравнительная: быстрее, громче, более внимательно", 12, TEXT_DARK)
    s += text_left(40, 488, "Превосходная: быстрее всех, громче всего", 12, TEXT_DARK)
    s += text_left(450, 470, "Образуется от наречий на -о/-е", 12, TEXT_MED)
    s += text_left(450, 488, "Сравнит. = прил. сравнит. форма!", 12, RED, weight="bold")

    # --- Syntax role ---
    s += card(20, 520, 760, 70)
    s += subtitle_badge(30, 528, "Синтаксическая роль", ACCENT)
    s += text_left(40, 556, "• Обстоятельство: Мальчик бежал быстро. (как? — быстро)", 12, TEXT_DARK)
    s += text_left(40, 574, "• Определение (редко): Пальто навырост. (какое? — навырост)", 12, TEXT_MED)

    s += svg_footer()
    return s


# ═══════════════════════════════════════════════════════════
# LESSON 7: Правописание наречий
# ═══════════════════════════════════════════════════════════
def lesson_7():
    s = svg_header()
    s += f'<rect width="{W}" height="{H}" fill="{BG}"/>'
    s += title_bar(0, "Правописание наречий")
    s += lesson_number_badge(7)

    # --- -О and -Е suffixes ---
    s += card(20, 60, 760, 130)
    s += subtitle_badge(30, 68, "Буквы О и Е на конце наречий", PRIMARY)

    s += f'<rect x="35" y="100" width="355" height="78" rx="8" fill="{HIGHLIGHT}" stroke="{PRIMARY}" stroke-width="1.5"/>'
    s += text_el(212, 118, "-О- после твёрдых согласных", 14, PRIMARY_DARK, weight="bold")
    s += text_left(45, 138, "крепко, громко, быстро, часто", 13, TEXT_DARK)
    s += text_left(45, 156, "Прил. крепкий → крепк-о", 12, TEXT_MED)

    s += f'<rect x="410" y="100" width="355" height="78" rx="8" fill="#EEF2FF" stroke="{ACCENT}" stroke-width="1.5"/>'
    s += text_el(587, 118, "-Е- после мягких согласных", 14, ACCENT, weight="bold")
    s += text_left(420, 138, "свеже, горячо, певуче, общий→обоче", 13, TEXT_DARK)
    s += text_left(420, 156, "Прил. свежий → свеж-е", 12, TEXT_MED)

    # --- Н and НН ---
    s += card(20, 200, 760, 120)
    s += subtitle_badge(30, 208, "Н и НН в наречиях на -о/-е", RED)

    s += f'<rect x="35" y="240" width="355" height="68" rx="8" fill="#FEF2F2" stroke="{RED}" stroke-width="1.5"/>'
    s += text_el(212, 258, "НН — от прил. с НН", 14, RED, weight="bold")
    s += text_left(45, 278, "взволнова**нн**ый → взволнова**нн**о", 12, TEXT_DARK)
    s += text_left(45, 294, "удивлённый → удивлённо", 12, TEXT_DARK)

    s += f'<rect x="410" y="240" width="355" height="68" rx="8" fill="{HIGHLIGHT}" stroke="{GREEN}" stroke-width="1.5"/>'
    s += text_el(587, 258, "Н — от прил. с Н", 14, GREEN, weight="bold")
    s += text_left(420, 278, "весёлый → весело (весёл → весел + о)", 12, TEXT_DARK)
    s += text_left(420, 294, "мудрый → мудро", 12, TEXT_DARK)

    # --- Hyphenated adverbs ---
    s += card(20, 330, 760, 140)
    s += subtitle_badge(30, 338, "Дефис в наречиях", ACCENT2)

    hyphen_rules = [
        ("по- + -ому/-ему", "по-новому, по-русски, по-летнему", PRIMARY),
        ("во- + -ых/-их", "во-первых, в-третьих, в-седьмых", ACCENT),
        ("кое-/ -то/ -либо/ -нибудь", "кое-где, где-то, когда-либо, куда-нибудь", GREEN),
        ("Сложение синонимов", "еле-еле, мало-мальски, тихо-смирно", BLUE),
    ]

    for i, (rule, examples, color) in enumerate(hyphen_rules):
        y_pos = 368 + i * 24
        bg = HIGHLIGHT if i % 2 == 0 else BG_CARD
        s += f'<rect x="35" y="{y_pos}" width="730" height="22" rx="4" fill="{bg}"/>'
        s += text_left(42, y_pos + 16, rule, 12, color, weight="bold")
        s += text_left(280, y_pos + 16, examples, 12, TEXT_DARK)

    # --- NOT/N rules ---
    s += card(20, 480, 760, 110)
    s += subtitle_badge(30, 488, "НЕ и НИ в наречиях", PRIMARY_DARK)

    s += f'<rect x="35" y="520" width="355" height="58" rx="8" fill="{HIGHLIGHT}" stroke="{PRIMARY}" stroke-width="1"/>'
    s += text_el(212, 538, "НЕ — отрицание", 13, PRIMARY_DARK, weight="bold")
    s += text_left(45, 556, "негде, некуда, неоткуда, незачем", 12, TEXT_DARK)
    s += text_left(45, 572, "нет условий для действия", 11, TEXT_MED)

    s += f'<rect x="410" y="520" width="355" height="58" rx="8" fill="#FEF2F2" stroke="{RED}" stroke-width="1"/>'
    s += text_el(587, 538, "НИ — усиление отрицания", 13, RED, weight="bold")
    s += text_left(420, 556, "нигде, никуда, ниоткуда, никак", 12, TEXT_DARK)
    s += text_left(420, 572, "в предложении с глаголом + НЕ", 11, TEXT_MED)

    s += svg_footer()
    return s


# ═══════════════════════════════════════════════════════════
# MAIN: Generate all SVGs and validate
# ═══════════════════════════════════════════════════════════

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    generators = [
        (1, "Фонетика и графика", lesson_1),
        (2, "Состав слова", lesson_2),
        (3, "Причастие как часть речи", lesson_3),
        (4, "Правописание причастий", lesson_4),
        (5, "Деепричастие как часть речи", lesson_5),
        (6, "Наречие как часть речи", lesson_6),
        (7, "Правописание наречий", lesson_7),
    ]

    results = []
    for n, title, gen_func in generators:
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{n}.svg")
        svg_content = gen_func()

        # Write SVG
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)

        # Validate with xml.etree.ElementTree
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            # Check basic structure
            assert root.tag == "{http://www.w3.org/2000/svg}svg" or root.tag == "svg", f"Root tag is {root.tag}"
            assert root.get("width") == "800", f"Width is {root.get('width')}"
            assert root.get("height") == "600", f"Height is {root.get('height')}"
            file_size = os.path.getsize(filepath)
            results.append(f"✅ lesson-{n}.svg — {title} — VALID ({file_size} bytes)")
        except ET.ParseError as e:
            results.append(f"❌ lesson-{n}.svg — {title} — XML ERROR: {e}")
        except Exception as e:
            results.append(f"❌ lesson-{n}.svg — {title} — ERROR: {e}")

    print("\n" + "=" * 60)
    print("GRADE 7 RUSSIAN LANGUAGE SVG GENERATION RESULTS")
    print("=" * 60)
    for r in results:
        print(r)
    print("=" * 60)
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Total files generated: {len(generators)}")

    # Summary counts
    valid = sum(1 for r in results if r.startswith("✅"))
    invalid = sum(1 for r in results if r.startswith("❌"))
    print(f"Valid: {valid} | Invalid: {invalid}")


if __name__ == "__main__":
    main()
