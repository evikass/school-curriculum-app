#!/usr/bin/env python3
"""Generate all 33 biology grade 8 (Human Anatomy) SVG lesson illustrations."""
import os
OUT = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade8/biology"
os.makedirs(OUT, exist_ok=True)
P = "#2E7D32"; L = "#E8F5E9"; M = "#C8E6C9"
def hdr(title, num):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{L}"/><stop offset="100%" stop-color="{M}"/></linearGradient></defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="{P}" stroke-width="2.5"/>
<text x="250" y="30" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="{P}" text-anchor="middle">{title}</text>
<text x="250" y="46" font-family="Arial,sans-serif" font-size="10" fill="#888" text-anchor="middle">Биология 8 класс — Урок {num}</text>
<line x1="30" y1="52" x2="470" y2="52" stroke="{P}" stroke-width="1.5" opacity="0.25"/>
'''
ftr = '\n<rect x="10" y="325" width="480" height="20" rx="4" fill="#2E7D32" opacity="0.85"/>\n<text x="250" y="339" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="white" font-weight="bold">Биология 8 класс</text>\n</svg>'
def ib(x,y,w,h,lines):
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="white" stroke="{P}" stroke-width="1" opacity="0.9"/>\n'
    for i,l in enumerate(lines): s+=f'<text x="{x+w//2}" y="{y+14+i*11}" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">{l}</text>\n'
    return s

# Human body outline (reusable)
def human_silhouette(cx=250,cy=200,scale=0.8):
    return f'''<g transform="translate({cx},{cy}) scale({scale})">
