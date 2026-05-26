#!/usr/bin/env python3
"""Add 1 missing lesson to each of 3 incomplete topics in grade 6 + create SVG images."""
import json, os

BASE = "/home/z/school-curriculum-app/public/data/grades/6"
IMG_BASE = "/home/z/school-curriculum-app/public/images/lessons/grade6"

def create_math_svg():
    """Create SVG for 'Графики на координатной плоскости' (math lesson14)"""
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#E3F2FD"/>
      <stop offset="100%" stop-color="#BBDEFB"/>
    </linearGradient>
  </defs>
  <rect width="500" height="350" fill="url(#bg)" rx="10"/>
  <rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#1565C0" stroke-width="3"/>
  <rect x="8" y="8" width="484" height="334" rx="6" fill="none" stroke="#1565C0" stroke-width="1" opacity="0.3"/>
  <polygon points="10,10 30,10 10,30" fill="#0D47A1" opacity="0.08"/>
  <polygon points="490,10 470,10 490,30" fill="#0D47A1" opacity="0.08"/>
  <polygon points="10,340 30,340 10,320" fill="#1976D2" opacity="0.08"/>
  <polygon points="490,340 470,340 490,320" fill="#42A5F5" opacity="0.08"/>
  <circle cx="70" cy="15" r="4" fill="#0D47A1" opacity="0.1"/>
  <circle cx="82" cy="15" r="4" fill="#0D47A1" opacity="0.1"/>
  <circle cx="94" cy="15" r="4" fill="#1976D2" opacity="0.1"/>
  <circle cx="406" cy="15" r="4" fill="#0D47A1" opacity="0.1"/>
  <circle cx="418" cy="15" r="4" fill="#0D47A1" opacity="0.1"/>
  <circle cx="430" cy="15" r="4" fill="#42A5F5" opacity="0.1"/>
  <text x="250" y="50" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#1565C0" text-anchor="middle">Графики на координатной плоскости</text>
  <text x="250" y="68" font-family="Arial,sans-serif" font-size="12" fill="#777" text-anchor="middle">Математика - Урок 14</text>
  <line x1="30" y1="78" x2="470" y2="78" stroke="#1565C0" stroke-width="2" opacity="0.25"/>
  <rect x="30" y="75" width="60" height="6" fill="#1565C0" opacity="0.15" rx="1"/>
  <rect x="410" y="75" width="60" height="6" fill="#1976D2" opacity="0.12" rx="1"/>

  <!-- Main chart area -->
  <rect x="20" y="88" width="290" height="210" rx="6" fill="white" stroke="#1565C0" stroke-width="1.5"/>
  <text x="165" y="104" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" text-anchor="middle" font-weight="bold">Прямая y = 2x - 1</text>
  <line x1="28" y1="108" x2="302" y2="108" stroke="#E0E0E0" stroke-width="1"/>
  <!-- Axes -->
  <line x1="60" y1="260" x2="290" y2="260" stroke="#555" stroke-width="1.5"/>
  <polygon points="290,260 283,256 283,264" fill="#555"/>
  <line x1="80" y1="288" x2="80" y2="118" stroke="#555" stroke-width="1.5"/>
  <polygon points="80,118 76,125 84,125" fill="#555"/>
  <text x="285" y="275" font-family="Arial,sans-serif" font-size="10" fill="#555" font-weight="bold">X</text>
  <text x="87" y="125" font-family="Arial,sans-serif" font-size="10" fill="#555" font-weight="bold">Y</text>
  <text x="84" y="270" font-family="Arial,sans-serif" font-size="9" fill="#555">0</text>
  <!-- Grid lines -->
  <line x1="120" y1="115" x2="120" y2="280" stroke="#E0E0E0" stroke-width="0.5"/>
  <line x1="160" y1="115" x2="160" y2="280" stroke="#E0E0E0" stroke-width="0.5"/>
  <line x1="200" y1="115" x2="200" y2="280" stroke="#E0E0E0" stroke-width="0.5"/>
  <line x1="240" y1="115" x2="240" y2="280" stroke="#E0E0E0" stroke-width="0.5"/>
  <line x1="30" y1="220" x2="295" y2="220" stroke="#E0E0E0" stroke-width="0.5"/>
  <line x1="30" y1="180" x2="295" y2="180" stroke="#E0E0E0" stroke-width="0.5"/>
  <line x1="30" y1="140" x2="295" y2="140" stroke="#E0E0E0" stroke-width="0.5"/>
  <!-- Line y = 2x - 1 -->
  <line x1="60" y1="260" x2="240" y2="120" stroke="#C62828" stroke-width="2.5"/>
  <!-- Points on the line -->
  <circle cx="80" cy="260" r="4" fill="#1565C0" stroke="white" stroke-width="1.5"/>
  <text x="88" y="258" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">(0, -1)</text>
  <circle cx="120" cy="220" r="4" fill="#1565C0" stroke="white" stroke-width="1.5"/>
  <text x="128" y="218" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">(1, 1)</text>
  <circle cx="160" cy="180" r="4" fill="#1565C0" stroke="white" stroke-width="1.5"/>
  <text x="168" y="178" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">(2, 3)</text>
  <circle cx="200" cy="140" r="4" fill="#1565C0" stroke="white" stroke-width="1.5"/>
  <text x="208" y="138" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">(3, 5)</text>

  <!-- Info card: How to plot a graph -->
  <rect x="318" y="88" width="163" height="100" rx="6" fill="white" stroke="#C62828" stroke-width="1.5"/>
  <text x="400" y="104" font-family="Arial,sans-serif" font-size="10" fill="#C62828" text-anchor="middle" font-weight="bold">Построение графика</text>
  <line x1="326" y1="108" x2="473" y2="108" stroke="#E0E0E0" stroke-width="1"/>
  <text x="332" y="125" font-family="Arial,sans-serif" font-size="9" fill="#333">1. Задаём таблицу:</text>
  <text x="332" y="140" font-family="monospace" font-size="8" fill="#1565C0">  x | 0 | 1 | 2 | 3</text>
  <text x="332" y="153" font-family="monospace" font-size="8" fill="#C62828">  y |-1 | 1 | 3 | 5</text>
  <text x="332" y="170" font-family="Arial,sans-serif" font-size="9" fill="#333">2. Строим точки</text>
  <text x="332" y="183" font-family="Arial,sans-serif" font-size="9" fill="#333">3. Соединяем линией</text>

  <!-- Info card: Key concepts -->
  <rect x="318" y="196" width="163" height="102" rx="6" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
  <text x="400" y="212" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle" font-weight="bold">Ключевые понятия</text>
  <line x1="326" y1="216" x2="473" y2="216" stroke="#E0E0E0" stroke-width="1"/>
  <text x="332" y="233" font-family="Arial,sans-serif" font-size="9" fill="#333">&#x2022; График функции</text>
  <text x="332" y="248" font-family="Arial,sans-serif" font-size="9" fill="#333">&#x2022; Аргумент (x)</text>
  <text x="332" y="263" font-family="Arial,sans-serif" font-size="9" fill="#333">&#x2022; Значение функции (y)</text>
  <text x="332" y="278" font-family="Arial,sans-serif" font-size="9" fill="#333">&#x2022; Линейная функция</text>
  <text x="332" y="293" font-family="Arial,sans-serif" font-size="9" fill="#333">&#x2022; Область определения</text>

  <!-- Bottom panel -->
  <rect x="15" y="308" width="470" height="30" rx="4" fill="#1565C0" opacity="0.85"/>
  <text x="250" y="329" font-family="Arial,sans-serif" font-size="15" text-anchor="middle" fill="white" font-weight="bold">Графики на координатной плоскости</text>
  <line x1="430" y1="100" x2="480" y2="100" stroke="#1565C0" stroke-width="0.5" opacity="0.15"/>
  <line x1="430" y1="120" x2="480" y2="120" stroke="#1565C0" stroke-width="0.5" opacity="0.15"/>
  <line x1="430" y1="140" x2="480" y2="140" stroke="#1565C0" stroke-width="0.5" opacity="0.15"/>
  <line x1="445" y1="90" x2="445" y2="150" stroke="#1565C0" stroke-width="0.5" opacity="0.15"/>
  <line x1="460" y1="90" x2="460" y2="150" stroke="#1565C0" stroke-width="0.5" opacity="0.15"/>
