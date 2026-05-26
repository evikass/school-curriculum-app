#!/usr/bin/env python3
"""Generate 6 detailed SVG files for Grade 7 Physical Education (Физкультура) lessons.

Each SVG: 800x600, educational content, Russian text,
green (#22C55E) / red (#EF4444) color scheme, sport diagrams.
"""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/pe"

# ── Color scheme ──────────────────────────────────────────────
PRIMARY      = "#22C55E"
PRIMARY_DARK = "#16A34A"
PRIMARY_LIGHT= "#86EFAC"
ACCENT       = "#EF4444"
ACCENT_DARK  = "#DC2626"
ACCENT_LIGHT = "#FCA5A5"
BG           = "#F0FDF4"
BG_CARD      = "#FFFFFF"
TEXT_DARK    = "#14532D"
TEXT_MED     = "#166534"
TEXT_LIGHT   = "#6B7280"
BORDER       = "#22C55E"
HIGHLIGHT_BG = "#DCFCE7"
HIGHLIGHT_BD = "#BBF7D0"
FOOTER_BG    = "#16A34A"
HEADER_BG    = "#14532D"


# ── XML escape ────────────────────────────────────────────────
def esc(text: str) -> str:
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;"))


# ── Shared SVG boilerplate ────────────────────────────────────
def svg_head(title: str, lesson_num: int) -> list[str]:
    """Return the top part of the SVG (up to the start of body content)."""
    L = []
    L.append('<?xml version="1.0" encoding="UTF-8"?>')
    L.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">')
    # ── defs ──
    L.append('  <defs>')
    L.append(f'    <linearGradient id="hdrGrad" x1="0%" y1="0%" x2="100%" y2="0%">')
    L.append(f'      <stop offset="0%" style="stop-color:{HEADER_BG};stop-opacity:1"/>')
    L.append(f'      <stop offset="100%" style="stop-color:{PRIMARY_DARK};stop-opacity:1"/>')
    L.append(f'    </linearGradient>')
    L.append(f'    <linearGradient id="ftrGrad" x1="0%" y1="0%" x2="100%" y2="0%">')
    L.append(f'      <stop offset="0%" style="stop-color:{PRIMARY_DARK};stop-opacity:1"/>')
    L.append(f'      <stop offset="100%" style="stop-color:{HEADER_BG};stop-opacity:1"/>')
    L.append(f'    </linearGradient>')
    L.append(f'    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">')
    L.append(f'      <stop offset="0%" style="stop-color:{BG_CARD};stop-opacity:1"/>')
    L.append(f'      <stop offset="100%" style="stop-color:{HIGHLIGHT_BG};stop-opacity:1"/>')
    L.append(f'    </linearGradient>')
    L.append(f'    <filter id="shadow" x="-2%" y="-2%" width="104%" height="104%">')
    L.append(f'      <feDropShadow dx="1" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.08"/>')
    L.append(f'    </filter>')
    L.append('  </defs>')
    # ── background ──
    L.append(f'  <rect x="0" y="0" width="800" height="600" rx="14" ry="14" fill="{BG}" stroke="{BORDER}" stroke-width="2"/>')
    # ── header ──
    L.append(f'  <rect x="0" y="0" width="800" height="62" rx="14" ry="14" fill="url(#hdrGrad)"/>')
    L.append(f'  <rect x="0" y="36" width="800" height="26" fill="url(#hdrGrad)"/>')
    # badge
    L.append(f'  <rect x="16" y="12" width="38" height="38" rx="8" fill="{ACCENT}" opacity="0.9"/>')
    L.append(f'  <text x="35" y="38" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#FFF">{lesson_num}</text>')
    # title
    L.append(f'  <text x="68" y="34" font-family="Arial,sans-serif" font-size="17" font-weight="bold" fill="#FFF">{esc(title)}</text>')
    L.append(f'  <text x="68" y="52" font-family="Arial,sans-serif" font-size="11" fill="{PRIMARY_LIGHT}">Физкультура — 7 класс — Урок {lesson_num}</text>')
    # separator
    L.append(f'  <line x1="20" y1="64" x2="780" y2="64" stroke="{PRIMARY_LIGHT}" stroke-width="1" opacity="0.5"/>')
    return L


def svg_foot() -> list[str]:
    """Return the footer part of the SVG."""
    L = []
    L.append(f'  <rect x="0" y="572" width="800" height="28" rx="0" fill="url(#ftrGrad)"/>')
    L.append(f'  <rect x="0" y="586" width="800" height="14" rx="14" fill="url(#ftrGrad)"/>')
    L.append(f'  <rect x="0" y="572" width="800" height="14" fill="url(#ftrGrad)"/>')
    L.append(f'  <text x="400" y="590" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#FFF">Физкультура · 7 класс</text>')
    L.append('</svg>')
    return L


