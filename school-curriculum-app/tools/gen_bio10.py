#!/usr/bin/env python3
"""Generate all 36 biology grade 10 (General Biology Advanced) SVG lesson illustrations."""
import os
OUT = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade10/biology"
os.makedirs(OUT, exist_ok=True)
P = "#2E7D32"; L = "#E8F5E9"; M = "#C8E6C9"
def hdr(title, num):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{L}"/><stop offset="100%" stop-color="{M}"/></linearGradient></defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="{P}" stroke-width="2.5"/>
<text x="250" y="30" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="{P}" text-anchor="middle">{title}</text>
<text x="250" y="46" font-family="Arial,sans-serif" font-size="10" fill="#888" text-anchor="middle">Биология 10 класс — Урок {num}</text>
<line x1="30" y1="52" x2="470" y2="52" stroke="{P}" stroke-width="1.5" opacity="0.25"/>
'''
ftr = '\n<rect x="10" y="325" width="480" height="20" rx="4" fill="#2E7D32" opacity="0.85"/>\n<text x="250" y="339" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="white" font-weight="bold">Биология 10 класс</text>\n</svg>'
def ib(x,y,w,h,lines):
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="white" stroke="{P}" stroke-width="1" opacity="0.9"/>\n'
    for i,l in enumerate(lines): s+=f'<text x="{x+w//2}" y="{y+14+i*11}" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">{l}</text>\n'
    return s

titles = {
1:"Биология как наука",2:"Методы научного познания в биологии",
3:"Уровни организации живой материи",4:"Биологические системы и их свойства",
5:"Химический состав клетки",6:"Углеводы и липиды",7:"Белки",
8:"Нуклеиновые кислоты",9:"АТФ и витамины",
10:"Ферменты — биологические катализаторы",11:"Вирусы — неклеточная форма жизни",
12:"Клеточная теория",13:"Клеточная мембрана",14:"Ядро",
15:"Органеллы цитоплазмы",16:"Прокариоты и эукариоты",
17:"Клеточный цикл",18:"Пластический и энергетический обмен",
19:"Энергетический обмен",20:"Фотосинтез и хемосинтез",
21:"Биосинтез белка",22:"Регуляция транскрипции и трансляции",
23:"Митоз — соматическое деление",24:"Мейоз — редукционное деление",
25:"Гаметогенез",26:"Оплодотворение и виды размножения",
27:"Основы генетики",28:"Хромосомная теория и сцепление генов",
29:"Взаимодействие генов",30:"Изменчивость",
31:"Генетика пола",32:"Генетика человека",
33:"Эмбриональное развитие",34:"Постэмбриональное развитие",
35:"Биогенетический закон и регуляция",36:"Клетка и организм — обобщение"
}

svgs = {}

# 1: Биология как наука
svgs[1]=hdr(titles[1],1)+'''
<g transform="translate(250,180)">
<circle cx="0" cy="0" r="65" fill="#2E7D32" opacity="0.07" stroke="#2E7D32" stroke-width="2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="12" fill="#2E7D32" text-anchor="middle" font-weight="bold">Биология</text>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Наука о жизни</text>
</g>
<g transform="translate(90,105)">
<rect x="-50" y="-20" width="100" height="40" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">Молекулярная</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">биология</text>
</g>
<g transform="translate(210,80)">
<rect x="-40" y="-20" width="80" height="40" rx="5" fill="white" stroke="#9C27B0" stroke-width="1.2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#9C27B0" text-anchor="middle" font-weight="bold">Цитология</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Клетки</text>
</g>
<g transform="translate(330,80)">
<rect x="-40" y="-20" width="80" height="40" rx="5" fill="white" stroke="#E65100" stroke-width="1.2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">Генетика</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Наследственность</text>
</g>
<g transform="translate(430,105)">
<rect x="-40" y="-20" width="80" height="40" rx="5" fill="white" stroke="#4CAF50" stroke-width="1.2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#4CAF50" text-anchor="middle" font-weight="bold">Экология</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Среда</text>
</g>
<g transform="translate(90,255)">
<rect x="-40" y="-20" width="80" height="40" rx="5" fill="white" stroke="#795548" stroke-width="1.2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#795548" text-anchor="middle" font-weight="bold">Эволюция</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Развитие</text>
</g>
<g transform="translate(430,255)">
<rect x="-40" y="-20" width="80" height="40" rx="5" fill="white" stroke="#C62828" stroke-width="1.2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">Эмбриология</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Развитие</text>
</g>
'''+ib(30,295,440,18,["Биология — система наук о живой природе | Интеграция с химией, физикой, математикой","Объект: живые системы | Предмет: закономерности жизни"])+ftr

# 2: Методы научного познания
svgs[2]=hdr(titles[2],2)+'''
<g transform="translate(80,140)">
<rect x="-50" y="-40" width="100" height="80" rx="5" fill="white" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">Наблюдение</text>
<line x1="-35" y1="-18" x2="35" y2="-18" stroke="#1565C0" stroke-width="0.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Описание явлений</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">без вмешательства</text>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Фиксация данных</text>
</g>
<g transform="translate(210,140)">
<rect x="-50" y="-40" width="100" height="80" rx="5" fill="white" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">Эксперимент</text>
<line x1="-35" y1="-18" x2="35" y2="-18" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Опыт, опытная</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">и контрольная</text>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">группы</text>
</g>
<g transform="translate(340,140)">
<rect x="-50" y="-40" width="100" height="80" rx="5" fill="white" stroke="#9C27B0" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#9C27B0" text-anchor="middle" font-weight="bold">Моделирование</text>
<line x1="-35" y1="-18" x2="35" y2="-18" stroke="#9C27B0" stroke-width="0.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Математические</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">и компьютерные</text>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">модели</text>
</g>
<g transform="translate(450,140)">
<rect x="-30" y="-40" width="60" height="80" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Сравнение</text>
<line x1="-20" y1="-18" x2="20" y2="-18" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Сходства</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">и</text>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">различия</text>
</g>
'''+ib(30,260,440,40,["Научный метод: наблюдение - гипотеза - эксперимент - анализ - вывод","Гипотеза: предположение, проверяемое экспериментом","Теория: обоснованная система знаний | Закон: устойчивая закономерность"])+ftr

# 3: Уровни организации живой материи
svgs[3]=hdr(titles[3],3)+'''
<g transform="translate(250,185)">
<rect x="-70" y="-105" width="140" height="24" rx="5" fill="#1B5E20" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-89" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle" font-weight="bold">Биосферный</text>
<rect x="-62" y="-76" width="124" height="22" rx="5" fill="#2E7D32" stroke="#1B5E20" stroke-width="1"/>
<text x="0" y="-61" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">Биогеоценотический</text>
<rect x="-54" y="-49" width="108" height="20" rx="5" fill="#388E3C" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="-35" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">Популяционно-видовой</text>
<rect x="-46" y="-24" width="92" height="18" rx="5" fill="#4CAF50" stroke="#388E3C" stroke-width="1"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">Организменный</text>
<rect x="-38" y="-1" width="76" height="16" rx="5" fill="#66BB6A" stroke="#4CAF50" stroke-width="1"/>
<text x="0" y="11" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">Органно-тканевый</text>
<rect x="-30" y="20" width="60" height="14" rx="5" fill="#81C784" stroke="#66BB6A" stroke-width="1"/>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="7" fill="#1B5E20" text-anchor="middle">Клеточный</text>
<rect x="-22" y="39" width="44" height="12" rx="4" fill="#A5D6A7" stroke="#81C784" stroke-width="1"/>
<text x="0" y="48" font-family="Arial,sans-serif" font-size="6" fill="#1B5E20" text-anchor="middle">Субклеточный</text>
<rect x="-14" y="56" width="28" height="10" rx="3" fill="#C8E6C9" stroke="#A5D6A7" stroke-width="1"/>
<text x="0" y="64" font-family="Arial,sans-serif" font-size="5" fill="#1B5E20" text-anchor="middle">Молекулярный</text>
</g>
'''+ftr

# 4: Биологические системы и их свойства
svgs[4]=hdr(titles[4],4)+'''
<g transform="translate(250,175)">
<circle cx="0" cy="0" r="60" fill="#2E7D32" opacity="0.07" stroke="#2E7D32" stroke-width="2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle" font-weight="bold">Свойства</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">биосистем</text>
</g>
<g transform="translate(85,105)">
<rect x="-45" y="-15" width="90" height="30" rx="5" fill="white" stroke="#C62828" stroke-width="1"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">Целостность</text>
</g>
<g transform="translate(200,85)">
<rect x="-45" y="-15" width="90" height="30" rx="5" fill="white" stroke="#1565C0" stroke-width="1"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">Саморегуляция</text>
</g>
<g transform="translate(310,85)">
<rect x="-45" y="-15" width="90" height="30" rx="5" fill="white" stroke="#9C27B0" stroke-width="1"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="#9C27B0" text-anchor="middle" font-weight="bold">Самовоспроизведение</text>
</g>
<g transform="translate(425,105)">
<rect x="-45" y="-15" width="90" height="30" rx="5" fill="white" stroke="#E65100" stroke-width="1"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">Развитие</text>
</g>
<g transform="translate(85,250)">
<rect x="-45" y="-15" width="90" height="30" rx="5" fill="white" stroke="#4CAF50" stroke-width="1"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="#4CAF50" text-anchor="middle" font-weight="bold">Обмен веществ</text>
</g>
<g transform="translate(200,265)">
<rect x="-45" y="-15" width="90" height="30" rx="5" fill="white" stroke="#795548" stroke-width="1"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="#795548" text-anchor="middle" font-weight="bold">Раздражимость</text>
</g>
<g transform="translate(310,265)">
<rect x="-45" y="-15" width="90" height="30" rx="5" fill="white" stroke="#FF9800" stroke-width="1"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="#FF9800" text-anchor="middle" font-weight="bold">Рост</text>
</g>
<g transform="translate(425,250)">
<rect x="-45" y="-15" width="90" height="30" rx="5" fill="white" stroke="#0097A7" stroke-width="1"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="6" fill="#0097A7" text-anchor="middle" font-weight="bold">Наследственность</text>
</g>
'''+ftr

# 5: Химический состав клетки
svgs[5]=hdr(titles[5],5)+'''
<g transform="translate(250,175)">
<!-- Pie chart representation -->
<circle cx="0" cy="0" r="60" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/>
<path d="M0,0 L0,-60 A60,60 0 0,1 51,-30 Z" fill="#42A5F5" opacity="0.5" stroke="#1565C0" stroke-width="1"/>
<path d="M0,0 L51,-30 A60,60 0 0,1 51,30 Z" fill="#E53935" opacity="0.4" stroke="#C62828" stroke-width="1"/>
<path d="M0,0 L51,30 A60,60 0 0,1 -30,51 Z" fill="#FF9800" opacity="0.4" stroke="#E65100" stroke-width="1"/>
<path d="M0,0 L-30,51 A60,60 0 0,1 -60,0 Z" fill="#9C27B0" opacity="0.3" stroke="#7B1FA2" stroke-width="1"/>
<path d="M0,0 L-60,0 A60,60 0 0,1 0,-60 Z" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
<text x="15" y="-30" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">O 65-70%</text>
<text x="30" y="10" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">C 15-18%</text>
<text x="10" y="35" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">H 8-10%</text>
<text x="-35" y="25" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="middle">N 1.5-3%</text>
<text x="-30" y="-25" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Прочие</text>
</g>
<g transform="translate(420,120)">
<rect x="-50" y="-40" width="100" height="80" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Макроэлементы</text>
<line x1="-35" y1="-18" x2="35" y2="-18" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">O, C, H, N</text>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">P, S, K, Ca</text>
<text x="0" y="21" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Na, Cl, Mg, Fe</text>
<text x="0" y="33" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">98% массы клетки</text>
</g>
'''+ib(30,270,440,35,["Макроэлементы: O, C, H, N — основа органических веществ","Микроэлементы: I, Zn, Cu, F, Mn, Co — катализаторы, гормоны","Вода: 70-80% массы клетки | Универсальный растворитель, среда реакций"])+ftr

# 6: Углеводы и липиды
svgs[6]=hdr(titles[6],6)+'''
<g transform="translate(130,175)">
<rect x="-80" y="-70" width="160" height="140" rx="5" fill="white" stroke="#FF9800" stroke-width="1.5"/>
<text x="0" y="-55" font-family="Arial,sans-serif" font-size="8" fill="#FF9800" text-anchor="middle" font-weight="bold">Углеводы</text>
<line x1="-65" y1="-48" x2="65" y2="-48" stroke="#FF9800" stroke-width="0.5"/>
<text x="0" y="-33" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle" font-weight="bold">Моносахариды</text>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Глюкоза C6H12O6</text>
<text x="0" y="-7" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Фруктоза, рибоза</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle" font-weight="bold">Дисахариды</text>
<text x="0" y="23" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Сахароза, лактоза</text>
<text x="0" y="40" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle" font-weight="bold">Полисахариды</text>
<text x="0" y="53" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Крахмал, гликоген, целлюлоза</text>
</g>
<g transform="translate(370,175)">
<rect x="-80" y="-70" width="160" height="140" rx="5" fill="white" stroke="#9C27B0" stroke-width="1.5"/>
<text x="0" y="-55" font-family="Arial,sans-serif" font-size="8" fill="#9C27B0" text-anchor="middle" font-weight="bold">Липиды</text>
<line x1="-65" y1="-48" x2="65" y2="-48" stroke="#9C27B0" stroke-width="0.5"/>
<text x="0" y="-33" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle" font-weight="bold">Простые липиды</text>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Жиры (триацилглицерины)</text>
<text x="0" y="-7" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Воска</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle" font-weight="bold">Сложные липиды</text>
<text x="0" y="23" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Фосфолипиды мембран</text>
<text x="0" y="40" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle" font-weight="bold">Стероиды</text>
<text x="0" y="53" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Холестерин, гормоны</text>
</g>
'''+ftr

# 7: Белки
svgs[7]=hdr(titles[7],7)+'''
<!-- Protein structure levels -->
<g transform="translate(90,120)">
<rect x="-55" y="-35" width="110" height="70" rx="5" fill="white" stroke="#E53935" stroke-width="1.5"/>
<text x="0" y="-22" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle" font-weight="bold">Первичная</text>
<line x1="-40" y1="-15" x2="40" y2="-15" stroke="#E53935" stroke-width="0.5"/>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Цепь аминокислот</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Пептидная связь</text>
<text x="0" y="25" font-family="Arial,sans-serif" font-size="5" fill="#E53935" text-anchor="middle">20 аминокислот</text>
</g>
<g transform="translate(250,120)">
<rect x="-55" y="-35" width="110" height="70" rx="5" fill="white" stroke="#FF9800" stroke-width="1.5"/>
<text x="0" y="-22" font-family="Arial,sans-serif" font-size="7" fill="#FF9800" text-anchor="middle" font-weight="bold">Вторичная</text>
<line x1="-40" y1="-15" x2="40" y2="-15" stroke="#FF9800" stroke-width="0.5"/>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Альфа-спираль</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Бета-складка</text>
<text x="0" y="25" font-family="Arial,sans-serif" font-size="5" fill="#FF9800" text-anchor="middle">Водородные связи</text>
</g>
<g transform="translate(410,120)">
<rect x="-55" y="-35" width="110" height="70" rx="5" fill="white" stroke="#9C27B0" stroke-width="1.5"/>
<text x="0" y="-22" font-family="Arial,sans-serif" font-size="7" fill="#9C27B0" text-anchor="middle" font-weight="bold">Третичная</text>
<line x1="-40" y1="-15" x2="40" y2="-15" stroke="#9C27B0" stroke-width="0.5"/>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Глобула</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Дисульфидные мостики</text>
<text x="0" y="25" font-family="Arial,sans-serif" font-size="5" fill="#9C27B0" text-anchor="middle">Гидрофобные связи</text>
</g>
'''+ib(30,220,440,60,["Четвертичная: объединение нескольких полипептидов (гемоглобин = 4 цепи)","Функции белков: каталитическая, структурная, транспортная, защитная, регуляторная","Денатурация: разрушение структуры (t, pH) | Ренатурация: восстановление структуры","20 аминокислот | Пептидная связь: -CO-NH- | Заменимые и незаменимые аминокислоты"])+ftr

# 8: Нуклеиновые кислоты
svgs[8]=hdr(titles[8],8)+'''
<!-- DNA double helix representation -->
<g transform="translate(170,185)">
<rect x="-90" y="-80" width="180" height="160" rx="5" fill="white" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="-65" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" text-anchor="middle" font-weight="bold">ДНК — двойная спираль</text>
<!-- Simplified double helix -->
<path d="M-50,-50 Q-25,-35 0,-50 Q25,-65 50,-50" stroke="#1565C0" stroke-width="2.5" fill="none"/>
<path d="M-50,-50 Q-25,-65 0,-50 Q25,-35 50,-50" stroke="#C62828" stroke-width="2.5" fill="none"/>
<!-- Rungs -->
<line x1="-25" y1="-50" x2="25" y2="-50" stroke="#9C27B0" stroke-width="1.5"/>
<path d="M-50,-25 Q-25,-10 0,-25 Q25,-40 50,-25" stroke="#1565C0" stroke-width="2.5" fill="none"/>
<path d="M-50,-25 Q-25,-40 0,-25 Q25,-10 50,-25" stroke="#C62828" stroke-width="2.5" fill="none"/>
<line x1="-25" y1="-25" x2="25" y2="-25" stroke="#9C27B0" stroke-width="1.5"/>
<path d="M-50,0 Q-25,15 0,0 Q25,-15 50,0" stroke="#1565C0" stroke-width="2.5" fill="none"/>
<path d="M-50,0 Q-25,-15 0,0 Q25,15 50,0" stroke="#C62828" stroke-width="2.5" fill="none"/>
<line x1="-25" y1="0" x2="25" y2="0" stroke="#FF9800" stroke-width="1.5"/>
<path d="M-50,25 Q-25,40 0,25 Q25,10 50,25" stroke="#1565C0" stroke-width="2.5" fill="none"/>
<path d="M-50,25 Q-25,10 0,25 Q25,40 50,25" stroke="#C62828" stroke-width="2.5" fill="none"/>
<line x1="-25" y1="25" x2="25" y2="25" stroke="#9C27B0" stroke-width="1.5"/>
<!-- Legend -->
<text x="0" y="50" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">A=T (2 вод. связи)</text>
<text x="0" y="60" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle">G-C (3 вод. связи)</text>
</g>
<g transform="translate(390,165)">
<rect x="-60" y="-55" width="120" height="110" rx="5" fill="white" stroke="#9C27B0" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="8" fill="#9C27B0" text-anchor="middle" font-weight="bold">РНК — одноцепочечная</text>
<line x1="-45" y1="-33" x2="45" y2="-33" stroke="#9C27B0" stroke-width="0.5"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">и-РНК: матрица</text>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">т-РНК: транспорт</text>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">р-РНК: рибосома</text>
<line x1="-45" y1="15" x2="45" y2="15" stroke="#9C27B0" stroke-width="0.5"/>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="5" fill="#9C27B0" text-anchor="middle">Рибоза (не дезоксирибоза)</text>
<text x="0" y="40" font-family="Arial,sans-serif" font-size="5" fill="#9C27B0" text-anchor="middle">U (не T)</text>
</g>
'''+ftr

# 9: АТФ и витамины
svgs[9]=hdr(titles[9],9)+'''
<!-- ATP structure -->
<g transform="translate(150,185)">
<rect x="-90" y="-70" width="180" height="140" rx="5" fill="white" stroke="#FF9800" stroke-width="1.5"/>
<text x="0" y="-55" font-family="Arial,sans-serif" font-size="8" fill="#FF9800" text-anchor="middle" font-weight="bold">АТФ — универсальный энергоноситель</text>
<!-- Simplified ATP: adenine + ribose + 3 phosphates -->
<rect x="-60" y="-40" width="35" height="25" rx="4" fill="#CE93D8" stroke="#7B1FA2" stroke-width="1"/>
<text x="-42" y="-23" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle">Аденин</text>
<rect x="-20" y="-40" width="35" height="25" rx="4" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
<text x="-2" y="-23" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle">Рибоза</text>
<circle cx="35" cy="-28" r="12" fill="#FF9800" stroke="#E65100" stroke-width="1.5"/>
<text x="35" y="-25" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle" font-weight="bold">P</text>
<circle cx="55" cy="-28" r="12" fill="#FFB74D" stroke="#E65100" stroke-width="1.5"/>
<text x="55" y="-25" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle" font-weight="bold">P</text>
<circle cx="75" cy="-28" r="12" fill="#FFCC80" stroke="#E65100" stroke-width="1.5"/>
<text x="75" y="-25" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">P</text>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="7" fill="#FF9800" text-anchor="middle" font-weight="bold">АТФ -> АДФ + P + 40 кДж</text>
<text x="0" y="15" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Синтез: АДФ + P + энергия -> АТФ</text>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Макроэргические связи ~~~</text>
<text x="0" y="45" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">В клетке 1 млрд молекул АТФ</text>
</g>
<g transform="translate(380,170)">
<rect x="-65" y="-50" width="130" height="100" rx="5" fill="white" stroke="#4CAF50" stroke-width="1.5"/>
<text x="0" y="-35" font-family="Arial,sans-serif" font-size="8" fill="#4CAF50" text-anchor="middle" font-weight="bold">Витамины</text>
<line x1="-50" y1="-28" x2="50" y2="-28" stroke="#4CAF50" stroke-width="0.5"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle" font-weight="bold">Жирорастворимые</text>
<text x="0" y="2" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">A, D, E, K</text>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle" font-weight="bold">Водорастворимые</text>
<text x="0" y="32" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">B1-B12, C</text>
<text x="0" y="44" font-family="Arial,sans-serif" font-size="5" fill="#4CAF50" text-anchor="middle">Коферменты</text>
</g>
'''+ftr

# 10: Ферменты
svgs[10]=hdr(titles[10],10)+'''
<!-- Enzyme-substrate complex -->
<g transform="translate(160,180)">
<text x="0" y="-65" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Модель индуцированного соответствия</text>
<!-- Substrate -->
<path d="M-70,-20 Q-65,-35 -55,-35 Q-45,-35 -40,-20 Q-45,-10 -55,-10 Q-65,-10 -70,-20Z" fill="#FF9800" opacity="0.6" stroke="#E65100" stroke-width="1.5"/>
<text x="-55" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">S</text>
<!-- Arrow -->
<line x1="-30" y1="-20" x2="20" y2="-20" stroke="#2E7D32" stroke-width="1.5"/>
<path d="M20,-20 L15,-23 M20,-20 L15,-17" stroke="#2E7D32" stroke-width="1.5"/>
<!-- Enzyme + substrate -->
<path d="M30,-35 Q35,-50 50,-50 Q65,-50 70,-35 Q75,-20 70,-5 Q65,10 50,10 Q35,10 30,-5 Q25,-20 30,-35Z" fill="#81C784" opacity="0.6" stroke="#2E7D32" stroke-width="1.5"/>
<path d="M40,-25 Q45,-35 50,-35 Q55,-35 60,-25 Q55,-15 50,-15 Q45,-15 40,-25Z" fill="#FF9800" opacity="0.5" stroke="#E65100" stroke-width="1"/>
<text x="50" y="-20" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">E+S</text>
<!-- Arrow -->
<line x1="80" y1="-20" x2="130" y2="-20" stroke="#2E7D32" stroke-width="1.5"/>
<path d="M130,-20 L125,-23 M130,-20 L125,-17" stroke="#2E7D32" stroke-width="1.5"/>
<!-- Products -->
<circle cx="150" cy="-30" r="10" fill="#E53935" opacity="0.4" stroke="#C62828" stroke-width="1"/>
<text x="150" y="-27" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">P1</text>
<circle cx="150" cy="-8" r="8" fill="#1565C0" opacity="0.4" stroke="#0D47A1" stroke-width="1"/>
<text x="150" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#0D47A1" text-anchor="middle" font-weight="bold">P2</text>
<path d="M30,-35 Q35,-50 50,-50 Q65,-50 70,-35 Q75,-20 70,-5 Q65,10 50,10 Q35,10 30,-5 Q25,-20 30,-35Z" fill="#81C784" opacity="0.3" stroke="#2E7D32" stroke-width="1.5" stroke-dasharray="3,2"/>
<text x="110" y="25" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">E (не меняется)</text>
</g>
'''+ib(30,265,440,40,["Фермент + Субстрат -> Комплекс -> Продукт + Фермент","Свойства: специфичность, каталитическая активность, зависимость от t и pH","Активный центр: участок связывания субстрата | Кофермент: небелковая часть"])+ftr

# 11: Вирусы
svgs[11]=hdr(titles[11],11)+'''
<!-- Virus structure -->
<g transform="translate(150,180)">
<circle cx="0" cy="0" r="40" fill="#FFEBEE" stroke="#C62828" stroke-width="2"/>
<path d="M-30,-15 Q-15,-25 0,-20 Q15,-25 30,-15 Q25,0 30,15 Q15,25 0,20 Q-15,25 -30,15 Q-25,0 -30,-15Z" fill="#E53935" opacity="0.3" stroke="#C62828" stroke-width="1.5"/>
<line x1="-15" y1="-5" x2="15" y2="5" stroke="#C62828" stroke-width="2"/>
<line x1="-10" y1="5" x2="10" y2="-5" stroke="#C62828" stroke-width="2"/>
<text x="0" y="55" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">Вирус (бактериофаг)</text>
<text x="0" y="68" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Капсид + нуклеиновая к-та</text>
</g>
<!-- Virus types -->
<g transform="translate(350,120)">
<rect x="-80" y="-35" width="160" height="70" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Типы вирусов</text>
<line x1="-65" y1="-12" x2="65" y2="-12" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="2" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">ДНК-содержащие: оспа, герпес</text>
<text x="0" y="15" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">РНК-содержащие: грипп, ВИЧ</text>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Бактериофаги: infect бактерии</text>
</g>
<g transform="translate(350,230)">
<rect x="-80" y="-25" width="160" height="50" rx="5" fill="white" stroke="#C62828" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">ВИЧ — ретровирус</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Обратная транскриптаза</text>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">РНК -> ДНК -> интеграция</text>
</g>
'''+ftr

# 12: Клеточная теория
svgs[12]=hdr(titles[12],12)+'''
<g transform="translate(90,120)">
<rect x="-55" y="-30" width="110" height="60" rx="5" fill="white" stroke="#795548" stroke-width="1.5"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="7" fill="#795548" text-anchor="middle" font-weight="bold">Гук, 1665</text>
<line x1="-40" y1="-8" x2="40" y2="-8" stroke="#795548" stroke-width="0.5"/>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Открыл клетки</text>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">(пробка)</text>
</g>
<g transform="translate(250,120)">
<rect x="-55" y="-30" width="110" height="60" rx="5" fill="white" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">Шлейден-Шванн</text>
<line x1="-40" y1="-8" x2="40" y2="-8" stroke="#1565C0" stroke-width="0.5"/>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Все организмы</text>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">из клеток</text>
</g>
<g transform="translate(410,120)">
<rect x="-55" y="-30" width="110" height="60" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Вирхов, 1855</text>
<line x1="-40" y1="-8" x2="40" y2="-8" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Каждая клетка</text>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">из клетки</text>
</g>
'''+ib(30,220,440,60,["Положения клеточной теории:","1. Клетка — элементарная единица строения и жизнедеятельности","2. Клетки всех организмов сходны по строению, хим. составу, функциям","3. Клетки размножаются делением (каждая из ранее существовавшей)","4. Многоклеточный организм — система клеток, специализированных по функциям"])+ftr

# 13: Клеточная мембрана
svgs[13]=hdr(titles[13],13)+'''
<!-- Fluid mosaic model -->
<g transform="translate(250,180)">
<!-- Phospholipid bilayer -->
<rect x="-120" y="-40" width="240" height="80" rx="3" fill="none" stroke="#2E7D32" stroke-width="1" stroke-dasharray="4,2"/>
<!-- Top layer - heads -->
<circle cx="-100" cy="-30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="-80" cy="-30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="-60" cy="-30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="-40" cy="-30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="-20" cy="-30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="0" cy="-30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="20" cy="-30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="40" cy="-30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="60" cy="-30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="80" cy="-30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="100" cy="-30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<!-- Top tails -->
<line x1="-100" y1="-24" x2="-100" y2="-8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="-80" y1="-24" x2="-80" y2="-8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="-60" y1="-24" x2="-60" y2="-8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="-40" y1="-24" x2="-40" y2="-8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="-20" y1="-24" x2="-20" y2="-8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="0" y1="-24" x2="0" y2="-8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="20" y1="-24" x2="20" y2="-8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="40" y1="-24" x2="40" y2="-8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="60" y1="-24" x2="60" y2="-8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="80" y1="-24" x2="80" y2="-8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="100" y1="-24" x2="100" y2="-8" stroke="#FFAB91" stroke-width="1.5"/>
<!-- Bottom tails -->
<line x1="-100" y1="24" x2="-100" y2="8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="-80" y1="24" x2="-80" y2="8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="-60" y1="24" x2="-60" y2="8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="-40" y1="24" x2="-40" y2="8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="-20" y1="24" x2="-20" y2="8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="0" y1="24" x2="0" y2="8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="20" y1="24" x2="20" y2="8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="40" y1="24" x2="40" y2="8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="60" y1="24" x2="60" y2="8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="80" y1="24" x2="80" y2="8" stroke="#FFAB91" stroke-width="1.5"/>
<line x1="100" y1="24" x2="100" y2="8" stroke="#FFAB91" stroke-width="1.5"/>
<!-- Bottom layer - heads -->
<circle cx="-100" cy="30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="-80" cy="30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="-60" cy="30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="-40" cy="30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="-20" cy="30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="0" cy="30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="20" cy="30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="40" cy="30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="60" cy="30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="80" cy="30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<circle cx="100" cy="30" r="6" fill="#E53935" opacity="0.6" stroke="#C62828" stroke-width="1"/>
<!-- Integral protein -->
<rect x="-15" y="-35" width="30" height="70" rx="8" fill="#42A5F5" opacity="0.5" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="2" font-family="Arial,sans-serif" font-size="5" fill="#0D47A1" text-anchor="middle">Белок</text>
</g>
'''+ib(30,270,440,35,["Жидкостно-мозаичная модель: фосфолипидный бислой + белки","Транспорт: диффузия, осмос, облегчённая диффузия, активный транспорт","Функции: барьерная, транспортная, рецепторная, ферментативная, межклеточная"])+ftr

# 14: Ядро
svgs[14]=hdr(titles[14],14)+'''
<g transform="translate(200,185)">
<ellipse cx="0" cy="0" rx="75" ry="65" fill="white" stroke="#7B1FA2" stroke-width="2"/>
<!-- Nuclear envelope (double membrane) -->
<ellipse cx="0" cy="0" rx="75" ry="65" fill="none" stroke="#9C27B0" stroke-width="1"/>
<!-- Nucleolus -->
<circle cx="10" cy="-10" r="18" fill="#CE93D8" stroke="#7B1FA2" stroke-width="1.5"/>
<text x="10" y="-7" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="middle">Ядрышко</text>
<!-- Chromatin -->
<path d="M-40,10 Q-30,0 -20,10 Q-10,20 0,10 Q10,0 20,10" stroke="#9C27B0" stroke-width="2" fill="none"/>
<path d="M-35,25 Q-25,15 -15,25 Q-5,35 5,25 Q15,15 25,25" stroke="#AB47BC" stroke-width="1.5" fill="none"/>
<!-- Nuclear pores -->
<circle cx="-55" cy="-30" r="3" fill="#E1BEE7" stroke="#7B1FA2" stroke-width="1"/>
<circle cx="55" cy="20" r="3" fill="#E1BEE7" stroke="#7B1FA2" stroke-width="1"/>
<circle cx="-45" cy="40" r="3" fill="#E1BEE7" stroke="#7B1FA2" stroke-width="1"/>
<text x="0" y="55" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="middle">Хроматин</text>
</g>
<g transform="translate(400,160)">
<rect x="-60" y="-55" width="120" height="110" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Функции ядра</text>
<line x1="-45" y1="-33" x2="45" y2="-33" stroke="#7B1FA2" stroke-width="0.5"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Хранение ДНК</text>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Транскрипция</text>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Редупликация ДНК</text>
<text x="0" y="21" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Регуляция клетки</text>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Ядерная оболочка:</text>
<text x="0" y="50" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">2 мембраны + поры</text>
</g>
'''+ftr

# 15: Органеллы цитоплазмы
svgs[15]=hdr(titles[15],15)+'''
<g transform="translate(85,130)">
<rect x="-55" y="-35" width="110" height="70" rx="5" fill="white" stroke="#E65100" stroke-width="1.2"/>
<text x="0" y="-22" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">Митохондрии</text>
<line x1="-40" y1="-15" x2="40" y2="-15" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">2 мембраны, кристы</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Клеточное дыхание</text>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">АТФ-синтез</text>
</g>
<g transform="translate(250,130)">
<rect x="-55" y="-35" width="110" height="70" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
<text x="0" y="-22" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">Комплекс Гольджи</text>
<line x1="-40" y1="-15" x2="40" y2="-15" stroke="#1565C0" stroke-width="0.5"/>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Стеки цистерн</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Модификация белков</text>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">Секреция, лизосомы</text>
</g>
<g transform="translate(415,130)">
<rect x="-55" y="-35" width="110" height="70" rx="5" fill="white" stroke="#9C27B0" stroke-width="1.2"/>
<text x="0" y="-22" font-family="Arial,sans-serif" font-size="6" fill="#9C27B0" text-anchor="middle" font-weight="bold">ЭПС</text>
<line x1="-40" y1="-15" x2="40" y2="-15" stroke="#9C27B0" stroke-width="0.5"/>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Гладкая: липиды</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Шероховатая: белки</text>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#9C27B0" text-anchor="middle">Транспорт, синтез</text>
</g>
<g transform="translate(120,250)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#C62828" stroke-width="1.2"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">Лизосомы</text>
<line x1="-40" y1="-5" x2="40" y2="-5" stroke="#C62828" stroke-width="0.5"/>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Пищеварение, автолиз</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">40+ ферментов</text>
</g>
<g transform="translate(280,250)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Рибосомы</text>
<line x1="-40" y1="-5" x2="40" y2="-5" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Синтез белка</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">80S (эукариоты)</text>
</g>
<g transform="translate(420,250)">
<rect x="-50" y="-25" width="100" height="50" rx="5" fill="white" stroke="#4CAF50" stroke-width="1.2"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="6" fill="#4CAF50" text-anchor="middle" font-weight="bold">Хлоропласты</text>
<line x1="-35" y1="-5" x2="35" y2="-5" stroke="#4CAF50" stroke-width="0.5"/>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Фотосинтез</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">2 мембраны, тилакоиды</text>
</g>
'''+ftr

# 16-36: Mix of detailed and themed SVGs
for n in range(16,37):
    t = titles[n]
    if n == 16:  # Прокариоты и эукариоты
        svgs[n]=hdr(t,n)+'''
