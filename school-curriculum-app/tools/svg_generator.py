#!/usr/bin/env python3
"""
Reusable SVG lesson illustration generator for school-curriculum-app.
Creates 500x350 SVG files with detailed biological/scientific drawings.

Usage:
  python3 tools/svg_generator.py --grade 7 --subject biology --lesson 1 --title "Title" --output path/
  python3 tools/svg_generator.py --grade 7 --subject biology --all --output path/

Each lesson gets a unique illustration based on topic keywords.
"""

import os
import sys
import argparse
import json

# ═══════════════════════════════════════════════════════════════
# SVG Template System
# ═══════════════════════════════════════════════════════════════

SUBJECT_COLORS = {
    "biology": {"primary": "#2E7D32", "light": "#E8F5E9", "mid": "#C8E6C9", "accent": "#4CAF50", "bar": "Биология"},
    "chemistry": {"primary": "#1565C0", "light": "#E3F2FD", "mid": "#BBDEFB", "accent": "#2196F3", "bar": "Химия"},
    "physics": {"primary": "#E65100", "light": "#FFF3E0", "mid": "#FFE0B2", "accent": "#FF9800", "bar": "Физика"},
    "history": {"primary": "#8D6E63", "light": "#EFEBE9", "mid": "#D7CCC8", "accent": "#A1887F", "bar": "История"},
    "geography": {"primary": "#00695C", "light": "#E0F2F1", "mid": "#B2DFDB", "accent": "#009688", "bar": "География"},
    "default": {"primary": "#37474F", "light": "#ECEFF1", "mid": "#CFD8DC", "accent": "#607D8B", "bar": ""},
}