# ── Helper: draw info card ────────────────────────────────────
def card(x, y, w, h, title, items, title_color=PRIMARY):
    """Return SVG lines for a rounded card with title bar and bullet items."""
    L = []
    # shadow + bg
    L.append(f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" ry="8" fill="url(#cardGrad)" stroke="{HIGHLIGHT_BD}" stroke-width="1" filter="url(#shadow)"/>')
    # title bar
    L.append(f'  <rect x="{x}" y="{y}" width="{w}" height="26" rx="8" ry="8" fill="{title_color}" opacity="0.88"/>')
    L.append(f'  <rect x="{x}" y="{y+14}" width="{w}" height="12" fill="{title_color}" opacity="0.88"/>')
    L.append(f'  <text x="{x + w//2}" y="{y+18}" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#FFF">{esc(title)}</text>')
    # items
    iy = y + 40
    for item in items:
        L.append(f'  <text x="{x+10}" y="{iy}" font-family="Arial,sans-serif" font-size="10.5" fill="{TEXT_MED}">{esc(item)}</text>')
        iy += 15
    return L


def icon_dot(cx, cy, r=3, color=PRIMARY):
    return f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" opacity="0.6"/>'


# ── Stick-figure helpers ──────────────────────────────────────
def stick_runner(x, y, scale=1.0, color=PRIMARY_DARK, opacity=0.7):
    """Running stick figure at (x,y) top-of-head."""
    s = scale
    L = []
    L.append(f'  <g transform="translate({x},{y}) scale({s})" opacity="{opacity}">')
    L.append(f'    <circle cx="0" cy="6" r="6" fill="none" stroke="{color}" stroke-width="2"/>')
    # body leaning forward
    L.append(f'    <line x1="0" y1="12" x2="4" y2="32" stroke="{color}" stroke-width="2.5"/>')
    # legs in running pose
    L.append(f'    <line x1="4" y1="32" x2="-8" y2="46" stroke="{color}" stroke-width="2.5"/>')
    L.append(f'    <line x1="4" y1="32" x2="16" y2="44" stroke="{color}" stroke-width="2.5"/>')
    # arms
    L.append(f'    <line x1="1" y1="18" x2="-10" y2="28" stroke="{color}" stroke-width="2"/>')
    L.append(f'    <line x1="1" y1="18" x2="12" y2="24" stroke="{color}" stroke-width="2"/>')
    L.append(f'  </g>')
    return L


def stick_standing(x, y, scale=1.0, color=PRIMARY_DARK, opacity=0.7):
    """Standing stick figure at (x,y) top-of-head."""
    s = scale
    L = []
    L.append(f'  <g transform="translate({x},{y}) scale({s})" opacity="{opacity}">')
    L.append(f'    <circle cx="0" cy="6" r="6" fill="none" stroke="{color}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="12" x2="0" y2="34" stroke="{color}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="34" x2="-8" y2="48" stroke="{color}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="34" x2="8" y2="48" stroke="{color}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="18" x2="-10" y2="30" stroke="{color}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="18" x2="10" y2="30" stroke="{color}" stroke-width="2"/>')
    L.append(f'  </g>')
    return L


# ══════════════════════════════════════════════════════════════
# LESSON 1 — Развитие выносливости
# ══════════════════════════════════════════════════════════════
def lesson1() -> str:
    L = svg_head("Развитие выносливости", 1)

    # Row 1 cards
    L += card(16, 72, 245, 145, "Виды выносливости", [
        "• Общая — длительная работа",
        "• Специальная — вид спорта",
        "• Скоростная — темп + время",
        "• Силовая — мышцы + время",
        "• Координационная — точность",
    ])
    L += card(271, 72, 245, 145, "Методы тренировки", [
        "• Равномерный — постоянный темп",
        "• Переменный — смена скорости",
        "• Интервальный — работа + отдых",
        "• Повторный — несколько серий",
        "• Круговой — станции упражнений",
    ])
    L += card(526, 72, 258, 145, "Пульсовые зоны", [
        "• Зона здоровья: 50–60% ЧСС макс",
        "• Аэробная: 60–75% ЧСС макс",
        "• Анаэробная: 75–90% ЧСС макс",
        "• Максимальная: 90–100%",
        "• Формула: 220 – возраст",
    ])

    # Row 2 cards
    L += card(16, 227, 245, 135, "Упражнения на выносливость", [
        "• Бег в медленном темпе 10–20 мин",
        "• Плавание 400–800 м",
        "• Прыжки со скакалкой 3–5 мин",
        "• Велосипед 15–30 мин",
    ])
    L += card(271, 227, 245, 135, "Принципы развития", [
        "• Постепенность — +10% в неделю",
        "• Регулярность — 3–4 раза/нед.",
        "• Разнообразие нагрузок",
        "• Чередование работы и отдыха",
    ])
    L += card(526, 227, 258, 135, "Тесты выносливости", [
        "• Бег 1000 м (девушки)",
        "• Бег 1500 м (юноши)",
        "• Бег 2000 м (ГТО)",
        "• Купер-тест: 12 мин бег",
    ])

    # ── Diagram: heart rate zones bar chart ──
    L.append(f'  <rect x="16" y="372" width="768" height="192" rx="8" fill="{BG_CARD}" stroke="{HIGHLIGHT_BD}" stroke-width="1" filter="url(#shadow)"/>')
    L.append(f'  <text x="400" y="392" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="{TEXT_DARK}">Пульсовые зоны и тренировочные эффекты</text>')

    zones = [
        ("Здоровье", "50-60%", 0.35, "#86EFAC"),
        ("Аэробная", "60-75%", 0.55, "#22C55E"),
        ("Анаэробная", "75-90%", 0.78, "#FBBF24"),
        ("Максимальная", "90-100%", 1.0, "#EF4444"),
    ]
    bar_base_y = 540
    bar_max_h = 120
    bar_w = 100
    start_x = 80
    for i, (name, pct, frac, clr) in enumerate(zones):
        bx = start_x + i * 180
        bh = int(bar_max_h * frac)
        by = bar_base_y - bh
        L.append(f'  <rect x="{bx}" y="{by}" width="{bar_w}" height="{bh}" rx="4" fill="{clr}" opacity="0.8"/>')
        L.append(f'  <text x="{bx+bar_w//2}" y="{by-6}" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="{TEXT_DARK}">{esc(name)}</text>')
        L.append(f'  <text x="{bx+bar_w//2}" y="{bar_base_y+14}" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="{TEXT_LIGHT}">{esc(pct)}</text>')

    # Effects labels
    effects = ["Восст.", "Жиросжиг.", "Вынослив.", "Скорость"]
    for i, ef in enumerate(effects):
        bx = start_x + i * 180
        L.append(f'  <text x="{bx+bar_w//2}" y="{bar_base_y+26}" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="{ACCENT_DARK}">{esc(ef)}</text>')

    # Runner icons
    L += stick_runner(60, 410, 0.6)
    L += stick_runner(720, 430, 0.55, ACCENT)

    L += svg_foot()
    return "\n".join(L)


# ══════════════════════════════════════════════════════════════
# LESSON 2 — Развитие силы и быстроты
# ══════════════════════════════════════════════════════════════
def lesson2() -> str:
    L = svg_head("Развитие силы и быстроты", 2)

    # Row 1
    L += card(16, 72, 245, 135, "Развитие силы", [
        "• Собственная масса (отжимания)",
        "• Отягощение 60–80% от макс.",
        "• 6–12 повторений, 3–4 подхода",
        "• Отдых между подходами 2–3 мин",
    ])
    L += card(271, 72, 245, 135, "Развитие быстроты", [
        "• Скорость реакции (старты)",
        "• Скорость одиночного движения",
        "• Частота движений (темп)",
        "• Интервалы: 5–30 сек макс.",
    ])
    L += card(526, 72, 258, 135, "Упражнения на силу", [
        "• Отжимания: 10–25 раз",
        "• Подтягивания: 5–15 раз",
        "• Приседания: 20–40 раз",
        "• Планка: 30–90 сек",
    ])

    # Row 2
    L += card(16, 217, 245, 135, "Упражнения на быстроту", [
        "• Челночный бег 3×10 м",
        "• Бег 30 м с ходу",
        "• Прыжки на месте 10 сек",
        "• Броски мяча в стену 20 сек",
    ])
    L += card(271, 217, 245, 135, "Принципы тренировки", [
        "• Сверхнагрузка — больше обычного",
        "• Прогрессия — рост нагрузки",
        "• Специфичность — цель тренировки",
        "• Обратимость — без тренир. слабеем",
    ])
    L += card(526, 217, 258, 135, "Правила безопасности", [
        "• Разминка перед тренировкой",
        "• Правильная техника упражнений",
        "• Страховка при работе с весом",
        "• Растяжка после нагрузки",
    ])

    # ── Diagram: strength vs speed curve ──
    L.append(f'  <rect x="16" y="362" width="768" height="202" rx="8" fill="{BG_CARD}" stroke="{HIGHLIGHT_BD}" stroke-width="1" filter="url(#shadow)"/>')
    L.append(f'  <text x="400" y="384" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="{TEXT_DARK}">Зависимость силы и быстроты от тренировочной нагрузки</text>')

    # Axes
    ax, ay = 80, 540
    L.append(f'  <line x1="{ax}" y1="{ay}" x2="{ax+650}" y2="{ay}" stroke="{TEXT_LIGHT}" stroke-width="1.5"/>')
    L.append(f'  <line x1="{ax}" y1="{ay}" x2="{ax}" y2="{ay-140}" stroke="{TEXT_LIGHT}" stroke-width="1.5"/>')
    L.append(f'  <text x="{ax-8}" y="{ay-140}" text-anchor="end" font-family="Arial,sans-serif" font-size="9" fill="{TEXT_LIGHT}">%</text>')
    L.append(f'  <text x="{ax+650}" y="{ay+14}" text-anchor="end" font-family="Arial,sans-serif" font-size="9" fill="{TEXT_LIGHT}">Нагрузка</text>')

    # Strength curve (green)
    pts_s = []
    for i in range(14):
        px = ax + 20 + i * 44
        frac = 1 - ((i - 6)**2) / 50
        if frac < 0.05: frac = 0.05
        py = ay - int(frac * 130)
        pts_s.append(f"{px},{py}")
    L.append(f'  <polyline points="{" ".join(pts_s)}" fill="none" stroke="{PRIMARY}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>')
    L.append(f'  <text x="{ax+310}" y="{ay-125}" font-family="Arial,sans-serif" font-size="10" fill="{PRIMARY}" font-weight="bold">Сила</text>')

    # Speed curve (red)
    pts_v = []
    for i in range(14):
        px = ax + 20 + i * 44
        frac = 0.9 * (1 - ((i - 3)**2) / 30)
        if frac < 0.05: frac = 0.05
        if i > 9: frac = max(0.05, frac - (i-9)*0.05)
        py = ay - int(frac * 120)
        pts_v.append(f"{px},{py}")
    L.append(f'  <polyline points="{" ".join(pts_v)}" fill="none" stroke="{ACCENT}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="6,3"/>')
    L.append(f'  <text x="{ax+170}" y="{ay-105}" font-family="Arial,sans-serif" font-size="10" fill="{ACCENT}" font-weight="bold">Быстрота</text>')

    # Dumbbell icon
    L.append(f'  <g transform="translate(680,400) scale(0.7)" opacity="0.25">')
    L.append(f'    <rect x="0" y="5" width="8" height="16" rx="2" fill="{PRIMARY_DARK}"/>')
    L.append(f'    <rect x="32" y="5" width="8" height="16" rx="2" fill="{PRIMARY_DARK}"/>')
    L.append(f'    <line x1="8" y1="13" x2="32" y2="13" stroke="{PRIMARY_DARK}" stroke-width="4"/>')
    L.append(f'  </g>')

    L += svg_foot()
    return "\n".join(L)


# ══════════════════════════════════════════════════════════════
# LESSON 3 — Баскетбол: техника и тактика
# ══════════════════════════════════════════════════════════════
def lesson3() -> str:
    L = svg_head("Баскетбол: техника и тактика", 3)

    # Row 1
    L += card(16, 72, 245, 135, "Ведение мяча (дриблинг)", [
        "• Пальцы, не ладонь!",
        "• Высота отскока: до пояса",
        "• Взгляд — вперёд, не на мяч",
        "• Смена рук при ведении",
    ])
    L += card(271, 72, 245, 135, "Передачи и броски", [
        "• Передача двумя от груди",
        "• Передача одной (баскетбол.)",
        "• Бросок «в прыжке»",
        "• Бросок «с крюка» (полукрюк)",
    ])
    L += card(526, 72, 258, 135, "Правила баскетбола", [
        "• 5 игроков на площадке",
        "• 4 четверти по 10 мин (ФИБА)",
        "• 3-очковый: 6.75 м от кольца",
        "• 5 фолов — удаление игрока",
    ])

    # Row 2
    L += card(16, 217, 245, 125, "Позиции игроков", [
        "• Разыгрывающий (1) — плеймейкер",
        "• Атакующий защитник (2)",
        "• Лёгкий форвард (3)",
        "• Тяжёлый форвард (4)",
    ])
    L += card(271, 217, 245, 125, "Центровой (5)", [
        "• Игра спиной к кольцу",
        "• Подбор на щите",
        "• Блокирование бросков",
        "• Позиция под кольцом",
    ])
    L += card(526, 217, 258, 125, "Тактика", [
        "• Нападение: заслон, отрыв",
        "• Защита: личная / зонная",
        "• Прессинг по всей площадке",
        "• Быстрый прорыв (fast break)",
    ])

    # ── Diagram: basketball half-court with positions ──
    L.append(f'  <rect x="16" y="352" width="390" height="212" rx="8" fill="{BG_CARD}" stroke="{HIGHLIGHT_BD}" stroke-width="1" filter="url(#shadow)"/>')
    L.append(f'  <text x="211" y="372" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="{TEXT_DARK}">Расстановка игроков (нападение)</text>')

    # Half-court outline
    cx, cy = 211, 475
    # key/paint area
    L.append(f'  <rect x="{cx-60}" y="{cy-70}" width="120" height="100" fill="none" stroke="{PRIMARY_DARK}" stroke-width="1.5" rx="2"/>')
    # free-throw circle
    L.append(f'  <circle cx="{cx}" cy="{cy-70}" r="40" fill="none" stroke="{PRIMARY_DARK}" stroke-width="1" stroke-dasharray="4,3"/>')
    # 3-point arc
    L.append(f'  <path d="M{cx-110},{cy+30} A130,130 0 0,1 {cx+110},{cy+30}" fill="none" stroke="{ACCENT}" stroke-width="1.5"/>')
    # basket
    L.append(f'  <circle cx="{cx}" cy="{cy-40}" r="8" fill="none" stroke="{ACCENT_DARK}" stroke-width="2"/>')
    # backboard
    L.append(f'  <line x1="{cx-15}" y1="{cy-60}" x2="{cx+15}" y2="{cy-60}" stroke="{TEXT_LIGHT}" stroke-width="2.5"/>')

    # Player positions (5 dots + labels)
    positions = [
        (cx, cy-85, "1", PRIMARY),       # PG
        (cx-70, cy-55, "2", PRIMARY),    # SG
        (cx+70, cy-55, "3", PRIMARY),    # SF
        (cx-45, cy-20, "4", ACCENT),     # PF
        (cx, cy+5, "5", ACCENT),         # C
    ]
    for px, py, lbl, clr in positions:
        L.append(f'  <circle cx="{px}" cy="{py}" r="11" fill="{clr}" opacity="0.85"/>')
        L.append(f'  <text x="{px}" y="{py+4}" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#FFF">{lbl}</text>')

    # ── Diagram: dribble technique ──
    L.append(f'  <rect x="416" y="352" width="368" height="212" rx="8" fill="{BG_CARD}" stroke="{HIGHLIGHT_BD}" stroke-width="1" filter="url(#shadow)"/>')
    L.append(f'  <text x="600" y="372" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="{TEXT_DARK}">Техника ведения мяча</text>')

    # Hand position diagram
    L.append(f'  <circle cx="520" cy="430" r="28" fill="none" stroke="{PRIMARY}" stroke-width="2"/>')
    L.append(f'  <circle cx="520" cy="430" r="5" fill="{ACCENT}" opacity="0.5"/>')
    L.append(f'  <text x="520" y="468" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="{TEXT_MED}">Мяч</text>')
    # Fingers
    for angle_deg in [-40, -15, 15, 40, 70]:
        import math
        rad = math.radians(angle_deg - 90)
        fx1 = 520 + 28 * math.cos(rad)
        fy1 = 430 + 28 * math.sin(rad)
        fx2 = 520 + 42 * math.cos(rad)
        fy2 = 430 + 42 * math.sin(rad)
        L.append(f'  <line x1="{fx1:.0f}" y1="{fy1:.0f}" x2="{fx2:.0f}" y2="{fy2:.0f}" stroke="{PRIMARY_DARK}" stroke-width="2" stroke-linecap="round"/>')
    L.append(f'  <text x="520" y="490" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="{ACCENT_DARK}">Контроль пальцами!</text>')

    # Bounce trajectory
    L.append(f'  <path d="M580,420 Q600,480 620,420 Q640,480 660,420 Q680,480 700,420" fill="none" stroke="{PRIMARY}" stroke-width="1.5" stroke-dasharray="4,2"/>')
    L.append(f'  <circle cx="600" cy="470" r="7" fill="{ACCENT}" opacity="0.4"/>')
    L.append(f'  <circle cx="640" cy="470" r="7" fill="{ACCENT}" opacity="0.4"/>')
    L.append(f'  <circle cx="680" cy="470" r="7" fill="{ACCENT}" opacity="0.4"/>')
    L.append(f'  <text x="640" y="500" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="{TEXT_LIGHT}">Траектория отскока</text>')

    # Height reference line
    L.append(f'  <line x1="570" y1="420" x2="720" y2="420" stroke="{PRIMARY_LIGHT}" stroke-width="1" stroke-dasharray="2,4"/>')
    L.append(f'  <text x="720" y="416" text-anchor="end" font-family="Arial,sans-serif" font-size="8" fill="{PRIMARY}">до пояса</text>')

    L += svg_foot()
    return "\n".join(L)


# ══════════════════════════════════════════════════════════════
# LESSON 4 — Волейбол: техника и тактика
# ══════════════════════════════════════════════════════════════
def lesson4() -> str:
    L = svg_head("Волейбол: техника и тактика", 4)

    # Row 1
    L += card(16, 72, 245, 135, "Подача мяча", [
        "• Нижняя прямая подача",
        "• Верхняя прямая подача",
        "• Подача в прыжке (силовая)",
        "• Цель: слабый принимающий",
    ])
    L += card(271, 72, 245, 135, "Приём и передача", [
        "• Нижний приём — двумя руками",
        "• Верхняя передача — пальцы",
        "• Площадка рук «замок» снизу",
        "• Ноги согнуты, вес на стопах",
    ])
    L += card(526, 72, 258, 135, "Нападающий удар", [
        "• Разбег: 3 шага",
        "• Отталкивание двумя ногами",
        "• Мах обеими руками вверх",
        "• Удар ладонью по мячу сверху",
    ])

    # Row 2
    L += card(16, 217, 245, 125, "Блокирование", [
        "• Одиночный и групповой блок",
        "• Руки вынесены над сеткой",
        "• Пальцы разведены широко",
        "• Перенос веса на пальцы",
    ])
    L += card(271, 217, 245, 125, "Позиции (6 игроков)", [
        "• 1 — правый защитник",
        "• 2 — правый нападающий",
        "• 3 — центр. нападающий",
        "• 4 — левый нападающий",
    ])
    L += card(526, 217, 258, 125, "Правила волейбола", [
        "• 5 партий до 25 очков",
        "• 3 касания на свою сторону",
        "• Переход по часовой стрелке",
        "• Либеро — только защита",
    ])

    # ── Diagram: volleyball court with positions ──
    L.append(f'  <rect x="16" y="352" width="385" height="212" rx="8" fill="{BG_CARD}" stroke="{HIGHLIGHT_BD}" stroke-width="1" filter="url(#shadow)"/>')
    L.append(f'  <text x="208" y="372" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="{TEXT_DARK}">Расстановка 6 игроков</text>')

    # Court
    court_x, court_y = 60, 390
    court_w, court_h = 296, 150
    L.append(f'  <rect x="{court_x}" y="{court_y}" width="{court_w}" height="{court_h}" fill="#FEF3C7" stroke="{PRIMARY_DARK}" stroke-width="1.5" rx="3"/>')
    # Net line
    net_y = court_y + court_h // 2
    L.append(f'  <line x1="{court_x}" y1="{net_y}" x2="{court_x+court_w}" y2="{net_y}" stroke="{ACCENT}" stroke-width="3"/>')
    L.append(f'  <text x="{court_x + court_w//2}" y="{net_y+4}" text-anchor="middle" font-family="Arial,sans-serif" font-size="7" fill="#FFF" font-weight="bold">СЕТКА</text>')

    # 6 player positions (front row: 2,3,4; back row: 1,6,5)
    front_y = net_y - 25
    back_y = net_y + 30
    vpositions = [
        (court_x + 50,  front_y, "4", PRIMARY),
        (court_x + 148, front_y, "3", PRIMARY),
        (court_x + 246, front_y, "2", PRIMARY),
        (court_x + 50,  back_y,  "5", ACCENT),
        (court_x + 148, back_y,  "6", ACCENT),
        (court_x + 246, back_y,  "1", ACCENT),
    ]
    for px, py, lbl, clr in vpositions:
        L.append(f'  <circle cx="{px}" cy="{py}" r="12" fill="{clr}" opacity="0.85"/>')
        L.append(f'  <text x="{px}" y="{py+4}" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#FFF">{lbl}</text>')

    # Labels
    L.append(f'  <text x="{court_x + court_w//2}" y="{front_y - 18}" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="{PRIMARY_DARK}">Передняя линия</text>')
    L.append(f'  <text x="{court_x + court_w//2}" y="{back_y + 28}" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="{ACCENT_DARK}">Задняя линия</text>')

    # ── Diagram: serve technique ──
    L.append(f'  <rect x="411" y="352" width="373" height="212" rx="8" fill="{BG_CARD}" stroke="{HIGHLIGHT_BD}" stroke-width="1" filter="url(#shadow)"/>')
    L.append(f'  <text x="597" y="372" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="{TEXT_DARK}">Верхняя прямая подача</text>')

    # Serve sequence 1-2-3
    # Phase 1: toss
    L.append(f'  <g transform="translate(470,400) scale(0.55)" opacity="0.7">')
    L.append(f'    <circle cx="0" cy="6" r="6" fill="none" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="12" x2="0" y2="34" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="34" x2="-8" y2="48" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="34" x2="8" y2="48" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="18" x2="-12" y2="8" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="18" x2="12" y2="28" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    L.append(f'  </g>')
    L.append(f'  <circle cx="466" cy="388" r="6" fill="{ACCENT}" opacity="0.6"/>')
    L.append(f'  <text x="480" y="442" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="{TEXT_MED}">1. Бросок</text>')

    # Phase 2: swing
    L.append(f'  <g transform="translate(580,400) scale(0.55)" opacity="0.7">')
    L.append(f'    <circle cx="0" cy="6" r="6" fill="none" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="12" x2="0" y2="34" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="34" x2="-8" y2="48" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="34" x2="8" y2="48" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="18" x2="-14" y2="4" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="18" x2="14" y2="28" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    L.append(f'  </g>')
    L.append(f'  <circle cx="590" cy="378" r="6" fill="{ACCENT}" opacity="0.6"/>')
    L.append(f'  <text x="590" y="442" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="{TEXT_MED}">2. Замах</text>')

    # Phase 3: hit
    L.append(f'  <g transform="translate(700,400) scale(0.55)" opacity="0.7">')
    L.append(f'    <circle cx="0" cy="6" r="6" fill="none" stroke="{ACCENT_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="12" x2="0" y2="34" stroke="{ACCENT_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="34" x2="-8" y2="48" stroke="{ACCENT_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="34" x2="8" y2="48" stroke="{ACCENT_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="18" x2="-12" y2="28" stroke="{ACCENT_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="18" x2="14" y2="2" stroke="{ACCENT_DARK}" stroke-width="2.5"/>')
    L.append(f'  </g>')
    L.append(f'  <circle cx="714" cy="370" r="6" fill="{ACCENT}" opacity="0.8"/>')
    # Arrow
    L.append(f'  <line x1="714" y1="370" x2="730" y2="355" stroke="{ACCENT}" stroke-width="1.5"/>')
    L.append(f'  <text x="710" y="442" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="{ACCENT_DARK}">3. Удар!</text>')

    # Arrow between phases
    L.append(f'  <path d="M510,415 L550,415" fill="none" stroke="{TEXT_LIGHT}" stroke-width="1.5" marker-end="url(#arrow)"/>')
    L.append(f'  <path d="M630,415 L665,415" fill="none" stroke="{TEXT_LIGHT}" stroke-width="1.5"/>')
    L.append(f'  <polygon points="665,411 675,415 665,419" fill="{TEXT_LIGHT}"/>')

    # Ball path
    L.append(f'  <path d="M730,355 Q750,340 760,330" fill="none" stroke="{ACCENT}" stroke-width="1" stroke-dasharray="3,2"/>')

    L += svg_foot()
    return "\n".join(L)


# ══════════════════════════════════════════════════════════════
# LESSON 5 — Акробатические упражнения
# ══════════════════════════════════════════════════════════════
def lesson5() -> str:
    L = svg_head("Акробатические упражнения", 5)

    # Row 1
    L += card(16, 72, 245, 145, "Кувырки", [
        "• Кувырок вперёд — группировка",
        "• Кувырок назад — толчок руками",
        "• Длинный кувырок — через прыжок",
        "• Перекат в сторону — на спине",
        "• Стойка на лопатках — упор",
    ], title_color=PRIMARY)
    L += card(271, 72, 245, 145, "Стойки и равновесие", [
        "• Стойка на руках (у стены)",
        "• Стойка на голове",
        "• Мост из положения лёжа",
        "• «Ласточка» — равновесие",
        "• Шпагат продольный/поперечный",
    ], title_color=PRIMARY)
    L += card(526, 72, 258, 145, "Техника безопасности", [
        "• Мат обязателен под телом!",
        "• Страховка партнёром всегда",
        "• Разминка перед акробатикой",
        "• Снять украшения и часы",
        "• Не выполнять без разрешения",
    ], title_color=ACCENT)

    # Row 2
    L += card(16, 227, 245, 125, "Связки элементов", [
        "• Кувырок → стойка → мост",
        "• Два кувырка вперёд подряд",
        "• Кувырок → «ласточка»",
        "• Комбинация из 4–5 элементов",
    ])
    L += card(271, 227, 245, 125, "Группировка", [
        "• Колени к груди, обхват руками",
        "• Подбородок прижат к груди",
        "• Спина округлена (дуга)",
        "• Основа всех кувырков!",
    ])
    L += card(526, 227, 258, 125, "Оценивание (ГТО)", [
        "• Кувырок вперёд: 5 сек",
        "• Стойка на лопатках: 10 сек",
        "• Мост: фиксация 3 сек",
        "• Комбинация из 4 элементов",
    ])

    # ── Diagram: forward roll sequence ──
    L.append(f'  <rect x="16" y="362" width="768" height="202" rx="8" fill="{BG_CARD}" stroke="{HIGHLIGHT_BD}" stroke-width="1" filter="url(#shadow)"/>')
    L.append(f'  <text x="400" y="384" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="{TEXT_DARK}">Кувырок вперёд: последовательность фаз</text>')

    # Phase 1: Starting position
    L.append(f'  <g transform="translate(80,420) scale(0.6)" opacity="0.75">')
    L.append(f'    <circle cx="0" cy="6" r="6" fill="none" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="12" x2="0" y2="34" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="34" x2="-8" y2="48" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="34" x2="8" y2="48" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="18" x2="-12" y2="32" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="18" x2="12" y2="32" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    L.append(f'  </g>')
    L.append(f'  <text x="80" y="470" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="{PRIMARY_DARK}">1. Исходное</text>')
    L.append(f'  <text x="80" y="482" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="{TEXT_LIGHT}">Полуприсед</text>')

    # Arrow 1
    L.append(f'  <line x1="120" y1="445" x2="165" y2="445" stroke="{TEXT_LIGHT}" stroke-width="1.5"/>')
    L.append(f'  <polygon points="165,441 175,445 165,449" fill="{TEXT_LIGHT}"/>')

    # Phase 2: Tuck / group
    L.append(f'  <g transform="translate(200,430) scale(0.6)" opacity="0.75">')
    L.append(f'    <circle cx="0" cy="20" r="6" fill="none" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    # tucked body
    L.append(f'    <path d="M0,26 Q0,40 -8,50 Q-14,55 -8,60" fill="none" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <path d="M0,26 Q0,40 8,50 Q14,55 8,60" fill="none" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="32" x2="-10" y2="44" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="32" x2="10" y2="44" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    L.append(f'  </g>')
    L.append(f'  <text x="200" y="470" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="{PRIMARY_DARK}">2. Группировка</text>')
    L.append(f'  <text x="200" y="482" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="{TEXT_LIGHT}">Колени к груди</text>')

    # Arrow 2
    L.append(f'  <line x1="240" y1="445" x2="285" y2="445" stroke="{TEXT_LIGHT}" stroke-width="1.5"/>')
    L.append(f'  <polygon points="285,441 295,445 285,449" fill="{TEXT_LIGHT}"/>')

    # Phase 3: Rolling on back
    L.append(f'  <ellipse cx="330" cy="455" rx="18" ry="12" fill="none" stroke="{PRIMARY_DARK}" stroke-width="2" opacity="0.75"/>')
    L.append(f'  <circle cx="316" cy="445" r="5" fill="none" stroke="{PRIMARY_DARK}" stroke-width="1.5" opacity="0.75"/>')
    L.append(f'  <path d="M335,445 Q340,435 330,430" fill="none" stroke="{PRIMARY}" stroke-width="1" stroke-dasharray="2,2"/>')
    L.append(f'  <text x="330" y="480" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="{PRIMARY_DARK}">3. Перекат</text>')
    L.append(f'  <text x="330" y="492" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="{TEXT_LIGHT}">По спине (дуга)</text>')

    # Arrow 3
    L.append(f'  <line x1="365" y1="445" x2="410" y2="445" stroke="{TEXT_LIGHT}" stroke-width="1.5"/>')
    L.append(f'  <polygon points="410,441 420,445 410,449" fill="{TEXT_LIGHT}"/>')

    # Phase 4: Coming up to squat
    L.append(f'  <g transform="translate(450,425) scale(0.6)" opacity="0.75">')
    L.append(f'    <circle cx="0" cy="6" r="6" fill="none" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="12" x2="0" y2="28" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="28" x2="-10" y2="40" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="28" x2="10" y2="40" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="18" x2="-10" y2="10" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="18" x2="10" y2="10" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    L.append(f'  </g>')
    L.append(f'  <text x="450" y="470" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="{PRIMARY_DARK}">4. Упор присев</text>')
    L.append(f'  <text x="450" y="482" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="{TEXT_LIGHT}">Руки вперед</text>')

    # Arrow 4
    L.append(f'  <line x1="485" y1="445" x2="530" y2="445" stroke="{TEXT_LIGHT}" stroke-width="1.5"/>')
    L.append(f'  <polygon points="530,441 540,445 530,449" fill="{TEXT_LIGHT}"/>')

    # Phase 5: Standing up
    L.append(f'  <g transform="translate(570,405) scale(0.6)" opacity="0.75">')
    L.append(f'    <circle cx="0" cy="6" r="6" fill="none" stroke="{ACCENT_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="12" x2="0" y2="34" stroke="{ACCENT_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="34" x2="-8" y2="48" stroke="{ACCENT_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="34" x2="8" y2="48" stroke="{ACCENT_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="18" x2="-10" y2="30" stroke="{ACCENT_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="18" x2="10" y2="30" stroke="{ACCENT_DARK}" stroke-width="2"/>')
    L.append(f'  </g>')
    L.append(f'  <text x="570" y="470" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="{ACCENT_DARK}">5. Встать</text>')
    L.append(f'  <text x="570" y="482" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="{TEXT_LIGHT}">Руки вверх</text>')

    # Safety warning box
    L.append(f'  <rect x="620" y="400" width="145" height="80" rx="6" fill="#FEF2F2" stroke="{ACCENT}" stroke-width="1.5"/>')
    L.append(f'  <text x="692" y="420" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="{ACCENT_DARK}">ВНИМАНИЕ!</text>')
    L.append(f'  <text x="692" y="436" text-anchor="middle" font-family="Arial,sans-serif" font-size="8.5" fill="{ACCENT_DARK}">Подбородок</text>')
    L.append(f'  <text x="692" y="448" text-anchor="middle" font-family="Arial,sans-serif" font-size="8.5" fill="{ACCENT_DARK}">прижат к груди!</text>')
    L.append(f'  <text x="692" y="464" text-anchor="middle" font-family="Arial,sans-serif" font-size="8.5" fill="{ACCENT_DARK}">Спина округлена!</text>')
    L.append(f'  <text x="692" y="476" text-anchor="middle" font-family="Arial,sans-serif" font-size="8.5" fill="{ACCENT_DARK}">Мат на месте!</text>')

    # Mat indicator under each phase
    for px in [80, 200, 330, 450, 570]:
        L.append(f'  <rect x="{px-25}" y="498" width="50" height="6" rx="2" fill="{PRIMARY_LIGHT}" opacity="0.5"/>')

    L += svg_foot()
    return "\n".join(L)


# ══════════════════════════════════════════════════════════════
# LESSON 6 — Лыжные ходы
# ══════════════════════════════════════════════════════════════
def lesson6() -> str:
    L = svg_head("Лыжные ходы", 6)

    # Row 1
    L += card(16, 72, 245, 155, "Классические ходы", [
        "• Попеременный двухшажный",
        "• Попеременный четырёхшажный",
        "• Одновременный бесшажный",
        "• Одновременный одношажный",
        "• Одновременный двухшажный",
    ])
    L += card(271, 72, 245, 155, "Коньковые ходы", [
        "• Полуконьковый ход",
        "• Коньковый без палок",
        "• Коньковый одновременный",
        "• Коньковый попеременный",
        "• Перекрёстный (двухшажный)",
    ])
    L += card(526, 72, 258, 155, "Выбор хода", [
        "• Классика — лыжня, равнина",
        "• Конёк — без лыжни, подъём",
        "• Бесшажный — хороший скольз.",
        "• Попеременный — подъём в гору",
        "• Одношажный — ускорение",
    ])

    # Row 2
    L += card(16, 237, 245, 125, "Попеременный двухшажный", [
        "• Правая нога + левая палка",
        "• Левая нога + правая палка",
        "• Скользящий шаг — основа",
        "• Толчок ногой назад-вверх",
    ])
    L += card(271, 237, 245, 125, "Одновременный бесшажный", [
        "• Толчок двумя палками сразу",
        "• Ноги не отталкиваются",
        "• Наклон туловища вперёд",
        "• Только при хорошем скольжении",
    ])
    L += card(526, 237, 258, 125, "Подъёмы и спуски", [
        "• «Полуёлочкой» — косой подъём",
        "• «Ёлочкой» — прямо в гору",
        "• «Лесенкой» — крутой подъём",
        "• Спуск в основной стойке",
    ])

    # ── Diagram: ski track patterns ──
    L.append(f'  <rect x="16" y="372" width="385" height="192" rx="8" fill="{BG_CARD}" stroke="{HIGHLIGHT_BD}" stroke-width="1" filter="url(#shadow)"/>')
    L.append(f'  <text x="208" y="392" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="{TEXT_DARK}">След лыжни: классический vs коньковый</text>')

    # Classic track (two parallel lines)
    L.append(f'  <text x="110" y="415" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY_DARK}">Классический ход</text>')
    for i in range(8):
        x1 = 50 + i * 16
        x2 = 50 + (i+1) * 16
        y_top = 425 + (5 if i % 2 == 0 else 0)
        y_bot = 425 + (5 if i % 2 == 1 else 0)
        L.append(f'  <line x1="{x1}" y1="{y_top}" x2="{x2}" y2="{y_bot}" stroke="{PRIMARY_DARK}" stroke-width="3" stroke-linecap="round"/>')
        L.append(f'  <line x1="{x1}" y1="{y_top+16}" x2="{x2}" y2="{y_bot+16}" stroke="{PRIMARY_DARK}" stroke-width="3" stroke-linecap="round"/>')

    # Skate track (V-shaped)
    L.append(f'  <text x="300" y="415" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="{ACCENT_DARK}">Коньковый ход</text>')
    for i in range(6):
        base_x = 230 + i * 22
        # V shape: left edge and right edge
        L.append(f'  <line x1="{base_x}" y1="438" x2="{base_x+6}" y2="425" stroke="{ACCENT_DARK}" stroke-width="2.5" stroke-linecap="round"/>')
        L.append(f'  <line x1="{base_x+12}" y1="438" x2="{base_x+6}" y2="425" stroke="{ACCENT_DARK}" stroke-width="2.5" stroke-linecap="round"/>')

    # Classic technique figure
    L.append(f'  <g transform="translate(80,470) scale(0.7)" opacity="0.65">')
    L.append(f'    <circle cx="0" cy="5" r="5" fill="none" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="10" x2="2" y2="30" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="2" y1="30" x2="-4" y2="44" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="2" y1="30" x2="8" y2="44" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    # Skis (long lines under feet)
    L.append(f'    <line x1="-10" y1="44" x2="4" y2="44" stroke="{PRIMARY_DARK}" stroke-width="3"/>')
    L.append(f'    <line x1="2" y1="44" x2="14" y2="44" stroke="{PRIMARY_DARK}" stroke-width="3"/>')
    # Poles
    L.append(f'    <line x1="2" y1="15" x2="-12" y2="42" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>')
    L.append(f'    <line x1="2" y1="15" x2="14" y2="40" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>')
    L.append(f'  </g>')

    # Skate technique figure
    L.append(f'  <g transform="translate(290,470) scale(0.7)" opacity="0.65">')
    L.append(f'    <circle cx="0" cy="5" r="5" fill="none" stroke="{ACCENT_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="10" x2="3" y2="30" stroke="{ACCENT_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="3" y1="30" x2="-8" y2="44" stroke="{ACCENT_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="3" y1="30" x2="14" y2="42" stroke="{ACCENT_DARK}" stroke-width="2"/>')
    # Skis at V angle
    L.append(f'    <line x1="-14" y1="46" x2="0" y2="42" stroke="{ACCENT_DARK}" stroke-width="3"/>')
    L.append(f'    <line x1="8" y1="42" x2="20" y2="46" stroke="{ACCENT_DARK}" stroke-width="3"/>')
    # Poles
    L.append(f'    <line x1="3" y1="15" x2="-10" y2="42" stroke="{ACCENT_DARK}" stroke-width="1.5"/>')
    L.append(f'    <line x1="3" y1="15" x2="16" y2="38" stroke="{ACCENT_DARK}" stroke-width="1.5"/>')
    L.append(f'  </g>')

    # Labels under figures
    L.append(f'  <text x="80" y="530" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="{PRIMARY_DARK}">Параллельные лыжи</text>')
    L.append(f'  <text x="290" y="530" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="{ACCENT_DARK}">V-образный отталкивание</text>')

    # ── Diagram: diagonal stride cycle ──
    L.append(f'  <rect x="411" y="372" width="373" height="192" rx="8" fill="{BG_CARD}" stroke="{HIGHLIGHT_BD}" stroke-width="1" filter="url(#shadow)"/>')
    L.append(f'  <text x="597" y="392" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="{TEXT_DARK}">Цикл попеременного двухшажного хода</text>')

    # Phase A: right leg push + left pole
    L.append(f'  <g transform="translate(470,440) scale(0.5)" opacity="0.7">')
    L.append(f'    <circle cx="0" cy="5" r="5" fill="none" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="10" x2="3" y2="30" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="3" y1="30" x2="-4" y2="45" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="3" y1="30" x2="10" y2="44" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="3" y1="15" x2="-14" y2="42" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>')
    L.append(f'    <line x1="3" y1="15" x2="16" y2="28" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>')
    L.append(f'  </g>')
    L.append(f'  <text x="475" y="478" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="{PRIMARY_DARK}">Правая + левая</text>')

    # Arrow
    L.append(f'  <line x1="510" y1="455" x2="545" y2="455" stroke="{TEXT_LIGHT}" stroke-width="1.5"/>')
    L.append(f'  <polygon points="545,451 555,455 545,459" fill="{TEXT_LIGHT}"/>')

    # Phase B: glide
    L.append(f'  <g transform="translate(590,440) scale(0.5)" opacity="0.7">')
    L.append(f'    <circle cx="0" cy="5" r="5" fill="none" stroke="{PRIMARY_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="10" x2="0" y2="32" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="32" x2="-8" y2="45" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="32" x2="8" y2="45" stroke="{PRIMARY_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="0" y1="18" x2="-10" y2="30" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>')
    L.append(f'    <line x1="0" y1="18" x2="10" y2="30" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>')
    L.append(f'  </g>')
    L.append(f'  <text x="590" y="478" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="{PRIMARY_DARK}">Скольжение</text>')

    # Arrow
    L.append(f'  <line x1="625" y1="455" x2="660" y2="455" stroke="{TEXT_LIGHT}" stroke-width="1.5"/>')
    L.append(f'  <polygon points="660,451 670,455 660,459" fill="{TEXT_LIGHT}"/>')

    # Phase C: left leg push + right pole
    L.append(f'  <g transform="translate(705,440) scale(0.5)" opacity="0.7">')
    L.append(f'    <circle cx="0" cy="5" r="5" fill="none" stroke="{ACCENT_DARK}" stroke-width="2"/>')
    L.append(f'    <line x1="0" y1="10" x2="-3" y2="30" stroke="{ACCENT_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="-3" y1="30" x2="-10" y2="44" stroke="{ACCENT_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="-3" y1="30" x2="4" y2="45" stroke="{ACCENT_DARK}" stroke-width="2.5"/>')
    L.append(f'    <line x1="-3" y1="15" x2="14" y2="42" stroke="{ACCENT_DARK}" stroke-width="1.5"/>')
    L.append(f'    <line x1="-3" y1="15" x2="-16" y2="28" stroke="{ACCENT_DARK}" stroke-width="1.5"/>')
    L.append(f'  </g>')
    L.append(f'  <text x="705" y="478" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="{ACCENT_DARK}">Левая + правая</text>')

    # Key points
    L.append(f'  <rect x="430" y="492" width="340" height="60" rx="5" fill="{HIGHLIGHT_BG}" stroke="{HIGHLIGHT_BD}" stroke-width="1"/>')
    L.append(f'  <text x="440" y="508" font-family="Arial,sans-serif" font-size="9" fill="{TEXT_MED}">Ключевые моменты:</text>')
    L.append(f'  <text x="440" y="522" font-family="Arial,sans-serif" font-size="8.5" fill="{TEXT_LIGHT}">• Толчок ногой — лыжа прижимается к снегу</text>')
    L.append(f'  <text x="440" y="536" font-family="Arial,sans-serif" font-size="8.5" fill="{TEXT_LIGHT}">• Палка ставится под углом 70–80°, рука прямая</text>')
    L.append(f'  <text x="440" y="548" font-family="Arial,sans-serif" font-size="8.5" fill="{TEXT_LIGHT}">• Наклон туловища 15–20°, взгляд вперёд</text>')

    L += svg_foot()
    return "\n".join(L)


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    generators = [
        (1, lesson1),
        (2, lesson2),
        (3, lesson3),
        (4, lesson4),
        (5, lesson5),
        (6, lesson6),
    ]

    generated = 0
    errors = []

    for num, gen_func in generators:
        svg_content = gen_func()
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")

        # Write
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)

        # Validate with xml.etree.ElementTree
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            ns = "{http://www.w3.org/2000/svg}"
            if root.tag != f"{ns}svg":
                errors.append(f"Lesson {num}: Root tag is {root.tag}, expected {ns}svg")
                print(f"  ❌ Lesson {num}: wrong root tag")
                continue
            # Count child elements as a sanity check
            child_count = len(list(root))
            generated += 1
            fsize = os.path.getsize(filepath)
            print(f"  ✅ Lesson {num}: lesson-{num}.svg  ({fsize:,} bytes, {child_count} elements)")
        except ET.ParseError as e:
            errors.append(f"Lesson {num}: XML parse error — {e}")
            print(f"  ❌ Lesson {num}: XML parse error — {e}")

    # ── Summary ──
    print(f"\n{'='*55}")
    print(f"Generated: {generated}/{len(generators)} SVG files")
    print(f"Output: {OUTPUT_DIR}")
    if errors:
        print(f"\n⚠️  Errors ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
    else:
        print("\n🎉 All 6 SVGs validated successfully as proper XML!")

    # File size check
    all_ok = True
    for num, _ in generators:
        fp = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
        if not os.path.exists(fp):
            print(f"  MISSING: {fp}")
            all_ok = False
        else:
            sz = os.path.getsize(fp)
            if sz < 1000:
                print(f"  WARNING: lesson-{num}.svg is very small ({sz} bytes)")
                all_ok = False
    if all_ok:
        print("✅ All files exist with reasonable sizes.")


if __name__ == "__main__":
    main()
