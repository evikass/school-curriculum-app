#!/usr/bin/env python3
"""Generate 12 detailed SVG files for Grade 10 Business (Бизнес) lessons."""

import xml.etree.ElementTree as ET
import os

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade10/business"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PRIMARY = "#FF6F00"
BG = "#FFF8E1"
DARK = "#3E2723"
MID = "#5D4037"
ACCENT = "#FFB300"
LIGHT_ACCENT = "#FFE082"
WHITE = "#FFFFFF"
SOFT_BG = "#FFF3E0"

LESSONS = [
    {
        "num": 1,
        "title": "Предпринимательство",
        "subtitle": "Бизнес — Урок 1",
        "sections": [
            {
                "type": "concept_boxes",
                "heading": "Ключевые понятия",
                "items": [
                    ("Предприниматель", "Человек, который\nсоздаёт бизнес\nи берёт на себя риски"),
                    ("Стартап", "Молодой проект,\nищущий масштабную\nбизнес-модель"),
                    ("Прибыль", "Доход минус расходы:\nцель любого бизнеса"),
                ],
            },
            {
                "type": "steps",
                "heading": "Путь предпринимателя",
                "items": [
                    "1. Замечаешь проблему",
                    "2. Рождаешь идею",
                    "3. Проверяешь гипотезы",
                    "4. Создаёшь MVP",
                    "5. Масштабируешь",
                ],
            },
            {
                "type": "tip",
                "text": "Совет: Настоящий предприниматель видит возможности там, где другие видят проблемы!",
            },
        ],
    },
    {
        "num": 2,
        "title": "Бизнес-идея",
        "subtitle": "Бизнес — Урок 2",
        "sections": [
            {
                "type": "concept_boxes",
                "heading": "Источники идей",
                "items": [
                    ("Личный опыт", "Реши свою\nсобственную\nпроблему"),
                    ("Наблюдение", "Изучай тренды\nи поведение\nлюдей"),
                    ("Кросс-индустрия", "Перенеси решение\nиз одной сферы\nв другую"),
                ],
            },
            {
                "type": "criteria_table",
                "heading": "Критерии оценки идеи",
                "rows": [
                    ("Решает ли проблему?", "★★★★★"),
                    ("Есть ли рынок?", "★★★★☆"),
                    ("Реализуема ли?", "★★★☆☆"),
                    ("Уникальна ли?", "★★★★☆"),
                ],
            },
            {
                "type": "tip",
                "text": "Совет: Идея без реализации — это фантазия. Тестируй идею на реальных людях!",
            },
        ],
    },
    {
        "num": 3,
        "title": "Бизнес-план",
        "subtitle": "Бизнес — Урок 3",
        "sections": [
            {
                "type": "flow_diagram",
                "heading": "Структура бизнес-плана",
                "items": [
                    "Резюме",
                    "Описание\nпродукта",
                    "Анализ\nрынка",
                    "Стратегия\nмаркетинга",
                    "Финансовый\nплан",
                ],
            },
            {
                "type": "key_points",
                "heading": "Зачем нужен бизнес-план?",
                "items": [
                    "Структурирует мысли",
                    "Помогает привлечь инвестиции",
                    "Позволяет оценить риски",
                    "Служит дорожной картой",
                ],
            },
            {
                "type": "tip",
                "text": "Совет: Бизнес-план — живой документ. Обновляй его по мере получения новых данных!",
            },
        ],
    },
    {
        "num": 4,
        "title": "Юридические основы",
        "subtitle": "Бизнес — Урок 4",
        "sections": [
            {
                "type": "comparison",
                "heading": "Формы бизнеса",
                "items": [
                    ("ИП", "Один владелец\nПростая регистрация\nЛичная ответственность"),
                    ("ООО", "От 1 учредителя\nУставный капитал\nОграниченная ответственность"),
                    ("АО", "Акционеры\nАкции\nСложное управление"),
                ],
            },
            {
                "type": "checklist",
                "heading": "Что нужно для регистрации",
                "items": [
                    "Выбрать форму собственности",
                    "Определить ОКВЭД",
                    "Подать документы в налоговую",
                    "Открыть расчётный счёт",
                ],
            },
            {
                "type": "tip",
                "text": "Совет: Консультируйся с юристом до подписания любых документов!",
            },
        ],
    },
    {
        "num": 5,
        "title": "Целевая аудитория",
        "subtitle": "Бизнес — Урок 5",
        "sections": [
            {
                "type": "segment_diagram",
                "heading": "Сегментация аудитории",
                "segments": [
                    ("Демография", "Возраст, пол,\nдоход, образование"),
                    ("География", "Страна, город,\nклимат, плотность"),
                    ("Поведение", "Привычки, частота\nпокупок, лояльность"),
                    ("Психографика", "Ценности, интересы,\nстиль жизни"),
                ],
            },
            {
                "type": "persona",
                "heading": "Метод «Аватар клиента»",
                "fields": [
                    "Имя: Анна, 25 лет",
                    "Работает в IT, живёт в городе",
                    "Ценит удобство и скорость",
                    "Готова платить за качество",
                ],
            },
            {
                "type": "tip",
                "text": "Совет: «Все» — это не целевая аудитория. Сужай сегмент для эффективного маркетинга!",
            },
        ],
    },
    {
        "num": 6,
        "title": "Продукт",
        "subtitle": "Бизнес — Урок 6",
        "sections": [
            {
                "type": "layers",
                "heading": "Уровни продукта",
                "items": [
                    ("Основной", "Какую проблему решает?", "#E65100"),
                    ("Реальный", "Характеристики и дизайн", "#FF8F00"),
                    ("Расширенный", "Сервис, гарантия, поддержка", "#FFB300"),
                ],
            },
            {
                "type": "mvp_cycle",
                "heading": "Цикл создания MVP",
                "items": [
                    "Идея →",
                    "MVP →",
                    "Обратная\nсвязь →",
                    "Улучшение →",
                    "Идея",
                ],
            },
            {
                "type": "tip",
                "text": "Совет: Не создавай идеальный продукт. Создай минимальный и улучшай по отзывам!",
            },
        ],
    },
    {
        "num": 7,
        "title": "Продвижение",
        "subtitle": "Бизнес — Урок 7",
        "sections": [
            {
                "type": "channels",
                "heading": "Каналы продвижения",
                "items": [
                    ("SMM", "Соцсети,\nконтент,\nвовлечение"),
                    ("SEO/SEM", "Поисковая\nоптимизация,\nреклама"),
                    ("PR", "Статьи,\nинтервью,\nмероприятия"),
                    ("Реферали", "Сарафанное\nрадио,\nпартнёрства"),
                ],
            },
            {
                "type": "funnel",
                "heading": "Воронка продаж",
                "items": [
                    ("Осведомлённость", 180),
                    ("Интерес", 140),
                    ("Желание", 90),
                    ("Действие", 50),
                ],
            },
            {
                "type": "tip",
                "text": "Совет: Измеряй каждый канал. Отключай то, что не работает, усиливай то, что приносит клиентов!",
            },
        ],
    },
    {
        "num": 8,
        "title": "Продажи",
        "subtitle": "Бизнес — Урок 8",
        "sections": [
            {
                "type": "steps",
                "heading": "Процесс продажи",
                "items": [
                    "1. Установление контакта",
                    "2. Выявление потребностей",
                    "3. Презентация решения",
                    "4. Работа с возражениями",
                    "5. Закрытие сделки",
                    "6. Последующие продажи",
                ],
            },
            {
                "type": "objection_boxes",
                "heading": "Топ возражений и ответы",
                "items": [
                    ("«Дорого»", "Покажи ценность\nи возврат инвестиций"),
                    ("«Подумаю»", "Уточни сомнения\nи дай дедлайн"),
                    ("«У конкурентов дешевле»", "Объясни отличия\nи преимущества"),
                ],
            },
            {
                "type": "tip",
                "text": "Совет: Продажи — это не уговоры, а помощь клиенту принять правильное решение!",
            },
        ],
    },
    {
        "num": 9,
        "title": "Финансовые расчёты",
        "subtitle": "Бизнес — Урок 9",
        "sections": [
            {
                "type": "formula_boxes",
                "heading": "Ключевые формулы",
                "items": [
                    ("Прибыль", "Доходы − Расходы"),
                    ("Маржа", "(Прибыль / Цена) × 100%"),
                    ("ROI", "(Прибыль / Инвестиции) × 100%"),
                    ("Точка безубыточности", "Пост.расх. / (Цена − Перем.расх.)"),
                ],
            },
            {
                "type": "mini_chart",
                "heading": "Структура расходов стартапа",
                "bars": [
                    ("Разработка", 35, "#E65100"),
                    ("Маркетинг", 25, "#FF8F00"),
                    ("Зарплаты", 25, "#FFB300"),
                    ("Прочее", 15, "#FFE082"),
                ],
            },
            {
                "type": "tip",
                "text": "Совет: Веди учёт с первого дня! Необходимые инструменты: таблицы, 1С, онлайн-бухгалтерия.",
            },
        ],
    },
    {
        "num": 10,
        "title": "Команда",
        "subtitle": "Бизнес — Урок 10",
        "sections": [
            {
                "type": "roles",
                "heading": "Ключевые роли в команде",
                "items": [
                    ("Визионер", "Стратегия\nи направление", "🎯"),
                    ("Технарь", "Продукт\nи технологии", "⚙"),
                    ("Продажник", "Клиенты\nи рост", "📈"),
                    ("Организатор", "Процессы\nи финансы", "📋"),
                ],
            },
            {
                "type": "key_points",
                "heading": "Принципы сильной команды",
                "items": [
                    "Дополнительные навыки друг друга",
                    "Общие ценности и видение",
                    "Прозрачная коммуникация",
                    "Чёткое распределение ролей",
                ],
            },
            {
                "type": "tip",
                "text": "Совет: Ищи людей, которые сильны там, где ты слаб. Один в поле не воин!",
            },
        ],
    },
    {
        "num": 11,
        "title": "Масштабирование",
        "subtitle": "Бизнес — Урок 11",
        "sections": [
            {
                "type": "scale_paths",
                "heading": "Пути масштабирования",
                "items": [
                    ("Географический", "Новые города\nи страны"),
                    ("Продуктовый", "Новые продукты\nи услуги"),
                    ("Канальный", "Новые каналы\nпродаж"),
                    ("Партнёрский", "Франшиза\nи лицензии"),
                ],
            },
            {
                "type": "growth_stages",
                "heading": "Стадии роста",
                "items": [
                    ("Запуск", "0→1"),
                    ("Рост", "1→10"),
                    ("Масштаб", "10→100"),
                    ("Зрелость", "100→∞"),
                ],
            },
            {
                "type": "tip",
                "text": "Совет: Не масштабируй сломанную модель. Сначала — работающий юнит-экономика, потом — рост!",
            },
        ],
    },
    {
        "num": 12,
        "title": "Защита бизнес-плана",
        "subtitle": "Бизнес — Урок 12",
        "sections": [
            {
                "type": "pitch_structure",
                "heading": "Структура питча",
                "items": [
                    ("Проблема", "1 мин"),
                    ("Решение", "1 мин"),
                    ("Рынок", "1 мин"),
                    ("Бизнес-модель", "1 мин"),
                    ("Команда", "30 сек"),
                    ("Просьба", "30 сек"),
                ],
            },
            {
                "type": "presentation_tips",
                "heading": "Секреты успешной защиты",
                "items": [
                    "Говори просто и понятно",
                    "Подкрепляй цифрами",
                    "Покажи прототип",
                    "Будь уверен и честен",
                    "Готовься к вопросам",
                ],
            },
            {
                "type": "tip",
                "text": "Совет: Инвесторы инвестируют в людей, а не в идеи. Покажи свою команду и мотивацию!",
            },
        ],
    },
]


