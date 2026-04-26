#!/usr/bin/env python3
"""Generate 10 detailed SVG files for Grade 11 Biology lessons."""

import xml.etree.ElementTree as ET
import os

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade11/biology"
PRIMARY = "#33691E"
PRIMARY_LIGHT = "#558B2F"
PRIMARY_DARK = "#1B5E20"
BG = "#F1F8E9"
ACCENT = "#8BC34A"
ACCENT2 = "#A5D6A7"
TEXT_DARK = "#1B5E20"
TEXT_MID = "#33691E"
TEXT_LIGHT = "#689F38"
GREY = "#777"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ────────────── helpers ──────────────

def svg_header(n):
    """Return the standard SVG opening with defs, background, border, header, footer."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#F1F8E9"/>
      <stop offset="100%" stop-color="#FFFFFF"/>
    </linearGradient>
    <linearGradient id="hdr" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#33691E"/>
      <stop offset="100%" stop-color="#558B2F"/>
    </linearGradient>
  </defs>
  <rect width="500" height="350" fill="url(#bg)" rx="10"/>
  <rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="{PRIMARY}" stroke-width="2.5"/>
'''

def svg_footer(title, n):
    return f'''  <line x1="30" y1="308" x2="470" y2="308" stroke="{PRIMARY}" stroke-width="1.5" opacity="0.25"/>
  <text x="250" y="330" font-family="Arial,sans-serif" font-size="11" fill="{PRIMARY}" text-anchor="middle">Биология · 11 класс</text>
</svg>'''

def header_text(title, n):
    return f'''  <text x="250" y="40" font-family="Arial,sans-serif" font-size="18" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">{title}</text>
  <text x="250" y="58" font-family="Arial,sans-serif" font-size="11" fill="{GREY}" text-anchor="middle">Биология — Урок {n}</text>
  <line x1="30" y1="66" x2="470" y2="66" stroke="{PRIMARY}" stroke-width="2" opacity="0.25"/>
  <clipPath id="ill"><rect x="15" y="72" width="470" height="230" rx="6"/></clipPath>
  <g clip-path="url(#ill)">
    <rect x="15" y="72" width="470" height="230" fill="{BG}" opacity="0.5"/>
'''

# ────────────── LESSON 1: Развитие эволюционных идей ──────────────

def lesson1():
    content = header_text("Развитие эволюционных идей", 1)
    content += f'''
    <!-- Timeline arrow -->
    <line x1="40" y1="180" x2="460" y2="180" stroke="{PRIMARY}" stroke-width="2" marker-end="url(#arrowhead)"/>
    <defs><marker id="arrowhead" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="{PRIMARY}"/>
    </marker></defs>
    
    <!-- Aristotle -->
    <circle cx="70" cy="180" r="8" fill="{ACCENT}" stroke="{PRIMARY}" stroke-width="1.5"/>
    <text x="70" y="170" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_DARK}" text-anchor="middle">IV в. до н.э.</text>
    <text x="70" y="200" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Аристотель</text>
    <text x="70" y="210" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">Лестница</text>
    <text x="70" y="219" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">существ</text>

    <!-- Linnaeus -->
    <circle cx="145" cy="180" r="8" fill="{ACCENT}" stroke="{PRIMARY}" stroke-width="1.5"/>
    <text x="145" y="170" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_DARK}" text-anchor="middle">XVIII в.</text>
    <text x="145" y="200" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Линней</text>
    <text x="145" y="210" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">Классификация</text>
    <text x="145" y="219" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">креационизм</text>

    <!-- Lamarck -->
    <circle cx="230" cy="180" r="8" fill="{ACCENT2}" stroke="{PRIMARY}" stroke-width="1.5"/>
    <text x="230" y="170" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_DARK}" text-anchor="middle">1809</text>
    <text x="230" y="200" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Ламарк</text>
    <text x="230" y="210" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">Трудовая</text>
    <text x="230" y="219" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">наследственность</text>

    <!-- Darwin -->
    <circle cx="330" cy="180" r="10" fill="{ACCENT}" stroke="{PRIMARY_DARK}" stroke-width="2"/>
    <text x="330" y="168" font-family="Arial,sans-serif" font-size="7.5" font-weight="bold" fill="{PRIMARY_DARK}" text-anchor="middle">1859</text>
    <text x="330" y="200" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY_DARK}" text-anchor="middle">Дарвин</text>
    <text x="330" y="211" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">Естественный</text>
    <text x="330" y="220" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">отбор</text>

    <!-- Modern synthesis -->
    <circle cx="425" cy="180" r="8" fill="{ACCENT2}" stroke="{PRIMARY}" stroke-width="1.5"/>
    <text x="425" y="170" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_DARK}" text-anchor="middle">XX в.</text>
    <text x="425" y="200" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Синтетич.</text>
    <text x="425" y="210" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">теория</text>
    <text x="425" y="219" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">эволюции</text>

    <!-- Key concepts box -->
    <rect x="30" y="233" width="440" height="58" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1" opacity="0.9"/>
    <text x="250" y="248" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Ключевые идеи эволюции</text>
    <text x="45" y="262" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">• Изменчивость — источник разнообразия признаков</text>
    <text x="45" y="274" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">• Наследственность — передача признаков потомкам</text>
    <text x="45" y="286" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">• Естественный отбор — выживание наиболее приспособленных</text>

    <!-- Decorative DNA helix hint top-right -->
    <path d="M430,80 Q445,95 430,110 Q415,125 430,140" fill="none" stroke="{ACCENT}" stroke-width="2" opacity="0.4"/>
    <path d="M445,80 Q430,95 445,110 Q460,125 445,140" fill="none" stroke="{ACCENT2}" stroke-width="2" opacity="0.4"/>
  </g>
'''
    return svg_header(1) + content + svg_footer("Развитие эволюционных идей", 1)


# ────────────── LESSON 2: Доказательства эволюции ──────────────

def lesson2():
    content = header_text("Доказательства эволюции", 2)
    content += f'''
    <!-- Four evidence boxes -->
    <!-- 1. Paleontological -->
    <rect x="25" y="80" width="105" height="80" rx="6" fill="white" stroke="{PRIMARY}" stroke-width="1.2"/>
    <rect x="25" y="80" width="105" height="18" rx="6" fill="{PRIMARY}" opacity="0.15"/>
    <text x="77" y="93" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Палеонтологические</text>
    <!-- Fossil icon -->
    <ellipse cx="55" cy="120" rx="14" ry="10" fill="{BG}" stroke="{PRIMARY}" stroke-width="1"/>
    <path d="M45,118 Q50,112 55,118 Q60,124 65,118" fill="none" stroke="{PRIMARY_DARK}" stroke-width="1.2"/>
    <path d="M47,125 Q52,119 57,125" fill="none" stroke="{PRIMARY_DARK}" stroke-width="1"/>
    <text x="77" y="150" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">Ископаемые</text>
    <text x="77" y="158" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">переходные формы</text>

    <!-- 2. Comparative anatomical -->
    <rect x="140" y="80" width="105" height="80" rx="6" fill="white" stroke="{PRIMARY}" stroke-width="1.2"/>
    <rect x="140" y="80" width="105" height="18" rx="6" fill="{PRIMARY}" opacity="0.15"/>
    <text x="192" y="93" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Сравнит. анатомич.</text>
    <!-- Homologous limbs -->
    <line x1="160" y1="140" x2="180" y2="115" stroke="{PRIMARY_DARK}" stroke-width="2"/>
    <line x1="180" y1="115" x2="185" y2="105" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>
    <line x1="180" y1="115" x2="192" y2="108" stroke="{PRIMARY_DARK}" stroke-width="1.5"/>
    <line x1="192" y1="130" x2="210" y2="115" stroke="{ACCENT}" stroke-width="2"/>
    <line x1="210" y1="115" x2="215" y2="105" stroke="{ACCENT}" stroke-width="1.5"/>
    <line x1="210" y1="115" x2="222" y2="108" stroke="{ACCENT}" stroke-width="1.5"/>
    <text x="192" y="150" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">Гомологичные</text>
    <text x="192" y="158" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">органы, рудименты</text>

    <!-- 3. Embryological -->
    <rect x="255" y="80" width="105" height="80" rx="6" fill="white" stroke="{PRIMARY}" stroke-width="1.2"/>
    <rect x="255" y="80" width="105" height="18" rx="6" fill="{PRIMARY}" opacity="0.15"/>
    <text x="307" y="93" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Эмбриологические</text>
    <!-- Embryo circles -->
    <circle cx="280" cy="125" r="12" fill="{BG}" stroke="{PRIMARY}" stroke-width="1"/>
    <circle cx="280" cy="124" r="6" fill="{ACCENT2}" stroke="{PRIMARY_DARK}" stroke-width="0.8"/>
    <circle cx="307" cy="125" r="12" fill="{BG}" stroke="{ACCENT}" stroke-width="1"/>
    <circle cx="307" cy="124" r="6" fill="{ACCENT2}" stroke="{PRIMARY_DARK}" stroke-width="0.8"/>
    <circle cx="334" cy="125" r="12" fill="{BG}" stroke="{ACCENT2}" stroke-width="1"/>
    <circle cx="334" cy="124" r="6" fill="{ACCENT2}" stroke="{PRIMARY_DARK}" stroke-width="0.8"/>
    <text x="280" y="148" font-family="Arial,sans-serif" font-size="5.5" fill="{TEXT_MID}" text-anchor="middle">рыба</text>
    <text x="307" y="148" font-family="Arial,sans-serif" font-size="5.5" fill="{TEXT_MID}" text-anchor="middle">салам.</text>
    <text x="334" y="148" font-family="Arial,sans-serif" font-size="5.5" fill="{TEXT_MID}" text-anchor="middle">человек</text>
    <text x="307" y="158" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">Закон Геккеля</text>

    <!-- 4. Molecular -->
    <rect x="370" y="80" width="105" height="80" rx="6" fill="white" stroke="{PRIMARY}" stroke-width="1.2"/>
    <rect x="370" y="80" width="105" height="18" rx="6" fill="{PRIMARY}" opacity="0.15"/>
    <text x="422" y="93" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Молекулярные</text>
    <!-- DNA comparison bars -->
    <rect x="385" y="108" width="75" height="6" rx="2" fill="{ACCENT}" opacity="0.7"/>
    <rect x="385" y="108" width="70" height="6" rx="2" fill="{PRIMARY_DARK}" opacity="0.5"/>
    <rect x="385" y="118" width="75" height="6" rx="2" fill="{ACCENT}" opacity="0.7"/>
    <rect x="385" y="118" width="55" height="6" rx="2" fill="{PRIMARY_DARK}" opacity="0.5"/>
    <rect x="385" y="128" width="75" height="6" rx="2" fill="{ACCENT}" opacity="0.7"/>
    <rect x="385" y="128" width="35" height="6" rx="2" fill="{PRIMARY_DARK}" opacity="0.5"/>
    <text x="422" y="150" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">Сходство ДНК</text>
    <text x="422" y="158" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">и белков</text>

    <!-- Central statement -->
    <rect x="30" y="170" width="440" height="30" rx="5" fill="{PRIMARY}" opacity="0.1"/>
    <text x="250" y="189" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Все доказательства подтверждают единство происхождения живых организмов</text>

    <!-- Example row -->
    <rect x="30" y="210" width="210" height="48" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1" opacity="0.9"/>
    <text x="135" y="225" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Рудименты</text>
    <text x="135" y="237" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">Копчик, аппендикс, мышцы уха</text>
    <text x="135" y="248" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">→ утратившие функцию органы</text>

    <rect x="260" y="210" width="210" height="48" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1" opacity="0.9"/>
    <text x="365" y="225" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Атавизмы</text>
    <text x="365" y="237" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">Многососковость, хвост</text>
    <text x="365" y="248" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">→ возврат к предкам</text>

    <!-- Biogeographic note -->
    <rect x="30" y="265" width="440" height="28" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1" opacity="0.9"/>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Биогеографические: уникальная фауна материков (Австралия → сумчатые)</text>
    <text x="250" y="290" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">Похожие условия → конвергентное сходство (кит и рыба)</text>
  </g>
'''
    return svg_header(2) + content + svg_footer("Доказательства эволюции", 2)


# ────────────── LESSON 3: Микроэволюция ──────────────

def lesson3():
    content = header_text("Микроэволюция", 3)
    content += f'''
    <!-- Central concept -->
    <ellipse cx="250" cy="110" rx="80" ry="22" fill="{PRIMARY}" opacity="0.12" stroke="{PRIMARY}" stroke-width="1.2"/>
    <text x="250" y="114" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Микроэволюция</text>

    <!-- Arrows to three pillars -->
    <line x1="190" y1="125" x2="105" y2="150" stroke="{PRIMARY}" stroke-width="1.2"/>
    <line x1="250" y1="132" x2="250" y2="150" stroke="{PRIMARY}" stroke-width="1.2"/>
    <line x1="310" y1="125" x2="395" y2="150" stroke="{PRIMARY}" stroke-width="1.2"/>

    <!-- Three pillars -->
    <rect x="30" y="150" width="145" height="55" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1.2"/>
    <text x="102" y="166" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Мутации</text>
    <text x="102" y="178" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">Генерация нового</text>
    <text x="102" y="188" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">генетического материала</text>
    <text x="102" y="200" font-family="Arial,sans-serif" font-size="6.5" fill="{ACCENT}" text-anchor="middle">Случайный характер</text>

    <rect x="185" y="150" width="130" height="55" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1.2"/>
    <text x="250" y="166" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Дрейф генов</text>
    <text x="250" y="178" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">Случайное изменение</text>
    <text x="250" y="188" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">частот аллелей</text>
    <text x="250" y="200" font-family="Arial,sans-serif" font-size="6.5" fill="{ACCENT}" text-anchor="middle">Эффект бутылочного горлышка</text>

    <rect x="325" y="150" width="145" height="55" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1.2"/>
    <text x="397" y="166" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Естеств. отбор</text>
    <text x="397" y="178" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">Направленный процесс</text>
    <text x="397" y="188" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">сохранения адаптаций</text>
    <text x="397" y="200" font-family="Arial,sans-serif" font-size="6.5" fill="{ACCENT}" text-anchor="middle">Движущий, стабилиз., дизруптивный</text>

    <!-- Result arrow -->
    <path d="M250,208 L250,222" stroke="{PRIMARY_DARK}" stroke-width="2" marker-end="url(#arr3)"/>
    <defs><marker id="arr3" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto">
      <polygon points="0 0, 7 2.5, 0 5" fill="{PRIMARY_DARK}"/>
    </marker></defs>

    <!-- Population change diagram -->
    <rect x="40" y="225" width="420" height="35" rx="5" fill="{PRIMARY}" opacity="0.08"/>
    <text x="250" y="240" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Изменение генофонда популяции → Новый вид</text>
    <text x="250" y="254" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}" text-anchor="middle">Видообразование: аллопатрическое, симпатрическое, парапатрическое</text>

    <!-- Forms of selection -->
    <rect x="30" y="268" width="135" height="30" rx="4" fill="white" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="97" y="280" font-family="Arial,sans-serif" font-size="7" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Движущий отбор</text>
    <text x="97" y="292" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">→ сдвиг нормы реакции</text>

    <rect x="175" y="268" width="135" height="30" rx="4" fill="white" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="242" y="280" font-family="Arial,sans-serif" font-size="7" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Стабилизирующий</text>
    <text x="242" y="292" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">→ сохранение нормы</text>

    <rect x="320" y="268" width="135" height="30" rx="4" fill="white" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="387" y="280" font-family="Arial,sans-serif" font-size="7" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Дизруптивный</text>
    <text x="387" y="292" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">→ разрыв на две формы</text>
  </g>
'''
    return svg_header(3) + content + svg_footer("Микроэволюция", 3)


# ────────────── LESSON 4: Макроэволюция ──────────────

def lesson4():
    content = header_text("Макроэволюция", 4)
    content += f'''
    <!-- Evolutionary tree -->
    <text x="250" y="88" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Филогенетическое древо</text>
    
    <!-- Tree trunk -->
    <line x1="250" y1="275" x2="250" y2="130" stroke="{PRIMARY}" stroke-width="3"/>
    <!-- Branch left - fish -->
    <path d="M250,250 Q200,240 150,200 Q120,180 90,160" fill="none" stroke="{PRIMARY_LIGHT}" stroke-width="2"/>
    <circle cx="85" cy="155" r="8" fill="{BG}" stroke="{PRIMARY}" stroke-width="1.2"/>
    <text x="85" y="158" font-family="Arial,sans-serif" font-size="7" fill="{PRIMARY}" text-anchor="middle">🐟</text>
    <text x="85" y="175" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">Рыбы</text>
    
    <!-- Branch - amphibians -->
    <path d="M200,235 Q180,210 170,190" fill="none" stroke="{PRIMARY_LIGHT}" stroke-width="2"/>
    <circle cx="168" cy="185" r="8" fill="{BG}" stroke="{PRIMARY}" stroke-width="1.2"/>
    <text x="168" y="188" font-family="Arial,sans-serif" font-size="7" fill="{PRIMARY}" text-anchor="middle">🐸</text>
    <text x="168" y="205" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">Земноводные</text>

    <!-- Branch - reptiles -->
    <path d="M250,220 Q270,200 290,180" fill="none" stroke="{PRIMARY_LIGHT}" stroke-width="2"/>
    <circle cx="295" cy="175" r="8" fill="{BG}" stroke="{PRIMARY}" stroke-width="1.2"/>
    <text x="295" y="178" font-family="Arial,sans-serif" font-size="7" fill="{PRIMARY}" text-anchor="middle">🦎</text>
    <text x="295" y="195" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">Пресмыкающиеся</text>

    <!-- Branch right - birds -->
    <path d="M280,200 Q310,185 340,165" fill="none" stroke="{PRIMARY_LIGHT}" stroke-width="2"/>
    <circle cx="345" cy="160" r="8" fill="{BG}" stroke="{PRIMARY}" stroke-width="1.2"/>
    <text x="345" y="163" font-family="Arial,sans-serif" font-size="7" fill="{PRIMARY}" text-anchor="middle">🦅</text>
    <text x="345" y="178" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">Птицы</text>

    <!-- Branch - mammals -->
    <path d="M250,180 Q300,160 380,140" fill="none" stroke="{PRIMARY_LIGHT}" stroke-width="2"/>
    <circle cx="385" cy="135" r="8" fill="{BG}" stroke="{PRIMARY}" stroke-width="1.2"/>
    <text x="385" y="138" font-family="Arial,sans-serif" font-size="7" fill="{PRIMARY}" text-anchor="middle">🐾</text>
    <text x="385" y="155" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">Млекопитающие</text>

    <!-- Time axis -->
    <text x="250" y="290" font-family="Arial,sans-serif" font-size="7" fill="{GREY}" text-anchor="middle">Время (млн лет) →</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="6" fill="{GREY}" text-anchor="middle">500    400    300    200    100    0</text>

    <!-- Key concepts -->
    <rect x="30" y="240" width="185" height="55" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="122" y="255" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Пути макроэволюции</text>
    <text x="40" y="268" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">• Ароморфоз — крупное усложнение</text>
    <text x="40" y="279" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">• Идиоадаптация — мелкие адаптации</text>
    <text x="40" y="290" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">• Дегенерация — упрощение строения</text>

    <rect x="290" y="240" width="175" height="55" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="377" y="255" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Правило</text>
    <text x="377" y="268" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">Неполного параллелизма:</text>
    <text x="377" y="279" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">Параллелизм не доходит</text>
    <text x="377" y="290" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">до совпадения групп</text>
  </g>
'''
    return svg_header(4) + content + svg_footer("Макроэволюция", 4)


# ────────────── LESSON 5: Экологические факторы ──────────────

def lesson5():
    content = header_text("Экологические факторы", 5)
    content += f'''
    <!-- Central circle -->
    <circle cx="250" cy="165" r="42" fill="{PRIMARY}" opacity="0.1" stroke="{PRIMARY}" stroke-width="1.5"/>
    <text x="250" y="160" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Экологические</text>
    <text x="250" y="173" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">факторы</text>

    <!-- Abiotic -->
    <rect x="25" y="80" width="140" height="90" rx="6" fill="white" stroke="{PRIMARY}" stroke-width="1.2"/>
    <rect x="25" y="80" width="140" height="16" rx="6" fill="{PRIMARY}" opacity="0.15"/>
    <text x="95" y="92" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Абиотические</text>
    <text x="35" y="108" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">🌡 Температура</text>
    <text x="35" y="119" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">💧 Влажность</text>
    <text x="35" y="130" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">☀️ Освещённость</text>
    <text x="35" y="141" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">💨 Давление, ветер</text>
    <text x="35" y="152" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">🧪 Состав почвы, воды</text>
    <line x1="95" y1="96" x2="220" y2="145" stroke="{PRIMARY}" stroke-width="1" opacity="0.5"/>

    <!-- Biotic -->
    <rect x="180" y="215" width="140" height="80" rx="6" fill="white" stroke="{PRIMARY}" stroke-width="1.2"/>
    <rect x="180" y="215" width="140" height="16" rx="6" fill="{PRIMARY}" opacity="0.15"/>
    <text x="250" y="227" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Биотические</text>
    <text x="190" y="243" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">🦊 Хищничество</text>
    <text x="190" y="254" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">🤝 Симбиоз</text>
    <text x="190" y="265" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">⚔️ Конкуренция</text>
    <text x="190" y="276" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">🦠 Паразитизм</text>
    <text x="190" y="287" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">🌿 Растительноядность</text>
    <line x1="250" y1="215" x2="250" y2="207" stroke="{PRIMARY}" stroke-width="1" opacity="0.5"/>

    <!-- Anthropogenic -->
    <rect x="340" y="80" width="130" height="90" rx="6" fill="white" stroke="{PRIMARY}" stroke-width="1.2"/>
    <rect x="340" y="80" width="130" height="16" rx="6" fill="#E53935" opacity="0.12"/>
    <text x="405" y="92" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#C62828" text-anchor="middle">Антропогенные</text>
    <text x="350" y="108" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">🏭 Загрязнение</text>
    <text x="350" y="119" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">🪓 Вырубка лесов</text>
    <text x="350" y="130" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">🏗️ Разрушение мест</text>
    <text x="355" y="141" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">обитания</text>
    <text x="350" y="152" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">☢️ Радиация, шум</text>
    <line x1="340" y1="135" x2="280" y2="150" stroke="{PRIMARY}" stroke-width="1" opacity="0.5"/>

    <!-- Limiting factor box -->
    <rect x="30" y="185" width="130" height="22" rx="4" fill="{ACCENT2}" stroke="{PRIMARY}" stroke-width="0.8" opacity="0.8"/>
    <text x="95" y="200" font-family="Arial,sans-serif" font-size="7.5" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Закон минимума Либиха</text>

    <!-- Tolerance curve -->
    <rect x="340" y="200" width="130" height="55" rx="4" fill="white" stroke="{PRIMARY}" stroke-width="0.8"/>
    <text x="405" y="213" font-family="Arial,sans-serif" font-size="7" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Кривая толерантности</text>
    <path d="M355,245 Q370,225 385,220 Q400,225 415,245 Q425,250 430,248" fill="none" stroke="{PRIMARY}" stroke-width="1.5"/>
    <line x1="355" y1="248" x2="445" y2="248" stroke="{GREY}" stroke-width="0.5"/>
    <text x="360" y="254" font-family="Arial,sans-serif" font-size="5.5" fill="{GREY}">мин</text>
    <text x="385" y="254" font-family="Arial,sans-serif" font-size="5.5" fill="{GREY}">оптимум</text>
    <text x="430" y="254" font-family="Arial,sans-serif" font-size="5.5" fill="{GREY}">макс</text>

    <!-- Shelford law -->
    <rect x="340" y="260" width="130" height="20" rx="4" fill="{ACCENT2}" stroke="{PRIMARY}" stroke-width="0.8" opacity="0.8"/>
    <text x="405" y="274" font-family="Arial,sans-serif" font-size="7" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Закон толерантности Шелфорда</text>
  </g>
'''
    return svg_header(5) + content + svg_footer("Экологические факторы", 5)


# ────────────── LESSON 6: Популяции и сообщества ──────────────

def lesson6():
    content = header_text("Популяции и сообщества", 6)
    content += f'''
    <!-- Population characteristics -->
    <rect x="25" y="80" width="220" height="105" rx="6" fill="white" stroke="{PRIMARY}" stroke-width="1.2"/>
    <rect x="25" y="80" width="220" height="16" rx="6" fill="{PRIMARY}" opacity="0.15"/>
    <text x="135" y="92" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Популяция и её свойства</text>
    
    <!-- Population dots cluster -->
    <circle cx="55" cy="125" r="4" fill="{ACCENT}" stroke="{PRIMARY}" stroke-width="0.8"/>
    <circle cx="68" cy="118" r="4" fill="{ACCENT}" stroke="{PRIMARY}" stroke-width="0.8"/>
    <circle cx="60" cy="138" r="4" fill="{ACCENT2}" stroke="{PRIMARY}" stroke-width="0.8"/>
    <circle cx="75" cy="132" r="4" fill="{ACCENT}" stroke="{PRIMARY}" stroke-width="0.8"/>
    <circle cx="50" cy="148" r="4" fill="{ACCENT2}" stroke="{PRIMARY}" stroke-width="0.8"/>
    <circle cx="82" cy="145" r="4" fill="{ACCENT}" stroke="{PRIMARY}" stroke-width="0.8"/>
    <circle cx="65" cy="155" r="4" fill="{ACCENT2}" stroke="{PRIMARY}" stroke-width="0.8"/>
    <!-- Dashed boundary -->
    <ellipse cx="65" cy="138" rx="30" ry="30" fill="none" stroke="{PRIMARY}" stroke-width="1" stroke-dasharray="3,2"/>
    <text x="65" y="172" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">Популяция</text>

    <!-- Properties list -->
    <text x="115" y="112" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">• Численность</text>
    <text x="115" y="123" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">• Плотность</text>
    <text x="115" y="134" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">• Рождаемость / Смертность</text>
    <text x="115" y="145" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">• Возрастной состав</text>
    <text x="115" y="156" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">• Половой состав</text>
    <text x="115" y="167" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">• Генофонд</text>
    <text x="115" y="178" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">• Динамика (рост/спад)</text>

    <!-- Community structure -->
    <rect x="260" y="80" width="210" height="105" rx="6" fill="white" stroke="{PRIMARY}" stroke-width="1.2"/>
    <rect x="260" y="80" width="210" height="16" rx="6" fill="{PRIMARY}" opacity="0.15"/>
    <text x="365" y="92" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Сообщество (биоценоз)</text>
    
    <!-- Trophic layers -->
    <rect x="275" y="103" width="180" height="14" rx="3" fill="{PRIMARY}" opacity="0.25"/>
    <text x="365" y="113" font-family="Arial,sans-serif" font-size="7" fill="{PRIMARY_DARK}" text-anchor="middle">Продуценты (растения)</text>
    <rect x="285" y="120" width="160" height="14" rx="3" fill="{ACCENT}" opacity="0.3"/>
    <text x="365" y="130" font-family="Arial,sans-serif" font-size="7" fill="{PRIMARY}" text-anchor="middle">Консументы I порядка (травоядные)</text>
    <rect x="295" y="137" width="140" height="14" rx="3" fill="{ACCENT2}" opacity="0.4"/>
    <text x="365" y="147" font-family="Arial,sans-serif" font-size="7" fill="{PRIMARY}" text-anchor="middle">Консументы II порядка (хищники)</text>
    <rect x="310" y="154" width="110" height="14" rx="3" fill="{BG}" stroke="{PRIMARY}" stroke-width="0.5"/>
    <text x="365" y="164" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">Редуценты (бактерии, грибы)</text>

    <!-- Population growth curves -->
    <rect x="25" y="195" width="220" height="95" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="135" y="210" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Динамика популяции</text>
    <!-- J-curve -->
    <path d="M40,275 Q60,272 80,268 Q110,258 130,235 Q145,210 160,230" fill="none" stroke="#E53935" stroke-width="1.5"/>
    <text x="165" y="228" font-family="Arial,sans-serif" font-size="6" fill="#C62828">J-кривая</text>
    <!-- S-curve -->
    <path d="M40,275 Q60,270 80,260 Q110,240 130,230 Q150,225 170,223" fill="none" stroke="{PRIMARY}" stroke-width="1.5"/>
    <line x1="40" y1="278" x2="180" y2="278" stroke="{GREY}" stroke-width="0.5"/>
    <line x1="40" y1="218" x2="180" y2="218" stroke="{PRIMARY}" stroke-width="0.5" stroke-dasharray="3,2" opacity="0.5"/>
    <text x="185" y="220" font-family="Arial,sans-serif" font-size="5.5" fill="{PRIMARY}">K</text>
    <text x="165" y="240" font-family="Arial,sans-serif" font-size="6" fill="{PRIMARY}">S-кривая</text>
    <text x="110" y="290" font-family="Arial,sans-serif" font-size="6" fill="{GREY}" text-anchor="middle">время →</text>
    <text x="35" y="255" font-family="Arial,sans-serif" font-size="5.5" fill="{GREY}" transform="rotate(-90,35,255)">N</text>

    <!-- Community interactions -->
    <rect x="260" y="195" width="210" height="95" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="365" y="210" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Типы взаимодействий</text>
    <text x="270" y="226" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">Мутуализм (+/+) — лишайник</text>
    <text x="270" y="238" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">Комменсализм (+/0) — рак-отшельник</text>
    <text x="270" y="250" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">Хищничество (+/−) — волк и заяц</text>
    <text x="270" y="262" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">Паразитизм (+/−) — клещ</text>
    <text x="270" y="274" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">Конкуренция (−/−) — ресурсы</text>
    <text x="270" y="286" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">Аменсализм (−/0) — антибиоз</text>
  </g>
'''
    return svg_header(6) + content + svg_footer("Популяции и сообщества", 6)


# ────────────── LESSON 7: Экосистемы ──────────────

def lesson7():
    content = header_text("Экосистемы", 7)
    content += f'''
    <!-- Ecosystem diagram -->
    <text x="250" y="90" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Структура экосистемы</text>
    
    <!-- Sun -->
    <circle cx="55" cy="115" r="16" fill="#FFF9C4" stroke="#FBC02D" stroke-width="1.5"/>
    <text x="55" y="119" font-family="Arial,sans-serif" font-size="9" fill="#F57F17" text-anchor="middle">☀️</text>
    <text x="55" y="140" font-family="Arial,sans-serif" font-size="6.5" fill="{GREY}" text-anchor="middle">Энергия</text>

    <!-- Arrow: Sun → Producers -->
    <line x1="72" y1="120" x2="115" y2="120" stroke="#FBC02D" stroke-width="1.5" marker-end="url(#arr7)"/>
    <defs><marker id="arr7" markerWidth="6" markerHeight="5" refX="6" refY="2.5" orient="auto">
      <polygon points="0 0, 6 2.5, 0 5" fill="#FBC02D"/>
    </marker></defs>

    <!-- Producers -->
    <rect x="118" y="105" width="75" height="32" rx="5" fill="{ACCENT}" opacity="0.3" stroke="{PRIMARY}" stroke-width="1.2"/>
    <text x="155" y="118" font-family="Arial,sans-serif" font-size="7.5" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Продуценты</text>
    <text x="155" y="130" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">Растения, водоросли</text>

    <!-- Arrow: Producers → Primary consumers -->
    <line x1="195" y1="120" x2="230" y2="120" stroke="{PRIMARY}" stroke-width="1.5" marker-end="url(#arr7g)"/>
    <defs><marker id="arr7g" markerWidth="6" markerHeight="5" refX="6" refY="2.5" orient="auto">
      <polygon points="0 0, 6 2.5, 0 5" fill="{PRIMARY}"/>
    </marker></defs>

    <!-- Primary consumers -->
    <rect x="233" y="105" width="75" height="32" rx="5" fill="{ACCENT2}" opacity="0.4" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="270" y="118" font-family="Arial,sans-serif" font-size="7.5" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Консументы I</text>
    <text x="270" y="130" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">Травоядные</text>

    <!-- Arrow -->
    <line x1="310" y1="120" x2="340" y2="120" stroke="{PRIMARY}" stroke-width="1.5" marker-end="url(#arr7g)"/>

    <!-- Secondary consumers -->
    <rect x="343" y="105" width="75" height="32" rx="5" fill="#FFCC80" opacity="0.4" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="380" y="118" font-family="Arial,sans-serif" font-size="7.5" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Консументы II</text>
    <text x="380" y="130" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">Хищники</text>

    <!-- Arrow down to decomposers -->
    <path d="M380,138 L380,160 L270,165" fill="none" stroke="{PRIMARY}" stroke-width="1" marker-end="url(#arr7g)"/>

    <!-- Decomposers -->
    <rect x="185" y="155" width="90" height="25" rx="5" fill="{BG}" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="230" y="168" font-family="Arial,sans-serif" font-size="7.5" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Редуценты</text>
    <text x="230" y="178" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}" text-anchor="middle">Бактерии, грибы</text>

    <!-- Nutrient cycle arrow back -->
    <path d="M185,170 L130,175 L125,140" fill="none" stroke="#795548" stroke-width="1" stroke-dasharray="3,2" marker-end="url(#arr7b)"/>
    <defs><marker id="arr7b" markerWidth="6" markerHeight="5" refX="6" refY="2.5" orient="auto">
      <polygon points="0 0, 6 2.5, 0 5" fill="#795548"/>
    </marker></defs>
    <text x="120" y="165" font-family="Arial,sans-serif" font-size="5.5" fill="#795548">вещества</text>

    <!-- Energy pyramid -->
    <rect x="30" y="200" width="200" height="95" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="130" y="215" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Пирамида энергии</text>
    
    <polygon points="130,225 100,290 160,290" fill="{ACCENT2}" opacity="0.4" stroke="{PRIMARY}" stroke-width="0.8"/>
    <!-- Trophic levels -->
    <line x1="100" y1="290" x2="160" y2="290" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="130" y="287" font-family="Arial,sans-serif" font-size="6" fill="{PRIMARY_DARK}" text-anchor="middle">Продуценты</text>
    <line x1="110" y1="273" x2="150" y2="273" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="130" y="270" font-family="Arial,sans-serif" font-size="6" fill="{PRIMARY_DARK}" text-anchor="middle">Конс. I</text>
    <line x1="118" y1="256" x2="142" y2="256" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="130" y="253" font-family="Arial,sans-serif" font-size="6" fill="{PRIMARY_DARK}" text-anchor="middle">Конс. II</text>
    <line x1="124" y1="239" x2="136" y2="239" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="130" y="236" font-family="Arial,sans-serif" font-size="5.5" fill="{PRIMARY_DARK}" text-anchor="middle">Конс. III</text>
    <text x="130" y="227" font-family="Arial,sans-serif" font-size="5" fill="{GREY}" text-anchor="middle">1% энергии</text>

    <!-- Rules -->
    <rect x="250" y="200" width="220" height="95" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="360" y="215" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Правила экосистемы</text>
    <text x="260" y="232" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">Правило 10%:</text>
    <text x="260" y="243" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">Переход ~10% энергии между</text>
    <text x="260" y="253" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">соседними трофическими уровнями</text>
    <text x="260" y="268" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">Поток энергии — открытый</text>
    <text x="260" y="279" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">Круговорот веществ — замкнутый</text>
    <text x="260" y="291" font-family="Arial,sans-serif" font-size="7.5" fill="{TEXT_MID}">Саморегуляция → устойчивость</text>
  </g>
'''
    return svg_header(7) + content + svg_footer("Экосистемы", 7)


# ────────────── LESSON 8: Биосфера ──────────────

def lesson8():
    content = header_text("Биосфера", 8)
    content += f'''
    <!-- Earth circle -->
    <circle cx="135" cy="180" r="65" fill="#E3F2FD" stroke="{PRIMARY}" stroke-width="1.5"/>
    <!-- Continents hint -->
    <ellipse cx="120" cy="165" rx="25" ry="20" fill="{ACCENT}" opacity="0.4" stroke="{PRIMARY_LIGHT}" stroke-width="0.8"/>
    <ellipse cx="150" cy="190" rx="15" ry="18" fill="{ACCENT}" opacity="0.4" stroke="{PRIMARY_LIGHT}" stroke-width="0.8"/>
    <ellipse cx="110" cy="200" rx="12" ry="10" fill="{ACCENT2}" opacity="0.5" stroke="{PRIMARY_LIGHT}" stroke-width="0.8"/>
    <text x="135" y="180" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY_DARK}" text-anchor="middle">Биосфера</text>

    <!-- Concentric shells around Earth -->
    <circle cx="135" cy="180" r="80" fill="none" stroke="{PRIMARY}" stroke-width="0.8" stroke-dasharray="4,3" opacity="0.4"/>
    <circle cx="135" cy="180" r="95" fill="none" stroke="{PRIMARY}" stroke-width="0.6" stroke-dasharray="4,3" opacity="0.3"/>

    <!-- Shells labels -->
    <rect x="225" y="85" width="240" height="80" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="345" y="100" font-family="Arial,sans-serif" font-size="8.5" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Оболочки биосферы (В.И. Вернадский)</text>
    
    <rect x="235" y="108" width="220" height="14" rx="3" fill="{ACCENT2}" opacity="0.3"/>
    <text x="345" y="118" font-family="Arial,sans-serif" font-size="7" fill="{PRIMARY}" text-anchor="middle">Атмосфера — газовая оболочка (до 20 км)</text>
    
    <rect x="235" y="124" width="220" height="14" rx="3" fill="#81D4FA" opacity="0.25"/>
    <text x="345" y="134" font-family="Arial,sans-serif" font-size="7" fill="{PRIMARY}" text-anchor="middle">Гидросфера — водная оболочка (до 11 км глуб.)</text>
    
    <rect x="235" y="140" width="220" height="14" rx="3" fill="{BG}" stroke="{PRIMARY}" stroke-width="0.5"/>
    <text x="345" y="150" font-family="Arial,sans-serif" font-size="7" fill="{PRIMARY}" text-anchor="middle">Литосфера — твёрдая оболочка (до 5 км глуб.)</text>

    <text x="345" y="162" font-family="Arial,sans-serif" font-size="6.5" fill="{GREY}" text-anchor="middle">Живое вещество — ~0.01% массы, но главная сила</text>

    <!-- Vernadsky's teachings -->
    <rect x="25" y="260" width="215" height="40" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="132" y="274" font-family="Arial,sans-serif" font-size="7.5" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Учение Вернадского</text>
    <text x="35" y="286" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">• Биогенная миграция атомов</text>
    <text x="35" y="296" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">• Живое вещество — геохимическая сила</text>

    <!-- Functions -->
    <rect x="250" y="175" width="215" height="110" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="357" y="190" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Функции живого вещества</text>
    <text x="260" y="205" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">🍃 Энергетическая — фотосинтез</text>
    <text x="260" y="218" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">🔄 Газовая — круговорот O₂ и CO₂</text>
    <text x="260" y="231" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">🧪 Концентрационная — накопление</text>
    <text x="270" y="242" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">элементов (Ca, P, Si)</text>
    <text x="260" y="255" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">🏗 Окислительно-восстановительная</text>
    <text x="260" y="268" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">🏗 Деструктивная — разложение</text>
    <text x="260" y="281" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">📊 Средообразующая — почвообразование</text>
  </g>
'''
    return svg_header(8) + content + svg_footer("Биосфера", 8)


# ────────────── LESSON 9: Человек и биосфера ──────────────

def lesson9():
    content = header_text("Человек и биосфера", 9)
    content += f'''
    <!-- Central: Human impact diagram -->
    <circle cx="250" cy="140" r="35" fill="{PRIMARY}" opacity="0.1" stroke="{PRIMARY}" stroke-width="1.5"/>
    <text x="250" y="136" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Человек</text>
    <text x="250" y="149" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">в биосфере</text>

    <!-- Negative impacts (left) -->
    <rect x="25" y="85" width="110" height="150" rx="5" fill="white" stroke="#E53935" stroke-width="1"/>
    <rect x="25" y="85" width="110" height="14" rx="5" fill="#FFCDD2" opacity="0.5"/>
    <text x="80" y="96" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="#C62828" text-anchor="middle">Отрицательное</text>
    <text x="35" y="113" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">🏭 Загрязнение</text>
    <text x="35" y="125" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">   атмосферы, воды</text>
    <text x="35" y="138" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">🌳 Обезлесение</text>
    <text x="35" y="150" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">🦏 Сокращение</text>
    <text x="40" y="161" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">биоразнообразия</text>
    <text x="35" y="173" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">🏜 Опустынивание</text>
    <text x="35" y="185" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">🌡 Парниковый эффект</text>
    <text x="35" y="197" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">🕳 Озоновые дыры</text>
    <text x="35" y="209" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">☢️ Радиоактивное</text>
    <text x="40" y="220" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">загрязнение</text>

    <!-- Positive actions (right) -->
    <rect x="365" y="85" width="110" height="150" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1"/>
    <rect x="365" y="85" width="110" height="14" rx="5" fill="{ACCENT2}" opacity="0.5"/>
    <text x="420" y="96" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Положительное</text>
    <text x="375" y="113" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">🏞 Заповедники</text>
    <text x="375" y="125" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">🌲 Лесовосстановление</text>
    <text x="375" y="138" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">♻️ Очистка стоков</text>
    <text x="375" y="150" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">📑 Красная книга</text>
    <text x="375" y="163" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">🌾 Селекция</text>
    <text x="375" y="175" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">🔬 Биотехнологии</text>
    <text x="375" y="188" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">📊 Мониторинг</text>
    <text x="375" y="200" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">🌍 Международные</text>
    <text x="380" y="211" font-family="Arial,sans-serif" font-size="6.5" fill="{TEXT_MID}">соглашения</text>

    <!-- Noosphere concept -->
    <rect x="25" y="245" width="220" height="55" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="135" y="260" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Ноосфера (Вернадский)</text>
    <text x="35" y="274" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">Сфера разума — этап эволюции биосферы,</text>
    <text x="35" y="285" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">где разумная деятельность человека</text>
    <text x="35" y="296" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">становится главным геохимическим фактором</text>

    <!-- Sustainable development -->
    <rect x="260" y="245" width="215" height="55" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="367" y="260" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Устойчивое развитие</text>
    <text x="270" y="274" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">📊 Экономика + Экология + Социум</text>
    <text x="270" y="285" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">🎯 Цели устойчивого развития ООН</text>
    <text x="270" y="296" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">♻️ Рациональное природопользование</text>
  </g>
'''
    return svg_header(9) + content + svg_footer("Человек и биосфера", 9)


# ────────────── LESSON 10: Основы биотехнологии ──────────────

def lesson10():
    content = header_text("Основы биотехнологии", 10)
    content += f'''
    <!-- Central DNA icon -->
    <path d="M70,85 Q85,105 70,125 Q55,145 70,165 Q85,185 70,205" fill="none" stroke="{PRIMARY}" stroke-width="2.5" opacity="0.3"/>
    <path d="M85,85 Q70,105 85,125 Q100,145 85,165 Q70,185 85,205" fill="none" stroke="{ACCENT}" stroke-width="2.5" opacity="0.3"/>
    <!-- Rungs -->
    <line x1="72" y1="100" x2="83" y2="100" stroke="{PRIMARY}" stroke-width="1.2" opacity="0.3"/>
    <line x1="67" y1="125" x2="88" y2="125" stroke="{PRIMARY}" stroke-width="1.2" opacity="0.3"/>
    <line x1="72" y1="150" x2="83" y2="150" stroke="{PRIMARY}" stroke-width="1.2" opacity="0.3"/>
    <line x1="67" y1="175" x2="88" y2="175" stroke="{PRIMARY}" stroke-width="1.2" opacity="0.3"/>
    <line x1="72" y1="200" x2="83" y2="200" stroke="{PRIMARY}" stroke-width="1.2" opacity="0.3"/>

    <!-- Four areas -->
    <rect x="110" y="80" width="180" height="55" rx="6" fill="white" stroke="{PRIMARY}" stroke-width="1.2"/>
    <rect x="110" y="80" width="180" height="14" rx="6" fill="{PRIMARY}" opacity="0.15"/>
    <text x="200" y="91" font-family="Arial,sans-serif" font-size="8.5" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Генная инженерия</text>
    <text x="120" y="108" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">• Рестрикция — разрезание ДНК</text>
    <text x="120" y="119" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">• Лигирование — сшивание фрагментов</text>
    <text x="120" y="130" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">• ПЦР — копирование генов</text>

    <rect x="305" y="80" width="175" height="55" rx="6" fill="white" stroke="{PRIMARY}" stroke-width="1.2"/>
    <rect x="305" y="80" width="175" height="14" rx="6" fill="{PRIMARY}" opacity="0.15"/>
    <text x="392" y="91" font-family="Arial,sans-serif" font-size="8.5" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Клеточная инженерия</text>
    <text x="315" y="108" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">• Гибридизация клеток</text>
    <text x="315" y="119" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">• Клонирование организмов</text>
    <text x="315" y="130" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">• Культура тканей</text>

    <rect x="110" y="145" width="180" height="55" rx="6" fill="white" stroke="{PRIMARY}" stroke-width="1.2"/>
    <rect x="110" y="145" width="180" height="14" rx="6" fill="{PRIMARY}" opacity="0.15"/>
    <text x="200" y="156" font-family="Arial,sans-serif" font-size="8.5" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Микробиологический синтез</text>
    <text x="120" y="173" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">• Антибиотики (пенициллин)</text>
    <text x="120" y="184" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">• Гормоны (инсулин)</text>
    <text x="120" y="195" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">• Ферменты, витамины</text>

    <rect x="305" y="145" width="175" height="55" rx="6" fill="white" stroke="{PRIMARY}" stroke-width="1.2"/>
    <rect x="305" y="145" width="175" height="14" rx="6" fill="{PRIMARY}" opacity="0.15"/>
    <text x="392" y="156" font-family="Arial,sans-serif" font-size="8.5" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Биоинженерия</text>
    <text x="315" y="173" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">• ГМО-организмы</text>
    <text x="315" y="184" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">• Биореакторы</text>
    <text x="315" y="195" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">• Биосенсоры</text>

    <!-- CRISPR -->
    <rect x="25" y="210" width="225" height="45" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="137" y="225" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">CRISPR-Cas9 — редактирование генома</text>
    <text x="137" y="238" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">«Генетические ножницы» — точечное изменение ДНК</text>
    <text x="137" y="250" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}" text-anchor="middle">Нобелевская премия 2020 (Шарпантье, Дудна)</text>

    <!-- Applications -->
    <rect x="260" y="210" width="215" height="45" rx="5" fill="white" stroke="{PRIMARY}" stroke-width="1"/>
    <text x="367" y="225" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">Применение</text>
    <text x="270" y="238" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">🏥 Медицина — генотерапия, вакцины</text>
    <text x="270" y="250" font-family="Arial,sans-serif" font-size="7" fill="{TEXT_MID}">🌾 С/х — устойчивые сорта, биоудобрения</text>

    <!-- Ethics -->
    <rect x="25" y="262" width="450" height="28" rx="5" fill="#FFF3E0" stroke="#F57C00" stroke-width="1"/>
    <text x="250" y="277" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="#E65100" text-anchor="middle">⚠️ Этические проблемы: клонирование человека, ГМО-продукты, генетическая дискриминация</text>
    <text x="250" y="288" font-family="Arial,sans-serif" font-size="7" fill="#BF360C" text-anchor="middle">Необходимость правового регулирования и биоэтики</text>
  </g>
'''
    return svg_header(10) + content + svg_footer("Основы биотехнологии", 10)


# ────────────── Main ──────────────

lessons = [
    lesson1, lesson2, lesson3, lesson4, lesson5,
    lesson6, lesson7, lesson8, lesson9, lesson10
]

generated = 0
errors = []

for i, gen_func in enumerate(lessons, 1):
    svg_content = gen_func()
    filepath = os.path.join(OUTPUT_DIR, f"lesson{i}.svg")
    
    # Validate as XML
    try:
        ET.fromstring(svg_content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)
        generated += 1
        print(f"✅ lesson{i}.svg — valid XML, written successfully")
    except ET.ParseError as e:
        errors.append((i, str(e)))
        # Try to save anyway
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"⚠️ lesson{i}.svg — XML parse error: {e}")

print(f"\n{'='*50}")
print(f"Generated: {generated}/10 files")
if errors:
    print(f"Errors in lessons: {[e[0] for e in errors]}")
    for num, err in errors:
        print(f"  Lesson {num}: {err}")
else:
    print("All files validated as well-formed XML ✅")
