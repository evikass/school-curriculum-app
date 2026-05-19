#!/usr/bin/env python3
"""Generate all 30 biology grade 11 (Evolution, Ecology, Biotechnology) SVG lesson illustrations."""
import os
OUT = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade11/biology"
os.makedirs(OUT, exist_ok=True)
P = "#2E7D32"; L = "#E8F5E9"; M = "#C8E6C9"
def hdr(title, num):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{L}"/><stop offset="100%" stop-color="{M}"/></linearGradient></defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="{P}" stroke-width="2.5"/>
<text x="250" y="30" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="{P}" text-anchor="middle">{title}</text>
<text x="250" y="46" font-family="Arial,sans-serif" font-size="10" fill="#888" text-anchor="middle">Биология 11 класс — Урок {num}</text>
<line x1="30" y1="52" x2="470" y2="52" stroke="{P}" stroke-width="1.5" opacity="0.25"/>
'''
ftr = '\n<rect x="10" y="325" width="480" height="20" rx="4" fill="#2E7D32" opacity="0.85"/>\n<text x="250" y="339" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="white" font-weight="bold">Биология 11 класс</text>\n</svg>'
def ib(x,y,w,h,lines):
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="white" stroke="{P}" stroke-width="1" opacity="0.9"/>\n'
    for i,l in enumerate(lines): s+=f'<text x="{x+w//2}" y="{y+14+i*11}" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">{l}</text>\n'
    return s

titles = {
1:"Развитие эволюционных идей",2:"Доказательства эволюции",
3:"Вид, его критерии и структура",4:"Популяция как единица эволюции",
5:"Факторы эволюции",6:"Естественный отбор и его формы",
7:"Приспособленность организмов",8:"Микроэволюция и видообразование",
9:"Макроэволюция и направления эволюции",10:"Развитие жизни в архее и протерозое",
11:"Развитие жизни в палеозое",12:"Развитие жизни в мезозое",
13:"Развитие жизни в кайнозое",14:"Происхождение человека",
15:"Экологические факторы и закономерности",16:"Популяции",
17:"Сообщества (биоценозы)",18:"Экосистемы и их структура",
19:"Круговорот веществ в экосистемах",20:"Сукцессия — смена экосистем",
21:"Учение В.И. Вернадского о биосфере",22:"Функции живого вещества в биосфере",
23:"Круговорот веществ в биосфере",24:"Антропогенные факторы и экологические проблемы",
25:"Глобальные экологические проблемы",26:"Охрана природы и устойчивое развитие",
27:"Селекция растений и животных",28:"Биотехнология: генетическая инженерия",
29:"Клеточная инженерия и клонирование",30:"Этические аспекты биотехнологии"
}

svgs = {}

# 1: Развитие эволюционных идей
svgs[1]=hdr(titles[1],1)+'''
<line x1="50" y1="185" x2="450" y2="185" stroke="#5D4037" stroke-width="2"/>
<path d="M450,185 L445,180 M450,185 L445,190" stroke="#5D4037" stroke-width="2" fill="none"/>
<circle cx="80" cy="185" r="7" fill="#795548" stroke="#4E342E" stroke-width="1.5"/>
<text x="80" y="205" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Античность</text>
<circle cx="170" cy="185" r="7" fill="#8D6E63" stroke="#4E342E" stroke-width="1.5"/>
<text x="170" y="205" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Линней</text>
<text x="170" y="215" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">XVIII в.</text>
<circle cx="250" cy="185" r="8" fill="#A1887F" stroke="#4E342E" stroke-width="1.5"/>
<text x="250" y="205" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Ламарк</text>
<text x="250" y="215" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">1809</text>
<circle cx="340" cy="185" r="9" fill="#66BB6A" stroke="#2E7D32" stroke-width="2"/>
<text x="340" y="207" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle" font-weight="bold">Дарвин</text>
<text x="340" y="217" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">1859</text>
<circle cx="430" cy="185" r="7" fill="#4CAF50" stroke="#2E7D32" stroke-width="1.5"/>
<text x="430" y="205" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">СТЭ</text>
<text x="430" y="215" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">XX-XXI в.</text>
<g transform="translate(120,105)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#8D6E63" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#8D6E63" text-anchor="middle" font-weight="bold">Ламарк</text>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Наследование приобрет.</text>
<text x="0" y="14" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Упражнение органов</text>
</g>
<g transform="translate(380,105)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Дарвин</text>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Естественный отбор</text>
<text x="0" y="14" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Борьба за существование</text>
</g>
'''+ib(30,245,440,55,["Креационизм: виды созданы Творцом и неизменны","Ламарк: стремление к совершенству, упражнение/неупражнение органов","Дарвин: наследственность + изменчивость + естественный отбор = эволюция","СТЭ: синтез дарвинизма и генетики (Шмальгаузен, Тимофеев-Ресовский)"])+ftr

# 2: Доказательства эволюции
svgs[2]=hdr(titles[2],2)+'''
<g transform="translate(85,150)">
<rect x="-55" y="-50" width="110" height="100" rx="5" fill="white" stroke="#795548" stroke-width="1.5"/>
<text x="0" y="-35" font-family="Arial,sans-serif" font-size="6" fill="#795548" text-anchor="middle" font-weight="bold">Палеонтоло-</text>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="6" fill="#795548" text-anchor="middle" font-weight="bold">гические</text>
<line x1="-40" y1="-18" x2="40" y2="-18" stroke="#795548" stroke-width="0.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Ископаемые</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">переходные формы</text>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Филогенет. ряды</text>
<text x="0" y="37" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Руководящие</text>
<text x="0" y="47" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">ископаемые</text>
</g>
<g transform="translate(250,150)">
<rect x="-55" y="-50" width="110" height="100" rx="5" fill="white" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="-35" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">Сравнительно-</text>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">анатомические</text>
<line x1="-40" y1="-18" x2="40" y2="-18" stroke="#1565C0" stroke-width="0.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Гомологичные органы</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Аналогичные органы</text>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Рудименты</text>
<text x="0" y="37" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Атавизмы</text>
</g>
<g transform="translate(415,150)">
<rect x="-55" y="-50" width="110" height="100" rx="5" fill="white" stroke="#9C27B0" stroke-width="1.5"/>
<text x="0" y="-35" font-family="Arial,sans-serif" font-size="6" fill="#9C27B0" text-anchor="middle" font-weight="bold">Молекулярно-</text>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="6" fill="#9C27B0" text-anchor="middle" font-weight="bold">биологические</text>
<line x1="-40" y1="-18" x2="40" y2="-18" stroke="#9C27B0" stroke-width="0.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Сходство ДНК</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Белки-гомологи</text>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Универсальный код</text>
<text x="0" y="37" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Сходство эмбрионов</text>
</g>
'''+ib(30,265,440,40,["Гомологичные: общее происхождение (рука, крыло, ласт) | Аналогичные: сходная функция","Рудименты: аппендикс, копчик | Атавизмы: хвост, многососковость","Эмбриологические: биогенетический закон, сходство ранних зародышей"])+ftr

# 3: Вид, его критерии и структура
svgs[3]=hdr(titles[3],3)+'''
<g transform="translate(250,175)">
<circle cx="0" cy="0" r="65" fill="#2E7D32" opacity="0.06" stroke="#2E7D32" stroke-width="2"/>
<text x="0" y="-45" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle" font-weight="bold">ВИД</text>
<line x1="-40" y1="-37" x2="40" y2="-37" stroke="#2E7D32" stroke-width="0.8" opacity="0.5"/>
</g>
<g transform="translate(90,95)">
<rect x="-42" y="-13" width="84" height="26" rx="5" fill="white" stroke="#C62828" stroke-width="1.2"/>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="5" fill="#C62828" text-anchor="middle" font-weight="bold">Морфологический</text>
</g>
<g transform="translate(210,72)">
<rect x="-42" y="-13" width="84" height="26" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle" font-weight="bold">Генетический</text>
</g>
<g transform="translate(340,72)">
<rect x="-42" y="-13" width="84" height="26" rx="5" fill="white" stroke="#F9A825" stroke-width="1.2"/>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="5" fill="#F9A825" text-anchor="middle" font-weight="bold">Физиологический</text>
</g>
<g transform="translate(440,95)">
<rect x="-42" y="-13" width="84" height="26" rx="5" fill="white" stroke="#9C27B0" stroke-width="1.2"/>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="5" fill="#9C27B0" text-anchor="middle" font-weight="bold">Экологический</text>
</g>
<g transform="translate(90,260)">
<rect x="-42" y="-13" width="84" height="26" rx="5" fill="white" stroke="#E65100" stroke-width="1.2"/>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle" font-weight="bold">Географический</text>
</g>
<g transform="translate(250,280)">
<rect x="-42" y="-13" width="84" height="26" rx="5" fill="white" stroke="#5D4037" stroke-width="1.2"/>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="5" fill="#5D4037" text-anchor="middle" font-weight="bold">Биохимический</text>
</g>
<g transform="translate(410,260)">
<rect x="-42" y="-13" width="84" height="26" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle" font-weight="bold">Исторический</text>
</g>
'''+ib(30,300,440,12,["Структура вида: популяции и подвиды | Ареал: область распространения вида"])+ftr

# 4: Популяция как единица эволюции
svgs[4]=hdr(titles[4],4)+'''
<g transform="translate(140,180)">
<circle cx="0" cy="0" r="55" fill="#2E7D32" opacity="0.07" stroke="#2E7D32" stroke-width="2"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Популяция</text>
<text x="0" y="2" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Единица эволюции</text>
<circle cx="-20" cy="25" r="3" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
<circle cx="-8" cy="35" r="3" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
<circle cx="5" cy="25" r="3" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
<circle cx="18" cy="35" r="3" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
<circle cx="-12" cy="42" r="3" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
<circle cx="10" cy="42" r="3" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
</g>
<g transform="translate(380,160)">
<rect x="-80" y="-65" width="160" height="130" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-50" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Почему популяция?</text>
<line x1="-65" y1="-43" x2="65" y2="-43" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="-28" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Открытая генетич. система</text>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Свободное скрещивание</text>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Генофонд: все гены</text>
<text x="0" y="13" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Мутационный процесс</text>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Изменение частот аллелей</text>
<text x="0" y="43" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Борьба за существование</text>
<text x="0" y="58" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Естественный отбор</text>
</g>
'''+ftr

# 5: Факторы эволюции
svgs[5]=hdr(titles[5],5)+'''
<g transform="translate(250,175)">
<circle cx="0" cy="0" r="35" fill="#2E7D32" opacity="0.12" stroke="#2E7D32" stroke-width="2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Эволюция</text>
</g>
<g transform="translate(85,105)">
<rect x="-55" y="-28" width="110" height="56" rx="5" fill="white" stroke="#C62828" stroke-width="1.5"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">Мутационный</text>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">процесс</text>
<line x1="-40" y1="5" x2="40" y2="5" stroke="#C62828" stroke-width="0.5"/>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Поставщик материала</text>
</g>
<g transform="translate(250,80)">
<rect x="-55" y="-28" width="110" height="56" rx="5" fill="white" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">Изоляция</text>
<line x1="-40" y1="0" x2="40" y2="0" stroke="#1565C0" stroke-width="0.5"/>
<text x="0" y="13" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Разделение генофонда</text>
</g>
<g transform="translate(415,105)">
<rect x="-55" y="-28" width="110" height="56" rx="5" fill="white" stroke="#9C27B0" stroke-width="1.5"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="7" fill="#9C27B0" text-anchor="middle" font-weight="bold">Дрейф генов</text>
<line x1="-40" y1="0" x2="40" y2="0" stroke="#9C27B0" stroke-width="0.5"/>
<text x="0" y="13" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Случайные изменения</text>
</g>
<g transform="translate(160,260)">
<rect x="-55" y="-28" width="110" height="56" rx="5" fill="white" stroke="#FF9800" stroke-width="1.5"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="7" fill="#FF9800" text-anchor="middle" font-weight="bold">Борьба за</text>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="7" fill="#FF9800" text-anchor="middle" font-weight="bold">существование</text>
<line x1="-40" y1="5" x2="40" y2="5" stroke="#FF9800" stroke-width="0.5"/>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Внутривидовая, межвидовая</text>
</g>
<g transform="translate(350,260)">
<rect x="-55" y="-28" width="110" height="56" rx="5" fill="white" stroke="#2E7D32" stroke-width="2"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Естественный</text>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">отбор</text>
<line x1="-40" y1="5" x2="40" y2="5" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Направляющий фактор</text>
</g>
'''+ftr

# 6: Естественный отбор и его формы
svgs[6]=hdr(titles[6],6)+'''
<g transform="translate(85,135)">
<rect x="-60" y="-45" width="120" height="90" rx="5" fill="white" stroke="#C62828" stroke-width="1.5"/>
<text x="0" y="-32" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">Движущий</text>
<line x1="-45" y1="-25" x2="45" y2="-25" stroke="#C62828" stroke-width="0.5"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Смещение нормы</text>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">реакции</text>
<!-- Small graph -->
<line x1="-35" y1="25" x2="35" y2="25" stroke="#C62828" stroke-width="0.8"/>
<line x1="-35" y1="25" x2="-35" y2="5" stroke="#C62828" stroke-width="0.8"/>
<path d="M-30,22 Q-20,8 -10,10 Q0,12 10,18 Q20,23 30,24" stroke="#C62828" stroke-width="1.5" fill="none"/>
<path d="M-30,23 Q-15,20 0,10 Q15,5 25,12" stroke="#E53935" stroke-width="1" fill="none" stroke-dasharray="3,2"/>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="4" fill="#C62828" text-anchor="middle">Изменение среды</text>
</g>
<g transform="translate(250,135)">
<rect x="-60" y="-45" width="120" height="90" rx="5" fill="white" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="-32" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">Стабилизирующий</text>
<line x1="-45" y1="-25" x2="45" y2="-25" stroke="#1565C0" stroke-width="0.5"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Сохранение нормы</text>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">реакции</text>
<!-- Small graph -->
<line x1="-35" y1="25" x2="35" y2="25" stroke="#1565C0" stroke-width="0.8"/>
<line x1="-35" y1="25" x2="-35" y2="5" stroke="#1565C0" stroke-width="0.8"/>
<path d="M-30,22 Q-15,6 0,8 Q15,6 30,22" stroke="#1565C0" stroke-width="1.5" fill="none"/>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="4" fill="#1565C0" text-anchor="middle">Стабильная среда</text>
</g>
<g transform="translate(415,135)">
<rect x="-60" y="-45" width="120" height="90" rx="5" fill="white" stroke="#F9A825" stroke-width="1.5"/>
<text x="0" y="-32" font-family="Arial,sans-serif" font-size="7" fill="#F9A825" text-anchor="middle" font-weight="bold">Разрывающий</text>
<line x1="-45" y1="-25" x2="45" y2="-25" stroke="#F9A825" stroke-width="0.5"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Две нормы реакции</text>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Элиминация средних</text>
<!-- Small graph -->
<line x1="-35" y1="25" x2="35" y2="25" stroke="#F9A825" stroke-width="0.8"/>
<line x1="-35" y1="25" x2="-35" y2="5" stroke="#F9A825" stroke-width="0.8"/>
<path d="M-30,22 Q-25,10 -20,8 Q-15,6 -10,15 Q-5,23 0,25 Q5,23 10,15 Q15,6 20,8 Q25,10 30,22" stroke="#F9A825" stroke-width="1.5" fill="none"/>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="4" fill="#F9A825" text-anchor="middle">Контрастная среда</text>
</g>
'''+ib(30,265,440,40,["Движущий: адаптация к новым условиям | Стабилизирующий: при постоянных условиях","Разрывающий (дизруптивный): форма для двух крайних вариантов","Половой отбор: конкуренция за партнёра | Формы борьбы: внутривидовая, межвидовая, с условиями"])+ftr

# 7: Приспособленность организмов
svgs[7]=hdr(titles[7],7)+'''
<g transform="translate(100,120)">
<rect x="-60" y="-30" width="120" height="60" rx="5" fill="#8BC34A" opacity="0.15" stroke="#558B2F" stroke-width="1.5"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#558B2F" text-anchor="middle" font-weight="bold">Маскировка</text>
<line x1="-45" y1="-10" x2="45" y2="-10" stroke="#558B2F" stroke-width="0.5"/>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Сходство с фоном</text>
<text x="0" y="15" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Палочник, камбала</text>
</g>
<g transform="translate(250,120)">
<rect x="-60" y="-30" width="120" height="60" rx="5" fill="#FF9800" opacity="0.15" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">Мимикрия</text>
<line x1="-45" y1="-10" x2="45" y2="-10" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Сходство с опасным</text>
<text x="0" y="15" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Журчалка похожа на осу</text>
</g>
<g transform="translate(400,120)">
<rect x="-55" y="-30" width="110" height="60" rx="5" fill="#F44336" opacity="0.15" stroke="#C62828" stroke-width="1.5"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">Предупреждающая</text>
<text x="0" y="-7" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">окраска</text>
<line x1="-40" y1="0" x2="40" y2="0" stroke="#C62828" stroke-width="0.5"/>
<text x="0" y="13" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Яркая = ядовитый</text>
<text x="0" y="23" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Осы, саламандры</text>
</g>
<g transform="translate(150,235)">
<rect x="-60" y="-25" width="120" height="50" rx="5" fill="#9C27B0" opacity="0.1" stroke="#7B1FA2" stroke-width="1.5"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Физиологические</text>
<line x1="-45" y1="-3" x2="45" y2="-3" stroke="#7B1FA2" stroke-width="0.5"/>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Спячка, анабиоз, синтез</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">антифризов, яды</text>
</g>
<g transform="translate(370,235)">
<rect x="-60" y="-25" width="120" height="50" rx="5" fill="#1565C0" opacity="0.1" stroke="#0D47A1" stroke-width="1.5"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="6" fill="#0D47A1" text-anchor="middle" font-weight="bold">Поведенческие</text>
<line x1="-45" y1="-3" x2="45" y2="-3" stroke="#0D47A1" stroke-width="0.5"/>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Запасание корма, миграции</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Гнездование, стайность</text>
</g>
'''+ib(30,285,440,22,["Приспособленность — результат естественного отбора","Относительность: при изменении условий приспособление может быть бесполезным или вредным"])+ftr

# 8: Микроэволюция и видообразование
svgs[8]=hdr(titles[8],8)+'''
<!-- Allopatric speciation -->
<text x="250" y="72" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Аллопатрическое видообразование</text>
<g transform="translate(100,160)">
<ellipse cx="0" cy="0" rx="50" ry="35" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle">Популяция A</text>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Исходный вид</text>
<circle cx="-15" cy="18" r="3" fill="#66BB6A"/>
<circle cx="0" cy="22" r="3" fill="#66BB6A"/>
<circle cx="15" cy="18" r="3" fill="#66BB6A"/>
</g>
<!-- Barrier -->
<rect x="155" y="100" width="15" height="120" rx="3" fill="#795548" opacity="0.4" stroke="#5D4037" stroke-width="1"/>
<text x="162" y="235" font-family="Arial,sans-serif" font-size="5" fill="#5D4037" text-anchor="middle">Барьер</text>
<g transform="translate(250,140)">
<ellipse cx="0" cy="0" rx="40" ry="30" fill="#E8F5E9" stroke="#388E3C" stroke-width="1.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#388E3C" text-anchor="middle">Популяция B</text>
<circle cx="-8" cy="15" r="3" fill="#81C784"/>
<circle cx="8" cy="18" r="3" fill="#81C784"/>
</g>
<g transform="translate(380,140)">
<ellipse cx="0" cy="0" rx="40" ry="30" fill="#FFF3E0" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Популяция C</text>
<circle cx="-8" cy="15" r="3" fill="#FFCC80"/>
<circle cx="8" cy="18" r="3" fill="#FFCC80"/>
</g>
<line x1="210" y1="120" x2="230" y2="130" stroke="#388E3C" stroke-width="1"/>
<line x1="210" y1="160" x2="230" y2="150" stroke="#E65100" stroke-width="1"/>
'''+ib(30,255,440,50,["Микроэволюция: изменения внутри вида (популяционный уровень)","Видообразование: аллопатрическое (географическая изоляция) и симпатрическое (экологическая)","Изоляция: географическая, экологическая, репродуктивная | Репродуктивная = завершающий этап"])+ftr

# 9: Макроэволюция и направления эволюции
svgs[9]=hdr(titles[9],9)+'''
<g transform="translate(85,130)">
<rect x="-55" y="-40" width="110" height="80" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Ароморфоз</text>
<line x1="-40" y1="-18" x2="40" y2="-18" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Крупные изменения</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">повышающие</text>
<text x="0" y="19" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">уровень организации</text>
<text x="0" y="33" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Лёгкие, 4 камеры</text>
</g>
<g transform="translate(250,130)">
<rect x="-55" y="-40" width="110" height="80" rx="5" fill="white" stroke="#FF9800" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#FF9800" text-anchor="middle" font-weight="bold">Идиоадаптация</text>
<line x1="-40" y1="-18" x2="40" y2="-18" stroke="#FF9800" stroke-width="0.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Мелкие изменения</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">приспособления к</text>
<text x="0" y="19" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">условиям среды</text>
<text x="0" y="33" font-family="Arial,sans-serif" font-size="5" fill="#FF9800" text-anchor="middle">Форма клюва</text>
</g>
<g transform="translate(415,130)">
<rect x="-55" y="-40" width="110" height="80" rx="5" fill="white" stroke="#795548" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#795548" text-anchor="middle" font-weight="bold">Дегенерация</text>
<line x1="-40" y1="-18" x2="40" y2="-18" stroke="#795548" stroke-width="0.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Упрощение</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">строения при</text>
<text x="0" y="19" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">паразитизме</text>
<text x="0" y="33" font-family="Arial,sans-serif" font-size="5" fill="#795548" text-anchor="middle">Ленточный червь</text>
</g>
'''+ib(30,240,440,55,["Ароморфоз: повышение организации (теплокровность, хлорофилл)","Идиоадаптация: частные приспособления без повышения организации","Дегенерация: утрата органов при паразитическом образе жизни","Правило Ч. Дарвина: дивергенция — расхождение признаков у потомков"])+ftr

# 10: Развитие жизни в архее и протерозое
svgs[10]=hdr(titles[10],10)+'''
<g transform="translate(120,170)">
<rect x="-70" y="-65" width="140" height="130" rx="5" fill="white" stroke="#795548" stroke-width="1.5"/>
<text x="0" y="-50" font-family="Arial,sans-serif" font-size="9" fill="#795548" text-anchor="middle" font-weight="bold">Архей</text>
<text x="0" y="-37" font-family="Arial,sans-serif" font-size="6" fill="#888" text-anchor="middle">3.8 - 2.5 млрд л.н.</text>
<line x1="-55" y1="-28" x2="55" y2="-28" stroke="#795548" stroke-width="0.5"/>
<text x="0" y="-13" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Зарождение жизни</text>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Прокариоты</text>
<text x="0" y="13" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Брожение (без O2)</text>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Первые строматолиты</text>
<text x="0" y="43" font-family="Arial,sans-serif" font-size="6" fill="#795548" text-anchor="middle">Анаэробная атмосфера</text>
<text x="0" y="56" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Бактерии, цианобактерии</text>
</g>
<g transform="translate(370,170)">
<rect x="-70" y="-65" width="140" height="130" rx="5" fill="white" stroke="#8D6E63" stroke-width="1.5"/>
<text x="0" y="-50" font-family="Arial,sans-serif" font-size="9" fill="#8D6E63" text-anchor="middle" font-weight="bold">Протерозой</text>
<text x="0" y="-37" font-family="Arial,sans-serif" font-size="6" fill="#888" text-anchor="middle">2.5 - 0.54 млрд л.н.</text>
<line x1="-55" y1="-28" x2="55" y2="-28" stroke="#8D6E63" stroke-width="0.5"/>
<text x="0" y="-13" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Кислородная катастрофа</text>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Эукариоты (1.5 млрд)</text>
<text x="0" y="13" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Одноклеточные водоросли</text>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Простейшие</text>
<text x="0" y="43" font-family="Arial,sans-serif" font-size="6" fill="#8D6E63" text-anchor="middle">Озоновый экран</text>
<text x="0" y="56" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Беспозвоночные (конец)</text>
</g>
'''+ftr

# 11-14: Geological eras + Human origins
for n in [11,12,13,14]:
    t = titles[n]
    if n == 11:
        svgs[n]=hdr(t,n)+'''
