#!/usr/bin/env python3
"""Generate Grade 7 Geometry SVG lesson images (7 lessons)."""

import os

BASE_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/geometry"
os.makedirs(BASE_DIR, exist_ok=True)

# ── colour palette ──────────────────────────────────────────────────
C_PRIMARY      = "#06B6D4"
C_PRIMARY_DK   = "#0891B2"
C_PRIMARY_DKR  = "#0E7490"
C_PRIMARY_LT   = "#22D3EE"
C_BG_TOP       = "#F0FDFA"
C_BG_BOT       = "#ECFEFF"
C_TEXT          = "#37474F"
C_TEXT_DK       = "#263238"
C_WHITE        = "#FFFFFF"
C_ACCENT       = "#D97706"
C_ACCENT_LT    = "#FCD34D"
C_GREEN        = "#059669"
C_RED          = "#DC2626"
C_PURPLE       = "#7C3AED"
C_ORANGE       = "#EA580C"


def svg_head(title: str, lesson_num: int, extra_defs: str = "") -> str:
    """Return the common SVG header with gradients, border, header bar."""
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">
  <defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{C_BG_TOP}" />
      <stop offset="100%" stop-color="{C_BG_BOT}" />
    </linearGradient>
    <linearGradient id="headerGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{C_PRIMARY_DK}" />
      <stop offset="100%" stop-color="{C_PRIMARY}" />
    </linearGradient>
    <linearGradient id="panelGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{C_PRIMARY}" />
      <stop offset="100%" stop-color="{C_PRIMARY_DK}" />
    </linearGradient>
    {extra_defs}
  </defs>
  <!-- background & border -->
  <rect width="800" height="600" fill="url(#bgGrad)" rx="12" />
  <rect x="3" y="3" width="794" height="594" rx="10" fill="none" stroke="{C_PRIMARY}" stroke-width="2.5" />
  <rect x="8" y="8" width="784" height="584" rx="8" fill="none" stroke="{C_PRIMARY}" stroke-width="1" opacity="0.2" />
  <!-- corner decorations -->
  <polygon points="12,12 42,12 12,42" fill="{C_PRIMARY}" opacity="0.08" />
  <polygon points="788,12 758,12 788,42" fill="{C_PRIMARY}" opacity="0.08" />
  <polygon points="12,588 42,588 12,558" fill="{C_PRIMARY}" opacity="0.08" />
  <polygon points="788,588 758,588 788,558" fill="{C_PRIMARY}" opacity="0.08" />
  <!-- decorative shapes -->
  <circle cx="740" cy="100" r="25" fill="none" stroke="{C_PRIMARY}" stroke-width="1" opacity="0.1" />
  <polygon points="60,540 80,510 100,540" fill="none" stroke="{C_PRIMARY}" stroke-width="1" opacity="0.1" />
  <rect x="70" y="80" width="18" height="18" fill="none" stroke="{C_PRIMARY}" stroke-width="1" opacity="0.08" transform="rotate(45,79,89)" />
  <!-- header bar -->
  <rect x="15" y="15" width="770" height="55" fill="url(#headerGrad)" rx="8" opacity="0.92" />
  <rect x="25" y="22" width="50" height="38" fill="{C_WHITE}" rx="6" opacity="0.25" />
  <text x="50" y="49" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="{C_WHITE}" text-anchor="middle">{lesson_num}</text>
  <text x="410" y="48" font-family="Arial,sans-serif" font-size="24" font-weight="bold" fill="{C_WHITE}" text-anchor="middle">{title}</text>
  <text x="760" y="35" font-family="Arial,sans-serif" font-size="10" fill="{C_WHITE}" text-anchor="end" opacity="0.7">7 класс</text>
  <text x="760" y="50" font-family="Arial,sans-serif" font-size="10" fill="{C_WHITE}" text-anchor="end" opacity="0.7">Геометрия</text>
  <line x1="20" y1="80" x2="780" y2="80" stroke="{C_PRIMARY}" stroke-width="2" opacity="0.25" />
'''


def svg_tail() -> str:
    return "</svg>\n"


def panel(x, y, w, h, title="", title_color=C_PRIMARY_DKR) -> str:
    """Rounded panel with optional title strip."""
    s = f'''  <rect x="{x+3}" y="{y+3}" width="{w}" height="{h}" fill="#000000" rx="8" opacity="0.05" />
  <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{C_WHITE}" rx="8" stroke="{C_PRIMARY}" stroke-width="1.5" opacity="0.95" />
'''
    if title:
        s += f'''  <rect x="{x}" y="{y}" width="{w}" height="24" fill="{C_PRIMARY}" rx="8" opacity="0.15" />
  <rect x="{x}" y="{y+16}" width="{w}" height="8" fill="{C_PRIMARY}" opacity="0.15" />
  <text x="{x + w//2}" y="{y+17}" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="{title_color}" text-anchor="middle">{title}</text>
'''
    return s


def formula_box(x, y, w, h, text_lines, bg_color="#FFF7ED", border_color=C_ACCENT) -> str:
    """Highlighted formula / theorem box."""
    s = f'''  <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{bg_color}" rx="8" stroke="{border_color}" stroke-width="1.5" />
  <rect x="{x}" y="{y}" width="5" height="{h}" fill="{border_color}" rx="2" />
'''
    ty = y + 20
    for line in text_lines:
        s += f'  <text x="{x+16}" y="{ty}" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="{C_TEXT_DK}">{line}</text>\n'
        ty += 18
    return s


def point_label(cx, cy, label, color=C_PRIMARY_DKR, size=14) -> str:
    return f'''  <circle cx="{cx}" cy="{cy}" r="3.5" fill="{color}" />
  <text x="{cx}" y="{cy-8}" font-family="Arial,sans-serif" font-size="{size}" font-weight="bold" fill="{color}" text-anchor="middle">{label}</text>
'''


# ═══════════════════════════════════════════════════════════════════
# LESSON 1 — Точки, прямые, отрезки
# ═══════════════════════════════════════════════════════════════════
def lesson1() -> str:
    s = svg_head("Точки, прямые, отрезки", 1)
    # ── Left panel: definitions ──
    s += panel(20, 90, 370, 200, "Основные понятия")
    s += f'''  <text x="32" y="130" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}"><tspan font-weight="bold" fill="{C_PRIMARY_DKR}">Точка</tspan> — самое простое понятие геометрии.</text>
  <text x="32" y="148" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">Точка не имеет размеров, обозначается: A, B, C ...</text>
  <text x="32" y="172" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}"><tspan font-weight="bold" fill="{C_PRIMARY_DKR}">Прямая</tspan> — бесконечна в обе стороны,</text>
  <text x="32" y="190" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">обозначается: a, b, c ... или AB</text>
  <text x="32" y="214" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}"><tspan font-weight="bold" fill="{C_PRIMARY_DKR}">Отрезок</tspan> — часть прямой, ограниченная</text>
  <text x="32" y="232" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">двумя точками. Обозначается: AB</text>
  <text x="32" y="256" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}"><tspan font-weight="bold" fill="{C_PRIMARY_DKR}">Луч</tspan> — часть прямой с началом в точке,</text>
  <text x="32" y="274" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">бесконечная в одну сторону. Обозначается: OA</text>