<path d="M0,-80 Q-5,-85 -5,-90 Q-5,-98 0,-100 Q5,-98 5,-90 Q5,-85 0,-80" fill="#BCAAA4" stroke="#5D4037" stroke-width="1"/>
<circle cx="0" cy="-108" r="12" fill="#D7CCC8" stroke="#5D4037" stroke-width="1.5"/>
<line x1="0" y1="-96" x2="0" y2="-50" stroke="#5D4037" stroke-width="2"/>
<line x1="0" y1="-70" x2="-25" y2="-55" stroke="#5D4037" stroke-width="2"/>
<line x1="0" y1="-70" x2="25" y2="-55" stroke="#5D4037" stroke-width="2"/>
<line x1="-25" y1="-55" x2="-30" y2="-35" stroke="#5D4037" stroke-width="1.5"/>
<line x1="25" y1="-55" x2="30" y2="-35" stroke="#5D4037" stroke-width="1.5"/>
<line x1="0" y1="-50" x2="-12" y2="0" stroke="#5D4037" stroke-width="2"/>
<line x1="0" y1="-50" x2="12" y2="0" stroke="#5D4037" stroke-width="2"/>
<line x1="-12" y1="0" x2="-15" y2="50" stroke="#5D4037" stroke-width="1.5"/>
<line x1="12" y1="0" x2="15" y2="50" stroke="#5D4037" stroke-width="1.5"/>
</g>'''

titles = {
1:"Место человека в живой природе",2:"Сходство человека с животными и отличия",3:"Доказательства эволюции человека",
4:"Этапы эволюции человека",5:"Расы человека",6:"Уровни организации организма",
7:"Клетка: строение и жизнедеятельность",8:"Ткани человека",9:"Строение скелета человека",
10:"Строение и виды костей",11:"Мышцы и их работа",12:"Внутренняя среда. Кровь",
13:"Иммунитет",14:"Строение сердца",15:"Кровообращение",16:"Лимфатическая система",
17:"Строение дыхательной системы",18:"Газообмен и регуляция дыхания",
19:"Пищеварение в ротовой полости и желудке",20:"Пищеварение в кишечнике",
21:"Обмен веществ и энергии",22:"Витамины",23:"Кожа и терморегуляция",
24:"Выделительная система",25:"Строение нервной системы",26:"Головной мозг",
27:"Спинной мозг",28:"Органы чувств и анализаторы",29:"Зрение, слух и равновесие",
30:"Рефлексы и ВНД",31:"Сон, речь, память",32:"Эндокринная система",
33:"Размножение и развитие"
}

svgs = {}

# 1
svgs[1]=hdr(titles[1],1)+'''
<g transform="translate(250,180)">
<circle cx="0" cy="-10" r="50" fill="#4CAF50" opacity="0.1" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Человек</text>
<g transform="translate(-60,40)"><rect x="-28" y="-10" width="56" height="20" rx="10" fill="#FF9800" opacity="0.3" stroke="#E65100" stroke-width="1"/><text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Животные</text></g>
<g transform="translate(60,40)"><rect x="-28" y="-10" width="56" height="20" rx="10" fill="#2196F3" opacity="0.3" stroke="#1565C0" stroke-width="1"/><text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">Млекопитающие</text></g>
<g transform="translate(-40,75)"><rect x="-22" y="-10" width="44" height="20" rx="10" fill="#9C27B0" opacity="0.3" stroke="#7B1FA2" stroke-width="1"/><text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle">Приматы</text></g>
<g transform="translate(40,75)"><rect x="-25" y="-10" width="50" height="20" rx="10" fill="#F44336" opacity="0.3" stroke="#C62828" stroke-width="1"/><text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">Хордовые</text></g>
</g>
'''+ib(30,275,440,40,["Тип Хордовые | Класс Млекопитающие | Отряд Приматы | Семейство Гоминиды","Сходство с животными: клеточное строение, обмен веществ, размножение","Отличия: прямохождение, речь, мышление, сознание, трудовая деятельность"])+ftr

# 2
svgs[2]=hdr(titles[2],2)+human_silhouette(150,190,0.7)+'''
<g transform="translate(350,160)">
<rect x="-80" y="-70" width="160" height="140" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-55" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Отличия от животных</text>
<rect x="-70" y="-45" width="140" height="16" rx="3" fill="#C8E6C9" stroke="#2E7D32" stroke-width="0.8"/>
<text x="0" y="-33" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Прямохождение</text>
<rect x="-70" y="-25" width="140" height="16" rx="3" fill="#C8E6C9" stroke="#2E7D32" stroke-width="0.8"/>
<text x="0" y="-13" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Речь (Брока, Вернике)</text>
<rect x="-70" y="-5" width="140" height="16" rx="3" fill="#C8E6C9" stroke="#2E7D32" stroke-width="0.8"/>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Абстрактное мышление</text>
<rect x="-70" y="15" width="140" height="16" rx="3" fill="#C8E6C9" stroke="#2E7D32" stroke-width="0.8"/>
<text x="0" y="27" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Сознание и самосознание</text>
<rect x="-70" y="35" width="140" height="16" rx="3" fill="#C8E6C9" stroke="#2E7D32" stroke-width="0.8"/>
<text x="0" y="47" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Трудовая деятельность</text>
</g>
'''+ftr

# 3
svgs[3]=hdr(titles[3],3)+'''
<g transform="translate(100,170)"><rect x="-50" y="-40" width="100" height="80" rx="5" fill="white" stroke="#795548" stroke-width="1.5"/><text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#795548" text-anchor="middle" font-weight="bold">Палеонтологические</text><text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Ископаемые останки</text><text x="0" y="2" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">австралопитеков,</text><text x="0" y="14" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">неандертальцев,</text><text x="0" y="26" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">кроманьонцев</text></g>
<g transform="translate(250,170)"><rect x="-50" y="-40" width="100" height="80" rx="5" fill="white" stroke="#1565C0" stroke-width="1.5"/><text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">Сравнительно-</text><text x="0" y="-13" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">анатомические</text><text x="0" y="2" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Рудименты:</text><text x="0" y="14" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">аппендикс,</text><text x="0" y="26" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">копчик, мышцы ушей</text></g>
<g transform="translate(400,170)"><rect x="-50" y="-40" width="100" height="80" rx="5" fill="white" stroke="#9C27B0" stroke-width="1.5"/><text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#9C27B0" text-anchor="middle" font-weight="bold">Молекулярно-</text><text x="0" y="-13" font-family="Arial,sans-serif" font-size="7" fill="#9C27B0" text-anchor="middle" font-weight="bold">генетические</text><text x="0" y="2" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">98% ДНК общее</text><text x="0" y="14" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">с шимпанзе</text><text x="0" y="26" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Сходство белков</text></g>
'''+ib(30,260,440,55,["Атавизмы: многососковость, хвост, сплошной волосяной покров","Эмбриологические: сходство зародышей на ранних стадиях","Биогенетический закон Геккеля: онтогенез повторяет филогенез"])+ftr

# 4
svgs[4]=hdr(titles[4],4)+'''
<line x1="50" y1="180" x2="450" y2="180" stroke="#5D4037" stroke-width="2"/>
<path d="M450,180 L445,175 M450,180 L445,185" stroke="#5D4037" stroke-width="2" fill="none"/>
<circle cx="80" cy="180" r="6" fill="#795548" stroke="#4E342E" stroke-width="1.5"/>
<text x="80" y="200" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Дриопитек</text>
<text x="80" y="210" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">20 млн л.н.</text>
<circle cx="150" cy="180" r="6" fill="#8D6E63" stroke="#4E342E" stroke-width="1.5"/>
<text x="150" y="200" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Австралопитек</text>
<text x="150" y="210" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">4 млн л.н.</text>
<circle cx="220" cy="180" r="6" fill="#A1887F" stroke="#4E342E" stroke-width="1.5"/>
<text x="220" y="200" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Ч. умелый</text>
<text x="220" y="210" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">2 млн л.н.</text>
<circle cx="280" cy="180" r="6" fill="#BCAAA4" stroke="#4E342E" stroke-width="1.5"/>
<text x="280" y="200" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Ч. прямоходящий</text>
<text x="280" y="210" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">1 млн л.н.</text>
<circle cx="340" cy="180" r="6" fill="#FFAB91" stroke="#BF360C" stroke-width="1.5"/>
<text x="340" y="200" font-family="Arial,sans-serif" font-size="5" fill="#BF360C" text-anchor="middle">Неандерталец</text>
<text x="340" y="210" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">200 тыс. л.н.</text>
<circle cx="410" cy="180" r="6" fill="#81C784" stroke="#2E7D32" stroke-width="1.5"/>
<text x="410" y="200" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Кроманьонец</text>
<text x="410" y="210" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">40 тыс. л.н.</text>
<!-- Brain size increase -->
<circle cx="80" cy="110" r="5" fill="#EFEBE9" stroke="#795548" stroke-width="1"/>
<circle cx="150" cy="100" r="8" fill="#EFEBE9" stroke="#8D6E63" stroke-width="1"/>
<circle cx="220" cy="88" r="10" fill="#EFEBE9" stroke="#A1887F" stroke-width="1"/>
<circle cx="280" cy="78" r="12" fill="#EFEBE9" stroke="#BCAAA4" stroke-width="1"/>
<circle cx="340" cy="68" r="14" fill="#EFEBE9" stroke="#FFAB91" stroke-width="1"/>
<circle cx="410" cy="55" r="16" fill="#EFEBE9" stroke="#81C784" stroke-width="1"/>
<text x="250" y="65" font-family="Arial,sans-serif" font-size="7" fill="#5D4037" text-anchor="middle">Увеличение мозга</text>
'''+ib(30,230,440,45,["Движущие силы антропогенеза: биологические и социальные факторы","Труд: изготовление орудий | Речь: передача опыта | Общество: совместная деятельность","Биологические факторы: наследственность, изменчивость, борьба за существование"])+ftr

# 5-33 (abbreviated - generate compact but meaningful SVGs)
for n in range(5,34):
    t = titles[n]
    # Create topic-specific content based on keywords
    if n == 5:  # Расы
        svgs[n] = hdr(t,n)+'''
