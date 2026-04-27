#!/usr/bin/env python3
"""Generate 15 educational SVG images for Grade 8 English language lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/english"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Color scheme
BLUE = "#3B82F6"
RED = "#DC2626"
DARK_BLUE = "#1E3A5F"
LIGHT_BLUE = "#DBEAFE"
LIGHT_RED = "#FEE2E2"
LIGHT_GREEN = "#DCFCE7"
LIGHT_YELLOW = "#FEF9C3"
LIGHT_GRAY = "#F3F4F6"
WHITE = "#FFFFFF"
BLACK = "#1F2937"
GRAY = "#6B7280"
GREEN = "#16A34A"
ORANGE = "#EA580C"
PURPLE = "#7C3AED"

SUBJ_COLOR = RED
VERB_COLOR = BLUE
OBJ_COLOR = GREEN

W, H = 800, 600

def esc(text):
    """Escape text for XML."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def svg_root():
    """Create base SVG element."""
    svg = ET.Element("svg")
    svg.set("xmlns", "http://www.w3.org/2000/svg")
    svg.set("width", str(W))
    svg.set("height", str(H))
    svg.set("viewBox", f"0 0 {W} {H}")
    return svg

def add_bg(svg, color=LIGHT_GRAY):
    """Add background rectangle."""
    rect = ET.SubElement(svg, "rect")
    rect.set("width", str(W))
    rect.set("height", str(H))
    rect.set("fill", color)
    rect.set("rx", "0")

def add_header(svg, title, subtitle=""):
    """Add header bar with title."""
    # Header background
    rect = ET.SubElement(svg, "rect")
    rect.set("x", "0")
    rect.set("y", "0")
    rect.set("width", str(W))
    rect.set("height", "70")
    rect.set("fill", BLUE)

    # Title text
    t = ET.SubElement(svg, "text")
    t.set("x", "400")
    t.set("y", "32")
    t.set("text-anchor", "middle")
    t.set("font-family", "Arial, sans-serif")
    t.set("font-size", "22")
    t.set("font-weight", "bold")
    t.set("fill", WHITE)
    t.text = esc(title)

    if subtitle:
        t2 = ET.SubElement(svg, "text")
        t2.set("x", "400")
        t2.set("y", "56")
        t2.set("text-anchor", "middle")
        t2.set("font-family", "Arial, sans-serif")
        t2.set("font-size", "14")
        t2.set("fill", "#BFDBFE")
        t2.text = esc(subtitle)

    # Accent line
    line = ET.SubElement(svg, "rect")
    line.set("x", "0")
    line.set("y", "70")
    line.set("width", str(W))
    line.set("height", "3")
    line.set("fill", RED)

def add_box(svg, x, y, w, h, fill=WHITE, stroke=BLUE, stroke_w=2, rx=8):
    """Add a rounded box."""
    rect = ET.SubElement(svg, "rect")
    rect.set("x", str(x))
    rect.set("y", str(y))
    rect.set("width", str(w))
    rect.set("height", str(h))
    rect.set("fill", fill)
    rect.set("stroke", stroke)
    rect.set("stroke-width", str(stroke_w))
    rect.set("rx", str(rx))
    return rect

def add_text(svg, x, y, text, size=14, color=BLACK, anchor="start", bold=False, font="Arial, sans-serif"):
    """Add text element."""
    t = ET.SubElement(svg, "text")
    t.set("x", str(x))
    t.set("y", str(y))
    t.set("text-anchor", anchor)
    t.set("font-family", font)
    t.set("font-size", str(size))
    t.set("fill", color)
    if bold:
        t.set("font-weight", "bold")
    t.text = esc(text)
    return t

def add_colored_text(svg, x, y, segments, size=14, anchor="start"):
    """Add text with multiple colored segments. segments = [(text, color), ...]"""
    t = ET.SubElement(svg, "text")
    t.set("x", str(x))
    t.set("y", str(y))
    t.set("text-anchor", anchor)
    t.set("font-family", "Arial, sans-serif")
    t.set("font-size", str(size))
    for text, color in segments:
        tspan = ET.SubElement(t, "tspan")
        tspan.set("fill", color)
        tspan.text = esc(text)
    return t

def add_section_title(svg, x, y, text, color=BLUE):
    """Add a section title with underline."""
    t = add_text(svg, x, y, text, size=15, color=color, bold=True)
    line = ET.SubElement(svg, "line")
    line.set("x1", str(x))
    line.set("y1", str(y + 3))
    line.set("x2", str(x + len(text) * 8))
    line.set("y2", str(y + 3))
    line.set("stroke", color)
    line.set("stroke-width", "1.5")