'''
    # ── Right panel: diagram ──
    s += panel(410, 90, 370, 200, "Диаграмма")
    # Point A
    s += point_label(470, 150, "A")
    # Point B
    s += point_label(630, 150, "B")
    # Segment AB
    s += f'  <line x1="473" y1="150" x2="627" y2="150" stroke="{C_PRIMARY}" stroke-width="3" />\n'
    s += f'  <text x="550" y="143" font-family="Arial,sans-serif" font-size="11" fill="{C_ACCENT}" text-anchor="middle">отрезок AB</text>\n'
    # Line through C
    s += point_label(470, 210, "C")
    s += f'  <line x1="435" y1="210" x2="740" y2="210" stroke="{C_PRIMARY_DKR}" stroke-width="2" stroke-dasharray="8,4" />\n'
    s += f'  <text x="660" y="203" font-family="Arial,sans-serif" font-size="11" fill="{C_PRIMARY_DKR}">прямая a</text>\n'
    # Ray from O
    s += point_label(470, 260, "O")
    s += f'  <line x1="473" y1="260" x2="750" y2="260" stroke="{C_RED}" stroke-width="2.5" />\n'
    s += f'  <polygon points="750,260 740,255 740,265" fill="{C_RED}" />\n'
    s += f'  <text x="630" y="253" font-family="Arial,sans-serif" font-size="11" fill="{C_RED}">луч OA</text>\n'

    # ── Bottom-left: intersection ──
    s += panel(20, 305, 370, 175, "Пересечение прямых")
    # Two intersecting lines
    s += f'  <line x1="45" y1="370" x2="250" y2="460" stroke="{C_PRIMARY}" stroke-width="2.5" />\n'
    s += f'  <line x1="45" y1="460" x2="250" y2="370" stroke="{C_RED}" stroke-width="2.5" />\n'
    s += point_label(148, 415, "O", C_RED)
    s += f'  <text x="270" y="385" font-family="Arial,sans-serif" font-size="11" fill="{C_PRIMARY}">прямая a</text>\n'
    s += f'  <text x="270" y="450" font-family="Arial,sans-serif" font-size="11" fill="{C_RED}">прямая b</text>\n'
    s += f'  <text x="60" y="475" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}">Две прямые пересекаются</text>\n'
    s += f'  <text x="60" y="490" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}">в одной точке O</text>\n'

    # ── Bottom-right: key properties ──
    s += formula_box(410, 305, 370, 80, [
        "Аксиома: через любые две точки",
        "можно провести прямую, и притом",
        "только одну.",
    ])
    s += formula_box(410, 400, 370, 80, [
        "Две прямые либо имеют одну",
        "общую точку (пересекаются),",
        "либо не имеют ни одной (параллельны).",
    ], bg_color="#F0FDF4", border_color=C_GREEN)

    s += svg_tail()
    return s


# ═══════════════════════════════════════════════════════════════════
# LESSON 2 — Угол и его виды
# ═══════════════════════════════════════════════════════════════════
def lesson2() -> str:
    s = svg_head("Угол и его виды", 2)
    # ── Left panel: definition ──
    s += panel(20, 90, 370, 130, "Определение угла")
    s += f'''  <text x="32" y="130" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}"><tspan font-weight="bold" fill="{C_PRIMARY_DKR}">Угол</tspan> — геометрическая фигура,</text>
  <text x="32" y="148" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">состоящая из двух лучей, выходящих</text>
  <text x="32" y="166" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">из одной точки (вершины).</text>
  <text x="32" y="190" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">Обозначение: ∠AOB, ∠α, ∠β</text>
  <text x="32" y="208" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">Единица измерения: градус (°)</text>
