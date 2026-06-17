#!/usr/bin/env python3
"""Generate 9 detailed educational SVG images for Grade 7 Physics lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/physics"
W, H = 800, 600

# Color palette — orange/amber scheme
BG = "#1C1917"          # dark background
BG2 = "#292524"         # slightly lighter bg
PRIMARY = "#F59E0B"     # amber-500
PRIMARY_LIGHT = "#FCD34D" # amber-300
PRIMARY_DARK = "#B45309"  # amber-700
ACCENT = "#F97316"      # orange-500
TEXT = "#FEF3C7"        # amber-50
TEXT2 = "#FDE68A"       # amber-200
DIM = "#92400E"         # amber-800
WHITE = "#FFFBEB"       # amber-50 light
GRID = "#44403C"        # stone-700
ARROW = "#FB923C"       # orange-400
GREEN = "#4ADE80"       # green-400
RED = "#F87171"         # red-400
BLUE = "#60A5FA"        # blue-400
CYAN = "#22D3EE"        # cyan-400


def esc(text):
    """Escape text for XML."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def svg_header(title):
    """Return opening SVG string with defs and background."""
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG}"/>
      <stop offset="100%" stop-color="{BG2}"/>
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{PRIMARY_DARK}"/>
      <stop offset="100%" stop-color="{PRIMARY}"/>
    </linearGradient>
    <linearGradient id="amberV" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{PRIMARY}"/>
      <stop offset="100%" stop-color="{PRIMARY_DARK}"/>
    </linearGradient>
    <marker id="arrowOrange" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="{ARROW}"/>
    </marker>
    <marker id="arrowWhite" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="{WHITE}"/>
    </marker>
    <marker id="arrowGreen" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="{GREEN}"/>
    </marker>
    <marker id="arrowRed" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="{RED}"/>
    </marker>
    <marker id="arrowBlue" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="{BLUE}"/>
    </marker>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <!-- Background -->
  <rect width="{W}" height="{H}" fill="url(#bgGrad)" rx="12"/>
  <!-- Decorative top bar -->
  <rect x="0" y="0" width="{W}" height="4" fill="url(#amberGrad)" rx="2"/>
'''


def title_block(title, subtitle="", y_offset=0):
    """Return SVG for title block at top."""
    y = 30 + y_offset
    parts = []
    # Icon circle
    parts.append(f'  <circle cx="40" cy="{y + 15}" r="18" fill="{PRIMARY_DARK}" stroke="{PRIMARY}" stroke-width="2"/>')
    parts.append(f'  <text x="40" y="{y + 21}" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="{WHITE}">7</text>')
    # Title
    parts.append(f'  <text x="68" y="{y + 22}" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="{PRIMARY}" filter="url(#glow)">{esc(title)}</text>')
    if subtitle:
        parts.append(f'  <text x="68" y="{y + 40}" font-family="Arial, sans-serif" font-size="13" fill="{TEXT2}">{esc(subtitle)}</text>')
    # Separator line
    sep_y = y + (48 if subtitle else 30)
    parts.append(f'  <line x1="20" y1="{sep_y}" x2="780" y2="{sep_y}" stroke="{DIM}" stroke-width="1" stroke-dasharray="4,4"/>')
    return "\n".join(parts)


def formula_box(x, y, w, h, formula_text, label="", font_size=28):
    """Return SVG for a highlighted formula box."""
    parts = []
    # Background
    parts.append(f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{BG2}" stroke="{PRIMARY}" stroke-width="2"/>')
    # Label
    if label:
        parts.append(f'  <text x="{x + w//2}" y="{y + 18}" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{TEXT2}">{esc(label)}</text>')
    # Formula
    fy = y + h//2 + (10 if label else 5)
    parts.append(f'  <text x="{x + w//2}" y="{fy}" text-anchor="middle" font-family="Arial, sans-serif" font-size="{font_size}" font-weight="bold" fill="{PRIMARY_LIGHT}" filter="url(#glow)">{esc(formula_text)}</text>')
    return "\n".join(parts)


def info_box(x, y, w, h, lines, title=""):
    """Return SVG for an info box with multiple lines of text."""
    parts = []
    parts.append(f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{BG2}" stroke="{GRID}" stroke-width="1"/>')
    if title:
        parts.append(f'  <text x="{x + 10}" y="{y + 18}" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="{PRIMARY}">{esc(title)}</text>')
    start_y = y + (30 if title else 14)
    for i, line in enumerate(lines):
        ty = start_y + i * 17
        if ty > y + h - 5:
            break
        parts.append(f'  <text x="{x + 10}" y="{ty}" font-family="Arial, sans-serif" font-size="11" fill="{TEXT}">{esc(line)}</text>')
    return "\n".join(parts)


def generate_lesson1():
    """Lesson 1: Механическое движение и его характеристики"""
    svg = svg_header("Механическое движение")
    svg += title_block("Механическое движение и его характеристики", "Траектория, путь, перемещение, скорость")
    
    # --- Left column: Diagram of motion ---
    # Trajectory path (curved)
    svg += f'''
  <!-- Motion diagram -->
  <text x="60" y="100" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{PRIMARY}">Траектория движения</text>
  <!-- Dashed trajectory path -->
  <path d="M 80,300 Q 150,180 250,250 Q 350,320 450,200" fill="none" stroke="{ARROW}" stroke-width="2.5" stroke-dasharray="8,4" marker-end="url(#arrowOrange)"/>
  <!-- Start point A -->
  <circle cx="80" cy="300" r="6" fill="{GREEN}"/>
  <text x="65" y="325" font-family="Arial, sans-serif" font-size="12" fill="{GREEN}" font-weight="bold">A</text>
  <!-- End point B -->
  <circle cx="445" cy="203" r="6" fill="{RED}"/>
  <text x="455" y="200" font-family="Arial, sans-serif" font-size="12" fill="{RED}" font-weight="bold">B</text>
  <!-- Path label (along curve) -->
  <text x="160" y="220" font-family="Arial, sans-serif" font-size="12" fill="{ARROW}">s — путь (длина траектории)</text>
  <!-- Displacement (straight line) -->
  <line x1="80" y1="300" x2="445" y2="203" stroke="{CYAN}" stroke-width="2" stroke-dasharray="6,3" marker-end="url(#arrowBlue)"/>
  <text x="200" y="280" font-family="Arial, sans-serif" font-size="12" fill="{CYAN}">Δr — перемещение</text>
  
  <!-- Moving object -->
  <rect x="240" y="240" width="24" height="14" rx="3" fill="{PRIMARY_DARK}" stroke="{PRIMARY}" stroke-width="1.5"/>
  <text x="270" y="250" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">тело</text>
'''
    
    # --- Formula boxes ---
    svg += formula_box(500, 85, 270, 70, "v = s / t", "Скорость равномерного движения", font_size=30)
    svg += formula_box(500, 170, 270, 60, "[v] = м/с", "Единица скорости", font_size=22)
    
    # --- Info boxes ---
    svg += info_box(30, 350, 230, 220, [
        "Траектория — линия, вдоль",
        "которой движется тело.",
        "",
        "Путь (s) — длина траектории.",
        "Скалярная величина.",
        "[s] = м (метр)",
        "",
        "Перемещение (Δr) — вектор",
        "от начальной точки к",
        "конечной. Векторная величина.",
    ], "Ключевые понятия")
    
    svg += info_box(280, 350, 230, 220, [
        "Равномерное движение —",
        "тело за равные промежутки",
        "времени проходит равные",
        "расстояния.",
        "",
        "Скорость постоянна: v = const",
        "",
        "Неравномерное движение —",
        "скорость меняется со временем.",
    ], "Виды движения")
    
    svg += info_box(530, 250, 240, 320, [
        "Формулы:",
        "",
        "v = s / t  (скорость)",
        "s = v · t   (путь)",
        "t = s / v   (время)",
        "",
        "Пример:",
        "Автомобиль проехал 120 км",
        "за 2 часа.",
        "v = 120 / 2 = 60 км/ч",
        "       = 60/3,6 ≈ 16,7 м/с",
        "",
        "Перевод: 1 км/ч = 1/3,6 м/с",
    ], "Расчёты")
    
    # Decorative element: speedometer icon
    svg += f'''
  <circle cx="620" cy="155" r="30" fill="none" stroke="{DIM}" stroke-width="2"/>
  <path d="M 600,170 A 25,25 0 0 1 640,170" fill="none" stroke="{PRIMARY}" stroke-width="3"/>
  <line x1="620" y1="155" x2="635" y2="165" stroke="{RED}" stroke-width="2"/>
  <circle cx="620" cy="155" r="3" fill="{RED}"/>
