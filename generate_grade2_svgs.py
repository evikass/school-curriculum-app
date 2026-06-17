#!/usr/bin/env python3
"""Generate unique thematic SVG illustrations for Grade 2 lessons."""

import json
import os
import re

SVG_DIR = 'public/images/lessons/grade2'
GRADE_DIR = 'public/data/grades/2'

def strip_emoji(text):
    """Remove emoji from text for clean SVG content."""
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u200d\u23cf\u23e9\u231a\ufe0f\u3030"
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub('', text).strip()

# ============================================================
# MATH SVGs (12 lessons)
# ============================================================
math_svgs = {
    1: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <style>
      @keyframes pop { 0%,100%{transform:scale(1)} 50%{transform:scale(1.08)} }
      @keyframes slide { 0%{transform:translateX(-5px)} 50%{transform:translateX(5px)} 100%{transform:translateX(-5px)} }
      .num { animation: pop 2s ease-in-out infinite; }
      .arrow { animation: slide 1.5s ease-in-out infinite; }
    </style>
  </defs>
  <rect width="500" height="350" fill="#E8F5E9"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#2E7D32">Образование чисел от 10 до 20</text>
  <!-- Number line 10-20 -->
  <line x1="30" y1="80" x2="470" y2="80" stroke="#2E7D32" stroke-width="3"/>
  <g font-family="Arial,sans-serif" font-size="14" fill="#1B5E20" text-anchor="middle">
    <circle cx="50" cy="80" r="16" fill="#C8E6C9" stroke="#2E7D32" stroke-width="2"/>
    <text x="50" y="85">10</text>
    <circle cx="90" cy="80" r="16" fill="#A5D6A7" stroke="#2E7D32" stroke-width="2"/>
    <text x="90" y="85">11</text>
    <circle cx="130" cy="80" r="16" fill="#81C784" stroke="#2E7D32" stroke-width="2"/>
    <text x="130" y="85">12</text>
    <circle cx="170" cy="80" r="16" fill="#66BB6A" stroke="#2E7D32" stroke-width="2"/>
    <text x="170" y="85">13</text>
    <circle cx="210" cy="80" r="16" fill="#4CAF50" stroke="#2E7D32" stroke-width="2"/>
    <text x="210" y="85">14</text>
    <circle cx="250" cy="80" r="16" fill="#43A047" stroke="#2E7D32" stroke-width="2"/>
    <text x="250" y="85">15</text>
    <circle cx="290" cy="80" r="16" fill="#388E3C" stroke="#2E7D32" stroke-width="2"/>
    <text x="290" y="85">16</text>
    <circle cx="330" cy="80" r="16" fill="#2E7D32" stroke="#1B5E20" stroke-width="2"/>
    <text x="330" y="85" fill="white">17</text>
    <circle cx="370" cy="80" r="16" fill="#1B5E20" stroke="#0D3B0F" stroke-width="2"/>
    <text x="370" y="85" fill="white">18</text>
    <circle cx="410" cy="80" r="16" fill="#1B5E20" stroke="#0D3B0F" stroke-width="2"/>
    <text x="410" y="85" fill="white">19</text>
    <circle cx="450" cy="80" r="16" fill="#0D3B0F" stroke="#0D3B0F" stroke-width="2"/>
    <text x="450" y="85" fill="white">20</text>
  </g>
  <!-- Ten sticks + ones -->
  <g class="num" transform="translate(60,120)">
    <rect x="0" y="0" width="60" height="50" fill="#FFF9C4" rx="8" stroke="#F9A825" stroke-width="2"/>
    <text x="30" y="20" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#E65100">1 десяток</text>
    <text x="30" y="40" text-anchor="middle" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#F57F17">10</text>
  </g>
  <g class="arrow">
    <text x="140" y="150" font-family="Arial,sans-serif" font-size="28" fill="#FF8F00">+</text>
  </g>
  <g class="num" transform="translate(160,120)">
    <rect x="0" y="0" width="60" height="50" fill="#FFECB3" rx="8" stroke="#F9A825" stroke-width="2"/>
    <text x="30" y="20" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#E65100">3 единицы</text>
    <text x="30" y="40" text-anchor="middle" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#F57F17">3</text>
  </g>
  <g class="arrow">
    <text x="240" y="150" font-family="Arial,sans-serif" font-size="28" fill="#2E7D32">=</text>
  </g>
  <g class="num" transform="translate(260,120)">
    <rect x="0" y="0" width="70" height="50" fill="#C8E6C9" rx="8" stroke="#2E7D32" stroke-width="2"/>
    <text x="35" y="20" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#1B5E20">Тринадцать</text>
    <text x="35" y="40" text-anchor="middle" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#2E7D32">13</text>
  </g>
  <!-- Counting blocks -->
  <g transform="translate(50,200)">
    <rect x="0" y="0" width="400" height="60" fill="white" rx="10" stroke="#E0E0E0" stroke-width="1"/>
    <text x="200" y="20" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#555">10 + 1 = 11   10 + 5 = 15   10 + 9 = 19</text>
    <text x="200" y="45" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#2E7D32">Десять и ещё несколько единиц</text>
  </g>
  <!-- Decorative -->
  <rect x="30" y="280" width="440" height="55" fill="#FFF8E1" rx="10"/>
  <text x="250" y="305" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#E65100">Как образуются числа?</text>
  <text x="250" y="325" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#795548">10 + N = 1N (одиннадцать, двенадцать, ..., девятнадцать)</text>
</svg>''',

    2: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <style>
      @keyframes count { 0%,100%{opacity:1} 50%{opacity:0.6} }
      .pulse { animation: count 2s ease-in-out infinite; }
    </style>
  </defs>
  <rect width="500" height="350" fill="#E3F2FD"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#1565C0">Круглые числа и счёт десятками</text>
  <!-- Bundles of 10 -->
  <g transform="translate(30,55)">
    <rect x="0" y="0" width="90" height="70" fill="#BBDEFB" rx="10" stroke="#1565C0" stroke-width="2"/>
    <text x="45" y="25" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" fill="#0D47A1">1 десяток</text>
    <text x="45" y="55" text-anchor="middle" font-family="Arial,sans-serif" font-size="28" font-weight="bold" fill="#1565C0">10</text>
  </g>
  <g transform="translate(130,55)" class="pulse">
    <rect x="0" y="0" width="90" height="70" fill="#90CAF9" rx="10" stroke="#1565C0" stroke-width="2"/>
    <text x="45" y="25" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" fill="#0D47A1">2 десятка</text>
    <text x="45" y="55" text-anchor="middle" font-family="Arial,sans-serif" font-size="28" font-weight="bold" fill="#1565C0">20</text>
  </g>
  <g transform="translate(230,55)">
    <rect x="0" y="0" width="90" height="70" fill="#64B5F6" rx="10" stroke="#1565C0" stroke-width="2"/>
    <text x="45" y="25" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" fill="white">3 десятка</text>
    <text x="45" y="55" text-anchor="middle" font-family="Arial,sans-serif" font-size="28" font-weight="bold" fill="white">30</text>
  </g>
  <g transform="translate(330,55)">
    <rect x="0" y="0" width="90" height="70" fill="#42A5F5" rx="10" stroke="#1565C0" stroke-width="2"/>
    <text x="45" y="25" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" fill="white">5 десятков</text>
    <text x="45" y="55" text-anchor="middle" font-family="Arial,sans-serif" font-size="28" font-weight="bold" fill="white">50</text>
  </g>
  <!-- Number line with round numbers highlighted -->
  <line x1="30" y1="155" x2="470" y2="155" stroke="#1565C0" stroke-width="2"/>
  <g font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="#333">
    <text x="50" y="150">0</text><text x="90" y="150">10</text><text x="130" y="150">20</text>
    <text x="170" y="150">30</text><text x="210" y="150">40</text><text x="250" y="150">50</text>
    <text x="290" y="150">60</text><text x="330" y="150">70</text><text x="370" y="150">80</text>
    <text x="410" y="150">90</text><text x="450" y="150">100</text>
  </g>
  <g font-family="Arial,sans-serif" font-size="12" font-weight="bold" text-anchor="middle" fill="#1565C0">
    <circle cx="50" cy="155" r="4" fill="#1565C0"/>
    <circle cx="90" cy="155" r="6" fill="#1565C0"/>
    <circle cx="130" cy="155" r="6" fill="#1565C0"/>
    <circle cx="170" cy="155" r="6" fill="#1565C0"/>
    <circle cx="210" cy="155" r="6" fill="#1565C0"/>
    <circle cx="250" cy="155" r="6" fill="#1565C0"/>
    <circle cx="290" cy="155" r="6" fill="#1565C0"/>
    <circle cx="330" cy="155" r="6" fill="#1565C0"/>
    <circle cx="370" cy="155" r="6" fill="#1565C0"/>
    <circle cx="410" cy="155" r="6" fill="#1565C0"/>
    <circle cx="450" cy="155" r="6" fill="#1565C0"/>
  </g>
  <!-- Counting by tens -->
  <rect x="30" y="175" width="440" height="80" fill="white" rx="10" stroke="#BBDEFB" stroke-width="2"/>
  <text x="250" y="200" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#1565C0">Считаем десятками:</text>
  <text x="250" y="225" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" fill="#0D47A1">10, 20, 30, 40, 50, 60, 70, 80, 90, 100</text>
  <text x="250" y="245" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">Круглые числа оканчиваются нулём</text>
  <!-- Visual bundles -->
  <g transform="translate(50,270)">
    <rect x="0" y="0" width="400" height="65" fill="#E3F2FD" rx="10"/>
    <g transform="translate(15,10)">
      <rect x="0" y="0" width="30" height="45" fill="#BBDEFB" rx="5" stroke="#1565C0" stroke-width="1"/>
      <text x="15" y="28" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#1565C0">10</text>
    </g>
    <g transform="translate(55,10)">
      <rect x="0" y="0" width="30" height="45" fill="#90CAF9" rx="5" stroke="#1565C0" stroke-width="1"/>
      <text x="15" y="28" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#1565C0">10</text>
    </g>
    <g transform="translate(95,10)">
      <rect x="0" y="0" width="30" height="45" fill="#64B5F6" rx="5" stroke="#1565C0" stroke-width="1"/>
      <text x="15" y="28" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#1565C0">10</text>
    </g>
    <text x="200" y="25" font-family="Arial,sans-serif" font-size="14" fill="#1565C0">3 пучка по 10 = 30</text>
    <text x="200" y="45" font-family="Arial,sans-serif" font-size="12" fill="#555">Три десятка = тридцать</text>
  </g>
</svg>''',

    3: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <style>
      @keyframes highlight { 0%,100%{fill:#FFF9C4} 50%{fill:#FFECB3} }
      .tens-box { animation: highlight 2s ease-in-out infinite; }
    </style>
  </defs>
  <rect width="500" height="350" fill="#FFF3E0"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#E65100">Двузначные числа и их разряды</text>
  <!-- Place value chart -->
  <rect x="80" y="50" width="340" height="90" fill="white" rx="10" stroke="#E65100" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#E65100">Разрядная таблица</text>
  <!-- Tens column -->
  <rect x="100" y="80" width="130" height="45" class="tens-box" rx="8" stroke="#FF8F00" stroke-width="2"/>
  <text x="165" y="100" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#E65100">Десятки</text>
  <text x="165" y="118" text-anchor="middle" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#FF8F00">3</text>
  <!-- Ones column -->
  <rect x="270" y="80" width="130" height="45" fill="#E8F5E9" rx="8" stroke="#2E7D32" stroke-width="2"/>
  <text x="335" y="100" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#2E7D32">Единицы</text>
  <text x="335" y="118" text-anchor="middle" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#2E7D32">7</text>
  <!-- Arrow to number -->
  <text x="250" y="165" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" fill="#555">3 десятка + 7 единиц =</text>
  <text x="250" y="195" text-anchor="middle" font-family="Arial,sans-serif" font-size="36" font-weight="bold" fill="#E65100">37</text>
  <!-- More examples -->
  <g transform="translate(30,215)">
    <rect x="0" y="0" width="140" height="55" fill="white" rx="8" stroke="#BBDEFB" stroke-width="1"/>
    <text x="70" y="22" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#1565C0">5 дес. + 2 ед.</text>
    <text x="70" y="45" text-anchor="middle" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#1565C0">52</text>
  </g>
  <g transform="translate(180,215)">
    <rect x="0" y="0" width="140" height="55" fill="white" rx="8" stroke="#F8BBD0" stroke-width="1"/>
    <text x="70" y="22" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#C2185B">8 дес. + 4 ед.</text>
    <text x="70" y="45" text-anchor="middle" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#C2185B">84</text>
  </g>
  <g transform="translate(330,215)">
    <rect x="0" y="0" width="140" height="55" fill="white" rx="8" stroke="#C8E6C9" stroke-width="1"/>
    <text x="70" y="22" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#2E7D32">9 дес. + 0 ед.</text>
    <text x="70" y="45" text-anchor="middle" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#2E7D32">90</text>
  </g>
  <!-- Rule -->
  <rect x="30" y="285" width="440" height="55" fill="#FFF8E1" rx="10"/>
  <text x="250" y="308" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#E65100">Двузначное число = десятки + единицы</text>
  <text x="250" y="328" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#795548">Первая цифра слева — десятки, вторая — единицы</text>
</svg>''',

    4: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <style>
      @keyframes addSlide { 0%{transform:translateX(0)} 50%{transform:translateX(10px)} 100%{transform:translateX(0)} }
      .slide { animation: addSlide 2s ease-in-out infinite; }
    </style>
  </defs>
  <rect width="500" height="350" fill="#F3E5F5"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#6A1B9A">Сложение двузначных чисел</text>
  <!-- Example 1 -->
  <rect x="30" y="50" width="440" height="80" fill="white" rx="10" stroke="#CE93D8" stroke-width="2"/>
  <text x="250" y="75" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#6A1B9A">Пример: 23 + 14</text>
  <g transform="translate(50,85)" font-family="Arial,sans-serif" font-size="14">
    <rect x="0" y="0" width="80" height="30" fill="#E1BEE7" rx="5"/>
    <text x="40" y="22" text-anchor="middle" fill="#6A1B9A">2 дес. + 1 дес.</text>
  </g>
  <g class="slide" transform="translate(150,85)" font-family="Arial,sans-serif" font-size="20" fill="#6A1B9A">
    <text x="15" y="22">+</text>
  </g>
  <g transform="translate(190,85)" font-family="Arial,sans-serif" font-size="14">
    <rect x="0" y="0" width="80" height="30" fill="#F3E5F5" rx="5"/>
    <text x="40" y="22" text-anchor="middle" fill="#6A1B9A">3 ед. + 4 ед.</text>
  </g>
  <text x="310" y="107" font-family="Arial,sans-serif" font-size="16" fill="#6A1B9A">= 3 дес. 7 ед. =</text>
  <text x="450" y="107" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#6A1B9A">37</text>
  <!-- Column method -->
  <rect x="30" y="145" width="440" height="120" fill="white" rx="10" stroke="#CE93D8" stroke-width="2"/>
  <text x="250" y="168" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#6A1B9A">Сложение столбиком</text>
  <g font-family="monospace" font-size="24" fill="#333" text-anchor="end">
    <text x="280" y="200">  2 3</text>
    <text x="280" y="225">+ 1 4</text>
    <line x1="210" y1="230" x2="290" y2="230" stroke="#6A1B9A" stroke-width="2"/>
    <text x="280" y="255" font-weight="bold" fill="#6A1B9A">  3 7</text>
  </g>
  <g transform="translate(310,180)" font-family="Arial,sans-serif" font-size="11" fill="#555">
    <text x="0" y="0">Единицы: 3+4=7</text>
    <text x="0" y="20">Десятки: 2+1=3</text>
  </g>
  <!-- Rule -->
  <rect x="30" y="280" width="440" height="55" fill="#F3E5F5" rx="10"/>
  <text x="250" y="303" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#6A1B9A">Правило сложения</text>
  <text x="250" y="323" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">Единицы складываем с единицами, десятки с десятками</text>
</svg>''',

    5: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <style>
      @keyframes minus { 0%,100%{opacity:1} 50%{opacity:0.5} }
      .fade { animation: minus 2s ease-in-out infinite; }
    </style>
  </defs>
  <rect width="500" height="350" fill="#FFEBEE"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#C62828">Вычитание двузначных чисел</text>
  <!-- Example -->
  <rect x="30" y="50" width="440" height="80" fill="white" rx="10" stroke="#EF9A9A" stroke-width="2"/>
  <text x="250" y="75" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#C62828">Пример: 56 - 23</text>
  <g font-family="Arial,sans-serif" font-size="14" fill="#C62828">
    <text x="80" y="110">5 дес. - 2 дес. = 3 дес.</text>
    <text x="280" y="110">6 ед. - 3 ед. = 3 ед.</text>
  </g>
  <text x="250" y="125" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" font-weight="bold" fill="#C62828">= 33</text>
  <!-- Column method -->
  <rect x="30" y="145" width="440" height="120" fill="white" rx="10" stroke="#EF9A9A" stroke-width="2"/>
  <text x="250" y="168" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#C62828">Вычитание столбиком</text>
  <g font-family="monospace" font-size="24" fill="#333" text-anchor="end">
    <text x="280" y="200">  5 6</text>
    <text x="280" y="225">- 2 3</text>
    <line x1="210" y1="230" x2="290" y2="230" stroke="#C62828" stroke-width="2"/>
    <text x="280" y="255" font-weight="bold" fill="#C62828">  3 3</text>
  </g>
  <g transform="translate(310,180)" font-family="Arial,sans-serif" font-size="11" fill="#555">
    <text x="0" y="0">Единицы: 6-3=3</text>
    <text x="0" y="20">Десятки: 5-2=3</text>
  </g>
  <!-- With borrowing -->
  <rect x="30" y="280" width="440" height="55" fill="#FFEBEE" rx="10"/>
  <text x="250" y="303" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#C62828">Если единиц не хватает — занимаем десяток</text>
  <text x="250" y="323" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">42 - 17: занимаем 1 десяток, будет 12-7=5, а 3-1=2, ответ: 25</text>
</svg>''',

    6: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <style>
      @keyframes multiply { 0%,100%{transform:scale(1)} 50%{transform:scale(1.05)} }
      .grow { animation: multiply 2s ease-in-out infinite; }
    </style>
  </defs>
  <rect width="500" height="350" fill="#E0F2F1"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#00695C">Что такое умножение?</text>
  <!-- Visual: groups of objects -->
  <g transform="translate(30,50)">
    <rect x="0" y="0" width="200" height="100" fill="white" rx="10" stroke="#80CBC4" stroke-width="2"/>
    <text x="100" y="20" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#00695C">3 группы по 4 яблока</text>
    <!-- Group 1 -->
    <g transform="translate(10,30)">
      <circle cx="10" cy="15" r="10" fill="#F44336"/><circle cx="35" cy="15" r="10" fill="#F44336"/>
      <circle cx="60" cy="15" r="10" fill="#F44336"/><circle cx="85" cy="15" r="10" fill="#F44336"/>
    </g>
    <!-- Group 2 -->
    <g transform="translate(10,55)">
      <circle cx="10" cy="15" r="10" fill="#FF9800"/><circle cx="35" cy="15" r="10" fill="#FF9800"/>
      <circle cx="60" cy="15" r="10" fill="#FF9800"/><circle cx="85" cy="15" r="10" fill="#FF9800"/>
    </g>
    <!-- Group 3 -->
    <g transform="translate(10,80)">
      <circle cx="10" cy="15" r="10" fill="#FFC107"/><circle cx="35" cy="15" r="10" fill="#FFC107"/>
      <circle cx="60" cy="15" r="10" fill="#FFC107"/><circle cx="85" cy="15" r="10" fill="#FFC107"/>
    </g>
  </g>
  <!-- Equation -->
  <g class="grow" transform="translate(260,70)">
    <rect x="0" y="0" width="210" height="80" fill="#B2DFDB" rx="10" stroke="#00695C" stroke-width="2"/>
    <text x="105" y="30" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" fill="#00695C">4 + 4 + 4 = 12</text>
    <text x="105" y="55" text-anchor="middle" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#00695C">4 x 3 = 12</text>
  </g>
  <!-- Definition -->
  <rect x="30" y="170" width="440" height="60" fill="white" rx="10" stroke="#80CBC4" stroke-width="2"/>
  <text x="250" y="195" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#00695C">Умножение — это сложение одинаковых слагаемых</text>
  <text x="250" y="218" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">Первый множитель — число в группе, второй — количество групп</text>
  <!-- Terminology -->
  <rect x="30" y="245" width="440" height="95" fill="#E0F2F1" rx="10"/>
  <text x="250" y="270" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#00695C">Названия компонентов</text>
  <g font-family="Arial,sans-serif" font-size="14" text-anchor="middle">
    <text x="130" y="295" fill="#00695C" font-weight="bold">4</text>
    <text x="175" y="295" fill="#555">x</text>
    <text x="220" y="295" fill="#00695C" font-weight="bold">3</text>
    <text x="265" y="295" fill="#555">=</text>
    <text x="310" y="295" fill="#00695C" font-weight="bold">12</text>
  </g>
  <g font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="#555">
    <text x="130" y="315">множитель</text>
    <text x="220" y="315">множитель</text>
    <text x="310" y="315">произведение</text>
  </g>
</svg>''',

    7: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <style>
      @keyframes twotimes { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-5px)} }
      .bounce { animation: twotimes 1.5s ease-in-out infinite; }
    </style>
  </defs>
  <rect width="500" height="350" fill="#FCE4EC"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#880E4F">Таблица умножения на 2</text>
  <!-- Table of 2 -->
  <rect x="30" y="50" width="440" height="250" fill="white" rx="10" stroke="#F48FB1" stroke-width="2"/>
  <text x="250" y="75" text-anchor="middle" font-family="Arial,sans-serif" font-size="15" font-weight="bold" fill="#880E4F">Умножение на 2 — это удвоение!</text>
  <g font-family="Arial,sans-serif" font-size="16" fill="#880E4F">
    <text x="80" y="105">2 x 1 = 2</text>
    <text x="280" y="105">2 x 6 = 12</text>
    <text x="80" y="130">2 x 2 = 4</text>
    <text x="280" y="130">2 x 7 = 14</text>
    <text x="80" y="155">2 x 3 = 6</text>
    <text x="280" y="155">2 x 8 = 16</text>
    <text x="80" y="180">2 x 4 = 8</text>
    <text x="280" y="180">2 x 9 = 18</text>
    <text x="80" y="205">2 x 5 = 10</text>
    <text x="280" y="205">2 x 10 = 20</text>
  </g>
  <!-- Visual: pairs -->
  <g class="bounce" transform="translate(60,225)">
    <circle cx="0" cy="15" r="12" fill="#F48FB1"/><circle cx="30" cy="15" r="12" fill="#F48FB1"/>
    <text x="55" y="22" font-family="Arial,sans-serif" font-size="12" fill="#880E4F">2 x 1 = 2</text>
    <circle cx="130" cy="15" r="12" fill="#EC407A"/><circle cx="160" cy="15" r="12" fill="#EC407A"/>
    <circle cx="190" cy="15" r="12" fill="#EC407A"/><circle cx="220" cy="15" r="12" fill="#EC407A"/>
    <text x="245" y="22" font-family="Arial,sans-serif" font-size="12" fill="#880E4F">2 x 2 = 4</text>
  </g>
  <!-- Tip -->
  <rect x="50" y="270" width="400" height="30" fill="#FCE4EC" rx="8"/>
  <text x="250" y="290" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#880E4F">Каждый ответ больше предыдущего на 2</text>
</svg>''',

    8: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <style>
      @keyframes threecount { 0%,100%{transform:scale(1)} 50%{transform:scale(1.06)} }
      .pulse3 { animation: threecount 2s ease-in-out infinite; }
    </style>
  </defs>
  <rect width="500" height="350" fill="#FFF8E1"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#E65100">Таблица умножения на 3</text>
  <!-- Table of 3 -->
  <rect x="30" y="50" width="440" height="210" fill="white" rx="10" stroke="#FFB74D" stroke-width="2"/>
  <text x="250" y="75" text-anchor="middle" font-family="Arial,sans-serif" font-size="15" font-weight="bold" fill="#E65100">Умножение на 3 — это утроение!</text>
  <g font-family="Arial,sans-serif" font-size="16" fill="#E65100">
    <text x="80" y="105">3 x 1 = 3</text>
    <text x="280" y="105">3 x 6 = 18</text>
    <text x="80" y="130">3 x 2 = 6</text>
    <text x="280" y="130">3 x 7 = 21</text>
    <text x="80" y="155">3 x 3 = 9</text>
    <text x="280" y="155">3 x 8 = 24</text>
    <text x="80" y="180">3 x 4 = 12</text>
    <text x="280" y="180">3 x 9 = 27</text>
    <text x="80" y="205">3 x 5 = 15</text>
    <text x="280" y="205">3 x 10 = 30</text>
  </g>
  <!-- Visual: triplets -->
  <g class="pulse3" transform="translate(60,230)">
    <circle cx="0" cy="15" r="10" fill="#FFB74D"/><circle cx="25" cy="15" r="10" fill="#FFB74D"/><circle cx="50" cy="15" r="10" fill="#FFB74D"/>
    <text x="75" y="22" font-family="Arial,sans-serif" font-size="12" fill="#E65100">3 x 1 = 3</text>
    <circle cx="150" cy="5" r="10" fill="#FFA726"/><circle cx="175" cy="5" r="10" fill="#FFA726"/><circle cx="200" cy="5" r="10" fill="#FFA726"/>
    <circle cx="150" cy="25" r="10" fill="#FFA726"/><circle cx="175" cy="25" r="10" fill="#FFA726"/><circle cx="200" cy="25" r="10" fill="#FFA726"/>
    <text x="225" y="22" font-family="Arial,sans-serif" font-size="12" fill="#E65100">3 x 2 = 6</text>
  </g>
  <!-- Tip -->
  <rect x="30" y="280" width="440" height="55" fill="#FFF8E1" rx="10"/>
  <text x="250" y="303" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#E65100">Сумма цифр ответа всегда равна 3, 6 или 9</text>
  <text x="250" y="323" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">12 (1+2=3), 15 (1+5=6), 18 (1+8=9), 21 (2+1=3)</text>
</svg>''',

    9: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <style>
      @keyframes divide { 0%,100%{transform:scale(1)} 50%{transform:scale(1.05)} }
      .grow { animation: divide 2s ease-in-out infinite; }
    </style>
  </defs>
  <rect width="500" height="350" fill="#E8EAF6"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#283593">Что такое деление?</text>
  <!-- Visual: sharing -->
  <rect x="30" y="50" width="440" height="100" fill="white" rx="10" stroke="#9FA8DA" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#283593">12 яблок разделили на 3 тарелки поровну</text>
  <!-- Plate 1 -->
  <g transform="translate(60,85)">
    <ellipse cx="50" cy="25" rx="45" ry="18" fill="#E8EAF6" stroke="#283593" stroke-width="2"/>
    <circle cx="35" cy="20" r="8" fill="#F44336"/><circle cx="50" cy="20" r="8" fill="#F44336"/><circle cx="65" cy="20" r="8" fill="#F44336"/><circle cx="80" cy="20" r="8" fill="#F44336"/>
    <text x="50" y="52" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#283593">4 яблока</text>
  </g>
  <!-- Plate 2 -->
  <g transform="translate(195,85)">
    <ellipse cx="50" cy="25" rx="45" ry="18" fill="#E8EAF6" stroke="#283593" stroke-width="2"/>
    <circle cx="35" cy="20" r="8" fill="#FF9800"/><circle cx="50" cy="20" r="8" fill="#FF9800"/><circle cx="65" cy="20" r="8" fill="#FF9800"/><circle cx="80" cy="20" r="8" fill="#FF9800"/>
    <text x="50" y="52" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#283593">4 яблока</text>
  </g>
  <!-- Plate 3 -->
  <g transform="translate(330,85)">
    <ellipse cx="50" cy="25" rx="45" ry="18" fill="#E8EAF6" stroke="#283593" stroke-width="2"/>
    <circle cx="35" cy="20" r="8" fill="#FFC107"/><circle cx="50" cy="20" r="8" fill="#FFC107"/><circle cx="65" cy="20" r="8" fill="#FFC107"/><circle cx="80" cy="20" r="8" fill="#FFC107"/>
    <text x="50" y="52" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#283593">4 яблока</text>
  </g>
  <!-- Equation -->
  <g class="grow" transform="translate(100,170)">
    <rect x="0" y="0" width="300" height="50" fill="#C5CAE9" rx="10" stroke="#283593" stroke-width="2"/>
    <text x="150" y="33" text-anchor="middle" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="#283593">12 : 3 = 4</text>
  </g>
  <!-- Terminology -->
  <rect x="30" y="240" width="440" height="95" fill="white" rx="10" stroke="#9FA8DA" stroke-width="2"/>
  <text x="250" y="265" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#283593">Названия компонентов</text>
  <g font-family="Arial,sans-serif" font-size="14" text-anchor="middle">
    <text x="130" y="290" fill="#283593" font-weight="bold">12</text>
    <text x="190" y="290" fill="#555">:</text>
    <text x="230" y="290" fill="#283593" font-weight="bold">3</text>
    <text x="280" y="290" fill="#555">=</text>
    <text x="330" y="290" fill="#283593" font-weight="bold">4</text>
  </g>
  <g font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="#555">
    <text x="130" y="310">делимое</text>
    <text x="230" y="310">делитель</text>
    <text x="330" y="310">частное</text>
  </g>
  <text x="250" y="330" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#283593">Деление — обратная операция умножению: 4 x 3 = 12</text>
</svg>''',

    10: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <style>
      @keyframes split2 { 0%,100%{opacity:1} 50%{opacity:0.7} }
      .blink { animation: split2 1.5s ease-in-out infinite; }
    </style>
  </defs>
  <rect width="500" height="350" fill="#F1F8E9"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#33691E">Деление на 2 и на 3</text>
  <!-- Divide by 2 -->
  <rect x="30" y="50" width="210" height="130" fill="white" rx="10" stroke="#8BC34A" stroke-width="2"/>
  <text x="135" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#33691E">Деление на 2</text>
  <g font-family="Arial,sans-serif" font-size="13" fill="#33691E">
    <text x="55" y="95">2 : 2 = 1</text>
    <text x="55" y="112">4 : 2 = 2</text>
    <text x="55" y="129">6 : 2 = 3</text>
    <text x="55" y="146">8 : 2 = 4</text>
    <text x="55" y="163">10 : 2 = 5</text>
    <text x="150" y="95">12 : 2 = 6</text>
    <text x="150" y="112">14 : 2 = 7</text>
    <text x="150" y="129">16 : 2 = 8</text>
    <text x="150" y="146">18 : 2 = 9</text>
    <text x="150" y="163">20 : 2 = 10</text>
  </g>
  <!-- Divide by 3 -->
  <rect x="260" y="50" width="210" height="130" fill="white" rx="10" stroke="#FF9800" stroke-width="2"/>
  <text x="365" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#E65100">Деление на 3</text>
  <g font-family="Arial,sans-serif" font-size="13" fill="#E65100">
    <text x="280" y="95">3 : 3 = 1</text>
    <text x="280" y="112">6 : 3 = 2</text>
    <text x="280" y="129">9 : 3 = 3</text>
    <text x="280" y="146">12 : 3 = 4</text>
    <text x="280" y="163">15 : 3 = 5</text>
    <text x="375" y="95">18 : 3 = 6</text>
    <text x="375" y="112">21 : 3 = 7</text>
    <text x="375" y="129">24 : 3 = 8</text>
    <text x="375" y="146">27 : 3 = 9</text>
    <text x="375" y="163">30 : 3 = 10</text>
  </g>
  <!-- Connection -->
  <rect x="30" y="195" width="440" height="65" fill="#F1F8E9" rx="10"/>
  <text x="250" y="218" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#33691E">Связь умножения и деления</text>
  <text x="250" y="240" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#555">Если 2 x 5 = 10, то 10 : 2 = 5 и 10 : 5 = 2</text>
  <!-- Visual -->
  <g class="blink" transform="translate(60,275)">
    <rect x="0" y="0" width="180" height="55" fill="white" rx="8" stroke="#8BC34A" stroke-width="1"/>
    <circle cx="25" cy="28" r="12" fill="#8BC34A"/><circle cx="55" cy="28" r="12" fill="#8BC34A"/>
    <circle cx="85" cy="28" r="12" fill="#8BC34A"/><circle cx="115" cy="28" r="12" fill="#8BC34A"/>
    <circle cx="145" cy="28" r="12" fill="#8BC34A"/>
    <text x="95" y="50" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#33691E">10 : 2 = 5 пар</text>
  </g>
  <g transform="translate(270,275)">
    <rect x="0" y="0" width="200" height="55" fill="white" rx="8" stroke="#FF9800" stroke-width="1"/>
    <circle cx="20" cy="28" r="10" fill="#FF9800"/><circle cx="45" cy="28" r="10" fill="#FF9800"/><circle cx="70" cy="28" r="10" fill="#FF9800"/>
    <circle cx="95" cy="28" r="10" fill="#FF9800"/><circle cx="120" cy="28" r="10" fill="#FF9800"/><circle cx="145" cy="28" r="10" fill="#FF9800"/>
    <circle cx="170" cy="28" r="10" fill="#FF9800"/>
    <text x="95" y="50" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#E65100">21 : 3 = 7 троек</text>
  </g>
</svg>''',

    11: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <style>
      @keyframes think { 0%,100%{transform:rotate(-3deg)} 50%{transform:rotate(3deg)} }
      .wobble { animation: think 2s ease-in-out infinite; }
    </style>
  </defs>
  <rect width="500" height="350" fill="#FFF3E0"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#BF360C">Решение задач</text>
  <!-- Problem card -->
  <rect x="30" y="50" width="440" height="90" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <text x="50" y="75" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#BF360C">Задача:</text>
  <text x="50" y="95" font-family="Arial,sans-serif" font-size="13" fill="#333">В корзине 8 яблок, а груш на 3 больше.</text>
  <text x="50" y="115" font-family="Arial,sans-serif" font-size="13" fill="#333">Сколько груш в корзине?</text>
  <!-- Steps -->
  <g transform="translate(30,155)">
    <rect x="0" y="0" width="105" height="55" fill="#FFCCBC" rx="8" stroke="#BF360C" stroke-width="1"/>
    <text x="52" y="22" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#BF360C">1. Условие</text>
    <text x="52" y="40" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">Яб. - 8</text>
    <text x="52" y="52" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">Гр. - ? на 3 б.</text>
  </g>
  <g class="wobble" transform="translate(145,155)">
    <rect x="0" y="0" width="105" height="55" fill="#FFE0B2" rx="8" stroke="#BF360C" stroke-width="1"/>
    <text x="52" y="22" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#BF360C">2. Вопрос</text>
    <text x="52" y="45" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">Сколько груш?</text>
  </g>
  <g transform="translate(260,155)">
    <rect x="0" y="0" width="105" height="55" fill="#FFF9C4" rx="8" stroke="#BF360C" stroke-width="1"/>
    <text x="52" y="22" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#BF360C">3. Решение</text>
    <text x="52" y="45" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#333">8 + 3 = 11</text>
  </g>
  <g transform="translate(375,155)">
    <rect x="0" y="0" width="95" height="55" fill="#C8E6C9" rx="8" stroke="#2E7D32" stroke-width="1"/>
    <text x="47" y="22" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#2E7D32">4. Ответ</text>
    <text x="47" y="45" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#2E7D32">11 груш</text>
  </g>
  <!-- Types -->
  <rect x="30" y="225" width="440" height="110" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <text x="250" y="248" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#BF360C">Типы задач</text>
  <g font-family="Arial,sans-serif" font-size="12">
    <rect x="50" y="258" width="120" height="28" fill="#FFCCBC" rx="5"/>
    <text x="110" y="277" text-anchor="middle" fill="#BF360C">На сложение</text>
    <rect x="185" y="258" width="120" height="28" fill="#BBDEFB" rx="5"/>
    <text x="245" y="277" text-anchor="middle" fill="#1565C0">На вычитание</text>
    <rect x="320" y="258" width="130" height="28" fill="#C8E6C9" rx="5"/>
    <text x="385" y="277" text-anchor="middle" fill="#2E7D32">На умножение</text>
  </g>
  <text x="250" y="318" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Внимательно читай условие, выдели вопрос, запиши решение!</text>
</svg>''',

    12: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <style>
      @keyframes measure { 0%,100%{transform:translateX(0)} 50%{transform:translateX(3px)} }
      .ruler { animation: measure 2s ease-in-out infinite; }
    </style>
  </defs>
  <rect width="500" height="350" fill="#E0F7FA"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#006064">Периметр фигур</text>
  <!-- Triangle -->
  <g transform="translate(30,50)">
    <rect x="0" y="0" width="200" height="140" fill="white" rx="10" stroke="#80DEEA" stroke-width="2"/>
    <polygon points="100,15 20,120 180,120" fill="none" stroke="#00838F" stroke-width="3"/>
    <text x="100" y="70" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#00838F">5 см</text>
    <text x="45" y="130" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#00838F">4 см</text>
    <text x="155" y="130" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#00838F">3 см</text>
  </g>
  <text x="130" y="210" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#00838F">P = 5+4+3 = 12 см</text>
  <!-- Rectangle -->
  <g transform="translate(260,50)">
    <rect x="0" y="0" width="210" height="140" fill="white" rx="10" stroke="#80DEEA" stroke-width="2"/>
    <rect x="40" y="20" width="130" height="90" fill="none" stroke="#00838F" stroke-width="3"/>
    <text x="105" y="60" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#00838F">6 см</text>
    <text x="20" y="70" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#00838F" transform="rotate(-90,20,70)">4 см</text>
  </g>
  <text x="365" y="210" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#00838F">P = (6+4)x2 = 20 см</text>
  <!-- Ruler -->
  <g class="ruler" transform="translate(30,230)">
    <rect x="0" y="0" width="440" height="30" fill="#FFECB3" rx="5" stroke="#F9A825" stroke-width="1"/>
    <g font-family="Arial,sans-serif" font-size="9" fill="#795548" text-anchor="middle">
      <line x1="22" y1="0" x2="22" y2="15" stroke="#795548" stroke-width="1"/><text x="22" y="25">1</text>
      <line x1="66" y1="0" x2="66" y2="15" stroke="#795548" stroke-width="1"/><text x="66" y="25">2</text>
      <line x1="110" y1="0" x2="110" y2="15" stroke="#795548" stroke-width="1"/><text x="110" y="25">3</text>
      <line x1="154" y1="0" x2="154" y2="15" stroke="#795548" stroke-width="1"/><text x="154" y="25">4</text>
      <line x1="198" y1="0" x2="198" y2="15" stroke="#795548" stroke-width="1"/><text x="198" y="25">5</text>
      <line x1="242" y1="0" x2="242" y2="15" stroke="#795548" stroke-width="1"/><text x="242" y="25">6</text>
      <line x1="286" y1="0" x2="286" y2="15" stroke="#795548" stroke-width="1"/><text x="286" y="25">7</text>
      <line x1="330" y1="0" x2="330" y2="15" stroke="#795548" stroke-width="1"/><text x="330" y="25">8</text>
      <line x1="374" y1="0" x2="374" y2="15" stroke="#795548" stroke-width="1"/><text x="374" y="25">9</text>
      <line x1="418" y1="0" x2="418" y2="15" stroke="#795548" stroke-width="1"/><text x="418" y="25">10</text>
    </g>
  </g>
  <!-- Definition -->
  <rect x="30" y="275" width="440" height="60" fill="#E0F7FA" rx="10"/>
  <text x="250" y="298" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#006064">Периметр — сумма длин всех сторон</text>
  <text x="250" y="318" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">P = a + b + c + ... (сложить все стороны)</text>
</svg>'''
}

