#!/usr/bin/env python3
import os

SVG_DIR = 'public/images/lessons/grade2'

# ============================================================
# ART SVGs (8 lessons)
# ============================================================
art_svgs = {
    1: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes paint{0%,100%{transform:rotate(-3deg)}50%{transform:rotate(3deg)}}.brush{animation:paint 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF3E0"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#BF360C">Что такое живопись?</text>
  <!-- Palette -->
  <g class="brush" transform="translate(30,50)">
    <ellipse cx="80" cy="80" rx="70" ry="50" fill="#795548"/>
    <circle cx="50" cy="65" r="10" fill="#F44336"/><circle cx="75" cy="55" r="10" fill="#FF9800"/>
    <circle cx="105" cy="55" r="10" fill="#FFC107"/><circle cx="125" cy="70" r="10" fill="#4CAF50"/>
    <circle cx="50" cy="90" r="10" fill="#2196F3"/><circle cx="80" cy="95" r="10" fill="#9C27B0"/>
    <ellipse cx="100" cy="90" rx="12" ry="10" fill="#795548"/>
  </g>
  <!-- Definition -->
  <rect x="200" y="55" width="270" height="120" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <text x="335" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#BF360C">Живопись</text>
  <text x="335" y="98" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#333">— вид изобразительного искусства</text>
  <text x="335" y="118" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#333">произведения создаются красками</text>
  <text x="335" y="138" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#333">на холсте, бумаге, дереве</text>
  <text x="335" y="162" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#BF360C">Живопись = «живо писать» (изображать)</text>
  <!-- Materials -->
  <rect x="30" y="195" width="440" height="65" fill="#FFF3E0" rx="10"/>
  <text x="250" y="218" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#BF360C">Материалы художника</text>
  <g font-family="Arial,sans-serif" font-size="11" fill="#333">
    <rect x="50" y="228" width="70" height="22" fill="#FFCCBC" rx="3"/><text x="85" y="244" text-anchor="middle">Краски</text>
    <rect x="130" y="228" width="70" height="22" fill="#FFE0B2" rx="3"/><text x="165" y="244" text-anchor="middle">Кисти</text>
    <rect x="210" y="228" width="70" height="22" fill="#FFF9C4" rx="3"/><text x="245" y="244" text-anchor="middle">Холст</text>
    <rect x="290" y="228" width="70" height="22" fill="#C8E6C9" rx="3"/><text x="325" y="244" text-anchor="middle">Палитра</text>
    <rect x="370" y="228" width="80" height="22" fill="#BBDEFB" rx="3"/><text x="410" y="244" text-anchor="middle">Карандаши</text>
  </g>
  <!-- Genres -->
  <rect x="30" y="270" width="440" height="65" fill="white" rx="10" stroke="#FFAB91" stroke-width="1"/>
  <text x="250" y="290" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#BF360C">Жанры живописи</text>
  <text x="250" y="310" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#333">Пейзаж, натюрморт, портрет, историческая картина</text>
  <text x="250" y="328" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Каждый жанр изображает свой мир</text>
</svg>''',

    2: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes cloud{0%,100%{transform:translateX(0)}50%{transform:translateX(5px)}}.sky{animation:cloud 3s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E3F2FD"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#0D47A1">Пейзаж</text>
  <!-- Landscape scene -->
  <rect x="30" y="50" width="440" height="160" fill="white" rx="10" stroke="#90CAF9" stroke-width="2"/>
  <!-- Sky -->
  <rect x="35" y="55" width="430" height="100" fill="#BBDEFB" rx="8"/>
  <!-- Sun -->
  <circle cx="400" cy="80" r="25" fill="#FFC107"/>
  <!-- Clouds -->
  <g class="sky">
    <ellipse cx="120" cy="75" rx="30" ry="15" fill="white"/>
    <ellipse cx="140" cy="70" rx="25" ry="15" fill="white"/>
    <ellipse cx="155" cy="78" rx="20" ry="12" fill="white"/>
  </g>
  <!-- Mountains -->
  <polygon points="35,155 130,80 225,155" fill="#81C784"/>
  <polygon points="150,155 260,70 370,155" fill="#66BB6A"/>
  <polygon points="280,155 380,90 465,155" fill="#4CAF50"/>
  <!-- Lake -->
  <ellipse cx="250" cy="170" rx="100" ry="15" fill="#64B5F6"/>
  <!-- Trees -->
  <rect x="70" y="135" width="5" height="20" fill="#5D4037"/>
  <circle cx="72" cy="128" r="12" fill="#388E3C"/>
  <rect x="420" y="130" width="5" height="25" fill="#5D4037"/>
  <circle cx="422" cy="123" r="14" fill="#2E7D32"/>
  <!-- Definition -->
  <rect x="30" y="225" width="440" height="110" fill="#E3F2FD" rx="10"/>
  <text x="250" y="248" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#0D47A1">Пейзаж — картина природы</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="272">Изображает: леса, горы, реки, поля</text>
    <text x="50" y="292">Передаёт настроение и красоту природы</text>
    <text x="50" y="312">Меняется по сезонам: зимний, весенний, летний, осенний</text>
    <text x="50" y="332" fill="#0D47A1">Известные художники-пейзажисты: Левитан, Шишкин, Саврасов</text>
  </g>
</svg>''',

    3: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes still{0%,100%{opacity:1}50%{opacity:0.8}}.fruit{animation:still 3s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF8E1"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#E65100">Натюрморт</text>
  <!-- Still life scene -->
  <rect x="30" y="50" width="440" height="160" fill="white" rx="10" stroke="#FFE082" stroke-width="2"/>
  <!-- Table -->
  <rect x="40" y="160" width="420" height="15" fill="#8D6E63" rx="2"/>
  <!-- Vase -->
  <path d="M200,160 Q190,130 195,110 Q200,90 220,85 Q240,90 245,110 Q250,130 240,160Z" fill="#1565C0" stroke="#0D47A1" stroke-width="1"/>
  <ellipse cx="220" cy="160" rx="20" ry="5" fill="#0D47A1"/>
  <!-- Flowers in vase -->
  <line x1="210" y1="85" x2="200" y2="55" stroke="#4CAF50" stroke-width="2"/>
  <circle cx="200" cy="50" r="8" fill="#F44336"/>
  <line x1="220" y1="85" x2="220" y2="50" stroke="#4CAF50" stroke-width="2"/>
  <circle cx="220" cy="45" r="8" fill="#FFC107"/>
  <line x1="230" y1="85" x2="240" y2="55" stroke="#4CAF50" stroke-width="2"/>
  <circle cx="240" cy="50" r="8" fill="#E91E63"/>
  <!-- Fruits -->
  <g class="fruit">
    <circle cx="130" cy="148" r="15" fill="#F44336"/>
    <circle cx="155" cy="152" r="12" fill="#FF9800"/>
    <circle cx="170" cy="145" r="13" fill="#FFC107"/>
  </g>
  <!-- Pitcher -->
  <path d="M320,160 Q310,140 315,120 Q320,100 340,95 Q355,95 360,110 L360,160Z" fill="#FFECB3" stroke="#E65100" stroke-width="1"/>
  <ellipse cx="340" cy="95" rx="22" ry="5" fill="#FFE082" stroke="#E65100" stroke-width="1"/>
  <!-- Info -->
  <rect x="30" y="225" width="440" height="110" fill="#FFF8E1" rx="10"/>
  <text x="250" y="248" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#E65100">Натюрморт — изображение неживых предметов</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="272">Фрукты, цветы, посуда, книги</text>
    <text x="50" y="292">Предметы располагают на столе</text>
    <text x="50" y="312">Важно передать форму, цвет, свет и тень</text>
    <text x="50" y="332" fill="#E65100">Натюрморт в переводе с французского — «мёртвая природа»</text>
  </g>
</svg>''',

    4: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes face{0%,100%{transform:scale(1)}50%{transform:scale(1.02)}}.portrait{animation:face 3s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#F3E5F5"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#6A1B9A">Портрет</text>
  <!-- Portrait frame -->
  <g class="portrait" transform="translate(30,50)">
    <rect x="0" y="0" width="160" height="180" fill="#5D4037" rx="5"/>
    <rect x="8" y="8" width="144" height="164" fill="#FFF8E1" rx="3"/>
    <!-- Stylized face -->
    <ellipse cx="80" cy="75" rx="40" ry="50" fill="#FFCC80"/>
    <circle cx="65" cy="65" r="5" fill="#333"/>
    <circle cx="95" cy="65" r="5" fill="#333"/>
    <path d="M65 90 Q80 100 95 90" fill="none" stroke="#5D4037" stroke-width="2"/>
    <path d="M55 50 Q65 35 80 40" fill="#4E342E" stroke="none"/>
    <path d="M80 40 Q95 35 105 50" fill="#4E342E" stroke="none"/>
    <rect x="45" y="120" width="70" height="40" fill="#1565C0" rx="3"/>
  </g>
  <!-- Definition -->
  <rect x="210" y="55" width="260" height="120" fill="white" rx="10" stroke="#CE93D8" stroke-width="2"/>
  <text x="340" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#6A1B9A">Портрет — изображение человека</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="225" y="100">Передаёт внешность и характер</text>
    <text x="225" y="118">Лицо — самое важное</text>
    <text x="225" y="136">Глаза, губы, причёска</text>
    <text x="225" y="154">Отражает настроение человека</text>
  </g>
  <!-- Types -->
  <rect x="30" y="245" width="440" height="90" fill="#F3E5F5" rx="10"/>
  <text x="250" y="268" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#6A1B9A">Виды портретов</text>
  <g font-family="Arial,sans-serif" font-size="11">
    <rect x="50" y="280" width="100" height="22" fill="#E1BEE7" rx="3"/><text x="100" y="296" text-anchor="middle" fill="#6A1B9A">Парадный</text>
    <rect x="165" y="280" width="100" height="22" fill="#F3E5F5" rx="3"/><text x="215" y="296" text-anchor="middle" fill="#6A1B9A">Камерный</text>
    <rect x="280" y="280" width="80" height="22" fill="#E1BEE7" rx="3"/><text x="320" y="296" text-anchor="middle" fill="#6A1B9A">Автопортрет</text>
    <rect x="375" y="280" width="80" height="22" fill="#F3E5F5" rx="3"/><text x="415" y="296" text-anchor="middle" fill="#6A1B9A">Миниатюра</text>
  </g>
  <text x="250" y="322" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#6A1B9A">Известные портретисты: Репин, Серов, Левитан</text>
</svg>''',

    5: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes spin{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}.toy{animation:spin 8s linear infinite;transform-origin:80px 130px}</style></defs>
  <rect width="500" height="350" fill="#FFF3E0"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#BF360C">Дымковская игрушка</text>
  <!-- Dymkovo toy -->
  <g class="toy" transform="translate(30,55)">
    <ellipse cx="80" cy="160" rx="40" ry="15" fill="#FFC107"/>
    <rect x="65" y="90" width="30" height="70" fill="white" stroke="#E65100" stroke-width="2" rx="5"/>
    <circle cx="80" cy="70" r="30" fill="white" stroke="#E65100" stroke-width="2"/>
    <circle cx="72" cy="65" r="4" fill="#F44336"/><circle cx="88" cy="65" r="4" fill="#F44336"/>
    <circle cx="80" cy="75" r="3" fill="#2196F3"/>
    <!-- Decorative circles -->
    <circle cx="70" cy="100" r="5" fill="#F44336"/><circle cx="90" cy="100" r="5" fill="#4CAF50"/>
    <circle cx="70" cy="120" r="5" fill="#2196F3"/><circle cx="90" cy="120" r="5" fill="#FFC107"/>
    <circle cx="80" cy="140" r="5" fill="#E91E63"/>
  </g>
  <!-- Info -->
  <rect x="170" y="55" width="300" height="155" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <text x="320" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#BF360C">Дымковская игрушка</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="185" y="100">Родина: слобода Дымково, г. Вятка</text>
    <text x="185" y="118">Материал: глина</text>
    <text x="185" y="136">Раскраска: яркая, узорная</text>
    <text x="185" y="154">Узоры: круги, ромбы, точки</text>
    <text x="185" y="172">Цвета: красный, жёлтый, синий,</text>
    <text x="185" y="190">зелёный, белый фон</text>
  </g>
  <!-- Features -->
  <rect x="30" y="225" width="440" height="110" fill="#FFF3E0" rx="10"/>
  <text x="250" y="248" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#BF360C">Особенности промысла</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="270">Лепят из глины вручную</text>
    <text x="50" y="290">Обжигают в печи</text>
    <text x="50" y="310">Белят мелом и расписывают</text>
    <text x="50" y="330" fill="#BF360C">Барышни, кони, птицы, олени</text>
  </g>
</svg>''',

    6: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes golden{0%,100%{opacity:1}50%{opacity:0.8}}.khohloma{animation:golden 3s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF8E1"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#E65100">Хохломская роспись</text>
  <!-- Khokhloma bowl -->
  <g class="golden" transform="translate(30,55)">
    <ellipse cx="100" cy="80" rx="80" ry="30" fill="#FFD54F"/>
    <path d="M20,80 Q20,130 40,150 Q60,170 100,170 Q140,170 160,150 Q180,130 180,80" fill="#C62828" stroke="#FFD54F" stroke-width="2"/>
    <!-- Pattern -->
    <path d="M50,100 Q70,85 90,100 Q110,115 130,100 Q150,85 170,100" fill="none" stroke="#FFD54F" stroke-width="3"/>
    <circle cx="70" cy="120" r="5" fill="#4CAF50"/><circle cx="100" cy="130" r="6" fill="#FFD54F"/>
    <circle cx="130" cy="120" r="5" fill="#4CAF50"/>
    <!-- Berry -->
    <circle cx="90" cy="110" r="4" fill="#C62828"/><circle cx="110" cy="110" r="4" fill="#C62828"/>
  </g>
  <!-- Info -->
  <rect x="230" y="55" width="240" height="155" fill="white" rx="10" stroke="#FFB74D" stroke-width="2"/>
  <text x="350" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#E65100">Хохломская роспись</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="245" y="100">Родина: Нижегородская область</text>
    <text x="245" y="118">Фон: чёрный, красный, золотой</text>
    <text x="245" y="136">Узоры: травка, ягодка, листочек</text>
    <text x="245" y="154">Предметы: посуда, ложки,</text>
    <text x="245" y="172">стаканы, шкатулки</text>
  </g>
  <!-- Colors and technique -->
  <rect x="30" y="225" width="440" height="110" fill="#FFF8E1" rx="10"/>
  <text x="250" y="248" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#E65100">Секрет «золотой» Хохломы</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="270">1. Деревянную посуду грунтуют</text>
    <text x="50" y="290">2. Покрывают оловянным порошком</text>
    <text x="50" y="310">3. Расписывают красками</text>
    <text x="50" y="330" fill="#E65100">4. Лакируют и запекают — появляется золотой блеск!</text>
  </g>
</svg>''',

    7: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes blue{0%,100%{opacity:1}50%{opacity:0.85}}.gzhel{animation:blue 3s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E3F2FD"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#0D47A1">Гжельская керамика</text>
  <!-- Gzhel vase -->
  <g class="gzhel" transform="translate(30,55)">
    <path d="M80,30 Q60,60 55,100 Q50,140 60,170 Q70,190 100,190 Q130,190 140,170 Q150,140 145,100 Q140,60 120,30Z" fill="white" stroke="#1565C0" stroke-width="2"/>
    <ellipse cx="100" cy="30" rx="22" ry="6" fill="white" stroke="#1565C0" stroke-width="2"/>
    <!-- Blue pattern -->
    <path d="M70,70 Q85,55 100,70 Q115,85 130,70" fill="none" stroke="#1565C0" stroke-width="2"/>
    <path d="M70,100 Q85,85 100,100 Q115,115 130,100" fill="none" stroke="#0D47A1" stroke-width="2"/>
    <circle cx="80" cy="140" r="6" fill="#1565C0"/><circle cx="100" cy="145" r="4" fill="#42A5F5"/>
    <circle cx="120" cy="140" r="6" fill="#1565C0"/>
    <path d="M70,160 Q85,150 100,160 Q115,170 130,160" fill="none" stroke="#1565C0" stroke-width="1.5"/>
  </g>
  <!-- Info -->
  <rect x="200" y="55" width="270" height="155" fill="white" rx="10" stroke="#90CAF9" stroke-width="2"/>
  <text x="335" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#0D47A1">Гжельская керамика</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="215" y="100">Родина: посёлок Гжель, Подмосковье</text>
    <text x="215" y="118">Цвета: белый + синий</text>
    <text x="215" y="136">Узоры: розы, птицы, сказочные</text>
    <text x="215" y="154">сюжеты в сине-белых тонах</text>
    <text x="215" y="172">Предметы: посуда, фигурки,</text>
    <text x="215" y="190">кувшины, часы</text>
  </g>
  <!-- Technique -->
  <rect x="30" y="225" width="440" height="110" fill="#E3F2FD" rx="10"/>
  <text x="250" y="248" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0D47A1">Особенности гжельской росписи</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="270">Роспись делается от руки кистью</text>
    <text x="50" y="290">Один мазок — от тёмного к светлому</text>
    <text x="50" y="310">«Теневой мазок» — главная техника</text>
    <text x="50" y="330" fill="#0D47A1">Синий цвет на белом — символ Гжели</text>
  </g>
</svg>''',

    8: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes bloom{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}.flower{animation:bloom 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF3E0"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#BF360C">Городецкая роспись</text>
  <!-- Gorodets board -->
  <g transform="translate(30,55)">
    <rect x="0" y="0" width="200" height="155" fill="#FFECB3" rx="8" stroke="#E65100" stroke-width="2"/>
    <!-- Horse -->
    <ellipse cx="100" cy="80" rx="40" ry="25" fill="#C62828"/>
    <circle cx="70" cy="65" r="15" fill="#C62828"/>
    <rect x="60" y="55" width="8" height="20" fill="#C62828" rx="2"/>
    <rect x="76" y="55" width="8" height="20" fill="#C62828" rx="2"/>
    <rect x="130" y="65" width="25" height="4" fill="#C62828" rx="1"/>
    <!-- Decorative flower -->
    <g class="flower" transform="translate(140,30)">
      <circle cx="0" cy="0" r="12" fill="#FFC107"/>
      <circle cx="0" cy="-15" r="8" fill="#4CAF50"/>
      <circle cx="14" cy="-5" r="8" fill="#4CAF50"/>
      <circle cx="9" cy="12" r="8" fill="#4CAF50"/>
      <circle cx="-9" cy="12" r="8" fill="#4CAF50"/>
      <circle cx="-14" cy="-5" r="8" fill="#4CAF50"/>
    </g>
  </g>
  <!-- Info -->
  <rect x="250" y="55" width="220" height="155" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <text x="360" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#BF360C">Городецкая роспись</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="265" y="100">Родина: г. Городец</text>
    <text x="265" y="118">Цвета: красный, чёрный,</text>
    <text x="265" y="136">зелёный, жёлтый</text>
    <text x="265" y="154">Мотивы: кони, птицы,</text>
    <text x="265" y="172">цветы, всадники</text>
    <text x="265" y="190">Предметы: прялки, доски</text>
  </g>
  <!-- Technique -->
  <rect x="30" y="225" width="440" height="110" fill="#FFF3E0" rx="10"/>
  <text x="250" y="248" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#BF360C">Особенности городецкой росписи</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="270">Яркие, сочные цвета</text>
    <text x="50" y="290">Конь — символ благополучия</text>
    <text x="50" y="310">Птица — символ счастья</text>
    <text x="50" y="330" fill="#BF360C">Розан и купавка — главные цветы</text>
  </g>
</svg>'''
}

# ============================================================
# MUSIC SVGs (6 lessons)
# ============================================================
music_svgs = {
    1: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes note{0%,100%{transform:translateY(0)}50%{transform:translateY(-5px)}}.music{animation:note 1s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#EDE7F6"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#4527A0">Песня, танец, марш</text>
  <!-- Three genres -->
  <g class="music" transform="translate(30,50)">
    <rect x="0" y="0" width="130" height="140" fill="white" rx="10" stroke="#CE93D8" stroke-width="2"/>
    <text x="65" y="25" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#C2185B">Песня</text>
    <text x="65" y="50" text-anchor="middle" font-family="Arial,sans-serif" font-size="28" fill="#C2185B">&#9835;</text>
    <text x="65" y="80" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">Поём слова</text>
    <text x="65" y="95" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">Мелодия + текст</text>
    <text x="65" y="115" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">Колыбельная,</text>
    <text x="65" y="128" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">гимн, частушка</text>
  </g>
  <g transform="translate(180,50)">
    <rect x="0" y="0" width="130" height="140" fill="white" rx="10" stroke="#CE93D8" stroke-width="2"/>
    <text x="65" y="25" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#E65100">Танец</text>
    <text x="65" y="50" text-anchor="middle" font-family="Arial,sans-serif" font-size="28" fill="#E65100">&#9834;</text>
    <text x="65" y="80" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">Движение</text>
    <text x="65" y="95" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">Ритм + пластика</text>
    <text x="65" y="115" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">Вальс, полька,</text>
    <text x="65" y="128" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">хоровод</text>
  </g>
  <g transform="translate(330,50)">
    <rect x="0" y="0" width="130" height="140" fill="white" rx="10" stroke="#CE93D8" stroke-width="2"/>
    <text x="65" y="25" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#2E7D32">Марш</text>
    <text x="65" y="50" text-anchor="middle" font-family="Arial,sans-serif" font-size="28" fill="#2E7D32">&#9833;</text>
    <text x="65" y="80" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">Шагаем</text>
    <text x="65" y="95" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#333">Чёткий ритм</text>
    <text x="65" y="115" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">Военный марш,</text>
    <text x="65" y="128" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">спортивный марш</text>
  </g>
  <!-- Common features -->
  <rect x="30" y="210" width="440" height="125" fill="#EDE7F6" rx="10"/>
  <text x="250" y="233" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#4527A0">Что общего?</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="255">Все три жанра — основа музыки</text>
    <text x="50" y="275">Песня — мелодия и слова</text>
    <text x="50" y="295">Танец — музыка для движения</text>
    <text x="50" y="315">Марш — музыка для шага</text>
    <text x="50" y="335" fill="#4527A0">Многие произведения сочетают эти жанры</text>
  </g>
</svg>''',

    2: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes melody{0%,100%{transform:translateX(0)}50%{transform:translateX(3px)}}.wave{animation:melody 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#F3E5F5"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#6A1B9A">Мелодия и ритм</text>
  <!-- Melody wave -->
  <rect x="30" y="50" width="440" height="120" fill="white" rx="10" stroke="#CE93D8" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#6A1B9A">Мелодия — душа музыки</text>
  <g class="wave">
    <path d="M50,110 Q80,80 110,100 Q140,120 170,90 Q200,60 230,85 Q260,110 290,80 Q320,50 350,75 Q380,100 410,90 L440,95" fill="none" stroke="#9C27B0" stroke-width="3"/>
  </g>
  <text x="250" y="155" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Последовательность звуков разной высоты</text>
  <!-- Rhythm -->
  <rect x="30" y="185" width="440" height="80" fill="#F3E5F5" rx="10"/>
  <text x="250" y="208" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#6A1B9A">Ритм — пульс музыки</text>
  <g font-family="Arial,sans-serif" font-size="20" fill="#6A1B9A" text-anchor="middle">
    <text x="70" y="240">&#9833;</text><text x="110" y="240">&#9833;</text>
    <text x="150" y="240">&#9834;</text><text x="210" y="240">&#9833;</text>
    <text x="250" y="240">&#9833;</text><text x="290" y="240">&#9834;</text>
    <text x="350" y="240">&#9833;</text><text x="390" y="240">&#9834;</text>
    <text x="430" y="240">&#9834;</text>
  </g>
  <!-- Comparison -->
  <rect x="30" y="280" width="210" height="55" fill="white" rx="8" stroke="#CE93D8"/>
  <text x="135" y="300" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#6A1B9A">Мелодия</text>
  <text x="135" y="320" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Высота звуков, их порядок</text>
  <rect x="260" y="280" width="210" height="55" fill="white" rx="8" stroke="#CE93D8"/>
  <text x="365" y="300" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#6A1B9A">Ритм</text>
  <text x="365" y="320" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Длительность звуков, их чередование</text>
</svg>''',

    3: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes speed{0%{transform:translateX(0)}100%{transform:translateX(5px)}50%{transform:translateX(0)}}.tempo{animation:speed 1s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF8E1"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#E65100">Темп и динамика</text>
  <!-- Tempo -->
  <rect x="30" y="50" width="210" height="150" fill="white" rx="10" stroke="#FFE082" stroke-width="2"/>
  <text x="135" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#E65100">Темп</text>
  <text x="135" y="88" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Скорость музыки</text>
  <g font-family="Arial,sans-serif" font-size="12">
    <rect x="50" y="100" width="170" height="25" fill="#BBDEFB" rx="5"/><text x="135" y="118" text-anchor="middle" fill="#1565C0">Медленно (адажио)</text>
    <rect x="50" y="130" width="170" height="25" fill="#C8E6C9" rx="5"/><text x="135" y="148" text-anchor="middle" fill="#2E7D32">Умеренно (анданте)</text>
    <rect x="50" y="160" width="170" height="25" fill="#FFCDD2" rx="5"/><text x="135" y="178" text-anchor="middle" fill="#C62828">Быстро (аллегро)</text>
  </g>
  <!-- Dynamics -->
  <rect x="260" y="50" width="210" height="150" fill="white" rx="10" stroke="#FFE082" stroke-width="2"/>
  <text x="365" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#E65100">Динамика</text>
  <text x="365" y="88" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Громкость музыки</text>
  <g font-family="Arial,sans-serif" font-size="12">
    <rect x="280" y="100" width="170" height="22" fill="#E3F2FD" rx="5"/><text x="365" y="116" text-anchor="middle" fill="#1565C0">Тихо (пиано)</text>
    <rect x="280" y="128" width="170" height="22" fill="#FFF9C4" rx="5"/><text x="365" y="144" text-anchor="middle" fill="#F57F17">Средне (меццо)</text>
    <rect x="280" y="156" width="170" height="22" fill="#FFCDD2" rx="5"/><text x="365" y="172" text-anchor="middle" fill="#C62828">Громко (форте)</text>
  </g>
  <!-- Examples -->
  <rect x="30" y="215" width="440" height="120" fill="#FFF8E1" rx="10"/>
  <text x="250" y="238" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#E65100">Примеры в музыке</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="260">Колыбельная — медленно и тихо</text>
    <text x="50" y="280">Марш — умеренно и громко</text>
    <text x="50" y="300">Гроза в музыке — быстро и громко</text>
    <text x="50" y="320" fill="#E65100">Темп и динамика создают настроение!</text>
  </g>
</svg>''',

    4: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes play{0%,100%{transform:rotate(-2deg)}50%{transform:rotate(2deg)}}.instrument{animation:play 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E8F5E9"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#1B5E20">Музыкальные инструменты</text>
  <!-- Groups -->
  <rect x="30" y="50" width="440" height="150" fill="white" rx="10" stroke="#A5D6A7" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#1B5E20">Группы инструментов</text>
  <g font-family="Arial,sans-serif" font-size="11">
    <rect x="50" y="82" width="130" height="50" fill="#FFCCBC" rx="5"/>
    <text x="115" y="100" text-anchor="middle" fill="#BF360C" font-weight="bold">Струнные</text>
    <text x="115" y="118" text-anchor="middle" fill="#555">скрипка, гитара</text>
    <rect x="195" y="82" width="130" height="50" fill="#BBDEFB" rx="5"/>
    <text x="260" y="100" text-anchor="middle" fill="#0D47A1" font-weight="bold">Духовые</text>
    <text x="260" y="118" text-anchor="middle" fill="#555">флейта, труба</text>
    <rect x="340" y="82" width="110" height="50" fill="#FFF9C4" rx="5"/>
    <text x="395" y="100" text-anchor="middle" fill="#F57F17" font-weight="bold">Ударные</text>
    <text x="395" y="118" text-anchor="middle" fill="#555">барабан, пианино</text>
    <rect x="50" y="142" width="130" height="50" fill="#C8E6C9" rx="5"/>
    <text x="115" y="160" text-anchor="middle" fill="#2E7D32" font-weight="bold">Клавишные</text>
    <text x="115" y="178" text-anchor="middle" fill="#555">пианино, орган</text>
    <rect x="195" y="142" width="130" height="50" fill="#E1BEE7" rx="5"/>
    <text x="260" y="160" text-anchor="middle" fill="#6A1B9A" font-weight="bold">Народные</text>
    <text x="260" y="178" text-anchor="middle" fill="#555">балалайка, баян</text>
  </g>
  <!-- How sound is made -->
  <rect x="30" y="215" width="440" height="120" fill="#E8F5E9" rx="10"/>
  <text x="250" y="238" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1B5E20">Как извлекается звук</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="260">Струнные — дёргают струны</text>
    <text x="50" y="280">Духовые — дуют в трубку</text>
    <text x="50" y="300">Ударные — бьют по поверхности</text>
    <text x="50" y="320">Клавишные — нажимают клавиши</text>
  </g>
</svg>''',

    5: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes folk{0%,100%{transform:scale(1)}50%{transform:scale(1.03)}}.traditional{animation:folk 3s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF3E0"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#BF360C">Русские народные песни</text>
  <!-- Song types -->
  <rect x="30" y="50" width="440" height="150" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#BF360C">Виды народных песен</text>
  <g font-family="Arial,sans-serif" font-size="11">
    <rect x="50" y="82" width="130" height="45" fill="#FFCDD2" rx="5"/><text x="115" y="100" text-anchor="middle" fill="#C62828" font-weight="bold">Колыбельные</text><text x="115" y="118" text-anchor="middle" fill="#555">баю-баю, спи малыш</text>
    <rect x="195" y="82" width="130" height="45" fill="#FFECB3" rx="5"/><text x="260" y="100" text-anchor="middle" fill="#E65100" font-weight="bold">Хороводные</text><text x="260" y="118" text-anchor="middle" fill="#555">во поле берёза стояла</text>
    <rect x="340" y="82" width="110" height="45" fill="#C8E6C9" rx="5"/><text x="395" y="100" text-anchor="middle" fill="#2E7D32" font-weight="bold">Плясовые</text><text x="395" y="118" text-anchor="middle" fill="#555">весёлые, задорные</text>
    <rect x="50" y="140" width="130" height="45" fill="#BBDEFB" rx="5"/><text x="115" y="158" text-anchor="middle" fill="#0D47A1" font-weight="bold">Обрядовые</text><text x="115" y="176" text-anchor="middle" fill="#555">Масленица, Коляда</text>
    <rect x="195" y="140" width="130" height="45" fill="#E1BEE7" rx="5"/><text x="260" y="158" text-anchor="middle" fill="#6A1B9A" font-weight="bold">Трудовые</text><text x="260" y="176" text-anchor="middle" fill="#555">пели за работой</text>
    <rect x="340" y="140" width="110" height="45" fill="#F8BBD0" rx="5"/><text x="395" y="158" text-anchor="middle" fill="#AD1457" font-weight="bold">Лирические</text><text x="395" y="176" text-anchor="middle" fill="#555">о любви, грустные</text>
  </g>
  <!-- Features -->
  <rect x="30" y="215" width="440" height="120" fill="#FFF3E0" rx="10"/>
  <text x="250" y="238" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#BF360C">Особенности народных песен</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="260">Передаются из поколения в поколение</text>
    <text x="50" y="280">Автор неизвестен — народное творчество</text>
    <text x="50" y="300">Исполняются хором или соло</text>
    <text x="50" y="320" fill="#BF360C">Народная песня — душа русского народа</text>
  </g>
</svg>''',

    6: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes compose{0%,100%{transform:rotate(-2deg)}50%{transform:rotate(2deg)}}.note{animation:compose 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E8EAF6"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#283593">Композиторы России</text>
  <!-- Composers -->
  <rect x="30" y="50" width="440" height="150" fill="white" rx="10" stroke="#9FA8DA" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#283593">Великие русские композиторы</text>
  <g font-family="Arial,sans-serif" font-size="11">
    <rect x="50" y="82" width="200" height="30" fill="#C5CAE9" rx="5"/><text x="150" y="102" text-anchor="middle" fill="#283593" font-weight="bold">М.И. Глинка (1804-1857)</text>
    <rect x="260" y="82" width="200" height="30" fill="#E8EAF6" rx="5"/><text x="360" y="102" text-anchor="middle" fill="#283593" font-weight="bold">П.И. Чайковский (1840-1893)</text>
    <rect x="50" y="120" width="200" height="30" fill="#E8EAF6" rx="5"/><text x="150" y="140" text-anchor="middle" fill="#283593" font-weight="bold">Н.А. Римский-Корсаков</text>
    <rect x="260" y="120" width="200" height="30" fill="#C5CAE9" rx="5"/><text x="360" y="140" text-anchor="middle" fill="#283593" font-weight="bold">С.В. Рахманинов</text>
    <rect x="50" y="158" width="200" height="30" fill="#C5CAE9" rx="5"/><text x="150" y="178" text-anchor="middle" fill="#283593" font-weight="bold">М.П. Мусоргский</text>
    <rect x="260" y="158" width="200" height="30" fill="#E8EAF6" rx="5"/><text x="360" y="178" text-anchor="middle" fill="#283593" font-weight="bold">Д.Д. Шостакович</text>
  </g>
  <!-- Famous works -->
  <rect x="30" y="215" width="440" height="120" fill="#E8EAF6" rx="10"/>
  <text x="250" y="238" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#283593">Известные произведения</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="260">Глинка — опера «Руслан и Людмила»</text>
    <text x="50" y="280">Чайковский — балет «Щелкунчик»</text>
    <text x="50" y="300">Римский-Корсаков — «Полет шмеля»</text>
    <text x="50" y="320" fill="#283593">Русская музыка — одна из величайших в мире!</text>
  </g>
</svg>'''
}

# ============================================================
# PE SVGs (8 lessons)
# ============================================================
pe_svgs = {
    1: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes stand{0%,100%{transform:translateY(0)}50%{transform:translateY(-2px)}}.march{animation:stand 1.5s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E8F5E9"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#1B5E20">Строевые упражнения</text>
  <!-- Figure doing drill -->
  <g class="march" transform="translate(60,55)">
    <circle cx="50" cy="20" r="18" fill="#C8E6C9" stroke="#2E7D32" stroke-width="2"/>
    <rect x="35" y="40" width="30" height="45" fill="#2E7D32" rx="5"/>
    <rect x="20" y="45" width="15" height="5" fill="#2E7D32" rx="2"/>
    <rect x="65" y="45" width="15" height="5" fill="#2E7D32" rx="2"/>
    <rect x="38" y="85" width="10" height="40" fill="#1B5E20" rx="3"/>
    <rect x="52" y="85" width="10" height="40" fill="#1B5E20" rx="3"/>
  </g>
  <!-- Commands -->
  <rect x="180" y="55" width="290" height="120" fill="white" rx="10" stroke="#A5D6A7" stroke-width="2"/>
  <text x="325" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#1B5E20">Строевые команды</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="195" y="100">«Становись!» — построение</text>
    <text x="195" y="118">«Равняйсь!» — выровняться</text>
    <text x="195" y="136">«Смирно!» — стойка прямо</text>
    <text x="195" y="154">«Вольно!» — расслабиться</text>
  </g>
  <!-- Formations -->
  <rect x="30" y="190" width="440" height="145" fill="#E8F5E9" rx="10"/>
  <text x="250" y="213" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1B5E20">Построения</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="235">Шеренга — в один ряд</text>
    <text x="50" y="255">Колонна — друг за другом</text>
    <text x="50" y="275">Круг — по окружности</text>
    <text x="50" y="295">Две шеренги — в два ряда</text>
    <text x="50" y="315" fill="#1B5E20">Строевые упражнения учат дисциплине</text>
    <text x="50" y="332" fill="#555">и согласованности действий</text>
  </g>
</svg>''',

    2: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes stretch{0%,100%{transform:scaleY(1)}50%{transform:scaleY(1.05)}}.exercise{animation:stretch 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF3E0"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#E65100">Общеразвивающие упражнения</text>
  <!-- Exercises -->
  <rect x="30" y="50" width="440" height="170" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#E65100">Виды упражнений</text>
  <g font-family="Arial,sans-serif" font-size="11">
    <rect x="50" y="82" width="130" height="40" fill="#FFCCBC" rx="5"/><text x="115" y="100" text-anchor="middle" fill="#BF360C" font-weight="bold">Для рук</text><text x="115" y="115" text-anchor="middle" fill="#555">вращения, махи</text>
    <rect x="195" y="82" width="130" height="40" fill="#FFE0B2" rx="5"/><text x="260" y="100" text-anchor="middle" fill="#E65100" font-weight="bold">Для ног</text><text x="260" y="115" text-anchor="middle" fill="#555">приседания, выпады</text>
    <rect x="340" y="82" width="110" height="40" fill="#FFF9C4" rx="5"/><text x="395" y="100" text-anchor="middle" fill="#F57F17" font-weight="bold">Для спины</text><text x="395" y="115" text-anchor="middle" fill="#555">наклоны</text>
    <rect x="50" y="132" width="130" height="40" fill="#C8E6C9" rx="5"/><text x="115" y="150" text-anchor="middle" fill="#2E7D32" font-weight="bold">Для пресса</text><text x="115" y="165" text-anchor="middle" fill="#555">скручивания</text>
    <rect x="195" y="132" width="130" height="40" fill="#BBDEFB" rx="5"/><text x="260" y="150" text-anchor="middle" fill="#1565C0" font-weight="bold">Прыжки</text><text x="260" y="165" text-anchor="middle" fill="#555">на месте, в длину</text>
    <rect x="340" y="132" width="110" height="40" fill="#E1BEE7" rx="5"/><text x="395" y="150" text-anchor="middle" fill="#6A1B9A" font-weight="bold">Для шеи</text><text x="395" y="165" text-anchor="middle" fill="#555">повороты</text>
  </g>
  <!-- Rules -->
  <rect x="30" y="235" width="440" height="100" fill="#FFF3E0" rx="10"/>
  <text x="250" y="258" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#E65100">Правила выполнения</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="278">Начинай с разминки</text>
    <text x="50" y="296">Делай плавно, без рывков</text>
    <text x="50" y="314">Дыши ровно: усилие — выдох</text>
    <text x="50" y="332" fill="#E65100">Упражнения развивают силу и гибкость!</text>
  </g>
</svg>''',

    3: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes flip{0%,100%{transform:rotate(0deg)}50%{transform:rotate(3deg)}}.acro{animation:flip 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E3F2FD"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#0D47A1">Акробатические упражнения</text>
  <!-- Acrobatic elements -->
  <rect x="30" y="50" width="440" height="120" fill="white" rx="10" stroke="#90CAF9" stroke-width="2"/>
  <g font-family="Arial,sans-serif" font-size="12">
    <rect x="50" y="60" width="120" height="40" fill="#BBDEFB" rx="5"/><text x="110" y="78" text-anchor="middle" fill="#0D47A1" font-weight="bold">Кувырок</text><text x="110" y="95" text-anchor="middle" fill="#555" font-size="10">вперёд и назад</text>
    <rect x="185" y="60" width="120" height="40" fill="#90CAF9" rx="5"/><text x="245" y="78" text-anchor="middle" fill="#0D47A1" font-weight="bold">Стойка</text><text x="245" y="95" text-anchor="middle" fill="#555" font-size="10">на лопатках</text>
    <rect x="320" y="60" width="130" height="40" fill="#64B5F6" rx="5"/><text x="385" y="78" text-anchor="middle" fill="white" font-weight="bold">Мост</text><text x="385" y="95" text-anchor="middle" fill="white" font-size="10">из положения лёжа</text>
    <rect x="50" y="115" width="120" height="40" fill="#42A5F5" rx="5"/><text x="110" y="133" text-anchor="middle" fill="white" font-weight="bold">Берёзка</text><text x="110" y="148" text-anchor="middle" fill="white" font-size="10">стойка на плечах</text>
    <rect x="185" y="115" width="120" height="40" fill="#BBDEFB" rx="5"/><text x="245" y="133" text-anchor="middle" fill="#0D47A1" font-weight="bold">Ласточка</text><text x="245" y="148" text-anchor="middle" fill="#555" font-size="10">равновесие</text>
    <rect x="320" y="115" width="130" height="40" fill="#90CAF9" rx="5"/><text x="385" y="133" text-anchor="middle" fill="#0D47A1" font-weight="bold">Колесо</text><text x="385" y="148" text-anchor="middle" fill="#555" font-size="10">боковой переворот</text>
  </g>
  <!-- Safety -->
  <rect x="30" y="185" width="440" height="155" fill="#E3F2FD" rx="10"/>
  <text x="250" y="208" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0D47A1">Техника безопасности</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="230">Делать только на мате!</text>
    <text x="50" y="250">Учитель должен быть рядом</text>
    <text x="50" y="270">Не спешить, осваивать постепенно</text>
    <text x="50" y="290">При кувырке подбородок к груди</text>
    <text x="50" y="310">При мосте — опираться на руки и ноги</text>
    <text x="50" y="330" fill="#0D47A1">Акробатика развивает ловкость и координацию!</text>
  </g>
</svg>''',

    4: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes balance{0%,100%{transform:rotate(-1deg)}50%{transform:rotate(1deg)}}.beam{animation:balance 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FBE9E7"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#BF360C">Упражнения на равновесие</text>
  <!-- Balance beam -->
  <g class="beam" transform="translate(30,50)">
    <rect x="0" y="100" width="440" height="8" fill="#8D6E63" rx="3"/>
    <rect x="0" y="108" width="440" height="5" fill="#5D4037" rx="2"/>
    <!-- Figure on beam -->
    <circle cx="220" cy="70" r="15" fill="#FFAB91" stroke="#BF360C" stroke-width="2"/>
    <rect x="210" y="85" width="20" height="15" fill="#BF360C" rx="3"/>
  </g>
  <!-- Exercises -->
  <rect x="30" y="175" width="440" height="165" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <text x="250" y="198" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#BF360C">Упражнения на равновесие</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="220">Стойка на одной ноге</text>
    <text x="50" y="240">Ходьба по гимнастической скамейке</text>
    <text x="50" y="260">Поза «ласточка»</text>
    <text x="50" y="280">Ходьба по линии с закрытыми глазами</text>
    <text x="50" y="300">Кружение на месте (5-10 раз)</text>
    <text x="50" y="320" fill="#BF360C">Равновесие развивает координацию и вестибулярный аппарат</text>
  </g>
</svg>''',

    5: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes run{0%,100%{transform:translateX(0)}50%{transform:translateX(5px)}}.sprint{animation:run 0.8s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E8F5E9"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#1B5E20">Беговые упражнения</text>
  <!-- Running track -->
  <rect x="30" y="50" width="440" height="80" fill="#FFECB3" rx="10"/>
  <line x1="30" y1="60" x2="470" y2="60" stroke="#F9A825" stroke-width="2" stroke-dasharray="10,5"/>
  <line x1="30" y1="80" x2="470" y2="80" stroke="#F9A825" stroke-width="2" stroke-dasharray="10,5"/>
  <line x1="30" y1="100" x2="470" y2="100" stroke="#F9A825" stroke-width="2" stroke-dasharray="10,5"/>
  <line x1="30" y1="120" x2="470" y2="120" stroke="#F9A825" stroke-width="2"/>
  <g class="sprint" font-family="Arial,sans-serif" font-size="20" fill="#1B5E20">
    <text x="100" y="85">&#127939;</text>
    <text x="250" y="85">&#127939;</text>
    <text x="380" y="85">&#127939;</text>
  </g>
  <!-- Types -->
  <rect x="30" y="145" width="440" height="100" fill="white" rx="10" stroke="#A5D6A7" stroke-width="2"/>
  <text x="250" y="168" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1B5E20">Виды бега</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="190">Обычный бег — спокойный темп</text>
    <text x="50" y="208">Бег с высоким подниманием бедра</text>
    <text x="50" y="226">Бег с захлёстом голени</text>
    <text x="50" y="244">Челночный бег — туда-обратно</text>
  </g>
  <!-- Rules -->
  <rect x="30" y="260" width="440" height="75" fill="#E8F5E9" rx="10"/>
  <text x="250" y="283" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1B5E20">Правила бега</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="303">Дыши: вдох через нос, выдох через рот</text>
    <text x="50" y="323">Руки согнуты, работают вдоль тела</text>
  </g>
</svg>''',

    6: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes jump{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}.leap{animation:jump 1s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF3E0"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#E65100">Прыжки</text>
  <!-- Jump types -->
  <rect x="30" y="50" width="440" height="140" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#E65100">Виды прыжков</text>
  <g font-family="Arial,sans-serif" font-size="12">
    <rect x="50" y="82" width="130" height="35" fill="#FFCCBC" rx="5"/><text x="115" y="100" text-anchor="middle" fill="#BF360C" font-weight="bold">В длину</text><text x="115" y="114" text-anchor="middle" fill="#555" font-size="10">с места и с разбега</text>
    <rect x="195" y="82" width="130" height="35" fill="#FFE0B2" rx="5"/><text x="260" y="100" text-anchor="middle" fill="#E65100" font-weight="bold">В высоту</text><text x="260" y="114" text-anchor="middle" fill="#555" font-size="10">перешагивание</text>
    <rect x="340" y="82" width="110" height="35" fill="#FFF9C4" rx="5"/><text x="395" y="100" text-anchor="middle" fill="#F57F17" font-weight="bold">На месте</text><text x="395" y="114" text-anchor="middle" fill="#555" font-size="10">на двух ногах</text>
    <rect x="50" y="130" width="130" height="35" fill="#C8E6C9" rx="5"/><text x="115" y="148" text-anchor="middle" fill="#2E7D32" font-weight="bold">Со скакалкой</text><text x="115" y="162" text-anchor="middle" fill="#555" font-size="10">на двух, на одной</text>
    <rect x="195" y="130" width="130" height="35" fill="#BBDEFB" rx="5"/><text x="260" y="148" text-anchor="middle" fill="#1565C0" font-weight="bold">Через гимн.</text><text x="260" y="162" text-anchor="middle" fill="#555" font-size="10">козла</text>
  </g>
  <!-- Technique -->
  <rect x="30" y="205" width="440" height="130" fill="#FFF3E0" rx="10"/>
  <text x="250" y="228" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#E65100">Техника прыжка в длину с места</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="250">1. Встать на линию, ноги на ширине плеч</text>
    <text x="50" y="270">2. Отвести руки назад, присесть</text>
    <text x="50" y="290">3. Оттолкнуться обеими ногами</text>
    <text x="50" y="310">4. Махнуть руками вперёд-вверх</text>
    <text x="50" y="330" fill="#E65100">5. Приземлиться на обе ноги, согнув колени</text>
  </g>
</svg>''',

    7: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes throw{0%,100%{transform:rotate(0deg)}50%{transform:rotate(10deg)}}.ball{animation:throw 1.5s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E3F2FD"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#0D47A1">Метание</text>
  <!-- Throwing types -->
  <rect x="30" y="50" width="440" height="120" fill="white" rx="10" stroke="#90CAF9" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#0D47A1">Виды метания</text>
  <g font-family="Arial,sans-serif" font-size="12">
    <rect x="50" y="82" width="180" height="35" fill="#BBDEFB" rx="5"/><text x="140" y="100" text-anchor="middle" fill="#0D47A1" font-weight="bold">Метание вдаль</text><text x="140" y="114" text-anchor="middle" fill="#555" font-size="10">мяча на дальность</text>
    <rect x="245" y="82" width="200" height="35" fill="#90CAF9" rx="5"/><text x="345" y="100" text-anchor="middle" fill="#0D47A1" font-weight="bold">Метание в цель</text><text x="345" y="114" text-anchor="middle" fill="#555" font-size="10">попасть в мишень</text>
    <rect x="50" y="128" width="180" height="35" fill="#64B5F6" rx="5"/><text x="140" y="146" text-anchor="middle" fill="white" font-weight="bold">Метание снизу</text><text x="140" y="158" text-anchor="middle" fill="white" font-size="10">как в игре «цирки»</text>
    <rect x="245" y="128" width="200" height="35" fill="#42A5F5" rx="5"/><text x="345" y="146" text-anchor="middle" fill="white" font-weight="bold">Метание сверху</text><text x="345" y="158" text-anchor="middle" fill="white" font-size="10">как в игре «вышибалы»</text>
  </g>
  <!-- Technique -->
  <rect x="30" y="185" width="440" height="150" fill="#E3F2FD" rx="10"/>
  <text x="250" y="208" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0D47A1">Техника метания мяча вдаль</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="230">1. Встать боком к направлению</text>
    <text x="50" y="250">2. Замахнуть руку назад</text>
    <text x="50" y="270">3. Перенести вес на толчковую ногу</text>
    <text x="50" y="290">4. Бросить мяч, выпрямив руку</text>
    <text x="50" y="310">5. Отпустить мяч в высшей точке</text>
    <text x="50" y="330" fill="#0D47A1">Метание развивает силу рук и глазомер!</text>
  </g>
</svg>''',

    8: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes play{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}.fun{animation:play 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF8E1"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#E65100">Игры с бегом</text>
  <!-- Games -->
  <rect x="30" y="50" width="440" height="160" fill="white" rx="10" stroke="#FFE082" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#E65100">Подвижные игры с бегом</text>
  <g font-family="Arial,sans-serif" font-size="11">
    <rect x="50" y="82" width="130" height="40" fill="#FFCDD2" rx="5"/><text x="115" y="100" text-anchor="middle" fill="#C62828" font-weight="bold">Салки</text><text x="115" y="115" text-anchor="middle" fill="#555">догонялки</text>
    <rect x="195" y="82" width="130" height="40" fill="#FFECB3" rx="5"/><text x="260" y="100" text-anchor="middle" fill="#E65100" font-weight="bold">Вышибалы</text><text x="260" y="115" text-anchor="middle" fill="#555">мячом из круга</text>
    <rect x="340" y="82" width="110" height="40" fill="#C8E6C9" rx="5"/><text x="395" y="100" text-anchor="middle" fill="#2E7D32" font-weight="bold">Третий</text><text x="395" y="115" text-anchor="middle" fill="#555">лишний</text>
    <rect x="50" y="132" width="130" height="40" fill="#BBDEFB" rx="5"/><text x="115" y="150" text-anchor="middle" fill="#1565C0" font-weight="bold">Караси</text><text x="115" y="165" text-anchor="middle" fill="#555">и щука</text>
    <rect x="195" y="132" width="130" height="40" fill="#E1BEE7" rx="5"/><text x="260" y="150" text-anchor="middle" fill="#6A1B9A" font-weight="bold">Совушка</text><text x="260" y="165" text-anchor="middle" fill="#555">замри!</text>
    <rect x="340" y="132" width="110" height="40" fill="#FFF9C4" rx="5"/><text x="395" y="150" text-anchor="middle" fill="#F57F17" font-weight="bold">Эстафета</text><text x="395" y="165" text-anchor="middle" fill="#555">команды</text>
  </g>
  <!-- Benefits -->
  <rect x="30" y="225" width="440" height="110" fill="#FFF8E1" rx="10"/>
  <text x="250" y="248" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#E65100">Чем полезны подвижные игры</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="270">Развивают быстроту и ловкость</text>
    <text x="50" y="290">Учат работать в команде</text>
    <text x="50" y="310">Укрепляют здоровье</text>
    <text x="50" y="330" fill="#E65100">Подвижные игры — это весело и полезно!</text>
  </g>
</svg>'''
}

# ============================================================
# TECH SVGs (6 lessons)
# ============================================================
tech_svgs = {
    1: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes fold{0%,100%{transform:scaleX(1)}50%{transform:scaleX(0.97)}}.paper{animation:fold 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E3F2FD"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#0D47A1">Свойства бумаги</text>
  <!-- Paper types -->
  <rect x="30" y="50" width="440" height="120" fill="white" rx="10" stroke="#90CAF9" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#0D47A1">Виды бумаги</text>
  <g font-family="Arial,sans-serif" font-size="11">
    <rect x="50" y="82" width="100" height="35" fill="#FFECB3" rx="5"/><text x="100" y="100" text-anchor="middle" fill="#E65100">Писчая</text><text x="100" y="112" text-anchor="middle" fill="#555" font-size="9">тетради</text>
    <rect x="165" y="82" width="100" height="35" fill="#FFCDD2" rx="5"/><text x="215" y="100" text-anchor="middle" fill="#C62828">Картон</text><text x="215" y="112" text-anchor="middle" fill="#555" font-size="9">коробки</text>
    <rect x="280" y="82" width="100" height="35" fill="#C8E6C9" rx="5"/><text x="330" y="100" text-anchor="middle" fill="#2E7D32">Гофрированная</text><text x="330" y="112" text-anchor="middle" fill="#555" font-size="9">упаковка</text>
    <rect x="50" y="128" width="100" height="35" fill="#BBDEFB" rx="5"/><text x="100" y="146" text-anchor="middle" fill="#1565C0">Копирка</text><text x="100" y="158" text-anchor="middle" fill="#555" font-size="9">перевод</text>
    <rect x="165" y="128" width="100" height="35" fill="#E1BEE7" rx="5"/><text x="215" y="146" text-anchor="middle" fill="#6A1B9A">Бархатная</text><text x="215" y="158" text-anchor="middle" fill="#555" font-size="9">открытки</text>
    <rect x="280" y="128" width="100" height="35" fill="#FFF9C4" rx="5"/><text x="330" y="146" text-anchor="middle" fill="#F57F17">Цветная</text><text x="330" y="158" text-anchor="middle" fill="#555" font-size="9">аппликации</text>
  </g>
  <!-- Properties -->
  <rect x="30" y="185" width="440" height="155" fill="#E3F2FD" rx="10"/>
  <text x="250" y="208" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0D47A1">Свойства бумаги</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="230">Легко режется ножницами</text>
    <text x="50" y="250">Сгибается и складывается</text>
    <text x="50" y="270">Склеивается клеем</text>
    <text x="50" y="290">Пропускает свет (прозрачная)</text>
    <text x="50" y="310">Намокает от воды</text>
    <text x="50" y="330" fill="#0D47A1">Бумагу делают из древесины — береги лес!</text>
  </g>
</svg>''',

    2: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes bloom{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}.flower{animation:bloom 3s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FCE4EC"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#880E4F">Аппликация «Цветы»</text>
  <!-- Flower -->
  <g class="flower" transform="translate(30,55)">
    <rect x="0" y="0" width="180" height="145" fill="white" rx="10" stroke="#F48FB1" stroke-width="2"/>
    <circle cx="90" cy="60" r="25" fill="#FFC107"/>
    <circle cx="90" cy="30" r="18" fill="#F44336"/>
    <circle cx="115" cy="45" r="18" fill="#E91E63"/>
    <circle cx="115" cy="75" r="18" fill="#FF5722"/>
    <circle cx="90" cy="90" r="18" fill="#F44336"/>
    <circle cx="65" cy="75" r="18" fill="#E91E63"/>
    <circle cx="65" cy="45" r="18" fill="#FF5722"/>
    <rect x="85" y="90" width="10" height="45" fill="#4CAF50"/>
    <ellipse cx="60" cy="120" rx="20" ry="8" fill="#66BB6A" transform="rotate(-30,60,120)"/>
  </g>
  <!-- Steps -->
  <rect x="230" y="55" width="240" height="145" fill="white" rx="10" stroke="#F48FB1" stroke-width="2"/>
  <text x="350" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#880E4F">Этапы работы</text>
  <g font-family="Arial,sans-serif" font-size="11" fill="#333">
    <text x="245" y="98">1. Подготовить цветную бумагу</text>
    <text x="245" y="115">2. Нарисовать детали цветка</text>
    <text x="245" y="132">3. Вырезать лепестки, стебель</text>
    <text x="245" y="149">4. Разложить на основе</text>
    <text x="245" y="166">5. Приклеить по порядку</text>
    <text x="245" y="183">6. Украсить дополнительно</text>
  </g>
  <!-- Tips -->
  <rect x="30" y="215" width="440" height="120" fill="#FCE4EC" rx="10"/>
  <text x="250" y="238" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#880E4F">Советы по аппликации</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="260">Клей наносить тонким слоем</text>
    <text x="50" y="280">Сначала крупные детали, потом мелкие</text>
    <text x="50" y="300">Лепестки можно наклеивать внахлёст</text>
    <text x="50" y="320" fill="#880E4F">Аппликация — вырезание и наклеивание фигур</text>
  </g>
</svg>''',

    3: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes fly{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}.bird{animation:fly 1.5s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E3F2FD"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#0D47A1">Оригами «Голубь»</text>
  <!-- Origami dove -->
  <g class="bird" transform="translate(30,55)">
    <rect x="0" y="0" width="180" height="130" fill="white" rx="10" stroke="#90CAF9" stroke-width="2"/>
    <!-- Stylized origami bird -->
    <polygon points="90,20 60,60 90,50" fill="#BBDEFB" stroke="#1565C0" stroke-width="1.5"/>
    <polygon points="90,20 120,60 90,50" fill="#90CAF9" stroke="#1565C0" stroke-width="1.5"/>
    <polygon points="60,60 90,50 50,80" fill="#BBDEFB" stroke="#1565C0" stroke-width="1.5"/>
    <polygon points="120,60 90,50 130,80" fill="#90CAF9" stroke="#1565C0" stroke-width="1.5"/>
    <polygon points="90,50 90,100 75,110" fill="#BBDEFB" stroke="#1565C0" stroke-width="1.5"/>
    <polygon points="90,50 90,100 105,110" fill="#90CAF9" stroke="#1565C0" stroke-width="1.5"/>
    <circle cx="82" cy="38" r="2" fill="#0D47A1"/>
  </g>
  <!-- Steps -->
  <rect x="230" y="55" width="240" height="130" fill="white" rx="10" stroke="#90CAF9" stroke-width="2"/>
  <text x="350" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0D47A1">Что такое оригами?</text>
  <g font-family="Arial,sans-serif" font-size="11" fill="#333">
    <text x="245" y="98">Оригами — японское искусство</text>
    <text x="245" y="115">складывания фигурок из бумаги</text>
    <text x="245" y="135">Нужен только квадратный лист!</text>
    <text x="245" y="155">Без клея и ножниц</text>
    <text x="245" y="175" fill="#0D47A1">Голубь — символ мира</text>
  </g>
  <!-- Folding tips -->
  <rect x="30" y="200" width="440" height="135" fill="#E3F2FD" rx="10"/>
  <text x="250" y="222" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0D47A1">Правила складывания</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="245">Сгибай аккуратно, проглаживай линию</text>
    <text x="50" y="265">Совмещай углы точно</text>
    <text x="50" y="285">Делай сгибы в одном направлении</text>
    <text x="50" y="305">Следуй инструкции шаг за шагом</text>
    <text x="50" y="325" fill="#0D47A1">Оригами развивает терпение и мелкую моторику!</text>
  </g>
</svg>''',

    4: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes pop{0%,100%{transform:scale(1)}50%{transform:scale(1.03)}}.volume{animation:pop 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF3E0"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#E65100">Объёмные поделки</text>
  <!-- 3D shapes -->
  <g class="volume" transform="translate(30,55)">
    <rect x="0" y="0" width="440" height="120" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
    <!-- Cube -->
    <g transform="translate(50,15)">
      <rect x="0" y="20" width="50" height="50" fill="#FFCCBC" stroke="#E65100" stroke-width="1.5"/>
      <polygon points="0,20 15,5 65,5 50,20" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
      <polygon points="50,20 65,5 65,55 50,70" fill="#FFAB91" stroke="#E65100" stroke-width="1.5"/>
      <text x="25" y="95" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#E65100">Кубик</text>
    </g>
    <!-- Cylinder -->
    <g transform="translate(170,15)">
      <rect x="10" y="20" width="50" height="50" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1.5"/>
      <ellipse cx="35" cy="20" rx="25" ry="10" fill="#DCEDC8" stroke="#2E7D32" stroke-width="1.5"/>
      <ellipse cx="35" cy="70" rx="25" ry="10" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1.5"/>
      <text x="35" y="95" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32">Цилиндр</text>
    </g>
    <!-- Cone -->
    <g transform="translate(300,10)">
      <polygon points="30,0 0,70 60,70" fill="#BBDEFB" stroke="#1565C0" stroke-width="1.5"/>
      <ellipse cx="30" cy="70" rx="30" ry="10" fill="#90CAF9" stroke="#1565C0" stroke-width="1.5"/>
      <text x="30" y="95" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1565C0">Конус</text>
    </g>
  </g>
  <!-- Techniques -->
  <rect x="30" y="195" width="440" height="140" fill="#FFF3E0" rx="10"/>
  <text x="250" y="218" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#E65100">Способы создания объёма</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="240">Сгибание и склеивание</text>
    <text x="50" y="260">Складывание гармошкой</text>
    <text x="50" y="280">Скручивание в трубочку</text>
    <text x="50" y="300">Надрезание и отгибание</text>
    <text x="50" y="320" fill="#E65100">Объёмные поделки украшают и развивают пространственное мышление</text>
</svg>''',

    5: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes cone{0%,100%{transform:rotate(-2deg)}50%{transform:rotate(2deg)}}.pine{animation:cone 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E8F5E9"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#1B5E20">Поделки из шишек</text>
  <!-- Pine cone craft -->
  <g class="pine" transform="translate(30,55)">
    <rect x="0" y="0" width="180" height="130" fill="white" rx="10" stroke="#A5D6A7" stroke-width="2"/>
    <!-- Pine cone body -->
    <ellipse cx="90" cy="65" rx="35" ry="45" fill="#8D6E63"/>
    <ellipse cx="90" cy="65" rx="30" ry="40" fill="#795548"/>
    <!-- Eyes -->
    <circle cx="80" cy="50" r="5" fill="white"/><circle cx="80" cy="50" r="2.5" fill="#333"/>
    <circle cx="100" cy="50" r="5" fill="white"/><circle cx="100" cy="50" r="2.5" fill="#333"/>
    <!-- Beak -->
    <polygon points="90,58 85,62 90,66 95,62" fill="#FF9800"/>
    <!-- Wings -->
    <ellipse cx="55" cy="65" rx="18" ry="25" fill="#A5D6A7" transform="rotate(15,55,65)"/>
    <ellipse cx="125" cy="65" rx="18" ry="25" fill="#A5D6A7" transform="rotate(-15,125,65)"/>
  </g>
  <!-- Materials and steps -->
  <rect x="230" y="55" width="240" height="130" fill="white" rx="10" stroke="#A5D6A7" stroke-width="2"/>
  <text x="350" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1B5E20">Что понадобится</text>
  <g font-family="Arial,sans-serif" font-size="11" fill="#333">
    <text x="245" y="98">Шишки (сосновые, еловые)</text>
    <text x="245" y="115">Пластилин для соединения</text>
    <text x="245" y="132">Жёлуди, листья, веточки</text>
    <text x="245" y="149">Клей, ножницы</text>
    <text x="245" y="166">Фантазия и терпение!</text>
  </g>
  <!-- Ideas -->
  <rect x="30" y="200" width="440" height="135" fill="#E8F5E9" rx="10"/>
  <text x="250" y="222" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1B5E20">Идеи поделок из шишек</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="245">Ёжик (шишка + пластилин)</text>
    <text x="50" y="265">Совёнок (шишка + вата)</text>
    <text x="50" y="285">Олень (шишки + веточки)</text>
    <text x="50" y="305">Ёлочка (шишки + краска)</text>
    <text x="50" y="325" fill="#1B5E20">Природные материалы — экологичные и красивые!</text>
  </g>
</svg>''',

    6: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes fall{0%,100%{transform:rotate(-3deg)}50%{transform:rotate(3deg)}}.leaf{animation:fall 3s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF8E1"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#E65100">Аппликация из листьев</text>
  <!-- Leaf art -->
  <g class="leaf" transform="translate(30,55)">
    <rect x="0" y="0" width="180" height="130" fill="white" rx="10" stroke="#FFE082" stroke-width="2"/>
    <!-- Fish from leaves -->
    <ellipse cx="90" cy="65" rx="40" ry="25" fill="#FF9800"/>
    <polygon points="130,65 155,45 155,85" fill="#F44336"/>
    <circle cx="70" cy="58" r="5" fill="#333"/>
    <!-- Leaf veins -->
    <line x1="60" y1="65" x2="120" y2="65" stroke="#E65100" stroke-width="1"/>
    <line x1="70" y1="55" x2="90" y2="65" stroke="#E65100" stroke-width="0.5"/>
    <line x1="70" y1="75" x2="90" y2="65" stroke="#E65100" stroke-width="0.5"/>
  </g>
  <!-- How to -->
  <rect x="230" y="55" width="240" height="130" fill="white" rx="10" stroke="#FFE082" stroke-width="2"/>
  <text x="350" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#E65100">Как сделать аппликацию</text>
  <g font-family="Arial,sans-serif" font-size="11" fill="#333">
    <text x="245" y="98">1. Собрать листья осенью</text>
    <text x="245" y="115">2. Высушить между страниц книг</text>
    <text x="245" y="132">3. Подобрать по форме и цвету</text>
    <text x="245" y="149">4. Разложить рисунок на бумаге</text>
    <text x="245" y="166">5. Аккуратно приклеить</text>
  </g>
  <!-- Ideas -->
  <rect x="30" y="200" width="440" height="135" fill="#FFF8E1" rx="10"/>
  <text x="250" y="222" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#E65100">Идеи из листьев</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="245">Рыбка (овальный лист + хвост)</text>
    <text x="50" y="265">Бабочка (два листа крыльями)</text>
    <text x="50" y="285">Ёжик (дубовый лист + иголки)</text>
    <text x="50" y="305">Павлин (листья как хвост)</text>
    <text x="50" y="325" fill="#E65100">Осенние листья — бесплатный материал для творчества!</text>
  </g>
</svg>'''
}

# ============================================================
# PROJECTS SVGs (12 lessons)
# ============================================================
projects_svgs = {}
project_titles = [
    ("Моя семья", "#E3F2FD", "#0D47A1", "family"),
    ("Мой питомец", "#FFF3E0", "#E65100", "pet"),
    ("Времена года", "#C8E6C9", "#2E7D32", "seasons"),
    ("Мой город", "#F3E5F5", "#6A1B9A", "city"),
    ("Исследование растений", "#E8F5E9", "#1B5E20", "plants"),
    ("Погода и природа", "#E3F2FD", "#0D47A1", "weather"),
    ("Мир животных", "#FFF8E1", "#E65100", "animals"),
    ("Экологический проект", "#E8F5E9", "#1B5E20", "ecology"),
    ("Подготовка к защите", "#FBE9E7", "#BF360C", "prepare"),
    ("Наглядные материалы", "#EDE7F6", "#4527A0", "materials"),
    ("Выступление", "#FCE4EC", "#880E4F", "present"),
    ("Анализ проекта", "#E8EAF6", "#283593", "analysis"),
]

project_descriptions = [
    ["Собери фото семьи", "Напиши рассказ о каждом", "Составь семейное древо"],
    ["Фото или рисунок питомца", "Расскажи о повадках", "Чем кормишь, как ухаживаешь"],
    ["4 сезона: зима, весна, лето, осень", "Признаки каждого сезона", "Рисунки и наблюдения"],
    ["Достопримечательности", "Улицы и парки", "Что тебе нравится в городе"],
    ["Наблюдай за ростом", "Замеряй высоту растения", "Фото-дневник наблюдений"],
    ["Записывай погоду каждый день", "Облачность, осадки, ветер", "Нарисуй диаграмму погоды"],
    ["Выбери группу животных", "Подготовь факты и фото", "Сделай мини-доклад"],
    ["Проблемы экологии", "Как мы можем помочь", "Посади дерево или убери мусор"],
    ["Составь план выступления", "Потренируйся говорить", "Уложись в 3-5 минут"],
    ["Постер или презентация", "Рисунки, схемы, фото", "Четко и наглядно"],
    ["Говори громко и чётко", "Смотри на слушателей", "Отвечай на вопросы"],
    ["Что получилось хорошо?", "Что можно улучшить?", "Чему ты научился?"],
]

for i, ((title, bg, color, slug), desc) in enumerate(zip(project_titles, project_descriptions)):
    n = i + 1
    projects_svgs[n] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <rect width="500" height="350" fill="{bg}"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="{color}">{title}</text>
  <rect x="30" y="50" width="440" height="130" fill="white" rx="10" stroke="{color}" stroke-width="2" opacity="0.9"/>
  <text x="250" y="75" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="{color}">Что сделать в проекте</text>
  <g font-family="Arial,sans-serif" font-size="13" fill="#333">
    <text x="50" y="100">1. {desc[0]}</text>
    <text x="50" y="125">2. {desc[1]}</text>
    <text x="50" y="150">3. {desc[2]}</text>
  </g>
  <rect x="30" y="195" width="440" height="140" fill="{bg}" rx="10"/>
  <text x="250" y="218" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="{color}">Этапы работы над проектом</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="242">1. Выбери тему и поставь цель</text>
    <text x="50" y="262">2. Собери информацию</text>
    <text x="50" y="282">3. Создай продукт (постер, презентацию)</text>
    <text x="50" y="302">4. Подготовь выступление</text>
    <text x="50" y="322" fill="{color}">5. Представь проект классу!</text>
  </g>
</svg>'''

# Save all
for i, svg in art_svgs.items():
    path = os.path.join(SVG_DIR, 'art', f'lesson{i}-unique.svg')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg)

for i, svg in music_svgs.items():
    path = os.path.join(SVG_DIR, 'music', f'lesson{i}-unique.svg')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg)

for i, svg in pe_svgs.items():
    path = os.path.join(SVG_DIR, 'pe', f'lesson{i}-unique.svg')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg)

for i, svg in tech_svgs.items():
    path = os.path.join(SVG_DIR, 'tech', f'lesson{i}-unique.svg')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg)

for i, svg in projects_svgs.items():
    path = os.path.join(SVG_DIR, 'projects', f'lesson{i}-unique.svg')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg)

print(f"Saved: art({len(art_svgs)}) + music({len(music_svgs)}) + pe({len(pe_svgs)}) + tech({len(tech_svgs)}) + projects({len(projects_svgs)}) = {len(art_svgs)+len(music_svgs)+len(pe_svgs)+len(tech_svgs)+len(projects_svgs)} SVGs")
