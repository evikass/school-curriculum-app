#!/usr/bin/env python3
"""Generate 10 detailed SVG files for Grade 11 Chemistry lessons."""

import xml.etree.ElementTree as ET
import os

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade11/chemistry"
PRIMARY = "#2E7D32"
PRIMARY_DARK = "#1B5E20"
PRIMARY_LIGHT = "#81C784"
BG = "#E8F5E9"
BG_LIGHT = "#F1F8E9"
PANEL_START = "#43A047"
PANEL_END = "#2E7D32"
WHITE = "#FFFFFF"
GRAY = "#777777"
DARK = "#333333"
ACCENT = "#66BB6A"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─────────────────────────────────────────────────────
# Utility helpers
# ─────────────────────────────────────────────────────

def escape(text):
    """XML-escape text."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def svg_root():
    """Create base SVG element with viewBox."""
    return ET.Element("svg", {
        "xmlns": "http://www.w3.org/2000/svg",
        "viewBox": "0 0 500 350",
    })


def add_defs(svg):
    """Add gradient defs."""
    defs = ET.SubElement(svg, "defs")
    # Background gradient
    lg = ET.SubElement(defs, "linearGradient", {"id": "bg", "x1": "0", "y1": "0", "x2": "0", "y2": "1"})
    ET.SubElement(lg, "stop", {"offset": "0%", "stop-color": BG})
    ET.SubElement(lg, "stop", {"offset": "100%", "stop-color": WHITE})
    # Panel gradient
    lg2 = ET.SubElement(defs, "linearGradient", {"id": "panel", "x1": "0", "y1": "0", "x2": "1", "y2": "0"})
    ET.SubElement(lg2, "stop", {"offset": "0%", "stop-color": PANEL_START})
    ET.SubElement(lg2, "stop", {"offset": "100%", "stop-color": PANEL_END})


def add_frame(svg):
    """Outer frame + background fill."""
    ET.SubElement(svg, "rect", {"width": "500", "height": "350", "fill": "url(#bg)", "rx": "10"})
    ET.SubElement(svg, "rect", {
        "x": "3", "y": "3", "width": "494", "height": "344",
        "rx": "8", "fill": "none", "stroke": PRIMARY, "stroke-width": "2.5"
    })


def add_header(svg, title, lesson_num):
    """Title + subtitle line."""
    ET.SubElement(svg, "text", {
        "x": "250", "y": "42", "font-family": "Arial,sans-serif",
        "font-size": "19", "font-weight": "bold", "fill": PRIMARY,
        "text-anchor": "middle"
    }).text = title
    ET.SubElement(svg, "text", {
        "x": "250", "y": "62", "font-family": "Arial,sans-serif",
        "font-size": "12", "fill": GRAY, "text-anchor": "middle"
    }).text = f"Химия — Урок {lesson_num}"
    ET.SubElement(svg, "line", {
        "x1": "30", "y1": "72", "x2": "470", "y2": "72",
        "stroke": PRIMARY, "stroke-width": "2", "opacity": "0.25"
    })


def add_footer(svg):
    """Footer text."""
    ET.SubElement(svg, "text", {
        "x": "250", "y": "340", "font-family": "Arial,sans-serif",
        "font-size": "11", "fill": GRAY, "text-anchor": "middle"
    }).text = "Химия · 11 класс"


def add_clip(svg, clip_id="ill"):
    """Clip-path for content area."""
    cp = ET.SubElement(svg, "defs")
    cl = ET.SubElement(cp, "clipPath", {"id": clip_id})
    ET.SubElement(cl, "rect", {"x": "15", "y": "80", "width": "470", "height": "225", "rx": "6"})


def t(svg, x, y, text, size=12, fill=DARK, anchor="middle", weight="normal", family="Arial,sans-serif"):
    """Add text element helper."""
    attrs = {
        "x": str(x), "y": str(y),
        "font-family": family, "font-size": str(size),
        "fill": fill, "text-anchor": anchor, "font-weight": weight
    }
    el = ET.SubElement(svg, "text", attrs)
    el.text = text
    return el


def rect(svg, x, y, w, h, fill, rx=0, stroke=None, sw=1, opacity=None):
    """Add rect element helper."""
    attrs = {"x": str(x), "y": str(y), "width": str(w), "height": str(h), "fill": fill, "rx": str(rx)}
    if stroke:
        attrs["stroke"] = stroke
        attrs["stroke-width"] = str(sw)
    if opacity is not None:
        attrs["opacity"] = str(opacity)
    return ET.SubElement(svg, "rect", attrs)


def circle(svg, cx, cy, r, fill, stroke=None, sw=1, opacity=None):
    attrs = {"cx": str(cx), "cy": str(cy), "r": str(r), "fill": fill}
    if stroke:
        attrs["stroke"] = stroke
        attrs["stroke-width"] = str(sw)
    if opacity is not None:
        attrs["opacity"] = str(opacity)
    return ET.SubElement(svg, "circle", attrs)


def line(svg, x1, y1, x2, y2, stroke=PRIMARY, sw=1, dash=None, opacity=None):
    attrs = {"x1": str(x1), "y1": str(y1), "x2": str(x2), "y2": str(y2), "stroke": stroke, "stroke-width": str(sw)}
    if dash:
        attrs["stroke-dasharray"] = dash
    if opacity is not None:
        attrs["opacity"] = str(opacity)
    return ET.SubElement(svg, "line", attrs)


def arrow(svg, x1, y1, x2, y2, stroke=PRIMARY, sw=1.5):
    """Line with arrowhead marker."""
    marker_id = f"arr_{x1}_{y1}_{x2}_{y2}".replace(".", "_").replace("-", "m")
    # Add marker to defs
    defs = svg.find("defs")
    if defs is None:
        defs = ET.SubElement(svg, "defs")
    marker = ET.SubElement(defs, "marker", {
        "id": marker_id, "markerWidth": "10", "markerHeight": "7",
        "refX": "10", "refY": "3.5", "orient": "auto"
    })
    ET.SubElement(marker, "polygon", {"points": "0 0, 10 3.5, 0 7", "fill": stroke})
    attrs = {
        "x1": str(x1), "y1": str(y1), "x2": str(x2), "y2": str(y2),
        "stroke": stroke, "stroke-width": str(sw),
        "marker-end": f"url(#{marker_id})"
    }
    return ET.SubElement(svg, "line", attrs)


def content_bg(svg):
    """Background for content area."""
    rect(svg, 15, 80, 470, 225, BG_LIGHT, rx=6, opacity=0.5)


# ─────────────────────────────────────────────────────
# LESSON GENERATORS
# ─────────────────────────────────────────────────────

def lesson1():
    """Амины — Amines."""
    svg = svg_root()
    add_defs(svg)
    add_frame(svg)
    add_header(svg, "Амины", 1)
    add_clip(svg)
    g = ET.SubElement(svg, "g", {"clip-path": "url(#ill)"})
    content_bg(g)

    # Left: Amine classification
    rect(g, 25, 88, 215, 90, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 132, 104, "Классификация аминов", 12, PRIMARY, weight="bold")
    t(g, 132, 122, "Первичные: R—NH₂", 11, DARK)
    t(g, 132, 138, "Вторичные: R₂—NH", 11, DARK)
    t(g, 132, 154, "Третичные: R₃—N", 11, DARK)
    t(g, 132, 170, "Аминогруппа: —NH₂", 11, PRIMARY_DARK)

    # Right: Methylamine structure
    rect(g, 260, 88, 215, 90, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 367, 104, "Метиламин CH₃NH₂", 12, PRIMARY, weight="bold")
    # Simple molecule diagram: N — C
    circle(g, 320, 138, 14, "#1565C0", stroke="#0D47A1", sw=1.5)  # N blue
    t(g, 320, 143, "N", 11, WHITE, weight="bold")
    circle(g, 370, 138, 14, "#424242", stroke="#212121", sw=1.5)  # C gray
    t(g, 370, 143, "C", 11, WHITE, weight="bold")
    line(g, 334, 138, 356, 138, stroke=DARK, sw=2)
    # H atoms on N
    t(g, 305, 115, "H", 10, "#666")
    t(g, 305, 158, "H", 10, "#666")
    line(g, 312, 127, 318, 132, stroke="#999", sw=1)
    line(g, 312, 149, 318, 145, stroke="#999", sw=1)
    # H atoms on C
    t(g, 395, 122, "H", 10, "#666")
    t(g, 395, 152, "H", 10, "#666")
    t(g, 405, 137, "H", 10, "#666")

    # Bottom left: Properties
    rect(g, 25, 186, 215, 75, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 132, 202, "Свойства аминов", 12, PRIMARY, weight="bold")
    t(g, 132, 218, "• Основания (протонируют H⁺)", 10, DARK)
    t(g, 132, 232, "• Горят: 4C₂H₅NH₂+15O₂→", 10, DARK)
    t(g, 132, 246, "  8CO₂+14H₂O+2N₂", 10, DARK)

    # Bottom right: Reactions
    rect(g, 260, 186, 215, 75, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 367, 202, "Химические реакции", 12, PRIMARY, weight="bold")
    t(g, 367, 218, "• С кислотами: R—NH₂+HCl→", 10, DARK)
    t(g, 367, 232, "  R—NH₃⁺Cl⁻ (соль)", 10, DARK)
    t(g, 367, 246, "• Алкилирование, ацилирование", 10, DARK)

    # Footer icon area
    rect(g, 25, 270, 450, 28, PRIMARY, rx=5, opacity=0.1)
    t(g, 250, 289, "Анилин — простейший ароматический амин (C₆H₅NH₂)", 11, PRIMARY_DARK)

    add_footer(svg)
    return svg


def lesson2():
    """Аминокислоты — Amino acids."""
    svg = svg_root()
    add_defs(svg)
    add_frame(svg)
    add_header(svg, "Аминокислоты", 2)
    add_clip(svg)
    g = ET.SubElement(svg, "g", {"clip-path": "url(#ill)"})
    content_bg(g)

    # General structure
    rect(g, 25, 88, 450, 65, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 250, 104, "Общая формула аминокислот", 13, PRIMARY, weight="bold")
    t(g, 250, 124, "H₂N—CH(R)—COOH", 16, DARK, weight="bold")
    t(g, 250, 143, "Аминогруппа (основные св-ва) + Карбоксильная группа (кислотные св-ва)", 10, GRAY)

    # Zwitterion
    rect(g, 25, 160, 220, 75, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 135, 176, "Цвиттер-ион", 12, PRIMARY, weight="bold")
    t(g, 135, 194, "H₃N⁺—CH(R)—COO⁻", 11, DARK, weight="bold")
    t(g, 135, 210, "Внутренняя соль в растворе", 10, GRAY)
    t(g, 135, 224, "pH ≠ 7 → изоэлектрическая точка", 10, GRAY)

    # Essential amino acids
    rect(g, 255, 160, 220, 75, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 365, 176, "Незаменимые аминокислоты", 12, PRIMARY, weight="bold")
    t(g, 365, 194, "Валин, Лейцин, Изолейцин", 10, DARK)
    t(g, 365, 208, "Лизин, Метионин, Треонин", 10, DARK)
    t(g, 365, 222, "Фенилаланин, Триптофан", 10, DARK)

    # Peptide bond
    rect(g, 25, 242, 450, 58, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 250, 258, "Пептидная связь (амидная)", 12, PRIMARY, weight="bold")
    t(g, 250, 275, "—CO—NH—   образуется при конденсации аминокислот", 11, DARK)
    t(g, 250, 290, "n аминокислот → полипептид + (n−1)H₂O", 10, GRAY)

    add_footer(svg)
    return svg


def lesson3():
    """Белки — Proteins."""
    svg = svg_root()
    add_defs(svg)
    add_frame(svg)
    add_header(svg, "Белки", 3)
    add_clip(svg)
    g = ET.SubElement(svg, "g", {"clip-path": "url(#ill)"})
    content_bg(g)

    # Structure levels
    rect(g, 25, 88, 220, 105, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 135, 104, "Уровни структуры", 13, PRIMARY, weight="bold")
    # Primary
    t(g, 42, 122, "①", 12, PRIMARY, weight="bold", anchor="start")
    t(g, 60, 122, "Первичная — последовательность", 10, DARK, anchor="start")
    t(g, 42, 137, "②", 12, PRIMARY, weight="bold", anchor="start")
    t(g, 60, 137, "Вторичная — α-спираль, β-слой", 10, DARK, anchor="start")
    t(g, 42, 152, "③", 12, PRIMARY, weight="bold", anchor="start")
    t(g, 60, 152, "Третичная — глобула (H-связи)", 10, DARK, anchor="start")
    t(g, 42, 167, "④", 12, PRIMARY, weight="bold", anchor="start")
    t(g, 60, 167, "Четвертичная — несколько цепей", 10, DARK, anchor="start")
    t(g, 42, 182, "   Пример: гемоглобин (4 цепи)", 9, GRAY, anchor="start")

    # Denaturation
    rect(g, 255, 88, 220, 105, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 365, 104, "Денатурация белков", 13, PRIMARY, weight="bold")
    t(g, 365, 124, "Нарушение структуры:", 11, DARK)
    t(g, 365, 140, "• Нагревание (t > 60°C)", 10, DARK)
    t(g, 365, 154, "• Кислоты и щёлочи", 10, DARK)
    t(g, 365, 168, "• Соли тяжёлых металлов", 10, DARK)
    t(g, 365, 182, "• Радиация, органич. раствор.", 10, DARK)

    # Color reactions
    rect(g, 25, 200, 450, 98, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 250, 218, "Качественные реакции на белки", 13, PRIMARY, weight="bold")
    # Two columns
    t(g, 135, 238, "Биуретовая реакция", 11, DARK, weight="bold")
    t(g, 135, 254, "NaOH + CuSO₄ → фиолетовый", 10, DARK)
    t(g, 135, 268, "(на пептидные связи)", 9, GRAY)

    t(g, 365, 238, "Ксантопротеиновая реакция", 11, DARK, weight="bold")
    t(g, 365, 254, "HNO₃(конц.) → жёлтый цвет", 10, DARK)
    t(g, 365, 268, "(на ароматические радикалы)", 9, GRAY)

    t(g, 250, 290, "Горение: запах жжёных перьев (N, S в составе)", 10, PRIMARY_DARK)

    add_footer(svg)
    return svg


def lesson4():
    """Нуклеиновые кислоты — Nucleic acids."""
    svg = svg_root()
    add_defs(svg)
    add_frame(svg)
    add_header(svg, "Нуклеиновые кислоты", 4)
    add_clip(svg)
    g = ET.SubElement(svg, "g", {"clip-path": "url(#ill)"})
    content_bg(g)

    # DNA / RNA comparison
    rect(g, 25, 88, 215, 120, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 132, 104, "ДНК (DNA)", 13, "#1565C0", weight="bold")
    t(g, 132, 122, "Дезоксирибонуклеиновая", 10, DARK)
    t(g, 132, 136, "Сахар: дезоксирибоза", 10, DARK)
    t(g, 132, 150, "Основания: A, T, G, C", 10, DARK)
    t(g, 132, 164, "Двойная спираль", 10, DARK)
    t(g, 132, 178, "A↔T (2 H-связи)", 10, "#1565C0")
    t(g, 132, 192, "G↔C (3 H-связи)", 10, "#1565C0")

    rect(g, 260, 88, 215, 120, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 367, 104, "РНК (RNA)", 13, "#C62828", weight="bold")
    t(g, 367, 122, "Рибонуклеиновая", 10, DARK)
    t(g, 367, 136, "Сахар: рибоза", 10, DARK)
    t(g, 367, 150, "Основания: A, U, G, C", 10, DARK)
    t(g, 367, 164, "Одинарная цепь", 10, DARK)
    t(g, 367, 178, "U вместо T", 10, "#C62828")
    t(g, 367, 192, "иРНК, тРНК, рРНК", 10, "#C62828")

    # Nucleotide structure
    rect(g, 25, 215, 450, 82, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 250, 233, "Структура нуклеотида", 13, PRIMARY, weight="bold")

    # Diagram: Phosphate - Sugar - Base
    rect(g, 60, 248, 90, 30, "#FFCDD2", rx=4, stroke="#E53935", sw=1)
    t(g, 105, 268, "Фосфат", 11, "#C62828")

    t(g, 165, 268, "—", 14, DARK)

    rect(g, 185, 248, 90, 30, "#C8E6C9", rx=4, stroke=PRIMARY, sw=1)
    t(g, 230, 268, "Сахар", 11, PRIMARY_DARK)

    t(g, 290, 268, "—", 14, DARK)

    rect(g, 310, 248, 110, 30, "#BBDEFB", rx=4, stroke="#1565C0", sw=1)
    t(g, 365, 268, "Азот. основание", 11, "#1565C0")

    t(g, 250, 292, "Правило Чаргаффа: [A]=[T], [G]=[C] (в ДНК)", 10, GRAY)

    add_footer(svg)
    return svg


def lesson5():
    """Полимеры — Polymers."""
    svg = svg_root()
    add_defs(svg)
    add_frame(svg)
    add_header(svg, "Полимеры", 5)
    add_clip(svg)
    g = ET.SubElement(svg, "g", {"clip-path": "url(#ill)"})
    content_bg(g)

    # Polymerization vs Polycondensation
    rect(g, 25, 88, 215, 100, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 132, 104, "Полимеризация", 13, PRIMARY, weight="bold")
    t(g, 132, 122, "nCH₂=CH₂ → (—CH₂—CH₂—)n", 11, DARK)
    t(g, 132, 138, "Без побочных продуктов", 10, GRAY)
    t(g, 132, 156, "Примеры:", 10, DARK, weight="bold")
    t(g, 132, 170, "Полиэтилен, полипропилен,", 10, DARK)
    t(g, 132, 184, "поливинилхлорид (ПВХ)", 10, DARK)

    rect(g, 260, 88, 215, 100, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 367, 104, "Поликонденсация", 13, PRIMARY, weight="bold")
    t(g, 367, 122, "Мономеры → Полимер + H₂O", 11, DARK)
    t(g, 367, 138, "Выделяется вода", 10, GRAY)
    t(g, 367, 156, "Примеры:", 10, DARK, weight="bold")
    t(g, 367, 170, "Фенолформальдегидная смола", 10, DARK)
    t(g, 367, 184, "Капрон, лавсан", 10, DARK)

    # Classification
    rect(g, 25, 196, 215, 105, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 132, 212, "Классификация", 13, PRIMARY, weight="bold")
    t(g, 132, 230, "По происхождению:", 10, DARK, weight="bold")
    t(g, 132, 244, "• Натуральные (каучук, шёлк)", 10, DARK)
    t(g, 132, 258, "• Искусственные (целлулоид)", 10, DARK)
    t(g, 132, 272, "• Синтетические (ПЭ, ПВХ)", 10, DARK)
    t(g, 132, 292, "По отношению к нагреву:", 10, DARK, weight="bold")

    # Thermoplastic vs thermosetting
    rect(g, 260, 196, 215, 105, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 367, 212, "Термопластичные", 11, PRIMARY, weight="bold")
    t(g, 367, 228, "Размягчаются при нагреве", 10, DARK)
    t(g, 367, 242, "Можно переплавлять", 10, GRAY)
    t(g, 367, 262, "Термореактивные", 11, PRIMARY, weight="bold")
    t(g, 367, 278, "Не размягчаются, разрушаются", 10, DARK)
    t(g, 367, 292, " необратимая сшивка", 10, GRAY)

    add_footer(svg)
    return svg


def lesson6():
    """Природные полимеры — Natural polymers."""
    svg = svg_root()
    add_defs(svg)
    add_frame(svg)
    add_header(svg, "Природные полимеры", 6)
    add_clip(svg)
    g = ET.SubElement(svg, "g", {"clip-path": "url(#ill)"})
    content_bg(g)

    # Polysaccharides
    rect(g, 25, 88, 450, 68, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 250, 104, "Полисахариды — (C₆H₁₀O₅)n", 13, PRIMARY, weight="bold")
    t(g, 132, 124, "Крахмал: запасающее вещество растений", 10, DARK)
    t(g, 132, 138, "Целлюлоза: структурный компонент клеточной стенки", 10, DARK)
    t(g, 132, 152, "Гликоген: запасающее вещество животных (животный крахмал)", 10, DARK)

    # Cellulose vs Starch
    rect(g, 25, 163, 215, 110, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 132, 179, "Целлюлоза", 13, PRIMARY, weight="bold")
    t(g, 132, 197, "β-гликозидные связи", 10, DARK)
    t(g, 132, 211, "Не усваивается человеком", 10, DARK)
    t(g, 132, 225, "(нет фермента целлюлазы)", 9, GRAY)
    t(g, 132, 243, "Степень полимеризации:", 10, DARK)
    t(g, 132, 257, "n = 2000–15000", 11, PRIMARY_DARK, weight="bold")
    t(g, 132, 269, "Волокна: хлопок, лён", 9, GRAY)

    rect(g, 260, 163, 215, 110, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 367, 179, "Крахмал", 13, PRIMARY, weight="bold")
    t(g, 367, 197, "α-гликозидные связи", 10, DARK)
    t(g, 367, 211, "Усваивается человеком", 10, DARK)
    t(g, 367, 225, "(амилаза в слюне)", 9, GRAY)
    t(g, 367, 243, "Амилоза + Амилопектин:", 10, DARK)
    t(g, 367, 257, "линейная + разветвлённая", 11, PRIMARY_DARK, weight="bold")
    t(g, 367, 269, "Йод → синее окрашивание", 9, "#1565C0")

    # Reactions
    rect(g, 25, 280, 450, 22, PRIMARY, rx=4, opacity=0.12)
    t(g, 250, 296, "Гидролиз: (C₆H₁₀O₅)n + nH₂O → nC₆H₁₂O₆ (глюкоза)", 10, PRIMARY_DARK)

    add_footer(svg)
    return svg


def lesson7():
    """Каучуки и резины — Rubbers and resins."""
    svg = svg_root()
    add_defs(svg)
    add_frame(svg)
    add_header(svg, "Каучуки и резины", 7)
    add_clip(svg)
    g = ET.SubElement(svg, "g", {"clip-path": "url(#ill)"})
    content_bg(g)

    # Natural rubber
    rect(g, 25, 88, 215, 115, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 132, 104, "Натуральный каучук", 12, PRIMARY, weight="bold")
    t(g, 132, 122, "изопрен: CH₂=C(CH₃)—CH=CH₂", 10, DARK)
    t(g, 132, 140, "Полимеризация изопрена:", 10, DARK)
    t(g, 132, 156, "nC₅H₈ → (—C₅H₈—)n", 11, PRIMARY_DARK, weight="bold")
    t(g, 132, 172, "цис-1,4-полиизопрен", 10, DARK)
    t(g, 132, 188, "Источник: сок гевеи", 10, GRAY)
    t(g, 132, 200, "Эластичный, липкий", 10, GRAY)

    # Synthetic rubber
    rect(g, 260, 88, 215, 115, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 367, 104, "Синтетические каучуки", 12, PRIMARY, weight="bold")
    t(g, 367, 122, "Бутадиеновый (СКБ):", 10, DARK)
    t(g, 367, 136, "nCH₂=CH—CH=CH₂", 10, DARK)
    t(g, 367, 152, "Изопреновый (СКИ):", 10, DARK)
    t(g, 367, 166, "nCH₂=C(CH₃)—CH=CH₂", 10, DARK)
    t(g, 367, 182, "Хлоропреновый, бутadiен-", 10, DARK)
    t(g, 367, 196, "нитрильный, силиконовый", 10, DARK)

    # Vulcanization
    rect(g, 25, 210, 450, 92, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 250, 228, "Вулканизация", 14, PRIMARY, weight="bold")
    t(g, 250, 248, "Каучук + S (серa) → Резина  (t° = 140–160°C)", 12, DARK)
    # Schematic diagram
    t(g, 80, 272, "Линейные цепи", 10, DARK)
    arrow(g, 150, 269, 200, 269, stroke=PRIMARY)
    t(g, 270, 272, "Сшивка серой (S)", 10, DARK, weight="bold")
    arrow(g, 350, 269, 400, 269, stroke=PRIMARY)
    t(g, 440, 272, "Резина", 10, PRIMARY_DARK, weight="bold")

    t(g, 250, 294, "Резина: прочная, упругая, нерастворимая, стойкая к износу", 10, GRAY)

    add_footer(svg)
    return svg


def lesson8():
    """Витамины — Vitamins."""
    svg = svg_root()
    add_defs(svg)
    add_frame(svg)
    add_header(svg, "Витамины", 8)
    add_clip(svg)
    g = ET.SubElement(svg, "g", {"clip-path": "url(#ill)"})
    content_bg(g)

    # Fat-soluble
    rect(g, 25, 88, 215, 130, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 132, 104, "Жирорастворимые", 12, PRIMARY, weight="bold")
    t(g, 45, 122, "A", 11, "#E65100", weight="bold", anchor="start")
    t(g, 62, 122, "— зрение, кожа (ретинол)", 10, DARK, anchor="start")
    t(g, 45, 138, "D", 11, "#E65100", weight="bold", anchor="start")
    t(g, 62, 138, "— кальций, кости (кальциферол)", 10, DARK, anchor="start")
    t(g, 45, 154, "E", 11, "#E65100", weight="bold", anchor="start")
    t(g, 62, 154, "— антиоксидант (токоферол)", 10, DARK, anchor="start")
    t(g, 45, 170, "K", 11, "#E65100", weight="bold", anchor="start")
    t(g, 62, 170, "— свёртывание крови (филлохинон)", 10, DARK, anchor="start")
    t(g, 132, 190, "Накапливаются в жировой ткани", 9, GRAY)
    t(g, 132, 204, "Опасна передозировка!", 9, "#C62828")

    # Water-soluble
    rect(g, 260, 88, 215, 130, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 367, 104, "Водорастворимые", 12, PRIMARY, weight="bold")
    t(g, 278, 122, "B₁", 10, "#1565C0", weight="bold", anchor="start")
    t(g, 298, 122, "— тиамин (энергетика)", 9, DARK, anchor="start")
    t(g, 278, 138, "B₂", 10, "#1565C0", weight="bold", anchor="start")
    t(g, 298, 138, "— рибофлавин (метаболизм)", 9, DARK, anchor="start")
    t(g, 278, 154, "B₆", 10, "#1565C0", weight="bold", anchor="start")
    t(g, 298, 154, "— пиридоксин (нервн. сис-ма)", 9, DARK, anchor="start")
    t(g, 278, 170, "B₁₂", 10, "#1565C0", weight="bold", anchor="start")
    t(g, 302, 170, "— кобаламин (кроветвор.)", 9, DARK, anchor="start")
    t(g, 278, 186, "C", 10, "#1565C0", weight="bold", anchor="start")
    t(g, 298, 186, "— аскорбиновая к-та (иммун.)", 9, DARK, anchor="start")
    t(g, 278, 202, "PP", 10, "#1565C0", weight="bold", anchor="start")
    t(g, 298, 202, "— ниацин (кожа, нервн. с-ма)", 9, DARK, anchor="start")
    t(g, 367, 214, "Не накапливаются, выводятся", 9, GRAY)

    # Avitaminosis
    rect(g, 25, 225, 450, 78, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 250, 243, "Заболевания при недостатке витаминов", 12, PRIMARY, weight="bold")
    t(g, 132, 262, "C → цинга (кровоточивость)", 10, DARK)
    t(g, 132, 276, "D → рахит (деформация костей)", 10, DARK)
    t(g, 367, 262, "A → куриная слепота", 10, DARK)
    t(g, 367, 276, "B₁ → бери-бери (нервн. с-ма)", 10, DARK)
    t(g, 250, 296, "Гиповитаминоз — недостаток, Гипервитаминоз — избыток", 9, GRAY)

    add_footer(svg)
    return svg


def lesson9():
    """Лекарственные вещества — Medicinal substances."""
    svg = svg_root()
    add_defs(svg)
    add_frame(svg)
    add_header(svg, "Лекарственные вещества", 9)
    add_clip(svg)
    g = ET.SubElement(svg, "g", {"clip-path": "url(#ill)"})
    content_bg(g)

    # Classification
    rect(g, 25, 88, 215, 130, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 132, 104, "Классификация лекарств", 12, PRIMARY, weight="bold")
    t(g, 132, 124, "• Анальгетики (обезболивание)", 10, DARK)
    t(g, 132, 138, "• Антибиотики (против бактерий)", 10, DARK)
    t(g, 132, 152, "• Антисептики (дезинфекция)", 10, DARK)
    t(g, 132, 166, "• Жаропонижающие", 10, DARK)
    t(g, 132, 180, "• Противовирусные", 10, DARK)
    t(g, 132, 194, "• Витаминные препараты", 10, DARK)
    t(g, 132, 210, "• Седативные, кардио и др.", 10, DARK)

    # Famous examples
    rect(g, 260, 88, 215, 130, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 367, 104, "Известные препараты", 12, PRIMARY, weight="bold")
    t(g, 367, 124, "Аспирин (ацетилсалициловая", 10, DARK)
    t(g, 367, 138, "  кислота) — жаропонижающее", 10, DARK)
    t(g, 367, 156, "Пенициллин — первый антибиотик", 10, DARK)
    t(g, 367, 170, "  (открыт А. Флемингом, 1928)", 9, GRAY)
    t(g, 367, 188, "Новокаин — местный анестетик", 10, DARK)
    t(g, 367, 204, "Йод, перекись H₂O₂ — антисептики", 10, DARK)

    # Safety rules
    rect(g, 25, 225, 450, 78, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 250, 243, "Правила безопасности", 13, "#C62828", weight="bold")
    t(g, 132, 262, "• По рецепту врача", 10, DARK)
    t(g, 132, 276, "• Соблюдать дозировку", 10, DARK)
    t(g, 367, 262, "• Проверять срок годности", 10, DARK)
    t(g, 367, 276, "• Хранить в недоступном для детей месте", 10, DARK)
    t(g, 250, 296, "Побочные эффекты, аллергия, привыкание — возможные последствия", 9, GRAY)

    add_footer(svg)
    return svg


def lesson10():
    """Химия и экология — Chemistry and ecology."""
    svg = svg_root()
    add_defs(svg)
    add_frame(svg)
    add_header(svg, "Химия и экология", 10)
    add_clip(svg)
    g = ET.SubElement(svg, "g", {"clip-path": "url(#ill)"})
    content_bg(g)

    # Pollution sources
    rect(g, 25, 88, 215, 115, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 132, 104, "Источники загрязнения", 12, "#C62828", weight="bold")
    t(g, 132, 124, "• ТЭС — CO₂, SO₂, NOₓ", 10, DARK)
    t(g, 132, 138, "• Хим. заводы — тяжёлые", 10, DARK)
    t(g, 132, 152, "  металлы (Pb, Hg, Cd)", 10, DARK)
    t(g, 132, 166, "• Автотранспорт — CO, NOₓ", 10, DARK)
    t(g, 132, 180, "• С/х — пестициды, нитраты", 10, DARK)
    t(g, 132, 194, "• Бытовые отходы — пластик", 10, DARK)

    # Environmental problems
    rect(g, 260, 88, 215, 115, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 367, 104, "Глобальные проблемы", 12, "#C62828", weight="bold")
    t(g, 367, 124, "Кислотные дожди:", 10, DARK, weight="bold")
    t(g, 367, 138, "SO₂+H₂O → H₂SO₃/H₂SO₄", 10, DARK)
    t(g, 367, 154, "Парниковый эффект:", 10, DARK, weight="bold")
    t(g, 367, 168, "CO₂, CH₄, N₂O ↑ температуру", 10, DARK)
    t(g, 367, 184, "Озоновые дыры:", 10, DARK, weight="bold")
    t(g, 367, 198, "Фреоны разрушают O₃ слой", 10, DARK)

    # Solutions
    rect(g, 25, 210, 450, 92, WHITE, rx=6, stroke=PRIMARY, sw=1.2)
    t(g, 250, 228, "Пути решения", 13, PRIMARY, weight="bold")
    t(g, 132, 248, "• Очистка выбросов (фильтры,", 10, DARK)
    t(g, 132, 262, "  скрубберы, электрофильтры)", 10, DARK)
    t(g, 132, 278, "• Безотходные технологии", 10, DARK)
    t(g, 132, 292, "• Переработка отходов", 10, DARK)
    t(g, 367, 248, "• Альтернативная энергетика", 10, DARK)
    t(g, 367, 262, "  (солнце, ветер, водород)", 10, DARK)
    t(g, 367, 278, "• Каталитические нейтрализаторы", 10, DARK)
    t(g, 367, 292, "• Биоразлагаемые полимеры", 10, DARK)

    add_footer(svg)
    return svg


# ─────────────────────────────────────────────────────
# MAIN: Generate all 10 SVGs
# ─────────────────────────────────────────────────────

generators = [
    lesson1, lesson2, lesson3, lesson4, lesson5,
    lesson6, lesson7, lesson8, lesson9, lesson10
]

titles = [
    "Амины", "Аминокислоты", "Белки", "Нуклеиновые кислоты", "Полимеры",
    "Природные полимеры", "Каучуки и резины", "Витамины",
    "Лекарственные вещества", "Химия и экология"
]

for i, gen in enumerate(generators, 1):
    svg = gen()
    # Indent for readability
    ET.indent(svg, space="  ")
    filepath = os.path.join(OUTPUT_DIR, f"lesson{i}.svg")
    tree = ET.ElementTree(svg)
    tree.write(filepath, encoding="unicode", xml_declaration=True)

    # Validate as XML
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        # Re-parse to validate
        ET.fromstring(content)
        print(f"✅ lesson{i}.svg — {titles[i-1]} — valid XML ({len(content)} bytes)")
    except ET.ParseError as e:
        print(f"❌ lesson{i}.svg — XML INVALID: {e}")

print(f"\nDone! 10 SVGs written to {OUTPUT_DIR}")
