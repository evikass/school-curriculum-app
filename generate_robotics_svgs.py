#!/usr/bin/env python3
"""Generate 8 detailed educational SVG images for Grade 8 Robotics lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/robotics"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Color palette ──────────────────────────────────────────────
PRIMARY = "#0284C7"
PRIMARY_LIGHT = "#38BDF8"
PRIMARY_DARK = "#0369A1"
ACCENT_CYAN = "#06B6D4"
ACCENT_TEAL = "#14B8A6"
BG_DARK = "#0F172A"
BG_CARD = "#1E293B"
BG_CODE = "#0D1117"
TEXT_WHITE = "#F8FAFC"
TEXT_LIGHT = "#CBD5E1"
TEXT_MUTED = "#94A3B8"
HIGHLIGHT = "#F59E0B"
HIGHLIGHT2 = "#A78BFA"
SUCCESS = "#22C55E"
DANGER = "#EF4444"
BORDER = "#334155"

SVG_W, SVG_H = 800, 600


def escape(text):
    """Escape special XML characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def svg_root():
    """Create base SVG element with common attributes."""
    ET.register_namespace("", "http://www.w3.org/2000/svg")
    svg = ET.Element("svg", {
        "xmlns": "http://www.w3.org/2000/svg",
        "width": str(SVG_W),
        "height": str(SVG_H),
        "viewBox": f"0 0 {SVG_W} {SVG_H}",
    })
    return svg


def add_bg(svg):
    """Add dark background with grid pattern."""
    # Main background
    ET.SubElement(svg, "rect", {
        "width": str(SVG_W), "height": str(SVG_H), "fill": BG_DARK
    })
    # Grid pattern
    defs = ET.SubElement(svg, "defs")
    pattern = ET.SubElement(defs, "pattern", {
        "id": "grid", "width": "40", "height": "40",
        "patternUnits": "userSpaceOnUse"
    })
    ET.SubElement(pattern, "path", {
        "d": "M 40 0 L 0 0 0 40",
        "fill": "none", "stroke": "#1E293B", "stroke-width": "0.5"
    })
    ET.SubElement(svg, "rect", {
        "width": str(SVG_W), "height": str(SVG_H),
        "fill": "url(#grid)", "opacity": "0.5"
    })
    # Gradient overlay at top
    grad = ET.SubElement(defs, "linearGradient", {
        "id": "topGrad", x1: "0", y1: "0", x2: "0", y2: "1"
    }) if False else ET.SubElement(defs, "linearGradient", {
        "id": "topGrad", "x1": "0", "y1": "0", "x2": "0", "y2": "1"
    })
    ET.SubElement(grad, "stop", {"offset": "0%", "stop-color": PRIMARY, "stop-opacity": "0.15"})
    ET.SubElement(grad, "stop", {"offset": "100%", "stop-color": PRIMARY, "stop-opacity": "0"})
    ET.SubElement(svg, "rect", {
        "width": str(SVG_W), "height": "200",
        "fill": "url(#topGrad)"
    })