<g transform="translate(250,175)">
<rect x="-100" y="-70" width="200" height="140" rx="5" fill="white" stroke="#4CAF50" stroke-width="1.5"/>
<text x="0" y="-55" font-family="Arial,sans-serif" font-size="10" fill="#4CAF50" text-anchor="middle" font-weight="bold">Палеозойская эра</text>
<text x="0" y="-42" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">540 - 248 млн л.н.</text>
<line x1="-85" y1="-35" x2="85" y2="-35" stroke="#4CAF50" stroke-width="0.5"/>
<text x="-45" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Кембрий</text>
<text x="45" y="-18" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Трилобиты, моллюски</text>
<text x="-45" y="0" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Ордовик-Силур</text>
<text x="45" y="0" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Рыбы, первые растения</text>
<text x="-45" y="18" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Девон</text>
<text x="45" y="18" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Амфибии, папоротники</text>
<text x="-45" y="36" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Карбон</text>
<text x="45" y="36" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Рептилии, каменноуг. лес</text>
<text x="-45" y="54" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Пермь</text>
<text x="45" y="54" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Зверообразные рептилии</text>
</g>
'''+ftr
    elif n == 12:
        svgs[n]=hdr(t,n)+'''
<g transform="translate(250,175)">
<rect x="-100" y="-70" width="200" height="140" rx="5" fill="white" stroke="#FF9800" stroke-width="1.5"/>
<text x="0" y="-55" font-family="Arial,sans-serif" font-size="10" fill="#FF9800" text-anchor="middle" font-weight="bold">Мезозойская эра</text>
<text x="0" y="-42" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">248 - 65 млн л.н.</text>
<line x1="-85" y1="-35" x2="85" y2="-35" stroke="#FF9800" stroke-width="0.5"/>
<text x="-45" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">Триас</text>
<text x="45" y="-18" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Первые динозавры</text>
<text x="-45" y="0" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">Юра</text>
<text x="45" y="0" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Гигантские динозавры</text>
<text x="0" y="15" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Первые птицы (археоптерикс), млекопитающие</text>
<text x="-45" y="33" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">Мел</text>
<text x="45" y="33" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Покрытосеменные</text>
<text x="0" y="48" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Мел-палеогеновое вымирание: падение астероида</text>
<text x="0" y="62" font-family="Arial,sans-serif" font-size="6" fill="#FF9800" text-anchor="middle">Эпоха рептилий господства</text>
</g>
'''+ftr
    elif n == 13:
        svgs[n]=hdr(t,n)+'''