'''
    
    svg += "\n</svg>"
    return svg


def generate_lesson2():
    """Lesson 2: Расчёт пути и времени движения"""
    svg = svg_header("Расчёт пути и времени")
    svg += title_block("Расчёт пути и времени движения", "Равномерное и неравномерное движение, графики")
    
    # --- Formula boxes (top) ---
    svg += formula_box(30, 85, 240, 70, "s = v · t", "Расчёт пути", font_size=30)
    svg += formula_box(290, 85, 240, 70, "t = s / v", "Расчёт времени", font_size=30)
    svg += formula_box(550, 85, 220, 70, "v = s / t", "Расчёт скорости", font_size=30)
    
    # --- Graph: s(t) for uniform motion ---
    svg += f'''
  <!-- Graph s(t) -->
  <text x="70" y="190" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{PRIMARY}">График пути s(t)</text>
  <rect x="60" y="200" width="340" height="190" rx="6" fill="{BG2}" stroke="{GRID}" stroke-width="1"/>
  <!-- Axes -->
  <line x1="100" y1="370" x2="380" y2="370" stroke="{WHITE}" stroke-width="1.5" marker-end="url(#arrowWhite)"/>
  <line x1="100" y1="370" x2="100" y2="210" stroke="{WHITE}" stroke-width="1.5" marker-end="url(#arrowWhite)"/>
  <text x="375" y="388" font-family="Arial, sans-serif" font-size="11" fill="{TEXT2}">t, с</text>
  <text x="60" y="218" font-family="Arial, sans-serif" font-size="11" fill="{TEXT2}">s, м</text>
  <text x="93" y="385" font-family="Arial, sans-serif" font-size="10" fill="{DIM}">0</text>
  <!-- Grid lines -->
  <line x1="100" y1="330" x2="370" y2="330" stroke="{GRID}" stroke-width="0.5"/>
  <line x1="100" y1="290" x2="370" y2="290" stroke="{GRID}" stroke-width="0.5"/>
  <line x1="100" y1="250" x2="370" y2="250" stroke="{GRID}" stroke-width="0.5"/>
  <line x1="170" y1="370" x2="170" y2="215" stroke="{GRID}" stroke-width="0.5"/>
  <line x1="240" y1="370" x2="240" y2="215" stroke="{GRID}" stroke-width="0.5"/>
  <line x1="310" y1="370" x2="310" y2="215" stroke="{GRID}" stroke-width="0.5"/>
  <!-- Line v₁ (steeper) -->
  <line x1="100" y1="370" x2="310" y2="230" stroke="{GREEN}" stroke-width="2.5"/>
  <text x="315" y="228" font-family="Arial, sans-serif" font-size="11" fill="{GREEN}">v₁</text>
  <!-- Line v₂ (less steep) -->
  <line x1="100" y1="370" x2="360" y2="290" stroke="{CYAN}" stroke-width="2.5"/>
  <text x="365" y="288" font-family="Arial, sans-serif" font-size="11" fill="{CYAN}">v₂</text>
  <text x="160" y="400" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">v₁ &gt; v₂ — крутой наклон</text>
'''
    
    # --- Graph: v(t) ---
    svg += f'''
  <!-- Graph v(t) -->
  <text x="460" y="190" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{PRIMARY}">График скорости v(t)</text>
  <rect x="440" y="200" width="340" height="190" rx="6" fill="{BG2}" stroke="{GRID}" stroke-width="1"/>
  <!-- Axes -->
  <line x1="480" y1="370" x2="760" y2="370" stroke="{WHITE}" stroke-width="1.5" marker-end="url(#arrowWhite)"/>
  <line x1="480" y1="370" x2="480" y2="210" stroke="{WHITE}" stroke-width="1.5" marker-end="url(#arrowWhite)"/>
  <text x="755" y="388" font-family="Arial, sans-serif" font-size="11" fill="{TEXT2}">t, с</text>
  <text x="440" y="218" font-family="Arial, sans-serif" font-size="11" fill="{TEXT2}">v, м/с</text>
  <text x="473" y="385" font-family="Arial, sans-serif" font-size="10" fill="{DIM}">0</text>
  <!-- Horizontal line v=const (uniform) -->
  <line x1="480" y1="270" x2="740" y2="270" stroke="{GREEN}" stroke-width="2.5"/>
  <text x="745" y="275" font-family="Arial, sans-serif" font-size="11" fill="{GREEN}">равномерное</text>
  <!-- Non-uniform (curve) -->
  <path d="M 480,320 Q 560,310 640,250 Q 700,220 740,215" fill="none" stroke="{RED}" stroke-width="2.5"/>
  <text x="745" y="215" font-family="Arial, sans-serif" font-size="11" fill="{RED}">неравномерн.</text>
  <!-- Area under v(t) = path -->
  <rect x="480" y="270" width="260" height="100" fill="{GREEN}" opacity="0.1" stroke="none"/>
  <text x="580" y="340" font-family="Arial, sans-serif" font-size="10" fill="{GREEN}">S = площадь</text>
'''
    
    # --- Info boxes bottom ---
    svg += info_box(30, 410, 250, 170, [
        "Равномерное движение:",
        "• v = const (постоянна)",
        "• s(t) — прямая линия",
        "• v(t) — горизонтальная",
        "",
        "Неравномерное движение:",
        "• v меняется",
        "• s(t) — кривая",
        "• Средняя скорость:",
        "  v_ср = s_общ / t_общ",
    ], "Сравнение видов движения")
    
    svg += info_box(300, 410, 240, 170, [
        "Пример 1: s = v · t",
      "Велосипедист едет со",
      "скоростью 5 м/с за 60 с:",
      "s = 5 · 60 = 300 м",
      "",
      "Пример 2: t = s / v",
      "Расстояние 150 м, v = 10 м/с:",
      "t = 150 / 10 = 15 с",
    ], "Примеры расчётов")
    
    svg += info_box(560, 410, 220, 170, [
        "Средняя скорость:",
      "",
      "v_ср = s_весь / t_всё",
      "",
      "НЕ среднее арифметическое!",
      "",
      "Пример:",
      "s₁=100м v₁=10м/с",
      "s₂=100м v₂=5м/с",
      "v_ср = 200/30 ≈ 6,7 м/с",
    ], "Важно!")
    
    svg += "\n</svg>"
    return svg


def generate_lesson3():
    """Lesson 3: Сила тяжести и вес тела"""
    svg = svg_header("Сила тяжести и вес")
    svg += title_block("Сила тяжести и вес тела", "F = mg, P = mg, свободное падение, масса vs вес")
    
    # --- Formula boxes ---
    svg += formula_box(30, 85, 230, 70, "F = m · g", "Сила тяжести", font_size=30)
    svg += formula_box(280, 85, 230, 70, "P = m · g", "Вес тела (покой)", font_size=30)
    svg += formula_box(530, 85, 240, 70, "g = 9,8 Н/кг", "Ускорение свободного падения", font_size=24)
    
    # --- Left: Force diagram with falling object ---
    svg += f'''
  <!-- Gravity force diagram -->
  <text x="60" y="185" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{PRIMARY}">Сила тяжести</text>
  <rect x="50" y="200" width="260" height="240" rx="6" fill="{BG2}" stroke="{GRID}" stroke-width="1"/>
  <!-- Earth surface -->
  <line x1="55" y1="400" x2="305" y2="400" stroke="{DIM}" stroke-width="2"/>
  <text x="150" y="425" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Земля</text>
  <!-- Object -->
  <rect x="150" y="280" width="50" height="40" rx="5" fill="{PRIMARY_DARK}" stroke="{PRIMARY}" stroke-width="2"/>
  <text x="165" y="305" font-family="Arial, sans-serif" font-size="11" fill="{WHITE}" text-anchor="middle">m</text>
  <!-- F gravity arrow -->
  <line x1="175" y1="320" x2="175" y2="390" stroke="{RED}" stroke-width="3" marker-end="url(#arrowRed)"/>
  <text x="190" y="365" font-family="Arial, sans-serif" font-size="13" fill="{RED}" font-weight="bold">Fтяж</text>
  <!-- Earth center arrow -->
  <text x="120" y="390" font-family="Arial, sans-serif" font-size="10" fill="{DIM}">↓ к центру Земли</text>