</svg>'''

def create_music_svg():
    """Create SVG for 'Музыка в кино и театре' (music lesson8)"""
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FCE4EC"/>
      <stop offset="100%" stop-color="#F8BBD0"/>
    </linearGradient>
  </defs>
  <rect width="500" height="350" fill="url(#bg)" rx="10"/>
  <rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#AD1457" stroke-width="3"/>
  <rect x="8" y="8" width="484" height="334" rx="6" fill="none" stroke="#AD1457" stroke-width="1" opacity="0.3"/>
  <polygon points="10,10 30,10 10,30" fill="#880E4F" opacity="0.08"/>
  <polygon points="490,10 470,10 490,30" fill="#880E4F" opacity="0.08"/>
  <polygon points="10,340 30,340 10,320" fill="#E91E63" opacity="0.08"/>
  <polygon points="490,340 470,340 490,320" fill="#F48FB1" opacity="0.08"/>
  <circle cx="70" cy="15" r="4" fill="#880E4F" opacity="0.1"/>
  <circle cx="82" cy="15" r="4" fill="#880E4F" opacity="0.1"/>
  <circle cx="94" cy="15" r="4" fill="#E91E63" opacity="0.1"/>
  <circle cx="406" cy="15" r="4" fill="#880E4F" opacity="0.1"/>
  <circle cx="418" cy="15" r="4" fill="#880E4F" opacity="0.1"/>
  <circle cx="430" cy="15" r="4" fill="#F48FB1" opacity="0.1"/>
  <text x="250" y="50" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#AD1457" text-anchor="middle">Музыка в кино и театре</text>
  <text x="250" y="68" font-family="Arial,sans-serif" font-size="12" fill="#777" text-anchor="middle">Музыка - Урок 8</text>
  <line x1="30" y1="78" x2="470" y2="78" stroke="#AD1457" stroke-width="2" opacity="0.25"/>
  <rect x="30" y="75" width="60" height="6" fill="#AD1457" opacity="0.15" rx="1"/>
  <rect x="410" y="75" width="60" height="6" fill="#E91E63" opacity="0.12" rx="1"/>

  <!-- Film strip -->
  <rect x="20" y="88" width="220" height="210" rx="6" fill="white" stroke="#AD1457" stroke-width="1.5"/>
  <text x="130" y="104" font-family="Arial,sans-serif" font-size="10" fill="#AD1457" text-anchor="middle" font-weight="bold">Киномузыка</text>
  <line x1="28" y1="108" x2="232" y2="108" stroke="#E0E0E0" stroke-width="1"/>
  <!-- Film strip shape -->
  <rect x="40" y="118" width="180" height="120" rx="4" fill="#FCE4EC" stroke="#AD1457" stroke-width="1"/>
  <rect x="42" y="120" width="176" height="116" rx="3" fill="#1a1a2e"/>
  <!-- Film perforations -->
  <rect x="44" y="125" width="8" height="6" rx="1" fill="#333"/>
  <rect x="44" y="137" width="8" height="6" rx="1" fill="#333"/>
  <rect x="44" y="149" width="8" height="6" rx="1" fill="#333"/>
  <rect x="44" y="161" width="8" height="6" rx="1" fill="#333"/>
  <rect x="44" y="173" width="8" height="6" rx="1" fill="#333"/>
  <rect x="44" y="185" width="8" height="6" rx="1" fill="#333"/>
  <rect x="44" y="197" width="8" height="6" rx="1" fill="#333"/>
  <rect x="208" y="125" width="8" height="6" rx="1" fill="#333"/>
  <rect x="208" y="137" width="8" height="6" rx="1" fill="#333"/>
  <rect x="208" y="149" width="8" height="6" rx="1" fill="#333"/>
  <rect x="208" y="161" width="8" height="6" rx="1" fill="#333"/>
  <rect x="208" y="173" width="8" height="6" rx="1" fill="#333"/>
  <rect x="208" y="185" width="8" height="6" rx="1" fill="#333"/>
  <rect x="208" y="197" width="8" height="6" rx="1" fill="#333"/>
  <!-- Stars on dark screen -->
  <circle cx="100" cy="145" r="2" fill="#FFD700" opacity="0.6"/>
  <circle cx="140" cy="155" r="2.5" fill="#FFD700" opacity="0.7"/>
  <circle cx="170" cy="140" r="1.5" fill="#FFD700" opacity="0.5"/>
  <circle cx="120" cy="170" r="2" fill="#FFD700" opacity="0.6"/>
  <circle cx="155" cy="180" r="1.5" fill="#FFD700" opacity="0.5"/>
  <circle cx="190" cy="165" r="2" fill="#FFD700" opacity="0.7"/>
  <!-- Musical notes floating -->
  <text x="80" y="160" font-family="serif" font-size="18" fill="#AD1457" opacity="0.4">&#9835;</text>
  <text x="160" y="175" font-family="serif" font-size="14" fill="#E91E63" opacity="0.3">&#9834;</text>
  <text x="130" y="195" font-family="serif" font-size="16" fill="#F48FB1" opacity="0.3">&#9833;</text>
  <!-- Sound waves from screen -->
  <path d="M65,210 Q70,205 75,210 Q80,215 85,210" fill="none" stroke="#AD1457" stroke-width="1.2" opacity="0.4"/>
  <path d="M95,210 Q100,205 105,210 Q110,215 115,210" fill="none" stroke="#E91E63" stroke-width="1" opacity="0.3"/>
  <path d="M125,210 Q130,205 135,210 Q140,215 145,210" fill="none" stroke="#F48FB1" stroke-width="0.8" opacity="0.25"/>
  <!-- Label -->
  <text x="130" y="250" font-family="Arial,sans-serif" font-size="8" fill="#AD1457" text-anchor="middle">Музыка создаёт настроение фильма</text>
  <text x="130" y="265" font-family="Arial,sans-serif" font-size="8" fill="#AD1457" text-anchor="middle">и подчёркивает эмоции героев</text>
  <text x="130" y="285" font-family="Arial,sans-serif" font-size="7" fill="#777" text-anchor="middle">Саундтрек, лейтмотив, фон</text>

  <!-- Theatre card -->
  <rect x="248" y="88" width="233" height="100" rx="6" fill="white" stroke="#E91E63" stroke-width="1.5"/>
  <text x="365" y="104" font-family="Arial,sans-serif" font-size="10" fill="#E91E63" text-anchor="middle" font-weight="bold">Музыка в театре</text>
  <line x1="256" y1="108" x2="473" y2="108" stroke="#E0E0E0" stroke-width="1"/>
  <!-- Stage curtains -->
  <path d="M260,115 Q280,130 300,115" fill="#AD1457" opacity="0.15" stroke="#AD1457" stroke-width="1"/>
  <path d="M280,115 Q300,130 320,115" fill="#AD1457" opacity="0.12" stroke="#AD1457" stroke-width="1"/>
  <path d="M300,115 Q320,130 340,115" fill="#AD1457" opacity="0.1" stroke="#AD1457" stroke-width="1"/>
  <path d="M320,115 Q340,130 360,115" fill="#AD1457" opacity="0.12" stroke="#AD1457" stroke-width="1"/>
  <path d="M340,115 Q360,130 380,115" fill="#AD1457" opacity="0.15" stroke="#AD1457" stroke-width="1"/>
  <path d="M380,115 Q400,130 420,115" fill="#AD1457" opacity="0.12" stroke="#AD1457" stroke-width="1"/>
  <path d="M420,115 Q440,130 460,115" fill="#AD1457" opacity="0.15" stroke="#AD1457" stroke-width="1"/>
  <path d="M460,115 Q470,130 475,115" fill="#AD1457" opacity="0.1" stroke="#AD1457" stroke-width="1"/>
  <!-- Stage info -->
  <text x="365" y="148" font-family="Arial,sans-serif" font-size="8" fill="#333">&#x2022; Опера — музыка + драма</text>
  <text x="365" y="162" font-family="Arial,sans-serif" font-size="8" fill="#333">&#x2022; Балет — музыка + танец</text>
  <text x="365" y="176" font-family="Arial,sans-serif" font-size="8" fill="#333">&#x2022; Мюзикл — пение + танцы</text>

  <!-- Examples card -->
  <rect x="248" y="196" width="233" height="102" rx="6" fill="white" stroke="#F48FB1" stroke-width="1.5"/>
  <text x="365" y="212" font-family="Arial,sans-serif" font-size="10" fill="#F48FB1" text-anchor="middle" font-weight="bold">Известные примеры</text>
  <line x1="256" y1="216" x2="473" y2="216" stroke="#E0E0E0" stroke-width="1"/>
  <text x="262" y="233" font-family="Arial,sans-serif" font-size="8" fill="#333">&#x2022; И. Дунаевский — «Дети капитана Гранта»</text>
  <text x="262" y="248" font-family="Arial,sans-serif" font-size="8" fill="#333">&#x2022; Д. Шостакович — «Гамлет»</text>
  <text x="262" y="263" font-family="Arial,sans-serif" font-size="8" fill="#333">&#x2022; С. Прокофьев — «Ромео и Джульетта»</text>
  <text x="262" y="278" font-family="Arial,sans-serif" font-size="8" fill="#333">&#x2022; А. Рыбников — «Юнона и Авось»</text>
  <text x="262" y="293" font-family="Arial,sans-serif" font-size="8" fill="#333">&#x2022; Э. Артемьев — «Свой среди чужих»</text>

  <!-- Bottom panel -->
  <rect x="15" y="308" width="470" height="30" rx="4" fill="#AD1457" opacity="0.85"/>
  <text x="250" y="329" font-family="Arial,sans-serif" font-size="15" text-anchor="middle" fill="white" font-weight="bold">Музыка в кино и театре</text>
  <circle cx="445" cy="130" r="5" fill="#AD1457" opacity="0.12"/>
  <line x1="450" y1="130" x2="450" y2="105" stroke="#AD1457" stroke-width="1" opacity="0.12"/>
  <circle cx="465" cy="125" r="5" fill="#E91E63" opacity="0.1"/>
  <line x1="470" y1="125" x2="470" y2="100" stroke="#E91E63" stroke-width="1" opacity="0.1"/>
</svg>'''