<g transform="translate(250,175)">
<rect x="-100" y="-70" width="200" height="140" rx="5" fill="white" stroke="#42A5F5" stroke-width="1.5"/>
<text x="0" y="-55" font-family="Arial,sans-serif" font-size="10" fill="#42A5F5" text-anchor="middle" font-weight="bold">Кайнозойская эра</text>
<text x="0" y="-42" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">65 млн л.н. - настоящее</text>
<line x1="-85" y1="-35" x2="85" y2="-35" stroke="#42A5F5" stroke-width="0.5"/>
<text x="-45" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">Палеоген</text>
<text x="45" y="-18" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Млекопитающие, птицы</text>
<text x="-45" y="0" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">Неоген</text>
<text x="45" y="0" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Приматы, гоминиды</text>
<text x="-45" y="18" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">Четвертичн.</text>
<text x="45" y="18" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Человек, ледниковье</text>
<text x="0" y="40" font-family="Arial,sans-serif" font-size="6" fill="#42A5F5" text-anchor="middle">Эпоха млекопитающих</text>
<text x="0" y="55" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Покрытосеменные доминируют</text>
</g>
'''+ftr
    elif n == 14:
        svgs[n]=hdr(t,n)+'''
<line x1="50" y1="185" x2="450" y2="185" stroke="#5D4037" stroke-width="2"/>
<path d="M450,185 L445,180 M450,185 L445,190" stroke="#5D4037" stroke-width="2" fill="none"/>
<circle cx="80" cy="185" r="6" fill="#795548" stroke="#4E342E" stroke-width="1.5"/>
<text x="80" y="205" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Дриопитек</text>
<circle cx="150" cy="185" r="6" fill="#8D6E63" stroke="#4E342E" stroke-width="1.5"/>
<text x="150" y="205" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Австралопитек</text>
<circle cx="220" cy="185" r="7" fill="#A1887F" stroke="#4E342E" stroke-width="1.5"/>
<text x="220" y="205" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Homo habilis</text>
<circle cx="300" cy="185" r="7" fill="#BCAAA4" stroke="#4E342E" stroke-width="1.5"/>
<text x="300" y="205" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">H. erectus</text>
<circle cx="370" cy="185" r="8" fill="#FFAB91" stroke="#BF360C" stroke-width="1.5"/>
<text x="370" y="205" font-family="Arial,sans-serif" font-size="5" fill="#BF360C" text-anchor="middle">Неандерталец</text>
<circle cx="440" cy="185" r="8" fill="#81C784" stroke="#2E7D32" stroke-width="2"/>
<text x="440" y="205" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle" font-weight="bold">H. sapiens</text>
<text x="250" y="100" font-family="Arial,sans-serif" font-size="8" fill="#5D4037" text-anchor="middle" font-weight="bold">Антропогенез</text>
<g transform="translate(100,120)">
<rect x="-55" y="-15" width="110" height="30" rx="5" fill="white" stroke="#5D4037" stroke-width="1"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="5" fill="#5D4037" text-anchor="middle">Биол. факторы: наслед., изменч., отбор</text>
</g>
<g transform="translate(400,120)">
<rect x="-55" y="-15" width="110" height="30" rx="5" fill="white" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="4" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Соц. факторы: труд, речь, общество</text>
</g>
'''+ib(30,230,440,50,["Дриопитек(20млн) - Австралопитек(4млн) - Ч.умелый(2млн) - Ч.прямоходящий - Неандерталец(200тыс) - Кроманьонец(40тыс)","Биологические: наследственность, изменчивость, борьба за существование, отбор","Социальные: труд (орудия), речь (общение), общество (совместная деятельность)"])+ftr

# 15-26: Ecology and Conservation (mix of detailed and themed)
for n in range(15,27):
    t = titles[n]
    if n == 15:  # Экологические факторы
        svgs[n]=hdr(t,n)+'''