<g transform="translate(85,160)"><circle cx="0" cy="-15" r="14" fill="#FFCC80" stroke="#E65100" stroke-width="1.5"/><ellipse cx="0" cy="15" rx="12" ry="18" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/><text x="0" y="42" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Монголоидная</text></g>
<g transform="translate(250,160)"><circle cx="0" cy="-15" r="14" fill="#8D6E63" stroke="#4E342E" stroke-width="1.5"/><ellipse cx="0" cy="15" rx="12" ry="18" fill="#A1887F" stroke="#4E342E" stroke-width="1"/><text x="0" y="42" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Негроидная</text></g>
<g transform="translate(415,160)"><circle cx="0" cy="-15" r="14" fill="#FFECB3" stroke="#F57F17" stroke-width="1.5"/><ellipse cx="0" cy="15" rx="12" ry="18" fill="#FFF9C4" stroke="#F57F17" stroke-width="1"/><text x="0" y="42" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle" font-weight="bold">Европеоидная</text></g>
'''+ib(30,240,440,50,["3 большие расы: европеоидная, монголоидная, негроидная","Расы — адаптации к условиям среды (цвет кожи, форма волос, черты лица)","Все расы принадлежат к одному виду Homo sapiens | Расизм научно необоснован"])+ftr
    elif n == 6:  # Уровни организации
        svgs[n] = hdr(t,n)+'''
