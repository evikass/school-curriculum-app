#!/usr/bin/env python3
"""Grade 6 Biology, Lessons 17-24: Gymnosperms to Leaf"""
import os
D = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade6/biology"
os.makedirs(D, exist_ok=True)

def W(inner, title, sub, c="#2E7D32"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350"><defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#E8F5E9"/><stop offset="100%" stop-color="#C8E6C9"/></linearGradient></defs><rect width="500" height="350" fill="url(#bg)" rx="10"/><rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="{c}" stroke-width="2.5"/><text x="250" y="30" font-family="Arial,sans-serif" font-size="16" font-weight="bold" fill="{c}" text-anchor="middle">{title}</text><text x="250" y="46" font-family="Arial,sans-serif" font-size="10" fill="#888" text-anchor="middle">{sub}</text><line x1="30" y1="52" x2="470" y2="52" stroke="{c}" stroke-width="1.5" opacity="0.25"/>{inner}<rect x="10" y="325" width="480" height="20" rx="4" fill="{c}" opacity="0.85"/><text x="250" y="339" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="white" font-weight="bold">Биология 6 класс</text></svg>'

# 17: Общая характеристика голосеменных
l17 = W('''
  <!-- Pine tree -->
  <g transform="translate(130,175)">
    <rect x="-5" y="10" width="10" height="60" fill="#795548" rx="2"/>
    <path d="M0 -60 L-40 10 L40 10 Z" fill="#2E7D32" opacity="0.8"/>
    <path d="M0 -50 L-32 5 L32 5 Z" fill="#388E3C" opacity="0.7"/>
    <path d="M0 -38 L-22 0 L22 0 Z" fill="#43A047" opacity="0.6"/>
    <ellipse cx="0" cy="75" rx="30" ry="5" fill="#8D6E63" opacity="0.3"/>
  </g>
  <!-- Cone closeup -->
  <g transform="translate(320,130)">
    <ellipse cx="0" cy="0" rx="18" ry="35" fill="#8D6E63" stroke="#5D4037" stroke-width="2"/>
    <!-- Scales -->
    <path d="M-15 -20 Q0 -25 15 -20" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <path d="M-17 -10 Q0 -15 17 -10" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <path d="M-18 0 Q0 -5 18 0" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <path d="M-17 10 Q0 5 17 10" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <path d="M-15 20 Q0 15 15 20" stroke="#5D4037" stroke-width="1.5" fill="none"/>
    <!-- Seeds visible under scale -->
    <ellipse cx="-5" cy="-5" rx="3" ry="5" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
    <ellipse cx="5" cy="5" rx="3" ry="5" fill="#FFCC80" stroke="#E65100" stroke-width="0.8"/>
    <!-- Wing -->
    <path d="M-8 -5 Q-18 -15 -12 -20" fill="#FFE0B2" stroke="#E65100" stroke-width="0.5" opacity="0.7"/>
    <text x="0" y="48" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Шишка с семенами</text>
  </g>
  <!-- Needle closeup -->
  <g transform="translate(430,120)">
    <path d="M0 30 L0 -20" stroke="#2E7D32" stroke-width="3" stroke-linecap="round"/>
    <path d="M8 30 L8 -20" stroke="#388E3C" stroke-width="3" stroke-linecap="round"/>
    <text x="4" y="45" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Хвоинки</text>
  </g>
  <!-- Features -->
  <rect x="280" y="220" width="195" height="85" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="377" y="237" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Особенности</text>
  <text x="290" y="253" font-family="Arial,sans-serif" font-size="7" fill="#555">- Семена (не споры!)</text>
  <text x="290" y="265" font-family="Arial,sans-serif" font-size="7" fill="#555">- Нет плодов (семена открыты)</text>
  <text x="290" y="277" font-family="Arial,sans-serif" font-size="7" fill="#555">- Листья - хвоя (иголки)</text>
  <text x="290" y="289" font-family="Arial,sans-serif" font-size="7" fill="#555">- Вечнозелёные (большинство)</text>
  <text x="290" y="301" font-family="Arial,sans-serif" font-size="7" fill="#555">- Смола защищает от вредителей</text>
  <text x="80" y="280" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Сосна</text>
''', "Общая характеристика голосеменных", "Биология 6 класс - Урок 17")

# 18: Разнообразие и значение голосеменных
l18 = W('''
  <!-- 4 types -->
  <g transform="translate(80,160)">
    <rect x="-4" y="15" width="8" height="45" fill="#795548" rx="2"/>
    <path d="M0 -30 L-30 15 L30 15 Z" fill="#2E7D32" opacity="0.8"/>
    <text x="0" y="75" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Сосна</text>
  </g>
  <g transform="translate(190,155)">
    <rect x="-4" y="20" width="8" height="40" fill="#795548" rx="2"/>
    <path d="M0 -25 L-25 20 L25 20 Z" fill="#1B5E20" opacity="0.7"/>
    <path d="M0 -15 L-18 25 L18 25 Z" fill="#2E7D32" opacity="0.6"/>
    <text x="0" y="75" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Ель</text>
  </g>
  <g transform="translate(300,160)">
    <rect x="-5" y="15" width="10" height="40" fill="#795548" rx="2"/>
    <!-- Larch branches -->
    <path d="M-5 5 L-30 -10" stroke="#795548" stroke-width="2" fill="none"/>
    <path d="M5 5 L30 -10" stroke="#795548" stroke-width="2" fill="none"/>
    <path d="M-5 20 L-25 10" stroke="#795548" stroke-width="2" fill="none"/>
    <path d="M5 20 L25 10" stroke="#795548" stroke-width="2" fill="none"/>
    <!-- Soft needles in clusters -->
    <circle cx="-30" cy="-12" r="8" fill="#81C784" opacity="0.6"/>
    <circle cx="30" cy="-12" r="8" fill="#81C784" opacity="0.6"/>
    <circle cx="-25" cy="8" r="7" fill="#81C784" opacity="0.5"/>
    <circle cx="25" cy="8" r="7" fill="#81C784" opacity="0.5"/>
    <text x="0" y="68" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Лиственница</text>
    <text x="0" y="79" font-family="Arial,sans-serif" font-size="6" fill="#FF9800" text-anchor="middle">(листопадная!)</text>
  </g>
  <g transform="translate(420,160)">
    <rect x="-3" y="10" width="6" height="35" fill="#795548" rx="2"/>
    <!-- Juniper bush -->
    <ellipse cx="0" cy="0" rx="20" ry="18" fill="#2E7D32" opacity="0.6"/>
    <ellipse cx="-8" cy="-5" rx="12" ry="10" fill="#388E3C" opacity="0.5"/>
    <!-- Berries -->
    <circle cx="-5" cy="5" r="3" fill="#1A237E" opacity="0.7"/>
    <circle cx="5" cy="3" r="3" fill="#1A237E" opacity="0.7"/>
    <circle cx="0" cy="8" r="2.5" fill="#283593" opacity="0.6"/>
    <text x="0" y="58" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Можжевельник</text>
  </g>
  <!-- Uses -->
  <rect x="30" y="250" width="440" height="60" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="268" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Значение голосеменных</text>
  <text x="250" y="284" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Древесина (строительство, мебель), смола (канифоль, скипидар)</text>
  <text x="250" y="298" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Кедровые орехи (пища), фитонциды (оздоровление воздуха), декоративные</text>
''', "Разнообразие и значение голосеменных", "Биология 6 класс - Урок 18")

# 19: Общая характеристика покрытосеменных
l19 = W('''
  <!-- Flowering plant -->
  <g transform="translate(130,175)">
    <rect x="-3" y="15" width="6" height="55" fill="#795548" rx="2"/>
    <!-- Leaves -->
    <ellipse cx="-15" cy="35" rx="15" ry="7" fill="#81C784" stroke="#4CAF50" stroke-width="1" transform="rotate(25,-15,35)"/>
    <ellipse cx="15" cy="45" rx="15" ry="7" fill="#81C784" stroke="#4CAF50" stroke-width="1" transform="rotate(-25,15,45)"/>
    <!-- Flower -->
    <g transform="translate(0,-10)">
      <!-- Petals -->
      <ellipse cx="0" cy="-14" rx="7" ry="14" fill="#E91E63" opacity="0.7"/>
      <ellipse cx="13" cy="-5" rx="7" ry="14" fill="#E91E63" opacity="0.7" transform="rotate(72,0,0)"/>
      <ellipse cx="8" cy="12" rx="7" ry="14" fill="#E91E63" opacity="0.7" transform="rotate(144,0,0)"/>
      <ellipse cx="-8" cy="12" rx="7" ry="14" fill="#E91E63" opacity="0.7" transform="rotate(216,0,0)"/>
      <ellipse cx="-13" cy="-5" rx="7" ry="14" fill="#E91E63" opacity="0.7" transform="rotate(288,0,0)"/>
      <!-- Center -->
      <circle cx="0" cy="0" r="7" fill="#FFC107" stroke="#FF9800" stroke-width="1"/>
      <!-- Stamens -->
      <line x1="0" y1="-3" x2="0" y2="-7" stroke="#FF9800" stroke-width="0.8"/>
      <line x1="3" y1="-1" x2="5" y2="-5" stroke="#FF9800" stroke-width="0.8"/>
      <line x1="-3" y1="-1" x2="-5" y2="-5" stroke="#FF9800" stroke-width="0.8"/>
    </g>
    <!-- Roots -->
    <path d="M0 70 Q-12 82 -15 90" stroke="#795548" stroke-width="2" fill="none"/>
    <path d="M0 70 Q12 82 15 90" stroke="#795548" stroke-width="2" fill="none"/>
    <path d="M0 70 Q0 85 0 92" stroke="#795548" stroke-width="1.5" fill="none"/>
  </g>
  <!-- Comparison with gymnosperm -->
  <g transform="translate(340,120)">
    <rect x="-90" y="-30" width="180" height="180" rx="6" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
    <text x="0" y="-12" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Покрытосеменные vs Голосеменные</text>
    <line x1="-85" y1="-2" x2="85" y2="-2" stroke="#ddd" stroke-width="1"/>
    <text x="-80" y="15" font-family="Arial,sans-serif" font-size="7" fill="#333">Семена в плоду</text>
    <text x="60" y="15" font-family="Arial,sans-serif" font-size="7" fill="#999">Семена открыты</text>
    <text x="-80" y="32" font-family="Arial,sans-serif" font-size="7" fill="#333">Есть цветок</text>
    <text x="60" y="32" font-family="Arial,sans-serif" font-size="7" fill="#999">Нет цветка</text>
    <text x="-80" y="49" font-family="Arial,sans-serif" font-size="7" fill="#333">Листья разные</text>
    <text x="60" y="49" font-family="Arial,sans-serif" font-size="7" fill="#999">Только хвоя</text>
    <text x="-80" y="66" font-family="Arial,sans-serif" font-size="7" fill="#333">Двойное оплодот.</text>
    <text x="60" y="66" font-family="Arial,sans-serif" font-size="7" fill="#999">Нет двойного</text>
    <text x="-80" y="83" font-family="Arial,sans-serif" font-size="7" fill="#333">350 000 видов</text>
    <text x="60" y="83" font-family="Arial,sans-serif" font-size="7" fill="#999">700 видов</text>
    <rect x="-50" y="95" width="100" height="22" rx="4" fill="#2E7D32" opacity="0.15"/>
    <text x="0" y="110" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Самый процветающий!</text>
    <text x="0" y="135" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Органы: корень, побег,</text>
    <text x="0" y="147" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">цветок, плод, семя</text>
  </g>
''', "Общая характеристика покрытосеменных", "Биология 6 класс - Урок 19")

# 20: Классы покрытосеменных: Двудольные и Однодольные
l20 = W('''
  <!-- Two columns -->
  <rect x="20" y="58" width="225" height="255" rx="8" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
  <text x="132" y="78" font-family="Arial,sans-serif" font-size="12" fill="#1565C0" text-anchor="middle" font-weight="bold">Двудольные</text>
  <!-- Seed with 2 cotyledons -->
  <g transform="translate(80,115)">
    <ellipse cx="0" cy="0" rx="22" ry="15" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/>
    <line x1="0" y1="-13" x2="0" y2="13" stroke="#F9A825" stroke-width="1"/>
    <text x="-8" y="4" font-family="Arial,sans-serif" font-size="7" fill="#F57F17">1</text>
    <text x="6" y="4" font-family="Arial,sans-serif" font-size="7" fill="#F57F17">2</text>
    <text x="0" y="28" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">2 семядоли</text>
  </g>
  <!-- Leaf with net venation -->
  <g transform="translate(185,115)">
    <ellipse cx="0" cy="0" rx="18" ry="25" fill="#81C784" stroke="#4CAF50" stroke-width="1.5"/>
    <line x1="0" y1="25" x2="0" y2="-20" stroke="#388E3C" stroke-width="1"/>
    <line x1="0" y1="-5" x2="-12" y2="-15" stroke="#388E3C" stroke-width="0.5"/>
    <line x1="0" y1="5" x2="12" y2="-5" stroke="#388E3C" stroke-width="0.5"/>
    <line x1="0" y1="-10" x2="10" y2="-18" stroke="#388E3C" stroke-width="0.5"/>
    <line x1="0" y1="0" x2="-14" y2="-5" stroke="#388E3C" stroke-width="0.5"/>
    <text x="0" y="38" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Сетчатое жилкование</text>
  </g>
  <!-- Features -->
  <text x="50" y="165" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">- 2 семядоли в семени</text>
  <text x="50" y="177" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">- Сетчатое жилкование</text>
  <text x="50" y="189" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">- 4-5 члеников в цветке</text>
  <text x="50" y="201" font-family="Arial,sans-serif" font-size="7" fill="#1565C0">- Стержневая корневая</text>
  <!-- Examples -->
  <text x="132" y="222" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Примеры:</text>
  <text x="132" y="234" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Роза, дуб, горох, морковь</text>
  <text x="132" y="246" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">картофель, подсолнечник</text>
  <!-- Right column: Monocots -->
  <rect x="255" y="58" width="225" height="255" rx="8" fill="#FFF3E0" stroke="#E65100" stroke-width="1.5"/>
  <text x="367" y="78" font-family="Arial,sans-serif" font-size="12" fill="#E65100" text-anchor="middle" font-weight="bold">Однодольные</text>
  <!-- Seed with 1 cotyledon -->
  <g transform="translate(315,115)">
    <ellipse cx="0" cy="0" rx="22" ry="15" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/>
    <ellipse cx="5" cy="0" rx="12" ry="10" fill="#FFE082" opacity="0.5"/>
    <text x="5" y="4" font-family="Arial,sans-serif" font-size="7" fill="#F57F17">1</text>
    <text x="0" y="28" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">1 семядоля</text>
  </g>
  <!-- Leaf with parallel venation -->
  <g transform="translate(420,115)">
    <ellipse cx="0" cy="0" rx="10" ry="25" fill="#81C784" stroke="#4CAF50" stroke-width="1.5"/>
    <line x1="-5" y1="22" x2="-5" y2="-20" stroke="#388E3C" stroke-width="0.5"/>
    <line x1="0" y1="25" x2="0" y2="-22" stroke="#388E3C" stroke-width="1"/>
    <line x1="5" y1="22" x2="5" y2="-20" stroke="#388E3C" stroke-width="0.5"/>
    <text x="0" y="38" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Параллельное</text>
  </g>
  <text x="285" y="165" font-family="Arial,sans-serif" font-size="7" fill="#E65100">- 1 семядоля в семени</text>
  <text x="285" y="177" font-family="Arial,sans-serif" font-size="7" fill="#E65100">- Параллельное жилкование</text>
  <text x="285" y="189" font-family="Arial,sans-serif" font-size="7" fill="#E65100">- 3 членика в цветке</text>
  <text x="285" y="201" font-family="Arial,sans-serif" font-size="7" fill="#E65100">- Мочковатая корневая</text>
  <text x="367" y="222" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Примеры:</text>
  <text x="367" y="234" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Пшеница, рис, лук, лилия</text>
  <text x="367" y="246" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">кукуруза, тюльпан</text>
''', "Классы покрытосеменных: Двудольные и Однодольные", "Биология 6 класс - Урок 20")

# 21: Разнообразие и значение цветковых растений
l21 = W('''
  <!-- Plant families -->
  <g transform="translate(80,110)">
    <!-- Rose family flower -->
    <g transform="translate(0,0)">
      <ellipse cx="0" cy="-10" rx="6" ry="12" fill="#F48FB1" opacity="0.7"/>
      <ellipse cx="10" cy="-3" rx="6" ry="12" fill="#F48FB1" opacity="0.7" transform="rotate(72,0,0)"/>
      <ellipse cx="6" cy="8" rx="6" ry="12" fill="#F48FB1" opacity="0.7" transform="rotate(144,0,0)"/>
      <ellipse cx="-6" cy="8" rx="6" ry="12" fill="#F48FB1" opacity="0.7" transform="rotate(216,0,0)"/>
      <ellipse cx="-10" cy="-3" rx="6" ry="12" fill="#F48FB1" opacity="0.7" transform="rotate(288,0,0)"/>
      <circle cx="0" cy="0" r="5" fill="#FFC107"/>
      <text x="0" y="25" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Розоцветные</text>
      <text x="0" y="36" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">яблоня, роза</text>
    </g>
  </g>
  <g transform="translate(200,110)">
    <!-- Legume flower -->
    <path d="M-5 -15 Q0 -20 5 -15 L8 -5 Q5 5 -5 5 L-8 -5 Z" fill="#CE93D8" stroke="#8E24AA" stroke-width="1"/>
    <path d="M-3 -8 Q0 -12 3 -8" fill="#AB47BC" stroke="#8E24AA" stroke-width="0.5"/>
    <text x="0" y="20" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Бобовые</text>
    <text x="0" y="31" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">горох, фасоль</text>
  </g>
  <g transform="translate(310,110)">
    <!-- Aster family - sunflower -->
    <circle cx="0" cy="0" r="10" fill="#795548"/>
    <ellipse cx="-10" cy="-8" rx="8" ry="4" fill="#FFC107" transform="rotate(-30,-10,-8)"/>
    <ellipse cx="10" cy="-8" rx="8" ry="4" fill="#FFC107" transform="rotate(30,10,-8)"/>
    <ellipse cx="-12" cy="3" rx="8" ry="4" fill="#FFC107" transform="rotate(-50,-12,3)"/>
    <ellipse cx="12" cy="3" rx="8" ry="4" fill="#FFC107" transform="rotate(50,12,3)"/>
    <ellipse cx="0" cy="-14" rx="8" ry="4" fill="#FFC107"/>
    <ellipse cx="0" cy="14" rx="8" ry="4" fill="#FFC107"/>
    <text x="0" y="28" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Сложноцветные</text>
    <text x="0" y="39" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">подсолнечник, астра</text>
  </g>
  <g transform="translate(430,110)">
    <!-- Grass family -->
    <path d="M0 15 L0 -10" stroke="#66BB6A" stroke-width="2"/>
    <path d="M0 -10 Q-8 -18 -5 -25" stroke="#81C784" stroke-width="1.5" fill="none"/>
    <path d="M0 -10 Q8 -18 5 -25" stroke="#81C784" stroke-width="1.5" fill="none"/>
    <path d="M0 -5 Q-10 -12 -10 -18" stroke="#81C784" stroke-width="1" fill="#81C784" opacity="0.5"/>
    <text x="0" y="28" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Злаки</text>
    <text x="0" y="39" font-family="Arial,sans-serif" font-size="6" fill="#666" text-anchor="middle">пшеница, рис</text>
  </g>
  <!-- Importance -->
  <rect x="30" y="185" width="440" height="120" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="203" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Значение цветковых растений</text>
  <text x="50" y="220" font-family="Arial,sans-serif" font-size="8" fill="#555">Пища: злаки (хлеб), овощи, фрукты, бобовые (белки)</text>
  <text x="50" y="235" font-family="Arial,sans-serif" font-size="8" fill="#555">Лекарства: ромашка, валериана, шиповник</text>
  <text x="50" y="250" font-family="Arial,sans-serif" font-size="8" fill="#555">Декоративные: розы, тюльпаны, хризантемы</text>
  <text x="50" y="265" font-family="Arial,sans-serif" font-size="8" fill="#555">Технические: лён (ткани), хлопок, каучук (гевея)</text>
  <text x="50" y="280" font-family="Arial,sans-serif" font-size="8" fill="#555">Кормовые: клевер, люцерна, кукуруза</text>
  <text x="50" y="298" font-family="Arial,sans-serif" font-size="7" fill="#C62828">Цветковые = основа жизни человека на Земле</text>
''', "Разнообразие и значение цветковых растений", "Биология 6 класс - Урок 21")

# 22: Корень. Виды корней и корневые системы
l22 = W('''
  <!-- Two root systems -->
  <!-- Taproot system -->
  <g transform="translate(130,180)">
    <!-- Plant top -->
    <rect x="-3" y="-25" width="6" height="25" fill="#795548" rx="2"/>
    <ellipse cx="-10" cy="-20" rx="10" ry="6" fill="#81C784" transform="rotate(30,-10,-20)"/>
    <ellipse cx="10" cy="-20" rx="10" ry="6" fill="#81C784" transform="rotate(-30,10,-20)"/>
    <!-- Main root -->
    <path d="M0 0 L0 90" stroke="#795548" stroke-width="5" stroke-linecap="round"/>
    <!-- Lateral roots -->
    <path d="M0 20 Q-20 30 -30 40" stroke="#8D6E63" stroke-width="2.5" fill="none"/>
    <path d="M0 20 Q20 30 30 40" stroke="#8D6E63" stroke-width="2.5" fill="none"/>
    <path d="M0 40 Q-18 48 -25 55" stroke="#8D6E63" stroke-width="2" fill="none"/>
    <path d="M0 40 Q18 48 25 55" stroke="#8D6E63" stroke-width="2" fill="none"/>
    <path d="M0 60 Q-12 65 -18 72" stroke="#8D6E63" stroke-width="1.5" fill="none"/>
    <path d="M0 60 Q12 65 18 72" stroke="#8D6E63" stroke-width="1.5" fill="none"/>
    <!-- Root hairs -->
    <line x1="-3" y1="75" x2="-8" y2="73" stroke="#A1887F" stroke-width="0.5"/>
    <line x1="-2" y1="80" x2="-7" y2="78" stroke="#A1887F" stroke-width="0.5"/>
    <line x1="3" y1="70" x2="8" y2="68" stroke="#A1887F" stroke-width="0.5"/>
    <!-- Root cap -->
    <path d="M-3 88 Q0 98 3 88" fill="#BCAAA4" stroke="#8D6E63" stroke-width="1"/>
    <text x="0" y="112" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" text-anchor="middle" font-weight="bold">Стержневая</text>
    <text x="0" y="124" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(двудольные)</text>
  </g>
  <!-- Fibrous root system -->
  <g transform="translate(370,180)">
    <rect x="-3" y="-25" width="6" height="25" fill="#795548" rx="2"/>
    <ellipse cx="-10" cy="-20" rx="10" ry="6" fill="#81C784" transform="rotate(30,-10,-20)"/>
    <ellipse cx="10" cy="-20" rx="10" ry="6" fill="#81C784" transform="rotate(-30,10,-20)"/>
    <!-- Many equal roots -->
    <path d="M0 0 Q-15 30 -20 70" stroke="#795548" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M0 0 Q-8 35 -12 75" stroke="#795548" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M0 0 Q0 40 0 80" stroke="#795548" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M0 0 Q8 35 12 75" stroke="#795548" stroke-width="3" fill="none" stroke-linecap="round"/>
    <path d="M0 0 Q15 30 20 70" stroke="#795548" stroke-width="3" fill="none" stroke-linecap="round"/>
    <!-- Secondary -->
    <path d="M-15 35 Q-25 42 -30 50" stroke="#8D6E63" stroke-width="1.5" fill="none"/>
    <path d="M12 40 Q20 48 25 55" stroke="#8D6E63" stroke-width="1.5" fill="none"/>
    <text x="0" y="112" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">Мочковатая</text>
    <text x="0" y="124" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">(однодольные)</text>
  </g>
  <!-- Root zones -->
  <rect x="210" y="80" width="180" height="70" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="300" y="96" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Зоны корня (сверху вниз)</text>
  <text x="220" y="112" font-family="Arial,sans-serif" font-size="7" fill="#555">1. Зона деления (рост)</text>
  <text x="220" y="124" font-family="Arial,sans-serif" font-size="7" fill="#555">2. Зона растяжения</text>
  <text x="220" y="136" font-family="Arial,sans-serif" font-size="7" fill="#555">3. Зона всасывания (корневые волоски)</text>
  <text x="220" y="148" font-family="Arial,sans-serif" font-size="7" fill="#555">4. Зона проведения</text>
''', "Корень. Виды корней и корневые системы", "Биология 6 класс - Урок 22")

# 23: Побег и стебель
l23 = W('''
  <!-- Plant shoot diagram -->
  <g transform="translate(150,185)">
    <!-- Main stem -->
    <rect x="-4" y="-70" width="8" height="120" fill="#795548" rx="2"/>
    <!-- Nodes -->
    <line x1="-20" y1="-50" x2="20" y2="-50" stroke="#5D4037" stroke-width="1" stroke-dasharray="3,2"/>
    <line x1="-20" y1="-20" x2="20" y2="-20" stroke="#5D4037" stroke-width="1" stroke-dasharray="3,2"/>
    <line x1="-20" y1="10" x2="20" y2="10" stroke="#5D4037" stroke-width="1" stroke-dasharray="3,2"/>
    <!-- Internodes labels -->
    <text x="30" y="-35" font-family="Arial,sans-serif" font-size="7" fill="#555">Междоузлие</text>
    <line x1="28" y1="-33" x2="15" y2="-35" stroke="#555" stroke-width="0.5"/>
    <text x="30" y="-5" font-family="Arial,sans-serif" font-size="7" fill="#555">Междоузлие</text>
    <line x1="28" y1="-3" x2="15" y2="-5" stroke="#555" stroke-width="0.5"/>
    <!-- Node label -->
    <text x="-55" y="-47" font-family="Arial,sans-serif" font-size="7" fill="#555">Узел</text>
    <line x1="-42" y1="-48" x2="-22" y2="-50" stroke="#555" stroke-width="0.5"/>
    <!-- Leaves at nodes -->
    <ellipse cx="-22" cy="-55" rx="18" ry="7" fill="#81C784" stroke="#4CAF50" stroke-width="1" transform="rotate(30,-22,-55)"/>
    <ellipse cx="22" cy="-55" rx="18" ry="7" fill="#81C784" stroke="#4CAF50" stroke-width="1" transform="rotate(-30,22,-55)"/>
    <ellipse cx="-22" cy="-25" rx="18" ry="7" fill="#81C784" stroke="#4CAF50" stroke-width="1" transform="rotate(30,-22,-25)"/>
    <ellipse cx="22" cy="-25" rx="18" ry="7" fill="#81C784" stroke="#4CAF50" stroke-width="1" transform="rotate(-30,22,-25)"/>
    <ellipse cx="-22" cy="5" rx="18" ry="7" fill="#81C784" stroke="#4CAF50" stroke-width="1" transform="rotate(30,-22,5)"/>
    <ellipse cx="22" cy="5" rx="18" ry="7" fill="#81C784" stroke="#4CAF50" stroke-width="1" transform="rotate(-30,22,5)"/>
    <!-- Terminal bud -->
    <ellipse cx="0" cy="-78" rx="6" ry="10" fill="#A5D6A7" stroke="#4CAF50" stroke-width="1.5"/>
    <text x="0" y="-90" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Почка</text>
    <!-- Axillary buds -->
    <circle cx="-25" cy="-45" r="4" fill="#C8E6C9" stroke="#4CAF50" stroke-width="0.8"/>
    <circle cx="25" cy="-45" r="4" fill="#C8E6C9" stroke="#4CAF50" stroke-width="0.8"/>
  </g>
  <!-- Stem cross-section -->
  <g transform="translate(380,155)">
    <circle cx="0" cy="0" r="55" fill="#FFF3E0" stroke="#795548" stroke-width="2"/>
    <!-- Bark -->
    <circle cx="0" cy="0" r="52" fill="none" stroke="#5D4037" stroke-width="4"/>
    <!-- Phloem -->
    <circle cx="0" cy="0" r="42" fill="none" stroke="#A1887F" stroke-width="3"/>
    <!-- Cambium -->
    <circle cx="0" cy="0" r="37" fill="none" stroke="#81C784" stroke-width="1.5" stroke-dasharray="3,2"/>
    <!-- Xylem (wood) -->
    <circle cx="0" cy="0" r="30" fill="#D7CCC8" stroke="#8D6E63" stroke-width="1.5"/>
    <!-- Annual rings -->
    <circle cx="0" cy="0" r="25" fill="none" stroke="#A1887F" stroke-width="0.8"/>
    <circle cx="0" cy="0" r="20" fill="none" stroke="#A1887F" stroke-width="0.8"/>
    <circle cx="0" cy="0" r="15" fill="none" stroke="#A1887F" stroke-width="0.8"/>
    <!-- Pith -->
    <circle cx="0" cy="0" r="8" fill="#FFF9C4" stroke="#F9A825" stroke-width="0.5"/>
  </g>
  <!-- Stem labels -->
  <text x="445" y="110" font-family="Arial,sans-serif" font-size="7" fill="#5D4037">Пробка</text>
  <text x="440" y="130" font-family="Arial,sans-serif" font-size="7" fill="#A1887F">Луб (флоэма)</text>
  <text x="440" y="148" font-family="Arial,sans-serif" font-size="7" fill="#4CAF50">Камбий</text>
  <text x="440" y="168" font-family="Arial,sans-serif" font-size="7" fill="#8D6E63">Древесина (ксилема)</text>
  <text x="440" y="188" font-family="Arial,sans-serif" font-size="7" fill="#F9A825">Сердцевина</text>
  <!-- Bottom -->
  <rect x="40" y="280" width="420" height="30" rx="4" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
  <text x="250" y="299" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Побег = стебель + листья + почки | Стебель: луб (вниз) и древесина (вверх) - проводящие ткани</text>
''', "Побег и стебель", "Биология 6 класс - Урок 23")

# 24: Лист. Внешнее и внутреннее строение
l24 = W('''
  <!-- External leaf structure -->
  <g transform="translate(140,160)">
    <!-- Leaf blade -->
    <path d="M0 -55 Q-35 -30 -40 0 Q-35 30 0 55 Q35 30 40 0 Q35 -30 0 -55 Z" fill="#81C784" stroke="#4CAF50" stroke-width="2"/>
    <!-- Main vein (midrib) -->
    <line x1="0" y1="-55" x2="0" y2="55" stroke="#388E3C" stroke-width="2"/>
    <!-- Side veins -->
    <path d="M0 -35 Q-20 -30 -30 -15" stroke="#388E3C" stroke-width="1" fill="none"/>
    <path d="M0 -35 Q20 -30 30 -15" stroke="#388E3C" stroke-width="1" fill="none"/>
    <path d="M0 -15 Q-25 -5 -35 10" stroke="#388E3C" stroke-width="1" fill="none"/>
    <path d="M0 -15 Q25 -5 35 10" stroke="#388E3C" stroke-width="1" fill="none"/>
    <path d="M0 10 Q-20 20 -30 30" stroke="#388E3C" stroke-width="1" fill="none"/>
    <path d="M0 10 Q20 20 30 30" stroke="#388E3C" stroke-width="1" fill="none"/>
    <!-- Petiole -->
    <rect x="-3" y="55" width="6" height="25" fill="#795548" rx="2"/>
    <!-- Stipules -->
    <path d="M-3 60 Q-12 55 -10 65" stroke="#4CAF50" stroke-width="1" fill="#81C784" opacity="0.5"/>
    <path d="M3 60 Q12 55 10 65" stroke="#4CAF50" stroke-width="1" fill="#81C784" opacity="0.5"/>
  </g>
  <!-- Labels for external -->
  <text x="140" y="255" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">Листовая пластинка</text>
  <text x="140" y="268" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">с сетчатым жилкованием</text>
  <!-- Internal structure (cross-section) -->
  <g transform="translate(380,165)">
    <rect x="-80" y="-70" width="160" height="140" fill="#C8E6C9" stroke="#4CAF50" stroke-width="1.5" rx="3"/>
    <!-- Upper epidermis -->
    <rect x="-75" y="-65" width="150" height="10" fill="#A5D6A7" stroke="#66BB6A" stroke-width="1"/>
    <text x="82" y="-58" font-family="Arial,sans-serif" font-size="6" fill="#333">Верх. эпидерма</text>
    <!-- Palisade mesophyll -->
    <g transform="translate(0,-42)">
      <rect x="-70" y="-8" width="140" height="18" fill="#81C784" stroke="#4CAF50" stroke-width="0.5"/>
      <!-- Columnar cells -->
      <rect x="-65" y="-6" width="5" height="14" fill="#66BB6A" rx="1"/>
      <rect x="-55" y="-6" width="5" height="14" fill="#66BB6A" rx="1"/>
      <rect x="-45" y="-6" width="5" height="14" fill="#66BB6A" rx="1"/>
      <rect x="-35" y="-6" width="5" height="14" fill="#66BB6A" rx="1"/>
      <rect x="-25" y="-6" width="5" height="14" fill="#66BB6A" rx="1"/>
      <rect x="-15" y="-6" width="5" height="14" fill="#66BB6A" rx="1"/>
      <rect x="-5" y="-6" width="5" height="14" fill="#66BB6A" rx="1"/>
      <rect x="5" y="-6" width="5" height="14" fill="#66BB6A" rx="1"/>
      <rect x="15" y="-6" width="5" height="14" fill="#66BB6A" rx="1"/>
      <rect x="25" y="-6" width="5" height="14" fill="#66BB6A" rx="1"/>
      <rect x="35" y="-6" width="5" height="14" fill="#66BB6A" rx="1"/>
      <rect x="45" y="-6" width="5" height="14" fill="#66BB6A" rx="1"/>
      <rect x="55" y="-6" width="5" height="14" fill="#66BB6A" rx="1"/>
      <rect x="65" y="-6" width="5" height="14" fill="#66BB6A" rx="1"/>
    </g>
    <text x="82" y="-40" font-family="Arial,sans-serif" font-size="6" fill="#333">Столбч. ткань</text>
    <!-- Spongy mesophyll -->
    <rect x="-70" y="-22" width="140" height="22" fill="#C8E6C9" stroke="#81C784" stroke-width="0.5"/>
    <!-- Irregular cells with spaces -->
    <ellipse cx="-50" cy="-12" rx="6" ry="4" fill="#A5D6A7"/>
    <ellipse cx="-35" cy="-8" rx="5" ry="4" fill="#A5D6A7"/>
    <ellipse cx="-20" cy="-14" rx="6" ry="3" fill="#A5D6A7"/>
    <ellipse cx="-5" cy="-9" rx="5" ry="4" fill="#A5D6A7"/>
    <ellipse cx="10" cy="-13" rx="6" ry="3" fill="#A5D6A7"/>
    <ellipse cx="25" cy="-8" rx="5" ry="4" fill="#A5D6A7"/>
    <ellipse cx="40" cy="-12" rx="6" ry="3" fill="#A5D6A7"/>
    <ellipse cx="55" cy="-9" rx="5" ry="4" fill="#A5D6A7"/>
    <text x="82" y="-8" font-family="Arial,sans-serif" font-size="6" fill="#333">Губч. ткань</text>
    <!-- Lower epidermis with stomata -->
    <rect x="-75" y="2" width="150" height="10" fill="#A5D6A7" stroke="#66BB6A" stroke-width="1"/>
    <!-- Stomata -->
    <ellipse cx="-30" cy="7" rx="8" ry="4" fill="#81C784" stroke="#388E3C" stroke-width="1"/>
    <ellipse cx="-30" cy="7" rx="3" ry="4" fill="#E8F5E9"/>
    <ellipse cx="20" cy="7" rx="8" ry="4" fill="#81C784" stroke="#388E3C" stroke-width="1"/>
    <ellipse cx="20" cy="7" rx="3" ry="4" fill="#E8F5E9"/>
    <text x="82" y="10" font-family="Arial,sans-serif" font-size="6" fill="#333">Ниж. эпидерма</text>
    <!-- Vein in cross-section -->
    <ellipse cx="0" cy="-10" rx="6" ry="25" fill="#FFF3E0" stroke="#F9A825" stroke-width="1"/>
    <circle cx="-2" cy="-10" r="2" fill="#E53935" opacity="0.5"/>
    <circle cx="2" cy="-10" r="2" fill="#42A5F5" opacity="0.5"/>
  </g>
  <!-- Stomata detail -->
  <g transform="translate(330,275)">
    <text x="0" y="-10" font-family="Arial,sans-serif" font-size="7" fill="#333" font-weight="bold">Устьице:</text>
    <ellipse cx="25" cy="-12" rx="10" ry="5" fill="#81C784" stroke="#388E3C" stroke-width="1"/>
    <ellipse cx="25" cy="-12" rx="4" ry="5" fill="#E8F5E9"/>
    <text x="45" y="-9" font-family="Arial,sans-serif" font-size="6" fill="#555">замыкающие клетки</text>
  </g>
''', "Лист. Внешнее и внутреннее строение", "Биология 6 класс - Урок 24")

lessons = [
    (17, "Общая характеристика голосеменных", l17),
    (18, "Разнообразие и значение голосеменных", l18),
    (19, "Общая характеристика покрытосеменных", l19),
    (20, "Классы покрытосеменных: Двудольные и Однодольные", l20),
    (21, "Разнообразие и значение цветковых растений", l21),
    (22, "Корень. Виды корней и корневые системы", l22),
    (23, "Побег и стебель", l23),
    (24, "Лист. Внешнее и внутреннее строение", l24),
]

for num, title, svg in lessons:
    with open(os.path.join(D, f"lesson{num}.svg"), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"lesson{num}.svg")

print("Done! 8 SVGs for Grade 6 Lessons 17-24.")