<g transform="translate(120,125)">
<rect x="-70" y="-35" width="140" height="70" rx="5" fill="#FF9800" opacity="0.12" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">Абиотические</text>
<line x1="-55" y1="-12" x2="55" y2="-12" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="2" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Свет, t, влажность</text>
<text x="0" y="14" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Давление, солёность</text>
<text x="0" y="26" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">pH, течения, ветер</text>
</g>
<g transform="translate(380,125)">
<rect x="-70" y="-35" width="140" height="70" rx="5" fill="#4CAF50" opacity="0.12" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Биотические</text>
<line x1="-55" y1="-12" x2="55" y2="-12" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="2" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Хищничество, конкуренция</text>
<text x="0" y="14" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Симбиоз, паразитизм</text>
<text x="0" y="26" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Мутуализм, комменсализм</text>
</g>
<g transform="translate(250,240)">
<rect x="-70" y="-30" width="140" height="60" rx="5" fill="#9C27B0" opacity="0.12" stroke="#7B1FA2" stroke-width="1.5"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="8" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Антропогенные</text>
<line x1="-55" y1="-7" x2="55" y2="-7" stroke="#7B1FA2" stroke-width="0.5"/>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Загрязнение, вырубка</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Урбанизация, интродукция</text>
</g>
'''+ib(30,295,440,18,["Закон оптимума | Закон минимума Либиха | Ограничивающий фактор","Фотопериодизм: реакция на длину дня | Экологическая валентность"])+ftr
    elif n == 18:  # Экосистемы и их структура
        svgs[n]=hdr(t,n)+'''