<g transform="translate(250,180)">
<rect x="-60" y="-80" width="120" height="22" rx="5" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1.5"/><text x="0" y="-65" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Организм</text>
<rect x="-50" y="-53" width="100" height="20" rx="5" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/><text x="0" y="-39" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Системы органов</text>
<rect x="-40" y="-28" width="80" height="18" rx="5" fill="#81C784" stroke="#2E7D32" stroke-width="1"/><text x="0" y="-15" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Органы</text>
<rect x="-30" y="-5" width="60" height="16" rx="5" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/><text x="0" y="7" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">Ткани</text>
<rect x="-20" y="16" width="40" height="14" rx="5" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/><text x="0" y="26" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">Клетки</text>
<rect x="-12" y="35" width="24" height="12" rx="5" fill="#388E3C" stroke="#2E7D32" stroke-width="1"/><text x="0" y="44" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle">Органоиды</text>
<rect x="-6" y="52" width="12" height="10" rx="3" fill="#1B5E20" stroke="#2E7D32" stroke-width="1"/><text x="0" y="60" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle">Молекулы</text>
</g>
'''+ftr
    elif n == 7:  # Клетка
        svgs[n] = hdr(t,n)+'''
<g transform="translate(200,180)">
<ellipse cx="0" cy="0" rx="80" ry="55" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/>
<ellipse cx="-15" cy="-5" rx="20" ry="15" fill="#C8E6C9" stroke="#388E3C" stroke-width="2"/>
<circle cx="-15" cy="-5" r="5" fill="#81C784" stroke="#1B5E20" stroke-width="1"/>
<ellipse cx="25" cy="-15" rx="12" ry="6" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
<ellipse cx="30" cy="15" rx="10" ry="5" fill="#FFAB91" stroke="#BF360C" stroke-width="1"/>
<circle cx="-35" cy="10" r="6" fill="#BBDEFB" stroke="#1565C0" stroke-width="1"/>
<circle cx="10" cy="20" r="5" fill="#E1BEE7" stroke="#7B1FA2" stroke-width="1"/>
<rect x="-50" y="-25" width="8" height="50" rx="2" fill="#CE93D8" stroke="#7B1FA2" stroke-width="1"/>
<text x="-15" y="-28" font-family="Arial,sans-serif" font-size="6" fill="#388E3C" text-anchor="middle">Ядро</text>
<text x="25" y="-25" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">Комплекс Гольджи</text>
<text x="30" y="25" font-family="Arial,sans-serif" font-size="5" fill="#BF360C" text-anchor="middle">Митохондрия</text>
<text x="-35" y="22" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">Вакуоль</text>
<text x="-50" y="-30" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="middle">ЭПС</text>
</g>
<g transform="translate(400,170)">
<rect x="-55" y="-50" width="110" height="100" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-35" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Органоиды клетки</text>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Ядро — управление</text>
<text x="0" y="-8" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Митохондрии — энергия</text>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Рибосомы — белки</text>
<text x="0" y="16" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">ЭПС — транспорт</text>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Гольджи — упаковка</text>
<text x="0" y="40" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Лизосомы — переваривание</text>
</g>
'''+ftr
    elif n == 8:  # Ткани
        svgs[n] = hdr(t,n)+'''
