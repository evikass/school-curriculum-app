#!/usr/bin/env python3
"""Generate all 25 biology grade 9 (General Biology) SVG lesson illustrations."""
import os
OUT = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade9/biology"
os.makedirs(OUT, exist_ok=True)
P = "#2E7D32"; L = "#E8F5E9"; M = "#C8E6C9"
def hdr(title, num):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{L}"/><stop offset="100%" stop-color="{M}"/></linearGradient></defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="{P}" stroke-width="2.5"/>
<text x="250" y="30" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="{P}" text-anchor="middle">{title}</text>
<text x="250" y="46" font-family="Arial,sans-serif" font-size="10" fill="#888" text-anchor="middle">Биология 9 класс — Урок {num}</text>
<line x1="30" y1="52" x2="470" y2="52" stroke="{P}" stroke-width="1.5" opacity="0.25"/>
'''
ftr = '\n<rect x="10" y="325" width="480" height="20" rx="4" fill="#2E7D32" opacity="0.85"/>\n<text x="250" y="339" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="white" font-weight="bold">Биология 9 класс</text>\n</svg>'
def ib(x,y,w,h,lines):
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="white" stroke="{P}" stroke-width="1" opacity="0.9"/>\n'
    for i,l in enumerate(lines): s+=f'<text x="{x+w//2}" y="{y+14+i*11}" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">{l}</text>\n'
    return s

titles = {
1:"Биология — наука о живом",2:"Классификация организмов",3:"Бактерии",
4:"Развитие эволюционных идей",5:"Доказательства эволюции",6:"Вид и его критерии",
7:"Естественный отбор и формы",8:"Приспособленность организмов",
9:"Возникновение жизни на Земле",10:"Развитие жизни на Земле",
11:"Происхождение человека",12:"Основные понятия генетики",
13:"Законы Менделя",14:"Решение генетических задач",
15:"Хромосомная теория и сцепление генов",16:"Генетика пола и наследование, сцепленное с полом",
17:"Изменчивость и её виды",18:"Селекция растений и животных",
19:"Экологические факторы",20:"Популяции и сообщества",
21:"Экосистемы и пищевые цепи",22:"Сукцессия — смена экосистем",
23:"Биосфера и живое вещество",24:"Влияние человека на биосферу",
25:"Охрана природы"
}

svgs = {}

# 1: Биология — наука о живом
svgs[1]=hdr(titles[1],1)+'''
<g transform="translate(250,180)">
<circle cx="0" cy="0" r="65" fill="#2E7D32" opacity="0.08" stroke="#2E7D32" stroke-width="2"/>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="11" fill="#2E7D32" text-anchor="middle" font-weight="bold">Биология</text>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Наука о живой природе</text>
<line x1="-30" y1="5" x2="30" y2="5" stroke="#2E7D32" stroke-width="0.8" opacity="0.5"/>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Обмен веществ</text>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Размножение</text>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Рост и развитие</text>
<text x="0" y="48" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Наследственность</text>
</g>
<g transform="translate(80,130)">
<rect x="-35" y="-18" width="70" height="36" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">Зоология</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Животные</text>
</g>
<g transform="translate(420,130)">
<rect x="-35" y="-18" width="70" height="36" rx="5" fill="white" stroke="#4CAF50" stroke-width="1.2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#4CAF50" text-anchor="middle" font-weight="bold">Ботаника</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Растения</text>
</g>
<g transform="translate(80,230)">
<rect x="-35" y="-18" width="70" height="36" rx="5" fill="white" stroke="#9C27B0" stroke-width="1.2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#9C27B0" text-anchor="middle" font-weight="bold">Генетика</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Наследственность</text>
</g>
<g transform="translate(420,230)">
<rect x="-35" y="-18" width="70" height="36" rx="5" fill="white" stroke="#E65100" stroke-width="1.2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">Экология</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Среда обитания</text>
</g>
'''+ib(30,280,440,30,["Признаки живого: обмен веществ, размножение, рост, развитие, раздражимость, наследственность","Методы биологии: наблюдение, эксперимент, моделирование, сравнение"])+ftr

# 2: Классификация организмов
svgs[2]=hdr(titles[2],2)+'''
<g transform="translate(250,180)">
<rect x="-80" y="-90" width="160" height="22" rx="5" fill="#1B5E20" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-75" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">Царство</text>
<line x1="-40" y1="-68" x2="-40" y2="-55" stroke="#2E7D32" stroke-width="1"/>
<line x1="40" y1="-68" x2="40" y2="-55" stroke="#2E7D32" stroke-width="1"/>
<rect x="-70" y="-55" width="60" height="20" rx="4" fill="#388E3C" stroke="#2E7D32" stroke-width="1"/>
<text x="-40" y="-41" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">Тип/Отдел</text>
<rect x="10" y="-55" width="60" height="20" rx="4" fill="#388E3C" stroke="#2E7D32" stroke-width="1"/>
<text x="40" y="-41" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">Тип/Отдел</text>
<line x1="-40" y1="-35" x2="-40" y2="-22" stroke="#2E7D32" stroke-width="1"/>
<rect x="-65" y="-22" width="50" height="18" rx="4" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
<text x="-40" y="-9" font-family="Arial,sans-serif" font-size="6" fill="white" text-anchor="middle">Класс</text>
<line x1="-40" y1="-4" x2="-40" y2="8" stroke="#2E7D32" stroke-width="1"/>
<rect x="-60" y="8" width="40" height="16" rx="4" fill="#66BB6A" stroke="#2E7D32" stroke-width="1"/>
<text x="-40" y="19" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Отряд</text>
<line x1="-40" y1="24" x2="-40" y2="36" stroke="#2E7D32" stroke-width="1"/>
<rect x="-55" y="36" width="30" height="14" rx="3" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
<text x="-40" y="46" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Семейство</text>
<line x1="-40" y1="50" x2="-40" y2="60" stroke="#2E7D32" stroke-width="1"/>
<rect x="-50" y="60" width="20" height="12" rx="3" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
<text x="-40" y="69" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Род</text>
<line x1="-40" y1="72" x2="-40" y2="82" stroke="#2E7D32" stroke-width="1"/>
<circle cx="-40" cy="88" r="5" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
<text x="-40" y="91" font-family="Arial,sans-serif" font-size="4" fill="#2E7D32" text-anchor="middle">Вид</text>
</g>
<g transform="translate(420,130)">
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">5 царств</text>
<rect x="-40" y="-18" width="80" height="14" rx="3" fill="#E8F5E9" stroke="#2E7D32" stroke-width="0.8"/>
<text x="0" y="-8" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Бактерии</text>
<rect x="-40" y="-2" width="80" height="14" rx="3" fill="#E8F5E9" stroke="#2E7D32" stroke-width="0.8"/>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Протисты</text>
<rect x="-40" y="14" width="80" height="14" rx="3" fill="#E8F5E9" stroke="#2E7D32" stroke-width="0.8"/>
<text x="0" y="24" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Грибы</text>
<rect x="-40" y="30" width="80" height="14" rx="3" fill="#E8F5E9" stroke="#2E7D32" stroke-width="0.8"/>
<text x="0" y="40" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Растения</text>
<rect x="-40" y="46" width="80" height="14" rx="3" fill="#E8F5E9" stroke="#2E7D32" stroke-width="0.8"/>
<text x="0" y="56" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">Животные</text>
</g>
'''+ib(30,280,440,30,["Иерархия: Царство-Тип-Класс-Отряд-Семейство-Род-Вид","Карл Линней: бинарная номенклатура (род + вид) | Вид — основная единица"])+ftr

# 3: Бактерии
svgs[3]=hdr(titles[3],3)+'''
<g transform="translate(130,170)">
<ellipse cx="0" cy="0" rx="25" ry="12" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/>
<text x="0" y="25" font-family="Arial,sans-serif" font-size="6" fill="#F9A825" text-anchor="middle" font-weight="bold">Кокк</text>
</g>
<g transform="translate(250,150)">
<ellipse cx="-20" cy="0" rx="14" ry="10" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/>
<ellipse cx="5" cy="0" rx="14" ry="10" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/>
<text x="-7" y="25" font-family="Arial,sans-serif" font-size="6" fill="#F9A825" text-anchor="middle" font-weight="bold">Диплококк</text>
</g>
<g transform="translate(380,160)">
<path d="M-30,0 Q-25,-10 -20,0 Q-15,10 -10,0 Q-5,-10 0,0 Q5,10 10,0 Q15,-10 20,0 Q25,10 30,0" fill="none" stroke="#F9A825" stroke-width="3"/>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="6" fill="#F9A825" text-anchor="middle" font-weight="bold">Спирохета</text>
</g>
<g transform="translate(130,260)">
<ellipse cx="0" cy="0" rx="18" ry="9" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/>
<path d="M0,-9 Q5,-18 0,-22" stroke="#F9A825" stroke-width="1.5" fill="none"/>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#F9A825" text-anchor="middle">Жгутик</text>
</g>
<g transform="translate(350,250)">
<rect x="-60" y="-30" width="120" height="60" rx="5" fill="white" stroke="#F9A825" stroke-width="1.2"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="7" fill="#F9A825" text-anchor="middle" font-weight="bold">Строение бактерии</text>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Клеточная стенка</text>
<text x="0" y="6" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Цитоплазма</text>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Нуклеоид (ДНК)</text>
<text x="0" y="28" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Рибосомы (70S)</text>
</g>
'''+ib(30,290,440,25,["Прокариоты: нет ядра, нет мембранных органелл | Формы: кокки, бациллы, вибрионы, спирохеты","Роль: азотфиксация, разложение, болезнетворные, пищевые (молочнокислые)"])+ftr

# 4: Развитие эволюционных идей
svgs[4]=hdr(titles[4],4)+'''
<g transform="translate(250,185)">
<line x1="-180" y1="0" x2="180" y2="0" stroke="#5D4037" stroke-width="2"/>
<path d="M180,0 L175,-5 M180,0 L175,5" stroke="#5D4037" stroke-width="2" fill="none"/>
<!-- Timeline markers -->
<circle cx="-150" cy="0" r="8" fill="#795548" stroke="#4E342E" stroke-width="1.5"/>
<text x="-150" y="20" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Античность</text>
<circle cx="-70" cy="0" r="8" fill="#8D6E63" stroke="#4E342E" stroke-width="1.5"/>
<text x="-70" y="20" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Линней</text>
<text x="-70" y="-18" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">XVIII в.</text>
<circle cx="0" cy="0" r="8" fill="#A1887F" stroke="#4E342E" stroke-width="1.5"/>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Ламарк</text>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">1809</text>
<circle cx="80" cy="0" r="10" fill="#66BB6A" stroke="#2E7D32" stroke-width="2"/>
<text x="80" y="22" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle" font-weight="bold">Дарвин</text>
<text x="80" y="-18" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">1859</text>
<circle cx="160" cy="0" r="8" fill="#4CAF50" stroke="#2E7D32" stroke-width="1.5"/>
<text x="160" y="20" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Синтетич.</text>
<text x="160" y="-18" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">XX в.</text>
</g>
<g transform="translate(90,100)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#8D6E63" stroke-width="1.2"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="6" fill="#8D6E63" text-anchor="middle" font-weight="bold">Ламарк</text>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Наследование</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">приобретённых</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">признаков</text>
</g>
<g transform="translate(400,100)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Дарвин</text>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Естественный</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">отбор — движущая</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">сила эволюции</text>
</g>
'''+ib(30,275,440,35,["Ламарк: стремление к совершенству, упражнение/неупражнение органов","Дарвин: наследственность, изменчивость, естественный отбор, борьба за существование","Синтетическая теория эволюции: объединила генетику и дарвинизм"])+ftr

# 5: Доказательства эволюции
svgs[5]=hdr(titles[5],5)+'''
<g transform="translate(85,150)">
<rect x="-55" y="-50" width="110" height="100" rx="5" fill="white" stroke="#795548" stroke-width="1.5"/>
<text x="0" y="-35" font-family="Arial,sans-serif" font-size="6" fill="#795548" text-anchor="middle" font-weight="bold">Палеонтоло-</text>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="6" fill="#795548" text-anchor="middle" font-weight="bold">гические</text>
<line x1="-40" y1="-18" x2="40" y2="-18" stroke="#795548" stroke-width="0.5"/>
<text x="0" y="-6" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Ископаемые</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">переходные</text>
<text x="0" y="16" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">формы</text>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Археоптерикс</text>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Ихтиостега</text>
</g>
<g transform="translate(250,150)">
<rect x="-55" y="-50" width="110" height="100" rx="5" fill="white" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="-35" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">Сравнительно-</text>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">анатомические</text>
<line x1="-40" y1="-18" x2="40" y2="-18" stroke="#1565C0" stroke-width="0.5"/>
<text x="0" y="-6" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Гомологичные</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">органы</text>
<text x="0" y="16" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Рудименты</text>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Атавизмы</text>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Аналогичные</text>
</g>
<g transform="translate(415,150)">
<rect x="-55" y="-50" width="110" height="100" rx="5" fill="white" stroke="#9C27B0" stroke-width="1.5"/>
<text x="0" y="-35" font-family="Arial,sans-serif" font-size="6" fill="#9C27B0" text-anchor="middle" font-weight="bold">Молекулярно-</text>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="6" fill="#9C27B0" text-anchor="middle" font-weight="bold">генетические</text>
<line x1="-40" y1="-18" x2="40" y2="-18" stroke="#9C27B0" stroke-width="0.5"/>
<text x="0" y="-6" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Сходство ДНК</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Белки-гомологи</text>
<text x="0" y="16" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Цитохром С</text>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Универсальный</text>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">генетич. код</text>
</g>
'''+ib(30,265,440,45,["Гомологичные органы: общее происхождение (рука, крыло, ласт)","Рудименты: аппендикс, копчик, мышцы ушей | Атавизмы: хвост, многососковость","Эмбриологические: сходство зародышей позвоночных на ранних стадиях"])+ftr

# 6: Вид и его критерии
svgs[6]=hdr(titles[6],6)+'''
<g transform="translate(250,175)">
<circle cx="0" cy="0" r="70" fill="#2E7D32" opacity="0.06" stroke="#2E7D32" stroke-width="2"/>
<text x="0" y="-50" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle" font-weight="bold">ВИД</text>
<line x1="-50" y1="-42" x2="50" y2="-42" stroke="#2E7D32" stroke-width="0.8" opacity="0.5"/>
</g>
<!-- Criteria boxes around the circle -->
<g transform="translate(100,90)">
<rect x="-45" y="-15" width="90" height="30" rx="5" fill="white" stroke="#C62828" stroke-width="1.2"/>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">Морфологический</text>
<text x="0" y="9" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Внешнее сходство</text>
</g>
<g transform="translate(250,72)">
<rect x="-45" y="-15" width="90" height="30" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle" font-weight="bold">Генетический</text>
<text x="0" y="9" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Число хромосом</text>
</g>
<g transform="translate(400,90)">
<rect x="-45" y="-15" width="90" height="30" rx="5" fill="white" stroke="#F9A825" stroke-width="1.2"/>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="6" fill="#F9A825" text-anchor="middle" font-weight="bold">Физиологический</text>
<text x="0" y="9" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Процессы жизнед.</text>
</g>
<g transform="translate(80,250)">
<rect x="-45" y="-15" width="90" height="30" rx="5" fill="white" stroke="#9C27B0" stroke-width="1.2"/>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="6" fill="#9C27B0" text-anchor="middle" font-weight="bold">Экологический</text>
<text x="0" y="9" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Место обитания</text>
</g>
<g transform="translate(250,270)">
<rect x="-45" y="-15" width="90" height="30" rx="5" fill="white" stroke="#E65100" stroke-width="1.2"/>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">Географический</text>
<text x="0" y="9" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Ареал вида</text>
</g>
<g transform="translate(420,250)">
<rect x="-45" y="-15" width="90" height="30" rx="5" fill="white" stroke="#5D4037" stroke-width="1.2"/>
<text x="0" y="-2" font-family="Arial,sans-serif" font-size="6" fill="#5D4037" text-anchor="middle" font-weight="bold">Биохимический</text>
<text x="0" y="9" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Состав веществ</text>
</g>
'''+ib(30,295,440,18,["Вид — основная единица классификации | Критерии: морфологический, генетический, физиологический, экологический, географический"])+ftr

# 7: Естественный отбор и формы
svgs[7]=hdr(titles[7],7)+'''
<g transform="translate(250,175)">
<!-- Central concept -->
<circle cx="0" cy="0" r="40" fill="#2E7D32" opacity="0.12" stroke="#2E7D32" stroke-width="2"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Естественный</text>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">отбор</text>
</g>
<!-- Three forms -->
<g transform="translate(85,130)">
<rect x="-60" y="-40" width="120" height="80" rx="5" fill="white" stroke="#C62828" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">Движущий</text>
<line x1="-45" y1="-18" x2="45" y2="-18" stroke="#C62828" stroke-width="0.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Смещение среднего</text>
<text x="0" y="6" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">значения признака</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">При изменении</text>
<text x="0" y="31" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">условий среды</text>
</g>
<g transform="translate(415,130)">
<rect x="-60" y="-40" width="120" height="80" rx="5" fill="white" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">Стабилизирующий</text>
<line x1="-45" y1="-18" x2="45" y2="-18" stroke="#1565C0" stroke-width="0.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Сохранение</text>
<text x="0" y="6" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">среднего значения</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Устранение</text>
<text x="0" y="31" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">крайних форм</text>
</g>
<g transform="translate(250,280)">
<rect x="-60" y="-25" width="120" height="50" rx="5" fill="white" stroke="#F9A825" stroke-width="1.5"/>
<text x="0" y="-10" font-family="Arial,sans-serif" font-size="7" fill="#F9A825" text-anchor="middle" font-weight="bold">Разрывающий</text>
<line x1="-45" y1="-3" x2="45" y2="-3" stroke="#F9A825" stroke-width="0.5"/>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Сохранение крайних</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">форм, элиминация средних</text>
</g>
'''+ftr

# 8: Приспособленность организмов
svgs[8]=hdr(titles[8],8)+'''
<!-- Protective coloration -->
<g transform="translate(100,120)">
<rect x="-60" y="-30" width="120" height="60" rx="5" fill="#8BC34A" opacity="0.2" stroke="#558B2F" stroke-width="1.5"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#558B2F" text-anchor="middle" font-weight="bold">Покровительственная</text>
<text x="0" y="-7" font-family="Arial,sans-serif" font-size="6" fill="#558B2F" text-anchor="middle" font-weight="bold">окраска</text>
<line x1="-45" y1="-1" x2="45" y2="-1" stroke="#558B2F" stroke-width="0.5"/>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Маскировка под фон</text>
<text x="0" y="21" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Белый медведь</text>
</g>
<!-- Mimicry -->
<g transform="translate(280,120)">
<rect x="-60" y="-30" width="120" height="60" rx="5" fill="#FF9800" opacity="0.15" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle" font-weight="bold">Мимикрия</text>
<line x1="-45" y1="-7" x2="45" y2="-7" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Сходство с опасным</text>
<text x="0" y="16" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">видом (оса-муха)</text>
</g>
<!-- Warning coloration -->
<g transform="translate(430,120)">
<rect x="-45" y="-30" width="90" height="60" rx="5" fill="#F44336" opacity="0.15" stroke="#C62828" stroke-width="1.5"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">Предупреждающая</text>
<text x="0" y="-7" font-family="Arial,sans-serif" font-size="6" fill="#C62828" text-anchor="middle" font-weight="bold">окраска</text>
<line x1="-35" y1="-1" x2="35" y2="-1" stroke="#C62828" stroke-width="0.5"/>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Яркая = опасный</text>
<text x="0" y="21" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Осы, лягушки</text>
</g>
<!-- Behavioral adaptations -->
<g transform="translate(160,230)">
<rect x="-60" y="-25" width="120" height="50" rx="5" fill="#9C27B0" opacity="0.15" stroke="#7B1FA2" stroke-width="1.5"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Поведенческие</text>
<line x1="-45" y1="-5" x2="45" y2="-5" stroke="#7B1FA2" stroke-width="0.5"/>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Замирание, бегство,</text>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">стайная защита</text>
</g>
<!-- Structural adaptations -->
<g transform="translate(370,230)">
<rect x="-60" y="-25" width="120" height="50" rx="5" fill="#1565C0" opacity="0.15" stroke="#0D47A1" stroke-width="1.5"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="6" fill="#0D47A1" text-anchor="middle" font-weight="bold">Строение тела</text>
<line x1="-45" y1="-5" x2="45" y2="-5" stroke="#0D47A1" stroke-width="0.5"/>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Форма тела, колючки,</text>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">панцирь, копыта</text>
</g>
'''+ib(30,280,440,30,["Приспособленность — результат естественного отбора","Относительность: приспособление к конкретным условиям, при изменении среды может стать бесполезным"])+ftr

# 9: Возникновение жизни на Земле
svgs[9]=hdr(titles[9],9)+'''
<!-- Timeline of origin -->
<line x1="50" y1="180" x2="450" y2="180" stroke="#5D4037" stroke-width="2"/>
<path d="M450,180 L445,175 M450,180 L445,185" stroke="#5D4037" stroke-width="2" fill="none"/>
<circle cx="80" cy="180" r="7" fill="#795548" stroke="#4E342E" stroke-width="1.5"/>
<text x="80" y="200" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Земля</text>
<text x="80" y="210" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">4.6 млрд</text>
<circle cx="150" cy="180" r="7" fill="#8D6E63" stroke="#4E342E" stroke-width="1.5"/>
<text x="150" y="200" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Хим. эвол.</text>
<text x="150" y="210" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">4-3.5 млрд</text>
<circle cx="230" cy="180" r="7" fill="#A1887F" stroke="#4E342E" stroke-width="1.5"/>
<text x="230" y="200" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Коацерваты</text>
<text x="230" y="210" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">3.8 млрд</text>
<circle cx="310" cy="180" r="8" fill="#66BB6A" stroke="#2E7D32" stroke-width="1.5"/>
<text x="310" y="200" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Прокариоты</text>
<text x="310" y="210" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">3.5 млрд</text>
<circle cx="390" cy="180" r="8" fill="#4CAF50" stroke="#2E7D32" stroke-width="1.5"/>
<text x="390" y="200" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Фотосинтез</text>
<text x="390" y="210" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">2.5 млрд</text>
<!-- Hypotheses -->
<g transform="translate(120,105)">
<rect x="-55" y="-20" width="110" height="40" rx="5" fill="white" stroke="#795548" stroke-width="1.2"/>
<text x="0" y="-8" font-family="Arial,sans-serif" font-size="6" fill="#795548" text-anchor="middle" font-weight="bold">Опарин-Холдейн</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Химическая эволюция</text>
<text x="0" y="15" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">из неорганических веществ</text>
</g>
<g transform="translate(380,105)">
<rect x="-55" y="-20" width="110" height="40" rx="5" fill="white" stroke="#9C27B0" stroke-width="1.2"/>
<text x="0" y="-8" font-family="Arial,sans-serif" font-size="6" fill="#9C27B0" text-anchor="middle" font-weight="bold">Панспермия</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Занос из космоса</text>
<text x="0" y="15" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">(микроорганизмы)</text>
</g>
'''+ib(30,240,440,50,["Опарин-Холдейн: из неорганических веществ под действием электрич. разрядов и УФ","Коацерваты — капли с оболочкой | Самозарождение отвергнуто Пастером","Этапы: неорганика - органика - биополимеры - коацерваты - пробионты - клетки"])+ftr

# 10: Развитие жизни на Земле
svgs[10]=hdr(titles[10],10)+'''
<!-- Geological eras timeline -->
<g transform="translate(70,80)">
<rect x="-45" y="-20" width="90" height="40" rx="5" fill="#795548" stroke="#4E342E" stroke-width="1.5"/>
<text x="0" y="-7" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle" font-weight="bold">Архей</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#D7CCC8" text-anchor="middle">3.5-2.5 млрд</text>
<text x="0" y="15" font-family="Arial,sans-serif" font-size="5" fill="#D7CCC8" text-anchor="middle">Прокариоты</text>
</g>
<g transform="translate(180,80)">
<rect x="-45" y="-20" width="90" height="40" rx="5" fill="#8D6E63" stroke="#4E342E" stroke-width="1.5"/>
<text x="0" y="-7" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle" font-weight="bold">Протерозой</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#D7CCC8" text-anchor="middle">2.5-0.54 млрд</text>
<text x="0" y="15" font-family="Arial,sans-serif" font-size="5" fill="#D7CCC8" text-anchor="middle">Эукариоты</text>
</g>
<g transform="translate(290,80)">
<rect x="-45" y="-20" width="90" height="40" rx="5" fill="#4CAF50" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-7" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle" font-weight="bold">Палеозой</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#C8E6C9" text-anchor="middle">540-248 млн</text>
<text x="0" y="15" font-family="Arial,sans-serif" font-size="5" fill="#C8E6C9" text-anchor="middle">Рыбы, амфибии</text>
</g>
<g transform="translate(365,145)">
<rect x="-45" y="-20" width="90" height="40" rx="5" fill="#FF9800" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="-7" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle" font-weight="bold">Мезозой</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#FFE0B2" text-anchor="middle">248-65 млн</text>
<text x="0" y="15" font-family="Arial,sans-serif" font-size="5" fill="#FFE0B2" text-anchor="middle">Рептилии</text>
</g>
<g transform="translate(440,210)">
<rect x="-45" y="-20" width="90" height="40" rx="5" fill="#42A5F5" stroke="#1565C0" stroke-width="1.5"/>
<text x="0" y="-7" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle" font-weight="bold">Кайнозой</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#BBDEFB" text-anchor="middle">65-0 млн</text>
<text x="0" y="15" font-family="Arial,sans-serif" font-size="5" fill="#BBDEFB" text-anchor="middle">Млекопитающие</text>
</g>
<!-- Arrow showing progression -->
<path d="M115,100 Q220,100 290,100 Q330,110 365,125 Q400,140 395,145" stroke="#5D4037" stroke-width="1.5" fill="none" stroke-dasharray="4,3"/>
<path d="M410,165 Q440,175 440,190" stroke="#5D4037" stroke-width="1.5" fill="none" stroke-dasharray="4,3"/>
'''+ib(30,275,440,35,["Архей: зарождение жизни | Протерозой: кислородная катастрофа, эукариоты","Палеозой: выход на сушу | Мезозой: эпоха рептилий | Кайнозой: эпоха млекопитающих","Вымирания: ордовикское, девонское, пермское, триасовое, меловое"])+ftr

# 11: Происхождение человека
svgs[11]=hdr(titles[11],11)+'''
<line x1="50" y1="185" x2="450" y2="185" stroke="#5D4037" stroke-width="2"/>
<path d="M450,185 L445,180 M450,185 L445,190" stroke="#5D4037" stroke-width="2" fill="none"/>
<circle cx="80" cy="185" r="6" fill="#795548" stroke="#4E342E" stroke-width="1.5"/>
<text x="80" y="205" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Дриопитек</text>
<text x="80" y="215" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">20 млн</text>
<circle cx="155" cy="185" r="6" fill="#8D6E63" stroke="#4E342E" stroke-width="1.5"/>
<text x="155" y="205" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Австралопитек</text>
<text x="155" y="215" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">4 млн</text>
<circle cx="230" cy="185" r="6" fill="#A1887F" stroke="#4E342E" stroke-width="1.5"/>
<text x="230" y="205" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Ч. умелый</text>
<text x="230" y="215" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">2 млн</text>
<circle cx="300" cy="185" r="7" fill="#BCAAA4" stroke="#4E342E" stroke-width="1.5"/>
<text x="300" y="205" font-family="Arial,sans-serif" font-size="5" fill="#4E342E" text-anchor="middle">Неандерталец</text>
<text x="300" y="215" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">200 тыс.</text>
<circle cx="390" cy="185" r="8" fill="#66BB6A" stroke="#2E7D32" stroke-width="2"/>
<text x="390" y="205" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle" font-weight="bold">Homo sapiens</text>
<text x="390" y="215" font-family="Arial,sans-serif" font-size="4" fill="#888" text-anchor="middle">40 тыс.</text>
<!-- Brain growth -->
<circle cx="80" cy="115" r="5" fill="#EFEBE9" stroke="#795548" stroke-width="1"/>
<circle cx="155" cy="108" r="7" fill="#EFEBE9" stroke="#8D6E63" stroke-width="1"/>
<circle cx="230" cy="100" r="9" fill="#EFEBE9" stroke="#A1887F" stroke-width="1"/>
<circle cx="300" cy="90" r="12" fill="#EFEBE9" stroke="#BCAAA4" stroke-width="1"/>
<circle cx="390" cy="78" r="15" fill="#EFEBE9" stroke="#66BB6A" stroke-width="1.5"/>
<text x="250" y="75" font-family="Arial,sans-serif" font-size="7" fill="#5D4037" text-anchor="middle">Рост мозга</text>
'''+ib(30,240,440,50,["Движущие силы: биологические (наследственность, отбор) и социальные (труд, речь)","Труд: изготовление орудий | Речь: передача опыта | Общество: совместная деятельность","Дриопитек - Австралопитек - Ч.умелый - Ч.прямоходящий - Неандерталец - Кроманьонец"])+ftr

# 12: Основные понятия генетики
svgs[12]=hdr(titles[12],12)+'''
<g transform="translate(250,175)">
<circle cx="0" cy="0" r="65" fill="#2E7D32" opacity="0.06" stroke="#2E7D32" stroke-width="2"/>
</g>
<g transform="translate(120,110)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#C62828" stroke-width="1.2"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">Ген</text>
<line x1="-40" y1="-5" x2="40" y2="-5" stroke="#C62828" stroke-width="0.5"/>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Участок ДНК,</text>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">кодирующий белок</text>
</g>
<g transform="translate(380,110)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">Аллель</text>
<line x1="-40" y1="-5" x2="40" y2="-5" stroke="#1565C0" stroke-width="0.5"/>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Разные формы</text>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">одного гена (A, a)</text>
</g>
<g transform="translate(120,230)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#9C27B0" stroke-width="1.2"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="7" fill="#9C27B0" text-anchor="middle" font-weight="bold">Генотип</text>
<line x1="-40" y1="-5" x2="40" y2="-5" stroke="#9C27B0" stroke-width="0.5"/>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Совокупность</text>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">всех генов (AaBb)</text>
</g>
<g transform="translate(380,230)">
<rect x="-55" y="-25" width="110" height="50" rx="5" fill="white" stroke="#E65100" stroke-width="1.2"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">Фенотип</text>
<line x1="-40" y1="-5" x2="40" y2="-5" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Внешние признаки</text>
<text x="0" y="17" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">цвет, форма, размер</text>
</g>
'''+ib(30,290,440,22,["Гомозигота: AA или aa | Гетерозигота: Aa | Доминантный: A | Рецессивный: a","Генотип + Среда = Фенотип | Аллельные гены в одной хромосомной паре"])+ftr

# 13: Законы Менделя
svgs[13]=hdr(titles[13],13)+'''
<!-- Punnett square for monohybrid cross -->
<g transform="translate(150,175)">
<text x="0" y="-65" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Моногибридное скрещивание</text>
<text x="0" y="-52" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Aa x Aa</text>
<!-- Grid -->
<line x1="-40" y1="-40" x2="-40" y2="40" stroke="#2E7D32" stroke-width="1.5"/>
<line x1="-40" y1="-40" x2="40" y2="-40" stroke="#2E7D32" stroke-width="1.5"/>
<rect x="-40" y="-40" width="80" height="80" fill="none" stroke="#2E7D32" stroke-width="1"/>
<line x1="-40" y1="0" x2="40" y2="0" stroke="#2E7D32" stroke-width="0.8"/>
<line x1="0" y1="-40" x2="0" y2="40" stroke="#2E7D32" stroke-width="0.8"/>
<!-- Headers -->
<text x="-20" y="-45" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">A</text>
<text x="20" y="-45" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">a</text>
<text x="-50" y="-17" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">A</text>
<text x="-50" y="23" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">a</text>
<!-- Cells -->
<rect x="-40" y="-40" width="40" height="40" fill="#C8E6C9" opacity="0.5"/>
<rect x="0" y="-40" width="40" height="40" fill="#C8E6C9" opacity="0.3"/>
<rect x="-40" y="0" width="40" height="40" fill="#C8E6C9" opacity="0.3"/>
<rect x="0" y="0" width="40" height="40" fill="white" opacity="0.5"/>
<text x="-20" y="-15" font-family="Arial,sans-serif" font-size="9" fill="#1B5E20" text-anchor="middle" font-weight="bold">AA</text>
<text x="20" y="-15" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Aa</text>
<text x="-20" y="25" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Aa</text>
<text x="20" y="25" font-family="Arial,sans-serif" font-size="9" fill="#888" text-anchor="middle" font-weight="bold">aa</text>
</g>
<!-- Ratios and laws -->
<g transform="translate(380,140)">
<rect x="-70" y="-55" width="140" height="110" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Законы Менделя</text>
<line x1="-55" y1="-33" x2="55" y2="-33" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">I: Единообразие F1</text>
<text x="0" y="-8" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">(доминирование)</text>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">II: Расщепление 3:1</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">в F2</text>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">III: Независимое</text>
<text x="0" y="48" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">наследование (9:3:3:1)</text>
</g>
'''+ftr

# 14: Решение генетических задач
svgs[14]=hdr(titles[14],14)+'''
<!-- Dihybrid cross example -->
<g transform="translate(250,100)">
<text x="0" y="0" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Дигибридное скрещивание</text>
<text x="0" y="15" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">AaBb x AaBb</text>
</g>
<!-- Gametes -->
<g transform="translate(120,145)">
<rect x="-50" y="-12" width="100" height="24" rx="5" fill="white" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="-1" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Гаметы:</text>
<text x="0" y="10" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">AB Ab aB ab</text>
</g>
<!-- F2 ratio -->
<g transform="translate(350,145)">
<rect x="-80" y="-25" width="160" height="50" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Расщепление F2</text>
<text x="0" y="2" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">9 : 3 : 3 : 1</text>
<text x="0" y="16" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">A_B_ : A_bb : aaB_ : aabb</text>
</g>
<!-- Steps -->
<g transform="translate(100,210)">
<rect x="-60" y="-20" width="120" height="40" rx="5" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="-8" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">1. Определить генотипы</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">родителей</text>
</g>
<g transform="translate(250,210)">
<rect x="-60" y="-20" width="120" height="40" rx="5" fill="#A5D6A7" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="-8" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">2. Записать гаметы</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">по правилу чистоты</text>
</g>
<g transform="translate(400,210)">
<rect x="-60" y="-20" width="120" height="40" rx="5" fill="#81C784" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="-8" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">3. Решётка Пеннета</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">и анализ F2</text>
</g>
'''+ib(30,265,440,45,["Правило чистоты гамет: в гамету попадает один аллель каждого гена","Моногибридное: 3:1 | Неполное доминирование: 1:2:1 | Дигибридное: 9:3:3:1","Анализирующее скрещивание: Aa x aa = 1:1 для определения генотипа"])+ftr

# 15: Хромосомная теория и сцепление генов
svgs[15]=hdr(titles[15],15)+'''
<!-- Chromosome with genes -->
<g transform="translate(140,180)">
<rect x="-15" y="-70" width="30" height="120" rx="12" fill="#CE93D8" stroke="#7B1FA2" stroke-width="2"/>
<rect x="-15" y="-5" width="30" height="10" fill="#E8F5E9" stroke="#7B1FA2" stroke-width="1"/>
<!-- Gene markers -->
<circle cx="0" cy="-50" r="6" fill="#E53935" stroke="#C62828" stroke-width="1"/>
<text x="25" y="-47" font-family="Arial,sans-serif" font-size="6" fill="#C62828" font-weight="bold">A</text>
<circle cx="0" cy="-30" r="6" fill="#1565C0" stroke="#0D47A1" stroke-width="1"/>
<text x="25" y="-27" font-family="Arial,sans-serif" font-size="6" fill="#0D47A1" font-weight="bold">B</text>
<circle cx="0" cy="10" r="6" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
<text x="25" y="13" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" font-weight="bold">C</text>
<circle cx="0" cy="35" r="6" fill="#FF9800" stroke="#E65100" stroke-width="1"/>
<text x="25" y="38" font-family="Arial,sans-serif" font-size="6" fill="#E65100" font-weight="bold">D</text>
<text x="0" y="68" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Хромосома</text>
</g>
<!-- Crossing over -->
<g transform="translate(300,165)">
<rect x="-70" y="-60" width="140" height="120" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.5"/>
<text x="0" y="-45" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Кроссинговер</text>
<line x1="-45" y1="-30" x2="-45" y2="40" stroke="#CE93D8" stroke-width="3"/>
<line x1="45" y1="-30" x2="45" y2="40" stroke="#AB47BC" stroke-width="3"/>
<path d="M-45,-10 Q0,-20 45,-10" stroke="#E53935" stroke-width="2" fill="none"/>
<path d="M-45,10 Q0,20 45,10" stroke="#1565C0" stroke-width="2" fill="none"/>
<circle cx="-45" cy="-25" r="4" fill="#E53935" stroke="#C62828" stroke-width="0.8"/>
<circle cx="45" cy="-25" r="4" fill="#1565C0" stroke="#0D47A1" stroke-width="0.8"/>
<circle cx="-45" cy="30" r="4" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.8"/>
<circle cx="45" cy="30" r="4" fill="#FF9800" stroke="#E65100" stroke-width="0.8"/>
<text x="0" y="52" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="middle">Обмен участками</text>
</g>
'''+ib(30,275,440,35,["Морган: гены в хромосоме сцеплены | Группа сцепления = хромосома","Кроссинговер: обмен участками гомологичных хромосом в мейозе","Расстояние между генами: 1% кроссинговера = 1 морганида | Картирование хромосом"])+ftr

# 16: Генетика пола и наследование, сцепленное с полом
svgs[16]=hdr(titles[16],16)+'''
<!-- Sex chromosomes -->
<g transform="translate(130,170)">
<!-- X chromosome -->
<rect x="-30" y="-50" width="22" height="80" rx="11" fill="#E53935" opacity="0.3" stroke="#C62828" stroke-width="2"/>
<text x="-19" y="42" font-family="Arial,sans-serif" font-size="8" fill="#C62828" text-anchor="middle" font-weight="bold">X</text>
<!-- X chromosome 2 -->
<rect x="8" y="-50" width="22" height="80" rx="11" fill="#E53935" opacity="0.3" stroke="#C62828" stroke-width="2"/>
<text x="19" y="42" font-family="Arial,sans-serif" font-size="8" fill="#C62828" text-anchor="middle" font-weight="bold">X</text>
<text x="0" y="60" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">XX — Женщина</text>
</g>
<g transform="translate(310,170)">
<!-- X chromosome -->
<rect x="-30" y="-50" width="22" height="80" rx="11" fill="#E53935" opacity="0.3" stroke="#C62828" stroke-width="2"/>
<text x="-19" y="42" font-family="Arial,sans-serif" font-size="8" fill="#C62828" text-anchor="middle" font-weight="bold">X</text>
<!-- Y chromosome -->
<rect x="8" y="-40" width="14" height="50" rx="5" fill="#1565C0" opacity="0.3" stroke="#0D47A1" stroke-width="2"/>
<text x="15" y="25" font-family="Arial,sans-serif" font-size="8" fill="#0D47A1" text-anchor="middle" font-weight="bold">Y</text>
<text x="0" y="60" font-family="Arial,sans-serif" font-size="7" fill="#0D47A1" text-anchor="middle" font-weight="bold">XY — Мужчина</text>
</g>
<!-- Inheritance pattern -->
<g transform="translate(430,150)">
<rect x="-50" y="-50" width="100" height="100" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-35" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Сцеплено с X</text>
<line x1="-35" y1="-28" x2="35" y2="-28" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Дальтонизм</text>
<text x="0" y="-3" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Гемофилия</text>
<line x1="-35" y1="5" x2="35" y2="5" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">X(d)X — носитель</text>
<text x="0" y="30" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">X(d)Y — болен</text>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">X(D)X(D) — здорова</text>
</g>
'''+ftr

# 17: Изменчивость и её виды
svgs[17]=hdr(titles[17],17)+'''
<g transform="translate(120,140)">
<rect x="-75" y="-55" width="150" height="110" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Наследственная</text>
<text x="0" y="-28" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">(генотипическая)</text>
<line x1="-60" y1="-20" x2="60" y2="-20" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="-7" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Мутационная</text>
<text x="0" y="5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Генные, хромосомные,</text>
<text x="0" y="15" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">геномные мутации</text>
<text x="0" y="32" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Комбинативная</text>
<text x="0" y="44" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Кроссинговер, перекомб.</text>
</g>
<g transform="translate(380,140)">
<rect x="-75" y="-55" width="150" height="110" rx="5" fill="white" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">Ненаследственная</text>
<text x="0" y="-28" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">(модификационная)</text>
<line x1="-60" y1="-20" x2="60" y2="-20" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Изменение фенотипа</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">под действием среды</text>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Не передаётся по</text>
<text x="0" y="34" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">наследству</text>
<text x="0" y="48" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Норма реакции</text>
</g>
<!-- Variation curve -->
<g transform="translate(250,265)">
<rect x="-100" y="-15" width="200" height="30" rx="5" fill="white" stroke="#2E7D32" stroke-width="1" opacity="0.9"/>
<path d="M-80,5 Q-60,-10 -40,-10 Q-20,-10 0,-10 Q20,-10 40,-10 Q60,-10 80,5" fill="none" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Вариационная кривая</text>
</g>
'''+ftr

# 18: Селекция растений и животных
svgs[18]=hdr(titles[18],18)+'''
<g transform="translate(120,150)">
<rect x="-70" y="-55" width="140" height="110" rx="5" fill="white" stroke="#4CAF50" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="8" fill="#4CAF50" text-anchor="middle" font-weight="bold">Селекция растений</text>
<line x1="-55" y1="-33" x2="55" y2="-33" stroke="#4CAF50" stroke-width="0.5"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Гибридизация</text>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Полиплоидия</text>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Отбор: массовый,</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">индивидуальный</text>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="5" fill="#4CAF50" text-anchor="middle">Мичурин, Вавилов</text>
</g>
<g transform="translate(380,150)">
<rect x="-70" y="-55" width="140" height="110" rx="5" fill="white" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="-40" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">Селекция животных</text>
<line x1="-55" y1="-33" x2="55" y2="-33" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Скрещивание</text>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">инбридинг, аутбридинг</text>
<text x="0" y="8" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Отбор по линии</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Проверка по потомству</text>
<text x="0" y="38" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">Гетерозис (гибридная сила)</text>
</g>
'''+ib(30,280,440,30,["Центры происхождения культурных растений (Вавилов): 8 центров","Закон гомологических рядов: сходные мутации у родственных видов","Полиплоидия: увеличение числа хромосомных наборов (3n, 4n)"])+ftr

# 19: Экологические факторы
svgs[19]=hdr(titles[19],19)+'''
<g transform="translate(120,120)">
<rect x="-70" y="-35" width="140" height="70" rx="5" fill="#FF9800" opacity="0.15" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">Абиотические</text>
<line x1="-55" y1="-12" x2="55" y2="-12" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Свет, температура,</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">влажность, воздух,</text>
<text x="0" y="24" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">давление, pH</text>
</g>
<g transform="translate(380,120)">
<rect x="-70" y="-35" width="140" height="70" rx="5" fill="#4CAF50" opacity="0.15" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Биотические</text>
<line x1="-55" y1="-12" x2="55" y2="-12" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Хищничество, конкуренция,</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">симбиоз, паразитизм,</text>
<text x="0" y="24" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">мутуализм, комменсализм</text>
</g>
<g transform="translate(250,230)">
<rect x="-70" y="-35" width="140" height="70" rx="5" fill="#9C27B0" opacity="0.15" stroke="#7B1FA2" stroke-width="1.5"/>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="8" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Антропогенные</text>
<line x1="-55" y1="-12" x2="55" y2="-12" stroke="#7B1FA2" stroke-width="0.5"/>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Загрязнение, вырубка,</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">осушение, строительство,</text>
<text x="0" y="24" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">интродукция видов</text>
</g>
'''+ib(30,285,440,25,["Закон оптимума: наилучшее значение фактора для организма","Закон минимума Либиха: фактор в минимуме ограничивает рост","Ограничивающий фактор: фактор, отклоняющийся от оптимума"])+ftr

# 20: Популяции и сообщества
svgs[20]=hdr(titles[20],20)+'''
<g transform="translate(130,175)">
<circle cx="0" cy="0" r="60" fill="#2E7D32" opacity="0.06" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Популяция</text>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Группа особей</text>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">одного вида</text>
<!-- Individual dots -->
<circle cx="-25" cy="20" r="3" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
<circle cx="-10" cy="30" r="3" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
<circle cx="5" cy="20" r="3" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
<circle cx="20" cy="30" r="3" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
<circle cx="-15" cy="40" r="3" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
<circle cx="10" cy="40" r="3" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.8"/>
</g>
<g transform="translate(380,160)">
<rect x="-80" y="-60" width="160" height="120" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="0" y="-45" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Характеристики популяции</text>
<line x1="-65" y1="-38" x2="65" y2="-38" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="-24" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Численность</text>
<text x="0" y="-12" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Плотность</text>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Рождаемость / Смертность</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Возрастной состав</text>
<text x="0" y="24" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Половой состав</text>
<text x="0" y="36" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Генетическое разнообразие</text>
<text x="0" y="48" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Динамика (рост/спад)</text>
</g>
'''+ftr

# 21: Экосистемы и пищевые цепи
svgs[21]=hdr(titles[21],21)+'''
<!-- Ecological pyramid -->
<g transform="translate(130,200)">
<polygon points="0,-70 50,-70 60,50 -60,50" fill="#4CAF50" opacity="0.15" stroke="#2E7D32" stroke-width="1.5"/>
<rect x="-50" y="35" width="100" height="15" rx="2" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
<text x="0" y="46" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle">Редуценты</text>
<rect x="-35" y="15" width="70" height="15" rx="2" fill="#FF9800" stroke="#E65100" stroke-width="1"/>
<text x="0" y="26" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle">Консументы II</text>
<rect x="-20" y="-5" width="40" height="15" rx="2" fill="#E53935" stroke="#C62828" stroke-width="1"/>
<text x="0" y="6" font-family="Arial,sans-serif" font-size="5" fill="white" text-anchor="middle">Консум. I</text>
<rect x="-10" y="-30" width="20" height="15" rx="2" fill="#4CAF50" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="4" fill="white" text-anchor="middle">Продуц.</text>
</g>
<!-- Food chain -->
<g transform="translate(350,175)">
<rect x="-100" y="-60" width="200" height="120" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-45" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Пищевая цепь</text>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="6" fill="#4CAF50" text-anchor="middle">Растение</text>
<line x1="0" y1="-22" x2="0" y2="-15" stroke="#2E7D32" stroke-width="1"/>
<path d="M0,-15 L-3,-18 M0,-15 L3,-18" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle">Травоядное</text>
<line x1="0" y1="-2" x2="0" y2="5" stroke="#2E7D32" stroke-width="1"/>
<path d="M0,5 L-3,2 M0,5 L3,2" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="18" font-family="Arial,sans-serif" font-size="6" fill="#FF9800" text-anchor="middle">Хищник</text>
<line x1="0" y1="21" x2="0" y2="28" stroke="#2E7D32" stroke-width="1"/>
<path d="M0,28 L-3,25 M0,28 L3,25" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="6" fill="#8D6E63" text-anchor="middle">Редуцент</text>
<text x="0" y="55" font-family="Arial,sans-serif" font-size="5" fill="#888" text-anchor="middle">Правило 10% энергии</text>
</g>
'''+ftr

# 22: Сукцессия — смена экосистем
svgs[22]=hdr(titles[22],22)+'''
<!-- Succession stages -->
<line x1="50" y1="190" x2="450" y2="190" stroke="#5D4037" stroke-width="2"/>
<path d="M450,190 L445,185 M450,190 L445,195" stroke="#5D4037" stroke-width="2" fill="none"/>
<!-- Stage 1 -->
<g transform="translate(100,170)">
<rect x="-15" y="10" width="30" height="10" rx="2" fill="#BCAAA4" stroke="#795548" stroke-width="1"/>
<line x1="-5" y1="10" x2="-5" y2="5" stroke="#66BB6A" stroke-width="1"/>
<line x1="5" y1="10" x2="5" y2="5" stroke="#66BB6A" stroke-width="1"/>
<text x="0" y="32" font-family="Arial,sans-serif" font-size="5" fill="#5D4037" text-anchor="middle">Лишайники</text>
</g>
<!-- Stage 2 -->
<g transform="translate(180,160)">
<rect x="-20" y="20" width="40" height="10" rx="2" fill="#8D6E63" stroke="#5D4037" stroke-width="1"/>
<line x1="-8" y1="20" x2="-8" y2="5" stroke="#66BB6A" stroke-width="1.5"/>
<line x1="8" y1="20" x2="8" y2="5" stroke="#66BB6A" stroke-width="1.5"/>
<line x1="0" y1="20" x2="0" y2="0" stroke="#4CAF50" stroke-width="2"/>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="5" fill="#5D4037" text-anchor="middle">Мхи и травы</text>
</g>
<!-- Stage 3 -->
<g transform="translate(270,150)">
<rect x="-25" y="30" width="50" height="10" rx="2" fill="#795548" stroke="#4E342E" stroke-width="1"/>
<line x1="0" y1="30" x2="0" y2="5" stroke="#4CAF50" stroke-width="2.5"/>
<circle cx="0" cy="0" r="12" fill="#4CAF50" opacity="0.3" stroke="#2E7D32" stroke-width="1"/>
<text x="0" y="52" font-family="Arial,sans-serif" font-size="5" fill="#5D4037" text-anchor="middle">Кустарники</text>
</g>
<!-- Stage 4 -->
<g transform="translate(370,140)">
<rect x="-30" y="40" width="60" height="10" rx="2" fill="#5D4037" stroke="#3E2723" stroke-width="1"/>
<line x1="-10" y1="40" x2="-10" y2="5" stroke="#4CAF50" stroke-width="3"/>
<line x1="10" y1="40" x2="10" y2="0" stroke="#388E3C" stroke-width="3"/>
<circle cx="-10" cy="-5" r="15" fill="#4CAF50" opacity="0.3" stroke="#2E7D32" stroke-width="1"/>
<circle cx="10" cy="-10" r="18" fill="#388E3C" opacity="0.3" stroke="#1B5E20" stroke-width="1"/>
<text x="0" y="62" font-family="Arial,sans-serif" font-size="5" fill="#5D4037" text-anchor="middle">Лес (климакс)</text>
</g>
<text x="250" y="95" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">Первичная сукцессия</text>
'''+ib(30,275,440,35,["Первичная: на безжизненном субстрате (лава, песок)","Вторичная: после нарушения (пожар, вырубка) на сохранившейся почве","Климаксовое сообщество: стабильное, самоподдерживающееся"])+ftr

# 23: Биосфера и живое вещество
svgs[23]=hdr(titles[23],23)+'''
<!-- Earth-like sphere -->
<g transform="translate(250,175)">
<circle cx="0" cy="0" r="65" fill="#42A5F5" opacity="0.15" stroke="#1565C0" stroke-width="2"/>
<!-- Atmosphere -->
<ellipse cx="0" cy="-40" rx="55" ry="12" fill="#90CAF9" opacity="0.3" stroke="#42A5F5" stroke-width="1"/>
<text x="0" y="-38" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">Атмосфера</text>
<!-- Hydrosphere -->
<ellipse cx="0" cy="20" rx="50" ry="18" fill="#1565C0" opacity="0.2" stroke="#0D47A1" stroke-width="1"/>
<text x="0" y="22" font-family="Arial,sans-serif" font-size="5" fill="#0D47A1" text-anchor="middle">Гидросфера</text>
<!-- Lithosphere -->
<ellipse cx="0" cy="50" rx="40" ry="10" fill="#8D6E63" opacity="0.3" stroke="#5D4037" stroke-width="1"/>
<text x="0" y="52" font-family="Arial,sans-serif" font-size="5" fill="#5D4037" text-anchor="middle">Литосфера</text>
<text x="0" y="-60" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Биосфера</text>
</g>
<!-- Vernadsky info -->
<g transform="translate(420,120)">
<rect x="-50" y="-30" width="100" height="60" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="0" y="-18" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">В.И. Вернадский</text>
<line x1="-35" y1="-10" x2="35" y2="-10" stroke="#2E7D32" stroke-width="0.5"/>
<text x="0" y="2" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Живое вещество</text>
<text x="0" y="14" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Биокосное вещество</text>
<text x="0" y="26" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Косное вещество</text>
</g>
'''+ib(30,280,440,30,["Биосфера: оболочка Земли, заселённая живыми организмами","Живое вещество: совокупность всех организмов | Масса: 2.4 x 10^12 т","Функции: газовая, концентрационная, окислительно-восстановительная"])+ftr

# 24: Влияние человека на биосферу
svgs[24]=hdr(titles[24],24)+'''
<g transform="translate(90,130)">
<rect x="-55" y="-35" width="110" height="70" rx="5" fill="#F44336" opacity="0.1" stroke="#C62828" stroke-width="1.5"/>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="7" fill="#C62828" text-anchor="middle" font-weight="bold">Загрязнение</text>
<line x1="-40" y1="-12" x2="40" y2="-12" stroke="#C62828" stroke-width="0.5"/>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Атмосферы (CO2, SO2)</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Гидросферы (нефть)</text>
<text x="0" y="24" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Почвы (пестициды)</text>
</g>
<g transform="translate(250,130)">
<rect x="-55" y="-35" width="110" height="70" rx="5" fill="#FF9800" opacity="0.1" stroke="#E65100" stroke-width="1.5"/>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">Истощение</text>
<line x1="-40" y1="-12" x2="40" y2="-12" stroke="#E65100" stroke-width="0.5"/>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Вырубка лесов</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Истощение почв</text>
<text x="0" y="24" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Перелов рыбы</text>
</g>
<g transform="translate(410,130)">
<rect x="-55" y="-35" width="110" height="70" rx="5" fill="#9C27B0" opacity="0.1" stroke="#7B1FA2" stroke-width="1.5"/>
<text x="0" y="-20" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Разрушение</text>
<line x1="-40" y1="-12" x2="40" y2="-12" stroke="#7B1FA2" stroke-width="0.5"/>
<text x="0" y="0" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Озонового слоя</text>
<text x="0" y="12" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Мест обитания</text>
<text x="0" y="24" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Биоразнообразия</text>
</g>
'''+ib(30,230,440,55,["Глобальное потепление: парниковые газы (CO2, CH4) | Средняя t +1.1C","Кислотные дожги: SO2 + H2O | Опустынивание: 6 млн га/год","Красная книга: исчезающие виды | Биоразнообразие сокращается в 1000 раз быстрее нормы"])+ftr

# 25: Охрана природы
svgs[25]=hdr(titles[25],25)+'''
<g transform="translate(100,140)">
<rect x="-60" y="-40" width="120" height="80" rx="5" fill="white" stroke="#4CAF50" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#4CAF50" text-anchor="middle" font-weight="bold">Заповедники</text>
<line x1="-45" y1="-18" x2="45" y2="-18" stroke="#4CAF50" stroke-width="0.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Полная охрана</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Хозяйство запрещено</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Научные исследования</text>
<text x="0" y="33" font-family="Arial,sans-serif" font-size="5" fill="#4CAF50" text-anchor="middle">Строгий режим</text>
</g>
<g transform="translate(250,140)">
<rect x="-60" y="-40" width="120" height="80" rx="5" fill="white" stroke="#FF9800" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#FF9800" text-anchor="middle" font-weight="bold">Заказники</text>
<line x1="-45" y1="-18" x2="45" y2="-18" stroke="#FF9800" stroke-width="0.5"/>
<text x="0" y="-5" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Частичная охрана</text>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Ограниченное</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">хозяйство</text>
<text x="0" y="33" font-family="Arial,sans-serif" font-size="5" fill="#FF9800" text-anchor="middle">Видовая охрана</text>
</g>
<g transform="translate(400,140)">
<rect x="-60" y="-40" width="120" height="80" rx="5" fill="white" stroke="#2196F3" stroke-width="1.5"/>
<text x="0" y="-25" font-family="Arial,sans-serif" font-size="7" fill="#2196F3" text-anchor="middle" font-weight="bold">Национальные</text>
<text x="0" y="-14" font-family="Arial,sans-serif" font-size="7" fill="#2196F3" text-anchor="middle" font-weight="bold">парки</text>
<line x1="-45" y1="-7" x2="45" y2="-7" stroke="#2196F3" stroke-width="0.5"/>
<text x="0" y="7" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Отдых + охрана</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Зонирование</text>
<text x="0" y="33" font-family="Arial,sans-serif" font-size="5" fill="#2196F3" text-anchor="middle">Туризм разрешён</text>
</g>
'''+ib(30,260,440,45,["Красная книга МСОП: категории EX, CR, EN, VU, NT, LC","Рамсерские водно-болотные угодья | Конвенция CITES","Устойчивое развитие: удовлетворение потребностей без ущерба будущим поколениям"])+ftr

for i in range(1,26):
    with open(f"{OUT}/lesson{i}.svg","w") as f:
        f.write(svgs[i])
print(f"Generated {len(svgs)} SVGs for grade 9 biology")
