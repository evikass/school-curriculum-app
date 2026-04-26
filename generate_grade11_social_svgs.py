#!/usr/bin/env python3
"""Generate SVG images for Grade 11 Social Studies (Обществознание) lessons."""

import os
import html
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade11/social"

LESSONS = [
    (1, "Человек как биосоциальное существо"),
    (2, "Познание"),
    (3, "Общество"),
    (4, "Экономика и её роль"),
    (5, "Государство и экономика"),
    (6, "Социальная структура"),
    (7, "Социальные институты"),
    (8, "Политика и власть"),
    (9, "Право"),
    (10, "Права человека"),
    (11, "Правонарушение и ответственность"),
    (12, "Избирательное право"),
]

# Color scheme
PRIMARY = "#00695C"
PRIMARY_LIGHT = "#4DB6AC"
PRIMARY_DARK = "#004D40"
BG = "#E0F2F1"
BG_LIGHT = "#F5FDFC"
ACCENT1 = "#00897B"
ACCENT2 = "#26A69A"
ACCENT3 = "#80CBC4"
TEXT_DARK = "#004D40"
TEXT_MED = "#00695C"


def title_font_size(title):
    if len(title) > 32:
        return 16
    elif len(title) > 26:
        return 18
    elif len(title) > 20:
        return 20
    return 22


def make_svg(lesson_num, title):
    tfs = title_font_size(title)
    escaped_title = html.escape(title)
    ill_content = get_illustration(lesson_num)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#E0F2F1"/>
      <stop offset="100%" stop-color="#F5FDFC"/>
    </linearGradient>
    <linearGradient id="panel" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#00695C"/>
      <stop offset="100%" stop-color="#00897B"/>
    </linearGradient>
  </defs>
  <rect width="500" height="350" fill="url(#bg)" rx="10"/>
  <rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="#00695C" stroke-width="2.5"/>
  <rect x="8" y="8" width="484" height="334" rx="6" fill="none" stroke="#00695C" stroke-width="1" opacity="0.3"/>
  <polygon points="10,10 30,10 10,30" fill="#00695C" opacity="0.12"/>
  <polygon points="490,10 470,10 490,30" fill="#00897B" opacity="0.12"/>
  <polygon points="10,340 30,340 10,320" fill="#26A69A" opacity="0.12"/>
  <polygon points="490,340 470,340 490,320" fill="#004D40" opacity="0.12"/>
  <text x="250" y="46" font-family="Arial,sans-serif" font-size="{tfs}" font-weight="bold" fill="#00695C" text-anchor="middle">{escaped_title}</text>
  <text x="250" y="66" font-family="Arial,sans-serif" font-size="12" fill="#777" text-anchor="middle">Обществознание — Урок {lesson_num}</text>
  <line x1="30" y1="76" x2="470" y2="76" stroke="#00695C" stroke-width="2" opacity="0.25"/>
  <rect x="30" y="73" width="60" height="5" fill="#00695C" opacity="0.18" rx="1"/>
  <rect x="410" y="73" width="60" height="5" fill="#00897B" opacity="0.12" rx="1"/>
  <clipPath id="ill"><rect x="15" y="83" width="470" height="217" rx="6"/></clipPath>
  <g clip-path="url(#ill)">
  <rect x="15" y="83" width="470" height="217" fill="#E0F2F1"/>
  {ill_content}
  </g>
  <rect x="12" y="305" width="476" height="32" rx="5" fill="url(#panel)"/>
  <line x1="20" y1="308" x2="20" y2="334" stroke="#26A69A" stroke-width="1.5" opacity="0.6"/>
  <line x1="480" y1="308" x2="480" y2="334" stroke="#26A69A" stroke-width="1.5" opacity="0.6"/>
  <text x="250" y="326" font-family="Arial,sans-serif" font-size="14" text-anchor="middle" fill="white" font-weight="bold">Обществознание · 11 класс</text>