'''
    # ── Right panel: angle diagram ──
    s += panel(410, 90, 370, 130, "Угол ∠AOB")
    # vertex O
    s += f'  <line x1="490" y1="200" x2="570" y2="130" stroke="{C_PRIMARY}" stroke-width="2.5" />\n'
    s += f'  <line x1="490" y1="200" x2="630" y2="200" stroke="{C_PRIMARY}" stroke-width="2.5" />\n'
    # arc for angle
    s += f'  <path d="M 520,185 A 35,35 0 0,1 525,172" fill="none" stroke="{C_ACCENT}" stroke-width="2" />\n'
    s += point_label(490, 200, "O")
    s += f'  <text x="575" y="128" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="{C_PRIMARY_DKR}">A</text>\n'
    s += f'  <text x="640" y="203" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="{C_PRIMARY_DKR}">B</text>\n'
    s += f'  <text x="533" y="178" font-family="Arial,sans-serif" font-size="12" fill="{C_ACCENT}">α</text>\n'

    # ── Bottom: 4 angle types ──
    # Acute
    s += panel(20, 235, 180, 175, "Острый")
    s += f'  <text x="110" y="272" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}" text-anchor="middle">0° &lt; α &lt; 90°</text>\n'
    s += f'  <line x1="60" y1="390" x2="160" y2="390" stroke="{C_PRIMARY}" stroke-width="2.5" />\n'
    s += f'  <line x1="60" y1="390" x2="105" y2="310" stroke="{C_PRIMARY}" stroke-width="2.5" />\n'
    s += f'  <path d="M 80,383 A 25,25 0 0,1 78,370" fill="none" stroke="{C_ACCENT}" stroke-width="2" />\n'
    s += f'  <text x="88" y="372" font-family="Arial,sans-serif" font-size="11" fill="{C_ACCENT}">α</text>\n'
    s += point_label(60, 390, "", C_PRIMARY_DKR, 10)

    # Right
    s += panel(210, 235, 180, 175, "Прямой")
    s += f'  <text x="300" y="272" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}" text-anchor="middle">α = 90°</text>\n'
    s += f'  <line x1="250" y1="390" x2="350" y2="390" stroke="{C_PRIMARY}" stroke-width="2.5" />\n'
    s += f'  <line x1="250" y1="390" x2="250" y2="310" stroke="{C_PRIMARY}" stroke-width="2.5" />\n'
    # right-angle square
    s += f'  <rect x="250" y="375" width="15" height="15" fill="none" stroke="{C_ACCENT}" stroke-width="1.5" />\n'

    # Obtuse
    s += panel(400, 235, 180, 175, "Тупой")
    s += f'  <text x="490" y="272" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}" text-anchor="middle">90° &lt; α &lt; 180°</text>\n'
    s += f'  <line x1="440" y1="390" x2="560" y2="390" stroke="{C_PRIMARY}" stroke-width="2.5" />\n'
    s += f'  <line x1="440" y1="390" x2="475" y2="310" stroke="{C_PRIMARY}" stroke-width="2.5" />\n'
    s += f'  <path d="M 458,383 A 25,25 0 0,0 465,360" fill="none" stroke="{C_ACCENT}" stroke-width="2" />\n'
    s += f'  <text x="468" y="365" font-family="Arial,sans-serif" font-size="11" fill="{C_ACCENT}">α</text>\n'

    # Straight / Развернутый
    s += panel(590, 235, 190, 175, "Развёрнутый")
    s += f'  <text x="685" y="272" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}" text-anchor="middle">α = 180°</text>\n'
    s += f'  <line x1="620" y1="370" x2="750" y2="370" stroke="{C_PRIMARY}" stroke-width="2.5" />\n'
    s += point_label(685, 370, "O", C_PRIMARY_DKR, 12)
    s += f'  <text x="630" y="363" font-family="Arial,sans-serif" font-size="11" fill="{C_PRIMARY_DKR}">A</text>\n'
    s += f'  <text x="740" y="363" font-family="Arial,sans-serif" font-size="11" fill="{C_PRIMARY_DKR}">B</text>\n'

    # ── Bisector box ──
    s += formula_box(20, 425, 760, 60, [
        "Биссектриса угла — луч, выходящий из вершины угла и делящий его пополам.",
        "Если ∠AOB = α, то биссектриса OC образует два угла по α/2.",
    ], bg_color="#F0FDF4", border_color=C_GREEN)

    # ── Bisector mini diagram ──
    s += panel(20, 500, 760, 85, "Биссектриса")
    s += f'  <line x1="80" y1="565" x2="200" y2="510" stroke="{C_PRIMARY}" stroke-width="2" />\n'
    s += f'  <line x1="80" y1="565" x2="200" y2="565" stroke="{C_PRIMARY}" stroke-width="2" />\n'
    s += f'  <line x1="80" y1="565" x2="230" y2="538" stroke="{C_GREEN}" stroke-width="2" stroke-dasharray="6,3" />\n'
    s += point_label(80, 565, "O", C_PRIMARY_DKR, 12)
    s += f'  <text x="203" y="507" font-family="Arial,sans-serif" font-size="11" fill="{C_PRIMARY_DKR}">A</text>\n'
    s += f'  <text x="203" y="575" font-family="Arial,sans-serif" font-size="11" fill="{C_PRIMARY_DKR}">B</text>\n'
    s += f'  <text x="234" y="535" font-family="Arial,sans-serif" font-size="11" fill="{C_GREEN}">C (биссектриса)</text>\n'
    # angle arcs
    s += f'  <path d="M 100,558 A 20,20 0 0,1 104,547" fill="none" stroke="{C_ACCENT}" stroke-width="1.5" />\n'
    s += f'  <path d="M 104,547 A 20,20 0 0,1 112,552" fill="none" stroke="{C_RED}" stroke-width="1.5" />\n'
    # formula text
    s += f'  <text x="300" y="530" font-family="Arial,sans-serif" font-size="13" fill="{C_TEXT}">∠AOC = ∠COB = α/2</text>\n'
    s += f'  <text x="300" y="555" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">Биссектриса делит угол на два равных угла</text>\n'

    s += svg_tail()
    return s


# ═══════════════════════════════════════════════════════════════════
# LESSON 3 — Треугольник
# ═══════════════════════════════════════════════════════════════════
def lesson3() -> str:
    s = svg_head("Треугольник", 3)
    # ── Top-left: definition ──
    s += panel(20, 90, 370, 110, "Определение")
    s += f'''  <text x="32" y="130" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}"><tspan font-weight="bold" fill="{C_PRIMARY_DKR}">Треугольник</tspan> — фигура, состоящая</text>
  <text x="32" y="148" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">из трёх точек (вершин), не лежащих</text>
  <text x="32" y="166" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">на одной прямой, и трёх отрезков,</text>
  <text x="32" y="184" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">их соединяющих (сторон).</text>
