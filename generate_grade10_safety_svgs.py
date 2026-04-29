#!/usr/bin/env python3
"""Generate 10 detailed SVG files for Grade 10 Safety/OBZh lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade10/safety"

# Colors
PRIMARY = "#E65100"
BG = "#FFF3E0"
DANGER = "#C62828"
SAFE = "#2E7D32"
DARK = "#37474F"
ACCENT = "#FF8F00"
LIGHT_ORANGE = "#FFE0B2"
LIGHT_GREEN = "#E8F5E9"
LIGHT_RED = "#FFEBEE"
LIGHT_BLUE = "#E3F2FD"
BLUE = "#1565C0"

LESSONS = [
    {
        "num": 1,
        "title": "Личная безопасность в повседневной жизни",
        "filename": "lesson1-personal-safety.svg",
        "content": {
            "left_title": "Правила безопасности",
            "left_items": [
                ("⚠", "Будьте бдительны на улице", DANGER),
                ("✓", "Избегайте безлюдных мест в темноте", SAFE),
                ("⚠", "Не разглашайте личные данные", DANGER),
                ("✓", "Сообщайте близким о маршруте", SAFE),
                ("⚠", "Осторожно с незнакомцами", DANGER),
            ],
            "right_title": "Телефоны экстренных служб",
            "right_items": [
                ("112", "Единый номер"),
                ("101", "Пожарная служба"),
                ("102", "Полиция"),
                ("103", "Скорая помощь"),
                ("104", "Газовая служба"),
            ],
            "bottom_title": "Алгоритм: если вам угрожает опасность",
            "bottom_steps": [
                "1. Оцените ситуацию",
                "2. Привлеките внимание окружающих",
                "3. Позвоните 112",
                "4. Дождитесь помощи",
            ],
        }
    },
    {
        "num": 2,
        "title": "Самозащита и правовые аспекты",
        "filename": "lesson2-self-defense-law.svg",
        "content": {
            "left_title": "Право на необходимую оборону",
            "left_items": [
                ("⚖", "Ст. 37 УК РФ — необходимая оборона", BLUE),
                ("✓", "Защита от опасного посягательства", SAFE),
                ("✓", "Не превышение пределов обороны", SAFE),
                ("⚠", "Превышение — уголовная ответственность", DANGER),
                ("⚖", "Ст. 39 УК РФ — крайняя необходимость", BLUE),
            ],
            "right_title": "Правила самозащиты",
            "right_items": [
                ("1", "Избегайте конфликта"),
                ("2", "Привлеките внимание людей"),
                ("3", "Используйте подручные средства"),
                ("4", "Защита = отражение нападения"),
                ("5", "Вызывайте полицию: 102"),
            ],
            "bottom_title": "Ключевое различие",
            "bottom_steps": [
                "ОБОРОНА — отражение реальной угрозы",
                "ПРЕВЫШЕНИЕ — несоразмерный вред атакующему",
            ],
        }
    },
    {
        "num": 3,
        "title": "Причины пожаров и профилактика",
        "filename": "lesson3-fire-causes-prevention.svg",
        "content": {
            "left_title": "Основные причины пожаров",
            "left_items": [
                ("⚠", "Неосторожное обращение с огнём", DANGER),
                ("⚠", "Нарушение правил электробезопасности", DANGER),
                ("⚠", "Неисправность отопительных приборов", DANGER),
                ("⚠", "Детские шалости с огнём", DANGER),
                ("⚠", "Нарушение правил при сварке", DANGER),
            ],
            "right_title": "Профилактика пожаров",
            "right_items": [
                ("✓", "Не оставляйте плиту без присмотра", SAFE),
                ("✓", "Проверяйте электропроводку", SAFE),
                ("✓", "Не перегружайте розетки", SAFE),
                ("✓", "Храните спички в недоступном месте", SAFE),
                ("✓", "Установите дымовые датчики", SAFE),
            ],
            "bottom_title": "Огнетушитель: типы и применение",
            "bottom_steps": [
                "ОП (порошковый) — твердые горючие, жидкости, газы",
                "ОУ (углекислотный) — электроустановки под напряжением",
            ],
        }
    },
    {
        "num": 4,
        "title": "Действия при пожаре",
        "filename": "lesson4-fire-actions.svg",
        "content": {
            "left_title": "Если пожар начался",
            "left_items": [
                ("1", "Немедленно звоните 101 или 112"),
                ("2", "Оцените масштаб возгорания"),
                ("3", "Эвакуируйтесь по плану"),
                ("4", "Не пользуйтесь лифтом!"),
                ("5", "Прикройте рот влажной тканью"),
            ],
            "right_title": "Если пути отрезаны",
            "right_items": [
                ("⚠", "Не паникуйте!", DANGER),
                ("✓", "Уйдите на балкон / к окну", SAFE),
                ("✓", "Закройте дверь, щели — мокрой тканью", SAFE),
                ("✓", "Подавайте сигналы спасателям", SAFE),
                ("⚠", "Не прыгайте из окон выше 3-го этажа", DANGER),
            ],
            "bottom_title": "Правило: дым опаснее огня!",
            "bottom_steps": [
                "Опуститесь на четвереньки — внизу есть чистый воздух",
                "Двигайтесь к выходу вдоль стены",
            ],
        }
    },
    {
        "num": 5,
        "title": "Чрезвычайные ситуации природного характера",
        "filename": "lesson5-natural-emergencies.svg",
        "content": {
            "left_title": "Виды ЧС природного характера",
            "left_items": [
                ("🌊", "Наводнения", BLUE),
                ("🌋", "Землетрясения", ACCENT),
                ("🌪", "Ураганы, смерчи", DANGER),
                ("⛰", "Оползни, сели", DARK),
                ("🔥", "Лесные пожары", DANGER),
            ],
            "right_title": "Действия при землетрясении",
            "right_items": [
                ("1", "В здании — встаньте в дверном проёме"),
                ("2", "Держитесь подальше от окон"),
                ("3", "На улице — вдали от зданий"),
                ("4", "Не пользуйтесь лифтом"),
                ("5", "После толчков — выйдите из здания"),
            ],
            "bottom_title": "Раннее предупреждение — залог выживания",
            "bottom_steps": [
                "Следите за прогнозами МЧС и штормовыми предупреждениями",
                "Заранее подготовьте «тревожный чемоданчик»",
            ],
        }
    },
    {
        "num": 6,
        "title": "Чрезвычайные ситуации техногенного характера",
        "filename": "lesson6-technogenic-emergencies.svg",
        "content": {
            "left_title": "Виды техногенных ЧС",
            "left_items": [
                ("☢", "Аварии на АЭС / радиация", DANGER),
                ("⚗", "Химические аварии (АХОВ)", ACCENT),
                ("💥", "Взрывы и обрушения зданий", DANGER),
                ("🔥", "Пожары на предприятиях", DANGER),
                ("🚰", "Загрязнение воды и почвы", DARK),
            ],
            "right_title": "Действия при химической аварии",
            "right_items": [
                ("1", "Закройте окна и двери"),
                ("2", "Защитите органы дыхания"),
                ("3", "Включите TV / радио для информации"),
                ("4", "Не выходите без указаний МЧС"),
                ("5", "При эвакуации — маршрут против ветра"),
            ],
            "bottom_title": "Защита при радиации",
            "bottom_steps": [
                "Укрытие в помещении (стены снижают излучение)",
                "Йодная профилактика — по указанию специалистов",
            ],
        }
    },
    {
        "num": 7,
        "title": "Оценка состояния и сердечно-лёгочная реанимация",
        "filename": "lesson7-cpr.svg",
        "content": {
            "left_title": "Признаки клинической смерти",
            "left_items": [
                ("⚠", "Отсутствие сознания", DANGER),
                ("⚠", "Отсутствие дыхания", DANGER),
                ("⚠", "Отсутствие пульса на сонной артерии", DANGER),
                ("⚠", "Расширенные зрачки", DANGER),
                ("⏱", "Время: 4–6 минут до биологической смерти", DANGER),
            ],
            "right_title": "Алгоритм СЛР (30:2)",
            "right_items": [
                ("1", "Убедитесь в безопасности"),
                ("2", "Проверьте реакцию и дыхание"),
                ("3", "Вызовите скорую: 103"),
                ("4", "30 нажатий на грудную клетку"),
                ("5", "2 вдоха (голова запрокинута)"),
            ],
            "bottom_title": "Параметры компрессий",
            "bottom_steps": [
                "Глубина: 5–6 см  |  Частота: 100–120 в мин  |  Точка: центр грудины",
            ],
        }
    },
    {
        "num": 8,
        "title": "Первая помощь при кровотечениях и травмах",
        "filename": "lesson8-bleeding-trauma.svg",
        "content": {
            "left_title": "Виды кровотечений",
            "left_items": [
                ("🔴", "Артериальное — алая кровь, фонтан", DANGER),
                ("🟤", "Венозное — тёмная кровь, течёт", ACCENT),
                ("🔴", "Капиллярное — кровь сочится", PRIMARY),
            ],
            "right_title": "Первая помощь",
            "right_items": [
                ("1", "Артериальное: жгут выше раны (+ записка)"),
                ("2", "Венозное: давящая повязка"),
                ("3", "Капиллярное: обработка + пластырь"),
                ("4", "При переломе: обездвижить (шина)"),
                ("5", "При ожоге: охладить водой 10–15 мин"),
            ],
            "bottom_title": "Правила наложения жгута",
            "bottom_steps": [
                "Время: зимой ≤1 ч, летом ≤1.5 ч  |  Обязательно запишите время!",
                "Ослабляйте жгут каждые 30 мин на 5 мин",
            ],
        }
    },
    {
        "num": 9,
        "title": "Электробезопасность",
        "filename": "lesson9-electrical-safety.svg",
        "content": {
            "left_title": "Опасности электричества",
            "left_items": [
                ("⚡", "Поражение током (≥0.1 А — смертельно)", DANGER),
                ("⚡", "Электроожоги", DANGER),
                ("⚡", "Пожар от КЗ и перегрузки", DANGER),
                ("⚠", "Влажность снижает сопротивление", DANGER),
                ("⚠", "Не прикасайтесь к пострадавшему!", DANGER),
            ],
            "right_title": "Правила электробезопасности",
            "right_items": [
                ("✓", "Не трогайте провода мокрыми руками", SAFE),
                ("✓", "Не перегружайте розетки", SAFE),
                ("✓", "Заземляйте электроприборы", SAFE),
                ("✓", "Отключайте приборы уходя", SAFE),
                ("✓", "Используйте УЗО (устройство защиты)", SAFE),
            ],
            "bottom_title": "Если человека ударило током",
            "bottom_steps": [
                "1. Отключите источник  2. Не касайтесь голыми руками",
                "3. Откиньте провод сухим непроводящим предметом  4. Вызовите 103",
            ],
        }
    },
    {
        "num": 10,
        "title": "Дорожная безопасность",
        "filename": "lesson10-road-safety.svg",
        "content": {
            "left_title": "Правила для пешеходов",
            "left_items": [
                ("✓", "Переходите по зебре / подземному переходу", SAFE),
                ("✓", "Смотрите налево, потом направо", SAFE),
                ("⚠", "Не переходите на красный сигнал", DANGER),
                ("⚠", "Не играйте возле проезжей части", DANGER),
                ("✓", "Носите светоотражатели в темноте", SAFE),
            ],
            "right_title": "Правила для велосипедистов",
            "right_items": [
                ("1", "Шлем — обязательно!"),
                ("2", "Двигайтесь по велодорожке"),
                ("3", "Сигнализируйте повороты рукой"),
                ("4", "Свет: фара + катафоты"),
                ("5", "До 14 лет — тротуар, не дорога"),
            ],
            "bottom_title": "Статистика: главные причины ДТП",
            "bottom_steps": [
                "1. Переход в неположенном месте  2. Невнимательность",
                "3. Превышение скорости  4. Управление в нетрезвом виде",
            ],
        }
    },
]


def escape_xml(text):
    """Escape special XML characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def generate_svg(lesson):
    """Generate SVG content for a lesson."""
    num = lesson["num"]
    title = lesson["title"]
    content = lesson["content"]
    filename = lesson["filename"]

    svg_parts = []

    def w(s=""):
        svg_parts.append(s)

    w(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">')

    # Defs
    w('  <defs>')
    w(f'    <linearGradient id="hdr{num}" x1="0%" y1="0%" x2="100%" y2="0%">')
    w(f'      <stop offset="0%" style="stop-color:#E65100;stop-opacity:1"/>')
    w(f'      <stop offset="100%" style="stop-color:#FF8F00;stop-opacity:1"/>')
    w(f'    </linearGradient>')
    w(f'    <linearGradient id="bg{num}" x1="0%" y1="0%" x2="0%" y2="100%">')
    w(f'      <stop offset="0%" style="stop-color:#FFF3E0;stop-opacity:1"/>')
    w(f'      <stop offset="100%" style="stop-color:#FFE0B2;stop-opacity:1"/>')
    w(f'    </linearGradient>')
    w(f'    <filter id="shadow{num}" x="-2%" y="-2%" width="104%" height="104%">')
    w(f'      <feDropShadow dx="1" dy="1" stdDeviation="2" flood-color="#000" flood-opacity="0.1"/>')
    w(f'    </filter>')
    w('  </defs>')

    # Background
    w(f'  <rect width="500" height="350" fill="url(#bg{num})"/>')

    # Rounded border
    w(f'  <rect x="2" y="2" width="496" height="346" rx="12" ry="12" fill="none" stroke="#E65100" stroke-width="2.5" opacity="0.6"/>')

    # Header background
    w(f'  <rect x="3" y="3" width="494" height="42" rx="10" ry="10" fill="url(#hdr{num})"/>')
    w(f'  <rect x="3" y="35" width="494" height="10" fill="url(#hdr{num})"/>')

    # Header text
    w(f'  <text x="250" y="20" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{escape_xml(title)}</text>')
    w(f'  <text x="250" y="36" font-family="Arial, sans-serif" font-size="10" fill="#FFF3E0" text-anchor="middle">ОБЖ — Урок {num}</text>')

    # Lesson number badge
    w(f'  <circle cx="28" cy="24" r="14" fill="#FFFFFF" opacity="0.25"/>')
    w(f'  <text x="28" y="28" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{num}</text>')

    # Content area - two columns
    y_start = 52

    # LEFT COLUMN
    left_x = 12
    left_w = 230
    left_title = content["left_title"]
    left_items = content["left_items"]

    # Left box background
    w(f'  <rect x="{left_x}" y="{y_start}" width="{left_w}" height="{12 + 18 + len(left_items) * 22 + 6}" rx="8" ry="8" fill="#FFFFFF" opacity="0.7" filter="url(#shadow{num})"/>')

    # Left title
    w(f'  <rect x="{left_x + 4}" y="{y_start + 3}" width="{left_w - 8}" height="18" rx="4" ry="4" fill="#E65100" opacity="0.15"/>')
    w(f'  <text x="{left_x + left_w // 2}" y="{y_start + 16}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#E65100" text-anchor="middle">{escape_xml(left_title)}</text>')

    # Left items
    item_y = y_start + 28
    for item in left_items:
        if len(item) == 3:
            icon, text, color = item
        else:
            icon, text = item
            color = DANGER
        # Color indicator dot
        w(f'  <circle cx="{left_x + 14}" cy="{item_y - 3}" r="4" fill="{color}" opacity="0.8"/>')
        # Item text
        w(f'  <text x="{left_x + 24}" y="{item_y}" font-family="Arial, sans-serif" font-size="9" fill="#37474F">{escape_xml(text)}</text>')
        item_y += 22

    # RIGHT COLUMN
    right_x = 252
    right_w = 236
    right_title = content["right_title"]
    right_items = content["right_items"]

    # Right box background
    w(f'  <rect x="{right_x}" y="{y_start}" width="{right_w}" height="{12 + 18 + len(right_items) * 22 + 6}" rx="8" ry="8" fill="#FFFFFF" opacity="0.7" filter="url(#shadow{num})"/>')

    # Right title
    w(f'  <rect x="{right_x + 4}" y="{y_start + 3}" width="{right_w - 8}" height="18" rx="4" ry="4" fill="#E65100" opacity="0.15"/>')
    w(f'  <text x="{right_x + right_w // 2}" y="{y_start + 16}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#E65100" text-anchor="middle">{escape_xml(right_title)}</text>')

    # Right items
    item_y = y_start + 28
    for i, item in enumerate(right_items):
        if len(item) == 3:
            icon, text, color = item
        else:
            icon, text = item
            color = SAFE
        # Step number / icon indicator
        if icon.isdigit():
            w(f'  <circle cx="{right_x + 14}" cy="{item_y - 3}" r="6" fill="{color}" opacity="0.2"/>')
            w(f'  <text x="{right_x + 14}" y="{item_y}" font-family="Arial, sans-serif" font-size="8" font-weight="bold" fill="{color}" text-anchor="middle">{icon}</text>')
        else:
            w(f'  <circle cx="{right_x + 14}" cy="{item_y - 3}" r="4" fill="{color}" opacity="0.8"/>')
        # Item text
        w(f'  <text x="{right_x + 26}" y="{item_y}" font-family="Arial, sans-serif" font-size="9" fill="#37474F">{escape_xml(text)}</text>')
        item_y += 22

    # BOTTOM SECTION
    bottom_title = content["bottom_title"]
    bottom_steps = content["bottom_steps"]

    # Calculate bottom Y based on which column is taller
    left_h = 12 + 18 + len(left_items) * 22 + 6
    right_h = 12 + 18 + len(right_items) * 22 + 6
    bottom_y = y_start + max(left_h, right_h) + 8

    # Bottom box
    bottom_h = 14 + 16 + len(bottom_steps) * 18 + 8
    w(f'  <rect x="12" y="{bottom_y}" width="476" height="{bottom_h}" rx="8" ry="8" fill="#FFFFFF" opacity="0.7" filter="url(#shadow{num})"/>')

    # Bottom accent bar
    w(f'  <rect x="12" y="{bottom_y}" width="5" height="{bottom_h}" rx="2" ry="0" fill="#E65100" opacity="0.7"/>')

    # Bottom title
    w(f'  <text x="250" y="{bottom_y + 14}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#C62828" text-anchor="middle">{escape_xml(bottom_title)}</text>')

    # Bottom steps
    step_y = bottom_y + 30
    for step in bottom_steps:
        # Step text with colored marker
        w(f'  <rect x="24" y="{step_y - 8}" width="452" height="15" rx="3" ry="3" fill="#E65100" opacity="0.06"/>')
        w(f'  <text x="30" y="{step_y}" font-family="Arial, sans-serif" font-size="9" fill="#37474F">{escape_xml(step)}</text>')
        step_y += 18

    # Add decorative icon based on lesson number
    icon_x = 470
    icon_y = 24

    # FOOTER
    footer_y = 338
    w(f'  <line x1="15" y1="{footer_y - 4}" x2="485" y2="{footer_y - 4}" stroke="#E65100" stroke-width="0.5" opacity="0.3"/>')
    w(f'  <text x="250" y="{footer_y}" font-family="Arial, sans-serif" font-size="8" fill="#9E9E9E" text-anchor="middle">Основы безопасности · 10 класс</text>')

    w('</svg>')

    return "\n".join(svg_parts)


def add_lesson_icons(svg_content, lesson_num):
    """Add lesson-specific decorative icons/illustrations to the SVG."""
    # Insert decorative elements before closing </svg>
    insert_pos = svg_content.rfind('</svg>')

    icon_svg = ""

    if lesson_num == 1:  # Personal safety - shield icon
        icon_svg = '''
  <!-- Shield icon -->
  <g transform="translate(440, 60)">
    <path d="M20,5 L35,12 L35,28 C35,38 20,48 20,48 C20,48 5,38 5,28 L5,12 Z" fill="#E65100" opacity="0.15" stroke="#E65100" stroke-width="1"/>
    <text x="20" y="32" font-family="Arial, sans-serif" font-size="16" fill="#E65100" text-anchor="middle">&#x1F6E1;</text>
  </g>'''

    elif lesson_num == 2:  # Self-defense & law - scales icon
        icon_svg = '''
  <!-- Scales of justice -->
  <g transform="translate(440, 58)">
    <line x1="20" y1="5" x2="20" y2="35" stroke="#1565C0" stroke-width="2" opacity="0.6"/>
    <line x1="5" y1="15" x2="35" y2="15" stroke="#1565C0" stroke-width="2" opacity="0.6"/>
    <polygon points="5,15 0,28 10,28" fill="#1565C0" opacity="0.2" stroke="#1565C0" stroke-width="1"/>
    <polygon points="35,15 30,28 40,28" fill="#1565C0" opacity="0.2" stroke="#1565C0" stroke-width="1"/>
    <circle cx="20" cy="5" r="3" fill="#1565C0" opacity="0.5"/>
  </g>'''

    elif lesson_num == 3:  # Fire causes - fire icon
        icon_svg = '''
  <!-- Fire icon -->
  <g transform="translate(442, 58)">
    <path d="M20,5 C25,15 35,20 30,35 C28,40 22,42 20,45 C18,42 12,40 10,35 C5,20 15,15 20,5Z" fill="#E65100" opacity="0.2" stroke="#E65100" stroke-width="1"/>
    <path d="M20,18 C23,24 28,27 25,36 C24,38 21,40 20,42 C19,40 16,38 15,36 C12,27 17,24 20,18Z" fill="#FF8F00" opacity="0.3"/>
  </g>'''

    elif lesson_num == 4:  # Fire actions - fire extinguisher
        icon_svg = '''
  <!-- Fire extinguisher icon -->
  <g transform="translate(443, 58)">
    <rect x="12" y="12" width="16" height="32" rx="4" fill="#C62828" opacity="0.2" stroke="#C62828" stroke-width="1"/>
    <rect x="16" y="5" width="8" height="10" rx="2" fill="#C62828" opacity="0.3"/>
    <line x1="20" y1="5" x2="32" y2="2" stroke="#C62828" stroke-width="1.5" opacity="0.5"/>
    <circle cx="20" cy="28" r="3" fill="#FFFFFF" opacity="0.4"/>
  </g>'''

    elif lesson_num == 5:  # Natural emergencies - tornado/earthquake
        icon_svg = '''
  <!-- Earthquake/wave icon -->
  <g transform="translate(440, 60)">
    <path d="M5,25 L12,15 L19,28 L26,10 L33,22 L40,18" fill="none" stroke="#C62828" stroke-width="2" opacity="0.4"/>
    <rect x="5" y="35" width="35" height="3" rx="1" fill="#37474F" opacity="0.2"/>
    <path d="M8,38 L8,48 M20,38 L20,48 M32,38 L32,48" stroke="#37474F" stroke-width="1" opacity="0.15"/>
  </g>'''

    elif lesson_num == 6:  # Technogenic - factory/radiation
        icon_svg = '''
  <!-- Radiation icon -->
  <g transform="translate(445, 60)">
    <circle cx="20" cy="22" r="18" fill="none" stroke="#C62828" stroke-width="1" opacity="0.3"/>
    <circle cx="20" cy="22" r="5" fill="#C62828" opacity="0.3"/>
    <path d="M20,17 L14,6" stroke="#C62828" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/>
    <path d="M24,19 L34,14" stroke="#C62828" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/>
    <path d="M24,25 L34,30" stroke="#C62828" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/>
    <path d="M20,27 L14,38" stroke="#C62828" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/>
    <path d="M16,25 L6,30" stroke="#C62828" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/>
    <path d="M16,19 L6,14" stroke="#C62828" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/>
  </g>'''

    elif lesson_num == 7:  # CPR - heart icon
        icon_svg = '''
  <!-- Heart / CPR icon -->
  <g transform="translate(443, 58)">
    <path d="M20,38 C5,28 0,15 8,8 C14,3 20,10 20,10 C20,10 26,3 32,8 C40,15 35,28 20,38Z" fill="#C62828" opacity="0.15" stroke="#C62828" stroke-width="1"/>
    <line x1="12" y1="20" x2="18" y2="20" stroke="#C62828" stroke-width="2" opacity="0.4"/>
    <line x1="18" y1="20" x2="22" y2="14" stroke="#C62828" stroke-width="2" opacity="0.4"/>
    <line x1="22" y1="14" x2="26" y2="26" stroke="#C62828" stroke-width="2" opacity="0.4"/>
    <line x1="26" y1="26" x2="28" y2="20" stroke="#C62828" stroke-width="2" opacity="0.4"/>
  </g>'''

    elif lesson_num == 8:  # Bleeding - bandage/cross icon
        icon_svg = '''
  <!-- Medical cross icon -->
  <g transform="translate(445, 60)">
    <rect x="8" y="8" width="24" height="34" rx="3" fill="#FFFFFF" opacity="0.5" stroke="#C62828" stroke-width="1"/>
    <rect x="16" y="14" width="8" height="22" rx="1" fill="#C62828" opacity="0.3"/>
    <rect x="11" y="19" width="18" height="8" rx="1" fill="#C62828" opacity="0.3"/>
  </g>'''

    elif lesson_num == 9:  # Electrical safety - lightning bolt
        icon_svg = '''
  <!-- Lightning bolt icon -->
  <g transform="translate(445, 58)">
    <polygon points="25,2 10,22 20,22 15,42 35,18 24,18 30,2" fill="#FF8F00" opacity="0.25" stroke="#FF8F00" stroke-width="1"/>
  </g>'''

    elif lesson_num == 10:  # Road safety - traffic light
        icon_svg = '''
  <!-- Traffic light icon -->
  <g transform="translate(450, 60)">
    <rect x="8" y="5" width="14" height="38" rx="4" fill="#37474F" opacity="0.3"/>
    <circle cx="15" cy="14" r="4" fill="#C62828" opacity="0.6"/>
    <circle cx="15" cy="24" r="4" fill="#FF8F00" opacity="0.4"/>
    <circle cx="15" cy="34" r="4" fill="#2E7D32" opacity="0.4"/>
  </g>'''

    return svg_content[:insert_pos] + icon_svg + "\n" + svg_content[insert_pos:]


def validate_svg(filepath):
    """Validate SVG as proper XML."""
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        # Check it's an SVG
        if "svg" in root.tag.lower():
            return True, "Valid SVG XML"
        else:
            return False, f"Root element is not SVG: {root.tag}"
    except ET.ParseError as e:
        return False, f"XML Parse Error: {str(e)}"
    except Exception as e:
        return False, f"Error: {str(e)}"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    success_count = 0
    fail_count = 0
    results = []

    for lesson in LESSONS:
        filename = lesson["filename"]
        filepath = os.path.join(OUTPUT_DIR, filename)

        # Generate SVG content
        svg_content = generate_svg(lesson)

        # Add lesson-specific decorative icons
        svg_content = add_lesson_icons(svg_content, lesson["num"])

        # Write file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)

        # Validate
        is_valid, message = validate_svg(filepath)

        if is_valid:
            success_count += 1
            results.append(f"  ✓ {filename} — VALID")
        else:
            fail_count += 1
            results.append(f"  ✗ {filename} — INVALID: {message}")

        # Also verify file size
        file_size = os.path.getsize(filepath)
        results[-1] += f" ({file_size} bytes)"

    print("=" * 60)
    print("Grade 10 Safety/OBZh SVG Generation Results")
    print("=" * 60)
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Total lessons: {len(LESSONS)}")
    print(f"Successfully generated: {success_count}")
    print(f"Failed: {fail_count}")
    print("-" * 60)
    for r in results:
        print(r)
    print("-" * 60)

    # List all generated files
    print(f"\nFiles in output directory:")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        if f.endswith(".svg"):
            fp = os.path.join(OUTPUT_DIR, f)
            print(f"  {f} ({os.path.getsize(fp)} bytes)")

    if fail_count == 0:
        print(f"\n✓ All {success_count} SVG files generated and validated successfully!")
    else:
        print(f"\n✗ {fail_count} file(s) failed validation!")

    return success_count


if __name__ == "__main__":
    main()
