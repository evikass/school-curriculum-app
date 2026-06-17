#!/usr/bin/env python3
"""Generate SVG lesson images for grade 9 biology (lessons 10-25)"""

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
  <text x="250" y="305" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#66BB6A">Биология · 9 класс</text>
</svg>'''

icons = {
    10: '<circle cx="250" cy="90" r="35" fill="#90CAF9" opacity="0.5"/><path d="M225 80 A25 25 0 0 1 275 80" stroke="#1E88E5" fill="none" stroke-width="2"/><path d="M225 80 A25 25 0 0 0 275 80" stroke="#1E88E5" fill="none" stroke-width="2"/><circle cx="250" cy="90" r="6" fill="#4CAF50"/><path d="M215 130 Q250 115 285 130" stroke="#4CAF50" fill="none" stroke-width="2"/>',
    11: '<circle cx="250" cy="90" r="30" fill="#FFCCBC"/><circle cx="240" cy="85" r="3" fill="#5D4037"/><circle cx="260" cy="85" r="3" fill="#5D4037"/><path d="M243 95 Q250 100 257 95" stroke="#5D4037" fill="none" stroke-width="1.5"/><path d="M220 90 Q210 70 225 65" stroke="#5D4037" fill="none" stroke-width="1"/><path d="M280 90 Q290 70 275 65" stroke="#5D4037" fill="none" stroke-width="1"/>',
    12: '<path d="M230 130 Q230 70 250 70 Q270 70 270 130" fill="#A5D6A7"/><path d="M235 130 Q235 80 250 80 Q265 80 265 130" fill="#81C784"/><circle cx="250" cy="100" r="8" fill="#FFE082"/><circle cx="250" cy="100" r="4" fill="#FF8F00"/>',
    13: '<circle cx="250" cy="90" r="30" fill="#FFE082" opacity="0.6"/><path d="M235 80 L250 65 L265 80" stroke="#FF8F00" fill="none" stroke-width="2"/><path d="M230 95 L220 110" stroke="#FF8F00" fill="none" stroke-width="2"/><path d="M270 95 L280 110" stroke="#FF8F00" fill="none" stroke-width="2"/><circle cx="250" cy="90" r="10" fill="#FFD54F"/>',
    14: '<rect x="220" y="70" width="60" height="80" rx="5" fill="#90CAF9" opacity="0.5"/><line x1="230" y1="85" x2="270" y2="85" stroke="#1E88E5" stroke-width="1.5"/><line x1="230" y1="95" x2="270" y2="95" stroke="#1E88E5" stroke-width="1.5"/><line x1="230" y1="105" x2="265" y2="105" stroke="#1E88E5" stroke-width="1.5"/><line x1="230" y1="115" x2="260" y2="115" stroke="#1E88E5" stroke-width="1.5"/>',
    15: '<ellipse cx="250" cy="80" rx="40" ry="15" fill="#CE93D8" opacity="0.4"/><ellipse cx="250" cy="100" rx="35" ry="12" fill="#AB47BC" opacity="0.3"/><ellipse cx="250" cy="118" rx="30" ry="10" fill="#7B1FA2" opacity="0.3"/><line x1="210" y1="80" x2="210" y2="118" stroke="#7B1FA2" stroke-width="1.5"/><line x1="290" y1="80" x2="290" y2="118" stroke="#7B1FA2" stroke-width="1.5"/>',
    16: '<circle cx="250" cy="85" r="20" fill="#EF9A9A" opacity="0.5"/><text x="250" y="90" text-anchor="middle" font-family="Arial" font-size="14" fill="#C62828" font-weight="bold">XY</text><path d="M225 120 Q250 105 275 120" stroke="#4CAF50" fill="none" stroke-width="2"/><path d="M235 125 Q250 110 265 125" stroke="#66BB6A" fill="none" stroke-width="2"/>',
    17: '<path d="M220 80 L280 80 L270 130 L230 130 Z" fill="#FFE082" opacity="0.5"/><circle cx="250" cy="105" r="12" fill="#FF8F00" opacity="0.6"/><path d="M250 90 L250 75" stroke="#FF5722" stroke-width="2"/><path d="M235 100 L215 85" stroke="#4CAF50" fill="none" stroke-width="2"/><path d="M265 100 L285 85" stroke="#4CAF50" fill="none" stroke-width="2"/>',
    18: '<path d="M230 70 L270 70 L270 130 L230 130 Z" fill="#A5D6A7"/><path d="M240 130 Q250 145 260 130" stroke="#4CAF50" fill="none" stroke-width="2"/><circle cx="250" cy="100" r="10" fill="#FFE082"/><circle cx="250" cy="100" r="5" fill="#FF8F00"/>',
    19: '<circle cx="250" cy="90" r="35" fill="#FFE082"/><path d="M250 55 L250 45" stroke="#FF8F00" stroke-width="3"/><path d="M225 60 L215 50" stroke="#FF8F00" stroke-width="2"/><path d="M275 60 L285 50" stroke="#FF8F00" stroke-width="2"/><path d="M220 90 L200 90" stroke="#4CAF50" stroke-width="2"/><path d="M280 90 L300 90" stroke="#4CAF50" stroke-width="2"/>',
    20: '<path d="M200 120 Q200 70 250 70 Q300 70 300 120" fill="#81C784"/><path d="M210 120 Q210 85 250 85 Q290 85 290 120" fill="#A5D6A7"/><circle cx="235" cy="100" r="4" fill="#2E7D32"/><circle cx="265" cy="95" r="4" fill="#2E7D32"/><circle cx="250" cy="110" r="4" fill="#2E7D32"/>',
    21: '<path d="M170 120 L250 80 L330 120 L330 160 L170 160 Z" fill="#A5D6A7" opacity="0.8"/><path d="M200 130 L250 110 L300 130" stroke="#2E7D32" fill="none" stroke-width="2"/><circle cx="250" cy="100" r="15" fill="#FFE082"/><path d="M250 85 L250 70" stroke="#FF8F00" stroke-width="2"/>',
    22: '<path d="M180 140 L220 100 L260 120 L300 80 L320 100" stroke="#4CAF50" fill="none" stroke-width="3"/><circle cx="180" cy="140" r="8" fill="#A5D6A7"/><circle cx="220" cy="100" r="8" fill="#81C784"/><circle cx="260" cy="120" r="8" fill="#66BB6A"/><circle cx="300" cy="80" r="8" fill="#4CAF50"/><circle cx="320" cy="100" r="10" fill="#2E7D32"/>',
    23: '<circle cx="250" cy="100" r="40" fill="#90CAF9" opacity="0.4"/><ellipse cx="250" cy="110" rx="30" ry="20" fill="#81C784"/><path d="M235 95 L250 70 L265 95" stroke="#4CAF50" fill="#A5D6A7" stroke-width="1"/><circle cx="250" cy="110" r="5" fill="#2E7D32"/>',
    24: '<rect x="215" y="70" width="70" height="50" rx="5" fill="#8D6E63" opacity="0.5"/><path d="M220 80 L230 90 L240 75 L250 85 L260 70 L270 80 L280 75" stroke="#FF5722" fill="none" stroke-width="2"/><path d="M225 120 L275 120" stroke="#795548" stroke-width="2"/>',
    25: '<path d="M220 130 L250 70 L280 130 Z" fill="#A5D6A7"/><path d="M235 130 L250 90 L265 130 Z" fill="#81C784"/><circle cx="250" cy="110" r="8" fill="#2E7D32"/><path d="M210 140 L290 140" stroke="#795548" stroke-width="2"/>',
}

titles = {
    10: "Развитие жизни на Земле",
    11: "Происхождение человека",
    12: "Основы генетики",
    13: "Законы Менделя",
    14: "Решение задач",
    15: "Сцепление генов",
    16: "Генетика пола",
    17: "Изменчивость",
    18: "Селекция",
    19: "Экологические факторы",
    20: "Популяции и сообщества",
    21: "Экосистемы",
    22: "Сукцессия",
    23: "Биосфера",
    24: "Влияние человека",
    25: "Охрана природы",
}

output_dirs = [
    '/home/z/my-project/school-curriculum-app/public/images/lessons/grade9/biology',
    '/home/z/my-project/school-curriculum-app/school-curriculum-site/images/lessons/grade9/biology',
    '/home/z/my-project/school-curriculum-app/android/app/src/main/assets/public/images/lessons/grade9/biology',
]

for lesson_num in range(10, 26):
    svg = SVG_TEMPLATE.format(
        icon=icons.get(lesson_num, ''),
        title=titles.get(lesson_num, f'Урок {lesson_num}')
    )
    for d in output_dirs:
        filepath = f'{d}/lesson{lesson_num}.svg'
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg)
    print(f'Created lesson{lesson_num}.svg')

print('Done!')