'''
    # ── Top-right: triangle diagram ──
    s += panel(410, 90, 370, 110, "Обозначение △ABC")
    # Triangle
    s += f'  <polygon points="520,185 600,110 680,185" fill="none" stroke="{C_PRIMARY}" stroke-width="2.5" />\n'
    s += point_label(520, 185, "A")
    s += point_label(600, 110, "B")
    s += point_label(680, 185, "C")
    s += f'  <text x="545" y="155" font-family="Arial,sans-serif" font-size="10" fill="{C_ACCENT}">c</text>\n'
    s += f'  <text x="640" y="140" font-family="Arial,sans-serif" font-size="10" fill="{C_ACCENT}">a</text>\n'
    s += f'  <text x="600" y="198" font-family="Arial,sans-serif" font-size="10" fill="{C_ACCENT}">b</text>\n'

    # ── Middle row: Types by sides ──
    s += panel(20, 215, 245, 170, "По сторонам")
    # Equilateral
    s += f'  <polygon points="60,285 90,255 120,285" fill="#ECFEFF" stroke="{C_PRIMARY}" stroke-width="2" />\n'
    s += f'  <text x="90" y="300" font-family="Arial,sans-serif" font-size="10" fill="{C_TEXT_DK}" text-anchor="middle">Равносторонний</text>\n'
    s += f'  <text x="90" y="314" font-family="Arial,sans-serif" font-size="10" fill="{C_PRIMARY_DKR}" text-anchor="middle">a = b = c</text>\n'
    # Isosceles
    s += f'  <polygon points="160,285 190,250 220,285" fill="#ECFEFF" stroke="{C_PRIMARY}" stroke-width="2" />\n'
    s += f'  <text x="190" y="300" font-family="Arial,sans-serif" font-size="10" fill="{C_TEXT_DK}" text-anchor="middle">Равнобедренный</text>\n'
    s += f'  <text x="190" y="314" font-family="Arial,sans-serif" font-size="10" fill="{C_PRIMARY_DKR}" text-anchor="middle">a = b ≠ c</text>\n'
    # Scalene
    s += f'  <polygon points="50,370 105,330 140,370" fill="#ECFEFF" stroke="{C_PRIMARY}" stroke-width="2" />\n'
    s += f'  <text x="95" y="383" font-family="Arial,sans-serif" font-size="10" fill="{C_TEXT_DK}" text-anchor="middle">Разносторонний</text>\n'
    s += f'  <text x="95" y="397" font-family="Arial,sans-serif" font-size="10" fill="{C_PRIMARY_DKR}" text-anchor="middle">a ≠ b ≠ c</text>\n'

    # ── Middle-right: Types by angles ──
    s += panel(280, 215, 245, 170, "По углам")
    # Acute
    s += f'  <polygon points="320,310 360,280 390,310" fill="#FFF7ED" stroke="{C_ORANGE}" stroke-width="2" />\n'
    s += f'  <text x="355" y="326" font-family="Arial,sans-serif" font-size="10" fill="{C_TEXT_DK}" text-anchor="middle">Остроугольный</text>\n'
    # Right
    s += f'  <polygon points="320,375 360,340 320,340" fill="#FFF7ED" stroke="{C_ORANGE}" stroke-width="2" />\n'
    s += f'  <rect x="320" y="362" width="13" height="13" fill="none" stroke="{C_ORANGE}" stroke-width="1.2" />\n'
    s += f'  <text x="350" y="375" font-family="Arial,sans-serif" font-size="10" fill="{C_TEXT_DK}" text-anchor="middle">Прямоугольный</text>\n'
    # Obtuse
    s += f'  <polygon points="430,375 460,345 510,375" fill="#FFF7ED" stroke="{C_ORANGE}" stroke-width="2" />\n'
    s += f'  <text x="470" y="390" font-family="Arial,sans-serif" font-size="10" fill="{C_TEXT_DK}" text-anchor="middle">Тупоугольный</text>\n'

    # ── Right column: properties ──
    s += panel(540, 215, 240, 170, "Свойства")
    s += f'''  <text x="552" y="258" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}">1. Против большей стороны</text>
  <text x="552" y="274" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}">   лежит больший угол</text>
  <text x="552" y="298" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}">2. Сумма любых двух сторон</text>
  <text x="552" y="314" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}">   больше третьей:</text>
  <text x="552" y="336" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="{C_PRIMARY_DKR}">   a + b &gt; c</text>
  <text x="552" y="358" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}">3. Сумма углов = 180°</text>
  <text x="552" y="374" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="{C_PRIMARY_DKR}">   ∠A + ∠B + ∠C = 180°</text>
'''

    # ── Bottom: Perimeter formula ──
    s += formula_box(20, 400, 760, 55, [
        "Периметр треугольника:  P = a + b + c",
    ])
    # ── Bottom: equal sides property ──
    s += panel(20, 470, 760, 115, "Свойства равнобедренного треугольника")
    # Isosceles triangle
    s += f'  <polygon points="100,560 140,490 180,560" fill="#ECFEFF" stroke="{C_PRIMARY}" stroke-width="2.5" />\n'
    s += f'  <line x1="140" y1="490" x2="140" y2="560" stroke="{C_GREEN}" stroke-width="1.5" stroke-dasharray="5,3" />\n'
    s += point_label(100, 560, "A")
    s += point_label(140, 490, "B")
    s += point_label(180, 560, "C")
    s += f'  <text x="155" y="530" font-family="Arial,sans-serif" font-size="10" fill="{C_GREEN}">h</text>\n'
    s += f'  <text x="260" y="505" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">1. Углы при основании равны: ∠A = ∠C</text>\n'
    s += f'  <text x="260" y="525" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">2. Биссектриса к основанию является</text>\n'
    s += f'  <text x="260" y="543" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">   медианой и высотой</text>\n'
    s += f'  <text x="260" y="563" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">3. Высота, биссектриса и медиана,</text>\n'
    s += f'  <text x="260" y="578" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">   проведённые к основанию, совпадают</text>\n'

    s += svg_tail()
    return s


# ═══════════════════════════════════════════════════════════════════
# LESSON 4 — Медианы, биссектрисы, высоты
# ═══════════════════════════════════════════════════════════════════
def lesson4() -> str:
    s = svg_head("Медианы, биссектрисы, высоты", 4)
    # ── Definitions ──
    s += panel(20, 90, 370, 150, "Определения")
    s += f'''  <text x="32" y="128" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}"><tspan font-weight="bold" fill="{C_PRIMARY_DKR}">Медиана</tspan> — отрезок, соединяющий</text>
  <text x="32" y="146" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">вершину с серединой противоположной</text>
  <text x="32" y="162" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">стороны.</text>
  <text x="32" y="184" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}"><tspan font-weight="bold" fill="{C_PRIMARY_DKR}">Биссектриса</tspan> — отрезок биссектрисы</text>
  <text x="32" y="202" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">угла, от вершины до противолежащей</text>
  <text x="32" y="218" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">стороны.</text>
  <text x="32" y="236" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}"><tspan font-weight="bold" fill="{C_PRIMARY_DKR}">Высота</tspan> — перпендикуляр из вершины</text>