def svg_header(title, subtitle, colors):
    """Generate SVG header with gradient background, border, title, subtitle."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{colors['light']}"/>
      <stop offset="100%" stop-color="{colors['mid']}"/>
    </linearGradient>
  </defs>
  <rect width="500" height="350" fill="url(#bg)" rx="10"/>
  <rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="{colors['primary']}" stroke-width="2.5"/>
  <text x="250" y="30" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="{colors['primary']}" text-anchor="middle">{title}</text>
  <text x="250" y="46" font-family="Arial,sans-serif" font-size="10" fill="#888" text-anchor="middle">{subtitle}</text>
  <line x1="30" y1="52" x2="470" y2="52" stroke="{colors['primary']}" stroke-width="1.5" opacity="0.25"/>
'''


def svg_footer(grade, subject):
    """Generate SVG footer bar."""
    colors = SUBJECT_COLORS.get(subject, SUBJECT_COLORS["default"])
    bar_text = f"{colors['bar']} {grade} класс" if colors['bar'] else f"{grade} класс"
    return f'''
  <rect x="10" y="325" width="480" height="20" rx="4" fill="{colors['primary']}" opacity="0.85"/>
  <text x="250" y="339" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="white" font-weight="bold">{bar_text}</text>
</svg>'''


def info_box(x, y, w, h, lines, title=None, stroke="#2E7D32"):
    """Generate a white info box with text lines."""
    parts = [f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="white" stroke="{stroke}" stroke-width="1" opacity="0.9"/>']
    if title:
        parts.append(f'  <text x="{x+w//2}" y="{y+14}" font-family="Arial,sans-serif" font-size="8" fill="{stroke}" text-anchor="middle" font-weight="bold">{title}</text>')
        start_y = y + 26
    else:
        start_y = y + 14
    for i, line in enumerate(lines):
        parts.append(f'  <text x="{x+w//2}" y="{start_y + i*12}" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">{line}</text>')
    return '\n'.join(parts)


def label(x, y, text, size=8, color="#333", bold=False):
    """Generate a text label."""
    weight = ' font-weight="bold"' if bold else ''
    return f'  <text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" text-anchor="middle"{weight}>{text}</text>'


def arrow(x1, y1, x2, y2, color="#2E7D32", width=1.5):
    """Generate an arrow line."""
    import math
    dx = x2 - x1
    dy = y2 - y1
    length = math.sqrt(dx*dx + dy*dy)
    if length == 0:
        return ''
    ux, uy = dx/length, dy/length
    px, py = -uy, ux
    ax, ay = x2 - ux*4 + px*3, y2 - uy*4 + py*3
    bx, by = x2 - ux*4 - px*3, y2 - uy*4 - py*3
    return f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"/>\n  <polygon points="{x2},{y2} {ax},{ay} {bx},{by}" fill="{color}"/>'


# ═══════════════════════════════════════════════════════════════
# Grade 7 Biology — Zoology Illustrations (32 lessons)
# ═══════════════════════════════════════════════════════════════

def bio7_lesson1(title, sub):
    """Общая характеристика животного мира"""
    return svg_header(title, sub, SUBJECT_COLORS["biology"]) + '''
  <!-- Animal kingdom overview -->
  <!-- Central circle: Animal Kingdom -->
  <circle cx="250" cy="170" r="45" fill="#4CAF50" opacity="0.15" stroke="#2E7D32" stroke-width="2"/>
  <text x="250" y="165" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle" font-weight="bold">Царство</text>
  <text x="250" y="178" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle" font-weight="bold">Животные</text>

  <!-- Surrounding groups -->
  <g transform="translate(90,90)">
    <ellipse rx="40" ry="20" fill="#FF9800" opacity="0.2" stroke="#E65100" stroke-width="1.5"/>
    <text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">Простейшие</text>
  </g>
  <g transform="translate(410,90)">
    <ellipse rx="40" ry="20" fill="#9C27B0" opacity="0.2" stroke="#7B1FA2" stroke-width="1.5"/>
    <text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Черви</text>
  </g>
  <g transform="translate(90,250)">
    <ellipse rx="40" ry="20" fill="#00BCD4" opacity="0.2" stroke="#00838F" stroke-width="1.5"/>
    <text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#00838F" text-anchor="middle" font-weight="bold">Моллюски</text>
  </g>
  <g transform="translate(410,250)">
    <ellipse rx="40" ry="20" fill="#F44336" opacity="0.2" stroke="#C62828" stroke-width="1.5"/>
    <text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">Членистоногие</text>
  </g>
  <g transform="translate(250,85)">
    <ellipse rx="45" ry="18" fill="#2196F3" opacity="0.2" stroke="#1565C0" stroke-width="1.5"/>
    <text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">Кишечнополостные</text>
  </g>
  <g transform="translate(250,265)">
    <ellipse rx="35" ry="18" fill="#795548" opacity="0.2" stroke="#4E342E" stroke-width="1.5"/>
    <text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#4E342E" text-anchor="middle" font-weight="bold">Хордовые</text>
  </g>

  <!-- Connecting lines -->
  <line x1="125" y1="100" x2="210" y2="150" stroke="#999" stroke-width="0.8" stroke-dasharray="3,2"/>
  <line x1="375" y1="100" x2="290" y2="150" stroke="#999" stroke-width="0.8" stroke-dasharray="3,2"/>
  <line x1="125" y1="245" x2="210" y2="195" stroke="#999" stroke-width="0.8" stroke-dasharray="3,2"/>
  <line x1="375" y1="245" x2="290" y2="195" stroke="#999" stroke-width="0.8" stroke-dasharray="3,2"/>
  <line x1="250" y1="103" x2="250" y2="125" stroke="#999" stroke-width="0.8" stroke-dasharray="3,2"/>
  <line x1="250" y1="248" x2="250" y2="215" stroke="#999" stroke-width="0.8" stroke-dasharray="3,2"/>

  <!-- Key animal traits -->
  <rect x="50" y="290" width="400" height="28" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="302" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Гетеротрофы | Нет клеточной стенки | Ограниченный рост | Активное движение | Запасное вещество — гликоген</text>
  <text x="250" y="313" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Более 2 млн видов — самое крупное царство организмов</text>
''' + svg_footer(7, "biology")


def bio7_lesson2(title, sub):
    """Классификация животных и методы зоологии"""
    return svg_header(title, sub, SUBJECT_COLORS["biology"]) + '''
  <!-- Taxonomy hierarchy (left side) -->
  <g transform="translate(30,70)">
    <rect x="0" y="0" width="180" height="20" rx="3" fill="#2E7D32" opacity="0.8"/>
    <text x="90" y="14" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">Царство Животные</text>
    
    <rect x="10" y="25" width="160" height="18" rx="3" fill="#388E3C" opacity="0.7"/>
    <text x="90" y="38" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">Тип Хордовые</text>
    
    <rect x="20" y="48" width="140" height="18" rx="3" fill="#43A047" opacity="0.6"/>
    <text x="90" y="61" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">Класс Млекопитающие</text>
    
    <rect x="30" y="71" width="120" height="18" rx="3" fill="#4CAF50" opacity="0.5"/>
    <text x="90" y="84" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">Отряд Хищные</text>
    
    <rect x="40" y="94" width="100" height="18" rx="3" fill="#66BB6A" opacity="0.5"/>
    <text x="90" y="107" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Семейство Псовые</text>
    
    <rect x="50" y="117" width="80" height="18" rx="3" fill="#81C784" opacity="0.5"/>
    <text x="90" y="130" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Род Волки</text>
    
    <rect x="60" y="140" width="60" height="18" rx="3" fill="#A5D6A7" opacity="0.5" stroke="#2E7D32" stroke-width="1"/>
    <text x="90" y="153" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Вид</text>
  </g>

  <!-- Methods of zoology (right side) -->
  <g transform="translate(240,70)">
    <text x="110" y="10" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Методы зоологии</text>
    
    <!-- Magnifying glass - observation -->
    <g transform="translate(40,45)">
      <circle cx="0" cy="0" r="15" fill="none" stroke="#FF9800" stroke-width="2"/>
      <line x1="11" y1="11" x2="22" y2="22" stroke="#FF9800" stroke-width="3"/>
      <text x="0" y="30" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Наблюдение</text>
    </g>
    
    <!-- Test tube - experiment -->
    <g transform="translate(130,45)">
      <rect x="-6" y="-15" width="12" height="25" rx="2" fill="none" stroke="#E53935" stroke-width="1.5"/>
      <rect x="-5" y="0" width="10" height="9" rx="1" fill="#E53935" opacity="0.3"/>
      <text x="0" y="25" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Эксперимент</text>
    </g>
    
    <!-- Bones - comparative anatomy -->
    <g transform="translate(220,45)">
      <path d="M-10 5 Q-8 -10 0 -12 Q8 -10 10 5 L8 10 Q0 12 -8 10 Z" fill="none" stroke="#795548" stroke-width="1.5"/>
      <text x="0" y="25" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Сравнение</text>
    </g>
    
    <!-- DNA - molecular -->
    <g transform="translate(85,110)">
      <path d="M-20,-10 Q-10,-15 0,-10 Q10,-5 20,-10" stroke="#9C27B0" stroke-width="1.5" fill="none"/>
      <path d="M-20,-3 Q-10,-8 0,-3 Q10,2 20,-3" stroke="#9C27B0" stroke-width="1.5" fill="none"/>
      <line x1="-15" y1="-8" x2="-15" y2="-5" stroke="#CE93D8" stroke-width="1"/>
      <line x1="-5" y1="-12" x2="-5" y2="-5" stroke="#CE93D8" stroke-width="1"/>
      <line x1="5" y1="-8" x2="5" y2="-1" stroke="#CE93D8" stroke-width="1"/>
      <line x1="15" y1="-10" x2="15" y2="-4" stroke="#CE93D8" stroke-width="1"/>
      <text x="0" y="15" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Молекулярный</text>
    </g>
    
    <!-- Fossil - paleontology -->
    <g transform="translate(185,110)">
      <ellipse cx="0" cy="-5" rx="15" ry="10" fill="#D7CCC8" stroke="#795548" stroke-width="1.5"/>
      <path d="M-8,-8 Q0,-3 8,-8" stroke="#5D4037" stroke-width="1" fill="none"/>
      <path d="M-6,-2 Q0,3 6,-2" stroke="#5D4037" stroke-width="1" fill="none"/>
      <text x="0" y="15" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Палеонтология</text>
    </g>
  </g>

  <!-- Linnaeus portrait hint -->
  <g transform="translate(370,200)">
    <circle cx="0" cy="-15" r="20" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/>
    <text x="0" y="-12" font-family="Arial,sans-serif" font-size="7" fill="#F57F17" text-anchor="middle" font-weight="bold">К.Линней</text>
    <text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">1707-1778</text>
    <text x="0" y="15" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Система</text>
    <text x="0" y="24" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">классификации</text>
  </g>
''' + svg_footer(7, "biology")


def bio7_lesson3(title, sub):
    """Общая характеристика простейших"""
    return svg_header(title, sub, SUBJECT_COLORS["biology"]) + '''
  <!-- Three protozoa types -->
  <!-- Amoeba -->
  <g transform="translate(85,160)">
    <path d="M-25,10 Q-35,-5 -20,-20 Q-10,-30 5,-25 Q20,-30 25,-15 Q35,-5 25,10 Q15,25 0,22 Q-15,25 -25,10 Z" fill="#B2DFDB" stroke="#00897B" stroke-width="2"/>
    <!-- Nucleus -->
    <ellipse cx="2" cy="-2" rx="8" ry="6" fill="#80CBC4" stroke="#00695C" stroke-width="1.5"/>
    <circle cx="2" cy="-2" r="3" fill="#4DB6AC"/>
    <!-- Pseudopods -->
    <path d="M-30,0 Q-45,5 -38,-5" fill="#B2DFDB" stroke="#00897B" stroke-width="1.5"/>
    <path d="M20,-20 Q30,-30 25,-15" fill="#B2DFDB" stroke="#00897B" stroke-width="1.5"/>
    <path d="M-10,20 Q-15,35 -5,28" fill="#B2DFDB" stroke="#00897B" stroke-width="1.5"/>
    <!-- Contractile vacuole -->
    <circle cx="15" cy="8" r="4" fill="#E0F7FA" stroke="#00BCD4" stroke-width="1"/>
    <!-- Food vacuole -->
    <circle cx="-10" cy="8" r="5" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1" opacity="0.6"/>
    <text x="0" y="48" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Амёба</text>
    <text x="0" y="58" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Ложноножки</text>
  </g>

  <!-- Euglena -->
  <g transform="translate(250,160)">
    <ellipse cx="0" cy="0" rx="30" ry="12" fill="#C8E6C9" stroke="#388E3C" stroke-width="2"/>
    <!-- Flagellum -->
    <path d="M28,-3 Q45,-15 50,-25 Q48,-20 55,-30" stroke="#388E3C" stroke-width="1.5" fill="none"/>
    <!-- Eye spot -->
    <circle cx="20" cy="-4" r="3" fill="#F44336" opacity="0.7"/>
    <!-- Chloroplasts -->
    <ellipse cx="-5" cy="-3" rx="6" ry="3" fill="#66BB6A" opacity="0.6"/>
    <ellipse cx="5" cy="4" rx="5" ry="2.5" fill="#66BB6A" opacity="0.6"/>
    <!-- Nucleus -->
    <circle cx="-10" cy="0" r="4" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
    <!-- Contractile vacuole -->
    <circle cx="15" cy="-2" r="3" fill="#E0F7FA" stroke="#00BCD4" stroke-width="0.8"/>
    <text x="0" y="30" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Эвглена</text>
    <text x="0" y="40" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Жгутик + хлоропласты</text>
  </g>

  <!-- Paramecium -->
  <g transform="translate(415,160)">
    <ellipse cx="0" cy="0" rx="18" ry="35" fill="#E1BEE7" stroke="#7B1FA2" stroke-width="2"/>
    <!-- Cilia -->
    <line x1="-18" y1="-20" x2="-24" y2="-22" stroke="#9C27B0" stroke-width="0.8"/>
    <line x1="-19" y1="-10" x2="-25" y2="-11" stroke="#9C27B0" stroke-width="0.8"/>
    <line x1="-19" y1="0" x2="-26" y2="0" stroke="#9C27B0" stroke-width="0.8"/>
    <line x1="-18" y1="10" x2="-24" y2="11" stroke="#9C27B0" stroke-width="0.8"/>
    <line x1="-16" y1="20" x2="-22" y2="22" stroke="#9C27B0" stroke-width="0.8"/>
    <line x1="18" y1="-20" x2="24" y2="-22" stroke="#9C27B0" stroke-width="0.8"/>
    <line x1="19" y1="-10" x2="25" y2="-11" stroke="#9C27B0" stroke-width="0.8"/>
    <line x1="19" y1="0" x2="26" y2="0" stroke="#9C27B0" stroke-width="0.8"/>
    <line x1="18" y1="10" x2="24" y2="11" stroke="#9C27B0" stroke-width="0.8"/>
    <line x1="16" y1="20" x2="22" y2="22" stroke="#9C27B0" stroke-width="0.8"/>
    <!-- Oral groove -->
    <path d="M-10,-15 Q-15,0 -8,15" stroke="#6A1B9A" stroke-width="1.5" fill="none"/>
    <!-- Macronucleus -->
    <ellipse cx="2" cy="-5" rx="8" ry="5" fill="#CE93D8" stroke="#6A1B9A" stroke-width="1"/>
    <!-- Micronucleus -->
    <circle cx="5" cy="3" r="3" fill="#AB47BC" stroke="#6A1B9A" stroke-width="1"/>
    <!-- Contractile vacuoles -->
    <circle cx="-5" cy="-18" r="4" fill="#E0F7FA" stroke="#00BCD4" stroke-width="0.8"/>
    <circle cx="-3" cy="18" r="4" fill="#E0F7FA" stroke="#00BCD4" stroke-width="0.8"/>
    <text x="0" y="50" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Инфузория</text>
    <text x="0" y="60" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Реснички</text>
  </g>

  <!-- Common features box -->
  <rect x="40" y="260" width="420" height="55" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="276" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Общие признаки простейших</text>
  <text x="250" y="290" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Одна клетка = целый организм | Эукариоты | Гетеротрофы (или миксотрофы)</text>
  <text x="250" y="302" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Сократительная вакуоль | Инцистирование при неблагоприятных условиях</text>
''' + svg_footer(7, "biology")


def bio7_lesson4(title, sub):
    """Общая характеристика кишечнополостных"""
    return svg_header(title, sub, SUBJECT_COLORS["biology"]) + '''
  <!-- Hydra - radial symmetry -->
  <g transform="translate(150,185)">
    <!-- Body column -->
    <path d="M-15,-60 Q-18,-20 -20,30 Q-15,50 0,55 Q15,50 20,30 Q18,-20 15,-60 Z" fill="#FFCDD2" stroke="#E53935" stroke-width="2"/>
    <!-- Tentacles -->
    <path d="M-15,-60 Q-35,-80 -30,-95" stroke="#EF5350" stroke-width="2" fill="none"/>
    <path d="M-8,-62 Q-20,-85 -15,-100" stroke="#EF5350" stroke-width="2" fill="none"/>
    <path d="M0,-64 Q0,-90 0,-105" stroke="#EF5350" stroke-width="2" fill="none"/>
    <path d="M8,-62 Q20,-85 15,-100" stroke="#EF5350" stroke-width="2" fill="none"/>
    <path d="M15,-60 Q35,-80 30,-95" stroke="#EF5350" stroke-width="2" fill="none"/>
    <!-- Mouth/hypostome -->
    <ellipse cx="0" cy="-55" rx="8" ry="5" fill="#FFCDD2" stroke="#C62828" stroke-width="1.5"/>
    <!-- Budding hydra -->
    <g transform="translate(18,0)">
      <path d="M0,0 Q5,-15 3,-25 Q0,-30 -3,-25 Q-5,-15 0,0" fill="#FFCDD2" stroke="#E53935" stroke-width="1.2"/>
      <path d="M3,-25 Q10,-32 8,-38" stroke="#EF5350" stroke-width="1" fill="none"/>
      <path d="M-3,-25 Q-10,-32 -8,-38" stroke="#EF5350" stroke-width="1" fill="none"/>
    </g>
    <!-- Nematocysts on tentacles -->
    <circle cx="-30" cy="-93" r="2" fill="#FFAB91" stroke="#E53935" stroke-width="0.5"/>
    <circle cx="-15" cy="-98" r="2" fill="#FFAB91" stroke="#E53935" stroke-width="0.5"/>
    <circle cx="0" cy="-103" r="2" fill="#FFAB91" stroke="#E53935" stroke-width="0.5"/>
    <!-- Labels -->
    <text x="-55" y="-65" font-family="Arial,sans-serif" font-size="6" fill="#C62828">Щупальца</text>
    <text x="-55" y="-30" font-family="Arial,sans-serif" font-size="6" fill="#C62828">Эктодерма</text>
    <text x="-55" y="-20" font-family="Arial,sans-serif" font-size="6" fill="#C62828">Энтодерма</text>
    <text x="-55" y="40" font-family="Arial,sans-serif" font-size="6" fill="#C62828">Подошва</text>
    <text x="28" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#C62828">Почкование</text>
  </g>

  <!-- Body wall detail (cross-section) -->
  <g transform="translate(380,170)">
    <rect x="-50" y="-60" width="100" height="120" rx="5" fill="white" stroke="#E53935" stroke-width="1.5"/>
    <text x="0" y="-45" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">Стенка тела</text>
    <!-- Three layers -->
    <rect x="-35" y="-35" width="70" height="18" rx="3" fill="#FFCDD2" stroke="#E53935" stroke-width="1"/>
    <text x="0" y="-23" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">Эктодерма</text>
    <rect x="-35" y="-14" width="70" height="14" rx="3" fill="#FFECB3" stroke="#FF8F00" stroke-width="1"/>
    <text x="0" y="-4" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Мезоглея</text>
    <rect x="-35" y="2" width="70" height="18" rx="3" fill="#FFCDD2" stroke="#E53935" stroke-width="1"/>
    <text x="0" y="14" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">Энтодерма</text>
    <!-- Nematocyst detail -->
    <g transform="translate(0,38)">
      <circle cx="0" cy="0" r="5" fill="#FFAB91" stroke="#E53935" stroke-width="1"/>
      <line x1="0" y1="0" x2="8" y2="-8" stroke="#E53935" stroke-width="0.8"/>
      <text x="0" y="15" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">Стрекательная</text>
      <text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">клетка</text>
    </g>
  </g>
''' + svg_footer(7, "biology")


def bio7_lesson5(title, sub):
    """Многообразие кишечнополостных"""
    return svg_header(title, sub, SUBJECT_COLORS["biology"]) + '''
  <!-- Three classes of coelenterates -->
  <!-- Hydrozoa (Hydra) -->
  <g transform="translate(85,170)">
    <path d="M-10,-50 Q-12,-10 -14,25 Q-10,40 0,42 Q10,40 14,25 Q12,-10 10,-50 Z" fill="#FFCDD2" stroke="#E53935" stroke-width="1.5"/>
    <path d="M-10,-50 Q-25,-65 -22,-75" stroke="#EF5350" stroke-width="1.5" fill="none"/>
    <path d="M0,-52 Q0,-70 0,-80" stroke="#EF5350" stroke-width="1.5" fill="none"/>
    <path d="M10,-50 Q25,-65 22,-75" stroke="#EF5350" stroke-width="1.5" fill="none"/>
    <text x="0" y="58" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Гидроидные</text>
    <text x="0" y="68" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Гидра</text>
  </g>

  <!-- Scyphozoa (Jellyfish) -->
  <g transform="translate(250,170)">
    <!-- Bell -->
    <path d="M-40,10 Q-45,-25 -30,-45 Q0,-60 30,-45 Q45,-25 40,10 Q20,15 0,12 Q-20,15 -40,10 Z" fill="#E1BEE7" stroke="#7B1FA2" stroke-width="2"/>
    <!-- Inner bell -->
    <path d="M-30,5 Q-30,-20 -15,-35 Q0,-42 15,-35 Q30,-20 30,5 Q15,8 0,6 Q-15,8 -30,5 Z" fill="#CE93D8" opacity="0.3"/>
    <!-- Tentacles -->
    <path d="M-35,10 Q-40,35 -30,55" stroke="#9C27B0" stroke-width="1.5" fill="none"/>
    <path d="M-20,12 Q-25,40 -15,60" stroke="#9C27B0" stroke-width="1.5" fill="none"/>
    <path d="M0,14 Q0,42 5,62" stroke="#9C27B0" stroke-width="1.5" fill="none"/>
    <path d="M20,12 Q25,40 15,60" stroke="#9C27B0" stroke-width="1.5" fill="none"/>
    <path d="M35,10 Q40,35 30,55" stroke="#9C27B0" stroke-width="1.5" fill="none"/>
    <!-- Oral arms -->
    <path d="M-12,12 Q-18,30 -10,45" stroke="#6A1B9A" stroke-width="2" fill="none"/>
    <path d="M12,12 Q18,30 10,45" stroke="#6A1B9A" stroke-width="2" fill="none"/>
    <text x="0" y="78" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Сцифоидные</text>
    <text x="0" y="88" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Медуза</text>
  </g>

  <!-- Anthozoa (Sea anemone / Coral) -->
  <g transform="translate(415,170)">
    <!-- Coral / Sea anemone base -->
    <path d="M-30,35 Q-35,10 -25,-10 Q-15,-25 0,-30 Q15,-25 25,-10 Q35,10 30,35 Z" fill="#FFCC80" stroke="#E65100" stroke-width="2"/>
    <!-- Tentacles crown -->
    <path d="M-25,-10 Q-40,-30 -30,-45" stroke="#FF9800" stroke-width="2" fill="none"/>
    <path d="M-15,-22 Q-25,-45 -15,-55" stroke="#FF9800" stroke-width="2" fill="none"/>
    <path d="M0,-30 Q0,-55 5,-65" stroke="#FF9800" stroke-width="2" fill="none"/>
    <path d="M15,-22 Q25,-45 15,-55" stroke="#FF9800" stroke-width="2" fill="none"/>
    <path d="M25,-10 Q40,-30 30,-45" stroke="#FF9800" stroke-width="2" fill="none"/>
    <!-- Mouth -->
    <ellipse cx="0" cy="-28" rx="5" ry="3" fill="#FFF3E0" stroke="#E65100" stroke-width="1"/>
    <text x="0" y="55" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Кораллы</text>
    <text x="0" y="65" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Актинии, рифы</text>
  </g>

  <!-- Info box -->
  <rect x="30" y="260" width="440" height="55" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="278" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Общие признаки кишечнополостных</text>
  <text x="250" y="292" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Двухслойные (эктодерма + энтодерма) | Радиальная симметрия | Кишечная полость</text>
  <text x="250" y="304" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Стрекательные клетки | Два жизненных поколения: полип и медуза</text>
''' + svg_footer(7, "biology")


def bio7_lesson6(title, sub):
    """Плоские черви"""
    return svg_header(title, sub, SUBJECT_COLORS["biology"]) + '''
  <!-- Planaria (free-living) -->
  <g transform="translate(120,145)">
    <path d="M-35,0 Q-45,-15 -35,-12 Q-25,-15 -15,0 Q0,10 20,5 Q35,0 45,-5 Q50,-10 45,-5 Q35,5 20,10 Q0,15 -15,5 Q-25,15 -35,12 Q-45,15 -35,0 Z" fill="#A5D6A7" stroke="#2E7D32" stroke-width="2"/>
    <!-- Triangular head -->
    <path d="M-35,0 L-50,-10 L-50,10 Z" fill="#81C784" stroke="#2E7D32" stroke-width="1.5"/>
    <!-- Eyespots -->
    <circle cx="-42" cy="-4" r="3" fill="#333" stroke="#000" stroke-width="0.5"/>
    <circle cx="-42" cy="4" r="3" fill="#333" stroke="#000" stroke-width="0.5"/>
    <!-- Pharynx -->
    <ellipse cx="0" cy="0" rx="5" ry="8" fill="#66BB6A" stroke="#1B5E20" stroke-width="1"/>
    <!-- Branching gut -->
    <path d="M5,-3 Q20,-8 35,-5" stroke="#4CAF50" stroke-width="1" fill="none"/>
    <path d="M5,3 Q20,8 35,5" stroke="#4CAF50" stroke-width="1" fill="none"/>
    <text x="0" y="25" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Планария</text>
    <text x="0" y="34" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Свободноживущий</text>
  </g>

  <!-- Liver fluke -->
  <g transform="translate(300,145)">
    <path d="M-20,-25 Q-30,-15 -25,0 Q-30,15 -20,25 Q0,35 20,25 Q30,15 25,0 Q30,-15 20,-25 Q0,-35 -20,-25 Z" fill="#FFCC80" stroke="#E65100" stroke-width="2"/>
    <!-- Oral sucker -->
    <circle cx="-18" cy="-15" r="6" fill="#FFE0B2" stroke="#BF360C" stroke-width="1.5"/>
    <!-- Ventral sucker -->
    <circle cx="-10" cy="0" r="5" fill="#FFE0B2" stroke="#BF360C" stroke-width="1.5"/>
    <!-- Branching gut -->
    <path d="M-12,-18 Q5,-25 20,-20" stroke="#BF360C" stroke-width="1" fill="none"/>
    <path d="M-12,0 Q5,-5 20,0" stroke="#BF360C" stroke-width="1" fill="none"/>
    <path d="M-12,5 Q0,15 15,18" stroke="#BF360C" stroke-width="1" fill="none"/>
    <text x="0" y="40" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Печёночный сосальщик</text>
    <text x="0" y="49" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Паразит</text>
  </g>

  <!-- Tapeworm -->
  <g transform="translate(430,145)">
    <!-- Scolex -->
    <circle cx="0" cy="-20" r="10" fill="#FFECB3" stroke="#F57F17" stroke-width="1.5"/>
    <!-- Hooks -->
    <circle cx="-5" cy="-28" r="2" fill="#F57F17"/>
    <circle cx="5" cy="-28" r="2" fill="#F57F17"/>
    <!-- Suckers -->
    <circle cx="-5" cy="-18" r="3" fill="#FFE082" stroke="#F57F17" stroke-width="1"/>
    <circle cx="5" cy="-18" r="3" fill="#FFE082" stroke="#F57F17" stroke-width="1"/>
    <!-- Proglottids -->
    <rect x="-8" y="-8" width="16" height="8" rx="2" fill="#FFF9C4" stroke="#F9A825" stroke-width="1"/>
    <rect x="-8" y="2" width="16" height="8" rx="2" fill="#FFF9C4" stroke="#F9A825" stroke-width="1"/>
    <rect x="-9" y="12" width="18" height="10" rx="2" fill="#FFF9C4" stroke="#F9A825" stroke-width="1"/>
    <text x="0" y="35" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Бычий цепень</text>
    <text x="0" y="44" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Паразит</text>
  </g>

  <!-- Life cycle hint -->
  <rect x="30" y="210" width="440" height="55" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="226" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Особенности плоских червей</text>
  <text x="250" y="240" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Трёхслойные (эктодерма, мезодерма, энтодерма) | Двусторонняя симметрия</text>
  <text x="250" y="252" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Кожно-мускульный мешок | Паразиты имеют присоски и крючья | Нет пищеварения у цепней</text>
''' + svg_footer(7, "biology")


def bio7_lesson7(title, sub):
    """Круглые черви"""
    return svg_header(title, sub, SUBJECT_COLORS["biology"]) + '''
  <!-- Ascaris (roundworm) -->
  <g transform="translate(160,175)">
    <!-- Body - cylindrical, tapered ends -->
    <path d="M-70,0 Q-80,-8 -70,-10 Q-40,-14 0,-14 Q40,-14 70,-10 Q80,-8 70,0 Q80,8 70,10 Q40,14 0,14 Q-40,14 -70,10 Q-80,8 -70,0 Z" fill="#FFECB3" stroke="#F57F17" stroke-width="2"/>
    <!-- Head end -->
    <ellipse cx="-75" cy="0" rx="8" ry="6" fill="#FFF9C4" stroke="#F57F17" stroke-width="1.5"/>
    <!-- Mouth -->
    <circle cx="-80" cy="0" r="2" fill="#F57F17"/>
    <!-- Tail (curved) -->
    <path d="M70,0 Q80,0 85,-5 Q88,-10 82,-12" stroke="#F57F17" stroke-width="2" fill="none"/>
    <!-- Internal structure -->
    <line x1="-65" y1="0" x2="65" y2="0" stroke="#FFE082" stroke-width="1.5" stroke-dasharray="4,2"/>
    <!-- Labels -->
    <line x1="0" y1="-20" x2="0" y2="-30" stroke="#666" stroke-width="0.5"/>
    <text x="0" y="-33" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Кишечник</text>
    <line x1="-50" y1="-16" x2="-50" y2="-28" stroke="#666" stroke-width="0.5"/>
    <text x="-50" y="-31" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Глотка</text>
    <!-- Cuticle label -->
    <text x="0" y="28" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Аскарида</text>
    <text x="0" y="38" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Раздельнополая, кутикула</text>
  </g>

  <!-- Cross-section -->
  <g transform="translate(390,170)">
    <circle cx="0" cy="0" r="45" fill="#FFF9C4" stroke="#F57F17" stroke-width="2"/>
    <!-- Cuticle -->
    <circle cx="0" cy="0" r="42" fill="none" stroke="#FFB300" stroke-width="2"/>
    <!-- Muscles -->
    <circle cx="0" cy="0" r="36" fill="#FFECB3" stroke="#F57F17" stroke-width="0.8" stroke-dasharray="3,2"/>
    <!-- Pseudocoelom label -->
    <text x="0" y="-15" font-family="Arial,sans-serif" font-size="6" fill="#F57F17" text-anchor="middle">Первичная</text>
    <text x="0" y="-7" font-family="Arial,sans-serif" font-size="6" fill="#F57F17" text-anchor="middle">полость</text>
    <!-- Intestine -->
    <ellipse cx="0" cy="8" rx="10" ry="7" fill="#FFE082" stroke="#F57F17" stroke-width="1"/>
    <!-- Oviducts -->
    <ellipse cx="-18" cy="-2" rx="6" ry="4" fill="#F8BBD0" stroke="#C2185B" stroke-width="1" opacity="0.6"/>
    <ellipse cx="18" cy="-2" rx="6" ry="4" fill="#F8BBD0" stroke="#C2185B" stroke-width="1" opacity="0.6"/>
    <text x="0" y="58" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Поперечный срез</text>
  </g>

  <!-- Info box -->
  <rect x="30" y="250" width="440" height="65" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="266" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Признаки круглых червей</text>
  <text x="250" y="280" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Цилиндрическое тело, заострённое на концах | Кутикула (покров)</text>
  <text x="250" y="292" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Первичная полость тела (псевдоцель) | Раздельнополые</text>
  <text x="250" y="304" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Сквозной кишечник (рот + анальное отверстие) | 20+ тыс. видов</text>
''' + svg_footer(7, "biology")


def bio7_lesson8(title, sub):
    """Кольчатые черви"""
    return svg_header(title, sub, SUBJECT_COLORS["biology"]) + '''
  <!-- Earthworm -->
  <g transform="translate(250,150)">
    <!-- Segmented body -->
    <path d="M-100,-10 Q-110,-5 -105,0 Q-110,5 -100,10 L100,10 Q110,5 105,0 Q110,-5 100,-10 Z" fill="#D7CCC8" stroke="#5D4037" stroke-width="2"/>
    <!-- Segments (rings) -->
    <line x1="-80" y1="-10" x2="-80" y2="10" stroke="#8D6E63" stroke-width="0.8"/>
    <line x1="-60" y1="-10" x2="-60" y2="10" stroke="#8D6E63" stroke-width="0.8"/>
    <line x1="-40" y1="-10" x2="-40" y2="10" stroke="#8D6E63" stroke-width="0.8"/>
    <line x1="-20" y1="-10" x2="-20" y2="10" stroke="#8D6E63" stroke-width="0.8"/>
    <line x1="0" y1="-10" x2="0" y2="10" stroke="#8D6E63" stroke-width="0.8"/>
    <line x1="20" y1="-10" x2="20" y2="10" stroke="#8D6E63" stroke-width="0.8"/>
    <line x1="40" y1="-10" x2="40" y2="10" stroke="#8D6E63" stroke-width="0.8"/>
    <line x1="60" y1="-10" x2="60" y2="10" stroke="#8D6E63" stroke-width="0.8"/>
    <line x1="80" y1="-10" x2="80" y2="10" stroke="#8D6E63" stroke-width="0.8"/>
    <!-- Clitellum (girdle) -->
    <rect x="-15" y="-12" width="35" height="24" rx="5" fill="#BCAAA4" stroke="#5D4037" stroke-width="1.5"/>
    <text x="2" y="3" font-family="Arial,sans-serif" font-size="5" fill="#3E2723" text-anchor="middle">Поясок</text>
    <!-- Setae -->
    <line x1="-70" y1="10" x2="-72" y2="16" stroke="#5D4037" stroke-width="1"/>
    <line x1="-50" y1="10" x2="-52" y2="16" stroke="#5D4037" stroke-width="1"/>
    <line x1="-30" y1="10" x2="-32" y2="16" stroke="#5D4037" stroke-width="1"/>
    <line x1="30" y1="10" x2="28" y2="16" stroke="#5D4037" stroke-width="1"/>
    <line x1="50" y1="10" x2="48" y2="16" stroke="#5D4037" stroke-width="1"/>
    <line x1="70" y1="10" x2="68" y2="16" stroke="#5D4037" stroke-width="1"/>
    <text x="0" y="35" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Дождевой червь</text>
    <text x="0" y="45" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Кольчатые сегменты, щетинки</text>
  </g>

  <!-- Cross-section of annelid -->
  <g transform="translate(120,250)">
    <circle cx="0" cy="0" r="30" fill="#EFEBE9" stroke="#5D4037" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="25" fill="#D7CCC8" stroke="#8D6E63" stroke-width="1"/>
    <circle cx="0" cy="0" r="15" fill="#BCAAA4" stroke="#8D6E63" stroke-width="0.8"/>
    <ellipse cx="0" cy="0" rx="7" ry="5" fill="#A1887F" stroke="#5D4037" stroke-width="1"/>
    <text x="0" y="3" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle">Кишка</text>
    <text x="0" y="40" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Вторичная полость</text>
  </g>

  <!-- Nereis (marine polychaete) -->
  <g transform="translate(400,250)">
    <path d="M-40,-5 Q-50,-3 -45,0 Q-50,3 -40,5 L40,5 Q50,3 45,0 Q50,-3 40,-5 Z" fill="#B2DFDB" stroke="#00695C" stroke-width="1.5"/>
    <!-- Parapodia with setae -->
    <path d="M-30,-5 L-35,-15" stroke="#00897B" stroke-width="1"/>
    <path d="M-30,5 L-35,15" stroke="#00897B" stroke-width="1"/>
    <path d="M-10,-5 L-15,-15" stroke="#00897B" stroke-width="1"/>
    <path d="M-10,5 L-15,15" stroke="#00897B" stroke-width="1"/>
    <path d="M10,-5 L5,-15" stroke="#00897B" stroke-width="1"/>
    <path d="M10,5 L5,15" stroke="#00897B" stroke-width="1"/>
    <path d="M30,-5 L25,-15" stroke="#00897B" stroke-width="1"/>
    <path d="M30,5 L25,15" stroke="#00897B" stroke-width="1"/>
    <!-- Head with eyes and antennae -->
    <circle cx="-45" cy="0" r="5" fill="#E0F2F1" stroke="#00695C" stroke-width="1"/>
    <path d="M-48,-3 L-55,-8" stroke="#00695C" stroke-width="1"/>
    <path d="M-48,3 L-55,8" stroke="#00695C" stroke-width="1"/>
    <text x="0" y="25" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Нереис</text>
    <text x="0" y="34" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Морской, параподии</text>
  </g>
''' + svg_footer(7, "biology")


def bio7_lesson9(title, sub):
    """Общая характеристика моллюсков"""
    return svg_header(title, sub, SUBJECT_COLORS["biology"]) + '''
  <!-- Mollusk body plan -->
  <g transform="translate(160,180)">
    <!-- Shell -->
    <path d="M-50,30 Q-60,-10 -40,-40 Q-20,-60 0,-60 Q20,-60 40,-40 Q60,-10 50,30 Z" fill="#FFE0B2" stroke="#E65100" stroke-width="2"/>
    <path d="M-42,25 Q-50,-5 -32,-32 Q-15,-50 0,-50 Q15,-50 32,-32 Q50,-5 42,25" fill="none" stroke="#FF8F00" stroke-width="1" opacity="0.5"/>
    <path d="M-34,20 Q-40,0 -25,-22 Q-10,-38 0,-38 Q10,-38 25,-22 Q40,0 34,20" fill="none" stroke="#FF8F00" stroke-width="1" opacity="0.5"/>
    <!-- Mantle visible -->
    <path d="M-45,30 Q-50,10 -35,-25 Q-15,-50 5,-50 Q25,-50 40,-25 Q55,10 45,30" fill="#FFECB3" stroke="#FFB300" stroke-width="1.5" opacity="0.6"/>
    <!-- Foot -->
    <path d="M-35,30 Q-40,45 -25,50 Q0,55 25,50 Q40,45 35,30 Z" fill="#FFCC80" stroke="#E65100" stroke-width="1.5"/>
    <!-- Head with tentacles -->
    <g transform="translate(-20,-55)">
      <line x1="0" y1="0" x2="-8" y2="-15" stroke="#BF360C" stroke-width="1.5"/>
      <line x1="10" y1="0" x2="2" y2="-15" stroke="#BF360C" stroke-width="1.5"/>
      <circle cx="-8" cy="-16" r="2" fill="#333"/>
      <circle cx="2" cy="-16" r="2" fill="#333"/>
    </g>
    <!-- Labels -->
    <text x="0" y="65" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">Раковина</text>
  </g>

  <!-- Internal structure diagram -->
  <g transform="translate(380,170)">
    <rect x="-55" y="-70" width="110" height="140" rx="5" fill="white" stroke="#E65100" stroke-width="1.5"/>
    <text x="0" y="-55" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">Органы моллюска</text>
    <!-- Heart -->
    <g transform="translate(-20,-30)">
      <path d="M0,-5 Q-5,-10 -3,-5 Q-5,0 0,5 Q5,0 3,-5 Q5,-10 0,-5 Z" fill="#E53935" stroke="#C62828" stroke-width="1"/>
      <text x="15" y="-2" font-family="Arial,sans-serif" font-size="5" fill="#333">Сердце</text>
    </g>
    <!-- Kidney -->
    <rect x="10" y="-38" width="15" height="10" rx="2" fill="#A5D6A7" stroke="#2E7D32" stroke-width="0.8"/>
    <text x="35" y="-31" font-family="Arial,sans-serif" font-size="5" fill="#333">Почка</text>
    <!-- Digestive -->
    <ellipse cx="-10" cy="-8" rx="12" ry="6" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
    <text x="10" y="-6" font-family="Arial,sans-serif" font-size="5" fill="#333">Печень</text>
    <!-- Gill/Lung -->
    <ellipse cx="-20" cy="15" rx="10" ry="8" fill="#BBDEFB" stroke="#1565C0" stroke-width="0.8"/>
    <text x="5" y="18" font-family="Arial,sans-serif" font-size="5" fill="#333">Жабра/лёгкое</text>
    <!-- Gonad -->
    <ellipse cx="5" cy="30" rx="10" ry="6" fill="#F8BBD0" stroke="#C2185B" stroke-width="0.8"/>
    <text x="25" y="33" font-family="Arial,sans-serif" font-size="5" fill="#333">Половая</text>
    <!-- Nervous -->
    <circle cx="-25" cy="45" r="4" fill="#CE93D8" stroke="#7B1FA2" stroke-width="0.8"/>
    <circle cx="15" cy="45" r="4" fill="#CE93D8" stroke="#7B1FA2" stroke-width="0.8"/>
    <line x1="-21" y1="45" x2="11" y2="45" stroke="#7B1FA2" stroke-width="0.8"/>
    <text x="-5" y="58" font-family="Arial,sans-serif" font-size="5" fill="#333">Нервные узлы</text>
  </g>
''' + svg_footer(7, "biology")


def bio7_lesson10(title, sub):
    """Многообразие и значение моллюсков"""
    return svg_header(title, sub, SUBJECT_COLORS["biology"]) + '''
  <!-- Gastropod (Snail) -->
  <g transform="translate(85,170)">
    <path d="M-15,25 Q-30,10 -25,-10 Q-20,-25 -10,-30 Q0,-35 10,-30 Q20,-20 15,-5 Q10,5 5,10" fill="#FFCC80" stroke="#E65100" stroke-width="2"/>
    <path d="M-10,-20 Q-5,-25 5,-25 Q12,-20 8,-10 Q5,-5 0,0" fill="none" stroke="#FF8F00" stroke-width="0.8" opacity="0.6"/>
    <!-- Body/foot -->
    <path d="M-15,25 Q-25,30 -20,35 Q0,40 20,35 Q25,30 15,25" fill="#FFE0B2" stroke="#BF360C" stroke-width="1.5"/>
    <!-- Head + tentacles -->
    <circle cx="-22" cy="20" r="6" fill="#FFE0B2" stroke="#BF360C" stroke-width="1"/>
    <line x1="-24" y1="16" x2="-28" y2="6" stroke="#BF360C" stroke-width="1.2"/>
    <line x1="-20" y1="16" x2="-16" y2="6" stroke="#BF360C" stroke-width="1.2"/>
    <circle cx="-28" cy="5" r="1.5" fill="#333"/>
    <circle cx="-16" cy="5" r="1.5" fill="#333"/>
    <text x="0" y="52" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Брюхоногие</text>
  </g>

  <!-- Bivalve -->
  <g transform="translate(250,170)">
    <!-- Left valve -->
    <path d="M-5,-35 Q-40,-30 -45,0 Q-40,30 -5,35 Z" fill="#FFECB3" stroke="#F57F17" stroke-width="2"/>
    <!-- Right valve -->
    <path d="M5,-35 Q40,-30 45,0 Q40,30 5,35 Z" fill="#FFF9C4" stroke="#F57F17" stroke-width="2"/>
    <!-- Hinge -->
    <line x1="0" y1="-35" x2="0" y2="35" stroke="#F57F17" stroke-width="2"/>
    <!-- Growth lines -->
    <path d="M-5,-25 Q-30,-20 -35,0" fill="none" stroke="#FFB300" stroke-width="0.5" opacity="0.5"/>
    <path d="M5,-25 Q30,-20 35,0" fill="none" stroke="#FFB300" stroke-width="0.5" opacity="0.5"/>
    <!-- Siphons -->
    <g transform="translate(0,-40)">
      <rect x="-8" y="-12" width="6" height="12" rx="2" fill="#FFE082" stroke="#F57F17" stroke-width="1"/>
      <rect x="2" y="-12" width="6" height="12" rx="2" fill="#FFE082" stroke="#F57F17" stroke-width="1"/>
    </g>
    <!-- Foot -->
    <path d="M-8,35 Q0,45 8,35" fill="#FFCC80" stroke="#BF360C" stroke-width="1"/>
    <text x="0" y="55" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Двустворчатые</text>
  </g>

  <!-- Cephalopod (Squid) -->
  <g transform="translate(415,170)">
    <!-- Mantle -->
    <path d="M-15,-40 Q-25,-20 -20,10 Q-15,25 0,30 Q15,25 20,10 Q25,-20 15,-40 Z" fill="#E1BEE7" stroke="#7B1FA2" stroke-width="2"/>
    <!-- Head -->
    <circle cx="0" cy="-45" r="15" fill="#CE93D8" stroke="#7B1FA2" stroke-width="1.5"/>
    <!-- Eyes -->
    <circle cx="-10" cy="-47" r="5" fill="#F3E5F5" stroke="#4A148C" stroke-width="1"/>
    <circle cx="-10" cy="-47" r="2" fill="#333"/>
    <circle cx="10" cy="-47" r="5" fill="#F3E5F5" stroke="#4A148C" stroke-width="1"/>
    <circle cx="10" cy="-47" r="2" fill="#333"/>
    <!-- Tentacles -->
    <path d="M-12,30 Q-20,45 -15,55" stroke="#9C27B0" stroke-width="1.5" fill="none"/>
    <path d="M-6,32 Q-10,50 -5,58" stroke="#9C27B0" stroke-width="1.5" fill="none"/>
    <path d="M0,33 Q0,52 3,60" stroke="#9C27B0" stroke-width="1.5" fill="none"/>
    <path d="M6,32 Q10,50 5,58" stroke="#9C27B0" stroke-width="1.5" fill="none"/>
    <path d="M12,30 Q20,45 15,55" stroke="#9C27B0" stroke-width="1.5" fill="none"/>
    <!-- Suckers -->
    <circle cx="-16" cy="50" r="1.5" fill="#AB47BC"/>
    <circle cx="-6" cy="53" r="1.5" fill="#AB47BC"/>
    <circle cx="3" cy="55" r="1.5" fill="#AB47BC"/>
    <circle cx="6" cy="53" r="1.5" fill="#AB47BC"/>
    <circle cx="16" cy="50" r="1.5" fill="#AB47BC"/>
    <!-- Funnel -->
    <path d="M-5,10 Q-10,18 -8,22" stroke="#6A1B9A" stroke-width="1.5" fill="none"/>
    <text x="0" y="72" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Головоногие</text>
  </g>

  <!-- Info -->
  <rect x="30" y="260" width="440" height="55" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="278" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Значение моллюсков</text>
  <text x="250" y="292" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Пища: устрицы, мидии, кальмары | Фильтраторы очищают воду | Жемчуг</text>
  <text x="250" y="304" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Вред: корабельный червь, слизни-вредители | Промежуточные хозяева паразитов</text>
''' + svg_footer(7, "biology")


def bio7_lesson11(title, sub):
    """Общая характеристика членистоногих"""
    return svg_header(title, sub, SUBJECT_COLORS["biology"]) + '''
  <!-- Arthropod features diagram -->
  <!-- Exoskeleton detail -->
  <g transform="translate(130,160)">
    <path d="M-50,-20 L50,-20 L50,20 L-50,20 Z" fill="#FFCC80" stroke="#E65100" stroke-width="2" rx="5"/>
    <path d="M-50,-20 Q0,-30 50,-20" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
    <!-- Segment lines -->
    <line x1="-25" y1="-22" x2="-25" y2="20" stroke="#BF360C" stroke-width="0.8"/>
    <line x1="0" y1="-24" x2="0" y2="20" stroke="#BF360C" stroke-width="0.8"/>
    <line x1="25" y1="-22" x2="25" y2="20" stroke="#BF360C" stroke-width="0.8"/>
    <!-- Jointed legs -->
    <path d="M-25,20 L-30,35 L-22,45" stroke="#BF360C" stroke-width="2" fill="none"/>
    <path d="M0,20 L-5,35 L3,45" stroke="#BF360C" stroke-width="2" fill="none"/>
    <path d="M25,20 L20,35 L28,45" stroke="#BF360C" stroke-width="2" fill="none"/>
    <!-- Chitin label -->
    <text x="0" y="10" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle" font-weight="bold">Хитин</text>
    <text x="0" y="60" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Членистые конечности</text>
  </g>

  <!-- Three classes -->
  <g transform="translate(400,100)">
    <text x="0" y="0" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">3 класса</text>
    <!-- Crustacea -->
    <g transform="translate(-60,25)">
      <rect x="-35" y="-10" width="70" height="22" rx="11" fill="#2196F3" opacity="0.3" stroke="#1565C0" stroke-width="1.5"/>
      <text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">Ракообразные</text>
    </g>
    <!-- Arachnida -->
    <g transform="translate(60,25)">
      <rect x="-35" y="-10" width="70" height="22" rx="11" fill="#9C27B0" opacity="0.3" stroke="#7B1FA2" stroke-width="1.5"/>
      <text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Паукообразные</text>
    </g>
    <!-- Insecta -->
    <g transform="translate(0,55)">
      <rect x="-30" y="-10" width="60" height="22" rx="11" fill="#4CAF50" opacity="0.3" stroke="#2E7D32" stroke-width="1.5"/>
      <text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Насекомые</text>
    </g>
  </g>

  <!-- Molting process -->
  <g transform="translate(380,240)">
    <text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Линька</text>
    <!-- Old exoskeleton -->
    <path d="M-35,-15 L-15,-15 L-15,15 L-35,15 Z" fill="none" stroke="#BF360C" stroke-width="1.5" stroke-dasharray="3,2"/>
    <text x="-25" y="25" font-family="Arial,sans-serif" font-size="5" fill="#BF360C" text-anchor="middle">Старый</text>
    <!-- Arrow -->
    <path d="M-8,0 L8,0" stroke="#2E7D32" stroke-width="1.5"/>
    <path d="M8,0 L5,-3 M8,0 L5,3" stroke="#2E7D32" stroke-width="1.5" fill="none"/>
    <!-- New soft body -->
    <path d="M15,-18 L35,-18 L35,18 L15,18 Z" fill="#FFECB3" stroke="#E65100" stroke-width="1.5"/>
    <text x="25" y="28" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">Новый</text>
  </g>

  <!-- Info box -->
  <rect x="30" y="290" width="440" height="28" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="308" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Хитиновый покров | Членистые конечности | Сегментированное тело | Линька | Самый многочисленный тип</text>
''' + svg_footer(7, "biology")


def bio7_lesson12(title, sub):
    """Ракообразные"""
    return svg_header(title, sub, SUBJECT_COLORS["biology"]) + '''
  <!-- Crayfish (River crab) -->
  <g transform="translate(200,175)">
    <!-- Cephalothorax -->
    <ellipse cx="0" cy="-15" rx="35" ry="25" fill="#E53935" opacity="0.7" stroke="#B71C1C" stroke-width="2"/>
    <!-- Rostrum -->
    <path d="M0,-40 L-5,-35 L5,-35 Z" fill="#C62828" stroke="#B71C1C" stroke-width="1"/>
    <!-- Eyes -->
    <circle cx="-15" cy="-30" r="4" fill="#333" stroke="#000" stroke-width="0.5"/>
    <circle cx="15" cy="-30" r="4" fill="#333" stroke="#000" stroke-width="0.5"/>
    <line x1="-15" y1="-34" x2="-15" y2="-38" stroke="#000" stroke-width="0.8"/>
    <line x1="15" y1="-34" x2="15" y2="-38" stroke="#000" stroke-width="0.8"/>
    <!-- Claws -->
    <g transform="translate(-40,-10)">
      <path d="M0,0 L-15,-10 L-25,-5 L-20,5 L-10,3 Z" fill="#EF5350" stroke="#B71C1C" stroke-width="1.5"/>
      <path d="M0,0 L-15,10 L-25,5 L-20,-5 L-10,-3 Z" fill="#EF5350" stroke="#B71C1C" stroke-width="1.5"/>
    </g>
    <g transform="translate(40,-10)">
      <path d="M0,0 L15,-10 L25,-5 L20,5 L10,3 Z" fill="#EF5350" stroke="#B71C1C" stroke-width="1.5"/>
      <path d="M0,0 L15,10 L25,5 L20,-5 L10,-3 Z" fill="#EF5350" stroke="#B71C1C" stroke-width="1.5"/>
    </g>
    <!-- Abdomen segments -->
    <path d="M-20,10 L-22,18 L-18,25 L-14,30 L-8,33 L0,35 L8,33 L14,30 L18,25 L22,18 L20,10" fill="#C62828" stroke="#B71C1C" stroke-width="1.5"/>
    <line x1="-14" y1="14" x2="14" y2="14" stroke="#B71C1C" stroke-width="0.5"/>
    <line x1="-16" y1="20" x2="16" y2="20" stroke="#B71C1C" stroke-width="0.5"/>
    <line x1="-14" y1="26" x2="14" y2="26" stroke="#B71C1C" stroke-width="0.5"/>
    <!-- Tail fan -->
    <path d="M-10,33 Q0,45 10,33" fill="#EF5350" stroke="#B71C1C" stroke-width="1"/>
    <!-- Walking legs -->
    <path d="M-30,5 L-42,20" stroke="#C62828" stroke-width="1.5"/>
    <path d="M-28,10 L-40,28" stroke="#C62828" stroke-width="1.5"/>
    <path d="M-25,15 L-35,32" stroke="#C62828" stroke-width="1.5"/>
    <path d="M30,5 L42,20" stroke="#C62828" stroke-width="1.5"/>
    <path d="M28,10 L40,28" stroke="#C62828" stroke-width="1.5"/>
    <path d="M25,15 L35,32" stroke="#C62828" stroke-width="1.5"/>
    <!-- Antennae -->
    <path d="M-10,-38 Q-25,-55 -20,-65" stroke="#C62828" stroke-width="1.5" fill="none"/>
    <path d="M10,-38 Q25,-55 20,-65" stroke="#C62828" stroke-width="1.5" fill="none"/>
    <!-- Short antennules -->
    <path d="M-5,-38 Q-12,-48 -10,-52" stroke="#EF5350" stroke-width="1" fill="none"/>
    <path d="M5,-38 Q12,-48 10,-52" stroke="#EF5350" stroke-width="1" fill="none"/>
  </g>

  <!-- Labels -->
  <g transform="translate(55,120)">
    <text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#B71C1C">Головогрудь</text>
  </g>
  <g transform="translate(55,175)">
    <text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#B71C1C">Ходульные</text>
    <text x="0" y="8" font-family="Arial,sans-serif" font-size="6" fill="#B71C1C">ноги</text>
  </g>
  <g transform="translate(55,210)">
    <text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#B71C1C">Брюшко</text>
  </g>

  <!-- Gill detail -->
  <g transform="translate(430,230)">
    <text x="0" y="-30" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Жабры</text>
    <path d="M-15,-20 Q-20,-10 -15,0 Q-10,10 -15,20" stroke="#1565C0" stroke-width="1.5" fill="none"/>
    <path d="M-5,-20 Q-10,-10 -5,0 Q0,10 -5,20" stroke="#1565C0" stroke-width="1.5" fill="none"/>
    <path d="M5,-20 Q0,-10 5,0 Q10,10 5,20" stroke="#1565C0" stroke-width="1.5" fill="none"/>
    <path d="M15,-20 Q10,-10 15,0 Q20,10 15,20" stroke="#1565C0" stroke-width="1.5" fill="none"/>
    <text x="0" y="35" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">Под карапаксом</text>
  </g>
''' + svg_footer(7, "biology")


def bio7_lesson13(title, sub):
    """Паукообразные"""
    return svg_header(title, sub, SUBJECT_COLORS["biology"]) + '''
  <!-- Spider -->
  <g transform="translate(170,175)">
    <!-- Cephalothorax -->
    <ellipse cx="0" cy="-15" rx="22" ry="18" fill="#5D4037" stroke="#3E2723" stroke-width="2"/>
    <!-- Abdomen -->
    <ellipse cx="0" cy="20" rx="28" ry="22" fill="#795548" stroke="#3E2723" stroke-width="2"/>
    <!-- Pattern on abdomen -->
    <path d="M-8,15 L0,10 L8,15 L0,20 Z" fill="#8D6E63" opacity="0.5"/>
    <!-- Eyes (8 eyes) -->
    <circle cx="-8" cy="-22" r="2" fill="#FFD54F" stroke="#333" stroke-width="0.5"/>
    <circle cx="8" cy="-22" r="2" fill="#FFD54F" stroke="#333" stroke-width="0.5"/>
    <circle cx="-4" cy="-25" r="1.5" fill="#FFD54F" stroke="#333" stroke-width="0.5"/>
    <circle cx="4" cy="-25" r="1.5" fill="#FFD54F" stroke="#333" stroke-width="0.5"/>
    <!-- Chelicerae -->
    <path d="M-5,-30 L-8,-38 L-3,-36" stroke="#3E2723" stroke-width="1.5" fill="none"/>
    <path d="M5,-30 L8,-38 L3,-36" stroke="#3E2723" stroke-width="1.5" fill="none"/>
    <!-- Pedipalps -->
    <path d="M-12,-28 L-18,-35" stroke="#5D4037" stroke-width="1.5"/>
    <path d="M12,-28 L18,-35" stroke="#5D4037" stroke-width="1.5"/>
    <!-- 8 Legs -->
    <path d="M-22,-10 Q-45,-25 -50,-40" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <path d="M-22,-5 Q-50,-10 -55,-20" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <path d="M-20,0 Q-45,5 -50,15" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <path d="M-18,5 Q-40,20 -42,35" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <path d="M22,-10 Q45,-25 50,-40" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <path d="M22,-5 Q50,-10 55,-20" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <path d="M20,0 Q45,5 50,15" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <path d="M18,5 Q40,20 42,35" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <!-- Spinnerets -->
    <ellipse cx="-5" cy="40" rx="3" ry="4" fill="#8D6E63" stroke="#3E2723" stroke-width="1"/>
    <ellipse cx="5" cy="40" rx="3" ry="4" fill="#8D6E63" stroke="#3E2723" stroke-width="1"/>
    <!-- Web thread -->
    <path d="M0,44 Q10,55 25,58" stroke="#9E9E9E" stroke-width="0.5" fill="none"/>
  </g>

  <!-- Scorpion -->
  <g transform="translate(420,175)">
    <!-- Cephalothorax -->
    <ellipse cx="-20" cy="0" rx="15" ry="12" fill="#FFCC80" stroke="#E65100" stroke-width="1.5"/>
    <!-- Eyes -->
    <circle cx="-25" cy="-5" r="2" fill="#333"/>
    <circle cx="-15" cy="-5" r="2" fill="#333"/>
    <!-- Chelicerae -->
    <path d="M-30,-5 L-38,-10 L-32,-8" stroke="#E65100" stroke-width="1.2" fill="none"/>
    <!-- Pedipalps (pincers) -->
    <path d="M-32,3 Q-45,-5 -50,-10 Q-52,-14 -48,-12 Q-42,-8 -35,0" stroke="#E65100" stroke-width="1.5" fill="#FFE0B2"/>
    <path d="M-32,5 Q-45,10 -50,15 Q-52,18 -48,16 Q-42,12 -35,5" stroke="#E65100" stroke-width="1.5" fill="#FFE0B2"/>
    <!-- Mesosoma (7 segments) -->
    <path d="M-5,-10 L30,-8 L30,8 L-5,10 Z" fill="#FFCC80" stroke="#E65100" stroke-width="1.5"/>
    <!-- Metasoma (tail) -->
    <path d="M30,0 Q40,-5 45,-15 Q48,-25 50,-35" stroke="#E65100" stroke-width="3" fill="none"/>
    <!-- Stinger -->
    <path d="M50,-35 L52,-45 L48,-38 Z" fill="#F44336" stroke="#C62828" stroke-width="1"/>
    <!-- Legs -->
    <path d="M0,-10 L-5,-22" stroke="#FF8F00" stroke-width="1"/>
    <path d="M10,-8 L8,-22" stroke="#FF8F00" stroke-width="1"/>
    <path d="M20,-8 L22,-22" stroke="#FF8F00" stroke-width="1"/>
    <path d="M0,10 L-5,22" stroke="#FF8F00" stroke-width="1"/>
    <path d="M10,8 L8,22" stroke="#FF8F00" stroke-width="1"/>
    <path d="M20,8 L22,22" stroke="#FF8F00" stroke-width="1"/>
  </g>

  <!-- Info -->
  <rect x="30" y="270" width="440" height="45" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="286" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">5 пар ходильных ног | Жабры | Хелицеры и педипальпы | Зеленые железы (выделение)</text>
  <text x="250" y="298" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Раки, крабы, креветки, омары | Около 70 000 видов</text>
''' + svg_footer(7, "biology")


def bio7_lesson13(title, sub):
    """Паукообразные"""
    return svg_header(title, sub, SUBJECT_COLORS["biology"]) + '''
  <!-- Spider web with spider -->
  <g transform="translate(250,175)">
    <!-- Web -->
    <line x1="0" y1="-80" x2="0" y2="80" stroke="#BDBDBD" stroke-width="0.5"/>
    <line x1="-80" y1="0" x2="80" y2="0" stroke="#BDBDBD" stroke-width="0.5"/>
    <line x1="-57" y1="-57" x2="57" y2="57" stroke="#BDBDBD" stroke-width="0.5"/>
    <line x1="57" y1="-57" x2="-57" y2="57" stroke="#BDBDBD" stroke-width="0.5"/>
    <!-- Spiral -->
    <path d="M10,0 Q10,10 0,10 Q-10,10 -10,0 Q-10,-10 0,-10 Q20,-10 20,10 Q20,30 -0,30 Q-30,30 -30,0 Q-30,-30 0,-30 Q40,-30 40,10 Q40,50 0,50 Q-50,50 -50,0 Q-50,-50 0,-50" stroke="#BDBDBD" stroke-width="0.5" fill="none"/>
    <!-- Spider on web -->
    <ellipse cx="10" cy="-15" rx="8" ry="6" fill="#5D4037" stroke="#3E2723" stroke-width="1.5"/>
    <ellipse cx="10" cy="-5" rx="6" ry="5" fill="#795548" stroke="#3E2723" stroke-width="1.5"/>
    <!-- Spider legs -->
    <path d="M3,-18 Q-10,-30 -15,-35" stroke="#5D4037" stroke-width="1" fill="none"/>
    <path d="M5,-15 Q-12,-18 -20,-15" stroke="#5D4037" stroke-width="1" fill="none"/>
    <path d="M5,-5 Q-12,-2 -18,5" stroke="#5D4037" stroke-width="1" fill="none"/>
    <path d="M5,-2 Q-10,8 -14,15" stroke="#5D4037" stroke-width="1" fill="none"/>
    <path d="M17,-18 Q30,-30 35,-35" stroke="#5D4037" stroke-width="1" fill="none"/>
    <path d="M15,-15 Q32,-18 40,-15" stroke="#5D4037" stroke-width="1" fill="none"/>
    <path d="M15,-5 Q32,-2 38,5" stroke="#5D4037" stroke-width="1" fill="none"/>
    <path d="M15,-2 Q30,8 34,15" stroke="#5D4037" stroke-width="1" fill="none"/>
  </g>

  <!-- Spider anatomy (side) -->
  <g transform="translate(80,280)">
    <text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#5D4037" text-anchor="middle" font-weight="bold">Строение паука</text>
    <ellipse cx="0" cy="0" rx="12" ry="8" fill="#795548" stroke="#3E2723" stroke-width="1"/>
    <ellipse cx="18" cy="0" rx="10" ry="7" fill="#8D6E63" stroke="#3E2723" stroke-width="1"/>
    <text x="0" y="15" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle">Головогрудь</text>
    <text x="18" y="15" font-family="Arial,sans-serif" font-size="5" fill="#333" text-anchor="middle">Брюшко</text>
  </g>

  <!-- Mite (tick) -->
  <g transform="translate(420,280)">
    <circle cx="0" cy="0" r="10" fill="#8D6E63" stroke="#3E2723" stroke-width="1.5"/>
    <circle cx="-10" cy="-5" r="4" fill="#A1887F" stroke="#3E2723" stroke-width="1"/>
    <!-- Legs -->
    <path d="M-7,-10 L-15,-18" stroke="#5D4037" stroke-width="1"/>
    <path d="M-3,-10 L-8,-20" stroke="#5D4037" stroke-width="1"/>
    <path d="M7,-10 L15,-18" stroke="#5D4037" stroke-width="1"/>
    <path d="M3,-10 L8,-20" stroke="#5D4037" stroke-width="1"/>
    <path d="M-7,8 L-15,16" stroke="#5D4037" stroke-width="1"/>
    <path d="M-3,8 L-8,18" stroke="#5D4037" stroke-width="1"/>
    <path d="M7,8 L15,16" stroke="#5D4037" stroke-width="1"/>
    <path d="M3,8 L8,18" stroke="#5D4037" stroke-width="1"/>
    <text x="0" y="28" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Клещ</text>
  </g>

  <!-- Info -->
  <rect x="140" y="260" width="300" height="28" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="290" y="278" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">4 пары ходильных ног | Хелицеры + педипальпы | Паутинные бородавки | Лёгочные мешки и трахеи</text>
''' + svg_footer(7, "biology")


def bio7_lesson14(title, sub):
    """Насекомые"""
    return svg_header(title, sub, SUBJECT_COLORS["biology"]) + '''
  <!-- Beetle - dorsal view (insect body plan) -->
  <g transform="translate(250,170)">
    <!-- Head -->
    <ellipse cx="-55" cy="0" rx="15" ry="12" fill="#8D6E63" stroke="#3E2723" stroke-width="2"/>
    <!-- Compound eyes -->
    <ellipse cx="-60" cy="-6" rx="6" ry="5" fill="#FFD54F" stroke="#333" stroke-width="0.8"/>
    <ellipse cx="-60" cy="6" rx="6" ry="5" fill="#FFD54F" stroke="#333" stroke-width="0.8"/>
    <!-- Antennae -->
    <path d="M-65,-8 Q-80,-20 -75,-30" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <path d="M-65,8 Q-80,20 -75,30" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <!-- Mouthparts -->
    <path d="M-70,0 L-78,-3 L-78,3 Z" fill="#6D4C41" stroke="#3E2723" stroke-width="1"/>
    <!-- Thorax (prothorax) -->
    <ellipse cx="-30" cy="0" rx="12" ry="14" fill="#A1887F" stroke="#3E2723" stroke-width="1.5"/>
    <!-- Elytra (wing covers) -->
    <path d="M-18,-14 L40,-12 L40,0 L-18,0 Z" fill="#6D4C41" stroke="#3E2723" stroke-width="1.5"/>
    <path d="M-18,0 L40,0 L40,12 L-18,14 Z" fill="#795548" stroke="#3E2723" stroke-width="1.5"/>
    <!-- Line down middle -->
    <line x1="-18" y1="0" x2="40" y2="0" stroke="#3E2723" stroke-width="0.8"/>
    <!-- Abdomen visible at end -->
    <ellipse cx="45" cy="0" rx="8" ry="10" fill="#A1887F" stroke="#3E2723" stroke-width="1"/>
    <!-- Legs (3 pairs) -->
    <path d="M-32,-12 L-40,-22 L-35,-28" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <path d="M-30,-14 L-32,-28 L-28,-32" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <path d="M-25,-14 L-20,-28 L-15,-32" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <path d="M-32,12 L-40,22 L-35,28" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <path d="M-30,14 L-32,28 L-28,32" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <path d="M-25,14 L-20,28 L-15,32" stroke="#5D4037" stroke-width="1.5" fill="none"/>
  </g>

  <!-- Body parts labels -->
  <g transform="translate(250,70)">
    <rect x="-190" y="-8" width="380" height="20" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
    <text x="-120" y="6" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Голова</text>
    <text x="0" y="6" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Грудь</text>
    <text x="120" y="6" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Брюшко</text>
  </g>

  <!-- Insect features box -->
  <rect x="30" y="270" width="440" height="45" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="286" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">3 отдела тела: голова, грудь, брюшко | 3 пары ног | 1-2 пары крыльев</text>
  <text x="250" y="298" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Фасеточные глаза | Усики (антенны) | Трахейное дыхание | Мальпигиевы сосуды</text>
''' + svg_footer(7, "biology")
```

Хм, у меня ошибка в уроке 14. Давайте я исправлю это и продолжу писать сценарий более осторожно. Сгенерирую все 32 урока с помощью одного сценария:⟨/thinking⟩

Хорошо, давайте создам полный инструмент и сразу сгенерирую все 32 SVG для 7 класса. Напишу скрипт целиком:⟨/thinking⟩

Создаю постоянный инструмент и генерирую SVG для 7 класса:Write.FileName: /home/z/my-project/school-curriculum-app/tools/svg_generator.py