<!-- Ecological pyramid -->
<g transform="translate(130,195)">
<polygon points="0,-65 50,-65 60,45 -60,45" fill="#4CAF50" opacity="0.12" stroke="#2E7D32" stroke-width="1.5"/>
<rect x="-50" y="30" width="100" height="15" rx="2" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
<text x="0" y="41" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle">Редуценты</text>
<rect x="-35" y="10" width="70" height="15" rx="2" fill="#FF9800" stroke="#E65100" stroke-width="1"/>
<text x="0" y="21" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle">Консументы II порядка</text>
<rect x="-22" y="-10" width="44" height="15" rx="2" fill="#E53935" stroke="#C62828" stroke-width="1"/>
<text x="0" y="1" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle">Консум. I</text>
<rect x="-10" y="-35" width="20" height="15" rx="2" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="4" fill="white" text-anchor="middle">Прод.</text>
</g>
<g transform="translate(370,170)">
<rect x="-80" y="-60" width="160" height="120" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-45" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Компоненты экосистемы</text>
<line x1="-65" y1="-38" x2="65" y2="-38" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="-22" font-family="Arial,sans-serif" font-size="6" fill="#4CAF50" text-anchor="middle">Продуценты (автотрофы)</text>
<text x="0" y="-8" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle">Консументы (гетеротрофы)</text>
<text x="0" y="6" font-family="Arial,sans-serif" font-size="6" fill="#8D6E63" text-anchor="middle">Редуценты (сапротрофы)</text>
<line x1="-65" y1="15" x2="65" y2="15" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Биотические + абиотические</text>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Пространство + потоки</text>
<text x="0" y="54" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">вещества и энергии</text>
</g>
'''+ftr
    elif n == 20:  # Сукцессия
        svgs[n]=hdr(t,n)+'''
