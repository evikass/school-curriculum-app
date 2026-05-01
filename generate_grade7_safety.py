#!/usr/bin/env python3
"""Generate educational SVG images for Grade 7 Safety/Life Safety (ОБЖ) lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/safety"
W, H = 800, 600

# Color scheme
ORANGE = "#EA580C"
DANGER = "#DC2626"
DARK = "#1C1917"
WHITE = "#FFFFFF"
LIGHT_BG = "#FFF7ED"
ORANGE_LIGHT = "#FED7AA"
ORANGE_MID = "#FB923C"
GRAY = "#78716C"
GRAY_LIGHT = "#D6D3D1"
YELLOW_WARN = "#FBBF24"
GREEN = "#16A34A"
BLUE = "#2563EB"
DARK_ORANGE = "#C2410C"


def escape_xml(text):
    """Escape text for XML attributes and content."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def svg_header(title):
    """Return the SVG root element with namespaces and basic defs."""
    svg = ET.Element("svg")
    svg.set("xmlns", "http://www.w3.org/2000/svg")
    svg.set("width", str(W))
    svg.set("height", str(H))
    svg.set("viewBox", f"0 0 {W} {H}")

    # Defs for gradients and filters
    defs = ET.SubElement(svg, "defs")

    # Background gradient
    grad = ET.SubElement(defs, "linearGradient")
    grad.set("id", "bgGrad")
    grad.set("x1", "0%")
    grad.set("y1", "0%")
    grad.set("x2", "0%")
    grad.set("y2", "100%")
    stop1 = ET.SubElement(grad, "stop")
    stop1.set("offset", "0%")
    stop1.set("style", f"stop-color:{LIGHT_BG};stop-opacity:1")
    stop2 = ET.SubElement(grad, "stop")
    stop2.set("offset", "100%")
    stop2.set("style", f"stop-color:#FFEDD5;stop-opacity:1")

    # Header gradient
    grad2 = ET.SubElement(defs, "linearGradient")
    grad2.set("id", "headerGrad")
    grad2.set("x1", "0%")
    grad2.set("y1", "0%")
    grad2.set("x2", "100%")
    grad2.set("y2", "0%")
    hstop1 = ET.SubElement(grad2, "stop")
    hstop1.set("offset", "0%")
    hstop1.set("style", f"stop-color:{ORANGE};stop-opacity:1")
    hstop2 = ET.SubElement(grad2, "stop")
    hstop2.set("offset", "100%")
    hstop2.set("style", f"stop-color:{DARK_ORANGE};stop-opacity:1")

    # Drop shadow filter
    filt = ET.SubElement(defs, "filter")
    filt.set("id", "shadow")
    filt.set("x", "-5%")
    filt.set("y", "-5%")
    filt.set("width", "110%")
    filt.set("height", "110%")
    feOff = ET.SubElement(filt, "feDropShadow")
    feOff.set("dx", "2")
    feOff.set("dy", "2")
    feOff.set("stdDeviation", "3")
    feOff.set("flood-color", "#00000033")

    return svg, defs


def add_background(svg):
    """Add the main background rectangle."""
    rect = ET.SubElement(svg, "rect")
    rect.set("width", str(W))
    rect.set("height", str(H))
    rect.set("fill", "url(#bgGrad)")
    rect.set("rx", "0")


def add_header(svg, title, subtitle="", lesson_num=1):
    """Add a styled header bar with title."""
    # Header background
    header_rect = ET.SubElement(svg, "rect")
    header_rect.set("x", "0")
    header_rect.set("y", "0")
    header_rect.set("width", str(W))
    header_rect.set("height", "80")
    header_rect.set("fill", "url(#headerGrad)")

    # Warning triangle icon
    g = ET.SubElement(svg, "g")
    g.set("transform", "translate(20, 15)")
    # Triangle
    poly = ET.SubElement(g, "polygon")
    poly.set("points", "25,5 5,45 45,45")
    poly.set("fill", YELLOW_WARN)
    poly.set("stroke", DARK)
    poly.set("stroke-width", "2")
    # Exclamation mark
    t = ET.SubElement(g, "text")
    t.set("x", "25")
    t.set("y", "38")
    t.set("text-anchor", "middle")
    t.set("font-size", "22")
    t.set("font-weight", "bold")
    t.set("fill", DARK)
    t.text = "!"

    # Lesson number badge
    badge = ET.SubElement(svg, "rect")
    badge.set("x", "70")
    badge.set("y", "18")
    badge.set("width", "36")
    badge.set("height", "36")
    badge.set("rx", "6")
    badge.set("fill", WHITE)
    badge.set("opacity", "0.9")
    badge_num = ET.SubElement(svg, "text")
    badge_num.set("x", "88")
    badge_num.set("y", "44")
    badge_num.set("text-anchor", "middle")
    badge_num.set("font-size", "18")
    badge_num.set("font-weight", "bold")
    badge_num.set("fill", ORANGE)
    badge_num.text = str(lesson_num)

    # Title text
    title_text = ET.SubElement(svg, "text")
    title_text.set("x", "120")
    title_text.set("y", "42")
    title_text.set("font-size", "22")
    title_text.set("font-weight", "bold")
    title_text.set("fill", WHITE)
    title_text.text = title

    # Subtitle
    if subtitle:
        sub = ET.SubElement(svg, "text")
        sub.set("x", "120")
        sub.set("y", "64")
        sub.set("font-size", "13")
        sub.set("fill", "#FED7AA")
        sub.text = subtitle

    # ОБЖ badge on right
    badge_r = ET.SubElement(svg, "rect")
    badge_r.set("x", str(W - 90))
    badge_r.set("y", "22")
    badge_r.set("width", "70")
    badge_r.set("height", "30")
    badge_r.set("rx", "15")
    badge_r.set("fill", "rgba(255,255,255,0.2)")
    badge_r.set("stroke", "rgba(255,255,255,0.5)")
    badge_r.set("stroke-width", "1")
    subj = ET.SubElement(svg, "text")
    subj.set("x", str(W - 55))
    subj.set("y", "43")
    subj.set("text-anchor", "middle")
    subj.set("font-size", "14")
    subj.set("font-weight", "bold")
    subj.set("fill", WHITE)
    subj.text = "ОБЖ"

    # Grade badge
    grade_badge = ET.SubElement(svg, "rect")
    grade_badge.set("x", str(W - 90))
    grade_badge.set("y", "52")
    grade_badge.set("width", "70")
    grade_badge.set("height", "22")
    grade_badge.set("rx", "11")
    grade_badge.set("fill", "rgba(255,255,255,0.15)")
    grade_t = ET.SubElement(svg, "text")
    grade_t.set("x", str(W - 55))
    grade_t.set("y", "67")
    grade_t.set("text-anchor", "middle")
    grade_t.set("font-size", "11")
    grade_t.set("fill", "#FED7AA")
    grade_t.text = "7 класс"

    # Bottom line
    line = ET.SubElement(svg, "line")
    line.set("x1", "0")
    line.set("y1", "80")
    line.set("x2", str(W))
    line.set("y2", "80")
    line.set("stroke", ORANGE)
    line.set("stroke-width", "3")