def add_title(svg, title, subtitle="", y_offset=0):
    """Add lesson title with decorative elements."""
    # Title background bar
    ET.SubElement(svg, "rect", {
        "x": "0", "y": str(10 + y_offset), "width": str(SVG_W), "height": "55",
        "fill": PRIMARY_DARK, "opacity": "0.9"
    })
    # Accent line
    ET.SubElement(svg, "rect", {
        "x": "0", "y": str(65 + y_offset), "width": str(SVG_W), "height": "3",
        "fill": PRIMARY_LIGHT
    })
    # Title text
    ET.SubElement(svg, "text", {
        "x": str(SVG_W // 2), "y": str(45 + y_offset),
        "text-anchor": "middle", "font-family": "Arial, sans-serif",
        "font-size": "22", "font-weight": "bold", "fill": TEXT_WHITE
    }).text = escape(title)
    if subtitle:
        ET.SubElement(svg, "text", {
            "x": str(SVG_W // 2), "y": str(82 + y_offset),
            "text-anchor": "middle", "font-family": "Arial, sans-serif",
            "font-size": "12", "fill": TEXT_MUTED
        }).text = escape(subtitle)


def add_card(svg, x, y, w, h, title="", fill=BG_CARD):
    """Add a rounded card element."""
    ET.SubElement(svg, "rect", {
        "x": str(x), "y": str(y), "width": str(w), "height": str(h),
        "rx": "8", "ry": "8", "fill": fill,
        "stroke": BORDER, "stroke-width": "1"
    })
    if title:
        # Card title bar
        ET.SubElement(svg, "rect", {
            "x": str(x), "y": str(y), "width": str(w), "height": "28",
            "rx": "8", "ry": "8", "fill": PRIMARY_DARK
        })
        # Cover bottom corners of title bar
        ET.SubElement(svg, "rect", {
            "x": str(x), "y": str(y + 20), "width": str(w), "height": "8",
            "fill": PRIMARY_DARK
        })
        ET.SubElement(svg, "text", {
            "x": str(x + w // 2), "y": str(y + 19),
            "text-anchor": "middle", "font-family": "Arial, sans-serif",
            "font-size": "11", "font-weight": "bold", "fill": TEXT_WHITE
        }).text = escape(title)


def add_code_block(svg, x, y, w, h, code_lines):
    """Add a code block with syntax highlighting appearance."""
    # Code background
    ET.SubElement(svg, "rect", {
        "x": str(x), "y": str(y), "width": str(w), "height": str(h),
        "rx": "4", "ry": "4", "fill": BG_CODE,
        "stroke": BORDER, "stroke-width": "1"
    })
    # Top bar with dots
    ET.SubElement(svg, "rect", {
        "x": str(x), "y": str(y), "width": str(w), "height": "20",
        "rx": "4", "ry": "4", "fill": "#161B22"
    })
    ET.SubElement(svg, "rect", {
        "x": str(x), "y": str(y + 16), "width": str(w), "height": "4",
        "fill": "#161B22"
    })
    # Window dots
    for i, color in enumerate(["#EF4444", "#F59E0B", "#22C55E"]):
        ET.SubElement(svg, "circle", {
            "cx": str(x + 14 + i * 16), "cy": str(y + 10),
            "r": "4", "fill": color
        })
    # Code lines
    line_y = y + 34
    for line in code_lines:
        ET.SubElement(svg, "text", {
            "x": str(x + 12), "y": str(line_y),
            "font-family": "Consolas, monospace", "font-size": "10",
            "fill": ACCENT_CYAN
        }).text = escape(line)
        line_y += 15


def add_bullet(svg, x, y, text, color=PRIMARY_LIGHT, font_size="12"):
    """Add a bullet point item."""
    ET.SubElement(svg, "circle", {
        "cx": str(x), "cy": str(y - 4), "r": "3", "fill": color
    })
    ET.SubElement(svg, "text", {
        "x": str(x + 12), "y": str(y),
        "font-family": "Arial, sans-serif", "font-size": font_size,
        "fill": TEXT_LIGHT
    }).text = escape(text)


def add_arrow(svg, x1, y1, x2, y2, color=PRIMARY_LIGHT):
    """Add an arrow line."""
    ET.SubElement(svg, "line", {
        "x1": str(x1), "y1": str(y1), "x2": str(x2), "y2": str(y2),
        "stroke": color, "stroke-width": "2", "marker-end": "url(#arrowhead)"
    })


def add_arrowhead_def(svg):
    """Add arrowhead marker definition."""
    defs = svg.find("{http://www.w3.org/2000/svg}defs")
    if defs is None:
        defs = ET.SubElement(svg, "defs")
    marker = ET.SubElement(defs, "marker", {
        "id": "arrowhead", "markerWidth": "10", "markerHeight": "7",
        "refX": "10", "refY": "3.5", "orient": "auto"
    })
    ET.SubElement(marker, "polygon", {
        "points": "0 0, 10 3.5, 0 7", "fill": PRIMARY_LIGHT
    })


def add_box_with_label(svg, x, y, w, h, label, color=PRIMARY, text_color=TEXT_WHITE, font_size="11"):
    """Add a box with centered label text."""
    ET.SubElement(svg, "rect", {
        "x": str(x), "y": str(y), "width": str(w), "height": str(h),
        "rx": "5", "ry": "5", "fill": color,
        "stroke": color, "stroke-width": "1"
    })
    ET.SubElement(svg, "text", {
        "x": str(x + w // 2), "y": str(y + h // 2 + 4),
        "text-anchor": "middle", "font-family": "Arial, sans-serif",
        "font-size": font_size, "font-weight": "bold", "fill": text_color
    }).text = escape(label)


# ═══════════════════════════════════════════════════════════════
#  LESSON 1 — Что такое робот
# ═══════════════════════════════════════════════════════════════
def lesson_1():
    svg = svg_root()
    add_bg(svg)
    add_arrowhead_def(svg)
    add_title(svg, "Что такое робот?", "Урок 1 — Введение в робототехнику")

    # ── Definition card ──
    add_card(svg, 20, 90, 360, 65)
    ET.SubElement(svg, "text", {
        "x": "30", "y": "112", "font-family": "Arial, sans-serif",
        "font-size": "11", "font-weight": "bold", "fill": HIGHLIGHT
    }).text = "Определение:"
    ET.SubElement(svg, "text", {
        "x": "30", "y": "128", "font-family": "Arial, sans-serif",
        "font-size": "10", "fill": TEXT_LIGHT
    }).text = escape("Робот — автоматическое устройство, заменяющее")
    ET.SubElement(svg, "text", {
        "x": "30", "y": "142", "font-family": "Arial, sans-serif",
        "font-size": "10", "fill": TEXT_LIGHT
    }).text = escape("человека при выполнении механических и интеллектуальных задач.")

    # ── Three laws of robotics ──
    add_card(svg, 400, 90, 380, 65, "Законы робототехники (Азимов)")
    laws = [
        "1. Робот не может причинить вред человеку",
        "2. Робот повинуется приказам человека",
        "3. Робот защищает себя, если это не противоречит 1 и 2"
    ]
    for i, law in enumerate(laws):
        ET.SubElement(svg, "text", {
            "x": "412", "y": str(128 + i * 14),
            "font-family": "Arial, sans-serif", "font-size": "9",
            "fill": TEXT_LIGHT
        }).text = escape(law)

    # ── Robot components diagram ──
    add_card(svg, 20, 170, 760, 200, "Основные компоненты робота")

    # Central controller
    add_box_with_label(svg, 330, 240, 140, 40, "Контроллер", PRIMARY)

    # Sensors (left)
    add_box_with_label(svg, 50, 235, 120, 50, "Датчики", ACCENT_TEAL)
    # Sensor sub-items
    for i, s in enumerate(["Ультразвук.", "Инфракрасный", "Световой"]):
        ET.SubElement(svg, "text", {
            "x": "60", "y": str(295 + i * 13),
            "font-family": "Arial, sans-serif", "font-size": "8",
            "fill": TEXT_MUTED
        }).text = escape(s)

    # Actuators (right)
    add_box_with_label(svg, 630, 235, 120, 50, "Исполн. мех.", HIGHLIGHT)
    # Actuator sub-items
    for i, s in enumerate(["Двигатели", "Сервоприводы", "Шаговые моторы"]):
        ET.SubElement(svg, "text", {
            "x": "640", "y": str(295 + i * 13),
            "font-family": "Arial, sans-serif", "font-size": "8",
            "fill": TEXT_MUTED
        }).text = escape(s)

    # Power (bottom)
    add_box_with_label(svg, 330, 300, 140, 30, "Питание", DANGER)

    # Arrows
    add_arrow(svg, 170, 260, 325, 258)
    add_arrow(svg, 475, 258, 625, 258)
    add_arrow(svg, 400, 283, 400, 296)

    # Labels on arrows
    ET.SubElement(svg, "text", {
        "x": "240", "y": "252", "font-family": "Arial, sans-serif",
        "font-size": "8", "fill": ACCENT_CYAN, "text-anchor": "middle"
    }).text = "Входные данные"
    ET.SubElement(svg, "text", {
        "x": "555", "y": "252", "font-family": "Arial, sans-serif",
        "font-size": "8", "fill": ACCENT_CYAN, "text-anchor": "middle"
    }).text = "Управление"

    # ── History timeline ──
    add_card(svg, 20, 385, 760, 185, "История развития робототехники")

    timeline_items = [
        ("1920", "К. Чапек\nввёл слово\n\"робот\""),
        ("1961", "Первый\nпромышленный\nробот Unimate"),
        ("1969", "Стэнфордская\nрука — первый\nэлектромех. робот"),
        ("1997", "Deep Blue\nпобеждает\nчемпиона мира"),
        ("2000", "ASIMO —\nгуманоидный\nробот Honda"),
        ("2020+", "AI и\nколлаборативные\nроботы"),
    ]

    # Timeline line
    ET.SubElement(svg, "line", {
        "x1": "60", "y1": "470", "x2": "740", "y2": "470",
        "stroke": PRIMARY_LIGHT, "stroke-width": "2"
    })

    for i, (year, desc) in enumerate(timeline_items):
        cx = 60 + i * 130
        # Dot
        ET.SubElement(svg, "circle", {
            "cx": str(cx), "cy": "470", "r": "6",
            "fill": PRIMARY_LIGHT, "stroke": BG_DARK, "stroke-width": "2"
        })
        # Year
        ET.SubElement(svg, "text", {
            "x": str(cx), "y": "490",
            "text-anchor": "middle", "font-family": "Arial, sans-serif",
            "font-size": "10", "font-weight": "bold", "fill": HIGHLIGHT
        }).text = year
        # Description lines
        lines = desc.split("\n")
        for j, line in enumerate(lines):
            ET.SubElement(svg, "text", {
                "x": str(cx), "y": str(505 + j * 12),
                "text-anchor": "middle", "font-family": "Arial, sans-serif",
                "font-size": "8", "fill": TEXT_MUTED
            }).text = escape(line)

    return svg


# ═══════════════════════════════════════════════════════════════
#  LESSON 2 — Виды роботов
# ═══════════════════════════════════════════════════════════════
def lesson_2():
    svg = svg_root()
    add_bg(svg)
    add_arrowhead_def(svg)
    add_title(svg, "Виды роботов", "Урок 2 — Классификация и типы роботов")

    types = [
        ("Промышленные", PRIMARY, [
            "Сварочные роботы",
            "Роботы-сборщики",
            "Покрасочные роботы",
            "Высокая точность",
            "Работают 24/7"
        ], "🏭"),
        ("Сервисные", ACCENT_TEAL, [
            "Роботы-пылесосы",
            "Медицинские роботы",
            "Роботы-доставщики",
            "Помощники в быту",
            "Социальные роботы"
        ], "🏥"),
        ("Мобильные", HIGHLIGHT, [
            "Колёсные платформы",
            "Гусеничные роботы",
            "Шагающие роботы",
            "Ровер-исследователи",
            "Автопилоты"
        ], "🚗"),
        ("Гуманоидные", HIGHLIGHT2, [
            "Двуногие роботы",
            "Имитация человека",
            "ASIMO, Atlas",
            "Сложная механика",
            "Много степеней свободы"
        ], "🤖"),
        ("Дроны", SUCCESS, [
            "Квадрокоптеры",
            "FPV-дроны",
            "Сельхоз. дроны",
            "Дроны-разведчики",
            "Доставка по воздуху"
        ], "✈"),
    ]

    card_w = 148
    card_h = 240
    start_x = 15
    gap = 5

    for i, (name, color, items, emoji) in enumerate(types):
        x = start_x + i * (card_w + gap)
        y = 90

        # Card background
        ET.SubElement(svg, "rect", {
            "x": str(x), "y": str(y), "width": str(card_w), "height": str(card_h),
            "rx": "8", "ry": "8", "fill": BG_CARD,
            "stroke": color, "stroke-width": "2"
        })

        # Color top bar
        ET.SubElement(svg, "rect", {
            "x": str(x), "y": str(y), "width": str(card_w), "height": "40",
            "rx": "8", "ry": "8", "fill": color
        })
        ET.SubElement(svg, "rect", {
            "x": str(x), "y": str(y + 32), "width": str(card_w), "height": "8",
            "fill": color
        })

        # Type name
        ET.SubElement(svg, "text", {
            "x": str(x + card_w // 2), "y": str(y + 26),
            "text-anchor": "middle", "font-family": "Arial, sans-serif",
            "font-size": "12", "font-weight": "bold", "fill": TEXT_WHITE
        }).text = escape(name)

        # Icon circle
        ET.SubElement(svg, "circle", {
            "cx": str(x + card_w // 2), "cy": str(y + 65),
            "r": "18", "fill": color, "opacity": "0.3"
        })
        ET.SubElement(svg, "text", {
            "x": str(x + card_w // 2), "y": str(y + 71),
            "text-anchor": "middle", "font-size": "18"
        }).text = emoji

        # Items
        for j, item in enumerate(items):
            ET.SubElement(svg, "circle", {
                "cx": str(x + 12), "cy": str(y + 98 + j * 22),
                "r": "2.5", "fill": color
            })
            ET.SubElement(svg, "text", {
                "x": str(x + 20), "y": str(y + 102 + j * 22),
                "font-family": "Arial, sans-serif", "font-size": "9",
                "fill": TEXT_LIGHT
            }).text = escape(item)

    # ── Classification criteria ──
    add_card(svg, 20, 345, 760, 230, "Критерии классификации роботов")

    criteria = [
        ("По назначению", ["Промышленные", "Бытовые", "Военные", "Медицинские"], PRIMARY),
        ("По среде работы", ["Наземные", "Воздушные", "Подводные", "Космические"], ACCENT_TEAL),
        ("По управлению", ["Автономные", "Полуавтономные", "Дистанционные", "Программируемые"], HIGHLIGHT),
        ("По подвижности", ["Стационарные", "Мобильные", "Гибридные", "Микро-роботы"], HIGHLIGHT2),
    ]

    for i, (title, items, color) in enumerate(criteria):
        cx = 40 + i * 190
        cy = 390

        # Column header
        ET.SubElement(svg, "rect", {
            "x": str(cx), "y": str(cy), "width": "170", "height": "24",
            "rx": "4", "fill": color, "opacity": "0.3"
        })
        ET.SubElement(svg, "text", {
            "x": str(cx + 85), "y": str(cy + 16),
            "text-anchor": "middle", "font-family": "Arial, sans-serif",
            "font-size": "10", "font-weight": "bold", "fill": color
        }).text = escape(title)

        for j, item in enumerate(items):
            ET.SubElement(svg, "text", {
                "x": str(cx + 10), "y": str(cy + 42 + j * 18),
                "font-family": "Arial, sans-serif", "font-size": "10",
                "fill": TEXT_LIGHT
            }).text = escape(f"• {item}")

    return svg


# ═══════════════════════════════════════════════════════════════
#  LESSON 3 — Знакомство с Arduino
# ═══════════════════════════════════════════════════════════════
def lesson_3():
    svg = svg_root()
    add_bg(svg)
    add_arrowhead_def(svg)
    add_title(svg, "Знакомство с Arduino", "Урок 3 — Платформа для создания электроники")

    # ── Arduino board diagram ──
    add_card(svg, 20, 90, 400, 270, "Архитектура платы Arduino Uno")

    # Board outline
    ET.SubElement(svg, "rect", {
        "x": "40", "y": "135", "width": "280", "height": "190",
        "rx": "6", "fill": "#0A3D62", "stroke": PRIMARY_LIGHT, "stroke-width": "2"
    })

    # USB connector
    ET.SubElement(svg, "rect", {
        "x": "40", "y": "190", "width": "25", "height": "45",
        "rx": "2", "fill": "#94A3B8", "stroke": TEXT_WHITE, "stroke-width": "1"
    })
    ET.SubElement(svg, "text", {
        "x": "72", "y": "216", "font-family": "Arial, sans-serif",
        "font-size": "7", "fill": TEXT_MUTED
    }).text = "USB"

    # MCU chip
    ET.SubElement(svg, "rect", {
        "x": "140", "y": "185", "width": "60", "height": "55",
        "rx": "2", "fill": "#1E293B", "stroke": HIGHLIGHT2, "stroke-width": "1.5"
    })
    ET.SubElement(svg, "text", {
        "x": "170", "y": "210", "text-anchor": "middle",
        "font-family": "Consolas, monospace", "font-size": "7",
        "font-weight": "bold", "fill": HIGHLIGHT2
    }).text = "ATmega"
    ET.SubElement(svg, "text", {
        "x": "170", "y": "222", "text-anchor": "middle",
        "font-family": "Consolas, monospace", "font-size": "7",
        "fill": HIGHLIGHT2
    }).text = "328P"

    # Crystal
    ET.SubElement(svg, "rect", {
        "x": "220", "y": "200", "width": "20", "height": "10",
        "rx": "2", "fill": "#334155", "stroke": TEXT_MUTED, "stroke-width": "0.5"
    })
    ET.SubElement(svg, "text", {
        "x": "230", "y": "218", "text-anchor": "middle",
        "font-family": "Arial, sans-serif", "font-size": "6", "fill": TEXT_MUTED
    }).text = "16MHz"

    # Power LED
    ET.SubElement(svg, "circle", {
        "cx": "100", "cy": "160", "r": "4", "fill": SUCCESS
    })
    ET.SubElement(svg, "text", {
        "x": "108", "y": "163", "font-family": "Arial, sans-serif",
        "font-size": "6", "fill": TEXT_MUTED
    }).text = "PWR"

    # TX/RX LEDs
    ET.SubElement(svg, "circle", {"cx": "115", "cy": "160", "r": "4", "fill": HIGHLIGHT})
    ET.SubElement(svg, "text", {"x": "123", "y": "163", "font-family": "Arial, sans-serif", "font-size": "6", "fill": TEXT_MUTED}).text = "TX"
    ET.SubElement(svg, "circle", {"cx": "135", "cy": "160", "r": "4", "fill": PRIMARY_LIGHT})
    ET.SubElement(svg, "text", {"x": "143", "y": "163", "font-family": "Arial, sans-serif", "font-size": "6", "fill": TEXT_MUTED}).text = "RX"

    # Digital pins (top)
    for i in range(14):
        px = 48 + i * 19
        ET.SubElement(svg, "rect", {
            "x": str(px), "y": "130", "width": "14", "height": "8",
            "fill": "#0A3D62", "stroke": ACCENT_CYAN, "stroke-width": "0.8"
        })
        if i < 10:
            ET.SubElement(svg, "text", {
                "x": str(px + 7), "y": "127",
                "text-anchor": "middle", "font-family": "Consolas, monospace",
                "font-size": "6", "fill": ACCENT_CYAN
            }).text = str(i)

    # PWM pins markers
    for pin in [3, 5, 6, 9, 10, 11]:
        px = 48 + pin * 19
        ET.SubElement(svg, "text", {
            "x": str(px + 7), "y": "145",
            "text-anchor": "middle", "font-family": "Consolas, monospace",
            "font-size": "5", "fill": HIGHLIGHT
        }).text = "~"

    # Analog pins (bottom)
    for i in range(6):
        px = 48 + i * 19
        ET.SubElement(svg, "rect", {
            "x": str(px), "y": "320", "width": "14", "height": "8",
            "fill": "#0A3D62", "stroke": SUCCESS, "stroke-width": "0.8"
        })
        ET.SubElement(svg, "text", {
            "x": str(px + 7), "y": "338",
            "text-anchor": "middle", "font-family": "Consolas, monospace",
            "font-size": "6", "fill": SUCCESS
        }).text = f"A{i}"

    # Power pins (right)
    power_pins = ["5V", "3.3V", "GND", "GND", "Vin"]
    for i, pin in enumerate(power_pins):
        py = 155 + i * 18
        ET.SubElement(svg, "rect", {
            "x": "296", "y": str(py), "width": "20", "height": "8",
            "fill": "#0A3D62", "stroke": DANGER, "stroke-width": "0.8"
        })
        ET.SubElement(svg, "text", {
            "x": "320", "y": str(py + 7),
            "font-family": "Consolas, monospace", "font-size": "6", "fill": DANGER
        }).text = pin

    # Reset button
    ET.SubElement(svg, "circle", {
        "cx": "270", "cy": "150", "r": "8",
        "fill": "#334155", "stroke": TEXT_MUTED, "stroke-width": "1"
    })
    ET.SubElement(svg, "text", {
        "x": "270", "y": "153", "text-anchor": "middle",
        "font-family": "Arial, sans-serif", "font-size": "5", "fill": TEXT_MUTED
    }).text = "RST"

    # Pin legend
    ET.SubElement(svg, "circle", {"cx": "50", "y": "355", "r": "4", "fill": ACCENT_CYAN})
    ET.SubElement(svg, "text", {"x": "58", "y": "358", "font-family": "Arial, sans-serif", "font-size": "8", "fill": TEXT_MUTED}).text = "Цифровые"
    ET.SubElement(svg, "circle", {"cx": "120", "y": "355", "r": "4", "fill": SUCCESS})
    ET.SubElement(svg, "text", {"x": "128", "y": "358", "font-family": "Arial, sans-serif", "font-size": "8", "fill": TEXT_MUTED}).text = "Аналоговые"
    ET.SubElement(svg, "circle", {"cx": "200", "y": "355", "r": "4", "fill": DANGER})
    ET.SubElement(svg, "text", {"x": "208", "y": "358", "font-family": "Arial, sans-serif", "font-size": "8", "fill": TEXT_MUTED}).text = "Питание"
    ET.SubElement(svg, "text", {"x": "50", "y": "358", "font-family": "Arial, sans-serif", "font-size": "8", "fill": HIGHLIGHT}).text = ""
    ET.SubElement(svg, "text", {"x": "275", "y": "358", "font-family": "Arial, sans-serif", "font-size": "8", "fill": HIGHLIGHT}).text = "~ = PWM"

    # ── Arduino IDE ──
    add_card(svg, 440, 90, 340, 270, "Arduino IDE")

    # IDE mockup
    ET.SubElement(svg, "rect", {
        "x": "455", "y": "125", "width": "310", "height": "195",
        "rx": "4", "fill": BG_CODE, "stroke": BORDER, "stroke-width": "1"
    })

    # Toolbar
    ET.SubElement(svg, "rect", {
        "x": "455", "y": "125", "width": "310", "height": "22",
        "rx": "4", "fill": "#161B22"
    })
    ET.SubElement(svg, "rect", {"x": "455", "y": "143", "width": "310", "height": "4", "fill": "#161B22"})

    # Toolbar icons
    for i, label in enumerate(["Verify", "Upload", "New", "Open", "Save"]):
        bx = 462 + i * 28
        ET.SubElement(svg, "rect", {
            "x": str(bx), "y": "129", "width": "24", "height": "14",
            "rx": "2", "fill": PRIMARY, "opacity": "0.5"
        })
        ET.SubElement(svg, "text", {
            "x": str(bx + 12), "y": "140",
            "text-anchor": "middle", "font-family": "Arial, sans-serif",
            "font-size": "5", "fill": TEXT_WHITE
        }).text = label

    # Code in IDE
    code = [
        ("void", " setup() {", HIGHLIGHT2, TEXT_LIGHT),
        ("", "  pinMode(13, OUTPUT);", "", ACCENT_CYAN),
        ("}", "", TEXT_LIGHT, ""),
        ("", "", "", ""),
        ("void", " loop() {", HIGHLIGHT2, TEXT_LIGHT),
        ("", "  digitalWrite(13, HIGH);", "", ACCENT_CYAN),
        ("", "  delay(1000);", "", ACCENT_CYAN),
        ("", "  digitalWrite(13, LOW);", "", ACCENT_CYAN),
        ("", "  delay(1000);", "", ACCENT_CYAN),
        ("}", "", TEXT_LIGHT, ""),
    ]
    line_y = 160
    for keyword, rest, kw_color, rest_color in code:
        if keyword:
            ET.SubElement(svg, "text", {
                "x": "465", "y": str(line_y),
                "font-family": "Consolas, monospace", "font-size": "10",
                "fill": kw_color
            }).text = keyword
            ET.SubElement(svg, "text", {
                "x": str(465 + len(keyword) * 7), "y": str(line_y),
                "font-family": "Consolas, monospace", "font-size": "10",
                "fill": rest_color
            }).text = rest
        elif rest:
            ET.SubElement(svg, "text", {
                "x": "465", "y": str(line_y),
                "font-family": "Consolas, monospace", "font-size": "10",
                "fill": rest_color
            }).text = rest
        line_y += 13

    # Status bar
    ET.SubElement(svg, "rect", {
        "x": "455", "y": "303", "width": "310", "height": "17",
        "fill": PRIMARY_DARK
    })
    ET.SubElement(svg, "text", {
        "x": "465", "y": "315",
        "font-family": "Arial, sans-serif", "font-size": "8",
        "fill": SUCCESS
    }).text = "✓ Compilation complete"

    # ── Key specs ──
    add_card(svg, 20, 375, 760, 200, "Характеристики Arduino Uno")

    specs = [
        ("Микроконтроллер", "ATmega328P", PRIMARY),
        ("Тактовая частота", "16 МГц", ACCENT_CYAN),
        ("Флеш-память", "32 КБ", HIGHLIGHT),
        ("SRAM", "2 КБ", ACCENT_TEAL),
        ("EEPROM", "1 КБ", HIGHLIGHT2),
        ("Цифровые пины", "14 (6 PWM)", PRIMARY_LIGHT),
        ("Аналоговые пины", "6", SUCCESS),
        ("Напряжение", "5В / 3.3В", DANGER),
    ]

    for i, (label, value, color) in enumerate(specs):
        row = i // 4
        col = i % 4
        x = 40 + col * 190
        y = 420 + row * 70

        # Spec box
        ET.SubElement(svg, "rect", {
            "x": str(x), "y": str(y), "width": "175", "height": "55",
            "rx": "6", "fill": BG_CODE, "stroke": color, "stroke-width": "1"
        })
        # Color accent bar
        ET.SubElement(svg, "rect", {
            "x": str(x), "y": str(y), "width": "4", "height": "55",
            "rx": "2", "fill": color
        })
        ET.SubElement(svg, "text", {
            "x": str(x + 14), "y": str(y + 22),
            "font-family": "Arial, sans-serif", "font-size": "9",
            "fill": TEXT_MUTED
        }).text = escape(label)
        ET.SubElement(svg, "text", {
            "x": str(x + 14), "y": str(y + 42),
            "font-family": "Consolas, monospace", "font-size": "14",
            "font-weight": "bold", "fill": color
        }).text = escape(value)

    return svg


# ═══════════════════════════════════════════════════════════════
#  LESSON 4 — Программирование Arduino
# ═══════════════════════════════════════════════════════════════
def lesson_4():
    svg = svg_root()
    add_bg(svg)
    add_arrowhead_def(svg)
    add_title(svg, "Программирование Arduino", "Урок 4 — Основы C++ для Arduino")

    # ── Program structure ──
    add_card(svg, 20, 90, 350, 240, "Структура программы")

    add_code_block(svg, 30, 125, 330, 195, [
        "// Подключение библиотек",
        "#include <Servo.h>",
        "",
        "// Объявление переменных",
        "int ledPin = 13;",
        "int sensorValue = 0;",
        "",
        "void setup() {",
        "  // Инициализация (выполняется 1 раз)",
        "  pinMode(ledPin, OUTPUT);",
        "  Serial.begin(9600);",
        "}",
        "",
        "void loop() {",
        "  // Основной цикл (повторяется)",
        "  sensorValue = analogRead(A0);",
        "  digitalWrite(ledPin, HIGH);",
        "  delay(500);",
        "  digitalWrite(ledPin, LOW);",
        "  delay(500);",
        "}",
    ])

    # ── Data types card ──
    add_card(svg, 390, 90, 390, 240, "Типы данных C++ для Arduino")

    types_data = [
        ("int", "Целое число", "-32768..32767", PRIMARY_LIGHT),
        ("float", "Дробное число", "3.14, -2.5", ACCENT_CYAN),
        ("bool", "Логический", "true / false", SUCCESS),
        ("char", "Символ", "'A', '0'", HIGHLIGHT),
        ("String", "Строка", "\"Hello\"", HIGHLIGHT2),
        ("byte", "0..255", "8 бит", ACCENT_TEAL),
        ("long", "Длинное целое", "-2млрд..2млрд", PRIMARY),
        ("unsigned int", "Беззнаковое", "0..65535", DANGER),
    ]

    # Header
    for j, header in enumerate(["Тип", "Описание", "Пример"]):
        hx = 400 + j * 120
        ET.SubElement(svg, "text", {
            "x": str(hx), "y": "130",
            "font-family": "Arial, sans-serif", "font-size": "9",
            "font-weight": "bold", "fill": HIGHLIGHT
        }).text = header

    for i, (dtype, desc, example, color) in enumerate(types_data):
        ry = 148 + i * 24
        # Row background
        if i % 2 == 0:
            ET.SubElement(svg, "rect", {
                "x": "395", "y": str(ry - 12), "width": "375", "height": "22",
                "fill": BG_CODE, "opacity": "0.5"
            })
        ET.SubElement(svg, "text", {
            "x": "400", "y": str(ry),
            "font-family": "Consolas, monospace", "font-size": "9",
            "fill": color
        }).text = dtype
        ET.SubElement(svg, "text", {
            "x": "520", "y": str(ry),
            "font-family": "Arial, sans-serif", "font-size": "9",
            "fill": TEXT_LIGHT
        }).text = escape(desc)
        ET.SubElement(svg, "text", {
            "x": "640", "y": str(ry),
            "font-family": "Consolas, monospace", "font-size": "8",
            "fill": TEXT_MUTED
        }).text = escape(example)

    # ── Digital I/O ──
    add_card(svg, 20, 345, 260, 230, "Цифровой ввод/вывод")

    add_code_block(svg, 30, 380, 240, 130, [
        "// Настройка пина",
        "pinMode(13, OUTPUT);",
        "pinMode(2, INPUT);",
        "",
        "// Запись на пин",
        "digitalWrite(13, HIGH);",
        "digitalWrite(13, LOW);",
        "",
        "// Чтение с пина",
        "int val = digitalRead(2);",
    ])

    # Digital signal diagram
    ET.SubElement(svg, "rect", {
        "x": "30", "y": "520", "width": "240", "height": "40",
        "fill": BG_CODE, "stroke": BORDER, "stroke-width": "0.5"
    })
    # Square wave
    points = "35,550 35,530 70,530 70,550 105,550 105,530 140,530 140,550 175,550 175,530 210,530 210,550 245,550 245,530 260,530"
    ET.SubElement(svg, "polyline", {
        "points": points, "fill": "none",
        "stroke": ACCENT_CYAN, "stroke-width": "1.5"
    })
    ET.SubElement(svg, "text", {
        "x": "150", "y": "545",
        "text-anchor": "middle", "font-family": "Arial, sans-serif",
        "font-size": "7", "fill": TEXT_MUTED
    }).text = "Цифровой сигнал (HIGH/LOW)"

    # ── Analog I/O ──
    add_card(svg, 300, 345, 260, 230, "Аналоговый ввод/вывод")

    add_code_block(svg, 310, 380, 240, 130, [
        "// Аналоговое чтение (0-1023)",
        "int val = analogRead(A0);",
        "",
        "// Аналоговая запись (0-255)",
        "analogWrite(9, 128);",
        "",
        "// ШИМ (PWM) сигнал",
        "// Частота ~490 Гц",
        "// Разрешение: 8 бит",
    ])

    # PWM signal diagram
    ET.SubElement(svg, "rect", {
        "x": "310", "y": "520", "width": "240", "height": "40",
        "fill": BG_CODE, "stroke": BORDER, "stroke-width": "0.5"
    })
    # PWM wave (50% duty cycle)
    pwm_points = "315,550 315,530 345,530 345,550 355,550 355,530 385,530 385,550 395,550 395,530 425,530 425,550 435,550 435,530 465,530 465,550 475,550 475,530 505,530 505,550 515,550 515,530 545,530 545,550"
    ET.SubElement(svg, "polyline", {
        "points": pwm_points, "fill": "none",
        "stroke": HIGHLIGHT, "stroke-width": "1.5"
    })
    ET.SubElement(svg, "text", {
        "x": "430", "y": "545",
        "text-anchor": "middle", "font-family": "Arial, sans-serif",
        "font-size": "7", "fill": TEXT_MUTED
    }).text = "ШИМ сигнал (PWM)"

    # ── Control structures ──
    add_card(svg, 580, 345, 200, 230, "Циклы и условия")

    add_code_block(svg, 590, 380, 180, 185, [
        "// Условие if/else",
        "if (val > 500) {",
        "  digitalWrite(13, HIGH);",
        "} else {",
        "  digitalWrite(13, LOW);",
        "}",
        "",
        "// Цикл for",
        "for (int i=0; i<10; i++){",
        "  Serial.println(i);",
        "}",
        "",
        "// Цикл while",
        "while (val < 1000){",
        "  val = analogRead(A0);",
        "}",
    ])

    return svg


# ═══════════════════════════════════════════════════════════════
#  LESSON 5 — Датчики для роботов
# ═══════════════════════════════════════════════════════════════
def lesson_5():
    svg = svg_root()
    add_bg(svg)
    add_arrowhead_def(svg)
    add_title(svg, "Датчики для роботов", "Урок 5 — Сенсорные системы робототехники")

    sensors = [
        {
            "name": "Ультразвуковой",
            "icon": "📡",
            "color": PRIMARY_LIGHT,
            "desc": "Измеряет расстояние\nс помощью звука",
            "range": "2 см — 400 см",
            "pin": "Trig / Echo",
            "code": "duration = pulseIn(echo, HIGH);\ndistance = duration * 0.034/2;",
        },
        {
            "name": "Инфракрасный",
            "icon": "🔴",
            "color": DANGER,
            "desc": "Детектирует препятствия\nпо отражению ИК-луча",
            "range": "0 — 30 см",
            "pin": "OUT (цифровой)",
            "code": "int obstacle = digitalRead(irPin);\n// 0 = препятствие",
        },
        {
            "name": "Световой",
            "icon": "☀",
            "color": HIGHLIGHT,
            "desc": "Измеряет освещённость\n(фоторезистор)",
            "range": "0 — 1023 (АЦП)",
            "pin": "A0 (аналоговый)",
            "code": "int light = analogRead(A0);\nif (light < 300) {",
        },
        {
            "name": "Температурный",
            "icon": "🌡",
            "color": ACCENT_TEAL,
            "desc": "Измеряет температуру\n(DHT11 / DHT22)",
            "range": "-40°C — +80°C",
            "pin": "Data (цифровой)",
            "code": "float t = dht.readTemperature();\nfloat h = dht.readHumidity();",
        },
        {
            "name": "Гироскоп",
            "icon": "🔄",
            "color": HIGHLIGHT2,
            "desc": "Измеряет угловую скорость\nи ориентацию (MPU6050)",
            "range": "±250°/сек",
            "pin": "SDA / SCL (I2C)",
            "code": "Wire.beginTransmission(0x68);\nWire.write(0x3B);",
        },
    ]

    # Sensor cards - top row of 3
    for i, s in enumerate(sensors[:3]):
        x = 20 + i * 260
        y = 90

        add_card(svg, x, y, 245, 185, s["name"])

        # Icon and color badge
        ET.SubElement(svg, "rect", {
            "x": str(x + 5), "y": str(y + 30), "width": "30", "height": "20",
            "rx": "4", "fill": s["color"], "opacity": "0.3"
        })
        ET.SubElement(svg, "text", {
            "x": str(x + 20), "y": str(y + 45),
            "text-anchor": "middle", "font-size": "14"
        }).text = s["icon"]

        # Description
        desc_lines = s["desc"].split("\n")
        for j, line in enumerate(desc_lines):
            ET.SubElement(svg, "text", {
                "x": str(x + 40), "y": str(y + 44 + j * 12),
                "font-family": "Arial, sans-serif", "font-size": "9",
                "fill": TEXT_LIGHT
            }).text = escape(line)

        # Range
        ET.SubElement(svg, "text", {
            "x": str(x + 10), "y": str(y + 78),
            "font-family": "Arial, sans-serif", "font-size": "8",
            "fill": TEXT_MUTED
        }).text = f"Диапазон: {s['range']}"

        # Pin
        ET.SubElement(svg, "text", {
            "x": str(x + 10), "y": str(y + 92),
            "font-family": "Consolas, monospace", "font-size": "8",
            "fill": s["color"]
        }).text = f"Пин: {s['pin']}"

        # Code snippet
        add_code_block(svg, x + 5, y + 100, 235, 75, s["code"].split("\n"))

    # Bottom row of 2
    for i, s in enumerate(sensors[3:]):
        x = 20 + i * 380
        y = 290

        add_card(svg, x, y, 370, 160, s["name"])

        # Icon
        ET.SubElement(svg, "rect", {
            "x": str(x + 5), "y": str(y + 30), "width": "30", "height": "20",
            "rx": "4", "fill": s["color"], "opacity": "0.3"
        })
        ET.SubElement(svg, "text", {
            "x": str(x + 20), "y": str(y + 45),
            "text-anchor": "middle", "font-size": "14"
        }).text = s["icon"]

        desc_lines = s["desc"].split("\n")
        for j, line in enumerate(desc_lines):
            ET.SubElement(svg, "text", {
                "x": str(x + 40), "y": str(y + 44 + j * 12),
                "font-family": "Arial, sans-serif", "font-size": "9",
                "fill": TEXT_LIGHT
            }).text = escape(line)

        ET.SubElement(svg, "text", {
            "x": str(x + 10), "y": str(y + 78),
            "font-family": "Arial, sans-serif", "font-size": "8",
            "fill": TEXT_MUTED
        }).text = f"Диапазон: {s['range']}"

        ET.SubElement(svg, "text", {
            "x": str(x + 10), "y": str(y + 92),
            "font-family": "Consolas, monospace", "font-size": "8",
            "fill": s["color"]
        }).text = f"Пин: {s['pin']}"

        add_code_block(svg, x + 5, y + 100, 360, 50, s["code"].split("\n"))

    # ── Sensor selection guide ──
    add_card(svg, 400, 290, 380, 160, "Как выбрать датчик?")

    steps = [
        ("1. Определите задачу", "Что нужно измерить?", PRIMARY_LIGHT),
        ("2. Выберите тип датчика", "Ультразвук, ИК, свет...", ACCENT_CYAN),
        ("3. Проверьте совместимость", "Напряжение, интерфейс", HIGHLIGHT),
        ("4. Подключите и протестируйте", "Пины, библиотеки, код", SUCCESS),
    ]

    for i, (step, detail, color) in enumerate(steps):
        sy = 330 + i * 28
        ET.SubElement(svg, "rect", {
            "x": "410", "y": str(sy), "width": "360", "height": "24",
            "rx": "4", "fill": BG_CODE
        })
        ET.SubElement(svg, "rect", {
            "x": "410", "y": str(sy), "width": "3", "height": "24",
            "fill": color
        })
        ET.SubElement(svg, "text", {
            "x": "420", "y": str(sy + 16),
            "font-family": "Arial, sans-serif", "font-size": "9",
            "font-weight": "bold", "fill": color
        }).text = escape(step)
        ET.SubElement(svg, "text", {
            "x": "600", "y": str(sy + 16),
            "font-family": "Arial, sans-serif", "font-size": "8",
            "fill": TEXT_MUTED
        }).text = escape(detail)

    return svg


# ═══════════════════════════════════════════════════════════════
#  LESSON 6 — Моторы и драйверы
# ═══════════════════════════════════════════════════════════════
def lesson_6():
    svg = svg_root()
    add_bg(svg)
    add_arrowhead_def(svg)
    add_title(svg, "Моторы и драйверы", "Урок 6 — Приводные системы роботов")

    # ── Motor types comparison ──
    motors = [
        {
            "name": "DC Мотор",
            "color": PRIMARY_LIGHT,
            "desc": ["Постоянного тока", "Простое управление", "Высокие обороты"],
            "spec": "3-12В, до 10000 об/мин",
            "code": ["// Направление вращения", "digitalWrite(in1, HIGH);", "digitalWrite(in2, LOW);", "// Скорость (PWM)", "analogWrite(enA, 200);"],
        },
        {
            "name": "Сервопривод",
            "color": HIGHLIGHT,
            "desc": ["Точный угол поворота", "0-180° (обычно)", "Встроенный контроллер"],
            "spec": "4.8-6В, крутящий момент 1.8 кг·см",
            "code": ["#include <Servo.h>", "Servo myservo;", "myservo.attach(9);", "myservo.write(90); // угол", "delay(1000);"],
        },
        {
            "name": "Шаговый мотор",
            "color": HIGHLIGHT2,
            "desc": ["Пошаговое вращение", "Высокая точность", "Удержание позиции"],
            "spec": "5-12В, 1.8° на шаг",
            "code": ["#include <Stepper.h>", "Stepper s(2048,8,10,9,11);", "s.setSpeed(10);", "s.step(512);", "// 512 шагов = 90°"],
        },
    ]

    for i, m in enumerate(motors):
        x = 20 + i * 260
        y = 90
        add_card(svg, x, y, 245, 260, m["name"])

        # Description items
        for j, item in enumerate(m["desc"]):
            ET.SubElement(svg, "text", {
                "x": str(x + 10), "y": str(y + 42 + j * 14),
                "font-family": "Arial, sans-serif", "font-size": "9",
                "fill": TEXT_LIGHT
            }).text = f"• {escape(item)}"

        # Spec
        ET.SubElement(svg, "text", {
            "x": str(x + 10), "y": str(y + 88),
            "font-family": "Consolas, monospace", "font-size": "8",
            "fill": m["color"]
        }).text = escape(m["spec"])

        # Code
        add_code_block(svg, x + 5, y + 98, 235, 150, m["code"])

    # ── H-Bridge diagram ──
    add_card(svg, 20, 365, 380, 210, "H-мост (L298N)")

    # H-Bridge schematic
    # Switches
    sw_positions = [
        (80, 405, "S1", PRIMARY_LIGHT),
        (260, 405, "S2", PRIMARY_LIGHT),
        (80, 510, "S3", ACCENT_CYAN),
        (260, 510, "S4", ACCENT_CYAN),
    ]
    for sx, sy, label, color in sw_positions:
        ET.SubElement(svg, "rect", {
            "x": str(sx), "y": str(sy), "width": "40", "height": "20",
            "rx": "3", "fill": BG_CODE, "stroke": color, "stroke-width": "1.5"
        })
        ET.SubElement(svg, "text", {
            "x": str(sx + 20), "y": str(sy + 14),
            "text-anchor": "middle", "font-family": "Consolas, monospace",
            "font-size": "9", "fill": color
        }).text = label

    # Motor in center
    ET.SubElement(svg, "circle", {
        "cx": "190", "cy": "467", "r": "22",
        "fill": "none", "stroke": HIGHLIGHT, "stroke-width": "2"
    })
    ET.SubElement(svg, "text", {
        "x": "190", "y": "462", "text-anchor": "middle",
        "font-family": "Arial, sans-serif", "font-size": "8",
        "fill": HIGHLIGHT
    }).text = "M"
    ET.SubElement(svg, "text", {
        "x": "190", "y": "474", "text-anchor": "middle",
        "font-family": "Arial, sans-serif", "font-size": "7",
        "fill": TEXT_MUTED
    }).text = "Motor"

    # VCC and GND
    ET.SubElement(svg, "text", {
        "x": "50", "y": "398", "font-family": "Consolas, monospace",
        "font-size": "9", "fill": DANGER
    }).text = "VCC +"
    ET.SubElement(svg, "text", {
        "x": "50", "y": "535", "font-family": "Consolas, monospace",
        "font-size": "9", "fill": PRIMARY_LIGHT
    }).text = "GND −"

    # Connecting lines
    ET.SubElement(svg, "line", {"x1": "100", "y1": "415", "x2": "168", "y2": "445", "stroke": BORDER, "stroke-width": "1.5"})
    ET.SubElement(svg, "line", {"x1": "280", "y1": "415", "x2": "212", "y2": "445", "stroke": BORDER, "stroke-width": "1.5"})
    ET.SubElement(svg, "line", {"x1": "100", "y1": "510", "x2": "168", "y2": "489", "stroke": BORDER, "stroke-width": "1.5"})
    ET.SubElement(svg, "line", {"x1": "280", "y1": "510", "x2": "212", "y2": "489", "stroke": BORDER, "stroke-width": "1.5"})

    # Direction table
    ET.SubElement(svg, "text", {
        "x": "340", "y": "400", "font-family": "Arial, sans-serif",
        "font-size": "8", "fill": TEXT_MUTED
    }).text = "S1+S4 → вперёд"
    ET.SubElement(svg, "text", {
        "x": "340", "y": "415", "font-family": "Arial, sans-serif",
        "font-size": "8", "fill": TEXT_MUTED
    }).text = "S2+S3 → назад"
    ET.SubElement(svg, "text", {
        "x": "340", "y": "430", "font-family": "Arial, sans-serif",
        "font-size": "8", "fill": DANGER
    }).text = "S1+S2 → КЗ! ✗"
    ET.SubElement(svg, "text", {
        "x": "340", "y": "445", "font-family": "Arial, sans-serif",
        "font-size": "8", "fill": DANGER
    }).text = "S3+S4 → КЗ! ✗"

    # ── PWM explanation ──
    add_card(svg, 420, 365, 360, 210, "ШИМ (PWM) — Управление скоростью")

    # PWM diagrams at different duty cycles
    duties = [
        ("25%", 75, 25),
        ("50%", 150, 50),
        ("75%", 225, 75),
    ]

    for i, (label, high_val, pct) in enumerate(duties):
        py = 410 + i * 55
        # Label
        ET.SubElement(svg, "text", {
            "x": "435", "y": str(py),
            "font-family": "Consolas, monospace", "font-size": "10",
            "fill": HIGHLIGHT
        }).text = label

        # Wave area
        ET.SubElement(svg, "rect", {
            "x": "480", "y": str(py - 12), "width": "280", "height": "30",
            "fill": BG_CODE, "rx": "3"
        })

        # Draw PWM wave
        period = 35
        for j in range(7):
            bx = 485 + j * period
            high_w = int(period * pct / 100)
            # High part
            ET.SubElement(svg, "rect", {
                "x": str(bx), "y": str(py - 10),
                "width": str(high_w), "height": "12",
                "fill": ACCENT_CYAN, "opacity": "0.6"
            })
            # Line
            ET.SubElement(svg, "line", {
                "x1": str(bx), "y1": str(py - 10),
                "x2": str(bx + high_w), "y2": str(py - 10),
                "stroke": ACCENT_CYAN, "stroke-width": "1.5"
            })
            ET.SubElement(svg, "line", {
                "x1": str(bx + high_w), "y1": str(py - 10),
                "x2": str(bx + high_w), "y2": str(py + 2),
                "stroke": ACCENT_CYAN, "stroke-width": "1"
            })
            ET.SubElement(svg, "line", {
                "x1": str(bx + high_w), "y1": str(py + 2),
                "x2": str(bx + period), "y2": str(py + 2),
                "stroke": ACCENT_CYAN, "stroke-width": "1.5"
            })

        # analogWrite value
        ET.SubElement(svg, "text", {
            "x": "770", "y": str(py),
            "font-family": "Consolas, monospace", "font-size": "8",
            "fill": TEXT_MUTED
        }).text = f"= {high_val}/255"

    # PWM formula
    ET.SubElement(svg, "text", {
        "x": "435", "y": "560",
        "font-family": "Arial, sans-serif", "font-size": "9",
        "fill": TEXT_LIGHT
    }).text = escape("Скорость = (analogWrite / 255) × 100%")

    return svg


# ═══════════════════════════════════════════════════════════════
#  LESSON 7 — Процесс создания робота
# ═══════════════════════════════════════════════════════════════
def lesson_7():
    svg = svg_root()
    add_bg(svg)
    add_arrowhead_def(svg)
    add_title(svg, "Процесс создания робота", "Урок 7 — От идеи до работающего робота")

    # ── Main process flow ──
    steps = [
        ("1", "Идея и\nпроектирование", PRIMARY_LIGHT, "Определить задачу\nНарисовать схему\nВыбрать компоненты"),
        ("2", "Сборка\nмеханики", ACCENT_TEAL, "Рама и шасси\nКолёса/гусеницы\nКрепёж моторов"),
        ("3", "Электроника\nи подключение", HIGHLIGHT, "Плата контроллера\nДатчики и моторы\nПровода и питание"),
        ("4", "Программи-\nрование", HIGHLIGHT2, "Алгоритм движения\nОбработка датчиков\nОтладка кода"),
        ("5", "Тестирование\nи доработка", SUCCESS, "Проверка функций\nИсправление ошибок\nОптимизация"),
    ]

    # Flow arrows
    for i in range(4):
        ax1 = 105 + i * 155
        ax2 = ax1 + 75
        ET.SubElement(svg, "line", {
            "x1": str(ax1), "y1": "130", "x2": str(ax2), "y2": "130",
            "stroke": PRIMARY_LIGHT, "stroke-width": "2",
            "marker-end": "url(#arrowhead)", "opacity": "0.5"
        })

    for i, (num, name, color, details) in enumerate(steps):
        x = 20 + i * 155
        y = 92

        # Step circle
        ET.SubElement(svg, "circle", {
            "cx": str(x + 55), "cy": str(y + 38),
            "r": "28", "fill": BG_CARD, "stroke": color, "stroke-width": "2.5"
        })
        ET.SubElement(svg, "text", {
            "x": str(x + 55), "y": str(y + 44),
            "text-anchor": "middle", "font-family": "Arial, sans-serif",
            "font-size": "18", "font-weight": "bold", "fill": color
        }).text = num

        # Step name
        name_lines = name.split("\n")
        for j, line in enumerate(name_lines):
            ET.SubElement(svg, "text", {
                "x": str(x + 55), "y": str(y + 82 + j * 13),
                "text-anchor": "middle", "font-family": "Arial, sans-serif",
                "font-size": "9", "font-weight": "bold", "fill": color
            }).text = escape(line)

        # Details
        detail_lines = details.split("\n")
        for j, line in enumerate(detail_lines):
            ET.SubElement(svg, "text", {
                "x": str(x + 55), "y": str(y + 112 + j * 12),
                "text-anchor": "middle", "font-family": "Arial, sans-serif",
                "font-size": "8", "fill": TEXT_MUTED
            }).text = escape(line)

    # ── Detailed breakdown ──
    # Design phase
    add_card(svg, 20, 200, 380, 180, "Проектирование — ключевой этап")

    design_items = [
        ("Постановка задачи", "Какую проблему решает робот?", PRIMARY_LIGHT),
        ("Функциональные требования", "Что должен делать робот?", ACCENT_CYAN),
        ("Выбор компонентов", "Контроллер, датчики, моторы", HIGHLIGHT),
        ("Электрическая схема", "Схема подключений (Fritzing)", HIGHLIGHT2),
        ("3D модель / чертеж", "Корпус, крепления, размеры", ACCENT_TEAL),
    ]

    for i, (title, desc, color) in enumerate(design_items):
        iy = 240 + i * 26
        ET.SubElement(svg, "rect", {
            "x": "30", "y": str(iy - 10), "width": "360", "height": "22",
            "rx": "4", "fill": BG_CODE
        })
        ET.SubElement(svg, "rect", {
            "x": "30", "y": str(iy - 10), "width": "3", "height": "22",
            "fill": color
        })
        ET.SubElement(svg, "text", {
            "x": "40", "y": str(iy + 4),
            "font-family": "Arial, sans-serif", "font-size": "9",
            "font-weight": "bold", "fill": color
        }).text = escape(title)
        ET.SubElement(svg, "text", {
            "x": "220", "y": str(iy + 4),
            "font-family": "Arial, sans-serif", "font-size": "8",
            "fill": TEXT_MUTED
        }).text = escape(desc)

    # Programming phase
    add_card(svg, 420, 200, 360, 180, "Программирование — логика робота")

    add_code_block(svg, 430, 235, 340, 135, [
        "// Основной алгоритм робота",
        "void loop() {",
        "  // 1. Чтение датчиков",
        "  int dist = readUltrasonic();",
        "  int light = analogRead(A0);",
        "",
        "  // 2. Принятие решения",
        "  if (dist < 20) {",
        "    turnRight();  // Объезд",
        "  } else {",
        "    moveForward();",
        "  }",
        "",
        "  // 3. Действие",
        "  delay(50);",
        "}",
    ])

    # ── Tools & Resources ──
    add_card(svg, 20, 395, 760, 180, "Инструменты и ресурсы")

    tools = [
        ("Проектирование", ["Fritzing", "Tinkercad", "Autodesk Fusion", "SolidWorks"], PRIMARY_LIGHT),
        ("Программирование", ["Arduino IDE", "VS Code", "PlatformIO", "Scratch/Blockly"], ACCENT_CYAN),
        ("Прототипирование", ["3D-печать", "Лазерная резка", "Пайка", "Breadboard"], HIGHLIGHT),
        ("Тестирование", ["Мультиметр", "Осциллограф", "Serial Monitor", "Логика"], SUCCESS),
    ]

    for i, (category, items, color) in enumerate(tools):
        cx = 40 + i * 190
        # Category header
        ET.SubElement(svg, "rect", {
            "x": str(cx), "y": "435", "width": "170", "height": "24",
            "rx": "4", "fill": color, "opacity": "0.2"
        })
        ET.SubElement(svg, "text", {
            "x": str(cx + 85), "y": "451",
            "text-anchor": "middle", "font-family": "Arial, sans-serif",
            "font-size": "10", "font-weight": "bold", "fill": color
        }).text = escape(category)

        for j, item in enumerate(items):
            ET.SubElement(svg, "rect", {
                "x": str(cx + 5), "y": str(465 + j * 22),
                "width": "160", "height": "18",
                "rx": "3", "fill": BG_CODE
            })
            ET.SubElement(svg, "text", {
                "x": str(cx + 12), "y": str(478 + j * 22),
                "font-family": "Arial, sans-serif", "font-size": "9",
                "fill": TEXT_LIGHT
            }).text = escape(item)

    return svg


# ═══════════════════════════════════════════════════════════════
#  LESSON 8 — Современные технологии в робототехнике
# ═══════════════════════════════════════════════════════════════
def lesson_8():
    svg = svg_root()
    add_bg(svg)
    add_arrowhead_def(svg)
    add_title(svg, "Современные технологии в робототехнике", "Урок 8 — AI, компьютерное зрение, IoT, коботы")

    # ── AI in Robotics ──
    add_card(svg, 20, 90, 380, 230, "Искусственный интеллект (AI)")

    # Neural network diagram
    # Input layer
    for i in range(4):
        cy = 140 + i * 30
        ET.SubElement(svg, "circle", {
            "cx": "60", "cy": str(cy), "r": "10",
            "fill": PRIMARY, "stroke": PRIMARY_LIGHT, "stroke-width": "1"
        })

    # Hidden layer 1
    for i in range(5):
        cy = 125 + i * 28
        ET.SubElement(svg, "circle", {
            "cx": "140", "cy": str(cy), "r": "10",
            "fill": HIGHLIGHT2, "stroke": "#C4B5FD", "stroke-width": "1"
        })

    # Hidden layer 2
    for i in range(5):
        cy = 125 + i * 28
        ET.SubElement(svg, "circle", {
            "cx": "220", "cy": str(cy), "r": "10",
            "fill": ACCENT_TEAL, "stroke": "#5EEAD4", "stroke-width": "1"
        })

    # Output layer
    for i in range(3):
        cy = 155 + i * 35
        ET.SubElement(svg, "circle", {
            "cx": "300", "cy": str(cy), "r": "10",
            "fill": SUCCESS, "stroke": "#86EFAC", "stroke-width": "1"
        })

    # Connections (simplified)
    for ix, iy in [(60, 140), (60, 170), (60, 200), (60, 230)]:
        for hx, hy in [(140, 125), (140, 153), (140, 181), (140, 209), (140, 237)]:
            ET.SubElement(svg, "line", {
                "x1": str(ix + 10), "y1": str(iy),
                "x2": str(hx - 10), "y2": str(hy),
                "stroke": BORDER, "stroke-width": "0.5", "opacity": "0.5"
            })

    for hx, hy in [(140, 125), (140, 153), (140, 181), (140, 209), (140, 237)]:
        for h2x, h2y in [(220, 125), (220, 153), (220, 181), (220, 209), (220, 237)]:
            ET.SubElement(svg, "line", {
                "x1": str(hx + 10), "y1": str(hy),
                "x2": str(h2x - 10), "y2": str(h2y),
                "stroke": BORDER, "stroke-width": "0.3", "opacity": "0.3"
            })

    for h2x, h2y in [(220, 125), (220, 153), (220, 181), (220, 209), (220, 237)]:
        for ox, oy in [(300, 155), (300, 190), (300, 225)]:
            ET.SubElement(svg, "line", {
                "x1": str(h2x + 10), "y1": str(h2y),
                "x2": str(ox - 10), "y2": str(oy),
                "stroke": BORDER, "stroke-width": "0.5", "opacity": "0.4"
            })

    # Layer labels
    labels_nn = [("Вход", 60, PRIMARY_LIGHT), ("Скрытый 1", 140, "#C4B5FD"),
                 ("Скрытый 2", 220, "#5EEAD4"), ("Выход", 300, "#86EFAC")]
    for label, lx, color in labels_nn:
        ET.SubElement(svg, "text", {
            "x": str(lx), "y": "258",
            "text-anchor": "middle", "font-family": "Arial, sans-serif",
            "font-size": "8", "fill": color
        }).text = label

    # AI capabilities
    ai_caps = [
        "Обучение с подкреплением — робот учится на ошибках",
        "Распознавание образов — идентификация объектов",
        "Планирование пути — оптимальные маршруты",
        "Адаптивное поведение — меняется по ситуации",
    ]
    for i, cap in enumerate(ai_caps):
        ET.SubElement(svg, "text", {
            "x": "35", "y": str(278 + i * 14),
            "font-family": "Arial, sans-serif", "font-size": "8",
            "fill": TEXT_MUTED
        }).text = f"→ {escape(cap)}"

    # ── Computer Vision ──
    add_card(svg, 420, 90, 360, 230, "Компьютерное зрение")

    # Vision pipeline
    cv_steps = [
        ("Камера", "Захват\nизображения", PRIMARY_LIGHT),
        ("Предобработка", "Фильтрация\nмасштабирование", ACCENT_CYAN),
        ("Детекция", "Поиск\nобъектов", HIGHLIGHT),
        ("Распознавание", "Классифи-\nкация", SUCCESS),
    ]

    for i, (name, desc, color) in enumerate(cv_steps):
        cx = 440 + i * 85
        # Step box
        ET.SubElement(svg, "rect", {
            "x": str(cx), "y": "130", "width": "75", "height": "55",
            "rx": "6", "fill": color, "opacity": "0.2", "stroke": color, "stroke-width": "1"
        })
        ET.SubElement(svg, "text", {
            "x": str(cx + 37), "y": "150",
            "text-anchor": "middle", "font-family": "Arial, sans-serif",
            "font-size": "8", "font-weight": "bold", "fill": color
        }).text = escape(name)
        desc_lines = desc.split("\n")
        for j, line in enumerate(desc_lines):
            ET.SubElement(svg, "text", {
                "x": str(cx + 37), "y": str(165 + j * 10),
                "text-anchor": "middle", "font-family": "Arial, sans-serif",
                "font-size": "7", "fill": TEXT_MUTED
            }).text = escape(line)

        # Arrow between steps
        if i < 3:
            ET.SubElement(svg, "line", {
                "x1": str(cx + 78), "y1": "157",
                "x2": str(cx + 85), "y2": "157",
                "stroke": PRIMARY_LIGHT, "stroke-width": "1.5",
                "marker-end": "url(#arrowhead)"
            })

    # CV techniques
    cv_techs = [
        ("OpenCV", "Библиотека компьютерного зрения", PRIMARY_LIGHT),
        ("YOLO", "Детекция объектов в реальном времени", HIGHLIGHT),
        ("TensorFlow Lite", "ML на встраиваемых устройствах", SUCCESS),
        ("Обработка изображений", "Фильтры, контуры, гистограммы", ACCENT_CYAN),
    ]
    for i, (name, desc, color) in enumerate(cv_techs):
        ty = 200 + i * 22
        ET.SubElement(svg, "rect", {
            "x": "435", "y": str(ty - 9), "width": "340", "height": "18",
            "rx": "3", "fill": BG_CODE
        })
        ET.SubElement(svg, "rect", {
            "x": "435", "y": str(ty - 9), "width": "2", "height": "18",
            "fill": color
        })
        ET.SubElement(svg, "text", {
            "x": "445", "y": str(ty + 3),
            "font-family": "Consolas, monospace", "font-size": "9",
            "fill": color
        }).text = name
        ET.SubElement(svg, "text", {
            "x": "570", "y": str(ty + 3),
            "font-family": "Arial, sans-serif", "font-size": "8",
            "fill": TEXT_MUTED
        }).text = escape(desc)

    # ── IoT ──
    add_card(svg, 20, 335, 260, 240, "Интернет вещей (IoT)")

    # IoT diagram
    iot_nodes = [
        ("Робот", 90, 390, PRIMARY_LIGHT),
        ("Облако", 150, 440, ACCENT_CYAN),
        ("Телефон", 50, 440, HIGHLIGHT),
        ("Сервер", 150, 490, SUCCESS),
        ("Датчик", 90, 510, ACCENT_TEAL),
    ]

    # Draw connections
    for i, (n1, x1, y1, c1) in enumerate(iot_nodes):
        for j, (n2, x2, y2, c2) in enumerate(iot_nodes):
            if i < j:
                ET.SubElement(svg, "line", {
                    "x1": str(x1), "y1": str(y1),
                    "x2": str(x2), "y2": str(y2),
                    "stroke": BORDER, "stroke-width": "0.8", "opacity": "0.5"
                })

    for name, nx, ny, color in iot_nodes:
        ET.SubElement(svg, "circle", {
            "cx": str(nx), "cy": str(ny), "r": "16",
            "fill": color, "opacity": "0.3", "stroke": color, "stroke-width": "1.5"
        })
        ET.SubElement(svg, "text", {
            "x": str(nx), "y": str(ny + 4),
            "text-anchor": "middle", "font-family": "Arial, sans-serif",
            "font-size": "7", "font-weight": "bold", "fill": color
        }).text = escape(name)

    # IoT features
    iot_features = [
        "WiFi / Bluetooth подключение",
        "MQTT — протокол сообщений",
        "Удалённое управление",
        "Сбор данных в облаке",
    ]
    for i, feat in enumerate(iot_features):
        ET.SubElement(svg, "text", {
            "x": "35", "y": str(530 + i * 12),
            "font-family": "Arial, sans-serif", "font-size": "8",
            "fill": TEXT_MUTED
        }).text = f"• {escape(feat)}"

    # ── Collaborative robots ──
    add_card(svg, 300, 335, 250, 240, "Коботы (Cobots)")

    cobot_items = [
        ("Безопасность", "Работают рядом с людьми", SUCCESS),
        ("Обучение", "Программирование\nпоказом движений", PRIMARY_LIGHT),
        ("Гибкость", "Быстрая переналадка\nна новые задачи", ACCENT_CYAN),
        ("Датчики силы", "Реагируют на\nстолкновения", HIGHLIGHT),
    ]

    for i, (title, desc, color) in enumerate(cobot_items):
        cy = 380 + i * 48
        ET.SubElement(svg, "rect", {
            "x": "310", "y": str(cy), "width": "230", "height": "40",
            "rx": "6", "fill": BG_CODE, "stroke": color, "stroke-width": "0.5"
        })
        ET.SubElement(svg, "rect", {
            "x": "310", "y": str(cy), "width": "3", "height": "40",
            "fill": color
        })
        ET.SubElement(svg, "text", {
            "x": "320", "y": str(cy + 16),
            "font-family": "Arial, sans-serif", "font-size": "10",
            "font-weight": "bold", "fill": color
        }).text = escape(title)
        desc_lines = desc.split("\n")
        for j, line in enumerate(desc_lines):
            ET.SubElement(svg, "text", {
                "x": "320", "y": str(cy + 28 + j * 10),
                "font-family": "Arial, sans-serif", "font-size": "7",
                "fill": TEXT_MUTED
            }).text = escape(line)

    # ── Future trends ──
    add_card(svg, 570, 335, 210, 240, "Тренды будущего")

    trends = [
        ("🧬", "Мягкая робототехника", PRIMARY_LIGHT),
        ("🧠", "Нейроморфные чипы", HIGHLIGHT2),
        ("🤝", "Рой роботов", ACCENT_CYAN),
        ("🔬", "Нанороботы", ACCENT_TEAL),
        ("🚀", "Космические роботы", HIGHLIGHT),
        ("🦾", "Экзоскелеты", SUCCESS),
    ]

    for i, (emoji, name, color) in enumerate(trends):
        ty = 380 + i * 30
        ET.SubElement(svg, "text", {
            "x": "585", "y": str(ty),
            "font-size": "14"
        }).text = emoji
        ET.SubElement(svg, "text", {
            "x": "608", "y": str(ty),
            "font-family": "Arial, sans-serif", "font-size": "9",
            "fill": color
        }).text = escape(name)

    return svg


# ═══════════════════════════════════════════════════════════════
#  MAIN — Generate and validate all SVGs
# ═══════════════════════════════════════════════════════════════
def indent_xml(elem, level=0):
    """Add indentation to XML for pretty-printing."""
    indent = "\n" + "  " * level
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = indent + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = indent
        for child in elem:
            indent_xml(child, level + 1)
        if not child.tail or not child.tail.strip():
            child.tail = indent
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = indent


generators = [
    (1, lesson_1),
    (2, lesson_2),
    (3, lesson_3),
    (4, lesson_4),
    (5, lesson_5),
    (6, lesson_6),
    (7, lesson_7),
    (8, lesson_8),
]

results = []
for n, gen_fn in generators:
    filepath = os.path.join(OUTPUT_DIR, f"lesson-{n}.svg")
    try:
        svg = gen_fn()
        indent_xml(svg)

        tree = ET.ElementTree(svg)
        tree.write(filepath, encoding="unicode", xml_declaration=True)

        # Validate
        ET.parse(filepath)
        file_size = os.path.getsize(filepath)
        results.append(f"✅ lesson-{n}.svg — {file_size:,} bytes — VALID XML")
    except Exception as e:
        results.append(f"❌ lesson-{n}.svg — ERROR: {e}")

print("=" * 60)
print("  Grade 8 Robotics SVG Generation Report")
print("=" * 60)
for r in results:
    print(f"  {r}")
print("=" * 60)
print(f"  Total: {len(results)} files generated")
print(f"  Output: {OUTPUT_DIR}")