<line x1="50" y1="190" x2="450" y2="190" stroke="#5D4037" stroke-width="2"/>
<path d="M450,190 L445,185 M450,190 L445,195" stroke="#5D4037" stroke-width="2" fill="none"/>
<g transform="translate(100,170)">
<rect x="-15" y="10" width="30" height="10" rx="2" fill="#BCAAA4" stroke="#795548" stroke-width="1"/>
<line x1="-5" y1="10" x2="-5" y2="5" stroke="#66BB6A" stroke-width="1"/>
<line x1="5" y1="10" x2="5" y2="5" stroke="#66BB6A" stroke-width="1"/>
<text x="0" y="32" font-family="Arial,sans-serif" font-size="5" fill="#5D4037" text-anchor="middle">Лишайники</text>
</g>
<g transform="translate(190,160)">
<rect x="-20" y="20" width="40" height="10" rx="2" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
<line x1="0" y1="20" x2="0" y2="0" stroke="#4CAF50" stroke-width="2"/>
<circle cx="0" cy="-5" r="8" fill="#4CAF50" opacity="0.3" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="5" fill="#5D4037" text-anchor="middle">Травы, мхи</text>
</g>
<g transform="translate(290,150)">
<rect x="-25" y="30" width="50" height="10" rx="2" fill="#795548" stroke="#4E342E" stroke-width="1"/>
<line x1="0" y1="30" x2="0" y2="5" stroke="#4CAF50" stroke-width="2.5"/>
<circle cx="0" cy="0" r="12" fill="#4CAF50" opacity="0.3" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="52" font-family="Arial,sans-serif" font-size="5" fill="#5D4037" text-anchor="middle">Кустарники</text>
</g>
<g transform="translate(390,140)">
<rect x="-30" y="40" width="60" height="10" rx="2" fill="#5D4037" stroke="#3E2723" stroke-width="1"/>
<line x1="-8" y1="40" x2="-8" y2="5" stroke="#4CAF50" stroke-width="3"/>
<line x1="8" y1="40" x2="8" y2="0" stroke="#388E3C" stroke-width="3"/>
<circle cx="-8" cy="0" r="14" fill="#4CAF50" opacity="0.3" stroke="#2E7D32" stroke-width="1"/>
<circle cx="8" cy="-5" r="16" fill="#388E3C" opacity="0.3" stroke="#1B5E20" stroke-width="1"/>
<text x="0" y="62" font-family="Arial,sans-serif" font-size="5" fill="#5D4037" text-anchor="middle">Климакс (лес)</text>
</g>
<text x="250" y="95" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Первичная сукцессия</text>
'''+ib(30,275,440,30,["Первичная: на безжизненном субстрате | Вторичная: после нарушения (пожар)","Климакс: стабильное самоподдерживающееся сообщество","Сукцессия: закономерная смена одних биоценозов другими"])+ftr
    elif n == 21:  # Вернадский
        svgs[n]=hdr(t,n)+'''
