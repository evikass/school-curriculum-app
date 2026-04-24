#!/usr/bin/env python3
"""Generate SVG images for grade 11 economy lessons."""

import os
import html

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade11/economy"

LESSONS = [
    (1, "Мировое хозяйство"),
    (2, "Сравнительные преимущества"),
    (3, "Теория Хекшера-Олина"),
    (4, "Международная мобильность факторов"),
    (5, "Торговая политика"),
    (6, "Таможенные союзы и интеграция"),
    (7, "ВТО и международные организации"),
    (8, "Торговый баланс"),
    (9, "Валютные курсы"),
    (10, "Валютные режимы"),
    (11, "Валютный рынок"),
    (12, "Международные валютные системы"),
    (13, "Сущность глобализации"),
    (14, "Транснациональные корпорации"),
    (15, "Преимущества и недостатки глобализации"),
    (16, "Глобальные проблемы"),
    (17, "Экономическая история России"),
    (18, "Структура экономики России"),
    (19, "Экономические реформы"),
    (20, "Перспективы экономики России"),
    (21, "Принципы налогообложения"),
    (22, "Налоги в России"),
    (23, "Налоговое администрирование"),
    (24, "Налоговая реформа"),
    (25, "Бюджетное устройство России"),
    (26, "Доходы и расходы бюджета"),
    (27, "Межбюджетные отношения"),
    (28, "Государственный долг"),
    (29, "Ключевые понятия экономики"),
    (30, "Решение задач"),
    (31, "Анализ экономических ситуаций"),
    (32, "Эссе по экономике"),
]


def title_font_size(title):
    """Return smaller font size for long titles."""
    if len(title) > 28:
        return 18
    elif len(title) > 22:
        return 20
    return 24


def make_svg(lesson_num, title):
    """Generate SVG content for a lesson."""
    tfs = title_font_size(title)
    escaped_title = html.escape(title)
    ill_content = get_illustration(lesson_num)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFF8E1"/>
      <stop offset="100%" stop-color="#FFFDE7"/>
    </linearGradient>
    <linearGradient id="panel" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#E65100"/>
      <stop offset="100%" stop-color="#F57C00"/>
    </linearGradient>
  </defs>
  <rect width="500" height="350" fill="url(#bg)" rx="10"/>
  <rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#E65100" stroke-width="3"/>
  <rect x="8" y="8" width="484" height="334" rx="6" fill="none" stroke="#E65100" stroke-width="1" opacity="0.3"/>
  <polygon points="10,10 30,10 10,30" fill="#E65100" opacity="0.12"/>
  <polygon points="490,10 470,10 490,30" fill="#1565C0" opacity="0.12"/>
  <polygon points="10,340 30,340 10,320" fill="#F9A825" opacity="0.12"/>
  <polygon points="490,340 470,340 490,320" fill="#2E7D32" opacity="0.12"/>
  <text x="250" y="48" font-family="Arial,sans-serif" font-size="{tfs}" font-weight="bold" fill="#E65100" text-anchor="middle">{escaped_title}</text>
  <text x="250" y="68" font-family="Arial,sans-serif" font-size="12" fill="#777" text-anchor="middle">Экономика - Урок {lesson_num}</text>
  <line x1="30" y1="78" x2="470" y2="78" stroke="#E65100" stroke-width="2" opacity="0.25"/>
  <rect x="30" y="75" width="60" height="5" fill="#E65100" opacity="0.18" rx="1"/>
  <rect x="410" y="75" width="60" height="5" fill="#1565C0" opacity="0.12" rx="1"/>
  <clipPath id="ill"><rect x="15" y="85" width="470" height="215" rx="6"/></clipPath>
  <g clip-path="url(#ill)">
  <rect x="15" y="85" width="470" height="215" fill="#FFF3E0"/>
  {ill_content}
  </g>
  <rect x="12" y="305" width="476" height="32" rx="5" fill="url(#panel)"/>
  <line x1="20" y1="308" x2="20" y2="334" stroke="#F9A825" stroke-width="1.5" opacity="0.6"/>
  <line x1="480" y1="308" x2="480" y2="334" stroke="#F9A825" stroke-width="1.5" opacity="0.6"/>
  <text x="250" y="326" font-family="Arial,sans-serif" font-size="15" text-anchor="middle" fill="white" font-weight="bold">Экономика</text>
