#!/usr/bin/env python3
"""
Generate 12 detailed SVG files for Grade 10 Philosophy lessons.
Color scheme: deep purple (#4A148C) primary, (#F3E5F5) bg gradient top, white bottom.
"""

import xml.etree.ElementTree as ET
import os
import html

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade10/philosophy"

# ── Color constants ──
PRIMARY = "#4A148C"
PRIMARY_LIGHT = "#7B1FA2"
PRIMARY_MED = "#9C27B0"
BG_TOP = "#F3E5F5"
BG_BOT = "#FFFFFF"
ACCENT = "#CE93D8"
DARK_TEXT = "#311B92"
SUBTITLE_COLOR = "#666666"
WHITE = "#FFFFFF"
BOX_BG = "#F3E5F5"
BOX_BORDER = "#CE93D8"

NS = "http://www.w3.org/2000/svg"


def _escape(text):
    return html.escape(text, quote=True)


def make_svg(lesson_num, title, content_fn):
    """Build an SVG with standard frame and lesson-specific content."""
    svg = ET.Element("svg", xmlns=NS, viewBox="0 0 500 350")

    # ── Defs ──
    defs = ET.SubElement(svg, "defs")

    grad = ET.SubElement(defs, "linearGradient", id="bg", x1="0", y1="0", x2="0", y2="1")
    ET.SubElement(grad, "stop", offset="0%", stopColor=BG_TOP)
    ET.SubElement(grad, "stop", offset="100%", stopColor=BG_BOT)

    grad2 = ET.SubElement(defs if defs is not None else svg, "linearGradient", id="panel", x1="0", y1="0", x2="1", y2="0")
    ET.SubElement(grad2, "stop", offset="0%", stopColor=PRIMARY_LIGHT)
    ET.SubElement(grad2, "stop", offset="100%", stopColor=PRIMARY)

    grad3 = ET.SubElement(defs, "linearGradient", id="headerGrad", x1="0", y1="0", x2="1", y2="0")
    ET.SubElement(grad3, "stop", offset="0%", stopColor=PRIMARY)
    ET.SubElement(grad3, "stop", offset="100%", stopColor=PRIMARY_LIGHT)

    # ── Background ──
    ET.SubElement(svg, "rect", width="500", height="350", fill="url(#bg)", rx="10")

    # ── Border ──
    ET.SubElement(svg, "rect", x="3", y="3", width="494", height="344",
                  rx="8", fill="none", stroke=PRIMARY, strokeWidth="2.5")

    # ── Inner decorative border ──
    ET.SubElement(svg, "rect", x="8", y="8", width="484", height="334",
                  rx="6", fill="none", stroke=PRIMARY, strokeWidth="1", opacity="0.15")

    # ── Corner decorations ──
    for pts in [
        "10,10 30,10 10,30",
        "490,10 470,10 490,30",
        "10,340 30,340 10,320",
        "490,340 470,340 490,320"
    ]:
        ET.SubElement(svg, "polygon", points=pts, fill=PRIMARY, opacity="0.10")

    # ── Title ──
    ET.SubElement(svg, "text", x="250", y="42", fontFamily="Arial,sans-serif",
                  fontSize="20", fontWeight="bold", fill=PRIMARY,
                  textAnchor="middle").text = title

    # ── Subtitle ──
    ET.SubElement(svg, "text", x="250", y="62", fontFamily="Arial,sans-serif",
                  fontSize="11", fill=SUBTITLE_COLOR,
                  textAnchor="middle").text = f"Философия — Урок {lesson_num}"

    # ── Separator ──
    ET.SubElement(svg, "line", x1="30", y1="72", x2="470", y2="72",
                  stroke=PRIMARY, strokeWidth="2", opacity="0.20")
    ET.SubElement(svg, "rect", x="30", y="70", width="60", height="4",
                  fill=PRIMARY, opacity="0.15", rx="1")
    ET.SubElement(svg, "rect", x="410", y="70", width="60", height="4",
                  fill=PRIMARY_LIGHT, opacity="0.10", rx="1")

    # ── Content area clip ──
    clip = ET.SubElement(defs, "clipPath", id="ill")
    ET.SubElement(clip, "rect", x="15", y="80", width="470", height="220", rx="6")

    content_g = ET.SubElement(svg, "g", clipPath="url(#ill)")
    # Content background
    ET.SubElement(content_g, "rect", x="15", y="80", width="470", height="220",
                  fill=BG_TOP, opacity="0.35")

    # ── Lesson-specific content ──
    content_fn(content_g, lesson_num, title)

    # ── Footer ──
    ET.SubElement(svg, "rect", x="12", y="305", width="476", height="32",
                  rx="5", fill="url(#panel)")
    ET.SubElement(svg, "line", x1="20", y1="308", x2="20", y2="334",
                  stroke=ACCENT, strokeWidth="1.5", opacity="0.5")
    ET.SubElement(svg, "line", x1="480", y1="308", x2="480", y2="334",
                  stroke=ACCENT, strokeWidth="1.5", opacity="0.5")
    ET.SubElement(svg, "text", x="250", y="326", fontFamily="Arial,sans-serif",
                  fontSize="14", textAnchor="middle", fill=WHITE,
                  fontWeight="bold").text = "Философия · 10 класс"

    return svg


