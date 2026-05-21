#!/usr/bin/env python3
"""Generate Physics grade 10 SVG lesson illustrations (lessons 51-64)."""
import os
OUT = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade10/physics"
os.makedirs(OUT, exist_ok=True)
P = "#1565C0"; L = "#E3F2FD"; M = "#BBDEFB"
def hdr(title, num):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{L}"/><stop offset="100%" stop-color="{M}"/></linearGradient></defs>
<rect width="500" height="350" fill="url(#bg)" rx="10"/>
<rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="{P}" stroke-width="2.5"/>
<text x="250" y="30" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="{P}" text-anchor="middle">{title}</text>
<text x="250" y="46" font-family="Arial,sans-serif" font-size="10" fill="#888" text-anchor="middle">Физика 10 класс — Урок {num}</text>
<line x1="30" y1="52" x2="470" y2="52" stroke="{P}" stroke-width="1.5" opacity="0.25"/>
'''
ftr = f'\n<rect x="10" y="325" width="480" height="20" rx="4" fill="{P}" opacity="0.85"/>\n<text x="250" y="339" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="white" font-weight="bold">Физика 10 класс</text>\n</svg>'
def ib(x,y,w,h,lines):
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="white" stroke="{P}" stroke-width="1" opacity="0.9"/>\n'
    for i,l in enumerate(lines): s+=f'<text x="{x+w//2}" y="{y+14+i*11}" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">{l}</text>\n'
    return s

# 51: Тепловые двигатели. Принцип действия
svg51=hdr("Тепловые двигатели. Принцип действия",51)+f'''
<!-- Hot reservoir -->
<rect x="160" y="65" width="180" height="30" rx="5" fill="#E53935" opacity="0.85"/>
<text x="250" y="84" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Нагреватель T1</text>
<!-- Q1 arrow down -->
<line x1="250" y1="95" x2="250" y2="125" stroke="#E53935" stroke-width="2.5"/>
<polygon points="250,125 245,118 255,118" fill="#E53935"/>
<text x="275" y="115" font-family="Arial,sans-serif" font-size="9" fill="#E53935" font-weight="bold">Q1</text>
<!-- Engine block -->
<rect x="185" y="128" width="130" height="55" rx="8" fill="white" stroke="{P}" stroke-width="2"/>
<text x="250" y="150" font-family="Arial,sans-serif" font-size="10" fill="{P}" text-anchor="middle" font-weight="bold">Двигатель</text>
<text x="250" y="170" font-family="Arial,sans-serif" font-size="9" fill="#555" text-anchor="middle">(рабочее тело)</text>
<!-- Work arrow right -->
<line x1="315" y1="155" x2="380" y2="155" stroke="#2E7D32" stroke-width="2.5"/>
<polygon points="380,155 373,151 373,159" fill="#2E7D32"/>
<text x="350" y="148" font-family="Arial,sans-serif" font-size="9" fill="#2E7D32" font-weight="bold">A</text>
<!-- Q2 arrow down -->
<line x1="250" y1="183" x2="250" y2="215" stroke="#1565C0" stroke-width="2.5"/>
<polygon points="250,215 245,208 255,208" fill="#1565C0"/>
<text x="275" y="208" font-family="Arial,sans-serif" font-size="9" fill="#1565C0" font-weight="bold">Q2</text>
<!-- Cold reservoir -->
<rect x="160" y="218" width="180" height="30" rx="5" fill="#1565C0" opacity="0.85"/>
<text x="250" y="237" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">Холодильник T2</text>
<!-- Key formulas box -->
<rect x="30" y="90" width="115" height="85" rx="6" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="87" y="108" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Первое начало</text>
<line x1="40" y1="113" x2="135" y2="113" stroke="{P}" stroke-width="0.5"/>
<text x="87" y="128" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Q1 = A + Q2</text>
<text x="87" y="145" font-family="Arial,sans-serif" font-size="6" fill="#888" text-anchor="middle">Теплота от нагревателя</text>
<text x="87" y="157" font-family="Arial,sans-serif" font-size="6" fill="#888" text-anchor="middle">идёт на работу и</text>
<text x="87" y="169" font-family="Arial,sans-serif" font-size="6" fill="#888" text-anchor="middle">теплоту холодильнику</text>
<!-- Work output box -->
<rect x="370" y="128" width="110" height="55" rx="6" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="425" y="146" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Полезная работа</text>
<line x1="380" y1="151" x2="470" y2="151" stroke="#2E7D32" stroke-width="0.5"/>
<text x="425" y="166" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">A = Q1 - Q2</text>
<text x="425" y="178" font-family="Arial,sans-serif" font-size="6" fill="#888" text-anchor="middle">A &lt; Q1 всегда</text>
<!-- Examples -->
<rect x="60" y="265" width="380" height="45" rx="6" fill="white" stroke="{P}" stroke-width="1"/>
<text x="250" y="280" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Примеры тепловых двигателей</text>
<text x="250" y="298" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">ДВС (автомобиль) | Паровая турбина (Электростанция) | Реактивный двигатель | Газовая турбина</text>
'''+ftr

# 52: КПД теплового двигателя
svg52=hdr("КПД теплового двигателя",52)+f'''
<!-- Central formula -->
<circle cx="250" cy="140" r="55" fill="white" stroke="#E53935" stroke-width="2"/>
<text x="250" y="130" font-family="Arial,sans-serif" font-size="12" fill="#E53935" text-anchor="middle" font-weight="bold">eta = A/Q1</text>
<text x="250" y="148" font-family="Arial,sans-serif" font-size="9" fill="#555" text-anchor="middle">= (Q1-Q2)/Q1</text>
<text x="250" y="163" font-family="Arial,sans-serif" font-size="7" fill="#888" text-anchor="middle">КПД &lt; 100% всегда</text>
<!-- Efficiency formula box -->
<rect x="30" y="80" width="120" height="75" rx="6" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="90" y="98" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Определение</text>
<line x1="40" y1="103" x2="140" y2="103" stroke="{P}" stroke-width="0.5"/>
<text x="90" y="118" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">eta = A/Q1 * 100%</text>
<text x="90" y="133" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Отношение полезной</text>
<text x="90" y="145" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">работы к затраченной</text>
<!-- Carnot box -->
<rect x="365" y="80" width="120" height="75" rx="6" fill="white" stroke="#7B1FA2" stroke-width="1.5"/>
<text x="425" y="98" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Цикл Карно</text>
<line x1="375" y1="103" x2="475" y2="103" stroke="#7B1FA2" stroke-width="0.5"/>
<text x="425" y="118" font-family="Arial,sans-serif" font-size="8" fill="#7B1FA2" text-anchor="middle" font-weight="bold">eta_max</text>
<text x="425" y="133" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">= (T1-T2)/T1</text>
<text x="425" y="148" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Максимальный КПД</text>
<!-- Bar chart of typical efficiencies -->
<rect x="50" y="210" width="400" height="100" rx="6" fill="white" stroke="{P}" stroke-width="1"/>
<text x="250" y="228" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Типичные значения КПД</text>
<!-- Bars -->
<rect x="70" y="260" width="50" height="40" rx="2" fill="#E53935" opacity="0.7"/>
<text x="95" y="285" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle" font-weight="bold">40%</text>
<text x="95" y="302" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">ДВС</text>
<rect x="140" y="255" width="50" height="45" rx="2" fill="#E65100" opacity="0.7"/>
<text x="165" y="280" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle" font-weight="bold">45%</text>
<text x="165" y="302" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Дизель</text>
<rect x="210" y="240" width="50" height="60" rx="2" fill="#2E7D32" opacity="0.7"/>
<text x="235" y="273" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle" font-weight="bold">60%</text>
<text x="235" y="302" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Пар. турб.</text>
<rect x="280" y="250" width="50" height="50" rx="2" fill="#7B1FA2" opacity="0.7"/>
<text x="305" y="278" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle" font-weight="bold">50%</text>
<text x="305" y="302" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Газ. турб.</text>
<rect x="350" y="235" width="50" height="65" rx="2" fill="#1565C0" opacity="0.7"/>
<text x="375" y="270" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle" font-weight="bold">80%</text>
<text x="375" y="302" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">Карно идеал.</text>
'''+ftr

# 53: Второй закон термодинамики
svg53=hdr("Второй закон термодинамики",53)+f'''
<!-- Entropy arrow -->
<g transform="translate(250,120)">
<rect x="-100" y="-35" width="200" height="70" rx="8" fill="white" stroke="#7B1FA2" stroke-width="2"/>
<text x="0" y="-15" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Энтропия</text>
<text x="0" y="3" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">delta S &gt;= 0</text>
<text x="0" y="20" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">в изолированной системе</text>
</g>
<!-- Clausius formulation -->
<rect x="20" y="175" width="220" height="75" rx="6" fill="white" stroke="#E53935" stroke-width="1.5"/>
<text x="130" y="193" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle" font-weight="bold">Формулировка Клаузиуса</text>
<line x1="30" y1="198" x2="230" y2="198" stroke="#E53935" stroke-width="0.5"/>
<text x="130" y="214" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Теплота не может самопроизвольно</text>
<text x="130" y="226" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">переходить от холодного тела</text>
<text x="130" y="238" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">к нагретому</text>
<!-- Kelvin formulation -->
<rect x="260" y="175" width="220" height="75" rx="6" fill="white" stroke="#1565C0" stroke-width="1.5"/>
<text x="370" y="193" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">Формулировка Кельвина</text>
<line x1="270" y1="198" x2="470" y2="198" stroke="#1565C0" stroke-width="0.5"/>
<text x="370" y="214" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">Невозможно создать тепловой</text>
<text x="370" y="226" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">двигатель с КПД = 100%</text>
<text x="370" y="238" font-family="Arial,sans-serif" font-size="6" fill="#333" text-anchor="middle">(вечный двигатель 2 рода)</text>
<!-- Irreversibility illustration -->
<rect x="60" y="268" width="380" height="45" rx="6" fill="white" stroke="#FF6F00" stroke-width="1"/>
<text x="250" y="283" font-family="Arial,sans-serif" font-size="7" fill="#FF6F00" text-anchor="middle" font-weight="bold">Необратимость процессов в природе</text>
<text x="250" y="300" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Теплопередача | Расширение газа | Трение | Диффузия — всё идёт в одном направлении</text>
'''+ftr

# 54: Плавление и кристаллизация
svg54=hdr("Плавление и кристаллизация",54)+f'''
<!-- Heating curve graph -->
<rect x="40" y="60" width="420" height="200" rx="6" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="250" y="78" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">График нагревания и плавления</text>
<!-- Axes -->
<line x1="80" y1="240" x2="440" y2="240" stroke="#333" stroke-width="1.5"/>
<polygon points="440,240 434,237 434,243" fill="#333"/>
<text x="440" y="252" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">t</text>
<line x1="80" y1="240" x2="80" y2="90" stroke="#333" stroke-width="1.5"/>
<polygon points="80,90 77,96 83,96" fill="#333"/>
<text x="70" y="95" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">T</text>
<!-- Heating curve: solid heating, melting plateau, liquid heating -->
<polyline points="80,230 140,190 140,190 230,190 230,190 300,160 380,130" fill="none" stroke="#E53935" stroke-width="2.5"/>
<!-- Melting plateau -->
<line x1="140" y1="190" x2="230" y2="190" stroke="#2E7D32" stroke-width="3"/>
<!-- Labels -->
<text x="100" y="225" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">Нагрев</text>
<text x="100" y="233" font-family="Arial,sans-serif" font-size="5" fill="#1565C0" text-anchor="middle">твёрдого</text>
<text x="185" y="185" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle" font-weight="bold">Плавление</text>
<text x="340" y="155" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">Нагрев</text>
<text x="340" y="163" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">жидкости</text>
<!-- T melt line -->
<line x1="80" y1="190" x2="140" y2="190" stroke="#7B1FA2" stroke-width="0.8" stroke-dasharray="3,2"/>
<text x="73" y="193" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="end">Tпл</text>
<!-- Formula box -->
<rect x="30" y="275" width="210" height="40" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
<text x="135" y="290" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle" font-weight="bold">Удельная теплота плавления</text>
<text x="135" y="306" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">Q = lambda * m</text>
<!-- Info box -->
<rect x="260" y="275" width="210" height="40" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="365" y="290" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">При плавлении / кристаллизации</text>
<text x="365" y="306" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">T = const, Q поглощается / выделяется</text>
'''+ftr

# 55: Испарение и конденсация. Кипение
svg55=hdr("Испарение и конденсация. Кипение",55)+f'''
<!-- Evaporation illustration -->
<rect x="30" y="60" width="200" height="135" rx="6" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="130" y="78" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Испарение</text>
<!-- Liquid surface -->
<rect x="55" y="140" width="150" height="30" rx="2" fill="#BBDEFB" stroke="#1565C0" stroke-width="1"/>
<text x="130" y="160" font-family="Arial,sans-serif" font-size="6" fill="#1565C0" text-anchor="middle">жидкость</text>
<!-- Escaping molecules -->
<circle cx="80" cy="130" r="3" fill="#E53935" opacity="0.7"/>
<line x1="80" y1="127" x2="80" y2="115" stroke="#E53935" stroke-width="0.8" stroke-dasharray="2,1"/>
<circle cx="130" cy="125" r="3" fill="#E53935" opacity="0.7"/>
<line x1="130" y1="122" x2="130" y2="108" stroke="#E53935" stroke-width="0.8" stroke-dasharray="2,1"/>
<circle cx="170" cy="132" r="3" fill="#E53935" opacity="0.7"/>
<line x1="170" y1="129" x2="170" y2="112" stroke="#E53935" stroke-width="0.8" stroke-dasharray="2,1"/>
<text x="130" y="105" font-family="Arial,sans-serif" font-size="5" fill="#E53935" text-anchor="middle">молекулы вылетают</text>
<text x="130" y="185" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">с поверхности, при любой T</text>
<!-- Boiling illustration -->
<rect x="260" y="60" width="210" height="135" rx="6" fill="white" stroke="#E65100" stroke-width="1.5"/>
<text x="365" y="78" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">Кипение</text>
<!-- Vessel -->
<rect x="290" y="140" width="120" height="30" rx="2" fill="#BBDEFB" stroke="#1565C0" stroke-width="1"/>
<!-- Bubbles -->
<circle cx="310" cy="135" r="4" fill="none" stroke="#1565C0" stroke-width="1"/>
<circle cx="340" cy="130" r="5" fill="none" stroke="#1565C0" stroke-width="1"/>
<circle cx="370" cy="128" r="3" fill="none" stroke="#1565C0" stroke-width="1"/>
<circle cx="325" cy="118" r="3" fill="none" stroke="#1565C0" stroke-width="0.8" opacity="0.6"/>
<circle cx="355" cy="115" r="4" fill="none" stroke="#1565C0" stroke-width="0.8" opacity="0.6"/>
<text x="365" y="105" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">пузырьки по всему объёму</text>
<text x="365" y="185" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">при T = Tкип, P = Pнас</text>
<!-- Formulas -->
<rect x="30" y="210" width="210" height="45" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
<text x="135" y="226" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle" font-weight="bold">Удельная теплота парообразования</text>
<text x="135" y="244" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle">Q = L * m</text>
<!-- Condensation -->
<rect x="260" y="210" width="210" height="45" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
<text x="365" y="226" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">Конденсация</text>
<text x="365" y="244" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Q выделяется = L * m, T = const</text>
<!-- Boiling point note -->
<rect x="80" y="270" width="340" height="40" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1"/>
<text x="250" y="285" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Tкип зависит от давления</text>
<text x="250" y="300" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Высокогорье: P↓ → Tкип↓ | Автоклав: P↑ → Tкип↑</text>
'''+ftr

# 56: Насыщенный пар. Влажность
svg56=hdr("Насыщенный пар. Влажность",56)+f'''
<!-- P vs T graph for saturated vapor -->
<rect x="30" y="60" width="240" height="165" rx="6" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="150" y="78" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Давление насыщенного пара Pн(T)</text>
<!-- Axes -->
<line x1="60" y1="200" x2="250" y2="200" stroke="#333" stroke-width="1"/>
<polygon points="250,200 244,197 244,203" fill="#333"/>
<text x="250" y="212" font-family="Arial,sans-serif" font-size="6" fill="#333">T</text>
<line x1="60" y1="200" x2="60" y2="90" stroke="#333" stroke-width="1"/>
<polygon points="60,90 57,96 63,96" fill="#333"/>
<text x="52" y="95" font-family="Arial,sans-serif" font-size="6" fill="#333">Pн</text>
<!-- Curve -->
<path d="M60,195 Q100,193 130,180 Q160,160 190,130 Q210,108 240,95" fill="none" stroke="#E53935" stroke-width="2"/>
<!-- Boiling point label -->
<circle cx="190" cy="130" r="3" fill="#E53935"/>
<text x="210" y="128" font-family="Arial,sans-serif" font-size="5" fill="#E53935">Tкип при Pатм</text>
<!-- Unsat line -->
<path d="M60,195 Q130,190 200,180 Q230,175 250,172" fill="none" stroke="#7B1FA2" stroke-width="1.2" stroke-dasharray="4,2"/>
<text x="220" y="168" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2">ненасыщ.</text>
<!-- Humidity info -->
<rect x="290" y="60" width="190" height="165" rx="6" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="385" y="78" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Влажность воздуха</text>
<line x1="300" y1="85" x2="470" y2="85" stroke="#2E7D32" stroke-width="0.5"/>
<text x="385" y="102" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Относительная:</text>
<text x="385" y="118" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle" font-weight="bold">phi = P/Pн * 100%</text>
<line x1="300" y1="128" x2="470" y2="128" stroke="#2E7D32" stroke-width="0.5"/>
<text x="385" y="145" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Абсолютная:</text>
<text x="385" y="160" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">rho = m/V (г/м^3)</text>
<line x1="300" y1="170" x2="470" y2="170" stroke="#2E7D32" stroke-width="0.5"/>
<text x="385" y="187" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Точка росы</text>
<text x="385" y="202" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">T при которой phi = 100%</text>
<text x="385" y="214" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">выпадает конденсат</text>
<!-- Psychrometer note -->
<rect x="60" y="240" width="380" height="40" rx="5" fill="white" stroke="#FF6F00" stroke-width="1"/>
<text x="250" y="255" font-family="Arial,sans-serif" font-size="7" fill="#FF6F00" text-anchor="middle" font-weight="bold">Психрометр: разность сухого и влажного термометров → phi</text>
<text x="250" y="270" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Норма: phi = 40-60% | Комфорт: phi = 30-50%</text>
'''+ftr

# 57: Поверхностное натяжение. Смачивание. Капиллярность
svg57=hdr("Поверхностное натяжение. Смачивание. Капиллярность",57)+f'''
<!-- Surface tension diagram -->
<rect x="20" y="60" width="150" height="130" rx="6" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="95" y="78" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Поверхностное натяжение</text>
<!-- Liquid surface with molecules -->
<rect x="35" y="120" width="120" height="40" rx="2" fill="#BBDEFB" stroke="#1565C0" stroke-width="1"/>
<!-- Surface layer -->
<line x1="35" y1="120" x2="155" y2="120" stroke="#E53935" stroke-width="2"/>
<!-- Molecules inside -->
<circle cx="55" cy="135" r="3" fill="#1565C0"/>
<circle cx="80" cy="130" r="3" fill="#1565C0"/>
<circle cx="105" cy="140" r="3" fill="#1565C0"/>
<circle cx="130" cy="132" r="3" fill="#1565C0"/>
<!-- Surface molecule with forces -->
<circle cx="95" cy="120" r="3" fill="#E53935"/>
<!-- Forces on surface molecule -->
<line x1="95" y1="117" x2="95" y2="108" stroke="#E53935" stroke-width="1.2"/>
<text x="102" y="108" font-family="Arial,sans-serif" font-size="5" fill="#E53935">F рез.</text>
<text x="95" y="175" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">F = sigma * l</text>
<text x="95" y="185" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">sigma — коэфф. пов. натяжения</text>
<!-- Wetting angles -->
<rect x="185" y="60" width="140" height="130" rx="6" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="255" y="78" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Смачивание</text>
<!-- Good wetting -->
<rect x="200" y="150" width="40" height="20" rx="1" fill="#795548" stroke="#333" stroke-width="0.5"/>
<path d="M200,150 Q210,140 215,150" fill="#BBDEFB" stroke="#1565C0" stroke-width="1"/>
<text x="220" y="100" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Смачивание</text>
<text x="220" y="108" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">theta &lt; 90</text>
<path d="M210,150 L218,140" stroke="#E53935" stroke-width="1"/>
<!-- Non-wetting -->
<rect x="275" y="150" width="40" height="20" rx="1" fill="#795548" stroke="#333" stroke-width="0.5"/>
<path d="M275,150 Q285,158 295,150" fill="#BBDEFB" stroke="#1565C0" stroke-width="1"/>
<text x="295" y="100" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">Несмачивание</text>
<text x="295" y="108" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">theta &gt; 90</text>
<path d="M285,150 L280,140" stroke="#E53935" stroke-width="1"/>
<!-- Capillary tubes -->
<rect x="340" y="60" width="145" height="130" rx="6" fill="white" stroke="#7B1FA2" stroke-width="1.5"/>
<text x="412" y="78" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Капиллярность</text>
<!-- Tube 1 - wetting (water) -->
<rect x="370" y="90" width="16" height="70" rx="1" fill="none" stroke="#333" stroke-width="1.2"/>
<path d="M370,120 Q378,110 386,120" fill="#BBDEFB" stroke="#1565C0" stroke-width="0.8"/>
<rect x="370" y="120" width="16" height="40" fill="#BBDEFB" opacity="0.5"/>
<text x="378" y="165" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">h↑</text>
<text x="378" y="88" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32" text-anchor="middle">Вода</text>
<!-- Tube 2 - non-wetting (mercury) -->
<rect x="440" y="90" width="16" height="70" rx="1" fill="none" stroke="#333" stroke-width="1.2"/>
<path d="M440,140 Q448,148 456,140" fill="#BBDEFB" stroke="#1565C0" stroke-width="0.8"/>
<rect x="440" y="140" width="16" height="20" fill="#BBDEFB" opacity="0.5"/>
<text x="448" y="165" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">h↓</text>
<text x="448" y="88" font-family="Arial,sans-serif" font-size="5" fill="#E65100" text-anchor="middle">Ртуть</text>
<!-- Jurin formula -->
<rect x="40" y="205" width="420" height="55" rx="6" fill="white" stroke="#E53935" stroke-width="1.5"/>
<text x="250" y="222" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle" font-weight="bold">Формула Жюрена</text>
<text x="250" y="240" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">h = 2*sigma*cos(theta) / (rho*g*r)</text>
<text x="250" y="254" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">r — радиус капилляра | rho — плотность жидкости | theta — краевой угол</text>
'''+ftr

# 58: Электризация тел. Электрический заряд
svg58=hdr("Электризация тел. Электрический заряд",58)+f'''
<!-- Two charge types -->
<circle cx="110" cy="110" r="25" fill="#E53935" opacity="0.2" stroke="#E53935" stroke-width="1.5"/>
<text x="110" y="114" font-family="Arial,sans-serif" font-size="18" fill="#E53935" text-anchor="middle" font-weight="bold">+</text>
<text x="110" y="145" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle">Положительный</text>
<circle cx="250" cy="110" r="25" fill="#1565C0" opacity="0.2" stroke="#1565C0" stroke-width="1.5"/>
<text x="250" y="114" font-family="Arial,sans-serif" font-size="18" fill="#1565C0" text-anchor="middle" font-weight="bold">-</text>
<text x="250" y="145" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle">Отрицательный</text>
<!-- Interaction arrows -->
<line x1="140" y1="105" x2="220" y2="105" stroke="#FF6F00" stroke-width="1.5"/>
<text x="180" y="100" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle">отталкивание</text>
<!-- Electroscope -->
<rect x="340" y="70" width="130" height="100" rx="6" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="405" y="87" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Электроскоп</text>
<!-- Jar -->
<rect x="370" y="92" width="70" height="60" rx="3" fill="none" stroke="#333" stroke-width="1.2"/>
<!-- Rod -->
<line x1="405" y1="92" x2="405" y2="75" stroke="#333" stroke-width="2"/>
<!-- Leaves -->
<line x1="405" y1="120" x2="390" y2="140" stroke="#FFD600" stroke-width="1.5"/>
<line x1="405" y1="120" x2="420" y2="140" stroke="#FFD600" stroke-width="1.5"/>
<circle cx="405" cy="120" r="2" fill="#333"/>
<text x="405" y="160" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">листочки расходятся</text>
<!-- Charge conservation -->
<rect x="30" y="180" width="210" height="55" rx="6" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="135" y="198" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Закон сохранения заряда</text>
<text x="135" y="216" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">q1 + q2 + ... = const</text>
<text x="135" y="230" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">в изолированной системе</text>
<!-- Electrification methods -->
<rect x="260" y="180" width="220" height="55" rx="6" fill="white" stroke="#7B1FA2" stroke-width="1.5"/>
<text x="370" y="198" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Способы электризации</text>
<text x="370" y="214" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Трением | Контактом | Через влияние</text>
<text x="370" y="228" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Электростатическая индукция</text>
<!-- Elementary charge -->
<rect x="80" y="250" width="340" height="40" rx="5" fill="white" stroke="#E65100" stroke-width="1.2"/>
<text x="250" y="266" font-family="Arial,sans-serif" font-size="7" fill="#E65100" text-anchor="middle" font-weight="bold">Элементарный заряд: e = 1.6 * 10^-19 Кл</text>
<text x="250" y="282" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">q = n*e | Электрон: q = -e | Протон: q = +e</text>
'''+ftr

# 59: Закон Кулона
svg59=hdr("Закон Кулона",59)+f'''
<!-- Two charges with force -->
<g transform="translate(200,145)">
<circle cx="-55" cy="0" r="20" fill="#E53935" opacity="0.2" stroke="#E53935" stroke-width="1.5"/>
<text x="-55" y="5" font-family="Arial,sans-serif" font-size="9" fill="#E53935" text-anchor="middle" font-weight="bold">q1</text>
<circle cx="55" cy="0" r="20" fill="#E53935" opacity="0.2" stroke="#E53935" stroke-width="1.5"/>
<text x="55" y="5" font-family="Arial,sans-serif" font-size="9" fill="#E53935" text-anchor="middle" font-weight="bold">q2</text>
<!-- Repulsion arrows (like charges) -->
<line x1="-35" y1="0" x2="-55" y2="0" stroke="#E53935" stroke-width="2"/>
<polygon points="-55,0 -48,-3 -48,3" fill="#E53935"/>
<line x1="35" y1="0" x2="55" y2="0" stroke="#E53935" stroke-width="2"/>
<polygon points="55,0 48,-3 48,3" fill="#E53935"/>
<!-- Distance r -->
<line x1="-55" y1="30" x2="55" y2="30" stroke="#7B1FA2" stroke-width="1.2"/>
<line x1="-55" y1="25" x2="-55" y2="35" stroke="#7B1FA2" stroke-width="1"/>
<line x1="55" y1="25" x2="55" y2="35" stroke="#7B1FA2" stroke-width="1"/>
<text x="0" y="42" font-family="Arial,sans-serif" font-size="8" fill="#7B1FA2" text-anchor="middle" font-weight="bold">r</text>
<text x="0" y="-30" font-family="Arial,sans-serif" font-size="6" fill="#E53935" text-anchor="middle">одноимённые — отталкивание</text>
</g>
<!-- Unlike charges below -->
<g transform="translate(200,230)">
<circle cx="-55" cy="0" r="16" fill="#E53935" opacity="0.2" stroke="#E53935" stroke-width="1"/>
<text x="-55" y="4" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle" font-weight="bold">+</text>
<circle cx="55" cy="0" r="16" fill="#1565C0" opacity="0.2" stroke="#1565C0" stroke-width="1"/>
<text x="55" y="4" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" text-anchor="middle" font-weight="bold">-</text>
<line x1="-39" y1="0" x2="-55" y2="0" stroke="#2E7D32" stroke-width="1.5"/>
<polygon points="-55,0 -48,-3 -48,3" fill="#2E7D32"/>
<line x1="39" y1="0" x2="55" y2="0" stroke="#2E7D32" stroke-width="1.5"/>
<polygon points="55,0 48,-3 48,3" fill="#2E7D32"/>
<text x="0" y="-22" font-family="Arial,sans-serif" font-size="6" fill="#2E7D32" text-anchor="middle">разноимённые — притяжение</text>
</g>
<!-- Main formula -->
<rect x="330" y="70" width="155" height="80" rx="6" fill="white" stroke="{P}" stroke-width="2"/>
<text x="407" y="90" font-family="Arial,sans-serif" font-size="8" fill="{P}" text-anchor="middle" font-weight="bold">Закон Кулона</text>
<line x1="340" y1="95" x2="475" y2="95" stroke="{P}" stroke-width="0.5"/>
<text x="407" y="115" font-family="Arial,sans-serif" font-size="11" fill="#E53935" text-anchor="middle" font-weight="bold">F = k*q1*q2/r^2</text>
<text x="407" y="135" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">k = 9*10^9 Н*м^2/Кл^2</text>
<text x="407" y="145" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">= 1/(4*pi*epsilon0)</text>
<!-- Conditions -->
<rect x="330" y="165" width="155" height="65" rx="6" fill="white" stroke="#FF6F00" stroke-width="1.2"/>
<text x="407" y="182" font-family="Arial,sans-serif" font-size="7" fill="#FF6F00" text-anchor="middle" font-weight="bold">Условия применения</text>
<line x1="340" y1="187" x2="475" y2="187" stroke="#FF6F00" stroke-width="0.5"/>
<text x="407" y="202" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Точечные заряды</text>
<text x="407" y="214" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Шары (r &lt;&lt; R)</text>
<text x="407" y="226" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Вакуум / воздух</text>
'''+ftr

# 60: Электрическое поле. Напряжённость
svg60=hdr("Электрическое поле. Напряжённость",60)+f'''
<!-- Positive charge field lines -->
<rect x="20" y="60" width="220" height="170" rx="6" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="130" y="78" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Линии напряжённости E</text>
<!-- Positive charge -->
<circle cx="130" cy="145" r="12" fill="#E53935" opacity="0.3" stroke="#E53935" stroke-width="1.5"/>
<text x="130" y="149" font-family="Arial,sans-serif" font-size="10" fill="#E53935" text-anchor="middle" font-weight="bold">+</text>
<!-- Field lines radiating out -->
<line x1="142" y1="145" x2="185" y2="145" stroke="#E53935" stroke-width="1.2"/>
<polygon points="185,145 179,142 179,148" fill="#E53935"/>
<line x1="118" y1="145" x2="75" y2="145" stroke="#E53935" stroke-width="1.2"/>
<polygon points="75,145 81,142 81,148" fill="#E53935"/>
<line x1="130" y1="133" x2="130" y2="95" stroke="#E53935" stroke-width="1.2"/>
<polygon points="130,95 127,101 133,101" fill="#E53935"/>
<line x1="130" y1="157" x2="130" y2="195" stroke="#E53935" stroke-width="1.2"/>
<polygon points="130,195 127,189 133,189" fill="#E53935"/>
<line x1="138" y1="137" x2="165" y2="110" stroke="#E53935" stroke-width="1"/>
<polygon points="165,110 158,113 161,118" fill="#E53935"/>
<line x1="122" y1="137" x2="95" y2="110" stroke="#E53935" stroke-width="1"/>
<polygon points="95,110 101,113 99,118" fill="#E53935"/>
<line x1="138" y1="153" x2="165" y2="180" stroke="#E53935" stroke-width="1"/>
<polygon points="165,180 158,177 161,172" fill="#E53935"/>
<line x1="122" y1="153" x2="95" y2="180" stroke="#E53935" stroke-width="1"/>
<polygon points="95,180 101,177 99,172" fill="#E53935"/>
<!-- Test charge -->
<circle cx="175" cy="145" r="5" fill="#7B1FA2" opacity="0.3" stroke="#7B1FA2" stroke-width="1"/>
<text x="175" y="148" font-family="Arial,sans-serif" font-size="5" fill="#7B1FA2" text-anchor="middle">q0</text>
<text x="130" y="215" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">+q: линии от заряда</text>
<!-- Negative charge field -->
<rect x="260" y="60" width="220" height="170" rx="6" fill="white" stroke="#1565C0" stroke-width="1.5"/>
<text x="370" y="78" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">Линии к отрицательному</text>
<circle cx="370" cy="145" r="12" fill="#1565C0" opacity="0.3" stroke="#1565C0" stroke-width="1.5"/>
<text x="370" y="149" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" text-anchor="middle" font-weight="bold">-</text>
<!-- Field lines pointing in -->
<line x1="425" y1="145" x2="382" y2="145" stroke="#1565C0" stroke-width="1.2"/>
<polygon points="382,145 388,142 388,148" fill="#1565C0"/>
<line x1="315" y1="145" x2="358" y2="145" stroke="#1565C0" stroke-width="1.2"/>
<polygon points="358,145 352,142 352,148" fill="#1565C0"/>
<line x1="370" y1="95" x2="370" y2="133" stroke="#1565C0" stroke-width="1.2"/>
<polygon points="370,133 367,127 373,127" fill="#1565C0"/>
<line x1="370" y1="195" x2="370" y2="157" stroke="#1565C0" stroke-width="1.2"/>
<polygon points="370,157 367,163 373,163" fill="#1565C0"/>
<text x="370" y="215" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">-q: линии к заряду</text>
<!-- Formulas -->
<rect x="30" y="245" width="140" height="55" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
<text x="100" y="262" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle" font-weight="bold">Определение</text>
<text x="100" y="278" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">E = F/q</text>
<text x="100" y="293" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">В/м (Н/Кл)</text>
<rect x="180" y="245" width="140" height="55" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
<text x="250" y="262" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Точечный заряд</text>
<text x="250" y="278" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">E = k*q/r^2</text>
<text x="250" y="293" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">убывает с расстоянием</text>
<rect x="330" y="245" width="140" height="55" rx="5" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="400" y="262" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Суперпозиция</text>
<text x="400" y="278" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle" font-weight="bold">E = E1 + E2 + ...</text>
<text x="400" y="293" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">векторная сумма</text>
'''+ftr

# 61: Работа сил электрического поля. Потенциал
svg61=hdr("Работа сил электрического поля. Потенциал",61)+f'''
<!-- Equipotential surfaces -->
<rect x="20" y="60" width="230" height="170" rx="6" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="135" y="78" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Эквипотенциальные поверхности</text>
<!-- Charge -->
<circle cx="135" cy="145" r="10" fill="#E53935" opacity="0.3" stroke="#E53935" stroke-width="1.5"/>
<text x="135" y="149" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle" font-weight="bold">+q</text>
<!-- Equipotential circles -->
<circle cx="135" cy="145" r="30" fill="none" stroke="#2E7D32" stroke-width="1" stroke-dasharray="4,2"/>
<text x="170" y="130" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">phi1</text>
<circle cx="135" cy="145" r="55" fill="none" stroke="#2E7D32" stroke-width="1" stroke-dasharray="4,2"/>
<text x="195" y="118" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">phi2</text>
<circle cx="135" cy="145" r="80" fill="none" stroke="#2E7D32" stroke-width="1" stroke-dasharray="4,2"/>
<text x="220" y="100" font-family="Arial,sans-serif" font-size="5" fill="#2E7D32">phi3</text>
<!-- Field line crossing -->
<line x1="135" y1="135" x2="135" y2="70" stroke="#E53935" stroke-width="1"/>
<polygon points="135,70 132,76 138,76" fill="#E53935"/>
<text x="145" y="95" font-family="Arial,sans-serif" font-size="5" fill="#E53935">E</text>
<text x="135" y="222" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">phi1 &gt; phi2 &gt; phi3</text>
<text x="135" y="232" font-family="Arial,sans-serif" font-size="5" fill="#555" text-anchor="middle">E перпендикулярна поверхностям</text>
<!-- Formulas -->
<rect x="270" y="60" width="210" height="170" rx="6" fill="white" stroke="#E53935" stroke-width="1.5"/>
<text x="375" y="78" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle" font-weight="bold">Формулы</text>
<line x1="280" y1="85" x2="470" y2="85" stroke="#E53935" stroke-width="0.5"/>
<text x="375" y="102" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Потенциал точечного заряда:</text>
<text x="375" y="118" font-family="Arial,sans-serif" font-size="10" fill="#7B1FA2" text-anchor="middle" font-weight="bold">phi = k*q/r</text>
<line x1="280" y1="128" x2="470" y2="128" stroke="#E53935" stroke-width="0.5"/>
<text x="375" y="145" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Напряжение:</text>
<text x="375" y="161" font-family="Arial,sans-serif" font-size="10" fill="#E65100" text-anchor="middle" font-weight="bold">U = phi1 - phi2</text>
<line x1="280" y1="170" x2="470" y2="170" stroke="#E53935" stroke-width="0.5"/>
<text x="375" y="187" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle" font-weight="bold">Работа поля:</text>
<text x="375" y="203" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32" text-anchor="middle" font-weight="bold">A = q*U = q*(phi1-phi2)</text>
<text x="375" y="220" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">A не зависит от траектории!</text>
<!-- Key relation -->
<rect x="40" y="245" width="420" height="55" rx="6" fill="white" stroke="#7B1FA2" stroke-width="1.5"/>
<text x="250" y="263" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Связь E и U</text>
<text x="250" y="281" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">E = U/d (однородное поле)</text>
<text x="250" y="294" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">d — расстояние между эквипотенциальными поверхностями</text>
'''+ftr

# 62: Проводники и диэлектрики в электрическом поле
svg62=hdr("Проводники и диэлектрики в электрическом поле",62)+f'''
<!-- Conductor in field -->
<rect x="20" y="60" width="225" height="155" rx="6" fill="white" stroke="#E53935" stroke-width="1.5"/>
<text x="132" y="78" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle" font-weight="bold">Проводник в поле E</text>
<!-- External field arrows -->
<line x1="30" y1="130" x2="60" y2="130" stroke="#7B1FA2" stroke-width="1.5"/>
<polygon points="60,130 54,127 54,133" fill="#7B1FA2"/>
<line x1="30" y1="145" x2="60" y2="145" stroke="#7B1FA2" stroke-width="1.5"/>
<polygon points="60,145 54,142 54,148" fill="#7B1FA2"/>
<line x1="30" y1="160" x2="60" y2="160" stroke="#7B1FA2" stroke-width="1.5"/>
<polygon points="60,160 54,157 54,163" fill="#7B1FA2"/>
<text x="30" y="120" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2">E0</text>
<!-- Conductor body -->
<rect x="70" y="105" width="90" height="80" rx="5" fill="#CFD8DC" stroke="#333" stroke-width="1.5"/>
<text x="115" y="150" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">Проводник</text>
<!-- Induced charges -->
<text x="76" y="125" font-family="Arial,sans-serif" font-size="8" fill="#E53935" font-weight="bold">+</text>
<text x="76" y="140" font-family="Arial,sans-serif" font-size="8" fill="#E53935" font-weight="bold">+</text>
<text x="76" y="155" font-family="Arial,sans-serif" font-size="8" fill="#E53935" font-weight="bold">+</text>
<text x="150" y="125" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" font-weight="bold">-</text>
<text x="150" y="140" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" font-weight="bold">-</text>
<text x="150" y="155" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" font-weight="bold">-</text>
<!-- E=0 inside -->
<text x="115" y="170" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">E = 0</text>
<!-- Field lines after -->
<line x1="160" y1="130" x2="200" y2="130" stroke="#7B1FA2" stroke-width="1.5"/>
<polygon points="200,130 194,127 194,133" fill="#7B1FA2"/>
<line x1="160" y1="145" x2="200" y2="145" stroke="#7B1FA2" stroke-width="1.5"/>
<polygon points="200,145 194,142 194,148" fill="#7B1FA2"/>
<line x1="160" y1="160" x2="200" y2="160" stroke="#7B1FA2" stroke-width="1.5"/>
<polygon points="200,160 194,157 194,163" fill="#7B1FA2"/>
<!-- Dielectric in field -->
<rect x="260" y="60" width="225" height="155" rx="6" fill="white" stroke="#1565C0" stroke-width="1.5"/>
<text x="372" y="78" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">Диэлектрик в поле E</text>
<!-- External field -->
<line x1="270" y1="130" x2="300" y2="130" stroke="#7B1FA2" stroke-width="1.5"/>
<polygon points="300,130 294,127 294,133" fill="#7B1FA2"/>
<line x1="270" y1="145" x2="300" y2="145" stroke="#7B1FA2" stroke-width="1.5"/>
<polygon points="300,145 294,142 294,148" fill="#7B1FA2"/>
<line x1="270" y1="160" x2="300" y2="160" stroke="#7B1FA2" stroke-width="1.5"/>
<polygon points="300,160 294,157 294,163" fill="#7B1FA2"/>
<text x="270" y="120" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2">E0</text>
<!-- Dielectric body -->
<rect x="310" y="105" width="90" height="80" rx="5" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/>
<text x="355" y="150" font-family="Arial,sans-serif" font-size="6" fill="#F9A825" text-anchor="middle">Диэлектрик</text>
<!-- Polarized dipoles -->
<text x="325" y="125" font-family="Arial,sans-serif" font-size="6" fill="#E53935">+-</text>
<text x="345" y="125" font-family="Arial,sans-serif" font-size="6" fill="#E53935">+-</text>
<text x="365" y="125" font-family="Arial,sans-serif" font-size="6" fill="#E53935">+-</text>
<text x="325" y="145" font-family="Arial,sans-serif" font-size="6" fill="#E53935">+-</text>
<text x="345" y="145" font-family="Arial,sans-serif" font-size="6" fill="#E53935">+-</text>
<text x="365" y="145" font-family="Arial,sans-serif" font-size="6" fill="#E53935">+-</text>
<text x="325" y="165" font-family="Arial,sans-serif" font-size="6" fill="#E53935">+-</text>
<text x="345" y="165" font-family="Arial,sans-serif" font-size="6" fill="#E53935">+-</text>
<text x="365" y="165" font-family="Arial,sans-serif" font-size="6" fill="#E53935">+-</text>
<!-- Weakened field after -->
<line x1="400" y1="135" x2="440" y2="135" stroke="#7B1FA2" stroke-width="1"/>
<polygon points="440,135 434,132 434,138" fill="#7B1FA2"/>
<line x1="400" y1="155" x2="440" y2="155" stroke="#7B1FA2" stroke-width="1"/>
<polygon points="440,155 434,152 434,158" fill="#7B1FA2"/>
<text x="430" y="120" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2">E = E0/eps</text>
<!-- Formulas -->
<rect x="30" y="230" width="210" height="60" rx="5" fill="white" stroke="#E53935" stroke-width="1.2"/>
<text x="135" y="248" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle" font-weight="bold">Проводник</text>
<text x="135" y="264" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">E = 0 внутри</text>
<text x="135" y="278" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">phi = const (эквипотенциален)</text>
<rect x="260" y="230" width="210" height="60" rx="5" fill="white" stroke="#1565C0" stroke-width="1.2"/>
<text x="365" y="248" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">Диэлектрик</text>
<text x="365" y="264" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">E = E0/epsilon (ослабляет)</text>
<text x="365" y="278" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">epsilon — диэлектрическая проницаемость</text>
'''+ftr

# 63: Электрическая ёмкость. Конденсаторы
svg63=hdr("Электрическая ёмкость. Конденсаторы",63)+f'''
<!-- Parallel plate capacitor -->
<rect x="20" y="60" width="250" height="180" rx="6" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="145" y="78" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Плоский конденсатор</text>
<!-- Left plate -->
<rect x="85" y="95" width="10" height="90" rx="2" fill="#E53935" opacity="0.7" stroke="#E53935" stroke-width="1.5"/>
<text x="75" y="90" font-family="Arial,sans-serif" font-size="8" fill="#E53935" text-anchor="middle" font-weight="bold">+q</text>
<!-- Charges on left plate -->
<text x="90" y="112" font-family="Arial,sans-serif" font-size="7" fill="white" font-weight="bold">+</text>
<text x="90" y="125" font-family="Arial,sans-serif" font-size="7" fill="white" font-weight="bold">+</text>
<text x="90" y="138" font-family="Arial,sans-serif" font-size="7" fill="white" font-weight="bold">+</text>
<text x="90" y="151" font-family="Arial,sans-serif" font-size="7" fill="white" font-weight="bold">+</text>
<text x="90" y="164" font-family="Arial,sans-serif" font-size="7" fill="white" font-weight="bold">+</text>
<!-- Right plate -->
<rect x="175" y="95" width="10" height="90" rx="2" fill="#1565C0" opacity="0.7" stroke="#1565C0" stroke-width="1.5"/>
<text x="195" y="90" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" text-anchor="middle" font-weight="bold">-q</text>
<text x="180" y="112" font-family="Arial,sans-serif" font-size="7" fill="white" font-weight="bold">-</text>
<text x="180" y="125" font-family="Arial,sans-serif" font-size="7" fill="white" font-weight="bold">-</text>
<text x="180" y="138" font-family="Arial,sans-serif" font-size="7" fill="white" font-weight="bold">-</text>
<text x="180" y="151" font-family="Arial,sans-serif" font-size="7" fill="white" font-weight="bold">-</text>
<text x="180" y="164" font-family="Arial,sans-serif" font-size="7" fill="white" font-weight="bold">-</text>
<!-- Field lines between plates -->
<line x1="97" y1="110" x2="173" y2="110" stroke="#7B1FA2" stroke-width="0.8"/>
<polygon points="173,110 167,107 167,113" fill="#7B1FA2"/>
<line x1="97" y1="130" x2="173" y2="130" stroke="#7B1FA2" stroke-width="0.8"/>
<polygon points="173,130 167,127 167,133" fill="#7B1FA2"/>
<line x1="97" y1="150" x2="173" y2="150" stroke="#7B1FA2" stroke-width="0.8"/>
<polygon points="173,150 167,147 167,153" fill="#7B1FA2"/>
<line x1="97" y1="170" x2="173" y2="170" stroke="#7B1FA2" stroke-width="0.8"/>
<polygon points="173,170 167,167 167,173" fill="#7B1FA2"/>
<text x="135" y="145" font-family="Arial,sans-serif" font-size="6" fill="#7B1FA2" text-anchor="middle">E</text>
<!-- d label -->
<line x1="95" y1="195" x2="95" y2="205" stroke="#333" stroke-width="0.5"/>
<line x1="175" y1="195" x2="175" y2="205" stroke="#333" stroke-width="0.5"/>
<line x1="95" y1="200" x2="175" y2="200" stroke="#333" stroke-width="1"/>
<text x="135" y="212" font-family="Arial,sans-serif" font-size="7" fill="#333" text-anchor="middle">d</text>
<!-- S label -->
<text x="135" y="230" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">S — площадь пластин</text>
<!-- Formulas -->
<rect x="290" y="60" width="190" height="110" rx="6" fill="white" stroke="#E53935" stroke-width="1.5"/>
<text x="385" y="78" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle" font-weight="bold">Формула ёмкости</text>
<line x1="300" y1="85" x2="470" y2="85" stroke="#E53935" stroke-width="0.5"/>
<text x="385" y="105" font-family="Arial,sans-serif" font-size="10" fill="#E53935" text-anchor="middle" font-weight="bold">C = q/U</text>
<text x="385" y="122" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">1 Фарад (Ф) = Кл/В</text>
<line x1="300" y1="130" x2="470" y2="130" stroke="#E53935" stroke-width="0.5"/>
<text x="385" y="148" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Плоский конденсатор:</text>
<text x="385" y="163" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" text-anchor="middle" font-weight="bold">C = eps*eps0*S/d</text>
<!-- Types of capacitors -->
<rect x="290" y="185" width="190" height="80" rx="6" fill="white" stroke="#2E7D32" stroke-width="1.2"/>
<text x="385" y="203" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Типы конденсаторов</text>
<line x1="300" y1="208" x2="470" y2="208" stroke="#2E7D32" stroke-width="0.5"/>
<text x="385" y="223" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Плоские | Сферические</text>
<text x="385" y="236" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Цилиндрические</text>
<text x="385" y="252" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">epsilon: воздух=1, стекло=5-10</text>
<text x="385" y="262" font-family="Arial,sans-serif" font-size="6" fill="#E65100" text-anchor="middle">eps0 = 8.85*10^-12 Ф/м</text>
'''+ftr

# 64: Энергия электрического поля
svg64=hdr("Энергия электрического поля",64)+f'''
<!-- Central energy formulas -->
<rect x="30" y="60" width="200" height="80" rx="6" fill="white" stroke="#E53935" stroke-width="1.5"/>
<text x="130" y="78" font-family="Arial,sans-serif" font-size="7" fill="#E53935" text-anchor="middle" font-weight="bold">Энергия конденсатора</text>
<line x1="40" y1="83" x2="220" y2="83" stroke="#E53935" stroke-width="0.5"/>
<text x="130" y="100" font-family="Arial,sans-serif" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">W = C*U^2 / 2</text>
<text x="130" y="118" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" text-anchor="middle" font-weight="bold">W = q^2 / (2*C)</text>
<text x="130" y="133" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">W = q*U / 2</text>
<!-- Third formula -->
<rect x="260" y="60" width="210" height="80" rx="6" fill="white" stroke="#1565C0" stroke-width="1.5"/>
<text x="365" y="78" font-family="Arial,sans-serif" font-size="7" fill="#1565C0" text-anchor="middle" font-weight="bold">Через поле</text>
<line x1="270" y1="83" x2="460" y2="83" stroke="#1565C0" stroke-width="0.5"/>
<text x="365" y="102" font-family="Arial,sans-serif" font-size="9" fill="#333" text-anchor="middle" font-weight="bold">W = eps*eps0*E^2*S*d / 2</text>
<line x1="270" y1="112" x2="460" y2="112" stroke="#1565C0" stroke-width="0.5"/>
<text x="365" y="130" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Объёмная плотность энергии:</text>
<text x="365" y="140" font-family="Arial,sans-serif" font-size="9" fill="#7B1FA2" text-anchor="middle" font-weight="bold">w = W/V = eps*eps0*E^2/2</text>
<!-- Energy diagram - capacitor with energy -->
<rect x="30" y="155" width="200" height="100" rx="6" fill="white" stroke="{P}" stroke-width="1.5"/>
<text x="130" y="173" font-family="Arial,sans-serif" font-size="7" fill="{P}" text-anchor="middle" font-weight="bold">Энергия в конденсаторе</text>
<!-- Capacitor symbol -->
<line x1="60" y1="195" x2="60" y2="225" stroke="#E53935" stroke-width="2.5"/>
<line x1="80" y1="195" x2="80" y2="225" stroke="#1565C0" stroke-width="2.5"/>
<!-- Energy glow -->
<rect x="60" y="195" width="20" height="30" fill="#FFD600" opacity="0.3"/>
<text x="70" y="214" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle">W</text>
<!-- Wires -->
<line x1="40" y1="210" x2="60" y2="210" stroke="#333" stroke-width="1"/>
<line x1="80" y1="210" x2="110" y2="210" stroke="#333" stroke-width="1"/>
<!-- + and - labels -->
<text x="55" y="190" font-family="Arial,sans-serif" font-size="8" fill="#E53935" font-weight="bold">+</text>
<text x="82" y="190" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" font-weight="bold">-</text>
<!-- Key concept -->
<text x="130" y="243" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Энергия запасена в электрическом поле</text>
<!-- Connections box -->
<rect x="260" y="155" width="210" height="100" rx="6" fill="white" stroke="#2E7D32" stroke-width="1.5"/>
<text x="365" y="173" font-family="Arial,sans-serif" font-size="7" fill="#2E7D32" text-anchor="middle" font-weight="bold">Связь формул</text>
<line x1="270" y1="178" x2="460" y2="178" stroke="#2E7D32" stroke-width="0.5"/>
<text x="365" y="196" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">C = q/U → q = C*U</text>
<text x="365" y="212" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">W = q*U/2 = C*U^2/2 = q^2/(2C)</text>
<line x1="270" y1="222" x2="460" y2="222" stroke="#2E7D32" stroke-width="0.5"/>
<text x="365" y="238" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle">W — работа по зарядке конденсатора</text>
<text x="365" y="249" font-family="Arial,sans-serif" font-size="6" fill="#FF6F00" text-anchor="middle">Выделяется при разрядке</text>
<!-- Unit box -->
<rect x="80" y="270" width="340" height="40" rx="5" fill="white" stroke="#7B1FA2" stroke-width="1.2"/>
<text x="250" y="286" font-family="Arial,sans-serif" font-size="7" fill="#7B1FA2" text-anchor="middle" font-weight="bold">Единицы измерения</text>
<text x="250" y="302" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">W: Джоуль (Дж) | w: Дж/м^3 | E: В/м | C: Фарад (Ф) | eps0 = 8.85*10^-12 Ф/м</text>
'''+ftr

svgs={51:svg51,52:svg52,53:svg53,54:svg54,55:svg55,56:svg56,57:svg57,58:svg58,59:svg59,60:svg60,61:svg61,62:svg62,63:svg63,64:svg64}
for num, content in svgs.items():
    path = os.path.join(OUT, f"lesson{num}.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written lesson{num}.svg")
print(f"Done! {len(svgs)} SVG files written")