</svg>'''


def get_illustration(n):
    """Return SVG illustration content for each lesson."""

    if n == 1:
        # Мировое хозяйство - Globe with connections
        return '''<circle cx="250" cy="195" r="70" fill="none" stroke="#E65100" stroke-width="2.5"/>
    <ellipse cx="250" cy="195" rx="70" ry="25" fill="none" stroke="#E65100" stroke-width="1" opacity="0.5"/>
    <ellipse cx="250" cy="195" rx="40" ry="70" fill="none" stroke="#E65100" stroke-width="1" opacity="0.5"/>
    <line x1="180" y1="195" x2="320" y2="195" stroke="#E65100" stroke-width="1" opacity="0.5"/>
    <circle cx="230" cy="175" r="5" fill="#F57C00"/>
    <circle cx="275" cy="185" r="5" fill="#1565C0"/>
    <circle cx="240" cy="215" r="5" fill="#2E7D32"/>
    <circle cx="270" cy="210" r="5" fill="#F9A825"/>
    <line x1="230" y1="175" x2="275" y2="185" stroke="#E65100" stroke-width="1.5" opacity="0.6"/>
    <line x1="275" y1="185" x2="270" y2="210" stroke="#E65100" stroke-width="1.5" opacity="0.6"/>
    <line x1="240" y1="215" x2="230" y2="175" stroke="#E65100" stroke-width="1.5" opacity="0.6"/>
    <line x1="240" y1="215" x2="270" y2="210" stroke="#E65100" stroke-width="1.5" opacity="0.6"/>
    <text x="250" y="285" font-family="Arial,sans-serif" font-size="13" fill="#E65100" text-anchor="middle" font-weight="bold">Мировое хозяйство</text>'''

    elif n == 2:
        # Сравнительные преимущества - Two bar charts with comparison
        return '''<rect x="100" y="160" width="40" height="80" fill="#F57C00" rx="3"/>
    <rect x="150" y="200" width="40" height="40" fill="#1565C0" rx="3"/>
    <rect x="310" y="200" width="40" height="40" fill="#F57C00" rx="3"/>
    <rect x="360" y="160" width="40" height="80" fill="#1565C0" rx="3"/>
    <text x="145" y="150" font-family="Arial,sans-serif" font-size="12" fill="#E65100" text-anchor="middle">Страна А</text>
    <text x="355" y="150" font-family="Arial,sans-serif" font-size="12" fill="#E65100" text-anchor="middle">Страна Б</text>
    <polygon points="210,190 240,180 240,195" fill="#2E7D32"/>
    <polygon points="290,190 260,180 260,195" fill="#2E7D32"/>
    <line x1="210" y1="190" x2="290" y2="190" stroke="#2E7D32" stroke-width="2"/>
    <text x="250" y="290" font-family="Arial,sans-serif" font-size="13" fill="#E65100" text-anchor="middle" font-weight="bold">Сравнительные преимущества</text>'''

    elif n == 3:
        # Теория Хекшера-Олина - Two regions exchanging factors
        return '''<rect x="60" y="140" width="130" height="90" rx="8" fill="none" stroke="#E65100" stroke-width="2"/>
    <text x="125" y="175" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle">Трудоизбыточная</text>
    <text x="125" y="195" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle">страна</text>
    <rect x="310" y="140" width="130" height="90" rx="8" fill="none" stroke="#1565C0" stroke-width="2"/>
    <text x="375" y="175" font-family="Arial,sans-serif" font-size="11" fill="#1565C0" text-anchor="middle">Капиталоизбыточная</text>
    <text x="375" y="195" font-family="Arial,sans-serif" font-size="11" fill="#1565C0" text-anchor="middle">страна</text>
    <line x1="190" y1="170" x2="310" y2="170" stroke="#F57C00" stroke-width="2" marker-end="url(#arrowR)"/>
    <text x="250" y="163" font-family="Arial,sans-serif" font-size="10" fill="#F57C00" text-anchor="middle">Трудоёмкие товары</text>
    <line x1="310" y1="200" x2="190" y2="200" stroke="#1565C0" stroke-width="2"/>
    <text x="250" y="218" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" text-anchor="middle">Капиталоёмкие товары</text>
    <polygon points="310,170 300,165 300,175" fill="#F57C00"/>
    <polygon points="190,200 200,195 200,205" fill="#1565C0"/>
    <text x="250" y="290" font-family="Arial,sans-serif" font-size="12" fill="#E65100" text-anchor="middle" font-weight="bold">Теория Хекшера-Олина</text>'''

    elif n == 4:
        # Международная мобильность факторов - Arrows between regions
        return '''<rect x="50" y="140" width="140" height="100" rx="8" fill="#FFF8E1" stroke="#E65100" stroke-width="2"/>
    <text x="120" y="195" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle">Регион 1</text>
    <rect x="310" y="140" width="140" height="100" rx="8" fill="#FFF8E1" stroke="#1565C0" stroke-width="2"/>
    <text x="380" y="195" font-family="Arial,sans-serif" font-size="11" fill="#1565C0" text-anchor="middle">Регион 2</text>
    <line x1="190" y1="160" x2="310" y2="160" stroke="#F57C00" stroke-width="2.5"/>
    <polygon points="310,160 300,155 300,165" fill="#F57C00"/>
    <text x="250" y="153" font-family="Arial,sans-serif" font-size="9" fill="#F57C00" text-anchor="middle">Капитал</text>
    <line x1="310" y1="220" x2="190" y2="220" stroke="#2E7D32" stroke-width="2.5"/>
    <polygon points="190,220 200,215 200,225" fill="#2E7D32"/>
    <text x="250" y="237" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle">Рабочая сила</text>
    <circle cx="120" cy="170" r="8" fill="#F9A825" opacity="0.4"/>
    <circle cx="380" cy="170" r="8" fill="#F9A825" opacity="0.4"/>
    <text x="250" y="290" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle" font-weight="bold">Мобильность факторов</text>'''

    elif n == 5:
        # Торговая политика - Shield/barrier with arrows
        return '''<rect x="210" y="120" width="80" height="120" rx="5" fill="none" stroke="#E65100" stroke-width="3"/>
    <text x="250" y="185" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle">Тариф</text>
    <line x1="100" y1="170" x2="205" y2="170" stroke="#2E7D32" stroke-width="2.5"/>
    <polygon points="205,170 195,165 195,175" fill="#2E7D32"/>
    <text x="140" y="163" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle">Экспорт</text>
    <line x1="295" y1="170" x2="400" y2="170" stroke="#1565C0" stroke-width="2.5"/>
    <polygon points="400,170 390,165 390,175" fill="#1565C0"/>
    <text x="360" y="163" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" text-anchor="middle">Импорт</text>
    <rect x="60" y="250" width="380" height="3" fill="#E65100" opacity="0.2"/>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="13" fill="#E65100" text-anchor="middle" font-weight="bold">Торговая политика</text>
    <rect x="225" y="130" width="50" height="15" fill="#F57C00" opacity="0.3" rx="2"/>
    <rect x="225" y="150" width="50" height="15" fill="#F57C00" opacity="0.3" rx="2"/>'''

    elif n == 6:
        # Таможенные союзы и интеграция - Connected circles
        return '''<circle cx="180" cy="190" r="40" fill="none" stroke="#E65100" stroke-width="2"/>
    <circle cx="250" cy="160" r="40" fill="none" stroke="#1565C0" stroke-width="2"/>
    <circle cx="320" cy="190" r="40" fill="none" stroke="#2E7D32" stroke-width="2"/>
    <text x="180" y="193" font-family="Arial,sans-serif" font-size="10" fill="#E65100" text-anchor="middle">Страна А</text>
    <text x="250" y="163" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" text-anchor="middle">Страна Б</text>
    <text x="320" y="193" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle">Страна В</text>
    <rect x="210" y="240" width="80" height="30" rx="5" fill="#F57C00" opacity="0.3"/>
    <text x="250" y="260" font-family="Arial,sans-serif" font-size="10" fill="#E65100" text-anchor="middle">Союз</text>
    <line x1="250" y1="200" x2="250" y2="240" stroke="#F57C00" stroke-width="1.5"/>
    <text x="250" y="290" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle" font-weight="bold">Таможенные союзы</text>'''

    elif n == 7:
        # ВТО и международные организации - Building with globe
        return '''<rect x="195" y="160" width="110" height="80" fill="none" stroke="#E65100" stroke-width="2"/>
    <rect x="220" y="180" width="25" height="30" fill="#E65100" opacity="0.2"/>
    <rect x="255" y="180" width="25" height="30" fill="#E65100" opacity="0.2"/>
    <polygon points="195,160 250,120 305,160" fill="none" stroke="#E65100" stroke-width="2"/>
    <text x="250" y="215" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle">ВТО</text>
    <circle cx="120" cy="170" r="25" fill="none" stroke="#1565C0" stroke-width="1.5"/>
    <ellipse cx="120" cy="170" rx="25" ry="10" fill="none" stroke="#1565C0" stroke-width="0.8" opacity="0.5"/>
    <text x="120" y="200" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" text-anchor="middle">МВФ</text>
    <circle cx="380" cy="170" r="25" fill="none" stroke="#2E7D32" stroke-width="1.5"/>
    <ellipse cx="380" cy="170" rx="25" ry="10" fill="none" stroke="#2E7D32" stroke-width="0.8" opacity="0.5"/>
    <text x="380" y="200" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle">ООН</text>
    <text x="250" y="290" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle" font-weight="bold">Международные организации</text>'''

    elif n == 8:
        # Торговый баланс - Scale/balance
        return '''<line x1="250" y1="120" x2="250" y2="200" stroke="#E65100" stroke-width="3"/>
    <polygon points="240,120 260,120 250,110" fill="#E65100"/>
    <line x1="160" y1="150" x2="340" y2="150" stroke="#E65100" stroke-width="2.5"/>
    <path d="M140,150 Q150,190 180,190" fill="none" stroke="#2E7D32" stroke-width="2"/>
    <line x1="160" y1="190" x2="200" y2="190" stroke="#2E7D32" stroke-width="2"/>
    <path d="M320,150 Q310,170 340,170" fill="none" stroke="#C62828" stroke-width="2"/>
    <line x1="300" y1="170" x2="360" y2="170" stroke="#C62828" stroke-width="2"/>
    <text x="180" y="210" font-family="Arial,sans-serif" font-size="11" fill="#2E7D32" text-anchor="middle">Экспорт</text>
    <text x="330" y="190" font-family="Arial,sans-serif" font-size="11" fill="#C62828" text-anchor="middle">Импорт</text>
    <rect x="80" y="240" width="130" height="30" rx="4" fill="#2E7D32" opacity="0.15"/>
    <rect x="290" y="240" width="130" height="30" rx="4" fill="#C62828" opacity="0.15"/>
    <text x="145" y="260" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle">+</text>
    <text x="355" y="260" font-family="Arial,sans-serif" font-size="10" fill="#C62828" text-anchor="middle">−</text>
    <text x="250" y="290" font-family="Arial,sans-serif" font-size="13" fill="#E65100" text-anchor="middle" font-weight="bold">Торговый баланс</text>'''

    elif n == 9:
        # Валютные курсы - Currency symbols with exchange arrows
        return '''<circle cx="160" cy="185" r="45" fill="none" stroke="#E65100" stroke-width="2"/>
    <text x="160" y="192" font-family="Arial,sans-serif" font-size="28" fill="#E65100" text-anchor="middle">$</text>
    <circle cx="340" cy="185" r="45" fill="none" stroke="#1565C0" stroke-width="2"/>
    <text x="340" y="192" font-family="Arial,sans-serif" font-size="28" fill="#1565C0" text-anchor="middle">&#8381;</text>
    <line x1="210" y1="170" x2="290" y2="170" stroke="#2E7D32" stroke-width="2.5"/>
    <polygon points="290,170 280,165 280,175" fill="#2E7D32"/>
    <line x1="290" y1="200" x2="210" y2="200" stroke="#F57C00" stroke-width="2.5"/>
    <polygon points="210,200 220,195 220,205" fill="#F57C00"/>
    <text x="250" y="165" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle">1$ → 95₽</text>
    <text x="250" y="290" font-family="Arial,sans-serif" font-size="13" fill="#E65100" text-anchor="middle" font-weight="bold">Валютные курсы</text>'''

    elif n == 10:
        # Валютные режимы - Different currency in boxes
        return '''<rect x="50" y="130" width="120" height="80" rx="6" fill="#FFF8E1" stroke="#E65100" stroke-width="2"/>
    <text x="110" y="160" font-family="Arial,sans-serif" font-size="10" fill="#E65100" text-anchor="middle">Фиксированный</text>
    <line x1="70" y1="180" x2="150" y2="180" stroke="#E65100" stroke-width="1.5"/>
    <rect x="190" y="130" width="120" height="80" rx="6" fill="#FFF8E1" stroke="#F57C00" stroke-width="2"/>
    <text x="250" y="160" font-family="Arial,sans-serif" font-size="10" fill="#F57C00" text-anchor="middle">Плавающий</text>
    <path d="M210,180 Q230,170 250,185 Q270,195 290,175" fill="none" stroke="#F57C00" stroke-width="1.5"/>
    <rect x="330" y="130" width="120" height="80" rx="6" fill="#FFF8E1" stroke="#1565C0" stroke-width="2"/>
    <text x="390" y="160" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" text-anchor="middle">Смешанный</text>
    <path d="M350,185 L370,175 L390,185 L410,170 L430,180" fill="none" stroke="#1565C0" stroke-width="1.5"/>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="12" fill="#E65100" text-anchor="middle" font-weight="bold">Валютные режимы</text>'''

    elif n == 11:
        # Валютный рынок - Trading chart with currency symbols
        return '''<line x1="70" y1="280" x2="70" y2="120" stroke="#E65100" stroke-width="2"/>
    <line x1="70" y1="280" x2="430" y2="280" stroke="#E65100" stroke-width="2"/>
    <polyline points="80,220 120,200 160,210 200,170 240,180 280,150 320,160 360,130 400,140 420,120" fill="none" stroke="#2E7D32" stroke-width="2.5"/>
    <polyline points="80,240 120,250 160,230 200,245 240,220 280,235 320,210 360,225 400,200 420,210" fill="none" stroke="#1565C0" stroke-width="2" stroke-dasharray="5,3"/>
    <text x="55" y="125" font-family="Arial,sans-serif" font-size="9" fill="#E65100" text-anchor="end">$</text>
    <text x="55" y="220" font-family="Arial,sans-serif" font-size="9" fill="#E65100" text-anchor="end">&#8381;</text>
    <text x="250" y="275" font-family="Arial,sans-serif" font-size="9" fill="#777" text-anchor="middle">Время</text>
    <circle cx="420" cy="120" r="4" fill="#2E7D32"/>
    <text x="250" y="295" font-family="Arial,sans-serif" font-size="13" fill="#E65100" text-anchor="middle" font-weight="bold">Валютный рынок</text>'''

    elif n == 12:
        # Международные валютные системы - Connected currency circles
        return '''<circle cx="150" cy="160" r="30" fill="none" stroke="#E65100" stroke-width="2"/>
    <text x="150" y="165" font-family="Arial,sans-serif" font-size="16" fill="#E65100" text-anchor="middle">$</text>
    <circle cx="250" cy="230" r="30" fill="none" stroke="#1565C0" stroke-width="2"/>
    <text x="250" y="235" font-family="Arial,sans-serif" font-size="16" fill="#1565C0" text-anchor="middle">&#8381;</text>
    <circle cx="350" cy="160" r="30" fill="none" stroke="#2E7D32" stroke-width="2"/>
    <text x="350" y="165" font-family="Arial,sans-serif" font-size="16" fill="#2E7D32" text-anchor="middle">&#8364;</text>
    <circle cx="250" cy="130" r="25" fill="none" stroke="#F9A825" stroke-width="2"/>
    <text x="250" y="135" font-family="Arial,sans-serif" font-size="12" fill="#F9A825" text-anchor="middle">SDR</text>
    <line x1="175" y1="165" x2="230" y2="135" stroke="#E65100" stroke-width="1.5" opacity="0.5"/>
    <line x1="270" y1="135" x2="325" y2="165" stroke="#2E7D32" stroke-width="1.5" opacity="0.5"/>
    <line x1="170" y1="180" x2="225" y2="215" stroke="#E65100" stroke-width="1.5" opacity="0.5"/>
    <line x1="275" y1="215" x2="330" y2="180" stroke="#2E7D32" stroke-width="1.5" opacity="0.5"/>
    <text x="250" y="290" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle" font-weight="bold">Валютные системы</text>'''

    elif n == 13:
        # Сущность глобализации - Globe with network
        return '''<circle cx="250" cy="190" r="75" fill="none" stroke="#E65100" stroke-width="2.5"/>
    <ellipse cx="250" cy="190" rx="75" ry="28" fill="none" stroke="#E65100" stroke-width="1" opacity="0.4"/>
    <line x1="175" y1="190" x2="325" y2="190" stroke="#E65100" stroke-width="0.8" opacity="0.4"/>
    <ellipse cx="250" cy="190" rx="45" ry="75" fill="none" stroke="#E65100" stroke-width="0.8" opacity="0.4"/>
    <circle cx="220" cy="165" r="6" fill="#F57C00"/>
    <circle cx="280" cy="175" r="6" fill="#1565C0"/>
    <circle cx="235" cy="215" r="6" fill="#2E7D32"/>
    <circle cx="270" cy="205" r="6" fill="#F9A825"/>
    <circle cx="250" cy="145" r="6" fill="#C62828"/>
    <line x1="220" y1="165" x2="280" y2="175" stroke="#333" stroke-width="1" opacity="0.4"/>
    <line x1="280" y1="175" x2="270" y2="205" stroke="#333" stroke-width="1" opacity="0.4"/>
    <line x1="235" y1="215" x2="220" y2="165" stroke="#333" stroke-width="1" opacity="0.4"/>
    <line x1="235" y1="215" x2="270" y2="205" stroke="#333" stroke-width="1" opacity="0.4"/>
    <line x1="250" y1="145" x2="220" y2="165" stroke="#333" stroke-width="1" opacity="0.4"/>
    <line x1="250" y1="145" x2="280" y2="175" stroke="#333" stroke-width="1" opacity="0.4"/>
    <text x="250" y="290" font-family="Arial,sans-serif" font-size="13" fill="#E65100" text-anchor="middle" font-weight="bold">Глобализация</text>'''

    elif n == 14:
        # Транснациональные корпорации - Building spanning globe
        return '''<circle cx="250" cy="210" r="60" fill="none" stroke="#E65100" stroke-width="1.5" opacity="0.5"/>
    <ellipse cx="250" cy="210" rx="60" ry="22" fill="none" stroke="#E65100" stroke-width="0.8" opacity="0.3"/>
    <rect x="200" y="120" width="100" height="80" fill="none" stroke="#1565C0" stroke-width="2"/>
    <polygon points="200,120 250,95 300,120" fill="none" stroke="#1565C0" stroke-width="2"/>
    <rect x="215" y="140" width="20" height="25" fill="#1565C0" opacity="0.3"/>
    <rect x="245" y="140" width="20" height="25" fill="#1565C0" opacity="0.3"/>
    <rect x="270" y="140" width="20" height="25" fill="#1565C0" opacity="0.3"/>
    <text x="250" y="185" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" text-anchor="middle">ТНК</text>
    <line x1="220" y1="200" x2="180" y2="230" stroke="#F57C00" stroke-width="1.5"/>
    <line x1="280" y1="200" x2="320" y2="230" stroke="#F57C00" stroke-width="1.5"/>
    <circle cx="170" cy="240" r="10" fill="#F57C00" opacity="0.3"/>
    <circle cx="330" cy="240" r="10" fill="#F57C00" opacity="0.3"/>
    <text x="170" y="244" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" text-anchor="middle">A</text>
    <text x="330" y="244" font-family="Arial,sans-serif" font-size="8" fill="#F57C00" text-anchor="middle">B</text>
    <text x="250" y="290" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle" font-weight="bold">Транснациональные корпорации</text>'''

    elif n == 15:
        # Преимущества и недостатки глобализации - Plus/minus scale
        return '''<line x1="250" y1="110" x2="250" y2="200" stroke="#E65100" stroke-width="3"/>
    <line x1="130" y1="150" x2="370" y2="150" stroke="#E65100" stroke-width="2.5"/>
    <rect x="100" y="160" width="110" height="70" rx="5" fill="#2E7D32" opacity="0.15" stroke="#2E7D32" stroke-width="1.5"/>
    <text x="155" y="185" font-family="Arial,sans-serif" font-size="20" fill="#2E7D32" text-anchor="middle">+</text>
    <text x="155" y="205" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle">Рост торговли</text>
    <rect x="290" y="160" width="110" height="70" rx="5" fill="#C62828" opacity="0.15" stroke="#C62828" stroke-width="1.5"/>
    <text x="345" y="185" font-family="Arial,sans-serif" font-size="20" fill="#C62828" text-anchor="middle">−</text>
    <text x="345" y="205" font-family="Arial,sans-serif" font-size="9" fill="#C62828" text-anchor="middle">Неравенство</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle" font-weight="bold">Плюсы и минусы глобализации</text>'''

    elif n == 16:
        # Глобальные проблемы - Warning signs
        return '''<polygon points="250,110 300,200 200,200" fill="none" stroke="#F9A825" stroke-width="2.5"/>
    <text x="250" y="185" font-family="Arial,sans-serif" font-size="30" fill="#F9A825" text-anchor="middle">!</text>
    <circle cx="120" cy="240" r="25" fill="none" stroke="#C62828" stroke-width="2"/>
    <text x="120" y="245" font-family="Arial,sans-serif" font-size="9" fill="#C62828" text-anchor="middle">CO2</text>
    <circle cx="250" cy="250" r="25" fill="none" stroke="#1565C0" stroke-width="2"/>
    <text x="250" y="255" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" text-anchor="middle">Бедность</text>
    <circle cx="380" cy="240" r="25" fill="none" stroke="#2E7D32" stroke-width="2"/>
    <text x="380" y="245" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle">Войны</text>
    <text x="250" y="290" font-family="Arial,sans-serif" font-size="13" fill="#E65100" text-anchor="middle" font-weight="bold">Глобальные проблемы</text>'''

    elif n == 17:
        # Экономическая история России - Timeline
        return '''<line x1="80" y1="180" x2="420" y2="180" stroke="#E65100" stroke-width="2.5"/>
    <circle cx="120" cy="180" r="8" fill="#E65100"/>
    <text x="120" y="210" font-family="Arial,sans-serif" font-size="9" fill="#E65100" text-anchor="middle">1917</text>
    <circle cx="190" cy="180" r="8" fill="#C62828"/>
    <text x="190" y="210" font-family="Arial,sans-serif" font-size="9" fill="#C62828" text-anchor="middle">1928</text>
    <circle cx="260" cy="180" r="8" fill="#1565C0"/>
    <text x="260" y="210" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" text-anchor="middle">1991</text>
    <circle cx="330" cy="180" r="8" fill="#2E7D32"/>
    <text x="330" y="210" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle">1998</text>
    <circle cx="400" cy="180" r="8" fill="#F9A825"/>
    <text x="400" y="210" font-family="Arial,sans-serif" font-size="9" fill="#F9A825" text-anchor="middle">2000+</text>
    <text x="120" y="235" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Революция</text>
    <text x="190" y="235" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">План</text>
    <text x="260" y="235" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Рынок</text>
    <text x="330" y="235" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Кризис</text>
    <text x="400" y="235" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Рост</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle" font-weight="bold">Экономическая история</text>'''

    elif n == 18:
        # Структура экономики России - Pie chart sectors
        return '''<circle cx="250" cy="190" r="70" fill="none" stroke="#E65100" stroke-width="1"/>
    <path d="M250,190 L250,120 A70,70 0 0,1 310,145Z" fill="#E65100" opacity="0.4"/>
    <path d="M250,190 L310,145 A70,70 0 0,1 320,190Z" fill="#1565C0" opacity="0.4"/>
    <path d="M250,190 L320,190 A70,70 0 0,1 310,235Z" fill="#2E7D32" opacity="0.4"/>
    <path d="M250,190 L310,235 A70,70 0 0,1 190,235Z" fill="#F9A825" opacity="0.4"/>
    <path d="M250,190 L190,235 A70,70 0 0,1 180,190Z" fill="#C62828" opacity="0.4"/>
    <path d="M250,190 L180,190 A70,70 0 0,1 250,120Z" fill="#7B1FA2" opacity="0.4"/>
    <text x="270" y="155" font-family="Arial,sans-serif" font-size="8" fill="#E65100">Нефть</text>
    <text x="305" y="190" font-family="Arial,sans-serif" font-size="8" fill="#1565C0">Газ</text>
    <text x="290" y="225" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32">С/х</text>
    <text x="230" y="240" font-family="Arial,sans-serif" font-size="8" fill="#F9A825">Услуги</text>
    <text x="195" y="205" font-family="Arial,sans-serif" font-size="8" fill="#C62828">Пром.</text>
    <text x="220" y="155" font-family="Arial,sans-serif" font-size="8" fill="#7B1FA2">IT</text>
    <text x="250" y="290" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle" font-weight="bold">Структура экономики</text>'''

    elif n == 19:
        # Экономические реформы - Arrow from old to new
        return '''<rect x="60" y="150" width="120" height="80" rx="6" fill="none" stroke="#C62828" stroke-width="2"/>
    <text x="120" y="180" font-family="Arial,sans-serif" font-size="10" fill="#C62828" text-anchor="middle">Плановая</text>
    <text x="120" y="195" font-family="Arial,sans-serif" font-size="10" fill="#C62828" text-anchor="middle">экономика</text>
    <rect x="320" y="150" width="120" height="80" rx="6" fill="none" stroke="#2E7D32" stroke-width="2"/>
    <text x="380" y="180" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle">Рыночная</text>
    <text x="380" y="195" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle">экономика</text>
    <line x1="185" y1="190" x2="315" y2="190" stroke="#F57C00" stroke-width="3"/>
    <polygon points="315,190 305,185 305,195" fill="#F57C00"/>
    <text x="250" y="183" font-family="Arial,sans-serif" font-size="10" fill="#F57C00" text-anchor="middle">Реформы</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="13" fill="#E65100" text-anchor="middle" font-weight="bold">Экономические реформы</text>'''

    elif n == 20:
        # Перспективы экономики России - Upward arrow chart
        return '''<line x1="80" y1="270" x2="80" y2="120" stroke="#E65100" stroke-width="2"/>
    <line x1="80" y1="270" x2="430" y2="270" stroke="#E65100" stroke-width="2"/>
    <polyline points="100,250 150,240 200,220 250,200 300,175 350,155 400,130" fill="none" stroke="#2E7D32" stroke-width="3"/>
    <polygon points="400,130 395,142 405,142" fill="#2E7D32"/>
    <rect x="100" y="245" width="40" height="25" fill="#E65100" opacity="0.2" rx="2"/>
    <rect x="180" y="225" width="40" height="45" fill="#F57C00" opacity="0.2" rx="2"/>
    <rect x="260" y="200" width="40" height="70" fill="#F9A825" opacity="0.2" rx="2"/>
    <rect x="340" y="165" width="40" height="105" fill="#2E7D32" opacity="0.2" rx="2"/>
    <text x="250" y="290" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle" font-weight="bold">Перспективы экономики</text>'''

    elif n == 21:
        # Принципы налогообложения - Document with rules
        return '''<rect x="170" y="110" width="160" height="150" rx="5" fill="white" stroke="#E65100" stroke-width="2"/>
    <line x1="190" y1="135" x2="310" y2="135" stroke="#E65100" stroke-width="1" opacity="0.5"/>
    <line x1="190" y1="155" x2="310" y2="155" stroke="#E65100" stroke-width="1" opacity="0.5"/>
    <line x1="190" y1="175" x2="310" y2="175" stroke="#E65100" stroke-width="1" opacity="0.5"/>
    <line x1="190" y1="195" x2="310" y2="195" stroke="#E65100" stroke-width="1" opacity="0.5"/>
    <line x1="190" y1="215" x2="310" y2="215" stroke="#E65100" stroke-width="1" opacity="0.5"/>
    <line x1="190" y1="235" x2="310" y2="235" stroke="#E65100" stroke-width="1" opacity="0.5"/>
    <circle cx="185" cy="130" r="3" fill="#E65100"/>
    <circle cx="185" cy="150" r="3" fill="#F57C00"/>
    <circle cx="185" cy="170" r="3" fill="#1565C0"/>
    <circle cx="185" cy="190" r="3" fill="#2E7D32"/>
    <circle cx="185" cy="210" r="3" fill="#F9A825"/>
    <circle cx="185" cy="230" r="3" fill="#7B1FA2"/>
    <text x="250" y="130" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Справедливость</text>
    <text x="250" y="150" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Эффективность</text>
    <text x="250" y="170" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Определённость</text>
    <text x="250" y="190" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Удобство</text>
    <text x="250" y="210" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Экономность</text>
    <text x="250" y="230" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Пропорциональность</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle" font-weight="bold">Принципы налогообложения</text>'''

    elif n == 22:
        # Налоги в России - Coins going to government building
        return '''<rect x="190" y="130" width="120" height="90" fill="none" stroke="#E65100" stroke-width="2"/>
    <polygon points="190,130 250,95 310,130" fill="none" stroke="#E65100" stroke-width="2"/>
    <rect x="215" y="160" width="20" height="30" fill="#E65100" opacity="0.2"/>
    <rect x="245" y="160" width="20" height="30" fill="#E65100" opacity="0.2"/>
    <rect x="275" y="160" width="20" height="30" fill="#E65100" opacity="0.2"/>
    <text x="250" y="205" font-family="Arial,sans-serif" font-size="10" fill="#E65100" text-anchor="middle">Налоги</text>
    <circle cx="100" cy="220" r="15" fill="#F9A825" opacity="0.4" stroke="#F9A825" stroke-width="1"/>
    <text x="100" y="225" font-family="Arial,sans-serif" font-size="10" fill="#F9A825" text-anchor="middle">₽</text>
    <circle cx="140" cy="240" r="12" fill="#F9A825" opacity="0.4" stroke="#F9A825" stroke-width="1"/>
    <circle cx="80" cy="245" r="12" fill="#F9A825" opacity="0.4" stroke="#F9A825" stroke-width="1"/>
    <line x1="120" y1="215" x2="190" y2="195" stroke="#F57C00" stroke-width="1.5" stroke-dasharray="4,3"/>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="13" fill="#E65100" text-anchor="middle" font-weight="bold">Налоги в России</text>'''

    elif n == 23:
        # Налоговое администрирование - Calculator and documents
        return '''<rect x="150" y="120" width="80" height="110" rx="5" fill="none" stroke="#E65100" stroke-width="2"/>
    <rect x="160" y="135" width="60" height="25" fill="#FFF8E1" stroke="#E65100" stroke-width="1"/>
    <rect x="160" y="168" width="15" height="12" fill="#E65100" opacity="0.3" rx="1"/>
    <rect x="180" y="168" width="15" height="12" fill="#E65100" opacity="0.3" rx="1"/>
    <rect x="200" y="168" width="15" height="12" fill="#E65100" opacity="0.3" rx="1"/>
    <rect x="160" y="185" width="15" height="12" fill="#E65100" opacity="0.3" rx="1"/>
    <rect x="180" y="185" width="15" height="12" fill="#E65100" opacity="0.3" rx="1"/>
    <rect x="200" y="185" width="15" height="12" fill="#E65100" opacity="0.3" rx="1"/>
    <rect x="160" y="202" width="15" height="12" fill="#E65100" opacity="0.3" rx="1"/>
    <rect x="180" y="202" width="15" height="12" fill="#E65100" opacity="0.3" rx="1"/>
    <rect x="200" y="202" width="15" height="12" fill="#E65100" opacity="0.3" rx="1"/>
    <rect x="280" y="130" width="100" height="120" rx="3" fill="white" stroke="#1565C0" stroke-width="1.5"/>
    <line x1="295" y1="150" x2="365" y2="150" stroke="#1565C0" stroke-width="0.8" opacity="0.4"/>
    <line x1="295" y1="165" x2="365" y2="165" stroke="#1565C0" stroke-width="0.8" opacity="0.4"/>
    <line x1="295" y1="180" x2="365" y2="180" stroke="#1565C0" stroke-width="0.8" opacity="0.4"/>
    <line x1="295" y1="195" x2="365" y2="195" stroke="#1565C0" stroke-width="0.8" opacity="0.4"/>
    <line x1="295" y1="210" x2="365" y2="210" stroke="#1565C0" stroke-width="0.8" opacity="0.4"/>
    <line x1="295" y1="225" x2="365" y2="225" stroke="#1565C0" stroke-width="0.8" opacity="0.4"/>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle" font-weight="bold">Налоговое администрирование</text>'''

    elif n == 24:
        # Налоговая реформа - Document with arrow transformation
        return '''<rect x="80" y="140" width="100" height="120" rx="5" fill="white" stroke="#C62828" stroke-width="1.5"/>
    <text x="130" y="165" font-family="Arial,sans-serif" font-size="9" fill="#C62828" text-anchor="middle">Старая</text>
    <text x="130" y="178" font-family="Arial,sans-serif" font-size="9" fill="#C62828" text-anchor="middle">система</text>
    <line x1="100" y1="195" x2="160" y2="195" stroke="#C62828" stroke-width="0.8" opacity="0.4"/>
    <line x1="100" y1="210" x2="160" y2="210" stroke="#C62828" stroke-width="0.8" opacity="0.4"/>
    <line x1="100" y1="225" x2="160" y2="225" stroke="#C62828" stroke-width="0.8" opacity="0.4"/>
    <rect x="320" y="140" width="100" height="120" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
    <text x="370" y="165" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle">Новая</text>
    <text x="370" y="178" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle">система</text>
    <line x1="340" y1="195" x2="400" y2="195" stroke="#2E7D32" stroke-width="0.8" opacity="0.4"/>
    <line x1="340" y1="210" x2="400" y2="210" stroke="#2E7D32" stroke-width="0.8" opacity="0.4"/>
    <line x1="340" y1="225" x2="400" y2="225" stroke="#2E7D32" stroke-width="0.8" opacity="0.4"/>
    <line x1="180" y1="200" x2="320" y2="200" stroke="#F57C00" stroke-width="3"/>
    <polygon points="320,200 310,195 310,205" fill="#F57C00"/>
    <text x="250" y="193" font-family="Arial,sans-serif" font-size="10" fill="#F57C00" text-anchor="middle">Реформа</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="13" fill="#E65100" text-anchor="middle" font-weight="bold">Налоговая реформа</text>'''

    elif n == 25:
        # Бюджетное устройство России - Layers of budget
        return '''<rect x="100" y="120" width="300" height="40" rx="5" fill="#E65100" opacity="0.3" stroke="#E65100" stroke-width="1.5"/>
    <text x="250" y="145" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle">Федеральный бюджет</text>
    <rect x="130" y="170" width="240" height="35" rx="5" fill="#1565C0" opacity="0.3" stroke="#1565C0" stroke-width="1.5"/>
    <text x="250" y="192" font-family="Arial,sans-serif" font-size="11" fill="#1565C0" text-anchor="middle">Региональный бюджет</text>
    <rect x="160" y="215" width="180" height="35" rx="5" fill="#2E7D32" opacity="0.3" stroke="#2E7D32" stroke-width="1.5"/>
    <text x="250" y="237" font-family="Arial,sans-serif" font-size="11" fill="#2E7D32" text-anchor="middle">Местный бюджет</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle" font-weight="bold">Бюджетное устройство</text>'''

    elif n == 26:
        # Доходы и расходы бюджета - Two columns
        return '''<text x="165" y="120" font-family="Arial,sans-serif" font-size="14" fill="#2E7D32" text-anchor="middle" font-weight="bold">Доходы</text>
    <rect x="80" y="130" width="170" height="30" rx="3" fill="#2E7D32" opacity="0.25"/>
    <text x="165" y="150" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle">Налоговые</text>
    <rect x="80" y="165" width="170" height="30" rx="3" fill="#2E7D32" opacity="0.18"/>
    <text x="165" y="185" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle">Неналоговые</text>
    <rect x="80" y="200" width="170" height="30" rx="3" fill="#2E7D32" opacity="0.12"/>
    <text x="165" y="220" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle">Безвозмездные</text>
    <text x="345" y="120" font-family="Arial,sans-serif" font-size="14" fill="#C62828" text-anchor="middle" font-weight="bold">Расходы</text>
    <rect x="260" y="130" width="170" height="30" rx="3" fill="#C62828" opacity="0.25"/>
    <text x="345" y="150" font-family="Arial,sans-serif" font-size="9" fill="#C62828" text-anchor="middle">Социальные</text>
    <rect x="260" y="165" width="170" height="30" rx="3" fill="#C62828" opacity="0.18"/>
    <text x="345" y="185" font-family="Arial,sans-serif" font-size="9" fill="#C62828" text-anchor="middle">Оборона</text>
    <rect x="260" y="200" width="170" height="30" rx="3" fill="#C62828" opacity="0.12"/>
    <text x="345" y="220" font-family="Arial,sans-serif" font-size="9" fill="#C62828" text-anchor="middle">Управление</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle" font-weight="bold">Доходы и расходы бюджета</text>'''

    elif n == 27:
        # Межбюджетные отношения - Arrows between budget levels
        return '''<rect x="160" y="100" width="180" height="40" rx="5" fill="#E65100" opacity="0.25" stroke="#E65100" stroke-width="1.5"/>
    <text x="250" y="125" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle">Федеральный</text>
    <rect x="80" y="200" width="150" height="40" rx="5" fill="#1565C0" opacity="0.25" stroke="#1565C0" stroke-width="1.5"/>
    <text x="155" y="225" font-family="Arial,sans-serif" font-size="11" fill="#1565C0" text-anchor="middle">Региональный</text>
    <rect x="270" y="200" width="150" height="40" rx="5" fill="#2E7D32" opacity="0.25" stroke="#2E7D32" stroke-width="1.5"/>
    <text x="345" y="225" font-family="Arial,sans-serif" font-size="11" fill="#2E7D32" text-anchor="middle">Региональный</text>
    <line x1="200" y1="140" x2="155" y2="200" stroke="#F57C00" stroke-width="2"/>
    <polygon points="155,200 160,190 150,190" fill="#F57C00"/>
    <line x1="300" y1="140" x2="345" y2="200" stroke="#F57C00" stroke-width="2"/>
    <polygon points="345,200 340,190 350,190" fill="#F57C00"/>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle" font-weight="bold">Межбюджетные отношения</text>'''

    elif n == 28:
        # Государственный долг - Stacked coins with chain
        return '''<ellipse cx="200" cy="230" rx="40" ry="12" fill="#F9A825" opacity="0.4" stroke="#F9A825" stroke-width="1"/>
    <ellipse cx="200" cy="218" rx="40" ry="12" fill="#F9A825" opacity="0.45" stroke="#F9A825" stroke-width="1"/>
    <ellipse cx="200" cy="206" rx="40" ry="12" fill="#F9A825" opacity="0.5" stroke="#F9A825" stroke-width="1"/>
    <ellipse cx="200" cy="194" rx="40" ry="12" fill="#F9A825" opacity="0.55" stroke="#F9A825" stroke-width="1"/>
    <ellipse cx="200" cy="182" rx="40" ry="12" fill="#F9A825" opacity="0.6" stroke="#F9A825" stroke-width="1"/>
    <ellipse cx="200" cy="170" rx="40" ry="12" fill="#F9A825" opacity="0.7" stroke="#F9A825" stroke-width="1"/>
    <text x="200" y="175" font-family="Arial,sans-serif" font-size="10" fill="#E65100" text-anchor="middle">Долг</text>
    <path d="M280,170 Q300,150 320,170 Q340,190 360,170 Q380,150 400,170" fill="none" stroke="#C62828" stroke-width="2.5"/>
    <text x="340" y="200" font-family="Arial,sans-serif" font-size="10" fill="#C62828" text-anchor="middle">Обслуживание</text>
    <line x1="240" y1="180" x2="280" y2="175" stroke="#C62828" stroke-width="1.5" stroke-dasharray="4,3"/>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="13" fill="#E65100" text-anchor="middle" font-weight="bold">Государственный долг</text>'''

    elif n == 29:
        # Ключевые понятия экономики - Key concepts symbols
        return '''<rect x="60" y="120" width="100" height="50" rx="6" fill="#E65100" opacity="0.2" stroke="#E65100" stroke-width="1.5"/>
    <text x="110" y="150" font-family="Arial,sans-serif" font-size="10" fill="#E65100" text-anchor="middle">Спрос</text>
    <rect x="200" y="120" width="100" height="50" rx="6" fill="#1565C0" opacity="0.2" stroke="#1565C0" stroke-width="1.5"/>
    <text x="250" y="150" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" text-anchor="middle">Предложение</text>
    <rect x="340" y="120" width="100" height="50" rx="6" fill="#2E7D32" opacity="0.2" stroke="#2E7D32" stroke-width="1.5"/>
    <text x="390" y="150" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle">Рынок</text>
    <rect x="60" y="190" width="100" height="50" rx="6" fill="#F9A825" opacity="0.2" stroke="#F9A825" stroke-width="1.5"/>
    <text x="110" y="220" font-family="Arial,sans-serif" font-size="10" fill="#F9A825" text-anchor="middle">Инфляция</text>
    <rect x="200" y="190" width="100" height="50" rx="6" fill="#7B1FA2" opacity="0.2" stroke="#7B1FA2" stroke-width="1.5"/>
    <text x="250" y="220" font-family="Arial,sans-serif" font-size="10" fill="#7B1FA2" text-anchor="middle">ВВП</text>
    <rect x="340" y="190" width="100" height="50" rx="6" fill="#C62828" opacity="0.2" stroke="#C62828" stroke-width="1.5"/>
    <text x="390" y="220" font-family="Arial,sans-serif" font-size="10" fill="#C62828" text-anchor="middle">Безработица</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle" font-weight="bold">Ключевые понятия</text>'''

    elif n == 30:
        # Решение задач - Math problem solving
        return '''<rect x="130" y="110" width="240" height="160" rx="8" fill="white" stroke="#E65100" stroke-width="2"/>
    <text x="250" y="140" font-family="Arial,sans-serif" font-size="12" fill="#E65100" text-anchor="middle" font-weight="bold">Задача</text>
    <line x1="150" y1="148" x2="350" y2="148" stroke="#E65100" stroke-width="1" opacity="0.3"/>
    <text x="170" y="170" font-family="Arial,sans-serif" font-size="10" fill="#333">ВВП = C + I + G + NX</text>
    <line x1="150" y1="185" x2="350" y2="185" stroke="#E65100" stroke-width="1" opacity="0.3"/>
    <text x="170" y="210" font-family="Arial,sans-serif" font-size="10" fill="#333">Если C=100, I=50</text>
    <text x="170" y="228" font-family="Arial,sans-serif" font-size="10" fill="#333">G=80, NX=20</text>
    <text x="170" y="252" font-family="Arial,sans-serif" font-size="11" fill="#2E7D32" font-weight="bold">ВВП = 250</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="13" fill="#E65100" text-anchor="middle" font-weight="bold">Решение задач</text>'''

    elif n == 31:
        # Анализ экономических ситуаций - Magnifying glass over chart
        return '''<line x1="80" y1="260" x2="80" y2="140" stroke="#E65100" stroke-width="1.5"/>
    <line x1="80" y1="260" x2="380" y2="260" stroke="#E65100" stroke-width="1.5"/>
    <polyline points="90,240 130,220 170,230 210,190 250,200 290,170 330,180 370,150" fill="none" stroke="#1565C0" stroke-width="2"/>
    <circle cx="280" cy="175" r="45" fill="none" stroke="#E65100" stroke-width="3"/>
    <line x1="312" y1="207" x2="350" y2="250" stroke="#E65100" stroke-width="5" stroke-linecap="round"/>
    <text x="250" y="290" font-family="Arial,sans-serif" font-size="11" fill="#E65100" text-anchor="middle" font-weight="bold">Анализ ситуаций</text>'''

    elif n == 32:
        # Эссе по экономике - Paper with pen
        return '''<rect x="150" y="100" width="170" height="160" rx="4" fill="white" stroke="#E65100" stroke-width="2"/>
    <line x1="170" y1="130" x2="300" y2="130" stroke="#E65100" stroke-width="0.8" opacity="0.4"/>
    <line x1="170" y1="150" x2="300" y2="150" stroke="#E65100" stroke-width="0.8" opacity="0.4"/>
    <line x1="170" y1="170" x2="300" y2="170" stroke="#E65100" stroke-width="0.8" opacity="0.4"/>
    <line x1="170" y1="190" x2="280" y2="190" stroke="#E65100" stroke-width="0.8" opacity="0.4"/>
    <line x1="170" y1="210" x2="260" y2="210" stroke="#E65100" stroke-width="0.8" opacity="0.4"/>
    <line x1="170" y1="230" x2="290" y2="230" stroke="#E65100" stroke-width="0.8" opacity="0.4"/>
    <text x="235" y="125" font-family="Arial,sans-serif" font-size="10" fill="#E65100" text-anchor="middle">Экономическое эссе</text>
    <rect x="310" y="180" width="8" height="80" rx="2" fill="#1565C0" transform="rotate(-30,314,220)"/>
    <polygon points="310,260 306,268 314,268" fill="#1565C0" transform="rotate(-30,314,220)"/>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="13" fill="#E65100" text-anchor="middle" font-weight="bold">Эссе по экономике</text>'''

    return ""


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    count = 0
    for lesson_num, title in LESSONS:
        svg_content = make_svg(lesson_num, title)
        filepath = os.path.join(OUTPUT_DIR, f"lesson{lesson_num}.svg")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)
        count += 1
        print(f"Created: {filepath}")

    print(f"\nDone! Generated {count} SVG files in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
