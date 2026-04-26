#!/usr/bin/env python3
"""
Generate 12 detailed SVG files for Grade 10 Career Guidance (Профориентация) lessons.
Color scheme: teal (#00695C) primary, (#E0F2F1) background
"""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade10/career"

# Colors
PRIMARY = "#00695C"
PRIMARY_DARK = "#004D40"
PRIMARY_LIGHT = "#E0F2F1"
ACCENT = "#26A69A"
ACCENT2 = "#80CBC4"
TEXT_DARK = "#004D40"
TEXT_MED = "#00695C"
TEXT_LIGHT = "#555555"
WHITE = "#FFFFFF"
BG_GRAD_TOP = "#E0F2F1"
BG_GRAD_BOT = "#FFFFFF"

LESSONS = [
    {
        "num": 1,
        "title": "Самоопределение",
        "subtitle": "Профориентация — Урок 1",
        "content": {
            "left_boxes": [
                {"title": "Кто я?", "items": ["Интересы и увлечения", "Сильные стороны", "Ценности и приоритеты", "Темперамент"]},
                {"title": "Самоанализ", "items": ["Тесты: Холланд, Майерс-Бриггс", "Дневник достижений", "Обратная связь от окружающих"]},
            ],
            "right_boxes": [
                {"title": "Формула выбора", "items": ["ХОЧУ — мотивация", "МОГУ — способности", "НАДО — востребованность"]},
                {"title": "Шаги", "items": ["1. Опишите себя", "2. Выявите таланты", "3. Составьте карту интересов", "4. Сузьте выбор"]},
            ],
            "center_icon": "compass",
        }
    },
    {
        "num": 2,
        "title": "Мир профессий",
        "subtitle": "Профориентация — Урок 2",
        "content": {
            "left_boxes": [
                {"title": "Классификация", "items": ["Человек—Природа", "Человек—Техника", "Человек—Человек", "Человек—Знаковая система", "Человек—Художественный образ"]},
            ],
            "right_boxes": [
                {"title": "Тренды рынка", "items": ["IT и цифровые профессии", "Биотехнологии", "Зелёная экономика", "Удалённая работа", "Нейросети и ИИ"]},
            ],
            "center_icon": "globe",
            "extra": "Классификация Климова: 5 типов профессий",
        }
    },
    {
        "num": 3,
        "title": "Образовательные пути",
        "subtitle": "Профориентация — Урок 3",
        "content": {
            "left_boxes": [
                {"title": "Варианты после 11 кл.", "items": ["ВУЗ (бакалавриат)", "Колледж / СПО", "Курсы переподготовки", "Работа + онлайн-обучение"]},
                {"title": "Форматы обучения", "items": ["Очное", "Очно-заочное", "Заочное", "Дистанционное"]},
            ],
            "right_boxes": [
                {"title": "Финансирование", "items": ["Бюджетные места", "Целевое направление", "Оплата по договору", "Гранты и стипендии"]},
                {"title": "Ключевые советы", "items": ["Сравните программы ВУЗов", "Учтите проходные баллы", "Изучите отзывы студентов"]},
            ],
            "center_icon": "path",
        }
    },
    {
        "num": 4,
        "title": "Принятие решения",
        "subtitle": "Профориентация — Урок 4",
        "content": {
            "left_boxes": [
                {"title": "Методы принятия", "items": ["Матрица решений", "Квадрат Декарта", "SWOT-анализ", "Метод «5 почему»"]},
                {"title": "Квадрат Декарта", "items": ["Что будет, если сделаю?", "Что будет, если НЕ сделаю?", "Чего НЕ будет, если сделаю?", "Чего НЕ будет, если НЕ сделаю?"]},
            ],
            "right_boxes": [
                {"title": "Барьеры", "items": ["Страх ошибки", "Давление окружения", "Нехватка информации", "Перфекционизм"]},
                {"title": "Советы", "items": ["Дедлайн на решение", "Соберите максимум фактов", "Доверьтесь интуиции", "Ошибки — часть пути"]},
            ],
            "center_icon": "decision",
        }
    },
    {
        "num": 5,
        "title": "Резюме студента",
        "subtitle": "Профориентация — Урок 5",
        "content": {
            "left_boxes": [
                {"title": "Структура резюме", "items": ["Контактная информация", "Цель (Objective)", "Образование", "Опыт и проекты", "Навыки и компетенции"]},
            ],
            "right_boxes": [
                {"title": "Правила", "items": ["1 страница — максимум", "Конкретика, не вода", "Глаголы действия: создал, организовал", "Проверить орфографию!"]},
                {"title": "Без опыта?", "items": ["Школьные проекты", "Волонтёрство", "Олимпиады и курсы", "Хобби как навык"]},
            ],
            "center_icon": "document",
        }
    },
    {
        "num": 6,
        "title": "Мотивационное письмо",
        "subtitle": "Профориентация — Урок 6",
        "content": {
            "left_boxes": [
                {"title": "Структура письма", "items": ["Вступление —Hook", "Почему эта программа?", "Ваш опыт и достижения", "Ваш вклад в сообщество", "Заключение — Call to Action"]},
            ],
            "right_boxes": [
                {"title": "Ошибки", "items": ["Шаблонные фразы", "Повторение резюме", "Грамматические ошибки", "Слишком длинно"]},
                {"title": "Лайфхаки", "items": ["Исследуйте ВУЗ/компанию", "Покажите, а не рассказывайте", "Будьте искренними", "Попросите кого-то проверить"]},
            ],
            "center_icon": "letter",
        }
    },
    {
        "num": 7,
        "title": "Подготовка к собеседованию",
        "subtitle": "Профориентация — Урок 7",
        "content": {
            "left_boxes": [
                {"title": "До собеседования", "items": ["Изучите компанию/ВУЗ", "Подготовьте самопрезентацию", "Соберите портфолио", "Продумайте гардероб"]},
            ],
            "right_boxes": [
                {"title": "Типы вопросов", "items": ["Расскажите о себе", "Ваши сильные стороны?", "Почему мы должны выбрать вас?", "Кем вы видите себя через 5 лет?"]},
                {"title": "STAR-метод", "items": ["S — Ситуация", "T — Задача", "A — Действие", "R — Результат"]},
            ],
            "center_icon": "prep",
        }
    },
    {
        "num": 8,
        "title": "Тренировка собеседования",
        "subtitle": "Профориентация — Урок 8",
        "content": {
            "left_boxes": [
                {"title": "Практика", "items": ["Mock-интервью с другом", "Запись на видео", "Таймер: 2 мин на ответ", "Обратная связь"]},
            ],
            "right_boxes": [
                {"title": "Невербалика", "items": ["Зрительный контакт", "Открытая поза", "Уверенный голос", "Улыбка"]},
                {"title": "Трудные вопросы", "items": ["Ваши слабости?", "Конфликт с коллегой?", "Неудача и уроки?", "Почему уходите?"]},
            ],
            "center_icon": "training",
        }
    },
    {
        "num": 9,
        "title": "Карьерный план",
        "subtitle": "Профориентация — Урок 9",
        "content": {
            "left_boxes": [
                {"title": "Этапы плана", "items": ["1. Цель (1 год)", "2. Цель (3 года)", "3. Цель (5 лет)", "4. Цель (10 лет)"]},
                {"title": "Ресурсы", "items": ["Образование и курсы", "Менторство", "Стажировки", "Профессиональные сообщества"]},
            ],
            "right_boxes": [
                {"title": "SMART-цели", "items": ["S — Конкретная", "M — Измеримая", "A — Достижимая", "R — Значимая", "T — Ограниченная по времени"]},
                {"title": "Действия сейчас", "items": ["Составьте план на листе", "Отметьте сроки", "Найдите наставника", "Начните с малого шага"]},
            ],
            "center_icon": "roadmap",
        }
    },
    {
        "num": 10,
        "title": "Личный бренд",
        "subtitle": "Профориентация — Урок 10",
        "content": {
            "left_boxes": [
                {"title": "Что такое бренд?", "items": ["Ваша репутация онлайн", "То, как вас видят другие", "Уникальная ценность", "Согласованность образа"]},
            ],
            "right_boxes": [
                {"title": "Платформы", "items": ["LinkedIn / Профиль", "GitHub / Портфолио", "Telegram-канал", "Личный сайт / блог"]},
                {"title": "Советы", "items": ["Профессиональное фото", "Единый стиль", "Публикуйте регулярно", "Комментируйте экспертов"]},
            ],
            "center_icon": "brand",
        }
    },
    {
        "num": 11,
        "title": "Нетворкинг",
        "subtitle": "Профориентация — Урок 11",
        "content": {
            "left_boxes": [
                {"title": "Принципы", "items": ["Взаимная польза", "Качество > количество", "Регулярность контактов", "Искренний интерес"]},
            ],
            "right_boxes": [
                {"title": "Инструменты", "items": ["Профессиональные мероприятия", "Онлайн-сообщества", "Алумни-сети ВУЗов", "Менторские программы"]},
                {"title": "Правила", "items": ["Предлагайте помощь первым", "Следите за контактами", "Благодарите людей", "Будьте на связи"]},
            ],
            "center_icon": "network",
        }
    },
    {
        "num": 12,
        "title": "Итоговый проект",
        "subtitle": "Профориентация — Урок 12",
        "content": {
            "left_boxes": [
                {"title": "Ваш проект", "items": ["Карьерный портфолио", "План развития на 3 года", "Резюме + мотивационное письмо", "Презентация личного бренда"]},
            ],
            "right_boxes": [
                {"title": "Критерии оценки", "items": ["Полнота и конкретика", "Связь с реальным рынком", "Логика и обоснованность", "Оригинальность подхода"]},
                {"title": "Защита проекта", "items": ["3–5 минут на презентацию", "Ответы на вопросы", "Обоснование каждого шага", "Рефлексия и выводы"]},
            ],
            "center_icon": "project",
        }
    },
]