'''
    
    # --- Middle: Weight on support ---
    svg += f'''
  <!-- Weight diagram -->
  <text x="370" y="185" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{PRIMARY}">Вес тела на опоре</text>
  <rect x="340" y="200" width="210" height="240" rx="6" fill="{BG2}" stroke="{GRID}" stroke-width="1"/>
  <!-- Table/surface -->
  <rect x="355" y="350" width="180" height="10" rx="2" fill="{DIM}"/>
  <!-- Object on table -->
  <rect x="410" y="300" width="50" height="50" rx="5" fill="{PRIMARY_DARK}" stroke="{PRIMARY}" stroke-width="2"/>
  <text x="425" y="330" font-family="Arial, sans-serif" font-size="11" fill="{WHITE}" text-anchor="middle">m</text>
  <!-- Weight arrow (down) -->
  <line x1="435" y1="350" x2="435" y2="395" stroke="{RED}" stroke-width="2.5" marker-end="url(#arrowRed)"/>
  <text x="450" y="380" font-family="Arial, sans-serif" font-size="11" fill="{RED}" font-weight="bold">P</text>
  <!-- Normal force arrow (up) -->
  <line x1="435" y1="300" x2="435" y2="250" stroke="{GREEN}" stroke-width="2.5" marker-end="url(#arrowGreen)"/>
  <text x="445" y="265" font-family="Arial, sans-serif" font-size="11" fill="{GREEN}" font-weight="bold">N</text>
  <!-- Label -->
  <text x="360" y="420" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">P = N (покой)</text>
'''
    
    # --- Right: Mass vs Weight ---
    svg += f'''
  <!-- Mass vs Weight -->
  <text x="610" y="185" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{PRIMARY}">Масса vs Вес</text>
  <rect x="570" y="200" width="210" height="240" rx="6" fill="{BG2}" stroke="{GRID}" stroke-width="1"/>
  <!-- Mass icon (balance) -->
  <text x="675" y="230" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{PRIMARY}">Масса (m)</text>
  <line x1="630" y1="245" x2="720" y2="245" stroke="{PRIMARY}" stroke-width="2"/>
  <line x1="675" y1="245" x2="675" y2="260" stroke="{PRIMARY}" stroke-width="2"/>
  <path d="M 640,260 L 660,275 L 650,275 L 640,260" fill="{PRIMARY_DARK}" stroke="{PRIMARY}" stroke-width="1"/>
  <path d="M 710,260 L 690,275 L 700,275 L 710,260" fill="{PRIMARY_DARK}" stroke="{PRIMARY}" stroke-width="1"/>
  <text x="675" y="295" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Скаляр [кг]</text>
  <text x="675" y="308" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Не зависит от места</text>
  <!-- Weight icon (spring) -->
  <text x="675" y="335" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{ARROW}">Вес (P)</text>
  <path d="M 665,345 L 670,350 L 660,355 L 670,360 L 660,365 L 670,370 L 665,375" fill="none" stroke="{ARROW}" stroke-width="2"/>
  <rect x="655" y="378" width="30" height="20" rx="3" fill="{PRIMARY_DARK}" stroke="{ARROW}" stroke-width="1.5"/>
  <text x="675" y="420" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Вектор [Н]</text>
  <text x="675" y="433" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Зависит от g</text>
'''
    
    # --- Bottom info ---
    svg += info_box(30, 450, 250, 130, [
        "Fтяж — сила, с которой",
        "Земля притягивает тело.",
        "Направлена к центру Земли.",
        "",
        "P — сила, с которой тело",
        "действует на опору/подвес.",
        "P = mg (в покое)",
    ], "Определения")
    
    svg += info_box(300, 450, 250, 130, [
        "Пример:",
        "m = 10 кг",
        "g = 9,8 Н/кг",
        "F = P = 10 · 9,8 = 98 Н",
        "",
        "На Луне g ≈ 1,6 Н/кг",
        "F = 10 · 1,6 = 16 Н",
    ], "Расчёт")
    
    svg += info_box(570, 450, 210, 130, [
        "Вес при движении:",
        "• Лифт вверх: P &gt; mg",
        "• Лифт вниз: P &lt; mg",
        "• Невесомость: P = 0",
        "  (свободное падение)",
    ], "Интересно")
    
    svg += "\n</svg>"
    return svg


def generate_lesson4():
    """Lesson 4: Сила упругости и сила трения"""
    svg = svg_header("Сила упругости и трение")
    svg += title_block("Сила упругости и сила трения", "Закон Гука F = kx, сила трения, виды трения")
    
    # --- Formula boxes ---
    svg += formula_box(30, 85, 350, 70, "F = k · x  (Закон Гука)", "Сила упругости", font_size=26)
    svg += formula_box(400, 85, 380, 70, "Fтр = μ · N", "Сила трения скольжения", font_size=28)
    
    # --- Left: Spring diagram (Hooke's law) ---
    svg += f'''
  <!-- Spring / Hooke's Law diagram -->
  <text x="60" y="185" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{PRIMARY}">Закон Гука: деформация пружины</text>
  <rect x="30" y="195" width="350" height="200" rx="6" fill="{BG2}" stroke="{GRID}" stroke-width="1"/>
  
  <!-- Undeformed spring -->
  <text x="50" y="225" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Исходное состояние:</text>
  <line x1="60" y1="240" x2="60" y2="240" stroke="{WHITE}" stroke-width="1"/>
  <!-- Wall -->
  <rect x="50" y="230" width="10" height="30" fill="{GRID}"/>
  <!-- Spring (relaxed) -->
  <path d="M 60,245 L 70,235 L 80,255 L 90,235 L 100,255 L 110,235 L 120,255 L 130,245" fill="none" stroke="{GREEN}" stroke-width="2"/>
  <!-- Block relaxed -->
  <rect x="130" y="232" width="30" height="26" rx="3" fill="{PRIMARY_DARK}" stroke="{GREEN}" stroke-width="1.5"/>
  <text x="145" y="250" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="{WHITE}">m</text>
  
  <!-- Deformed spring -->
  <text x="50" y="290" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Растянутая пружина:</text>
  <rect x="50" y="300" width="10" height="30" fill="{GRID}"/>
  <!-- Stretched spring -->
  <path d="M 60,315 L 80,305 L 100,325 L 120,305 L 140,325 L 160,305 L 180,325 L 200,315" fill="none" stroke="{RED}" stroke-width="2"/>
  <!-- Block stretched -->
  <rect x="200" y="302" width="30" height="26" rx="3" fill="{PRIMARY_DARK}" stroke="{RED}" stroke-width="1.5"/>
  <text x="215" y="320" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="{WHITE}">m</text>
  <!-- x displacement -->
  <line x1="130" y1="345" x2="200" y2="345" stroke="{CYAN}" stroke-width="1.5" marker-end="url(#arrowBlue)"/>
  <text x="155" y="360" font-family="Arial, sans-serif" font-size="11" fill="{CYAN}" text-anchor="middle">x</text>
  <!-- Force arrow -->
  <line x1="230" y1="315" x2="280" y2="315" stroke="{ARROW}" stroke-width="2.5" marker-end="url(#arrowOrange)"/>
  <text x="255" y="308" font-family="Arial, sans-serif" font-size="11" fill="{ARROW}">F</text>
  <!-- Fупр arrow back -->
  <line x1="200" y1="325" x2="155" y2="325" stroke="{GREEN}" stroke-width="2" marker-end="url(#arrowGreen)"/>
  <text x="170" y="340" font-family="Arial, sans-serif" font-size="10" fill="{GREEN}">Fупр</text>