def add_card(svg, x, y, w, h, title="", items=None, color=ORANGE, icon_char=""):
    """Add a rounded card with optional title and bullet items."""
    # Card background
    card = ET.SubElement(svg, "rect")
    card.set("x", str(x))
    card.set("y", str(y))
    card.set("width", str(w))
    card.set("height", str(h))
    card.set("rx", "10")
    card.set("fill", WHITE)
    card.set("stroke", color)
    card.set("stroke-width", "2")
    card.set("filter", "url(#shadow)")

    # Color bar at top
    bar = ET.SubElement(svg, "rect")
    bar.set("x", str(x))
    bar.set("y", str(y))
    bar.set("width", str(w))
    bar.set("height", "6")
    bar.set("rx", "3")
    bar.set("fill", color)

    # Icon if provided
    cy = y + 14
    if icon_char:
        icon_bg = ET.SubElement(svg, "circle")
        icon_bg.set("cx", str(x + 24))
        icon_bg.set("cy", str(cy + 10))
        icon_bg.set("r", "14")
        icon_bg.set("fill", color)
        icon_t = ET.SubElement(svg, "text")
        icon_t.set("x", str(x + 24))
        icon_t.set("y", str(cy + 16))
        icon_t.set("text-anchor", "middle")
        icon_t.set("font-size", "14")
        icon_t.set("font-weight", "bold")
        icon_t.set("fill", WHITE)
        icon_t.text = icon_char

    # Title
    if title:
        t = ET.SubElement(svg, "text")
        t.set("x", str(x + 46 if icon_char else 14))
        t.set("y", str(cy + 14))
        t.set("font-size", "14")
        t.set("font-weight", "bold")
        t.set("fill", DARK)
        t.text = title
        cy += 24

    # Items
    if items:
        for i, item in enumerate(items):
            # Bullet
            bullet = ET.SubElement(svg, "circle")
            bullet.set("cx", str(x + 20))
            bullet.set("cy", str(cy + 8))
            bullet.set("r", "3")
            bullet.set("fill", color)

            txt = ET.SubElement(svg, "text")
            txt.set("x", str(x + 30))
            txt.set("y", str(cy + 12))
            txt.set("font-size", "12")
            txt.set("fill", DARK)
            # Truncate long items
            display = item[:45] + "..." if len(item) > 48 else item
            txt.text = display
            cy += 20


def add_numbered_step(svg, x, y, num, text, color=ORANGE):
    """Add a numbered step with circle badge."""
    # Circle
    circ = ET.SubElement(svg, "circle")
    circ.set("cx", str(x + 14))
    circ.set("cy", str(y + 8))
    circ.set("r", "14")
    circ.set("fill", color)

    # Number
    n = ET.SubElement(svg, "text")
    n.set("x", str(x + 14))
    n.set("y", str(y + 13))
    n.set("text-anchor", "middle")
    n.set("font-size", "13")
    n.set("font-weight", "bold")
    n.set("fill", WHITE)
    n.text = str(num)

    # Text
    t = ET.SubElement(svg, "text")
    t.set("x", str(x + 36))
    t.set("y", str(y + 13))
    t.set("font-size", "12")
    t.set("fill", DARK)
    display = text[:55] + "..." if len(text) > 58 else text
    t.text = display


def add_warning_sign(svg, cx, cy, size=30, text="!"):
    """Add a triangular warning sign."""
    g = ET.SubElement(svg, "g")
    pts = f"{cx},{cy - size} {cx - size},{cy + int(size * 0.7)} {cx + size},{cy + int(size * 0.7)}"
    poly = ET.SubElement(g, "polygon")
    poly.set("points", pts)
    poly.set("fill", YELLOW_WARN)
    poly.set("stroke", DARK)
    poly.set("stroke-width", "2")
    t = ET.SubElement(g, "text")
    t.set("x", str(cx))
    t.set("y", str(cy + int(size * 0.25)))
    t.set("text-anchor", "middle")
    t.set("font-size", str(int(size * 0.9)))
    t.set("font-weight", "bold")
    t.set("fill", DARK)
    t.text = text


def add_danger_sign(svg, cx, cy, size=28):
    """Add a circular danger/prohibition sign."""
    circ_outer = ET.SubElement(svg, "circle")
    circ_outer.set("cx", str(cx))
    circ_outer.set("cy", str(cy))
    circ_outer.set("r", str(size))
    circ_outer.set("fill", DANGER)
    circ_outer.set("stroke", DARK)
    circ_outer.set("stroke-width", "2")
    circ_inner = ET.SubElement(svg, "circle")
    circ_inner.set("cx", str(cx))
    circ_inner.set("cy", str(cy))
    circ_inner.set("r", str(size - 5))
    circ_inner.set("fill", "none")
    circ_inner.set("stroke", WHITE)
    circ_inner.set("stroke-width", "3")
    # Horizontal bar
    bar = ET.SubElement(svg, "line")
    bar.set("x1", str(cx - size + 8))
    bar.set("y1", str(cy))
    bar.set("x2", str(cx + size - 8))
    bar.set("y2", str(cy))
    bar.set("stroke", WHITE)
    bar.set("stroke-width", "4")