'''

    # ── Medians diagram ──
    s += panel(410, 90, 370, 150, "Медианы")
    # Triangle
    s += f'  <polygon points="500,220 590,120 700,220" fill="none" stroke="{C_PRIMARY}" stroke-width="2" />\n'
    # Midpoints
    s += f'  <circle cx="545" cy="170" r="3" fill="{C_RED}" />\n'  # mid AB
    s += f'  <circle cx="645" cy="170" r="3" fill="{C_RED}" />\n'  # mid BC
    s += f'  <circle cx="600" cy="220" r="3" fill="{C_RED}" />\n'  # mid AC
    # Medians
    s += f'  <line x1="500" y1="220" x2="645" y2="170" stroke="{C_RED}" stroke-width="1.5" stroke-dasharray="5,3" />\n'
    s += f'  <line x1="590" y1="120" x2="600" y2="220" stroke="{C_RED}" stroke-width="1.5" stroke-dasharray="5,3" />\n'
    s += f'  <line x1="700" y1="220" x2="545" y2="170" stroke="{C_RED}" stroke-width="1.5" stroke-dasharray="5,3" />\n'
    # Centroid
    s += f'  <circle cx="597" cy="187" r="4" fill="{C_ACCENT}" />\n'
    s += point_label(500, 220, "A")
    s += point_label(590, 120, "B")
    s += point_label(700, 220, "C")
    s += f'  <text x="607" y="193" font-family="Arial,sans-serif" font-size="11" fill="{C_ACCENT}">M</text>\n'

    # ── Bisectors diagram ──
    s += panel(20, 255, 370, 170, "Биссектрисы")
    s += f'  <polygon points="90,400 180,280 280,400" fill="none" stroke="{C_PRIMARY}" stroke-width="2" />\n'
    # Bisectors
    s += f'  <line x1="90" y1="400" x2="222" y2="365" stroke="{C_PURPLE}" stroke-width="1.5" stroke-dasharray="5,3" />\n'
    s += f'  <line x1="180" y1="280" x2="185" y2="400" stroke="{C_PURPLE}" stroke-width="1.5" stroke-dasharray="5,3" />\n'
    s += f'  <line x1="280" y1="400" x2="147" y2="360" stroke="{C_PURPLE}" stroke-width="1.5" stroke-dasharray="5,3" />\n'
    # Incenter
    s += f'  <circle cx="183" cy="370" r="4" fill="{C_ACCENT}" />\n'
    s += point_label(90, 400, "A")
    s += point_label(180, 280, "B")
    s += point_label(280, 400, "C")
    s += f'  <text x="193" y="377" font-family="Arial,sans-serif" font-size="11" fill="{C_ACCENT}">I</text>\n'

    # ── Altitudes diagram ──
    s += panel(410, 255, 370, 170, "Высоты")
    s += f'  <polygon points="480,400 570,290 690,400" fill="none" stroke="{C_PRIMARY}" stroke-width="2" />\n'
    # Altitudes
    s += f'  <line x1="480" y1="400" x2="623" y2="375" stroke="{C_GREEN}" stroke-width="1.5" stroke-dasharray="5,3" />\n'
    s += f'  <line x1="570" y1="290" x2="585" y2="400" stroke="{C_GREEN}" stroke-width="1.5" stroke-dasharray="5,3" />\n'
    s += f'  <line x1="690" y1="400" x2="534" y2="358" stroke="{C_GREEN}" stroke-width="1.5" stroke-dasharray="5,3" />\n'
    # Orthocenter
    s += f'  <circle cx="580" cy="377" r="4" fill="{C_ACCENT}" />\n'
    s += point_label(480, 400, "A")
    s += point_label(570, 290, "B")
    s += point_label(690, 400, "C")
    s += f'  <text x="590" y="383" font-family="Arial,sans-serif" font-size="11" fill="{C_ACCENT}">H</text>\n'

    # ── Bottom: key properties ──
    s += formula_box(20, 440, 370, 65, [
        "Медианы пересекаются в одной",
        "точке M и делятся 2:1 от вершины.",
    ], bg_color="#FFF7ED", border_color=C_ACCENT)
    s += formula_box(410, 440, 370, 65, [
        "Высоты пересекаются в одной",
        "точке H — ортоцентре треугольника.",
    ], bg_color="#F0FDF4", border_color=C_GREEN)

    s += formula_box(20, 520, 370, 65, [
        "Биссектрисы пересекаются в одной",
        "точке I — центре вписанной окружности.",
    ], bg_color="#FDF4FF", border_color=C_PURPLE)
    s += formula_box(410, 520, 370, 65, [
        "В равнобедренном △ медиана,",
        "биссектриса и высота совпадают.",
    ], bg_color="#FEF2F2", border_color=C_RED)

    s += svg_tail()
    return s


# ═══════════════════════════════════════════════════════════════════
# LESSON 5 — Признаки равенства треугольников
# ═══════════════════════════════════════════════════════════════════
def lesson5() -> str:
    s = svg_head("Признаки равенства треугольников", 5)
    # ── SSS ──
    s += panel(20, 90, 240, 240, "1-й признак: ССС")
    # Two triangles side by side
    s += f'  <polygon points="45,270 90,195 135,270" fill="#ECFEFF" stroke="{C_PRIMARY}" stroke-width="2" />\n'
    s += f'  <polygon points="145,270 190,195 235,270" fill="#FFF7ED" stroke="{C_ORANGE}" stroke-width="2" />\n'
    # Tick marks on sides
    s += f'  <line x1="65" y1="232" x2="69" y2="238" stroke="{C_PRIMARY_DKR}" stroke-width="1.5" />\n'
    s += f'  <line x1="165" y1="232" x2="169" y2="238" stroke="{C_ORANGE}" stroke-width="1.5" />\n'
    s += f'  <line x1="112" y1="230" x2="116" y2="236" stroke="{C_PRIMARY_DKR}" stroke-width="1.5" />\n'
    s += f'  <line x1="212" y1="230" x2="216" y2="236" stroke="{C_ORANGE}" stroke-width="1.5" />\n'
    s += f'  <line x1="85" y1="268" x2="89" y2="274" stroke="{C_PRIMARY_DKR}" stroke-width="1.5" />\n'
    s += f'  <line x1="185" y1="268" x2="189" y2="274" stroke="{C_ORANGE}" stroke-width="1.5" />\n'
    s += f'  <text x="140" y="296" font-family="Arial,sans-serif" font-size="10" fill="{C_TEXT_DK}" text-anchor="middle">AB=A&#8321;B&#8321;  BC=B&#8321;C&#8321;  AC=A&#8321;C&#8321;</text>\n'
    s += f'  <text x="140" y="315" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="{C_GREEN}" text-anchor="middle">=&gt; △ABC = △A&#8321;B&#8321;C&#8321;</text>\n'

    # ── SAS ──
    s += panel(280, 90, 240, 240, "2-й признак: СУС")
    s += f'  <polygon points="305,270 350,195 395,270" fill="#ECFEFF" stroke="{C_PRIMARY}" stroke-width="2" />\n'
    s += f'  <polygon points="405,270 450,195 495,270" fill="#FFF7ED" stroke="{C_ORANGE}" stroke-width="2" />\n'
    # Angle arcs
    s += f'  <path d="M 317,262 A 15,15 0 0,1 322,252" fill="none" stroke="{C_RED}" stroke-width="1.5" />\n'
    s += f'  <path d="M 417,262 A 15,15 0 0,1 422,252" fill="none" stroke="{C_RED}" stroke-width="1.5" />\n'
    # tick marks
    s += f'  <line x1="325" y1="232" x2="329" y2="238" stroke="{C_PRIMARY_DKR}" stroke-width="1.5" />\n'
    s += f'  <line x1="425" y1="232" x2="429" y2="238" stroke="{C_ORANGE}" stroke-width="1.5" />\n'
    s += f'  <line x1="365" y1="268" x2="369" y2="274" stroke="{C_PRIMARY_DKR}" stroke-width="1.5" />\n'
    s += f'  <line x1="465" y1="268" x2="469" y2="274" stroke="{C_ORANGE}" stroke-width="1.5" />\n'
    s += f'  <text x="400" y="296" font-family="Arial,sans-serif" font-size="10" fill="{C_TEXT_DK}" text-anchor="middle">AB=A&#8321;B&#8321;  ∠A=∠A&#8321;  AC=A&#8321;C&#8321;</text>\n'
    s += f'  <text x="400" y="315" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="{C_GREEN}" text-anchor="middle">=&gt; △ABC = △A&#8321;B&#8321;C&#8321;</text>\n'

    # ── ASA ──
    s += panel(540, 90, 240, 240, "3-й признак: УСУ")
    s += f'  <polygon points="565,270 610,195 655,270" fill="#ECFEFF" stroke="{C_PRIMARY}" stroke-width="2" />\n'
    s += f'  <polygon points="665,270 710,195 755,270" fill="#FFF7ED" stroke="{C_ORANGE}" stroke-width="2" />\n'
    # Angle arcs at two vertices
    s += f'  <path d="M 577,262 A 15,15 0 0,1 582,252" fill="none" stroke="{C_RED}" stroke-width="1.5" />\n'
    s += f'  <path d="M 677,262 A 15,15 0 0,1 682,252" fill="none" stroke="{C_RED}" stroke-width="1.5" />\n'
    s += f'  <path d="M 625,230 A 15,15 0 0,0 640,225" fill="none" stroke="{C_RED}" stroke-width="1.5" />\n'
    s += f'  <path d="M 725,230 A 15,15 0 0,0 740,225" fill="none" stroke="{C_RED}" stroke-width="1.5" />\n'
    # tick mark on one side
    s += f'  <line x1="605" y1="232" x2="609" y2="238" stroke="{C_PRIMARY_DKR}" stroke-width="1.5" />\n'
    s += f'  <line x1="705" y1="232" x2="709" y2="238" stroke="{C_ORANGE}" stroke-width="1.5" />\n'
    s += f'  <text x="660" y="296" font-family="Arial,sans-serif" font-size="10" fill="{C_TEXT_DK}" text-anchor="middle">∠A=∠A&#8321;  AB=A&#8321;B&#8321;  ∠B=∠B&#8321;</text>\n'
    s += f'  <text x="660" y="315" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="{C_GREEN}" text-anchor="middle">=&gt; △ABC = △A&#8321;B&#8321;C&#8321;</text>\n'

    # ── Key properties ──
    s += formula_box(20, 345, 760, 55, [
        "Треугольники равны, если их можно совместить наложением. У равных треугольников все",
        "соответствующие элементы равны: стороны, углы, высоты, медианы, биссектрисы.",
    ], bg_color="#F0FDF4", border_color=C_GREEN)

    # ── Summary table ──
    s += panel(20, 415, 760, 170, "Сводка признаков равенства")
    # Table header
    s += f'  <rect x="30" y="445" width="240" height="22" fill="{C_PRIMARY}" rx="4" opacity="0.2" />\n'
    s += f'  <rect x="275" y="445" width="240" height="22" fill="{C_PRIMARY}" rx="4" opacity="0.2" />\n'
    s += f'  <rect x="520" y="445" width="250" height="22" fill="{C_PRIMARY}" rx="4" opacity="0.2" />\n'
    s += f'  <text x="150" y="461" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="{C_PRIMARY_DKR}" text-anchor="middle">1-й признак (ССС)</text>\n'
    s += f'  <text x="395" y="461" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="{C_PRIMARY_DKR}" text-anchor="middle">2-й признак (СУС)</text>\n'
    s += f'  <text x="645" y="461" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="{C_PRIMARY_DKR}" text-anchor="middle">3-й признак (УСУ)</text>\n'
    # Table body
    s += f'  <text x="150" y="490" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}" text-anchor="middle">Три стороны</text>\n'
    s += f'  <text x="150" y="506" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}" text-anchor="middle">одного треугольника</text>\n'
    s += f'  <text x="150" y="522" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}" text-anchor="middle">равны трём сторонам</text>\n'
    s += f'  <text x="150" y="538" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}" text-anchor="middle">другого</text>\n'
    s += f'  <text x="150" y="558" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}" text-anchor="middle">a=a&#8321;, b=b&#8321;, c=c&#8321;</text>\n'

    s += f'  <text x="395" y="490" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}" text-anchor="middle">Две стороны и угол</text>\n'
    s += f'  <text x="395" y="506" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}" text-anchor="middle">между ними одного</text>\n'
    s += f'  <text x="395" y="522" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}" text-anchor="middle">треугольника равны</text>\n'
    s += f'  <text x="395" y="538" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}" text-anchor="middle">соответствующим</text>\n'
    s += f'  <text x="395" y="558" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}" text-anchor="middle">элементам другого</text>\n'

    s += f'  <text x="645" y="490" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}" text-anchor="middle">Сторона и два</text>\n'
    s += f'  <text x="645" y="506" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}" text-anchor="middle">прилежащих угла</text>\n'
    s += f'  <text x="645" y="522" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}" text-anchor="middle">одного треугольника</text>\n'
    s += f'  <text x="645" y="538" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}" text-anchor="middle">равны соответствующим</text>\n'
    s += f'  <text x="645" y="558" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}" text-anchor="middle">элементам другого</text>\n'

    # Dividers
    s += f'  <line x1="270" y1="445" x2="270" y2="575" stroke="{C_PRIMARY}" stroke-width="1" opacity="0.2" />\n'
    s += f'  <line x1="515" y1="445" x2="515" y2="575" stroke="{C_PRIMARY}" stroke-width="1" opacity="0.2" />\n'

    s += svg_tail()
    return s


# ═══════════════════════════════════════════════════════════════════
# LESSON 6 — Признаки параллельности
# ═══════════════════════════════════════════════════════════════════
def lesson6() -> str:
    s = svg_head("Признаки параллельности", 6)
    # ── Big diagram: two parallel lines with transversal ──
    s += panel(20, 90, 760, 260, "Параллельные прямые и секущая")

    # Line a (top)
    s += f'  <line x1="50" y1="170" x2="450" y2="170" stroke="{C_PRIMARY}" stroke-width="2.5" />\n'
    # Line b (bottom)
    s += f'  <line x1="50" y1="300" x2="450" y2="300" stroke="{C_PRIMARY}" stroke-width="2.5" />\n'
    # Transversal c
    s += f'  <line x1="130" y1="130" x2="350" y2="340" stroke="{C_RED}" stroke-width="2" />\n'

    # Labels
    s += f'  <text x="455" y="167" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="{C_PRIMARY_DKR}">a</text>\n'
    s += f'  <text x="455" y="297" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="{C_PRIMARY_DKR}">b</text>\n'
    s += f'  <text x="355" y="345" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="{C_RED}">c (секущая)</text>\n'

    # Intersection points
    s += f'  <circle cx="210" cy="170" r="3" fill="{C_RED}" />\n'
    s += f'  <circle cx="285" cy="300" r="3" fill="{C_RED}" />\n'
    s += f'  <text x="215" y="163" font-family="Arial,sans-serif" font-size="11" fill="{C_RED}">E</text>\n'
    s += f'  <text x="290" y="295" font-family="Arial,sans-serif" font-size="11" fill="{C_RED}">F</text>\n'

    # Angle markers - Corresponding angles (1 and 5)
    s += f'  <path d="M 210,185 A 18,18 0 0,0 220,180" fill="none" stroke="{C_ACCENT}" stroke-width="2" />\n'
    s += f'  <path d="M 285,315 A 18,18 0 0,0 295,310" fill="none" stroke="{C_ACCENT}" stroke-width="2" />\n'
    s += f'  <text x="228" y="195" font-family="Arial,sans-serif" font-size="11" fill="{C_ACCENT}">1</text>\n'
    s += f'  <text x="300" y="325" font-family="Arial,sans-serif" font-size="11" fill="{C_ACCENT}">5</text>\n'

    # Angle 2 and 6 (other corresponding)
    s += f'  <path d="M 195,185 A 18,18 0 0,1 200,195" fill="none" stroke="{C_GREEN}" stroke-width="2" />\n'
    s += f'  <path d="M 270,315 A 18,18 0 0,1 275,325" fill="none" stroke="{C_GREEN}" stroke-width="2" />\n'
    s += f'  <text x="183" y="200" font-family="Arial,sans-serif" font-size="11" fill="{C_GREEN}">2</text>\n'
    s += f'  <text x="258" y="330" font-family="Arial,sans-serif" font-size="11" fill="{C_GREEN}">6</text>\n'

    # Angle 3 and 7 (alternate)
    s += f'  <path d="M 220,158 A 18,18 0 0,1 225,165" fill="none" stroke="{C_PURPLE}" stroke-width="2" />\n'
    s += f'  <path d="M 270,315 A 18,18 0 0,1 275,325" fill="none" stroke="{C_PURPLE}" stroke-width="2" />\n'
    s += f'  <text x="228" y="158" font-family="Arial,sans-serif" font-size="11" fill="{C_PURPLE}">3</text>\n'
    s += f'  <text x="258" y="330" font-family="Arial,sans-serif" font-size="11" fill="{C_PURPLE}">7</text>\n'

    # Angle 4 and 8
    s += f'  <text x="195" y="158" font-family="Arial,sans-serif" font-size="11" fill="{C_RED}">4</text>\n'
    s += f'  <text x="300" y="295" font-family="Arial,sans-serif" font-size="11" fill="{C_RED}">8</text>\n'

    # Right side: legend
    s += f'  <text x="490" y="140" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="{C_TEXT_DK}">Типы углов:</text>\n'
    # Corresponding
    s += f'  <rect x="490" y="152" width="14" height="14" fill="{C_ACCENT}" rx="2" />\n'
    s += f'  <text x="510" y="164" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}">Соответственные (∠1 и ∠5)</text>\n'
    # Alternate interior
    s += f'  <rect x="490" y="174" width="14" height="14" fill="{C_GREEN}" rx="2" />\n'
    s += f'  <text x="510" y="186" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}">Накрест лежащие (∠3 и ∠6)</text>\n'
    # Same-side
    s += f'  <rect x="490" y="196" width="14" height="14" fill="{C_PURPLE}" rx="2" />\n'
    s += f'  <text x="510" y="208" font-family="Arial,sans-serif" font-size="11" fill="{C_TEXT}">Односторонние (∠3 и ∠5)</text>\n'

    # Parallel arrows
    s += f'  <text x="60" y="168" font-family="Arial,sans-serif" font-size="14" fill="{C_PRIMARY}">&#x21DA;</text>\n'
    s += f'  <text x="60" y="298" font-family="Arial,sans-serif" font-size="14" fill="{C_PRIMARY}">&#x21DA;</text>\n'

    # ── Three criteria boxes ──
    s += formula_box(20, 365, 245, 95, [
        "Признак 1:",
        "Если соответственные",
        "углы равны, то прямые",
      "параллельны: ∠1=∠5 =&gt; a∥b",
    ], bg_color="#FFF7ED", border_color=C_ACCENT)
    s += formula_box(280, 365, 245, 95, [
        "Признак 2:",
        "Если накрест лежащие",
        "углы равны, то прямые",
      "параллельны: ∠3=∠6 =&gt; a∥b",
    ], bg_color="#F0FDF4", border_color=C_GREEN)
    s += formula_box(540, 365, 240, 95, [
        "Признак 3:",
        "Если сумма односторонних",
        "углов = 180°, то прямые",
      "параллельны: ∠3+∠5=180°",
    ], bg_color="#FDF4FF", border_color=C_PURPLE)

    # ── Bottom: converse ──
    s += panel(20, 475, 760, 110, "Свойства параллельных прямых (обратные)")
    s += f'''  <text x="32" y="510" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">Если a ∥ b, то:</text>
  <text x="32" y="530" font-family="Arial,sans-serif" font-size="12" fill="{C_ACCENT}">1) Соответственные углы равны: ∠1 = ∠5</text>
  <text x="32" y="548" font-family="Arial,sans-serif" font-size="12" fill="{C_GREEN}">2) Накрест лежащие углы равны: ∠3 = ∠6</text>
  <text x="400" y="530" font-family="Arial,sans-serif" font-size="12" fill="{C_PURPLE}">3) Сумма односторонних = 180°: ∠3 + ∠5 = 180°</text>
  <text x="400" y="548" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">4) Через точку вне прямой можно провести</text>
  <text x="400" y="566" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">   только одну прямую, параллельную данной</text>