<g transform="translate(140,175)">
<rect x="-90" y="-75" width="180" height="150" rx="5" fill="white" stroke="#F9A825" stroke-width="1.5"/>
<text x="0" y="-60" font-family="Arial,sans-serif" font-size="8" fill="#F9A825" text-anchor="middle" font-weight="bold">Прокариоты</text>
<ellipse cx="0" cy="-15" rx="50" ry="25" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/>
<circle cx="15" cy="-15" r="8" fill="#FFD54F" stroke="#F9A825" stroke-width="1"/>
<text x="0" y="25" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Нет ядра</text>
<text x="0" y="35" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Нуклеоид</text>
<text x="0" y="45" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">70S рибосомы</text>
<text x="0" y="55" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Нет мембранных органелл</text>
<text x="0" y="65" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">1 хромосома (кольцевая)</text>
</g>
<g transform="translate(380,175)">
<rect x="-90" y="-75" width="180" height="150" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-60" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Эукариоты</text>
<ellipse cx="0" cy="-15" rx="50" ry="30" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1.5"/>
<circle cx="0" cy="-15" r="10" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="4" fill="#2E7D32" text-anchor="middle">Ядро</text>
<text x="0" y="25" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Есть ядро</text>
<text x="0" y="35" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">80S рибосомы</text>
<text x="0" y="45" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Мембранные органеллы</text>
<text x="0" y="55" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Несколько хромосом</text>
<text x="0" y="65" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Митоз, мейоз</text>
</g>
'''+ftr
    elif n == 17:  # Клеточный цикл
        svgs[n]=hdr(t,n)+'''
