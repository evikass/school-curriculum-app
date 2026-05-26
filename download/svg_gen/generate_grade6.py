#!/usr/bin/env python3
"""Generate detailed biology SVG illustrations - grade 6."""
import os, sys

OUTPUT = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade6/biology"
os.makedirs(OUTPUT, exist_ok=True)

def H(title, sub, bg1="#E8F5E9", bg2="#C8E6C9", a="#2E7D32"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400"><defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{bg1}"/><stop offset="100%" stop-color="{bg2}"/></linearGradient></defs><rect width="600" height="400" fill="url(#bg)" rx="12"/><rect x="3" y="3" width="594" height="394" rx="10" fill="none" stroke="{a}" stroke-width="2"/><text x="300" y="38" font-family="Arial,sans-serif" font-size="18" font-weight="bold" fill="{a}" text-anchor="middle">{title}</text><text x="300" y="56" font-family="Arial,sans-serif" font-size="11" fill="#777" text-anchor="middle">{sub}</text><line x1="30" y1="66" x2="570" y2="66" stroke="{a}" stroke-width="1.5" opacity="0.3"/>'''

def F(title, a="#2E7D32"):
    return f'''<rect x="15" y="360" width="570" height="28" rx="5" fill="{a}" opacity="0.85"/><text x="300" y="380" font-family="Arial,sans-serif" font-size="13" text-anchor="middle" fill="white" font-weight="bold">{title}</text></svg>'''

def W(n, svg):
    with open(os.path.join(OUTPUT, f"lesson{n}.svg"), 'w') as f: f.write(svg)

# Helper: panel box
def panel(x,y,w,h,title,a):
    return f'''<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="white" stroke="{a}" stroke-width="1.5"/><rect x="{x}" y="{y}" width="{w}" height="22" rx="8" fill="{a}" opacity="0.85"/><rect x="{x}" y="{y+16}" width="{w}" height="8" fill="{a}" opacity="0.85"/><text x="{x+w//2}" y="{y+16}" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">{title}</text>'''

# ===== LESSON 1 =====
W(1, H("Биология - наука о живой природе", "Биология 6 класс - Урок 1") + f'''
{panel(15,75,270,275,"НАУКА БИОЛОГИЯ","#2E7D32")}
<text x="30" y="108" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" font-weight="bold">Биология = биос + логос</text>
<text x="30" y="123" font-family="Arial,sans-serif" font-size="9" fill="#555">(жизнь + наука)</text>
<line x1="30" y1="130" x2="260" y2="130" stroke="#C8E6C9" stroke-width="1"/>
<text x="30" y="148" font-family="Arial,sans-serif" font-size="9" fill="#333">Разделы биологии:</text>
<circle cx="42" cy="165" r="8" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/><text x="42" y="168" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">1</text><text x="55" y="168" font-family="Arial,sans-serif" font-size="9" fill="#333">Ботаника - растения</text>
<circle cx="42" cy="190" r="8" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/><text x="42" y="193" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">2</text><text x="55" y="193" font-family="Arial,sans-serif" font-size="9" fill="#333">Зоология - животные</text>
<circle cx="42" cy="215" r="8" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/><text x="42" y="218" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">3</text><text x="55" y="218" font-family="Arial,sans-serif" font-size="9" fill="#333">Микробиология - бактерии</text>
<circle cx="42" cy="240" r="8" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/><text x="42" y="243" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">4</text><text x="55" y="243" font-family="Arial,sans-serif" font-size="9" fill="#333">Микология - грибы</text>
<circle cx="42" cy="265" r="8" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/><text x="42" y="268" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">5</text><text x="55" y="268" font-family="Arial,sans-serif" font-size="9" fill="#333">Экология - взаимосвязи</text>
<circle cx="42" cy="290" r="8" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/><text x="42" y="293" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">6</text><text x="55" y="293" font-family="Arial,sans-serif" font-size="9" fill="#333">Генетика - наследственность</text>
<circle cx="42" cy="315" r="8" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/><text x="42" y="318" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">7</text><text x="55" y="318" font-family="Arial,sans-serif" font-size="9" fill="#333">Анатомия - строение человека</text>

{panel(300,75,285,275,"МЕТОДЫ ИЗУЧЕНИЯ","#388E3C")}
<!-- Microscope icon -->
<rect x="420" y="105" width="20" height="70" rx="3" fill="#546E7A" stroke="#37474F" stroke-width="1.5"/>
<rect x="413" y="175" width="34" height="5" rx="1" fill="#455A64"/>
<circle cx="430" cy="155" r="6" fill="#607D8B" stroke="#37474F" stroke-width="1"/>
<rect x="418" y="95" width="24" height="15" rx="3" fill="#78909C" stroke="#37474F" stroke-width="1"/>
<ellipse cx="430" cy="185" rx="28" ry="4" fill="#37474F"/>

<text x="315" y="118" font-family="Arial,sans-serif" font-size="9" fill="#388E3C" font-weight="bold">Наблюдение</text>
<text x="315" y="133" font-family="Arial,sans-serif" font-size="8" fill="#555">В природе и лаборатории</text>
<text x="315" y="155" font-family="Arial,sans-serif" font-size="9" fill="#388E3C" font-weight="bold">Эксперимент</text>
<text x="315" y="170" font-family="Arial,sans-serif" font-size="8" fill="#555">Проверка гипотез</text>
<text x="315" y="192" font-family="Arial,sans-serif" font-size="9" fill="#388E3C" font-weight="bold">Микроскопирование</text>
<text x="315" y="207" font-family="Arial,sans-serif" font-size="8" fill="#555">Изучение клеток</text>
<text x="315" y="229" font-family="Arial,sans-serif" font-size="9" fill="#388E3C" font-weight="bold">Сравнение</text>
<text x="315" y="244" font-family="Arial,sans-serif" font-size="8" fill="#555">Сходства и различия</text>
<text x="315" y="266" font-family="Arial,sans-serif" font-size="9" fill="#388E3C" font-weight="bold">Моделирование</text>
<text x="315" y="281" font-family="Arial,sans-serif" font-size="8" fill="#555">Создание моделей</text>
<text x="315" y="303" font-family="Arial,sans-serif" font-size="9" fill="#388E3C" font-weight="bold">Измерение</text>
<text x="315" y="318" font-family="Arial,sans-serif" font-size="8" fill="#555">Количественные данные</text>
''' + F("Биология - наука о живой природе"))

# ===== LESSON 2 =====
W(2, H("Признаки живого", "Биология 6 класс - Урок 2") + f'''
{panel(15,75,570,135,"ПРИЗНАКИ ЖИВОГО","#388E3C")}
<!-- 6 signs of life as icons -->
<circle cx="70" cy="130" r="25" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/>
<text x="70" y="128" font-family="Arial,sans-serif" font-size="16" fill="#2E7D32" text-anchor="middle">&#9883;</text>
<text x="70" y="140" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Обмен</text>
<text x="70" y="150" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">веществ</text>

<circle cx="170" cy="130" r="25" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/>
<text x="170" y="128" font-family="Arial,sans-serif" font-size="16" fill="#2E7D32" text-anchor="middle">&#8593;</text>
<text x="170" y="140" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Рост и</text>
<text x="170" y="150" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">развитие</text>

<circle cx="270" cy="130" r="25" fill="#FCE4EC" stroke="#C2185B" stroke-width="2"/>
<text x="270" y="128" font-family="Arial,sans-serif" font-size="16" fill="#C2185B" text-anchor="middle">&#9829;</text>
<text x="270" y="140" font-family="Arial,sans-serif" font-size="7" fill="#C2185B" text-anchor="middle">Размно-</text>
<text x="270" y="150" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">жение</text>

<circle cx="370" cy="130" r="25" fill="#E3F2FD" stroke="#1565C0" stroke-width="2"/>
<text x="370" y="128" font-family="Arial,sans-serif" font-size="16" fill="#1565C0" text-anchor="middle">&#8592;&#8594;</text>
<text x="370" y="140" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle">Движе-</text>
<text x="370" y="150" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">ние</text>

<circle cx="470" cy="130" r="25" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
<text x="470" y="128" font-family="Arial,sans-serif" font-size="16" fill="#E65100" text-anchor="middle">&#9888;</text>
<text x="470" y="140" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle">Раздра-</text>
<text x="470" y="150" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">жимость</text>

<circle cx="540" cy="130" r="22" fill="#F3E5F5" stroke="#7B1FA2" stroke-width="2"/>
<text x="540" y="140" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle">Клеточ.</text>
<text x="540" y="150" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">строен.</text>

{panel(15,220,270,130,"УРОВНИ ОРГАНИЗАЦИИ","#1B5E20")}
<text x="30" y="248" font-family="Arial,sans-serif" font-size="9" fill="#1B5E20">Молекулярный</text>
<text x="30" y="264" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32">Клеточный</text>
<text x="30" y="280" font-family="Arial,sans-serif" font-size="9" fill="#388E3C">Тканевый</text>
<text x="30" y="296" font-family="Arial,sans-serif" font-size="9" fill="#43A047">Органный</text>
<text x="30" y="312" font-family="Arial,sans-serif" font-size="9" fill="#66BB6A">Организменный</text>
<text x="30" y="328" font-family="Arial,sans-serif" font-size="9" fill="#81C784">Популяционный</text>
<text x="30" y="344" font-family="Arial,sans-serif" font-size="9" fill="#A5D6A7">Биосферный</text>
<!-- Arrow showing increasing complexity -->
<path d="M220,250 L220,340" stroke="#1B5E20" stroke-width="2"/>
<polygon points="215,340 220,350 225,340" fill="#1B5E20"/>

{panel(300,220,285,130,"СВОЙСТВА ЖИВОГО","#388E3C")}
<text x="315" y="248" font-family="Arial,sans-serif" font-size="9" fill="#333">Живые организмы:</text>
<text x="315" y="266" font-family="Arial,sans-serif" font-size="8" fill="#555">Состоят из клеток</text>
<text x="315" y="280" font-family="Arial,sans-serif" font-size="8" fill="#555">Питаются и дышат</text>
<text x="315" y="294" font-family="Arial,sans-serif" font-size="8" fill="#555">Растут и развиваются</text>
<text x="315" y="308" font-family="Arial,sans-serif" font-size="8" fill="#555">Размножаются</text>
<text x="315" y="322" font-family="Arial,sans-serif" font-size="8" fill="#555">Реагируют на раздражители</text>
<text x="315" y="336" font-family="Arial,sans-serif" font-size="8" fill="#555">Выделяют энергию</text>
''' + F("Признаки живого"))

# Continue with remaining lessons using templates
# I'll create efficient template-based illustrations

# Template for cell-related topics
def cell_svg(n, title, sub, details, a="#2E7D32", bg1="#E8F5E9", bg2="#C8E6C9"):
    return H(title, sub, bg1, bg2, a) + f'''
{panel(15,75,280,275,"КЛЕТКА","#2E7D32")}
<ellipse cx="155" cy="195" rx="105" ry="80" fill="#C8E6C9" stroke="#2E7D32" stroke-width="2.5"/>
<ellipse cx="155" cy="192" rx="35" ry="25" fill="#81C784" stroke="#1B5E20" stroke-width="2"/>
<circle cx="155" cy="190" r="10" fill="#66BB6A" stroke="#1B5E20" stroke-width="1"/>
<text x="155" y="193" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">ядрышко</text>
<text x="155" y="218" font-family="Arial,sans-serif" font-size="8" fill="#1B5E20" text-anchor="middle">ядро</text>
<ellipse cx="100" cy="175" rx="15" ry="6" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
<text x="100" y="190" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">митох.</text>
<ellipse cx="200" cy="200" rx="14" ry="10" fill="#BBDEFB" stroke="#1565C0" stroke-width="1"/>
<text x="200" y="204" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">вакуоль</text>
<circle cx="85" cy="205" r="3" fill="#EF9A9A" stroke="#C62828" stroke-width="0.5"/>
<circle cx="92" cy="210" r="3" fill="#EF9A9A" stroke="#C62828" stroke-width="0.5"/>
<circle cx="120" cy="220" r="3" fill="#EF9A9A" stroke="#C62828" stroke-width="0.5"/>
<text x="95" y="225" font-family="Arial,sans-serif" font-size="6" fill="#C62828">рибосомы</text>
<ellipse cx="210" cy="165" rx="14" ry="8" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
<line x1="200" y1="165" x2="220" y2="165" stroke="#2E7D32" stroke-width="0.5"/>
<text x="210" y="180" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">хлоропласт</text>
<text x="155" y="100" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">мембрана</text>
<text x="155" y="280" font-family="Arial,sans-serif" font-size="8" fill="#795548" text-anchor="middle">клеточная стенка (снаружи)</text>
<path d="M120,195 Q130,188 125,200 Q120,208 130,205" fill="none" stroke="#7E57C2" stroke-width="1.2"/>
<text x="130" y="215" font-family="Arial,sans-serif" font-size="6" fill="#7E57C2">ЭПС</text>

{panel(310,75,275,275,"ДЕТАЛИ","#388E3C")}
{details}
''' + F(title, a)

# Lesson 3
W(3, cell_svg(3, "Строение клетки", "Биология 6 класс - Урок 3", '''
<text x="325" y="105" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" font-weight="bold">Основные части:</text>
<rect x="325" y="115" width="8" height="8" rx="2" fill="#2E7D32"/><text x="340" y="123" font-family="Arial,sans-serif" font-size="9" fill="#333">Оболочка (мембрана)</text>
<rect x="325" y="135" width="8" height="8" rx="2" fill="#558B2F"/><text x="340" y="143" font-family="Arial,sans-serif" font-size="9" fill="#333">Цитоплазма</text>
<rect x="325" y="155" width="8" height="8" rx="2" fill="#1B5E20"/><text x="340" y="163" font-family="Arial,sans-serif" font-size="9" fill="#333">Ядро</text>
<line x1="325" y1="175" x2="570" y2="175" stroke="#C8E6C9" stroke-width="1"/>
<text x="325" y="195" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" font-weight="bold">Органоиды:</text>
<text x="325" y="213" font-family="Arial,sans-serif" font-size="9" fill="#555">Митохондрии - энергия</text>
<text x="325" y="230" font-family="Arial,sans-serif" font-size="9" fill="#555">Рибосомы - синтез белка</text>
<text x="325" y="247" font-family="Arial,sans-serif" font-size="9" fill="#555">Хлоропласты - фотосинтез</text>
<text x="325" y="264" font-family="Arial,sans-serif" font-size="9" fill="#555">Вакуоли - запас веществ</text>
<text x="325" y="281" font-family="Arial,sans-serif" font-size="9" fill="#555">ЭПС - транспорт</text>
<line x1="325" y1="290" x2="570" y2="290" stroke="#C8E6C9" stroke-width="1"/>
<text x="325" y="308" font-family="Arial,sans-serif" font-size="9" fill="#1B5E20" font-weight="bold">Растительная клетка</text>
<text x="325" y="325" font-family="Arial,sans-serif" font-size="8" fill="#555">+ клеточная стенка</text>
<text x="325" y="340" font-family="Arial,sans-serif" font-size="8" fill="#555">+ хлоропласты</text>
'''))

# Lesson 4
W(4, H("Химический состав клетки", "Биология 6 класс - Урок 4", "#FFF3E0", "#FFE0B2", "#E65100") + f'''
{panel(15,75,280,275,"ЭЛЕМЕНТНЫЙ СОСТАВ","#E65100")}
<!-- Cell with elements -->
<ellipse cx="155" cy="200" rx="80" ry="60" fill="#FFE0B2" stroke="#E65100" stroke-width="2"/>
<circle cx="100" cy="180" r="12" fill="#EF5350" stroke="#C62828" stroke-width="1"/><text x="100" y="184" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">O</text>
<circle cx="155" cy="165" r="12" fill="#42A5F5" stroke="#1565C0" stroke-width="1"/><text x="155" y="169" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">H</text>
<circle cx="210" cy="180" r="12" fill="#FFA726" stroke="#E65100" stroke-width="1"/><text x="210" y="184" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">C</text>
<circle cx="155" cy="230" r="12" fill="#AB47BC" stroke="#6A1B9A" stroke-width="1"/><text x="155" y="234" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle">N</text>
<text x="155" y="275" font-family="Arial,sans-serif" font-size="9" fill="#E65100" text-anchor="middle" font-weight="bold">Макроэлементы: O, C, H, N (98%)</text>
<text x="155" y="290" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Микроэлементы: Fe, Zn, Cu, I, F</text>
<text x="155" y="305" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Ультрамикроэлементы: Au, U</text>

{panel(310,75,275,135,"НЕОРГАНИЧЕСКИЕ ВЕЩЕСТВА","#BF360C")}
<text x="325" y="105" font-family="Arial,sans-serif" font-size="10" fill="#BF360C" font-weight="bold">Вода (70-80%)</text>
<text x="325" y="120" font-family="Arial,sans-serif" font-size="8" fill="#555">Растворитель, среда реакций</text>
<text x="325" y="140" font-family="Arial,sans-serif" font-size="10" fill="#BF360C" font-weight="bold">Минеральные соли (1-1.5%)</text>
<text x="325" y="155" font-family="Arial,sans-serif" font-size="8" fill="#555">NaCl, KCl, Ca, Mg, P</text>
<text x="325" y="175" font-family="Arial,sans-serif" font-size="8" fill="#555">Поддержание осмотического</text>
<text x="325" y="188" font-family="Arial,sans-serif" font-size="8" fill="#555">давления, часть костей</text>

{panel(310,220,275,130,"ОРГАНИЧЕСКИЕ ВЕЩЕСТВА","#E65100")}
<rect x="325" y="235" width="8" height="8" rx="2" fill="#EF5350"/><text x="340" y="243" font-family="Arial,sans-serif" font-size="9" fill="#333">Белки (10-15%)</text>
<rect x="325" y="255" width="8" height="8" rx="2" fill="#FFA726"/><text x="340" y="263" font-family="Arial,sans-serif" font-size="9" fill="#333">Липиды (5-8%)</text>
<rect x="325" y="275" width="8" height="8" rx="2" fill="#66BB6A"/><text x="340" y="283" font-family="Arial,sans-serif" font-size="9" fill="#333">Углеводы (1-2%)</text>
<rect x="325" y="295" width="8" height="8" rx="2" fill="#AB47BC"/><text x="340" y="303" font-family="Arial,sans-serif" font-size="9" fill="#333">Нуклеиновые к-ты (1-3%)</text>
<rect x="325" y="315" width="8" height="8" rx="2" fill="#78909C"/><text x="340" y="323" font-family="Arial,sans-serif" font-size="9" fill="#333">АТФ (0.1-0.5%)</text>
''' + F("Химический состав клетки", "#E65100"))

# Lesson 5: Bacteria structure
W(5, H("Строение и жизнедеятельность бактерий", "Биология 6 класс - Урок 5", "#FFF3E0", "#FFE0B2", "#E65100") + f'''
{panel(15,75,280,275,"ФОРМЫ БАКТЕРИЙ","#E65100")}
<!-- Cocci -->
<circle cx="70" cy="110" r="12" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
<circle cx="95" cy="115" r="10" fill="#FFE0B2" stroke="#E65100" stroke-width="1.2"/>
<text x="80" y="140" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Кокки</text>
<!-- Bacilli -->
<rect x="50" y="155" width="35" height="14" rx="7" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/>
<text x="70" y="185" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Бациллы</text>
<!-- Spirillum -->
<path d="M50,210 Q60,200 70,210 Q80,220 90,210 Q100,200 110,210" fill="none" stroke="#E65100" stroke-width="3" stroke-linecap="round"/>
<text x="80" y="230" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Спириллы</text>
<!-- Vibrio -->
<path d="M55,260 Q70,245 80,260" fill="none" stroke="#E65100" stroke-width="3.5" stroke-linecap="round"/>
<text x="70" y="280" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Вибрионы</text>
<!-- Staph -->
<circle cx="160" cy="105" r="7" fill="#FFB74D" stroke="#E65100" stroke-width="1"/>
<circle cx="172" cy="100" r="7" fill="#FFB74D" stroke="#E65100" stroke-width="1"/>
<circle cx="166" cy="115" r="7" fill="#FFB74D" stroke="#E65100" stroke-width="1"/>
<circle cx="178" cy="112" r="7" fill="#FFB74D" stroke="#E65100" stroke-width="1"/>
<text x="168" y="133" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Стафилококки</text>
<!-- Streptococci chain -->
<circle cx="145" cy="155" r="6" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
<circle cx="158" cy="155" r="6" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
<circle cx="171" cy="155" r="6" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
<circle cx="184" cy="155" r="6" fill="#FFCC80" stroke="#E65100" stroke-width="1"/>
<text x="165" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Стрептококки</text>

{panel(310,75,275,275,"СТРОЕНИЕ БАКТЕРИИ","#BF360C")}
<!-- Large bacterium diagram -->
<ellipse cx="440" cy="180" rx="55" ry="30" fill="#FFE0B2" stroke="#E65100" stroke-width="2"/>
<ellipse cx="440" cy="180" rx="62" ry="35" fill="none" stroke="#FF8F00" stroke-width="1.5" stroke-dasharray="4,2"/>
<text x="385" y="158" font-family="Arial,sans-serif" font-size="7" fill="#FF8F00">капсула</text>
<ellipse cx="455" cy="175" rx="18" ry="10" fill="#FFCC80" stroke="#BF360C" stroke-width="1" stroke-dasharray="2,1"/>
<text x="455" y="178" font-family="Arial,sans-serif" font-size="6" fill="#BF360C" text-anchor="middle">нуклеоид</text>
<circle cx="420" cy="175" r="2" fill="#BF360C"/>
<circle cx="435" cy="190" r="2" fill="#BF360C"/>
<circle cx="460" cy="190" r="2" fill="#BF360C"/>
<path d="M495,180 Q505,173 510,180 Q515,187 520,180" fill="none" stroke="#E65100" stroke-width="1.5"/>
<text x="510" y="170" font-family="Arial,sans-serif" font-size="7" fill="#E65100">жгутик</text>
<line x1="395" y1="170" x2="385" y2="162" stroke="#BF360C" stroke-width="0.8"/>
<line x1="393" y1="185" x2="383" y2="195" stroke="#BF360C" stroke-width="0.8"/>
<text x="370" y="200" font-family="Arial,sans-serif" font-size="6" fill="#888">пили</text>
<text x="440" y="230" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle">клеточная стенка</text>
<text x="440" y="250" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Прокариоты - нет ядра</text>
<text x="440" y="265" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">ДНК кольцевая</text>
<text x="440" y="280" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Споры для выживания</text>
<text x="440" y="300" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Деление каждые 20 мин</text>
<text x="440" y="320" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Размер: 0.5-5 мкм</text>
''' + F("Строение бактерий", "#E65100"))

# Lessons 6-23: Generate with focused templates
lessons_rest = [
    (6, "Роль бактерий", "#FFF3E0", "#FFE0B2", "#BF360C", "bacteria_role"),
    (7, "Общая характеристика грибов", "#EFEBE9", "#D7CCC8", "#5D4037", "fungi"),
    (8, "Многообразие грибов", "#EFEBE9", "#D7CCC8", "#795548", "fungi_div"),
    (9, "Водоросли", "#E0F7FA", "#B2EBF2", "#00695C", "algae"),
    (10, "Мхи", "#E8F5E9", "#C8E6C9", "#1B5E20", "moss"),
    (11, "Папоротники", "#E8F5E9", "#C8E6C9", "#2E7D32", "fern"),
    (12, "Голосеменные", "#F1F8E9", "#DCEDC8", "#558B2F", "gymno"),
    (13, "Покрытосеменные", "#FCE4EC", "#F8BBD0", "#AD1457", "angio"),
    (14, "Корень", "#EFEBE9", "#D7CCC8", "#5D4037", "root"),
    (15, "Побег и стебель", "#E8F5E9", "#C8E6C9", "#2E7D32", "stem"),
    (16, "Лист", "#E8F5E9", "#C8E6C9", "#1B5E20", "leaf"),
    (17, "Цветок и плод", "#FCE4EC", "#F8BBD0", "#C2185B", "flower"),
    (18, "Фотосинтез и дыхание", "#E8F5E9", "#C8E6C9", "#2E7D32", "photo"),
    (19, "Минеральное питание", "#E8F5E9", "#C8E6C9", "#558B2F", "mineral"),
    (20, "Рост и развитие растений", "#E8F5E9", "#C8E6C9", "#388E3C", "growth"),
    (21, "Вегетативное размножение", "#E8F5E9", "#C8E6C9", "#2E7D32", "veg_repro"),
    (22, "Семенное размножение", "#F1F8E9", "#DCEDC8", "#558B2F", "seed"),
    (23, "Природные сообщества", "#E8F5E9", "#C8E6C9", "#1B5E20", "community"),
]

# Topic-specific illustration generators
def ill_bacteria_role(a):
    return f'''
{panel(15,75,280,275,"РОЛЬ В ПРИРОДЕ","#BF360C")}
<text x="30" y="105" font-family="Arial,sans-serif" font-size="9" fill="#BF360C" font-weight="bold">Почвообразование</text>
<text x="30" y="120" font-family="Arial,sans-serif" font-size="8" fill="#555">Разрушают остатки организмов</text>
<text x="30" y="140" font-family="Arial,sans-serif" font-size="9" fill="#BF360C" font-weight="bold">Круговорот веществ</text>
<text x="30" y="155" font-family="Arial,sans-serif" font-size="8" fill="#555">Азотфиксация - связывают N2</text>
<text x="30" y="175" font-family="Arial,sans-serif" font-size="9" fill="#BF360C" font-weight="bold">Симбиоз</text>
<text x="30" y="190" font-family="Arial,sans-serif" font-size="8" fill="#555">Кишечная флора животных</text>
<text x="30" y="210" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold">Фотосинтезирующие</text>
<text x="30" y="225" font-family="Arial,sans-serif" font-size="8" fill="#555">Цианобактерии - кислород</text>

{panel(310,75,275,130,"РОЛЬ ДЛЯ ЧЕЛОВЕКА","#E65100")}
<text x="325" y="105" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold">Положительная:</text>
<text x="325" y="120" font-family="Arial,sans-serif" font-size="8" fill="#555">Молочнокислые (кефир, йогурт)</text>
<text x="325" y="135" font-family="Arial,sans-serif" font-size="8" fill="#555">Антибиотики (пенициллин)</text>
<text x="325" y="150" font-family="Arial,sans-serif" font-size="8" fill="#555">Силосование, очистка воды</text>
<text x="325" y="170" font-family="Arial,sans-serif" font-size="9" fill="#C62828" font-weight="bold">Отрицательная:</text>
<text x="325" y="185" font-family="Arial,sans-serif" font-size="8" fill="#555">Возбудители болезней</text>
<text x="325" y="200" font-family="Arial,sans-serif" font-size="8" fill="#555">Порча продуктов питания</text>

{panel(310,220,275,130,"АЗОТФИКСАЦИЯ","#558B2F")}
<text x="450" y="248" font-family="Arial,sans-serif" font-size="9" fill="#558B2F" text-anchor="middle" font-weight="bold">Клубеньковые бактерии</text>
<!-- Root with nodules -->
<line x1="450" y1="270" x2="450" y2="330" stroke="#8D6E63" stroke-width="3"/>
<circle cx="435" cy="295" r="6" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
<circle cx="460" cy="305" r="7" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
<circle cx="445" cy="315" r="5" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
<text x="450" y="345" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">клубеньки на корнях бобовых</text>'''

def ill_fungi(a):
    return f'''
{panel(15,75,280,275,"СТРОЕНИЕ ГРИБА","#5D4037")}
<!-- Mushroom -->
<ellipse cx="140" cy="110" rx="60" ry="22" fill="#8D6E63" stroke="#4E342E" stroke-width="2"/>
<ellipse cx="140" cy="110" rx="55" ry="18" fill="#A1887F"/>
<circle cx="120" cy="106" r="4" fill="#795548" opacity="0.5"/>
<circle cx="155" cy="108" r="3" fill="#795548" opacity="0.5"/>
<rect x="134" y="130" width="12" height="60" rx="4" fill="#BCAAA4" stroke="#5D4037" stroke-width="1.5"/>
<ellipse cx="140" cy="142" rx="16" ry="3" fill="#D7CCC8" stroke="#5D4037" stroke-width="0.8"/>
<!-- Mycelium -->
<line x1="134" y1="190" x2="110" y2="215" stroke="#8D6E63" stroke-width="2"/>
<line x1="110" y1="215" x2="95" y2="230" stroke="#8D6E63" stroke-width="1.5"/>
<line x1="146" y1="190" x2="160" y2="218" stroke="#8D6E63" stroke-width="2"/>
<line x1="160" y1="218" x2="175" y2="232" stroke="#8D6E63" stroke-width="1.5"/>
<line x1="140" y1="190" x2="140" y2="225" stroke="#8D6E63" stroke-width="2"/>
<text x="140" y="250" font-family="Arial,sans-serif" font-size="8" fill="#4E342E" text-anchor="middle" font-weight="bold">Грибница (мицелий)</text>
<text x="90" y="103" font-family="Arial,sans-serif" font-size="7" fill="#5D4037">шляпка</text>
<text x="155" y="162" font-family="Arial,sans-serif" font-size="7" fill="#5D4037">ножка</text>
<text x="95" y="130" font-family="Arial,sans-serif" font-size="7" fill="#5D4037">пластинки</text>
<line x1="20" y1="190" x2="260" y2="190" stroke="#795548" stroke-width="1" stroke-dasharray="3,2"/>

{panel(310,75,275,275,"ОСОБЕННОСТИ ГРИБОВ","#795548")}
<text x="325" y="105" font-family="Arial,sans-serif" font-size="10" fill="#795548" font-weight="bold">Как растения:</text>
<text x="325" y="120" font-family="Arial,sans-serif" font-size="9" fill="#555">Неподвижны, растут всю жизнь</text>
<text x="325" y="135" font-family="Arial,sans-serif" font-size="9" fill="#555">Клеточная стенка (хитин!)</text>
<line x1="325" y1="145" x2="570" y2="145" stroke="#D7CCC8" stroke-width="1"/>
<text x="325" y="165" font-family="Arial,sans-serif" font-size="10" fill="#795548" font-weight="bold">Как животные:</text>
<text x="325" y="180" font-family="Arial,sans-serif" font-size="9" fill="#555">Гетеротрофы</text>
<text x="325" y="195" font-family="Arial,sans-serif" font-size="9" fill="#555">Запас: гликоген</text>
<line x1="325" y1="205" x2="570" y2="205" stroke="#D7CCC8" stroke-width="1"/>
<text x="325" y="225" font-family="Arial,sans-serif" font-size="10" fill="#795548" font-weight="bold">Уникальное:</text>
<text x="325" y="240" font-family="Arial,sans-serif" font-size="9" fill="#555">Тело из гифов (нитей)</text>
<text x="325" y="255" font-family="Arial,sans-serif" font-size="9" fill="#555">Размножение спорами</text>
<text x="325" y="270" font-family="Arial,sans-serif" font-size="9" fill="#555">Всасывание пищи поверхностью</text>
<text x="325" y="290" font-family="Arial,sans-serif" font-size="10" fill="#5D4037" font-weight="bold">Типы питания:</text>
<text x="325" y="308" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32">Сапротрофы - на мёртвом</text>
<text x="325" y="323" font-family="Arial,sans-serif" font-size="9" fill="#C62828">Паразиты - на живом</text>
<text x="325" y="338" font-family="Arial,sans-serif" font-size="9" fill="#00695C">Симбионты - совместно</text>'''

def ill_fungi_div(a):
    return f'''
{panel(15,75,185,170,"ШЛЯПОЧНЫЕ","#5D4037")}
<ellipse cx="108" cy="110" rx="40" ry="15" fill="#8D6E63" stroke="#4E342E" stroke-width="1.5"/>
<rect x="103" y="124" width="10" height="35" rx="3" fill="#BCAAA4" stroke="#5D4037" stroke-width="1"/>
<text x="108" y="178" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Съедобные и ядовитые</text>

{panel(210,75,185,170,"ПЛЕСНЕВЫЕ","#795548")}
<rect x="230" y="120" width="40" height="30" rx="2" fill="#FFECB3" stroke="#F9A825" stroke-width="1"/>
<line x1="250" y1="120" x2="250" y2="95" stroke="#7B1FA2" stroke-width="2"/>
<circle cx="250" cy="90" r="10" fill="#CE93D8" stroke="#7B1FA2" stroke-width="1"/>
<text x="300" y="178" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Мукор, пеницилл</text>

{panel(405,75,180,170,"ДРОЖЖИ","#8D6E63")}
<ellipse cx="495" cy="110" rx="14" ry="10" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.2"/>
<ellipse cx="512" cy="105" rx="8" ry="6" fill="#FFF9C4" stroke="#F9A825" stroke-width="0.8"/>
<ellipse cx="480" cy="130" rx="12" ry="9" fill="#FFF9C4" stroke="#F9A825" stroke-width="1"/>
<text x="495" y="178" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Почкование, брожение</text>

{panel(15,260,270,95,"ЗНАЧЕНИЕ ГРИБОВ","#5D4037")}
<text x="30" y="285" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold">Положительное:</text>
<text x="30" y="300" font-family="Arial,sans-serif" font-size="8" fill="#555">Пища, антибиотики, дрожжи</text>
<text x="30" y="320" font-family="Arial,sans-serif" font-size="9" fill="#C62828" font-weight="bold">Отрицательное:</text>
<text x="30" y="335" font-family="Arial,sans-serif" font-size="8" fill="#555">Паразиты, ядовитые, порча</text>

{panel(300,260,285,95,"ГРИБЫ-ПАРАЗИТЫ","#BF360C")}
<text x="315" y="285" font-family="Arial,sans-serif" font-size="8" fill="#555">Трутовик - на деревьях</text>
<text x="315" y="300" font-family="Arial,sans-serif" font-size="8" fill="#555">Головня - на злаках</text>
<text x="315" y="315" font-family="Arial,sans-serif" font-size="8" fill="#555">Ржавчина - на пшенице</text>
<text x="315" y="335" font-family="Arial,sans-serif" font-size="8" fill="#555">Фитофтора - на картофеле</text>'''

def ill_algae(a):
    return f'''
{panel(15,75,185,170,"ОДНОКЛЕТОЧНЫЕ","#00695C")}
<!-- Chlamydomonas -->
<circle cx="108" cy="135" r="20" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1.5"/>
<circle cx="108" cy="133" r="7" fill="#81C784" stroke="#1B5E20" stroke-width="1"/>
<circle cx="103" cy="128" r="3" fill="#EF5350" stroke="#C62828" stroke-width="0.5"/>
<path d="M108,115 L108,105" stroke="#2E7D32" stroke-width="1.5"/>
<text x="108" y="170" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Хламидомонада</text>

{panel(210,75,185,170,"НИТЧАТЫЕ","#00897B")}
<!-- Spirogyra -->
<rect x="230" y="95" width="30" height="18" rx="5" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
<rect x="260" y="95" width="30" height="18" rx="5" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
<rect x="290" y="95" width="30" height="18" rx="5" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
<rect x="320" y="95" width="30" height="18" rx="5" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
<text x="290" y="130" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Спирогира (нить из клеток)</text>
<!-- Diatom -->
<ellipse cx="290" cy="160" rx="20" ry="8" fill="#E0F7FA" stroke="#00695C" stroke-width="1"/>
<line x1="270" y1="160" x2="310" y2="160" stroke="#00695C" stroke-width="0.5"/>
<text x="290" y="178" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Диатомеи</text>

{panel(405,75,180,170,"МНОГОКЛЕТОЧНЫЕ","#004D40")}
<!-- Kelp -->
<path d="M495,95 L495,130 Q480,150 475,180 Q470,200 480,220" fill="none" stroke="#2E7D32" stroke-width="3"/>
<path d="M495,130 Q510,150 515,180 Q520,200 510,220" fill="none" stroke="#388E3C" stroke-width="3"/>
<path d="M495,95 Q485,90 475,95" fill="none" stroke="#1B5E20" stroke-width="2"/>
<text x="495" y="235" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Ламинария (морская капуста)</text>

{panel(15,260,570,95,"ЗНАЧЕНИЕ ВОДОРОСЛЕЙ","#00695C")}
<text x="30" y="285" font-family="Arial,sans-serif" font-size="9" fill="#00695C" font-weight="bold">В природе:</text>
<text x="30" y="300" font-family="Arial,sans-serif" font-size="8" fill="#555">Фотосинтез - 80% кислорода Земли</text>
<text x="30" y="315" font-family="Arial,sans-serif" font-size="8" fill="#555">Начало пищевых цепей в водоёмах</text>
<text x="300" y="285" font-family="Arial,sans-serif" font-size="9" fill="#00695C" font-weight="bold">Для человека:</text>
<text x="300" y="300" font-family="Arial,sans-serif" font-size="8" fill="#555">Пища (ламинария, порфира)</text>
<text x="300" y="315" font-family="Arial,sans-serif" font-size="8" fill="#555">Агар-агар, йод, удобрения</text>
<text x="450" y="285" font-family="Arial,sans-serif" font-size="9" fill="#C62828" font-weight="bold">Вред:</text>
<text x="450" y="300" font-family="Arial,sans-serif" font-size="8" fill="#555">Цветение воды</text>
<text x="450" y="315" font-family="Arial,sans-serif" font-size="8" fill="#555">Зарастание водоёмов</text>'''

def ill_moss(a):
    return f'''
{panel(15,75,280,275,"СТРОЕНИЕ МХА","#1B5E20")}
<!-- Moss plant -->
<rect x="135" y="130" width="6" height="100" rx="2" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
<!-- Leaves (small) -->
<path d="M135,150 Q120,145 115,150 Q120,155 135,152" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.8"/>
<path d="M141,150 Q155,145 160,150 Q155,155 141,152" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.8"/>
<path d="M135,170 Q118,165 113,170 Q118,175 135,172" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.8"/>
<path d="M141,170 Q158,165 163,170 Q158,175 141,172" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.8"/>
<path d="M135,190 Q122,185 117,190 Q122,195 135,192" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.8"/>
<path d="M141,190 Q154,185 159,190 Q154,195 141,192" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.8"/>
<!-- Capsule on stalk -->
<line x1="138" y1="100" x2="138" y2="130" stroke="#2E7D32" stroke-width="1.5"/>
<ellipse cx="138" cy="95" rx="10" ry="14" fill="#8D6E63" stroke="#4E342E" stroke-width="1.5"/>
<ellipse cx="138" cy="82" rx="8" ry="3" fill="#BCAAA4" stroke="#5D4037" stroke-width="0.8"/>
<!-- Rhizoids -->
<line x1="138" y1="230" x2="125" y2="250" stroke="#8D6E63" stroke-width="1"/>
<line x1="138" y1="230" x2="145" y2="252" stroke="#8D6E63" stroke-width="1"/>
<line x1="138" y1="230" x2="135" y2="255" stroke="#8D6E63" stroke-width="1"/>
<text x="165" y="95" font-family="Arial,sans-serif" font-size="7" fill="#5D4037">коробочка</text>
<text x="155" y="115" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">ножка</text>
<text x="150" y="165" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">стебелёк</text>
<text x="150" y="185" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32">листочки</text>
<text x="155" y="248" font-family="Arial,sans-serif" font-size="7" fill="#8D6E63">ризоиды</text>

{panel(310,75,275,275,"ОСОБЕННОСТИ МХОВ","#1B5E20")}
<text x="325" y="105" font-family="Arial,sans-serif" font-size="9" fill="#1B5E20" font-weight="bold">Нет корней</text>
<text x="325" y="120" font-family="Arial,sans-serif" font-size="8" fill="#555">Ризоиды вместо корней</text>
<text x="325" y="140" font-family="Arial,sans-serif" font-size="9" fill="#1B5E20" font-weight="bold">Нет проводящей системы</text>
<text x="325" y="155" font-family="Arial,sans-serif" font-size="8" fill="#555">Вода по поверхности стебля</text>
<text x="325" y="175" font-family="Arial,sans-serif" font-size="9" fill="#1B5E20" font-weight="bold">Размножение спорами</text>
<text x="325" y="190" font-family="Arial,sans-serif" font-size="8" fill="#555">Споры в коробочке</text>
<text x="325" y="210" font-family="Arial,sans-serif" font-size="9" fill="#1B5E20" font-weight="bold">Чередование поколений</text>
<text x="325" y="225" font-family="Arial,sans-serif" font-size="8" fill="#555">Гаметофит + спорофит</text>
<line x1="325" y1="238" x2="570" y2="238" stroke="#C8E6C9" stroke-width="1"/>
<text x="325" y="258" font-family="Arial,sans-serif" font-size="9" fill="#1B5E20" font-weight="bold">Представители:</text>
<text x="325" y="275" font-family="Arial,sans-serif" font-size="8" fill="#555">Кукушкин лён</text>
<text x="325" y="290" font-family="Arial,sans-serif" font-size="8" fill="#555">Сфагнум (торфяной мох)</text>
<text x="325" y="305" font-family="Arial,sans-serif" font-size="8" fill="#555">Образует торф</text>
<text x="325" y="325" font-family="Arial,sans-serif" font-size="8" fill="#555">Впервые заселяют сушу</text>
<text x="325" y="340" font-family="Arial,sans-serif" font-size="8" fill="#555">после воды</text>'''

# For remaining lessons, use simpler but still illustrative templates
def ill_generic_plant(title_parts, a):
    """Generic plant illustration template."""
    return f'''
{panel(15,75,280,275,"ИЛЛЮСТРАЦИЯ",a)}
<!-- Plant illustration -->
<rect x="130" y="130" width="8" height="110" rx="2" fill="#81C784" stroke="#2E7D32" stroke-width="1.5"/>
<path d="M130,165 Q105,155 95,165 Q105,175 130,170" fill="#66BB6A" stroke="#2E7D32" stroke-width="1.2"/>
<path d="M138,155 Q160,145 170,155 Q160,165 138,160" fill="#66BB6A" stroke="#2E7D32" stroke-width="1.2"/>
<path d="M130,195 Q110,185 100,195 Q110,205 130,200" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
<path d="M138,185 Q158,175 168,185 Q158,195 138,190" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
<line x1="134" y1="240" x2="115" y2="270" stroke="#8D6E63" stroke-width="2"/>
<line x1="134" y1="240" x2="145" y2="272" stroke="#8D6E63" stroke-width="2"/>
<line x1="134" y1="240" x2="134" y2="275" stroke="#8D6E63" stroke-width="2.5"/>
<text x="140" y="290" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">{title_parts}</text>

{panel(310,75,275,275,"КЛЮЧЕВЫЕ ПОНЯТИЯ",a)}
<text x="325" y="105" font-family="Arial,sans-serif" font-size="10" fill="{a}" font-weight="bold">{title_parts}</text>'''

# Map keys to illustration functions
ill_map = {
    "bacteria_role": ill_bacteria_role,
    "fungi": ill_fungi,
    "fungi_div": ill_fungi_div,
    "algae": ill_algae,
    "moss": ill_moss,
}

for n, title, bg1, bg2, a, key in lessons_rest:
    sub = f"Биология 6 класс - Урок {n}"
    if key in ill_map:
        body = ill_map[key](a)
    else:
        body = ill_generic_plant(title, a)
    W(n, H(title, sub, bg1, bg2, a) + body + F(title, a))

print(f"Grade 6: all 23 SVGs generated")