def create_tech_svg():
    """Create SVG for 'Этапы проектной деятельности' (tech lesson9)"""
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ECEFF1"/>
      <stop offset="100%" stop-color="#CFD8DC"/>
    </linearGradient>
  </defs>
  <rect width="500" height="350" fill="url(#bg)" rx="10"/>
  <rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#455A64" stroke-width="3"/>
  <rect x="8" y="8" width="484" height="334" rx="6" fill="none" stroke="#455A64" stroke-width="1" opacity="0.3"/>
  <polygon points="10,10 30,10 10,30" fill="#37474F" opacity="0.08"/>
  <polygon points="490,10 470,10 490,30" fill="#37474F" opacity="0.08"/>
  <polygon points="10,340 30,340 10,320" fill="#546E7A" opacity="0.08"/>
  <polygon points="490,340 470,340 490,320" fill="#90A4AE" opacity="0.08"/>
  <circle cx="70" cy="15" r="4" fill="#37474F" opacity="0.1"/>
  <circle cx="82" cy="15" r="4" fill="#37474F" opacity="0.1"/>
  <circle cx="94" cy="15" r="4" fill="#546E7A" opacity="0.1"/>
  <circle cx="406" cy="15" r="4" fill="#37474F" opacity="0.1"/>
  <circle cx="418" cy="15" r="4" fill="#37474F" opacity="0.1"/>
  <circle cx="430" cy="15" r="4" fill="#90A4AE" opacity="0.1"/>
  <text x="250" y="50" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#455A64" text-anchor="middle">Этапы проектной деятельности</text>
  <text x="250" y="68" font-family="Arial,sans-serif" font-size="12" fill="#777" text-anchor="middle">Технология - Урок 9</text>
  <line x1="30" y1="78" x2="470" y2="78" stroke="#455A64" stroke-width="2" opacity="0.25"/>
  <rect x="30" y="75" width="60" height="6" fill="#455A64" opacity="0.15" rx="1"/>
  <rect x="410" y="75" width="60" height="6" fill="#546E7A" opacity="0.12" rx="1"/>

  <!-- Process flow: 5 stages -->
  <!-- Stage 1 -->
  <rect x="20" y="88" width="88" height="85" rx="6" fill="white" stroke="#455A64" stroke-width="1.5"/>
  <circle cx="64" cy="106" r="12" fill="#455A64" opacity="0.1"/>
  <text x="64" y="110" font-family="Arial,sans-serif" font-size="12" fill="#455A64" text-anchor="middle" font-weight="bold">1</text>
  <text x="64" y="128" font-family="Arial,sans-serif" font-size="8" fill="#455A64" text-anchor="middle" font-weight="bold">Замысел</text>
  <text x="64" y="140" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Идея, цель,</text>
  <text x="64" y="150" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">потребность</text>
  <text x="64" y="164" font-family="Arial,sans-serif" font-size="7" fill="#999" text-anchor="middle">&#x1F4A1;</text>

  <!-- Arrow 1→2 -->
  <line x1="112" y1="130" x2="118" y2="130" stroke="#78909C" stroke-width="2"/>
  <polygon points="118,130 114,126 114,134" fill="#78909C"/>

  <!-- Stage 2 -->
  <rect x="120" y="88" width="88" height="85" rx="6" fill="white" stroke="#546E7A" stroke-width="1.5"/>
  <circle cx="164" cy="106" r="12" fill="#546E7A" opacity="0.1"/>
  <text x="164" y="110" font-family="Arial,sans-serif" font-size="12" fill="#546E7A" text-anchor="middle" font-weight="bold">2</text>
  <text x="164" y="128" font-family="Arial,sans-serif" font-size="8" fill="#546E7A" text-anchor="middle" font-weight="bold">Конструир.</text>
  <text x="164" y="140" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Эскиз, чертёж,</text>
  <text x="164" y="150" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">размеры</text>
  <text x="164" y="164" font-family="Arial,sans-serif" font-size="7" fill="#999" text-anchor="middle">&#x1F4D0;</text>

  <!-- Arrow 2→3 -->
  <line x1="212" y1="130" x2="218" y2="130" stroke="#78909C" stroke-width="2"/>
  <polygon points="218,130 214,126 214,134" fill="#78909C"/>

  <!-- Stage 3 -->
  <rect x="220" y="88" width="88" height="85" rx="6" fill="white" stroke="#607D8B" stroke-width="1.5"/>
  <circle cx="264" cy="106" r="12" fill="#607D8B" opacity="0.1"/>
  <text x="264" y="110" font-family="Arial,sans-serif" font-size="12" fill="#607D8B" text-anchor="middle" font-weight="bold">3</text>
  <text x="264" y="128" font-family="Arial,sans-serif" font-size="8" fill="#607D8B" text-anchor="middle" font-weight="bold">Технология</text>
  <text x="264" y="140" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">План работ,</text>
  <text x="264" y="150" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">инструменты</text>
  <text x="264" y="164" font-family="Arial,sans-serif" font-size="7" fill="#999" text-anchor="middle">&#x1F527;</text>

  <!-- Arrow 3→4 -->
  <line x1="312" y1="130" x2="318" y2="130" stroke="#78909C" stroke-width="2"/>
  <polygon points="318,130 314,126 314,134" fill="#78909C"/>

  <!-- Stage 4 -->
  <rect x="320" y="88" width="88" height="85" rx="6" fill="white" stroke="#78909C" stroke-width="1.5"/>
  <circle cx="364" cy="106" r="12" fill="#78909C" opacity="0.1"/>
  <text x="364" y="110" font-family="Arial,sans-serif" font-size="12" fill="#78909C" text-anchor="middle" font-weight="bold">4</text>
  <text x="364" y="128" font-family="Arial,sans-serif" font-size="8" fill="#78909C" text-anchor="middle" font-weight="bold">Изготовление</text>
  <text x="364" y="140" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Сборка,</text>
  <text x="364" y="150" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">отделка</text>
  <text x="364" y="164" font-family="Arial,sans-serif" font-size="7" fill="#999" text-anchor="middle">&#x1F528;</text>

  <!-- Arrow 4→5 -->
  <line x1="412" y1="130" x2="418" y2="130" stroke="#78909C" stroke-width="2"/>
  <polygon points="418,130 414,126 414,134" fill="#78909C"/>

  <!-- Stage 5 -->
  <rect x="420" y="88" width="68" height="85" rx="6" fill="white" stroke="#90A4AE" stroke-width="1.5"/>
  <circle cx="454" cy="106" r="12" fill="#90A4AE" opacity="0.1"/>
  <text x="454" y="110" font-family="Arial,sans-serif" font-size="12" fill="#90A4AE" text-anchor="middle" font-weight="bold">5</text>
  <text x="454" y="128" font-family="Arial,sans-serif" font-size="8" fill="#90A4AE" text-anchor="middle" font-weight="bold">Оценка</text>
  <text x="454" y="140" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Защита,</text>
  <text x="454" y="150" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">рефлексия</text>
  <text x="454" y="164" font-family="Arial,sans-serif" font-size="7" fill="#999" text-anchor="middle">&#x2B50;</text>

  <!-- Bottom card: Project types -->
  <rect x="20" y="182" width="220" height="116" rx="6" fill="white" stroke="#455A64" stroke-width="1.5"/>
  <text x="130" y="198" font-family="Arial,sans-serif" font-size="10" fill="#455A64" text-anchor="middle" font-weight="bold">Виды проектов</text>
  <line x1="28" y1="202" x2="232" y2="202" stroke="#E0E0E0" stroke-width="1"/>
  <text x="32" y="218" font-family="Arial,sans-serif" font-size="8" fill="#333">&#x2022; Практико-ориентированный</text>
  <text x="40" y="230" font-family="Arial,sans-serif" font-size="7" fill="#777">  Создание полезного изделия</text>
  <text x="32" y="246" font-family="Arial,sans-serif" font-size="8" fill="#333">&#x2022; Исследовательский</text>
  <text x="40" y="258" font-family="Arial,sans-serif" font-size="7" fill="#777">  Изучение проблемы, эксперимент</text>
  <text x="32" y="274" font-family="Arial,sans-serif" font-size="8" fill="#333">&#x2022; Творческий</text>
  <text x="40" y="286" font-family="Arial,sans-serif" font-size="7" fill="#777">  Художественное оформление</text>

  <!-- Right card: Project documentation -->
  <rect x="248" y="182" width="233" height="116" rx="6" fill="white" stroke="#546E7A" stroke-width="1.5"/>
  <text x="365" y="198" font-family="Arial,sans-serif" font-size="10" fill="#546E7A" text-anchor="middle" font-weight="bold">Документация проекта</text>
  <line x1="256" y1="202" x2="473" y2="202" stroke="#E0E0E0" stroke-width="1"/>
  <text x="262" y="218" font-family="Arial,sans-serif" font-size="8" fill="#333">&#x2022; Титульный лист</text>
  <text x="262" y="233" font-family="Arial,sans-serif" font-size="8" fill="#333">&#x2022; Цель и задачи</text>
  <text x="262" y="248" font-family="Arial,sans-serif" font-size="8" fill="#333">&#x2022; Эскиз / чертёж изделия</text>
  <text x="262" y="263" font-family="Arial,sans-serif" font-size="8" fill="#333">&#x2022; Технологическая карта</text>
  <text x="262" y="278" font-family="Arial,sans-serif" font-size="8" fill="#333">&#x2022; Экономический расчёт</text>
  <text x="262" y="293" font-family="Arial,sans-serif" font-size="8" fill="#333">&#x2022; Самооценка результата</text>

  <!-- Bottom panel -->
  <rect x="15" y="308" width="470" height="30" rx="4" fill="#455A64" opacity="0.85"/>
  <text x="250" y="329" font-family="Arial,sans-serif" font-size="15" text-anchor="middle" fill="white" font-weight="bold">Этапы проектной деятельности</text>
  <rect x="440" y="110" width="4" height="30" fill="#455A64" opacity="0.1" transform="rotate(30,442,125)"/>
  <circle cx="435" cy="108" r="6" fill="none" stroke="#455A64" stroke-width="1.5" opacity="0.1"/>
  <rect x="460" y="115" width="4" height="25" fill="#546E7A" opacity="0.08" transform="rotate(-20,462,128)"/>