<g transform="translate(250,185)">
<circle cx="0" cy="0" r="55" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">M</text>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Митоз</text>
</g>
<g transform="translate(400,120)">
<rect x="-55" y="-25" width="110" height="50" rx="20" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#1B5E20" text-anchor="middle" font-weight="bold">G1 - рост</text>
</g>
<g transform="translate(410,200)">
<rect x="-55" y="-25" width="110" height="50" rx="20" fill="#FFCC80" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">S - синтез ДНК</text>
</g>
<g transform="translate(370,275)">
<rect x="-55" y="-20" width="110" height="40" rx="20" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="7" fill="#1B5E20" text-anchor="middle" font-weight="bold">G2 - подготовка</text>
</g>
<g transform="translate(100,260)">
<rect x="-60" y="-20" width="120" height="40" rx="5" fill="white" stroke="#C62828" stroke-width="1"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">G0 - покой</text>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Выход из цикла</text>
</g>
'''+ib(30,295,440,18,["Интерфаза: G1 + S + G2 (90% времени) | Митоз: профаза-метафаза-анафаза-телофаза","S-фаза: редупликация ДНК | Контрольные точки: G1/S, G2/M"])+ftr
    elif n == 18:  # Пластический и энергетический обмен
        svgs[n]=hdr(t,n)+'''