'''
    
    # --- Right: Friction types ---
    svg += f'''
  <!-- Friction types -->
  <text x="430" y="185" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{PRIMARY}">Виды силы трения</text>
  <rect x="400" y="195" width="380" height="200" rx="6" fill="{BG2}" stroke="{GRID}" stroke-width="1"/>
  
  <!-- 1. Static friction -->
  <text x="420" y="220" font-family="Arial, sans-serif" font-size="12" fill="{ARROW}">1. Трение покоя</text>
  <rect x="430" y="228" width="40" height="20" rx="3" fill="{PRIMARY_DARK}" stroke="{ARROW}" stroke-width="1"/>
  <line x1="420" y1="248" x2="490" y2="248" stroke="{DIM}" stroke-width="2"/>
  <line x1="475" y1="238" x2="500" y2="238" stroke="{RED}" stroke-width="1.5" marker-end="url(#arrowRed)"/>
  <text x="510" y="242" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Тело не движется</text>
  
  <!-- 2. Sliding friction -->
  <text x="420" y="275" font-family="Arial, sans-serif" font-size="12" fill="{ARROW}">2. Трение скольжения</text>
  <rect x="430" y="283" width="40" height="20" rx="3" fill="{PRIMARY_DARK}" stroke="{ARROW}" stroke-width="1"/>
  <line x1="420" y1="303" x2="490" y2="303" stroke="{DIM}" stroke-width="2"/>
  <line x1="470" y1="293" x2="500" y2="293" stroke="{RED}" stroke-width="1.5" marker-end="url(#arrowRed)"/>
  <line x1="475" y1="293" x2="455" y2="293" stroke="{GREEN}" stroke-width="1.5" marker-end="url(#arrowGreen)"/>
  <text x="510" y="297" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Тело скользит</text>
  
  <!-- 3. Rolling friction -->
  <text x="420" y="330" font-family="Arial, sans-serif" font-size="12" fill="{ARROW}">3. Трение качения</text>
  <circle cx="450" cy="358" r="12" fill="none" stroke="{ARROW}" stroke-width="2"/>
  <line x1="438" y1="370" x2="462" y2="370" stroke="{ARROW}" stroke-width="1.5"/>
  <line x1="420" y1="370" x2="490" y2="370" stroke="{DIM}" stroke-width="2"/>
  <text x="510" y="362" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Колесо катится</text>
  <text x="510" y="377" font-family="Arial, sans-serif" font-size="10" fill="{GREEN}">Fтр.кач &lt; Fтр.скольж</text>
'''
    
    # --- Bottom info ---
    svg += info_box(30, 410, 250, 170, [
        "Закон Гука:",
        "Fупр = k · x",
        "k — жёсткость [Н/м]",
        "x — удлинение [м]",
        "",
        "Сила упругости направлена",
        "противоположно деформации.",
        "",
        "Пример: k = 100 Н/м,",
        "x = 0,05 м → F = 5 Н",
    ], "Сила упругости")
    
    svg += info_box(300, 410, 250, 170, [
        "Сила трения:",
        "Fтр = μ · N",
        "μ — коэффициент трения",
        "N — сила нормальной реакции",
        "",
        "Трение зависит от:",
        "• Материала поверхностей",
        "• Силы прижимания (N)",
        "• НЕ зависит от площади!",
    ], "Сила трения")
    
    svg += info_box(570, 410, 210, 170, [
        "Полезное трение:",
        "• Ходьба",
        "• Торможение",
        "• Движение колёс",
        "",
        "Вредное трение:",
        "• Износ деталей",
        "• Нагрев механизмов",
        "",
        "Борьба: смазка,",
        "подшипники, полировка",
    ], "Трение: + и −")
    
    svg += "\n</svg>"
    return svg


def generate_lesson5():
    """Lesson 5: Законы Ньютона"""
    svg = svg_header("Законы Ньютона")
    svg += title_block("Законы Ньютона", "I закон (инерция), II закон (F=ma), III закон (действие=противодействие)")
    
    # --- Three law cards ---
    # Law I
    svg += f'''
  <!-- I Закон Ньютона -->
  <rect x="25" y="90" width="240" height="230" rx="8" fill="{BG2}" stroke="{PRIMARY}" stroke-width="2"/>
  <rect x="25" y="90" width="240" height="30" rx="8" fill="{PRIMARY_DARK}"/>
  <text x="145" y="110" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{WHITE}">I Закон Ньютона</text>
  <text x="40" y="145" font-family="Arial, sans-serif" font-size="11" fill="{PRIMARY_LIGHT}" font-weight="bold">Закон инерции:</text>
  <text x="40" y="163" font-family="Arial, sans-serif" font-size="10" fill="{TEXT}">Тело сохраняет состояние</text>
  <text x="40" y="177" font-family="Arial, sans-serif" font-size="10" fill="{TEXT}">покоя или равномерного</text>
  <text x="40" y="191" font-family="Arial, sans-serif" font-size="10" fill="{TEXT}">прямолинейного движения,</text>
  <text x="40" y="205" font-family="Arial, sans-serif" font-size="10" fill="{TEXT}">если на него не действуют</text>
  <text x="40" y="219" font-family="Arial, sans-serif" font-size="10" fill="{TEXT}">другие тела или их действие</text>
  <text x="40" y="233" font-family="Arial, sans-serif" font-size="10" fill="{TEXT}">скомпенсировано.</text>
  <!-- Inertia diagram: object moving at constant v -->
  <line x1="50" y1="270" x2="230" y2="270" stroke="{DIM}" stroke-width="2"/>
  <rect x="80" y="254" width="35" height="22" rx="3" fill="{PRIMARY_DARK}" stroke="{GREEN}" stroke-width="1.5"/>
  <line x1="115" y1="265" x2="145" y2="265" stroke="{GREEN}" stroke-width="2" marker-end="url(#arrowGreen)"/>
  <text x="150" y="268" font-family="Arial, sans-serif" font-size="11" fill="{GREEN}">v = const</text>
  <text x="145" y="300" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{DIM}">F = 0 → v = const</text>