<g transform="translate(70,140)"><rect x="-40" y="-30" width="80" height="60" rx="5" fill="#FFCDD2" stroke="#C62828" stroke-width="1.5"/><text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">Эпителиальная</text><g transform="translate(0,5)"><rect x="-15" y="-8" width="10" height="8" fill="#EF9A9A" stroke="#C62828" stroke-width="0.5"/><rect x="-5" y="-8" width="10" height="8" fill="#EF9A9A" stroke="#C62828" stroke-width="0.5"/><rect x="5" y="-8" width="10" height="8" fill="#EF9A9A" stroke="#C62828" stroke-width="0.5"/><rect x="-15" y="0" width="10" height="8" fill="#EF9A9A" stroke="#C62828" stroke-width="0.5"/><rect x="-5" y="0" width="10" height="8" fill="#EF9A9A" stroke="#C62828" stroke-width="0.5"/><rect x="5" y="0" width="10" height="8" fill="#EF9A9A" stroke="#C62828" stroke-width="0.5"/></g></g>
<g transform="translate(195,140)"><rect x="-40" y="-30" width="80" height="60" rx="5" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1.5"/><text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Соединительная</text><g transform="translate(0,5)"><circle cx="-10" cy="-5" r="3" fill="#A5D6A7" stroke="#2E7D32" stroke-width="0.5"/><circle cx="5" cy="-8" r="2" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/><circle cx="10" cy="5" r="3" fill="#A5D6A7" stroke="#2E7D32" stroke-width="0.5"/><circle cx="-5" cy="8" r="2" fill="#81C784" stroke="#2E7D32" stroke-width="0.5"/><line x1="-15" y1="0" x2="15" y2="0" stroke="#66BB6A" stroke-width="0.5"/><line x1="0" y1="-10" x2="0" y2="10" stroke="#66BB6A" stroke-width="0.5"/></g></g>
<g transform="translate(320,140)"><rect x="-40" y="-30" width="80" height="60" rx="5" fill="#BBDEFB" stroke="#1565C0" stroke-width="1.5"/><text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">Мышечная</text><g transform="translate(0,5)"><rect x="-15" y="-8" width="30" height="8" rx="3" fill="#90CAF9" stroke="#1565C0" stroke-width="0.8"/><rect x="-15" y="3" width="30" height="8" rx="3" fill="#64B5F6" stroke="#1565C0" stroke-width="0.8"/></g></g>
<g transform="translate(445,140)"><rect x="-40" y="-30" width="80" height="60" rx="5" fill="#E1BEE7" stroke="#7B1FA2" stroke-width="1.5"/><text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Нервная</text><g transform="translate(0,0)"><circle cx="0" cy="0" r="6" fill="#CE93D8" stroke="#7B1FA2" stroke-width="1"/><line x1="-6" y1="0" x2="-20" y2="-8" stroke="#7B1FA2" stroke-width="1"/><line x1="-6" y1="0" x2="-20" y2="8" stroke="#7B1FA2" stroke-width="1"/><line x1="6" y1="0" x2="25" y2="0" stroke="#7B1FA2" stroke-width="1.5"/></g></g>
'''+ib(30,230,440,55,["Эпителиальная: покровы, железы | Соединительная: кровь, кость, хрящ, жир","Мышечная: гладкая, поперечнополосатая (скелетная), сердечная","Нервная: нейроны (тело, дендриты, аксон) + нейроглия"])+ftr
    elif n in (9,10):  # Скелет
        svgs[n] = hdr(t,n)+'''