<g transform="translate(130,180)">
<rect x="-80" y="-65" width="160" height="130" rx="5" fill="white" stroke="#4CAF50" stroke-width="1.5"/>
<text x="0" y="-50" font-family="Arial,sans-serif" font-size="8" fill="#4CAF50" text-anchor="middle" font-weight="bold">Пластический обмен</text>
<text x="0" y="-38" font-family="Arial,sans-serif" font-size="6" fill="#888" text-anchor="middle">(ассимиляция)</text>
<line x1="-65" y1="-30" x2="65" y2="-30" stroke="#4CAF50" stroke-width="0.5"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Простые вещества -> Сложные</text>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Фотосинтез</text>
<text x="0" y="13" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Биосинтез белка</text>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Синтез липидов</text>
<text x="0" y="43" font-family="Arial,sans-serif" font-size="6" fill="#4CAF50" text-anchor="middle">Энергия + АТФ расходуется</text>
</g>
<g transform="translate(370,180)">
<rect x="-80" y="-65" width="160" height="130" rx="5" fill="white" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="-50" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">Энергетический обмен</text>
<text x="0" y="-38" font-family="Arial,sans-serif" font-size="6" fill="#888" text-anchor="middle">(диссимиляция)</text>
<line x1="-65" y1="-30" x2="65" y2="-30" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Сложные вещества -> Простые</text>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Гликолиз</text>
<text x="0" y="13" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Клеточное дыхание</text>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Брожение</text>
<text x="0" y="43" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Энергия + АТФ образуется</text>
</g>
'''+ftr
    elif n == 19:  # Энергетический обмен
        svgs[n]=hdr(t,n)+'''