'''
    
    # Law II
    svg += f'''
  <!-- II Закон Ньютона -->
  <rect x="280" y="90" width="240" height="230" rx="8" fill="{BG2}" stroke="{PRIMARY}" stroke-width="2"/>
  <rect x="280" y="90" width="240" height="30" rx="8" fill="{PRIMARY_DARK}"/>
  <text x="400" y="110" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{WHITE}">II Закон Ньютона</text>
  <!-- Big formula -->
  <text x="400" y="155" text-anchor="middle" font-family="Arial, sans-serif" font-size="32" font-weight="bold" fill="{PRIMARY_LIGHT}" filter="url(#glow)">F = m · a</text>
  <text x="400" y="178" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Ускорение прямо пропорционально</text>
  <text x="400" y="192" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">силе и обратно пропорционально</text>
  <text x="400" y="206" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">массе тела</text>
  <!-- Force diagram -->
  <rect x="330" y="225" width="40" height="30" rx="3" fill="{PRIMARY_DARK}" stroke="{PRIMARY}" stroke-width="1.5"/>
  <text x="350" y="244" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="{WHITE}">m</text>
  <line x1="370" y1="240" x2="420" y2="240" stroke="{RED}" stroke-width="2.5" marker-end="url(#arrowRed)"/>
  <text x="395" y="233" font-family="Arial, sans-serif" font-size="11" fill="{RED}" font-weight="bold">F</text>
  <line x1="370" y1="260" x2="420" y2="260" stroke="{GREEN}" stroke-width="2" marker-end="url(#arrowGreen)"/>
  <text x="395" y="275" font-family="Arial, sans-serif" font-size="11" fill="{GREEN}" font-weight="bold">a</text>
  <text x="400" y="305" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{DIM}">[F]=Н, [m]=кг, [a]=м/с²</text>
'''
    
    # Law III
    svg += f'''
  <!-- III Закон Ньютона -->
  <rect x="535" y="90" width="240" height="230" rx="8" fill="{BG2}" stroke="{PRIMARY}" stroke-width="2"/>
  <rect x="535" y="90" width="240" height="30" rx="8" fill="{PRIMARY_DARK}"/>
  <text x="655" y="110" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{WHITE}">III Закон Ньютона</text>
  <text x="655" y="150" text-anchor="middle" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="{PRIMARY_LIGHT}" filter="url(#glow)">F₁ = −F₂</text>
  <text x="655" y="175" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Действие = Противодействие</text>
  <text x="655" y="192" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Силы равны по модулю,</text>
  <text x="655" y="206" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">противоположны по</text>
  <text x="655" y="220" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">направлению, приложены</text>
  <text x="655" y="234" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">к разным телам!</text>
  <!-- Two objects pushing -->
  <rect x="580" y="255" width="40" height="30" rx="3" fill="{PRIMARY_DARK}" stroke="{RED}" stroke-width="1.5"/>
  <rect x="690" y="255" width="40" height="30" rx="3" fill="{BG}" stroke="{GREEN}" stroke-width="1.5"/>
  <line x1="620" y1="270" x2="660" y2="270" stroke="{RED}" stroke-width="2" marker-end="url(#arrowRed)"/>
  <text x="635" y="265" font-family="Arial, sans-serif" font-size="10" fill="{RED}">F₁</text>
  <line x1="690" y1="275" x2="650" y2="275" stroke="{GREEN}" stroke-width="2" marker-end="url(#arrowGreen)"/>
  <text x="665" y="290" font-family="Arial, sans-serif" font-size="10" fill="{GREEN}">F₂</text>
  <text x="655" y="305" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{DIM}">|F₁| = |F₂|</text>
'''
    
    # --- Bottom examples ---
    svg += info_box(25, 340, 250, 240, [
        "Примеры I закона:",
        "",
        "• Книга на столе — покой",
        "  (Fтяж = N, уравновешены)",
        "• Мяч катится по льду —",
        "  равномерное движение",
        "  (трение мало)",
        "• Космонавт в космосе —",
        "  движется по инерции",
        "",
        "Инерция — свойство тела",
        "сохранять свою скорость.",
    ], "I Закон: примеры")
    
    svg += info_box(290, 340, 250, 240, [
        "Примеры II закона:",
        "",
        "• Чем больше сила, тем",
        "  больше ускорение.",
        "• Чем больше масса, тем",
        "  меньше ускорение.",
        "",
        "Задача: m=2кг, F=10Н",
        "a = F/m = 10/2 = 5 м/с²",
        "",
        "Если F удвоить → a удвоится",
        "Если m удвоить → a уменьш.",
    ], "II Закон: примеры")
    
    svg += info_box(555, 340, 220, 240, [
        "Примеры III закона:",
        "",
        "• Стол давит на книгу,",
        "  книга — на стол.",
        "• Ноги толкают землю,",
        "  земля — ноги (ходьба).",
        "• Ракета: газы назад,",
        "  ракета вперёд.",
        "",
        "Важно: силы приложены",
        "к РАЗНЫМ телам, поэтому",
        "не уравновешивают!",
    ], "III Закон: примеры")
    
    svg += "\n</svg>"
    return svg


def generate_lesson6():
    """Lesson 6: Давление и его единицы"""
    svg = svg_header("Давление")
    svg += title_block("Давление и его единицы", "p = F/S, единицы (Па), увеличение/уменьшение давления")
    
    # --- Formula box ---
    svg += formula_box(30, 85, 350, 80, "p = F / S", "Давление", font_size=34)
    svg += formula_box(400, 85, 380, 80, "[p] = Па = Н/м²", "Единица давления — Паскаль", font_size=24)
    
    # --- Diagram: same force, different area ---
    svg += f'''
  <!-- Pressure comparison diagram -->
  <text x="60" y="200" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{PRIMARY}">Одинаковая сила — разное давление</text>
  <rect x="30" y="210" width="480" height="200" rx="6" fill="{BG2}" stroke="{GRID}" stroke-width="1"/>
  
  <!-- Small area → high pressure -->
  <text x="100" y="235" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{RED}">Малая площадь</text>
  <text x="100" y="250" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{RED}">→ Большое давление</text>
  <!-- Sharp object -->
  <polygon points="90,265 110,265 105,330 95,330" fill="{PRIMARY_DARK}" stroke="{RED}" stroke-width="2"/>
  <line x1="100" y1="265" x2="100" y2="235" stroke="{ARROW}" stroke-width="2" marker-end="url(#arrowOrange)"/>
  <text x="120" y="340" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">F=10Н, S=0,001м²</text>
  <text x="120" y="355" font-family="Arial, sans-serif" font-size="10" fill="{RED}" font-weight="bold">p = 10 000 Па</text>
  <!-- Surface -->
  <line x1="55" y1="330" x2="155" y2="330" stroke="{DIM}" stroke-width="3"/>
  
  <!-- Large area → low pressure -->
  <text x="330" y="235" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{GREEN}">Большая площадь</text>
  <text x="330" y="250" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{GREEN}">→ Малое давление</text>
  <!-- Wide object -->
  <rect x="290" y="265" width="80" height="60" rx="3" fill="{PRIMARY_DARK}" stroke="{GREEN}" stroke-width="2"/>
  <line x1="330" y1="265" x2="330" y2="235" stroke="{ARROW}" stroke-width="2" marker-end="url(#arrowOrange)"/>
  <text x="340" y="340" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">F=10Н, S=0,1м²</text>
  <text x="340" y="355" font-family="Arial, sans-serif" font-size="10" fill="{GREEN}" font-weight="bold">p = 100 Па</text>
  <!-- Surface -->
  <line x1="260" y1="325" x2="420" y2="325" stroke="{DIM}" stroke-width="3"/>