<g transform="translate(250,180)">
<!-- Skull -->
<ellipse cx="0" cy="-80" rx="18" ry="22" fill="none" stroke="#795548" stroke-width="2"/>
<ellipse cx="-5" cy="-85" rx="4" ry="3" fill="none" stroke="#5D4037" stroke-width="1"/>
<ellipse cx="5" cy="-85" rx="4" ry="3" fill="none" stroke="#5D4037" stroke-width="1"/>
<path d="M-4,-75 L4,-75" stroke="#5D4037" stroke-width="1"/>
<path d="M-2,-72 L2,-72" stroke="#5D4037" stroke-width="0.8"/>
<!-- Spine -->
<line x1="0" y1="-58" x2="0" y2="10" stroke="#795548" stroke-width="3"/>
<!-- Ribcage -->
<path d="M-25,-45 Q-30,-25 -25,0 Q-15,10 0,10" fill="none" stroke="#795548" stroke-width="1.5"/>
<path d="M25,-45 Q30,-25 25,0 Q15,10 0,10" fill="none" stroke="#795548" stroke-width="1.5"/>
<path d="M-22,-40 Q0,-30 22,-40" fill="none" stroke="#795548" stroke-width="1"/>
<path d="M-24,-30 Q0,-20 24,-30" fill="none" stroke="#795548" stroke-width="1"/>
<!-- Pelvis -->
<path d="M-20,10 Q-25,25 -15,35 Q0,40 15,35 Q25,25 20,10" fill="none" stroke="#795548" stroke-width="2"/>
<!-- Arms -->
<line x1="-25" y1="-45" x2="-40" y2="-30" stroke="#795548" stroke-width="2"/>
<line x1="-40" y1="-30" x2="-45" y2="-10" stroke="#795548" stroke-width="2"/>
<line x1="-45" y1="-10" x2="-48" y2="10" stroke="#795548" stroke-width="1.5"/>
<line x1="25" y1="-45" x2="40" y2="-30" stroke="#795548" stroke-width="2"/>
<line x1="40" y1="-30" x2="45" y2="-10" stroke="#795548" stroke-width="2"/>
<line x1="45" y1="-10" x2="48" y2="10" stroke="#795548" stroke-width="1.5"/>
<!-- Legs -->
<line x1="-10" y1="35" x2="-12" y2="70" stroke="#795548" stroke-width="2.5"/>
<line x1="-12" y1="70" x2="-14" y2="100" stroke="#795548" stroke-width="2"/>
<line x1="10" y1="35" x2="12" y2="70" stroke="#795548" stroke-width="2.5"/>
<line x1="12" y1="70" x2="14" y2="100" stroke="#795548" stroke-width="2"/>
</g>
<g transform="translate(420,120)">
<rect x="-45" y="-30" width="90" height="60" rx="5" fill="white" stroke="#795548" stroke-width="1.5"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="7" fill="#795548" text-anchor="middle" font-weight="bold">Виды костей</text>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Трубчатые: бедро</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Губчатые: позвонки</text>
<text x="0" y="24" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Плоские: череп, рёбра</text>
</g>
'''+ib(30,295,440,18,["Скелет: опора, защита органов, движение | 206 костей | Суставы — подвижные соединения"])+ftr
    elif n == 11:  # Мышцы
        svgs[n] = hdr(t,n)+human_silhouette(250,180,0.85)+'''
<g transform="translate(200,-20)"><path d="M-8,-60 Q-12,-50 -10,-40 Q-5,-35 0,-40 Q5,-35 10,-40 Q12,-50 8,-60 Q0,-65 -8,-60" fill="#E53935" opacity="0.3" stroke="#C62828" stroke-width="1"/></g>
<g transform="translate(300,-20)"><path d="M-8,-60 Q-12,-50 -10,-40 Q-5,-35 0,-40 Q5,-35 10,-40 Q12,-50 8,-60 Q0,-65 -8,-60" fill="#E53935" opacity="0.3" stroke="#C62828" stroke-width="1"/></g>
<rect x="-25" y="-50" width="15" height="35" rx="5" fill="#E53935" opacity="0.25" stroke="#C62828" stroke-width="0.8"/>
<rect x="10" y="-50" width="15" height="35" rx="5" fill="#E53935" opacity="0.25" stroke="#C62828" stroke-width="0.8"/>
'''+ib(30,280,440,30,["Гладкие (непроизвольные) | Поперечнополосатые (произвольные) | Сердечная","Агонисты и антагонисты | Гиподинамия — недостаток движения","Работа мышц: сокращение + расслабление | Утомление | Тренированность"])+ftr
    elif n == 12:  # Кровь
        svgs[n] = hdr(t,n)+'''