<!-- Three stages -->
<g transform="translate(85,130)">
<rect x="-55" y="-40" width="110" height="80" rx="5" fill="white" stroke="#FF9800" stroke-width="1.5"/>
<text x="0" y="-28" font-family="Arial,sans-serif" font-size="7" fill="#FF9800" text-anchor="middle" font-weight="bold">I. Подготовка</text>
<line x1="-40" y1="-20" x2="40" y2="-20" stroke="#FF9800" stroke-width="0.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Белки -> аминок-ты</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Жиры -> глицерин + ЖК</text>
<text x="0" y="19" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Крахмал -> глюкоза</text>
<text x="0" y="33" font-family="Arial,sans-serif" font-size="5" fill="#FF9800" text-anchor="middle">В лизосомах</text>
</g>
<g transform="translate(250,130)">
<rect x="-55" y="-40" width="110" height="80" rx="5" fill="white" stroke="#E53935" stroke-width="1.5"/>
<text x="0" y="-28" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle" font-weight="bold">II. Гликолиз</text>
<line x1="-40" y1="-20" x2="40" y2="-20" stroke="#E53935" stroke-width="0.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">C6H12O6 -> 2C3H4O3</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Глюкоза -> ПВК</text>
<text x="0" y="19" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">2 АТФ (чистых)</text>
<text x="0" y="33" font-family="Arial,sans-serif" font-size="5" fill="#E53935" text-anchor="middle">В цитоплазме</text>
</g>
<g transform="translate(415,130)">
<rect x="-55" y="-40" width="110" height="80" rx="5" fill="white" stroke="#9C27B0" stroke-width="1.5"/>
<text x="0" y="-28" font-family="Arial,sans-serif" font-size="7" fill="#9C27B0" text-anchor="middle" font-weight="bold">III. Клеточ. дыхание</text>
<line x1="-40" y1="-20" x2="40" y2="-20" stroke="#9C27B0" stroke-width="0.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">ПВК + O2 -> CO2 + H2O</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Цикл Кребса</text>
<text x="0" y="19" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">36 АТФ</text>
<text x="0" y="33" font-family="Arial,sans-serif" font-size="5" fill="#9C27B0" text-anchor="middle">В митохондриях</text>
</g>
'''+ib(30,260,440,40,["Общее уравнение: C6H12O6 + 6O2 -> 6CO2 + 6H2O + 38 АТФ","Гликолиз: 2 АТФ (бескислородный) | Клеточное дыхание: 36 АТФ (кислородный)","Брожение (без O2): молочнокислое, спиртовое — 2 АТФ"])+ftr
    elif n == 20:  # Фотосинтез и хемосинтез
        svgs[n]=hdr(t,n)+'''