# ============================================================
# RUSSIAN SVGs (10 lessons)
# ============================================================
russian_svgs = {
    1: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <style>
      @keyframes person { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-3px)} }
      .bob { animation: person 2s ease-in-out infinite; }
    </style>
  </defs>
  <rect width="500" height="350" fill="#E3F2FD"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#0D47A1">Имя существительное</text>
  <!-- Person icon -->
  <g class="bob" transform="translate(60,55)">
    <circle cx="50" cy="25" r="22" fill="#1565C0"/>
    <circle cx="50" cy="25" r="18" fill="#BBDEFB"/>
    <rect x="30" y="50" width="40" height="50" fill="#1565C0" rx="5"/>
    <rect x="20" y="55" width="15" height="40" fill="#1565C0" rx="3"/>
    <rect x="65" y="55" width="15" height="40" fill="#1565C0" rx="3"/>
    <rect x="30" y="100" width="15" height="30" fill="#1565C0" rx="3"/>
    <rect x="55" y="100" width="15" height="30" fill="#1565C0" rx="3"/>
  </g>
  <!-- Definition -->
  <rect x="170" y="55" width="300" height="70" fill="white" rx="10" stroke="#90CAF9" stroke-width="2"/>
  <text x="320" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#0D47A1">Кто? Что?</text>
  <text x="320" y="98" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#333">Существительное — часть речи,</text>
  <text x="320" y="115" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#333">обозначает предмет</text>
  <!-- Examples -->
  <rect x="30" y="140" width="440" height="80" fill="#E3F2FD" rx="10"/>
  <text x="250" y="162" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0D47A1">Примеры</text>
  <g transform="translate(50,175)" font-family="Arial,sans-serif" font-size="13">
    <rect x="0" y="0" width="100" height="25" fill="#BBDEFB" rx="5"/>
    <text x="50" y="18" text-anchor="middle" fill="#0D47A1">мальчик</text>
    <rect x="110" y="0" width="90" height="25" fill="#BBDEFB" rx="5"/>
    <text x="155" y="18" text-anchor="middle" fill="#0D47A1">кошка</text>
    <rect x="210" y="0" width="90" height="25" fill="#BBDEFB" rx="5"/>
    <text x="255" y="18" text-anchor="middle" fill="#0D47A1">стол</text>
    <rect x="310" y="0" width="110" height="25" fill="#BBDEFB" rx="5"/>
    <text x="365" y="18" text-anchor="middle" fill="#0D47A1">радость</text>
  </g>
  <!-- Categories -->
  <rect x="30" y="235" width="210" height="100" fill="white" rx="10" stroke="#90CAF9" stroke-width="1"/>
  <text x="135" y="255" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#0D47A1">Одушевлённые</text>
  <text x="135" y="275" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#333">Кто?</text>
  <text x="135" y="295" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">мальчик, кошка, птица</text>
  <text x="135" y="315" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">учитель, медведь</text>
  <rect x="260" y="235" width="210" height="100" fill="white" rx="10" stroke="#90CAF9" stroke-width="1"/>
  <text x="365" y="255" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#0D47A1">Неодушевлённые</text>
  <text x="365" y="275" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#333">Что?</text>
  <text x="365" y="295" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">стол, книга, дерево</text>
  <text x="365" y="315" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">город, ветер</text>