def add_grammar_formula(svg, x, y, formula_parts, w=360, h=36):
    """Add a grammar formula box. formula_parts = [(text, color), ...]"""
    add_box(svg, x, y, w, h, fill=LIGHT_YELLOW, stroke=BLUE, stroke_w=2, rx=6)
    t = ET.SubElement(svg, "text")
    t.set("x", str(x + w // 2))
    t.set("y", str(y + 24))
    t.set("text-anchor", "middle")
    t.set("font-family", "Arial, sans-serif")
    t.set("font-size", "15")
    t.set("font-weight", "bold")
    for text, color in formula_parts:
        tspan = ET.SubElement(t, "tspan")
        tspan.set("fill", color)
        tspan.text = esc(text)

def add_example_sentence(svg, x, y, en_text, ru_text, idx):
    """Add an example sentence with number."""
    # Number badge
    circle = ET.SubElement(svg, "circle")
    circle.set("cx", str(x + 10))
    circle.set("cy", str(y - 4))
    circle.set("r", "9")
    circle.set("fill", BLUE)
    add_text(svg, x + 10, y, str(idx), size=11, color=WHITE, anchor="middle", bold=True)
    add_text(svg, x + 26, y, en_text, size=13, color=DARK_BLUE)
    add_text(svg, x + 26, y + 16, ru_text, size=11, color=GRAY)

def add_table(svg, x, y, headers, rows, col_widths, header_color=BLUE):
    """Add a table."""
    row_h = 28
    total_w = sum(col_widths)

    # Header
    add_box(svg, x, y, total_w, row_h, fill=header_color, stroke=header_color, rx=0)
    cx = x
    for i, header in enumerate(headers):
        add_text(svg, cx + col_widths[i] // 2, y + 19, header, size=12, color=WHITE, anchor="middle", bold=True)
        cx += col_widths[i]

    # Rows
    for r, row in enumerate(rows):
        ry = y + row_h + r * row_h
        bg = WHITE if r % 2 == 0 else LIGHT_BLUE
        add_box(svg, x, ry, total_w, row_h, fill=bg, stroke="#CBD5E1", stroke_w=1, rx=0)
        cx = x
        for i, cell in enumerate(row):
            add_text(svg, cx + 8, ry + 19, cell, size=11, color=BLACK)
            cx += col_widths[i]

    return y + row_h + len(rows) * row_h

def add_rule_box(svg, x, y, w, h, title, text, icon="!"):
    """Add a highlighted rule box."""
    add_box(svg, x, y, w, h, fill=LIGHT_RED, stroke=RED, stroke_w=2, rx=6)
    # Icon circle
    circle = ET.SubElement(svg, "circle")
    circle.set("cx", str(x + 18))
    circle.set("cy", str(y + 18))
    circle.set("r", "12")
    circle.set("fill", RED)
    add_text(svg, x + 18, y + 23, icon, size=14, color=WHITE, anchor="middle", bold=True)
    add_text(svg, x + 36, y + 22, title, size=13, color=RED, bold=True)
    add_text(svg, x + 12, y + 44, text, size=11, color=BLACK)

def add_arrow(svg, x1, y1, x2, y2, color=BLUE):
    """Add an arrow line."""
    line = ET.SubElement(svg, "line")
    line.set("x1", str(x1))
    line.set("y1", str(y1))
    line.set("x2", str(x2))
    line.set("y2", str(y2))
    line.set("stroke", color)
    line.set("stroke-width", "2")
    line.set("marker-end", "url(#arrowhead)")

def add_defs(svg):
    """Add common defs like arrow markers."""
    defs = ET.SubElement(svg, "defs")
    marker = ET.SubElement(defs, "marker")
    marker.set("id", "arrowhead")
    marker.set("markerWidth", "10")
    marker.set("markerHeight", "7")
    marker.set("refX", "10")
    marker.set("refY", "3.5")
    marker.set("orient", "auto")
    poly = ET.SubElement(marker, "polygon")
    poly.set("points", "0 0, 10 3.5, 0 7")
    poly.set("fill", BLUE)

def add_footer(svg, lesson_num):
    """Add footer."""
    rect = ET.SubElement(svg, "rect")
    rect.set("x", "0")
    rect.set("y", str(H - 30))
    rect.set("width", str(W))
    rect.set("height", "30")
    rect.set("fill", DARK_BLUE)
    add_text(svg, 20, H - 10, f"Grade 8 | English | Lesson {lesson_num}", size=11, color="#94A3B8")
    add_text(svg, W - 20, H - 10, f"Lesson {lesson_num}/15", size=11, color="#94A3B8", anchor="end")


# ===================== LESSON GENERATORS =====================

def lesson_01():
    """Present Simple."""
    svg = svg_root()
    add_defs(svg)
    add_bg(svg)
    add_header(svg, "Present Simple", "Настоящее простое время")

    # Formula boxes
    add_section_title(svg, 20, 100, "Формула образования / Formation")
    add_grammar_formula(svg, 20, 112, [("S + V", SUBJ_COLOR), (" (", GRAY), ("V/Vs/Ves", VERB_COLOR), (") + ...", GRAY)], w=355, h=36)
    add_grammar_formula(svg, 390, 112, [("S + ", SUBJ_COLOR), ("do not / does not", RED), (" + V", VERB_COLOR), (" + ...", GRAY)], w=380, h=36)

    # Question form
    add_grammar_formula(svg, 20, 156, [("Do/Does", RED), (" + S + ", SUBJ_COLOR), ("V", VERB_COLOR), (" + ...?", GRAY)], w=750, h=36)

    # Time markers box
    add_section_title(svg, 20, 215, "Маркеры времени / Time Markers")
    markers = ["always", "usually", "often", "sometimes", "rarely", "never", "every day", "on Mondays"]
    bx = 20
    for i, m in enumerate(markers):
        x = 20 + (i % 4) * 190
        y = 225 + (i // 4) * 30
        add_box(svg, x, y, 175, 24, fill=LIGHT_BLUE, stroke=BLUE, stroke_w=1, rx=12)
        add_text(svg, x + 87, y + 17, m, size=12, color=DARK_BLUE, anchor="middle", bold=True)

    # Rules
    add_section_title(svg, 20, 300, "Правила / Rules")
    add_rule_box(svg, 20, 310, 370, 55, "Правило 1: Окончание -s/-es",
                 "He/She/It + V-s/es: works, goes, studies")
    add_rule_box(svg, 410, 310, 370, 55, "Правило 2: Отрицание",
                 "He doesn't work. / They don't work.")

    # Table
    add_section_title(svg, 20, 385, "Спряжение глагола WORK / Conjugation")
    headers = ["", "Утверждение +", "Отрицание −", "Вопрос ?"]
    rows = [
        ["I", "I work", "I don't work", "Do I work?"],
        ["He/She/It", "He works", "He doesn't work", "Does he work?"],
        ["We/You/They", "We work", "We don't work", "Do we work?"],
    ]
    add_table(svg, 20, 398, headers, rows, [90, 200, 200, 200])

    # Examples
    add_section_title(svg, 20, 500, "Примеры / Examples")
    add_example_sentence(svg, 20, 520, "She goes to school every day.", "Она ходит в школу каждый день.", 1)
    add_example_sentence(svg, 20, 550, "I don't like spicy food.", "Я не люблю острую еду.", 2)
    add_example_sentence(svg, 400, 520, "Do you speak English?", "Ты говоришь по-английски?", 3)
    add_example_sentence(svg, 400, 550, "He always reads books.", "Он всегда читает книги.", 4)

    add_footer(svg, 1)
    return svg

def lesson_02():
    """Present Continuous."""
    svg = svg_root()
    add_defs(svg)
    add_bg(svg)
    add_header(svg, "Present Continuous", "Настоящее длительное время")

    add_section_title(svg, 20, 100, "Формула образования / Formation")
    add_grammar_formula(svg, 20, 112, [("S + ", SUBJ_COLOR), ("am/is/are", VERB_COLOR), (" + ", GRAY), ("V-ing", RED), (" + ...", GRAY)], w=355, h=36)
    add_grammar_formula(svg, 390, 112, [("S + ", SUBJ_COLOR), ("am/is/are + not", RED), (" + ", GRAY), ("V-ing", VERB_COLOR)], w=380, h=36)
    add_grammar_formula(svg, 20, 156, [("Am/Is/Are", RED), (" + S + ", SUBJ_COLOR), ("V-ing", VERB_COLOR), (" + ...?", GRAY)], w=750, h=36)

    add_section_title(svg, 20, 210, "Маркеры времени / Time Markers")
    markers = ["now", "right now", "at the moment", "currently", "Look!", "Listen!", "today", "this week"]
    for i, m in enumerate(markers):
        x = 20 + (i % 4) * 190
        y = 220 + (i // 4) * 30
        add_box(svg, x, y, 175, 24, fill=LIGHT_BLUE, stroke=BLUE, stroke_w=1, rx=12)
        add_text(svg, x + 87, y + 17, m, size=12, color=DARK_BLUE, anchor="middle", bold=True)

    add_section_title(svg, 20, 295, "Правила правописания -ing / Spelling Rules")
    headers = ["Правило", "Пример"]
    rows = [
        ["Общее: +ing", "work → working, play → playing"],
        ["Немая -e: drop e + ing", "make → making, write → writing"],
        ["Удвоение согласной", "run → running, swim → swimming"],
        ["Конец -ie → y + ing", "lie → lying, die → dying"],
    ]
    add_table(svg, 20, 308, headers, rows, [230, 460])

    add_section_title(svg, 20, 430, "Примеры / Examples")
    add_example_sentence(svg, 20, 452, "I am reading a book now.", "Я сейчас читаю книгу.", 1)
    add_example_sentence(svg, 20, 482, "She is not sleeping at the moment.", "Она не спит в данный момент.", 2)
    add_example_sentence(svg, 400, 452, "Are they playing football?", "Они играют в футбол?", 3)
    add_example_sentence(svg, 400, 482, "Look! It is raining!", "Смотри! Идёт дождь!", 4)

    add_rule_box(svg, 20, 520, 750, 45, "Запомни!",
                 "Stative verbs (know, like, want, love) НЕ используются в Present Continuous!")

    add_footer(svg, 2)
    return svg

def lesson_03():
    """Present Perfect."""
    svg = svg_root()
    add_defs(svg)
    add_bg(svg)
    add_header(svg, "Present Perfect", "Настоящее совершённое время")

    add_section_title(svg, 20, 100, "Формула образования / Formation")
    add_grammar_formula(svg, 20, 112, [("S + ", SUBJ_COLOR), ("have/has", VERB_COLOR), (" + ", GRAY), ("V3 (Past Participle)", RED), (" + ...", GRAY)], w=355, h=36)
    add_grammar_formula(svg, 390, 112, [("S + ", SUBJ_COLOR), ("haven't/hasn't", RED), (" + ", GRAY), ("V3", VERB_COLOR), (" + ...", GRAY)], w=380, h=36)
    add_grammar_formula(svg, 20, 156, [("Have/Has", RED), (" + S + ", SUBJ_COLOR), ("V3", VERB_COLOR), (" + ...?", GRAY)], w=750, h=36)

    add_section_title(svg, 20, 210, "Маркеры времени / Time Markers")
    markers = ["ever", "never", "already", "yet", "just", "recently", "since", "for"]
    for i, m in enumerate(markers):
        x = 20 + (i % 4) * 190
        y = 220 + (i // 4) * 30
        add_box(svg, x, y, 175, 24, fill=LIGHT_RED, stroke=RED, stroke_w=1, rx=12)
        add_text(svg, x + 87, y + 17, m, size=12, color=DARK_BLUE, anchor="middle", bold=True)

    add_section_title(svg, 20, 295, "Таблица неправильных глаголов / Irregular Verbs")
    headers = ["V1 (Infinitive)", "V2 (Past Simple)", "V3 (Past Participle)"]
    rows = [
        ["go", "went", "gone"],
        ["write", "wrote", "written"],
        ["see", "saw", "seen"],
        ["eat", "ate", "eaten"],
        ["do", "did", "done"],
    ]
    add_table(svg, 20, 308, headers, rows, [230, 230, 230])

    add_section_title(svg, 20, 468, "Примеры / Examples")
    add_example_sentence(svg, 20, 490, "I have already done my homework.", "Я уже сделал домашнее задание.", 1)
    add_example_sentence(svg, 20, 520, "She has never been to London.", "Она никогда не была в Лондоне.", 2)
    add_example_sentence(svg, 400, 490, "Have you ever eaten sushi?", "Ты когда-нибудь ел суши?", 3)
    add_example_sentence(svg, 400, 520, "He hasn't finished yet.", "Он ещё не закончил.", 4)

    add_rule_box(svg, 20, 553, 750, 35, "Since vs For",
                 "since + момент (since 2020) | for + период (for 3 years)")

    add_footer(svg, 3)
    return svg

def lesson_04():
    """Past Simple."""
    svg = svg_root()
    add_defs(svg)
    add_bg(svg)
    add_header(svg, "Past Simple", "Прошедшее простое время")

    add_section_title(svg, 20, 100, "Формула образования / Formation")
    add_grammar_formula(svg, 20, 112, [("S + ", SUBJ_COLOR), ("V2 / V-ed", VERB_COLOR), (" + ...", GRAY)], w=240, h=36)
    add_grammar_formula(svg, 270, 112, [("S + ", SUBJ_COLOR), ("did not", RED), (" + ", GRAY), ("V", VERB_COLOR), (" + ...", GRAY)], w=250, h=36)
    add_grammar_formula(svg, 530, 112, [("Did", RED), (" + S + ", SUBJ_COLOR), ("V", VERB_COLOR), (" + ...?", GRAY)], w=240, h=36)

    add_section_title(svg, 20, 165, "Маркеры времени / Time Markers")
    markers = ["yesterday", "last week", "last month", "last year", "ago", "in 2020", "the other day", "then"]
    for i, m in enumerate(markers):
        x = 20 + (i % 4) * 190
        y = 175 + (i // 4) * 30
        add_box(svg, x, y, 175, 24, fill=LIGHT_YELLOW, stroke=ORANGE, stroke_w=1, rx=12)
        add_text(svg, x + 87, y + 17, m, size=12, color=DARK_BLUE, anchor="middle", bold=True)

    add_section_title(svg, 20, 248, "Regular vs Irregular Verbs")
    headers = ["Тип", "Правило", "Пример"]
    rows = [
        ["Regular", "+ed", "work → worked, play → played"],
        ["Regular (e)", "+d", "like → liked, live → lived"],
        ["Regular (y)", "-y +ied", "study → studied, cry → cried"],
        ["Irregular", "особая форма", "go → went, see → saw, eat → ate"],
    ]
    add_table(svg, 20, 261, headers, rows, [120, 180, 390])

    add_section_title(svg, 20, 385, "Спряжение глагола WORK / Conjugation")
    headers2 = ["", "Утверждение +", "Отрицание −", "Вопрос ?"]
    rows2 = [
        ["I/He/She/It", "I worked", "I didn't work", "Did I work?"],
        ["We/You/They", "We worked", "We didn't work", "Did we work?"],
    ]
    add_table(svg, 20, 398, headers2, rows2, [130, 190, 190, 180])

    add_section_title(svg, 20, 468, "Примеры / Examples")
    add_example_sentence(svg, 20, 490, "We visited Paris last summer.", "Мы посетили Париж прошлым летом.", 1)
    add_example_sentence(svg, 20, 520, "She didn't go to school yesterday.", "Она не пошла в школу вчера.", 2)
    add_example_sentence(svg, 400, 490, "Did you watch the movie?", "Ты смотрел фильм?", 3)
    add_example_sentence(svg, 400, 520, "He bought a new car two days ago.", "Он купил машину два дня назад.", 4)

    add_footer(svg, 4)
    return svg

def lesson_05():
    """Past Continuous."""
    svg = svg_root()
    add_defs(svg)
    add_bg(svg)
    add_header(svg, "Past Continuous", "Прошедшее длительное время")

    add_section_title(svg, 20, 100, "Формула образования / Formation")
    add_grammar_formula(svg, 20, 112, [("S + ", SUBJ_COLOR), ("was/were", VERB_COLOR), (" + ", GRAY), ("V-ing", RED), (" + ...", GRAY)], w=355, h=36)
    add_grammar_formula(svg, 390, 112, [("S + ", SUBJ_COLOR), ("was/were + not", RED), (" + V-ing", VERB_COLOR)], w=380, h=36)
    add_grammar_formula(svg, 20, 156, [("Was/Were", RED), (" + S + ", SUBJ_COLOR), ("V-ing", VERB_COLOR), (" + ...?", GRAY)], w=750, h=36)

    add_section_title(svg, 20, 210, "Маркеры времени / Time Markers")
    markers = ["at 5 pm yesterday", "at that time", "while", "when", "all day", "from 2 to 4", "as", "the whole evening"]
    for i, m in enumerate(markers):
        x = 20 + (i % 4) * 190
        y = 220 + (i // 4) * 30
        add_box(svg, x, y, 175, 24, fill=LIGHT_BLUE, stroke=BLUE, stroke_w=1, rx=12)
        add_text(svg, x + 87, y + 17, m, size=12, color=DARK_BLUE, anchor="middle", bold=True)

    add_section_title(svg, 20, 295, "Past Continuous + Past Simple / Комбинация")
    add_rule_box(svg, 20, 308, 750, 48, "Когда использовать / When to use",
                 "Действие происходило в определённый момент в прошлом / было прервано другим действием")

    # Diagram: two parallel bars
    add_box(svg, 20, 370, 370, 100, fill=LIGHT_YELLOW, stroke=ORANGE, stroke_w=2, rx=6)
    add_text(svg, 30, 388, "Длительное действие (Past Continuous):", size=11, color=ORANGE, bold=True)
    add_box(svg, 50, 400, 250, 18, fill=LIGHT_BLUE, stroke=BLUE, stroke_w=1, rx=4)
    add_text(svg, 175, 414, "was reading", size=11, color=BLUE, anchor="middle")
    # Interrupting action
    line = ET.SubElement(svg, "line")
    line.set("x1", "180"); line.set("y1", "398"); line.set("x2", "180"); line.set("y2", "460")
    line.set("stroke", RED); line.set("stroke-width", "2"); line.set("stroke-dasharray", "4")
    add_text(svg, 200, 430, "phone rang (Past Simple)", size=11, color=RED, bold=True)

    add_section_title(svg, 20, 485, "Примеры / Examples")
    add_example_sentence(svg, 20, 505, "I was reading when the phone rang.", "Я читал, когда зазвонил телефон.", 1)
    add_example_sentence(svg, 400, 505, "They were playing all evening.", "Они играли весь вечер.", 2)
    add_example_sentence(svg, 20, 535, "She wasn't sleeping at midnight.", "Она не спала в полночь.", 3)
    add_example_sentence(svg, 400, 535, "Were you watching TV at 8 pm?", "Ты смотрел ТВ в 8 вечера?", 4)

    add_footer(svg, 5)
    return svg

def lesson_06():
    """Future Simple."""
    svg = svg_root()
    add_defs(svg)
    add_bg(svg)
    add_header(svg, "Future Simple", "Будущее простое время")

    add_section_title(svg, 20, 100, "Формула образования / Formation")
    add_grammar_formula(svg, 20, 112, [("S + ", SUBJ_COLOR), ("will", VERB_COLOR), (" + ", GRAY), ("V", RED), (" + ...", GRAY)], w=240, h=36)
    add_grammar_formula(svg, 270, 112, [("S + ", SUBJ_COLOR), ("will not (won't)", RED), (" + ", GRAY), ("V", VERB_COLOR)], w=260, h=36)
    add_grammar_formula(svg, 540, 112, [("Will", RED), (" + S + ", SUBJ_COLOR), ("V", VERB_COLOR), (" ...?", GRAY)], w=230, h=36)

    add_section_title(svg, 20, 165, "Маркеры времени / Time Markers")
    markers = ["tomorrow", "next week", "next month", "next year", "soon", "in 2025", "the day after tomorrow", "in the future"]
    for i, m in enumerate(markers):
        x = 20 + (i % 4) * 190
        y = 175 + (i // 4) * 30
        add_box(svg, x, y, 175, 24, fill=LIGHT_GREEN, stroke=GREEN, stroke_w=1, rx=12)
        add_text(svg, x + 87, y + 17, m, size=12, color=DARK_BLUE, anchor="middle", bold=True)

    add_section_title(svg, 20, 248, "Случаи использования / When to use")
    add_rule_box(svg, 20, 261, 370, 48, "1. Спонтанные решения",
                 "The phone is ringing. — I'll answer it!")
    add_rule_box(svg, 410, 261, 370, 48, "2. Предсказания",
                 "It will rain tomorrow. / You will be fine.")
    add_rule_box(svg, 20, 318, 370, 48, "3. Обещания",
                 "I will help you with homework.")
    add_rule_box(svg, 410, 318, 370, 48, "4. Предложения/просьбы",
                 "Will you open the window? / Shall we go?")

    add_section_title(svg, 20, 385, "Спряжение / Conjugation")
    headers = ["", "Утверждение +", "Отрицание −", "Вопрос ?"]
    rows = [
        ["I/He/She/It", "I will go", "I won't go", "Will I go?"],
        ["We/You/They", "We will go", "We won't go", "Will we go?"],
    ]
    add_table(svg, 20, 398, headers, rows, [130, 190, 190, 180])

    add_section_title(svg, 20, 468, "Примеры / Examples")
    add_example_sentence(svg, 20, 490, "I will call you tomorrow.", "Я позвоню тебе завтра.", 1)
    add_example_sentence(svg, 20, 520, "She won't come to the party.", "Она не придёт на вечеринку.", 2)
    add_example_sentence(svg, 400, 490, "Will you help me?", "Ты поможешь мне?", 3)
    add_example_sentence(svg, 400, 520, "We will win the game!", "Мы выиграем игру!", 4)

    add_footer(svg, 6)
    return svg

def lesson_07():
    """To be going to."""
    svg = svg_root()
    add_defs(svg)
    add_bg(svg)
    add_header(svg, "To be going to", "Конструкция «собираться сделать»")

    add_section_title(svg, 20, 100, "Формула образования / Formation")
    add_grammar_formula(svg, 20, 112, [("S + ", SUBJ_COLOR), ("am/is/are going to", VERB_COLOR), (" + ", GRAY), ("V", RED), (" + ...", GRAY)], w=355, h=36)
    add_grammar_formula(svg, 390, 112, [("S + ", SUBJ_COLOR), ("am/is/are not going to", RED), (" + V", VERB_COLOR)], w=380, h=36)
    add_grammar_formula(svg, 20, 156, [("Am/Is/Are", RED), (" + S + going to", SUBJ_COLOR), (" + V", VERB_COLOR), (" ...?", GRAY)], w=750, h=36)

    add_section_title(svg, 20, 210, "Когда использовать / When to use")
    add_rule_box(svg, 20, 223, 370, 55, "1. Планы и намерения",
                 "I am going to study medicine. We are going to travel.")
    add_rule_box(svg, 410, 223, 370, 55, "2. Предсказания по признакам",
                 "Look at the clouds! It is going to rain.")

    # Comparison diagram
    add_section_title(svg, 20, 298, "Will vs Going to — разница / Difference")
    add_box(svg, 20, 310, 370, 100, fill=LIGHT_BLUE, stroke=BLUE, stroke_w=2, rx=6)
    add_text(svg, 30, 330, "WILL", size=16, color=BLUE, bold=True)
    add_text(svg, 30, 350, "• Спонтанное решение", size=12, color=BLACK)
    add_text(svg, 30, 368, "• Предсказание без доказательств", size=12, color=BLACK)
    add_text(svg, 30, 386, "• I'll answer the phone!", size=11, color=GRAY)

    add_box(svg, 410, 310, 370, 100, fill=LIGHT_GREEN, stroke=GREEN, stroke_w=2, rx=6)
    add_text(svg, 420, 330, "GOING TO", size=16, color=GREEN, bold=True)
    add_text(svg, 420, 350, "* Запланированное действие", size=12, color=BLACK)
    add_text(svg, 420, 368, "* Предсказание по признакам", size=12, color=BLACK)
    add_text(svg, 420, 386, "* I'm going to visit my grandma.", size=11, color=GRAY)

    add_section_title(svg, 20, 428, "Примеры / Examples")
    add_example_sentence(svg, 20, 450, "I am going to buy a new phone.", "Я собираюсь купить новый телефон.", 1)
    add_example_sentence(svg, 20, 480, "She isn't going to come.", "Она не собирается приходить.", 2)
    add_example_sentence(svg, 400, 450, "Are you going to study tonight?", "Ты собираешься учиться вечером?", 3)
    add_example_sentence(svg, 400, 480, "He is going to fix the car.", "Он собирается починить машину.", 4)

    add_rule_box(svg, 20, 518, 750, 45, "Запомни!",
                 "Going to всегда требует формуку глагола to be (am/is/are) и НЕ меняет V на V-ing!")

    add_footer(svg, 7)
    return svg

def lesson_08():
    """Modal Verbs: Can, Could, Must."""
    svg = svg_root()
    add_defs(svg)
    add_bg(svg)
    add_header(svg, "Modal Verbs: Can, Could, Must", "Модальные глаголы: возможность, разрешение, обязанность")

    add_section_title(svg, 20, 100, "Формула / Formation")
    add_grammar_formula(svg, 20, 112, [("S + ", SUBJ_COLOR), ("can/could/must", VERB_COLOR), (" + ", GRAY), ("V", RED), (" + ...", GRAY)], w=750, h=36)

    # Three columns
    # CAN
    add_box(svg, 20, 162, 245, 200, fill=LIGHT_BLUE, stroke=BLUE, stroke_w=2, rx=8)
    add_text(svg, 142, 185, "CAN", size=20, color=BLUE, anchor="middle", bold=True)
    add_text(svg, 142, 205, "могу, умею", size=12, color=GRAY, anchor="middle")
    add_text(svg, 30, 225, "• Ability (способность)", size=11, color=BLACK)
    add_text(svg, 30, 245, "  I can swim.", size=11, color=DARK_BLUE)
    add_text(svg, 30, 265, "• Permission (разрешение)", size=11, color=BLACK)
    add_text(svg, 30, 285, "  Can I go home?", size=11, color=DARK_BLUE)
    add_text(svg, 30, 305, "• Request (просьба)", size=11, color=BLACK)
    add_text(svg, 30, 325, "  Can you help me?", size=11, color=DARK_BLUE)
    add_text(svg, 30, 348, "Past: could", size=10, color=GRAY)

    # COULD
    add_box(svg, 278, 162, 245, 200, fill=LIGHT_YELLOW, stroke=ORANGE, stroke_w=2, rx=8)
    add_text(svg, 400, 185, "COULD", size=20, color=ORANGE, anchor="middle", bold=True)
    add_text(svg, 400, 205, "мог, мог бы", size=12, color=GRAY, anchor="middle")
    add_text(svg, 288, 225, "• Past ability (способность)", size=11, color=BLACK)
    add_text(svg, 288, 245, "  I could read at 5.", size=11, color=DARK_BLUE)
    add_text(svg, 288, 265, "• Polite request", size=11, color=BLACK)
    add_text(svg, 288, 285, "  Could you help me?", size=11, color=DARK_BLUE)
    add_text(svg, 288, 305, "• Possibility", size=11, color=BLACK)
    add_text(svg, 288, 325, "  It could be true.", size=11, color=DARK_BLUE)
    add_text(svg, 288, 348, "Более вежливая форма can", size=10, color=GRAY)

    # MUST
    add_box(svg, 536, 162, 245, 200, fill=LIGHT_RED, stroke=RED, stroke_w=2, rx=8)
    add_text(svg, 658, 185, "MUST", size=20, color=RED, anchor="middle", bold=True)
    add_text(svg, 658, 205, "должен, обязан", size=12, color=GRAY, anchor="middle")
    add_text(svg, 546, 225, "• Obligation (обязанность)", size=11, color=BLACK)
    add_text(svg, 546, 245, "  I must do homework.", size=11, color=DARK_BLUE)
    add_text(svg, 546, 265, "• Strong advice", size=11, color=BLACK)
    add_text(svg, 546, 285, "  You must see a doctor.", size=11, color=DARK_BLUE)
    add_text(svg, 546, 305, "• Prohibition (mustn't)", size=11, color=BLACK)
    add_text(svg, 546, 325, "  You mustn't smoke here.", size=11, color=DARK_BLUE)
    add_text(svg, 546, 348, "Mustn't = запрещено!", size=10, color=RED)

    add_section_title(svg, 20, 380, "Отрицание / Negative Forms")
    add_text(svg, 20, 400, "can → cannot (formal) / can't (informal)", size=13, color=BLACK)
    add_text(svg, 20, 420, "could → couldn't", size=13, color=BLACK)
    add_text(svg, 20, 440, "must → mustn't (= prohibition, НЕ «не обязан»)", size=13, color=RED, bold=True)
    add_text(svg, 20, 460, "Не обязан = don't have to / needn't", size=13, color=BLUE, bold=True)

    add_rule_box(svg, 20, 480, 750, 40, "Важно!",
                 "Модальные глаголы НЕ меняют форму (нет -s, -ed, -ing) и после них всегда V (без to)!")

    add_section_title(svg, 20, 535, "Примеры / Examples")
    add_example_sentence(svg, 20, 555, "She can speak three languages.", "Она может говорить на 3 языках.", 1)
    add_example_sentence(svg, 400, 555, "Must I wear a uniform? — Yes, you must.", "Я должен носить форму?", 2)

    add_footer(svg, 8)
    return svg

def lesson_09():
    """Modal Verbs: Should, May, Might."""
    svg = svg_root()
    add_defs(svg)
    add_bg(svg)
    add_header(svg, "Modal Verbs: Should, May, Might", "Модальные глаголы: совет, разрешение, возможность")

    add_section_title(svg, 20, 100, "Формула / Formation")
    add_grammar_formula(svg, 20, 112, [("S + ", SUBJ_COLOR), ("should/may/might", VERB_COLOR), (" + ", GRAY), ("V", RED), (" + ...", GRAY)], w=750, h=36)

    # Three columns
    # SHOULD
    add_box(svg, 20, 162, 245, 190, fill=LIGHT_GREEN, stroke=GREEN, stroke_w=2, rx=8)
    add_text(svg, 142, 185, "SHOULD", size=20, color=GREEN, anchor="middle", bold=True)
    add_text(svg, 142, 205, "следует, должен (совет)", size=11, color=GRAY, anchor="middle")
    add_text(svg, 30, 225, "• Advice (совет)", size=11, color=BLACK)
    add_text(svg, 30, 245, "  You should rest more.", size=11, color=DARK_BLUE)
    add_text(svg, 30, 265, "• Recommendation", size=11, color=BLACK)
    add_text(svg, 30, 285, "  She should see a doctor.", size=11, color=DARK_BLUE)
    add_text(svg, 30, 305, "• Opinion", size=11, color=BLACK)
    add_text(svg, 30, 325, "  We should leave now.", size=11, color=DARK_BLUE)
    add_text(svg, 30, 345, "Neg: shouldn't", size=10, color=GRAY)

    # MAY
    add_box(svg, 278, 162, 245, 190, fill=LIGHT_YELLOW, stroke=ORANGE, stroke_w=2, rx=8)
    add_text(svg, 400, 185, "MAY", size=20, color=ORANGE, anchor="middle", bold=True)
    add_text(svg, 400, 205, "может, возможно", size=11, color=GRAY, anchor="middle")
    add_text(svg, 288, 225, "• Permission (разрешение)", size=11, color=BLACK)
    add_text(svg, 288, 245, "  May I come in?", size=11, color=DARK_BLUE)
    add_text(svg, 288, 265, "• Possibility (50%)", size=11, color=BLACK)
    add_text(svg, 288, 285, "  It may rain today.", size=11, color=DARK_BLUE)
    add_text(svg, 288, 305, "• Formal permission", size=11, color=BLACK)
    add_text(svg, 288, 325, "  You may leave now.", size=11, color=DARK_BLUE)
    add_text(svg, 288, 345, "Более формальный than can", size=10, color=GRAY)

    # MIGHT
    add_box(svg, 536, 162, 245, 190, fill="#F3E8FF", stroke=PURPLE, stroke_w=2, rx=8)
    add_text(svg, 658, 185, "MIGHT", size=20, color=PURPLE, anchor="middle", bold=True)
    add_text(svg, 658, 205, "возможно (меньше %)", size=11, color=GRAY, anchor="middle")
    add_text(svg, 546, 225, "• Weak possibility (30%)", size=11, color=BLACK)
    add_text(svg, 546, 245, "  He might come later.", size=11, color=DARK_BLUE)
    add_text(svg, 546, 265, "• Polite suggestion", size=11, color=BLACK)
    add_text(svg, 546, 285, "  You might try again.", size=11, color=DARK_BLUE)
    add_text(svg, 546, 305, "• Past: might have + V3", size=11, color=BLACK)
    add_text(svg, 546, 325, "  She might have forgotten.", size=11, color=DARK_BLUE)
    add_text(svg, 546, 345, "Менее уверен, чем may", size=10, color=GRAY)

    add_section_title(svg, 20, 370, "Сравнение возможности / Possibility Comparison")
    add_text(svg, 20, 392, "must (95% уверены) → should (75%) → may (50%) → might (30%) → can't (0%)", size=13, color=DARK_BLUE, bold=True)

    # Visual bar chart
    bars = [("must", 95, RED), ("should", 75, ORANGE), ("may", 50, BLUE), ("might", 30, PURPLE), ("can't", 5, GRAY)]
    for i, (label, pct, color) in enumerate(bars):
        bx = 50 + i * 150
        bar_w = int(pct * 0.9)
        add_box(svg, bx, 410, bar_w, 20, fill=color, stroke=color, stroke_w=0, rx=3)
        add_text(svg, bx, 440, f"{label} ({pct}%)", size=10, color=color, bold=True)

    add_section_title(svg, 20, 465, "Примеры / Examples")
    add_example_sentence(svg, 20, 487, "You should eat more vegetables.", "Тебе следует есть больше овощей.", 1)
    add_example_sentence(svg, 20, 517, "May I use your phone?", "Можно воспользоваться твоим телефоном?", 2)
    add_example_sentence(svg, 400, 487, "It might snow tomorrow.", "Завтра, возможно, пойдёт снег.", 3)
    add_example_sentence(svg, 400, 517, "He shouldn't stay up late.", "Ему не следует ложиться поздно.", 4)

    add_footer(svg, 9)
    return svg

def lesson_10():
    """Passive Voice."""
    svg = svg_root()
    add_defs(svg)
    add_bg(svg)
    add_header(svg, "Passive Voice", "Пассивный залог")

    add_section_title(svg, 20, 100, "Формула / Formation")
    add_grammar_formula(svg, 20, 112, [("S + ", SUBJ_COLOR), ("be", VERB_COLOR), (" + ", GRAY), ("V3 (Past Participle)", RED), (" + ...", GRAY)], w=500, h=36)
    add_grammar_formula(svg, 540, 112, [("by + ", BLUE), ("agent", RED), (" (кем?)", GRAY)], w=230, h=36)

    add_section_title(svg, 20, 165, "Active vs Passive / Активный vs Пассивный")
    add_box(svg, 20, 178, 370, 65, fill=LIGHT_BLUE, stroke=BLUE, stroke_w=2, rx=6)
    add_text(svg, 30, 198, "ACTIVE: Subject performs action", size=12, color=BLUE, bold=True)
    add_text(svg, 30, 218, "Shakespeare wrote Hamlet.", size=13, color=DARK_BLUE)
    add_text(svg, 30, 234, "Шекспир написал Гамлета.", size=10, color=GRAY)

    add_box(svg, 410, 178, 370, 65, fill=LIGHT_RED, stroke=RED, stroke_w=2, rx=6)
    add_text(svg, 420, 198, "PASSIVE: Subject receives action", size=12, color=RED, bold=True)
    add_text(svg, 420, 218, "Hamlet was written by Shakespeare.", size=13, color=DARK_BLUE)
    add_text(svg, 420, 234, "Гамлет был написан Шекспиром.", size=10, color=GRAY)

    add_section_title(svg, 20, 260, "Таблица времён / Tenses in Passive")
    headers = ["Время", "Формула", "Пример"]
    rows = [
        ["Present Simple", "am/is/are + V3", "English is spoken worldwide."],
        ["Past Simple", "was/were + V3", "The letter was sent yesterday."],
        ["Future Simple", "will be + V3", "The project will be finished."],
        ["Present Perfect", "have/has been + V3", "The work has been done."],
        ["Present Continuous", "am/is/are being + V3", "The house is being built."],
        ["Modal Verbs", "modal + be + V3", "It must be done today."],
    ]
    add_table(svg, 20, 273, headers, rows, [155, 205, 330])

    add_section_title(svg, 20, 455, "Примеры / Examples")
    add_example_sentence(svg, 20, 477, "The book was published in 1999.", "Книга была опубликована в 1999.", 1)
    add_example_sentence(svg, 20, 507, "These cars are made in Germany.", "Эти машины сделаны в Германии.", 2)
    add_example_sentence(svg, 400, 477, "The window was broken by the boy.", "Окно было разбито мальчиком.", 3)
    add_example_sentence(svg, 400, 507, "The test will be checked tomorrow.", "Тест будет проверен завтра.", 4)

    add_rule_box(svg, 20, 540, 750, 35, "Когда использовать?",
                 "Когда важен объект, а не кто совершил действие / Когда исполнитель неизвестен")

    add_footer(svg, 10)
    return svg

def lesson_11():
    """Conditionals: Zero and First."""
    svg = svg_root()
    add_defs(svg)
    add_bg(svg)
    add_header(svg, "Conditionals: Zero & First", "Условные предложения: Нулевой и Первый тип")

    # Zero Conditional
    add_box(svg, 20, 85, 380, 230, fill=LIGHT_BLUE, stroke=BLUE, stroke_w=2, rx=8)
    add_text(svg, 210, 108, "ZERO CONDITIONAL", size=16, color=BLUE, anchor="middle", bold=True)
    add_text(svg, 210, 126, "Нулевое условное (общие истины)", size=11, color=GRAY, anchor="middle")

    add_grammar_formula(svg, 30, 138, [("If + ", RED), ("Present Simple", VERB_COLOR), (", ", GRAY), ("Present Simple", BLUE)], w=360, h=32)

    add_text(svg, 40, 188, "Условие (If)", size=12, color=RED, bold=True)
    add_text(svg, 40, 206, "If you heat water to 100°C,", size=12, color=DARK_BLUE)
    add_text(svg, 40, 224, "If people don't eat,", size=12, color=DARK_BLUE)
    add_text(svg, 220, 188, "Результат", size=12, color=BLUE, bold=True)
    add_text(svg, 220, 206, "it boils.", size=12, color=DARK_BLUE)
    add_text(svg, 220, 224, "they get hungry.", size=12, color=DARK_BLUE)

    add_text(svg, 40, 252, "= Когда/Если — всегда так!", size=11, color=GRAY)

    # First Conditional
    add_box(svg, 410, 85, 370, 230, fill=LIGHT_GREEN, stroke=GREEN, stroke_w=2, rx=8)
    add_text(svg, 595, 108, "FIRST CONDITIONAL", size=16, color=GREEN, anchor="middle", bold=True)
    add_text(svg, 595, 126, "Первое условное (реальные)", size=11, color=GRAY, anchor="middle")

    add_grammar_formula(svg, 420, 138, [("If + ", RED), ("Present Simple", VERB_COLOR), (", ", GRAY), ("Future Simple", BLUE)], w=350, h=32)

    add_text(svg, 430, 188, "Условие (If)", size=12, color=RED, bold=True)
    add_text(svg, 430, 206, "If it rains tomorrow,", size=12, color=DARK_BLUE)
    add_text(svg, 430, 224, "If you study hard,", size=12, color=DARK_BLUE)
    add_text(svg, 610, 188, "Результат", size=12, color=GREEN, bold=True)
    add_text(svg, 610, 206, "we will stay home.", size=12, color=DARK_BLUE)
    add_text(svg, 610, 224, "you will pass the exam.", size=12, color=DARK_BLUE)

    add_text(svg, 430, 252, "= Реальная возможность в будущем", size=11, color=GRAY)

    # Important rules
    add_section_title(svg, 20, 335, "Важные правила / Important Rules")
    add_rule_box(svg, 20, 348, 370, 50, "НЕ ставьте WILL после IF!",
                 "If it will rain — WRONG! / If it rains — CORRECT!")
    add_rule_box(svg, 410, 348, 370, 50, "Порядок частей можно менять",
                 "We will stay home if it rains. (без запятой)")

    # Examples
    add_section_title(svg, 20, 418, "Примеры / Examples")
    add_example_sentence(svg, 20, 440, "If you freeze water, it becomes ice.", "Если заморозить воду, она станет льдом. (Zero)", 1)
    add_example_sentence(svg, 20, 470, "If she calls, I will tell her.", "Если она позвонит, я ей скажу. (First)", 2)
    add_example_sentence(svg, 20, 500, "Plants die if they don't get water.", "Растения гибнут без воды. (Zero)", 3)
    add_example_sentence(svg, 400, 440, "If we hurry, we will catch the bus.", "Если поторопимся, успеем на автобус. (First)", 4)
    add_example_sentence(svg, 400, 470, "If you mix red and blue, you get purple.", "Если смешать красный и синий — фиолетовый. (Zero)", 5)

    add_footer(svg, 11)
    return svg

def lesson_12():
    """Conditionals: Second and Third."""
    svg = svg_root()
    add_defs(svg)
    add_bg(svg)
    add_header(svg, "Conditionals: Second & Third", "Условные предложения: Второй и Третий тип")

    # Second Conditional
    add_box(svg, 20, 85, 380, 215, fill=LIGHT_YELLOW, stroke=ORANGE, stroke_w=2, rx=8)
    add_text(svg, 210, 108, "SECOND CONDITIONAL", size=16, color=ORANGE, anchor="middle", bold=True)
    add_text(svg, 210, 126, "Нереальная ситуация в настоящем/будущем", size=10, color=GRAY, anchor="middle")

    add_grammar_formula(svg, 30, 138, [("If + ", RED), ("Past Simple", VERB_COLOR), (", ", GRAY), ("would + V", BLUE)], w=360, h=32)

    add_text(svg, 40, 188, "If I had a million dollars,", size=12, color=DARK_BLUE)
    add_text(svg, 40, 208, "I would buy a big house.", size=12, color=DARK_BLUE)
    add_text(svg, 40, 234, "Если бы у меня был миллион, я бы купил дом.", size=10, color=GRAY)
    add_text(svg, 40, 256, "(Но у меня нет миллиона — нереально!)", size=10, color=ORANGE)
    add_text(svg, 40, 278, "If I were you, I would apologize.", size=12, color=DARK_BLUE)
    add_text(svg, 40, 293, "(were для всех лиц в If!)", size=10, color=RED)

    # Third Conditional
    add_box(svg, 410, 85, 370, 215, fill=LIGHT_RED, stroke=RED, stroke_w=2, rx=8)
    add_text(svg, 595, 108, "THIRD CONDITIONAL", size=16, color=RED, anchor="middle", bold=True)
    add_text(svg, 595, 126, "Нереальная ситуация в прошлом (сожаление)", size=10, color=GRAY, anchor="middle")

    add_grammar_formula(svg, 420, 138, [("If + ", RED), ("Past Perfect", VERB_COLOR), (", ", GRAY), ("would have + V3", BLUE)], w=350, h=32)

    add_text(svg, 430, 188, "If I had studied harder,", size=12, color=DARK_BLUE)
    add_text(svg, 430, 208, "I would have passed the exam.", size=12, color=DARK_BLUE)
    add_text(svg, 430, 234, "Если бы я учился усерднее, я бы сдал экзамен.", size=10, color=GRAY)
    add_text(svg, 430, 256, "(Но уже поздно — прошлое не изменить!)", size=10, color=RED)
    add_text(svg, 430, 278, "If she had come, we would have won.", size=12, color=DARK_BLUE)
    add_text(svg, 430, 293, "(Она не пришла, и мы не выиграли)", size=10, color=GRAY)

    # Comparison table
    add_section_title(svg, 20, 315, "Сравнение всех типов / Comparison")
    headers = ["Тип", "Условие (If)", "Результат", "Реальность"]
    rows = [
        ["Zero", "Present", "Present", "100% реально"],
        ["First", "Present", "Future (will)", "Возможно"],
        ["Second", "Past", "would + V", "Нереально сейчас"],
        ["Third", "Past Perfect", "would have + V3", "Нереально в прошлом"],
    ]
    add_table(svg, 20, 328, headers, rows, [80, 175, 195, 240])

    add_section_title(svg, 20, 450, "Примеры / Examples")
    add_example_sentence(svg, 20, 472, "If I were rich, I would travel the world.", "Если бы я был богат, я бы путешествовал. (2nd)", 1)
    add_example_sentence(svg, 20, 502, "If he had driven carefully, he wouldn't have crashed.", "Если бы он ехал осторожно... (3rd)", 2)
    add_example_sentence(svg, 400, 472, "If she knew his number, she would call.", "Если бы она знала номер... (2nd)", 3)
    add_example_sentence(svg, 400, 502, "If we had left earlier, we would have caught the train.", "Если бы мы вышли раньше... (3rd)", 4)

    add_footer(svg, 12)
    return svg

def lesson_13():
    """Daily Routine."""
    svg = svg_root()
    add_defs(svg)
    add_bg(svg)
    add_header(svg, "Daily Routine", "Распорядок дня — лексика и фразы")

    add_section_title(svg, 20, 100, "Утро / Morning")
    morning = [("wake up", "просыпаться"), ("get up", "вставать"), ("brush teeth", "чистить зубы"),
               ("take a shower", "принимать душ"), ("have breakfast", "завтракать"), ("get dressed", "одеваться"),
               ("leave home", "выходить из дома"), ("go to school", "идти в школу")]
    for i, (en, ru) in enumerate(morning):
        x = 20 + (i % 4) * 190
        y = 112 + (i // 4) * 42
        add_box(svg, x, y, 180, 36, fill=LIGHT_YELLOW, stroke=ORANGE, stroke_w=1, rx=6)
        add_text(svg, x + 90, y + 15, en, size=12, color=DARK_BLUE, anchor="middle", bold=True)
        add_text(svg, x + 90, y + 30, ru, size=9, color=GRAY, anchor="middle")

    add_section_title(svg, 20, 205, "День / Afternoon")
    afternoon = [("have lunch", "обедать"), ("attend classes", "посещать уроки"), ("do homework", "делать дом. задание"),
                 ("have a snack", "перекусить"), ("go to the library", "идти в библиотеку"), ("study", "учиться"),
                 ("meet friends", "встречать друзей"), ("play sports", "заниматься спортом")]
    for i, (en, ru) in enumerate(afternoon):
        x = 20 + (i % 4) * 190
        y = 217 + (i // 4) * 42
        add_box(svg, x, y, 180, 36, fill=LIGHT_BLUE, stroke=BLUE, stroke_w=1, rx=6)
        add_text(svg, x + 90, y + 15, en, size=12, color=DARK_BLUE, anchor="middle", bold=True)
        add_text(svg, x + 90, y + 30, ru, size=9, color=GRAY, anchor="middle")

    add_section_title(svg, 20, 310, "Вечер / Evening & Night")
    evening = [("have dinner", "ужинать"), ("watch TV", "смотреть ТВ"), ("read a book", "читать книгу"),
               ("take a bath", "принять ванну"), ("go to bed", "ложиться спать"), ("fall asleep", "засыпать"),
               ("set the alarm", "поставить будильник"), ("chat online", "общаться онлайн")]
    for i, (en, ru) in enumerate(evening):
        x = 20 + (i % 4) * 190
        y = 322 + (i // 4) * 42
        add_box(svg, x, y, 180, 36, fill="#E0E7FF", stroke="#6366F1", stroke_w=1, rx=6)
        add_text(svg, x + 90, y + 15, en, size=12, color=DARK_BLUE, anchor="middle", bold=True)
        add_text(svg, x + 90, y + 30, ru, size=9, color=GRAY, anchor="middle")

    add_section_title(svg, 20, 415, "Полезные фразы / Useful Phrases")
    add_text(svg, 20, 438, "I usually wake up at 7 am.", size=13, color=DARK_BLUE)
    add_text(svg, 20, 456, "Я обычно просыпаюсь в 7 утра.", size=10, color=GRAY)
    add_text(svg, 400, 438, "After school, I do my homework.", size=13, color=DARK_BLUE)
    add_text(svg, 400, 456, "После школы я делаю домашнее задание.", size=10, color=GRAY)
    add_text(svg, 20, 478, "Before going to bed, I read for 30 min.", size=13, color=DARK_BLUE)
    add_text(svg, 20, 496, "Перед сном я читаю 30 минут.", size=10, color=GRAY)
    add_text(svg, 400, 478, "My day starts early and ends late.", size=13, color=DARK_BLUE)
    add_text(svg, 400, 496, "Мой день начинается рано и заканчивается поздно.", size=10, color=GRAY)

    add_rule_box(svg, 20, 520, 750, 45, "Время суток / Time of Day",
                 "in the morning / in the afternoon / in the evening / at night / at noon / at midnight")

    add_footer(svg, 13)
    return svg

def lesson_14():
    """Hobbies and Free Time."""
    svg = svg_root()
    add_defs(svg)
    add_bg(svg)
    add_header(svg, "Hobbies & Free Time", "Хобби и свободное время — лексика и фразы")

    add_section_title(svg, 20, 100, "Виды хобби / Types of Hobbies")
    categories = [
        ("Спорт / Sport", ["play football", "go swimming", "ride a bike", "do yoga"], LIGHT_GREEN, GREEN),
        ("Творчество / Creative", ["draw & paint", "play the guitar", "write stories", "take photos"], LIGHT_YELLOW, ORANGE),
        ("Интеллектуальные", ["read books", "solve puzzles", "play chess", "learn languages"], LIGHT_BLUE, BLUE),
        ("Социальные / Social", ["hang out with friends", "chat online", "go shopping", "watch movies"], "#E0E7FF", "#6366F1"),
    ]
    y_pos = 112
    for cat_name, items, bg, border in categories:
        add_box(svg, 20, y_pos, 760, 38, fill=bg, stroke=border, stroke_w=1, rx=6)
        add_text(svg, 30, y_pos + 15, cat_name, size=12, color=border, bold=True)
        add_text(svg, 200, y_pos + 24, "  |  ".join(items), size=11, color=DARK_BLUE)
        y_pos += 44

    add_section_title(svg, 20, 295, "Фразы для описания хобби / Phrases")
    phrases_headers = ["Английский", "Русский"]
    phrases_rows = [
        ["I'm interested in...", "Я интересуюсь..."],
        ["I'm fond of...", "Я увлекаюсь..."],
        ["I enjoy + V-ing", "Мне нравится..."],
        ["I'm good at + V-ing", "Я хорош в..."],
        ["My hobby is...", "Моё хобби — ..."],
        ["In my free time, I...", "В свободное время я..."],
        ["I spend time + V-ing", "Я провожу время..."],
        ["I'm keen on...", "Я увлечён..."],
    ]
    add_table(svg, 20, 308, phrases_headers, phrases_rows, [350, 330])

    add_section_title(svg, 20, 545, "Примеры / Examples")
    add_example_sentence(svg, 20, 568, "I enjoy playing basketball after school.", "Мне нравится играть в баскетбол после школы.", 1)
    add_example_sentence(svg, 400, 568, "She is fond of drawing landscapes.", "Она увлекается рисованием пейзажей.", 2)

    add_footer(svg, 14)
    return svg

def lesson_15():
    """Reading Strategies."""
    svg = svg_root()
    add_defs(svg)
    add_bg(svg)
    add_header(svg, "Reading Strategies", "Стратегии чтения — skimming, scanning, intensive")

    # Three strategy columns
    # Skimming
    add_box(svg, 20, 85, 245, 240, fill=LIGHT_BLUE, stroke=BLUE, stroke_w=2, rx=8)
    add_text(svg, 142, 108, "SKIMMING", size=18, color=BLUE, anchor="middle", bold=True)
    add_text(svg, 142, 126, "Просмотровое чтение", size=10, color=GRAY, anchor="middle")

    add_text(svg, 30, 148, "Цель: Общее понимание", size=11, color=BLACK, bold=True)
    add_text(svg, 30, 166, "Get the gist / main idea", size=10, color=GRAY)
    add_text(svg, 30, 188, "Как:", size=11, color=BLUE, bold=True)
    add_text(svg, 30, 206, "* Read title & headings", size=11, color=DARK_BLUE)
    add_text(svg, 30, 222, "* Read first & last paragraphs", size=11, color=DARK_BLUE)
    add_text(svg, 30, 238, "* Read first sentence of each", size=11, color=DARK_BLUE)
    add_text(svg, 30, 254, "  paragraph (topic sentence)", size=11, color=DARK_BLUE)
    add_text(svg, 30, 274, "Скорость: Быстро!", size=10, color=BLUE, bold=True)
    add_text(svg, 30, 292, "~300+ words/min", size=10, color=GRAY)

    # Scanning
    add_box(svg, 278, 85, 245, 240, fill=LIGHT_GREEN, stroke=GREEN, stroke_w=2, rx=8)
    add_text(svg, 400, 108, "SCANNING", size=18, color=GREEN, anchor="middle", bold=True)
    add_text(svg, 400, 126, "Поисковое чтение", size=10, color=GRAY, anchor="middle")

    add_text(svg, 288, 148, "Цель: Найти конкретную инфо", size=11, color=BLACK, bold=True)
    add_text(svg, 288, 166, "Find specific information", size=10, color=GRAY)
    add_text(svg, 288, 188, "Как:", size=11, color=GREEN, bold=True)
    add_text(svg, 288, 206, "* Know what you're looking for", size=11, color=DARK_BLUE)
    add_text(svg, 288, 222, "* Don't read every word", size=11, color=DARK_BLUE)
    add_text(svg, 288, 238, "* Look for keywords, names,", size=11, color=DARK_BLUE)
    add_text(svg, 288, 254, "  dates, numbers", size=11, color=DARK_BLUE)
    add_text(svg, 288, 274, "Скорость: Очень быстро!", size=10, color=GREEN, bold=True)
    add_text(svg, 288, 292, "~500+ words/min", size=10, color=GRAY)

    # Intensive
    add_box(svg, 536, 85, 245, 240, fill=LIGHT_RED, stroke=RED, stroke_w=2, rx=8)
    add_text(svg, 658, 108, "INTENSIVE", size=18, color=RED, anchor="middle", bold=True)
    add_text(svg, 658, 126, "Изучающее чтение", size=10, color=GRAY, anchor="middle")

    add_text(svg, 546, 148, "Цель: Полное понимание", size=11, color=BLACK, bold=True)
    add_text(svg, 546, 166, "Detailed comprehension", size=10, color=GRAY)
    add_text(svg, 546, 188, "Как:", size=11, color=RED, bold=True)
    add_text(svg, 546, 206, "* Read every word carefully", size=11, color=DARK_BLUE)
    add_text(svg, 546, 222, "* Understand grammar & vocab", size=11, color=DARK_BLUE)
    add_text(svg, 546, 238, "* Take notes, underline", size=11, color=DARK_BLUE)
    add_text(svg, 546, 254, "* Look up unknown words", size=11, color=DARK_BLUE)
    add_text(svg, 546, 274, "Скорость: Медленно", size=10, color=RED, bold=True)
    add_text(svg, 546, 292, "~50-100 words/min", size=10, color=GRAY)

    # Tips section
    add_section_title(svg, 20, 345, "Советы для эффективного чтения / Reading Tips")
    tips = [
        "1. Before reading: Look at the title, headings, images — predict the content.",
        "2. While reading: Highlight unknown words, but don't stop at every word.",
        "3. After reading: Summarize the main idea in your own words.",
        "4. Use context clues to guess meaning of new words.",
        "5. Read regularly — 15-20 minutes every day in English!",
        "6. Choose texts at your level — not too easy, not too hard.",
    ]
    for i, tip in enumerate(tips):
        y = 362 + i * 24
        bg = LIGHT_YELLOW if i % 2 == 0 else WHITE
        add_box(svg, 20, y - 12, 760, 22, fill=bg, stroke="#CBD5E1", stroke_w=1, rx=4)
        add_text(svg, 30, y + 2, tip, size=11, color=DARK_BLUE)

    add_section_title(svg, 20, 520, "Когда какую стратегию? / Which Strategy?")
    add_text(svg, 20, 542, "Skimming: newspaper article, book review, brochure", size=12, color=BLUE)
    add_text(svg, 20, 560, "Scanning: timetable, dictionary, phone book, menu", size=12, color=GREEN)
    add_text(svg, 20, 578, "Intensive: textbook, exam text, legal document, poem", size=12, color=RED)

    add_footer(svg, 15)
    return svg


# ===================== MAIN =====================

generators = [
    lesson_01, lesson_02, lesson_03, lesson_04, lesson_05,
    lesson_06, lesson_07, lesson_08, lesson_09, lesson_10,
    lesson_11, lesson_12, lesson_13, lesson_14, lesson_15,
]

results = []
for i, gen in enumerate(generators, 1):
    svg = gen()
    filepath = os.path.join(OUTPUT_DIR, f"lesson-{i}.svg")

    # Validate: write to string and parse back
    xml_str = ET.tostring(svg, encoding="unicode", xml_declaration=True)

    # Validate by parsing
    try:
        ET.fromstring(xml_str)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(xml_str)
        file_size = os.path.getsize(filepath)
        results.append(f"Lesson {i:2d}: OK ({file_size:,} bytes) → lesson-{i}.svg")
    except ET.ParseError as e:
        results.append(f"Lesson {i:2d}: XML ERROR — {e}")

print("=" * 60)
print("GRADE 8 ENGLISH SVG GENERATION RESULTS")
print("=" * 60)
for r in results:
    print(r)
print("=" * 60)
print(f"Total: {len(results)} files processed")
ok = sum(1 for r in results if "OK" in r)
print(f"Success: {ok}/{len(results)}")