</svg>'''


def get_illustration(n):
    if n == 1:
        # Человек как биосоциальное существо
        return '''
    <!-- Definition box -->
    <rect x="25" y="90" width="450" height="40" rx="5" fill="#00695C" opacity="0.1" stroke="#00695C" stroke-width="1"/>
    <text x="250" y="107" font-family="Arial,sans-serif" font-size="10" fill="#004D40" text-anchor="middle" font-weight="bold">Определение:</text>
    <text x="250" y="122" font-family="Arial,sans-serif" font-size="9" fill="#004D40" text-anchor="middle">Человек — биосоциальное существо, сочетающее биологическую природу и социальные качества</text>

    <!-- Two main aspects -->
    <rect x="25" y="138" width="215" height="145" rx="6" fill="white" stroke="#00897B" stroke-width="1.5"/>
    <rect x="25" y="138" width="215" height="24" rx="6" fill="#00897B"/>
    <text x="132" y="155" font-family="Arial,sans-serif" font-size="12" fill="white" text-anchor="middle" font-weight="bold">Биологическая природа</text>
    <circle cx="50" cy="180" r="4" fill="#26A69A"/>
    <text x="58" y="184" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Наследственность (генотип)</text>
    <circle cx="50" cy="198" r="4" fill="#26A69A"/>
    <text x="58" y="202" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Анатомо-физиологические особенности</text>
    <circle cx="50" cy="216" r="4" fill="#26A69A"/>
    <text x="58" y="220" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Инстинкты и рефлексы</text>
    <circle cx="50" cy="234" r="4" fill="#26A69A"/>
    <text x="58" y="238" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Потребности: пища, безопасность</text>
    <circle cx="50" cy="252" r="4" fill="#26A69A"/>
    <text x="58" y="256" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Возрастные стадии развития</text>
    <circle cx="50" cy="270" r="4" fill="#26A69A"/>
    <text x="58" y="274" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Расовые и половые различия</text>

    <rect x="260" y="138" width="215" height="145" rx="6" fill="white" stroke="#00695C" stroke-width="1.5"/>
    <rect x="260" y="138" width="215" height="24" rx="6" fill="#00695C"/>
    <text x="367" y="155" font-family="Arial,sans-serif" font-size="12" fill="white" text-anchor="middle" font-weight="bold">Социальная природа</text>
    <circle cx="285" cy="180" r="4" fill="#00695C"/>
    <text x="293" y="184" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Сознание и мышление</text>
    <circle cx="285" cy="198" r="4" fill="#00695C"/>
    <text x="293" y="202" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Речь и коммуникация</text>
    <circle cx="285" cy="216" r="4" fill="#00695C"/>
    <text x="293" y="220" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Трудовая деятельность</text>
    <circle cx="285" cy="234" r="4" fill="#00695C"/>
    <text x="293" y="238" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Культура и ценности</text>
    <circle cx="285" cy="252" r="4" fill="#00695C"/>
    <text x="293" y="256" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Социализация личности</text>
    <circle cx="285" cy="270" r="4" fill="#00695C"/>
    <text x="293" y="274" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Социальные роли и статусы</text>

    <!-- Connecting arrow -->
    <line x1="240" y1="210" x2="260" y2="210" stroke="#26A69A" stroke-width="2"/>
    <polygon points="260,210 254,205 254,215" fill="#26A69A"/>
    <line x1="260" y1="220" x2="240" y2="220" stroke="#26A69A" stroke-width="2"/>
    <polygon points="240,220 246,215 246,225" fill="#26A69A"/>'''

    elif n == 2:
        # Познание
        return '''
    <!-- Definition -->
    <rect x="25" y="90" width="450" height="35" rx="5" fill="#00695C" opacity="0.1" stroke="#00695C" stroke-width="1"/>
    <text x="250" y="107" font-family="Arial,sans-serif" font-size="10" fill="#004D40" text-anchor="middle" font-weight="bold">Познание — процесс приобретения и развития знаний об окружающем мире</text>

    <!-- Two types of cognition -->
    <rect x="25" y="132" width="145" height="150" rx="6" fill="white" stroke="#00897B" stroke-width="1.5"/>
    <rect x="25" y="132" width="145" height="22" rx="6" fill="#00897B"/>
    <text x="97" y="148" font-family="Arial,sans-serif" font-size="11" fill="white" text-anchor="middle" font-weight="bold">Чувственное</text>
    <text x="35" y="172" font-family="Arial,sans-serif" font-size="9" fill="#004D40" font-weight="bold">Ощущение</text>
    <text x="35" y="183" font-family="Arial,sans-serif" font-size="8" fill="#666">отражение отдельных свойств</text>
    <text x="35" y="198" font-family="Arial,sans-serif" font-size="9" fill="#004D40" font-weight="bold">Восприятие</text>
    <text x="35" y="209" font-family="Arial,sans-serif" font-size="8" fill="#666">целостный образ предмета</text>
    <text x="35" y="224" font-family="Arial,sans-serif" font-size="9" fill="#004D40" font-weight="bold">Представление</text>
    <text x="35" y="235" font-family="Arial,sans-serif" font-size="8" fill="#666">образ без воздействия</text>
    <text x="35" y="255" font-family="Arial,sans-serif" font-size="9" fill="#00897B" font-style="italic">Пример: запах цветка</text>
    <text x="35" y="268" font-family="Arial,sans-serif" font-size="9" fill="#00897B" font-style="italic">Пример: образ дома</text>

    <rect x="180" y="132" width="145" height="150" rx="6" fill="white" stroke="#00695C" stroke-width="1.5"/>
    <rect x="180" y="132" width="145" height="22" rx="6" fill="#00695C"/>
    <text x="252" y="148" font-family="Arial,sans-serif" font-size="11" fill="white" text-anchor="middle" font-weight="bold">Рациональное</text>
    <text x="190" y="172" font-family="Arial,sans-serif" font-size="9" fill="#004D40" font-weight="bold">Понятие</text>
    <text x="190" y="183" font-family="Arial,sans-serif" font-size="8" fill="#666">существенные признаки</text>
    <text x="190" y="198" font-family="Arial,sans-serif" font-size="9" fill="#004D40" font-weight="bold">Суждение</text>
    <text x="190" y="209" font-family="Arial,sans-serif" font-size="8" fill="#666">утверждение/отрицание</text>
    <text x="190" y="224" font-family="Arial,sans-serif" font-size="9" fill="#004D40" font-weight="bold">Умозаключение</text>
    <text x="190" y="235" font-family="Arial,sans-serif" font-size="8" fill="#666">вывод из суждений</text>
    <text x="190" y="255" font-family="Arial,sans-serif" font-size="9" fill="#00695C" font-style="italic">Пример: понятие «дерево»</text>
    <text x="190" y="268" font-family="Arial,sans-serif" font-size="9" fill="#00695C" font-style="italic">Пример: силлогизм</text>

    <rect x="335" y="132" width="140" height="150" rx="6" fill="white" stroke="#26A69A" stroke-width="1.5"/>
    <rect x="335" y="132" width="140" height="22" rx="6" fill="#26A69A"/>
    <text x="405" y="148" font-family="Arial,sans-serif" font-size="11" fill="white" text-anchor="middle" font-weight="bold">Виды истины</text>
    <circle cx="350" cy="172" r="4" fill="#00897B"/>
    <text x="358" y="176" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Абсолютная истина</text>
    <circle cx="350" cy="192" r="4" fill="#00897B"/>
    <text x="358" y="196" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Относительная истина</text>
    <circle cx="350" cy="212" r="4" fill="#00897B"/>
    <text x="358" y="216" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Объективная истина</text>
    <line x1="345" y1="230" x2="465" y2="230" stroke="#26A69A" stroke-width="1" opacity="0.4"/>
    <text x="405" y="248" font-family="Arial,sans-serif" font-size="9" fill="#004D40" font-weight="bold">Критерии истины:</text>
    <text x="405" y="262" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Практика, логика, опыт</text>'''

    elif n == 3:
        # Общество
        return '''
    <!-- Definition -->
    <rect x="25" y="90" width="450" height="35" rx="5" fill="#00695C" opacity="0.1" stroke="#00695C" stroke-width="1"/>
    <text x="250" y="107" font-family="Arial,sans-serif" font-size="10" fill="#004D40" text-anchor="middle" font-weight="bold">Общество — обособившаяся от природы часть материального мира, включающая способы взаимодействия людей</text>

    <!-- Spheres of society - 4 boxes -->
    <rect x="25" y="132" width="225" height="75" rx="6" fill="white" stroke="#00897B" stroke-width="1.5"/>
    <rect x="25" y="132" width="225" height="20" rx="6" fill="#00897B"/>
    <text x="137" y="147" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">Экономическая сфера</text>
    <text x="35" y="165" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Производство, распределение, обмен, потребление</text>
    <text x="35" y="178" font-family="Arial,sans-serif" font-size="8" fill="#666">Пример: рынок товаров, банки, предприятия</text>
    <text x="35" y="198" font-family="Arial,sans-serif" font-size="8" fill="#00897B">Субъекты: производители, потребители</text>

    <rect x="260" y="132" width="215" height="75" rx="6" fill="white" stroke="#00695C" stroke-width="1.5"/>
    <rect x="260" y="132" width="215" height="20" rx="6" fill="#00695C"/>
    <text x="367" y="147" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">Политическая сфера</text>
    <text x="270" y="165" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Власть, государство, партии, право</text>
    <text x="270" y="178" font-family="Arial,sans-serif" font-size="8" fill="#666">Пример: выборы, законы, суды</text>
    <text x="270" y="198" font-family="Arial,sans-serif" font-size="8" fill="#00695C">Субъекты: государство, партии, граждане</text>

    <rect x="25" y="215" width="225" height="75" rx="6" fill="white" stroke="#26A69A" stroke-width="1.5"/>
    <rect x="25" y="215" width="225" height="20" rx="6" fill="#26A69A"/>
    <text x="137" y="230" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">Социальная сфера</text>
    <text x="35" y="248" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Классы, страты, группы, семья</text>
    <text x="35" y="261" font-family="Arial,sans-serif" font-size="8" fill="#666">Пример: социальная мобильность</text>
    <text x="35" y="281" font-family="Arial,sans-serif" font-size="8" fill="#26A69A">Субъекты: социальные группы, индивиды</text>

    <rect x="260" y="215" width="215" height="75" rx="6" fill="white" stroke="#004D40" stroke-width="1.5"/>
    <rect x="260" y="215" width="215" height="20" rx="6" fill="#004D40"/>
    <text x="367" y="230" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">Духовная сфера</text>
    <text x="270" y="248" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Наука, образование, искусство, религия</text>
    <text x="270" y="261" font-family="Arial,sans-serif" font-size="8" fill="#666">Пример: университеты, музеи, театры</text>
    <text x="270" y="281" font-family="Arial,sans-serif" font-size="8" fill="#004D40">Субъекты: учёные, деятели культуры</text>'''

    elif n == 4:
        # Экономика и её роль
        return '''
    <!-- Definition -->
    <rect x="25" y="90" width="450" height="35" rx="5" fill="#00695C" opacity="0.1" stroke="#00695C" stroke-width="1"/>
    <text x="250" y="107" font-family="Arial,sans-serif" font-size="10" fill="#004D40" text-anchor="middle" font-weight="bold">Экономика — система хозяйствования, обеспечивающая общество материальными благами</text>

    <!-- Main question -->
    <rect x="150" y="132" width="200" height="28" rx="14" fill="#00695C" opacity="0.15" stroke="#00695C" stroke-width="1.5"/>
    <text x="250" y="150" font-family="Arial,sans-serif" font-size="10" fill="#00695C" text-anchor="middle" font-weight="bold">Что? Как? Для кого?</text>

    <!-- Three economic questions -->
    <rect x="25" y="168" width="145" height="75" rx="5" fill="white" stroke="#00897B" stroke-width="1.5"/>
    <text x="97" y="185" font-family="Arial,sans-serif" font-size="10" fill="#00897B" text-anchor="middle" font-weight="bold">Что производить?</text>
    <text x="35" y="200" font-family="Arial,sans-serif" font-size="8" fill="#666">Какие товары и услуги</text>
    <text x="35" y="212" font-family="Arial,sans-serif" font-size="8" fill="#666">нужны обществу?</text>
    <text x="35" y="234" font-family="Arial,sans-serif" font-size="8" fill="#00897B" font-style="italic">Пример: автомобили</text>

    <rect x="180" y="168" width="145" height="75" rx="5" fill="white" stroke="#00695C" stroke-width="1.5"/>
    <text x="252" y="185" font-family="Arial,sans-serif" font-size="10" fill="#00695C" text-anchor="middle" font-weight="bold">Как производить?</text>
    <text x="190" y="200" font-family="Arial,sans-serif" font-size="8" fill="#666">Какими способами и</text>
    <text x="190" y="212" font-family="Arial,sans-serif" font-size="8" fill="#666">ресурсами?</text>
    <text x="190" y="234" font-family="Arial,sans-serif" font-size="8" fill="#00695C" font-style="italic">Пример: конвейер</text>

    <rect x="335" y="168" width="140" height="75" rx="5" fill="white" stroke="#26A69A" stroke-width="1.5"/>
    <text x="405" y="185" font-family="Arial,sans-serif" font-size="10" fill="#26A69A" text-anchor="middle" font-weight="bold">Для кого?</text>
    <text x="345" y="200" font-family="Arial,sans-serif" font-size="8" fill="#666">Кто будет потребителем?</text>
    <text x="345" y="212" font-family="Arial,sans-serif" font-size="8" fill="#666">Как распределять?</text>
    <text x="345" y="234" font-family="Arial,sans-serif" font-size="8" fill="#26A69A" font-style="italic">Пример: по доходу</text>

    <!-- Factors of production -->
    <text x="250" y="260" font-family="Arial,sans-serif" font-size="10" fill="#004D40" text-anchor="middle" font-weight="bold">Факторы производства</text>
    <rect x="25" y="270" width="110" height="22" rx="4" fill="#00897B" opacity="0.2" stroke="#00897B" stroke-width="1"/>
    <text x="80" y="285" font-family="Arial,sans-serif" font-size="9" fill="#004D40" text-anchor="middle">Земля</text>
    <rect x="145" y="270" width="110" height="22" rx="4" fill="#00695C" opacity="0.2" stroke="#00695C" stroke-width="1"/>
    <text x="200" y="285" font-family="Arial,sans-serif" font-size="9" fill="#004D40" text-anchor="middle">Труд</text>
    <rect x="265" y="270" width="110" height="22" rx="4" fill="#26A69A" opacity="0.2" stroke="#26A69A" stroke-width="1"/>
    <text x="320" y="285" font-family="Arial,sans-serif" font-size="9" fill="#004D40" text-anchor="middle">Капитал</text>
    <rect x="385" y="270" width="80" height="22" rx="4" fill="#004D40" opacity="0.2" stroke="#004D40" stroke-width="1"/>
    <text x="425" y="285" font-family="Arial,sans-serif" font-size="9" fill="#004D40" text-anchor="middle">Предпр.</text>'''

    elif n == 5:
        # Государство и экономика
        return '''
    <!-- Definition -->
    <rect x="25" y="90" width="450" height="35" rx="5" fill="#00695C" opacity="0.1" stroke="#00695C" stroke-width="1"/>
    <text x="250" y="107" font-family="Arial,sans-serif" font-size="10" fill="#004D40" text-anchor="middle" font-weight="bold">Государство регулирует экономику для обеспечения стабильности и социальной справедливости</text>

    <!-- Methods of regulation -->
    <rect x="25" y="132" width="225" height="80" rx="6" fill="white" stroke="#00897B" stroke-width="1.5"/>
    <rect x="25" y="132" width="225" height="20" rx="6" fill="#00897B"/>
    <text x="137" y="147" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">Прямые методы</text>
    <circle cx="40" cy="168" r="3" fill="#00897B"/>
    <text x="48" y="172" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Законодательство</text>
    <circle cx="40" cy="184" r="3" fill="#00897B"/>
    <text x="48" y="188" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Лицензирование</text>
    <circle cx="40" cy="200" r="3" fill="#00897B"/>
    <text x="48" y="204" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Госзаказ и субсидии</text>

    <rect x="260" y="132" width="215" height="80" rx="6" fill="white" stroke="#00695C" stroke-width="1.5"/>
    <rect x="260" y="132" width="215" height="20" rx="6" fill="#00695C"/>
    <text x="367" y="147" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">Косвенные методы</text>
    <circle cx="275" cy="168" r="3" fill="#00695C"/>
    <text x="283" y="172" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Налоговая политика</text>
    <circle cx="275" cy="184" r="3" fill="#00695C"/>
    <text x="283" y="188" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Кредитно-денежная политика</text>
    <circle cx="275" cy="200" r="3" fill="#00695C"/>
    <text x="283" y="204" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Таможенные пошлины</text>

    <!-- Economic functions of state -->
    <text x="250" y="232" font-family="Arial,sans-serif" font-size="10" fill="#004D40" text-anchor="middle" font-weight="bold">Функции государства в экономике</text>
    <rect x="25" y="240" width="145" height="50" rx="5" fill="white" stroke="#26A69A" stroke-width="1"/>
    <text x="97" y="258" font-family="Arial,sans-serif" font-size="9" fill="#004D40" text-anchor="middle" font-weight="bold">Стабилизация</text>
    <text x="97" y="272" font-family="Arial,sans-serif" font-size="8" fill="#666" text-anchor="middle">Борьба с кризисами</text>
    <rect x="180" y="240" width="145" height="50" rx="5" fill="white" stroke="#26A69A" stroke-width="1"/>
    <text x="252" y="258" font-family="Arial,sans-serif" font-size="9" fill="#004D40" text-anchor="middle" font-weight="bold">Распределение</text>
    <text x="252" y="272" font-family="Arial,sans-serif" font-size="8" fill="#666" text-anchor="middle">Перераспределение доходов</text>
    <rect x="335" y="240" width="140" height="50" rx="5" fill="white" stroke="#26A69A" stroke-width="1"/>
    <text x="405" y="258" font-family="Arial,sans-serif" font-size="9" fill="#004D40" text-anchor="middle" font-weight="bold">Общественные блага</text>
    <text x="405" y="272" font-family="Arial,sans-serif" font-size="8" fill="#666" text-anchor="middle">Образование, дороги</text>'''

    elif n == 6:
        # Социальная структура
        return '''
    <!-- Definition -->
    <rect x="25" y="90" width="450" height="35" rx="5" fill="#00695C" opacity="0.1" stroke="#00695C" stroke-width="1"/>
    <text x="250" y="107" font-family="Arial,sans-serif" font-size="10" fill="#004D40" text-anchor="middle" font-weight="bold">Социальная структура — совокупность взаимосвязанных социальных групп и слоёв общества</text>

    <!-- Pyramid of social stratification -->
    <polygon points="250,130 370,275 130,275" fill="none" stroke="#00695C" stroke-width="2"/>
    <line x1="185" y1="200" x2="315" y2="200" stroke="#00695C" stroke-width="1" stroke-dasharray="4,3"/>
    <line x1="160" y1="240" x2="340" y2="240" stroke="#00695C" stroke-width="1" stroke-dasharray="4,3"/>

    <text x="250" y="168" font-family="Arial,sans-serif" font-size="9" fill="#00695C" text-anchor="middle" font-weight="bold">Элита</text>
    <rect x="200" y="175" width="100" height="20" rx="3" fill="#00695C" opacity="0.15"/>
    <text x="250" y="190" font-family="Arial,sans-serif" font-size="8" fill="#00695C" text-anchor="middle">Высший класс</text>

    <text x="250" y="222" font-family="Arial,sans-serif" font-size="9" fill="#00897B" text-anchor="middle" font-weight="bold">Средний класс</text>
    <rect x="170" y="228" width="160" height="20" rx="3" fill="#00897B" opacity="0.15"/>
    <text x="250" y="242" font-family="Arial,sans-serif" font-size="8" fill="#00897B" text-anchor="middle">Предприниматели, специалисты</text>

    <text x="250" y="260" font-family="Arial,sans-serif" font-size="9" fill="#26A69A" text-anchor="middle" font-weight="bold">Низший класс</text>
    <rect x="145" y="265" width="210" height="14" rx="3" fill="#26A69A" opacity="0.15"/>
    <text x="250" y="276" font-family="Arial,sans-serif" font-size="8" fill="#26A69A" text-anchor="middle">Рабочие, малоимущие</text>

    <!-- Social mobility -->
    <rect x="380" y="130" width="95" height="130" rx="5" fill="white" stroke="#00695C" stroke-width="1"/>
    <text x="427" y="148" font-family="Arial,sans-serif" font-size="9" fill="#00695C" text-anchor="middle" font-weight="bold">Мобильность</text>
    <line x1="390" y1="155" x2="465" y2="155" stroke="#00695C" stroke-width="0.5" opacity="0.3"/>
    <text x="427" y="170" font-family="Arial,sans-serif" font-size="8" fill="#004D40" text-anchor="middle">Восходящая</text>
    <text x="427" y="180" font-family="Arial,sans-serif" font-size="8" fill="#004D40" text-anchor="middle">&#x2191; карьерный рост</text>
    <line x1="390" y1="190" x2="465" y2="190" stroke="#00695C" stroke-width="0.5" opacity="0.3"/>
    <text x="427" y="205" font-family="Arial,sans-serif" font-size="8" fill="#004D40" text-anchor="middle">Нисходящая</text>
    <text x="427" y="215" font-family="Arial,sans-serif" font-size="8" fill="#004D40" text-anchor="middle">&#x2193; потеря статуса</text>
    <line x1="390" y1="225" x2="465" y2="225" stroke="#00695C" stroke-width="0.5" opacity="0.3"/>
    <text x="427" y="240" font-family="Arial,sans-serif" font-size="8" fill="#004D40" text-anchor="middle">Горизонт.</text>
    <text x="427" y="250" font-family="Arial,sans-serif" font-size="8" fill="#004D40" text-anchor="middle">&#x2194; смена профессии</text>'''

    elif n == 7:
        # Социальные институты
        return '''
    <!-- Definition -->
    <rect x="25" y="90" width="450" height="35" rx="5" fill="#00695C" opacity="0.1" stroke="#00695C" stroke-width="1"/>
    <text x="250" y="107" font-family="Arial,sans-serif" font-size="10" fill="#004D40" text-anchor="middle" font-weight="bold">Социальный институт — устойчивая форма организации совместной деятельности людей</text>

    <!-- 5 main institutions -->
    <rect x="25" y="132" width="90" height="75" rx="5" fill="white" stroke="#00695C" stroke-width="1.5"/>
    <rect x="25" y="132" width="90" height="18" rx="5" fill="#00695C"/>
    <text x="70" y="145" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">Семья</text>
    <text x="70" y="163" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Воспроизводство</text>
    <text x="70" y="173" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">рода, воспитание</text>
    <text x="70" y="195" font-family="Arial,sans-serif" font-size="7" fill="#00695C" text-anchor="middle">Брак, родство</text>

    <rect x="125" y="132" width="90" height="75" rx="5" fill="white" stroke="#00897B" stroke-width="1.5"/>
    <rect x="125" y="132" width="90" height="18" rx="5" fill="#00897B"/>
    <text x="170" y="145" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">Государство</text>
    <text x="170" y="163" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Управление,</text>
    <text x="170" y="173" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">безопасность</text>
    <text x="170" y="195" font-family="Arial,sans-serif" font-size="7" fill="#00897B" text-anchor="middle">Власть, закон</text>

    <rect x="225" y="132" width="90" height="75" rx="5" fill="white" stroke="#26A69A" stroke-width="1.5"/>
    <rect x="225" y="132" width="90" height="18" rx="5" fill="#26A69A"/>
    <text x="270" y="145" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">Производство</text>
    <text x="270" y="163" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Создание благ,</text>
    <text x="270" y="173" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">распределение</text>
    <text x="270" y="195" font-family="Arial,sans-serif" font-size="7" fill="#26A69A" text-anchor="middle">Рынок, труд</text>

    <rect x="325" y="132" width="80" height="75" rx="5" fill="white" stroke="#004D40" stroke-width="1.5"/>
    <rect x="325" y="132" width="80" height="18" rx="5" fill="#004D40"/>
    <text x="365" y="145" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">Образование</text>
    <text x="365" y="163" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Передача знаний,</text>
    <text x="365" y="173" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">социализация</text>
    <text x="365" y="195" font-family="Arial,sans-serif" font-size="7" fill="#004D40" text-anchor="middle">Школа, ВУЗ</text>

    <rect x="415" y="132" width="60" height="75" rx="5" fill="white" stroke="#80CBC4" stroke-width="1.5"/>
    <rect x="415" y="132" width="60" height="18" rx="5" fill="#80CBC4"/>
    <text x="445" y="145" font-family="Arial,sans-serif" font-size="8" fill="white" text-anchor="middle" font-weight="bold">Религия</text>
    <text x="445" y="163" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Духовные</text>
    <text x="445" y="173" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">потребности</text>
    <text x="445" y="195" font-family="Arial,sans-serif" font-size="7" fill="#80CBC4" text-anchor="middle">Церковь</text>

    <!-- Elements of social institution -->
    <rect x="25" y="218" width="450" height="80" rx="6" fill="white" stroke="#00695C" stroke-width="1"/>
    <text x="250" y="234" font-family="Arial,sans-serif" font-size="10" fill="#00695C" text-anchor="middle" font-weight="bold">Элементы социального института</text>
    <line x1="35" y1="240" x2="465" y2="240" stroke="#00695C" stroke-width="0.5" opacity="0.3"/>
    <circle cx="45" cy="256" r="3" fill="#00897B"/>
    <text x="53" y="260" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Цель (функция института)</text>
    <circle cx="45" cy="272" r="3" fill="#00897B"/>
    <text x="53" y="276" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Нормы и правила поведения</text>
    <circle cx="250" cy="256" r="3" fill="#00695C"/>
    <text x="258" y="260" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Учреждения (организации)</text>
    <circle cx="250" cy="272" r="3" fill="#00695C"/>
    <text x="258" y="276" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Символы и культурные образцы</text>'''

    elif n == 8:
        # Политика и власть
        return '''
    <!-- Definition -->
    <rect x="25" y="90" width="450" height="35" rx="5" fill="#00695C" opacity="0.1" stroke="#00695C" stroke-width="1"/>
    <text x="250" y="107" font-family="Arial,sans-serif" font-size="10" fill="#004D40" text-anchor="middle" font-weight="bold">Власть — способность и возможность оказывать влияние на поведение людей</text>

    <!-- Forms of government -->
    <rect x="25" y="132" width="145" height="90" rx="6" fill="white" stroke="#00695C" stroke-width="1.5"/>
    <rect x="25" y="132" width="145" height="20" rx="6" fill="#00695C"/>
    <text x="97" y="147" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">Монархия</text>
    <text x="35" y="166" font-family="Arial,sans-serif" font-size="8" fill="#004D40">Власть передаётся по наследству</text>
    <line x1="35" y1="172" x2="160" y2="172" stroke="#00695C" stroke-width="0.5" opacity="0.3"/>
    <text x="35" y="184" font-family="Arial,sans-serif" font-size="8" fill="#00897B">Абсолютная (Саудовская Аравия)</text>
    <text x="35" y="198" font-family="Arial,sans-serif" font-size="8" fill="#00897B">Ограниченная (Великобритания)</text>

    <rect x="180" y="132" width="145" height="90" rx="6" fill="white" stroke="#00897B" stroke-width="1.5"/>
    <rect x="180" y="132" width="145" height="20" rx="6" fill="#00897B"/>
    <text x="252" y="147" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">Республика</text>
    <text x="190" y="166" font-family="Arial,sans-serif" font-size="8" fill="#004D40">Власть избирается народом</text>
    <line x1="190" y1="172" x2="315" y2="172" stroke="#00897B" stroke-width="0.5" opacity="0.3"/>
    <text x="190" y="184" font-family="Arial,sans-serif" font-size="8" fill="#00695C">Президентская (США)</text>
    <text x="190" y="198" font-family="Arial,sans-serif" font-size="8" fill="#00695C">Парламентская (Германия)</text>

    <rect x="335" y="132" width="140" height="90" rx="6" fill="white" stroke="#26A69A" stroke-width="1.5"/>
    <rect x="335" y="132" width="140" height="20" rx="6" fill="#26A69A"/>
    <text x="405" y="147" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">Форма устройства</text>
    <circle cx="350" cy="168" r="3" fill="#26A69A"/>
    <text x="358" y="172" font-family="Arial,sans-serif" font-size="8" fill="#004D40">Унитарное государство</text>
    <circle cx="350" cy="184" r="3" fill="#26A69A"/>
    <text x="358" y="188" font-family="Arial,sans-serif" font-size="8" fill="#004D40">Федерация (Россия)</text>
    <circle cx="350" cy="200" r="3" fill="#26A69A"/>
    <text x="358" y="204" font-family="Arial,sans-serif" font-size="8" fill="#004D40">Конфедерация</text>

    <!-- Sources of power -->
    <rect x="25" y="230" width="450" height="68" rx="6" fill="white" stroke="#00695C" stroke-width="1"/>
    <text x="250" y="248" font-family="Arial,sans-serif" font-size="10" fill="#00695C" text-anchor="middle" font-weight="bold">Источники власти</text>
    <rect x="35" y="256" width="80" height="30" rx="4" fill="#00695C" opacity="0.15" stroke="#00695C" stroke-width="1"/>
    <text x="75" y="275" font-family="Arial,sans-serif" font-size="8" fill="#004D40" text-anchor="middle">Авторитет</text>
    <rect x="125" y="256" width="80" height="30" rx="4" fill="#00897B" opacity="0.15" stroke="#00897B" stroke-width="1"/>
    <text x="165" y="275" font-family="Arial,sans-serif" font-size="8" fill="#004D40" text-anchor="middle">Сила</text>
    <rect x="215" y="256" width="80" height="30" rx="4" fill="#26A69A" opacity="0.15" stroke="#26A69A" stroke-width="1"/>
    <text x="255" y="275" font-family="Arial,sans-serif" font-size="8" fill="#004D40" text-anchor="middle">Закон</text>
    <rect x="305" y="256" width="80" height="30" rx="4" fill="#004D40" opacity="0.15" stroke="#004D40" stroke-width="1"/>
    <text x="345" y="275" font-family="Arial,sans-serif" font-size="8" fill="#004D40" text-anchor="middle">Богатство</text>
    <rect x="395" y="256" width="70" height="30" rx="4" fill="#80CBC4" opacity="0.2" stroke="#80CBC4" stroke-width="1"/>
    <text x="430" y="275" font-family="Arial,sans-serif" font-size="8" fill="#004D40" text-anchor="middle">Знание</text>'''

    elif n == 9:
        # Право
        return '''
    <!-- Definition -->
    <rect x="25" y="90" width="450" height="35" rx="5" fill="#00695C" opacity="0.1" stroke="#00695C" stroke-width="1"/>
    <text x="250" y="107" font-family="Arial,sans-serif" font-size="10" fill="#004D40" text-anchor="middle" font-weight="bold">Право — система общеобязательных норм, охраняемых государством</text>

    <!-- Signs of law -->
    <rect x="25" y="132" width="225" height="90" rx="6" fill="white" stroke="#00695C" stroke-width="1.5"/>
    <rect x="25" y="132" width="225" height="20" rx="6" fill="#00695C"/>
    <text x="137" y="147" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">Признаки права</text>
    <circle cx="40" cy="168" r="3" fill="#00695C"/>
    <text x="48" y="172" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Нормативность</text>
    <circle cx="40" cy="184" r="3" fill="#00695C"/>
    <text x="48" y="188" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Общеобязательность</text>
    <circle cx="40" cy="200" r="3" fill="#00695C"/>
    <text x="48" y="204" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Обеспеченность государством</text>

    <rect x="260" y="132" width="215" height="90" rx="6" fill="white" stroke="#00897B" stroke-width="1.5"/>
    <rect x="260" y="132" width="215" height="20" rx="6" fill="#00897B"/>
    <text x="367" y="147" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">Функции права</text>
    <circle cx="275" cy="168" r="3" fill="#00897B"/>
    <text x="283" y="172" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Регулятивная</text>
    <circle cx="275" cy="184" r="3" fill="#00897B"/>
    <text x="283" y="188" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Охранительная</text>
    <circle cx="275" cy="200" r="3" fill="#00897B"/>
    <text x="283" y="204" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Воспитательная</text>

    <!-- Branches of law -->
    <text x="250" y="240" font-family="Arial,sans-serif" font-size="10" fill="#004D40" text-anchor="middle" font-weight="bold">Отрасли права</text>
    <rect x="25" y="248" width="90" height="50" rx="4" fill="white" stroke="#00695C" stroke-width="1"/>
    <text x="70" y="268" font-family="Arial,sans-serif" font-size="8" fill="#00695C" text-anchor="middle" font-weight="bold">Гражданское</text>
    <text x="70" y="280" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">имущество, сделки</text>
    <rect x="125" y="248" width="90" height="50" rx="4" fill="white" stroke="#00897B" stroke-width="1"/>
    <text x="170" y="268" font-family="Arial,sans-serif" font-size="8" fill="#00897B" text-anchor="middle" font-weight="bold">Уголовное</text>
    <text x="170" y="280" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">преступления</text>
    <rect x="225" y="248" width="90" height="50" rx="4" fill="white" stroke="#26A69A" stroke-width="1"/>
    <text x="270" y="268" font-family="Arial,sans-serif" font-size="8" fill="#26A69A" text-anchor="middle" font-weight="bold">Администра-</text>
    <text x="270" y="280" font-family="Arial,sans-serif" font-size="8" fill="#26A69A" text-anchor="middle" font-weight="bold">тивное</text>
    <rect x="325" y="248" width="80" height="50" rx="4" fill="white" stroke="#004D40" stroke-width="1"/>
    <text x="365" y="268" font-family="Arial,sans-serif" font-size="8" fill="#004D40" text-anchor="middle" font-weight="bold">Семейное</text>
    <text x="365" y="280" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">брак, дети</text>
    <rect x="415" y="248" width="60" height="50" rx="4" fill="white" stroke="#80CBC4" stroke-width="1"/>
    <text x="445" y="268" font-family="Arial,sans-serif" font-size="8" fill="#80CBC4" text-anchor="middle" font-weight="bold">Трудо-</text>
    <text x="445" y="280" font-family="Arial,sans-serif" font-size="8" fill="#80CBC4" text-anchor="middle" font-weight="bold">вое</text>'''

    elif n == 10:
        # Права человека
        return '''
    <!-- Definition -->
    <rect x="25" y="90" width="450" height="35" rx="5" fill="#00695C" opacity="0.1" stroke="#00695C" stroke-width="1"/>
    <text x="250" y="107" font-family="Arial,sans-serif" font-size="10" fill="#004D40" text-anchor="middle" font-weight="bold">Права человека — неотъемлемые права, принадлежащие каждому от рождения</text>

    <!-- Generations of rights -->
    <rect x="25" y="132" width="145" height="80" rx="6" fill="white" stroke="#00695C" stroke-width="1.5"/>
    <rect x="25" y="132" width="145" height="22" rx="6" fill="#00695C"/>
    <text x="97" y="148" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">I поколение</text>
    <text x="35" y="167" font-family="Arial,sans-serif" font-size="8" fill="#004D40">Личные и политические</text>
    <circle cx="40" cy="180" r="2.5" fill="#00695C"/>
    <text x="48" y="184" font-family="Arial,sans-serif" font-size="7" fill="#666">Право на жизнь</text>
    <circle cx="40" cy="193" r="2.5" fill="#00695C"/>
    <text x="48" y="197" font-family="Arial,sans-serif" font-size="7" fill="#666">Свобода слова</text>
    <circle cx="40" cy="206" r="2.5" fill="#00695C"/>
    <text x="48" y="210" font-family="Arial,sans-serif" font-size="7" fill="#666">Равенство перед законом</text>

    <rect x="180" y="132" width="145" height="80" rx="6" fill="white" stroke="#00897B" stroke-width="1.5"/>
    <rect x="180" y="132" width="145" height="22" rx="6" fill="#00897B"/>
    <text x="252" y="148" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">II поколение</text>
    <text x="190" y="167" font-family="Arial,sans-serif" font-size="8" fill="#004D40">Социально-экономические</text>
    <circle cx="195" cy="180" r="2.5" fill="#00897B"/>
    <text x="203" y="184" font-family="Arial,sans-serif" font-size="7" fill="#666">Право на труд</text>
    <circle cx="195" cy="193" r="2.5" fill="#00897B"/>
    <text x="203" y="197" font-family="Arial,sans-serif" font-size="7" fill="#666">Право на образование</text>
    <circle cx="195" cy="206" r="2.5" fill="#00897B"/>
    <text x="203" y="210" font-family="Arial,sans-serif" font-size="7" fill="#666">Право на отдых</text>

    <rect x="335" y="132" width="140" height="80" rx="6" fill="white" stroke="#26A69A" stroke-width="1.5"/>
    <rect x="335" y="132" width="140" height="22" rx="6" fill="#26A69A"/>
    <text x="405" y="148" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">III поколение</text>
    <text x="345" y="167" font-family="Arial,sans-serif" font-size="8" fill="#004D40">Коллективные права</text>
    <circle cx="350" cy="180" r="2.5" fill="#26A69A"/>
    <text x="358" y="184" font-family="Arial,sans-serif" font-size="7" fill="#666">Право на мир</text>
    <circle cx="350" cy="193" r="2.5" fill="#26A69A"/>
    <text x="358" y="197" font-family="Arial,sans-serif" font-size="7" fill="#666">Право на экологию</text>
    <circle cx="350" cy="206" r="2.5" fill="#26A69A"/>
    <text x="358" y="210" font-family="Arial,sans-serif" font-size="7" fill="#666">Право на развитие</text>

    <!-- Key documents -->
    <rect x="25" y="222" width="450" height="76" rx="6" fill="white" stroke="#00695C" stroke-width="1"/>
    <text x="250" y="240" font-family="Arial,sans-serif" font-size="10" fill="#00695C" text-anchor="middle" font-weight="bold">Основные документы</text>
    <line x1="35" y1="246" x2="465" y2="246" stroke="#00695C" stroke-width="0.5" opacity="0.3"/>
    <rect x="35" y="252" width="130" height="38" rx="4" fill="#00695C" opacity="0.08"/>
    <text x="100" y="268" font-family="Arial,sans-serif" font-size="8" fill="#00695C" text-anchor="middle" font-weight="bold">Всеобщая декларация</text>
    <text x="100" y="280" font-family="Arial,sans-serif" font-size="8" fill="#00695C" text-anchor="middle">прав человека (1948)</text>
    <rect x="175" y="252" width="150" height="38" rx="4" fill="#00897B" opacity="0.08"/>
    <text x="250" y="268" font-family="Arial,sans-serif" font-size="8" fill="#00897B" text-anchor="middle" font-weight="bold">Конвенция о правах</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="8" fill="#00897B" text-anchor="middle">ребёнка (1989)</text>
    <rect x="335" y="252" width="130" height="38" rx="4" fill="#26A69A" opacity="0.08"/>
    <text x="400" y="268" font-family="Arial,sans-serif" font-size="8" fill="#26A69A" text-anchor="middle" font-weight="bold">Конституция РФ</text>
    <text x="400" y="280" font-family="Arial,sans-serif" font-size="8" fill="#26A69A" text-anchor="middle">гл. 2 (1993)</text>'''

    elif n == 11:
        # Правонарушение и ответственность
        return '''
    <!-- Definition -->
    <rect x="25" y="90" width="450" height="35" rx="5" fill="#00695C" opacity="0.1" stroke="#00695C" stroke-width="1"/>
    <text x="250" y="107" font-family="Arial,sans-serif" font-size="10" fill="#004D40" text-anchor="middle" font-weight="bold">Правонарушение — виновное противоправное деяние, влекущее юридическую ответственность</text>

    <!-- Classification -->
    <rect x="25" y="132" width="225" height="85" rx="6" fill="white" stroke="#C62828" stroke-width="1.5"/>
    <rect x="25" y="132" width="225" height="20" rx="6" fill="#C62828" opacity="0.8"/>
    <text x="137" y="147" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">Преступление</text>
    <text x="35" y="167" font-family="Arial,sans-serif" font-size="8" fill="#004D40">Общественно опасное деяние</text>
    <text x="35" y="180" font-family="Arial,sans-serif" font-size="8" fill="#666">Пример: кража, убийство, мошенничество</text>
    <text x="35" y="196" font-family="Arial,sans-serif" font-size="8" fill="#C62828" font-weight="bold">Ответственность: уголовная</text>
    <text x="35" y="208" font-family="Arial,sans-serif" font-size="8" fill="#C62828">Лишение свободы, штраф</text>

    <rect x="260" y="132" width="215" height="85" rx="6" fill="white" stroke="#00695C" stroke-width="1.5"/>
    <rect x="260" y="132" width="215" height="20" rx="6" fill="#00695C"/>
    <text x="367" y="147" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">Проступок</text>
    <text x="270" y="167" font-family="Arial,sans-serif" font-size="8" fill="#004D40">Не представляет общественной опасности</text>
    <text x="270" y="180" font-family="Arial,sans-serif" font-size="8" fill="#666">Пример: нарушение ПДД, мелкое хулиганство</text>
    <text x="270" y="196" font-family="Arial,sans-serif" font-size="8" fill="#00695C" font-weight="bold">Ответственность:</text>
    <text x="270" y="208" font-family="Arial,sans-serif" font-size="8" fill="#00695C">Административная, дисциплинарная</text>

    <!-- Elements of offence -->
    <rect x="25" y="225" width="450" height="73" rx="6" fill="white" stroke="#00695C" stroke-width="1"/>
    <text x="250" y="243" font-family="Arial,sans-serif" font-size="10" fill="#00695C" text-anchor="middle" font-weight="bold">Состав правонарушения</text>
    <rect x="35" y="250" width="100" height="38" rx="4" fill="#00695C" opacity="0.1" stroke="#00695C" stroke-width="1"/>
    <text x="85" y="268" font-family="Arial,sans-serif" font-size="8" fill="#00695C" text-anchor="middle" font-weight="bold">Объект</text>
    <text x="85" y="280" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Охраняемое благо</text>
    <rect x="145" y="250" width="100" height="38" rx="4" fill="#00897B" opacity="0.1" stroke="#00897B" stroke-width="1"/>
    <text x="195" y="268" font-family="Arial,sans-serif" font-size="8" fill="#00897B" text-anchor="middle" font-weight="bold">Субъект</text>
    <text x="195" y="280" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Правонарушитель</text>
    <rect x="255" y="250" width="100" height="38" rx="4" fill="#26A69A" opacity="0.1" stroke="#26A69A" stroke-width="1"/>
    <text x="305" y="268" font-family="Arial,sans-serif" font-size="8" fill="#26A69A" text-anchor="middle" font-weight="bold">Объект. сторона</text>
    <text x="305" y="280" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Деяние, последствия</text>
    <rect x="365" y="250" width="100" height="38" rx="4" fill="#004D40" opacity="0.1" stroke="#004D40" stroke-width="1"/>
    <text x="415" y="268" font-family="Arial,sans-serif" font-size="8" fill="#004D40" text-anchor="middle" font-weight="bold">Субъект. сторона</text>
    <text x="415" y="280" font-family="Arial,sans-serif" font-size="7" fill="#666" text-anchor="middle">Вина, мотив, цель</text>'''

    elif n == 12:
        # Избирательное право
        return '''
    <!-- Definition -->
    <rect x="25" y="90" width="450" height="35" rx="5" fill="#00695C" opacity="0.1" stroke="#00695C" stroke-width="1"/>
    <text x="250" y="107" font-family="Arial,sans-serif" font-size="10" fill="#004D40" text-anchor="middle" font-weight="bold">Избирательное право — совокупность правовых норм, регулирующих порядок выборов</text>

    <!-- Principles -->
    <rect x="25" y="132" width="220" height="85" rx="6" fill="white" stroke="#00695C" stroke-width="1.5"/>
    <rect x="25" y="132" width="220" height="20" rx="6" fill="#00695C"/>
    <text x="135" y="147" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">Принципы избирательного права</text>
    <circle cx="40" cy="168" r="3" fill="#00695C"/>
    <text x="48" y="172" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Всеобщее (с 18 лет)</text>
    <circle cx="40" cy="184" r="3" fill="#00695C"/>
    <text x="48" y="188" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Равное (1 человек = 1 голос)</text>
    <circle cx="40" cy="200" r="3" fill="#00695C"/>
    <text x="48" y="204" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Прямое (непосредственное)</text>
    <circle cx="40" cy="208" r="3" fill="#26A69A"/>
    <text x="48" y="212" font-family="Arial,sans-serif" font-size="0" fill="#004D40">spacer</text>

    <rect x="255" y="132" width="220" height="85" rx="6" fill="white" stroke="#00897B" stroke-width="1.5"/>
    <rect x="255" y="132" width="220" height="20" rx="6" fill="#00897B"/>
    <text x="365" y="147" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle" font-weight="bold">Тайное голосование</text>
    <text x="265" y="167" font-family="Arial,sans-serif" font-size="9" fill="#004D40">Никто не может контролировать</text>
    <text x="265" y="180" font-family="Arial,sans-serif" font-size="9" fill="#004D40">волеизъявление гражданина</text>
    <line x1="265" y1="188" x2="465" y2="188" stroke="#00897B" stroke-width="0.5" opacity="0.3"/>
    <text x="365" y="203" font-family="Arial,sans-serif" font-size="8" fill="#666">Бюллетень не содержит идентификации</text>
    <text x="365" y="214" font-family="Arial,sans-serif" font-size="8" fill="#666">Кабина для тайного голосования</text>

    <!-- Types of electoral systems -->
    <rect x="25" y="225" width="215" height="73" rx="6" fill="white" stroke="#00695C" stroke-width="1.5"/>
    <rect x="25" y="225" width="215" height="20" rx="6" fill="#00695C"/>
    <text x="132" y="240" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Мажоритарная система</text>
    <text x="35" y="258" font-family="Arial,sans-serif" font-size="8" fill="#004D40">Побеждает набравший большинство</text>
    <text x="35" y="270" font-family="Arial,sans-serif" font-size="8" fill="#666">Пример: выборы Президента РФ</text>
    <text x="35" y="286" font-family="Arial,sans-serif" font-size="8" fill="#00695C">+ связь депутат-избиратель</text>
    <text x="35" y="296" font-family="Arial,sans-serif" font-size="8" fill="#C62828">- неучтённые голоса меньшинства</text>

    <rect x="250" y="225" width="225" height="73" rx="6" fill="white" stroke="#00897B" stroke-width="1.5"/>
    <rect x="250" y="225" width="225" height="20" rx="6" fill="#00897B"/>
    <text x="362" y="240" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Пропорциональная система</text>
    <text x="260" y="258" font-family="Arial,sans-serif" font-size="8" fill="#004D40">Места по % голосов за партию</text>
    <text x="260" y="270" font-family="Arial,sans-serif" font-size="8" fill="#666">Пример: выборы в Гос. Думу</text>
    <text x="260" y="286" font-family="Arial,sans-serif" font-size="8" fill="#00897B">+ представительство партий</text>
    <text x="260" y="296" font-family="Arial,sans-serif" font-size="8" fill="#C62828">- слабая связь депутат-избиратель</text>'''

    return ''


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    generated = []
    errors = []

    for lesson_num, title in LESSONS:
        svg_content = make_svg(lesson_num, title)
        filepath = os.path.join(OUTPUT_DIR, f"lesson{lesson_num}.svg")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)

        # Validate XML
        try:
            ET.parse(filepath)
            generated.append(filepath)
            print(f"OK: lesson{lesson_num}.svg — {title}")
        except ET.ParseError as e:
            errors.append((filepath, str(e)))
            print(f"ERROR: lesson{lesson_num}.svg — {e}")

    print(f"\nGenerated {len(generated)} SVGs, {len(errors)} errors")
    if errors:
        for fp, err in errors:
            print(f"  {fp}: {err}")

    return len(errors) == 0


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