def add_section_label(svg, x, y, text, color=ORANGE):
    """Add a section label with left accent bar."""
    bar = ET.SubElement(svg, "rect")
    bar.set("x", str(x))
    bar.set("y", str(y))
    bar.set("width", "4")
    bar.set("height", "18")
    bar.set("rx", "2")
    bar.set("fill", color)
    t = ET.SubElement(svg, "text")
    t.set("x", str(x + 10))
    t.set("y", str(y + 14))
    t.set("font-size", "14")
    t.set("font-weight", "bold")
    t.set("fill", color)
    t.text = text


def add_footer(svg, text="Основы безопасности жизнедеятельности | 7 класс"):
    """Add footer bar."""
    footer = ET.SubElement(svg, "rect")
    footer.set("x", "0")
    footer.set("y", str(H - 30))
    footer.set("width", str(W))
    footer.set("height", "30")
    footer.set("fill", DARK)
    ft = ET.SubElement(svg, "text")
    ft.set("x", str(W // 2))
    ft.set("y", str(H - 10))
    ft.set("text-anchor", "middle")
    ft.set("font-size", "11")
    ft.set("fill", GRAY_LIGHT)
    ft.text = text


# ============================================================
# LESSON 1: Правила дорожного движения для велосипедистов
# ============================================================
def generate_lesson1():
    svg, defs = svg_header("Правила дорожного движения для велосипедистов")
    add_background(svg)
    add_header(svg, "Правила дорожного движения для велосипедистов",
               "Безопасное управление велосипедом на дороге", 1)

    # Left column: Traffic rules for cyclists
    add_section_label(svg, 20, 98, "Основные правила", ORANGE)

    rules = [
        "Велосипед — транспортное средство",
        "Управление с 14 лет на дороге",
        "Двигаться по правому краю проезжей части",
        "Запрещено ездить по тротуарам",
        "Использовать световозвращатели",
        "Шлем обязателен для безопасности",
    ]
    add_card(svg, 20, 120, 250, 180, "Правила езды", rules, ORANGE, "📋")

    # Middle column: Hand signals
    add_section_label(svg, 285, 98, "Ручные сигналы", ORANGE)

    signals_data = [
        ("Поворот направо", "Левая рука вытянута\nвправо, согнута в локте"),
        ("Поворот налево", "Левая рука вытянута\nв сторону"),
        ("Остановка", "Левая рука поднята\nвертикально вверх"),
    ]

    y_off = 120
    for label, desc in signals_data:
        # Signal box
        box = ET.SubElement(svg, "rect")
        box.set("x", "285")
        box.set("y", str(y_off))
        box.set("width", "230")
        box.set("height", "52")
        box.set("rx", "8")
        box.set("fill", WHITE)
        box.set("stroke", ORANGE)
        box.set("stroke-width", "1.5")

        # Orange dot
        dot = ET.SubElement(svg, "circle")
        dot.set("cx", "300")
        dot.set("cy", str(y_off + 26))
        dot.set("r", "8")
        dot.set("fill", ORANGE)

        sig_title = ET.SubElement(svg, "text")
        sig_title.set("x", "316")
        sig_title.set("y", str(y_off + 20))
        sig_title.set("font-size", "12")
        sig_title.set("font-weight", "bold")
        sig_title.set("fill", DARK)
        sig_title.text = label

        sig_desc = ET.SubElement(svg, "text")
        sig_desc.set("x", "316")
        sig_desc.set("y", str(y_off + 38))
        sig_desc.set("font-size", "10")
        sig_desc.set("fill", GRAY)
        sig_desc.text = desc.split("\n")[0]

        y_off += 60

    # Right column: Warning signs for cyclists
    add_section_label(svg, 530, 98, "Знаки для велосипедистов", DANGER)

    signs_data = [
        ("🚲", "Велосипедная дорожка", GREEN),
        ("⛔", "Движение велосипедов запрещено", DANGER),
        ("⚠", "Осторожно: велосипедисты", YELLOW_WARN),
    ]

    y_off = 120
    for icon, label, color in signs_data:
        box = ET.SubElement(svg, "rect")
        box.set("x", "530")
        box.set("y", str(y_off))
        box.set("width", "250")
        box.set("height", "50")
        box.set("rx", "8")
        box.set("fill", WHITE)
        box.set("stroke", color)
        box.set("stroke-width", "1.5")

        # Color circle for icon
        ic = ET.SubElement(svg, "circle")
        ic.set("cx", "555")
        ic.set("cy", str(y_off + 25))
        ic.set("r", "14")
        ic.set("fill", color)

        ic_t = ET.SubElement(svg, "text")
        ic_t.set("x", "555")
        ic_t.set("y", str(y_off + 30))
        ic_t.set("text-anchor", "middle")
        ic_t.set("font-size", "12")
        ic_t.set("fill", WHITE)
        ic_t.text = icon

        sign_label = ET.SubElement(svg, "text")
        sign_label.set("x", "578")
        sign_label.set("y", str(y_off + 30))
        sign_label.set("font-size", "11")
        sign_label.set("fill", DARK)
        sign_label.text = label

        y_off += 58

    # Bottom section: Safety equipment checklist
    add_section_label(svg, 20, 330, "Экипировка велосипедиста", GREEN)

    equip_items = [
        "Шлем — защита головы при падении",
        "Световозвращатели — видимость в темноте",
        "Звонок — предупреждение пешеходов",
        "Зеркало заднего вида — контроль обстановки",
        "Свет фары и габаритные огни",
        "Аптечка и инструменты",
    ]

    # Two-column layout for equipment
    col1 = equip_items[:3]
    col2 = equip_items[3:]

    y_pos = 354
    for i, item in enumerate(col1):
        add_numbered_step(svg, 20, y_pos, i + 1, item, GREEN)
        y_pos += 28

    y_pos = 354
    for i, item in enumerate(col2):
        add_numbered_step(svg, 400, y_pos, i + 4, item, GREEN)
        y_pos += 28

    # Important note at bottom
    note = ET.SubElement(svg, "rect")
    note.set("x", "20")
    note.set("y", "470")
    note.set("width", str(W - 40))
    note.set("height", "70")
    note.set("rx", "10")
    note.set("fill", "#FEF2F2")
    note.set("stroke", DANGER)
    note.set("stroke-width", "2")

    add_warning_sign(svg, 50, 505, 20, "!")

    note_t = ET.SubElement(svg, "text")
    note_t.set("x", "80")
    note_t.set("y", "498")
    note_t.set("font-size", "13")
    note_t.set("font-weight", "bold")
    note_t.set("fill", DANGER)
    note_t.text = "Важно помнить!"

    note_body = ET.SubElement(svg, "text")
    note_body.set("x", "80")
    note_body.set("y", "518")
    note_body.set("font-size", "11")
    note_body.set("fill", DARK)
    note_body.text = "Нарушение ПДД на велосипеде влечёт административную ответственность."

    note_body2 = ET.SubElement(svg, "text")
    note_body2.set("x", "80")
    note_body2.set("y", "534")
    note_body2.set("font-size", "11")
    note_body2.set("fill", DARK)
    note_body2.text = "Перевозка детей до 7 лет — только на специальном сиденье с подножками."

    add_footer(svg)
    return svg


# ============================================================
# LESSON 2: Причины ДТП и их предотвращение
# ============================================================
def generate_lesson2():
    svg, defs = svg_header("Причины ДТП и их предотвращение")
    add_background(svg)
    add_header(svg, "Причины ДТП и их предотвращение",
               "Статистика, причины и правила безопасного поведения", 2)

    # Statistics section
    add_section_label(svg, 20, 98, "Статистика ДТП", DANGER)

    # Stats cards
    stats = [
        ("70%", "ДТП по вине\nводителей", DANGER),
        ("20%", "ДТП по вине\nпешеходов", ORANGE),
        ("10%", "Прочие\nпричины", GRAY),
    ]

    x_off = 20
    for val, label, color in stats:
        box = ET.SubElement(svg, "rect")
        box.set("x", str(x_off))
        box.set("y", "118")
        box.set("width", "120")
        box.set("height", "75")
        box.set("rx", "10")
        box.set("fill", WHITE)
        box.set("stroke", color)
        box.set("stroke-width", "2")
        box.set("filter", "url(#shadow)")

        val_t = ET.SubElement(svg, "text")
        val_t.set("x", str(x_off + 60))
        val_t.set("y", str(148))
        val_t.set("text-anchor", "middle")
        val_t.set("font-size", "24")
        val_t.set("font-weight", "bold")
        val_t.set("fill", color)
        val_t.text = val

        label_t = ET.SubElement(svg, "text")
        label_t.set("x", str(x_off + 60))
        label_t.set("y", str(168))
        label_t.set("text-anchor", "middle")
        label_t.set("font-size", "10")
        label_t.set("fill", GRAY)
        label_t.text = label.split("\n")[0]

        x_off += 135

    # Main causes
    add_section_label(svg, 430, 98, "Основные причины ДТП", ORANGE)

    causes = [
        "Превышение скорости движения",
        "Управление в нетрезвом состоянии",
        "Нарушение правил проезда перекрёстков",
        "Неправильный выбор дистанции",
        "Невнимательность и отвлечение",
        "Нарушение правил обгона",
    ]
    add_card(svg, 430, 118, 350, 170, "Причины", causes, DANGER, "⚠")

    # Prevention section
    add_section_label(svg, 20, 220, "Предотвращение ДТП", GREEN)

    # Steps for safe behavior
    prevention_steps = [
        ("1", "Соблюдайте скоростной режим и дистанцию"),
        ("2", "Не отвлекайтесь за рулём (телефон, разговоры)"),
        ("3", "Используйте ремни безопасности и детские кресла"),
        ("4", "Уступайте дорогу пешеходам на переходах"),
        ("5", "Соблюдайте правила проезда перекрёстков"),
        ("6", "Не садитесь за руль в нетрезвом виде"),
    ]

    y_pos = 244
    for num, text in prevention_steps:
        add_numbered_step(svg, 20, y_pos, num, text, GREEN)
        y_pos += 30

    # Pedestrian rules
    add_section_label(svg, 430, 310, "Безопасность пешехода", ORANGE)

    ped_rules = [
        "Переходите дорогу по зебре",
        "Смотрите налево, затем направо",
        "Не перебегайте на красный сигнал",
        "Носите световозвращатели в темноте",
        "Не играйте вблизи проезжей части",
    ]

    add_card(svg, 430, 332, 350, 150, "Правила пешехода", ped_rules, ORANGE, "🚶")

    # Bottom warning
    warn_box = ET.SubElement(svg, "rect")
    warn_box.set("x", "20")
    warn_box.set("y", "470")
    warn_box.set("width", str(W - 40))
    warn_box.set("height", "70")
    warn_box.set("rx", "10")
    warn_box.set("fill", "#FEF2F2")
    warn_box.set("stroke", DANGER)
    warn_box.set("stroke-width", "2")

    add_danger_sign(svg, 50, 505, 18)

    wt = ET.SubElement(svg, "text")
    wt.set("x", "80")
    wt.set("y", "498")
    wt.set("font-size", "13")
    wt.set("font-weight", "bold")
    wt.set("fill", DANGER)
    wt.text = "Критический факт"

    wb = ET.SubElement(svg, "text")
    wb.set("x", "80")
    wb.set("y", "518")
    wb.set("font-size", "11")
    wb.set("fill", DARK)
    wb.text = "Ежегодно в России происходит более 130 000 ДТП, в которых погибают и получают травмы люди."

    wb2 = ET.SubElement(svg, "text")
    wb2.set("x", "80")
    wb2.set("y", "534")
    wb2.set("font-size", "11")
    wb2.set("fill", DARK)
    wb2.text = "Соблюдение ПДД — главная мера профилактики дорожного травматизма."

    add_footer(svg)
    return svg


# ============================================================
# LESSON 3: Причины пожаров и их предотвращение
# ============================================================
def generate_lesson3():
    svg, defs = svg_header("Причины пожаров и их предотвращение")
    add_background(svg)
    add_header(svg, "Причины пожаров и их предотвращение",
               "Электричество, неосторожное обращение с огнём, профилактика", 3)

    # Left: Main causes of fires
    add_section_label(svg, 20, 98, "Основные причины пожаров", DANGER)

    fire_causes = [
        "Неосторожное обращение с огнём — 40%",
        "Нарушение правил электробезопасности — 25%",
        "Неисправность электрооборудования — 15%",
        "Детские шалости с огнём — 10%",
        "Нарушение правил пожарной безопасности — 10%",
    ]
    add_card(svg, 20, 118, 280, 170, "Причины пожаров", fire_causes, DANGER, "🔥")

    # Right: Electrical safety
    add_section_label(svg, 315, 98, "Электробезопасность", ORANGE)

    electric_rules = [
        "Не перегружайте розетки",
        "Не используйте повреждённые провода",
        "Отключайте приборы уходя",
        "Не оставляйте без присмотра",
        "Заземляйте электроприборы",
    ]
    add_card(svg, 315, 118, 230, 170, "Правила", electric_rules, ORANGE, "⚡")

    # Far right: Prevention
    add_section_label(svg, 560, 98, "Профилактика", GREEN)

    prevention = [
        "Датчики дыма в помещениях",
        "Огнетушитель в доступном месте",
        "План эвакуации на видном месте",
        "Не курить в постели",
        "Не оставлять плиту без присмотра",
    ]
    add_card(svg, 560, 118, 220, 170, "Меры", prevention, GREEN, "🛡")

    # Fire extinguisher types
    add_section_label(svg, 20, 310, "Типы огнетушителей", ORANGE)

    extinguishers = [
        ("ОП", "Порошковый", "Универсальный, для всех типов", BLUE),
        ("ОУ", "Углекислотный", "Для электроустановок", ORANGE),
        ("ОВ", "Водный", "Для твердых материалов", GREEN),
    ]

    x_off = 20
    for abbr, name, desc, color in extinguishers:
        box = ET.SubElement(svg, "rect")
        box.set("x", str(x_off))
        box.set("y", "332")
        box.set("width", "245")
        box.set("height", "65")
        box.set("rx", "8")
        box.set("fill", WHITE)
        box.set("stroke", color)
        box.set("stroke-width", "1.5")

        # Abbreviation badge
        badge = ET.SubElement(svg, "rect")
        badge.set("x", str(x_off + 10))
        badge.set("y", str(332 + 10))
        badge.set("width", "40")
        badge.set("height", "44")
        badge.set("rx", "6")
        badge.set("fill", color)

        abbr_t = ET.SubElement(svg, "text")
        abbr_t.set("x", str(x_off + 30))
        abbr_t.set("y", str(332 + 38))
        abbr_t.set("text-anchor", "middle")
        abbr_t.set("font-size", "16")
        abbr_t.set("font-weight", "bold")
        abbr_t.set("fill", WHITE)
        abbr_t.text = abbr

        name_t = ET.SubElement(svg, "text")
        name_t.set("x", str(x_off + 60))
        name_t.set("y", str(332 + 28))
        name_t.set("font-size", "12")
        name_t.set("font-weight", "bold")
        name_t.set("fill", DARK)
        name_t.text = name

        desc_t = ET.SubElement(svg, "text")
        desc_t.set("x", str(x_off + 60))
        desc_t.set("y", str(332 + 45))
        desc_t.set("font-size", "10")
        desc_t.set("fill", GRAY)
        desc_t.text = desc

        x_off += 255

    # Emergency procedure steps
    add_section_label(svg, 20, 420, "При пожаре: порядок действий", DANGER)

    steps = [
        "1. Вызовите пожарную охрану: 101 или 112",
        "2. Выведите людей из помещения",
        "3. Отключите электроэнергию и газ",
        "4. Приступите к тушению огнетушителем",
        "5. Не открывайте окна (приток кислорода)",
        "6. Если выйти нельзя — ждите спасателей у окна",
    ]

    y_pos = 444
    for step in steps:
        parts = step.split(". ", 1)
        num = parts[0]
        txt = parts[1] if len(parts) > 1 else step
        add_numbered_step(svg, 20, y_pos, num, txt, DANGER)
        y_pos += 22

    add_footer(svg)
    return svg


# ============================================================
# LESSON 4: Природные ЧС
# ============================================================
def generate_lesson4():
    svg, defs = svg_header("Природные чрезвычайные ситуации")
    add_background(svg)
    add_header(svg, "Природные чрезвычайные ситуации",
               "Землетрясения, наводнения, ураганы, торнадо", 4)

    # Four emergency type cards in 2x2 grid
    emergencies = [
        ("Землетрясение", [
            "Держитесь подальше от зданий",
            "В здании — под столом, в дверном проёме",
            "На улице — на открытом месте",
            "Не пользуйтесь лифтом",
        ], DANGER, "📉"),
        ("Наводнение", [
            "Слушайте предупреждения МЧС",
            "Соберите документы и ценности",
            "Поднимитесь на верхние этажи",
            "Не пытайтесь переплыть поток",
        ], BLUE, "🌊"),
        ("Ураган", [
            "Закройте окна и двери",
            "Находитесь в укрытии",
            "Держитесь подальше от окон",
            "Запасите воду и продукты",
        ], ORANGE, "🌀"),
        ("Торнадо (смерч)", [
            "Укройтесь в подвале",
            "В поле — лягте в яму",
            "Не укрывайтесь под мостом",
            "Держитесь подальше от деревьев",
        ], DARK_ORANGE, "🌪"),
    ]

    positions = [(20, 100), (415, 100), (20, 320), (415, 320)]
    for (x, y), (title, items, color, icon) in zip(positions, emergencies):
        add_card(svg, x, y, 370, 180, title, items, color, icon)

    # Bottom warning bar
    warn_box = ET.SubElement(svg, "rect")
    warn_box.set("x", "20")
    warn_box.set("y", "530")
    warn_box.set("width", str(W - 40))
    warn_box.set("height", "28")
    warn_box.set("rx", "8")
    warn_box.set("fill", DANGER)

    wt = ET.SubElement(svg, "text")
    wt.set("x", str(W // 2))
    wt.set("y", "549")
    wt.set("text-anchor", "middle")
    wt.set("font-size", "12")
    wt.set("font-weight", "bold")
    wt.set("fill", WHITE)
    wt.text = "Единый номер вызова экстренных служб: 112"

    add_footer(svg)
    return svg


# ============================================================
# LESSON 5: Техногенные ЧС
# ============================================================
def generate_lesson5():
    svg, defs = svg_header("Техногенные чрезвычайные ситуации")
    add_background(svg)
    add_header(svg, "Техногенные чрезвычайные ситуации",
               "Промышленные аварии, химическое и радиационное заражение", 5)

    # Left: Types of technogenic emergencies
    add_section_label(svg, 20, 98, "Виды техногенных ЧС", DANGER)

    tech_types = [
        "Аварии на химических предприятиях",
        "Аварии на радиационных объектах",
        "Взрывы и пожары на производстве",
        "Аварии на электростанциях",
        "Обрушения зданий и сооружений",
        "Аварии на трубопроводах",
    ]
    add_card(svg, 20, 118, 250, 175, "Классификация", tech_types, DANGER, "🏭")

    # Middle: Chemical safety
    add_section_label(svg, 285, 98, "Химическая безопасность", ORANGE)

    chem_rules = [
        "Используйте противогаз или респиратор",
        "Двигайтесь перпендикулярно ветру",
        "Укройтесь в герметичном помещении",
        "Закройте окна и вентиляцию",
        "Пейте только бутилированную воду",
    ]
    add_card(svg, 285, 118, 240, 175, "При хим. аварии", chem_rules, ORANGE, "⚗")

    # Right: Radiation safety
    add_section_label(svg, 540, 98, "Радиационная безопасность", BLUE)

    rad_rules = [
        "Укрытие в помещении (защита от облучения)",
        "Герметизация окон и дверей",
        "Приём йодистого калия",
        "Защита органов дыхания",
        "Не употребляйте загрязнённые продукты",
    ]
    add_card(svg, 540, 118, 240, 175, "При радиац. аварии", rad_rules, BLUE, "☢")

    # Bottom: Action plan
    add_section_label(svg, 20, 318, "Порядок действий при техногенной ЧС", GREEN)

    steps = [
        "1. Услышали сирену — включите радио/ТВ",
        "2. Узнайте характер опасности и зону поражения",
        "3. Выполните рекомендации МЧС",
        "4. Подготовьте документы и средства защиты",
        "5. При эвакуации — следуйте по указанному маршруту",
        "6. Не возвращайтесь без разрешения властей",
    ]

    # Two columns for steps
    col1 = steps[:3]
    col2 = steps[3:]

    y_pos = 342
    for step in col1:
        parts = step.split(". ", 1)
        add_numbered_step(svg, 20, y_pos, parts[0], parts[1], GREEN)
        y_pos += 30

    y_pos = 342
    for step in col2:
        parts = step.split(". ", 1)
        add_numbered_step(svg, 400, y_pos, parts[0], parts[1], GREEN)
        y_pos += 30

    # Warning zones info
    zone_box = ET.SubElement(svg, "rect")
    zone_box.set("x", "20")
    zone.set("y", "460") if False else None  # skip, just set it
    zone_box.set("y", "460")
    zone_box.set("width", str(W - 40))
    zone_box.set("height", "80")
    zone_box.set("rx", "10")
    zone_box.set("fill", WHITE)
    zone_box.set("stroke", DANGER)
    zone_box.set("stroke-width", "2")
    zone_box.set("filter", "url(#shadow)")

    # Zone colors
    zones = [
        ("Зона А", "Район чрезвычайной опасности", DANGER),
        ("Зона Б", "Зона опасного заражения", ORANGE),
        ("Зона В", "Зона умеренного заражения", YELLOW_WARN),
    ]

    x_off = 35
    for zone_name, zone_desc, color in zones:
        zb = ET.SubElement(svg, "rect")
        zb.set("x", str(x_off))
        zb.set("y", "470")
        zb.set("width", "220")
        zb.set("height", "55")
        zb.set("rx", "6")
        zb.set("fill", color)
        zb.set("opacity", "0.15")

        zt = ET.SubElement(svg, "text")
        zt.set("x", str(x_off + 10))
        zt.set("y", "492")
        zt.set("font-size", "14")
        zt.set("font-weight", "bold")
        zt.set("fill", color)
        zt.text = zone_name

        zd = ET.SubElement(svg, "text")
        zd.set("x", str(x_off + 10))
        zd.set("y", "512")
        zd.set("font-size", "11")
        zd.set("fill", DARK)
        zd.text = zone_desc

        x_off += 245

    add_footer(svg)
    return svg


# ============================================================
# LESSON 6: Первая помощь при кровотечениях
# ============================================================
def generate_lesson6():
    svg, defs = svg_header("Первая помощь при кровотечениях")
    add_background(svg)
    add_header(svg, "Первая помощь при кровотечениях",
               "Виды кровотечений, жгут, давящая повязка, порядок действий", 6)

    # Top row: Types of bleeding
    add_section_label(svg, 20, 98, "Виды кровотечений", DANGER)

    bleed_types = [
        ("Капиллярное", "Кровь сочится каплями,\nцвет — ярко-красный", ORANGE, "Небольшая рана"),
        ("Венозное", "Кровь тёмно-красная,\nтечёт равномерно", BLUE, "Опасная потеря крови"),
        ("Артериальное", "Кровь алая, пульсирует\nфонтаном", DANGER, "Угроза жизни!"),
    ]

    x_off = 20
    for btype, desc, color, severity in bleed_types:
        box = ET.SubElement(svg, "rect")
        box.set("x", str(x_off))
        box.set("y", "118")
        box.set("width", "250")
        box.set("height", "80")
        box.set("rx", "10")
        box.set("fill", WHITE)
        box.set("stroke", color)
        box.set("stroke-width", "2")
        box.set("filter", "url(#shadow)")

        # Color bar at top
        cbar = ET.SubElement(svg, "rect")
        cbar.set("x", str(x_off))
        cbar.set("y", "118")
        cbar.set("width", "250")
        cbar.set("height", "6")
        cbar.set("rx", "3")
        cbar.set("fill", color)

        bt = ET.SubElement(svg, "text")
        bt.set("x", str(x_off + 12))
        bt.set("y", str(140))
        bt.set("font-size", "14")
        bt.set("font-weight", "bold")
        bt.set("fill", color)
        bt.text = btype

        bd1 = ET.SubElement(svg, "text")
        bd1.set("x", str(x_off + 12))
        bd1.set("y", str(158))
        bd1.set("font-size", "10")
        bd1.set("fill", DARK)
        bd1.text = desc.split("\n")[0]

        bd2 = ET.SubElement(svg, "text")
        bd2.set("x", str(x_off + 12))
        bd2.set("y", str(172))
        bd2.set("font-size", "10")
        bd2.set("fill", GRAY)
        bd2.text = desc.split("\n")[1] if "\n" in desc else severity

        # Severity badge
        sev = ET.SubElement(svg, "rect")
        sev.set("x", str(x_off + 180))
        sev.set("y", str(130))
        sev.set("width", "58")
        sev.set("height", "18")
        sev.set("rx", "9")
        sev.set("fill", color)
        sev_t = ET.SubElement(svg, "text")
        sev_t.set("x", str(x_off + 209))
        sev_t.set("y", str(143))
        sev_t.set("text-anchor", "middle")
        sev_t.set("font-size", "8")
        sev_t.set("font-weight", "bold")
        sev_t.set("fill", WHITE)
        sev_t.text = severity[:12]

        x_off += 260

    # Left: First aid steps
    add_section_label(svg, 20, 220, "Первая помощь: шаг за шагом", GREEN)

    aid_steps = [
        "1. Вызовите скорую помощь: 103 или 112",
        "2. Успокойте пострадавшего, уложите",
        "3. Оцените вид кровотечения",
        "4. При артериальном — наложите жгут",
        "5. При венозном — давящая повязка",
        "6. При капиллярном — промойте и заклейте",
    ]

    y_pos = 244
    for step in aid_steps:
        parts = step.split(". ", 1)
        add_numbered_step(svg, 20, y_pos, parts[0], parts[1], GREEN)
        y_pos += 28

    # Right: Tourniquet instructions
    add_section_label(svg, 430, 220, "Наложение жгута", DANGER)

    tourniquet_rules = [
        "Жгут — только при артериальном кровотечении!",
        "Накладывается выше раны на 5-7 см",
        "Под жгут — ткань (не на голую кожу)",
        "Затягивайте до остановки кровотечения",
        "Запишите время наложения жгута",
        "Максимальное время летом — 2 часа",
        "Максимальное время зимой — 1 час",
        "Ослабляйте жгут каждые 30 минут",
    ]

    add_card(svg, 430, 240, 350, 195, "Правила наложения жгута", tourniquet_rules, DANGER, "🩹")

    # Pressure bandage
    add_section_label(svg, 20, 440, "Давящая повязка", ORANGE)

    pressure_steps = [
        "1. Приложите стерильную салфетку к ране",
        "2. Поверх — тугой валик из бинта",
        "3. Плотно прибинтуйте валик к ране",
        "4. Проверьте пульс ниже повязки",
    ]

    y_pos = 462
    for step in pressure_steps:
        parts = step.split(". ", 1)
        add_numbered_step(svg, 20, y_pos, parts[0], parts[1], ORANGE)
        y_pos += 24

    # Important note
    note = ET.SubElement(svg, "rect")
    note.set("x", "430")
    note.set("y", "460")
    note.set("width", "350")
    note.set("height", "80")
    note.set("rx", "10")
    note.set("fill", "#FEF2F2")
    note.set("stroke", DANGER)
    note.set("stroke-width", "2")

    add_warning_sign(svg, 460, 500, 18, "!")

    nt = ET.SubElement(svg, "text")
    nt.set("x", "488")
    nt.set("y", "488")
    nt.set("font-size", "12")
    nt.set("font-weight", "bold")
    nt.set("fill", DANGER)
    nt.text = "Запомните!"

    nb1 = ET.SubElement(svg, "text")
    nb1.set("x", "488")
    nb1.set("y", "508")
    nb1.set("font-size", "11")
    nb1.set("fill", DARK)
    nb1.text = "Жгут — крайняя мера! Сначала попробуйте"

    nb2 = ET.SubElement(svg, "text")
    nb2.set("x", "488")
    nb2.set("y", "524")
    nb2.set("font-size", "11")
    nb2.set("fill", DARK)
    nb2.text = "остановить кровь давящей повязкой или пальцевым прижатием."

    add_footer(svg)
    return svg


# ============================================================
# LESSON 7: Первая помощь при переломах и ожогах
# ============================================================
def generate_lesson7():
    svg, defs = svg_header("Первая помощь при переломах и ожогах")
    add_background(svg)
    add_header(svg, "Первая помощь при переломах и ожогах",
               "Иммобилизация, степени ожогов, порядок действий", 7)

    # Left column: Fractures
    add_section_label(svg, 20, 98, "Переломы костей", DANGER)

    fracture_types = [
        ("Закрытый перелом", "Кость сломана, кожа цела"),
        ("Открытый перелом", "Кость видна в ране, кровотечение"),
    ]

    y_off = 118
    for ftype, fdesc in fracture_types:
        box = ET.SubElement(svg, "rect")
        box.set("x", "20")
        box.set("y", str(y_off))
        box.set("width", "250")
        box.set("height", "42")
        box.set("rx", "8")
        box.set("fill", WHITE)
        box.set("stroke", DANGER)
        box.set("stroke-width", "1.5")

        ft = ET.SubElement(svg, "text")
        ft.set("x", "32")
        ft.set("y", str(y_off + 18))
        ft.set("font-size", "12")
        ft.set("font-weight", "bold")
        ft.set("fill", DARK)
        ft.text = ftype

        fd = ET.SubElement(svg, "text")
        fd.set("x", "32")
        fd.set("y", str(y_off + 34))
        fd.set("font-size", "10")
        fd.set("fill", GRAY)
        fd.text = fdesc

        y_off += 50

    # First aid for fractures
    add_section_label(svg, 20, 228, "Первая помощь при переломах", GREEN)

    frac_steps = [
        "1. Вызовите скорую помощь: 103 или 112",
        "2. Обеспечьте неподвижность конечности",
        "3. Наложите шину из подручных средств",
        "4. Шина фиксирует 2 сустава выше и ниже",
        "5. При открытом — остановите кровь",
        "6. Приложите холод к месту перелома",
        "7. Дайте обезболивающее",
    ]

    y_pos = 250
    for step in frac_steps:
        parts = step.split(". ", 1)
        add_numbered_step(svg, 20, y_pos, parts[0], parts[1], GREEN)
        y_pos += 24

    # Right column: Burns
    add_section_label(svg, 430, 98, "Ожоги: степени", ORANGE)

    burn_degrees = [
        ("I степень", "Покраснение, боль, отёк", YELLOW_WARN, "Лёгкая"),
        ("II степень", "Пузыри с жидкостью, сильная боль", ORANGE, "Средняя"),
        ("III степень", "Омертвение кожи, струпья", DANGER, "Тяжёлая"),
        ("IV степень", "Обугливание тканей, костей", DARK, "Крайне тяжёлая"),
    ]

    y_off = 118
    for degree, desc, color, severity in burn_degrees:
        box = ET.SubElement(svg, "rect")
        box.set("x", "430")
        box.set("y", str(y_off))
        box.set("width", "350")
        box.set("height", "42")
        box.set("rx", "8")
        box.set("fill", WHITE)
        box.set("stroke", color)
        box.set("stroke-width", "1.5")

        # Degree badge
        db = ET.SubElement(svg, "rect")
        db.set("x", "440")
        db.set("y", str(y_off + 8))
        db.set("width", "80")
        db.set("height", "26")
        db.set("rx", "6")
        db.set("fill", color)

        dt = ET.SubElement(svg, "text")
        dt.set("x", "480")
        dt.set("y", str(y_off + 26))
        dt.set("text-anchor", "middle")
        dt.set("font-size", "11")
        dt.set("font-weight", "bold")
        dt.set("fill", WHITE)
        dt.text = degree

        dd = ET.SubElement(svg, "text")
        dd.set("x", "530")
        dd.set("y", str(y_off + 26))
        dd.set("font-size", "11")
        dd.set("fill", DARK)
        dd.text = desc

        # Severity
        sv = ET.SubElement(svg, "text")
        sv.set("x", "760")
        sv.set("y", str(y_off + 26))
        sv.set("text-anchor", "end")
        sv.set("font-size", "10")
        sv.set("fill", color)
        sv.set("font-weight", "bold")
        sv.text = severity

        y_off += 48

    # First aid for burns
    add_section_label(svg, 430, 320, "Первая помощь при ожогах", GREEN)

    burn_aid = [
        "1. Уберите источник ожога",
        "2. Охлаждайте ожог прохладной водой 10-20 мин",
        "3. Наложите стерильную повязку",
        "4. Дайте обезболивающее",
        "5. При обширных ожогах — вызовите скорую",
    ]

    y_pos = 342
    for step in burn_aid:
        parts = step.split(". ", 1)
        add_numbered_step(svg, 430, y_pos, parts[0], parts[1], GREEN)
        y_pos += 24

    # DO NOT DO section
    add_section_label(svg, 20, 440, "Чего делать НЕЛЬЗЯ", DANGER)

    donts = [
        "НЕ вставляйте кость обратно при открытом переломе",
        "НЕ снимайте одежду, прилипшую к ожогу",
        "НЕ смазывайте ожог маслом или кремом",
        "НЕ прикладывайте лёд напрямую к коже",
        "НЕ вскрывайте пузыри при ожоге II степени",
        "НЕ двигайте сломанную конечность без шины",
    ]

    y_pos = 462
    for dont in donts:
        add_danger_sign(svg, 34, y_pos + 6, 8)
        dt = ET.SubElement(svg, "text")
        dt.set("x", "52")
        dt.set("y", str(y_pos + 10))
        dt.set("font-size", "11")
        dt.set("fill", DANGER)
        display = dont[:60] + "..." if len(dont) > 63 else dont
        dt.text = display
        y_pos += 20

    # Right: Important note
    note = ET.SubElement(svg, "rect")
    note.set("x", "430")
    note.set("y", "470")
    note.set("width", "350")
    note.set("height", "70")
    note.set("rx", "10")
    note.set("fill", "#FEF2F2")
    note.set("stroke", DANGER)
    note.set("stroke-width", "2")

    add_warning_sign(svg, 460, 505, 18, "!")

    nt = ET.SubElement(svg, "text")
    nt.set("x", "488")
    nt.set("y", "498")
    nt.set("font-size", "12")
    nt.set("font-weight", "bold")
    nt.set("fill", DANGER)
    nt.text = "Главное правило!"

    nb = ET.SubElement(svg, "text")
    nb.set("x", "488")
    nb.set("y", "518")
    nb.set("font-size", "11")
    nb.set("fill", DARK)
    nb.text = "Не навредите! Неправильная помощь может усугубить"

    nb2 = ET.SubElement(svg, "text")
    nb2.set("x", "488")
    nb2.set("y", "533")
    nb2.set("font-size", "11")
    nb2.set("fill", DARK)
    nb2.text = "состояние пострадавшего. Вызывайте специалистов."

    add_footer(svg)
    return svg


# ============================================================
# MAIN: Generate all lessons
# ============================================================
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    generators = [
        (1, generate_lesson1),
        (2, generate_lesson2),
        (3, generate_lesson3),
        (4, generate_lesson4),
        (5, generate_lesson5),
        (6, generate_lesson6),
        (7, generate_lesson7),
    ]

    results = []
    for num, gen_func in generators:
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
        try:
            svg = gen_func()

            # Validate by converting to string and parsing back
            tree = ET.ElementTree(svg)
            ET.indent(tree, space="  ")

            # Write the file
            tree.write(filepath, encoding="unicode", xml_declaration=True)

            # Validate the written file
            validate_tree = ET.parse(filepath)
            root = validate_tree.getroot()

            # Check dimensions
            w = root.get("width")
            h = root.get("height")

            # Count elements
            count = sum(1 for _ in root.iter())

            results.append(f"✅ lesson-{num}.svg — {w}x{h}, {count} elements, valid XML")
        except Exception as e:
            results.append(f"❌ lesson-{num}.svg — ERROR: {e}")

    print("=" * 60)
    print("Grade 7 Safety SVG Generation Results")
    print("=" * 60)
    for r in results:
        print(r)
    print("=" * 60)

    # Final validation pass
    print("\nFinal XML Validation:")
    all_valid = True
    for num in range(1, 8):
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            # Check no unescaped characters
            xml_str = ET.tostring(root, encoding="unicode")
            # Re-parse to ensure validity
            ET.fromstring(xml_str)
            size = os.path.getsize(filepath)
            print(f"  lesson-{num}.svg: VALID ({size:,} bytes)")
        except ET.ParseError as e:
            all_valid = False
            print(f"  lesson-{num}.svg: INVALID — {e}")
        except Exception as e:
            all_valid = False
            print(f"  lesson-{num}.svg: ERROR — {e}")

    if all_valid:
        print("\n🎉 All 7 SVG files generated and validated successfully!")
    else:
        print("\n⚠️ Some files have validation issues.")

    return all_valid


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