</svg>'''


def add_lesson_to_json(filepath, topic_name, new_lesson):
    """Add a lesson to a specific topic in the detailedTopics array."""
    with open(filepath, 'r', encoding='utf-8') as f:
        d = json.load(f)

    for t in d['lessons']['detailedTopics']:
        if t['topic'] == topic_name:
            t['lessons'].append(new_lesson)
            break

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"  Added lesson to {topic_name} in {os.path.basename(filepath)}")


def main():
    # 1. Create SVG files
    svg_math = create_math_svg()
    svg_music = create_music_svg()
    svg_tech = create_tech_svg()

    with open(f"{IMG_BASE}/math/lesson14.svg", 'w', encoding='utf-8') as f:
        f.write(svg_math)
    print("Created math/lesson14.svg")

    with open(f"{IMG_BASE}/music/lesson8.svg", 'w', encoding='utf-8') as f:
        f.write(svg_music)
    print("Created music/lesson8.svg")

    with open(f"{IMG_BASE}/tech/lesson9.svg", 'w', encoding='utf-8') as f:
        f.write(svg_tech)
    print("Created tech/lesson9.svg")

    # 2. Add lessons to JSON
    math_lesson = {
        "title": "Графики на координатной плоскости",
        "image": "/images/lessons/grade6/math/lesson14.svg",
        "description": "**График функции** — множество всех точек координатной плоскости, абсциссы которых равны значениям аргумента, а ординаты — соответствующим значениям функции.\n\n**Построение графика линейной функции y = kx + b:**\n1. Составить таблицу значений (выбрать 2-3 значения x)\n2. Вычислить соответствующие значения y\n3. Построить точки на координатной плоскости\n4. Соединить точки прямой линией\n\n**Пример: y = 2x - 1**\n\n| x | 0 | 1 | 2 | 3 |\n|---|---|---|---|---|\n| y | -1 | 1 | 3 | 5 |\n\n**Прямая пропорциональность:** y = kx (график проходит через начало координат)\n- При k > 0 — прямая идёт из III четверти в I\n- При k < 0 — прямая идёт из II четверти в IV\n\n**Взаимное расположение графиков:**\n- Если k одинаковый — прямые параллельны\n- Если k разный — прямые пересекаются",
        "tasks": [
            "Постройте график функции y = 2x - 1 по таблице значений",
            "Принадлежит ли точка A(3; 5) графику функции y = 2x - 1?",
            "Постройте график функции y = -3x + 6 и найдите точку пересечения с осью y",
            "Не выполняя построения, определите, пересекаются ли графики y = 2x + 3 и y = 2x - 1"
        ],
        "examples": [
            "Для y = 2x - 1: при x = 0 получаем y = -1, при x = 2 получаем y = 3",
            "Точка (3; 5) принадлежит графику y = 2x - 1, так как 5 = 2×3 - 1",
            "Графики y = 2x + 3 и y = 2x - 1 параллельны (одинаковый коэффициент k = 2)"
        ],
        "keyPoints": [
            "График линейной функции — прямая линия",
            "Для построения достаточно двух точек",
            "Коэффициент k определяет наклон прямой, b — сдвиг по оси y"
        ],
        "content": "**График функции** — множество всех точек координатной плоскости, абсциссы которых равны значениям аргумента, а ординаты — соответствующим значениям функции.\n\n**Построение графика линейной функции y = kx + b:**\n1. Составить таблицу значений\n2. Вычислить соответствующие значения y\n3. Построить точки на координатной плоскости\n4. Соединить точки прямой линией"
    }

    music_lesson = {
        "title": "Музыка в кино и театре",
        "image": "/images/lessons/grade6/music/lesson8.svg",
        "description": "**Музыка в кино и театре** — один из важнейших элементов художественного произведения, который создаёт атмосферу, подчёркивает эмоции и усиливает воздействие на зрителя.\n\n**Роль музыки в кино:**\n- Создание настроения и атмосферы сцены\n- Характеристика героев (лейтмотив)\n- Передача временной и пространственной среды\n- Усиление драматического напряжения\n\n**Лейтмотив** — музыкальная тема, связанная с определённым персонажем, местом или идеей. Впервые широко применил Рихард Вагнер в своих операх.\n\n**Виды киномузыки:**\n- Внутрикадровая (звучит в самом фильме — радио, концерт)\n- Закадровая (музыкальное сопровождение, не слышимое героями)\n\n**Музыка в театре:**\n- Опера — ведущая роль музыки, пение заменяет речь\n- Балет — сюжет передаётся танцем под оркестровую музыку\n- Мюзикл — сочетание диалогов, пения и хореографии\n- Драматический спектакль — музыкальное оформление и фоновая музыка",
        "tasks": [
            "Объясните, что такое лейтмотив и приведите пример",
            "В чём различие внутрикадровой и закадровой музыки?",
            "Назовите известного композитора, писавшего музыку к фильмам",
            "Какую роль играет музыка в балетном спектакле?"
        ],
        "examples": [
            "Лейтмотив «Имперского марша» из «Звёздных войн» звучит при появлении Дарта Вейдера",
            "И. Дунаевский написал музыку к фильмам «Дети капитана Гранта» и «Весёлые ребята»",
            "В балете «Щелкунчик» музыка Чайковского передаёт характер каждого персонажа"
        ],
        "keyPoints": [
            "Музыка в кино создаёт настроение и характеризует героев",
            "Лейтмотив — музыкальная тема, связанная с персонажем или идеей",
            "Опера, балет и мюзикл — виды театра, где музыка играет ведущую роль"
        ],
        "content": "**Музыка в кино и театре** — важнейший элемент художественного произведения, создающий атмосферу и усиливающий эмоциональное воздействие.\n\n**Роль музыки в кино:** создание настроения, характеристика героев, передача среды.\n\n**Лейтмотив** — музыкальная тема персонажа или идеи.\n\n**Виды киномузыки:** внутрикадровая и закадровая."
    }

    tech_lesson = {
        "title": "Этапы проектной деятельности",
        "image": "/images/lessons/grade6/tech/lesson9.svg",
        "description": "**Проектная деятельность** — процесс создания нового продукта от замысла до оценки результата.\n\n**5 основных этапов проекта:**\n\n**1. Поисково-исследовательский (замысел)**\n- Определение потребности и проблемы\n- Формулировка цели проекта\n- Выбор темы и обоснование\n\n**2. Конструкторский (проектирование)**\n- Разработка эскиза изделия\n- Выполнение чертежа с размерами\n- Выбор материалов и комплектующих\n\n**3. Технологический (планирование)**\n- Составление технологической карты\n- Подбор инструментов и приспособлений\n- Определение последовательности операций\n\n**4. Практический (изготовление)**\n- Выполнение заготовительных операций\n- Сборка и соединение деталей\n- Отделка и оформление изделия\n\n**5. Заключительный (оценка)**\n- Испытание и тестирование изделия\n- Презентация и защита проекта\n- Самооценка и рефлексия\n\n**Документация проекта:**\n- Титульный лист\n- Цель и задачи\n- Эскиз / чертёж\n- Технологическая карта\n- Экономический расчёт\n- Самооценка результата",
        "tasks": [
            "Перечислите 5 основных этапов проектной деятельности",
            "Составьте технологическую карту для изготовления кухонной лопатки",
            "Что должно быть на титульном листе проекта?",
            "В чём разница между конструкторским и технологическим этапами?"
        ],
        "examples": [
            "Цель проекта: изготовить подставку под горячее из древесины",
            "Технологическая карта: 1) Разметка → 2) Выпиливание → 3) Шлифовка → 4) Покрытие лаком",
            "Экономический расчёт: стоимость материалов + затраченное время"
        ],
        "keyPoints": [
            "Проект состоит из 5 этапов: замысел, конструирование, технология, изготовление, оценка",
            "Технологическая карта описывает последовательность операций",
            "Каждый этап завершается конкретным результатом"
        ],
        "content": "**Проектная деятельность** — процесс создания нового продукта от замысла до оценки результата.\n\n**5 этапов:**\n1. Поисково-исследовательский (замысел)\n2. Конструкторский (проектирование)\n3. Технологический (планирование)\n4. Практический (изготовление)\n5. Заключительный (оценка)\n\n**Документация:** титульный лист, цель, эскиз, технологическая карта, экономический расчёт."
    }

    add_lesson_to_json(f"{BASE}/math.json", "Координаты на плоскости", math_lesson)
    add_lesson_to_json(f"{BASE}/music.json", "Музыка и жизнь", music_lesson)
    add_lesson_to_json(f"{BASE}/tech.json", "Проектная деятельность", tech_lesson)

    print("\nDone! Added 3 lessons + 3 SVG images")


if __name__ == "__main__":
    main()
