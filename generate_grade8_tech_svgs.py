#!/usr/bin/env python3
"""Generate Grade 8 Technology (Технология) SVG images for all 13 lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/tech"

# Color scheme
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
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


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
        lines.append(f'  <text x="{x+12}" y="{ty}" font-size="12" fill="{TEXT_DARK}">• {escape(item)}</text>')
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
# LESSON 1: Основы проектной деятельности
# ============================================================
def lesson_1():
    svg = svg_header()
    svg += header_bar(1, "Основы проектной деятельности", "Фундамент проектной работы")
    
    # Project stages flow - horizontal arrows
    stages = ["Замысел", "Исследование", "Проектирование", "Изготовление", "Оценка"]
    colors = [PRIMARY_DARK, PRIMARY, ACCENT, PRIMARY_LIGHT, GREEN]
    sx = 40
    for i, (stage, color) in enumerate(zip(stages, colors)):
        svg += stage_arrow(sx + i*148, 95, 140, 40, stage, color)
    
    svg += f"""
  <!-- Left: Project lifecycle detail -->
  {info_box(25, 155, 350, 230, "Этапы проектной деятельности", [
      "1. Определение проблемы и цели",
      "2. Сбор и анализ информации",
      "3. Разработка вариантов решения",
      "4. Выбор оптимального решения",
      "5. Планирование работы",
      "6. Выполнение проекта",
      "7. Тестирование и оценка",
      "8. Защита и презентация",
      "9. Рефлексия и выводы"
  ])}
  
  <!-- Right: Key principles -->
  {info_box(395, 155, 380, 120, "Принципы проектирования", [
      "Системность — целостный подход к проекту",
      "Ресурсоёмкость — учёт материалов и времени",
      "Безопасность — соблюдение правил ТБ",
      "Экологичность — минимальный вред природе"
  ])}
  
  <!-- Right bottom: Project types -->
  {info_box(395, 290, 380, 95, "Типы проектов", [
      "Информационный — сбор и анализ данных",
      "Практико-ориентированный — создание изделия",
      "Исследовательский — изучение явлений",
      "Творческий — оригинальное решение"
  ])}
  
  <!-- Bottom highlight -->
  {highlight_box(25, 400, 750, 55, [
      "⚡ Важно: Проект начинается с проблемы, а заканчивается результатом!",
      "Каждый этап имеет критерии оценки и конкретные продукты деятельности"
  ])}
  
  <!-- Decorative gear icons -->
  <circle cx="60" cy="490" r="30" fill="none" stroke="{ACCENT}" stroke-width="2" opacity="0.3"/>
  <circle cx="60" cy="490" r="15" fill="none" stroke="{ACCENT}" stroke-width="1.5" opacity="0.3"/>
  <line x1="60" y1="458" x2="60" y2="465" stroke="{ACCENT}" stroke-width="2" opacity="0.3"/>
  <line x1="60" y1="515" x2="60" y2="522" stroke="{ACCENT}" stroke-width="2" opacity="0.3"/>
  <line x1="28" y1="490" x2="35" y2="490" stroke="{ACCENT}" stroke-width="2" opacity="0.3"/>
  <line x1="85" y1="490" x2="92" y2="490" stroke="{ACCENT}" stroke-width="2" opacity="0.3"/>
  
  <!-- Bottom info -->
  {info_box(110, 470, 665, 110, "Документы проекта", [
      "Паспорт проекта: тема, цель, задачи, сроки, ресурсы",
      "Техническое задание: требования к изделию",
      "Технологическая карта: последовательность операций",
      "Эскиз и чертёж: графическое представление изделия",
      "Самооценка: анализ результатов и выводы"
  ])}
  """
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 2: Графическая документация
# ============================================================
def lesson_2():
    svg = svg_header()
    svg += header_bar(2, "Графическая документация", "Чертежи, эскизы, спецификации")
    
    # Drawing frame (main title block)
    svg += f"""
  <!-- Drawing frame illustration -->
  <rect x="30" y="90" width="320" height="280" fill="{WHITE}" stroke="{PRIMARY}" stroke-width="2" filter="url(#shadow)"/>
  <rect x="35" y="95" width="310" height="270" fill="none" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <rect x="235" y="305" width="110" height="55" fill="{BG_WARM}" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <text x="290" y="325" font-size="9" fill="{TEXT_DARK}" text-anchor="middle">Чертёж детали</text>
  <text x="290" y="340" font-size="8" fill="{GRAY}" text-anchor="middle">Масштаб 1:1</text>
  <text x="290" y="352" font-size="8" fill="{GRAY}" text-anchor="middle">Материал: дерево</text>
  
  <!-- Simple technical drawing inside frame -->
  <!-- Top view (rectangle with hole) -->
  <rect x="80" y="115" width="120" height="80" fill="none" stroke="{TEXT_DARK}" stroke-width="1.5"/>
  <circle cx="140" cy="155" r="15" fill="none" stroke="{TEXT_DARK}" stroke-width="1"/>
  <text x="140" y="125" font-size="9" fill="{BLUE}" text-anchor="middle">Вид сверху</text>
  
  <!-- Front view -->
  <rect x="80" y="215" width="120" height="60" fill="none" stroke="{TEXT_DARK}" stroke-width="1.5"/>
  <line x1="80" y1="215" x2="80" y2="275" stroke="{TEXT_DARK}" stroke-width="1.5"/>
  <text x="140" y="235" font-size="9" fill="{BLUE}" text-anchor="middle">Вид спереди</text>
  
  <!-- Dimension lines -->
  <line x1="80" y1="290" x2="200" y2="290" stroke="{RED}" stroke-width="0.7"/>
  <line x1="80" y1="286" x2="80" y2="294" stroke="{RED}" stroke-width="0.7"/>
  <line x1="200" y1="286" x2="200" y2="294" stroke="{RED}" stroke-width="0.7"/>
  <text x="140" y="302" font-size="8" fill="{RED}" text-anchor="middle">120</text>
  
  <!-- Right side: Types of documentation -->
  {info_box(375, 90, 400, 140, "Виды графической документации", [
      "Эскиз — от руки, с соблюдением пропорций",
      "Чертёж — по правилам ЕСКД, точные размеры",
      "Технический рисунок — наглядное изображение",
      "Схема — условное изображение структуры",
      "Спецификация — перечень деталей и материалов"
  ])}
  
  {info_box(375, 245, 400, 125, "Правила оформления чертежа", [
      "Формат листа: А4 (210×297), А3 (297×420)",
      "Масштаб: 1:1, 1:2 (уменьшение), 2:1 (увеличение)",
      "Линии: основная s=0.5-1.4мм, штриховая, тонкая",
      "Шрифт: чертёжный по ГОСТ 2.304-81",
      "Основная надпись: ГОСТ 2.104-2006"
  ])}
  
  <!-- Line types legend -->
  {info_box(30, 390, 745, 90, "Типы линий на чертеже", [
      "━━━━━━━━ Сплошная основная — видимый контур",
      "┈┈┈┈┈┈┈┈┈ Сплошная тонкая — размерные и выносные линии",
      "- - - - - - Штриховая — невидимый контур",
      "─·─·─·─·─ Штрихпунктирная — осевые и центровые линии"
  ])}
  
  {highlight_box(30, 495, 745, 45, [
      "📐 Стандарты ЕСКД — Единая система конструкторской документации",
      "Все чертежи выполняются по ГОСТ для взаимопонимания специалистов"
  ])}
  
  <!-- Decorative compass -->
  <line x1="720" y1="505" x2="740" y2="530" stroke="{ACCENT}" stroke-width="1.5" opacity="0.4"/>
  <line x1="720" y1="505" x2="700" y2="530" stroke="{ACCENT}" stroke-width="1.5" opacity="0.4"/>
  <circle cx="720" cy="502" r="4" fill="{ACCENT}" opacity="0.4"/>
  """
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 3: Свойства и породы древесины
# ============================================================
def lesson_3():
    svg = svg_header()
    svg += header_bar(3, "Свойства и породы древесины", "Хвойные и лиственные породы")
    
    # Wood cross-section diagram
    svg += f"""
  <!-- Tree cross-section -->
  <circle cx="160" cy="240" r="100" fill="#DEB887" stroke="{PRIMARY_DARK}" stroke-width="2" filter="url(#shadow)"/>
  <circle cx="160" cy="240" r="70" fill="#D2B48C" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <circle cx="160" cy="240" r="40" fill="#C4A882" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <circle cx="160" cy="240" r="15" fill="#8B7355" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  
  <!-- Labels for cross-section -->
  <line x1="160" y1="140" x2="160" y2="118" stroke="{TEXT_DARK}" stroke-width="1"/>
  <text x="160" y="112" font-size="10" fill="{TEXT_DARK}" text-anchor="middle">Кора</text>
  <line x1="230" y1="170" x2="260" y2="150" stroke="{TEXT_DARK}" stroke-width="1"/>
  <text x="275" y="152" font-size="10" fill="{TEXT_DARK}">Луб</text>
  <line x1="210" y1="240" x2="250" y2="240" stroke="{TEXT_DARK}" stroke-width="1"/>
  <text x="280" y="244" font-size="10" fill="{TEXT_DARK}">Заболонь</text>
  <line x1="200" y1="280" x2="245" y2="300" stroke="{TEXT_DARK}" stroke-width="1"/>
  <text x="275" y="305" font-size="10" fill="{TEXT_DARK}">Ядро</text>
  <text x="160" y="245" font-size="9" fill="{WHITE}" text-anchor="middle">Сердцевина</text>
  
  <!-- Growth rings illustration -->
  <ellipse cx="160" cy="210" rx="90" ry="8" fill="none" stroke="#A0845C" stroke-width="0.5" opacity="0.5"/>
  <ellipse cx="160" cy="260" rx="85" ry="7" fill="none" stroke="#A0845C" stroke-width="0.5" opacity="0.5"/>
  
  <!-- Softwood info -->
  {info_box(380, 90, 395, 145, "Хвойные породы (мягкие)", [
      "Сосна — смолистая, прочная, строительная",
      "Ель — менее смолистая, резонансная",
      "Лиственница — плотная, влагостойкая",
      "Кедр — мягкая, ароматная, для мебели",
      "Пихта — мягкая, однородная"
  ], PRIMARY)}
  
  <!-- Hardwood info -->
  {info_box(380, 248, 395, 145, "Лиственные породы (твёрдые)", [
      "Дуб — прочный, долговечный, красивый",
      "Берёза — однородная, лёгкая в обработке",
      "Бук — твёрдый, хорошо гнётся",
      "Ясень — упругий, для спортивного инвентаря",
      "Липа — мягкая, для резьбы"
  ], PRIMARY_LIGHT)}
  
  <!-- Properties -->
  {info_box(25, 370, 370, 120, "Физические свойства древесины", [
      "Плотность: лёгкая (&lt;540) / средняя / тяжёлая (&gt;740)",
      "Влажность: свободная и связанная вода",
      "Усушка: уменьшение размеров при высыхании",
      "Разбухание: увеличение при увлажнении",
      "Теплопроводность: низкая (хороший изолятор)"
  ])}
  
  {info_box(410, 408, 370, 82, "Механические свойства", [
      "Прочность: сопротивление разрушению",
      "Твёрдость: сопротивление вдавливанию",
      "Упругость: восстановление формы",
      "Пластичность: изменение без разрушения"
  ])}
  
  {highlight_box(25, 505, 750, 40, [
      "🌲 Древесина — возобновляемый природный материал. Выбор породы зависит от назначения изделия!"
  ])}
  """
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 4: Ручные инструменты для обработки древесины
# ============================================================
def lesson_4():
    svg = svg_header()
    svg += header_bar(4, "Ручные инструменты для обработки древесины", "Пилы, рубанки, стамески")
    
    svg += f"""
  <!-- Saw illustration -->
  <rect x="40" y="105" width="200" height="8" rx="2" fill="{GRAY}" stroke="#4B5563" stroke-width="1"/>
  <rect x="240" y="92" width="70" height="34" rx="4" fill="#8B7355" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <!-- Saw teeth -->
  <polygon points="40,113 45,120 50,113 55,120 60,113 65,120 70,113 75,120 80,113 85,120 90,113 95,120 100,113 105,120 110,113 115,120 120,113 125,120 130,113 135,120 140,113 145,120 150,113 155,120 160,113 165,120 170,113 175,120 180,113 185,120 190,113 195,120 200,113 205,120 210,113 215,120 220,113 225,120 230,113 235,120 240,113" fill="{GRAY}" stroke="#4B5563" stroke-width="0.5"/>
  <text x="140" y="140" font-size="11" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Ножовка</text>
  
  <!-- Plane illustration -->
  <rect x="40" y="168" width="140" height="20" rx="3" fill="#8B7355" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <rect x="80" y="155" width="50" height="13" rx="2" fill="#A0845C" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <rect x="95" y="148" width="20" height="7" rx="1" fill="{GRAY}" stroke="#4B5563" stroke-width="1"/>
  <rect x="40" y="188" width="140" height="5" fill="#8B7355" stroke="{PRIMARY_DARK}" stroke-width="0.5"/>
  <rect x="90" y="193" width="40" height="3" fill="{GRAY}"/>
  <text x="110" y="213" font-size="11" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Рубанок</text>
  
  <!-- Chisel illustration -->
  <rect x="70" y="233" width="8" height="50" fill="{GRAY}" stroke="#4B5563" stroke-width="1"/>
  <rect x="60" y="283" width="28" height="8" rx="1" fill="#8B7355" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <polygon points="60,233 78,233 69,200" fill="{GRAY}" stroke="#4B5563" stroke-width="1"/>
  <text x="70" y="308" font-size="11" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Стамеска</text>
  
  <!-- Tools categories -->
  {info_box(375, 95, 400, 110, "Инструменты для пиления", [
      "Ножовка — продольное и поперечное пиление",
      "Лучковая пила — криволинейный распил",
      "Ножовка с обушком — точный тонкий распил",
      "Лобзик — фигурный выпиливание"
  ])}
  
  {info_box(375, 218, 400, 110, "Инструменты для строгания", [
      "Рубанок — черновое и чистовое строгание",
      "Шерхебель — грубое снятие материала",
      "Фуганок — выравнивание длинных деталей",
      "Цикля — окончательная зачистка"
  ])}
  
  {info_box(375, 341, 400, 110, "Инструменты для сверления и долбления", [
      "Коловорот — ручное сверление",
      "Ручная дрель — быстрое сверление",
      "Сверло перьевое — отверстия в дереве",
      "Стамеска — выборка пазов и гнёзд"
  ])}
  
  {info_box(25, 325, 335, 95, "Вспомогательные инструменты", [
      "Киянка — деревянный молоток",
      "Угольник — проверка прямых углов",
      "Рейсмус — разметка толщины",
      "Линейка и рулетка — измерение"
  ])}
  
  {highlight_box(25, 468, 750, 60, [
      "⚠ Правила безопасности: надёжно закрепляй заготовку,",
      "не держи руку на линии реза, работай острым инструментом!",
      "Тупой инструмент опаснее острого — требует большего усилия"
  ])}
  
  <!-- Measurement marks -->
  <rect x="30" y="545" width="740" height="25" rx="4" fill="{WHITE}" stroke="{BORDER}" stroke-width="1" opacity="0.6"/>
  <text x="400" y="562" font-size="11" fill="{TEXT_MED}" text-anchor="middle">📏 Измеряй дважды, режь один раз!</text>
  """
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 5: Виды соединений древесины
# ============================================================
def lesson_5():
    svg = svg_header()
    svg += header_bar(5, "Виды соединений древесины", "Гвоздь, шуруп, клей, шип, паз")
    
    svg += f"""
  <!-- Nail joint -->
  <rect x="40" y="105" width="130" height="25" rx="2" fill="#DEB887" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>
  <rect x="40" y="130" width="130" height="25" rx="2" fill="#D2B48C" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>
  <line x1="85" y1="105" x2="85" y2="155" stroke="{GRAY}" stroke-width="2.5"/>
  <circle cx="85" cy="105" r="3" fill="{GRAY}"/>
  <text x="105" y="170" font-size="11" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Гвоздевое</text>
  
  <!-- Screw joint -->
  <rect x="195" y="105" width="130" height="25" rx="2" fill="#DEB887" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>
  <rect x="195" y="130" width="130" height="25" rx="2" fill="#D2B48C" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>
  <line x1="260" y1="108" x2="260" y2="152" stroke="#4B5563" stroke-width="2"/>
  <line x1="256" y1="118" x2="264" y2="114" stroke="#4B5563" stroke-width="1"/>
  <line x1="256" y1="128" x2="264" y2="124" stroke="#4B5563" stroke-width="1"/>
  <line x1="256" y1="138" x2="264" y2="134" stroke="#4B5563" stroke-width="1"/>
  <line x1="255" y1="148" x2="265" y2="144" stroke="#4B5563" stroke-width="1"/>
  <circle cx="260" cy="105" r="5" fill="none" stroke="#4B5563" stroke-width="1.5"/>
  <line x1="260" y1="100" x2="260" y2="110" stroke="#4B5563" stroke-width="1.5"/>
  <text x="260" y="170" font-size="11" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Шурупное</text>
  
  <!-- Glue joint -->
  <rect x="350" y="105" width="130" height="25" rx="2" fill="#DEB887" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>
  <rect x="350" y="130" width="130" height="25" rx="2" fill="#D2B48C" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>
  <rect x="355" y="127" width="120" height="6" rx="1" fill="{ACCENT}" opacity="0.7"/>
  <text x="415" y="170" font-size="11" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Клеевое</text>
  
  <!-- Dovetail joint -->
  <rect x="505" y="105" width="130" height="50" rx="2" fill="#DEB887" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>
  <polygon points="530,105 540,130 530,155 550,155 560,130 550,105" fill="#D2B48C" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>
  <polygon points="570,105 580,130 570,155 590,155 600,130 590,105" fill="#D2B48C" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>
  <polygon points="610,105 620,130 610,155 625,155 625,105" fill="#D2B48C" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>
  <text x="570" y="170" font-size="11" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Ласточкин хвост</text>
  
  <!-- Mortise and tenon -->
  <rect x="660" y="115" width="30" height="30" fill="none" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>
  <rect x="660" y="105" width="120" height="50" rx="2" fill="none" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>
  <rect x="690" y="125" width="60" height="10" fill="#D2B48C" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>
  <text x="720" y="170" font-size="11" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Шип-паз</text>
  
  <!-- Detailed info boxes -->
  {info_box(25, 190, 250, 145, "Неразъёмные соединения", [
      "Гвоздевое — быстрое, но слабое",
      "Шурупное — прочнее гвоздевого",
      "Клеевое — прочное, невидимое",
      "Ласточкин хвост — без клея и гвоздей",
      "Шиповое — самое прочное из ручных"
  ])}
  
  {info_box(290, 190, 250, 145, "Разъёмные соединения", [
      "Болтовое — с гайкой и шайбой",
      "Винтовое — для регулировки",
      "Шурупное в гладкое — можно выкрутить",
      "Клиновое — для разборной мебели",
      "Штифтовое — со вставным шипом"
  ])}
  
  {info_box(555, 190, 225, 145, "Выбор соединения", [
      "Нагрузка: прочность?",
      "Внешний вид: видно/скрыто?",
      "Разборность: нужно ли?",
      "Инструменты: что есть?",
      "Материал: толщина деталей?"
  ])}
  
  {highlight_box(25, 355, 750, 50, [
      "🔑 Главное правило: вид соединения зависит от назначения изделия, нагрузки и условий эксплуатации",
      "Мебельные шипы + клей = самое прочное и красивое соединение"
  ])}
  
  <!-- Wood joint types comparison table -->
  {info_box(25, 420, 750, 150, "Сравнение видов соединений", [
      "Гвоздь        — прочность: ★★☆☆☆   скорость: ★★★★★   разборность: нет     внешний вид: ★★☆☆☆",
      "Шуруп         — прочность: ★★★☆☆   скорость: ★★★★☆   разборность: да      внешний вид: ★★★☆☆",
      "Клей            — прочность: ★★★★☆   скорость: ★★★☆☆   разборность: нет     внешний вид: ★★★★★",
      "Шип-паз      — прочность: ★★★★★   скорость: ★★☆☆☆   разборность: нет     внешний вид: ★★★★★",
      "Ласточкин хв. — прочность: ★★★★★   скорость: ★☆☆☆☆   разборность: нет     внешний вид: ★★★★★",
      "Болт            — прочность: ★★★★☆   скорость: ★★★☆☆   разборность: да      внешний вид: ★★☆☆☆"
  ])}
  """
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 6: Свойства металлов и сплавов
# ============================================================
def lesson_6():
    svg = svg_header()
    svg += header_bar(6, "Свойства металлов и сплавов", "Чёрные и цветные металлы, сталь")
    
    svg += f"""
  <!-- Classification diagram - tree structure -->
  <rect x="280" y="90" width="240" height="35" rx="6" fill="{PRIMARY_DARK}" filter="url(#shadow)"/>
  <text x="400" y="113" font-size="14" fill="{WHITE}" text-anchor="middle" font-weight="bold">Металлы и сплавы</text>
  
  <!-- Branches -->
  <line x1="330" y1="125" x2="200" y2="155" stroke="{PRIMARY}" stroke-width="2"/>
  <line x1="470" y1="125" x2="600" y2="155" stroke="{PRIMARY}" stroke-width="2"/>
  
  <!-- Ferrous -->
  <rect x="80" y="155" width="240" height="30" rx="5" fill="{GRAY}" filter="url(#shadow)"/>
  <text x="200" y="175" font-size="13" fill="{WHITE}" text-anchor="middle" font-weight="bold">Чёрные металлы</text>
  
  <line x1="140" y1="185" x2="100" y2="200" stroke="{GRAY}" stroke-width="1.5"/>
  <line x1="200" y1="185" x2="200" y2="200" stroke="{GRAY}" stroke-width="1.5"/>
  <line x1="260" y1="185" x2="300" y2="200" stroke="{GRAY}" stroke-width="1.5"/>
  
  <rect x="30" y="200" width="130" height="25" rx="4" fill="#6B7280"/>
  <text x="95" y="217" font-size="10" fill="{WHITE}" text-anchor="middle">Чугун</text>
  <rect x="170" y="200" width="130" height="25" rx="4" fill="#4B5563"/>
  <text x="235" y="217" font-size="10" fill="{WHITE}" text-anchor="middle">Сталь</text>
  <rect x="270" y="200" width="80" height="25" rx="4" fill="#9CA3AF"/>
  <text x="310" y="217" font-size="10" fill="{WHITE}" text-anchor="middle">Феррит</text>
  
  <!-- Non-ferrous -->
  <rect x="480" y="155" width="240" height="30" rx="5" fill="{ACCENT}" filter="url(#shadow)"/>
  <text x="600" y="175" font-size="13" fill="{WHITE}" text-anchor="middle" font-weight="bold">Цветные металлы</text>
  
  <line x1="530" y1="185" x2="490" y2="200" stroke="{ACCENT}" stroke-width="1.5"/>
  <line x1="600" y1="185" x2="600" y2="200" stroke="{ACCENT}" stroke-width="1.5"/>
  <line x1="670" y1="185" x2="710" y2="200" stroke="{ACCENT}" stroke-width="1.5"/>
  
  <rect x="420" y="200" width="110" height="25" rx="4" fill="#D97706"/>
  <text x="475" y="217" font-size="10" fill="{WHITE}" text-anchor="middle">Медь</text>
  <rect x="540" y="200" width="110" height="25" rx="4" fill="#B45309"/>
  <text x="595" y="217" font-size="10" fill="{WHITE}" text-anchor="middle">Алюминий</text>
  <rect x="660" y="200" width="110" height="25" rx="4" fill="#92400E"/>
  <text x="715" y="217" font-size="10" fill="{WHITE}" text-anchor="middle">Цинк, Олово</text>
  
  <!-- Properties comparison -->
  {info_box(25, 245, 245, 165, "Физические свойства", [
      "Плотность: Al(2.7) Fe(7.8) Cu(8.9)",
      "Температура плавления:",
      "  Al — 660°C, Cu — 1083°C",
      "  Fe — 1538°C, Sn — 232°C",
      "Электропроводность: Cu &gt; Al &gt; Fe",
      "Теплопроводность: Cu &gt; Al &gt; Fe",
      "Цвет: Cu — красный, Au — жёлтый"
  ])}
  
  {info_box(285, 245, 245, 165, "Механические свойства", [
      "Прочность — сопротивление разрушению",
      "Пластичность — изменение формы",
      "Твёрдость — сопротивление вдавл.",
      "Упругость — возврат формы",
      "Хрупкость — разрушение без деф.",
      "Вязкость — работа на разрушение",
      "Усталость — разрушение при циклах"
  ])}
  
  {info_box(545, 245, 235, 165, "Сплавы и их применение", [
      "Сталь — конструкции, инструменты",
      "Чугун — детали машин, трубы",
      "Бронза — подшипники, скульптуры",
      "Латунь — фурнитура, приборы",
      "Дюралюминий — авиация, мебель",
      "Припой — соединение деталей",
      "Нержавейка — посуда, медицина"
  ])}
  
  {highlight_box(25, 425, 750, 50, [
      "⚖ Сталь = железо + углерод (до 2%). Чем больше углерода — тем твёрже, но хрупче!",
      "Легирующие добавки (Cr, Ni, W) придают стали специальные свойства"
  ])}
  
  <!-- Steel types -->
  {info_box(25, 490, 370, 90, "Виды стали", [
      "Углеродистая: низко-, средне-, высокоуглеродистая",
      "Легированная: хромистая, никелевая, вольфрамовая",
      "Инструментальная: для резцов, свёрл, напильников",
      "Конструкционная: для деталей машин и сооружений"
  ])}
  
  {info_box(410, 490, 365, 90, "Обработка металлов", [
      "Механическая: резание, гибка, штамповка",
      "Термическая: закалка, отпуск, отжиг",
      "Термохимическая: цементация, азотирование",
      "Литейная: отливка в формы"
  ])}
  """
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 7: Ручная обработка металла
# ============================================================
def lesson_7():
    svg = svg_header()
    svg += header_bar(7, "Ручная обработка металла", "Резание, опиливание, гибка, сверление")
    
    svg += f"""
  <!-- Cutting illustration -->
  <rect x="40" y="105" width="160" height="12" fill="#9CA3AF" stroke="#6B7280" stroke-width="1"/>
  <polygon points="55,105 60,95 65,105" fill="#4B5563" stroke="#374151" stroke-width="1"/>
  <polygon points="85,105 90,95 95,105" fill="#4B5563" stroke="#374151" stroke-width="1"/>
  <polygon points="115,105 120,95 125,105" fill="#4B5563" stroke="#374151" stroke-width="1"/>
  <polygon points="145,105 150,95 155,105" fill="#4B5563" stroke="#374151" stroke-width="1"/>
  <polygon points="175,105 180,95 185,105" fill="#4B5563" stroke="#374151" stroke-width="1"/>
  <line x1="40" y1="122" x2="200" y2="122" stroke="{RED}" stroke-width="1" stroke-dasharray="4,2"/>
  <text x="120" y="138" font-size="11" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Резание ножовкой</text>
  
  <!-- Filing illustration -->
  <rect x="250" y="105" width="160" height="12" fill="#9CA3AF" stroke="#6B7280" stroke-width="1"/>
  <rect x="280" y="88" width="100" height="17" rx="2" fill="#6B7280" stroke="#4B5563" stroke-width="1"/>
  <rect x="370" y="85" width="40" height="23" rx="3" fill="#8B7355" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <!-- File teeth marks -->
  <line x1="283" y1="103" x2="285" y2="100" stroke="#374151" stroke-width="0.5"/>
  <line x1="288" y1="103" x2="290" y2="100" stroke="#374151" stroke-width="0.5"/>
  <line x1="293" y1="103" x2="295" y2="100" stroke="#374151" stroke-width="0.5"/>
  <line x1="298" y1="103" x2="300" y2="100" stroke="#374151" stroke-width="0.5"/>
  <line x1="303" y1="103" x2="305" y2="100" stroke="#374151" stroke-width="0.5"/>
  <text x="330" y="138" font-size="11" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Опиливание</text>
  
  <!-- Bending illustration -->
  <polyline points="40,170 90,170 105,200 160,200" fill="none" stroke="#9CA3AF" stroke-width="5" stroke-linecap="round"/>
  <polyline points="40,170 90,170 105,200 160,200" fill="none" stroke="#6B7280" stroke-width="3" stroke-linecap="round"/>
  <text x="100" y="225" font-size="11" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Гибка</text>
  
  <!-- Drilling illustration -->
  <polygon points="300,160 305,195 295,195" fill="#6B7280" stroke="#4B5563" stroke-width="1"/>
  <rect x="295" y="195" width="10" height="15" fill="#9CA3AF" stroke="#6B7280" stroke-width="1"/>
  <rect x="280" y="210" width="40" height="10" fill="#9CA3AF" stroke="#6B7280" stroke-width="1"/>
  <circle cx="300" cy="215" r="4" fill="#4B5563"/>
  <text x="300" y="240" font-size="11" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Сверление</text>
  
  <!-- Operations detail -->
  {info_box(430, 95, 345, 165, "Операции обработки металла", [
      "Резание — ножовкой по металлу",
      "Опиливание — напильниками разных типов",
      "Гибка — в тисках или на оправке",
      "Сверление — ручной или электрической дрелью",
      "Нарезание резьбы — метчиками и плашками",
      "Рубка — зубилом и киянкой"
  ])}
  
  {info_box(25, 258, 370, 140, "Напильники: типы насечки", [
      "Драчёвый — грубое снятие (0.5-1.0 мм)",
      "Личный — средняя обработка (0.2-0.5 мм)",
      "Бархатный — чистовая (0.05-0.2 мм)",
      "Плоский — для плоских поверхностей",
      "Круглый — для отверстий и закруглений",
      "Трёхгранный — для углов и пазов"
  ])}
  
  {info_box(410, 275, 365, 123, "Правила безопасной работы", [
      "Закрепи заготовку в тисках надёжно!",
      "Ножовку веди ровно, без перекосов",
      "Опиливай движением «от себя»",
      "Сверло прижимай равномерно",
      "Стружку убирай щёткой, не рукой!",
      "Надевай защитные очки при рубке"
  ], RED)}
  
  {highlight_box(25, 415, 750, 50, [
      "🔧 Последовательность: разметка → закрепление → резание → опиливание → сверление → гибка → зачистка",
      "Качество обработки зависит от правильного выбора инструмента!"
  ])}
  
  <!-- Threading info -->
  {info_box(25, 480, 370, 100, "Нарезание резьбы", [
      "Метчик — внутренняя резьба (в отверстии)",
      "Плашка — наружная резьба (на стержне)",
      "М4, М5, М6, М8 — размеры метрической резьбы",
      "Смазывай маслом при нарезании!"
  ])}
  
  {info_box(410, 415, 365, 80, "Шабрение и притирка", [
      "Шабрение — снятие тонких слоев шабером",
      "Притирка — доводка до высокой точности",
      "Контроль: штангенциркуль, микрометр"
  ])}
  
  {info_box(410, 508, 365, 72, "Маркировка сталей", [
      "Ст3 — конструкционная, 45 — среднеуглерод.",
      "У8 — инструментальная углеродистая",
      "45Х — легированная хромистая"
  ])}
  """
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 8: Основы электротехники
# ============================================================
def lesson_8():
    svg = svg_header()
    svg += header_bar(8, "Основы электротехники", "Напряжение, ток, сопротивление, цепи")
    
    svg += f"""
  <!-- Ohm's Law triangle -->
  <polygon points="400,110 300,280 500,280" fill="{BG_WARM}" stroke="{PRIMARY}" stroke-width="2" filter="url(#shadow)"/>
  <line x1="350" y1="195" x2="450" y2="195" stroke="{PRIMARY}" stroke-width="1.5"/>
  <line x1="400" y1="195" x2="400" y2="280" stroke="{PRIMARY}" stroke-width="1.5"/>
  <text x="400" y="175" font-size="22" fill="{PRIMARY_DARK}" text-anchor="middle" font-weight="bold">U</text>
  <text x="350" y="250" font-size="18" fill="{PRIMARY}" text-anchor="middle" font-weight="bold">I</text>
  <text x="450" y="250" font-size="18" fill="{PRIMARY}" text-anchor="middle" font-weight="bold">R</text>
  <text x="400" y="300" font-size="13" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Закон Ома: U = I × R</text>
  
  <!-- Simple circuit diagram -->
  <rect x="25" y="100" width="230" height="180" rx="6" fill="{WHITE}" stroke="{PRIMARY}" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="140" y="120" font-size="12" fill="{PRIMARY_DARK}" text-anchor="middle" font-weight="bold">Простая электрическая цепь</text>
  
  <!-- Battery symbol -->
  <line x1="50" y1="180" x2="50" y2="220" stroke="{TEXT_DARK}" stroke-width="2"/>
  <line x1="40" y1="180" x2="60" y2="180" stroke="{TEXT_DARK}" stroke-width="2.5"/>
  <line x1="44" y1="188" x2="56" y2="188" stroke="{TEXT_DARK}" stroke-width="1.5"/>
  <line x1="40" y1="196" x2="60" y2="196" stroke="{TEXT_DARK}" stroke-width="2.5"/>
  <line x1="44" y1="204" x2="56" y2="204" stroke="{TEXT_DARK}" stroke-width="1.5"/>
  <line x1="40" y1="212" x2="60" y2="212" stroke="{TEXT_DARK}" stroke-width="2.5"/>
  <line x1="50" y1="165" x2="50" y2="180" stroke="{TEXT_DARK}" stroke-width="2"/>
  <text x="68" y="198" font-size="10" fill="{RED}">+</text>
  <text x="68" y="212" font-size="10" fill="{BLUE}">−</text>
  
  <!-- Wires -->
  <line x1="50" y1="165" x2="140" y2="165" stroke="{TEXT_DARK}" stroke-width="1.5"/>
  <line x1="140" y1="165" x2="200" y2="165" stroke="{TEXT_DARK}" stroke-width="1.5"/>
  <line x1="200" y1="165" x2="200" y2="220" stroke="{TEXT_DARK}" stroke-width="1.5"/>
  <line x1="200" y1="220" x2="50" y2="220" stroke="{TEXT_DARK}" stroke-width="1.5"/>
  
  <!-- Switch symbol -->
  <circle cx="140" cy="165" r="3" fill="{TEXT_DARK}"/>
  <line x1="140" y1="165" x2="160" y2="152" stroke="{TEXT_DARK}" stroke-width="1.5"/>
  <text x="140" y="145" font-size="9" fill="{BLUE}" text-anchor="middle">Ключ</text>
  
  <!-- Lamp symbol -->
  <circle cx="200" cy="192" r="12" fill="none" stroke="{TEXT_DARK}" stroke-width="1.5"/>
  <line x1="192" y1="184" x2="208" y2="200" stroke="{TEXT_DARK}" stroke-width="1"/>
  <line x1="208" y1="184" x2="192" y2="200" stroke="{TEXT_DARK}" stroke-width="1"/>
  <text x="200" y="240" font-size="9" fill="{BLUE}" text-anchor="middle">Лампа</text>
  
  <!-- Current direction -->
  <text x="120" y="160" font-size="9" fill="{RED}">→ I</text>
  
  <!-- Quantities -->
  {info_box(545, 100, 230, 130, "Электрические величины", [
      "U — напряжение (В, Вольт)",
      "I — сила тока (А, Ампер)",
      "R — сопротивление (Ом)",
      "P — мощность (Вт, Ватт)",
      "P = U × I = I²R = U²/R"
  ])}
  
  <!-- Series vs Parallel -->
  {info_box(25, 320, 370, 145, "Последовательное соединение", [
      "Проводники подключены друг за другом",
      "I₁ = I₂ = I₃ (ток одинаков)",
      "U = U₁ + U₂ + U₃ (напряжения складываются)",
      "R = R₁ + R₂ + R₃ (сопротивления складываются)",
      "Пример: ёлочная гирлянда",
      "⚠ Если одна лампа перегорит — все погаснут"
  ])}
  
  {info_box(410, 320, 365, 145, "Параллельное соединение", [
      "Проводники подключены к одним точкам",
      "U₁ = U₂ = U₃ (напряжение одинаково)",
      "I = I₁ + I₂ + I₃ (токи складываются)",
      "1/R = 1/R₁ + 1/R₂ (общее сопр. меньше)",
      "Пример: лампы в квартире",
      "✓ Одна лампа перегорит — остальные горят"
  ])}
  
  {highlight_box(25, 480, 750, 55, [
      "⚡ Закон Ома — фундамент электротехники: I = U/R",
      "Короткое замыкание: R → 0, I → max — ОПАСНО! Плавкие предохранители защищают цепь"
  ])}
  
  {info_box(25, 548, 750, 35, "", [
      "Амперметр — измеряет ток (подключается последовательно) | Вольтметр — измеряет напряжение (подключается параллельно)"
  ])}
  """
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 9: Бытовые электроприборы
# ============================================================
def lesson_9():
    svg = svg_header()
    svg += header_bar(9, "Бытовые электроприборы", "Безопасность, типы, обслуживание")
    
    svg += f"""
  <!-- Appliance categories - grid layout -->
  <!-- Heating -->
  <rect x="30" y="95" width="240" height="100" rx="8" fill="{WHITE}" stroke="{RED}" stroke-width="2" filter="url(#shadow)"/>
  <rect x="30" y="95" width="240" height="28" rx="8" fill="{RED}"/>
  <rect x="30" y="117" width="240" height="6" fill="{RED}"/>
  <text x="150" y="115" font-size="13" fill="{WHITE}" text-anchor="middle" font-weight="bold">Нагревательные</text>
  <text x="45" y="140" font-size="11" fill="{TEXT_DARK}">• Утюг — 1000-2200 Вт</text>
  <text x="45" y="156" font-size="11" fill="{TEXT_DARK}">• Обогреватель — 1500-2500 Вт</text>
  <text x="45" y="172" font-size="11" fill="{TEXT_DARK}">• Фен — 1200-2200 Вт</text>
  <text x="45" y="188" font-size="11" fill="{TEXT_DARK}">• Плита — 1000-3000 Вт</text>
  
  <!-- Mechanical -->
  <rect x="285" y="95" width="240" height="100" rx="8" fill="{WHITE}" stroke="{BLUE}" stroke-width="2" filter="url(#shadow)"/>
  <rect x="285" y="95" width="240" height="28" rx="8" fill="{BLUE}"/>
  <rect x="285" y="117" width="240" height="6" fill="{BLUE}"/>
  <text x="405" y="115" font-size="13" fill="{WHITE}" text-anchor="middle" font-weight="bold">Механические</text>
  <text x="300" y="140" font-size="11" fill="{TEXT_DARK}">• Пылесос — 1000-2200 Вт</text>
  <text x="300" y="156" font-size="11" fill="{TEXT_DARK}">• Миксер — 300-700 Вт</text>
  <text x="300" y="172" font-size="11" fill="{TEXT_DARK}">• Блендер — 400-1200 Вт</text>
  <text x="300" y="188" font-size="11" fill="{TEXT_DARK}">• Стиральная машина — 2000 Вт</text>
  
  <!-- Combined -->
  <rect x="540" y="95" width="240" height="100" rx="8" fill="{WHITE}" stroke="{GREEN}" stroke-width="2" filter="url(#shadow)"/>
  <rect x="540" y="95" width="240" height="28" rx="8" fill="{GREEN}"/>
  <rect x="540" y="117" width="240" height="6" fill="{GREEN}"/>
  <text x="660" y="115" font-size="13" fill="{WHITE}" text-anchor="middle" font-weight="bold">Комбинированные</text>
  <text x="555" y="140" font-size="11" fill="{TEXT_DARK}">• Холодильник — 100-400 Вт</text>
  <text x="555" y="156" font-size="11" fill="{TEXT_DARK}">• Кондиционер — 1000-3500 Вт</text>
  <text x="555" y="172" font-size="11" fill="{TEXT_DARK}">• Микроволновка — 700-1500 Вт</text>
  <text x="555" y="188" font-size="11" fill="{TEXT_DARK}">• Посудомойка — 1800-2500 Вт</text>
  
  <!-- Safety rules -->
  {info_box(25, 215, 375, 170, "⚠ Правила безопасности", [
      "Не прикасайся мокрыми руками к розетке!",
      "Не вытаскивай вилку за провод!",
      "Не используй неисправные приборы!",
      "Не перегружай розетки (не более 3500 Вт)!",
      "Заземляй приборы с металлическим корпусом!",
      "Отключай приборы уходя из дома!",
      "Не оставляй включённые приборы без присмотра!",
      "Не используй приборы рядом с водой!"
  ], RED)}
  
  <!-- Maintenance -->
  {info_box(415, 215, 365, 170, "Обслуживание приборов", [
      "Регулярная очистка от пыли и грязи",
      "Проверка целостности шнура и вилки",
      "Своевременная замена фильтров",
      "Не разбирать включённые приборы!",
      "Доверять ремонт специалистам",
      "Следить за сроком эксплуатации",
      "Использовать стабилизаторы напряжения",
      "Хранить инструкции по эксплуатации"
  ])}
  
  <!-- Energy efficiency -->
  {info_box(25, 400, 375, 100, "Классы энергоэффективности", [
      "A+++ — самый экономичный",
      "A++, A+ — высокая экономичность",
      "A, B — хорошая экономичность",
      "C, D — средняя",
      "E, F, G — низкая (не покупайте!)"
  ], GREEN)}
  
  {info_box(415, 400, 365, 100, "Экономия электроэнергии", [
      "Используй LED-лампы (экономия 80%)",
      "Выключай свет, выходя из комнаты",
      "Не открывай холодильник надолго",
      "Стирай при полной загрузке",
      "Используй таймеры и датчики движения"
  ], PRIMARY)}
  
  {highlight_box(25, 515, 750, 55, [
      "🔌 Мощность прибора = Напряжение × Сила тока. P = U × I",
      "Суммарная мощность включённых приборов не должна превышать нагрузку проводки!"
  ])}
  """
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 10: Основы кулинарии
# ============================================================
def lesson_10():
    svg = svg_header()
    svg += header_bar(10, "Основы кулинарии", "Гигиена, оборудование, продукты")
    
    svg += f"""
  <!-- Food groups diagram - plate model -->
  <ellipse cx="180" cy="230" rx="120" ry="90" fill="{WHITE}" stroke="{PRIMARY}" stroke-width="2" filter="url(#shadow)"/>
  <ellipse cx="180" cy="230" rx="115" ry="85" fill="none" stroke="{BORDER}" stroke-width="1"/>
  
  <!-- Food sections -->
  <path d="M180,140 L180,230 L90,175 A115,85 0 0,1 180,140Z" fill="#86EFAC" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <path d="M180,230 L270,175 A115,85 0 0,1 180,320Z" fill="#FDE68A" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <path d="M180,230 L90,285 A115,85 0 0,1 90,175Z" fill="#FCA5A5" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  <path d="M180,230 L270,285 A115,85 0 0,1 180,320Z" fill="#93C5FD" stroke="{PRIMARY_DARK}" stroke-width="1"/>
  
  <text x="130" y="185" font-size="10" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Овощи</text>
  <text x="130" y="196" font-size="10" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">и фрукты</text>
  <text x="230" y="185" font-size="10" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Злаки,</text>
  <text x="230" y="196" font-size="10" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">хлеб</text>
  <text x="130" y="280" font-size="10" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Мясо,</text>
  <text x="130" y="291" font-size="10" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">рыба</text>
  <text x="230" y="280" font-size="10" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Молочные</text>
  <text x="230" y="291" font-size="10" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">продукты</text>
  
  <text x="180" y="235" font-size="9" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">Здоровая</text>
  <text x="180" y="246" font-size="9" fill="{TEXT_DARK}" text-anchor="middle" font-weight="bold">тарелка</text>
  
  <!-- Hygiene rules -->
  {info_box(345, 95, 430, 155, "Правила гигиены на кухне", [
      "Мой руки перед готовкой и после каждого перерыва!",
      "Используй отдельные доски для мяса и овощей",
      "Мой овощи и фрукты перед приготовлением",
      "Храни продукты при правильной температуре",
      "Не используй продукты с истёкшим сроком",
      "Следи за чистотой рабочей поверхности",
      "Надевай фартук и убирай волосы"
  ], RED)}
  
  <!-- Kitchen equipment -->
  {info_box(345, 265, 430, 125, "Кухонное оборудование", [
      "Кастрюли и сковороды — варка и жарка",
      "Ножи: поварской, хлебный, для овощей",
      "Разделочные доски: мясо / овощи / хлеб",
      "Мерный стакан и кухонные весы",
      "Венчик, лопатка, шумовка, дуршлаг"
  ])}
  
  <!-- Cooking methods -->
  {info_box(25, 345, 240, 130, "Способы тепловой обработки", [
      "Варка — в воде или на пару",
      "Жарка — на сковороде с маслом",
      "Запекание — в духовке",
      "Тушение — с небольшим количеством воды",
      "Бланширование — краткая варка"
  ])}
  
  {info_box(280, 345, 240, 130, "Виды нарезки продуктов", [
      "Кубиками — для супов и рагу",
      "Соломкой — для салатов",
      "Кольцами — лук, морковь",
      "Ломтиками — для бутербродов",
      "Крошка — для посыпки"
  ])}
  
  {info_box(535, 405, 240, 70, "Температурные режимы", [
      "Варка: 100°C (кипение воды)",
      "Жарка: 150-200°C",
      "Духовка: 160-250°C"
  ])}
  
  {highlight_box(25, 490, 750, 55, [
      "🍽 Пищевая безопасность: мясо — полностью прожаривать, яйца — не сырые,",
      "молоко — кипятить! Разделочные доски — отдельные для каждого типа продуктов!"
  ])}
  
  {info_box(535, 345, 240, 50, "СанПиН нормы", [
      "Мясная доска — красная, Овощная — зелёная"
  ])}
  """
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 11: Приготовление блюд
# ============================================================
def lesson_11():
    svg = svg_header()
    svg += header_bar(11, "Приготовление блюд", "Рецепты, техники, планирование")
    
    svg += f"""
  <!-- Recipe card -->
  <rect x="25" y="95" width="280" height="250" rx="8" fill="{WHITE}" stroke="{PRIMARY}" stroke-width="2" filter="url(#shadow)"/>
  <rect x="25" y="95" width="280" height="35" rx="8" fill="{PRIMARY}"/>
  <rect x="25" y="122" width="280" height="8" fill="{PRIMARY}"/>
  <text x="165" y="118" font-size="14" fill="{WHITE}" text-anchor="middle" font-weight="bold">Рецепт: Каша рисовая</text>
  
  <text x="40" y="155" font-size="12" fill="{PRIMARY_DARK}" font-weight="bold">Ингредиенты:</text>
  <text x="40" y="172" font-size="11" fill="{TEXT_DARK}">• Рис — 1 стакан (200 г)</text>
  <text x="40" y="188" font-size="11" fill="{TEXT_DARK}">• Молоко — 2 стакана (500 мл)</text>
  <text x="40" y="204" font-size="11" fill="{TEXT_DARK}">• Вода — 1 стакан (250 мл)</text>
  <text x="40" y="220" font-size="11" fill="{TEXT_DARK}">• Масло сливочное — 30 г</text>
  <text x="40" y="236" font-size="11" fill="{TEXT_DARK}">• Сахар — 2 ст. ложки</text>
  <text x="40" y="252" font-size="11" fill="{TEXT_DARK}">• Соль — 0,5 ч. ложки</text>
  
  <text x="40" y="275" font-size="12" fill="{PRIMARY_DARK}" font-weight="bold">Технология:</text>
  <text x="40" y="292" font-size="11" fill="{TEXT_DARK}">1. Промыть рис, залить водой</text>
  <text x="40" y="308" font-size="11" fill="{TEXT_DARK}">2. Варить до полуготовности</text>
  <text x="40" y="324" font-size="11" fill="{TEXT_DARK}">3. Добавить молоко, варить 15 мин</text>
  <text x="40" y="340" font-size="11" fill="{TEXT_DARK}">4. Добавить масло и сахар</text>
  
  <!-- Cooking techniques -->
  {info_box(320, 95, 455, 130, "Основные техники приготовления", [
      "Варка — нагревание в жидкой среде (100°C)",
      "Припускание — варка в малом количестве воды",
      "Жарка — нагревание с жиром (150-200°C)",
      "Тушение — обжарка + варка в соусе",
      "Запекание — приготовление в духовке"
  ])}
  
  <!-- Meal planning -->
  {info_box(320, 240, 455, 120, "Планирование меню", [
      "Завтрак: каши, яичница, бутерброды, чай",
      "Обед: суп, второе блюдо, салат, компот",
      "Полдник: фрукты, выпечка, кефир",
      "Ужин: лёгкое блюдо за 3 часа до сна",
      "Суточная норма: белки 30%, жиры 25%, углеводы 45%"
  ])}
  
  <!-- Kitchen safety during cooking -->
  {info_box(25, 360, 370, 120, "Безопасность при готовке", [
      "Осторожно с кипящей водой и маслом!",
      "Ручки сковород — от себя",
      "Не наливай масло на раскалённую сковороду",
      "Снимай крышку от себя (пар обжигает!)",
      "Используй прихватки для горячей посуды",
      "Не оставляй плиту без присмотра"
  ], RED)}
  
  <!-- Nutrition basics -->
  {info_box(410, 375, 365, 105, "Пищевая ценность продуктов", [
      "Белки — «строительный материал» (мясо, рыба)",
      "Жиры — энергетический запас (масло, орехи)",
      "Углеводы — основной источник энергии",
      "Витамины — для здоровья (овощи, фрукты)",
      "Минеральные вещества — кости, кровь"
  ], GREEN)}
  
  {highlight_box(25, 495, 750, 55, [
      "📖 Правило рецепта: строго соблюдай пропорции и последовательность операций!",
      "Время и температура — ключевые параметры. Термометр для мяса — гарантия безопасности!"
  ])}
  """
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 12: Современные технологии в промышленности
# ============================================================
def lesson_12():
    svg = svg_header()
    svg += header_bar(12, "Современные технологии в промышленности", "ЧПУ, 3D-печать, автоматизация")
    
    svg += f"""
  <!-- Technology icons - modern grid -->
  <!-- CNC Machine -->
  <rect x="30" y="95" width="180" height="130" rx="8" fill="{WHITE}" stroke="{BLUE}" stroke-width="2" filter="url(#shadow)"/>
  <rect x="30" y="95" width="180" height="28" rx="8" fill="{BLUE}"/>
  <rect x="30" y="117" width="180" height="6" fill="{BLUE}"/>
  <text x="120" y="115" font-size="12" fill="{WHITE}" text-anchor="middle" font-weight="bold">ЧПУ-станок</text>
  <!-- CNC illustration -->
  <rect x="50" y="133" width="60" height="40" fill="#E5E7EB" stroke="#6B7280" stroke-width="1"/>
  <rect x="60" y="138" width="40" height="30" fill="#D1D5DB" stroke="#6B7280" stroke-width="0.5"/>
  <line x1="80" y1="143" x2="80" y2="163" stroke="{RED}" stroke-width="1.5"/>
  <circle cx="80" cy="143" r="3" fill="{RED}"/>
  <rect x="120" y="133" width="70" height="40" fill="#F3F4F6" stroke="#6B7280" stroke-width="0.5"/>
  <text x="155" y="148" font-size="8" fill="{GRAY}" text-anchor="middle">G-код</text>
  <text x="155" y="160" font-size="7" fill="{GRAY}" text-anchor="middle">X12 Y34 Z5</text>
  <text x="50" y="192" font-size="9" fill="{TEXT_DARK}">Высокая точность</text>
  <text x="50" y="204" font-size="9" fill="{TEXT_DARK}">до 0.01 мм</text>
  
  <!-- 3D Printing -->
  <rect x="225" y="95" width="180" height="130" rx="8" fill="{WHITE}" stroke="{GREEN}" stroke-width="2" filter="url(#shadow)"/>
  <rect x="225" y="95" width="180" height="28" rx="8" fill="{GREEN}"/>
  <rect x="225" y="117" width="180" height="6" fill="{GREEN}"/>
  <text x="315" y="115" font-size="12" fill="{WHITE}" text-anchor="middle" font-weight="bold">3D-печать</text>
  <!-- 3D printer illustration -->
  <rect x="260" y="133" width="50" height="50" fill="none" stroke="#6B7280" stroke-width="1.5"/>
  <rect x="270" y="165" width="30" height="5" fill="#86EFAC" stroke="{GREEN}" stroke-width="0.5"/>
  <rect x="268" y="158" width="34" height="8" fill="#86EFAC" stroke="{GREEN}" stroke-width="0.5"/>
  <line x1="285" y1="133" x2="285" y2="158" stroke="#6B7280" stroke-width="1"/>
  <text x="325" y="152" font-size="8" fill="{GRAY}">PLA/ABS</text>
  <text x="325" y="164" font-size="8" fill="{GRAY}">Слой за слоем</text>
  <text x="245" y="192" font-size="9" fill="{TEXT_DARK}">Аддитивная технология</text>
  <text x="245" y="204" font-size="9" fill="{TEXT_DARK}">Сложные формы</text>
  
  <!-- Laser cutting -->
  <rect x="420" y="95" width="180" height="130" rx="8" fill="{WHITE}" stroke="{RED}" stroke-width="2" filter="url(#shadow)"/>
  <rect x="420" y="95" width="180" height="28" rx="8" fill="{RED}"/>
  <rect x="420" y="117" width="180" height="6" fill="{RED}"/>
  <text x="510" y="115" font-size="12" fill="{WHITE}" text-anchor="middle" font-weight="bold">Лазерная резка</text>
  <!-- Laser illustration -->
  <rect x="445" y="140" width="60" height="40" fill="none" stroke="#6B7280" stroke-width="1"/>
  <line x1="475" y1="140" x2="475" y2="170" stroke="{RED}" stroke-width="1.5"/>
  <circle cx="475" cy="175" r="3" fill="{RED}" opacity="0.7"/>
  <text x="515" y="152" font-size="8" fill="{GRAY}">CO₂ лазер</text>
  <text x="515" y="164" font-size="8" fill="{GRAY}">10600 нм</text>
  <text x="440" y="192" font-size="9" fill="{TEXT_DARK}">Точность 0.1 мм</text>
  <text x="440" y="204" font-size="9" fill="{TEXT_DARK}">Листовой материал</text>
  
  <!-- Robotics -->
  <rect x="615" y="95" width="165" height="130" rx="8" fill="{WHITE}" stroke="{ACCENT}" stroke-width="2" filter="url(#shadow)"/>
  <rect x="615" y="95" width="165" height="28" rx="8" fill="{ACCENT}"/>
  <rect x="615" y="117" width="165" height="6" fill="{ACCENT}"/>
  <text x="697" y="115" font-size="12" fill="{WHITE}" text-anchor="middle" font-weight="bold">Робототехника</text>
  <!-- Robot arm -->
  <line x1="670" y1="180" x2="700" y2="155" stroke="#6B7280" stroke-width="3"/>
  <line x1="700" y1="155" x2="730" y2="170" stroke="#6B7280" stroke-width="3"/>
  <circle cx="670" cy="180" r="5" fill="#D97706"/>
  <circle cx="700" cy="155" r="4" fill="#D97706"/>
  <rect x="660" y="183" width="20" height="20" fill="#9CA3AF" stroke="#6B7280" stroke-width="1"/>
  <text x="635" y="192" font-size="9" fill="{TEXT_DARK}">Автоматизация</text>
  <text x="635" y="204" font-size="9" fill="{TEXT_DARK}">процессов</text>
  
  <!-- Detailed info -->
  {info_box(25, 240, 250, 140, "ЧПУ-обработка", [
      "CNC — Computer Numerical Control",
      "Фрезерные, токарные, сверлильные",
      "Управление через G-код",
      "Точность до 0.01 мм",
      "Повторяемость изделий",
      "CAD → CAM → ЧПУ-станок"
  ], BLUE)}
  
  {info_box(290, 240, 250, 140, "3D-печать: технологии", [
      "FDM — послойное наплавление",
      "SLA — стереолитография (ультрафиолет)",
      "SLS — селективное спекание",
      "Материалы: PLA, ABS, нейлон",
      "Металлическая печать (DMLS)",
      "Биопечать органов (перспектива)"
  ], GREEN)}
  
  {info_box(555, 240, 225, 140, "Индустрия 4.0", [
      "IoT — интернет вещей",
      "ИИ — искусственный интеллект",
      "Big Data — большие данные",
      "Облачные вычисления",
      "Цифровые двойники",
      "Гибкое производство"
  ], ACCENT)}
  
  {highlight_box(25, 395, 750, 50, [
      "🏭 CAD (проектирование) → CAM (подготовка программы) → ЧПУ (изготовление) — цифровая цепочка",
      "Современное производство: от идеи до изделия без бумажных чертежей!"
  ])}
  
  <!-- Industry comparison -->
  {info_box(25, 460, 370, 120, "Эволюция производства", [
      "1.0 — паровые машины (XVIII в.)",
      "2.0 — конвейер, электричество (XX в.)",
      "3.0 — компьютеры, автоматизация (1970-е)",
      "4.0 — IoT, ИИ, роботы (сейчас)",
      "5.0 — человек + ИИ (будущее)"
  ])}
  
  {info_box(410, 460, 365, 120, "Преимущества современных технологий", [
      "Высокая точность и повторяемость",
      "Сокращение отходов материала",
      "Быстрое прототипирование",
      "Гибкая настройка на новое изделие",
      "Удалённый контроль и мониторинг",
      "Снижение доли ручного труда"
  ])}
  """
    svg += svg_footer()
    return svg


# ============================================================
# LESSON 13: Профессии современного производства
# ============================================================
def lesson_13():
    svg = svg_header()
    svg += header_bar(13, "Профессии современного производства", "Инженерия, IT, рабочие специальности")
    
    svg += f"""
  <!-- Professional sectors - card layout -->
  <!-- Engineering -->
  <rect x="25" y="95" width="245" height="135" rx="8" fill="{WHITE}" stroke="{BLUE}" stroke-width="2" filter="url(#shadow)"/>
  <rect x="25" y="95" width="245" height="30" rx="8" fill="{BLUE}"/>
  <rect x="25" y="119" width="245" height="6" fill="{BLUE}"/>
  <text x="147" y="116" font-size="13" fill="{WHITE}" text-anchor="middle" font-weight="bold">🔧 Инженерные</text>
  <text x="40" y="143" font-size="11" fill="{TEXT_DARK}">• Инженер-конструктор</text>
  <text x="40" y="159" font-size="11" fill="{TEXT_DARK}">• Инженер-технолог</text>
  <text x="40" y="175" font-size="11" fill="{TEXT_DARK}">• Инженер-программист ЧПУ</text>
  <text x="40" y="191" font-size="11" fill="{TEXT_DARK}">• Инженер по качеству</text>
  <text x="40" y="207" font-size="11" fill="{TEXT_DARK}">• Проектировщик CAD/CAM</text>
  <text x="40" y="223" font-size="9" fill="{BLUE}" font-style="italic">Зарплата: 60-150 тыс. ₽</text>
  
  <!-- IT -->
  <rect x="285" y="95" width="245" height="135" rx="8" fill="{WHITE}" stroke="{GREEN}" stroke-width="2" filter="url(#shadow)"/>
  <rect x="285" y="95" width="245" height="30" rx="8" fill="{GREEN}"/>
  <rect x="285" y="119" width="245" height="6" fill="{GREEN}"/>
  <text x="407" y="116" font-size="13" fill="{WHITE}" text-anchor="middle" font-weight="bold">💻 IT-специалисты</text>
  <text x="300" y="143" font-size="11" fill="{TEXT_DARK}">• Программист / Разработчик</text>
  <text x="300" y="159" font-size="11" fill="{TEXT_DARK}">• Специалист по ИИ и ML</text>
  <text x="300" y="175" font-size="11" fill="{TEXT_DARK}">• Data Scientist / Аналитик</text>
  <text x="300" y="191" font-size="11" fill="{TEXT_DARK}">• DevOps-инженер</text>
  <text x="300" y="207" font-size="11" fill="{TEXT_DARK}">• Кибербезопасник</text>
  <text x="300" y="223" font-size="9" fill="{GREEN}" font-style="italic">Зарплата: 80-300 тыс. ₽</text>
  
  <!-- Skilled trades -->
  <rect x="545" y="95" width="235" height="135" rx="8" fill="{WHITE}" stroke="{ACCENT}" stroke-width="2" filter="url(#shadow)"/>
  <rect x="545" y="95" width="235" height="30" rx="8" fill="{ACCENT}"/>
  <rect x="545" y="119" width="235" height="6" fill="{ACCENT}"/>
  <text x="662" y="116" font-size="13" fill="{WHITE}" text-anchor="middle" font-weight="bold">⚒ Рабочие специальности</text>
  <text x="560" y="143" font-size="11" fill="{TEXT_DARK}">• Токарь-фрезеровщик ЧПУ</text>
  <text x="560" y="159" font-size="11" fill="{TEXT_DARK}">• Оператор 3D-печати</text>
  <text x="560" y="175" font-size="11" fill="{TEXT_DARK}">• Сварщик</text>
  <text x="560" y="191" font-size="11" fill="{TEXT_DARK}">• Электромонтажник</text>
  <text x="560" y="207" font-size="11" fill="{TEXT_DARK}">• Наладчик оборудования</text>
  <text x="560" y="223" font-size="9" fill="{ACCENT}" font-style="italic">Зарплата: 50-120 тыс. ₽</text>
  
  <!-- Skills needed -->
  {info_box(25, 248, 250, 145, "Ключевые навыки будущего", [
      "Критическое мышление и логика",
      "Программирование и алгоритмы",
      "Работа с данными и аналитика",
      "Креативность и инновации",
      "Коммуникация и командная работа",
      "Адаптивность и самообучение"
  ], PRIMARY)}
  
  {info_box(290, 248, 250, 145, "Образование и обучение", [
      "Колледж — рабочая специальность",
      "ВУЗ — инженерное образование",
      "Курсы — переквалификация",
      "Онлайн-обучение — новые навыки",
      "Стажировки — практический опыт",
      "Непрерывное обучение (Lifelong Learning)"
  ], GREEN)}
  
  {info_box(555, 248, 225, 145, "Тренды рынка труда", [
      "Автоматизация рутины",
      "Дистанционная работа",
      "Междисциплинарность",
      "Soft skills наравне с Hard",
      "Дефицит инженеров",
      "Рост сектора IT"
  ], ACCENT)}
  
  {highlight_box(25, 410, 750, 50, [
      "🌟 Профессия будущего = технические знания + цифровые навыки + креативность",
      "Рабочие специальности с навыками ЧПУ и 3D-печати востребованы больше, чем когда-либо!"
  ])}
  
  <!-- Career path -->
  {info_box(25, 478, 375, 105, "Путь в профессию", [
      "7-9 класс: кружки, олимпиады, профориентация",
      "10-11 класс: профильные предметы, курсы",
      "Колледж: практические навыки, стажировки",
      "ВУЗ: глубокие знания, исследования",
      "Работа: наставничество, повышение квалификации"
  ])}
  
  {info_box(415, 478, 365, 105, "Профессии в tecnologii (8 класс)", [
      "Столяр — обработка древесины",
      "Слесарь — обработка металла",
      "Электромонтёр — электрические сети",
      "Повар — кулинарное дело",
      "Оператор станков с ЧПУ — современные технологии",
      "Инженер — проектирование и управление"
  ])}
  """
    svg += svg_footer()
    return svg


# ============================================================
# Main: Generate all SVGs
# ============================================================
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    generators = [
        (1, lesson_1),
        (2, lesson_2),
        (3, lesson_3),
        (4, lesson_4),
        (5, lesson_5),
        (6, lesson_6),
        (7, lesson_7),
        (8, lesson_8),
        (9, lesson_9),
        (10, lesson_10),
        (11, lesson_11),
        (12, lesson_12),
        (13, lesson_13),
    ]
    
    results = []
    for num, gen_func in generators:
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
        svg_content = gen_func()
        
        # Write file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)
        
        # Validate with xml.etree.ElementTree
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            results.append((num, filepath, "✓ VALID", None))
        except ET.ParseError as e:
            results.append((num, filepath, "✗ INVALID", str(e)))
    
    # Print results
    print("=" * 70)
    print("Grade 8 Technology SVG Generation Results")
    print("=" * 70)
    for num, path, status, error in results:
        print(f"  Lesson {num:2d}: {path} — {status}")
        if error:
            print(f"           Error: {error}")
    
    valid_count = sum(1 for _, _, s, _ in results if "VALID" in s and "IN" not in s)
    invalid_count = len(results) - valid_count
    print("-" * 70)
    print(f"  Total: {len(results)} | Valid: {valid_count} | Invalid: {invalid_count}")
    print("=" * 70)
    
    return invalid_count == 0


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
