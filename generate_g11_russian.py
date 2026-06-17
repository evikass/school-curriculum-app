#!/usr/bin/env python3
"""Generate 12 detailed SVG files for Grade 11 Russian Language lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade11/russian"

# Color scheme
PRIMARY = "#D32F2F"
BG_LIGHT = "#FFEBEE"
BG_WHITE = "#FFFFFF"
TEXT_DARK = "#212121"
TEXT_MEDIUM = "#424242"
TEXT_LIGHT = "#757575"
ACCENT_DARK = "#B71C1C"
ACCENT_LIGHT = "#EF9A9A"
BORDER_COLOR = "#D32F2F"

LESSONS = [
    {
        "num": 1,
        "title": "Сложное предложение",
        "subtitle": "Русский язык — Урок 1",
        "content": {
            "definition": "Сложное предложение — предложение, состоящее\nиз двух и более грамматических основ.",
            "types": [
                ("Сложносочинённое (ССП)", "Основы связаны\nсоюзами: и, а, но, или"),
                ("Сложноподчинённое (СПП)", "Основы связаны\nподчинительными союзами"),
                ("Бессоюзное (БСП)", "Основы связаны\nпо смыслу и интонации"),
            ],
            "example": "[Ветер дул], и [дождь шёл]. — ССП\n[Я знаю], (что завтра экзамен). — СПП\n[Лес шумел], [дождь лил]. — БСП",
            "rule": "Запятая ставится между частями\nсложного предложения!",
        }
    },
    {
        "num": 2,
        "title": "Пунктуация в СПП",
        "subtitle": "Русский язык — Урок 2",
        "content": {
            "definition": "СПП — сложное предложение, в котором\nодна часть подчинена другой союзом\nили союзным словом.",
            "types": [
                ("Придаточное определительное", "Какой? Слова: который,\nкакой, чей, что"),
                ("Придаточное изъяснительное", "Падежные вопросы.\nСоюзы: что, чтобы, ли"),
                ("Придаточное обстоятельственное", "Где? Когда? Почему?\nЗачем? Несмотря на что?"),
            ],
            "example": "[Мы подошли], (где рос дуб).\n[Я уверен], (что он придёт).\n[День был жаркий], (так что\nмы пошли на реку).",
            "rule": "Придаточное отделяется запятой.\nСоюз входит в придаточную часть!",
        }
    },
    {
        "num": 3,
        "title": "Прямая и косвенная речь",
        "subtitle": "Русский язык — Урок 3",
        "content": {
            "definition": "Прямая речь — точная передача чужой\nречи. Косвенная речь — передача\nчужой речи в виде придаточного.",
            "types": [
                ("А: «П!»", "Слова автора —\nпрямая речь после"),
                ("«П», — а.", "Прямая речь —\nслова автора после"),
                ("А: «П,» — а.", "Разрыв прямой\nречи словами автора"),
            ],
            "example": "Он сказал: «Я приду завтра.»\n«Я приду завтра», — сказал он.\nОн сказал косвенно,\nчто придёт завтра.",
            "rule": "Прямая речь в кавычках!\nКосвенная: союз что/чтобы +\nизменение лица глагола.",
        }
    },
    {
        "num": 4,
        "title": "Н и НН в разных частях речи",
        "subtitle": "Русский язык — Урок 4",
        "content": {
            "definition": "Правописание Н и НН — одно из\nсамых сложных правил орфографии.\nЗависит от части речи и способа\nсловообразования.",
            "types": [
                ("НН в прилагательных", "основа на Н + Н = НН\n(длиННый, стаNNый)\nот глаголов на -овать"),
                ("Н в прилагательных", "В непроизводных прилаг.\n(синий, зелёный, юный,\nсвиной, рьяный, пряный)"),
                ("Н/НН в причастиях", "НН: есть приставка, -ова-,\nзависимые слова.\nН: нет приставки и зав. слов"),
            ],
            "example": "Длинный (длин+н), утренний,\nвязаный свитер, но:\nсвязанный (с приставкой),\nжареный → зажаренный",
            "rule": "Исключения: ветреный, масленый,\nсолёный, зелёный, юный,\nсвиной, пряный, рьяный, багряный.",
        }
    },
    {
        "num": 5,
        "title": "Правописание приставок",
        "subtitle": "Русский язык — Урок 5",
        "content": {
            "definition": "Приставки делятся на группы по\nправилам написания: неизменяемые,\nна -З/-С, ПРЕ-/ПРИ-.",
            "types": [
                ("Неизменяемые", "над-, под-, об-, от-,\nперед-, сверх-, меж-,\nв-, на-, за-, с-"),
                ("На -З / -С", "Раз-/рас-, без-/бес-,\nвоз-/вос-, из-/ис-.\nПеред глухой — С!"),
                ("ПРЕ- / ПРИ-", "ПРЕ-: = очень, = пере-\nПРИ-: приближение,\nприсоединение, близость"),
            ],
            "example": "Бесконечный (к — глух.),\nно: беззвёздный (з — звонк.)\nПреодолеть = перe-,\nПриехать = приближение",
            "rule": "З/С: перед глухой согласной\nпишется С, перед звонкой — З.\nПРЕ/ПРИ: смотри значение!",
        }
    },
    {
        "num": 6,
        "title": "Правописание глагольных форм",
        "subtitle": "Русский язык — Урок 6",
        "content": {
            "definition": "Глагольные формы: инфинитив,\nпрош. время, причастия, деепри-\nчастия. Орфограммы: -ТСЯ/-ТЬСЯ,\nсуффиксы, личные окончания.",
            "types": [
                ("-ТСЯ / -ТЬСЯ", "ТЬСЯ — инфинитив (что делать?)\nТСЯ — 3 лицо (что делает?)\nУчится / Учиться"),
                ("Суффиксы прош. времени", "-Л- перед окончанием.\nМёрз, грёб, лёг —\nбез Л перед -л-"),
                ("Спряжение", "I спр.: -ешь, -ет, -ем, -ете\nII спр.: -ишь, -ит, -им, -ите\nИсключ.: гнать, держать, ..."),
            ],
            "example": "Он учится (что делает?) в школе.\nОн хочет учиться (что делать?).\nII спр.: видеть, обидеть,\nненавидеть, зависеть, терпеть",
            "rule": "ТСЯ/ТЬСЯ: поставь вопрос!\nСпряжение: по неопр. форме,\nкроме 11 исключений II спр.",
        }
    },
    {
        "num": 7,
        "title": "Текст как единица речи",
        "subtitle": "Русский язык — Урок 7",
        "content": {
            "definition": "Текст — последовательность предло-\nжений, связанных по смыслу и\nграмматически. Основные признаки:\nцельность, связность, завершённость.",
            "types": [
                ("Средства связи", "Лексический повтор,\nместоимения, союзы,\nсинонимы, антонимы"),
                ("Цепная связь", "Каждое следующее предлож.\nсвязано с предыдущим:\nА → В, В → С, С → D"),
                ("Параллельная связь", "Предложения связаны с одним:\nА → В, А → С, А → D\nВсе к одному的主题"),
            ],
            "example": "Цепная: Лес шумел. В лесу\nбыло темно. Темнота пугала.\nПараллельная: Лес шумел.\nВетер крепчал. Дождь лил.",
            "rule": "Текст = тема + идея + структура.\nАбзац — часть текста,\nвыделяющая микротему.",
        }
    },
    {
        "num": 8,
        "title": "Стили речи",
        "subtitle": "Русский язык — Урок 8",
        "content": {
            "definition": "Стиль речи — система языковых\nсредств, используемая в определён-\nной сфере общения.",
            "types": [
                ("Научный", "Точность, логичность,\nтерминология, сложный\nсинтаксис"),
                ("Официально-деловой", "Стандартность, клише,\nканцеляризмы, точность,\nбезэмоциональность"),
                ("Публицистический", "Воздействие, оценка,\nобразность, экспрессия,\nречевые стандарты"),
            ],
            "example": "Научный: «Гипотеза подтверждена\nэкспериментально.»\nДеловой: «Договор вступает\nв силу...»\nПублиц.: «Как же так вышло?!»",
            "rule": "5 стилей: научный, деловой,\nпублицистический,\nхудожественный,\nразговорный.",
        }
    },
    {
        "num": 9,
        "title": "Изобразительно-выразительные средства",
        "subtitle": "Русский язык — Урок 9",
        "content": {
            "definition": "Тропы и фигуры речи — средства\nхудожественной выразительности,\nделающие речь образной.",
            "types": [
                ("Тропы", "Метафора — скрытое сравн.\nЭпитет — образное определ.\nОлицетворение — неживое\nкак живое"),
                ("Сравнение", "Сопоставление двух предметов:\nкак, словно, будто, точно.\n«Лес как храм»"),
                ("Фигуры речи", "Инверсия — обратный порядок.\nАнафора — единоначатие.\nАнтитеза — противопоставл.\nГрадация — усиление"),
            ],
            "example": "Метафора: «золотые руки»\nЭпитет: «мармеладное небо»\nОлицетв.: «ветер плачет»\nАнтитеза: «Преступление и\nнаказание»",
            "rule": "Тропы — на основе переносного\nзначения. Фигуры — особый\nпорядок или построение.\nМетонимия, гипербола, литота.",
        }
    },
    {
        "num": 10,
        "title": "Нормы литературного языка",
        "subtitle": "Русский язык — Урок 10",
        "content": {
            "definition": "Литературная норма — правило\nобразцового использования языко-\nвых средств. Нормы обязательны\nдля официального общения.",
            "types": [
                ("Орфоэпические", "Произносительные нормы:\nквАртал, звОнит, катАлог,\nтОрты, шАрфы"),
                ("Грамматические", "Морфологические и\nсинтаксические нормы:\nнет туфель (не туфлей!),\nоценивать (не оценивать)"),
                ("Лексические", "Правильное употребление\nслов: надеть одежду,\nодеть ребёнка; оплатить\nза проезд → оплатить проезд"),
            ],
            "example": "Правильно: звонИт, красИвее,\nдоговор, средства, инженеры.\nНеправильно: звОнит,\nкрасивЕе, дОговор",
            "rule": "Орфоэпия — правильное\nпроизношение и ударение.\nГрамматика — правильные\nформы и конструкции.",
        }
    },
    {
        "num": 11,
        "title": "Подготовка к сочинению",
        "subtitle": "Русский язык — Урок 11",
        "content": {
            "definition": "Сочинение — письменная работа,\nдемонстрирующая умение формули-\nровать мысль и аргументировать\nпозицию.",
            "types": [
                ("Структура сочинения", "Вступление →\nПостановка проблемы →\nКомментарий →\nПозиция автора → Своя"),
                ("Аргументация", "1. Литературный пример\n2. Исторический/жизненный\n3. Связь с позиций автора\nМинимум 2 аргумента!"),
                ("Клише", "«Автор поднимает проблему...»\n«Согласен с автором...»\n«Правильность своей точки\nзрения могу доказать...»"),
            ],
            "example": "1. Формулируем проблему текста\n2. Комментируем (2 примера)\n3. Позиция автора: ...\n4. Моя позиция: согласен/нет\n5. Аргумент из литературы\n6. Вывод",
            "rule": "Объём: минимум 150 слов.\nОбязательно: проблема,\nкомментарий, позиция автора,\nсвоя позиция, аргументы.",
        }
    },
    {
        "num": 12,
        "title": "Подготовка к ЕГЭ",
        "subtitle": "Русский язык — Урок 12",
        "content": {
            "definition": "ЕГЭ по русскому языку — обязатель-\nный экзамен. Состоит из двух частей:\nтестовой (26 заданий) и сочинения.",
            "types": [
                ("Часть 1: Тест", "Задания 1-26:\nОрфография, пунктуация,\nграмматика, речь,\nработа с текстом"),
                ("Часть 2: Сочинение", "Задание 27:\nПроблема текста,\nкомментарий, позиция,\nсвоя позиция, аргументы"),
                ("Критерии сочинения", "K1 — формулировка проблемы\nK2 — комментарий\nK3 — позиция автора\nK4-K6 — своя позиция\nМакс. 24 балла за сочинение"),
            ],
            "example": "Орфография: Н/НН, слитно/раздельно\nПунктуация: запятые при СПП,\nвводных словах, обособлении\nГрамматика: синт. нормы,\nморфологические нормы",
            "rule": "Максимальный балл: 58.\nМинимальный: 36.\nВремя: 3,5 часа.\nСовет: решайте типовые задания!",
        }
    },
]


def escape_xml(text):
    """Escape special XML characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def build_svg(lesson):
    """Build a detailed SVG string for a lesson."""
    num = lesson["num"]
    title = lesson["title"]
    subtitle = lesson["subtitle"]
    c = lesson["content"]

    svg_parts = []
    svg_parts.append('<?xml version="1.0" encoding="UTF-8"?>')
    svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">')

    # Definitions for gradients
    svg_parts.append('  <defs>')
    svg_parts.append(f'    <linearGradient id="headerGrad{num}" x1="0%" y1="0%" x2="100%" y2="0%">')
    svg_parts.append(f'      <stop offset="0%" stop-color="{PRIMARY}"/>')
    svg_parts.append(f'      <stop offset="100%" stop-color="{ACCENT_DARK}"/>')
    svg_parts.append('    </linearGradient>')
    svg_parts.append(f'    <linearGradient id="boxGrad{num}" x1="0%" y1="0%" x2="0%" y2="100%">')
    svg_parts.append(f'      <stop offset="0%" stop-color="#FFFFFF"/>')
    svg_parts.append(f'      <stop offset="100%" stop-color="{BG_LIGHT}"/>')
    svg_parts.append('    </linearGradient>')
    svg_parts.append('  </defs>')

    # Background
    svg_parts.append(f'  <rect width="500" height="350" rx="12" ry="12" fill="{BG_LIGHT}"/>')

    # Border
    svg_parts.append(f'  <rect x="1.5" y="1.5" width="497" height="347" rx="12" ry="12" '
                     f'fill="none" stroke="{BORDER_COLOR}" stroke-width="2.5"/>')

    # Header bar
    svg_parts.append(f'  <rect x="3" y="3" width="494" height="52" rx="10" ry="10" fill="url(#headerGrad{num})"/>')
    svg_parts.append(f'  <rect x="3" y="30" width="494" height="25" fill="url(#headerGrad{num})"/>')

    # Lesson number badge
    svg_parts.append(f'  <circle cx="32" cy="29" r="18" fill="{BG_WHITE}" opacity="0.9"/>')
    svg_parts.append(f'  <text x="32" y="34" font-family="Arial, sans-serif" font-size="16" font-weight="bold" '
                     f'fill="{PRIMARY}" text-anchor="middle">{num}</text>')

    # Title
    svg_parts.append(f'  <text x="58" y="24" font-family="Arial, sans-serif" font-size="15" font-weight="bold" '
                     f'fill="#FFFFFF">{escape_xml(title)}</text>')

    # Subtitle
    svg_parts.append(f'  <text x="58" y="42" font-family="Arial, sans-serif" font-size="10" '
                     f'fill="#FFCDD2">{escape_xml(subtitle)}</text>')

    # Decorative line under header
    svg_parts.append(f'  <line x1="15" y1="60" x2="485" y2="60" stroke="{ACCENT_LIGHT}" stroke-width="0.5" opacity="0.6"/>')

    # Definition box
    def_y = 68
    svg_parts.append(f'  <rect x="15" y="{def_y}" width="470" height="52" rx="6" ry="6" '
                     f'fill="#FFFFFF" stroke="{PRIMARY}" stroke-width="1" opacity="0.95"/>')
    svg_parts.append(f'  <rect x="15" y="{def_y}" width="5" height="52" rx="2" ry="0" fill="{PRIMARY}"/>')

    # Definition label
    svg_parts.append(f'  <text x="28" y="{def_y + 13}" font-family="Arial, sans-serif" font-size="8" '
                     f'font-weight="bold" fill="{PRIMARY}">ОПРЕДЕЛЕНИЕ</text>')

    # Definition text
    def_lines = c["definition"].split("\n")
    for i, line in enumerate(def_lines):
        svg_parts.append(f'  <text x="28" y="{def_y + 26 + i * 12}" font-family="Arial, sans-serif" '
                         f'font-size="10" fill="{TEXT_DARK}">{escape_xml(line)}</text>')

    # Three type boxes
    box_y = 128
    box_width = 148
    box_height = 80
    box_gap = 13
    box_xs = [15, 15 + box_width + box_gap, 15 + 2 * (box_width + box_gap)]

    type_colors = [PRIMARY, "#C62828", "#B71C1C"]

    for i, (t_title, t_desc) in enumerate(c["types"]):
        bx = box_xs[i]
        # Box background
        svg_parts.append(f'  <rect x="{bx}" y="{box_y}" width="{box_width}" height="{box_height}" '
                         f'rx="6" ry="6" fill="#FFFFFF" stroke="{type_colors[i]}" stroke-width="1" opacity="0.95"/>')

        # Colored top strip
        svg_parts.append(f'  <rect x="{bx}" y="{box_y}" width="{box_width}" height="18" '
                         f'rx="6" ry="6" fill="{type_colors[i]}" opacity="0.15"/>')
        svg_parts.append(f'  <rect x="{bx}" y="{box_y + 12}" width="{box_width}" height="6" '
                         f'fill="{type_colors[i]}" opacity="0.15"/>')

        # Type title
        svg_parts.append(f'  <text x="{bx + 7}" y="{box_y + 13}" font-family="Arial, sans-serif" '
                         f'font-size="8" font-weight="bold" fill="{type_colors[i]}">{escape_xml(t_title)}</text>')

        # Type description
        desc_lines = t_desc.split("\n")
        for j, line in enumerate(desc_lines):
            svg_parts.append(f'  <text x="{bx + 7}" y="{box_y + 28 + j * 11}" font-family="Arial, sans-serif" '
                             f'font-size="9" fill="{TEXT_MEDIUM}">{escape_xml(line)}</text>')

    # Connecting arrows between boxes
    for i in range(2):
        ax = box_xs[i] + box_width + 1
        svg_parts.append(f'  <line x1="{ax}" y1="{box_y + box_height // 2}" '
                         f'x2="{ax + box_gap - 2}" y2="{box_y + box_height // 2}" '
                         f'stroke="{ACCENT_LIGHT}" stroke-width="1.5" stroke-dasharray="2,2"/>')

    # Example box
    ex_y = 216
    svg_parts.append(f'  <rect x="15" y="{ex_y}" width="280" height="72" rx="6" ry="6" '
                     f'fill="#FFFFFF" stroke="{ACCENT_LIGHT}" stroke-width="1" opacity="0.95"/>')

    # Example label
    svg_parts.append(f'  <rect x="15" y="{ex_y}" width="60" height="14" rx="3" ry="3" fill="{PRIMARY}" opacity="0.85"/>')
    svg_parts.append(f'  <text x="45" y="{ex_y + 11}" font-family="Arial, sans-serif" font-size="8" '
                     f'font-weight="bold" fill="#FFFFFF" text-anchor="middle">ПРИМЕР</text>')

    # Example text
    ex_lines = c["example"].split("\n")
    for i, line in enumerate(ex_lines):
        svg_parts.append(f'  <text x="25" y="{ex_y + 26 + i * 11}" font-family="Arial, sans-serif" '
                         f'font-size="9" fill="{TEXT_DARK}">{escape_xml(line)}</text>')

    # Rule box (right side)
    rule_y = 216
    svg_parts.append(f'  <rect x="305" y="{rule_y}" width="180" height="72" rx="6" ry="6" '
                     f'fill="#FFFFFF" stroke="{PRIMARY}" stroke-width="1.2" opacity="0.95"/>')
    svg_parts.append(f'  <rect x="305" y="{rule_y}" width="180" height="14" rx="6" ry="6" '
                     f'fill="{PRIMARY}" opacity="0.12"/>')
    svg_parts.append(f'  <rect x="305" y="{rule_y + 8}" width="180" height="6" fill="{PRIMARY}" opacity="0.12"/>')

    # Rule label
    svg_parts.append(f'  <text x="312" y="{rule_y + 11}" font-family="Arial, sans-serif" font-size="8" '
                     f'font-weight="bold" fill="{PRIMARY}">⚡ ПРАВИЛО</text>')

    # Rule text
    rule_lines = c["rule"].split("\n")
    for i, line in enumerate(rule_lines):
        svg_parts.append(f'  <text x="312" y="{rule_y + 26 + i * 11}" font-family="Arial, sans-serif" '
                         f'font-size="9" fill="{TEXT_DARK}">{escape_xml(line)}</text>')

    # Decorative element - small dots
    for dx in range(0, 470, 20):
        svg_parts.append(f'  <circle cx="{15 + dx}" cy="296" r="1" fill="{ACCENT_LIGHT}" opacity="0.5"/>')

    # Separator line
    svg_parts.append(f'  <line x1="15" y1="300" x2="485" y2="300" stroke="{ACCENT_LIGHT}" stroke-width="0.8" opacity="0.4"/>')

    # Key concept highlights (small badges)
    badge_y = 305
    badge_items = [f"Урок {num}", title.split()[0][:10]]
    badge_x = 15
    for item in badge_items:
        bw = len(item) * 6 + 14
        svg_parts.append(f'  <rect x="{badge_x}" y="{badge_y}" width="{bw}" height="16" rx="8" ry="8" '
                         f'fill="{PRIMARY}" opacity="0.1"/>')
        svg_parts.append(f'  <text x="{badge_x + bw // 2}" y="{badge_y + 12}" font-family="Arial, sans-serif" '
                         f'font-size="8" fill="{PRIMARY}" text-anchor="middle">{escape_xml(item)}</text>')
        badge_x += bw + 8

    # Decorative book icon
    svg_parts.append(f'  <rect x="455" y="{badge_y}" width="14" height="16" rx="2" ry="2" fill="none" '
                     f'stroke="{PRIMARY}" stroke-width="1" opacity="0.4"/>')
    svg_parts.append(f'  <line x1="462" y1="{badge_y}" x2="462" y2="{badge_y + 16}" '
                     f'stroke="{PRIMARY}" stroke-width="1" opacity="0.4"/>')

    # Footer
    svg_parts.append(f'  <text x="250" y="340" font-family="Arial, sans-serif" font-size="9" '
                     f'fill="{TEXT_LIGHT}" text-anchor="middle">Русский язык · 11 класс</text>')

    # Small decorative accent at bottom
    svg_parts.append(f'  <rect x="220" y="344" width="60" height="2" rx="1" ry="1" fill="{PRIMARY}" opacity="0.3"/>')

    svg_parts.append('</svg>')

    return "\n".join(svg_parts)