<!-- Light and dark phases -->
<g transform="translate(140,180)">
<rect x="-90" y="-75" width="180" height="150" rx="5" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/>
<text x="0" y="-60" font-family="Arial,sans-serif" font-size="8" fill="#F9A825" text-anchor="middle" font-weight="bold">Световая фаза</text>
<line x1="-75" y1="-52" x2="75" y2="-52" stroke="#F9A825" stroke-width="0.5"/>
<text x="0" y="-35" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">В тилакоидах гран</text>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">H2O -> 2H+ + 1/2 O2 + 2e-</text>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Фотолиз воды</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">АДФ -> АТФ</text>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">НАДФ+ -> НАДФ-H2</text>
<text x="0" y="48" font-family="Arial,sans-serif" font-size="6" fill="#F9A825" text-anchor="middle">O2 — побочный продукт</text>
<text x="0" y="62" font-family="Arial,sans-serif" font-size="6" fill="#F9A825" text-anchor="middle">Хлорофилл поглощает свет</text>
</g>
<g transform="translate(380,180)">
<rect x="-90" y="-75" width="180" height="150" rx="5" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-60" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Темновая фаза</text>
<line x1="-75" y1="-52" x2="75" y2="-52" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="-35" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">В строме хлоропласта</text>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Цикл Кальвина</text>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">CO2 + НАДФ-H2 + АТФ</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">-> C6H12O6 (глюкоза)</text>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Рибулозобисфосфат</text>
<text x="0" y="48" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Не нужен свет напрямую</text>
<text x="0" y="62" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Нужны продукты световой</text>
</g>
'''+ib(30,275,440,35,["6CO2 + 6H2O -> C6H12O6 + 6O2 (суммарное уравнение)","Хемосинтез: автотрофы без света, энергия окисления неорг. веществ (нитрифицирующие бактерии)","Хлоропласт: 2 мембраны + тилакоиды гран + строма | Хлорофилл a, b"])+ftr
    elif n == 21:  # Биосинтез белка
        svgs[n]=hdr(t,n)+'''