'''
    # ── Axiom ──
    s += formula_box(20, 570, 760, 22, [
        "Аксиома параллельности (Евклид): через точку, не лежащую на прямой, проходит только одна прямая, параллельная данной.",
    ], bg_color="#FEF2F2", border_color=C_RED)

    s += svg_tail()
    return s


# ═══════════════════════════════════════════════════════════════════
# LESSON 7 — Сумма углов треугольника
# ═══════════════════════════════════════════════════════════════════
def lesson7() -> str:
    s = svg_head("Сумма углов треугольника", 7)

    # ── Main theorem ──
    s += formula_box(20, 90, 760, 55, [
        "Теорема: Сумма углов треугольника равна 180°",
        "∠A + ∠B + ∠C = 180°",
    ], bg_color="#FFF7ED", border_color=C_ACCENT)

    # ── Proof diagram ──
    s += panel(20, 160, 440, 220, "Доказательство")
    # Triangle
    s += f'  <polygon points="120,350 240,200 370,350" fill="none" stroke="{C_PRIMARY}" stroke-width="2.5" />\n'
    # Parallel line through B
    s += f'  <line x1="120" y1="200" x2="380" y2="200" stroke="{C_GREEN}" stroke-width="1.5" stroke-dasharray="8,4" />\n'
    s += f'  <text x="383" y="198" font-family="Arial,sans-serif" font-size="11" fill="{C_GREEN}">a ∥ AC</text>\n'
    # Angle arcs at A
    s += f'  <path d="M 140,340 A 22,22 0 0,1 150,320" fill="none" stroke="{C_ACCENT}" stroke-width="2" />\n'
    s += f'  <text x="153" y="325" font-family="Arial,sans-serif" font-size="12" fill="{C_ACCENT}">α</text>\n'
    # Angle arcs at B
    s += f'  <path d="M 225,218 A 22,22 0 0,0 210,210" fill="none" stroke="{C_RED}" stroke-width="2" />\n'
    s += f'  <path d="M 255,218 A 22,22 0 0,1 270,210" fill="none" stroke="{C_PURPLE}" stroke-width="2" />\n'
    s += f'  <text x="205" y="212" font-family="Arial,sans-serif" font-size="12" fill="{C_RED}">β</text>\n'
    s += f'  <text x="272" y="212" font-family="Arial,sans-serif" font-size="12" fill="{C_PURPLE}">γ</text>\n'
    # Angle arc at C
    s += f'  <path d="M 350,340 A 22,22 0 0,0 340,320" fill="none" stroke="{C_PRIMARY_LT}" stroke-width="2" />\n'
    s += f'  <text x="340" y="318" font-family="Arial,sans-serif" font-size="12" fill="{C_PRIMARY_LT}">α</text>\n'
    # Angle β on parallel line left
    s += f'  <path d="M 200,200 A 22,22 0 0,0 215,210" fill="none" stroke="{C_RED}" stroke-width="1.5" />\n'
    s += f'  <text x="192" y="203" font-family="Arial,sans-serif" font-size="11" fill="{C_RED}">β</text>\n'
    # Angle γ on parallel line right
    s += f'  <path d="M 275,200 A 22,22 0 0,1 260,210" fill="none" stroke="{C_PURPLE}" stroke-width="1.5" />\n'
    s += f'  <text x="277" y="203" font-family="Arial,sans-serif" font-size="11" fill="{C_PURPLE}">γ</text>\n'
    # Points
    s += point_label(120, 350, "A")
    s += point_label(240, 200, "B")
    s += point_label(370, 350, "C")
    # Explanation
    s += f'  <text x="32" y="378" font-family="Arial,sans-serif" font-size="10" fill="{C_TEXT}">α + β + γ = 180° (развёрнутый угол)</text>\n'

    # ── Right panel: examples ──
    s += panel(480, 160, 300, 220, "Примеры")
    # Example 1: 60-60-60
    s += f'  <text x="492" y="200" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="{C_PRIMARY_DKR}">Равносторонний:</text>\n'
    s += f'  <text x="492" y="218" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">60° + 60° + 60° = 180°</text>\n'
    # Example 2: 90-45-45
    s += f'  <text x="492" y="248" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="{C_PRIMARY_DKR}">Прямоугольный равнобедренный:</text>\n'
    s += f'  <text x="492" y="266" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">90° + 45° + 45° = 180°</text>\n'
    # Example 3: 90-30-60
    s += f'  <text x="492" y="296" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="{C_PRIMARY_DKR}">Прямоугольный (30°-60°-90°):</text>\n'
    s += f'  <text x="492" y="314" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">90° + 60° + 30° = 180°</text>\n'
    # Example 4
    s += f'  <text x="492" y="344" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="{C_PRIMARY_DKR}">Тупоугольный:</text>\n'
    s += f'  <text x="492" y="362" font-family="Arial,sans-serif" font-size="12" fill="{C_TEXT}">110° + 40° + 30° = 180°</text>\n'

    # ── Exterior angle theorem ──
    s += panel(20, 395, 440, 195, "Внешний угол треугольника")
    # Triangle with exterior angle
    s += f'  <polygon points="120,550 200,430 320,550" fill="none" stroke="{C_PRIMARY}" stroke-width="2.5" />\n'
    # Extend side BC
    s += f'  <line x1="200" y1="430" x2="400" y2="480" stroke="{C_PRIMARY}" stroke-width="1.5" stroke-dasharray="6,3" />\n'
    # Exterior angle arc
    s += f'  <path d="M 380,475 A 30,30 0 0,0 360,445" fill="none" stroke="{C_RED}" stroke-width="2.5" />\n'
    # Interior angles
    s += f'  <path d="M 137,540 A 18,18 0 0,1 145,522" fill="none" stroke="{C_ACCENT}" stroke-width="1.5" />\n'
    s += f'  <path d="M 303,540 A 18,18 0 0,0 295,522" fill="none" stroke="{C_GREEN}" stroke-width="1.5" />\n'
    # Labels
    s += point_label(120, 550, "A")
    s += point_label(200, 430, "B")
    s += point_label(320, 550, "C")
    s += f'  <text x="142" y="524" font-family="Arial,sans-serif" font-size="12" fill="{C_ACCENT}">∠A</text>\n'
    s += f'  <text x="283" y="520" font-family="Arial,sans-serif" font-size="12" fill="{C_GREEN}">∠C</text>\n'
    s += f'  <text x="370" y="460" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="{C_RED}">∠BCD</text>\n'

    # ── Right: theorem text ──
    s += formula_box(480, 395, 300, 90, [
        "Внешний угол равен сумме",
        "двух внутренних углов,",
        "не смежных с ним:",
        "∠BCD = ∠A + ∠C",
    ], bg_color="#FEF2F2", border_color=C_RED)

    # Corollaries
    s += formula_box(480, 500, 300, 90, [
        "Следствия:",
        "1. Внешний угол &gt; каждого",
        "   внутреннего, не смежного с ним",
        "2. В прямоугольном △ сумма",
        "   острых углов = 90°",
    ], bg_color="#F0FDF4", border_color=C_GREEN)

    s += svg_tail()
    return s


# ═══════════════════════════════════════════════════════════════════
# MAIN — write all 7 files
# ═══════════════════════════════════════════════════════════════════
generators = [lesson1, lesson2, lesson3, lesson4, lesson5, lesson6, lesson7]

for i, gen in enumerate(generators, 1):
    path = os.path.join(BASE_DIR, f"lesson-{i}.svg")
    content = gen()
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Written {path}  ({len(content)} bytes)")

print("\n✅ All 7 SVG files generated.")