</svg>''',

    2: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes colorChange{0%,100%{fill:#E1BEE7}50%{fill:#CE93D8}}.color{animation:colorChange 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#F3E5F5"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#6A1B9A">Имя прилагательное</text>
  <rect x="30" y="50" width="440" height="70" fill="white" rx="10" stroke="#CE93D8" stroke-width="2"/>
  <text x="250" y="75" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#6A1B9A">Какой? Какая? Какое? Какие?</text>
  <text x="250" y="100" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#333">Прилагательное — часть речи, обозначает признак предмета</text>
  <!-- Word pairs -->
  <g transform="translate(30,135)" font-family="Arial,sans-serif" font-size="14">
    <rect x="0" y="0" width="130" height="30" fill="#E1BEE7" rx="5"/><text x="65" y="22" text-anchor="middle" fill="#6A1B9A">красивый</text>
    <text x="140" y="22" fill="#6A1B9A">+</text>
    <rect x="155" y="0" width="80" height="30" fill="#BBDEFB" rx="5"/><text x="195" y="22" text-anchor="middle" fill="#0D47A1">дом</text>
    <text x="245" y="22" fill="#6A1B9A">=</text>
    <rect x="260" y="0" width="190" height="30" class="color" rx="5"/><text x="355" y="22" text-anchor="middle" fill="#6A1B9A">красивый дом</text>
  </g>
  <g transform="translate(30,175)" font-family="Arial,sans-serif" font-size="14">
    <rect x="0" y="0" width="130" height="30" fill="#C8E6C9" rx="5"/><text x="65" y="22" text-anchor="middle" fill="#2E7D32">весёлый</text>
    <text x="140" y="22" fill="#6A1B9A">+</text>
    <rect x="155" y="0" width="100" height="30" fill="#FFECB3" rx="5"/><text x="205" y="22" text-anchor="middle" fill="#E65100">щенок</text>
    <text x="265" y="22" fill="#6A1B9A">=</text>
    <rect x="280" y="0" width="190" height="30" fill="#E8F5E9" rx="5"/><text x="375" y="22" text-anchor="middle" fill="#2E7D32">весёлый щенок</text>
  </g>
  <!-- Gender -->
  <rect x="30" y="220" width="440" height="120" fill="white" rx="10" stroke="#CE93D8" stroke-width="2"/>
  <text x="250" y="243" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#6A1B9A">Род прилагательных</text>
  <g font-family="Arial,sans-serif" font-size="12">
    <rect x="50" y="255" width="120" height="25" fill="#FFCDD2" rx="5"/><text x="110" y="273" text-anchor="middle" fill="#C62828">М.р. -ый -ий</text>
    <rect x="190" y="255" width="120" height="25" fill="#F8BBD0" rx="5"/><text x="250" y="273" text-anchor="middle" fill="#AD1457">Ж.р. -ая -яя</text>
    <rect x="330" y="255" width="120" height="25" fill="#E1BEE7" rx="5"/><text x="390" y="273" text-anchor="middle" fill="#6A1B9A">Ср.р. -ое -ее</text>
  </g>
  <g font-family="Arial,sans-serif" font-size="11" fill="#555">
    <text x="110" y="300">красивый, синий</text>
    <text x="250" y="300">красивая, синяя</text>
    <text x="390" y="300">красивое, синее</text>
  </g>
  <text x="250" y="330" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#6A1B9A">Прилагательное согласуется с существительным в роде</text>
</svg>''',

    3: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes run{0%{transform:translateX(0)}100%{transform:translateX(5px)}50%{transform:translateX(0)}}.action{animation:run 1.5s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF3E0"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#BF360C">Глагол</text>
  <rect x="30" y="50" width="440" height="60" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <text x="250" y="75" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#BF360C">Что делать? Что сделать? Что делает?</text>
  <text x="250" y="98" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#333">Глагол — часть речи, обозначает действие предмета</text>
  <!-- Action examples -->
  <g class="action" transform="translate(30,125)" font-family="Arial,sans-serif" font-size="13">
    <rect x="0" y="0" width="90" height="28" fill="#FFCCBC" rx="5"/><text x="45" y="20" text-anchor="middle" fill="#BF360C">бежать</text>
    <rect x="100" y="0" width="90" height="28" fill="#FFE0B2" rx="5"/><text x="145" y="20" text-anchor="middle" fill="#E65100">прыгать</text>
    <rect x="200" y="0" width="90" height="28" fill="#FFF9C4" rx="5"/><text x="245" y="20" text-anchor="middle" fill="#F57F17">читать</text>
    <rect x="300" y="0" width="90" height="28" fill="#C8E6C9" rx="5"/><text x="345" y="20" text-anchor="middle" fill="#2E7D32">рисовать</text>
  </g>
  <!-- Tenses -->
  <rect x="30" y="170" width="440" height="165" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <text x="250" y="195" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#BF360C">Времена глагола</text>
  <g font-family="Arial,sans-serif" font-size="12">
    <rect x="50" y="210" width="120" height="35" fill="#BBDEFB" rx="5"/>
    <text x="110" y="228" text-anchor="middle" fill="#0D47A1" font-weight="bold">Прошедшее</text>
    <text x="110" y="242" text-anchor="middle" fill="#1565C0" font-size="10">что делал? -л</text>
    <rect x="190" y="210" width="120" height="35" fill="#C8E6C9" rx="5"/>
    <text x="250" y="228" text-anchor="middle" fill="#2E7D32" font-weight="bold">Настоящее</text>
    <text x="250" y="242" text-anchor="middle" fill="#388E3C" font-size="10">что делает?</text>
    <rect x="330" y="210" width="120" height="35" fill="#FFCDD2" rx="5"/>
    <text x="390" y="228" text-anchor="middle" fill="#C62828" font-weight="bold">Будущее</text>
    <text x="390" y="242" text-anchor="middle" fill="#D32F2F" font-size="10">что будет делать?</text>
  </g>
  <g font-family="Arial,sans-serif" font-size="12" fill="#555" text-anchor="middle">
    <text x="110" y="270">читал</text>
    <text x="250" y="270">читает</text>
    <text x="390" y="270">будет читать</text>
  </g>
  <text x="250" y="310" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#BF360C">Глагол изменяется по временам, числам и лицам</text>
</svg>''',

    4: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes link{0%,100%{stroke-width:3}50%{stroke-width:5}}.chain{animation:link 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E8F5E9"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#1B5E20">Связь слов в предложении</text>
  <!-- Sentence diagram -->
  <rect x="30" y="50" width="440" height="60" fill="white" rx="10" stroke="#A5D6A7" stroke-width="2"/>
  <text x="250" y="75" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" fill="#1B5E20">Маленькая девочка читает интересную книгу.</text>
  <text x="250" y="100" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Слова связаны по смыслу и грамматически</text>
  <!-- Word connections -->
  <g transform="translate(30,125)">
    <rect x="0" y="0" width="440" height="100" fill="#E8F5E9" rx="10"/>
    <text x="80" y="25" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" fill="#1B5E20">девочка</text>
    <line x1="80" y1="30" x2="80" y2="55" class="chain" stroke="#4CAF50"/>
    <text x="80" y="70" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#2E7D32">читает</text>
    <line x1="110" y1="25" x2="240" y2="25" stroke="#4CAF50" stroke-width="2" stroke-dasharray="5,3"/>
    <text x="270" y="25" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" fill="#1B5E20">книгу</text>
    <line x1="270" y1="30" x2="270" y2="55" stroke="#4CAF50" stroke-width="2" stroke-dasharray="5,3"/>
    <text x="270" y="70" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#2E7D32">интересную</text>
    <line x1="50" y1="25" x2="20" y2="25" stroke="#4CAF50" stroke-width="2" stroke-dasharray="5,3"/>
    <text x="20" y="50" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#2E7D32">маленькая</text>
  </g>
  <!-- Types -->
  <rect x="30" y="240" width="210" height="95" fill="white" rx="10" stroke="#A5D6A7" stroke-width="1"/>
  <text x="135" y="262" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#1B5E20">Согласование</text>
  <text x="135" y="282" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">маленькая девочка</text>
  <text x="135" y="300" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">род, число, падеж</text>
  <text x="135" y="318" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">совпадают</text>
  <rect x="260" y="240" width="210" height="95" fill="white" rx="10" stroke="#A5D6A7" stroke-width="1"/>
  <text x="365" y="262" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#1B5E20">Управление</text>
  <text x="365" y="282" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">читает книгу</text>
  <text x="365" y="300" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">глагол требует</text>
  <text x="365" y="318" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">определённый падеж</text>
</svg>''',

    5: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes stress{0%,100%{fill:#F44336}50%{fill:#E57373}}.stress{animation:stress 1.5s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFEBEE"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#B71C1C">Безударные гласные в корне</text>
  <rect x="30" y="50" width="440" height="60" fill="white" rx="10" stroke="#EF9A9A" stroke-width="2"/>
  <text x="250" y="75" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" fill="#B71C1C">Чтобы написать правильно — подбирай проверочное слово!</text>
  <text x="250" y="98" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#333">Проверочное слово — где гласная под ударением</text>
  <!-- Examples -->
  <g transform="translate(30,125)" font-family="Arial,sans-serif">
    <rect x="0" y="0" width="200" height="55" fill="#FFCDD2" rx="8" stroke="#EF5350" stroke-width="1"/>
    <text x="100" y="20" text-anchor="middle" font-size="14">тр<span class="stress">а</span>ва</text>
    <text x="100" y="42" text-anchor="middle" font-size="12" fill="#B71C1C">проверка: тр<span fill="#F44336" font-weight="bold">а</span>вы</text>
    <rect x="220" y="0" width="220" height="55" fill="#FFCDD2" rx="8" stroke="#EF5350" stroke-width="1"/>
    <text x="330" y="20" text-anchor="middle" font-size="14">д<span class="stress">о</span>ма</text>
    <text x="330" y="42" text-anchor="middle" font-size="12" fill="#B71C1C">проверка: д<span fill="#F44336" font-weight="bold">о</span>м</text>
  </g>
  <g transform="translate(30,190)" font-family="Arial,sans-serif">
    <rect x="0" y="0" width="200" height="55" fill="#FFCDD2" rx="8" stroke="#EF5350" stroke-width="1"/>
    <text x="100" y="20" text-anchor="middle" font-size="14">л<span class="stress">и</span>са</text>
    <text x="100" y="42" text-anchor="middle" font-size="12" fill="#B71C1C">проверка: л<span fill="#F44336" font-weight="bold">и</span>сы</text>
    <rect x="220" y="0" width="220" height="55" fill="#FFCDD2" rx="8" stroke="#EF5350" stroke-width="1"/>
    <text x="330" y="20" text-anchor="middle" font-size="14">зв<span class="stress">е</span>ри</text>
    <text x="330" y="42" text-anchor="middle" font-size="12" fill="#B71C1C">проверка: зв<span fill="#F44336" font-weight="bold">е</span>рь</text>
  </g>
  <!-- Algorithm -->
  <rect x="30" y="260" width="440" height="75" fill="#FFEBEE" rx="10"/>
  <text x="250" y="282" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#B71C1C">Алгоритм проверки</text>
  <text x="250" y="302" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">1. Прочитай слово 2. Найди безударную гласную</text>
  <text x="250" y="320" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">3. Подбери проверочное слово 4. Напиши правильно</text>
</svg>''',

    6: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes ring{0%,100%{stroke-width:2}50%{stroke-width:4}}.pair{animation:ring 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#F1F8E9"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#1B5E20">Парные согласные в корне</text>
  <!-- Pairs -->
  <rect x="30" y="50" width="440" height="100" fill="white" rx="10" stroke="#A5D6A7" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1B5E20">Парные согласные звуки</text>
  <g font-family="Arial,sans-serif" font-size="18" font-weight="bold" text-anchor="middle">
    <rect x="55" y="82" width="50" height="30" fill="#C8E6C9" rx="5"/><text x="80" y="104" fill="#2E7D32">Б</text>
    <text x="118" y="104" fill="#1B5E20">-</text>
    <rect x="130" y="82" width="50" height="30" fill="#FFCDD2" rx="5"/><text x="155" y="104" fill="#C62828">П</text>
    <rect x="210" y="82" width="50" height="30" fill="#C8E6C9" rx="5"/><text x="235" y="104" fill="#2E7D32">В</text>
    <text x="273" y="104" fill="#1B5E20">-</text>
    <rect x="285" y="82" width="50" height="30" fill="#FFCDD2" rx="5"/><text x="310" y="104" fill="#C62828">Ф</text>
    <rect x="365" y="82" width="50" height="30" fill="#C8E6C9" rx="5"/><text x="390" y="104" fill="#2E7D32">Г</text>
    <text x="428" y="104" fill="#1B5E20">-</text>
    <rect x="440" y="82" width="50" height="30" fill="#FFCDD2" rx="5"/><text x="465" y="104" fill="#C62828">К</text>
  </g>
  <!-- Check examples -->
  <g transform="translate(30,165)" font-family="Arial,sans-serif">
    <rect x="0" y="0" width="210" height="55" fill="#E8F5E9" rx="8" stroke="#A5D6A7"/>
    <text x="105" y="22" text-anchor="middle" font-size="14">ду<span class="pair" stroke="#2E7D32">б</span></text>
    <text x="105" y="45" text-anchor="middle" font-size="12" fill="#1B5E20">проверка: ду<span fill="#2E7D32" font-weight="bold">б</span>ы</text>
    <rect x="230" y="0" width="210" height="55" fill="#E8F5E9" rx="8" stroke="#A5D6A7"/>
    <text x="335" y="22" text-anchor="middle" font-size="14">ша<span class="pair" stroke="#2E7D32">б</span></text>
    <text x="335" y="45" text-anchor="middle" font-size="12" fill="#1B5E20">проверка: ша<span fill="#2E7D32" font-weight="bold">б</span>ка (нет)</text>
  </g>
  <!-- Rule -->
  <rect x="30" y="235" width="440" height="100" fill="white" rx="10" stroke="#A5D6A7" stroke-width="2"/>
  <text x="250" y="258" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1B5E20">Как проверить парную согласную?</text>
  <text x="250" y="280" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">Измени слово так, чтобы после согласной стояла гласная</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#1B5E20" text-anchor="middle">
    <text x="130" y="305">ду<b>б</b> - ду<b>б</b>ы</text>
    <text x="370" y="305">сне<b>г</b> - сне<b>г</b>а</text>
  </g>
  <text x="250" y="328" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">лодка - лодочки, медведь - медведи</text>
</svg>''',

    7: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes soft{0%,100%{opacity:1}50%{opacity:0.6}}.sign{animation:soft 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E8EAF6"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#283593">Разделительный мягкий знак</text>
  <rect x="30" y="50" width="440" height="60" fill="white" rx="10" stroke="#9FA8DA" stroke-width="2"/>
  <text x="250" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" fill="#283593">Мягкий знак (Ь) разделяет согласную и гласную</text>
  <text x="250" y="100" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">Пишется перед Е, Ё, Ю, Я, И</text>
  <!-- Examples -->
  <g transform="translate(30,125)" font-family="Arial,sans-serif">
    <rect x="0" y="0" width="130" height="65" fill="#C5CAE9" rx="8" stroke="#283593" stroke-width="1"/>
    <text x="65" y="25" text-anchor="middle" font-size="20" font-weight="bold" fill="#283593">дерев<span class="sign" fill="#3F51B5">ь</span>я</text>
    <text x="65" y="48" text-anchor="middle" font-size="10" fill="#555">без Ь: дерева</text>
    <text x="65" y="60" text-anchor="middle" font-size="10" fill="#283593">с Ь: деревья</text>
    <rect x="145" y="0" width="130" height="65" fill="#C5CAE9" rx="8" stroke="#283593" stroke-width="1"/>
    <text x="210" y="25" text-anchor="middle" font-size="20" font-weight="bold" fill="#283593">в<span class="sign" fill="#3F51B5">ь</span>юга</text>
    <text x="210" y="48" text-anchor="middle" font-size="10" fill="#555">без Ь: вюга (нет)</text>
    <text x="210" y="60" text-anchor="middle" font-size="10" fill="#283593">с Ь: вьюга</text>
    <rect x="290" y="0" width="130" height="65" fill="#C5CAE9" rx="8" stroke="#283593" stroke-width="1"/>
    <text x="355" y="25" text-anchor="middle" font-size="20" font-weight="bold" fill="#283593">п<span class="sign" fill="#3F51B5">ь</span>еса</text>
    <text x="355" y="48" text-anchor="middle" font-size="10" fill="#555">без Ь: песа (нет)</text>
    <text x="355" y="60" text-anchor="middle" font-size="10" fill="#283593">с Ь: пьеса</text>
  </g>
  <!-- More words -->
  <rect x="30" y="205" width="440" height="55" fill="#E8EAF6" rx="10"/>
  <text x="250" y="225" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#283593">листья, ручьи, семья, платье, крылья, соловьи</text>
  <text x="250" y="248" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Ь показывает, что согласный звук произносится мягко</text>
  <!-- Compare -->
  <rect x="30" y="270" width="210" height="65" fill="white" rx="8" stroke="#9FA8DA"/>
  <text x="135" y="292" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#C62828">полю</text>
  <text x="135" y="315" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Ь — показатель мягкости</text>
  <rect x="260" y="270" width="210" height="65" fill="white" rx="8" stroke="#9FA8DA"/>
  <text x="365" y="292" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#283593">полью</text>
  <text x="365" y="315" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Ь — разделительный</text>
</svg>''',

    8: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes prefix{0%{transform:translateX(-3px)}100%{transform:translateX(3px)}50%{transform:translateX(0)}}.pre{animation:prefix 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FBE9E7"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#BF360C">Правописание приставок</text>
  <rect x="30" y="50" width="440" height="50" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#BF360C">Приставка — часть слова, стоит перед корнем</text>
  <text x="250" y="90" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Приставки пишутся одинаково, независимо от произношения</text>
  <!-- Prefixes -->
  <g transform="translate(30,115)" font-family="Arial,sans-serif">
    <rect x="0" y="0" width="100" height="40" fill="#FFCCBC" rx="8" stroke="#BF360C" stroke-width="1"/>
    <text x="50" y="18" text-anchor="middle" font-size="16" font-weight="bold" fill="#BF360C">на-</text>
    <text x="50" y="33" text-anchor="middle" font-size="10" fill="#555">написал</text>
    <rect x="110" y="0" width="100" height="40" fill="#FFE0B2" rx="8" stroke="#E65100" stroke-width="1"/>
    <text x="160" y="18" text-anchor="middle" font-size="16" font-weight="bold" fill="#E65100">за-</text>
    <text x="160" y="33" text-anchor="middle" font-size="10" fill="#555">забежал</text>
    <rect x="220" y="0" width="100" height="40" fill="#FFF9C4" rx="8" stroke="#F57F17" stroke-width="1"/>
    <text x="270" y="18" text-anchor="middle" font-size="16" font-weight="bold" fill="#F57F17">по-</text>
    <text x="270" y="33" text-anchor="middle" font-size="10" fill="#555">побежал</text>
    <rect x="330" y="0" width="100" height="40" fill="#C8E6C9" rx="8" stroke="#2E7D32" stroke-width="1"/>
    <text x="380" y="18" text-anchor="middle" font-size="16" font-weight="bold" fill="#2E7D32">про-</text>
    <text x="380" y="33" text-anchor="middle" font-size="10" fill="#555">прочитал</text>
  </g>
  <!-- Word structure -->
  <g class="pre" transform="translate(30,175)">
    <rect x="0" y="0" width="440" height="55" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
    <text x="20" y="25" font-family="Arial,sans-serif" font-size="13" fill="#BF360C">приставка</text>
    <rect x="15" y="30" width="60" height="20" fill="#FFCCBC" rx="3"/><text x="45" y="44" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#BF360C">за</text>
    <text x="85" y="44" font-family="Arial,sans-serif" font-size="13" fill="#555">|</text>
    <text x="120" y="25" font-family="Arial,sans-serif" font-size="13" fill="#2E7D32">корень</text>
    <rect x="100" y="30" width="90" height="20" fill="#C8E6C9" rx="3"/><text x="145" y="44" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#2E7D32">беж</text>
    <text x="200" y="44" font-family="Arial,sans-serif" font-size="13" fill="#555">|</text>
    <text x="250" y="25" font-family="Arial,sans-serif" font-size="13" fill="#1565C0">суффикс</text>
    <rect x="220" y="30" width="80" height="20" fill="#BBDEFB" rx="3"/><text x="260" y="44" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#1565C0">ал</text>
    <text x="310" y="44" font-family="Arial,sans-serif" font-size="13" fill="#555">|</text>
    <text x="370" y="25" font-family="Arial,sans-serif" font-size="13" fill="#6A1B9A">окончание</text>
    <rect x="330" y="30" width="80" height="20" fill="#E1BEE7" rx="3"/><text x="370" y="44" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#6A1B9A">нул.</text>
  </g>
  <!-- Rule -->
  <rect x="30" y="245" width="440" height="90" fill="#FBE9E7" rx="10"/>
  <text x="250" y="268" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#BF360C">Правило</text>
  <text x="250" y="290" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">Приставки на-, за-, по-, про-, об-, от-, над-, под-</text>
  <text x="250" y="310" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">пишутся всегда одинаково, независимо от произношения</text>
  <text x="250" y="330" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#BF360C">записать, подписать, отписать — приставка сохраняется</text>
</svg>''',

    9: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes build{0%,100%{transform:scaleY(1)}50%{transform:scaleY(1.03)}}.block{animation:build 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E3F2FD"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#0D47A1">Текст и его структура</text>
  <!-- Text structure diagram -->
  <rect x="30" y="50" width="440" height="280" fill="white" rx="10" stroke="#90CAF9" stroke-width="2"/>
  <text x="250" y="75" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#0D47A1">Структура текста</text>
  <!-- Beginning -->
  <g class="block" transform="translate(60,90)">
    <rect x="0" y="0" width="380" height="50" fill="#BBDEFB" rx="8" stroke="#1565C0" stroke-width="2"/>
    <text x="190" y="20" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#0D47A1">Вступление (зачин)</text>
    <text x="190" y="40" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#1565C0">О чём будет текст? Введение в тему</text>
  </g>
  <!-- Middle -->
  <g class="block" transform="translate(60,155)">
    <rect x="0" y="0" width="380" height="65" fill="#90CAF9" rx="8" stroke="#1565C0" stroke-width="2"/>
    <text x="190" y="20" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#0D47A1">Основная часть</text>
    <text x="190" y="40" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1">Развитие событий, описание,</text>
    <text x="190" y="55" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1">рассуждение</text>
  </g>
  <!-- End -->
  <g class="block" transform="translate(60,235)">
    <rect x="0" y="0" width="380" height="50" fill="#64B5F6" rx="8" stroke="#1565C0" stroke-width="2"/>
    <text x="190" y="20" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="white">Заключение (концовка)</text>
    <text x="190" y="40" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="white">Вывод, итог, завершение мысли</text>
  </g>
  <!-- Arrows -->
  <text x="250" y="148" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" fill="#1565C0">|</text>
  <text x="250" y="230" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" fill="#1565C0">|</text>
  <text x="250" y="305" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1">Текст — связанные предложения на одну тему</text>
</svg>''',

    10: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes step{0%,100%{opacity:1}50%{opacity:0.7}}.highlight{animation:step 1.5s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF8E1"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#E65100">План текста</text>
  <!-- Steps -->
  <rect x="30" y="50" width="440" height="60" fill="white" rx="10" stroke="#FFE082" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#E65100">План — это краткая запись содержания текста</text>
  <text x="250" y="92" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Помогает понять и пересказать текст</text>
  <!-- Plan example -->
  <g transform="translate(30,125)">
    <rect x="0" y="0" width="440" height="130" fill="#FFF8E1" rx="10" stroke="#FFE082" stroke-width="2"/>
    <text x="220" y="22" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#E65100">План рассказа «Весна пришла»</text>
    <g class="highlight" font-family="Arial,sans-serif" font-size="12">
      <rect x="20" y="35" width="400" height="22" fill="#FFECB3" rx="3"/>
      <text x="30" y="51" fill="#E65100">1. Последние дни зимы.</text>
      <rect x="20" y="62" width="400" height="22" fill="#FFF9C4" rx="3"/>
      <text x="30" y="78" fill="#E65100">2. Первые признаки весны.</text>
      <rect x="20" y="89" width="400" height="22" fill="#FFECB3" rx="3"/>
      <text x="30" y="105" fill="#E65100">3. Весёлые ручьи и птицы.</text>
    </g>
  </g>
  <!-- How to make a plan -->
  <rect x="30" y="270" width="440" height="65" fill="white" rx="10" stroke="#FFE082" stroke-width="2"/>
  <text x="250" y="290" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#E65100">Как составить план</text>
  <text x="250" y="310" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">1. Прочитай текст 2. Раздели на части 3. Озаглавь каждую часть</text>
  <text x="250" y="325" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">4. Запиши пункты плана по порядку</text>
</svg>'''
}

# Continue with other subjects...
print("Math and Russian SVGs defined. Continuing with other subjects...")

# Save math SVGs
for i, svg in math_svgs.items():
    path = os.path.join(SVG_DIR, 'math', f'lesson{i}-unique.svg')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Saved: {path}")

# Save russian SVGs
for i, svg in russian_svgs.items():
    path = os.path.join(SVG_DIR, 'russian', f'lesson{i}-unique.svg')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Saved: {path}")

print("Math (12) + Russian (10) = 22 SVGs saved")