<!-- Central dogma: DNA -> RNA -> Protein -->
<g transform="translate(250,100)">
<rect x="-40" y="-18" width="80" height="36" rx="5" fill="#1565C0" opacity="0.2" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" text-anchor="middle" font-weight="bold">ДНК</text>
</g>
<line x1="250" y1="118" x2="250" y2="135" stroke="#2E7D32" stroke-width="2"/>
<path d="M250,135 L247,130 M250,135 L253,130" stroke="#2E7D32" stroke-width="1.5"/>
<text x="270" y="130" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">Транскрипция</text>
<g transform="translate(250,160)">
<rect x="-40" y="-18" width="80" height="36" rx="5" fill="#9C27B0" opacity="0.2" stroke="#9C27B0" stroke-width="1.5"/>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="10" fill="#9C27B0" text-anchor="middle" font-weight="bold">и-РНК</text>
</g>
<line x1="250" y1="178" x2="250" y2="195" stroke="#2E7D32" stroke-width="2"/>
<path d="M250,195 L247,190 M250,195 L253,190" stroke="#2E7D32" stroke-width="1.5"/>
<text x="270" y="190" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32">Трансляция</text>
<g transform="translate(250,225)">
<rect x="-50" y="-18" width="100" height="36" rx="5" fill="#4CAF50" opacity="0.2" stroke="#4CAF50" stroke-width="1.5"/>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="10" fill="#4CAF50" text-anchor="middle" font-weight="bold">Белок</text>
</g>
'''+ib(30,265,440,40,["Транскрипция: ДНК -> и-РНК (в ядре, РНК-полимераза)","Трансляция: и-РНК -> белок (в рибосоме, т-РНК приносит аминокислоты)","Кодон: 3 нуклеотида = 1 аминокислота | Генетический код: триплетный, вырожденный, универсальный"])+ftr
    elif n == 23:  # Митоз
        svgs[n]=hdr(t,n)+'''
<g transform="translate(65,140)">
<circle cx="0" cy="0" r="25" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1.5"/>
<circle cx="-5" cy="-3" r="8" fill="#CE93D8" opacity="0.5" stroke="#7B1FA2" stroke-width="1"/>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle" font-weight="bold">Профаза</text>
<text x="0" y="48" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">Спирализация</text>
</g>
<g transform="translate(170,140)">
<circle cx="0" cy="0" r="25" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1.5"/>
<line x1="-10" y1="-5" x2="-10" y2="5" stroke="#7B1FA2" stroke-width="2"/>
<line x1="10" y1="-5" x2="10" y2="5" stroke="#7B1FA2" stroke-width="2"/>
<line x1="-18" y1="0" x2="18" y2="0" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle" font-weight="bold">Метафаза</text>
<text x="0" y="48" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">Веретено деления</text>
</g>
<g transform="translate(275,140)">
<circle cx="0" cy="0" r="25" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1.5"/>
<line x1="-18" y1="-10" x2="-5" y2="-3" stroke="#7B1FA2" stroke-width="2"/>
<line x1="18" y1="-10" x2="5" y2="-3" stroke="#7B1FA2" stroke-width="2"/>
<line x1="-18" y1="10" x2="-5" y2="3" stroke="#E53935" stroke-width="2"/>
<line x1="18" y1="10" x2="5" y2="3" stroke="#E53935" stroke-width="2"/>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle" font-weight="bold">Анафаза</text>
<text x="0" y="48" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">Расхождение</text>
</g>
<g transform="translate(380,140)">
<ellipse cx="-15" cy="0" rx="15" ry="20" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1.5"/>
<ellipse cx="15" cy="0" rx="15" ry="20" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1.5"/>
<circle cx="-15" cy="-2" r="5" fill="#CE93D8" opacity="0.5" stroke="#7B1FA2" stroke-width="0.8"/>
<circle cx="15" cy="-2" r="5" fill="#CE93D8" opacity="0.5" stroke="#7B1FA2" stroke-width="0.8"/>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle" font-weight="bold">Телофаза</text>
<text x="0" y="48" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">2 ядра</text>
</g>
'''+ib(30,230,440,60,["Митоз: соматическое деление | 2n -> 2n + 2n | Дочерние клетки идентичны материнской","Фазы: профаза (спирализация) - метафаза (метафазная пластинка) - анафаза (расхождение) - телофаза","Биологическое значение: рост, регенерация, бесполое размножение | 2n=46 (человек)"])+ftr
    elif n == 24:  # Мейоз
        svgs[n]=hdr(t,n)+'''