def validate_svg(svg_string):
    """Validate that SVG string is proper XML."""
    try:
        ET.fromstring(svg_string)
        return True, "Valid XML"
    except ET.ParseError as e:
        return False, str(e)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    generated = 0
    validated = 0
    errors = []

    for lesson in LESSONS:
        num = lesson["num"]
        filename = f"lesson{num}.svg"
        filepath = os.path.join(OUTPUT_DIR, filename)

        svg_content = build_svg(lesson)

        # Validate before writing
        is_valid, msg = validate_svg(svg_content)
        if not is_valid:
            errors.append(f"{filename}: Validation FAILED - {msg}")
            print(f"  ✗ {filename} - XML validation FAILED: {msg}")
            continue

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)

        generated += 1
        validated += 1
        print(f"  ✓ {filename} - Generated & Validated ({len(svg_content)} bytes)")

    # Double-check: re-read and validate all files
    print("\n--- Re-validation check ---")
    for i in range(1, 13):
        filepath = os.path.join(OUTPUT_DIR, f"lesson{i}.svg")
        if not os.path.exists(filepath):
            errors.append(f"lesson{i}.svg: File missing!")
            print(f"  ✗ lesson{i}.svg - MISSING")
            continue
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        is_valid, msg = validate_svg(content)
        if not is_valid:
            errors.append(f"lesson{i}.svg: Re-validation FAILED - {msg}")
            print(f"  ✗ lesson{i}.svg - Re-validation FAILED: {msg}")
        else:
            print(f"  ✓ lesson{i}.svg - Re-validated OK ({len(content)} bytes)")

    print(f"\n{'='*50}")
    print(f"Generated: {generated}/12")
    print(f"Validated: {validated}/12")
    print(f"Errors: {len(errors)}")
    if errors:
        print("Error details:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("All SVGs generated and validated successfully!")
    print(f"Output: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