'''
    
    # --- Right: Examples of pressure ---
    svg += f'''
  <!-- Examples -->
  <text x="560" y="200" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{PRIMARY}">Примеры давления</text>
  <rect x="530" y="210" width="250" height="200" rx="6" fill="{BG2}" stroke="{GRID}" stroke-width="1"/>
  
  <!-- Knife (increase pressure) -->
  <text x="550" y="235" font-family="Arial, sans-serif" font-size="11" fill="{ARROW}">Увеличение давления:</text>
  <path d="M 560,250 L 620,250 L 620,280 L 560,280 Z" fill="none" stroke="{ARROW}" stroke-width="1.5"/>
  <polygon points="575,280 605,280 600,310 580,310" fill="{PRIMARY_DARK}" stroke="{RED}" stroke-width="1.5"/>
  <text x="630" y="300" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Нож — острый</text>
  <text x="630" y="313" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">край (малая S)</text>
  
  <!-- Snowshoes (decrease pressure) -->
  <text x="550" y="345" font-family="Arial, sans-serif" font-size="11" fill="{ARROW}">Уменьшение давления:</text>
  <rect x="560" y="355" width="50" height="8" rx="2" fill="{PRIMARY_DARK}" stroke="{GREEN}" stroke-width="1.5"/>
  <rect x="555" y="363" width="60" height="5" rx="2" fill="{DIM}" stroke="{GREEN}" stroke-width="1"/>
  <text x="630" y="365" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Лыжи — широкие</text>
  <text x="630" y="378" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">(большая S)</text>
'''
    
    # --- Bottom info ---
    svg += info_box(30, 425, 250, 155, [
        "Давление p = F / S:",
        "F — сила, действующая на",
        "  поверхность [Н]",
        "S — площадь поверхности [м²]",
        "",
        "1 Па = 1 Н/м²",
        "1 кПа = 1000 Па",
        "1 гПа = 100 Па",
        "1 МПа = 1 000 000 Па",
    ], "Формула и единицы")
    
    svg += info_box(300, 425, 250, 155, [
        "Как увеличить давление:",
        "• Увеличить силу F",
        "• Уменьшить площадь S",
        "  (заточить, заострить)",
        "",
        "Как уменьшить давление:",
        "• Уменьшить силу F",
        "• Увеличить площадь S",
        "  (широкие шины, лыжи)",
    ], "Управление давлением")
    
    svg += info_box(570, 425, 210, 155, [
        "Примеры:",
        "• Гвоздь: острый конец",
        "  p очень большое",
        "• Фундамент: широкое",
        "  основание, p мало",
        "• Танк: гусеницы,",
        "  p = 40-50 кПа",
        "• Человек: p ≈ 20 кПа",
    ], "Практика")
    
    svg += "\n</svg>"
    return svg


def generate_lesson7():
    """Lesson 7: Давление жидкостей и газов"""
    svg = svg_header("Давление жидкостей")
    svg += title_block("Давление жидкостей и газов", "Закон Паскаля, гидростатическое давление p = ρgh")
    
    # --- Formula boxes ---
    svg += formula_box(30, 85, 360, 70, "p = ρ · g · h", "Гидростатическое давление", font_size=30)
    svg += formula_box(410, 85, 370, 70, "Закон Паскаля", "Давление передаётся одинаково во все стороны", font_size=18)
    
    # --- Left: Pascal's law diagram ---
    svg += f'''
  <!-- Pascal's Law -->
  <text x="60" y="185" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{PRIMARY}">Закон Паскаля</text>
  <rect x="30" y="195" width="260" height="200" rx="6" fill="{BG2}" stroke="{GRID}" stroke-width="1"/>
  <!-- Container shape -->
  <ellipse cx="160" cy="370" rx="100" ry="15" fill="none" stroke="{ARROW}" stroke-width="1.5"/>
  <path d="M 60,250 L 60,370" fill="none" stroke="{ARROW}" stroke-width="1.5"/>
  <path d="M 260,250 L 260,370" fill="none" stroke="{ARROW}" stroke-width="1.5"/>
  <ellipse cx="160" cy="250" rx="100" ry="15" fill="none" stroke="{ARROW}" stroke-width="1.5"/>
  <!-- Liquid fill -->
  <ellipse cx="160" cy="320" rx="98" ry="14" fill="{BLUE}" opacity="0.2"/>
  <rect x="62" y="320" width="196" height="50" fill="{BLUE}" opacity="0.2"/>
  <!-- Pressure arrows from center point -->
  <circle cx="160" cy="330" r="5" fill="{PRIMARY}"/>
  <line x1="160" y1="330" x2="160" y2="280" stroke="{RED}" stroke-width="1.5" marker-end="url(#arrowRed)"/>
  <line x1="160" y1="330" x2="210" y2="310" stroke="{RED}" stroke-width="1.5" marker-end="url(#arrowRed)"/>
  <line x1="160" y1="330" x2="110" y2="310" stroke="{RED}" stroke-width="1.5" marker-end="url(#arrowRed)"/>
  <line x1="160" y1="330" x2="210" y2="350" stroke="{RED}" stroke-width="1.5" marker-end="url(#arrowRed)"/>
  <line x1="160" y1="330" x2="110" y2="350" stroke="{RED}" stroke-width="1.5" marker-end="url(#arrowRed)"/>
  <text x="160" y="400" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Давление одинаково</text>
  <text x="160" y="413" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">во всех направлениях</text>
'''
    
    # --- Middle: Hydrostatic pressure vessel ---
    svg += f'''
  <!-- Hydrostatic pressure -->
  <text x="340" y="185" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{PRIMARY}">Гидростатическое давление</text>
  <rect x="310" y="195" width="220" height="200" rx="6" fill="{BG2}" stroke="{GRID}" stroke-width="1"/>
  <!-- Water column -->
  <rect x="370" y="220" width="60" height="150" rx="3" fill="{BLUE}" opacity="0.25" stroke="{ARROW}" stroke-width="1.5"/>
  <!-- Water level marks -->
  <line x1="440" y1="240" x2="455" y2="240" stroke="{DIM}" stroke-width="1"/>
  <text x="460" y="244" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">h₁</text>
  <line x1="440" y1="300" x2="455" y2="300" stroke="{DIM}" stroke-width="1"/>
  <text x="460" y="304" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">h₂</text>
  <line x1="440" y1="370" x2="455" y2="370" stroke="{DIM}" stroke-width="1"/>
  <text x="460" y="374" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">h₃</text>
  <!-- Pressure arrows at different depths -->
  <line x1="370" y1="240" x2="345" y2="240" stroke="{GREEN}" stroke-width="1.5" marker-end="url(#arrowGreen)"/>
  <text x="320" y="244" font-family="Arial, sans-serif" font-size="9" fill="{GREEN}">p₁</text>
  <line x1="370" y1="300" x2="330" y2="300" stroke="{ARROW}" stroke-width="2" marker-end="url(#arrowOrange)"/>
  <text x="310" y="304" font-family="Arial, sans-serif" font-size="9" fill="{ARROW}">p₂</text>
  <line x1="370" y1="370" x2="320" y2="370" stroke="{RED}" stroke-width="2.5" marker-end="url(#arrowRed)"/>
  <text x="300" y="374" font-family="Arial, sans-serif" font-size="9" fill="{RED}">p₃</text>
  <!-- Labels -->
  <text x="390" y="260" font-family="Arial, sans-serif" font-size="10" fill="{DIM}">мало</text>
  <text x="390" y="340" font-family="Arial, sans-serif" font-size="10" fill="{RED}">велико</text>
'''
    
    # --- Right: Communicating vessels ---
    svg += f'''
  <!-- Communicating vessels -->
  <text x="600" y="185" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{PRIMARY}">Сообщающиеся сосуды</text>
  <rect x="550" y="195" width="220" height="200" rx="6" fill="{BG2}" stroke="{GRID}" stroke-width="1"/>
  <!-- U-tube -->
  <path d="M 600,220 L 600,340 Q 600,370 630,370 L 700,370 Q 730,370 730,340 L 730,220" fill="none" stroke="{ARROW}" stroke-width="2"/>
  <!-- Water in U-tube -->
  <path d="M 600,280 L 600,340 Q 600,365 630,365 L 700,365 Q 730,365 730,340 L 730,280" fill="{BLUE}" opacity="0.3" stroke="none"/>
  <!-- Water level line -->
  <line x1="590" y1="280" x2="740" y2="280" stroke="{CYAN}" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="660" y="275" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{CYAN}">Уровень одинаков</text>
  <!-- Different density -->
  <text x="660" y="410" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Однородная жидкость —</text>
  <text x="660" y="423" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">уровни равны</text>