def escape_xml(text):
    """Escape text for XML attributes and content."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def draw_center_icon(icon_type, cx, cy):
    """Generate SVG elements for the center icon based on type."""
    elements = []
    if icon_type == "compass":
        # Compass rose
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="22" fill="none" stroke="{PRIMARY}" stroke-width="2"/>')
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="16" fill="none" stroke="{ACCENT}" stroke-width="1" opacity="0.5"/>')
        elements.append(f'<polygon points="{cx},{cy-20} {cx+5},{cy-5} {cx},{cy} {cx-5},{cy-5}" fill="{PRIMARY}" opacity="0.8"/>')
        elements.append(f'<polygon points="{cx},{cy+20} {cx+5},{cy+5} {cx},{cy} {cx-5},{cy+5}" fill="{ACCENT}" opacity="0.6"/>')
        elements.append(f'<line x1="{cx-20}" y1="{cy}" x2="{cx+20}" y2="{cy}" stroke="{PRIMARY}" stroke-width="1.5" opacity="0.5"/>')
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="{PRIMARY}"/>')
    elif icon_type == "globe":
        # Globe
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="22" fill="none" stroke="{PRIMARY}" stroke-width="2"/>')
        elements.append(f'<ellipse cx="{cx}" cy="{cy}" rx="10" ry="22" fill="none" stroke="{ACCENT}" stroke-width="1" opacity="0.6"/>')
        elements.append(f'<line x1="{cx-22}" y1="{cy}" x2="{cx+22}" y2="{cy}" stroke="{ACCENT}" stroke-width="1" opacity="0.6"/>')
        elements.append(f'<ellipse cx="{cx}" cy="{cy-8}" rx="18" ry="5" fill="none" stroke="{ACCENT}" stroke-width="0.8" opacity="0.4"/>')
        elements.append(f'<ellipse cx="{cx}" cy="{cy+8}" rx="18" ry="5" fill="none" stroke="{ACCENT}" stroke-width="0.8" opacity="0.4"/>')
    elif icon_type == "path":
        # Winding path with arrows
        elements.append(f'<path d="M{cx-25},{cy+15} Q{cx-10},{cy+15} {cx-10},{cy} Q{cx-10},{cy-15} {cx+5},{cy-15} Q{cx+20},{cy-15} {cx+20},{cy-5}" fill="none" stroke="{PRIMARY}" stroke-width="2.5" stroke-linecap="round"/>')
        elements.append(f'<polygon points="{cx+20},{cy-10} {cx+25},{cy-5} {cx+20},{cy}" fill="{PRIMARY}"/>')
        elements.append(f'<circle cx="{cx-25}" cy="{cy+15}" r="3" fill="{ACCENT}"/>')
        elements.append(f'<circle cx="{cx+22}" cy="{cy-5}" r="4" fill="{PRIMARY}" opacity="0.5"/>')
    elif icon_type == "decision":
        # Decision diamond / crossroads
        dx, dy = cx, cy
        elements.append(f'<polygon points="{dx},{dy-22} {dx+22},{dy} {dx},{dy+22} {dx-22},{dy}" fill="none" stroke="{PRIMARY}" stroke-width="2"/>')
        elements.append(f'<text x="{dx}" y="{dy+1}" font-family="Arial,sans-serif" font-size="10" fill="{PRIMARY}" text-anchor="middle" dominant-baseline="middle">?</text>')
        elements.append(f'<line x1="{dx-22}" y1="{dy}" x2="{dx-35}" y2="{dy-10}" stroke="{ACCENT}" stroke-width="1.5" marker-end="none"/>')
        elements.append(f'<line x1="{dx+22}" y1="{dy}" x2="{dx+35}" y2="{dy-10}" stroke="{ACCENT}" stroke-width="1.5"/>')
        elements.append(f'<line x1="{dx}" y1="{dy+22}" x2="{dx}" y2="{dy+35}" stroke="{ACCENT}" stroke-width="1.5"/>')
    elif icon_type == "document":
        # Resume document
        rx, ry = cx - 14, cy - 18
        elements.append(f'<rect x="{rx}" y="{ry}" width="28" height="36" rx="3" fill="{WHITE}" stroke="{PRIMARY}" stroke-width="2"/>')
        elements.append(f'<line x1="{rx+6}" y1="{ry+10}" x2="{rx+22}" y2="{ry+10}" stroke="{ACCENT}" stroke-width="2"/>')
        elements.append(f'<line x1="{rx+6}" y1="{ry+17}" x2="{rx+22}" y2="{ry+17}" stroke="{ACCENT}" stroke-width="1.5" opacity="0.5"/>')
        elements.append(f'<line x1="{rx+6}" y1="{ry+23}" x2="{rx+18}" y2="{ry+23}" stroke="{ACCENT}" stroke-width="1.5" opacity="0.5"/>')
        elements.append(f'<line x1="{rx+6}" y1="{ry+29}" x2="{rx+20}" y2="{ry+29}" stroke="{ACCENT}" stroke-width="1.5" opacity="0.5"/>')
    elif icon_type == "letter":
        # Envelope / letter
        ex, ey = cx - 20, cy - 14
        elements.append(f'<rect x="{ex}" y="{ey}" width="40" height="28" rx="3" fill="{WHITE}" stroke="{PRIMARY}" stroke-width="2"/>')
        elements.append(f'<polyline points="{ex},{ey} {cx},{ey+14} {ex+40},{ey}" fill="none" stroke="{PRIMARY}" stroke-width="1.5"/>')
        elements.append(f'<line x1="{ex+8}" y1="{ey+20}" x2="{ex+20}" y2="{ey+20}" stroke="{ACCENT}" stroke-width="1" opacity="0.5"/>')
        elements.append(f'<line x1="{ex+8}" y1="{ey+24}" x2="{ex+16}" y2="{ey+24}" stroke="{ACCENT}" stroke-width="1" opacity="0.5"/>')
    elif icon_type == "prep":
        # Checklist / clipboard
        px, py = cx - 14, cy - 18
        elements.append(f'<rect x="{px}" y="{py}" width="28" height="36" rx="3" fill="{WHITE}" stroke="{PRIMARY}" stroke-width="2"/>')
        elements.append(f'<rect x="{px+8}" y="{py-4}" width="12" height="8" rx="2" fill="{PRIMARY}" opacity="0.3"/>')
        elements.append(f'<line x1="{px+5}" y1="{py+12}" x2="{px+23}" y2="{py+12}" stroke="{ACCENT}" stroke-width="1.5"/>')
        elements.append(f'<line x1="{px+5}" y1="{py+19}" x2="{px+23}" y2="{py+19}" stroke="{ACCENT}" stroke-width="1.5" opacity="0.5"/>')
        elements.append(f'<line x1="{px+5}" y1="{py+26}" x2="{px+18}" y2="{py+26}" stroke="{ACCENT}" stroke-width="1.5" opacity="0.5"/>')
        # Checkmarks
        elements.append(f'<path d="M{px+3},{py+11} L{px+5},{py+13} L{px+9},{py+8}" fill="none" stroke="{PRIMARY}" stroke-width="1.2"/>')
    elif icon_type == "training":
        # Speech bubbles (mock interview)
        bx, by = cx, cy
        elements.append(f'<rect x="{bx-22}" y="{by-15}" width="24" height="18" rx="4" fill="{PRIMARY}" opacity="0.15" stroke="{PRIMARY}" stroke-width="1.5"/>')
        elements.append(f'<polygon points="{bx-14},{by+3} {bx-10},{by+3} {bx-14},{by+8}" fill="{PRIMARY}" opacity="0.15"/>')
        elements.append(f'<rect x="{bx-2}" y="{by-10}" width="24" height="18" rx="4" fill="{ACCENT}" opacity="0.15" stroke="{ACCENT}" stroke-width="1.5"/>')
        elements.append(f'<polygon points="{bx+10},{by+8} {bx+14},{by+8} {bx+14},{by+13}" fill="{ACCENT}" opacity="0.15"/>')
    elif icon_type == "roadmap":
        # Road / steps going up
        sx, sy = cx - 20, cy + 15
        steps = [(sx, sy), (sx+10, sy-8), (sx+20, sy-16), (sx+30, sy-24)]
        for i, (x, y) in enumerate(steps):
            w, h = 16, 8
            elements.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="{PRIMARY}" opacity="{0.3 + i*0.2}"/>')
        elements.append(f'<line x1="{steps[0][0]+8}" y1="{steps[0][1]}" x2="{steps[-1][0]+8}" y2="{steps[-1][1]}" stroke="{ACCENT}" stroke-width="1.5" stroke-dasharray="3,2"/>')
        # Flag at top
        fx, fy = steps[-1][0]+8, steps[-1][1]-10
        elements.append(f'<line x1="{fx}" y1="{fy+10}" x2="{fx}" y2="{fy-5}" stroke="{PRIMARY}" stroke-width="1.5"/>')
        elements.append(f'<polygon points="{fx},{fy-5} {fx+10},{fy-2} {fx},{fy+1}" fill="{ACCENT}"/>')
    elif icon_type == "brand":
        # Star / badge
        points = []
        import math
        for i in range(10):
            angle = math.pi / 2 + i * math.pi / 5
            r = 20 if i % 2 == 0 else 10
            x = cx + r * math.cos(angle)
            y = cy - r * math.sin(angle)
            points.append(f"{x:.1f},{y:.1f}")
        elements.append(f'<polygon points="{" ".join(points)}" fill="{PRIMARY}" opacity="0.2" stroke="{PRIMARY}" stroke-width="1.5"/>')
        elements.append(f'<text x="{cx}" y="{cy+4}" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">B</text>')
    elif icon_type == "network":
        # Network nodes
        positions = [(cx, cy-18), (cx-18, cy+5), (cx+18, cy+5), (cx-8, cy+18), (cx+8, cy+18), (cx, cy)]
        for x, y in positions:
            elements.append(f'<circle cx="{x}" cy="{y}" r="5" fill="{PRIMARY}" opacity="0.25" stroke="{PRIMARY}" stroke-width="1"/>')
        # Center node bigger
        elements.append(f'<circle cx="{cx}" cy="{cy}" r="7" fill="{ACCENT}" opacity="0.3" stroke="{PRIMARY}" stroke-width="1.5"/>')
        # Lines
        for x, y in positions[:-1]:
            elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="{ACCENT}" stroke-width="1" opacity="0.5"/>')
    elif icon_type == "project":
        # Trophy / achievement
        tx, ty = cx, cy
        # Cup
        elements.append(f'<path d="M{tx-12},{ty-15} L{tx-10},{ty+5} Q{tx},{ty+12} {tx+10},{ty+5} L{tx+12},{ty-15} Z" fill="{PRIMARY}" opacity="0.2" stroke="{PRIMARY}" stroke-width="1.5"/>')
        # Handles
        elements.append(f'<path d="M{tx-12},{ty-10} Q{tx-22},{ty-10} {tx-18},{ty}" fill="none" stroke="{ACCENT}" stroke-width="1.5"/>')
        elements.append(f'<path d="M{tx+12},{ty-10} Q{tx+22},{ty-10} {tx+18},{ty}" fill="none" stroke="{ACCENT}" stroke-width="1.5"/>')
        # Base
        elements.append(f'<rect x="{tx-8}" y="{ty+8}" width="16" height="4" rx="1" fill="{PRIMARY}" opacity="0.3"/>')
        elements.append(f'<rect x="{tx-12}" y="{ty+12}" width="24" height="4" rx="2" fill="{PRIMARY}" opacity="0.3"/>')
        # Star
        elements.append(f'<text x="{tx}" y="{ty}" font-family="Arial,sans-serif" font-size="10" fill="{PRIMARY}" text-anchor="middle">★</text>')
    return "\n    ".join(elements)


def build_content_box(x, y, w, h, box_data, is_left=True):
    """Build an SVG content box with title and bullet items."""
    lines = []
    # Box background
    lines.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.2" opacity="0.95"/>')
    # Title bar
    lines.append(f'<rect x="{x}" y="{y}" width="{w}" height="22" rx="6" fill="{PRIMARY}" opacity="0.12"/>')
    # Fix bottom corners of title bar
    lines.append(f'<rect x="{x}" y="{y+16}" width="{w}" height="6" fill="{PRIMARY}" opacity="0.12"/>')
    # Title text
    lines.append(f'<text x="{x+w//2}" y="{y+15}" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">{escape_xml(box_data["title"])}</text>')
    # Divider
    lines.append(f'<line x1="{x+8}" y1="{y+24}" x2="{x+w-8}" y2="{y+24}" stroke="{ACCENT2}" stroke-width="0.8"/>')
    # Items
    item_y = y + 37
    for item in box_data["items"]:
        # Bullet
        lines.append(f'<circle cx="{x+14}" cy="{item_y-3}" r="2.5" fill="{ACCENT}" opacity="0.7"/>')
        # Text
        lines.append(f'<text x="{x+22}" y="{item_y}" font-family="Arial,sans-serif" font-size="10" fill="{TEXT_LIGHT}">{escape_xml(item)}</text>')
        item_y += 15
    return "\n    ".join(lines)


def generate_svg(lesson):
    """Generate SVG for a single lesson."""
    num = lesson["num"]
    title = lesson["title"]
    subtitle = lesson["subtitle"]
    content = lesson["content"]
    left_boxes = content["left_boxes"]
    right_boxes = content["right_boxes"]
    icon_type = content.get("center_icon", "compass")
    extra = content.get("extra", "")

    # Calculate box dimensions
    # Layout: left column | center icon | right column
    left_x = 18
    center_x = 250
    right_x = 310
    col_w = 170
    content_y = 88

    # Count total boxes and distribute
    all_boxes = left_boxes + right_boxes
    num_left = len(left_boxes)
    num_right = len(right_boxes)

    # Calculate box heights
    left_box_h = []
    for b in left_boxes:
        left_box_h.append(28 + len(b["items"]) * 15 + 8)

    right_box_h = []
    for b in right_boxes:
        right_box_h.append(28 + len(b["items"]) * 15 + 8)

    total_left_h = sum(left_box_h) + (num_left - 1) * 8
    total_right_h = sum(right_box_h) + (num_right - 1) * 8
    max_content_h = max(total_left_h, total_right_h)

    # Center icon vertical position
    icon_cy = content_y + max_content_h // 2

    svg_parts = []
    svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">')

    # Defs
    svg_parts.append('  <defs>')
    svg_parts.append(f'    <linearGradient id="bg{num}" x1="0" y1="0" x2="0" y2="1">')
    svg_parts.append(f'      <stop offset="0%" stop-color="{BG_GRAD_TOP}"/>')
    svg_parts.append(f'      <stop offset="100%" stop-color="{BG_GRAD_BOT}"/>')
    svg_parts.append(f'    </linearGradient>')
    svg_parts.append(f'    <linearGradient id="hdr{num}" x1="0" y1="0" x2="1" y2="0">')
    svg_parts.append(f'      <stop offset="0%" stop-color="{PRIMARY}"/>')
    svg_parts.append(f'      <stop offset="100%" stop-color="{PRIMARY_DARK}"/>')
    svg_parts.append(f'    </linearGradient>')
    svg_parts.append('  </defs>')

    # Background
    svg_parts.append(f'  <rect width="500" height="350" fill="url(#bg{num})" rx="10"/>')

    # Border
    svg_parts.append(f'  <rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="{PRIMARY}" stroke-width="2.5"/>')

    # Inner border
    svg_parts.append(f'  <rect x="8" y="8" width="484" height="334" rx="6" fill="none" stroke="{PRIMARY}" stroke-width="1" opacity="0.3"/>')

    # Corner decorations
    svg_parts.append(f'  <polygon points="10,10 30,10 10,30" fill="{PRIMARY}" opacity="0.12"/>')
    svg_parts.append(f'  <polygon points="490,10 470,10 490,30" fill="{PRIMARY_DARK}" opacity="0.12"/>')
    svg_parts.append(f'  <polygon points="10,340 30,340 10,320" fill="{PRIMARY}" opacity="0.12"/>')
    svg_parts.append(f'  <polygon points="490,340 470,340 490,320" fill="{PRIMARY_DARK}" opacity="0.12"/>')

    # Header area background
    svg_parts.append(f'  <rect x="12" y="12" width="476" height="55" rx="6" fill="{PRIMARY}" opacity="0.06"/>')

    # Title
    svg_parts.append(f'  <text x="250" y="42" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">{escape_xml(title)}</text>')

    # Subtitle
    svg_parts.append(f'  <text x="250" y="60" font-family="Arial,sans-serif" font-size="12" fill="{TEXT_MED}" text-anchor="middle" opacity="0.7">{escape_xml(subtitle)}</text>')

    # Divider line
    svg_parts.append(f'  <line x1="30" y1="72" x2="470" y2="72" stroke="{PRIMARY}" stroke-width="2" opacity="0.2"/>')
    # Accent bars on divider
    svg_parts.append(f'  <rect x="30" y="70" width="60" height="4" fill="{PRIMARY}" opacity="0.15" rx="1"/>')
    svg_parts.append(f'  <rect x="410" y="70" width="60" height="4" fill="{PRIMARY_DARK}" opacity="0.1" rx="1"/>')

    # Lesson number badge
    badge_x, badge_y = 470, 30
    svg_parts.append(f'  <circle cx="{badge_x}" cy="{badge_y}" r="14" fill="{PRIMARY}" opacity="0.15"/>')
    svg_parts.append(f'  <circle cx="{badge_x}" cy="{badge_y}" r="10" fill="{PRIMARY}" opacity="0.2"/>')
    svg_parts.append(f'  <text x="{badge_x}" y="{badge_y+4}" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">{num}</text>')

    # Content area background
    content_area_h = max_content_h + 20
    if content_area_h > 215:
        content_area_h = min(content_area_h, 235)
    svg_parts.append(f'  <rect x="15" y="78" width="470" height="{content_area_h}" rx="6" fill="{PRIMARY_LIGHT}" opacity="0.4"/>')

    # Left column boxes
    curr_y = content_y
    for i, box in enumerate(left_boxes):
        bh = left_box_h[i]
        svg_parts.append(build_content_box(left_x, curr_y, col_w, bh, box, is_left=True))
        curr_y += bh + 8

    # Right column boxes
    curr_y = content_y
    for i, box in enumerate(right_boxes):
        bh = right_box_h[i]
        svg_parts.append(build_content_box(right_x, curr_y, col_w, bh, box, is_left=False))
        curr_y += bh + 8

    # Center icon
    svg_parts.append(draw_center_icon(icon_type, center_x, icon_cy))

    # Center connecting lines (decorative)
    svg_parts.append(f'  <line x1="{left_x + col_w + 5}" y1="{icon_cy}" x2="{center_x - 28}" y2="{icon_cy}" stroke="{ACCENT2}" stroke-width="1" stroke-dasharray="3,3" opacity="0.5"/>')
    svg_parts.append(f'  <line x1="{center_x + 28}" y1="{icon_cy}" x2="{right_x - 5}" y2="{icon_cy}" stroke="{ACCENT2}" stroke-width="1" stroke-dasharray="3,3" opacity="0.5"/>')

    # Extra text if present
    if extra:
        extra_y = content_y + max_content_h + 12
        svg_parts.append(f'  <rect x="30" y="{extra_y}" width="440" height="18" rx="3" fill="{PRIMARY}" opacity="0.08"/>')
        svg_parts.append(f'  <text x="250" y="{extra_y + 13}" font-family="Arial,sans-serif" font-size="10" fill="{TEXT_MED}" text-anchor="middle" font-style="italic">{escape_xml(extra)}</text>')

    # Footer area
    footer_y = 328
    svg_parts.append(f'  <line x1="30" y1="{footer_y - 8}" x2="470" y2="{footer_y - 8}" stroke="{PRIMARY}" stroke-width="1" opacity="0.15"/>')
    svg_parts.append(f'  <text x="250" y="{footer_y}" font-family="Arial,sans-serif" font-size="10" fill="{PRIMARY}" text-anchor="middle" opacity="0.5">Профориентация · 10 класс</text>')

    # Small decorative dots in footer
    svg_parts.append(f'  <circle cx="160" cy="{footer_y - 3}" r="2" fill="{ACCENT}" opacity="0.3"/>')
    svg_parts.append(f'  <circle cx="340" cy="{footer_y - 3}" r="2" fill="{ACCENT}" opacity="0.3"/>')

    svg_parts.append('</svg>')
    return "\n".join(svg_parts)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    generated = 0
    validated = 0
    errors = []

    for lesson in LESSONS:
        num = lesson["num"]
        filename = f"lesson{num}.svg"
        filepath = os.path.join(OUTPUT_DIR, filename)

        # Generate SVG content
        svg_content = generate_svg(lesson)

        # Write file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)
        generated += 1
        print(f"  Generated: {filename}")

        # Validate as XML
        try:
            ET.fromstring(svg_content)
            validated += 1
            print(f"  Validated: {filename} ✓")
        except ET.ParseError as e:
            errors.append(f"{filename}: {e}")
            print(f"  VALIDATION ERROR in {filename}: {e}")

    print(f"\n{'='*50}")
    print(f"Generation complete: {generated}/12 SVGs generated")
    print(f"Validation complete: {validated}/12 SVGs passed XML validation")
    if errors:
        print(f"\nErrors found:")
        for err in errors:
            print(f"  - {err}")
    else:
        print(f"\nAll SVGs are valid XML! ✓")

    # Additional file size check
    print(f"\nFile sizes:")
    total_size = 0
    for lesson in LESSONS:
        num = lesson["num"]
        filepath = os.path.join(OUTPUT_DIR, f"lesson{num}.svg")
        size = os.path.getsize(filepath)
        total_size += size
        print(f"  lesson{num}.svg: {size:,} bytes")
    print(f"  Total: {total_size:,} bytes")


if __name__ == "__main__":
    main()
