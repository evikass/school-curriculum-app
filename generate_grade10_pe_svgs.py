#!/usr/bin/env python3
"""Generate 12 detailed SVG files for Grade 10 Physical Education (Физкультура) lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade10/pe"

# Color scheme
PRIMARY = "#2E7D32"
PRIMARY_LIGHT = "#4CAF50"
PRIMARY_DARK = "#1B5E20"
BG = "#E8F5E9"
BG_WHITE = "#FFFFFF"
ACCENT = "#66BB6A"
TEXT_DARK = "#1B5E20"
TEXT_MED = "#2E7D32"
TEXT_LIGHT = "#555555"
BORDER = "#2E7D32"
BOX_BG = "#F1F8E9"
BOX_BORDER = "#A5D6A7"
HIGHLIGHT = "#C8E6C9"

LESSONS = [
    {
        "num": 1,
        "title": "Здоровый образ жизни и его компоненты",
        "filename": "lesson1-healthy-lifestyle.svg",
        "content": {
            "boxes": [
                {"x": 20, "y": 68, "w": 220, "h": 125, "title": "Компоненты ЗОЖ",
                 "items": ["• Рациональное питание", "• Двигательная активность", "• Закаливание организма", "• Личная гигиена", "• Отказ от вредных привычек"]},
                {"x": 260, "y": 68, "w": 220, "h": 125, "title": "Режим дня",
                 "items": ["• Сон 7-8 часов", "• Регулярные тренировки", "• Чередование труда/отдыха", "• Прогулки на воздухе", "• Водные процедуры"]},
                {"x": 20, "y": 203, "w": 220, "h": 105, "title": "Питание",
                 "items": ["• Белки, жиры, углеводы", "• Витамины и минералы", "• Режим: 3-5 раз/день", "• Вода: 1.5-2 л/день"]},
                {"x": 260, "y": 203, "w": 220, "h": 105, "title": "Вредные привычки",
                 "items": ["• Курение — риск рака", "• Алкоголь — разрушение ЦНС", "• Наркотики — зависимость", "• Малоактивный образ жизни"]},
            ],
            "diagram": None,
        }
    },
    {
        "num": 2,
        "title": "Двигательная активность и здоровье",
        "filename": "lesson2-motor-activity.svg",
        "content": {
            "boxes": [
                {"x": 20, "y": 68, "w": 220, "h": 120, "title": "Влияние на организм",
                 "items": ["• Укрепление сердечно-сосудистой", "• Улучшение дыхания", "• Развитие мышц и костей", "• Повышение иммунитета"]},
                {"x": 260, "y": 68, "w": 220, "h": 120, "title": "Нормы активности",
                 "items": ["• Подростки: 60 мин/день", "• Аэробная: 3-5 раз/нед.", "• Силовая: 2-3 раз/нед.", "• Растяжка: ежедневно"]},
                {"x": 20, "y": 198, "w": 220, "h": 110, "title": "Гиподинамия",
                 "items": ["• Слабость мышц и связок", "• Нарушение осанки", "• Избыточный вес", "• Снижение работоспособности"]},
                {"x": 260, "y": 198, "w": 220, "h": 110, "title": "Пульс и нагрузка",
                 "items": ["• Макс. ЧСС = 220 - возраст", "• Зона здоровья: 50-60%", "• Аэробная зона: 60-75%", "• Контроль самочувствия"]},
            ],
        }
    },
    {
        "num": 3,
        "title": "Оценка физической подготовленности",
        "filename": "lesson3-fitness-assessment.svg",
        "content": {
            "boxes": [
                {"x": 20, "y": 68, "w": 220, "h": 115, "title": "Тесты ГТО",
                 "items": ["• Бег 30 м — скорость", "• Бег 1000/2000 м — вынослив.", "• Подтягивание — сила", "• Наклон вперёд — гибкость"]},
                {"x": 260, "y": 68, "w": 220, "h": 115, "title": "Нормативы (юноши)",
                 "items": ["• Бег 100 м: 13.8-15.0 с", "• Бег 2000 м: 8.20-10.00 мин", "• Подтягивание: 9-12 раз", "• Прыжок в длину: 200-240 см"]},
                {"x": 20, "y": 193, "w": 220, "h": 115, "title": "Нормативы (девушки)",
                 "items": ["• Бег 100 м: 16.0-17.5 с", "• Бег 2000 м: 10.00-12.00 мин", "• Отжимание: 10-17 раз", "• Прыжок в длину: 170-200 см"]},
                {"x": 260, "y": 193, "w": 220, "h": 115, "title": "Самоконтроль",
                 "items": ["• Ведение дневника тренировок", "• Замеры ЧСС до/после", "• Контроль веса и роста", "• Оценка самочувствия"]},
            ],
        }
    },
    {
        "num": 4,
        "title": "Бег на средние и длинные дистанции",
        "filename": "lesson4-distance-running.svg",
        "content": {
            "boxes": [
                {"x": 20, "y": 68, "w": 220, "h": 110, "title": "Техника бега",
                 "items": ["• Постановка с передней части", "• Угол наклона туловища 4-5°", "• Работа рук: плечи расслабл.", "• Частота шагов: 160-180/мин"]},
                {"x": 260, "y": 68, "w": 220, "h": 110, "title": "Дыхание",
                 "items": ["• Ритм: 3-3 или 2-2 шага", "• Вдох через нос и рот", "• Глубокий выдох", "• «Второе дыхание» на 3-5 км"]},
                {"x": 20, "y": 188, "w": 220, "h": 120, "title": "Тактика бега",
                 "items": ["• Равномерный темп — лучший", "• Старт: 90-95% от макс.", "• Финишный спурт: 200-400 м", "• Не резко менять скорость"]},
                {"x": 260, "y": 188, "w": 220, "h": 120, "title": "Дистанции",
                 "items": ["• 800 м — средняя", "• 1500 м — средняя", "• 3000 м — длинная", "• 5000 м — длинная"]},
            ],
        }
    },
    {
        "num": 5,
        "title": "Прыжки и метания",
        "filename": "lesson5-jumps-throws.svg",
        "content": {
            "boxes": [
                {"x": 20, "y": 68, "w": 220, "h": 115, "title": "Прыжок в длину",
                 "items": ["• Разбег: 18-22 шага", "• Отталкивание: 70-75°", "• Полёт: «согнув ноги»", "• Приземление: на пятки"]},
                {"x": 260, "y": 68, "w": 220, "h": 115, "title": "Прыжок в высоту",
                 "items": ["• Способ «фосбюри-флоп»", "• Дуговой разбег 8-10 шагов", "• Отталкивание дальней ногой", "• Переход через планку спиной"]},
                {"x": 20, "y": 193, "w": 220, "h": 115, "title": "Метание мяча",
                 "items": ["• Хват: из-за головы", "• Разбег: 3-5 бросковых шагов", "• «Натянутый лук» — финал", "• Выпуск под углом 40-45°"]},
                {"x": 260, "y": 193, "w": 220, "h": 115, "title": "Метание гранаты",
                 "items": ["• Хват за ручку снизу", "• Разбег: 10-12 м", "• Скрестный шаг", "• Бросок из-за головы"]},
            ],
        }
    },
    {
        "num": 6,
        "title": "Баскетбол: техника и тактика",
        "filename": "lesson6-basketball.svg",
        "content": {
            "boxes": [
                {"x": 20, "y": 68, "w": 220, "h": 115, "title": "Техника владения мячом",
                 "items": ["• Ведение: пальцы, не ладонь", "• Передача двумя руками", "• Бросок «в прыжке»", "• Подбор щита (отскок)"]},
                {"x": 260, "y": 68, "w": 220, "h": 115, "title": "Правила игры",
                 "items": ["• 5 игроков на площадке", "• 4 четверти по 10 мин", "• 3-очковая линия: 6.75 м", "• Фол: 5 личных — удаление"]},
                {"x": 20, "y": 193, "w": 220, "h": 115, "title": "Тактика нападения",
                 "items": ["• Быстрый отрыв (fast break)", "• «Заслон» — наведение", "• Передача «в разрез»", "• Расположение 3-2 / 2-3"]},
                {"x": 260, "y": 193, "w": 220, "h": 115, "title": "Тактика защиты",
                 "items": ["• Личная опека (man-to-man)", "• Зонная защита 2-1-2", "• Прессинг по всей площадке", "• Подстраховка партнёра"]},
            ],
        }
    },
    {
        "num": 7,
        "title": "Волейбол: техника и тактика",
        "filename": "lesson7-volleyball.svg",
        "content": {
            "boxes": [
                {"x": 20, "y": 68, "w": 220, "h": 115, "title": "Основные приёмы",
                 "items": ["• Нижняя передача (приём)", "• Верхняя передача (связка)", "• Нападающий удар", "• Блокирование"]},
                {"x": 260, "y": 68, "w": 220, "h": 115, "title": "Правила игры",
                 "items": ["• 6 игроков на площадке", "• 5 партий до 25 очков", "• 3 касания на сторону", "• Пятая партия до 15 очков"]},
                {"x": 20, "y": 193, "w": 220, "h": 115, "title": "Подача мяча",
                 "items": ["• Нижняя прямая подача", "• Верхняя прямая подача", "• Подача в прыжке (силовая)", "• Цель: слабый игрок"]},
                {"x": 260, "y": 193, "w": 220, "h": 115, "title": "Расстановки",
                 "items": ["• 4-2: 2 связующих", "• 5-1: 1 связующий", "• Переход: по часовой стрелке", "• Либеро — защита"]},
            ],
        }
    },
    {
        "num": 8,
        "title": "Футбол: техника и тактика",
        "filename": "lesson8-football.svg",
        "content": {
            "boxes": [
                {"x": 20, "y": 68, "w": 220, "h": 115, "title": "Техника владения мячом",
                 "items": ["• Ведение внутренней частью", "• Остановка подошвой", "• Передача (пас) низом", "• Удар внутренней подъёмом"]},
                {"x": 260, "y": 68, "w": 220, "h": 115, "title": "Правила игры",
                 "items": ["• 11 игроков на поле", "• 2 тайма по 45 минут", "• Офсайд — вне игры", "• Жёлтая/красная карточки"]},
                {"x": 20, "y": 193, "w": 220, "h": 115, "title": "Тактика нападения",
                 "items": ["• Пас «на ход» партнёру", "• «Стенка» — комбинация", "• Фланговый прорыв", "• Стандартные положения"]},
                {"x": 260, "y": 193, "w": 220, "h": 115, "title": "Тактика защиты",
                 "items": ["• Персональная опека", "• Зонная оборона", "• Офсайдная ловушка", "• Плотность обороны"]},
            ],
        }
    },
    {
        "num": 9,
        "title": "Акробатические упражнения",
        "filename": "lesson9-acrobatics.svg",
        "content": {
            "boxes": [
                {"x": 20, "y": 68, "w": 220, "h": 115, "title": "Кувырки",
                 "items": ["• Кувырок вперёд: группир.", "• Кувырок назад: толчок", "• Длинный кувырок", "• Стойка на лопатках"]},
                {"x": 260, "y": 68, "w": 220, "h": 115, "title": "Равновесие",
                 "items": ["• Стойка на руках (у стены)", "• Мост из положения лёжа", "• «Ласточка» — равновесие", "• Шпагат продольный/поперечн."]},
                {"x": 20, "y": 193, "w": 220, "h": 115, "title": "Техника безопасности",
                 "items": ["• Мат всегда под телом", "• Страховка партнёром", "• Разминка обязательна", "• Без украшений и часов"]},
                {"x": 260, "y": 193, "w": 220, "h": 115, "title": "Связки элементов",
                 "items": ["• Кувырок → стойка → мост", "• Два кувырка вперёд", "• Кувырок → «ласточка»", "• Комбинация из 4-5 элем."]},
            ],
        }
    },
    {
        "num": 10,
        "title": "Опорный прыжок",
        "filename": "lesson10-vault.svg",
        "content": {
            "boxes": [
                {"x": 20, "y": 68, "w": 220, "h": 115, "title": "Фазы прыжка",
                 "items": ["• Разбег: 15-20 м (макс.)", "• Наскок на мостик: 2 ноги", "• Толчок руками о коня", "• Приземление: на носки→пятки"]},
                {"x": 260, "y": 68, "w": 220, "h": 115, "title": "Виды прыжков",
                 "items": ["• Прыжок ноги врозь", "• Прыжок согнув ноги", "• Прыжок боком (конь в дл.)", "• Прыжок прогнувшись"]},
                {"x": 20, "y": 193, "w": 220, "h": 115, "title": "Техника разбега",
                 "items": ["• Ускорение к мостику", "• Длина: 15-20 м", "• Наскок чуть согнув ноги", "• Мах руками вверх-вперёд"]},
                {"x": 260, "y": 193, "w": 220, "h": 115, "title": "Безопасность",
                 "items": ["• Страховка у снаряда", "• Проверка креплений", "• Мостик устойчиво стоит", "• Приземление в упор присев"]},
            ],
        }
    },
    {
        "num": 11,
        "title": "Развитие физических качеств",
        "filename": "lesson11-physical-qualities.svg",
        "content": {
            "boxes": [
                {"x": 20, "y": 68, "w": 220, "h": 115, "title": "5 физических качеств",
                 "items": ["• Сила — преодоление сопротивл.", "• Быстрота — скорость реакции", "• Выносливость — длит. работа", "• Гибкость — амплитуда движ.", "• Ловкость — координация"]},
                {"x": 260, "y": 68, "w": 220, "h": 115, "title": "Методы развития силы",
                 "items": ["• Повторный: 6-10 повтор.", "• Изометрический: 5-6 сек", "• Круговая тренировка", "• Отягощение 60-80% от макс."]},
                {"x": 20, "y": 193, "w": 220, "h": 115, "title": "Развитие выносливости",
                 "items": ["• Равномерный бег 15-30 мин", "• Интервальный: 200м×8-10", "• Кросс по пересеч. местности", "• Плавание 20-40 мин"]},
                {"x": 260, "y": 193, "w": 220, "h": 115, "title": "Развитие гибкости",
                 "items": ["• Статич. растяжка 15-30 сек", "• Динамич. махи 10-15 раз", "• Упр. с партнёром", "• Регулярность: ежедневно"]},
            ],
        }
    },
    {
        "num": 12,
        "title": "Профессионально-прикладная физическая подготовка",
        "filename": "lesson12-applied-training.svg",
        "content": {
            "boxes": [
                {"x": 20, "y": 68, "w": 220, "h": 115, "title": "Цели ППФП",
                 "items": ["• Подготовка к профессии", "• Развитие спец. качеств", "• Формирование прикладн. нав.", "• Профилактика проф. заболеваний"]},
                {"x": 260, "y": 68, "w": 220, "h": 115, "title": "Профессии и качества",
                 "items": ["• Программист: осанка, зрение", "• Строитель: сила, вынослив.", "• Водитель: реакция, вниман.", "• Учитель: голос, вынослив."]},
                {"x": 20, "y": 193, "w": 220, "h": 115, "title": "Прикладные упражнения",
                 "items": ["• Упр. на координацию", "• Статические удержания", "• Развитие вестиб. аппарата", "• Дыхательная гимнастика"]},
                {"x": 260, "y": 193, "w": 220, "h": 115, "title": "Профилактика",
                 "items": ["• Паузы: каждые 45 мин", "• Гимнастика для глаз", "• Упр. для осанки", "• Комплекс производ. гимн."]},
            ],
        }
    },
]


def escape_xml(text: str) -> str:
    """Escape special XML characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def build_svg(lesson: dict) -> str:
    n = lesson["num"]
    title = lesson["title"]
    boxes = lesson["content"]["boxes"]

    lines = []
    lines.append('<?xml version="1.0" encoding="UTF-8"?>')
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">')

    # Defs for styles and gradients
    lines.append('  <defs>')
    lines.append(f'    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">')
    lines.append(f'      <stop offset="0%" style="stop-color:{PRIMARY_DARK};stop-opacity:1" />')
    lines.append(f'      <stop offset="100%" style="stop-color:{PRIMARY};stop-opacity:1" />')
    lines.append('    </linearGradient>')
    lines.append(f'    <linearGradient id="footerGrad" x1="0%" y1="0%" x2="100%" y2="0%">')
    lines.append(f'      <stop offset="0%" style="stop-color:{PRIMARY};stop-opacity:1" />')
    lines.append(f'      <stop offset="100%" style="stop-color:{PRIMARY_DARK};stop-opacity:1" />')
    lines.append('    </linearGradient>')
    lines.append('  </defs>')

    # Background
    lines.append(f'  <rect x="0" y="0" width="500" height="350" rx="12" ry="12" fill="{BG}" stroke="{BORDER}" stroke-width="2.5"/>')

    # Header bar
    lines.append(f'  <rect x="0" y="0" width="500" height="52" rx="12" ry="12" fill="url(#headerGrad)"/>')
    lines.append(f'  <rect x="0" y="30" width="500" height="22" fill="url(#headerGrad)"/>')  # fill corners

    # Lesson number badge
    badge_x = 14
    badge_y = 10
    lines.append(f'  <rect x="{badge_x}" y="{badge_y}" width="32" height="32" rx="6" ry="6" fill="{BG_WHITE}" opacity="0.2"/>')
    lines.append(f'  <text x="{badge_x + 16}" y="{badge_y + 23}" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="{BG_WHITE}">{n}</text>')

    # Title text
    lines.append(f'  <text x="56" y="24" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{BG_WHITE}">{escape_xml(title)}</text>')
    lines.append(f'  <text x="56" y="42" font-family="Arial, sans-serif" font-size="10" fill="{HIGHLIGHT}">Физкультура — Урок {n}</text>')

    # Decorative line below header
    lines.append(f'  <line x1="15" y1="54" x2="485" y2="54" stroke="{ACCENT}" stroke-width="1" opacity="0.5"/>')

    # Content boxes
    for box in boxes:
        bx, by, bw, bh = box["x"], box["y"], box["w"], box["h"]
        btitle = box["title"]
        items = box["items"]

        # Box background
        lines.append(f'  <rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="6" ry="6" fill="{BOX_BG}" stroke="{BOX_BORDER}" stroke-width="1"/>')

        # Box title bar
        lines.append(f'  <rect x="{bx}" y="{by}" width="{bw}" height="22" rx="6" ry="6" fill="{PRIMARY}" opacity="0.85"/>')
        lines.append(f'  <rect x="{bx}" y="{by + 12}" width="{bw}" height="10" fill="{PRIMARY}" opacity="0.85"/>')
        lines.append(f'  <text x="{bx + bw // 2}" y="{by + 15}" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{BG_WHITE}">{escape_xml(btitle)}</text>')

        # Box items
        item_y = by + 36
        for item in items:
            lines.append(f'  <text x="{bx + 8}" y="{item_y}" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_MED}">{escape_xml(item)}</text>')
            item_y += 14

    # Decorative sport icons (simplified SVG shapes)
    # Add a small sport-related icon based on lesson number
    icon_x = 240
    icon_y = 322
    if n in [4, 5]:
        # Running figure (simplified)
        lines.append(f'  <g transform="translate({icon_x}, {icon_y - 8}) scale(0.5)" opacity="0.3">')
        lines.append(f'    <circle cx="12" cy="4" r="4" fill="{PRIMARY}"/>')
        lines.append(f'    <line x1="12" y1="8" x2="12" y2="22" stroke="{PRIMARY}" stroke-width="2"/>')
        lines.append(f'    <line x1="12" y1="22" x2="6" y2="32" stroke="{PRIMARY}" stroke-width="2"/>')
        lines.append(f'    <line x1="12" y1="22" x2="18" y2="32" stroke="{PRIMARY}" stroke-width="2"/>')
        lines.append(f'    <line x1="12" y1="12" x2="4" y2="20" stroke="{PRIMARY}" stroke-width="2"/>')
        lines.append(f'    <line x1="12" y1="12" x2="20" y2="8" stroke="{PRIMARY}" stroke-width="2"/>')
        lines.append('  </g>')
    elif n in [6, 7, 8]:
        # Ball icon
        lines.append(f'  <circle cx="{icon_x + 6}" cy="{icon_y - 2}" r="8" fill="none" stroke="{PRIMARY}" stroke-width="1.5" opacity="0.3"/>')
        lines.append(f'  <path d="M{icon_x + 6},{icon_y - 10} Q{icon_x + 2},{icon_y - 2} {icon_x + 6},{icon_y + 6}" fill="none" stroke="{PRIMARY}" stroke-width="1" opacity="0.3"/>')
    elif n in [9, 10]:
        # Gymnastics figure
        lines.append(f'  <g transform="translate({icon_x}, {icon_y - 10}) scale(0.5)" opacity="0.3">')
        lines.append(f'    <circle cx="12" cy="4" r="4" fill="{PRIMARY}"/>')
        lines.append(f'    <line x1="12" y1="8" x2="12" y2="22" stroke="{PRIMARY}" stroke-width="2"/>')
        lines.append(f'    <line x1="4" y1="12" x2="20" y2="12" stroke="{PRIMARY}" stroke-width="2"/>')
        lines.append(f'    <line x1="12" y1="22" x2="6" y2="32" stroke="{PRIMARY}" stroke-width="2"/>')
        lines.append(f'    <line x1="12" y1="22" x2="18" y2="32" stroke="{PRIMARY}" stroke-width="2"/>')
        lines.append('  </g>')
    elif n == 1:
        # Heart icon for healthy lifestyle
        lines.append(f'  <path d="M{icon_x + 6},{icon_y + 2} C{icon_x + 6},{icon_y - 2} {icon_x},{icon_y - 6} {icon_x},{icon_y - 2} C{icon_x},{icon_y + 1} {icon_x + 6},{icon_y + 5} {icon_x + 6},{icon_y + 2} Z" fill="{PRIMARY}" opacity="0.25"/>')
    elif n == 3:
        # Stopwatch icon
        lines.append(f'  <circle cx="{icon_x + 6}" cy="{icon_y - 2}" r="7" fill="none" stroke="{PRIMARY}" stroke-width="1.5" opacity="0.3"/>')
        lines.append(f'  <line x1="{icon_x + 6}" y1="{icon_y - 2}" x2="{icon_x + 6}" y2="{icon_y - 7}" stroke="{PRIMARY}" stroke-width="1.5" opacity="0.3"/>')
    elif n == 11:
        # Dumbbell icon
        lines.append(f'  <g transform="translate({icon_x - 4}, {icon_y - 6})" opacity="0.3">')
        lines.append(f'    <rect x="0" y="3" width="4" height="8" rx="1" fill="{PRIMARY}"/>')
        lines.append(f'    <rect x="16" y="3" width="4" height="8" rx="1" fill="{PRIMARY}"/>')
        lines.append(f'    <line x1="4" y1="7" x2="16" y2="7" stroke="{PRIMARY}" stroke-width="2"/>')
        lines.append('  </g>')

    # Footer
    lines.append(f'  <rect x="0" y="330" width="500" height="20" rx="0" ry="0" fill="url(#footerGrad)"/>')
    # Bottom rounded corners overlay
    lines.append(f'  <rect x="0" y="338" width="500" height="12" rx="12" ry="12" fill="url(#footerGrad)"/>')
    lines.append(f'  <rect x="0" y="330" width="500" height="8" fill="url(#footerGrad)"/>')
    lines.append(f'  <text x="250" y="344" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="{BG_WHITE}">Физкультура · 10 класс</text>')

    lines.append('</svg>')
    return "\n".join(lines)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    generated = 0
    errors = []

    for lesson in LESSONS:
        svg_content = build_svg(lesson)
        filepath = os.path.join(OUTPUT_DIR, lesson["filename"])

        # Write file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)

        # Validate as XML
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            if root.tag != "{http://www.w3.org/2000/svg}svg":
                errors.append(f"Lesson {lesson['num']}: Root tag is not <svg>")
                continue
            generated += 1
            print(f"✅ Lesson {lesson['num']:2d}: {lesson['filename']}")
        except ET.ParseError as e:
            errors.append(f"Lesson {lesson['num']}: XML parse error: {e}")
            print(f"❌ Lesson {lesson['num']:2d}: XML parse error: {e}")

    print(f"\n{'='*50}")
    print(f"Generated: {generated}/{len(LESSONS)} SVG files")
    print(f"Output directory: {OUTPUT_DIR}")

    if errors:
        print(f"\n⚠️  Errors ({len(errors)}):")
        for err in errors:
            print(f"  - {err}")
    else:
        print("\n🎉 All SVGs validated successfully as proper XML!")

    # Additional validation: check all files exist
    all_exist = True
    for lesson in LESSONS:
        fp = os.path.join(OUTPUT_DIR, lesson["filename"])
        if not os.path.exists(fp):
            print(f"  MISSING: {fp}")
            all_exist = False
        else:
            size = os.path.getsize(fp)
            if size < 500:
                print(f"  WARNING: {lesson['filename']} is suspiciously small ({size} bytes)")
                all_exist = False

    if all_exist:
        print("✅ All files exist with reasonable sizes.")


if __name__ == "__main__":
    main()
