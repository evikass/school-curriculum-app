#!/usr/bin/env python3
"""Generate SVG lesson images for grade 11 biology (lessons 11-30)"""

SVG_TEMPLATE = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#E8F5E9"/>
      <stop offset="100%" stop-color="#FFFFFF"/>
    </linearGradient>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#4CAF50"/>
      <stop offset="100%" stop-color="#2E7D32"/>
    </linearGradient>
  </defs>
  <rect width="500" height="350" rx="16" fill="url(#bg)" stroke="#C8E6C9" stroke-width="2"/>
  <circle cx="420" cy="60" r="45" fill="#E8F5E9" opacity="0.6"/>
  <circle cx="60" cy="290" r="35" fill="#E8F5E9" opacity="0.4"/>
  {icon}
  <text x="250" y="280" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" fill="#2E7D32" font-weight="bold">{title}</text>
  <text x="250" y="305" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#66BB6A">Биология · 11 класс</text>
</svg>'''

# Icons for each lesson (simple SVG shapes)
icons = {
    11: '<path d="M200 80 L250 40 L300 80 L280 80 L280 160 L220 160 L220 80 Z" fill="#8D6E63" opacity="0.7"/><circle cx="250" cy="130" r="25" fill="#A5D6A7"/><circle cx="250" cy="130" r="15" fill="#66BB6A"/><path d="M240 100 Q250 70 260 100" stroke="#4CAF50" fill="none" stroke-width="2"/>',
    12: '<ellipse cx="250" cy="100" rx="50" ry="25" fill="#A5D6A7"/><rect x="230" y="100" width="40" height="60" rx="5" fill="#81C784"/><path d="M200 160 Q250 200 300 160" stroke="#4CAF50" fill="none" stroke-width="3"/><circle cx="250" cy="80" r="8" fill="#FFD54F"/>',
    13: '<circle cx="250" cy="110" r="40" fill="#A5D6A7"/><circle cx="250" cy="110" r="25" fill="#81C784"/><path d="M240 80 L250 50 L260 80" stroke="#4CAF50" fill="none" stroke-width="2"/><rect x="225" y="150" width="50" height="40" rx="5" fill="#8D6E63" opacity="0.5"/>',
    14: '<circle cx="250" cy="90" r="30" fill="#FFCCBC"/><circle cx="240" cy="85" r="3" fill="#5D4037"/><circle cx="260" cy="85" r="3" fill="#5D4037"/><path d="M243 95 Q250 100 257 95" stroke="#5D4037" fill="none" stroke-width="1.5"/><path d="M220 90 Q210 70 225 65" stroke="#5D4037" fill="none" stroke-width="1"/><path d="M280 90 Q290 70 275 65" stroke="#5D4037" fill="none" stroke-width="1"/>',
    15: '<circle cx="250" cy="90" r="35" fill="#FFE082"/><path d="M250 55 L250 45" stroke="#FF8F00" stroke-width="3"/><path d="M225 60 L215 50" stroke="#FF8F00" stroke-width="2"/><path d="M275 60 L285 50" stroke="#FF8F00" stroke-width="2"/><path d="M220 90 L200 90" stroke="#4CAF50" stroke-width="2"/><path d="M280 90 L300 90" stroke="#4CAF50" stroke-width="2"/><path d="M250 125 L250 145" stroke="#4CAF50" stroke-width="2"/>',
    16: '<path d="M200 150 Q200 80 250 80 Q300 80 300 150" fill="#81C784"/><path d="M210 150 Q210 95 250 95 Q290 95 290 150" fill="#A5D6A7"/><circle cx="235" cy="120" r="4" fill="#2E7D32"/><circle cx="265" cy="110" r="4" fill="#2E7D32"/><circle cx="250" cy="135" r="4" fill="#2E7D32"/><path d="M220 150 L280 150" stroke="#4CAF50" stroke-width="2"/>',
    17: '<path d="M180 100 L200 80 L220 100" stroke="#4CAF50" fill="none" stroke-width="3"/><path d="M220 100 L240 80 L260 100" stroke="#66BB6A" fill="none" stroke-width="3"/><path d="M260 100 L280 80 L300 100" stroke="#81C784" fill="none" stroke-width="3"/><circle cx="240" cy="130" r="20" fill="#A5D6A7"/><circle cx="240" cy="130" r="10" fill="#4CAF50"/>',
    18: '<path d="M170 120 L250 80 L330 120 L330 160 L170 160 Z" fill="#A5D6A7" opacity="0.8"/><path d="M200 130 L250 110 L300 130" stroke="#2E7D32" fill="none" stroke-width="2"/><circle cx="250" cy="100" r="15" fill="#FFE082"/><path d="M250 85 L250 70" stroke="#FF8F00" stroke-width="2"/>',
    19: '<circle cx="250" cy="90" r="35" fill="#90CAF9" opacity="0.5"/><path d="M215 90 Q250 60 285 90" stroke="#42A5F5" fill="none" stroke-width="2"/><path d="M215 90 Q250 120 285 90" stroke="#42A5F5" fill="none" stroke-width="2"/><circle cx="250" cy="90" r="8" fill="#1E88E5"/><path d="M210 130 L290 130" stroke="#4CAF50" stroke-width="2"/><path d="M225 130 L225 155" stroke="#4CAF50" fill="none" stroke-width="2"/><path d="M275 130 L275 155" stroke="#4CAF50" fill="none" stroke-width="2"/>',
    20: '<path d="M180 140 L220 100 L260 120 L300 80 L320 100" stroke="#4CAF50" fill="none" stroke-width="3"/><circle cx="180" cy="140" r="8" fill="#A5D6A7"/><circle cx="220" cy="100" r="8" fill="#81C784"/><circle cx="260" cy="120" r="8" fill="#66BB6A"/><circle cx="300" cy="80" r="8" fill="#4CAF50"/><circle cx="320" cy="100" r="10" fill="#2E7D32"/>',
    21: '<circle cx="250" cy="100" r="40" fill="#90CAF9" opacity="0.4"/><ellipse cx="250" cy="110" rx="30" ry="20" fill="#81C784"/><path d="M235 95 L250 70 L265 95" stroke="#4CAF50" fill="#A5D6A7" stroke-width="1"/><circle cx="250" cy="110" r="5" fill="#2E7D32"/>',
    22: '<path d="M220 70 L280 70 L280 130 L220 130 Z" fill="#FFE082" opacity="0.5"/><circle cx="250" cy="90" r="12" fill="#81C784"/><path d="M238 90 L262 90" stroke="#2E7D32" stroke-width="2"/><path d="M250 78 L250 102" stroke="#2E7D32" stroke-width="2"/><path d="M200 140 L250 130 L300 140" stroke="#4CAF50" fill="none" stroke-width="2"/>',
    23: '<circle cx="250" cy="90" r="35" fill="#90CAF9" opacity="0.5"/><path d="M220 80 A30 30 0 0 1 280 80" stroke="#1E88E5" fill="none" stroke-width="2"/><path d="M220 80 A30 30 0 0 0 280 80" stroke="#1E88E5" fill="none" stroke-width="2"/><circle cx="250" cy="90" r="6" fill="#4CAF50"/><path d="M215 130 Q250 115 285 130" stroke="#4CAF50" fill="none" stroke-width="2"/><path d="M225 135 Q250 120 275 135" stroke="#66BB6A" fill="none" stroke-width="2"/>',
    24: '<rect x="215" y="70" width="70" height="50" rx="5" fill="#8D6E63" opacity="0.5"/><path d="M220 80 L230 90 L240 75 L250 85 L260 70 L270 80 L280 75" stroke="#FF5722" fill="none" stroke-width="2"/><path d="M225 120 L275 120" stroke="#795548" stroke-width="2"/>',
    25: '<circle cx="250" cy="90" r="30" fill="#FFE082" opacity="0.6"/><path d="M250 60 L250 45" stroke="#FF8F00" stroke-width="3"/><path d="M230 65 L220 50" stroke="#FF8F00" stroke-width="2"/><path d="M270 65 L280 50" stroke="#FF8F00" stroke-width="2"/><rect x="215" y="120" width="70" height="40" rx="5" fill="#A5D6A7" opacity="0.6"/>',
    26: '<path d="M220 130 L250 70 L280 130 Z" fill="#A5D6A7"/><path d="M235 130 L250 90 L265 130 Z" fill="#81C784"/><circle cx="250" cy="110" r="8" fill="#2E7D32"/><path d="M210 140 L290 140" stroke="#795548" stroke-width="2"/>',
    27: '<path d="M230 80 Q250 60 270 80 L270 130 L230 130 Z" fill="#A5D6A7"/><path d="M240 130 Q250 145 260 130" stroke="#4CAF50" fill="none" stroke-width="2"/><circle cx="250" cy="100" r="10" fill="#FFE082"/><circle cx="250" cy="100" r="5" fill="#FF8F00"/>',
    28: '<path d="M230 70 L270 70 L270 120 Q270 140 250 140 Q230 140 230 120 Z" fill="#90CAF9" opacity="0.6"/><path d="M240 85 L260 85" stroke="#1E88E5" stroke-width="2"/><path d="M240 95 L260 95" stroke="#1E88E5" stroke-width="2"/><path d="M240 105 L255 105" stroke="#1E88E5" stroke-width="2"/>',
    29: '<circle cx="250" cy="95" r="30" fill="#CE93D8" opacity="0.4"/><circle cx="250" cy="95" r="18" fill="#AB47BC" opacity="0.5"/><circle cx="250" cy="95" r="8" fill="#7B1FA2"/><path d="M235 125 L250 140 L265 125" stroke="#7B1FA2" fill="none" stroke-width="2"/>',
    30: '<circle cx="250" cy="90" r="25" fill="#EF9A9A" opacity="0.5"/><path d="M235 75 L265 105" stroke="#C62828" stroke-width="2"/><path d="M265 75 L235 105" stroke="#C62828" stroke-width="2"/><path d="M220 130 L280 130" stroke="#4CAF50" stroke-width="2"/><circle cx="250" cy="130" r="8" fill="#A5D6A7"/>',
}

titles = {
    11: "Архей и протерозой",
    12: "Палеозой",
    13: "Мезозой",
    14: "Кайнозой и человек",
    15: "Экологические факторы",
    16: "Популяции",
    17: "Биоценозы",
    18: "Экосистемы",
    19: "Круговорот веществ",
    20: "Сукцессия",
    21: "Биосфера",
    22: "Функции живого вещества",
    23: "Круговорот в биосфере",
    24: "Антропогенные факторы",
    25: "Глобальные проблемы",
    26: "Охрана природы",
    27: "Селекция",
    28: "Генетическая инженерия",
    29: "Клеточная инженерия",
    30: "Этика биотехнологии",
}

output_dirs = [
    '/home/z/my-project/school-curriculum-app/public/images/lessons/grade11/biology',
    '/home/z/my-project/school-curriculum-app/school-curriculum-site/images/lessons/grade11/biology',
    '/home/z/my-project/school-curriculum-app/android/app/src/main/assets/public/images/lessons/grade11/biology',
]

for lesson_num in range(11, 31):
    svg = SVG_TEMPLATE.format(
        icon=icons.get(lesson_num, ''),
        title=titles.get(lesson_num, f'Урок {lesson_num}')
    )
    for d in output_dirs:
        filepath = f'{d}/lesson{lesson_num}.svg'
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg)
    print(f'Created lesson{lesson_num}.svg')

print('Done! Created SVGs for lessons 11-30 in all 3 locations')
