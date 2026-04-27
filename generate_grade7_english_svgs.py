#!/usr/bin/env python3
"""Generate Grade 7 English Language SVG lesson images."""

import os
import xml.etree.ElementTree as ET

OUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/english"
os.makedirs(OUT_DIR, exist_ok=True)

BLUE = "#3B82F6"
RED = "#DC2626"
DARK = "#1E3A5F"
GRAY = "#6B7280"
LIGHT_BLUE = "#DBEAFE"
LIGHT_RED = "#FEE2E2"
YELLOW_BG = "#FEF9C3"
WHITE = "#FFFFFF"
BG = "#F3F4F6"
HEADER_DARK = "#1E3A5F"
BORDER = "#CBD5E1"


def escape(text):
    """Escape XML special characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def svg_start(title_ru, title_en, lesson_num, total=6):
    """Return opening SVG string with header."""
    return f'''<?xml version='1.0' encoding='utf-8'?>
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">
<defs><marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="{BLUE}" /></marker></defs>
<rect width="800" height="600" fill="{BG}" rx="0" />
<rect x="0" y="0" width="800" height="70" fill="{BLUE}" />
<text x="400" y="32" text-anchor="middle" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="{WHITE}">{escape(title_en)}</text>
<text x="400" y="56" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="#BFDBFE">{escape(title_ru)}</text>
<rect x="0" y="70" width="800" height="3" fill="{RED}" />'''


def svg_end(lesson_num, total=6):
    """Return closing SVG string with footer."""
    return f'''<rect x="0" y="570" width="800" height="30" fill="{HEADER_DARK}" />
<text x="20" y="590" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="#94A3B8">Grade 7 | English | Lesson {lesson_num}</text>
<text x="780" y="590" text-anchor="end" font-family="Arial, sans-serif" font-size="11" fill="#94A3B8">Lesson {lesson_num}/{total}</text>
</svg>'''


def section_title(y, title):
    return f'''<text x="20" y="{y}" text-anchor="start" font-family="Arial, sans-serif" font-size="15" fill="{BLUE}" font-weight="bold">{escape(title)}</text>
<line x1="20" y1="{y+3}" x2="{20+len(title)*8}" y2="{y+3}" stroke="{BLUE}" stroke-width="1.5" />'''


def formula_box(x, y, w, h, parts):
    """A yellow box with colored text parts. parts = [(text, color), ...]"""
    tspans = "".join(f'<tspan fill="{c}">{escape(t)}</tspan>' for t, c in parts)
    return f'''<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{YELLOW_BG}" stroke="{BLUE}" stroke-width="2" rx="6" />
<text x="{x+w//2}" y="{y+h//2+5}" text-anchor="middle" font-family="Arial, sans-serif" font-size="15" font-weight="bold">{tspans}</text>'''


def rule_box(x, y, w, h, num, title, detail):
    """Red-bordered rule box with circle number."""
    cx = x + 18
    cy = y + 18
    return f'''<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{LIGHT_RED}" stroke="{RED}" stroke-width="2" rx="6" />
<circle cx="{cx}" cy="{cy}" r="12" fill="{RED}" />
<text x="{cx}" y="{cy+5}" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="{WHITE}" font-weight="bold">{num}</text>
<text x="{cx+20}" y="{cy+4}" text-anchor="start" font-family="Arial, sans-serif" font-size="13" fill="{RED}" font-weight="bold">{escape(title)}</text>
<text x="{x+14}" y="{y+h-8}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="#1F2937">{escape(detail)}</text>'''


def pill(x, y, w, h, text, fill=LIGHT_BLUE, stroke=BLUE, text_color=DARK):
    """Pill-shaped label."""
    return f'''<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="1" rx="12" />
<text x="{x+w//2}" y="{y+h//2+4}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{text_color}" font-weight="bold">{escape(text)}</text>'''


def table_header(y, cols, widths, start_x=20):
    """Draw table header row. cols = [(text, width), ...]"""
    total_w = sum(widths)
    parts = [f'<rect x="{start_x}" y="{y}" width="{total_w}" height="28" fill="{BLUE}" stroke="{BLUE}" stroke-width="2" rx="0" />']
    cx = start_x
    for (text, w) in zip(cols, widths):
        parts.append(f'<text x="{cx + w//2}" y="{y+19}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{WHITE}" font-weight="bold">{escape(text)}</text>')
        cx += w
    return "\n".join(parts)


def table_row(y, cols, widths, start_x=20, alt=False):
    """Draw table data row."""
    total_w = sum(widths)
    bg = LIGHT_BLUE if alt else WHITE
    parts = [f'<rect x="{start_x}" y="{y}" width="{total_w}" height="28" fill="{bg}" stroke="{BORDER}" stroke-width="1" rx="0" />']
    cx = start_x
    for (text, w) in zip(cols, widths):
        parts.append(f'<text x="{cx+10}" y="{y+19}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="#1F2937">{escape(text)}</text>')
        cx += w
    return "\n".join(parts)


def example_item(x, y, num, en_text, ru_text):
    """Numbered example with English and Russian translation."""
    return f'''<circle cx="{x+10}" cy="{y}" r="9" fill="{BLUE}" />
<text x="{x+10}" y="{y+4}" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{WHITE}" font-weight="bold">{num}</text>
<text x="{x+26}" y="{y+4}" text-anchor="start" font-family="Arial, sans-serif" font-size="13" fill="{DARK}">{escape(en_text)}</text>
<text x="{x+26}" y="{y+18}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{GRAY}">{escape(ru_text)}</text>'''


# ============================================================
# LESSON 1: Daily Routines and Habits
# ============================================================
def lesson1():
    s = svg_start("Повседневные привычки и рутины", "Daily Routines and Habits", 1)
    y = 90

    # Formation
    s += section_title(y, "Present Simple / Настоящее простое время")
    y += 18
    s += formula_box(20, y, 355, 36, [("S + V", RED), (" (", GRAY), ("V/Vs/es", BLUE), (") + ...", GRAY)])
    s += formula_box(390, y, 380, 36, [("S + ", RED), ("don't/doesn't", RED), (" + V", BLUE), (" + ...", GRAY)])
    y += 44
    s += formula_box(20, y, 750, 36, [("Do/Does", RED), (" + S + ", RED), ("V", BLUE), (" + ... ?", GRAY)])
    y += 50

    # Time markers
    s += section_title(y, "Маркеры времени / Time Expressions")
    y += 18
    markers = ["always", "usually", "often", "sometimes", "rarely", "never", "every day", "on weekdays"]
    for i, m in enumerate(markers):
        col = i % 4
        row = i // 4
        px = 20 + col * 195
        py = y + row * 32
        s += pill(px, py, 180, 24, m)
    y += 75

    # Rules
    s += section_title(y, "Правила / Rules")
    y += 18
    s += rule_box(20, y, 370, 55, "!", "Окончание -s/-es", "He/She/It + V-s/es: works, goes, studies")
    s += rule_box(410, y, 370, 55, "!", "Отрицание и вопрос", "She doesn't work. / Does she work?")
    y += 65

    # Conjugation table
    s += section_title(y, "Спряжение / Conjugation: WORK")
    y += 18
    widths = [130, 200, 200, 160]
    s += table_header(y, ["", "Утверждение +", "Отрицание \u2212", "Вопрос ?"], widths)
    y += 28
    s += table_row(y, ["I", "I work", "I don't work", "Do I work?"], widths, alt=False)
    y += 28
    s += table_row(y, ["He/She/It", "He works", "He doesn't work", "Does he work?"], widths, alt=True)
    y += 28
    s += table_row(y, ["We/You/They", "We work", "We don't work", "Do we work?"], widths, alt=False)
    y += 40

    # Vocabulary
    s += section_title(y, "Словарь / Vocabulary")
    y += 18
    vocab = [("wake up", "просыпаться"), ("have breakfast", "завтракать"),
             ("go to school", "идти в школу"), ("do homework", "делать уроки")]
    for i, (en, ru) in enumerate(vocab):
        col = i % 2
        row = i // 2
        px = 20 + col * 390
        py = y + row * 22
        s += f'<text x="{px}" y="{py+12}" text-anchor="start" font-family="Arial, sans-serif" font-size="12" fill="{DARK}"><tspan fill="{BLUE}" font-weight="bold">{escape(en)}</tspan> \u2014 {escape(ru)}</text>'
    y += 55

    # Examples
    s += section_title(y, "Примеры / Examples")
    y += 16
    s += example_item(20, y, 1, "I usually wake up at 7 am.", "Я обычно просыпаюсь в 7 утра.")
    s += example_item(400, y, 2, "She doesn't watch TV on weekdays.", "Она не смотрит ТВ в будни.")
    y += 38
    s += example_item(20, y, 3, "Do you always do your homework?", "Ты всегда делаешь домашнее задание?")
    s += example_item(400, y, 4, "He goes to school by bus.", "Он ездит в школу на автобусе.")

    s += svg_end(1)
    return s


# ============================================================
# LESSON 2: Household Chores
# ============================================================
def lesson2():
    s = svg_start("Домашние обязанности", "Household Chores", 2)
    y = 90

    # Have to / Must
    s += section_title(y, "Модальные глаголы / Modal Verbs: HAVE TO &amp; MUST")
    y += 18
    s += formula_box(20, y, 370, 36, [("S + ", RED), ("have to / has to", BLUE), (" + V", DARK)])
    s += formula_box(410, y, 370, 36, [("S + ", RED), ("must", BLUE), (" + V", DARK)])
    y += 44
    s += formula_box(20, y, 370, 36, [("S + ", RED), ("don't/doesn't have to", BLUE), (" + V", DARK)])
    s += formula_box(410, y, 370, 36, [("S + ", RED), ("must not (mustn't)", RED), (" + V", DARK)])
    y += 50

    # Difference
    s += section_title(y, "Разница / Difference: HAVE TO vs MUST")
    y += 18
    # Have to box
    s += f'''<rect x="20" y="{y}" width="370" height="70" fill="{LIGHT_BLUE}" stroke="{BLUE}" stroke-width="2" rx="6" />
<text x="205" y="{y+18}" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="{BLUE}" font-weight="bold">HAVE TO</text>
<text x="30" y="{y+36}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="#1F2937">Внешняя необходимость (по обстоятельствам)</text>
<text x="30" y="{y+52}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}">I have to wash the dishes. (Мама сказала)</text>
<text x="30" y="{y+65}" text-anchor="start" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">Don't have to = не обязательно</text>'''
    # Must box
    s += f'''<rect x="410" y="{y}" width="370" height="70" fill="{LIGHT_RED}" stroke="{RED}" stroke-width="2" rx="6" />
<text x="595" y="{y+18}" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="{RED}" font-weight="bold">MUST</text>
<text x="420" y="{y+36}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="#1F2937">Внутренняя необходимость (личное решение)</text>
<text x="420" y="{y+52}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}">I must clean my room. (Я так решил)</text>
<text x="420" y="{y+65}" text-anchor="start" font-family="Arial, sans-serif" font-size="10" fill="{GRAY}">Mustn't = запрещено</text>'''
    y += 82

    # Imperative
    s += section_title(y, "Повелительное наклонение / Imperative")
    y += 18
    s += rule_box(20, y, 370, 55, "!", "Утверждение", "Wash the dishes! / Open the window!")
    s += rule_box(410, y, 370, 55, "!", "Отрицание (Don't)", "Don't leave your clothes on the floor!")
    y += 65

    # Vocabulary
    s += section_title(y, "Словарь / Vocabulary: Chores")
    y += 18
    vocab = [("wash the dishes", "мыть посуду"), ("vacuum the carpet", "пылесосить"),
             ("clean the room", "убирать комнату"), ("do the laundry", "стирать"),
             ("take out the rubbish", "выносить мусор"), ("water the plants", "поливать растения"),
             ("make the bed", "заправлять кровать"), ("sweep the floor", "подметать пол")]
    for i, (en, ru) in enumerate(vocab):
        col = i % 2
        row = i // 2
        px = 20 + col * 390
        py = y + row * 20
        s += f'<text x="{px}" y="{py+12}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}"><tspan fill="{BLUE}" font-weight="bold">{escape(en)}</tspan> \u2014 {escape(ru)}</text>'
    y += 90

    # Examples
    s += section_title(y, "Примеры / Examples")
    y += 16
    s += example_item(20, y, 1, "I have to wash the dishes every day.", "Я должен мыть посуду каждый день.")
    s += example_item(400, y, 2, "You mustn't play near the road!", "Тебе нельзя играть у дороги!")
    y += 38
    s += example_item(20, y, 3, "She has to make her bed.", "Ей нужно заправлять кровать.")
    s += example_item(400, y, 4, "Don't leave your room messy!", "Не оставляй комнату в беспорядке!")

    s += svg_end(2)
    return s


# ============================================================
# LESSON 3: Planning a Trip
# ============================================================
def lesson3():
    s = svg_start("Планирование поездки", "Planning a Trip", 3)
    y = 90

    # Future forms
    s += section_title(y, "Формы будущего времени / Future Forms")
    y += 18
    # Will
    s += f'''<rect x="20" y="{y}" width="240" height="80" fill="{LIGHT_BLUE}" stroke="{BLUE}" stroke-width="2" rx="6" />
<text x="140" y="{y+18}" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="{BLUE}" font-weight="bold">WILL</text>
<text x="30" y="{y+36}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="#1F2937">Решение в момент речи,</text>
<text x="30" y="{y+50}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="#1F2937">предсказание, обещание</text>
<text x="30" y="{y+68}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}">S + will + V</text>'''
    # Going to
    s += f'''<rect x="275" y="{y}" width="250" height="80" fill="{YELLOW_BG}" stroke="{BLUE}" stroke-width="2" rx="6" />
<text x="400" y="{y+18}" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="{BLUE}" font-weight="bold">BE GOING TO</text>
<text x="285" y="{y+36}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="#1F2937">Заранее запланированное,</text>
<text x="285" y="{y+50}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="#1F2937">намерение, план</text>
<text x="285" y="{y+68}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}">S + am/is/are going to + V</text>'''
    # Present Continuous
    s += f'''<rect x="540" y="{y}" width="240" height="80" fill="{LIGHT_RED}" stroke="{RED}" stroke-width="2" rx="6" />
<text x="660" y="{y+18}" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="{RED}" font-weight="bold">PRES. CONTINUOUS</text>
<text x="550" y="{y+36}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="#1F2937">Точно запланированное</text>
<text x="550" y="{y+50}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="#1F2937">(билеты, время)</text>
<text x="550" y="{y+68}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}">S + am/is/are + V-ing</text>'''
    y += 92

    # Comparison table
    s += section_title(y, "Сравнение / Comparison")
    y += 18
    widths = [160, 280, 280]
    s += table_header(y, ["Ситуация", "Форма", "Пример"], widths)
    y += 28
    s += table_row(y, ["Мгновенное решение", "will", "\"I'll help you!\""], widths, alt=False)
    y += 28
    s += table_row(y, ["План / намерение", "be going to", "\"I'm going to visit London.\""], widths, alt=True)
    y += 28
    s += table_row(y, ["Точное расписание", "Pres. Continuous", "\"We're leaving at 9.\""], widths, alt=False)
    y += 42

    # Travel vocabulary
    s += section_title(y, "Словарь / Travel Vocabulary")
    y += 18
    vocab = [("book tickets", "бронировать билеты"), ("pack luggage", "собирать багаж"),
             ("check in", "регистрироваться"), ("board the plane", "садиться на самолёт"),
             ("destination", "пункт назначения"), ("suitcase", "чемодан"),
             ("passport", "загранпаспорт"), ("travel agency", "турагентство")]
    for i, (en, ru) in enumerate(vocab):
        col = i % 2
        row = i // 2
        px = 20 + col * 390
        py = y + row * 20
        s += f'<text x="{px}" y="{py+12}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}"><tspan fill="{BLUE}" font-weight="bold">{escape(en)}</tspan> \u2014 {escape(ru)}</text>'
    y += 90

    # Examples
    s += section_title(y, "Примеры / Examples")
    y += 16
    s += example_item(20, y, 1, "I think it will rain tomorrow.", "Думаю, завтра будет дождь.")
    s += example_item(400, y, 2, "We're going to visit Paris in summer.", "Мы собираемся посетить Париж летом.")
    y += 38
    s += example_item(20, y, 3, "Our train is leaving at 8:30.", "Наш поезд отправляется в 8:30.")
    s += example_item(400, y, 4, "I'll carry your suitcase for you!", "Я понесу твой чемодан!")

    s += svg_end(3)
    return s


# ============================================================
# LESSON 4: Sightseeing and Activities
# ============================================================
def lesson4():
    s = svg_start("Осмотр достопримечательностей", "Sightseeing and Activities", 4)
    y = 90

    # Past Simple / Past Continuous
    s += section_title(y, "Прошедшие времена / Past Tenses")
    y += 18
    # Past Simple box
    s += f'''<rect x="20" y="{y}" width="370" height="90" fill="{LIGHT_BLUE}" stroke="{BLUE}" stroke-width="2" rx="6" />
<text x="205" y="{y+18}" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="{BLUE}" font-weight="bold">PAST SIMPLE</text>
<text x="30" y="{y+36}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="#1F2937">Завершённое действие в прошлом</text>
<text x="30" y="{y+52}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}">S + V-ed / V2 (irregular)</text>
<text x="30" y="{y+66}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}">S + did not + V</text>
<text x="30" y="{y+80}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}">Did + S + V?</text>'''
    # Past Continuous box
    s += f'''<rect x="410" y="{y}" width="370" height="90" fill="{YELLOW_BG}" stroke="{RED}" stroke-width="2" rx="6" />
<text x="595" y="{y+18}" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="{RED}" font-weight="bold">PAST CONTINUOUS</text>
<text x="420" y="{y+36}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="#1F2937">Действие в процессе в прошлом</text>
<text x="420" y="{y+52}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}">S + was/were + V-ing</text>
<text x="420" y="{y+66}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}">S + was/were not + V-ing</text>
<text x="420" y="{y+80}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}">Was/Were + S + V-ing?</text>'''
    y += 102

    # When/While rule
    s += section_title(y, "Комбинация / When + Past Simple, While + Past Continuous")
    y += 18
    s += rule_box(20, y, 370, 55, "!", "WHEN + Past Simple", "I was walking WHEN it started to rain.")
    s += rule_box(410, y, 370, 55, "!", "WHILE + Past Continuous", "WHILE she was reading, the phone rang.")
    y += 65

    # Time markers
    s += section_title(y, "Маркеры времени / Time Markers")
    y += 18
    markers_ps = ["yesterday", "last week", "in 2023", "two days ago"]
    markers_pc = ["at 5 pm yesterday", "while", "when", "all morning"]
    for i, m in enumerate(markers_ps):
        s += pill(20 + i * 190, y, 178, 24, m, LIGHT_BLUE, BLUE)
    y += 30
    for i, m in enumerate(markers_pc):
        s += pill(20 + i * 190, y, 178, 24, m, YELLOW_BG, RED, RED)
    y += 40

    # Sightseeing vocab
    s += section_title(y, "Словарь / Sightseeing Vocabulary")
    y += 18
    vocab = [("cathedral", "собор"), ("museum", "музей"),
             ("monument", "памятник"), ("art gallery", "художественная галерея"),
             ("sightseeing tour", "экскурсия"), ("take photos", "фотографировать"),
             ("buy souvenirs", "покупать сувениры"), ("go sightseeing", "осматривать достопримечательности")]
    for i, (en, ru) in enumerate(vocab):
        col = i % 2
        row = i // 2
        px = 20 + col * 390
        py = y + row * 20
        s += f'<text x="{px}" y="{py+12}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}"><tspan fill="{BLUE}" font-weight="bold">{escape(en)}</tspan> \u2014 {escape(ru)}</text>'
    y += 90

    # Examples
    s += section_title(y, "Примеры / Examples")
    y += 16
    s += example_item(20, y, 1, "We visited the museum yesterday.", "Мы посетили музей вчера.")
    s += example_item(400, y, 2, "I was taking photos when it rained.", "Я фотографировал, когда пошёл дождь.")
    y += 38
    s += example_item(20, y, 3, "While they were sightseeing, we rested.", "Пока они осматривали, мы отдыхали.")
    s += example_item(400, y, 4, "Did you buy any souvenirs?", "Ты купил сувениры?")

    s += svg_end(4)
    return s


# ============================================================
# LESSON 5: Environmental Problems
# ============================================================
def lesson5():
    s = svg_start("Экологические проблемы", "Environmental Problems", 5)
    y = 90

    # Modal verbs for obligation/advice
    s += section_title(y, "Модальные глаголы / Modal Verbs for Obligation &amp; Advice")
    y += 18
    # Should box
    s += f'''<rect x="20" y="{y}" width="240" height="80" fill="{LIGHT_BLUE}" stroke="{BLUE}" stroke-width="2" rx="6" />
<text x="140" y="{y+18}" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="{BLUE}" font-weight="bold">SHOULD</text>
<text x="30" y="{y+36}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="#1F2937">Совет, рекомендация</text>
<text x="30" y="{y+52}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}">S + should + V</text>
<text x="30" y="{y+66}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}">S + should not (shouldn't) + V</text>'''
    # Must box
    s += f'''<rect x="275" y="{y}" width="250" height="80" fill="{LIGHT_RED}" stroke="{RED}" stroke-width="2" rx="6" />
<text x="400" y="{y+18}" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="{RED}" font-weight="bold">MUST</text>
<text x="285" y="{y+36}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="#1F2937">Обязанность, необходимость</text>
<text x="285" y="{y+52}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}">S + must + V</text>
<text x="285" y="{y+66}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}">S + must not (mustn't) + V</text>'''
    # Have to box
    s += f'''<rect x="540" y="{y}" width="240" height="80" fill="{YELLOW_BG}" stroke="{BLUE}" stroke-width="2" rx="6" />
<text x="660" y="{y+18}" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="{BLUE}" font-weight="bold">HAVE TO</text>
<text x="550" y="{y+36}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="#1F2937">Вынужденная необходимость</text>
<text x="550" y="{y+52}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}">S + have to / has to + V</text>
<text x="550" y="{y+66}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}">S + don't have to + V</text>'''
    y += 92

    # Comparison table
    s += section_title(y, "Сравнение / Comparison of Modals")
    y += 18
    widths = [140, 200, 200, 220]
    s += table_header(y, ["Модальный", "Значение", "Пример", "Перевод"], widths)
    y += 28
    s += table_row(y, ["should", "совет", "You should recycle.", "Вам следует перерабатывать."], widths, alt=False)
    y += 28
    s += table_row(y, ["must", "обязанность", "We must protect nature.", "Мы должны беречь природу."], widths, alt=True)
    y += 28
    s += table_row(y, ["have to", "необходимость", "I have to sort rubbish.", "Мне нужно сортировать мусор."], widths, alt=False)
    y += 28
    s += table_row(y, ["mustn't", "запрещено", "You mustn't litter!", "Нельзя мусорить!"], widths, alt=True)
    y += 28
    s += table_row(y, ["don't have to", "не обязат.", "You don't have to come.", "Необязательно приходить."], widths, alt=False)
    y += 42

    # Environment vocabulary
    s += section_title(y, "Словарь / Environment Vocabulary")
    y += 18
    vocab = [("pollution", "загрязнение"), ("recycle", "перерабатывать"),
             ("global warming", "глобальное потепление"), ("endangered species", "исчезающие виды"),
             ("deforestation", "вырубка лесов"), ("rubbish / litter", "мусор"),
             ("solar energy", "солнечная энергия"), ("protect nature", "защищать природу")]
    for i, (en, ru) in enumerate(vocab):
        col = i % 2
        row = i // 2
        px = 20 + col * 390
        py = y + row * 20
        s += f'<text x="{px}" y="{py+12}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}"><tspan fill="{BLUE}" font-weight="bold">{escape(en)}</tspan> \u2014 {escape(ru)}</text>'
    y += 90

    # Examples
    s += section_title(y, "Примеры / Examples")
    y += 16
    s += example_item(20, y, 1, "You should use public transport.", "Тебе следует пользоваться общ. транспортом.")
    s += example_item(400, y, 2, "We must stop deforestation!", "Мы должны остановить вырубку лесов!")
    y += 38
    s += example_item(20, y, 3, "People mustn't throw litter in parks.", "Люди не должны бросать мусор в парках.")
    s += example_item(400, y, 4, "We don't have to use plastic bags.", "Необязательно использовать пластиковые пакеты.")

    s += svg_end(5)
    return s


# ============================================================
# LESSON 6: Digital World
# ============================================================
def lesson6():
    s = svg_start("Цифровой мир", "Digital World", 6)
    y = 90

    # Present Perfect
    s += section_title(y, "Present Perfect / Настоящее совершённое время")
    y += 18
    s += formula_box(20, y, 355, 36, [("S + ", RED), ("have/has", BLUE), (" + V3", DARK), (" + ...", GRAY)])
    s += formula_box(390, y, 380, 36, [("S + ", RED), ("haven't/hasn't", RED), (" + V3", DARK), (" + ...", GRAY)])
    y += 44
    s += formula_box(20, y, 750, 36, [("Have/Has", RED), (" + S + ", RED), ("V3", BLUE), (" + ... ?", GRAY)])
    y += 50

    # Usage rules
    s += section_title(y, "Когда используем / When to Use Present Perfect")
    y += 18
    s += rule_box(20, y, 370, 55, "1", "Опыт в жизни", "I have visited London. (Когда-либо в жизни)")
    s += rule_box(410, y, 370, 55, "2", "Результат виден сейчас", "She has broken her phone. (Оно сломано)")
    y += 63
    s += rule_box(20, y, 370, 55, "3", "Действие началось, ещё длится", "I have known him for 5 years.")
    s += rule_box(410, y, 370, 55, "4", "Недавнее событие", "They have just arrived. (Только что)")
    y += 65

    # Key words
    s += section_title(y, "Ключевые слова / Key Words")
    y += 18
    words = [("ever", "когда-либо"), ("never", "никогда"),
             ("just", "только что"), ("already", "уже"),
             ("yet", "ещё не"), ("recently", "недавно"),
             ("since", "с (момента)"), ("for", "в течение")]
    for i, (en, ru) in enumerate(words):
        col = i % 4
        row = i // 4
        px = 20 + col * 195
        py = y + row * 30
        s += pill(px, py, 180, 24, f"{en} \u2014 {ru}")
    y += 75

    # Position of adverbs
    s += section_title(y, "Позиция наречий / Adverb Position")
    y += 18
    widths = [200, 260, 260]
    s += table_header(y, ["Наречие", "Позиция", "Пример"], widths)
    y += 28
    s += table_row(y, ["just", "после have/has", "I have just finished."], widths, alt=False)
    y += 28
    s += table_row(y, ["already", "после have/has", "She has already left."], widths, alt=True)
    y += 28
    s += table_row(y, ["yet", "в конце предложения", "Have you done it yet?"], widths, alt=False)
    y += 28
    s += table_row(y, ["ever / never", "после have/has", "I have never been there."], widths, alt=True)
    y += 42

    # Technology vocabulary
    s += section_title(y, "Словарь / Technology Vocabulary")
    y += 18
    vocab = [("download an app", "скачать приложение"), ("create an account", "создать аккаунт"),
             ("go online", "выходить в интернет"), ("update software", "обновлять ПО"),
             ("send a message", "отправить сообщение"), ("search the web", "искать в интернете")]
    for i, (en, ru) in enumerate(vocab):
        col = i % 2
        row = i // 2
        px = 20 + col * 390
        py = y + row * 20
        s += f'<text x="{px}" y="{py+12}" text-anchor="start" font-family="Arial, sans-serif" font-size="11" fill="{DARK}"><tspan fill="{BLUE}" font-weight="bold">{escape(en)}</tspan> \u2014 {escape(ru)}</text>'

    # Examples - squeeze into remaining space
    y += 72
    s += example_item(20, y, 1, "I have just downloaded a new app.", "Я только что скачал новое приложение.")
    s += example_item(400, y, 2, "Have you ever visited this website?", "Ты когда-нибудь посещал этот сайт?")

    s += svg_end(6)
    return s


# ============================================================
# Generate all and validate
# ============================================================
lessons = [
    (1, lesson1),
    (2, lesson2),
    (3, lesson3),
    (4, lesson4),
    (5, lesson5),
    (6, lesson6),
]

results = []
for num, gen_func in lessons:
    svg_content = gen_func()
    filepath = os.path.join(OUT_DIR, f"lesson-{num}.svg")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content)
    # Validate
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        w = root.attrib.get("width", "?")
        h = root.attrib.get("height", "?")
        results.append(f"  lesson-{num}.svg: VALID XML | {w}x{h} | {len(svg_content)} chars")
    except ET.ParseError as e:
        results.append(f"  lesson-{num}.svg: INVALID XML - {e}")

print("=" * 60)
print("Grade 7 English SVG Generation Results")
print("=" * 60)
print(f"Output directory: {OUT_DIR}")
print(f"Files generated: {len(lessons)}")
print()
for r in results:
    print(r)
print()
print("All SVGs validated with xml.etree.ElementTree.")