<g transform="translate(150,170)">
<circle cx="0" cy="0" r="50" fill="#FFEBEE" stroke="#C62828" stroke-width="2"/>
<circle cx="-15" cy="-10" r="12" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="10" cy="5" r="11" fill="#E53935" opacity="0.5" stroke="#C62828" stroke-width="1"/>
<circle cx="-5" cy="15" r="10" fill="#E53935" opacity="0.7" stroke="#C62828" stroke-width="1"/>
<circle cx="20" cy="-15" r="8" fill="#90CAF9" stroke="#1565C0" stroke-width="1.5"/>
<circle cx="-20" cy="5" r="5" fill="#BBDEFB" stroke="#1565C0" stroke-width="1"/>
<text x="0" y="65" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">Кровь</text>
</g>
<g transform="translate(380,130)">
<rect x="-70" y="-40" width="140" height="80" rx="5" fill="white" stroke="#C62828" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">Состав крови</text>
<rect x="-60" y="-15" width="45" height="15" rx="3" fill="#E53935" opacity="0.5" stroke="#C62828" stroke-width="0.8"/>
<text x="-37" y="-4" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle">Эритроциты</text>
<rect x="15" y="-15" width="45" height="15" rx="3" fill="#90CAF9" stroke="#1565C0" stroke-width="0.8"/>
<text x="37" y="-4" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">Лейкоциты</text>
<rect x="-60" y="5" width="50" height="15" rx="3" fill="#FFAB91" stroke="#BF360C" stroke-width="0.8"/>
<text x="-35" y="16" font-family="Arial,sans-serif" font-size="5" fill="#BF360C" text-anchor="middle">Тромбоциты</text>
<rect x="5" y="5" width="55" height="15" rx="3" fill="#FFE0B2" stroke="#E65100" stroke-width="0.8"/>
<text x="32" y="16" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">Плазма (55%)</text>
</g>
'''+ib(30,265,440,45,["Эритроциты: транспорт O2 и CO2 (гемоглобин) | Без ядра","Лейкоциты: иммунная защита | Фагоцитоз | Тромбоциты: свёртывание","Плазма: вода, белки, соли, гормоны | Группы крови: I, II, III, IV | Резус-фактор"])+ftr
    elif n == 13:  # Иммунитет
        svgs[n] = hdr(t,n)+'''
<g transform="translate(150,170)">
<circle cx="0" cy="0" r="30" fill="#FFEBEE" stroke="#C62828" stroke-width="2"/>
<path d="M-5,-10 Q0,-15 5,-10 L3,5 Q0,8 -3,5Z" fill="#E53935" stroke="#C62828" stroke-width="1"/>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">Микроб</text>
</g>
<g transform="translate(300,170)">
<circle cx="0" cy="0" r="20" fill="#90CAF9" stroke="#1565C0" stroke-width="2"/>
<circle cx="0" cy="0" r="8" fill="#42A5F5" stroke="#0D47A1" stroke-width="1"/>
<text x="0" y="32" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">Лейкоцит</text>
</g>
<g transform="translate(420,170)">
<path d="M-10,-20 Q-5,-25 0,-20 Q5,-25 10,-20 Q15,-15 10,-10 Q5,-5 0,-10 Q-5,-5 -10,-10 Q-15,-15 -10,-20" fill="#CE93D8" stroke="#7B1FA2" stroke-width="1.5"/>
<line x1="0" y1="-10" x2="0" y2="10" stroke="#7B1FA2" stroke-width="1.5"/>
<line x1="-8" y1="0" x2="8" y2="0" stroke="#7B1FA2" stroke-width="1"/>
<text x="0" y="25" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Антитело</text>
</g>
'''+ib(30,260,440,50,["Врождённый: кожный барьер, фагоцитоз, лизоцим, интерферон","Приобретённый: антитела, Т- и В-лимфоциты, клетки памяти","Вакцинация: введение ослабленных антигенов | Сыворотка: готовые антитела"])+ftr
    elif n in (14,15):  # Сердце и кровообращение
        svgs[n] = hdr(t,n)+'''
