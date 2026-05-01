#!/usr/bin/env python3
"""Generate 12 SVG images for Grade 8 Physical Education (Физкультура/ОБЖ) lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/pe"
WIDTH = 800
HEIGHT = 600

# Color scheme
PRIMARY = "#22C55E"      # energetic green
ACCENT = "#EF4444"       # red accent
PRIMARY_DARK = "#16A34A"  # darker green
ACCENT_DARK = "#DC2626"   # darker red
BG_LIGHT = "#F0FDF4"     # very light green bg
BG_ACCENT = "#FEF2F2"    # very light red bg
TEXT_DARK = "#1E293B"     # dark text
TEXT_MED = "#475569"      # medium text
WHITE = "#FFFFFF"
LIGHT_GREEN = "#BBF7D0"
LIGHT_RED = "#FECACA"
MID_GREEN = "#86EFAC"
MID_RED = "#FCA5A5"

def escape_xml(text):
    """Escape special XML characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def svg_header():
    """Return common SVG header elements as string."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">'''


def bg_rect(color=BG_LIGHT):
    """Background rectangle."""
    return f'<rect width="{WIDTH}" height="{HEIGHT}" fill="{color}" rx="12"/>'


def title_banner(y, text, color=PRIMARY):
    """Green/red title banner at top."""
    return f'''
  <rect x="0" y="{y}" width="{WIDTH}" height="60" fill="{color}" rx="0"/>
  <text x="{WIDTH//2}" y="{y+38}" text-anchor="middle" font-family="Arial, sans-serif" font-size="24" font-weight="bold" fill="{WHITE}">{escape_xml(text)}</text>'''


def subtitle_bar(y, text, color=PRIMARY_DARK):
    """Smaller subtitle bar."""
    return f'''
  <rect x="20" y="{y}" width="{WIDTH-40}" height="36" fill="{color}" rx="8"/>
  <text x="{WIDTH//2}" y="{y+24}" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="{WHITE}">{escape_xml(text)}</text>'''


def info_box(x, y, w, h, title, lines, box_color=WHITE, border_color=PRIMARY, title_bg=PRIMARY):
    """Rounded info box with title and bullet lines."""
    parts = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{box_color}" stroke="{border_color}" stroke-width="2" rx="8"/>',
        f'<rect x="{x}" y="{y}" width="{w}" height="28" fill="{title_bg}" rx="8"/>',
        f'<rect x="{x}" y="{y+20}" width="{w}" height="8" fill="{title_bg}"/>',
        f'<text x="{x+w//2}" y="{y+19}" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{WHITE}">{escape_xml(title)}</text>',
    ]
    ly = y + 44
    for line in lines:
        parts.append(f'<text x="{x+12}" y="{ly}" font-family="Arial, sans-serif" font-size="12" fill="{TEXT_DARK}">{escape_xml(line)}</text>')
        ly += 18
    return '\n'.join(parts)


def accent_box(x, y, w, h, title, lines, box_color=WHITE, border_color=ACCENT, title_bg=ACCENT):
    """Red accent info box."""
    return info_box(x, y, w, h, title, lines, box_color, border_color, title_bg)


def icon_circle(cx, cy, r, color, label):
    """Circle with text inside."""
    return f'''
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" opacity="0.9"/>
  <text x="{cx}" y="{cy+5}" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{WHITE}">{escape_xml(label)}</text>'''


def stickman(x, y, scale=1.0, color=TEXT_DARK, pose="standing"):
    """Draw a simple stick figure. Poses: standing, running, jumping, throwing, swimming."""
    s = scale
    parts = []
    # Head
    parts.append(f'<circle cx="{x}" cy="{y - 30*s}" r="{8*s}" fill="none" stroke="{color}" stroke-width="{2*s}"/>')
    if pose == "standing":
        # Body
        parts.append(f'<line x1="{x}" y1="{y-22*s}" x2="{x}" y2="{y+10*s}" stroke="{color}" stroke-width="{2*s}"/>')
        # Arms
        parts.append(f'<line x1="{x}" y1="{y-12*s}" x2="{x-15*s}" y2="{y+2*s}" stroke="{color}" stroke-width="{2*s}"/>')
        parts.append(f'<line x1="{x}" y1="{y-12*s}" x2="{x+15*s}" y2="{y+2*s}" stroke="{color}" stroke-width="{2*s}"/>')
        # Legs
        parts.append(f'<line x1="{x}" y1="{y+10*s}" x2="{x-12*s}" y2="{y+30*s}" stroke="{color}" stroke-width="{2*s}"/>')
        parts.append(f'<line x1="{x}" y1="{y+10*s}" x2="{x+12*s}" y2="{y+30*s}" stroke="{color}" stroke-width="{2*s}"/>')
    elif pose == "running":
        parts.append(f'<line x1="{x}" y1="{y-22*s}" x2="{x+3*s}" y2="{y+10*s}" stroke="{color}" stroke-width="{2*s}"/>')
        parts.append(f'<line x1="{x+2*s}" y1="{y-12*s}" x2="{x-14*s}" y2="{y-4*s}" stroke="{color}" stroke-width="{2*s}"/>')
        parts.append(f'<line x1="{x+2*s}" y1="{y-12*s}" x2="{x+18*s}" y2="{y-18*s}" stroke="{color}" stroke-width="{2*s}"/>')
        parts.append(f'<line x1="{x+3*s}" y1="{y+10*s}" x2="{x-10*s}" y2="{y+30*s}" stroke="{color}" stroke-width="{2*s}"/>')
        parts.append(f'<line x1="{x+3*s}" y1="{y+10*s}" x2="{x+16*s}" y2="{y+26*s}" stroke="{color}" stroke-width="{2*s}"/>')
    elif pose == "jumping":
        parts.append(f'<line x1="{x}" y1="{y-22*s}" x2="{x}" y2="{y+10*s}" stroke="{color}" stroke-width="{2*s}"/>')
        parts.append(f'<line x1="{x}" y1="{y-12*s}" x2="{x-18*s}" y2="{y-20*s}" stroke="{color}" stroke-width="{2*s}"/>')
        parts.append(f'<line x1="{x}" y1="{y-12*s}" x2="{x+18*s}" y2="{y-20*s}" stroke="{color}" stroke-width="{2*s}"/>')
        parts.append(f'<line x1="{x}" y1="{y+10*s}" x2="{x-16*s}" y2="{y+25*s}" stroke="{color}" stroke-width="{2*s}"/>')
        parts.append(f'<line x1="{x}" y1="{y+10*s}" x2="{x+16*s}" y2="{y+25*s}" stroke="{color}" stroke-width="{2*s}"/>')
    elif pose == "throwing":
        parts.append(f'<line x1="{x}" y1="{y-22*s}" x2="{x+2*s}" y2="{y+10*s}" stroke="{color}" stroke-width="{2*s}"/>')
        parts.append(f'<line x1="{x+1*s}" y1="{y-12*s}" x2="{x-14*s}" y2="{y+2*s}" stroke="{color}" stroke-width="{2*s}"/>')
        parts.append(f'<line x1="{x+1*s}" y1="{y-12*s}" x2="{x+20*s}" y2="{y-22*s}" stroke="{color}" stroke-width="{2*s}"/>')
        parts.append(f'<line x1="{x+2*s}" y1="{y+10*s}" x2="{x-8*s}" y2="{y+30*s}" stroke="{color}" stroke-width="{2*s}"/>')
        parts.append(f'<line x1="{x+2*s}" y1="{y+10*s}" x2="{x+14*s}" y2="{y+28*s}" stroke="{color}" stroke-width="{2*s}"/>')
    elif pose == "swimming":
        parts.append(f'<line x1="{x}" y1="{y-22*s}" x2="{x+5*s}" y2="{y+8*s}" stroke="{color}" stroke-width="{2*s}"/>')
        parts.append(f'<line x1="{x+2*s}" y1="{y-10*s}" x2="{x+22*s}" y2="{y-16*s}" stroke="{color}" stroke-width="{2*s}"/>')
        parts.append(f'<line x1="{x+2*s}" y1="{y-10*s}" x2="{x-16*s}" y2="{y-14*s}" stroke="{color}" stroke-width="{2*s}"/>')
        parts.append(f'<line x1="{x+5*s}" y1="{y+8*s}" x2="{x+18*s}" y2="{y+4*s}" stroke="{color}" stroke-width="{2*s}"/>')
        parts.append(f'<line x1="{x+5*s}" y1="{y+8*s}" x2="{x-12*s}" y2="{y+14*s}" stroke="{color}" stroke-width="{2*s}"/>')
    return '\n'.join(parts)


def decorative_dots(x, y, count=5, color=PRIMARY, r=4):
    """Decorative dots in a row."""
    parts = []
    for i in range(count):
        parts.append(f'<circle cx="{x + i*14}" cy="{y}" r="{r}" fill="{color}" opacity="0.3"/>')
    return '\n'.join(parts)


def footer_bar(lesson_num):
    """Bottom footer bar."""
    return f'''
  <rect x="0" y="{HEIGHT-32}" width="{WIDTH}" height="32" fill="{PRIMARY_DARK}"/>
  <text x="{WIDTH//2}" y="{HEIGHT-10}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{WHITE}">8 класс | Физкультура/ОБЖ | Урок {lesson_num}</text>'''


def generate_lesson_1():
    """Lesson 1: Гимнастика: виды и значение"""
    svg = svg_header()
    svg += bg_rect()
    svg += title_banner(0, "Гимнастика: виды и значение")
    
    # Three columns for gymnastics types
    # Artistic gymnastics
    svg += info_box(20, 80, 240, 200, "Спортивная гимнастика", [
        "• Опорный прыжок",
        "• Вольные упражнения",
        "• Перекладина",
        "• Брусья",
        "• Бревно (жен.)",
        "• Кольца (муж.)",
    ])
    # Rhythmic gymnastics
    svg += accent_box(280, 80, 240, 200, "Художественная гимнастика", [
        "• Скакалка",
        "• Обруч",
        "• Мяч",
        "• Булавы",
        "• Лента",
        "• Только женщины",
    ])
    # Acrobatic
    svg += info_box(540, 80, 240, 200, "Акробатика", [
        "• Кувырки вперёд/назад",
        "• Стойка на руках",
        "• Колесо",
        "• Мостик",
        "• Сальто",
        "• Балансировки",
    ])
    
    # Stickmen in different gymnastic poses
    svg += stickman(140, 340, 1.2, PRIMARY_DARK, "jumping")
    svg += stickman(400, 340, 1.2, ACCENT_DARK, "standing")
    svg += stickman(660, 340, 1.2, PRIMARY_DARK, "jumping")
    
    # Labels under stickmen
    svg += f'<text x="140" y="395" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{TEXT_MED}">Вольные</text>'
    svg += f'<text x="400" y="395" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{TEXT_MED}">С предметами</text>'
    svg += f'<text x="660" y="395" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{TEXT_MED}">Акробатика</text>'
    
    # Value/importance section
    svg += subtitle_bar(410, "Значение гимнастики")
    svg += info_box(20, 460, 370, 90, "Физическое развитие", [
        "• Развитие силы, гибкости, координации",
        "• Формирование правильной осанки",
        "• Укрепление мышечного корсета",
    ])
    svg += accent_box(410, 460, 370, 90, "Психическое развитие", [
        "• Воспитание дисциплины и смелости",
        "• Развитие самоконтроля",
        "• Формирование эстетического вкуса",
    ])
    
    svg += footer_bar(1)
    svg += '</svg>'
    return svg


def generate_lesson_2():
    """Lesson 2: Лёгкая атлетика: королева спорта"""
    svg = svg_header()
    svg += bg_rect()
    svg += title_banner(0, "Лёгкая атлетика: королева спорта")
    
    # Three main categories
    svg += info_box(20, 80, 245, 180, "Бег", [
        "• Спринт (60м, 100м, 200м)",
        "• Средние дистанции (800м, 1500м)",
        "• Длинные дистанции (5000м, 10000м)",
        "• Эстафета (4х100м, 4х400м)",
        "• Барьерный бег",
        "• Марафон (42 195 м)",
    ])
    svg += accent_box(277, 80, 245, 180, "Прыжки", [
        "• Прыжок в длину с разбега",
        "• Тройной прыжок",
        "• Прыжок в высоту",
        "• Прыжок с шестом",
        "",
        "Фаза: разбег -> толчок ->",
        "  полёт -> приземление",
    ])
    svg += info_box(535, 80, 245, 180, "Метания", [
        "• Толкание ядра",
        "• Метание копья",
        "• Метание диска",
        "• Метание молота",
        "",
        "Техника: хват -> разбег ->",
        "  финальное усилие -> выпуск",
    ])
    
    # Running track diagram
    svg += subtitle_bar(275, "Беговая дорожка — схема")
    # Draw a simplified oval track
    svg += f'''
  <ellipse cx="400" cy="370" rx="280" ry="60" fill="none" stroke="{PRIMARY}" stroke-width="3"/>
  <ellipse cx="400" cy="370" rx="230" ry="40" fill="none" stroke="{PRIMARY_DARK}" stroke-width="2" stroke-dasharray="8,4"/>
  <line x1="120" y1="370" x2="120" y2="310" stroke="{ACCENT}" stroke-width="3"/>
  <text x="122" y="305" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{ACCENT}" font-weight="bold">СТАРТ</text>
  <line x1="680" y1="370" x2="680" y2="310" stroke="{ACCENT}" stroke-width="3"/>
  <text x="678" y="305" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{ACCENT}" font-weight="bold">ФИНИШ</text>'''
    
    # Runner on track
    svg += stickman(300, 358, 1.0, ACCENT_DARK, "running")
    
    # Key facts box
    svg += accent_box(20, 440, 370, 110, "Почему «королева спорта»?", [
        "• Самый древний вид соревнований",
      "• Входит в программу Олимпиад с 776 г. до н.э.",
      "• Наиболее массовый вид спорта",
      "• Базовая подготовка для всех видов",
    ])
    svg += info_box(410, 440, 370, 110, "Мировые рекорды (муж.)", [
        "• 100 м — 9,58 с (У. Болт)",
        "• 200 м — 19,19 с (У. Болт)",
        "• Прыжок в длину — 8,95 м",
        "• Прыжок в высоту — 2,45 м",
    ])
    
    svg += footer_bar(2)
    svg += '</svg>'
    return svg


def generate_lesson_3():
    """Lesson 3: Спортивные игры: общая характеристика"""
    svg = svg_header()
    svg += bg_rect()
    svg += title_banner(0, "Спортивные игры: общая характеристика")
    
    # Classification diagram
    svg += f'''
  <rect x="260" y="78" width="280" height="44" fill="{PRIMARY}" rx="22"/>
  <text x="400" y="106" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="{WHITE}">Спортивные игры</text>'''
    
    # Two branches: team and individual
    svg += f'<line x1="330" y1="122" x2="200" y2="150" stroke="{PRIMARY_DARK}" stroke-width="2"/>'
    svg += f'<line x1="470" y1="122" x2="600" y2="150" stroke="{ACCENT}" stroke-width="2"/>'
    
    svg += f'''<rect x="100" y="150" width="200" height="36" fill="{PRIMARY_DARK}" rx="18"/>
  <text x="200" y="174" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{WHITE}">Командные</text>'''
    
    svg += f'''<rect x="500" y="150" width="200" height="36" fill="{ACCENT}" rx="18"/>
  <text x="600" y="174" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{WHITE}">Индивидуальные</text>'''
    
    # Team sports items
    team_sports = ["Футбол", "Баскетбол", "Волейбол", "Гандбол", "Хоккей", "Регби"]
    for i, sport in enumerate(team_sports):
        cx = 80 + (i % 3) * 80
        cy = 215 + (i // 3) * 60
        svg += icon_circle(cx, cy, 26, LIGHT_GREEN if i % 2 == 0 else MID_GREEN, sport)
    
    # Individual sports
    ind_sports = ["Теннис", "Бадминтон", "Наст. теннис", "Шахматы", "Дартс", "Бокс"]
    for i, sport in enumerate(ind_sports):
        cx = 480 + (i % 3) * 80
        cy = 215 + (i // 3) * 60
        svg += icon_circle(cx, cy, 26, LIGHT_RED if i % 2 == 0 else MID_RED, sport)
    
    # Common characteristics
    svg += subtitle_bar(330, "Общие характеристики спортивных игр")
    
    svg += info_box(20, 380, 245, 180, "Тактика и стратегия", [
        "• Распределение ролей",
        "• Взаимодействие игроков",
      "• Атакующие действия",
      "• Защитные действия",
      "• Стандартные позиции",
      "• Моментальное решение",
    ])
    svg += accent_box(282, 380, 245, 180, "Физические качества", [
      "• Быстрота реакции",
      "• Выносливость",
      "• Ловкость и координация",
      "• Скоростная сила",
      "• Гибкость",
      "• Точность движений",
    ])
    svg += info_box(543, 380, 245, 180, "Правила и судейство", [
      "• Регламент матча",
      "• Система очков",
      "• Штрафные санкции",
      "• Замены игроков",
      "• Тайм-ауты",
      "• Видео-повтор (VAR)",
    ])
    
    svg += footer_bar(3)
    svg += '</svg>'
    return svg


def generate_lesson_4():
    """Lesson 4: Футбол: техника и тактика"""
    svg = svg_header()
    svg += bg_rect()
    svg += title_banner(0, "Футбол: техника и тактика")
    
    # Football field diagram
    svg += f'''
  <rect x="40" y="80" width="340" height="220" fill="#4ADE80" stroke="{TEXT_DARK}" stroke-width="2" rx="4"/>
  <line x1="210" y1="80" x2="210" y2="300" stroke="{WHITE}" stroke-width="2"/>
  <circle cx="210" cy="190" r="35" fill="none" stroke="{WHITE}" stroke-width="2"/>
  <circle cx="210" cy="190" r="3" fill="{WHITE}"/>
  <!-- Penalty areas -->
  <rect x="40" y="135" width="60" height="110" fill="none" stroke="{WHITE}" stroke-width="2"/>
  <rect x="320" y="135" width="60" height="110" fill="none" stroke="{WHITE}" stroke-width="2"/>
  <!-- Goal areas -->
  <rect x="40" y="160" width="25" height="60" fill="none" stroke="{WHITE}" stroke-width="1.5"/>
  <rect x="355" y="160" width="25" height="60" fill="none" stroke="{WHITE}" stroke-width="1.5"/>
  <text x="210" y="72" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{TEXT_MED}">Схема футбольного поля</text>'''
    
    # Player positions on the field (4-4-2 formation)
    positions = [
        (100, 265, "ВР"),  # goalkeeper
        (100, 220, "ЦЗ"), (100, 160, "ЦЗ"),  # center backs
        (80, 245, "ЛЗ"), (120, 135, "ПЗ"),  # fullbacks
        (170, 220, "ЦП"), (170, 160, "ЦП"),  # center mids
        (140, 250, "ЛП"), (200, 130, "ПП"),  # wingers
        (250, 220, "ЦН"), (250, 160, "ЦН"),  # strikers
    ]
    for px, py, label in positions:
        svg += f'<circle cx="{px}" cy="{py}" r="10" fill="{PRIMARY_DARK}" opacity="0.8"/>'
        svg += f'<text x="{px}" y="{py+4}" text-anchor="middle" font-family="Arial, sans-serif" font-size="8" fill="{WHITE}" font-weight="bold">{label}</text>'
    
    # Technique section
    svg += info_box(410, 80, 370, 130, "Техника владения мячом", [
      "• Ведение мяча (дриблинг)",
      "• Приём мяча (остановка)",
      "• Передача (пас) — короткий, длинный",
      "• Удар по мячу — внутренней стороной, подъёмом",
    ])
    svg += accent_box(410, 220, 370, 130, "Тактические схемы", [
      "• 4-4-2 — классическая расстановка",
      "• 4-3-3 — атакующий футбол",
      "• 3-5-2 — контроль центра",
      "• Прессинг и контратака",
    ])
    
    # Rules box
    svg += subtitle_bar(360, "Основные правила")
    svg += info_box(20, 410, 245, 140, "Размеры и время", [
      "• Поле: 90-120 х 45-90 м",
      "• Матч: 2 тайма по 45 мин",
      "• Состав: 11 игроков",
      "• Замены: до 5 за матч",
      "• Офсайд — вне игры",
      "• Пенальти — 11 м",
    ])
    svg += accent_box(282, 410, 245, 140, "Нарушения и штрафы", [
      "• Жёлтая карточка — предупреждение",
      "• Красная карточка — удаление",
      "• Штрафной удар (прямой/непрямой)",
      "• Угловой удар",
      "• Свободный удар",
      "• Пенальти за фол в штрафной",
    ])
    svg += info_box(543, 410, 245, 140, "Кубки и турниры", [
      "• Чемпионат мира (FIFA)",
      "• Лига чемпионов УЕФА",
      "• Евро (чемпионат Европы)",
      "• РФПЛ — чемпионат России",
      "• Кубок России",
      "• Олимпийский турнир",
    ])
    
    svg += footer_bar(4)
    svg += '</svg>'
    return svg


def generate_lesson_5():
    """Lesson 5: Баскетбол: техника и тактика"""
    svg = svg_header()
    svg += bg_rect()
    svg += title_banner(0, "Баскетбол: техника и тактика")
    
    # Basketball court diagram
    svg += f'''
  <rect x="40" y="80" width="340" height="220" fill="#F59E0B" stroke="{TEXT_DARK}" stroke-width="2" rx="4" opacity="0.3"/>
  <rect x="40" y="80" width="340" height="220" fill="none" stroke="{TEXT_DARK}" stroke-width="2" rx="4"/>
  <line x1="210" y1="80" x2="210" y2="300" stroke="{TEXT_DARK}" stroke-width="2"/>
  <circle cx="210" cy="190" r="30" fill="none" stroke="{TEXT_DARK}" stroke-width="2"/>
  <!-- 3-point arcs -->
  <path d="M 40,140 Q 120,80 210,120 Q 300,80 380,140" fill="none" stroke="{TEXT_DARK}" stroke-width="1.5"/>
  <path d="M 40,240 Q 120,300 210,260 Q 300,300 380,240" fill="none" stroke="{TEXT_DARK}" stroke-width="1.5"/>
  <!-- Baskets -->
  <rect x="36" y="178" width="8" height="24" fill="{ACCENT}" stroke="{TEXT_DARK}" stroke-width="1"/>
  <rect x="376" y="178" width="8" height="24" fill="{ACCENT}" stroke="{TEXT_DARK}" stroke-width="1"/>
  <!-- Free throw lines -->
  <rect x="48" y="162" width="50" height="56" fill="none" stroke="{TEXT_DARK}" stroke-width="1.5"/>
  <rect x="322" y="162" width="50" height="56" fill="none" stroke="{TEXT_DARK}" stroke-width="1.5"/>
  <text x="210" y="72" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{TEXT_MED}">Схема баскетбольной площадки</text>'''
    
    # Player positions on court (5 players)
    bball_positions = [
        (70, 190, "РЗ"),   # point guard
        (150, 130, "АЗ"),  # shooting guard
        (150, 250, "ЛФ"),  # small forward
        (250, 130, "ТФ"),  # power forward
        (300, 190, "Ц"),   # center
    ]
    for px, py, label in bball_positions:
        svg += f'<circle cx="{px}" cy="{py}" r="12" fill="{PRIMARY_DARK}" opacity="0.85"/>'
        svg += f'<text x="{px}" y="{py+4}" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="{WHITE}" font-weight="bold">{label}</text>'
    
    # Technique box
    svg += info_box(410, 80, 370, 130, "Техника игры", [
      "• Ведение мяча (дриблинг)",
      "• Передача — двумя руками от груди",
      "• Бросок — двухтактный, трёхочковый",
      "• Подбор мяча (ребаунд)",
    ])
    svg += accent_box(410, 220, 370, 130, "Тактика игры", [
      "• Пик-н-ролл (заслон + проход)",
      "• Изоляция (1 на 1)",
      "• Быстрый отрыв (фаст-брейк)",
      "• Зонная защита (2-3, 3-2)",
    ])
    
    # Rules
    svg += subtitle_bar(360, "Основные правила")
    svg += info_box(20, 410, 245, 140, "Размеры и время", [
      "• Площадка: 28 х 15 м",
      "• Кольцо: 3,05 м высота",
      "• Матч: 4 четверти по 10 мин",
      "• Состав: 5 на площадке",
      "• 24 сек — время на атаку",
      "• 3 сек — в штрафной зоне",
    ])
    svg += accent_box(282, 410, 245, 140, "Нарушения", [
      "• Пробежка — более 2 шагов",
      "• Двойное ведение",
      "• Нарушение 3/5/24 секунд",
      "• Фол — толчок, блок",
      "• Технический фол",
      "• Дисквалифицирующий фол",
    ])
    svg += info_box(543, 410, 245, 140, "Знаменитые лиги", [
      "• NBA — США (лучшие игроки)",
      "• Евролига — лучший в Европе",
      "• Единная лига ВТБ — Россия",
      "• Чемпионат мира ФИБА",
      "• Олимпийский турнир",
      "• Джеймс, Джордан, Коби",
    ])
    
    svg += footer_bar(5)
    svg += '</svg>'
    return svg


def generate_lesson_6():
    """Lesson 6: Волейбол: техника и тактика"""
    svg = svg_header()
    svg += bg_rect()
    svg += title_banner(0, "Волейбол: техника и тактика")
    
    # Volleyball court diagram
    svg += f'''
  <rect x="60" y="80" width="300" height="230" fill="#93C5FD" stroke="{TEXT_DARK}" stroke-width="2" rx="4" opacity="0.3"/>
  <rect x="60" y="80" width="300" height="230" fill="none" stroke="{TEXT_DARK}" stroke-width="2" rx="4"/>
  <line x1="60" y1="195" x2="360" y2="195" stroke="{ACCENT}" stroke-width="3"/>
  <line x1="210" y1="80" x2="210" y2="310" stroke="{TEXT_DARK}" stroke-width="1" stroke-dasharray="6,3"/>
  <!-- Net representation -->
  <rect x="56" y="185" width="308" height="3" fill="{ACCENT_DARK}"/>
  <text x="210" y="182" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{ACCENT_DARK}" font-weight="bold">СЕТКА (2,43 м муж / 2,24 м жен)</text>
  <text x="210" y="72" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{TEXT_MED}">Схема волейбольной площадки</text>'''
    
    # Player positions - Team 1 (bottom half)
    team1 = [(110, 280), (170, 280), (230, 280), (290, 280), (350, 280), (130, 240)]
    labels1 = ["1", "2", "3", "4", "5", "6"]
    for i, ((px, py), lbl) in enumerate(zip(team1, labels1)):
        svg += f'<circle cx="{px}" cy="{py}" r="11" fill="{PRIMARY_DARK}" opacity="0.85"/>'
        svg += f'<text x="{px}" y="{py+4}" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="{WHITE}" font-weight="bold">{lbl}</text>'
    
    # Player positions - Team 2 (top half)
    team2 = [(110, 110), (170, 110), (230, 110), (290, 110), (350, 110), (130, 150)]
    for i, (px, py) in enumerate(team2):
        svg += f'<circle cx="{px}" cy="{py}" r="11" fill="{ACCENT_DARK}" opacity="0.85"/>'
        svg += f'<text x="{px}" y="{py+4}" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="{WHITE}" font-weight="bold">{i+1}</text>'
    
    # Technique section
    svg += info_box(400, 80, 380, 140, "Техника волейбола", [
      "• Нижняя передача (приём мяча снизу)",
      "• Верхняя передача (двумя руками сверху)",
      "• Нападающий удар (прямым ходом)",
      "• Подача — нижняя, верхняя, планер",
      "• Блок — одиночный, групповой",
    ])
    svg += accent_box(400, 230, 380, 110, "Тактика и расстановка", [
      "• Расстановка 5-1 (1 связующий)",
      "• Расстановка 4-2 (2 связующих)",
      "• Переход (ротация) по часовой стрелке",
      "• Либеро — игрок задней линии",
    ])
    
    # Rules
    svg += subtitle_bar(350, "Основные правила")
    svg += info_box(20, 400, 245, 150, "Размеры и счёт", [
      "• Площадка: 18 х 9 м",
      "• Партия до 25 очков (преимущ. +2)",
      "• 5 партий (до 3 побед)",
      "• 5-я партия до 15 очков",
      "• 3 касания на атаку (блок не сч.)",
      "• Состав: 6 на площадке",
      "• 7 запасных игроков",
    ])
    svg += accent_box(282, 400, 245, 150, "Нарушения", [
      "• Касание сетки игроком",
      "• Заступ на чужую половину",
      "• Двойное касание",
      "• Задержка мяча (бросок)",
      "• 4 касания команды",
      "• Ошибка расстановки",
      "• Нарушение при подаче",
    ])
    svg += info_box(543, 400, 245, 150, "Турниры", [
      "• Волейбольная Лига Наций",
      "• Чемпионат мира FIVB",
      "• Олимпийские игры",
      "• Суперлига — Россия",
      "• Лига чемпионов CEV",
      "• Кубок ЕКВ",
      "• Мировой Гран-при",
    ])
    
    svg += footer_bar(6)
    svg += '</svg>'
    return svg


def generate_lesson_7():
    """Lesson 7: Плавание: способы и техника"""
    svg = svg_header()
    svg += bg_rect()
    svg += title_banner(0, "Плавание: способы и техника")
    
    # Swimming pool lanes
    svg += f'''
  <rect x="20" y="78" width="380" height="240" fill="#BFDBFE" stroke="{TEXT_DARK}" stroke-width="2" rx="6"/>
  <text x="210" y="72" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{TEXT_MED}">Бассейн: 50 м, 8 дорожек</text>'''
    # Lanes
    for i in range(8):
        ly = 95 + i * 28
        svg += f'<line x1="25" y1="{ly}" x2="395" y2="{ly}" stroke="{WHITE}" stroke-width="1.5"/>'
    
    # Swimmers in different styles
    svg += stickman(80, 115, 0.9, TEXT_DARK, "swimming")
    svg += stickman(80, 171, 0.9, TEXT_DARK, "swimming")
    svg += stickman(80, 227, 0.9, TEXT_DARK, "swimming")
    svg += stickman(80, 283, 0.9, TEXT_DARK, "swimming")
    
    # Style labels
    svg += f'<text x="210" y="118" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{PRIMARY_DARK}" font-weight="bold">Кроль на груди (вольный стиль)</text>'
    svg += f'<text x="210" y="174" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{ACCENT_DARK}" font-weight="bold">Брасс</text>'
    svg += f'<text x="210" y="230" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{PRIMARY_DARK}" font-weight="bold">Баттерфляй</text>'
    svg += f'<text x="210" y="286" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{ACCENT_DARK}" font-weight="bold">Кроль на спине</text>'
    
    # Swimming styles details
    svg += info_box(420, 78, 360, 95, "Кроль (вольный стиль)", [
      "• Самый быстрый способ плавания",
      "• Попеременная работа рук и ног",
      "• Ноги — непрерывный удар вверх-вниз",
      "• Дыхание — поворот головы в сторону",
    ])
    svg += accent_box(420, 183, 360, 75, "Брасс", [
      "• Одновременная работа рук и ног",
      "• «Лягушачьи» движения ногами",
      "• Дыхание — подъём головы над водой",
    ])
    svg += info_box(420, 268, 360, 60, "Баттерфляй (дельфин)", [
      "• Самый сложный и энергозатратный стиль",
      "• Одновременный гребок обеими руками",
    ])
    
    # Safety and technique tips
    svg += subtitle_bar(340, "Техника безопасности и советы")
    svg += info_box(20, 390, 250, 150, "Правила безопасности", [
      "• Разминка перед заплывом",
      "• Не плавать на полный желудок",
      "• Соблюдать дистанцию между",
      "  пловцами на дорожках",
      "• Не прыгать на мелководье",
      "• Использовать шапочку и очки",
      "• Не заплывать за буйки",
    ])
    svg += accent_box(285, 390, 250, 150, "Олимпийские дистанции", [
      "• 50 м вольный стиль (спринт)",
      "• 100 м — все стили",
      "• 200 м — все стили",
      "• 400 м вольный стиль",
      "• 1500 м вольный стиль",
      "• Эстафеты 4х100, 4х200",
      "• Комплексное плавание",
    ])
    svg += info_box(550, 390, 230, 150, "Знаменитые пловцы", [
      "• М. Фелпс — 23 олимп. золота",
      "• К. Ледецки — королева的水",
      "• А. Попов — легенда спринта",
      "• Л. Клебер — брасс",
      "• Ю. Прилуцкий — Россия",
      "• Рекорд 100м кр: 46,86 с",
      "• Рекорд 200м батт: 1:50,3",
    ])
    
    svg += footer_bar(7)
    svg += '</svg>'
    return svg


def generate_lesson_8():
    """Lesson 8: Лыжная подготовка: ходы и техника"""
    svg = svg_header()
    svg += bg_rect()
    svg += title_banner(0, "Лыжная подготовка: ходы и техника")
    
    # Ski tracks diagram
    svg += f'''
  <rect x="20" y="80" width="760" height="130" fill="#E0F2FE" stroke="{TEXT_DARK}" stroke-width="1" rx="6"/>
  <text x="400" y="96" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{TEXT_MED}">Лыжня — классический и коньковый ход</text>'''
    
    # Classic tracks (two parallel lines)
    svg += f'<line x1="40" y1="130" x2="760" y2="130" stroke="{PRIMARY_DARK}" stroke-width="2" stroke-dasharray="12,4"/>'
    svg += f'<line x1="40" y1="150" x2="760" y2="150" stroke="{PRIMARY_DARK}" stroke-width="2" stroke-dasharray="12,4"/>'
    svg += f'<text x="60" y="122" font-family="Arial, sans-serif" font-size="10" fill="{PRIMARY_DARK}">Классическая лыжня</text>'
    
    # Skating tracks (V-shape pattern)
    for x in range(80, 740, 40):
        svg += f'<line x1="{x}" y1="170" x2="{x+20}" y2="195" stroke="{ACCENT}" stroke-width="2"/>'
        svg += f'<line x1="{x+20}" y1="195" x2="{x+40}" y2="170" stroke="{ACCENT}" stroke-width="2"/>'
    svg += f'<text x="60" y="172" font-family="Arial, sans-serif" font-size="10" fill="{ACCENT}">Коньковый ход (V-образный)</text>'
    
    # Stickman on skis
    svg += stickman(200, 148, 0.8, PRIMARY_DARK, "running")
    svg += stickman(500, 170, 0.8, ACCENT_DARK, "running")
    
    # Types of ski techniques
    svg += info_box(20, 225, 245, 165, "Классические ходы", [
      "• Попеременный двухшажный",
      "• Одновременный бесшажный",
      "• Одновременный одношажный",
      "• Одновременный двухшажный",
      "• Полуконьковый ход",
      "",
      "Отталкивание ногой назад",
      "  по классической лыжне",
    ])
    svg += accent_box(280, 225, 245, 165, "Коньковые ходы", [
      "• Коньковый без палок",
      "• Коньковый одновременный",
      "• Коньковый двухшажный",
      "• Полуконьковый",
      "",
      "Отталкивание ребром лыжи",
      "  V-образное скольжение",
      "  Скорость выше классики",
    ])
    svg += info_box(540, 225, 240, 165, "Спуски и подъёмы", [
      "• Спуск в основной стойке",
      "• Спуск в высокой стойке",
      "• Спуск в низкой стойке",
      "• Подъём «лесенкой»",
      "• Подъём «ёлочкой»",
      "• Подъём «полуёлочкой»",
      "",
      "Торможение: плугом, упором",
    ])
    
    # Equipment and safety
    svg += subtitle_bar(400, "Инвентарь и безопасность")
    svg += info_box(20, 440, 245, 110, "Лыжный инвентарь", [
      "• Беговые лыжи (классические)",
      "• Коньковые лыжи (короче)",
      "• Лыжные палки (до подмышки)",
      "• Лыжные ботинки",
      "• Крепления (NNN, SNS)",
      "• Смазка (мазь держания/скольж.)",
    ])
    svg += accent_box(282, 440, 245, 110, "Безопасность на лыжне", [
      "• Разминка перед выходом на снег",
      "• Соответствующая одежда",
      "• Соблюдать дистанцию",
      "• Не пересекать чужую лыжню",
      "• Спуск по своей дорожке",
      "• Осторожно на спусках и поворотах",
    ])
    svg += info_box(543, 440, 240, 110, "Соревнования", [
      "• Спринт (1,5 км)",
      "• Гонка преследования (пурсьют)",
      "• Индивидуальная гонка (10/15 км)",
      "• Марафон (50 км)",
      "• Эстафета 4х5 / 4х10 км",
      "• Тур де Ски — многодневка",
    ])
    
    svg += footer_bar(8)
    svg += '</svg>'
    return svg


def generate_lesson_9():
    """Lesson 9: Физическая подготовка и её виды"""
    svg = svg_header()
    svg += bg_rect()
    svg += title_banner(0, "Физическая подготовка и её виды")
    
    # Central hub-and-spoke diagram for physical qualities
    svg += f'''
  <circle cx="400" cy="220" r="50" fill="{PRIMARY}" stroke="{PRIMARY_DARK}" stroke-width="3"/>
  <text x="400" y="215" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="{WHITE}">Физические</text>
  <text x="400" y="230" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="{WHITE}">качества</text>'''
    
    # Four qualities radiating out
    qualities = [
        (170, 120, "Сила", PRIMARY_DARK, LIGHT_GREEN),
        (630, 120, "Быстрота", ACCENT, LIGHT_RED),
        (170, 320, "Выносливость", ACCENT_DARK, LIGHT_RED),
        (630, 320, "Гибкость", PRIMARY, LIGHT_GREEN),
    ]
    for qx, qy, label, color, bg_color in qualities:
        svg += f'<line x1="400" y1="220" x2="{qx}" y2="{qy}" stroke="{color}" stroke-width="2"/>'
        svg += f'<circle cx="{qx}" cy="{qy}" r="38" fill="{bg_color}" stroke="{color}" stroke-width="3"/>'
        svg += f'<text x="{qx}" y="{qy+5}" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{color}">{label}</text>'
    
    # Detailed boxes for each quality
    svg += info_box(20, 380, 185, 170, "Сила", [
      "• Способность преодолевать",
      "  внешнее сопротивление",
      "• Упражнения с отягощ.",
      "• Отжимания, подтягив.",
      "• Приседания со штангой",
      "• 3-5 подходов по 8-12 раз",
    ])
    svg += accent_box(215, 380, 185, 170, "Быстрота", [
      "• Способность выполнять",
      "  движения за мин. время",
      "• Бег на короткие дистанции",
      "• Челночный бег 3х10 м",
      "• Быстрые изменения напр.",
      "• Интервальная тренировка",
    ])
    svg += info_box(410, 380, 185, 170, "Выносливость", [
      "• Способность длительно",
      "  выполнять работу",
      "• Бег на длинные дистанции",
      "• Плавание, велоспорт",
      "• Кросс по пересечён. местн.",
      "• Пульс 130-150 уд/мин",
    ])
    svg += accent_box(600, 380, 180, 170, "Гибкость", [
      "• Способность выполнять",
      "  движения с большой ампл.",
      "• Растяжка, шпагат, мостик",
      "• Наклоны вперёд/назад",
      "• Упражнения на растяжку",
      "• 15-30 сек на каждое",
    ])
    
    # Additional info
    svg += f'''<rect x="20" y="80" width="100" height="24" fill="{PRIMARY_DARK}" rx="12"/>
  <text x="70" y="96" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{WHITE}" font-weight="bold">Общая физ.подг.</text>'''
    svg += f'''<rect x="680" y="80" width="100" height="24" fill="{ACCENT}" rx="12"/>
  <text x="730" y="96" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{WHITE}" font-weight="bold">Специальная</text>'''
    
    svg += footer_bar(9)
    svg += '</svg>'
    return svg


def generate_lesson_10():
    """Lesson 10: Здоровый образ жизни и его компоненты"""
    svg = svg_header()
    svg += bg_rect()
    svg += title_banner(0, "Здоровый образ жизни и его компоненты")
    
    # Central circle — ЗОЖ
    svg += f'''
  <circle cx="400" cy="200" r="55" fill="{PRIMARY}" stroke="{PRIMARY_DARK}" stroke-width="3"/>
  <text x="400" y="193" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{WHITE}">Здоровый</text>
  <text x="400" y="210" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="{WHITE}">образ жизни</text>'''
    
    # Four components
    components = [
        (130, 130, "Питание", PRIMARY_DARK, "🥗"),
        (670, 130, "Движение", ACCENT, "🏃"),
        (130, 280, "Сон/Отдых", ACCENT_DARK, "😴"),
        (670, 280, "Гигиена", PRIMARY, "🧼"),
    ]
    for cx, cy, label, color, emoji in components:
        svg += f'<line x1="400" y1="200" x2="{cx}" y2="{cy}" stroke="{color}" stroke-width="2" stroke-dasharray="6,3"/>'
        svg += f'<circle cx="{cx}" cy="{cy}" r="35" fill="{color}" opacity="0.15" stroke="{color}" stroke-width="2"/>'
        svg += f'<text x="{cx}" y="{cy+5}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="{color}">{label}</text>'
    
    # Detailed boxes
    svg += info_box(20, 340, 185, 210, "Рациональное питание", [
      "• 3-5 приёмов пищи в день",
      "• Белки, жиры, углеводы",
      "• Витамины и минералы",
      "• 1,5-2 л воды в день",
      "• Овощи и фрукты",
      "• Ограничить сахар и соль",
      "• Не переедать перед сном",
      "• Завтрак — обязательный приём",
    ])
    svg += accent_box(215, 340, 185, 210, "Физическая активность", [
      "• 60 мин активности в день",
      "• Утренняя гимнастика",
      "• Спортивные секции 3 р/нед",
      "• Прогулки на свежем воздухе",
      "• Подвижные игры",
      "• Чередование труда и отдыха",
      "• Отказ от лифта — лестница",
      "• Растяжка и разминка",
    ])
    svg += info_box(410, 340, 185, 210, "Сон и отдых", [
      "• 8-10 часов сна (подростки)",
      "• Ложиться до 22:00",
      "• Проветривание спальни",
      "• Отказ от экранов перед сном",
      "• Активный отдых на природе",
      "• Чередование умственной и",
      "  физической нагрузки",
      "• Выходные без гаджетов",
    ])
    svg += accent_box(600, 340, 185, 210, "Личная гигиена", [
      "• Ежедневный душ",
      "• Чистка зубов 2 раза/день",
      "• Смена нательного белья",
      "• Мытьё рук перед едой",
      "• Уход за ногтями и волосами",
      "• Проветривание помещения",
      "• Уборка рабочего места",
      "• Спортивная форма — чистая",
    ])
    
    svg += footer_bar(10)
    svg += '</svg>'
    return svg


def generate_lesson_11():
    """Lesson 11: Профилактика травм на занятиях физкультурой"""
    svg = svg_header()
    svg += bg_rect()
    svg += title_banner(0, "Профилактика травм на занятиях физкультурой")
    
    # Warning triangle
    svg += f'''
  <polygon points="400,90 340,175 460,175" fill="none" stroke="{ACCENT}" stroke-width="4" stroke-linejoin="round"/>
  <text x="400" y="165" text-anchor="middle" font-family="Arial, sans-serif" font-size="48" font-weight="bold" fill="{ACCENT}">!</text>
  <text x="400" y="195" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{ACCENT_DARK}" font-weight="bold">ВНИМАНИЕ: БЕЗОПАСНОСТЬ ПРЕЖДЕ ВСЕГО</text>'''
    
    # Main categories in 3 columns
    svg += info_box(20, 210, 245, 185, "Разминка и подготовка", [
      "• Обязательная разминка (10-15 мин)",
      "• Разогрев всех групп мышц",
      "• Растяжка после разминки",
      "• Постепенное увеличение нагрузки",
      "• Проверка инвентаря перед занятием",
      "• Удобная спортивная форма и обувь",
      "• Снятие украшений и часов",
      "• Волосы собраны (для девочек)",
    ])
    svg += accent_box(280, 210, 245, 185, "Правильная техника", [
      "• Соблюдать технику выполнения",
      "• Не выполнять сложные элементы",
      "  без подготовки",
      "• Следовать указаниям учителя",
      "• Соблюдать дистанцию между",
      "  учащимися",
      "• Правильное приземление",
      "  (на две ноги, амортизация)",
      "• Не толкаться и не подножки",
    ])
    svg += info_box(540, 210, 240, 185, "Инвентарь и среда", [
      "• Исправный спортивный инвентарь",
      "• Чистый и сухой спортивный зал",
      "• Маты под снарядами",
      "• Проверка креплений (лыжи)",
      "• Безопасная зона вокруг",
      "  гимнастических снарядов",
      "• Ограждение зоны бросков",
      "• Температура в зале 16-18 C",
    ])
    
    # Common injuries section
    svg += subtitle_bar(405, "Типичные травмы и первая помощь")
    svg += info_box(20, 450, 245, 110, "Типичные травмы", [
      "• Растяжение связок и мышц",
      "• Ушибы и ссадины",
      "• Вывихи суставов",
      "• Переломы (редко)",
      "• Потёртости и мозоли",
    ])
    svg += accent_box(282, 450, 245, 110, "Первая помощь (R.I.C.E.)", [
      "R — Rest (покой)",
      "I — Ice (лёд на 15-20 мин)",
      "C — Compression (тугая повязка)",
      "E — Elevation (поднять конечность)",
      "Обязательно — обратиться к врачу!",
    ])
    svg += info_box(543, 450, 240, 110, "Профилактика", [
      "• Регулярные медосмотры",
      "• Учёт состояния здоровья",
      "• Ограничения по заболеваниям",
      "• Страховка при выполнении",
      "  сложных элементов",
    ])
    
    svg += footer_bar(11)
    svg += '</svg>'
    return svg


def generate_lesson_12():
    """Lesson 12: Олимпийское движение: история и современность"""
    svg = svg_header()
    svg += bg_rect()
    svg += title_banner(0, "Олимпийское движение: история и современность")
    
    # Olympic rings
    rings_data = [
        (240, 120, "#0081C8"),  # blue
        (310, 120, "#000000"),  # black
        (380, 120, "#EE334E"),  # red
        (275, 145, "#FCB131"),  # yellow
        (345, 145, "#00A651"),  # green
    ]
    for cx, cy, color in rings_data:
        svg += f'<circle cx="{cx}" cy="{cy}" r="25" fill="none" stroke="{color}" stroke-width="4"/>'
    
    svg += f'<text x="310" y="185" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" fill="{TEXT_MED}">Citius, Altius, Fortius — Быстрее, Выше, Сильнее</text>'
    
    # Two columns: Ancient and Modern
    svg += info_box(20, 200, 375, 170, "Древние Олимпийские игры", [
      "• Первые игры — 776 г. до н.э., Олимпия (Греция)",
      "• Проводились в честь бога Зевса",
      "• Длились 5 дней, каждые 4 года",
      "• Виды: бег, панкратион, пятиборье,",
      "  борьба, гонки на колесницах",
      "• Участники — только свободные греки-мужчины",
      "• Священное перемирие (экехейрия)",
      "• Запрещены в 394 г. н.э. (имп. Феодосий)",
    ])
    svg += accent_box(410, 200, 370, 170, "Современные Олимпийские игры", [
      "• Возрождены Пьером де Кубертеном (1896)",
      "• I Олимпиада — Афины, 1896 г.",
      "• Зимние Олимпийские игры — с 1924 г.",
      "• Паралимпийские игры — с 1960 г.",
      "• Проводятся каждые 4 года",
      "• Олимпийская хартия — основной документ",
      "• МОК — Международный олимпийский комитет",
      "• Россия на Олимпиадах с 1900 г.",
    ])
    
    # Timeline
    svg += subtitle_bar(380, "Хронология олимпийского движения")
    # Timeline line
    svg += f'<line x1="40" y1="435" x2="760" y2="435" stroke="{PRIMARY}" stroke-width="3"/>'
    
    events = [
        (80, "776 до н.э.", "Первые игры"),
        (230, "1896", "Афины, I Олимпиада"),
        (380, "1924", "Зимние игры"),
        (530, "1980", "Москва, XXII Олимпиада"),
        (680, "2024", "Париж, XXXIII Олимпиада"),
    ]
    for ex, year, desc in events:
        svg += f'<circle cx="{ex}" cy="435" r="6" fill="{ACCENT}"/>'
        svg += f'<text x="{ex}" y="425" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{PRIMARY_DARK}" font-weight="bold">{year}</text>'
        svg += f'<text x="{ex}" y="455" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="{TEXT_MED}">{desc}</text>'
    
    # Russia highlights
    svg += info_box(20, 475, 375, 80, "Олимпийские чемпионы России", [
      "• А. Карелин (борьба) — 3-кратный олимпийский чемпион",
      "• Л. Егорова (лыжи) — 6 золотых медалей",
      "• С. Хоркина (гимнастика) — 2 золота",
    ])
    svg += accent_box(410, 475, 370, 80, "Ценности олимпизма", [
      "• Дружба, солидарность, честная игра",
      "• Спорт как средство мира и взаимопонимания",
      "• Ни расы, ни религии — только талант!",
    ])
    
    svg += footer_bar(12)
    svg += '</svg>'
    return svg


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    generators = [
        generate_lesson_1,
        generate_lesson_2,
        generate_lesson_3,
        generate_lesson_4,
        generate_lesson_5,
        generate_lesson_6,
        generate_lesson_7,
        generate_lesson_8,
        generate_lesson_9,
        generate_lesson_10,
        generate_lesson_11,
        generate_lesson_12,
    ]
    
    results = []
    for i, gen in enumerate(generators, 1):
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{i}.svg")
        try:
            svg_content = gen()
            # Validate with xml.etree.ElementTree
            ET.fromstring(svg_content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(svg_content)
            file_size = os.path.getsize(filepath)
            results.append(f"  ✅ lesson-{i}.svg — valid XML, {file_size} bytes")
        except ET.ParseError as e:
            results.append(f"  ❌ lesson-{i}.svg — XML PARSE ERROR: {e}")
        except Exception as e:
            results.append(f"  ❌ lesson-{i}.svg — ERROR: {e}")
    
    # Final validation pass
    print("=" * 60)
    print("Grade 8 PE (Физкультура/ОБЖ) SVG Generation Report")
    print("=" * 60)
    print()
    for r in results:
        print(r)
    print()
    
    # Count successes
    success_count = sum(1 for r in results if "✅" in r)
    print(f"Result: {success_count}/{len(generators)} SVGs generated and validated successfully")
    
    # Verify all files exist
    print("\nFile verification:")
    for i in range(1, 13):
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{i}.svg")
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            print(f"  lesson-{i}.svg — exists ({size} bytes)")
        else:
            print(f"  lesson-{i}.svg — MISSING!")


if __name__ == "__main__":
    main()