'''
    
    # --- Bottom info ---
    svg += info_box(30, 420, 250, 160, [
        "Закон Паскаля:",
        "Давление, производимое на",
        "жидкость или газ, передаётся",
        "без изменения в каждую",
        "точку объёма жидкости.",
        "",
        "Применение:",
        "• Гидравлический пресс",
        "• Тормозная система",
    ], "Закон Паскаля")
    
    svg += info_box(300, 420, 250, 160, [
        "p = ρgh:",
        "ρ — плотность [кг/м³]",
        "g = 9,8 Н/кг",
        "h — глубина [м]",
        "",
        "Пример (вода):",
        "ρ = 1000 кг/м³",
        "h = 10 м",
        "p = 1000·9,8·10 = 98 кПа",
    ], "Гидростатика")
    
    svg += info_box(570, 420, 210, 160, [
        "Атмосферное давление:",
        "Pатм ≈ 101 325 Па",
        "       ≈ 101,3 кПа",
        "",
        "Опыт Торричелли:",
        "760 мм рт. ст.",
        "= 101 325 Па",
        "",
        "1 мм рт. ст. ≈ 133 Па",
    ], "Атмосфера")
    
    svg += "\n</svg>"
    return svg


def generate_lesson8():
    """Lesson 8: Механическая работа"""
    svg = svg_header("Механическая работа")
    svg += title_block("Механическая работа", "A = Fs, единицы (Дж), положительная/отрицательная работа, угол")
    
    # --- Formula boxes ---
    svg += formula_box(30, 85, 280, 70, "A = F · s", "Механическая работа", font_size=32)
    svg += formula_box(330, 85, 230, 70, "[A] = Дж = Н·м", "Единица — Джоуль", font_size=22)
    svg += formula_box(580, 85, 200, 70, "A = F·s·cosα", "С учётом угла", font_size=20)
    
    # --- Diagram: Work with angle ---
    svg += f'''
  <!-- Work diagram -->
  <text x="60" y="195" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{PRIMARY}">Работа силы при движении</text>
  <rect x="30" y="205" width="480" height="200" rx="6" fill="{BG2}" stroke="{GRID}" stroke-width="1"/>
  <!-- Surface -->
  <line x1="50" y1="360" x2="490" y2="360" stroke="{DIM}" stroke-width="2"/>
  <!-- Object -->
  <rect x="140" y="325" width="60" height="35" rx="5" fill="{PRIMARY_DARK}" stroke="{PRIMARY}" stroke-width="2"/>
  <text x="170" y="348" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{WHITE}">m</text>
  <!-- Displacement arrow -->
  <line x1="200" y1="343" x2="300" y2="343" stroke="{CYAN}" stroke-width="2" marker-end="url(#arrowBlue)"/>
  <text x="250" y="335" font-family="Arial, sans-serif" font-size="12" fill="{CYAN}" text-anchor="middle">s</text>
  <!-- Force arrow at angle -->
  <line x1="170" y1="325" x2="170" y2="245" stroke="{RED}" stroke-width="2.5" marker-end="url(#arrowRed)"/>
  <text x="155" y="260" font-family="Arial, sans-serif" font-size="12" fill="{RED}" font-weight="bold">F</text>
  <!-- Angle arc -->
  <path d="M 180,325 A 15,15 0 0 0 176,310" fill="none" stroke="{PRIMARY_LIGHT}" stroke-width="1.5"/>
  <text x="195" y="315" font-family="Arial, sans-serif" font-size="12" fill="{PRIMARY_LIGHT}">α</text>
  <!-- Component arrows -->
  <line x1="170" y1="325" x2="220" y2="325" stroke="{GREEN}" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#arrowGreen)"/>
  <text x="225" y="320" font-family="Arial, sans-serif" font-size="10" fill="{GREEN}">F·cosα</text>
  <line x1="220" y1="325" x2="220" y2="280" stroke="{DIM}" stroke-width="1" stroke-dasharray="3,3"/>
'''
    
    # --- Three cases of work ---
    svg += f'''
  <!-- Three cases -->
  <text x="560" y="195" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{PRIMARY}">Знак работы</text>
  <rect x="530" y="205" width="250" height="200" rx="6" fill="{BG2}" stroke="{GRID}" stroke-width="1"/>
  
  <!-- Positive work -->
  <circle cx="565" cy="235" r="8" fill="{GREEN}" opacity="0.5"/>
  <text x="565" y="239" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{WHITE}">+</text>
  <text x="580" y="239" font-family="Arial, sans-serif" font-size="11" fill="{GREEN}" font-weight="bold">A &gt; 0</text>
  <text x="580" y="255" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Сила вдоль движения</text>
  <text x="580" y="268" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">(α &lt; 90°)</text>
  
  <!-- Zero work -->
  <circle cx="565" cy="295" r="8" fill="{DIM}" opacity="0.5"/>
  <text x="565" y="299" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{WHITE}">0</text>
  <text x="580" y="299" font-family="Arial, sans-serif" font-size="11" fill="{PRIMARY}" font-weight="bold">A = 0</text>
  <text x="580" y="315" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Сила ⊥ движению</text>
  <text x="580" y="328" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">(α = 90°)</text>
  
  <!-- Negative work -->
  <circle cx="565" cy="355" r="8" fill="{RED}" opacity="0.5"/>
  <text x="565" y="359" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{WHITE}">−</text>
  <text x="580" y="359" font-family="Arial, sans-serif" font-size="11" fill="{RED}" font-weight="bold">A &lt; 0</text>
  <text x="580" y="375" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">Сила против движения</text>
  <text x="580" y="388" font-family="Arial, sans-serif" font-size="10" fill="{TEXT2}">(α &gt; 90°)</text>