<g transform="translate(250,175)">
<ellipse cx="0" cy="0" rx="45" ry="50" fill="#FFEBEE" stroke="#C62828" stroke-width="2"/>
<line x1="-5" y1="-45" x2="-5" y2="45" stroke="#C62828" stroke-width="1.5"/>
<line x1="-45" y1="0" x2="45" y2="0" stroke="#C62828" stroke-width="1.5"/>
<!-- 4 chambers -->
<text x="-22" y="-25" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">П.пред.</text>
<text x="22" y="-25" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">Л.пред.</text>
<text x="-22" y="20" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">П.жел.</text>
<text x="22" y="20" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">Л.жел.</text>
<!-- Valves -->
<path d="M-22,-5 Q-18,-2 -14,-5" stroke="#E65100" stroke-width="1.5" fill="none"/>
<path d="M14,-5 Q18,-2 22,-5" stroke="#E65100" stroke-width="1.5" fill="none"/>
<!-- Arteries/veins -->
<line x1="22" y1="-45" x2="22" y2="-58" stroke="#C62828" stroke-width="2.5"/>
<line x1="-22" y1="-45" x2="-22" y2="-58" stroke="#1565C0" stroke-width="2.5"/>
<line x1="22" y1="45" x2="22" y2="58" stroke="#C62828" stroke-width="2.5"/>
<line x1="-22" y1="45" x2="-22" y2="58" stroke="#1565C0" stroke-width="2.5"/>
</g>
<g transform="translate(80,200)">
<text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">Вены (синяя)</text>
</g>
<g transform="translate(420,200)">
<text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle">Артерии (красная)</text>
</g>
'''+ib(30,280,440,30,["4 камеры: 2 предсердия + 2 желудочка | Клапаны: створчатые, полулунные","2 круга: большой (аорта-тело-полые вены) и малый (лёгочная артерия-лёгкие-вены)","Автоматия сердца: синусно-предсердный узел | Пульс: 60-80 уд/мин"])+ftr
    else:
        # Generic but themed SVG for remaining lessons
        icons = {
            16:"Лимфатическая система",17:"Дыхательная система",18:"Газообмен",
            19:"Пищеварение (рот, желудок)",20:"Пищеварение (кишечник)",
            21:"Обмен веществ",22:"Витамины",23:"Кожа",24:"Выделение",
            25:"Нервная система",26:"Головной мозг",27:"Спинной мозг",
            28:"Органы чувств",29:"Зрение и слух",30:"Рефлексы и ВНД",
            31:"Сон, речь, память",32:"Эндокринная система",33:"Размножение"
        }
        colors = {16:"#42A5F5",17:"#66BB6A",18:"#66BB6A",19:"#FF9800",20:"#FF9800",
                  21:"#E53935",22:"#FFD54F",23:"#FFAB91",24:"#AB47BC",
                  25:"#7B1FA2",26:"#7B1FA2",27:"#7B1FA2",28:"#26A69A",
                  29:"#26A69A",30:"#5C6BC0",31:"#5C6BC0",32:"#EC407A",33:"#EC407A"}
        c = colors.get(n,"#2E7D32")
        sub = icons.get(n,t)
        svgs[n] = hdr(t,n)+f'''
<g transform="translate(250,170)">
<circle cx="0" cy="0" r="60" fill="{c}" opacity="0.1" stroke="{c}" stroke-width="2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="12" fill="{c}" text-anchor="middle" font-weight="bold">{sub}</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="9" fill="{c}" text-anchor="middle">8 класс</text>
</g>
<g transform="translate(120,280)">
<rect x="-60" y="-12" width="120" height="24" rx="5" fill="white" stroke="{c}" stroke-width="1" opacity="0.9"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="{c}" text-anchor="middle">Строение и функции</text>
</g>
<g transform="translate(380,280)">
<rect x="-60" y="-12" width="120" height="24" rx="5" fill="white" stroke="{c}" stroke-width="1" opacity="0.9"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="{c}" text-anchor="middle">Гигиена и профилактика</text>
</g>
'''+ftr

for i in range(1,34):
    with open(f"{OUT}/lesson{i}.svg","w") as f:
        f.write(svgs[i])
print(f"Generated {len(svgs)} SVGs for grade 8 biology")