def add_box(g, x, y, w, h, title_text, body_lines, title_size="10", body_size="9"):
    """Add a styled box with title and body text."""
    ET.SubElement(g, "rect", x=str(x), y=str(y), width=str(w), height=str(h),
                  rx="5", fill=WHITE, stroke=BOX_BORDER, strokeWidth="1.2", opacity="0.95")
    # Title bar
    ET.SubElement(g, "rect", x=str(x), y=str(y), width=str(w), height="18",
                  rx="5", fill=PRIMARY, opacity="0.85")
    # Fix bottom corners of title bar
    ET.SubElement(g, "rect", x=str(x), y=str(y + 12), width=str(w), height="6",
                  fill=PRIMARY, opacity="0.85")
    ET.SubElement(g, "text", x=str(x + w // 2), y=str(y + 13),
                  fontFamily="Arial,sans-serif", fontSize=title_size,
                  fontWeight="bold", fill=WHITE, textAnchor="middle").text = title_text
    for i, line in enumerate(body_lines):
        ET.SubElement(g, "text", x=str(x + 8), y=str(y + 30 + i * 13),
                      fontFamily="Arial,sans-serif", fontSize=body_size,
                      fill=DARK_TEXT, textAnchor="start").text = line


def add_quote(g, x, y, w, text, author=""):
    """Add a styled quote block."""
    ET.SubElement(g, "rect", x=str(x), y=str(y), width=str(w), height="38",
                  rx="4", fill=PRIMARY, opacity="0.08")
    ET.SubElement(g, "line", x1=str(x + 4), y1=str(y + 4), x2=str(x + 4), y2=str(y + 34),
                  stroke=PRIMARY, strokeWidth="3", opacity="0.6")
    ET.SubElement(g, "text", x=str(x + 12), y=str(y + 14),
                  fontFamily="Georgia,serif", fontSize="8.5", fontStyle="italic",
                  fill=DARK_TEXT).text = f"\u201C{text}\u201D"
    if author:
        ET.SubElement(g, "text", x=str(x + w - 8), y=str(y + 30),
                      fontFamily="Arial,sans-serif", fontSize="8", fill=PRIMARY_LIGHT,
                      textAnchor="end").text = f"\u2014 {author}"


def add_circle_icon(g, cx, cy, r, symbol, fill_color=PRIMARY, opacity="0.12"):
    """Add a circle with a symbol inside."""
    ET.SubElement(g, "circle", cx=str(cx), cy=str(cy), r=str(r),
                  fill="none", stroke=fill_color, strokeWidth="1.5", opacity="0.5")
    ET.SubElement(g, "text", x=str(cx), y=str(cy + 5),
                  fontFamily="serif", fontSize=str(int(r * 1.2)),
                  fill=fill_color, textAnchor="middle").text = symbol


# ═══════════════════════════════════════════════════════════════
#  LESSON CONTENT GENERATORS
# ═══════════════════════════════════════════════════════════════

def lesson1_birth(g, num, title):
    """Рождение философии"""
    # Left: Definition box
    add_box(g, 20, 85, 225, 100, "ОПРЕДЕЛЕНИЕ", [
        "Философия (φιλοσοφία) —",
        "«любовь к мудрости»",
        "Наука о наиболее общих",
        "законах природы, общества",
        "и мышления"
    ])
    # Right: Key concepts box
    add_box(g, 255, 85, 225, 100, "КЛЮЧЕВЫЕ ПОНЯТИЯ", [
        "• Миф → Логос (переход)",
        "• Космоцентризм",
        "• Первоначала (архе)",
        "• Фалес: вода — основа",
        "• Гераклит: всё течёт"
    ])
    # Quote
    add_quote(g, 20, 195, 460, "Всё есть вода — начало всего", "Фалес Милетский")
    # Bottom: Timeline
    ET.SubElement(g, "rect", x="20", y="242", width="460", height="50", rx="5",
                  fill=WHITE, stroke=BOX_BORDER, strokeWidth="1")
    ET.SubElement(g, "text", x="250", y="256", fontFamily="Arial,sans-serif",
                  fontSize="9", fontWeight="bold", fill=PRIMARY, textAnchor="middle").text = "ХРОНОЛОГИЯ"
    # Timeline line
    ET.SubElement(g, "line", x1="40", y1="272", x2="460", y2="272",
                  stroke=PRIMARY, strokeWidth="1.5", opacity="0.4")
    for dx, label in [(40, "VII в."), (145, "VI в."), (250, "V в."), (355, "IV в.")]:
        ET.SubElement(g, "circle", cx=str(dx), cy="272", r="4", fill=PRIMARY, opacity="0.6")
        ET.SubElement(g, "text", x=str(dx), y="285", fontFamily="Arial,sans-serif",
                      fontSize="7.5", fill=DARK_TEXT, textAnchor="middle").text = label
    add_circle_icon(g, 475, 140, 16, "Φ")


def lesson2_socrates(g, num, title):
    """Сократ"""
    add_box(g, 20, 85, 225, 110, "СОКРАТ (469–399 до н.э.)", [
        "• Не написал ни одной книги",
        "• Майевтика — «повивальное",
        "  искусство» рождения истины",
        "• Ирония — признание незнания",
        "• Диалектика — поиск истины",
        "  через диалог"
    ])
    add_box(g, 255, 85, 225, 110, "МЕТОД СОКРАТА", [
        "1. Задать вопрос",
        "2. Опровергнуть ответ",
        "3. Поставить в тупик",
        "4. Помочь найти истину",
        "",
        "«Я знаю, что ничего не знаю»"
    ])
    add_quote(g, 20, 205, 460, "Непроверенная жизнь не стоит того, чтобы жить", "Сократ")
    # Bottom: Ethics box
    add_box(g, 20, 252, 460, 42, "ГЛАВНАЯ ИДЕЯ", [
        "Добродетель = Знание. Человек совершает зло не по злому умыслу, а по неведению."
    ], title_size="9", body_size="8.5")
    add_circle_icon(g, 475, 170, 14, "Σ")


def lesson3_plato(g, num, title):
    """Платон"""
    add_box(g, 20, 85, 225, 105, "ПЛАТОН (427–347 до н.э.)", [
        "• Ученик Сократа",
        "• Основатель Академии",
        "• 36 диалогов — жанр философии",
        "• Объективный идеализм",
        "• Мир идей (эйдосов)"
    ])
    add_box(g, 255, 85, 225, 105, "ТЕОРИЯ ИДЕЙ", [
        "Мир идей (истинный)",
        "    ↓ отражение",
        "Мир вещей (теневой)",
        "",
        "Притча о пещере:",
        "Тени на стене = наш мир"
    ])
    add_quote(g, 20, 200, 460, "Тело — темница души", "Платон")
    # Cave diagram
    ET.SubElement(g, "rect", x="20", y="248", width="460", height="46", rx="5",
                  fill=WHITE, stroke=BOX_BORDER, strokeWidth="1")
    ET.SubElement(g, "text", x="250", y="262", fontFamily="Arial,sans-serif",
                  fontSize="9", fontWeight="bold", fill=PRIMARY, textAnchor="middle").text = "ПРИТЧА О ПЕЩЕРЕ"
    # Simple cave illustration
    ET.SubElement(g, "rect", x="40", y="270", width="80", height="18", rx="3",
                  fill=PRIMARY, opacity="0.15")
    ET.SubElement(g, "text", x="80", y="283", fontFamily="Arial,sans-serif",
                  fontSize="7.5", fill=DARK_TEXT, textAnchor="middle").text = "Пещера"
    ET.SubElement(g, "text", x="140", y="283", fontFamily="Arial,sans-serif",
                  fontSize="10", fill=PRIMARY).text = "→"
    ET.SubElement(g, "rect", x="155", y="270", width="80", height="18", rx="3",
                  fill=PRIMARY, opacity="0.25")
    ET.SubElement(g, "text", x="195", y="283", fontFamily="Arial,sans-serif",
                  fontSize="7.5", fill=DARK_TEXT, textAnchor="middle").text = "Тени"
    ET.SubElement(g, "text", x="255", y="283", fontFamily="Arial,sans-serif",
                  fontSize="10", fill=PRIMARY).text = "→"
    ET.SubElement(g, "rect", x="270", y="270", width="80", height="18", rx="3",
                  fill=PRIMARY, opacity="0.4")
    ET.SubElement(g, "text", x="310", y="283", fontFamily="Arial,sans-serif",
                  fontSize="7.5", fill=DARK_TEXT, textAnchor="middle").text = "Свет"
    ET.SubElement(g, "text", x="370", y="283", fontFamily="Arial,sans-serif",
                  fontSize="10", fill=PRIMARY).text = "→"
    ET.SubElement(g, "rect", x="385", y="270", width="80", height="18", rx="3",
                  fill=PRIMARY, opacity="0.6")
    ET.SubElement(g, "text", x="425", y="283", fontFamily="Arial,sans-serif",
                  fontSize="7.5", fill=WHITE, textAnchor="middle").text = "Истина"
    add_circle_icon(g, 475, 160, 14, "Π")


def lesson4_aristotle(g, num, title):
    """Аристотель"""
    add_box(g, 20, 85, 225, 105, "АРИСТОТЕЛЬ (384–322 до н.э.)", [
        "• Ученик Платона",
        "• Воспитатель Александра М.",
        "• Основатель Ликея",
        "• Систематизатор наук",
        "• «Учитель тех, кто знает»"
    ])
    add_box(g, 255, 85, 225, 105, "КЛЮЧЕВЫЕ ИДЕИ", [
        "• Категории (10 видов бытия)",
        "• 4 причины: материальная,",
        "  формальная, действующая,",
        "  целевая",
        "• Золотая середина"
    ])
    add_quote(g, 20, 200, 460, "Платон мне друг, но истина дороже", "Аристотель")
    # Four causes diagram
    ET.SubElement(g, "rect", x="20", y="248", width="460", height="46", rx="5",
                  fill=WHITE, stroke=BOX_BORDER, strokeWidth="1")
    ET.SubElement(g, "text", x="250", y="262", fontFamily="Arial,sans-serif",
                  fontSize="9", fontWeight="bold", fill=PRIMARY, textAnchor="middle").text = "ЧЕТЫРЕ ПРИЧИНЫ (на примере статуи)"
    causes = [("Материя", "мрамор"), ("Форма", "образ"), ("Действие", "скульптор"), ("Цель", "красота")]
    for i, (name, ex) in enumerate(causes):
        bx = 35 + i * 115
        ET.SubElement(g, "rect", x=str(bx), y="268", width="105", height="22", rx="3",
                      fill=PRIMARY, opacity=str(0.15 + i * 0.1))
        ET.SubElement(g, "text", x=str(bx + 52), y="279", fontFamily="Arial,sans-serif",
                      fontSize="7.5", fill=DARK_TEXT, textAnchor="middle").text = f"{name}: {ex}"
    add_circle_icon(g, 475, 160, 14, "Α")


def lesson5_ethics(g, num, title):
    """Что такое этика"""
    add_box(g, 20, 85, 225, 105, "ОПРЕДЕЛЕНИЕ ЭТИКИ", [
        "Этика — философская",
        "дисциплина, изучающая",
        "мораль и нравственность",
        "",
        "От греч. ethos — обычай,",
        "характер, нрав"
    ])
    add_box(g, 255, 85, 225, 105, "СТРУКТУРА ЭТИКИ", [
        "• Дескриптивная — описывает",
        "  мораль разных эпох",
        "• Нормативная — задаёт",
        "  идеалы и правила",
        "• Метаэтика — анализирует",
        "  язык морали"
    ])
    add_quote(g, 20, 200, 460, "Действовать нравственно — значит действовать согласно разуму", "Спиноза")
    # Three pillars
    ET.SubElement(g, "rect", x="20", y="248", width="460", height="46", rx="5",
                  fill=WHITE, stroke=BOX_BORDER, strokeWidth="1")
    ET.SubElement(g, "text", x="250", y="262", fontFamily="Arial,sans-serif",
                  fontSize="9", fontWeight="bold", fill=PRIMARY, textAnchor="middle").text = "ТРИ СТОЛПА ЭТИКИ"
    pillars = [("Добро", "#4A148C"), ("Долг", "#7B1FA2"), ("Справедливость", "#9C27B0")]
    for i, (name, clr) in enumerate(pillars):
        bx = 60 + i * 145
        ET.SubElement(g, "rect", x=str(bx - 30), y="268", width="100", height="22", rx="3",
                      fill=clr, opacity="0.75")
        ET.SubElement(g, "text", x=str(bx + 20), y="283", fontFamily="Arial,sans-serif",
                      fontSize="9", fill=WHITE, textAnchor="middle", fontWeight="bold").text = name
    add_circle_icon(g, 475, 160, 14, "E")


def lesson6_virtue(g, num, title):
    """Добродетель и порок"""
    add_box(g, 20, 85, 225, 100, "ДОБРОДЕТЕЛЬ", [
        "Добродетель — устойчивое",
        "свойство личности,",
        "направленное на добро",
        "",
        "Кардинальные добродетели:",
        "Мудрость · Справедливость"
    ])
    add_box(g, 255, 85, 225, 100, "ПОРОК", [
        "Порок — устойчивое",
        "отклонение от моральной",
        "нормы, противоположность",
        "добродетели",
        "",
        "Семь смертных грехов"
    ])
    add_quote(g, 20, 195, 460, "Добродетель — это золотая середина между двумя крайностями", "Аристотель")
    # Spectrum diagram
    ET.SubElement(g, "rect", x="20", y="242", width="460", height="52", rx="5",
                  fill=WHITE, stroke=BOX_BORDER, strokeWidth="1")
    ET.SubElement(g, "text", x="250", y="256", fontFamily="Arial,sans-serif",
                  fontSize="9", fontWeight="bold", fill=PRIMARY, textAnchor="middle").text = "ЗОЛОТАЯ СЕРЕДИНА (мезотес)"
    # Spectrum
    ET.SubElement(g, "line", x1="50", y1="275", x2="450", y2="275",
                  stroke=PRIMARY, strokeWidth="2", opacity="0.3")
    # Deficiency
    ET.SubElement(g, "rect", x="50", y="268", width="90", height="14", rx="3",
                  fill="#FFCDD2", stroke="#EF5350", strokeWidth="0.8")
    ET.SubElement(g, "text", x="95", y="279", fontFamily="Arial,sans-serif",
                  fontSize="7.5", fill="#C62828", textAnchor="middle").text = "Недостаток"
    # Virtue
    ET.SubElement(g, "rect", x="185", y="265", width="130", height="20", rx="4",
                  fill="#C8E6C9", stroke=PRIMARY, strokeWidth="1.2")
    ET.SubElement(g, "text", x="250", y="279", fontFamily="Arial,sans-serif",
                  fontSize="9", fill=PRIMARY, textAnchor="middle", fontWeight="bold").text = "Добродетель ✓"
    # Excess
    ET.SubElement(g, "rect", x="360", y="268", width="90", height="14", rx="3",
                  fill="#FFCDD2", stroke="#EF5350", strokeWidth="0.8")
    ET.SubElement(g, "text", x="405", y="279", fontFamily="Arial,sans-serif",
                  fontSize="7.5", fill="#C62828", textAnchor="middle").text = "Избыток"
    add_circle_icon(g, 475, 160, 14, "Δ")


def lesson7_modern_ethics(g, num, title):
    """Современная этика"""
    add_box(g, 20, 85, 150, 105, "ДЕОНТОЛОГИЯ", [
        "Кант:",
      "Категорический",
        "императив —",
        "поступай по правилу,",
        "которое можешь",
        "считать законом"
    ])
    add_box(g, 178, 85, 150, 105, "УТИЛИТАРИЗМ", [
        "Бентам, Милль:",
        "Морально то, что",
        "приносит наибольшее",
        "счастье наибольшему",
        "числу людей"
    ])
    add_box(g, 336, 85, 145, 105, "ЭТИКА ДОБРОДЕТЕЛИ", [
        "Макинтайр:",
        "Возврат к Аристотелю",
        "Акцент на характере,",
        "а не на правилах",
        ""
    ])
    add_quote(g, 20, 200, 460, "Поступай только согласно такой максиме, которую ты желал бы видеть всеобщим законом", "И. Кант")
    # Comparison table
    ET.SubElement(g, "rect", x="20", y="248", width="460", height="46", rx="5",
                  fill=WHITE, stroke=BOX_BORDER, strokeWidth="1")
    ET.SubElement(g, "text", x="250", y="262", fontFamily="Arial,sans-serif",
                  fontSize="9", fontWeight="bold", fill=PRIMARY, textAnchor="middle").text = "ТРИ ПОДХОДА К МОРАЛИ"
    cols = [("Долг", "Кант"), ("Результат", "Милль"), ("Характер", "Аристотель")]
    for i, (approach, author) in enumerate(cols):
        bx = 55 + i * 155
        ET.SubElement(g, "rect", x=str(bx - 25), y="268", width="120", height="20", rx="3",
                      fill=PRIMARY, opacity=str(0.2 + i * 0.15))
        ET.SubElement(g, "text", x=str(bx + 35), y="282", fontFamily="Arial,sans-serif",
                      fontSize="8", fill=DARK_TEXT, textAnchor="middle").text = f"{approach} ({author})"


def lesson8_moral_choice(g, num, title):
    """Моральный выбор"""
    add_box(g, 20, 85, 225, 95, "МОРАЛЬНЫЙ ВЫБОР", [
        "Моральный выбор —",
        "сознательное предпочтение",
        "определённого варианта",
        "поведения в ситуации",
        "морального конфликта",
        ""
    ])
    add_box(g, 255, 85, 225, 95, "ДИЛЕММЫ", [
        "• Конфликт двух долгов",
        "• Личное vs общественное",
        "• Свобода vs ответственность",
        "• Цель vs средства",
        "",
        "«Трамвайная задача»"
    ])
    add_quote(g, 20, 190, 460, "Свобода — это то, что ты делаешь с тем, что сделали с тобой", "Сартр")
    # Decision tree
    ET.SubElement(g, "rect", x="20", y="238", width="460", height="56", rx="5",
                  fill=WHITE, stroke=BOX_BORDER, strokeWidth="1")
    ET.SubElement(g, "text", x="250", y="252", fontFamily="Arial,sans-serif",
                  fontSize="9", fontWeight="bold", fill=PRIMARY, textAnchor="middle").text = "СХЕМА МОРАЛЬНОГО ВЫБОРА"
    # Decision flow
    ET.SubElement(g, "rect", x="170", y="258", width="160", height="16", rx="3",
                  fill=PRIMARY, opacity="0.2")
    ET.SubElement(g, "text", x="250", y="270", fontFamily="Arial,sans-serif",
                  fontSize="7.5", fill=DARK_TEXT, textAnchor="middle").text = "Моральная дилемма"
    # Branches
    ET.SubElement(g, "line", x1="210", y1="274", x2="140", y2="286",
                  stroke=PRIMARY, strokeWidth="1", opacity="0.5")
    ET.SubElement(g, "line", x1="290", y1="274", x2="360", y2="286",
                  stroke=PRIMARY, strokeWidth="1", opacity="0.5")
    ET.SubElement(g, "rect", x="80", y="283", width="120", height="10", rx="2",
                  fill="#C8E6C9", stroke=PRIMARY, strokeWidth="0.5")
    ET.SubElement(g, "text", x="140", y="291", fontFamily="Arial,sans-serif",
                  fontSize="6.5", fill=DARK_TEXT, textAnchor="middle").text = "Вариант А (долг)"
    ET.SubElement(g, "rect", x="300", y="283", width="120", height="10", rx="2",
                  fill="#FFCDD2", stroke=PRIMARY, strokeWidth="0.5")
    ET.SubElement(g, "text", x="360", y="291", fontFamily="Arial,sans-serif",
                  fontSize="6.5", fill=DARK_TEXT, textAnchor="middle").text = "Вариант Б (сочувствие)"


def lesson9_modern_phil(g, num, title):
    """Философия Нового времени"""
    add_box(g, 20, 85, 150, 110, "РАЦИОНАЛИЗМ", [
        "Декарт:",
        "«Cogito, ergo sum»",
        "(Мыслю, значит существую)",
        "",
        "Идеи врождены,",
        "разум — источник",
        "знания"
    ])
    add_box(g, 178, 85, 150, 110, "ЭМПИРИЗМ", [
        "Локк, Юм:",
        "«Tabula rasa» —",
        "чистая доска",
        "",
        "Опыт — источник",
        "знания, идеи",
        "приобретены"
    ])
    add_box(g, 336, 85, 145, 110, "КАНТ", [
        "Синтез двух",
        "подходов:",
        "",
        "Опыт без понятий",
        "слеп, понятия без",
        "опыта пусты",
        ""
    ])
    add_quote(g, 20, 205, 460, "Имей мужество пользоваться собственным умом!", "И. Кант")
    # Timeline
    ET.SubElement(g, "rect", x="20", y="252", width="460", height="42", rx="5",
                  fill=WHITE, stroke=BOX_BORDER, strokeWidth="1")
    ET.SubElement(g, "text", x="250", y="266", fontFamily="Arial,sans-serif",
                  fontSize="9", fontWeight="bold", fill=PRIMARY, textAnchor="middle").text = "ЭПОХА НОВОГО ВРЕМЕНИ (XVII–XVIII вв.)"
    ET.SubElement(g, "line", x1="40", y1="280", x2="460", y2="280",
                  stroke=PRIMARY, strokeWidth="1.5", opacity="0.3")
    for dx, lbl in [(50, "Декарт 1596"), (160, "Спиноза 1632"), (270, "Локк 1632"), (380, "Кант 1724")]:
        ET.SubElement(g, "circle", cx=str(dx), cy="280", r="3", fill=PRIMARY, opacity="0.6")
        ET.SubElement(g, "text", x=str(dx), y="291", fontFamily="Arial,sans-serif",
                      fontSize="6.5", fill=DARK_TEXT, textAnchor="middle").text = lbl


def lesson10_existentialism(g, num, title):
    """Экзистенциализм"""
    add_box(g, 20, 85, 225, 110, "ЭКЗИСТЕНЦИАЛИЗМ", [
        "От лат. existentia —",
        "существование",
        "",
        "• Существование",
        "  предшествует сущности",
        "• Человек сам создаёт себя",
        "• Свобода = ответственность"
    ])
    add_box(g, 255, 85, 225, 110, "КЛЮЧЕВЫЕ ФИГУРЫ", [
        "• Кьеркегор — «отец»",
        "• Хайдеггер — Бытие",
        "• Сартр — свобода",
        "• Камю — абсурд",
        "• Ясперс — пограничная",
        "  ситуация",
        ""
    ])
    add_quote(g, 20, 205, 460, "Человек обречён быть свободным", "Ж.-П. Сартр")
    # Core concepts
    ET.SubElement(g, "rect", x="20", y="252", width="460", height="42", rx="5",
                  fill=WHITE, stroke=BOX_BORDER, strokeWidth="1")
    ET.SubElement(g, "text", x="250", y="266", fontFamily="Arial,sans-serif",
                  fontSize="9", fontWeight="bold", fill=PRIMARY, textAnchor="middle").text = "ОСНОВНЫЕ КАТЕГОРИИ"
    concepts = ["Абсурд", "Тревога", "Свобода", "Ответственность", "Подлинность"]
    for i, c in enumerate(concepts):
        cx = 50 + i * 90
        ET.SubElement(g, "rect", x=str(cx), y="272", width="80", height="16", rx="8",
                      fill=PRIMARY, opacity=str(0.15 + i * 0.07))
        ET.SubElement(g, "text", x=str(cx + 40), y="284", fontFamily="Arial,sans-serif",
                      fontSize="7.5", fill=DARK_TEXT, textAnchor="middle").text = c


def lesson11_phil_of_science(g, num, title):
    """Философия науки"""
    add_box(g, 20, 85, 225, 100, "ЧТО ТАКОЕ НАУКА?", [
        "Наука — система знаний,",
        "основанная на методе",
        "",
        "Критерии научности:",
        "• Объективность",
        "• Проверяемость (Поппер)",
        "• Системность"
    ])
    add_box(g, 255, 85, 225, 100, "ФИЛОСОФЫ НАУКИ", [
        "• Поппер — фальсификация",
        "• Кун — парадигмы и",
        "  научные революции",
        "• Лакатос — программа",
        "• Фейерабенд — «всё",
        "  годится» (эпистемологич."
    ])
    add_quote(g, 20, 195, 460, "Научная теория должна быть фальсифицируема", "К. Поппер")
    # Paradigm shift diagram
    ET.SubElement(g, "rect", x="20", y="242", width="460", height="52", rx="5",
                  fill=WHITE, stroke=BOX_BORDER, strokeWidth="1")
    ET.SubElement(g, "text", x="250", y="256", fontFamily="Arial,sans-serif",
                  fontSize="9", fontWeight="bold", fill=PRIMARY, textAnchor="middle").text = "СМЕНА ПАРАДИГМ (по Куну)"
    stages = [
        ("Нормальная\nнаука", 0.15),
        ("Аномалии", 0.25),
        ("Кризис", 0.4),
        ("Революция", 0.55),
        ("Новая\nпарадигма", 0.7)
    ]
    for i, (name, op) in enumerate(stages):
        bx = 30 + i * 92
        ET.SubElement(g, "rect", x=str(bx), y="263", width="82", height="24", rx="3",
                      fill=PRIMARY, opacity=str(op))
        color = WHITE if op > 0.45 else DARK_TEXT
        ET.SubElement(g, "text", x=str(bx + 41), y="278", fontFamily="Arial,sans-serif",
                      fontSize="7", fill=color, textAnchor="middle").text = name.replace("\n", " ")
        if i < len(stages) - 1:
            ET.SubElement(g, "text", x=str(bx + 86), y="278", fontFamily="Arial,sans-serif",
                          fontSize="9", fill=PRIMARY).text = "→"


def lesson12_phil_and_life(g, num, title):
    """Философия и жизнь"""
    add_box(g, 20, 85, 225, 100, "ФИЛОСОФИЯ В ЖИЗНИ", [
        "Философия — не абстракция,",
        "а способ осмысления",
        "собственного бытия",
        "",
        "• Смысл жизни",
        "• Свобода воли"
    ])
    add_box(g, 255, 85, 225, 100, "СМЫСЛ ЖИЗНИ", [
        "• Фромм: любовь и труд",
        "• Франкл: поиск смысла",
        "  даже в страдании",
        "• Камю: бунт против",
        "  абсурда",
        "• Толстой: служение добру"
    ])
    add_quote(g, 20, 195, 460, "Тот, кто знает зачем жить, может выдержать почти любое как", "Ф. Ницше")
    # Life areas
    ET.SubElement(g, "rect", x="20", y="242", width="460", height="52", rx="5",
                  fill=WHITE, stroke=BOX_BORDER, strokeWidth="1")
    ET.SubElement(g, "text", x="250", y="256", fontFamily="Arial,sans-serif",
                  fontSize="9", fontWeight="bold", fill=PRIMARY, textAnchor="middle").text = "ФИЛОСОФИЯ ОТВЕЧАЕТ НА ВОПРОСЫ"
    questions = ["Кто я?", "Зачем живу?", "Что есть добро?", "Свободен ли я?", "В чём истина?"]
    for i, q in enumerate(questions):
        cx = 30 + i * 90
        ET.SubElement(g, "rect", x=str(cx), y="264", width="82", height="24", rx="12",
                      fill=PRIMARY, opacity=str(0.15 + i * 0.08))
        ET.SubElement(g, "text", x=str(cx + 41), y="280", fontFamily="Arial,sans-serif",
                      fontSize="7.5", fill=DARK_TEXT, textAnchor="middle", fontWeight="bold").text = q


# ═══════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════

LESSONS = [
    (1, "Рождение философии", lesson1_birth),
    (2, "Сократ", lesson2_socrates),
    (3, "Платон", lesson3_plato),
    (4, "Аристотель", lesson4_aristotle),
    (5, "Что такое этика", lesson5_ethics),
    (6, "Добродетель и порок", lesson6_virtue),
    (7, "Современная этика", lesson7_modern_ethics),
    (8, "Моральный выбор", lesson8_moral_choice),
    (9, "Философия Нового времени", lesson9_modern_phil),
    (10, "Экзистенциализм", lesson10_existentialism),
    (11, "Философия науки", lesson11_phil_of_science),
    (12, "Философия и жизнь", lesson12_phil_and_life),
]

os.makedirs(OUTPUT_DIR, exist_ok=True)

valid_count = 0
invalid_count = 0

for num, title, content_fn in LESSONS:
    svg = make_svg(num, title, content_fn)
    filepath = os.path.join(OUTPUT_DIR, f"lesson{num}.svg")

    # Write with proper XML declaration
    tree = ET.ElementTree(svg)
    ET.indent(tree, space="  ")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        tree.write(f, encoding="unicode", xml_declaration=False)

    # Validate
    try:
        tree2 = ET.parse(filepath)
        root = tree2.getroot()
        assert root.tag == f"{{{NS}}}svg" or root.tag == "svg"
        valid_count += 1
        print(f"✓ lesson{num}.svg — {title}")
    except ET.ParseError as e:
        invalid_count += 1
        print(f"✗ lesson{num}.svg — INVALID XML: {e}")

print(f"\n{'='*50}")
print(f"Total generated: {len(LESSONS)}")
print(f"Valid XML: {valid_count}")
print(f"Invalid XML: {invalid_count}")
print(f"Output dir: {OUTPUT_DIR}")