<g transform="translate(250,175)">
<circle cx="0" cy="0" r="60" fill="#42A5F5" opacity="0.12" stroke="#1565C0" stroke-width="2"/>
<ellipse cx="0" cy="-35" rx="50" ry="10" fill="#90CAF9" opacity="0.3" stroke="#42A5F5" stroke-width="1"/>
<text x="0" y="-33" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">Атмосфера</text>
<ellipse cx="0" cy="15" rx="45" ry="15" fill="#1565C0" opacity="0.2" stroke="#0D47A1" stroke-width="1"/>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="5" fill="#0D47A1" text-anchor="middle">Гидросфера</text>
<ellipse cx="0" cy="45" rx="35" ry="8" fill="#8D6E63" opacity="0.3" stroke="#5D4037" stroke-width="1"/>
<text x="0" y="47" font-family="Arial,sans-serif" font-size="5" fill="#5D4037" text-anchor="middle">Литосфера</text>
<text x="0" y="-55" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Биосфера</text>
</g>
<g transform="translate(430,130)">
<rect x="-45" y="-35" width="90" height="70" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-22" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">В.И. Вернадский</text>
<line x1="-30" y1="-14" x2="30" y2="-14" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Учение о биосфере</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Живое вещество</text>
<text x="0" y="24" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Ноосфера</text>
</g>
'''+ib(30,275,440,30,["Биосфера: оболочка Земли, населённая организмами (от озонового слоя до дна океана)","Живое вещество: совокупность всех организмов | Ноосфера: сфера разума","Вернадский: живое вещество — геохимическая сила планетарного масштаба"])+ftr
    else:
        icons = {16:"Популяции",17:"Биоценозы",19:"Круговорот веществ",
        22:"Функции живого вещества",23:"Круговорот в биосфере",
        24:"Антропогенные проблемы",25:"Глобальные проблемы",26:"Охрана природы"}
        colors = {16:"#2E7D32",17:"#4CAF50",19:"#1565C0",
        22:"#2E7D32",23:"#42A5F5",24:"#C62828",
        25:"#E53935",26:"#4CAF50"}
        facts = {
        16:["Популяция: группа особей одного вида на одной территории","Численность, плотность, рождаемость, смертность, возрастной состав","Динамика: рост (J-кривая, S-кривая) | Кривые выживания"],
        17:["Биоценоз: исторически сложившееся сообщество организмов","Видовая структура: доминанты, эдификаторы, фоновые виды","Пространственная: ярусность, мозаичность | Трофическая: цепи, сети"],
        19:["Круговорот: использование веществ многократно","Углерод: CO2 - фотосинтез - дыхание/гниение - CO2","Азот: N2 - фиксация - нитраты - организмы - аммиак | Фосфор: из пород"],
        22:["Газовая: O2 и CO2 в атмосфере","Концентрационная: накопление элементов в организмах","Окс.-восст.: изменение валентности элементов"],
        23:["Углеродный цикл: фотосинтез, дыхание, горение топлива","Азотный цикл: азотфиксация, нитрификация, денитрификация","Водный цикл: испарение, конденсация, осадки, сток"],
        24:["Загрязнение: атмосферное, водное, почвенное","Опустынивание, обезлесение, эрозия почв","Сокращение биоразнообразия, фрагментация местообитаний"],
        25:["Глобальное потепление: +1.1C, парниковые газы (CO2, CH4, N2O)","Разрушение озона: фреоны | Кислотные дожди: SO2, NOx","Истощение ресурсов, перенаселение, продовольственная проблема"],
        26:["ООН: Цели устойчивого развития (17 целей)","Охраняемые территории: 15% суши, 7% океана","Рамочная конвенция: 30x30 (30% к 2030)"]
        }
        c = colors.get(n,"#2E7D32")
        sub = icons.get(n,t)
        facts_lines = facts.get(n,["Ключевые понятия","Структура и функции","Значение"])
        svgs[n] = hdr(t,n)+f'''
<g transform="translate(250,170)">
<circle cx="0" cy="0" r="60" fill="{c}" opacity="0.1" stroke="{c}" stroke-width="2"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="11" fill="{c}" text-anchor="middle" font-weight="bold">{sub}</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="9" fill="{c}" text-anchor="middle">11 класс</text>
</g>
'''+ib(30,250,440,50,facts_lines)+ftr

# 27-30: Biotechnology
for n in range(27,31):
    t = titles[n]
    if n == 27:  # Селекция
        svgs[n]=hdr(t,n)+'''
<g transform="translate(120,155)">
<rect x="-75" y="-55" width="150" height="110" rx="5" fill="white" stroke="#4CAF50" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="8" fill="#4CAF50" text-anchor="middle" font-weight="bold">Селекция растений</text>
<line x1="-60" y1="-33" x2="60" y2="-33" stroke="#4CAF50" stroke-width="0.5"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Гибридизация</text>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Полиплоидия</text>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Массовый и индивид. отбор</text>
<text x="0" y="25" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Мутагенез</text>
<text x="0" y="43" font-family="Arial,sans-serif" font-size="5" fill="#4CAF50" text-anchor="middle">Вавилов: 8 центров</text>
</g>
<g transform="translate(380,155)">
<rect x="-75" y="-55" width="150" height="110" rx="5" fill="white" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">Селекция животных</text>
<line x1="-60" y1="-33" x2="60" y2="-33" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Инбридинг / Аутбридинг</text>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Отбор по линии</text>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Проверка по потомству</text>
<text x="0" y="25" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Гетерозис</text>
<text x="0" y="43" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">Искусств. осеменение</text>
</g>
'''+ftr
    elif n == 28:  # Генная инженерия
        svgs[n]=hdr(t,n)+'''