<g transform="translate(250,175)">
<!-- Meiosis I -->
<text x="-100" y="-70" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Мейоз I</text>
<rect x="-150" y="-60" width="100" height="25" rx="5" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
<text x="-100" y="-43" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">2n (конъюгация)</text>
<line x1="-100" y1="-35" x2="-100" y2="-15" stroke="#2E7D32" stroke-width="1"/>
<path d="M-100,-15 L-103,-10 M-100,-15 L-97,-10" stroke="#2E7D32" stroke-width="1"/>
<rect x="-150" y="-10" width="100" height="20" rx="5" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
<text x="-100" y="4" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Кроссинговер</text>
<line x1="-100" y1="10" x2="-100" y2="25" stroke="#2E7D32" stroke-width="1"/>
<path d="M-100,25 L-103,20 M-100,25 L-97,20" stroke="#2E7D32" stroke-width="1"/>
<rect x="-175" y="30" width="50" height="20" rx="5" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
<text x="-150" y="44" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">n</text>
<rect x="-125" y="30" width="50" height="20" rx="5" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
<text x="-100" y="44" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">n</text>
<!-- Meiosis II -->
<text x="100" y="-70" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">Мейоз II</text>
<rect x="50" y="-60" width="100" height="25" rx="5" fill="#FFE0B2" stroke="#E65100" stroke-width="1"/>
<text x="100" y="-43" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">n (редупликация нет)</text>
<line x1="100" y1="-35" x2="100" y2="-15" stroke="#E65100" stroke-width="1"/>
<path d="M100,-15 L97,-10 M100,-15 L103,-10" stroke="#E65100" stroke-width="1"/>
<rect x="25" y="-10" width="50" height="20" rx="5" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
<text x="50" y="4" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">nc</text>
<rect x="100" y="-10" width="50" height="20" rx="5" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
<text x="125" y="4" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">nc</text>
<line x1="50" y1="10" x2="50" y2="25" stroke="#E65100" stroke-width="1"/>
<line x1="125" y1="10" x2="125" y2="25" stroke="#E65100" stroke-width="1"/>
<rect x="15" y="30" width="35" height="20" rx="5" fill="#FFB74D" stroke="#E65100" stroke-width="1"/>
<text x="32" y="44" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">nc</text>
<rect x="55" y="30" width="35" height="20" rx="5" fill="#FFB74D" stroke="#E65100" stroke-width="1"/>
<text x="72" y="44" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">nc</text>
<rect x="95" y="30" width="35" height="20" rx="5" fill="#FFB74D" stroke="#E65100" stroke-width="1"/>
<text x="112" y="44" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">nc</text>
<rect x="140" y="30" width="35" height="20" rx="5" fill="#FFB74D" stroke="#E65100" stroke-width="1"/>
<text x="157" y="44" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">nc</text>
</g>
'''+ib(30,280,440,30,["Мейоз: 2n -> 4 x nc | Редукционное деление | Гомологичные хромосомы расходятся","Конъюгация + кроссинговер в профазе I | Рекомбинация генетического материала","Значение: образование гамет, генетическое разнообразие"])+ftr
    else:
        # Themed generic SVGs for remaining lessons
        icons = {
        22:"Регуляция генов",25:"Гаметогенез",26:"Оплодотворение",27:"Генетика",
        28:"Сцепление генов",29:"Взаимодействие",30:"Изменчивость",
        31:"Генетика пола",32:"Генетика человека",33:"Эмбриогенез",
        34:"Постэмбриогенез",35:"Биогенет. закон",36:"Обобщение"
        }
        colors = {22:"#7B1FA2",25:"#E53935",26:"#E91E63",27:"#2E7D32",
                  28:"#7B1FA2",29:"#FF9800",30:"#1565C0",
                  31:"#C62828",32:"#795548",33:"#4CAF50",
                  34:"#0097A7",35:"#5D4037",36:"#2E7D32"}
        c = colors.get(n,"#2E7D32")
        sub = icons.get(n,t)
        # Custom info boxes per lesson
        facts = {
        22:["Оперон: промотор + оператор + структурные гены","Индукторы: включают гены | Репрессоры: выключают","Регуляция у прокариот (лактозный оперон) и эукариот"],
        25:["Сперматогенез: 2n -> n (4 сперматозоида)","Овогенез: 2n -> n (1 яйцеклетка + 3 направл. тельца)","Фазы: размножение, рост, созревание (мейоз), формирование"],
        26:["Оплодотворение: слияние гамет -> зигота (2n)","Наружное (вода) и внутреннее (наземные)","Двойное оплодотворение у цветковых растений"],
        27:["Мендель: I - единообразие, II - расщепление 3:1, III - независимое","Анализирующее скрещивание | Неполное доминирование","Генотип + среда = фенотип | Чистота гамет"],
        28:["Морган: сцепление генов в хромосоме","Кроссинговер: обмен участками | 1% = 1 морганида","Группа сцепления = хромосома | У дрозофилы 4 группы"],
        29:["Комплементарность: 9:7 | Эпистаз: 12:3:1 или 9:3:4","Полимерия: кумулятивное действие (цвет кожи)","Плейотропия: один ген - несколько признаков"],
        30:["Мутационная: генные (точковые), хромосомные, геномные","Комбинативная: кроссинговер, независимое расхождение","Модификационная: норма реакции, не наследуется"],
        31:["X-X: женщина | X-Y: мужчина | 44+XX / 44+XY","Сцеплено с X: дальтонизм, гемофилия | С Y: гипертрихоз","X-сцепленные рецессивные: чаще у мужчин"],
        32:["46 хромосом (44 аутосомы + XX/XY)","Методы: генеалогический, близнецовый, цитогенетический","Хромосомные болезни: Даун (21), Клайнфельтер (XXY), Тернер (X0)"],
        33:["Зигота -> бластула -> гаструла -> нейрула -> зародыш","Дробление: бластомеры | Гаструляция: 2-3 слоя","Зародышевые листки: эктодерма, энтодерма, мезодерма"],
        34:["Прямое: яйцо -> взрослая (птицы, рептилии, млекопитающие)","Непрямое: с метаморфозом (лягушка, бабочка)","Личинка: адаптация к разным условиям | Регенерация"],
        35:["Геккель-Мюллер: онтогенез повторяет филогенез","Биогенетический закон: рекапитуляция признаков предков","Онтогенез: от зиготы до смерти | Филогенез: история вида"],
        36:["Клетка: мембрана, ядро, органеллы, цитоплазма","Организм: клетки -> ткани -> органы -> системы","Обмен веществ, самовоспроизведение, развитие, раздражимость"]
        }
        facts_lines = facts.get(n,["Строение и функции","Значение в биологии","Ключевые понятия"])
        svgs[n] = hdr(t,n)+f'''
<g transform="translate(250,170)">
<circle cx="0" cy="0" r="60" fill="{c}" opacity="0.1" stroke="{c}" stroke-width="2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="11" fill="{c}" text-anchor="middle" font-weight="bold">{sub}</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="9" fill="{c}" text-anchor="middle">10 класс</text>
</g>
'''+ib(30,250,440,50,facts_lines)+ftr

for i in range(1,37):
    with open(f"{OUT}/lesson{i}.svg","w") as f:
        f.write(svgs[i])
print(f"Generated {len(svgs)} SVGs for grade 10 biology")