def escape(text):
    """Escape text for XML."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def build_svg(lesson):
    """Build an SVG string for a lesson."""
    num = lesson["num"]
    title = lesson["title"]
    subtitle = lesson["subtitle"]
    sections = lesson["sections"]

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <filter id="shadow" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#00000020"/>
    </filter>
    <linearGradient id="headerGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#E65100"/>
      <stop offset="100%" stop-color="#FF8F00"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="500" height="350" rx="12" ry="12" fill="{BG}" stroke="{PRIMARY}" stroke-width="2.5"/>

  <!-- Header bar -->
  <rect x="0" y="0" width="500" height="52" rx="12" ry="12" fill="url(#headerGrad)"/>
  <rect x="0" y="20" width="500" height="32" fill="url(#headerGrad)"/>

  <!-- Title -->
  <text x="250" y="22" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="{WHITE}">{escape(title)}</text>
  <text x="250" y="42" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{LIGHT_ACCENT}">{escape(subtitle)}</text>

  <!-- Lesson number badge -->
  <circle cx="30" cy="26" r="16" fill="{WHITE}" opacity="0.25"/>
  <text x="30" y="31" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{WHITE}">{num}</text>

'''

    y_cursor = 60

    for section in sections:
        stype = section["type"]

        if stype == "concept_boxes":
            heading = section["heading"]
            items = section["items"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 5
            box_y = y_cursor
            box_w = 148
            box_h = 68
            gap = 8
            start_x = 20
            for i, (label, desc) in enumerate(items):
                bx = start_x + i * (box_w + gap)
                svg += f'  <rect x="{bx}" y="{box_y}" width="{box_w}" height="{box_h}" rx="8" ry="8" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.2" filter="url(#shadow)"/>\n'
                svg += f'  <rect x="{bx}" y="{box_y}" width="{box_w}" height="20" rx="8" ry="8" fill="{ACCENT}" opacity="0.2"/>\n'
                svg += f'  <rect x="{bx}" y="{box_y + 12}" width="{box_w}" height="8" fill="{ACCENT}" opacity="0.2"/>\n'
                svg += f'  <text x="{bx + box_w // 2}" y="{box_y + 15}" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{DARK}">{escape(label)}</text>\n'
                lines = desc.split("\n")
                for li, line in enumerate(lines):
                    svg += f'  <text x="{bx + box_w // 2}" y="{box_y + 32 + li * 12}" text-anchor="middle" font-family="Arial, sans-serif" font-size="8.5" fill="{MID}">{escape(line)}</text>\n'
            y_cursor = box_y + box_h + 8

        elif stype == "steps":
            heading = section["heading"]
            items = section["items"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 8
            for i, item in enumerate(items):
                svg += f'  <rect x="25" y="{y_cursor - 9}" width="450" height="18" rx="4" ry="4" fill="{ACCENT}" opacity="{0.12 + i * 0.05}"/>\n'
                svg += f'  <text x="35" y="{y_cursor}" font-family="Arial, sans-serif" font-size="9.5" fill="{DARK}">{escape(item)}</text>\n'
                y_cursor += 21

        elif stype == "criteria_table":
            heading = section["heading"]
            rows = section["rows"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 5
            # Table header
            svg += f'  <rect x="20" y="{y_cursor}" width="460" height="18" rx="4" ry="4" fill="{ACCENT}" opacity="0.3"/>\n'
            svg += f'  <text x="30" y="{y_cursor + 13}" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{DARK}">Критерий</text>\n'
            svg += f'  <text x="430" y="{y_cursor + 13}" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{DARK}">Оценка</text>\n'
            y_cursor += 20
            for i, (criterion, rating) in enumerate(rows):
                bg_opacity = 0.06 if i % 2 == 0 else 0.02
                svg += f'  <rect x="20" y="{y_cursor}" width="460" height="18" rx="2" ry="2" fill="{PRIMARY}" opacity="{bg_opacity}"/>\n'
                svg += f'  <text x="30" y="{y_cursor + 13}" font-family="Arial, sans-serif" font-size="9" fill="{DARK}">{escape(criterion)}</text>\n'
                svg += f'  <text x="430" y="{y_cursor + 13}" font-family="Arial, sans-serif" font-size="9" fill="{PRIMARY}">{escape(rating)}</text>\n'
                y_cursor += 18

        elif stype == "flow_diagram":
            heading = section["heading"]
            items = section["items"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 8
            box_w = 78
            box_h = 50
            gap = 12
            start_x = 20
            for i, item in enumerate(items):
                bx = start_x + i * (box_w + gap)
                # Arrow between boxes
                if i > 0:
                    arrow_x = bx - gap
                    svg += f'  <polygon points="{arrow_x},{y_cursor + box_h // 2 - 4} {arrow_x + 8},{y_cursor + box_h // 2} {arrow_x},{y_cursor + box_h // 2 + 4}" fill="{PRIMARY}" opacity="0.6"/>\n'
                svg += f'  <rect x="{bx}" y="{y_cursor}" width="{box_w}" height="{box_h}" rx="8" ry="8" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.2" filter="url(#shadow)"/>\n'
                lines = item.split("\n")
                total_h = len(lines) * 12
                start_ly = y_cursor + (box_h - total_h) // 2 + 10
                for li, line in enumerate(lines):
                    svg += f'  <text x="{bx + box_w // 2}" y="{start_ly + li * 12}" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{DARK}">{escape(line)}</text>\n'
            y_cursor += box_h + 8

        elif stype == "key_points":
            heading = section["heading"]
            items = section["items"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 8
            col = 0
            col_x = [20, 260]
            for i, item in enumerate(items):
                cx = col_x[col]
                svg += f'  <rect x="{cx}" y="{y_cursor - 9}" width="230" height="18" rx="9" ry="9" fill="{WHITE}" stroke="{ACCENT}" stroke-width="0.8"/>\n'
                svg += f'  <circle cx="{cx + 12}" cy="{y_cursor}" r="4" fill="{ACCENT}"/>\n'
                svg += f'  <text x="{cx + 22}" y="{y_cursor + 3}" font-family="Arial, sans-serif" font-size="9" fill="{DARK}">{escape(item)}</text>\n'
                col += 1
                if col >= 2:
                    col = 0
                    y_cursor += 22

        elif stype == "comparison":
            heading = section["heading"]
            items = section["items"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 5
            box_w = 148
            box_h = 68
            gap = 8
            start_x = 16
            for i, (label, desc) in enumerate(items):
                bx = start_x + i * (box_w + gap)
                fill_alpha = ["0.15", "0.10", "0.08"][i] if i < 3 else "0.10"
                svg += f'  <rect x="{bx}" y="{y_cursor}" width="{box_w}" height="{box_h}" rx="8" ry="8" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.2" filter="url(#shadow)"/>\n'
                svg += f'  <rect x="{bx}" y="{y_cursor}" width="{box_w}" height="22" rx="8" ry="8" fill="{ACCENT}" opacity="{fill_alpha}"/>\n'
                svg += f'  <rect x="{bx}" y="{y_cursor + 14}" width="{box_w}" height="8" fill="{ACCENT}" opacity="{fill_alpha}"/>\n'
                svg += f'  <text x="{bx + box_w // 2}" y="{y_cursor + 16}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="{PRIMARY}">{escape(label)}</text>\n'
                lines = desc.split("\n")
                for li, line in enumerate(lines):
                    svg += f'  <text x="{bx + box_w // 2}" y="{y_cursor + 34 + li * 11}" text-anchor="middle" font-family="Arial, sans-serif" font-size="8.5" fill="{MID}">{escape(line)}</text>\n'
            y_cursor += box_h + 8

        elif stype == "checklist":
            heading = section["heading"]
            items = section["items"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 8
            for i, item in enumerate(items):
                # Checkbox
                svg += f'  <rect x="28" y="{y_cursor - 9}" width="12" height="12" rx="2" ry="2" fill="none" stroke="{ACCENT}" stroke-width="1.2"/>\n'
                svg += f'  <polyline points="{30},{y_cursor - 3} {33},{y_cursor} {38},{y_cursor - 6}" fill="none" stroke="{PRIMARY}" stroke-width="1.5"/>\n'
                svg += f'  <text x="48" y="{y_cursor}" font-family="Arial, sans-serif" font-size="9.5" fill="{DARK}">{escape(item)}</text>\n'
                y_cursor += 18

        elif stype == "segment_diagram":
            heading = section["heading"]
            segments = section["segments"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 5
            box_w = 105
            box_h = 55
            cols = 2
            gap_x = 12
            gap_y = 8
            start_x = 20
            for i, (label, desc) in enumerate(segments):
                row = i // cols
                col = i % cols
                bx = start_x + col * (box_w + gap_x)
                by = y_cursor + row * (box_h + gap_y)
                colors = ["#E65100", "#FF8F00", "#FFB300", "#FFC107"]
                c = colors[i % len(colors)]
                svg += f'  <rect x="{bx}" y="{by}" width="{box_w}" height="{box_h}" rx="8" ry="8" fill="{WHITE}" stroke="{c}" stroke-width="1.5" filter="url(#shadow)"/>\n'
                svg += f'  <rect x="{bx}" y="{by}" width="{box_w}" height="18" rx="8" ry="8" fill="{c}" opacity="0.2"/>\n'
                svg += f'  <rect x="{bx}" y="{by + 10}" width="{box_w}" height="8" fill="{c}" opacity="0.2"/>\n'
                svg += f'  <text x="{bx + box_w // 2}" y="{by + 13}" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{c}">{escape(label)}</text>\n'
                lines = desc.split("\n")
                for li, line in enumerate(lines):
                    svg += f'  <text x="{bx + box_w // 2}" y="{by + 28 + li * 10}" text-anchor="middle" font-family="Arial, sans-serif" font-size="8" fill="{MID}">{escape(line)}</text>\n'
            total_rows = (len(segments) + cols - 1) // cols
            y_cursor = y_cursor + total_rows * (box_h + gap_y) + 4

        elif stype == "persona":
            heading = section["heading"]
            fields = section["fields"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 5
            box_w = 460
            box_h = 72
            bx = 20
            svg += f'  <rect x="{bx}" y="{y_cursor}" width="{box_w}" height="{box_h}" rx="10" ry="10" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.2" filter="url(#shadow)"/>\n'
            # Avatar circle
            svg += f'  <circle cx="{bx + 35}" cy="{y_cursor + box_h // 2}" r="22" fill="{SOFT_BG}" stroke="{ACCENT}" stroke-width="1"/>\n'
            svg += f'  <text x="{bx + 35}" y="{y_cursor + box_h // 2 + 5}" text-anchor="middle" font-family="Arial, sans-serif" font-size="18" fill="{PRIMARY}">👤</text>\n'
            # Fields
            for i, field in enumerate(fields):
                row = i // 2
                col = i % 2
                fx = bx + 70 + col * 200
                fy = y_cursor + 18 + row * 22
                svg += f'  <text x="{fx}" y="{fy}" font-family="Arial, sans-serif" font-size="9.5" fill="{DARK}">{escape(field)}</text>\n'
            y_cursor += box_h + 8

        elif stype == "layers":
            heading = section["heading"]
            items = section["items"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 8
            layer_w = 340
            layer_h = 24
            start_x = 80
            for i, (label, desc, color) in enumerate(items):
                inset = i * 30
                ly = y_cursor + i * (layer_h + 4)
                svg += f'  <rect x="{start_x + inset}" y="{ly}" width="{layer_w - inset * 2}" height="{layer_h}" rx="5" ry="5" fill="{color}" opacity="0.25" stroke="{color}" stroke-width="1"/>\n'
                svg += f'  <text x="{start_x + inset + 10}" y="{ly + 16}" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{DARK}">{escape(label)}</text>\n'
                svg += f'  <text x="{start_x + inset + layer_w - inset * 2 - 10}" y="{ly + 16}" text-anchor="end" font-family="Arial, sans-serif" font-size="8.5" fill="{MID}">{escape(desc)}</text>\n'
            y_cursor += len(items) * (layer_h + 4) + 4

        elif stype == "mvp_cycle":
            heading = section["heading"]
            items = section["items"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 8
            # Draw a circular arrangement
            center_x = 250
            center_y = y_cursor + 40
            radius = 55
            import math
            for i, item in enumerate(items):
                angle = -math.pi / 2 + i * 2 * math.pi / len(items)
                ix = center_x + int(radius * math.cos(angle))
                iy = center_y + int(radius * math.sin(angle))
                lines = item.split("\n")
                bw = 72
                bh = 28 if len(lines) == 1 else 38
                svg += f'  <rect x="{ix - bw // 2}" y="{iy - bh // 2}" width="{bw}" height="{bh}" rx="6" ry="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.2" filter="url(#shadow)"/>\n'
                for li, line in enumerate(lines):
                    total_h = len(lines) * 11
                    start_ly = iy - total_h // 2 + 10 + li * 11
                    svg += f'  <text x="{ix}" y="{start_ly}" text-anchor="middle" font-family="Arial, sans-serif" font-size="8.5" font-weight="bold" fill="{DARK}">{escape(line)}</text>\n'
                # Arrow to next
                next_i = (i + 1) % len(items)
                next_angle = -math.pi / 2 + next_i * 2 * math.pi / len(items)
                nx = center_x + int(radius * math.cos(next_angle))
                ny = center_y + int(radius * math.sin(next_angle))
                # Simple line
                dx = nx - ix
                dy = ny - iy
                length = math.sqrt(dx * dx + dy * dy)
                if length > 0:
                    ux = dx / length
                    uy = dy / length
                    sx = ix + int(ux * 28)
                    sy = iy + int(uy * 18)
                    ex = nx - int(ux * 28)
                    ey = ny - int(uy * 18)
                    svg += f'  <line x1="{sx}" y1="{sy}" x2="{ex}" y2="{ey}" stroke="{PRIMARY}" stroke-width="1" opacity="0.4"/>\n'
                    # Arrowhead
                    svg += f'  <polygon points="{ex},{ey} {ex - int(ux * 6 - uy * 3)},{ey - int(uy * 6 + ux * 3)} {ex - int(ux * 6 + uy * 3)},{ey - int(uy * 6 - ux * 3)}" fill="{PRIMARY}" opacity="0.5"/>\n'
            y_cursor = center_y + 65

        elif stype == "channels":
            heading = section["heading"]
            items = section["items"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 5
            box_w = 105
            box_h = 55
            cols = 2
            gap_x = 12
            gap_y = 8
            start_x = 20
            for i, (label, desc) in enumerate(items):
                row = i // cols
                col = i % cols
                bx = start_x + col * (box_w + gap_x)
                by = y_cursor + row * (box_h + gap_y)
                svg += f'  <rect x="{bx}" y="{by}" width="{box_w}" height="{box_h}" rx="8" ry="8" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.2" filter="url(#shadow)"/>\n'
                svg += f'  <rect x="{bx}" y="{by}" width="{box_w}" height="18" rx="8" ry="8" fill="{ACCENT}" opacity="0.2"/>\n'
                svg += f'  <rect x="{bx}" y="{by + 10}" width="{box_w}" height="8" fill="{ACCENT}" opacity="0.2"/>\n'
                svg += f'  <text x="{bx + box_w // 2}" y="{by + 14}" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY}">{escape(label)}</text>\n'
                lines = desc.split("\n")
                for li, line in enumerate(lines):
                    svg += f'  <text x="{bx + box_w // 2}" y="{by + 30 + li * 10}" text-anchor="middle" font-family="Arial, sans-serif" font-size="8.5" fill="{MID}">{escape(line)}</text>\n'
            total_rows = (len(items) + cols - 1) // cols
            y_cursor = y_cursor + total_rows * (box_h + gap_y) + 4

        elif stype == "funnel":
            heading = section["heading"]
            items = section["items"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 8
            funnel_x = 130
            funnel_w = 280
            step_h = 22
            for i, (label, width_pct) in enumerate(items):
                w = int(funnel_w * width_pct / 200)
                offset = (funnel_w - w) // 2
                fy = y_cursor + i * (step_h + 3)
                opacity = 0.15 + i * 0.12
                svg += f'  <rect x="{funnel_x + offset}" y="{fy}" width="{w}" height="{step_h}" rx="4" ry="4" fill="{PRIMARY}" opacity="{opacity}"/>\n'
                svg += f'  <text x="{funnel_x + offset + w // 2}" y="{fy + 15}" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{WHITE if opacity > 0.25 else DARK}">{escape(label)}</text>\n'
            y_cursor += len(items) * (step_h + 3) + 4

        elif stype == "objection_boxes":
            heading = section["heading"]
            items = section["items"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 5
            box_w = 148
            box_h = 60
            gap = 8
            start_x = 16
            for i, (objection, response) in enumerate(items):
                bx = start_x + i * (box_w + gap)
                by = y_cursor
                svg += f'  <rect x="{bx}" y="{by}" width="{box_w}" height="{box_h}" rx="8" ry="8" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.2" filter="url(#shadow)"/>\n'
                svg += f'  <rect x="{bx}" y="{by}" width="{box_w}" height="20" rx="8" ry="8" fill="#E65100" opacity="0.15"/>\n'
                svg += f'  <rect x="{bx}" y="{by + 12}" width="{box_w}" height="8" fill="#E65100" opacity="0.15"/>\n'
                svg += f'  <text x="{bx + box_w // 2}" y="{by + 14}" text-anchor="middle" font-family="Arial, sans-serif" font-size="9.5" font-weight="bold" fill="#C62828">{escape(objection)}</text>\n'
                lines = response.split("\n")
                for li, line in enumerate(lines):
                    svg += f'  <text x="{bx + box_w // 2}" y="{by + 32 + li * 11}" text-anchor="middle" font-family="Arial, sans-serif" font-size="8" fill="{MID}">{escape(line)}</text>\n'
            y_cursor += box_h + 8

        elif stype == "formula_boxes":
            heading = section["heading"]
            items = section["items"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 5
            box_w = 220
            box_h = 24
            cols = 2
            gap_x = 16
            gap_y = 6
            for i, (name, formula) in enumerate(items):
                row = i // cols
                col = i % cols
                bx = 20 + col * (box_w + gap_x)
                by = y_cursor + row * (box_h + gap_y)
                svg += f'  <rect x="{bx}" y="{by}" width="{box_w}" height="{box_h}" rx="6" ry="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1" filter="url(#shadow)"/>\n'
                svg += f'  <text x="{bx + 8}" y="{by + 16}" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}">{escape(name)}:</text>\n'
                svg += f'  <text x="{bx + 8}" y="{by + 16}" dx="{len(name) * 6 + 10}" font-family="Arial, sans-serif" font-size="8.5" fill="{DARK}">{escape(formula)}</text>\n'
            total_rows = (len(items) + cols - 1) // cols
            y_cursor += total_rows * (box_h + gap_y) + 4

        elif stype == "mini_chart":
            heading = section["heading"]
            bars = section["bars"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 8
            max_val = max(b[1] for b in bars)
            chart_x = 120
            chart_w = 300
            bar_h = 18
            for i, (label, val, color) in enumerate(bars):
                by = y_cursor + i * (bar_h + 4)
                w = int(chart_w * val / max_val)
                svg += f'  <text x="{chart_x - 5}" y="{by + 13}" text-anchor="end" font-family="Arial, sans-serif" font-size="8.5" fill="{MID}">{escape(label)}</text>\n'
                svg += f'  <rect x="{chart_x}" y="{by}" width="{w}" height="{bar_h}" rx="4" ry="4" fill="{color}" opacity="0.7"/>\n'
                svg += f'  <text x="{chart_x + w + 8}" y="{by + 13}" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{DARK}">{val}%</text>\n'
            y_cursor += len(bars) * (bar_h + 4) + 4

        elif stype == "roles":
            heading = section["heading"]
            items = section["items"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 5
            box_w = 105
            box_h = 60
            cols = 2
            gap_x = 12
            gap_y = 8
            start_x = 20
            for i, (role, desc, icon) in enumerate(items):
                row = i // cols
                col = i % cols
                bx = start_x + col * (box_w + gap_x)
                by = y_cursor + row * (box_h + gap_y)
                svg += f'  <rect x="{bx}" y="{by}" width="{box_w}" height="{box_h}" rx="8" ry="8" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.2" filter="url(#shadow)"/>\n'
                svg += f'  <text x="{bx + box_w // 2}" y="{by + 15}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12">{escape(icon)}</text>\n'
                svg += f'  <text x="{bx + box_w // 2}" y="{by + 28}" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}">{escape(role)}</text>\n'
                lines = desc.split("\n")
                for li, line in enumerate(lines):
                    svg += f'  <text x="{bx + box_w // 2}" y="{by + 40 + li * 10}" text-anchor="middle" font-family="Arial, sans-serif" font-size="8" fill="{MID}">{escape(line)}</text>\n'
            total_rows = (len(items) + cols - 1) // cols
            y_cursor = y_cursor + total_rows * (box_h + gap_y) + 4

        elif stype == "scale_paths":
            heading = section["heading"]
            items = section["items"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 5
            box_w = 105
            box_h = 55
            cols = 2
            gap_x = 12
            gap_y = 8
            start_x = 20
            for i, (label, desc) in enumerate(items):
                row = i // cols
                col = i % cols
                bx = start_x + col * (box_w + gap_x)
                by = y_cursor + row * (box_h + gap_y)
                svg += f'  <rect x="{bx}" y="{by}" width="{box_w}" height="{box_h}" rx="8" ry="8" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.2" filter="url(#shadow)"/>\n'
                svg += f'  <rect x="{bx}" y="{by}" width="{box_w}" height="18" rx="8" ry="8" fill="{ACCENT}" opacity="0.2"/>\n'
                svg += f'  <rect x="{bx}" y="{by + 10}" width="{box_w}" height="8" fill="{ACCENT}" opacity="0.2"/>\n'
                svg += f'  <text x="{bx + box_w // 2}" y="{by + 13}" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}">{escape(label)}</text>\n'
                lines = desc.split("\n")
                for li, line in enumerate(lines):
                    svg += f'  <text x="{bx + box_w // 2}" y="{by + 28 + li * 10}" text-anchor="middle" font-family="Arial, sans-serif" font-size="8.5" fill="{MID}">{escape(line)}</text>\n'
            total_rows = (len(items) + cols - 1) // cols
            y_cursor = y_cursor + total_rows * (box_h + gap_y) + 4

        elif stype == "growth_stages":
            heading = section["heading"]
            items = section["items"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 8
            box_w = 100
            box_h = 42
            gap = 12
            start_x = 20
            for i, (stage, metric) in enumerate(items):
                bx = start_x + i * (box_w + gap)
                by = y_cursor
                opacities = [0.2, 0.35, 0.55, 0.75]
                op = opacities[i % len(opacities)]
                svg += f'  <rect x="{bx}" y="{by}" width="{box_w}" height="{box_h}" rx="8" ry="8" fill="{PRIMARY}" opacity="{op}" filter="url(#shadow)"/>\n'
                svg += f'  <text x="{bx + box_w // 2}" y="{by + 17}" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{WHITE}">{escape(stage)}</text>\n'
                svg += f'  <text x="{bx + box_w // 2}" y="{by + 33}" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{LIGHT_ACCENT}">{escape(metric)}</text>\n'
            y_cursor += box_h + 8

        elif stype == "pitch_structure":
            heading = section["heading"]
            items = section["items"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 5
            # Two columns
            col1_x = 20
            col2_x = 260
            col_w = 220
            row_h = 20
            for i, (part, time) in enumerate(items):
                col = i // 3
                row = i % 3
                bx = col1_x if col == 0 else col2_x
                by = y_cursor + row * (row_h + 4)
                svg += f'  <rect x="{bx}" y="{by}" width="{col_w}" height="{row_h}" rx="6" ry="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1" filter="url(#shadow)"/>\n'
                svg += f'  <text x="{bx + 10}" y="{by + 14}" font-family="Arial, sans-serif" font-size="9.5" font-weight="bold" fill="{PRIMARY}">{escape(part)}</text>\n'
                # Time badge
                svg += f'  <rect x="{bx + col_w - 50}" y="{by + 3}" width="42" height="14" rx="7" ry="7" fill="{ACCENT}" opacity="0.2"/>\n'
                svg += f'  <text x="{bx + col_w - 29}" y="{by + 14}" text-anchor="middle" font-family="Arial, sans-serif" font-size="8" fill="{PRIMARY}">{escape(time)}</text>\n'
            y_cursor += 3 * (row_h + 4) + 8

        elif stype == "presentation_tips":
            heading = section["heading"]
            items = section["items"]
            svg += f'  <!-- Section: {escape(heading)} -->\n'
            svg += f'  <text x="20" y="{y_cursor}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{escape(heading)}</text>\n'
            y_cursor += 8
            col = 0
            col_x = [20, 260]
            for i, item in enumerate(items):
                cx = col_x[col]
                svg += f'  <rect x="{cx}" y="{y_cursor - 9}" width="230" height="18" rx="9" ry="9" fill="{WHITE}" stroke="{ACCENT}" stroke-width="0.8"/>\n'
                # Star icon
                svg += f'  <text x="{cx + 12}" y="{y_cursor + 3}" font-family="Arial, sans-serif" font-size="9" fill="{ACCENT}">★</text>\n'
                svg += f'  <text x="{cx + 24}" y="{y_cursor + 3}" font-family="Arial, sans-serif" font-size="9" fill="{DARK}">{escape(item)}</text>\n'
                col += 1
                if col >= 2:
                    col = 0
                    y_cursor += 22
            if col != 0:
                y_cursor += 22

        # Tip section (common)
        if section["type"] == "tip":
            text = section["text"]
            svg += f'  <!-- Tip -->\n'
            tip_y = 325
            svg += f'  <rect x="15" y="{tip_y}" width="470" height="18" rx="9" ry="9" fill="{PRIMARY}" opacity="0.1"/>\n'
            svg += f'  <text x="250" y="{tip_y + 13}" text-anchor="middle" font-family="Arial, sans-serif" font-size="8.5" font-style="italic" fill="{DARK}">{escape(text)}</text>\n'

    # Footer
    svg += f'''
  <!-- Footer -->
  <line x1="20" y1="343" x2="480" y2="343" stroke="{ACCENT}" stroke-width="0.5" opacity="0.5"/>
  <text x="250" y="340" text-anchor="middle" font-family="Arial, sans-serif" font-size="8" fill="{MID}" opacity="0.7">Бизнес · 10 класс</text>
</svg>'''
    return svg


def main():
    validated_count = 0
    failed = []

    for lesson in LESSONS:
        num = lesson["num"]
        svg_content = build_svg(lesson)
        filepath = os.path.join(OUTPUT_DIR, f"lesson{num}.svg")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)

        # Validate as proper XML
        try:
            ET.parse(filepath)
            validated_count += 1
            print(f"  ✅ lesson{num}.svg — valid XML ({len(svg_content)} bytes)")
        except ET.ParseError as e:
            failed.append((num, str(e)))
            print(f"  ❌ lesson{num}.svg — INVALID XML: {e}")

    print(f"\n{'='*50}")
    print(f"Generated: {len(LESSONS)} files")
    print(f"Validated: {validated_count}/{len(LESSONS)} passed XML validation")
    if failed:
        print(f"Failed: {failed}")
    else:
        print("All SVGs are valid XML! ✅")


if __name__ == "__main__":
    main()