<g transform="translate(250,180)">
<!-- DNA recombination diagram -->
<rect x="-120" y="-70" width="240" height="140" rx="5" fill="white" stroke="#9C27B0" stroke-width="1.5"/>
<text x="0" y="-55" font-family="Arial,sans-serif" font-size="8" fill="#9C27B0" text-anchor="middle" font-weight="bold">Генетическая инженерия</text>
<line x1="-100" y1="-48" x2="100" y2="-48" stroke="#9C27B0" stroke-width="0.5"/>
<!-- Source DNA -->
<rect x="-95" y="-35" width="55" height="20" rx="3" fill="#E1BEE7" stroke="#9C27B0" stroke-width="1"/>
<text x="-67" y="-21" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="middle">Ген-донор</text>
<!-- Restriction enzyme -->
<line x1="-35" y1="-25" x2="0" y2="-25" stroke="#E53935" stroke-width="1.5"/>
<path d="M0,-25 L-3,-28 M0,-25 L-3,-22" stroke="#E53935" stroke-width="1"/>
<text x="-17" y="-15" font-family="Arial,sans-serif" font-size="4" fill="#E53935" text-anchor="middle">Рестриктаза</text>
<!-- Vector -->
<rect x="5" y="-35" width="55" height="20" rx="3" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
<text x="32" y="-21" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Вектор (плазмида)</text>
<!-- Ligase -->
<line x1="65" y1="-25" x2="100" y2="-25" stroke="#1565C0" stroke-width="1.5"/>
<path d="M100,-25 L97,-28 M100,-25 L97,-22" stroke="#1565C0" stroke-width="1"/>
<text x="82" y="-15" font-family="Arial,sans-serif" font-size="4" fill="#1565C0" text-anchor="middle">Лигаза</text>
<!-- Recombinant -->
<rect x="-30" y="5" width="60" height="20" rx="3" fill="#B39DDB" stroke="#7B1FA2" stroke-width="1"/>
<text x="0" y="19" font-family="Arial,sans-serif" font-size="5" fill="#4A148C" text-anchor="middle">Рекомбинантная ДНК</text>
<line x1="0" y1="25" x2="0" y2="35" stroke="#9C27B0" stroke-width="1"/>
<path d="M0,35 L-3,32 M0,35 L3,32" stroke="#9C27B0" stroke-width="1"/>
<!-- Host cell -->
<ellipse cx="0" cy="50" rx="30" ry="12" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="53" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Клетка-хозяин</text>
</g>
'''+ib(30,275,440,30,["Рестриктазы: разрезают ДНК | Лигазы: сшивают фрагменты | Векторы: плазмиды, вирусы","ГМО: бактерии (инсулин), растения (устойчивость), животные (модели)","ПЦР: копирование ДНК in vitro | Секвенирование: определение последовательности"])+ftr
    elif n == 29:  # Клеточная инженерия
        svgs[n]=hdr(t,n)+'''
<g transform="translate(250,175)">
<!-- Cell fusion / cloning diagram -->
<rect x="-120" y="-70" width="240" height="140" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-55" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Клеточная инженерия</text>
<line x1="-100" y1="-48" x2="100" y2="-48" stroke="#2E7D32" stroke-width="0.5"/>
<!-- Two cells -->
<circle cx="-60" cy="-25" r="15" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1.5"/>
<text x="-60" y="-22" font-family="Arial,sans-serif" font-size="4" fill="#2E7D32" text-anchor="middle">Клетка 1</text>
<circle cx="60" cy="-25" r="15" fill="#FFF3E0" stroke="#E65100" stroke-width="1.5"/>
<text x="60" y="-22" font-family="Arial,sans-serif" font-size="4" fill="#E65100" text-anchor="middle">Клетка 2</text>
<!-- Fusion -->
<line x1="-42" y1="-25" x2="-15" y2="-25" stroke="#9C27B0" stroke-width="1.5"/>
<line x1="42" y1="-25" x2="15" y2="-25" stroke="#9C27B0" stroke-width="1.5"/>
<text x="0" y="-30" font-family="Arial,sans-serif" font-size="4" fill="#9C27B0" text-anchor="middle">Слияние</text>
<!-- Hybrid -->
<ellipse cx="0" cy="5" rx="22" ry="15" fill="#F3E5F5" stroke="#9C27B0" stroke-width="1.5"/>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="middle">Гибрид</text>
<!-- Cloning -->
<text x="0" y="35" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Клонирование</text>
<line x1="-60" y1="48" x2="60" y2="48" stroke="#2E7D32" stroke-width="0.8"/>
<!-- Clone cells -->
<circle cx="-40" cy="48" r="6" fill="#E8F5E9" stroke="#2E7D32" stroke-width="0.8"/>
<circle cx="-20" cy="48" r="6" fill="#E8F5E9" stroke="#2E7D32" stroke-width="0.8"/>
<circle cx="0" cy="48" r="6" fill="#E8F5E9" stroke="#2E7D32" stroke-width="0.8"/>
<circle cx="20" cy="48" r="6" fill="#E8F5E9" stroke="#2E7D32" stroke-width="0.8"/>
<circle cx="40" cy="48" r="6" fill="#E8F5E9" stroke="#2E7D32" stroke-width="0.8"/>
</g>
'''+ib(30,275,440,30,["Гибридома: слияние B-лимфоцита и клетки миеломы -> моноклональные антитела","Клонирование: пересадка ядра соматической клетки в яйцеклетку (овца Долли, 1996)","Культура клеток: выращивание in vitro | Тотипотентность растительных клеток"])+ftr
    elif n == 30:  # Этические аспекты
        svgs[n]=hdr(t,n)+'''
<g transform="translate(85,130)">
<rect x="-55" y="-35" width="110" height="70" rx="5" fill="white" stroke="#C62828" stroke-width="1.5"/>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">ГМО</text>
<line x1="-40" y1="-12" x2="40" y2="-12" stroke="#C62828" stroke-width="0.5"/>
<text x="0" y="2" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Безопасность продуктов</text>
<text x="0" y="14" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Маркировка</text>
<text x="0" y="26" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Влияние на экосистемы</text>
</g>
<g transform="translate(250,130)">
<rect x="-55" y="-35" width="110" height="70" rx="5" fill="white" stroke="#9C27B0" stroke-width="1.5"/>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="7" fill="#9C27B0" text-anchor="middle" font-weight="bold">Клонирование</text>
<line x1="-40" y1="-12" x2="40" y2="-12" stroke="#9C27B0" stroke-width="0.5"/>
<text x="0" y="2" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Клонирование человека</text>
<text x="0" y="14" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Терапевтическое</text>
<text x="0" y="26" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Репродуктивное</text>
</g>
<g transform="translate(415,130)">
<rect x="-55" y="-35" width="110" height="70" rx="5" fill="white" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">Геномика</text>
<line x1="-40" y1="-12" x2="40" y2="-12" stroke="#1565C0" stroke-width="0.5"/>
<text x="0" y="2" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Редактирование генома</text>
<text x="0" y="14" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">CRISPR-Cas9</text>
<text x="0" y="26" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Генетическая приватность</text>
</g>
'''+ib(30,235,440,60,["Биоэтика: принципы - автономия, благодеяние, справедливость, не навреди","Конвенция ООН по биоразнообразию | Картахенский протокол по биобезопасности","CRISPR-Cas9: редактирование генома | Запрет репродуктивного клонирования человека","Стволовые клетки: эмбриональные vs взрослые | Пренатальная диагностика"])+ftr

for i in range(1,31):
    with open(f"{OUT}/lesson{i}.svg","w") as f:
        f.write(svgs[i])
print(f"Generated {len(svgs)} SVGs for grade 11 biology")