'''
    
    # --- Bottom info ---
    svg += info_box(30, 420, 250, 160, [
        "Механическая работа:",
        "A = F · s · cos α",
        "",
        "F — сила [Н]",
        "s — перемещение [м]",
        "α — угол между F и s",
        "",
        "A = 0, если:",
        "• F = 0 (нет силы)",
        "• s = 0 (нет движения)",
        "• α = 90° (сила ⊥ пути)",
    ], "Определение")
    
    svg += info_box(300, 420, 250, 160, [
        "Примеры:",
        "",
        "1) Подъём груза F=100Н,",
        "   h=3м: A = 100·3 = 300 Дж",
        "",
        "2) Трение Fтр=20Н, s=5м:",
        "   A = −20·5 = −100 Дж",
        "   (сила против движения)",
        "",
        "3) Сила тяжести при движении",
        "   по горизонтали: A = 0",
    ], "Примеры расчётов")
    
    svg += info_box(570, 420, 210, 160, [
        "Важно помнить:",
        "",
        "• Работа — скалярная",
        "  величина (не вектор)",
        "• Может быть +, −, 0",
        "• 1 Дж = 1 Н · 1 м",
        "• 1 кДж = 1000 Дж",
        "• 1 МДж = 1 000 000 Дж",
        "",
        "Совершает работу та",
        "сила, которая вызывает",
        "перемещение!",
    ], "Ключевые моменты")
    
    svg += "\n</svg>"
    return svg


def generate_lesson9():
    """Lesson 9: Мощность"""
    svg = svg_header("Мощность")
    svg += title_block("Мощность", "N = A/t, единицы (Вт), мощность vs работа, практические примеры")
    
    # --- Formula boxes ---
    svg += formula_box(30, 85, 300, 70, "N = A / t", "Мощность", font_size=32)
    svg += formula_box(350, 85, 220, 70, "[N] = Вт = Дж/с", "Единица — Ватт", font_size=22)
    svg += formula_box(590, 85, 190, 70, "N = F · v", "Мощность при движении", font_size=22)
    
    # --- Diagram: Power comparison ---
    svg += f'''
  <!-- Power comparison: two workers -->
  <text x="60" y="195" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{PRIMARY}">Мощность: кто быстрее?</text>
  <rect x="30" y="205" width="480" height="180" rx="6" fill="{BG2}" stroke="{GRID}" stroke-width="1"/>
  
  <!-- Worker 1 (slow) -->
  <text x="120" y="230" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{CYAN}">Медленный</text>
  <!-- Person icon -->
  <circle cx="120" cy="250" r="8" fill="none" stroke="{CYAN}" stroke-width="1.5"/>
  <line x1="120" y1="258" x2="120" y2="285" stroke="{CYAN}" stroke-width="1.5"/>
  <line x1="105" y1="268" x2="135" y2="268" stroke="{CYAN}" stroke-width="1.5"/>
  <line x1="120" y1="285" x2="108" y2="310" stroke="{CYAN}" stroke-width="1.5"/>
  <line x1="120" y1="285" x2="132" y2="310" stroke="{CYAN}" stroke-width="1.5"/>
  <!-- Box being carried -->
  <rect x="100" y="310" width="40" height="25" rx="3" fill="{PRIMARY_DARK}" stroke="{CYAN}" stroke-width="1.5"/>
  <text x="120" y="327" text-anchor="middle" font-family="Arial, sans-serif" font-size="8" fill="{WHITE}">A=500Дж</text>
  <text x="120" y="355" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{CYAN}">t = 50 с</text>
  <text x="120" y="370" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{CYAN}" font-weight="bold">N = 10 Вт</text>
  
  <!-- Worker 2 (fast) -->
  <text x="350" y="230" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{RED}">Быстрый</text>
  <circle cx="350" cy="250" r="8" fill="none" stroke="{RED}" stroke-width="1.5"/>
  <line x1="350" y1="258" x2="350" y2="285" stroke="{RED}" stroke-width="1.5"/>
  <line x1="335" y1="268" x2="365" y2="268" stroke="{RED}" stroke-width="1.5"/>
  <line x1="350" y1="285" x2="338" y2="310" stroke="{RED}" stroke-width="1.5"/>
  <line x1="350" y1="285" x2="362" y2="310" stroke="{RED}" stroke-width="1.5"/>
  <rect x="330" y="310" width="40" height="25" rx="3" fill="{PRIMARY_DARK}" stroke="{RED}" stroke-width="1.5"/>
  <text x="350" y="327" text-anchor="middle" font-family="Arial, sans-serif" font-size="8" fill="{WHITE}">A=500Дж</text>
  <text x="350" y="355" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="{RED}">t = 10 с</text>
  <text x="350" y="370" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="{RED}" font-weight="bold">N = 50 Вт</text>
  
  <!-- Comparison arrow -->
  <text x="235" y="310" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{PRIMARY}">Та же A,</text>
  <text x="235" y="326" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="{PRIMARY}">но N разная!</text>
'''
    
    # --- Right: Power of common devices ---
    svg += f'''
  <!-- Power table -->
  <text x="560" y="195" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="{PRIMARY}">Мощность устройств</text>
  <rect x="530" y="205" width="250" height="180" rx="6" fill="{BG2}" stroke="{GRID}" stroke-width="1"/>
  <text x="550" y="228" font-family="Arial, sans-serif" font-size="11" fill="{TEXT2}">Человек: ~75 Вт</text>
  <rect x="545" y="233" width="75" height="6" rx="3" fill="{CYAN}"/>
  
  <text x="550" y="258" font-family="Arial, sans-serif" font-size="11" fill="{TEXT2}">Лампочка: 60-100 Вт</text>
  <rect x="545" y="263" width="100" height="6" rx="3" fill="{PRIMARY}"/>
  
  <text x="550" y="288" font-family="Arial, sans-serif" font-size="11" fill="{TEXT2}">Утюг: ~2000 Вт</text>
  <rect x="545" y="293" width="180" height="6" rx="3" fill="{ARROW}"/>
  
  <text x="550" y="318" font-family="Arial, sans-serif" font-size="11" fill="{TEXT2}">Автомобиль: ~75 кВт</text>
  <rect x="545" y="323" width="220" height="6" rx="3" fill="{RED}"/>
  
  <text x="550" y="348" font-family="Arial, sans-serif" font-size="11" fill="{TEXT2}">Электровоз: ~5 МВт</text>
  <rect x="545" y="353" width="230" height="6" rx="3" fill="{RED}"/>
'''
    
    # --- Bottom info ---
    svg += info_box(30, 400, 250, 180, [
        "Мощность N = A / t:",
        "N — мощность [Вт]",
        "A — работа [Дж]",
        "t — время [с]",
      "",
      "1 Вт = 1 Дж/с",
      "1 кВт = 1000 Вт",
      "1 МВт = 1 000 000 Вт",
      "",
      "Мощность характеризует",
      "быстроту совершения",
      "работы.",
    ], "Определение")
    
    svg += info_box(300, 400, 250, 180, [
      "Примеры расчётов:",
      "",
      "1) A = 600 Дж, t = 30 с",
      "   N = 600/30 = 20 Вт",
      "",
      "2) N = 2 кВт, t = 10 с",
      "   A = N·t = 2000·10",
      "     = 20 000 Дж = 20 кДж",
      "",
      "3) v = 20 м/с, F = 500 Н",
      "   N = F·v = 500·20",
      "     = 10 000 Вт = 10 кВт",
    ], "Расчёты")
    
    svg += info_box(570, 400, 210, 180, [
      "Работа vs Мощность:",
      "",
      "Работа (A) — сколько",
      "совершено (Дж).",
      "",
      "Мощность (N) — как",
      "быстро совершено (Вт).",
      "",
      "A = N · t",
      "N = A / t",
      "",
      "Лошадиная сила:",
      "1 л.с. ≈ 735,5 Вт",
    ], "Сравнение")
    
    svg += "\n</svg>"
    return svg


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
        (8, generate_lesson8),
        (9, generate_lesson9),
    ]
    
    print(f"Generating {len(generators)} SVG files to {OUTPUT_DIR}/\n")
    
    all_valid = True
    for lesson_num, gen_func in generators:
        svg_content = gen_func()
        filepath = os.path.join(OUTPUT_DIR, f"lesson-{lesson_num}.svg")
        
        # Write file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"  ✓ Written: lesson-{lesson_num}.svg ({len(svg_content)} bytes)")
        
        # Validate with xml.etree.ElementTree
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            # Check dimensions
            w = root.get("width")
            h = root.get("height")
            assert w == "800", f"Width is {w}, expected 800"
            assert h == "600", f"Height is {h}, expected 600"
            print(f"    ✓ Valid XML, dimensions: {w}x{h}")
        except ET.ParseError as e:
            print(f"    ✗ XML PARSE ERROR: {e}")
            all_valid = False
        except AssertionError as e:
            print(f"    ✗ DIMENSION ERROR: {e}")
            all_valid = False
    
    print(f"\n{'='*60}")
    if all_valid:
        print("SUCCESS: All 9 SVG files generated and validated!")
    else:
        print("WARNING: Some SVG files had validation issues!")
    print(f"Output directory: {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
